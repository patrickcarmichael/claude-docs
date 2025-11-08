---
title: "Crewai: OpenLIT Overview"
description: "OpenLIT Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# OpenLIT Overview


[OpenLIT](https://github.com/openlit/openlit?src=crewai-docs) is an open-source tool that makes it simple to monitor the performance of AI agents, LLMs, VectorDBs, and GPUs with just **one** line of code.

It provides OpenTelemetry-native tracing and metrics to track important parameters like cost, latency, interactions and task sequences.
This setup enables you to track hyperparameters and monitor for performance issues, helping you find ways to enhance and fine-tune your agents over time.

<Frame caption="OpenLIT Dashboard">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2b7fe9d84e9ec2b33c5eae6fa5668bee" alt="Overview Agent usage including cost and tokens" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/openlit1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c971bf515a852fd31020a8b1324f1c1c 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=84c289d1cb65df00729c0265b937953d 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a2f16c0fff510b112190d86e4d660f57 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d16913f544b0bab3b1b6df63f9d221eb 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f3fb2555418f5a64d567b5ab2c16da87 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=58ca748851de32f75bfeb36bb2cbdcfa 2500w" />

  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=74bb57f622b6eeb67fd33d93d682df26" alt="Overview of agent otel traces and metrics" data-og-width="3024" width="3024" data-og-height="1728" height="1728" data-path="images/openlit2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5f8faf220f9d7a5660652ec531dd07f9 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a02410c4bf920c9aafe972416e52a400 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=21b69af51e7ed46fb5b38a932a64471b 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b32ebaa0e210ff7151bb831d4e2fd5fc 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c360d0388bd1af92dedde1967e41017f 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9f14c8d65a0ca1177c2aa848c7a57aaa 2500w" />

  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=734cbc0c8fee538986d74b063c20cef6" alt="Overview of agent traces in details" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/openlit3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=37d3f6eb4f5b66f6466fba0c02137aec 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9769fd3fdadf6acd8eadb2f80b4cc352 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=0f3367e37d8642fe4aa81f444c17b03d 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a2c9c17452fde4610823a981d60ce226 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bf6526be4832980353137d0e19e38768 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a0c09334de9c7d1bb7f90a7ea636379f 2500w" />
</Frame>

### Features

* **Analytics Dashboard**: Monitor your Agents health and performance with detailed dashboards that track metrics, costs, and user interactions.
* **OpenTelemetry-native Observability SDK**: Vendor-neutral SDKs to send traces and metrics to your existing observability tools like Grafana, DataDog and more.
* **Cost Tracking for Custom and Fine-Tuned Models**: Tailor cost estimations for specific models using custom pricing files for precise budgeting.
* **Exceptions Monitoring Dashboard**: Quickly spot and resolve issues by tracking common exceptions and errors with a monitoring dashboard.
* **Compliance and Security**: Detect potential threats such as profanity and PII leaks.
* **Prompt Injection Detection**: Identify potential code injection and secret leaks.
* **API Keys and Secrets Management**: Securely handle your LLM API keys and secrets centrally, avoiding insecure practices.
* **Prompt Management**: Manage and version Agent prompts using PromptHub for consistent and easy access across Agents.
* **Model Playground** Test and compare different models for your CrewAI agents before deployment.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← OpenLIT Integration](./2220-openlit-integration.md)

**Next:** [Setup Instructions →](./2222-setup-instructions.md)
