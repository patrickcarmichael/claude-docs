---
title: "Rules"
source: "https://docs.cursor.com/ko/context/rules"
language: "ko"
language_name: "Korean"
---

# Rules
Source: https://docs.cursor.com/ko/context/rules

재사용 가능하고 스코프가 지정된 지침으로 Agent 모델의 동작을 제어해.

Rules는 Agent와 Inline Edit에 시스템 수준 지침을 제공해. 프로젝트에 대한 지속적인 컨텍스트, 기본 설정, 워크플로로 생각하면 돼.

Cursor는 네 가지 유형의 Rules를 지원해:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    `.cursor/rules`에 저장돼. 버전 관리되며 코드베이스 스코프에만 적용돼.
  </Card>

  <Card title="User Rules" icon="user">
    Cursor 환경 전체에 전역 적용돼. 설정에서 정의되며 항상 적용돼.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    마크다운 형식의 Agent 지침. `.cursor/rules`의 간단한 대안이야.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    여전히 지원되지만 더는 권장하지 않아. 대신 Project Rules를 사용해.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## 규칙의 동작 방식
</div>

대규모 언어 모델은 완료 사이의 상태를 기억하지 않아. 규칙은 프롬프트 수준에서 지속적이고 재사용 가능한 컨텍스트를 제공해.

규칙이 적용되면, 규칙 내용이 모델 컨텍스트의 시작에 포함돼. 이렇게 하면 AI가 코드 생성, 편집 해석, 워크플로 지원에서 일관된 가이드를 따르게 돼.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="채팅 컨텍스트에 적용된 규칙" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  규칙은 [Chat](/ko/chat/overview)과 [Inline
  Edit](/ko/inline-edit/overview)에 적용돼. 활성화된 규칙은 Agent 사이드바에 표시돼.
</Info>

<div id="project-rules">
  ## Project rules
</div>

프로젝트 규칙은 `.cursor/rules`에 있어. 각 규칙은 파일 단위로 관리되고, 버전 관리돼. 경로 패턴으로 범위를 지정하거나, 수동으로 실행하거나, 관련성에 따라 포함할 수도 있어. 하위 디렉터리는 해당 폴더 범위로 적용되는 자체 `.cursor/rules` 디렉터리를 둘 수 있어.

프로젝트 규칙은 이런 데 써봐:

* 코드베이스에 대한 도메인 지식을 정의
* 프로젝트 특화 워크플로우나 템플릿 자동화
* 스타일이나 아키텍처 결정 표준화

<div id="rule-anatomy">
  ### 규칙 구조
</div>

각 규칙 파일은 메타데이터와 콘텐츠를 지원하는 **MDC**(`.mdc`) 형식으로 작성돼. 타입 드롭다운에서 `description`, `globs`, `alwaysApply` 속성을 바꿔 규칙이 적용되는 방식을 제어할 수 있어.

| <span class="no-wrap">Rule Type</span>         | Description                                         |
| :--------------------------------------------- | :-------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | 항상 모델 컨텍스트에 포함돼                                     |
| <span class="no-wrap">`Auto Attached`</span>   | glob 패턴과 일치하는 파일이 참조될 때 포함돼                         |
| <span class="no-wrap">`Agent Requested`</span> | AI가 포함 여부를 결정할 수 있도록 제공돼. `description`은 반드시 제공해야 해 |
| <span class="no-wrap">`Manual`</span>          | `@ruleName`을 사용해 명시적으로 언급된 경우에만 포함돼                 |

```
---
description: RPC 서비스 보일러플레이트
globs:
alwaysApply: false
---

- 서비스를 정의할 때는 내부 RPC 패턴을 사용해
- 서비스 이름은 항상 snake_case를 사용해

@service-template.ts
```

<div id="nested-rules">
  ### 중첩 규칙
</div>

프로젝트 곳곳에 `.cursor/rules` 디렉터리를 두고 규칙을 정리해. 해당 디렉터리 안의 파일이 참조되면, 중첩 규칙이 자동으로 적용돼.

```
project/
  .cursor/rules/        # 프로젝트 전체 규칙
  backend/
    server/
      .cursor/rules/    # 백엔드 전용 규칙
  frontend/
    .cursor/rules/      # 프런트엔드 전용 규칙
```

<div id="creating-a-rule">
  ### 규칙 만들기
</div>

`New Cursor Rule` 명령을 사용하거나 `Cursor Settings > Rules`로 가서 규칙을 만들어. 그러면 `.cursor/rules`에 새 규칙 파일이 생성돼. 설정에서 모든 규칙과 상태를 한눈에 볼 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="간결한 규칙 vs 긴 규칙 비교" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### 규칙 생성
</div>

대화 중에 `/Generate Cursor Rules` 명령으로 규칙을 바로 만들어. 에이전트 동작을 어떻게 할지 정했고, 그걸 계속 쓰고 싶을 때 유용해.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    사용 중인 브라우저가 video 태그를 지원하지 않아.
  </video>
</Frame>

<div id="best-practices">
  ## 모범 사례
</div>

좋은 규칙은 명확한 초점, 실행 가능성, 그리고 적절한 범위를 갖춰야 해.

* 규칙은 500줄 이하로 유지하기
* 큰 규칙은 여러 개의 조합 가능한 규칙으로 나누기
* 구체적인 예시나 참조 파일 제공하기
* 애매한 가이드는 피하고, 내부 문서처럼 명확하게 쓰기
* 채팅에서 프롬프트를 반복할 땐 규칙을 재사용하기

<div id="examples">
  ## 예시
</div>

<AccordionGroup>
  <Accordion title="프론트엔드 컴포넌트와 API 검증 표준">
    이 규칙은 프론트엔드 컴포넌트의 기준을 정해:

    components 디렉터리에서 작업할 때:

    * 스타일링은 항상 Tailwind 사용
    * 애니메이션은 Framer Motion 사용
    * 컴포넌트 네이밍 컨벤션 준수

    이 규칙은 API 엔드포인트 검증을 강제해:

    API 디렉터리에서:

    * 모든 검증에 zod 사용
    * zod 스키마로 반환 타입 정의
    * 스키마에서 생성된 타입 export
  </Accordion>

  <Accordion title="Express 서비스와 React 컴포넌트 템플릿">
    이 규칙은 Express 서비스 템플릿을 제공해:

    Express 서비스를 만들 때 이 템플릿을 써:

    * RESTful 원칙 준수
    * 에러 핸들링 미들웨어 포함
    * 적절한 로깅 설정

    @express-service-template.ts

    이 규칙은 React 컴포넌트 구조를 정의해:

    React 컴포넌트는 다음 레이아웃을 따라야 해:

    * 맨 위에 Props 인터페이스
    * 컴포넌트는 named export
    * 스타일은 하단에 배치

    @component-template.tsx
  </Accordion>

  <Accordion title="개발 워크플로 자동화와 문서 생성">
    이 규칙은 앱 분석을 자동화해:

    앱 분석을 요청받으면:

    1. `npm run dev`로 dev 서버 실행
    2. 콘솔 로그 수집
    3. 성능 개선안 제안

    이 규칙은 문서 생성을 도와:

    문서 초안 작성 시:

    * 코드 주석 추출
    * README.md 분석
    * 마크다운 문서 생성
  </Accordion>

  <Accordion title="Cursor에 새 설정 추가하기">
    먼저 `@reactiveStorageTypes.ts`에 토글할 프로퍼티를 만들어.

    `@reactiveStorageService.tsx`의 `INIT_APPLICATION_USER_PERSISTENT_STORAGE`에 기본값을 추가해.

    베타 기능이면 `@settingsBetaTab.tsx`에 토글을 추가하고, 아니면 `@settingsGeneralTab.tsx`에 추가해. 일반 체크박스는 `<SettingsSubSection>`으로 추가할 수 있어. 예시는 파일의 나머지 부분을 참고해.

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    앱에서 사용하려면 reactiveStorageService를 import해서 해당 프로퍼티를 써:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

프로바이더와 프레임워크에서 제공되는 예시가 많아. 커뮤니티가 기여한 규칙은 크라우드소싱 컬렉션과 온라인 레포지토리 전반에서 찾아볼 수 있어.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md`는 에이전트 지침을 정의하는 간단한 마크다운 파일이야. 간단한 사용 사례라면 프로젝트 루트에 두고 `.cursor/rules`의 대안으로 쓰면 돼.

Project Rules와 달리 `AGENTS.md`는 메타데이터나 복잡한 설정이 없는 순수 마크다운 파일이야. 구조화된 규칙의 오버헤드 없이 간단하고 읽기 쉬운 지침이 필요한 프로젝트에 딱이야.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [개념](./section.md) →