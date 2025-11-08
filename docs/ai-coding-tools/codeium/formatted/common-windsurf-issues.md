---
title: "Common Windsurf Issues"
source: "https://docs.windsurf.com/troubleshooting/windsurf-common-issues"
---

# Common Windsurf Issues
Source: https://docs.windsurf.com/troubleshooting/windsurf-common-issues



### General FAQ

<AccordionGroup>
  <Accordion title="I subscribed to Pro so why am I stuck on the Free tier?">
    First, give it a few minutes to update. If that doesn't work, try logging out of Windsurf on the website, restarting your IDE, and logging back into Windsurf. Additionally, please make sure you have the latest version of Windsurf installed.
  </Accordion>

  <Accordion title="How do I cancel my Pro/Teams subscription?">
    You can cancel your paid plan by going to your Profile by clicking your icon on the top right of the [Windsurf website](https://windsurf.com/profile).

    To cancel your Pro subscription, navigate to the `Billing` page in the navigation panel on the left and click "Cancel Plan".

    To cancel your Teams subscription, navigate to the `Manage Team` page in the navigation panel on the left and click "Cancel Plan".
  </Accordion>

  <Accordion title="How do I disable code snippet telemetry?">
    As mentioned in our [security page](https://windsurf.com/security), you can opt out of code snippet telemetry by going to your settings [account settings](https://windsurf.com/settings). For more information, please visit our [Terms of Service](https://windsurf.com/terms-of-service-individual).
  </Accordion>

  <Accordion title="How do I delete my account?">
    You can delete your account by going to your settings [account settings](https://windsurf.com/settings), scrolling down and clicking on "Delete Account".

    <Note>If you are a member within an organization, please reach out to your administrator.</Note>
  </Accordion>

  <Accordion title="How do I request a feature?">
    You can vote, comment, and request features on our [feature request forum](https://codeium.canny.io/feature-requests).

    You can also reach out to us on Twitter/X! [@windsurf](https://x.com/windsurf)
  </Accordion>
</AccordionGroup>

### I'm experiencing rate limiting issues

We're subject to rate limits and unfortunately sometimes hit capacity for the premium models we work with. We are actively working on getting these limits increased and fairly distributing the capacity that we have!

This should not be an issue forever. If you get this error, please wait a few moments and try again.

### Pylance or Pyright isn't working / Python syntax highlighting is broken or subpar

We've gone ahead and developed a [Pyright extension specifically for Windsurf](/windsurf/advanced/#windsurf-extensions). Please search for "Windsurf Pyright" or paste `@id:codeium.windsurfPyright` into the extension search.

### How do I download Diagnostic logs to send to the Windsurf support team?

You can download diagnostic logs by going to your Cascade Panel, tapping the three dots in the top right corner, and then clicking "Download Diagnostics".

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b92c1e66d7d6b88e45147038adaae291" data-og-width="806" width="806" data-og-height="612" height="612" data-path="assets/windsurf/windsurf-download-diagnostics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=09afe7b42fc139c708989d828fe37897 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=48eadc9aaa349983cd70ac95be11d88a 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=28b3a95b07e2f2730eb458e609c7a26b 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=2dd140d8ad56ca5d8cff1f4b2e4bea91 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=07607f0f91a6f96ddaed9d5094866a2a 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-download-diagnostics.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=dc790fe0efd81f7f728d2c49cee15b40 2500w" />
</Frame>

### On MacOS, I see a pop-up: 'Windsurf' is damaged and cannot be opened.

This pop-up is due to a false positive in MacOS security features. You can usually resolve this by going to "System Settings -> Privacy & Security" and clicking "Allow" or "Open anyway" for Windsurf. If this fails or is not possible, try the following steps:

1. Ensure that Windsurf is placed under your `/Applications` folder and that you are running it from there.
2. Check your processor type: if your Mac has an Intel chip, make sure you have the Intel version. If it's Apple Silicon (like M1, M2 or M3), make sure you have the Apple Silicon version. You can select the processor type from the [Mac download page](https://windsurf.com/windsurf/download_mac).
3. Try redownloading the DMG and reinstalling from [the official download page](https://windsurf.com/windsurf/download_mac), as the failing security feature is usually triggered on download.
4. Make sure Windsurf (and the "Windsurf is Damaged" pop-up) is closed, and run `xattr -c "/Applications/Windsurf.app/"`.

### I received an error message about updates on Windows, or updates are not appearing on Windows.

For example:

> Updates are disabled because you are running the user-scope installation of Windsurf as Administrator.

We cannot auto-update Windsurf when it is run as Administrator. Please re-run Windsurf with User scope to update.

### What domains should I whitelist for network filters/firewalls, VPNs, or proxies?

If you're using any network filtering, firewalls, VPN services, or working in environments with restricted network access, you may experience connectivity issues with Windsurf. To ensure smooth operation, please whitelist the following domains in your network configuration:

* \*.codeium.com
* \*.windsurf.com
* \*.codeiumdata.com

### On Linux, Windsurf quietly doesn't launch, or crashes on launch

This is usually due to an Electron permissions issue, which VSCode also has, and is expected when using the tarball on Linux.

The easiest way to fix it is to run the following:

```bash  theme={null}
sudo chown root:root /path/to/windsurf/chrome-sandbox
sudo chown 4755 /path/to/windsurf/chrome-sandbox
```

You should then be able to launch Windsurf. You can also just run `windsurf` with the flag `--no-sandbox`, though we don't encourage this.

If this fails, then try the below.

### I received an error message saying 'Windsurf failed to start'

<Warning>Warning: deleting these folders will remove your conversation history and local settings!</Warning>

Delete the following folder:

Windows: `C:\Users\<YOUR_USERNAME>\.codeium\windsurf\cascade`

Linux/Mac: `~/.codeium/windsurf/cascade`

and try restarting the IDE.

### I received an error message about updates on Windows, or updates are not appearing on Windows.

An example:

> Updates are disabled because you are running the user-scope installation of Windsurf as Administrator.

We cannot auto-update Windsurf when it is run as Administrator. Please re-run Windsurf with User scope to update.

### My Cascade panel goes blank

Please reach out to us if this happens! A screen recording would be much appreciated. This can often be solved by clearing your chat history (`~/.codeium/windsurf/cascade`).

---

← Previous: [Gathering Logs](./gathering-logs.md) | [Index](./index.md) | Next: [Gathering Logs](./gathering-logs.md) →