---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 4: Conversation with Memory using AI Messages and Human Messages \[#sec\_step4]

```python PYTHON
a2_mem_ai_hum = agent_executor.invoke({
   "input": q2,
   "chat_history": [HumanMessage(content=q1),
                    AIMessage(content=a1['output'])] # we add here the human query and the generation of the model at turn 1

})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will copy and paste the code from the previous conversation into this one, and then use it to plot the revenue numbers.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\nimport matplotlib.pyplot as plt\n\ndata = pd.read_csv('modified_revenue_table.csv')\n\n# Plot the revenue numbers\nplt.plot(data['revenue'])\n\nplt.savefig('revenue_plot.png')"}}

[0m[36;1m[1;3m[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: Here's a plot of the revenue numbers:
<img alt="Revenue plot" revenue_plot.png""="" src=""/>
Grounded answer: Here's a plot of the revenue numbers:
<co: 0="">! [Revenue plot]("revenue_plot.png")</co:>[0m

[1m> Finished chain.[0m
```
It works! Let's go on with the conversation.
```python PYTHON
q3 = "set the min of y axis to zero and the max to 1000"
a3_mem_ai_hum = agent_executor.invoke({
   "input": q3,
   "chat_history": [HumanMessage(content=q1),
                    AIMessage(content=a1['output']),
                    HumanMessage(content=q2), # we now add info from turn 2

                    AIMessage(content=a2_mem_ai_hum['output'])]
})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will copy and paste the previous code and make the changes requested by the user. Then I will execute the code to plot the graph with the changes applied.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\nimport matplotlib.pyplot as plt\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv("modified_revenue_table.csv")\n\n# Plot revenue against time\nplt.plot(df["time"], df["revenue"], marker="o")\n\n# Set minimum and maximum values for y-axis\nplt.ylim(0, 1000)\n\nplt.savefig("revenue_plot.png")'}}

[0m[36;1m[1;3m[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: Here's the plot with the requested changes:
<img alt="Revenue plot" revenue_plot.png""="" src=""/>
Grounded answer: Here's the plot with the requested changes:
<co: 0="">! [Revenue plot]("revenue_plot.png")</co:>[0m

[1m> Finished chain.[0m
```
The model does what we asked, but it decides to introduce the marker="o" in the plotting function. While in this case the modification of the code does not affect the quality of the output, this is still an undesidered behaviour, since the model is introducing a modification that was not required.

To address this problem, we can further enrich the chat history by adding information from the reasoning chain.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
