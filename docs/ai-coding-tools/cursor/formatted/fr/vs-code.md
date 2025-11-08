---
title: "VS Code"
source: "https://docs.cursor.com/fr/guides/migration/vscode"
language: "fr"
language_name: "French"
---

# VS Code
Source: https://docs.cursor.com/fr/guides/migration/vscode

Importer les paramètres et extensions de VS Code en un clic

Cursor est basé sur la base de code de VS Code, ce qui nous permet de nous concentrer sur la meilleure expérience de codage propulsée par l’IA tout en conservant un environnement d’édition familier. Ça te permet de migrer facilement tes paramètres VS Code existants vers Cursor.

<div id="profile-migration">
  ## Migration de profil
</div>

<div id="one-click-import">
  ### Import en un clic
</div>

Voici comment récupérer toute ta config VS Code en un clic :

1. Ouvre les paramètres de Cursor (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. Va dans General > Account
3. Sous "VS Code Import", clique sur le bouton Import

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

Ça va transférer tes :

* Extensions
* Thèmes
* Paramètres
* Raccourcis clavier

<div id="manual-profile-migration">
  ### Migration manuelle du profil
</div>

Si tu passes d’une machine à une autre, ou si tu veux plus de contrôle sur tes paramètres, tu peux migrer ton profil manuellement.

<div id="exporting-a-profile">
  #### Exporter un profil
</div>

1. Dans ton instance VS Code, ouvre la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Recherche "Preferences: Open Profiles (UI)"
3. Trouve le profil que tu veux exporter dans la barre latérale gauche
4. Clique sur le menu à 3 points et sélectionne "Export Profile"
5. Choisis de l’exporter soit sur ta machine locale, soit vers un GitHub Gist

<div id="importing-a-profile">
  #### Importer un profil
</div>

1. Dans ton instance Cursor, ouvre la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Recherche "Preferences: Open Profiles (UI)"
3. Clique sur le menu déroulant à côté de "New Profile" et clique sur "Import Profile"
4. Colle l’URL du GitHub Gist ou choisis "Select File" pour importer un fichier local
5. Clique sur "Import" en bas de la boîte de dialogue pour enregistrer le profil
6. Enfin, dans la barre latérale, sélectionne le nouveau profil et clique sur l’icône en forme de coche pour l’activer

<div id="settings-and-interface">
  ## Paramètres et interface
</div>

<div id="settings-menus">
  ### Menus des paramètres
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Accède à la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), puis tape "Cursor Settings"
  </Card>

  <Card title="VS Code Settings" icon="code">
    Accède à la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), puis tape "Preferences: Open Settings (UI)"
  </Card>
</CardGroup>

<div id="version-updates">
  ### Mises à jour de version
</div>

<Card title="Version Updates" icon="code-merge">
  On rebase régulièrement Cursor sur la dernière version de VS Code pour rester à jour
  avec les fonctionnalités et correctifs. Pour garantir la stabilité, Cursor utilise souvent des versions de
  VS Code légèrement plus anciennes.
</Card>

<div id="activity-bar-orientation">
  ### Orientation de la barre d’activité
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

On l’a mise à l’horizontale pour optimiser l’espace de l’interface de chat IA. Si tu préfères en vertical :

1. Ouvre la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Recherche "Preferences: Open Settings (UI)"
3. Recherche `workbench.activityBar.orientation`
4. Défini la valeur sur `vertical`
5. Redémarre Cursor

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Schémas d’architecture](./schmas-darchitecture.md) →