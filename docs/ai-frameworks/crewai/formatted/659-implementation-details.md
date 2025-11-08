---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `CodeInterpreterTool` uses Docker to create a secure environment for code execution:

```python Code theme={null}
class CodeInterpreterTool(BaseTool):
    name: str = "Code Interpreter"
    description: str = "Interprets Python3 code strings with a final print statement."
    args_schema: Type[BaseModel] = CodeInterpreterSchema
    default_image_tag: str = "code-interpreter:latest"

    def _run(self, **kwargs) -> str:
        code = kwargs.get("code", self.code)
        libraries_used = kwargs.get("libraries_used", [])

        if self.unsafe_mode:
            return self.run_code_unsafe(code, libraries_used)
        else:
            return self.run_code_safety(code, libraries_used)
```

The tool performs the following steps:

1. Verifies that the Docker image exists or builds it if necessary
2. Creates a Docker container with the current working directory mounted
3. Installs any required libraries specified by the agent
4. Executes the Python code in the container
5. Returns the output of the code execution
6. Cleans up by stopping and removing the container

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./658-run-the-task.md)

**Next:** [Security Considerations →](./660-security-considerations.md)
