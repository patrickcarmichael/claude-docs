---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Load the database

Next, we load the database for our manufacturing data.

### Download the sql files from the link below to create the database.

We create an in-memory SQLite database using SQL scripts for the `product_tracking` and `status` tables. You can get the [SQL tables here](https://github.com/cohere-ai/notebooks/tree/main/notebooks/agents/i-5O-sql-agent).

We then create a SQLDatabase instance, which will be used by our LangChain tools and agents to interact with the data.
```python PYTHON
import sqlite3

from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

def get_engine_for_manufacturing_db():
    """Create an in-memory database with the manufacturing data tables."""
    connection = sqlite3.connect(":memory:", check_same_thread=False)

    # Read and execute the SQL scripts

    for sql_file in ['product_tracking.sql', 'status.sql']:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
            connection.executescript(sql_script)

    return create_engine(
        "sqlite://",
        creator=lambda: connection,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
