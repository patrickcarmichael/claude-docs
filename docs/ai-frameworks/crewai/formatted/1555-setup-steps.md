---
title: "Crewai: Setup Steps"
description: "Setup Steps section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup Steps


<Steps>
  <Step title="Connect your HubSpot account with CrewAI AMP">
    * Log in to your `CrewAI AMP account > Triggers`
    * Select `HubSpot` from the list of available triggers
    * Choose the HubSpot account you want to connect with CrewAI AMP
    * Follow the on-screen prompts to authorize CrewAI AMP access to your HubSpot account
    * A confirmation message will appear once HubSpot is successfully connected with CrewAI AMP
  </Step>

  <Step title="Create a HubSpot Workflow">
    * Log in to your `HubSpot account > Automations > Workflows > New workflow`
    * Select the workflow type that fits your needs (e.g., Start from scratch)
    * In the workflow builder, click the Plus (+) icon to add a new action.
    * Choose `Integrated apps > CrewAI > Kickoff a Crew`.
    * Select the Crew you want to initiate.
    * Click `Save` to add the action to your workflow

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d53acad518d2e330bd4a69ca76808b11" alt="HubSpot Workflow 1" data-og-width="670" width="670" data-og-height="556" height="556" data-path="images/enterprise/hubspot-workflow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=54aa0bc6e1080e9dfbd5184e23ebefe3 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9eaec24db82ba8a59ac9c43047ce2d1 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f100f688d3f1961f0328d4141f04ad99 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c2147f9de1f60270ef81c5d271acd272 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=aec4cc0e27775dd21cbfb35fad7c6634 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=24d1d4bb9cc84719f78166c6bfa5de81 2500w" />
    </Frame>
  </Step>

  <Step title="Use Crew results with other actions">
    * After the Kickoff a Crew step, click the Plus (+) icon to add a new action.
    * For example, to send an internal email notification, choose `Communications > Send internal email notification`
    * In the Body field, click `Insert data`, select `View properties or action outputs from > Action outputs > Crew Result` to include Crew data in the email
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a096e4d667b63a65b1061bdc5f659199" alt="HubSpot Workflow 2" data-og-width="670" width="670" data-og-height="437" height="437" data-path="images/enterprise/hubspot-workflow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ffe8190dbfdc46039f7ddfb586566ac2 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=066a379f6f677a48a07d66a61b192722 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=871c51f5376163d894e0945665a17b37 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=eb6be36a9c8432789077b82465038c16 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=448437694af0fd88f3d0667ecd6e9ef9 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0a1ef821542f93d1d51601eb3954273a 2500w" />
      </Frame>
    * Configure any additional actions as needed
    * Review your workflow steps to ensure everything is set up correctly
    * Activate the workflow
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b8e6f426200408867d0a09526a93f32f" alt="HubSpot Workflow 3" data-og-width="670" width="670" data-og-height="647" height="647" data-path="images/enterprise/hubspot-workflow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b59d6e2251da148d974ec0605a78acd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=04629b326d956c53658267c418818165 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=eae451ae67430e9283936cd3d06edb26 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=389235975e0ca14bbb3a6b1b307d7508 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0863f7fdf8ef41628ab5b2093700f25f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=89186e6b7ebc362512ea3dc05407dcec 2500w" />
      </Frame>
  </Step>
</Steps>

For more detailed information on available actions and customization options, refer to the [HubSpot Workflows Documentation](https://knowledge.hubspot.com/workflows/create-workflows).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./1554-prerequisites.md)

**Next:** [Kickoff Crew →](./1556-kickoff-crew.md)
