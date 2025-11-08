---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## LLM as a judge

Create reward functions with LLM as a judge
```python
from openai import OpenAI 
import os

@reward_function
def evaluate(messages: list[dict], criteria: str = None, **kwargs) -> dict:
    """
    Evaluate the last message in the conversation using GPT-4 as a judge.
    
    Args:
        messages: List of message dicts. The last message is assumed to be the result to evaluate.
        criteria: Optional custom evaluation criteria. If not provided, uses default criteria.
        **kwargs: Additional arguments to pass to the OpenAI API.
    
    Returns:
        dict with 'score' (1-10), 'reasoning', and 'raw_response'
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Extract the conversation history and the result to evaluate

    conversation_history = messages[:-1]
    result_to_evaluate = messages[-1]
    
    # Default evaluation criteria

    if criteria is None:
        criteria = """
Please evaluate the quality of the assistant's response based on:
1. Accuracy: Is the information correct?
2. Helpfulness: Does it address the user's question?
3. Clarity: Is it well-explained and easy to understand?
4. Completeness: Does it cover all necessary aspects?

Provide a score from 1-10 (10 being best) and explain your reasoning.
"""
    
    # Build the judge prompt

    judge_messages = [
        {
            "role": "system",
            "content": "You are an expert evaluator. Your job is to objectively assess the quality of AI assistant responses."
        },
        {
            "role": "user",
            "content": f"""Here is a conversation and a response to evaluate:

CONVERSATION HISTORY:
{format_conversation(conversation_history)}

RESPONSE TO EVALUATE:
{result_to_evaluate['content']}

EVALUATION CRITERIA:
{criteria}

Please respond in the following format:
Score: [1-10]
Reasoning: [Your detailed explanation]
"""
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=judge_messages,
        temperature=kwargs.pop('temperature', 0.3),  # Lower temp for more consistent judging

        **kwargs,
    )
    
    # Parse the response

    judgment_text = response.choices[0].message.content
    score, reasoning = parse_judgment(judgment_text)
    
    return {
        "score": score,
        "reasoning": reasoning,
        "raw_response": judgment_text,
        "usage": response.usage.model_dump() if response.usage else None
    }


def format_conversation(messages: list[dict]) -> str:
    """Format conversation history for display."""
    if not messages:
        return "[No prior conversation]"
    
    formatted = []
    for msg in messages:
        role = msg['role'].upper()
        content = msg['content']
        formatted.append(f"{role}: {content}")
    return "\n\n".join(formatted)


def parse_judgment(text: str) -> tuple[float, str]:
    """Parse score and reasoning from the judge's response."""
    lines = text.strip().split('\n')
    score = None
    reasoning = ""
    
    for i, line in enumerate(lines):
        if line.startswith("Score:"):
            # Extract score

            score_text = line.replace("Score:", "").strip()
            try:
                score = float(score_text.split('/')[0].strip())
            except ValueError:
                score = None
        elif line.startswith("Reasoning:"):
            # Extract reasoning (rest of the text)

            reasoning = line.replace("Reasoning:", "").strip()
            if i + 1 < len(lines):
                reasoning += "\n" + "\n".join(lines[i+1:])
            break
    
    # If parsing fails, use defaults

    if score is None:
        score = 5.0  # Default middle score

    if not reasoning:
        reasoning = text  # Use full text as reasoning

    
    return score, reasoning
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
