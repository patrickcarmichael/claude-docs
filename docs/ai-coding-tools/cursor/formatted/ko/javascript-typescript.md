---
title: "JavaScript & TypeScript"
source: "https://docs.cursor.com/ko/guides/languages/javascript"
language: "ko"
language_name: "Korean"
---

# JavaScript & TypeScript
Source: https://docs.cursor.com/ko/guides/languages/javascript

프레임워크 지원을 갖춘 JavaScript 및 TypeScript 개발

Cursor에서 JavaScript와 TypeScript 개발을 시작해봐! 이 에디터는 확장 생태계를 통해 JS/TS 개발을 강력하게 지원해. Cursor를 최대한 활용하려면 아래 내용을 참고해.

<div id="essential-extensions">
  ## 필수 확장 프로그램
</div>

Cursor는 어떤 확장 프로그램이든 잘 어울리지만, 처음 시작한다면 아래 걸 추천해:

* **ESLint** - Cursor의 AI 기반 린트 자동 수정 기능에 꼭 필요
* **JavaScript and TypeScript Language Features** - 강화된 언어 지원과 IntelliSense
* **Path Intellisense** - 파일 경로 스마트 자동 완성

<div id="cursor-features">
  ## Cursor 기능
</div>

Cursor는 기존 JavaScript/TypeScript 워크플로우를 다음으로 강화해줘:

* **탭 자동완성**: 프로젝트 구조를 이해하는 컨텍스트 인식 코드 자동완성
* **자동 임포트**: 사용하자마자 라이브러리를 자동으로 임포트해 줘
* **인라인 편집**: 어떤 줄에서든 `CMD+K`로 문법에 맞게 즉시 편집
* **Composer 가이드**: Composer로 여러 파일에 걸쳐 코드 계획과 편집

<div id="framework-intelligence-with-docs">
  ### @Docs로 강화된 프레임워크 인텔리전스
</div>

Cursor의 @Docs 기능은 AI가 참조할 수 있는 사용자 지정 문서 소스를 추가해 JavaScript 개발을 한층 끌어올려줘. MDN, Node.js, 또는 즐겨 쓰는 프레임워크의 문서를 추가해서 더 정확하고 문맥에 맞는 코드 제안을 받아봐.

<Card title="@Docs에 대해 더 알아보기" icon="book" href="/ko/context/@-symbols/@-docs">
  Cursor에서 사용자 지정 문서 소스를 추가하고 관리하는 방법을 알아봐.
</Card>

<div id="automatic-linting-resolution">
  ### 린트 자동 해결
</div>

Cursor의 돋보이는 기능 중 하나는 Linter 확장과의 매끄러운 통합이야.
ESLint 같은 linter를 설정하고, 'Iterate on Lints' 설정을 활성화해 둬.

그러면 Composer에서 Agent 모드를 사용할 때, AI가 질의에 답하고 코드 변경을 수행한 뒤 linter 출력 결과를 자동으로 읽고, 놓쳤을 수도 있는 lint 오류를 고치려고 시도해.

<div id="framework-support">
  ## 프레임워크 지원
</div>

Cursor는 다음과 같은 주요 JavaScript 프레임워크와 라이브러리에서 매끄럽게 동작해:

### React & Next.js

* 지능형 컴포넌트 제안이 포함된 완전한 JSX/TSX 지원
* Next.js용 서버 컴포넌트 및 API 라우트 인텔리전스
* 추천: [**React Developer Tools**](cursor:extension/msjsdiag.vscode-react-native) 확장

<div id="vuejs">
  ### Vue.js
</div>

* Volar 통합 기반 템플릿 문법 지원
* 컴포넌트 자동 완성 및 타입 체크
* 추천: [**Vue Language Features**](cursor:extension/vue.volar)

<div id="angular">
  ### Angular
</div>

* 템플릿 검증 및 TypeScript 데코레이터 지원
* 컴포넌트/서비스 생성
* 추천: [**Angular Language Service**](cursor:extension/Angular.ng-template)

<div id="svelte">
  ### Svelte
</div>

* 컴포넌트 문법 하이라이팅과 지능형 자동 완성
* 반응형 구문 및 스토어 제안
* 추천: [**Svelte for VS Code**](cursor:extension/svelte.svelte-vscode)

<div id="backend-frameworks-expressnestjs">
  ### 백엔드 프레임워크 (Express/NestJS)
</div>

* 라우트와 미들웨어 인텔리전스
* NestJS용 TypeScript 데코레이터 지원
* API 테스트 도구 연동

기억해줘, Cursor의 AI 기능은 이 모든 프레임워크에서 잘 작동하고, 각 프레임워크의 패턴과 베스트 프랙티스를 이해해 관련성 높은 제안을 제공해. AI는 컴포넌트 생성부터 복잡한 리팩터링까지 도와주면서, 프로젝트의 기존 패턴을 존중해.

---

← Previous: [Java](./java.md) | [Index](./index.md) | Next: [Python](./python.md) →