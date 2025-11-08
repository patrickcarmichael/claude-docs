---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quickstart: Create an Instant Cluster

1. Log into api.together.ai.
2. Click **GPU Clusters** in the top navigation menu.
3. Click **Create Cluster**.
4. Choose whether you want **Reserved** capacity or **On-demand**, based on your needs.
5. Select the **cluster size**, for example `8xH100`.
6. Enter a **cluster name**.
7. Choose a **cluster type** either Kubernetes or Slurm.
8. Select a **region**.
9. Choose the reservation **duration** for your cluster.
10. Create and name your **shared volume** (minimum size 1 TiB).
11. Optional: Select your **NVIDIA driver** and **CUDA** versions.
12. Click **Proceed**.

Your cluster will now be ready for you to use.

### Capacity Types

* **Reserved**: You pay upfront to reserve GPU capacity for a duration between 1-90 days.
* **On-demand**: You  pay as you go for GPU capacity on an hourly basis. No pre-payment or reservation needed, and you can terminate your cluster at any time.

### Node Types

We have the following node types available in Instant Clusters.

* NVIDIA HGX B200
* NVIDIA HGX H200
* NVIDIA HGX H100 SXM
* NVIDIA HGX H100 SXM - Inference (lower Infiniband multi-node GPU-to-GPU bandwidth, suitable for single-node inference)

If you don't see an available node type, select the "Notify Me" option to get notified when capacity is online. You can also contact us with your request via [support@together.ai](mailto:support@together.ai).

### Pricing

Pricing information for different GPU node types can be found [here](https://www.together.ai/instant-gpu-clusters).

### Cluster Status

* From the UI, verify that your cluster transitions to Ready.
* Monitor progress and health indicators directly from the cluster list.

### Start Training with Kubernetes

#### Install kubectl

Install `kubectl` in your environment, for example on [MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/).

#### Download kubeconfig

From the Instant Clusters UI, download the kubeconfig and copy it to your local machine:
```bash
~/.kube/together_instant.kubeconfig
export KUBECONFIG=$HOME/.kube/together_instant.kubeconfig
kubectl get nodes
```

> You can rename the file to `config`, but back up your existing config first.

#### Verify Connectivity

```bash
kubectl get nodes
```

You should see all worker and control plane nodes listed.

#### Deploy a Pod with Storage

* Create a PersistentVolumeClaim for shared storage.
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-pvc
spec:
  accessModes:
    - ReadWriteMany   # Multiple pods can read/write

  resources:
    requests:
      storage: 10Gi   # Requested size

  storageClassName: shared-storage-class
```

* Create a PersistentVolumeClaim for local storage.
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  accessModes:
    - ReadWriteOnce   # Only one pod/node can mount at a time

  resources:
    requests:
      storage: 50Gi
  storageClassName: local-storage-class
```

* Mount them into a pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  restartPolicy: Never
  containers:
    - name: ubuntu
      image: debian:stable-slim
      command: ["/bin/sh", "-c", "sleep infinity"]
      volumeMounts:
        - name: shared-pvc
          mountPath: /mnt/shared
        - name: local-pvc
          mountPath: /mnt/local
  volumes:
    - name: shared-pvc
      persistentVolumeClaim:
        claimName: shared-pvc
    - name: local-pvc
      persistentVolumeClaim:
        claimName: local-pvc
```

Apply and connect:
```bash
kubectl apply -f manifest.yaml
kubectl exec -it test-pod -- bash
```

#### Kubernetes Dashboard Access

* From the cluster UI, click the K8s Dashboard URL.
* Retrieve your access token using the following command:
```bash
kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user-token | awk '{print $1}') -o jsonpath='{.data.token}' | base64 -d | pbcopy
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
