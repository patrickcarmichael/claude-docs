---
title: "Crewai: Access the raw response"
description: "Access the raw response section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Access the raw response

print(result.raw)
```

### Parameters and Return Values

| Parameter         | Type                               | Description                                                               |
| :---------------- | :--------------------------------- | :------------------------------------------------------------------------ |
| `messages`        | `Union[str, List[Dict[str, str]]]` | Either a string query or a list of message dictionaries with role/content |
| `response_format` | `Optional[Type[Any]]`              | Optional Pydantic model for structured output                             |

The method returns a `LiteAgentOutput` object with the following properties:

* `raw`: String containing the raw output text
* `pydantic`: Parsed Pydantic model (if a `response_format` was provided)
* `agent_role`: Role of the agent that produced the output
* `usage_metrics`: Token usage metrics for the execution

### Structured Output

You can get structured output by providing a Pydantic model as the `response_format`:

```python Code theme={null}
from pydantic import BaseModel
from typing import List

class ResearchFindings(BaseModel):
    main_points: List[str]
    key_technologies: List[str]
    future_predictions: str

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Use kickoff() to interact directly with the agent](./24-use-kickoff-to-interact-directly-with-the-agent.md)

**Next:** [Get structured output →](./26-get-structured-output.md)
