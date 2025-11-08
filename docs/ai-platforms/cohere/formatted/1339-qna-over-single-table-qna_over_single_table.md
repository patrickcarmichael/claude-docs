---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## QnA over Single Table \[#qna\_over\_single\_table]

In the example below, we show how the Python tool can be used to load a dataframe and extract information from it. To do this successfully we need to:

* Pass the file name to the preamble so the model knows how to load the dataframe
* Pass a preview of the dataframe in the preamble so the model knows which columns/rows to query

We will ask the following questions given income statement data.

* What is the highest value of cost of goods and service?
* What is the largest gross profit margin?
* What is the minimum ratio of operating income loss divided by non operating income expense?
```python PYTHON
question_dict ={
    'q1': ['what is the highest value of cost of goods and service?',169559000000],
    'q2': ['what is the largest gross profit margin?',0.3836194330595236],
    'q3': ['what is the minimum ratio of operating income loss divided by non operating income expense?',35.360599]
}
```
```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Here is a preview of the dataframe:
{head_df}
""".format(head_df=income_statement.head(3).to_markdown())

print(preamble)
```
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Here is a preview of the dataframe:

|    | Unnamed: 0 | index                 | RevenueFromContractWithCustomerExcludingAssessedTax | CostOfGoodsAndServicesSold |  GrossProfit | ResearchAndDevelopmentExpense | SellingGeneralAndAdministrativeExpense | OperatingExpenses | OperatingIncomeLoss | NonoperatingIncomeExpense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | IncomeTaxExpenseBenefit | NetIncomeLoss | EarningsPerShareBasic | EarningsPerShareDiluted | WeightedAverageNumberOfSharesOutstandingBasic | WeightedAverageNumberOfDilutedSharesOutstanding |
| -: | ---------: | :-------------------- | --------------------------------------------------: | -------------------------: | -----------: | ----------------------------: | -------------------------------------: | ----------------: | ------------------: | ------------------------: | ------------------------------------------------------------------------------------------: | ----------------------: | ------------: | --------------------: | ----------------------: | --------------------------------------------: | ----------------------------------------------: |
|  0 |          0 | 2017-10-01-2018-09-29 |                                        265595000000 |                1.63756e+11 | 101839000000 |                    1.4236e+10 |                             1.6705e+10 |        3.0941e+10 |          7.0898e+10 |                 2.005e+09 |                                                                                  7.2903e+10 |              1.3372e+10 |   59531000000 |                     3 |                    2.98 |                                   1.98215e+10 |                                     2.00004e+10 |
|  1 |          1 | 2018-09-30-2018-12-29 |                                         84310000000 |                        nan |  32031000000 |                           nan |                                    nan |               nan |                 nan |                       nan |                                                                                         nan |                     nan |   19965000000 |                  1.05 |                    1.05 |                                           nan |                                             nan |
|  2 |          2 | 2018-09-30-2019-09-28 |                                        260174000000 |                1.61782e+11 |  98392000000 |                    1.6217e+10 |                             1.8245e+10 |        3.4462e+10 |           6.393e+10 |                 1.807e+09 |                                                                                  6.5737e+10 |              1.0481e+10 |   55256000000 |                  2.99 |                    2.97 |                                   1.84713e+10 |                                     1.85957e+10 |
```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    question = val[0]
    answer = val[1]
    output = cohere_agent(question, preamble, tools, verbose=True)
    print(f'GT Answer:{val[1]}')
    print('-'*50)
```
```txt title="Output"
question:q1

running 0th step.
I will use Python to find the highest value of 'CostOfGoodsAndServicesSold' in the 'income_statement.csv' dataframe.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'CostOfGoodsAndServicesSold\'\nhighest_cost = df[\'CostOfGoodsAndServicesSold\'].max()\n\nprint(f"The highest value of \'CostOfGoodsAndServicesSold\' is {highest_cost}")'}

== tool results: [{'python_answer': "The highest value of 'CostOfGoodsAndServicesSold' is 169559000000.0\n"}]
The highest value of 'CostOfGoodsAndServicesSold' is 169559000000.0.
GT Answer:169559000000
--------------------------------------------------
question:q2

running 0th step.
I will write and execute Python code to find the largest gross profit margin.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Calculate gross profit margin\ndf[\'GrossProfitMargin\'] = df[\'GrossProfit\'] / df[\'RevenueFromContractWithCustomerExcludingAssessedTax\'] * 100\n\n# Find the largest gross profit margin\nlargest_gross_profit_margin = df[\'GrossProfitMargin\'].max()\n\nprint(f"The largest gross profit margin is {largest_gross_profit_margin:.2f}%")'}

== tool results: [{'python_answer': 'The largest gross profit margin is 38.36%\n'}]
The largest gross profit margin is 38.36%.
GT Answer:0.3836194330595236
--------------------------------------------------
question:q3

running 0th step.
I will use Python to find the minimum ratio of operating income loss divided by non-operating income expense.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv("income_statement.csv")\n\n# Calculate the ratio of operating income loss to non-operating income expense\ndf["OperatingIncomeLossRatio"] = df["OperatingIncomeLoss"] / df["NonoperatingIncomeExpense"]\n\n# Find the minimum ratio\nmin_ratio = df["OperatingIncomeLossRatio"].min()\n\nprint(f"The minimum ratio of operating income loss to non-operating income expense is: {min_ratio:.2f}")'}

== tool results: [{'python_answer': 'The minimum ratio of operating income loss to non-operating income expense is: 35.36\n'}]
The minimum ratio of operating income loss to non-operating income expense is 35.36.
GT Answer:35.360599
--------------------------------------------------
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
