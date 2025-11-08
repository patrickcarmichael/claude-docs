---
title: "VS Code"
source: "https://docs.cursor.com/es/guides/migration/vscode"
language: "es"
language_name: "Spanish"
---

# VS Code
Source: https://docs.cursor.com/es/guides/migration/vscode

Importa la configuración y las extensiones de VS Code con un clic

Cursor se basa en la base de código de VS Code, lo que nos permite enfocarnos en ofrecer la mejor experiencia de programación con IA mientras mantenemos un entorno de edición familiar. Esto hace que sea fácil migrar tu configuración de VS Code a Cursor.

<div id="profile-migration">
  ## Migración de perfil
</div>

<div id="one-click-import">
  ### Importación con un clic
</div>

Así puedes traer toda tu configuración de VS Code en un solo clic:

1. Abre la configuración de Cursor (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. Ve a General > Account
3. En "VS Code Import", haz clic en el botón Import

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

Esto transferirá tus:

* Extensiones
* Temas
* Configuraciones
* Atajos de teclado

<div id="manual-profile-migration">
  ### Migración manual del perfil
</div>

Si estás cambiando de máquina o quieres más control sobre tu configuración, puedes migrar tu perfil manualmente.

<div id="exporting-a-profile">
  #### Exportar un perfil
</div>

1. En tu instancia de VS Code, abre la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Busca "Preferences: Open Profiles (UI)"
3. Encuentra el perfil que quieres exportar en la barra lateral izquierda
4. Haz clic en el menú de 3 puntos y selecciona "Export Profile"
5. Elige exportarlo a tu equipo local o a un GitHub Gist

<div id="importing-a-profile">
  #### Importar un perfil
</div>

1. En tu instancia de Cursor, abre la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Busca "Preferences: Open Profiles (UI)"
3. Haz clic en el menú desplegable junto a "New Profile" y luego en "Import Profile"
4. Pega la URL del GitHub Gist o elige "Select File" para subir un archivo local
5. Haz clic en "Import" en la parte inferior del cuadro de diálogo para guardar el perfil
6. Por último, en la barra lateral, elige el nuevo perfil y haz clic en el ícono de check para activarlo

<div id="settings-and-interface">
  ## Configuración e interfaz
</div>

<div id="settings-menus">
  ### Menús de configuración
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Accedé desde la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), luego escribí "Cursor Settings"
  </Card>

  <Card title="VS Code Settings" icon="code">
    Accedé desde la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), luego escribí "Preferences: Open Settings (UI)"
  </Card>
</CardGroup>

<div id="version-updates">
  ### Actualizaciones de versión
</div>

<Card title="Actualizaciones de versión" icon="code-merge">
  Regularmente rebasemos Cursor sobre la última versión de VS Code para mantenernos al día
  con las funciones y correcciones. Para garantizar la estabilidad, Cursor suele usar versiones
  de VS Code ligeramente anteriores.
</Card>

<div id="activity-bar-orientation">
  ### Orientación de la Activity Bar
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

La pusimos horizontal para optimizar el espacio de la interfaz de chat con IA. Si la preferís vertical:

1. Abrí la Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Buscá "Preferences: Open Settings (UI)"
3. Buscá `workbench.activityBar.orientation`
4. Configurá el valor en `vertical`
5. Reiniciá Cursor

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Diagramas de arquitectura](./diagramas-de-arquitectura.md) →