---
title: "Crewai: Security Considerations"
description: "Security Considerations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Security Considerations


By default, the `CodeInterpreterTool` runs code in an isolated Docker container, which provides a layer of security. However, there are still some security considerations to keep in mind:

1. The Docker container has access to the current working directory, so sensitive files could potentially be accessed.
2. If the Docker container is unavailable and the code needs to run safely, it will be executed in a sandbox environment. For security reasons, installing arbitrary libraries is not allowed
3. The `unsafe_mode` parameter allows code to be executed directly on the host machine, which should only be used in trusted environments.
4. Be cautious when allowing agents to install arbitrary libraries, as they could potentially include malicious code.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Implementation Details](./659-implementation-details.md)

**Next:** [Conclusion →](./661-conclusion.md)
