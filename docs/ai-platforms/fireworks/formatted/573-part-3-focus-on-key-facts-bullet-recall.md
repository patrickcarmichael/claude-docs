---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Part 3: Focus on key facts (Bullet Recall)

Our third evaluator narrows the comparison window from the **entire source document** to a **curated bullet list of key facts**. Pure document‑level ROUGE can reward nonsense phrases that merely echo scattered words; by contrast, scoring against a focused checklist forces the model to mention the specific points humans actually care about.

The downside is cost: generating high‑quality bullet lists requires either human or much larger LLM annotation.

For example, a bullet point list of our new example might look like the following:
```python
[
"An explosion occurred at the LASD Special Enforcement Bureau (SEB) training facility in Monterey Park around 7:30 a.m.",
"Three sheriff’s deputies were killed, reportedly while handling explosives; cause appears accidental.",
"FBI, ATF, LAPD bomb squad, and L.A. County Fire responded; further injuries are unconfirmed.",
"Officials including Governor Newsom and Supervisors Barger and Solis issued condolences; more details pending from Sheriff Luna.",
]
```

Let’s enhance our dataset by adding this list and start writing our reward function. We’ll keep parts that we’ve developed so far and build upon that.
```python
def extract_bullets(orig: List[Dict]) -> Optional[List[str]]:
    return orig[-1].get("bullets") if orig else None

@reward_function
def summary_reward_v3_bullets(
    messages:          List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    bullets:           Optional[List[str]]
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)
    bullets = extract_bullets(original_messages)

    if summary is None or bullets is None:
        return EvaluateResult(0.0, "parse error",
                              {"coverage": MetricResult(0, False, "parse")},
                              error="parse_error")

    if token_len(summary) > 50:
        tl = token_len(summary)
        return EvaluateResult(0.0, f"length {tl} > 50",
                              {"coverage": MetricResult(0, False, "too long"),
                               "token_len": MetricResult(tl, False, str(tl))})

    joined = "\n".join(bullets)
    cov    = rouge_recall(summary, joined)

    return EvaluateResult(round(cov, 4),
                          f"Rouge-L recall {cov:.2f}",
                          {"coverage": MetricResult(cov, cov > .7, f"{cov:.2f}"),
                           "token_len": MetricResult(token_len(summary), True, str(token_len(summary)))})
```

Once again, let’s run it through our pipeline and get a sample result:
```python
"Three LASD deputies died in a likely accidental blast at SEB facility. FBI, ATF, LAPD responded. Officials expressed condolences. Details from Sheriff awaited."
```

By rewarding matches to these distilled key facts, the model learns to deliver summaries that are short **and** on-point—no more empty verbage, far fewer hallucinations. It looks a lot better than when we first started. We could reasonably stop here—the summaries are now short and reliably cover the must‑know facts—but let’s push one step further.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
