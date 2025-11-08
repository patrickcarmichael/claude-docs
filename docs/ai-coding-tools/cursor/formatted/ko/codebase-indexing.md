---
title: "Codebase Indexing"
source: "https://docs.cursor.com/ko/context/codebase-indexing"
language: "ko"
language_name: "Korean"
---

# Codebase Indexing
Source: https://docs.cursor.com/ko/context/codebase-indexing

Cursor가 코드베이스를 더 잘 이해하기 위해 학습하는 방법

Cursor는 각 파일의 임베딩을 계산해 코드베이스를 인덱싱해. 이렇게 하면 코드에 대한 AI 답변이 더 정확해져. 프로젝트를 열면 Cursor가 자동으로 인덱싱을 시작해. 새 파일은 점진적으로 인덱싱돼.
인덱싱 상태 확인: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Codebase 인덱싱 진행 표시기" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## 구성
</div>

Cursor는 [ignore files](/ko/context/ignore-files) (예: `.gitignore`, `.cursorignore`)에 포함된 파일을 제외하고 모든 파일을 인덱싱해.

`Show Settings`를 클릭해서:

* 새 저장소에 대한 자동 인덱싱 활성화
* 무시할 파일 설정

<Tip>
  [대용량 콘텐츠 파일 무시](/ko/context/ignore-files)는 답변
  정확도를 높여.
</Tip>

<div id="view-indexed-files">
  ### 인덱싱된 파일 보기
</div>

인덱싱된 파일 경로를 보려면: `Cursor Settings` > `Indexing & Docs` > `View included files`

그러면 인덱싱된 모든 파일이 나열된 `.txt` 파일이 열려.

<div id="multi-root-workspaces">
  ## 멀티 루트 워크스페이스
</div>

Cursor는 [멀티 루트 워크스페이스](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces)를 지원해서 여러 코드베이스로 작업할 수 있어:

* 모든 코드베이스가 자동으로 인덱싱돼
* 각 코드베이스의 컨텍스트가 AI에 제공돼
* `.cursor/rules`가 모든 폴더에서 적용돼

<div id="pr-search">
  ## PR search
</div>

PR search는 과거 변경 사항을 검색 가능하게 만들고 AI로 접근할 수 있게 해서 코드베이스의 변화를 이해하는 데 도움을 줘.

<div id="how-it-works">
  ### How it works
</div>

Cursor는 저장소 히스토리에서 **머지된 모든 PR을 자동으로 인덱싱**해. 요약은 시맨틱 검색 결과에 표시되고, 최근 변경을 우선하는 스마트 필터링이 적용돼.

Agent는 `@[PR number]`, `@[commit hash]`, `@[branch name]`를 사용해 **PR, 커밋, 이슈, 브랜치**를 컨텍스트로 가져올 수 있어. GitHub 댓글과 Bugbot 리뷰도 연결되어 있으면 포함돼.

**지원 플랫폼**에는 GitHub, GitHub Enterprise, Bitbucket이 포함돼. GitLab은 현재 지원하지 않아.

<Note>
  GitHub Enterprise users: The fetch tool falls back to git commands due to
  VSCode auth limitations.
</Note>

<div id="using-pr-search">
  ### Using PR search
</div>

"다른 PR에서 서비스는 어떻게 구현돼?" 같은 질문을 해봐. Agent가 자동으로 관련 PR을 컨텍스트로 가져와서 저장소 히스토리에 기반한 포괄적인 답변을 제공해.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="인덱싱된 코드베이스를 한눈에 어디서 볼 수 있어?">
    아직 전역 목록은 없어. 각 프로젝트를 Cursor에서 열고 Codebase Indexing 설정에서
    확인해봐.
  </Accordion>

  <Accordion title="인덱싱된 코드베이스를 전부 어떻게 삭제해?">
    Settings에서 Cursor 계정을 삭제하면 인덱싱된 모든 코드베이스가 제거돼.
    아니면 각 프로젝트의 Codebase Indexing 설정에서 개별 코드베이스를
    삭제해.
  </Accordion>

  <Accordion title="인덱싱된 코드베이스는 얼마나 오래 보관돼?">
    인덱싱된 코드베이스는 6주 동안 활동이 없으면 삭제돼. 프로젝트를 다시 열면
    재인덱싱이 진행돼.
  </Accordion>

  <Accordion title="내 소스 코드는 Cursor 서버에 저장돼?">
    아니. Cursor는 파일명이나 소스 코드를 저장하지 않고 임베딩만 생성해. 파일명은 난독화되고 코드 청크는 암호화돼.

    Agent가 코드베이스를 검색할 때, Cursor가 서버에서 임베딩을 가져와 청크를 복호화해.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [파일 무시](./section.md) →