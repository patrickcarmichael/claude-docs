---
title: Chroma Documentation
description: Complete documentation for Chroma AI-native vector database
service: chroma
version: 1.0
last_updated: 2025-11-08
---

# Chroma Documentation for LLMs

Chroma is an open-source AI-native vector database designed for building AI applications with semantic search, retrieval-augmented generation (RAG), and embedding-based retrieval.

## Overview

Chroma makes it easy to build AI applications by making knowledge, probability, and compute accessible. It combines the simplicity of SQLite with the power of vector embeddings, providing a lightweight, developer-friendly approach to building vector-powered applications.

**Official Repository:** https://github.com/chroma-core/chroma
**Website:** https://www.trychroma.com
**Documentation:** https://docs.trychroma.com

## Core Features

### Vector Database

- Native vector storage and indexing
- Fast similarity search and retrieval
- Support for various embedding models
- Automatic embedding generation with built-in models

### Developer-Friendly

- Python and JavaScript/TypeScript SDKs
- Simple API for adding, querying, and deleting embeddings
- SQLite-based persistent storage option
- In-memory mode for quick prototyping

### Multiple Deployment Modes

- Local development (in-memory or SQLite)
- Docker deployment
- Chroma Cloud (managed service)
- Self-hosted server mode

### Flexible Data Management

- Collections for organizing embeddings by topic
- Metadata filtering for advanced queries
- Support for JSON, text, and binary data
- Document chunking and management

## Installation

### Python

```bash
pip install chromadb
```

### Node.js / TypeScript

```bash
npm install chromadb
```

### Docker

```bash
docker run -p 8000:8000 chromadb/chroma
```

## Quick Start Examples

### Python - Create and Query

```python
import chromadb

# Create a client (uses in-memory SQLite by default)
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="my_collection")

# Add documents
collection.add(
    ids=["1", "2", "3"],
    documents=[
        "The capital of France is Paris",
        "The capital of Germany is Berlin",
        "The capital of Spain is Madrid"
    ],
    metadatas=[
        {"country": "France"},
        {"country": "Germany"},
        {"country": "Spain"}
    ]
)

# Query
results = collection.query(
    query_texts=["What is the capital of France?"],
    n_results=2
)

print(results)
# Returns most similar documents and their distances
```

### JavaScript/TypeScript

```javascript
import { ChromaClient } from "chromadb";

const client = new ChromaClient();

// Create a collection
const collection = await client.getOrCreateCollection({
    name: "my_collection"
});

// Add documents
await collection.add({
    ids: ["1", "2", "3"],
    documents: [
        "The capital of France is Paris",
        "The capital of Germany is Berlin",
        "The capital of Spain is Madrid"
    ],
    metadatas: [
        { country: "France" },
        { country: "Germany" },
        { country: "Spain" }
    ]
});

// Query
const results = await collection.query({
    queryTexts: ["What is the capital of France?"],
    nResults: 2
});

console.log(results);
```

## Core Operations

### Create a Collection

```python
collection = client.create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}  # Distance metric
)
```

### Add Documents

```python
collection.add(
    ids=["doc1", "doc2"],
    documents=["Document content 1", "Document content 2"],
    embeddings=[[1.2, 2.3, ...], [4.5, 5.6, ...]],  # Optional
    metadatas=[{"source": "pdf"}, {"source": "web"}],
    documents_uris=["file1.pdf", "file2.html"]  # Optional
)
```

### Query Documents

```python
# By text (automatic embedding)
results = collection.query(
    query_texts=["search query"],
    n_results=10,
    where={"source": "pdf"}  # Filter by metadata
)

# By embedding
results = collection.query(
    query_embeddings=[[1.2, 2.3, ...]],
    n_results=10
)
```

### Update Documents

```python
collection.update(
    ids=["doc1"],
    documents=["Updated content"],
    metadatas=[{"updated": True}]
)
```

### Delete Documents

```python
collection.delete(ids=["doc1"])
# Or delete by metadata filter
collection.delete(where={"source": "old_source"})
```

### Get Documents

```python
results = collection.get(
    ids=["doc1", "doc2"],
    where={"source": "pdf"}
)
```

## Embeddings

### Default Embeddings

Chroma includes default embedding models:

- **all-MiniLM-L6-v2**: Fast, ~384 dimensions
- **sentence-transformers/all-mpnet-base-v2**: High quality, ~768 dimensions

### Custom Embeddings

```python
from chromadb.utils import embedding_functions

# Hugging Face embeddings
hf_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key="your_key",
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

collection = client.create_collection(
    name="my_collection",
    embedding_function=hf_ef
)

# OpenAI embeddings
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your_key",
    model_name="text-embedding-3-small"
)
```

## Distance Metrics

Chroma supports multiple distance metrics for similarity:

- **cosine**: Cosine similarity (default, recommended for text)
- **l2**: Euclidean distance
- **ip**: Inner product

```python
collection = client.create_collection(
    name="my_collection",
    metadata={"hnsw:space": "cosine"}  # or "l2", "ip"
)
```

## Metadata Filtering

### Simple Filters

```python
# Exact match
where={"source": "pdf"}

# Multiple conditions (AND)
where={
    "$and": [
        {"source": "pdf"},
        {"year": {"$gte": 2020}}
    ]
}

# Multiple conditions (OR)
where={
    "$or": [
        {"source": "pdf"},
        {"source": "web"}
    ]
}

# Comparison operators
where={"year": {"$gt": 2020}}  # Greater than
where={"year": {"$lt": 2020}}  # Less than
where={"year": {"$gte": 2020}} # Greater than or equal
where={"year": {"$lte": 2020}} # Less than or equal
where={"year": {"$eq": 2020}}  # Equal
where={"year": {"$ne": 2020}}  # Not equal
where={"tags": {"$in": ["important", "urgent"]}}  # In list
where={"tags": {"$nin": ["spam"]}}  # Not in list
```

## Persistence

### SQLite (Default)

```python
import chromadb

# Persistent directory
client = chromadb.PersistentClient(path="/path/to/data")
```

### In-Memory (Development)

```python
client = chromadb.Client()  # Ephemeral
```

### HTTP Client (Server Mode)

```python
import chromadb

client = chromadb.HttpClient(host="localhost", port=8000)
```

## Server Mode

### Start Chroma Server

```bash
chroma run --path /db_path --port 8000
```

### Connect from Client

```python
import chromadb

client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    auth_provider="chromadb.auth.BasicAuthClientProvider",
    auth_credentials="username:password"
)
```

## Use Cases

### Retrieval-Augmented Generation (RAG)

Store documents and retrieve relevant context for LLM prompts:

```python
# Store documents
collection.add(
    ids=["doc1", "doc2"],
    documents=["Document 1 content", "Document 2 content"]
)

# Retrieve relevant context
context = collection.query(
    query_texts=["User question"],
    n_results=5
)

# Use context in LLM prompt
prompt = f"Context: {context['documents']} Question: {user_question}"
```

### Semantic Search

Build search functionality based on meaning:

```python
results = collection.query(
    query_texts=["Find articles about machine learning"],
    n_results=10,
    where={"category": "technology"}
)
```

### Recommendation Systems

Find similar items based on embeddings:

```python
# Store product descriptions
collection.add(
    ids=product_ids,
    documents=product_descriptions,
    metadatas=[{"price": p} for p in prices]
)

# Find similar products
similar = collection.query(
    query_texts=["User viewed product"],
    n_results=5,
    where={"price": {"$lt": 100}}
)
```

### Question Answering

Build QA systems with document retrieval:

```python
# Index knowledge base
kb_collection = client.create_collection("knowledge_base")
kb_collection.add(ids=doc_ids, documents=doc_texts)

# Answer questions
def answer_question(question):
    context = kb_collection.query(
        query_texts=[question],
        n_results=3
    )
    # Pass context and question to LLM
    return llm.generate(question=question, context=context)
```

### Duplicate Detection

Find similar/duplicate documents:

```python
duplicates = collection.query(
    query_embeddings=[doc_embedding],
    n_results=10
)

# Items with high similarity (low distance) are likely duplicates
```

## Advanced Features

### Batch Operations

```python
# Batch add for better performance
ids = [f"doc_{i}" for i in range(1000)]
documents = [f"Document {i}" for i in range(1000)]

collection.add(ids=ids, documents=documents)
```

### Collection Metadata

```python
# Create with metadata
collection = client.create_collection(
    name="my_collection",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 400
    }
)

# Update metadata
collection.modify(
    metadata={"description": "My updated collection"}
)
```

### List and Delete Collections

```python
# List all collections
collections = client.list_collections()

# Get collection
collection = client.get_collection(name="my_collection")

# Delete collection
client.delete_collection(name="my_collection")
```

## Performance Optimization

### Index Configuration

```python
collection = client.create_collection(
    name="optimized",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 200,  # Index construction speed
        "hnsw:search_ef": 100  # Search quality/speed
    }
)
```

### Batch Size

Process documents in optimal batch sizes:

```python
batch_size = 100
for i in range(0, len(docs), batch_size):
    batch_docs = docs[i:i+batch_size]
    collection.add(ids=ids[i:i+batch_size], documents=batch_docs)
```

### Query Parameters

```python
# Return only top N results
results = collection.query(
    query_texts=["query"],
    n_results=5  # Adjust based on needs
)
```

## Integration Patterns

### With LangChain

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

vectorstore = Chroma(
    embedding_function=OpenAIEmbeddings(),
    collection_name="documents"
)

# Use in chains
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
```

### With LangGraph

```python
from langchain_community.vectorstores import Chroma

state = {
    "query": "user question",
    "context": []
}

def retrieve_documents(state):
    results = chroma_collection.query(
        query_texts=[state["query"]],
        n_results=5
    )
    return {"context": results["documents"]}
```

### With OpenAI

```python
import openai
import chromadb

collection = client.create_collection("documents")

# Store documents
collection.add(ids=["1"], documents=["Content"])

# Retrieve and use with OpenAI
context = collection.query(query_texts=["query"], n_results=3)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": f"Context: {context}"},
        {"role": "user", "content": "User question"}
    ]
)
```

## Client Modes

### Persistent Client (Production)

```python
persistent_client = chromadb.PersistentClient(path="/path/to/db")
```

### Ephemeral Client (Testing)

```python
ephemeral_client = chromadb.Client()
```

### HTTP Client (Remote Server)

```python
http_client = chromadb.HttpClient(
    host="localhost",
    port=8000
)
```

### Transient HTTP Client

```python
transient_client = chromadb.TransientClient()
```

## Authentication

### Basic Auth

```python
client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    auth_provider="chromadb.auth.BasicAuthClientProvider",
    auth_credentials="username:password"
)
```

### Token Auth

```python
client = chromadb.HttpClient(
    host="localhost",
    port=8000,
    auth_provider="chromadb.auth.TokenAuthClientProvider",
    auth_credentials="token_value"
)
```

## Error Handling

```python
import chromadb
from chromadb.errors import InvalidCollectionException

try:
    collection = client.get_collection(name="missing")
except InvalidCollectionException:
    # Create if doesn't exist
    collection = client.create_collection(name="missing")

try:
    results = collection.query(query_texts=["query"])
except ValueError as e:
    # Handle invalid query
    print(f"Query error: {e}")
```

## Limitations and Considerations

### Scale Limits

- Local deployment suitable for millions of vectors
- For larger scale, consider Chroma Cloud
- Vector dimension typically between 384-1536

### Embedding Models

- Default models work well for English
- Consider multilingual models for international content
- Custom embeddings increase latency

### Storage

- SQLite is file-based, check disk space
- In-memory mode loses data on restart
- Use persistent mode for production

## API Reference Summary

### Collection Methods

- `add()` - Add documents/embeddings
- `query()` - Query by text or embeddings
- `update()` - Update documents
- `delete()` - Delete documents
- `get()` - Get documents by ID
- `modify()` - Modify collection metadata
- `delete()` - Delete collection
- `count()` - Get collection size

### Client Methods

- `create_collection()` - Create new collection
- `get_collection()` - Get existing collection
- `list_collections()` - List all collections
- `delete_collection()` - Delete collection
- `get_version()` - Get Chroma version
- `reset()` - Reset client (clear all data)

## Best Practices

1. **Use Persistent Storage**: In production, use PersistentClient or server mode
2. **Batch Operations**: Add documents in batches for better performance
3. **Index Configuration**: Tune HNSW parameters for your use case
4. **Metadata Filters**: Combine vector search with metadata filtering
5. **Error Handling**: Implement proper error handling and logging
6. **Embeddings**: Choose appropriate embedding models for your domain
7. **Query Limits**: Set reasonable n_results to balance performance
8. **Collection Organization**: Use separate collections for different data types

## Troubleshooting

### Connection Issues

```python
# Test connection
try:
    client.heartbeat()
    print("Connected")
except Exception as e:
    print(f"Connection failed: {e}")
```

### Embedding Errors

```python
# Ensure documents are not empty
if not documents or all(d == "" for d in documents):
    raise ValueError("Documents cannot be empty")
```

### Query Performance

```python
# Profile slow queries
import time

start = time.time()
results = collection.query(query_texts=["query"], n_results=100)
print(f"Query time: {time.time() - start}s")
```

## Related Services

- **Pinecone**: Fully managed vector database for production scale
- **Weaviate**: Open-source vector database with GraphQL API
- **Qdrant**: Vector database with filtering and multi-tenant support
- **Milvus**: Open-source vector database by LF AI

## Resources

- **GitHub**: https://github.com/chroma-core/chroma
- **Discord Community**: https://discord.gg/MMeYNTmh7f
- **Website**: https://www.trychroma.com
- **Docs**: https://docs.trychroma.com
- **Blog**: https://blog.trychroma.com

## Support

- Community Discord for questions
- GitHub Issues for bugs and feature requests
- Documentation for troubleshooting guides
- Email support for enterprise customers

---

**Navigation**: [Documentation Index](index.md) | [Source](../llms-full.txt)
