---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cluster Storage

Source: https://docs.together.ai/docs/cluster-storage


A Together GPU Cluster has 3 types of storage:

### 1. Local disks

Each server has NVME drives which can be used for high speed local read/writes.

### 2. Shared `/home` folder

The `/home` folder is shared across all nodes, mounted as an NFS volume from the head node. This should be used for code, configs, logs, etc. It should not be used for training data or checkpointing, as it is slower.

We recommend logging into the Slurm head node first to properly set up your user folder with the right permissions.

### 3. Shared remote attached storage

The GPU nodes all have a mounted volume from a high-speed storage cluster, which is useful for reading training data and writing checkpoints to/from a central location.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
