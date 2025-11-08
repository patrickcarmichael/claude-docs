---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Takeaways

By walking a plain language model through four reward tweaks—length gate, document overlap, key‑bullet focus, and a final fluency blend—we steered it into a dependable 50‑token summarizer. Each change showed, in minutes, how the model bends to whatever signal we supply, thanks to the lightweight evaluator‑swap workflow built into Fireworks’ RFT platform.

1. **A model follows its incentives, not your intentions.** Define the right reward and you steer behaviour directly; leave gaps and the model finds them.
2. **Start simple, then layer complexity.** A binary length check exposed verbosity problems instantly; later signals refined relevance and style.
3. **End‑to‑end feedback beats imitation alone.** Rewarding the full output captures goals that token‑level training can’t touch.

The exercise also showed how quickly you can iterate when evaluators are first‑class citizens: swap one in, rerun, and immediately trace the effect. Keep that loop handy, keep the reward honest, and your models will do exactly what you ask—**nothing more, nothing less.**

That’s the demo — let the summaries speak for themselves.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
