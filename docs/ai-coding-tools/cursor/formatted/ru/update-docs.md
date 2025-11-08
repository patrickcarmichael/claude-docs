---
title: "Update Docs"
source: "https://docs.cursor.com/ru/cli/cookbook/update-docs"
language: "ru"
language_name: "Russian"
---

# Update Docs
Source: https://docs.cursor.com/ru/cli/cookbook/update-docs

Обновляй документацию в репозитории с помощью Cursor CLI в GitHub Actions

Обновляй документацию в GitHub Actions с помощью Cursor CLI. Два подхода: полная автономность агента или детерминированный пайплайн, где агент изменяет только файлы.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Обновление документации

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Проверить репозиторий
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Установить Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Настроить git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Обновить документацию
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Ты работаешь в среде GitHub Actions runner.

            GitHub CLI доступен как `gh` и аутентифицирован через `GH_TOKEN`. Git доступен. У тебя есть права на запись в репозиторий и возможность комментировать pull request’ы, но ты не должен создавать или редактировать PR.

            # Контекст:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Цель:
            - Реализовать сквозной процесс обновления документации, управляемый инкрементальными изменениями в исходном PR.

            # Требования:
            1) Определи, что изменилось в исходном PR и, если было несколько пушей, вычисли инкрементальные diff’ы с момента последнего успешного обновления документации.
            2) Обновляй только релевантные разделы документации на основе этих инкрементальных изменений.
            3) Поддерживай постоянную ветку документации для текущего head PR, используя префикс ветки из Контекста. Создай её, если отсутствует; иначе обнови и отправь изменения в origin.
            4) У тебя НЕТ прав создавать PR. Вместо этого оставь или обнови один короткий комментарий к PR (1–2 предложения), который кратко объясняет обновления документации и включает встроенную ссылку сравнения для быстрого создания PR.

            # Входные данные и соглашения:
            - Используй `gh pr diff` и историю git, чтобы обнаружить изменения и получить инкрементальные диапазоны с момента последнего обновления документации.
            - Не пытайся создавать или редактировать PR напрямую. Используй формат ссылки сравнения выше.
            - Держи изменения минимальными и согласованными со стилем репозитория. Если обновления документации не нужны, не вноси изменений и не оставляй комментарий.

            # Результаты при обновлениях:
            - Отправленные коммиты в постоянную ветку документации для текущего head PR.
            - Один комментарий естественным языком в исходном PR, который включает упомянутую встроенную ссылку сравнения. Избегай дублей; обнови предыдущий комментарий бота, если он есть.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Обновление документации

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Проверить репозиторий
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Установить Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Настроить git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Сгенерировать обновления документации (без commit/push/comment)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Ты работаешь в среде GitHub Actions runner.

            GitHub CLI доступен как `gh` и аутентифицирован через `GH_TOKEN`. Git доступен.

            ВАЖНО: не создавай ветки, не выполняй commit, push и не оставляй комментарии в PR. Меняй только файлы в рабочем каталоге по необходимости. Следующий шаг workflow опубликует изменения и оставит комментарий в PR.

            # Контекст:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Цель:
            - Обновить документацию репозитория на основе инкрементальных изменений, внесённых этим PR.

            # Требования:
            1) Определи, что изменилось в исходном PR (используй `gh pr diff` и историю git при необходимости). Если существует постоянная ветка документации `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}`, можно использовать её как точку только для чтения, чтобы понять предыдущие обновления.
            2) Обновляй только релевантную документацию на основе этих изменений. Сохраняй правки минимальными и согласованными со стилем репозитория.
            3) Не выполняй commit, push, не создавай ветки и не оставляй комментарии в PR. Оставь рабочее дерево только с обновлёнными файлами; следующий шаг их опубликует.

            # Ввод и соглашения:
            - Используй `gh pr diff` и историю git, чтобы выявить изменения и сфокусировать правки в документации соответствующим образом.
            - Если обновления документации не требуются, не вноси изменений и не выводи ничего.

            # Результаты при наличии обновлений:
            - Изменённые файлы документации только в рабочем каталоге (без commit/push/comment).
            " --force --model "$MODEL" --output-format=text

        - name: Опубликовать ветку документации
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Убедись, что мы на локальной ветке, которую можно отправить
            git fetch origin --prune

            # Создать/переключиться на постоянную ветку документации, сохранив текущие изменения в рабочем дереве
            git checkout -B "$DOCS_BRANCH"

            # Проиндексировать и обнаружить изменения
            git add -A
            if git diff --staged --quiet; then
              echo "Нет изменений в документации для публикации. Пропускаем commit/push."
              exit 0
            fi

            COMMIT_MSG="docs: обновление для PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: Оставить или обновить комментарий в PR
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor обновил ветку документации: \`${DOCS_BRANCH}\`"
              echo "Теперь можно [посмотреть diff и быстро создать PR, чтобы смержить эти обновления документации](${COMPARE_URL})."
              echo
              echo "_Этот комментарий будет обновляться при последующих запусках по мере изменений в PR._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Если редактирование последнего комментария бота не удалось (старый gh), перейти к созданию нового комментария
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Обновлён существующий комментарий в PR."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Опубликован новый комментарий в PR."
  ```
</CodeGroup>

---

← Previous: [Перевод ключей](./section.md) | [Index](./index.md) | Next: [GitHub Actions](./github-actions.md) →