---
title: "VS Code"
source: "https://docs.cursor.com/id/guides/migration/vscode"
language: "id"
language_name: "Indonesian"
---

# VS Code
Source: https://docs.cursor.com/id/guides/migration/vscode

Impor pengaturan dan ekstensi VS Code dengan sekali klik

Cursor dibangun di atas codebase VS Code, jadi kita bisa fokus bikin pengalaman ngoding bertenaga AI yang maksimal sambil tetap mempertahankan lingkungan editor yang familiar. Ini memudahkan kamu buat migrasi pengaturan VS Code yang sudah ada ke Cursor.

<div id="profile-migration">
  ## Migrasi Profil
</div>

<div id="one-click-import">
  ### Impor Sekali Klik
</div>

Begini cara dapetin seluruh setup VS Code kamu dalam satu klik:

1. Buka Cursor Settings (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. Masuk ke General > Account
3. Di bawah "VS Code Import", klik tombol Import

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

Ini bakal mindahin:

* Extensions
* Themes
* Settings
* Keybindings

<div id="manual-profile-migration">
  ### Migrasi Profil Manual
</div>

Kalau kamu pindah perangkat, atau pengen kontrol lebih atas pengaturan kamu, kamu bisa migrasi profil secara manual.

<div id="exporting-a-profile">
  #### Mengekspor Profil
</div>

1. Di VS Code kamu, buka Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Cari "Preferences: Open Profiles (UI)"
3. Temukan profil yang mau diekspor di sidebar kiri
4. Klik menu 3 titik dan pilih "Export Profile"
5. Pilih untuk mengekspornya ke perangkat lokal kamu atau ke GitHub Gist

<div id="importing-a-profile">
  #### Mengimpor Profil
</div>

1. Di Cursor kamu, buka Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Cari "Preferences: Open Profiles (UI)"
3. Klik menu dropdown di sebelah 'New Profile' dan klik 'Import Profile'
4. Tempel URL GitHub Gist atau pilih 'Select File' untuk mengunggah file lokal
5. Klik 'Import' di bagian bawah dialog untuk nyimpen profil
6. Terakhir, di sidebar, pilih profil baru dan klik ikon centang buat ngaktifinnya

<div id="settings-and-interface">
  ## Pengaturan dan Antarmuka
</div>

<div id="settings-menus">
  ### Menu Pengaturan
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Akses via Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), lalu ketik "Cursor Settings"
  </Card>

  <Card title="VS Code Settings" icon="code">
    Akses via Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), lalu ketik "Preferences: Open Settings (UI)"
  </Card>
</CardGroup>

<div id="version-updates">
  ### Pembaruan Versi
</div>

<Card title="Version Updates" icon="code-merge">
  Kami rutin me-rebase Cursor ke versi VS Code terbaru supaya tetap mengikuti
  fitur dan perbaikan terkini. Demi stabilitas, Cursor sering memakai versi
  VS Code yang sedikit lebih lama.
</Card>

<div id="activity-bar-orientation">
  ### Orientasi Activity Bar
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

Kami bikin horizontal supaya ruang untuk antarmuka chat AI lebih optimal. Kalau lebih suka vertikal:

1. Buka Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Cari "Preferences: Open Settings (UI)"
3. Cari `workbench.activityBar.orientation`
4. Set nilainya ke `vertical`
5. Restart Cursor

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Diagram Arsitektur](./diagram-arsitektur.md) →