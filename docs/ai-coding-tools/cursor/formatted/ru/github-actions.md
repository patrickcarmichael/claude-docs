---
title: "GitHub Actions"
source: "https://docs.cursor.com/ru/cli/github-actions"
language: "ru"
language_name: "Russian"
---

# GitHub Actions
Source: https://docs.cursor.com/ru/cli/github-actions

Узнай, как использовать Cursor CLI в GitHub Actions и других системах непрерывной интеграции

Используй Cursor CLI в GitHub Actions и других системах CI/CD, чтобы автоматизировать задачи разработки.

<div id="github-actions-integration">
  ## Интеграция с GitHub Actions
</div>

Базовая конфигурация:

```yaml  theme={null}
- name: Установка Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Запуск Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Твой промпт здесь" --model gpt-5
```

<div id="cookbook-examples">
  ## Примеры из «книги рецептов»
</div>

Смотри наши примеры с практическими сценариями: [обновление документации](/ru/cli/cookbook/update-docs) и [исправление проблем в CI](/ru/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Другие CI‑системы
</div>

Используй Cursor CLI в любой CI/CD‑системе с:

* **возможностью запускать shell‑скрипты** (bash, zsh и т. д.)
* **переменными окружения** для настройки ключа API
* **доступом в интернет** для обращения к API Cursor

<div id="autonomy-levels">
  ## Уровни автономности
</div>

Выбери уровень автономности агента:

<div id="full-autonomy-approach">
  ### Полная автономность
</div>

Дай агенту полный контроль над операциями с git, API-вызовами и внешними интеграциями. Настройка проще, но требует больше доверия.

**Пример:** В нашем рецепте [Update Documentation](/ru/cli/cookbook/update-docs) первый сценарий позволяет агенту:

* Анализировать изменения в PR
* Создавать и управлять ветками git
* Коммитить и пушить изменения
* Оставлять комментарии в pull request'ах
* Обрабатывать все ошибки

```yaml  theme={null}
- name: Обновить документацию (полная автономность)
  run: |
    cursor-agent -p "У тебя есть полный доступ к git, GitHub CLI и операциям с PR. 
    Веди весь процесс обновления документации, включая коммиты, пуши и комментарии к PR."
```

<div id="restricted-autonomy-approach">
  ### Подход с ограниченной автономией
</div>

<Note>
  Рекомендуем использовать этот подход с **ограничениями на основе разрешений** для продакшен‑CI‑воркфлоу. Это сочетает лучшее из обоих миров: агент может умно выполнять сложный анализ и вносить изменения в файлы, а критически важные операции остаются детерминированными и поддающимися аудиту.
</Note>

Ограничивай операции агента, а критические этапы выноси в отдельные шаги воркфлоу. Больше контроля и предсказуемости.

**Пример:** Второй воркфлоу в этом же сборнике рецептов ограничивает агента только изменениями файлов:

```yaml  theme={null}
- name: Генерация обновлений документации (с ограничениями)
  run: |
    cursor-agent -p "ВАЖНО: не создавай ветки, не выполняй commit, push и не оставляй комментарии в PR. 
    Меняй только файлы в рабочем каталоге. Публикацией займётся следующий шаг workflow."

- name: Публикация ветки документации (детерминированно)
  run: |
    # Детерминированные операции git выполняются CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: обновление для PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Публикация комментария в PR (детерминированно)  
  run: |
    # Детерминированное комментирование PR выполняется CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Документация обновлена"
```

<div id="permission-based-restrictions">
  ### Ограничения на базе разрешений
</div>

Используй [конфигурации разрешений](/ru/cli/reference/permissions), чтобы применять ограничения на уровне CLI:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## Аутентификация
</div>

<div id="generate-your-api-key">
  ### Сгенерируй свой API‑ключ
</div>

Сначала [сгенерируй API‑ключ](/ru/cli/reference/authentication#api-key-authentication) в своей панели управления Cursor.

<div id="configure-repository-secrets">
  ### Настрой секреты репозитория
</div>

Надёжно сохрани свой API‑ключ Cursor в репозитории:

1. Перейди в свой репозиторий на GitHub
2. Нажми **Settings** → **Secrets and variables** → **Actions**
3. Нажми **New repository secret**
4. Назови его `CURSOR_API_KEY`
5. Вставь свой API‑ключ в поле значения
6. Нажми **Add secret**

<div id="use-in-workflows">
  ### Использование в workflow
</div>

Установи переменную окружения `CURSOR_API_KEY`:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [Update Docs](./update-docs.md) | [Index](./index.md) | Next: [Использование Headless CLI](./headless-cli.md) →