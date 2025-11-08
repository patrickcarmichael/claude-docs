---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/id/guides/languages/swift"
language: "id"
language_name: "Indonesian"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/id/guides/languages/swift

Integrasikan Cursor dengan Xcode untuk pengembangan Swift

Selamat datang di pengembangan Swift di Cursor! Mau bikin app iOS, aplikasi macOS, atau proyek Swift sisi server, semuanya aman. Panduan ini bakal bantu lo nyiapin environment Swift di Cursor, mulai dari dasar sampai fitur yang lebih advanced.

<div id="basic-workflow">
  ## Alur Dasar
</div>

Cara paling sederhana buat pakai Cursor dengan Swift adalah menjadikannya editor kode utama sambil tetap mengandalkan Xcode untuk build dan ngejalanin app. Kamu bakal dapat fitur-fitur keren seperti:

* Pelengkapan kode pintar
* Bantuan ngoding bertenaga AI (coba [CMD+K](/id/inline-edit/overview) di baris mana pun)
* Akses cepat ke dokumentasi lewat [@Docs](/id/context/@-symbols/@-docs)
* Highlighting sintaks
* Navigasi kode dasar

Kalau perlu build atau jalanin app, cukup pindah ke Xcode. Alur kerja ini pas buat developer yang mau manfaatin kapabilitas AI dari Cursor sambil tetap pakai tool Xcode yang familiar buat debugging dan deployment.

<div id="hot-reloading">
  ### Hot Reloading
</div>

Saat pakai workspace atau project Xcode (bukannya buka folder langsung di Xcode), Xcode sering kali bisa ngeabaikan perubahan pada file kamu yang dibuat di Cursor, atau di luar Xcode pada umumnya.

Walau kamu bisa buka foldernya di Xcode buat beresin ini, kamu mungkin perlu tetap pakai project untuk alur kerja pengembangan Swift.

Solusi yang oke adalah pakai [Inject](https://github.com/krzysztofzablocki/Inject), library hot reloading untuk Swift yang memungkinkan app kamu “hot reload” dan ke-update seketika begitu ada perubahan secara real-time. Ini gak kena efek samping dari masalah workspace/project Xcode, dan memungkinkan kamu ngelakuin perubahan di Cursor lalu langsung tercermin di app kamu.

<CardGroup cols={1}>
  <Card title="Inject - Hot Reloading untuk Swift" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Pelajari lebih lanjut tentang Inject dan cara makainya di project Swift kamu.
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## Pengembangan Swift Lanjutan
</div>

<Note>
  Bagian panduan ini banyak terinspirasi dari [Thomas
  Ricouard](https://x.com/Dimillian) dan
  [artikelnya](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  tentang penggunaan Cursor untuk pengembangan iOS. Cek artikelnya buat
  detail lebih lanjut dan follow dia untuk konten Swift lainnya.
</Note>

Kalau kamu pengin cuma buka satu editor sekaligus dan mau ngindarin bolak-balik antara Xcode dan Cursor, kamu bisa pakai ekstensi seperti [Sweetpad](https://sweetpad.hyzyla.dev/) buat mengintegrasikan Cursor langsung dengan sistem build inti Xcode.

Sweetpad adalah ekstensi yang powerful yang memungkinkan kamu build, run, dan debug proyek Swift langsung di Cursor, tanpa mengorbankan fitur-fitur Xcode.

Buat mulai pakai Sweetpad, kamu tetap perlu Xcode terpasang di Mac kamu—itu fondasi pengembangan Swift. Kamu bisa mengunduh Xcode dari [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835). Setelah Xcode siap, yuk tingkatkan pengalaman pengembangan kamu di Cursor dengan beberapa tool penting.

Buka terminal kamu dan jalankan:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →