---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploying via EKS (Elastic Kubernetes Service)

Amazon Elastic Kubernetes Service (EKS) provides a managed Kubernetes environment, allowing you to run containerized applications at scale. It leverages Kubernetes’ orchestration capabilities for efficient resource management and scalability.

In this section, we’ll walk through setting up an EKS cluster, configuring it for GPU support, and deploying your application.

### **Launch EKS cluster**

First, launch an EKS cluster by following the steps in the [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html), and in particular, the steps in Prerequisites and Step 1-4.

The steps in summary:

* Install AWS CLI and Kubectl
* Create the Amazon EKS cluster
* As part of adding nodes to the cluster in step3, use the following
  * AMI type - Amazon Linux 2023 - Nvidia (nvidia drivers pre-installed)
  * Instance Type - g5.2xlarge - 8vCPU
  * Storage - 512 GB

<img src="file:4d84fd66-c540-4b5b-aa84-fc7290639886" />

You can then view the cluster information in the AWS console.

<img src="file:e740810d-ec82-4288-856f-5deeec8d8f48" />

### **Define environment variables**

Next, set environment variables from the machine where the AWS CLI and Kubectl are installed.
```bash
export CUSTOMER_TAG=proxy.replicated.com/proxy/cohere/us-docker.pkg.dev/cohere-artifacts/replicated/single-serving-embed-multilingual-03:<YOUR_MODEL_TAG>
export LICENSE_ID="<YOUR_LICENSE_ID>"
export DOCKER_CONFIG=$(mktemp -d)
cat <<EOF > "${DOCKER_CONFIG}/config.json" { "auths": { "proxy.replicated.com": {"auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"}}EOF
kubectl create secret generic cohere-pull-secret --from-file=.dockerconfigjson="{$DOCKER_CONFIG}/config.json" --type=kubernetes.io/dockerconfigjson
```json
[Further reference](https://docs.cohere.com/v2/docs/single-container-on-private-clouds)

### **Generate application manifest**

Next, generate an application manifest by creating a file named `cohere.yaml`. The file contents should be copied from [this link](https://docs.cohere.com/v2/docs/single-container-on-private-clouds).

### **Start deployment**

Next, start the deployment by applying the configuration file. Then, check the status and monitor the logs of your pods.
```bash
kubectl apply -f cohere.yaml
kubectl get pods
kubectl logs -f <pod-name-from-above-command>
```

### **Call the model**

Next, run the model by first setting up port forwarding.
```bash
kubectl port-forward svc/cohere 8080:8080
```bash
Then, open a second window and send a test request using the curl command.
```bash
curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing embeddings in english"], "input_type": "classification"}'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
