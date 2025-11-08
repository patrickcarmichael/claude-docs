---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What this tutorial will cover

| You'll practice …                                              | … and walk away with                                                                      |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| ✅ **Generate a synthetic DuckDB** that mirrors your schema     | `synthetic_openflights.db` (\<20 MB) served via an MCP endpoint                           |
| ✅ **Create a MECE query set** & compute ground-truth rows      | `generated_queries.json` & `ground_truth_results.json`                                    |
| ✅ **Build NL ↔ SQL result pairs** for fine-tuning and eval     | `final_rft_sql_train_data.jsonl` & `final_rft_sql_test_data.jsonl`                        |
| ✅ **Run an RFT job on Fireworks AI**                           | A tuned **Qwen 2.5-7B** checkpoint                                                        |
| ✅ **Benchmark baseline vs. tuned model** and a larger baseline | > 30% exact-match improvement over Qwen 2.5-7B base model and > 20% over SoTA base models |

### Agenda

0. 🛠️ Development Environment Setup
1. 🗄️ Simulate the "Production" Database
2. 📋 Acquire the Schema (No Real Data!)
3. 🧪 Create the Synthetic Training Sandbox with an LLM
4. ✅ Validate the Sandbox
5. 📝 Generate Example SQL Queries
6. ♻️ Query-Aware Augmentation of the Synthetic Sandbox
7. 🎯 Execute Queries to Get Ground-Truth Answers
8. 💬 Generate Natural Language Questions for Final RFT Training Data
9. 🛰️ Deploy an MCP Server for the Synthetic Data
10. ☁️ Set Up Google Cloud CLI & .gcloudignore
11. 📦 Containerize & Deploy the MCP Server
12. 🔍 Define an evaluation function for RFT
13. 🧪 Test English -> SQL of a base model without fine-tuning
14. 🚀 Launch the Fine-Tuning Job & Deploy via the UI
15. ⚖️ Evaluate Model Performance
16. ✨ Cleanup & Conclusion

>   **Demo vs Real World 🌍**\
> Look for these call-outs to see the difference between the self-contained demo steps in this notebook and the equivalent actions you’d perform on your own private schema, logs, and query store.

### 0. 🛠️ Development Environment Setup

**Complete these steps once in your terminal, *outside* this notebook.**

1. **Get a Fireworks AI API Key**
   * Go to [fireworks.ai](https://fireworks.ai) and sign up.
   * Create an API key from your settings page.
   * Create a file named `.env` in your project directory and add your key:
```
     FIREWORKS_API_KEY="YOUR_API_KEY_HERE"
```

2. **Install `uv`**
   * `uv` is a fast Python package manager from Astral. Follow the official installation instructions at [docs.astral.sh/uv/](https://docs.astral.sh/uv/).
   * It's significantly faster than pip and handles dependency resolution more reliably.

3. **Create a Virtual Environment and Install Packages**
   * Once `uv` is installed, initialize a project.
```bash
   # Run this in your terminal

   uv init --python 3.12
```
   * Install all required packages using `uv add`.
```bash
   # Run this in your terminal

   uv add duckdb tabulate pandas pyarrow requests \
          pydantic python-dotenv \
          jsonlines fireworks-ai \
          mcp-server-motherduck ipykernel
```
   * Create and activate a virtual environment
```bash
   # Run this in your terminal

   uv sync
   source .venv/bin/activate
```

After running these commands, your environment is ready. You can proceed with the tutorial.

### 1. 🗄️ Simulate the "Production" Database

First, we'll create a database that represents your real, populated production database. We'll download the public OpenFlights dataset and load it into a DuckDB file.

#### What is DuckDB?

DuckDB is an in-process SQL OLAP database management system. Think of it as "SQLite for analytics". It's perfect for this tutorial because:

* It's embedded (no server setup required)
* It's fast for analytical queries
* It has excellent SQL compatibility
* The entire database is just a single file
* It has an existing MCP server we can use ([mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck))

>   **Real World 🌍**: You already have this! It's your live production database (or a replica). You would skip this entire step.
```python
import urllib.request
import pathlib
import pandas as pd
import duckdb

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
