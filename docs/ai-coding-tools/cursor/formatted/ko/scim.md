---
title: "SCIM"
source: "https://docs.cursor.com/ko/account/teams/scim"
language: "ko"
language_name: "Korean"
---

# SCIM
Source: https://docs.cursor.com/ko/account/teams/scim

사용자와 그룹의 자동 관리용 SCIM 프로비저닝 설정

<div id="overview">
  ## 개요
</div>

SCIM 2.0 프로비저닝은 아이덴티티 제공자를 통해 팀 구성원과 디렉터리 그룹을 자동으로 관리해. SSO가 활성화된 Enterprise 플랜에서 사용할 수 있어.

<product_visual type="screenshot">
  Active Directory Management 구성으로 표시된 SCIM 설정 대시보드
</product_visual>

<div id="prerequisites">
  ## 사전 준비 사항
</div>

* Cursor Enterprise 플랜
* SSO가 먼저 구성되어 있어야 함 — **SCIM에는 활성화된 SSO 연결이 필요함**
* 아이덴티티 제공자(Okta, Azure AD 등)에 대한 관리자 권한
* Cursor 조직에 대한 관리자 권한

<div id="how-it-works">
  ## 동작 방식
</div>

<div id="user-provisioning">
  ### 사용자 프로비저닝
</div>

IDP의 SCIM 애플리케이션에 할당되면 사용자는 자동으로 Cursor에 추가돼. 할당 해제되면 제거돼. 변경 사항은 실시간으로 동기화돼.

<div id="directory-groups">
  ### 디렉터리 그룹
</div>

디렉터리 그룹과 멤버십은 IDP에서 동기화돼. 그룹과 사용자 관리는 IDP에서만 해야 해 — Cursor는 이 정보를 읽기 전용으로 보여줘.

<div id="spend-management">
  ### 지출 관리
</div>

디렉터리 그룹별로 사용자당 지출 한도를 다르게 설정해. 디렉터리 그룹 한도가 팀 수준 한도보다 우선이야. 여러 그룹에 속한 사용자는 적용 가능한 한도 중 가장 높은 한도가 적용돼.

<div id="setup">
  ## 설정
</div>

<Steps>
  <Step title="SSO가 구성되어 있는지 확인">
    SCIM을 쓰려면 먼저 SSO가 설정돼 있어야 해. 아직 SSO를 안 했다면,
    진행하기 전에 [SSO 설정 가이드](/ko/account/teams/sso)를 따라줘.
  </Step>

  <Step title="Active Directory Management에 접근">
    관리자 계정으로
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    로 이동하거나, 대시보드 설정에서
    "Active Directory Management" 탭을 선택해.
  </Step>

  <Step title="SCIM 설정 시작">
    SSO가 확인되면 단계별 SCIM 설정 링크가 보여. 이걸 클릭해서
    설정 마법사를 시작해.
  </Step>

  <Step title="아이덴티티 제공자에서 SCIM 구성">
    아이덴티티 제공자에서: - SCIM 애플리케이션 생성 또는 구성 - Cursor가 제공한 SCIM 엔드포인트와 토큰 사용 - 사용자 및 그룹 푸시 프로비저닝 활성화 - 연결 테스트
  </Step>

  <Step title="지출 한도 구성(선택)">
    Cursor의 Active Directory Management 페이지로 돌아와서: - 동기화된
    디렉터리 그룹 확인 - 필요에 따라 특정 그룹에 사용자별 지출 한도 설정 -
    여러 그룹에 속한 사용자에게 적용되는 한도 검토
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### 아이덴티티 제공자 설정
</div>

제공자별 설정 방법은 아래를 참고해:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Okta, Azure AD, Google Workspace 등 설정 안내.
</Card>

<div id="managing-users-and-groups">
  ## 사용자와 그룹 관리
</div>

<Warning>
  모든 사용자와 그룹 관리는 IdP(아이덴티티 프로바이더)에서만 관리해야 해.
  IdP에서 변경한 내용은 자동으로 Cursor랑 동기화되지만,
  Cursor에서 사용자나 그룹을 직접 수정할 수는 없어.
</Warning>

<div id="user-management">
  ### 사용자 관리
</div>

* IdP에서 SCIM 애플리케이션에 할당해서 사용자를 추가해
* SCIM 애플리케이션에서 할당 해제해서 사용자를 제거해
* 사용자 프로필 변경(이름, 이메일)은 IdP에서 자동으로 동기화돼

<div id="group-management">
  ### 그룹 관리
</div>

* 디렉터리 그룹은 IdP에서 자동으로 동기화돼
* 그룹 멤버십 변경은 실시간으로 반영돼
* 그룹을 활용해 사용자를 조직하고 서로 다른 지출 한도를 설정해

<div id="spend-limits">
  ### 지출 한도
</div>

* 각 디렉터리 그룹마다 사용자별 한도를 다르게 설정해
* 사용자는 속한 그룹 중 가장 높은 지출 한도를 상속받아
* 그룹 한도가 팀 전체 기본 사용자별 한도보다 우선이야

<div id="faq">
  ## FAQ
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### 내 대시보드에 SCIM 관리가 안 보이는 이유가 뭐야?
</div>

SCIM을 설정하기 전에 SSO가 제대로 구성돼 있고 정상 작동하는지 확인해. SCIM은 작동하려면 활성 SSO 연결이 필요해.

<div id="why-arent-users-syncing">
  ### 사용자 동기화가 안 되는 이유가 뭐야?
</div>

아이덴티티 프로바이더에서 사용자가 SCIM 애플리케이션에 할당돼 있는지 확인해. 사용자가 Cursor에 나타나려면 명시적으로 할당돼 있어야 해.

<div id="why-arent-groups-appearing">
  ### 그룹이 안 보이는 이유가 뭐야?
</div>

아이덴티티 프로바이더의 SCIM 설정에서 그룹 푸시 프로비저닝이 활성화돼 있는지 확인해. 그룹 동기화는 사용자 동기화와 별도로 설정해야 해.

<div id="why-arent-spend-limits-applying">
  ### 지출 한도가 적용되지 않는 이유가 뭐야?
</div>

아이덴티티 프로바이더에서 사용자가 기대한 그룹에 제대로 할당돼 있는지 확인해. 적용되는 지출 한도는 그룹 멤버십으로 결정돼.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### Cursor에서 SCIM 사용자와 그룹을 직접 관리할 수 있어?
</div>

아니. 모든 사용자와 그룹 관리는 아이덴티티 프로바이더에서만 해야 해. Cursor는 이 정보를 읽기 전용으로 표시해.

<div id="how-quickly-do-changes-sync">
  ### 변경 사항은 얼마나 빨리 동기화돼?
</div>

아이덴티티 프로바이더에서 이뤄진 변경 사항은 실시간으로 Cursor에 동기화돼. 대량 일괄 작업은 잠깐 지연될 수 있어.

---

← Previous: [구성원 & 역할](./section.md) | [Index](./index.md) | Next: [시작하기](./section.md) →