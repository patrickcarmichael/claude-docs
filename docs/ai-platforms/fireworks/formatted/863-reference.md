---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reference

<AccordionGroup>
  <Accordion title="Job states">
    Batch jobs progress through several states:

    | State          | Description                                           |
    | -------------- | ----------------------------------------------------- |
    | **VALIDATING** | Dataset is being validated for format requirements    |
    | **PENDING**    | Job is queued and waiting for resources               |
    | **RUNNING**    | Actively processing requests                          |
    | **COMPLETED**  | All requests successfully processed                   |
    | **FAILED**     | Unrecoverable error occurred (check status message)   |
    | **EXPIRED**    | Exceeded 24-hour limit (completed requests are saved) |
  </Accordion>

  <Accordion title="Supported models">
    * **Base Models** – Any model in the [Model Library](https://fireworks.ai/models)
    * **Custom Models** – Your uploaded or fine-tuned models

    *Note: Newly added models may have a delay before being supported. See [Quantization](/models/quantization) for precision info.*
  </Accordion>

  <Accordion title="Limits and constraints">
    * **Per-request limits:** Same as [Chat Completion API limits](/api-reference/post-chatcompletions)
    * **Input dataset:** Max 500MB
    * **Output dataset:** Max 8GB (job may expire early if reached)
    * **Job timeout:** 24 hours maximum
  </Accordion>

  <Accordion title="Handling expired jobs">
    Jobs expire after 24 hours. Completed rows are billed and saved to the output dataset.

    **Resume processing:**
```bash
    firectl create batch-inference-job \
      --continue-from original-job-id \
      --model accounts/fireworks/models/llama-v3p1-8b-instruct \
      --output-dataset-id new-output-dataset
```
    This processes only unfinished/failed requests from the original job.

    **Download complete lineage:**
```bash
    firectl download dataset output-dataset-id --download-lineage
```
    Downloads all datasets in the continuation chain.
  </Accordion>

  <Accordion title="Best practices">
    * **Validate thoroughly:** Check dataset format before uploading
    * **Descriptive IDs:** Use meaningful `custom_id` values for tracking
    * **Optimize tokens:** Set reasonable `max_tokens` limits
    * **Monitor progress:** Track long-running jobs regularly
    * **Cache optimization:** Place static content first in prompts
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
