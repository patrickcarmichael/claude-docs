---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Start training

First, set your Fireworks API key so the Fireworks CLI can authenticate you:
```bash
export FIREWORKS_API_KEY="<your-fireworks-key>"
```
Next, we'll launch the RFT job using the evaluator and dataset you just registered. We're using a small base model (`qwen3-0p6b`) to keep training fast and inexpensive. Because your evaluator and dataset were already registered with Fireworks in the last step, we don't need to specify them again here.
```bash
cd ..
eval-protocol create rft 
    --base-model accounts/fireworks/models/qwen3-0p6b
```
The CLI will output dashboard links where you can monitor your training job in real-time.

<Frame>
  <img src="https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=ca2553da459a27a7b82771bfae07a6f1" alt="GSM8K evaluation score showing upward trajectory" data-og-width="1090" width="1090" data-og-height="479" height="479" data-path="images/fine-tuning/gsm8k-rft-final.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?w=280&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=ae0c72579e2e6e5654a04138820505d8 280w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?w=560&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=c79460e3470abc158ec08f544bd9f0b6 560w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?w=840&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=c809eba0a3968f99c51b6e6ca1adc38d 840w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?w=1100&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=2fc65dd97cfb82dce989900215e1dd5a 1100w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?w=1650&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=3f2025bacf483a7bea26c0aa3aab61be 1650w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-rft-final.png?w=2500&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=ab6e5c638257937c22b3f0b95f22d0c0 2500w" />
</Frame>

<Tip>
  You can also store your API key in a `.env` file instead of exporting it each session.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
