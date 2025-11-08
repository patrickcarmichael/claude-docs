---
title: "Crewai: Optimizing for Specific Models"
description: "Optimizing for Specific Models section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Optimizing for Specific Models


Different models thrive on differently structured prompts. Making deeper adjustments can significantly boost performance by aligning your prompts with a model's nuances.

### Example: Llama 3.3 Prompting Template

For instance, when dealing with Meta's Llama 3.3, deeper-level customization may reflect the recommended structure described at:
[https://www.llama.com/docs/model-cards-and-prompt-formats/llama3\_1/#prompt-template](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/#prompt-template)

Here's an example to highlight how you might fine-tune an Agent to leverage Llama 3.3 in code:

```python  theme={null}
from crewai import Agent, Crew, Task, Process
from crewai_tools import DirectoryReadTool, FileReadTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the crew](./368-run-the-crew.md)

**Next:** [Define templates for system, user (prompt), and assistant (response) messages →](./370-define-templates-for-system-user-prompt-and-assist.md)
