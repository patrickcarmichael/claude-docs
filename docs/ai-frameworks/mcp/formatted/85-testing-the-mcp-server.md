---
title: "Mcp: Testing the MCP Server"
description: "Testing the MCP Server section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## Testing the MCP Server


For testing purposes, we will be using [Visual Studio Code](https://code.visualstudio.com), but any client that supports MCP and the new authorization specification will fit.

Press <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> and select **MCP: Add server...**. Select **HTTP** and enter `http://localhost:3000`. Give the server a unique name to be used inside Visual Studio Code. In `mcp.json` you should now see an entry like this:

```json  theme={null}
"my-mcp-server-18676652": {
  "url": "http://localhost:3000",
  "type": "http"
}
```

On connection, you will be taken to the browser, where you will be prompted to consent to Visual Studio Code having access to the `mcp:tools` scope.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=d5183fb7c257993aed1b2246f0bbbb27" alt="Keycloak consent form for VS Code." data-og-width="1915" width="1915" data-og-height="1536" height="1536" data-path="images/tutorial-authorization/keycloak-vscode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=93bb132878b75189c0cf198a59d3b053 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=155520f0a1b88422247d9910cb59899f 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=4fd24398061374fd940b05d97701dcbc 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=e949784fc78e1f44bc8d3edeb218220b 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=30fc4dbf14307aac8a2ae938b112ef5b 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/keycloak-vscode.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=3a0b543da5988dd95b1a447b138c83be 2500w" />
</Frame>

After consenting, you will see the tools listed right above the server entry in `mcp.json`.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=f7c34d1bf115fe6934e01b4a5a91168b" alt="Tools listed in VS Code." data-og-width="496" width="496" data-og-height="160" height="160" data-path="images/tutorial-authorization/tools-vs-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=9e66d87c84323d4efafb9fa80b58b611 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=4b2ef221709a1696272241badcfd7c42 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=ce16053621cc5b24a5f5a83fe541feaa 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=59f05ee1ee685b60b0b3fe884cd732f8 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=ea1afa55bd8f26278d2317ef0ef1a8fb 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=1f6dd6a4d23ee579f73421689c4c2daa 2500w" />
</Frame>

You will be able to invoke individual tools with the help of the `#` sign in the chat view.

<Frame>
  <img src="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=76cbef68e48821a3c5467bd20c7e89fe" alt="Invoking MCP tools in VS Code." data-og-width="1276" width="1276" data-og-height="396" height="396" data-path="images/tutorial-authorization/tools-vs-code-invoke.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=280&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=7f5687389fe8bf48369a45738ec07795 280w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=560&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=dcc4a1857264bda9f2566e50db51704f 560w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=840&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=2774a73e612220975ee6d491430b9ee5 840w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=1100&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=014f88a40adddb9faf5f93306dea376c 1100w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=1650&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=d938978e4507cd933695cce01ee49901 1650w, https://mintcdn.com/mcp/sAd4SGUO-cEUqgzn/images/tutorial-authorization/tools-vs-code-invoke.png?w=2500&fit=max&auto=format&n=sAd4SGUO-cEUqgzn&q=85&s=0250d29b2e115324e0b94a4796938bad 2500w" />
</Frame>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Implementation Example](./84-implementation-example.md)

**Next:** [Common Pitfalls and How to Avoid Them →](./86-common-pitfalls-and-how-to-avoid-them.md)
