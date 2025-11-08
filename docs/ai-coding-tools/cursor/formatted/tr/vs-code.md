---
title: "VS Code"
source: "https://docs.cursor.com/tr/guides/migration/vscode"
language: "tr"
language_name: "Turkish"
---

# VS Code
Source: https://docs.cursor.com/tr/guides/migration/vscode

Tek tıkla VS Code ayarlarını ve uzantılarını içe aktar

Cursor, VS Code kod tabanını temel alır; bu sayede tanıdık bir düzenleme ortamını korurken en iyi yapay zeka destekli kodlama deneyimine odaklanabiliyoruz. Bu da mevcut VS Code ayarlarını Cursor’a taşımanı kolaylaştırır.

<div id="profile-migration">
  ## Profil Taşıma
</div>

<div id="one-click-import">
  ### Tek tıkla içe aktarma
</div>

Tüm VS Code kurulumunu tek tıkla şöyle alırsın:

1. Cursor Settings’i aç (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. General > Account’a git
3. "VS Code Import" altında Import butonuna tıkla

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

Bu işlem şunları taşır:

* Extensions
* Themes
* Settings
* Keybindings

<div id="manual-profile-migration">
  ### Manuel profil taşıma
</div>

Makineler arasında geçiş yapıyorsan ya da ayarların üzerinde daha fazla kontrol istiyorsan, profilini manuel olarak taşıyabilirsin.

<div id="exporting-a-profile">
  #### Profil dışa aktarma
</div>

1. VS Code örneğinde Command Palette’i aç (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. "Preferences: Open Profiles (UI)" ifadesini ara
3. Sol kenar çubuğunda dışa aktarmak istediğin profili bul
4. 3 noktalı menüye tıkla ve "Export Profile"’ı seç
5. Yerel makineye ya da bir GitHub Gist’e dışa aktarmayı seç

<div id="importing-a-profile">
  #### Profil içe aktarma
</div>

1. Cursor örneğinde Command Palette’i aç (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. "Preferences: Open Profiles (UI)" ifadesini ara
3. 'New Profile' yanındaki açılır menüye tıkla ve 'Import Profile'ı seç
4. GitHub Gist’in URL’sini yapıştır ya da yerel bir dosya yüklemek için 'Select File'ı seç
5. Profili kaydetmek için ileti penceresinin altındaki 'Import' butonuna tıkla
6. Son olarak, kenar çubuğunda yeni profili seç ve etkinleştirmek için onay işareti simgesine tıkla

<div id="settings-and-interface">
  ## Ayarlar ve Arayüz
</div>

<div id="settings-menus">
  ### Ayar Menüler
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Komut Paletinden eriş (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), ardından "Cursor Settings" yaz
  </Card>

  <Card title="VS Code Settings" icon="code">
    Komut Paletinden eriş (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), ardından "Preferences: Open Settings (UI)" yaz
  </Card>
</CardGroup>

<div id="version-updates">
  ### Sürüm Güncellemeleri
</div>

<Card title="Version Updates" icon="code-merge">
  Güncel özellikler ve düzeltmelerle uyumlu kalmak için Cursor’ı düzenli olarak
  en yeni VS Code sürümüne yeniden temellendiriyoruz (rebase). Kararlılığı sağlamak için Cursor sık sık
  biraz daha eski VS Code sürümlerini kullanır.
</Card>

<div id="activity-bar-orientation">
  ### Etkinlik Çubuğu Yönü
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

AI sohbet arayüzü için alanı optimize etmek adına yatay yaptık. Dikey istiyorsan:

1. Komut Paletini aç (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. "Preferences: Open Settings (UI)" ara
3. `workbench.activityBar.orientation` ara
4. Değeri `vertical` olarak ayarla
5. Cursor’ı yeniden başlat

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Mimari Diyagramlar](./mimari-diyagramlar.md) →