---
title: "Crewai: Typical Workflow"
description: "Typical Workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Typical Workflow


1. **Discovery**: Call `GET /inputs` to understand what your crew needs
2. **Execution**: Submit inputs via `POST /kickoff` to start processing
3. **Monitoring**: Poll `GET /status/{kickoff_id}` until completion
4. **Results**: Extract the final output from the completed response

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Base URL](./2402-base-url.md)

**Next:** [Error Handling →](./2404-error-handling.md)
