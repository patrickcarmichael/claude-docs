---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## We can also store this for later use in prompts

schema_for_prompt = schema_df.to_markdown(index=False)
```

✅ Schema successfully extracted from 'production' database:

| database          | schema | name      | column\_names                                                                | column\_types                                                          | temporary |
| :---------------- | :----- | :-------- | :--------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :-------- |
| prod\_openflights | main   | airlines  | \['airline\_id' 'name' 'alias' 'iata' 'icao' 'callsign' 'country' 'active']  | \['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' | False     |
|                   |        |           |                                                                              | 'VARCHAR']                                                             |           |
| prod\_openflights | main   | airports  | \['airport\_id' 'name' 'city' 'country' 'iata' 'icao' 'latitude' 'longitude' | \['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'DOUBLE'  | False     |
|                   |        |           | 'altitude' 'timezone' 'dst' 'tz\_db' 'type' 'source']                        | 'DOUBLE' 'BIGINT' 'DOUBLE' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR']    |           |
| prod\_openflights | main   | countries | \['name' 'iso\_code' 'dafif\_code']                                          | \['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False     |
| prod\_openflights | main   | planes    | \['name' 'iata' 'icao']                                                      | \['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False     |
| prod\_openflights | main   | routes    | \['airline' 'airline\_id' 'source\_airport' 'source\_airport\_id'            | \['VARCHAR' 'DOUBLE' 'VARCHAR' 'DOUBLE' 'VARCHAR' 'DOUBLE' 'VARCHAR'   | False     |
|                   |        |           | 'destination\_airport' 'destination\_airport\_id' 'codeshare' 'stops'        | 'BIGINT' 'VARCHAR']                                                    |           |
|                   |        |           | 'equipment']                                                                 |                                                                        |           |

### 3. 🧪 Create the Synthetic Training Sandbox with an LLM

Now that we have the schema, we will use a large language model to generate a complete, contextually-aware synthetic dataset.

#### Key Concepts in This Step:

**Dynamic Pydantic Model Generation**: We dynamically create Pydantic models based on your database schema. This ensures the LLM's output is structured and parseable, adapting to any database schema automatically.

**Chunked Generation Strategy**: Instead of asking for all data at once (which could overwhelm the LLM or hit token limits), we generate data in small chunks of 2 rows per API call. This approach:

* Ensures high-quality, coherent data
* Avoids token limit issues

**Contextual Awareness**: Each generation request includes previously generated data as context, preventing duplicates and ensuring variety.

To fine-tune our model with RFT, **we will only interact with this synthetic database.**

>   **Real World 🌍**: This pattern is directly applicable. You would use the same approach with your production schema to generate synthetic data that maintains the structure and relationships of your real data without exposing any actual records.
```python
import pandas as pd
import os
from pydantic import create_model, BaseModel
from fireworks import LLM
import duckdb
import json
from dotenv import load_dotenv
from typing import List, Optional, Any, Dict, Type
import datetime
import decimal
import uuid
import math
import time


TARGET_ROW_COUNT = 100  # The number of rows to generate for each table.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
