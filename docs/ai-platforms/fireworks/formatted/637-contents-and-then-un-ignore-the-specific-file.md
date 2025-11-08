---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

##    contents, and then un-ignore the specific file.

!data/
data/*
!data/synthetic_openflights.db
```

11. d) Deploy your MCP server as a Cloud Run app by running (from your project root):
```bash
gcloud run deploy mcp-sql-rft-server \
  --source . \
  --region < YOUR_GCP_REGION > \
  --project < YOUR_GCP_PROJECT_ID > \
  --allow-unauthenticated \
  --port 8080
```

Note this will create a default Docker repository called `cloud-run-source-deploy`; press Y to continue when prompted.

11. e) Test that your MCP server is working as expected by running the following from your terminal:
12. e) i. To get your MCP server's URL:
```bash
gcloud run services describe mcp-sql-rft-server \
--project < YOUR_GCP_PROJECT_ID > \
--region < YOUR_GCP_REGION > \
--format="value(status.url)"
```

11. e) ii. (optional) To check the names of the MCP server's available tools:
```bash
curl -X POST "< YOUR_MCP_SERVER_URL_FROM_STEP_i >/mcp/" \
-H "Content-Type: application/json" \
-H "Accept: application/json, text/event-stream" \
-d '{
    "id": "list-tools-1",
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {
        "session": {"id": "test-from-my-laptop"}
    }
}'
```

> Note that the above is a generally useful way to check an MCP server's tools.
> In this case, the tool of interest is the "query" tool.

11. e) iii. To send a test request to the MCP server:
```bash
curl -X POST "< YOUR_MCP_SERVER_URL_FROM_STEP_i >/mcp/" \
-H "Content-Type: application/json" \
-H "Accept: application/json, text/event-stream" \
-d '{
    "id": "query-1",
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "session": {"id": "test-from-my-laptop"},
        "name": "query",
        "arguments": {
            "query": "SELECT COUNT(*) FROM airlines;"
        }
    }
}'
```

### 12. 🔍 Define an evaluation function for RFT

Here, we define an `evaluate` function for RFT, which will interface with our MCP server. Note that you will not directly execute the function here, but will use it as part of the Fireworks Evaluations UI.

#### Understanding the Evaluation Function:

The evaluation function is the heart of RFT. It:

1. Receives the model's generated SQL query
2. Executes it against the real database (via MCP)
3. Compares the result with ground truth
4. Returns a reward score (0 or 1)

This binary reward signal drives the reinforcement learning process. The model learns through trial and error which SQL patterns lead to correct results.

Key design decisions:

* **Exact match comparison**: We normalize values and sort rows to handle different but equivalent result orderings
* **Robust error handling**: SQL syntax errors or execution failures return a score of 0
* **Detailed reasoning**: The function returns explanatory messages for debugging

Ensure that you set MCP\_SERVER\_URL to be your actual MCP server URL from step 11. e) i.

>   **Real World 🌍**\
> You would follow along in the same way here. The evaluation function could also be further customized, with, for example:
>
>   * Partial credit for near-correct answers
>   * Performance-based rewards (faster queries get higher scores)
```python
import requests
import json
import math

MCP_SERVER_URL = None  # <--- PUT MCP SERVER URL HERE without the /mcp/ suffix at the end

def evaluate(messages: list[dict], ground_truth: list[dict], **kwargs) -> dict:
    """
    Evaluates the model's generated SQL query by executing it against a live
    MCP server and comparing the result with the ground_truth.
    """
    
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

    # --- 1. Get MCP Server URL from Environment Variables ---

    mcp_server_url = MCP_SERVER_URL
    if not mcp_server_url:
        return {"score": 0, "is_score_valid": False, "reason": "FATAL: MCP_SERVER_URL environment variable is not set."}

    # --- 2. Get the SQL query from the model's response ---

    sql_query = messages[-1]['content'].strip()
    if not sql_query:
        return {"score": 0, "reason": "Model returned an empty response."}

    # --- 3. Execute the Query against the MCP Server ---

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call",
        "params": {"session": {"id": "stateless-eval-session"}, "name": "query", "arguments": {"query": sql_query}}
    }
    try:
        with requests.post(f"{mcp_server_url}/mcp/", headers=headers, json=payload, timeout=15, stream=True) as response:
            response.raise_for_status()
            response_data = None
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        json_part = decoded_line[len('data:'):].strip()
                        if json_part:
                            response_data = json.loads(json_part)
                            break
            if response_data is None:
                return {"score": 0, "reason": "Could not find JSON data in event stream response from MCP server."}

        if "error" in response_data:
            return {"score": 0, "reason": f"SQL execution failed. Error: {response_data['error'].get('message', 'Unknown')}"}

        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)

    except requests.exceptions.RequestException as e:
        return {"score": 0, "reason": f"Network error calling MCP server: {e}"}
    except json.JSONDecodeError as e:
        return {"score": 0, "reason": f"JSON decode error from server response: {e}"}
    except (KeyError, IndexError):
        return {"score": 0, "reason": f"Failed to parse predicted result from MCP server response structure. Data found: {json.dumps(response_data)}"}
    except Exception as e:
        return {"score": 0, "reason": f"An unexpected error occurred during query execution: {e}"}

    # --- 4. Process Ground Truth ---

    if not isinstance(ground_truth, list):
        return {"score": 0, "is_score_valid": False, "reason": f"FATAL: ground_truth is not a list as expected. Got type: {type(ground_truth)}"}
    ground_truth_rows = ground_truth


    # --- 5. Comparison Logic ---

    def normalize_and_stringify(v):
        """
        Normalizes numbers and None before string conversion.
        """
        if v is None:
            return str(v)
        
        if isinstance(v, float) and not math.isinf(v) and not math.isnan(v) and v == int(v):
            v = int(v)
        return str(v)

    try:
        gt_values = sorted([sorted(map(normalize_and_stringify, row.values())) for row in ground_truth_rows])
        predicted_values = sorted([sorted(map(normalize_and_stringify, row.values())) for row in predicted_rows])

        if gt_values == predicted_values:
            score = 1
            reason = "Success: The SQL query produced the exact expected result."
        else:
            score = 0
            gt_json = json.dumps(ground_truth_rows)
            pred_json = json.dumps(predicted_rows)
            reason = f"Incorrect result. Expected (from ground_truth): {gt_json}. Got (from query): {pred_json}."
    
    except Exception as e:
        return {"score": 0, "reason": f"Error during result comparison: {e}"}

    return {"score": score, "reason": reason}
```

### 13. 🧪 Test English -> SQL of a base model without fine-tuning

Here, we test a base model's ability to generate SQL from a natural language question on a single example from our training data.

This is a quick sanity check that:

1. **Verifies your MCP server is working**: Ensures the server is accessible and can execute queries
2. **Tests the full pipeline**: Confirms that the flow from natural language → SQL generation → execution → result parsing works end-to-end
3. **Shows a concrete example**: Demonstrates what happens when an off-the-shelf model tries to answer a question about your specific database

The test process:

1. Load one example from your training data (by default, the first row)
2. Feed the natural language question to a base model (e.g., Llama 3.1 8B)
3. Execute whatever SQL the model generates against your MCP server
4. Compare the result to the ground truth
5. Print whether it succeeded or failed

What to expect:

* The base model might get it right! Simple queries often work.
* Or, you'll see some kind of failure: wrong column names, missing aliases, incorrect syntax, etc.
* Either outcome is fine; this is just a quick test to see the model in action before fine-tuning.

To try different examples, change `ROW_INDEX_TO_TEST` to test other rows from your dataset.

Ensure that you set MCP\_SERVER\_URL to be your actual MCP server URL from step 11. e) i.

>   **Real World 🌍**\
> You can follow along in the same way here. This single-example test is just a quick way to verify everything is wired up correctly before launching the more expensive fine-tuning job.
```python
import requests
import json
import os
from fireworks import LLM

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
