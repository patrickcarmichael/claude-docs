---
title: "SSO"
source: "https://docs.cursor.com/ko/account/teams/sso"
language: "ko"
language_name: "Korean"
---

# SSO
Source: https://docs.cursor.com/ko/account/teams/sso

팀의 Single Sign-On 설정하기

<div id="overview">
  ## 개요
</div>

SAML 2.0 SSO는 Business 플랜에서 추가 비용 없이 제공돼. 기존 IdP(Identity Provider)를 사용해서 별도의 Cursor 계정 없이 팀원을 인증할 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## 사전 준비 사항
</div>

* Cursor Team 플랜
* ID 공급자(예: Okta)에 대한 관리자 권한
* Cursor 조직에 대한 관리자 권한

<div id="configuration-steps">
  ## 구성 단계
</div>

<Steps>
  <Step title="Cursor 계정에 로그인">
    관리자 계정으로 [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings)로 이동해.
  </Step>

  <Step title="SSO 구성 찾기">
    "Single Sign-On (SSO)" 섹션을 찾아 펼쳐.
  </Step>

  <Step title="설정 시작하기">
    "SSO Provider Connection settings" 버튼을 눌러 SSO 설정을 시작하고, 안내 마법사를 따라가.
  </Step>

  <Step title="IdP 구성">
    네 identity provider(예: Okta)에서:

    * 새 SAML 애플리케이션 만들기
    * Cursor 정보로 SAML 설정 구성하기
    * Just-in-Time(JIT) 프로비저닝 설정하기
  </Step>

  <Step title="도메인 인증">
    "Domain verification settings" 버튼을 눌러 Cursor에서 사용자 도메인을 인증해.
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Identity Provider 설정 가이드
</div>

제공자별 설정 방법은 여기에서 확인해:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Okta, Azure AD, Google Workspace 등 설정 가이드.
</Card>

<div id="additional-settings">
  ## 추가 설정
</div>

* 관리자 대시보드에서 SSO 강제 적용 관리
* 새 사용자는 SSO로 로그인하면 자동으로 등록돼
* 아이덴티티 제공자를 통해 사용자 관리 수행

<div id="troubleshooting">
  ## 문제 해결
</div>

문제가 생기면:

* Cursor에서 도메인이 인증되었는지 확인해줘
* SAML 속성이 올바르게 매핑됐는지 확인해줘
* 관리자 대시보드에서 SSO가 활성화돼 있는지 확인해줘
* 아이덴티티 제공자와 Cursor에서 이름(First name)과 성(Last name)이 일치하는지 확인해줘
* 위의 제공자별 가이드를 확인해봐
* 문제가 계속되면 [hi@cursor.com](mailto:hi@cursor.com)으로 연락해줘

---

← Previous: [시작하기](./section.md) | [Index](./index.md) | Next: [업데이트 접근 권한](./section.md) →