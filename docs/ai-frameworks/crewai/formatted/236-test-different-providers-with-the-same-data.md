---
title: "Crewai: Test different providers with the same data"
description: "Test different providers with the same data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Test different providers with the same data

providers_to_test = [
    {
        "name": "OpenAI",
        "config": {
            "provider": "openai",
            "config": {"model": "text-embedding-3-small"}
        }
    },
    {
        "name": "Ollama",
        "config": {
            "provider": "ollama",
            "config": {"model": "mxbai-embed-large"}
        }
    }
]

for provider in providers_to_test:
    print(f"\nTesting {provider['name']} embeddings...")

    # Create crew with specific embedder
    crew = Crew(
        agents=[...],
        tasks=[...],
        memory=True,
        embedder=provider['config']
    )

    # Run your test and measure performance
    result = crew.kickoff()
    print(f"{provider['name']} completed successfully")
```

### Troubleshooting Embedding Issues

**Model not found errors:**

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use without exposing keys in code](./235-use-without-exposing-keys-in-code.md)

**Next:** [Verify model availability →](./237-verify-model-availability.md)
