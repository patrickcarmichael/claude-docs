# Anthropic Claude

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)

**The Most Helpful, Harmless, and Honest AI Assistant**

Anthropic Claude is a family of frontier AI models designed with safety, helpfulness, and harmlessness at the core. Available through the Anthropic API, Amazon Bedrock, Google Cloud Vertex AI, and other platforms.

**Official Resources**:
- [Anthropic Website](https://www.anthropic.com/)
- [API Documentation](https://docs.anthropic.com/)
- [Claude Console](https://console.anthropic.com/)
- [Discord Community](https://discord.gg/anthropic)

---

## Key Features

### Advanced Reasoning
- **Extended Thinking**: Deep problem-solving with visible reasoning
- **Analysis & Coding**: Superior performance on complex technical tasks
- **Instruction Following**: Precise adherence to detailed prompts
- **Agentic Capabilities**: Multi-step workflows with tool use

### Safety & Reliability
- **Constitutional AI**: Built-in safety principles
- **Reduced Hallucinations**: More accurate and trustworthy responses
- **Transparent Limitations**: Clear about uncertainty
- **Responsible AI**: Ethical AI development practices

### Developer Experience
- **Vision Support**: Process images and documents
- **Function Calling**: Integrate with external tools and APIs
- **Streaming**: Real-time response generation
- **Message Batching**: Process multiple requests efficiently

---

## Available Models

### Claude 4.5 Series (Latest)

| Model | Best For | Context | Pricing |
|-------|----------|---------|---------|
| **Claude Sonnet 4.5** | Balanced performance, production | 200K tokens | Mid |
| **Claude Haiku 4.5** | Speed, high-volume tasks | 200K tokens | Lowest |

### Claude 4 Series

| Model | Best For | Context | Pricing |
|-------|----------|---------|---------|
| **Claude Sonnet 4** | High intelligence, complex tasks | 200K tokens | Mid-High |
| **Claude Opus 4.1** | Maximum capability (limited availability) | 200K tokens | Highest |

See [Full Model Documentation](./llms-full.txt) for detailed specifications.

---

## Quick Start

### 1. Get Your API Key
```bash
# Visit https://console.anthropic.com/
# Create account or sign in
# Navigate to API Keys section
# Generate new API key
```

### 2. Install SDK

**Python**:
```bash
pip install anthropic
```

**TypeScript**:
```bash
npm install @anthropic-ai/sdk
```

### 3. Make Your First Request

**Python**:
```python
from anthropic import Anthropic

client = Anthropic(api_key="YOUR_API_KEY")
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain quantum computing"}
    ]
)
print(message.content[0].text)
```

**TypeScript**:
```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const message = await client.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [{ role: 'user', content: 'Explain quantum computing' }]
});
console.log(message.content[0].text);
```

---

## Common Use Cases

- **Code Generation & Review**: Write, debug, and optimize code
- **Technical Documentation**: Create and maintain docs
- **Data Analysis**: Analyze and extract insights from data
- **Customer Support**: Build intelligent support systems
- **Research Assistance**: Summarize papers, extract information
- **Creative Writing**: Generate content, brainstorm ideas

---

## Pricing

**Input tokens**: $0.80 - $15.00 per 1M tokens (varies by model)
**Output tokens**: $4.00 - $75.00 per 1M tokens (varies by model)
**Context Caching**: 90% discount on cached input tokens
**Batch API**: 50% discount on request processing

See [Anthropic Pricing](https://www.anthropic.com/pricing) for current rates.

---

## Support

- **Official Website**: [anthropic.com](https://www.anthropic.com/)
- **Documentation**: [docs.anthropic.com](https://docs.anthropic.com/)
- **Status Page**: [status.anthropic.com](https://status.anthropic.com/)
- **Discord**: [discord.gg/anthropic](https://discord.gg/anthropic)

---

*Part of the [AI Development Documentation Hub](../../)*

Last Updated: January 2025
