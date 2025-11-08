---
title: "Analytics"
source: "https://docs.cursor.com/ko/account/teams/analytics"
language: "ko"
language_name: "Korean"
---

# Analytics
Source: https://docs.cursor.com/ko/account/teams/analytics

팀 사용량 및 활동 지표 추적

팀 관리자는 [대시보드](/ko/account/teams/dashboard)에서 지표를 확인할 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Total Usage
</div>

팀 전체의 집계 지표를 확인해. 총 탭 수와 프리미엄 요청을 포함해. 팀 생성 후 30일이 안 된 경우엔 생성 이후 사용량이 반영되고, 팀원이 합류하기 전 활동도 포함돼.

<div id="per-active-user">
  ### Per Active User
</div>

활성 사용자 1인당 평균 지표를 확인해: 수락된 탭, 코드 라인 수, 프리미엄 요청.

<div id="user-activity">
  ### User Activity
</div>

주간 및 월간 활성 사용자를 추적해.

<div id="analytics-report-headers">
  ## 분석 보고서 헤더
</div>

대시보드에서 분석 데이터를 내보내면 보고서에 사용자 행동과 기능 사용에 대한 상세 지표가 포함돼. 각 헤더의 의미는 다음과 같아:

<div id="user-information">
  ### 사용자 정보
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  분석 데이터가 기록된 날짜 (예: 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  시스템에서 각 사용자를 식별하는 고유 ID
</ResponseField>

<ResponseField name="Email" type="string">
  계정에 연결된 사용자의 이메일 주소
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  해당 날짜에 사용자가 활성 상태였는지 표시
</ResponseField>

<div id="ai-generated-code-metrics">
  ### AI 생성 코드 메트릭
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  AI 채팅 기능이 제안한 추가 코드 라인의 총합
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  AI 채팅이 삭제를 제안한 코드 라인의 총합
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  사용자가 수락해 코드에 추가한 AI 제안 라인 수
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  사용자가 수락한 AI 제안 삭제 라인 수
</ResponseField>

<div id="feature-usage-metrics">
  ### 기능 사용 메트릭
</div>

<ResponseField name="Chat Total Applies" type="number">
  사용자가 채팅에서 AI 생성 변경을 적용한 횟수
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  사용자가 AI 제안을 수락한 횟수
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  사용자가 AI 제안을 거부한 횟수
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  사용자에게 AI 제안 탭이 표시된 횟수
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  사용자가 수락한 AI 제안 탭 수
</ResponseField>

<div id="request-type-metrics">
  ### 요청 유형 메트릭
</div>

<ResponseField name="Edit Requests" type="number">
  composer/edit 기능을 통해 발생한 요청 (Cmd+K 인라인 편집)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  사용자가 AI에 질문한 채팅 요청
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  AI 에이전트(특화된 AI 어시스턴트)에게 보낸 요청
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Cmd+K(또는 Ctrl+K) 커맨드 팔레트를 사용한 횟수
</ResponseField>

<div id="subscription-and-api-metrics">
  ### 구독 및 API 메트릭
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  사용자의 구독 플랜에 포함된 AI 요청
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  프로그래매틱 액세스를 위해 API 키로 수행된 요청
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  사용량 기반 과금에 포함되는 요청
</ResponseField>

<div id="additional-features">
  ### 추가 기능
</div>

<ResponseField name="Bugbot Usages" type="number">
  버그 탐지/수정 AI 기능 사용 횟수
</ResponseField>

<div id="configuration-information">
  ### 구성 정보
</div>

<ResponseField name="Most Used Model" type="string">
  사용자가 가장 자주 사용한 AI 모델 (예: GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  AI 제안을 적용할 때 가장 자주 사용된 파일 확장자 (예: .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  탭 완성 기능에서 가장 자주 사용된 파일 확장자
</ResponseField>

<ResponseField name="Client Version" type="string">
  사용 중인 Cursor 에디터 버전
</ResponseField>

<div id="calculated-metrics">
  ### 계산된 메트릭
</div>

보고서에는 AI 코드 기여도를 이해하는 데 도움이 되는 처리된 데이터도 포함돼:

* 총 추가/삭제 라인: 모든 코드 변경의 원시 개수
* 수락된 추가/삭제 라인: AI 제안에서 비롯돼 수락된 라인 수
* Composer Requests: 인라인 composer 기능을 통해 발생한 요청
* Chat Requests: 채팅 인터페이스를 통해 발생한 요청

<Note>
  숫자 값은 존재하지 않으면 기본값 0, boolean 값은 기본값 false,
  문자열 값은 기본값 빈 문자열이야. 메트릭은 사용자별로 일 단위로 집계돼.
</Note>

---

← Previous: [AI Code Tracking API](./ai-code-tracking-api.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →