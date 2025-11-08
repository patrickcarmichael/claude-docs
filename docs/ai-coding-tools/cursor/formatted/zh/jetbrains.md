---
title: "JetBrains"
source: "https://docs.cursor.com/zh/guides/migration/jetbrains"
language: "zh"
language_name: "Chinese"
---

# JetBrains
Source: https://docs.cursor.com/zh/guides/migration/jetbrains

使用熟悉的工具从 JetBrains IDE 迁移到 Cursor

Cursor 提供现代、由 AI 驱动的编码体验，足以替代你的 JetBrains 系列 IDE。虽然一开始的迁移可能有些不适应，但基于 VS Code 的底座让 Cursor 具备强大的功能和高度可定制性。

<div id="editor-components">
  ## 编辑器组件
</div>

<div id="extensions">
  ### 扩展
</div>

JetBrains IDE 是很棒的工具，自带针对目标语言和框架的预设配置。

Cursor 不同——开箱就是一块空白画布，你可以按自己喜好自由定制，不受原本面向的语言和框架限制。

Cursor 拥有庞大的扩展生态，JetBrains IDE 提供的几乎所有功能（甚至更多！）都能通过这些扩展实现。

看看下面这些热门扩展：

<CardGroup cols={4}>
  <Card title="Remote SSH" icon="network-wired" href="cursor:extension/anysphere.remote-ssh">
    SSH 扩展
  </Card>

  <Card title="Project Manager" icon="folder-tree" href="cursor:extension/alefragnani.project-manager">
    管理多个项目
  </Card>

  <Card title="GitLens" icon="git" href="cursor:extension/eamodio.gitlens">
    增强的 Git 集成
  </Card>

  <Card title="Local History" icon="clock-rotate-left" href="cursor:extension/xyz.local-history">
    跟踪本地文件变更
  </Card>

  <Card title="Error Lens" icon="bug" href="cursor:extension/usernamehw.errorlens">
    内联错误高亮
  </Card>

  <Card title="ESLint" icon="code-compare" href="cursor:extension/dbaeumer.vscode-eslint">
    代码静态检查
  </Card>

  <Card title="Prettier" icon="wand-magic-sparkles" href="cursor:extension/esbenp.prettier-vscode">
    代码格式化
  </Card>

  <Card title="Todo Tree" icon="folder-tree" href="cursor:extension/Gruntfuggly.todo-tree">
    跟踪 TODO 和 FIXME
  </Card>
</CardGroup>

<div id="keyboard-shortcuts">
  ### 键盘快捷键
</div>

Cursor 内置快捷键管理器，可以把你喜欢的快捷键映射到相应的操作。

用这个扩展，几乎所有 JetBrains IDE 的快捷键都能直接带到 Cursor！
记得查看扩展文档，了解如何按你的偏好进行配置：

<Card title="IntelliJ IDEA Keybindings" icon="keyboard" href="cursor:extension/k--kato.intellij-idea-keybindings">
  安装此扩展，把 JetBrains IDE 的快捷键带到 Cursor。
</Card>

<Note>
  常见但不同的快捷键：

  * 查找动作：⌘/Ctrl+Shift+P（对比 ⌘/Ctrl+Shift+A）
  * 快速修复：⌘/Ctrl+.（对比 Alt+Enter）
  * 转到文件：⌘/Ctrl+P（对比 ⌘/Ctrl+Shift+N）
</Note>

<div id="themes">
  ### 主题
</div>

用这些社区主题，在 Cursor 中复刻你最喜欢的 JetBrains IDE 的外观与体验。

可以选择标准的 Darcula 主题，或挑一个能匹配你 JetBrains 工具语法高亮的主题。

<CardGroup cols={1}>
  <Card title="JetBrains - Darcula Theme" icon="moon" horizontal href="cursor:extension/rokoroku.vscode-theme-darcula">
    体验经典的 JetBrains Darcula 深色主题
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="JetBrains PyCharm" icon="python" horizontal href="cursor:extension/gabemahoney.pycharm-dark-theme-for-python" />

  <Card title="IntelliJ" icon="java" horizontal href="cursor:extension/compassak.intellij-idea-new-ui" />

  <Card title="JetBrains Fleet" icon="code" horizontal href="cursor:extension/MichaelZhou.fleet-theme" />

  <Card title="JetBrains Rider" icon="hashtag" horizontal href="cursor:extension/muhammad-sammy.rider-theme" />
</CardGroup>

<CardGroup cols={1}>
  <Card title="JetBrains Icons" icon="icons" horizontal href="cursor:extension/ardonplay.vscode-jetbrains-icon-theme">
    获取熟悉的 JetBrains 文件与文件夹图标
  </Card>
</CardGroup>

<div id="font">
  ### 字体
</div>

想要完整的 JetBrains 风格体验，可以使用官方的 JetBrains Mono 字体：

1. 下载并在系统中安装 JetBrains Mono 字体：

<CardGroup cols={1}>
  <Card title="Download JetBrains Mono" icon="link" horizontal href="https://www.jetbrains.com/lp/mono/" />
</CardGroup>

2. 安装字体后重启 Cursor
3. 在 Cursor 中打开设置（⌘/Ctrl + ,）
4. 搜索“Font Family”
5. 将字体族设置为 `'JetBrains Mono'`

<Note>
  想要获得更好的体验，也可以在设置中将 `"editor.fontLigatures": true` 设为启用以开启字体连字。
</Note>

<div id="ide-specific-migration">
  ## 针对特定 IDE 的迁移
</div>

很多用户喜欢 JetBrains 系列 IDE，因为它们对目标语言和框架提供了开箱即用的支持。Cursor 不同——开箱即用就是一块空白画布，你可以随心定制，不受限于 IDE 预设的语言和框架。

Cursor 已经接入了 VS Code 的扩展生态，几乎所有（甚至更多！）JetBrains IDE 的功能都能通过这些扩展复现。

下面是针对各个 JetBrains IDE 的推荐扩展。

<div id="intellij-idea-java">
  ### IntelliJ IDEA (Java)
</div>

<CardGroup cols={2}>
  <Card title="Language Support for Java" icon="java" href="cursor:extension/redhat.java">
    核心 Java 语言特性
  </Card>

  <Card title="Debugger for Java" icon="bug" href="cursor:extension/vscjava.vscode-java-debug">
    Java 调试支持
  </Card>

  <Card title="Test Runner for Java" icon="vial" href="cursor:extension/vscjava.vscode-java-test">
    运行与调试 Java 测试
  </Card>

  <Card title="Maven for Java" icon="box" href="cursor:extension/vscjava.vscode-maven">
    Maven 支持
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Project Manager for Java" icon="folder-tree" href="cursor:extension/vscjava.vscode-java-dependency" horizontal>
    项目管理工具
  </Card>
</CardGroup>

<Warning>
  关键差异：

  * 构建/运行配置通过 launch.json 管理
  * Spring Boot 工具通过 ["Spring Boot Extension Pack"](cursor:extension/vmware.vscode-boot-dev-pack) 扩展提供
  * Gradle 支持通过 ["Gradle for Java"](cursor:extension/vscjava.vscode-gradle) 扩展提供
</Warning>

<div id="pycharm-python">
  ### PyCharm (Python)
</div>

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    核心 Python 支持
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    快速类型检查
  </Card>

  <Card title="Jupyter" icon="notebook" href="cursor:extension/ms-toolsai.jupyter">
    Notebook 支持
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python 格式化与代码规范检查
  </Card>
</CardGroup>

<Note>
  关键差异：

  * 虚拟环境通过命令面板管理
  * 调试配置在 launch.json 中
  * 依赖管理通过 requirements.txt 或 Poetry
</Note>

<div id="webstorm-javascripttypescript">
  ### WebStorm (JavaScript/TypeScript)
</div>

<CardGroup cols={2}>
  <Card title="JavaScript and TypeScript Nightly" icon="js" href="cursor:extension/ms-vscode.vscode-typescript-next">
    最新语言特性
  </Card>

  <Card title="ES7+ React/Redux Snippets" icon="react" href="cursor:extension/dsznajder.es7-react-js-snippets">
    React 开发
  </Card>

  <Card title="Vue Language Features" icon="vuejs" href="cursor:extension/Vue.volar">
    Vue.js 支持
  </Card>

  <Card title="Angular Language Service" icon="angular" href="cursor:extension/Angular.ng-template">
    Angular 开发
  </Card>
</CardGroup>

<Info>
  大多数 WebStorm 功能已内置于 Cursor/VS Code，包括：

  * npm scripts 视图
  * 调试
  * Git 集成
  * TypeScript 支持
</Info>

<div id="phpstorm-php">
  ### PhpStorm (PHP)
</div>

<CardGroup cols={2}>
  <Card title="PHP Intelephense" icon="php" href="cursor:extension/bmewburn.vscode-intelephense-client">
    PHP 语言服务器
  </Card>

  <Card title="PHP Debug" icon="bug" href="cursor:extension/xdebug.php-debug">
    Xdebug 集成
  </Card>

  <Card title="PHP Intellisense" icon="brain" href="cursor:extension/felixfbecker.php-intellisense">
    代码智能
  </Card>

  <Card title="PHP DocBlocker" icon="comment-dots" href="cursor:extension/neilbrayfield.php-docblocker">
    文档工具
  </Card>
</CardGroup>

<Note>
  关键差异：

  * Xdebug 通过 launch.json 配置
  * Composer 在终端中集成使用
  * 数据库工具通过 ["SQLTools"](cursor:extension/mtxr.sqltools) 扩展提供
</Note>

<div id="rider-net">
  ### Rider (.NET)
</div>

<CardGroup cols={2}>
  <Card title="C#" icon="code" href="cursor:extension/anysphere.csharp">
    C# 核心支持
  </Card>

  <Card title="DotRush" icon="toolbox" href="cursor:extension/nromanov.dotrush">
    开源 C# 开发环境
  </Card>

  <Card title="ReSharper Plugin" icon="box" href="https://www.jetbrains.com/help/resharper-vscode/Get_started.html#installation">
    JetBrains C# 插件
  </Card>

  <Card title=".NET Install Tool" icon="box-open" href="cursor:extension/ms-dotnettools.vscode-dotnet-runtime">
    .NET SDK 管理
  </Card>
</CardGroup>

<Warning>
  主要差异：

  * 通过文件资源管理器使用解决方案资源管理器
  * 通过 CLI 或扩展进行 NuGet 包管理
  * 通过测试资源管理器集成测试运行器
</Warning>

<div id="goland-go">
  ### GoLand（Go）
</div>

<CardGroup cols={1}>
  <Card title="Go" icon="golang" href="cursor:extension/golang.Go">
    官方 Go 扩展
  </Card>
</CardGroup>

<Note>
  主要差异：

  * 自动提示安装 Go 工具链
  * 通过 launch.json 进行调试
  * 包管理与 go.mod 集成
</Note>

<div id="tips-for-a-smooth-transition">
  ## 平滑过渡小贴士
</div>

<Steps>
  <Step title="使用命令面板">
    按 <kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> 查找命令
  </Step>

  <Step title="AI 功能">
    利用 Cursor 的 AI 功能完成代码补全和重构
  </Step>

  <Step title="自定义设置">
    调整你的 settings.json，优化工作流
  </Step>

  <Step title="终端集成">
    使用内置终端执行命令行操作
  </Step>

  <Step title="扩展">
    在 VS Code 扩展市场浏览更多工具
  </Step>
</Steps>

<Info>
  记住，虽然有些工作流可能不同，但 Cursor 提供强大的 AI 辅助编码能力，能让你的效率超越传统 IDE。
</Info>

---

← Previous: [iOS 与 macOS（Swift）](./ios-macosswift.md) | [Index](./index.md) | Next: [VS Code](./vs-code.md) →