---
title: "Java"
source: "https://docs.cursor.com/zh/guides/languages/java"
language: "zh"
language_name: "Chinese"
---

# Java
Source: https://docs.cursor.com/zh/guides/languages/java

使用 JDK、扩展与构建工具设置 Java 开发环境

本指南将帮你为 Java 开发配置 Cursor，涵盖设置 JDK、安装所需扩展、调试、运行 Java 应用，以及集成 Maven、Gradle 等构建工具。还会介绍与 IntelliJ 或 VS Code 类似的工作流特性。

<Note>
  开始之前，先确保你已安装 Cursor 并更新到最新版本。
</Note>

<div id="setting-up-java-for-cursor">
  ## 为 Cursor 配置 Java
</div>

<div id="java-installation">
  ### 安装 Java
</div>

在开始设置 Cursor 之前，需要先在你的机器上安装 Java。

<Warning>
  Cursor 不自带 Java 编译器，如果还没装，需要先安装一个 JDK。
</Warning>

<CardGroup cols={1}>
  <Card title="Windows 安装" icon="windows">
    下载并安装一个 JDK（例如 OpenJDK、Oracle JDK、Microsoft Build of
    OpenJDK）。

    <br />

    设置 JAVA\_HOME，并把 JAVA\_HOME\bin 加到你的 PATH。
  </Card>

  <Card title="macOS 安装" icon="apple">
    通过 Homebrew 安装（`brew install openjdk`），或下载安装包进行安装。

    <br />

    确保 JAVA\_HOME 指向已安装的 JDK。
  </Card>

  <Card title="Linux 安装" icon="linux">
    使用你的包管理器（例如 `sudo apt install openjdk-17-jdk` 或等效命令），
    或通过 SDKMAN 安装。
  </Card>
</CardGroup>

要检查是否安装成功，运行：

```bash  theme={null}
java -version
javac -version
```

<Info>
  如果 Cursor 未检测到你的 JDK，请在 settings.json 中手动配置：
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/path/to/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/path/to/jdk-17",
      "default": true
    }
  ]
}
```

<Warning>重启 Cursor 以应用更改。</Warning>

<div id="cursor-setup">
  ### Cursor 设置
</div>

<Info>Cursor 兼容 VS Code 扩展。请手动安装以下扩展：</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    包含 Java 语言支持、调试器、测试运行器、Maven 支持和
    项目管理器
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    使用 Gradle 构建系统所必需
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Spring Boot 开发必备
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Kotlin 应用开发必需
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### 配置构建工具
</div>

<div id="maven">
  #### Maven
</div>

确保已安装 Maven（`mvn -version`）。如需安装，请从 [maven.apache.org](https://maven.apache.org/download.cgi) 获取：

1. 下载二进制包
2. 解压到目标位置
3. 将 MAVEN\_HOME 环境变量设置为解压后的目录
4. 将 %MAVEN\_HOME%\bin（Windows）或 \$MAVEN\_HOME/bin（Unix）添加到 PATH

<div id="gradle">
  #### Gradle
</div>

确保已安装 Gradle（`gradle -version`）。如需安装，请从 [gradle.org](https://gradle.org/install/) 获取：

1. 下载二进制发行版
2. 解压到目标位置
3. 将 GRADLE\_HOME 环境变量设置为解压后的目录
4. 将 %GRADLE\_HOME%\bin（Windows）或 \$GRADLE\_HOME/bin（Unix）添加到 PATH

或者使用 Gradle Wrapper，它会自动下载并使用正确的 Gradle 版本：

<div id="running-and-debugging">
  ## 运行与调试
</div>

现在一切都准备好了，该运行并调试你的 Java 代码了。
根据你的需求，可以用以下方式：

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    点击任意 main 方法上方出现的“Run”链接，快速运行
    你的程序
  </Card>

  <Card title="Debug" icon="bug">
    打开“Run and Debug”侧边栏面板，使用“Run”按钮启动
    你的应用
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    在命令行中使用 Maven 或 Gradle 命令执行
  </Card>

  <Card title="Spring Boot" icon="leaf">
    直接从 Spring Boot Dashboard 扩展
    启动 Spring Boot 应用
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor 工作流
</div>

Cursor 的 AI 功能可以显著提升你的 Java 开发效率。下面是一些在 Java 场景下用好 Cursor 的方式：

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      为方法、方法签名，以及 getters/setters 等 Java 模板代码提供智能补全。
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      实现设计模式、重构代码，或生成具备正确继承层次的类。
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      快速内联修改方法、修复错误，或在不中断工作流的情况下生成单元测试。
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      获取 Java 概念支持、调试异常，或理解各类框架特性。
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### 示例工作流
</div>

1. **生成 Java 模板代码**\
   使用 [Tab completion](/zh/tab/overview) 快速生成构造函数、getters/setters、equals/hashCode 方法，以及其他重复性的 Java 模式。

2. **调试复杂的 Java 异常**\
   遇到晦涩的 Java 堆栈跟踪时，选中它并用 [Ask](/zh/chat/overview) 解释根因并给出可能的修复方案。

3. **重构遗留 Java 代码**\
   使用 [Agent mode](/zh/chat/agent) 现代化旧 Java 代码——将匿名类改为 lambda，升级到更新的 Java 语言特性，或实现设计模式。

4. **框架开发**\
   用 @docs 把你的文档加入 Cursor 上下文，在 Cursor 中生成特定框架的代码。

---

← Previous: [高效使用文档](./section.md) | [Index](./index.md) | Next: [JavaScript 与 TypeScript](./javascript-typescript.md) →