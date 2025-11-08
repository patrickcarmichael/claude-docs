# AI Development Documentation Hub

A comprehensive, organized collection of AI development documentation optimized for both human developers and AI coding assistants.

## 📁 Documentation Structure

### 🤖 [Claude Code](./claude-code/)
Complete documentation for Claude's AI coding assistant CLI tool.

- **[Getting Started](./claude-code/getting-started/)** - Overview, quickstart, workflows
- **[Features](./claude-code/features/)** - Sub-agents, plugins, skills, hooks, MCP
- **[Configuration](./claude-code/configuration/)** - Settings, IDEs, terminal config
- **[Deployment](./claude-code/deployment/)** - Cloud providers, sandboxing, networking
- **[Administration](./claude-code/administration/)** - Security, monitoring, costs
- **[Reference](./claude-code/reference/)** - CLI commands, APIs, technical specs
- **[Guides](./claude-code/guides/)** - CI/CD integration, migration, troubleshooting

📄 [Full Documentation (LLMs.txt)](./claude-code/llms-full.txt) - 532KB optimized for AI

---

### 🧠 [AI Platforms](./ai-platforms/)
LLM APIs and AI service platforms.

| Platform | Focus | Size |
|----------|-------|------|
| **[Anthropic](./ai-platforms/anthropic/)** | Claude API & SDKs | 4.3M |
| **[Cohere](./ai-platforms/cohere/)** | Enterprise LLM platform | 2.7M |
| **[Fireworks](./ai-platforms/fireworks/)** | Fast LLM inference | 991K |
| **[OpenRouter](./ai-platforms/openrouter/)** | Multi-model routing | 839K |
| **[Together.ai](./ai-platforms/together-ai/)** | Open-source LLMs | 1.3M |

---

### 💻 [AI Coding Tools](./ai-coding-tools/)
AI-powered development environments and code assistants.

| Tool | Type | Size |
|------|------|------|
| **[Cursor](./ai-coding-tools/cursor/)** | AI-first code editor | 11M |
| **[Codeium](./ai-coding-tools/codeium/)** | Code completion | 695K |
| **[Windsurf](./ai-coding-tools/windsurf/)** | AI coding assistant | 695K |

**Related**: See [Claude Code](./claude-code/) for CLI-based AI coding

---

### 🔧 [AI Frameworks](./ai-frameworks/)
Frameworks and protocols for building AI applications.

| Framework | Purpose | Size |
|-----------|---------|------|
| **[LangChain](./ai-frameworks/langchain/)** | LLM application framework | 346K |
| **[LangGraph](./ai-frameworks/langgraph/)** | Agent workflow framework | 618K |
| **[CrewAI](./ai-frameworks/crewai/)** | Multi-agent orchestration | 1.9M |
| **[MCP](./ai-frameworks/mcp/)** | Model Context Protocol | 852K |

**Related**: [Claude Code MCP Integration](./claude-code/features/mcp.md)

---

### 🌐 [Web Frameworks](./web-frameworks/)
Modern web frameworks with AI/LLM integration.

| Framework | Type | Size |
|-----------|------|------|
| **[Next.js](./web-frameworks/nextjs/)** | React framework | 2.9M |
| **[Astro](./web-frameworks/astro/)** | Content-focused framework | 2.5M |
| **[Streamlit](./web-frameworks/streamlit/)** | Python data app framework | 1.4M |
| **[Vercel](./web-frameworks/vercel/)** | Deployment platform | 7.9M |

---

### 🏗️ [Infrastructure](./infrastructure/)
Developer tools, databases, and platform services.

| Service | Category | Size |
|---------|----------|------|
| **[Supabase](./infrastructure/supabase/)** | Backend/Database | 4.0M |
| **[Pinecone](./infrastructure/pinecone/)** | Vector database | 2.8M |
| **[ElevenLabs](./infrastructure/elevenlabs/)** | Voice AI | 5.5M |
| **[Cloudflare](./infrastructure/cloudflare/)** | Edge computing | 24K |
| **[Mintlify](./infrastructure/mintlify/)** | Documentation platform | 781K |
| **[GitBook](./infrastructure/gitbook/)** | Documentation platform | 422K |

---

## 🎯 Quick Navigation

### By Use Case

**Building AI Applications:**
1. Choose your LLM: [AI Platforms](./ai-platforms/)
2. Pick a framework: [AI Frameworks](./ai-frameworks/)
3. Add tools: [Claude Code](./claude-code/) or [AI Coding Tools](./ai-coding-tools/)

**Setting Up Claude Code:**
1. [Quickstart](./claude-code/getting-started/quickstart.md)
2. [Configuration](./claude-code/configuration/settings.md)
3. [Common Workflows](./claude-code/getting-started/common-workflows.md)

**Working with Agents:**
- [Claude Code Sub-Agents](./claude-code/features/sub-agents.md)
- [CrewAI Multi-Agent](./ai-frameworks/crewai/)
- [LangGraph Workflows](./ai-frameworks/langgraph/)

**Integration & Deployment:**
- [MCP Protocol](./ai-frameworks/mcp/) + [Claude Code MCP](./claude-code/features/mcp.md)
- [GitHub Actions](./claude-code/guides/github-actions.md)
- [Cloud Deployment](./claude-code/deployment/)

---

## 📊 Collection Stats

- **Total Documentation**: 69 files (2 new platforms added)
- **Total Size**: ~60MB (increased from 52MB)
- **Platforms Covered**: 23 (added Streamlit, Supabase)
- **Categories**: 6

---

## 🔍 About This Collection

### What is llms-full.txt?

Files ending in `llms-full.txt` follow the [llms.txt standard](https://llmstxt.org/) - a format specifically designed for AI consumption. These files contain complete documentation in a single, LLM-optimized format.

### File Organization

```
docs/
├── claude-code/          # Organized by topic (getting-started, features, etc.)
├── ai-platforms/         # One directory per platform
├── ai-coding-tools/      # AI development environments
├── ai-frameworks/        # LLM application frameworks
├── web-frameworks/       # Web development frameworks
└── infrastructure/       # Supporting services and tools
```

### Cross-References

Documentation is interlinked where relevant:
- Claude Code integrates with MCP → See [MCP Framework](./ai-frameworks/mcp/)
- Using Claude with Anthropic API → See [Anthropic Platform](./ai-platforms/anthropic/)
- Deploying on Vercel → See [Vercel Docs](./web-frameworks/vercel/)

---

## 🚀 Using This Documentation

### For AI Assistants

```bash
# Feed entire platform docs to AI
cat docs/ai-platforms/anthropic/llms-full.txt | your-ai-tool

# Provide Claude Code context
cat docs/claude-code/llms-full.txt | claude -p "help me configure MCP"
```

### For Development

```bash
# Search across all docs
grep -r "authentication" docs/

# Find specific platform info
cat docs/ai-platforms/openrouter/llms-full.txt | grep "API key"
```

### For Research

All documentation is in plain text/markdown, perfect for:
- Training custom models
- Building documentation search
- Comparative analysis
- RAG applications

---

## 📚 External Resources

- **Claude Code**: https://code.claude.com/docs/
- **llms.txt Standard**: https://llmstxt.org/
- **llms-txt Hub**: https://github.com/thedaviddias/llms-txt-hub

---

*Last Updated: 2025-11-08*
