---
title: "Permissions"
source: "https://docs.cursor.com/zh/cli/reference/permissions"
language: "zh"
language_name: "Chinese"
---

# Permissions
Source: https://docs.cursor.com/zh/cli/reference/permissions

用于控制智能体访问文件和命令的权限类型

在 CLI 配置中通过权限令牌控制智能体可执行的操作。可在 `~/.cursor/cli-config.json`（全局）或 `<project>/.cursor/cli.json`（项目级）中设置权限。

<div id="permission-types">
  ## 权限类型
</div>

<div id="shell-commands">
  ### Shell 命令
</div>

**格式：** `Shell(commandBase)`

控制对 shell 命令的访问。`commandBase` 是命令行中的第一个标记（token）。

<div class="full-width-table">
  | 示例           | 描述                        |
  | ------------ | ------------------------- |
  | `Shell(ls)`  | 允许运行 `ls` 命令              |
  | `Shell(git)` | 允许使用任意 `git` 子命令          |
  | `Shell(npm)` | 允许使用 npm 包管理器命令           |
  | `Shell(rm)`  | 拒绝具有破坏性的文件删除（通常用于 `deny`） |
</div>

<div id="file-reads">
  ### 文件读取
</div>

**格式：** `Read(pathOrGlob)`

控制对文件和目录的读取权限。支持 glob 模式。

<div class="full-width-table">
  | 示例                  | 描述                          |
  | ------------------- | --------------------------- |
  | `Read(src/**/*.ts)` | 允许读取 `src` 中的 TypeScript 文件 |
  | `Read(**/*.md)`     | 允许在任意位置读取 Markdown 文件       |
  | `Read(.env*)`       | 拒绝读取环境变量文件                  |
  | `Read(/etc/passwd)` | 拒绝读取系统文件                    |
</div>

<div id="file-writes">
  ### 文件写入
</div>

**格式：** `Write(pathOrGlob)`

控制对文件和目录的写入权限。支持 glob 模式。在打印模式下使用时，写入文件需要加上 `--force`。

<div class="full-width-table">
  | 示例                    | 描述                  |
  | --------------------- | ------------------- |
  | `Write(src/**)`       | 允许写入 `src` 下的任意文件   |
  | `Write(package.json)` | 允许修改 `package.json` |
  | `Write(**/*.key)`     | 拒绝写入私钥文件            |
  | `Write(**/.env*)`     | 拒绝写入环境变量文件          |
</div>

<div id="configuration">
  ## 配置
</div>

在 CLI 配置文件的 `permissions` 对象中添加权限：

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## 模式匹配
</div>

* Glob 模式支持 `**`、`*` 和 `?` 通配符
* 相对路径作用域限定为当前工作区
* 绝对路径可指向项目之外的文件
* 拒绝规则优先生效于允许规则

---

← Previous: [参数](./section.md) | [Index](./index.md) | Next: [斜杠命令](./section.md) →