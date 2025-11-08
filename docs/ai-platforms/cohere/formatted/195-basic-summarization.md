---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic summarization

You can perform text summarization with a simple prompt asking the model to summarize a piece of text.

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  document = """Equipment rental in North America is predicted to "normalize" going into 2024,
  according to Josh Nickell, vice president of equipment rental for the American Rental
  Association (ARA).
  "Rental is going back to 'normal,' but normal means that strategy matters again -
  geography matters, fleet mix matters, customer type matters," Nickell said. "In
  late 2020 to 2022, you just showed up with equipment and you made money.
  "Everybody was breaking records, from the national rental chains to the smallest
  rental companies; everybody was having record years, and everybody was raising
  prices. The conversation was, 'How much are you up?' And now, the conversation
  is changing to 'What's my market like?'"
  Nickell stressed this shouldn't be taken as a pessimistic viewpoint. It's simply
  coming back down to Earth from unprecedented circumstances during the time of Covid.
  Rental companies are still seeing growth, but at a more moderate level."""

  message = f"Generate a concise summary of this text\n{document}"

  response = co.chat(
      model="command-a-03-2025",
      messages=[{"role": "user", "content": message}],
  )


  print(response.message.content[0].text)
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "user",
        "content": "Generate a concise summary of this text\n\nEquipment rental in North America is predicted to \"normalize\" going into 2024, according to Josh Nickell, vice president of equipment rental for the American Rental Association (ARA).\n\"Rental is going back to '\''normal,'\'' but normal means that strategy matters again - geography matters, fleet mix matters, customer type matters,\" Nickell said. \"In late 2020 to 2022, you just showed up with equipment and you made money.\n\"Everybody was breaking records, from the national rental chains to the smallest rental companies; everybody was having record years, and everybody was raising prices. The conversation was, '\''How much are you up?'\'' And now, the conversation is changing to '\''What'\''s my market like?'\''\"\nNickell stressed this shouldn'\''t be taken as a pessimistic viewpoint. It'\''s simply coming back down to Earth from unprecedented circumstances during the time of Covid. Rental companies are still seeing growth, but at a more moderate level."
      }
    ]
  }'
```
</CodeBlocks>

(NOTE: Here, we are passing the document as a variable, but you can also just copy the document directly into the message and ask Chat to summarize it.)

Here's a sample output:
```
The equipment rental market in North America is expected to normalize by 2024,
according to Josh Nickell of the American Rental Association. This means a shift
from the unprecedented growth of 2020-2022, where demand and prices were high,
to a more strategic approach focusing on geography, fleet mix, and customer type.
Rental companies are still experiencing growth, but at a more moderate and sustainable level.
```

### Length control

You can further control the output by defining the length of the summary in your prompt. For example, you can specify the number of sentences to be generated.
```python PYTHON
message = f"Summarize this text in one sentence\n{document}"

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```
And here's what a sample of the output might look like:
```
The equipment rental market in North America is expected to stabilize in 2024,
with a focus on strategic considerations such as geography, fleet mix, and
customer type, according to Josh Nickell of the American Rental Association (ARA).
```
You can also specify the length in terms of word count.
```python PYTHON
message = f"Summarize this text in less than 10 words\n{document}"

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```
```
Rental equipment supply and demand to balance.
```javascript
(Note: While the model is generally good at adhering to length instructions, due to the nature of LLMs, we do not guarantee that the exact word, sentence, or paragraph numbers will be generated.)

### Format control

Instead of generating summaries as paragraphs, you can also prompt the model to generate the summary as bullet points.
```python PYTHON
message = f"Generate a concise summary of this text as bullet points\n{document}"

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```
```
- Equipment rental in North America is expected to "normalize" by 2024, according to Josh Nickell
  of the American Rental Association (ARA).
- This "normalization" means a return to strategic focus on factors like geography, fleet mix,
  and customer type.
- In the past two years, rental companies easily made money and saw record growth due to the
  unique circumstances of the Covid pandemic.
- Now, the focus is shifting from universal success to varying market conditions and performance.
- Nickell's outlook is not pessimistic; rental companies are still growing, but at a more 
  sustainable and moderate pace.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
