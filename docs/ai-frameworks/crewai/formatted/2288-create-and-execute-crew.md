---
title: "Crewai: Create and execute crew"
description: "Create and execute crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create and execute crew

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

result = crew.kickoff()
```

### Observability and Governance

Monitor your CrewAI agents through TrueFoundry's metrics tab:
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=33755ff848cb457e162e806c20c98216" alt="TrueFoundry metrics" data-og-width="3840" width="3840" data-og-height="1984" height="1984" data-path="images/gateway-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=49a01b5e5bcc0429efd529860c020c10 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=3f47f171146339690e3516a892020626 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=857541d282cce3557f796ade097be01c 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2f2b883b00e823ceb25ae1b747c656a4 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9ddee789557bdbaacec42fd405180458 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e9097f84b482e5c4da153d2d0271e6bf 2500w" />

With Truefoundry's AI gateway, you can monitor and analyze:

* **Performance Metrics**: Track key latency metrics like Request Latency, Time to First Token (TTFS), and Inter-Token Latency (ITL) with P99, P90, and P50 percentiles
* **Cost and Token Usage**: Gain visibility into your application's costs with detailed breakdowns of input/output tokens and the associated expenses for each model
* **Usage Patterns**: Understand how your application is being used with detailed analytics on user activity, model distribution, and team-based usage
* **Rate limit and Load balancing**: You can set up rate limiting, load balancing and fallback for your models

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create tasks](./2287-create-tasks.md)

**Next:** [Tracing →](./2289-tracing.md)
