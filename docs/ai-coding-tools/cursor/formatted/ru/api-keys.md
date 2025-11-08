---
title: "API Keys"
source: "https://docs.cursor.com/ru/settings/api-keys"
language: "ru"
language_name: "Russian"
---

# API Keys
Source: https://docs.cursor.com/ru/settings/api-keys

Используй своего LLM‑провайдера

Используй свои API‑ключи, чтобы отправлять неограниченные AI‑сообщения за свой счёт. После настройки Cursor будет использовать твои API‑ключи для прямых вызовов к LLM‑провайдерам.

Чтобы использовать свой API‑ключ, открой `Cursor Settings` > `Models` и введи свои API‑ключи. Нажми **Verify**. После проверки твой API‑ключ будет активирован.

<Warning>
  Собственные API‑ключи работают только со стандартными чат‑моделями. Функции, которым нужны специализированные модели (например, Tab Completion), продолжат использовать встроенные модели Cursor.
</Warning>

<div id="supported-providers">
  ## Поддерживаемые провайдеры
</div>

* **OpenAI** — только стандартные чат‑модели без reasoning. Переключатель моделей покажет доступные модели OpenAI.
* **Anthropic** — все модели Claude, доступные через Anthropic API.
* **Google** — модели Gemini, доступные через Google AI API.
* **Azure OpenAI** — модели, развернутые в твоем экземпляре Azure OpenAI Service.
* **AWS Bedrock** — используй AWS access keys, secret keys или IAM‑роли. Работает с моделями, доступными в твоей конфигурации Bedrock.

Уникальный внешний ID создается после проверки твоей Bedrock IAM‑роли; его можно добавить в политику доверия IAM‑роли для дополнительной безопасности.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Мой API‑ключ будет где-то храниться или покидать моё устройство?">
    Твой API‑ключ не хранится, но отправляется на наш сервер с каждым запросом. Все запросы проходят через наш бэкенд для финальной сборки промпта.
  </Accordion>
</AccordionGroup>

---

← Previous: [Модели](./section.md) | [Index](./index.md) | Next: [Tab](./tab.md) →