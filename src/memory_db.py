"""长期记忆模块 - SQLite 实现

功能：
1. 用户画像管理（偏好设备、常见问题）
2. 对话历史存储（多轮上下文）
3. 自动案例沉淀（待审核案例）
4. 会话管理（恢复对话）

使用：
    from memory_db import MemoryDB
    db = MemoryDB()

    # 记录消息
    db.save_message(session_id, user_id, role, content, tools_used)

    # 获取对话历史
    history = db.get_session_history(session_id, limit=10)

    # 获取用户画像
    profile = db.get_user_profile(user_id)
"""

import os
import json
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict
from dataclasses import dataclass

# 数据库路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "memory.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "data", "schema.sql")


@dataclass
class UserProfile:
    """用户画像"""
    user_id: str
    nickname: Optional[str] = None
    preferred_devices: List[str] = None
    common_issues: List[str] = None
    skill_level: str = "beginner"
    total_sessions: int = 0
    total_messages: int = 0
    first_seen: str = None
    last_active: str = None

    def to_prompt_context(self) -> str:
        """转成prompt上下文"""
        parts = []
        if self.preferred_devices:
            parts.append(f"常用设备: {', '.join(self.preferred_devices)}")
        if self.common_issues:
            parts.append(f"常见问题: {', '.join(self.common_issues[:3])}")
        if parts:
            return "【用户偏好】" + "; ".join(parts)
        return ""


@dataclass
class Message:
    """消息记录"""
    message_id: int
    session_id: str
    role: str
    content: str
    timestamp: str
    tools_used: Optional[List[str]] = None
    cases_referenced: Optional[List[str]] = None


class MemoryDB:
    """SQLite 记忆数据库"""

    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        """获取数据库连接"""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        """初始化数据库（首次运行创建表）"""
        if not os.path.exists(self.db_path):
            # 首次创建
            conn = self._get_conn()
            if os.path.exists(SCHEMA_PATH):
                with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                    conn.executescript(f.read())
            conn.commit()
            conn.close()
            print(f"[MemoryDB] 数据库已创建: {self.db_path}")

    # ==================== 用户画像 ====================

    def get_user_profile(self, user_id: str) -> Optional[UserProfile]:
        """获取用户画像，不存在返回None"""
        conn = self._get_conn()
        cursor = conn.execute(
            "SELECT * FROM user_profiles WHERE user_id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        return UserProfile(
            user_id=row['user_id'],
            nickname=row['nickname'],
            preferred_devices=json.loads(row['preferred_devices']) if row['preferred_devices'] else [],
            common_issues=json.loads(row['common_issues']) if row['common_issues'] else [],
            skill_level=row['skill_level'],
            total_sessions=row['total_sessions'],
            total_messages=row['total_messages'],
            first_seen=row['first_seen'],
            last_active=row['last_active']
        )

    def create_or_update_user(self, user_id: str, nickname: Optional[str] = None) -> UserProfile:
        """创建或更新用户"""
        conn = self._get_conn()

        # 检查是否存在
        existing = self.get_user_profile(user_id)

        if existing:
            # 更新最后活跃时间
            conn.execute(
                "UPDATE user_profiles SET last_active = CURRENT_TIMESTAMP WHERE user_id = ?",
                (user_id,)
            )
            conn.commit()
            conn.close()
            return existing

        # 创建新用户
        conn.execute(
            """INSERT INTO user_profiles
                (user_id, nickname, preferred_devices, common_issues, skill_level)
                VALUES (?, ?, ?, ?, ?)""",
            (user_id, nickname, '[]', '[]', 'beginner')
        )
        conn.commit()
        conn.close()

        return self.get_user_profile(user_id)

    def update_user_preferences(self, user_id: str,
                                 devices: Optional[List[str]] = None,
                                 issues: Optional[List[str]] = None):
        """更新用户偏好（从对话中自动提取）"""
        conn = self._get_conn()

        if devices:
            conn.execute(
                "UPDATE user_profiles SET preferred_devices = ? WHERE user_id = ?",
                (json.dumps(devices), user_id)
            )

        if issues:
            conn.execute(
                "UPDATE user_profiles SET common_issues = ? WHERE user_id = ?",
                (json.dumps(issues), user_id)
            )

        conn.commit()
        conn.close()

    # ==================== 会话管理 ====================

    def create_session(self, session_id: str, user_id: str, title: Optional[str] = None) -> str:
        """创建新会话（如果已存在则返回现有会话ID）"""
        conn = self._get_conn()

        # 先检查会话是否已存在
        cursor = conn.execute(
            "SELECT session_id FROM sessions WHERE session_id = ?",
            (session_id,)
        )
        if cursor.fetchone():
            # 已存在，只更新最后活跃时间
            conn.execute(
                "UPDATE sessions SET updated_at = CURRENT_TIMESTAMP WHERE session_id = ?",
                (session_id,)
            )
            conn.commit()
            conn.close()
            return session_id

        # 关闭该用户的其他活跃会话
        conn.execute(
            "UPDATE sessions SET status = 'closed' WHERE user_id = ? AND status = 'active'",
            (user_id,)
        )

        # 创建新会话
        conn.execute(
            "INSERT INTO sessions (session_id, user_id, title) VALUES (?, ?, ?)",
            (session_id, user_id, title or "新对话")
        )

        # 更新用户会话数
        conn.execute(
            "UPDATE user_profiles SET total_sessions = total_sessions + 1 WHERE user_id = ?",
            (user_id,)
        )

        conn.commit()
        conn.close()
        return session_id

    def get_active_session(self, user_id: str) -> Optional[Dict]:
        """获取用户当前活跃会话"""
        conn = self._get_conn()
        cursor = conn.execute(
            "SELECT * FROM sessions WHERE user_id = ? AND status = 'active' ORDER BY updated_at DESC LIMIT 1",
            (user_id,)
        )
        row = cursor.fetchone()
        conn.close()

        if row:
            return dict(row)
        return None

    def update_session_context(self, session_id: str, device_context: str):
        """更新会话的设备上下文（如检测用户在问D0551）"""
        conn = self._get_conn()
        conn.execute(
            "UPDATE sessions SET device_context = ?, updated_at = CURRENT_TIMESTAMP WHERE session_id = ?",
            (device_context, session_id)
        )
        conn.commit()
        conn.close()

    # ==================== 消息记录 ====================

    def save_message(self, session_id: str, user_id: str, role: str,
                     content: str, tools_used: Optional[List[str]] = None,
                     cases_referenced: Optional[List[str]] = None,
                     latency_ms: Optional[int] = None) -> int:
        """保存消息，返回message_id"""
        conn = self._get_conn()

        cursor = conn.execute(
            """INSERT INTO messages
                (session_id, user_id, role, content, tools_used, cases_referenced, latency_ms)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (session_id, user_id, role, content,
             json.dumps(tools_used) if tools_used else None,
             json.dumps(cases_referenced) if cases_referenced else None,
             latency_ms)
        )

        message_id = cursor.lastrowid

        # 更新用户消息数
        if role == 'user':
            conn.execute(
                "UPDATE user_profiles SET total_messages = total_messages + 1 WHERE user_id = ?",
                (user_id,)
            )

        # 更新会话时间
        conn.execute(
            "UPDATE sessions SET updated_at = CURRENT_TIMESTAMP WHERE session_id = ?",
            (session_id,)
        )

        conn.commit()
        conn.close()
        return message_id

    def get_session_history(self, session_id: str, limit: int = 10) -> List[Message]:
        """获取会话历史（用于多轮对话上下文）"""
        conn = self._get_conn()
        cursor = conn.execute(
            """SELECT * FROM messages
               WHERE session_id = ?
               ORDER BY timestamp DESC
               LIMIT ?""",
            (session_id, limit)
        )

        rows = cursor.fetchall()
        conn.close()

        messages = []
        for row in reversed(rows):  # 倒序转回正序
            messages.append(Message(
                message_id=row['message_id'],
                session_id=row['session_id'],
                role=row['role'],
                content=row['content'],
                timestamp=row['timestamp'],
                tools_used=json.loads(row['tools_used']) if row['tools_used'] else None,
                cases_referenced=json.loads(row['cases_referenced']) if row['cases_referenced'] else None
            ))

        return messages

    def get_recent_messages(self, user_id: str, limit: int = 20) -> List[Message]:
        """获取用户最近的所有消息（跨会话）"""
        conn = self._get_conn()
        cursor = conn.execute(
            """SELECT * FROM messages
               WHERE user_id = ?
               ORDER BY timestamp DESC
               LIMIT ?""",
            (user_id, limit)
        )

        rows = cursor.fetchall()
        conn.close()

        return [Message(
            message_id=row['message_id'],
            session_id=row['session_id'],
            role=row['role'],
            content=row['content'],
            timestamp=row['timestamp']
        ) for row in rows]

    # ==================== 自动案例沉淀 ====================

    def save_pending_case(self, session_id: str, user_id: str,
                          query: str, answer: str,
                          source_message_id: int) -> int:
        """保存待审核案例"""
        conn = self._get_conn()
        cursor = conn.execute(
            """INSERT INTO pending_cases
                (session_id, user_id, query, answer, source_message_id)
                VALUES (?, ?, ?, ?, ?)""",
            (session_id, user_id, query, answer, source_message_id)
        )
        case_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return case_id

    def get_pending_cases(self, limit: int = 10) -> List[Dict]:
        """获取待审核案例列表"""
        conn = self._get_conn()
        cursor = conn.execute(
            """SELECT * FROM pending_cases
               WHERE reviewed = FALSE
               ORDER BY extracted_at DESC
               LIMIT ?""",
            (limit,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def approve_case(self, pending_case_id: int, final_case_id: str,
                     reviewer_notes: Optional[str] = None):
        """审核通过案例"""
        conn = self._get_conn()
        conn.execute(
            """UPDATE pending_cases
               SET reviewed = TRUE, approved = TRUE,
                   final_case_id = ?, reviewer_notes = ?
               WHERE case_id = ?""",
            (final_case_id, reviewer_notes, pending_case_id)
        )
        conn.commit()
        conn.close()

    # ==================== 统计与分析 ====================

    def get_stats(self, user_id: Optional[str] = None) -> Dict:
        """获取统计信息"""
        conn = self._get_conn()

        if user_id:
            # 单个用户统计
            cursor = conn.execute(
                """SELECT
                    COUNT(DISTINCT session_id) as total_sessions,
                    COUNT(*) as total_messages,
                    AVG(latency_ms) as avg_latency
                   FROM messages WHERE user_id = ?""",
                (user_id,)
            )
        else:
            # 全局统计
            cursor = conn.execute(
                """SELECT
                    COUNT(DISTINCT user_id) as total_users,
                    COUNT(DISTINCT session_id) as total_sessions,
                    COUNT(*) as total_messages
                   FROM messages"""
            )

        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else {}

    # ==================== 缓存管理 ====================

    def clear_all_caches(self):
        """清除所有检索缓存（案例更新后调用）"""
        try:
            # 清除案例检索缓存
            from memory import clear_search_cache as clear_case_cache
            clear_case_cache()
        except Exception as e:
            print(f"[Cache] 清除案例缓存失败: {e}")

        try:
            # 清除文档检索缓存
            from retrieve import clear_search_cache as clear_doc_cache
            clear_doc_cache()
        except Exception as e:
            print(f"[Cache] 清除文档缓存失败: {e}")

        print("[Cache] 所有检索缓存已清除")

    def approve_and_clear_cache(self, pending_case_id: int, final_case_id: str,
                                 reviewer_notes: Optional[str] = None):
        """审核通过案例并清除缓存（确保新案例立即生效）"""
        self.approve_case(pending_case_id, final_case_id, reviewer_notes)
        self.clear_all_caches()
        print(f"[Cache] 案例 {final_case_id} 已审核通过，缓存已刷新")


# 全局实例（模块级单例）
_memory_db = None

def get_memory_db() -> MemoryDB:
    """获取全局记忆数据库实例"""
    global _memory_db
    if _memory_db is None:
        _memory_db = MemoryDB()
    return _memory_db


def clear_all_caches():
    """便捷函数：清除所有缓存"""
    db = get_memory_db()
    db.clear_all_caches()
