---
title: "Invalid type returned by Astro page."
section: 331
---

# Invalid type returned by Astro page.

> Route returned a `RETURNED_VALUE`. Only a Response can be returned from Astro files.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Only instances of [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) can be returned inside Astro files.

pages/login.astro

```astro
---
return new Response(null, {
 status: 404,
 statusText: 'Not found'
});


// Alternatively, for redirects, Astro.redirect also returns an instance of Response
return Astro.redirect('/login');
---
```jsx
**See Also:**

* [Response](/en/guides/on-demand-rendering/#response)

---

[← Previous](330-prerendered-routes-arent-supported-when-internationalization-domains-are-enabled.md) | [Index](index.md) | [Next →](index.md)
