---
title: "Crewai: Define flow state"
description: "Define flow state section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define flow state

class MarketResearchState(BaseModel):
    product: str = ""
    analysis: MarketAnalysis | None = None

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define a structured output format](./116-define-a-structured-output-format.md)

**Next:** [Create a flow class →](./118-create-a-flow-class.md)
