---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- Schema helpers ---

def map_sql_type_to_python(sql_type: str) -> Type:
    s = str(sql_type).upper()
    if "DECIMAL" in s: return decimal.Decimal
    if any(k in s for k in ("DOUBLE","FLOAT","REAL")): return float
    if any(k in s for k in ("BIGINT","INT")): return int
    if any(k in s for k in ("VARCHAR","TEXT","STRING")): return str
    if "TIMESTAMP" in s: return datetime.datetime
    if "DATE" in s: return datetime.date
    if "TIME" in s: return datetime.time
    if "BOOLEAN" in s: return bool
    if any(k in s for k in ("BLOB","BYTEA")): return bytes
    if "UUID" in s: return uuid.UUID
    return object

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con_ro:
    schema_df = con_ro.sql("DESCRIBE;").df()
schema_for_prompt = schema_df.to_markdown(index=False)

def extract_tables_from_query(sql: str) -> Set[str]:
    """Extract table names from SQL query."""
    # Remove comments

    sql = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)
    sql = re.sub(r'/\*.*?\*/', '', sql, flags=re.DOTALL)
    
    tables = set()
    # Match FROM and JOIN clauses

    patterns = [
        r'(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        r'(?:FROM|JOIN)\s+"([^"]+)"',
        r'(?:FROM|JOIN)\s+`([^`]+)`',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, sql, re.IGNORECASE)
        tables.update(matches)
    
    # Filter out SQL keywords that might be captured

    sql_keywords = {'select', 'where', 'group', 'order', 'having', 'limit', 'as', 'on', 'and', 'or', 'not', 'in', 'exists'}
    tables = {t for t in tables if t.lower() not in sql_keywords}
    
    return tables

def table_columns(name: str) -> List[str]:
    row = schema_df[schema_df["name"] == name]
    if row.empty:
        return []
    return list(row.iloc[0]["column_names"])

def table_types(name: str) -> List[str]:
    row = schema_df[schema_df["name"] == name]
    if row.empty:
        return []
    return list(row.iloc[0]["column_types"])

def build_rows_payload_model(tables: List[str]) -> Type[BaseModel]:
    per_table_row_models: Dict[str, Type[BaseModel]] = {}
    for t in tables:
        cols = table_columns(t)
        types = table_types(t)
        if not cols:
            continue
        fields: Dict[str, Any] = {}
        for c, ty in zip(cols, types):
            fields[c] = (Optional[map_sql_type_to_python(ty)], None)
        per_table_row_models[t] = create_model(f"{t.capitalize()}Row", **fields)
    
    payload_fields: Dict[str, Any] = {}
    for t, row_model in per_table_row_models.items():
        payload_fields[t] = (List[row_model], [])
    
    if not payload_fields:
        return create_model("RowsPayloadFallback", rows=(List[dict], []))
    return create_model("RowsPayload", **payload_fields)

def count_rows(con, sql: str) -> int:
    try:
        return con.sql(f"SELECT COUNT(*) AS c FROM ({sql}) AS t").fetchone()[0]
    except Exception:
        return -1

def get_sample_data(con, table: str, limit: int = 3) -> List[dict]:
    """Get sample rows from a table for context."""
    try:
        df = con.sql(f'SELECT * FROM "{table}" LIMIT {limit}').df()
        return df.to_dict("records")
    except Exception:
        return []

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
