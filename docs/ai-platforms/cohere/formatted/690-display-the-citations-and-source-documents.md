---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display the citations and source documents

if response.message.citations:
    print("\nCITATIONS:")
    for citation in response.message.citations:
        print(citation, "\n")
```
```
You can get to know your teammates by joining relevant Slack channels and engaging in team-building activities. These activities include monthly outings and weekly game nights. You are also welcome to suggest new activity ideas.

CITATIONS:
start=38 end=69 text='joining relevant Slack channels' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] 

start=86 end=111 text='team-building activities.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] 

start=137 end=176 text='monthly outings and weekly game nights.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] 

start=201 end=228 text='suggest new activity ideas.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
