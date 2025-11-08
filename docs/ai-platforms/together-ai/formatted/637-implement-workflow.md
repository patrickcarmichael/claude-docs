---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implement Workflow

```python
  from typing import List


  def serial_chain_workflow(
      input_query: str,
      prompt_chain: List[str],
  ) -> List[str]:
      """Run a serial chain of LLM calls to address the `input_query`
      using a list of prompts specified in `prompt_chain`.
      """
      response_chain = []
      response = input_query
      for i, prompt in enumerate(prompt_chain):
          print(f"Step {i+1}")
          response = run_llm(
              f"{prompt}\nInput:\n{response}",
              model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
          )
          response_chain.append(response)
          print(f"{response}\n")
      return response_chain
```
```typescript
  /*
    Run a serial chain of LLM calls to address the `inputQuery`
    using a list of prompts specified in `promptChain`.
  */
  async function serialChainWorkflow(inputQuery: string, promptChain: string[]) {
    const responseChain: string[] = [];
    let response = inputQuery;

    for (const prompt of promptChain) {
      console.log(`Step ${promptChain.indexOf(prompt) + 1}`);

      response = await runLLM(
        `${prompt}\nInput:\n${response}`,
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
      );
      console.log(`${response}\n`);
      responseChain.push(response);
    }

    return responseChain;
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
