---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced MoA example

In the previous example, we went over how to implement MoA with 2 layers (4 LLMs answering and one LLM aggregating). However, one strength of MoA is being able to go through several layers to get an even better response. In this example, we'll go through how to run MoA with 3+ layers.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0d8b3ab35cd1c934702082358f0aea7f" alt="" data-og-width="2036" width="2036" data-og-height="926" height="926" data-path="images/guides/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d5d56bcaa112033fd024a43c6873ffd4 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=476fbdc4c0e77ab6e281d11535799e85 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=838eb9b5f26594a63dab6c57effc376e 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=436b698543fd544c09b24ac4a0b4aec8 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8f99043f81c6b16b8581441f3ad2205e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/2.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=19b41287a5693e2863443f3becfa36dd 2500w" />
</Frame>
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
