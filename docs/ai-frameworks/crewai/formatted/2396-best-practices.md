---
title: "Crewai: **Best Practices**"
description: "**Best Practices** section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## **Best Practices**


* **Secure credentials**: Store API keys and bearer tokens in environment variables or a secrets manager
* **Plan for latency**: External automations may take longer—set appropriate polling intervals and timeouts
* **Reuse sessions**: Bedrock Agents support session IDs so you can maintain context across multiple tool calls
* **Validate responses**: Normalise remote output (JSON, text, status codes) before forwarding it to downstream tasks
* **Monitor usage**: Track audit logs in CrewAI Platform or AWS CloudWatch to stay ahead of quota limits and failures

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Managed agent on Bedrock](./2395-managed-agent-on-bedrock.md)

**Next:** [GET /inputs →](./2397-get-inputs.md)
