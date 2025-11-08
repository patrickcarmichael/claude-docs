# OpenRouter

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)

**Unified API for All LLMs**

OpenRouter provides a single API to access 200+ language models from multiple providers. Switch models instantly without changing code, optimize for cost or performance, and avoid vendor lock-in.

**Official Resources**:
- [OpenRouter Website](https://openrouter.ai/)
- [API Documentation](https://openrouter.ai/docs)
- [Model Rankings](https://openrouter.ai/rankings)
- [Discord Community](https://discord.gg/openrouter)

---

## Key Features

### Multi-Provider Access
- **200+ Models**: GPT-4, Claude, Gemini, Llama, and more
- **One API**: Switch models with a single parameter change
- **Automatic Fallback**: Retry failed requests with different providers
- **Load Balancing**: Route to fastest/cheapest available provider

### Cost Optimization
- **Real-Time Pricing**: See costs before making requests
- **Model Comparison**: Find the best price/performance ratio
- **Credits System**: Prepaid credits or pay-as-you-go
- **Free Tier**: Try models with free credits

### Developer Experience
- **OpenAI Compatible**: Drop-in replacement for OpenAI API
- **Model Rankings**: Community-driven quality scores
- **Usage Analytics**: Track costs and performance
- **OAuth Integration**: Let users bring their own keys

---

## Popular Models via OpenRouter

| Model | Provider | Context | Relative Cost |
|-------|----------|---------|---------------|
| **GPT-4 Turbo** | OpenAI | 128K | High |
| **Claude Sonnet 4.5** | Anthropic | 200K | Mid-High |
| **Gemini 2.5 Pro** | Google | 1M | Mid |
| **Llama 3.3 70B** | Meta (OSS) | 128K | Low |
| **Mixtral 8x22B** | Mistral | 64K | Low-Mid |

See [Full Model Documentation](./llms-full.txt) for complete list.

---

## Quick Start

### 1. Get Your API Key
```bash
# Visit https://openrouter.ai/
# Sign up with Google/Discord/Email
# Navigate to Keys section
# Create new API key
```

### 2. Install SDK

**Python** (OpenAI SDK):
```bash
pip install openai
```

**TypeScript** (OpenAI SDK):
```bash
npm install openai
```

### 3. Make Your First Request

**Python**:
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_KEY"
)

response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4.5",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
print(response.choices[0].message.content)
```

**TypeScript**:
```typescript
import OpenAI from 'openai';

const client = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY
});

const response = await client.chat.completions.create({
    model: "anthropic/claude-sonnet-4.5",
    messages: [{ role: "user", content: "Explain quantum computing" }]
});
console.log(response.choices[0].message.content);
```

---

## Common Use Cases

- **Multi-Model Applications**: Compare outputs from different models
- **Cost Optimization**: Switch to cheaper models when appropriate
- **Fallback Strategy**: Automatic retry with alternative models
- **Model Evaluation**: Test which model works best for your use case
- **Avoid Vendor Lock-in**: Switch providers without code changes

---

## Pricing

**Per-Token Pricing**: Varies by model and provider
**Credits System**: Prepaid credits or pay-as-you-go
**Free Tier**: Limited free credits for testing

Pricing shown in real-time on OpenRouter platform before making requests.

See [OpenRouter Pricing](https://openrouter.ai/docs#models) for current rates.

---

## Support

- **Official Website**: [openrouter.ai](https://openrouter.ai/)
- **Documentation**: [openrouter.ai/docs](https://openrouter.ai/docs)
- **Discord**: [discord.gg/openrouter](https://discord.gg/openrouter)
- **Model Rankings**: [openrouter.ai/rankings](https://openrouter.ai/rankings)

---

*Part of the [AI Development Documentation Hub](../../)*

Last Updated: January 2025
