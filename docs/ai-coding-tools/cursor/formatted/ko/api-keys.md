---
title: "API Keys"
source: "https://docs.cursor.com/ko/settings/api-keys"
language: "ko"
language_name: "Korean"
---

# API Keys
Source: https://docs.cursor.com/ko/settings/api-keys

직접 LLM 제공업체 사용

네 비용으로 무제한 AI 메시지를 보내려면 네 API 키를 사용하면 돼. 설정해두면 Cursor가 네 API 키로 LLM 제공업체를 직접 호출해.

API 키를 쓰려면 `Cursor Settings` > `Models`로 가서 API 키를 입력해. 그런 다음 **Verify**를 클릭해. 검증이 끝나면 API 키가 활성화돼.

<Warning>
  커스텀 API 키는 표준 채팅 모델에서만 동작해. 특수 모델이 필요한 기능(예: Tab Completion)은 계속 Cursor의 기본 제공 모델을 사용할 거야.
</Warning>

<div id="supported-providers">
  ## 지원되는 제공자
</div>

* **OpenAI** - 표준(비-추론) 채팅 모델만 지원. 모델 선택기에서 사용 가능한 OpenAI 모델이 보여.
* **Anthropic** - Anthropic API를 통해 제공되는 모든 Claude 모델.
* **Google** - Google AI API를 통해 제공되는 Gemini 모델.
* **Azure OpenAI** - 너의 Azure OpenAI Service 인스턴스에 배포된 모델.
* **AWS Bedrock** - AWS 액세스 키, 시크릿 키, 또는 IAM 역할 사용. 너의 Bedrock 구성에서 사용 가능한 모델과 함께 작동해.

Bedrock IAM 역할을 검증한 후 고유한 External ID가 생성되고, 추가 보안을 위해 이 값을 IAM 역할 신뢰 정책에 추가할 수 있어.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="내 API 키가 저장되거나 기기를 벗어나?">
    네 API 키는 저장되지 않지만, 요청마다 우리 서버로 전송돼. 모든 요청은 최종 프롬프트 구성을 위해 우리 백엔드를 통해 라우팅돼.
  </Accordion>
</AccordionGroup>

---

← Previous: [모델](./section.md) | [Index](./index.md) | Next: [Tab](./tab.md) →