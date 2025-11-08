---
title: "Crewai: Configuration Steps"
description: "Configuration Steps section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Steps


Before you can start using Crew Studio, you need to configure your LLM connections:

<Steps>
  <Step title="Set Up LLM Connection">
    Go to the **LLM Connections** tab in your CrewAI AMP dashboard and create a new LLM connection.

    <Note>
      Feel free to use any LLM provider you want that is supported by CrewAI.
    </Note>

    Configure your LLM connection:

    * Enter a `Connection Name` (e.g., `OpenAI`)
    * Select your model provider: `openai` or `azure`
    * Select models you'd like to use in your Studio-generated Crews
      * We recommend at least `gpt-4o`, `o1-mini`, and `gpt-4o-mini`
    * Add your API key as an environment variable:
      * For OpenAI: Add `OPENAI_API_KEY` with your API key
      * For Azure OpenAI: Refer to [this article](https://blog.crewai.com/configuring-azure-openai-with-crewai-a-comprehensive-guide/) for configuration details
    * Click `Add Connection` to save your configuration

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c06fcdb008733c7e1d6ec7fcd055ff2c" alt="LLM Connection Configuration" data-og-width="2526" width="2526" data-og-height="1794" height="1794" data-path="images/enterprise/llm-connection-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=929f529b52c50511a773f2ec0791cd9a 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3f922308dfa3d65a392d5ebecec593dd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=df92dce860921dac542382ca3882decb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1772f4775c3f02e17d152bc00a08ba45 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=508cb4812120d6bc6b3010415f118a4a 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2eb75a3247fbc61ab727978b8a6ce371 2500w" />
    </Frame>
  </Step>

  <Step title="Verify Connection Added">
    Once you complete the setup, you'll see your new connection added to the list of available connections.

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3726ffaa33f0bfdf221dd542ae729f69" alt="Connection Added" data-og-width="1966" width="1966" data-og-height="532" height="532" data-path="images/enterprise/connection-added.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4acf6c926c288b5d32f9c537329b4611 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bdfd3df0a3d3f3ba1d2f91472471ba0 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1658dc464f8869ad3f0eb0595faf4048 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a0e1b1b559acc03bfbc3a40f17920e40 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=837c27260c5c258d9da4c306e4d16ae0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=649700c55072c94135d7a44e07b5f0df 2500w" />
    </Frame>
  </Step>

  <Step title="Configure LLM Defaults">
    In the main menu, go to **Settings → Defaults** and configure the LLM Defaults settings:

    * Select default models for agents and other components
    * Set default configurations for Crew Studio

    Click `Save Settings` to apply your changes.

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b773c2d7e8338e8dbf609ff45ce16eda" alt="LLM Defaults Configuration" data-og-width="2534" width="2534" data-og-height="1128" height="1128" data-path="images/enterprise/llm-defaults.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b08470ddaeb12d378083dff2e852934b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e58e547acb63b13b01fdf52c1771d42d 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c9b45ef41f6b3068580a4085c5c914cf 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4366e6bb2207f83d10b825a6e5393743 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1a48e293ccbcb1c990cfb0a56d386b32 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f11e748fbc1d3ef89abfef88b95ba9fb 2500w" />
    </Frame>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← What is Crew Studio?](./1523-what-is-crew-studio.md)

**Next:** [Using Crew Studio →](./1525-using-crew-studio.md)
