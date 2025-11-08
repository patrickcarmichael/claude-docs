---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Output

Here's the LaTeX code to create a simple table with three columns and two rows, including a header row with the titles "Name," "Age," and "City," and a data row with the values "John," "25," and "New York":
```LaTeX
\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|}
\hline
Name & Age & City \\
\hline
John & 25 & New York \\
\hline
\end{tabular}
\caption{Sample Table}
\label{tab:sample}
\end{table}
```
Explanation:

* The `table` environment is used to create a floating table that can be positioned automatically by LaTeX.
* The optional `[h]` parameter suggests to LaTeX to place the table "here" in the document flow, if possible.
* The `\centering` command centers the table horizontally on the page.
* The `tabular` environment is used to create the actual table structure.
* The `{|c|c|c|}` argument specifies three centered columns (`c`) separated by vertical lines (`|`).
* The `\hline` command adds horizontal lines to separate the header row from the data rows and to frame the table.
* The `&` character separates the cells within a row, and `\\` marks the end of a row.
* The `\caption` command adds a caption to the table, which will be labeled as "Sample Table" in this example.
* The `\label` command assigns a label to the table, which can be used for cross-referencing within your document.

When you compile your LaTeX document, this code will generate a table that looks like this:
```
+------+-----+----------+
| Name | Age |   City   |
+------+-----+----------+
| John |  25 | New York |
+------+-----+----------+
```
***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
