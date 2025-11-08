---
title: "Extract file path using jq"
source: ""
---

# Extract file path using jq
file_path=$(echo "$input" | jq -r '.tool_info.file_path')

---

← Previous: [Read JSON from stdin](./read-json-from-stdin.md) | [Index](./index.md) | Next: [Format based on file extension](./format-based-on-file-extension.md) →