---
title: "Crewai: Print the complete system prompt that will be sent to the LLM"
description: "Print the complete system prompt that will be sent to the LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Print the complete system prompt that will be sent to the LLM

if "system" in generated_prompt:
    print("=== SYSTEM PROMPT ===")
    print(generated_prompt["system"])
    print("\n=== USER PROMPT ===")
    print(generated_prompt["user"])
else:
    print("=== COMPLETE PROMPT ===")
    print(generated_prompt["prompt"])

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Generate and inspect the actual prompt](./360-generate-and-inspect-the-actual-prompt.md)

**Next:** [You can also see how the task description gets formatted →](./362-you-can-also-see-how-the-task-description-gets-for.md)
