---
title: "Caching overview"
source: https://docs.streamlit.io/develop/concepts/architecture/caching
section: 22
---

# Caching overview

Source: https://docs.streamlit.io/develop/concepts/architecture/caching


Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes development super easy. But it comes with two major challenges:

1. Long-running functions run again and again, which slows down your app.
2. Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.

But don't worry! Streamlit lets you tackle both issues with its built-in caching mechanism. Caching stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns. Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use [Session State](/develop/concepts/architecture/session-state) instead.

<Collapse title="Table of contents">{true}&gt;

1. [Minimal example](#minimal-example)
2. [Basic usage](#basic-usage)
3. [Advanced usage](#advanced-usage)
4. [Migrating from st.cache](#migrating-from-stcache)

</Collapse>

---

[← Previous](21-the-app-chrome.md) | [Index](index.md) | [Next →](index.md)
