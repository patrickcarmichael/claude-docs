---
title: "Crewai: Performance and batching"
description: "Performance and batching section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Performance and batching


CrewAI batches trace uploads to reduce overhead on high-volume runs:

* A TraceBatchManager buffers events and sends them in batches via the Plus API client
* Reduces network chatter and improves reliability on flaky connections
* Automatically enabled in the default trace listener; no configuration needed

This yields more stable tracing under load while preserving detailed task/agent telemetry.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with trace analysis or any other CrewAI AMP features.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Using Traces for Debugging](./1486-using-traces-for-debugging.md)

**Next:** [Webhook Streaming →](./1488-webhook-streaming.md)
