---
title: "Linear"
source: "https://docs.cursor.com/ko/integrations/linear"
language: "ko"
language_name: "Korean"
---

# Linear
Source: https://docs.cursor.com/ko/integrations/linear

Linear에서 Background Agents 사용하기

이슈를 Cursor에 위임하거나 댓글에서 `@Cursor`를 멘션해서 Linear에서 바로 [Background Agents](/ko/background-agent)를 사용해.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## 시작하기
</div>

<div id="installation">
  ### 설치
</div>

<Note>
  Linear 통합을 연결하려면 Cursor 관리자여야 해. 다른 팀 설정은 비관리자 멤버도 사용할 수 있어.
</Note>

1. [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)로 이동
2. Linear 옆의 *Connect* 클릭
3. Linear 워크스페이스를 연결하고 팀 선택
4. *Authorize* 클릭
5. Cursor에서 남은 Background Agent 설정 마무리:
   * GitHub 연결하고 기본 리포지토리 선택
   * 사용량 기반 과금 켜기
   * 개인정보 설정 확인

<div id="account-linking">
  ### 계정 연결
</div>

처음 사용할 때 Cursor랑 Linear 계정을 연결해야 해. PR 만들려면 GitHub 연결이 필요해.

<div id="how-to-use">
  ## 사용 방법
</div>

이슈를 Cursor에 맡기거나 댓글에 `@Cursor`를 멘션해. Cursor가 이슈를 분석해서 비개발 업무는 자동으로 걸러줘.

<div id="delegating-issues">
  ### 이슈 위임하기
</div>

1. Linear 이슈 열기
2. 담당자 필드 클릭
3. "Cursor" 선택

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Linear에서 Cursor에 이슈를 위임하기" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Cursor 멘션하기
</div>

새 에이전트를 배정하거나 추가 지침을 알려주려면 댓글에 `@Cursor`를 멘션해. 예: `@Cursor 위에 설명한 인증 버그를 고쳐줘`.

<div id="workflow">
  ## 워크플로우
</div>

Background Agents는 Linear에서 실시간 상태를 표시하고 완료되면 자동으로 PR을 만들어. 진행 상황은 [Cursor 대시보드](https://www.cursor.com/dashboard?tab=background-agents)에서 확인할 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Linear의 Background Agent 상태 업데이트" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### 후속 안내
</div>

에이전트 세션에서 답장하면 에이전트에 대한 후속 메시지로 전송돼. 실행 중인 Background Agent에 추가 지침을 주려면 Linear 댓글에서 `@Cursor`를 멘션하면 돼.

<div id="configuration">
  ## 구성
</div>

[Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents)에서 Background Agent 설정을 관리해.

<div className="full-width-table">
  | Setting                | Location         | Description                            |
  | :--------------------- | :--------------- | :------------------------------------- |
  | **Default Repository** | Cursor Dashboard | 프로젝트 리포지토리가 지정되지 않았을 때 사용할 기본 리포지토리    |
  | **Default Model**      | Cursor Dashboard | Background Agents에 사용할 AI 모델           |
  | **Base Branch**        | Cursor Dashboard | PR을 생성할 기준 브랜치(보통 `main` 또는 `develop`) |
</div>

<div id="configuration-options">
  ### 구성 옵션
</div>

Background Agent 동작은 여러 방법으로 설정할 수 있어:

**Issue description or comments**: `[key=value]` 문법을 써. 예:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Issue labels**: 상위-하위 레이블 구조를 사용해. 상위 레이블은 구성 키, 하위 레이블은 값이야.

**Project labels**: 이슈 레이블과 동일한 상위-하위 구조를 프로젝트 레벨에 적용해.

지원되는 구성 키:

* `repo`: 대상 리포지토리 지정(예: `owner/repository`)
* `branch`: PR 생성 시 기준 브랜치 지정
* `model`: 사용할 AI 모델 지정

<div id="repository-selection">
  ### 리포지토리 선택
</div>

Cursor는 다음 우선순위로 작업할 리포지토리를 결정해:

1. **Issue description/comments**: 이슈 본문이나 코멘트의 `[repo=owner/repository]` 문법
2. **Issue labels**: 해당 Linear 이슈에 연결된 리포지토리 레이블
3. **Project labels**: Linear 프로젝트에 연결된 리포지토리 레이블
4. **Default repository**: Cursor 대시보드 설정에 지정된 리포지토리

<div id="setting-up-repository-labels">
  #### 리포지토리 레이블 설정
</div>

Linear에서 리포지토리 레이블을 만들려면:

1. Linear 워크스페이스의 **Settings**로 이동
2. **Labels** 클릭
3. **New group** 클릭
4. 그룹 이름을 "repo"로 지정(대소문자 무시 - 반드시 정확히 "repo"여야 하고 "Repository" 등 변형은 불가)
5. 해당 그룹 안에 `owner/repo` 형식으로 각 리포지토리 레이블 생성

이 레이블을 이슈나 프로젝트에 할당해서 Background Agent가 작업할 리포지토리를 지정할 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Linear에서 리포지토리 레이블 구성하기" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →