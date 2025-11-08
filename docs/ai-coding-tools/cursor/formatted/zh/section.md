---
title: "疑难排查指南"
source: "https://docs.cursor.com/zh/troubleshooting/troubleshooting-guide"
language: "zh"
language_name: "Chinese"
---

# 疑难排查指南
Source: https://docs.cursor.com/zh/troubleshooting/troubleshooting-guide

修复问题与提交错误报告的步骤

Cursor 的问题可能来自扩展、应用数据或系统层面的故障。先试试这些疑难排查步骤。

<CardGroup cols={1}>
  <Card horizontal title="报告问题" icon="bug" href="#reporting-an-issue">
    向 Cursor 团队报告问题的步骤
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## 疑难解答
</div>

<Steps>
  <Step title="检查网络连接">
    先确认 Cursor 能否连接到其服务。

    **运行网络诊断：** 前往 `Cursor Settings` > `Network`，点击 `Run Diagnostics`。这会测试你与 Cursor 服务器的连接，并定位影响 AI 功能、更新或其他联机功能的网络问题。

    如果诊断显示连接异常，检查防火墙设置、代理配置或可能阻止 Cursor 访问的网络限制。
  </Step>

  <Step title="清理扩展数据">
    针对扩展相关问题：

    **暂时禁用所有扩展：** 在命令行运行 `cursor --disable-extensions`。如果问题消失，逐个重新启用扩展以定位有问题的那个。

    **重置扩展数据：** 卸载并重装有问题的扩展以重置其存储的数据。查看扩展设置中重装后仍会保留的配置。
  </Step>

  <Step title="清理应用数据">
    <Warning>
      这会删除你的应用数据，包括扩展、主题、代码片段以及与安装相关的数据。先导出你的个人资料以保留这些数据。
    </Warning>

    为了在更新或重装后恢复，Cursor 会在应用外部存储应用数据。

    清理应用数据的方法：

    **Windows：** 在命令提示符中运行以下命令：

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **macOS：** 在终端运行 `sudo rm -rf ~/Library/Application\ Support/Cursor` 和 `rm -f ~/.cursor.json`。

    **Linux：** 在终端运行 `rm -rf ~/.cursor ~/.config/Cursor/`。
  </Step>

  <Step title="卸载 Cursor">
    卸载 Cursor：

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        在开始菜单搜索“Add or Remove Programs”，找到“Cursor”，点击“Uninstall”。
      </Card>

      <Card horizontal title="macOS" icon="apple">
        打开“应用程序”文件夹，右键点击“Cursor”，选择“移到废纸篓”。
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **对于 .deb 包：** `sudo apt remove cursor`

        **对于 .rpm 包：** `sudo dnf remove cursor` 或 `sudo yum remove cursor`

        **对于 AppImage：** 删除所在位置的 Cursor.appimage 文件。
      </Card>
    </CardGroup>
  </Step>

  <Step title="重新安装 Cursor">
    从[下载页面](https://www.cursor.com/downloads)重新安装。未清理应用数据时，Cursor 会恢复到之前的状态；否则将获得全新安装。
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## 报告问题
</div>

如果这些步骤仍然无效，去[论坛](https://forum.cursor.com/)反馈。

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  在 Cursor 论坛报告 Bug 或问题
</Card>

为便于快速排查，请提供：

<CardGroup cols={2}>
  <Card title="问题截图" icon="image">
    截取屏幕，并打码/遮盖敏感信息。
  </Card>

  <Card title="复现步骤" icon="list-check">
    记录能复现问题的具体步骤。
  </Card>

  <Card title="系统信息" icon="computer">
    从以下路径获取系统信息：

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="请求 ID" icon="shield-halved" href="/zh/troubleshooting/request-reporting">
    点击查看如何收集请求 ID 的指南
  </Card>

  <Card title="控制台错误" icon="bug">
    检查开发者控制台：<br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="日志" icon="file-lines">
    打开日志：<br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [获取请求 ID](./section-110.md) | [Index](./index.md) | Next: [Welcome](./welcome.md) →