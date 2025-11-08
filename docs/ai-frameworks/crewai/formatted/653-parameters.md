---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


The `CodeInterpreterTool` accepts the following parameters during initialization:

* **user\_dockerfile\_path**: Optional. Path to a custom Dockerfile to use for the code interpreter container.
* **user\_docker\_base\_url**: Optional. URL to the Docker daemon to use for running the container.
* **unsafe\_mode**: Optional. Whether to run code directly on the host machine instead of in a Docker container or sandbox. Default is `False`. Use with caution!
* **default\_image\_tag**: Optional. Default Docker image tag. Default is `code-interpreter:latest`

When using the tool with an agent, the agent will need to provide:

* **code**: Required. The Python 3 code to execute.
* **libraries\_used**: Optional. A list of libraries used in the code that need to be installed. Default is `[]`

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with code execution enabled](./652-create-an-agent-with-code-execution-enabled.md)

**Next:** [Agent Integration Example →](./654-agent-integration-example.md)
