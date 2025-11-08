---
title: "Python"
source: "https://docs.cursor.com/zh/guides/languages/python"
language: "zh"
language_name: "Chinese"
---

# Python
Source: https://docs.cursor.com/zh/guides/languages/python

使用扩展和代码检查工具配置 Python 开发环境

<Note>
  本指南受 [Jack Fields](https://x.com/OrdinaryInds)
  及其关于为 Python 开发配置 VS Code 的
  [文章](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  启发良多。想了解更多细节，去看看他的文章吧。
</Note>

<div id="prerequisites">
  ## 前置条件
</div>

开始之前，先确认你已经：

* 安装了 [Python](https://python.org)（建议 3.8 或更高版本）
* 安装了用于版本控制的 [Git](https://git-scm.com/)
* 安装了 Cursor，并更新到最新版本

<div id="essential-extensions">
  ## 必备扩展
</div>

以下扩展可将 Cursor 打造成功能齐全的 Python 开发环境。它们提供语法高亮、代码静态检查、调试以及单元测试能力。

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Microsoft 提供的核心语言支持
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    高性能 Python 语言服务器
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    更强大的调试功能
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python 代码静态检查与格式化工具
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### 高级 Python 工具链
</div>

虽然以上扩展一直是 Cursor 中最受欢迎的 Python 开发扩展，我们也新增了一些扩展，能帮你更充分地发挥 Python 开发效能。

<div id="uv-python-environment-manager">
  #### `uv` - Python 环境管理器
</div>

[uv](https://github.com/astral-sh/uv) 是一款现代的 Python 包管理器，除创建与管理虚拟环境外，还可替代 pip 作为默认包管理器。

要安装 uv，请在终端运行以下命令：

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Python 代码静态检查与格式化工具
</div>

[Ruff](https://docs.astral.sh/ruff/) 是一款现代的 Python 代码静态检查与格式化工具，可用于检查编程错误、帮助遵循编码规范，并给出重构建议。它可以与 Black 搭配用于代码格式化。

要安装 Ruff，在终端中运行以下命令：

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Cursor 配置
</div>

<div id="1-python-interpreter">
  ### 1. Python 解释器
</div>

在 Cursor 中配置你的 Python 解释器：

1. 打开命令面板（Cmd/Ctrl + Shift + P）
2. 搜索“Python: Select Interpreter”
3. 选择你的 Python 解释器（如果用的是虚拟环境，就选对应的环境）

<div id="2-code-formatting">
  ### 2. 代码格式化
</div>

用 Black 设置自动代码格式化：

<Note>
  Black 是一个代码格式化器，会自动把你的代码整理成
  一致的风格。它零配置，并在 Python 社区被广泛采用。
</Note>

要安装 Black，在终端运行以下命令：

```bash  theme={null}
pip install black
```

然后，在你的 `settings.json` 文件里添加下面这段配置，把 Cursor 设为使用 Black 进行代码格式化：

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. Linting
</div>

可以用 PyLint 来检查编程错误、强制执行编码规范，并给出重构建议。

要安装 PyLint，在终端里运行以下命令：

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. 类型检查
</div>

除了进行 lint 检查，我们还可以用 MyPy 来检测类型错误。

安装 MyPy 时，在终端运行以下命令：

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## 调试
</div>

Cursor 为 Python 提供强大的调试功能：

1. 点击行号栏设置断点
2. 使用 Debug 面板（Cmd/Ctrl + Shift + D）
3. 配置 `launch.json` 以自定义调试配置

<div id="recommended-features">
  ## 推荐功能
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/zh/tab/overview">
    贴合你操作意图的智能代码补全
  </Card>

  <Card title="Chat" icon="comments" href="/zh/chat/overview">
    用自然对话来探索并理解代码
  </Card>

  <Card title="Agent" icon="robot" href="/zh/chat/agent">
    借助 AI 处理复杂的开发任务
  </Card>

  <Card title="Context" icon="network-wired" href="/zh/context/model-context-protocol">
    从第三方系统引入上下文
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/zh/tab/auto-import">
    编写代码时自动导入模块
  </Card>

  <Card title="AI Review" icon="check-double" href="/zh/tab/overview#quality">
    Cursor 持续用 AI 审查你的代码
  </Card>
</CardGroup>

<div id="framework-support">
  ## 框架支持
</div>

Cursor 可无缝配合主流 Python 框架：

* **Web 框架**：Django、Flask、FastAPI
* **数据科学**：Jupyter、NumPy、Pandas
* **机器学习**：TensorFlow、PyTorch、scikit-learn
* **测试**：pytest、unittest
* **API**：requests、aiohttp
* **数据库**：SQLAlchemy、psycopg2

---

← Previous: [JavaScript 与 TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS 与 macOS（Swift）](./ios-macosswift.md) →