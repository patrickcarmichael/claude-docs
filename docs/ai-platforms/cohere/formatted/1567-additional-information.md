---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Additional Information

You are an expert who answers the user's question by creating SQL queries and executing them.
You are equipped with a number of relevant SQL tools.

Here is information about the database:
{schema_info}
""".format(schema_info=context)
```
```python PYTHON
output=agent_executor.invoke({
   "input": 'provide the name of the best customer? The customer who has spent the most money is the best.',
   "preamble": preamble
})
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will write a SQL query to find the customer who has spent the most money.
{'tool_name': 'sql_db_query', 'parameters': {'query': 'SELECT c.FirstName, c.LastName, SUM(i.Total) AS TotalSpent FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY c.CustomerId ORDER BY TotalSpent DESC LIMIT 1;'}}
[0m[36;1m[1;3m[('Helena', 'Holý', 49.62)][0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The customer who has spent the most money is Helena Holý.
Grounded answer: The customer who has spent the most money is <co: 0="">Helena Holý</co:>.[0m

[1m> Finished chain.[0m
```
```python PYTHON
print(output['output'])
```
```txt title="Output"
The customer who has spent the most money is Helena Holý.
```
We can see that passing that additional context actually avoids the error seen in the previous section and gets to the answer in one tool call. This works as long as you have a few tables and a few columns per table. We will follow up with more techniques to improve stability and scalability in future work.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
