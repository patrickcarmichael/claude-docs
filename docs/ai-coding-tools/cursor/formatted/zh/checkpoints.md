---
title: "Checkpoints"
source: "https://docs.cursor.com/zh/agent/chat/checkpoints"
language: "zh"
language_name: "Chinese"
---

# Checkpoints
Source: https://docs.cursor.com/zh/agent/chat/checkpoints

在 Agent 更改后保存并恢复先前状态

Checkpoints 会自动为 Agent 对你代码库的更改创建快照。需要时，你可以用它们撤销 Agent 的修改。

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## 恢复检查点
</div>

有两种恢复方式：

1. **从输入框**：在之前的请求上点击 `Restore Checkpoint` 按钮
2. **从消息**：鼠标悬停在消息上时点击“+”按钮

<Warning>
  检查点不是版本控制。需要永久历史请用 Git。
</Warning>

<div id="how-they-work">
  ## 工作原理
</div>

* 本地存储，独立于 Git
* 仅跟踪 Agent 的变更（不包含手动编辑）
* 自动清理

<Note>
  手动编辑不会被跟踪。检查点只用于记录 Agent 的变更。
</Note>

<div id="faq">
  ## 常见问题
</div>

<AccordionGroup>
  <Accordion title="检查点会影响 Git 吗？">
    不会。它们独立于 Git 历史。
  </Accordion>

  {" "}

  <Accordion title="会保存多久？">
    仅在当前会话和近期历史中保存，并会自动清理。
  </Accordion>

  <Accordion title="可以手动创建吗？">
    不行。它们由 Cursor 自动创建。
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Commands](./commands.md) →