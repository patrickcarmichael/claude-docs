---
title: "Dokümanları Güncelle"
source: "https://docs.cursor.com/tr/cli/cookbook/update-docs"
language: "tr"
language_name: "Turkish"
---

# Dokümanları Güncelle
Source: https://docs.cursor.com/tr/cli/cookbook/update-docs

GitHub Actions’ta Cursor CLI kullanarak bir depo için dokümanları güncelle

GitHub Actions’ta Cursor CLI kullanarak dokümantasyonu güncelle. İki yaklaşım var: tam ajan özerkliği ya da yalnızca ajanın dosya değişiklikleri yaptığı deterministik bir iş akışı.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Belgeleri Güncelle

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
        - name: Depoyu Checkout et
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Cursor CLI'yi Yükle
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Git'i Yapılandır
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Belgeleri Güncelle
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "GitHub Actions runner'ında çalışıyorsun.

            GitHub CLI `gh` olarak mevcut ve `GH_TOKEN` ile kimliği doğrulanmış. Git mevcut. Depo içeriğine yazma erişimin var ve PR'lere yorum yapabilirsin, ama PR oluşturamaz veya düzenleyemezsin.

            # Bağlam:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Amaç:
            - Orijinal PR'deki artımlı değişikliklerle yönlendirilen uçtan uca bir dokümantasyon güncelleme akışını uygula.

            # Gereksinimler:
            1) Orijinal PR'de nelerin değiştiğini belirle ve birden fazla push olduysa, son başarılı dokümantasyon güncellemesinden bu yana artımlı diff'leri hesapla.
            2) Yalnızca bu artımlı değişikliklere göre ilgili dokümanları güncelle.
            3) Bu PR head'i için Bağlamdaki Docs Branch Prefix'i kullanarak kalıcı dokümantasyon dalını koru. Eksikse oluştur, aksi halde güncelle ve değişiklikleri origin'e push et.
            4) PR oluşturma iznin YOK. Bunun yerine, dokümantasyon güncellemelerini kısaca açıklayan ve hızlı PR oluşturmak için satır içi bir karşılaştırma bağlantısı içeren tek bir doğal dil PR yorumu (1–2 cümle) gönder veya güncelle.

            # Girdiler ve kurallar:
            - Değişiklikleri tespit etmek ve son dokümantasyon güncellemesinden bu yana artımlı aralıkları çıkarmak için `gh pr diff` ve git geçmişini kullan.
            - PR'leri doğrudan oluşturmayı veya düzenlemeyi deneme. Yukarıdaki karşılaştırma bağlantısı biçimini kullan.
            - Değişiklikleri minimumda tut ve depo stiline uygun davran. Doküman güncellemesi gerekmiyorsa, değişiklik yapma ve yorum gönderme.

            # Güncellemeler gerçekleştiğinde teslimatlar:
            - Bu PR head'i için kalıcı dokümantasyon dalına push'lanmış commit'ler.
            - Orijinal PR üzerinde, yukarıdaki satır içi karşılaştırma bağlantısını içeren tek bir doğal dil PR yorumu. Yinelenen yorumlardan kaçın; varsa önceki bot yorumunu güncelle.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Belgeleri Güncelle

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
        - name: Depoyu getir
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Cursor CLI'yi yükle
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Git’i yapılandır
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Belge güncellemelerini oluştur (commit/push/yorum yok)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "GitHub Actions runner’ında çalışıyorsun.

            GitHub CLI `gh` olarak mevcut ve `GH_TOKEN` ile kimliği doğrulanmış. Git mevcut.

            ÖNEMLİ: Dal oluşturma, commit, push yapma veya PR yorumu gönderme. Yalnızca gerektiğinde çalışma dizinindeki dosyaları değiştir. Yayınlama ve PR’a yorum yapma, ilerideki bir iş akışı adımının sorumluluğunda.

            # Bağlam:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Hedef:
            - Bu PR’nin getirdiği artımlı değişikliklere göre depo belgelerini güncelle.

            # Gereksinimler:
            1) Orijinal PR’de neyin değiştiğini belirle (gerektiğinde `gh pr diff` ve git geçmişini kullan). Mevcut kalıcı bir docs dalı `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` varsa, önceki güncellemeleri anlamak için salt okunur referans olarak kullanabilirsin.
            2) Yalnızca bu değişikliklere bağlı ilgili belgeleri güncelle. Düzenlemeleri minimumda tut ve depo tarzıyla tutarlı ol.
            3) Commit, push yapma, dal oluşturma veya PR yorumu gönderme. Çalışma ağacını yalnızca güncellenmiş dosyalarla bırak; sonraki adım yayınlayacak.

            # Girdiler ve kurallar:
            - Değişiklikleri tespit etmek ve belge düzenlemelerini buna göre odaklamak için `gh pr diff` ve git geçmişini kullan.
            - Eğer belge güncellemesi gerekmiyorsa, değişiklik yapma ve çıktı üretme.

            # Güncellemeler olduğunda çıktı:
            - Yalnızca çalışma dizininde değiştirilmiş belge dosyaları (commit/push/yorum yok).
            " --force --model "$MODEL" --output-format=text

        - name: Belgeler dalını yayınla
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Ensure we are on a local branch that we can push
            git fetch origin --prune

            # Create/switch to the persistent docs branch, keeping current working tree changes
            git checkout -B "$DOCS_BRANCH"

            # Stage and detect changes
            git add -A
            if git diff --staged --quiet; then
              echo "Yayınlanacak belge değişikliği yok. Commit/push atlanıyor."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: PR yorumunu gönder veya güncelle
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
              echo "Cursor belgeler dalını güncelledi: \`${DOCS_BRANCH}\`"
              echo "Artık [farkı görüntüleyebilir ve bu belge güncellemelerini birleştirmek için hızlıca bir PR oluşturabilirsin](${COMPARE_URL})."
              echo
              echo "_Bu yorum, PR değiştikçe sonraki çalıştırmalarda güncellenecek._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Son bot yorumunu düzenlemek başarısız olursa (daha eski gh), yeni bir yorum oluşturmaya geri dön
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Mevcut PR yorumu güncellendi."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Yeni PR yorumu gönderildi."
            fi
  ```
</CodeGroup>

---

← Previous: [Anahtarları Çevir](./anahtarlar-evir.md) | [Index](./index.md) | Next: [GitHub Actions](./github-actions.md) →