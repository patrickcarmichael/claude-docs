# AI Platforms

LLM API providers and AI service platforms for building applications.

## Platforms

### 🤖 [Anthropic](./anthropic/)
**Claude API & SDKs** | 4.3MB

Creator of Claude - state-of-the-art language models with long context windows and strong reasoning capabilities.

- **Models**: Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
- **Key Features**: 200K context window, vision, tool use, function calling
- **Best For**: Complex reasoning, long documents, coding assistance

📄 [Full Documentation](./anthropic/llms-full.txt)

**Related Tools**: [Claude Code](../claude-code/) - Official CLI assistant

---

### 🚀 [Cohere](./cohere/)
**Enterprise LLM Platform** | 2.7MB

Enterprise-focused LLM platform with strong RAG and embedding capabilities.

- **Models**: Command, Command-R, Embed
- **Key Features**: Enterprise RAG, embeddings, reranking, multilingual
- **Best For**: Search, retrieval, enterprise applications

📄 [Full Documentation](./cohere/llms-full.txt)

---

### 🔥 [Fireworks](./fireworks/)
**Fast LLM Inference** | 991KB

High-performance LLM inference platform optimized for speed and cost.

- **Models**: Open-source models, custom deployments
- **Key Features**: Fast inference, competitive pricing, model marketplace
- **Best For**: Production deployments, cost-sensitive applications

📄 [Full Documentation](./fireworks/llms-full.txt)

---

### 🔀 [OpenRouter](./openrouter/)
**Multi-Model LLM Router** | 839KB

Unified API to access multiple LLM providers through a single interface.

- **Models**: 100+ models from OpenAI, Anthropic, Meta, Google, etc.
- **Key Features**: Fallback routing, model comparison, unified pricing
- **Best For**: Model flexibility, cost optimization, A/B testing

📄 [Full Documentation](./openrouter/llms-full.txt)

---

### 🤝 [Together.ai](./together-ai/)
**Open-Source LLM Platform** | 1.3MB

Platform focused on open-source and custom model deployment.

- **Models**: Llama, Mixtral, Qwen, custom fine-tuned models
- **Key Features**: Fine-tuning, custom deployments, open-source focus
- **Best For**: Open-source models, custom training, research

📄 [Full Documentation](./together-ai/llms-full.txt)

---

## Comparison

| Platform | Strength | Context | Best Use Case |
|----------|----------|---------|---------------|
| **Anthropic** | Reasoning & safety | 200K | Complex tasks, long docs |
| **Cohere** | Enterprise RAG | 128K | Search, retrieval |
| **Fireworks** | Speed & cost | Varies | Production, cost-sensitive |
| **OpenRouter** | Model variety | Varies | Multi-model access |
| **Together.ai** | Open-source | Varies | Custom models, research |

---

## Integration Examples

### With Claude Code
```bash
# Use Claude Code with different providers
claude --model anthropic/claude-3-5-sonnet
claude --model openrouter/anthropic/claude-3.5-sonnet
```

See: [Claude Code Model Config](../claude-code/configuration/model-config.md)

### With AI Frameworks
- **LangChain**: Supports all platforms → [LangChain Docs](../ai-frameworks/langchain/)
- **LangGraph**: Agent workflows → [LangGraph Docs](../ai-frameworks/langgraph/)
- **CrewAI**: Multi-agent systems → [CrewAI Docs](../ai-frameworks/crewai/)

---

## Common Patterns

### Choosing a Platform

**For production applications:**
1. Start with [Anthropic](./anthropic/) for quality
2. Add [OpenRouter](./openrouter/) for flexibility
3. Consider [Fireworks](./fireworks/) for cost optimization

**For enterprise:**
1. [Anthropic](./anthropic/) for critical tasks
2. [Cohere](./cohere/) for RAG/search
3. Deploy via [AWS Bedrock](../claude-code/deployment/amazon-bedrock.md) or [GCP Vertex](../claude-code/deployment/google-vertex-ai.md)

**For research/experimentation:**
1. [Together.ai](./together-ai/) for open-source models
2. [OpenRouter](./openrouter/) for quick comparisons
3. Fine-tune on [Together.ai](./together-ai/)

---

## Related Documentation

- **AI Coding Tools**: [Cursor](../ai-coding-tools/cursor/), [Windsurf](../ai-coding-tools/windsurf/), [Claude Code](../claude-code/)
- **AI Frameworks**: [LangChain](../ai-frameworks/langchain/), [LangGraph](../ai-frameworks/langgraph/), [CrewAI](../ai-frameworks/crewai/)
- **Deployment**: [Claude Code Deployment Options](../claude-code/deployment/)

---

*Part of the [AI Development Documentation Hub](../)*
