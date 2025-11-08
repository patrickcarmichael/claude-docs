---
title: "Setting up SSO & SCIM"
source: "https://docs.windsurf.com/windsurf/accounts/sso-scim"
---

# Setting up SSO & SCIM
Source: https://docs.windsurf.com/windsurf/accounts/sso-scim



This feature is only available to Teams and Enterprise users.

<Tabs>
  <Tab title="Google SSO">
    Windsurf now supports sign in with Single Sign-On (SSO) via SAML. If your organization uses Microsoft Entra, Okta, Google Workspaces, or some other identity provider that supports SAML, you will be able to use SSO with Windsurf.

    <Note>Windsurf only supports SP-initiated SSO; IDP-initiated SSO is NOT currently supported.</Note>

    ### Configure IDP Application

    On the google admin console (admin.google.com) click **Apps -> Web and mobile apps** on the left.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9d300c86c609da6ee3fb630e91f4de3e" data-og-width="530" width="530" data-og-height="788" height="788" data-path="assets/auth/sso-google.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9403af117b9c97981fe559adb9b978fc 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=058d140139f82caca5fee61a7d1f68cf 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b94d0aaf6b28f8646827af8918d07df8 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f3898fed99df69da663658fd214d8676 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7a78f68f99b617431f0df9f765a8bec0 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=19da5d516023353f4cc46dba47ce5b25 2500w" />
    </Frame>

    Click on **Add app**, and then **Add custom SAML app**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=44375b535f269f130aea8c5bd6e736be" data-og-width="514" width="514" data-og-height="534" height="534" data-path="assets/auth/sso-google2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=15b8ea405f2270379d74bfc0f4f2d59b 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4a7a6ea30e5b1656dd8e92612494d632 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=db37dd58c7c32527476d114151bb7b66 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=baa8aaa599b97b9c59f45eb0796febb4 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5c1ae0fe3ac82b2965a2eea3601af438 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f67c6c78e1ff1bd171532584e4aa7c2f 2500w" />
    </Frame>

    Fill out **App name** with `Windsurf`, and click **Next**.

    The next screen (Google Identity Provider details) on Google’s console page has data you’ll need to copy to Windsurf’s SSO settings on [https://windsurf.com/team/settings](https://windsurf.com/team/settings).

    * Copy **SSO URL** from Google’s console page to Windsurf’s settings under **SSO URL**

    * Copy **Entity ID** from Google’s console page to Windsurf’s settings under **Idp Entity ID**

    * Copy **Certificate** from Google’s console page to Windsurf’s settings under **X509 Certificate**

    * Click **Continue** on Google’s console page

    The next screen on Google’s console page requires you to copy data from Codeium’s settings page

    * Copy **Callback URL** from Codeium’s settings page to Google’s console page under **ACS URL**
    * Copy **SP Entity ID** from Codeium’s settings page to Google’s console page under **SP Entity ID**
    * Change **Name ID** format to **EMAIL**
    * Click **Continue** on Google’s console page

    The next screen on Google’s console page requires some configuration

    * Click on **Add Mapping**, select **First name** and set the **App attributes** to **firstName**
    * Click on **Add Mapping**, select **Last name** and set the **App attributes** to **lastName**
    * Click **Finish**

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c29f0ebf5a05dd5fae3a1127c4111d29" data-og-width="2078" width="2078" data-og-height="862" height="862" data-path="assets/auth/sso-google3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=585b8d21d5b284ee28d9bd911c0d4295 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1a0dd06112db14e2acabe0750583dd71 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c82b1e1f6cf07b54049170ee5ac36eda 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fdac0e1950fd2e618710c99cee1c7656 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=45f58fd68db2619d5e87b3995c7103bf 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d6ae5462ed098ae48de0aa6b5801cacf 2500w" />
    </Frame>

    On Codeium’s settings page, click **Enable Login with SAML**, and then click **Save**. Make sure to click on **Test Login** to make sure login works as expected. All users now will have SSO login enforced.
  </Tab>

  <Tab title="Azure AD SSO">
    Windsurf Enterprise now supports sign in with Single Sign-On (SSO) via SAML. If your organization uses Microsoft Entra ID (formerly Azure AD), you will be able to use SSO with Windsurf.

    <Note>Windsurf only supports SP-initiated SSO; IDP-initiated SSO is NOT currently supported.</Note>

    ## Part 1: Create Enterprise Application in Microsoft Entra ID

    <Note>All steps in this section are performed in the **Microsoft Entra ID admin center**.</Note>

    1. In Microsoft Entra ID, click on **Add**, and then **Enterprise Application**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=70c1ef27e1870d1f95176d12cd7c9c47" data-og-width="854" width="854" data-og-height="384" height="384" data-path="assets/auth/sso-azure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1b88d7269fba84433a203348fd8a3920 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2f71d980824f058c3a36d499f4f488d6 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9bef7d83fd3afa0d42b25b81ab20d8e3 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b9c7eb219d3ff471f38175b0be2cdac8 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6802d42ea85adeb86d22f32e59ef8a5f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0eac589296d06ffcf16e6d2bdc771d0c 2500w" />
    </Frame>

    2. Click on **Create your own application**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d8d3d2b159172edef9033487d1167b52" data-og-width="680" width="680" data-og-height="202" height="202" data-path="assets/auth/sso-azure2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=66949d79e560dcf2c75bcafdcfb1b54a 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6ad3c318b6e47fa95b3e8677d01846ce 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=febe960a9ff782cebaf247868fd22bee 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f1c804a5b3dd2310840c95327f46241c 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7c4186eb8abb76e222579aae95f5b000 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1274eed53f279fbe64b0d52294708672 2500w" />
    </Frame>

    3. Name your application **Windsurf**, select *Integrate any other application you don't find in the gallery*, and then click **Create**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=38dd3186171705ca16387dfff4a5b24b" data-og-width="968" width="968" data-og-height="342" height="342" data-path="assets/auth/sso-azure3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6c9dc6a0601145171999431fb61e0c4d 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=87b686e30cea98fa1075ceffc0fa40f1 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b03c9c18b557b0f3d113d86fa8c30577 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=43bd3dc28697ed33fe0342dd456d2d3d 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=20d19e9d664e7c835253b775229a969f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=abebde3954de441e86f120269ac6b092 2500w" />
    </Frame>

    ## Part 2: Configure SAML and User Attributes in Microsoft Entra ID

    <Note>All steps in this section are performed in the **Microsoft Entra ID admin center**.</Note>

    4. In your new Windsurf application, click on **Set up single sign on**, then click **SAML**.

    5. Click on **Edit** under **Basic SAML Configuration**.

    6. **Keep this Entra ID tab open** and open a new tab to navigate to the **Windsurf Teams SSO settings** at [https://windsurf.com/team/settings](https://windsurf.com/team/settings).

    7. In the **Microsoft Entra ID** SAML configuration form:
       * **Identifier (Entity ID)**: Copy the **SP Entity ID** value from the **Windsurf SSO settings page**
       * **Reply URL (Assertion Consumer Service URL)**: Copy the **Callback URL** value from the **Windsurf SSO settings page**
       * Click **Save** at the top

    8. Configure user attributes for proper name display. In **Microsoft Entra ID**, under **Attributes & Claims**, click **Edit**.

    9. Create 2 new claims by clicking **Add new claim** for each:
       * **First claim**: Name = `firstName`, Source attribute = `user.givenname`
       * **Second claim**: Name = `lastName`, Source attribute = `user.surname`

    ## Part 3: Configure SSO Settings in Windsurf Portal

    <Note>Complete the configuration in the **Windsurf portal** ([https://windsurf.com/team/settings](https://windsurf.com/team/settings)).</Note>

    10. In the **Windsurf SSO settings page**:
        * **Pick your SSO ID**: Choose a unique identifier for your team's login portal (this cannot be changed later)
        * **IdP Entity ID**: Copy the value from **Microsoft Entra ID** under **Set up Windsurf** → **Microsoft Entra Identifier**
        * **SSO URL**: Copy the **Login URL** value from **Microsoft Entra ID**
        * **X509 Certificate**: Download the **SAML certificate (Base64)** from **Microsoft Entra ID**, open the file, and paste the text content here

    11. In the **Windsurf portal**, click **Enable Login with SAML**, then click **Save**.

    12. **Test the configuration**: Click **Test Login** to verify the SSO configuration works as expected.

    <Note>**Important**: Do not log out or close the Windsurf settings page until you've successfully tested the login. If the test fails, you may need to troubleshoot your configuration before proceeding.</Note>
  </Tab>

  <Tab title="Okta SSO">
    Windsurf Enterprise now supports sign in with Single Sign-On (SSO) via SAML. If your organization uses Microsoft Entra, Okta, Google Workspaces, or some other identity provider that supports SAML, you will be able to use SSO with Windsurf.

    <Note>Windsurf only supports SP-initiated SSO; IDP-initiated SSO is NOT currently supported.</Note>

    ### Configure IDP Application

    Click on Applications on the left sidebar, and then Create App Integration

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e3f879d2fa7faeba003aa04e2c5d3a4a" data-og-width="1248" width="1248" data-og-height="962" height="962" data-path="assets/auth/sso-okta1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=07c6dc86816c5d6cf956401bee450128 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2f2d86ae21cdef97580a0824ca01ffc8 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ec432c4e43c969491df691687b1c8719 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4f42e54a6f8de42f3fa17349df08394e 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9f1cb10571d1c2ea02bf30638a762e9c 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5c76f872b9163ec64637213aa646ba30 2500w" />
    </Frame>

    Select SAML 2.0 as the sign-in method

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=df39e8a15a879d8f2798a4284087c567" data-og-width="1600" width="1600" data-og-height="1023" height="1023" data-path="assets/auth/sso-okta2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=26a63721d0018efa7b8a4800e6f408bb 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c052bfa279c58dc361223b5582a62c80 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=00ed32012a519da9011059476f423aa6 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=eb3839e1a82fa9bc1467a456a38a993b 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c678d8128c2aa8d5b42eb1ff185d80a8 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9586e95f5e7e3cc3f167548bdcec2b48 2500w" />
    </Frame>

    Set the app name as Windsurf (or to any other name), and click Next

    Configure the SAML settings as

    * Single sign-on URL to [https://auth.windsurf.com/\_\_/auth/handler](https://auth.windsurf.com/__/auth/handler)
    * Audience URI (SP Entity ID) to [www.codeium.com](http://www.codeium.com)
    * NameID format to EmailAddress
    * Application username to Email

    Configure the attribute statements as following, and then click **Next**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0903972c21dd13147a1adfe8791f1679" data-og-width="1398" width="1398" data-og-height="602" height="602" data-path="assets/auth/sso-okta3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f247cb5627519ba2052a1c66bcabac11 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8b0e97b79dbe969605c026e1d42918bf 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2c9e0db1830545f4605ec52128d0c13f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f21b1c853cd6e3fb6234eaba4936714a 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e207e6d97821d5b568bcb3175aaa877c 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5b9415f606224a480a8a21fd39d3c6b7 2500w" />
    </Frame>

    In the feedback section, select “This is an internal app that we have created”, and click **Finish**.

    ### Register Okta as a SAML provider

    You should be redirected to the Sign on tab under your custom SAML application. Now you’ll want to take the info in this page and fill it out in Windsurf’s SSO settings.

    * Open [https://windsurf.com/team/settings](https://windsurf.com/team/settings), and click on Configure SAML
    * Copy the text after ‘Issuer’ in Okta’s application page and paste it under Idp Entity ID
    * Copy the text after ‘Sign on URL’ in Okta’s application page and paste it under SSO URL
    * Download the Signing Certificate and paste it under X509 certificate
    * Check Enable Login with SAML and then click Save
    * Test the login with the Test Login button. You should see a success message:

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=574e091c869162bc41dc0aa36cd209fa" data-og-width="1046" width="1046" data-og-height="270" height="270" data-path="assets/auth/sso-okta4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c0de67fc05d02d94917d0eb38a93bfc7 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8a4532d29bde6a981fcfa56b16d2089c 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b166bddfbf60fd9be17010aedbc5f300 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4cc97e1ce5cbce8fe4b68f5736943608 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=10278811dec7a4ace3e27dafafe4dfdf 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=85583cef85521726dc3daa5307b6d733 2500w" />
    </Frame>

    At this point everything should have been configured, and can now add users to the new Windsurf Okta application.

    You should share your organization's custom Login Portal URL with your users and ask them to sign in via that link.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f3ccced59b0cbc7d0f0b1b6b39f1ee1c" data-og-width="988" width="988" data-og-height="312" height="312" data-path="assets/auth/sso-okta5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=02f37508edd5db6db866fd78e4a7acb9 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c12ca954c3031664fbcd2ca960b5383b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=75b02544b99c1e0a578234b57a07ea34 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cb11ec40d15a57198f780ae701029f44 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e51d3d2475655aef87f71b8b6105fb55 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=46ba7597ae1b616f37354006d6c5f907 2500w" />
    </Frame>

    Users who login to Windsurf via SSO will be auto-approved into the team.

    ### Caveats

    Note that Windsurf does not currently support IDP-initiated login flows.

    We also do not yet support OIDC.

    # Troubleshooting

    ### Login with SAML config failed: Firebase: Error (auth/operation-not-allowed)

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f65534799dfd8f941a68dc9fc72236d4" data-og-width="617" width="617" data-og-height="92" height="92" data-path="assets/auth/sso-okta6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4f6a8118ceb9a6511557fb3d5a89cfd8 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0cc4bcb6da5527e085f1e95e7565b2f6 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f1b542a1a5d5f18a6f07ce1fef0099f8 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5b8cdc47c2f5c742e4bef33ba4eb459a 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=087c32afb9c9f9850d596b218be3f923 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=02c760fbfa8d931d9781b596ede9d08d 2500w" />
    </Frame>

    This points to your an invalid SSO ID, or your SSO URL being incorrect, make sure it is alphanumeric and has no extra spaces or invalid characters. Please go over the steps in the guide again and make sure you use the correct values.

    ### Login with SAML config failed: Firebase: SAML Response \<Issuer> mismatch. (auth/invalid-credential)

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=446c8ad9510b7dcc8e744c7b80862c29" data-og-width="752" width="752" data-og-height="117" height="117" data-path="assets/auth/sso-okta7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=efd56e3400b53ceb05c2a6f3f16dca44 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f41a12504545c5f78998cb6f152564c9 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=21967311e74ec09546b31c6f49dc2dd8 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2d07267015603fb0e6d4ccd0ba3c1e81 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=619c0eaf530646e7b6dd294d5cc2712a 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a6217bfd37b259f63112cf22c3bb098b 2500w" />
    </Frame>

    This points to your IdP entity ID being invalid, please make sure you copy it correctly from the Okta portal, without any extra characters or spaces before or after the string.

    ### Failed to verify the signature in samlresponse

    This points to an incorrect value of your X509 certificate, please make sure you copy the correct key, and that it is formatted as:

    ```
    -----BEGIN CERTIFICATE-----
    value
    ------END CERTIFICATE------
    ```
  </Tab>

  <Tab title="Azure SCIM">
    Windsurf supports SCIM synchronization for users and groups with Microsoft Entra ID / Azure AD. It isn't necessary to setup SSO to use SCIM synchronization, but it is highly recommended.

    You'll need:

    * Admin access to Microsoft Entra ID / Azure AD
    * Admin access to Windsurf
    * An existing Windsurf Application on Entra ID (normally from your existing SSO application)

    <Note>
      **Service Key Permissions Required**

      The service key used for SCIM provisioning must have the following permissions:

      * **Team User Read** - Required to read user and group information
      * **Team User Update** - Required to create and update users and groups
      * **Team User Delete** - Required to deactivate/delete users and groups

      You can create a custom role with these permissions or use an existing admin role that includes them.
    </Note>

    ## Step 1: Create a Role with SCIM Permissions

    Before setting up SCIM provisioning, you need to create a role with the required permissions.

    1. Go to [Windsurf Team Settings](https://windsurf.com/team/settings)
    2. Under "Other Settings", click **Configure** next to **Role Management**
    3. Click **Add Role** and name it "SCIM Provisioning"
    4. Add the following permissions:
       * Team User Read
       * Team User Update
       * Team User Delete
    5. Click **Save**

    ## Step 2: Navigate to the existing Windsurf Application

    Go to Microsoft Entra ID on Azure, click on Enterprise applications on the left sidebar, and then click on the existing Windsurf application in the list.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c2425d24cadc8997c694a4b8a950169a" data-og-width="1258" width="1258" data-og-height="664" height="664" data-path="assets/auth/scim-azure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d2a0a5702a29ce1264d133bb5d3545c1 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f91fd83f53b34bab00d17c64358ac511 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4fc4661fa56013064005d8d923a13547 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=196d0489a6a5fdf4200ab92e7f5835d5 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fb03af9c8d156c0f5c2331ab5289d588 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=58bcf8651ea7dc34d4f7e561b7c6ab34 2500w" />
    </Frame>

    ## Step 3: Setup SCIM provisioning

    Click on Get started under Provision User Accounts in the middle (step 3), and then click on Get started again.

    <Frame>
      <img src="https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=1e9c8417da7568dc587941955f6d0ace" data-og-width="2582" width="2582" data-og-height="1858" height="1858" data-path="assets/auth/scim-azure2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=280&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=ce2a379d150e9b6383eeb48e52c96a01 280w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=560&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=4f51c287262043282173de0e1efc538c 560w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=840&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=21c65050cb093e453197eecbd348d773 840w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=1100&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=074fcdd9f2ef2e03ad23580185dd48fe 1100w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=1650&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=324c2d04d90956f34ee3c9a8c11ef548 1650w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=2500&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=cd3257cf044253173943f57c3b89a5b6 2500w" />
    </Frame>

    Under the Provisioning setup page, select the following options.

    Provisioning Mode:  Automatic

    Admin Credentials > Tenant URL: [https://server.codeium.com/scim/v2](https://server.codeium.com/scim/v2)

    <Frame>
      <img src="https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=ee0b34f8f0f131441eb9ca9e89ccbcda" data-og-width="560" width="560" data-og-height="416" height="416" data-path="assets/auth/scim-azure-admin-credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?w=280&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=c8581d4e4ad89b8a5edf7c138c364854 280w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?w=560&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=b689bb2e0efdf652f56a2a9b94b51f27 560w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?w=840&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=9a5e159c52dd929afbc02ce2292f05e5 840w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?w=1100&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=babac19088e58725307bdadaa495f9d6 1100w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?w=1650&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=6b2a1255d4ee047ee6f9aa4556dbaa21 1650w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure-admin-credentials.png?w=2500&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=ebf7a44a0053609e44623549c6aae9b5 2500w" />
    </Frame>

    Leave the Azure provisioning page open, now go to the Windsurf web portal, and click on the profile icon  in the NavBar on the top of the page.Under Team Settings, select Service Key and click on Add Service Key. Enter any key name (such as 'Azure SCIM Provisioning'), **select the "SCIM Provisioning" role you created earlier**, and click Create Service Key. Copy the output key, go back to the Azure page, paste it to Secret Token.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=80477c2c0d31631e38e217b22e9f42a3" data-og-width="1612" width="1612" data-og-height="1013" height="1013" data-path="assets/auth/scim-azure3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c547369cd10d19d77dbdb3586045c027 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e375425a3fe55cc5425f53e78b34f32f 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f15b3e3d387acd4ac3371b882595252a 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=49e6c3e224944aef0dfa88b13b401a74 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7dd27466493288c1d49a4327070f9f6f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4f40f4c6d50b15c421ba344a2013a8cc 2500w" />
    </Frame>

    (What you should see after creating the key on Windsurf)

    On the Provisioning page, click on Test Connection and that should have verified the SCIM connection.

    Now above the Provisioning form click on Save.

    ## Step 4: Configure SCIM Provisioning

    After clicking on Save, a new option Mappings should have appeared in the Provisioning page. Expand Mappings, and click on Provision Microsoft Entra ID Users

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=276791b068bd34c2bcbe5321e95abfd6" data-og-width="666" width="666" data-og-height="438" height="438" data-path="assets/auth/scim-azure4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6e36e1d72d4db00f49e114fdcc4a25be 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c11c14a5020abebd95bb43a970d88584 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=190236b1aaadafb15d6b7b7bc320ade2 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9d153d92aeb12bfaf4bd7868270d0e17 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=00ff52c3a669e6dbb4f7346e0831fa23 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=640997349e4672552c5f07b170e81d22 2500w" />
    </Frame>

    Under attribute Mappings, delete all fields under displayName, leaving only the fields userName, active, and displayName.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ddb9440614a4bc04f7c561bbf64a2d5a" data-og-width="1260" width="1260" data-og-height="190" height="190" data-path="assets/auth/scim-azure5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=394d02238802b10210ff30262a7e669e 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=da13a8c0a933b23e30d66c8a25c7509b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fef036d0c788f16fe95ebca4f360388d 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b3a2f8ec1b2b3482ec86aa26e3dad431 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b4c4b2f43e28978d2c3acafee01a3ed0 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3bf1b1e6d6863d74fd5344f25ac07ecc 2500w" />
    </Frame>

    For active, now click on Edit. Under Expression, modify the field to

    ```
    NOT([IsSoftDeleted])
    ```

    Then click Ok.

    Your user attributes should look like

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2beab12c979d3272d522293080634811" data-og-width="2826" width="2826" data-og-height="490" height="490" data-path="assets/auth/scim-azure6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4a8ee3358e95d0cd9d50bd0d538564a7 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a80cc215059b3780ca14c6ba370a6586 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=60057214f7d952812b598371e6c978d3 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e9bcab8fd1017d0892bea2a169ac02e9 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=786f7e9bf633dcbd60d8059a61caf106 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d4e9a7b532a2f85244bcaa90572ba06a 2500w" />
    </Frame>

    In the Attribute Mapping page, click on Save on top, and navigate back to the Provisioning page.

    Now click on the same page, under Mappings click on Provision Microsoft Entra ID Groups. Now only click delete for externalId, and click Save on top. Navigate back to the Provisioning page.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=11e89ce7d057c455ea00e0f469351b61" data-og-width="1258" width="1258" data-og-height="203" height="203" data-path="assets/auth/scim-azure7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cd56976ca792e265e725662085b17a19 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=bd115677b029f5e93699ab0a03768382 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d4bded4bf9d8689909e28c61ad510ce0 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d57065b32eff89171254875a8df64498 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b6360f57f064b8ef7a10b63de8cfc7ef 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=51e4b607b0652154956ce119600415ba 2500w" />
    </Frame>

    On the Provisioning page at the bottom, there should also be a Provisioning Status toggle. Set that to On to enable SCIM syncing. Now every 40 minutes your users and groups for the Entra ID application will be synced to Windsurf.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1214073ce82bd85a1c2a57834005608f" data-og-width="686" width="686" data-og-height="306" height="306" data-path="assets/auth/scim-azure8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=53139148e9394f611f436dc2128bcc33 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a227c181354a371f3ae4aa13673a5c89 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b9f85d836d1f06eb19a365d2f0cd9106 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6dd2cc814ee02f9bd402348e8c202d38 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=35af8b5f5183e3d4bfda09ec4d7b092b 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d69d23c955420b31547dabb0b0950863 2500w" />
    </Frame>

    Click on Save to finish, you have now enabled user and group syncing for SCIM. Only users and groups assigned to the application will be synced to Windsurf. Note that removing users only disables them access to Windsurf (and stops them from taking up a seat) rather than deleting users due to Azure's SCIM design.
  </Tab>

  <Tab title="Okta SCIM">
    Windsurf supports SCIM synchronization for users and groups with Okta. It isn't necessary to setup SSO to use SCIM synchronization, but it is highly recommended.

    You'll need:

    * Admin access to Okta
    * Admin access to Windsurf
    * An existing Windsurf Application on Okta (normally from your existing SSO application)

    ## Step 1: Navigate to the existing Windsurf Application

    Go to Okta, click on Applications, Applications on the left sidebar, and then click on the existing Windsurf application in the application list.

    ## Step 2: Enable SCIM Provisioning

    Under the general tab, App Settings click on Edit on the top right. Then tick the 'Enable SCIM Provisioning' checkbox, then click Save. A new provisioning tab should have showed up on the top.

    Now go to provisioning, click Edit and input in the following fields:

    SCIM connector base URL: [https://server.codeium.com/scim/v2](https://server.codeium.com/scim/v2)

    Unique identifier field for users: email

    Supported provisioning actions: Push New Users, Push Profile Updates, Push Groups

    Authentication Mode: HTTP Header

    For HTTP Header - Authorization, you can generate the token from

    * [https://windsurf.com/team/settings](https://windsurf.com/team/settings) and go to the Service Key Configuration
    * Click on Configure, then Add Service Key, and give your API key a name
    * Copy the API key, go back to Okta and paste it to HTTP Header - Authorization

    Click on Save after filling out Provisioning Integration.

    ## Step 3: Setup Provisioning

    Under the provisioning tab, on the left there should be two new tabs. Click on To App, and Edit Provisioning to App. Tick the checkbox for Create Users, Update User Attributes, and Deactivate Users, and click Save.

    After this step, all users assigned to the group will now be synced to Windsurf.

    ## Step 4: Setup Group Provisioning (Optional)

    In order to sync groups to Windsurf, you will have to specify which groups to push. Under the application, click on the Push Groups tab on top. Now click on + Push Groups -> Find Groups by name. Filter for the group you would like to add, make sure Push group memberships immediately is checked, and then click Save. The group will be created and group members will be synced to Windsurf. Groups can then be used to filter for group analytics in the analytics page.
  </Tab>

  <Tab title="SCIM API">
    This guide shows how to create and maintain groups in Windsurf with the SCIM API.

    There are reasons one may want to provision groups manually rather than with their Identity Provider (Azure/Okta). Companies may want Groups provisioned from a different internal source (HR website, Sourcecode Management Tool etc.) that Windsurf doesn't have access to, or companies may finer control to Groups than what their Idendity Provider provides. Groups can thus be created with an API via HTTP request instead. The following provides examples on the HTTP request via CURL.

    There are 5 main APIs here, Create Group, Add group members, Replace group members, Delete Group, and List Users in a Group.

    ### Create Group

    ```
    curl -k -X POST https://server.codeium.com/scim/v2/Groups -d '{
    "displayName": "<group name>",
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]
    }' -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### Add Group Members

    ```
    curl -X PATCH https://server.codeium.com/scim/v2/Groups/<group name> -d '{"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations":[
    {
    "op": "add",
    "path":"members",
    "value": [{"value": "<email 1>"}, {"value": "<email 2>"}]
    }]}' -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### Replace Group Members

    ```
    curl -X PATCH https://server.codeium.com/scim/v2/Groups/<group name> -d '{"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations":[
    {
    "op": "replace",
    "path":"members",
    "value": [{"value": "<email 1>"}, {"value": "<email 2>"}]
    }]}' -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### Delete Group

    ```
    curl -X DELETE https://server.codeium.com/scim/v2/Groups/<group name> -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### List Group

    ```
    curl -X GET -H "Authorization: Bearer <api secret key>" "https://server.codeium.com/scim/v2/Groups"
    ```

    ### List Users in a Group

    ```
    curl -X GET -H "Authorization: Bearer <api secret key>" "https://server.codeium.com/scim/v2/Groups/<group_id>"
    ```

    You'll have to at least create the group first, and then replace group to create a group with members in them. You'll also need to URL encode the group names if your group name has a special character like space, so a Group name such as 'Engineering Group' will have to be 'Engineering%20Group' in the URL.

    Note that users need to be created in Windsurf (through SCIM or manually creating the account) before they can be added to a group.

    ## User APIs

    There are also APIs for users as well. The following are some of the common SCIM APIs that Windsurf supports.

    Disable a user (Enable by replacing false to true):

    ```
    curl -X PATCH \
      https://server.codeium.com/scim/v2/Users/<user api key> \
      -H 'Content-Type: application/scim+json' \
      -H 'Authorization: Bearer <api secret key>' \
      -d '{
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        "Operations": [
          {
            "op": "replace",
            "path": "active",
            "value": false
          }
        ]
      }'
    ```

    Create a user:

    ```
    curl -X POST \
      https://server.codeium.com/scim/v2/Users \
      -H 'Content-Type: application/scim+json' \
      -H 'Authorization: Bearer <api secret key>' \
      -d '{
        "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
        "userName": "<email>",
        "displayName": "<full name>",
        "active": true,
    }' 
    ```

    Update name:

    ```
    curl -X PATCH \
      'https://<enterprise portal url>/_route/api_server/scim/v2/Users/<user api key>' \
        -H 'Authorization: Bearer <service key>' \
        -H 'Content-Type: application/scim+json' \
        -d '{
          "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
          "Operations": [
            {
              "op": "Replace",
              "path": "displayName",
              "value": "<new name>"
            }
          ]
       }'
    ```

    ## Creating Api Secret Key

    Go to [https://windsurf.com/team/settings](https://windsurf.com/team/settings). Under Service Key Configuration, click on Add Service Key. Enter any key name (such as 'Azure Provisioning Key') and click Create Service Key. Copy the output key and save it, you can now use the key to authorize the above APIs.
  </Tab>

  <Tab title="Duo">
    ## Prerequisites

    This guide assumes that you have Duo configured and acts as your organizational IDP, or has external IDP configured.

    You will need administrator access to both Duo and Windsurf accounts.

    ## Configure Duo for Windsurf

    1. Navigate to Applications, and add a Generic SAML service provider

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7e598d7e9a9ee2c3884caa1c60ba68ff" data-og-width="2230" width="2230" data-og-height="920" height="920" data-path="assets/auth/duo-sso-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3aec1b67ffcd908e98ff8fdc8efb9f13 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6fae9b15acbd20d00ba1342e29c03566 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2a92b9bd222d601f17445724a5740c4d 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=07e9adea00e0cab9016ad608222894f5 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=78b9eeb4b38c111b8a305442ecf22038 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f3fae806d80ac44e2feb9be6d623c311 2500w" />
    </Frame>

    2. Navigate to SSO in Team Settings

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=df8dde8b5b66a27532a3f42cdd803a17" data-og-width="1676" width="1676" data-og-height="1444" height="1444" data-path="assets/auth/windsurf-sso-team-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=24e65a0584ca92c5092e7a8b39d29a85 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a1aaf95ae69ecadbb071f972cf209d9a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8e0faad235bc863532c0cf5e8260d51f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c1d83d71116443257b524c595132a21d 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ad30f5f9af3dde7f95666544e8a483ef 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fcf587e6ef653eff95139a4d550e3e08 2500w" />
    </Frame>

    3. When enabling SAML for the first time, you will be required to set up your SSO ID. **You will not be able to change it later.**

       It is advised to set this to your organization or team name with alphanumeric characters only.

    4. Copy the `Entity ID` value from the Duo portal and paste it into the `IdP Entity ID` field in the Windsurf portal.

    5. Copy the `Single Sign-On URL` value from the Duo portal and paste it into the `SSO URL` field in the Windsurf portal.

    6. Copy the certificate value from the Duo portal and paste it in the `X509 Certificate` field in the Windsurf portal

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a7594c846a32e958a1bacfc01c5d3ef3" data-og-width="1536" width="1536" data-og-height="290" height="290" data-path="assets/auth/duo-sso-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=953a07d45101a639db53f6d22667c2a0 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1fbc8e990bebcbad0cd70f9bce288a8b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=769ba894b06157867cba16e6c7c9858b 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0e65532cda4e2039dfe07c02fd55aa52 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9095538c85e97051654d911b3bb10e91 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f907b2efbe7eaabdaa8aa8c6fb350d86 2500w" />
    </Frame>

    7. Copy the `SP Identity ID` value from the Windsurf portal and paste it into the `Entity ID` field in the Duo portal.

    8. Copy the `Callback URL (Assertion Consumer Service URL)` from the Windsurf portal and paste it into the `Assertion Consumer Service (ACS) URL` field in the Duo portal.

    9. In the Duo portal, configure the attribute statements as following:

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=bb3b514b94a6b0ebba19aa492c8be4a2" data-og-width="1676" width="1676" data-og-height="290" height="290" data-path="assets/auth/duo-sso-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a3de0ba0a3a188f34f178c200209cc17 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=88374d6e4f03ce1e45cb3094fe3e98e8 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d94638ec8d0a22bfa7ec00eb6514ec58 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f1c7e2ae138409c19a56dd12287fdaec 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7cfe010d8214ae7e7b655b5b6efba472 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=769ae9ad721e322e67f6d84bf139a33d 2500w" />
    </Frame>

    10. Enable the SAML login in the Windsurf portal so you can test it.

    **NOTE: DO NOT LOGOUT OR CLOSE THE WINDOW AT THIS POINT.**

    If you get an error or it times out, troubleshoot your settings, otherwise you have to disable your SAML Settings in the Windsurf portal.

    **If you logout or close the window without confirming a successful test - you may get locked out.**

    11. Once your test was successfully completed, you may logout. You can now use SSO sign in when browsing to your team/organization page with the SSO ID you have configured in step 3.

    [https://www.codeium.com/yourssoid/login](https://www.codeium.com/yourssoid/login)
  </Tab>

  <Tab title="PingID">
    ## Prerequisites

    This guide assumes that you have PingID configured and acts as your organizational IDP, or has external IDP configured.

    You will need administrator access to both PingID and Windsurf accounts.

    ## Configure PingID for Windsurf

    1. Navigate to Applications and add Windsurf as a SAML Application

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f86f6145e0eac599178ca9d9ee66b776" data-og-width="2258" width="2258" data-og-height="1068" height="1068" data-path="assets/auth/pingid-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0ad46a1b2741392e7b9317cb469e55ea 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=894534973d6592c29d157db78a542b26 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cea5d47e23bcff6ef6811358f893533f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1e2f9e94729c777800b7b9e4dfe32082 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6b7ab758d275aa2b2e63a9c4e01bea62 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=dfb01b08c5fdd2ebe1d9e80e5052426b 2500w" />
    </Frame>

    2. Navigate to SSO in Team Settings

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=df8dde8b5b66a27532a3f42cdd803a17" data-og-width="1676" width="1676" data-og-height="1444" height="1444" data-path="assets/auth/windsurf-sso-team-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=24e65a0584ca92c5092e7a8b39d29a85 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a1aaf95ae69ecadbb071f972cf209d9a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8e0faad235bc863532c0cf5e8260d51f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c1d83d71116443257b524c595132a21d 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ad30f5f9af3dde7f95666544e8a483ef 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fcf587e6ef653eff95139a4d550e3e08 2500w" />
    </Frame>

    3. When enabling SAML for the first time, you will be required to set up your SSO ID. **You will not be able to change it later.**

    It is advised to set this to your organization or team name with alphanumeric characters only.

    4. In PingID - choose to manually enter the configuration and fill out the fields with the following values:

    * ACS URLs - this is the `Callback URL (Assertion Consumer Service URL)` from the Windsurf portal.
    * Entity ID - this is the `SP Entity ID` from the Windsurf portal.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e33dc0b9d021309da0fcdb2ac4f08bbb" data-og-width="974" width="974" data-og-height="672" height="672" data-path="assets/auth/pingid-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=085f011d0ddf369d9b05502ccbfbb5dc 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=160eebad525ebc56527d0c9e9945492a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fccab270df675b3608a5e72afdcda1bc 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=dcab45be60955341f5e47e1746fd36f4 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6819f76a0f703860f8f53fc486bf696d 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4d1dde99a6c5a62b6c1798f1c694e220 2500w" />
    </Frame>

    5. Copy the `Issuer ID` from PingID to the `IdP Entity ID` value in the Windsurf portal.

    6. Copy the `Single Signon Service` value from PingID to the `SSO URL` value in the Windsurf portal.

    7. Download the Signing Certificate from PingID as X509 PEM (.crt), open the file and copy its contents to the `X509 Certificate` value in the Windsurf portal.

    **Note**: make sure you have the fill begin and end lines with 5 dashes (-) and no other characters are copied!

    8. In attribute mappings, make sure to map:

    * `saml_subject` - Email Address
    * `firstName` - Given Name
    * `lastName` - Family Name

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4ff17f07bfb897072fb68e212ee2ac12" data-og-width="1398" width="1398" data-og-height="780" height="780" data-path="assets/auth/pingid-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7af2eb21b83c86fa66ab0a93b744a81a 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c817c9e4a5abbe3827baf40050108679 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1f4f584e1f6586dadb0632457eb840f1 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=062bae9cd58477962da4f51fb5590bc4 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=efa1fb0cc4d775c8695521195d31949e 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4fe0ba0d6cd6b3eb6796557696e9a08d 2500w" />
    </Frame>

    9. Add/edit any other policies and access as required by your setup/organization

    10. Enable the SAML login in the Windsurf portal so you can test it.

    **NOTE: DO NOT LOGOUT OR CLOSE THE WINDOW AT THIS POINT.**

    If you get an error or it times out, troubleshoot your settings, otherwise you have to disable your SAML Settings in the Windsurf portal.

    **If you logout or close the window without confirming a successful test - you may get locked out.**

    11. Once your test was successfully completed, you may logout. You can now use SSO sign in when browsing to your team/organization page with the SSO ID you have configured in step 3.

    [https://www.codeium.com/yourssoid/login](https://www.codeium.com/yourssoid/login)
  </Tab>
</Tabs>

---

← Previous: [Role Based Access & Management](./role-based-access-management.md) | [Index](./index.md) | Next: [Getting started with Teams and Enterprise](./getting-started-with-teams-and-enterprise.md) →