---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chapter 5: Evaluating SFT Results

### Testing Format Learning Success

**The Critical Test**: Can our fine-tuned model use the target format WITHOUT being explicitly told to do so?
```python
sample_question = "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much does she make every day at the farmers' market?"

sft_llm_response = sft_llm.chat.completions.create(
    messages=[{"role": "user", "content": sample_question}]
)

sft_llm_response.choices[0].message.content
```

**Actual output:**
```
Okay, let's see. Janet's ducks lay 16 eggs each day. She eats 3 eggs every morning for breakfast. Then she bakes muffins and uses 4 eggs for that. The rest she sells at the market for $2 each. So, I need to calculate how much she makes daily from the sales.

First, I'll find out how many eggs she has after eating and baking. So, total eggs laid per day is 16. She eats 3, so 16 - 3 = 13 eggs left. Then she uses 4 eggs for muffins, so 13 - 4 = 9 eggs remaining.

Now, she sells these 9 eggs at $2 each. So, 9 eggs * $2 = $18. That should be her daily earnings from the market.

[WORK]
1. Total eggs laid per day: 16
2. Eggs eaten for breakfast: 3
3. Eggs used for muffins: 4
4. Eggs remaining after eating and baking: 16 - 3 - 4 = 9
5. Price per egg: $2
6. Total earnings from farmers' market: 9 * 2 = 18
[/WORK]

[RESULT]
18
[/RESULT]
```

**SUCCESS! SFT taught the model to automatically use the target format!**

This demonstrates how SFT can make structural patterns the model's default behavior.

If your format learning is incomplete, consider:

* More training examples (aim for 1000+)
* Higher learning rate (try 1e-4)
* More epochs (try 5-8)
* Verify training data format consistency

Now that we have consistent, structured responses, we can focus purely on improving the *quality* of the content within that structure. This is where Stage 2 (RFT) shines - optimizing for correctness while maintaining our learned formatting.

### Understanding SFT's Strengths and Limitations

Strengths demonstrated

* Consistent output formatting
* No system prompts needed
* Internalized behavior patterns

Limitations to address

* Accuracy may not improve dramatically
* Only mimics teacher, doesn't generalize
* No feedback loop for corrections

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
