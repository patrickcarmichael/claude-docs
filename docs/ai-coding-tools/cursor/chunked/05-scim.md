# SCIM

**Navigation:** [← Previous](./04-developers.md) | [Index](./index.md) | [Next →](./06-overview.md)

---

# SCIM
Source: https://docs.cursor.com/en/account/teams/scim

Set up SCIM provisioning for automated user and group management

## Overview

SCIM 2.0 provisioning automatically manages your team members and directory groups through your identity provider. Available on Enterprise plans with SSO enabled.

<product_visual type="screenshot">
  SCIM settings dashboard showing Active Directory Management configuration
</product_visual>

## Prerequisites

* Cursor Enterprise plan
* SSO must be configured first - **SCIM requires an active SSO connection**
* Admin access to your identity provider (Okta, Azure AD, etc.)
* Admin access to your Cursor organization

## How it works

### User provisioning

Users are automatically added to Cursor when assigned to the SCIM application in your identity provider. When unassigned, they're removed. Changes sync in real-time.

### Directory groups

Directory groups and their membership sync from your identity provider. Group and user management must be done through your identity provider - Cursor displays this information as read-only.

### Spend management

Set different per-user spend limits for each directory group. Directory group limits take precedence over team-level limits. Users in multiple groups receive the highest applicable spend limit.

## Setup

<Steps>
  <Step title="Ensure SSO is configured">
    SCIM requires SSO to be set up first. If you haven't configured SSO yet,
    follow the [SSO setup guide](/en/account/teams/sso) before proceeding.
  </Step>

  <Step title="Access Active Directory Management">
    Navigate to
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    with an admin account, or go to your dashboard settings and select the
    "Active Directory Management" tab.
  </Step>

  <Step title="Start SCIM setup">
    Once SSO is verified, you'll see a link for step-by-step SCIM setup. Click
    this to begin the configuration wizard.
  </Step>

  <Step title="Configure SCIM in your identity provider">
    In your identity provider: - Create or configure your SCIM application - Use
    the SCIM endpoint and token provided by Cursor - Enable user and push group
    provisioning - Test the connection
  </Step>

  <Step title="Configure spend limits (optional)">
    Back in Cursor's Active Directory Management page: - View your synchronized
    directory groups - Set per-user spend limits for specific groups as needed -
    Review which limits apply to users in multiple groups
  </Step>
</Steps>

### Identity provider setup

For provider-specific setup instructions:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Setup instructions for Okta, Azure AD, Google Workspace, and more.
</Card>

## Managing users and groups

<Warning>
  All user and group management must be done through your identity provider.
  Changes made in your identity provider will automatically sync to Cursor, but
  you cannot modify users or groups directly in Cursor.
</Warning>

### User management

* Add users by assigning them to your SCIM application in your identity provider
* Remove users by unassigning them from the SCIM application
* User profile changes (name, email) sync automatically from your identity provider

### Group management

* Directory groups are automatically synced from your identity provider
* Group membership changes are reflected in real-time
* Use groups to organize users and set different spend limits

### Spend limits

* Set different per-user limits for each directory group
* Users inherit the highest spend limit from their groups
* Group limits override the default team-wide per-user limit

## FAQ

### Why isn't SCIM management showing up in my dashboard?

Ensure SSO is properly configured and working before setting up SCIM. SCIM requires an active SSO connection to function.

### Why aren't users syncing?

Verify that users are assigned to the SCIM application in your identity provider. Users must be explicitly assigned to appear in Cursor.

### Why aren't groups appearing?

Check that push group provisioning is enabled in your identity provider's SCIM settings. Group sync must be configured separately from user sync.

### Why aren't spend limits applying?

Confirm users are properly assigned to the expected groups in your identity provider. Group membership determines which spend limits apply.

### Can I manage SCIM users and groups directly in Cursor?

No. All user and group management must be done through your identity provider. Cursor displays this information as read-only.

### How quickly do changes sync?

Changes made in your identity provider sync to Cursor in real-time. There may be a brief delay for large bulk operations.



# Get Started
Source: https://docs.cursor.com/en/account/teams/setup

Create and set up a Cursor team

## Cursor for Teams

Cursor works for individuals and teams. The Teams plan provides tools for organizations: SSO, team management, access controls, and usage analytics.

## Creating a Team

Create a team by following these steps:

<Steps>
  <Step title="Set up Teams plan">
    To create a Team, follow these steps:

    1. **For new users**: Visit [cursor.com/team/new-team](https://cursor.com/team/new-team) to create a new account and team
    2. **For existing users**: Go to your [dashboard](/en/account/dashboard) and click "Upgrade to Teams"
  </Step>

  <Step title="Enter Team details">
    Select a Team name and billing cycle

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="Invite members">
    Invite team members. User counts are prorated - you only pay for the time users are members.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="Enable SSO (optional)">
    Enable [SSO](/en/account/teams/sso) for security and automated onboarding.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

## FAQ

<AccordionGroup>
  <Accordion title="My team uses ZScalar / a proxy / a VPN, will Cursor work?">
    Cursor uses HTTP/2 by default. Some proxies and VPNs block this.

    Enable HTTP/1.1 fallback in settings to use HTTP/1.1 instead.
  </Accordion>

  <Accordion title="How can I purchase licenses for my company?">
    Cursor bills per active user, not seats. Add or remove users anytime - new members are charged pro-rata for their remaining time. If a removed user has used any credits, their seat remains occupied until the end of the billing cycle.

    Your renewal date stays the same.
  </Accordion>

  <Accordion title="How can I set up a team when I'm not using Cursor?">
    Set yourself as an [Unpaid Admin](/en/account/teams/members) to manage without a license.

    <Warning>
      Teams need at least one paid member. You can set up, invite a member, then change your role before billing.
    </Warning>
  </Accordion>

  <Accordion title="How can I add Cursor to my company's MDM?">
    Download links for all platforms are available at [cursor.com/downloads](https://cursor.com/downloads).

    MDM instructions:

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html) (formerly VMware)
    * [Microsoft Intune (Windows)](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune (Mac)](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



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



# Update Access
Source: https://docs.cursor.com/en/account/update-access

Choose how often you receive updates

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor has two update channels.

<Tabs>
  <Tab title="Default">
    The default update channel with tested releases.

    * Stable releases
    * Bug fixes from pre-release testing
    * Default for all users
    * Only option for team users

    <Note>
      Team and business accounts use Default mode.
    </Note>
  </Tab>

  <Tab title="Early Access">
    Pre-release versions with new features.

    <Warning>
      Early Access builds may have bugs or stability issues.
    </Warning>

    * Access to features in development
    * May contain bugs
    * Not available for team accounts
  </Tab>
</Tabs>

## Change update channel

1. **Open settings**: Press <Kbd>Cmd+Shift+J</Kbd>
2. **Go to Beta**: Select Beta in the sidebar
3. **Select channel**: Choose Default or Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Report Early Access issues on the [Forum](https://forum.cursor.com).



# Apply
Source: https://docs.cursor.com/en/agent/apply

Learn how to apply, accept, or reject code suggestions from chat using Apply

## How Apply works

Apply is a specialized Cursor model that takes code generated by chat and integrates it into your files. It processes the code blocks from chat conversations and applies the changes to your codebase.

Apply does not generate code itself. The chat model generates the code, and Apply handles the integration into existing files. It can process changes across multiple files and large codebases.

## Apply code blocks

To apply a code block suggestion, press the play button in the top right corner of a code block.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/en/agent/chat/checkpoints

Save and restore previous states after Agent changes

Checkpoints are automatic snapshots of Agent's changes to your codebase. They let you undo Agent modifications if needed.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

## Restoring checkpoints

Two ways to restore:

1. **From input box**: Click `Restore Checkpoint` button on previous requests
2. **From message**: Click the + button when hovering over a message

<Warning>
  Checkpoints are not version control. Use Git for permanent history.
</Warning>

## How they work

* Stored locally, separate from Git
* Track only Agent changes (not manual edits)
* Cleaned up automatically

<Note>
  Manual edits aren't tracked. Only use checkpoints for Agent changes.
</Note>

## FAQ

<AccordionGroup>
  <Accordion title="Do checkpoints affect Git?">
    No. They're separate from Git history.
  </Accordion>

  {" "}

  <Accordion title="How long are they kept?">
    For the current session and recent history. Automatically cleaned up.
  </Accordion>

  <Accordion title="Can I create them manually?">
    No. They're created automatically by Cursor.
  </Accordion>
</AccordionGroup>

{" "}



# Commands
Source: https://docs.cursor.com/en/agent/chat/commands

Define commands for reusable workflows

Custom commands allow you to create reusable workflows that can be triggered with a simple `/` prefix in the chat input box. These commands help standardize processes across your team and make common tasks more efficient.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Commands are currently in beta. The feature and syntax may change as we continue to improve it.
</Info>

## How commands work

Commands are defined as plain Markdown files that can be stored in two locations:

1. **Project commands**: Stored in the `.cursor/commands` directory of your project
2. **Global commands**: Stored in the `~/.cursor/commands` directory in your home directory

When you type `/` in the chat input box, Cursor will automatically detect and display available commands from both directories, making them instantly accessible across your workflow.

## Creating commands

1. Create a `.cursor/commands` directory in your project root
2. Add `.md` files with descriptive names (e.g., `review-code.md`, `write-tests.md`)
3. Write plain Markdown content describing what the command should do
4. Commands will automatically appear in the chat when you type `/`

Here's an example of how your commands directory structure might look:

```
.cursor/
└── commands/
    ├── address-github-pr-comments.md
    ├── code-review-checklist.md
    ├── create-pr.md
    ├── light-review-existing-diffs.md
    ├── onboard-new-developer.md
    ├── run-all-tests-and-fix.md
    ├── security-audit.md
    └── setup-new-feature.md
```

## Examples

Try these commands in your projects to get a feel for how they work.

<AccordionGroup>
  <Accordion title="Code review checklist">
    ```markdown  theme={null}
    # Code Review Checklist

    ## Overview
    Comprehensive checklist for conducting thorough code reviews to ensure quality, security, and maintainability.

    ## Review Categories

    ### Functionality
    - [ ] Code does what it's supposed to do
    - [ ] Edge cases are handled
    - [ ] Error handling is appropriate
    - [ ] No obvious bugs or logic errors

    ### Code Quality
    - [ ] Code is readable and well-structured
    - [ ] Functions are small and focused
    - [ ] Variable names are descriptive
    - [ ] No code duplication
    - [ ] Follows project conventions

    ### Security
    - [ ] No obvious security vulnerabilities
    - [ ] Input validation is present
    - [ ] Sensitive data is handled properly
    - [ ] No hardcoded secrets
    ```
  </Accordion>

  <Accordion title="Security audit">
    ```markdown  theme={null}
    # Security Audit

    ## Overview
    Comprehensive security review to identify and fix vulnerabilities in the codebase.

    ## Steps
    1. **Dependency audit**
       - Check for known vulnerabilities
       - Update outdated packages
       - Review third-party dependencies

    2. **Code security review**
       - Check for common vulnerabilities
       - Review authentication/authorization
       - Audit data handling practices

    3. **Infrastructure security**
       - Review environment variables
       - Check access controls
       - Audit network security

    ## Security Checklist
    - [ ] Dependencies updated and secure
    - [ ] No hardcoded secrets
    - [ ] Input validation implemented
    - [ ] Authentication secure
    - [ ] Authorization properly configured
    ```
  </Accordion>

  <Accordion title="Setup new feature">
    ```markdown  theme={null}
    # Setup New Feature

    ## Overview
    Systematically set up a new feature from initial planning through to implementation structure.

    ## Steps
    1. **Define requirements**
       - Clarify feature scope and goals
       - Identify user stories and acceptance criteria
       - Plan technical approach

    2. **Create feature branch**
       - Branch from main/develop
       - Set up local development environment
       - Configure any new dependencies

    3. **Plan architecture**
       - Design data models and APIs
       - Plan UI components and flow
       - Consider testing strategy

    ## Feature Setup Checklist
    - [ ] Requirements documented
    - [ ] User stories written
    - [ ] Technical approach planned
    - [ ] Feature branch created
    - [ ] Development environment ready
    ```
  </Accordion>

  <Accordion title="Create pull request">
    ```markdown  theme={null}
    # Create PR

    ## Overview
    Create a well-structured pull request with proper description, labels, and reviewers.

    ## Steps
    1. **Prepare branch**
       - Ensure all changes are committed
       - Push branch to remote
       - Verify branch is up to date with main

    2. **Write PR description**
       - Summarize changes clearly
       - Include context and motivation
       - List any breaking changes
       - Add screenshots if UI changes

    3. **Set up PR**
       - Create PR with descriptive title
       - Add appropriate labels
       - Assign reviewers
       - Link related issues

    ## PR Template
    - [ ] Feature A
    - [ ] Bug fix B
    - [ ] Unit tests pass
    - [ ] Manual testing completed
    ```
  </Accordion>

  <Accordion title="Run tests and fix failures">
    ```markdown  theme={null}
    # Run All Tests and Fix Failures

    ## Overview
    Execute the full test suite and systematically fix any failures, ensuring code quality and functionality.

    ## Steps
    1. **Run test suite**
       - Execute all tests in the project
       - Capture output and identify failures
       - Check both unit and integration tests

    2. **Analyze failures**
       - Categorize by type: flaky, broken, new failures
       - Prioritize fixes based on impact
       - Check if failures are related to recent changes

    3. **Fix issues systematically**
       - Start with the most critical failures
       - Fix one issue at a time
       - Re-run tests after each fix
    ```
  </Accordion>

  <Accordion title="Onboard new developer">
    ```markdown  theme={null}
    # Onboard New Developer

    ## Overview
    Comprehensive onboarding process to get a new developer up and running quickly.

    ## Steps
    1. **Environment setup**
       - Install required tools
       - Set up development environment
       - Configure IDE and extensions
       - Set up git and SSH keys

    2. **Project familiarization**
       - Review project structure
       - Understand architecture
       - Read key documentation
       - Set up local database

    ## Onboarding Checklist
    - [ ] Development environment ready
    - [ ] All tests passing
    - [ ] Can run application locally
    - [ ] Database set up and working
    - [ ] First PR submitted
    ```
  </Accordion>
</AccordionGroup>



# Compact
Source: https://docs.cursor.com/en/agent/chat/compact

Save space in chat with compact mode interface

Compact mode provides a streamlined chat interface by reducing visual clutter and maximizing available space for conversations.

## Overview

When enabled, compact mode transforms the chat interface by:

* **Hiding icons** for a cleaner, minimalist appearance
* **Auto-collapsing diffs** to reduce visual noise
* **Auto-collapsing input** to maximize conversation space

This setting is particularly useful when working on smaller screens or when you prefer a focused, distraction-free chat experience.

## Before and After

### Default mode

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="Chat interface in default mode showing all icons and expanded elements" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

### Compact mode

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="Chat interface in compact mode with hidden icons and collapsed elements" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

## Enabling compact mode

To enable compact mode:

1. Open Cursor Settings
2. Navigate to **Chat** settings
3. Toggle **Compact Mode** to enable

The interface will immediately update to the streamlined view, giving you more space to focus on your conversations.



# Duplicate
Source: https://docs.cursor.com/en/agent/chat/duplicate

Create branches from any point in a conversation

Duplicate/fork chats to explore alternative solutions without losing your current conversation.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

## How to duplicate

1. Find where you want to branch off
2. Click the three dots on the message
3. Select "Duplicate Chat"

## What happens

* Context up to that point is preserved
* Original conversation remains unchanged
* Both chats maintain separate history



# Export
Source: https://docs.cursor.com/en/agent/chat/export

Export chats to markdown format

Export Agent chats as markdown files for sharing or documentation.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

## What's exported

* All messages and responses
* Code blocks with syntax highlighting
* File references and context
* Chronological conversation flow

## How to export

1. Navigate to the chat to export
2. Click context menu → "Export Chat"
3. Save the file locally

<Warning>
  Review exports for sensitive data: API keys, internal URLs, proprietary code,
  personal information
</Warning>



# History
Source: https://docs.cursor.com/en/agent/chat/history

View and manage chat conversations

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Access past Agent conversations from the history panel.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat History" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

## Opening history

* Click the history icon in Agent sidepane
* Press <Kbd tooltip="Open chat history">Opt Cmd '</Kbd>

## Managing chats

* **Edit titles**: Click to rename
* **Delete**: Remove unneeded chats
* **Open**: Click to review full conversation

Chat history is stored locally in a SQLite database on your machine.

<Note>
  To preserve chats, [export them](/en/agent/chats/export) as markdown.
</Note>

## Background Agents

Background agent chats aren't in regular history but instead stored in a remote database. Use <Kbd tooltip="Open background agent control panel">Cmd E</Kbd> to view them.

## Referencing past chats

Use [@Past Chats](/en/context/@-symbols/@-past-chats) to include context from previous conversations in your current chat.



# Summarization
Source: https://docs.cursor.com/en/agent/chat/summarization

Context management for long conversations in chat

## Message summarization

As conversations grow longer, Cursor automatically summarizes and manages context to keep your chats efficient. Learn how to use the context menu and understand how files are condensed to fit within model context windows.

### Using the /summarize command

You can manually trigger summarization using the `/summarize` command in chat. This command helps manage context when conversations become too long, allowing you to continue working efficiently without losing important information.

<Info>
  For a deeper dive into how context works in Cursor, check our [Working with
  Context](/en/guides/working-with-context) guide.
</Info>

### How summarization works

When conversations grow longer, they exceed the model's context window limit:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Context window limit</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

To solve this, Cursor summarizes older messages to make room for new conversations.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Context window limit
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Summarized Messages
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

## File & folder condensation

While chat summarization handles long conversations, Cursor uses a different strategy for managing large files and folders: **smart condensation**. When you include files in your conversation, Cursor determines the best way to present them based on their size and available context space.

Here are the different states a file/folder can be in:

### Condensed

When files or folders are too large to fit within the context window, Cursor automatically condenses them. Condensing shows the model key structural elements like function signatures, classes, and methods. From this condensed view, the model can choose to expand specific files if needed. This approach maximizes effective use of the available context window.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Context menu" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

### Significantly condensed

When a file name appears with a "Significantly Condensed" label, the file was too large to include in full, even in condensed form. Only the file name will be shown to the model.

### Not included

When a warning icon appears next to a file or folder, the item is too large to be included in the context window, even in condensed form. This helps you understand which parts of your codebase are accessible to the model.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context menu" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# Tabs
Source: https://docs.cursor.com/en/agent/chat/tabs

Run multiple Agent conversations simultaneously

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

## Overview

Press <Kbd>Cmd+T</Kbd> to create new tabs. Each tab maintains separate conversation history, context, and model selection.

<Tip>
  For parallel workflows, try [Background Agents](/en/background-agents)
</Tip>

## Managing tabs

* Create new tabs with <Kbd>Cmd+T</Kbd>. Each tab starts with a fresh conversation and maintains its own context.

* Switch between tabs by clicking their headers or using <Kbd>Ctrl+Tab</Kbd> to cycle through them.

* Tab titles are auto-generated after the first message, but you can rename them by right-clicking on the tab header.

<Tip>
  Use one task per tab, provide clear initial descriptions, and close finished
  tabs to keep your workspace organized.
</Tip>

### Conflicts

Cursor prevents multiple tabs from editing the same files. You'll be prompted to resolve conflicts.

## Reference other chats

Use [@Past Chats](/en/context/@-symbols/@-past-chats) to include context from other tabs or previous sessions.



# Modes
Source: https://docs.cursor.com/en/agent/modes

Choose the right mode for your task - from autonomous coding to focused edits

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent offers different modes optimized for specific tasks. Each mode has different capabilities and tools enabled to match your workflow needs.

<div className="full-width-table">
  | Mode                  | For                           | Capabilities                                | Tools             |
  | :-------------------- | :---------------------------- | :------------------------------------------ | :---------------- |
  | **[Agent](#agent)**   | Complex features, refactoring | Autonomous exploration, multi-file edits    | All tools enabled |
  | **[Ask](#ask)**       | Learning, planning, questions | Read-only exploration, no automatic changes | Search tools only |
  | **[Custom](#custom)** | Specialized workflows         | User-defined capabilities                   | Configurable      |
</div>

## Agent

The default mode for complex coding tasks. Agent autonomously explores your codebase, edits multiple files, runs commands, and fixes errors to complete your requests.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

## Ask

Read-only mode for learning and exploration. Ask searches your codebase and provides answers without making any changes - perfect for understanding code before modifying it.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

## Custom

Create your own modes with specific tool combinations and instructions. Mix and match capabilities to fit your workflow.

<Note>
  Custom modes are in beta. Enable them in `Cursor Settings` → `Chat` → `Custom
    Modes`
</Note>

### Examples

<AccordionGroup>
  <Accordion title="Learn">
    **Tools:** All Search\
    **Instructions:** Focus on explaining concepts thoroughly and ask clarifying questions
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Tools:** Edit & Reapply **Instructions:** Improve code structure without
    adding new functionality
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Tools:** Codebase, Read file, Terminal **Instructions:** Create detailed
    implementation plans in `plan.md`
  </Accordion>

  <Accordion title="Debug">
    **Tools:** All Search, Terminal, Edit & Reapply\
    **Instructions:** Investigate issues thoroughly before proposing fixes
  </Accordion>
</AccordionGroup>

## Switching modes

* Use the mode picker dropdown in Agent
* Press <Kbd>Cmd+.</Kbd> for quick switching
* Set keyboard shortcuts in [settings](#settings)

## Settings

All modes share common configuration options:

<div className="full-width-table">
  | Setting            | Description                           |
  | :----------------- | :------------------------------------ |
  | Model              | Choose which AI model to use          |
  | Keyboard shortcuts | Set shortcuts to switch between modes |
</div>

Mode-specific settings:

<div className="full-width-table">
  | Mode       | Settings                      | Description                                           |
  | :--------- | :---------------------------- | :---------------------------------------------------- |
  | **Agent**  | Auto-run and Auto-fix Errors  | Automatically run commands and fix errors             |
  | **Ask**    | Search Codebase               | Automatically find relevant files                     |
  | **Custom** | Tool selection & Instructions | Configure [tools](/en/agent/tools) and custom prompts |
</div>



# Overview
Source: https://docs.cursor.com/en/agent/overview

Assistant for autonomous coding tasks, terminal commands, and code editing

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent is Cursor's assistant that can complete complex coding tasks independently, run terminal commands, and edit code. Access in sidepane with <Kbd>Cmd+I</Kbd>.

<Frame caption="Agent in sidepane">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/en/agent/modes" className="hover:text-primary transition-colors">
          Modes
        </a>
      </h2>

      <p className="text-sm">
        Choose between Agent, Ask, or create custom modes. Each mode has
        different capabilities and tools to match your workflow.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agent modes" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/tools" className="hover:text-primary transition-colors">
          Tools
        </a>
      </h3>

      <p className="text-sm">
        Agent uses tools to search, edit, and run commands. From semantic codebase
        search to terminal execution, these tools enable autonomous task
        completion.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Agent tools" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/apply" className="hover:text-primary transition-colors">
          Apply Changes
        </a>
      </h3>

      <p className="text-sm">
        Integrate AI-suggested code blocks into your codebase. Apply handles
        large-scale changes efficiently while maintaining precision.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="Apply changes" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/review" className="hover:text-primary transition-colors">
          Review Diffs
        </a>
      </h3>

      <p className="text-sm">
        Examine changes before accepting them. Review interface shows additions
        and deletions with color-coded lines for control over modifications.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/chats/tabs" className="hover:text-primary transition-colors">
          Chat Tabs
        </a>
      </h3>

      <p className="text-sm">
        Run multiple conversations simultaneously with <Kbd>Cmd+T</Kbd>. Each tab
        maintains its own context, history, and model selection.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          Checkpoints
        </a>
      </h3>

      <p className="text-sm">
        Automatic snapshots track Agent's changes. Restore previous states if
        changes don't work as expected or to try different approaches.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/terminal" className="hover:text-primary transition-colors">
          Terminal Integration
        </a>
      </h3>

      <p className="text-sm">
        Agent executes terminal commands, monitors output, and handles multi-step
        processes. Configure auto-run for trusted workflows or require
        confirmation for safety.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Terminal integration" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/chats/history" className="hover:text-primary transition-colors">
          Chat History
        </a>
      </h3>

      <p className="text-sm">
        Access past conversations with <Kbd>Opt Cmd '</Kbd>. Review previous
        discussions, track coding sessions, and reference context from earlier
        chats.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chat history" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/agent/chats/export" className="hover:text-primary transition-colors">
          Export Chats
        </a>
      </h3>

      <p className="text-sm">
        Export conversations to markdown format. Share solutions with team
        members, document decisions, or create knowledge bases from coding
        sessions.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/en/context/rules" className="hover:text-primary transition-colors">
          Rules
        </a>
      </h3>

      <p className="text-sm">
        Define custom instructions for Agent behavior. Rules help maintain coding
        standards, enforce patterns, and personalize how Agent assists with your
        project.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Agent rules" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Planning
Source: https://docs.cursor.com/en/agent/planning

How Agent plans and manages complex tasks with todos and queuing

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent can plan ahead and manage complex tasks with structured to-do lists and message queuing, making long-horizon tasks easier to understand and track.

## Agent to-dos

Agent can break down longer tasks into manageable steps with dependencies, creating a structured plan that updates as work progresses.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

### How it works

* Agent automatically creates to-do lists for complex tasks
* Each item can have dependencies on other tasks
* The list updates in real-time as work progresses
* Completed tasks are marked off automatically

### Visibility

* To-dos appear in the chat interface
* If [Slack integration](/en/slack) is set up, to-dos are also visible there
* You can view the full task breakdown at any time

<Tip>
  For better planning, describe your end goal clearly. Agent will create more
  accurate task breakdowns when it understands the full scope.
</Tip>

<Note>Planning and to-dos are currently not supported for auto mode.</Note>

## Queued messages

Queue follow-up messages while Agent is working on the current task. Your instructions wait in line and execute automatically when ready.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

### Using the queue

1. While Agent is working, type your next instruction
2. Press <Kbd>Ctrl+Enter</Kbd> to add it to the queue
3. Messages appear in order below the active task
4. Reorder queued messages by clicking arrow
5. Agent processes them sequentially after finishing

### Override the queue

To queue your message instead of using default messaging, use <Kbd>Ctrl+Enter</Kbd>. To send a message immediately without queuing, use <Kbd>Cmd+Enter</Kbd>. This "force pushes" your message, bypassing the queue to execute right away.

## Default messaging

Messages send as fast as possible by default, typically appearing right after Agent completes a tool call. This creates the most responsive experience.

### How default messaging works

* Your message gets appended to the most recent user message in the chat
* Messages typically attach to tool results and send immediately when ready
* This creates a more natural conversation flow without interrupting Agent's current work
* By default, this happens when you press Enter while Agent is working



# Diffs & Review
Source: https://docs.cursor.com/en/agent/review

Review and manage code changes generated by the AI agent

When Agent generates code changes, they're presented in a review interface that shows additions and deletions with color-coded lines. This allows you to examine and control which changes are applied to your codebase.

The review interface displays code changes in a familiar diff format:

## Diffs

<div className="full-width-table">
  | Type              | Meaning                    | Example                                                                                               |
  | :---------------- | :------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | New code additions         | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | Code removals              | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | Unchanged surrounding code | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

## Review

After generation completes, you'll see a prompt to review all changes before proceeding. This gives you an overview of what will be modified.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Review input interface" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

### File-by-file

A floating review bar appears at the bottom of your screen, allowing you to:

* **Accept** or **reject** changes for the current file
* Navigate to the **next file** with pending changes
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Your browser does not support the video tag.
    </video>
  </Frame>

### Selective acceptance

For fine-grained control:

* To accept most changes: reject unwanted lines, then click **Accept all**
* To reject most changes: accept wanted lines, then click **Reject all**

## Review changes

At the end of the agent response, click the **Review changes** button to see the full diff of the changes.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/en/agent/terminal

Run terminal commands automatically as part of agent operations

Agent executes commands in Cursor's native terminal with preserved history. Click skip to send <kbd>Ctrl+C</kbd> and interrupt commands.

## Troubleshooting

<Info>
  Some shell themes (for example, Powerlevel9k/Powerlevel10k) can interfere with
  the inline terminal output. If your command output looks truncated or
  misformatted, disable the theme or switch to a simpler prompt when Agent runs.
</Info>

### Disable heavy prompts for Agent sessions

Use the `CURSOR_AGENT` environment variable in your shell config to detect when
the Agent is running and skip initializing fancy prompts/themes.

```zsh  theme={null}

# ~/.zshrc — disable Powerlevel10k when Cursor Agent runs
if [[ -n "$CURSOR_AGENT" ]]; then
  # Skip theme initialization for better compatibility
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — fall back to a simple prompt in Agent sessions
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Tools
Source: https://docs.cursor.com/en/agent/tools

Tools available to agents for searching, editing, and running code

A list of all tools available to modes within the [Agent](/en/agent/overview), which you can enable or disable when building your own [custom modes](/en/agent/modes#custom).

<Note>
  There is no limit on the number of tool calls Agent can make during a task. Agent will continue using tools as needed to complete your request.
</Note>

## Search

Tools used to search your codebase and the web to find relevant information.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Reads up to 250 lines (750 in max mode) of a file.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Read the structure of a directory without reading file contents.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Perform semantic searches within your [indexed
    codebase](/en/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Search for exact keywords or patterns within files.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Find files by name using fuzzy matching.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Generate search queries and perform web searches.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Retrieve specific [rules](/en/context/rules) based on type and description.
  </Accordion>
</AccordionGroup>

## Edit

Tools used to make specific edits to your files and codebase.

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    Suggest edits to files and [apply](/en/agent/apply) them automatically.
  </Accordion>

  <Accordion title="Delete File" icon="trash">
    Delete files autonomously (can be disabled in settings).
  </Accordion>
</AccordionGroup>

## Run

Chat can interact with your terminal.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Execute terminal commands and monitor output.
  </Accordion>
</AccordionGroup>

<Note>By default, Cursor uses the first terminal profile available.</Note>

To set your preferred terminal profile:

1. Open Command Palette (`Cmd/Ctrl+Shift+P`)
2. Search for "Terminal: Select Default Profile"
3. Choose your desired profile

## MCP

Chat can use configured MCP servers to interact with external services, such as databases or 3rd party APIs.

<AccordionGroup>
  <Accordion title="Toggle MCP Servers" icon="server">
    Toggle available MCP servers. Respects auto-run configuration.
  </Accordion>
</AccordionGroup>

Learn more about [Model Context Protocol](/en/context/model-context-protocol) and explore available servers in the [MCP directory](/en/tools).

## Advanced options

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Automatically apply edits without manual confirmation.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Automatically execute terminal commands and accept edits. Useful for running test suites and verifying changes.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Configure allow lists to specify which tools can execute automatically. Allow lists provide better security by explicitly defining permitted operations.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Automatically resolve linter errors and warnings when encountered by Agent.
  </Accordion>
</AccordionGroup>



# Background Agents
Source: https://docs.cursor.com/en/background-agent

Asynchronous remote agents in Cursor

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

With background agents, spawn asynchronous agents that edit and run code in a remote environment. View their status, send follow-ups, or take over anytime.

## How to Use

You can access background agents in two ways:

1. **Background Agent Sidebar**: Use the background agent tab in the native Cursor sidebar to view all background agents associated with your account, search existing agents, and start new ones.
2. **Background Agent Mode**: Hit <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd> to trigger background agent mode in the UI.

After submitting a prompt, select your agent from the list to view status and enter the machine.

<Note>
  <p className="!mb-0">
    Background agents require data retention on the order of a few days.
  </p>
</Note>

## Setup

Background agents run in an isolated ubuntu-based machine by default. Agents have internet access and can install packages.

#### GitHub connection

Background agents clone your repo from GitHub and work on a separate branch, pushing to your repo for easy handoff.

Grant read-write privileges to your repo (and any dependent repos or submodules). We'll support other providers (GitLab, BitBucket, etc) in the future.

##### IP Allow List Configuration

If your organization uses GitHub's IP allow list feature, you'll need to configure access for background agents. See the [GitHub integration documentation](/en/integrations/github#ip-allow-list-configuration) for complete setup instructions including contact information and IP addresses.

#### Base Environment Setup

For advanced cases, set up the environment yourself. Get an IDE instance connected to the remote machine. Set up your machine, install tools and packages, then take a snapshot. Configure runtime settings:

* Install command runs before an agent starts and installs runtime dependencies. This might mean running `npm install` or `bazel build`.
* Terminals run background processes while the agent works - like starting a web server or compiling protobuf files.

For the most advanced cases, use a Dockerfile for machine setup. The dockerfile lets you set up system-level dependencies: install specific compiler versions, debuggers, or switch the base OS image. Don't `COPY` the entire project - we manage the workspace and check out the correct commit. Still handle dependency installation in the install script.

Enter any required secrets for your dev environment - they're stored encrypted-at-rest (using KMS) in our database and provided in the background agent environment.

The machine setup lives in `.cursor/environment.json`, which can be committed in your repo (recommended) or stored privately. The setup flow guides you through creating `environment.json`.

#### Maintenance Commands

When setting up a new machine, we start from the base environment, then run the `install` command from your `environment.json`. This command is what a developer would run when switching branches - install any new dependencies.

For most people, the `install` command is `npm install` or `bazel build`.

To ensure fast machine startup, we cache disk state after the `install` command runs. Design it to run multiple times. Only disk state persists from the `install` command - processes started here won't be alive when the agent starts.

#### Startup Commands

After running `install`, the machine starts and we run the `start` command followed by starting any `terminals`. This starts processes that should be alive when the agent runs.

The `start` command can often be skipped. Use it if your dev environment relies on docker - put `sudo service docker start` in the `start` command.

`terminals` are for app code. These terminals run in a `tmux` session available to you and the agent. For example, many website repos put `npm run watch` as a terminal.

#### The `environment.json` Spec

The `environment.json` file can look like:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Run Next.js",
      "command": "npm run dev"
    }
  ]
}
```

Formally, the spec is [defined here](https://www.cursor.com/schemas/environment.schema.json).

## Models

Only [Max Mode](/en/context/max-mode)-compatible models are available for background agents.

## Pricing

Learn more about [Background Agent pricing](/en/account/pricing#background-agent).

## Security

Background Agents are available in Privacy Mode. We never train on your code and only retain code for running the agent. [Learn more about Privacy mode](https://www.cursor.com/privacy-overview).

What you should know:

1. Grant read-write privileges to our GitHub app for repos you want to edit. We use this to clone the repo and make changes.
2. Your code runs inside our AWS infrastructure in isolated VMs and is stored on VM disks while the agent is accessible.
3. The agent has internet access.
4. The agent auto-runs all terminal commands, letting it iterate on tests. This differs from the foreground agent, which requires user approval for every command. Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks, tricking the agent to upload code to malicious websites. See [OpenAI's explanation about risks of prompt injection for background agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. If privacy mode is disabled, we collect prompts and dev environments to improve the product.
6. If you disable privacy mode when starting a background agent, then enable it during the agent's run, the agent continues with privacy mode disabled until it completes.

## Dashboard settings

Workspace admins can configure additional settings from the Background Agents tab on the dashboard.

### Defaults Settings

* **Default model** – the model used when a run does not specify one. Pick any model that supports Max Mode.
* **Default repository** – when empty, agents ask the user to choose a repo. Supplying a repo here lets users skip that step.
* **Base branch** – the branch agents fork from when creating pull requests. Leave blank to use the repository’s default branch.

### Security Settings

All security options require admin privileges.

* **User restrictions** – choose *None* (all members can start background agents) or *Allow list*. When set to *Allow list* you specify exactly which teammates can create agents.
* **Team follow-ups** – when on, anyone in the workspace can add follow-up messages to an agent someone else started. Turn it off to restrict follow-ups to the agent owner and admins.
* **Display agent summary** – controls whether Cursor shows the agent’s file-diff images and code snippets. Disable this if you prefer not to expose file paths or code in the sidebar.
* **Display agent summary in external channels** – extends the previous toggle to Slack or any external channel you’ve connected.

Changes save instantly and affect new agents immediately.



# Add Follow-up
Source: https://docs.cursor.com/en/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
Send an additional instruction to a running background agent.




# Agent Conversation
Source: https://docs.cursor.com/en/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
Retrieve the conversation history of a background agent.

If the background agent has been deleted, you cannot access the conversation.



# Agent Status
Source: https://docs.cursor.com/en/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
Get the current status and results of a specific background agent.




# API Key Info
Source: https://docs.cursor.com/en/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
Retrieve metadata about the API key used for authentication.




# Delete an Agent
Source: https://docs.cursor.com/en/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
Permanently delete a background agent and its associated resources.




# Launch an Agent
Source: https://docs.cursor.com/en/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
Start a new background agent to work on your repository.




# List Agents
Source: https://docs.cursor.com/en/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
Retrieve a paginated list of all background agents for the authenticated user.




# List Models
Source: https://docs.cursor.com/en/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
Retrieve a list of recommended models for background agents.

If you want to provide the background agent's model during creation, you can use this endpoint to see a list of recommended models.

In that case, we also recommend having an "Auto" option, in which you would not provide a model name to the creation endpoint,
and we will pick the most appropriate model.



# List GitHub Repositories
Source: https://docs.cursor.com/en/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Retrieve a list of GitHub repositories accessible to the authenticated user.

<Warning>
  **This endpoint has very strict rate limits.**

  Limit requests to **1 / user / minute**, and **30 / user / hour.**

  This request can take tens of seconds to respond for users with access to many repositories.

  Make sure to handle this information not being available gracefully.
</Warning>



# Overview
Source: https://docs.cursor.com/en/background-agent/api/overview

Programmatically create and manage background agents that work on your repositories


# Background Agents API

<Badge variant="beta">Beta</Badge>

The Background Agents API allows you to programmatically create and manage AI-powered coding agents that work autonomously on your repositories.
You can use the API to automatically respond to user feedback, fix bugs, update docs, and much more!

<Info>
  Background Agents API is currently in beta, we'd love your feedback on it!
</Info>

## Key features

* **Autonomous code generation** - Create agents that can understand your prompt and make changes to your codebase
* **Repository integration** - Work directly with GitHub repositories
* Follow-up prompts - Add additional instructions to running agents
* **Usage-based pricing** - Pay only for the tokens you use
* **Scalable** - Support for up to 256 active agents per API key

## Quick start

### 1. Get your API key

**Navigate** to [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations) to create your API key.

### 2. Start using the API

All API endpoints are relative to:

```
https://api.cursor.com
```

See the [API reference](/en/background-agent/api/launch-an-agent) for a detailed list of endpoints.

## Authentication

All API requests require authentication using a Bearer token:

```
Authorization: Bearer YOUR_API_KEY
```

API keys are created in the [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations). Keys are scoped to your account and grant permission to create and manage agents (subject to your plan limits and repository access).

## Pricing

The API is currently in beta with the same pricing as Background Agents. Pricing may change as we scale the service. See [Background Agent pricing](/en/account/pricing#background-agent).

## Next steps

* Read the main [Background Agents overview](/en/background-agent) to understand environments, permissions, and workflows.
* Try Background Agents from [web & mobile](/en/background-agent/web-and-mobile).
* Join the discussion in [Discord #background-agent](https://discord.gg/jfgpZtYpmb) or email [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com).



# Webhooks
Source: https://docs.cursor.com/en/background-agent/api/webhooks

Receive real-time notifications about background agent status changes


# Webhooks

When you create an agent with a webhook URL, Cursor will send HTTP POST requests to notify you about status changes. Currently, only `statusChange` events are supported, specifically when an agent encounters an `ERROR` or `FINISHED` state.

## Webhook verification

To ensure the webhook requests are authentically from Cursor, verify the signature included with each request:

### Headers

Each webhook request includes the following headers:

* **`X-Webhook-Signature`** – Contains the HMAC-SHA256 signature in the format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – A unique identifier for this delivery (useful for logging)
* **`X-Webhook-Event`** – The event type (currently only `statusChange`)
* **`User-Agent`** – Always set to `Cursor-Agent-Webhook/1.0`

### Signature verification

To verify the webhook signature, compute the expected signature and compare it with the received signature:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' + 
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Always use the raw request body (before any parsing) when computing the signature.

## Payload format

The webhook payload is sent as JSON with the following structure:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "Added README.md with installation instructions"
}
```

Note that some fields are optional and will only be included when available.

## Best practices

* **Verify signatures** – Always verify the webhook signature to ensure the request is from Cursor
* **Handle retries** – Webhooks may be retried if your endpoint returns an error status code
* **Return quickly** – Return a 2xx status code as soon as possible
* **Use HTTPS** – Always use HTTPS URLs for webhook endpoints in production
* **Store raw payloads** – Store the raw webhook payload for debugging and future verification



# Web & Mobile
Source: https://docs.cursor.com/en/background-agent/web-and-mobile

Run coding agents from any device with seamless handoff to desktop

## Overview

Cursor's Agent on web brings a powerful coding assistant to every device. Whether you're on your phone during a walk, or working in your web browser, you can now kick off powerful coding agents that work in the background.
When they're done, pick up their work inside Cursor, review and merge changes, or share links with your team to collaborate.

Get started at [cursor.com/agents](https://cursor.com/agents).

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Cursor web agent interface" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

## Getting started

### Quick setup

1. **Visit the web app**: Go to [cursor.com/agents](https://cursor.com/agents) on any device
2. **Sign in**: Log in with your Cursor account
3. **Connect GitHub**: Link your GitHub account to access repositories
4. **Start your first agent**: Type in a task and watch the agent get to work

### Mobile installation

For the best mobile experience, install Cursor as a Progressive Web App (PWA):

* **iOS**: Open [cursor.com/agents](https://cursor.com/agents) in Safari, tap the share button, then "Add to Home Screen"
* **Android**: Open the URL in Chrome, tap the menu, then "Add to Home Screen" or "Install App"

<Tip>
  Installing as a PWA provides a native-feeling experience with: - Full-screen
  interface - Faster startup times - App icon on your home screen
</Tip>

## Working across devices

The Web and Mobile Agent is designed to work with your desktop workflow; click "Open in Cursor" to continue the agent's work in your IDE.

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Review and handoff" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

### Team collaboration

* **Shared access**: Share links with team members to collaborate on agent runs.
* **Review process**: Collaborators can review diffs and provide feedback.
* **Pull request management**: Create, review, and merge pull requests directly from the web interface.

### Slack integration

Trigger agents directly from Slack by mentioning `@Cursor`, and when starting agents from web or mobile, opt to receive Slack notifications upon completion.

<Card title="Use Cursor in Slack" icon="slack" href="/en/slack">
  Learn more about setting up and using the Slack integration, including
  triggering agents and receiving notifications.
</Card>

## Pricing

Web & mobile agents use the same pricing model as Background Agents.

Learn more about [Background Agent pricing](/en/account/pricing#background-agent).

## Troubleshooting

<AccordionGroup>
  <Accordion title="Agent runs are not starting">
    * Ensure you're logged in and have connected your GitHub account. - Check
      that you have the necessary repository permissions - You will also need to
      be on a Pro Trial or paid plan with usage based pricing enabled. To enable
      usage based pricing, go to your
      [Dashboard](https://www.cursor.com/dashboard?tab=settings) settings tab.
  </Accordion>

  <Accordion title="Can't see agent runs on mobile">
    Try refreshing the page or clearing your browser cache. Ensure you're using
    the same account across devices.
  </Accordion>

  <Accordion title="Slack integration not working">
    Verify that your workspace admin has installed the Cursor Slack app and that
    you have the proper permissions.
  </Accordion>
</AccordionGroup>



# Bugbot
Source: https://docs.cursor.com/en/bugbot

AI code review for pull requests

Bugbot reviews pull requests and identifies bugs, security issues, and code quality problems.

<Tip>
  Bugbot includes a free tier: every user gets a limited number of free PR reviews each month. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to a 14‑day free Pro trial for unlimited reviews (subject to standard abuse guardrails).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot leaving comments on a PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

## How it works

Bugbot analyzes PR diffs and leaves comments with explanations and fix suggestions. It runs automatically on each PR update or manually when triggered.

* Runs **automatic reviews** on every PR update
* **Manual trigger** by commenting `cursor review` or `bugbot run` on any PR
* **Fix in Cursor** links open issues directly in Cursor
* **Fix in Web** links open issues directly in [cursor.com/agents](https://cursor.com/agents)

## Setup

Requires Cursor admin access and GitHub org admin access.

1. Go to [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Navigate to the Bugbot tab
3. Click `Connect GitHub` (or `Manage Connections` if already connected)
4. Follow the GitHub installation flow
5. Return to the dashboard to enable Bugbot on specific repositories

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot GitHub setup" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

## Configuration

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Repository settings

    Enable or disable Bugbot per repository from your installations list. Bugbot runs only on PRs you author.

    ### Personal settings

    * Run **only when mentioned** by commenting `cursor review` or `bugbot run`
    * Run **only once** per PR, skipping subsequent commits
  </Tab>

  <Tab title="Team">
    ### Repository settings

    Team admins can enable Bugbot per repository, configure allow/deny lists for reviewers, and set:

    * Run **only once** per PR per installation, skipping subsequent commits
    * **Disable inline reviews** to prevent Bugbot from leaving comments directly on code lines

    Bugbot runs for all contributors to enabled repositories, regardless of team membership.

    ### Personal settings

    Team members can override settings for their own PRs:

    * Run **only when mentioned** by commenting `cursor review` or `bugbot run`
    * Run **only once** per PR, skipping subsequent commits
    * **Enable reviews on draft PRs** to include draft pull requests in automatic reviews
  </Tab>
</Tabs>

### Analytics

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot dashboard" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

## Rules

Create `.cursor/BUGBOT.md` files to provide project-specific context for reviews. Bugbot always includes the root `.cursor/BUGBOT.md` file and any additional files found while traversing upward from changed files.

```
project/
  .cursor/BUGBOT.md          # Always included (project-wide rules)
  backend/
    .cursor/BUGBOT.md        # Included when reviewing backend files
    api/
      .cursor/BUGBOT.md      # Included when reviewing API files
  frontend/
    .cursor/BUGBOT.md        # Included when reviewing frontend files
```

<AccordionGroup>
  <Accordion title="Example .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Project review guidelines

    ## Security focus areas

    - Validate user input in API endpoints
    - Check for SQL injection vulnerabilities in database queries
    - Ensure proper authentication on protected routes

    ## Architecture patterns

    - Use dependency injection for services
    - Follow the repository pattern for data access
    - Implement proper error handling with custom error classes

    ## Common issues

    - Memory leaks in React components (check useEffect cleanup)
    - Missing error boundaries in UI components
    - Inconsistent naming conventions (use camelCase for functions)

    ```
  </Accordion>
</AccordionGroup>

## Pricing

Bugbot offers two tiers: **Free** and **Pro**.

### Free tier

Every user gets a limited number of free PR reviews each month. For teams, each team member gets their own free reviews. When you reach the limit, reviews pause until your next billing cycle. You can upgrade anytime to the 14‑day free Pro trial for unlimited reviews.

### Pro tier

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Flat rate

    \$40 per month for unlimited Bugbot reviews on up to 200 PRs per month across all repositories.

    ### Getting started

    Subscribe through your account settings.
  </Tab>

  <Tab title="Teams">
    ### Per-user billing

    Teams pay \$40 per user per month for unlimited reviews.

    We count a user as someone who authored PRs reviewed by Bugbot in a month.

    All licenses are relinquished at the start of each billing cycle, and will be assigned out on a first-come, first-served basis. If a user doesn't author any PRs reviewed by Bugbot in a month, the seat can be used by another user.

    ### Seat limits

    Team admins can set maximum Bugbot seats per month to control costs.

    ### Getting started

    Subscribe through your team dashboard to enable billing.

    ### Abuse guardrails

    In order to prevent abuse, we have a pooled cap of 200 pull requests per month for every Bugbot license. If you need more than 200 pull requests per month, please contact us at [hi@cursor.com](mailto:hi@cursor.com) and we'll be happy to help you out.

    For example, if your team has 100 users, your organization will initially be able to review 20,000 pull requests per month. If you reach that limit naturally, please reach out to us and we'll be happy to increase the limit.
  </Tab>
</Tabs>

## Troubleshooting

If Bugbot isn't working:

1. **Enable verbose mode** by commenting `cursor review verbose=true` or `bugbot run verbose=true` for detailed logs and request ID
2. **Check permissions** to verify Bugbot has repository access
3. **Verify installation** to confirm the GitHub app is installed and enabled

Include the request ID from verbose mode when reporting issues.

## FAQ

<AccordionGroup>
  <Accordion title="Is Bugbot privacy-mode compliant?">
    Yes, Bugbot follows the same privacy compliance as Cursor and processes data identically to other Cursor requests.
  </Accordion>

  <Accordion title="What happens when I hit the free tier limit?">
    When you reach your monthly free tier limit, Bugbot reviews pause until your next billing cycle. You can upgrade to the 14‑day free Pro trial for unlimited reviews (subject to standard abuse guardrails).
  </Accordion>
</AccordionGroup>

```
```



# Code Review
Source: https://docs.cursor.com/en/cli/cookbook/code-review

Build a GitHub Actions workflow that uses Cursor CLI to automatically review pull requests and provide feedback

This tutorial shows you how to set up code review using Cursor CLI in GitHub Actions. The workflow will analyze pull requests, identify issues, and post feedback as comments.

<Tip>
  For most users, we recommend using [Bugbot](/en/bugbot) instead. Bugbot provides managed automated code review with no setup required. This CLI approach is useful to explore capabilities and for advanced customization.
</Tip>

<div className="space-y-4">
  <Expandable title="full workflow file">
    ```yaml cursor-code-review.yml theme={null}
    name: Code Review

    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]

    permissions:
      pull-requests: write
      contents: read
      issues: write

    jobs:
      code-review:
        runs-on: ubuntu-latest
        # Skip automated code review for draft PRs
        if: github.event.pull_request.draft == false
        steps:
          - name: Checkout repository
            uses: actions/checkout@v4
            with:
              fetch-depth: 0
              ref: ${{ github.event.pull_request.head.sha }}

          - name: Install Cursor CLI
            run: |
              curl https://cursor.com/install -fsS | bash
              echo "$HOME/.cursor/bin" >> $GITHUB_PATH

          - name: Configure git identity
            run: |
              git config user.name "Cursor Agent"
              git config user.email "cursoragent@cursor.com"

          - name: Perform automated code review
            env:
              CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
              MODEL: gpt-5
              GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
              BLOCKING_REVIEW: ${{ vars.BLOCKING_REVIEW || 'false' }}
            run: |
              cursor-agent --force --model "$MODEL" --output-format=text --print 'You are operating in a GitHub Actions runner performing automated code review. The gh CLI is available and authenticated via GH_TOKEN. You may comment on pull requests.

              Context:
              - Repo: ${{ github.repository }}
              - PR Number: ${{ github.event.pull_request.number }}
              - PR Head SHA: ${{ github.event.pull_request.head.sha }}
              - PR Base SHA: ${{ github.event.pull_request.base.sha }}
              - Blocking Review: ${{ env.BLOCKING_REVIEW }}

              Objectives:
              1) Re-check existing review comments and reply resolved when addressed.
              2) Review the current PR diff and flag only clear, high-severity issues.
              3) Leave very short inline comments (1-2 sentences) on changed lines only and a brief summary at the end.

              Procedure:
              - Get existing comments: gh pr view --json comments
              - Get diff: gh pr diff
              - Get changed files with patches to compute inline positions: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/files --paginate --jq '.[] | {filename,patch}'
              - Compute exact inline anchors for each issue (file path + diff position). Comments MUST be placed inline on the changed line in the diff, not as top-level comments.
              - Detect prior top-level "no issues" style comments authored by this bot (match bodies like: "✅ no issues", "No issues found", "LGTM").
              - If CURRENT run finds issues and any prior "no issues" comments exist:
                - Prefer to remove them to avoid confusion:
                  - Try deleting top-level issue comments via: gh api -X DELETE repos/${{ github.repository }}/issues/comments/<comment_id>
                  - If deletion isn't possible, minimize them via GraphQL (minimizeComment) or edit to prefix "[Superseded by new findings]".
                - If neither delete nor minimize is possible, reply to that comment: "⚠️ Superseded: issues were found in newer commits".
              - If a previously reported issue appears fixed by nearby changes, reply: ✅ This issue appears to be resolved by the recent changes
              - Analyze ONLY for:
                - Null/undefined dereferences
                - Resource leaks (unclosed files or connections)
                - Injection (SQL/XSS)
                - Concurrency/race conditions
                - Missing error handling for critical operations
                - Obvious logic errors with incorrect behavior
                - Clear performance anti-patterns with measurable impact
                - Definitive security vulnerabilities
              - Avoid duplicates: skip if similar feedback already exists on or near the same lines.

              Commenting rules:
              - Max 10 inline comments total; prioritize the most critical issues
              - One issue per comment; place on the exact changed line
              - All issue comments MUST be inline (anchored to a file and line/position in the PR diff)
              - Natural tone, specific and actionable; do not mention automated or high-confidence
              - Use emojis: 🚨 Critical 🔒 Security ⚡ Performance ⚠️ Logic ✅ Resolved ✨ Improvement

              Submission:
              - If there are NO issues to report and an existing top-level comment indicating "no issues" already exists (e.g., "✅ no issues", "No issues found", "LGTM"), do NOT submit another comment. Skip submission to avoid redundancy.
              - If there are NO issues to report and NO prior "no issues" comment exists, submit one brief summary comment noting no issues.
              - If there ARE issues to report and a prior "no issues" comment exists, ensure that prior comment is deleted/minimized/marked as superseded before submitting the new review.
              - If there ARE issues to report, submit ONE review containing ONLY inline comments plus an optional concise summary body. Use the GitHub Reviews API to ensure comments are inline:
                - Build a JSON array of comments like: [{ "path": "<file>", "position": <diff_position>, "body": "..." }]
                - Submit via: gh api repos/${{ github.repository }}/pulls/${{ github.event.pull_request.number }}/reviews -f event=COMMENT -f body="$SUMMARY" -f comments='[$COMMENTS_JSON]'
              - Do NOT use: gh pr review --approve or --request-changes

              Blocking behavior:
              - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
              - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
              - Always set CRITICAL_ISSUES_FOUND at the end
              '

          - name: Check blocking review results
            if: env.BLOCKING_REVIEW == 'true'
            run: |
              echo "Checking for critical issues..."
              echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

              if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
                echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
                exit 1
              else
                echo "✅ No blocking issues found."
              fi
    ```
  </Expandable>

  <Frame>
    <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=31c7e4b54276532df8010645686ebbbc" alt="Automated code review in action showing inline comments on a pull request" data-og-width="2920" width="2920" data-og-height="1272" height="1272" data-path="images/cli/cookbook/code-review/comment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=25e552210fa8425a10ff459bf4cd6006 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=234bf271bc595e763549c4f04d2e6fbb 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=b6f6d1444de7fe0197e3d35fa35955e8 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=300314314f5071b77f735460be33985f 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=10e4db857ee84c55d17222cef492611d 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/comment.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=e65add70ffebfeb9ad05c9bb19a5f4e1 2500w" />
  </Frame>
</div>

## Configure authentication

[Set up your API key and repository secrets](/en/cli/github-actions#authentication) to authenticate Cursor CLI in GitHub Actions.

## Set up agent permissions

Create a configuration file to control what actions the agent can perform. This prevents unintended operations like pushing code or creating pull requests.

Create `.cursor/cli.json` in your repository root:

```json  theme={null}
{
  "permissions": {
    "deny": [
      "Shell(git push)",
      "Shell(gh pr create)",
      "Write(**)"
    ]
  }
}
```

This configuration allows the agent to read files and use the GitHub CLI for comments, but prevents it from making changes to your repository. See the [permissions reference](/en/cli/reference/permissions) for more configuration options.

## Build the GitHub Actions workflow

Now let's build the workflow step by step.

### Set up the workflow trigger

Create `.github/workflows/cursor-code-review.yml` and configure it to run on pull requests:

```yaml  theme={null}
name: Cursor Code Review

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  code-review:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    
    steps:
```

### Checkout the repository

Add the checkout step to access the pull request code:

```yaml  theme={null}
- name: Checkout repository
  uses: actions/checkout@v4
  with:
    fetch-depth: 0
    ref: ${{ github.event.pull_request.head.sha }}
```

### Install Cursor CLI

Add the CLI installation step:

```yaml  theme={null}
- name: Install Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH
```

### Configure the review agent

Before implementing the full review step, let's understand the anatomy of our review prompt. This section outlines how we want the agent to behave:

**Objective**:
We want the agent to review the current PR diff and flag only clear, high-severity issues, then leave very short inline comments (1-2 sentences) on changed lines only with a brief summary at the end. This keeps the signal-to-noise ratio balanced.

**Format**:
We want comments that are short and to the point. We use emojis to make scanning comments easier, and we want a high-level summary of the full review at the end.

**Submission**:
When the review is done, we want the agent to include a short comment based on what was found during the review. The agent should submit one review containing inline comments plus a concise summary.

**Edge cases**:
We need to handle:

* Existing comments being resolved: The agent should mark them as done when addressed
* Avoid duplicates: The agent should skip commenting if similar feedback already exists on or near the same lines

**Final prompt**:
The complete prompt combines all these behavioral requirements to create focused, actionable feedback

Now let's implement the review agent step:

```yaml  theme={null}
- name: Perform code review
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
    GH_TOKEN: ${{ github.token }}
  run: |
    cursor-agent --force --model "$MODEL" --output-format=text --print "You are operating in a GitHub Actions runner performing automated code review. The gh CLI is available and authenticated via GH_TOKEN. You may comment on pull requests.
    
    Context:
    - Repo: ${{ github.repository }}
    - PR Number: ${{ github.event.pull_request.number }}
    - PR Head SHA: ${{ github.event.pull_request.head.sha }}
    - PR Base SHA: ${{ github.event.pull_request.base.sha }}
    
    Objectives:
    1) Re-check existing review comments and reply resolved when addressed
    2) Review the current PR diff and flag only clear, high-severity issues
    3) Leave very short inline comments (1-2 sentences) on changed lines only and a brief summary at the end
    
    Procedure:
    - Get existing comments: gh pr view --json comments
    - Get diff: gh pr diff
    - If a previously reported issue appears fixed by nearby changes, reply: ✅ This issue appears to be resolved by the recent changes
    - Avoid duplicates: skip if similar feedback already exists on or near the same lines
    
    Commenting rules:
    - Max 10 inline comments total; prioritize the most critical issues
    - One issue per comment; place on the exact changed line
    - Natural tone, specific and actionable; do not mention automated or high-confidence
    - Use emojis: 🚨 Critical 🔒 Security ⚡ Performance ⚠️ Logic ✅ Resolved ✨ Improvement
    
    Submission:
    - Submit one review containing inline comments plus a concise summary
    - Use only: gh pr review --comment
    - Do not use: gh pr review --approve or --request-changes"
```

```text  theme={null}
.
├── .cursor/
│   └── cli.json
├── .github/
│   └── workflows/
│       └── cursor-code-review.yml
```

## Test your reviewer

Create a test pull request to verify the workflow works and the agent posts review comments with emoji feedback.

<Frame>
  <img src="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=aa989eb5b7520e6718a48afd8daa70d9" alt="Pull request showing automated review comments with emojis and inline feedback on specific lines" data-og-width="1250" width="1250" data-og-height="704" height="704" data-path="images/cli/cookbook/code-review/github-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=280&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=9f2e324beb1cccb8052dcd0682323e47 280w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=560&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f08497ddb17921f4bb4638ef4eec3379 560w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=840&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=3c869c0ed8eb8b5743dd3821e57cd406 840w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1100&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=19e98ed953f4cc17b2c578ce543cf88d 1100w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=1650&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=4d9f47472af81254bd09b5f6234fc97f 1650w, https://mintcdn.com/cursor/KODIqSiRh6LRGwl9/images/cli/cookbook/code-review/github-actions.png?w=2500&fit=max&auto=format&n=KODIqSiRh6LRGwl9&q=85&s=f3af19e3edd7f8bbbb77ba6566d8e183 2500w" />
</Frame>

## Next steps

You now have a working automated code review system. Consider these enhancements:

* Set up additional workflows for [fixing CI failures](/en/cli/cookbook/fix-ci)
* Configure different review levels for different branches
* Integrate with your team's existing code review process
* Customize the agent's behavior for different file types or directories

<Expandable title="Advanced: Blocking reviews">
  You can configure the workflow to fail if critical issues are found, preventing the pull request from being merged until addressed.

  **Add blocking behavior to the prompt**

  First, update your review agent step to include the `BLOCKING_REVIEW` environment variable and add this blocking behavior to the prompt:

  ```
  Blocking behavior:
  - If BLOCKING_REVIEW is true and any 🚨 or 🔒 issues were posted: echo "CRITICAL_ISSUES_FOUND=true" >> $GITHUB_ENV
  - Otherwise: echo "CRITICAL_ISSUES_FOUND=false" >> $GITHUB_ENV
  - Always set CRITICAL_ISSUES_FOUND at the end
  ```

  **Add the blocking check step**

  Then add this new step after your code review step:

  ```yaml  theme={null}
        - name: Check blocking review results
          if: env.BLOCKING_REVIEW == 'true'
          run: |
            echo "Checking for critical issues..."
            echo "CRITICAL_ISSUES_FOUND: ${CRITICAL_ISSUES_FOUND:-unset}"

            if [ "${CRITICAL_ISSUES_FOUND:-false}" = "true" ]; then
              echo "❌ Critical issues found and blocking review is enabled. Failing the workflow."
              exit 1
            else
              echo "✅ No blocking issues found."
            fi
  ```
</Expandable>



# Fix CI Failures
Source: https://docs.cursor.com/en/cli/cookbook/fix-ci

Fix CI issues for a repository by using Cursor CLI in GitHub Actions

Fix CI failures using Cursor CLI in GitHub Actions. This workflow analyzes failures, makes targeted fixes, and creates a fix branch with a quick-create PR link.

This workflow monitors a specific workflow by name. Update the `workflows` list to match your actual CI workflow name.

<CodeGroup>
  ```yaml auto-fix-ci.yml theme={null}
  name: Fix CI Failures

  on:
    workflow_run:
      workflows: [Test]
      types: [completed]

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    attempt-fix:
      if: >-
        ${{ github.event.workflow_run.conclusion == 'failure' && github.event.workflow_run.name != 'Fix CI Failures' }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Fix CI failure
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: ci-fix
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - Workflow Run ID: ${{ github.event.workflow_run.id }}
            - Workflow Run URL: ${{ github.event.workflow_run.html_url }}
            - Fix Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end CI fix flow driven by the failing PR, creating a separate persistent fix branch and proposing a quick-create PR back into the original PR's branch.

            # Requirements:
            1) Identify the PR associated with the failed workflow run and determine its base and head branches. Let HEAD_REF be the PR's head branch (the contributor/origin branch).
            2) Maintain a persistent fix branch for this PR head using the Fix Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            3) Attempt to resolve the CI failure by making minimal, targeted edits consistent with the repo's style. Keep changes scoped and safe.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the CI fix and includes an inline compare link to quick-create a PR.

            # Inputs and conventions:
            - Use `gh api`, `gh run view`, `gh pr view`, `gh pr diff`, `gh pr list`, `gh run download`, and git commands as needed to discover the failing PR and branches.
            - Avoid duplicate comments; if a previous bot comment exists, update it instead of posting a new one.
            - If no actionable fix is possible, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent fix branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Secret Audit
Source: https://docs.cursor.com/en/cli/cookbook/secret-audit

Audit secrets for a repository by using Cursor CLI in GitHub Actions

Audit your repository for security vulnerabilities and secrets exposure using Cursor CLI. This workflow scans for potential secrets, detects risky workflow patterns, and proposes security fixes.

<CodeGroup>
  ```yaml auto-secret-audit.yml theme={null}
  name: Secrets Audit

  on:
    schedule:
      - cron: "0 4 * * *"
    workflow_dispatch:

  permissions:
    contents: write
    pull-requests: write
    actions: read

  jobs:
    secrets-audit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Scan and propose hardening
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: audit
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
             - Hardening Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Perform a repository secrets exposure and workflow hardening audit on a schedule, and propose minimal safe fixes.

            # Requirements:
            1) Scan for potential secrets in tracked files and recent history; support allowlist patterns if present (e.g., .gitleaks.toml).
            2) Detect risky workflow patterns: unpinned actions, overbroad permissions, unsafe pull_request_target usage, secrets in forked PR contexts, deprecated insecure commands, missing permissions blocks.
            3) Maintain a persistent branch for this run using the Hardening Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) Propose minimal edits: redact literals where safe, add ignore rules, pin actions to SHA, reduce permissions, add guardrails to workflows, and add a SECURITY_LOG.md summarizing changes and remediation guidance.
            5) Push to origin.
            6) If there is at least one open PR in the repo, post or update a single natural-language comment (1–2 sentences) on the most recently updated open PR that briefly explains the hardening changes and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update an existing bot comment if present. If no changes or no open PRs, post nothing.

            # Inputs and conventions:
            - Use `gh` to list PRs and to post comments. Avoid duplicate comments.

            # Deliverables when updates occur:
             - Pushed commits to the persistent hardening branch for this run.
            - A single natural-language PR comment with the compare link above (only if an open PR exists).
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Translate Keys
Source: https://docs.cursor.com/en/cli/cookbook/translate-keys

Translate keys for a repository by using Cursor CLI in GitHub Actions

Manage translation keys for internationalization using Cursor CLI. This workflow detects new or changed i18n keys in pull requests and fills missing translations without overwriting existing ones.

<CodeGroup>
  ```yaml auto-translate-keys.yml theme={null}
  name: Translate Keys

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    i18n:
      if: ${{ !startsWith(github.head_ref, 'translate/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git identity
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Propose i18n updates
          env:
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            MODEL: gpt-5
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: translate
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs directly.

            # Context:
            - Repo: ${{ github.repository }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Head Ref: ${{ github.head_ref }}
            - Translate Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Detect i18n keys added or changed in the PR and fill only missing locales in message files. Never overwrite existing translations.

            # Requirements:
            1) Determine changed keys by inspecting the PR diff (source files and messages files).
            2) Compute missing keys per locale using the source/canonical locale as truth.
            3) Add entries only for missing keys. Preserve all existing values untouched.
            4) Validate JSON formatting and schemas.
            5) Maintain a persistent translate branch for this PR head using the Translate Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            6) Post or update a single PR comment on the original PR written in natural language (1–2 sentences) that briefly explains what was updated and why, and includes an inline compare link to quick-create a PR.
            7) Avoid duplicate comments; update a previous bot comment if present.
            8) If no changes are necessary, make no commits and post no comment.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes.

            # Deliverables when updates occur:
            - Pushed commits to the persistent translate branch for this PR head.
            - A single natural-language PR comment on the original PR with the compare link above.
            " --force --model "$MODEL" --output-format=text

  ```
</CodeGroup>



# Update Docs
Source: https://docs.cursor.com/en/cli/cookbook/update-docs

Update docs for a repository by using Cursor CLI in GitHub Actions

Update documentation using Cursor CLI in GitHub Actions. Two approaches: full agent autonomy or deterministic workflow with agent-only file modifications.

<CodeGroup>
  ```yaml auto-update-docs.yml theme={null}
  name: Update Docs

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Update docs
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available. You have write access to repository contents and can comment on pull requests, but you must not create or edit PRs.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}
            - Docs Branch Prefix: ${{ env.BRANCH_PREFIX }}

            # Goal:
            - Implement an end-to-end docs update flow driven by incremental changes to the original PR.

            # Requirements:
            1) Determine what changed in the original PR and, if there have been multiple pushes, compute the incremental diffs since the last successful docs update.
            2) Update only the relevant docs based on those incremental changes.
            3) Maintain the persistent docs branch for this PR head using the Docs Branch Prefix from Context. Create it if missing, update it otherwise, and push changes to origin.
            4) You do NOT have permission to create PRs. Instead, post or update a single natural-language PR comment (1–2 sentences) that briefly explains the docs updates and includes an inline compare link to quick-create a PR

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes and derive incremental ranges since the last docs update.
            - Do not attempt to create or edit PRs directly. Use the compare link format above.
            - Keep changes minimal and consistent with repo style. If no doc updates are necessary, make no changes and post no comment.

            # Deliverables when updates occur:
            - Pushed commits to the persistent docs branch for this PR head.
            - A single natural-language PR comment on the original PR that includes the inline compare link above. Avoid posting duplicates; update a previous bot comment if present.
            " --force --model "$MODEL" --output-format=text
  ```

  ```yaml auto-update-docs-deterministic.yml theme={null}
  name: Update Docs

  on:
    pull_request:
      types: [opened, synchronize, reopened, ready_for_review]

  permissions:
    contents: write
    pull-requests: write

  jobs:
    auto-docs:
      if: ${{ !startsWith(github.head_ref, 'docs/') }}
      runs-on: ubuntu-latest
      steps:
        - name: Checkout repository
          uses: actions/checkout@v4
          with:
            fetch-depth: 0

        - name: Install Cursor CLI
          run: |
            curl https://cursor.com/install -fsS | bash
            echo "$HOME/.cursor/bin" >> $GITHUB_PATH

        - name: Configure git
          run: |
            git config user.name "Cursor Agent"
            git config user.email "cursoragent@cursor.com"

        - name: Generate docs updates (no commit/push/comment)
          env:
            MODEL: gpt-5
            CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
          run: |
            cursor-agent -p "You are operating in a GitHub Actions runner.

            The GitHub CLI is available as `gh` and authenticated via `GH_TOKEN`. Git is available.

            IMPORTANT: Do NOT create branches, commit, push, or post PR comments. Only modify files in the working directory as needed. A later workflow step is responsible for publishing changes and commenting on the PR.

            # Context:
            - Repo: ${{ github.repository }}
            - Owner: ${{ github.repository_owner }}
            - PR Number: ${{ github.event.pull_request.number }}
            - Base Ref: ${{ github.base_ref }}
            - Head Ref: ${{ github.head_ref }}

            # Goal:
            - Update repository documentation based on incremental changes introduced by this PR.

            # Requirements:
            1) Determine what changed in the original PR (use `gh pr diff` and git history as needed). If an existing persistent docs branch `${{ env.BRANCH_PREFIX }}/${{ github.head_ref }}` exists, you may use it as a read-only reference point to understand prior updates.
            2) Update only the relevant docs based on those changes. Keep edits minimal and consistent with repo style.
            3) Do NOT commit, push, create branches, or post PR comments. Leave the working tree with updated files only; a later step will publish.

            # Inputs and conventions:
            - Use `gh pr diff` and git history to detect changes and focus documentation edits accordingly.
            - If no doc updates are necessary, make no changes and produce no output.

            # Deliverables when updates occur:
            - Modified documentation files in the working directory only (no commits/pushes/comments).
            " --force --model "$MODEL" --output-format=text

        - name: Publish docs branch
          id: publish_docs
          env:
            BRANCH_PREFIX: docs
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |
            echo "changes_published=false" >> "$GITHUB_OUTPUT"

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"

            # Ensure we are on a local branch that we can push
            git fetch origin --prune

            # Create/switch to the persistent docs branch, keeping current working tree changes
            git checkout -B "$DOCS_BRANCH"

            # Stage and detect changes
            git add -A
            if git diff --staged --quiet; then
              echo "No docs changes to publish. Skipping commit/push."
              exit 0
            fi

            COMMIT_MSG="docs: update for PR #${PR_NUMBER} (${HEAD_REF} @ $(git rev-parse --short HEAD))"
            git commit -m "$COMMIT_MSG"
            git push --set-upstream origin "$DOCS_BRANCH"

            echo "changes_published=true" >> "$GITHUB_OUTPUT"

        - name: Post or update PR comment
          if: steps.publish_docs.outputs.changes_published == 'true'
          env:
            GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            BRANCH_PREFIX: docs
            REPO: ${{ github.repository }}
            BASE_REF: ${{ github.base_ref }}
            HEAD_REF: ${{ github.head_ref }}
            PR_NUMBER: ${{ github.event.pull_request.number }}
          run: |

            DOCS_BRANCH="${BRANCH_PREFIX}/${HEAD_REF}"
            COMPARE_URL="https://github.com/${REPO}/compare/${BASE_REF}...${DOCS_BRANCH}?quick_pull=1&title=docs%3A+updates+for+PR+%23${PR_NUMBER}"

            COMMENT_FILE="${RUNNER_TEMP}/auto-docs-comment.md"
            {
              echo "Cursor updated docs branch: \`${DOCS_BRANCH}\`"
              echo "You can now [view the diff and quick-create a PR to merge these docs updates](${COMPARE_URL})."
              echo
              echo "_This comment will be updated on subsequent runs as the PR changes._"
              echo
              echo "<!-- auto-update-docs-split -->"
            } > "$COMMENT_FILE"

            # If editing the last bot comment fails (older gh), fall back to creating a new comment
            if gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE" --edit-last; then
              echo "Updated existing PR comment."
            else
              gh pr comment "$PR_NUMBER" --body-file "$COMMENT_FILE"
              echo "Posted new PR comment."
            fi
  ```
</CodeGroup>



# GitHub Actions
Source: https://docs.cursor.com/en/cli/github-actions

Learn how to use Cursor CLI in GitHub Actions and other continuous integration systems

Use Cursor CLI in GitHub Actions and other CI/CD systems to automate development tasks.

## GitHub Actions integration

Basic setup:

```yaml  theme={null}
- name: Install Cursor CLI
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Run Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Your prompt here" --model gpt-5
```

## Cookbook examples

See our cookbook examples for practical workflows: [updating documentation](/en/cli/cookbook/update-docs) and [fixing CI issues](/en/cli/cookbook/fix-ci).

## Other CI systems

Use Cursor CLI in any CI/CD system with:

* **Shell script execution** (bash, zsh, etc.)
* **Environment variables** for API key configuration
* **Internet connectivity** to reach Cursor's API

## Autonomy levels

Choose your agent's autonomy level:

### Full autonomy approach

Give the agent complete control over git operations, API calls, and external interactions. Simpler setup, requires more trust.

**Example:** In our [Update Documentation](/en/cli/cookbook/update-docs) cookbook, the first workflow lets the agent:

* Analyze PR changes
* Create and manage git branches
* Commit and push changes
* Post comments on pull requests
* Handle all error scenarios

```yaml  theme={null}
- name: Update docs (full autonomy)
  run: |
    cursor-agent -p "You have full access to git, GitHub CLI, and PR operations. 
    Handle the entire docs update workflow including commits, pushes, and PR comments."
```

### Restricted autonomy approach

<Note>
  We recommend using this approach with **permission-based restrictions** for production CI workflows. This gives you the best of both worlds: the agent can intelligently handle complex analysis and file modifications while critical operations remain deterministic and auditable.
</Note>

Limit agent operations while handling critical steps in separate workflow steps. Better control and predictability.

**Example:** The second workflow in the same cookbook restricts the agent to only file modifications:

```yaml  theme={null}
- name: Generate docs updates (restricted)
  run: |
    cursor-agent -p "IMPORTANT: Do NOT create branches, commit, push, or post PR comments. 
    Only modify files in the working directory. A later workflow step handles publishing."

- name: Publish docs branch (deterministic)
  run: |
    # Deterministic git operations handled by CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: update for PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Post PR comment (deterministic)  
  run: |
    # Deterministic PR commenting handled by CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs updated"
```

### Permission-based restrictions

Use [permission configurations](/en/cli/reference/permissions) to enforce restrictions at the CLI level:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

## Authentication

### Generate your API key

First, [generate an API key](/en/cli/reference/authentication#api-key-authentication) from your Cursor dashboard.

### Configure repository secrets

Store your Cursor API key securely in your repository:

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name it `CURSOR_API_KEY`
5. Paste your API key as the value
6. Click **Add secret**

### Use in workflows

Set your `CURSOR_API_KEY` environment variable:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```



# Using Headless CLI
Source: https://docs.cursor.com/en/cli/headless

Learn how to write scripts using Cursor CLI for automated code analysis, generation, and modification

Use Cursor CLI in scripts and automation workflows for code analysis, generation, and refactoring tasks.

## How it works

Use [print mode](/en/cli/using#non-interactive-mode) (`-p, --print`) for non-interactive scripting and automation.

### File modification in scripts

Combine `--print` with `--force` to modify files in scripts:

```bash  theme={null}

# Enable file modifications in print mode
cursor-agent -p --force "Refactor this code to use modern ES6+ syntax"


# Without --force, changes are only proposed, not applied
cursor-agent -p "Add JSDoc comments to this file"  # Won't modify files


# Batch processing with actual file changes
find src/ -name "*.js" | while read file; do
  cursor-agent -p --force "Add comprehensive JSDoc comments to $file"
done
```

<Warning>
  The `--force` flag allows the agent to make direct file changes without confirmation
</Warning>

## Setup

See [Installation](/en/cli/installation) and [Authentication](/en/cli/reference/authentication) for complete setup details.

```bash  theme={null}

# Install Cursor CLI
curl https://cursor.com/install -fsS | bash


# Set API key for scripts  
export CURSOR_API_KEY=your_api_key_here
cursor-agent -p "Analyze this code"
```

## Example scripts

Use different output formats for different script needs. See [Output format](/en/cli/reference/output-format) for details.

### Searching the codebase

Use `--output-format text` for readable responses:

```bash  theme={null}
#!/bin/bash

# Simple codebase question

cursor-agent -p --output-format text "What does this codebase do?"
```

### Automated code review

Use `--output-format json` for structured analysis:

```bash  theme={null}
#!/bin/bash

# simple-code-review.sh - Basic code review script

echo "Starting code review..."


# Review recent changes
cursor-agent -p --force --output-format text \
  "Review the recent code changes and provide feedback on:
  - Code quality and readability  
  - Potential bugs or issues
  - Security considerations
  - Best practices compliance

  Provide specific suggestions for improvement and write to review.txt"

if [ $? -eq 0 ]; then
  echo "✅ Code review completed successfully"
else
  echo "❌ Code review failed"
  exit 1
fi
```

### Real-time progress tracking

Use `--output-format stream-json` for real-time progress tracking:

```bash  theme={null}
#!/bin/bash

# stream-progress.sh - Track progress in real-time

echo "🚀 Starting stream processing..."


# Track progress in real-time
accumulated_text=""
tool_count=0
start_time=$(date +%s)

cursor-agent -p --force --output-format stream-json \
  "Analyze this project structure and create a summary report in analysis.txt" | \
  while IFS= read -r line; do
    
    type=$(echo "$line" | jq -r '.type // empty')
    subtype=$(echo "$line" | jq -r '.subtype // empty')
    
    case "$type" in
      "system")
        if [ "$subtype" = "init" ]; then
          model=$(echo "$line" | jq -r '.model // "unknown"')
          echo "🤖 Using model: $model"
        fi
        ;;
        
      "assistant")
        # Accumulate streaming text deltas
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        
        # Show live progress
        printf "\r📝 Generating: %d chars" ${#accumulated_text}
        ;;
        
      "tool_call")
        if [ "$subtype" = "started" ]; then
          tool_count=$((tool_count + 1))
          
          # Extract tool information
          if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // "unknown"')
            echo -e "\n🔧 Tool #$tool_count: Creating $path"
          elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
            path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // "unknown"')
            echo -e "\n📖 Tool #$tool_count: Reading $path"
          fi
          
        elif [ "$subtype" = "completed" ]; then
          # Extract and show tool results
          if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.linesCreated // 0')
            size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.fileSize // 0')
            echo "   ✅ Created $lines lines ($size bytes)"
          elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
            lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.totalLines // 0')
            echo "   ✅ Read $lines lines"
          fi
        fi
        ;;
        
      "result")
        duration=$(echo "$line" | jq -r '.duration_ms // 0')
        end_time=$(date +%s)
        total_time=$((end_time - start_time))
        
        echo -e "\n\n🎯 Completed in ${duration}ms (${total_time}s total)"
        echo "📊 Final stats: $tool_count tools, ${#accumulated_text} chars generated"
        ;;
    esac
  done
```



# Installation
Source: https://docs.cursor.com/en/cli/installation

Install and update Cursor CLI

## Installation

### macOS, Linux and Windows (WSL)

Install Cursor CLI with a single command:

```bash  theme={null}
curl https://cursor.com/install -fsS | bash
```

### Verification

After installation, verify that Cursor CLI is working correctly:

```bash  theme={null}
cursor-agent --version
```

## Post-installation setup

1. **Add \~/.local/bin to your PATH:**

   For bash:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

   For zsh:

   ```bash  theme={null}
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

2. **Start using Cursor Agent:**
   ```bash  theme={null}
   cursor-agent
   ```

## Updates

Cursor CLI will try to auto-update by default to ensure you always have the latest version.

To manually update Cursor CLI to the latest version:

```bash  theme={null}
cursor-agent update

# or 
cursor-agent upgrade
```

Both commands will update Cursor Agent to the latest version.



# MCP
Source: https://docs.cursor.com/en/cli/mcp

Use MCP servers with cursor-agent to connect external tools and data sources

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

## Overview

The Cursor CLI supports [Model Context Protocol (MCP)](/en/context/mcp) servers, allowing you to connect external tools and data sources to `cursor-agent`. **MCP in the CLI uses the same configuration as the editor** - any MCP servers you've configured will work seamlessly with both.

<Card title="Learn about MCP" icon="link" href="/en/context/mcp">
  New to MCP? Read the complete guide on configuration, authentication, and available servers
</Card>

## CLI commands

Use the `cursor-agent mcp` command to manage MCP servers:

### List configured servers

View all configured MCP servers and their current status:

```bash  theme={null}
cursor-agent mcp list
```

This shows:

* Server names and identifiers
* Connection status (connected/disconnected)
* Configuration source (project or global)
* Transport method (stdio, HTTP, SSE)

### List available tools

View tools provided by a specific MCP server:

```bash  theme={null}
cursor-agent mcp list-tools <identifier>
```

This displays:

* Tool names and descriptions
* Required and optional parameters
* Parameter types and constraints

### Login to MCP server

Authenticate with an MCP server configured in your `mcp.json`:

```bash  theme={null}
cursor-agent mcp login <identifier>
```

### Disable MCP server

Remove an MCP server from the local approved list:

```bash  theme={null}
cursor-agent mcp disable <identifier>
```

## Using MCP with Agent

Once you have MCP servers configured (see the [main MCP guide](/en/context/mcp) for setup), `cursor-agent` automatically discovers and uses available tools when relevant to your requests.

```bash  theme={null}

# Check what MCP servers are available
cursor-agent mcp list


# See what tools a specific server provides
cursor-agent mcp list-tools playwright


# Use cursor-agent - it automatically uses MCP tools when helpful
cursor-agent --prompt "Navigate to google.com and take a screenshot of the search page"
```

The CLI follows the same configuration precedence as the editor (project → global → nested), automatically discovering configurations from parent directories.

## Related

<CardGroup cols={2}>
  <Card title="MCP Overview" icon="link" href="/en/context/mcp">
    Complete MCP guide: setup, configuration, and authentication
  </Card>

  <Card title="Available MCP Tools" icon="table" href="/en/tools">
    Browse pre-built MCP servers you can use
  </Card>
</CardGroup>



# Cursor CLI
Source: https://docs.cursor.com/en/cli/overview

Get started with Cursor CLI to code in your terminal

Cursor CLI lets you interact with AI agents directly from your terminal to write, review, and modify code. Whether you prefer an interactive terminal interface or print automation for scripts and CI pipelines, the CLI provides powerful coding assistance right where you work.

```bash  theme={null}

# Install
curl https://cursor.com/install -fsS | bash


# Run interactive session
cursor-agent
```

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/cli-overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b323547dd61e985df8c0d6179c1492bd" autoPlay loop muted playsInline controls data-path="images/cli/cli-overview.mp4" />
</Frame>

<Info>
  Cursor CLI is currently in beta, we'd love your feedback on it!
</Info>

### Interactive mode

Start a conversational session with the agent to describe your goals, review proposed changes, and approve commands:

```bash  theme={null}

# Start interactive session
cursor-agent


# Start with initial prompt
cursor-agent "refactor the auth module to use JWT tokens"
```

### Non-interactive mode

Use print mode for non-interactive scenarios like scripts, CI pipelines, or automation:

```bash  theme={null}

# Run with specific prompt and model
cursor-agent -p "find and fix performance issues" --model "gpt-5"


# Use with git changes included for review
cursor-agent -p "review these changes for security issues" --output-format text
```

### Sessions

Resume previous conversations to maintain context across multiple interactions:

```bash  theme={null}

# List all previous chats
cursor-agent ls


# Resume latest conversation  
cursor-agent resume


# Resume specific conversation
cursor-agent --resume="chat-id-here"
```



# Authentication
Source: https://docs.cursor.com/en/cli/reference/authentication

Authenticate Cursor CLI using browser flow or API keys

Cursor CLI supports two authentication methods: browser-based login (recommended) and API keys.

## Browser authentication (recommended)

Use the browser flow for the easiest authentication experience:

```bash  theme={null}

# Log in using browser flow
cursor-agent login


# Check authentication status
cursor-agent status


# Log out and clear stored authentication
cursor-agent logout
```

The login command will open your default browser and prompt you to authenticate with your Cursor account. Once completed, your credentials are securely stored locally.

## API key authentication

For automation, scripts, or CI/CD environments, use API key authentication:

### Step 1: Generate an API key

Generate an API key in your Cursor dashboard under Integrations > User API Keys.

### Step 2: Set the API key

You can provide the API key in two ways:

**Option 1: Environment variable (recommended)**

```bash  theme={null}
export CURSOR_API_KEY=your_api_key_here
cursor-agent "implement user authentication"
```

**Option 2: Command line flag**

```bash  theme={null}
cursor-agent --api-key your_api_key_here "implement user authentication"
```

## Authentication status

Check your current authentication status:

```bash  theme={null}
cursor-agent status
```

This command will display:

* Whether you're authenticated
* Your account information
* Current endpoint configuration

## Troubleshooting

* **"Not authenticated" errors:** Run `cursor-agent login` or ensure your API key is correctly set
* **SSL certificate errors:** Use the `--insecure` flag for development environments
* **Endpoint issues:** Use the `--endpoint` flag to specify a custom API endpoint



# Configuration
Source: https://docs.cursor.com/en/cli/reference/configuration

Agent CLI configuration reference for cli-config.json

Configure the Agent CLI using the `cli-config.json` file.

## File location

<div class="full-width-table">
  | Type    | Platform    | Path                                       |
  | :------ | :---------- | :----------------------------------------- |
  | Global  | macOS/Linux | `~/.cursor/cli-config.json`                |
  | Global  | Windows     | `$env:USERPROFILE\.cursor\cli-config.json` |
  | Project | All         | `<project>/.cursor/cli.json`               |
</div>

<Note>Only permissions can be configured at the project level. All other CLI settings must be set globally.</Note>

Override with environment variables:

* **`CURSOR_CONFIG_DIR`**: custom directory path
* **`XDG_CONFIG_HOME`** (Linux/BSD): uses `$XDG_CONFIG_HOME/cursor/cli-config.json`

## Schema

### Required fields

<div class="full-width-table">
  | Field               | Type      | Description                                                             |
  | :------------------ | :-------- | :---------------------------------------------------------------------- |
  | `version`           | number    | Config schema version (current: `1`)                                    |
  | `editor.vimMode`    | boolean   | Enable Vim keybindings (default: `false`)                               |
  | `permissions.allow` | string\[] | Permitted operations (see [Permissions](/en/cli/reference/permissions)) |
  | `permissions.deny`  | string\[] | Forbidden operations (see [Permissions](/en/cli/reference/permissions)) |
</div>

### Optional fields

<div class="full-width-table">
  | Field                    | Type    | Description                     |
  | :----------------------- | :------ | :------------------------------ |
  | `model`                  | object  | Selected model configuration    |
  | `hasChangedDefaultModel` | boolean | CLI-managed model override flag |
</div>

## Examples

### Minimal config

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

### Enable Vim mode

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": true },
  "permissions": { "allow": ["Shell(ls)"], "deny": [] }
}
```

### Configure permissions

```json  theme={null}
{
  "version": 1,
  "editor": { "vimMode": false },
  "permissions": {
    "allow": ["Shell(ls)", "Shell(echo)"],
    "deny": ["Shell(rm)"]
  }
}
```

See [Permissions](/en/cli/reference/permissions) for available permission types and examples.

## Troubleshooting

**Config errors**: Move the file aside and restart:

```bash  theme={null}
mv ~/.cursor/cli-config.json ~/.cursor/cli-config.json.bad
```

**Changes don't persist**: Ensure valid JSON and write permissions. Some fields are CLI-managed and may be overwritten.

## Notes

* Pure JSON format (no comments)
* CLI performs self-repair for missing fields
* Corrupted files are backed up as `.bad` and recreated
* Permission entries are exact strings (see [Permissions](/en/cli/reference/permissions) for details)



# Output format
Source: https://docs.cursor.com/en/cli/reference/output-format

Output schema for text, JSON and stream-JSON formats

The Cursor Agent CLI provides multiple output formats with the `--output-format` option when combined with `--print`. These formats include structured formats for programmatic use (`json`, `stream-json`) and a simplified text format for human-readable progress tracking.

<Note>
  The default `--output-format` is `stream-json`. This option is only valid when printing (`--print`) or when print mode is inferred (non-TTY stdout or piped stdin).
</Note>

## JSON format

The `json` output format emits a single JSON object (followed by a newline) when the run completes successfully. Deltas and tool events are not emitted; text is aggregated into the final result.

On failure, the process exits with a non-zero code and writes an error message to stderr. No well-formed JSON object is emitted in failure cases.

### Success response

When successful, the CLI outputs a JSON object with the following structure:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<full assistant text>",
  "session_id": "<uuid>",
  "request_id": "<optional request id>"
}
```

<div class="full-width-table">
  | Field             | Description                                                         |
  | ----------------- | ------------------------------------------------------------------- |
  | `type`            | Always `"result"` for terminal results                              |
  | `subtype`         | Always `"success"` for successful completions                       |
  | `is_error`        | Always `false` for successful responses                             |
  | `duration_ms`     | Total execution time in milliseconds                                |
  | `duration_api_ms` | API request time in milliseconds (currently equal to `duration_ms`) |
  | `result`          | Complete assistant response text (concatenation of all text deltas) |
  | `session_id`      | Unique session identifier                                           |
  | `request_id`      | Optional request identifier (may be omitted)                        |
</div>

## Stream JSON format

The `stream-json` output format emits newline-delimited JSON (NDJSON). Each line contains a single JSON object representing a real-time event during execution.

The stream ends with a terminal `result` event on success. On failure, the process exits with a non-zero code and the stream may end early without a terminal event; an error message is written to stderr.

### Event types

#### System initialization

Emitted once at the beginning of each session:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/absolute/path",
  "session_id": "<uuid>",
  "model": "<model display name>",
  "permissionMode": "default"
}
```

<Note>
  Future fields like `tools` and `mcp_servers` may be added to this event.
</Note>

#### User message

Contains the user's input prompt:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

#### Assistant text delta

Emitted multiple times as the assistant generates its response. These events contain incremental text chunks:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<delta chunk>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Concatenate all `message.content[].text` values in order to reconstruct the complete assistant response.
</Note>

#### Tool call events

Tool calls are tracked with start and completion events:

**Tool call started:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Tool call completed:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "file contents...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

#### Tool call types

**Read file tool:**

* **Started**: `tool_call.readToolCall.args` contains `{ "path": "file.txt" }`
* **Completed**: `tool_call.readToolCall.result.success` contains file metadata and content

**Write file tool:**

* **Started**: `tool_call.writeToolCall.args` contains `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **Completed**: `tool_call.writeToolCall.result.success` contains `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Other tools:**

* May use `tool_call.function` structure with `{ "name": "tool_name", "arguments": "..." }`

#### Terminal result

The final event emitted on successful completion:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<full assistant text>",
  "session_id": "<uuid>",
  "request_id": "<optional request id>"
}
```

### Example sequence

Here's a representative NDJSON sequence showing the typical flow of events:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Read README.md and create a summary"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"I'll "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"read the README.md file"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Project\n\nThis is a sample project...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" and create a summary"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README Summary\n\nThis project contains...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"I'll read the README.md file and create a summary","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

## Text format

The `text` output format provides a simplified, human-readable stream of agent actions. Instead of detailed JSON events, it outputs concise text descriptions of what the agent is doing in real-time.

This format is useful for monitoring agent progress without the overhead of parsing structured data, making it ideal for logging, debugging, or simple progress tracking.

### Example output

```
Read file
Edited file
Ran terminal command
Created new file
```

Each action appears on a new line as the agent performs it, providing immediate feedback on the agent's progress through the task.

## Implementation notes

* Each event is emitted as a single line terminated by `\n`
* `thinking` events are suppressed in print mode and will not appear in either output format
* Field additions may occur over time in a backward-compatible way (consumers should ignore unknown fields)
* The stream format provides real-time updates, while the JSON format waits for completion before outputting results
* Concatenate all `assistant` message deltas to reconstruct the complete response
* Tool call IDs can be used to correlate start/completion events
* Session IDs remain consistent throughout a single agent execution



# Parameters
Source: https://docs.cursor.com/en/cli/reference/parameters

Complete command reference for Cursor Agent CLI

## Global options

Global options can be used with any command:

<div class="full-width-table">
  | Option                     | Description                                                                                                         |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
  | `-v, --version`            | Output the version number                                                                                           |
  | `-a, --api-key <key>`      | API key for authentication (can also use `CURSOR_API_KEY` env var)                                                  |
  | `-p, --print`              | Print responses to console (for scripts or non-interactive use). Has access to all tools, including write and bash. |
  | `--output-format <format>` | Output format (only works with `--print`): `text`, `json`, or `stream-json` (default: `stream-json`)                |
  | `-b, --background`         | Start in background mode (open composer picker on launch)                                                           |
  | `--fullscreen`             | Enable fullscreen mode                                                                                              |
  | `--resume [chatId]`        | Resume a chat session                                                                                               |
  | `-m, --model <model>`      | Model to use                                                                                                        |
  | `-f, --force`              | Force allow commands unless explicitly denied                                                                       |
  | `-h, --help`               | Display help for command                                                                                            |
</div>

## Commands

<div class="full-width-table">
  | Command           | Description                               | Usage                                           |
  | ----------------- | ----------------------------------------- | ----------------------------------------------- |
  | `login`           | Authenticate with Cursor                  | `cursor-agent login`                            |
  | `logout`          | Sign out and clear stored authentication  | `cursor-agent logout`                           |
  | `status`          | Check authentication status               | `cursor-agent status`                           |
  | `mcp`             | Manage MCP servers                        | `cursor-agent mcp`                              |
  | `update\|upgrade` | Update Cursor Agent to the latest version | `cursor-agent update` or `cursor-agent upgrade` |
  | `ls`              | Resume a chat session                     | `cursor-agent ls`                               |
  | `resume`          | Resume the latest chat session            | `cursor-agent resume`                           |
  | `help [command]`  | Display help for command                  | `cursor-agent help [command]`                   |
</div>

<Note>
  When no command is specified, Cursor Agent starts in interactive chat mode by default.
</Note>

## MCP

Manage MCP servers configured for Cursor Agent.

<div class="full-width-table">
  | Subcommand                | Description                                                      | Usage                                      |
  | ------------------------- | ---------------------------------------------------------------- | ------------------------------------------ |
  | `login <identifier>`      | Authenticate with an MCP server configured in `.cursor/mcp.json` | `cursor-agent mcp login <identifier>`      |
  | `list`                    | List configured MCP servers and their status                     | `cursor-agent mcp list`                    |
  | `list-tools <identifier>` | List available tools and their argument names for a specific MCP | `cursor-agent mcp list-tools <identifier>` |
</div>

All MCP commands support `-h, --help` for command-specific help.

## Arguments

When starting in chat mode (default behavior), you can provide an initial prompt:

**Arguments:**

* `prompt` — Initial prompt for the agent

## Getting help

All commands support the global `-h, --help` option to display command-specific help.



# Permissions
Source: https://docs.cursor.com/en/cli/reference/permissions

Permission types for controlling agent access to files and commands

Configure what the agent is allowed to do using permission tokens in your CLI configuration. Permissions are set in `~/.cursor/cli-config.json` (global) or `<project>/.cursor/cli.json` (project-specific).

## Permission types

### Shell commands

**Format:** `Shell(commandBase)`

Controls access to shell commands. The `commandBase` is the first token in the command line.

<div class="full-width-table">
  | Example      | Description                                        |
  | ------------ | -------------------------------------------------- |
  | `Shell(ls)`  | Allow running `ls` commands                        |
  | `Shell(git)` | Allow any `git` subcommand                         |
  | `Shell(npm)` | Allow npm package manager commands                 |
  | `Shell(rm)`  | Deny destructive file removal (commonly in `deny`) |
</div>

### File reads

**Format:** `Read(pathOrGlob)`

Controls read access to files and directories. Supports glob patterns.

<div class="full-width-table">
  | Example             | Description                             |
  | ------------------- | --------------------------------------- |
  | `Read(src/**/*.ts)` | Allow reading TypeScript files in `src` |
  | `Read(**/*.md)`     | Allow reading markdown files anywhere   |
  | `Read(.env*)`       | Deny reading environment files          |
  | `Read(/etc/passwd)` | Deny reading system files               |
</div>

### File writes

**Format:** `Write(pathOrGlob)`

Controls write access to files and directories. Supports glob patterns. When using in print mode, `--force` is required to write files.

<div class="full-width-table">
  | Example               | Description                           |
  | --------------------- | ------------------------------------- |
  | `Write(src/**)`       | Allow writing to any file under `src` |
  | `Write(package.json)` | Allow modifying package.json          |
  | `Write(**/*.key)`     | Deny writing private key files        |
  | `Write(**/.env*)`     | Deny writing environment files        |
</div>

## Configuration

Add permissions to the `permissions` object in your CLI configuration file:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Shell(ls)",
      "Shell(git)", 
      "Read(src/**/*.ts)",
      "Write(package.json)"
    ],
    "deny": [
      "Shell(rm)",
      "Read(.env*)",
      "Write(**/*.key)"
    ]
  }
}
```

## Pattern matching

* Glob patterns use `**`, `*`, and `?` wildcards
* Relative paths are scoped to the current workspace
* Absolute paths can target files outside the project
* Deny rules take precedence over allow rules



# Slash commands
Source: https://docs.cursor.com/en/cli/reference/slash-commands

Quick actions available within Cursor CLI sessions

<div class="full-width-table">
  | Command               | Description                                         |
  | --------------------- | --------------------------------------------------- |
  | `/model <model>`      | Set or list models                                  |
  | `/auto-run [state]`   | Toggle auto-run (default) or set \[on\|off\|status] |
  | `/new-chat`           | Start a new chat session                            |
  | `/vim`                | Toggle Vim keys                                     |
  | `/help [command]`     | Show help (/help \[cmd])                            |
  | `/feedback <message>` | Share feedback with the team                        |
  | `/resume <chat>`      | Resume a previous chat by folder name               |
  | `/copy-req-id`        | Copy last request ID                                |
  | `/logout`             | Sign out from Cursor                                |
  | `/quit`               | Exit                                                |
</div>



# Shell Mode
Source: https://docs.cursor.com/en/cli/shell-mode

Run shell commands directly from the CLI without leaving your conversation

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Shell Mode runs shell commands directly from the CLI without leaving your conversation. Use it for quick, non-interactive commands with safety checks and output displayed in the conversation.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/cli/shell-mode/cli-shell-mode.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5194392f1189eb1eba340d731e86bd5f" autoPlay loop muted playsInline controls data-path="images/cli/shell-mode/cli-shell-mode.mp4" />
</Frame>

## Command execution

Commands run in your login shell (`$SHELL`) with the CLI's working directory and environment. Chain commands to run in other directories:

```bash  theme={null}
cd subdir && npm test
```

## Output

<product_visual type="screenshot">
  Command output showing header with exit code, stdout/stderr display, and truncation controls
</product_visual>

Large outputs are truncated automatically and long-running processes timeout to maintain performance.

## Limitations

* Commands timeout after 30 seconds
* Long-running processes, servers, and interactive prompts are not supported
* Use short, non-interactive commands for best results

## Permissions

Commands are checked against your permissions and team settings before execution. See [Permissions](/en/cli/reference/permissions) for detailed configuration.

<product_visual type="screenshot">
  Decision banner showing approval options: Run, Reject/Propose, Add to allowlist, and Auto-run
</product_visual>

Admin policies may block certain commands, and commands with redirection cannot be allowlisted inline.

## Usage guidelines

Shell Mode works well for status checks, quick builds, file operations, and environment inspection.

Avoid long-running servers, interactive applications, and commands requiring input.

Each command runs independently - use `cd <dir> && ...` to run commands in other directories.

## Troubleshooting

* If a command hangs, cancel with <Kbd>Ctrl+C</Kbd> and add non-interactive flags
* When prompted for permissions, approve once or add to allowlist with <Kbd>Tab</Kbd>
* For truncated output, use <Kbd>Ctrl+O</Kbd> to expand
* To run in different directories, use `cd <dir> && ...` since changes don't persist
* Shell Mode supports zsh and bash from your `$SHELL` variable

## FAQ

<AccordionGroup>
  <Accordion title="Does `cd` persist across runs?">
    No. Each command runs independently. Use `cd <dir> && ...` to run commands in different directories.
  </Accordion>

  <Accordion title="Can I change the timeout?">
    No. Commands are limited to 30 seconds and this is not configurable.
  </Accordion>

  <Accordion title="Where are permissions configured?">
    Permissions are managed by CLI and team configuration. Use the decision banner to add commands to allowlists.
  </Accordion>

  <Accordion title="How do I exit Shell Mode?">
    Press <Kbd>Escape</Kbd> when the input is empty, <Kbd>Backspace</Kbd>/<Kbd>Delete</Kbd> on empty input, or <Kbd>Ctrl+C</Kbd> to clear and exit.
  </Accordion>
</AccordionGroup>



# Using Agent in CLI
Source: https://docs.cursor.com/en/cli/using

Prompt, review, and iterate effectively with Cursor CLI

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

## Prompting

Stating intent clearly is recommended for the best results. For example, you can use the prompt "do not write any code" to ensure that the agent won't edit any files. This is generally helpful when planning tasks before implementing them.

Agent currently has tools for file operations, searching, and running shell commands. More tools are being added, similar to the IDE agent.

## MCP

Agent supports [MCP (Model Context Protocol)](/en/tools/mcp) for extended functionality and integrations. The CLI will automatically detect and respect your `mcp.json` configuration file, enabling the same MCP servers and tools that you've configured for the IDE.

## Rules

The CLI agent supports the same [rules system](/en/context/rules) as the IDE. You can create rules in the `.cursor/rules` directory to provide context and guidance to the agent. These rules will be automatically loaded and applied based on their configuration, allowing you to customize the agent's behavior for different parts of your project or specific file types.

<Note>
  The CLI also reads `AGENTS.md` and `CLAUDE.md` at the project root (if present) and applies them as rules alongside `.cursor/rules`.
</Note>

## Working with Agent

### Navigation

Previous messages can be accessed using arrow up (<Kbd>ArrowUp</Kbd>) where you can cycle through them.

### Review

Review changes with <Kbd>Cmd+R</Kbd>. Press <Kbd>i</Kbd> to add follow-up instructions. Use <Kbd>ArrowUp</Kbd>/<Kbd>ArrowDown</Kbd> to scroll, and <Kbd>ArrowLeft</Kbd>/<Kbd>ArrowRight</Kbd> to switch files.

### Selecting context

Select files and folders to include in context with <Kbd>@</Kbd>. Free up space in the context window by running `/compress`. See [Summarization](/en/agent/chat/summarization) for details.

## History

Continue from an existing thread with `--resume [thread id]` to load prior context.

To resume the most recent conversation, use `cursor-agent resume`.

You can also run `cursor-agent ls` to see a list of previous conversations.

## Command approval

Before running terminal commands, CLI will ask you to approve (<Kbd>y</Kbd>) or reject (<Kbd>n</Kbd>) execution.

## Non-interactive mode

Use `-p` or `--print` to run Agent in non-interactive mode. This will print the response to the console.

With non-interactive mode, you can invoke Agent in a non-interactive way. This allows you to integrate it in scripts, CI pipelines, etc.

You can combine this with `--output-format` to control how the output is formatted. For example, use `--output-format json` for structured output that's easier to parse in scripts, or `--output-format text` for plain text output.

<Note>
  Cursor has full write access in non-interactive mode.
</Note>



# Keyboard Shortcuts
Source: https://docs.cursor.com/en/configuration/kbd

Keyboard shortcuts and keybindings in Cursor

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Overview of keyboard shortcuts in Cursor. See all keyboard shortcuts by pressing <Kbd>Cmd R</Kbd> then <Kbd>Cmd S</Kbd> or by opening command palette <Kbd>Cmd Shift P</Kbd> and searching for `Keyboard Shortcuts`.

Learn more about Keyboard Shortcuts in Cursor with [Key Bindings for VS Code](https://code.visualstudio.com/docs/getstarted/keybindings) as a baseline for Cursor's keybindings.

All Cursor keybindings, including Cursor-specific features, can be remapped in Keyboard Shortcuts settings.

## General

<div className="full-width-table equal-table-columns">
  | Shortcut               | Action                                  |
  | ---------------------- | --------------------------------------- |
  | <Kbd>Cmd I</Kbd>       | Toggle Sidepanel (unless bound to mode) |
  | <Kbd>Cmd L</Kbd>       | Toggle Sidepanel (unless bound to mode) |
  | <Kbd>Cmd E</Kbd>       | Background Agent control panel          |
  | <Kbd>Cmd .</Kbd>       | Mode Menu                               |
  | <Kbd>Cmd /</Kbd>       | Loop between AI models                  |
  | <Kbd>Cmd Shift J</Kbd> | Cursor settings                         |
  | <Kbd>Cmd ,</Kbd>       | General settings                        |
  | <Kbd>Cmd Shift P</Kbd> | Command palette                         |
</div>

## Chat

Shortcuts for the chat input box.

<div className="full-width-table equal-table-columns">
  | Shortcut                                             | Action                       |
  | ---------------------------------------------------- | ---------------------------- |
  | <Kbd>Return</Kbd>                                    | Nudge (default)              |
  | <Kbd>Ctrl Return</Kbd>                               | Queue message                |
  | <Kbd>Cmd Return</Kbd> when typing                    | Force send message           |
  | <Kbd>Cmd Shift Backspace</Kbd>                       | Cancel generation            |
  | <Kbd>Cmd Shift L</Kbd> with code selected            | Add selected code as context |
  | <Kbd>Cmd V</Kbd> with code or log in clipboard       | Add clipboard as context     |
  | <Kbd>Cmd Shift V</Kbd> with code or log in clipboard | Add clipboard to input box   |
  | <Kbd>Cmd Return</Kbd> with suggested changes         | Accept all changes           |
  | <Kbd>Cmd Backspace</Kbd>                             | Reject all changes           |
  | <Kbd>Tab</Kbd>                                       | Cycle to next message        |
  | <Kbd>Shift Tab</Kbd>                                 | Cycle to previous message    |
  | <Kbd>Cmd Opt /</Kbd>                                 | Model toggle                 |
  | <Kbd>Cmd N</Kbd> / <Kbd>Cmd R</Kbd>                  | New chat                     |
  | <Kbd>Cmd T</Kbd>                                     | New chat tab                 |
  | <Kbd>Cmd \[</Kbd>                                    | Previous chat                |
  | <Kbd>Cmd ]</Kbd>                                     | Next chat                    |
  | <Kbd>Cmd W</Kbd>                                     | Close chat                   |
  | <Kbd>Escape</Kbd>                                    | Unfocus field                |
</div>

## Inline Edit

<div className="full-width-table equal-table-columns">
  | Shortcut                       | Action             |
  | ------------------------------ | ------------------ |
  | <Kbd>Cmd K</Kbd>               | Open               |
  | <Kbd>Cmd Shift K</Kbd>         | Toggle input focus |
  | <Kbd>Return</Kbd>              | Submit             |
  | <Kbd>Cmd Shift Backspace</Kbd> | Cancel             |
  | <Kbd>Opt Return</Kbd>          | Ask quick question |
</div>

## Code Selection & Context

<div className="full-width-table equal-table-columns">
  | Shortcut                                              | Action                               |
  | ----------------------------------------------------- | ------------------------------------ |
  | <Kbd>@</Kbd>                                          | [@-symbols](/en/context/@-symbols/)  |
  | <Kbd>#</Kbd>                                          | Files                                |
  | <Kbd>/</Kbd>                                          | Shortcut Commands                    |
  | <Kbd>Cmd Shift L</Kbd>                                | Add selection to Chat                |
  | <Kbd>Cmd Shift K</Kbd>                                | Add selection to Edit                |
  | <Kbd>Cmd L</Kbd>                                      | Add selection to new chat            |
  | <Kbd>Cmd M</Kbd>                                      | Toggle file reading strategies       |
  | <Kbd>Cmd →</Kbd>                                      | Accept next word of suggestion       |
  | <Kbd>Cmd Return</Kbd>                                 | Search codebase in chat              |
  | Select code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd V</Kbd>       | Add copied reference code as context |
  | Select code, <Kbd>Cmd C</Kbd>, <Kbd>Cmd Shift V</Kbd> | Add copied code as text context      |
</div>

## Tab

<div className="full-width-table equal-table-columns">
  | Shortcut         | Action            |
  | ---------------- | ----------------- |
  | <Kbd>Tab</Kbd>   | Accept suggestion |
  | <Kbd>Cmd →</Kbd> | Accept next word  |
</div>

## Terminal

<div className="full-width-table equal-table-columns">
  | Shortcut              | Action                   |
  | --------------------- | ------------------------ |
  | <Kbd>Cmd K</Kbd>      | Open terminal prompt bar |
  | <Kbd>Cmd Return</Kbd> | Run generated command    |
  | <Kbd>Escape</Kbd>     | Accept command           |
</div>



# Shell Commands
Source: https://docs.cursor.com/en/configuration/shell

Install and use Cursor shell commands

Cursor provides command-line tools to open files and folders from your terminal. Install both the `cursor` and `code` commands to integrate Cursor with your development workflow.

## Installing CLI commands

Install the CLI commands through the Command Palette:

1. Open the Command Palette (Cmd/Ctrl + P)
2. Type "Install" to filter installation commands
3. Select and run `Install 'cursor' to shell`
4. Repeat and select `Install 'code' to shell`

<product_visual type="screenshot">
  Command Palette showing CLI installation options
</product_visual>

## Using the CLI commands

After installation, use either command to open files or folders in Cursor:

```bash  theme={null}

# Using the cursor command
cursor path/to/file.js
cursor path/to/folder/


# Using the code command (VS Code compatible)
code path/to/file.js
code path/to/folder/
```

## Command options

Both commands support these options:

* Open a file: `cursor file.js`
* Open a folder: `cursor ./my-project`
* Open multiple items: `cursor file1.js file2.js folder1/`
* Open in a new window: `cursor -n` or `cursor --new-window`
* Wait for the window to close: `cursor -w` or `cursor --wait`

## FAQ

<AccordionGroup>
  <Accordion title="What's the difference between cursor and code commands?">
    They're identical. The `code` command is provided for VS Code compatibility.
  </Accordion>

  <Accordion title="Do I need to install both commands?">
    No, install either or both based on preference.
  </Accordion>

  <Accordion title="Where are the commands installed?">
    Commands are installed in your system's default shell configuration file (e.g., `.bashrc`, `.zshrc`, or `.config/fish/config.fish`).
  </Accordion>
</AccordionGroup>



# Themes
Source: https://docs.cursor.com/en/configuration/themes

Customize the appearance of Cursor

Cursor supports both light and dark themes for your coding environment. Cursor inherits VS Code's theming capabilities - use any VS Code theme, create custom themes, and install theme extensions from the marketplace.

## Changing theme

1. Open the Command Palette (Cmd/Ctrl + P)
2. Type "theme" to filter commands
3. Select "Preferences: Color Theme"
4. Choose a theme

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de83bbba983509af2002e4dfafe703ff" alt="Theme selection menu in Cursor showing available color themes" data-og-width="3584" width="3584" data-og-height="2072" height="2072" data-path="images/config/themes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=85b365baa01a725becb482e69eed6292 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=46eb0bed7d0d98612968135d727ee838 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8629851793f4498e7639ee4347484c88 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ea75113e217cc84f99f8f6d63af34ade 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ec5b85b5a4464d2af801f92b317a7e31 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/config/themes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=54fc29efe263f9935ba3273675ced7be 2500w" />
</Frame>

## FAQ

<AccordionGroup>
  <Accordion title="Can I use my VS Code themes in Cursor?">
    Yes! Cursor is compatible with VS Code themes. Install any VS Code marketplace theme or copy custom theme files.
  </Accordion>

  <Accordion title="How do I create a custom theme?">
    Create custom themes like in VS Code. Use "Developer: Generate Color Theme From Current Settings" to start from current settings, or follow the VS Code theme authoring guide.
  </Accordion>
</AccordionGroup>



# @Code
Source: https://docs.cursor.com/en/context/@-symbols/@-code

Reference specific code snippets in Cursor using @Code

Reference specific code sections using the `@Code` symbol. This provides more granular control than [`@Files & Folders`](/en/context/@-symbols/@-files-and-folders), letting you select precise code snippets instead of entire files.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fba3d385441084e243cd168eee8c9a9a" data-og-width="1850" width="1850" data-og-height="948" height="948" data-path="images/context/symbols/@-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6337ef4855301fdfef729012783d3cee 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ef348ae46e4a51ee298a6a5fa356eebd 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40ec3857dd21120790037ea409fac80d 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=604bfeb6907e96da64b1f814681232c8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cee1a79d449a4d163f566a6013b69318 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-code.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d4bb99b85dfa5ad539e63c3670171abe 2500w" />
</Frame>



# @Cursor Rules
Source: https://docs.cursor.com/en/context/@-symbols/@-cursor-rules

Apply project-specific rules and guidelines

The `@Cursor Rules` symbol provides access to [project rules](/en/context/rules) and guidelines you've set up, letting you explicitly apply them to your context.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e2f45682a0b471e5726cd5452ab6bceb" data-og-width="1518" width="1518" data-og-height="973" height="973" data-path="images/context/symbols/@-rules.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6e67889ef0390f9be3c557247469c95b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1c22061fe8c8d000deeabbf404f1650d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a220fd7fbef492c2d523ed9e31324666 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44224ba38fd2a5460963b884c994d178 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=df766d5499d8b54ca4fa2211600515f6 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-rules.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a06393ddd0d85711ad72d7b8991946a5 2500w" />
</Frame>



# @Files & Folders
Source: https://docs.cursor.com/en/context/@-symbols/@-files-and-folders

Reference files and folders as context in Chat and Inline Edit

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

## Files

Reference entire files in Chat and Inline Edit by selecting `@Files & Folders` followed by the filename to search. You can also drag files from the sidebar directly into Agent to add as context.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8d46d3c961a3e898fd12c0cc1e1c8dce" data-og-width="2227" width="2227" data-og-height="1414" height="1414" data-path="images/context/symbols/@-files-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a3a78c7a6d2311a31efb941c40fbe11b 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bfe1eff4516dce93f789e560e92f14ad 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=462239ebfd0181acfe36d2f937f32ca6 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1a64cd3cc0a07825c51d70c40dfe72fd 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=64ea129f283dd98fd9814820d6684a99 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-files-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b40e591d3e500f06eeb32fac49d4f90c 2500w" />
</Frame>

## Folders

When referencing folders using `@Folders`, Cursor provides the folder path and overview of its contents to help the AI understand what's available.

<Tip>
  After selecting a folder, type `/` to navigate deeper and see all subfolders.
</Tip>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a102e1c1cb7180c3ec6a1356273839a" data-og-width="2150" width="2150" data-og-height="1367" height="1367" data-path="images/context/symbols/@-folders.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4b91de3b118c842aec8e1da04ca233d2 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fcba40013ff1349c28382151b52d5853 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=83cc5ac8db19a0d59de9a980c0ea10d7 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b87a80a369b62d48a2363a97a391de2 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29e93d39857f71ba7e00947e209514de 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-folders.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa9b88463b43fa482c0654a0a0b362ca 2500w" />
</Frame>

### Full folder content

Enable **Full Folder Content** in settings. When enabled, Cursor attempts to include all files from the folder in the context.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=ee37944a2e874a708b9d8281a063e580" data-og-width="1996" width="1996" data-og-height="296" height="296" data-path="images/context/symbols/folder-setting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=09520107c0518601c58f099ed119adab 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=748aecb97c43066f0be03416f9ed6ed0 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fd7e7c816092c9eed3182382fa77ff8f 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=91baab4860e0f671196607f3c364b4d8 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d2450ee2fcd6d8c59ba2412fad11121 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/folder-setting.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f4690bdb099c27092b9ddb6143bd8068 2500w" />
</Frame>

For large folders exceeding the context window, an outline view appears with a tooltip showing how many files were included while Cursor manages the available context space.

<Note>
  Using full folder content with [Max mode enabled](/en/context/max-mode)
  significantly increases request costs as more input tokens are consumed.
</Note>

## Context management

Large files and folders are automatically condensed to fit within context limits. See [file & folder condensation](/en/agent/chats/summarization#file--folder-condensation) for details.



# @Git
Source: https://docs.cursor.com/en/context/@-symbols/@-git

Reference Git changes and branch differences

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=dba4c696d66e1274b96bf3261c8d927b" data-og-width="1658" width="1658" data-og-height="932" height="932" data-path="images/context/symbols/@-git.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=69bf90d13f034275fb78ab48e71d25ac 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e8c89a03ebdd5a1c1a576c8555380957 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ec7309f9ec4364c4ac0d237a9977f23 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f2d82f1eb2be6275c8b91ae63e943ee7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4e27a0a13a731fc0fe85a85a327f9884 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-git.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=aa1acf93e5e87b7a81d766a52601960d 2500w" />
</Frame>

* `@Commit`: Reference current working state changes compared to the last commit. Shows all modified, added, and deleted files not yet committed.
* `@Branch`: Compare your current branch's changes with the main branch. Shows all commits and changes in your branch but not in main.



# @Link
Source: https://docs.cursor.com/en/context/@-symbols/@-link

Include web content by pasting URLs

When you paste a URL in Chat, Cursor automatically tags it as an `@Link` and fetches the content to use as context. This includes support for PDF documents - Cursor extracts and parses text content from any publicly accessible PDF URL.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d96b384a0480aba7981b6fbebee1fac8" data-og-width="1618" width="1618" data-og-height="1035" height="1035" data-path="images/context/symbols/@-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d251326cc25b2835488b1f25b05f2c4f 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d1b64f393d89cfc547c6e12ae7a6adef 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d5a2aa41c6a6affea03379adac5e76c8 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e94e2c0610eafea625996386374e8898 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=404333e65fa1c98e2e92fd941d2e8b92 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=63d9a66571fde75678b6fa0d0cbac44f 2500w" />
</Frame>

## Unlink

To use a URL as plain text without fetching its content:

* Click the tagged link and select `Unlink`
* Or paste while holding `Shift` to prevent automatic tagging

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5eca9b93aa4c2ba4f8d0f6a97a34052f" data-og-width="1212" width="1212" data-og-height="408" height="408" data-path="images/context/symbols/@-link-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=be5f171437d0d3c79ded195c7a387741 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5ca29084e45c832b6aa9015fcd5cf680 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=eb394772d364e392ff794c43ed1fbfcc 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5df343df91b3bf4aed9edb32fc192059 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a35df3274c439984b2072eb758d05fb1 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-link-menu.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a20f166b838435ade65084c844cc3c6a 2500w" />
</Frame>



# @Linter Errors
Source: https://docs.cursor.com/en/context/@-symbols/@-linter-errors

Access and reference linting errors in your codebase

`@Linter Errors` symbol automatically captures and provides context about linting errors and warnings from your currently active file. [Agent](/en/agent/overview) can see lint errors by default.

<Note>
  For linter errors to be visible, you need the appropriate language server
  installed and configured for your programming language. Cursor automatically
  detects and uses installed language servers, but you may need to install
  additional extensions or tools for specific languages.
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6ef34b3ae96a7d49695035cb5c3ac9f9" data-og-width="1590" width="1590" data-og-height="1017" height="1017" data-path="images/context/symbols/@-linter-errors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13e682f26536e5cb104142bcc7becbeb 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=cf3947376ee2e17f83c08809b23e864c 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=13d026063f9bc5e61c78740fee8eebc5 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29c834609d2f549b295be53cdbf7eec6 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b2131adda5b89685d7d7a26ed218fee 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-linter-errors.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9cd3c3e34cbee0f73fe478024018539 2500w" />
</Frame>



# @Past Chats
Source: https://docs.cursor.com/en/context/@-symbols/@-past-chats

Include summarized chats from history

When working on complex tasks in [Chat](/en/chat), you might need to reference context or decisions from previous conversations. The `@Past Chats` symbol includes summarized versions of previous chats as context.

Particularly useful when:

* You have a long Chat session with important context to reference
* You're starting a new related task and want continuity
* You want to share reasoning or decisions from a previous session

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=6839cf571e64e1ed10dd5dc270d4ac45" data-og-width="2340" width="2340" data-og-height="1485" height="1485" data-path="images/context/symbols/@-past-chats.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0278e6fdce8d8771ecd6f64faf5048db 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3a2d4722e90c1078c11fcd695993d84a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d46e21680b56820aef7a9baf34891e0 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f19f25e6988729059f40731378ce4fab 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=86f9457d09e7dd4578c8609fd3cff6b5 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-past-chats.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8efb9e097f9e434d0b7f03cac9b02396 2500w" />
</Frame>



# @Recent Changes
Source: https://docs.cursor.com/en/context/@-symbols/@-recent-changes

Include recently modified code as context

The `@Recent Changes` symbol includes recent code modifications as context in AI conversations.

* Changes are chronologically ordered
* Prioritizes the last 10 changes
* Respects `.cursorignore` settings

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e6968afeeed9e790121d8280f63b670d" data-og-width="1556" width="1556" data-og-height="996" height="996" data-path="images/context/symbols/@-recent-changes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=beae76f109d8eb29788ab3c90f72b831 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c4e6ad386c30f9546e1485ca4c14c0f2 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7d80d31e720b167408cd308204fa666a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=868a93753377dcb2d6820c748b9b17d7 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e84e94c4fe64f9e4270fd72883a4962d 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-recent-changes.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=139ffc703716759bb8b8c35e57bd6dbf 2500w" />
</Frame>



# @Web
Source: https://docs.cursor.com/en/context/@-symbols/@-web

Search the web for current information

With `@Web`, Cursor searches the web using [exa.ai](https://exa.ai) to find up-to-date information and add it as context. This includes the ability to parse PDF files from direct links.

<Note>
  Web search is disabled by default. Enable it in Settings → Features → Web
  Search.
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=17621610c12478f27190b96db57ca8de" data-og-width="1700" width="1700" data-og-height="1085" height="1085" data-path="images/context/symbols/@-web.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1be39cb8bbbfa22f2341635e7c5fe6d0 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=40b6aac5bee79bb5656024077bee7ece 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9a8515d8c9c5624135665a9545de32db 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8c7b721901f8cb82d39458ed054ee946 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=255c56da352f6faff0d92cf24f7dabb2 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/symbols/@-web.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=22561389d116bcbe01f5a860c0097b27 2500w" />
</Frame>




---

**Navigation:** [← Previous](./04-developers.md) | [Index](./index.md) | [Next →](./06-overview.md)