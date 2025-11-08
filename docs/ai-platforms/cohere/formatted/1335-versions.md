---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## versions

print('cohere version:', cohere.__version__)
print('langchain version:', langchain.__version__)
print('langchain_core version:', langchain_core.__version__)
print('langchain_experimental version:', langchain_experimental.__version__)
```
```txt title="Output"
cohere version: 5.5.1
langchain version: 0.2.0
langchain_core version: 0.2.0
langchain_experimental version: 0.0.59
```

### API Key

```python PYTHON
COHERE_API_KEY = os.environ["COHERE_API_KEY"]
CHAT_URL= "https://api.cohere.ai/v1/chat"
COHERE_MODEL = 'command-a-03-2025'
co = cohere.Client(api_key=COHERE_API_KEY)
```

### Data Loading

```python PYTHON
income_statement = pd.read_csv('income_statement.csv')
balance_sheet = pd.read_csv('balance_sheet.csv')
```
```python PYTHON
income_statement.head(2)
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Unnamed: 0
        </th>

        <th>
          index
        </th>

        <th>
          RevenueFromContractWithCustomerExcludingAssessedTax
        </th>

        <th>
          CostOfGoodsAndServicesSold
        </th>

        <th>
          GrossProfit
        </th>

        <th>
          ResearchAndDevelopmentExpense
        </th>

        <th>
          SellingGeneralAndAdministrativeExpense
        </th>

        <th>
          OperatingExpenses
        </th>

        <th>
          OperatingIncomeLoss
        </th>

        <th>
          NonoperatingIncomeExpense
        </th>

        <th>
          IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest
        </th>

        <th>
          IncomeTaxExpenseBenefit
        </th>

        <th>
          NetIncomeLoss
        </th>

        <th>
          EarningsPerShareBasic
        </th>

        <th>
          EarningsPerShareDiluted
        </th>

        <th>
          WeightedAverageNumberOfSharesOutstandingBasic
        </th>

        <th>
          WeightedAverageNumberOfDilutedSharesOutstanding
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          0
        </td>

        <td>
          2017-10-01-2018-09-29
        </td>

        <td>
          265595000000
        </td>

        <td>
          1.637560e+11
        </td>

        <td>
          101839000000
        </td>

        <td>
          1.423600e+10
        </td>

        <td>
          1.670500e+10
        </td>

        <td>
          3.094100e+10
        </td>

        <td>
          7.089800e+10
        </td>

        <td>
          2.005000e+09
        </td>

        <td>
          7.290300e+10
        </td>

        <td>
          1.337200e+10
        </td>

        <td>
          59531000000
        </td>

        <td>
          3.00
        </td>

        <td>
          2.98
        </td>

        <td>
          1.982151e+10
        </td>

        <td>
          2.000044e+10
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          1
        </td>

        <td>
          2018-09-30-2018-12-29
        </td>

        <td>
          84310000000
        </td>

        <td>
          NaN
        </td>

        <td>
          32031000000
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          19965000000
        </td>

        <td>
          1.05
        </td>

        <td>
          1.05
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>
      </tr>
    </tbody>
  </table>
</div>
```python PYTHON
balance_sheet.head(2)
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          Unnamed: 0
        </th>

        <th>
          index
        </th>

        <th>
          CashAndCashEquivalentsAtCarryingValue
        </th>

        <th>
          MarketableSecuritiesCurrent
        </th>

        <th>
          AccountsReceivableNetCurrent
        </th>

        <th>
          InventoryNet
        </th>

        <th>
          NontradeReceivablesCurrent
        </th>

        <th>
          OtherAssetsCurrent
        </th>

        <th>
          AssetsCurrent
        </th>

        <th>
          MarketableSecuritiesNoncurrent
        </th>

        <th>
          ...
        </th>

        <th>
          LongTermDebtNoncurrent
        </th>

        <th>
          OtherLiabilitiesNoncurrent
        </th>

        <th>
          LiabilitiesNoncurrent
        </th>

        <th>
          Liabilities
        </th>

        <th>
          CommitmentsAndContingencies
        </th>

        <th>
          CommonStocksIncludingAdditionalPaidInCapital
        </th>

        <th>
          RetainedEarningsAccumulatedDeficit
        </th>

        <th>
          AccumulatedOtherComprehensiveIncomeLossNetOfTax
        </th>

        <th>
          StockholdersEquity
        </th>

        <th>
          LiabilitiesAndStockholdersEquity
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          0
        </td>

        <td>
          2017-09-30
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          ...
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          134047000000
        </td>

        <td>
          NaN
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          1
        </td>

        <td>
          2018-09-29
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          ...
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          NaN
        </td>

        <td>
          107147000000
        </td>

        <td>
          NaN
        </td>
      </tr>
    </tbody>
  </table>

  <p>
    2 rows × 30 columns
  </p>
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
