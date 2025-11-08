# CrewAI Tracing

**Navigation:** [← Previous](./11-replay-tasks-from-latest-crew-kickoff.md) | [Index](./index.md) | [Next →](./13-team-management.md)

---

# CrewAI Tracing
Source: https://docs.crewai.com/en/observability/tracing

Built-in tracing for CrewAI Crews and Flows with the CrewAI AMP platform


# CrewAI Built-in Tracing

CrewAI provides built-in tracing capabilities that allow you to monitor and debug your Crews and Flows in real-time. This guide demonstrates how to enable tracing for both **Crews** and **Flows** using CrewAI's integrated observability platform.

> **What is CrewAI Tracing?** CrewAI's built-in tracing provides comprehensive observability for your AI agents, including agent decisions, task execution timelines, tool usage, and LLM calls - all accessible through the [CrewAI AMP platform](https://app.crewai.com).

<img src="https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=b7e95a8f56ed3c459699acf641b4ae5a" alt="CrewAI Tracing Interface" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/crewai-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=280&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=432b91fbee9d71f0c152a097c1b87773 280w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=560&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=62b6417d4f5289617124df196c0a9c94 560w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=840&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=fb115418f8fb1c0bb79e9ac647158996 840w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=1100&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=bb955f30c027461597f15dbe436fc068 1100w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=1650&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=d891852f83abfd576cc6b2c3eb83749c 1650w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=2500&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=67cbde03f418d19d66d4273df9427db2 2500w" />


## Prerequisites

Before you can use CrewAI tracing, you need:

1. **CrewAI AMP Account**: Sign up for a free account at [app.crewai.com](https://app.crewai.com)
2. **CLI Authentication**: Use the CrewAI CLI to authenticate your local environment

```bash  theme={null}
crewai login
```


## Setup Instructions

### Step 1: Create Your CrewAI AMP Account

Visit [app.crewai.com](https://app.crewai.com) and create your free account. This will give you access to the CrewAI AMP platform where you can view traces, metrics, and manage your crews.

### Step 2: Install CrewAI CLI and Authenticate

If you haven't already, install CrewAI with the CLI tools:

```bash  theme={null}
uv add crewai[tools]
```

Then authenticate your CLI with your CrewAI AMP account:

```bash  theme={null}
crewai login
```

This command will:

1. Open your browser to the authentication page
2. Prompt you to enter a device code
3. Authenticate your local environment with your CrewAI AMP account
4. Enable tracing capabilities for your local development

### Step 3: Enable Tracing in Your Crew

You can enable tracing for your Crew by setting the `tracing` parameter to `True`:

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool


# Define your agents
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI and data science",
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    tools=[SerperDevTool()],
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
)


# Create tasks for your agents
research_task = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
    Identify key trends, breakthrough technologies, and potential industry impacts.""",
    expected_output="Full analysis report in bullet points",
    agent=researcher,
)

writing_task = Task(
    description="""Using the insights provided, develop an engaging blog
    post that highlights the most significant AI advancements.
    Your post should be informative yet accessible, catering to a tech-savvy audience.""",
    expected_output="Full blog post of at least 4 paragraphs",
    agent=writer,
)


# Enable tracing in your crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    tracing=True,  # Enable built-in tracing
    verbose=True
)


# Execute your crew
result = crew.kickoff()
```

### Step 4: Enable Tracing in Your Flow

Similarly, you can enable tracing for CrewAI Flows:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class ExampleFlow(Flow[ExampleState]):
    def __init__(self):
        super().__init__(tracing=True)  # Enable tracing for the flow

    @start()
    def first_method(self):
        print("Starting the flow")
        self.state.counter = 1
        self.state.message = "Flow started"
        return "continue"

    @listen("continue")
    def second_method(self):
        print("Continuing the flow")
        self.state.counter += 1
        self.state.message = "Flow continued"
        return "finish"

    @listen("finish")
    def final_method(self):
        print("Finishing the flow")
        self.state.counter += 1
        self.state.message = "Flow completed"


# Create and run the flow with tracing enabled
flow = ExampleFlow(tracing=True)
result = flow.kickoff()
```

### Step 5: View Traces in the CrewAI AMP Dashboard

After running the crew or flow, you can view the traces generated by your CrewAI application in the CrewAI AMP dashboard. You should see detailed steps of the agent interactions, tool usages, and LLM calls.
Just click on the link below to view the traces or head over to the traces tab in the dashboard [here](https://app.crewai.com/crewai_plus/trace_batches)
<img src="https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=72981ddafcda030270c059f08b98db03" alt="CrewAI Tracing Interface" data-og-width="3272" width="3272" data-og-height="162" height="162" data-path="images/view-traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=280&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=ccd01161e9258840e74ef1c451f84269 280w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=560&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=d8feaccbddc300723769a977ca3e0ff9 560w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=840&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=2b404956f27d32dd38b0a5d4bf48ab58 840w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=1100&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=8bc1f5f99f4289ee1dd7ebe2e60bb189 1100w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=1650&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=1ab7e96c4017cf1cbab719c695884969 1650w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=2500&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=3ab9ea0309e81741969db86307657b90 2500w" />

### Alternative: Environment Variable Configuration

You can also enable tracing globally by setting an environment variable:

```bash  theme={null}
export CREWAI_TRACING_ENABLED=true
```

Or add it to your `.env` file:

```env  theme={null}
CREWAI_TRACING_ENABLED=true
```

When this environment variable is set, all Crews and Flows will automatically have tracing enabled, even without explicitly setting `tracing=True`.


## Viewing Your Traces

### Access the CrewAI AMP Dashboard

1. Visit [app.crewai.com](https://app.crewai.com) and log in to your account
2. Navigate to your project dashboard
3. Click on the **Traces** tab to view execution details

### What You'll See in Traces

CrewAI tracing provides comprehensive visibility into:

* **Agent Decisions**: See how agents reason through tasks and make decisions
* **Task Execution Timeline**: Visual representation of task sequences and dependencies
* **Tool Usage**: Monitor which tools are called and their results
* **LLM Calls**: Track all language model interactions, including prompts and responses
* **Performance Metrics**: Execution times, token usage, and costs
* **Error Tracking**: Detailed error information and stack traces

### Trace Features

* **Execution Timeline**: Click through different stages of execution
* **Detailed Logs**: Access comprehensive logs for debugging
* **Performance Analytics**: Analyze execution patterns and optimize performance
* **Export Capabilities**: Download traces for further analysis

### Authentication Issues

If you encounter authentication problems:

1. Ensure you're logged in: `crewai login`
2. Check your internet connection
3. Verify your account at [app.crewai.com](https://app.crewai.com)

### Traces Not Appearing

If traces aren't showing up in the dashboard:

1. Confirm `tracing=True` is set in your Crew/Flow
2. Check that `CREWAI_TRACING_ENABLED=true` if using environment variables
3. Ensure you're authenticated with `crewai login`
4. Verify your crew/flow is actually executing



# TrueFoundry Integration
Source: https://docs.crewai.com/en/observability/truefoundry



TrueFoundry provides an enterprise-ready [AI Gateway](https://www.truefoundry.com/ai-gateway) which can integrate with agentic frameworks like CrewAI and provides governance and observability for your AI Applications. TrueFoundry AI Gateway serves as a unified interface for LLM access, providing:

* **Unified API Access**: Connect to 250+ LLMs (OpenAI, Claude, Gemini, Groq, Mistral) through one API
* **Low Latency**: Sub-3ms internal latency with intelligent routing and load balancing
* **Enterprise Security**: SOC 2, HIPAA, GDPR compliance with RBAC and audit logging
* **Quota and cost management**: Token-based quotas, rate limiting, and comprehensive usage tracking
* **Observability**: Full request/response logging, metrics, and traces with customizable retention


## How TrueFoundry Integrates with CrewAI

### Installation & Setup

<Steps>
  <Step title="Install CrewAI">
    ```bash  theme={null}
    pip install crewai
    ```
  </Step>

  <Step title="Get TrueFoundry Access Token">
    1. Sign up for a [TrueFoundry account](https://www.truefoundry.com/register)
    2. Follow the steps here in [Quick start](https://docs.truefoundry.com/gateway/quick-start)
  </Step>

  <Step title="Configure CrewAI with TrueFoundry">
        <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=746c0bd23a77535f35b0b2bcf3320bf5" alt="TrueFoundry Code Configuration" data-og-width="2940" width="2940" data-og-height="1664" height="1664" data-path="images/new-code-snippet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1d7f4e8883760766aa1ae1274fba2ffe 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4604432c1e1121d24c3fa6ad93bc0bd9 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=8dd95282de37aa70090ac61a00b6e1bb 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=920a67bee38e979c770d775195b60864 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4173b6e99ed12b00b54bf3f222589863 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=176dd84222c8c1a6f40af3e0adb88e37 2500w" />

    ```python  theme={null}
    from crewai import LLM

    # Create an LLM instance with TrueFoundry AI Gateway
    truefoundry_llm = LLM(
        model="openai-main/gpt-4o",  # Similarly, you can call any model from any provider
        base_url="your_truefoundry_gateway_base_url",
        api_key="your_truefoundry_api_key"
    )

    # Use in your CrewAI agents
    from crewai import Agent

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=truefoundry_llm,
            verbose=True
        )
    ```
  </Step>
</Steps>

### Complete CrewAI Example

```python  theme={null}
from crewai import Agent, Task, Crew, LLM


# Configure LLM with TrueFoundry
llm = LLM(
    model="openai-main/gpt-4o",
    base_url="your_truefoundry_gateway_base_url", 
    api_key="your_truefoundry_api_key"
)


# Create agents
researcher = Agent(
    role='Research Analyst',
    goal='Conduct detailed market research',
    backstory='Expert market analyst with attention to detail',
    llm=llm,
    verbose=True
)

writer = Agent(
    role='Content Writer', 
    goal='Create comprehensive reports',
    backstory='Experienced technical writer',
    llm=llm,
    verbose=True
)


# Create tasks
research_task = Task(
    description='Research AI market trends for 2024',
    agent=researcher,
    expected_output='Comprehensive research summary'
)

writing_task = Task(
    description='Create a market research report',
    agent=writer,
    expected_output='Well-structured report with insights',
    context=[research_task]
)


# Create and execute crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

result = crew.kickoff()
```

### Observability and Governance

Monitor your CrewAI agents through TrueFoundry's metrics tab:
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=33755ff848cb457e162e806c20c98216" alt="TrueFoundry metrics" data-og-width="3840" width="3840" data-og-height="1984" height="1984" data-path="images/gateway-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=49a01b5e5bcc0429efd529860c020c10 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=3f47f171146339690e3516a892020626 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=857541d282cce3557f796ade097be01c 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2f2b883b00e823ceb25ae1b747c656a4 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9ddee789557bdbaacec42fd405180458 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e9097f84b482e5c4da153d2d0271e6bf 2500w" />

With Truefoundry's AI gateway, you can monitor and analyze:

* **Performance Metrics**: Track key latency metrics like Request Latency, Time to First Token (TTFS), and Inter-Token Latency (ITL) with P99, P90, and P50 percentiles
* **Cost and Token Usage**: Gain visibility into your application's costs with detailed breakdowns of input/output tokens and the associated expenses for each model
* **Usage Patterns**: Understand how your application is being used with detailed analytics on user activity, model distribution, and team-based usage
* **Rate limit and Load balancing**: You can set up rate limiting, load balancing and fallback for your models


## Tracing

For a more detailed understanding on tracing, please see [getting-started-tracing](https://docs.truefoundry.com/docs/tracing/tracing-getting-started).For tracing, you can add the Traceloop SDK:
For tracing, you can add the Traceloop SDK:

```bash  theme={null}
pip install traceloop-sdk
```

```python  theme={null}
from traceloop.sdk import Traceloop


# Initialize enhanced tracing
Traceloop.init(
    api_endpoint="https://your-truefoundry-endpoint/api/tracing",
    headers={
        "Authorization": f"Bearer {your_truefoundry_pat_token}",
        "TFY-Tracing-Project": "your_project_name",
    },
)
```

This provides additional trace correlation across your entire CrewAI workflow.
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=90623834e0ba9f4ccb09890f6824912d" alt="TrueFoundry CrewAI Tracing" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/tracing_crewai.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d05099079060dfd1588ac0c8de28e07b 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=645362e069e687f7dc6fd6c44a97a4ef 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=aac6d42bbd2f457b59f6a4b22d6a7be1 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7f166e1329cef8da8c1e07a38dc75506 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6e91cffda555b8cc7ce1800ed1b508b1 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bf6296110bd62d9bb30ae2d0822d4b8d 2500w" />



# Weave Integration
Source: https://docs.crewai.com/en/observability/weave

Learn how to use Weights & Biases (W&B) Weave to track, experiment with, evaluate, and improve your CrewAI applications.


# Weave Overview

[Weights & Biases (W\&B) Weave](https://weave-docs.wandb.ai/) is a framework for tracking, experimenting with, evaluating, deploying, and improving LLM-based applications.

<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.gif?s=4a933830e3e3cf146c4c87cb44d46475" alt="Overview of W&B Weave CrewAI tracing usage" data-og-width="852" width="852" data-og-height="480" height="480" data-path="images/weave-tracing.gif" data-optimize="true" data-opv="3" />

Weave provides comprehensive support for every stage of your CrewAI application development:

* **Tracing & Monitoring**: Automatically track LLM calls and application logic to debug and analyze production systems
* **Systematic Iteration**: Refine and iterate on prompts, datasets, and models
* **Evaluation**: Use custom or pre-built scorers to systematically assess and enhance agent performance
* **Guardrails**: Protect your agents with pre- and post-safeguards for content moderation and prompt safety

Weave automatically captures traces for your CrewAI applications, enabling you to monitor and analyze your agents' performance, interactions, and execution flow. This helps you build better evaluation datasets and optimize your agent workflows.


## Setup Instructions

<Steps>
  <Step title="Install required packages">
    ```shell  theme={null}
    pip install crewai weave
    ```
  </Step>

  <Step title="Set up W&B Account">
    Sign up for a [Weights & Biases account](https://wandb.ai) if you haven't already. You'll need this to view your traces and metrics.
  </Step>

  <Step title="Initialize Weave in Your Application">
    Add the following code to your application:

    ```python  theme={null}
    import weave

    # Initialize Weave with your project name
    weave.init(project_name="crewai_demo")
    ```

    After initialization, Weave will provide a URL where you can view your traces and metrics.
  </Step>

  <Step title="Create your Crews/Flows">
    ```python  theme={null}
    from crewai import Agent, Task, Crew, LLM, Process

    # Create an LLM with a temperature of 0 to ensure deterministic outputs
    llm = LLM(model="gpt-4o", temperature=0)

    # Create agents
    researcher = Agent(
        role='Research Analyst',
        goal='Find and analyze the best investment opportunities',
        backstory='Expert in financial analysis and market research',
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role='Report Writer',
        goal='Write clear and concise investment reports',
        backstory='Experienced in creating detailed financial reports',
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    # Create tasks
    research_task = Task(
        description='Deep research on the {topic}',
        expected_output='Comprehensive market data including key players, market size, and growth trends.',
        agent=researcher
    )

    writing_task = Task(
        description='Write a detailed report based on the research',
        expected_output='The report should be easy to read and understand. Use bullet points where applicable.',
        agent=writer
    )

    # Create a crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True,
        process=Process.sequential,
    )

    # Run the crew
    result = crew.kickoff(inputs={"topic": "AI in material science"})
    print(result)
    ```
  </Step>

  <Step title="View Traces in Weave">
    After running your CrewAI application, visit the Weave URL provided during initialization to view:

    * LLM calls and their metadata
    * Agent interactions and task execution flow
    * Performance metrics like latency and token usage
    * Any errors or issues that occurred during execution

    <Frame caption="Weave Tracing Dashboard">
      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f59e556fcc0ac8fcca8eaeef4c0551ae" alt="Weave tracing example with CrewAI" data-og-width="3456" width="3456" data-og-height="1986" height="1986" data-path="images/weave-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=42efb320cedff3209765027d4f47e187 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=85318181f2afd6237c71cecedfda8104 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6124c3113060320d39847c47faa02ac4 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e04300ff38ddf3624acc078bacf6712e 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c0ba473c3fa41c2939df4e28bc1098b5 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6d860d735bc5a42fb68085fc4ef01b2c 2500w" />
    </Frame>
  </Step>
</Steps>


## Features

* Weave automatically captures all CrewAI operations: agent interactions and task executions; LLM calls with metadata and token usage; tool usage and results.
* The integration supports all CrewAI execution methods: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.
* Automatic tracing of all [crewAI-tools](https://github.com/crewAIInc/crewAI-tools).
* Flow feature support with decorator patching (`@start`, `@listen`, `@router`, `@or_`, `@and_`).
* Track custom guardrails passed to CrewAI `Task` with `@weave.op()`.

For detailed information on what's supported, visit the [Weave CrewAI documentation](https://weave-docs.wandb.ai/guides/integrations/crewai/#getting-started-with-flow).


## Resources

* [📘 Weave Documentation](https://weave-docs.wandb.ai)
* [📊 Example Weave x CrewAI dashboard](https://wandb.ai/ayut/crewai_demo/weave/traces?cols=%7B%22wb_run_id%22%3Afalse%2C%22attributes.weave.client_version%22%3Afalse%2C%22attributes.weave.os_name%22%3Afalse%2C%22attributes.weave.os_release%22%3Afalse%2C%22attributes.weave.os_version%22%3Afalse%2C%22attributes.weave.source%22%3Afalse%2C%22attributes.weave.sys_version%22%3Afalse%7D\&peekPath=%2Fayut%2Fcrewai_demo%2Fcalls%2F0195c838-38cb-71a2-8a15-651ecddf9d89)
* [🐦 X](https://x.com/weave_wb)



# Telemetry
Source: https://docs.crewai.com/en/telemetry

Understanding the telemetry data collected by CrewAI and how it contributes to the enhancement of the library.


## Telemetry

<Note>
  By default, we collect no data that would be considered personal information under GDPR and other privacy regulations.
  We do collect Tool's names and Agent's roles, so be advised not to include any personal information in the tool's names or the Agent's roles.
  Because no personal information is collected, it's not necessary to worry about data residency.
  When `share_crew` is enabled, additional data is collected which may contain personal information if included by the user.
  Users should exercise caution when enabling this feature to ensure compliance with privacy regulations.
</Note>

CrewAI utilizes anonymous telemetry to gather usage statistics with the primary goal of enhancing the library.
Our focus is on improving and developing the features, integrations, and tools most utilized by our users.

It's pivotal to understand that by default, **NO personal data is collected** concerning prompts, task descriptions, agents' backstories or goals,
usage of tools, API calls, responses, any data processed by the agents, or secrets and environment variables.
When the `share_crew` feature is enabled, detailed data including task descriptions, agents' backstories or goals, and other specific attributes are collected
to provide deeper insights. This expanded data collection may include personal information if users have incorporated it into their crews or tasks.
Users should carefully consider the content of their crews and tasks before enabling `share_crew`.
Users can disable telemetry by setting the environment variable `CREWAI_DISABLE_TELEMETRY` to `true` or by setting `OTEL_SDK_DISABLED` to `true` (note that the latter disables all OpenTelemetry instrumentation globally).

### Examples:

```python  theme={null}

# Disable CrewAI telemetry only
os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'


# Disable all OpenTelemetry (including CrewAI)
os.environ['OTEL_SDK_DISABLED'] = 'true'
```

### Data Explanation:

| Defaulted | Data                                     | Reason and Specifics                                                                                                                                                                                                                                                                                             |
| :-------- | :--------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes       | CrewAI and Python Version                | Tracks software versions. Example: CrewAI v1.2.3, Python 3.8.10. No personal data.                                                                                                                                                                                                                               |
| Yes       | Crew Metadata                            | Includes: randomly generated key and ID, process type (e.g., 'sequential', 'parallel'), boolean flag for memory usage (true/false), count of tasks, count of agents. All non-personal.                                                                                                                           |
| Yes       | Agent Data                               | Includes: randomly generated key and ID, role name (should not include personal info), boolean settings (verbose, delegation enabled, code execution allowed), max iterations, max RPM, max retry limit, LLM info (see LLM Attributes), list of tool names (should not include personal info). No personal data. |
| Yes       | Task Metadata                            | Includes: randomly generated key and ID, boolean execution settings (async\_execution, human\_input), associated agent's role and key, list of tool names. All non-personal.                                                                                                                                     |
| Yes       | Tool Usage Statistics                    | Includes: tool name (should not include personal info), number of usage attempts (integer), LLM attributes used. No personal data.                                                                                                                                                                               |
| Yes       | Test Execution Data                      | Includes: crew's randomly generated key and ID, number of iterations, model name used, quality score (float), execution time (in seconds). All non-personal.                                                                                                                                                     |
| Yes       | Task Lifecycle Data                      | Includes: creation and execution start/end times, crew and task identifiers. Stored as spans with timestamps. No personal data.                                                                                                                                                                                  |
| Yes       | LLM Attributes                           | Includes: name, model\_name, model, top\_k, temperature, and class name of the LLM. All technical, non-personal data.                                                                                                                                                                                            |
| Yes       | Crew Deployment attempt using crewAI CLI | Includes: The fact a deploy is being made and crew id, and if it's trying to pull logs, no other data.                                                                                                                                                                                                           |
| No        | Agent's Expanded Data                    | Includes: goal description, backstory text, i18n prompt file identifier. Users should ensure no personal info is included in text fields.                                                                                                                                                                        |
| No        | Detailed Task Information                | Includes: task description, expected output description, context references. Users should ensure no personal info is included in these fields.                                                                                                                                                                   |
| No        | Environment Information                  | Includes: platform, release, system, version, and CPU count. Example: 'Windows 10', 'x86\_64'. No personal data.                                                                                                                                                                                                 |
| No        | Crew and Task Inputs and Outputs         | Includes: input parameters and output results as non-identifiable data. Users should ensure no personal info is included.                                                                                                                                                                                        |
| No        | Comprehensive Crew Execution Data        | Includes: detailed logs of crew operations, all agents and tasks data, final output. All non-personal and technical in nature.                                                                                                                                                                                   |

<Note>
  "No" in the "Defaulted" column indicates that this data is only collected when `share_crew` is set to `true`.
</Note>

### Opt-In Further Telemetry Sharing

Users can choose to share their complete telemetry data by enabling the `share_crew` attribute to `True` in their crew configurations.
Enabling `share_crew` results in the collection of detailed crew and task execution data, including `goal`, `backstory`, `context`, and `output` of tasks.
This enables a deeper insight into usage patterns.

<Warning>
  If you enable `share_crew`, the collected data may include personal information if it has been incorporated into crew configurations, task descriptions, or outputs.
  Users should carefully review their data and ensure compliance with GDPR and other applicable privacy regulations before enabling this feature.
</Warning>



# Apify Actors
Source: https://docs.crewai.com/en/tools/automation/apifyactorstool

`ApifyActorsTool` lets you call Apify Actors to provide your CrewAI workflows with web scraping, crawling, data extraction, and web automation capabilities.


# `ApifyActorsTool`

Integrate [Apify Actors](https://apify.com/actors) into your CrewAI workflows.


## Description

The `ApifyActorsTool` connects [Apify Actors](https://apify.com/actors), cloud-based programs for web scraping and automation, to your CrewAI workflows.
Use any of the 4,000+ Actors on [Apify Store](https://apify.com/store) for use cases such as extracting data from social media, search engines, online maps, e-commerce sites, travel portals, or general websites.

For details, see the [Apify CrewAI integration](https://docs.apify.com/platform/integrations/crewai) in Apify documentation.


## Steps to get started

<Steps>
  <Step title="Install dependencies">
    Install `crewai[tools]` and `langchain-apify` using pip: `pip install 'crewai[tools]' langchain-apify`.
  </Step>

  <Step title="Obtain an Apify API token">
    Sign up to [Apify Console](https://console.apify.com/) and get your [Apify API token](https://console.apify.com/settings/integrations)..
  </Step>

  <Step title="Configure environment">
    Set your Apify API token as the `APIFY_API_TOKEN` environment variable to enable the tool's functionality.
  </Step>
</Steps>


## Usage example

Use the `ApifyActorsTool` manually to run the [RAG Web Browser Actor](https://apify.com/apify/rag-web-browser) to perform a web search:

```python  theme={null}
from crewai_tools import ApifyActorsTool


# Initialize the tool with an Apify Actor
tool = ApifyActorsTool(actor_name="apify/rag-web-browser")


# Run the tool with input parameters
results = tool.run(run_input={"query": "What is CrewAI?", "maxResults": 5})


# Process the results
for result in results:
    print(f"URL: {result['metadata']['url']}")
    print(f"Content: {result.get('markdown', 'N/A')[:100]}...")
```

### Expected output

Here is the output from running the code above:

```text  theme={null}
URL: https://www.example.com/crewai-intro
Content: CrewAI is a framework for building AI-powered workflows...
URL: https://docs.crewai.com/
Content: Official documentation for CrewAI...
```

The `ApifyActorsTool` automatically fetches the Actor definition and input schema from Apify using the provided `actor_name` and then constructs the tool description and argument schema. This means you need to specify only a valid `actor_name`, and the tool handles the rest when used with agents—no need to specify the `run_input`. Here's how it works:

```python  theme={null}
from crewai import Agent
from crewai_tools import ApifyActorsTool

rag_browser = ApifyActorsTool(actor_name="apify/rag-web-browser")

agent = Agent(
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="You are an experienced researcher with attention to detail",
    tools=[rag_browser],
)
```

You can run other Actors from [Apify Store](https://apify.com/store) simply by changing the `actor_name` and, when using it manually, adjusting the `run_input` based on the Actor input schema.

For an example of usage with agents, see the [CrewAI Actor template](https://apify.com/templates/python-crewai).


## Configuration

The `ApifyActorsTool` requires these inputs to work:

* **`actor_name`**
  The ID of the Apify Actor to run, e.g., `"apify/rag-web-browser"`. Browse all Actors on [Apify Store](https://apify.com/store).
* **`run_input`**
  A dictionary of input parameters for the Actor when running the tool manually.
  * For example, for the `apify/rag-web-browser` Actor: `{"query": "search term", "maxResults": 5}`
  * See the Actor's [input schema](https://apify.com/apify/rag-web-browser/input-schema) for the list of input parameters.


## Resources

* **[Apify](https://apify.com/)**: Explore the Apify platform.
* **[How to build an AI agent on Apify](https://blog.apify.com/how-to-build-an-ai-agent/)** - A complete step-by-step guide to creating, publishing, and monetizing AI agents on the Apify platform.
* **[RAG Web Browser Actor](https://apify.com/apify/rag-web-browser)**: A popular Actor for web search for LLMs.
* **[CrewAI Integration Guide](https://docs.apify.com/platform/integrations/crewai)**: Follow the official guide for integrating Apify and CrewAI.



# Composio Tool
Source: https://docs.crewai.com/en/tools/automation/composiotool

Composio provides 250+ production-ready tools for AI agents with flexible authentication management.


# `ComposioToolSet`


## Description

Composio is an integration platform that allows you to connect your AI agents to 250+ tools. Key features include:

* **Enterprise-Grade Authentication**: Built-in support for OAuth, API Keys, JWT with automatic token refresh
* **Full Observability**: Detailed tool usage logs, execution timestamps, and more


## Installation

To incorporate Composio tools into your project, follow the instructions below:

```shell  theme={null}
pip install composio-crewai
pip install crewai
```

After the installation is complete, either run `composio login` or export your composio API key as `COMPOSIO_API_KEY`. Get your Composio API key from [here](https://app.composio.dev)


## Example

The following example demonstrates how to initialize the tool and execute a github action:

1. Initialize Composio toolset

```python Code theme={null}
from composio_crewai import ComposioToolSet, App, Action
from crewai import Agent, Task, Crew

toolset = ComposioToolSet()
```

2. Connect your GitHub account

<CodeGroup>
  ```shell CLI theme={null}
  composio add github
  ```

  ```python Code theme={null}
  request = toolset.initiate_connection(app=App.GITHUB)
  print(f"Open this URL to authenticate: {request.redirectUrl}")
  ```
</CodeGroup>

3. Get Tools

* Retrieving all the tools from an app (not recommended for production):

```python Code theme={null}
tools = toolset.get_tools(apps=[App.GITHUB])
```

* Filtering tools based on tags:

```python Code theme={null}
tag = "users"

filtered_action_enums = toolset.find_actions_by_tags(
    App.GITHUB,
    tags=[tag], 
)

tools = toolset.get_tools(actions=filtered_action_enums)
```

* Filtering tools based on use case:

```python Code theme={null}
use_case = "Star a repository on GitHub"

filtered_action_enums = toolset.find_actions_by_use_case(
    App.GITHUB, use_case=use_case, advanced=False
)

tools = toolset.get_tools(actions=filtered_action_enums)
```

<Tip>Set `advanced` to True to get actions for complex use cases</Tip>

* Using specific tools:

In this demo, we will use the `GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER` action from the GitHub app.

```python Code theme={null}
tools = toolset.get_tools(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)
```

Learn more about filtering actions [here](https://docs.composio.dev/patterns/tools/use-tools/use-specific-actions)

4. Define agent

```python Code theme={null}
crewai_agent = Agent(
    role="GitHub Agent",
    goal="You take action on GitHub using GitHub APIs",
    backstory="You are AI agent that is responsible for taking actions on GitHub on behalf of users using GitHub APIs",
    verbose=True,
    tools=tools,
    llm= # pass an llm
)
```

5. Execute task

```python Code theme={null}
task = Task(
    description="Star a repo composiohq/composio on GitHub",
    agent=crewai_agent,
    expected_output="Status of the operation",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

crew.kickoff()
```

* More detailed list of tools can be found [here](https://app.composio.dev)



# MultiOn Tool
Source: https://docs.crewai.com/en/tools/automation/multiontool

The `MultiOnTool` empowers CrewAI agents with the capability to navigate and interact with the web through natural language instructions.


## Overview

The `MultiOnTool` is designed to wrap [MultiOn's](https://docs.multion.ai/welcome) web browsing capabilities, enabling CrewAI agents to control web browsers using natural language instructions. This tool facilitates seamless web browsing, making it an essential asset for projects requiring dynamic web data interaction and automation of web-based tasks.


## Installation

To use this tool, you need to install the MultiOn package:

```shell  theme={null}
uv add multion
```

You'll also need to install the MultiOn browser extension and enable API usage.


## Steps to Get Started

To effectively use the `MultiOnTool`, follow these steps:

1. **Install CrewAI**: Ensure that the `crewai[tools]` package is installed in your Python environment.
2. **Install and use MultiOn**: Follow [MultiOn documentation](https://docs.multion.ai/learn/browser-extension) for installing the MultiOn Browser Extension.
3. **Enable API Usage**: Click on the MultiOn extension in the extensions folder of your browser (not the hovering MultiOn icon on the web page) to open the extension configurations. Click the API Enabled toggle to enable the API.


## Example

The following example demonstrates how to initialize the tool and execute a web browsing task:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import MultiOnTool


# Initialize the tool
multion_tool = MultiOnTool(api_key="YOUR_MULTION_API_KEY", local=False)


# Define an agent that uses the tool
browser_agent = Agent(
    role="Browser Agent",
    goal="Control web browsers using natural language",
    backstory="An expert browsing agent.",
    tools=[multion_tool],
    verbose=True,
)


# Example task to search and summarize news
browse_task = Task(
    description="Summarize the top 3 trending AI News headlines",
    expected_output="A summary of the top 3 trending AI News headlines",
    agent=browser_agent,
)


# Create and run the crew
crew = Crew(agents=[browser_agent], tasks=[browse_task])
result = crew.kickoff()
```


## Parameters

The `MultiOnTool` accepts the following parameters during initialization:

* **api\_key**: Optional. Specifies the MultiOn API key. If not provided, it will look for the `MULTION_API_KEY` environment variable.
* **local**: Optional. Set to `True` to run the agent locally on your browser. Make sure the MultiOn browser extension is installed and API Enabled is checked. Default is `False`.
* **max\_steps**: Optional. Sets the maximum number of steps the MultiOn agent can take for a command. Default is `3`.


## Usage

When using the `MultiOnTool`, the agent will provide natural language instructions that the tool translates into web browsing actions. The tool returns the results of the browsing session along with a status.

```python Code theme={null}

# Example of using the tool with an agent
browser_agent = Agent(
    role="Web Browser Agent",
    goal="Search for and summarize information from the web",
    backstory="An expert at finding and extracting information from websites.",
    tools=[multion_tool],
    verbose=True,
)


# Create a task for the agent
search_task = Task(
    description="Search for the latest AI news on TechCrunch and summarize the top 3 headlines",
    expected_output="A summary of the top 3 AI news headlines from TechCrunch",
    agent=browser_agent,
)


# Run the task
crew = Crew(agents=[browser_agent], tasks=[search_task])
result = crew.kickoff()
```

If the status returned is `CONTINUE`, the agent should be instructed to reissue the same instruction to continue execution.


## Implementation Details

The `MultiOnTool` is implemented as a subclass of `BaseTool` from CrewAI. It wraps the MultiOn client to provide web browsing capabilities:

```python Code theme={null}
class MultiOnTool(BaseTool):
    """Tool to wrap MultiOn Browse Capabilities."""

    name: str = "Multion Browse Tool"
    description: str = """Multion gives the ability for LLMs to control web browsers using natural language instructions.
            If the status is 'CONTINUE', reissue the same instruction to continue execution
        """
    
    # Implementation details...
    
    def _run(self, cmd: str, *args: Any, **kwargs: Any) -> str:
        """
        Run the Multion client with the given command.
        
        Args:
            cmd (str): The detailed and specific natural language instruction for web browsing
            *args (Any): Additional arguments to pass to the Multion client
            **kwargs (Any): Additional keyword arguments to pass to the Multion client
        """
        # Implementation details...
```


## Conclusion

The `MultiOnTool` provides a powerful way to integrate web browsing capabilities into CrewAI agents. By enabling agents to interact with websites through natural language instructions, it opens up a wide range of possibilities for web-based tasks, from data collection and research to automated interactions with web services.



# Overview
Source: https://docs.crewai.com/en/tools/automation/overview

Automate workflows and integrate with external platforms and services

These tools enable your agents to automate workflows, integrate with external platforms, and connect with various third-party services for enhanced functionality.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="Apify Actor Tool" icon="spider" href="/en/tools/automation/apifyactorstool">
    Run Apify actors for web scraping and automation tasks.
  </Card>

  <Card title="Composio Tool" icon="puzzle-piece" href="/en/tools/automation/composiotool">
    Integrate with hundreds of apps and services through Composio.
  </Card>

  <Card title="Multion Tool" icon="window-restore" href="/en/tools/automation/multiontool">
    Automate browser interactions and web-based workflows.
  </Card>

  <Card title="Zapier Actions Adapter" icon="bolt" href="/en/tools/automation/zapieractionstool">
    Expose Zapier Actions as CrewAI tools for automation across thousands of apps.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Workflow Automation**: Automate repetitive tasks and processes
* **API Integration**: Connect with external APIs and services
* **Data Synchronization**: Sync data between different platforms
* **Process Orchestration**: Coordinate complex multi-step workflows
* **Third-party Services**: Leverage external tools and platforms

```python  theme={null}
from crewai_tools import ApifyActorTool, ComposioTool, MultiOnTool


# Create automation tools
apify_automation = ApifyActorTool()
platform_integration = ComposioTool()
browser_automation = MultiOnTool()


# Add to your agent
agent = Agent(
    role="Automation Specialist",
    tools=[apify_automation, platform_integration, browser_automation],
    goal="Automate workflows and integrate systems"
)
```


## **Integration Benefits**

* **Efficiency**: Reduce manual work through automation
* **Scalability**: Handle increased workloads automatically
* **Reliability**: Consistent execution of workflows
* **Connectivity**: Bridge different systems and platforms
* **Productivity**: Focus on high-value tasks while automation handles routine work



# Zapier Actions Tool
Source: https://docs.crewai.com/en/tools/automation/zapieractionstool

The `ZapierActionsAdapter` exposes Zapier actions as CrewAI tools for automation.


# `ZapierActionsAdapter`


## Description

Use the Zapier adapter to list and call Zapier actions as CrewAI tools. This enables agents to trigger automations across thousands of apps.


## Installation

This adapter is included with `crewai-tools`. No extra install required.


## Environment Variables

* `ZAPIER_API_KEY` (required): Zapier API key. Get one from the Zapier Actions dashboard at [https://actions.zapier.com/](https://actions.zapier.com/) (create an account, then generate an API key). You can also pass `zapier_api_key` directly when constructing the adapter.


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.adapters.zapier_adapter import ZapierActionsAdapter

adapter = ZapierActionsAdapter(api_key="your_zapier_api_key")
tools = adapter.tools()

agent = Agent(
    role="Automator",
    goal="Execute Zapier actions",
    backstory="Automation specialist",
    tools=tools,
    verbose=True,
)

task = Task(
    description="Create a new Google Sheet and add a row using Zapier actions",
    expected_output="Confirmation with created resource IDs",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```


## Notes & limits

* The adapter lists available actions for your key and creates `BaseTool` wrappers dynamically.
* Handle action‑specific required fields in your task instructions or tool call.
* Rate limits depend on your Zapier plan; see the Zapier Actions docs.


## Notes

* The adapter fetches available actions and generates `BaseTool` wrappers dynamically.



# Bedrock Invoke Agent Tool
Source: https://docs.crewai.com/en/tools/integration/bedrockinvokeagenttool

Enables CrewAI agents to invoke Amazon Bedrock Agents and leverage their capabilities within your workflows


# `BedrockInvokeAgentTool`

The `BedrockInvokeAgentTool` enables CrewAI agents to invoke Amazon Bedrock Agents and leverage their capabilities within your workflows.


## Installation

```bash  theme={null}
uv pip install 'crewai[tools]'
```


## Requirements

* AWS credentials configured (either through environment variables or AWS CLI)
* `boto3` and `python-dotenv` packages
* Access to Amazon Bedrock Agents


## Usage

Here's how to use the tool with a CrewAI agent:

```python {2, 4-8} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools.aws.bedrock.agents.invoke_agent_tool import BedrockInvokeAgentTool


# Initialize the tool
agent_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id"
)


# Create a CrewAI agent that uses the tool
aws_expert = Agent(
    role='AWS Service Expert',
    goal='Help users understand AWS services and quotas',
    backstory='I am an expert in AWS services and can provide detailed information about them.',
    tools=[agent_tool],
    verbose=True
)


# Create a task for the agent
quota_task = Task(
    description="Find out the current service quotas for EC2 in us-west-2 and explain any recent changes.",
    agent=aws_expert
)


# Create a crew with the agent
crew = Crew(
    agents=[aws_expert],
    tasks=[quota_task],
    verbose=2
)


# Run the crew
result = crew.kickoff()
print(result)
```


## Tool Arguments

| Argument             | Type   | Required | Default   | Description                                 |
| :------------------- | :----- | :------- | :-------- | :------------------------------------------ |
| **agent\_id**        | `str`  | Yes      | None      | The unique identifier of the Bedrock agent  |
| **agent\_alias\_id** | `str`  | Yes      | None      | The unique identifier of the agent alias    |
| **session\_id**      | `str`  | No       | timestamp | The unique identifier of the session        |
| **enable\_trace**    | `bool` | No       | False     | Whether to enable trace for debugging       |
| **end\_session**     | `bool` | No       | False     | Whether to end the session after invocation |
| **description**      | `str`  | No       | None      | Custom description for the tool             |


## Environment Variables

```bash  theme={null}
BEDROCK_AGENT_ID=your-agent-id           # Alternative to passing agent_id
BEDROCK_AGENT_ALIAS_ID=your-agent-alias-id # Alternative to passing agent_alias_id
AWS_REGION=your-aws-region               # Defaults to us-west-2
AWS_ACCESS_KEY_ID=your-access-key        # Required for AWS authentication
AWS_SECRET_ACCESS_KEY=your-secret-key    # Required for AWS authentication
```


## Advanced Usage

### Multi-Agent Workflow with Session Management

```python {2, 4-22} theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools.aws.bedrock.agents.invoke_agent_tool import BedrockInvokeAgentTool


# Initialize tools with session management
initial_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id"
)

followup_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id"
)

final_tool = BedrockInvokeAgentTool(
    agent_id="your-agent-id",
    agent_alias_id="your-agent-alias-id",
    session_id="custom-session-id",
    end_session=True
)


# Create agents for different stages
researcher = Agent(
    role='AWS Service Researcher',
    goal='Gather information about AWS services',
    backstory='I am specialized in finding detailed AWS service information.',
    tools=[initial_tool]
)

analyst = Agent(
    role='Service Compatibility Analyst',
    goal='Analyze service compatibility and requirements',
    backstory='I analyze AWS services for compatibility and integration possibilities.',
    tools=[followup_tool]
)

summarizer = Agent(
    role='Technical Documentation Writer',
    goal='Create clear technical summaries',
    backstory='I specialize in creating clear, concise technical documentation.',
    tools=[final_tool]
)


# Create tasks
research_task = Task(
    description="Find all available AWS services in us-west-2 region.",
    agent=researcher
)

analysis_task = Task(
    description="Analyze which services support IPv6 and their implementation requirements.",
    agent=analyst
)

summary_task = Task(
    description="Create a summary of IPv6-compatible services and their key features.",
    agent=summarizer
)


# Create a crew with the agents and tasks
crew = Crew(
    agents=[researcher, analyst, summarizer],
    tasks=[research_task, analysis_task, summary_task],
    process=Process.sequential,
    verbose=2
)


# Run the crew
result = crew.kickoff()
```


## Use Cases

### Hybrid Multi-Agent Collaborations

* Create workflows where CrewAI agents collaborate with managed Bedrock agents running as services in AWS
* Enable scenarios where sensitive data processing happens within your AWS environment while other agents operate externally
* Bridge on-premises CrewAI agents with cloud-based Bedrock agents for distributed intelligence workflows

### Data Sovereignty and Compliance

* Keep data-sensitive agentic workflows within your AWS environment while allowing external CrewAI agents to orchestrate tasks
* Maintain compliance with data residency requirements by processing sensitive information only within your AWS account
* Enable secure multi-agent collaborations where some agents cannot access your organization's private data

### Seamless AWS Service Integration

* Access any AWS service through Amazon Bedrock Actions without writing complex integration code
* Enable CrewAI agents to interact with AWS services through natural language requests
* Leverage pre-built Bedrock agent capabilities to interact with AWS services like Bedrock Knowledge Bases, Lambda, and more

### Scalable Hybrid Agent Architectures

* Offload computationally intensive tasks to managed Bedrock agents while lightweight tasks run in CrewAI
* Scale agent processing by distributing workloads between local CrewAI agents and cloud-based Bedrock agents

### Cross-Organizational Agent Collaboration

* Enable secure collaboration between your organization's CrewAI agents and partner organizations' Bedrock agents
* Create workflows where external expertise from Bedrock agents can be incorporated without exposing sensitive data
* Build agent ecosystems that span organizational boundaries while maintaining security and data control



# CrewAI Run Automation Tool
Source: https://docs.crewai.com/en/tools/integration/crewaiautomationtool

Enables CrewAI agents to invoke CrewAI Platform automations and leverage external crew services within your workflows.


# `InvokeCrewAIAutomationTool`

The `InvokeCrewAIAutomationTool` provides CrewAI Platform API integration with external crew services. This tool allows you to invoke and interact with CrewAI Platform automations from within your CrewAI agents, enabling seamless integration between different crew workflows.


## Installation

```bash  theme={null}
uv pip install 'crewai[tools]'
```


## Requirements

* CrewAI Platform API access
* Valid bearer token for authentication
* Network access to CrewAI Platform automation endpoints


## Usage

Here's how to use the tool with a CrewAI agent:

```python {2, 4-9} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import InvokeCrewAIAutomationTool


# Initialize the tool
automation_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://data-analysis-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Data Analysis Crew",
    crew_description="Analyzes data and generates insights"
)


# Create a CrewAI agent that uses the tool
automation_coordinator = Agent(
    role='Automation Coordinator',
    goal='Coordinate and execute automated crew tasks',
    backstory='I am an expert at leveraging automation tools to execute complex workflows.',
    tools=[automation_tool],
    verbose=True
)


# Create a task for the agent
analysis_task = Task(
    description="Execute data analysis automation and provide insights",
    agent=automation_coordinator,
    expected_output="Comprehensive data analysis report"
)


# Create a crew with the agent
crew = Crew(
    agents=[automation_coordinator],
    tasks=[analysis_task],
    verbose=2
)


# Run the crew
result = crew.kickoff()
print(result)
```


## Tool Arguments

| Argument                | Type   | Required | Default | Description                                         |
| :---------------------- | :----- | :------- | :------ | :-------------------------------------------------- |
| **crew\_api\_url**      | `str`  | Yes      | None    | Base URL of the CrewAI Platform automation API      |
| **crew\_bearer\_token** | `str`  | Yes      | None    | Bearer token for API authentication                 |
| **crew\_name**          | `str`  | Yes      | None    | Name of the crew automation                         |
| **crew\_description**   | `str`  | Yes      | None    | Description of what the crew automation does        |
| **max\_polling\_time**  | `int`  | No       | 600     | Maximum time in seconds to wait for task completion |
| **crew\_inputs**        | `dict` | No       | None    | Dictionary defining custom input schema fields      |


## Environment Variables

```bash  theme={null}
CREWAI_API_URL=https://your-crew-automation.crewai.com  # Alternative to passing crew_api_url
CREWAI_BEARER_TOKEN=your_bearer_token_here              # Alternative to passing crew_bearer_token
```


## Advanced Usage

### Custom Input Schema with Dynamic Parameters

```python {2, 4-15} theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import InvokeCrewAIAutomationTool
from pydantic import Field


# Define custom input schema
custom_inputs = {
    "year": Field(..., description="Year to retrieve the report for (integer)"),
    "region": Field(default="global", description="Geographic region for analysis"),
    "format": Field(default="summary", description="Report format (summary, detailed, raw)")
}


# Create tool with custom inputs
market_research_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://state-of-ai-report-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="State of AI Report",
    crew_description="Retrieves a comprehensive report on state of AI for a given year and region",
    crew_inputs=custom_inputs,
    max_polling_time=15 * 60  # 15 minutes timeout
)


# Create an agent with the tool
research_agent = Agent(
    role="Research Coordinator",
    goal="Coordinate and execute market research tasks",
    backstory="You are an expert at coordinating research tasks and leveraging automation tools.",
    tools=[market_research_tool],
    verbose=True
)


# Create and execute a task with custom parameters
research_task = Task(
    description="Conduct market research on AI tools market for 2024 in North America with detailed format",
    agent=research_agent,
    expected_output="Comprehensive market research report"
)

crew = Crew(
    agents=[research_agent],
    tasks=[research_task]
)

result = crew.kickoff()
```

### Multi-Stage Automation Workflow

```python {2, 4-35} theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import InvokeCrewAIAutomationTool


# Initialize different automation tools
data_collection_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://data-collection-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Data Collection Automation",
    crew_description="Collects and preprocesses raw data"
)

analysis_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://analysis-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Analysis Automation",
    crew_description="Performs advanced data analysis and modeling"
)

reporting_tool = InvokeCrewAIAutomationTool(
    crew_api_url="https://reporting-crew-[...].crewai.com",
    crew_bearer_token="your_bearer_token_here",
    crew_name="Reporting Automation",
    crew_description="Generates comprehensive reports and visualizations"
)


# Create specialized agents
data_collector = Agent(
    role='Data Collection Specialist',
    goal='Gather and preprocess data from various sources',
    backstory='I specialize in collecting and cleaning data from multiple sources.',
    tools=[data_collection_tool]
)

data_analyst = Agent(
    role='Data Analysis Expert',
    goal='Perform advanced analysis on collected data',
    backstory='I am an expert in statistical analysis and machine learning.',
    tools=[analysis_tool]
)

report_generator = Agent(
    role='Report Generation Specialist',
    goal='Create comprehensive reports and visualizations',
    backstory='I excel at creating clear, actionable reports from complex data.',
    tools=[reporting_tool]
)


# Create sequential tasks
collection_task = Task(
    description="Collect market data for Q4 2024 analysis",
    agent=data_collector
)

analysis_task = Task(
    description="Analyze collected data to identify trends and patterns",
    agent=data_analyst
)

reporting_task = Task(
    description="Generate executive summary report with key insights and recommendations",
    agent=report_generator
)


# Create a crew with sequential processing
crew = Crew(
    agents=[data_collector, data_analyst, report_generator],
    tasks=[collection_task, analysis_task, reporting_task],
    process=Process.sequential,
    verbose=2
)

result = crew.kickoff()
```


## Use Cases

### Distributed Crew Orchestration

* Coordinate multiple specialized crew automations to handle complex, multi-stage workflows
* Enable seamless handoffs between different automation services for comprehensive task execution
* Scale processing by distributing workloads across multiple CrewAI Platform automations

### Cross-Platform Integration

* Bridge CrewAI agents with CrewAI Platform automations for hybrid local-cloud workflows
* Leverage specialized automations while maintaining local control and orchestration
* Enable secure collaboration between local agents and cloud-based automation services

### Enterprise Automation Pipelines

* Create enterprise-grade automation pipelines that combine local intelligence with cloud processing power
* Implement complex business workflows that span multiple automation services
* Enable scalable, repeatable processes for data analysis, reporting, and decision-making

### Dynamic Workflow Composition

* Dynamically compose workflows by chaining different automation services based on task requirements
* Enable adaptive processing where the choice of automation depends on data characteristics or business rules
* Create flexible, reusable automation components that can be combined in various ways

### Specialized Domain Processing

* Access domain-specific automations (financial analysis, legal research, technical documentation) from general-purpose agents
* Leverage pre-built, specialized crew automations without rebuilding complex domain logic
* Enable agents to access expert-level capabilities through targeted automation services


## Custom Input Schema

When defining `crew_inputs`, use Pydantic Field objects to specify the input parameters:

```python  theme={null}
from pydantic import Field

crew_inputs = {
    "required_param": Field(..., description="This parameter is required"),
    "optional_param": Field(default="default_value", description="This parameter is optional"),
    "typed_param": Field(..., description="Integer parameter", ge=1, le=100)  # With validation
}
```


## Error Handling

The tool provides comprehensive error handling for common scenarios:

* **API Connection Errors**: Network connectivity issues with CrewAI Platform
* **Authentication Errors**: Invalid or expired bearer tokens
* **Timeout Errors**: Tasks that exceed the maximum polling time
* **Task Failures**: Crew automations that fail during execution
* **Input Validation Errors**: Invalid parameters passed to automation endpoints


## API Endpoints

The tool interacts with two main API endpoints:

* `POST {crew_api_url}/kickoff`: Starts a new crew automation task
* `GET {crew_api_url}/status/{crew_id}`: Checks the status of a running task


## Notes

* The tool automatically polls the status endpoint every second until completion or timeout
* Successful tasks return the result directly, while failed tasks return error information
* Bearer tokens should be kept secure and not hardcoded in production environments
* Consider using environment variables for sensitive configuration like bearer tokens
* Custom input schemas must be compatible with the target crew automation's expected parameters



# Overview
Source: https://docs.crewai.com/en/tools/integration/overview

Connect CrewAI agents with external automations and managed AI services

Integration tools let your agents hand off work to other automation platforms and managed AI services. Use them when a workflow needs to invoke an existing CrewAI deployment or delegate specialised tasks to providers such as Amazon Bedrock.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="CrewAI Run Automation Tool" icon="robot" href="/en/tools/integration/crewaiautomationtool">
    Invoke live CrewAI Platform automations, pass custom inputs, and poll for results directly from your agent.
  </Card>

  <Card title="Bedrock Invoke Agent Tool" icon="aws" href="/en/tools/integration/bedrockinvokeagenttool">
    Call Amazon Bedrock Agents from your crews, reuse AWS guardrails, and stream responses back into the workflow.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Chain automations**: Kick off an existing CrewAI deployment from within another crew or flow
* **Enterprise hand-off**: Route tasks to Bedrock Agents that already encapsulate company logic and guardrails
* **Hybrid workflows**: Combine CrewAI reasoning with downstream systems that expose their own agent APIs
* **Long-running jobs**: Poll external automations and merge the final results back into the current run


## **Quick Start Example**

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import InvokeCrewAIAutomationTool
from crewai_tools.aws.bedrock.agents.invoke_agent_tool import BedrockInvokeAgentTool


# External automation
analysis_automation = InvokeCrewAIAutomationTool(
    crew_api_url="https://analysis-crew.acme.crewai.com",
    crew_bearer_token="YOUR_BEARER_TOKEN",
    crew_name="Analysis Automation",
    crew_description="Runs the production-grade analysis pipeline",
)


# Managed agent on Bedrock
knowledge_router = BedrockInvokeAgentTool(
    agent_id="bedrock-agent-id",
    agent_alias_id="prod",
)

automation_strategist = Agent(
    role="Automation Strategist",
    goal="Orchestrate external automations and summarise their output",
    backstory="You coordinate enterprise workflows and know when to delegate tasks to specialised services.",
    tools=[analysis_automation, knowledge_router],
    verbose=True,
)

execute_playbook = Task(
    description="Run the analysis automation and ask the Bedrock agent for executive talking points.",
    agent=automation_strategist,
)

Crew(agents=[automation_strategist], tasks=[execute_playbook]).kickoff()
```


## **Best Practices**

* **Secure credentials**: Store API keys and bearer tokens in environment variables or a secrets manager
* **Plan for latency**: External automations may take longer—set appropriate polling intervals and timeouts
* **Reuse sessions**: Bedrock Agents support session IDs so you can maintain context across multiple tool calls
* **Validate responses**: Normalise remote output (JSON, text, status codes) before forwarding it to downstream tasks
* **Monitor usage**: Track audit logs in CrewAI Platform or AWS CloudWatch to stay ahead of quota limits and failures



# GET /inputs
Source: https://docs.crewai.com/en/api-reference/inputs

enterprise-api.en.yaml get /inputs
Get required inputs for your crew




# Introduction
Source: https://docs.crewai.com/en/api-reference/introduction

Complete reference for the CrewAI AMP REST API


# CrewAI AMP API

Welcome to the CrewAI AMP API reference. This API allows you to programmatically interact with your deployed crews, enabling integration with your applications, workflows, and services.


## Quick Start

<Steps>
  <Step title="Get Your API Credentials">
    Navigate to your crew's detail page in the CrewAI AMP dashboard and copy your Bearer Token from the Status tab.
  </Step>

  <Step title="Discover Required Inputs">
    Use the `GET /inputs` endpoint to see what parameters your crew expects.
  </Step>

  <Step title="Start a Crew Execution">
    Call `POST /kickoff` with your inputs to start the crew execution and receive a `kickoff_id`.
  </Step>

  <Step title="Monitor Progress">
    Use `GET /status/{kickoff_id}` to check execution status and retrieve results.
  </Step>
</Steps>


## Authentication

All API requests require authentication using a Bearer token. Include your token in the `Authorization` header:

```bash  theme={null}
curl -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  https://your-crew-url.crewai.com/inputs
```

### Token Types

| Token Type            | Scope                     | Use Case                                                     |
| :-------------------- | :------------------------ | :----------------------------------------------------------- |
| **Bearer Token**      | Organization-level access | Full crew operations, ideal for server-to-server integration |
| **User Bearer Token** | User-scoped access        | Limited permissions, suitable for user-specific operations   |

<Tip>
  You can find both token types in the Status tab of your crew's detail page in the CrewAI AMP dashboard.
</Tip>


## Base URL

Each deployed crew has its own unique API endpoint:

```
https://your-crew-name.crewai.com
```

Replace `your-crew-name` with your actual crew's URL from the dashboard.


## Typical Workflow

1. **Discovery**: Call `GET /inputs` to understand what your crew needs
2. **Execution**: Submit inputs via `POST /kickoff` to start processing
3. **Monitoring**: Poll `GET /status/{kickoff_id}` until completion
4. **Results**: Extract the final output from the completed response


## Error Handling

The API uses standard HTTP status codes:

| Code  | Meaning                                    |
| ----- | :----------------------------------------- |
| `200` | Success                                    |
| `400` | Bad Request - Invalid input format         |
| `401` | Unauthorized - Invalid bearer token        |
| `404` | Not Found - Resource doesn't exist         |
| `422` | Validation Error - Missing required inputs |
| `500` | Server Error - Contact support             |


## Interactive Testing

<Info>
  **Why no "Send" button?** Since each CrewAI AMP user has their own unique crew URL, we use **reference mode** instead of an interactive playground to avoid confusion. This shows you exactly what the requests should look like without non-functional send buttons.
</Info>

Each endpoint page shows you:

* ✅ **Exact request format** with all parameters
* ✅ **Response examples** for success and error cases
* ✅ **Code samples** in multiple languages (cURL, Python, JavaScript, etc.)
* ✅ **Authentication examples** with proper Bearer token format

### **To Test Your Actual API:**

<CardGroup cols={2}>
  <Card title="Copy cURL Examples" icon="terminal">
    Copy the cURL examples and replace the URL + token with your real values
  </Card>

  <Card title="Use Postman/Insomnia" icon="play">
    Import the examples into your preferred API testing tool
  </Card>
</CardGroup>

**Example workflow:**

1. **Copy this cURL example** from any endpoint page
2. **Replace `your-actual-crew-name.crewai.com`** with your real crew URL
3. **Replace the Bearer token** with your real token from the dashboard
4. **Run the request** in your terminal or API client


## Need Help?

<CardGroup cols={2}>
  <Card title="Enterprise Support" icon="headset" href="mailto:support@crewai.com">
    Get help with API integration and troubleshooting
  </Card>

  <Card title="Enterprise Dashboard" icon="chart-line" href="https://app.crewai.com">
    Manage your crews and view execution logs
  </Card>
</CardGroup>



# POST /kickoff
Source: https://docs.crewai.com/en/api-reference/kickoff

enterprise-api.en.yaml post /kickoff
Start a crew execution




# POST /resume
Source: https://docs.crewai.com/en/api-reference/resume

enterprise-api.en.yaml post /resume
Resume crew execution with human feedback




# GET /status/{kickoff_id}
Source: https://docs.crewai.com/en/api-reference/status

enterprise-api.en.yaml get /status/{kickoff_id}
Get execution status




# Changelog
Source: https://docs.crewai.com/en/changelog

Product updates, improvements, and bug fixes for CrewAI

<Update label="Sep 30, 2025">
  ## v1.0.0a1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/1.0.0a1)

  ## What's Changed

  ### Core Improvements & Fixes

  * Fixed permission handling for `actions` in agent configuration
  * Updated CI workflows and release publishing to support the new monorepo structure
  * Bumped Python support to 3.13 and refreshed workspace metadata

  ### New Features & Enhancements

  * Added `apps` and `actions` attributes to `Agent` for richer runtime control
  * Merged the `crewai-tools` repository into the main workspace (monorepo)
  * Bumped all packages to 1.0.0a1 to mark the alpha milestone

  ### Cleanup & Infrastructure

  * Delivered a new CI pipeline with version pinning and publishing strategy
  * Unified internal code to manage multiple packages coherently
</Update>

<Update label="Sep 26, 2025">
  ## v0.201.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.201.1)

  ## What's Changed

  ### Core Improvements & Fixes

  * Renamed Watson embedding provider to `watsonx` and refreshed environment variable prefixes
  * Added ChromaDB compatibility for `watsonx` and `voyageai` embedding providers

  ### Cleanup & Deprecations

  * Standardized environment variable prefixes for all embedding providers
  * Bumped CrewAI to 0.201.1 and updated internal dependencies
</Update>

<Update label="Sep 24, 2025">
  ## v0.201.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.201.0)

  ## What's Changed

  ### Core Improvements & Fixes

  * Made the `ready` parameter optional in `_create_reasoning_plan`
  * Fixed nested config handling for embedder configuration
  * Added `batch_size` support to avoid token limit errors
  * Corrected Quickstart documentation directory naming
  * Resolved test duration cache issues and event exports
  * Added fallback logic to crew settings

  ### New Features & Enhancements

  * Introduced thread-safe platform context management
  * Added `crewai uv` wrapper command to run `uv` from the CLI
  * Enabled marking traces as failed for observability workflows
  * Added custom embedding types and provider migration support
  * Upgraded ChromaDB to v1.1.0 with compatibility fixes and type improvements
  * Added Pydantic-compatible import validation and reorganized dependency groups

  ### Documentation & Guides

  * Updated changelog coverage for recent releases (0.193.x series)
  * Documented metadata support for LLM Guardrail events
  * Added guidance for fallback behavior and configuration visibility

  ### Cleanup & Deprecations

  * Resolved Ruff and MyPy issues across modules
  * Improved type annotations and consolidated utilities
  * Deprecated legacy utilities in favor of Pydantic-compatible imports

  ### Contributors

  * @qizwiz (first contribution)
</Update>

<Update label="Sep 20, 2025">
  ## v0.193.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.193.2)

  ## What's Changed

  * Updated pyproject templates to use the right version
</Update>

<Update label="Sep 20, 2025">
  ## v0.193.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.193.1)

  ## What's Changed

  * Series of minor fixes and linter improvements
</Update>

<Update label="Sep 19, 2025">
  ## v0.193.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.193.0)

  ## Core Improvements & Fixes

  * Fixed handling of the `model` parameter during OpenAI adapter initialization
  * Resolved test duration cache issues in CI workflows
  * Fixed flaky test related to repeated tool usage by agents
  * Added missing event exports to `__init__.py` for consistent module behavior
  * Dropped message storage from metadata in Mem0 to reduce bloat
  * Fixed L2 distance metric support for backward compatibility in vector search

  ## New Features & Enhancements

  * Introduced thread-safe platform context management
  * Added test duration caching for optimized `pytest-split` runs
  * Added ephemeral trace improvements for better trace control
  * Made search parameters for RAG, knowledge, and memory fully configurable
  * Enabled ChromaDB to use OpenAI API for embedding functions
  * Added deeper observability tools for user-level insights
  * Unified RAG storage system with instance-specific client support

  ## Documentation & Guides

  * Updated `RagTool` references to reflect CrewAI native RAG implementation
  * Improved internal docs for `langgraph` and `openai` agent adapters with type annotations and docstrings
</Update>

<Update label="Sep 11, 2025">
  ## v0.186.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.186.1)

  ## What's Changed

  * Fixed version not being found and silently failing reversion
  * Bumped CrewAI version to 0.186.1 and updated dependencies in the CLI
</Update>

<Update label="Sep 10, 2025">
  ## v0.186.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.186.0)

  ## What's Changed

  * Refer to the GitHub release notes for detailed changes
</Update>

<Update label="Sep 04, 2025">
  ## v0.177.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.177.0)

  ## Core Improvements & Fixes

  * Achieved parity between `rag` package and current implementation
  * Enhanced LLM event handling with task and agent metadata
  * Fixed mutable default arguments by replacing them with `None`
  * Suppressed Pydantic deprecation warnings during initialization
  * Fixed broken example link in `README.md`
  * Removed Python 3.12+ only Ruff rules for compatibility
  * Migrated CI workflows to use `uv` and updated dev tooling

  ## New Features & Enhancements

  * Added tracing improvements and cleanup
  * Centralized event logic by moving `events` module to `crewai.events`

  ## Documentation & Guides

  * Updated Enterprise Action Auth Token section documentation
  * Published documentation updates for `v0.175.0` release

  ## Cleanup & Refactoring

  * Refactored parser into modular functions for better structure
</Update>

<Update label="Aug 28, 2025">
  ## v0.175.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.175.0)

  ## Core Improvements & Fixes

  * Fixed migration of the `tool` section during `crewai update`
  * Reverted OpenAI pin: now requires `openai >=1.13.3` due to fixed import issues
  * Fixed flaky tests and improved test stability
  * Improved `Flow` listener resumability for HITL and cyclic flows
  * Enhanced timeout handling in `PlusAPI` and `TraceBatchManager`
  * Batched entity memory items to reduce redundant operations

  ## New Features & Enhancements

  * Added support for additional parameters in `Flow.start()` methods
  * Displayed task names in verbose CLI output
  * Added centralized embedding types and introduced a base embedding client
  * Introduced generic clients for ChromaDB and Qdrant
  * Added support for `crewai config reset` to clear tokens
  * Enabled `crewai_trigger_payload` auto-injection
  * Simplified RAG client initialization and introduced RAG configuration system
  * Added Qdrant RAG provider support
  * Improved tracing with better event data
  * Added support to remove Auth0 and email entry on `crewai login`

  ## Documentation & Guides

  * Added documentation for automation triggers
  * Fixed API Reference OpenAPI sources and redirects
  * Added hybrid search alpha parameter to the docs

  ## Cleanup & Deprecations

  * Added deprecation notice for `Task.max_retries`
  * Removed Auth0 dependency from login flow
</Update>

<Update label="Aug 19, 2025">
  ## v0.165.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.165.1)

  ## Core Improvements & Fixes

  * Fixed compatibility in `XMLSearchTool` by converting config values to strings for `configparser`
  * Fixed flaky Pytest test involving `PytestUnraisableExceptionWarning`
  * Mocked telemetry in test suite for more stable CI runs
  * Moved Chroma lockfile handling to `db_storage_path`
  * Ignored deprecation warnings from `chromadb`
  * Pinned OpenAI version `<1.100.0` due to `ResponseTextConfigParam` import issue

  ## New Features & Enhancements

  * Included exchanged agent messages into `ExternalMemory` metadata
  * Automatically injected `crewai_trigger_payload`
  * Renamed internal flag `inject_trigger_input` to `allow_crewai_trigger_context`
  * Continued tracing improvements and ephemeral tracing logic
  * Consolidated tracing logic conditions
  * Added support for `agent_id`-linked memory entries in `Mem0`

  ## Documentation & Guides

  * Added example to Tool Repository docs
  * Updated Mem0 documentation for Short-Term and Entity Memory integration
  * Revised Korean translations and improved sentence structures

  ## Cleanup & Chores

  * Removed deprecated AgentOps integration
</Update>

<Update label="Aug 19, 2025">
  ## v0.165.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.165.0)

  ## Core Improvements & Fixes

  * Fixed compatibility in `XMLSearchTool` by converting config values to strings for `configparser`
  * Fixed flaky Pytest test involving `PytestUnraisableExceptionWarning`
  * Mocked telemetry in test suite for more stable CI runs
  * Moved Chroma lockfile handling to `db_storage_path`
  * Ignored deprecation warnings from `chromadb`
  * Pinned OpenAI version `<1.100.0` due to `ResponseTextConfigParam` import issue

  ## New Features & Enhancements

  * Included exchanged agent messages into `ExternalMemory` metadata
  * Automatically injected `crewai_trigger_payload`
  * Renamed internal flag `inject_trigger_input` to `allow_crewai_trigger_context`
  * Continued tracing improvements and ephemeral tracing logic
  * Consolidated tracing logic conditions
  * Added support for `agent_id`-linked memory entries in `Mem0`

  ## Documentation & Guides

  * Added example to Tool Repository docs
  * Updated Mem0 documentation for Short-Term and Entity Memory integration
  * Revised Korean translations and improved sentence structures

  ## Cleanup & Chores

  * Removed deprecated AgentOps integration
</Update>

<Update label="Aug 13, 2025">
  ## v0.159.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.159.0)

  ## Core Improvements & Fixes

  * Improved LLM message formatting performance for better runtime efficiency
  * Fixed use of incorrect endpoint in enterprise configuration auth/parameters
  * Commented out listener resumability check for stability during partial flow resumption

  ## New Features & Enhancements

  * Added `enterprise configure` command to CLI for streamlined enterprise setup
  * Introduced partial flow resumability support

  ## Documentation & Guides

  * Added documentation for new tools
  * Added Korean translations
  * Updated documentation with TrueFoundry integration details
  * Added RBAC documentation and general cleanup
  * Fixed API reference and revamped examples/cookbooks across EN, PT-BR, and KO
</Update>

<Update label="Aug 06, 2025">
  ## v0.157.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.157.0)

  ## v0.157.0 What's Changed

  ## Core Improvements & Fixes

  * Enabled word wrapping for long input tool
  * Allowed persisting Flow state with `BaseModel` entries
  * Optimized string operations using `partition()` for performance
  * Dropped support for deprecated User Memory system
  * Bumped LiteLLM version to `1.74.9`
  * Fixed CLI to show missing modules more clearly during import
  * Supported device authorization with Okta

  ## New Features & Enhancements

  * Added `crewai config` CLI command group with tests
  * Added default value support for `crew.name`
  * Introduced initial tracing capabilities
  * Added support for LangDB integration
  * Added support for CLI configuration documentation

  ## Documentation & Guides

  * Updated MCP documentation with `connect_timeout` attribute
  * Added LangDB integration documentation
  * Added CLI config documentation
  * General feature doc updates and cleanup
</Update>

<Update label="Jul 30, 2025">
  ## v0.152.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.152.0)

  ## Core Improvements & Fixes

  * Removed `crewai signup` references and replaced them with `crewai login`
  * Fixed support for adding memories to Mem0 using `agent_id`
  * Changed the default value in Mem0 configuration
  * Updated import error to show missing module files clearly
  * Added timezone support to event timestamps

  ## New Features & Enhancements

  * Enhanced `Flow` class to support custom flow names
  * Refactored RAG components into a dedicated top-level module

  ## Documentation & Guides

  * Fixed incorrect model naming in Google Vertex AI documentation
</Update>

<Update label="Jul 23, 2025">
  ## v0.150.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.150.0)

  ## Core Improvements & Fixes

  * Used file lock around Chroma client initialization
  * Removed workaround related to SQLite without FTS5
  * Dropped unsupported `stop` parameter for LLM models automatically
  * Fixed `save` method and updated related test cases
  * Fixed message handling for Ollama models when last message is from assistant
  * Removed duplicate print on LLM call error
  * Added deprecation notice to `UserMemory`
  * Upgraded LiteLLM to version 1.74.3

  ## New Features & Enhancements

  * Added support for ad-hoc tool calling via internal LLM class
  * Updated Mem0 Storage from v1.1 to v2

  ## Documentation & Guides

  * Fixed neatlogs documentation
  * Added Tavily Search & Extractor tools to the Search-Research suite
  * Added documentation for `SerperScrapeWebsiteTool` and reorganized Serper section
  * General documentation updates and improvements

  ## crewai-tools v0.58.0

  ### New Tools / Enhancements

  * **SerperScrapeWebsiteTool**: Added a tool for extracting clean content from URLs
  * **Bedrock AgentCore**: Integrated browser and code interpreter toolkits for Bedrock agents
  * **Stagehand Update**: Refactored and updated Stagehand integration

  ### Fixes & Cleanup

  * **FTS5 Support**: Enabled SQLite FTS5 for improved text search in test workflows
  * **Test Speedups**: Parallelized GitHub Actions test suite for faster CI runs
  * **Cleanup**: Removed SQLite workaround due to FTS5 support being available
    **MongoDBVectorSearchTool**: Fixed serialization and schema handling
</Update>

<Update label="Jul 16, 2025">
  ## v0.148.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.148.0)

  ## Core Improvements & Fixes

  * Used production WorkOS environment ID
  * Added SQLite FTS5 support to test workflow
  * Fixed agent knowledge handling
  * Compared using `BaseLLM` class instead of `LLM`
  * Fixed missing `create_directory` parameter in `Task` class

  ## New Features & Enhancements

  * Introduced Agent evaluation functionality
  * Added Evaluator experiment and regression testing methods
  * Implemented thread-safe `AgentEvaluator`
  * Enabled event emission for Agent evaluation
  * Supported evaluation of single `Agent` and `LiteAgent`
  * Added integration with `neatlogs`
  * Added crew context tracking for LLM guardrail events

  ## Documentation & Guides

  * Added documentation for `guardrail` attributes and usage examples
  * Added integration guide for `neatlogs`
  * Updated documentation for Agent repository and `Agent.kickoff` usage
</Update>

<Update label="Jul 09, 2025">
  ## v0.141.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.141.0)

  ## Core Improvements & Fixes

  * Sped up GitHub Actions tests through parallelization

  ## New Features & Enhancements

  * Added crew context tracking for LLM guardrail events

  ## Documentation & Guides

  * Added documentation for Agent repository usage
  * Added documentation for `Agent.kickoff` method
</Update>

<Update label="Jul 02, 2025">
  ## v0.140.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.140.0)

  ## Core Improvements & Fixes

  * Fixed typo in test prompts
  * Fixed project name normalization by stripping trailing slashes during crew creation
  * Ensured environment variables are written in uppercase
  * Updated LiteLLM dependency
  * Refactored collection handling in `RAGStorage`
  * Implemented PEP 621 dynamic versioning

  ## New Features & Enhancements

  * Added capability to track LLM calls by task and agent
  * Introduced `MemoryEvents` to monitor memory usage
  * Added console logging for memory system and LLM guardrail events
  * Improved data training support for models up to 7B parameters
  * Added Scarf and Reo.dev analytics tracking
  * CLI workos login

  ## Documentation & Guides

  * Updated CLI LLM documentation
  * Added Nebius integration to the docs
  * Corrected typos in installation and pt-BR documentation
  * Added docs about `MemoryEvents`
  * Implemented docs redirects and included development tools
</Update>

<Update label="Jun 25, 2025">
  ## v0.134.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.134.0)

  ## Core Improvements & Fixes

  * Fixed tools parameter syntax
  * Fixed type annotation in `Task`
  * Fixed SSL error when retrieving LLM data from GitHub
  * Ensured compatibility with Pydantic 2.7.x
  * Removed `mkdocs` from project dependencies
  * Upgraded Langfuse code examples to use Python SDK v3
  * Added sanitize role feature in `mem0` storage
  * Improved Crew search during memory reset
  * Improved console printer output

  ## New Features & Enhancements

  * Added support for initializing a tool from defined `Tool` attributes
  * Added official way to use MCP Tools within a `CrewBase`
  * Enhanced MCP tools support to allow selecting multiple tools per agent in `CrewBase`
  * Added Oxylabs Web Scraping tools

  ## Documentation & Guides

  * Updated `quickstart.mdx`
  * Added docs on `LLMGuardrail` events
  * Updated documentation with comprehensive service integration details
  * Updated recommendation filters for MCP and Enterprise tools
  * Updated docs for Maxim observability
  * Added pt-BR documentation translation
  * General documentation improvements
</Update>

<Update label="Jun 12, 2025">
  ## v0.130.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.130.0)

  ## Core Improvements & Fixes

  * Removed duplicated message related to Tool result output
  * Fixed missing `manager_agent` tokens in `usage_metrics` from kickoff
  * Fixed telemetry singleton to respect dynamic environment variables
  * Fixed issue where Flow status logs could hide human input
  * Increased default X-axis spacing for flow plotting

  ## New Features & Enhancements

  * Added support for multi-org actions in the CLI
  * Enabled async tool executions for more efficient workflows
  * Introduced `LiteAgent` with Guardrail integration
  * Upgraded `LiteLLM` to support latest OpenAI version

  ## Documentation & Guides

  * Documented minimum `UV` version for Tool repository
  * Improved examples for Hallucination Guardrail
  * Updated planning docs for LLM usage
  * Added documentation for Maxim support in Agent observability
  * Expanded integrations documentation with images for enterprise features
  * Fixed guide on persistence
  * Updated Python version support to support python 3.13.x
</Update>

<Update label="Jun 05, 2025">
  ## v0.126.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.126.0)

  ### What’s Changed

  #### Core Improvements & Fixes

  * Added support for Python 3.13
  * Fixed agent knowledge sources issue
  * Persisted available tools from a Tool repository
  * Enabled tools to be loaded from Agent repository via their own module
  * Logged usage of tools when called by an LLM

  #### New Features & Enhancements

  * Added streamable-http transport support in MCP integration
  * Added support for community analytics
  * Expanded OpenAI-compatible section with a Gemini example
  * Introduced transparency features for prompts and memory systems
  * Minor enhancements for Tool publishing

  #### Documentation & Guides

  * Major restructuring of docs for better navigation
  * Expanded MCP integration documentation
  * Updated memory docs and README visuals
  * Fixed missing await keywords in async kickoff examples
  * Updated Portkey and Azure embeddings documentation
  * Added enterprise testing image to the LLM guide
  * General updates to the README
</Update>

<Update label="May 27, 2025">
  ## v0.121.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.121.1)

  Bug fixes and better docs
</Update>

<Update label="May 22, 2025">
  ## v0.121.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.121.0)

  # What’s Changed

  ## Core Improvements & Fixes

  * Fixed encoding error when creating tools
  * Fixed failing llama test
  * Updated logging configuration for consistency
  * Enhanced telemetry initialization and event handling

  ## New Features & Enhancements

  * Added markdown attribute to the Task class
  * Added reasoning attribute to the Agent class
  * Added inject\_date flag to Agent for automatic date injection
  * Implemented HallucinationGuardrail (no-op with test coverage)

  ## Documentation & Guides

  * Added documentation for StagehandTool and improved MDX structure
  * Added documentation for MCP integration and updated enterprise docs
  * Documented knowledge events and updated reasoning docs
  * Added stop parameter documentation
  * Fixed import references in doc examples (before\_kickoff, after\_kickoff)
  * General docs updates and restructuring for clarity
</Update>

<Update label="May 15, 2025">
  ## v0.120.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.120.1)

  ## Whats New

  * Fixes Interpolation with hyphens
</Update>

<Update label="May 14, 2025">
  ## v0.120.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.120.0)

  ### Core Improvements & Fixes

  •	Enabled full Ruff rule set by default for stricter linting
  •	Addressed race condition in FilteredStream using context managers
  •	Fixed agent knowledge reset issue
  •	Refactored agent fetching logic into utility module

  ### New Features & Enhancements

  •	Added support for loading an Agent directly from a repository
  •	Enabled setting an empty context for Task
  •	Enhanced Agent repository feedback and fixed Tool auto-import behavior
  •	Introduced direct initialization of knowledge (bypassing knowledge\_sources)

  ### Documentation & Guides

  •	Updated security.md for current security practices
  •	Cleaned up Google setup section for clarity
  •	Added link to AI Studio when entering Gemini key
  •	Updated Arize Phoenix observability guide
  •	Refreshed flow documentation
</Update>

<Update label="May 08, 2025">
  ## v0.119.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.119.0)

  What’s Changed

  ## Core Improvements & Fixes

  * Improved test reliability by enhancing pytest handling for flaky tests
  * Fixed memory reset crash when embedding dimensions mismatch
  * Enabled parent flow identification for Crew and LiteAgent
  * Prevented telemetry-related crashes when unavailable
  * Upgraded LiteLLM version for better compatibility
  * Fixed llama converter tests by removing skip\_external\_api

  ## New Features & Enhancements

  * Introduced knowledge retrieval prompt re-writting in Agent for improved tracking and debugging
  * Made LLM setup and quickstart guides model-agnostic

  ## Documentation & Guides

  * Added advanced configuration docs for the RAG tool
  * Updated Windows troubleshooting guide
  * Refined documentation examples for better clarity
  * Fixed typos across docs and config files
</Update>

<Update label="Apr 30, 2025">
  ## v0.118.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.118.0)

  ### Core Improvements & Fixes

  * Fixed issues with missing prompt or system templates.
  * Removed global logging configuration to avoid unintended overrides.
  * Renamed TaskGuardrail to LLMGuardrail for improved clarity.
  * Downgraded litellm to version 1.167.1 for compatibility.
  * Added missing **init**.py files to ensure proper module initialization.

  ### New Features & Enhancements

  * Added support for no-code Guardrail creation to simplify AI behavior controls.

  ### Documentation & Guides

  * Removed CrewStructuredTool from public documentation to reflect internal usage.
  * Updated enterprise documentation and YouTube embed for improved onboarding experience.
</Update>

<Update label="Apr 28, 2025">
  ## v0.117.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.117.1)

  * build: upgrade crewai-tools
  * upgrade liteLLM to latest version
  * Fix Mem0 OSS
</Update>

<Update label="Apr 28, 2025">
  ## v0.117.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.117.0)

  # What's Changed

  ## New Features & Enhancements

  * Added `result_as_answer` parameter support in `@tool` decorator.
  * Introduced support for new language models: GPT-4.1, Gemini-2.0, and Gemini-2.5 Pro.
  * Enhanced knowledge management capabilities.
  * Added Huggingface provider option in CLI.
  * Improved compatibility and CI support for Python 3.10+.

  ## Core Improvements & Fixes

  * Fixed issues with incorrect template parameters and missing inputs.
  * Improved asynchronous flow handling with coroutine condition checks.
  * Enhanced memory management with isolated configuration and correct memory object copying.
  * Fixed initialization of lite agents with correct references.
  * Addressed Python type hint issues and removed redundant imports.
  * Updated event placement for improved tool usage tracking.
  * Raised explicit exceptions when flows fail.
  * Removed unused code and redundant comments from various modules.
  * Updated GitHub App token action to v2.

  ## Documentation & Guides

  * Enhanced documentation structure, including enterprise deployment instructions.
  * Automatically create output folders for documentation generation.
  * Fixed broken link in `WeaviateVectorSearchTool` documentation.
  * Fixed guardrail documentation usage and import paths for JSON search tools.
  * Updated documentation for `CodeInterpreterTool`.
  * Improved SEO, contextual navigation, and error handling for documentation pages.
</Update>

<Update label="Apr 10, 2025">
  ## v0.114.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.114.0)

  # What's Changed

  ## New Features & Enhancements

  * Agents as an atomic unit. (`Agent(...).kickoff()`)
  * Support to Custom LLM implementations.
  * Integrated External Memory and Opik observability.
  * Enhanced YAML extraction.
  * Multimodal agent validation.
  * Added Secure fingerprints for agents and crews.

  ## Core Improvements & Fixes

  * Improved serialization, agent copying, and Python compatibility.
  * Added wildcard support to emit()
  * Added support for additional router calls and context window adjustments.
  * Fixed typing issues, validation, and import statements.
  * Improved method performance.
  * Enhanced agent task handling, event emissions, and memory management.
  * Fixed CLI issues, conditional tasks, cloning behavior, and tool outputs.

  ## Documentation & Guides

  * Improved documentation structure, theme, and organization.
  * Added guides for Local NVIDIA NIM with WSL2, W\&B Weave, and Arize Phoenix.
  * Updated tool configuration examples, prompts, and observability docs.
  * Guide on using singular agents within Flows
</Update>

<Update label="Mar 17, 2025">
  ## v0.108.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.108.0)

  # Features

  * Converted tabs to spaces in crew\.py template in PR #2190
  * Enhanced LLM Streaming Response Handling and Event System in PR #2266
  * Included model\_name in PR #2310
  * Enhanced Event Listener with rich visualization and improved logging in PR #2321
  * Added fingerprints in PR #2332

  # Bug Fixes

  * Fixed Mistral issues in PR #2308
  * Fixed a bug in documentation in PR #2370
  * Fixed type check error in fingerprint property in PR #2369

  # Documentation Updates

  * Improved tool documentation in PR #2259
  * Updated installation guide for the uv tool package in PR #2196
  * Added instructions for upgrading crewAI with the uv tool in PR #2363
  * Added documentation for ApifyActorsTool in PR #2254
</Update>

<Update label="Mar 09, 2025">
  ## v0.105.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.105.0)

  **Core Improvements & Fixes**

  * Fixed issues with missing template variables and user memory configuration.
  * Improved async flow support and addressed agent response formatting.
  * Enhanced memory reset functionality and fixed CLI memory commands.
  * Fixed type issues, tool calling properties, and telemetry decoupling.

  **New Features & Enhancements**

  * Added Flow state export and improved state utilities.
  * Enhanced agent knowledge setup with optional crew embedder.
  * Introduced event emitter for better observability and LLM call tracking.
  * Added support for Python 3.10 and ChatOllama from langchain\_ollama.
  * Integrated context window size support for the o3-mini model.
  * Added support for multiple router calls.

  **Documentation & Guides**

  * Improved documentation layout and hierarchical structure.
  * Added QdrantVectorSearchTool guide and clarified event listener usage.
  * Fixed typos in prompts and updated Amazon Bedrock model listings.
</Update>

<Update label="Feb 13, 2025">
  ## v0.102.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.102.0)

  ### Core Improvements & Fixes

  * Enhanced LLM Support: Improved structured LLM output, parameter handling, and formatting for Anthropic models.
  * Crew & Agent Stability: Fixed issues with cloning agents/crews using knowledge sources, multiple task outputs in conditional tasks, and ignored Crew task callbacks.
  * Memory & Storage Fixes: Fixed short-term memory handling with Bedrock, ensured correct embedder initialization, and added a reset memories function in the crew class.
  * Training & Execution Reliability: Fixed broken training and interpolation issues with dict and list input types.

  ### New Features & Enhancements

  * Advanced Knowledge Management: Improved naming conventions and enhanced embedding configuration with custom embedder support.
  * Expanded Logging & Observability: Added JSON format support for logging and integrated MLflow tracing documentation.
  * Data Handling Improvements: Updated excel\_knowledge\_source.py to process multi-tab files.
  * General Performance & Codebase Clean-Up: Streamlined enterprise code alignment and resolved linting issues.
  * Adding new tool QdrantVectorSearchTool

  ### Documentation & Guides

  * Updated AI & Memory Docs: Improved Bedrock, Google AI, and long-term memory documentation.
  * Task & Workflow Clarity: Added "Human Input" row to Task Attributes, Langfuse guide, and FileWriterTool documentation.
  * Fixed Various Typos & Formatting Issues.

  ### Maintenance & Miscellaneous

  * Refined Google Docs integrations and task handling for the current year.
</Update>

<Update label="Jan 28, 2025">
  ## v0.100.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.100.0)

  * Feat: Add Composio docs
  * Feat: Add SageMaker as a LLM provider
  * Fix: Overall LLM connection issues
  * Fix: Using safe accessors on training
  * Fix: Add version check to crew\_chat.py
  * Docs: New docs for crewai chat
  * Docs: Improve formatting and clarity in CLI and Composio Tool docs
</Update>

<Update label="Jan 20, 2025">
  ## v0.98.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.98.0)

  * Feat: Conversation crew v1
  * Feat: Add unique ID to flow states
  * Feat: Add @persist decorator with FlowPersistence interface
  * Integration: Add SambaNova integration
  * Integration: Add NVIDIA NIM provider in cli
  * Integration: Introducing VoyageAI
  * Chore: Update date to current year in template
  * Fix: Fix API Key Behavior and Entity Handling in Mem0 Integration
  * Fix: Fixed core invoke loop logic and relevant tests
  * Fix: Make tool inputs actual objects and not strings
  * Fix: Add important missing parts to creating tools
  * Fix: Drop litellm version to prevent windows issue
  * Fix: Before kickoff if inputs are none
  * Fix: TYPOS
  * Fix: Nested pydantic model issue
  * Fix: Docling issues
  * Fix: union issue
  * Docs updates
</Update>

<Update label="Jan 04, 2025">
  ## v0.95.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.95.0)

  * Feat: Adding Multimodal Abilities to Crew
  * Feat: Programatic Guardrails
  * Feat: HITL multiple rounds
  * Feat: Gemini 2.0 Support
  * Feat: CrewAI Flows Improvements
  * Feat: Add Workflow Permissions
  * Feat: Add support for langfuse with litellm
  * Feat: Portkey Integration with CrewAI
  * Feat: Add interpolate\_only method and improve error handling
  * Feat: Docling Support
  * Feat: Weviate Support
  * Fix: output\_file not respecting system path
  * Fix disk I/O error when resetting short-term memory.
  * Fix: CrewJSONEncoder now accepts enums
  * Fix: Python max version
  * Fix: Interpolation for output\_file in Task
  * Fix: Handle coworker role name case/whitespace properly
  * Fix: Add tiktoken as explicit dependency and document Rust requirement
  * Fix: Include agent knowledge in planning process
  * Fix: Change storage initialization to None for KnowledgeStorage
  * Fix: Fix optional storage checks
  * Fix: include event emitter in flows
  * Fix: Docstring, Error Handling, and Type Hints Improvements
  * Fix: Suppressed userWarnings from litellm pydantic issues
</Update>

<Update label="Dec 05, 2024">
  ## v0.86.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.86.0)

  * remove all references to pipeline and pipeline router
  * docs: Add Nvidia NIM as provider in Custom LLM
  * add knowledge demo + improve knowledge docs
  * Brandon/cre 509 hitl multiple rounds of followup
  * New docs about yaml crew with decorators. Simplify template crew
</Update>

<Update label="Dec 04, 2024">
  ## v0.85.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.85.0)

  * Added knowledge to agent level
  * Feat/remove langchain
  * Improve typed task outputs
  * Log in to Tool Repository on `crewai login`
  * Fixes issues with result as answer not properly exiting LLM loop
  * fix: missing key name when running with ollama provider
  * fix spelling issue found
  * Update readme for running mypy
  * Add knowledge to mint.json
  * Update Github actions
  * Docs Update Agents docs to include two approaches for creating an agent
  * Documentation Improvements: LLM Configuration and Usage
</Update>

<Update label="Nov 25, 2024">
  ## v0.83.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.83.0)

  * New `before_kickoff` and `after_kickoff` crew callbacks
  * Support to pre-seed agents with Knowledge
  * Add support for retrieving user preferences and memories using Mem0
  * Fix Async Execution
  * Upgrade chroma and adjust embedder function generator
  * Update CLI Watson supported models + docs
  * Reduce level for Bandit
  * Fixing all tests
  * Update Docs
</Update>

<Update label="Nov 14, 2024">
  ## v0.80.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.80.0)

  * Fixing Tokens callback replacement bug
  * Fixing Step callback issue
  * Add cached prompt tokens info on usage metrics
  * Fix crew\_train\_success test
</Update>

<Update label="Nov 11, 2024">
  ## v0.79.4

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.79.4)

  Series of small bug fixes around llms support
</Update>

<Update label="Nov 10, 2024">
  ## v0.79.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.79.0)

  * Add inputs to flows
  * Enhance log storage to support more data types
  * Add support to IBM memory
  * Add Watson as an option in CLI
  * Add security.md file
  * Replace .netrc with uv environment variables
  * Move BaseTool to main package and centralize tool description generation
  * Raise an error if an LLM doesnt return a response
  * Fix flows to support cycles and added in test
  * Update how we name crews and fix missing config
  * Update docs
</Update>

<Update label="Oct 30, 2024">
  ## v0.76.9

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.76.9)

  * Update plot command for flow to crewai flow plot
  * Add tomli so we can support 3.10
  * Forward install command options to `uv sync`
  * Improve tool text description and args
  * Improve tooling and flow docs
  * Update flows cli to allow you to easily add additional crews to a flow with crewai flow add-crew
  * Fixed flows bug when using multiple start and listen(and\_(..., ..., ...))
</Update>

<Update label="Oct 23, 2024">
  ## v0.76.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.76.2)

  Updating crewai create commadn
</Update>

<Update label="Oct 23, 2024">
  ## v0.76.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.76.0)

  * fix/fixed missing API prompt + CLI docs update
  * chore(readme): fixing step for 'running tests' in the contribution
  * support unsafe code execution. add in docker install and running checks
  * Fix memory imports for embedding functions by
</Update>

<Update label="Oct 23, 2024">
  ## v0.75.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.75.1)

  new `--provider` option on crewai crewat
</Update>

<Update label="Oct 23, 2024">
  ## v0.75.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.75.0)

  * Fixing test post training
  * Simplify flows
  * Adapt `crewai tool install <tool>`
  * Ensure original embedding config works
  * Fix bugs
  * Update docs - Including adding Cerebras LLM example configuration to LLM docs
  * Drop unnecessary tests
</Update>

<Update label="Oct 18, 2024">
  ## v0.74.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.74.2)

  * feat: add poetry.lock to uv migration
  * fix tool calling issue
</Update>

<Update label="Oct 18, 2024">
  ## v0.74.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.74.0)

  * UV migration
  * Adapt Tools CLI to UV
  * Add warning from Poetry -> UV
  * CLI to allow for model selection & submitting API keys
  * New Memory Base
  * Fix Linting and Warnings
  * Update Docs
  * Bug fixesh
</Update>

<Update label="Oct 11, 2024">
  ## v0.70.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.70.1)

  * New Flow feature
  * Flow visualizer
  * Create `crewai create flow` command
  * Create `crewai tool create <tool>` command
  * Add Git validations for publishing tools
  * fix: JSON encoding date objects
  * New Docs
  * Update README
  * Bug fixes
</Update>

<Update label="Sep 27, 2024">
  ## v0.65.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.65.2)

  * Adding experimental Flows feature
  * Fixing order of tasks bug
  * Updating templates
</Update>

<Update label="Sep 27, 2024">
  ## v0.64.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.64.0)

  * Ordering tasks properly
  * Fixing summarization logic
  * Fixing stop words logic
  * Increases default max iterations to 20
  * Fix crew's key after input interpolation
  * Fixing Training Feature
  * Adding initial tools API
  * TYPOS
  * Updating Docs

  Fixes: #1359 #1355 #1353 #1356 and others
</Update>

<Update label="Sep 25, 2024">
  ## v0.63.6

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.63.6)

  * Updating projects templates
</Update>

<Update label="Sep 25, 2024">
  ## v0.63.5

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.63.5)

  * Bringing support to o1 family back, and any model that don't support stop words
  * Updating dependencies
  * Updating logs
  * Updating docs
</Update>

<Update label="Sep 24, 2024">
  ## v0.63.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.63.2)

  * Adding OPENAI\_BASE\_URL as fallback
  * Adding proper LLM import
  * Updating docs
</Update>

<Update label="Sep 24, 2024">
  ## v0.63.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.63.1)

  * Small bug fix for support future CrewAI deploy
</Update>

<Update label="Sep 24, 2024">
  ## v0.63.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.63.0)

  * New LLM class to interact with LLMs (leveraging LiteLLM)
  * Adding support to custom memory interfaces
  * Bringing GPT-4o-mini as the default model
  * Updates Docs
  * Updating dependencies
  * Bug fixes
    * Remove redundant task creation in `kickoff_for_each_async`
</Update>

<Update label="Sep 18, 2024">
  ## v0.61.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.61.0)

  * Updating dependencies
  * Printing max rpm message in different color
  * Updating all cassettes for tests
  * Always ending on a user message - to better support certain models like bedrock ones
  * Overall small bug fixes
</Update>

<Update label="Sep 16, 2024">
  ## v0.60.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.60.0)

  * Removing LangChain and Rebuilding Executor
  * Get all of out tests back to green
  * Adds the ability to not use system prompt use\_system\_prompt on the Agent
  * Adds the ability to not use stop words (to support o1 models) use\_stop\_words on the Agent
  * Sliding context window gets renamed to respect\_context\_window, and enable by default
  * Delegation is now disabled by default
  * Inner prompts were slightly changed as well
  * Overall reliability and quality of results
  * New support for:
    * Number of max requests per minute
    * A maximum number of iterations before giving a final answer
    * Proper take advantage of system prompts
    * Token calculation flow
    * New logging of the crew and agent execution
</Update>

<Update label="Sep 13, 2024">
  ## v0.55.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.55.2)

  * Adding ability for auto complete
  * Add name and expected\_output to TaskOutput
  * New `crewai install` CLI
  * New `crewai deploy` CLI
  * Cleaning up of Pipeline feature
  * Updated docs
  * Dev experience improvements like bandit CI pipeline
  * Fix bugs:
    * Ability to use `planning_llm`
    * Fix YAML based projects
    * Fix Azure support
    * Add support to Python 3.10
    * Moving away from Pydantic v1
</Update>

<Update label="Aug 11, 2024">
  ## v0.51.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.51.0)

  * crewAI Testing / Evaluation - [https://docs.crewai.com/core-concepts/Testing/](https://docs.crewai.com/core-concepts/Testing/)
  * Adding new sliding context window
  * Allowing all attributes on YAML - [https://docs.crewai.com/getting-started/Start-a-New-CrewAI-Project-Template-Method/#customizing-your-project](https://docs.crewai.com/getting-started/Start-a-New-CrewAI-Project-Template-Method/#customizing-your-project)
  * Adding initial Pipeline Structure - [https://docs.crewai.com/core-concepts/Pipeline/](https://docs.crewai.com/core-concepts/Pipeline/)
  * Ability to set LLM for planning step - [https://docs.crewai.com/core-concepts/Planning/](https://docs.crewai.com/core-concepts/Planning/)
  * New crew run command - [https://docs.crewai.com/getting-started/Start-a-New-CrewAI-Project-Template-Method/#running-your-project](https://docs.crewai.com/getting-started/Start-a-New-CrewAI-Project-Template-Method/#running-your-project)
  * Saving file now dumps dict into JSON - [https://docs.crewai.com/core-concepts/Tasks/#creating-directories-when-saving-files](https://docs.crewai.com/core-concepts/Tasks/#creating-directories-when-saving-files)
  * Using verbose settings for tool outputs
  * Added new Github Templates
  * New Vision tool - [https://docs.crewai.com/tools/VisionTool/](https://docs.crewai.com/tools/VisionTool/)
  * New DALL-E Tool - [https://docs.crewai.com/tools/DALL-ETool/](https://docs.crewai.com/tools/DALL-ETool/)
  * New MySQL tool - [https://docs.crewai.com/tools/MySQLTool/](https://docs.crewai.com/tools/MySQLTool/)
  * New NL2SQL Tool - [https://docs.crewai.com/tools/NL2SQLTool.md](https://docs.crewai.com/tools/NL2SQLTool.md)
  * Bug Fixes:
    * Bug with planning feature output
    * Async tasks for hierarchical process
    * Better pydantic output for non OAI models
    * JSON truncation issues
    * Fix logging types
    * Only import AgentOps if the Env Key is set
    * Sanitize agent roles to ensure valid directory names (Windows)
    * Tools name shouldn't contain space for OpenAI
    * A bunch of minor issues
</Update>

<Update label="Jul 20, 2024">
  ## v0.41.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.41.1)

  * Fix bug with planning feature
</Update>

<Update label="Jul 19, 2024">
  ## v0.41.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.41.0)

  * **\[Breaking Change]** Type Safe output
    * All crews and tasks now return a proper object TaskOuput and CrewOutput
  * **\[Feature]** New planning feature for crews (plan before act)
    * by adding planning=True to the Crew instance
  * **\[Feature]** Introduced Replay Feature
    * New CLI that allow you to list the tasks from last run and replay from a specific one
  * **\[Feature]** Ability to reset memory
    * You can clean your crew memory before running it again
  * **\[Feature]** Add retry feature for LLM calls
    * You can retry llm calls and not stop the crew execution
  * **\[Feature]** Added ability to customize converter
  * **\[Tool]** Enhanced tools with type hinting and new attributes
  * **\[Tool]** Added MultiON Tool
  * **\[Tool]** Fixed filecrawl tools
  * **\[Tool]** Fixed bug in Scraping tool
  * **\[Tools]** Bumped crewAI-tools dependency to version
  * **\[Bugs]** General bug fixes and improvements
  * **\[Bugs]** Telemetry fixes
  * **\[Bugs]** Spell check corrections
  * **\[Docs]** Updated documentation
</Update>

<Update label="Jul 06, 2024">
  ## v0.36.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.36.0)

  * Bug fix
  * Updating Docs
  * Updating native prompts
  * Fixing TYPOs on the prompts
  * Adding AgentOps native support
  * Adding Firecrawl Tools
  * Adding new ability to return a tool results as an agent result
  * Improving coding Interpreter tool
  * Adding new option to create your own corveter class (docs pending)
</Update>

<Update label="Jul 04, 2024">
  ## v0.35.8

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.35.8)

  * fixing embechain dependency issue
</Update>

<Update label="Jul 02, 2024">
  ## v0.35.7

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.35.7)

  * New @composiohq integration is out
  * Documentation update
  * Custom GPT Updated
  * Adjusting manager verbosity level
  * Bug fixes
</Update>

<Update label="Jul 01, 2024">
  ## v0.35.5

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.35.5)

  * Fix embedchain dependency
</Update>

<Update label="Jul 01, 2024">
  ## v0.35.4

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.35.4)

  * Updating crewai create CLI to use the new version
</Update>

<Update label="Jul 01, 2024">
  ## v0.35.3

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.35.3)

  * Code Execution Bug fixed
  * Updating overall docs
  * Bumping version of crewai-tools
  * Bumping versions of many dependencies
  * Overall bugfixes
</Update>

<Update label="Jun 29, 2024">
  ## v0.35.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.35.0)

  * Your agents can now execute code
  * Bring Any 3rd-party agent, LlamaIndex, LangChain and Autogen  agents can all be part of your crew now!
  * Train you crew before you execute it and get consistent results! New CLI `crewai train -n X`
  * Bug fixes and docs updates (still missing some new docs updates coming soon)
</Update>

<Update label="Jun 22, 2024">
  ## v0.32.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.32.2)

  * Updating `crewai create` CLI to use the new version
  * Fixing delegation agent matching
</Update>

<Update label="Jun 21, 2024">
  ## v0.32.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.32.0)

  * New `kickoff_for_each`, `kickoff_async` and `kickoff_for_each_async` methods for better control over the kickoff process
  * Adding support for all LlamaIndex hub integrations
  * Adding `usage_metrics` to full output or a crew
  * Adding support to multiple crews on the new YAML format
  * Updating dependencies
  * Fixed Bugs and TYPOs
  * Documentation updated
  * Added search in docs
  * Making gpt-4o the default model
  * Adding new docs for LangTrace, Browserbase and Exa Search
  * Adding timestamp to logging
</Update>

<Update label="May 23, 2024">
  ## v0.30.11

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.30.11)

  * Updating project generation template
</Update>

<Update label="May 14, 2024">
  ## v0.30.8

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.30.8)

  * Updating dependencies
  * Small bug fixes on crewAI project structure
  * Removing custom YAML parser for now
</Update>

<Update label="May 14, 2024">
  ## v0.30.5

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.30.5)

  * Making agent delegation more versatile for smaller models
</Update>

<Update label="May 13, 2024">
  ## v0.30.4

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.30.4)

  **Docs Update will follow** sorry about that and thank you for bearing with me, we are launching new docs soon!

  ➿  Fixing task callback
  🧙  Ability to set a specific agent as manager instead of having crew create your one
  📄  Ability to set system, prompt and response templates, so it works more reliable with opensource models (works better with smaller models)
  👨‍💻  Improving json and pydantic output (works better with smaller models)
  🔎 Improving tool name recognition (works better with smaller models)
  🧰  Improvements for tool usage (works better with smaller models)
  📃  Initial support to bring your own prompts
  2️⃣  Fixing duplicating token calculator metrics
  🪚  Adding couple new tools, Browserbase and Exa Search
  📁  Ability to create directory when saving as file
  🔁  Updating dependencies - double check tools
  📄  Overall small documentation improvements
  🐛  Smaller bug fixes (typos and such)
  👬  Fixing co-worker / coworker issues
  👀  Smaller Readme Updates
</Update>

<Update label="Apr 11, 2024">
  ## v0.28.8

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.28.8)

  * updating version used on crewai CLI
</Update>

<Update label="Apr 11, 2024">
  ## v0.28.7

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/0.28.7)

  * Bug fixes
  * Updating crewAI tool version with bug fixes
</Update>

<Update label="Apr 08, 2024">
  ## v0.28.5

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.28.5)

  * Major Long term memory interpolation issue
  * Updating tools package dependency with fixes
  * Removing unnecessary certificate
</Update>

<Update label="Apr 07, 2024">
  ## v0.28.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.28.2)

  * Major long term memory fix
</Update>

<Update label="Apr 06, 2024">
  ## v0.28.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.28.1)

  * Updating crewai-tools to 0.1.15
</Update>

<Update label="Apr 05, 2024">
  ## v0.28.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.28.0)

  * Not overriding LLM callbacks
  * Adding `max_execution_time` support
  * Adding specific memory docs
  * Moving tool usage logging color to purple from yellow
  * Updating Docs
</Update>

<Update label="Apr 04, 2024">
  ## v0.27.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.27.0)

  * 🧠 **Memory (shared crew memory)** - To enable it just add `memory=True` to your crew, it will work transparently and make outcomes better and more reliable, it's disable by default for now
  * 🤚🏼 **Native Human Input Support:** [docs](https://docs.crewai.com/how-to/Human-Input-on-Execution/)
  * 🌐 **Universal RAG Tools Support:** Any models, beyond just OpenAI. [Example](https://docs.crewai.com/tools/DirectorySearchTool/#custom-model-and-embeddings)
  * 🔍 **Enhanced Cache Control:** Meet the ingenious cache\_function attribute: [docs](https://docs.crewai.com/core-concepts/Tools/#custom-caching-mechanism)
  * 🔁 **Updated crewai-tools Dependency:** Always in sync with the latest and greatest.
  * ⛓️ **Cross Agent Delegation:** Smoother cooperation between agents.
  * 💠 **Inner Prompt Improvements:** A finer conversational flow.
  * 📝 **Improving tool usage with better parsing**
  * 🔒 **Security improvements and updating dependencies**
  * 📄 **Documentation improved**
  * 🐛 **Bug fixes**
</Update>

<Update label="Mar 12, 2024">
  ## v0.22.5

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.22.5)

  * Other minor import issues on the new templates
</Update>

<Update label="Mar 12, 2024">
  ## v0.22.4

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.22.4)

  Fixing template issues
</Update>

<Update label="Mar 11, 2024">
  ## v0.22.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.22.2)

  * Fixing bug on the new cli template
  * Guaranteeing tasks order on new cli template
</Update>

<Update label="Mar 11, 2024">
  ## v0.22.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.22.0)

  * Adding initial CLI `crewai create` command
  * Adding ability to agents and tasks to be defined using dictionaries
  * Adding more clear agent logging
  * Fixing bug Exceed maximum recursion depth bug
  * Fixing docs
  * Updating README
</Update>

<Update label="Mar 04, 2024">
  ## v0.19.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.19.0)

  * Efficiency in tool usage +1023.21%
  * Mean tools used +276%
  * Tool errors slashed by 67%, more reliable than ever.
  * Delegation capabilities enhanced
  * Ability to fallback to function calling by setting `function_calling_llm` to Agent or Crew
  * Ability to get crew execution metrics after `kickoff` with `crew.usage_metrics`
  * Adding ability for inputs being passed in kickoff now `crew.kickoff(inputs: {'key': 'value})`
  * Updating Docs
</Update>

<Update label="Feb 28, 2024">
  ## v0.16.3

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.16.3)

  * Fixing overall bugs
  * Making sure code is backwards compatible
</Update>

<Update label="Feb 28, 2024">
  ## v0.16.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.16.0)

  * Removing lingering `crewai_tools` dependency
  * Adding initial support for inputs interpolation (missing docs)
  * Adding ability to track tools usage, tools error, formatting errors, tokens usage
  * Updating README
</Update>

<Update label="Feb 26, 2024">
  ## v0.14.4

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.14.4)

  * Updating timeouts
  * Updating docs
  * Removing crewai\_tools as a mandatory
  * Making agents memory-less by default for token count reduction (breaking change for people counting on this previously)
</Update>

<Update label="Feb 24, 2024">
  ## v0.14.3

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.14.3)

  * Fixing broken docs link
  * Adding support for agents without tools
  * Avoid empty task outputs
</Update>

<Update label="Feb 22, 2024">
  ## v0.14.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.14.0)

  All improvements from the v0.14.0rc.

  * Support to export json and pydantic from opensource models
</Update>

<Update label="Feb 20, 2024">
  ## v0.14.0rc

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.14.0rc0)

  * Adding support to crewai-tools
  * Adding support to format tasks output as Pydantic Objects Or JSON
  * Adding support to save tasks ouput to a file
  * Improved reliability for inter agent delegation
  * Revamp tools usage logic to proper use function calling
  * Updating internal prompts
  * Supporting tools with no arguments
  * Bug fixes
</Update>

<Update label="Feb 16, 2024">
  ## v0.11.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.11.2)

  * Adding further error logging so users understand what is happening if a tool fails
</Update>

<Update label="Feb 16, 2024">
  ## v0.11.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.11.1)

  * It fixes a  bug on the tool usage logic that was early caching the result even if there was an error on the usage, preventing it from using the tool again.
  * It will also print any error message in red allowing the user to understand what was the problem with the tool.
</Update>

<Update label="Feb 13, 2024">
  ## v0.11.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.11.0)

  * Ability to set `function_calling_llm` on both the entire crew and individual agents
  * Some early attempts on cost reduction
  * Improving function calling for tools
  * Updates docs
</Update>

<Update label="Feb 10, 2024">
  ## v0.10.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.10.0)

  * Ability to get `full_ouput` from crew kickoff with all tasks outputs
  * Ability to set `step_callback` function for both Agents and Crews so you can get all intermediate steps
  * Remembering Agent of the expected format after certain number of tool usages.
  * New tool usage internals now using json, unlocking tools with multiple arguments
  * Refactoring overall delegation logic, now way more reliable
  * Fixed `max_inter` bug now properly forcing llm to answer as it gets to that
  * Rebuilt caching structure, making sure multiple agents can use the same cache
  * Refactoring Task repeated usage prevention logic
  * Removing now unnecessary `CrewAgentOutputParser`
  * Opt-in to share complete crew related data with the crewAI team
  * Overall Docs update
</Update>

<Update label="Feb 08, 2024">
  ## v0.5.5

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.5.5)

  * Overall doc + readme improvements
  * Fixing RPM controller being set unnecessarily
  * Adding early stage anonymous telemetry for lib improvement
</Update>

<Update label="Feb 07, 2024">
  ## v0.5.3

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.5.3)

  * quick Fix for hierarchical manager
</Update>

<Update label="Feb 06, 2024">
  ## v0.5.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.5.2)

  * Adding `manager_llm` for hierarchical process
  * Improving `max_inter` and `max_rpm` logic
  * Updating README and Docs
</Update>

<Update label="Feb 04, 2024">
  ## v0.5.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.5.0)

  This new version bring a lot of new features and improvements to the library.

  ## Features

  * Adding Task Callbacks.
  * Adding support for Hierarchical process.
  * Adding ability to references specific tasks in another task.
  * Adding ability to parallel task execution.

  ## Improvements

  * Revamping Max Iterations and Max Requests per Minute.
  * Developer experience improvements, docstrings and such.
  * Small improvements and TYPOs.
  * Fix static typing errors.
  * Updated README and Docs.
</Update>

<Update label="Jan 14, 2024">
  ## v0.1.32

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.1.32)

  * Moving to LangChain 0.1.0
  * Improving Prompts
  * Adding ability to limit maximum number of iterations for an agent
  * Adding ability to Request Per Minute throttling for both Agents and Crews
  * Adding initial support for translations
  * Adding Greek translation
  * Improve code readability
  * Starting new documentation with mkdocs
</Update>

<Update label="Jan 07, 2024">
  ## v0.1.23

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.1.23)

  * Many Reliability improvements
  * Prompt changes
  * Initial changes for supporting multiple languages
  * Fixing bug on task repeated execution
  * Better execution error handling
  * Updating READMe
</Update>

<Update label="Dec 30, 2023">
  ## v0.1.14

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.1.14)

  * Adding tool caching a loop execution prevention. (@joaomdmoura)
  * Adding more guidelines for Agent delegation. (@joaomdmoura)
  * Updating to use new openai lib version. (@joaomdmoura)
  * Adding verbose levels to the logger. (@joaomdmoura)
  * Removing WIP code. (@joaomdmoura)
  * A lot of developer quality of life improvements (Special thanks to @greysonlalonde).
  * Updating to pydantic v2 (Special thanks to @greysonlalonde as well).
</Update>

<Update label="Nov 24, 2023">
  ## v0.1.2

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.1.2)

  * Adding ability to use other LLMs, not OpenAI
</Update>

<Update label="Nov 19, 2023">
  ## v0.1.1

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.1.1)

  # CrewAI v0.1.1 Release Notes

  ## What's New

  * **Crew Verbose Mode**:  Now allowing you to inspect a the tasks are being executed.

  * **README and Docs Updates**: A series of minor updates on the docs
</Update>

<Update label="Nov 14, 2023">
  ## v0.1.0

  [View release on GitHub](https://github.com/crewAIInc/crewAI/releases/tag/v0.1.0)

  # CrewAI v0.1.0 Release Notes

  We are thrilled to announce the initial release of CrewAI, version 0.1.0! CrewAI is a framework designed to facilitate the orchestration of autonomous AI agents capable of role-playing and collaboration to accomplish complex tasks more efficiently.

  ## What's New

  * **Initial Launch**: CrewAI is now officially in the wild! This foundational release lays the groundwork for AI agents to work in tandem, each with its own specialized role and objectives.

  * **Role-Based Agent Design**: Define and customize agents with specific roles, goals, and the tools they need to succeed.

  * **Inter-Agent Delegation**: Agents are now equipped to autonomously delegate tasks, enabling dynamic distribution of workload among the team.

  * **Task Management**: Create and assign tasks dynamically with the flexibility to specify the tools needed for each task.

  * **Sequential Processes**: Set up your agents to tackle tasks one after the other, ensuring organized and predictable workflows.

  * **Documentation**: Start exploring CrewAI with our initial documentation that guides you through the setup and use of the framework.

  ## Enhancements

  * Detailed API documentation for the `Agent`, `Task`, `Crew`, and `Process` classes.
  * Examples and tutorials to help you build your first CrewAI application.
  * Basic setup for collaborative and delegation mechanisms among agents.

  ## Known Issues

  * As this is the first release, there may be undiscovered bugs and areas for optimization. We encourage the community to report any issues found during use.

  ## Upcoming Features

  * **Advanced Process Management**: In future releases, we will introduce more complex processes for task management including consensual and hierarchical workflows.
</Update>



# HITL Workflows
Source: https://docs.crewai.com/en/enterprise/guides/human-in-the-loop

Learn how to implement Human-In-The-Loop workflows in CrewAI for enhanced decision-making

Human-In-The-Loop (HITL) is a powerful approach that combines artificial intelligence with human expertise to enhance decision-making and improve task outcomes. This guide shows you how to implement HITL within CrewAI.


## Setting Up HITL Workflows

<Steps>
  <Step title="Configure Your Task">
    Set up your task with human input enabled:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cb2e2bab131e9eff86b0c51dceb16e11" alt="Crew Human Input" data-og-width="624" width="624" data-og-height="165" height="165" data-path="images/enterprise/crew-human-input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1bc2a85e5aa6e736a118fe2c91452dc6 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=137c8e9c09c9a93ba1b683ad3e247e0d 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79c8be91790b117c1498568ca48f4287 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4da8411c0c26ee98c0dcdde6117353fe 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1b24b707df7ec697db2652d80ed3ff8f 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-human-input.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=39a7543043c397cf4ff84582216ddb65 2500w" />
    </Frame>
  </Step>

  <Step title="Provide Webhook URL">
    When kicking off your crew, include a webhook URL for human input:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f2d298c0b4c7b3a62e1dee4e2e6f1bb3" alt="Crew Webhook URL" data-og-width="624" width="624" data-og-height="259" height="259" data-path="images/enterprise/crew-webhook-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=80f52cbe2cd1c6a2a4cd3e2039c22971 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6496d6f5e1fe13fec8be8a406e635b26 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=27cfbbf1fecdab2540df4aeb7ddd15b6 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=57d3439e96917a0627189bfd188af4a0 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=cad1f034d8fd4113f08df6bf1a58f3fa 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-webhook-url.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fba10cd375c57bcd9b2a216067b5bd44 2500w" />
    </Frame>
  </Step>

  <Step title="Receive Webhook Notification">
    Once the crew completes the task requiring human input, you'll receive a webhook notification containing:

    * **Execution ID**
    * **Task ID**
    * **Task output**
  </Step>

  <Step title="Review Task Output">
    The system will pause in the `Pending Human Input` state. Review the task output carefully.
  </Step>

  <Step title="Submit Human Feedback">
    Call the resume endpoint of your crew with the following information:

    <Frame>
      <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1e1c2ca22a2d674426f8e663fed33eca" alt="Crew Resume Endpoint" data-og-width="624" width="624" data-og-height="261" height="261" data-path="images/enterprise/crew-resume-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=09014207ae06e6522303b77e4648f0d4 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1ad53990ab04014e622b3acdb37ca604 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=afb11308edffa03de969712505cf95ab 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bd69f0d75ec47ac2c6280f24a550bff 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f81e1ebcdc8a9348133503eb5eb4e37a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-resume-endpoint.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b12843fa2b80cc86580220766a1f4cc4 2500w" />
    </Frame>

    <Warning>
      **Critical: Webhook URLs Must Be Provided Again**:
      You **must** provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`) in the resume call that you used in the kickoff call. Webhook configurations are **NOT** automatically carried over from kickoff - they must be explicitly included in the resume request to continue receiving notifications for task completion, agent steps, and crew completion.
    </Warning>

    Example resume call with webhooks:

    ```bash  theme={null}
    curl -X POST {BASE_URL}/resume \
      -H "Authorization: Bearer YOUR_API_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "execution_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
        "task_id": "research_task",
        "human_feedback": "Great work! Please add more details.",
        "is_approve": true,
        "taskWebhookUrl": "https://your-server.com/webhooks/task",
        "stepWebhookUrl": "https://your-server.com/webhooks/step",
        "crewWebhookUrl": "https://your-server.com/webhooks/crew"
      }'
    ```

    <Warning>
      **Feedback Impact on Task Execution**:
      It's crucial to exercise care when providing feedback, as the entire feedback content will be incorporated as additional context for further task executions.
    </Warning>

    This means:

    * All information in your feedback becomes part of the task's context.
    * Irrelevant details may negatively influence it.
    * Concise, relevant feedback helps maintain task focus and efficiency.
    * Always review your feedback carefully before submission to ensure it contains only pertinent information that will positively guide the task's execution.
  </Step>

  <Step title="Handle Negative Feedback">
    If you provide negative feedback:

    * The crew will retry the task with added context from your feedback.
    * You'll receive another webhook notification for further review.
    * Repeat steps 4-6 until satisfied.
  </Step>

  <Step title="Execution Continuation">
    When you submit positive feedback, the execution will proceed to the next steps.
  </Step>
</Steps>


## Best Practices

* **Be Specific**: Provide clear, actionable feedback that directly addresses the task at hand
* **Stay Relevant**: Only include information that will help improve the task execution
* **Be Timely**: Respond to HITL prompts promptly to avoid workflow delays
* **Review Carefully**: Double-check your feedback before submitting to ensure accuracy


## Common Use Cases

HITL workflows are particularly valuable for:

* Quality assurance and validation
* Complex decision-making scenarios
* Sensitive or high-stakes operations
* Creative tasks requiring human judgment
* Compliance and regulatory reviews



# React Component Export
Source: https://docs.crewai.com/en/enterprise/guides/react-component-export

Learn how to export and integrate CrewAI AMP React components into your applications

This guide explains how to export CrewAI AMP crews as React components and integrate them into your own applications.


## Exporting a React Component

<Steps>
  <Step title="Export the Component">
    Click on the ellipsis (three dots on the right of your deployed crew) and select the export option and save the file locally. We will be using `CrewLead.jsx` for our example.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e0c72184b57eeae414674023197fca1b" alt="Export React Component" data-og-width="493" width="493" data-og-height="359" height="359" data-path="images/enterprise/export-react-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8493fbf39305d5f66dea0f19af860363 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=77698a5cf65d840dc81de4bd72bb4db1 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fe2f4ee4cf620354f6413726983a33fb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c817314a4164f7c55ecd424ab5de61cf 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6d982c3772ec31c866bcdcabaa8a6b5e 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/export-react-component.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b9e48143a23435526cf924906aac876 2500w" />
    </Frame>
  </Step>
</Steps>


## Setting Up Your React Environment

To run this React component locally, you'll need to set up a React development environment and integrate this component into a React project.

<Steps>
  <Step title="Install Node.js">
    * Download and install Node.js from the official website: [https://nodejs.org/](https://nodejs.org/)
    * Choose the LTS (Long Term Support) version for stability.
  </Step>

  <Step title="Create a new React project">
    * Open Command Prompt or PowerShell
    * Navigate to the directory where you want to create your project
    * Run the following command to create a new React project:

      ```bash  theme={null}
      npx create-react-app my-crew-app
      ```
    * Change into the project directory:

      ```bash  theme={null}
      cd my-crew-app
      ```
  </Step>

  <Step title="Install necessary dependencies">
    ```bash  theme={null}
    npm install react-dom
    ```
  </Step>

  <Step title="Create the CrewLead component">
    * Move the downloaded file `CrewLead.jsx` into the `src` folder of your project,
  </Step>

  <Step title="Modify your App.js to use the CrewLead component">
    * Open `src/App.js`
    * Replace its contents with something like this:

    ```jsx  theme={null}
    import React from 'react';
    import CrewLead from './CrewLead';

    function App() {
        return (
            <div className="App">
                <CrewLead baseUrl="YOUR_API_BASE_URL" bearerToken="YOUR_BEARER_TOKEN" />
            </div>
        );
    }

    export default App;
    ```

    * Replace `YOUR_API_BASE_URL` and `YOUR_BEARER_TOKEN` with the actual values for your API.
  </Step>

  <Step title="Start the development server">
    * In your project directory, run:

      ```bash  theme={null}
      npm start
      ```
    * This will start the development server, and your default web browser should open automatically to [http://localhost:3000](http://localhost:3000), where you'll see your React app running.
  </Step>
</Steps>


## Customization

You can then customise the `CrewLead.jsx` to add color, title etc

<Frame>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4673fd3ac9eedc1c83b777afb8cf09c9" alt="Customise React Component" data-og-width="1119" width="1119" data-og-height="939" height="939" data-path="images/enterprise/customise-react-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=551606e5340b4eb48fa2ca617486ab17 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4861d2caa401af697527bbafe3cfdb8a 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ce6d2304d336e487c9bfbd8e1fde5eaf 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1b2d7f443f10ff21f73e14ef42f91063 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=af6ddc00aa79e8b1606d74b587336a5d 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=997057d8f5ed2b15166ea3cec704a4f3 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=714c15d129b3db4bd96cdc55e80916dd" alt="Customise React Component" data-og-width="1058" width="1058" data-og-height="427" height="427" data-path="images/enterprise/customise-react-component-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5c589ec079cd09f29551136ee607d0a5 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=059851daaaf939d0a5bb2aa1598940cf 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3bad7a6f0f18aff57419ded53c398f15 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6753c201e535c8fcebd1d949436003c7 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=352df6d7283212880ef271a8fb673098 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/customise-react-component-2.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=725cfe8688b8135dd25290296d787dbf 2500w" />
</Frame>


## Next Steps

* Customize the component styling to match your application's design
* Add additional props for configuration
* Integrate with your application's state management
* Add error handling and loading states



---

**Navigation:** [← Previous](./11-replay-tasks-from-latest-crew-kickoff.md) | [Index](./index.md) | [Next →](./13-team-management.md)
