---
title: "Crewai: Setup Steps"
description: "Setup Steps section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup Steps


<Steps>
  <Step title="Ensure the CrewAI Slack trigger is set up">
    In the CrewAI dashboard, navigate to the **Triggers** section.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6d976bf9516d737af0b7ea3a77aa2b2a" alt="CrewAI Slack Integration" data-og-width="1962" width="1962" data-og-height="1052" height="1052" data-path="images/enterprise/slack-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ce8a2090ccca8027450db4f447f65cd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=72063bc9e37d7ca4f495cb4dcac4fd04 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bfb09bbf40fa85cff58485d75d6d2e55 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=30e1149f8bbe585c443d9b57c33d3888 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c6b943586531c6fab7eab1b9c2f61092 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=106a0fe6ed7e2f3a69b5bde02f21d860 2500w" />
    </Frame>

    Verify that Slack is listed and is connected.
  </Step>

  <Step title="Open your Slack channel">
    * Navigate to the channel where you want to kickoff the crew.
    * Type the slash command "**/kickoff**" to initiate the crew kickoff process.
    * You should see a  "**Kickoff crew**" appear as you type:
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cf16579e88e59903af9ac3f2ef374555" alt="Kickoff crew" data-og-width="601" width="601" data-og-height="157" height="157" data-path="images/enterprise/kickoff-slack-crew.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f43ffa15817823e76313f33c889f5708 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bd173c20d88c0bf4466f1af1098bb285 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=00d64ee5b69f4c9497f32dd18335f53e 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6a38124f5f963b15b1cc0d6acaa1996f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=94c6909651b61ec2b4de17687d1ce95a 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=47df98421d2a98e3fbc19015d2cb48ee 2500w" />
      </Frame>
    * Press Enter or select the "**Kickoff crew**" option. A dialog box titled "**Kickoff an AI Crew**" will appear.
  </Step>

  <Step title="Select the crew you want to start">
    * In the dropdown menu labeled "**Select of the crews online:**", choose the crew you want to start.
    * In the example below, "**prep-for-meeting**" is selected:
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7c92f688fcd7f1f0251cd90670014e34" alt="Kickoff crew dropdown" data-og-width="631" width="631" data-og-height="333" height="333" data-path="images/enterprise/kickoff-slack-crew-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7efe2a1a20f23311e914b0fdedf7532a 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2bb784762404d9d7713743e8da6f0057 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5aa472c131ee27c39c925b555f6d451d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18b84066d96edbacc103e57e99be592e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=208d754df14ea8bcd287990df3d6bd55 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=98efd80f079ee57494997f45e03455ed 2500w" />
      </Frame>
    * If your crew requires any inputs, click the "**Add Inputs**" button to provide them.
      <Note>
        The "**Add Inputs**" button is shown in the example above but is not yet clicked.
      </Note>
  </Step>

  <Step title="Click Kickoff and wait for the crew to complete">
    * Once you've selected the crew and added any necessary inputs, click "**Kickoff**" to start the crew.
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e5bebbf61fb92832dc1ebef0a77d5654" alt="Kickoff crew" data-og-width="628" width="628" data-og-height="771" height="771" data-path="images/enterprise/kickoff-slack-crew-kickoff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3c04a8e5c5f45211135c3b31423b3baf 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6d444a78f6991956f03eb92c8e83de0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=789ad738a8dd10a4e9ad83de0be5faf3 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a1fec0a13f00082ab70c7c12744d2954 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2d7e271cf05848aaebdd7445923f6daf 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=912bf7b4abb0d51b46ddf3f9d02230c2 2500w" />
      </Frame>
    * The crew will start executing and you will see the results in the Slack channel.
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a3d451c03c3ff7ebf64eb9bb1b41c18c" alt="Kickoff crew results" data-og-width="653" width="653" data-og-height="678" height="678" data-path="images/enterprise/kickoff-slack-crew-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fcaf9677647222c1a7c716ed197c9c60 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bf3ff58196c634ebbaa545ad815593ba 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=34fd1fcef59569b7503b47587e29b31b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ceeb582a0ea6ce7c4ce86080c5f09506 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7b1bac2cd281b5770f3ad33d13fc3e22 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1bef274ced3f62e923578f882cc36fc8 2500w" />
      </Frame>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./1592-prerequisites.md)

**Next:** [Tips →](./1594-tips.md)
