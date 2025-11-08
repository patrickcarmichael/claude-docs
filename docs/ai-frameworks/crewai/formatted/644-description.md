---
title: "Crewai: Description"
description: "Description section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Description


The `CodeInterpreterTool` enables CrewAI agents to execute Python 3 code that they generate autonomously. This functionality is particularly valuable as it allows agents to create code, execute it, obtain the results, and utilize that information to inform subsequent decisions and actions.

There are several ways to use this tool:

### Docker Container (Recommended)

This is the primary option. The code runs in a secure, isolated Docker container, ensuring safety regardless of its content.
Make sure Docker is installed and running on your system. If you don’t have it, you can install it from [here](https://docs.docker.com/get-docker/).

### Sandbox environment

If Docker is unavailable — either not installed or not accessible for any reason — the code will be executed in a restricted Python environment - called sandbox.
This environment is very limited, with strict restrictions on many modules and built-in functions.

### Unsafe Execution

**NOT RECOMMENDED FOR PRODUCTION**
This mode allows execution of any Python code, including dangerous calls to `sys, os..` and similar modules. [Check out](/en/tools/ai-ml/codeinterpretertool#enabling-unsafe-mode) how to enable this mode

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `CodeInterpreterTool`](./643-codeinterpretertool.md)

**Next:** [Logging →](./645-logging.md)
