---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1: Create an Instant Cluster

First, let's create an 8×H100 cluster to train nanochat.

1. Log into [api.together.ai](https://api.together.ai)
2. Click **GPU Clusters** in the top navigation menu
3. Click **Create Cluster**
4. Select **On-demand** capacity
5. Choose **8xH100** as your cluster size
6. Enter a cluster name (e.g., `nanochat-training`)
7. Select **Slurm on Kubernetes** as the cluster type
8. Choose your preferred region
9. Create a shared volume, min 1 TB storage
10. Click **Preview CLuster** and then "Confirm & Create"
    <Frame><img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=bb1efef1417b404fd8b8aaa50e74eb4c" alt="" data-og-width="3136" width="3136" data-og-height="2598" height="2598" data-path="images/guides/nanochat/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=81d379b89146ce7d7fe4706758bca46e 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=756f70fad503cc742dbde7f1e3079ceb 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=714ef6e20e08911c160c80246027cff0 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=8c9aba3aa3e0feed200d2153f0bdb63b 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=1f6ecc3ccba91861d4ddb2e0fe1e342d 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/1.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=e31df18d9275bcaf0e4b878794cd3353 2500w" /></Frame>

Your cluster will be ready in a few minutes. Once the status shows **Ready**, you can proceed to the next step.

>   **ℹ️ Info**
>
> For detailed information about Instant Clusters features and options, see the [Instant Clusters documentation](/docs/instant-clusters).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
