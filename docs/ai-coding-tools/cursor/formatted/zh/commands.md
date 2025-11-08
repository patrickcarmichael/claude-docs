---
title: "Commands"
source: "https://docs.cursor.com/zh/agent/chat/commands"
language: "zh"
language_name: "Chinese"
---

# Commands
Source: https://docs.cursor.com/zh/agent/chat/commands

为可复用的工作流定义命令

自定义命令让你创建可复用的工作流，并可在聊天输入框中通过简单的 `/` 前缀触发。这些命令有助于在团队内标准化流程并提升常见任务的效率。

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  命令目前处于 beta 阶段。随着我们持续改进，功能与语法可能会发生变化。
</Info>

<div id="how-commands-work">
  ## 命令的工作方式
</div>

命令是以纯 Markdown 文件的形式定义的，可以存放在两个位置：

1. **项目命令**：位于项目的 `.cursor/commands` 目录
2. **全局命令**：位于用户主目录的 `~/.cursor/commands` 目录

当你在聊天输入框中输入 `/` 时，Cursor 会自动检测并显示这两个目录中的可用命令，让它们在整个工作流程中随取随用。

<div id="creating-commands">
  ## 创建命令
</div>

1. 在项目根目录下创建一个 `.cursor/commands` 目录
2. 添加带有描述性名称的 `.md` 文件（例如 `review-code.md`、`write-tests.md`）
3. 用纯 Markdown 编写该命令应执行的说明
4. 当你输入 `/` 时，命令会自动出现在聊天中

下面是你的 commands 目录结构可能的样子：

```
.cursor/
└── commands/
    ├── 处理 GitHub PR 评论.md
    ├── 代码审查清单.md
    ├── 创建 PR.md
    ├── 轻量审阅现有改动.md
    ├── 新开发者入职.md
    ├── 运行全部测试并修复.md
    ├── 安全审计.md
    └── 新功能设置.md
```

<div id="examples">
  ## 示例
</div>

在项目里试试这些命令，感受一下它们是如何工作的。

<AccordionGroup>
  <Accordion title="代码评审清单">
    ```markdown  theme={null}
    # 代码评审清单

    ## 概览
    用于开展全面代码评审的完整清单，确保质量、安全性和可维护性。

    ## 评审类别

    ### 功能
    - [ ] 代码按预期工作
    - [ ] 已覆盖边界情况
    - [ ] 错误处理得当
    - [ ] 无明显缺陷或逻辑错误

    ### 代码质量
    - [ ] 代码可读、结构清晰
    - [ ] 函数小而专注
    - [ ] 变量命名清晰且具描述性
    - [ ] 无重复代码
    - [ ] 遵循项目约定

    ### 安全
    - [ ] 无明显安全漏洞
    - [ ] 具备输入验证
    - [ ] 正确处理敏感数据
    - [ ] 未硬编码敏感信息/密钥
    ```
  </Accordion>

  <Accordion title="安全审计">
    ```markdown  theme={null}
    # 安全审计

    ## 概览
    对代码库进行全面安全审查，识别并修复漏洞。

    ## 步骤
    1. **依赖审计**
       - 检查已知漏洞
       - 更新过时包
       - 审查第三方依赖

    2. **代码安全审查**
       - 检查常见漏洞
       - 审查认证/授权
       - 审计数据处理实践

    3. **基础设施安全**
       - 审查环境变量
       - 检查访问控制
       - 审计网络安全

    ## 安全清单
    - [ ] 依赖已更新且安全
    - [ ] 无硬编码机密
    - [ ] 已实施输入校验
    - [ ] 认证安全
    - [ ] 授权配置正确
    ```
  </Accordion>

  <Accordion title="设置新功能">
    ```markdown  theme={null}
    # 设置新特性

    ## 概览
    从前期规划到实现结构，系统化地搭建一个新特性。

    ## 步骤
    1. **定义需求**
       - 明确特性范围和目标
       - 梳理用户故事和验收标准
       - 制定技术方案

    2. **创建特性分支**
       - 从 main/develop 派生分支
       - 搭建本地开发环境
       - 配置新增依赖

    3. **规划架构**
       - 设计数据模型和 API
       - 规划 UI 组件与流程
       - 制定测试策略

    ## 特性设置清单
    - [ ] 需求已记录
    - [ ] 用户故事已编写
    - [ ] 技术方案已制定
    - [ ] 特性分支已创建
    - [ ] 开发环境已就绪
    ```
  </Accordion>

  <Accordion title="创建 pull request">
    ```markdown  theme={null}
    # 创建 PR

    ## 概览
    创建一个结构清晰的 pull request，包含完善的描述、标签和评审人。

    ## 步骤
    1. **准备分支**
       - 确保所有更改已提交
       - 将分支推送到远程仓库
       - 确认分支与 main 同步最新

    2. **撰写 PR 描述**
       - 清晰总结更改
       - 包含背景与动机
       - 列出任何破坏性变更
       - 如果涉及 UI 变更，附上截图

    3. **设置 PR**
       - 使用具描述性的标题创建 PR
       - 添加合适的标签
       - 指定评审人
       - 关联相关 issue

    ## PR 模板
    - [ ] 功能 A
    - [ ] Bug 修复 B
    - [ ] 单元测试通过
    - [ ] 手动测试完成
    ```
  </Accordion>

  <Accordion title="运行测试并修复失败">
    ```markdown  theme={null}
    # 运行全部测试并修复失败

    ## 概览
    执行完整测试套件，并系统化地修复任何失败，确保代码质量与功能正确性。

    ## 步骤
    1. **运行测试套件**
       - 运行项目中的所有测试
       - 捕获输出并定位失败
       - 同时检查单元测试和集成测试

    2. **分析失败**
       - 按类型分类：不稳定（flaky）、已损坏、新增失败
       - 按影响优先级进行修复
       - 检查是否与近期改动相关

    3. **系统化地修复问题**
       - 先从最关键的失败着手
       - 一次修复一个问题
       - 每次修复后重新运行测试
    ```
  </Accordion>

  <Accordion title="引导新开发者上手">
    ```markdown  theme={null}
    # 新开发者上手指南

    ## 概览
    完整的入职流程，帮新开发者快速上手并开始工作。

    ## 步骤
    1. **环境搭建**
       - 安装必需工具
       - 搭建开发环境
       - 配置 IDE 与扩展
       - 配置 Git 和 SSH 密钥

    2. **项目熟悉**
       - 查看项目结构
       - 理解架构
       - 阅读关键文档
       - 配置本地数据库

    ## 入职清单
    - [ ] 开发环境就绪
    - [ ] 所有测试通过
    - [ ] 能在本地运行应用
    - [ ] 数据库已配置且可用
    - [ ] 已提交首个 PR
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [紧凑](./section.md) →