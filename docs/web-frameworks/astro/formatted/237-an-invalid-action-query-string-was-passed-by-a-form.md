---
title: "An invalid Action query string was passed by a form."
section: 237
---

# An invalid Action query string was passed by a form.

Deprecated

Deprecated since version 4.13.2.

> **ActionsUsedWithForGetError**: Action ACTION\_NAME was called from a form using a GET request, but only POST requests are supported. This often occurs if `method="POST"` is missing on the form.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Action was called from a form using a GET request, but only POST requests are supported. This often occurs if `method="POST"` is missing on the form.

**See Also:**

* [Actions RFC](https://github.com/withastro/roadmap/blob/actions/proposals/0046-actions.md)

---

[← Previous](236-action-handler-returned-invalid-data.md) | [Index](index.md) | [Next →](index.md)
