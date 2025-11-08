---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Customize Your Evaluation Job

We support three evaluation types:

* **Classify** – Categorizes input into one of the provided categories
* **Score** – Evaluates input and produces a score within a specified range
* **Compare** – Compares responses from two models to determine which performs better according to given criteria

### Judge Configuration

The `judge` object contains two required fields:

* **judge model** – (string) The model used for evaluation
* **system template** – (Jinja template) Provides guidance for the judge to assess the data

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=743b1501300f81d64a5e894af26e1b60" alt="" data-og-width="1444" width="1444" data-og-height="612" height="612" data-path="images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=737e67d9f45af98fa6e3515574204955 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=69388fd95b9d0e4ef9d8273db499a308 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=eac9dda26f97f7168b00968cbd070cbe 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=55bd95040582f77a24ea60c4322bb5e9 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cda932a1db9dcf828e1ebef025001cf8 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/78697dc06e49b17bc554cb35e8ed18694bb6f8b8bab420658012a0409e6cd978-image.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=81d8508ab932f2b9970bd9d56c93cc75 2500w" />
</Frame>

### Model Configuration Parameters

#### Classify

* **labels** – (list of strings) Categories for input classification. For each category, you can specify whether it's considered 'pass' or 'fail' for statistics computation
* **model\_to\_evaluate** – Configuration for the model being evaluated

#### Score

* **min\_score** – (float) Minimum score the judge can assign
* **max\_score** – (float) Maximum score the judge can assign
* **model\_to\_evaluate** – Configuration for the model being evaluated

#### Compare

* Only requires judge setup and two model configurations for comparison

### Model Evaluation Configuration

Choose whether to evaluate existing data or generate new responses:

* **"Configure"** – Generate data using the model for evaluation
* **"Field name"** – Data required for evaluation is already present in your dataset

**Option 1: Model Object**\
Use when generating new responses for evaluation. The object requires:

* **model\_name** – (string) One of our supported models
* **system\_template** – (Jinja2 template) An instruction for generation, e.g., "You are a helpful assistant." (see [Understanding Templates](ai-evaluations#understanding-templates))
* **input\_template** – (Jinja2 template) Input format, e.g., `"{{prompt}}"` (see [Understanding Templates](ai-evaluations#understanding-templates))
* **max\_tokens** – (integer) Maximum tokens for generation
* **temperature** – (float) Temperature setting for generation

**Option 2: Column Reference (String)**\
Use when evaluating pre-existing data from your dataset. Simply specify the column name containing the data to evaluate.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=e2096024a7613749a53d9e30227d0a41" alt="" data-og-width="3198" width="3198" data-og-height="1448" height="1448" data-path="images/together-ai-evaluations-ui-model-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d54e96248608aa438aeebb5abe6d5fee 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=2f958bfe7f5fb112a81be6dc340fdae3 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8d73f99dc289304e777614cea486ecb2 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9e902cf6083499a4cf93bcbc9ab54dd2 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=30756869fb96066a8ac315f16120f505 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/together-ai-evaluations-ui-model-config.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1b4dd0a67e4b3699c7a8edfbebccca72 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
