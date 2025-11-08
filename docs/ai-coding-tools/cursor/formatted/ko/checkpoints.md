---
title: "Checkpoints"
source: "https://docs.cursor.com/ko/agent/chat/checkpoints"
language: "ko"
language_name: "Korean"
---

# Checkpoints
Source: https://docs.cursor.com/ko/agent/chat/checkpoints

Agent 변경 후 이전 상태 저장 및 복원

Checkpoints는 Agent가 코드베이스에 가한 변경을 자동으로 스냅샷으로 저장해. 필요하면 Agent가 한 수정을 언제든 되돌릴 수 있어.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## 체크포인트 복원
</div>

복원하는 방법은 두 가지야:

1. **입력 박스에서**: 이전 요청에 있는 `Restore Checkpoint` 버튼을 클릭
2. **메시지에서**: 메시지에 마우스를 올린 뒤 표시되는 + 버튼을 클릭

<Warning>
  체크포인트는 버전 관리가 아니야. 영구적인 기록은 Git을 써.
</Warning>

<div id="how-they-work">
  ## 동작 방식
</div>

* Git과 분리되어 로컬에 저장됨
* 수동 편집은 제외하고 Agent 변경만 추적됨
* 자동으로 정리됨

<Note>
  수동 편집은 추적되지 않아. 체크포인트는 Agent 변경에만 써.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="체크포인트가 Git에 영향 줘?">
    아니. Git 히스토리랑은 별개야.
  </Accordion>

  {" "}

  <Accordion title="얼마나 오래 보관돼?">
    현재 세션이랑 최근 기록 동안. 자동으로 정리돼.
  </Accordion>

  <Accordion title="직접 만들 수 있어?">
    아니. Cursor가 자동으로 만들어.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Commands](./commands.md) →