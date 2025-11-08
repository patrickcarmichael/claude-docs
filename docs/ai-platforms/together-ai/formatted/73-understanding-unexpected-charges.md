---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Understanding Unexpected Charges

If you're seeing charges on your account without making API calls, you may be incurring costs from deployed resources that continue to run even when not actively used.

### Common Causes of Unexpected Charges

1. **Fine-tuned Model Hosting**: Deployed fine-tuned models incur per-minute hosting fees regardless of API usage. These charges continue until you stop the endpoint.

2. **Dedicated Endpoints**: These are charged based on hardware allocation, even without active requests. Charges accrue as long as the endpoint remains active.

3. **Serverless Model Usage**: Charged based on actual token usage and model size - you only pay for what you use.

### Managing Your Deployments

To avoid unexpected charges:

1. Visit your [models dashboard](https://api.together.xyz/models)
2. Check for deployed fine-tuned models or active dedicated endpoints
3. Stop any unused endpoints

Monitor usage and pricing at [together.ai/pricing](https://www.together.ai/pricing). Deployment charges are separate from usage charges and credit purchases.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
