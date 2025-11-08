---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Integration Options

Fireworks metrics can be integrated with various observability platforms through multiple approaches:

### OpenTelemetry Collector Integration

The Fireworks metrics endpoint can be integrated with OpenTelemetry Collector by configuring a Prometheus receiver that scrapes the endpoint. This allows Fireworks metrics to be pushed to a variety of popular exporters—see the [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/) for a full list.

### Direct Prometheus Integration

To integrate directly with Prometheus, specify the Fireworks metrics endpoint in your scrape config:
```yaml
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'fireworks'
    metrics_path: 'v1/accounts/<account-id>/metrics'
    authorization:
      type: "Bearer"
      credentials: "YOUR_API_KEY"
    static_configs:
      - targets: ['api.fireworks.ai']
    scheme: https
```
For more details on Prometheus configuration, refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

### Supported Platforms

Fireworks metrics can be exported to various observability platforms including:

* Prometheus
* Datadog
* Grafana
* New Relic

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
