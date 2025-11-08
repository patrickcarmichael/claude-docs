---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Set the default model

DEFAULT_MODEL="claude-3-5-haiku-20241022"

def classify_support_request(request, actual_intent):
    # Define the prompt for the classification task

    classification_prompt = f"""You will be acting as a customer support ticket classification system. 
        ...
        ...The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """

    message = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": classification_prompt}],
    )
    usage = message.usage  # Get the usage statistics for the API call for how many input and output tokens were used.

    reasoning_and_intent = message.content[0].text

    # Use Python's regular expressions library to extract `reasoning`.

    reasoning_match = re.search(
        r"<reasoning>(.*?)</reasoning>", reasoning_and_intent, re.DOTALL
    )
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""

    # Similarly, also extract the `intent`.

    intent_match = re.search(r"<intent>(.*?)</intent>", reasoning_and_intent, re.DOTALL)
    intent = intent_match.group(1).strip() if intent_match else ""

      # Check if the model's prediction is correct.

    correct = actual_intent.strip() == intent.strip()

    # Return the reasoning, intent, correct, and usage.

    return reasoning, intent, correct, usage
```javascript
Let’s break down the edits we’ve made:

* We added the `actual_intent` from our test cases into the `classify_support_request` method and set up a comparison to assess whether Claude’s intent classification matches our golden intent classification.
* We extracted usage statistics for the API call to calculate cost based on input and output tokens used

### Run your evaluation

A proper evaluation requires clear thresholds and benchmarks to determine what is a good result. The script above will give us the runtime values for accuracy, response time, and cost per classification, but we still would need clearly established thresholds. For example:

* **Accuracy:** 95% (out of 100 tests)
* **Cost per classification:** 50% reduction on average (across 100 tests) from current routing method

Having these thresholds allows you to quickly and easily tell at scale, and with impartial empiricism, what method is best for you and what changes might need to be made to better fit your requirements.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
