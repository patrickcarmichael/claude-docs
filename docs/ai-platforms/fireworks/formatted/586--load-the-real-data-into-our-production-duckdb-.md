---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- Load the real data into our "production" DuckDB ---

with duckdb.connect(PROD_DB_PATH) as con:
    for name, filename in FILES_TO_DOWNLOAD.items():
        url = f"{BASE_URL}{filename}"
        path = DATA_DIR / filename
        if not path.exists():
            urllib.request.urlretrieve(url, path)
            print(f"✅ Downloaded: {path}")

        # Load data using pandas to handle missing headers and null values

        df = pd.read_csv(path, header=None, names=COLUMN_NAMES[name], na_values=["\\N"])
        con.execute(f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM df")

    print(f"\n✅ 'Production' database simulated at: {PROD_DB_PATH}")
    print("Tables created:", con.sql("SHOW TABLES;").fetchall())
```

✅ 'Production' database simulated at: data/prod\_openflights.db
Tables created: \[('airlines',), ('airports',), ('countries',), ('planes',), ('routes',)]

### 2. 📋 Acquire the Schema (No Real Data!)

This is a critical step. We connect to our "production" database and extract **only its schema** (the table structure, column names, and data types). We do not touch or read any of the data rows. This schema is the only artifact we need from the production environment.

#### Why Schema-Only?

This approach is powerful because:

* **Privacy**: No actual customer data leaves your production environment
* **Security**: No risk of exposing sensitive data during fine-tuning
* **Efficiency**: Schema information is tiny compared to actual data

The `DESCRIBE` command in DuckDB gives us comprehensive schema information without accessing any rows.

>   **Real World 🌍**: You would connect to your production database and run the DESCRIBE command shown below, thus obtaining the schema information for all its tables.
```python
import duckdb

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
