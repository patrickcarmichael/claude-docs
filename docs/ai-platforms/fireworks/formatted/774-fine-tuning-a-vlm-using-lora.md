---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fine-tuning a VLM using LoRA

<Steps>
  <Step title="Prepare your vision dataset">
    vision datasets must be in JSONL format in OpenAI-compatible chat format.
    Each line represents a complete training example.

    **Dataset Requirements:**

    * **Format**: `.jsonl` file
    * **Minimum examples**: 3
    * **Maximum examples**: 3 million per dataset
    * **Images**: Must be base64 encoded with proper MIME type prefixes
    * **Supported image formats**: PNG, JPG, JPEG

    **Message Schema:**
    Each training example must include a `messages` array where each message has:

    * `role`: one of `system`, `user`, or `assistant`
    * `content`: an array containing text and image objects or just text

    ### Basic VLM Dataset Example

```json
    {
      "messages": [
        {
          "role": "system",
          "content": "You are a helpful visual assistant that can analyze images and answer questions about them."
        },
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What objects do you see in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
              }
            }
          ]
        },
        {
          "role": "assistant",
          "content": "I can see a red car, a tree, and a blue house in this image."
        }
      ]
    }
```
    ### If your dataset contains image urls

    Images must be base64 encoded with MIME type prefixes. If your dataset contains image URLs, you'll need to download and encode them to base64.

    <Tabs>
      <Tab title="❌ Incorrect">
```json
        {
          "type": "image_url",
          "image_url": {
            // ❌ Raw HTTP/HTTPS URLs are NOT supported
            "url": "https://example.com/image.jpg"
          }
        }
```
      </Tab>

      <Tab title="✅ Correct">
```json
        {
          "type": "image_url",
          "image_url": {
            // ✅ Use data URI with base64 encoding
            // Format: data:image/{format};base64,{base64_encoded_data}
            "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
          }
        }
```
      </Tab>
    </Tabs>

    You can use the following script to automatically convert your dataset to the correct format:

    <AccordionGroup>
      <Accordion title="Python script to download and encode images to base64">
        **Usage:**
```bash
        # Install required dependency

        pip install requests

        # Download the script

        wget https://raw.githubusercontent.com/fw-ai/cookbook/refs/heads/main/learn/vlm-finetuning/utils/download_images_and_encode_to_b64.py

        # Run the script - will output a new dataset <path_to_your_dataset>_base64.jsonl

        python download_images_and_encode_to_b64.py --input_file <path_to_your_dataset.jsonl>
```
      </Accordion>
    </AccordionGroup>

    ### Advanced Dataset Examples

    <Tabs>
      <Tab title="Multi-image Conversation">
```json
        {
          "messages": [
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Compare these two images and tell me the differences"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
                  }
                },
                {
                  "type": "image_url", 
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4BBBSkZJRg..."
                  }
                }
              ]
            },
            {
              "role": "assistant",
              "content": "The first image shows a daytime scene while the second shows the same location at night. The lighting and shadows are completely different."
            }
          ]
        }
```
      </Tab>

      <Tab title="Multi-turn Conversation">
```json
        {
          "messages": [
            {
              "role": "system",
              "content": "You are a helpful visual assistant that can analyze images and remember details from previous images in our conversation."
            },
            {
              "role": "user", 
              "content": [
                {
                  "type": "text",
                  "text": "Can you describe this kitchen layout for me?"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQ..."
                  }
                }
              ]
            },
            {
              "role": "assistant",
              "content": "This is a modern open-plan kitchen with white cabinets, granite countertops, and stainless steel appliances. The island is positioned in the center with bar seating for 3-4 people. There's a large window above the sink providing natural light."
            },
            {
              "role": "user",
              "content": "Now look at this living room. Do you think the styles would work well together?"
            },
            {
              "role": "assistant", 
              "content": "I'd be happy to help compare the styles! However, I don't see a living room image in your message. Could you please share the living room photo so I can analyze how well it would coordinate with the modern kitchen style we just discussed?"
            },
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "Sorry about that! Here's the living room:"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/jpeg;base64,/9j/4BBBSkZJRgABAQ..."
                  }
                }
              ]
            },
            {
              "role": "assistant",
              "content": "Perfect! This living room has a complementary modern aesthetic that would work beautifully with the kitchen. Both spaces feature clean lines and a neutral color palette. The living room's contemporary furniture and the kitchen's sleek design would create a cohesive flow in an open floor plan. The warm wood accents in the living room would add nice contrast to the kitchen's cooler tones."
            },
          ]
        }
```
      </Tab>
    </Tabs>

    ### Try with an Example Dataset

    To get a feel for how VLM fine-tuning works, you can use an example vision dataset. This is a classification dataset that contains images of food with `<think></think>` tags for reasoning.

    <Tabs>
      <Tab title="Download with curl">
```bash
        # Download the example dataset

        curl -L -o food_reasoning.jsonl https://huggingface.co/datasets/fireworks-ai/vision-food-reasoning-dataset/resolve/main/food_reasoning.jsonl
```
      </Tab>

      <Tab title="Download with wget">
```bash
        # Download the example dataset  

        wget https://huggingface.co/datasets/fireworks-ai/vision-food-reasoning-dataset/resolve/main/food_reasoning.jsonl
```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Upload your VLM dataset">
    Upload your prepared JSONL dataset to Fireworks for training:

    <Tabs>
      <Tab title="firectl">
```bash
        firectl create dataset my-vlm-dataset /path/to/vlm_training_data.jsonl
```
      </Tab>

      <Tab title="UI">
        Navigate to the Datasets tab in the Fireworks console, click "Create Dataset", and upload your JSONL file through the wizard.

        <Frame>
          <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=33255bb2d9afefc697230a6f4e723577" alt="Dataset creation interface" data-og-width="2972" width="2972" data-og-height="2060" height="2060" data-path="images/fine-tuning/dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=e1f7631eedf19be2ffe910e931734378 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5148e67713f7a207c47a73da1fa56658 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=dde9343748034e1d13ae4fbc1ad4aecf 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a4a99ce824157064f5cbbdfdf0953c0d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=699fd69866de9383a06dc08a5139cb69 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b55ed77bc807c1ebf00223fff2997342 2500w" />
        </Frame>
      </Tab>

      <Tab title="REST API">
```javascript
        // Create dataset entry
        const createDatasetPayload = {
          datasetId: "my-vlm-dataset",
          dataset: { userUploaded: {} }
        };

        const response = await fetch(`${BASE_URL}/datasets`, {
          method: "POST",
          headers: { 
            "Authorization": `Bearer ${API_KEY}`,
            "Content-Type": "application/json"
          },
          body: JSON.stringify(createDatasetPayload)
        });

        // Upload JSONL file
        const formData = new FormData();
        formData.append("file", fileInput.files[0]);

        const uploadResponse = await fetch(`${BASE_URL}/datasets/my-vlm-dataset:upload`, {
          method: "POST",
          headers: { "Authorization": `Bearer ${API_KEY}` },
          body: formData
        });
```
      </Tab>
    </Tabs>

    <Tip>
      For larger datasets (>500MB), use `firectl` as it handles large uploads more reliably than the web interface. For enhanced data control and security, we also support bring your own bucket (BYOB) configurations. See our [Secure Fine Tuning](/fine-tuning/secure-fine-tuning#gcs-bucket-integration) guide for setup details.
    </Tip>
  </Step>

  <Step title="Launch VLM fine-tuning job">
    Create a supervised fine-tuning job for your VLM:

    <Tabs>
      <Tab title="firectl">
```bash
        firectl create sftj \
          --base-model accounts/fireworks/models/qwen2p5-vl-32b-instruct \
          --dataset my-vlm-dataset \
          --output-model my-custom-vlm \
          --epochs 3
```
        For additional parameters like learning rates, evaluation datasets, and batch sizes, see [Additional SFT job settings](/fine-tuning/fine-tuning-models#additional-sft-job-settings).
      </Tab>

      <Tab title="UI">
        1. Navigate to the Fine-tuning tab in the Fireworks console
        2. Click "Create Fine-tuning Job"
        3. Select your VLM base model (Qwen 2.5 VL)
        4. Choose your uploaded dataset
        5. Configure training parameters
        6. Launch the job

        <Frame>
          <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=102b729d2d50fd9466d3b36606992443" alt="Fine-tuning job creation interface" data-og-width="2970" width="2970" data-og-height="2048" height="2048" data-path="images/fine-tuning/create-sftj.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=eabe188f029777c24abd5c3d9787c1da 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5fd4390ff45d3412c1b0cc687392d054 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=add5687145f89362ce42a171136b2639 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d074f5e4c69f9fed3644d9cdd637570d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d4830964471e8e7450fcbfad39a54269 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=2635d10a906f4c5b75899f41e8f1bf6c 2500w" />
        </Frame>
      </Tab>
    </Tabs>

    VLM fine-tuning jobs typically take longer than text-only models due to the additional image processing. Expect training times of several hours depending on dataset size and model complexity.
  </Step>

  <Step title="Monitor training progress">
    Track your VLM fine-tuning job in the [Fireworks console](https://app.fireworks.ai/dashboard/fine-tuning).

    <Frame>
      <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=2aa1e7f17fc8c070d52158a47f060300" alt="VLM fine-tuning job in the Fireworks console" data-og-width="3802" width="3802" data-og-height="1690" height="1690" data-path="images/fine-tuning/vlm-sftj.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4a0a7cc3b9a1f15dfa529cbc7cb3fc7d 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=be9b10f14100644e5bacf2d1320f07a1 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=c30a34029e337362fd1b68ab9e284af8 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=7aca6caa6584382211c2a956d5e57b02 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=eeed5ba8c2e92be97029fd43c3a3597c 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=e83d0ba476e94812a27f81105b36f1d9 2500w" />
    </Frame>

    Monitor key metrics:

    * **Training loss**: Should generally decrease over time
    * **Evaluation loss**: Monitor for overfitting if using evaluation dataset
    * **Training progress**: Epochs completed and estimated time remaining

    <Check>
      Your VLM fine-tuning job is complete when the status shows `COMPLETED` and your custom model is ready for deployment.
    </Check>
  </Step>

  <Step title="Deploy your fine-tuned VLM">
    Once training is complete, deploy your custom VLM:

    <Tabs>
      <Tab title="firectl">
```bash
        # Create a deployment for your fine-tuned VLM

        firectl create deployment my-custom-vlm

        # Check deployment status

        firectl get deployment accounts/your-account/deployment/deployment-id
```
      </Tab>

      <Tab title="UI">
        Deploy from the UI using the `Deploy` dropdown in the fine-tuning job page.

        <Frame>
          <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=896e4e94621b9eeb8a6207b1f4ba2e08" alt="Deploy dropdown in the fine-tuning job page" data-og-width="3802" width="3802" data-og-height="1690" height="1690" data-path="images/fine-tuning/vlm-sftj-deploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a31edefdaa851b15a5e1386fcecbbbe4 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=7376dcfadaa71f950e72a6d61f93d6a4 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ecaae0f37a36a03da0e664b2caf49505 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=c3bb4ed6bdfd7f1334948ba410c32be1 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=f8cb54c40529e395e5b2bf7ae1daf01b 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/vlm-sftj-deploy.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=f195e66cab9bfde9a9ff756115f57772 2500w" />
        </Frame>
      </Tab>
    </Tabs>
  </Step>
</Steps>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
