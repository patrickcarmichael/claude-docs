---
title: "Crewai: Create a task that includes error handling instructions"
description: "Create a task that includes error handling instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a task that includes error handling instructions

robust_extract_task = Task(
    description="""
    Extract the main heading from example.com.
    Be aware that you might encounter errors such as:
    - Invalid URL format
    - Missing API key
    - Rate limit exceeded
    - Network or API errors
    
    If you encounter any errors, provide a clear explanation of what went wrong
    and suggest possible solutions.
    """,
    expected_output="Either the extracted heading or a clear error explanation",
    agent=web_scraper_agent,
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Error Handling](./1326-error-handling.md)

**Next:** [Rate Limiting →](./1328-rate-limiting.md)
