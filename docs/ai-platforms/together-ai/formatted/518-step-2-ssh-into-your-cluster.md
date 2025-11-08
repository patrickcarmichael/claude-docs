---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: SSH into Your Cluster

From the Instant Clusters UI, you'll find SSH access details for your cluster.

A command like the one below can be copied from the instant clusters dashboard.
<Frame><img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4a050ff646ed47e2170097444194b3f3" alt="" data-og-width="3136" width="3136" data-og-height="2598" height="2598" data-path="images/guides/nanochat/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=1471b86739a04513ac1e78c1afa1801a 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=dc8482f041ce00798f581a62db347b4f 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=33db19c5345c30d7151f222c1a170842 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=a7805b729ed28bd5de76e61e9451bd63 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=574c4f780ef4f2a828cad63a719d87dd 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/2.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=398b359f5aa96fbf55a545a64b0f913e 2500w" /></Frame>
```bash
  ssh <username>@<cluster-hostname>
```

You can also use `ssh -o ServerAliveInterval=60` - it sends a ping to the ssh server every 60s, so it keeps the TCP ssh session alive, even if there's no terminal input/output for a long time during training.

Once connected, you'll be in the login node of your Slurm cluster.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
