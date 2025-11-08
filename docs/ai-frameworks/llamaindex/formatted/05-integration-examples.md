---
title: "Llamaindex: Integration Examples"
description: "Integration Examples section of Llamaindex documentation"
source: "https://llamaindex.com"
last_updated: "2025-11-08"
---

## Integration Examples


### OpenAI Integration

```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-4", temperature=0.7)
```

### Anthropic Claude Integration

```python
from llama_index.llms.anthropic import Anthropic

llm = Anthropic(model="claude-3-opus-20240229")
```

### Local Ollama Integration

```python
from llama_index.llms.ollama import Ollama

llm = Ollama(model="mistral", base_url="http://localhost:11434")
```

### AWS Bedrock Integration

```python
from llama_index.llms.bedrock import Bedrock

llm = Bedrock(model="anthropic.claude-3-sonnet-20240229-v1:0")
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use Cases by Provider Category](./04-use-cases-by-provider-category.md)

**Next:** [Advanced Features →](./06-advanced-features.md)
