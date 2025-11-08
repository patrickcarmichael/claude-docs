---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 6: Run the Training Pipeline

Now you're ready to kick off the full training pipeline! nanochat includes a `speedrun.sh` script that orchestrates all training phases:
```bash
  bash speedrun.sh

  # or you can use screen

  screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh
```

This script will execute the following stages:

1. **Tokenizer Training** - Trains a GPT-4 style BPE tokenizer on FineWeb-Edu data
2. **Base Model Pretraining** - Trains the base transformer model with rotary embeddings and Muon optimizer
3. **Midtraining** - Fine-tunes on a curated mixture of SmolTalk, MMLU, and GSM8K tasks
4. **Supervised Fine-Tuning (SFT)** - Aligns the model for conversational interactions
5. **Evaluation** - Runs CORE benchmarks and generates a comprehensive report

The entire training process takes approximately **4 hours** on 8×H100 GPUs.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=d77d394dee60ff4576f461932ba317df" alt="" data-og-width="2606" width="2606" data-og-height="2212" height="2212" data-path="images/guides/nanochat/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=b2832b8925d4f7f4970400ff91a15ec2 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=aad30fd3ce919b479e3dc0281cad59a9 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=ef3fbc34fdbc444163f2e26fb9ebe7c7 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=3cc7cc6b28114b7ea531358c75b2e509 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=f67b83d0e53dcf9fdf7a081fcaf8316a 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/4.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=a70b3e9c60091511189a4fd0b7d233c5 2500w" />
</Frame>

**Monitor Training Progress**

During training, you can monitor several key metrics:

* **Model Flops Utilization (MFU)**: Should be around 50% for optimal performance
* **tok/sec**: Tracks tokens processed per second of training
* **Step timing**: Each step should complete in a few seconds

The scripts automatically log progress and save checkpoints under `$NANOCHAT_BASE_DIR`.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=82bdc348257581badd6ef22c819dcd10" alt="" data-og-width="2606" width="2606" data-og-height="2212" height="2212" data-path="images/guides/nanochat/5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=280&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4e696d8c87ad41292392fb66fc94140a 280w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=560&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=ebb08f3efee42a3c74b55b7fe0a89181 560w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=840&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4b4512ce3929c97609967e1f2cb39f16 840w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=1100&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=770f79729d0154ba5f5c275e6921eb95 1100w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=1650&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=4ea8ea07ebf4844d562e75036e8858c3 1650w, https://mintcdn.com/togetherai-52386018/nCgXSa6ThqEuOBrA/images/guides/nanochat/5.png?w=2500&fit=max&auto=format&n=nCgXSa6ThqEuOBrA&q=85&s=889ec5da7ce8c3b69d42a1fbe6a2fbdb 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
