---
title: "Crewai: Notes"
description: "Notes section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Notes


* The tool automatically polls the status endpoint every second until completion or timeout
* Successful tasks return the result directly, while failed tasks return error information
* Bearer tokens should be kept secure and not hardcoded in production environments
* Consider using environment variables for sensitive configuration like bearer tokens
* Custom input schemas must be compatible with the target crew automation's expected parameters

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← API Endpoints](./2388-api-endpoints.md)

**Next:** [Overview →](./2390-overview.md)
