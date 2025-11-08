---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `MultiOnTool` is implemented as a subclass of `BaseTool` from CrewAI. It wraps the MultiOn client to provide web browsing capabilities:

```python Code theme={null}
class MultiOnTool(BaseTool):
    """Tool to wrap MultiOn Browse Capabilities."""

    name: str = "Multion Browse Tool"
    description: str = """Multion gives the ability for LLMs to control web browsers using natural language instructions.
            If the status is 'CONTINUE', reissue the same instruction to continue execution
        """
    
    # Implementation details...
    
    def _run(self, cmd: str, *args: Any, **kwargs: Any) -> str:
        """
        Run the Multion client with the given command.
        
        Args:
            cmd (str): The detailed and specific natural language instruction for web browsing
            *args (Any): Additional arguments to pass to the Multion client
            **kwargs (Any): Additional keyword arguments to pass to the Multion client
        """
        # Implementation details...
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./2328-run-the-task.md)

**Next:** [Conclusion →](./2330-conclusion.md)
