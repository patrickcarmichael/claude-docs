---
title: "SSO"
source: "https://docs.cursor.com/ru/account/teams/sso"
language: "ru"
language_name: "Russian"
---

# SSO
Source: https://docs.cursor.com/ru/account/teams/sso

Настрой единый вход для своей команды

<div id="overview">
  ## Обзор
</div>

SAML 2.0 SSO доступен без доплаты в тарифах Business. Используй своего текущего провайдера идентификации (IdP), чтобы аутентифицировать участников команды без отдельных аккаунтов в Cursor.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Предварительные требования
</div>

* Тариф Cursor Team
* Права администратора в твоём провайдере идентификации (например, Okta)
* Права администратора в твоей организации Cursor

<div id="configuration-steps">
  ## Шаги настройки
</div>

<Steps>
  <Step title="Sign in to your Cursor account">
    Зайди на [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) под админ-аккаунтом.
  </Step>

  <Step title="Locate the SSO configuration">
    Найди раздел «Single Sign-On (SSO)» и разверни его.
  </Step>

  <Step title="Begin the setup process">
    Нажми кнопку «SSO Provider Connection settings», чтобы начать настройку SSO, и следуй мастеру.
  </Step>

  <Step title="Configure your identity provider">
    В своём провайдере идентификации (например, Okta):

    * Создай новое SAML‑приложение
    * Настрой параметры SAML, используя информацию Cursor
    * Включи Just‑in‑Time (JIT) провижнинг
  </Step>

  <Step title="Verify domain">
    Подтверди домен своих пользователей в Cursor, нажав кнопку «Domain verification settings».
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Руководства по настройке провайдера идентификации
</div>

Для инструкций, специфичных для конкретного провайдера:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Инструкции по настройке для Okta, Azure AD, Google Workspace и других.
</Card>

<div id="additional-settings">
  ## Дополнительные настройки
</div>

* Настраивай обязательное использование SSO через админ‑панель
* Новые пользователи автоматически подключаются при входе через SSO
* Управляй пользователями через своего провайдера идентификации

<div id="troubleshooting">
  ## Устранение неполадок
</div>

Если возникают проблемы:

* Проверь, что домен подтверждён в Cursor
* Убедись, что атрибуты SAML корректно сопоставлены
* Проверь, что SSO включён в админ‑панели
* Сверь имя и фамилию между провайдером идентификации и Cursor
* Ознакомься с руководствами по конкретным провайдерам выше
* Напиши на [hi@cursor.com](mailto:hi@cursor.com), если проблема не исчезает

---

← Previous: [Быстрый старт](./section.md) | [Index](./index.md) | Next: [Доступ к обновлениям](./section.md) →