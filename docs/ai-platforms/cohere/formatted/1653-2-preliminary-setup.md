---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Preliminary setup

Install the Python packages you will use below and import them. For example, you can run the command below to install `cohere` if you haven't done so.
```sh
pip install "cohere>=5.11.0"
```
```python
import cohere
import os
import sagemaker as sage

from sagemaker.s3 import S3Uploader
```
Make sure you have access to the resources in your AWS account. For example, you can configure an AWS profile by the command `aws configure sso` (see [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-configure)) and run the command below to set the environment variable `AWS_PROFILE` as your profile name.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
