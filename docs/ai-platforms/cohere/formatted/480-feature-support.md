---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Feature support

The most complete set of features is found on the cohere platform, while each of the cloud platforms support subsets of these features. Please consult the platform-specific documentation for more information about the parameters that they support.

| Feature          | Cohere Platform | Bedrock     | Sagemaker   | Azure       | OCI         | Private Deployment |
| ---------------- | --------------- | ----------- | ----------- | ----------- | ----------- | ------------------ |
| chat\_stream     | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| chat             | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| generate\_stream | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| generate         | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| embed            | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| rerank           | ✅               | ✅           | ✅           | ✅           | ⬜️          | ✅                  |
| classify         | ✅               | ⬜️          | ⬜️          | ⬜️          | ⬜️          | ✅                  |
| summarize        | ✅               | ⬜️          | ⬜️          | ⬜️          | ⬜️          | ✅                  |
| tokenize         | ✅               | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline)        |
| detokenize       | ✅               | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline)        |
| check\_api\_key  | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
