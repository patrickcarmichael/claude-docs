---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 5: Configure Cache Directory

To optimize data loading performance, set the nanochat cache directory to the `/scratch` volume, which is optimized for high-throughput I/O:
```bash
  export NANOCHAT_BASE_DIR="/scratch/$USER/nanochat/.cache/nanochat"
```

This needs to be changed inside the `speedrun.sh` file and ensures that dataset streaming, checkpoints, and intermediate artifacts don't bottleneck your training.

>   **ℹ️ Info**
>
> This step is critical and without it, during training, you'll notice that your FLOP utilization is only \~13% instead of \~50%. This is due to dataloading bottlenecks.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
