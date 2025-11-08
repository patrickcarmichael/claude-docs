---
title: "Rules"
source: "https://docs.cursor.com/id/context/rules"
language: "id"
language_name: "Indonesian"
---

# Rules
Source: https://docs.cursor.com/id/context/rules

Kendalikan perilaku model Agent dengan instruksi yang reusable dan scoped.

Rules ngasih instruksi level sistem buat Agent dan Inline Edit. Anggap aja ini sebagai konteks, preferensi, atau workflow yang persistent buat proyek lo.

Cursor mendukung empat jenis rules:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Disimpan di `.cursor/rules`, di-version control dan di-scope ke codebase lo.
  </Card>

  <Card title="User Rules" icon="user">
    Global buat environment Cursor lo. Didefinisikan di settings dan selalu diterapkan.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Instruksi Agent dalam format markdown. Alternatif simpel buat `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Masih didukung, tapi deprecated. Mending pake Project Rules.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Cara kerja rules
</div>

Large language models nggak nyimpen memori antar completion. Rules ngasih konteks yang persisten dan bisa dipakai ulang di level prompt.

Saat diterapkan, isi rule bakal disertakan di awal konteks model. Ini kasih panduan yang konsisten buat AI untuk ngasilin kode, ngeinterpretasi edit, atau bantuin workflow.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Rule diterapkan dalam konteks dengan chat" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Rules berlaku untuk [Chat](/id/chat/overview) dan [Inline
  Edit](/id/inline-edit/overview). Rules yang aktif bakal muncul di sidebar Agent.
</Info>

<div id="project-rules">
  ## Aturan proyek
</div>

Aturan proyek ada di `.cursor/rules`. Setiap aturan adalah sebuah file dan dilacak dengan kontrol versi. Aturan bisa dibatasi dengan pola path, dipanggil secara manual, atau disertakan berdasarkan relevansi. Subdirektori bisa memiliki direktori `.cursor/rules` sendiri yang cakupannya hanya folder tersebut.

Gunakan aturan proyek untuk:

* Menyandikan pengetahuan domain-spesifik tentang codebase kamu
* Mengotomatiskan alur kerja atau templat khusus proyek
* Menyeragamkan keputusan gaya atau arsitektur

<div id="rule-anatomy">
  ### Anatomi rule
</div>

Setiap file rule ditulis dalam **MDC** (`.mdc`), format yang mendukung metadata dan konten. Atur bagaimana rule diterapkan lewat dropdown tipe yang mengubah properti `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Tipe Rule</span>         | Deskripsi                                                                                  |
| :--------------------------------------------- | :----------------------------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Selalu disertakan dalam konteks model                                                      |
| <span class="no-wrap">`Auto Attached`</span>   | Disertakan saat file yang cocok dengan pola glob direferensikan                            |
| <span class="no-wrap">`Agent Requested`</span> | Tersedia untuk AI, yang memutuskan apakah akan menyertakannya. Harus menyertakan deskripsi |
| <span class="no-wrap">`Manual`</span>          | Hanya disertakan saat disebutkan secara eksplisit menggunakan `@ruleName`                  |

```
---
description: Boilerplate layanan RPC
globs:
alwaysApply: false
---

- Gunakan pola RPC internal kami saat mendefinisikan layanan
- Selalu gunakan snake_case untuk nama layanan.

@service-template.ts
```

<div id="nested-rules">
  ### Aturan bertingkat
</div>

Susun aturan dengan menaruhnya di direktori `.cursor/rules` di seluruh proyek lo. Aturan bertingkat bakal otomatis nempel saat file di direktori itu direferensiin.

```
project/
  .cursor/rules/        # Aturan untuk seluruh proyek
  backend/
    server/
      .cursor/rules/    # Aturan khusus backend
  frontend/
    .cursor/rules/      # Aturan khusus frontend
```

<div id="creating-a-rule">
  ### Membuat rule
</div>

Bikin rule pakai perintah `New Cursor Rule` atau lewat `Cursor Settings > Rules`. Ini bakal bikin file rule baru di `.cursor/rules`. Dari Settings kamu bisa lihat semua rule beserta statusnya.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Perbandingan rule yang ringkas vs yang panjang" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="creating-a-rule">
  ### Membuat rule
</div>

Bikin rule langsung di percakapan pakai perintah `/Generate Cursor Rules`. Berguna kalau kamu udah nentuin perilaku agent dan pengin pakai ulang.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Browser kamu tidak mendukung tag video.
  </video>
</Frame>

<div id="best-practices">
  ## Praktik terbaik
</div>

Aturan yang bagus itu fokus, bisa dieksekusi, dan jelas ruang lingkupnya.

* Jaga aturan tetap di bawah 500 baris
* Pecah aturan besar jadi beberapa aturan yang bisa dikomposisikan
* Sertakan contoh konkret atau file rujukan
* Hindari panduan yang samar. Tulis aturan seperti dok internal yang jelas
* Pakai ulang aturan saat ngeulang prompt di chat

<div id="examples">
  ## Contoh
</div>

<AccordionGroup>
  <Accordion title="Standar untuk komponen frontend dan validasi API">
    Aturan ini menetapkan standar untuk komponen frontend:

    Saat bekerja di direktori components:

    * Selalu pakai Tailwind untuk styling
    * Pakai Framer Motion untuk animasi
    * Ikuti konvensi penamaan komponen

    Aturan ini juga menegakkan validasi untuk endpoint API:

    Di direktori API:

    * Pakai zod untuk semua validasi
    * Definisikan return type dengan skema zod
    * Ekspor tipe yang dihasilkan dari skema
  </Accordion>

  <Accordion title="Template untuk layanan Express dan komponen React">
    Aturan ini menyediakan template untuk layanan Express:

    Pakai template ini saat bikin layanan Express:

    * Ikuti prinsip RESTful
    * Sertakan middleware penanganan error
    * Siapkan logging yang proper

    @express-service-template.ts

    Aturan ini mendefinisikan struktur komponen React:

    Komponen React harus mengikuti layout berikut:

    * Interface Props di bagian atas
    * Komponen sebagai named export
    * Styles di bagian bawah

    @component-template.tsx
  </Accordion>

  <Accordion title="Mengotomatiskan alur kerja pengembangan dan pembuatan dokumentasi">
    Aturan ini mengotomatiskan analisis app:

    Saat diminta menganalisis app:

    1. Jalankan dev server dengan `npm run dev`
    2. Ambil log dari console
    3. Sarankan peningkatan performa

    Aturan ini membantu generasi dokumentasi:

    Bantu menyusun dokumentasi dengan:

    * Mengekstrak komentar kode
    * Menganalisis README.md
    * Menghasilkan dokumentasi markdown
  </Accordion>

  <Accordion title="Menambahkan pengaturan baru di Cursor">
    Pertama, bikin properti toggle di `@reactiveStorageTypes.ts`.

    Tambahkan nilai default di `INIT_APPLICATION_USER_PERSISTENT_STORAGE` dalam `@reactiveStorageService.tsx`.

    Untuk fitur beta, tambahkan toggle di `@settingsBetaTab.tsx`, kalau bukan, tambahkan di `@settingsGeneralTab.tsx`. Toggle bisa ditambahkan sebagai `<SettingsSubSection>` untuk checkbox umum. Lihat bagian lain file untuk contoh.

    ```
    <SettingsSubSection
    				label="Nama fitur kamu"
    				description="Deskripsi fitur kamu"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    Untuk dipakai di app, import reactiveStorageService dan gunakan propertinya:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Banyak contoh tersedia dari berbagai provider dan framework. Aturan yang dikontribusikan komunitas bisa ditemukan di beragam koleksi dan repositori crowdsourced online.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` adalah file markdown sederhana untuk mendefinisikan instruksi agent. Simpan di root proyek sebagai alternatif `.cursor/rules` untuk use case yang straightforward.

Berbeda dari Project Rules, `AGENTS.md` adalah file markdown polos tanpa metadata atau konfigurasi yang kompleks. Pas banget buat proyek yang butuh instruksi sederhana, mudah dibaca, tanpa overhead aturan terstruktur.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [Konsep](./konsep.md) →