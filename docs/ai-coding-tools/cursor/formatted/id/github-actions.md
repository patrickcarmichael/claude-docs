---
title: "GitHub Actions"
source: "https://docs.cursor.com/id/cli/github-actions"
language: "id"
language_name: "Indonesian"
---

# GitHub Actions
Source: https://docs.cursor.com/id/cli/github-actions

Pelajari cara menggunakan Cursor CLI di GitHub Actions dan sistem integrasi berkelanjutan lainnya

Gunakan Cursor CLI di GitHub Actions dan sistem CI/CD lainnya untuk mengotomatiskan tugas pengembangan.

<div id="github-actions-integration">
  ## Integrasi GitHub Actions
</div>

Konfigurasi dasar:

```yaml  theme={null}
- name: Instal Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Jalankan Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Prompt kamu di sini" --model gpt-5
```

<div id="cookbook-examples">
  ## Contoh cookbook
</div>

Lihat contoh cookbook kami untuk alur kerja praktis: [memperbarui dokumentasi](/id/cli/cookbook/update-docs) dan [memperbaiki isu CI](/id/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Sistem CI lainnya
</div>

Pakai Cursor CLI di sistem CI/CD apa pun dengan:

* **Eksekusi skrip shell** (bash, zsh, dll.)
* **Variabel lingkungan** untuk konfigurasi API key
* **Koneksi internet** untuk mengakses API Cursor

<div id="autonomy-levels">
  ## Tingkat otonomi
</div>

Pilih tingkat otonomi agent lo:

<div id="full-autonomy-approach">
  ### Pendekatan otonomi penuh
</div>

Kasih agent kontrol penuh atas operasi git, panggilan API, dan interaksi eksternal. Setup lebih simpel, tapi butuh kepercayaan lebih.

**Contoh:** Di cookbook [Update Documentation](/id/cli/cookbook/update-docs) kita, workflow pertama bikin agent bisa:

* Menganalisis perubahan PR
* Bikin dan ngelola branch git
* Commit dan push perubahan
* Ngepost komentar di pull request
* Nanganin semua skenario error

```yaml  theme={null}
- name: Perbarui dokumentasi (otonomi penuh)
  run: |
    cursor-agent -p "Kamu punya akses penuh ke git, GitHub CLI, dan operasi PR. 
    Tangani seluruh alur pembaruan dokumentasi, termasuk commit, push, dan komentar PR."
```

<div id="restricted-autonomy-approach">
  ### Pendekatan otonomi terbatas
</div>

<Note>
  Kami merekomendasikan pakai pendekatan ini dengan **pembatasan berbasis izin** untuk alur kerja CI produksi. Ini ngasih kamu yang terbaik dari dua sisi: agen bisa dengan cerdas menangani analisis kompleks dan modifikasi file, sementara operasi kritis tetap deterministik dan bisa diaudit.
</Note>

Batasi operasi agen, sementara langkah-langkah kritis ditangani di langkah alur kerja terpisah. Kontrol dan prediktabilitas jadi lebih baik.

**Contoh:** Alur kerja kedua di cookbook yang sama membatasi agen hanya untuk modifikasi file:

```yaml  theme={null}
- name: Hasilkan pembaruan docs (terbatas)
  run: |
    cursor-agent -p "PENTING: Jangan membuat branch, commit, push, atau mengirim komentar PR. 
    Hanya ubah file di direktori kerja. Langkah workflow selanjutnya yang akan menangani publikasi."

- name: Publikasikan branch docs (deterministik)
  run: |
    # Operasi git deterministik ditangani oleh CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: update untuk PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Kirim komentar PR (deterministik)  
  run: |
    # Komentar PR deterministik ditangani oleh CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs diperbarui"
```

<div id="permission-based-restrictions">
  ### Pembatasan berbasis izin
</div>

Gunakan [konfigurasi izin](/id/cli/reference/permissions) untuk menegakkan pembatasan pada tingkat CLI:

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
  ## Autentikasi
</div>

<div id="generate-your-api-key">
  ### Generate API key
</div>

Pertama, [generate API key](/id/cli/reference/authentication#api-key-authentication) dari dashboard Cursor.

<div id="configure-repository-secrets">
  ### Konfigurasikan repository secrets
</div>

Simpan API key Cursor dengan aman di repository:

1. Buka repository GitHub lo
2. Klik **Settings** → **Secrets and variables** → **Actions**
3. Klik **New repository secret**
4. Kasih nama `CURSOR_API_KEY`
5. Tempel API key lo sebagai value
6. Klik **Add secret**

<div id="use-in-workflows">
  ### Gunakan di workflows
</div>

Set environment variable `CURSOR_API_KEY`:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [Update Docs](./update-docs.md) | [Index](./index.md) | Next: [Menggunakan Headless CLI](./menggunakan-headless-cli.md) →