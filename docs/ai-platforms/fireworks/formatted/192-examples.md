---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

<Tabs>
  <Tab title="Draft model">
    Use a smaller model to speed up generation:
```bash
    firectl create deployment accounts/fireworks/models/llama-v3p3-70b-instruct \
      --draft-model="accounts/fireworks/models/llama-v3p2-1b-instruct" \
      --draft-token-count=4
```
  </Tab>

  <Tab title="N-gram speculation">
    Use input history for speculation (no draft model needed):
```bash
    firectl create deployment accounts/fireworks/models/llama-v3p3-70b-instruct \
      --ngram-speculation-length=3 \
      --draft-token-count=4
```
  </Tab>
</Tabs>

<Tip>
  Fireworks also supports [Predicted Outputs](/guides/predicted-outputs) which works in addition to model-based speculative decoding.
</Tip>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
