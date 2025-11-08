---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 6. Create an endpoint for inference from the exported engine

The Cohere client provides a built-in method to create an endpoint for inference, which will automatically deploy the model from the TensorRT-LLM engine you just exported.
```Python PYTHON 
co.sagemaker_finetuning.create_endpoint(
    arn=arn,
    endpoint_name=endpoint_name,
    s3_models_dir=s3_output_dir,
    recreate=True,
    instance_type=instance_type,
    role="ServiceRoleSagemaker",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
