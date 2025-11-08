---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## call the PythonAstREPLTool in order to pass tables to the tool

df_locals = {'df':pd.read_csv('income_statement.csv')}
tools = [PythonAstREPLTool(locals=df_locals)]

agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )

preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
Here is a preview of the dataframe:
{head_df}
""".format(head_df=income_statement.head(3).to_markdown())
```
Let's loop again over the same dictionary of questions.
```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    agent_executor.invoke({
       "input": val[0],
       "preamble": preamble,
    })
    print(f'GT Answer:{val[1]}')
    print('-'*50)
```
```txt title="Output"
question:q1


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to find the highest value of Cost of Goods and Services Sold from the provided dataframe.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv('income_statement.csv')\n\n# Find the highest value in the 'CostOfGoodsAndServicesSold' column\nmax_value = df['CostOfGoodsAndServicesSold'].max()\n\nprint(f'The highest value of Cost of Goods and Services Sold is {max_value:.2f}')\n"}}

[0m[36;1m[1;3mThe highest value of Cost of Goods and Services Sold is 169559000000.00
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The highest value of Cost of Goods and Services Sold is 169559000000.00.
Grounded answer: The highest value of Cost of Goods and Services Sold is <co: 0="">169559000000.00</co:>.[0m

[1m> Finished chain.[0m
GT Answer:169559000000
--------------------------------------------------
question:q2


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to calculate the largest gross profit margin from the data frame provided.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate the gross profit margin as a percentage\ndf[\'GrossProfitMargin\'] = (df[\'GrossProfit\'] / df[\'RevenueFromContractWithCustomerExcludingAssessedTax\']) * 100\n\n# Find the row with the maximum gross profit margin\nmax_margin_row = df.loc[df[\'GrossProfitMargin\'].idxmax()]\n\nprint(f"The largest gross profit margin is {max_margin_row[\'GrossProfitMargin\']}% on {max_margin_row[\'index\']}")\n'}}

[0m[36;1m[1;3mThe largest gross profit margin is 38.36194330595236% on 2019-12-29-2020-03-28
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The largest gross profit margin is approximately 38.36% on 2019-12-29 to 2020-03-28.
Grounded answer: The largest gross profit margin is <co: 0="">approximately 38.36</co:>% on <co: 0="">2019-12-29 to 2020-03-28</co:>.[0m

[1m> Finished chain.[0m
GT Answer:0.3836194330595236
--------------------------------------------------
question:q3


[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write and execute Python code to calculate the minimum ratio of Operating Income Loss divided by Non Operating Income Expense.
{'tool_name': 'python_interpreter', 'parameters': {'code': "import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv('income_statement.csv')\n\n# Calculate the ratio\nratios = df['OperatingIncomeLoss'] / df['NonoperatingIncomeExpense']\n\n# Find the minimum ratio\nmin_ratio = ratios.min()\n\nprint(f'Minimum ratio: {min_ratio:.2f}')\n"}}

[0m[36;1m[1;3mMinimum ratio: 35.36
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately **35.36**.
Grounded answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately *<co: 0="">*35.36</co:>**.[0m

[1m> Finished chain.[0m
GT Answer:35.360599
--------------------------------------------------
```
Also in this case, the Agent correctly answers all the questions.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
