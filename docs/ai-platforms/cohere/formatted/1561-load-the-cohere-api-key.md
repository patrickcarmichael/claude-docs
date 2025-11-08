---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## load the cohere api key

os.environ["COHERE_API_KEY"] = ""
```
```python PYTHON
DB_NAME='Chinook.db'
MODEL="command-a-03-2025"
llm = ChatCohere(model=MODEL, temperature=0.1,verbose=True)
db = SQLDatabase.from_uri(f"sqlite:///{DB_NAME}")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
context = toolkit.get_context()
tools = toolkit.get_tools()

print('**List of pre-defined Langchain Tools**')
print([tool.name for tool in tools])
```
```txt title="Output"
**List of pre-defined Langchain Tools**
['sql_db_query', 'sql_db_schema', 'sql_db_list_tables', 'sql_db_query_checker']
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
