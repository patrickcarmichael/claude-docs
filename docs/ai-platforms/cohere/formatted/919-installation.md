---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Installation

First, install the OpenAI SDK and import the package.

Then, create a client and configure it with the compatibility API base URL and your Cohere API key.

<Tabs>
  <Tab title="Python">
```bash
    pip install openai
```
```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )
```
  </Tab>

  <Tab title="TypeScript">
```bash
    npm install openai
```
```typescript TYPESCRIPT

    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
    });
```
  </Tab>
</Tabs>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
