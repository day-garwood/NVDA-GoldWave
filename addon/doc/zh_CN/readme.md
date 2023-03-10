# GoldWave 支持插件 #

* 作者: Joseph Lee, NVDA contributors.
* 下载[稳定版][1]
* NVDA compatibility: 2022.4 and later

此插件可增强GoldWave音频编辑器的无障碍体验性。

## 快捷键 ##

* NVDA+Shift+C： 在音频编辑过程中切换朗读命令。
* Control+Shift+P: 报告当前的轨道位置。
* NVDA+Shift+R: 报告当前编辑曲目的剩余时间。
* Control+NVDA+1: 报告您正在编辑的通道。
* Control+NVDA+2: 报告音频文件的总长度。
* Control+NVDA+3： 读出音频选择信息的摘要。
* Control+NVDA+4: 报告缩放级别。

有关GoldWave和键盘命令的更多信息，请参阅GoldWave手册。

注意：现在需要 GoldWave 6或更高版本。

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.

## 版本22.03

* 需要NVDA 2021.3或更高版本。
* 当试图在 Windows 7、8和8.1上安装插件时，将显示一条警告消息。

## 版本21.10

* NVDA 2021.2或更高版本是必需的，因为 NVDA 的更改会影响此插件。
* 在 GoldWave 6.57及更高版本中，按下播放/回放/停止键时，NVDA 将不再重复加载文件的名称。

## 版本21.06

* 使用 Flake8 解决了许多编码样式问题和潜在错误。

## 版本20.06

* 使用 Flake8 解决了许多编码样式问题和潜在错误。

## 版本20.04

* 添加了有关restig time命令（NVDA + Shift + R）的输入帮助消息。
* 切换命令 （NVDA_Shift_C） 现在显示在 NVDA 的输入手势对话框中的"GoldWave"分类下。

## 版本20.01

* 需要NVDA 2019.3或更高版本。

## 版本19.11

* 现在需要Windows 7 SP1，GoldWave 6.x和NVDA 2019.1或更高版本。
* 新增了声音窗口的帮助消息（如果安装了Control Usage Assistant插件，则可以使用）。

## 版本18.12

* 现在在将某些命令通知设置为关闭的情况下执行某些GoldWave命令时，NVDA将不再显示任何操作或发出错误提示音（在某些情况下，这可能会导致异常行为）。
* 内部更改以支持将来的NVDA版本。

## 版本18.07

* 修复了尝试获取轨道的剩余时间时不会显示前导零的问题。

## 版本17.05

* 增加了在启用调试日志记录的情况下运行NVDA时提供调试信息的功能,注意: 这需要（NVDA 2017.1或更高版本）。
* 更新翻译。

## 版本16.12

* 版本方案现在是year.month而不是major.minor。

## 版本4.0

* 附加存储库已转移到GitHub（现在位于 https://github.com/josephsl/goldwave).
* 现在查找诸如通道名称,和其他状态信息之类的信息时性能得到改善。

## 版本3.0

* 增加了一条命令来报告当前曲目的剩余时间(NVDA+Shift+R)。
* 报告通道信息等状态信息时略有改进。

## 版本2.0

* 支持GoldWave 6，包括64位版本的GoldWave（请参阅上面的注释）。
* 现在可以从插件管理器（NVDA 2014.3及更高版本）访问插件帮助。
* 如果按左声道的Control + Shift + L等声道选择命令，NVDA现在会报告选定的声道。
* 数字编辑字段中的各种问题（如审查字段和混合对话框中的时间选择器）已得到修复，包括选择文本，更新值等。
* 当切换到其他程序时，命令通知设置将被记住。

## 版本1.2

* 修复了NVDA难以公布一些编辑字段的问题。
* 新的更新和翻译。
* 请注意，由于近期NVDA的变化，音频选择和其他状态命令在某些系统中可能无法按预期工作。

## 版本1.1

* 支持盲文中的消息通告。
* 音频选择摘要以英语以外的语言显示。
* 添加了更多命令通告，包括提示位置移动和删除/修剪操作。
* 修复了数字编辑字段中的问题，例如各种效果对话框中没有任何字段名称或错误字段名称被宣布。
* 新的更新和翻译。

## 版本1.0

* 发布初始版本。

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=goldwave
