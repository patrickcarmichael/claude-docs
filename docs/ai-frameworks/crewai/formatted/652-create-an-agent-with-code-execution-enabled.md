---
title: "Crewai: Create an agent with code execution enabled"
description: "Create an agent with code execution enabled section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with code execution enabled

programmer_agent = Agent(
    role="Python Programmer",
    goal="Write and execute Python code to solve problems",
    backstory="An expert Python programmer who can write efficient code to solve complex problems.",
    allow_code_execution=True,  # This automatically adds the CodeInterpreterTool
    verbose=True,
)
```

### Enabling `unsafe_mode`

```python Code theme={null}
from crewai_tools import CodeInterpreterTool

code = """
import os
os.system("ls -la")
"""

CodeInterpreterTool(unsafe_mode=True).run(code=code)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run the crew](./651-create-and-run-the-crew.md)

**Next:** [Parameters →](./653-parameters.md)
