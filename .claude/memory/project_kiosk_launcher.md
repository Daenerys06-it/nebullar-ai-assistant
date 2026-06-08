---
name: project_kiosk_launcher
description: KOZEN Kiosk Launcher — 定制 Android 桌面/系统，对标商米 Sunmi OS 体验
type: project
---

## KOZEN Kiosk Launcher 项目

用户 leader 提出新需求：给公司的 Android 金融终端设备"套一层 OS Launcher"，让客户体验对标 **商米（Sunmi）**，不再是原生 Android 的粗糙感觉。

**Why**: 公司给客户提供的机器跑的是原生 Android（AOSP），用户能看见系统设置、通知栏、多任务等，体验像"开发板"而不是"专业金融终端"。商米等竞品通过深度定制 Launcher 屏蔽了 Android 感，开机即品牌体验。

**How to apply**:
- 这是一个全新的 Android 项目（非 Python），与 [[project_kozen_ai_assistant]] 是独立的工作流
- 技术路线：Launcher App + DeviceAdmin + LockTask Kiosk 模式（Google 官方方案）
- 用户需要先做技术 POC，然后拿方案跟 leader 讨论
- AI 辅助开发是 leader 明确提出的方向——用户可以通过这个项目实践 AI 辅助 Android 开发
- 用户是 FAE 角色，但 leader 希望 ta 也参与这个项目的开发（作为 AI 能力训练）

## 当前进展（2026-06-08）

- 用户已理解 Kiosk Launcher 概念（对标商米模式）
- 已完成详细技术方案梳理（8 大模块，含完整代码示例）
- 技术方案已存档到 [[reference_kiosk_launcher_tech]]
- 下一步：用户拿方案跟 leader 汇报 → 确定是否启动 POC

## 与 AI 助手的协作
- Kiosk Launcher 是独立 Android 项目，与 Python AI 助手项目无代码耦合
- 但两个项目都涉及"AI 辅助开发"理念——用户可以把在 AI 助手项目中学到的 AI 工具使用经验迁移过来
