---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 1. Dynamically Create Pydantic Models from the SQL Schema ---

def map_sql_type_to_python(sql_type: str) -> Type:
    """Maps SQL data types to Python types for Pydantic models."""
    sql_type_upper = str(sql_type).upper()
    if 'DECIMAL' in sql_type_upper: return decimal.Decimal
    if 'DOUBLE' in sql_type_upper or 'FLOAT' in sql_type_upper or 'REAL' in sql_type_upper: return float
    if 'BIGINT' in sql_type_upper or 'INT' in sql_type_upper: return int
    if 'VARCHAR' in sql_type_upper or 'TEXT' in sql_type_upper or 'STRING' in sql_type_upper: return str
    if 'TIMESTAMP' in sql_type_upper: return datetime.datetime
    if 'DATE' in sql_type_upper: return datetime.date
    if 'TIME' in sql_type_upper: return datetime.time
    if 'BOOLEAN' in sql_type_upper: return bool
    if 'BLOB' in sql_type_upper or 'BYTEA' in sql_type_upper: return bytes
    if 'UUID' in sql_type_upper: return uuid.UUID
    return object

pydantic_models: Dict[str, Type[BaseModel]] = {}
table_names = schema_df['name'].unique()

for table_name in table_names:
    table_schema = schema_df[schema_df['name'] == table_name].iloc[0]
    fields: Dict[str, Any] = {}
    col_names = table_schema['column_names']
    col_types = table_schema['column_types']
    for i, col_name in enumerate(col_names):
        python_type = map_sql_type_to_python(col_types[i])
        fields[col_name] = (Optional[python_type], None)
    model_name = table_name.capitalize() + "Model"
    pydantic_models[table_name] = create_model(model_name, **fields)

dataset_fields: Dict[str, Any] = {
    table_name: (List[model], ...) for table_name, model in pydantic_models.items()
}
SyntheticDataset = create_model('SyntheticDataset', **dataset_fields)
print("✅ Dynamically created Pydantic models for all tables.")


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
