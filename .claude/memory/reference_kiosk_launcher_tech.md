---
name: reference_kiosk_launcher_tech
description: Kiosk Launcher 完整技术方案 — 8大模块拆解 + Android 代码 + AI 工具选型
type: reference
---

## Kiosk Launcher 技术方案（对标商米 Sunmi）

### 概念
Kiosk Launcher = 一个被设为默认桌面的 Android App，接管系统桌面，同时把用户"锁"在允许的操作范围内。最终效果：用户感觉不到这是 Android，就像 ATM 机一样。

### 8 大功能模块

| # | 模块 | 说明 |
|---|------|------|
| 1 | 基础 Launcher | 声明 HOME category 的 Activity，接管桌面 |
| 2 | Kiosk 锁定 | DevicePolicyManager + LockTask 模式，白名单锁定 |
| 3 | DeviceAdminReceiver | 设备管理器，获取系统级控制权的前提 |
| 4 | SystemUI 隐藏 | 隐藏状态栏/导航栏/通知，禁用全局按键 |
| 5 | 开机自启 | BOOT_COMPLETED 广播 → 自动拉起 Launcher |
| 6 | 远程管理 (MDM) | 远程下发白名单/APK升级/重启/擦除 |
| 7 | 崩溃保护 | 全局异常捕获 + 看门狗定时检查 Launcher 存活 |
| 8 | 管理员设置 | 隐蔽入口 + 密码保护，WiFi/白名单/日志管理 |

### 核心技术栈
- **语言**: Kotlin
- **关键 API**: DevicePolicyManager, LockTask, PackageInstaller Session, BOOT_COMPLETED
- **远程管理**: Retrofit + 轮询或 WebSocket/MQTT 长连接
- **最简实现**: 可在 Android Studio 中新建项目，AI 生成 70%+ 代码

### AI 工具选型
| 阶段 | 工具 | 用途 |
|------|------|------|
| 代码生成 | Claude Code / Cursor | Launcher 核心代码、Kiosk 锁定、SystemUI 隐藏 |
| UI 布局 | Claude（描述需求 → XML） | 主界面、设置页布局 |
| 调试 | Claude（贴 Logcat） | 崩溃分析、权限问题、厂商兼容性 |
| 文档 | Claude / Hermes | 技术文档、部署手册 |

### 项目结构（规划）
```
kozen-kiosk-launcher/
├── app/src/main/java/com/kozen/launcher/
│   ├── KioskLauncherActivity.kt      # 主界面
│   ├── KioskDeviceAdminReceiver.kt    # DeviceAdmin
│   ├── BootReceiver.kt               # 开机自启
│   ├── kiosk/
│   │   ├── KioskManager.kt           # LockTask 管理
│   │   ├── SystemUIHider.kt          # UI 隐藏
│   │   └── CrashGuard.kt             # 崩溃保护
│   ├── remote/
│   │   ├── RemoteConfigManager.kt     # MDM 客户端
│   │   └── KozenApiService.kt        # API 接口
│   ├── apps/
│   │   └── AppListAdapter.kt         # 白名单应用列表
│   └── utils/
│       ├── DeviceUtils.kt
│       └── SecurityUtils.kt
└── backend/                          # 远程管理后台（后续）
```

### 关键风险
- 不同厂商 ROM 对 SystemUI 隐藏的支持不一致（华为/小米/原生 Android）
- 静默安装需要系统签名或 root 权限（可用 PackageInstaller Session API 替代）
- DeviceAdmin 可能被用户手动关闭（需要防关闭机制）
