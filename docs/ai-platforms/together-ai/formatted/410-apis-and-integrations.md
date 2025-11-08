---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## APIs and Integrations

### tcloud CLI

Download the CLI:

* [Mac](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-darwin-universal.tar.gz)
* [Linux](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-linux-amd64.tar.gz)

Authenticate via Google SSO:
```bash
tcloud sso login
```

Create a cluster:
```bash
tcloud cluster create my-cluster \ 
  --num-gpus 8 \
  --reservation-duration 1 \  
  --instance-type H100-SXM \ 
  --region us-central-8 \  
  --shared-volume-name my-volume \   
  --size-tib 1
```

Optionally, you can specify whether you want to provision reserved capacity or on-demand by using the `billing-type` field and setting its value to either `prepaid` (i.e. a reservation) or `on_demand`.
```bash
tcloud cluster create my-cluster \
  --num-gpus 8 \
  --billing-type prepaid \
  --reservation-duration 1 \
  --instance-type H100-SXM \
  --region us-central-8 \
  --shared-volume-name my-volume \
  --size-tib 1
```

Delete a cluster:
```bash
tcloud cluster delete <CLUSTER_UUID>
```

### REST API

All cluster management actions (create, scale, delete, storage, etc.) are available via REST API endpoints for programmatic control.

The API documentation can be found [here](https://docs.together.ai/api-reference/gpuclusterservice/create-gpu-cluster).

### Terraform Provider

Use the Together Terraform Provider to define clusters, storage, and scaling policies as code. This allows reproducible infrastructure management integrated with existing Terraform workflows.

### SkyPilot

You can orchestrate AI workloads on Instant Clusters using SkyPilot.

The following example shows how to use Together with SkyPilot and orchestrate `gpt-oss-20b` finetuning on it.

#### Use Together Instant Cluster with SkyPilot

1. ```bash
    uv pip install skypilot[kubernetes]
```

2. Launch a Together Instant Cluster with cluster type selected as Kubernetes

* Get the Kubernetes config for the cluster
* Save the kubeconfig to a file say `./together.kubeconfig`
* Copy the kubeconfig to your `~/.kube/config` or merge the Kubernetes config with your existing kubeconfig file.
```bash
  mkdir -p ~/.kube
  cp together-kubeconfig ~/.kube/config
```
  or
```bash
  KUBECONFIG=./together-kubeconfig:~/.kube/config kubectl config view --flatten > /tmp/merged_kubeconfig && mv /tmp/merged_kubeconfig ~/.kube/config    
```
  SkyPilot automatically picks up your credentials to the Together Instant Cluster.

3. Check that SkyPilot can access the Together Instant Cluster
```console
   $ sky check k8s
   Checking credentials to enable infra for SkyPilot.
     Kubernetes: enabled [compute]
       Allowed contexts:
       └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6: enabled.

   🎉 Enabled infra 🎉
     Kubernetes [compute]
       Allowed contexts:
       └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6

   To enable a cloud, follow the hints above and rerun: sky check
   If any problems remain, refer to detailed docs at: https://docs.skypilot.co/en/latest/getting-started/installation.html
```
   Your Together cluster is now accessible with SkyPilot.

4. Check the available GPUs on the cluster:
```console
   $ sky show-gpus --infra k8s
   Kubernetes GPUs
   Context: t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6
   GPU   REQUESTABLE_QTY_PER_NODE  UTILIZATION  
   H100  1, 2, 4, 8                8 of 8 free  
   Kubernetes per-node GPU availability
   CONTEXT                                                                              NODE                GPU   UTILIZATION  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-8ct86            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-fjqbt            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-hst5f            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  gpu-dp-gsd6b-k4m4x  H100  8 of 8 free  
```

#### Example: Finetuning gpt-oss-20b on the Together Instant Cluster

Launch a gpt-oss finetuning job on the Together cluster is now as simple as a single command:
```bash
sky launch -c gpt-together gpt-oss-20b.yaml
```

You can download the yaml file [here](https://github.com/skypilot-org/skypilot/tree/master/llm/gpt-oss-finetuning#lora-finetuning).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
