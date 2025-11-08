---
title: "VS Code"
source: "https://docs.cursor.com/ru/guides/migration/vscode"
language: "ru"
language_name: "Russian"
---

# VS Code
Source: https://docs.cursor.com/ru/guides/migration/vscode

Импортируй настройки и расширения VS Code в один клик

Cursor построен на базе кода VS Code, поэтому мы можем сосредоточиться на создании лучшего AI‑опыта разработки, сохраняя знакомую среду редактирования. Это упрощает перенос твоих текущих настроек VS Code в Cursor.

<div id="profile-migration">
  ## Миграция профиля
</div>

<div id="one-click-import">
  ### Импорт в один клик
</div>

Вот как забрать всю твою конфигурацию VS Code в один клик:

1. Открой Cursor Settings (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. Перейди в General > Account
3. В разделе "VS Code Import" нажми кнопку Import

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

Будут перенесены:

* расширения
* темы
* настройки
* сочетания клавиш

<div id="manual-profile-migration">
  ### Ручная миграция профиля
</div>

Если ты переезжаешь на другой компьютер или хочешь больше контроля над настройками, можно вручную перенести профиль.

<div id="exporting-a-profile">
  #### Экспорт профиля
</div>

1. В своём VS Code открой Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Найди "Preferences: Open Profiles (UI)"
3. Найди профиль, который хочешь экспортировать, в левой боковой панели
4. Нажми на меню с тремя точками и выбери "Export Profile"
5. Экспортируй либо на локальный компьютер, либо в GitHub Gist

<div id="importing-a-profile">
  #### Импорт профиля
</div>

1. В своём Cursor открой Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Найди "Preferences: Open Profiles (UI)"
3. Нажми на выпадающее меню рядом с "New Profile" и выбери "Import Profile"
4. Вставь URL GitHub Gist или нажми "Select File", чтобы загрузить локальный файл
5. Нажми "Import" внизу диалога, чтобы сохранить профиль
6. В конце в боковой панели выбери новый профиль и нажми на значок галочки, чтобы активировать его

<div id="settings-and-interface">
  ## Настройки и интерфейс
</div>

<div id="settings-menus">
  ### Меню настроек
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Открой через Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), затем введи «Cursor Settings»
  </Card>

  <Card title="VS Code Settings" icon="code">
    Открой через Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), затем введи «Preferences: Open Settings (UI)»
  </Card>
</CardGroup>

<div id="version-updates">
  ### Обновления версий
</div>

<Card title="Version Updates" icon="code-merge">
  Мы регулярно обновляем базу Cursor до последней версии VS Code, чтобы оставаться в
  курсе новых функций и исправлений. Для стабильности Cursor часто использует
  чуть более старые версии VS Code.
</Card>

<div id="activity-bar-orientation">
  ### Ориентация Activity Bar
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

Мы сделали её горизонтальной, чтобы оптимизировать место для интерфейса AI-чата. Если тебе нужна вертикальная:

1. Открой Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Найди «Preferences: Open Settings (UI)»
3. Найди `workbench.activityBar.orientation`
4. Установи значение `vertical`
5. Перезапусти Cursor

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Архитектурные диаграммы](./section.md) →