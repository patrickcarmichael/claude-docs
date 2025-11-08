---
title: "Crewai: Your OpenAI key"
description: "Your OpenAI key section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Your OpenAI key

os.environ["OPENAI_API_KEY"] = "sk-proj-..."
```

With the environment variables set, we can now initialize the Langfuse client. get\_client() initializes the Langfuse client using the credentials provided in the environment variables.

```python  theme={null}
from langfuse import get_client
 
langfuse = get_client()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com" # 🇺🇸 US region](./2188-osenvironlangfuse_host-httpsuscloudlangfusecom-us-.md)

**Next:** [Verify connection →](./2190-verify-connection.md)
