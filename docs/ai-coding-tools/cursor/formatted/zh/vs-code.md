---
title: "VS Code"
source: "https://docs.cursor.com/zh/guides/migration/vscode"
language: "zh"
language_name: "Chinese"
---

# VS Code
Source: https://docs.cursor.com/zh/guides/migration/vscode

一键导入 VS Code 设置和扩展

Cursor 基于 VS Code 代码库构建，让我们在保留熟悉的编辑环境的同时，专注打造最佳的 AI 驱动编码体验。这样你就能轻松将现有的 VS Code 设置迁移到 Cursor。

<div id="profile-migration">
  ## 配置迁移
</div>

<div id="one-click-import">
  ### 一键导入
</div>

一键把你的 VS Code 整套配置带过来：

1. 打开 Cursor 设置（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>）
2. 前往 General > Account
3. 在“VS Code Import”下，点击 Import 按钮

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

这会迁移你的：

* 扩展
* 主题
* 设置
* 按键绑定

<div id="manual-profile-migration">
  ### 手动配置迁移
</div>

如果在不同机器间切换，或想更细致地掌控设置，可以手动迁移配置。

<div id="exporting-a-profile">
  #### 导出配置
</div>

1. 在 VS Code 中打开命令面板（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>）
2. 搜索“Preferences: Open Profiles (UI)”
3. 在左侧边栏找到要导出的配置
4. 点击三点菜单并选择“Export Profile”
5. 选择导出到本机或导出到 GitHub Gist

<div id="importing-a-profile">
  #### 导入配置
</div>

1. 在 Cursor 中打开命令面板（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>）
2. 搜索“Preferences: Open Profiles (UI)”
3. 点击“New Profile”旁的下拉菜单并选择“Import Profile”
4. 粘贴 GitHub Gist 的 URL，或选择“Select File”上传本地文件
5. 在对话框底部点击“Import”保存配置
6. 最后在侧边栏选择新配置并点击勾选图标以启用

<div id="settings-and-interface">
  ## 设置与界面
</div>

<div id="settings-menus">
  ### 设置菜单
</div>

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    通过命令面板（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>）打开，然后输入 "Cursor Settings"
  </Card>

  <Card title="VS Code Settings" icon="code">
    通过命令面板（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>）打开，然后输入 "Preferences: Open Settings (UI)"
  </Card>
</CardGroup>

<div id="version-updates">
  ### 版本更新
</div>

<Card title="Version Updates" icon="code-merge">
  我们会定期将 Cursor rebase 到最新的 VS Code 版本，以保持与其最新功能与修复同步。为确保稳定性，Cursor 通常会使用略旧的 VS Code 版本。
</Card>

<div id="activity-bar-orientation">
  ### Activity Bar 方向
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

我们将其设置为横向，以便为 AI 聊天界面节省空间。如果你更喜欢纵向：

1. 打开命令面板（<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>）
2. 搜索 "Preferences: Open Settings (UI)"
3. 搜索 `workbench.activityBar.orientation`
4. 将其设置为 `vertical`
5. 重启 Cursor

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [架构图](./section.md) →