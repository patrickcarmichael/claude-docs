---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Build the evaluation framework \[#eval-framework]

We now setup the tools we will use for evaluation.

We use three criteria that are graded using LLMs:

* Completeness: checks if the summary includes all the important information from the original text that it should include
* Correctness: checks if there are any hallucinations or factual inaccuracies in the summary
* Conciseness: checks if the summary includes any unnecessary information or wordiness

In this cookbook, we will use Command-R to grade the completions. However, note that in practice, we typically use an ensemble of multiple LLM evaluators to reduce any bias.
```python PYTHON

grading_prompt_template = """You are an AI grader that given a prompt, a completion, and a criterion, grades the completion based on the prompt and criterion. Below is a prompt, a completion, and a criterion with which to grade the completion. You need to respond according to the criterion instructions.

PROMPT:
{prompt}

COMPLETION:
{completion}

CRITERION:
{criteria}

Do not provide an explanation or respond with additional text. Only respond with the final score in the format SCORE: <final_score>

SCORE:"""


criteria_completeness = """Please judge the above completion on whether or not all the completion fully addresses the task posed in the prompt. The completion should contain all the information that is asked for by the prompt while also upholding the constraints mentioned in the prompt. Please return a grade between 1 and 5, where 1 means the completion does not address the prompt at all, 2 means the completion mostly does not address the prompt, 3 is neutral, 4 means the completion mostly addresses the prompt, and 5 means the completion fully addresses the prompt."""

criteria_correctness = """Please judge the above completion on whether or not all information was derived from the prompt and that no information is false. Return a grade between 1 and 5, where 1 means the answers are entirely untruthful relative to the prompt, 2 means the answers are somewhat untruthful relative to the prompt, 3 means neutral, 4 means the answers are somewhat truthful relative to the prompt, and 5 means the answers are entirely truthful relative to the prompt. Evaluate only the truthfulness of the answers, not whether or not they capture all the relevant information in the prompt."""

criteria_conciseness = """Please judge the above completion on whether or not the completion contains any unnecessary information or wordiness that does not help answer the specific instruction given in the prompt. Return a grade between 1 and 5, where 1 means the completion contains many unnecessary details and wordiness that do not answer the specific instruction given in the prompt, 2 means the completion contains some unnecessary details or wordiness, 3 means neutral, 4 means the completion contains few unnecessary details or wordiness, and 5 means the completion contains only necessary details that answer the specific instruction given in the prompt."""


def score_llm(prompt: str, completion: str, criteria: str) -> int:
    """
    Score a completion based on a prompt and a criterion using LLM Because we
    grade all completions on a scale of 1-5, we will normalize the scores by 5 so that the final score
    is between 0 and 1.
    """
    grading_prompt = grading_prompt_template.format(
        prompt=prompt, completion=completion, criteria=criteria
    )
    # Use Cohere to grade the completion

    completion = co.chat(message=grading_prompt, model=co_model, temperature=0.2).text

    ### Alternatively, use OpenAI to grade the completion (requires key)

    # import openai

    # completion = openai.OpenAI(api_key="INSERT OPENAI KEY HERE").chat.completions.create(

    #     model="gpt-4",

    #     messages=[{"role": "user", "content": grading_prompt}],

    #     temperature=0.2,

    # ).choices[0].message.content

    # Extract the score from the completion

    score = float(re.search(r"[12345]", completion).group()) / 5
    return score
```
In addition, we have two criteria that are graded programmatically:

* Format: checks if the summary follows the format (e.g. bullets) that was requested in the prompt
* Length: checks if the summary follows the length that was requested in the prompt.
```python PYTHON

def score_format(completion: str, format_type: str) -> int:
    """
    Returns 1 if the completion is in the correct format, 0 otherwise.
    """
    if format_type == "paragraphs":
        return int(_is_only_paragraphs(completion))
    elif format_type == "bullets":
        return int(_is_only_bullets(completion))
    return 0

def score_length(
    completion: str,
    format_type: str,
    min_val: int,
    max_val: int,
    number: Optional[int] = None
) -> int:
    """
    Returns 1 if the completion has the correct length for the given format, 0 otherwise. This
    includes both word count and number of items (optional).
    """
    # Split into items (each bullet for bullets or each paragraph for paragraphs)

    if format_type == "bullets":
        items = _extract_markdown_bullets(completion, include_bullet=False)
    elif format_type == "paragraphs":
        items = completion.split("\n")

    # Strip whitespace and remove empty items

    items = [item for item in items if item.strip() != ""]

    # Check number of items if provided

    if number is not None and len(items) != number:
        return 0

    # Check length of each item

    for item in items:
        num_words = item.strip().split()
        if min_val is None and len(num_words) > max_val:
            return 0
        elif max_val is None and len(num_words) < min_val:
            return 0
        elif not min_val <= len(num_words) <= max_val:
            return 0
    return 1


def _is_only_bullets(text: str) -> bool:
    """
    Returns True if text is only markdown bullets.
    """
    bullets = _extract_markdown_bullets(text, include_bullet=True)

    for bullet in bullets:
        text = text.replace(bullet, "")

    return text.strip() == ""


def _is_only_paragraphs(text: str) -> bool:
    """
    Returns True if text is only paragraphs (no bullets).
    """
    bullets = _extract_markdown_bullets(text, include_bullet=True)

    return len(bullets) == 0


def _extract_markdown_bullets(text: str, include_bullet: bool = False) -> List[str]:
    """
    Extracts markdown bullets from text as a list. If include_bullet is True, the bullet will be
    included in the output. The list of accepted bullets is: -, *, +, •, and any number followed by
    a period.
    """
    if include_bullet:
        return re.findall(r"^[ \t]*(?:[-*+•]|[\d]+\.).*\w+.*$", text, flags=re.MULTILINE)
    return re.findall(r"^[ \t]*(?:[-*+•]|[\d]+\.)(.*\w+.*)$", text, flags=re.MULTILINE)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
