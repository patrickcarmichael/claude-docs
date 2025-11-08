---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Grading evals

When deciding which method to use to grade evals, choose the fastest, most reliable, most scalable method:

1. **Code-based grading**: Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgements that require less rule-based rigidity.
   * Exact match: `output == golden_answer`
   * String match: `key_phrase in output`

2. **Human grading**: Most flexible and high quality, but slow and expensive. Avoid if possible.

3. **LLM-based grading**: Fast and flexible, scalable and suitable for complex judgement. Test to ensure reliability first then scale.

### Tips for LLM-based grading

* **Have detailed, clear rubrics**: "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'"
  >   **📝 Note**
>
> A given use case, or even a specific success criteria for that use case, might require several rubrics for holistic evaluation.
* **Empirical or specific**: For example, instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1-5. Purely qualitative evaluations are hard to assess quickly and at scale.
* **Encourage reasoning**: Ask the LLM to think first before deciding an evaluation score, and then discard the reasoning. This increases evaluation performance, particularly for tasks requiring complex judgement.

<Accordion title="Example: LLM-based grading">
```python
  import anthropic

  def build_grader_prompt(answer, rubric):
      return f"""Grade this answer based on the rubric:
      <rubric>{rubric}</rubric>
      <answer>{answer}</answer>
      Think through your reasoning in <thinking> tags, then output 'correct' or 'incorrect' in <result> tags.""

  def grade_completion(output, golden_answer):
      grader_response = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=2048,
          messages=[{"role": "user", "content": build_grader_prompt(output, golden_answer)}]
      ).content[0].text

      return "correct" if "correct" in grader_response.lower() else "incorrect"

  # Example usage

  eval_data = [
      {"question": "Is 42 the answer to life, the universe, and everything?", "golden_answer": "Yes, according to 'The Hitchhiker's Guide to the Galaxy'."},
      {"question": "What is the capital of France?", "golden_answer": "The capital of France is Paris."}
  ]

  def get_completion(prompt: str):
      message = client.messages.create(
          model="claude-sonnet-4-5",
          max_tokens=1024,
          messages=[
          {"role": "user", "content": prompt}
          ]
      )
      return message.content[0].text

  outputs = [get_completion(q["question"]) for q in eval_data]
  grades = [grade_completion(output, a["golden_answer"]) for output, a in zip(outputs, eval_data)]
  print(f"Score: {grades.count('correct') / len(grades) * 100}%")
```typescript
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
