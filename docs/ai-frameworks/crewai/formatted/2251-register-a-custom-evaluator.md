---
title: "Crewai: Register a custom evaluator"
description: "Register a custom evaluator section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Register a custom evaluator

@client.register_local_evaluator("random_evaluator")
def random_evaluator(**kwargs):
    score = random.random()
    return EvaluationResult(
        score_raw=score,
        pass_=score >= 0.5,
        explanation="example explanation",
    )

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the Patronus client](./2250-initialize-the-patronus-client.md)

**Next:** [Initialize the tool with the custom evaluator →](./2252-initialize-the-tool-with-the-custom-evaluator.md)
