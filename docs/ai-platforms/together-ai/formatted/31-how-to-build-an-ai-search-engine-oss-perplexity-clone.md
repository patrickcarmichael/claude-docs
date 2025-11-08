---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How To Build An AI Search Engine (OSS Perplexity Clone)

Source: https://docs.together.ai/docs/ai-search-engine

How to build an AI search engine inspired by Perplexity with Next.js and Together AI

[TurboSeek](https://www.turboseek.io/) is an app that answers questions using [Together AI’s](https://www.together.ai/) open-source LLMs. It pulls multiple sources from the web using Exa's API, then summarizes them to present a single answer to the user.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8e4b3476c21b5b285796f863c8ad8753" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b1b2203b00c3f1227b8a062537b4b5dd 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=64cdf40461d0d4e0c8ec94ea8b66ae23 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=19c3d34f6f9c61bc625a46b401fc1b63 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=2c7a2ee11b344af1fac0de3ea1d4d813 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=5c4f33b1542b6f4f04ee54063c86171f 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/4.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9c6d49f9aa68d54e59a6f3c91273beb3 2500w" />
</Frame>

In this post, you’ll learn how to build the core parts of TurboSeek. The app is [open-source](https://github.com/Nutlope/turboseek/) and built with Next.js and Tailwind, but Together’s API can be used with any language or framework.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
