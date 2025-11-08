---
title: "Crewai: Webhook Output Examples"
description: "Webhook Output Examples section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Webhook Output Examples


**Note:** Any `meta` object provided in your kickoff request will be included in all webhook payloads, allowing you to track requests and maintain context across the entire crew execution lifecycle.

<Tabs>
  <Tab title="Step Webhook">
    `stepWebhookUrl` - Callback that will be executed upon each agent inner thought

    ```json  theme={null}
    {
        "prompt": "Research the financial industry for potential AI solutions",
        "thought": "I need to conduct preliminary research on the financial industry",
        "tool": "research_tool",
        "tool_input": "financial industry AI solutions",
        "result": "**Preliminary Research Report on the Financial Industry for crewai Enterprise Solution**\n1. Industry Overview and Trends\nThe financial industry in ....\nConclusion:\nThe financial industry presents a fertile ground for implementing AI solutions like crewai, particularly in areas such as digital customer engagement, risk management, and regulatory compliance. Further engagement with the lead is recommended to better tailor the crewai solution to their specific needs and scale.",
        "kickoff_id": "97eba64f-958c-40a0-b61c-625fe635a3c0",
        "meta": {
            "requestId": "travel-req-123",
            "source": "web-app"
        }
    }
    ```
  </Tab>

  <Tab title="Task Webhook">
    `taskWebhookUrl` - Callback that will be executed upon the end of each task

    ```json  theme={null}
    {
        "description": "Using the information gathered from the lead's data, conduct preliminary research on the lead's industry, company background, and potential use cases for crewai. Focus on finding relevant data that can aid in scoring the lead and planning a strategy to pitch them crewai.",
        "name": "Industry Research Task",
        "expected_output": "Detailed research report on the financial industry",
        "summary": "The financial industry presents a fertile ground for implementing AI solutions like crewai, particularly in areas such as digital customer engagement, risk management, and regulatory compliance. Further engagement with the lead is recommended to better tailor the crewai solution to their specific needs and scale.",
        "agent": "Research Agent",
        "output": "**Preliminary Research Report on the Financial Industry for crewai Enterprise Solution**\n1. Industry Overview and Trends\nThe financial industry in ....\nConclusion:\nThe financial industry presents a fertile ground for implementing AI solutions like crewai, particularly in areas such as digital customer engagement, risk management, and regulatory compliance.",
        "output_json": {
            "industry": "financial",
            "key_opportunities": ["digital customer engagement", "risk management", "regulatory compliance"]
        },
        "kickoff_id": "97eba64f-958c-40a0-b61c-625fe635a3c0",
        "meta": {
            "requestId": "travel-req-123",
            "source": "web-app"
        }
    }
    ```
  </Tab>

  <Tab title="Crew Webhook">
    `crewWebhookUrl` - Callback that will be executed upon the end of the crew execution

    ```json  theme={null}
    {
        "kickoff_id": "97eba64f-958c-40a0-b61c-625fe635a3c0",
        "result": "**Final Analysis Report**\n\nLead Score: Customer service enhancement and compliance are particularly relevant.\n\nTalking Points:\n- Highlight how crewai's AI solutions can transform customer service\n- Discuss crewai's potential for sustainability goals\n- Emphasize compliance capabilities\n- Stress adaptability for various operation scales",
        "result_json": {
            "lead_score": "Customer service enhancement, and compliance are particularly relevant.",
            "talking_points": [
                "Highlight how crewai's AI solutions can transform customer service with automated, personalized experiences and 24/7 support, improving both customer satisfaction and operational efficiency.",
                "Discuss crewai's potential to help the institution achieve its sustainability goals through better data analysis and decision-making, contributing to responsible investing and green initiatives.",
                "Emphasize crewai's ability to enhance compliance with evolving regulations through efficient data processing and reporting, reducing the risk of non-compliance penalties.",
                "Stress the adaptability of crewai to support both extensive multinational operations and smaller, targeted projects, ensuring the solution grows with the institution's needs."
            ]
        },
        "token_usage": {
            "total_tokens": 1250,
            "prompt_tokens": 800,
            "completion_tokens": 450
        },
        "meta": {
            "requestId": "travel-req-123",
            "source": "web-app"
        }
    }
    ```
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Webhooks](./2434-setting-up-webhooks.md)

**Next:** [FAQs →](./2436-faqs.md)
