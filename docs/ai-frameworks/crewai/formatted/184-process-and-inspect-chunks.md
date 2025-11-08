---
title: "Crewai: Process and inspect chunks"
description: "Process and inspect chunks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Process and inspect chunks

test_source.add()
print(f"Number of chunks created: {len(test_source.chunks)}")
for i, chunk in enumerate(test_source.chunks[:3]):  # Show first 3 chunks
    print(f"Chunk {i+1}: {chunk[:50]}...")
```

### Common Knowledge Storage Issues

**"File not found" errors:**

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Check chunking behavior](./183-check-chunking-behavior.md)

**Next:** [Ensure files are in the correct location →](./185-ensure-files-are-in-the-correct-location.md)
