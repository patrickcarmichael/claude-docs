---
title: "Crewai: Initialize enhanced tracing"
description: "Initialize enhanced tracing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize enhanced tracing

Traceloop.init(
    api_endpoint="https://your-truefoundry-endpoint/api/tracing",
    headers={
        "Authorization": f"Bearer {your_truefoundry_pat_token}",
        "TFY-Tracing-Project": "your_project_name",
    },
)
```

This provides additional trace correlation across your entire CrewAI workflow.
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=90623834e0ba9f4ccb09890f6824912d" alt="TrueFoundry CrewAI Tracing" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/tracing_crewai.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d05099079060dfd1588ac0c8de28e07b 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=645362e069e687f7dc6fd6c44a97a4ef 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=aac6d42bbd2f457b59f6a4b22d6a7be1 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7f166e1329cef8da8c1e07a38dc75506 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6e91cffda555b8cc7ce1800ed1b508b1 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bf6296110bd62d9bb30ae2d0822d4b8d 2500w" />

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Tracing](./2289-tracing.md)

**Next:** [Weave Integration →](./2291-weave-integration.md)
