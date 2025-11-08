---
title: "Crewai: Method 2: Using the API"
description: "Method 2: Using the API section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Method 2: Using the API


You can also kickoff crews programmatically using the CrewAI AMP REST API.

### Authentication

All API requests require a bearer token for authentication:

```bash  theme={null}
curl -H "Authorization: Bearer YOUR_CREW_TOKEN" https://your-crew-url.crewai.com
```

Your bearer token is available on the Status tab of your crew's detail page.

### Checking Crew Health

Before executing operations, you can verify that your crew is running properly:

```bash  theme={null}
curl -H "Authorization: Bearer YOUR_CREW_TOKEN" https://your-crew-url.crewai.com
```

A successful response will return a message indicating the crew is operational:

```
Healthy%
```

### Step 1: Retrieve Required Inputs

First, determine what inputs your crew requires:

```bash  theme={null}
curl -X GET \
  -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  https://your-crew-url.crewai.com/inputs
```

The response will be a JSON object containing an array of required input parameters, for example:

```json  theme={null}
{"inputs":["topic","current_year"]}
```

This example shows that this particular crew requires two inputs: `topic` and `current_year`.

### Step 2: Kickoff Execution

Initiate execution by providing the required inputs:

```bash  theme={null}
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  -d '{"inputs": {"topic": "AI Agent Frameworks", "current_year": "2025"}}' \
  https://your-crew-url.crewai.com/kickoff
```

The response will include a `kickoff_id` that you'll need for tracking:

```json  theme={null}
{"kickoff_id":"abcd1234-5678-90ef-ghij-klmnopqrstuv"}
```

### Step 3: Check Execution Status

Monitor the execution progress using the kickoff\_id:

```bash  theme={null}
curl -X GET \
  -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  https://your-crew-url.crewai.com/status/abcd1234-5678-90ef-ghij-klmnopqrstuv
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Method 1: Using the Web Interface](./1558-method-1-using-the-web-interface.md)

**Next:** [Handling Executions →](./1560-handling-executions.md)
