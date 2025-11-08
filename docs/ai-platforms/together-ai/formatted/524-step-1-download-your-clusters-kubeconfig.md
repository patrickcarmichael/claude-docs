---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1: Download Your Cluster's Kubeconfig

While training is running (or after it completes), download your cluster's kubeconfig from the Together AI dashboard. This will allow you to access the cluster using kubectl.

1. Go to your cluster in the Together AI dashboard
2. Click on the **View Kubeconfig** button
3. Copy and save the kubeconfig file to your local machine (e.g., `~/.kube/nanochat-cluster-config`)

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=c879f73961de55cfb06f4dd83602260b" alt="" data-og-width="3136" width="3136" data-og-height="2598" height="2598" data-path="images/guides/nanochat/6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=0d621d1a52843df9bd39fa7496395be1 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=e89097fbb4bec1503def8ed8abec5507 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=fbafafb52a1b45a98b7f5f97acd50fc3 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=44fb0683eee383a3cf484fc2ab48a175 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4306e9cd6c86e38925364df871826827 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/6.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=37e57273e371c246aa1a3572b836270f 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
