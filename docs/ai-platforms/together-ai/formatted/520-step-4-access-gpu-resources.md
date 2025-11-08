---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 4: Access GPU Resources

Use Slurm's `srun` command to allocate 8 GPUs for your training job:
```bash
  srun --gres=gpu:8 --pty bash
```

This command requests 8 GPUs and gives you an interactive bash session on a compute node. Once you're on the compute node, verify GPU access:
```bash
  nvidia-smi
```

You should see all 8 H100 GPUs listed with their memory and utilization stats like below.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=93378a3fae8db4f27c53c61d4f3c86aa" alt="" data-og-width="2222" width="2222" data-og-height="2196" height="2196" data-path="images/guides/nanochat/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=2bf0af7074878754f2b74d8aa0685fee 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=8768e758fced8fb71b506e8ca55b058a 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3d7cec0dac1089bfd6f4969c5270d341 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=ce3754eeb833e577bb88c111534c5271 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=1bb8b8a7adaf39b46db4a7d3124d58f3 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/3.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=abab57e1deafde093756bdaa520ee6d0 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
