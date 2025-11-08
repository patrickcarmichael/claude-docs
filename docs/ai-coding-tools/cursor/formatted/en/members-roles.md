---
title: "Members & Roles"
source: "https://docs.cursor.com/en/account/teams/members"
language: "en"
language_name: "English"
---

# Members & Roles
Source: https://docs.cursor.com/en/account/teams/members

Manage team members and roles

Cursor teams have three roles:

## Roles

**Members** are the default role with access to Cursor's Pro features.

* Full access to Cursor's Pro features
* No access to billing settings or admin dashboard
* Can see their own usage and remaining usage-based budget

**Admins** control team management and security settings.

* Full access to Pro features
* Add/remove members, modify roles, setup SSO
* Configure usage-based pricing and spending limits
* Access to team analytics

**Unpaid Admins** manage teams without using a paid seat - ideal for IT or finance staff who don't need Cursor access.

* Not billable, no Pro features
* Same administrative capabilities as Admins

<Info>Unpaid Admins require at least one paid user on the team.</Info>

## Role Comparison

<div className="full-width-table">
  | Capability             | Member | Admin | Unpaid Admin |
  | ---------------------- | :----: | :---: | :----------: |
  | Use Cursor features    |    ✓   |   ✓   |              |
  | Invite members         |    ✓   |   ✓   |       ✓      |
  | Remove members         |        |   ✓   |       ✓      |
  | Change user role       |        |   ✓   |       ✓      |
  | Admin dashboard        |        |   ✓   |       ✓      |
  | Configure SSO/Security |        |   ✓   |       ✓      |
  | Manage Billing         |        |   ✓   |       ✓      |
  | View Analytics         |        |   ✓   |       ✓      |
  | Manage Access          |        |   ✓   |       ✓      |
  | Set usage controls     |        |   ✓   |       ✓      |
  | Requires paid seat     |    ✓   |   ✓   |              |
</div>

## Managing members

All team members can invite others. We don't currently control invites.

### Add member

Add members three ways:

1. **Email invitation**

   * Click `Invite Members`
   * Enter email addresses
   * Users receive email invites

2. **Invite link**

   * Click `Invite Members`
   * Copy `Invite Link`
   * Share with team members

3. **SSO**
   * Configure SSO in [admin dashboard](/en/account/teams/sso)
   * Users auto-join when logging in via SSO email

<Warning>
  Invite links have a long expiration date - anyone with the link can join.
  Revoke them or use [SSO](/en/account/teams/sso)
</Warning>

### Remove member

Admins can remove members anytime via context menu → "Remove". If a member has used any credits, their seat remains occupied until the end of the billing cycle.

### Change role

Admins can change roles for other members by clicking the context menu and then use the "Change role" option.<br />

There must be at least one Admin, and one paid member on the team at all times.

## Security & SSO

SAML 2.0 Single Sign-On (SSO) is available on Team plans. Key features include:

* Configure SSO connections ([learn more](/en/account/teams/sso))
* Set up domain verification
* Automatic user enrollment
* SSO enforcement options
* Identity provider integration (Okta, etc)

<Note>
  <p className="!mb-0">Domain verification is required to enable SSO.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

## Usage Controls

Access usage settings to:

* Enable usage-based pricing
* Enable for premium models
* Set admin-only modifications
* Set monthly spending limits
* Monitor team-wide usage

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

## Billing

When adding team members:

* Each member or admin adds a billable seat (see [pricing](https://cursor.com/pricing))
* New members are charged pro-rata for their remaining time in the billing period
* Unpaid admin seats aren't counted

Mid-month additions charge only for days used. When removing members who have used credits, their seat remains occupied until the end of the billing cycle - no pro-rated refunds are given.

Role changes (e.g., Admin to Unpaid Admin) adjust billing from the change date. Choose monthly or yearly billing.

Monthly/yearly renewal occurs on your original signup date, regardless of member changes.

### Switch to Yearly billing

Save **20%** by switching from monthly to yearly:

1. Go to [Dashboard](https://cursor.com/dashboard)
2. In account section, click "Advanced" then "Upgrade to yearly billing"

<Note>
  You can only switch from monthly to yearly via dashboard. To switch from
  yearly to monthly, contact [hi@cursor.com](mailto:hi@cursor.com).
</Note>

---

← Previous: [Enterprise Settings](./enterprise-settings.md) | [Index](./index.md) | Next: [SCIM](./scim.md) →