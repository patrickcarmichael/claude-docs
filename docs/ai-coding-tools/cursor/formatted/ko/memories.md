---
title: "Memories"
source: "https://docs.cursor.com/ko/context/memories"
language: "ko"
language_name: "Korean"
---

# Memories
Source: https://docs.cursor.com/ko/context/memories



Memories는 Chat에서의 대화를 바탕으로 자동으로 생성되는 규칙이야. 프로젝트 단위로 적용되고, 세션이 바뀌어도 컨텍스트를 계속 유지해.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/memories.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d10452508d962d7a9ec37de1c22245d1" alt="Cursor의 Memories" controls data-path="images/context/rules/memories.mp4" />
</Frame>

<div id="how-memories-are-created">
  ## 메모리가 생성되는 방식
</div>

1. **사이드카 관찰**: Cursor는 사이드카 방식을 사용해서 다른 모델이 너의 대화를 관찰하고 관련 메모리를 자동으로 추출해. 이건 네가 작업하는 동안 백그라운드에서 수동적으로 일어나. 백그라운드에서 생성된 메모리는 저장되기 전에 사용자 승인이 필요해서, 무엇을 기억할지에 대한 신뢰와 통제를 보장해.

2. **도구 호출**: Agent는 기억해 달라고 명시적으로 요청했을 때나, 이후 세션을 위해 보존해야 할 중요한 정보를 감지했을 때 도구 호출로 직접 메모리를 만들 수 있어.

<div id="manage-memories">
  ## 메모리 관리
</div>

Cursor Settings → Rules에서 메모리를 관리할 수 있어.

---

← Previous: [Model Context Protocol (MCP)](./model-context-protocol-mcp.md) | [Index](./index.md) | Next: [Rules](./rules.md) →