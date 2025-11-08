---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Errors and Troubleshooting

### Why am I getting an error when uploading a training file?

Common issues:

* Incorrect API key (403 status).
* Insufficient balance (minimum \$5 required). Add a credit card or adjust limits. If balance is sufficient, contact support.

### Why was my job cancelled?

Reasons:

* Insufficient balance.
* Incorrect WandB API key.

Check events via CLI: `$ together list-events <job-fine-tune-id>` or web interface.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c72daddc474b7c58ac078f33a000f6e0" alt="" data-og-width="1106" width="1106" data-og-height="961" height="961" data-path="images/guides/48.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=cd56c516c74446d5a96018aaf5b17771 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1d30d46d9e760daac203362db424da83 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=377e452ba9318eb504c4da8c54e9c79c 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=dbb7ef05f5e68d16766ce444cca50f22 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=97da7406edc7e127c7ad8629770f8505 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/48.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=fd6929a5e71905a334c1d645d8b3bcb5 2500w" />
</Frame>

Example event log for billing limit:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ee5d65a6f7b6d39416ee4d770f8647f0" alt="" data-og-width="1654" width="1654" data-og-height="1484" height="1484" data-path="images/guides/49.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ef33bd87a3f569825c0ca708e3b2fc76 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f49f93a10ac9c19d16566a96387c4bac 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=27488e3c150bd331af52c97681cdccf4 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e28a9d6c76577f5de9fe582ab6994f11 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=be6ae1f2b4771ab888f7632c7c006c23 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/49.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d47edeea1f37908dc310c1872aa62a3b 2500w" />
</Frame>

### What should I do if my job is cancelled due to billing limits?

Add a credit card to increase your spending limit, make a payment, or adjust limits. Contact support if needed.

### Why was there an error while running my job?

If failing after download but before training, likely training data issue. Check event log:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=85298509c50a8fff62e59c6c53f14f30" alt="" data-og-width="1648" width="1648" data-og-height="1140" height="1140" data-path="images/guides/50.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=05054022ed28478f088043eeac5f4369 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9538377bec0fd8dfdbd206f28155867a 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1e1037334d7a9f6b5af2284c80d4f2ea 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=36fd3184594c66ac6226890761081986 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=33eeed12ca878771fbbfad1b75d51413 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/50.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b589880f37eff5eba367ba7e96db5e04 2500w" />
</Frame>

Verify file with: `$ together files check ~/Downloads/unified_joke_explanations.jsonl`

If data passes checks but errors persist, contact support.

For other errors (e.g., hardware failures), jobs may restart automatically with refunds.

### How do I know if my job was restarted?

Jobs restart automatically on internal errors. Check event log for restarts, new job ID, and refunds.

Example:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=05454172c0a1c05d0ab593b263e953ad" alt="" data-og-width="1958" width="1958" data-og-height="404" height="404" data-path="images/guides/51.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f39fe1e133f609f85bdcc3c26a991936 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ee91c0fb691bfe2a38d22f4321673379 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=89cf371d1b489f0c4271ec0799219a14 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=0afdb50badf0ecb4f19623fff7d09115 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=bd0c5232037129595a9d5043ac66ad2e 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/51.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=953d1a91eb74c8358750c151de97a3a1 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
