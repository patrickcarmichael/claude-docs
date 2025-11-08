---
title: "Common Issues"
source: "https://docs.cursor.com/en/troubleshooting/common-issues"
language: "en"
language_name: "English"
---

# Common Issues
Source: https://docs.cursor.com/en/troubleshooting/common-issues

Solutions for common problems and FAQs

Below are common issues and their solutions.

### Networking Issues

First, check your network connectivity. Go to `Cursor Settings` > `Network` and click `Run Diagnostics`. This will test your connection to Cursor's servers and help identify any network-related issues that might be affecting AI features, updates, or other online functionality.

Cursor relies on HTTP/2 for AI features because it handles streamed responses efficiently. If your network doesn't support HTTP/2, you may experience indexing failures and AI feature issues.

This occurs on corporate networks, VPNs, or when using proxies like Zscaler.

To resolve this, enable HTTP/1.1 fallback in app settings (not Cursor settings): press `CMD/CTRL + ,`, search for `HTTP/2`, then enable `Disable HTTP/2`. This forces HTTP/1.1 usage and resolves the issue.

We plan to add automatic detection and fallback.

### Resource Issues (CPU, RAM, etc.)

High CPU or RAM usage can slow your machine or trigger resource warnings.

While large codebases require more resources, high usage typically stems from extensions or settings issues.

<Note>
  If you are seeing a low RAM warning on **MacOS**, please note that there is a bug for some users that can show wildly incorrect values. If you are seeing this, please open the Activity Monitor and look at the "Memory" tab to see the correct memory usage.
</Note>

If you're experiencing high CPU or RAM usage, try these steps:

<AccordionGroup>
  <Accordion title="Check Your Extensions">
    Extensions can impact performance.

    The Extension Monitor shows resource consumption for all your installed and built-in extensions.

    Enable the extension monitor from `Settings` > `Application` > `Experimental` and toggle `Extension Monitor: Enabled`. This will prompt you to restart Cursor.

    Open it: `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor runs your extensions in one or more **extension hosts**. Usually, most of your extensions will run in the same extension host, which means an extension consuming a lot of CPU time can suffocate its neighboring extensions!

    The Extension Monitor will show:

    * Every long-lived process launched by an extension (MacOS and Linux only).
    * **% Ext Host**: The percentage of total extension host time consumed by this extension. Helps identify which extensions are using the most time relative to others.
    * **Max Blocking**: An extensions's longest continuous block of execution, per monitoring interval.
    * **% CPU**:
      * For extensions: The percentage of total CPU usage attributed to the extension's code.
      * For processes: The percentage of total CPU usage attributed to the launched process (MacOS and Linux only).
    * **Memory**:
      * For extensions: The amount of JS heap memory used by the extension's code (external allocations not counted).
      * For processes: The amount of system memory used by the launched process (MacOS and Linux only).

    You can also test by running `cursor --disable-extensions` from the command line. If performance improves, re-enable extensions one by one to identify problematic ones.

    Try Extension Bisect to identify problematic extensions. Read more [here](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect). Note: this works best for immediate issues, not gradual performance degradation.
  </Accordion>

  <Accordion title="Use the Process Explorer">
    The Process Explorer shows which processes consume resources.

    Open it: Command Palette (`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    Review processes under:

    * **`extensionHost`**: Extension-related issues
    * **`ptyHost`**: Terminal resource consumption

    The Process Explorer displays each terminal and its running commands for diagnosis.

    For other high-usage processes, report to the [forum](https://forum.cursor.com/).
  </Accordion>

  <Accordion title="Monitor System Resources">
    Use your operating system's monitoring tools to determine if the issue is Cursor-specific or system-wide.
  </Accordion>

  <Accordion title="Testing a Minimal Installation">
    If issues persist, test a minimal Cursor installation.
  </Accordion>
</AccordionGroup>

## General FAQs

<AccordionGroup>
  <Accordion title="I see an update on the changelog but Cursor won't update">
    New updates use staged rollouts - randomly selected users receive updates first. Expect your update within a few days.
  </Accordion>

  <Accordion title="I have issues with my GitHub login in Cursor / How do I log out of GitHub in Cursor?">
    Use `Sign Out of GitHub` from the command palette `Ctrl/⌘ + Shift + P`.
  </Accordion>

  <Accordion title="I can't use GitHub Codespaces">
    GitHub Codespaces isn't supported yet.
  </Accordion>

  <Accordion title="I have errors connecting to Remote SSH">
    SSH to Mac or Windows machines isn't supported. For other issues, report to the [forum](https://forum.cursor.com/) with logs.
  </Accordion>

  <Accordion title="SSH Connection Problems on Windows">
    If you see "SSH is only supported in Microsoft versions of VS Code":

    1. Uninstall Remote-SSH:
       * Open Extensions view (`Ctrl + Shift + X`)
       * Search "Remote-SSH"
       * Click gear icon → "Uninstall"

    2. Install Anysphere Remote SSH:
       * Open Cursor marketplace
       * Search "SSH"
       * Install the Anysphere Remote SSH extension

    3. After installation:
       * Close all VS Code instances with active SSH connections
       * Restart Cursor
       * Reconnect via SSH

    Verify your SSH configuration and keys are properly set up.
  </Accordion>

  <Accordion title="Cursor Tab and Inline Edit do not work behind my corporate proxy">
    Cursor Tab and Inline Edit use HTTP/2 for lower latency and resource usage. Some corporate proxies (e.g., Zscaler) block HTTP/2. Fix by setting `"cursor.general.disableHttp2": true` in settings (`Cmd/Ctrl + ,`, search `http2`).
  </Accordion>

  <Accordion title="I just subscribed to Pro but I'm still on the free plan in the app">
    Log out and back in from Cursor Settings.
  </Accordion>

  <Accordion title="When will my usage reset again?">
    Pro subscribers: Click `Manage Subscription` in the [Dashboard](https://cursor.com/dashboard) to view your renewal date.

    Free users: Check your first Cursor email date. Usage resets monthly from that date.
  </Accordion>

  <Accordion title="My Chat/Composer history disappeared after an update">
    Low disk space may cause Cursor to clear historical data during updates. To prevent this:

    1. Maintain sufficient free disk space before updating
    2. Clean up unnecessary system files regularly
    3. Back up important conversations before updating
  </Accordion>

  <Accordion title="How do I uninstall Cursor?">
    Follow [this guide](https://code.visualstudio.com/docs/setup/uninstall). Replace "VS Code" or "Code" with "Cursor", and ".vscode" with ".cursor".
  </Accordion>

  <Accordion title="How do I delete my account?">
    Click `Delete Account` in the [Dashboard](https://cursor.com/dashboard). This permanently deletes your account and all associated data.
  </Accordion>

  <Accordion title="How do I open Cursor from the command line?">
    Run `cursor` in your terminal. If the command is missing:

    1. Open command palette `⌘⇧P`
    2. Type `install command`
    3. Select `Install 'cursor' command` (optionally install `code` command to override VS Code's)
  </Accordion>

  <Accordion title="Unable to Sign In to Cursor">
    If clicking Sign In redirects to cursor.com but doesn't sign you in, disable your firewall or antivirus software - they may block the sign-in process.
  </Accordion>

  <Accordion title="Suspicious Activity Message">
    Due to recent increased misuse of our system, your request may have been blocked as a security measure. Here's how to resolve this:

    First, check your VPN. If you're using one, try turning it off, as VPNs can sometimes trigger our security systems.

    If that doesn't resolve it, you can try:

    * Creating a new chat
    * Waiting a bit and trying again later
    * Creating a new account using Google or GitHub authentication
    * Upgrading to Cursor Pro
  </Accordion>
</AccordionGroup>

---

← Previous: [MCP Servers](./mcp-servers.md) | [Index](./index.md) | Next: [Getting a Request ID](./getting-a-request-id.md) →