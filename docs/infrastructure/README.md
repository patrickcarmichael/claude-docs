# Infrastructure & Services

Developer tools, databases, and platform services supporting AI applications.

## Services

### 🟢 [Supabase](./supabase/)
**Open Source Backend Platform** | 4.0MB

Open source Firebase alternative with PostgreSQL, real-time subscriptions, and AI/vector support.

- **Type**: Backend-as-a-Service (BaaS)
- **Database**: PostgreSQL with pgvector for embeddings
- **Features**: Real-time APIs, auth, storage, edge functions
- **Best For**: Full-stack apps, RAG systems, AI integrations

📄 [Full Documentation](./supabase/llms-full.txt)

**AI Use Cases:**
- Store and query embeddings with pgvector
- OpenAI, Hugging Face, and LangChain integrations
- Semantic search and RAG applications
- AI-powered real-time features

**Deploy**: Supabase Cloud or self-hosted

---

### 🌲 [Pinecone](./pinecone/)
**Vector Database** | 2.8MB

Fully managed vector database for AI applications and semantic search.

- **Type**: Vector database (cloud-native)
- **Use Cases**: RAG, semantic search, recommendations
- **Features**: Real-time updates, hybrid search, filtering
- **Scale**: Billions of vectors

📄 [Full Documentation](./pinecone/llms-full.txt)

**AI Use Cases:**
- RAG applications (Retrieval Augmented Generation)
- Semantic search over documents
- Recommendation engines
- Long-term memory for AI agents

**Use with**: [LangChain](../ai-frameworks/langchain/), [LangGraph](../ai-frameworks/langgraph/)

---

### 🧠 [Chroma](./chroma/)
**Open-Source Vector Database** | 4.2MB

Lightweight, developer-friendly vector database for prototyping and building AI applications locally.

- **Type**: Vector database (open-source)
- **Deployment**: Local (in-memory/SQLite), Docker, Cloud
- **Best For**: Prototyping, development, RAG systems
- **Features**: Simple API, in-memory + persistent modes, metadata filtering

📄 [Full Documentation](./chroma/llms-full.txt)

**Key Benefits:**
- No vendor lock-in - fully open-source
- Fast local development with SQLite
- Works seamlessly with LangChain
- Configurable embedding models
- HNSW indexing for fast similarity search

**AI Use Cases:**
- Rapid prototyping of RAG applications
- Local semantic search
- Embedding-based retrieval
- Development/testing environments
- Knowledge base Q&A systems

**Use with**: [LangChain](../ai-frameworks/langchain/), [Anthropic](../ai-platforms/anthropic/)

---

### ⚡ [Qdrant](./qdrant/)
**Open-Source Vector Database** | 3.2KB

Rust-based, high-performance vector database with hybrid search capabilities.

- **Type**: Vector database (managed cloud, hybrid, self-hosted)
- **Built in**: Rust for high performance
- **Features**: Hybrid search, RAG, payload filtering, HNSW indexing
- **Deployment**: Cloud SaaS, Kubernetes hybrid, Docker self-hosted

📄 [Full Documentation](./qdrant/llms-full.txt)

**AI Use Cases:**
- Semantic search with hybrid dense + sparse vectors
- RAG applications with advanced filtering
- Multivector representations (ColBERT, late interaction)
- Enterprise deployments with data sovereignty

**Key Advantages:**
- Open-source with flexible deployment options
- Superior filtering capabilities for RAG
- Built-in FastEmbed for local embeddings
- Data sovereignty options (no vendor lock-in)

**Use with**: [LangChain](../ai-frameworks/langchain/), [LlamaIndex](../ai-frameworks/llamaindex/)

---

### 🔍 [Weaviate](./weaviate/)
**AI-Native Vector Database with Hybrid Search** | 24KB

Open-source vector database with GraphQL API, hybrid search, knowledge graph, and modularity.

- **Type**: Vector database (self-hosted or managed cloud)
- **API**: GraphQL (primary) and REST
- **Features**: Hybrid search, multi-tenancy, pluggable vectorizers, advanced filtering
- **Deployment**: Weaviate Cloud, Docker, Kubernetes, Embedded Python/JS
- **Scale**: Billions of vectors

📄 [Full Documentation](./weaviate/llms-full.txt) | 📖 [README](./weaviate/)

**AI Use Cases:**
- RAG systems with semantic context retrieval
- Hybrid search combining vector + keyword matching
- Knowledge graphs with semantic understanding
- Long-term memory for intelligent agents
- Zero-shot classification and clustering

**Key Advantages:**
- GraphQL API for intuitive, flexible queries
- Hybrid search (semantic + keyword BM25)
- Self-hosted option with no vendor lock-in
- Built-in multi-tenancy for multi-customer applications
- Pluggable vectorizers: OpenAI, Cohere, HuggingFace, local models

**Use with**: [LangChain](../ai-frameworks/langchain/), [LlamaIndex](../ai-frameworks/llamaindex/), [Anthropic](../ai-platforms/anthropic/)

---

### 🔊 [ElevenLabs](./elevenlabs/)
**Voice AI Platform** | 5.5MB

Advanced text-to-speech and voice cloning platform.

- **Type**: Voice synthesis and cloning
- **Features**: Realistic voices, voice cloning, multilingual
- **Best For**: Voice assistants, audio content, accessibility
- **Quality**: Production-grade voice synthesis

📄 [Full Documentation](./elevenlabs/llms-full.txt)

**AI Use Cases:**
- Voice interfaces for LLM applications
- Audio content generation
- Multilingual voice assistants
- Accessibility features

---

### ☁️ [Cloudflare](./cloudflare/)
**Edge Computing Platform** | 24KB

Global edge computing platform with AI capabilities.

- **Type**: Edge platform, CDN, security
- **Features**: Workers, Pages, R2 storage, AI inference
- **Best For**: Edge computing, global distribution, security
- **Scale**: Global network in 300+ cities

📄 [Full Documentation](./cloudflare/llms-full.txt)

**AI Features:**
- Workers AI (edge LLM inference)
- Vectorize (vector database)
- AI Gateway (LLM proxy/cache)
- Global low-latency access

**Alternative to**: [Vercel](../web-frameworks/vercel/) for some use cases

---

### 📚 [Mintlify](./mintlify/)
**Documentation Platform** | 781KB

Modern documentation platform with AI-powered features.

- **Type**: Documentation hosting and management
- **Features**: Beautiful docs, AI search, API references
- **Best For**: Product documentation, API docs
- **AI Integration**: Auto-generates llms.txt files

📄 [Full Documentation](./mintlify/llms-full.txt)

**Features:**
- Automatic llms.txt generation
- AI-powered search
- Beautiful default themes
- MDX support

**Similar to**: [GitBook](./gitbook/)

---

### 📖 [GitBook](./gitbook/)
**Documentation Platform** | 422KB

Collaborative documentation platform for teams.

- **Type**: Documentation and knowledge management
- **Features**: Collaboration, version control, publishing
- **Best For**: Team documentation, internal wikis
- **AI Integration**: llms.txt generation

📄 [Full Documentation](./gitbook/llms-full.txt)

**Features:**
- Git-backed documentation
- Team collaboration
- llms.txt support
- Beautiful publishing

**Similar to**: [Mintlify](./mintlify/)

---

## Service Comparison

| Service | Category | Pricing | Best For |
|---------|----------|---------|----------|
| **Supabase** | Backend/Database | Free + pay-per-use | Full-stack, RAG, vectors |
| **Pinecone** | Vector DB | Pay-per-use | Pure vector search, simplicity |
| **Chroma** | Vector DB | Free (open-source) | Development, prototyping |
| **Qdrant** | Vector DB | Open-source + cloud | Flexibility, filtering, sovereignty |
| **Weaviate** | Vector DB | Open-source + cloud | Hybrid search, GraphQL, knowledge graphs |
| **ElevenLabs** | Voice AI | Subscription | Voice interfaces |
| **Cloudflare** | Edge platform | Free + paid tiers | Global distribution |
| **Mintlify** | Docs platform | Free + enterprise | Product docs |
| **GitBook** | Docs platform | Free + paid tiers | Team documentation |

---

## Common Use Cases

### RAG Application Stack

```
User Query
  ↓
LLM (Anthropic/OpenRouter)
  ↓
Vector Search (Pinecone)
  ↓
Retrieved Context
  ↓
LLM Response
```

**Components:**
- **Vector DB**: [Pinecone](./pinecone/)
- **LLM**: [Anthropic](../ai-platforms/anthropic/) or [OpenRouter](../ai-platforms/openrouter/)
- **Framework**: [LangChain](../ai-frameworks/langchain/)
- **Web**: [Next.js](../web-frameworks/nextjs/)

---

### Voice AI Assistant

```
User Voice Input
  ↓
Speech-to-Text
  ↓
LLM Processing
  ↓
Text-to-Speech (ElevenLabs)
  ↓
Voice Output
```

**Components:**
- **Voice**: [ElevenLabs](./elevenlabs/)
- **LLM**: [Anthropic](../ai-platforms/anthropic/)
- **Deploy**: [Cloudflare Workers](./cloudflare/) or [Vercel](../web-frameworks/vercel/)

---

### AI Documentation Site

```
Content Creation
  ↓
LLM-generated docs
  ↓
Documentation Platform
  ↓
Auto llms.txt
  ↓
AI-readable docs
```

**Options:**
- [Mintlify](./mintlify/) - Modern, API-focused
- [GitBook](./gitbook/) - Team collaboration
- [Astro](../web-frameworks/astro/) - Custom build

---

### Edge AI Application

```
Global User Request
  ↓
Cloudflare Edge
  ↓
Workers AI (edge LLM)
  ↓
Vectorize (vector DB)
  ↓
Fast response (<100ms)
```

**Stack:**
- **Edge**: [Cloudflare Workers](./cloudflare/)
- **Vector**: Cloudflare Vectorize
- **Alternative**: [Vercel Edge](../web-frameworks/vercel/)

---

## Integration Patterns

### Pattern 1: LangChain + Pinecone
**Semantic Search and RAG**

```python
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

# Create vector store
vectorstore = Pinecone(...)

# Semantic search
results = vectorstore.similarity_search(query)
```

**See**:
- [Pinecone Docs](./pinecone/llms-full.txt)
- [LangChain Docs](../ai-frameworks/langchain/)

---

### Pattern 2: Next.js + ElevenLabs
**Voice-Enabled Chat**

```typescript
// Convert LLM response to speech
const audio = await elevenLabs.textToSpeech(llmResponse)
```

**See**:
- [ElevenLabs Docs](./elevenlabs/llms-full.txt)
- [Next.js Docs](../web-frameworks/nextjs/)

---

### Pattern 3: Cloudflare + OpenRouter
**Global AI API**

```typescript
// Edge function with LLM
export default {
  async fetch(request) {
    const response = await fetch('https://openrouter.ai/api/...')
    return response
  }
}
```

**See**:
- [Cloudflare Docs](./cloudflare/llms-full.txt)
- [OpenRouter Docs](../ai-platforms/openrouter/)

---

## Choosing Services

### For Vector Search/RAG
**Primary Options:**

[Pinecone](./pinecone/) - Cloud-native simplicity
- Fully managed infrastructure
- Pay-per-use pricing
- Production-ready at scale
- Best if: Want zero maintenance

[Chroma](./chroma/) - Fast development & prototyping
- Lightweight, open-source
- Local development with SQLite
- No vendor lock-in
- Best if: Building MVPs or rapid prototyping

[Weaviate](./weaviate/) - Hybrid search & knowledge graphs
- Self-hosted or managed cloud
- GraphQL API for flexible queries
- Hybrid search (semantic + keyword)
- Multi-tenancy and modular vectorizers
- Best if: Need hybrid search, knowledge graphs, or GraphQL API

[Qdrant](./qdrant/) - Open-source flexibility
- Self-hosted, hybrid, or managed cloud
- Superior filtering for RAG
- Better data control/sovereignty
- Best if: Need customization or compliance control

**Alternatives:**
- Cloudflare Vectorize (edge vector DB)
- Supabase pgvector (for smaller datasets with relational data)

---

### For Voice AI
**Primary**: [ElevenLabs](./elevenlabs/)
- Best quality
- Voice cloning
- Multilingual

**Use cases**:
- Voice assistants
- Content generation
- Accessibility

---

### For Documentation
**Mintlify** if:
- API documentation focused
- Want modern design
- Need automatic llms.txt

**GitBook** if:
- Team collaboration priority
- Git integration needed
- Internal wikis

**Astro** if:
- Full customization wanted
- Static site preferred
- Developer resources available

---

### For Edge Computing
**Cloudflare** if:
- Global low-latency critical
- Need security features (DDoS, etc.)
- Want integrated AI inference

**Vercel** if:
- Using Next.js
- Want seamless Git integration
- Need preview deployments

---

## Related Documentation

### AI Platforms
- [Anthropic](../ai-platforms/anthropic/) - LLM API
- [OpenRouter](../ai-platforms/openrouter/) - Multi-model access
- [Cohere](../ai-platforms/cohere/) - Embeddings + reranking

### AI Frameworks
- [LangChain](../ai-frameworks/langchain/) - Integrate all services
- [LangGraph](../ai-frameworks/langgraph/) - Agent workflows
- [MCP](../ai-frameworks/mcp/) - Context protocol

### Web Frameworks
- [Next.js](../web-frameworks/nextjs/) - Build web apps
- [Vercel](../web-frameworks/vercel/) - Deploy applications
- [Astro](../web-frameworks/astro/) - Static sites

---

*Part of the [AI Development Documentation Hub](../)*
