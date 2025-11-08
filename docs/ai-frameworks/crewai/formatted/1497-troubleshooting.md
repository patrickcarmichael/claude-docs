---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


**Trigger not firing:**

* Verify the trigger is enabled in your deployment's Triggers tab
* Check integration connection status under Tools & Integrations
* Ensure all required environment variables are properly configured

**Execution failures:**

* Check the execution logs for error details
* Use `crewai triggers run <trigger_name>` to test locally and see the exact payload structure
* Verify your crew can handle the `crewai_trigger_payload` parameter
* Ensure your crew doesn't expect parameters that aren't included in the trigger payload

**Development issues:**

* Always test with `crewai triggers run <trigger>` before deploying to see the complete payload
* Remember that `crewai run` does NOT simulate trigger calls—use `crewai triggers run` instead
* Use `crewai triggers list` to verify which triggers are available for your connected integrations
* After deployment, your crew will receive the actual trigger payload, so test thoroughly locally first

Automation triggers transform your CrewAI deployments into responsive, event-driven systems that can seamlessly integrate with your existing business processes and tools.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Building Trigger-Driven Automations](./1496-building-trigger-driven-automations.md)

**Next:** [Azure OpenAI Setup →](./1498-azure-openai-setup.md)
