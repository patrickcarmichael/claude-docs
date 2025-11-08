---
title: "SSO"
source: "https://docs.cursor.com/en/account/teams/sso"
language: "en"
language_name: "English"
---

# SSO
Source: https://docs.cursor.com/en/account/teams/sso

Set up single sign-on for your team

## Overview

SAML 2.0 SSO is available at no additional cost on Business plans. Use your existing identity provider (IdP) to authenticate team members without separate Cursor accounts.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

## Prerequisites

* Cursor Team plan
* Admin access to your identity provider (e.g., Okta)
* Admin access to your Cursor organization

## Configuration Steps

<Steps>
  <Step title="Sign in to your Cursor account">
    Navigate to [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings) with an admin account.
  </Step>

  <Step title="Locate the SSO configuration">
    Find the "Single Sign-On (SSO)" section and expand it.
  </Step>

  <Step title="Begin the setup process">
    Click the "SSO Provider Connection settings"button to start SSO setup and follow the wizard.
  </Step>

  <Step title="Configure your identity provider">
    In your identity provider (e.g., Okta):

    * Create new SAML application
    * Configure SAML settings using Cursor's information
    * Set up Just-in-Time (JIT) provisioning
  </Step>

  <Step title="Verify domain">
    Verify the domain of your users in Cursor by clicking the "Domain verification settings" button.
  </Step>
</Steps>

### Identity Provider Setup Guides

For provider-specific setup instructions:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Setup instructions for Okta, Azure AD, Google Workspace, and more.
</Card>

## Additional Settings

* Manage SSO enforcement through admin dashboard
* New users auto-enroll when signing in through SSO
* Handle user management through your identity provider

## Troubleshooting

If issues occur:

* Verify domain is verified in Cursor
* Ensure SAML attributes are properly mapped
* Check SSO is enabled in admin dashboard
* Match first and last names between identity provider and Cursor
* Check provider-specific guides above
* Contact [hi@cursor.com](mailto:hi@cursor.com) if issues persist

---

← Previous: [Get Started](./get-started.md) | [Index](./index.md) | Next: [Update Access](./update-access.md) →