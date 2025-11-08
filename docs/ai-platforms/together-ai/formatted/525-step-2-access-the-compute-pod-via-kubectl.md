---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Access the Compute Pod via kubectl

From your **local machine**, set up kubectl access to your cluster:
```bash
  # Set the KUBECONFIG environment variable

  export KUBECONFIG=/path/to/nanochat-cluster-config

  # List pods in the slurm namespace

  kubectl -n slurm get pods
```

You should see your Slurm compute pods listed. Identify the production pod where your training ran:
```bash
  # Example output:

  # NAME                              READY   STATUS    RESTARTS   AGE

  # slurm-compute-production-abc123   1/1     Running   0          2h

  # Exec into the pod

  kubectl -n slurm exec -it <your-slurm-compute-production-pod> -- /bin/bash
```

Once inside the pod, navigate to the nanochat directory:
```bash
  cd /path/to/nanochat
```

**Set Up Python Virtual Environment**

Inside the compute pod, set up the Python virtual environment using `uv`:
```bash
  # Install uv (if not already installed)

  command -v uv &> /dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh

  # Create a local virtual environment

  [ -d ".venv" ] || uv venv

  # Install the repo dependencies with GPU support

  uv sync --extra gpu

  # Activate the virtual environment

  source .venv/bin/activate
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
