-- Nebullar AI Assistant - SQLite 数据库 Schema
-- 长期记忆：用户画像 + 对话历史 + 自动案例沉淀

-- 用户画像表
CREATE TABLE IF NOT EXISTS user_profiles (
    user_id TEXT PRIMARY KEY,
    nickname TEXT,
    -- 用户偏好（JSON格式）
    preferred_devices TEXT,  -- ["D0551", "D0552", "P18"]
    common_issues TEXT,      -- ["刷机失败", "写号", "OTA升级"]
    skill_level TEXT,        -- beginner/intermediate/advanced
    -- 统计信息
    total_sessions INTEGER DEFAULT 0,
    total_messages INTEGER DEFAULT 0,
    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 会话表（每次打开网页为一个会话）
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    title TEXT,  -- 会话主题（自动生成）
    device_context TEXT,  -- 当前会话讨论的设备
    status TEXT DEFAULT 'active',  -- active/closed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_profiles(user_id)
);

-- 消息表（对话历史）
CREATE TABLE IF NOT EXISTS messages (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    role TEXT NOT NULL,  -- user/assistant/system
    content TEXT NOT NULL,
    -- 引用信息（用于溯源）
    tools_used TEXT,     -- JSON ["search_cases", "search_docs"]
    cases_referenced TEXT,  -- JSON ["case_xxx", "case_yyy"]
    latency_ms INTEGER,  -- 响应耗时
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id),
    FOREIGN KEY (user_id) REFERENCES user_profiles(user_id)
);

-- 自动沉淀的案例表（待审核）
CREATE TABLE IF NOT EXISTS pending_cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    user_id TEXT,
    -- 案例内容
    query TEXT NOT NULL,      -- 用户问题
    answer TEXT NOT NULL,     -- AI回答
    -- 元数据
    source_message_id INTEGER,
    extracted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reviewed BOOLEAN DEFAULT FALSE,  -- 是否已人工审核
    approved BOOLEAN DEFAULT NULL,   -- 审核结果
    reviewer_notes TEXT,
    -- 关联到正式案例表
    final_case_id TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- 用户反馈表（用于改进）
CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    user_id TEXT NOT NULL,
    rating INTEGER,  -- 1-5星
    comment TEXT,    -- 文字反馈
    issue_type TEXT, -- wrong_answer/missing_info/too_slow/other
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 索引（加速查询）
CREATE INDEX IF NOT EXISTS idx_messages_session ON messages(session_id);
CREATE INDEX IF NOT EXISTS idx_messages_user ON messages(user_id);
CREATE INDEX IF NOT EXISTS idx_messages_timestamp ON messages(timestamp);
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_updated ON sessions(updated_at);
