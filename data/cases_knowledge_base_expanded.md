# Nebullar FAE 技术支持知识库（扩展版）

> 本文档包含26条FAE技术支持案例，已扩展口语化表达和同义词，便于模糊匹配。
> 总案例数：26条 | 覆盖模块：刷机/写号/adb/设备信息/资源管理

---

## 【案例1】case_adb_device_not_found_debugging_off

**所属产品**：terminal_device  
**功能模块**：adb_connection  
**记录日期**：2026-06-15  
**预估耗时**：5分钟

### 问题描述（原始）
使用 ADB 将设备与电脑连接后，执行 adb devices 查询不到设备，或电脑侧没有识别到可调试设备。常见用户说法包括：adb 看不到设备、adb devices 没有设备、电脑连不上设备、设备无法被 adb 识别。

### 扩展检索关键词
识别不到, 连接失败, adb工具, 连不上, POS机, 终端, Android调试, 调试桥, adb连接, 连不上电脑, 刷卡机, 检测不到, 机器, 找不到设备, 连接不上

### 根本原因
设备未开启开发者模式，或已经进入开发者模式但未打开 USB debugging / 调试开关，导致 ADB 没有调试授权入口。

### 详细解决方案
在设备系统设置中连续点击系统版本号 7 次以上，进入开发者模式；返回设置页进入开发者选项，打开 USB debugging / debugging 调试开关；重新插拔 USB 线后，在设备弹窗中允许当前电脑进行 USB 调试；再执行 adb devices 确认设备是否变为 device 状态。

### 标签
adb, adb devices, 设备连接, 电脑识别不到设备, 开发者模式, USB debugging, debugging, 调试开关, Terminal Manager SDK

---

## 【案例2】case_ota_flash_send_da_fail_need_format_refresh

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-06-22  
**预估耗时**：10分钟

### 问题描述（原始）
刷 OTA 版本包时直接刷写，出现 STATUS_BROM_CMD_SEND_DA_FAIL (0xC0060003) 报错，刷机失败。常见说法：刷OTA报错、刷版本包失败、send DA fail、0xC0060003、刷机刷不进去、刷不进固件。

### 扩展检索关键词
出错, flash, 烧写, 失败, 刷版本, 提示, 刷写, 烧录, 升级固件, 刷固件, 重装系统, 报, 异常, 报错, 报错信息

### 根本原因
刷写前没有先让设备初始化：软件 Format 里的自动刷新 / 整机刷新未开启，设备未完成初始化，导致 DA（Download Agent）下发失败。

### 详细解决方案
先在软件 Format 中开启自动刷新 / 整机刷新，让设备先初始化；等初始化完成后，再刷写对应版本的 OTA 版本包，即可正常烧录。

### 标签
OTA, 刷机, 版本包, Format, 自动刷新, 整机刷新, 初始化, STATUS_BROM_CMD_SEND_DA_FAIL, 0xC0060003, DA, Download Agent, send DA fail, 刷写失败, terminal

---

## 【案例3】case_d0552_play_integrity_strong_fail_vending_update

**所属产品**：terminal_device  
**功能模块**：play_integrity  
**记录日期**：2026-06-22  
**预估耗时**：5分钟

### 问题描述（原始）
D0552 双屏机器做 API check（Play Integrity）时，strong integrity 这项不通过（basic / device / strong 三项里 strong 过不了）。常见说法：strong integrity 不过、integrity check 失败、API check 不通过、双屏机 strong 过不了、D0552 strong integrity fail。

### 扩展检索关键词


### 根本原因
Google Play 商店（com.android.vending）发生自动更新，导致 Play Integrity 的 strong integrity 校验不通过。

### 详细解决方案
执行 adb shell cmd package uninstall-system-updates com.android.vending 卸载 Play 商店的系统更新（回退到出厂版本），再重新做 API check，basic / device / strong 三项即可全部通过。

### 标签
D0552, 双屏, 双屏机, Play Integrity, strong integrity, integrity check, API check, Google Play, com.android.vending, 商店自动更新, uninstall-system-updates, adb, terminal

---

## 【案例4】case_p18_flash_data_mux_timeout_low_battery

**所属产品**：terminal_device  
**功能模块**：firmware_flash  
**记录日期**：2026-06-24  
**预估耗时**：30分钟

### 问题描述（原始）
P18 设备刷机时报错 data_mux receive timeout or canceled，刷机中断/失败。常见说法：P18 刷机报 data_mux、data mux receive timeout、刷机超时被取消、P18 刷不进去。

### 扩展检索关键词
timeout, 刷版本, 报, 刷固件, 报错, 机器, 出错, flash, hang住, 终端, 烧写, 失败, 刷写, 升级固件, 重装系统

### 根本原因
P18 设备电量不足，刷机过程中 data_mux 通信超时或被取消。

### 详细解决方案
先给 P18 充电一段时间，待电量充足后再重新刷机即可正常完成。

### 标签
P18, 刷机, data_mux, data mux, receive timeout, canceled, 刷机超时, 电量不足, 充电, 固件, terminal

---

## 【案例5】case_p18_flash_data_mux_timeout_low_battery_v2

**所属产品**：terminal_device  
**功能模块**：p18_flash  
**记录日期**：2026-06-23  
**预估耗时**：30分钟

### 问题描述（原始）
P18 设备刷机过程中出现 data_mux receive timeout or canceled 报错，刷机失败或刷机流程中断。常见说法：P18 刷机超时、data_mux timeout、receive timeout、timeout or canceled、刷机刷不进去。

### 扩展检索关键词
timeout, 刷版本, 报, 刷固件, 报错, 机器, 出错, flash, hang住, 终端, 烧写, 失败, 刷写, 升级固件, 重装系统

### 根本原因
P18 设备电量不足，导致刷机过程中通信超时或被取消。

### 详细解决方案
先给 P18 设备充电一段时间，确保电量充足后再重新刷机；通常充一定时间后再次刷机即可恢复。

### 标签
P18, 刷机, 烧录, flash, data_mux, data_mux receive timeout or canceled, receive timeout, timeout or canceled, 电量不足, 低电量, 充电, terminal

---

## 【案例6】case_engineering_mode_87

**所属产品**：terminal_device  
**功能模块**：device_test  
**记录日期**：2026-07-03  
**预估耗时**：5分钟

### 问题描述（原始）
需要测试设备硬件功能，如 WiFi、NFC、触摸屏、屏幕显示、按键、喇叭、以太网、钱箱等，或进入工程模式进行硬件诊断。常见说法：怎么测 wifi、WiFi 测试方法、怎么测 NFC、NFC 测试在哪、屏幕颜色不对、触摸屏不灵、按键没反应、喇叭没声音、以太网连不上、钱箱打不开、工程模式怎么进、*#87# 是什么、工模测试、硬件测试。

### 扩展检索关键词
模式, 点不了, 无响应, 检测不到, 机器, 状态, 找不到设备, 连接失败, 连不上, 终端, 没变化, 点不动, 没反应, 连不上电脑, 刷卡机

### 根本原因
设备支持通过暗码 *#87# 进入工程模式（工模），内含 MM1 测试菜单，手动测试包含：色彩测试、灯测试、触摸屏测试、主屏测试、按键测试、WiFi 测试、单喇叭测试、以太网测试、钱箱测试、NFC A卡测试、NFC B卡测试、Micro USB 测试等硬件检测功能。

### 详细解决方案
1. 在设备拨号界面输入 *#87# 自动进入工程模式；2. 点击【MM1 测试】选项；3. 点击【手动测试】进入测试菜单；4. 选择需要测试的项目：- 色彩：检测屏幕显示颜色是否正常 - 灯：检测指示灯是否正常 - 触摸屏：检测触摸功能是否正常 - 主屏：检测主屏幕显示是否正常 - 按键：检测物理按键是否正常 - WiFi：检测无线网络功能 - 单喇叭：检测喇叭声音是否正常 - 以太网：检测有线网络连接 - 钱箱：检测钱箱开关功能 - NFC A卡：检测 NFC A卡读写 - NFC B卡：检测 NFC B卡读写 - Micro USB：检测 USB 接口功能；5. 按提示完成测试并查看结果。

### 标签
工程模式, 工模, *#87#, MM1 测试, 手动测试, WiFi 测试, NFC 测试, 触摸屏测试, 屏幕测试, 按键测试, 喇叭测试, 以太网测试, 钱箱测试, 硬件测试, 暗码, Terminal Manager SDK

---

## 【案例7】case_ota_scatter_file_invalid_0xC0030001

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-07-03  
**预估耗时**：15分钟

### 问题描述（原始）
刷机时报错 ERROR: STATUS_SCATTER_FILE_INVALID (0xC0030001)，提示 the scatter file format is invalid，或刷机软件提示[HINT]:Please select a valid load or ask for help。常见说法：刷机报错 scatter file 无效、scatter file 格式不对、0xC0030001 错误、刷机包选不了、提示 select valid load。

### 扩展检索关键词
出错, flash, 烧写, 失败, 刷版本, 提示, 刷写, 烧录, 升级固件, 刷固件, 重装系统, 报, 异常, 报错, 报错信息

### 根本原因
刷机包下载不完整或解压过程出错，导致 scatter 文件损坏或格式不正确，刷机软件无法识别该刷机包。

### 详细解决方案
1. 重新下载完整的刷机包，确保下载过程中网络稳定；2. 使用正规解压软件（如 7-Zip、WinRAR）重新解压，避免解压过程损坏文件；3. 解压后检查文件夹中是否有 scatter.txt 或类似命名的文件，且文件大小不为 0KB；4. 在刷机软件中重新选择解压后的刷机包路径；5. 如仍报错，尝试更换下载源或联系研发获取完整的刷机包。

### 标签
OTA, 刷机, scatter file, STATUS_SCATTER_FILE_INVALID, 0xC0030001, 刷机包, 文件格式无效, 下载, 解压, 刷机失败, terminal

---

## 【案例8】case_factory_reset_clear_flag_422754

**所属产品**：terminal_device  
**功能模块**：device_recovery  
**记录日期**：2026-07-03  
**预估耗时**：5分钟

### 问题描述（原始）
设备已经恢复出厂设置，想要回退到恢复之前的状态，或误操作恢复出厂后想找回数据。常见说法：恢复出厂设置了能恢复吗、怎么回到恢复之前、误点了恢复出厂、数据能找回吗、*#422754# 是什么。

### 扩展检索关键词
POS机, 终端, 刷卡机, 机器, 硬件

### 根本原因
设备支持通过暗码 *#422754# 访问恢复出厂设置的标志位，将其设置为 clear 状态可以回退恢复操作，让设备回到恢复前的状态。

### 详细解决方案
1. 在设备拨号界面输入暗码 *#422754#；2. 在弹出的界面中找到恢复出厂设置的标志位选项；3. 将标志位设置为 clear 状态；4. 点击确认按钮；5. 重启设备，设备将回到恢复出厂设置之前的状态。

### 标签
恢复出厂设置, factory reset, *#422754#, 暗码, 数据恢复, 回退, 标志位, clear, Terminal Manager SDK, device

---

## 【案例9】case_v5_flash_tool_firmware_upgrade

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-07-03  
**预估耗时**：10分钟

### 问题描述（原始）
需要使用 SP Flash Tool V5 进行固件升级/刷机，不知道具体操作步骤，或刷机工具使用方法。适用于 D0551、D0552 等设备的正常刷机（Firmware Upgrade 模式，不需要格式化）。常见说法：怎么刷机、V5 刷机工具怎么用、flash tool 怎么用、固件升级步骤、怎么进刷机模式、刷机工具配置、D0551 怎么刷机、D0552 怎么刷机、D5 刷机步骤、正常刷机、Firmware Upgrade 怎么用。

### 扩展检索关键词
升版本, 模式, 刷到, 刷版本, 刷固件, 机器, 状态, flash, 终端, 烧写, 刷写, 升级固件, 重装系统, 更新到, 升到

### 根本原因
需要使用 SP Flash Tool V5 工具进行固件升级，该工具适用于 D 系列（如 D0551、D0552）机器。使用 Firmware Upgrade 模式进行正常刷机，不需要先格式化。

### 详细解决方案
【前置准备】首次使用需安装驱动（只需做一次）：双击运行 DriverInstall.exe 安装刷机驱动，然后下载对应的刷机软件。

【适用范围】D 系列（D0551、D0552 等）机器

【刷机方式】Firmware Upgrade（正常刷机，无需格式化）

操作步骤：
1. 解压 SP_Flash_Tool_V5 文件夹，打开 flash_tool.exe
2. 点击左上角 File 菜单 → Options，设置语言为 English
3. 进入 Download 页面，第一行 Download DA 点击 Choose，选择刷机包文件夹中的 MTK_AllInOne_DA.bin
4. 第二行配置文件（scatter file）点击 Choose，选择文件夹中的 .txt 文件
5. 选择 Firmware Upgrade 模式（正常刷机，不需要格式化）
6. USB 线先连接设备（不接电源线），点击 Download 按钮，然后再将 USB 另一端插入电脑（防止提前连接进入充电模式）
7. 等待刷机进度完成，显示成功即可

【注意】这是正常刷机步骤（Firmware Upgrade），不是格式化刷机。如果刷机失败或需要清空数据，才需要使用 Format 格式化刷机。

### 标签
V5, SP Flash Tool, 刷机, 固件升级, D系列, D0551, D0552, D5, flash_tool, MTK_AllInOne_DA, scatter file, Firmware Upgrade, 正常刷机, 不需要格式化, OTA, 刷机工具, USB 连接顺序, terminal

---

## 【案例10】case_p18_k1_flash_tool_selector

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-08-03  
**预估耗时**：10分钟

### 问题描述（原始）
需要使用 FlashToolSelector 对 P18 或 K1 设备进行刷机/固件升级。常见说法：P18 怎么刷机、K1 怎么刷机、FlashToolSelector 怎么用、P18 刷机步骤、K1 刷机方法。

### 扩展检索关键词
升版本, 刷到, 刷版本, 刷固件, 机器, flash, 终端, 烧写, 刷写, 升级固件, 重装系统, 更新到, 升到, 刷卡机, 烧录

### 根本原因
P18 和 K1 设备使用 FlashToolSelector 工具进行刷机，该工具简化了刷机流程，通过选择 flash.xml 配置文件即可进行格式化或固件升级操作。

### 详细解决方案
【前置准备】首次使用需安装驱动（只需做一次）：双击运行 DriverInstall.exe 安装刷机驱动，然后下载对应的刷机软件。

【适用范围】P18、K1 设备

操作步骤：
1. 打开 FlashToolSelector 软件
2. 选择 P18/K1 软件包中 download_agent 文件夹下的 flash.xml 文件
3. 根据需要选择以下两个选项之一进行刷机：
   - 格式化：清除设备数据并重新刷入固件
   - 固件升级：保留数据，仅升级固件版本
4. 按照软件提示完成刷机操作

【注意】
- 格式化会清除设备所有数据，请提前备份重要信息
- 固件升级不会影响设备数据，可直接升级
- 刷机过程中保持设备电量充足，避免中断

### 标签
P18, K1, FlashToolSelector, 刷机, 固件升级, 格式化, flash.xml, download_agent, OTA, 刷机工具, terminal

---

## 【案例11】case_d0551_d0552_cross_flash_compatibility

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-07-03  
**预估耗时**：5分钟

### 问题描述（原始）
D0551 或 D0552 机器刷机时不知道能用哪个版本的固件，或刷机包选错导致失败。常见说法：D0551 能刷 D0552 的固件吗、D0552 能刷安卓15吗、互刷机制、D0551 和 D0552 固件通用吗、刷机包选哪个、D0551刷D0552固件、跨型号刷机。

### 扩展检索关键词
flash, 烧写, 刷版本, 刷写, 烧录, 升级固件, 刷固件, 重装系统

### 根本原因
D0551 和 D0552 机器有互刷机制，但需要注意版本兼容性：D0551 支持安卓15和安卓13版本，也可以刷 D0552-安卓13（但需要先格式化刷机）；D0552 不支持安卓15，只能刷 D0551-安卓13 或 D0552-安卓13。

### 详细解决方案
【互刷机制对照表（2025年7月更新）】

D0551 机器可以刷：
✅ D0551-安卓15版本
✅ D0551-安卓13版本
✅ D0552-安卓13版本（新增支持，但需要先用对应版本格式化刷机）

D0552 机器可以刷：
❌ D0551-安卓15版本（不可刷）
✅ D0551-安卓13版本
✅ D0552-安卓13版本

【重要更新】D0551 刷 D0552-安卓13 操作步骤：
1. 确认设备型号：进入设备 Settings → About Services，查看 Model Name（确认是 D0551）和 Android Version（确认当前系统版本）
2. 下载 D0552 的安卓13版本固件包
3. 进入刷机工具的 Format 页面
4. 选择自动刷新（执行格式化）
5. 等待设备初始化完成
6. 再加载 D0552-安卓13 固件包，选择 Firmware Upgrade 模式
7. 点击 Download 进行刷机

【选择原则】
1. 先确认机器型号（进入 Settings → About Services 查看 Model Name）
2. D0551 优先用安卓15版本，或安卓13版本（可以是 D0551-安卓13 或 D0552-安卓13）
3. D0552 只能用安卓13版本（可以是 D0551-安卓13 或 D0552-安卓13）
4. D0552 不可刷安卓15版本
5. D0551 刷 D0552 固件前必须先格式化刷机，不能直接 OTA 升级

### 标签
互刷机制, D0551, D0552, 安卓15, 安卓13, 固件兼容性, 刷机包选择, OTA, 固件升级, cross flash, terminal

---

## 【案例12】case_mdm_resource_package_invalid_org

**所属产品**：terminal_device  
**功能模块**：resource_management  
**记录日期**：2026-07-03  
**预估耗时**：10分钟

### 问题描述（原始）
推送资源包到设备时出现 MDM failed; Update resource package resource file is invalid now! 错误，资源包无法正常下发到设备。常见说法：资源包推送失败、MDM failed、资源包无效、Update resource package failed、资源下发不了。

### 扩展检索关键词
POS机, 终端, 刷卡机, 机器, 硬件

### 根本原因
资源包中设置的所属机构与机器的所属机构不同，云端 MDM 校验失败，导致资源包无法推送到设备。

### 详细解决方案
1. 登录 TMS 平台（Terminal Manager System）；2. 查看设备的当前所属机构；3. 查看资源包配置的所属机构；4. 将设备移动到与资源包相同的机构下（修改设备所属机构，或重新上传资源包到正确机构）；5. 重新推送资源包。

### 标签
MDM, TMS, 资源包, resource package, 所属机构, 云端校验, 推送失败, invalid now, Terminal Manager SDK, 资源管理, 设备机构

---

## 【案例13】case_usb_connection_power_conflict

**所属产品**：terminal_device  
**功能模块**：usb_connection  
**记录日期**：2026-07-03  
**预估耗时**：5分钟

### 问题描述（原始）
设备用 USB 连接电脑时出现问题，ADB 无法识别设备，或电脑检测不到设备连接。常见说法：USB 连不上电脑、adb devices 没反应、电脑识别不到设备、USB 连接失败、设备连不上电脑。

### 扩展检索关键词
adb工具, 点不了, 调试桥, adb连接, 无响应, 检测不到, 机器, 找不到设备, 连接失败, 连不上, 终端, Android调试, 没变化, 点不动, 没反应

### 根本原因
Micro USB 数据电缆与电源供应电缆之间存在冲突。如果设备断电状态下直接插 USB 线，设备会识别 USB 端口用于充电功能，而不是数据通信功能，导致电脑无法识别设备。

### 详细解决方案
正确连接顺序：
1. 先插好电源线，开启设备（确保设备有电且开机）
2. 然后插入 Micro USB 连接线到电脑
3. 请勿在设备断电状态下连接 USB 线缆
4. 连接后尝试通过 ADB 方式连接设备（adb devices）
5. 检查设备序列号是否显示出来
6. 有时电脑上的弹出式连接窗口可能不会显示连接状态，但只要 ADB 能识别即可正常使用。

### 标签
USB, USB 连接, adb, 设备连接, 电源冲突, Micro USB, 充电模式, 数据模式, 电脑识别, Terminal Manager SDK

---

## 【案例14】case_d5_check_version_in_engineering_mode

**所属产品**：terminal_device  
**功能模块**：device_info  
**记录日期**：2026-07-03  
**预估耗时**：2分钟

### 问题描述（原始）
需要查看 D5 系列机器的版本号信息，包括内部版本号、外部版本号、副屏固件版本号等。常见说法：怎么查看版本号、D5 版本号在哪看、内部版本号怎么查、副屏固件版本、*#87# 版本号。

### 扩展检索关键词


### 根本原因
D5 系列机器支持通过暗码 *#87# 进入工程模式，在 MM1 测试菜单中点击版本号可以查看详细的版本信息。

### 详细解决方案
1. 在设备拨号界面输入暗码 *#87# 进入工程模式；2. 点击【MM1 测试】选项；3. 在 MM1 测试菜单中找到并点击【版本号】；4. 查看显示的版本信息：- 内部版本号 - 外部版本号 - 副屏固件版本号 等详细信息。

### 标签
D5, 版本号, 内部版本号, 外部版本号, 副屏固件, 工程模式, 工模, *#87#, MM1 测试, device, Terminal Manager SDK

---

## 【案例15】case_open_log_98

**所属产品**：terminal_device  
**功能模块**：device_log  
**记录日期**：2026-07-03  
**预估耗时**：3分钟

### 问题描述（原始）
需要抓取设备日志进行问题排查，或开启日志记录功能。常见说法：怎么抓日志、怎么打开日志、日志记录在哪开、*#98# 是什么、如何导出日志。

### 扩展检索关键词
POS机, 终端, 刷卡机, 机器, 硬件

### 根本原因
设备支持通过暗码 *#98# 快速打开日志功能，用于记录机器运行日志，方便后续问题分析和排查。

### 详细解决方案
1. 在设备拨号界面输入暗码 *#98#；2. 系统自动打开日志记录功能；3. 进行需要记录的操作（复现问题）；4. 日志会自动保存，可通过相应工具或路径导出查看。

### 标签
日志, log, *#98#, 暗码, 抓日志, 日志记录, 问题排查, 导出日志, Terminal Manager SDK, device

---

## 【案例16】case_d0551_d0552_google_key_writing

**所属产品**：terminal_device  
**功能模块**：device_provisioning  
**记录日期**：2026-07-16  
**预估耗时**：10分钟

### 问题描述（原始）
需要为 D0551 或 D0552 设备写入 Google Key（Attestation Key），或设备缺少 attestation key 导致相关功能异常。常见说法：写号、写 Google Key、刷 attestation key、D0551 写号、D0552 写号、设备没有 key、attestation key 丢失。

### 扩展检索关键词
POS机, 写序列号, 刷号, 终端, 写IMEI, 写barcode, 刷卡机, 刷SN, 写号, 写SN, 写设备号, 机器, 硬件

### 根本原因
设备出厂时未预置 Google Attestation Key，或 key 丢失/损坏，需要通过 IMEIwriter 工具重新写入对应的 key 文件。

### 详细解决方案
【环境准备】设备保持关机状态，先插上电源线，再插数据线与电脑相连，尽量在写号之前让设备开机一段时间让它有充足的电量。

【操作步骤】
1. 打开 IMEIwriter 工具，勾选 KeyFiles 下面的 attestation key
2. 弹出 File Select，选择对应的 bin 文件：
   - D0551 对应：d0551_nebullar_20250811.bin
   - D0552 对应：D0552_20260320.bin
   选择后点击 OK
3. System Config 中勾选 Barcode（即设备的 SN 号）
4. 点击 Start，将 SN 号填入弹窗中
5. 此时将设备的电源线重新插拔一次，当设备屏幕出现 meta mode，即为成功

【故障排查】
- 若无反应，观察是否进入了充电模式
- 若进入充电模式，插拔数据线和电源线，或充一段时间电之后再尝试

### 标签
D0551, D0552, Google Key, Attestation Key, 写号, IMEIwriter, meta mode, 刷 key, 设备 provisioning, Terminal Manager SDK

---

## 【案例17】case_download_no_response

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-07-16  
**预估耗时**：10分钟

### 问题描述（原始）
点击 Download 之后无反应，刷机工具没有响应，或设备没有进入刷机模式。常见说法：Download 没反应、点击下载没反应、刷机工具点下载没反应、Download 按钮点了没反应、刷机没反应、刷机工具无响应。

### 扩展检索关键词
模式, 点不了, 刷版本, 无响应, 刷固件, 机器, 状态, flash, 终端, 烧写, 刷写, 升级固件, 没变化, 重装系统, 点不动

### 根本原因
点击 Download 无反应需要根据场景判断原因：1) 刷 OTA 包时未先 Format 初始化导致 DA 下发失败；2) 格式化刷机时未正确进入刷机流程；3) 设备进入充电模式而非数据传输模式；4) 设备型号与固件版本不兼容导致互刷失败。

### 详细解决方案
[结论] 点击 Download 无反应，根据场景按以下三步排查：

### 场景一：刷 OTA 版本包
**现象**：刷机时报 STATUS_BROM_CMD_SEND_DA_FAIL (0xC0060003) 或 send DA fail

**解决**：
1. 不要直接点 Download 刷 OTA
2. 先在软件 Format 中勾选 自动刷新 / 整机刷新
3. 让设备完成初始化（等待初始化完成）
4. 再选择对应版本的 OTA 包刷写
5. 最后点击 Download 进行烧录

### 场景二：需要格式化刷机（Firmware Upgrade）
**现象**：刷机包需要完整擦除数据重新刷写

**解决**：
1. 进入刷机工具的 Format 页面
2. 选择 自动刷新 或 整机刷新 模式
3. 等待设备初始化完成（屏幕可能有提示）
4. 再加载固件包，选择 Firmware Upgrade 模式
5. 最后点击 Download

### 场景三：普通版本更新
**现象**：设备看起来正常，但点击 Download 后无响应，或刷机工具没识别到设备

**解决**：
1. 检查是否进入充电模式：
   - 断电状态下插 USB，设备会识别为充电而非数据传输
   - 正确顺序：先插电源线 - 设备开机 - 再插 USB 数据线 - 最后点击 Download
2. 若已进入充电模式：重新插拔电源线和数据线，确保设备在开机状态下连接
3. 检查 USB 线和端口是否正常（建议换原装线或 USB 2.0 端口）

### 仍有问题？检查互刷兼容性
如果以上步骤都试过还是无反应，可能是设备型号与固件版本不兼容：

| 设备 | 可刷版本 | 不可刷版本 |
|:---|:---|:---|
| D0551 | [可] D0551-安卓15 [可] D0551-安卓13 | [不可] D0552-安卓13 |
| D0552 | [可] D0551-安卓13 [可] D0552-安卓13 | [不可] D0551-安卓15 |

**检查方法**：
1. 确认设备型号（D0551 还是 D0552）
2. 确认固件版本（安卓13 还是 安卓15）
3. 对照上表检查是否跨型号刷入了不支持的版本

### 标签
Download, 刷机, OTA, 无反应, send DA fail, 0xC0060003, Format, 自动刷新, 整机刷新, 充电模式, 互刷机制, D0551, D0552, 安卓13, 安卓15, terminal

---

## 【案例18】case_flash_interrupted_usb_unrecognized

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-07-16  
**预估耗时**：70分钟

### 问题描述（原始）
机器刷一半不小心断开，之后再刷机无法刷机，电脑报无法识别的USB设备错误。常见说法：刷机中断、刷一半断了、USB无法识别、刷机失败、电脑认不出设备、刷机报错。注意：此问题与普通的USB连接失败不同，是刷机过程中断电/断连导致设备异常状态引起的。常见于D系列设备（D0551/D0552）。

### 扩展检索关键词
刷版本, 报, 刷固件, 报错, 机器, 出错, flash, 终端, 烧写, 失败, 刷写, 升级固件, 重装系统, 刷卡机, 烧录

### 根本原因
刷机过程中意外断电或USB断开，导致设备处于不完整的刷机状态（俗称变砖或假死），主板上的小电池仍有残余电量维持错误状态，电脑无法正确识别设备。此问题在D系列设备（D0551/D0552）中较为常见。

### 详细解决方案
[适用设备] D系列设备（D0551/D0552）等

[解决方案] 拔掉电池充分放电法

1. 断开所有连接
   - 拔掉USB数据线
   - 拔掉电源线
   - 拔掉设备电池（如果是可拆卸电池）

2. 静置放电
   - 让设备静置至少1个小时
   - 目的：让主板上的小电池充分放电，彻底清除错误状态

3. 重新刷机
   - 重新连接电源
   - 按正常流程重新刷机
   - 无需其他特殊操作

[预防措施]
- 刷机过程中保持电源稳定
- 使用可靠的USB线和端口
- 刷机时不要触碰设备和线缆
- 确保电脑不会进入休眠/睡眠模式

[D系列特别说明]
- D0551/D0552设备在刷机时务必保持电量充足
- 如反复出现此问题，建议更换USB线或端口
- 刷机前建议先充电30分钟以上

### 标签
刷机中断, USB无法识别, 刷机失败, 电池放电, 变砖恢复, 假死状态, 刷机断电, D系列, D0551, D0552, OTA, firmware, terminal

---

## 【案例19】case_flash_tool_cli_download

**所属产品**：terminal_device  
**功能模块**：ota_flash  
**记录日期**：2026-07-16  
**预估耗时**：15分钟

### 问题描述（原始）
需要使用 flash_tool 命令行进行下载/刷机，不想用GUI界面操作，或需要批量自动化刷机。常见说法：命令行刷机、flash_tool 命令行、自动化刷机、批量刷机、不用界面刷机、console模式刷机。

### 扩展检索关键词
flash, mode, 模式, 烧写, 刷版本, 刷写, 方式, 烧录, 升级固件, 刷固件, 重装系统, 状态

### 根本原因
flash_tool 支持命令行模式，可以通过配置文件(XML)或直接命令行参数执行下载，适用于批量操作或自动化场景。

### 详细解决方案
【前置条件】
1. 以管理员权限运行 CMD
2. 进入到 flash_tool.exe 同级目录

【方式一：使用配置文件 config.xml】

1. 生成配置文件
   - 打开 flash_tool GUI
   - File → Export Console Mode XML → Download...
   - 保存为 download.xml

2. 命令行执行
   flash_tool -i download.xml
   （-i 参数后接 xml 文件路径）

3. download.xml 关键参数说明
   - chip-name：芯片型号
   - download-agent：DA文件路径
   - scatter：scatter文件路径
   - rom-list：指定下载镜像路径（为空则自动加载）
   - log-info log_on：true=开启控制台日志
   - log-info log_path：日志保存目录

4. 下载方式配置（修改<commands>标签）

   固件升级模式：
   <commands>
       <firmware-upgrade>
           <scene>FIRMWARE_UPGRADE</scene>
           <format validation="false" physical="false" erase-flag="NormalErase" auto-format="true" auto-format-flag="FormatAll" />
           <da-download-all />
       </firmware-upgrade>
   </commands>

   格式化下载模式：
   <commands>
       <format-download>
           <combo-format>
               <format validation="false" physical="true" erase-flag="NormalErase" auto-format="true" auto-format-flag="FormatAll" />
           </combo-format>
           <da-download-all />
       </format-download>
   </commands>

   仅下载模式：
   <commands>
       <download-only>
           <da-download-all />
       </download-only>
   </commands>

【方式二：不使用配置文件（直接命令行）】

flash_tool -d MTK_AllInOne_DA.bin -s MT6575_Android_scatter.txt -c download

参数说明：
- -d：DA文件路径（必需）
- -s：scatter文件路径（必需）
- -c：下载模式（可选）
  • download：仅下载
  • format-download：格式化下载
  • firmware-upgrade：固件升级

【常见问题】
- 如果提示权限不足，确认是否以管理员运行 CMD
- 如果找不到文件，确认路径是否正确（支持相对路径和绝对路径）
- 批量刷机可以写批处理脚本(.bat)循环执行

### 标签
flash_tool, 命令行, CLI, 批量刷机, 自动化, download.xml, firmware-upgrade, format-download, OTA, 刷机工具, terminal

---

## 【案例20】case_d0551_d0552_write_sn_imei_writer

**所属产品**：terminal_device  
**功能模块**：device_provisioning  
**记录日期**：2026-07-28  
**预估耗时**：5分钟

### 问题描述（原始）
需要为D0551或D0552设备写入SN序列号（Barcode），或设备出厂时SN未写入/需要修改SN。常见说法：D0551写号、D0552写号、写SN、写序列号、设备没有SN号、SN号怎么写、IMEI writer怎么用、怎么写入条形码。

### 扩展检索关键词
POS机, 写序列号, 刷号, 终端, 写IMEI, 写barcode, 刷卡机, 刷SN, 写号, 写SN, 写设备号, 机器, 硬件

### 根本原因
设备出厂时SN（序列号/Barcode）未预置，或需要修改SN号，需要使用IMEI Writer工具写入。

### 详细解决方案
【适用设备】D0551、D0552（操作步骤相同）

【环境准备】
- Windows PC
- 下载IMEI Writer工具
- 设备关机状态，先插上电源线
- 用数据线连接设备到电脑

【操作步骤】
1. 打开IMEI Writer，点击Option -> 选择Composite Device (ADB)
2. 点击Smart Phone
3. 点击System Config
4. 勾选Barcode（即SN号输入选项）
5. 在输入框中填入要写入的SN序列号（Barcode）
6. 先点击Start按钮，然后按顺序连接：
   - 先插上设备电源线
   - 再插入USB数据线
7. 当设备屏幕左下角显示">meta mode"时，表示写号过程已开始，等待完成即可。

【注意事项】
- 必须先点Start，再插电源和USB
- 如果进入充电模式，拔线重试
- 确保SN号输入正确，写入后不易修改

### 标签
D0551, D0552, 写号, 写SN, SN, 序列号, Barcode, IMEI Writer, meta mode, 设备配置, device provisioning, Terminal Manager SDK

---

## 【案例21】case_check_android_version_settings

**所属产品**：terminal_device  
**功能模块**：device_info  
**记录日期**：2026-08-03  
**预估耗时**：2分钟

### 问题描述（原始）
需要查看设备的 Android 版本号。常见说法：怎么看安卓版本、Android version 在哪里看、系统版本号怎么查、设备安卓几。

### 扩展检索关键词
POS机, 终端, 刷卡机, 机器, 硬件

### 根本原因
设备的 Android 版本信息可以在系统设置的 About Services 页面中查看。

### 详细解决方案
1. 进入设备 Settings（设置）页面；2. 找到并点击【About Services】（关于服务）选项；3. 在 About Services 页面中找到【Android Version】或【Android 版本】；4. 显示的即为设备当前运行的 Android 版本号（如 Android 13、Android 15 等）。

### 标签
Android版本, Android Version, 系统版本, Settings, About Services, device, Terminal Manager SDK

---

## 【案例22】case_check_model_name_settings

**所属产品**：terminal_device  
**功能模块**：device_info  
**记录日期**：2026-08-03  
**预估耗时**：2分钟

### 问题描述（原始）
需要查看设备的型号名称（Model Name）。常见说法：设备型号怎么看、Model name 在哪里、怎么查设备型号、D0551 还是 D0552 怎么区分。

### 扩展检索关键词
POS机, 终端, 刷卡机, 机器, 硬件

### 根本原因
设备的型号名称（如 D0551、D0552、P18 等）可以在系统设置的 About Services 页面中查看。

### 详细解决方案
1. 进入设备 Settings（设置）页面；2. 找到并点击【About Services】（关于服务）选项；3. 在 About Services 页面中找到【Model Name】或【型号名称】；4. 显示的即为设备的型号名称（如 D0551、D0552、P18 等），可用于确认设备型号以选择正确的固件版本。

### 标签
Model Name, 型号名称, 设备型号, D0551, D0552, Settings, About Services, device, Terminal Manager SDK

---

## 【案例23】case_check_device_name_settings

**所属产品**：terminal_device  
**功能模块**：device_info  
**记录日期**：2026-08-03  
**预估耗时**：2分钟

### 问题描述（原始）
需要查看或确认设备的设备名称（Device Name）。常见说法：设备名称怎么看、Device name 在哪里、设备叫什么名。

### 扩展检索关键词
POS机, 终端, 刷卡机, 机器, 硬件

### 根本原因
设备的设备名称（Device Name）可以在系统设置的 About Services 页面中查看。

### 详细解决方案
1. 进入设备 Settings（设置）页面；2. 找到并点击【About Services】（关于服务）选项；3. 在 About Services 页面中找到【Device Name】或【设备名称】；4. 显示的即为设备的名称信息。

### 标签
Device Name, 设备名称, Settings, About Services, device, Terminal Manager SDK

---

## 【案例24】case_check_device_info_settings

**所属产品**：terminal_device  
**功能模块**：device_info  
**记录日期**：2026-08-03  
**预估耗时**：3分钟

### 问题描述（原始）
需要查看设备的完整基础信息，包括版本号、安卓版本、型号等，用于刷机前确认设备信息或问题排查。常见说法：怎么查看设备信息、设备基础信息在哪、刷机前怎么看设备型号、设备参数怎么查。

### 扩展检索关键词
flash, POS机, 终端, 烧写, 刷版本, 刷写, 刷卡机, 烧录, 升级固件, 刷固件, 重装系统, 机器, 硬件

### 根本原因
设备的完整基础信息（Build Number、Android Version、Model Name、Device Name 等）都集中在 Settings → About Services 页面中，便于用户一次性查看所有关键信息。

### 详细解决方案
【刷机前确认设备型号步骤】
1. 进入设备 Settings（设置）页面
2. 点击【About Services】（关于服务）
3. 查看以下关键信息：
   - Build Number：设备版本号（内部版本号）
   - Android Version：安卓系统版本（如 Android 13/15）
   - Model Name：设备型号（如 D0551、D0552、P18）
   - Device Name：设备名称
4. 根据 Model Name 和 Android Version 选择正确的刷机固件版本

【注意】
- D0551 支持安卓15和安卓13版本
- D0552 不支持安卓15，只能刷安卓13版本
- 确认型号和版本后再进行刷机操作，避免刷入不兼容的固件

### 标签
设备信息, 基础信息, 刷机前确认, Build Number, Android Version, Model Name, Device Name, Settings, About Services, device, Terminal Manager SDK

---

## 【案例25】case_k1_flash_tool_selector

**所属产品**：terminal_device  
**功能模块**：k1_flash  
**记录日期**：2026-08-03  
**预估耗时**：10分钟

### 问题描述（原始）
需要使用 FlashToolSelector 对 K1 设备进行刷机/固件升级。常见说法：K1 怎么刷机、K1 刷机步骤、FlashToolSelector K1 怎么用、K1 固件升级、K1 刷机方法。

### 扩展检索关键词
升版本, 刷到, 刷版本, 刷固件, 机器, flash, 终端, 烧写, 刷写, 升级固件, 重装系统, 更新到, 升到, 刷卡机, 烧录

### 根本原因
K1 设备使用 FlashToolSelector 工具进行刷机，操作步骤与 P18 完全一致。该工具简化了刷机流程，通过选择 flash.xml 配置文件即可进行格式化或固件升级操作。

### 详细解决方案
【前置准备】首次使用需安装驱动（只需做一次）：双击运行 DriverInstall.exe 安装刷机驱动，然后下载对应的刷机软件。

【适用范围】K1 设备（操作步骤与 P18 完全一致）

操作步骤：
1. 打开 FlashToolSelector 软件
2. 选择 K1 软件包中 download_agent 文件夹下的 flash.xml 文件
3. 根据需要选择以下两个选项之一进行刷机：
   - 格式化：清除设备数据并重新刷入固件
   - 固件升级：保留数据，仅升级固件版本
4. 按照软件提示完成刷机操作

【注意】
- 格式化会清除设备所有数据，请提前备份重要信息
- 固件升级不会影响设备数据，可直接升级
- 刷机过程中保持设备电量充足，避免中断
- K1 与 P18 刷机步骤完全相同，可参考 P18 刷机案例

### 标签
K1, FlashToolSelector, 刷机, 固件升级, 格式化, flash.xml, download_agent, OTA, 刷机工具, terminal

---

## 【案例26】case_d0551_write_sn_imei_writer

**所属产品**：terminal_device  
**功能模块**：device_provisioning  
**记录日期**：2026-07-28  
**预估耗时**：5分钟

### 问题描述（原始）
需要为D0551设备写入SN序列号（Barcode），或设备出厂时SN未写入/需要修改SN。常见说法：D0551写号、写SN、写序列号、设备没有SN号、SN号怎么写、IMEI writer怎么用、怎么写入条形码。

### 扩展检索关键词
POS机, 写序列号, 刷号, 终端, 写IMEI, 写barcode, 刷卡机, 刷SN, 写号, 写SN, 写设备号, 机器, 硬件

### 根本原因
设备出厂时SN（序列号/Barcode）未预置，或需要修改SN号，需要使用IMEI Writer工具通过AP_DB方式写入。

### 详细解决方案
【环境准备】
- Windows PC
- 下载IMEI Writer工具
- 设备关机状态，先插上电源线
- 用数据线连接设备到电脑

【操作步骤】
1. 打开IMEI Writer，点击Option -> 选择Composite Device (ADB)
2. 点击Smart Phone
3. 点击System Config
4. 勾选三个选项框，点击AP_DB，选择文件：d0551_nebullar_20250810.bin
5. 在输入框中填入要写入的SN序列号（Barcode）
6. 先点击Start按钮，然后按顺序连接：
   - 先插上设备电源线
   - 再插入USB数据线
7. 当设备屏幕左下角显示">meta mode"时，表示写号过程已开始，等待完成即可。

【注意事项】
- 必须先点Start，再插电源和USB
- 如果进入充电模式，拔线重试
- bin文件必须选择对应设备的版本

### 标签
D0551, 写号, 写SN, SN, 序列号, Barcode, IMEI Writer, AP_DB, meta mode, 设备配置, device provisioning, Terminal Manager SDK

---

