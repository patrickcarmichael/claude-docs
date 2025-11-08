---
title: "Crewai: psycopg2 was installed to run this example with PostgreSQL"
description: "psycopg2 was installed to run this example with PostgreSQL section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# psycopg2 was installed to run this example with PostgreSQL

nl2sql = NL2SQLTool(db_uri="postgresql://example@localhost:5432/test_db")

@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[nl2sql]
    )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./805-usage.md)

**Next:** [Example →](./807-example.md)
