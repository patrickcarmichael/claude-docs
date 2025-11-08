---
title: "VS Code"
source: "https://docs.cursor.com/ja/guides/migration/vscode"
language: "ja"
language_name: "Japanese"
---

# VS Code
Source: https://docs.cursor.com/ja/guides/migration/vscode

ワンクリックで VS Code の設定と拡張機能をインポート

Cursor は VS Code のコードベース上に構築されているため、親しみのある編集環境を保ちながら、最高の AI 搭載コーディング体験の実現に集中できる。これにより、既存の VS Code の設定を簡単に Cursor に移行できる。

<div id="profile-migration">
  ## プロファイル移行
</div>

<div id="one-click-import">
  ### ワンクリックインポート
</div>

VS Code のセットアップをワンクリックでまるごと取り込む手順:

1. Cursor の設定を開く（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>）
2. General > Account に移動
3. 「VS Code Import」の下にある Import ボタンをクリック

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

これで以下が移行される:

* Extensions
* Themes
* Settings
* Keybindings

<div id="manual-profile-migration">
  ### 手動でのプロファイル移行
</div>

マシン間で移行する場合や、設定を細かくコントロールしたい場合は、プロファイルを手動で移行できる。

<div id="exporting-a-profile">
  #### プロファイルのエクスポート
</div>

1. VS Code で Command Palette を開く（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>）
2. 「Preferences: Open Profiles (UI)」を検索
3. 左サイドバーでエクスポートしたいプロファイルを見つける
4. 3 点メニューをクリックして「Export Profile」を選択
5. ローカルマシンまたは GitHub Gist へのエクスポートを選ぶ

<div id="importing-a-profile">
  #### プロファイルのインポート
</div>

1. Cursor で Command Palette を開く（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>）
2. 「Preferences: Open Profiles (UI)」を検索
3. 「New Profile」の横にあるドロップダウンメニューをクリックし、「Import Profile」をクリック
4. GitHub Gist の URL を貼り付けるか、「Select File」を選んでローカルファイルをアップロード
5. ダイアログ下部の「Import」をクリックしてプロファイルを保存
6. 最後に、サイドバーで新しいプロファイルを選び、チェックアイコンをクリックして有効化する

<div id="settings-and-interface">
  ## 設定とインターフェース
</div>

<div id="settings-menus">
  ### 設定メニュー
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Command Palette（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>）を開いて、"Cursor Settings" と入力
  </Card>

  <Card title="VS Code Settings" icon="code">
    Command Palette（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>）を開いて、"Preferences: Open Settings (UI)" と入力
  </Card>
</CardGroup>

<div id="version-updates">
  ### バージョンアップデート
</div>

<Card title="Version Updates" icon="code-merge">
  最新の VS Code バージョンに追従するため、Cursor は定期的にリベースして
  機能や修正を取り込んでいる。安定性を確保するために、Cursor はあえて少し古い
  VS Code バージョンを使うことがある。
</Card>

<div id="activity-bar-orientation">
  ### アクティビティバーの向き
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

AI チャットインターフェースのスペースを最適化するために横向きにしている。縦向きが良ければ:

1. Command Palette（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>）を開く
2. "Preferences: Open Settings (UI)" を検索
3. `workbench.activityBar.orientation` を検索
4. 値を `vertical` に設定
5. Cursor を再起動

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [アーキテクチャ図](./section.md) →