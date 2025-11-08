---
title: "Mcp: `notifications/resources/updated`"
description: "`notifications/resources/updated` section of Mcp documentation"
source: "https://modelcontextprotocol.io/clients"
last_updated: "2025-11-08"
---

## `notifications/resources/updated`


### `ResourceUpdatedNotification`

<div class="tsd-signature"><span class="tsd-signature-keyword">interface</span> <span class="tsd-kind-interface">ResourceUpdatedNotification</span> <span class="tsd-signature-symbol">\{</span><br />  <a class="tsd-kind-property" href="#">method</a><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">"notifications/resources/updated"</span><span class="tsd-signature-symbol">;</span><br />  <a class="tsd-kind-property" href="#resourceupdatednotification-params">params</a><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-symbol">\{</span> <span class="tsd-kind-property">uri</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span> <span class="tsd-signature-symbol">}</span><span class="tsd-signature-symbol">;</span><br /><span class="tsd-signature-symbol">}</span></div><div class="tsd-comment tsd-typography"><p>A notification from the server to the client, informing it that a resource has changed and may need to be read again. This should only be sent if the client previously sent a resources/subscribe request.</p> </div><section class="tsd-panel tsd-member"><div data-typedoc-h="3" class="tsd-anchor-link" id="resourceupdatednotification-params"><span>params</span><a href="#resourceupdatednotification-params" aria-label="Permalink" class="tsd-anchor-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="assets/icons.svg#icon-anchor" /></svg></a></div><div class="tsd-signature"><span class="tsd-kind-property">params</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-symbol">\{</span> <span class="tsd-kind-property">uri</span><span class="tsd-signature-symbol">:</span> <span class="tsd-signature-type">string</span> <span class="tsd-signature-symbol">}</span></div><div class="tsd-type-declaration"><div data-typedoc-h="4">Type declaration</div><ul class="tsd-parameters"><li class="tsd-parameter"><div data-typedoc-h="5"><span class="tsd-kind-property">uri</span><span class="tsd-signature-symbol">: </span><span class="tsd-signature-type">string</span></div><div class="tsd-comment tsd-typography"><p>The URI of the resource that has been updated. This might be a sub-resource of the one that the client actually subscribed to.</p> </div><div class="tsd-comment tsd-typography" /></li></ul></div><aside class="tsd-sources"><p>Overrides Notification.params</p></aside></section>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `notifications/resources/list_changed`](./173-notificationsresourceslist_changed.md)

**Next:** [`notifications/roots/list_changed` →](./175-notificationsrootslist_changed.md)
