---
title: "Code Review"
source: "https://docs.cursor.com/id/cli/cookbook/code-review"
language: "id"
language_name: "Indonesian"
---

# Code Review
Source: https://docs.cursor.com/id/cli/cookbook/code-review

Bangun workflow GitHub Actions yang menggunakan Cursor CLI untuk secara otomatis meninjau pull request dan memberikan masukan

Tutorial ini nunjukin cara nyetel code review pakai Cursor CLI di GitHub Actions. Workflow-nya bakal menganalisis pull request, nemuin masalah, dan ngepost masukan sebagai komentar.

<Tip>
  Buat kebanyakan pengguna, kami nyaranin pakai [Bugbot](/id/bugbot) aja. Bugbot ngasih automated code review terkelola tanpa perlu setup. Pendekatan CLI ini berguna buat ngejelajahi kapabilitas dan kustomisasi tingkat lanjut.
</Tip>

<div className="space-y-4">
  <Expandable title="file workflow lengkap">
    ```yaml cursor-code-review.yml theme={null}
    name: Code Review

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # Lewati tinjauan kode otomatis untuk PR draft
        if: github.event.pull_request.draft == false
        steps:
          - name: Checkout repositori
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Pasang Cursor CLI
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: Konfigurasikan identitas git
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: Lakukan tinjauan kode otomatis
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'Kamu berjalan di runner GitHub Actions untuk melakukan tinjauan kode otomatis. gh CLI tersedia dan telah diautentikasi lewat GH_TOKEN. Kamu boleh berkomentar di pull request.

              Konteks:
              - Repo: ${{ github.repository }}
              - PR Number: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Tinjauan yang Memblokir: ${{ env.BLOCKING_REVIEW }}

              Tujuan:
              1) Cek ulang komentar tinjauan yang sudah ada dan balas resolved saat sudah ditangani.
              2) Tinjau diff PR saat ini dan tandai hanya isu yang jelas dengan tingkat keparahan tinggi.
              3) Tinggalkan komentar inline yang sangat singkat (1–2 kalimat) hanya pada baris yang diubah, plus ringkasan singkat di akhir.

              Prosedur:
              - Ambil komentar yang ada: gh pr view --json comments
              - Ambil diff: gh pr diff
              - Ambil file yang berubah beserta patch untuk menghitung posisi inline: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - Hitung anchor inline yang tepat untuk tiap isu (path file + posisi diff). Komentar HARUS ditempatkan inline pada baris yang diubah di diff, bukan sebagai komentar tingkat atas.
              - Deteksi komentar tingkat atas sebelumnya bergaya "tidak ada isu" yang dibuat oleh bot ini (cocokkan isi seperti: "✅ no issues", "No issues found", "LGTM").
              - Jika run SAAT INI menemukan isu dan ada komentar "tidak ada isu" sebelumnya:
                - Lebih baik hapus untuk menghindari kebingungan:
                  - Coba hapus komentar tingkat atas itu via: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - Jika penghapusan tidak memungkinkan, minimalkan via GraphQL (minimizeComment) atau edit dengan menambahkan awalan "[Digantikan oleh temuan baru]".
                - Jika tidak bisa dihapus atau diminimalkan, balas komentar itu: "⚠️ Digantikan: isu ditemukan pada commit yang lebih baru".
              - Jika isu yang dilaporkan sebelumnya tampak sudah diperbaiki oleh perubahan terbaru di sekitarnya, balas: ✅ Isu ini tampaknya telah terselesaikan oleh perubahan terbaru
              - Analisis HANYA untuk:
                - Dereferensi null/undefined
                - Kebocoran sumber daya (file atau koneksi tidak ditutup)
                - Injeksi (SQL/XSS)
                - Concurrency/race condition
                - Kurangnya penanganan error untuk operasi kritis
                - Kesalahan logika yang jelas dengan perilaku tidak benar
                - Pola antiperkinerja yang jelas dengan dampak terukur
                - Kerentanan keamanan yang pasti
              - Hindari duplikasi: lewati jika umpan balik serupa sudah ada pada atau dekat baris yang sama.

              Aturan komentar:
              - Maks 10 komentar inline total; prioritaskan isu yang paling kritis
              - Satu isu per komentar; tempatkan tepat pada baris yang diubah
              - Semua komentar isu HARUS inline (ditautkan ke file dan baris/posisi di diff PR)
              - Nada natural, spesifik, dan actionable; jangan sebut otomatis atau tingkat kepercayaan tinggi
              - Gunakan emoji: 🚨 Kritis 🔒 Keamanan ⚡ Performa ⚠️ Logika ✅ Terselesaikan ✨ Peningkatan

              Pengiriman:
              - Jika TIDAK ada isu untuk dilaporkan dan komentar tingkat atas yang menyatakan "tidak ada isu" sudah ada (misalnya, "✅ no issues", "No issues found", "LGTM"), JANGAN kirim komentar baru. Lewati pengiriman untuk menghindari redundansi.
              - Jika TIDAK ada isu untuk dilaporkan dan TIDAK ada komentar "tidak ada isu" sebelumnya, kirim satu komentar ringkas yang menyatakan tidak ada isu.
              - Jika ADA isu untuk dilaporkan dan ada komentar "tidak ada isu" sebelumnya, pastikan komentar sebelumnya dihapus/diminimalkan/diberi tanda sudah digantikan sebelum mengirim tinjauan baru.
              - Jika ADA isu untuk dilaporkan, kirim SATU tinjauan yang HANYA berisi komentar inline plus ringkasan singkat opsional. Gunakan GitHub Reviews API untuk memastikan komentar bersifat inline:
                - Bangun array JSON komentar seperti: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Kirim lewat: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - JANGAN gunakan: gh pr review --approve atau --request-changes

              Perilaku pemblokiran:
              - Jika BLOCKING_REVIEW bernilai true dan ada isu 🚨 atau 🔒 yang diposting: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - Jika tidak: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - Selalu set CRITICAL_ISSUES_FOUND di akhir
              '

          - name: Check blocking review results
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "Memeriksa isu kritis..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ Isu kritis ditemukan dan peninjauan pemblokiran diaktifkan. Menggagalkan workflow."
                exit 1
              else
                echo "✅ Tidak ada isu yang memblokir."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="Tinjauan kode otomatis yang menampilkan komentar inline di pull request" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

<div id="configure-authentication">
  ## Konfigurasi autentikasi
</div>

[Siapkan API key dan secret repositori](/id/cli/github-actions#authentication) untuk mengautentikasi Cursor CLI di GitHub Actions.

<div id="set-up-agent-permissions">
  ## Menyiapkan izin agen
</div>

Bikin file konfigurasi buat ngontrol tindakan yang bisa dilakukan agen. Ini mencegah operasi yang nggak diinginkan seperti nge-push kode atau bikin pull request.

Bikin `.cursor/cli.json` di root repositori lo:

```json  theme={null}
{
  "izin": {
    "tolak": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Tulis(**)"
    ]
  }
}
```

Konfigurasi ini bikin agent bisa baca file dan pakai GitHub CLI buat komentar, tapi ngeblok dia buat ngubah apa pun di repositori lo. Lihat [permissions reference](/id/cli/reference/permissions) buat opsi konfigurasi lainnya.

<div id="build-the-github-actions-workflow">
  ## Bangun workflow GitHub Actions
</div>

Sekarang kita bangun workflow-nya langkah demi langkah.

<div id="set-up-the-workflow-trigger">
  ### Setel trigger workflow
</div>

Bikin `.github/workflows/cursor-code-review.yml` dan konfigurasikan supaya jalan saat ada pull request:

```yaml  theme={null}
name: Tinjauan Kode Cursor

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

<div id="checkout-the-repository">
  ### Checkout repositori
</div>

Tambahkan langkah checkout untuk mengakses kode pada pull request:

```yaml  theme={null}
- name: Checkout repository
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

<div id="install-cursor-cli">
  ### Instal CLI Cursor
</div>

Tambahkan langkah instalasi CLI:

```yaml  theme={null}
- name: Instal Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

<div id="configure-the-review-agent">
  ### Konfigurasi review agent
</div>

Sebelum nerapin langkah full review, yuk pahami anatomi review prompt kita. Bagian ini ngejelasin gimana kita pengin agent berperilaku:

**Objective**:
Kita pengin agent nge-review PR diff saat ini dan cuma nandain isu yang jelas dengan tingkat keparahan tinggi, lalu ninggalin komentar inline yang sangat singkat (1–2 kalimat) hanya di baris yang berubah, dengan ringkasan singkat di akhir. Ini bantu jaga rasio signal-to-noise tetap seimbang.

**Format**:
Kita pengin komentar yang pendek dan to the point. Kita pakai emoji biar nge-scan komentar lebih gampang, dan kita mau ringkasan high-level dari full review di bagian akhir.

**Submission**:
Saat review selesai, kita pengin agent nyertakan komentar pendek berdasarkan temuan selama review. Agent harus submit satu review yang berisi komentar inline plus ringkasan yang ringkas.

**Edge cases**:
Kita perlu nangani:

* Komentar yang sudah ada dan udah diselesaikan: agent harus nandain sebagai selesai ketika sudah di-address
* Hindari duplikasi: agent harus skip komentar kalau feedback serupa sudah ada di atau dekat baris yang sama

**Final prompt**:
Prompt lengkap ini nggabungin semua requirement perilaku buat bikin feedback yang fokus dan bisa ditindaklanjuti

Sekarang yuk implement langkah review agent:

```yaml  theme={null}
- name: Lakukan code review
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "Kamu berjalan di GitHub Actions runner yang melakukan code review otomatis. gh CLI tersedia dan sudah diautentikasi via GH_TOKEN. Kamu boleh berkomentar di pull request.
    
    Context:
    - Repo: ${{ github.repository }}
    - PR Number: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Objectives:
    1) Cek ulang komentar review yang sudah ada dan balas resolved kalau sudah ditangani
    2) Review diff PR saat ini dan tandai hanya isu yang jelas dengan tingkat keparahan tinggi
    3) Tinggalkan komentar inline yang sangat singkat (1–2 kalimat) hanya pada baris yang berubah, plus ringkasan singkat di akhir
    
    Procedure:
    - Dapatkan komentar yang ada: gh pr view --json comments
    - Dapatkan diff: gh pr diff
    - Jika isu yang dilaporkan sebelumnya tampak sudah diperbaiki oleh perubahan di sekitarnya, balas: ✅ Isu ini tampaknya sudah terselesaikan oleh perubahan terbaru
    - Hindari duplikasi: lewati jika umpan balik serupa sudah ada pada atau dekat baris yang sama
    
    Commenting rules:
    - Maksimal 10 komentar inline total; prioritaskan isu yang paling kritis
    - Satu isu per komentar; tempatkan tepat pada baris yang berubah
    - Nada santai, spesifik, dan dapat ditindaklanjuti; jangan sebutkan otomatis atau tingkat keyakinan tinggi
    - Gunakan emoji: 🚨 Kritis 🔒 Keamanan ⚡ Performa ⚠️ Logika ✅ Terselesaikan ✨ Peningkatan
    
    Submission:
    - Kirim satu review yang berisi komentar inline plus ringkasan singkat
    - Hanya gunakan: gh pr review --comment
    - Jangan gunakan: gh pr review --approve atau --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

<div id="test-your-reviewer">
  ## Tes reviewer lo
</div>

Bikin pull request percobaan buat ngecek workflow-nya jalan dan agen ngepost komentar review dengan feedback emoji.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull request yang menampilkan komentar review otomatis dengan emoji dan feedback inline pada baris tertentu" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

<div id="next-steps">
  ## Langkah berikutnya
</div>

Sekarang kamu sudah punya sistem code review otomatis yang berfungsi. Pertimbangkan peningkatan berikut:

* Siapkan workflow tambahan untuk [memperbaiki kegagalan CI](/id/cli/cookbook/fix-ci)
* Konfigurasikan level review yang berbeda untuk branch yang berbeda
* Integrasikan dengan proses code review tim kamu yang sudah ada
* Kustomisasi perilaku agent untuk tipe file atau direktori yang berbeda

<Expandable title="Advanced: Blocking reviews">
  Kamu bisa mengonfigurasi workflow agar gagal kalau ditemukan isu kritis, sehingga pull request nggak bisa di-merge sampai ditangani.

  **Tambahkan perilaku blocking ke prompt**

  Pertama, update langkah review agent kamu untuk menyertakan variabel lingkungan `BLOCKING_REVIEW` dan tambahkan perilaku blocking ini ke prompt:

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **Tambahkan langkah pemeriksaan blocking**

  Lalu tambahkan langkah baru ini setelah langkah code review kamu:

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>

---

← Previous: [Bugbot](./bugbot.md) | [Index](./index.md) | Next: [Perbaiki Kegagalan CI](./perbaiki-kegagalan-ci.md) →