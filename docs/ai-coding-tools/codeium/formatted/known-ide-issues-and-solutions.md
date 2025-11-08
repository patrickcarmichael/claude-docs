---
title: "Known IDE issues and solutions"
source: ""
---

# Known IDE issues and solutions

## e.split is not defined

You are using an unsupported VS Code version, please update to a supported version and try again. You can find a list of supported versions [here](/plugins/compatibility).

## Using the wrong API Server

If a user changes their API Server/Portal URL in their **workspace** settings, this will override their user settings and may result in an error where the extension is communicating with the wrong API server.

Make sure that your API Server/Portal URL is set correctly and not overridden accidentally by the workspace settings.

## Not seeing Codeium Chat responses

If you are trying to send messages to Codeium chat but not seeing responses, check if you can cancel the response. If you are unable to cancel the response, this means that the response was completed but not displayed. This can happen if the Chat Web Server loses connection to the extension. Reloading VS Code and opening the Codeium Chat panel again should show the responses.

## Unable to read file .../package.json

```
Unable to read file .../.vscode/extensions/codeium.codeium-<version>/package.json 
```

If the above error shows up in the Codeium logs, try deleting the extension folder (.../.vscode/extensions/codeium.codeium-\<version>) and reinstall the extension.

## VS Code Enterprise Updater Loop

"Codeium Enterprise Updated" every time you open VSCode, try restarting all extensions

1. Open the command palette ( CTRL + SHIFT + P )
2. Run 'Disable All Installed Extensions'
3. Run 'Enable all Extensions'
4. Restart VS Code

Make sure all extensions are enabled again.

## Enterprise updater doesn't install Codeium extension

The Enterprise updater is installed, but no extension is being downloaded or installed in VSCode. No extension logs option is available in VSCode output window drop down. The only available log you can see is:

```
[info] ExtensionService#_doActivateExtension Codeium.codeium-enterprise-updater, startup: false, activationEvent: 'onStartupFinished'
```

If you have previously disabled the Codeium extension and later uninstalled it, VSCode will not clear the disabled flag.

In order to do so manually:

1. Open the command palette ( CTRL + SHIFT + P )
2. Run 'Codeium Enterprise: Reset'
3. Select "Help" from the popup
4. Select "Show Disabled Extensions"
5. Re-enable your Codeium Extension

## Proxy / Network Issues

Unchecking `Detect Proxy` in Codeium settings in VSCode can sometimes resolve issues where the extension is incorrectly attempting to use a proxy.

## Certificate Issues

If you encounter the following errors:

```
ConnectError: [internal] unable to get issuer certificate
```

```
[ERROR]: [internal] unable to verify the first certificate
```

```
tls: failed to verify certificate: x509: "<yourdomainurl>" certificate is not standards compliant
```

This suggests that the Codeium extension is unable to trust the TLS connection to your enterprise portal / API server because it does not trust the certificate being presented. This either means that the certificate presented by the Codeium deployment is untrusted or a certificate presented by a corporate proxy intercepting the request is untrusted.

In either case, the most preferable solution is to ensure that the root certificate that signed this certificate is properly installed on end-user machines in the appropriate location. VS Code and most other IDEs load certificates from the operating system's default location.

Your certificate is issued and managed by your local IT or Admin team. Please reach out to them for assistance with installing the necessary certificates on your system.

It is important that the full certificate chain is being presented from wherever TLS is being terminated. Oftentimes, if only the leaf certificate is presented, VS Code and other IDEs are unable to verify its authenticity because they are not aware of the intermediate certificate which validates the leaf certificate and is validated by the root certificate. Browsers are often able to work around this issue as users will likely have encountered a different website that does present the full certificate chain, so the intermediate cert is seen and cached, but applications like VS Code don't have this advantage.

The Network Proxy Text VS Code extension is useful for debugging certificate issues.

---

← Previous: [How to reset or change your Enterprise URL](./how-to-reset-or-change-your-enterprise-url.md) | [Index](./index.md) | Next: [Gathering Logs](./gathering-logs.md) →