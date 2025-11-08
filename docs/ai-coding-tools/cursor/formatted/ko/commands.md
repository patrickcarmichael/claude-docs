---
title: "Commands"
source: "https://docs.cursor.com/ko/agent/chat/commands"
language: "ko"
language_name: "Korean"
---

# Commands
Source: https://docs.cursor.com/ko/agent/chat/commands

재사용 가능한 워크플로를 위한 명령 정의

사용자 지정 명령은 채팅 입력창에서 간단한 `/` 프리픽스로 호출할 수 있는 재사용 가능한 워크플로를 만들 수 있게 해줘. 이런 명령을 쓰면 팀 전반의 프로세스를 표준화하고, 반복적인 작업을 더 효율적으로 처리할 수 있어.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  명령은 현재 베타야. 기능과 문법은 계속 개선되는 과정에서 변경될 수 있어.
</Info>

<div id="how-commands-work">
  ## 명령어가 동작하는 방식
</div>

명령어는 두 위치에 저장할 수 있는 일반 Markdown 파일로 정의돼:

1. **프로젝트 명령어**: 네 프로젝트의 `.cursor/commands` 디렉터리에 저장됨
2. **글로벌 명령어**: 홈 디렉터리의 `~/.cursor/commands` 디렉터리에 저장됨

채팅 입력창에 `/`를 입력하면 Cursor가 두 디렉터리에서 사용 가능한 명령어를 자동으로 찾아 표시해서, 워크플로 전반에서 바로 쓸 수 있게 해줘.

<div id="creating-commands">
  ## 커맨드 만들기
</div>

1. 프로젝트 루트에 `.cursor/commands` 디렉터리를 만든다
2. 의미 있는 이름의 `.md` 파일을 추가한다 (예: `review-code.md`, `write-tests.md`)
3. 커맨드가 수행해야 할 내용을 일반 Markdown으로 작성한다
4. 채팅창에서 `/`를 입력하면 커맨드가 자동으로 표시된다

커맨드 디렉터리 구조는 대략 이렇게 될 수 있어:

```
.cursor/
└── commands/
    ├── address-github-pr-comments.md
    ├── code-review-checklist.md
    ├── create-pr.md
    ├── light-review-existing-diffs.md
    ├── onboard-new-developer.md
    ├── run-all-tests-and-fix.md
    ├── security-audit.md
    └── setup-new-feature.md
```

<div id="examples">
  ## 예시
</div>

프로젝트에서 이 명령어들을 직접 써 보면서 어떻게 작동하는지 감을 잡아봐.

<AccordionGroup>
  <Accordion title="코드 리뷰 체크리스트">
    ```markdown  theme={null}
    # 코드 리뷰 체크리스트

    ## 개요
    품질, 보안, 유지관리성을 보장하기 위한 철저한 코드 리뷰용 종합 체크리스트.

    ## 리뷰 범주

    ### 기능
    - [ ] 코드가 의도대로 동작함
    - [ ] 경계/특수 케이스가 처리됨
    - [ ] 오류 처리가 적절함
    - [ ] 명백한 버그나 로직 오류가 없음

    ### 코드 품질
    - [ ] 코드가 읽기 쉽고 구조가 잘 잡혀 있음
    - [ ] 함수가 작고 한 가지 책임에 집중함
    - [ ] 변수명이 명확하고 설명적임
    - [ ] 코드 중복이 없음
    - [ ] 프로젝트 컨벤션을 준수함

    ### 보안
    - [ ] 명백한 보안 취약점이 없음
    - [ ] 입력 검증이 구현되어 있음
    - [ ] 민감한 데이터가 적절히 처리됨
    - [ ] 하드코딩된 시크릿이 없음
    ```
  </Accordion>

  <Accordion title="보안 감사">
    ```markdown  theme={null}
    # 보안 감사

    ## 개요
    코드베이스의 취약점을 식별하고 해결하기 위한 종합 보안 점검.

    ## 단계
    1. **의존성 감사**
       - 알려진 취약점 확인
       - 구버전 패키지 업데이트
       - 서드파티 의존성 검토

    2. **코드 보안 검토**
       - 공통 취약점 확인
       - 인증/인가 검토
       - 데이터 처리 관행 점검

    3. **인프라 보안**
       - 환경 변수 검토
       - 접근 제어 확인
       - 네트워크 보안 점검

    ## 보안 체크리스트
    - [ ] 의존성 최신화 및 안전성 확보
    - [ ] 하드코딩된 시크릿 없음
    - [ ] 입력 검증 구현 완료
    - [ ] 인증 안전함
    - [ ] 인가가 올바르게 구성됨
    ```
  </Accordion>

  <Accordion title="새 기능 설정">
    ```markdown  theme={null}
    # 새 기능 설정

    ## 개요
    초기 기획부터 구현 구조까지 새 기능을 체계적으로 준비해.

    ## 단계
    1. **요구사항 정의**
       - 기능 범위와 목표를 명확히 해
       - 사용자 스토리와 승인 기준을 정리해
       - 기술적 접근 방식을 계획해

    2. **기능 브랜치 생성**
       - main/develop에서 브랜치 따와
       - 로컬 개발 환경을 준비해
       - 새 의존성을 설정해

    3. **아키텍처 설계**
       - 데이터 모델과 API를 설계해
       - UI 컴포넌트와 플로우를 계획해
       - 테스트 전략을 수립해

    ## 기능 설정 체크리스트
    - [ ] 요구사항 문서화 완료
    - [ ] 사용자 스토리 작성 완료
    - [ ] 기술적 접근 방식 계획 완료
    - [ ] 기능 브랜치 생성 완료
    - [ ] 개발 환경 준비 완료
    ```
  </Accordion>

  <Accordion title="풀 리퀘스트 생성">
    ```markdown  theme={null}
    # PR 생성

    ## 개요
    명확한 설명, 라벨, 리뷰어를 갖춘 잘 구조화된 풀 리퀘스트를 만들어.

    ## 단계
    1. **브랜치 준비**
       - 모든 변경 사항이 커밋되었는지 확인
       - 브랜치를 원격에 푸시
       - 브랜치가 main과 최신 상태인지 확인

    2. **PR 설명 작성**
       - 변경 사항을 명확하게 요약
       - 배경 및 동기 포함
       - 브레이킹 체인지가 있다면 나열
       - UI 변경이 있으면 스크린샷 추가

    3. **PR 설정**
       - 내용을 잘 드러내는 제목으로 PR 생성
       - 적절한 라벨 추가
       - 리뷰어 지정
       - 관련 이슈 링크

    ## PR 템플릿
    - [ ] 기능 A
    - [ ] 버그 수정 B
    - [ ] 단위 테스트 통과
    - [ ] 수동 테스트 완료
    ```
  </Accordion>

  <Accordion title="테스트를 실행하고 실패를 고쳐">
    ```markdown  theme={null}
    # 모든 테스트 실행 및 실패 수정

    ## 개요
    전체 테스트 스위트를 실행하고 실패를 체계적으로 수정해서 코드 품질과 기능을 보장해.

    ## 단계
    1. **테스트 스위트 실행**
       - 프로젝트의 모든 테스트를 실행해
       - 출력을 캡처하고 실패를 식별해
       - 단위 테스트와 통합 테스트를 모두 확인해

    2. **실패 분석**
       - 유형별로 분류: 플래키, 깨짐, 신규 실패
       - 영향도에 따라 수정 우선순위를 정해
       - 최근 변경과 관련된 실패인지 확인해

    3. **체계적으로 이슈 수정**
       - 가장 중요한 실패부터 시작해
       - 한 번에 하나의 이슈만 수정해
       - 각 수정 후 테스트를 다시 실행해
    ```
  </Accordion>

  <Accordion title="새 개발자 온보딩">
    ```markdown  theme={null}
    # 새 개발자 온보딩

    ## 개요
    새 개발자가 빠르게 작업을 시작하도록 돕는 종합 온보딩 프로세스.

    ## 단계
    1. **환경 설정**
       - 필수 도구 설치
       - 개발 환경 구성
       - IDE 및 확장 프로그램 설정
       - Git 및 SSH 키 설정

    2. **프로젝트 익히기**
       - 프로젝트 구조 검토
       - 아키텍처 파악
       - 핵심 문서 읽기
       - 로컬 데이터베이스 구성

    ## 온보딩 체크리스트
    - [ ] 개발 환경 준비 완료
    - [ ] 모든 테스트 통과
    - [ ] 로컬에서 애플리케이션 실행 가능
    - [ ] 데이터베이스 구성 및 정상 동작
    - [ ] 첫 PR 제출
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [Compact](./compact.md) →