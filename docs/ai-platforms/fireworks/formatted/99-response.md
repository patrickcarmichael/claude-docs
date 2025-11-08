---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response

<Tabs>
  <Tab title="application/json">
    <ResponseField name="id" type="string" required>
      The unique identifier for the image generation request.
    </ResponseField>

    <ResponseField name="base64" type="string" required>
      Includes a base64-encoded string containing an image in PNG format.
      To retrieve the image, base64-decode the string into binary data,
      then load that binary data as a PNG file.
    </ResponseField>

    <ResponseField name="finishReason" type="string" required>
      Can be `SUCCESS` or `CONTENT_FILTERED`.

      Specifies the outcome of the image generation process. It could be
      `SUCCESS` indicating that the image was successfully generated, or
      `CONTENT_FILTERED` if the image was filtered due to the safety\_check=true
      parameter being set.
    </ResponseField>

    <ResponseField name="seed" type="integer" required>
      The seed used for the image generation process.
    </ResponseField>
  </Tab>

  <Tab title="image/jpeg">
    When the Accept type is `image/jpeg`, the response body will contain a binary image. Additionally, the response will include headers such as:

    **Content-Length:** Represents the length of the binary image content.

    **Seed:** The random seed used to generate the image.

    **Finish-Reason:** Indicates the outcome of the image generation, such as `CONTENT_FILTERED` or `SUCCESS`.
  </Tab>

  <Tab title="image/png">
    When the Accept type is `image/png`, the response body will contain a binary image. Additionally, the response will include headers such as:

    **Content-Length:** Represents the length of the binary image content.

    **Seed:** The random seed used to generate the image.

    **Finish-Reason:** Indicates the outcome of the image generation, such as `CONTENT_FILTERED` or `SUCCESS`.
  </Tab>
</Tabs>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
