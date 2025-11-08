**Navigation:** [← Previous](./04-content-variants.md) | [Index](./index.md) | [Next →](./06-authenticated-access.md)

# Authenticated access

Set up custom authentication for your published content

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

Authenticated access allows you to publish your content while requiring authentication from any visitors who want to view it. When enabled, GitBook lets your authentication provider handle who has access to the content.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FlwfYBtUnP8SnBPbsOZEi%2Fvisitor-authentication.svg?alt=media&#x26;token=23e3c844-fffa-48b6-969e-63afd309d69a" alt="A screenshot showing a login screen for docs behind authenticated access"><figcaption><p>Add a sign in to your published documentation.</p></figcaption></figure>

### Use cases

Common use cases for authenticated access include:

* Publishing sensitive product documentation that should only be accessible to paying customers, sales prospects or partners.
* Publishing internal knowledge base content that should only be accessible to employees of your company.

### How it works

There are two methods you can choose from when setting up authenticated access:

1. Installing one of our authentication integrations — we currently support Okta, Azure, and Auth0. We **highly recommend** this option if you’re using an authentication provider we support.
2. Create and host your own server to handle the authentication. Many different technologies can be used, but it’s up to you to code and maintain the solution you choose.

Head to [Enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access) to start setting up protected access for your site.



# Enabling authenticated access

To protect your docs behind a sign-in screen, you’ll need to first enable authenticated access for your site.

### Enable authenticated access

Head to your [site’s settings](https://gitbook.com/docs/documentation/publishing-documentation/site-settings), and choose **Authenticated access** from your site’s audience settings. Once selected, you’ll see a few options you’ll need to continue configuring your site. You’ll also see a generated "**Private key**", which you’ll need at a later point in the authenticated access setup.

### Choose an authentication method

Depending on your setup, we have integrations and guides on setting up authenticated access for different tools.

Head to the relevant guide to continue setting up authenticated access for your site.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Setting up Auth0</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FRC8ah9trT3HsKVau1mnH%2Fcard_auth0.svg?alt=media&#x26;token=66d83098-b07c-4ee1-b41d-f9766dfdf703">card_auth0.svg</a></td><td><a href="setting-up-auth0">setting-up-auth0</a></td></tr><tr><td>Setting up Azure AD</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FKrbZXlJ3dMpfRu87FMGS%2Fcard_azure_ad.svg?alt=media&#x26;token=9ab99f1f-bd44-4a01-829b-3572d4559dff">card_azure_ad.svg</a></td><td><a href="setting-up-azure-ad">setting-up-azure-ad</a></td></tr><tr><td>Setting up Okta</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fb1BCMkshEsKD26yyp0Wt%2Fcard_okta.svg?alt=media&#x26;token=81133f4d-0a34-40e3-958e-616a268a12c1">card_okta.svg</a></td><td><a href="setting-up-okta">setting-up-okta</a></td></tr><tr><td>Setting up AWS Cognito</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FiWvq26r9Mxig2qbWMJJ4%2Fcard_aws_cognito.svg?alt=media&#x26;token=f275b67c-fbcc-46e2-8eb6-b46f9629ef0e">card_aws_cognito.svg</a></td><td><a href="setting-up-aws-cognito">setting-up-aws-cognito</a></td></tr><tr><td>Setting up OIDC</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F4OZgzd8PCJQQ98Aq1aYz%2Fcard_oidc.svg?alt=media&#x26;token=17363f03-2dc6-4ea4-853b-03a636686496">card_oidc.svg</a></td><td><a href="setting-up-oidc">setting-up-oidc</a></td></tr><tr><td>Setting up a custom backend</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FkiyIjK7tW99zVp1y1ksI%2Fcard_custom_backend.svg?alt=media&#x26;token=03687058-22d1-462e-8d4a-c42f6b51a1df">card_custom_backend.svg</a></td><td><a href="setting-up-a-custom-backend">setting-up-a-custom-backend</a></td></tr></tbody></table>



# Setting up Auth0

Set up an Auth0 login screen for visitors to your docs.

{% hint style="info" %}
Head to our guides to find a [full walk-through](https://gitbook.com/docs/guides/product-guides/how-to-personalize-your-gitbook-site-using-auth0-and-adaptive-content) on setting up authenticated access and adaptive content with Auth0.
{% endhint %}

{% hint style="warning" %}
This guide takes your through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through [Enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

To setup your GitBook site with authenticated access using Auth0, the process looks as follows:

{% stepper %}
{% step %}

#### [Create a new application in Auth0](#id-1.-create-a-new-application-in-auth0)

Create an Auth0 application in your Auth0 dashboard.
{% endstep %}

{% step %}

#### [Install and configure the Auth0 integration](#id-2.-install-and-configure-the-auth0-integration)

Install the Auth0 integration and add the required configuration to your GitBook site.
{% endstep %}

{% step %}

#### [Configure Auth0 for Adaptive content (optional)](#id-3.-configure-auth0-for-adaptive-content-optional)

Configure Auth0 to work with adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### 1. Create a new application in Auth0

Start by creating a new application in your Auth0 platform dashboard. This application will allow the GitBook Auth0 integration to request tokens to validate user identity before granting them access to your site.

1. Sign in to your Auth0 [dashboard](https://manage.auth0.com/dashboard/).
2. Head to **Applications > Applications** section from the left sidebar.
3. Click on the **+ Create Application** button, and give your app a name.
4. Under the **Choose an application type,** select **Regular Web Applications**.
5. In the **Quickstart** screen of the newly created app, select **Node.js (Express)** and then **I want to integrated my app**.
6. You should then see a configuration screen like below.\
   Click **Save Settings And Continue**.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHoIpHTIRmkCvhw1kBVZZ%2Fauth0_app_configure_screen.png?alt=media&#x26;token=ef189183-2547-4e5e-b22f-2d3169f2b600" alt=""><figcaption></figcaption></figure>
7. Click on the **Settings** tab.
8. Copy and make note of the **Domain**, **Client ID** and **Client Secret**.

{% hint style="warning" %}
Please ensure that you have **at least one connection enabled** for your Auth0 application under the **Connections** tab.
{% endhint %}

### 2. Install and configure the Auth0 integration

Once you've created the Auth0 application, the next step is to install the Auth0 integration in GitBook and link it with your Auth0 application using the credentials you generated earlier:

1. Navigate to the site where you've enabled authenticated access and want to use Auth0 as the identity provider.
2. Click on the **Integrations** button in the top right from your site’s settings.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FgBMsbydNsuqx7eqcz0JN%2Fva_site_integration_overview_screen.png?alt=media&#x26;token=ead70cf3-93cf-4aef-b77a-321afad38900" alt=""><figcaption></figcaption></figure>
3. Click on **Authenticated Access** from the categories in the sidebar.
4. Select the **Auth0** integration.
5. Click **Install on this site**.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F98d9Svq3PBdpaiRuyV14%2Fauth0_install_integration.png?alt=media&#x26;token=155beba6-bc85-42c6-acb8-18f782f207a4" alt=""><figcaption></figcaption></figure>
6. After installing the integration on your site, you should see the integration's configuration screen:\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FGpdmoJqOQvrwFBaQ17Gv%2Fauth0_configure_integration.png?alt=media&#x26;token=61bc203c-2553-453f-b701-176264af044b" alt=""><figcaption></figcaption></figure>
7. Enter the **Domain**, **Client ID** and **Client Secret** values you copied after creating the Auth0 application earlier. For Auth0 Domain, enter the Domain copied from Auth0 (make sure to prefix it with `https://`).
8. **(optional)** Enable the **Include claims in JWT token** option at the bottom of the dialog if you have enabled your site for [adaptive content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content).
9. Copy and make note of the **Callback** **URL** displayed **at the bottom of the dialog**.
10. Click **Save**.
11. Head back to the Auth0 application you created earlier in the Auth0 dashboard.
12. Browse to **Applications > Applications** in the sidebar and select the **Settings** tab.
13. Scroll down to the **Application URIs** section of the settings
14. Paste the **Callback URL** you copied earlier from the GitBook integration dialog into the **Allowed Callback URL** input field.
15. Click **Save.**
16. Head back to **Auth0 integration** installation screen **in GitBook**.
17. Close the integration dialogs and click on the **Settings** tab in the site screen.
18. Browse to **Audience** and select **Authenticated access** (if not already selected).
19. Select **Auth0** from the dropdown in the **Authentication backend** section.
20. Click **Update audience**.
21. Head to the site's overview screen and click **Publish** if the site is not already published.

Your site is now published behind authenticated access using your Auth0 as identity provider.

To test it out, click on **Visit**. You will be asked to sign in with Auth0, which confirms that your site is published behind authenticated access using Auth0.

### 3. Configure Auth0 for Adaptive content (optional)

{% embed url="<https://www.youtube.com/embed/uhWeQkgyg8Y?si=7_kD3RF-Is_MnYhZ>" %}

To leverage the Adaptive Content capability in your authenticated access site, [configure the Auth0 application](https://auth0.com/docs/secure/tokens/json-web-tokens/create-custom-claims) to include additional user information in the authentication token as claims.

These claims, represented as key-value pairs, are passed to GitBook and can be used to [adapt content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content) dynamically for your site visitors.



# Setting up Azure AD

Set up an Azure AD login screen for visitors to your docs.

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

{% hint style="info" %}
There is a known limitation with the Azure integration where heading URL fragments will be removed upon authentication. The user will still land on the correct page, but will be taken to the top of the page instead of the heading in the URL. Once a user is authenticated this behavior will no longer occur during a session and the user would be directed to the correct heading.

This is due to a security measure put in place by Microsoft.
{% endhint %}

### Overview

To setup your GitBook site with authenticated access using Azure AD, the process looks as follows:

{% stepper %}
{% step %}

#### [Create an app registration in Azure AD](#id-1.-create-an-app-registration-in-azure-a-d)

Create an Azure AD application registration in your Microsoft Entra ID admin dashboard.
{% endstep %}

{% step %}

#### [Install and configure the Azure AD integration on your site](#id-2.-install-and-configure-the-azure-a-d-integration)

Install the Azure AD integration and add the required configuration to your GitBook site.
{% endstep %}

{% step %}

#### [Configure Azure AD for adaptive content (optional)](#id-3.-configure-azure-a-d-for-adaptive-content-optional)

Configure your Azure AD to work with Adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### 1. Create an app registration in Azure AD

Start by creating an app registration in your Microsoft Entra ID dashboard. This application registration will allow the GitBook Azure AD integration to request tokens to validate user identity before granting them access to your site.

1. Sign in to your Microsoft Entra ID admin [dashboard](https://entra.microsoft.com/).
2. Head to **Identity** > **Applications** > **App registrations** from the left sidebar.
3. Click on **+ New registration,** and give your registration a name.
4. Under **Supported account types,** select “**Accounts in this organizational directory only (Default Directory only - Single tenant)”**.
5. Leave the Redirect URI field empty for now—you will need to fill this in later.
6. Click **Register** to complete the app registration.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FuB6p6HxRmveHp1cfsiKa%2Fazure_ad_integration_register_app.png?alt=media&#x26;token=cbc82bc5-189e-433a-b990-042066768307" alt="An Azure screenshot showing how to register an Azure AD app"><figcaption><p>Register an app for the GitBook VA integration.</p></figcaption></figure>
7. You should then see your new app registration **Overview** screen. Copy and make note of the **Application (client) ID** and **Directory (tenant) ID**.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FETQziXVuqGnho8GGOVBZ%2Fazure_ad_integration_app_reg_overview.png?alt=media&#x26;token=266a55e3-db75-4a4a-923c-8302f69653d5" alt="An Azure screenshot showing the app registration overview"><figcaption><p>Overview of the newly created app registration.</p></figcaption></figure>
8. Click on **Add a certificate or secret**. You should see the following **Certificates & Secrets** screen:\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FnXJbnpnGhOI6Udjrx8bS%2Fazure_ad_integration_client_secrets.png?alt=media&#x26;token=9202689b-4657-4bea-bf74-42b51e1051e5" alt="An Azure screenshot showing where to add a certificate or secret"><figcaption><p>Add a certificate or secret.</p></figcaption></figure>
9. Click on **+ New client secret**.
10. Enter suitable description for the secret and click **Add**.
11. Copy and make note of the **Value** field (***not** the Secret ID*) of the secret you just created.

### 2. Install and configure the Azure AD integration

Once you've created the Azure AD app registration, the next step is to install the Azure AD integration in GitBook and link it with your Azure application using the credentials you generated earlier:

1. Navigate to the site where you’ve [enabled authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/enabling-authenticated-access#enable-authenticated-access) and want to use Azure AD as the identity provider.
2. Click on the **Integrations** button in the top right from your site’s settings.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FgBMsbydNsuqx7eqcz0JN%2Fva_site_integration_overview_screen.png?alt=media&#x26;token=ead70cf3-93cf-4aef-b77a-321afad38900" alt="A GitBook screenshot showing the site settings overview"><figcaption></figcaption></figure>
3. Click on **Authenticated Access** from the categories in the sidebar.
4. Select the **Azure** integration.
5. Click **Install on this site**.\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FCiveWUn0FWMEdS3YRU62%2FScreenshot%202025-03-24%20at%2018.10.09.png?alt=media&#x26;token=fcaedce7-40f5-40e5-acd1-040e90822be4" alt="A GitBook screenshot showing installation of the Azure AD integration"><figcaption></figcaption></figure>
6. After installing the integration on your site, you should see the integration's configuration screen:\\

   <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FvO9pXBCZkcprDDIVFkcf%2FScreenshot%202025-03-24%20at%2018.17.02.png?alt=media&#x26;token=e082d3dd-1e6b-44b4-beaf-a5d67812e055" alt="A GitBook screenshot showing the Azure AD configuration dialog"><figcaption></figcaption></figure>
7. Enter the **Client ID**, **Tenant ID**, and **Client Secret** values you copied after [creating the Azure AD app registration](#id-1.-create-an-app-registration-in-azure-a-d) earlier, and click “Save”.
8. Copy the **URL** displayed **at the bottom of the dialog**.
9. Head back to the Azure AD app registration you created earlier in the Microsoft Entra ID dashboard.
10. Browse to **Manage** > **Authentication** in the sidebar.
11. Click **+ Add a platform** and select **Web** card in the panel that opens.\\

    <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FUssw9BNY66urLYH376sE%2FScreenshot%202025-03-24%20at%2018.28.58.png?alt=media&#x26;token=2c2b2b84-b7e9-4fc3-a7bd-2751dacfd579" alt="An Azure screenshot showing authentication platform settings"><figcaption></figcaption></figure>
12. Paste the GitBook integration **URL** you copied earlier in the **Redirect URI** field, and click “Configure”\\

    <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fi9fVjsa351I6kVzJw64X%2Fimage.png?alt=media&#x26;token=85d1d25a-bdb8-4453-b30e-54a21304f870" alt="An Azure screenshot showing where to enter the redirect URI"><figcaption></figcaption></figure>
13. Head back to **Azure integration** installation screen **in GitBook**.
14. Close the integration dialogs and click on the **Settings** tab in the site screen.
15. Browse to **Audience** and select **Authenticated access** (if not already selected).
16. Select **Azure** from the dropdown in the **Authentication backend** section.
17. Click **Update audience**.\\

    <figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Finc5DrItbyXUIXP4K4ic%2FScreenshot%202025-03-24%20at%2018.41.45.png?alt=media&#x26;token=e06283f6-f7d6-4556-9ef7-747b47493064" alt="A GitBook screenshot showing authenticated access settings"><figcaption></figcaption></figure>
18. Head to the site's overview screen and click **Publish** if the site is not already published.

Your site is now published behind authenticated access using your Azure AD as identity provider.

To test it out, click on Visit. You will be asked to sign in with Azure, which confirms that your site is published behind authenticated access using Azure.

{% hint style="info" %}
Upon accessing the published content URL and after logging in with your Azure credentials, you may see a screen telling you that you need to "Request approval" from your admin. Your admin can grant this request by accessing the published content URL, logging in, and granting approval on behalf of the organization.
{% endhint %}

### 3. Configure Azure AD for Adaptive content (optional)

To leverage the Adaptive Content capability in your authenticated access site, configure the Azure AD app registration to include additional user information in the authentication token as claims.

These claims, represented as key-value pairs, are passed to GitBook and can be used to [adapt content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content) dynamically for your site visitors.

Azure AD supports different types and levels of claims, each with its own method of setup:

* **Standard Claims**: Common claims that may be included in tokens but are not always present by default.

{% hint style="info" %}
Azure AD keeps token sizes optimized for performance. As a result, many claims are **not** included in the token by default and must be explicitly requested by the application. To ensure claims like `email` , `groups` or `roles` are included, they must be explicitly requested as **optional claims**.
{% endhint %}

* **Optional Claims**: Additional predefined claims that can be enabled for an application.
* **Custom Claims**: Claims sourced from custom user attributes in Azure AD or external systems via a custom claims provider.

For more details on how to include these different types of claims in the tokens generated by your Azure AD app, refer to the following Microsoft Entra documentation guides:

* [User Attributes](https://learn.microsoft.com/en-us/entra/external-id/customers/how-to-add-attributes-to-token)
* [Optional Claims](https://learn.microsoft.com/en-us/entra/identity-platform/optional-claims?toc=%2Fentra%2Fexternal-id%2Ftoc.json\&bc=%2Fentra%2Fexternal-id%2Fbreadcrumb%2Ftoc.json\&tabs=appui)
* [Custom Claims](https://learn.microsoft.com/en-us/entra/identity-platform/custom-claims-provider-overview)

After setting up and configuring the right claims to send to GitBook, head to “[Adapting your content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content)” to continue configuring your site.



# Setting up AWS Cognito

Set up an AWS Cognito login screen for visitors to your docs.

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

To setup your GitBook site with authenticated access using AWS Cognito, the process looks as follows:

{% stepper %}
{% step %}

#### Create a new AWS Cognito application

Create an AWS Cognito application from your AWS dashboard.
{% endstep %}

{% step %}

#### Install and configure the AWS Cognito integration

Install the AWS Cognito integration and add the required configuration.
{% endstep %}

{% step %}

#### Configure AWS Cognito for adaptive content (optional)

Configure AWS Cognito to work with adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### Create a new AWS Cognito application

Go to your desired User Pool in Cognito, and click on App integration. Make a note of the Cognito domain, we will need it to configure the integration.

Scroll to the bottom and click "Create app client". For the app type, select "Confidential client." Scroll down to Hosted UI settings. In allowed Callback URLs, enter the Callback URL you got from GitBook upon installing the integration on a space.

Scroll further down to "OAuth 2.0 grant types"- make sure "Authorization code grant" is selected.

For "OpenID connect scopes", make sure OpenID is selected.

Scroll down and click "Create app client".

Click on the created app client and make a note of the Client ID and Client Secret.

### Install and configure the AWS Cognito integration

Navigate to integrations within the GitBook app, select authenticated access as the category, and install the AWS Cognito integration.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FCZy21M4LIPwMVSxI3ec1%2FScreen%20Shot%202024-12-13%20at%203.37.39%20PM.png?alt=media&#x26;token=4e31d496-04eb-4d00-ac45-011b543edfe4" alt="A GitBook screenshot showing the AWS Cognito integration install screen"><figcaption></figcaption></figure>

Once you've installed it on your site, go to configuration and make a note of the Callback URL right above the Save button. We will need it to set up Cognito.

Open up the Cognito integration's configuration screen for the space you installed the integration on.

It should look like the following image:

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fgy177CzFZiy6U4IntLUE%2FScreen%20Shot%202024-12-13%20at%203.41.57%20PM.png?alt=media&#x26;token=3823d5cb-56e0-4e02-abd6-6d6d66cacf71" alt="A GitBook screenshot showing the AWS Cognito configuration screen"><figcaption></figcaption></figure>

For Client ID, Cognito Domain, and Client Secret, paste in the values you got from Cognito.

Hit Save.

Now, in GitBook, close the integrations modal and click on the Manage site button. Navigate to **Audience**, select **Authenticated access**, and choose Cognito as the backend. Then, click **Update audience**. Go to the site’s screen and click **Publish**.\
\
The site is now published behind authenticated access controlled by your Auth0 application. To try it out, click on Visit. You will be asked to sign in with Cognito, which confirms that your site is published behind authenticated access using Auth0.

### Configure AWS Cognito for adaptive content (optional)

To leverage Adaptive Content with authenticated access in GitBook, you’ll need to configure your Amazon Cognito user pool to include custom claims in the ID token.

This is typically done by creating a [Cognito Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html)—specifically a *Pre Token Generation* Lambda—that returns a JSON payload overriding or appending custom claims. These claims might include user roles, subscription tiers, or any other metadata relevant to your content.

Here’s an example of what that could look like:

```javascript
export const handler = async (event, context) => {
  // Retrieve user attribute from event request
  const userAttributes = event.request.userAttributes;

  // Add additional claims to event response
  event.response = {
    "claimsAndScopeOverrideDetails": {
      "idTokenGeneration": {},
      "accessTokenGeneration": {
        "claimsToAddOrOverride": {
          "products": ['api', 'sites', 'askAI'],
          "isBetaUser": true,
          "isAlphaUser": true,
        }
      }
    }
  };
  // Return to Amazon Cognito
  context.done(null, event);
};
```

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwwKLiRUOJ27tjJCPc1Vd%2FScreenshot%202025-06-30%20at%2017.31.23.png?alt=media&#x26;token=f015ad33-1e96-47d4-82a5-e3b259f55a0e" alt=""><figcaption></figcaption></figure>

Once added, these key-value pairs are included in the authentication token and passed to GitBook, allowing your site to dynamically adapt its content based on the authenticated user’s profile.



# Setting up Okta

Set up an Okta login screen for visitors to your docs.

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

To setup your GitBook site with authenticated access using Okta, the process looks as follows:

{% stepper %}
{% step %}

#### Create a new Okta application

Create an Okta application from your Okta dashboard.
{% endstep %}

{% step %}

#### Install and configure the Okta integration

Install the Okta integration and add the required configuration.
{% endstep %}

{% step %}

#### Configure Okta for adaptive content (optional)

Configure Okta to work with adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### Create a new Okta application

First, sign in to Okta platform (the admin version) and create a new app integration (or use an existing one) by clicking the Applications button in the left sidebar.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8roQ3QDR5zsyFh2FoQS4%2FScreen%20Shot%202023-10-30%20at%201.32.55%20PM.png?alt=media&#x26;token=dc46f9f6-ec54-456f-ba7b-397477089e1a" alt="An Okta screenshot showing the create app integration screen"><figcaption></figcaption></figure>

Click Create App Integration and select OIDC - OpenID Connect as the Sign-In method. And then select Web Application as the application type.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FqgFHYo6HOUGF8dUTFEJM%2FScreen%20Shot%202023-10-30%20at%201.39.15%20PM.png?alt=media&#x26;token=0ac8e337-6082-4a28-b3df-33fa4e33dc0d" alt="An Okta screenshot showing the integration setup"><figcaption></figcaption></figure>

Name it appropriately and don't edit any other setting on that page. For assignments, choose the appropriate checkbox. Click Save.

On the next screen, copy Client ID and Client Secret. Copy the Okta Domain right below your email address by clicking the dropdown in the top right.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FJQWvrITuUlno737DbQKM%2FScreen%20Shot%202023-10-30%20at%204.52.14%20PM.png?alt=media&#x26;token=82a63cfd-a1e6-4666-b132-30fc98e95c22" alt="An Okta screenshot showing where to copy client credentials"><figcaption></figcaption></figure>

We will need these values to configure the Okta Integration.

### Install and configure the Okta integration

Navigate to the Integrations tab in the site you want to publish and locate the Okta integration or navigate directly to this [https://app.gitbook.com/integrations/VA-Okta](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/broken-reference).

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FeFArORtsvAcvgwbDZNce%2FScreen%20Shot%202024-12-13%20at%203.21.30%20PM.png?alt=media&#x26;token=199acbf6-3100-49af-886e-d2d09445f978" alt="A GitBook screenshot showing the site settings page"><figcaption></figcaption></figure>

Install the integration on your site.

Upon installation on site, you will see a screen asking you enter the Client ID, Okta Domain, and Client Secret.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FHrwQ0ASv1tD6kTZPVLMY%2FScreen%20Shot%202024-12-13%20at%203.34.37%20PM.png?alt=media&#x26;token=0844c1db-14b8-415c-8d51-33d4618e900e" alt="A GitBook screenshot showing the Okta credentials modal"><figcaption></figcaption></figure>

For Client ID, Okta Domain (remove `https://`prefix, if any) and Client Secret, paste in the value you copied from Okta Dashboard.

Click Save.

Copy the URL displayed in the modal and enter it as a Sign-In redirect URI in Okta (as shown in the below screenshot). Hit Save.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FpPZlqJlE6koyHrWhSp8i%2FScreen%20Shot%202024-01-14%20at%207.55.08%20PM.png?alt=media&#x26;token=99abc690-c82b-4974-9b5a-7ba6fbd11ed2" alt="An Okta screenshot showing the sign-in redirect URI configuration"><figcaption></figcaption></figure>

Now, in GitBook, close the integrations modal and click on the Manage site button. Navigate to **Audience**, select **Authenticated access**, and choose Okta as the backend. Then, click **Update audience**. Go to the site’s screen and click **Publish**.\
\
The site is now published behind authenticated access controlled by your Auth0 application. To try it out, click on Visit. You will be asked to sign in with Okta, which confirms that your site is published behind authenticated access using Auth0.

### Configure Okta for adaptive content (optional)

To enable Adaptive Content in your GitBook site with authenticated access, you’ll need to configure your Okta application to include relevant user data as claims in the authentication token.

Claims are key-value pairs embedded in the token sent to GitBook. These claims can be used to dynamically tailor documentation based on the user’s role, plan, location, or any other identifying attribute.

Okta supports multiple types of claims:

* **Standard Claims**\
  These are common claims (like `email`, `name`, or `groups`) that may be included by default but often need to be explicitly added to your token configuration for consistent availability.
* **Custom Claims**\
  You can define custom claims in Okta using [custom user attributes](https://help.okta.com/oie/en-us/Content/Topics/Directory/custom-user-profile-attributes.htm) or expression-based logic. These allow you to pass highly specific values—like plan tier, account ID, or internal team flags.
* **Groups as Claims**\
  You can also pass Okta groups as claims, which is especially useful when defining audience segments like “enterprise users” or “beta testers.” These can be filtered and mapped in your authorization server’s claim configuration.

To add or customize claims in Okta:

1. Open your Okta Admin Console.
2. Navigate to **Security > API > Authorization Servers**.
3. Edit the authorization server used for your GitBook site.
4. Under the **Claims** tab, add rules to include the desired claims in the token.
5. Make sure your GitBook site is reading and mapping those claims correctly.

Once claims are being passed into GitBook, follow the steps in [Adapting your content](https://www.gitbook.com/docs/adaptive-content/configure-your-site) to define what content should be shown to whom.



# Setting up OIDC

Set up an OIDC login screen for visitors to your docs.

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

To setup your GitBook site with authenticated access using OIDC, the process looks as follows:

{% stepper %}
{% step %}

#### Create a new application with your identity provider

Create an application from your identity provider’s dashboard.
{% endstep %}

{% step %}

#### Install and configure the OIDC integration

Install the Auth0 integration and add the required configuration.
{% endstep %}
{% endstepper %}

OIDC stands for OpenID Connect, and it's an identity layer built on top of OAuth. Many identity providers abide by OIDC, and GitBook's OIDC integration for authenticated access allows you to publish your space behind authenticated access, and access to the content is controlled by your Identity Provider

{% hint style="info" %}
Since this guide is a generic guide meant for all identity providers, some details may vary depending on your Identity Provider. For illustration purposes, we are using Google as the identity provider in this guide.
{% endhint %}

### Create a new application with your identity provider

There are some things that you need to set up on your Identity Provider in order to get the integration to work.

You need to create a new app inside your Identity Provider. Its type should be "Web Application." In Google, you create these under "API and Services", "Credentials", and then under "OAuth 2.0 Client IDs."\\

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8ra7t88ktqM7yX7w1l4m%2FScreen%20Shot%202024-05-15%20at%2011.19.59%20AM.png?alt=media&#x26;token=bc1fbb59-5a36-47f8-985f-da9c743e3adb" alt="A screenshot showing creation of an OAuth client in an identity provider"><figcaption></figcaption></figure>

Click on Create Credentials, select OAuth Client ID, select Web Application as the type, name it appropriately, and under Authorized Redirect URIs, enter the Callback URL you got from GitBook.

Click Create. Make a note of the Client ID and Client Secret. We will need these to finish configuring of our integration in GitBook.

### Install and configure the OIDC integration

Navigate to integrations within the GitBook app, select authenticated access as the category, and install the OIDC integration. Install the OIDC integration on your chosen docs site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FCZy21M4LIPwMVSxI3ec1%2FScreen%20Shot%202024-12-13%20at%203.37.39%20PM.png?alt=media&#x26;token=4e31d496-04eb-4d00-ac45-011b543edfe4" alt="A GitBook screenshot showing the OIDC integration installation"><figcaption></figcaption></figure>

Once you've installed it on your site, go to configuration and make a note of the Callback URL right above the Save button. We may need it to set up the Identity Provider.

Open up the OIDC integration's configuration screen for the space you installed the integration on.

It should look like the following image

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F04b2yAGjDIJQsA2aPIEO%2FScreen%20Shot%202024-12-13%20at%203.38.30%20PM.png?alt=media&#x26;token=e89e34c5-0e95-4547-a507-cc1d727b6ee5" alt="A GitBook screenshot showing the OIDC configuration screen"><figcaption></figcaption></figure>

For Client ID and Client Secret, paste in the values you got for your identity provider.

Now, you will need to find the Authorization Endpoint and Access Token Endpoint for your Identity Provider. For Google, these are `https://accounts.google.com/o/oauth2/v2/auth` and `https://oauth2.googleapis.com/token` respectively.

{% hint style="info" %}
If you are not using Google, these endpoints will be different for you. Please look into the documentation of your identity provider to locate these endpoints
{% endhint %}

For OAuth Scope, its value will be again be different depending on your Identity Provider. In case of Google, you can enter `openid`.

{% hint style="info" %}
Please look at the list of allowed scopes in your Identity Provider's documentation, and enter the value of the least permissive scope. We only use the Access Token to verify that the user is authenticated, and we do not use the Access Token to fetch any further information. So, entering the least permissive scope is the best security recommendation.
{% endhint %}

Hit Save.

Now, in GitBook, close the integrations modal and click on the Manage site button. Navigate to **Audience**, select **Authenticated access**, and choose OIDC as the backend. Then, click **Update audience**. Go to the site’s screen and click **Publish**.\
\
The site is now published behind authenticated access controlled by your Auth0 application. To try it out, click on Visit. You will be asked to sign in with OIDC, which confirms that your site is published behind authenticated access using Auth0.



# Setting up a custom backend

Set up a custom login screen for visitors to your docs.

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

This guide walks you through setting up a protected sign-in screen for your GitBook documentation site using your own **custom** authentication backend.

{% hint style="info" %}
If you are using one of the authentication providers we support or have an [OpenID Connect](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol) (OIDC) compliant backend, check out our integration guides for a more streamlined setup:\
\
[Auth0](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/setting-up-auth0) | [Azure AD](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/setting-up-azure-ad) | [Okta](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/setting-up-okta) | [AWS Cognito](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/setting-up-aws-cognito) | [OIDC](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access/setting-up-oidc)
{% endhint %}

### Overview

To setup a custom authentication system for your GitBook site, follow these key steps:

{% stepper %}
{% step %}
[**Create a custom backend to authenticate your users**](#id-1.-create-a-custom-backend-to-authenticate-your-users)

Implement a backend that prompts users to login and authenticate them.
{% endstep %}

{% step %}
[**Sign and pass a JWT token to GitBook**](#id-2.-sign-and-pass-a-jwt-token-to-gitbook)

Create a JWT token and sign it with your site’s private key.
{% endstep %}

{% step %}
[**Configure a fallback URL**](#id-3.-configure-a-fallback-url)

Configure a URL to be used when an unauthenticated visitor access your site.
{% endstep %}

{% step %}
[**Set up multi-tenant authenticated access (optional)**](#id-4.-set-up-multi-tenant-authenticated-access)

Configure your backend to handle authentication across multiple GitBook sites.
{% endstep %}

{% step %}
[**Configure your backend for adaptive content (optional)**](#id-5.-configure-your-backend-for-adaptive-content)

Configure your backend to work with adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### 1. Create a custom backend to authenticate your users

In order to start authenticating users before they can visit your documentation, you’ll need to set up a server that can handle login and authentication of users.

Your backend should:

* Prompt users to log in using your preferred authentication method.
* Validate user credentials and authenticate them.
* Generate and sign a **JSON Web Token (JWT)** upon successful authentication.
* Redirect users to GitBook with the JWT included in the URL.

### 2. Sign and pass a JWT token to GitBook

Once your backend authenticates a user, it must **generate a JWT** and **pass it to GitBook** when **redirecting** them to your site. The token should be signed using the **private key** provided in your site's audience settings after [enabling authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/enabling-authenticated-access#enable-authenticated-access).

The following example should demonstrate how a login request handler in your custom backend could look like:

{% code title="index.ts" %}

```typescript
import { Request, Response } from 'express';
import * as jose from 'jose';

import { getUserInfo } from '../services/user-info-service';
import { getFeatureFlags } from '../services/feature-flags-service';

const GITBOOK_VISITOR_SIGNING_KEY = process.env.GITBOOK_VISITOR_SIGNING_KEY!;
const GITBOOK_DOCS_URL = 'https://mycompany.gitbook.io/myspace';

export async function handleAppLoginRequest(req: Request, res: Response) {
    // Your business logic for handling the login request
    // For example, checking credentials and authenticating the user
    //
    // e.g.:
    // const loggedInUser = await authenticateUser(req.body.username, req.body.password);
    
    // Generate a signed JWT
    const gitbookVisitorJWT = await new jose.SignJWT({})
        .setProtectedHeader({ alg: 'HS256' })
        .setIssuedAt()
        .setExpirationTime('2h') // Arbitrary 2-hour expiration
        .sign(new TextEncoder().encode(GITBOOK_VISITOR_SIGNING_KEY));
    
    // Redirect the user to GitBook with the JWT token in the URL
    const redirectURL = `${GITBOOK_DOCS_URL}/?jwt_token=${gitbookVisitorJWT}`;
    res.redirect(redirectURL);
}
```

{% endcode %}

### 3. Configure a fallback URL

The fallback URL is used when an unauthenticated visitor tries to access your protected site. GitBook will then redirect them to this URL.

This URL should point to a handler in your custom backend, where you can prompt them to login, authenticate and then redirect them back to your site with the JWT included in the URL.

For instance, if your login screen is located at `https://example.com/login`, you should include this value as the fallback URL.

You can configure this fallback URL within your site’s audience settings under the "Authenticated access" tab.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FB48PEdMz1tCDf0Q0lo4d%2FScreenshot%202025-03-25%20at%2015.00.08.png?alt=media&#x26;token=e22fe867-e1f6-44f7-8b4f-a868ac620464" alt="A GitBook screenshot showing where to configure a fallback URL"><figcaption><p>Configure a fallback URL</p></figcaption></figure>

When redirecting to the fallback URL, GitBook includes a `location` query parameter to the fallback URL that you can leverage in your handler to redirect the user to the original location of the user:

```javascript
const gitbookVisitorJWT = await new jose.SignJWT({})
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('2h') // Arbitrary 2-hour expiration
    .sign(new TextEncoder().encode(GITBOOK_VISITOR_SIGNING_KEY));
    
// Redirect to the original GitBook docs URL with the JWT included as jwt_token query parameter
// If a location is provided, the user will be redirected back to their original destination
const redirectURL = `${GITBOOK_DOCS_URL}/${req.query.location || ''}?jwt_token=${gitbookVisitorJWT}`;
res.redirect(redirectURL);
```

{% hint style="warning" %}
Because GitBook relies on the `location` search param - you cannot use it in your fallback URL. For example, `https://auth.gitbook.com/?location=something` is not a valid fallback URL.
{% endhint %}

### 4. Set up multi-tenant authenticated access (optional)

If you’re using GitBook as a platform to provide content to your different customers, you probably need to set up multi-tenant authenticated access. Your authentication backend needs to be responsible for handling authentication across multiple different sites. This is possible in GitBook with a few small tweaks to your custom authentication backend code.

#### Adding all tenants to your authentication server

Your authentication backend will need to know the JWT signing keys and the URLs of all the GitBook sites you expect it to handle. If you have two sites in your organization for Customer A and Customer B, you can imagine your authentication code storing such mapping:

```typescript
const CUSTOMER_A = {
  jwtSigningKey: 'aaa-aaa-aaa-aaa',
  url: 'https://mycompany.gitbook.io/customer-a'
};

const CUSTOMER_B = {
  jwtSigningKey: 'bbb-bbb-bbb-bbb',
  url: 'https://mycompany.gitbook.io/customer-b'
};
```

#### Giving your authentication server additional context

When GitBook is unable to authenticate a user's request, it redirects them to the fallback URL. This URL points to your authentication backend, which is responsible for authenticating the user and redirecting them back to the requested content.

To support multiple tenants, your authentication backend needs to know which GitBook site the user is meant to access. This information can be passed in the fallback URL.

So for example, you could setup the fallback URLs for each sites as follow:

<table><thead><tr><th width="150.75390625">GitBook Site</th><th>Fallback URL</th></tr></thead><tbody><tr><td>Customer A site</td><td><code>https://auth-backend.acme.org/login?site=customer-a</code></td></tr><tr><td>Customer B site</td><td><code>https://auth-backend.acme.org/login?site=customer-b</code></td></tr></tbody></table>

Your authentication backend can then check this information and handle the redirection to the correct site accordingly:

```javascript
const customerInfo = req.query.site === 'customer-a' ? CUSTOMER_A : CUSTOMER_B;
  
const gitbookVisitorJWT = await new jose.SignJWT({})
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('2h') // Arbitrary 2-hour expiration
    .sign(new TextEncoder().encode(customerInfo.jwtSigningKey));
    
// Redirect to the original GitBook docs URL with the JWT included as jwt_token query parameter
// If a location is provided, the user will be redirected back to their original destination
const redirectURL = `${customerInfo.url}/${req.query.location || ''}?jwt_token=${gitbookVisitorJWT}`;
res.redirect(redirectURL);
```

### 5. Configure your backend for adaptive content (optional)

{% hint style="warning" %}
This feature is still under development and coming soon to the [Ultimate site plan](https://www.gitbook.com/pricing).&#x20;

Please sign up for the waitlist at <https://www.gitbook.com/#alpha-waitlist>
{% endhint %}

To leverage the Adaptive Content capability in your authenticated access setup, you can include additional user attributes (claims) in the payload of the JWT that your custom backend generates and include in the URL when redirecting the user to the site.

These claims when included in the JWT are used by GitBook to [adapt content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content) dynamically for your site visitors.

Putting it all together, the following code example demonstrates how you could include these claims in the JWT, which can then be used by GitBook to adapt content for your visitors:

{% code title="index.ts" %}

```typescript
import { Request, Response } from 'express';
import * as jose from 'jose';

import { getUserInfo } from '../services/user-info-service';
import { getFeatureFlags } from '../services/feature-flags-service';

const GITBOOK_VISITOR_SIGNING_KEY = process.env.GITBOOK_VISITOR_SIGNING_KEY!;
const GITBOOK_DOCS_URL = 'https://mycompany.gitbook.io/myspace';

export async function handleAppLoginRequest(req: Request, res: Response) {
    // Your business logic for handling the login request
    // For example, checking credentials and authenticating the user
    //
    // e.g.:
    // const loggedInUser = await authenticateUser(req.body.username, req.body.password);
    
    // For the purpose of this example, assume a logged-in user object
    const loggedInUser = { id: '12345' }; // Replace with actual authentication logic

    // Retrieve user information to pass to GitBook
    const userInfo = await getUserInfo(loggedInUser.id);
    
    // Generate a signed JWT and include the user attributes as claims
    const gitbookVisitorClaims = {
        firstName: userInfo.firstName,
        lastName: userInfo.lastName,
        isBetaUser: userInfo.isBetaUser,
        products: userInfo.products.map((product) => product.name),
        featureFlags: await getFeatureFlags({ userId: loggedInUser.id })
    };
    
    const gitbookVisitorJWT = await new jose.SignJWT(gitbookVisitorClaims)
        .setProtectedHeader({ alg: 'HS256' })
        .setIssuedAt()
        .setExpirationTime('2h') // Arbitrary 2-hour expiration
        .sign(new TextEncoder().encode(GITBOOK_VISITOR_SIGNING_KEY));
    
    // Redirect the user to GitBook with the JWT token in the URL
    const redirectURL = `${GITBOOK_DOCS_URL}/?jwt_token=${gitbookVisitorJWT}`;
    res.redirect(redirectURL);
}
```

{% endcode %}

After setting up and configuring the right claims to send to GitBook, head to “[Adapting your content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content)” to continue configuring your site.



# Adaptive content

Deliver a tailored documentation experience based on who's reading.

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

When a user visits your site, you may already know things about them — such as who they are, which plan they’re subscribed to, and which features they have access to.

Adaptive content helps to build a tailored documentation experience based on who is reading.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwYV7jtuVoJNcmEHjnRTO%2F20_08_25_adaptive_content.webp?alt=media&#x26;token=c7373b37-d23c-4752-8e29-537c99097f0d" alt="A GitBook screenshot showing adaptive content controls"><figcaption><p>Personalize your user’s documentation experience through adaptive content</p></figcaption></figure>

<p align="center"><a href="https://gitbook.com/adaptive-content-demo/" class="button primary">Launch the demo site</a></p>

{% hint style="info" %}
Adaptive content is slightly different from [authenticated access](https://gitbook.com/docs/documentation/publishing-documentation/authenticated-access), although they can work together.&#x20;

While authenticated access allows you to protect your docs through a login, adaptive content customizes published material based on various authentication methods — including authenticated access or those from your own app.
{% endhint %}

### How it works

Adaptive content works in one of two ways:

1. Passing data from your app to GitBook
2. Passing data from authenticated access

When a user visits your sites, we call the data they bring with them their “claims” — basically data that helps to identify a user. These claims are controllable by you — the site author — and can be used through the GitBook editor to show or hide different pages, variants, and sections in your docs.

Head to our page about [enabling adaptive content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content) to start setting up adaptive content for your site.



# Enabling adaptive content

Choose an authentication method to pass user data to GitBook.

To start customizing your documentation experience for your readers, you'll need to enable adaptive content and decide how your visitor data is passed to GitBook. This lets your site's content dynamically adapt based on who's viewing it.

### Enable adaptive content

Before you’re able to pass user data to GitBook, you’ll need to configure your site to use adaptive content.

Head to your [site’s settings](https://gitbook.com/docs/documentation/publishing-documentation/site-settings), and enable **Adaptive content** from your site’s audience settings. Once enabled, you’ll get a generated ‘Visitor token signing key’, which you’ll need in order to continue the adaptive content setup.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FH5SCBHouCTo5hrp9ymfW%2F18_07_25_enable_adaptive_content.svg?alt=media&#x26;token=3deb470a-f1c9-4621-87fb-7379d95682f0" alt="A GitBook screenshot showing the enable adaptive content toggle"><figcaption><p>Enable adaptive content</p></figcaption></figure>

### Set your visitor schema

After enabling adaptive content, you’ll need to define a schema for the types of claims you expect GitBook to receive when a user visits your site.

The visitor schema should reflect how these claims are structured when sent to GitBook.

For example, if you expect a visitor to potentially be a beta user in your product, you would set a visitor schema similar to:

```json
{
  "type": "object",
  "properties": {
    "isBetaUser": {
      "type": "boolean",
      "description": "Whether the visitor is a Beta user."
    }
  },
  "additionalProperties": false
}
```

This will also help you use autocomplete when configuring your claims in the [condition editor](https://gitbook.com/docs/documentation/publishing-documentation/adapting-your-content#working-with-the-condition-editor). Visitor schemas only support the following types:

{% tabs %}
{% tab title="Strings" %}
Read claims being passed in as strings.

Strings **must contain an enum** key, which needs to contain any expected values that would be found on the key being read.

```json
{
  "type": "object",
  "properties": {
    "language": {
          "type": "string",
          "description": "The language of the visitor",
          "enum": [
            "en",
            "fr",
            "it"
          ]
  },
  "additionalProperties": false
}
```

{% endtab %}

{% tab title="Booleans" %}
Read claims being passed in as booleans.

```json
{
  "type": "object",
  "properties": {
    "isBetaUser": {
      "type": "boolean",
      "description": "Whether the visitor is a Beta user."
    },
  },
  "additionalProperties": false
}
```

{% endtab %}

{% tab title="Objects" %}
Nest claims in an object to group similar values.

```json
{
  // Top level claims
  "type": "object",
  "properties": {
    // Nested claims
    "access": {
      "type": "object",
      "description": "User’s access to product feature",
      "properties": {
        "isAlphaUser": {
          "type": "boolean",
          "description": "Whether the visitor is a Alpha user."
        },
        "isBetaUser": {
          "type": "boolean",
          "description": "Whether the visitor is a Beta user."
        },
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

{% endtab %}
{% endtabs %}

### Set an unsigned claim

Unsigned claims are a specific type of claim that identifies claims coming through that might not be signed by a client application. It is required to set claims in your visitor schema as `unsigned` if you are passing claims through URL parameters, unsigned cookies, and feature flags.

If you intend to work with unsigned claims, you will need to declare the claims you are expecting in the schema under an “unsigned” prop alongside your signed claims.

```json
{
  "type": "object",
  "properties": {
    "isBetaUser": {
      "type": "boolean",
      "description": "Whether the visitor is a Beta user."
    },
    // Add unsigned claims
    "unsigned": {
      "type": "object",
      "description": "Unsigned claims of the site visitor.",
      "properties": {
        "language": {
          "type": "string",
          "description": "The language of the visitor",
          "enum": [
            "en",
            "fr",
            "it"
          ]
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

### Pass visitor data to GitBook

GitBook provides different ways to pass visitor data to adapt your site's content. After defining your schema, you’ll need to decide how you want to pass your visitor data to GitBook.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><i class="fa-cookie">:cookie:</i></td><td><strong>Cookies</strong></td><td>Pass visitor data into your docs through a public or signed cookie.</td><td><a href="enabling-adaptive-content/cookies">cookies</a></td></tr><tr><td><i class="fa-link">:link:</i></td><td><strong>URL</strong></td><td>Pass visitor data into your docs through URL query parameters.</td><td><a href="enabling-adaptive-content/url">url</a></td></tr><tr><td><i class="fa-flag">:flag:</i></td><td><strong>Feature flags</strong></td><td>Pass visitor data into your docs through a feature flag provider.</td><td><a href="enabling-adaptive-content/feature-flags">feature-flags</a></td></tr><tr><td><i class="fa-lock">:lock:</i></td><td><strong>Authenticated access</strong></td><td>Pass visitor data into your docs through an authentication provider.</td><td><a href="enabling-adaptive-content/authenticated-access">authenticated-access</a></td></tr></tbody></table>



# Cookies

Pass visitor data into your docs through a public or signed cookie.

{% hint style="info" %}
Head to our guides to find a [full walk-through](https://app.gitbook.com/s/LBGJKQic7BQYBXmVSjy0/docs-personalization-and-authentication/setting-up-adaptive-content) on setting up adaptive content with cookies.
{% endhint %}

{% hint style="warning" %}
Using adaptive content with feature flags requires adding code to your application.

This method only works if your site is served under a [custom domain](https://gitbook.com/docs/documentation/publishing-documentation/custom-domain).
{% endhint %}

You can pass visitor data to your docs through your visitors browser cookies. Below is an overview of the different methods.

<table data-full-width="false"><thead><tr><th width="335.125">Method</th><th width="266.6015625">Use-cases</th><th width="206.58984375">Ease of setup</th><th width="202">Security</th><th>Format</th></tr></thead><tbody><tr><td>Signed cookie <code>gitbook-visitor-token</code></td><td>API test credentials, customer identification</td><td>Require signing and a custom domain</td><td><span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span> Properties can only be defined by the backend</td><td>JWT</td></tr><tr><td>Public cookie <code>gitbook-visitor-public</code></td><td>Feature flags, roles</td><td>Easy to set up</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span> Visitor can override the properties</td><td>JSON</td></tr></tbody></table>

### Public cookie

To pass data to GitBook from a public cookie, you’ll need to send the data from your application by setting a public `gitbook-visitor-public` cookie.

Below is a simple JavaScript example:

```javascript
import Cookies from 'js-cookie';

const cookieData = {
  isLoggedIn: true,
  isBetaUser: false,
};

Cookies.set('gitbook-visitor-public', JSON.stringify(cookieData), {
  secure: true,
  domain: '*.acme.org',
})
```

{% hint style="warning" %}
Data passed through public cookies must be defined in your visitor schema through an [unsigned](https://gitbook.com/docs/publishing-documentation/adaptive-content/enabling-adaptive-content#setting-unsigned-claims) object.
{% endhint %}

### Signed cookie

To pass data to GitBook more securely, you’ll need to send the data as a [JSON Web Token](https://jwt.io/introduction) from your application in a cookie named `gitbook-visitor-token` tied to your domain.

To set this up, you'll need to adjust your application’s login flow to include the following steps:

{% stepper %}
{% step %}
**Generate a JWT when users logs in to your application**

Whenever a user logs in to your product, generate a JWT that contains selected attributes of your authenticated user's info.
{% endstep %}

{% step %}
**Sign the JWT using the site's visitor signing key**

Then, make sure to sign the JWT using the site's **visitor signing key**, which you can find in your site’s audience settings after enabling Adaptive Content.
{% endstep %}

{% step %}
**Store the JWT in a wildcard session cookie**

Finally you need to store the signed JWT containing your user's info into a wildcard session cookie **under your product domain**.

For example, if your application is served behind the `app.acme.org` domain, the cookie will need to be created under the `.acme.org` wildcard domain.
{% endstep %}
{% endstepper %}

Below is a simple TypeScript example:

```typescript
import * as jose from 'jose';

import { Request, Response } from 'express';

import { getUserInfo } from '../services/user-info-service';
import { getFeatureFlags } from '../services/feature-flags-service';

const GITBOOK_VISITOR_SIGNING_KEY = process.env.GITBOOK_VISITOR_SIGNING_KEY;
const GITBOOK_VISITOR_COOKIE_NAME = 'gitbook-visitor-token';


export async function handleAppLoginRequest(req: Request, res: Response) {
   // Your business logic for handling the login request
   // For example, checking credentials and authenticating the user
   //
   // e,g:
   // const loggedInUser = await authenticateUser(req.body.username, req.body.password);

   // After authenticating the user, retrieve user information that you wish
   // to pass to GitBook from your database or user service.
   const userInfo = await getUserInfo(loggedInUser.id);
      
   // Build the JWT payload with the user's information
   const gitbookVisitorClaims = {
       firstName: userInfo.firstName,
       lastName: userInfo.lastName,
       isBetaUser: userInfo.isBetaUser
       products: userInfo.products.map((product) => product.name),
       featureFlags: await getFeatureFlags({userId: loggedInUser.id})
   }
   
   // Generate a signed JWT using the claims
   const gitbookVisitorJWT = await new jose.SignJWT(gitbookVisitorClaims)
     .setProtectedHeader({ alg: 'HS256' })
     .setIssuedAt()
     .setExpirationTime('2h') // abritary 2 hours expiration
     .sign(GITBOOK_VISITOR_SIGNING_KEY);
     
  // Include a `gitbook-visitor-token` cookie including the encoded JWT in your
  // login handler response
  res.cookie(GITBOOK_VISITOR_COOKIE_NAME, gitbookVisitorJWT, {
     httpOnly: true,
     secure: process.env.NODE_ENV === 'production',
     maxAge: 2 * 60 * 60 * 1000, // abritary 2 hours expiration
     domain: '.acme.org' //
  });
  
  // Rest of your login handler logic including redirecting the user to your app
  res.redirect('/'); // Example redirect
}
```



# URL

Pass visitor data into your docs through URL query parameters.

{% hint style="info" %}
Head to our guides to find a [full walk-through](https://gitbook.com/docs/guides/product-guides/how-to-personalize-your-gitbook-site-using-url-parameters-and-adaptive-content) on setting up adaptive content with cookies.
{% endhint %}

You can pass visitor data to your docs through URL query parameters. Below is an overview of the method:

<table data-full-width="false"><thead><tr><th width="325.45703125">Method</th><th width="266.6015625">Use-cases</th><th width="206.58984375">Ease of setup</th><th width="202">Security</th><th>Format</th></tr></thead><tbody><tr><td>Query parameters <code>visitor.&#x3C;prop>=</code></td><td>Feature flags, roles</td><td>Easy to use</td><td><span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span> Visitor can override the properties</td><td>JSON</td></tr></tbody></table>

### Query parameters

To pass data to GitBook through URL parameters, you’ll need to pass the data in the URL in the format `visitor.<prop>`.

For example:

```url
https://docs.acme.org/?visitor.language=fr
```

This will allow you to use these claims in the [condition editor](https://gitbook.com/docs/documentation/publishing-documentation/adapting-your-content#working-with-the-condition-editor) under the unsigned object:

```javascript
visitor.claims.unsigned.language === "fr"
```

{% hint style="warning" %}
Data passed through query parameters must be defined in your visitor schema through an [unsigned](https://gitbook.com/docs/publishing-documentation/adaptive-content/enabling-adaptive-content#setting-unsigned-claims) object. Additionally, query parameters can be easily changed by the visitor and are best suited for non-sensitive information.
{% endhint %}

### Video tutorial

{% embed url="<https://www.youtube.com/embed/hCd2_AAHU_I?si=jm2VOThMVh7NdJm>\_" %}



# Feature flags

Pass visitor data into your docs through a feature flag provider.

{% hint style="warning" %}
Using adaptive content with feature flags requires adding code to your application.

Currently, the GitBook helper only supports React based setups.
{% endhint %}

GitBook provides helper functions and integrations for popular feature flag service providers like [**LaunchDarkly**](#launchdarkly) and [**Reflag**](#reflag).

This allows you to read the feature flags users have access to in your product, as they read your docs. This is useful if you need to show documentation for features that are only available to a specific group of people.

### LaunchDarkly

LaunchDarkly allows you to send feature flag access as claims through the [`launchdarkly-react-client-sdk`](https://launchdarkly.com/docs/sdk/client-side/react/react-web) and GitBook’s [`@gitbook/adaptive`](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content/broken-reference) package.

If you’re using LaunchDarkly feature flags in your product already, chances are you already have this package configured.

To pass you these feature flags as claims to GitBook, follow these steps:

{% stepper %}
{% step %}
**Install the LaunchDarkly integration**

To get started, you’ll first need to [install the LaunchDarkly integration](https://app.gitbook.com/integrations/launchdarkly) into your GitBook site.
{% endstep %}

{% step %}
**Set up your project and access keys**

Add your project key and your service access token from your [LaunchDarkly settings](https://app.launchdarkly.com/settings) to the integration’s configuration.
{% endstep %}

{% step %}
**Install and add the GitBook helper to your application**

After setting up the LaunchDarkly integration, you’ll need to install the GitBook adaptive content helper in your application.

```bash
npm install @gitbook/adaptive
```

{% endstep %}

{% step %}
**Configure your application**

You’ll need to use the `withLaunchDarkly` helper with the LaunchDarkly React SDK to pass context into GitBook.

<pre class="language-javascript"><code class="lang-javascript">import { render } from 'react-dom';
<strong>import { withLaunchDarkly } from '@gitbook/adaptive';
</strong><strong>import { asyncWithLDProvider, useLDClient } from 'launchdarkly-react-client-sdk';
</strong>import MyApplication from './MyApplication';

function PassFeatureFlagsToGitBookSite() {
<strong>    const ldClient = useLDClient();
</strong>    React.useEffect(() => {
        if (!ldClient) {
            return;
        }
<strong>        return withLaunchDarkly(ldClient);
</strong>    }, [ldClient]);
    return null;
}
(async () => {
    const LDProvider = await asyncWithLDProvider({
        clientSideID: 'client-side-id-123abc',
        context: {
            kind: 'user',
            key: 'user-key-123abc',
            name: 'Sandy Smith',
            email: 'sandy@example.com'
        },
        options: { /* ... */ }
    });
    render(
        &#x3C;LDProvider>
            &#x3C;PassFeatureFlagsToGitBookSite />
            &#x3C;MyApplication />
        &#x3C;/LDProvider>,
        document.getElementById('reactDiv'),
    );
})();
</code></pre>

{% endstep %}

{% step %}
**Check your visitor schema**

A [visitor schema](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content/..#set-your-visitor-schema) is required in order for your claims to be able to be read in your published site. Installing and configuring the LaunchDarkly integration should automatically set your visitor schema for you.
{% endstep %}

{% step %}
**Personalize your content**

After setting your visitor schema, you’re ready to tailor your docs experience for the users visiting your site, using the feature flags the user has access to.

Any feature flag value available in LaunchDarkly will be exposed as part of the visitor schema under the `visitor.claims.unsigned.launchdarkly` object. Read more about unsigned claims [here](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content/..#set-an-unsigned-claim).

Head to [adapting your content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content) to learn more about personalizing your docs for your users.
{% endstep %}
{% endstepper %}

### Reflag

Reflag allows you to send feature flag access as claims through the [`@reflag/react-sdk`](https://www.npmjs.com/package/@reflag/react-sdk) and GitBook’s [`@gitbook/adaptive`](https://github.com/GitbookIO/integrations/tree/main/packages/adaptive) package.

If you’re using Reflag feature flags in your product already, chances are you already have this package configured.

To pass you these feature flags as claims to GitBook, follow these steps:

{% stepper %}
{% step %}
**Install the Reflag Integration**

To get started, you’ll first need to [install the Reflag integration](https://app.gitbook.com/integrations/bucket) into your GitBook site.
{% endstep %}

{% step %}
**Set up your secret key**

Add your secret key from your [Reflag settings](https://app.reflag.com/envs/current/settings/app-environments) to the integration’s configuration.
{% endstep %}

{% step %}
**Install the GitBook helper to your application**

After setting up the Reflag integration, you’ll need to install the GitBook adaptive content helper in your application.

```bash
npm install @gitbook/adaptive
```

{% endstep %}

{% step %}
**Configure your application**

You’ll need to use the `withReflag` helper with the Reflag React SDK to pass context into GitBook.

<pre class="language-javascript"><code class="lang-javascript"><strong>import { withReflag } from '@gitbook/adaptive';
</strong><strong>import { ReflagProvider, useClient } from '@reflag/react-sdk';
</strong>import MyApplication from './MyApplication';

function PassFeatureFlagsToGitBookSite() {
<strong>    const client = useClient();
</strong>    React.useEffect(() => {
        if (!client) {
            return;
        }
<strong>        return withReflag(client);
</strong>    }, [client]);
    return null;
}
export function Application() {
    const currentUser = useLoggedInUser();
    const appConfig = useAppConfig();
    return (
        &#x3C;ReflagProvider
            publishableKey={appConfig.reflagCom.publishableKey}
            user={{
                id: currentUser.uid,
                email: currentUser.email ?? undefined,
                name: currentUser.displayName ?? '',
            }}
            company={{
                id: currentUser.company.id,
            }}
        >
            &#x3C;PassFeatureFlagsToGitBookSite />
            &#x3C;MyApplication />
        &#x3C;/ReflagProvider>
    );
}
</code></pre>

{% endstep %}

{% step %}
**Check your visitor schema**

A [visitor schema](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content/..#set-your-visitor-schema) is required in order for your claims to be able to be read in your published site. Installing and configuring the Reflag integration should automatically set your visitor schema for you.
{% endstep %}

{% step %}
**Personalize your content**

After setting your visitor schema, you’re ready to tailor your docs experience for the users visiting your site, using the feature flags the user has access to.

Any feature flag value available in Reflag will be exposed as part of the visitor schema under the `visitor.claims.unsigned.reflag` object. Read more about unsigned claims [here](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/enabling-adaptive-content/..#set-an-unsigned-claim).

Head to [adapting your content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content) to learn more about personalizing your docs for your users.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Feature flag values are evaluated on the client side, so avoid using this method to pass sensitive or security-critical data.
{% endhint %}



---
**Navigation:** [← Previous](./04-content-variants.md) | [Index](./index.md) | [Next →](./06-authenticated-access.md)
