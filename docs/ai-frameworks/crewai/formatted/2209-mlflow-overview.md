---
title: "Crewai: MLflow Overview"
description: "MLflow Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# MLflow Overview


[MLflow](https://mlflow.org/) is an open-source platform to assist machine learning practitioners and teams in handling the complexities of the machine learning process.

It provides a tracing feature that enhances LLM observability in your Generative AI applications by capturing detailed information about the execution of your application’s services.
Tracing provides a way to record the inputs, outputs, and metadata associated with each intermediate step of a request, enabling you to easily pinpoint the source of bugs and unexpected behaviors.

<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/mlflow-tracing.gif?s=be88ff36aec776c005102164d804322a" alt="Overview of MLflow crewAI tracing usage" data-og-width="1144" width="1144" data-og-height="720" height="720" data-path="images/mlflow-tracing.gif" data-optimize="true" data-opv="3" />

### Features

* **Tracing Dashboard**: Monitor activities of your crewAI agents with detailed dashboards that include inputs, outputs and metadata of spans.
* **Automated Tracing**: A fully automated integration with crewAI, which can be enabled by running `mlflow.crewai.autolog()`.
* **Manual Trace Instrumentation with minor efforts**: Customize trace instrumentation through MLflow's high-level fluent APIs such as decorators, function wrappers and context managers.
* **OpenTelemetry Compatibility**: MLflow Tracing supports exporting traces to an OpenTelemetry Collector, which can then be used to export traces to various backends such as Jaeger, Zipkin, and AWS X-Ray.
* **Package and Deploy Agents**: Package and deploy your crewAI agents to an inference server with a variety of deployment targets.
* **Securely Host LLMs**: Host multiple LLM from various providers in one unified endpoint through MFflow gateway.
* **Evaluation**: Evaluate your crewAI agents with a wide range of metrics using a convenient API `mlflow.evaluate()`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← MLflow Integration](./2208-mlflow-integration.md)

**Next:** [Setup Instructions →](./2210-setup-instructions.md)
