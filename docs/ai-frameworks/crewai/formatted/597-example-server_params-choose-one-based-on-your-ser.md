---
title: "Crewai: Example server_params (choose one based on your server type):"
description: "Example server_params (choose one based on your server type): section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example server_params (choose one based on your server type):

# 1. Stdio Server:
server_params=StdioServerParameters(
    command="python3",
    args=["servers/your_server.py"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example with custom connection timeout](./596-example-with-custom-connection-timeout.md)

**Next:** [2. SSE Server: →](./598-2-sse-server.md)
