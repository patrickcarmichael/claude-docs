# Weaviate

**AI-Native Vector Database with Hybrid Search**

Weaviate is an open-source, cloud-native vector database designed specifically for AI and machine learning applications. It combines semantic search capabilities with advanced filtering, GraphQL API, and modular architecture to power modern RAG systems and AI agents.

## Platform Overview

Weaviate stores data objects alongside their vector embeddings, enabling intelligent semantic search beyond keyword matching. Its hybrid search combines semantic similarity with traditional BM25 keyword search for optimal retrieval.

**Key Positioning:**
- **Type**: Vector database + knowledge graph capability
- **Architecture**: Self-hosted or fully managed cloud
- **API**: GraphQL (primary) and REST
- **Scale**: Billions of vectors support
- **Best For**: RAG systems, semantic search, AI agents, knowledge bases

## Key Features

### Hybrid Search
- **Semantic Search**: Vector similarity search for meaning-based retrieval
- **Keyword Search**: Traditional BM25 text search
- **Combined**: Weighted hybrid search combining both approaches
- **Filtering**: Advanced metadata filtering before/during search

### GraphQL API
- Intuitive, efficient API for all operations
- Query and mutation support
- Aggregations and analytics
- Minimize over-fetching of data

### Modularity
- **Pluggable Vectorizers**: OpenAI, Cohere, HuggingFace, Google PaLM, Ollama
- **Custom Modules**: Extend functionality with custom integrations
- **Framework Support**: LangChain, LlamaIndex, Semantic Kernel
- **Flexible Architecture**: Adapt to any deployment scenario

### Advanced Filtering
- **Metadata Filters**: Filter before vector search
- **Property-Based Queries**: Search specific fields
- **Range Queries**: Numeric and date filtering
- **Complex WHERE Clauses**: Combine filters with vector search

### Multi-Tenancy
- Isolate data per tenant/customer
- Shared infrastructure with data separation
- Tenant-specific configurations

### Vector Quantization
- Compressed vector storage
- Reduced memory footprint
- Maintained search accuracy

## Use Cases

### Retrieval Augmented Generation (RAG)
- Semantic search for relevant context
- Multi-document question answering
- Knowledge-enhanced LLM responses
- Fact-grounded text generation

### Semantic Search
- Document and content discovery
- Product catalog search
- Job and talent matching
- Recommendation systems

### Knowledge Graphs
- Relationship-aware semantic search
- Entity linking and disambiguation
- Graph-based reasoning
- Knowledge base integration

### Agent Systems
- Memory for AI agents
- Context retrieval for decision-making
- Long-term agent knowledge storage
- Multi-step reasoning support

### Classification & Clustering
- Zero-shot classification
- Semantic similarity grouping
- Anomaly detection
- Pattern discovery

## Deployment Options

| Option | Best For | Setup |
|--------|----------|-------|
| **Weaviate Cloud** | Production, managed service | Serverless, auto-scaling |
| **Docker** | Development, local testing | docker-compose setup |
| **Kubernetes** | Enterprise, self-managed | Custom infrastructure |
| **Embedded** | Prototyping, evaluation | Python/JS in-process |

## Integration Patterns

### Pattern 1: LangChain + Weaviate RAG
```python
from weaviate.client import Client
from langchain.vectorstores import Weaviate
from langchain.chat_models import ChatAnthropic

# Connect to Weaviate
client = Client("http://localhost:8080")
vectorstore = Weaviate(client, index_name="Document")

# RAG retrieval
retriever = vectorstore.as_retriever()
context = retriever.get_relevant_documents(query)

# Generate with context
llm = ChatAnthropic()
response = llm.predict(input=f"Context: {context}\nQuestion: {query}")
```

### Pattern 2: Hybrid Search
```graphql
query {
  Get {
    Article(
      where: {
        path: ["published"]
        operator: GreaterThan
        valueDate: "2024-01-01"
      }
      nearText: {
        concepts: ["machine learning"]
        distance: 0.7
      }
      hybrid: {
        query: "AI models"
        alpha: 0.7
      }
      limit: 10
    ) {
      title
      content
      _additional {
        distance
        score
      }
    }
  }
}
```

### Pattern 3: Multi-Tenant Search
```python
# Isolate data per tenant
client.data_object.create(
    data_object={
        "title": "Document",
        "tenant_id": "customer-123"
    },
    class_name="Document",
    tenant="customer-123"
)

# Query with tenant isolation
results = client.query.get("Document").with_tenant("customer-123").do()
```

## Comparison with Other Vector Databases

| Feature | Weaviate | Pinecone | Milvus | Qdrant |
|---------|----------|----------|--------|--------|
| **Self-Hosted** | ✓ | ✗ | ✓ | ✓ |
| **GraphQL API** | ✓ | ✗ | ✗ | ✗ |
| **Hybrid Search** | ✓ | ✓ | ✗ | ✓ |
| **Multi-Tenancy** | ✓ | ✓ | ✓ | ✓ |
| **Managed Cloud** | ✓ | ✓ | ✗ | ✓ |
| **LangChain Support** | ✓ | ✓ | ✓ | ✓ |
| **Ease of Setup** | ◐ | ✓ | ◐ | ✓ |

## Embedding Models Supported

### Built-in Vectorizers
- **OpenAI**: text-embedding-3-small, text-embedding-3-large
- **Cohere**: embed-english-v3.0, embed-english-light-v3.0
- **HuggingFace**: Default models and custom models
- **Google**: PaLM embeddings
- **Ollama**: Local model embeddings

### Custom Embeddings
- Use external embedding services
- Manage embeddings separately
- Bring your own vectors

## Use with Other Services

### Vector DB Stack
- [Pinecone](../pinecone/) - Alternative managed vector DB
- [Supabase](../supabase/) - PostgreSQL with pgvector support
- [Cloudflare Vectorize](../cloudflare/) - Edge vector database

### AI Platforms
- [Anthropic](../../ai-platforms/anthropic/) - Claude models
- [OpenRouter](../../ai-platforms/openrouter/) - Multi-model access
- [Cohere](../../ai-platforms/cohere/) - Embeddings & reranking

### AI Frameworks
- [LangChain](../../ai-frameworks/langchain/) - Primary integration framework
- [LlamaIndex](../../ai-frameworks/llamaindex/) - Data indexing support
- [LangGraph](../../ai-frameworks/langgraph/) - Agent workflows

### Deployment
- [Vercel](../../web-frameworks/vercel/) - Web app deployment
- [Cloudflare Workers](../cloudflare/) - Edge computing
- [Kubernetes](https://kubernetes.io/) - Container orchestration

## Configuration Examples

### Docker Deployment
```yaml
version: '3.4'
services:
  weaviate:
    image: semitechnologies/weaviate:latest
    environment:
      QUERY_DEFAULTS_LIMIT: 100
      AUTHENTICATION_APIKEY_ENABLED: "true"
      AUTHENTICATION_APIKEY_ALLOWED_KEYS: "supersecret"
      PERSISTENCE_DATA_PATH: "/var/lib/weaviate"
    ports:
      - "8080:8080"
    volumes:
      - weaviate_data:/var/lib/weaviate
volumes:
  weaviate_data:
```

### Schema Definition
```graphql
mutation {
  ClassCreate(
    class: {
      class: "Document"
      description: "A text document"
      vectorizer: "text2vec-openai"
      properties: [
        {
          name: "title"
          description: "The document title"
          dataType: ["string"]
        }
        {
          name: "content"
          description: "The document content"
          dataType: ["text"]
        }
        {
          name: "published"
          description: "Publication date"
          dataType: ["date"]
        }
      ]
    }
  ) {
    class
  }
}
```

## Performance Characteristics

- **Search Latency**: Sub-second semantic search for billions of vectors
- **Throughput**: Millions of requests per day
- **Storage**: Compressed vectors reduce footprint by 10-100x
- **Scaling**: Linear scaling with vector count
- **Replication**: Built-in replication and backup support

## Getting Started

### Quick Start (Docker)
```bash
docker-compose up weaviate
```

Then access at http://localhost:8080

### Python Client
```bash
pip install weaviate-client
```

```python
import weaviate

client = weaviate.Client("http://localhost:8080")

# Create data
client.data_object.create(
    data_object={"title": "Article", "content": "..."},
    class_name="Article"
)

# Search
results = client.query.get("Article").with_near_text({
    "concepts": ["machine learning"]
}).do()
```

### JavaScript/TypeScript
```bash
npm install weaviate-client
```

```typescript
import weaviate from 'weaviate-client';

const client = weaviate.client({
  scheme: 'http',
  host: 'localhost:8080',
});

const result = await client.data.creator()
  .withClassName('Article')
  .withProperties({title: 'Article', content: '...'})
  .do();
```

## Learning Resources

### Official Resources
- **Documentation**: https://docs.weaviate.io/
- **GitHub**: https://github.com/weaviate/weaviate
- **Academy**: https://academy.weaviate.io/ (Free courses)
- **Community Slack**: https://slack.weaviate.io/

### Guides & Tutorials
- [Weaviate & LangChain](https://docs.weaviate.io/developers/weaviate/integrate/llamaindex)
- [Hybrid Search Guide](https://docs.weaviate.io/developers/weaviate/search/hybrid)
- [Multi-Tenancy Setup](https://docs.weaviate.io/developers/weaviate/manage-data/multi-tenancy)
- [RAG Patterns](https://docs.weaviate.io/developers/weaviate/tutorials/rag)

## Full Documentation

📄 [Complete Weaviate Documentation](./llms-full.txt) - Comprehensive reference including API details, advanced features, and best practices.

---

## Related Vector Databases

- **[Pinecone](../pinecone/)** - Managed, fully serverless vector database (comparison)
- **[Supabase](../supabase/)** - PostgreSQL with pgvector for hybrid storage (alternative)
- **[Cloudflare Vectorize](../cloudflare/)** - Edge-based vector database (comparison)

## Common Questions

**Q: Weaviate vs Pinecone - which should I choose?**
- **Weaviate**: If you need self-hosting, GraphQL API, or transparent architecture
- **Pinecone**: If you prefer fully managed service and simpler setup

**Q: Can I use Weaviate with Anthropic Claude?**
Yes! Use with LangChain's Weaviate vectorstore integration with Claude models.

**Q: Does Weaviate support local deployment?**
Yes! Docker, Kubernetes, and Embedded Weaviate options available.

**Q: What embedding models does Weaviate support?**
OpenAI, Cohere, HuggingFace, Google, Ollama, and custom embeddings.

---

*Part of the [Infrastructure & Services](../) documentation hub*
