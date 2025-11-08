---
title: "VS Code"
source: "https://docs.cursor.com/de/guides/migration/vscode"
language: "de"
language_name: "German"
---

# VS Code
Source: https://docs.cursor.com/de/guides/migration/vscode

VS-Code-Einstellungen und -Erweiterungen mit einem Klick importieren

Cursor basiert auf dem VS-Code-Codebasis, sodass wir uns darauf konzentrieren können, die beste KI-gestützte Coding-Erfahrung zu bieten – bei gleichzeitig vertrauter Bearbeitungsumgebung. So kannst du deine vorhandenen VS-Code-Einstellungen ganz einfach zu Cursor migrieren.

<div id="profile-migration">
  ## Profilmigration
</div>

<div id="one-click-import">
  ### Import mit einem Klick
</div>

So holst du dir dein komplettes VS Code-Setup mit einem Klick:

1. Öffne die Cursor-Einstellungen (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. Navigiere zu General > Account
3. Klicke unter „VS Code Import“ auf die Schaltfläche „Import“

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

Damit werden folgende Elemente übernommen:

* Extensions
* Themes
* Settings
* Keybindings

<div id="manual-profile-migration">
  ### Manuelle Profilmigration
</div>

Wenn du zwischen Rechnern wechselst oder mehr Kontrolle über deine Einstellungen willst, kannst du dein Profil manuell migrieren.

<div id="exporting-a-profile">
  #### Profil exportieren
</div>

1. Öffne in deiner VS Code-Instanz die Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Suche nach „Preferences: Open Profiles (UI)“
3. Finde in der linken Sidebar das Profil, das du exportieren möchtest
4. Klicke auf das 3-Punkte-Menü und wähle „Export Profile“
5. Wähle, ob du es auf deinen lokalen Rechner exportieren oder in einem GitHub Gist speichern möchtest

<div id="importing-a-profile">
  #### Profil importieren
</div>

1. Öffne in deiner Cursor-Instanz die Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Suche nach „Preferences: Open Profiles (UI)“
3. Klicke auf das Dropdown-Menü neben „New Profile“ und dann auf „Import Profile“
4. Füge entweder die URL des GitHub Gists ein oder wähle „Select File“, um eine lokale Datei hochzuladen
5. Klicke unten im Dialog auf „Import“, um das Profil zu speichern
6. Wähle schließlich in der Sidebar das neue Profil und klicke auf das Häkchen, um es zu aktivieren

<div id="settings-and-interface">
  ## Einstellungen und Oberfläche
</div>

<div id="settings-menus">
  ### Einstellungsmenüs
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Zugriff über die Befehlspalette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), dann „Cursor Settings“ eingeben
  </Card>

  <Card title="VS Code Settings" icon="code">
    Zugriff über die Befehlspalette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), dann „Preferences: Open Settings (UI)“ eingeben
  </Card>
</CardGroup>

<div id="version-updates">
  ### Versionsupdates
</div>

<Card title="Version Updates" icon="code-merge">
  Wir rebasen Cursor regelmäßig auf die neueste VS-Code-Version, um bei
  Features und Fixes auf dem neuesten Stand zu bleiben. Für mehr Stabilität
  verwendet Cursor oft leicht ältere VS-Code-Versionen.
</Card>

<div id="activity-bar-orientation">
  ### Ausrichtung der Aktivitätsleiste
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

Wir haben sie horizontal gestaltet, um Platz für die AI-Chat-Oberfläche zu optimieren. Wenn dir die vertikale Ausrichtung lieber ist:

1. Öffne die Befehlspalette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Suche nach „Preferences: Open Settings (UI)“
3. Suche nach `workbench.activityBar.orientation`
4. Setze den Wert auf `vertical`
5. Starte Cursor neu

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Architekturschaubilder](./architekturschaubilder.md) →