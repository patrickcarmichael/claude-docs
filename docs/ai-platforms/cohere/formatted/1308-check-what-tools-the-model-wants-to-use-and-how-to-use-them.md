---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Check what tools the model wants to use and how to use them

res = co.chat(
    model="command-a-03-2025",
    preamble="Today is Thursday, may 23, 2024",
    message="book an hour long appointment for the first available free slot after 3pm",
    force_single_step=False,
    tools=[list_calendar_events_tool, create_calendar_event_tool])

while res.tool_calls:
  print(res.text) # This will be an observation and a plan with next steps

  # invoke the recommended tools

  tool_results = []
  for call in res.tool_calls:
    tool_results.append({"call": call, "outputs": invoke_tool(call)})

  # send back the tool results

  res = co.chat(
    model="command-a-03-2025",
    chat_history=res.chat_history,
    message="",
    force_single_step=False,
    tools=[list_calendar_events_tool, create_calendar_event_tool],
    tool_results=tool_results,
  )

print(res.text) # print the final answer

```
```txt title="Output"
I will check the user's calendar for today after 3pm and book an hour-long appointment in the first available slot.
Listing events: [{"start": "14:00", "end": "15:00"}, {"start": "15:00", "end": "16:00"}, {"start": "17:00", "end": "18:00"}]
The user has events scheduled from 2pm to 4pm and from 5pm to 6pm. I will book an hour-long appointment from 4pm to 5pm.
Creating a 1 hour long event at 16:00 on 05/23/2024
I've booked an hour-long appointment for you today from 4pm to 5pm.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
