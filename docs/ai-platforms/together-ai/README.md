# Together AI

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)

**The Cloud Platform for Open-Source AI**

Together AI provides the fastest and most cost-effective platform for running open-source AI models. Fine-tune, deploy, and scale custom models with production-grade infrastructure.

**Official Resources**:
- [Together Website](https://www.together.ai/)
- [API Documentation](https://docs.together.ai/)
- [Platform Dashboard](https://api.together.ai/)
- [Discord Community](https://discord.gg/together)

---

## Key Features

### Open-Source Focus
- **100+ Models**: Leading open-source models
- **Custom Fine-Tuning**: Train models on your data
- **Full Model Control**: Deploy and manage custom models
- **No Vendor Lock-in**: Run models anywhere after training

### Performance
- **Flash Attention**: Optimized for speed
- **Low Latency**: Sub-second inference
- **Auto-Scaling**: Handle traffic spikes
- **GPU Optimization**: Efficient resource utilization

### Developer Platform
- **OpenAI Compatible**: Easy migration
- **Function Calling**: Tool integration
- **Streaming**: Real-time responses
- **Batch Processing**: Cost-effective bulk requests

---

## Popular Models

| Model | Type | Context |
|-------|------|---------|
| **Llama 3.3 70B** | Chat/Instruct | 128K tokens |
| **Qwen 2.5 72B** | Chat/Instruct | 128K tokens |
| **Mixtral 8x22B** | MoE Chat | 64K tokens |
| **DeepSeek Coder V2** | Code | 64K tokens |
| **FLUX.1** | Image Gen | - |

See [Full Model Documentation](./llms-full.txt) for complete list.

---

## Quick Start

### 1. Get Your API Key
```bash
# Visit https://api.together.ai/
# Sign up or log in
# Navigate to API Keys section
# Create new API key
```

### 2. Install SDK

**Python**:
```bash
pip install together
```

**TypeScript** (OpenAI SDK):
```bash
npm install openai
```

### 3. Make Your First Request

**Python**:
```python
from together import Together

client = Together(api_key="YOUR_API_KEY")
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.3-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
print(response.choices[0].message.content)
```

**TypeScript**:
```typescript
import OpenAI from 'openai';

const client = new OpenAI({
    baseURL: 'https://api.together.xyz/v1',
    apiKey: process.env.TOGETHER_API_KEY
});

const response = await client.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.3-70B-Instruct-Turbo",
    messages: [{ role: "user", content: "Explain quantum computing" }]
});
console.log(response.choices[0].message.content);
```

---

## Common Use Cases

- **Fine-Tuning**: Custom models for specific domains
- **Open-Source Deployment**: Run latest open models
- **Cost-Sensitive Applications**: Cheaper than closed models
- **Image Generation**: Open-source image models
- **Research & Development**: Experiment with cutting-edge models

---

## Pricing

**Competitive pricing** with per-token costs.
**Fine-tuning**: Custom pricing based on compute requirements.
**Reserved Capacity**: Dedicated GPU instances available.

See [Together Pricing](https://www.together.ai/pricing) for current rates.

---

## Support

- **Official Website**: [together.ai](https://www.together.ai/)
- **Documentation**: [docs.together.ai](https://docs.together.ai/)
- **Discord**: [discord.gg/together](https://discord.gg/together)
- **Status Page**: [status.together.ai](https://status.together.ai/)

---

*Part of the [AI Development Documentation Hub](../../)*

Last Updated: January 2025
