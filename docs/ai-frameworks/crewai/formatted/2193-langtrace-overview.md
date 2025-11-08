---
title: "Crewai: Langtrace Overview"
description: "Langtrace Overview section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Langtrace Overview


Langtrace is an open-source, external tool that helps you set up observability and evaluations for Large Language Models (LLMs), LLM frameworks, and Vector Databases.
While not built directly into CrewAI, Langtrace can be used alongside CrewAI to gain deep visibility into the cost, latency, and performance of your CrewAI Agents.
This integration allows you to log hyperparameters, monitor performance regressions, and establish a process for continuous improvement of your Agents.

<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=85b67e42028ca9383087737279f8931f" alt="Overview of a select series of agent session runs" data-og-width="1717" width="1717" data-og-height="1299" height="1299" data-path="images/langtrace1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ba769f765ef36edf033e2caf8c7df4c7 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9e24743472c91a4b42dc235c8b16691a 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f70296efa8dd1619670008b9af8d7e78 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c8281aea8f979aa38ff1b6519e3fb840 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c55eafbe3e6fee44aaa208f8ce988847 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace1.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=677e866fb2e110afc4e7f6800abafdc3 2500w" />
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=24f08e5c56b6200e386d305a7bee347c" alt="Overview of agent traces" data-og-width="1725" width="1725" data-og-height="1094" height="1094" data-path="images/langtrace2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9182a51d34df98e5a5b7b994b6d11d4d 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=fa10f203c90f5394c5a3fe5b96b52685 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1a1d34a1ac4c2d2d5a4748e4a4a46c97 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=81bb4d002d59c63f80c2cff7f2afbadd 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=de0fe6458f4595f73615ce7acb6b5d37 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace2.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1cf56b30d10a0ef841aa762fa27c74a2 2500w" />
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f1a8624e0c05d59deded640e4751a986" alt="Overview of llm traces in details" data-og-width="1710" width="1710" data-og-height="1217" height="1217" data-path="images/langtrace3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=3483f588b90a032d4919847e6e63772a 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c638c41d0e0e156c2c2e0ed1e80bfde1 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6d2b588d0a6c176a8fd80e4d3844d955 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=611c9167a54facb43c95a2239bba6a39 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=62a6bfc0052934c423ce245ddef1a28e 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langtrace3.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=726ee5e7feed10e6f507233807e70ae9 2500w" />

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Langtrace Integration](./2192-langtrace-integration.md)

**Next:** [Setup Instructions →](./2194-setup-instructions.md)
