# Cohere

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)

**Enterprise-Grade Natural Language AI Platform**

Cohere provides leading language AI models for search, generation, and understanding. Built for enterprise with security, scalability, and customization at the core.

**Official Resources**:
- [Cohere Website](https://cohere.com/)
- [API Documentation](https://docs.cohere.com/)
- [Cohere Dashboard](https://dashboard.cohere.com/)
- [Discord Community](https://discord.gg/cohere)

---

## Key Features

### Enterprise-Focused
- **Deployment Flexibility**: Cloud, on-premise, or private cloud
- **Data Privacy**: Your data never trains public models
- **Compliance**: SOC 2, GDPR, HIPAA compliant options
- **Fine-Tuning**: Custom models for your use case

### Specialized Capabilities
- **Embed**: Industry-leading text embeddings
- **Rerank**: Improve search result relevance
- **Chat**: Conversational AI with RAG support
- **Generate**: Text generation for various tasks
- **Classify**: Text classification and sentiment analysis

---

## Available Models

| Model | Best For | Context |
|-------|----------|---------|
| **Command R+** | Complex reasoning, multilingual | 128K tokens |
| **Command R** | Balanced performance, production | 128K tokens |
| **Command** | General tasks, generation | 4K tokens |
| **Embed v3** | Embeddings, search, RAG | 512 tokens |
| **Rerank v3** | Search re-ranking | 4K tokens |

See [Full Model Documentation](./llms-full.txt) for detailed specifications.

---

## Quick Start

### 1. Get Your API Key
```bash
# Visit https://dashboard.cohere.com/
# Create account or sign in
# Copy your API key from dashboard
```

### 2. Install SDK

**Python**:
```bash
pip install cohere
```

**TypeScript**:
```bash
npm install cohere-ai
```

### 3. Make Your First Request

**Python**:
```python
import cohere

co = cohere.Client('YOUR_API_KEY')
response = co.chat(
    model='command-r-plus',
    message='Explain quantum computing'
)
print(response.text)
```

**TypeScript**:
```typescript
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({ token: process.env.COHERE_API_KEY });
const response = await cohere.chat({
    model: 'command-r-plus',
    message: 'Explain quantum computing'
});
console.log(response.text);
```

---

## Common Use Cases

- **Enterprise Search**: Semantic search with RAG
- **Customer Support**: Intelligent chatbots and assistants
- **Content Generation**: Marketing copy, documentation
- **Data Classification**: Categorize and organize content
- **Multilingual Applications**: 100+ language support

---

## Pricing

**Pay-as-you-go** and **Enterprise** pricing available.
Contact Cohere for custom pricing based on your needs.

See [Cohere Pricing](https://cohere.com/pricing) for current rates.

---

## Support

- **Official Website**: [cohere.com](https://cohere.com/)
- **Documentation**: [docs.cohere.com](https://docs.cohere.com/)
- **Discord**: [discord.gg/cohere](https://discord.gg/cohere)
- **Enterprise Support**: Available with enterprise plans

---

*Part of the [AI Development Documentation Hub](../../)*

Last Updated: January 2025
