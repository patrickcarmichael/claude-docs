---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 4. EVALUATION FUNCTIONS for OpenAI and Anthropic ---

def get_sql_and_evaluate_openai(client, model_id: str, system_prompt: str, user_prompt: str, ground_truth: list[dict]) -> int:
    """
    Calls OpenAI API, executes SQL, and compares to ground truth.
    """
    try:
        messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
        response = client.chat.completions.create(model=model_id, messages=messages, temperature=0.0)
        raw_output = response.choices[0].message.content.strip()
        
        # Clean the SQL output

        sql_query = clean_sql_output(raw_output)

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

        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)
        
        is_correct = are_results_equal(predicted_rows, ground_truth)
        return 1 if is_correct else 0
    except Exception as e:
        print(f"--> Error during evaluation for model {model_id}: {e}")
        return 0

def get_sql_and_evaluate_anthropic(client, model_id: str, system_prompt: str, user_prompt: str, ground_truth: list[dict]) -> int:
    """
    Calls Anthropic API, executes SQL, and compares to ground truth.
    """
    try:
        response = client.messages.create(model=model_id, system=system_prompt, messages=[{"role": "user", "content": user_prompt}], temperature=0.0, max_tokens=2048)
        raw_output = response.content[0].text.strip()
        
        # Clean the SQL output

        sql_query = clean_sql_output(raw_output)

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

        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)
        
        is_correct = are_results_equal(predicted_rows, ground_truth)
        return 1 if is_correct else 0
    except Exception as e:
        print(f"--> Error during evaluation for model {model_id}: {e}")
        return 0

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
