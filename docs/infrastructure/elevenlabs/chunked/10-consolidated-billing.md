**Navigation:** [← Previous](./09-voice-library.md) | [Index](./index.md) | [Next →](./11-build.md)

# Consolidated billing

> Manage multiple workspaces with unified billing and shared credit pools.

<Info>
  Consolidated billing is an Enterprise feature that allows you to link multiple workspaces under a
  single billing account.
</Info>


## Overview

Consolidated billing enables you to manage multiple workspaces across different environments while maintaining a single billing account.
This feature is particularly useful for organizations that need to operate in multiple regions or maintain separate workspaces for different teams while keeping billing centralized.

With consolidated billing, you have:

* **Unified billing** – Receive a single invoice for all linked workspaces.
* **Shared credit pools** – All workspaces share the same credit allocation.
* **Cross-environment support** – Link workspaces from isolated environments (e.g., EU, India) to the US billing workspace.
* **Independent management** – Each workspace maintains its own members, SSO configurations, and settings.


## How it works

Consolidated billing creates a relationship between workspaces where one workspace (the "billing workspace") receives usage reports from other workspaces (the "reporting workspaces"). All usage is then billed through the billing workspace.

### Billing workspace

The billing workspace must be located in the US environment (`elevenlabs.io`). This workspace:

* Receives usage reports from all linked workspaces.
* Issues a single monthly invoice.
* Shows general usage coming from each reporting workspace.

### Reporting workspaces

Reporting workspaces can be located on elevenlabs.io or in an isolated environment. These workspaces:

* Report their usage to the billing workspace.
* Maintain their own members and configurations.
* Show, as usual, granular usage analytics for that workspace.

<Note>
  Within the same region, users cannot be members of multiple workspaces. This limitation only
  applies within the same environment.
</Note>


## Setup process

Consolidated billing is an Enterprise feature that requires configuration by our team. To enable consolidated billing for your organization, contact your dedicated Customer Success Manager.


## Usage tracking

The billing workspace will be able to see the usage of all linked workspaces.

<img src="file:20ddec8b-3f83-4978-a977-017a518a99c3" alt="Consolidated billing reporting view" />

The reporting workspace will only be able to see analytics for its own usage. However, the total credits left shown in the sidebar will be the sum of all linked workspaces.


## FAQ

<AccordionGroup>
  <Accordion title="Can I set credit limits for each workspace?">
    No, all workspaces share the same credit pool. However, you can closely track the usage of each
    workspace.
  </Accordion>

  <Accordion title="Can I have different subscription tiers for different workspaces?">
    No, all workspaces must share the same subscription. The billing workspace determines the
    subscription level for all linked workspaces.
  </Accordion>

  <Accordion title="Can I unlink a workspace from consolidated billing?">
    Yes, you can disable consolidated billing on any reporting workspace. This will require setting
    up a new subscription for that workspace or removing that workspace entirely. To do so, get in
    touch with your dedicated Customer Success Manager.
  </Accordion>

  <Accordion title="Can both workspaces be located on elevenlabs.io?">
    Yes, both workspaces can be located on elevenlabs.io - this is useful if you want to have
    multiple segregated teams. Sharing resources between workspaces is not possible so consider
    using permissions with [user groups](/docs/product-guides/administration/workspaces/user-groups)
    before enabling consolidated billing.
  </Accordion>
</AccordionGroup>



# Data residency

> Store your data in specific jurisdictions with ElevenLabs' isolated environments.

<Info>
  Data residency is an Enterprise feature. For details on enabling this for your organization,
  please see the "Getting Access" section below.
</Info>


## Overview

ElevenLabs offers "data residency" through isolated environments in certain jurisdictions, allowing customers to limit data storage to those locations. As a standard, ElevenLabs' customer data is hosted/stored in the U.S., however ElevenLabs has released additional storage locations in the EU and India.

Depending on the customer's location, isolated environments in a particular region may also provide the benefit of reduced latency.


## Data residency in isolated environments

ElevenLabs offers data residency in certain jurisdictions to allow customers to choose where their data is stored. While storage will take place in the selected location, processing may nevertheless occur outside of the selected location, including by ElevenLabs' international affiliates and subprocessors, for support purposes, and for content moderation purposes. This detail is captured within ElevenLabs' Data Processing Agreement.

In certain locations, configurations may be available to limit processing to the selected residency location. For example, with respect to EU residency, users may restrict processing to the EU by using Zero Retention Mode and the API. In such case, content submitted to the Service will not be processed outside of the EU, provided the use of certain optional integrations (ex. Custom LLMs or post-call webhooks that require out-of-region processing) may result in processing outside of such jurisdiction.


## Existing core compliance features

Isolated environments complement ElevenLabs' existing suite of security and compliance measures designed to safeguard customer data:

**GDPR Compliance**: Our platform and practices are designed to align with applicable GDPR requirements, including measures designed to ensure lawful data processing, adherence to data subject rights, and the implementation of appropriate security measures as required by GDPR.

**SOC2 Certification**: ElevenLabs maintains SOC2 certification, demonstrating our commitment to high standards for security, availability and confidentiality.

**Zero Retention Mode (Optional)**: Customers can enable Zero Retention Mode, ensuring that sensitive content and data processed by our models are not retained on ElevenLabs servers. This is a powerful feature for minimizing data footprint.

**End-to-End Encryption**: Data transmitted to and from ElevenLabs models is protected by end-to-end encryption, securing it in transit.

**HIPAA Compliance**: For qualifying healthcare enterprises, ElevenLabs offers Business Associate Agreements (BAAs), which offer additional protections in relation to its HIPAA-Eligible Services.


## Developer considerations

Isolated environments are completely separate ElevenLabs workspaces, available via a different address on the web. As such, you will need to get access to this feature first to be able to sign in to an isolated environment with data residency.

### EU

* **Web**: [https://eu.residency.elevenlabs.io](https://eu.residency.elevenlabs.io)
* **API**: `https://api.eu.residency.elevenlabs.io`
* **WebSockets**: `wss://api.eu.residency.elevenlabs.io`

### India

* **Web**: [https://in.residency.elevenlabs.io](https://in.residency.elevenlabs.io)
* **API**: `https://api.in.residency.elevenlabs.io`
* **WebSockets**: `wss://api.in.residency.elevenlabs.io`

Your account on the isolated environment will be separate to the one on elevenlabs.io, and your workspace will be blank. This means that when using an isolated environment via API, you will need to hit a different API URL with a different API key.


## Limitations

Currently, ElevenLabs provides limited support for migrating your resources from non-isolated to isolated environments. However, you can enable professional voice clone link sharing from a non-isolated environment and add it to your isolated environment; please refer to the FAQ below for instructions.
Reach out to us if you intend to move instant voice clones. For other resources, such as agents in the Agents Platform, we recommend recreation via the API where possible.

Dubbing is not currently available in isolated environments.

### India

* India has limited availability for the LLMs in the Agents Platform. Currently, we support: GPT 4o,
  GLM-4.5-Air, Qwen3-30B, Qwen3-4B and Custom LLMs. All open source models are hosted by ElevenLabs.
* Twilio doesn't currently offer an India routing region for its calls.


## Getting access

Data residency is an exclusive feature available to ElevenLabs' Enterprise customers.

**Existing Enterprise Customers**: If you are an existing Enterprise customer, please contact [success@elevenlabs.io](mailto:success@elevenlabs.io) to discuss enabling an isolated environment for your account.

**New Customers**: Organizations interested in ElevenLabs Enterprise and requiring an isolated environment should contact [sales@elevenlabs.io](mailto:sales@elevenlabs.io) to discuss specific needs and implementation.


## FAQ

<AccordionGroup>
  <Accordion title="Can I run my isolated environment in parallel with the non-isolated one?">
    Yes, it is possible to do this and to bill the usage for both of them on the same invoice. For
    more details on unified billing across multiple workspaces, see [consolidated
    billing](/docs/product-guides/administration/consolidated-billing).
  </Accordion>

  <Accordion title="How does this relate to GDPR compliance?">
    For customers subject to GDPR, ElevenLabs provides options to limit storage and, in some cases,
    processing to the EU to support customers' compliance efforts.
  </Accordion>

  <Accordion title="Do isolated environments impact API performance?">
    For users inside the isolated environment region, data residency may potentially reduce latency
    due to localized processing. For users outside the isolated environment region, performance is
    expected to remain consistent with our global infrastructure. While there may be benefits as it
    relates to latency, the purpose of these data residency options are not specifically to improve
    latency.
  </Accordion>

  <Accordion title="Is Zero Retention Mode automatically enabled in isolated environments?">
    No, Zero Retention Mode is an optional feature that can be enabled separately, even for accounts
    with data residency. It provides an additional layer of data minimization by preventing storage of
    content on our servers.
  </Accordion>

  <Accordion title="My API requests to the isolated environment are failing">
    Double check that you are using the correct API URL and the correct API key for the account on the
    isolated environment.
  </Accordion>

  <Accordion title="How do I use an isolated environment in the SDK?">
    When you create the ElevenLabs client object, it takes an environment parameter which is by
    default US but you can set it to your desired environment.
  </Accordion>

  <Accordion title="How do I share a PVC from a non-isolated environment to an isolated environment?">
    To share a PVC with an isolated environment, first enable link sharing for that voice. Then copy
    the link, and add the prefix of the isolated environment to the voice link: From:
    `elevenlabs.io/...` → To: `eu.residency.elevenlabs.io/...`
  </Accordion>
</AccordionGroup>



# Usage analytics

> Track your API usage, monitor credit consumption, and analyze account activity

Usage analytics lets you view all the activity on the platform for your account or workspace.

To access usage analytics, click on “My Account” in the bottom left corner and select [Usage Analytics](https://elevenlabs.io/app/usage)

<img src="file:478c5f4e-a2c8-4477-9f56-fd0d332dbe5f" alt="Account and Workspace tabs" />

There are two tabs for usage analytics. On an Enterprise plan, the account tab shows data for your individual account, whereas the workspace tab covers all accounts under your workspace.

If you're not on an Enterprise plan, the data will be the same for your account and your workspace, but some information will only be available in your workspace tab, such as your Voice Add/Edit Operations quota.


## Credit usage

In the Credit Usage section, you can filter your usage data in a number of different ways.

In the account tab, you can break your usage down by voice, product or API key, for example.

In the workspace you have additional options allowing you to break usage down by individual user or workspace group.

You can view the data by day, week, month or cumulatively. If you want to be more specific, you can use filters to show only your usage for specific voices, products or API keys.

This feature is quite powerful, allowing you to gain great insights into your usage or understand your customers' usage if you've implemented us in your product.

<img src="file:d4b70598-ac6d-4c60-b163-7c16edce63a1" alt="Credit use broken down by voice" />


## API requests

In the API Requests section, you'll find not only the total number of requests made within a specific timeframe but also the number of concurrent requests during that period.

You can view data by different time periods, for example, hour, day, month and year, and at different levels of granularity.

<img src="file:840dc58b-f8e5-40fb-be8e-456dfb4b8aa1" alt="Workspace API calls" />


## Export data

You also have the option to export your usage data as a CSV file. To do this, just click the "Export as CSV" button, and the data from your current view will be exported and downloaded.

<img src="file:1cf94472-4e78-48fb-8ef8-a99c78a81097" alt="Export your usage data as CSV" />



# Workspaces

> An overview on how teams can collaborate in a shared Workspace.

<img src="file:14907711-ca95-484b-8169-169dc70e6a79" alt="Workspaces" />

<Info>
  Workspaces are currently only available for Scale, Business and Enterprise customers.
</Info>


## Overview

For teams that want to collaborate in ElevenLabs, we offer shared Workspaces. Workspaces offer the following benefits:

* **Shared billing** - Rather than having each of your team members individually create & manage subscriptions, all of your team’s character usage and billing is centralized under one Workspace.
* **Shared resources** - Within a Workspace, your team can share: voices, studio instances, ElevenLabs agents, dubbings and more.
* **Access management** - Your Workspace admin can easily add and remove team members.
* **API Key management** - You can issue and revoke unlimited API keys for your team.


## FAQ

<AccordionGroup>
  <Accordion title="How do I create a Workspace?">
    ### Creating a Workspace

    Workspaces are automatically enabled on all accounts with Scale, Business and Enterprise subscriptions. On the Scale and Business plans, the account owner will be the Workspace admin by default. They will have the power to add more team members as well as nominate others to be an admin. When setting up your Enterprise account, you’ll be asked to nominate a Workspace admin.
  </Accordion>

  <Accordion title="How do I add a team member to a Workspace?">
    ### Adding a team member to a Workspace

    <Info>
      Only administrators can add and remove team members.
    </Info>

    <Frame>
      <img src="file:e8d5fe0a-dd06-4e87-8d4c-4e3637c0baf2" alt="Workspace domain verification" />
    </Frame>

    Once you are logged in, select your profile in the bottom left of the dashboard and choose **Workspace settings** and then navigate to the **Members** tab. From there you'll be able to add team members, assign roles and remove members from the Workspace.

    #### Bulk Invites

    Enterprise customers can invite their users in bulk once their domain has been verified following the [Verify Domain step](/docs/product-guides/administration/workspaces/sso#verify-your-email-domain) from the SSO configuration process.

    #### User Auto Provisioning

    Enterprise customers can enable user auto provisioning via the **Security & SSO** tab in workspace settings. When this is enabled, new users with an email domain matching one of your verified domains will automatically join your workspace and take up a seat.
  </Accordion>

  <Accordion title="What roles can I assign members?">
    ### Roles

    There are two roles, Admins and Members. Members have full access to your Workspace and can generate an unlimited number of characters (within your current overall plan’s limit).

    Admins have all of the access of Members, with the added ability to add/remove teammates and permissions to manage your subscription.
  </Accordion>

  <Accordion title="How do I manage billing?">
    ### Managing Billing

    <Info>
      Only admins can manage billing.
    </Info>

    To manage your billing, select your profile in the bottom left of the dashboard and choose **Subscription**. From there, you’ll be able to update your payment information and access past invoices.
  </Accordion>

  <Accordion title="How do I manage Service Accounts / API keys?">
    ### Managing Service Accounts

    To manage Service Accounts, select your profile in the bottom left of the dashboard and choose **Workspace settings**. Navigate to the **Service Accounts** tab and you’ll be able to create / delete service accounts as well as issue new API keys for those service accounts.

    <Note>
      "Workspace API keys" were formerly a type of Service Account with a single API key.
    </Note>
  </Accordion>

  <Accordion title="Who is the Workspace owner?">
    ### Managing the Workspace owner

    Each Workspace can have one owner. By default, this will be the account owner for Scale and Business subscriptions. Ownership can be transferred to another account.

    If you downgrade your subscription and exceed the available number of seats on your new plan, all users apart from the owner will be locked out. The admin can also lock users in advance of the downgrade.
  </Accordion>
</AccordionGroup>



# Service Accounts and API Keys

> An overview on how to configure Service Accounts and API keys for your workspace

<img src="file:4b2c178c-433b-4179-9334-3b10765dfd29" alt="Service Accounts" />


## Overview

<Info>
  Service Accounts are currently only available for multi-seat customers, and only Workspace admins
  can use this feature. To upgrade, [get in touch with our sales
  team](https://elevenlabs.io/contact-sales).
</Info>

Service Accounts and their respective API keys allow access to workspace resources without relying on an individual's access to ElevenLabs.


## Service Accounts

A service account acts as a workspace member. When originally created, they do not have access to any resources.

The service account can be granted access to resources by either adding the service account to a group or directly sharing resources with the service account.
It is recommended to add them to a group so that future users can be added to the same group and have the same permissions.


## Rotating API keys

<Info>
  When creating a new API key to replace one that you are rotating out, make sure to create the API
  key for the same service account and copy the API key permissions from the old API key to ensure
  that no access is lost.
</Info>

API keys can either be rotated via the UI or via the API.

To rotate API keys on the web, click on your profile icon located at the bottom left of the dashboard, select **Workspace settings**, and then navigate to the **Service Accounts** tab.
From there, you can create a new API key for the same service account. Once you've switched to using the new API key, you can delete the old one from this tab.

To rotate API keys via the API, please see the API reference underneath **Service Accounts** for the relevant endpoints.



# Single Sign-On (SSO)

> An overview on how to set up SSO for your Workspace.

<img src="file:06b0f289-dd19-40d5-beda-a5703bbe6973" alt="SSO" />


## Overview

<Info>
  SSO is currently only available for Enterprise customers, and only Workspace admins can use this
  feature. To upgrade, [get in touch with our sales team](https://elevenlabs.io/contact-sales).
</Info>

Single Sign-On (SSO) allows your team to log in to ElevenLabs by using your existing identity provider. This allows your team to use the same credentials they use for other services to log in to ElevenLabs.


## Guide

<Steps>
  <Step title="Access your SSO settings">
    Click on your profile icon located at the bottom left of the dashboard, select **Workspace settings**, and then navigate to the **Security & SSO** tab.
  </Step>

  <Step title="Choose identity providers">
    You can choose from a variety of pre-configured identity providers, including Google, Apple, GitHub, etc. Custom organization SSO providers will only appear in this list after they have been configured, as shown in the "SSO Provider" section.
  </Step>

  <Step title="Verify your email domain">
    Next, you need to verify your email domain for authentication. This lets ElevenLabs know that you own the domain you are configuring for SSO. This is a security measure to prevent unauthorized access to your Workspace.

    Click the **Verify domain** button and enter the domain name you want to verify. After completing this step, click on the domain pending verification. You will be prompted to add a DNS TXT record to your domain's DNS settings. Once the DNS record has been added, click on the **Verify** button.
  </Step>

  <Step title="Configure SSO">
    If you want to configure your own SSO provider, select the SSO provider dropdown to select between OIDC (OpenID Connect) and SAML (Security Assertion Markup Language).

    <Info>
      Only Service Provider (SP) initiated SSO is supported for SAML. To ease the sign in process, you can create a bookmark app in your SSO provider linking to 

      [https://elevenlabs.io/app/sign-in?use_sso=true](https://elevenlabs.io/app/sign-in?use_sso=true)

      . You can include the user's email as an additional query parameter to pre-fill the field. For example 

      [https://elevenlabs.io/app/sign-in?use_sso=true&email=test@test.com](https://elevenlabs.io/app/sign-in?use_sso=true&email=test@test.com)
    </Info>

    Once you've filled out the required fields, click the **Update SSO** button to save your changes.

    <Warning>
      Configuring a new SSO provider will log out all Workspace members currently logged in with SSO.
    </Warning>
  </Step>
</Steps>


## FAQ

<AccordionGroup>
  <Accordion title="Microsoft Entra Identifier / Azure AD - SAML">
    What shall I fill for Identifier (Entity ID)?

    * Use Service Provider Entity Id

    What shall I fill for Reply URL (Assertion Consumer Service) URL in SAML?

    * Use Redirect URL

    What is ACS URL?

    * Same as Assertion Consumer Service URL

    Which fields should I use to provide ElevenLabs?

    * Use *Microsoft Entra Identifier* for IdP Entity ID
    * Use *Login URL* for IdP Sign-In URL
  </Accordion>

  <Accordion title="Okta - SAML">
    **What to fill in on the Okta side**:

    * **Audience Restriction**: This is the Service Provider Entity ID from the ElevenLabs SSO configuration page.
    * **Single Sign-On URL/Recipient URL/Destination**: This is the Redirect URL from the ElevenLabs SSO configuration page.

    **What to fill in on the ElevenLabs side**:

    * Create the application in Okta and then fill out these fields using the results
    * **Identity Provider Entity Id**: Use the SAML Issuer ID
    * **Identity Provider Sign-In URL**: Use the Sign On URL from Okta
      * This can generally be found in the Metadata details within the Sign On tab of the Okta application
      * It will end in **/sso/saml**
  </Accordion>

  <Accordion title="OneLogin - SAML">
    * Please fill Recipient field with the value of Redirect URL.
  </Accordion>

  <Accordion title="OIDC - Common Errors">
    Please ensure that `email` and `email_verified` are included in the custom attributes returned in the OIDC response. Without these, the following errors may be hit:

    * *No email address was received*: Fixed by adding **email** to the response.
    * *Account exists with different credentials*: Fixed by adding **email\_verified** to the response
  </Accordion>

  <Accordion title="I am getting the error 'Unable to login with saml.workspace...'">
    * One known error: Inside the `<saml:Subject>` field of the SAML response, make sure `<saml:NameID>` is set to the email address of the user.
  </Accordion>
</AccordionGroup>



# Sharing resources

> An overview on how to share resources within a Workspace.

<img src="file:15b78e59-97b4-4213-b6c6-a25758becc39" alt="Sharing a project" />


## Overview

If your subscription plan includes multiple seats, you can share resources with your members. Resources you
can share include: voices, ElevenLabs agents, studio projects and more. Check the
[Workspaces API](/docs/api-reference/workspace/share-workspace-resource) for an up-to-date list of resources you can share.


## Sharing

You can share a **resource** with a **principal**. A principal is one of the following:

* A user
* A user group
* A service account

A resource can be shared with at most 100 principals.

Service Accounts behave like individual users. They don't have access to anything in the Workspace when they are created, but they can be added to resources by resource admins.

#### Default Sharing

If you would like to share with specific principals for each new resource by default, this can be enabled in your personal settings page under **Default Sharing Preferences**.
Every new resource created after this is enabled will be automatically shared with the principals that you add here.


## Roles

When you share a resource with a principal, you can assign them a **role**. We support the following roles:

* **Viewer**: Viewers can discover the resource and its contents. They can also "use" the resource, e.g., generate TTS with a voice or listen to the audio of a studio instance.
* **Editor**: Everything a viewer can do, plus they can also edit the contents of the resource.
* **Admin**: Everything an editor can do, plus they can also delete the resource and manage sharing permissions.

When you create a resource, you have admin permissions on it. Other resource admins cannot remove your admin permissions on the resources you created.

<Warning>
  Workspace admins have admin permissions on all resources in the workspace. This can be removed
  from them only by removing their Workspace admin role.
</Warning>



# User groups

> An overview on how to create and manage user groups.

<img src="file:c1c2a483-451a-4176-92d2-f52e1ee2b466" alt="Group Management" />


## Overview

<Info>
   Only Workspace admins can create, edit, and delete user groups. 
</Info>

User groups allow you to manage permissions for multiple users at once.


## Creating a user group

You can create a user group from **Workspace settings**. You can then [share resources](/docs/product-guides/administration/workspaces/sharing-resources) with the group directly.
If access to a user group is lost, access to resources shared with that group is also lost.


## Multiple groups

User groups cannot be nested, but you can add users to multiple groups. If a user is part of multiple groups, they will have the union of all the permissions of the groups they are part of.

For example, you can create a voice and grant the **Sales** and **Marketing** groups viewer and editor roles on the voice, respectively.
If a user is part of both groups, they will have editor permissions on the voice. Losing access to the **Marketing** group will downgrade the user's permissions to viewer.


## Disabling platform features

Permissions for groups can be revoked for specific product features, such as Professional Voice Cloning or Sound Effects.
To do this, you first have to remove the relevant permissions from the **Everyone** group. Afterwards, enable the permissions for each group that should have access.



# Webhooks

> Enable external integrations by receiving webhook events.


## Overview

Certain events within ElevenLabs can be configured to trigger webhooks, allowing external applications and systems to receive and process these events as they occur. Currently supported event types include:

| Event type                       | Description                                                  |
| -------------------------------- | ------------------------------------------------------------ |
| `post_call_transcription`        | A Agents Platform call has finished and analysis is complete |
| `voice_removal_notice`           | A shared voice is scheduled to be removed                    |
| `voice_removal_notice_withdrawn` | A shared voice is no longer scheduled for removal            |
| `voice_removed`                  | A shared voice has been removed and is no longer useable     |


## Configuration

Webhooks can be created, disabled and deleted from the general settings page. For users within [Workspaces](/docs/product-guides/administration/workspaces/overview), only the workspace admins can configure the webhooks for the workspace.

<Frame background="subtle">
  ![HMAC webhook configuration](file:f526667a-a219-411e-9eb5-8f5157c92a50)
</Frame>

After creation, the webhook can be selected to listen for events within product settings such as [Agents Platform](/docs/agents-platform/workflows/post-call-webhooks).

Webhooks can be disabled from the general settings page at any time. Webhooks that repeatedly fail are auto disabled if there are 10 or more consecutive failures and the last successful delivery was more than 7 days ago or has never been successfully delivered. Auto-disabled webhooks require re-enabling from the settings page. Webhooks can be deleted if not in use by any products.


## Integration

To integrate with webhooks, the listener should create an endpoint handler to receive the webhook event data POST requests. After validating the signature, the handler should quickly return HTTP 200 to indicate successful receipt of the webhook event, repeat failure to correctly return may result in the webhook becoming automatically disabled.
Each webhook event is dispatched only once, refer to the [API](/docs/api-reference/introduction) for methods to poll and get product specific data.

### Top-level fields

| Field             | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| `type`            | string | Type of event            |
| `data`            | object | Data for the event       |
| `event_timestamp` | string | When this event occurred |


## Example webhook payload

```json
{
  "type": "post_call_transcription",
  "event_timestamp": 1739537297,
  "data": {
    "agent_id": "xyz",
    "conversation_id": "abc",
    "status": "done",
    "transcript": [
      {
        "role": "agent",
        "message": "Hey there angelo. How are you?",
        "tool_calls": null,
        "tool_results": null,
        "feedback": null,
        "time_in_call_secs": 0,
        "conversation_turn_metrics": null
      },
      {
        "role": "user",
        "message": "Hey, can you tell me, like, a fun fact about 11 Labs?",
        "tool_calls": null,
        "tool_results": null,
        "feedback": null,
        "time_in_call_secs": 2,
        "conversation_turn_metrics": null
      },
      {
        "role": "agent",
        "message": "I do not have access to fun facts about Eleven Labs. However, I can share some general information about the company. Eleven Labs is an AI voice technology platform that specializes in voice cloning and text-to-speech...",
        "tool_calls": null,
        "tool_results": null,
        "feedback": null,
        "time_in_call_secs": 9,
        "conversation_turn_metrics": {
          "convai_llm_service_ttfb": {
            "elapsed_time": 0.3704247010173276
          },
          "convai_llm_service_ttf_sentence": {
            "elapsed_time": 0.5551181449554861
          }
        }
      }
    ],
    "metadata": {
      "start_time_unix_secs": 1739537297,
      "call_duration_secs": 22,
      "cost": 296,
      "deletion_settings": {
        "deletion_time_unix_secs": 1802609320,
        "deleted_logs_at_time_unix_secs": null,
        "deleted_audio_at_time_unix_secs": null,
        "deleted_transcript_at_time_unix_secs": null,
        "delete_transcript_and_pii": true,
        "delete_audio": true
      },
      "feedback": {
        "overall_score": null,
        "likes": 0,
        "dislikes": 0
      },
      "authorization_method": "authorization_header",
      "charging": {
        "dev_discount": true
      },
      "termination_reason": ""
    },
    "analysis": {
      "evaluation_criteria_results": {},
      "data_collection_results": {},
      "call_successful": "success",
      "transcript_summary": "The conversation begins with the agent asking how Angelo is, but Angelo redirects the conversation by requesting a fun fact about 11 Labs. The agent acknowledges they don't have specific fun facts about Eleven Labs but offers to provide general information about the company. They briefly describe Eleven Labs as an AI voice technology platform specializing in voice cloning and text-to-speech technology. The conversation is brief and informational, with the agent adapting to the user's request despite not having the exact information asked for."
    },
    "conversation_initiation_client_data": {
      "conversation_config_override": {
        "agent": {
          "prompt": null,
          "first_message": null,
          "language": "en"
        },
        "tts": {
          "voice_id": null
        }
      },
      "custom_llm_extra_body": {},
      "dynamic_variables": {
        "user_name": "angelo"
      }
    }
  }
}
```


## Authentication

It is important for the listener to validate all incoming webhooks. Webhooks currently support authentication via HMAC signatures. Set up HMAC authentication by:

* Securely storing the shared secret generated upon creation of the webhook
* Verifying the ElevenLabs-Signature header in your endpoint using the shared secret

The ElevenLabs-Signature takes the following format:

```json
t=timestamp,v0=hash
```

The hash is equivalent to the hex encoded sha256 HMAC signature of `timestamp.request_body`. Both the hash and timestamp should be validated, an example is shown here:

<Tabs>
  <Tab title="Python">
    Example python webhook handler using FastAPI:

    ```python
    from fastapi import FastAPI, Request
    import time
    import hmac
    from hashlib import sha256

    app = FastAPI()

    # Example webhook handler
    @app.post("/webhook")
    async def receive_message(request: Request):
        payload = await request.body()
        headers = request.headers.get("elevenlabs-signature")
        if headers is None:
            return
        timestamp = headers.split(",")[0][2:]
        hmac_signature = headers.split(",")[1]

        # Validate timestamp
        tolerance = int(time.time()) - 30 * 60
        if int(timestamp) < tolerance
            return

        # Validate signature
        full_payload_to_sign = f"{timestamp}.{payload.decode('utf-8')}"
        mac = hmac.new(
            key=secret.encode("utf-8"),
            msg=full_payload_to_sign.encode("utf-8"),
            digestmod=sha256,
        )
        digest = 'v0=' + mac.hexdigest()
        if hmac_signature != digest:
            return

        # Continue processing

        return {"status": "received"}
    ```
  </Tab>

  <Tab title="JavaScript">
    <Tabs>
      <Tab title="Express">
        Example javascript webhook handler using node express framework:

        ```javascript
        const crypto = require('crypto');
        const secret = process.env.WEBHOOK_SECRET;
        const bodyParser = require('body-parser');

        // Ensure express js is parsing the raw body through instead of applying it's own encoding
        app.use(bodyParser.raw({ type: '*/*' }));

        // Example webhook handler
        app.post('/webhook/elevenlabs', async (req, res) => {
          const headers = req.headers['ElevenLabs-Signature'].split(',');
          const timestamp = headers.find((e) => e.startsWith('t=')).substring(2);
          const signature = headers.find((e) => e.startsWith('v0='));

          // Validate timestamp
          const reqTimestamp = timestamp * 1000;
          const tolerance = Date.now() - 30 * 60 * 1000;
          if (reqTimestamp < tolerance) {
            res.status(403).send('Request expired');
            return;
          } else {
            // Validate hash
            const message = `${timestamp}.${req.body}`;
            const digest = 'v0=' + crypto.createHmac('sha256', secret).update(message).digest('hex');
            if (signature !== digest) {
              res.status(401).send('Request unauthorized');
              return;
            }
          }

          // Validation passed, continue processing ...

          res.status(200).send();
        });
        ```
      </Tab>

      <Tab title="Next.js">
        Example javascript webhook handler using Next.js API route:

        ```javascript app/api/convai-webhook/route.js
        import { NextResponse } from "next/server";
        import type { NextRequest } from "next/server";
        import crypto from "crypto";

        export async function GET() {
          return NextResponse.json({ status: "webhook listening" }, { status: 200 });
        }

        export async function POST(req: NextRequest) {
          const secret = process.env.ELEVENLABS_CONVAI_WEBHOOK_SECRET; // Add this to your env variables
          const { event, error } = await constructWebhookEvent(req, secret);
          if (error) {
            return NextResponse.json({ error: error }, { status: 401 });
          }

          if (event.type === "post_call_transcription") {
            console.log("event data", JSON.stringify(event.data, null, 2));
          }

          return NextResponse.json({ received: true }, { status: 200 });
        }

        const constructWebhookEvent = async (req: NextRequest, secret?: string) => {
          const body = await req.text();
          const signature_header = req.headers.get("ElevenLabs-Signature");
          console.log(signature_header);

          if (!signature_header) {
            return { event: null, error: "Missing signature header" };
          }

          const headers = signature_header.split(",");
          const timestamp = headers.find((e) => e.startsWith("t="))?.substring(2);
          const signature = headers.find((e) => e.startsWith("v0="));

          if (!timestamp || !signature) {
            return { event: null, error: "Invalid signature format" };
          }

          // Validate timestamp
          const reqTimestamp = Number(timestamp) * 1000;
          const tolerance = Date.now() - 30 * 60 * 1000;
          if (reqTimestamp < tolerance) {
            return { event: null, error: "Request expired" };
          }

          // Validate hash
          const message = `${timestamp}.${body}`;

          if (!secret) {
            return { event: null, error: "Webhook secret not configured" };
          }

          const digest =
            "v0=" + crypto.createHmac("sha256", secret).update(message).digest("hex");
          console.log({ digest, signature });
          if (signature !== digest) {
            return { event: null, error: "Invalid signature" };
          }

          const event = JSON.parse(body);
          return { event, error: null };
        };
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>



# Private deployment

> Deploy ElevenLabs Text to Speech models in your private cloud infrastructure for maximum security and control.


## Get Started

<Info>
  Private deployment documentation and technical resources are available to authorized enterprise
  customers.
</Info>

ElevenLabs is able to deploy its models through the AWS Marketplace and Amazon SageMaker, allowing enterprise customers to run Text to Speech models within their own secure cloud infrastructure.

<CardGroup cols={2}>
  <Card title="State-of-the-art models" icon="duotone waveform-lines">
    Access to ElevenLabs' v2 and v2.5 TTS models
  </Card>

  <Card title="Complete data control" icon="duotone database">
    All text and audio data remains within your infrastructure
  </Card>

  <Card title="Enhanced security" icon="duotone shield-check">
    Meet strict compliance and data residency requirements
  </Card>

  <Card title="Enterprise support" icon="duotone headset">
    Dedicated engineering support and guidance for your deployment
  </Card>
</CardGroup>

To learn more about private deployment options and get access to the technical documentation, contact your ElevenLabs account team or [reach out to our sales team](https://elevenlabs.io/contact-sales).



# Productions

> Human-edited transcripts, subtitles, dubs and audiobooks at scale.


## Overview

Productions is a service that lets you order human-edited transcripts, subtitles, dubs, and audiobooks directly on the ElevenLabs platform. A team of expert linguists and localization professionals vetted and trained by ElevenLabs works on your content and delivers you polished final assets.

<Frame>
  ![Productions Get Human Review Option](file:f135a835-1e24-485d-a859-5275d22fddb1)
</Frame>


## Why use Productions?

* <b>Quality at scale</b>: Your audience cares – let native speakers ensure your multilingual
  content looks, sounds, and feels natural.
* <b>Speed and cost</b>: 5-10x cheaper than traditional LSP services and ready in days vs. weeks or
  months.
* <b>Ease of use</b>: No more email chains or procurement threads – get your content polished and
  ready for your audiences in just a few clicks.


## Services

Click the cards below to learn more about our different Productions services:

<CardGroup cols={2}>
  <Card title="Transcripts" icon="duotone pen-clip" href="/docs/services/productions/transcripts">
    Reviewed by native speakers for maximum accuracy
  </Card>

  <Card title="Subtitles" icon="duotone subtitles" href="/docs/services/productions/subtitles">
    Adapted to formatting and accessibility requirements
  </Card>

  <Card title="Dubbing" icon="duotone microphone" href="/docs/services/productions/dubbing">
    Script translation and audio generation by localization professionals
  </Card>

  <Card title="Audiobooks (coming soon)" icon="duotone book">
    Support for single and multi-speaker voice casting
  </Card>
</CardGroup>


## How it works

<Steps>
  <Step title="Upload new files or select existing files">
    **Ordering a new asset**: head to the [Productions](https://elevenlabs.io/app/productions) page of your ElevenLabs account and create a new order. You may also see a *Productions* option when using the order dialog for other products like [Speech to Text](https://elevenlabs.io/app/speech-to-text) or [Dubbing](https://elevenlabs.io/app/dubbing)

    <Frame background="subtle">
      <img src="file:457a0631-e170-409c-b3a1-0e9b6b7a3477" alt="Productions STT Dialog" />
    </Frame>

    **Starting from an existing asset**: you can also order human-edited versions of existing assets in your ElevenLabs account. Look for the 'Get human review' button in the top right of the editor view for this option.

    <Frame background="subtle">
      ![Productions Get Human Review Option](file:064bd387-3008-4a61-b927-2657736b943a)
    </Frame>
  </Step>

  <Step title="Review and confirm quote">
    Once you upload a file, select a language, and choose your style guide options, you'll see a quote with an **estimated** price for the settings you've chosen.

    When you click *Continue*, the file will be analyzed and the final price will be returned.

    <Frame background="subtle">
      ![Productions quote](file:82fd9b8b-afce-4d83-865e-75417b5e512c)
    </Frame>

    <Info>
      You may see an error message that there is no capacity available for the language you're interested in. If this happens, please check back later! Productions is a new service, and additional capacity will be added as it scales up.
    </Info>
  </Step>

  <Step title="Complete checkout">
    After reviewing the final quote, click *Checkout* and follow the dialog instructions to complete your payment.

    <Info>
      Enterprise orders are deducted from workspace credits instead of going through our payment processor. If you have any questions or run into access issues, please contact your workspace admin or reach out to us at 

      [productions@elevenlabs.io](mailto:productions@elevenlabs.io)

      .
    </Info>
  </Step>

  <Step title="Track your order progress">
    Head to the [Productions](https://elevenlabs.io/app/productions) page of your ElevenLabs account and click any order to open a side panel with more details.

    You'll also receive an email when your order is ready.

    <Frame background="subtle">
      ![Sidebar](file:fcc0c190-0e31-4e50-a050-4a4952ead357)
    </Frame>
  </Step>

  <Step title="View and download your completed assets and invoices">
    Open a completed Production and click the *View* button to open a read only copy. You can also download an invoice for your order by clicking the link next to *Details*.

    To export your completed assets, use the export menu in the sidebar or inside the read only copy.

    <Frame background="subtle">
      ![Export menu](file:b0b8b538-750b-406c-a328-802f7c739b2c)
    </Frame>
  </Step>

  <Step title="Organize your assets into folders">
    Productions has a folder system to help you organize your assets. Click *New folder* to create a new folder. Click *Manage* and use the *Move to Folder* option in the toolbar to nest folders inside other folders.

    <Frame background="subtle">
      ![Folders](file:4c1d5fcc-f218-4451-bc4a-b68cacdd9855)
    </Frame>
  </Step>
</Steps>


## Enterprise

We offer a white glove service to enterprise customers that can make volume commitments, including:

* Discounted per minute rates on each of our services
* Expedited turnaround times
* Advanced pre and post-processing services

Email us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io) or [contact sales](https://elevenlabs.io/contact-sales) to learn more.


## FAQ

<AccordionGroup>
  <Accordion title="How much does it cost?">
    All Productions prices are presented to you in USD (\$) per minute of source audio. Exact prices depend on the type of asset you want to order (transcript, subtitles, dub, etc.), the source and target languages, and any custom style guide options you choose.

    We **always** show you up front how much a Production will cost before asking you to confirm and complete a checkout process.
  </Accordion>

  <Accordion title="What languages do you support?">
    We currently support the following languages for Productions jobs, both source and target:

    * Arabic
    * English
    * French
    * German
    * Hindi
    * Italian
    * Portuguese
    * Russian
    * Spanish
    * Turkish
    * Ukrainian

    We're working hard to expand our language coverage quickly and will update this list as new languages become available.
  </Accordion>

  <Accordion title="What if I'm not happy with the result?">
    You can leave feedback on a completed production by opening it (use the *View* option in the sidebar) and clicking the *Feedback* button.
  </Accordion>

  <Accordion title="Can I make changes once I receive the final version?">
    No. You can export a completed Production and make changes off platform. We plan to add support for this soon.
  </Accordion>

  <Accordion title="Are Productions jobs really done by humans?">
    Yes, Productions is powered by a network of expert linguists and localization professionals
    vetted and trained by ElevenLabs.

    If you'd like to join our Producer network, please check the Productions openings on our [Careers page](https://elevenlabs.io/careers)
  </Accordion>

  <Accordion title="I have specific requirements I'd like to discuss – is that possible?">
    Yes, please contact us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io).
  </Accordion>
</AccordionGroup>



# Transcripts

> Human-edited transcripts from ElevenLabs Productions


## General

Transcripts ordered from Productions are reviewed and corrected by native speakers for maximum accuracy.
We offer 2 types of human transcripts:

| **Option**                 | **When to use it**                          | **Description**                                                                                                                                               |
| -------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Non‑verbatim (”clean”)** | Podcasts, webinars, marketing, personal use | Removes filler words, stutters, audio event tags for smoother reading. Focuses on transcribing the core meaning. Most suitable for the majority of use-cases. |
| **Verbatim**               | Legal, research                             | Attempts to capture *exactly* what is said, including all filler words, stutters and audio event tags.                                                        |

* For a more detailed breakdown of non-verbatim vs. verbatim transcription options, please see the [**Style guides**](#style-guides) section below.
* For more information about other Productions services, please see the [Overview](/docs/services/productions/overview) page.


## How it works

<Steps>
  <Step title="Order transcript">
    <AccordionGroup>
      <Accordion title="Transcribing new files">
        ### Productions page

        The easiest way to order a new transcript from Productions is from the [Productions](https://elevenlabs.io/app/productions) page in your ElevenLabs account.

        <Frame background="subtle">
          <img src="file:f135a835-1e24-485d-a859-5275d22fddb1" alt="Productions Home" />
        </Frame>

        ### Speech to Text Order Dialog

        You can also select the *Human Transcript* option in the [Speech to Text](/docs/capabilities/speech-to-text) order dialog.

        <Frame background="subtle">
          <img src="file:457a0631-e170-409c-b3a1-0e9b6b7a3477" alt="Productions STT Dialog" />
        </Frame>
      </Accordion>

      <Accordion title="Starting from an existing transcript">
        Open an existing transcript and click the *Get human review* button to create a new Productions order for that transcript.

        <Frame background="subtle">
          <img src="file:064bd387-3008-4a61-b927-2657736b943a" alt="Productions Get Human Review" />
        </Frame>
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Export transcript">
    You will receive an email notification when your transcript is ready and see it marked as 'Done' on your Productions page.

    <AccordionGroup>
      <Accordion title="Quick export">
        Open a transcript on your [Productions](https://elevenlabs.io/app/productions) page and click the three dots, then the *Export* button.

        <Frame background="subtle">
          ![Export menu](file:b0b8b538-750b-406c-a328-802f7c739b2c)
        </Frame>
      </Accordion>

      <Accordion title="Export from viewer">
        Open a transcript on your [Productions](https://elevenlabs.io/app/productions) page and click the *View* icon to open the transcript viewer.

        <Frame background="subtle">
          ![Viewer export menu](file:3bed3298-d367-4d94-80ac-a55c6b4fbd19)
        </Frame>
      </Accordion>
    </AccordionGroup>
  </Step>
</Steps>


## Pricing

All prices are in USD (\$) and per minute of source audio.

<div>
  | **Language**        | **Non-verbatim (per minute)** | **Verbatim** (per minute) |
  | ------------------- | :---------------------------: | :-----------------------: |
  | Arabic              |             \$3.00            |           \$3.90          |
  | English             |             \$2.00            |           \$2.60          |
  | French              |             \$2.75            |           \$3.60          |
  | German              |             \$3.30            |           \$4.30          |
  | Hindi               |             \$2.20            |           \$2.90          |
  | Italian             |             \$3.00            |           \$3.90          |
  | Portuguese (Brazil) |             \$2.75            |           \$3.60          |
  | Russian             |             \$3.50            |           \$4.60          |
  | Spanish             |             \$2.00            |           \$2.60          |
  | Turkish             |             \$3.30            |           \$4.30          |
  | Ukrainian           |             \$3.00            |           \$3.90          |
</div>

<Warning>
  Prices are subject to change. You will always see the final price for an order during the checkout
  process.
</Warning>


## SLAs / Delivery Time

We aim to deliver all transcripts **within 48 hours.** If you are an enterprise interested in achieving quicker turnaround times, please contact us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io).


## Style guides

When ordering a Productions transcript, you will see the option to activate 'Verbatim' mode for an extra 30% fee. Please read the breakdown below for more information about this option.

<Frame background="subtle">
  <img src="file:5c84d967-4292-438b-a3d5-d359b4d6659d" alt="Productions Style Guide" />
</Frame>

<AccordionGroup>
  <Accordion title="Non-verbatim">
    Non-verbatim transcription, also called *clean* or *intelligent verbatim*, focuses on clarity and readability. Unlike verbatim transcriptions, it removes unnecessary elements like filler words, stutters, and irrelevant sounds while preserving the speaker’s message.

    <Info>
      This is the default option for Productions transcriptions. Unless you explicitly select 'Verbatim' mode, we will deliver a non-verbatim transcript.
    </Info>

    What gets left out in non-verbatim transcripts:

    * **Filler words and verbal tics** like “um,” “like,” “you know,” or “I mean”
    * **Repetitions** including intentional and unintentional (e.g. stuttering)
    * **Audio event tags,** including non-verbal sounds like \[coughing] or \[throat clearing] as well as environmental sounds like \[dog barking]
    * **Slang or incorrect grammar** (e.g. ‘ain’t’ → ‘is not’)
  </Accordion>

  <Accordion title="Verbatim">
    In verbatim transcription, the goal is to capture ***everything that can be heard,***, meaning:

    * All detailed verbal elements: stutters, repetitions, etc
    * All non-verbal elements like human sounds (\[cough]) and environmental sounds (\[dog barking])
  </Accordion>

  <Accordion title="Non-verbatim vs. verbatim">
    The following table provides a comprehensive breakdown of our non-verbatim vs. verbatim transcription services.

    | **Feature**                 | **Verbatim Transcription**                                                                  | **Verbatim Example**                                         | **Non-Verbatim (Clean) Transcription**                                                                                                                                                                                                                                  | **Non-Verbatim Example**                                                           |
    | --------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
    | **Filler words**            | All filler words are included exactly as spoken.                                            | "So, um, I was like, you know, maybe we should wait."        | Filler words like "um," "like," "you know" are removed.                                                                                                                                                                                                                 | "I was thinking maybe we should wait."                                             |
    | **Stutters**                | Stutters and repeated syllables are transcribed with hyphens.                               | "I-I-I don't know what to say."                              | Stutters are removed for smoother reading.                                                                                                                                                                                                                              | "I don't know what to say."                                                        |
    | **Repetitions**             | Repeated words are retained even when unintentional.                                        | "She, she, she told me not to come."                         | Unintentional repetitions are removed.                                                                                                                                                                                                                                  | "She told me not to come."                                                         |
    | **False Starts**            | False starts are included using double hyphens.                                             | "I was going to—no, actually—let's wait."                    | False starts are removed unless they show meaningful hesitation.                                                                                                                                                                                                        | "Let's wait."                                                                      |
    | **Interruptions**           | Speaker interruptions are marked with a single hyphen.                                      | Speaker 1: "Did you see—" Speaker 2: "Yes, I did."           | Interruptions are simplified or smoothed.                                                                                                                                                                                                                               | Speaker 1: "Did you see it?" Speaker 2: "Yes, I did."                              |
    | **Informal Contractions**   | Informal speech is preserved as spoken.                                                     | "She was gonna go, but y'all called."                        | Standard grammar should be used for clarity, outside of exceptions. Please refer to your [language style guide](https://www.notion.so/Transcription-1e5506eacaa280678598cf06de67802d?pvs=21) to know which contractions to keep vs. when to resort to standard grammar. | "She was going to go, but you all called."                                         |
    | **Emphasized Words**        | Elongated pronunciations are reflected with extended spelling.                              | "That was amaaazing!"                                        | Standard spelling is used.                                                                                                                                                                                                                                              | "That was amazing!"                                                                |
    | **Interjections**           | Interjections and vocal expressions are included.                                           | "Ugh, this is terrible. Wow, I can't believe it!"            | Only meaningful interjections are retained.                                                                                                                                                                                                                             | "This is terrible. Wow, I can't believe it!"                                       |
    | **Swear Words**             | Swear words are fully transcribed.                                                          | "Fuck this, I'm not going."                                  | Swear words should be fully transcribed, unless indicated otherwise.                                                                                                                                                                                                    | "Fuck this, I'm not going."                                                        |
    | **Pronunciation Mistakes**  | Mispronounced words are corrected.                                                          | **Example (spoken):** "ecsetera" **Transcribed:** "etcetera" | Mispronounced words are corrected here as well.                                                                                                                                                                                                                         | **Example (spoken):** "ecsetera" **Transcribed:** "etcetera"                       |
    | **Non-verbal human sounds** | Human non-verbal sounds like \[laughing], \[sighing], \[swallowing] are transcribed inline. | "I—\[sighs]—don't know."                                     | Most non-verbal sounds are excluded unless they impact meaning.                                                                                                                                                                                                         | "I don't know."                                                                    |
    | **Environmental Sounds**    | Environmental sounds are described in square brackets.                                      | "\[door slams], \[birds chirping], \[phone buzzes]"          | Omit unless essential to meaning. **Include if:** 1. The sound impacts emotion or meaning 2. The sound is directly referenced by the speaker                                                                                                                            | "What was that noise? \[dog barking]" "Hang on, I hear something \[door slamming]" |
  </Accordion>
</AccordionGroup>


## FAQ

<AccordionGroup>
  <Accordion title="What if I'm not happy with the result?">
    You can leave feedback on a completed transcript by clicking the three dots (⋯) next to your deliverable and selecting *Feedback*.
  </Accordion>

  <Accordion title="Can I make changes once I receive the final version?">
    No. You can export a completed transcript and make changes off platform. We plan to add support for this soon.
  </Accordion>
</AccordionGroup>



# Subtitles

> Human-edited captions and subtitles from ElevenLabs Productions


## General

Subtitles and captions ordered from Productions are reviewed and edited by native speakers for maximum accuracy and accessibility. We offer both subtitles and captions to meet your specific needs.

* For more detailed pricing information, please see the [**Pricing**](#pricing) section below.
* For more information about other Productions services, please see the [Overview](/docs/services/productions/overview) page.


## Captions vs. subtitles

Captions and subtitles serve different audiences and purposes, although they both display text on screen.

* **Captions** transcribe spoken dialogue and include SDH<a href="#sdh-footnote" aria-label="SDH footnote"><sup>1</sup></a> by default. They are not translated.

* **Subtitles** translate spoken dialogue for viewers who do not understand the source language; SDH<a href="#sdh-footnote" aria-label="SDH footnote"><sup>1</sup></a> can by included upon request.

<div>
  |                        | **Captions**                                | **Subtitles**                                  |
  | ---------------------- | ------------------------------------------- | ---------------------------------------------- |
  | Content                | Spoken dialogue                             | Spoken dialogue                                |
  | Translation            | No                                          | Yes                                            |
  | Non‑speech sounds      | Included by default                         | Not included by default                        |
  | Music cues             | Included by default                         | Not included by default                        |
  | Speaker identification | Included by default                         | Not included by default                        |
  | Typical audience       | Deaf/Hard of Hearing; same-language viewers | Hearing viewers who don’t know source language |
</div>

<div id="sdh-footnote">
  <sup>1</sup> SDH (Subtitles for the Deaf and Hard of Hearing) adds essential non‑speech audio cues
  (e.g., \[door slams], ♪ music ♪) and speaker identification. Included by default in captions;
  optional for subtitles.
</div>


## How it works

<Steps>
  <Step title="Order subtitles and captions">
    The easiest way to order new subtitles from Productions is from the
    [Productions](https://elevenlabs.io/app/productions) page in your ElevenLabs account.

    <Frame background="subtle">
      ![Productions Home Page](file:f135a835-1e24-485d-a859-5275d22fddb1)
    </Frame>
  </Step>

  <Step title="Export subtitles and captions">
    You will receive an email notification when your subtitles are ready and see them marked as
    'Done' on your Productions page. Export your completed subtitles in SRT format.

    <Frame background="subtle">
      ![Export Subtitles](file:87a0c9c2-6aad-431c-bfcb-a385a7236741)
    </Frame>
  </Step>
</Steps>


## Pricing

All prices are in USD (\$) and are per minute of source audio.

<div>
  | **Language**        | **Captions** | **Subtitles (English Source)** |
  | ------------------- | :----------: | :----------------------------: |
  | Arabic              |    \$3.60    |             \$9.00             |
  | English             |    \$2.20    |                -               |
  | French              |    \$3.30    |             \$8.00             |
  | German              |    \$4.00    |             \$9.90             |
  | Hindi               |    \$2.60    |             \$7.00             |
  | Italian             |    \$3.60    |             \$9.00             |
  | Portuguese (Brazil) |    \$3.30    |             \$9.00             |
  | Russian             |    \$4.20    |             \$9.90             |
  | Spanish             |    \$2.40    |             \$7.00             |
  | Turkish             |    \$4.00    |             \$9.00             |
  | Ukrainian           |    \$3.60    |             \$9.00             |
</div>

<Info>
  SDH is included in captions pricing. When added to subtitles, SDH is charged +30% above the
  standard subtitle rates.
</Info>

<Warning>
  Prices are subject to change. You will always see the final price for an order during the checkout
  process.
</Warning>


## SLAs / Delivery time

We aim to deliver all subtitles and captions **within 48-72 hours.** If you are an enterprise interested in achieving quicker turnaround times, please contact us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io).


## FAQ

<AccordionGroup>
  <Accordion title="What file formats do you support for subtitles?">
    We support SRT format for subtitle exports.
  </Accordion>

  <Accordion title="What if I'm not happy with the result?">
    You can leave feedback on a completed subtitle project by clicking the three dots (⋯) next to your deliverable and selecting *Feedback*.
  </Accordion>

  <Accordion title="Can I make changes once I receive the final version?">
    No. You can export completed subtitles and make changes off platform. We plan to add support for this soon.
  </Accordion>
</AccordionGroup>



# Dubbing (beta)

> Human-edited dubbing services from ElevenLabs Productions


## General

With our Productions dubbing offering, localize your content to reach any audience in the world. Share your video, source language, and destination language, and receive a fully dubbed video which is natural-sounding and production-ready.

* For more detailed pricing information, please see the [**Pricing**](#pricing) section below.
* For more information about other Productions services, please see the [Overview](/docs/services/productions/overview) page.


## How it works

<Steps>
  <Step title="Order a dub">
    The easiest way to order a dub from Productions is through the [Productions](https://elevenlabs.io/app/productions) page in your ElevenLabs account. Simply share:

    * **Your video file** (MP4, MOV, AVI, MKV)
    * **Source language** (e.g., English)
    * **Target language** (e.g., Spanish, Hindi, Arabic)

    <Frame background="subtle">
      <img src="file:f135a835-1e24-485d-a859-5275d22fddb1" alt="Productions Home" />
    </Frame>
  </Step>

  <Step title="Processing">
    Using proprietary AI models with human-in-the-loop craftsmanship, we:

    * Accurately **transcribe** the source audio
    * **Translate** into the requested target language with contextual accuracy
    * **Generate** synthetic voices matched to speaker identity and tone, or use custom voices
    * **Synchronize** dubbed speech with the original video timing
  </Step>

  <Step title="Order delivery">
    You'll receive a fully dubbed video with multiple export options: MP4 Video (default), AAC Audio, MP3 Audio, WAV Audio, Audio Tracks or Clips (Zip File), AAF (Timeline Data), SRT Captions, TXT Transcript.

    **To export your completed dub:**

    1. Access your order in the [Productions](https://elevenlabs.io/app/productions) page
    2. Click **View** to open the project
    3. Once inside the project, select your desired format from the export options
    4. Choose whether to normalize the audio (optional)
    5. Click **Export** to generate the file
    6. You can then view or download your exported dub

    <Frame background="subtle">
      <img src="file:f8565830-a077-4b93-a4da-901ef0bbbcbd" alt="Productions Export Dub" />
    </Frame>
  </Step>
</Steps>


## Behind the scenes

We follow a strict workflow to deliver consistent, natural-sounding dubs:

* **Transcription**: highly accurate transcription and speaker allocation.
* **Translation**: thorough review of translation accuracy by a native speaker, and edits to make the voice-over sound as natural as possible.
* **Voice selection**: we carefully pick the right voice for your dub, or use the voices you've shared with us.
* **Pacing**: we regenerate segments or edit the transcription to ensure the best possible pacing on each segment.
* **Quality control**: each dub goes through a checklist to ensure accuracy, consistency, and natural delivery.


## Pricing

All prices are in USD (\$) and are per minute of source audio. Dubbing is currently available from English source to the following destination languages:

<div>
  | **Destination Language** | **Dubbing** |
  | ------------------------ | :---------: |
  | Arabic                   |   \$22.00   |
  | French                   |   \$22.00   |
  | German                   |   \$22.00   |
  | Hindi                    |   \$22.00   |
  | Italian                  |   \$22.00   |
  | Portuguese (Brazil)      |   \$22.00   |
  | Russian                  |   \$22.00   |
  | Spanish                  |   \$22.00   |
  | Turkish                  |   \$22.00   |
  | Ukrainian                |   \$22.00   |
</div>

<Warning>
  Prices are subject to change. You will always see the final price for an order during the checkout
  process.
</Warning>


## SLAs / Delivery time

We aim to deliver all dubbing projects **within 7 business days.** If you are an enterprise interested in achieving quicker turnaround times, please contact us at [productions@elevenlabs.io](mailto:productions@elevenlabs.io).


## FAQ

<AccordionGroup>
  <Accordion title="What video formats do you support?">
    We support MP4, MOV, AVI, and MKV formats for video uploads. The final dubbed video is delivered in MP4 format by default.
  </Accordion>

  <Accordion title="What if I'm not happy with the result?">
    You can leave feedback on a completed dub by clicking the three dots (⋯) next to your deliverable and selecting *Feedback*.
  </Accordion>

  <Accordion title="Can I make changes once I receive the final version?">
    Yes, you can open the project in Dubbing Studio and make changes to refine the output.
  </Accordion>

  <Accordion title="Do you provide lip sync?">
    We do our best to match timing and visible mouth movements, but perfect lip sync is not guaranteed and may vary depending on the content.
  </Accordion>
</AccordionGroup>



# Troubleshooting

> Explore common issues and solutions.

Our models are non-deterministic, meaning outputs can vary based on inputs. While we strive to enhance predictability, some variability is inherent. This guide outlines common issues and preventive measures.


## General

<AccordionGroup>
  <Accordion title="Inconsistencies in volume and quality">
    If the generated voice output varies in volume or tone, it is often due to inconsistencies in the voice clone training audio.

    * **Apply compression**: Compress the training audio to reduce dynamic range and ensure consistent audio. Aim for a RMS between -23 dB and -18 dB and the true peak below -3 dB.
    * **Background noise**: Ensure the training audio contains only the voice you want to clone — no music, noise, or pops. Background noise, sudden bursts of energy or consistent low-frequency energy can make the AI less stable.
    * **Speaker consistency**: Ensure the speaker maintains a consistent distance from the microphone and avoids whispering or shouting. Variations can lead to inconsistent volume or tonality.
    * **Audio length**:
      * **Instant Voice Cloning**: Use 1–2 minutes of consistent audio. Consistency in tonality, performance, accent, and quality is crucial.
      * **Professional Voice Cloning**: Use at least 30 minutes, ideally 2+ hours, of consistent audio for best results.

    To minimize issues, consider breaking your text into smaller segments. This approach helps maintain consistent volume and reduces degradation over longer audio generations. Utilize our Studio feature to generate several smaller audio segments simultaneously, ensuring better quality and consistency.

    <Note>
      Refer to our guides for optimizing Instant and Professional Voice Clones for best practices and
      advice.
    </Note>
  </Accordion>

  <Accordion title="Mispronunciation">
    The multilingual models may rarely mispronounce certain words, even in English. This issue appears to be somewhat arbitrary but seems to be voice and text-dependent. It occurs more frequently with certain voices and text, especially when using words that also appear in other languages.

    * **Use Studio**: This feature helps minimize mispronunciation issues, which are more prevalent in longer text sections when using Speech Synthesis. While it won't completely eliminate the problem, it can help avoid it and make it easier to regenerate specific sections without redoing the entire text.
    * **Properly cloned voices**: Similar to addressing inconsistency issues, using a properly cloned voice in the desired languages can help reduce mispronunciation.
    * **Specify pronunciation**: When using our Studio feature, consider specifying the pronunciation of certain words, such as character names and brand names, or how acronyms should be read. For more information, refer to the Pronunciation Dictionary section of our guide to Studio.
  </Accordion>

  <Accordion title="Language switching and accent drift">
    The AI can sometimes switch languages or accents throughout a single generation, especially if that generation is longer in length. This issue is similar to the mispronunciation problem and is something we are actively working to improve.

    * **Use properly cloned voices**: Using an Instant Voice Clone or a Professional Voice Clone trained on high-quality, consistent audio in the desired language can help mitigate this issue. Pairing this with the Studio feature can further enhance stability.
    * **Understand voice limitations**: Default and generated voices are primarily English and may carry an English accent when used for other languages. Cloning a voice that speaks the target language with the desired accent provides the AI with better context, reducing the likelihood of language switching.
    * **Language selection**: Currently, the AI determines the language based on the input text. Writing in the desired language is crucial, especially when using pre-made voices that are English-based, as they may introduce an English accent.
    * **Optimal text length**: The AI tends to maintain a consistent accent over shorter text segments. For best results, keep text generations under 800-900 characters when using Text-to-Speech. The Studio workflow can help manage longer texts by breaking them into smaller, more manageable segments.
  </Accordion>

  <Accordion title="Mispronounced numbers, symbols or acronyms">
    The models may mispronounce certain numbers, symbols and acronyms. For example, the numbers "1, 2, 3" might be pronounced as "one," "two," "three" in English. To ensure correct pronunciation in another language, write them out phonetically or in words as you want them to be spoken.

    * **Example**: For the number "1" to be pronounced in French, write "un."
    * **Symbols**: Specify how symbols should be read, e.g., "\$" as "dollar" or "euro."
    * **Acronyms**: Spell out acronyms phonetically.
  </Accordion>

  <Accordion title="Corrupt speech">
    Corrupt speech is a rare issue where the model generates muffled or distorted audio. This occurs
    unpredictably, and we have not identified a cause. If encountered, regenerate the section to
    resolve the issue.
  </Accordion>

  <Accordion title="Audio degradation over longer generations">
    Audio quality may degrade during extended text-to-speech conversions, especially with the Multilingual v1 model. To mitigate this, break text into sections under 800 characters.

    * **Voice Selection**: Some voices are more susceptible to degradation. Use high-quality samples for cloned voices to minimize artifacts.
    * **Stability and Similarity**: Adjust these settings to influence voice behavior and artifact prominence. Hover over each setting for more details.
  </Accordion>

  <Accordion title="Style exaggeration">
    For some voices, this voice setting can lead to instability, including inconsistent speed,
    mispronunciation and the addition of extra sounds. We recommend keeping this setting at 0,
    especially if you find you are experiencing these issues in your generated audio.
  </Accordion>
</AccordionGroup>


## Studio (formerly Projects)

<AccordionGroup>
  <Accordion title="File imports">
    The import function attempts to import the file you provide to the website. Given the variability in website structures and book formatting, including images, always verify the import for accuracy.

    * **Chapter images**: If a book's chapters start with an image as the first letter, the AI may not recognize the letter. Manually add the letter to each chapter.
    * **Paragraph structure**: If text imports as a single long paragraph instead of following the original book's structure, it may not function correctly. Ensure the text maintains its original line breaks. If issues persist, try copying and pasting. If this fails, the text format may need conversion or rewriting.
    * **Preferred format**: EPUB is the recommended file format for creating a project in Studio. A well-structured EPUB will automatically split each chapter in Studio, facilitating navigation. Ensure each chapter heading is formatted as "Heading 1" for proper recognition.

    <Note>
      Always double-check imported content for accuracy and structure.
    </Note>
  </Accordion>

  <Accordion title="Glitches between paragraphs">
    Occasionally, glitches or sharp breaths may occur between paragraphs. This is rare and differs
    from standard Text to Speech issues. If encountered, regenerate the preceding paragraph, as the
    problem often originates there.
  </Accordion>
</AccordionGroup>

<Note>
  If an issue persists after following this troubleshooting guide, please [contact our support
  team](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937).
</Note>



# Zero Retention Mode (Enterprise)

> Learn how to use Zero Retention Mode to protect sensitive data.


## Background

By default, we retain data, in accordance with our Privacy Policy, to enhance our services, troubleshoot issues, and ensure the security of our systems. However, for some enterprise customers, we offer a "Zero Retention Mode" option for specific products. In this Zero Retention Mode, most data in requests and responses are immediately deleted once the request is completed.

ElevenLabs has agreements in place with each third-party LLM provider which expressly prohibit such providers from training their models on customer content, whether or not Zero Retention Mode is enabled.


## What is Zero Retention Mode?

Zero Retention Mode provides an additional level of security and peace of mind for especially sensitive workflows. When enabled, logging of certain data points is restricted, including:

* TTS text input
* TTS audio output
* Voice Changer audio input
* Voice Changer audio output
* STT audio input
* STT text output
* ElevenLabs Agents: all input and output
* Email associated with the account generating the input in our logs

This data is related to the processing of the request, and can only be seen by the user doing the request and the volatile memory of the process serving the request. None of this data is sent at any point to a database where data is stored long term.


## Who has access to Zero Retention Mode?

Enterprise customers can use Zero Retention Mode. It is primarily intended for use by our customers in the healthcare and banking sector, and other customers who may use our services to process sensitive information.


## When can a customer use Zero Retention Mode?

Zero Retention Mode is available to select enterprise customers. However, access to this feature may be restricted if ElevenLabs determines a customer's use case to be high risk, if an account is flagged by an automated system for additional moderation or at ElevenLabs' sole discretion. In such cases, the enterprise administrator will be promptly notified of the restriction.


## How does Zero Retention Mode work?

Zero Retention Mode only works for API requests, specifically:

* **Text to Speech**: this covers the Text-to-Speech (TTS) API, including all endpoints beginning with `/v1/text-to-speech/` and the TTS websocket connection.
* **Voice Changer**: this covers the Voice Changer API, including all endpoints starting with `/v1/speech-to-speech/`.

After setup, check the request history to verify Zero Retention Mode is enabled. If enabled, there should be no requests in the history.

Zero Retention Mode can be used by sending `enable_logging=false` with the product which supports it.

For example, in the Text to Speech API, you can set the query parameter [enable\_logging](https://elevenlabs.io/docs/api-reference/text-to-speech#parameter-enable-logging) to a `false` value:

<CodeBlocks>
  ```python title="Python" {12}
  from elevenlabs import ElevenLabs

  elevenlabs = ElevenLabs(
    api_key="YOUR_API_KEY",
  )

  response = elevenlabs.text_to_speech.convert(
    voice_id=voice_id,
    output_format="mp3_22050_32",
    text=text,
    model_id="eleven_turbo_v2",
    enable_logging=False,
  )

  ```

  ```javascript title="JavaScript" {9}
  import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

  const elevenlabs = new ElevenLabsClient({ apiKey: 'YOUR_API_KEY' });

  await elevenlabs.textToSpeech.convert(voiceId, {
    outputFormat: 'mp3_44100_128',
    text: text,
    modelId: 'eleven_turbo_v2',
    enableLogging: false,
  });
  ```

  ```bash title="cURL"
  curl --request POST \
    --url 'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?enable_logging=false' \
    --header 'Content-Type: application/json'
  ```
</CodeBlocks>


## What products are configured for Zero Retention Mode?

| Product                    | Type                 | Default Retention | Eligible for zero Retention |
| -------------------------- | -------------------- | ----------------- | --------------------------- |
| Text to Speech             | Text Input           | Enabled           | Yes                         |
|                            | Audio Output         | Enabled           | Yes                         |
| Voice Changer              | Audio Input          | Enabled           | Yes                         |
|                            | Audio Output         | Enabled           | Yes                         |
| Speech to Text             | Audio Input          | Enabled           | Yes                         |
|                            | Text Output          | Enabled           | Yes                         |
| Instant Voice Cloning      | Audio Samples        | Enabled           | No                          |
| Professional Voice Cloning | Audio Samples        | Enabled           | No                          |
| Dubbing                    | Audio/Video Input    | Enabled           | No                          |
|                            | Audio Output         | Enabled           | No                          |
| Projects                   | Text Input           | Enabled           | No                          |
|                            | Audio Output         | Enabled           | No                          |
| Agents Platform            | All Input and Output | Enabled           | Yes                         |

For ElevenLabs Agents, Gemini and Claude LLMs can be used in Zero Retention Mode.


## FAQ

<AccordionGroup>
  <Accordion title="What are some limitations of Zero Retention Mode?" default>
    Troubleshooting and support for Zero Retention Mode is limited. Because of the configuration, we
    will not be able to diagnose issues with TTS/STS generations. Debugging will be more difficult
    as a result.
  </Accordion>

  <Accordion title="How does retention work if Zero Retention Mode is not active?">
    Customers by default have history preservation enabled. All customers can use the API to delete
    generations at any time. This action will immediately remove the corresponding audio and text
    from our database; however, debugging and moderation logs may still retain data related to the
    generation.
  </Accordion>

  <Accordion title="Data backup (When Zero Retention Mode is not used)">
    For any retained data, we regularly back up such data to prevent data loss in the event of any
    unexpected incidents. Following data deletion, database items are retained in backups for up to
    30 days After this period, the data expires and is not recoverable.
  </Accordion>

  <Accordion title="Account deletion (When Zero Retention Mode is not used)">
    All data is deleted from our systems permanently when you delete your account. This includes all
    data associated with your account, such as API keys, request history, and any other data stored
    in your account. We also take commercially reasonable efforts to delete debugging data related
    to your account.
  </Accordion>
</AccordionGroup>



# Agents Platform

> Learn how to build, launch, and scale agents with ElevenLabs.

Agents accomplish tasks through natural dialogue - from quick requests to complex, open-ended workflows. ElevenLabs provides voice-rich, expressive models, developer tools for building multimodal agents, and tools to monitor and evaluate agent performance at scale.

<div id="agents-cards">
  <a href="/docs/agents-platform/build/overview">
    <div>
      <img src="file:14664ce5-6627-44cb-a94e-c0d2ff0c2866" alt="" />
    </div>

    <div>
      <h3>
        Build
      </h3>

      <p>
        Build multimodal agents with our developer toolkit, dashboard, or visual workflow builder
      </p>
    </div>
  </a>

  <a href="/docs/agents-platform/integrate/overview">
    <div>
      <img src="file:26fc8805-072c-4da9-893d-a09195b0dc3e" alt="" />
    </div>

    <div>
      <h3>
        Integrate
      </h3>

      <p>
        Integrate multimodal agents across telephony systems, web, and mobile
      </p>
    </div>
  </a>

  <a href="/docs/agents-platform/operate/overview">
    <div>
      <img src="file:7395c9e9-402a-4171-858a-a103c1555c5c" alt="" />

      <svg fill="none" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z" />
      </svg>
    </div>

    <div>
      <h3>
        Operate
      </h3>

      <p>
        Evaluate agent performance with built-in testing, evals, and analytics
      </p>
    </div>
  </a>
</div>


## Platform capabilities

From design to deployment to optimization, ElevenLabs provides everything you need to build agents at scale.

### Design and configure

| Goal                          | Guide                                                                      | Description                                                            |
| ----------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Create conversation workflows | [Workflows](/docs/agents-platform/customization/agent-workflows)           | Build multi-step workflows with visual workflow builder                |
| Write system prompts          | [System prompt](/docs/agents-platform/best-practices/prompting-guide)      | Learn best practices for crafting effective agent prompts              |
| Select language model         | [Models](/docs/agents-platform/build/models)                               | Choose from supported LLMs or bring your own custom model              |
| Control conversation flow     | [Conversation flow](/docs/agents-platform/customization/conversation-flow) | Configure turn-taking, interruptions, and timeout settings             |
| Configure voice & language    | [Voice & language](/docs/agents-platform/customization/voice)              | Select from 5k+ voices across 31 languages with customization options  |
| Add knowledge to agent        | [Knowledge base](/docs/agents-platform/customization/knowledge-base)       | Upload documents and enable RAG for grounded responses                 |
| Connect tools                 | [Tools](/docs/agents-platform/customization/tools)                         | Enable agents to call clients & APIs to perform actions                |
| Personalize each conversation | [Personalization](/docs/agents-platform/customization/personalization)     | Use dynamic variables and overrides for per-conversation customization |
| Secure agent access           | [Authentication](/docs/agents-platform/customization/authentication)       | Implement custom authentication for protected agent access             |

### Connect and deploy

| Goal                        | Guide                                                                               | Description                                                        |
| --------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Build with React components | [ElevenLabs UI](https://ui.elevenlabs.io)                                           | Pre-built components library for audio & agent apps (shadcn-based) |
| Embed widget in website     | [Widget](/docs/agents-platform/customization/widget)                                | Add a customizable web widget to any website                       |
| Build React web apps        | [React SDK](/docs/agents-platform/libraries/react)                                  | Voice-enabled React hooks and components                           |
| Build iOS apps              | [Swift SDK](/docs/agents-platform/libraries/swift)                                  | Native iOS SDK for voice agents                                    |
| Build Android apps          | [Kotlin SDK](/docs/agents-platform/libraries/kotlin)                                | Native Android SDK for voice agents                                |
| Build React Native apps     | [React Native SDK](/docs/agents-platform/libraries/react-native)                    | Cross-platform iOS and Android with React Native                   |
| Connect via SIP trunk       | [SIP trunk](/docs/agents-platform/phone-numbers/sip-trunking)                       | Integrate with existing telephony infrastructure                   |
| Make batch outbound calls   | [Batch calls](/docs/agents-platform/phone-numbers/batch-calls)                      | Trigger multiple calls programmatically                            |
| Use Twilio integration      | [Twilio](/docs/agents-platform/phone-numbers/twilio-integration/native-integration) | Native Twilio integration for phone calls                          |
| Build custom integrations   | [WebSocket API](/docs/agents-platform/libraries/websocket)                          | Low-level WebSocket protocol for custom implementations            |
| Receive real-time events    | [Events](/docs/agents-platform/customization/events)                                | Subscribe to conversation events and updates                       |

### Monitor and optimize

| Goal                         | Guide                                                                        | Description                                          |
| ---------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| Test agent behavior          | [Testing](/docs/agents-platform/customization/agent-testing)                 | Create and run automated tests for your agents       |
| Analyze conversation quality | [Conversation analysis](/docs/agents-platform/customization/agent-analysis)  | Extract insights and evaluate conversation outcomes  |
| Track metrics & analytics    | [Analytics](/docs/agents-platform/dashboard)                                 | Monitor performance metrics and conversation history |
| Configure data retention     | [Privacy](/docs/agents-platform/customization/privacy)                       | Set retention policies for conversations and audio   |
| Reduce LLM costs             | [Cost optimization](/docs/agents-platform/customization/llm/optimising-cost) | Monitor and optimize language model expenses         |


## Architecture

The Agents Platform coordinates 4 core components:

1. A fine-tuned Speech to Text (ASR) model for speech recognition
2. Your choice of language model or [custom](/docs/agents-platform/customization/llm/custom-llm) LLM
3. A low-latency Text to Speech (TTS) model across 5k+ voices and 31 languages
4. A proprietary turn-taking model that handles conversation timing

<Card title="Quickstart" href="/docs/agents-platform/quickstart">
  Build your first agent in 5 minutes
</Card>



---
**Navigation:** [← Previous](./09-voice-library.md) | [Index](./index.md) | [Next →](./11-build.md)
