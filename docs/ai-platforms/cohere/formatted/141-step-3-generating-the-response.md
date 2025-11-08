---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Generating the response

Finally, we call the Chat endpoint by passing the retrieved documents. This tells the model to run in RAG-mode and use these documents in its response.

The response and citations are then generated based on the the query and the documents retrieved.

<CodeBlocks>
```python PYTHON
  messages = [{"role": "user", "content": message}]

  # Generate the response

  response = co.chat(
      model="command-a-03-2025",
      messages=messages,
      documents=reranked_documents,
  )

  # Display the response

  print(response.message.content[0].text)

  # Display the citations and source documents

  if response.message.citations:
      print("\nCITATIONS:")
      for citation in response.message.citations:
          print(citation, "\n")
```
```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/chat' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "user",
        "content": "I'\''m joining a new team as a Principal Analyst. What are the best ways to quickly get to know my teammates?"
      }
    ],
    "documents": [
      {
        "data": {
          "text": "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!"
        }
      },
      {
        "data": {
          "text": "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged."
        }
      }
    ]
  }'
```
</CodeBlocks>
```mdx
To get to know your teammates, you can join relevant Slack channels to stay informed and engaged. You will receive an invite via email. You can also participate in team-building activities such as monthly outings and weekly game nights.

CITATIONS:
start=39 end=67 text='join relevant Slack channels' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] type='TEXT_CONTENT' 

start=71 end=97 text='stay informed and engaged.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] type='TEXT_CONTENT' 

start=107 end=135 text='receive an invite via email.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] type='TEXT_CONTENT' 

start=164 end=188 text='team-building activities' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] type='TEXT_CONTENT' 

start=197 end=236 text='monthly outings and weekly game nights.' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] type='TEXT_CONTENT'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
