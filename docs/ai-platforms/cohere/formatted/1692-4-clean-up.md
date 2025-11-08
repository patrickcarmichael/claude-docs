---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Clean-up

### A. Delete the endpoint

After you've successfully performed inference, you can delete the deployed endpoint to avoid being charged continuously. This can also be done via the Cohere AWS SDK:
```python
co.delete_endpoint()
co.close()
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
