---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Events stream

type='message-start' id='fba98ad3-e5a1-413c-a8de-84fbf9baabf7' delta=ChatMessageStartEventDelta(message=ChatMessageStartEventDeltaMessage(role='assistant', content=[], tool_plan='', tool_calls=[], citations=[])) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan='I')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' will')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' search')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' for')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' the')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' weather')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' in')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' Madrid')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' and')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan=' Brasilia')) 
 --------------------------------------------------
type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(message=ChatToolPlanDeltaEventDeltaMessage(tool_plan='.')) 
 --------------------------------------------------
type='tool-call-start' index=0 delta=ChatToolCallStartEventDelta(message=ChatToolCallStartEventDeltaMessage(tool_calls=ToolCallV2(id='get_weather_p1t92w7gfgq7', type='function', function=ToolCallV2Function(name='get_weather', arguments='')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='{\n    "')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='location')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='":')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments=' "')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='Madrid')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='"')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='\n')))) 
 --------------------------------------------------
type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='}')))) 
 --------------------------------------------------
type='tool-call-end' index=0 
 --------------------------------------------------
type='tool-call-start' index=1 delta=ChatToolCallStartEventDelta(message=ChatToolCallStartEventDeltaMessage(tool_calls=ToolCallV2(id='get_weather_ay6nmvjgp9vn', type='function', function=ToolCallV2Function(name='get_weather', arguments='')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='{\n    "')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='location')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='":')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments=' "')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='Bras')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='ilia')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='"')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='\n')))) 
 --------------------------------------------------
type='tool-call-delta' index=1 delta=ChatToolCallDeltaEventDelta(message=ChatToolCallDeltaEventDeltaMessage(tool_calls=ChatToolCallDeltaEventDeltaMessageToolCalls(function=ChatToolCallDeltaEventDeltaMessageToolCallsFunction(arguments='}')))) 
 --------------------------------------------------
type='tool-call-end' index=1 
 --------------------------------------------------
type='message-end' id=None delta=ChatMessageEndEventDelta(finish_reason='TOOL_CALL', usage=Usage(billed_units=UsageBilledUnits(input_tokens=37.0, output_tokens=28.0, search_units=None, classifications=None), tokens=UsageTokens(input_tokens=913.0, output_tokens=83.0))) 
 --------------------------------------------------
```

### Response generation step

#### Event types

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

#### Example stream

The following is an example stream in the response generation step.
```mdx wordWrap
"What's the weather in Madrid and Brasilia?"

type='message-start' id='e8f9afc1-0888-46f0-a9ed-eb0e5a51e17f' delta=ChatMessageStartEventDelta(message=ChatMessageStartEventDeltaMessage(role='assistant', content=[], tool_plan='', tool_calls=[], citations=[])) 
 --------------------------------------------------
type='content-start' index=0 delta=ChatContentStartEventDelta(message=ChatContentStartEventDeltaMessage(content=ChatContentStartEventDeltaMessageContent(text='', type='text'))) 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='It'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' is'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' currently'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' 2'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='4'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='°'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='C in'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' Madrid'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' and'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' 2'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='8'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='°'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='C in'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' Brasilia'))) logprobs=None 
 --------------------------------------------------
type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='.'))) logprobs=None 
 --------------------------------------------------
type='citation-start' index=0 delta=CitationStartEventDelta(message=CitationStartEventDeltaMessage(citations=Citation(start=16, end=20, text='24°C', sources=[ToolSource(type='tool', id='get_weather_m3kdvxncg1p8:0', tool_output={'temperature': '{"madrid":"24°C"}'})], type='TEXT_CONTENT'))) 
 --------------------------------------------------
type='citation-end' index=0 
 --------------------------------------------------
type='citation-start' index=1 delta=CitationStartEventDelta(message=CitationStartEventDeltaMessage(citations=Citation(start=35, end=39, text='28°C', sources=[ToolSource(type='tool', id='get_weather_cfwfh3wzkbrs:0', tool_output={'temperature': '{"brasilia":"28°C"}'})], type='TEXT_CONTENT'))) 
 --------------------------------------------------
type='citation-end' index=1 
 --------------------------------------------------
type='content-end' index=0 
 --------------------------------------------------
type='message-end' id=None delta=ChatMessageEndEventDelta(finish_reason='COMPLETE', usage=Usage(billed_units=UsageBilledUnits(input_tokens=87.0, output_tokens=19.0, search_units=None, classifications=None), tokens=UsageTokens(input_tokens=1061.0, output_tokens=85.0))) 
 --------------------------------------------------
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
