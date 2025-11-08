---
title: "Mcp: `notifications/initialized`"
description: "`notifications/initialized` section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## `notifications/initialized`


### `InitializedNotification`

<div class="tsd-signature"><span class="tsd-signature-keyword">interface</span> <span class="tsd-kind-interface">InitializedNotification</span> <span class="tsd-signature-symbol">\{</span><br />  <a class="tsd-kind-property" href="#">method</a><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">"notifications/initialized"</span><span class="tsd-signature-symbol">;</span><br />  <a class="tsd-kind-property" href="#initializednotification-params">params</a><span class="tsd-signature-symbol">?:</span> <span class="tsd-signature-symbol">\{</span> <span class="tsd-kind-property">\_meta</span><span class="tsd-signature-symbol">?:</span> <span class="tsd-signature-symbol">\{</span> <span class="tsd-signature-symbol">\[</span><span class="tsd-kind-index-signature">key</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span><span class="tsd-signature-symbol">]:</span> <span class="tsd-signature-type">unknown</span> <span class="tsd-signature-symbol">}</span><span class="tsd-signature-symbol">;</span> <span class="tsd-signature-symbol">\[</span><span class="tsd-kind-index-signature">key</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span><span class="tsd-signature-symbol">]:</span> <span class="tsd-signature-type">unknown</span> <span class="tsd-signature-symbol">}</span><span class="tsd-signature-symbol">;</span><br /><span class="tsd-signature-symbol">}</span></div><div class="tsd-comment tsd-typography"><p>This notification is sent from the client to the server after initialization has finished.</p> </div><section class="tsd-panel tsd-member tsd-is-inherited"><div data-typedoc-h="3" class="tsd-anchor-link" id="initializednotification-params"><code class="tsd-tag">Optional</code><span>params</span><a href="#initializednotification-params" aria-label="Permalink" class="tsd-anchor-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="assets/icons.svg#icon-anchor" /></svg></a></div><div class="tsd-signature"><span class="tsd-kind-property">params</span><span class="tsd-signature-symbol">?:</span> <span class="tsd-signature-symbol">\{</span> <span class="tsd-kind-property">\_meta</span><span class="tsd-signature-symbol">?:</span> <span class="tsd-signature-symbol">\{</span> <span class="tsd-signature-symbol">\[</span><span class="tsd-kind-index-signature">key</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span><span class="tsd-signature-symbol">]:</span> <span class="tsd-signature-type">unknown</span> <span class="tsd-signature-symbol">}</span><span class="tsd-signature-symbol">;</span> <span class="tsd-signature-symbol">\[</span><span class="tsd-kind-index-signature">key</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span><span class="tsd-signature-symbol">]:</span> <span class="tsd-signature-type">unknown</span> <span class="tsd-signature-symbol">}</span></div><div class="tsd-type-declaration"><div data-typedoc-h="4">Type declaration</div><ul class="tsd-parameters"><li class="tsd-parameter-index-signature"><div data-typedoc-h="5"><span class="tsd-signature-symbol">\[</span><span class="tsd-kind-parameter">key</span>: <span class="tsd-signature-type">string</span><span class="tsd-signature-symbol">]:</span> <span class="tsd-signature-type">unknown</span></div></li><li class="tsd-parameter"><div data-typedoc-h="5"><code class="tsd-tag">Optional</code><span class="tsd-kind-property">\_meta</span><span class="tsd-signature-symbol">?: </span><span class="tsd-signature-symbol">\{</span> <span class="tsd-signature-symbol">\[</span><span class="tsd-kind-index-signature">key</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span><span class="tsd-signature-symbol">]:</span> <span class="tsd-signature-type">unknown</span> <span class="tsd-signature-symbol">}</span></div><div class="tsd-comment tsd-typography"><p>See <a href="/specification/2025-06-18/basic/index#meta">General fields: <code>\_meta</code></a> for notes on <code>\_meta</code> usage.</p> </div><div class="tsd-comment tsd-typography" /></li></ul></div><aside class="tsd-sources"><p>Inherited from Notification.params</p></aside></section>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `notifications/cancelled`](./168-notificationscancelled.md)

**Next:** [`notifications/message` →](./170-notificationsmessage.md)
