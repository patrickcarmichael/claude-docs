---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quickstart

### 1. Register for an account

First, [register for an account](https://api.together.xyz/settings/api-keys) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:
```bash
export TOGETHER_API_KEY=xxxxx
```

### 2. Install your preferred library

Together provides an official library for Python:
```bash
pip install together
```
As well as an official library for TypeScript/JavaScript:
```bash
npm install together-ai
```
You can also call our HTTP API directly using any language you like.

### 3. Query the models via our API

In this example, we're giving it a picture of a trello board and asking the model to describe it to us.
```python
  from together import Together

  client = Together()

  getDescriptionPrompt = "You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail. Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly. Make sure to mention every part of the screenshot including any headers, footers, etc. Use the exact text from the screenshot."

  imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"

  stream = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": getDescriptionPrompt},
                  {"type": "image_url", "image_url": {"url": imageUrl}},
              ],
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  let getDescriptionPrompt = `You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail.

  - Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly.
  - Make sure to mention every part of the screenshot including any headers, footers, etc.
  - Use the exact text from the screenshot.
  `;
  let imageUrl =
    "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png";

  async function main() {
    const stream = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      temperature: 0.2,
      stream: true,
      max_tokens: 500,
      messages: [
        {
          role: "user",
          // @ts-expect-error Need to fix the TypeScript library type
          content: [
            { type: "text", text: getDescriptionPrompt },
            {
              type: "image_url",
              image_url: {
                url: imageUrl,
              },
            },
          ],
        },
      ],
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
  }

  main();
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
         "messages": [
           {
             "role": "user",
             "content": [
               {
                 "type": "text",
                 "text": "You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail. Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly. Make sure to mention every part of the screenshot including any headers, footers, etc. Use the exact text from the screenshot."
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"
                 }
               }
             ]
           }
         ]
       }'
```

#### Output

```
The attached screenshot appears to be a Trello board, a project management tool used for organizing tasks and projects into boards. Below is a detailed breakdown of the UI:

**Header**
-----------------

* A blue bar spanning the top of the page
* White text reading "Trello" in the top-left corner
* White text reading "Workspaces", "Recent", "Starred", "Templates", and "Create" in the top-right corner, separated by small white dots
* A white box with a blue triangle and the word "Board" inside it

**Top Navigation Bar**
----------------------

* A blue bar with white text reading "Project A"
* A dropdown menu with options "Workspace visible" and "Board"
* A search bar with a magnifying glass icon

**Main Content**
-----------------

* Three columns of cards with various tasks and projects
* Each column has a header with a title
* Cards are white with gray text and a blue border
* Each card has a checkbox, a title, and a description
* Some cards have additional details such as a yellow or green status indicator, a due date, and comments

**Footer**
------------

* A blue bar with white text reading "Add a card"
* A button to add a new card to the board

**Color Scheme**
-----------------

* Blue and white are the primary colors used in the UI
* Yellow and green are used as status indicators
* Gray is used for text and borders

**Font Family**
----------------

* The font family used throughout the UI is clean and modern, with a sans-serif font

**Iconography**
----------------

* The UI features several icons, including:
        + A magnifying glass icon for the search bar
        + A triangle icon for the "Board" dropdown menu
        + A checkbox icon for each card
        + A status indicator icon (yellow or green)
        + A comment icon (a speech bubble)

**Layout**
------------

* The UI is divided into three columns: "To Do", "In Progress", and "Done"
* Each column has a header with a title
* Cards are arranged in a vertical list within each column
* The cards are spaced evenly apart, with a small gap between each card

**Overall Design**
-------------------

* The UI is clean and modern, with a focus on simplicity and ease of use
* The use of blue and white creates a sense of calmness and professionalism
* The icons and graphics are simple and intuitive, making it easy to navigate the UI

This detailed breakdown provides a comprehensive understanding of the UI mockup, including its layout, color scheme, and components.
```

### Query models with a local image

If you want to query models with a local image, here is an example:
```python
  from together import Together
  import base64

  client = Together()

  getDescriptionPrompt = "what is in the image"

  imagePath = "/home/Desktop/dog.jpeg"


  def encode_image(image_path):
      with open(image_path, "rb") as image_file:
          return base64.b64encode(image_file.read()).decode("utf-8")


  base64_image = encode_image(imagePath)

  stream = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": getDescriptionPrompt},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": f"data:image/jpeg;base64,{base64_image}"
                      },
                  },
              ],
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(
          chunk.choices[0].delta.content or "" if chunk.choices else "",
          end="",
          flush=True,
      )
```
```typescript
  import Together from "together-ai";
  import fs from "fs/promises";

  const together = new Together();

  const getDescriptionPrompt = "what is in the image";

  const imagePath = "./dog.jpeg";

  async function main() {
    const imageUrl = await fs.readFile(imagePath, { encoding: "base64" });

    const stream = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      stream: true,
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: getDescriptionPrompt },
            {
              type: "image_url",
              image_url: {
                url: `data:image/jpeg;base64,${imageUrl}`,
              },
            },
          ],
        },
      ],
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
  }

  main();
```
```bash
  # Note: Replace BASE64_IMAGE with your base64-encoded image data

  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
         "messages": [
           {
             "role": "user",
             "content": [
               {
                 "type": "text",
                 "text": "what is in the image"
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "data:image/jpeg;base64,BASE64_IMAGE"
                 }
               }
             ]
           }
         ]
       }'
```

#### Output

```
The Image contains two dogs sitting close to each other
```

### Query models with video input

```python
  # Multi-modal message with text and video

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What's happening in this video?"},
                  {
                      "type": "video_url",
                      "video_url": {
                          "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  // Multi-modal message with text and video

  async function main() {
    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "What's happening in this video?" },
            {
              type: "video_url",
              video_url: {
                url: "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
              },
            },
          ],
        },
      ],
    });
    
    process.stdout.write(response.choices[0]?.message?.content || "");
  }

  main();
```

#### Output

```
The video appears to be a promotional advertisement for Google Chromecast. It showcases various scenes of people using the device in different settings, such as classrooms and offices. The video highlights the versatility and ease of use of Chromecast by demonstrating how it can be used to cast content from laptops and other devices onto larger screens like TVs or monitors. The final frame displays the Chromecast logo and website URL, indicating the product being advertised.
```

### Query models with multiple images

```python
  # Multi-modal message with multiple images

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Compare these two images."},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                      },
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  // Multi-modal message with multiple images

  async function main() {
    const response = await together.chat.completions.create({
      model: "meta-llama/Llama-4-Scout-17B-16E-Instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Compare these two images." },
            {
              type: "image_url",
              image_url: {
                url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png",
              },
            },
            {
              type: "image_url",
              image_url: {
                url: "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png",
              },
            },
          ],
        },
      ],
    });
    
    process.stdout.write(response.choices[0]?.message?.content || "");
  }

  main();
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "meta-llama/Llama-4-Scout-17B-16E-Instruct",
         "messages": [
           {
             "role": "user",
             "content": [
               {
                 "type": "text",
                 "text": "Compare these two images."
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/yosemite.png"
                 }
               },
               {
                 "type": "image_url",
                 "image_url": {
                   "url": "https://huggingface.co/datasets/patrickvonplaten/random_img/resolve/main/slack.png"
                 }
               }
             ]
           }
         ]
       }'
```

#### Output

```
The first image is a collage of multiple identical landscape photos showing a natural scene with rocks, trees, and a stream under a blue sky. The second image is a screenshot of a mobile app interface, specifically the navigation menu of the Canva app, which includes icons for Home, DMs (Direct Messages), Activity, Later, Canvases, and More.

#### Comparison:

1. **Content**:
   - The first image focuses on a natural landscape.
   - The second image shows a digital interface from an app.

2. **Purpose**:
   - The first image could be used for showcasing nature, design elements in graphic work, or as a background.
   - The second image represents the functionality and layout of the Canva app's navigation system.

3. **Visual Style**:
   - The first image has vibrant colors and realistic textures typical of outdoor photography.
   - The second image uses flat design icons with a simple color palette suited for user interface design.

4. **Context**:
   - The first image is likely intended for artistic or environmental contexts.
   - The second image is relevant to digital design and app usability discussions.
```

### Pricing

For vision models images are converted to 1,601 to 6,404 tokens depending on image size. We currently used this formula to calculate the number of tokens in an image:
```
T = min(2, max(H // 560, 1)) * min(2, max(W // 560, 1)) * 1601
```javascript
*(T= tokens, H=height, W=width)*


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
