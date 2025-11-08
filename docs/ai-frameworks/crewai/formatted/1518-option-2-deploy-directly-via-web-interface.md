---
title: "Crewai: Option 2: Deploy Directly via Web Interface"
description: "Option 2: Deploy Directly via Web Interface section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Option 2: Deploy Directly via Web Interface


You can also deploy your crews directly through the CrewAI AMP web interface by connecting your GitHub account. This approach doesn't require using the CLI on your local machine.

<Steps>
  <Step title="Pushing to GitHub">
    You need to push your crew to a GitHub repository. If you haven't created a crew yet, you can [follow this tutorial](/en/quickstart).
  </Step>

  <Step title="Connecting GitHub to CrewAI AMP">
    1. Log in to [CrewAI AMP](https://app.crewai.com)
    2. Click on the button "Connect GitHub"

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e622053d392d9ca0033bb88b34d82f8d" alt="Connect GitHub Button" data-og-width="1021" width="1021" data-og-height="327" height="327" data-path="images/enterprise/connect-github.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=67a2ba40e2c5dabacfafcb2359e569cf 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=533ddd0da6106dc71b9cbcd010f89a5c 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d8a3f55321172ab1e4179c6d05f30b4d 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc5f7c278ecc22125a1f641454cec2d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d8f3da31bd39d97f37b7f405ef3b048 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7ce7bda27a7f94bb173f25fe9845a1cb 2500w" />
    </Frame>
  </Step>

  <Step title="Select the Repository">
    After connecting your GitHub account, you'll be able to select which repository to deploy:

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=937cf62f283090f134e299aa157aad22" alt="Select Repository" data-og-width="3366" width="3366" data-og-height="956" height="956" data-path="images/enterprise/select-repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3f5167362c6836f644ab356b61c7f8db 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c1293a61ff1fba1b19b8669b942595da 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ac1c94be313ab5c3c3f64741e3696be 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7991df0620583adeb443551dfbf8eeb8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1bf91d7875849fb251fa92c24c1564aa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=17ab305443f30d6f4796b2415564a3dc 2500w" />
    </Frame>
  </Step>

  <Step title="Set Environment Variables">
    Before deploying, you'll need to set up your environment variables to connect to your LLM provider or other services:

    1. You can add variables individually or in bulk
    2. Enter your environment variables in `KEY=VALUE` format (one per line)

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=84aa7644b9a1e20eb2e38309ce274ccb" alt="Set Environment Variables" data-og-width="3386" width="3386" data-og-height="606" height="606" data-path="images/enterprise/set-env-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c5521837a0ea86776e2ac13883f72750 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=98882c7ba545f4a09bc2248af54bc1ac 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=884ffc4ddc80104657dd60429f262254 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6f811c643a2268d264d95a3701a4d151 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=efd5564b6b4ffe6d68654cbdc8e515cc 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=51fb85358802539cb78c5dc7cf997b92 2500w" />
    </Frame>
  </Step>

  <Step title="Deploy Your Crew">
    1. Click the "Deploy" button to start the deployment process
    2. You can monitor the progress through the progress bar
    3. The first deployment typically takes around 10-15 minutes; subsequent deployments will be faster

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2eb5fa4cf040c65462a372b6667adc60" alt="Deploy Progress" data-og-width="3386" width="3386" data-og-height="1170" height="1170" data-path="images/enterprise/deploy-progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=91d47e6e3edc1df183acb360cbc6af1f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f917ef44ece66ef051db174b4dea47d8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dfc99edd2ff1678afa564ae33cb9c784 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=522b1ce917f9ecd15aee60c0e2241965 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=62ab85baa7a80d6fb98c50fdb7d588c7 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3190fa0b08cfbcdc75d385bde06535fa 2500w" />
    </Frame>

    Once deployment is complete, you'll see:

    * Your crew's unique URL
    * A Bearer token to protect your crew API
    * A "Delete" button if you need to remove the deployment
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Remove a deployment](./1517-remove-a-deployment.md)

**Next:** [⚠️ Environment Variable Security Requirements →](./1519-environment-variable-security-requirements.md)
