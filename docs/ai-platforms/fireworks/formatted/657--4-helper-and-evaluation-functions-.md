---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 4. HELPER AND EVALUATION FUNCTIONS ---

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

def get_sql_and_evaluate(llm_obj, system_prompt: str, user_prompt: str, ground_truth: list[dict]) -> int:
    """
    Calls a pre-configured LLM object to get a SQL query, executes it, and compares to ground truth.
    Returns 1 for a correct result, 0 for an incorrect one.
    """
    try:
        # Step 1: Get SQL from the model

        messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
        response = llm_obj.chat.completions.create(messages=messages, temperature=0.0)
        sql_query = response.choices[0].message.content.strip()

        # Step 2: Execute SQL on MCP server

        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        payload = {"id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call", "params": {"session": {"id": "full-eval-session"}, "name": "query", "arguments": {"query": sql_query}}}

        response_data = None
        with requests.post(f"{MCP_SERVER_URL}/mcp/", headers=headers, json=payload, timeout=30, stream=True) as mcp_response:
            mcp_response.raise_for_status()
            for line in mcp_response.iter_lines():
                if line and line.decode('utf-8').startswith('data:'):
                    json_part = line.decode('utf-8')[len('data:'):].strip()
                    if json_part:
                        response_data = json.loads(json_part)
                        break

        if response_data is None or "error" in response_data:
            return 0

        # Step 3: Parse and compare results

        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)

        return 1 if are_results_equal(predicted_rows, ground_truth) else 0
    except Exception as e:
        print(f"--> Error during evaluation for model {llm_obj.model}: {e}")
        return 0

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
