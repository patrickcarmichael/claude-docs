---
title: "Agen Latar Belakang"
source: "https://docs.cursor.com/id/background-agent"
language: "id"
language_name: "Indonesian"
---

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

---

← Previous: [Tools](./tools.md) | [Index](./index.md) | Next: [Tambahkan Tindak Lanjut](./tambahkan-tindak-lanjut.md) →