# LlamaIndex

📄 [Full Documentation](./llms-full.txt) | 📑 [Chunked](./chunked/index.md) | ✨ [Formatted](./formatted/index.md)


**LLM Data Framework for RAG and Agents** | 1.2MB

The leading framework for building LLM-powered agents over your data. LlamaIndex specializes in data indexing, retrieval, and context augmentation for Retrieval-Augmented Generation (RAG) applications.

## Overview

LlamaIndex bridges the gap between large language models and your private data. Instead of fine-tuning, it uses intelligent indexing and retrieval to provide LLMs with relevant context for accurate answers.

**Platform Focus**: Data indexing, retrieval-augmented generation, agent workflows
**Language**: Python (also TypeScript available)
**Best For**: RAG applications, document QA, data-driven agents
**Creator**: Logan Ott, Jerry Liu, Simon Last (LlamaIndex team)

## Core Concepts

### 1. **Data Ingestion & Indexing**
- **Data Connectors**: Load from 200+ data sources (APIs, PDFs, SQL, web, etc.)
- **Data Indexing**: Create searchable indexes over your data
- **Vector Embeddings**: Convert data to embeddings for semantic search
- **Document Processing**: Parse complex documents (PDFs, tables, charts)

### 2. **Retrieval Mechanisms**
- **Vector Index**: Semantic similarity search over embeddings
- **Keyword Index**: Traditional keyword-based retrieval
- **Hybrid Retrieval**: Combine semantic and keyword search
- **Recursive Retrieval**: Multi-level indexing for hierarchical data

### 3. **Query and Chat Engines**
- **Query Engine**: Single-round QA over your data
- **Chat Engine**: Multi-turn conversations with memory
- **Structured Data Mode**: Extract specific information
- **Streaming**: Real-time response generation

### 4. **Agent Frameworks**
- **Autonomous Agents**: Self-directed task execution
- **Tool Use**: Access databases, APIs, and services
- **Agent Workflows**: Sequential and parallel task execution
- **Human-in-the-Loop**: Interactive agent supervision

## Key Features

### 50+ LLM Provider Support
- **Major Providers**: OpenAI, Claude, Gemini, Azure OpenAI, AWS Bedrock
- **Open Source**: Ollama, Mistral, Llama 2, local models
- **Specialized**: Cohere, Groq, Together AI, Fireworks
- **Flexible**: Easy provider switching and fallback strategies

### Data Connectors (200+)
- **APIs**: OpenAI, Discord, GitHub, Web services
- **Cloud**: Google Drive, Notion, Airtable, Slack
- **Databases**: SQL, MongoDB, Elasticsearch, Weaviate
- **Documents**: PDFs, Word, Excel, web scraping
- **Enterprise**: SharePoint, Salesforce, ServiceNow

### Indexing Strategies
- **Vector Indexing**: Semantic search using embeddings
- **Keyword Indexing**: BM25 and regex-based retrieval
- **Structured Data Index**: SQL and JSON queries
- **Tree Index**: Hierarchical document organization
- **Knowledge Graph**: Entity and relationship indexing

### Advanced Retrieval
- **Hybrid Search**: Semantic + keyword combination
- **Multi-Select**: Parallel retrieval from multiple indexes
- **Recursive**: Multi-level document navigation
- **Reranking**: Post-retrieval result ranking
- **Query Transformation**: Optimize queries before retrieval

## Use Cases

### Document Question Answering
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What are the main topics?")
```

**Applications**:
- Financial document analysis (earnings calls, research)
- Legal document review (contracts, regulations)
- Medical record QA (patient histories, research papers)
- Technical documentation search

### Chat with Your Data
```python
chat_engine = index.as_chat_engine()
response = chat_engine.chat("Tell me about recent developments")
```

**Applications**:
- Customer support chatbots
- Interactive data exploration
- Research assistants
- Knowledge management

### Autonomous Agents
```python
from llama_index.core.agent import AgentRunner

agent = AgentRunner.from_llm_and_tools(
    llm=llm,
    tools=[database_tool, search_tool, calculator_tool]
)
response = agent.chat("Analyze our Q3 sales data")
```

**Applications**:
- Research automation
- Business process automation
- Data analysis workflows
- Task scheduling and execution

### Multi-Modal RAG
```python
# Process images, tables, and text
index = VectorStoreIndex.from_documents(
    documents,
    show_progress=True
)
```

**Applications**:
- Visual document analysis
- Scientific paper comprehension
- Architectural documentation
- Product catalog search

## LLM Integration

### Supported Providers

**Production Enterprise**:
- OpenAI (GPT-4, GPT-4 Vision)
- Anthropic Claude 3 (Opus, Sonnet, Haiku)
- Google Gemini (Pro, Ultra)
- Azure OpenAI
- AWS Bedrock

**Cost-Effective**:
- Mistral AI
- Groq (ultra-fast)
- Together AI
- Fireworks AI

**Open Source & Local**:
- Ollama (free, local)
- LlamaCPP
- Hugging Face models
- vLLM servers

📄 **Full Provider Details**: [LLM Integrations](./llms-full.txt)

### Provider Selection Strategy

**For RAG Quality**: Use Claude 3 Opus or GPT-4 for best retrieval quality

**For Cost**: Use Mistral or Groq for 10-50x cost savings

**For Privacy**: Use Ollama or local models for zero data transmission

**For Speed**: Use Groq (50ms latency) for real-time applications

## Architecture Components

```
Your Data
    ↓
Data Connectors (200+ sources)
    ↓
Documents → Chunking → Embeddings
    ↓
Vector Store (Pinecone, Weaviate, etc.)
    ↓
Indexing Layer
    ↓
Retrieval Pipeline
    ↓
LLM (50+ providers)
    ↓
Chat/Query Engines
    ↓
Agent Framework
    ↓
Application Output
```

## Comparison with Other Frameworks

| Aspect | LlamaIndex | LangChain | LangGraph | CrewAI |
|--------|-----------|-----------|-----------|--------|
| **RAG Specialization** | ✓ Specialized | ◐ General | ✗ Limited | ✗ Limited |
| **Data Indexing** | ✓ Built-in | ◐ Basic | ✗ No | ✗ No |
| **Vector DB Support** | ✓ 20+ | ✓ 15+ | ✗ Limited | ◐ Some |
| **Agent Framework** | ✓ Yes | ✓ Yes | ✓ Advanced | ✓ Specialized |
| **Multi-Agent** | ◐ Basic | ◐ Basic | ✓ Yes | ✓ Specialized |
| **LLM Providers** | ✓ 50+ | ✓ 50+ | ✓ 40+ | ✓ 40+ |
| **Learning Curve** | Easy | Medium | High | Medium |

## Getting Started

### Installation
```bash
pip install llama-index
# or with specific integrations
pip install llama-index-llms-openai
pip install llama-index-embeddings-openai
```

### Basic RAG Example
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

# Load documents
documents = SimpleDirectoryReader("./data").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("Your question here?")
print(response)
```

### Configuration
```python
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Configure LLM and embeddings
Settings.llm = OpenAI(model="gpt-4")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-large")

# All indexes now use these settings
index = VectorStoreIndex.from_documents(documents)
```

## Advanced Topics

### Custom Indexing
- Create custom index types for specialized data
- Implement domain-specific retrieval logic
- Optimize for your specific use cases

### Vector Store Integration
- **Pinecone**: Managed vector search
- **Weaviate**: Open-source vector database
- **Milvus**: Scalable vector storage
- **Qdrant**: Optimized similarity search
- **Chroma**: Embedded vector database

### LlamaCloud Services
- **LlamaParse**: Advanced document parsing (tables, figures, OCR)
- **LlamaExtract**: Structured data extraction
- **LlamaIndex Cloud**: Managed indexing and retrieval

### Observability & Evaluation
- **CallbackHandlers**: Monitor LLM calls and costs
- **Evaluators**: Assess response quality
- **Tracing**: Debug agent workflows
- **Metrics**: Track performance and costs

## Integration Patterns

### LlamaIndex + Vector Database
```
LlamaIndex Indexes → Pinecone/Weaviate → RAG Application
```
**See**: [Pinecone Integration](../../infrastructure/pinecone/)

### LlamaIndex + Claude
```
Your Data → LlamaIndex RAG → Claude 3 LLM → High-quality answers
```
**See**: [Claude Integration Guide](../../ai-platforms/anthropic/)

### LlamaIndex + LangChain
```
LlamaIndex (Retrieval) → LangChain (Chains) → Application
```
**See**: [LangChain Documentation](../langchain/)

### LlamaIndex + Agents
```
LlamaIndex Retrieval → Agent Tools → Autonomous Task Execution
```
**See**: [Agent Framework Documentation](./llms-full.txt) | [Chunked Version](./chunked/index.md)

## Performance Tips

### Indexing Performance
- Use batch processing for large datasets
- Leverage async operations for parallel processing
- Select appropriate chunking strategies
- Use vector store caching

### Query Performance
- Implement response caching
- Use similarity thresholds to filter results
- Leverage reranking for quality
- Stream responses for UI responsiveness

### Cost Optimization
- Use Mistral or Groq instead of OpenAI (10-50x cheaper)
- Implement token budgeting
- Cache embeddings and indexes
- Use fallback to cheaper models

### Latency Reduction
- Use Groq for ultra-fast inference (50ms)
- Stream responses to client
- Parallelize retrieval with multiple indexes
- Cache frequent queries

## Enterprise Features

### LlamaCloud
- **LlamaParse**: Industrial-strength document parsing
- **LlamaExtract**: Automatic structured data extraction
- **Indexing Pipeline**: Managed end-to-end solution
- **Enterprise Support**: SLA and dedicated support

### Compliance & Security
- **Data Sovereignty**: Local model option (Ollama)
- **Access Control**: Role-based permissions
- **Audit Logging**: Complete audit trails
- **Encryption**: In-transit and at-rest options

## Related Documentation

### AI Development
- **[LangChain](../langchain/)** - General LLM application framework
- **[LangGraph](../langgraph/)** - Complex agent workflows
- **[CrewAI](../crewai/)** - Multi-agent orchestration
- **[MCP](../mcp/)** - Model Context Protocol for integrations

### Infrastructure
- **[Pinecone](../../infrastructure/pinecone/)** - Vector database
- **[Weaviate](../../infrastructure/weaviate/)** - Vector search
- **[Chroma](../../infrastructure/chroma/)** - Embedded vectors

### AI Platforms
- **[Anthropic Claude](../../ai-platforms/anthropic/)** - Claude LLM
- **[OpenAI](../../ai-platforms/openai/)** - GPT models
- **[Google Gemini](../../ai-platforms/google/)** - Gemini models

### Web Frameworks
- **[Next.js](../../web-frameworks/nextjs/)** - Build RAG UIs
- **[Streamlit](../../web-frameworks/streamlit/)** - Quick prototyping
- **[FastAPI](../../web-frameworks/fastapi/)** - API backends

## Learning Resources

### Official Documentation
- **Main Docs**: https://docs.llamaindex.ai/
- **Developers Guide**: https://developers.llamaindex.ai/python/framework/
- **LlamaHub**: Community integrations

### Community
- **Discord**: Community support and discussions
- **GitHub**: Open-source contributions
- **Blog**: Tutorials and case studies
- **Twitter/LinkedIn**: Latest updates

## Key Differentiators

### vs LangChain
- **Advantage**: Better RAG capabilities, easier retrieval customization
- **LangChain Strength**: More general-purpose, larger ecosystem
- **Use Case**: Choose LlamaIndex for RAG, LangChain for general chains

### vs LangGraph
- **Advantage**: Simpler learning curve, built-in data handling
- **LangGraph Strength**: More powerful agent state management
- **Use Case**: Use LlamaIndex for basic agents, LangGraph for complex workflows

### vs Custom Solutions
- **Advantage**: Pre-built integrations, faster development, battle-tested
- **Custom Strength**: Complete flexibility
- **Use Case**: Choose LlamaIndex for faster time-to-market

## File References

- **LLM Integrations**: [llms-full.txt](./llms-full.txt) - 50+ LLM providers with configuration
- **Framework Guide**: https://developers.llamaindex.ai/python/framework/

---

*Part of the [AI Frameworks](../) documentation hub*

**Created**: November 2024
**Last Updated**: November 2024
**Source**: https://docs.llamaindex.ai/ | https://developers.llamaindex.ai/
