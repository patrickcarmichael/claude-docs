---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Part 1: Teach brevity (Length Gate)

Our opening baseline is a **binary “length‑only” reward**: a summary earns full credit if it stays within the token budget and zero otherwise. This simple gate makes it crystal‑clear to the model that excess verbosity is unacceptable.
```python
def token_len(txt: str) -> int:
    return len(txt.strip().split())

def extract_summary(msgs: List[Dict]) -> Optional[str]:
    for m in reversed(msgs):
        if m.get("role") == "assistant" and not m.get("tool_calls"):
            return m.get("content", "").strip()
    return None
```
```python
@reward_function
def length_gate_only(
    messages:           List[Dict[str, str]],
    original_messages:  Optional[List[Dict[str, str]]] = None,
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)

    if summary is None:
        return EvaluateResult(
            score   = 0.0,
            reason  = "parse error",
            metrics = {"token_len": MetricResult(0, False, "parse error")},
            error   = "parse_error",
        )

    tok_len = token_len(summary)
    if tok_len > 50:
        return EvaluateResult(
            score   = 0.0,
            reason  = f"length {tok_len} > 50 tokens",
            metrics = {"token_len": MetricResult(tok_len, False, str(tok_len))},
        )

    return EvaluateResult(
        score   = 1.0,
        reason  = f"length {tok_len} tokens (within limit)",
        metrics = {"token_len": MetricResult(tok_len, True,  str(tok_len))},
    )
```

Drop this evaluator into Fireworks’ RFT pipeline, point it at your dataset, and you’ll immediately force the model to tighten its summaries. Taking a look at a sample output, we see the following issue:
```python
"An explosion at an LASD training site killed 3 deputies."
```

The model learned that it can output very short “summaries” and achieve very high rewards. We’ll need to iterate on our reward function again.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
