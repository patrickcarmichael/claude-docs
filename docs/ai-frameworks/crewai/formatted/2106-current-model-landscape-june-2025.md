---
title: "Crewai: Current Model Landscape (June 2025)"
description: "Current Model Landscape (June 2025) section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Current Model Landscape (June 2025)


<Warning>
  **Snapshot in Time**: The following model rankings represent current leaderboard standings as of June 2025, compiled from [LMSys Arena](https://arena.lmsys.org/), [Artificial Analysis](https://artificialanalysis.ai/), and other leading benchmarks. LLM performance, availability, and pricing change rapidly. Always conduct your own evaluations with your specific use cases and data.
</Warning>

### Leading Models by Category

The tables below show a representative sample of current top-performing models across different categories, with guidance on their suitability for CrewAI agents:

<Note>
  These tables/metrics showcase selected leading models in each category and are not exhaustive. Many excellent models exist beyond those listed here. The goal is to illustrate the types of capabilities to look for rather than provide a complete catalog.
</Note>

<Tabs>
  <Tab title="Reasoning & Planning">
    **Best for Manager LLMs and Complex Analysis**

    | Model                      | Intelligence Score | Cost (\$/M tokens) | Speed    | Best Use in CrewAI                                  |
    | :------------------------- | :----------------- | :----------------- | :------- | :-------------------------------------------------- |
    | **o3**                     | 70                 | \$17.50            | Fast     | Manager LLM for complex multi-agent coordination    |
    | **Gemini 2.5 Pro**         | 69                 | \$3.44             | Fast     | Strategic planning agents, research coordination    |
    | **DeepSeek R1**            | 68                 | \$0.96             | Moderate | Cost-effective reasoning for budget-conscious crews |
    | **Claude 4 Sonnet**        | 53                 | \$6.00             | Fast     | Analysis agents requiring nuanced understanding     |
    | **Qwen3 235B (Reasoning)** | 62                 | \$2.63             | Moderate | Open-source alternative for reasoning tasks         |

    These models excel at multi-step reasoning and are ideal for agents that need to develop strategies, coordinate other agents, or analyze complex information.
  </Tab>

  <Tab title="Coding & Technical">
    **Best for Development and Tool-Heavy Workflows**

    | Model                 | Coding Performance | Tool Use Score | Cost (\$/M tokens) | Best Use in CrewAI                            |
    | :-------------------- | :----------------- | :------------- | :----------------- | :-------------------------------------------- |
    | **Claude 4 Sonnet**   | Excellent          | 72.7%          | \$6.00             | Primary coding agent, technical documentation |
    | **Claude 4 Opus**     | Excellent          | 72.5%          | \$30.00            | Complex software architecture, code review    |
    | **DeepSeek V3**       | Very Good          | High           | \$0.48             | Cost-effective coding for routine development |
    | **Qwen2.5 Coder 32B** | Very Good          | Medium         | \$0.15             | Budget-friendly coding agent                  |
    | **Llama 3.1 405B**    | Good               | 81.1%          | \$3.50             | Function calling LLM for tool-heavy workflows |

    These models are optimized for code generation, debugging, and technical problem-solving, making them ideal for development-focused crews.
  </Tab>

  <Tab title="Speed & Efficiency">
    **Best for High-Throughput and Real-Time Applications**

    | Model                   | Speed (tokens/s) | Latency (TTFT) | Cost (\$/M tokens) | Best Use in CrewAI                   |
    | :---------------------- | :--------------- | :------------- | :----------------- | :----------------------------------- |
    | **Llama 4 Scout**       | 2,600            | 0.33s          | \$0.27             | High-volume processing agents        |
    | **Gemini 2.5 Flash**    | 376              | 0.30s          | \$0.26             | Real-time response agents            |
    | **DeepSeek R1 Distill** | 383              | Variable       | \$0.04             | Cost-optimized high-speed processing |
    | **Llama 3.3 70B**       | 2,500            | 0.52s          | \$0.60             | Balanced speed and capability        |
    | **Nova Micro**          | High             | 0.30s          | \$0.04             | Simple, fast task execution          |

    These models prioritize speed and efficiency, perfect for agents handling routine operations or requiring quick responses. **Pro tip**: Pairing these models with fast inference providers like Groq can achieve even better performance, especially for open-source models like Llama.
  </Tab>

  <Tab title="Balanced Performance">
    **Best All-Around Models for General Crews**

    | Model                 | Overall Score | Versatility | Cost (\$/M tokens) | Best Use in CrewAI                |
    | :-------------------- | :------------ | :---------- | :----------------- | :-------------------------------- |
    | **GPT-4.1**           | 53            | Excellent   | \$3.50             | General-purpose crew LLM          |
    | **Claude 3.7 Sonnet** | 48            | Very Good   | \$6.00             | Balanced reasoning and creativity |
    | **Gemini 2.0 Flash**  | 48            | Good        | \$0.17             | Cost-effective general use        |
    | **Llama 4 Maverick**  | 51            | Good        | \$0.37             | Open-source general purpose       |
    | **Qwen3 32B**         | 44            | Good        | \$1.23             | Budget-friendly versatility       |

    These models offer good performance across multiple dimensions, suitable for crews with diverse task requirements.
  </Tab>
</Tabs>

### Selection Framework for Current Models

<AccordionGroup>
  <Accordion title="High-Performance Crews" icon="rocket">
    **When performance is the priority**: Use top-tier models like **o3**, **Gemini 2.5 Pro**, or **Claude 4 Sonnet** for manager LLMs and critical agents. These models excel at complex reasoning and coordination but come with higher costs.

    **Strategy**: Implement a multi-model approach where premium models handle strategic thinking while efficient models handle routine operations.
  </Accordion>

  <Accordion title="Cost-Conscious Crews" icon="dollar-sign">
    **When budget is a primary constraint**: Focus on models like **DeepSeek R1**, **Llama 4 Scout**, or **Gemini 2.0 Flash**. These provide strong performance at significantly lower costs.

    **Strategy**: Use cost-effective models for most agents, reserving premium models only for the most critical decision-making roles.
  </Accordion>

  <Accordion title="Specialized Workflows" icon="screwdriver-wrench">
    **For specific domain expertise**: Choose models optimized for your primary use case. **Claude 4** series for coding, **Gemini 2.5 Pro** for research, **Llama 405B** for function calling.

    **Strategy**: Select models based on your crew's primary function, ensuring the core capability aligns with model strengths.
  </Accordion>

  <Accordion title="Enterprise & Privacy" icon="shield">
    **For data-sensitive operations**: Consider open-source models like **Llama 4** series, **DeepSeek V3**, or **Qwen3** that can be deployed locally while maintaining competitive performance.

    **Strategy**: Deploy open-source models on private infrastructure, accepting potential performance trade-offs for data control.
  </Accordion>
</AccordionGroup>

### Key Considerations for Model Selection

* **Performance Trends**: The current landscape shows strong competition between reasoning-focused models (o3, Gemini 2.5 Pro) and balanced models (Claude 4, GPT-4.1). Specialized models like DeepSeek R1 offer excellent cost-performance ratios.

* **Speed vs. Intelligence Trade-offs**: Models like Llama 4 Scout prioritize speed (2,600 tokens/s) while maintaining reasonable intelligence, whereas models like o3 maximize reasoning capability at the cost of speed and price.

* **Open Source Viability**: The gap between open-source and proprietary models continues to narrow, with models like Llama 4 Maverick and DeepSeek V3 offering competitive performance at attractive price points. Fast inference providers particularly shine with open-source models, often delivering better speed-to-cost ratios than proprietary alternatives.

<Info>
  **Testing is Essential**: Leaderboard rankings provide general guidance, but your specific use case, prompting style, and evaluation criteria may produce different results. Always test candidate models with your actual tasks and data before making final decisions.
</Info>

### Practical Implementation Strategy

<Steps>
  <Step title="Start with Proven Models">
    Begin with well-established models like **GPT-4.1**, **Claude 3.7 Sonnet**, or **Gemini 2.0 Flash** that offer good performance across multiple dimensions and have extensive real-world validation.
  </Step>

  <Step title="Identify Specialized Needs">
    Determine if your crew has specific requirements (coding, reasoning, speed) that would benefit from specialized models like **Claude 4 Sonnet** for development or **o3** for complex analysis. For speed-critical applications, consider fast inference providers like **Groq** alongside model selection.
  </Step>

  <Step title="Implement Multi-Model Strategy">
    Use different models for different agents based on their roles. High-capability models for managers and complex tasks, efficient models for routine operations.
  </Step>

  <Step title="Monitor and Optimize">
    Track performance metrics relevant to your use case and be prepared to adjust model selections as new models are released or pricing changes.
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Key Principles Summary](./2105-key-principles-summary.md)

**Next:** [Using Multimodal Agents →](./2107-using-multimodal-agents.md)
