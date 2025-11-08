---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Change "<aws_profile>" to your own AWS profile name

os.environ["AWS_PROFILE"] = "<aws_profile>"
```typescript
Finally, you need to set all the following variables using your own information. It's best not to add a trailing slash to these paths, as that could mean some parts won't work correctly. You can use either `ml.p4de.24xlarge` or `ml.p5.48xlarge` as the `instance_type` for Cohere Bring Your Own Fine-tuning, but the `instance_type` used for export and inference (endpoint creation) must be identical.
```Python PYTHON 

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
