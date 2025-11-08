---
title: "Crewai: Set Up Enterprise Governance for CrewAI"
description: "Set Up Enterprise Governance for CrewAI section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Set Up Enterprise Governance for CrewAI


**Why Enterprise Governance?**
If you are using CrewAI inside your organization, you need to consider several governance aspects:

* **Cost Management**: Controlling and tracking AI spending across teams
* **Access Control**: Managing which teams can use specific models
* **Usage Analytics**: Understanding how AI is being used across the organization
* **Security & Compliance**: Maintaining enterprise security standards
* **Reliability**: Ensuring consistent service across all users

Portkey adds a comprehensive governance layer to address these enterprise needs. Let's implement these controls step by step.

<Steps>
  <Step title="Create Virtual Key">
    Virtual Keys are Portkey's secure way to manage your LLM provider API keys. They provide essential controls like:

    * Budget limits for API usage
    * Rate limiting capabilities
    * Secure API key storage

    To create a virtual key:
    Go to [Virtual Keys](https://app.portkey.ai/virtual-keys) in the Portkey App. Save and copy the virtual key ID

    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/Virtual%20Key%20from%20Portkey%20Docs.png" width="500" />
    </Frame>

    <Note>
      Save your virtual key ID - you'll need it for the next step.
    </Note>
  </Step>

  <Step title="Create Default Config">
    Configs in Portkey define how your requests are routed, with features like advanced routing, fallbacks, and retries.

    To create your config:

    1. Go to [Configs](https://app.portkey.ai/configs) in Portkey dashboard
    2. Create new config with:
       ```json  theme={null}
       {
           "virtual_key": "YOUR_VIRTUAL_KEY_FROM_STEP1",
          	"override_params": {
             "model": "gpt-4o" // Your preferred model name
           }
       }
       ```
    3. Save and note the Config name for the next step

    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20Portkey%20Docs%20Config.png" width="500" />
    </Frame>
  </Step>

  <Step title="Configure Portkey API Key">
    Now create a Portkey API key and attach the config you created in Step 2:

    1. Go to [API Keys](https://app.portkey.ai/api-keys) in Portkey and Create new API key
    2. Select your config from `Step 2`
    3. Generate and save your API key

    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20API%20Key.png" width="500" />
    </Frame>
  </Step>

  <Step title="Connect to CrewAI">
    After setting up your Portkey API key with the attached config, connect it to your CrewAI agents:

    ```python  theme={null}
    from crewai import Agent, LLM
    from portkey_ai import PORTKEY_GATEWAY_URL

    # Configure LLM with your API key
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="YOUR_PORTKEY_API_KEY"
    )

    # Create agent with Portkey-enabled LLM
    researcher = Agent(
        role="Senior Research Scientist",
        goal="Discover groundbreaking insights about the assigned topic",
        backstory="You are an expert researcher with deep domain knowledge.",
        verbose=True,
        llm=portkey_llm
    )
    ```
  </Step>
</Steps>

<AccordionGroup>
  <Accordion title="Step 1: Implement Budget Controls & Rate Limits">
    ### Step 1: Implement Budget Controls & Rate Limits

    Virtual Keys enable granular control over LLM access at the team/department level. This helps you:

    * Set up [budget limits](https://portkey.ai/docs/product/ai-gateway/virtual-keys/budget-limits)
    * Prevent unexpected usage spikes using Rate limits
    * Track departmental spending

    #### Setting Up Department-Specific Controls:

    1. Navigate to [Virtual Keys](https://app.portkey.ai/virtual-keys) in Portkey dashboard
    2. Create new Virtual Key for each department with budget limits and rate limits
    3. Configure department-specific limits

    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/Virtual%20Key%20from%20Portkey%20Docs.png" width="500" />
    </Frame>
  </Accordion>

  <Accordion title="Step 2: Define Model Access Rules">
    ### Step 2: Define Model Access Rules

    As your AI usage scales, controlling which teams can access specific models becomes crucial. Portkey Configs provide this control layer with features like:

    #### Access Control Features:

    * **Model Restrictions**: Limit access to specific models
    * **Data Protection**: Implement guardrails for sensitive data
    * **Reliability Controls**: Add fallbacks and retry logic

    #### Example Configuration:

    Here's a basic configuration to route requests to OpenAI, specifically using GPT-4o:

    ```json  theme={null}
    {
    	"strategy": {
    		"mode": "single"
    	},
    	"targets": [
    		{
    			"virtual_key": "YOUR_OPENAI_VIRTUAL_KEY",
    			"override_params": {
    				"model": "gpt-4o"
    			}
    		}
    	]
    }
    ```

    Create your config on the [Configs page](https://app.portkey.ai/configs) in your Portkey dashboard.

    <Note>
      Configs can be updated anytime to adjust controls without affecting running applications.
    </Note>
  </Accordion>

  <Accordion title="Step 3: Implement Access Controls">
    ### Step 3: Implement Access Controls

    Create User-specific API keys that automatically:

    * Track usage per user/team with the help of virtual keys
    * Apply appropriate configs to route requests
    * Collect relevant metadata to filter logs
    * Enforce access permissions

    Create API keys through:

    * [Portkey App](https://app.portkey.ai/)
    * [API Key Management API](/en/api-reference/admin-api/control-plane/api-keys/create-api-key)

    Example using Python SDK:

    ```python  theme={null}
    from portkey_ai import Portkey

    portkey = Portkey(api_key="YOUR_ADMIN_API_KEY")

    api_key = portkey.api_keys.create(
        name="engineering-team",
        type="organisation",
        workspace_id="YOUR_WORKSPACE_ID",
        defaults={
            "config_id": "your-config-id",
            "metadata": {
                "environment": "production",
                "department": "engineering"
            }
        },
        scopes=["logs.view", "configs.read"]
    )
    ```

    For detailed key management instructions, see our [API Keys documentation](/en/api-reference/admin-api/control-plane/api-keys/create-api-key).
  </Accordion>

  <Accordion title="Step 4: Deploy & Monitor">
    ### Step 4: Deploy & Monitor

    After distributing API keys to your team members, your enterprise-ready CrewAI setup is ready to go. Each team member can now use their designated API keys with appropriate access levels and budget controls.

    Monitor usage in Portkey dashboard:

    * Cost tracking by department
    * Model usage patterns
    * Request volumes
    * Error rates
  </Accordion>
</AccordionGroup>

<Note>
  ### Enterprise Features Now Available

  **Your CrewAI integration now has:**

  * Departmental budget controls
  * Model access governance
  * Usage tracking & attribution
  * Security guardrails
  * Reliability features
</Note>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Choose which LLM to use for each agent based on your needs](./2269-choose-which-llm-to-use-for-each-agent-based-on-yo.md)

**Next:** [Frequently Asked Questions →](./2271-frequently-asked-questions.md)
