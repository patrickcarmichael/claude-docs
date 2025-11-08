# SSO

**Navigation:** [← Previous](./15-serveurs-mcp.md) | [Index](./index.md) | [Next →](./17-web.md)

---

# SSO
Source: https://docs.cursor.com/id/account/teams/sso

Setel single sign-on buat tim lo

<div id="overview">
  ## Ikhtisar
</div>

SSO SAML 2.0 tersedia tanpa biaya tambahan di paket Business. Pakai identity provider (IdP) yang sudah ada buat mengautentikasi anggota tim tanpa perlu akun Cursor terpisah.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Prasyarat
</div>

* Paket Cursor Team
* Akses admin ke penyedia identitas lo (misalnya Okta)
* Akses admin ke organisasi Cursor lo

<div id="configuration-steps">
  ## Langkah Konfigurasi
</div>

<Steps>
  <Step title="Masuk ke akun Cursor lo">
    Buka [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) pakai akun admin.
  </Step>

  <Step title="Cari konfigurasi SSO">
    Temuin bagian "Single Sign-On (SSO)" lalu buka.
  </Step>

  <Step title="Mulai proses setup">
    Klik tombol "SSO Provider Connection settings" buat mulai setup SSO dan ikutin wizard.
  </Step>

  <Step title="Konfigurasi identity provider lo">
    Di identity provider lo (misalnya Okta):

    * Bikin aplikasi SAML baru
    * Konfigurasi pengaturan SAML pakai info dari Cursor
    * Set up Just-in-Time (JIT) provisioning
  </Step>

  <Step title="Verifikasi domain">
    Verifikasi domain user lo di Cursor dengan klik tombol "Domain verification settings".
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Panduan Setup Identity Provider
</div>

Buat instruksi setup per provider:

<Card title="Panduan Identity Provider" icon="book" href="https://workos.com/docs/integrations">
  Instruksi setup untuk Okta, Azure AD, Google Workspace, dan lainnya.
</Card>

<div id="additional-settings">
  ## Pengaturan Tambahan
</div>

* Atur penerapan SSO lewat dasbor admin
* Pengguna baru otomatis terdaftar saat masuk lewat SSO
* Kelola pengguna lewat penyedia identitas lo

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

Kalau ada masalah:

* Pastikan domain sudah terverifikasi di Cursor
* Pastikan atribut SAML dipetakan dengan benar
* Cek SSO sudah diaktifkan di dasbor admin
* Samakan nama depan dan belakang antara identity provider dan Cursor
* Cek panduan khusus penyedia di atas
* Hubungi [hi@cursor.com](mailto:hi@cursor.com) kalau masalah tetap berlanjut



# Akses Pembaruan
Source: https://docs.cursor.com/id/account/update-access

Pilih seberapa sering kamu mau menerima pembaruan

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor punya dua kanal pembaruan.

<Tabs>
  <Tab title="Default">
    Kanal pembaruan standar dengan rilis yang sudah diuji.

    * Rilis stabil
    * Perbaikan bug dari pengujian pra-rilis
    * Standar untuk semua pengguna
    * Satu-satunya opsi untuk pengguna tim

    <Note>
      Akun tim dan bisnis pakai mode Default.
    </Note>
  </Tab>

  <Tab title="Early Access">
    Versi pra-rilis dengan fitur baru.

    <Warning>
      Build Early Access bisa mengandung bug atau masalah stabilitas.
    </Warning>

    * Akses ke fitur yang masih dikembangkan
    * Mungkin mengandung bug
    * Tidak tersedia untuk akun tim
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## Ubah kanal pembaruan
</div>

1. **Buka pengaturan**: Tekan <Kbd>Cmd+Shift+J</Kbd>
2. **Buka Beta**: Pilih Beta di sidebar
3. **Pilih kanal**: Pilih Default atau Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Laporkan masalah Early Access di [Forum](https://forum.cursor.com).



# Apply
Source: https://docs.cursor.com/id/agent/apply

Pelajari cara menerapkan, menerima, atau menolak saran kode dari chat menggunakan Apply

<div id="how-apply-works">
  ## Cara kerja Apply
</div>

Apply adalah model khusus di Cursor yang mengambil kode yang dihasilkan oleh chat dan mengintegrasikannya ke file lo. Model ini memproses blok kode dari percakapan chat dan menerapkan perubahan tersebut ke codebase lo.

Apply tidak menghasilkan kode sendiri. Model chat yang menghasilkan kode, sementara Apply menangani integrasinya ke file yang sudah ada. Model ini bisa memproses perubahan di banyak file dan pada codebase yang besar.

<div id="apply-code-blocks">
  ## Menerapkan blok kode
</div>

Untuk menerapkan saran pada blok kode, tekan tombol play di pojok kanan atas blok kode.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/id/agent/chat/checkpoints

Simpan dan pulihkan state sebelumnya setelah perubahan Agent

Checkpoints adalah snapshot otomatis dari perubahan Agent ke codebase lo. Fitur ini bikin lo bisa nge-undo modifikasi Agent kalau perlu.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Memulihkan checkpoint
</div>

Ada dua cara untuk memulihkan:

1. **Dari kotak input**: Klik tombol `Restore Checkpoint` pada permintaan sebelumnya
2. **Dari pesan**: Klik tombol + saat mengarahkan kursor ke sebuah pesan

<Warning>
  Checkpoint bukan sistem version control. Pakai Git untuk riwayat permanen.
</Warning>

<div id="how-they-work">
  ## Cara kerjanya
</div>

* Disimpan secara lokal, terpisah dari Git
* Hanya melacak perubahan Agent (bukan edit manual)
* Dibersihkan secara otomatis

<Note>
  Edit manual nggak dilacak. Pakai checkpoint cuma untuk perubahan Agent.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah checkpoint berpengaruh ke Git?">
    Nggak. Mereka terpisah dari riwayat Git.
  </Accordion>

  {" "}

  <Accordion title="Berapa lama disimpan?">
    Buat sesi saat ini dan riwayat terbaru. Dibersihkan otomatis.
  </Accordion>

  <Accordion title="Bisa bikin manual?">
    Nggak. Mereka dibuat otomatis oleh Cursor.
  </Accordion>
</AccordionGroup>

{" "}



# Perintah
Source: https://docs.cursor.com/id/agent/chat/commands

Tentukan perintah untuk alur kerja yang dapat digunakan ulang

Perintah kustom memungkinkan lo bikin alur kerja yang bisa dipakai ulang dan dipicu dengan awalan sederhana `/` di kotak input chat. Perintah ini bantu nyeragamin proses di seluruh tim lo dan bikin tugas-tugas umum jadi lebih efisien.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Perintah saat ini masih beta. Fitur dan sintaksnya bisa berubah seiring kami terus ningkatin fiturnya.
</Info>

<div id="how-commands-work">
  ## Cara kerja command
</div>

Command didefinisikan sebagai file Markdown biasa yang bisa disimpan di dua lokasi:

1. **Project commands**: Disimpan di direktori `.cursor/commands` di project lo
2. **Global commands**: Disimpan di direktori `~/.cursor/commands` di home directory lo

Saat lo ngetik `/` di kotak input chat, Cursor bakal otomatis mendeteksi dan nampilin command yang tersedia dari kedua direktori tersebut, jadi langsung bisa diakses di seluruh workflow lo.

<div id="creating-commands">
  ## Membuat command
</div>

1. Bikin direktori `.cursor/commands` di root project
2. Tambahin file `.md` dengan nama yang deskriptif (misalnya, `review-code.md`, `write-tests.md`)
3. Tulis konten Markdown biasa yang ngejelasin apa yang harus dilakukan command
4. Command bakal otomatis muncul di chat pas lo ngetik `/`

Nih contoh struktur direktori command lo:

```
.cursor/
└── commands/
    ├── tanggapi-komentar-pr-github.md
    ├── daftar-periksa-code-review.md
    ├── buat-pr.md
    ├── review-ringan-diff-yang-ada.md
    ├── onboarding-developer-baru.md
    ├── jalankan-semua-test-dan-perbaiki.md
    ├── audit-keamanan.md
    └── setup-fitur-baru.md
```

<div id="examples">
  ## Contoh
</div>

Coba perintah ini di proyek lo biar kerasa cara kerjanya.

<AccordionGroup>
  <Accordion title="Checklist code review">
    ```markdown  theme={null}
    # Daftar Periksa Code Review

    ## Ikhtisar
    Daftar periksa komprehensif untuk melakukan code review menyeluruh demi memastikan kualitas, keamanan, dan kemudahan pemeliharaan.

    ## Kategori Review

    ### Fungsionalitas
    - [ ] Kode berfungsi sesuai yang diharapkan
    - [ ] Kasus tepi ditangani
    - [ ] Penanganan error sudah tepat
    - [ ] Tidak ada bug atau kesalahan logika yang jelas

    ### Kualitas Kode
    - [ ] Kode mudah dibaca dan terstruktur dengan baik
    - [ ] Fungsi kecil dan fokus
    - [ ] Nama variabel deskriptif
    - [ ] Tidak ada duplikasi kode
    - [ ] Mengikuti konvensi proyek

    ### Keamanan
    - [ ] Tidak ada kerentanan keamanan yang jelas
    - [ ] Validasi input diterapkan
    - [ ] Data sensitif ditangani dengan benar
    - [ ] Tidak ada secret yang di-hardcode
    ```
  </Accordion>

  <Accordion title="Audit keamanan">
    ```markdown  theme={null}
    # Audit Keamanan

    ## Ringkasan
    Tinjauan keamanan menyeluruh untuk mengidentifikasi dan memperbaiki kerentanan pada codebase.

    ## Langkah
    1. **Audit dependensi**
       - Periksa kerentanan yang diketahui
       - Perbarui paket yang usang
       - Tinjau dependensi pihak ketiga

    2. **Tinjauan keamanan kode**
       - Periksa kerentanan umum
       - Tinjau autentikasi/otorisasi
       - Audit praktik penanganan data

    3. **Keamanan infrastruktur**
       - Tinjau variabel lingkungan
       - Periksa kontrol akses
       - Audit keamanan jaringan

    ## Daftar Periksa Keamanan
    - [ ] Dependensi diperbarui dan aman
    - [ ] Tidak ada secret yang di-hardcode
    - [ ] Validasi input diimplementasikan
    - [ ] Autentikasi aman
    - [ ] Otorisasi dikonfigurasi dengan benar
    ```
  </Accordion>

  <Accordion title="Siapkan fitur baru">
    ```markdown  theme={null}
    # Menyiapkan Fitur Baru

    ## Ringkasan
    Menyiapkan fitur baru secara sistematis dari perencanaan awal hingga struktur implementasinya.

    ## Langkah
    1. **Tentukan requirement**
       - Perjelas cakupan dan tujuan fitur
       - Identifikasi user story dan acceptance criteria
       - Rencanakan pendekatan teknis

    2. **Buat feature branch**
       - Branch dari main/develop
       - Siapkan environment pengembangan lokal
       - Konfigurasi dependensi baru (jika ada)

    3. **Rencanakan arsitektur**
       - Rancang model data dan API
       - Rencanakan komponen UI dan alurnya
       - Pertimbangkan strategi pengujian

    ## Checklist Setup Fitur
    - [ ] Requirement terdokumentasi
    - [ ] User story ditulis
    - [ ] Pendekatan teknis direncanakan
    - [ ] Feature branch dibuat
    - [ ] Environment pengembangan siap
    ```
  </Accordion>

  <Accordion title="Buat pull request">
    ```markdown  theme={null}
    # Buat PR

    ## Ringkasan
    Bikin pull request yang terstruktur rapi dengan deskripsi, label, dan reviewer yang tepat.

    ## Langkah
    1. **Siapkan branch**
       - Pastikan semua perubahan sudah di-commit
       - Push branch ke remote
       - Pastikan branch sudah up-to-date dengan main

    2. **Tulis deskripsi PR**
       - Ringkas perubahan dengan jelas
       - Sertakan konteks dan motivasi
       - Cantumkan perubahan yang bersifat breaking
       - Tambahkan screenshot kalau ada perubahan UI

    3. **Setelan PR**
       - Bikin PR dengan judul yang deskriptif
       - Tambahkan label yang sesuai
       - Assign reviewer
       - Tautkan issue terkait

    ## Template PR
    - [ ] Fitur A
    - [ ] Perbaikan bug B
    - [ ] Unit test lulus
    - [ ] Pengujian manual selesai
    ```
  </Accordion>

  <Accordion title="Jalankan test dan perbaiki kegagalan">
    ```markdown  theme={null}
    # Jalankan Semua Tes dan Perbaiki Kegagalan

    ## Ringkasan
    Jalankan seluruh suite pengujian dan perbaiki kegagalan secara sistematis untuk memastikan kualitas dan fungsionalitas kode.

    ## Langkah
    1. **Jalankan suite pengujian**
       - Jalankan semua tes di proyek
       - Simpan output dan identifikasi kegagalan
       - Periksa baik unit test maupun integration test

    2. **Analisis kegagalan**
       - Kategorikan berdasarkan jenis: flaky, broken, failure baru
       - Prioritaskan perbaikan berdasarkan dampaknya
       - Cek apakah kegagalan terkait perubahan terbaru

    3. **Perbaiki masalah secara sistematis**
       - Mulai dari kegagalan yang paling kritis
       - Perbaiki satu masalah dalam satu waktu
       - Jalankan ulang tes setelah setiap perbaikan
    ```
  </Accordion>

  <Accordion title="Onboard developer baru">
    ```markdown  theme={null}
    # Onboarding Developer Baru

    ## Ringkasan
    Proses onboarding komprehensif agar developer baru bisa segera siap dan produktif.

    ## Langkah
    1. **Penyiapan environment**
       - Instal tool yang diperlukan
       - Siapkan environment pengembangan
       - Konfigurasi IDE dan ekstensi
       - Siapkan git dan key SSH

    2. **Pengenalan proyek**
       - Tinjau struktur proyek
       - Pahami arsitektur
       - Baca dokumentasi utama
       - Siapkan database lokal

    ## Daftar Periksa Onboarding
    - [ ] Environment pengembangan siap
    - [ ] Semua test lulus
    - [ ] Bisa menjalankan aplikasi secara lokal
    - [ ] Database disiapkan dan berjalan
    - [ ] PR pertama diajukan
    ```
  </Accordion>
</AccordionGroup>



# Compact
Source: https://docs.cursor.com/id/agent/chat/compact

Hemat ruang di chat dengan antarmuka mode compact

Mode compact nyediain antarmuka chat yang ringkas dengan ngurangin distraksi visual dan memaksimalkan ruang buat percakapan.

<div id="overview">
  ## Ikhtisar
</div>

Saat diaktifkan, mode ringkas mengubah antarmuka chat dengan:

* **Menyembunyikan ikon** untuk tampilan yang lebih bersih dan minimalis
* **Secara otomatis menciutkan diff** untuk mengurangi kebisingan visual
* **Secara otomatis menciutkan input** untuk memaksimalkan ruang percakapan

Pengaturan ini sangat berguna saat bekerja di layar yang lebih kecil atau kalau kamu lebih suka pengalaman chat yang fokus dan bebas distraksi.

<div id="before-and-after">
  ## Sebelum dan Sesudah
</div>

<div id="default-mode">
  ### Mode bawaan
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="Antarmuka chat dalam mode bawaan yang menampilkan semua ikon dan elemen yang diperluas" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### Mode ringkas
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="Antarmuka chat dalam mode ringkas dengan ikon yang disembunyikan dan elemen yang diciutkan" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## Mengaktifkan mode ringkas
</div>

Untuk mengaktifkan mode ringkas:

1. Buka Cursor Settings
2. Buka pengaturan **Chat**
3. Aktifkan **Compact Mode**

Antarmuka akan langsung beralih ke tampilan yang lebih ringkas, ngasih kamu lebih banyak ruang buat fokus ke percakapan.



# Duplikat
Source: https://docs.cursor.com/id/agent/chat/duplicate

Bikin branch dari titik mana pun dalam percakapan

Duplikasi/fork chat buat ngeksplor solusi alternatif tanpa kehilangan percakapan yang lagi jalan.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## Cara menduplikasi
</div>

1. Tentukan titik tempat kamu mau mulai branch
2. Klik ikon tiga titik pada pesan
3. Pilih "Duplicate Chat"

<div id="what-happens">
  ## Apa yang terjadi
</div>

* Konteks sampai titik itu tetap tersimpan
* Percakapan asli tetap apa adanya
* Kedua chat menyimpan riwayatnya masing-masing



# Ekspor
Source: https://docs.cursor.com/id/agent/chat/export

Ekspor obrolan ke format Markdown

Ekspor obrolan Agent sebagai file Markdown untuk dibagikan atau didokumentasikan.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## Apa yang diekspor
</div>

* Semua pesan dan respons
* Blok kode dengan penyorotan sintaks
* Referensi file dan konteks
* Alur percakapan secara kronologis

<div id="how-to-export">
  ## Cara mengekspor
</div>

1. Buka chat yang ingin diekspor
2. Klik menu konteks → "Export Chat"
3. Simpan file ke lokal

<Warning>
  Periksa hasil ekspor untuk data sensitif: kunci API, URL internal, kode berpemilik,
  informasi pribadi
</Warning>



# Riwayat
Source: https://docs.cursor.com/id/agent/chat/history

Lihat dan kelola percakapan chat

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Akses percakapan Agent yang lalu dari panel riwayat.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Riwayat Chat" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## Membuka histori
</div>

* Klik ikon histori di panel samping Agent
* Tekan <Kbd tooltip="Open chat history">Opt Cmd '</Kbd>

<div id="managing-chats">
  ## Mengelola chat
</div>

* **Edit judul**: Klik untuk mengganti nama
* **Hapus**: Hapus chat yang nggak diperlukan
* **Buka**: Klik untuk meninjau percakapan lengkap

Riwayat chat disimpan secara lokal di database SQLite di mesin kamu.

<Note>
  Biar chat tetap tersimpan, [ekspor](/id/agent/chats/export) sebagai markdown.
</Note>

<div id="background-agents">
  ## Background Agents
</div>

Obrolan background agent nggak muncul di riwayat biasa, tapi disimpan di database remote. Pakai <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> buat ngeliatnya.

<div id="referencing-past-chats">
  ## Mereferensikan chat sebelumnya
</div>

Gunakan [@Past Chats](/id/context/@-symbols/@-past-chats) buat masukin konteks dari percakapan sebelumnya ke chat lo yang sekarang.



# Ringkasan
Source: https://docs.cursor.com/id/agent/chat/summarization

Pengelolaan konteks untuk percakapan panjang di chat

<div id="message-summarization">
  ## Perangkuman pesan
</div>

Saat percakapan makin panjang, Cursor otomatis meringkas dan mengelola konteks supaya chat tetap efisien. Pelajari cara pakai context menu dan pahami bagaimana file diringkas agar muat dalam window konteks model.

<div id="using-the-summarize-command">
  ### Menggunakan perintah /summarize
</div>

Kamu bisa menjalankan peringkasan secara manual pakai perintah `/summarize` di chat. Perintah ini membantu ngatur konteks saat percakapan jadi terlalu panjang, jadi kamu bisa tetap lanjut kerja dengan efisien tanpa kehilangan info penting.

<Info>
  Buat bahasan lebih mendalam tentang cara kerja konteks di Cursor, cek panduan [Bekerja dengan Konteks](/id/guides/working-with-context).
</Info>

<div id="how-summarization-works">
  ### Cara kerja peringkasan
</div>

Saat percakapan makin panjang, percakapan itu bisa melampaui batas context window model:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Batas context window</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Buat ngatasi ini, Cursor meringkas pesan yang lebih lama supaya ada ruang untuk percakapan baru.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Batas context window
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Pesan yang Dirangkum
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

## Kondensasi file & folder

Kalau peringkasan chat ngurusin percakapan panjang, Cursor pakai strategi beda buat nge-handle file dan folder yang besar: **kondensasi cerdas**. Kalau lo nyertakan file dalam percakapan, Cursor bakal nentuin cara terbaik buat nampilin file itu berdasarkan ukurannya dan ruang konteks yang tersedia.

Berikut berbagai status yang bisa dimiliki file/folder:

<div id="condensed">
  ### Ringkas
</div>

Saat file atau folder terlalu besar untuk dimuat dalam jendela konteks, Cursor otomatis meringkasnya. Peringkasan menampilkan ke model elemen struktural penting seperti tanda tangan fungsi, kelas, dan metode. Dari tampilan ringkas ini, model bisa memilih buat memperluas file tertentu kalau diperlukan. Pendekatan ini memaksimalkan pemanfaatan jendela konteks yang tersedia.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Menu konteks" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Dipadatkan secara signifikan
</div>

Saat nama file muncul dengan label "Dipadatkan secara signifikan", berarti file tersebut terlalu besar untuk disertakan secara penuh, bahkan dalam bentuk ringkas. Hanya nama file yang akan ditampilkan ke model.

<div id="not-included">
  ### Tidak disertakan
</div>

Kalau ikon peringatan muncul di sebelah file atau folder, berarti item itu terlalu besar buat dimasukin ke jendela konteks, bahkan dalam bentuk ringkas. Ini bantu lo ngerti bagian mana dari codebase yang bisa diakses model.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# Tab
Source: https://docs.cursor.com/id/agent/chat/tabs

Jalankan beberapa percakapan Agent sekaligus

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## Ikhtisar
</div>

Tekan <Kbd>Cmd+T</Kbd> untuk membuat tab baru. Setiap tab punya riwayat percakapan, konteks, dan pilihan modelnya sendiri.

<Tip>
  Buat alur kerja paralel, coba [Background Agents](/id/background-agents)
</Tip>

<div id="managing-tabs">
  ## Mengelola tab
</div>

* Bikin tab baru dengan <Kbd>Cmd+T</Kbd>. Setiap tab dimulai dengan percakapan baru dan punya konteksnya sendiri.

* Pindah antartab dengan klik header-nya atau pakai <Kbd>Ctrl+Tab</Kbd> buat ganti tab satu per satu.

* Judul tab dibuat otomatis setelah pesan pertama, tapi lo bisa ganti dengan klik kanan di header tab.

<Tip>
  Pakai satu task per tab, kasih deskripsi awal yang jelas, dan tutup tab
  yang sudah selesai biar workspace lo tetap rapi.
</Tip>

<div id="conflicts">
  ### Konflik
</div>

Cursor mencegah beberapa tab ngedit file yang sama. Lo bakal diminta buat menyelesaikan konflik.

<div id="reference-other-chats">
  ## Rujuk obrolan lain
</div>

Gunakan [@Past Chats](/id/context/@-symbols/@-past-chats) buat nyertain konteks dari tab lain atau sesi sebelumnya.



# Mode
Source: https://docs.cursor.com/id/agent/modes

Pilih mode yang pas buat tugasmu—dari coding otonom sampai edit yang fokus

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent punya beberapa mode yang dioptimalkan buat tugas tertentu. Tiap mode punya kapabilitas dan tools berbeda yang diaktifkan biar sesuai kebutuhan workflow lo.

<div className="full-width-table">
  | Mode                  | Untuk                             | Kapabilitas                                    | Tools                |
  | :-------------------- | :-------------------------------- | :--------------------------------------------- | :------------------- |
  | **[Agent](#agent)**   | Fitur kompleks, refactoring       | Eksplorasi otonom, edit multi-file             | Semua tools aktif    |
  | **[Ask](#ask)**       | Belajar, perencanaan, tanya-jawab | Eksplorasi read-only, tanpa perubahan otomatis | Tools pencarian saja |
  | **[Custom](#custom)** | Workflow khusus                   | Kapabilitas yang ditentukan pengguna           | Bisa dikonfigurasi   |
</div>

<div id="agent">
  ## Agent
</div>

Mode bawaan untuk tugas coding yang kompleks. Agent secara otomatis menelusuri codebase, mengedit banyak file, menjalankan perintah, dan memperbaiki error buat nyelesaiin permintaan lo.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

Mode baca-saja untuk belajar dan eksplorasi. Ask menelusuri codebase lo dan kasih jawaban tanpa bikin perubahan apa pun—pas banget buat paham kode sebelum ngedit.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## Kustom
</div>

Bikin mode sendiri dengan kombinasi tool dan instruksi spesifik. Mix and match kapabilitas biar pas sama workflow-mu.

<Note>
  Mode kustom masih beta. Aktifkan di `Cursor Settings` → `Chat` → `Custom
      Modes`
</Note>

<div id="examples">
  ### Contoh
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **Tools:** All Search\
    **Instructions:** Fokus menjelaskan konsep secara menyeluruh dan ajukan pertanyaan klarifikasi
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Tools:** Edit & Reapply **Instructions:** Perbaiki struktur kode tanpa
    nambah fungsionalitas baru
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Tools:** Codebase, Read file, Terminal **Instructions:** Bikin rencana implementasi yang detail di `plan.md`
  </Accordion>

  <Accordion title="Debug">
    **Tools:** All Search, Terminal, Edit & Reapply\
    **Instructions:** Investigasi masalah secara menyeluruh sebelum ngasih solusi
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## Mengganti mode
</div>

* Pakai dropdown pemilih mode di Agent
* Tekan <Kbd>Cmd+.</Kbd> untuk beralih cepat
* Atur pintasan keyboard di [settings](#settings)

<div id="settings">
  ## Settings
</div>

Semua mode punya opsi konfigurasi yang sama:

<div className="full-width-table">
  | Setting            | Description                         |
  | :----------------- | :---------------------------------- |
  | Model              | Pilih model AI yang dipakai         |
  | Keyboard shortcuts | Set shortcut buat pindah antar mode |
</div>

Pengaturan khusus per mode:

<div className="full-width-table">
  | Mode       | Settings                      | Description                                            |
  | :--------- | :---------------------------- | :----------------------------------------------------- |
  | **Agent**  | Auto-run and Auto-fix Errors  | Jalanin perintah otomatis dan benerin error            |
  | **Ask**    | Search Codebase               | Otomatis nyari file yang relevan                       |
  | **Custom** | Tool selection & Instructions | Konfigurasi [tools](/id/agent/tools) dan prompt khusus |
</div>



# Ikhtisar
Source: https://docs.cursor.com/id/agent/overview

Asisten untuk tugas pengkodean otonom, perintah terminal, dan penyuntingan kode

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent adalah asisten Cursor yang bisa menyelesaikan tugas coding yang kompleks secara mandiri, menjalankan perintah terminal, dan mengedit kode. Akses lewat sidepane dengan <Kbd>Cmd+I</Kbd>.

<Frame caption="Agent di sidepane">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/id/agent/modes" className="hover:text-primary transition-colors">
          Mode
        </a>
      </h2>

      <p className="text-sm">
        Pilih antara Agent, Ask, atau bikin mode kustom. Tiap mode punya
        kapabilitas dan tools yang beda-beda biar cocok sama workflow lo.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Mode Agent" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/tools" className="hover:text-primary transition-colors">
          Tools
        </a>
      </h3>

      <p className="text-sm">
        Agent menggunakan tools untuk mencari, mengedit, dan menjalankan perintah. Mulai dari pencarian codebase semantik hingga eksekusi di terminal, tools ini memungkinkan penyelesaian tugas secara otonom.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Tools Agent" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/apply" className="hover:text-primary transition-colors">
          Terapkan Perubahan
        </a>
      </h3>

      <p className="text-sm">
        Integrasikan blok kode yang direkomendasikan AI ke codebase lo. Apply menangani
        perubahan berskala besar secara efisien sambil tetap presisi.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="Terapkan perubahan" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/review" className="hover:text-primary transition-colors">
          Tinjau Diff
        </a>
      </h3>

      <p className="text-sm">
        Cek perubahan sebelum menyetujuinya. Antarmuka peninjauan menampilkan penambahan
        dan penghapusan dengan baris berwarna agar kamu bisa mengontrol modifikasi.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/chats/tabs" className="hover:text-primary transition-colors">
          Tab Obrolan
        </a>
      </h3>

      <p className="text-sm">
        Jalankan beberapa percakapan sekaligus dengan <Kbd>Cmd+T</Kbd>. Setiap tab
        mempertahankan konteks, riwayat, dan pilihan modelnya sendiri.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          Checkpoints
        </a>
      </h3>

      <p className="text-sm">
        Snapshot otomatis ngelacak perubahan Agent. Balikin ke status sebelumnya kalau
        perubahan nggak jalan sesuai ekspektasi atau buat nyoba pendekatan lain.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/terminal" className="hover:text-primary transition-colors">
          Integrasi Terminal
        </a>
      </h3>

      <p className="text-sm">
        Agent mengeksekusi perintah terminal, memantau output, dan menangani proses
        multi-tahap. Atur auto-run untuk alur kerja tepercaya atau minta
        konfirmasi demi keamanan.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Integrasi terminal" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/chats/history" className="hover:text-primary transition-colors">
          Riwayat Chat
        </a>
      </h3>

      <p className="text-sm">
        Akses percakapan sebelumnya dengan <Kbd>Opt Cmd '</Kbd>. Tinjau
        diskusi terdahulu, lacak sesi ngoding, dan rujuk konteks dari chat
        sebelumnya.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Riwayat chat" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/agent/chats/export" className="hover:text-primary transition-colors">
          Ekspor Chat
        </a>
      </h3>

      <p className="text-sm">
        Ekspor percakapan ke format Markdown. Bagikan solusi ke anggota tim, dokumentasikan keputusan, atau bikin knowledge base dari sesi ngoding.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/id/context/rules" className="hover:text-primary transition-colors">
          Aturan
        </a>
      </h3>

      <p className="text-sm">
        Tentukan instruksi khusus buat perilaku Agent. Aturan bantu ngejaga standar
        penulisan kode, menegakkan pola, dan ngepersonalisasi cara Agent ngebantu
        proyek lo.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Aturan Agent" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Perencanaan
Source: https://docs.cursor.com/id/agent/planning

Cara Agent merencanakan dan mengelola tugas kompleks dengan to-do dan antrean

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent bisa merencanakan terlebih dulu dan mengelola tugas kompleks dengan daftar tugas yang terstruktur serta antrian pesan, sehingga tugas berjangka panjang lebih mudah dipahami dan dipantau.

<div id="agent-to-dos">
  ## To-do Agent
</div>

Agent bisa memecah tugas panjang menjadi langkah-langkah yang mudah dikelola dengan dependensi, sehingga terbentuk rencana terstruktur yang terus diperbarui seiring progres kerja.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Cara kerja
</div>

* Agent otomatis membuat daftar to-do untuk tugas kompleks
* Tiap item bisa punya dependensi pada tugas lain
* Daftar diperbarui secara real-time seiring progres berjalan
* Tugas yang selesai ditandai otomatis

<div id="visibility">
  ### Visibilitas
</div>

* To-do muncul di antarmuka chat
* Kalau [integrasi Slack](/id/slack) disetel, to-do juga keliatan di sana
* Kamu bisa melihat rincian pemecahan tugas lengkap kapan aja

<Tip>
  Biar perencanaannya lebih bagus, jelasin tujuan akhirnya dengan jelas. Agent bakal bikin
  pemecahan tugas yang lebih akurat kalau paham cakupan penuh.
</Tip>

<Note>Perencanaan dan to-do saat ini belum didukung di mode otomatis.</Note>

<div id="queued-messages">
  ## Pesan dalam antrean
</div>

Antre pesan lanjutan sementara Agent ngerjain tugas saat ini. Instruksi lo nunggu di antrean dan jalan otomatis begitu siap.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Menggunakan antrean
</div>

1. Sambil Agent bekerja, ketik instruksi berikutnya
2. Tekan <Kbd>Ctrl+Enter</Kbd> buat nambahkannya ke antrean
3. Pesan muncul berurutan di bawah tugas aktif
4. Ubah urutan pesan yang diantrikan dengan klik panah
5. Agent bakal memprosesnya satu per satu setelah selesai

<div id="override-the-queue">
  ### Mengabaikan antrean
</div>

Buat masukin pesan lo ke antrean alih-alih pakai pengiriman default, gunakan <Kbd>Ctrl+Enter</Kbd>. Buat ngirim pesan langsung tanpa diantrikan, gunakan <Kbd>Cmd+Enter</Kbd>. Ini bakal “memaksa” pesan lo dikirim, ngelewatin antrean supaya langsung dieksekusi.

<div id="default-messaging">
  ## Pesan default
</div>

Secara default, pesan dikirim secepat mungkin, biasanya muncul tepat setelah Agent selesai menjalankan pemanggilan tool. Ini bikin pengalaman jadi paling responsif.

<div id="how-default-messaging-works">
  ### Cara kerja pesan default
</div>

* Pesan lo bakal digabung ke pesan user terbaru di chat
* Pesan biasanya menempel ke hasil tool dan langsung dikirim begitu siap
* Ini bikin alur percakapan lebih natural tanpa mengganggu kerja Agent saat ini
* Secara default, ini kejadian saat lo menekan Enter sementara Agent lagi bekerja



# Diffs & Review
Source: https://docs.cursor.com/id/agent/review

Tinjau dan kelola perubahan kode yang dihasilkan oleh agen AI

Saat Agent menghasilkan perubahan kode, perubahan tersebut ditampilkan dalam antarmuka review yang menandai penambahan dan penghapusan dengan baris berwarna. Ini memungkinkan kamu meninjau dan menentukan perubahan mana yang diterapkan ke codebase kamu.

Antarmuka review menampilkan perubahan kode dalam format diff yang familiar:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Meaning                         | Example                                                                                               |
  | :---------------- | :------------------------------ | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | Penambahan kode baru            | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Penghapusan kode                | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Kode konteks yang tidak berubah | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Review
</div>

Setelah proses generasi selesai, bakal muncul prompt buat nge-review semua perubahan sebelum lanjut. Ini ngasih gambaran umum tentang apa aja yang bakal diubah.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Antarmuka review input" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Per berkas
</div>

Bilah review mengambang bakal muncul di bagian bawah layar, bikin lo bisa:

* **Accept** atau **Reject** perubahan untuk berkas saat ini
* Pindah ke **next file** yang masih punya perubahan tertunda
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Browser lo nggak mendukung tag video.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Penerimaan selektif
</div>

Buat kontrol yang lebih detail:

* Buat nerima sebagian besar perubahan: tolak baris yang nggak diinginkan, lalu klik **Accept all**
* Buat nolak sebagian besar perubahan: terima baris yang diinginkan, lalu klik **Reject all**

<div id="review-changes">
  ## Tinjau perubahan
</div>

Di akhir respons agent, klik tombol **Tinjau perubahan** untuk melihat diff lengkap dari perubahan.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/id/agent/terminal

Jalankan perintah terminal secara otomatis sebagai bagian dari operasi agen

Agen mengeksekusi perintah di terminal native Cursor dengan riwayat yang tetap tersimpan. Klik Skip untuk mengirim <kbd>Ctrl+C</kbd> dan menghentikan perintah.

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

<Info>
  Beberapa tema shell (misalnya Powerlevel9k/Powerlevel10k) bisa mengganggu
  output terminal inline. Kalau output perintah kelihatan terpotong atau
  salah format, nonaktifkan temanya atau ganti ke prompt yang lebih sederhana saat Agent berjalan.
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### Nonaktifkan prompt berat untuk sesi Agent
</div>

Pakai variabel lingkungan `CURSOR_AGENT` di konfigurasi shell buat mendeteksi kapan
Agent lagi berjalan dan lewati inisialisasi prompt/tema yang “fancy”.

```zsh  theme={null}

# ~/.zshrc — nonaktifkan Powerlevel10k saat Cursor Agent berjalan
if [[ -n "$CURSOR_AGENT" ]]; then
  # Lewati inisialisasi tema untuk meningkatkan kompatibilitas
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — gunakan prompt sederhana sebagai cadangan dalam sesi Agent
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Tools
Source: https://docs.cursor.com/id/agent/tools

Tools yang tersedia untuk agen buat nyari, ngedit, dan ngejalanin kode

Daftar semua tools yang tersedia buat mode di dalam [Agent](/id/agent/overview), yang bisa lo aktifin atau nonaktifin waktu bikin [custom modes](/id/agent/modes#custom) lo sendiri.

<Note>
  Nggak ada batas jumlah panggilan tool yang bisa dilakukan Agent selama suatu tugas. Agent bakal terus pakai tools sesuai kebutuhan sampai permintaan lo kelar.
</Note>

<div id="search">
  ## Pencarian
</div>

Alat untuk menelusuri codebase dan web demi menemukan informasi yang relevan.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Membaca hingga 250 baris (750 dalam mode maksimum) dari sebuah file.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Membaca struktur direktori tanpa membaca isi file.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Melakukan pencarian semantik dalam [codebase
    yang terindeks](/id/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Mencari kata kunci atau pola yang persis di dalam file.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Menemukan file berdasarkan nama menggunakan fuzzy matching.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Membuat kueri pencarian dan melakukan penelusuran web.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Mengambil [rules](/id/context/rules) tertentu berdasarkan tipe dan deskripsinya.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Edit
</div>

Alat buat ngelakuin edit spesifik ke file dan codebase lo.

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    Ngasih saran edit ke file dan [nge-apply](/id/agent/apply) secara otomatis.
  </Accordion>

  <Accordion title="Delete File" icon="trash">
    Hapus file secara otomatis (bisa dimatiin di settings).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Run
</div>

Chat bisa berinteraksi langsung dengan terminal lo.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Jalanin perintah terminal dan pantau output-nya.
  </Accordion>
</AccordionGroup>

<Note>Secara default, Cursor bakal pakai profil terminal pertama yang tersedia.</Note>

Buat ngatur profil terminal yang lo pengin:

1. Buka Command Palette (`Cmd/Ctrl+Shift+P`)
2. Cari "Terminal: Select Default Profile"
3. Pilih profil yang lo mau

<div id="mcp">
  ## MCP
</div>

Chat bisa pakai server MCP yang sudah dikonfigurasi buat berinteraksi dengan layanan eksternal, seperti database atau API pihak ketiga.

<AccordionGroup>
  <Accordion title="Toggle MCP Servers" icon="server">
    Nyalakan/nonaktifkan server MCP yang tersedia. Mengikuti konfigurasi auto-run.
  </Accordion>
</AccordionGroup>

Pelajari lebih lanjut tentang [Model Context Protocol](/id/context/model-context-protocol) dan jelajahi server yang tersedia di [direktori MCP](/id/tools).

<div id="advanced-options">
  ## Opsi lanjutan
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Terapkan perubahan secara otomatis tanpa konfirmasi manual.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Jalankan perintah terminal dan terima perubahan secara otomatis. Berguna untuk menjalankan test suite dan memverifikasi perubahan.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Konfigurasikan allow list untuk menentukan tool mana yang boleh berjalan otomatis. Allow list meningkatkan keamanan dengan secara eksplisit mendefinisikan operasi yang diizinkan.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Secara otomatis memperbaiki error dan peringatan linter saat ditemui oleh Agent.
  </Accordion>
</AccordionGroup>



# Agen Latar Belakang
Source: https://docs.cursor.com/id/background-agent

Agen jarak jauh asinkron di Cursor

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Dengan background agents, spawn agen asinkron yang mengedit dan menjalankan kode di lingkungan remote. Lihat status mereka, kirim tindak lanjut, atau ambil alih kapan saja.

<div id="how-to-use">
  ## Cara Menggunakan
</div>

Lo bisa akses background agent dengan dua cara:

1. **Background Agent Sidebar**: Pakai tab background agent di sidebar native Cursor buat lihat semua background agent yang terhubung ke akun lo, cari agent yang udah ada, dan mulai yang baru.
2. **Background Agent Mode**: Pencet <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> buat ngaktifin background agent mode di UI.

Abis submit prompt, pilih agent lo dari daftar buat lihat status dan masuk ke mesin.

<Note>
  <p className="!mb-0">
    Background agent butuh retensi data selama beberapa hari.
  </p>
</Note>

<div id="setup">
  ## Setup
</div>

Background agent berjalan di mesin Ubuntu terisolasi secara default. Agent punya akses internet dan bisa memasang paket.

<div id="github-connection">
  #### Koneksi GitHub
</div>

Agen latar belakang nge-clone repo lo dari GitHub dan kerja di branch terpisah, terus nge-push ke repo lo biar gampang dioper.

Kasih hak akses read-write ke repo lo (dan repo atau submodule yang jadi dependensi). Kita bakal dukung penyedia lain (GitLab, Bitbucket, dll.) ke depannya.

<div id="ip-allow-list-configuration">
  ##### Konfigurasi Daftar Izin IP
</div>

Kalau organisasi lo pakai fitur daftar izin IP GitHub, lo perlu ngatur akses buat agen background. Lihat [dokumentasi integrasi GitHub](/id/integrations/github#ip-allow-list-configuration) buat petunjuk setup lengkap, termasuk info kontak dan alamat IP.

<div id="base-environment-setup">
  #### Penyiapan Lingkungan Dasar
</div>

Untuk kasus yang lebih advanced, atur sendiri lingkungannya. Dapatkan instance IDE yang terhubung ke mesin remote. Siapkan mesin kamu, instal tools dan paket, lalu ambil snapshot. Konfigurasikan pengaturan runtime:

* Perintah install berjalan sebelum agent mulai dan memasang dependensi runtime. Ini bisa berarti menjalankan `npm install` atau `bazel build`.
* Terminal menjalankan proses background saat agent bekerja—misalnya menjalankan server web atau mengompilasi file protobuf.

Untuk kasus paling advanced, gunakan Dockerfile untuk penyiapan mesin. Dockerfile memungkinkan kamu menyiapkan dependensi tingkat sistem: memasang versi compiler tertentu, debugger, atau mengganti base OS image. Jangan `COPY` seluruh proyek—kami yang mengelola workspace dan checkout commit yang tepat. Tetap lakukan instalasi dependensi di install script.

Masukkan secrets yang diperlukan untuk lingkungan dev kamu—secrets disimpan terenkripsi at rest (menggunakan KMS) di database kami dan disediakan ke environment agent di background.

Penyiapan mesin ada di `.cursor/environment.json`, yang bisa kamu commit ke repo (direkomendasikan) atau simpan privat. Alur penyiapan akan memandu kamu membuat `environment.json`.

<div id="maintenance-commands">
  #### Perintah Maintenance
</div>

Saat nyiapin mesin baru, kita mulai dari base environment, lalu jalanin perintah `install` dari `environment.json` lo. Perintah ini yang biasa dijalanin developer saat pindah branch—buat install dependency baru.

Buat kebanyakan orang, perintah `install` itu `npm install` atau `bazel build`.

Biar startup mesin cepet, kita nge-cache state disk setelah perintah `install` jalan. Rancang biar bisa dijalanin berkali-kali. Cuma state disk yang ke-persist dari perintah `install`—proses yang dimulai di sini nggak bakal hidup waktu agent mulai.

<div id="startup-commands">
  #### Perintah Startup
</div>

Setelah menjalankan `install`, mesin akan menyala dan kita menjalankan perintah `start`, lalu menyalakan semua `terminals`. Ini memulai proses yang harus tetap berjalan saat agen aktif.

Perintah `start` sering bisa dilewati. Pakai ini kalau environment dev kamu bergantung pada Docker—taruh `sudo service docker start` di perintah `start`.

`terminals` dipakai untuk kode aplikasi. Terminal-terminal ini berjalan dalam sesi `tmux` yang bisa diakses kamu dan agen. Misalnya, banyak repo website menaruh `npm run watch` sebagai sebuah terminal.

<div id="the-environmentjson-spec">
  #### Spesifikasi `environment.json`
</div>

File `environment.json` bisa berbentuk seperti:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Menjalankan Next.js",
      "command": "npm run dev"
    }
  ]
}
```

Secara formal, spesifikasinya [didefinisikan di sini](https://www.cursor.com/schemas/environment.schema.json).

<div id="models">
  ## Model
</div>

Hanya model yang kompatibel dengan [Max Mode](/id/context/max-mode) yang tersedia untuk agen background.

<div id="pricing">
  ## Harga
</div>

Pelajari lebih lanjut tentang [penetapan harga Background Agent](/id/account/pricing#background-agent).

<div id="security">
  ## Keamanan
</div>

Background Agents tersedia dalam Privacy Mode. Kami nggak pernah melatih model pakai kode lo dan cuma nyimpen kode buat ngejalanin agent. [Pelajari lebih lanjut tentang Privacy Mode](https://www.cursor.com/privacy-overview).

Hal yang perlu lo tahu:

1. Kasih hak akses read-write ke app GitHub kami untuk repo yang mau lo edit. Ini dipakai buat nge-clone repo dan nge-apply perubahan.
2. Kode lo jalan di infrastruktur AWS kami dalam VM yang terisolasi dan disimpan di disk VM selama agent masih aktif.
3. Agent punya akses internet.
4. Agent otomatis ngejalanin semua perintah terminal, biar bisa iterasi di pengujian. Ini beda dari foreground agent, yang butuh persetujuan user untuk setiap perintah. Auto-run bisa memperkenalkan risiko kebocoran data: penyerang bisa ngejalanin prompt injection, ngejebak agent buat mengunggah kode ke situs berbahaya. Lihat [penjelasan OpenAI tentang risiko prompt injection untuk background agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. Kalau Privacy Mode dimatikan, kami ngumpulin prompt dan environment dev buat ningkatin produk.
6. Kalau lo matiin Privacy Mode saat mulai background agent, lalu lo nyalain lagi di tengah jalan, agent bakal lanjut dengan Privacy Mode nonaktif sampai selesai.

<div id="dashboard-settings">
  ## Pengaturan dashboard
</div>

Admin workspace bisa mengonfigurasi pengaturan tambahan lewat tab Background Agents di dashboard.

<div id="defaults-settings">
  ### Pengaturan Default
</div>

* **Model default** – model yang dipakai saat sebuah run nggak nentuin model. Pilih model apa pun yang mendukung Max Mode.
* **Repositori default** – kalau kosong, agen bakal minta pengguna milih repo. Ngisi repo di sini bikin pengguna bisa lewatin langkah itu.
* **Branch dasar** – branch yang jadi asal fork agen saat bikin pull request. Biarkan kosong untuk pakai branch default repositori.

<div id="security-settings">
  ### Pengaturan Keamanan
</div>

Semua opsi keamanan butuh privilese admin.

* **Pembatasan pengguna** – pilih *Tidak ada* (semua member bisa mulai agen latar belakang) atau *Allow list*. Kalau diset ke *Allow list*, lo nentuin persis siapa aja rekan tim yang boleh bikin agen.
* **Tindak lanjut tim** – kalau aktif, siapa pun di workspace bisa nambah pesan tindak lanjut ke agen yang dimulai orang lain. Matikan untuk ngebates tindak lanjut cuma ke pemilik agen dan admin.
* **Tampilkan ringkasan agen** – ngatur apakah Cursor nampilin gambar file-diff dan potongan kode agen. Nonaktifkan ini kalau lo nggak mau nge-ekspose path file atau kode di sidebar.
* **Tampilkan ringkasan agen di kanal eksternal** – memperluas toggle sebelumnya ke Slack atau kanal eksternal apa pun yang udah lo sambungin.

Perubahan kesimpen instan dan langsung ngefek ke agen baru.



# Tambahkan Tindak Lanjut
Source: https://docs.cursor.com/id/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
Kirim instruksi tambahan ke agen latar belakang yang sedang berjalan.




# Percakapan Agen
Source: https://docs.cursor.com/id/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
Ambil riwayat percakapan dari agen latar.

Kalau agen latar sudah dihapus, kamu nggak bisa lagi mengakses percakapannya.



# Status Agen
Source: https://docs.cursor.com/id/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
Dapatkan status dan hasil saat ini dari agen latar belakang tertentu.




# Informasi Kunci API
Source: https://docs.cursor.com/id/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
Mengambil metadata tentang kunci API yang digunakan untuk autentikasi.




# Hapus Agen
Source: https://docs.cursor.com/id/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
Hapus agen latar belakang beserta sumber daya terkait secara permanen.




# Meluncurkan Agent
Source: https://docs.cursor.com/id/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
Mulai agent latar belakang baru untuk bekerja di repositorimu.




# Daftar Agen
Source: https://docs.cursor.com/id/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
Mengambil daftar berhalaman dari semua agen latar belakang untuk pengguna yang diautentikasi.




# Daftar Model
Source: https://docs.cursor.com/id/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
Ambil daftar model yang direkomendasikan untuk background agent.

Kalau kamu mau menetapkan model background agent saat pembuatan, kamu bisa pakai endpoint ini untuk melihat daftar model yang direkomendasikan.

Dalam kasus itu, kami juga menyarankan menyediakan opsi "Auto", di mana kamu nggak mengirimkan nama model ke endpoint pembuatan,
dan kami akan memilih model yang paling sesuai.



# Daftar Repositori GitHub
Source: https://docs.cursor.com/id/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Ambil daftar repositori GitHub yang bisa diakses oleh pengguna terautentikasi.

<Warning>
  **Endpoint ini punya rate limit yang sangat ketat.**

  Batasin request ke **1 / pengguna / menit**, dan **30 / pengguna / jam.**

  Request ini bisa butuh puluhan detik buat ngerespons kalau pengguna punya akses ke banyak repositori.

  Pastikan lo nangani kondisi saat informasi ini nggak tersedia dengan baik.
</Warning>



# Ikhtisar
Source: https://docs.cursor.com/id/background-agent/api/overview

Buat dan kelola agent latar belakang yang bekerja di repositori kamu secara terprogram

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">Beta</Badge>

Background Agents API memungkinkan lo bikin dan ngelola agen coding bertenaga AI secara terprogram yang bekerja secara otonom di repositori lo.
Lo bisa pakai API ini buat otomatis nanggepin masukan pengguna, benerin bug, update dokumentasi, dan banyak lagi!

<Info>
  Background Agents API saat ini masih beta, kami bakal seneng banget nerima masukan dari lo!
</Info>

<div id="key-features">
  ## Fitur utama
</div>

* **Pembuatan kode otonom** - Bikin agen yang bisa paham prompt lo dan ngeubah codebase lo
* **Integrasi repository** - Kerja langsung dengan repository GitHub
* Follow-up prompt - Tambahin instruksi tambahan ke agen yang lagi jalan
* **Harga berbasis penggunaan** - Bayar cuma buat token yang lo pakai
* **Skalabel** - Dukungan sampai 256 agen aktif per API key

<div id="quick-start">
  ## Mulai cepat
</div>

<div id="1-get-your-api-key">
  ### 1. Dapatkan kunci API-mu
</div>

**Buka** [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) untuk membuat kunci API-mu.

<div id="2-start-using-the-api">
  ### 2. Mulai pakai API
</div>

Semua endpoint API relatif terhadap:

```
https://api.cursor.com
```

Lihat [referensi API](/id/background-agent/api/launch-an-agent) buat daftar endpoint yang lengkap.

<div id="authentication">
  ## Autentikasi
</div>

Semua request API perlu autentikasi dengan token Bearer:

```
Authorization: Bearer KUNCI_API_LO
```

Kunci API dibuat di [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations). Kunci ini terikat ke akun lo dan memberi izin untuk membuat serta mengelola agent (tergantung batas paket lo dan akses repositori).

<div id="pricing">
  ## Harga
</div>

API saat ini masih dalam beta dengan harga yang sama seperti Background Agents. Harga bisa berubah seiring pertumbuhan layanan. Lihat [harga Background Agent](/id/account/pricing#background-agent).

<div id="next-steps">
  ## Langkah berikutnya
</div>

* Baca [ikhtisar utama Background Agents](/id/background-agent) untuk memahami environment, permissions, dan workflows.
* Coba Background Agents di [web & mobile](/id/background-agent/web-and-mobile).
* Gabung diskusi di [Discord #background-agent](https://discord.gg/jfgpZtYpmb) atau kirim email ke [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com).



# Webhooks
Source: https://docs.cursor.com/id/background-agent/api/webhooks

Dapatkan notifikasi real-time tentang perubahan status agen latar belakang

<div id="webhooks">
  # Webhooks
</div>

Saat bikin agent dengan URL webhook, Cursor bakal ngirim request HTTP POST buat ngasih tahu perubahan status. Saat ini, cuma event `statusChange` yang didukung, khususnya ketika agent masuk ke state `ERROR` atau `FINISHED`.

<div id="webhook-verification">
  ## Verifikasi webhook
</div>

Biar yakin request webhook benar-benar dari Cursor, verifikasi signature yang disertakan di setiap request:

<div id="headers">
  ### Headers
</div>

Setiap request webhook menyertakan header berikut:

* **`X-Webhook-Signature`** – Berisi signature HMAC-SHA256 dengan format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Identifier unik untuk delivery ini (berguna buat logging)
* **`X-Webhook-Event`** – Jenis event (saat ini hanya `statusChange`)
* **`User-Agent`** – Selalu di-set ke `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Verifikasi signature
</div>

Buat verifikasi signature webhook, hitung signature yang diharapkan lalu bandingkan dengan signature yang diterima:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' + 
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Selalu gunakan body request mentah (sebelum pemrosesan atau parsing apa pun) saat menghitung signature.

<div id="payload-format">
  ## Format payload
</div>

Payload webhook dikirim dalam bentuk JSON dengan struktur berikut:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Menambahkan README.md berisi panduan instalasi"
}
```

Perlu dicatat, beberapa field itu opsional dan cuma bakal disertakan kalau tersedia.

<div id="best-practices">
  ## Praktik terbaik
</div>

* **Verifikasi signature** – Selalu verifikasi signature webhook buat memastikan permintaan itu dari Cursor
* **Tangani retry** – Webhook bisa dicoba ulang kalau endpoint kamu ngembaliin status code error
* **Balas cepat** – Balikin status code 2xx secepat mungkin
* **Pakai HTTPS** – Selalu pakai URL HTTPS buat endpoint webhook di production
* **Simpan payload mentah** – Simpan payload webhook mentah buat debugging dan verifikasi ke depannya



# Web & Mobile
Source: https://docs.cursor.com/id/background-agent/web-and-mobile

Jalankan agen coding dari perangkat apa pun dengan handoff mulus ke desktop

<div id="overview">
  ## Gambaran Umum
</div>

Agent Cursor di web menghadirkan asisten coding yang powerful ke setiap perangkat. Baik lagi pakai HP sambil jalan, atau kerja di browser, sekarang kamu bisa ngejalanin agent coding powerfull yang bekerja di latar belakang.
Begitu selesai, lanjutkan hasil kerja mereka di Cursor, review dan merge perubahan, atau bagikan tautan ke tim buat kolaborasi.

Mulai di [cursor.com/agents](https://cursor.com/agents).

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Antarmuka agent web Cursor" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## Memulai
</div>

<div id="quick-setup">
  ### Penyiapan cepat
</div>

1. **Kunjungi web app**: Buka [cursor.com/agents](https://cursor.com/agents) di perangkat apa pun
2. **Masuk**: Login dengan akun Cursor
3. **Hubungkan GitHub**: Tautkan akun GitHub buat akses repositori
4. **Mulai agent pertamamu**: Ketik tugas dan lihat agent mulai bekerja

<div id="mobile-installation">
  ### Instalasi mobile
</div>

Biar pengalaman mobile maksimal, install Cursor sebagai Progressive Web App (PWA):

* **iOS**: Buka [cursor.com/agents](https://cursor.com/agents) di Safari, ketuk tombol bagikan, lalu "Add to Home Screen"
* **Android**: Buka URL di Chrome, ketuk menu, lalu "Add to Home Screen" atau "Install App"

<Tip>
  Menginstal sebagai PWA memberikan pengalaman mirip native dengan: - Antarmuka layar penuh - Waktu mulai lebih cepat - Ikon app di layar beranda
</Tip>

<div id="working-across-devices">
  ## Bekerja lintas perangkat
</div>

Web dan Mobile Agent dirancang buat nyatu sama alur kerja desktop lo; klik "Open in Cursor" buat nerusin kerja agent di IDE lo.

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Review dan handoff" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### Kolaborasi tim
</div>

* **Akses bersama**: Share tautan ke anggota tim buat kolaborasi di run agent.
* **Proses review**: Kolaborator bisa nge-review diff dan ngasih feedback.
* **Manajemen pull request**: Bikin, review, dan merge pull request langsung dari antarmuka web.

<div id="slack-integration">
  ### Integrasi Slack
</div>

Trigger agent langsung dari Slack dengan nyebut `@Cursor`, dan pas mulai agent dari web atau mobile, pilih buat nerima notifikasi Slack setelah selesai.

<Card title="Pakai Cursor di Slack" icon="slack" href="/id/slack">
  Pelajari lebih lanjut soal nyetel dan pakai integrasi Slack, termasuk
  nge-trigger agent dan nerima notifikasi.
</Card>

<div id="pricing">
  ## Harga
</div>

Agen web dan mobile pakai model harga yang sama seperti Background Agents.

Pelajari lebih lanjut tentang [harga Background Agent](/id/account/pricing#background-agent).

<div id="troubleshooting">
  ## Pemecahan masalah
</div>

<AccordionGroup>
  <Accordion title="Agent runs are not starting">
    * Pastikan lo udah login dan udah nyambungin akun GitHub lo. - Cek
      kalau lo punya permission repository yang diperlukan - Lo juga perlu
      ada di Pro Trial atau paket berbayar dengan usage-based pricing diaktifin. Buat ngaktifin
      usage-based pricing, buka tab settings di
      [Dashboard](https://www.cursor.com/dashboard?tab=settings).
  </Accordion>

  <Accordion title="Can't see agent runs on mobile">
    Coba refresh halaman atau bersihin cache browser. Pastikan lo pakai
    akun yang sama di semua perangkat.
  </Accordion>

  <Accordion title="Slack integration not working">
    Pastikan admin workspace lo udah install app Cursor Slack dan
    lo punya permission yang sesuai.
  </Accordion>
</AccordionGroup>



# Bugbot
Source: https://docs.cursor.com/id/bugbot

Tinjauan kode AI untuk pull request

Bugbot meninjau pull request dan mengidentifikasi bug, isu keamanan, dan masalah kualitas kode.

<Tip>
  Bugbot punya paket gratis: setiap user dapat jatah tinjauan PR gratis tiap bulan. Saat mencapai batas, tinjauan akan dijeda sampai siklus penagihan berikutnya. Lo bisa upgrade kapan aja ke uji coba Pro gratis 14 hari untuk tinjauan tanpa batas (dengan guardrail anti-penyalahgunaan standar).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot ninggalin komentar di PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## Cara kerjanya
</div>

Bugbot menganalisis diff PR dan meninggalkan komentar berisi penjelasan serta saran perbaikan. Ini berjalan otomatis di setiap pembaruan PR atau bisa dijalankan manual saat dipicu.

* Menjalankan **review otomatis** di setiap pembaruan PR
* **Pemicu manual** dengan komentar `cursor review` atau `bugbot run` di PR mana pun
* Tautan **Fix in Cursor** membuka issue langsung di Cursor
* Tautan **Fix in Web** membuka issue langsung di [cursor.com/agents](https://cursor.com/agents)

<div id="setup">
  ## Setup
</div>

Butuh akses admin Cursor dan admin untuk organisasi GitHub.

1. Buka [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Buka tab Bugbot
3. Klik `Connect GitHub` (atau `Manage Connections` kalau sudah terhubung)
4. Ikuti alur instalasi GitHub
5. Balik ke dashboard untuk mengaktifkan Bugbot di repositori tertentu

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Pengaturan Bugbot di GitHub" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## Konfigurasi
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Pengaturan repositori

    Aktifkan atau nonaktifkan Bugbot per repositori dari daftar instalasi lo. Bugbot cuma jalan di PR yang lo bikin.

    ### Pengaturan personal

    * Jalan **hanya kalau disebut** dengan komentar `cursor review` atau `bugbot run`
    * Jalan **hanya sekali** per PR, ngelewatin commit berikutnya
  </Tab>

  <Tab title="Team">
    ### Pengaturan repositori

    Admin tim bisa ngaktifin Bugbot per repositori, nyetel allow/deny list buat reviewer, dan ngatur:

    * Jalan **hanya sekali** per PR per instalasi, ngelewatin commit berikutnya
    * **Nonaktifkan inline review** biar Bugbot gak ninggalin komentar langsung di baris kode

    Bugbot jalan buat semua kontributor di repositori yang diaktifkan, terlepas dari keanggotaan tim.

    ### Pengaturan personal

    Anggota tim bisa override pengaturan buat PR mereka sendiri:

    * Jalan **hanya kalau disebut** dengan komentar `cursor review` atau `bugbot run`
    * Jalan **hanya sekali** per PR, ngelewatin commit berikutnya
    * **Aktifkan review di draft PR** buat nyertain draft pull request dalam review otomatis
  </Tab>
</Tabs>

<div id="analytics">
  ### Analitik
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Dasbor Bugbot" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Aturan
</div>

Buat file `.cursor/BUGBOT.md` untuk ngasih konteks spesifik proyek buat review. Bugbot selalu nyertakan file `.cursor/BUGBOT.md` di root dan file tambahan apa pun yang ketemu saat menelusuri naik dari file yang diubah.

```
project/
  .cursor/BUGBOT.md          # Selalu disertakan (aturan tingkat proyek)
  backend/
    .cursor/BUGBOT.md        # Disertakan saat meninjau file backend
    api/
      .cursor/BUGBOT.md      # Disertakan saat meninjau file API
  frontend/
    .cursor/BUGBOT.md        # Disertakan saat meninjau file frontend
```

<AccordionGroup>
  <Accordion title="Contoh .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Pedoman peninjauan proyek

    ## Fokus keamanan

    - Validasi input pengguna di endpoint API
    - Periksa kerentanan SQL injection dalam kueri database
    - Pastikan autentikasi yang benar pada rute yang dilindungi

    ## Pola arsitektur

    - Gunakan dependency injection untuk layanan
    - Ikuti pola repository untuk akses data
    - Terapkan penanganan error yang tepat dengan kelas error kustom

    ## Masalah umum

    - Kebocoran memori di komponen React (cek cleanup di useEffect)
    - Tidak ada error boundary di komponen UI
    - Konvensi penamaan tidak konsisten (gunakan camelCase untuk fungsi)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Harga
</div>

Bugbot menawarkan dua paket: **Gratis** dan **Pro**.

<div id="free-tier">
  ### Paket gratis
</div>

Setiap user dapat jatah terbatas untuk review PR gratis tiap bulan. Buat tim, tiap anggota tim punya jatah review gratisnya sendiri. Begitu nyentuh batas, review bakal ke-pause sampai siklus penagihan berikutnya. Kamu bisa upgrade kapan aja ke uji coba Pro 14 hari gratis buat review tanpa batas.

<div id="pro-tier">
  ### Paket Pro
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Tarif tetap

    \$40 per bulan untuk review Bugbot tanpa batas pada hingga 200 PR per bulan di semua repositori.

    ### Memulai

    Berlangganan lewat pengaturan akun.
  </Tab>

  <Tab title="Teams">
    ### Penagihan per pengguna

    Tim membayar \$40 per pengguna per bulan untuk review tanpa batas.

    Kami menganggap pengguna sebagai seseorang yang membuat PR yang direview oleh Bugbot dalam satu bulan.

    Semua lisensi dilepas di awal setiap siklus penagihan, dan akan dialokasikan berdasarkan urutan pendaftaran. Kalau seorang pengguna nggak membuat PR apa pun yang direview oleh Bugbot dalam satu bulan, kursi tersebut bisa dipakai oleh pengguna lain.

    ### Batas kursi

    Admin tim bisa menetapkan jumlah maksimum kursi Bugbot per bulan untuk mengontrol biaya.

    ### Memulai

    Berlangganan lewat dasbor tim untuk mengaktifkan penagihan.

    ### Pembatasan penyalahgunaan

    Untuk mencegah penyalahgunaan, kami punya batas gabungan 200 pull request per bulan untuk setiap lisensi Bugbot. Kalau kamu butuh lebih dari 200 pull request per bulan, hubungi kami di [hi@cursor.com](mailto:hi@cursor.com) dan kami dengan senang hati bakal bantu.

    Misalnya, kalau tim kamu punya 100 pengguna, organisasi kamu awalnya bisa mereview 20.000 pull request per bulan. Kalau kamu mencapai batas itu secara natural, silakan hubungi kami dan kami dengan senang hati akan menaikkan batasnya.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

Kalau Bugbot nggak jalan:

1. **Aktifin mode verbose** dengan nge-comment `cursor review verbose=true` atau `bugbot run verbose=true` buat log detail dan request ID
2. **Cek permissions** buat mastihin Bugbot punya akses ke repository
3. **Cek instalasi** buat mastihin GitHub app ke-install dan aktif

Sertakan request ID dari mode verbose waktu ngelaporin masalah.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah Bugbot sesuai dengan mode privasi?">
    Ya, Bugbot mengikuti kepatuhan privasi yang sama seperti Cursor dan memproses data dengan cara yang sama seperti permintaan Cursor lainnya.
  </Accordion>

  <Accordion title="Apa yang terjadi saat aku mencapai batas paket gratis?">
    Saat kamu mencapai batas paket gratis bulanan, peninjauan Bugbot akan dijeda sampai siklus penagihan berikutnya. Kamu bisa upgrade ke uji coba Pro gratis 14 hari untuk peninjauan tanpa batas (dengan perlindungan penyalahgunaan standar).
  </Accordion>
</AccordionGroup>

```
```



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



# Perbaiki Kegagalan CI
Source: https://docs.cursor.com/id/cli/cookbook/fix-ci

Perbaiki masalah CI untuk sebuah repositori dengan Cursor CLI di GitHub Actions

Perbaiki kegagalan CI menggunakan Cursor CLI di GitHub Actions. Workflow ini menganalisis kegagalan, melakukan perbaikan terarah, dan membuat branch perbaikan dengan tautan PR quick-create.

Workflow ini memantau workflow tertentu berdasarkan nama. Perbarui daftar `workflows` agar sesuai dengan nama workflow CI yang sebenarnya.

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
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

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Audit Secret
Source: https://docs.cursor.com/id/cli/cookbook/secret-audit

Audit secret untuk sebuah repository menggunakan Cursor CLI di GitHub Actions

Audit repository-mu untuk kerentanan keamanan dan kebocoran secret pakai Cursor CLI. Workflow ini memindai potensi secret, mendeteksi pola workflow berisiko, dan mengusulkan perbaikan keamanan.

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
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

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Translate Keys
Source: https://docs.cursor.com/id/cli/cookbook/translate-keys

Terjemahkan key untuk repositori dengan Cursor CLI di GitHub Actions

Kelola key terjemahan untuk internasionalisasi menggunakan Cursor CLI. Workflow ini mendeteksi key i18n baru atau yang berubah di pull request dan mengisi terjemahan yang belum ada tanpa menimpa terjemahan yang sudah ada.

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
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

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



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



# Menggunakan Headless CLI
Source: https://docs.cursor.com/id/cli/headless

Pelajari cara menulis skrip menggunakan Cursor CLI untuk analisis kode, pembuatan, dan modifikasi otomatis

Pakai Cursor CLI di skrip dan alur otomatis buat analisis kode, pembuatan, dan refactoring.

<div id="how-it-works">
  ## Cara kerjanya
</div>

Gunakan [print mode](/id/cli/using#non-interactive-mode) (`-p, --print`) untuk skrip non-interaktif dan otomatisasi.

<div id="file-modification-in-scripts">
  ### Modifikasi file di skrip
</div>

Padukan `--print` dengan `--force` untuk mengubah file di skrip:

```bash  theme={null}

# Aktifkan modifikasi file dalam mode cetak
cursor-agent -p --force "Refactor kode ini agar menggunakan sintaks ES6+ modern"


# Tanpa --force, perubahan hanya diusulkan, tidak diterapkan
cursor-agent -p "Tambahkan komentar JSDoc ke file ini"  # Tidak akan memodifikasi file


# Pemrosesan batch dengan perubahan file sesungguhnya
find src/ -name "*.js" | while read file; do
  cursor-agent -p --force "Tambahkan komentar JSDoc yang komprehensif ke $file"
done
```

<Warning>
  Flag `--force` memungkinkan agen melakukan perubahan file secara langsung tanpa konfirmasi
</Warning>

<div id="setup">
  ## Penyiapan
</div>

Lihat [Instalasi](/id/cli/installation) dan [Autentikasi](/id/cli/reference/authentication) untuk detail penyiapan lengkap.

```bash  theme={null}

# Instal Cursor CLI
curl https://cursor.com/install -fsS | bash


# Atur kunci API untuk skrip  
export CURSOR_API_KEY=your_api_key_here
cursor-agent -p "Analisis kode ini"
```

<div id="example-scripts">
  ## Contoh skrip
</div>

Gunakan format output yang berbeda untuk kebutuhan skrip yang berbeda. Lihat [Format output](/id/cli/reference/output-format) untuk detailnya.

<div id="searching-the-codebase">
  ### Menelusuri codebase
</div>

Gunakan `--output-format text` untuk respons yang mudah dibaca:

```bash  theme={null}
#!/bin/bash

# Pertanyaan kodebase sederhana

cursor-agent -p --output-format text "Apa yang dilakukan kodebase ini?"
```

<div id="automated-code-review">
  ### Tinjauan kode otomatis
</div>

Pakai `--output-format json` buat analisis terstruktur:

```bash  theme={null}
#!/bin/bash

# simple-code-review.sh - Skrip peninjauan kode dasar

echo "Memulai peninjauan kode..."


# Meninjau perubahan terbaru
cursor-agent -p --force --output-format text \
  "Tinjau perubahan kode terbaru dan berikan feedback tentang:
  - Kualitas dan keterbacaan kode  
  - Potensi bug atau masalah
  - Pertimbangan keamanan
  - Kepatuhan terhadap praktik terbaik

  Berikan saran spesifik untuk perbaikan dan tulis ke review.txt"

if [ $? -eq 0 ]; then
  echo "✅ Peninjauan kode berhasil diselesaikan"
else
  echo "❌ Peninjauan kode gagal"
  exit 1
fi
```

<div id="real-time-progress-tracking">
  ### Pelacakan progres waktu nyata
</div>

Gunakan `--output-format stream-json` untuk melacak progres secara waktu nyata:

```bash  theme={null}
#!/bin/bash

# stream-progress.sh - Lacak progres secara real-time

echo "🚀 Memulai pemrosesan stream..."


# Lacak progres secara real-time
accumulated_text=""
tool_count=0
start_time=$(date +%s)

cursor-agent -p --force --output-format stream-json \
  "Analisis struktur proyek ini dan buat ringkasan di analysis.txt" | \
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 Memakai model: $model"
        fi
        ;;
        
      "assistant")
        # Akumulasi delta teks streaming
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        
        # Tampilkan progres secara langsung
        printf "\r📝 Menghasilkan: %d karakter" ${#accumulated_text}
        ;;
        
      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))
          
          # Ekstrak informasi alat
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 Alat #$tool_count: Membuat $path"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 Alat #$tool_count: Membaca $path"
          fi
          
        elif [ "$subtype" = "completed" ]; then
          # Ekstrak dan tampilkan hasil alat
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ Membuat $lines baris ($size byte)"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ Membaca $lines baris"
          fi
        fi
        ;;
        
      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))
        
        echo -e "\n\n🎯 Selesai dalam ${duration}ms (${total_time}s total)"
        echo "📊 Statistik akhir: $tool_count alat, ${#accumulated_text} karakter dihasilkan"
        ;;
    esac
  done
```



# Instalasi
Source: https://docs.cursor.com/id/cli/installation

Menginstal dan memperbarui Cursor CLI

<div id="installation">
  ## Instalasi
</div>

<div id="macos-linux-and-windows-wsl">
  ### macOS, Linux, dan Windows (WSL)
</div>

Instal CLI Cursor dengan satu perintah:

```bash  theme={null}
curl https://cursor.com/install -fsS | bash
```

<div id="verification">
  ### Verifikasi
</div>

Setelah instalasi, pastikan Cursor CLI berfungsi dengan benar:

```bash  theme={null}
cursor-agent --version
```

<div id="post-installation-setup">
  ## Penyiapan setelah instalasi
</div>

1. **Tambah \~/.local/bin ke PATH lo:**

   Untuk bash:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   Untuk zsh:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Mulai pakai Cursor Agent:**
   ```bash  theme={null}
   cursor-agent
   ```

<div id="updates">
  ## Pembaruan
</div>

Secara default, Cursor CLI bakal coba memperbarui otomatis biar kamu selalu pakai versi terbaru.

Untuk memperbarui Cursor CLI ke versi terbaru secara manual:

```bash  theme={null}
cursor-agent update

# atau 
cursor-agent upgrade
```

Kedua perintah akan mengupdate Cursor Agent ke versi terbaru.



# MCP
Source: https://docs.cursor.com/id/cli/mcp

Gunakan server MCP dengan cursor-agent untuk terhubung ke alat eksternal dan sumber data

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="overview">
  ## Ikhtisar
</div>

CLI Cursor mendukung server [Model Context Protocol (MCP)](/id/context/mcp), yang bikin lo bisa nyambungin tool eksternal dan sumber data ke `cursor-agent`. **MCP di CLI pakai konfigurasi yang sama kayak editor** — server MCP apa pun yang udah lo set bakal jalan mulus di keduanya.

<Card title="Pelajari tentang MCP" icon="link" href="/id/context/mcp">
  Baru kenal MCP? Baca panduan lengkap soal konfigurasi, autentikasi, dan server yang tersedia
</Card>

<div id="cli-commands">
  ## Perintah CLI
</div>

Gunakan perintah `cursor-agent mcp` buat ngelola server MCP:

<div id="list-configured-servers">
  ### Daftar server yang tersetup
</div>

Lihat semua server MCP yang tersetup dan statusnya saat ini:

```bash  theme={null}
cursor-agent mcp list
```

Ini menampilkan:

* Nama server dan pengenal
* Status koneksi (terhubung/terputus)
* Sumber konfigurasi (proyek atau global)
* Metode transport (stdio, HTTP, SSE)

<div id="list-available-tools">
  ### Lihat daftar tool yang tersedia
</div>

Lihat tool yang disediakan oleh server MCP tertentu:

```bash  theme={null}
cursor-agent mcp list-tools <identifier>
```

Ini menampilkan:

* Nama dan deskripsi tool
* Parameter wajib dan opsional
* Jenis parameter dan batasannya

<div id="login-to-mcp-server">
  ### Login ke server MCP
</div>

Lakukan autentikasi ke server MCP yang dikonfigurasi di `mcp.json`:

```bash  theme={null}
cursor-agent mcp login <identifier>
```

<div id="disable-mcp-server">
  ### Nonaktifkan server MCP
</div>

Hapus server MCP dari daftar lokal yang disetujui:

```bash  theme={null}
cursor-agent mcp disable <identifier>
```

<div id="using-mcp-with-agent">
  ## Menggunakan MCP bareng Agent
</div>

Begitu lo udah ngonfigurasi server MCP (lihat [panduan MCP utama](/id/context/mcp) buat setup), `cursor-agent` bakal otomatis nemuin dan make tools yang tersedia kalau relevan sama permintaan lo.

```bash  theme={null}

# Cek server MCP yang tersedia
cursor-agent mcp list


# Lihat alat apa yang disediakan oleh server tertentu
cursor-agent mcp list-tools playwright


# Gunakan cursor-agent - otomatis memakai alat MCP saat membantu
cursor-agent --prompt "Buka google.com dan ambil tangkapan layar halaman pencarian"
```

CLI mengikuti urutan prioritas konfigurasi yang sama seperti editor (proyek → global → bertingkat), secara otomatis mendeteksi konfigurasi dari direktori induk.

<div id="related">
  ## Terkait
</div>

<CardGroup cols={2}>
  <Card title="MCP Overview" icon="link" href="/id/context/mcp">
    Panduan MCP lengkap: penyiapan, konfigurasi, dan autentikasi
  </Card>

  <Card title="Available MCP Tools" icon="table" href="/id/tools">
    Jelajahi server MCP siap pakai yang bisa kamu gunakan
  </Card>
</CardGroup>



# Cursor CLI
Source: https://docs.cursor.com/id/cli/overview

Mulai pakai Cursor CLI buat ngoding di terminal

Cursor CLI bikin lo bisa berinteraksi sama agen AI langsung dari terminal buat nulis, nge-review, dan ngubah kode. Mau pakai antarmuka terminal interaktif atau output non-interaktif buat otomatisasi di script dan pipeline CI, CLI ngasih bantuan ngoding yang powerful tepat di tempat lo kerja.

```bash  theme={null}

# Instal
curl https://cursor.com/install -fsS | bash


# Jalankan sesi interaktif
cursor-agent
```

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/cli-overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b323547dd61e985df8c0d6179c1492bd" autoPlay loop muted playsInline controls data-path="images/cli/cli-overview.mp4" />
</Frame>

<Info>
  Cursor CLI saat ini masih beta, kami sangat pengin dengerin feedback kamu!
</Info>

<div id="interactive-mode">
  ### Mode interaktif
</div>

Mulai sesi percakapan bareng agent buat jelasin tujuan kamu, nge-review perubahan yang diusulin, dan nyetujuin command:

```bash  theme={null}

# Mulai sesi interaktif
cursor-agent


# Mulai dengan prompt awal
cursor-agent "refactor modul auth agar menggunakan token JWT"
```

<div id="non-interactive-mode">
  ### Mode non-interaktif
</div>

Gunakan mode print untuk skenario non-interaktif seperti skrip, pipeline CI, atau automasi:

```bash  theme={null}

# Jalankan dengan prompt dan model tertentu
cursor-agent -p "temukan dan perbaiki masalah performa" --model "gpt-5"


# Sertakan perubahan git untuk ditinjau
cursor-agent -p "tinjau perubahan ini untuk isu keamanan" --output-format text
```

<div id="sessions">
  ### Sesi
</div>

Lanjutkan percakapan sebelumnya untuk mempertahankan konteks di berbagai interaksi:

```bash  theme={null}

# Daftarkan semua obrolan sebelumnya
cursor-agent ls


# Lanjutkan percakapan terbaru  
cursor-agent resume


# Lanjutkan percakapan tertentu
cursor-agent --resume="chat-id-here"
```



# Autentikasi
Source: https://docs.cursor.com/id/cli/reference/authentication

Autentikasi Cursor CLI lewat alur browser atau kunci API

Cursor CLI mendukung dua metode autentikasi: login via browser (disarankan) dan kunci API.

<div id="browser-authentication-recommended">
  ## Autentikasi lewat browser (disarankan)
</div>

Pakai flow via browser buat pengalaman autentikasi yang paling mudah:

```bash  theme={null}

# Masuk lewat alur browser
cursor-agent login


# Cek status autentikasi
cursor-agent status


# Keluar dan hapus autentikasi yang tersimpan
cursor-agent logout
```

Perintah login bakal buka browser default kamu dan minta kamu buat autentikasi pake akun Cursor. Setelah selesai, kredensial kamu bakal disimpen secara aman di perangkat lokal.

<div id="api-key-authentication">
  ## Otentikasi kunci API
</div>

Untuk otomatisasi, skrip, atau lingkungan CI/CD, pakai otentikasi kunci API:

<div id="step-1-generate-an-api-key">
  ### Langkah 1: Buat kunci API
</div>

Bikin kunci API di dashboard Cursor lo, di Integrations > User API Keys.

<div id="step-2-set-the-api-key">
  ### Langkah 2: Setel kunci API
</div>

Lo bisa nyediain kunci API dengan dua cara:

**Opsi 1: Variabel lingkungan (disarankan)**

```bash  theme={null}
export CURSOR_API_KEY=your_api_key_here
cursor-agent "implement autentikasi pengguna"
```

**Opsi 2: Flag baris perintah**

```bash  theme={null}
cursor-agent --api-key your_api_key_here "implement user authentication"
```

<div id="authentication-status">
  ## Status autentikasi
</div>

Cek status autentikasi kamu saat ini:

```bash  theme={null}
cursor-agent status
```

Perintah ini akan menampilkan:

* Apakah kamu sudah diautentikasi
* Informasi akun kamu
* Konfigurasi endpoint saat ini

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

* **Error "Not authenticated":** Jalanin `cursor-agent login` atau pastiin API key lo udah diset dengan bener
* **Error sertifikat SSL:** Pakai flag `--insecure` buat environment pengembangan
* **Masalah endpoint:** Pakai flag `--endpoint` buat nentuin custom API endpoint



# Konfigurasi
Source: https://docs.cursor.com/id/cli/reference/configuration

Referensi konfigurasi Agent CLI untuk cli-config.json

Atur Agent CLI menggunakan file `cli-config.json`.

<div id="file-location">
  ## Lokasi file
</div>

<div class="full-width-table">
  | Tipe   | Platform    | Path                                       |
  | :----- | :---------- | :----------------------------------------- |
  | Global | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Proyek | Semua       | `<project>/.cursor/cli.json`               |
</div>

<Note>Cuma izin yang bisa dikonfigurasi di level proyek. Semua pengaturan CLI lainnya harus diatur secara global.</Note>

Override dengan variabel lingkungan:

* **`CURSOR_CONFIG_DIR`**: path direktori kustom
* **`XDG_CONFIG_HOME`** (Linux/BSD): memakai `$XDG_CONFIG_HOME/cursor/cli-config.json`

<div id="schema">
  ## Skema
</div>

<div id="required-fields">
  ### Field wajib
</div>

<div class="full-width-table">
  | Field               | Type      | Deskripsi                                                                   |
  | :------------------ | :-------- | :-------------------------------------------------------------------------- |
  | `version`           | number    | Versi skema konfigurasi (saat ini: `1`)                                     |
  | `editor.vimMode`    | boolean   | Mengaktifkan keybinding Vim (default: `false`)                              |
  | `permissions.allow` | string\[] | Operasi yang diizinkan (lihat [Permissions](/id/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Operasi yang dilarang (lihat [Permissions](/id/cli/reference/permissions))  |
</div>

<div id="optional-fields">
  ### Field opsional
</div>

<div class="full-width-table">
  | Field                    | Type    | Deskripsi                             |
  | :----------------------- | :------ | :------------------------------------ |
  | `model`                  | object  | Konfigurasi model yang dipilih        |
  | `hasChangedDefaultModel` | boolean | Flag override model yang dikelola CLI |
</div>

<div id="examples">
  ## Contoh
</div>

<div id="minimal-config">
  ### Konfigurasi minimal
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="enable-vim-mode">
  ### Aktifkan Mode Vim
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

<div id="configure-permissions">
  ### Konfigurasikan izin
</div>

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

Lihat [Permissions](/id/cli/reference/permissions) untuk jenis izin yang tersedia dan contohnya.

<div id="troubleshooting">
  ## Pemecahan Masalah
</div>

**Error konfigurasi**: Pindahin file-nya dulu ke lokasi lain, lalu restart:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Perubahan nggak tersimpan**: Pastikan JSON valid dan punya izin tulis. Beberapa field dikelola CLI dan bisa ke-overwrite.

<div id="notes">
  ## Catatan
</div>

* Format JSON murni (tanpa komentar)
* CLI melakukan perbaikan otomatis untuk field yang hilang
* File yang rusak dicadangkan sebagai `.bad` dan dibuat ulang
* Entri izin harus berupa string yang persis sama (lihat [Permissions](/id/cli/reference/permissions) untuk detail)



# Format output
Source: https://docs.cursor.com/id/cli/reference/output-format

Skema output untuk format teks, JSON, dan stream-JSON

Cursor Agent CLI menyediakan beberapa format output melalui opsi `--output-format` saat digabungkan dengan `--print`. Format ini mencakup format terstruktur untuk penggunaan terprogram (`json`, `stream-json`) dan format teks yang lebih sederhana untuk pelacakan progres yang mudah dibaca manusia.

<Note>
  Nilai default `--output-format` adalah `stream-json`. Opsi ini hanya berlaku saat melakukan print (`--print`) atau ketika mode print diinferensikan (stdout non-TTY atau stdin yang dipipe).
</Note>

<div id="json-format">
  ## Format JSON
</div>

Format output `json` menghasilkan satu objek JSON (diikuti baris baru) saat run selesai dengan sukses. Delta dan event tool tidak dikeluarkan; teks digabungkan ke hasil akhir.

Jika gagal, proses keluar dengan kode non-zero dan menulis pesan error ke stderr. Tidak ada objek JSON yang terformat dengan benar yang dikeluarkan dalam kasus kegagalan.

<div id="success-response">
  ### Respons sukses
</div>

Saat berhasil, CLI mengeluarkan objek JSON dengan struktur berikut:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<teks lengkap asisten>",
  "session_id": "<uuid>",
  "request_id": "<id permintaan (opsional)>"
}
```

<div class="full-width-table">
  | Field             | Deskripsi                                                                 |
  | ----------------- | ------------------------------------------------------------------------- |
  | `type`            | Selalu `"result"` untuk hasil di terminal                                 |
  | `subtype`         | Selalu `"success"` untuk penyelesaian yang sukses                         |
  | `is_error`        | Selalu `false` untuk respons yang sukses                                  |
  | `duration_ms`     | Total waktu eksekusi dalam milidetik                                      |
  | `duration_api_ms` | Waktu permintaan API dalam milidetik (saat ini sama dengan `duration_ms`) |
  | `result`          | Teks respons asisten lengkap (penggabungan semua delta teks)              |
  | `session_id`      | Identifier sesi unik                                                      |
  | `request_id`      | Identifier permintaan opsional (bisa dihilangkan)                         |
</div>

<div id="stream-json-format">
  ## Format JSON stream
</div>

Format output `stream-json` menghasilkan JSON yang dipisahkan baris baru (NDJSON). Setiap baris berisi satu objek JSON yang merepresentasikan event real-time selama eksekusi.

Stream berakhir dengan event terminal `result` saat berhasil. Jika gagal, proses keluar dengan kode non-nol dan stream bisa berakhir lebih awal tanpa event terminal; pesan error ditulis ke stderr.

<div id="event-types">
  ### Jenis event
</div>

<div id="system-initialization">
  #### Inisialisasi sistem
</div>

Dikirim sekali di awal setiap sesi:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/absolute/path",
  "session_id": "<uuid>",
  "model": "<model display name>",
  "permissionMode": "default"
}
```

<Note>
  Di masa mendatang, bidang seperti `tools` dan `mcp_servers` mungkin akan ditambahkan ke event ini.
</Note>

<div id="user-message">
  #### Pesan pengguna
</div>

Berisi prompt yang dimasukkan pengguna:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Delta teks asisten
</div>

Dipancarkan beberapa kali saat asisten menghasilkan responsnya. Event ini berisi potongan teks bertahap:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<cuplikan delta>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Gabungkan semua nilai `message.content[].text` secara berurutan untuk menyusun ulang respons lengkap asisten.
</Note>

<div id="tool-call-events">
  #### Peristiwa pemanggilan alat
</div>

Pemanggilan alat dilacak dengan peristiwa mulai dan selesai:

**Pemanggilan alat dimulai:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Panggilan alat selesai:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "konten file...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### Jenis pemanggilan tool
</div>

**Tool baca file:**

* **Dimulai**: `tool_call.readToolCall.args` memuat `{ "path": "file.txt" }`
* **Selesai**: `tool_call.readToolCall.result.success` memuat metadata dan konten file

**Tool tulis file:**

* **Dimulai**: `tool_call.writeToolCall.args` memuat `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **Selesai**: `tool_call.writeToolCall.result.success` memuat `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Tool lainnya:**

* Bisa menggunakan struktur `tool_call.function` dengan `{ "name": "tool_name", "arguments": "..." }`

<div id="terminal-result">
  #### Hasil terminal
</div>

Event terakhir yang dipancarkan saat berhasil selesai:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<teks lengkap asisten>",
  "session_id": "<uuid>",
  "request_id": "<opsional id permintaan>"
}
```

<div id="example-sequence">
  ### Contoh urutan
</div>

Berikut adalah urutan NDJSON representatif yang menunjukkan alur kejadian yang khas:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Baca README.md dan buat ringkasan"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Aku akan "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"membaca berkas README.md"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Proyek\n\nIni adalah proyek contoh...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" dan membuat ringkasan"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# Ringkasan README\n\nProyek ini berisi...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# Ringkasan README\n\nProyek ini berisi...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"Aku akan membaca berkas README.md dan membuat ringkasan","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## Format teks
</div>

Format output `text` menyajikan rangkaian tindakan agen yang disederhanakan dan mudah dibaca. Alih-alih event JSON yang detail, format ini menampilkan deskripsi teks ringkas tentang apa yang lagi dilakukan agen secara real-time.

Format ini berguna buat memantau progress agen tanpa overhead parsing data terstruktur, jadi ideal buat logging, debugging, atau pelacakan progress sederhana.

<div id="example-output">
  ### Contoh output
</div>

```
Membaca file
Mengedit file
Menjalankan perintah di terminal
Membuat file baru
```

Setiap aksi muncul di baris baru saat agen mengeksekusinya, memberi umpan balik instan tentang progres agen dalam menyelesaikan tugas.

<div id="implementation-notes">
  ## Catatan implementasi
</div>

* Setiap event dipancarkan sebagai satu baris yang diakhiri dengan `\n`
* Event `thinking` disembunyikan dalam mode cetak dan tidak akan muncul di kedua format output
* Penambahan field dapat terjadi dari waktu ke waktu dengan cara yang kompatibel mundur (konsumen harus mengabaikan field yang tidak dikenal)
* Format stream memberikan pembaruan waktu nyata, sementara format JSON menunggu hingga selesai sebelum mengeluarkan hasil
* Gabungkan semua delta pesan `assistant` untuk merekonstruksi respons lengkap
* ID pemanggilan tool dapat digunakan untuk mengorelasikan event mulai/selesai
* ID sesi tetap konsisten sepanjang satu eksekusi agen



# Parameter
Source: https://docs.cursor.com/id/cli/reference/parameters

Referensi lengkap perintah untuk Cursor Agent CLI

<div id="global-options">
  ## Opsi global
</div>

Opsi global bisa dipakai dengan perintah apa pun:

<div class="full-width-table">
  | Opsi                       | Deskripsi                                                                                                                |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
  | `-v, --version`            | Tampilkan nomor versi                                                                                                    |
  | `-a, --api-key <key>`      | API key untuk autentikasi (juga bisa pakai variabel lingkungan `CURSOR_API_KEY`)                                         |
  | `-p, --print`              | Cetak respons ke konsol (buat skrip atau penggunaan non-interaktif). Punya akses ke semua tool, termasuk write dan bash. |
  | `--output-format <format>` | Format output (hanya berfungsi dengan `--print`): `text`, `json`, atau `stream-json` (default: `stream-json`)            |
  | `-b, --background`         | Mulai dalam mode latar belakang (buka composer picker saat diluncurkan)                                                  |
  | `--fullscreen`             | Aktifkan mode layar penuh                                                                                                |
  | `--resume [chatId]`        | Lanjutkan sesi chat                                                                                                      |
  | `-m, --model <model>`      | Model yang dipakai                                                                                                       |
  | `-f, --force`              | Paksa izinkan perintah kecuali yang secara eksplisit ditolak                                                             |
  | `-h, --help`               | Tampilkan bantuan untuk perintah                                                                                         |
</div>

<div id="commands">
  ## Perintah
</div>

<div class="full-width-table">
  | Perintah          | Deskripsi                                   | Penggunaan                                        |
  | ----------------- | ------------------------------------------- | ------------------------------------------------- |
  | `login`           | Autentikasi dengan Cursor                   | `cursor-agent login`                              |
  | `logout`          | Keluar dan hapus autentikasi yang tersimpan | `cursor-agent logout`                             |
  | `status`          | Cek status autentikasi                      | `cursor-agent status`                             |
  | `mcp`             | Kelola server MCP                           | `cursor-agent mcp`                                |
  | `update\|upgrade` | Perbarui Cursor Agent ke versi terbaru      | `cursor-agent update` atau `cursor-agent upgrade` |
  | `ls`              | Lanjutkan sesi chat                         | `cursor-agent ls`                                 |
  | `resume`          | Lanjutkan sesi chat terbaru                 | `cursor-agent resume`                             |
  | `help [command]`  | Tampilkan bantuan untuk perintah            | `cursor-agent help [command]`                     |
</div>

<Note>
  Kalau nggak ada perintah yang ditentukan, Cursor Agent bakal mulai dalam mode chat interaktif secara default.
</Note>

<div id="mcp">
  ## MCP
</div>

Kelola server MCP yang dikonfigurasi untuk Cursor Agent.

<div class="full-width-table">
  | Subcommand                | Deskripsi                                                              | Penggunaan                                 |
  | ------------------------- | ---------------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | Masuk ke server MCP yang dikonfigurasi di `.cursor/mcp.json`           | `cursor-agent mcp login <identifier>`      |
  | `list`                    | Lihat daftar server MCP yang dikonfigurasi beserta statusnya           | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | Lihat daftar tool yang tersedia dan nama argumennya untuk MCP tertentu | `cursor-agent mcp list-tools <identifier>` |
</div>

Semua perintah MCP mendukung `-h, --help` untuk bantuan khusus perintah.

<div id="arguments">
  ## Argumen
</div>

Saat mulai dalam mode chat (perilaku default), lo bisa ngasih prompt awal:

**Argumen:**

* `prompt` — Prompt awal buat agen

<div id="getting-help">
  ## Mendapatkan bantuan
</div>

Semua perintah mendukung opsi global `-h, --help` untuk menampilkan bantuan khusus untuk perintah tersebut.



# Permissions
Source: https://docs.cursor.com/id/cli/reference/permissions

Jenis izin untuk mengontrol akses agen ke file dan perintah

Atur apa yang boleh dilakukan agen pakai token izin di konfigurasi CLI lo. Izin disetel di `~/.cursor/cli-config.json` (global) atau `<project>/.cursor/cli.json` (spesifik proyek).

<div id="permission-types">
  ## Jenis izin
</div>

<div id="shell-commands">
  ### Perintah shell
</div>

**Format:** `Shell(commandBase)`

Mengontrol akses ke perintah shell. `commandBase` adalah token pertama di baris perintah.

<div class="full-width-table">
  | Contoh       | Deskripsi                                                  |
  | ------------ | ---------------------------------------------------------- |
  | `Shell(ls)`  | Izinkan menjalankan perintah `ls`                          |
  | `Shell(git)` | Izinkan subperintah `git` apa pun                          |
  | `Shell(npm)` | Izinkan perintah pengelola paket npm                       |
  | `Shell(rm)`  | Tolak penghapusan file yang destruktif (umumnya di `deny`) |
</div>

<div id="file-reads">
  ### Pembacaan file
</div>

**Format:** `Read(pathOrGlob)`

Mengontrol akses baca ke file dan direktori. Mendukung pola glob.

<div class="full-width-table">
  | Contoh              | Deskripsi                                 |
  | ------------------- | ----------------------------------------- |
  | `Read(src/**/*.ts)` | Izinkan membaca file TypeScript di `src`  |
  | `Read(**/*.md)`     | Izinkan membaca file Markdown di mana pun |
  | `Read(.env*)`       | Tolak membaca file environment            |
  | `Read(/etc/passwd)` | Tolak membaca file sistem                 |
</div>

<div id="file-writes">
  ### Penulisan file
</div>

**Format:** `Write(pathOrGlob)`

Mengontrol akses tulis ke file dan direktori. Mendukung pola glob. Saat digunakan dalam mode print, `--force` diperlukan untuk menulis file.

<div class="full-width-table">
  | Contoh                | Deskripsi                                      |
  | --------------------- | ---------------------------------------------- |
  | `Write(src/**)`       | Izinkan menulis ke file apa pun di bawah `src` |
  | `Write(package.json)` | Izinkan memodifikasi package.json              |
  | `Write(**/*.key)`     | Tolak menulis file kunci privat                |
  | `Write(**/.env*)`     | Tolak menulis file environment                 |
</div>

<div id="configuration">
  ## Konfigurasi
</div>

Tambah izin ke objek `permissions` di file konfigurasi CLI lo:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

<div id="pattern-matching">
  ## Pencocokan pola
</div>

* Pola glob menggunakan wildcard `**`, `*`, dan `?`
* Path relatif berlaku dalam workspace saat ini
* Path absolut bisa menargetkan file di luar proyek
* Aturan deny memiliki prioritas dibanding aturan allow



# Perintah slash
Source: https://docs.cursor.com/id/cli/reference/slash-commands

Aksi cepat yang tersedia di sesi Cursor CLI

<div class="full-width-table">
  | Command               | Description                                           |
  | --------------------- | ----------------------------------------------------- |
  | `/model <model>`      | Set atau lihat daftar model                           |
  | `/auto-run [state]`   | Toggle auto-run (default) atau set \[on\|off\|status] |
  | `/new-chat`           | Mulai sesi chat baru                                  |
  | `/vim`                | Toggle tombol Vim                                     |
  | `/help [command]`     | Tampilkan bantuan (/help \[cmd])                      |
  | `/feedback <message>` | Kirim feedback ke tim                                 |
  | `/resume <chat>`      | Lanjutkan chat sebelumnya berdasarkan nama folder     |
  | `/copy-req-id`        | Salin ID request terakhir                             |
  | `/logout`             | Sign out dari Cursor                                  |
  | `/quit`               | Keluar                                                |
</div>



# Mode Shell
Source: https://docs.cursor.com/id/cli/shell-mode

Jalanin perintah shell langsung dari CLI tanpa ninggalin percakapan

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Shell Mode ngejalanin perintah shell langsung dari CLI tanpa keluar dari percakapan. Pakai buat perintah cepat yang non-interaktif dengan safety check, dan output-nya bakal ditampilin di percakapan.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

<div id="command-execution">
  ## Eksekusi perintah
</div>

Perintah dijalankan di shell login lo (`$SHELL`) dengan direktori kerja dan environment milik CLI. Rangkaikan perintah buat dijalankan di direktori lain:

```bash  theme={null}
cd subdir && npm test
```

<div id="output">
  ## Output
</div>

<product_visual type="screenshot">
  Output perintah menampilkan header dengan kode keluar (exit code), tampilan stdout/stderr, dan kontrol pemendekan
</product_visual>

Output yang besar dipendekkan secara otomatis, dan proses yang berjalan lama akan di-timeout untuk menjaga performa.

<div id="limitations">
  ## Keterbatasan
</div>

* Perintah akan timeout setelah 30 detik
* Proses jangka panjang, server, dan prompt interaktif tidak didukung
* Gunakan perintah singkat yang non-interaktif untuk hasil terbaik

<div id="permissions">
  ## Permissions
</div>

Perintah bakal diperiksa berdasarkan permissions dan pengaturan tim kamu sebelum dijalankan. Lihat [Permissions](/id/cli/reference/permissions) untuk konfigurasi mendetail.

<product_visual type="screenshot">
  Banner keputusan yang menampilkan opsi persetujuan: Run, Reject/Propose, Add to allowlist, dan Auto-run
</product_visual>

Kebijakan admin bisa memblokir perintah tertentu, dan perintah dengan redirection nggak bisa dimasukkan ke allowlist secara inline.

<div id="usage-guidelines">
  ## Pedoman penggunaan
</div>

Shell Mode cocok untuk pengecekan status, build cepat, operasi file, dan inspeksi environment.

Hindari server yang berjalan lama, aplikasi interaktif, dan perintah yang memerlukan input.

Setiap perintah berjalan secara independen — pakai `cd <dir> && ...` untuk menjalankan perintah di direktori lain.

<div id="troubleshooting">
  ## Pemecahan masalah
</div>

* Kalau perintah ngegantung, batalin dengan <Kbd>Ctrl+C</Kbd> dan tambahin flag non-interaktif
* Kalau diminta izin, setujui sekali atau tambahin ke allowlist pakai <Kbd>Tab</Kbd>
* Kalau output kepotong, pakai <Kbd>Ctrl+O</Kbd> buat nge-expand
* Buat jalanin di direktori lain, pakai `cd <dir> && ...` soalnya perubahan nggak ke-save
* Shell Mode dukung zsh dan bash sesuai variabel `$SHELL` kamu

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apakah `cd` bertahan antar run?">
    Nggak. Tiap perintah jalan sendiri. Pakai `cd <dir> && ...` buat jalanin perintah di direktori yang beda.
  </Accordion>

  <Accordion title="Bisa nggak aku ubah timeout?">
    Nggak. Perintah dibatasi 30 detik dan ini nggak bisa dikonfigurasi.
  </Accordion>

  <Accordion title="Izin dikonfigurasinya di mana?">
    Izin dikelola lewat konfigurasi CLI dan tim. Pakai decision banner buat nambahin perintah ke allowlist.
  </Accordion>

  <Accordion title="Gimana cara keluar dari Shell Mode?">
    Tekan <Kbd>Escape</Kbd> waktu input kosong, <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> pas input kosong, atau <Kbd>Ctrl+C</Kbd> buat nge-clear dan keluar.
  </Accordion>
</AccordionGroup>



# Menggunakan Agent di CLI
Source: https://docs.cursor.com/id/cli/using

Meminta, meninjau, dan beriterasi secara efektif dengan Cursor CLI

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="prompting">
  ## Prompting
</div>

Ngasih tahu intent dengan jelas itu disarankan biar hasilnya maksimal. Misalnya, lo bisa pakai prompt "do not write any code" buat memastikan agent nggak bakal ngedit file apa pun. Ini biasanya membantu waktu ngerencanain task sebelum ngejalaninnya.

Agent saat ini punya tools buat operasi file, pencarian, dan ngejalanin perintah shell. Lebih banyak tools bakal ditambahin, mirip kayak agent di IDE.

<div id="mcp">
  ## MCP
</div>

Agent mendukung [MCP (Model Context Protocol)](/id/tools/mcp) untuk fungsionalitas dan integrasi yang lebih luas. CLI bakal otomatis mendeteksi dan mengikuti file konfigurasi `mcp.json` lo, jadi server dan tool MCP yang sama kayak yang udah lo set di IDE bakal aktif juga.

<div id="rules">
  ## Rules
</div>

Agen CLI mendukung [sistem rules](/id/context/rules) yang sama seperti di IDE. Kamu bisa bikin rules di direktori `.cursor/rules` buat ngasih konteks dan panduan ke agen. Rules ini bakal otomatis dimuat dan diterapkan sesuai konfigurasinya, jadi kamu bisa ngustom perilaku agen buat bagian-bagian tertentu di proyekmu atau tipe file tertentu.

<Note>
  CLI juga baca `AGENTS.md` dan `CLAUDE.md` di root proyek (kalau ada) dan nerapinnya sebagai rules bareng `.cursor/rules`.
</Note>

<div id="working-with-agent">
  ## Bekerja dengan Agent
</div>

<div id="navigation">
  ### Navigasi
</div>

Pesan sebelumnya bisa diakses pakai panah atas (<Kbd>ArrowUp</Kbd>) dan kamu bisa menelusurinya satu per satu.

<div id="review">
  ### Review
</div>

Review perubahan dengan <Kbd>Cmd+R</Kbd>. Tekan <Kbd>i</Kbd> buat nambah instruksi lanjutan. Pakai <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> buat nge-scroll, dan <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> buat pindah file.

<div id="selecting-context">
  ### Memilih konteks
</div>

Pilih file dan folder buat disertakan ke konteks dengan <Kbd>@</Kbd>. Bebasin ruang di jendela konteks dengan menjalankan `/compress`. Lihat [Summarization](/id/agent/chat/summarization) buat detailnya.

<div id="history">
  ## Riwayat
</div>

Lanjutkan dari thread yang sudah ada dengan `--resume [thread id]` untuk memuat konteks sebelumnya.

Untuk melanjutkan percakapan terbaru, gunakan `cursor-agent resume`.

Kamu juga bisa menjalankan `cursor-agent ls` untuk melihat daftar percakapan sebelumnya.

<div id="command-approval">
  ## Persetujuan perintah
</div>

Sebelum ngejalanin perintah di terminal, CLI bakal minta lo buat nyetujuin (<Kbd>y</Kbd>) atau nolak (<Kbd>n</Kbd>) eksekusinya.

<div id="non-interactive-mode">
  ## Mode non-interaktif
</div>

Gunakan `-p` atau `--print` buat jalanin Agent dalam mode non-interaktif. Ini bakal nge-print respons ke konsol.

Dengan mode non-interaktif, lo bisa manggil Agent tanpa interaksi. Ini bikin lo bisa ngintegrasiin Agent ke skrip, pipeline CI, dll.

Lo bisa nggabungin ini dengan `--output-format` buat ngontrol format output. Misalnya, pakai `--output-format json` buat output terstruktur yang lebih gampang di-parse di skrip, atau `--output-format text` buat output teks polos.

<Note>
  Cursor punya akses tulis penuh dalam mode non-interaktif.
</Note>



# Pintasan Keyboard
Source: https://docs.cursor.com/id/configuration/kbd

Pintasan keyboard dan pemetaan tombol di Cursor

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Ikhtisar pintasan keyboard di Cursor. Lihat semua pintasan keyboard dengan menekan <Kbd>Cmd R</Kbd> lalu <Kbd>Cmd S</Kbd> atau dengan membuka command palette <Kbd>Cmd Shift P</Kbd> dan mencari `Keyboard Shortcuts`.

Pelajari lebih lanjut tentang pintasan keyboard di Cursor dengan [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) sebagai acuan dasar untuk keybinding Cursor.

Semua keybinding di Cursor, termasuk fitur khusus Cursor, bisa diubah di pengaturan Keyboard Shortcuts.

<div id="general">
  ## Umum
</div>

<div className="full-width-table equal-table-columns">
  | Pintasan               | Aksi                                            |
  | ---------------------- | ----------------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Alihkan Panel Samping (kecuali terikat ke mode) |
  | <Kbd>Cmd L</Kbd>       | Alihkan Panel Samping (kecuali terikat ke mode) |
  | <Kbd>Cmd E</Kbd>       | Panel kontrol Background Agent                  |
  | <Kbd>Cmd .</Kbd>       | Menu Mode                                       |
  | <Kbd>Cmd /</Kbd>       | Berpindah di antara model AI                    |
  | <Kbd>Cmd Shift J</Kbd> | Pengaturan Cursor                               |
  | <Kbd>Cmd ,</Kbd>       | Pengaturan umum                                 |
  | <Kbd>Cmd Shift P</Kbd> | Palet perintah                                  |
</div>

<div id="chat">
  ## Chat
</div>

Shortcut untuk kotak input chat.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Aksi                                        |
  | ---------------------------------------------------- | ------------------------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (default)                             |
  | <Kbd>Ctrl Return</Kbd>                               | Antrikan pesan                              |
  | <Kbd>Cmd Return</Kbd> when typing                    | Paksa kirim pesan                           |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Batalkan pembuatan                          |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Tambahkan kode yang dipilih sebagai konteks |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Tambahkan isi clipboard sebagai konteks     |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Tambahkan isi clipboard ke kotak input      |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Terima semua perubahan                      |
  | <Kbd>Cmd Backspace</Kbd>                             | Tolak semua perubahan                       |
  | <Kbd>Tab</Kbd>                                       | Pindah ke pesan berikutnya                  |
  | <Kbd>Shift Tab</Kbd>                                 | Pindah ke pesan sebelumnya                  |
  | <Kbd>Cmd Opt /</Kbd>                                 | Ganti model                                 |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | Chat baru                                   |
  | <Kbd>Cmd T</Kbd>                                     | Tab chat baru                               |
  | <Kbd>Cmd \[</Kbd>                                    | Chat sebelumnya                             |
  | <Kbd>Cmd ]</Kbd>                                     | Chat berikutnya                             |
  | <Kbd>Cmd W</Kbd>                                     | Tutup chat                                  |
  | <Kbd>Escape</Kbd>                                    | Lepas fokus bidang                          |
</div>

<div id="inline-edit">
  ## Edit Inline
</div>

<div className="full-width-table equal-table-columns">
  | Pintasan                       | Aksi                    |
  | ------------------------------ | ----------------------- |
  | <Kbd>Cmd K</Kbd>               | Buka                    |
  | <Kbd>Cmd Shift K</Kbd>         | Alihkan fokus input     |
  | <Kbd>Return</Kbd>              | Kirim                   |
  | <Kbd>Cmd Shift Backspace</Kbd> | Batalkan                |
  | <Kbd>Opt Return</Kbd>          | Ajukan pertanyaan cepat |
</div>

## Pemilihan Kode & Konteks

<div className="full-width-table equal-table-columns">
  | Pintasan                                             | Aksi                                                  |
  | ---------------------------------------------------- | ----------------------------------------------------- |
  | <Kbd>@</Kbd>                                         | [Simbol @](/id/context/@-symbols/)                    |
  | <Kbd>#</Kbd>                                         | File                                                  |
  | <Kbd>/</Kbd>                                         | Perintah pintasan                                     |
  | <Kbd>Cmd Shift L</Kbd>                               | Tambahkan pilihan ke Chat                             |
  | <Kbd>Cmd Shift K</Kbd>                               | Tambahkan pilihan ke Edit                             |
  | <Kbd>Cmd L</Kbd>                                     | Tambahkan pilihan ke chat baru                        |
  | <Kbd>Cmd M</Kbd>                                     | Ganti strategi pembacaan file                         |
  | <Kbd>Cmd →</Kbd>                                     | Terima kata berikutnya dari saran                     |
  | <Kbd>Cmd Return</Kbd>                                | Cari codebase di chat                                 |
  | Pilih kode, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Tambahkan kode referensi yang disalin sebagai konteks |
  | Pilih kode, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Tambahkan kode yang disalin sebagai konteks teks      |
</div>

<div id="tab">
  ## Tab
</div>

<div className="full-width-table equal-table-columns">
  | Pintasan         | Aksi                    |
  | ---------------- | ----------------------- |
  | <Kbd>Tab</Kbd>   | Terima saran            |
  | <Kbd>Cmd →</Kbd> | Terima kata selanjutnya |
</div>

<div id="terminal">
  ## Terminal
</div>

<div className="full-width-table equal-table-columns">
  | Shortcut              | Aksi                          |
  | --------------------- | ----------------------------- |
  | <Kbd>Cmd K</Kbd>      | Buka bar prompt terminal      |
  | <Kbd>Cmd Return</Kbd> | Jalankan perintah yang dibuat |
  | <Kbd>Escape</Kbd>     | Terima perintah               |
</div>



# Perintah Shell
Source: https://docs.cursor.com/id/configuration/shell

Instal dan gunakan perintah shell Cursor

Cursor menyediakan alat command-line untuk membuka file dan folder dari terminal. Instal perintah `cursor` dan `code` untuk mengintegrasikan Cursor ke alur kerja pengembangan lo.

<div id="installing-cli-commands">
  ## Menginstal perintah CLI
</div>

Pasang perintah CLI lewat Command Palette:

1. Buka Command Palette (Cmd/Ctrl + P)
2. Ketik "Install" untuk memfilter perintah instalasi
3. Pilih dan jalankan `Install 'cursor' to shell`
4. Ulangi dan pilih `Install 'code' to shell`

<product_visual type="screenshot">
  Command Palette menampilkan opsi pemasangan CLI
</product_visual>

<div id="using-the-cli-commands">
  ## Menggunakan perintah CLI
</div>

Setelah instalasi, gunakan salah satu perintah berikut untuk membuka file atau folder di Cursor:

```bash  theme={null}

# Menggunakan perintah cursor
cursor path/to/file.js
cursor path/to/folder/


# Menggunakan perintah code (kompatibel dengan VS Code)
code path/to/file.js
code path/to/folder/
```

<div id="command-options">
  ## Opsi perintah
</div>

Kedua perintah mendukung opsi berikut:

* Buka berkas: `cursor file.js`
* Buka folder: `cursor ./my-project`
* Buka beberapa item: `cursor file1.js file2.js folder1/`
* Buka di jendela baru: `cursor -n` atau `cursor --new-window`
* Tunggu hingga jendela ditutup: `cursor -w` atau `cursor --wait`

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Apa beda perintah cursor dan code?">
    Keduanya sama. Perintah `code` disediakan untuk kompatibilitas dengan VS Code.
  </Accordion>

  <Accordion title="Perlu install dua-duanya?">
    Nggak, install salah satu atau keduanya sesuai preferensi.
  </Accordion>

  <Accordion title="Perintahnya ke-install di mana?">
    Perintah di-install di file konfigurasi shell default sistem kamu (misalnya `.bashrc`, `.zshrc`, atau `.config/fish/config.fish`).
  </Accordion>
</AccordionGroup>



# Tema
Source: https://docs.cursor.com/id/configuration/themes

Kustomisasi tampilan Cursor

Cursor mendukung tema terang dan gelap buat lingkungan ngoding kamu. Cursor mewarisi kapabilitas tema dari VS Code—pakai tema VS Code apa pun, bikin tema kustom, dan pasang ekstensi tema dari marketplace.

<div id="changing-theme">
  ## Mengganti tema
</div>

1. Buka Command Palette (Cmd/Ctrl + P)
2. Ketik "theme" untuk memfilter perintah
3. Pilih "Preferences: Color Theme"
4. Pilih tema

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de83bbba983509af2002e4dfafe703ff" alt="Menu pilihan tema di Cursor yang menampilkan tema warna yang tersedia" data-og-width="3584" width="3584" data-og-height="2072" height="2072" data-path="images/config/themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=85b365baa01a725becb482e69eed6292 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=46eb0bed7d0d98612968135d727ee838 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8629851793f4498e7639ee4347484c88 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ea75113e217cc84f99f8f6d63af34ade 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ec5b85b5a4464d2af801f92b317a7e31 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=54fc29efe263f9935ba3273675ced7be 2500w" />
</Frame>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Bisa nggak aku pakai tema VS Code di Cursor?">
    Bisa! Cursor kompatibel dengan tema VS Code. Install tema apa pun dari VS Code Marketplace atau salin file tema kustom.
  </Accordion>

  <Accordion title="Gimana cara bikin tema kustom?">
    Bikin tema kustom sama kayak di VS Code. Pakai "Developer: Generate Color Theme From Current Settings" buat mulai dari pengaturan saat ini, atau ikutin panduan pembuatan tema VS Code.
  </Accordion>
</AccordionGroup>



# @Code
Source: https://docs.cursor.com/id/context/@-symbols/@-code

Referensi cuplikan kode spesifik di Cursor pakai @Code

Referensi bagian kode tertentu pakai simbol `@Code`. Ini ngasih kontrol yang lebih detail dibanding [`@Files & Folders`](/id/context/@-symbols/@-files-and-folders), jadi kamu bisa milih cuplikan kode yang tepat, bukan seluruh file.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fba3d385441084e243cd168eee8c9a9a" data-og-width="1850" width="1850" data-og-height="948" height="948" data-path="images/context/symbols/@-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6337ef4855301fdfef729012783d3cee 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ef348ae46e4a51ee298a6a5fa356eebd 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40ec3857dd21120790037ea409fac80d 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=604bfeb6907e96da64b1f814681232c8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cee1a79d449a4d163f566a6013b69318 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d4bb99b85dfa5ad539e63c3670171abe 2500w" />
</Frame>



# @Cursor Rules
Source: https://docs.cursor.com/id/context/@-symbols/@-cursor-rules

Terapkan aturan dan pedoman khusus proyek

Simbol `@Cursor Rules` ngasih akses ke [aturan proyek](/id/context/rules) dan pedoman yang udah lo set, jadi lo bisa menerapkannya secara eksplisit ke konteks lo.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e2f45682a0b471e5726cd5452ab6bceb" data-og-width="1518" width="1518" data-og-height="973" height="973" data-path="images/context/symbols/@-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6e67889ef0390f9be3c557247469c95b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1c22061fe8c8d000deeabbf404f1650d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a220fd7fbef492c2d523ed9e31324666 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44224ba38fd2a5460963b884c994d178 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=df766d5499d8b54ca4fa2211600515f6 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a06393ddd0d85711ad72d7b8991946a5 2500w" />
</Frame>



# @Files & Folders
Source: https://docs.cursor.com/id/context/@-symbols/@-files-and-folders

Gunakan file dan folder sebagai konteks di Chat dan Inline Edit

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="files">
  ## Files
</div>

Rujuk seluruh file di Chat dan Inline Edit dengan memilih `@Files & Folders`, lalu ketik nama file untuk mencari. Lo juga bisa menyeret file dari sidebar langsung ke Agent buat nambahinnya sebagai konteks.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8d46d3c961a3e898fd12c0cc1e1c8dce" data-og-width="2227" width="2227" data-og-height="1414" height="1414" data-path="images/context/symbols/@-files-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a3a78c7a6d2311a31efb941c40fbe11b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bfe1eff4516dce93f789e560e92f14ad 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=462239ebfd0181acfe36d2f937f32ca6 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1a64cd3cc0a07825c51d70c40dfe72fd 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=64ea129f283dd98fd9814820d6684a99 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b40e591d3e500f06eeb32fac49d4f90c 2500w" />
</Frame>

<div id="folders">
  ## Folder
</div>

Saat ngerujuk folder pakai `@Folders`, Cursor ngasih path folder dan ringkasan isinya biar AI paham apa aja yang tersedia.

<Tip>
  Setelah milih folder, ketik "/" buat masuk lebih dalam dan lihat semua subfolder.
</Tip>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a102e1c1cb7180c3ec6a1356273839a" data-og-width="2150" width="2150" data-og-height="1367" height="1367" data-path="images/context/symbols/@-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4b91de3b118c842aec8e1da04ca233d2 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fcba40013ff1349c28382151b52d5853 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=83cc5ac8db19a0d59de9a980c0ea10d7 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b87a80a369b62d48a2363a97a391de2 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29e93d39857f71ba7e00947e209514de 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa9b88463b43fa482c0654a0a0b362ca 2500w" />
</Frame>

<div id="full-folder-content">
  ### Konten folder lengkap
</div>

Aktifin **Konten Folder Lengkap** di pengaturan. Kalau diaktifkan, Cursor bakal nyoba nyertakan semua file dari folder ke dalam konteks.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ee37944a2e874a708b9d8281a063e580" data-og-width="1996" width="1996" data-og-height="296" height="296" data-path="images/context/symbols/folder-setting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=09520107c0518601c58f099ed119adab 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=748aecb97c43066f0be03416f9ed6ed0 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fd7e7c816092c9eed3182382fa77ff8f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=91baab4860e0f671196607f3c364b4d8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d2450ee2fcd6d8c59ba2412fad11121 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f4690bdb099c27092b9ddb6143bd8068 2500w" />
</Frame>

Untuk folder besar yang melebihi jendela konteks, tampilan outline bakal muncul dengan tooltip yang nunjukin berapa banyak file yang disertakan, sementara Cursor ngatur ruang konteks yang tersedia.

<Note>
  Pakai konten folder lengkap bareng [Mode Maks diaktifkan](/id/context/max-mode)
  bisa ningkatin biaya request secara signifikan karena lebih banyak token input kepake.
</Note>

<div id="context-management">
  ## Manajemen konteks
</div>

File dan folder berukuran besar otomatis diringkas agar tetap dalam batas konteks. Lihat [pengondensasian file & folder](/id/agent/chats/summarization#file--folder-condensation) untuk detailnya.



# @Git
Source: https://docs.cursor.com/id/context/@-symbols/@-git

Rujuk perubahan Git dan perbedaan branch

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=dba4c696d66e1274b96bf3261c8d927b" data-og-width="1658" width="1658" data-og-height="932" height="932" data-path="images/context/symbols/@-git.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=69bf90d13f034275fb78ab48e71d25ac 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e8c89a03ebdd5a1c1a576c8555380957 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ec7309f9ec4364c4ac0d237a9977f23 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f2d82f1eb2be6275c8b91ae63e943ee7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4e27a0a13a731fc0fe85a85a327f9884 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa1acf93e5e87b7a81d766a52601960d 2500w" />
</Frame>

* `@Commit`: Merujuk perubahan di state kerja saat ini dibanding commit terakhir. Menampilkan semua file yang dimodifikasi, ditambahkan, dan dihapus yang belum di-commit.
* `@Branch`: Bandingkan perubahan di branch kamu saat ini dengan branch main. Menampilkan semua commit dan perubahan di branch kamu yang belum ada di main.



# @Link
Source: https://docs.cursor.com/id/context/@-symbols/@-link

Sertakan konten web dengan menempelkan URL

Saat lo menempelkan URL di Chat, Cursor otomatis menandainya sebagai `@Link` dan mengambil kontennya untuk dipakai sebagai konteks. Ini juga mendukung dokumen PDF — Cursor mengekstrak dan mengurai konten teks dari URL PDF yang dapat diakses publik.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d96b384a0480aba7981b6fbebee1fac8" data-og-width="1618" width="1618" data-og-height="1035" height="1035" data-path="images/context/symbols/@-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d251326cc25b2835488b1f25b05f2c4f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d1b64f393d89cfc547c6e12ae7a6adef 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d5a2aa41c6a6affea03379adac5e76c8 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e94e2c0610eafea625996386374e8898 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=404333e65fa1c98e2e92fd941d2e8b92 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=63d9a66571fde75678b6fa0d0cbac44f 2500w" />
</Frame>

<div id="unlink">
  ## Hapus Tautan
</div>

Gunakan URL sebagai teks biasa tanpa mengambil kontennya:

* Klik tautan yang ditandai dan pilih `Unlink`
* Atau tempel sambil menahan `Shift` untuk mencegah penandaan otomatis

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5eca9b93aa4c2ba4f8d0f6a97a34052f" data-og-width="1212" width="1212" data-og-height="408" height="408" data-path="images/context/symbols/@-link-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=be5f171437d0d3c79ded195c7a387741 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ca29084e45c832b6aa9015fcd5cf680 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eb394772d364e392ff794c43ed1fbfcc 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5df343df91b3bf4aed9edb32fc192059 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a35df3274c439984b2072eb758d05fb1 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a20f166b838435ade65084c844cc3c6a 2500w" />
</Frame>



# @Linter Errors
Source: https://docs.cursor.com/id/context/@-symbols/@-linter-errors

Akses dan rujuk error linting di codebase lo

Simbol `@Linter Errors` otomatis nangkep dan ngasih konteks tentang error dan peringatan linting dari file aktif lo saat ini. [Agent](/id/agent/overview) bisa lihat lint errors secara default.

<Note>
  Biar linter errors kelihatan, lo perlu language server yang sesuai
  dipasang dan dikonfigurasi buat bahasa pemrograman lo. Cursor otomatis
  mendeteksi dan pakai language server yang terpasang, tapi lo mungkin perlu
  pasang ekstensi atau tools tambahan buat bahasa tertentu.
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6ef34b3ae96a7d49695035cb5c3ac9f9" data-og-width="1590" width="1590" data-og-height="1017" height="1017" data-path="images/context/symbols/@-linter-errors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13e682f26536e5cb104142bcc7becbeb 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cf3947376ee2e17f83c08809b23e864c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13d026063f9bc5e61c78740fee8eebc5 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29c834609d2f549b295be53cdbf7eec6 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b2131adda5b89685d7d7a26ed218fee 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9cd3c3e34cbee0f73fe478024018539 2500w" />
</Frame>



# @Past Chats
Source: https://docs.cursor.com/id/context/@-symbols/@-past-chats

Sertakan obrolan yang diringkas dari riwayat

Saat ngerjain tugas kompleks di [Chat](/id/chat), kadang kamu perlu merujuk konteks atau keputusan dari percakapan sebelumnya. Simbol `@Past Chats` nyediain versi ringkas dari obrolan sebelumnya sebagai konteks.

Khususnya berguna ketika:

* Kamu punya sesi Chat panjang dengan konteks penting yang perlu dirujuk
* Kamu mulai tugas baru yang terkait dan pengin kontinuitas
* Kamu pengin berbagi alasan atau keputusan dari sesi sebelumnya

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6839cf571e64e1ed10dd5dc270d4ac45" data-og-width="2340" width="2340" data-og-height="1485" height="1485" data-path="images/context/symbols/@-past-chats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0278e6fdce8d8771ecd6f64faf5048db 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3a2d4722e90c1078c11fcd695993d84a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d46e21680b56820aef7a9baf34891e0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f19f25e6988729059f40731378ce4fab 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=86f9457d09e7dd4578c8609fd3cff6b5 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8efb9e097f9e434d0b7f03cac9b02396 2500w" />
</Frame>



# @Recent Changes
Source: https://docs.cursor.com/id/context/@-symbols/@-recent-changes

Sertakan kode yang baru dimodifikasi sebagai konteks

Simbol `@Recent Changes` menyertakan perubahan kode terbaru sebagai konteks dalam percakapan AI.

* Perubahan diurutkan secara kronologis
* Memprioritaskan 10 perubahan terakhir
* Mengikuti pengaturan `.cursorignore`

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e6968afeeed9e790121d8280f63b670d" data-og-width="1556" width="1556" data-og-height="996" height="996" data-path="images/context/symbols/@-recent-changes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=beae76f109d8eb29788ab3c90f72b831 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c4e6ad386c30f9546e1485ca4c14c0f2 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7d80d31e720b167408cd308204fa666a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=868a93753377dcb2d6820c748b9b17d7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e84e94c4fe64f9e4270fd72883a4962d 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=139ffc703716759bb8b8c35e57bd6dbf 2500w" />
</Frame>




---

**Navigation:** [← Previous](./15-serveurs-mcp.md) | [Index](./index.md) | [Next →](./17-web.md)