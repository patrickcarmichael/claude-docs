---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an ingest pipeline with an inference processor

Create an ingest pipeline with an inference processor by using the [`put_pipeline`](https://www.elastic.co/guide/en/elasticsearch/reference/current/put-pipeline-api.html) method. Reference the inference endpoint created above as the `model_id` to infer against the data that is being ingested in the pipeline.
```python PYTHON
client.options(ignore_status=[404]).ingest.delete_pipeline(id="cohere_embeddings")

client.ingest.put_pipeline(
    id="cohere_embeddings",
    description="Ingest pipeline for Cohere inference.",
    processors=[
        {
            "inference": {
                "model_id": "cohere_embeddings",
                "input_output": {
                    "input_field": "text",
                    "output_field": "text_embedding",
                },
            }
        }
    ],
)
```
Let's note a few important parameters from that API call:

* `inference`: A processor that performs inference using a machine learning model.
* `model_id`: Specifies the ID of the inference endpoint to be used. In this example, the model ID is set to `cohere_embeddings`.
* `input_output`: Specifies input and output fields.
* `input_field`: Field name from which the `dense_vector` representation is created.
* `output_field`: Field name which contains inference results.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
