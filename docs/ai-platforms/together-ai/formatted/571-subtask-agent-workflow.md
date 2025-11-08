---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Subtask Agent Workflow

An alternate and useful parallel workflow. This workflow begins with an LLM breaking down the task into subtasks that are dynamically determined based on the input. These subtasks are then processed in parallel by multiple worker LLMs. Finally, the orchestrator LLM synthesizes the workers' outputs into the final result.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3033de4327c6f5acedc35d5ff47290c4" alt="" data-og-width="4118" width="4118" data-og-height="1793" height="1793" data-path="images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5759ca55b49d3542d6c156be30ce9424 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a262112478ac7b9e3c8743aae475412d 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fac6dd08237e1ac86ef86aa6e5d1c0e6 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=93838a2ed1523e39f29aeb8bdfa6fda9 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=74ed0c8802e44e210036ef08dbfdbd95 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/7f624d5eb5f2ee0250b08b9c8b64e2a7239ca5ab16de50ca12f10fefeaf6adaa-parallel2.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bdf28b0ebd4db4539215318034cec012 2500w" />
</Frame>

>   **ℹ️ Info**
>
> ### Subtask Workflow Cookbook

  For a more detailed walk-through refer to the [notebook here](https://togetherai.link/agent-recipes-deep-dive-orchestrator) .

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
