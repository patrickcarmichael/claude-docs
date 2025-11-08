# Chroma

**Open-Source Vector Database for AI Applications** | ~4.2MB

Lightweight, developer-friendly vector database designed for building semantic search and RAG applications with embeddings.

## Overview

Chroma is an AI-native vector database that makes it easy to build AI applications with semantic search and retrieval. It's designed for developers and combines the simplicity of SQLite with the power of vector embeddings.

- **Type**: Vector database (open-source)
- **Best For**: Prototyping, development, local AI applications
- **Deployment**: Local (in-memory/SQLite), Docker, Chroma Cloud
- **Language Support**: Python, JavaScript/TypeScript

## Key Characteristics

### Developer-Friendly
- Simple, intuitive API
- SQLite-based persistent storage
- In-memory mode for quick prototyping
- Automatic embedding generation

### Performance
- Fast similarity search with HNSW indexing
- Metadata filtering for refined queries
- Efficient batch operations
- Optimizable index configuration

### Flexibility
- Multiple deployment modes (local, Docker, cloud)
- Custom embedding model support
- Configurable distance metrics (cosine, L2, inner product)
- Multiple language SDK support

## Quick Start

### Installation
```bash
# Python
pip install chromadb

# Node.js
npm install chromadb
```

### Basic Usage
```python
import chromadb

# Create client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="documents")

# Add documents
collection.add(
    ids=["1", "2"],
    documents=["Document 1", "Document 2"]
)

# Query
results = collection.query(
    query_texts=["Search query"],
    n_results=5
)
```

## Use Cases

### Retrieval-Augmented Generation (RAG)
Store documents and retrieve relevant context for LLM prompts to provide grounded responses.

### Semantic Search
Build search functionality based on meaning rather than keyword matching for better results.

### Recommendation Systems
Find similar items by comparing embeddings within metadata constraints.

### Question Answering
Index knowledge bases and retrieve relevant documents to answer user questions.

### Duplicate Detection
Identify similar or duplicate documents by querying embedding similarity.

### Personal Knowledge Management
Create searchable repositories of notes, articles, and documents with semantic organization.

## Core Features

### Collections
Organize embeddings by topic or data type:

```python
collection = client.create_collection(name="my_documents")
```

### Metadata Filtering
Combine vector similarity with metadata filters:

```python
results = collection.query(
    query_texts=["query"],
    where={"category": "technology", "year": {"$gte": 2020}}
)
```

### Custom Embeddings
Use OpenAI, Hugging Face, or custom embedding models:

```python
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your_key",
    model_name="text-embedding-3-small"
)
```

### Multiple Deployment Modes
- **In-memory**: Quick prototyping (ephemeral)
- **SQLite**: Local persistent storage
- **Docker**: Containerized deployment
- **HTTP Client**: Remote server connection
- **Chroma Cloud**: Managed service

### Distance Metrics
- **Cosine**: Default, recommended for text
- **L2**: Euclidean distance
- **IP**: Inner product

## Integration Patterns

### LangChain Integration
```python
from langchain.vectorstores import Chroma

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

retriever = vectorstore.as_retriever()
```

### OpenAI Integration
```python
# Store documents with OpenAI embeddings
collection = client.create_collection(
    name="documents",
    embedding_function=OpenAIEmbeddingFunction(api_key=key)
)

# Retrieve and use with ChatGPT
context = collection.query(query_texts=[question], n_results=3)
```

### Custom Application Integration
```python
# Add documents from various sources
collection.add(
    ids=document_ids,
    documents=document_texts,
    metadatas=metadata_list
)

# Query in your application
results = collection.query(
    query_texts=[user_input],
    n_results=10,
    where=filters
)
```

## Advantages

- **Open Source**: Full control, no vendor lock-in
- **Easy Setup**: Works out of the box for development
- **Flexible**: Multiple deployment and embedding options
- **Fast**: HNSW indexing for efficient similarity search
- **Developer-Focused**: Simple API, clear documentation
- **Production-Ready**: Supports persistent storage and authentication

## Limitations

- **Scale**: Better for development; enterprise scale requires Chroma Cloud
- **Complex Queries**: Limited to similarity + metadata filtering
- **Distributed**: No built-in horizontal scaling for local deployment
- **Multi-tenancy**: Limited built-in multi-tenant support in local mode
- **Query Language**: No SQL-like query language for complex operations

## When to Use Chroma

### Choose Chroma if:
- Building prototypes or MVPs quickly
- Need local development environment
- Want open-source without cloud dependency
- Building small to medium-scale RAG applications
- Team prefers simple, developer-friendly APIs

### Consider alternatives if:
- Need extreme scale (billions of vectors)
- Require highly available distributed system
- Need complex, production-grade infrastructure
- Building enterprise SaaS platform
- Require advanced filtering and aggregations

## Compared to Other Vector Databases

| Feature | Chroma | Pinecone | Weaviate | Qdrant |
|---------|--------|----------|----------|--------|
| **Type** | Open-source | Managed | Open-source | Open-source |
| **Deployment** | Local/Docker/Cloud | Cloud | Self-hosted/Cloud | Self-hosted/Cloud |
| **Ease of Use** | Very Easy | Easy | Moderate | Moderate |
| **Scale** | Small-Medium | Enterprise | Medium-Large | Medium-Large |
| **Filtering** | Metadata | Hybrid search | Filters | Filters |
| **Cost** | Free (local) | Pay-per-use | Infrastructure | Infrastructure |
| **Community** | Growing | Large | Large | Growing |

## Documentation

Full documentation available at: [llms-full.txt](./llms-full.txt)

Includes:
- Detailed API reference
- Embedding model configuration
- Deployment guides
- Advanced features and optimization
- Integration patterns
- Best practices and troubleshooting

## Examples

### Example 1: RAG Pipeline
```python
import chromadb
from openai import OpenAI

# Set up Chroma
client = chromadb.Client()
collection = client.create_collection(name="docs")

# Index documents
collection.add(
    ids=[str(i) for i in range(len(docs))],
    documents=docs
)

# Query and augment prompt
def answer_question(question):
    context = collection.query(
        query_texts=[question],
        n_results=3
    )

    prompt = f"Context: {context['documents']}\nQuestion: {question}"

    response = OpenAI.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response
```

### Example 2: Semantic Search API
```python
import chromadb

collection = client.create_collection(name="products")

# Index product catalog
collection.add(
    ids=product_ids,
    documents=product_descriptions,
    metadatas=[{"price": p, "category": c} for p, c in zip(prices, categories)]
)

# Search endpoint
def search(query, max_price=None):
    where_filter = None
    if max_price:
        where_filter = {"price": {"$lte": max_price}}

    return collection.query(
        query_texts=[query],
        where=where_filter,
        n_results=10
    )
```

### Example 3: Document Deduplication
```python
# Find similar documents
def find_duplicates(document_id, similarity_threshold=0.95):
    doc = collection.get(ids=[document_id])

    similar = collection.query(
        query_embeddings=doc["embeddings"],
        n_results=10
    )

    # Filter by similarity threshold
    duplicates = [
        (doc_id, distance)
        for doc_id, distance in zip(similar["ids"][0], similar["distances"][0])
        if distance < (1 - similarity_threshold)
    ]
    return duplicates
```

## Resources

- **GitHub Repository**: https://github.com/chroma-core/chroma
- **Official Website**: https://www.trychroma.com
- **Documentation**: https://docs.trychroma.com
- **Discord Community**: https://discord.gg/MMeYNTmh7f
- **Blog**: https://blog.trychroma.com

## Related Services

### Alternative Vector Databases
- **[Pinecone](../pinecone/)** - Fully managed, enterprise-scale
- **[Weaviate](../weaviate/)** - GraphQL-based vector database
- **[Qdrant](../qdrant/)** - Production-ready with filtering

### Complementary Services
- **[Anthropic](../../ai-platforms/anthropic/)** - LLM API for augmentation
- **[OpenRouter](../../ai-platforms/openrouter/)** - Multi-model LLM access
- **[LangChain](../../ai-frameworks/langchain/)** - Integrate with LLM frameworks
- **[LangGraph](../../ai-frameworks/langgraph/)** - Build agent workflows

## AI Use Cases

### Semantic Document Search
```
User Query → Embed Query → Vector Search in Chroma → Return Relevant Docs
```

### Knowledge-Augmented Chatbot
```
User Message → Retrieve Relevant Context from Chroma → Pass to LLM → Generate Response
```

### Recommendation Engine
```
User Preference → Find Similar Items in Chroma → Return Recommendations
```

### Multi-Document Q&A
```
Knowledge Base → Index in Chroma → Query → Retrieve Context → Answer Questions
```

## Deployment

### Local Development
```bash
pip install chromadb
python -c "import chromadb; client = chromadb.Client()"
```

### Docker
```bash
docker run -p 8000:8000 chromadb/chroma
```

### Chroma Cloud
Sign up at https://www.trychroma.com for managed hosting

## Performance Tips

1. **Batch Operations**: Add documents in batches for faster indexing
2. **Index Configuration**: Tune HNSW parameters for your use case
3. **Query Limits**: Set reasonable n_results to balance quality/speed
4. **Metadata Filtering**: Use filters to reduce search space
5. **Embedding Selection**: Choose appropriate embedding models for your domain

## Troubleshooting

### Connection Issues
- Check server is running: `chroma run --path /db_path`
- Verify host/port configuration in client
- Check firewall rules for HTTP access

### Embedding Errors
- Ensure documents are not empty strings
- Verify embedding model is properly configured
- Check API keys for external embedding services

### Query Performance
- Profile queries to identify bottlenecks
- Adjust HNSW parameters if needed
- Consider using metadata filters to narrow search space

---

*Part of the [Infrastructure & Services](../) documentation hub*
