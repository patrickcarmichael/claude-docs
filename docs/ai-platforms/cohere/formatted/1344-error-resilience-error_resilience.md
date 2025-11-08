---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error Resilience \[#error\_resilience]

In the previous example over single table, the model successfully answered your questions. However, the model may not always have access to the preview of the data. You will see that when we remove the preview from the preamble, the model runs into an error and is not produce the answer. We will solve this problem with two different ways:

* Asking the model to keep trying until it fixes the issue.
* Giving the model another tool to view the data and telling it to preview the data before writing code.

You will see that the second method is able to come to the answer with fewer steps.
```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
"""

question1 = "what is the highest value of cost of goods and service?"

output = cohere_agent(question1, preamble, tools, verbose=True)
```
```txt title="Output"
running 0th step.
I will use Python to find the highest value of 'Cost of Goods and Service' in the 'income_statement.csv' file.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'Cost of Goods and Service\'\nhighest_cost = df[\'Cost of Goods and Service\'].max()\n\nprint(f"The highest value of \'Cost of Goods and Service\' is: {highest_cost}")'}

== tool results: [{'python_answer': "KeyError('Cost of Goods and Service')"}]
Sorry, there is no column named 'Cost of Goods and Service' in the 'income_statement.csv' file.
```
As you see above, the model failed to execute because it assumed certain column names but they turned out to be wrong. One simple fix is to tell the model to continue to solve the problem in the face of error.
```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
If you run into error, keep trying until you fix it. You may need to view the data to understand the error.
"""

question1 = "what is the highest value of cost of goods and service?"

output = cohere_agent(question1, preamble, tools, verbose=True)
```
```txt title="Output"
running 0th step.
I will use Python to find the highest value of cost of goods and service.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'Cost of Goods and Services\'\nhighest_cost = df[\'Cost of Goods and Services\'].max()\n\nprint(f"The highest value of \'Cost of Goods and Services\' is: {highest_cost}")'}

== tool results: [{'python_answer': "KeyError('Cost of Goods and Services')"}]
I encountered an error. I will now view the data to understand the error.

running 2th step.
= running tool run_python_code, with parameters: {'code': "import pandas as pd\n\ndf = pd.read_csv('income_statement.csv')\n\nprint(df.columns)"}
== tool results: [{'python_answer': "Index(['Unnamed: 0', 'index',\n       'RevenueFromContractWithCustomerExcludingAssessedTax',\n       'CostOfGoodsAndServicesSold', 'GrossProfit',\n       'ResearchAndDevelopmentExpense',\n       'SellingGeneralAndAdministrativeExpense', 'OperatingExpenses',\n       'OperatingIncomeLoss', 'NonoperatingIncomeExpense',\n       'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',\n       'IncomeTaxExpenseBenefit', 'NetIncomeLoss', 'EarningsPerShareBasic',\n       'EarningsPerShareDiluted',\n       'WeightedAverageNumberOfSharesOutstandingBasic',\n       'WeightedAverageNumberOfDilutedSharesOutstanding'],\n      dtype='object')\n"}]
I found that the column name is 'CostOfGoodsAndServicesSold'. I will now use this to find the highest value.

running 3th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\ndf = pd.read_csv(\'income_statement.csv\')\n\n# Find the highest value of \'Cost of Goods and Services\'\nhighest_cost = df[\'CostOfGoodsAndServicesSold\'].max()\n\nprint(f"The highest value of \'Cost of Goods and Services\' is: {highest_cost}")'}

== tool results: [{'python_answer': "The highest value of 'Cost of Goods and Services' is: 169559000000.0\n"}]
The highest value of 'Cost of Goods and Services' is 169559000000.0.
```

### Add Viewing Tool \[#add\_viewing\_tool]

What if we directly give the model the ability to view the data as a tool so that it can explicitly use it instead of indirectly figuring it out?
```python PYTHON
def view_csv_data(path: str) -> dict:
    """
    Function to view the head, tail and shape of a given csv file.
    """
    df = pd.read_csv(path)

    return {
        "head": df.head().to_string(),
        "tail": df.tail().to_string(),
        "shape": str(df.shape),
    }

functions_map = {
    "run_python_code": run_python_code,
    "view_csv_data": view_csv_data
}

tools = [
    {
        "name": "run_python_code",
        "description": "given a python code, runs it",
        "parameter_definitions": {
            "code": {
                "description": "executable python code",
                "type": "str",
                "required": True
            }
        }
    },
    {
        "name": "view_csv_data",
        "description": "give path to csv data and get head, tail and shape of the data",
        "parameter_definitions": {
            "path": {
                "description": "path to csv",
                "type": "str",
                "required": True
            }
        }
    },
]
```
```python PYTHON
preamble = """
You are an expert who answers the user's question. You are working with a pandas dataframe in Python. The name of the dataframe is `income_statement.csv`.
Always view the data first to write flawless code.
"""

question1 = "what is the highest value of cost of goods and service?"

output = cohere_agent(question1, preamble, tools, verbose=True)
```
```txt title="Output"
running 0th step.
I will first view the data and then write and execute Python code to find the highest value of cost of goods and service.

running 1th step.
= running tool view_csv_data, with parameters: {'path': 'income_statement.csv'}
== tool results: [{'head': '   Unnamed: 0                  index  RevenueFromContractWithCustomerExcludingAssessedTax  CostOfGoodsAndServicesSold   GrossProfit  ResearchAndDevelopmentExpense  SellingGeneralAndAdministrativeExpense  OperatingExpenses  OperatingIncomeLoss  NonoperatingIncomeExpense  IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest  IncomeTaxExpenseBenefit  NetIncomeLoss  EarningsPerShareBasic  EarningsPerShareDiluted  WeightedAverageNumberOfSharesOutstandingBasic  WeightedAverageNumberOfDilutedSharesOutstanding\n0           0  2017-10-01-2018-09-29                                         265595000000                1.637560e+11  101839000000                   1.423600e+10                            1.670500e+10       3.094100e+10         7.089800e+10               2.005000e+09                                                                                 7.290300e+10             1.337200e+10    59531000000                   3.00                     2.98                                   1.982151e+10                                     2.000044e+10\n1           1  2018-09-30-2018-12-29                                          84310000000                         NaN   32031000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    19965000000                   1.05                     1.05                                            NaN                                              NaN\n2           2  2018-09-30-2019-09-28                                         260174000000                1.617820e+11   98392000000                   1.621700e+10                            1.824500e+10       3.446200e+10         6.393000e+10               1.807000e+09                                                                                 6.573700e+10             1.048100e+10    55256000000                   2.99                     2.97                                   1.847134e+10                                     1.859565e+10\n3           3  2018-12-30-2019-03-30                                          58015000000                         NaN   21821000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    11561000000                   0.62                     0.61                                            NaN                                              NaN\n4           4  2019-03-31-2019-06-29                                          53809000000                         NaN   20227000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    10044000000                   0.55                     0.55                                            NaN                                              NaN', 'tail': '    Unnamed: 0                  index  RevenueFromContractWithCustomerExcludingAssessedTax  CostOfGoodsAndServicesSold   GrossProfit  ResearchAndDevelopmentExpense  SellingGeneralAndAdministrativeExpense  OperatingExpenses  OperatingIncomeLoss  NonoperatingIncomeExpense  IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest  IncomeTaxExpenseBenefit  NetIncomeLoss  EarningsPerShareBasic  EarningsPerShareDiluted  WeightedAverageNumberOfSharesOutstandingBasic  WeightedAverageNumberOfDilutedSharesOutstanding\n6            6  2019-09-29-2019-12-28                                          91819000000                         NaN   35217000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    22236000000                   1.26                     1.25                                            NaN                                              NaN\n7            7  2019-09-29-2020-09-26                                         274515000000                1.695590e+11  104956000000                   1.875200e+10                            1.991600e+10       3.866800e+10         6.628800e+10                803000000.0                                                                                 6.709100e+10             9.680000e+09    57411000000                   3.31                     3.28                                   1.735212e+10                                     1.752821e+10\n8            8  2019-12-29-2020-03-28                                          58313000000                         NaN   22370000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    11249000000                   0.64                     0.64                                            NaN                                              NaN\n9            9  2020-03-29-2020-06-27                                          59685000000                         NaN   22680000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    11253000000                   0.65                     0.65                                            NaN                                              NaN\n10          10  2020-06-28-2020-09-26                                          64698000000                         NaN   24689000000                            NaN                                     NaN                NaN                  NaN                        NaN                                                                                          NaN                      NaN    12673000000                   0.74                     0.73                                            NaN                                              NaN', 'shape': '(11, 17)'}]
The column name is 'CostOfGoodsAndServicesSold'. I will now write and execute Python code to find the highest value in this column.

running 2th step.
= running tool run_python_code, with parameters: {'code': "import pandas as pd\n\ndf = pd.read_csv('income_statement.csv')\n\nprint(df['CostOfGoodsAndServicesSold'].max())"}
== tool results: [{'python_answer': '169559000000.0\n'}]
The highest value of cost of goods and services is 169559000000.0.
```
By being prescriptive, we were able to cut down a step and get to the answer faster.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
