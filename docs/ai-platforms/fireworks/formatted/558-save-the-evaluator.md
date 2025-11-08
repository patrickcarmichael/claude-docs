---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Save the evaluator

rft_evaluator_filename = "kd-rft-evaluator.py"
with open(rft_evaluator_filename, 'w') as f:
    f.write(rft_evaluator_code)
```

### Setting Up RFT Training (Manual Dashboard Configuration)

Due to the complexity of reinforcement learning setup, we'll use the Fireworks dashboard for the final configuration steps.

#### Step 1: Upload the RFT Evaluator

1. **Navigate to Evaluators**
   * Go to [https://app.fireworks.ai/dashboard/evaluations](https://app.fireworks.ai/dashboard/evaluations)

2. **Create New Evaluator**
   * Click **"Create Evaluator"**
   * **Evaluator Name**: `kd-rft-evaluator`

3. **Configure Dataset**
   * Select **"Select an existing dataset"**
   * Choose the `kd-rft-dataset` you uploaded earlier

4. **Add Evaluator Code**
   * Choose **"Start from scratch"**
   * Click **"Next"**
   * In the code editor, delete any existing code
   * Copy and paste the complete code from `kd-rft-evaluator.py`

5. **Save Evaluator**
   * Click **"Save Evaluator"**
   * Your evaluator is now ready for RFT training

#### Step 2: Create RFT Training Job

1. **Navigate to Fine-Tuning**
   * Go to the **Fine-Tuning** tab in the dashboard
   * Click **"Fine-Tune a Model"**
   * Select **"Reinforcement"** tab

2. **Configure Training Job**

   **Model Selection:**

   * Select your SFT-trained model
   * Use `job.output_model` from your SFT job to obtain SFT model name (e.g., `accounts/your-account/models/kd-sft-model`)

   **Dataset:**

   * Select `kd-rft-dataset` from the dropdown

   **Evaluator:**

   * Select `kd-rft-evaluator` (the one you just created)

   **Training Settings:**

   * **Rollout Settings**: Leave as default values
   * **Model Output Name**:
     * Option 1: Leave blank for auto-generated name
     * Option 2: Enter custom name (e.g., `kd-rft-model`)
   * **Other Hyperparameters**: Leave as defaults

3. **Launch Training**
   * Review your configuration
   * Click **"Create Job"**
   * **Important**: Note the output model name for evaluation later

4. **Monitoring**

* Track progress in the dashboard's [Fine Tuning section](https://app.fireworks.ai/dashboard/fine-tuning).
* Once the job status is `Completed`, you can deploy your model.

### Deploying the Fine-Tuned Model

```python
rft_llm = LLM(
    model="<rft-model-output-name>", # Replace <rft-model-output-name> with the model ID from your completed fine-tuning job

    deployment_type="on-demand",
    id="kd-rft-model",
    min_replica_count=0,
    max_replica_count=1
)
rft_llm.apply()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
