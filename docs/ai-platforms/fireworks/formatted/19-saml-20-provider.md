---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SAML 2.0 provider

<Steps>
  <Step title="Create SAML 2.0 application">
    Create a SAML 2.0 application in your identity provider, e.g. [Okta](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm).
  </Step>

  <Step title="Set SSO URL">
    Set the SSO URL to the URL provided by Fireworks. It looks like:
```http
    https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/saml2/idpresponse
```
  </Step>

  <Step title="Configure Audience URI">
    Configure the Audience URI (SP Entity ID) as provided by Fireworks. It looks like:
```
    urn:amazon:cognito:sp:<some-unique-identifier>
```
  </Step>

  <Step title="Create Attribute Statement">
    Create an Attribute Statement with the name:
```http
    http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
```

    and the value `user.email`
  </Step>

  <Step title="Keep default settings">
    Leave the rest of the settings as defaults.
  </Step>

  <Step title="Note down metadata URL">
    Note down the "metadata url" for your newly created application. You will need to provide this to your Fireworks AI representative to complete your account set up.
  </Step>
</Steps>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
