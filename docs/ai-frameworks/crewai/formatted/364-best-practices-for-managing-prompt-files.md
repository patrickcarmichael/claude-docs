---
title: "Crewai: Best Practices for Managing Prompt Files"
description: "Best Practices for Managing Prompt Files section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Best Practices for Managing Prompt Files


When engaging in low-level prompt customization, follow these guidelines to keep things organized and maintainable:

1. **Keep files separate** – Store your customized prompts in dedicated JSON files outside your main codebase.
2. **Version control** – Track changes within your repository, ensuring clear documentation of prompt adjustments over time.
3. **Organize by model or language** – Use naming schemes like `prompts_llama.json` or `prompts_es.json` to quickly identify specialized configurations.
4. **Document changes** – Provide comments or maintain a README detailing the purpose and scope of your customizations.
5. **Minimize alterations** – Only override the specific slices you genuinely need to adjust, keeping default functionality intact for everything else.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define your own system template without default instructions](./363-define-your-own-system-template-without-default-in.md)

**Next:** [The Simplest Way to Customize Prompts →](./365-the-simplest-way-to-customize-prompts.md)
