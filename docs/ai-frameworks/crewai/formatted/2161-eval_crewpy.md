---
title: "Crewai: eval_crew.py"
description: "eval_crew.py section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# eval_crew.py

from braintrust import Eval
from autoevals import Levenshtein

def evaluate_crew_task(input_data):
    """Task function that wraps our crew for evaluation."""
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": input_data["topic"]})
    return str(result)

Eval(
    "AI Research Crew",  # Project name
    {
        "data": lambda: [
            {"topic": "artificial intelligence trends 2024"},
            {"topic": "machine learning breakthroughs"},
            {"topic": "AI ethics and governance"},
        ],
        "task": evaluate_crew_task,
        "scores": [Levenshtein],
    },
)
```

Setup your API key and run:

```bash  theme={null}
export BRAINTRUST_API_KEY="YOUR_API_KEY"
braintrust eval eval_crew.py
```

See the [Braintrust Eval SDK guide](https://www.braintrust.dev/docs/start/eval-sdk) for more details.

### Key Features of Braintrust Integration

* **Comprehensive Tracing**: Track all agent interactions, tool usage, and LLM calls
* **Performance Monitoring**: Monitor execution times, token usage, and success rates
* **Experiment Tracking**: Compare different crew configurations and models
* **Automated Evaluation**: Set up custom evaluation metrics for crew outputs
* **Error Tracking**: Monitor and debug failures across your crew executions
* **Cost Analysis**: Track token usage and associated costs

### Version Compatibility Information

* Python 3.8+
* CrewAI >= 0.86.0
* Braintrust >= 0.1.0
* OpenTelemetry SDK >= 1.31.0

### References

* [Braintrust Documentation](https://www.braintrust.dev/docs) - Overview of the Braintrust platform
* [Braintrust CrewAI Integration](https://www.braintrust.dev/docs/integrations/crew-ai) - Official CrewAI integration guide
* [Braintrust Eval SDK](https://www.braintrust.dev/docs/start/eval-sdk) - Run experiments via the SDK
* [CrewAI Documentation](https://docs.crewai.com/) - Overview of the CrewAI framework
* [OpenTelemetry Docs](https://opentelemetry.io/docs/) - OpenTelemetry guide
* [Braintrust GitHub](https://github.com/braintrustdata/braintrust) - Source code for Braintrust SDK

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run your crew](./2160-run-your-crew.md)

**Next:** [Datadog Integration →](./2162-datadog-integration.md)
