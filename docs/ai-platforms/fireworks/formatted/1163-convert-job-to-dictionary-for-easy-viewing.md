---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Convert job to dictionary for easy viewing

job = BatchInferenceJob.get("my-batch-job", "my-account")
if job:
    job_dict = BatchInferenceJob.to_dict(job)
    print(job_dict)
    # Output:

    # {

    #     'name': 'accounts/my-account/batchInferenceJobs/my-batch-job',

    #     'display_name': 'My Batch Job',

    #     'model': 'accounts/fireworks/models/llama-v3p1-8b-instruct',

    #     'state': 'JOB_STATE_COMPLETED',

    #     'create_time': '2024-01-01 08:00:00 UTC',

    #     'inference_parameters': {'max_tokens': 1024, 'temperature': 0.7}

    # }

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
