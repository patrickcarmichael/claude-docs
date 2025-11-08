---
title: "Crewai: Check if API keys are set"
description: "Check if API keys are set section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Check if API keys are set

required_keys = ["OPENAI_API_KEY", "GOOGLE_API_KEY", "COHERE_API_KEY"]
for key in required_keys:
    if os.getenv(key):
        print(f"✅ {key} is set")
    else:
        print(f"❌ {key} is not set")
```

**Performance comparison:**

```python  theme={null}
import time

def test_embedding_performance(embedder_config, test_text="This is a test document"):
    start_time = time.time()

    crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True,
        embedder=embedder_config
    )

    # Simulate memory operation
    crew.kickoff()

    end_time = time.time()
    return end_time - start_time

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Verify model availability](./237-verify-model-availability.md)

**Next:** [Compare performance →](./239-compare-performance.md)
