---
title: "iOS 与 macOS（Swift）"
source: "https://docs.cursor.com/zh/guides/languages/swift"
language: "zh"
language_name: "Chinese"
---

# iOS 与 macOS（Swift）
Source: https://docs.cursor.com/zh/guides/languages/swift

将 Cursor 与 Xcode 集成开展 Swift 开发

欢迎在 Cursor 中进行 Swift 开发！不管是构建 iOS 应用、macOS 应用，还是服务端 Swift 项目，我们都能帮上忙。本指南会带你在 Cursor 中设置 Swift 开发环境，从基础入门，到进阶功能逐步深入。

<div id="basic-workflow">
  ## 基本工作流
</div>

在 Swift 开发里，最简单的用法是把 Cursor 当作主力代码编辑器，同时继续用 Xcode 来构建和运行 app。你能享受到这些功能：

* 智能补全
* AI 编码辅助（在任意一行试试 [CMD+K](/zh/inline-edit/overview)）
* 用 [@Docs](/zh/context/@-symbols/@-docs) 快速看文档
* 语法高亮
* 基础代码导航

需要构建或运行 app 时，直接切回 Xcode。这个工作流很适合想利用 Cursor 的 AI 能力，同时在调试和部署上继续用熟悉的 Xcode 工具的开发者。

<div id="hot-reloading">
  ### 热重载
</div>

当使用 Xcode 的 workspace 或 project（而不是直接在 Xcode 里打开文件夹）时，Xcode 往往会忽略你在 Cursor 或任何 Xcode 之外对文件做的更改。

虽然把文件夹直接在 Xcode 里打开可以缓解这个问题，但在 Swift 的开发工作流中，你可能需要使用 project。

一个很棒的解决方案是用 [Inject](https://github.com/krzysztofzablocki/Inject)，这是一个 Swift 的热重载库，能让你的 app 在代码变更后实时“热重载”并立即更新。它不会受到 Xcode workspace/project 机制带来的副作用影响，你在 Cursor 里的更改会立刻反映到 app 中。

<CardGroup cols={1}>
  <Card title="Inject - Swift 的热重载" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    了解 Inject，并学习如何在 Swift 项目中使用它。
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## 高级 Swift 开发
</div>

<Note>
  本指南的这一部分深受 [Thomas
  Ricouard](https://x.com/Dimillian) 及其关于在 iOS 开发中使用 Cursor 的
  [文章](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  启发。想了解更多细节，请查看他的文章，并关注他获取更多 Swift 内容。
</Note>

如果你想只开一个编辑器，避免在 Xcode 和 Cursor 之间来回切换，可以使用像 [Sweetpad](https://sweetpad.hyzyla.dev/) 这样的扩展，把 Cursor 直接集成到 Xcode 的底层构建系统中。

Sweetpad 是一个功能强大的扩展，让你可以在不牺牲 Xcode 功能的前提下，直接在 Cursor 中构建、运行和调试 Swift 项目。

要开始使用 Sweetpad，你仍然需要在 Mac 上安装 Xcode——它是 Swift 开发的基础。你可以从 [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835) 下载 Xcode。完成 Xcode 的安装后，我们再用一些必备工具来增强你在 Cursor 中的开发体验。

打开终端并运行：

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →