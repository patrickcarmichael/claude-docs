---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cancel a specific batch by ID

batch_id = "your-batch-id-here"
cancelled_batch = client.batches.cancel_batch(batch_id)

print(cancelled_batch)
```

### 7. Get a list of all batches

At any time, you can see all your batches.
```python
  from together import Together

  client = Together()

  ## List all batches

  batches = client.batches.list_batches()

  for batch in batches:
      print(batch)
```
```ts
  import Together from "together-ai";

  const client = new Together();

  const allBatches = await client.batches.list();

  for (const batch of allBatches) {
    console.log(batch);
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
