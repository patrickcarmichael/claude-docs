---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

Setup and connect DSPy to LLMs on Together AI
```python
  import dspy

  # Configure dspy with a LLM from Together AI

  lm = dspy.LM(
      "together_ai/togethercomputer/llama-2-70b-chat",
      api_key=os.environ.get("TOGETHER_API_KEY"),
      api_base="https://api.together.xyz/v1",
  )

  # Now you can call the LLM directly as follows

  lm("Say this is a test!", temperature=0.7)  # => ['This is a test!']

  lm(
      messages=[{"role": "user", "content": "Say this is a test!"}]
  )  # => ['This is a test!']

```

Now we can set up a DSPy module, like `dspy.ReAct` with a task-specific signature. For example, `question -> answer: float` tells the module to take a question and to produce a floating point number answer below.
```python
  # Configure dspy to use the LLM

  dspy.configure(lm=lm)


  # Gives the agent access to a python interpreter

  def evaluate_math(expression: str):
      return dspy.PythonInterpreter({}).execute(expression)


  # Gives the agent access to a wikipedia search tool

  def search_wikipedia(query: str):

      results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(
          query, k=3
      )
      return [x["text"] for x in results]


  # setup ReAct module with question and math answer signature

  react = dspy.ReAct(
      "question -> answer: float",
      tools=[evaluate_math, search_wikipedia],
  )

  pred = react(
      question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?"
  )

  print(pred.answer)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
