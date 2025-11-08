---
title: "Pricing"
source: "https://docs.cursor.com/ko/account/pricing"
language: "ko"
language_name: "Korean"
---

# Pricing
Source: https://docs.cursor.com/ko/account/pricing

Cursor의 요금제와 가격

Cursor는 무료로 써보거나 개인/팀 요금제를 구매할 수 있어.

<div id="individual">
  ## 개인
</div>

모든 개인 플랜에는 다음이 포함돼:

* 무제한 탭 자동완성
* 모든 모델에 대한 확장된 에이전트 사용 한도
* Bugbot 접근
* Background Agents 접근

각 플랜에는 모델 추론 [API 가격](/ko/models#model-pricing)에 따라 사용량이 청구돼:

* Pro에는 API 에이전트 사용 \$20 + 추가 보너스 사용 포함
* Pro Plus에는 API 에이전트 사용 \$70 + 추가 보너스 사용 포함
* Ultra에는 API 에이전트 사용 \$400 + 추가 보너스 사용 포함

보장된 포함 사용량 외에 추가 보너스 용량을 제공하려고 계속 노력하고 있어. 모델마다 API 비용이 달라서, 선택한 모델에 따라 토큰 출력과 포함 사용량이 소진되는 속도가 달라져. [대시보드](https://cursor.com/dashboard?tab=usage)에서 사용량과 토큰 상세를 확인할 수 있어. 에디터에서는 한도 알림이 수시로 표시돼.

<img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c42b8ad6347f6fe9d075647dfece934c" alt="사용 한도" style={{ borderRadius: 16 }} data-og-width="666" width="666" data-og-height="394" height="394" data-path="images/account/usage-limits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1ca3b5ab64a6ba6f3ad7d75b1ee72e2 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d39dc254e7d059ac24310f26ea47dd5d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=153472f14b4c10ec9a096b7a9db59888 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc8b0cdb5c0677e45c1a082d0002880 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=cf4ac9875f5e587d16d4c6f1e7fdc057 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=13f21676cda8e4c2973bc3371892f4aa 2500w" />

<div id="how-much-usage-do-i-need">
  ### 어느 정도 써야 충분할까?
</div>

우리 사용 데이터 기준으로, 대략 아래 정도를 예상할 수 있어:

* **Daily Tab 사용자**: 항상 \$20 이내
* **Limited Agent 사용자**: 포함된 \$20 안에 머무르는 경우가 많아
* **Daily Agent 사용자**: 보통 월 총 사용 $60–$100
* **파워 유저(복수 에이전트/자동화)**: 종종 월 총 사용 \$200+

우리 사용 데이터 기준으로, *중간 사용자*에게 한도는 대략 다음과 비슷해:

* Pro: Sonnet 4 요청 약 225회, Gemini 요청 약 550회, 또는 GPT 5 요청 약 500회
* Pro+: Sonnet 4 요청 약 675회, Gemini 요청 약 1,650회, 또는 GPT 5 요청 약 1,500회
* Ultra: Sonnet 4 요청 약 4,500회, Gemini 요청 약 11,000회, 또는 GPT 5 요청 약 10,000회

<div id="what-happens-when-i-reach-my-limit">
  ### 한도에 도달하면 어떻게 돼?
</div>

포함된 월간 사용량을 초과하면 에디터에서 알림이 뜨고 다음 중에서 선택할 수 있어:

* **온디맨드 사용량 추가**: 동일한 API 요율로 종량제 결제로 Cursor 계속 쓰기
* **플랜 업그레이드**: 더 많은 포함 사용량이 제공되는 상위 티어로 올리기

온디맨드 사용량은 포함 사용량과 동일한 요율로 월별 청구돼. 요청의 품질이나 속도가 저하되는 일은 절대 없어.

<div id="teams">
  ## Teams
</div>

팀 플랜은 두 가지야: Teams (\$40/사용자/월)와 Enterprise(맞춤).

Teams 플랜은 다음과 같은 추가 기능을 제공해:

* Privacy Mode 강제 적용
* 사용량 통계가 포함된 Admin 대시보드
* 팀 결제 중앙화
* SAML/OIDC SSO

셀프 서비스로 충분한 경우엔 Teams를 추천해. 우선 지원, 사용량 풀링, 청구서 결제, SCIM, 고급 보안 제어가 필요하다면 [Enterprise](/ko/contact-sales)를 추천해.

[Teams 가격](/ko/account/teams/pricing)에 대해 더 알아봐.

<div id="auto">
  ## Auto
</div>

Auto를 켜면 Cursor가 현재 수요를 기준으로 즉시 작업에 가장 잘 맞고 신뢰성이 가장 높은 프리미엄 모델을 골라줘. 이 기능은 출력 성능 저하를 감지하면 문제를 해결하기 위해 자동으로 모델을 전환할 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
</Frame>

<Note>우린 Auto의 품질과 전반적인 성능에 크게 투자했어. 9월 15일 이후 다음 결제 갱신부터 Auto는 아래 API 요율로 사용량이 청구돼.</Note>

* **Input + Cache Write**: 1M tokens당 \$1.25
* **Output**: 1M tokens당 \$6.00
* **Cache Read**: 1M tokens당 \$0.25

에디터와 대시보드 모두 Auto를 포함한 사용량을 보여줘. 직접 모델을 고르길 원하면 해당 모델의 리스트 API 가격으로 사용량이 청구돼.

<div id="max-mode">
  ## Max Mode
</div>

일부 모델은 [Max Mode](/ko/models#max-mode)를 사용할 수 있어서, 최대 1M 토큰까지 더 긴 추론과 더 큰 컨텍스트 윈도를 지원해. 대부분의 코딩 작업에는 Max Mode가 필요 없지만, 특히 큰 파일이나 코드베이스를 다루는 복잡한 쿼리에는 도움이 될 수 있어. Max Mode를 사용하면 사용량이 더 늘어나. 모든 요청과 토큰 사용 내역은 [대시보드](https://cursor.com/dashboard?tab=usage)에서 확인할 수 있어.

<div id="bugbot">
  ## Bugbot
</div>

Bugbot은 Cursor 구독과는 별개의 제품이고, 자체 요금제가 있어.

* **Pro** (\$40/월): 월 최대 200개 PR에 대한 무제한 리뷰, Cursor Ask 무제한 이용, 버그 수정을 위한 Cursor 연동, Bugbot Rules 이용 가능
* **Teams** (\$40/사용자/월): 모든 PR에 대한 무제한 코드 리뷰, Cursor Ask 무제한 이용, 팀 단위 풀 사용량, 고급 규칙과 설정
* **Enterprise** (맞춤형): Teams의 모든 기능에 더해 고급 분석과 보고, 우선 지원, 계정 관리

[Bugbot 요금제](https://cursor.com/bugbot#pricing)를 자세히 알아봐.

<div id="background-agent">
  ## Background Agent
</div>

Background Agent는 선택한 [model](/ko/models)의 API 요금이 적용돼. 처음 쓸 때 Background Agent의 지출 한도를 설정하라는 안내가 뜰 거야.

<Info>
  Background Agent용 Virtual Machine(VM) 컴퓨트 요금은 추후 책정될 예정이야.
</Info>

---

← Previous: [Billing](./billing.md) | [Index](./index.md) | Next: [Admin API](./admin-api.md) →