---
title: "Update Docs"
source: "https://docs.cursor.com/id/cli/cookbook/update-docs"
language: "id"
language_name: "Indonesian"
---

# Update Docs
Source: https://docs.cursor.com/id/cli/cookbook/update-docs

Perbarui dokumen untuk sebuah repositori menggunakan Cursor CLI di GitHub Actions

Perbarui dokumentasi menggunakan Cursor CLI di GitHub Actions. Ada dua pendekatan: otonomi agen penuh atau alur kerja deterministik dengan modifikasi file hanya oleh agen.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Perbarui Docs

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
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Konfigurasi git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Perbarui docs
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Kamu lagi berjalan di runner GitHub Actions.

            GitHub CLI tersedia sebagai `gh` dan sudah diautentikasi lewat `GH_TOKEN`. Git tersedia. Kamu punya akses tulis ke konten repository dan bisa komentar di pull request, tapi kamu nggak boleh bikin atau ngedit PR.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Terapkan alur pembaruan docs end-to-end yang dipicu oleh perubahan inkremental pada PR asli.

            # Requirements:
            1) Tentukan apa yang berubah di PR asli dan, kalau ada beberapa push, hitung diff inkremental sejak pembaruan docs sukses terakhir.
            2) Perbarui hanya docs yang relevan berdasarkan perubahan inkremental tersebut.
            3) Pertahankan branch docs yang persisten untuk head PR ini dengan Prefix Branch Docs dari Context. Buat kalau belum ada, perbarui kalau sudah ada, dan push perubahan ke origin.
            4) Kamu TIDAK punya izin buat bikin PR. Sebagai gantinya, kirim atau perbarui satu komentar PR berbahasa natural (1–2 kalimat) yang singkat menjelaskan pembaruan docs dan menyertakan tautan compare inline untuk cepat bikin PR

            # Inputs and conventions:
            - Gunakan `gh pr diff` dan riwayat git untuk mendeteksi perubahan dan menurunkan rentang inkremental sejak pembaruan docs terakhir.
            - Jangan coba bikin atau ngedit PR secara langsung. Gunakan format tautan compare di atas.
            - Jaga perubahan seminimal mungkin dan konsisten dengan gaya repo. Kalau nggak ada pembaruan docs yang diperlukan, jangan buat perubahan dan jangan kirim komentar.

            # Deliverables when updates occur:
            - Commit yang dipush ke branch docs persisten untuk head PR ini.
            - Satu komentar PR berbahasa natural di PR asli yang menyertakan tautan compare inline di atas. Hindari kirim duplikat; perbarui komentar bot sebelumnya kalau ada.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Perbarui Docs

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
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Instal Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Konfigurasi git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Hasilkan pembaruan docs (tanpa commit/push/komentar)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "Kamu sedang berjalan di runner GitHub Actions.

            GitHub CLI tersedia sebagai `gh` dan sudah diautentikasi via `GH_TOKEN`. Git tersedia.

            PENTING: Jangan membuat branch, commit, push, atau mem-posting komentar PR. Hanya ubah file di working directory seperlunya. Langkah workflow berikutnya yang akan mempublikasikan perubahan dan mengomentari PR.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Goal:
            - Perbarui dokumentasi repository berdasarkan perubahan inkremental yang diperkenalkan oleh PR ini.

            # Requirements:
            1) Tentukan apa yang berubah di PR asli (gunakan `gh pr diff` dan riwayat git jika perlu). Jika branch docs persisten `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` sudah ada, kamu boleh menggunakannya sebagai titik referensi read-only untuk memahami pembaruan sebelumnya.
            2) Perbarui hanya docs yang relevan berdasarkan perubahan tersebut. Jaga edit seminimal mungkin dan konsisten dengan gaya repo.
            3) Jangan commit, push, membuat branch, atau mem-posting komentar PR. Biarkan working tree hanya dengan file yang sudah diperbarui; langkah berikutnya yang akan mempublikasikan.

            # Inputs and conventions:
            - Gunakan `gh pr diff` dan riwayat git untuk mendeteksi perubahan dan memfokuskan penyuntingan docs sesuai.
            - Jika tidak ada pembaruan docs yang diperlukan, jangan lakukan perubahan dan jangan menghasilkan output.

            # Deliverables when updates occur:
            - File docs yang dimodifikasi hanya di working directory (tanpa commit/push/komentar).
            " --force --model "$MODEL" --output-format=text

        - name: Publikasikan branch docs
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Pastikan kita berada di branch lokal yang bisa kita push
            git fetch origin --prune

            # Buat/berpindah ke branch docs persisten, sambil mempertahankan perubahan working tree saat ini
            git checkout -B "$DOCS_BRANCH"

            # Stage dan deteksi perubahan
            git add -A
            if git diff --staged --quiet; then
              echo "Tidak ada perubahan docs untuk dipublikasikan. Melewati commit/push."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: Posting atau perbarui komentar PR
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
              echo "Cursor memperbarui branch docs: \`${DOCS_BRANCH}\`"
              echo "Sekarang kamu bisa [melihat diff dan cepat membuat PR untuk menggabungkan pembaruan docs ini](${COMPARE_URL})."
              echo
              echo "_Komentar ini akan diperbarui pada run berikutnya saat PR berubah._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # Jika mengedit komentar bot terakhir gagal (versi gh lebih lama), fallback ke membuat komentar baru
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Komentar PR yang ada telah diperbarui."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Komentar PR baru telah diposting."
            fi
  ```
</CodeGroup>

---

← Previous: [Translate Keys](./translate-keys.md) | [Index](./index.md) | Next: [GitHub Actions](./github-actions.md) →