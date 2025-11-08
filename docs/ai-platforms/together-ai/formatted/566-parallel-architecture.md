---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parallel Architecture

Run multiple LLMs in parallel and aggregate their solutions.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=563f3308591ef0da8d01a05de0cf83ed" alt="" data-og-width="3856" width="3856" data-og-height="1792" height="1792" data-path="images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c41987be307115e06c9f92515c7067ce 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9671d4da9e5a5ca9bceb7f94ce5089f6 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ab1c7b3726580483dafd0b3aa21f74b6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d10471ea6b7f34d639117129a5e9250c 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a077c1f04ec3bbb35626abcb6d46fce7 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7d8952be506a0da8656a5328b91fecb0c3d7b3a7a949b46d9e00002d07bd5f4f-parallel1.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4500e603783ef5326b1d6548383aa701 2500w" />
</Frame>

>   **ℹ️ Info**
>
> Notice that the same user prompt goes to each parallel LLM for execution. An alternate parallel workflow where this main prompt task is broken in sub-tasks is presented later.

>   **ℹ️ Info**
>
> ### Parallel Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-parallelization) .

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
