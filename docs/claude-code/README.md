# Claude Code Documentation

Complete documentation for Claude Code - Anthropic's official AI coding assistant CLI.

## 📚 Documentation Sections

### 🚀 [Getting Started](./getting-started/)
Perfect for new users and quick reference.

- **[Overview](./getting-started/overview.md)** - What is Claude Code and key capabilities
- **[Quickstart](./getting-started/quickstart.md)** - Get up and running in minutes
- **[Common Workflows](./getting-started/common-workflows.md)** - Typical development patterns
- **[Claude Code on the Web](./getting-started/claude-code-on-the-web.md)** - Browser-based usage

**Start here**: [Quickstart Guide](./getting-started/quickstart.md)

---

### ✨ [Features](./features/)
Core capabilities and extensibility options.

- **[Sub-Agents](./features/sub-agents.md)** - Specialized AI assistants for complex tasks
- **[Plugins](./features/plugins.md)** - Extend functionality with plugins
- **[Skills](./features/skills.md)** - Model-invoked modular capabilities
- **[Hooks](./features/hooks.md)** - Event-based automation reference
- **[Hooks Guide](./features/hooks-guide.md)** - Practical hook implementation
- **[MCP](./features/mcp.md)** - Model Context Protocol integration
- **[Output Styles](./features/output-styles.md)** - Customize output formatting

**Power users**: Combine [Sub-Agents](./features/sub-agents.md) + [MCP](./features/mcp.md) + [Hooks](./features/hooks.md)

**Related**: [MCP Framework Docs](../ai-frameworks/mcp/)

---

### ⚙️ [Configuration](./configuration/)
Customize Claude Code for your workflow.

- **[Settings](./configuration/settings.md)** - Comprehensive settings reference
- **[Model Config](./configuration/model-config.md)** - Configure AI models
- **[Memory](./configuration/memory.md)** - Context and memory management
- **[Status Line](./configuration/statusline.md)** - Configure status display
- **[Terminal Config](./configuration/terminal-config.md)** - Terminal integration
- **[VS Code](./configuration/vs-code.md)** - VS Code integration
- **[JetBrains](./configuration/jetbrains.md)** - IntelliJ/PyCharm integration

**First time setup**: [Settings](./configuration/settings.md) → [Model Config](./configuration/model-config.md)

---

### 🚢 [Deployment](./deployment/)
Deploy Claude Code in various environments.

- **[Amazon Bedrock](./deployment/amazon-bedrock.md)** - AWS Bedrock integration
- **[Google Vertex AI](./deployment/google-vertex-ai.md)** - GCP Vertex AI setup
- **[Dev Container](./deployment/devcontainer.md)** - Containerized development
- **[Sandboxing](./deployment/sandboxing.md)** - Security isolation
- **[Network Config](./deployment/network-config.md)** - Proxy and firewall setup
- **[LLM Gateway](./deployment/llm-gateway.md)** - Enterprise LLM routing
- **[Third-Party Integrations](./deployment/third-party-integrations.md)** - External services

**Cloud deployment**: [Bedrock](./deployment/amazon-bedrock.md) or [Vertex AI](./deployment/google-vertex-ai.md)

**Related**: [Anthropic API Docs](../ai-platforms/anthropic/)

---

### 🔐 [Administration](./administration/)
Manage security, costs, and compliance.

- **[Setup](./administration/setup.md)** - Initial admin setup
- **[IAM](./administration/iam.md)** - Identity and access management
- **[Security](./administration/security.md)** - Security best practices
- **[Data Usage](./administration/data-usage.md)** - Data handling and privacy
- **[Monitoring & Usage](./administration/monitoring-usage.md)** - Track usage metrics
- **[Costs](./administration/costs.md)** - Cost management
- **[Analytics](./administration/analytics.md)** - Usage analytics
- **[Plugin Marketplaces](./administration/plugin-marketplaces.md)** - Manage plugin sources

**Admin checklist**: [Setup](./administration/setup.md) → [IAM](./administration/iam.md) → [Security](./administration/security.md)

---

### 📖 [Reference](./reference/)
Technical specifications and API documentation.

- **[CLI Reference](./reference/cli-reference.md)** - Complete command-line interface
- **[Interactive Mode](./reference/interactive-mode.md)** - Interactive session commands
- **[Slash Commands](./reference/slash-commands.md)** - Built-in slash commands
- **[Checkpointing](./reference/checkpointing.md)** - Session state management
- **[Plugins Reference](./reference/plugins-reference.md)** - Plugin API documentation
- **[Headless Mode](./reference/headless.md)** - Non-interactive usage
- **[Legal & Compliance](./reference/legal-and-compliance.md)** - Terms and compliance

**Quick lookup**: [CLI Reference](./reference/cli-reference.md) | [Slash Commands](./reference/slash-commands.md)

---

### 📝 [Guides](./guides/)
Step-by-step tutorials and advanced patterns.

- **[GitHub Actions](./guides/github-actions.md)** - CI/CD with GitHub (if available)
- **[GitLab CI/CD](./guides/gitlab-ci-cd.md)** - GitLab integration (if available)
- **[Migration Guide](./guides/migration-guide.md)** - Upgrade and migration
- **[Troubleshooting](./guides/troubleshooting.md)** - Common issues and solutions

**CI/CD Setup**: [GitHub Actions](./guides/github-actions.md) or [GitLab CI/CD](./guides/gitlab-ci-cd.md)

---

## 📄 Complete Documentation

**[llms-full.txt](./llms-full.txt)** (532KB) - Complete documentation in LLM-optimized format

**Available Formats:**
- **[Formatted Version](./formatted/index.md)** - Beautifully formatted markdown with YAML front matter
- **[Chunked Version](./chunked/index.md)** - Split into 9 manageable sections
- **[Organized Docs](#-documentation-sections)** - Topic-based structure (above)

Perfect for:
- Feeding to AI coding assistants
- Context for Claude conversations
- Training custom models
- Offline reference

**Format Benefits:**
- **Formatted**: Clean markdown, YAML metadata, easy reading
- **Chunked**: 9 logical sections (~60KB each), AI-optimized
- **Organized**: Topic-based navigation, quick reference

---

## 🔗 Cross-References

### Related AI Tools
- **AI Coding Assistants**: [Cursor](../ai-coding-tools/cursor/), [Windsurf](../ai-coding-tools/windsurf/)
- **LLM API**: [Anthropic Platform](../ai-platforms/anthropic/)

### Integration Options
- **MCP Protocol**: [MCP Feature](./features/mcp.md) + [MCP Framework](../ai-frameworks/mcp/)
- **Agent Frameworks**: [LangChain](../ai-frameworks/langchain/), [CrewAI](../ai-frameworks/crewai/)

### Deployment Platforms
- **Web Framework**: [Next.js](../web-frameworks/nextjs/), [Vercel](../web-frameworks/vercel/)
- **Cloud**: [AWS Bedrock](./deployment/amazon-bedrock.md), [GCP Vertex](./deployment/google-vertex-ai.md)

---

## 🎯 Quick Workflows

### First-Time Setup
1. [Quickstart](./getting-started/quickstart.md) - Install and configure
2. [Settings](./configuration/settings.md) - Customize preferences
3. [Common Workflows](./getting-started/common-workflows.md) - Learn patterns

### Power User Setup
1. [Sub-Agents](./features/sub-agents.md) - Enable specialized agents
2. [MCP](./features/mcp.md) - Connect external data sources
3. [Hooks](./features/hooks-guide.md) - Automate workflows
4. [Plugins](./features/plugins.md) - Extend capabilities

### Team/Enterprise Deployment
1. [Admin Setup](./administration/setup.md) - Configure for team
2. [IAM](./administration/iam.md) - Set up access control
3. [Deployment](./deployment/) - Choose cloud provider
4. [Monitoring](./administration/monitoring-usage.md) - Track usage

---

## 📋 Additional Resources

- **[Documentation Map](./docs-map.md)** - Complete file listing
- **Official Site**: https://code.claude.com/
- **GitHub**: https://github.com/anthropics/claude-code

---

*Part of the [AI Development Documentation Hub](../)*
