# AI Frameworks

Frameworks and protocols for building LLM applications, agents, and workflows.

## Frameworks

### 🦜 [LangChain](./langchain/)
**LLM Application Framework** | 346KB

The most popular Python framework for building LLM applications.

- **Focus**: Chains, agents, retrieval, tool calling
- **Language**: Python (also TypeScript)
- **Best For**: RAG, chatbots, data analysis
- **Ecosystem**: Huge community, extensive integrations

📄 [Full Documentation](./langchain/llms-full.txt)

**Key Components:**
- Chains for composing LLM calls
- Memory for conversation state
- Retrieval for RAG applications
- Agents for autonomous workflows

**Related**: [LangGraph](./langgraph/) for advanced agent workflows

---

### 📊 [LangGraph](./langgraph/)
**Agent Workflow Framework** | 618KB

Advanced framework for building stateful, multi-actor agent applications.

- **Focus**: Complex agent workflows, state management
- **Language**: Python
- **Best For**: Multi-step reasoning, agentic systems
- **Part of**: LangChain ecosystem

📄 [Full Documentation](./langgraph/llms-full.txt)

**Key Features:**
- Graph-based workflow definition
- Persistent state management
- Branching and looping logic
- Human-in-the-loop support

**Use with**: [LangChain](./langchain/) for full capabilities

---

### 👥 [CrewAI](./crewai/)
**Multi-Agent Orchestration** | 1.9MB

Framework for orchestrating role-based AI agents working together.

- **Focus**: Multi-agent collaboration, role delegation
- **Language**: Python
- **Best For**: Complex tasks requiring multiple specialized agents
- **Philosophy**: Agents as team members

📄 [Full Documentation](./crewai/llms-full.txt)

**Key Concepts:**
- Agents with specific roles
- Tasks assigned to agents
- Crews coordinating agents
- Sequential and parallel execution

**Similar to**: [Claude Code Sub-Agents](../claude-code/features/sub-agents.md)

---

### 🦙 [LlamaIndex](./llamaindex/)
**LLM Data Framework for RAG** | 1.2MB

Leading framework for building LLM-powered agents over your data with intelligent indexing and retrieval.

- **Focus**: Data indexing, retrieval-augmented generation (RAG), document QA
- **Language**: Python (also TypeScript)
- **Best For**: Document Q&A, RAG applications, data-driven agents
- **Specialization**: 50+ LLM providers, 200+ data connectors

📄 [Full Documentation](./llamaindex/llms-full.txt)

**Key Features:**
- 50+ LLM provider support (OpenAI, Claude, Gemini, local models)
- 200+ data connectors (APIs, databases, PDFs, cloud storage)
- Advanced retrieval strategies (vector, keyword, hybrid, recursive)
- Agent framework for autonomous task execution
- LlamaCloud for managed document processing

**Comparison**: More specialized for RAG than [LangChain](./langchain/), simpler than [LangGraph](./langgraph/)

---

### 🔌 [MCP](./mcp/)
**Model Context Protocol** | 852KB

Protocol for connecting AI models to external data sources and tools.

- **Focus**: Standardized context integration
- **Language**: Protocol specification (multi-language)
- **Best For**: Connecting LLMs to external systems
- **Created by**: Anthropic

📄 [Full Documentation](./mcp/llms-full.txt)

**Key Features:**
- Standard protocol for context
- Server/client architecture
- Tool and resource providers
- Language-agnostic

**Implemented in**: [Claude Code MCP Integration](../claude-code/features/mcp.md)

---

### 🔍 [Haystack](./haystack/)
**Production-Ready LLM Orchestration** | 368KB

End-to-end framework for building production-ready applications powered by LLMs with emphasis on retrieval-augmented generation and document intelligence.

- **Focus**: RAG pipelines, document retrieval, semantic search
- **Language**: Python
- **Best For**: Enterprise document search, scaled information retrieval
- **Philosophy**: Vendor-neutral, component-based architecture

📄 [Full Documentation](./haystack/llms-full.txt)

**Key Features:**
- Retrieval-augmented generation (RAG) pipelines
- Advanced retrieval strategies (dense, sparse, hybrid)
- Multi-vendor LLM support
- Production-grade stability and monitoring

**Related**: [LangChain](./langchain/) for broader orchestration, [LlamaIndex](./llamaindex/) for pure indexing

---

## Framework Comparison

| Framework | Focus | Complexity | Best For |
|-----------|-------|------------|----------|
| **LangChain** | General LLM apps | Medium | RAG, chatbots, data analysis |
| **LangGraph** | Agent workflows | High | Complex multi-step agents |
| **CrewAI** | Multi-agent teams | Medium | Role-based collaboration |
| **LlamaIndex** | Data indexing & RAG | Easy-Medium | Document QA, data-driven agents |
| **Haystack** | RAG & retrieval | Medium | Enterprise document search |
| **MCP** | Context integration | Low | Connecting data sources |

---

## Choosing a Framework

### For RAG Applications
**Use**: [LangChain](./langchain/)

```python
# Example: Build a RAG chatbot
from langchain import chains, vectorstores
# See LangChain docs for full examples
```

**With**: [Pinecone](../infrastructure/pinecone/) or other vector DB

---

### For Complex Agents
**Use**: [LangGraph](./langgraph/)

```python
# Example: Multi-step agent workflow
from langgraph import graph
# Define stateful agent workflows
```

**Related**: [Claude Code Sub-Agents](../claude-code/features/sub-agents.md)

---

### For Multi-Agent Systems
**Use**: [CrewAI](./crewai/)

```python
# Example: Team of specialized agents
from crewai import Agent, Task, Crew
# Coordinate multiple agents
```

**Inspiration**: [Claude Code Sub-Agents](../claude-code/features/sub-agents.md)

---

### For Document Q&A and Data Indexing
**Use**: [LlamaIndex](./llamaindex/)

```python
# Example: Index documents and ask questions
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What are the main topics?")
```

**Best For**:
- Document question answering
- Building intelligent data indices
- RAG applications with complex data sources
- Leveraging 50+ LLM providers

**Works with**: Claude, GPT-4, Gemini, Mistral, local models

---

### For Production RAG at Scale
**Use**: [Haystack](./haystack/)

```python
# Example: Enterprise document search
from haystack import Pipeline
from haystack.components.retrievers import DensePassageRetriever
from haystack.components.generators import OpenAIGenerator
# Build retrieval pipelines with vector databases
```

**Works with**: Vector databases (Pinecone, Weaviate, Qdrant)

---

### For External Integration
**Use**: [MCP](./mcp/)

Connect your LLM to:
- Databases
- APIs
- File systems
- External tools

**Implementation**: [Claude Code MCP](../claude-code/features/mcp.md)

---

## Integration Patterns

### LangChain + Vector Database
```
LangChain → Embeddings → Pinecone → RAG Application
```

**See**:
- [LangChain Docs](./langchain/llms-full.txt)
- [Pinecone Docs](../infrastructure/pinecone/)

### LangGraph + MCP
```
LangGraph Agent → MCP Server → External Data → LLM
```

**See**:
- [LangGraph Docs](./langgraph/llms-full.txt)
- [MCP Docs](./mcp/llms-full.txt)

### CrewAI + Multiple LLMs
```
CrewAI Crew → Agent A (GPT-4) + Agent B (Claude) → Coordinated Output
```

**See**:
- [CrewAI Docs](./crewai/llms-full.txt)
- [AI Platforms](../ai-platforms/)

### LlamaIndex + Vector Database
```
Documents → LlamaIndex Indexing → Pinecone/Weaviate → Query Results
```

**See**:
- [LlamaIndex Docs](./llamaindex/llms-full.txt)
- [Pinecone](../infrastructure/pinecone/) - Vector database
- [Anthropic Claude](../ai-platforms/anthropic/) - High-quality LLM backend

---

## Use with AI Platforms

All frameworks work with:
- **[Anthropic](../ai-platforms/anthropic/)** - Claude models
- **[OpenRouter](../ai-platforms/openrouter/)** - Multi-model access
- **[Cohere](../ai-platforms/cohere/)** - Enterprise features
- **[Together.ai](../ai-platforms/together-ai/)** - Open-source models

---

## Development Workflow

### 1. Prototype
Start with [LangChain](./langchain/) for quick prototyping:
- Test LLM integrations
- Build basic chains
- Validate concepts

### 2. Scale Complexity
Move to [LangGraph](./langgraph/) for:
- State management
- Complex workflows
- Production agents

### 3. Add Context
Integrate [MCP](./mcp/) for:
- External data sources
- Tool integration
- Real-time information

### 4. Multi-Agent (if needed)
Use [CrewAI](./crewai/) when:
- Multiple specialized tasks
- Role-based delegation needed
- Parallel agent execution

---

## Related Documentation

### AI Coding Tools
- [Claude Code](../claude-code/) - CLI with built-in agents
- [Cursor](../ai-coding-tools/cursor/) - AI IDE
- [Codeium](../ai-coding-tools/codeium/) - Code completion

### Infrastructure
- [Pinecone](../infrastructure/pinecone/) - Vector database for RAG
- [Vercel](../web-frameworks/vercel/) - Deploy LangChain apps

### Web Frameworks
- [Next.js](../web-frameworks/nextjs/) - Build web UIs for agents
- [Astro](../web-frameworks/astro/) - Content-focused LLM apps

---

*Part of the [AI Development Documentation Hub](../)*
