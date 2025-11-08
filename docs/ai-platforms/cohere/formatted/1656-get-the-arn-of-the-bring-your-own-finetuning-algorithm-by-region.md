---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get the arn of the bring your own finetuning algorithm by region

cohere_package = (
    "cohere-command-r-v2-byoft-8370167e649c32a1a5f00267cd334c2c"
)
algorithm_map = {
    "us-east-1": f"arn:aws:sagemaker:us-east-1:865070037744:algorithm/{cohere_package}",
    "us-east-2": f"arn:aws:sagemaker:us-east-2:057799348421:algorithm/{cohere_package}",
    "us-west-2": f"arn:aws:sagemaker:us-west-2:594846645681:algorithm/{cohere_package}",
    "eu-central-1": f"arn:aws:sagemaker:eu-central-1:446921602837:algorithm/{cohere_package}",
    "ap-southeast-1": f"arn:aws:sagemaker:ap-southeast-1:192199979996:algorithm/{cohere_package}",
    "ap-southeast-2": f"arn:aws:sagemaker:ap-southeast-2:666831318237:algorithm/{cohere_package}",
    "ap-northeast-1": f"arn:aws:sagemaker:ap-northeast-1:977537786026:algorithm/{cohere_package}",
    "ap-south-1": f"arn:aws:sagemaker:ap-south-1:077584701553:algorithm/{cohere_package}",
}
if region not in algorithm_map:
    raise Exception(f"Current region {region} is not supported.")
arn = algorithm_map[region]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
