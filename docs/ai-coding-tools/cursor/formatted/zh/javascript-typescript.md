---
title: "JavaScript 与 TypeScript"
source: "https://docs.cursor.com/zh/guides/languages/javascript"
language: "zh"
language_name: "Chinese"
---

# JavaScript 与 TypeScript
Source: https://docs.cursor.com/zh/guides/languages/javascript

支持框架的 JavaScript 和 TypeScript 开发

欢迎在 Cursor 中进行 JavaScript 和 TypeScript 开发！编辑器通过其扩展生态为 JS/TS 开发提供了卓越支持。下面是让你充分利用 Cursor 的要点。

<div id="essential-extensions">
  ## 必备扩展
</div>

虽然 Cursor 能很好地配合你喜欢的任何扩展使用，但如果你刚入门，我们推荐先安装这些：

* **ESLint** - 启用 Cursor 基于 AI 的 lint 自动修复所必需
* **JavaScript and TypeScript Language Features** - 提供更强的语言支持与 IntelliSense
* **Path Intellisense** - 智能文件路径补全

<div id="cursor-features">
  ## Cursor 功能
</div>

Cursor 通过以下方式增强你现有的 JavaScript/TypeScript 工作流：

* **Tab 补全**：具备上下文感知的代码补全，理解你的项目结构
* **自动导入**：在你使用库时，Tab 会自动为你导入
* **行内编辑**：在任意行使用 `CMD+K`，即可以完美语法进行编辑
* **Composer 指引**：用 Composer 在多个文件间规划并编辑代码

<div id="framework-intelligence-with-docs">
  ### 搭配 @Docs 的框架智能
</div>

Cursor 的 @Docs 功能允许你添加可供 AI 参考的自定义文档源，进一步加速 JavaScript 开发。把 MDN、Node.js 或你常用框架的文档接入进来，就能获得更准确、更具上下文的代码建议。

<Card title="深入了解 @Docs" icon="book" href="/zh/context/@-symbols/@-docs">
  了解如何在 Cursor 中添加和管理自定义文档源。
</Card>

<div id="automatic-linting-resolution">
  ### 自动修复 Lint 问题
</div>

Cursor 的一大亮点是与 Linter 扩展的无缝集成。
确保你已配置好 linter（例如 ESLint），并启用“Iterate on Lints”设置。

随后，在 Composer 中使用 Agent 模式时，一旦 AI 回答了你的问题并进行了代码更改，它会自动读取 linter 的输出，并尝试修复那些它之前可能未发现的 lint 错误。

<div id="framework-support">
  ## 框架支持
</div>

Cursor 可与所有主流 JavaScript 框架和库无缝配合，例如：

### React & Next.js

* 完整的 JSX/TSX 支持与智能组件提示
* 面向 Next.js 的 Server Component 与 API 路由智能
* 推荐：[**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native) 扩展

<div id="vuejs">
  ### Vue.js
</div>

* 基于 Volar 的模板语法支持
* 组件自动补全与类型检查
* 推荐：[**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* 模板校验与 TypeScript 装饰器支持
* 组件与服务生成
* 推荐：[**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* 组件语法高亮与智能补全
* 响应式语句与 store 提示
* 推荐：[**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### 后端框架（Express/NestJS）
</div>

* 路由与中间件智能
* 面向 NestJS 的 TypeScript 装饰器支持
* 集成 API 测试工具

记得，Cursor 的 AI 功能可良好适配以上所有框架，理解它们的模式与最佳实践，从而提供相关建议。AI 能帮上忙的范围涵盖从组件创建到复杂重构，同时会尊重你项目的既有模式。

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →