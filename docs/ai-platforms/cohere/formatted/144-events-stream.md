---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Events stream

In RAG, the events streamed by the endpoint follows the structure of a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events) but contains additional events for tool calling and response generation with the associated contents. This section describes the stream of events and their contents.

### Event types

`message-start`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

`content-start`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

`content-delta`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

`citation-start`

Emitted for every citation generated in the response. This event contains the details about a citation such as the `start` and `end` indices of the text that cites a source(s), the corresponding `text`, and the list of `sources`.

`citation-end`

Emitted to indicate the end of a citation. If there are multiple citations generated, the events will come as a sequence of `citation-start` and `citation-end` pairs.

`content-end`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

`message-end`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

### Example stream

The following is an example stream with RAG.
```mdx wordWrap
"Where do the tallest penguins live?"

type='message-start' id='d93f187e-e9ac-44a9-a2d9-bdf2d65fee94' delta=ChatMessageStartEventDelta(message=ChatMessageStartEventDeltaMessage(role='assistant', content=[], tool_plan='', tool_calls=[], citations=[])) 
 --------------------------------------------------
type='content-start' index=0 delta=ChatContentStartEventDelta(message=ChatContentStartEventDeltaMessage(content=ChatContentStartEventDeltaMessageContent(text='', type='text'))) 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='The'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' tallest'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' penguins'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' are'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' the'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' Emperor'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' penguins'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='.'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' They'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' only'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' live'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' in'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' Antarctica'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='.'))) logprobs=None 
 --------------------------------------------------
type='citation-start' index=0 delta=CitationStartEventDelta(message=CitationStartEventDeltaMessage(citations=Citation(start=29, end=46, text='Emperor penguins.', sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})], type='TEXT_CONTENT'))) 
 --------------------------------------------------
type='citation-end' index=0 
 --------------------------------------------------
type='citation-start' index=1 delta=CitationStartEventDelta(message=CitationStartEventDeltaMessage(citations=Citation(start=65, end=76, text='Antarctica.', sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})], type='TEXT_CONTENT'))) 
 --------------------------------------------------
type='citation-end' index=1 
 --------------------------------------------------
type='content-end' index=0 
 --------------------------------------------------
type='message-end' id=None delta=ChatMessageEndEventDelta(finish_reason='COMPLETE', usage=Usage(billed_units=UsageBilledUnits(input_tokens=34.0, output_tokens=14.0, search_units=None, classifications=None), tokens=UsageTokens(input_tokens=721.0, output_tokens=59.0))) 
 --------------------------------------------------
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
