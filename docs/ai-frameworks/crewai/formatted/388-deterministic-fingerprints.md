---
title: "Crewai: Deterministic Fingerprints"
description: "Deterministic Fingerprints section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Deterministic Fingerprints


While you cannot directly set the UUID and creation timestamp, you can create deterministic fingerprints using the `generate` method with a seed:

```python  theme={null}
from crewai.security import Fingerprint

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The fingerprint remains unchanged](./387-the-fingerprint-remains-unchanged.md)

**Next:** [Create a deterministic fingerprint using a seed string →](./389-create-a-deterministic-fingerprint-using-a-seed-st.md)
