---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Subscribe to the finetune algorithm

To subscribe to the model algorithm:

1. Open the algorithm listing page [Cohere Command R Finetuning](https://aws.amazon.com/marketplace/pp/prodview-2czs5tbao7b7c)
2. On the AWS Marketplace listing, click on the **Continue to Subscribe** button.
3. On the **Subscribe to this software** page, review and click on **"Accept Offer"** if you and your organization agrees with EULA, pricing, and support terms. On the "Configure and launch" page, make sure ARN displayed in your region match with the ARN in the following cell.
```sh
pip install "cohere>=5.11.0"
```
```python
import cohere
import boto3
import sagemaker as sage
from sagemaker.s3 import S3Uploader
```
The algorithm is available in the list of AWS regions specified below.
```python
region = boto3.Session().region_name

cohere_package = ""

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
