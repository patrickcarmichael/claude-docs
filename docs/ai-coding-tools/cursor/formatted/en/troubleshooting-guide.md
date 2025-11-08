---
title: "Troubleshooting Guide"
source: "https://docs.cursor.com/en/troubleshooting/troubleshooting-guide"
language: "en"
language_name: "English"
---

# Troubleshooting Guide
Source: https://docs.cursor.com/en/troubleshooting/troubleshooting-guide

Steps to fix issues and report bugs

Cursor issues can stem from extensions, app data, or system problems. Try these troubleshooting steps.

<CardGroup cols={1}>
  <Card horizontal title="Reporting an Issue" icon="bug" href="#reporting-an-issue">
    Steps to report an issue to the Cursor team
  </Card>
</CardGroup>

## Troubleshooting

<Steps>
  <Step title="Check network connectivity">
    First check if Cursor can connect to its services.

    **Run network diagnostics:** Go to `Cursor Settings` > `Network` and click `Run Diagnostics`. This tests your connection to Cursor's servers and identifies network issues affecting AI features, updates, or other online functionality.

    If diagnostics reveal connectivity issues, check firewall settings, proxy configuration, or network restrictions blocking Cursor's access.
  </Step>

  <Step title="Clearing extension data">
    For extension issues:

    **Disable all extensions temporarily:** Run `cursor --disable-extensions` from the command line. If issues resolve, re-enable extensions one by one to identify the problematic one.

    **Reset extension data:** Uninstall and reinstall problematic extensions to reset their stored data. Check settings for extension configuration that persists after reinstallation.
  </Step>

  <Step title="Clearing app data">
    <Warning>
      This deletes your app data, including extensions, themes, snippets, and installation-related data. Export your profile first to preserve this data.
    </Warning>

    Cursor stores app data outside the app for restoration between updates and reinstallations.

    To clear app data:

    **Windows:** Run these commands in Command Prompt:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **MacOS:** Run `sudo rm -rf ~/Library/Application\ Support/Cursor` and `rm -f ~/.cursor.json` in Terminal.

    **Linux:** Run `rm -rf ~/.cursor ~/.config/Cursor/` in Terminal.
  </Step>

  <Step title="Uninstalling Cursor">
    To uninstall Cursor:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Search "Add or Remove Programs" in Start Menu, find "Cursor", click "Uninstall".
      </Card>

      <Card horizontal title="MacOS" icon="apple">
        Open Applications folder, right-click "Cursor", select "Move to Trash".
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **For .deb packages:** `sudo apt remove cursor`

        **For .rpm packages:** `sudo dnf remove cursor` or `sudo yum remove cursor`

        **For AppImage:** Delete the Cursor.appimage file from its location.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Reinstalling Cursor">
    Reinstall from the [Downloads page](https://www.cursor.com/downloads). Without cleared app data, Cursor restores to its previous state. Otherwise, you get a fresh install.
  </Step>
</Steps>

## Reporting an Issue

If these steps don't help, report to the [forum](https://forum.cursor.com/).

<Card horizontal title="Cursor Forum" icon="message" href="https://forum.cursor.com/">
  Report a bug or issue on the Cursor forum
</Card>

For quick resolution, provide:

<CardGroup cols={2}>
  <Card title="Screenshot of Issue" icon="image">
    Capture a screenshot, redact sensitive information.
  </Card>

  <Card title="Steps to Reproduce" icon="list-check">
    Document exact steps to reproduce the issue.
  </Card>

  <Card title="System Information" icon="computer">
    Get system info from:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="Request IDs" icon="shield-halved" href="/en/troubleshooting/request-reporting">
    Click to view our guide on gathering request IDs
  </Card>

  <Card title="Console Errors" icon="bug">
    Check developer console: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Logs" icon="file-lines">
    Access logs: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [Getting a Request ID](./getting-a-request-id.md) | [Index](./index.md) | Next: [Welcome](./welcome.md) →