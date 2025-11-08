---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## One global Rouge scorer – re-use for speed

_ro = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)

def rouge_recall(pred: str, ref: str) -> float:
    return _ro.score(pred, ref)["rougeL"].recall

def extract_doc(orig: List[Dict]) -> Optional[str]:
    return orig[-2].get("content", "").strip() if orig else None  

@reward_function
def summary_reward_v2_doc(
    messages:          List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)
    doc     = extract_doc(original_messages)

    if summary is None or doc is None:
        return EvaluateResult(0.0, "parse error",
                              {"coverage": MetricResult(0, False, "parse")},
                              error="parse_error")

    if token_len(summary) > 50:
        tl = token_len(summary)
        return EvaluateResult(0.0, f"length {tl} > 50",
                              {"coverage": MetricResult(0, False, "too long"),
                               "token_len": MetricResult(tl, False, str(tl))})

    cov = rouge_recall(summary, doc)    # 0–1

    return EvaluateResult(round(cov, 4),
                          f"Rouge-L recall {cov:.2f}",
                          {"coverage": MetricResult(cov, cov > .7, f"{cov:.2f}"),
                           "token_len": MetricResult(token_len(summary), True, str(token_len(summary)))})
```

Running it through the Fireworks RFT pipeline shows us that summaries regain essential details - which is an important counter-balance to the brevity score that we implemented earlier.
```python
"Three LASD deputies dead explosion at SEB training place, maybe accident with explosives, unclear if more hurt, FBI ATF LAPD there, waiting sheriff talk more."
```

This reads much better than before, but it still reads like a bullet mash‑up—missing verbs, punctuation, and time context—so clarity and polish are next on the fix‑list.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
