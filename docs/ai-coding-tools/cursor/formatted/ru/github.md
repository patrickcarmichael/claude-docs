---
title: "GitHub"
source: "https://docs.cursor.com/ru/integrations/github"
language: "ru"
language_name: "Russian"
---

# GitHub
Source: https://docs.cursor.com/ru/integrations/github

Официальное приложение Cursor GitHub для фоновых агентов

[Background Agents](/ru/background-agent) и [Bugbot](/ru/bugbot) требуют приложения Cursor GitHub для клонирования репозиториев и отправки изменений.

<div id="installation">
  ## Установка
</div>

1. Перейди в [Integrations в Dashboard](https://cursor.com/dashboard?tab=integrations)
2. Нажми **Connect** рядом с GitHub
3. Выбери: **All repositories** или **Selected repositories**

Чтобы отключить свой аккаунт GitHub, вернись в раздел интеграций в Dashboard и нажми **Disconnect Account**.

<div id="using-agent-in-github">
  ## Использование агента в GitHub
</div>

Интеграция с GitHub позволяет запускать фоновые сценарии агента прямо из pull request'ов и issues. Ты можешь запустить агента, чтобы он прочитал контекст, внес исправления и запушил коммиты, оставив комментарий `@cursor [prompt]` в любом PR или issue.

Если у тебя включён [Bugbot](/ru/bugbot), оставь комментарий `@cursor fix`, чтобы взять предложенное исправление от Bugbot и запустить фонового агента для решения проблемы.

<div id="permissions">
  ## Разрешения
</div>

Приложению GitHub нужны определённые разрешения для работы с фоновыми агентами:

<div className="full-width-table">
  | Разрешение                | Назначение                                                       |
  | ------------------------- | ---------------------------------------------------------------- |
  | **Доступ к репозиторию**  | Клонировать твой код и создавать рабочие ветки                   |
  | **Pull requests**         | Создавать PR с изменениями агента для твоего ревью               |
  | **Issues**                | Отслеживать баги и задачи, которые агенты находят или исправляют |
  | **Checks and statuses**   | Сообщать о качестве кода и результатах тестов                    |
  | **Actions and workflows** | Отслеживать CI/CD‑пайплайны и статус деплоя                      |
</div>

Все разрешения соответствуют принципу наименьших привилегий, необходимых для работы фоновых агентов.

<div id="ip-allow-list-configuration">
  ## Настройка списка разрешённых IP
</div>

Если твоя организация использует функцию GitHub по списку разрешённых IP для ограничения доступа к репозиториям, сначала свяжись с поддержкой, чтобы включить функциональность allowlist IP для вашей команды.

<div id="contact-support">
  ### Связаться с поддержкой
</div>

Перед настройкой allowlist IP свяжись с [hi@cursor.com](mailto:hi@cursor.com), чтобы включить эту функцию для вашей команды. Это требуется для обоих методов ниже.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### Включить список разрешённых IP для установленных GitHub Apps (рекомендуется)
</div>

У приложения Cursor для GitHub список IP уже преднастроен. Ты можешь включить allowlist для установленных приложений, чтобы автоматически унаследовать этот список. Это рекомендованный подход, потому что он позволяет нам обновлять список, а твоя организация будет получать обновления автоматически.

Чтобы включить это:

1. Перейди в раздел Security настроек организации
2. Открой настройки IP allow list
3. Отметь **"Allow access by GitHub Apps"**

Подробные инструкции смотри в [документации GitHub](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

<div id="add-ips-directly-to-your-allowlist">
  ### Добавить IP-адреса напрямую в свой allowlist
</div>

Если твоя организация использует определяемые IdP allowlist в GitHub или по другим причинам не может использовать преднастроенный allowlist, ты можешь вручную добавить IP-адреса:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  Список IP-адресов может изредка меняться. Команды, использующие списки разрешённых IP, получат заблаговременное уведомление перед добавлением или удалением IP-адресов.
</Note>

<div id="troubleshooting">
  ## Устранение неполадок
</div>

<AccordionGroup>
  <Accordion title="Агент не может получить доступ к репозиторию">
    * Установи GitHub‑приложение с доступом к репозиторию
    * Проверь права доступа к приватным репозиториям
    * Проверь свои права в аккаунте GitHub
  </Accordion>

  <Accordion title="Нет прав на создание pull request'ов">
    * Дай приложению права на запись в pull requests
    * Проверь правила защиты веток
    * Переустанови приложение, если срок установки истёк
  </Accordion>

  <Accordion title="Приложение не отображается в настройках GitHub">
    * Проверь, не установлено ли оно на уровне организации
    * Переустанови с [github.com/apps/cursor](https://github.com/apps/cursor)
    * Обратись в поддержку, если установка повреждена
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →