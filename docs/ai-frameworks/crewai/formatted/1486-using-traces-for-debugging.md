---
title: "Crewai: Using Traces for Debugging"
description: "Using Traces for Debugging section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Using Traces for Debugging


Traces are invaluable for troubleshooting issues with your crews:

<Steps>
  <Step title="Identify Failure Points">
    When a crew execution doesn't produce the expected results, examine the trace to find where things went wrong. Look for:

    * Failed tasks
    * Unexpected agent decisions
    * Tool usage errors
    * Misinterpreted instructions

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c892a75b7a22a57949a2641a0fe45bfa" alt="Failure Points" data-og-width="820" width="820" data-og-height="924" height="924" data-path="images/enterprise/failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ecbcbd312dd467cb5cc1dae4a443c56d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c0452a9db1f339e63686941a533d8946 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ded3f2fff055c8d16bcad99ad537da46 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f871feb85f88ba397a259ee8392aef3e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2acf042b2e6b185f1fbc41100751e03f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1e9fc9104e6b55b586a9b13e120de908 2500w" />
    </Frame>
  </Step>

  <Step title="Optimize Performance">
    Use execution metrics to identify performance bottlenecks:

    * Tasks that took longer than expected
    * Excessive token usage
    * Redundant tool operations
    * Unnecessary API calls
  </Step>

  <Step title="Improve Cost Efficiency">
    Analyze token usage and cost estimates to optimize your crew's efficiency:

    * Consider using smaller models for simpler tasks
    * Refine prompts to be more concise
    * Cache frequently accessed information
    * Structure tasks to minimize redundant operations
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Understanding the Trace Interface](./1485-understanding-the-trace-interface.md)

**Next:** [Performance and batching →](./1487-performance-and-batching.md)
