---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 4: Port Forward to Access the UI

In a **new terminal window on your local machine**, set up port forwarding to access the web UI:
```bash
  # Set the KUBECONFIG (if not already set in this terminal)

  export KUBECONFIG=/path/to/nanochat-cluster-config

  # Forward port 8000 from the pod to local port 6818

  kubectl -n slurm port-forward <your-slurm-compute-production-pod> 6818:8000
```

The port forwarding will remain active as long as this terminal session is open.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
