# AI Development Documentation Hub

[![Documentation](https://img.shields.io/badge/Docs-67_files-blue)](./docs/) [![Size](https://img.shields.io/badge/Size-~52MB-green)]() [![Platforms](https://img.shields.io/badge/Platforms-21-orange)]()

> **Comprehensive AI development documentation collection** - Optimized for both human developers and AI coding assistants. All documentation follows the [llms.txt standard](https://llmstxt.org/) for maximum AI compatibility.

---

## 📁 Documentation Structure

### 🤖 **[Claude Code](./docs/claude-code/)** - AI Coding Assistant
Complete documentation for Anthropic's Claude Code CLI tool.

**Quick Links:**
- [Getting Started](./docs/claude-code/getting-started/) - Installation, quickstart, workflows
- [Features](./docs/claude-code/features/) - Sub-agents, plugins, skills, hooks, MCP
- [Configuration](./docs/claude-code/configuration/) - Settings, IDE integration
- [Full LLMs.txt](./docs/claude-code/llms-full.txt) (532KB)

**Contents:** 44 markdown files organized by topic + full documentation file

---

### 🧠 **[AI Platforms](./docs/ai-platforms/)** - LLM API Providers
Documentation for major LLM API platforms.

| Platform | Size | Description |
|----------|------|-------------|
| [Anthropic](./docs/ai-platforms/anthropic/) | 4.3M | Claude API & SDKs |
| [Cohere](./docs/ai-platforms/cohere/) | 2.7M | Enterprise LLM platform |
| [Fireworks](./docs/ai-platforms/fireworks/) | 991K | Fast LLM inference |
| [OpenRouter](./docs/ai-platforms/openrouter/) | 839K | Multi-model routing |
| [Together.ai](./docs/ai-platforms/together-ai/) | 1.3M | Open-source LLM platform |

**Total:** 5 platforms, ~10.1MB

---

### 💻 **[AI Coding Tools](./docs/ai-coding-tools/)** - Development Assistants
AI-powered code editors and assistants.

| Tool | Size | Type |
|------|------|------|
| [Cursor](./docs/ai-coding-tools/cursor/) | 11M | AI-first code editor |
| [Codeium](./docs/ai-coding-tools/codeium/) | 695K | Code completion |
| [Windsurf](./docs/ai-coding-tools/windsurf/) | 695K | AI coding assistant |

**Total:** 3 tools, ~12.4MB

---

### 🔧 **[AI Frameworks](./docs/ai-frameworks/)** - Build AI Apps
Frameworks and protocols for LLM applications.

| Framework | Size | Purpose |
|-----------|------|---------|
| [LangChain](./docs/ai-frameworks/langchain/) | 346K | LLM application framework |
| [LangGraph](./docs/ai-frameworks/langgraph/) | 618K | Agent workflows |
| [CrewAI](./docs/ai-frameworks/crewai/) | 1.9M | Multi-agent orchestration |
| [MCP](./docs/ai-frameworks/mcp/) | 852K | Model Context Protocol |

**Total:** 4 frameworks, ~3.7MB

---

### 🌐 **[Web Frameworks](./docs/web-frameworks/)** - Build Interfaces
Modern web frameworks for AI applications.

| Framework | Size | Focus |
|-----------|------|-------|
| [Next.js](./docs/web-frameworks/nextjs/) | 2.9M | React framework |
| [Astro](./docs/web-frameworks/astro/) | 2.5M | Content-focused |
| [Vercel](./docs/web-frameworks/vercel/) | 7.9M | Deployment platform |

**Total:** 3 frameworks, ~13.3MB

---

### 🏗️ **[Infrastructure](./docs/infrastructure/)** - Services & Tools
Developer tools, databases, and platform services.

| Service | Size | Category |
|---------|------|----------|
| [Pinecone](./docs/infrastructure/pinecone/) | 2.8M | Vector database |
| [ElevenLabs](./docs/infrastructure/elevenlabs/) | 5.5M | Voice AI |
| [Cloudflare](./docs/infrastructure/cloudflare/) | 24K | Edge computing |
| [Mintlify](./docs/infrastructure/mintlify/) | 781K | Documentation platform |
| [GitBook](./docs/infrastructure/gitbook/) | 422K | Documentation platform |

**Total:** 5 services, ~9.5MB

---

## 🚀 Quick Start

### For Developers

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/claude-docs.git
cd claude-docs

# Browse documentation
cd docs/

# Search across all docs
grep -r "API authentication" docs/

# View specific platform
cat docs/ai-platforms/anthropic/llms-full.txt
```

### For AI Assistants

```bash
# Feed documentation to Claude Code
cat docs/claude-code/llms-full.txt | claude -p "help me set up MCP"

# Provide multiple contexts
cat docs/ai-platforms/anthropic/llms-full.txt \
    docs/ai-frameworks/langchain/llms-full.txt | your-ai-tool
```

### For RAG Applications

All `llms-full.txt` files are optimized for:
- Vector database ingestion
- RAG (Retrieval Augmented Generation)
- AI training data
- Semantic search

---

## 📊 Collection Stats

- **Total Files**: 67 documentation files
- **Total Size**: ~52MB of AI-optimized documentation
- **Platforms**: 21 major AI/dev platforms
- **Categories**: 6 organized categories
- **Format**: Markdown + llms-full.txt (plain text)

---

## 🎯 Use Cases

### Building AI Applications

**Stack Example:**
1. **LLM**: [Anthropic Claude](./docs/ai-platforms/anthropic/)
2. **Framework**: [LangChain](./docs/ai-frameworks/langchain/)
3. **Vector DB**: [Pinecone](./docs/infrastructure/pinecone/)
4. **Web**: [Next.js](./docs/web-frameworks/nextjs/)
5. **Deploy**: [Vercel](./docs/web-frameworks/vercel/)

### AI-Assisted Development

**Workflow:**
1. Use [Claude Code](./docs/claude-code/) for coding
2. Reference [platform docs](./docs/ai-platforms/) for APIs
3. Integrate with [frameworks](./docs/ai-frameworks/)
4. Deploy on [infrastructure](./docs/infrastructure/)

### Multi-Agent Systems

**Resources:**
- [Claude Code Sub-Agents](./docs/claude-code/features/sub-agents.md)
- [CrewAI](./docs/ai-frameworks/crewai/)
- [LangGraph](./docs/ai-frameworks/langgraph/)

---

## 📚 Documentation Format

### About llms-full.txt

Files ending in `llms-full.txt` follow the **[llms.txt standard](https://llmstxt.org/)** - a format designed specifically for AI consumption:

- **Single file**: Complete docs in one place
- **Plain text**: No HTML/JavaScript parsing needed
- **Structured**: Markdown formatting preserved
- **Optimized**: For LLM context windows

### Directory Structure

```
docs/
├── claude-code/              # Organized by topic
│   ├── getting-started/
│   ├── features/
│   ├── configuration/
│   ├── deployment/
│   ├── administration/
│   ├── reference/
│   ├── guides/
│   ├── llms-full.txt
│   └── README.md
│
├── ai-platforms/             # One dir per platform
│   ├── anthropic/
│   │   └── llms-full.txt
│   ├── cohere/
│   └── ...
│
├── ai-coding-tools/
├── ai-frameworks/
├── web-frameworks/
├── infrastructure/
└── README.md                 # This file
```

---

## 🔗 Cross-References

Documentation is extensively cross-linked:

- **Claude Code** ↔ **MCP Framework**: [Integration Guide](./docs/claude-code/features/mcp.md)
- **LangChain** ↔ **Pinecone**: RAG applications
- **Next.js** ↔ **Vercel**: Deployment
- **AI Platforms** ↔ **Frameworks**: API integration

Each category README includes relevant cross-references to related docs.

---

## 🛠️ Using This Collection

### Search Examples

```bash
# Find authentication docs across all platforms
grep -r "authentication" docs/ai-platforms/

# Search for MCP references
grep -r "Model Context Protocol" docs/

# Find specific API patterns
grep -r "streaming" docs/ai-platforms/anthropic/
```

### Integration Examples

```bash
# Build a RAG app reference
cat docs/ai-frameworks/langchain/llms-full.txt \
    docs/infrastructure/pinecone/llms-full.txt \
    docs/ai-platforms/anthropic/llms-full.txt

# Web development stack
cat docs/web-frameworks/nextjs/llms-full.txt \
    docs/web-frameworks/vercel/llms-full.txt
```

---

## 🤝 Related Resources

### Official Documentation Sites
- **Claude Code**: https://code.claude.com/docs/
- **llms.txt Standard**: https://llmstxt.org/
- **llms-txt Hub**: https://github.com/thedaviddias/llms-txt-hub

### Additional Tools
- **Claude Code GitHub**: https://github.com/anthropics/claude-code
- **Anthropic API**: https://docs.anthropic.com/
- **Model Context Protocol**: https://modelcontextprotocol.io/

---

## 📖 Navigation

**Main Documentation**: [docs/README.md](./docs/README.md)

**By Category:**
- [Claude Code](./docs/claude-code/README.md)
- [AI Platforms](./docs/ai-platforms/README.md)
- [AI Coding Tools](./docs/ai-coding-tools/README.md)
- [AI Frameworks](./docs/ai-frameworks/README.md)
- [Web Frameworks](./docs/web-frameworks/README.md)
- [Infrastructure](./docs/infrastructure/README.md)

---

## 📝 About This Repository

This repository contains a curated, organized collection of AI development documentation:

1. **Fetched** from official sources following the llms.txt standard
2. **Organized** into logical categories for easy navigation
3. **Cross-linked** for discovering related resources
4. **Optimized** for both human reading and AI consumption

**Created**: 2025-11-08
**Last Updated**: 2025-11-08
**Total Documentation**: 67 files (~52MB)

---

## 🎯 Quick Links

| What you need | Where to find it |
|---------------|------------------|
| Get started with Claude Code | [Quickstart](./docs/claude-code/getting-started/quickstart.md) |
| Choose an LLM API | [AI Platforms](./docs/ai-platforms/) |
| Build AI applications | [AI Frameworks](./docs/ai-frameworks/) |
| AI coding assistance | [AI Coding Tools](./docs/ai-coding-tools/) |
| Deploy your app | [Web Frameworks](./docs/web-frameworks/) |
| Vector database for RAG | [Pinecone](./docs/infrastructure/pinecone/) |

---

*Comprehensive AI development documentation - optimized for developers and AI assistants.*
