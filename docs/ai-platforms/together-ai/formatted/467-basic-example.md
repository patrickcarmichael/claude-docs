---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic example

Let's look at a simple example, where we pass a transcript of a voice note to a model and ask it to summarize it.

We want the summary to have the following structure:
```json
{
  "title": "A title for the voice note",
  "summary": "A short one-sentence summary of the voice note",
  "actionItems": ["Action item 1", "Action item 2"]
}
```

We can tell our model to use this structure by giving it a [JSON Schema](https://json-schema.org/) definition. Since writing JSON Schema by hand is a bit tedious, we'll use a library to help – Pydantic in Python, and Zod in TypeScript.

Once we have the schema, we can include it in the system prompt and give it to our model using the `response_format` key.

Let's see what this looks like:
```py
  import json
  import together
  from pydantic import BaseModel, Field

  client = together.Together()


  ## Define the schema for the output

  class VoiceNote(BaseModel):
      title: str = Field(description="A title for the voice note")
      summary: str = Field(
          description="A short one sentence summary of the voice note."
      )
      actionItems: list[str] = Field(
          description="A list of action items from the voice note"
      )


  def main():
      transcript = (
          "Good morning! It's 7:00 AM, and I'm just waking up. Today is going to be a busy day, "
          "so let's get started. First, I need to make a quick breakfast. I think I'll have some "
          "scrambled eggs and toast with a cup of coffee. While I'm cooking, I'll also check my "
          "emails to see if there's anything urgent."
      )

      # Call the LLM with the JSON schema

      extract = client.chat.completions.create(
          messages=[
              {
                  "role": "system",
                  "content": f"The following is a voice message transcript. Only answer in JSON and follow this schema {json.dumps(VoiceNote.model_json_schema())}.",
              },
              {
                  "role": "user",
                  "content": transcript,
              },
          ],
          model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
          response_format={
              "type": "json_schema",
              "schema": VoiceNote.model_json_schema(),
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

  // Defining the schema we want our data in
  const voiceNoteSchema = z.object({
    title: z.string().describe("A title for the voice note"),
    summary: z
      .string()
      .describe("A short one sentence summary of the voice note."),
    actionItems: z
      .array(z.string())
      .describe("A list of action items from the voice note"),
  });
  const jsonSchema = zodToJsonSchema(voiceNoteSchema, { target: "openAi" });

  async function main() {
    const transcript =
      "Good morning! It's 7:00 AM, and I'm just waking up. Today is going to be a busy day, so let's get started. First, I need to make a quick breakfast. I think I'll have some scrambled eggs and toast with a cup of coffee. While I'm cooking, I'll also check my emails to see if there's anything urgent.";
    const extract = await together.chat.completions.create({
      messages: [
        {
          role: "system",
          content: `The following is a voice message transcript. Only answer in JSON and follow this schema ${JSON.stringify(jsonSchema)}.`,
        },
        {
          role: "user",
          content: transcript,
        },
      ],
      model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      response_format: { type: "json_object", schema: jsonSchema },
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
```Text
  curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -d '{
    "messages": [
      {
        "role": "system",
        "content": "The following is a voice message transcript. Only answer in JSON."
      },
      {
        "role": "user",
        "content": "Good morning! It'"'"'s 7:00 AM, and I'"'"'m just waking up. Today is going to be a busy day, so let'"'"'s get started. First, I need to make a quick breakfast. I think I'"'"'ll have some scrambled eggs and toast with a cup of coffee. While I'"'"'m cooking, I'"'"'ll also check my emails to see if there'"'"'s anything urgent."
      }
    ],
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    "response_format": {
      "type": "json_object",
      "schema": {
        "properties": {
          "title": {
            "description": "A title for the voice note",
            "title": "Title",
            "type": "string"
          },
          "summary": {
            "description": "A short one sentence summary of the voice note.",
            "title": "Summary",
            "type": "string"
          },
          "actionItems": {
            "description": "A list of action items from the voice note",
            "items": { "type": "string" },
            "title": "Actionitems",
            "type": "array"
          }
        },
        "required": ["title", "summary", "actionItems"],
        "title": "VoiceNote",
        "type": "object"
      }
    }
  }'
```

If we try it out, our model responds with the following:
```json
{
  "title": "Morning Routine",
  "summary": "Starting the day with a quick breakfast and checking emails",
  "actionItems": [
    "Cook scrambled eggs and toast",
    "Brew a cup of coffee",
    "Check emails for urgent messages"
  ]
}
```

Pretty neat!

Our model has generated a summary of the user's transcript using the schema we gave it.

### Prompting the model

It's important to always tell the model to respond **only in JSON** and include a plain‑text copy of the schema in the prompt (either as a system prompt or a user message). This instruction must be given *in addition* to passing the schema via the `response_format` parameter.

By giving an explicit "respond in JSON" direction and showing the schema text, the model will generate output that matches the structure you defined. This combination of a textual schema and the `response_format` setting ensures consistent, valid JSON responses every time.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
