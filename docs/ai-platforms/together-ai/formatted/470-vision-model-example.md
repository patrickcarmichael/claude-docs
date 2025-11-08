---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Vision model example

Let's look at another example, this time using a vision model.

We want our LLM to extract text from the following screenshot of a Trello board:

![Trello board](https://files.readme.io/4512824ce58b18d946c8a8c786a21a5346e18e8b1860fc03de07d69a0145450e-image.png)

In particular, we want to know the name of the project (Project A), and the number of columns in the board (4).

Let's try it out:
```py
  import json
  import together
  from pydantic import BaseModel, Field

  client = together.Together()


  ## Define the schema for the output

  class ImageDescription(BaseModel):
      project_name: str = Field(
          description="The name of the project shown in the image"
      )
      col_num: int = Field(description="The number of columns in the board")


  def main():
      imageUrl = "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png"

      # Call the LLM with the JSON schema

      extract = client.chat.completions.create(
          messages=[
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text",
                          "text": "Extract a JSON object from the image.",
                      },
                      {
                          "type": "image_url",
                          "image_url": {
                              "url": imageUrl,
                          },
                      },
                  ],
              },
          ],
          model="Qwen/Qwen2.5-VL-72B-Instruct",
          response_format={
              "type": "json_schema",
              "schema": ImageDescription.model_json_schema(),
          },
      )

      output = json.loads(extract.choices[0].message.content)
      print(json.dumps(output, indent=2))
      return output


  main()
```
```typescript
  import Together from "together-ai";
  import { z } from "zod";
  import { zodToJsonSchema } from "zod-to-json-schema";

  const together = new Together();

  // Define the shape of our data
  const schema = z.object({
    projectName: z
      .string()
      .describe("The name of the project shown in the image"),
    columnCount: z.number().describe("The number of columns in the board"),
  });
  const jsonSchema = zodToJsonSchema(schema, { target: "openAi" });

  const imageUrl =
    "https://napkinsdev.s3.us-east-1.amazonaws.com/next-s3-uploads/d96a3145-472d-423a-8b79-bca3ad7978dd/trello-board.png";

  async function main() {
    const extract = await together.chat.completions.create({
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "Extract a JSON object from the image." },
            {
              type: "image_url",
              image_url: { url: imageUrl },
            },
          ],
        },
      ],
      model: "Qwen/Qwen2.5-VL-72B-Instruct",
      response_format: {
        type: "json_object",
        schema: jsonSchema,
      },
    });

    if (extract?.choices?.[0]?.message?.content) {
      const output = JSON.parse(extract?.choices?.[0]?.message?.content);
      console.log(output);
      return output;
    }
    return "No output.";
  }

  main();
```

If we run it, we get the following output:
```json
{
  "projectName": "Project A",
  "columnCount": 4
}
```

JSON mode has worked perfectly alongside Qwen's vision model to help us extract structured text from an image!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
