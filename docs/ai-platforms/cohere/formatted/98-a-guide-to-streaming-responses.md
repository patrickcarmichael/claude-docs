---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## A Guide to Streaming Responses

> The document explains how the Chat API can stream events like text generation in real-time.

The [Chat API](/reference/chat) is capable of streaming events (such as text generation) as they come. This means that partial results from the model can be displayed within moments, even if the full generation takes longer.

You're likely already familiar with streaming. When you ask the model a question using [the Cohere playground](https://dashboard.cohere.com/playground), the interface doesn't output a single block of text, instead it *streams* the text out a few words at a time. In many user interfaces enabling streaming improves the user experience by lowering the perceived latency.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
