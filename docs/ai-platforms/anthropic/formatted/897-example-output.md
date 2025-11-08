---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Output

To calculate the total sales amount for each salesperson based on the given criteria, you can use the following nested Excel formula:

\=SUMPRODUCT((A2:A100=A2)(B2:B100="Electronics")(MONTH(D2:D100)=1)\*(C2:C100))

Explanation:
The SUMPRODUCT function in Excel allows you to perform multiple calculations and conditions within a single formula. Here's how the formula works:

* (A2:A100=A2) creates an array of TRUE/FALSE values indicating whether each cell in the range A2:A100 matches the salesperson's name in cell A2.
* (B2:B100="Electronics") creates an array of TRUE/FALSE values indicating whether each cell in the range B2:B100 contains the product category "Electronics".
* (MONTH(D2:D100)=1) creates an array of TRUE/FALSE values indicating whether each cell in the range D2:D100 represents a date in the month of January.
* (C2:C100) is the range containing the sales amounts.
  The SUMPRODUCT function multiplies the corresponding elements of these arrays and then sums up the results. In this case, it multiplies the TRUE/FALSE values (1 for TRUE, 0 for FALSE) with the sales amounts, effectively summing only the sales that meet all the specified criteria.
  {' '}
  <Tip>
    **Tip**: Make sure the ranges A2:A100, B2:B100, C2:C100, and D2:D100 cover
    all the relevant data in your table. If your data extends beyond row 100,
    adjust the ranges accordingly. Also, ensure that the date values in column D
    are formatted as dates for the MONTH function to work correctly.
  </Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
