---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## finally, define the preamble

preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Here is a preview of the dataframe:
{head_df}
""".format(head_df=income_statement.head(3).to_markdown())
```
Then, we define the dictionary including the questions we want the Agent to answer, and their answer.
```python PYTHON
question_dict ={
    'q1': ['what is the highest value of cost of goods and service?',169559000000],
    'q2': ['what is the largest gross profit margin?',0.3836194330595236],
    'q3': ['what is the minimum ratio of operating income loss divided by non operating income expense',35.360599]
}
```
Let's now see how the Agent answers each of the questions.
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
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value in the \'CostOfGoodsAndServicesSold\' column\nmax_value = df[\'CostOfGoodsAndServicesSold\'].max()\n\nprint(f"The highest value of Cost of Goods and Services Sold is {max_value}")'}}

[0m[36;1m[1;3mThe highest value of Cost of Goods and Services Sold is 169559000000.0
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The highest value of Cost of Goods and Services Sold is 169559000000.0.
Grounded answer: The highest value of Cost of Goods and Services Sold is <co: 0="">169559000000.0</co:>.[0m

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
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import pandas as pd\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate the ratio\nratios = df[\'OperatingIncomeLoss\'] / df[\'NonoperatingIncomeExpense\']\n\nprint("Minimum ratio:", ratios.min())'}}

[0m[36;1m[1;3mMinimum ratio: 35.36059850374065
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately **35.36**.
Grounded answer: The minimum ratio of Operating Income Loss divided by Non Operating Income Expense is approximately *<co: 0="">*35.36</co:>**.[0m

[1m> Finished chain.[0m
GT Answer:35.360599
--------------------------------------------------
```
Nice! The agent uses the Python tool to write the code to access the data in the tables, and perform the required calculations.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
