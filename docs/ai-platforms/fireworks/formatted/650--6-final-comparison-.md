---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## --- 6. FINAL COMPARISON ---

print("\n" + "="*20)
print("COMPARISON")
print("="*20)

if not predicted_rows:
    print("Skipping comparison: no rows returned from query or an error occurred.")
else:
    gt_values = sorted([sorted(map(str, row.values())) for row in GROUND_TRUTH_ROWS])
    predicted_values = sorted([sorted(map(str, row.values())) for row in predicted_rows])

    if gt_values == predicted_values:
        print("\n✅ GOOD RESULT: The base model generated SQL that produced the correct data.\n")
    else:
        print("\n❌ BAD RESULT: The base model's SQL produced different data than expected.\n")
        print("This is often the intended outcome when testing a base model, as it highlights what fine-tuning needs to correct.")
```
```text
    Successfully loaded row 0 from 'data/final_rft_sql_train_data.jsonl'.
    
    {'messages': [{'role': 'system', 'content': "You are an expert SQL data analyst.\nYour task is to write a single, valid DuckDB SQL query to answer the user's question, based on the provided database schema.\nWrite only the raw SQL query text and nothing else (i.e., no markdown formatting); your output should be a directly executable valid SQL query.\nMake sure your queries do not return duplicate rows (i.e., GROUP BY all columns that are not aggregate functions).\nEnsure the generated SQL is valid for DuckDB.\n\n**Database Schema:**\n| database              | schema   | name      | column_names                                                               | column_types                                                          | temporary   |\n|:----------------------|:---------|:----------|:---------------------------------------------------------------------------|:----------------------------------------------------------------------|:------------|\n| synthetic_openflights | main     | airlines  | ['airline_id' 'name' 'alias' 'iata' 'icao' 'callsign' 'country' 'active']  | ['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' | False       |\n|                       |          |           |                                                                            |  'VARCHAR']                                                           |             |\n| synthetic_openflights | main     | airports  | ['airport_id' 'name' 'city' 'country' 'iata' 'icao' 'latitude' 'longitude' | ['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'DOUBLE'  | False       |\n|                       |          |           |  'altitude' 'timezone' 'dst' 'tz_db' 'type' 'source']                      |  'DOUBLE' 'BIGINT' 'DOUBLE' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR']  |             |\n| synthetic_openflights | main     | countries | ['name' 'iso_code' 'dafif_code']                                           | ['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False       |\n| synthetic_openflights | main     | planes    | ['name' 'iata' 'icao']                                                     | ['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False       |\n| synthetic_openflights | main     | routes    | ['airline' 'airline_id' 'source_airport' 'source_airport_id'               | ['VARCHAR' 'BIGINT' 'VARCHAR' 'BIGINT' 'VARCHAR' 'BIGINT' 'VARCHAR'   | False       |\n|                       |          |           |  'destination_airport' 'destination_airport_id' 'codeshare' 'stops'        |  'BIGINT' 'VARCHAR']                                                  |             |\n|                       |          |           |  'equipment']                                                              |                                                                       |             |"}, {'role': 'user', 'content': 'Which active airlines in India have the most routes, and how many routes does each operate?'}, {'role': 'assistant', 'content': "SELECT a.name AS airline_name, COUNT(r.airline_id) AS route_count FROM airlines a JOIN routes r ON a.airline_id = r.airline_id WHERE a.active = 'Y' AND a.country = 'India' GROUP BY a.name ORDER BY route_count DESC, airline_name"}], 'ground_truth': [{'airline_name': 'Alliance Air', 'route_count': 50}, {'airline_name': 'IndiGo Airlines', 'route_count': 50}, {'airline_name': 'Air India', 'route_count': 29}, {'airline_name': 'Crimson Air', 'route_count': 1}, {'airline_name': 'SkyLark Airways', 'route_count': 1}]}
    
    ====================
    LLM QUERY GENERATION
    ====================
    User prompt: Which active airlines in India have the most routes, and how many routes does each operate?
    Ground truth: [{'airline_name': 'Alliance Air', 'route_count': 50}, {'airline_name': 'IndiGo Airlines', 'route_count': 50}, {'airline_name': 'Air India', 'route_count': 29}, {'airline_name': 'Crimson Air', 'route_count': 1}, {'airline_name': 'SkyLark Airways', 'route_count': 1}]
    Calling model 'accounts/fireworks/models/llama-v3p1-8b-instruct' to generate SQL query...
    
    Model Generated SQL Query:
    SELECT T1.name, COUNT(T2.airline_id) FROM airlines AS T1 INNER JOIN routes AS T2 ON T1.airline_id = T2.airline_id WHERE T1.country = 'India' AND T1.active = 1 GROUP BY T1.name ORDER BY COUNT(T2.airline_id) DESC LIMIT 1
    
    ====================
    MCP SERVER EXECUTION
    ====================
    Sending query to MCP server...
    
    Parsed Result from Server:
    [
      {}
    ]
    
    ====================
    COMPARISON
    ====================
    
    ❌ BAD RESULT: The base model's SQL produced different data than expected.
    
    This is often the intended outcome when testing a base model, as it highlights what fine-tuning needs to correct.
```

### 14. 🚀 Launch the Fine-Tuning Job & Deploy via the UI

Now we'll use the Fireworks AI web interface to take our prepared dataset and fine-tune a model. This process uses your custom `evaluate` function to teach a base model how to generate SQL correctly.

#### RFT vs Traditional Fine-Tuning:

Traditional supervised fine-tuning (SFT) would:

* Require thousands of examples
* Teach the model to mimic exact SQL syntax
* Often overfit to specific query patterns

Reinforcement fine-tuning (RFT) instead:

* Works with just hundreds of examples
* Rewards correct results regardless of SQL syntax
* Discovers novel solutions through exploration
* Generalizes better to unseen queries

>   **Real World 🌍**\
> This is the core of the RFT process. You're teaching a general-purpose model a very specific and valuable new skill using a powerful, UI-driven workflow. You may follow along as described below

As described in the [Fireworks RFT documentation](https://fireworks.ai/docs/fine-tuning/reinforcement-fine-tuning-models), the process involves uploading your data, creating an evaluator, running the job, and deploying.

**14. a) Upload Your Dataset**

1. Navigate to the **Datasets** tab in your [https://app.fireworks.ai](https://app.fireworks.ai) dashboard.
2. Click **"Create Dataset"**.
3. Upload your training file: `data/final_rft_sql_train_data.jsonl`.
4. Give it a memorable name, like `rft-sql-train-data-v1`, and save it.

**14. b) Create the Evaluator**

1. Navigate to the **Evaluations** tab in the dashboard.
2. Click **"Create Evaluator"**. This will open the web IDE.
3. In the editor on the left, replace the template code with your full `evaluate` function from step 12 above. This function already contains the logic to connect to your MCP server and compare the results. You just need to add your MCP server URL to the MCP\_SERVER\_URL line.
4. Save the evaluator with a name like `rft-sql-mcp-evaluator-v1`.

**14. c) Launch the Fine-Tuning Job**

1. Navigate to the **Fine-Tuning** tab.
2. Click **"Fine-Tune a Model"** and select **Reinforcement**.
3. Configure the job:
   * **Model Selection:** Select a model, for example `qwen2p5-7b` (may appear as `Qwen2.5 7B`).
   * **Dataset:** Select the `rft-sql-train-data-v1` you uploaded.
   * **Evaluator:** Select the `rft-sql-mcp-evaluator-v1` you just created.
   * **Rollout:** You can leave these as the default values.
   * **Optional Settings:** You can leave the Model Output Name blank and get the default name, or enter a name of your choosing.
4. You can leave most other hyperparameters as their defaults, though fine-tuning for 32 epochs (i.e., setting `Epochs` to `32`) is recommended due to the complexity of the task.
5. Click **"Create Job"**.

**14. d) Monitor and Deploy**

1. You can monitor the progress of your job in the **Fine-Tuning** tab. In this example, we trained for 32 epochs and got the following plot:
   <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a407b8e0dc88181a2678bdf61e9f2444" alt="RFT Training Progress" data-og-width="1648" width="1648" data-og-height="914" height="914" data-path="examples/assets/rft-sql-training.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a0af5936493d30c7473f711e1a59bbf3 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=c90f2795e9228b5cd26c1cab1eb7ed5f 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=09bdbb68073d786de76a20b9fec7cd81 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3142e20c4ed6d362cc29965d5942ef91 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=87e9ee35eb86cc472c353d5955fec1b8 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=af04ad9f047bf0e100ab8aaafaddd72f 2500w" />
2. Once the job status is `Completed`, you can deploy your model. To deploy, click "Deploy" on the top right of your fine-tuning job's page and then "Deploy LoRA Model". Please note:
   * The Model under "Select base model\*" should be the one from your Reinforcement Fine-Tuning job (this should be populated automatically)
   * Speculative decoding is an advanced technique that can improve latency, but is not needed for this use-case
   * Feel free to make the other selections (Performance, Scaling, and Metadata) as needed; enabling autoscaling is recommended to reduce costs
3. Find this new model and click the **Deploy** button to create an API endpoint.

**14. e) Test Your New Model!**
Once deployed, copy your new model's ID and paste it into the `LLM_MODEL` variable in the testing cell (step #13) to make sure it works as expected, along with your MCP server URL (i.e., `LLM_MODEL = "accounts/<your-account-id>/models/<your-model-id>"` and `MCP_SERVER_URL = "<your-mcp-server-url>"`).

### 15. ⚖️ Evaluate Model Performance

Now for the moment of truth. We will systematically compare the performance of the original base model against our newly fine-tuned model, as well as a much larger base model, to quantify the improvement and general accuracy.

We'll run both models against every entry in our test dataset (final\_rft\_sql\_test\_data.jsonl). For each entry, we will:

1. Provide the same system and user prompt to both the base model and the fine-tuned model.
2. Capture the SQL query generated by each.
3. Execute each query against our live MCP server.
4. Compare the query result to the ground\_truth from our dataset.
5. Keep a running score for each model.

This process will give us a clear, data-driven view of how much more accurate our model became after reinforcement fine-tuning.

>   **Real World 🌍**
> This is a critical step in any MLOps loop. Evaluating a model on a consistent test set is the only way to prove that your efforts have resulted in a tangible improvement. In production, you'd also want to:
>
>   * Track latency and cost metrics
>   * Monitor for drift over time
>   * A/B test against your current solution
>   * Collect user feedback on query quality
```python
import requests
import json
import os
import time
from fireworks import LLM
from tqdm.auto import tqdm
from dotenv import load_dotenv

load_dotenv()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
