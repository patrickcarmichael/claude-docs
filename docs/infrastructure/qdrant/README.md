# Qdrant

**High-Performance Vector Database for Semantic Search & RAG**

Qdrant is a Rust-based, open-source vector database platform specializing in similarity search and retrieval-augmented generation (RAG) for AI applications.

## Platform Overview

- **Type**: Vector database (managed cloud, hybrid, and self-hosted)
- **Language**: Written in Rust for high performance
- **License**: Open source (AGPL-3.0)
- **Primary Use**: Similarity search, RAG, semantic similarity

## Key Features

### Core Capabilities

- **Hybrid Search**: Combine dense vectors (semantic similarity) with sparse vectors (keyword matching) in a single query
- **Retrieval-Augmented Generation (RAG)**: Efficient nearest neighbor search with advanced payload filtering
- **Multivector Support**: Token-level embeddings for late interaction models like ColBERT
- **Advanced Indexing**: HNSW-based (Hierarchical Navigable Small World) indexing with configurable parameters
- **Payload Filtering**: Filter results based on metadata and structured data
- **Scalability**: Handle billions of vectors with low latency

### Technical Highlights

- Built in **Rust** for performance and memory efficiency
- **FastEmbed** integration for efficient local embedding generation
- **REST and gRPC APIs** for flexible integration
- **Official clients**: Python, JavaScript, Rust, Go, Java, .NET
- **Data sovereignty**: Full control over data location and compliance
- **Enterprise-ready**: High availability, zero-downtime upgrades, comprehensive monitoring

## Deployment Options

### 1. Managed Cloud
- SaaS solution with full management
- Automatic scaling and backups
- No infrastructure maintenance required
- Best for production applications

### 2. Hybrid Cloud
- Run Qdrant on your own Kubernetes clusters
- Use Qdrant cloud console for management
- Maintain data sovereignty
- Balance control and convenience

### 3. Self-Hosted
- Docker-based deployment
- Full control and customization
- Run locally, on-premises, or private clouds
- Best for specific compliance requirements

## Use Cases

### Semantic Search
- Document similarity and retrieval
- Code search
- Image similarity
- Product recommendations

### Retrieval-Augmented Generation (RAG)
- Question-answering systems
- Document-grounded chatbots
- Context retrieval for LLM prompts
- Long-context AI applications

### Recommendation Systems
- Personalized product recommendations
- Content discovery
- User similarity matching

### AI Agent Memory
- Long-term memory storage for agents
- Episodic memory for multi-turn interactions
- Knowledge base management

## Integration with AI Frameworks

### LangChain Integration
```python
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings

# Create vector store with Qdrant
vectorstore = Qdrant(
    client=qdrant_client,
    collection_name="my_collection",
    embeddings=OpenAIEmbeddings()
)

# Similarity search
results = vectorstore.similarity_search(query)
```

### LlamaIndex Integration
- Native Qdrant vector store support
- Streamlined indexing and retrieval
- Hybrid search capabilities

## Comparison with Other Vector Databases

| Feature | Qdrant | Pinecone | Weaviate |
|---------|--------|----------|----------|
| **Architecture** | Rust-based | Cloud-only | Graph-based |
| **Deployment** | Managed, Hybrid, Self-hosted | Managed cloud only | Self-hosted, cloud |
| **Hybrid Search** | Yes (dense + sparse) | Yes | Yes |
| **Filtering** | Advanced payload filtering | Advanced | Advanced |
| **Performance** | High (Rust) | High | High |
| **Cost Model** | Free tier + pay-per-use | Pay-per-use | Open source + managed |
| **Ideal For** | Flexibility, sovereignty | Simplicity, scale | Knowledge graphs, RAG |

## Pricing

- **Self-hosted**: Open source, free
- **Managed Cloud**: Pay-per-use model based on:
  - Storage (vector data)
  - API requests
  - Ingestion throughput
- **Hybrid Cloud**: Custom enterprise pricing

## Common Patterns

### Pattern 1: RAG with Qdrant and LangChain
```python
from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Initialize
client = QdrantClient("http://localhost:6333")
vectorstore = Qdrant(client, "documents", embeddings)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)

# Query
answer = qa_chain.run("What is...?")
```

### Pattern 2: Hybrid Search
```python
# Combine dense and sparse vectors
from qdrant_client import QdrantClient

client = QdrantClient("http://localhost:6333")

results = client.search_batch(
    collection_name="my_collection",
    requests=[
        {
            "vector": dense_embedding,
            "sparse_vector": sparse_embedding,
            "limit": 10,
            "filter": {
                "must": [{"key": "category", "match": {"value": "tech"}}]
            }
        }
    ]
)
```

## Getting Started

### Local Development with Docker
```bash
# Start Qdrant server
docker run -p 6333:6333 qdrant/qdrant

# Connect from Python
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
```

### Cloud Deployment
1. Sign up at [Qdrant Cloud](https://cloud.qdrant.io)
2. Create a new cluster
3. Configure API keys
4. Connect using API endpoint

### Installation
```bash
pip install qdrant-client

# With dependencies
pip install qdrant-client[fastembed]
```

## Key Resources

📄 **Full Documentation**: [llms-full.txt](./llms-full.txt)

**Official Links:**
- Website: https://qdrant.tech
- Documentation: https://docs.qdrant.tech
- GitHub: https://github.com/qdrant/qdrant
- Cloud Console: https://cloud.qdrant.io

## Related Vector Database Platforms

- **[Pinecone](../pinecone/)** - Cloud-native vector DB with managed infrastructure
- **[Weaviate](../weaviate/)** - Open-source vector DB with graph capabilities
- **Supabase pgvector** - PostgreSQL with vector support for smaller-scale applications

## Related Documentation

### AI Frameworks
- [LangChain](../../ai-frameworks/langchain/) - Build RAG applications
- [LlamaIndex](../../ai-frameworks/llamaindex/) - Data indexing for LLMs
- [MCP](../../ai-frameworks/mcp/) - Context protocol integration

### AI Platforms
- [Anthropic](../../ai-platforms/anthropic/) - Use with LLMs for RAG
- [OpenAI](../../ai-platforms/openai/) - Embeddings and chat models
- [Cohere](../../ai-platforms/cohere/) - Embeddings and reranking

### Infrastructure
- [Supabase](../supabase/) - Backend database with pgvector
- [PostgreSQL pgvector](../postgres/) - Vector extension for relational DB

---

*Part of the [AI Development Documentation Hub](../../)*
