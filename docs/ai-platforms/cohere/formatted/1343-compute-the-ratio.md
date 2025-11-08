---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## compute the ratio

ratio = x/y
print(f"Their ratio is: {ratio}")
```
```txt title="Output"
The largest stockholders equity value is: 134047000000.0
The smallest revenue value is: 53809000000.0
Their ratio is: 2.4911631883142227
```
```python PYTHON
preamble = """
You are an expert who answers the user's question in complete sentences. You are working with two pandas dataframe in Python. Ensure your output is a string.

Here is a preview of the `income_statement.csv` dataframe:
{table_1}

Here is a preview of the `balance_sheet.csv` dataframe:
{table_2}
""".format(table_1=income_statement.head(3).to_markdown(),table_2=balance_sheet.head(3).to_markdown())


print(preamble)
```
```txt title="Output"
You are an expert who answers the user's question in complete sentences. You are working with two pandas dataframe in Python. Ensure your output is a string.

Here is a preview of the `income_statement.csv` dataframe:
|    |   Unnamed: 0 | index                 |   RevenueFromContractWithCustomerExcludingAssessedTax |   CostOfGoodsAndServicesSold |   GrossProfit |   ResearchAndDevelopmentExpense |   SellingGeneralAndAdministrativeExpense |   OperatingExpenses |   OperatingIncomeLoss |   NonoperatingIncomeExpense |   IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest |   IncomeTaxExpenseBenefit |   NetIncomeLoss |   EarningsPerShareBasic |   EarningsPerShareDiluted |   WeightedAverageNumberOfSharesOutstandingBasic |   WeightedAverageNumberOfDilutedSharesOutstanding |
|---:|-------------:|:----------------------|------------------------------------------------------:|-----------------------------:|--------------:|--------------------------------:|-----------------------------------------:|--------------------:|----------------------:|----------------------------:|----------------------------------------------------------------------------------------------:|--------------------------:|----------------:|------------------------:|--------------------------:|------------------------------------------------:|--------------------------------------------------:|
|  0 |            0 | 2017-10-01-2018-09-29 |                                          265595000000 |                  1.63756e+11 |  101839000000 |                      1.4236e+10 |                               1.6705e+10 |          3.0941e+10 |            7.0898e+10 |                   2.005e+09 |                                                                                    7.2903e+10 |                1.3372e+10 |     59531000000 |                    3    |                      2.98 |                                     1.98215e+10 |                                       2.00004e+10 |
|  1 |            1 | 2018-09-30-2018-12-29 |                                           84310000000 |                nan           |   32031000000 |                    nan          |                             nan          |        nan          |          nan          |                 nan         |                                                                                  nan          |              nan          |     19965000000 |                    1.05 |                      1.05 |                                   nan           |                                     nan           |
|  2 |            2 | 2018-09-30-2019-09-28 |                                          260174000000 |                  1.61782e+11 |   98392000000 |                      1.6217e+10 |                               1.8245e+10 |          3.4462e+10 |            6.393e+10  |                   1.807e+09 |                                                                                    6.5737e+10 |                1.0481e+10 |     55256000000 |                    2.99 |                      2.97 |                                     1.84713e+10 |                                       1.85957e+10 |

Here is a preview of the `balance_sheet.csv` dataframe:
|    |   Unnamed: 0 | index      |   CashAndCashEquivalentsAtCarryingValue |   MarketableSecuritiesCurrent |   AccountsReceivableNetCurrent |   InventoryNet |   NontradeReceivablesCurrent |   OtherAssetsCurrent |   AssetsCurrent |   MarketableSecuritiesNoncurrent |   PropertyPlantAndEquipmentNet |   OtherAssetsNoncurrent |   AssetsNoncurrent |        Assets |   AccountsPayableCurrent |   OtherLiabilitiesCurrent |   ContractWithCustomerLiabilityCurrent |   CommercialPaper |   LongTermDebtCurrent |   LiabilitiesCurrent |   LongTermDebtNoncurrent |   OtherLiabilitiesNoncurrent |   LiabilitiesNoncurrent |   Liabilities |   CommitmentsAndContingencies |   CommonStocksIncludingAdditionalPaidInCapital |   RetainedEarningsAccumulatedDeficit |   AccumulatedOtherComprehensiveIncomeLossNetOfTax |   StockholdersEquity |   LiabilitiesAndStockholdersEquity |
|---:|-------------:|:-----------|----------------------------------------:|------------------------------:|-------------------------------:|---------------:|-----------------------------:|---------------------:|----------------:|---------------------------------:|-------------------------------:|------------------------:|-------------------:|--------------:|-------------------------:|--------------------------:|---------------------------------------:|------------------:|----------------------:|---------------------:|-------------------------:|-----------------------------:|------------------------:|--------------:|------------------------------:|-----------------------------------------------:|-------------------------------------:|--------------------------------------------------:|---------------------:|-----------------------------------:|
|  0 |            0 | 2017-09-30 |                            nan          |                  nan          |                   nan          |    nan         |                 nan          |         nan          |   nan           |                    nan           |                   nan          |            nan          |      nan           | nan           |             nan          |               nan         |                            nan         |        nan        |           nan         |        nan           |             nan          |                 nan          |            nan          | nan           |                           nan |                                   nan          |                         nan          |                                        nan        |         134047000000 |                      nan           |
|  1 |            1 | 2018-09-29 |                            nan          |                  nan          |                   nan          |    nan         |                 nan          |         nan          |   nan           |                    nan           |                   nan          |            nan          |      nan           | nan           |             nan          |               nan         |                            nan         |        nan        |           nan         |        nan           |             nan          |                 nan          |            nan          | nan           |                           nan |                                   nan          |                         nan          |                                        nan        |         107147000000 |                      nan           |
|  2 |            2 | 2019-09-28 |                              4.8844e+10 |                    5.1713e+10 |                     2.2926e+10 |      4.106e+09 |                   2.2878e+10 |           1.2352e+10 |     1.62819e+11 |                      1.05341e+11 |                     3.7378e+10 |              3.2978e+10 |        1.75697e+11 |   3.38516e+11 |               4.6236e+10 |                 3.772e+10 |                              5.522e+09 |          5.98e+09 |             1.026e+10 |          1.05718e+11 |               9.1807e+10 |                   5.0503e+10 |              1.4231e+11 |   2.48028e+11 |                             0 |                                     4.5174e+10 |                           4.5898e+10 |                                         -5.84e+08 |          90488000000 |                        3.38516e+11 |
```
```python PYTHON
for qsn,val in question_dict.items():
    print(f'question:{qsn}')
    question = val[0]
    output = cohere_agent(question, preamble, tools, verbose=True)
```
```txt title="Output"
question:q1

running 0th step.
I will use the provided code to find the ratio of the largest stockholders equity to the smallest revenue.

running 1th step.
= running tool run_python_code, with parameters: {'code': 'import pandas as pd\n\n# Read the CSV files into dataframes\nincome_statement = pd.read_csv(\'income_statement.csv\')\nbalance_sheet = pd.read_csv(\'balance_sheet.csv\')\n\n# Find the smallest revenue\nsmallest_revenue = income_statement[\'RevenueFromContractWithCustomerExcludingAssessedTax\'].min()\n\n# Find the largest stockholders equity\nlargest_stockholders_equity = balance_sheet[\'StockholdersEquity\'].max()\n\n# Calculate the ratio\nratio = largest_stockholders_equity / smallest_revenue\nprint(f"The ratio of the largest stockholders equity to the smallest revenue is {ratio:.2f}")'}

== tool results: [{'python_answer': 'The ratio of the largest stockholders equity to the smallest revenue is 2.49\n'}]
The ratio of the largest stockholders equity to the smallest revenue is 2.49.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
