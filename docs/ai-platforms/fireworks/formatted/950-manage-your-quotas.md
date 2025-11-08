---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Manage your quotas

<AccordionGroup>
  <Accordion title="Budget control">
    Control your monthly spending with flexible budget limits. Set a limit that fits your needs and adjust it anytime.

    ### View and adjust your spend limit

    Check your current spend limit:
```bash
    firectl list quotas
```
    Set a custom monthly budget:
```bash
    firectl update quota monthly-spend-usd --value <AMOUNT>
```
    For example, to set a \$200 monthly budget:
```bash
    firectl update quota monthly-spend-usd --value 200
```
    ### When you reach your budget

    When you reach your spending limit, all API requests pause automatically across serverless inference, deployments, and fine-tuning. To resume, [add credits](https://fireworks.ai/billing) to increase your tier and set a higher budget.
  </Accordion>

  <Accordion title="On-demand deployment quotas">
    On-demand deployments have GPU quotas instead of rate limits:

    | GPU Type                         | Default Quota |
    | -------------------------------- | ------------- |
    | Nvidia A100                      | 8 GPUs        |
    | Nvidia H100                      | 8 GPUs        |
    | Nvidia H200                      | 8 GPUs        |
    | GPU hours/month                  | 2,000         |
    | LoRAs (on-demand and serverless) | 100           |

    <Tip>
      Need more GPUs? [Contact us](https://fireworks.ai/company/contact-us) to request a quota increase.
    </Tip>
  </Accordion>

  <Accordion title="Serverless rate limits">
    ### Default limits

    All accounts with a payment method get these limits:

    | Limit                                    | Value |
    | ---------------------------------------- | ----- |
    | Requests per minute (RPM)                | 6,000 |
    | Audio min per minute, Whisper-v3-large   | 200   |
    | Audio min per minute, Whisper-v3-turbo   | 400   |
    | Concurrent connections, streaming speech | 10    |
    | LoRAs (on-demand and serverless)         | 100   |

    <Tip>
      Make sure to add a [payment method](https://fireworks.ai/billing) to access higher rate limits up to 6,000 RPM. Without a payment method, you're limited to 10 RPM. Your rate limits will increase automatically once the payment method is added.
    </Tip>

    <Tip>
      During periods of high load, RPM limit may be lower.
    </Tip>

    ### How rate limiting works

    Dynamic rate limits support high RPM limits in a fair manner, while limiting spiky traffic from impacting other users:

    * **Gradual scaling**: Your minimum limits increase as you sustain consistent high usage
    * **Typical scale-up**: Traffic can typically double within an hour without issues
    * **Burst handling**: Short traffic spikes are accommodated during autoscaling

    **Monitoring your limits:**

    * Check response headers to see your current limits and remaining capacity
    * `x-ratelimit-limit-requests`: Your current minimum limit
    * `x-ratelimit-remaining-requests`: Remaining capacity
    * `x-ratelimit-over-limit: yes`: Your request was processed but you're near capacity

    <Tip>
      For production workloads requiring consistent performance and higher limits, use [on-demand deployments](/guides/ondemand-deployments). They provide dedicated GPUs with no rate limits and SLA guarantees.
    </Tip>
  </Accordion>

  <Accordion title="Account recovery">
    If your account is suspended due to failed payment:

    1. Go to [Billing → Invoices](https://fireworks.ai/billing)
    2. Pay any outstanding invoices
    3. Your account reactivates automatically within an hour

    <Tip>
      Still suspended after resolving payment issues? Contact support via [Discord](https://discord.gg/fireworks-ai) or email [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).
    </Tip>
  </Accordion>
</AccordionGroup>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
