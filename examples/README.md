# Examples: AI Application Development with Claude

This directory contains **4 comprehensive, production-ready examples** demonstrating practical applications using Anthropic Claude and related AI frameworks.

Each example is fully documented, includes working code, and can be used as a starting point for your own projects.

## Examples Overview

### 1. RAG Application: LangChain + Pinecone + Anthropic
**Directory**: `/rag-app`

A complete Retrieval-Augmented Generation (RAG) system for Q&A over custom documents.

**Features**:
- Load documents from multiple formats (PDF, Markdown, Text, DOCX)
- Generate embeddings with OpenAI or Anthropic
- Vector storage with Pinecone
- Semantic search and document retrieval
- Context-augmented response generation
- Interactive chat interface
- Batch query processing

**Use Cases**:
- Knowledge base Q&A
- Document analysis
- Custom AI assistants
- Internal knowledge systems

**Tech Stack**:
- LangChain - LLM framework
- Pinecone - Vector database
- Anthropic Claude - Generation
- Python - Backend

**Quick Start**:
```bash
cd rag-app
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
python ingest.py --path ./data/documents
python chat.py
```

**Key Files**:
- `retriever.py` - RAG orchestration
- `ingest.py` - Document ingestion
- `chat.py` - Interactive interface
- `config.py` - Configuration

---

### 2. Multi-Agent System: CrewAI
**Directory**: `/multi-agent`

A sophisticated multi-agent system for complex collaborative tasks.

**Features**:
- Define specialized agents with roles and goals
- Create tasks with dependencies
- Orchestrate agent workflows
- Agent-to-agent collaboration
- Tool integration for agents
- Memory and context management
- Support for complex reasoning

**Use Cases**:
- Content creation (research → write → edit)
- Data analysis workflows
- Customer support automation
- Software development assistance
- Research and investigation

**Tech Stack**:
- CrewAI - Agent orchestration
- LangChain - Foundation
- Anthropic Claude - Agent reasoning
- Python - Backend

**Quick Start**:
```bash
cd multi-agent
pip install -r requirements.txt
cp .env.example .env  # Add your API keys
python content_crew.py --topic "Claude Code Fundamentals"
```

**Key Files**:
- `content_crew.py` - Content creation workflow
- `config.py` - Configuration
- `agents/` - Agent definitions
- `tools/` - Tool implementations

---

### 3. Chat Interface: Next.js + Streaming
**Directory**: `/chat-interface`

A modern, production-ready chat web application with real-time streaming.

**Features**:
- Real-time streaming responses
- Multi-turn conversations
- Customizable system prompts
- Model selection
- Temperature and token controls
- Responsive design (mobile, tablet, desktop)
- Message history
- Dark/light mode
- TypeScript type safety

**Use Cases**:
- AI chatbot interfaces
- Customer support chat
- Internal assistant applications
- Knowledge base chat
- Custom domain chatbots

**Tech Stack**:
- Next.js 14 - React framework
- TypeScript - Type safety
- Tailwind CSS - Styling
- Anthropic SDK - API integration
- React Hooks - State management

**Quick Start**:
```bash
cd chat-interface
npm install
cp .env.local.example .env.local  # Add your API key
npm run dev
# Open http://localhost:3000
```

**Key Files**:
- `app/api/chat/route.ts` - Server-side streaming endpoint
- `lib/useChat.ts` - Custom React hook
- `components/` - UI components

---

### 4. Claude Code Automation: Scripting & Productivity
**Directory**: `/claude-code-automation`

Automation scripts using Claude Code for AI-powered development tasks.

**Features**:
- Code generation and refactoring
- Automated test generation
- Documentation generation
- Code analysis and review
- Batch processing with parallel workers
- Integration with development workflows
- CLI automation
- Git integration

**Use Cases**:
- Automated documentation
- Bulk code refactoring
- Test generation
- Code quality analysis
- Development automation
- Project initialization

**Tech Stack**:
- Claude Code CLI - AI assistant
- Anthropic SDK - API integration
- Python - Scripting
- Click - CLI framework
- Concurrent Processing - Parallelization

**Quick Start**:
```bash
cd claude-code-automation
pip install -r requirements.txt
cp .env.example .env  # Add your API key
python scripts/code_review.py --files src/**/*.py
```

**Key Files**:
- `utils/claude_wrapper.py` - Claude API wrapper
- `utils/batch_processor.py` - Batch processing
- `scripts/` - Automation scripts

---

## Directory Structure

```
examples/
├── README.md                       # This file
│
├── rag-app/                       # RAG Application
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── config.py
│   ├── retriever.py
│   ├── ingest.py
│   ├── chat.py
│   ├── query.py
│   ├── utils/
│   │   ├── document_loader.py
│   │   └── prompt_templates.py
│   └── data/
│       └── documents/
│
├── multi-agent/                   # Multi-Agent System
│   ├── README.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── config.py
│   ├── content_crew.py
│   ├── agents/
│   ├── tools/
│   └── workflows/
│
├── chat-interface/                # Next.js Chat App
│   ├── README.md
│   ├── package.json
│   ├── .env.local.example
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── app/
│   │   ├── api/chat/
│   │   └── layout.tsx
│   ├── components/
│   ├── lib/
│   └── public/
│
└── claude-code-automation/        # Automation Scripts
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    ├── scripts/
    │   ├── generate_docs.py
    │   ├── batch_refactor.py
    │   └── code_review.py
    ├── utils/
    │   ├── claude_wrapper.py
    │   └── batch_processor.py
    └── templates/
```

## Technology Stack Summary

| Technology | Used In | Purpose |
|------------|---------|---------|
| **LangChain** | RAG, Multi-Agent | LLM application framework |
| **Pinecone** | RAG | Vector database for embeddings |
| **CrewAI** | Multi-Agent | Agent orchestration |
| **Next.js** | Chat Interface | Web framework |
| **Anthropic Claude** | All | Language model |
| **Python** | RAG, Multi-Agent, Automation | Backend logic |
| **TypeScript** | Chat Interface | Type-safe JavaScript |
| **Tailwind CSS** | Chat Interface | Styling |

## Getting Started

### Prerequisites

- **API Keys**: Anthropic API key (required for all examples)
- **Python 3.9+** (for RAG, Multi-Agent, Automation)
- **Node.js 18+** (for Chat Interface)
- Basic knowledge of Python or JavaScript

### Step-by-Step

#### 1. Clone/Download Examples

```bash
cd examples/
ls -la  # See all examples
```

#### 2. Choose an Example

Pick based on your needs:
- **Start here**: Chat Interface (simplest, web-based)
- **Learn RAG**: RAG Application
- **Advanced**: Multi-Agent System
- **Automation**: Claude Code Automation

#### 3. Follow Example README

Each example has detailed setup instructions:

```bash
cd <example-name>
cat README.md  # Read full documentation
```

#### 4. Install Dependencies

For Python examples:
```bash
pip install -r requirements.txt
```

For Node.js examples:
```bash
npm install
```

#### 5. Configure API Keys

Create `.env` or `.env.local`:
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

#### 6. Run Example

Follow the "Quick Start" section in each README.

## Common Tasks

### Run the Chat Interface Locally

```bash
cd chat-interface
npm install
npm run dev
# Open http://localhost:3000
```

### Use RAG for Q&A

```bash
cd rag-app
python ingest.py --path ./my-documents/
python chat.py
```

### Generate Documentation with Claude Code

```bash
cd claude-code-automation
python scripts/generate_docs.py --project ./my-project
```

### Create Multi-Agent Workflow

```bash
cd multi-agent
python content_crew.py --topic "Machine Learning Basics"
```

## Integration Guide

### Use RAG with Chat Interface

```typescript
// Chat interface can use RAG backend
const response = await fetch("/api/chat/rag", {
  body: JSON.stringify({
    messages,
    documents: retrievedDocs  // From RAG system
  })
});
```

### Use Multi-Agent in Chat

```python
# Multi-agent results can be returned via chat API
crew_result = crew.kickoff(inputs={...})
return ClaudeResponse(crew_result)
```

### Automate with Claude Code

```bash
# Generate tests for chat interface
cd claude-code-automation
python scripts/test_generator.py \
  --source ../chat-interface/lib/useChat.ts \
  --output ../chat-interface/__tests__/useChat.test.ts
```

## Best Practices

### Environment Variables
- Never commit `.env` files with real keys
- Use `.env.example` as template
- Keep sensitive data in environment variables
- Use different keys for dev/prod

### Error Handling
- All examples include error handling
- Check logs for debugging
- Use verbose mode for detailed output
- Add retry logic for API calls

### Performance
- Cache embeddings in RAG
- Batch process large datasets
- Use streaming for long responses
- Implement rate limiting

### Security
- Store API keys securely
- Validate user inputs
- Use HTTPS in production
- Implement authentication

## Troubleshooting

### "API Key not found"
```bash
# Check environment variable
echo $ANTHROPIC_API_KEY

# Set if missing
export ANTHROPIC_API_KEY=sk-ant-...
```

### "Module not found" (Python)
```bash
# Ensure pip dependencies installed
pip install -r requirements.txt

# Check Python path
which python3
```

### "Module not found" (Node.js)
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### "Port already in use" (Next.js)
```bash
# Use different port
npm run dev -- -p 3001
```

## Documentation References

Each example references the comprehensive documentation in this repo:

- [Claude Code Documentation](/docs/claude-code/) - Using Claude Code
- [LangChain Documentation](/docs/ai-frameworks/langchain/) - RAG framework
- [CrewAI Documentation](/docs/ai-frameworks/crewai/) - Multi-agent framework
- [Anthropic Claude API](/docs/ai-platforms/anthropic/) - API reference
- [Next.js Documentation](/docs/web-frameworks/nextjs/) - Web framework
- [Pinecone Documentation](/docs/infrastructure/pinecone/) - Vector database

## Advanced Topics

- [RAG with Metadata Filtering](./rag-app/README.md#metadata-filtering)
- [Custom Agents in CrewAI](./multi-agent/README.md#custom-agents)
- [Database Integration for Chat](./chat-interface/README.md#persistence)
- [Batch Processing at Scale](./claude-code-automation/README.md#performance)

## Contributing

When creating examples:
1. Follow the structure of existing examples
2. Include comprehensive README
3. Add `.env.example` template
4. Provide working code (not pseudocode)
5. Include error handling
6. Add usage examples
7. Reference documentation

## Resources

### Official Documentation
- [Anthropic Claude](https://docs.anthropic.com/)
- [LangChain](https://python.langchain.com/)
- [CrewAI](https://docs.crewai.com/)
- [Next.js](https://nextjs.org/docs)
- [Pinecone](https://docs.pinecone.io/)

### Tutorials & Guides
- [Claude Code Official](https://code.claude.com/)
- [llms.txt Standard](https://llmstxt.org/)
- [Building AI Apps](https://docs.anthropic.com/guides/)

## License

These examples are provided as learning resources. See individual example directories for specific licensing information.

## Support

For issues or questions:
1. Check the example's README
2. Review the documentation links
3. Check the example's error logs
4. Consult the main docs/ directory

---

**Start with an example that matches your use case!**

- 🔍 Need to ask questions about documents? → [RAG Application](./rag-app/)
- 🤖 Need multiple specialized AI agents? → [Multi-Agent System](./multi-agent/)
- 💬 Need a web chat interface? → [Chat Interface](./chat-interface/)
- ⚙️ Need to automate development tasks? → [Claude Code Automation](./claude-code-automation/)
