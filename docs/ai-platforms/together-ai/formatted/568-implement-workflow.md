---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implement Workflow

```python
  import asyncio
  from typing import List


  async def parallel_workflow(
      prompt: str,
      proposer_models: List[str],
      aggregator_model: str,
      aggregator_prompt: str,
  ):
      """Run a parallel chain of LLM calls to address the `input_query`
      using a list of models specified in `models`.

      Returns output from final aggregator model.
      """

      # Gather intermediate responses from proposer models

      proposed_responses = await asyncio.gather(
          *[run_llm_parallel(prompt, model) for model in proposer_models]
      )

      # Aggregate responses using an aggregator model

      final_output = run_llm(
          user_prompt=prompt,
          model=aggregator_model,
          system_prompt=aggregator_prompt
          + "\n"
          + "\n".join(
              f"{i+1}. {str(element)}"
              for i, element in enumerate(proposed_responses)
          ),
      )

      return final_output, proposed_responses
```
```typescript
  import dedent from "dedent";

  /*
    Run a parallel chain of LLM calls to address the `inputQuery`
    using a list of models specified in `proposerModels`.

    Returns output from final aggregator model.
  */
  async function parallelWorkflow(
    inputQuery: string,
    proposerModels: string[],
    aggregatorModel: string,
    aggregatorSystemPrompt: string,
  ) {
    // Gather intermediate responses from proposer models
    const proposedResponses = await Promise.all(
      proposerModels.map((model) => runLLM(inputQuery, model)),
    );

    // Aggregate responses using an aggregator model
    const aggregatorSystemPromptWithResponses = dedent`
      ${aggregatorSystemPrompt}

      ${proposedResponses.map((response, i) => `${i + 1}. response`)}
    `;

    const finalOutput = await runLLM(
      inputQuery,
      aggregatorModel,
      aggregatorSystemPromptWithResponses,
    );

    return [finalOutput, proposedResponses];
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
