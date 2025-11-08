---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploying via EC2 instances

Amazon Elastic Compute Cloud (EC2) provides scalable computing capacity in the AWS cloud and forms the foundation of your private deployment.

In this section, we’ll walk through launching an appropriate GPU-enabled EC2 instance, connecting to it securely, and installing the necessary NVIDIA drivers to utilize the GPU hardware.

The following sections provide a step by step guide to deploy the Embed Multilingual 3 model on EC2.

### Launch EC2 instance

First, launch an EC2 instance with the following specifications:

* Application and OS images - Ubuntu
* Instance Type - g5.2xlarge - 8vCPU
* Storage - 512 GB - root volume

<img src="file:cc24daff-1325-4308-aca3-a267352ebf15" />

<img src="file:1dc1231b-fc1a-4766-9168-e0971de7615c" />

### SSH to the EC2 instance using AWS console - ‘EC2 Instance Connect’ option.

Next, connect to your EC2 instance using the “EC2 Instance Connect” option. This allows you to access the instance through a browser-based client using the default username “ubuntu.” Ensure your instance has a public IPv4 address for successful connection.

<img src="file:c0024b8b-36a6-4df9-915e-99ff32e48690" />

### Install Nvidia drivers

Next, install the NVIDIA drivers on your EC2 instance to enable GPU support. Use the following commands to install the necessary drivers and the NVIDIA CUDA toolkit.

* Nvidia drivers
```bash
  sudo apt install -y ubuntu-drivers-common
  sudo ubuntu-drivers install
  sudo apt install nvidia-cuda-toolkit
```json
  [Further reference](https://documentation.ubuntu.com/aws/en/latest/aws-how-to/instances/install-nvidia-drivers/)

* Nvidia container toolkit
```bash
  curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
  sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
  sudo apt-get update
  sudo apt-get install -y nvidia-container-toolkit
```json
  [Further reference](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

* Reboot the system
  This is often necessary after installing drivers or making significant system changes to ensure all components are properly initialized and running with the latest configurations.

  Before rebooting, restart any mentioned services after running the above commands.
```bash
  sudo reboot
```
* Verify that the GPU is correctly installed
```bash
  nvidia-smi
```
<img src="file:03acd401-cc4d-4fe6-8634-cd69e9a19c5f" />

### **Install docker on the instance**

Next, install Docker on your instance. This involves updating the package list, installing Docker, starting the Docker service, and verifying the installation by running a test container.
```bash
sudo apt-get update
sudo apt-get install docker.io -ysudo systemctl start docker
sudo docker run hello-world
sudo systemctl enable docker
docker --version
```json
[Further reference](https://medium.com/@srijaanaparthy/step-by-step-guide-to-install-docker-on-ubuntu-in-aws-a39746e5a63d)

### **Define environment variables**

```bash
export CUSTOMER_TAG=proxy.replicated.com/proxy/cohere/us-docker.pkg.dev/cohere-artifacts/replicated/single-serving-embed-multilingual-03:<YOUR_MODEL_TAG>
export LICENSE_ID="<YOUR_LICENSE_ID>"
export DOCKER_CONFIG=$(mktemp -d)
cat <<EOF > "${DOCKER_CONFIG}/config.json" { "auths": { "proxy.replicated.com": {"auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"}}EOF
```json
[Further reference](https://docs.cohere.com/v2/docs/single-container-on-private-clouds)

### **Pull container image**

Next, prepare the environment by obtaining the required software components for deployment.
```bash
sudo docker pull $CUSTOMER_TAG
```
If you encounter an error “permission denied while trying to connect to the Docker daemon socket at”, run the following command:
```bash
sudo chmod 666 /var/run/docker.sock
```json
[Further reference](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)

Then, verify that the image has been pulled successfully:
```bash
sudo docker images
```
<img src="file:88861793-4e89-4a71-90cf-17fb897788af" />

### **Start container**

Next, run the Docker container. This starts the container in detached mode with GPU support.
```bash
sudo docker run -d --rm --name embed-english --gpus=1 --net=host proxy.replicated.com/proxy/cohere/us-docker.pkg.dev/cohere-artifacts/replicated/single-serving-embed-multilingual-03:<YOUR_MODEL_TAG>

sudo docker ps
```
<img src="file:18a55437-ce7b-43e2-8d07-b33d60c299d2" />

### **Call the model**

Next, test calling the model by executing the `curl` command to send a `POST` request to the local server. This tests the model’s functionality by providing input data for processing.
```bash
curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing multilingual embeddings"], "input_type": "classification"}'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
