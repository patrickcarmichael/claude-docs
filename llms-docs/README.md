# LLM-Friendly Documentation Collection

This directory contains `llms-full.txt` files from various developer platforms and AI services. These files follow the [llms.txt standard](https://llmstxt.org/) - a proposal to standardize how websites provide documentation in an LLM-friendly format.

## What is llms-full.txt?

The `llms-full.txt` file combines a website's entire documentation into a single file optimized for AI tools and language models. Unlike `llms.txt` (which is an index of links), `llms-full.txt` provides comprehensive content directly, making it ideal for:

- AI coding assistants (Claude Code, Cursor, Windsurf)
- Context-aware code suggestions
- Training and fine-tuning language models
- Offline documentation access

## Collection Stats

**Total Files**: 21 comprehensive documentation sources
**Total Size**: ~51MB of developer documentation
**Last Updated**: 2025-11-08

## Files in This Collection

### AI Platforms & LLM Services
| Platform | File | Size | Description |
|----------|------|------|-------------|
| **Anthropic** | `anthropic-llms-full.txt` | 4.3M | Claude API, SDKs, and best practices |
| **Cohere** | `cohere-llms-full.txt` | 2.7M | Cohere LLM API documentation |
| **Fireworks** | `fireworks-llms-full.txt` | 991K | Fireworks AI platform docs |
| **OpenRouter** | `openrouter-llms-full.txt` | 839K | Multi-model LLM routing |
| **Together.ai** | `together-llms-full.txt` | 1.3M | Together AI inference platform |

### AI Development Tools
| Platform | File | Size | Description |
|----------|------|------|-------------|
| **Cursor** | `cursor-llms-full.txt` | 11M | AI-first code editor documentation |
| **Windsurf** | `windsurf-llms-full.txt` | 695K | AI coding assistant docs |
| **Codeium** | `codeium-llms-full.txt` | 695K | AI code completion platform |
| **CrewAI** | `crewai-llms-full.txt` | 1.9M | Multi-agent AI framework |

### Developer Frameworks & Tools
| Platform | File | Size | Description |
|----------|------|------|-------------|
| **Next.js** | `nextjs-llms-full.txt` | 2.9M | React framework documentation |
| **Astro** | `astro-llms-full.txt` | 2.5M | Modern web framework |
| **Vercel** | `vercel-llms-full.txt` | 7.9M | Deployment platform (largest file) |
| **LangChain** | `langchain-llms-full.txt` | 346K | Python LLM framework |
| **LangGraph** | `langgraph-llms-full.txt` | 618K | Agent workflow framework |

### AI/ML Infrastructure
| Platform | File | Size | Description |
|----------|------|------|-------------|
| **Pinecone** | `pinecone-llms-full.txt` | 2.8M | Vector database documentation |
| **ElevenLabs** | `elevenlabs-llms-full.txt` | 5.5M | Voice AI platform |

### Developer Tools & Platforms
| Platform | File | Size | Description |
|----------|------|------|-------------|
| **Claude Code** | `claude-code-llms-full.txt` | 532K | Claude CLI documentation |
| **MCP** | `mcp-llms-full.txt` | 852K | Model Context Protocol spec |
| **Cloudflare** | `cloudflare-llms-full.txt` | 24K | Cloudflare developer docs |
| **Mintlify** | `mintlify-llms-full.txt` | 781K | Documentation platform |
| **GitBook** | `gitbook-llms-full.txt` | 422K | Documentation platform |

## Usage

### For AI Coding Assistants

These files can be provided as context to AI assistants:

```bash
# Example: Use with Claude Code
claude -p "Using the Next.js docs, help me create a new API route"

# Example: Feed to Cursor
# Copy content from nextjs-llms-full.txt into Cursor's context
```

### For Development Reference

```bash
# Quick search across all docs
grep -r "authentication" llms-docs/

# Search specific platform
grep "API key" anthropic-llms-full.txt
```

### For Research & Analysis

These files are excellent for:
- Comparing API designs across platforms
- Analyzing documentation patterns
- Training custom models on technical content
- Building documentation search tools

## How These Were Collected

1. Research identified the llms.txt standard (proposed September 2024)
2. Web search found major platforms implementing the standard
3. Automated fetching from public `/llms-full.txt` endpoints
4. Validation and organization into this collection

## The llms.txt Standard

The standard defines two files:
- **`llms.txt`**: Index with links and descriptions (requires following links)
- **`llms-full.txt`**: Complete content in single file (this collection)

Learn more: https://llmstxt.org/

## Contributing

Found a platform with llms-full.txt that should be added? Common patterns:
- `https://docs.example.com/llms-full.txt`
- `https://example.com/docs/llms-full.txt`
- `https://platform.example.com/llms-full.txt`

## Related Resources

- **llms-txt-hub**: https://github.com/thedaviddias/llms-txt-hub (comprehensive directory)
- **Official spec**: https://llmstxt.org/
- **Claude Code docs**: https://code.claude.com/docs/

---

*Collection curated for AI-assisted development and comprehensive technical reference.*
