---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 3. HELPER FUNCTIONS ---

def clean_sql_output(sql_text: str) -> str:
    """
    Cleans SQL output by removing markdown code blocks and extracting pure SQL.
    Handles various formats like ```sql, ```SQL, or just ```
    """
    # Strip leading/trailing whitespace

    sql_text = sql_text.strip()
    
    # Pattern to match markdown code blocks with optional language specification

    # This will match ```sql, ```SQL, ```postgres, or just ```

    pattern = r'^```(?:sql|SQL|postgres|POSTGRES)?\s*\n?(.*?)```$'
    match = re.match(pattern, sql_text, re.DOTALL)
    
    if match:
        # Extract the SQL from within the code block

        sql_text = match.group(1).strip()
    else:
        # If no full code block match, just remove any leading ```sql or trailing ```

        # Remove leading markdown

        sql_text = re.sub(r'^```(?:sql|SQL|postgres|POSTGRES)?\s*\n?', '', sql_text)
        # Remove trailing markdown

        sql_text = re.sub(r'\n?```$', '', sql_text)
    
    return sql_text.strip()

def parse_duckdb_ascii_table(table_string: str) -> list[dict]:
    """
    Parses a DuckDB-style ASCII table string into a list of dictionaries.
    This version robustly handles 'NULL' values and empty strings.
    """
    lines = table_string.strip().split('\n')
    content_lines = [line for line in lines if line.strip() and not line.startswith('+')]
    if len(content_lines) < 2:
        return []
    
    header_raw = [h.strip() for h in content_lines[0].split('|')[1:-1]]
    data_lines = content_lines[1:]
    
    if len(data_lines) > 0:
        try:
            first_data_values = [v.strip() for v in data_lines[0].split('|')[1:-1]]
            if len(first_data_values) == len(header_raw) and all(v.isupper() for v in first_data_values):
                data_lines = data_lines[1:]
        except IndexError:
            pass

    rows = []
    for line in data_lines:
        try:
            values_raw = [v.strip() for v in line.split('|')[1:-1]]
            if len(values_raw) == len(header_raw):
                row_dict = {}
                for i, header in enumerate(header_raw):
                    value_str = values_raw[i]
                    if value_str.upper() == 'NULL' or value_str == '':
                        row_dict[header] = None
                        continue
                    
                    try:
                        if '.' in value_str:
                            row_dict[header] = float(value_str)
                        else:
                            row_dict[header] = int(value_str)
                    except (ValueError, TypeError):
                        row_dict[header] = value_str
                rows.append(row_dict)
        except IndexError:
            continue
    return rows

def are_results_equal(predicted_rows: list[dict], ground_truth_rows: list[dict]) -> bool:
    """
    Compares datasets by converting all values to strings and sorting them,
    which ignores row order, column order, and data types (e.g., int vs float).
    """
    try:
        gt_values = sorted([sorted(map(str, row.values())) for row in ground_truth_rows])
        predicted_values = sorted([sorted(map(str, row.values())) for row in predicted_rows])
        return gt_values == predicted_values
    except Exception:
        return False

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
