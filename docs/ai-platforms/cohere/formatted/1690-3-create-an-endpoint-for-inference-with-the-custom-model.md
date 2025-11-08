---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Create an endpoint for inference with the custom model

### A. Create an endpoint

The Cohere AWS SDK provides a built-in method for creating an endpoint for inference. This will automatically deploy the model you finetuned earlier.

>   **Note**: This is equivalent to creating and deploying a `ModelPackage` in SageMaker's SDK.
```python
endpoint_name = "test-finetune"
co.sagemaker_finetuning.create_endpoint(
    arn=arn,
    endpoint_name=endpoint_name,
    s3_models_dir=s3_models_dir,
    recreate=True,
    instance_type="ml.p4de.24xlarge",
    role="ServiceRoleSagemaker",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
