---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the model

model="c4ai-aya-vision-32b"

def generate_text(image_path, message):
    """
    Generate text responses from Aya Vision model based on an image and text prompt.

    Args:
        image_path (str): Path to the image file
        message (str): Text prompt to send with the image

    Returns:
        None: Prints the model's response
    """

    # Define an image in Base64-encoded format

    with open(image_path, "rb") as img_file:
        base64_image_url = f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

    # Make an API call to the Cohere Chat endpoint, passing the user message and image

    response = co.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": message},
                    {"type": "image_url", "image_url": {"url": base64_image_url}},
                ],
            }
        ],
    )

    # Print the response

    print(response.message.content[0].text)
```
Let's also set up a function to render images on this notebook as we go through the use cases.

Note: the images used in this notebook can be downloaded [here](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/images/aya-vision)
```python PYTHON
from IPython.display import Image, display

def render_image(image_path):
    """
    Display an image in the notebook with a fixed width.

    Args:
        image_path (str): Path to the image file to display
    """
    display(Image(filename=image_path, width=400))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
