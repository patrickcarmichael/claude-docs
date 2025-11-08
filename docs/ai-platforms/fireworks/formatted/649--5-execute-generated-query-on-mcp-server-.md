---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 5. EXECUTE GENERATED QUERY ON MCP SERVER ---

predicted_rows = []
if model_generated_sql:
    try:
        print("\n" + "="*20)
        print("MCP SERVER EXECUTION")
        print("="*20)
        print(f"Sending query to MCP server...")
        
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        payload = {
            "id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call",
            "params": {"session": {"id": "stateless-eval-session"}, "name": "query", "arguments": {"query": model_generated_sql}}
        }

        with requests.post(f"{MCP_SERVER_URL}/mcp/", headers=headers, json=payload, timeout=20, stream=True) as response:
            response.raise_for_status()
            response_data = None
            for line in response.iter_lines():
                if line and line.decode('utf-8').startswith('data:'):
                    json_part = line.decode('utf-8')[len('data:'):].strip()
                    if json_part:
                        response_data = json.loads(json_part)
                        break
            
            if response_data is None: raise RuntimeError("No JSON data in event stream.")
            if "error" in response_data: raise RuntimeError(f"SQL Error: {response_data['error'].get('message', 'Unknown')}")

            ascii_table = response_data['result']['content'][0]['text']
            predicted_rows = parse_duckdb_ascii_table(ascii_table)
            print("\nParsed Result from Server:")
            print(json.dumps(predicted_rows, indent=2))

    except Exception as e:
        print(f"\nAN ERROR OCCURRED during MCP call: {e}")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
