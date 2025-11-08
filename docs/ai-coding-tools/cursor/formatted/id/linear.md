---
title: "Linear"
source: "https://docs.cursor.com/id/integrations/linear"
language: "id"
language_name: "Indonesian"
---

# Linear
Source: https://docs.cursor.com/id/integrations/linear

Gunakan Background Agents dari Linear

Pakai [Background Agents](/id/background-agent) langsung dari Linear dengan mendelegasikan isu ke Cursor atau menyebut `@Cursor` di komentar.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## Mulai
</div>

<div id="installation">
  ### Instalasi
</div>

<Note>
  Kamu harus jadi admin Cursor untuk menyambungkan integrasi Linear. Pengaturan tim lainnya tersedia untuk anggota non-admin.
</Note>

1. Buka [integrasi Cursor](https://www.cursor.com/en/dashboard?tab=integrations)
2. Klik *Connect* di samping Linear
3. Sambungkan workspace Linear kamu dan pilih tim
4. Klik *Authorize*
5. Selesaikan sisa pengaturan Background Agent di Cursor:
   * Sambungkan GitHub dan pilih repositori default
   * Aktifkan penagihan berbasis penggunaan
   * Konfirmasi pengaturan privasi

<div id="account-linking">
  ### Penautan akun
</div>

Pertama kali dipakai, kamu akan diminta menautkan akun Cursor dan Linear. Koneksi GitHub diperlukan untuk membuat PR.

<div id="how-to-use">
  ## Cara menggunakan
</div>

Delegasikan issue ke Cursor atau mention `@Cursor` di komentar. Cursor bakal menganalisis issue dan otomatis nyaring pekerjaan non-development.

<div id="delegating-issues">
  ### Mendelegasikan issue
</div>

1. Buka issue di Linear
2. Klik field assignee
3. Pilih "Cursor"

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Mendelegasikan issue ke Cursor di Linear" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Mention Cursor
</div>

Mention `@Cursor` di komentar buat nge-assign agen baru atau kasih instruksi tambahan, misalnya: `@Cursor tolong perbaiki bug autentikasi yang dijelaskan di atas`.

<div id="workflow">
  ## Alur kerja
</div>

Background Agent menampilkan status real-time di Linear dan otomatis bikin PR saat selesai. Lacak progres di [dashboard Cursor](https://www.cursor.com/dashboard?tab=background-agents).

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Pembaruan status Background Agent di Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### Instruksi tindak lanjut
</div>

Lo bisa balas di sesi agent dan pesannya bakal dikirim sebagai tindak lanjut ke agent. Cukup mention `@Cursor` di komentar Linear buat ngasih panduan tambahan ke Background Agent yang lagi jalan.

<div id="configuration">
  ## Konfigurasi
</div>

Atur pengaturan Background Agent dari [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div className="full-width-table">
  | Setting                | Location         | Description                                                          |
  | :--------------------- | :--------------- | :------------------------------------------------------------------- |
  | **Default Repository** | Cursor Dashboard | Repository utama saat nggak ada repository proyek yang dikonfigurasi |
  | **Default Model**      | Cursor Dashboard | Model AI untuk Background Agents                                     |
  | **Base Branch**        | Cursor Dashboard | Branch asal untuk membuat PR (umumnya `main` atau `develop`)         |
</div>

<div id="configuration-options">
  ### Opsi konfigurasi
</div>

Kamu bisa ngatur perilaku Background Agent lewat beberapa cara:

**Deskripsi issue atau komentar**: Pakai sintaks `[key=value]`, misalnya:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Label issue**: Pakai struktur label induk–anak, di mana label induk adalah key konfigurasi dan label anak adalah valuenya.

**Label proyek**: Struktur induk–anak yang sama seperti label issue, diterapkan di level proyek.

Key konfigurasi yang didukung:

* `repo`: Tentukan repository target (misalnya, `owner/repository`)
* `branch`: Tentukan base branch untuk pembuatan PR
* `model`: Tentukan model AI yang dipakai

<div id="repository-selection">
  ### Pemilihan repository
</div>

Cursor nentuin repository yang akan dikerjain pakai urutan prioritas ini:

1. **Deskripsi/komentar issue**: Sintaks `[repo=owner/repository]` di teks issue atau komentar
2. **Label issue**: Label repository yang ditempel ke issue Linear tersebut
3. **Label proyek**: Label repository yang ditempel ke proyek Linear
4. **Default repository**: Repository yang disetel di pengaturan Cursor Dashboard

<div id="setting-up-repository-labels">
  #### Menyiapkan label repository
</div>

Buat label repository di Linear dengan langkah berikut:

1. Buka **Settings** di workspace Linear kamu
2. Klik **Labels**
3. Klik **New group**
4. Kasih nama grup "repo" (nggak case-sensitive — harus persis "repo", bukan "Repository" atau variasi lain)
5. Di dalam grup itu, buat label untuk tiap repository pakai format `owner/repo`

Label ini bisa kamu pasang ke issue atau proyek buat nunjukin repository tempat Background Agent bakal kerja.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Mengonfigurasi label repository di Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →