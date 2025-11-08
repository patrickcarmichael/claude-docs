---
title: "Tools"
source: "https://docs.cursor.com/ko/agent/tools"
language: "ko"
language_name: "Korean"
---

# Tools
Source: https://docs.cursor.com/ko/agent/tools

코드를 검색·편집·실행하기 위해 에이전트가 사용할 수 있는 도구

[Agent](/ko/agent/overview) 내 각 모드에서 사용할 수 있는 모든 도구 목록이야. 직접 [custom modes](/ko/agent/modes#custom)를 만들 때 도구를 켜거나 끌 수 있어.

<Note>
  작업 중 Agent가 호출할 수 있는 도구 횟수에는 제한이 없어. 요청을 완료할 때까지 필요한 만큼 계속 사용할 거야.
</Note>

<div id="search">
  ## 검색
</div>

코드베이스와 웹에서 관련 정보를 찾는 검색 도구들.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    파일을 최대 250줄까지 읽어 (최대 모드에선 750줄).
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    파일 내용을 읽지 않고 디렉터리 구조만 확인해.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    [인덱싱된
    코드베이스](/ko/context/codebase-indexing)에서 시맨틱 검색을 수행해.
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    파일에서 정확한 키워드나 패턴을 찾아.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    퍼지 매칭으로 파일 이름을 찾아.
  </Accordion>

  <Accordion title="Web" icon="globe">
    검색 쿼리를 만들고 웹 검색을 실행해.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    유형과 설명에 맞는 특정 [규칙](/ko/context/rules)을 가져와.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## 편집
</div>

파일과 코드베이스에 특정 수정을 가하는 도구.

<AccordionGroup>
  <Accordion title="수정 & 재적용" icon="pencil">
    파일에 대한 수정 사항을 제안하고 [apply](/ko/agent/apply)로 자동 적용해.
  </Accordion>

  <Accordion title="파일 삭제" icon="trash">
    파일을 자동으로 삭제해 (설정에서 끌 수 있어).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## 실행
</div>

Chat이 터미널과 상호작용할 수 있어.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    터미널 명령을 실행하고 출력을 모니터링해.
  </Accordion>
</AccordionGroup>

<Note>기본적으로 Cursor는 사용 가능한 첫 번째 터미널 프로필을 써.</Note>

선호하는 터미널 프로필을 설정하려면:

1. Command Palette 열기 (`Cmd/Ctrl+Shift+P`)
2. "Terminal: Select Default Profile" 검색
3. 원하는 프로필 선택

<div id="mcp">
  ## MCP
</div>

Chat은 설정된 MCP 서버를 통해 데이터베이스나 서드파티 API 같은 외부 서비스와 상호작용할 수 있어.

<AccordionGroup>
  <Accordion title="MCP 서버 토글" icon="server">
    사용 가능한 MCP 서버를 토글해. 자동 실행 설정을 따를 거야.
  </Accordion>
</AccordionGroup>

[Model Context Protocol](/ko/context/model-context-protocol)에 대해 더 알아보고, [MCP 디렉터리](/ko/tools)에서 사용 가능한 서버를 확인해봐.

<div id="advanced-options">
  ## 고급 옵션
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    수동 확인 없이 편집을 자동 적용해.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    터미널 명령을 자동 실행하고 편집도 자동으로 수락해. 테스트 스위트 실행이나 변경 사항 검증에 유용해.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    자동 실행을 허용할 도구를 지정하는 allowlist를 설정해. allowlist는 허용된 작업을 명시적으로 정의해서 보안을 강화해.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Agent가 발견한 린터 오류와 경고를 자동으로 고쳐.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [백그라운드 에이전트](./section.md) →