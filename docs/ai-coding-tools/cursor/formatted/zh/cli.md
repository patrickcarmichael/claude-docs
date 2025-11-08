---
title: "使用无头 CLI"
source: "https://docs.cursor.com/zh/cli/headless"
language: "zh"
language_name: "Chinese"
---

# 使用无头 CLI
Source: https://docs.cursor.com/zh/cli/headless

了解如何使用 Cursor CLI 编写脚本，实现代码分析、生成与修改的自动化

在脚本与自动化流程中使用 Cursor CLI，执行代码分析、生成与重构等任务。

<div id="how-it-works">
  ## 工作原理
</div>

在非交互式脚本和自动化场景中使用 [print 模式](/zh/cli/using#non-interactive-mode)（`-p, --print`）。

<div id="file-modification-in-scripts">
  ### 在脚本中修改文件
</div>

将 `--print` 与 `--force` 一起使用，在脚本中修改文件：

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [安装](./section.md) →