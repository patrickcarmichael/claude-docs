---
title: "Astro.clientAddress is not available in prerendered pages."
section: 349
---

# Astro.clientAddress is not available in prerendered pages.

> **StaticClientAddressNotAvailable**: `Astro.clientAddress` is only available on pages that are server-rendered.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.clientAddress` property is only available when [Server-side rendering](/en/guides/on-demand-rendering/) is enabled.

To get the user’s IP address in static mode, different APIs such as [Ipify](https://www.ipify.org/) can be used in a [Client-side script](/en/guides/client-side-scripts/) or it may be possible to get the user’s IP using a serverless function hosted on your hosting provider.

**See Also:**

* [Enabling SSR in Your Project](/en/guides/on-demand-rendering/)
* [Astro.clientAddress](/en/reference/api-reference/#clientaddress)

---

[← Previous](348-sessions-cannot-be-used-with-an-adapter-that-doesnt-support-server-output.md) | [Index](index.md) | [Next →](index.md)
