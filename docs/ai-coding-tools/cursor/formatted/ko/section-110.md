---
title: "요청 ID 가져오기"
source: "https://docs.cursor.com/ko/troubleshooting/request-reporting"
language: "ko"
language_name: "Korean"
---

# 요청 ID 가져오기
Source: https://docs.cursor.com/ko/troubleshooting/request-reporting

기술 지원을 위한 요청 ID 찾기

Cursor 팀이 기술 문제를 조사할 때, "request ID"를 요청할 수도 있어.

<div id="what-is-a-request-id">
  ## 요청 ID가 뭐야?
</div>

요청 ID는 내부 시스템에서 Cursor로 보내는 각 요청을 고유하게 식별해.

형식 예: `8f2a5b91-4d3e-47c6-9f12-5e8d94ca7d23`

<div id="how-do-i-find-a-request-id">
  ## 요청 ID는 어떻게 찾지?
</div>

<Warning>
  Privacy Mode가 켜져 있으면 요청 ID 접근이 제한돼. 이슈를 보고할 땐 Privacy Mode를 꺼줘.

  참고: Business 플랜 사용자는 조직 관리자 설정으로 기본적으로 Privacy Mode가 켜져 있어.
</Warning>

<div id="getting-your-current-request-id">
  ### 현재 요청 ID 가져오기
</div>

현재 또는 최근 대화에 대한 이슈를 보고하려면:

Chat 사이드바에서 대화를 연 상태로, 컨텍스트 메뉴(오른쪽 위)를 열고 `Copy Request ID`를 선택해.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=01fe3046ccea814d9ae6c80686b8684b" data-og-width="361" width="361" data-og-height="202" height="202" data-path="images/requestIDpopup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fbb94c19668419fbc1d21c9116a19ef5 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=56561e4e16b31c814602a318a82df51f 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=adc9ff078b7f75df11fef1ae14e9a765 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=a67269d4c68a5852515c4674c5bb92c5 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=359b3c85b61ff24fae47231fe05bbbe2 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDpopup.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=5a161625fb3bd58ca1e09e14bc1e34f7 2500w" />
</Frame>

복사한 요청 ID를 안내된 대로 포럼이나 이메일로 보내줘.

<div id="getting-a-request-id-from-a-previous-action">
  ### 이전 작업에서 요청 ID 가져오기
</div>

`Report AI Action` 명령으로 과거 요청 ID를 가져와:

1. 커맨드 팔레트 열기 `⌘⇧P`
2. `Report AI Action` 입력
3. `Report AI Action` 옵션 선택

그러면 Chat, CMD+K, Apply 전반의 최근 AI 작업이 표시돼.

<Frame>
  <img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e7ea2fde75a272fde9094fbe6f7a9713" data-og-width="598" width="598" data-og-height="281" height="281" data-path="images/requestIDlist.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=0343e4a4a0ff03918bc78d0d12f9c049 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=33412487f180e8103892df87e9edc3bd 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e3e24102bbe41665b4df8871e4e7aaef 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=cd3693456ad54eafeebb10bd21f603ea 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=c7931e7efb82170161dde245766d075a 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/requestIDlist.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=bde365dc3c37d2040a206ee2771bf97f 2500w" />
</Frame>

시간과 기능을 확인해 해당 작업을 선택해. 요청 ID를 복사해서 우리에게 보내줘.

---

← Previous: [Common Issues](./common-issues.md) | [Index](./index.md) | Next: [문제 해결 가이드](./section.md) →