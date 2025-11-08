---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

**GPU Not Available**

If `nvidia-smi` doesn't show GPUs after `srun`:
```bash
  # Try requesting GPUs explicitly

  srun --gres=gpu:8 --nodes=1 --pty bash
```

**Out of Memory Errors**

If you encounter OOM errors during training:

1. Check that `NANOCHAT_BASE_DIR` is set to `/scratch`
2. Ensure no other processes are using GPU memory
3. The default batch sizes should work on H100 80GB

**Port Forwarding Connection Issues**

If you can't connect to the web UI:

1. Verify the pod name matches exactly: `kubectl -n slurm get pods`
2. Ensure the web server is running: check logs in the pod terminal
3. Try a different local port if 6818 is in use

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
