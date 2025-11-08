---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Usage

```python
  reference_models = [
      "microsoft/WizardLM-2-8x22B",
      "Qwen/Qwen2.5-72B-Instruct-Turbo",
      "google/gemma-2-27b-it",
      "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  ]

  user_prompt = """Jenna and her mother picked some apples from their apple farm.
  Jenna picked half as many apples as her mom. If her mom got 20 apples, how many apples did they both pick?"""

  aggregator_model = "deepseek-ai/DeepSeek-V3"

  aggregator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query.
  Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information
  provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the
  given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured,
  coherent, and adheres to the highest standards of accuracy and reliability.

  Responses from models:"""


  async def main():
      answer, intermediate_reponses = await parallel_workflow(
          prompt=user_prompt,
          proposer_models=reference_models,
          aggregator_model=aggregator_model,
          aggregator_prompt=aggregator_system_prompt,
      )

      for i, response in enumerate(intermediate_reponses):
          print(f"Intermetidate Response {i+1}:\n\n{response}\n")

      print(f"Final Answer: {answer}\n")


  asyncio.run(main())
```
```typescript
  const referenceModels = [
    "microsoft/WizardLM-2-8x22B",
    "Qwen/Qwen2.5-72B-Instruct-Turbo",
    "google/gemma-2-27b-it",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
  ];

  const userPrompt = dedent`
    Jenna and her mother picked some apples from their apple farm.
    Jenna picked half as many apples as her mom.

    If her mom got 20 apples, how many apples did they both pick?
  `;

  const aggregatorModel = "deepseek-ai/DeepSeek-V3";

  const aggregatorSystemPrompt = dedent`
    You have been provided with a set of responses from various
    open-source models to the latest user query. Your task is to
    synthesize these responses into a single, high-quality response.
    It is crucial to critically evaluate the information provided in
    these responses, recognizing that some of it may be biased or incorrect.
    Your response should not simply replicate the given answers but
    should offer a refined, accurate, and comprehensive reply to the
    instruction. Ensure your response is well-structured, coherent, and
    adheres to the highest standards of accuracy and reliability.

    Responses from models:
  `;

  async function main() {
    const [answer, intermediateResponses] = await parallelWorkflow(
      userPrompt,
      referenceModels,
      aggregatorModel,
      aggregatorSystemPrompt,
    );
    for (const response of intermediateResponses) {
      console.log(
        `## Intermediate Response: ${intermediateResponses.indexOf(response) + 1}:\n`,

      );
      console.log(`${response}\n`);
    }
    console.log(`## Final Answer:`);

    console.log(`${answer}\n`);
  }

  main();
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
