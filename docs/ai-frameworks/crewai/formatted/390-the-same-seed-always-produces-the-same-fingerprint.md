---
title: "Crewai: The same seed always produces the same fingerprint"
description: "The same seed always produces the same fingerprint section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# The same seed always produces the same fingerprint

same_fingerprint = Fingerprint.generate(seed="my-agent-id")
assert deterministic_fingerprint.uuid_str == same_fingerprint.uuid_str

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a deterministic fingerprint using a seed string](./389-create-a-deterministic-fingerprint-using-a-seed-st.md)

**Next:** [You can also set metadata →](./391-you-can-also-set-metadata.md)
