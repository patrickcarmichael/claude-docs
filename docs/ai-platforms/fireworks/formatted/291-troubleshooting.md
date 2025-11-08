---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

### Common Issues

1. **Authentication Errors**:
```
   Error: Authentication failed. Check your API key.
```
   Solution: Ensure `FIREWORKS_API_KEY` is correctly set.

2. **Metrics Folder Not Found**:
```
   Error: Metrics folder not found: ./my_metrics/clarity
```
   Solution: Check that the path exists and contains a valid `main.py` file.

3. **Invalid Sample File**:
```
   Error: Failed to parse sample file. Ensure it's a valid JSONL file.
```
   Solution: Verify the sample file is in the correct JSONL format.

4. **Deployment Permission Issues**:
```
   Error: Permission denied. Your API key doesn't have deployment permissions.
```
   Solution: Use a production API key with deployment permissions or request additional permissions.

5. **Task Bundle Validation Errors**:
```
   Error: Missing required files in task bundle: tools.py, reward.py
```
   Solution: Ensure your task bundle has all required files.

6. **Model API Key Not Set**:
```
   Warning: MODEL_AGENT environment variable is not set
```
   Solution: Set the MODEL\_AGENT environment variable or use the --model parameter.

7. **Import Errors with Task Bundle**:
```
   Error: Failed to import tool registry from example.task.tools
```
   Solution: Check that the Python path is correct and the module can be imported.

### Getting Help

For additional help, use the `--help` flag with any command:
```bash
reward-kit --help
reward-kit preview --help
reward-kit deploy --help
reward-kit agent-eval --help
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
