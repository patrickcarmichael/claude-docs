---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Have a multi-turn conversation with the ReAct agent

The chat history enables you to have multi-turn conversations with the ReAct agent.
```python PYTHON
from langchain_core.messages import HumanMessage, AIMessage

chat_history = [
    HumanMessage(content="I'm considering switching to Oracle for my CRM."),
    AIMessage(content="That sounds like a good idea! How can I help you?"),
    HumanMessage(content="Recap me all the info you can find about their offering."),
]

prompt = ChatPromptTemplate.from_messages(chat_history)
```
```python PYTHON
agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search, vectorstore_search, python_tool],
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=[internet_search, vectorstore_search, python_tool], verbose=True)
```
```python PYTHON
response = agent_executor.invoke({
    "preamble": preamble,
})

response['output']
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will search for 'Oracle CRM offering' and relay the information I find to the user.
{'tool_name': 'internet_search', 'parameters': {'query': 'Oracle CRM offering'}}
[0m[36;1m[1;3m[{'url': 'https://docs.oracle.com/en/applications/siebel/', 'content': 'Siebel CRM delivers a combination of transactional, analytical, and engagement features to manage all customer-facing operations. With solutions tailored to more than 20 industries, Siebel CRM delivers comprehensive on-premise CRM solutions that are tailored industry solutions with role-based customer intelligence and pre-built integration.'}, {'url': 'https://www.softwareadvice.com/resources/breaking-down-oracle-crm/', 'content': "Oracle's Marketing Cloud provides a comprehensive set of tools that cover a range of digital marketing needs. This includes tools for cross-channel marketing, i.e., marketing automation for both B2B and B2C marketers, as well as data management, content marketing and social media marketing. Cross-Channel Marketing."}, {'url': 'https://www.trustradius.com/products/oracle-crm-on-demand/reviews?qs=pros-and-cons', 'content': "What is Oracle CRM On Demand?The basis of this offering is the Market2Lead product that Oracle acquired in 2010. It has now been fully integrated with Oracle's On Demand CRM product and is a full-featured marketing automation product with features from lead management and nurturing, to measuring marketing ROI."}, {'url': 'https://www.oracle.com/cx/siebel/', 'content': 'In addition to standard CRM functionality, this industry solution includes asset, premises, and contracts management; work orders; oil well management and oil field service; B2C and B2B web portals; and credit and fraud management capabilities.\nDesigned for pharmaceutical sales, Siebel CRM Life Sciences provides personalized content delivery tools to help sales and marketing teams deliver the right messages during each customer interaction.\n Marketing, sales, and customer service applications are fully integrated and designed to manage the complex interactions and relationships between brand owners, their partners (including brokers and distributors), their customers, and the end consumer.\n It leverages data and AI to transform CX–launching offers, acquiring and retaining customers, omnichannel ecommerce and customer care, and fulfilling and monetizing services.\n It leverages data and AI to transform CX–launching offers, acquiring and retaining customers, omnichannel ecommerce and customer care, and fulfilling and monetizing services.\n Provide world-class citizen services while delivering comprehensive, cost-efficient case management and policy management, including social services, justice and public safety, constituent services/311, self-service citizen portals, tax and revenue, and licensing and permitting.\n'}, {'url': 'https://www.suretysystems.com/insights/oracle-customer-relationship-management-a-complete-overview/', 'content': 'Effective CRM systems offer the following features for enterprise users: Simple, easy-to-use interface; ... Oracle CRM simplifies customer relationship management by enhancing customer interactions and improving customer satisfaction and sales growth. Oracle Client Experience (CX), a connected suite of tools that transcends standard CRM ...'}][0m[32;1m[1;3mRelevant Documents: 0,1,2,3,4
Cited Documents: 0,1,2,3,4
Answer: Oracle's CRM offering includes the following:
- Marketing Cloud, which provides a comprehensive set of tools that cover a range of digital marketing needs, including cross-channel marketing, marketing automation, data management, content marketing and social media marketing
- CRM On Demand, which is a full-featured marketing automation product with features from lead management and nurturing, to measuring marketing ROI
- Siebel CRM, which delivers a combination of transactional, analytical, and engagement features to manage all customer-facing operations, with solutions tailored to more than 20 industries
- Siebel CRM Life Sciences, which provides personalised content delivery tools to help sales and marketing teams deliver the right messages during each customer interaction
- Oracle Client Experience (CX), a connected suite of tools that transcends standard CRM
Grounded answer: Oracle's CRM offering includes the following:
- <co: 1="">Marketing Cloud</co:>, which provides a <co: 1="">comprehensive set of tools</co:> that cover a <co: 1="">range of digital marketing needs</co:>, including <co: 1="">cross-channel marketing</co:>, <co: 1="">marketing automation</co:>, <co: 1="">data management</co:>, <co: 1="">content marketing</co:> and <co: 1="">social media marketing</co:>
- <co: 2="">CRM On Demand</co:>, which is a <co: 2="">full-featured marketing automation product</co:> with features from <co: 2="">lead management and nurturing</co:>, to <co: 2="">measuring marketing ROI</co:>
- <co: 0,3="">Siebel CRM</co:>, which delivers a <co: 0="">combination of transactional, analytical, and engagement features</co:> to <co: 0="">manage all customer-facing operations</co:>, with <co: 0="">solutions tailored to more than 20 industries</co:>
- <co: 3="">Siebel CRM Life Sciences</co:>, which provides <co: 3="">personalised content delivery tools</co:> to help <co: 3="">sales and marketing teams deliver the right messages during each customer interaction</co:>
- <co: 4="">Oracle Client Experience (CX</co:>), a <co: 4="">connected suite of tools</co:> that <co: 4="">transcends standard CRM</co:>[0m

[1m> Finished chain.[0m


"Oracle's CRM offering includes the following:\n- Marketing Cloud, which provides a comprehensive set of tools that cover a range of digital marketing needs, including cross-channel marketing, marketing automation, data management, content marketing and social media marketing\n- CRM On Demand, which is a full-featured marketing automation product with features from lead management and nurturing, to measuring marketing ROI\n- Siebel CRM, which delivers a combination of transactional, analytical, and engagement features to manage all customer-facing operations, with solutions tailored to more than 20 industries\n- Siebel CRM Life Sciences, which provides personalised content delivery tools to help sales and marketing teams deliver the right messages during each customer interaction\n- Oracle Client Experience (CX), a connected suite of tools that transcends standard CRM"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
