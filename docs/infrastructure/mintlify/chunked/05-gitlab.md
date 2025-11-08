**Navigation:** [← Previous](./04-fonts.md) | [Index](./index.md) | [Next →](./06-vercel.md)

# GitLab
Source: https://mintlify.com/docs/deploy/gitlab

Sync your docs with a GitLab repo

We use access tokens and webhooks to authenticate and sync changes between GitLab and Mintlify.

* Mintlify uses access tokens to pull information from GitLab.
* GitLab uses webhooks to notify Mintlify when changes are made, enabling preview deployments for merge requests.


## Set up the connection

<Note>
  **HTTPS cloning required**: Your GitLab project must have HTTPS cloning enabled for Mintlify to access your repository. You can verify this in GitLab by going to your project's **Settings** > **General** > **Visibility and access controls** section.
</Note>

<Steps>
  <Step title="Find your project ID">
    In your GitLab project, navigate to **Settings** > **General** and locate your **Project ID**.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4aae3ff6adbb509b607a63a4998992d0" alt="The General Settings page in the GitLab dashboard. The Project ID is highlighted." data-og-width="950" width="950" data-og-height="775" height="775" data-path="images/gitlab/gitlab-project-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=88f0bf511026ec7ed08f681ec90daf60 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e724501d42bcadf2afee5a3383864b8f 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7292cf914432f5773b27d0f7a26f77e8 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=df4fc24c66567b6fa8aaf96ef84be3db 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c18b327b668e3111c2c365bd28804d4f 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6d58f398e6a9dd837c15ef62bd84eca6 2500w" />
    </Frame>
  </Step>

  <Step title="Generate an access token">
    Navigate to **Settings** > **Access Tokens** and select **Add new token**.

    Configure the token with these settings:

    * **Name**: Mintlify
    * **Role**: Maintainer (required for private repos)
    * **Scopes**: `api` and `read_api`

    Click **Create project access token** and copy the token.

    <Note>
      If Project Access Tokens are not available, you can use a Personal Access Token instead. Note that Personal Access Tokens expire and must be updated.
    </Note>

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=59ef23c54d88cdd723632086bced658b" alt="The Access tokens page in the GitLab dashboard. The settings to configure for Mintlify are highlighted." data-og-width="1166" width="1166" data-og-height="904" height="904" data-path="images/gitlab/gitlab-project-access-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ed79687a8c28122d877619f87c2f10f5 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=eee224427bd45c62f4b300ff35e18c20 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c58082216f7abcdca53dae175bc50e05 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4391e8f8149b4750ce5727e90434d4cc 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0b593dfe4be4578274123931ec3fd9a8 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=072f13cde75508169457c8bec172183f 2500w" />
    </Frame>
  </Step>

  <Step title="Set up the connection">
    In the [Mintlify dashboard](https://dashboard.mintlify.com/settings/deployment/git-settings):

    1. Enter your project ID and access token.
    2. Complete any other required configurations.
    3. Click **Save Changes**.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=882adfd7c2a3349608bc6240aa5b467d" alt="The Git Settings page in the Mintlify dashboard. The GitLab configuration settings are highlighted." data-og-width="2994" width="2994" data-og-height="1704" height="1704" data-path="images/gitlab/gitlab-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=92f573381038c697fb061a9793cbea4d 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=634591e44b502650a859b04aba4f3f07 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=82eda65fcc9475daf4c9d20eb1f5ac77 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cc48a4ac66d50a65dcc4913111b26943 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7932ae6cf49e9ba69d8133ff9f17fa23 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=106cb2e8a7eb3bdaef7f994bfcd31da8 2500w" />
    </Frame>
  </Step>
</Steps>


## Create the webhook

Webhooks allow us to receive events when changes are made so that we can
automatically trigger deployments.

<Steps>
  <Step title="Navigate to Settings > Webhooks and click 'Add new Webhook'">
    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=760e8faa2437ecf8ff2739c4dfa0bdc4" alt="Screenshot of the Webhooks page in the GitLab dashboard." data-og-width="3014" width="3014" data-og-height="1704" height="1704" data-path="images/gitlab/gitlab-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=08c3f527fcd75de5c88682d6fc08018e 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c7579b9b8372dc9781dd1da38b1e404e 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a0225726564aa9987b44bfb35f750c35 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=006a5aa0f321344da2d528c928f3bf4d 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=99c65eb0a83da2b793c1608ea3a47cbc 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a8943cc826fc0bb2ab6db79ece619d8c 2500w" />
    </Frame>
  </Step>

  <Step title="Set up URL and webhook">
    In the "URL" field, enter the endpoint `https://leaves.mintlify.com/gitlab-webhook` and name the webhook "Mintlify".
  </Step>

  <Step title="Paste token">
    Paste the Webhook token generated after setting up the connection.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=60c68dd86fa476e90af8cec2e5ee7c81" alt="Screenshot of the GitLab connection in the Mintlify dashboard. The Show Webtoken button is highlighted." data-og-width="555" width="555" data-og-height="527" height="527" data-path="images/gitlab/gitlab-show-webtoken.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=90210c502642ebd9e493440279b675b7 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6533a778a099d0c4fc65e04e64587444 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6f4e8533153ee8efa98864377656a377 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b29eaa2ea7df3ca4e21fba49835a8360 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c1e857545a40103103e5958f03faecc7 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=74798e74cae86d02520e756f0d7cfb37 2500w" />
    </Frame>
  </Step>

  <Step title="Select events">
    Select these events to trigger the webhook:

    * **Push events** (All branches)
    * **Merge requests events**

    When you're done it should look like this:

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=00c0ce70ce9e8dbc2712f71aaeef3362" alt="The Webhook page in the GitLab dashboard. The settings to configure for Mintlify are highlighted." data-og-width="1161" width="1161" data-og-height="1740" height="1740" data-path="images/gitlab/gitlab-project-webtoken.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d78ea01ef0a043783195c6d548d20eea 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b77667d112aa91a2db02ab5fb356f733 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7b2f55fe589a11b9e5ce5633b62c34ad 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=531491f03816a11e44b651c921dc1789 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=24770ed142d0cf9b7bfb0dc307c13449 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e8644419580dc23875105fb06f3f4433 2500w" />
    </Frame>
  </Step>

  <Step title="Test the Webhook">
    After creating the Webhook, click the "Test" dropdown and select "Push events" to send a sample payload to ensure it's configured correctly. It'll say "Hook executed successfully: HTTP 200" if configured correctly.

    This will help you verify that everything is working correctly and that your documentation will sync properly with your GitLab repository.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3ad52f7ac39124a4c03944256d0b79d3" alt="Screenshot of the GitLab Webhooks page. The 'Push events' menu item is highlighted in the 'Test' menu." data-og-width="1161" width="1161" data-og-height="724" height="724" data-path="images/gitlab/gitlab-project-webtoken-test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d174db5e7ba73d19a9431adca65ebe6c 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9dfb2d09246cb81c0074a2a429e940f7 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3db14fb7784c9380f627336622f73a8f 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=68dc65bc33081a8a08c869f7f1ea8761 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ebd368461ffa4880d63a3ecbda59d84e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1e510fe852d154bb8aca3dd2c20387aa 2500w" />
    </Frame>
  </Step>
</Steps>



# Monorepo setup
Source: https://mintlify.com/docs/deploy/monorepo

Deploy your docs from a repo that contains multiple projects

Configure Mintlify to deploy documentation from a specific directory within a monorepo. This setup allows you to maintain documentation alongside your code in repositories that contain multiple projects or services.


## Prerequisites

* Admin access to your Mintlify project.
* Documentation files organized in a dedicated directory within your monorepo.
* A valid `docs.json` in your documentation directory.


## Configure monorepo deployment

<Steps>
  <Step title="Access Git settings">
    Navigate to [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) in your dashboard.

    <Frame>
      <img className="block dark:hidden my-0 pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=796f90a80651694cb858c77f4f1145a8" alt="The project settings panel in the Git Settings menu. The Set up as monorepo toggle button is enabled and a path to the /docs directory is specified." data-og-width="1350" width="1350" data-og-height="900" height="900" data-path="images/monorepo-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=097e11d375af49c9617962a77d2ce9c0 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f960d33286f33cd98ffd3e9f62b25be0 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e26e53043300bb5d6ff3bc2188403a18 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dbbd8b22e7da94e7c7cb5dff758c4c21 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1c6427d476468f4a3377ad9c948b7058 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3e745697b35f6aa8c09ec488847b029a 2500w" />

      <img className="hidden dark:block my-0 pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=03624a6ce64b3c3d504e27585cf857aa" alt="The project settings panel in the Git Settings menu. The Set up as monorepo toggle button is enabled and a path to the /docs directory is specified." data-og-width="1350" width="1350" data-og-height="900" height="900" data-path="images/monorepo-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=afcec75c9db2d7ecfff4a1930f991fc3 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ec31e2a26d6e744530db890ffaa3e435 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=6d2915f5e45882bdc0c333e9db950939 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=85f043394c8d5eb8b97b75bfa4f56e4c 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=5efddceac87ddd8ca95c627f9c8ac8b4 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c5d92cfbf8d90ddf69325c206c50e577 2500w" />
    </Frame>
  </Step>

  <Step title="Set your documentation path">
    1. Select the **Set up as monorepo** toggle button.
    2. Enter the relative path to your docs directory. For example, if your docs are in the `docs` directory, enter `/docs`.

    <Note>
      Do not include a trailing slash in the path.
    </Note>

    3. Select **Save changes**.
  </Step>
</Steps>



# Personalization setup
Source: https://mintlify.com/docs/deploy/personalization-setup

Let users log in for customized documentation experiences

Personalization customizes your documentation for each user when they are logged in. For example, you can prefill their API keys, show content specific to their plan or role, or hide sections they don't need access to.


## Personalization features

Customize content with these personalization capabilities.

### API key prefilling

Automatically populate API playground fields with user-specific values by returning matching field names in your user data. The field names in your user data must exactly match the names in the API playground for automatic prefilling to work.

### Dynamic MDX content

Display dynamic content based on user information like name, plan, or organization using the `user` variable.

```jsx  theme={null}
Welcome back, {user.firstName}! Your {user.org?.plan} plan includes...
```

See the [User data format](#user-data-format) section below for detailed examples and implementation guidance.

### Page visibility

Restrict which pages are visible to your users by adding `groups` fields to your pages' frontmatter. By default, every page is visible to every user.

Users will only see pages for `groups` that they are in.

```mdx  theme={null}
---
title: "Managing your users"
description: "Adding and removing users from your organization"
groups: ["admin"]
---
```


## User data format

When implementing personalization, your system returns user data in a specific format that enables content customization. This data can be sent as either a raw JSON object or within a signed JWT, depending on your handshake method. The shape of the data is the same for both.

```tsx  theme={null}
type User = {
  expiresAt?: number;
  groups?: string[];
  content?: Record<string, any>;
  apiPlaygroundInputs?: {
    header?: Record<string, any>;
    query?: Record<string, any>;
    cookie?: Record<string, any>;
    server?: Record<string, string>;
  };
};
```

<ParamField path="expiresAt" type="number">
  Session expiration time in **seconds since epoch**. If the user loads a page after this time, their stored data is automatically deleted and they must reauthenticate.
  <Warning><b>For JWT handshakes:</b> This differs from the JWT's `exp` claim, which determines when a JWT is considered invalid. Set the JWT `exp` claim to a short duration (10 seconds or less) for security. Use `expiresAt` for the actual session length (hours to weeks).</Warning>
</ParamField>

<ParamField path="groups" type="string[]">
  List of groups the user belongs to. Pages with matching `groups` in their frontmatter are visible to this user.

  **Example**: User with `groups: ["admin", "engineering"]` can access pages tagged with either the `admin` or `engineering` groups.
</ParamField>

<ParamField path="content" type="object">
  Custom data accessible in your `MDX` content via the `user` variable. Use this for dynamic personalization throughout your documentation.

  **Basic example**:

  ```json  theme={null}
  { "firstName": "Ronan", "company": "Acme Corp", "plan": "Enterprise" }
  ```

  **Usage in `MDX`**:

  ```mdx  theme={null}
  Welcome back, {user.firstName}! Your {user.plan} plan includes...
  ```

  With the example `user` data, this would render as: Welcome back, Ronan! Your Enterprise plan includes...

  **Advanced conditional rendering**:

  ```jsx  theme={null}
  Authentication is an enterprise feature. {
    user.org === undefined
      ? <>To access this feature, first create an account at the <a href="https://dashboard.mintlify.com/login">Mintlify dashboard</a>.</>
      : user.org.plan !== 'enterprise'
        ? <>You are currently on the ${user.org.plan ?? 'free'} plan. See <a href="https://mintlify.com/pricing">our pricing page</a> for information about upgrading.</>
        : <>To request this feature for your enterprise org, contact your admin.</>
  }
  ```

  <Note>
    The information in `user` is only available for logged-in users. For logged-out users, the value of `user` will be `{}`. To prevent the page from crashing for logged-out users, always use optional chaining on your `user` fields. For example, `{user.org?.plan}`.
  </Note>
</ParamField>

<ParamField path="apiPlaygroundInputs" type="object">
  User-specific values that prefill API playground fields. Saves users time by auto-populating their data when testing APIs.

  **Example**:

  ```json  theme={null}
  {
    "header": { "X-API-Key": "user_api_key_123" },
    "server": { "subdomain": "foo" },
    "query": { "org_id": "12345" }
  }
  ```

  If a user makes requests at a specific subdomain, you can send `{ server: { subdomain: 'foo' } }` as an `apiPlaygroundInputs` field. This value will be prefilled on any API page with the `subdomain` value.

  <Note>The `header`, `query`, and `cookie` fields will only prefill if they are part of your [OpenAPI security scheme](https://swagger.io/docs/specification/authentication/). If a field is in either the `Authorization` or `Server` sections, it will prefill. Creating a standard header parameter named `Authorization` will not enable this feature.</Note>
</ParamField>

### Example user data

```json  theme={null}
{
  "expiresAt": 1735689600,
  "groups": ["admin", "beta-users"],
  "content": {
    "firstName": "Jane",
    "lastName": "Smith",
    "company": "TechCorp",
    "plan": "Enterprise",
    "region": "us-west"
  },
  "apiPlaygroundInputs": {
    "header": {
      "Authorization": "Bearer abc123",
      "X-Org-ID": "techcorp"
    },
    "server": {
      "environment": "production",
      "region": "us-west"
    }
  }
}
```


## Configuring personalization

Select the handshake method that you want to configure.

<Tabs>
  <Tab title="JWT">
    ### Prerequisites

    * A login system that can generate and sign JWTs
    * A backend service that can create redirect URLs

    ### Implementation

    <Steps>
      <Step title="Generate a private key.">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Personalization**.
        3. Select **JWT**.
        4. Enter the URL of your existing login flow and select **Save changes**.
        5. Select **Generate new key**.
        6. Store your key securely where it can be accessed by your backend.
      </Step>

      <Step title="Integrate Mintlify personalization into your login flow.">
        Modify your existing login flow to include these steps after user login:

        * Create a JWT containing the logged-in user's info in the `User` format. See the [User data format](#user-data-format) section above for more information.
        * Sign the JWT with the secret key, using the ES256 algorithm.
        * Create a redirect URL back to your docs, including the JWT as the hash.
      </Step>
    </Steps>

    ### Example

    Your documentation is hosted at `docs.foo.com`. You want your docs to be separate from your dashboard (or you don't have a dashboard) and enable personalization.

    Generate a JWT secret. Then create a login endpoint at `https://foo.com/docs-login` that initiates a login flow to your documentation.

    After verifying user credentials:

    * Generate a JWT with user data in Mintlify's format.
    * Sign the JWT and redirect to `https://docs.foo.com#{SIGNED_JWT}`.

    ```ts  theme={null}
    import * as jose from 'jose';
    import { Request, Response } from 'express';

    const TWO_WEEKS_IN_MS = 1000 * 60 * 60 * 24 * 7 * 2;

    const signingKey = await jose.importPKCS8(process.env.MINTLIFY_PRIVATE_KEY, 'ES256');

    export async function handleRequest(req: Request, res: Response) {
      const user = {
        expiresAt: Math.floor((Date.now() + TWO_WEEKS_IN_MS) / 1000),
        groups: res.locals.user.groups,
        content: {
          firstName: res.locals.user.firstName,
          lastName: res.locals.user.lastName,
        },
      };

      const jwt = await new jose.SignJWT(user)
        .setProtectedHeader({ alg: 'ES256' })
        .setExpirationTime('10 s')
        .sign(signingKey);

      return res.redirect(`https://docs.foo.com#${jwt}`);
    }
    ```

    ### Preserving page anchors

    To redirect users to specific sections after login, use this URL format: `https://docs.foo.com/page#jwt={SIGNED_JWT}&anchor={ANCHOR}`.

    **Example**:

    * Original URL: `https://docs.foo.com/quickstart#step-one`
    * Redirect URL: `https://docs.foo.com/quickstart#jwt={SIGNED_JWT}&anchor=step-one`
  </Tab>

  <Tab title="OAuth 2.0">
    ### Prerequisites

    * An OAuth server that supports the Auth Code with PKCE Flow
    * Ability to create an API endpoint accessible by OAuth access tokens

    ### Implementation

    <Steps>
      <Step title="Create user info API endpoint.">
        Create an API endpoint that:

        * Accepts OAuth access tokens for authentication.
        * Returns user data in the `User` format. See the [User data format](#user-data-format) section above for more information.
        * Defines the scopes for access.
      </Step>

      <Step title="Configure your OAuth personalization settings.">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Personalization**.
        3. Select **OAuth** and configure these fields:

        * **Authorization URL**: Your OAuth authorization endpoint.
        * **Client ID**: Your OAuth 2.0 client identifier.
        * **Scopes**: Permissions to request. Copy the **entire** scope string (for example, for a scope like `provider.users.docs`, copy the complete `provider.users.docs`). Must match the scopes of the endpoint that you configured in the first step.
        * **Token URL**: Your OAuth token exchange endpoint.
        * **Info API URL**: Endpoint to retrieve user data for personalization. Created in the first step.

        4. Select **Save changes**
      </Step>

      <Step title="Configure your OAuth server.">
        1. Copy the **Redirect URL** from your [authentication settings](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Add this URL as an authorized redirect URL in your OAuth server configuration.
      </Step>
    </Steps>

    ### Example

    Your documentation is hosted at `foo.com/docs` and you have an existing OAuth server that supports the PKCE flow. You want to personalize your docs based on user data.

    **Create a user info endpoint** at `api.foo.com/docs/user-info`, which requires an OAuth access token with the `provider.users.docs` scope and responds with the user's custom data:

    ```json  theme={null}
    {
      "content": {
        "firstName": "Jane",
        "lastName": "Doe"
      },
      "groups": ["engineering", "admin"]
    }
    ```

    **Configure your OAuth server details** in your dashboard:

    * **Authorization URL**: `https://auth.foo.com/authorization`
    * **Client ID**: `ydybo4SD8PR73vzWWd6S0ObH`
    * **Scopes**: `['docs-user-info']`
    * **Token URL**: `https://auth.foo.com/exchange`
    * **Info API URL**: `https://api.foo.com/docs/user-info`

    **Configure your OAuth server** to allow redirects to your callback URL.
  </Tab>

  <Tab title="Shared session">
    ### Prerequisites

    * A dashboard or user portal with cookie-based session authentication.
    * Ability to create an API endpoint at the same origin or subdomain as your dashboard.
      * If your dashboard is at `foo.com`, the **API URL** must start with `foo.com` or `*.foo.com`.
      * If your dashboard is at `dash.foo.com`, the **API URL** must start with `dash.foo.com` or `*.dash.foo.com`.
    * Your docs are hosted at the same domain or subdomain as your dashboard.
      * If your dashboard is at `foo.com`, your **docs** must be hosted at `foo.com` or `*.foo.com`.
      * If your dashboard is at `*.foo.com`, your **docs** must be hosted at `foo.com` or `*.foo.com`.

    ### Implementation

    <Steps>
      <Step title="Create user info API endpoint.">
        Create an API endpoint that:

        * Uses your existing session authentication to identify users
        * Returns user data in the `User` format (see the [User data format](#user-data-format) section above)
        * If the API domain and the docs domain **do not exactly match**:
          * Add the docs domain to your API's `Access-Control-Allow-Origin` header (must not be `*`).
          * Set your API's `Access-Control-Allow-Credentials` header to `true`.
          <Warning>
            Only enable CORS headers on this specific endpoint, not your entire dashboard API.
          </Warning>
      </Step>

      <Step title="Configure your personalization settings">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Personalization**.
        3. Select **Shared Session**.
        4. Enter your **Info API URL**, which is the endpoint from the first step.
        5. Enter your **Login URL**, where users log into your dashboard.
        6. Select **Save changes**.
      </Step>
    </Steps>

    ### Examples

    #### Dashboard at subdomain, docs at subdomain

    You have a dashboard at `dash.foo.com`, which uses cookie-based session authentication. Your dashboard API routes are hosted at `dash.foo.com/api`. You want to set up personalization for your docs hosted at `docs.foo.com`.

    **Setup process**:

    1. **Create endpoint** `dash.foo.com/api/docs/user-info` that identifies users via session authentication and responds with their user data.
    2. **Add CORS headers** for this route only:
       * `Access-Control-Allow-Origin`: `https://docs.foo.com`
       * `Access-Control-Allow-Credentials`: `true`
    3. **Configure API URL** in authentication settings: `https://dash.foo.com/api/docs/user-info`.

    #### Dashboard at subdomain, docs at root

    You have a dashboard at `dash.foo.com`, which uses cookie-based session authentication. Your dashboard API routes are hosted at `dash.foo.com/api`. You want to set up personalization for your docs hosted at `foo.com/docs`.

    **Setup process**:

    1. **Create endpoint** `dash.foo.com/api/docs/user-info` that identifies users via session authentication and responds with their user data.
    2. **Add CORS headers** for this route only:
       * `Access-Control-Allow-Origin`: `https://foo.com`
       * `Access-Control-Allow-Credentials`: `true`
    3. **Configure API URL** in authentication settings: `https://dash.foo.com/api/docs/user-info`.

    #### Dashboard at root, docs at root

    You have a dashboard at `foo.com/dashboard`, which uses cookie-based session authentication. Your dashboard API routes are hosted at `foo.com/api`. You want to set up personalization for your docs hosted at `foo.com/docs`.

    **Setup process**:

    1. **Create endpoint** `foo.com/api/docs/user-info` that identifies users via session authentication and responds with their user data.
    2. **Configure API URL** in authentication settings: `https://foo.com/api/docs/user-info`

    <Note>
      No CORS configuration is needed since the dashboard and docs share the same domain.
    </Note>
  </Tab>
</Tabs>



# Preview deployments
Source: https://mintlify.com/docs/deploy/preview-deployments

Preview changes to your docs in a live deployment

<Info>
  Preview deployments are available on [Pro and Enterprise plans](https://mintlify.com/pricing?ref=preview-deployments).
</Info>

Preview deployments let you see how changes to your docs will look before merging to production. Each preview creates a shareable URL that updates automatically as you push new changes.


## Creating preview deployments

Preview deployments are created automatically through pull requests or manually from your dashboard.

### Automatic previews

When you create a pull request, the Mintlify bot automatically adds a link to view the preview deployment in your pull request. The preview updates each time you push new commits to the branch.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4cbf574001b521afbd8c9f6717ed907f" alt="Link to view deployment in the pull request timeline" className="block dark:hidden" data-og-width="1704" width="1704" data-og-height="142" height="142" data-path="images/previews/preview-deployment-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=ffa4ba05f4e3f34bd5ad947743959df2 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a87ea5b13d3444849a8fab4a43a5fc22 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1ce1ff2e47b42af3db49c2394f8837f2 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f6b44ca1a53080b2d8b8252784aec487 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=bd5d0e2d7721005d6d7740a96a996ff5 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e217516260f683cf2417a7ef75e8db8a 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=9fbb5054761316d1bbb8168646ed51bf" alt="Link to view deployment in the pull request timeline" className="hidden dark:block" data-og-width="1704" width="1704" data-og-height="142" height="142" data-path="images/previews/preview-deployment-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e7b687ed13f8af142c95a89815b42498 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=ebabc65e5a7fc6852d7c94632119f96a 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=6ca64fb1d342b667c40a1b7cee5f13f6 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=24a0e64ff92331d88950db41a9240409 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=fc090479eb70d57448ad26bf279f8b3a 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/preview-deployment-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=50f581e8856cb179d142197218c956cc 2500w" />
</Frame>

### Manual previews

You can manually create a preview for any branch.

1. Go to your [dashboard](https://dashboard.mintlify.com/).
2. Select **Previews**.
3. Select **Create preview**.
4. Enter your branch name.
5. Select **Create deployment**.


## Redeploying a preview

Redeploy a preview to refresh content or retry after a failed deployment.

1. Select the preview from your [dashboard](https://dashboard.mintlify.com/).
2. Select **Redeploy**.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=eaa1711b0c580931036f1d1f4685312e" alt="The Previews menu with the deploy button emphasized by an orange rectangle." className="block dark:hidden" data-og-width="2104" width="2104" data-og-height="634" height="634" data-path="images/previews/redeploy-preview-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=8e14a4269e5e49c5f58704cfb9c7c3ee 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f982b0d0dbb6615c83b1a370e832e22e 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=bcc1ac87bc01dbd392c2fed61ac977d7 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=636df2e9155b22989c03e222db33227a 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c65406f8131b395506026be9f46dc646 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1e193e05303626f9c5ea4a03986a33bf 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=086e0340522fc6a620e47e3e35703ae2" alt="The Previews menu with the deploy button emphasized by an orange rectangle." className="hidden dark:block" data-og-width="2104" width="2104" data-og-height="634" height="634" data-path="images/previews/redeploy-preview-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4b646047473c193d3b112a622da00369 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=5b1cd268146f7799d9a52e9a960b86bf 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0b1b451fd93ed8c27815db88e77e9daf 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=57d3acd1587110a80bf80ed4d0b23f24 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=d05748dbe4b8008f53fcc2da6ec3cde7 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/previews/redeploy-preview-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=d084422d4921243da615209a1d92eb89 2500w" />
</Frame>


## Sharing preview deployments

Preview deployments can be publicly accessible or restricted to authenticated users.

**Public access**: Preview URLs are publicly viewable by default. Share a preview link with anyone who needs to review your changes.

**Restricted access**: Enable preview deployment authentication to limit preview access to authenticated Mintlify users only. See [Authentication Setup](/deploy/authentication-setup) for more information.



# Reverse proxy
Source: https://mintlify.com/docs/deploy/reverse-proxy

Configure a custom reverse proxy to serve your documentation

<Note>
  Reverse proxy configurations are only supported for [Custom plans](https://mintlify.com/pricing?ref=reverse-proxy).
</Note>

To serve your documentation through a custom reverse proxy, you must configure routing rules, caching policies, and header forwarding.

When you implement a reverse proxy, monitor for potential issues with domain verification, SSL certificate provisioning, authentication flows, performance, and analytics tracking.


## Routing configuration

Proxy these paths to your Mintlify subdomain with the specified caching policies:

| Path                              | Destination                     | Caching       |
| --------------------------------- | ------------------------------- | ------------- |
| `/.well-known/acme-challenge/*`   | `<your-subdomain>.mintlify.app` | No cache      |
| `/.well-known/vercel/*`           | `<your-subdomain>.mintlify.app` | No cache      |
| `/mintlify-assets/_next/static/*` | `<your-subdomain>.mintlify.app` | Cache enabled |
| `/_mintlify/*`                    | `<your-subdomain>.mintlify.app` | No cache      |
| `/*`                              | `<your-subdomain>.mintlify.app` | No cache      |
| `/`                               | `<your-subdomain>.mintlify.app` | No cache      |


## Required header configuration

Configure your reverse proxy with these header requirements:

* **Origin**: Contains the target subdomain `<your-subdomain>.mintlify.app`
* **X-Forwarded-For**: Preserves client IP information
* **X-Forwarded-Proto**: Preserves original protocol (HTTP/HTTPS)
* **X-Real-IP**: Forwards the real client IP address
* **User-Agent**: Forwards the user agent

<Warning>
  Ensure that the `Host` header is not forwarded
</Warning>


## Example nginx configuration

```nginx  theme={null}
server {
    listen 80;
    server_name <your-domain>.com;

    # Let's Encrypt verification paths
    location ~ ^/\.well-known/acme-challenge/ {
        proxy_pass https://<your-subdomain>.mintlify.app;
        proxy_set_header Origin <your-subdomain>.mintlify.app;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header User-Agent $http_user_agent;

        # Disable caching for verification paths
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # Vercel verification paths
    location ~ ^/\.well-known/vercel/ {
        proxy_pass https://<your-subdomain>.mintlify.app;
        proxy_set_header Origin <your-subdomain>.mintlify.app;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header User-Agent $http_user_agent;

        # Disable caching for verification paths
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # Static assets with caching
    location ~ ^/mintlify-assets/_next/static/ {
        proxy_pass https://<your-subdomain>.mintlify.app;
        proxy_set_header Origin <your-subdomain>.mintlify.app;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header User-Agent $http_user_agent;

        # Enable caching for static assets
        add_header Cache-Control "public, max-age=86400";
    }

    # Mintlify-specific paths
    location ~ ^/_mintlify/ {
        proxy_pass https://<your-subdomain>.mintlify.app;
        proxy_set_header Origin <your-subdomain>.mintlify.app;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header User-Agent $http_user_agent;

        # Disable caching for Mintlify paths
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # Root path
    location = / {
        proxy_pass https://<your-subdomain>.mintlify.app;
        proxy_set_header Origin <your-subdomain>.mintlify.app;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header User-Agent $http_user_agent;

        # Disable caching for dynamic content
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # All other documentation paths
    location / {
        proxy_pass https://<your-subdomain>.mintlify.app;
        proxy_set_header Origin <your-subdomain>.mintlify.app;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header User-Agent $http_user_agent;

        # Disable caching for dynamic content
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }
}
```


## Troubleshooting

### 404 error

**Symptoms**: Documentation loads, but features don't work. API calls fail.

**Cause**: `Host` header is being forwarded or `Origin` header is missing.

**Solution**:

* Remove `Host` header forwarding
* Set `Origin` header to `<your-subdomain>.mintlify.app`

### Performance issues

**Symptoms**: Slow page loads and layout shifts.

**Cause**: Incorrect caching configuration.

**Solution**: Enable caching only for `/mintlify-assets/_next/static/*` paths.



# AWS Route 53 and CloudFront
Source: https://mintlify.com/docs/deploy/route53-cloudfront

Host documentation at a custom subpath using AWS services

To host your documentation at a custom subpath such as `yoursite.com/docs` using AWS Route 53 and CloudFront, you need to configure your DNS provider to point to your CloudFront distribution.


## Repository structure

Your documentation files must be organized within your repository to match your chosen subpath structure. For example, if you want your documentation at `yoursite.com/docs`, you would create a `docs/` directory with all of your documentation files.


## High-level overview

Route traffic to these paths with a Cache Policy of **CachingDisabled**:

* `/.well-known/acme-challenge/*` - Required for Let's Encrypt certificate verification
* `/.well-known/vercel/*` - Required for domain verification
* `/docs/*` - Required for subpath routing
* `/docs/` - Required for subpath routing

Route traffic to this path with a Cache Policy of **CachingEnabled**:

* `/mintlify-assets/_next/static/*`
* `Default (*)`	- Your websites landing page

All Behaviors must have the an **origin request policy** of `AllViewerExceptHostHeader`.

<img src="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=666a7c785bcc7f6b2aa23424f8c1c668" alt="CloudFront &#x22;Behaviors&#x22; page with 4 behaviors: /docs/*, /docs, Default, and /.well-known/*." data-og-width="1603" width="1603" data-og-height="365" height="365" data-path="images/cloudfront/all-behaviors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=280&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=71017f7f8adb9707c30a4af5f18466c1 280w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=560&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b3d0b64d01d3d9405b3237ffe99e8b9f 560w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=840&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=97dd0acfd49dfd2f345f2fd3018e9db0 840w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1100&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b5f9cdf34197e6b4d86e36980d6a000f 1100w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1650&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=c4a30fd51baf478014221afc66c7ac2a 1650w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=2500&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b10b0389187a79b2367074200a34dc17 2500w" />


## Create CloudFront distribution

1. Navigate to [CloudFront](https://aws.amazon.com/cloudfront) inside the AWS console.
2. Select **Create distribution**.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=cd402e36a077943e5de51319a2fba9c3" alt="CloudFront Distributions page with the &#x22;Create distribution&#x22; button emphasized." data-og-width="3024" width="3024" data-og-height="922" height="922" data-path="images/cloudfront/create-distribution.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a14e9b98b0a52b5506139de3990ed56c 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=fff44181d05af6479ebf8f71793a9df2 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7f1bd8301e645206bd75dd4a00b39bb7 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=652ccfcf0b02689df1303e036689f30a 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=77d0f33cd3538e0945e392e3a7347aa3 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-distribution.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b3857c3316d9018af53d363296f156c1 2500w" />
</Frame>

3. For the Origin domain, input `[SUBDOMAIN].mintlify.dev` where `[SUBDOMAIN]` is your project's unique subdomain.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3bccb966a96cba7ec83364dabf5ba788" alt="CloudFront &#x22;Create distribution&#x22; page showing &#x22;acme.mintlify.dev&#x22; as the origin domain." data-og-width="1495" width="1495" data-og-height="1036" height="1036" data-path="images/cloudfront/origin-name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5f80b263a9f29ec240019d96d9edaf6d 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7746f61d09fcd8d68c2b82eedeba4a83 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5c4db2ba59e618dcb16f7219fa1d5c67 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f2adcb53996e6ba67072e566563a4b0e 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e1c482ddd1688c0b7b35f08a05ad8801 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/origin-name.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3486245acffbe7d9eff91e179eb64dba 2500w" />
</Frame>

4. For "Web Application Firewall (WAF)," enable security protections.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=73a02de58bfbce884656443bb5d1ec42" alt="Web Application Firewall (WAF) options with &#x22;Enable security protections&#x22; selected." data-og-width="1482" width="1482" data-og-height="877" height="877" data-path="images/cloudfront/enable-security-protections.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8ad5bdde51829e1972c399de3d8806bf 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1d9535dfc44839225a3ac3b578a91f7a 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=13bccc1bd18c1e493697f946c42c99b0 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5b4d95a51ca31be7a27a651e149c11a8 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f859c34c5c459da088e65cf9d41fda5f 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/enable-security-protections.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=9b7a10b459e612101c36a21cc24b2c2e 2500w" />
</Frame>

5. The remaining settings should be default.
6. Select **Create distribution**.


## Add default origin

1. After creating the distribution, navigate to the "Origins" tab.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=bbf7cd128d5fa29b2d957e224757d90c" alt="A CloudFront distribution with the &#x22;Origins&#x22; tab highlighted." data-og-width="3024" width="3024" data-og-height="1466" height="1466" data-path="images/cloudfront/origins.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=aa7bae4c10cf41533acabddcfc54f568 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7d703fcc13c4526c48b3e82fce390324 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f0f0120635fd5452703f78e3db14f60c 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f26e5b8f578123e38f8b235252658b52 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b3949751be07019ea134de611921bf8e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/origins.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9d8272f1f9a9066b3166330b8a707a69 2500w" />
</Frame>

2. Find your staging URL that mirrors the main domain. This is highly variant depending on how your landing page is hosted. For example, the Mintlify staging URL is [mintlify-landing-page.vercel.app](https://mintlify-landing-page.vercel.app).

<Info>
  If your landing page is hosted on Webflow, use Webflow's staging URL. It would look like `.webflow.io`.

  If you use Vercel, use the `.vercel.app` domain available for every project.
</Info>

3. Create a new Origin and add your staging URL as the "Origin domain."

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c67257bc20e907ea4da1a8719fae0543" alt="CloudFront &#x22;Create origin&#x22; page with a &#x22;Origin domain&#x22; input field highlighted." data-og-width="3024" width="3024" data-og-height="1332" height="1332" data-path="images/cloudfront/default-origin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=be2c93bed56c831d4f0328f913365927 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=762bf1eca446eeec28749e6d031b42fc 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=36f2f39ecd5607134cb037f3366de8a9 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=5c0bf927f10b494efbe4860c3c0cc674 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8edb7f1a41443eda7cf820cabd9d9eb1 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-origin.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c91110942758408e864542c42a152d04 2500w" />
</Frame>

By this point, you should have two Origins: one with `[SUBDOMAIN].mintlify.app` and another with your staging URL.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=c1fdd6d6e346e0e7b3a669daba284fba" alt="CloudFront &#x22;Origins&#x22; page with two origins: One for mintlify and another for mintlify-landing-page." data-og-width="1230" width="1230" data-og-height="690" height="690" data-path="images/cloudfront/final-origins.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d6f49353d428a3918a50019415f3b332 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=dd47af40f1a0f2b3a293603a8996d94f 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=779c21e2440c9a67ab4f6c2868f21e11 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a4fb662350e37ebb0e890069d711ded7 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=bf9804c4703342bc0de775f27ff55494 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/final-origins.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3ade799350b7e7ee33ccec38a974ed38 2500w" />
</Frame>


## Set behaviors

Behaviors in CloudFront enable control over the subpath logic. At a high level, we're looking to create the following logic:

* **If a user lands on your custom subpath**, go to `[SUBDOMAIN].mintlify.dev`.
* **If a user lands on any other page**, go the current landing page.

1. Navigate to the "Behaviors" tab of your CloudFront distribution.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=6ab02a43a5427d2d1306dfd6d313bc49" alt="CloudFront &#x22;Behaviors&#x22; tab highlighted." data-og-width="3024" width="3024" data-og-height="1384" height="1384" data-path="images/cloudfront/behaviors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=f5cf4e6e79ea2cb17f57668d938b6d42 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=b1657d38c9cdfbf180c746cf0bbab348 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=605f1ee4a420dd549a5feb4fe186063b 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=ca4656368268c50468cc87261d17092e 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7ad8b32781d0e8cdb8c7d2fc7b7b6691 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/behaviors.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=19d0067d18ab1c69d03168c82be480ff 2500w" />
</Frame>

2. Select the **Create behavior** button and create the following behaviors.

### `/.well-known/*`

Create behaviors for Vercel domain verification paths with a **Path pattern** of `/.well-known/*` and set **Origin and origin groups** to your docs URL.

For "Cache policy," select **CachingDisabled** to ensure these verification requests pass through without caching.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=374fd2e53349cc9796515cda82a9b165" alt="CloudFront &#x22;Create behavior&#x22; page with a &#x22;Path pattern&#x22; of &#x22;/.well-known/*&#x22; and &#x22;Origin and origin groups&#x22; pointing to the staging URL." data-og-width="1413" width="1413" data-og-height="1098" height="1098" data-path="images/cloudfront/well-known-policy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=8ecced93fe28b40cbf6be37c834c6a8c 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a500a1b484f3251724a470987e156f43 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=be86e4de31b968087c11e4c780ab1e5d 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0889bd6abd0faa4f6eb972c62839e45c 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3659464f1ce1e75c49c2add0cc7c91ef 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/well-known-policy.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ffc102f5136367e16b0cb21322be97b7 2500w" />
</Frame>

<Info>
  If `.well-known/*` is too generic, it can be narrowed down to 2 behaviors at a minimum for Vercel:

  * `/.well-known/vercel/*` - Required for Vercel domain verification
  * `/.well-known/acme-challenge/*` - Required for Let's Encrypt certificate verification
</Info>

### Your custom subpath

Create a behavior with a **Path pattern** of your chosen subpath, for example `/docs`, with **Origin and origin groups** pointing to the `.mintlify.dev` URL (in our case `acme.mintlify.dev`).

* Set "Cache policy" to **CachingOptimized**.
* Set "Origin request policy" to **AllViewerExceptHostHeader**.
* Set Viewer Protocol Policy to **Redirect HTTP to HTTPS**

<Frame>
    <img src="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=0ce9e6db0d16c0c095abf1bc44e68833" alt="CloudFront &#x22;Create behavior&#x22; page with a &#x22;Path pattern&#x22; of &#x22;/docs/*&#x22; and &#x22;Origin and origin groups&#x22; pointing to the acme.mintlify.dev URL." data-og-width="1520" width="1520" data-og-height="1117" height="1117" data-path="images/cloudfront/behavior-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=280&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=7ab1bb41895bb54e7e6aa14f6f83ac50 280w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=560&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=bb5384522a0a391acc94fd837abd4351 560w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=840&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=d56f68b911e11ce2a022e5740f80a7fe 840w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=1100&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=51107e34efbe3a0724823989b7c19221 1100w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=1650&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=17211bee07269e1ca4e013a7e8414b8c 1650w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/behavior-1.png?w=2500&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=275446c0ebfc6ad984632f2071291185 2500w" />
</Frame>

### Your custom subpath with wildcard

Create a behavior with a **Path pattern** of your chosen subpath followed by `/*`, for example `/docs/*`, and **Origin and origin groups** pointing to the same `.mintlify.dev` URL.

These settings should exactly match your base subpath behavior. With the exception of the **Path pattern**.

* Set "Cache policy" to **CachingOptimized**.
* Set "Origin request policy" to **AllViewerExceptHostHeader**.
* Set "Viewer protocol policy" to **Redirect HTTP to HTTPS**

### `/mintlify-assets/_next/static/*`

* Set "Cache policy" to **CachingOptimized**
* Set "Origin request policy" to **AllViewerExceptHostHeader**
* Set "Viewer protocol policy" to **Redirect HTTP to HTTPS**

### `Default (*)`

Lastly, we're going to edit the `Default (*)` behavior.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d1404011b4a312d88c7e523bbcf94316" alt="A CloudFront distribution with the &#x22;Default (*)&#x22; behavior selected and the Edit button emphasized." data-og-width="3024" width="3024" data-og-height="1406" height="1406" data-path="images/cloudfront/default-behavior-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=a667557538a05b428b88de0860055fdc 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0ef97f41ff4722b83ada48dcfe4a6fb3 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=477ee3b3ff613ff0db18da30685a66e7 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=0293e235eeaa0b07d06d5aa1b237154d 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e049af02765251c8dc70f75871ce8646 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-1.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=420d002f4dd0a5d33b6f3939ccba08f8 2500w" />
</Frame>

1. Change the default behavior's **Origin and origin groups** to the staging URL (in our case `mintlify-landing-page.vercel.app`).

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=3c81d60889bc1157954524865a0bde14" alt="CloudFront &#x22;Edit behavior&#x22; page with the &#x22;Origin and origin groups&#x22; input field highlighted." data-og-width="3024" width="3024" data-og-height="1298" height="1298" data-path="images/cloudfront/default-behavior-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=978b2b690638bffc0b4d8a042c38496b 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=163f9ce0d805d64936d0ad3d0f1e95b8 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=79132725b4b9360f74098fb37d8aa39f 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=8254ab4be3bb28a5a8eb6ac56cac4c04 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=2b75a3d1bd5e7f728e6fc98dec394abd 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/default-behavior-2.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=21d56c18cbd73f2e0939ac52805c9517 2500w" />
</Frame>

2. Select **Save changes**.

### Check behaviors are set up correctly

If you follow the above steps, your behaviors should look like this:

<Frame>
    <img src="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=666a7c785bcc7f6b2aa23424f8c1c668" alt="CloudFront &#x22;Behaviors&#x22; page with 4 behaviors: /docs/*, /docs, Default, and /.well-known/*." data-og-width="1603" width="1603" data-og-height="365" height="365" data-path="images/cloudfront/all-behaviors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=280&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=71017f7f8adb9707c30a4af5f18466c1 280w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=560&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b3d0b64d01d3d9405b3237ffe99e8b9f 560w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=840&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=97dd0acfd49dfd2f345f2fd3018e9db0 840w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1100&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b5f9cdf34197e6b4d86e36980d6a000f 1100w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=1650&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=c4a30fd51baf478014221afc66c7ac2a 1650w, https://mintcdn.com/mintlify/in3v2q9tGvWcAFWD/images/cloudfront/all-behaviors.png?w=2500&fit=max&auto=format&n=in3v2q9tGvWcAFWD&q=85&s=b10b0389187a79b2367074200a34dc17 2500w" />
</Frame>


## Preview distribution

You can now test if your distribution is set up properly by going to the "General" tab and visiting the **Distribution domain name** URL.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b7f0582640bb6650054c7b40ee9bdd57" alt="CloudFront &#x22;General&#x22; tab with the &#x22;Distribution domain name&#x22; URL highlighted." data-og-width="3024" width="3024" data-og-height="1394" height="1394" data-path="images/cloudfront/preview-distribution.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=88578895d491f6405b39aa52d91123ec 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0c07a7178b43c2d4d2011fafc34bef59 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7ba052eb7683b44ebf829a0806ba0aa0 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9fe004b5b8c70190e09a51478b05b9f6 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c0e9bf74112262191fd0c053f3a42a74 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/preview-distribution.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cf41b0e9aeedefab2e2f8dba02f43460 2500w" />
</Frame>

All pages should be directing to your main landing page, but if you append your chosen subpath, for example `/docs`, to the URL, you should see it going to your Mintlify documentation instance.


## Connect with Route53

Now, we're going to bring the functionality of the CloudFront distribution into your primary domain.

<Note>
  For this section, you can also refer to AWS's official guide on [Configuring
  Amazon Route 53 to route traffic to a CloudFront
  distribution](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html#routing-to-cloudfront-distribution-config)
</Note>

1. Navigate to [Route53](https://aws.amazon.com/route53) inside the AWS console.
2. Navigate to the "Hosted zone" for your primary domain.
3. Select **Create record**.

<Frame>
    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=27a00457e2401c2d55262291dda15579" alt="Route 53 &#x22;Records&#x22; page with the &#x22;Create record&#x22; button emphasized." data-og-width="1540" width="1540" data-og-height="1238" height="1238" data-path="images/cloudfront/route53-create-record.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a89b265f8944bd325f6422ae0532aa7b 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=71b98a1b9face10930f59047e6b06da8 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c05ef2f2a52142c2a5c5588ae458302c 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a3ff847c7cd962bff070660ac65e6cab 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7257b0f07303f69ad65e2af26ae20937 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/cloudfront/route53-create-record.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=44902e21c0e9ed907d1ef95a81f98a8c 2500w" />
</Frame>

4. Toggle `Alias` and then **Route traffic to** the `Alias to CloudFront distribution` option.

<Frame>
    <img src="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=cb7dbe0320f3f73233ed6452ac3b0372" alt="Route 53 &#x22;Create record&#x22; page with the &#x22;Alias&#x22; toggle and the &#x22;Route traffic to&#x22; menu highlighted." data-og-width="3024" width="3024" data-og-height="1494" height="1494" data-path="images/cloudfront/create-record-alias.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=280&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=7e6a7c98c6385b708c13a4ba97e7be28 280w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=560&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=d3585515b33059d1c2796651fd4e3747 560w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=840&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=e8d6264e546b432c60ee555c4d188cb3 840w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=1100&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=4fc4e520251cf12caff27666ea2ccdc5 1100w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=1650&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=233ca4593b197c489cada291613333a3 1650w, https://mintcdn.com/mintlify/WXXCCJWDplNJgTwZ/images/cloudfront/create-record-alias.png?w=2500&fit=max&auto=format&n=WXXCCJWDplNJgTwZ&q=85&s=1561e423e0702a1cac1d3c4fbdd4dca9 2500w" />
</Frame>

5. Select **Create records**.

<Note>
  You may need to remove the existing A record if one currently exists.
</Note>

Your documentation is now live at your chosen subpath for your primary domain.

<Note>
  After configuring your DNS, custom subdomains are usually available within a few minutes. DNS propagation can sometimes take 1-4 hours, and in rare cases up to 48 hours. If your subdomain is not immediately available, please wait before troubleshooting.
</Note>



---
**Navigation:** [← Previous](./04-fonts.md) | [Index](./index.md) | [Next →](./06-vercel.md)
