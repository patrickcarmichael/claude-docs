---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

<AccordionGroup>
  <Accordion title="1. Prepare Your Dataset">
    Datasets must be in JSONL format (one JSON object per line):

    **Requirements:**

    * **File format:** JSONL (each line is a valid JSON object)
    * **Size limit:** Under 500MB
    * **Required fields:** `custom_id` (unique) and `body` (request parameters)

    **Example dataset:**
```json
    {"custom_id": "request-1", "body": {"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of France?"}], "max_tokens": 100}}
    {"custom_id": "request-2", "body": {"messages": [{"role": "user", "content": "Explain quantum computing"}], "temperature": 0.7}}
    {"custom_id": "request-3", "body": {"messages": [{"role": "user", "content": "Tell me a joke"}]}}
```
    Save as `batch_input_data.jsonl` locally.
  </Accordion>

  <Accordion title="2. Upload Your Dataset">
    <Tabs>
      <Tab title="UI">
        You can simply navigate to the dataset tab, click `Create Dataset` and follow the wizard.

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=33255bb2d9afefc697230a6f4e723577" alt="Dataset Upload" data-og-width="2972" width="2972" data-og-height="2060" height="2060" data-path="images/fine-tuning/dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=e1f7631eedf19be2ffe910e931734378 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5148e67713f7a207c47a73da1fa56658 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=dde9343748034e1d13ae4fbc1ad4aecf 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a4a99ce824157064f5cbbdfdf0953c0d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=699fd69866de9383a06dc08a5139cb69 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b55ed77bc807c1ebf00223fff2997342 2500w" />
      </Tab>

      <Tab title="firectl">
```bash
        firectl create dataset batch-input-dataset ./batch_input_data.jsonl
```
      </Tab>

      <Tab title="HTTP API">
        You need to make two separate HTTP requests. One for creating the dataset entry and one for uploading the dataset. Full reference here: [Create dataset](/api-reference/create-dataset).
```bash
        # Create Dataset Entry

        curl -X POST "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/datasets" \
          -H "Authorization: Bearer ${API_KEY}" \
          -H "Content-Type: application/json" \
          -d '{
            "datasetId": "batch-input-dataset",
            "dataset": { "userUploaded": {} }
          }'

        # Upload JSONL file

        curl -X POST "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/datasets/batch-input-dataset:upload" \
          -H "Authorization: Bearer ${API_KEY}" \
          -F "file=@./batch_input_data.jsonl"
```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="3. Create a Batch Job">
    <Tabs>
      <Tab title="UI">
        Navigate to the Batch Inference tab and click "Create Batch Inference Job". Select your input dataset:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=c74141b465db64bd4ca3c037d20b3f30" alt="BIJ Dataset Select" data-og-width="3840" width="3840" data-og-height="1982" height="1982" data-path="images/batch-inference/BIJ_Dataset_Select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ad3decfc23ff03325cc141ddb0bc3853 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4f8af4b1fb7736f614229eb4ba19bc71 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=cfe1d39030f0c62956bfc194464b181e 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3e45d9a631ed269bfc65976050127e75 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=df78513dac5d93ff6e316ac501662309 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=6581fe37392ca0df9907f1aaa57861f7 2500w" />

        Choose your model:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=384fe513029928f248d751e58e2f89b9" alt="BIJ Model Select" data-og-width="3840" width="3840" data-og-height="1970" height="1970" data-path="images/batch-inference/BIJ_Model_Select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d902f47c06ab6a6fa1aeb6df721ba1ab 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ce98f4d224a1485b4e600e08c860f947 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=1115f215e13cae034bc16a8f85f89316 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=fc380420be1ae9e6bbacb80bbd1bf810 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4675a8e7e3bdb523f68c177bcfde4347 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=fabe3dd83aa7daf1c161cdc754d09782 2500w" />

        Configure optional settings:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=56179acd8c88d94143fda4b78c5cec2a" alt="BIJ Optional Settings" data-og-width="3840" width="3840" data-og-height="1976" height="1976" data-path="images/batch-inference/BIJ_Optional_Settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b3b8500e3b62e3314a289cf9fdd2a4b5 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=9f7870d2799cfdc8f83eb86d490e6192 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=23086532b59056a622bb03b4d13b7512 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=8000e1cacdf5dff70f4a18ebffb5b3b8 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=6564c2703f112beb51da20d1f5f95b5d 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=7fd4dd8043ac01bd8efe3af0552e6cb0 2500w" />
      </Tab>

      <Tab title="firectl">
```bash
        firectl create batch-inference-job \
          --model accounts/fireworks/models/llama-v3p1-8b-instruct \
          --input-dataset-id batch-input-dataset
```
        With additional parameters:
```bash
        firectl create batch-inference-job \
          --job-id my-batch-job \
          --model accounts/fireworks/models/llama-v3p1-8b-instruct \
          --input-dataset-id batch-input-dataset \
          --output-dataset-id batch-output-dataset \
          --max-tokens 1024 \
          --temperature 0.7 \
          --top-p 0.9
```
      </Tab>

      <Tab title="HTTP API">
```bash
        curl -X POST "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/batchInferenceJobs?batchInferenceJobId=my-batch-job" \
          -H "Authorization: Bearer ${API_KEY}" \
          -H "Content-Type: application/json" \
          -d '{
            "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
            "inputDatasetId": "accounts/'${ACCOUNT_ID}'/datasets/batch-input-dataset",
            "outputDatasetId": "accounts/'${ACCOUNT_ID}'/datasets/batch-output-dataset",
            "inferenceParameters": {
              "maxTokens": 1024,
              "temperature": 0.7,
              "topP": 0.9
            }
          }'
```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="4. Monitor Your Job">
    <Tabs>
      <Tab title="UI">
        View all your batch inference jobs in the dashboard:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=523de401343695e5db041c42b36364ea" alt="BIJ List" data-og-width="3840" width="3840" data-og-height="1986" height="1986" data-path="images/batch-inference/BIJ_List.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5eb7409172fe41f7d8fdf472f673e5bc 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a6b3851347a0302d1942ccc20a01cd48 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=991bee935ffeeae9f177de6d016ee2c8 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=146cf5029a45bf2cf9c140aa5e56c7c5 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4909a6d11d5927d83d6d5a7062d35c54 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=8d54557cf79cdc8aca7d7eb27078b748 2500w" />
      </Tab>

      <Tab title="firectl">
```bash
        # Get job status

        firectl get batch-inference-job my-batch-job

        # List all batch jobs

        firectl list batch-inference-jobs
```
      </Tab>

      <Tab title="HTTP API">
```bash
        # Get specific job

        curl -X GET "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/batchInferenceJobs/my-batch-job" \
          -H "Authorization: Bearer ${API_KEY}"

        # List all jobs

        curl -X GET "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/batchInferenceJobs" \
          -H "Authorization: Bearer ${API_KEY}"
```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="5. Download Results">
    <Tabs>
      <Tab title="UI">
        Navigate to the output dataset and download the results:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=af22b69efced8a70bcac70fecdf38ba8" alt="BIJ Dataset Download" data-og-width="3840" width="3840" data-og-height="1976" height="1976" data-path="images/batch-inference/BIJ_Dataset_Download.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=770f031bb6313b77cf2abcbc3f7684de 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3353ebde5f51bc348170c4d6cb1ee75f 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4180e89050342a2848db0a0670de2b35 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=64b7c055d37652271e6cda3da3fc4ccb 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ec7edc0a8e862d839f881df18c5eaf18 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4db728381845bb89bbc98258bd7f2449 2500w" />
      </Tab>

      <Tab title="firectl">
```bash
        firectl download dataset batch-output-dataset
```
      </Tab>

      <Tab title="HTTP API">
```bash
        # Get download endpoint and save response

        curl -s -X GET "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/datasets/batch-output-dataset:getDownloadEndpoint" \
          -H "Authorization: Bearer ${API_KEY}" \
          -d '{}' > download.json

        # Extract and download all files

        jq -r '.filenameToSignedUrls | to_entries[] | "\(.key) \(.value)"' download.json | \
        while read -r object_path signed_url; do
            fname=$(basename "$object_path")
            echo "Downloading → $fname"
            curl -L -o "$fname" "$signed_url"
        done
```
      </Tab>
    </Tabs>

    <Tip>
      The output dataset contains two files: a **results file** (successful responses in JSONL format) and an **error file** (failed requests with debugging info).
    </Tip>
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
