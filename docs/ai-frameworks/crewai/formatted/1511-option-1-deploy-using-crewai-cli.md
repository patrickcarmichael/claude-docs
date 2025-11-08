---
title: "Crewai: Option 1: Deploy Using CrewAI CLI"
description: "Option 1: Deploy Using CrewAI CLI section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Option 1: Deploy Using CrewAI CLI


The CLI provides the fastest way to deploy locally developed crews to the Enterprise platform.

<Steps>
  <Step title="Install CrewAI CLI">
    If you haven't already, install the CrewAI CLI:

    ```bash  theme={null}
    pip install crewai[tools]
    ```

    <Tip>
      The CLI comes with the main CrewAI package, but the `[tools]` extra ensures you have all deployment dependencies.
    </Tip>
  </Step>

  <Step title="Authenticate with the Enterprise Platform">
    First, you need to authenticate your CLI with the CrewAI AMP platform:

    ```bash  theme={null}
    # If you already have a CrewAI AMP account, or want to create one:
    crewai login
    ```

    When you run either command, the CLI will:

    1. Display a URL and a unique device code
    2. Open your browser to the authentication page
    3. Prompt you to confirm the device
    4. Complete the authentication process

    Upon successful authentication, you'll see a confirmation message in your terminal!
  </Step>

  <Step title="Create a Deployment">
    From your project directory, run:

    ```bash  theme={null}
    crewai deploy create
    ```

    This command will:

    1. Detect your GitHub repository information
    2. Identify environment variables in your local `.env` file
    3. Securely transfer these variables to the Enterprise platform
    4. Create a new deployment with a unique identifier

    On successful creation, you'll see a message like:

    ```shell  theme={null}
    Deployment created successfully!
    Name: your_project_name
    Deployment ID: 01234567-89ab-cdef-0123-456789abcdef
    Current Status: Deploy Enqueued
    ```
  </Step>

  <Step title="Monitor Deployment Progress">
    Track the deployment status with:

    ```bash  theme={null}
    crewai deploy status
    ```

    For detailed logs of the build process:

    ```bash  theme={null}
    crewai deploy logs
    ```

    <Tip>
      The first deployment typically takes 10-15 minutes as it builds the container images. Subsequent deployments are much faster.
    </Tip>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./1510-prerequisites.md)

**Next:** [Additional CLI Commands →](./1512-additional-cli-commands.md)
