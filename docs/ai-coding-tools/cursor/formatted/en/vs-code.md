---
title: "VS Code"
source: "https://docs.cursor.com/en/guides/migration/vscode"
language: "en"
language_name: "English"
---

# VS Code
Source: https://docs.cursor.com/en/guides/migration/vscode

Import VS Code settings and extensions with one click

Cursor is based upon the VS Code codebase, allowing us to focus on making the best AI-powered coding experience while maintaining a familiar editing environment. This makes it easy to migrate your existing VS Code settings to Cursor.

## Profile Migration

### One-click Import

Here's how to get your entire VS Code setup in one click:

1. Open the Cursor Settings (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd>)
2. Navigate to General > Account
3. Under "VS Code Import", click the Import button

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b7288403921047910fed69f1ae19b3d4" data-og-width="1307" width="1307" data-og-height="359" height="359" data-path="images/get-started/vscode-import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2bb1ffd673292810c7f271f224ee1937 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f431f47576e4f9767eb062ca5a2e5f82 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a67b7c2e6f8150207350875f27ccf0a1 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6a08000a573992f18a90b07c4a62adb4 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e1ad4cd3868fba54ef75f84894a03797 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/vscode-import.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4335d8732c6c0b9039da434e9deac267 2500w" />
</Frame>

This will transfer your:

* Extensions
* Themes
* Settings
* Keybindings

### Manual Profile Migration

If you are moving between machines, or want more control over your settings, you can manually migrate your profile.

#### Exporting a Profile

1. On your VS Code instance, open the Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Search for "Preferences: Open Profiles (UI)"
3. Find the profile you want to export on the left sidebar
4. Click the 3-dot menu and select "Export Profile"
5. Choose to export it either to your local machine or to a GitHub Gist

#### Importing a Profile

1. On your Cursor instance, open the Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Search for "Preferences: Open Profiles (UI)"
3. Click the dropdown menu next to 'New Profile' and click 'Import Profile'
4. Either paste in the URL of the GitHub Gist or choose 'Select File' to upload a local file
5. Click 'Import' at the bottom of the dialog to save the profile
6. Finally, in the sidebar, choose the new profile and click the tick icon to active it

## Settings and Interface

### Settings Menus

<CardGroup>
  <Card title="Cursor Settings" icon="gear">
    Access via Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), then type "Cursor Settings"
  </Card>

  <Card title="VS Code Settings" icon="code">
    Access via Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd>{" "}

    * <kbd>P</kbd>), then type "Preferences: Open Settings (UI)"
  </Card>
</CardGroup>

### Version Updates

<Card title="Version Updates" icon="code-merge">
  We regularly rebase Cursor onto the latest VS Code version to stay current
  with features and fixes. To ensure stability, Cursor often uses slightly older
  VS Code versions.
</Card>

### Activity Bar Orientation

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7115db4ad44e29bf50cbb93d4a6766e6" data-og-width="478" width="478" data-og-height="186" height="186" data-path="images/get-started/activity-bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f6690aff02f6b23ec1c44d9b3addb0f5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6ad8ce9e58f8f5e2bc40cbae481b738b 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a93ec8cd4ecedb992a3c7775f5156095 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8cb513a6c916bb3164af6fc14451a0fa 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=149cef381de2fc65580dcaabd11cd5dd 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/activity-bar.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d77ca2579d38947010f406a7558a7380 2500w" />
</Frame>

We made it horizontal to optimize space for the AI chat interface. If you prefer vertical:

1. Open the Command Palette (<kbd>⌘</kbd>/<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>)
2. Search for "Preferences: Open Settings (UI)"
3. Search for `workbench.activityBar.orientation`
4. Set the value to `vertical`
5. Restart Cursor

---

← Previous: [JetBrains](./jetbrains.md) | [Index](./index.md) | Next: [Architectural Diagrams](./architectural-diagrams.md) →