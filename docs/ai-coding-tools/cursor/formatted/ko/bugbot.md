---
title: "Bugbot"
source: "https://docs.cursor.com/ko/bugbot"
language: "ko"
language_name: "Korean"
---

# Bugbot
Source: https://docs.cursor.com/ko/bugbot

풀 리퀘스트용 AI 코드 리뷰

Bugbot은 풀 리퀘스트를 리뷰하고 버그, 보안 취약점, 코드 품질 문제를 찾아줘.

<Tip>
  Bugbot엔 무료 플랜이 있어: 모든 사용자가 매달 제한된 횟수의 무료 PR 리뷰를 받아. 한도에 도달하면 다음 결제 주기까지 리뷰가 잠시 멈춰. 표준 남용 방지 가드레일이 적용되는 무제한 리뷰를 위해 언제든 14일 무료 Pro 체험으로 업그레이드할 수 있어.
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="PR에 댓글을 남기는 Bugbot" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## 작동 방식
</div>

Bugbot은 PR diff를 분석해서 설명과 수정 제안을 담은 댓글을 남겨. 각 PR이 업데이트될 때마다 자동으로 실행되거나, 수동으로 트리거해서 실행할 수도 있어.

* PR이 업데이트될 때마다 **자동 리뷰** 실행
* 어떤 PR이든 `cursor review` 또는 `bugbot run` 댓글로 **수동 트리거**
* **Fix in Cursor** 링크로 이슈를 Cursor에서 바로 열 수 있어
* **Fix in Web** 링크로 이슈를 [cursor.com/agents](https://cursor.com/agents)에서 바로 열 수 있어

<div id="setup">
  ## 설정
</div>

Cursor 관리자 권한과 GitHub 조직 관리자 권한이 필요해.

1. [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)로 가
2. Bugbot 탭으로 이동해
3. `Connect GitHub` 클릭해 (이미 연결돼 있다면 `Manage Connections`)
4. GitHub 설치 흐름을 따라가
5. 대시보드로 돌아와서 특정 리포지토리에서 Bugbot을 활성화해

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot GitHub 설정" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## 구성
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### 리포지토리 설정

    설치 목록에서 리포지토리별로 Bugbot을 켜거나 꺼. Bugbot은 네가 만든 PR에서만 돌아가.

    ### 개인 설정

    * 댓글로 `cursor review` 또는 `bugbot run`을 달아 **언급됐을 때만 실행**
    * 이후 커밋은 건너뛰고 PR당 **한 번만 실행**
  </Tab>

  <Tab title="Team">
    ### 리포지토리 설정

    팀 관리자는 리포지토리별로 Bugbot을 켜고, 리뷰어 허용/차단 목록을 설정하며, 다음을 구성할 수 있어:

    * 설치 단위로 PR당 **한 번만 실행**, 이후 커밋은 건너뛰기
    * Bugbot이 코드 라인에 직접 댓글을 남기지 않도록 **인라인 리뷰 비활성화**

    Bugbot은 팀 소속 여부와 관계없이 활성화된 리포지토리의 모든 기여자에게 실행돼.

    ### 개인 설정

    팀 구성원은 자신의 PR에 대해 설정을 재정의할 수 있어:

    * 댓글로 `cursor review` 또는 `bugbot run`을 달아 **언급됐을 때만 실행**
    * 이후 커밋은 건너뛰고 PR당 **한 번만 실행**
    * 초안 풀 리퀘스트도 자동 리뷰에 포함되도록 **드래프트 PR에서 리뷰 활성화**
  </Tab>
</Tabs>

<div id="analytics">
  ### 분석
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot 대시보드" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## 규칙
</div>

프로젝트별 리뷰 컨텍스트를 제공하려면 `.cursor/BUGBOT.md` 파일을 만들어. Bugbot은 항상 루트의 `.cursor/BUGBOT.md` 파일과 변경된 파일에서 상위 디렉터리로 올라가며 찾은 모든 추가 파일을 포함해.

```
project/
  .cursor/BUGBOT.md          # 항상 포함됨(프로젝트 전체 규칙)
  backend/
    .cursor/BUGBOT.md        # 백엔드 파일 검토 시 포함됨
    api/
      .cursor/BUGBOT.md      # API 파일 검토 시 포함됨
  frontend/
    .cursor/BUGBOT.md        # 프런트엔드 파일 검토 시 포함됨
```

<AccordionGroup>
  <Accordion title="예시 .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # 프로젝트 리뷰 가이드라인

    ## 보안 중점 영역

    - API 엔드포인트에서 사용자 입력 검증
    - 데이터베이스 쿼리의 SQL 인젝션 취약점 점검
    - 보호된 라우트에 적절한 인증 보장

    ## 아키텍처 패턴

    - 서비스에 의존성 주입 사용
    - 데이터 접근에 리포지토리 패턴 적용
    - 커스텀 에러 클래스로 적절한 오류 처리 구현

    ## 흔한 문제

    - React 컴포넌트의 메모리 누수(useEffect 정리 함수 확인)
    - UI 컴포넌트에 오류 경계 누락
    - 일관되지 않은 네이밍 컨벤션(함수는 camelCase 사용)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## 요금제
</div>

Bugbot은 두 가지 요금제를 제공해: **Free**와 **Pro**.

<div id="free-tier">
  ### 무료 플랜
</div>

모든 사용자는 매달 제한된 횟수의 무료 PR 리뷰를 받게 돼. 팀이라면 각 팀원마다 자신의 무료 리뷰가 제공돼. 한도에 도달하면 다음 결제 주기까지 리뷰가 일시 중지돼. 언제든지 14일 무료 Pro 체험으로 업그레이드해서 무제한 리뷰를 쓸 수 있어.

<div id="pro-tier">
  ### 프로 티어
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### 정액제

    모든 리포지토리에서 한 달 최대 200개의 PR에 대해 Bugbot 무제한 리뷰: 월 \$40.

    ### 시작하기

    계정 설정에서 구독해.
  </Tab>

  <Tab title="Teams">
    ### 사용자별 과금

    팀은 사용자 1명당 월 \$40로 무제한 리뷰를 이용해.

    한 달 동안 Bugbot이 리뷰한 PR을 작성한 사람을 사용자로 집계해.

    모든 라이선스는 각 청구 주기 시작 시 반납되고, 선착순으로 재할당돼. 어떤 사용자가 한 달 동안 Bugbot이 리뷰한 PR을 하나도 작성하지 않으면, 그 좌석은 다른 사용자가 쓸 수 있어.

    ### 좌석 한도

    팀 관리자는 비용 관리를 위해 월별 Bugbot 좌석 최대치를 설정할 수 있어.

    ### 시작하기

    팀 대시보드에서 구독해 결제를 활성화해.

    ### 오남용 방지

    오남용을 막기 위해, 모든 Bugbot 라이선스에는 한 달 200개의 풀 리퀘스트라는 공유 상한이 있어. 한 달에 200개 이상이 필요하면 [hi@cursor.com](mailto:hi@cursor.com)으로 연락해 줘. 기꺼이 도와줄게.

    예를 들어, 팀에 사용자가 100명이라면, 조직은 처음에 한 달에 20,000개의 풀 리퀘스트를 리뷰할 수 있어. 그 한도에 자연스럽게 도달했다면 우리에게 연락해 줘. 한도를 높여줄게.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## 문제 해결
</div>

Bugbot이 작동하지 않을 때:

1. 자세한 로그와 요청 ID를 확인하려면 `cursor review verbose=true` 또는 `bugbot run verbose=true`를 **주석으로 추가해서 verbose 모드 켜기**
2. **권한 확인**해서 Bugbot이 저장소에 접근할 수 있는지 확인하기
3. **설치 확인**해서 GitHub 앱이 설치되고 활성화되어 있는지 확인하기

문제 신고할 때는 verbose 모드에서 나온 요청 ID를 꼭 포함해줘.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Bugbot는 privacy mode를 준수해?">
    응, Bugbot은 Cursor랑 같은 프라이버시 준수 기준을 따르고, 다른 Cursor 요청이랑 동일한 방식으로 데이터를 처리해.
  </Accordion>

  <Accordion title="무료 티어 한도에 도달하면 어떻게 돼?">
    월간 무료 티어 한도에 도달하면 다음 결제 주기까지 Bugbot 리뷰가 잠시 멈춰. 무제한 리뷰를 쓰려면 14일 무료 Pro 체험으로 업그레이드할 수 있어(표준 오남용 방지 가이드 적용).
  </Accordion>
</AccordionGroup>

```
```

---

← Previous: [웹 & 모바일](./section.md) | [Index](./index.md) | Next: [Code Review](./code-review.md) →