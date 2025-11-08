---
title: "Использование Headless CLI"
source: "https://docs.cursor.com/ru/cli/headless"
language: "ru"
language_name: "Russian"
---

# Использование Headless CLI
Source: https://docs.cursor.com/ru/cli/headless

Узнай, как писать скрипты с помощью Cursor CLI для автоматизированного анализа, генерации и модификации кода

Используй Cursor CLI в скриптах и автоматизации для анализа, генерации и рефакторинга кода.

<div id="how-it-works">
  ## Как это работает
</div>

Используй [режим печати](/ru/cli/using#non-interactive-mode) (`-p, --print`) для неинтерактивных сценариев и автоматизации.

<div id="file-modification-in-scripts">
  ### Изменение файлов в скриптах
</div>

Комбинируй `--print` с `--force`, чтобы изменять файлы в скриптах:

```bash  theme={null}

---

← Previous: [GitHub Actions](./github-actions.md) | [Index](./index.md) | Next: [Установка](./section.md) →