---
title: "Crewai: Load model and tokenizer"
description: "Load model and tokenizer section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Load model and tokenizer

tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

def custom_embeddings(text: str) -> list[float]:
    # Tokenize and get model outputs
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)

    # Use mean pooling to get text embedding
    embeddings = outputs.last_hidden_state.mean(dim=1)

    # Convert to list of floats and return
    return embeddings[0].tolist()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Custom Embeddings](./850-custom-embeddings.md)

**Next:** [Use custom embeddings with the tool →](./852-use-custom-embeddings-with-the-tool.md)
