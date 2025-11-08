---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## FAQ

**Q: How long do batches take to complete?**\
A: Processing time depends on batch size and model complexity. Most batches typically complete within 1-12 hours, but can take up to 24 hours (or only partially complete within 24 hours) depending on inference capacity.

**Q: Can I cancel a running batch?**\
A: Currently, batches cannot be cancelled once processing begins.

**Q: What happens if my batch exceeds the deadline?**\
A: The batch will be marked as EXPIRED and partial results may be available.

**Q: Are results returned in the same order as requests?**\
A: No, results may be in any order. Use `custom_id` to match requests with responses.

**Q: Can I use the same file for multiple batches?**\
A: Yes, uploaded files can be reused for multiple batch jobs.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
