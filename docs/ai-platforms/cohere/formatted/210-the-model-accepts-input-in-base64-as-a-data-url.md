---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The model accepts input in base64 as a Data URL


def image_to_base64_data_url(image_path):
    # Open the image file

    with Image.open(image_path) as img:
        # Create a BytesIO object to hold the image data in memory

        buffered = BytesIO()
        # Save the image as PNG to the BytesIO object

        img.save(buffered, format="PNG")
        # Encode the image data in base64

        img_base64 = base64.b64encode(buffered.getvalue()).decode(
            "utf-8"
        )

    # Create the Data URL and assumes the original image file type was png

    data_url = f"data:image/png;base64,{img_base64}"
    return data_url


processed_image = image_to_base64_data_url("<PATH_TO_IMAGE>")

res = co.embed(
    images=[processed_image],
    model="embed-v4.0",
    embedding_types=["float"],
    input_type="image",
)

res.embeddings.float
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
