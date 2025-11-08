---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## GPT-2 tiny fluency model (load once)

_tok  = AutoTokenizer.from_pretrained("gpt2")
_gpt2 = AutoModelForCausalLM.from_pretrained("gpt2"); _gpt2.eval()

def fluency(text: str) -> float:
    with torch.no_grad():
        ids  = _tok(text, return_tensors="pt").input_ids
        loss = _gpt2(ids, labels=ids).loss.item()
    return max(0.0, min(1.0, 1 - (loss - 2) / 8))   # maps loss ≈2-10 → score 1-0

@reward_function
def summary_reward_final(
    messages:          List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)
    bullets = extract_bullets(original_messages)

    if summary is None or bullets is None:
        return EvaluateResult(0.0, "parse error",
                              {"coverage": MetricResult(0, False, "parse"),
                               "fluency" : MetricResult(0, False, "parse")},
                              error="parse_error")

    if token_len(summary) > 50:
        tl = token_len(summary)
        return EvaluateResult(0.0, f"length {tl} > 50",
                              {"coverage": MetricResult(0, False, "too long"),
                               "fluency" : MetricResult(0, False, "too long"),
                               "token_len": MetricResult(tl, False, str(tl))})

    cov = max(0.05, rouge_recall(summary, "\n".join(bullets)))
    fl  = max(0.05, fluency(summary))
    score = math.sqrt(cov * fl)

    return EvaluateResult(round(score, 4),
                          f"cov={cov:.2f}, flu={fl:.2f}",
                          {"coverage": MetricResult(cov, cov > .7, f"{cov:.2f}"),
                           "fluency" : MetricResult(fl,  fl > .7, f"{fl:.2f}"),
                           "token_len": MetricResult(token_len(summary), True, str(token_len(summary)))})
```

This blended signal nudges the model to mention every must‑know bullet **and** read naturally, giving us crisp, on‑topic summaries with human‑friendly flow—our final polish after the earlier length and coverage stages.

Here’s an output:
```python
"An explosion at LASD’s SEB facility killed three deputies during explosives training. FBI, ATF, and LAPD responded. Officials offered condolences, and further details are expected from Sheriff Luna as the investigation continues into the apparent accident."
```

Exactly 47 tokens! It names the location, casualties, training context, responding agencies, public response, and the pending investigation—all in polished, complete sentences with no filler.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
