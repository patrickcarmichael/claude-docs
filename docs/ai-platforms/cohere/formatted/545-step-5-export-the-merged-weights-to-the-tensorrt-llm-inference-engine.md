---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 5. Export the merged weights to the TensorRT-LLM inference engine

Create Cohere client and use it to export the merged weights to the TensorRT-LLM inference engine. The exported TensorRT-LLM engine will be stored in a tar file `{s3_output_dir}/{export_name}.tar.gz` in S3, where the file name is the same as the `export_name`.
```Python PYTHON 
co = cohere.SagemakerClient(aws_region=region)
co.sagemaker_finetuning.export_finetune(
    arn=arn,
    name=export_name,
    s3_checkpoint_dir=s3_checkpoint_dir,
    s3_output_dir=s3_output_dir,
    instance_type=instance_type,
    role="ServiceRoleSagemaker",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
