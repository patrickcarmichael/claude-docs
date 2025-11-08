---
title: "Crewai: Building Trigger-Driven Automations"
description: "Building Trigger-Driven Automations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Building Trigger-Driven Automations


Before building your automation, it's helpful to understand the structure of trigger payloads that your crews and flows will receive.

### Trigger Setup Checklist

Before wiring a trigger into production, make sure you:

* Connect the integration under **Tools & Integrations** and complete any OAuth or API key steps
* Enable the trigger toggle on the deployment that should respond to events
* Provide any required environment variables (API tokens, tenant IDs, shared secrets)
* Create or update tasks that can parse the incoming payload within the first crew task or flow step
* Decide whether to pass trigger context automatically using `allow_crewai_trigger_context`
* Set up monitoring—webhook logs, CrewAI execution history, and optional external alerting

### Testing Triggers Locally with CLI

The CrewAI CLI provides powerful commands to help you develop and test trigger-driven automations without deploying to production.

#### List Available Triggers

View all available triggers for your connected integrations:

```bash  theme={null}
crewai triggers list
```

This command displays all triggers available based on your connected integrations, showing:

* Integration name and connection status
* Available trigger types
* Trigger names and descriptions

#### Simulate Trigger Execution

Test your crew with realistic trigger payloads before deployment:

```bash  theme={null}
crewai triggers run <trigger_name>
```

For example:

```bash  theme={null}
crewai triggers run microsoft_onedrive/file_changed
```

This command:

* Executes your crew locally
* Passes a complete, realistic trigger payload
* Simulates exactly how your crew will be called in production

<Warning>
  **Important Development Notes:**

  * Use `crewai triggers run <trigger>` to simulate trigger execution during development
  * Using `crewai run` will NOT simulate trigger calls and won't pass the trigger payload
  * After deployment, your crew will be executed with the actual trigger payload
  * If your crew expects parameters that aren't in the trigger payload, execution may fail
</Warning>

### Triggers with Crew

Your existing crew definitions work seamlessly with triggers, you just need to have a task to parse the received payload:

```python  theme={null}
@CrewBase
class MyAutomatedCrew:
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
        )

    @task
    def parse_trigger_payload(self) -> Task:
        return Task(
            config=self.tasks_config['parse_trigger_payload'],
            agent=self.researcher(),
        )

    @task
    def analyze_trigger_content(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_trigger_data'],
            agent=self.researcher(),
        )
```

The crew will automatically receive and can access the trigger payload through the standard CrewAI context mechanisms.

<Note>
  Crew and Flow inputs can include `crewai_trigger_payload`. CrewAI automatically injects this payload:

  * Tasks: appended to the first task's description by default ("Trigger Payload: {crewai_trigger_payload}")
  * Control via `allow_crewai_trigger_context`: set `True` to always inject, `False` to never inject
  * Flows: any `@start()` method that accepts a `crewai_trigger_payload` parameter will receive it
</Note>

### Integration with Flows

For flows, you have more control over how trigger data is handled:

#### Accessing Trigger Payload

All `@start()` methods in your flows will accept an additional parameter called `crewai_trigger_payload`:

```python  theme={null}
from crewai.flow import Flow, start, listen

class MyAutomatedFlow(Flow):
    @start()
    def handle_trigger(self, crewai_trigger_payload: dict = None):
        """
        This start method can receive trigger data
        """
        if crewai_trigger_payload:
            # Process the trigger data
            trigger_id = crewai_trigger_payload.get('id')
            event_data = crewai_trigger_payload.get('payload', {})

            # Store in flow state for use by other methods
            self.state.trigger_id = trigger_id
            self.state.trigger_type = event_data

            return event_data

        # Handle manual execution
        return None

    @listen(handle_trigger)
    def process_data(self, trigger_data):
        """
        Process the data from the trigger
        """
        # ... process the trigger
```

#### Triggering Crews from Flows

When kicking off a crew within a flow that was triggered, pass the trigger payload as it:

```python  theme={null}
@start()
def delegate_to_crew(self, crewai_trigger_payload: dict = None):
    """
    Delegate processing to a specialized crew
    """
    crew = MySpecializedCrew()

    # Pass the trigger payload to the crew
    result = crew.crew().kickoff(
        inputs={
            'a_custom_parameter': "custom_value",
            'crewai_trigger_payload': crewai_trigger_payload
        },
    )

    return result
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Managing Triggers](./1495-managing-triggers.md)

**Next:** [Troubleshooting →](./1497-troubleshooting.md)
