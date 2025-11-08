---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Connect to the synthetic database

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    
    # Get the list of all tables created

    all_tables = [table[0] for table in con.sql("SHOW TABLES;").fetchall()]
    
    # Select the first 3 tables to display (or all if fewer than 3)

    tables_to_validate = all_tables[:3]

    print("--- Validating the first few tables in the synthetic sandbox ---\n")

    # Execute and print results for the selected tables

    for table_name in tables_to_validate:
        print(f"--- SELECT * FROM {table_name} LIMIT 3; ---")
        try:
            result_df = con.sql(f"SELECT * FROM {table_name} LIMIT 3;").df()
            if not result_df.empty:
                print(tabulate(result_df, headers='keys', tablefmt='psql'))
            else:
                print(f"(Table '{table_name}' is empty)")
        except Exception as e:
            print(f"Query failed for table '{table_name}': {e}")
        print("\n")
```

\--- Validating the first few tables in the synthetic sandbox ---

\--- SELECT \* FROM airlines LIMIT 3; ---

| airline\_id | name                  | alias | iata | icao | callsign     | country      | active |
| ----------- | --------------------- | ----- | ---- | ---- | ------------ | ------------ | ------ |
| 58          | Nordic Eagle Airlines | NEA   | NE   | NEA  | NORDIC EAGLE | Finland      | Y      |
| 70          | Sapphire Sky Airlines | SSA   | SS   | SSA  | SAPPHIRESKY  | South Africa | Y      |
| 86          | Polar Air             | PA    | PL   | POL  | POLARAIR     | Malaysia     | Y      |

\--- SELECT \* FROM airports LIMIT 3; ---

| airport\_id | name                    | city   | country | iata | icao | latitude | longitude | altitude | timezone | dst | tz\_db       | type    | source      |
| ----------- | ----------------------- | ------ | ------- | ---- | ---- | -------- | --------- | -------- | -------- | --- | ------------ | ------- | ----------- |
| 17          | Rainbow Paris Airport   | Paris  | France  | RPA  | RPA  | 48.8566  | 2.3522    | 35       | 1        | E   | Europe/Paris | airport | OurAirports |
| 32          | Orbit Paris Airport     | Paris  | France  | ORP  | ORPA | 48.8566  | 2.3522    | 35       | 1        | E   | Europe/Paris | airport | OurAirports |
| 77          | Red Star Moscow Airport | Moscow | Russia  | RSM  | RSMA | 55.7558  | 37.6173   | 15       |          |     |              |         |             |

\--- SELECT \* FROM countries LIMIT 3; ---

| name         | iso\_code | dafif\_code |
| ------------ | --------- | ----------- |
| Norway       | NO        | NOR         |
| Italy        | IT        | ITA         |
| Saudi Arabia | SA        | SAU         |

### 5. 📝 Generate Example SQL Queries

With our synthetic database in place, the next step is to create a set of synthetic SQL queries. These SQL queries will be executed against our database of synthetic data to get the ground truth labels for RFT. Furthermore, these same SQL queries will be used as input to an LLM to generate queries in natural language. This will enable us to form our final RFT dataset, which pairs natural language queries with ground truth results from the database.

#### Query Generation Strategy:

* **Diversity**: We want queries covering different SQL features (JOINs, GROUP BY, aggregates)
* **Complexity Range**: From simple SELECT statements to complex multi-table joins
* **Deterministic Results**: Queries include ORDER BY clauses where necessary to break ties and ensure consistent results
* **MECE Principle**: Mutually Exclusive, Collectively Exhaustive - covering all major query patterns

>   **Real World 🌍**: You would use a historical log of real SQL queries that have been run against your production database; aim for \~500 unique SQL queries. These logs are the most valuable source of training data because they represent the *actual* way your users query your data.
```python
import pandas as pd
import json
import time
from pydantic import BaseModel, Field
from typing import List
from fireworks import LLM
import os
import duckdb
from dotenv import load_dotenv

load_dotenv()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
