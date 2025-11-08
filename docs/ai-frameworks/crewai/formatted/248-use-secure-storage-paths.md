---
title: "Crewai: Use secure storage paths"
description: "Use secure storage paths section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Use secure storage paths

storage_path = os.getenv("CREWAI_STORAGE_DIR", "./storage")
os.makedirs(storage_path, mode=0o700, exist_ok=True)  # Restricted permissions

crew = Crew(
    memory=True,
    long_term_memory=LongTermMemory(
        storage=LTMSQLiteStorage(
            db_path=f"{storage_path}/memory.db"
        )
    )
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Store sensitive data in environment variables](./247-store-sensitive-data-in-environment-variables.md)

**Next:** [Troubleshooting →](./249-troubleshooting.md)
