# Fireworks AI

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)

**The Fastest AI Inference Platform**

Fireworks AI provides blazing-fast inference for open-source and proprietary models with production-grade infrastructure, optimized for speed and cost.

**Official Resources**:
- [Fireworks Website](https://fireworks.ai/)
- [API Documentation](https://docs.fireworks.ai/)
- [Platform Dashboard](https://fireworks.ai/dashboard)
- [Discord Community](https://discord.gg/fireworks)

---

## Key Features

### Performance
- **Sub-Second Latency**: Fastest inference in the industry
- **Optimized Infrastructure**: Custom chips and software stack
- **Auto-Scaling**: Handle traffic spikes seamlessly
- **Global CDN**: Low latency worldwide

### Model Selection
- **80+ Models**: Open-source and proprietary
- **Custom Models**: Deploy your fine-tuned models
- **Multi-Modal**: Text, image, audio, video
- **Function Calling**: Tool integration support

### Developer Experience
- **OpenAI Compatible**: Drop-in replacement
- **Streaming**: Real-time responses
- **Batch Processing**: Cost-effective bulk requests
- **Fine-Tuning**: Custom model training

---

## Popular Models

| Model | Type | Context |
|-------|------|---------|
| **Llama 3.3 70B** | Open LLM | 128K tokens |
| **Mixtral 8x22B** | MoE LLM | 64K tokens |
| **Qwen 2.5 72B** | Open LLM | 128K tokens |
| **DeepSeek V3** | Open LLM | 64K tokens |
| **Stable Diffusion 3** | Image Gen | - |

See [Full Model Documentation](./llms-full.txt) for complete list.

---

## Quick Start

### 1. Get Your API Key
```bash
# Visit https://fireworks.ai/
# Sign up or log in
# Navigate to API Keys in dashboard
```

### 2. Install SDK

**Python**:
```bash
pip install fireworks-ai
```

**TypeScript**:
```bash
npm install @fireworks-ai/sdk
```

### 3. Make Your First Request

**Python**:
```python
from fireworks.client import Fireworks

client = Fireworks(api_key="YOUR_API_KEY")
response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p3-70b-instruct",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
print(response.choices[0].message.content)
```

**TypeScript**:
```typescript
import Fireworks from '@fireworks-ai/sdk';

const client = new Fireworks({ apiKey: process.env.FIREWORKS_API_KEY });
const response = await client.chat.completions.create({
    model: "accounts/fireworks/models/llama-v3p3-70b-instruct",
    messages: [{ role: "user", content: "Explain quantum computing" }]
});
console.log(response.choices[0].message.content);
```

---

## Common Use Cases

- **High-Traffic Applications**: Fast inference at scale
- **Real-Time Chat**: Low-latency conversations
- **Image Generation**: Fast image creation
- **RAG Systems**: Efficient retrieval-augmented generation
- **Open-Source Deployment**: Run open models efficiently

---

## Pricing

**Competitive pricing** with pay-as-you-go and reserved capacity options.
Significantly cheaper than closed-source alternatives.

See [Fireworks Pricing](https://fireworks.ai/pricing) for current rates.

---

## Support

- **Official Website**: [fireworks.ai](https://fireworks.ai/)
- **Documentation**: [docs.fireworks.ai](https://docs.fireworks.ai/)
- **Discord**: [discord.gg/fireworks](https://discord.gg/fireworks)
- **Status Page**: [status.fireworks.ai](https://status.fireworks.ai/)

---

*Part of the [AI Development Documentation Hub](../../)*

Last Updated: January 2025
