---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Monitoring a Fine-tuning Job

Fine-tuning can take time depending on the model size, dataset size, and hyperparameters. Your job will progress through several states: Pending, Queued, Running, Uploading, and Completed.

You can monitor and manage the job's progress using the following methods:

* **List all jobs**: `client.fine_tuning.list()`
* **Status of a job**: `client.fine_tuning.retrieve(id=ft_resp.id)`
* **List all events for a job**: `client.fine_tuning.list_events(id=ft_resp.id)` - Retrieves logs and events generated during the job
* **Cancel job**: `client.fine_tuning.cancel(id=ft_resp.id)`
* **Download fine-tuned model**: `client.fine_tuning.download(id=ft_resp.id)`

Once the job is complete (`status == 'completed'`), the response from `retrieve` will contain the name of your newly created fine-tuned model. It follows the pattern: `<your-account>/<base-model-name>:<suffix>:<job-id>`.

**Check Status via API**
```python
  ## Check status of the job

  resp = client.fine_tuning.retrieve(ft_resp.id)
  print(resp.status)

  ## This loop will print the logs of the job thus far

  for event in client.fine_tuning.list_events(id=ft_resp.id).data:
      print(event.message)
```
```bash
  ## Using CLI

  together fine-tuning retrieve "your-job-id"
```

Example output:
```text
Fine tune request created
Job started at Thu Apr  3 03:19:46 UTC 2025
Model data downloaded for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at Thu Apr  3 03:19:48 UTC 2025
Data downloaded for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at 2025-04-03T03:19:55.595750
WandB run initialized.
Training started for model togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT
Epoch completed, at step 24
Epoch completed, at step 48
Epoch completed, at step 72
Training completed for togethercomputer/Meta-Llama-3.1-8B-Instruct-Reference__TOG__FT at Thu Apr  3 03:27:55 UTC 2025
Uploading output model
Compressing output model
Model compression complete
Model upload complete
Job finished at Thu Apr  3 03:31:33 UTC 2025
```

**Dashboard Monitoring**

You can also monitor your job on the [Together AI jobs dashboard](https://api.together.xyz/jobs).

If you provided a Weights & Biases API key, you can view detailed training metrics on the W\&B platform, including loss curves and more.

<img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=2973b0ebdc3f38a4b7466c02fd0ddc40" alt="" data-og-width="3290" width="3290" data-og-height="1366" height="1366" data-path="images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c511ef3fd1475fd005d3387fa3ef5194 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8ae7668e3592726f6bb90272d45d16b4 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9246196bf8f56237a60bc35020873347 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=11bf77aec25449cdd17fc5f9b5252fb7 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b7833a099df09e37c228384c3e203685 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/ad25e0527bb7c1718477f0ac51b7d4a158d59e32b13bf1c4d97577e3e7a5b937-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=5ad6e32772425ac3006d368830a3d999 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
