---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Compute Access

You can run workloads on Instant Clusters using Kubernetes or Slurm-on-Kubernetes.

### Kubernetes

Use `kubectl` to submit jobs, manage pods, and interact with your cluster. See [Quickstart](#quickstart) for setup details.

### Slurm Direct SSH

For HPC workflows, you can enable Slurm-on-Kubernetes:

* Directly SSH into a Slurm node.
* Use familiar Slurm commands (`sbatch`, `srun`, etc.) to manage distributed training jobs.

This provides the flexibility of traditional HPC job scheduling alongside Kubernetes.

#### SSH to Slurm Login Pod

Please note that at this time, you must add your SSH key to your account prior to deploying a cluster in order for the key to register
in your LDAP server.

Tip: When you click your cluster in the Together Cloud UI, the Cluster details page shows copy-ready Slurm commands tailored to your cluster (for example, `squeue`, `sinfo`, `srun`, `sbatch`). Use these to quickly verify connectivity and submit jobs.

The hostname of worker pods will always be the name of the node with `.slurm.pod` at the end. For instance, `gpu-dp-hmqnh-nwlnj.slurm.pod`.

The hostname of the login pod, which is the place you will likely wish to start most jobs and routines from is always `slurm-login`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
