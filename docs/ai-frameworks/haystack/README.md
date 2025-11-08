# 🔍 Haystack

**Production-Ready LLM Orchestration Framework** | 368KB

Haystack is an end-to-end framework for building production-ready LLM applications with emphasis on retrieval-augmented generation (RAG), semantic search, and document intelligence at scale.

- **Focus**: RAG pipelines, document retrieval, semantic search, question answering
- **Language**: Python
- **Maturity**: Production-proven (enterprise deployments)
- **Best For**: Scaled document intelligence, RAG systems, enterprise search
- **Philosophy**: Vendor-neutral, component-based pipeline architecture

📄 [Full Documentation](./llms-full.txt)

## Key Features

- **Retrieval-Augmented Generation (RAG)**
  - Vector database integration (Pinecone, Weaviate, Qdrant, etc.)
  - Advanced hybrid retrieval strategies
  - Document indexing and semantic search

- **LLM Integration**
  - Support for OpenAI, Cohere, Anthropic Claude, and 30+ providers
  - Self-hosted model support (Llama, Mistral, etc.)
  - AWS Bedrock, Azure OpenAI, SageMaker integration

- **Production Focus**
  - Stability and backward compatibility
  - Enterprise-grade deployments
  - Monitoring and observability
  - Telemetry for optimization

- **Flexible Pipeline Architecture**
  - Component-based design
  - Custom component development
  - Complex workflow orchestration
  - Transparent data flow

- **Developer Tools**
  - deepset Studio: Visual pipeline builder
  - Hayhooks: REST API wrapper
  - CLI for pipeline management
  - Comprehensive documentation

## Use Cases

### Document Intelligence
```python
# Build a searchable knowledge base
from haystack import Pipeline
from haystack.components.retrievers import DensePassageRetriever
from haystack.components.generators import OpenAIGenerator

pipeline = Pipeline()
pipeline.add_component("retriever", retriever)
pipeline.add_component("generator", generator)

result = pipeline.run({"retriever": {"query": "What is...?"}})
```

**Best For:**
- Enterprise document search
- Internal knowledge bases
- Technical documentation systems
- FAQ automation

### Semantic Search
- Product recommendation engines
- Content discovery systems
- Academic paper search
- Legal document analysis

### Question Answering
- Customer support automation
- Research assistants
- Domain expertise tools
- Multi-document QA

## Framework Comparison

### vs. LangChain
- **Haystack**: More focused on RAG and production deployment
- **LangChain**: Broader agent and chain orchestration
- **Overlap**: Both support LLM orchestration, but different strengths
- **Choose Haystack if**: You need specialized RAG at scale
- **Choose LangChain if**: You need general-purpose LLM app building

### vs. LlamaIndex
- **Haystack**: Full pipeline orchestration framework
- **LlamaIndex**: Data indexing and retrieval focus
- **Haystack**: More flexible for complex workflows
- **LlamaIndex**: Simpler for pure indexing scenarios

### vs. LangGraph
- **Haystack**: Production RAG framework
- **LangGraph**: Advanced agent state management
- **Haystack**: Better for information retrieval
- **LangGraph**: Better for agentic workflows with complex reasoning

## Installation

```bash
# Basic installation
pip install haystack-ai

# With vector database support
pip install haystack-ai[pinecone]
pip install haystack-ai[weaviate]

# Docker deployment
docker pull deepset/haystack:latest
```

## Key Components

### Retrievers
- **DensePassageRetriever**: Vector-based semantic search
- **BM25Retriever**: Keyword-based retrieval
- **HybridRetriever**: Combined semantic + keyword search

### Generators
- **OpenAIGenerator**: GPT-4, GPT-3.5 integration
- **CohereGenerator**: Cohere model support
- **HuggingFaceGenerator**: Open-source model support
- **Custom generators**: Build your own LLM integration

### Pipelines
- **Document processing**: Extract, convert, index documents
- **Query execution**: Run complex retrieval workflows
- **Result aggregation**: Combine multiple retrieval results

### Vector Stores
Supported databases:
- Pinecone
- Weaviate
- Qdrant
- Milvus
- Elasticsearch
- Custom implementations

## Production Deployment

### deepset Studio
- Visual pipeline builder
- No-code pipeline creation
- Real-time testing and monitoring
- One-click deployment

### Hayhooks
- REST API wrapper
- OpenAI-compatible endpoints
- Load balancing
- Integration with external systems

### Enterprise Support
- Haystack Enterprise for expert guidance
- deepset AI Platform for managed hosting
- Custom component development
- Performance optimization consulting

## Learning Resources

**Official Documentation**: https://docs.haystack.deepset.ai

**Getting Started**:
- [Installation Guide](https://docs.haystack.deepset.ai/docs/installation)
- [Quick Start Tutorial](https://docs.haystack.deepset.ai/docs/get_started)
- [Core Concepts](https://docs.haystack.deepset.ai/docs/components)

**GitHub Resources**:
- [Main Repository](https://github.com/deepset-ai/haystack)
- [Tutorials](https://github.com/deepset-ai/haystack-tutorials)
- [Examples](https://github.com/deepset-ai/haystack/tree/main/examples)

**Community**:
- Discord: Official Haystack Discord community
- Stack Overflow: Tag 'haystack'
- GitHub Discussions
- Blog: https://www.deepset.ai/blog

## Related Frameworks

**Building Blocks with Haystack**:

### Haystack + LangChain
Combine Haystack's RAG strengths with LangChain's orchestration:
```
LangChain Agent → Haystack RAG Pipeline → Results
```
[See LangChain docs](../langchain/)

### Haystack + LlamaIndex
Use both for different retrieval strategies:
```
LlamaIndex Data Indexing ← → Haystack Pipeline → Output
```
[See LlamaIndex docs](../llamaindex/)

### Haystack + MCP
Connect external data sources:
```
Haystack Pipeline → MCP Server → External Data
```
[See MCP docs](../mcp/)

## Notable Users

Haystack powers applications at:
- Apple
- Meta
- Netflix
- Databricks
- Airbus
- NVIDIA
- Intel
- And 100+ organizations globally

## When to Use Haystack

### Choose Haystack If You Need:
✅ Production-ready RAG systems
✅ Enterprise-scale document retrieval
✅ Vendor-neutral LLM integration
✅ Complex pipeline orchestration
✅ Stable, backward-compatible API
✅ Team-based development tools
✅ Self-hosted deployment options

### Consider Alternatives If You Need:
- Simple agent workflows → [LangGraph](../langgraph/)
- Pure data indexing → LlamaIndex
- General LLM orchestration → [LangChain](../langchain/)
- Protocol-based integration → [MCP](../mcp/)

## Integration with AI Platforms

Haystack works seamlessly with:
- **[Anthropic Claude](../../ai-platforms/anthropic/)** - Enterprise LLM
- **[OpenAI](../../ai-platforms/openai/)** - GPT models
- **[Cohere](../../ai-platforms/cohere/)** - Enterprise AI
- **[Together.ai](../../ai-platforms/together-ai/)** - Open-source models

## Development Workflow

### 1. Design Pipeline
Use deepset Studio or code to define your pipeline structure.

### 2. Prototype Locally
Test components and pipeline logic on your machine.

### 3. Integrate Data
Connect to your vector database and document sources.

### 4. Build & Test
Create retrieval and generation components.

### 5. Monitor & Optimize
Use telemetry and monitoring to improve performance.

### 6. Deploy
Use Hayhooks or Docker for production deployment.

## Quick Start Example

```python
from haystack import Pipeline
from haystack.components.retrievers import DensePassageRetriever
from haystack.components.generators import OpenAIGenerator
from haystack.document_stores import InMemoryDocumentStore

# 1. Create document store
doc_store = InMemoryDocumentStore()

# 2. Add documents
documents = [
    {"content": "Haystack is an LLM framework"},
    {"content": "RAG improves LLM answers with retrieval"}
]
doc_store.write_documents(documents)

# 3. Create retriever
retriever = DensePassageRetriever(document_store=doc_store)

# 4. Create generator
generator = OpenAIGenerator()

# 5. Build pipeline
pipeline = Pipeline()
pipeline.add_component("retriever", retriever)
pipeline.add_component("generator", generator)
pipeline.connect("retriever.documents", "generator.documents")

# 6. Run pipeline
results = pipeline.run({
    "retriever": {"query": "What is RAG?"},
})

print(results["generator"]["replies"])
```

## Key Advantages

1. **Enterprise-Grade**
   - Production-proven deployments
   - Stable API and backward compatibility
   - Professional support available

2. **RAG Specialized**
   - Purpose-built for retrieval workflows
   - Advanced retrieval strategies
   - Optimization for large-scale documents

3. **Flexible Architecture**
   - Component-based design
   - Custom component support
   - Complex workflow capabilities

4. **Vendor Neutral**
   - Works with any LLM provider
   - Self-hosted and cloud deployment
   - Multiple vector database options

5. **Developer Experience**
   - Clear API design
   - Visual pipeline builder
   - Active community
   - Comprehensive documentation

## Resources

- **Website**: https://www.deepset.ai/
- **Documentation**: https://docs.haystack.deepset.ai
- **GitHub**: https://github.com/deepset-ai/haystack
- **GitHub Discussions**: Community support and discussions
- **Blog**: https://www.deepset.ai/blog

---

*Part of the [AI Frameworks documentation](../)*
