---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Option 2: Upload a Custom Adapter & run inference on it on Together

The Together API also allows you to upload your own private LoRA adapter files for inference. To upload a custom adapter:

### **Step 1: Prepare Adapter File:**

Ensure your adapter file is compatible with the above supported base models.

If you are getting the adapter from HuggingFace you can find information about the base model there as well.

You need to make sure that the adapter you are trying to upload has an `adapter_config.json` and `adapter_model.safetensors` files.

### **Step 2: Upload Adapter Using Together API:**

**Source 1: Source the adapter from an AWS s3 bucket:**
```bash
  #!/bin/bash
  # uploadadapter.sh

  # Generate presigned adapter url

  ADAPTER_URL="s3://test-s3-presigned-adapter/my-70B-lora-1.zip"
  PRESIGNED_ADAPTER_URL=$(aws s3 presign ${ADAPTER_URL})

  # Specify additional params

  MODEL_TYPE="adapter"
  ADAPTER_MODEL_NAME="test-lora-model-70B-1"
  BASE_MODEL="meta-llama/Meta-Llama-3.1-70B-Instruct"
  DESCRIPTION="test_70b_lora_description" # Lazy curl replace below, don't put spaces here.

  # Upload

  curl -v https://api.together.xyz/v0/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "model_name": "'${ADAPTER_MODEL_NAME}'",
    "model_source": "'${PRESIGNED_ADAPTER_URL}'",
    "model_type": "'${MODEL_TYPE}'",
    "base_model": "'${BASE_MODEL}'",
    "description": "'${DESCRIPTION}'"
  }'
```

**Source 2: Source the adapter from HuggingFace:**

Make sure that the adapter contains `adapter_config.json` and `adapter_model.safetensors` files in Files and versions tab on HuggingFace.
```bash
  # From HuggingFace

  HF_URL="https://huggingface.co/reissbaker/llama-3.1-8b-abliterated-lora"

  MODEL_TYPE="adapter"
  BASE_MODEL="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference"
  DESCRIPTION="test_lora_8B"
  ADAPTER_MODEL_NAME=test-lora-model-creation-8b
  HF_TOKEN=hf_token
  TOGETHER_API_KEY=together-api-key

  # Upload

  curl -v https://api.together.xyz/v0/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "model_name": "'${ADAPTER_MODEL_NAME}'",
    "model_source": "'${HF_URL}'",
    "model_type": "'${MODEL_TYPE}'",
    "description": "'${DESCRIPTION}'",
    "hf_token": "'${HF_TOKEN}'"
  }'
```

For both Option 1 and 2 the output contains the "job\_id" and "model\_name". The model name must be unique, if you attempt to upload a model name that previously was uploaded you will receive a "Model name already exists" error.
```json
  {
    "data": {
      "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",   <------- Job ID
      "model_name": "devuser/test-lora-model-creation-8b",
      "model_source": "remote_archive"
    },
    "message": "job created"
  }
```

You can poll our API using the "job\_id" until the adapter has finished uploading.
```bash
  curl https://api.together.xyz/v1/jobs/job-b641db51-38e8-40f2-90a0-5353aeda6f21 \
    -H "Authorization: Bearer $TOGETHER_API_KEY" | jq .
```

The output contains a "status" field. When the "status" is "Complete", your adapter is ready!
```json
  {
    "type": "adapter_upload",
    "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
    "status": "Complete",
    "status_updates": []
  }
```

### **Step 3: Run LoRA Inference**:

Take the model\_name string you get from the adapter upload output below, then use it through the Together API.
```json
  {
    "data": {
      "job_id": "job-b641db51-38e8-40f2-90a0-5353aeda6f21",
      "model_name": "devuser/test-lora-model-creation-8b",      <------ Model Name
      "model_source": "remote_archive"
    },
    "message": "job created"
  }
```

Make Together API call to the model:
```bash
  MODEL_NAME_FOR_INFERENCE="devuser/test-lora-model-creation-8b"

   curl -X POST https://api.together.xyz/v1/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "'$MODEL_NAME_FOR_INFERENCE'",
      "prompt": "Q: The capital of France is?\nA:",
      "temperature": 0.8,
      "max_tokens": 128
    }'
```

Expected Response:
```json
  {
    "id": "8f3317dd3c3a39ef-YYZ",
    "object": "text.completion",
    "created": 1734398453,
    "model": "devuser/test-lora-model-creation-8b",
    "prompt": [],
    "choices": [
      {
        "text": " Paris\nB: Berlin\nC: Warsaw\nD: London\nAnswer: A",
        "finish_reason": "eos",
        "seed": 13424880326038300000,
        "logprobs": null,
        "index": 0
      }
    ],
    "usage": {
      "prompt_tokens": 10,
      "completion_tokens": 18,
      "total_tokens": 28,
      "cache_hit_rate": 0
    }
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
