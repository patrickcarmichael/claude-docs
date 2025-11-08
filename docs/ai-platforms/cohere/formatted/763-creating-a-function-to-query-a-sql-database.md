---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating a function to query a SQL database

Next, we'll define a function called `sql_table_query` that allows us to execute SQL queries on our evaluation\_results database.

This function will enable us to retrieve and analyze data from our evaluation\_results table, allowing for dynamic querying based on our specific needs.
```python PYTHON
def sql_table_query(query: str) -> dict:
    """
    Execute an SQL query on the evaluation_results table and return the result as a dictionary.

    Args:
    query (str): SQL query to execute on the evaluation_results table

    Returns:
    dict: Result of the SQL query
    """
    try:
        # Connect to the SQLite database

        conn = sqlite3.connect("evaluation_results.db")

        # Execute the query and fetch the results into a DataFrame

        df = pd.read_sql_query(query, conn)

        # Close the connection

        conn.close()

        # Convert DataFrame to dictionary

        result_dict = df.to_dict(orient="records")

        return result_dict

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return str(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return str(e)


functions_map = {"sql_table_query": sql_table_query}
```
We can test the function by running a simple query:
```python PYTHON
result = sql_table_query(
    "SELECT * FROM evaluation_results WHERE usecase = 'extract_names'"
)
print(result)
```
```mdx

[{'usecase': 'extract_names', 'run': 'A', 'score': 0.5, 'temperature': 0.3, 'tokens': 103, 'latency': 1.12}, {'usecase': 'extract_names', 'run': 'B', 'score': 0.2, 'temperature': 0.3, 'tokens': 101, 'latency': 2.85}, {'usecase': 'extract_names', 'run': 'C', 'score': 0.7, 'temperature': 0.3, 'tokens': 101, 'latency': 2.22}, {'usecase': 'extract_names', 'run': 'D', 'score': 0.7, 'temperature': 0.5, 'tokens': 120, 'latency': 3.2}]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
