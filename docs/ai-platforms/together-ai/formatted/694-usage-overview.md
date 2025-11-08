---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage overview

Together AI has created sessions to measure TCI usage.

A session is an active code execution environment that can be called to execute code, they can be used multiple times and have a lifespan of 60 minutes.

Typical TCI usage follows this workflow:

1. Start a session (create a TCI instance).
2. Call that session to execute code; TCI outputs `stdout` and `stderr`.
3. Optionally reuse an existing session by calling its `session_id`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
