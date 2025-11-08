---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the tools

import json

def list_calendar_events(date: str):
  events = '[{"start": "14:00", "end": "15:00"}, {"start": "15:00", "end": "16:00"}, {"start": "17:00", "end": "18:00"}]'
  print(f"Listing events: {events}")
  return events

def create_calendar_event(date: str, time: str, duration: int):
  print(f"Creating a {duration} hour long event at {time} on {date}")
  return True

list_calendar_events_tool = {
  "name": "list_calendar_events",
  "description": "returns a list of calendar events for the specified date, including the start time and end time for each event",
  "parameter_definitions": {
    "date": {
      "description": "the date to list events for, formatted as mm/dd/yy",
      "type": "str",
      "required": True
    }
  }
}

create_calendar_event_tool = {
  "name": "create_calendar_event_tool",
  "description": "creates a calendar event of the specified duration at the specified time and date",
  "parameter_definitions": {
    "date": {
      "description": "the date on which the event starts, formatted as mm/dd/yy",
      "type": "str",
      "required": True
    },
    "time": {
      "description": "the time of the event, formatted using 24h military time formatting",
      "type": "str",
      "required": True
    },
    "duration": {
      "description": "the number of hours the event lasts for",
      "type": "float",
      "required": True
    }
  }
}

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
