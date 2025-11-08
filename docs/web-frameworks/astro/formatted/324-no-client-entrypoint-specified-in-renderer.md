---
title: "No client entrypoint specified in renderer."
section: 324
---

# No client entrypoint specified in renderer.

> **NoClientEntrypoint**: `COMPONENT_NAME` component has a `client:CLIENT_DIRECTIVE` directive, but no client entrypoint was provided by `RENDERER_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro tried to hydrate a component on the client, but the renderer used does not provide a client entrypoint to use to hydrate.

**See Also:**

* [addRenderer option](/en/reference/integrations-reference/#addrenderer-option)
* [Hydrating framework components](/en/guides/framework-components/#hydrating-interactive-components)

---

[← Previous](323-cannot-use-server-islands-without-an-adapter.md) | [Index](index.md) | [Next →](index.md)
