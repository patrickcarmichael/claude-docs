---
title: "Crewai: Setting Up HITL Workflows"
description: "Setting Up HITL Workflows section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← HITL Workflows](./2411-hitl-workflows.md)

**Next:** [Best Practices →](./2413-best-practices.md)
