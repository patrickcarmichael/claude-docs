---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 3. HELPER FUNCTION: To parse the server's ASCII table response ---

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
