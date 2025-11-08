---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Metrics

In addition to standard metrics like losses, for DPO we report:

* Accuracies — percentage of times the reward for the preferred response is greater than the reward for the non-preferred response.
* KL Divergence — similarity of output distributions between the trained model and the reference model, calculated as:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b8b1d25445ba1bba2b9030465513163f" alt="" data-og-width="1576" width="1576" data-og-height="224" height="224" data-path="images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bcde16cd75ea3a7f5e3104813fe6f84c 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=15681435f5912e1bfa76161bf2ec9a41 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=72a118b288a7f1d3003992773d9446d5 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fb1fb0f5e58457b02b9a2e8b41921ace 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=408caa3fe63b89ae2cb938353cb05a9c 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0bc34a184c15eafcc5598e6db49ae681 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
