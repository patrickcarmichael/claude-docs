# AI Coding Tools

AI-powered development environments and code assistants that enhance developer productivity.

## Tools

### ⚡ [Cursor](./cursor/)
**AI-First Code Editor** | 11MB (Largest collection)

Fork of VS Code rebuilt from the ground up for AI-native development.

- **Features**: Chat with codebase, AI autocomplete, inline edits, composer
- **AI Integration**: GPT-4, Claude, custom models
- **Best For**: Full IDE replacement, heavy AI usage
- **Pricing**: Free tier + Pro subscription

📄 [Full Documentation](./cursor/llms-full.txt)

**Key Capabilities:**
- Multi-file editing with AI
- Codebase-aware chat
- Terminal integration
- Git workflow automation

---

### 🎯 [Codeium](./codeium/)
**AI Code Completion Platform** | 695KB

Fast, free AI code completion with enterprise options.

- **Features**: Autocomplete, chat, search, command
- **AI Integration**: Proprietary models, fast inference
- **Best For**: Code completion, free alternative to Copilot
- **Pricing**: Free for individuals, team/enterprise tiers

📄 [Full Documentation](./codeium/llms-full.txt)

**Key Capabilities:**
- Multi-language support (70+ languages)
- IDE plugins (VS Code, JetBrains, Vim, etc.)
- On-premise deployment options
- Context-aware suggestions

---

### 🌊 [Windsurf](./windsurf/)
**AI Coding Assistant** | 695KB

Modern AI coding assistant focused on workflow integration.

- **Features**: Code generation, refactoring, documentation
- **AI Integration**: Multiple LLM backends
- **Best For**: Developers wanting lightweight AI assistance
- **Pricing**: Subscription-based

📄 [Full Documentation](./windsurf/llms-full.txt)

---

## Comparison

| Tool | Type | Integration | Offline | Best For |
|------|------|-------------|---------|----------|
| **Cursor** | Full IDE | Deep, built-in | Limited | Heavy AI users |
| **Codeium** | Plugin | Plugin-based | No | Free alternative |
| **Windsurf** | Assistant | Standalone | Limited | Lightweight |
| **[Claude Code](../claude-code/)** | CLI | Terminal-native | Yes | Command-line workflow |

---

## Choose Your Tool

### Cursor - Full AI IDE
**When to use:**
- You want AI deeply integrated in your editor
- Multi-file AI edits are important
- You prefer VS Code-style interface
- Budget allows Pro subscription

**Getting started:**
1. Download Cursor
2. Configure AI models
3. Learn keyboard shortcuts
4. Try Composer for multi-file tasks

---

### Codeium - Free Completion
**When to use:**
- You want free AI autocomplete
- Your IDE is already optimized
- You need multi-IDE support
- Privacy/on-premise is important

**Getting started:**
1. Install Codeium plugin
2. Sign up for free account
3. Configure in your IDE
4. Use in your existing workflow

---

### Windsurf - Lightweight Assistant
**When to use:**
- You want minimal disruption
- Specific task assistance needed
- Exploring AI coding tools
- Don't need full IDE replacement

---

### Claude Code - CLI Power
**When to use:**
- Terminal-centric workflow
- Scripting and automation
- Headless/server environments
- Deep integration with shell

**See**: [Claude Code Documentation](../claude-code/)

---

## Integration with Other Tools

### AI Platforms
All tools can integrate with:
- [Anthropic](../ai-platforms/anthropic/) - Claude models
- [OpenRouter](../ai-platforms/openrouter/) - Multiple models
- Custom API endpoints

### Development Workflows
- **Version Control**: All support Git integration
- **CI/CD**: Use [Claude Code](../claude-code/) for automation
- **Frameworks**: Work with [Next.js](../web-frameworks/nextjs/), [Astro](../web-frameworks/astro/), etc.

---

## Common Patterns

### Multi-Tool Workflow

Many developers use multiple tools:

1. **Cursor** for main development
2. **Claude Code** for CLI tasks and automation
3. **Codeium** in secondary IDEs

### Team Adoption

**Phase 1: Exploration**
- Individual developers try different tools
- Evaluate fit with existing workflow

**Phase 2: Standardization**
- Choose primary tool for team
- Keep Claude Code for scripts/CI

**Phase 3: Optimization**
- Configure enterprise deployments
- Set up team guidelines
- Track productivity metrics

---

## Related Documentation

### Configuration & Setup
- [Claude Code Configuration](../claude-code/configuration/)
- [Model Configuration](../claude-code/configuration/model-config.md)

### AI Frameworks
- [LangChain](../ai-frameworks/langchain/) - For building AI features
- [MCP](../ai-frameworks/mcp/) - Context protocol integration

### Deployment
- [Claude Code Deployment](../claude-code/deployment/)
- [Enterprise Setup](../claude-code/administration/)

---

*Part of the [AI Development Documentation Hub](../)*
