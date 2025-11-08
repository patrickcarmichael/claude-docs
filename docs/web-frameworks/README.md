# Web Frameworks

Modern web frameworks for building AI-powered applications and LLM interfaces.

## Frameworks

### ⚡ [Next.js](./nextjs/)
**React Framework** | 2.9MB

The most popular React framework for production applications.

- **Type**: Full-stack React framework
- **Features**: SSR, SSG, API routes, server components
- **Best For**: Production web apps, AI chat interfaces
- **AI Integration**: Easy to add LLM APIs, streaming responses

📄 [Full Documentation](./nextjs/llms-full.txt)

**AI Use Cases:**
- Chat interfaces with streaming
- RAG applications with API routes
- AI-powered content generation
- Server-side LLM processing

**Deploy on**: [Vercel](./vercel/) (creators of Next.js)

---

### 🚀 [Astro](./astro/)
**Content-Focused Framework** | 2.5MB

Modern framework optimized for content-heavy sites with optional interactivity.

- **Type**: Content-first framework
- **Features**: Island architecture, multi-framework support
- **Best For**: Documentation sites, blogs, marketing pages
- **AI Integration**: Excellent for AI-generated content sites

📄 [Full Documentation](./astro/llms-full.txt)

**AI Use Cases:**
- AI-powered documentation sites
- LLM-generated blog content
- Static AI knowledge bases
- SEO-optimized AI content

**This site**: Could be built with Astro!

---

### 💬 [Streamlit](./streamlit/)
**Data App Framework** | 1.4MB

Python framework for building interactive data applications and dashboards with AI.

- **Type**: Python web framework
- **Features**: Interactive widgets, real-time updates, built-in components
- **Best For**: Data apps, dashboards, AI demos, prototyping
- **AI Integration**: Perfect for LLM apps, embeddings, RAG demos

📄 [Full Documentation](./streamlit/llms-full.txt)

**AI Use Cases:**
- Interactive LLM demos and prototypes
- RAG application dashboards
- Data visualization with AI analysis
- Quick AI app development

**Deploy on**: Streamlit Cloud or [Vercel](./vercel/)

---

### 🔷 [Vercel](./vercel/)
**Deployment Platform** | 7.9MB (Largest in category)

Cloud platform for deploying web applications with edge capabilities.

- **Type**: Platform-as-a-Service
- **Features**: Edge functions, instant deployments, analytics
- **Best For**: Deploying Next.js, AI applications, APIs
- **AI Integration**: Edge functions for fast LLM responses

📄 [Full Documentation](./vercel/llms-full.txt)

**AI Features:**
- Edge runtime for low-latency LLM calls
- AI SDK for building AI apps
- Streaming responses
- Built-in analytics

**Related**: [Vercel AI SDK](https://sdk.vercel.ai/) (not in this collection)

---

## Framework Comparison

| Framework | Type | Build Time | Runtime | Best AI Use Case |
|-----------|------|------------|---------|------------------|
| **Next.js** | Full-stack | Medium | Dynamic | Chat interfaces, RAG apps |
| **Astro** | Static-first | Fast | Static + Islands | Documentation, content |
| **Streamlit** | Python web | Instant | Dynamic | AI demos, dashboards |
| **Vercel** | Platform | N/A | Edge + Serverless | Deploy any framework |

---

## Building AI Applications

### Chat Interface with Next.js

**Perfect for**:
- ChatGPT-style interfaces
- Customer support bots
- AI assistants

**Example stack**:
```
Next.js App Router
  ↓
API Routes (server-side)
  ↓
Anthropic/OpenRouter API
  ↓
Streaming responses to client
```

**See**: [Next.js Docs](./nextjs/llms-full.txt)

**Deploy**: [Vercel Platform](./vercel/)

---

### Documentation with Astro

**Perfect for**:
- AI-generated documentation
- API references
- Knowledge bases

**Example stack**:
```
Astro Static Site
  ↓
LLM-generated content
  ↓
MDX for rich content
  ↓
Fast static delivery
```

**See**: [Astro Docs](./astro/llms-full.txt)

**Alternative**: [Mintlify](../infrastructure/mintlify/) or [GitBook](../infrastructure/gitbook/)

---

### Edge AI with Vercel

**Perfect for**:
- Low-latency LLM calls
- Global distribution
- Real-time AI features

**Example stack**:
```
Vercel Edge Functions
  ↓
Streaming LLM responses
  ↓
Global CDN
  ↓
Sub-100ms response times
```

**See**: [Vercel Docs](./vercel/llms-full.txt)

---

## Integration with AI Tools

### AI Platforms
Build web UIs for:
- [Anthropic](../ai-platforms/anthropic/) - Claude API
- [OpenRouter](../ai-platforms/openrouter/) - Multi-model access
- [Cohere](../ai-platforms/cohere/) - Enterprise RAG

### AI Frameworks
Use with:
- [LangChain](../ai-frameworks/langchain/) - Backend logic
- [LangGraph](../ai-frameworks/langgraph/) - Agent workflows
- [MCP](../ai-frameworks/mcp/) - Context integration

### Vector Databases
Connect to:
- [Pinecone](../infrastructure/pinecone/) - Vector search
- Other vector DBs for RAG

---

## Common Patterns

### Pattern 1: Next.js + LangChain + Pinecone
**RAG Chat Application**

```
User Query
  ↓
Next.js API Route
  ↓
LangChain retrieval
  ↓
Pinecone vector search
  ↓
LLM with context
  ↓
Streaming response
```

### Pattern 2: Astro + Static Generation
**AI Documentation Site**

```
LLM generates content
  ↓
Markdown files
  ↓
Astro build
  ↓
Static site
  ↓
Fast global delivery
```

### Pattern 3: Vercel Edge + OpenRouter
**Multi-Model AI App**

```
User request
  ↓
Vercel Edge Function
  ↓
OpenRouter (try multiple models)
  ↓
Return best response
  ↓
Edge-cached when possible
```

---

## Development Workflow

### Local Development
1. Choose framework ([Next.js](./nextjs/) or [Astro](./astro/))
2. Add AI integration ([AI Platforms](../ai-platforms/))
3. Optional: Add framework ([LangChain](../ai-frameworks/langchain/))
4. Use [Claude Code](../claude-code/) for AI-assisted development

### Production Deployment
1. Build your application
2. Deploy to [Vercel](./vercel/) or other platform
3. Configure environment variables for API keys
4. Monitor with [Analytics](./vercel/llms-full.txt)

---

## Best Practices

### Next.js AI Apps
- Use server components for LLM calls (keep API keys secret)
- Stream responses for better UX
- Implement rate limiting
- Cache expensive LLM operations

### Astro AI Content
- Generate content at build time when possible
- Use islands for interactive AI features
- Optimize for SEO
- Implement incremental builds

### Vercel Deployment
- Use Edge for latency-sensitive operations
- Configure proper caching headers
- Monitor function execution times
- Set appropriate timeouts

---

## Related Documentation

### AI Coding Tools
- [Claude Code](../claude-code/) - AI assistance while building
- [Cursor](../ai-coding-tools/cursor/) - AI IDE for web development

### Infrastructure
- [Cloudflare](../infrastructure/cloudflare/) - Alternative edge platform
- [Mintlify](../infrastructure/mintlify/) - Documentation platform
- [GitBook](../infrastructure/gitbook/) - Documentation platform

---

*Part of the [AI Development Documentation Hub](../)*
