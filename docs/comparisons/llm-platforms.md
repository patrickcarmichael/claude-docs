# LLM Platforms Comparison

Comprehensive side-by-side comparison of major LLM API providers and platforms for building AI applications.

## Overview

| Platform | Creator | Founded | Primary Focus | Model Count | Best For |
|----------|---------|---------|---------------|-------------|----------|
| **Anthropic** | Anthropic | 2021 | Safety-first, long context | 3 | Complex reasoning, long documents |
| **Cohere** | Cohere | 2021 | Enterprise RAG & embeddings | 5+ | Search, retrieval, enterprise |
| **Fireworks** | Fireworks AI | 2023 | Fast inference & cost | 30+ | Production deployments, cost optimization |
| **OpenRouter** | OpenRouter | 2023 | Multi-provider aggregation | 100+ | Model flexibility, A/B testing |
| **Together.ai** | Together Computer | 2022 | Open-source & custom models | 50+ | Custom training, research |

---

## Features Comparison

### Core Capabilities

| Feature | Anthropic | Cohere | Fireworks | OpenRouter | Together.ai |
|---------|-----------|--------|-----------|-----------|-------------|
| **Text Generation** | Yes | Yes | Yes | Yes | Yes |
| **Vision/Images** | Yes (multimodal) | No | Yes | Yes (varies) | Limited |
| **Tool Use** | Yes | Yes | Limited | Yes | Limited |
| **Function Calling** | Yes | Yes | Limited | Yes | Limited |
| **Embeddings** | No | Yes | Limited | No | Yes |
| **Reranking** | No | Yes | No | No | No |
| **Fine-tuning** | No | Yes | Limited | Limited | Yes |
| **Batch Processing** | Yes | Yes | Yes | Limited | Yes |
| **Streaming** | Yes | Yes | Yes | Yes | Yes |
| **Vision Models** | Yes (Claude) | No | Yes | Yes | Yes |

### Advanced Features

| Feature | Anthropic | Cohere | Fireworks | OpenRouter | Together.ai |
|---------|-----------|--------|-----------|-----------|-------------|
| **Multi-turn Conversations** | Native | Native | Native | Native | Native |
| **System Prompts** | Yes | Yes | Yes | Yes | Yes |
| **Prompt Caching** | Yes (beta) | No | No | Limited | No |
| **Agentic Loop Support** | Yes | Yes | Yes | Yes | Yes |
| **Custom Model Deployment** | No | Limited | Yes | No | Yes |
| **On-Premise Options** | No | Yes | Limited | No | Yes |
| **Model Fine-tuning** | No | Yes | Limited | Limited | Yes |
| **Retrieval Integration** | No | Built-in | Limited | Depends | No |

---

## Context Windows & Model Specs

### Anthropic

| Model | Context | Input Cost | Output Cost | Reasoning |
|-------|---------|-----------|------------|-----------|
| **Claude 3.5 Sonnet** | 200K | $3/1M | $15/1M | Excellent |
| **Claude 3 Opus** | 200K | $15/1M | $75/1M | Best-in-class |
| **Claude 3 Haiku** | 200K | $0.80/1M | $4/1M | Fast, cheap |

**Strengths:**
- Largest context windows (200K tokens)
- Strong reasoning capabilities
- Excellent safety alignment
- Native vision support
- Tool use and function calling

**Best for:** Complex reasoning tasks, long documents (200K token analysis), research, safety-critical applications

### Cohere

| Model | Context | Input Cost | Output Cost | Specialty |
|-------|---------|-----------|------------|-----------|
| **Command R+** | 128K | $3/1M | $15/1M | Production |
| **Command R** | 128K | $0.50/1M | $1.50/1M | Affordable |
| **Command** | 4K | Varies | Varies | Legacy |

**Strengths:**
- Enterprise-grade RAG capabilities
- Built-in embeddings API
- Reranking for retrieval
- Multilingual support
- Connectors for knowledge bases

**Best for:** Enterprise search, RAG systems, retrieval augmentation, multilingual applications, knowledge management

### Fireworks

| Model Category | Examples | Speed | Cost |
|---|---|---|---|
| **Open Source** | Llama 2, Mistral, Qwen | Very Fast | Low |
| **Proprietary** | Fireworks Llama | Very Fast | Very Low |
| **Serverless** | 30+ models | Medium | Variable |

**Context:** Varies by model (4K-100K+)

**Strengths:**
- Fastest inference in industry
- Lowest cost for volume
- 30+ open-source models available
- Custom model deployment
- Pay-per-token pricing
- Model fine-tuning available

**Best for:** Production deployments, cost-sensitive applications, high-volume inference, open-source models

### OpenRouter

| Capability | Count | Models | Coverage |
|---|---|---|---|
| **Total Models** | 100+ | From 5+ providers | Comprehensive |
| **Provider Access** | 5+ | OpenAI, Anthropic, Cohere, Google, Meta | Multi-provider |
| **Context Range** | Wide | 4K to 100K+ | All tiers |

**Strengths:**
- Access to 100+ models from single API
- Automatic fallback routing
- Model comparison tools
- Unified pricing aggregation
- Developer-friendly
- Flexible model selection

**Best for:** Model flexibility, A/B testing, avoiding vendor lock-in, exploring different models, development workflows

### Together.ai

| Model Set | Count | Focus | Use Case |
|---|---|---|---|
| **Open Source** | 30+ | Community models | Research |
| **Fine-tuning** | Custom | Training | Production |
| **Deployment** | Custom | Private clouds | Enterprise |

**Strengths:**
- Extensive open-source model library
- Fine-tuning on custom data
- Private cloud deployment options
- Community-driven model selection
- Research-friendly
- Custom model support

**Best for:** Open-source models, custom training, research projects, privacy-conscious deployments, fine-tuning

---

## Pricing Models

### Cost Structure Comparison

| Platform | Pricing Model | Unit | Base Cost | Volume Discounts |
|----------|--------------|------|-----------|-----------------|
| **Anthropic** | Per-token | Input/Output | Fixed | Available |
| **Cohere** | Per-token + Features | Input/Output + API | Fixed | Custom enterprise |
| **Fireworks** | Per-token | Input/Output | Very low | Tiered |
| **OpenRouter** | Per-token (aggregated) | Input/Output | Model-dependent | Varies |
| **Together.ai** | Per-token + Features | Input/Output | Variable | Available |

### Example Cost (1M Input Tokens)

| Platform | Model | 1M Tokens Cost |
|----------|-------|----------------|
| **Anthropic** | Claude 3.5 Sonnet | $3.00 |
| **Cohere** | Command R | $0.50 |
| **Fireworks** | Llama 2 70B | $0.30-0.50 |
| **OpenRouter** | Varies | $0.50-15.00 |
| **Together.ai** | Varies | $0.20-3.00 |

**Note:** Prices fluctuate; output tokens typically cost 2-5x input tokens.

### Pricing Details

#### Anthropic
- **Model-based pricing:** Different rates per model
- **Input/Output tokens:** Separate pricing tiers
- **Volume discounts:** Available for enterprise
- **No setup fees:** Pay-as-you-go
- **Free tier:** 15 API calls/day for developers

#### Cohere
- **Enterprise focus:** Custom pricing
- **Feature-based add-ons:** Embeddings, reranking extra
- **Tiered models:** Command vs Command-R pricing
- **Volume pricing:** Available for large-scale use
- **Free tier:** Limited trial credits

#### Fireworks
- **Most competitive:** Lowest cost per token
- **Pay per call:** No minimum spending
- **Tiered by model:** Open-source cheaper
- **Volume benefits:** Automatic optimization
- **Free tier:** Limited free credits

#### OpenRouter
- **Provider aggregation:** Different costs per model
- **Routing optimization:** Automatic fallback
- **Usage tracking:** Detailed analytics
- **No platform fee:** Pure pass-through pricing
- **Free tier:** Testing available

#### Together.ai
- **Model variable:** Pricing per model
- **Fine-tuning costs:** Separate from inference
- **Enterprise pricing:** Custom deployments
- **Volume discounts:** Available
- **Free tier:** Starter credits

---

## API & Integration

### Client SDK Support

| Language | Anthropic | Cohere | Fireworks | OpenRouter | Together.ai |
|----------|-----------|--------|-----------|-----------|------------|
| **Python** | Native | Native | Native | Community | Native |
| **JavaScript** | Native | Native | Community | Native | Community |
| **TypeScript** | Native | Native | Community | Native | Community |
| **Go** | Native | Limited | Community | Limited | Limited |
| **Java** | Limited | Native | Limited | Limited | Limited |
| **REST API** | Yes | Yes | Yes | Yes | Yes |

### Framework Integration

| Framework | Anthropic | Cohere | Fireworks | OpenRouter | Together.ai |
|-----------|-----------|--------|-----------|-----------|-------------|
| **LangChain** | Full | Full | Full | Full | Full |
| **LangGraph** | Full | Limited | Limited | Limited | Limited |
| **CrewAI** | Full | Full | Full | Full | Full |
| **Llamaindex** | Full | Full | Full | Full | Full |

---

## Deployment & Operations

### Infrastructure & Regions

| Platform | Regions | SLA | Uptime | On-Premise |
|----------|---------|-----|--------|-----------|
| **Anthropic** | US, EU, Singapore | Enterprise | 99.9%+ | No |
| **Cohere** | AWS regions | Enterprise | 99.9% | Yes |
| **Fireworks** | US, EU, Asia | Standard | 99.9% | Limited |
| **OpenRouter** | Depends on provider | Variable | Variable | No |
| **Together.ai** | US, EU | Standard | 99%+ | Yes |

### Security & Compliance

| Feature | Anthropic | Cohere | Fireworks | OpenRouter | Together.ai |
|---------|-----------|--------|-----------|-----------|-------------|
| **HTTPS Only** | Yes | Yes | Yes | Yes | Yes |
| **API Key Auth** | Yes | Yes | Yes | Yes | Yes |
| **Data Encryption** | Yes | Yes | Yes | Yes | Yes |
| **GDPR Compliant** | Yes | Yes | Yes | Yes | Yes |
| **SOC 2 Certified** | Yes | Yes | Limited | Limited | Limited |
| **Enterprise Auth** | Yes | Yes | Limited | Limited | Limited |
| **Data Residency** | Available | Available | Limited | Limited | Available |

---

## Rate Limits & Quotas

### Standard Rate Limits

| Platform | Requests/Min | Tokens/Min | Burst | Notes |
|----------|-------------|-----------|-------|-------|
| **Anthropic** | 50 | 40K | 10x | Per-key limits |
| **Cohere** | 100 | 100K | Higher | Enterprise higher |
| **Fireworks** | 200 | Unlimited | High | Very generous |
| **OpenRouter** | 100 | 100K | Variable | Provider-dependent |
| **Together.ai** | 100 | 100K | Variable | Model-dependent |

---

## Decision Matrix

### For Complex Reasoning Tasks
**Winner: Anthropic**
- 200K context window
- Best reasoning capabilities
- Native tool use
- Vision support

### For Enterprise Search/RAG
**Winner: Cohere**
- Built-in embeddings
- Reranking API
- Enterprise connectors
- RAG optimization

### For Cost-Sensitive Production
**Winner: Fireworks**
- Lowest cost per token
- Fastest inference
- Open-source models
- Custom deployments

### For Model Flexibility
**Winner: OpenRouter**
- 100+ models
- Single API
- Multi-provider
- Developer-friendly

### For Custom Models & Research
**Winner: Together.ai**
- Fine-tuning capabilities
- Open-source focus
- Private deployments
- Research tools

---

## Quick Selection Guide

### Use Anthropic If You...
- Need maximum reasoning capability
- Work with 100K+ token documents
- Require vision capabilities
- Prioritize safety and alignment
- Value strong instruction-following

### Use Cohere If You...
- Build search/retrieval systems
- Need enterprise RAG
- Want built-in embeddings
- Require multilingual support
- Need production reliability

### Use Fireworks If You...
- Optimize for cost
- Require fastest inference
- Use open-source models
- Deploy at high volume
- Need fine-tuning capabilities

### Use OpenRouter If You...
- Want to test multiple models
- Avoid vendor lock-in
- Need model flexibility
- Prefer development simplicity
- Plan A/B testing

### Use Together.ai If You...
- Focus on open-source models
- Need fine-tuning
- Want private deployments
- Do research/experimentation
- Require custom training

---

## Integration Examples

### With Claude Code
```bash
# Use different LLM platforms with Claude Code
claude --model anthropic/claude-3-5-sonnet
claude --model openrouter/anthropic/claude-3.5-sonnet
claude --model openrouter/cohere/command-r
claude --model openrouter/mistralai/mistral-7b
```

### With LangChain
```python
# Anthropic
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-5-sonnet")

# Cohere
from langchain_cohere import ChatCohere
llm = ChatCohere(model="command-r")

# OpenRouter (via OpenAI-compatible API)
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="openrouter/anthropic/claude-3-5-sonnet")
```

### With LangGraph
```python
# All platforms work with LangGraph
from langgraph import graph
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-5-sonnet")
# Build agent workflows
```

---

## Switching Between Platforms

### Migration Paths

**From OpenAI to Anthropic:**
1. Use OpenRouter for gradual migration
2. Test Claude models alongside GPT-4
3. Switch to direct Anthropic API
4. Benefits: Better reasoning, 200K context

**From Anthropic to Cohere:**
1. Add Cohere for RAG/search
2. Use together in multi-model setup
3. Integrate embeddings API
4. Benefits: Better search, enterprise features

**From Single Provider to Multi-Provider:**
1. Switch to OpenRouter
2. Test different models
3. Select best performers per task
4. Benefits: Flexibility, cost optimization

---

## Performance Benchmarks

### Latency (First Token Time)

| Platform | Model | Latency |
|----------|-------|---------|
| **Anthropic** | Claude 3.5 Sonnet | 500-800ms |
| **Cohere** | Command R | 300-600ms |
| **Fireworks** | Llama 70B | 100-300ms |
| **OpenRouter** | Varies | 200-1000ms |
| **Together.ai** | Varies | 150-500ms |

*Varies by model, token count, and load*

### Reasoning Quality

| Benchmark | Anthropic | Cohere | Fireworks | OpenRouter | Together.ai |
|-----------|-----------|--------|-----------|-----------|-------------|
| **Math** | Excellent | Good | Fair | Varies | Good |
| **Code** | Excellent | Good | Very Good | Excellent | Good |
| **Logic** | Excellent | Good | Fair | Varies | Fair |

---

## Support & Community

| Platform | Support | Community | Documentation | Status |
|----------|---------|-----------|---------------|--------|
| **Anthropic** | Enterprise support | Active Discord/forum | Excellent | Rapidly evolving |
| **Cohere** | Enterprise support | Growing community | Good | Stable |
| **Fireworks** | Good support | Growing | Good | Rapidly evolving |
| **OpenRouter** | Community | Community-driven | Adequate | Stable |
| **Together.ai** | Community | Research community | Good | Growing |

---

## Key Takeaways

1. **Anthropic** leads in reasoning and long-context capability
2. **Cohere** specializes in enterprise RAG and search
3. **Fireworks** offers best cost-per-token and speed
4. **OpenRouter** provides maximum flexibility with 100+ models
5. **Together.ai** excels at open-source and custom models

**Recommendation:** Most production systems use 2-3 platforms:
- Anthropic for reasoning/complex tasks
- Fireworks for cost-optimized production
- OpenRouter for flexibility/A/B testing

---

## Related Documentation

- **[AI Platforms](../ai-platforms/)** - Individual platform docs
- **[Claude Code Model Config](../claude-code/configuration/model-config.md)** - Using these in Claude Code
- **[AI Frameworks](../ai-frameworks/)** - Integration patterns
- **[Infrastructure](../infrastructure/)** - Deployment options

---

*Last updated: November 2025*
*Part of the [AI Development Documentation Hub](../)*
