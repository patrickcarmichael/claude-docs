**Navigation:** [← Previous](./05-no-cors-headers.md) | [Index](./index.md) | [Next →](./07-working-with-ssl-certificates.md)

---

# Trusted IPs

Copy page

Ask AI about this page

Last updated September 15, 2025

Trusted IPs are available on [Enterprise plans](/docs/plans/enterprise)

Those with the [owner](/docs/rbac/access-roles#owner-role), [member](/docs/rbac/access-roles#member-role) and [admin](/docs/rbac/access-roles#admin-role) roles can manage Trusted IPs

With Trusted IPs [enabled](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips#managing-trusted-ips) at the level of your [project](/docs/projects/project-dashboard#settings), only visitors from an allowed IP address can access your deployment. The deployment URL will return `404` [No Deployment Found](/docs/errors/platform-error-codes#404:-deployment_not_found) for all other requests. Trusted IPs is configured by specifying a list of IPv4 addresses and IPv4 CIDR ranges.

Trusted IPs is suitable for customers who access Vercel deployments through a specific IP address. For example, limiting preview deployment access to your VPN. Trusted IPs can also be enabled in production, for example, to restrict incoming access to only requests through your external proxy.

![Enabling Trusted IPs.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Ftrusted-ips-dash-light.png&w=1920&q=75)![Enabling Trusted IPs.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Ftrusted-ips-dash-dark.png&w=1920&q=75)

Enabling Trusted IPs.

## [Trusted IPs security considerations](#trusted-ips-security-considerations)

The table below outlines key considerations and security implications when using Trusted IPs for your deployments on Vercel.

| Consideration | Description |
| --- | --- |
| General Considerations |  |
| Environment Configuration | Can be enabled for different environments. See [Understanding Deployment Protection by environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) |
| Compatibility | Operates as a required layer on top of [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection). |
| Bypass Methods | Can be bypassed using [Shareable Links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) and [Protection Bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) |
| IP Address Support | Supports IPv4 addresses and IPv4 CIDR ranges |
| Prerequisites |  |
| Preview Environment Requirements | Can only be enabled in preview when [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) is also enabled. |
| External Proxy Configuration | Requires [rulesets](/guides/can-i-use-a-proxy-on-top-of-my-vercel-deployment) configuration to avoid blocking proxy IPs. [Contact our sales team for more information](/contact/sales) |
| Security Considerations |  |
| Firewall Precedence | [Vercel Firewall](/docs/vercel-firewall) takes precedence over Trusted IPs |
| IP Blocking | IPs or CIDRs listed in [IP Blocking](/docs/security/vercel-waf/ip-blocking) will be blocked even if listed in Trusted IPs |
| DDoS Mitigation | Trusted IPs do not bypass [DDoS Mitigation](/docs/security/ddos-mitigation) unless configured |
| Deployment Impact | Changing the Trusted IPs list affects all deployments |
| Disabling Trusted IPs | Disabling makes all existing deployments accessible from any IP |

## [Managing Trusted IPs](#managing-trusted-ips)

You can manage Trusted IPs through the dashboard, API, or Terraform:

### [Manage using the dashboard](#manage-using-the-dashboard)

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Trusted IPs for
    2.  Go to Settings then Deployment Protection
2.  ### [Manage Vercel Authentication](#manage-vercel-authentication)
    
    Ensure Vercel Authentication is enabled. See [Managing Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication#managing-vercel-authentication).
    
3.  ### [Manage Trusted IPs](#manage-trusted-ips)
    
    From the Trusted IPs section:
    
    1.  Use the toggle to enable the feature
    2.  Select the [deployment environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) you want to protect
    3.  Enter your list of IPv4 addresses and IPv4 CIDR ranges with an optional note describing the address
    4.  Finally, select Save
    
    All your existing and future deployments will be protected with Trusted IPs for that project. Visitors to your project deployments from IP addresses not included in your list will see a [No Deployment Found](/docs/errors/platform-error-codes#404:-deployment_not_found) error page.
    

### [Manage using the API](#manage-using-the-api)

You can manage Trusted IPs using the Vercel API endpoint to [update an existing project](/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body

*   `deploymentType`
    *   `prod_deployment_urls_and_all_previews`: Standard Protection
    *   `all`: All Deployments
    *   `preview`: Only Preview Deployments
    *   `production`: Only Production Deployments
*   `addresses`: Array of addresses
    *   `value`: The IPv4, or IPv4 CIDR address
    *   `note`: Optional note about the address
    *   `protectionMode`
        *   `additional`: IP is required along with other enabled protection methods (recommended setting)
        *   `additional`: IP is required along with other enabled protection methods

```
// enable / update trusted ips
{
  "trustedIps": {
      "deploymentType": "all" | "preview" | "production" | "prod_deployment_urls_and_all_previews",
      "addresses": { "value": "<value>"; "note": "<note>" | undefined }[],
      "protectionMode": "additional"
  }
}
// disbale trusted ips
{
  "trustedIps": null
}
```

### [Manage using Terraform](#manage-using-terraform)

You can configure Trusted IPs using `trusted_ips` in the `vercel_project` data source in the [Vercel Terraform Provider](https://registry.terraform.io/providers/vercel/vercel/latest/docs/data-sources/project).

--------------------------------------------------------------------------------
title: "Vercel Authentication"
description: "Learn how to use Vercel Authentication to restrict access to your deployments."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/vercel-authentication"
--------------------------------------------------------------------------------

# Vercel Authentication

Copy page

Ask AI about this page

Last updated September 15, 2025

Vercel Authentication is available on [all plans](/docs/plans)

Those with the [owner](/docs/rbac/access-roles#owner-role), [member](/docs/rbac/access-roles#member-role) and [admin](/docs/rbac/access-roles#admin-role) roles can manage Vercel Authentication

Vercel Authentication lets you restrict access to your public and non-public deployments. It is the recommended approach to protecting your deployments, and available on all plans. When enabled, it allows only users with deployment access to view and comment on your site.

Users attempting to access the deployment will encounter a Vercel login redirect. If already logged into Vercel, Vercel will authenticate them automatically.

After login, users are redirected and a cookie is set in the browser if they have view access. If the user does not have access to view the deployment, they will be redirected to [request access](#access-requests).

## [Who can access protected deployments?](#who-can-access-protected-deployments)

*   Logged in [team members](/docs/rbac/access-roles#team-level-roles) with at least a viewer role ([Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) or [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role))
*   Logged in [project members](/docs/rbac/access-roles#project-level-roles) with at least the [project Viewer](/docs/rbac/access-roles#project-viewer) role
*   Logged in members of an [access group](/docs/rbac/access-groups) that has access to the project the deployment belongs to
*   Logged in Vercel users who have been [granted access](#access-requests)
*   Anyone who has been given a [Shareable Link](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) to the deployment
*   Tools using the [protection bypass for automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) header

## [Access requests](#access-requests)

Access requests are available on [all plans](/docs/plans)

Those with the [owner](/docs/rbac/access-roles#owner-role), [member](/docs/rbac/access-roles#member-role), [admin](/docs/rbac/access-roles#admin-role) and [developer](/docs/rbac/access-roles#developer-role) roles can accept or reject access requests

When a Vercel user visits your protected deployment, but they do not have permission to access it, they have the option to request access for their Vercel account. This request triggers an email and Vercel notification to the branch authors.

![External users can request access to protected deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Frequest-access.png&w=640&q=75)![External users can request access to protected deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Frequest-access-dark.png&w=640&q=75)

External users can request access to protected deployments.

The access request can be approved or declined. Additionally, granted access can be revoked for a user at any time.

Users granted access can view the latest deployment from a specific branch when logged in with their Vercel account. They can also leave preview [Comments](/docs/comments) if these are enabled on your team.

Those on the Hobby plan can only have one external user per account. If you need more, you can upgrade to a [Pro plan](/docs/plans/pro-plan/trials).

You can manage access requests in the following way

1.  From your [dashboard](/dashboard) go to the Settings tab
2.  Select Deployment Protection and then choose the Requests tab to see pending requests
3.  Choose Access to manage existing access

![Access requests can be approved and declined on the Dashboard > Settings > Deployment Protection > Requests section.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-requests.png&w=1920&q=75)![Access requests can be approved and declined on the Dashboard > Settings > Deployment Protection > Requests section.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-requests-dark.png&w=1920&q=75)

Access requests can be approved and declined on the Dashboard > Settings > Deployment Protection > Requests section.

![Granted access requests can be managed on the Dashboard > Settings > Deployment Protection > Access section.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fgranted-access-list.png&w=1920&q=75)![Granted access requests can be managed on the Dashboard > Settings > Deployment Protection > Access section.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fgranted-access-list-dark.png&w=1920&q=75)

Granted access requests can be managed on the Dashboard > Settings > Deployment Protection > Access section.

Access requests can also be managed using the share modal on the deployment page

![Access requests can be approved, declined and revoked in the deployment share modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-access-v2-light.png&w=828&q=75)![Access requests can be approved, declined and revoked in the deployment share modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fmanage-access-v2-dark.png&w=828&q=75)

Access requests can be approved, declined and revoked in the deployment share modal.

## [Vercel Authentication security considerations](#vercel-authentication-security-considerations)

You can configure Vercel Authentication for different environments, as outlined in [Understanding Deployment Protection by environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment). This feature works alongside other security measures like [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips). For specific use-cases, you can bypass Vercel Authentication with methods like [Shareable Links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) or [Protection bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation).

Disabling Vercel Authentication renders all existing deployments unprotected. However, re-enabling it allows previously authenticated users to maintain access without a new login provided they have already authenticated to the specific deployment and have a cookie set in their browser. The authentication token sent as a cookie is restricted to one URL and isn't transferable, even between URLs pointing to the same deployment.

| Consideration | Description |
| --- | --- |
| Environment Configuration | Can be enabled for different environments. See [Understanding Deployment Protection by environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) |
| Compatibility | Compatible with [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips) |
| Bypass Methods | Can be bypassed using [Shareable Links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) and [Protection bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) |
| Disabling | All existing deployments become unprotected when Vercel Authentication is disabled |
| Re-enabling | Users who have logged in previously will still have access without re-authenticating |
| Token Scope | Tokens are valid for a single URL and are not reusable across different URLs |

## [Managing Vercel Authentication](#managing-vercel-authentication)

Admins and members can enable or disable Vercel Authentication for their team. Hobby teams can also enable or disable for their own projects. Vercel Authentication is managed on a per-project basis.

You can manage Vercel Authentication through the dashboard, API, or Terraform:

### [Manage using the dashboard](#manage-using-the-dashboard)

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Password Protection for
    2.  Go to Settings then Deployment Protection
2.  ### [Manage Vercel Authentication](#manage-vercel-authentication)
    
    From the Vercel Authentication section:
    
    1.  Use the toggle to enable the feature
    2.  Select the [deployment environment](/docs/deployments/environments) you want to protect
    3.  Finally, Select Save
    
    All your existing and future deployments will be protected with Vercel Authentication for the project. Next time when you access a deployment, you will be asked to log in with Vercel if you aren't already logged in, you will be redirected to the deployment URL and a cookie will be set in your browser for that deployment URL.
    
    ![Enabling Vercel Authentication.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fsso-protection-light.png&w=1920&q=75)![Enabling Vercel Authentication.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fsso-protection-dark.png&w=1920&q=75)
    
    Enabling Vercel Authentication.
    

### [Manage using the API](#manage-using-the-api)

You can manage Vercel Authentication using the Vercel API endpoint to [update an existing project](/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body

*   `prod_deployment_urls_and_all_previews`: Standard Protection
*   `all`: All Deployments
*   `preview`: Only Preview Deployments

```
// enable / update Vercel Authentication
{
  "ssoProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview"
  }
}
 
// disable Vercel Authentication
{
  "ssoProtection": null
}
```

### [Manage using Terraform](#manage-using-terraform)

You can configure Vercel Authentication using `vercel_authentication` in the `vercel_project` data source in the [Vercel Terraform Provider](https://registry.terraform.io/providers/vercel/vercel/latest/docs/data-sources/project).

--------------------------------------------------------------------------------
title: "Deployment Retention"
description: "Learn how Deployment Retention policies affect a deployment's lifecycle"
last_updated: "null"
source: "https://vercel.com/docs/deployment-retention"
--------------------------------------------------------------------------------

# Deployment Retention

Copy page

Ask AI about this page

Last updated September 24, 2025

Deployment Retention is available on [all plans](/docs/plans)

Deployment retention refers to the configured policies that determine how long different types of deployments are kept before they are automatically deleted.

These configured retention policies allow you to control how long your deployment data is stored, providing:

*   Enhanced protection: Remove outdated deployments with potential vulnerabilities or sensitive data
*   Compliance support: Configure retention policies to align with your compliance requirements.
*   Efficient storage management: Automatically clear out unnecessary deployments

Vercel provides unlimited deployment retention for all deployments, regardless of the plan that you are on.

You can configure retention durations for the following deployment states:

*   Canceled deployments
*   Errored deployments
*   Preview deployments
*   Production deployments

The latest production deployment will always be retained, regardless of the retention policy.

For example, imagine you created a production deployment with a 60-day retention period on 01/01/2024 and later replaced it with a newer deployment. The origin deployment would expire on 03/01/2024, entering the recovery period, and users accessing it would see a 410 status code. If required, you could still restore it until 03/31/2024, when all associated resources are permanently removed and restoring the deployment is no longer possible.

Once a policy is enabled on a project, deployments within the retention period will start to be automatically marked for deletion, within a few days of enabling the policy.

## [Setting a deployment retention policy](#setting-a-deployment-retention-policy)

To configure a retention policy, navigate to the Settings tab of your project and follow these steps:

1.  Select Security on the side panel of the project settings page
2.  Scroll down to the Deployment Retention Policy section
3.  Select the drop down menu with the appropriate duration
4.  Save the new retention policy for your project

### [Viewing deployment retention policy](#viewing-deployment-retention-policy)

You can view your deployments retention policy using [Vercel CLI](/docs/cli/list) and running the following command from your terminal:

terminal

```
vercel list [project-name] [--policy errored=6m]
```

## [Restoring a deleted deployment](#restoring-a-deleted-deployment)

When a deployment is marked for deletion either accidentally or as part of the retention policy, you can restore it within the recovery period. This period is 30 days for successfully built deployments, but unsuccessful deployments may be garbage collected sooner.

To restore a deleted deployment, navigate to the Settings tab of your project:

1.  Select Security on the side panel of the project settings page
2.  Scroll down to the Recently Deleted section
3.  Find the deployment that needs to be restored, and click on the dropdown menu item Restore
4.  Complete the modal

## [More resources](#more-resources)

*   [View Deployment Retention Policies](/docs/cli/list#unique-options)
*   [Troubleshoot Deployment Retention Errors](/docs/errors/DEPLOYMENT_DELETED)

--------------------------------------------------------------------------------
title: "Deploying to Vercel"
description: "Learn how to create and manage deployments on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/deployments"
--------------------------------------------------------------------------------

# Deploying to Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

A deployment on Vercel is the result of a successful build of your project. Each time you deploy, Vercel generates a unique URL so you and your team can preview changes in a live [environment](/docs/deployments/environments).

Vercel supports multiple ways to create a deployment:

*   [Git](#git)
*   [Vercel CLI](#vercel-cli)
*   [Deploy Hooks](#deploy-hooks)
*   [Vercel REST API](#vercel-rest-api)

## [Deployment Methods](#deployment-methods)

### [Git](#git)

The most common way to create a deployment is by pushing code to a connected [Git repository](/docs/git). When you [import a Git repository to Vercel](/docs/git#deploying-a-git-repository), each commit or pull request (on supported Git providers) automatically triggers a new deployment.

Vercel supports the following providers:

*   [GitHub](/docs/git/vercel-for-github)
*   [GitLab](/docs/git/vercel-for-gitlab)
*   [Bitbucket](/docs/git/vercel-for-bitbucket)
*   [Azure DevOps](/docs/git/vercel-for-azure-pipelines)

You can also [create deployments from a Git reference](/docs/git#creating-a-deployment-from-a-git-reference) using the Vercel Dashboard if you need to deploy specific commits or branches manually.

### [Vercel CLI](#vercel-cli)

You can deploy your Projects directly from the command line using [Vercel CLI](/docs/cli). This method works whether your project is connected to Git or not.

1.  Install Vercel CLI:
    
    ```
    npm i -g vercel
    ```
    
2.  Initial Deployment:
    
    In your project's root directory, run:
    
    ```
    vercel --prod
    ```
    
    This links your local directory to your Vercel Project and creates a [Production Deployment](/docs/deployments/environments#production-environment). A `.vercel` directory is added to store Project and Organization IDs.
    

Vercel CLI can also integrate with custom CI/CD workflows or third-party pipelines. Learn more about the different [environments on Vercel](/docs/deployments/environments).

### [Deploy Hooks](#deploy-hooks)

[Deploy Hooks](/docs/deploy-hooks) let you trigger deployments with a unique URL. You must have a connected Git repository to use this feature, but the deployment does not require a new commit.

1.  From your Project settings, create a Deploy Hook
2.  A unique URL is generated for each Project
3.  Make an HTTP `GET` or `POST` request to this URL to trigger the deployment

Refer to the [Deploy Hooks documentation](/docs/deploy-hooks) for more information.

### [Vercel REST API](#vercel-rest-api)

The [Vercel REST API](/docs/rest-api) lets you create deployments by making an HTTP `POST` request to the deployment endpoint. In this workflow:

1.  Generate a SHA for each file you want to deploy
2.  Upload those files to Vercel
3.  Send a request to create a new deployment with those file references

This method is especially useful for custom workflows, multi-tenant applications, or integrating with third-party services not officially supported by Vercel. For more details, see the [API reference](/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment) and [How do I generate an SHA for uploading a file](/guides/how-do-i-generate-an-sha-for-uploading-a-file-to-the-vercel-api).

## [Accessing Deployments](#accessing-deployments)

Vercel provides three default environments—Local, Preview, and Production:

1.  Local Development: developing and testing code changes on your local machine
2.  Preview: deploying for further testing, QA, or collaboration without impacting your live site
3.  Production: deploying the final changes to your user-facing site with the production domain

Learn more about [environments](/docs/deployments/environments).

## [Using the Dashboard](#using-the-dashboard)

Vercel’s dashboard provides a centralized way to view, manage, and gain insights into your deployments.

### [Resources Tab and Deployment Summary](#resources-tab-and-deployment-summary)

When you select a deployment from your Project → Deployments page, you can select the Resources tab to view and search:

*   Middleware: Any configured [matchers](/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config).
*   Static Assets: Files (HTML, CSS, JS) and their sizes.
*   Functions: The type, runtime, size, and regions.

You can use the three dot (…) menu for a given function to jump to that function in Logs, Analytics, Speed Insights, or the Observability tab.

![Example of a deployment resources page with a search applied.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeployment-resources-page-light.png&w=3840&q=75)![Example of a deployment resources page with a search applied.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeployment-resources-page-dark.png&w=3840&q=75)

Example of a deployment resources page with a search applied.

You can also see a summary of these resources by expanding the Deployment Summary section on a Deployment Details page. To visit the Deployment Details page for a deployment, select it from your Project → Deployments page.

![Example of an open deployment summary.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-light.png&w=3840&q=75)![Example of an open deployment summary.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-dark.png&w=3840&q=75)

Example of an open deployment summary.

You’ll also see your build time, detected framework, and any relevant logs or errors.

### [Project Overview](#project-overview)

On your Project Overview page, you can see the latest production deployment, including the generated URL and commit details, and deployment logs for debugging.

### [Managing Deployments](#managing-deployments)

From the Deployments tab, you can:

*   Redeploy: Re-run the build for a specific commit or configuration.
*   Inspect: View logs and build outputs.
*   Assign a Custom Domain: Point custom domains to any deployment.
*   Promote to Production: Convert a preview deployment to production (if needed).

For more information on interacting with your deployments, see [Managing Deployments](/docs/deployments/managing-deployments).

--------------------------------------------------------------------------------
title: "Claim Deployments"
description: "Learn how to take ownership of deployments on Vercel with the Claim Deployments feature."
last_updated: "null"
source: "https://vercel.com/docs/deployments/claim-deployments"
--------------------------------------------------------------------------------

# Claim Deployments

Copy page

Ask AI about this page

Last updated September 30, 2025

The Claim Deployments feature enables users to take control of deployments by transferring them to their Vercel accounts. Users can generate and share a claim URL, which allows others to assume ownership of these deployments. This feature is particularly helpful for AI-generated deployments and facilitates the transfer of projects between different accounts with different owners.

However, when transferring a project between two teams owned by the same user, it is recommended to use the [Project Transfer flow](/docs/projects/transferring-projects#starting-a-transfer) instead of the Claim Deployments flow.

## [Get started](#get-started)

*   [Claim deployments template](https://github.com/vercel/claim-deployments-demo)
*   [Demo](https://claim-deployments-demo.vercel.app)
*   [Demo with resource claims](https://claim-deployments-demo-with-resource.vercel.app/)

## [Associated resources](#associated-resources)

When a user claims a deployment, Vercel also transfers any associated resources (limited to specific providers) to the new owner's account. These resources maintain their connections to the project, ensuring a seamless transition of both the deployment and its dependencies.

The resource provider that currently supports resource transfer is [Prisma](https://vercel.com/marketplace/prisma).

For more details on the transfer process, see [Resources with Claim Deployments flows](/docs/integrations/create-integration/marketplace-flows#resources-with-claim-deployments).

## [Important endpoints](#important-endpoints)

*   Claim Deployments URL: `https://vercel.com/claim-deployment?[...]`
    
*   Initiate a project transfer request: [POST /projects/:idOrName/transfer-request](/docs/rest-api/reference/endpoints/projects/create-project-transfer-request)
    
*   Complete a project transfer: [PUT /projects/transfer-request/:code](/docs/rest-api/reference/endpoints/projects/accept-project-transfer-request)
    
    *   _This endpoint is not needed if you are using the Claim Deployments URL_

## [Example use case: automated AI-generated deployment](#example-use-case:-automated-ai-generated-deployment)

1.  File upload: The AI agent uploads the deployment files using the Vercel API: [POST /files](/docs/rest-api/reference/endpoints/deployments/upload-deployment-files).
    
2.  Deployment creation:
    
    *   Create a new deployment using the [Vercel CLI](/docs/cli/deploying-from-cli)
    *   Or create a deployment with the Vercel API: [POST /files](/docs/rest-api/reference/endpoints/deployments/upload-deployment-files) followed by [POST /deployments](/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment).
3.  Project transfer request:
    
    *   The agent initiates a transfer request with: [POST /projects/:idOrName/transfer-request](/docs/rest-api/reference/endpoints/projects/create-project-transfer-request).
    *   This returns a `code` (valid for 24 hours) that allows the agent to transfer the project to another team, typically the end user who initiated the request.
4.  Generate claim URL:
    
    *   The agent generates a claim URL and shares it with the user: `https://vercel.com/claim-deployment?code=xxx&returnUrl=https://xxx`
5.  User claims the deployment:
    
    *   The user accesses the claim page using the URL and selects a team within their Vercel account to transfer the deployment.
6.  Project transfer completion:
    
    *   After the user clicks Transfer, the Vercel API ([PUT /projects/transfer-request/:code](/docs/rest-api/reference/endpoints/projects/accept-project-transfer-request)) completes the project transfer, assigning it to the user’s selected team. This step is not necessary if you are using the Claim Deployments Flow.

Get started with [this template](https://github.com/vercel/claim-deployments-demo) of claiming deployments ([demo](https://claim-deployments-demo.vercel.app)).

## [Team restructuring](#team-restructuring)

When reorganizing teams, you can easily transfer ownership of projects to another team using the Claim Deployments feature.

## [Migrating personal projects to a company account](#migrating-personal-projects-to-a-company-account)

Freelancers or employees can move deployments from their personal accounts to a company’s Vercel account by generating and sharing a claim URL.

--------------------------------------------------------------------------------
title: "Environments"
description: "Environments are for developing locally, testing changes in a pre-production environment, and serving end-users in production."
last_updated: "null"
source: "https://vercel.com/docs/deployments/environments"
--------------------------------------------------------------------------------

# Environments

Copy page

Ask AI about this page

Last updated June 2, 2025

Vercel provides three default environments—Local, Preview, and Production:

1.  Local Development: developing and testing code changes on your local machine
2.  Preview: deploying for further testing, QA, or collaboration without impacting your live site
3.  Production: deploying the final changes to your user-facing site with the production domain

Pro and Enterprise teams can create Custom Environments for more specialized workflows (e.g., `staging`, `QA`). Every environment can define it’s own unique environment variables, like database connection information or API keys.

## [Local Development Environment](#local-development-environment)

This environment is where you develop new features and fix bugs on your local machine. When building with [frameworks](/docs/frameworks), use the [Vercel CLI](/docs/cli) to pull the environment variables for your project.

1.  Install the Vercel CLI:
    
    ```
    npm install -g vercel
    ```
    
2.  Link your Vercel project with your local directory:
    
    ```
    vercel link
    ```
    
3.  Pull environment variables locally for use with application development:
    
    ```
    vercel env pull
    ```
    

This will populate the `.env.local` file in your application directory.

## [Preview Environment (Pre-production)](#preview-environment-pre-production)

Preview environments allow you to deploy and test changes in a live setting, without affecting your production site. By default, Vercel creates a preview deployment when you:

*   Push a commit to a branch that is not your production branch (commonly `main`)
*   Create a pull request (PR) on [GitHub, GitLab, or Bitbucket](/docs/git)
*   Deploy using the CLI without the `-prod` flag, for example just `vercel`

Each deployment gets an automatically generated URL, and you'll typically see links appear in your Git provider’s PR comments or in the Vercel Dashboard.

There are two types of preview URLs:

*   Branch-specific URL – Always points to the latest changes on that branch
*   Commit-specific URL – Points to the exact deployment of that commit

Learn more about [generated URLs](/docs/deployments/generated-urls).

## [Production Environment](#production-environment)

The Production environment is the live, user-facing version of your site or application.

By default, pushing or merging changes into your production branch (commonly `main`) triggers a production deployment. You can also explicitly deploy to production via the CLI:

```
vercel --prod
```

When a production deployment succeeds, Vercel updates your production domains to point to the new deployment, ensuring your users see the latest changes immediately. For advanced workflows, you can disable the auto-promotion of deployments and [manually control promotion](/docs/deployments/promoting-a-deployment).

## [Custom Environments](#custom-environments)

Custom environments are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Custom environments are useful for longer-running pre-production environments like `staging`, `QA`, or any other specialized workflow you require.

Team owners and project admins can create, update, or remove custom environments.

### [Creating a custom environment](#creating-a-custom-environment)

DashboardcURLSDK

1.  Go to your Project Settings in the Vercel Dashboard
2.  Under Environments, click Create Environment
3.  Provide a name (e.g., `staging`), and optionally:
    *   Branch Tracking to automatically deploy whenever a matching branch is pushed
    *   Attach a Domain to give a persistent URL to your environment
    *   Import variables from another environment to seed this environment with existing environment variables

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

cURL

```
curl --request POST \
  --url https://api.vercel.com/v9/projects/<project-id-or-name>/custom-environments \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "slug": "<environment_name_slug>",
    "description": "<environment_description>",
  }'
```

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

createCustomEnvironment

```
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.environment.createCustomEnvironment({
    idOrName: '<project-id-or-name>',
    requestBody: {
      slug: '<environment_name_slug>',
      description: '<environment_description>',
    },
  });
  // Handle the result
  console.log(result);
}
 
run();
```

### [Using custom environments via the CLI](#using-custom-environments-via-the-cli)

You can deploy, pull, and manage environment variables to your custom environment with the CLI:

```
# Deploy to a custom environment named "staging":
vercel deploy --target=staging
 
# Pull environment variables from "staging":
vercel pull --environment=staging
 
# Add environment variables to "staging":
vercel env add MY_KEY staging
```

### [Pricing and limits](#pricing-and-limits)

Custom environments are available at no additional cost on the Pro and Enterprise plans. The number of custom environments you can create is based on your plan:

*   Pro: 1 custom environment per project
*   Enterprise: 12 custom environments per project

## [More resources](#more-resources)

*   [Learn about the different environments on Vercel](https://www.youtube.com/watch?v=nZrAgov_-D8)

--------------------------------------------------------------------------------
title: "Accessing Deployments through Generated URLs"
description: "When you create a new deployment, Vercel will automatically generate a unique URL which you can use to access that particular deployment."
last_updated: "null"
source: "https://vercel.com/docs/deployments/generated-urls"
--------------------------------------------------------------------------------

# Accessing Deployments through Generated URLs

Copy page

Ask AI about this page

Last updated September 24, 2025

When you create a new [deployment](/docs/deployments) in either a preview or production [environment](/docs/deployments/environments), Vercel will automatically generate a unique URL in order for you to access that deployment. You can use this URL to access a particular deployment for as long as your set [deployment retention policy](/docs/security/deployment-retention#setting-a-deployment-retention-policy) allows.

This URL is publicly accessible by default, but you can configure it to be private using [deployment protection](/docs/security/deployment-protection).

The make up of the URL depends on how it was created and if it relates to a branch of a specific commit. To learn more, see [URL Components](/docs/deployments/generated-urls#url-components).

## [Viewing generated URLs](#viewing-generated-urls)

You can access these automatically generated URLs in the following ways:

*   On the command line when the build has completed.
*   When using Git, you can access either a URL for the branch or for each commit. To learn more, see [Generated from Git](#generated-from-git).
*   Under the Project's Overview and Deployments tabs, as shown below:

![Generated URL for a production deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgenerated-url-prod-light.png&w=3840&q=75)![Generated URL for a production deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgenerated-url-prod-dark.png&w=3840&q=75)

Generated URL for a production deployment.

## [URL Components](#url-components)

Generated URLs are comprised of several different pieces of data associated with the underlying deployment. Varying combinations of the following information may be used to generate a URL:

| Value | Description | Created when |
| --- | --- | --- |
| `<project-name>` | The name of the [Project](/docs/projects/overview) that contains the deployment | Git branch, Git commit, CLI |
| `<unique-hash>` | 9 randomly generated numbers and letters | Git commit |
| `<scope-slug>` | The slug (not the name) of the account or [team](/docs/accounts/create-a-team) that contains the project/deployment | Git branch, Git commit, CLI |
| `<branch-name>` | The name of the Git branch for which the deployment was created | Git branch |

### [Generated from Git](#generated-from-git)

When are working with Git, Vercel will automatically generate a URL for the following:

*   The commit: This URL will always show you a preview of changes from that specific commit. This is useful for sharing a specific version of your project at a point in time.
    
    url-structure
    
    ```
    <project-name>-<unique-hash>-<scope-slug>.vercel.app
    ```
    
*   The branch: The URL generated from a Git branch will always show you the most recent changes for the branch and won't change if you push new commits to the branch. For this reason, this format is ideal for sharing with team members during your review process. The URL has the following structure:
    
    url-structure
    
    ```
    <project-name>-git-<branch-name>-<scope-slug>.vercel.app
    ```
    

To access the commit URL, click the View deployment button from your pull request. To access the branch URL, click the Visit Preview button from the pull request comment.

![Viewing deployment URLs in a pull request on GitHub.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit-link-light.png&w=1920&q=75)![Viewing deployment URLs in a pull request on GitHub.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit-link-dark.png&w=1920&q=75)

Viewing deployment URLs in a pull request on GitHub.

### [Generated with Vercel CLI](#generated-with-vercel-cli)

To access the URL for a successful deployment from Vercel CLI, you can save the [standard output of the deploy command](/docs/cli/deploy#standard-output-usage). The generated URL will have the following structure:

url-structure

```
<project-name>-<scope-slug>.vercel.app;
```

Once you deploy to the production environment, the above URL will point to the production deployment.

If the deployment is created on a [Team](/docs/accounts/create-a-team), you can also use the URL specific to the deployment's author. It will have the following structure:

url-structure

```
<project-name>-<author-name>-<scope-slug>.vercel.app;
```

This allows you to stay on top of the latest change deployed by a particular [member](/docs/accounts/team-members-and-roles) of a team within a specific project.

### [Truncation](#truncation)

If more than 63 characters are present before the `.vercel.app` suffix (or the respective [Preview Deployment Suffix](#preview-deployment-suffix)) for a generated URL, they will be truncated.

### [Anti-phishing protection](#anti-phishing-protection)

If your `<project-name>` resembles a regular web domain, it may be shortened to avoid that resemblance. For example, `www-company-com` would be changed to just `company`. This is done to prevent an accidental trigger of anti-phishing protection built into web browsers that protect the user from visiting domains that look roughly like other domains they visit.

## [Preview Deployment Suffix](#preview-deployment-suffix)

Preview Deployment Suffix is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Preview Deployment Suffixes allow you to customize the URL of a [preview deployment](/docs/deployments/environments#preview-environment-pre-production) by replacing the default `vercel.app` suffix with a [custom domain](/docs/domains/add-a-domain) of your choice.

To learn more, see the [Preview Deployment Suffix](/docs/deployments/preview-deployment-suffix) documentation.

--------------------------------------------------------------------------------
title: "Accessing Build Logs"
description: "Learn how to use Vercel's build logs to monitor the progress of building or running your deployment, and check for possible errors or build failures."
last_updated: "null"
source: "https://vercel.com/docs/deployments/logs"
--------------------------------------------------------------------------------

# Accessing Build Logs

Copy page

Ask AI about this page

Last updated September 24, 2025

When you deploy your website to Vercel, the platform generates build logs that show the deployment progress. The build logs contain information about:

*   The version of the build tools
*   Warnings or errors encountered during the build process
*   Details about the files and dependencies that were installed, compiled, or built during the deployment

Build logs are particularly useful for debugging issues that may arise during deployment. If a deployment fails, these can help you identify the root cause of the issue.

To access build logs, click the Build Logs button from the production deployment tile in the projects overview page.

![View build logs for your Vercel deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Flogs%2Fbuttons-light.png&w=3840&q=75)![View build logs for your Vercel deployments.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Flogs%2Fbuttons-dark.png&w=3840&q=75)

View build logs for your Vercel deployments.

## [How build logs work?](#how-build-logs-work)

Build logs are generated at build time for all [Deployments](/docs/deployments). The logs are similar to your framework's [Build Command](/docs/deployments/configure-a-build#build-command) output, with a few minor additions from the Vercel build system. Once a build is complete, no new logs will be recorded.

In addition to the list of build actions, you can also find errors or warnings. These are highlighted with different colors, such as yellow for warnings and red for errors. This color coding makes it flexible to investigate why your build failed and which part of your website is affected. Build logs are stored indefinitely for each deployment.

Build logs will automatically be truncated, if the total size reaches over 4MB.

### [Link to build logs](#link-to-build-logs)

If you click on the timestamp to the left of the log entry, you get a link to that log entry. This will highlight the selected log and append the line number to the URL as an anchor (`#L6`). You can then share this link with other team members to point them to a specific line in the log.

You can select multiple lines by holding the `Shift` key and clicking the timestamps. This will create a link for the content between the first and last lines (`#L6-L9`).

The log link is only accessible to [team members](/docs/rbac/managing-team-members). Anyone who is not a member or has a valid Vercel account cannot access this link.

![Create a link to a log entry.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Flogs%2Flog-link-light.png&w=3840&q=75)![Create a link to a log entry.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Flogs%2Flog-link-dark.png&w=3840&q=75)

Create a link to a log entry.

The link to build logs feature works for logs that are up to 2000 lines long.

## [Save logs](#save-logs)

You can use [Drains](/docs/drains) to export, store, and analyze your build logs. Log Drains configuration can be accessed through the Vercel dashboard or through one of our [Logging integrations](/integrations#logging).

--------------------------------------------------------------------------------
title: "Managing Deployments"
description: "Learn how to manage your current and previously deployed projects to Vercel through the dashboard. You can redeploy at any time and even delete a deployment."
last_updated: "null"
source: "https://vercel.com/docs/deployments/managing-deployments"
--------------------------------------------------------------------------------

# Managing Deployments

Copy page

Ask AI about this page

Last updated September 24, 2025

You can manage all current and previous deployments regardless of environment, status, or branch from the [dashboard](/dashboard). To manage a deployment from the dashboard:

1.  Ensure your team is selected from the scope selector
2.  Select your project
3.  From the top navigation, select the Deployments tab
4.  You can then filter, redeploy, or manually promote your deployment to production

[Vercel CLI](https://vercel.com/cli) and [Vercel REST API](/docs/rest-api) also provide alternative ways to manage your deployments. You can find a full list of the commands available in the [Vercel CLI Reference](/docs/cli/deploying-from-cli), along with the deployments section of the [Vercel REST API Reference](/docs/rest-api/reference/endpoints/deployments).

## [Filter deployment](#filter-deployment)

You can filter your deployments based on branch, status, and deployment environment:

1.  Select your project from the [dashboard](/dashboard)
2.  From the top navigation, select the Deployments tab
3.  Use the dropdowns to search by Branch, Date Range, All Environments, or Status
    
    ![The Deployments tab with the status filter dropdown open.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Ffiltering-deployments%2Ffilter-status-light.png&w=1200&q=75)![The Deployments tab with the status filter dropdown open.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Ffiltering-deployments%2Ffilter-status-dark.png&w=1200&q=75)
    
    The Deployments tab with the status filter dropdown open.
    

## [Delete a deployment](#delete-a-deployment)

DashboardcURLSDK

If you no longer need a specific deployment of your app, you can delete it from your project with the following steps:

1.  From your [dashboard](/dashboard), select the project where the specific deployment is located.
2.  Click on the Deployments tab.
3.  From the list of deployments, click on the deployment that you want to delete
4.  Click the ... button.
5.  From the context menu, select Delete.

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

cURL

```
curl --request DELETE \
  --url https://api.vercel.com/v13/deployments/<deployment-id> \
  --header "Authorization: Bearer $VERCEL_TOKEN"
```

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

deleteDeployment

```
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.deployments.deleteDeployment({
    id: 'deployment-id',
  });
 
  // Handle the result
  console.log(result);
}
 
run();
```

Deleting a deployment prevents you from using instant rollback on it and might break the links used in integrations, such as the ones in the pull requests of your Git provider.

You can also set a [deployment retention policy](#set-the-deployment-retention-policy) to automatically delete deployments after a certain period.

### [Set the deployment retention policy](#set-the-deployment-retention-policy)

You can set the retention policy for your deployments to automatically delete them after a certain period. To learn more, see [Deployment Retention](/docs/security/deployment-retention).

## [Deployment protection](#deployment-protection)

Vercel provides a way to protect your deployments from being accessed by unauthorized users. You can use [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) to restrict access to your deployments to only Vercel users with [suitable access rights](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication#who-can-access-protected-deployments). You can also configure which [environments](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) are protected.

In addition, Enterprise teams can use [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips) and [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) to further secure their deployments. Password protection is also available as a paid add-on for Pro teams.

To learn more, see [Deployment Protection](/docs/security/deployment-protection).

## [Redeploy a project](#redeploy-a-project)

Vercel automatically redeploys your application when you make any commits. However, there can be situations such as bad cached data where you need to Redeploy your application to fix issues manually. To do so:

1.  Ensure your team is selected from the scope selector
2.  Select your project
3.  From the top navigation, select the Deployments tab
4.  Locate the deployment you wish to deploy. You may need to use the [filter](/docs/deployments/managing-deployments#filter-deployment) options
5.  Click the ellipsis icon () and select Redeploy
6.  In the Redeploy to Production window, decide if you want to use the existing [Build Cache](/docs/deployments/troubleshoot-a-build#understanding-build-cache), and then select Redeploy

![Option to confirm redeploy to production.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fredeploy-model-light.png&w=1080&q=75)![Option to confirm redeploy to production.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fredeploy-model-dark.png&w=1080&q=75)

Option to confirm redeploy to production.

### [When to Redeploy](#when-to-redeploy)

Other than your custom needs to redeploy, it's always recommended to redeploy your application to Vercel for the following use cases:

*   Enabling the [Analytics](/docs/analytics/quickstart)
*   Changing the [Environment Variables](/docs/environment-variables)
*   [Outage Resiliency](/docs/regions#outage-resiliency)
*   Making changes to Build & Development Settings
*   Redirect or Rewrites from a subdomain to a subpath

--------------------------------------------------------------------------------
title: "Inspecting your Open Graph metadata"
description: "Learn how to inspect and validate your Open Graph metadata through the Open Graph deployment tab."
last_updated: "null"
source: "https://vercel.com/docs/deployments/og-preview"
--------------------------------------------------------------------------------

# Inspecting your Open Graph metadata

Copy page

Ask AI about this page

Last updated September 15, 2025

You can use the Open Graph tab on every deployment on Vercel to validate and view your [Open Graph (OG)](https://ogp.me/) data across a range of social media sites before you share it out. Routes using [Deployment Protection](/docs/deployments/deployment-protection) can also be inspected.

To view your data:

1.  Choose your account or team from the [scope selector](/docs/dashboard-features#scope-selector)
2.  Select your project and go to the Deployments tab
3.  From the Deployments tab, select the deployment you wish to view the metadata for
4.  Select the Open Graph tab:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fog-tab-light.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fog-tab-dark.png&w=1080&q=75)
    
5.  From here, you can view the metadata and a preview for [Twitter](/docs/deployments/og-preview#twitter-specific-metadata), Slack, Facebook, and LinkedIn for [specific pages](/docs/deployments/og-preview#filter-by-pathname) in your deployment

## [Filter by pathname](#filter-by-pathname)

You can use the Path dropdown to view the OG card for any page on that particular deployment.

## [Metadata](#metadata)

These properties set by the [Open Graph protocol](https://ogp.me/#metadata).

| Property | Value | Description |
| --- | --- | --- |
| `title` | The title tag used to name the page. 70 characters max. | This is used by default if no other values are passed. |
| `description` | The meta.description tag used to describe the page. 200 characters max. | This is used by default if no other values are passed. |
| `og:image` | Absolute URL to image. | Use the [OG Image Generation](/docs/og-image-generation) documentation to create new images. |
| `og:title` | A title for link previews. | You can use this to override the meta title if you want the OG title to be different. |
| `og:description` | A one to two sentence description for link previews. | You can use this to override the meta description if you want the OG title to be different. |
| `og:url` | A canonical URL for link previews. | You should provide the absolute URL. |

index.js

```
<div>
  <head>
    <meta name="og:title" content="Vercel CDN" />
    <meta name="og:description" content="Vercel CDN" />
    <meta name="og:image" content={ // Because OG images must have a absolute
    URL, we use the // `VERCEL_URL` environment variable to get the deployment’s
    URL. // More info: // https://vercel.com/docs/environment-variables
    `${ process.env.VERCEL_URL ? 'https://' + process.env.VERCEL_URL : ''
    }/api/vercel` } />
    <meta
      name="og:url"
      content="https://vercel.com/docs/cdn"
    />
  </head>
  <h1>A page with Open Graph Image.</h1>
</div>
```

### [Twitter-specific metadata](#twitter-specific-metadata)

| Property | `content` value | Additional information |
| --- | --- | --- |
| `twitter:image` | A URL to an image file or to a dynamically generated image. `og:image` is used as a fallback. | `JPG`,`PNG`, `WEBP` and `GIF`. `SVG` is not supported |
| `twitter:card` | The type of card used for Twitter link previews | `summary`, `summary_large_image`, `app`, or `player` |
| `twitter:title` | A string that shows for Twitter link previews. `og:title` is used as a fallback. | 70 characters max |
| `twitter:description` | A description for Twitter link previews. `og:description` is used as a fallback. | 200 characters max |

index.js

```
<div>
  <head>
    <meta name="twitter:title" content="Vercel CDN for Twitter" />
    <meta name="twitter:description" content="Vercel CDN for Twitter" />
    <meta
      name="twitter:image"
      content="https://og-examples.vercel.sh/api/static"
    />
    <meta name="twitter:card" content="summary_large_image" />
  </head>
  <h1>A page with Open Graph Image.</h1>
</div>
```

--------------------------------------------------------------------------------
title: "Preview Deployment Suffix"
description: "When you create a new deployment, Vercel will automatically generate a unique URL which you can use to access that particular deployment."
last_updated: "null"
source: "https://vercel.com/docs/deployments/preview-deployment-suffix"
--------------------------------------------------------------------------------

# Preview Deployment Suffix

Copy page

Ask AI about this page

Last updated September 24, 2025

Preview Deployment Suffix is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Preview Deployment Suffixes allow you to customize the URL of a [preview deployment](/docs/deployments/environments#preview-environment-pre-production) by replacing the default `vercel.app` suffix with a [custom domain](/docs/domains/add-a-domain) of your choice.

The entered custom domain must be:

*   Available and active within the team that enabled the Preview Deployment Suffix
*   Using Vercel's [Nameservers](/docs/domains/add-a-domain#vercel-nameservers)

### [Enabling the Preview Deployment Suffix](#enabling-the-preview-deployment-suffix)

Preview Deployment Suffix is included and enabled by default in Enterprise plans

To enable Preview Deployment Suffix, and customize the appearance of any of your generated URLs:

1.  From your [dashboard](/dashboard), select the Settings tab
2.  Select the Billing tab
3.  Under Add-Ons, set the toggle for Preview Deployment Suffix to Enabled
4.  Navigate to the Settings tab on the team dashboard
5.  Select the General tab and scroll down to the Preview Deployment Suffix section
6.  Enter the custom domain of your choice in the input, and push Save

![Selecting a custom value for the Preview Deployment Suffix.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployment-suffix-light.png&w=1920&q=75)![Selecting a custom value for the Preview Deployment Suffix.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployment-suffix-dark.png&w=1920&q=75)

Selecting a custom value for the Preview Deployment Suffix.

If you are not able to use Vercel's Nameservers, see our guide on [how to use a custom domain without Vercel's Nameservers](/guides/preview-deployment-suffix-without-vercel-nameservers).

See the [plans add-ons](/docs/pricing#pro-plan-add-ons) documentation for information on pricing.

### [Disabling the Preview Deployment Suffix](#disabling-the-preview-deployment-suffix)

To disable Preview Deployment Suffix:

1.  From your [dashboard](/dashboard), select the Settings tab
2.  Select the Billing tab
3.  Under Add-Ons, set the toggle for Preview Deployment Suffix to Disabled

The next preview deployment generated will revert back to the default `vercel.app` suffix.

### [Broken Preview Deployment Suffix error](#broken-preview-deployment-suffix-error)

You may encounter this error if you are using the [Preview Deployment Suffix](#preview-deployment-suffix) in your team. Make sure that the custom domain you configured is:

*   Active (not deleted)
*   Available within the team that enabled the [Preview Deployment Suffix](#preview-deployment-suffix)
*   Backed by an [active wildcard certificate](https://knowledge.digicert.com/generalinformation/INFO900.html)

The best way to satisfy all of these constraints is to ensure the domain is also added to a project located in the same team. In this project, you can include a single `index.html` that displays when someone visits the root of the domain.

--------------------------------------------------------------------------------
title: "Promoting Deployments"
description: "Learn how to promote deployments to production on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/deployments/promoting-a-deployment"
--------------------------------------------------------------------------------

# Promoting Deployments

Copy page

Ask AI about this page

Last updated September 24, 2025

By default, when you merge to or make commits to your production branch (often `main`), Vercel will automatically promote the changes to Production. However, there are a number of ways to manually change which deployment is served to people who visit your production domain:

*   [Instant rollback](#instant-rollback): You can use this as a way to instantly revert to an earlier [deployment](/docs/instant-rollback#eligible-deployments) that has served production traffic. It works by assigning your domains to an existing deployment, rather than doing a complete rebuild
*   [Promote preview to production](#promote-a-deployment-from-preview-to-production): You can use this as a way to promote a preview deployment to production through a complete rebuild
*   [Promote a staged production build](#staging-and-promoting-a-production-deployment): You can use this option to promote a production deployment which has never served production traffic. To use this option, you must turn off the auto-assignment of domains. This option won't trigger a rebuild

## [Instant Rollback](#instant-rollback)

Use this when you want to replace the current production deployment with another deployment that has already been serving as current in the past. Instant Rollback is a faster process since it involves assigning domains to an existing deployment rather than a complete rebuild and is ideal to quickly recover from an incident in production to roll back. However, because it does not do a complete rebuild, items such as environment variables will not be rebuilt.

For more information on how and when to use it, see the [Instant Rollback docs](/docs/instant-rollback).

## [Promote a deployment from preview to production](#promote-a-deployment-from-preview-to-production)

There may be times when you need to promote an existing preview deployment to production, such as when you need to temporarily use a branch that isn't set as the [production branch](/docs/git#production-branch).

To promote an existing preview deployment to production on Vercel, do the following:

1.  Go to your project's Deployments tab. This tab lists all the previously deployed builds
2.  Click the ellipsis (), and from the context menu select Promote to Production
3.  The popup dialog informs you of which domain(s) will be linked to the build once promoted. To confirm, select Promote to Production

![Option to confirm promote to production.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdeployment%2Fpromote-to-prod-light.png&w=1080&q=75)![Option to confirm promote to production.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdeployment%2Fpromote-to-prod-dark.png&w=1080&q=75)

Option to confirm promote to production.

If you have different [Environment Variables](/docs/environment-variables#environments) set for preview and production deployments then the variables used will change from preview to those you have linked to the production environment. You cannot use your preview environment variables in a production deployment

## [Staging and promoting a production deployment](#staging-and-promoting-a-production-deployment)

In some cases you may want to create a production-like deployment to use as a staging environment before promoting it to production.

In this scenario, you can turn off the auto-assignment of domains for your production build, as described below. Turning off the auto-assignment of domains means the deployment won't automatically be served to your production traffic, but also means you must manually promote it to production.

### [CLI](#cli)

For steps on using this workflow in the CLI, see [Deploying a staged production build](/docs/cli/deploying-from-cli#deploying-a-staged-production-build).

### [Dashboard](#dashboard)

1.  On your [dashboard](/dashboard), select your project
2.  Select the Settings tab and go to your Environments settings
3.  Click on Production and go to the Branch Tracking section
4.  Disable the Auto-assign Custom Production Domains toggle
5.  When you are ready to promote this staged deployment to production, select the ellipses (…) next to the deployment
6.  From the menu, select the Promote option
7.  From the Promote dialog, confirm the deployment, and select the Promote button:

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpromote-to-prod-light.png&w=1080&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpromote-to-prod-dark.png&w=1080&q=75)

Vercel will instantly promote the deployment; it doesn't require a rebuild. Once promoted, the deployment is marked as [Current](#production-deployment-state).

## [Production deployment state](#production-deployment-state)

Your production deployments could be in one of three states:

*   Staged – This means that a commit has been pushed to `main`, but a domain has not been auto-assigned to the deployment. This type of a deployment can be promoted to Current
*   Promoted – This production deployment has been [promoted](#staging-and-promoting-a-production-deployment) from staging. If a deployment has already been promoted in the past, you can't promote it again. If you want to use a previously promoted deployment, you must do a rollback to it
*   Current – This is the production deployment that is aliased to your domain and the one that is currently being served to your users

--------------------------------------------------------------------------------
title: "Sharing a Preview Deployment"
description: "Learn how to share a preview deployment with your team and external collaborators."
last_updated: "null"
source: "https://vercel.com/docs/deployments/sharing-deployments"
--------------------------------------------------------------------------------

# Sharing a Preview Deployment

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Sharing with members of your team](#sharing-with-members-of-your-team)

By default, members of your [Vercel team](/docs/accounts/create-a-team) that have [access to your project](/docs/rbac/access-roles/project-level-roles) will also have access to your deployment. This allows them to comment, see who else is viewing the preview, and use the toolbar. Users who don't have access to the project will not have access to your deployment.

To share a preview deployment with a member of your team you can do any of the following:

*   Send an invite to individual users (external or team members), or groups of people
*   Copy the URL from the address bar of your browser and send it to them
*   Select Share in the [Vercel Toolbar](/docs/vercel-toolbar) menu, copy the URL and send it to them

They will also be able to find it by using the [generated URL](/docs/deployments/generated-urls) from any deployment in the [Vercel dashboard](/dashboard).

## [Sharing a preview deployment with external collaborators](#sharing-a-preview-deployment-with-external-collaborators)

To share a deployment with anyone, you can do any of the following:

*   Recommended: [Invite users](#invite-users) to view your deployment
*   [Set access to anyone](#sharing-with-sharable-links-and-managing-permissions) (or anyone with the link if deployment protection is enabled)
*   [Accept an access request](/docs/deployments/sharing-deployments#request-access)

When you share a preview deployment with an external user, they will not be added to your Vercel team. The collaborator does not need to have a Vercel account, but will need to create one if they wish to view a deployment that is [protected](#sharing-with-deployment-protection-enabled), use the [toolbar](/docs/vercel-toolbar), or leave [comments](/docs/comments).

Note that you can share two types of links: branch links, which reflect the latest commit, and commit links, which reflect changes up to a specific commit.

When sharing from the Share button next to the deployment in the Vercel dashboard, the share modal defaults to the branch link. You can switch to the commit link by selecting the dropdown arrow.

When sharing from Share in the toolbar menu, you'll share the current link. If it's a commit-specific link, you can switch to the branch link to share an always up-to-date preview.

### [Invite users](#invite-users)

Users on Pro and Enterprise teams can use this method to add one or more collaborators. Hobby users are limited to one collaborator at any one time. To invite users to view your deployment:

1.  Select Share in the toolbar menu or select the Share button next to the deployment in the [Vercel dashboard](/dashboard)
2.  In the Share modal that appears, enter the email(s), or names of people on your Vercel team you want to invite. You can also add a message to the invitation. The invitation will be sent as an email to the user(s)
3.  The invited user can now view the preview deployment. If Deployment Protection is enabled or if they want to add a comment, they will need to log into their Vercel account
4.  You can revoke access at any time by returning to the Share dialog and choosing the Revoke icon next to the user's email

![Share with invite.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fvercel-toolbar%2Finvite-share-preview-light.png&w=1080&q=75)![Share with invite.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fvercel-toolbar%2Finvite-share-preview-dark.png&w=1080&q=75)

Share with invite.

This is the recommended method for sharing a deployment with external collaborators, as it allows you to control who has access to your deployment on an individual basis.

### [Sharing with sharable links and managing permissions](#sharing-with-sharable-links-and-managing-permissions)

1.  Select Share in the toolbar menu or select the Share button on the deployment page in the [Vercel dashboard](/dashboard)
2.  In the Share modal that appears, you can manage who can view and comment on deployments:
    *   Team members with access: This is the default setting. Only team members who have access to this project and external users granted access can comment
    *   Anyone (Without deployment protection): If you don't have [deployment protection](/docs/security/deployment-protection) enabled, you can change the setting to Anyone. This allows any visitor who logs in with a Vercel account to leave comments on the preview, regardless of their team status
    *   Anyone with the link (With deployment protection): If you have deployment protection on, you can select Anyone with the link. This option creates a [sharable link that bypasses deployment protection](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links). Anyone with this link can log in to the toolbar and comment, even if they are not a part of your team or haven't been individually added as collaborators

![The Share settings modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fshareable-links-light.png&w=1200&q=75)![The Share settings modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fsharable-links-dark.png&w=1200&q=75)

The Share settings modal.

1.  After setting the chosen permission, use the Copy Link button to copy the link to your clipboard. This specific URL should be used, rather than the one from the address bar of your browser.

To learn more, see [sharable links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) in Deployment Protection.

### [Request access](#request-access)

If someone without access to comment attempts to log into the toolbar on a deployment, they will see a screen with the option to Request Access. You will be notified by email and the Vercel [notifications](/docs/notifications) widget when a request is made to a deployment you own.

To respond to the request:

1.  Select Share in the toolbar menu or select the Share button next to the deployment in the [Vercel dashboard](/dashboard)
2.  In the popup modal that appears, review the list under Access Requests
3.  Respond to the request by either allowing or denying access

## [Sharing with deployment protection enabled](#sharing-with-deployment-protection-enabled)

It is important to ensure the security of your preview deployments, which you can enable through [deployment protection](/docs/security/deployment-protection/methods-to-protect-deployments). We recommend that you scope access to the fewest number of people possible.

Deployment protection allows you to secure your preview deployments, with [Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and/or [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) to ensure that only authorized users can view your preview deployment.

*   If you don't have deployment protection enabled, anyone with the link can view your deployment
*   If you have Authentication enabled, only team members can view your deployment, unless you have added the user individually or they have requested access, or you have enabled sharable links
*   If you have Password Protection enabled, only users with the password can view your deployment, unless you have added the user individually or they have requested access, or you have enabled sharable links

--------------------------------------------------------------------------------
title: "Troubleshooting Build Errors"
description: "Learn how to resolve common scenarios you may encounter during the Build step, including build errors that cancel a deployment and long build times."
last_updated: "null"
source: "https://vercel.com/docs/deployments/troubleshoot-a-build"
--------------------------------------------------------------------------------

# Troubleshooting Build Errors

Copy page

Ask AI about this page

Last updated October 24, 2025

You can troubleshoot build errors that occur during the Build step of your deployment to Vercel. This guide will help you understand how to investigate build failures and long build times.

## [Troubleshooting views](#troubleshooting-views)

You can use the following views on your dashboard to troubleshoot a build:

*   Build logs - the console output when your deployment is building which can be found under the Deployment Status section of the Project's Deployment page.
*   Resources tab - the functions, middleware, and assets from your deployment's build.
*   Source tab - the output of the build after the deployment is successful. This can also be accessed by appending `/_src` to the Deployment URL

You can navigate to these views from the Deployment page by clicking on the Source tab, the Resources tab or the Build Logs accordion as shown below.

## [Troubleshoot Build failures](#troubleshoot-build-failures)

If your build fails, Vercel will report the error message on the Deployments page so that you can investigate and fix the underlying issue.

In the following we show you how to look up the error message of your failed build.

### [Investigating Build logs](#investigating-build-logs)

[Build logs](/docs/deployments/logs) provide you with an insight into what happened during the build of a deployment and can be accessed by:

1.  From your Vercel dashboard, select the project and then the [Deployments](/docs/projects/project-dashboard#deployments) tab
2.  Select the deployment. When there are build issues you will notice an error status next to deployment name

![Error status on the Deployments tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-deploy-overview-page-02-1.png&w=3840&q=75)![Error status on the Deployments tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-deploy-overview-page-02-1-dark.png&w=3840&q=75)

Error status on the Deployments tab.

1.  On the errored deployment's page, you will see a summary of the error in the preview section. In the Deployment Details section, expand the Building accordion to expand the logs. There are situations where [build logs are not available](#build-logs-not-available), in this scenario the error will be presented in the UI instead.
    
2.  Scroll down in the build logs until you find a red section where the keyword "Error" is mentioned. It can be mentioned once or multiple times. In many cases, the last mention is not indicative like in the example below where it says `yarn run build exited with 1`. If you look a few lines above, you will see an additional error which in this case indicates where the problem is with a link for more details. Sometimes, an error may not be mentioned in the lines above but the output will often help you identify where the problem is.
    

![Error in the logs of the Building accordion.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-deploy-overview-page-03.png&w=1080&q=75)![Error in the logs of the Building accordion.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-deploy-overview-page-03.png&w=1080&q=75)

Error in the logs of the Building accordion.

It is recommended to build your project on your local machine first (the build command varies per project) before deploying on Vercel. This will catch issues specific to your code or to your project's dependencies. In the example above, when the command `npm run build` (that runs `next build`) is run in the local console for a Next.js project, the error happens after building locally.

![Error in local console.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-console.png&w=1080&q=75)![Error in local console.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-console.png&w=1080&q=75)

Error in local console.

### [Build Logs not available](#build-logs-not-available)

Builds can fail without providing any build logs when Vercel detects a missing precondition that prevents a build from starting. For example:

*   An invalid [`vercel.json` configuration](/docs/project-configuration) was committed
*   When using [Ignored Build Steps](/guides/how-do-i-use-the-ignored-build-step-field-on-vercel)
*   Commits were made from a contributor that is not a [team member](/docs/accounts/team-members-and-roles)

In this case, you cannot access the Building accordion described above, and instead, Vercel will present an overlay that contains the error message.

![Build logs not available for a deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-no-logs-v2-light.png&w=3840&q=75)![Build logs not available for a deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-error-no-logs-v2-dark.png&w=3840&q=75)

Build logs not available for a deployment.

## [Cancelled Builds due to limits](#cancelled-builds-due-to-limits)

Sometimes, your Deployment Build can hit platform limits so that the build will be cancelled and throw a corresponding error that will be shown in the Build logs. Review the limits below in case you run into them.

### [Build container resources](#build-container-resources)

Every Build is provided with the following resources:

|  | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| Memory | 8192 MB | 8192 MB | Custom |
| Disk space | 23 GB | 23 GB | Custom |
| CPUs | 2 | 4 | Custom |

For Hobby customers, these limits are fixed. Pro and Enterprise customers can purchase [Enhanced or Turbo build machines](/docs/builds/managing-builds#build-machine-types) with extra CPUs, larger memory, and storage. Exceeding the memory or disk space allocations limits cancels the build and triggers a system report in your [Build logs](/docs/deployments/logs), identifying memory and disk space issues.

By default, the system generates this report only when it detects a problem. To receive a report for every deployment, set `VERCEL_BUILD_SYSTEM_REPORT=1` as an [environment variable](/docs/environment-variables#creating-environment-variables).

This report helps you detect hidden Out of Memory (OOM) events, and provides insights into disk usage by breaking down the sizes of your source code, `node_modules`, and output, and flagging files over 100 MB. The input size in the report corresponds to the size of your checked-out repository or files uploaded by CLI. The `node_modules` size represents the total size of all `node_modules` folders on disk.

| Resource | Allocation | Description |
| --- | --- | --- |
| Memory | 8192 MB | Fixed memory allocation. Builds exceeding this limit will be cancelled |
| CPUs | 4 | Number of CPUs allocated for build processing |
| Disk Space | 23 GB | Fixed disk space allocation. Builds exceeding this limit will be cancelled |
| System Report | Conditional | Generated in [Build logs](/docs/deployments/logs) when memory or disk space limits are reached. Available by default |
| Forced Reporting | Optional | Set `VERCEL_BUILD_SYSTEM_REPORT=1` as an [environment variable](/docs/environment-variables#creating-environment-variables) to enable reporting for all builds |

Review the below steps to help navigate this situation:

*   Review what package the error is related to and explore the package's documentation to see if the memory allocation can be customized with an install or Build command
*   If no package is specified, look into reducing the amount of JavaScript that your Project might be using or find a more efficient JavaScript bundler
*   Review what you are importing in your code such as third-party services, icons and media files

### [Build duration](#build-duration)

The total build duration is shown on the Vercel Dashboard and includes all three steps: building, checking, and assigning domains. Each step also shows the individual duration.

A Build can last for a maximum of 45 minutes. If the build exceeds this time, the deployment will be canceled and the error will be shown on the Deployment's Build logs. If you run into this limit, review this [guide](https://vercel.com/guides/how-do-i-reduce-my-build-time-with-next-js-on-vercel) that explains how to reduce the Build time with a Next.js Project.

### [Caching](#caching)

The maximum size of the Build's cache is 1 GB. It is retained for one month and it applies at the level of each [Build cache key](#caching-process).

It is not possible to manually configure which files are cached at this time.

## [Other Build errors](#other-build-errors)

You may come across the following Build-specific errors when deploying your Project. The link for each error provides possible causes of the error that can help you troubleshoot.

*   [Missing Build script](/docs/errors/error-list#missing-build-script)
*   [Recursive invocation of commands](/docs/errors/error-list#recursive-invocation-of-commands)
*   [Pnpm engine unsupported](/docs/errors/error-list#pnpm-engine-unsupported)

A 'module not found' error is a syntax error that will appear at build time. This error appears when the static import statement cannot find the file at the declared path. For more information, see [How do I resolve a 'module not found' error?](/guides/how-do-i-resolve-a-module-not-found-error)

## [Troubleshoot Build time](#troubleshoot-build-time)

### [Understanding Build cache](#understanding-build-cache)

The first Build in a Project will take longer as the Build cache is initially empty. Subsequent builds that have the same [Build cache key](#caching-process) will take less time because elements from your build, such as [framework files and node modules](#what-is-cached), will be reused from the available cache. The next sections will describe the factors that affect the Build cache to help you decrease the Build time

### [What is cached](#what-is-cached)

Vercel caches files based on the [Framework Preset](/docs/deployments/configure-a-build#framework-preset) selected in your [Project settings](/docs/projects/overview#project-settings). The following files are cached in addition to `node_modules/**`:

| Framework | Cache Pattern |
| --- | --- |
| Next.js | `.next/cache/**` |
| Nuxt | `.nuxt/**` |
| Gatsby.js | `{.cache,public}/**` |
| Eleventy | `.cache/**` |
| Jekyll | `{vendor/bin,vendor/cache,vendor/bundle}/**` |
| Middleman | `{vendor/bin,vendor/cache,vendor/bundle}/**` |

Note that the framework detection is dependent on the preset selection made in the [Build settings](/docs/deployments/configure-a-build#build-and-development-settings). You should make sure that the correct framework is set for your project for optimum build caching.

### [Caching process](#caching-process)

At the beginning of each build, the previous Build's cache is restored prior to the [Install Command](/docs/deployments/configure-a-build#install-command) or [Build command](/docs/deployments/configure-a-build#build-command) executing. Each deployment is associated with a unique Build cache key that is derived from the combination of the following data:

*   [Personal Account](/docs/teams-and-accounts#creating-a-personal-account) or [Team](/docs/teams-and-accounts)
*   [Project](/docs/projects/overview)
*   [Framework Preset](/docs/deployments/configure-a-build#framework-preset)
*   [Root Directory](/docs/deployments/configure-a-build#root-directory)
*   [Node.js Version](/docs/functions/runtimes/node-js#node.js-version)
*   [Package Manager](/docs/deployments/configure-a-build#install-command)
*   [Git branch](/docs/git)

Let's say that under your account `MyTeam`, you have a project `MySite` that is connected to your Git repository `MyCode` on the `main` branch for the production environment. When you make a commit to the `main` branch for the first time, you trigger a build that creates a production deployment with a new unique cache key. For any new commits to the `main` branch of `MyCode`, the existing Build cache is used as long as `MySite` is under `MyTeam`.

If you create a new Git branch in `MyCode` and make a commit to it, there is no cache for that specific branch. In this case, the last [production Deployment](/docs/deployments/environments#production-environment) cache is used to create a preview deployment and a new branch cache is created for subsequent commits to the new branch.

If you use [Vercel functions](/docs/functions) to process HTTP requests in your project, each Vercel Function is built separately in the Build step and has its own cache, based on the [Runtime](/docs/functions/runtimes) used. Therefore, the number and size of Vercel functions will affect your Build time. For Next.js projects, Vercel functions are bundled to optimize Build resources as described [here](/docs/functions/configuring-functions/advanced-configuration#bundling-vercel-functions).

At the end of each Build step, successful builds will update the cache and failed builds will not modify the existing cache.

### [Excluding development dependencies](#excluding-development-dependencies)

Since development dependencies (for example, packages such as `webpack` or `Babel`) are not needed in production, you may want to prevent them from being installed when deploying to Vercel to reduce the Build time. To skip development dependencies, customize the [Install Command](/docs/deployments/configure-a-build#install-command) to be `npm install --only=production` or `yarn install --production`.

## [Managing Build cache](#managing-build-cache)

Sometimes, you may not want to use the Build cache for a specific deployment. You can invalidate or delete the existing Build cache in the following ways:

*   Use the Redeploy button for the specific deployment in the Project's [Deployments](/docs/deployments/managing-deployments) page. In the popup window that follows, leave the checkbox Use existing Build Cache unchecked. See [Redeploying a project](/docs/deployments/managing-deployments#redeploy-a-project) for more information.
*   Use [`vercel --force`](/docs/cli/deploy#force) with [Vercel CLI](/docs/cli) to build and deploy the project without the Build cache
*   Use an Environment Variable `VERCEL_FORCE_NO_BUILD_CACHE` with a value of `1` on your project to skip the Build cache
*   Use an Environment Variable `TURBO_FORCE` with a value of `true` on your project to skip Turborepo [Remote Cache](/docs/monorepos/remote-caching)
*   Use the `forceNew` optional query parameter with a value of `1` when [creating a new deployment with the Vercel API](/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment) to skip the Build cache

When redeploying without the existing Build Cache, the Remote Cache from [Turborepo](https://turborepo.com/docs/core-concepts/remote-caching) and [Nx](https://nx.app/) are automatically excluded.

--------------------------------------------------------------------------------
title: "Troubleshoot project collaboration"
description: "Learn about common reasons for deployment issues related to team member requirements and how to resolve them."
last_updated: "null"
source: "https://vercel.com/docs/deployments/troubleshoot-project-collaboration"
--------------------------------------------------------------------------------

# Troubleshoot project collaboration

Copy page

Ask AI about this page

Last updated September 30, 2025

This guide will help you understand how to troubleshoot deployment failures related to project collaboration.

For private repositories, if we cannot identify the Vercel user associated with a commit, any deployment associated with that commit will fail. You can use the following checklist to make sure your Vercel team is properly configured:

Ensure all contributors pushing code are members of your Vercel team.

For each team member, verify their Vercel account is connected to their git provider.

Confirm bot commits are properly configured by the git provider.

Collaboration is free for public repositories.

## [Team configuration](#team-configuration)

### [Hobby teams](#hobby-teams)

The [Hobby Plan](/docs/plans/hobby) does not support collaboration for private repositories. If you need collaboration, upgrade to the [Pro Plan](/docs/plans/pro).

To deploy commits under a Hobby team, the commit author must be the owner of the Hobby team containing the Vercel project connected to the Git repository. This is verified by comparing the [Login Connections](/docs/accounts#login-methods-and-connections) Hobby team's owner with the commit author.

To make sure we can verify your commits:

1.  Make sure all commits are authored by the git user associated with your account.
2.  Link your git provider to your Vercel account in [Account Settings](/docs/accounts#sign-up-with-a-git-provider)

If your account is not connected to your git provider, make sure you've properly configured your [Vercel email address](/docs/accounts#managing-emails) so that it matches the email associated with the commit.

For the most reliable experience, ensure both your project and account are properly connected to your git provider.

For more information, see [Using Hobby teams](/docs/git#using-hobby-teams)

### [Pro teams](#pro-teams)

The [Pro Plan](/docs/plans/pro) allows for collaboration through team membership. Each person committing to your codebase should be added as a team member.

To deploy commits under a Vercel Pro team, the commit author must be a member of the team containing the Vercel project connected to the Git repository.

To make sure we can verify commits associated with your team:

1.  Each person committing code can be [added as a team member](/docs/rbac/managing-team-members).
2.  Make sure the commit author is a confirmed [member of your team](/docs/accounts#team-membership).
3.  Team members should link their git provider to their Vercel account in [Account Settings](/docs/accounts#sign-up-with-a-git-provider)

For more information, see [Using Pro teams](/docs/git#using-pro-teams)

### [Bot access](#bot-access)

Ensure your bots are properly configured and that their commits are clearly identified as automated.

## [Account configuration](#account-configuration)

### [Connecting Git provider accounts](#connecting-git-provider-accounts)

Each team member must connect their git provider account to their Vercel account:

1.  Visit [Account Settings](https://vercel.com/account/settings/authentication)
2.  Navigate to the [Login Connections](/docs/accounts#login-methods-and-connections) section
3.  Connect your GitHub, GitLab, or Bitbucket account

### [Managing multiple email addresses](#managing-multiple-email-addresses)

If you use multiple email addresses for git commits, you will need to configure a secondary email address with either your git provider or Vercel depending on if your git repository is linked to your project.

To add secondary email addresses to your Vercel account:

1.  Go to your [Account Settings](https://vercel.com/account/settings#email)
2.  Add any email addresses you use for git commits
3.  Verify each email address

--------------------------------------------------------------------------------
title: "Exclude Files from Deployments with .vercelignore"
description: "The .vercelignore file allows you to define which files and directories should be ignored when uploading your project to Vercel."
last_updated: "null"
source: "https://vercel.com/docs/deployments/vercel-ignore"
--------------------------------------------------------------------------------

# Exclude Files from Deployments with .vercelignore

Copy page

Ask AI about this page

Last updated March 12, 2025

The `.vercelignore` file can be used to specify files and directories that should be excluded from the deployment process when using Vercel. This file works similarly to a `.gitignore` file, but it is specific to Vercel.

The `.vercelignore` file should be placed in the root directory of your project and should contain a list of files and directories, one per line, that should be excluded from deployment. For example, to prevent an `/image` directory and `/private.html` file within a project from being uploaded to Vercel, you would add them to the `.vercelignore` file like this:

.vercelignore

```
image
private.html
```

## [Allowlist](#allowlist)

A typical `.vercelignore` file assumes all files are allowed and each entry is a pattern to ignore. Alternatively, you can ignore all files and each entry is a pattern to allow.

Add a wildcard `/*` as the first line in `.vercelignore` to ensure all directories and files in the project root are ignored. The following lines must then start with a `!` to invert the ignore action and ensure the directory or file is allowed.

.vercelignore

```
# Ignore everything (folders and files) on root only
/*
!api
!vercel.json
!*.html
```

## [Uploaded Files](#uploaded-files)

Aside from the [default exclusions](/docs/deployments/build-features#ignored-files-and-folders), all files within your project are uploaded to Vercel if no source path is specified to be excluded in a `.vercelignore` configuration file

The complete list of files and directories excluded by default can be found in the [ignored files and folders](/docs/deployments/build-features#ignored-files-and-folders) documentation.

## [Served Files](#served-files)

The use of a `.vercelignore` configuration file allows you to keep private files safe and also makes your deployment faster by uploading only the essential files. Non-targeted files are prevented from being deployed and served on Vercel.

## [Monorepos](#monorepos)

If you have a monorepo, a `.vercelignore` in the project root directory always takes precedence over one that is defined at the root level. If there is no `.vercelignore` to be found at the project level, Vercel will use the `.vercelignore` at the root level.

--------------------------------------------------------------------------------
title: "Using the Directory Listing"
description: "The Directory Listing is served when a particular path is a directory and does not contain an index file. Learn how to toggle and disable it in this guide."
last_updated: "null"
source: "https://vercel.com/docs/directory-listing"
--------------------------------------------------------------------------------

# Using the Directory Listing

Copy page

Ask AI about this page

Last updated September 24, 2025

The Directory Listing setting enables you to display the contents of a directory when a user visits its path. For example, if you create a directory at the root of your project called `/assets`, then when people visit `https://your-site.com/assets`, they will see the files and folders within that directory, as shown in the example below:

![The contents of a /assets directory.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-page-light.png&w=1920&q=75)![The contents of a /assets directory.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-dark2.png&w=1920&q=75)

The contents of a /assets directory.

You can enable or disable Directory Listing from the Advanced tab in your project settings.

![Directory Listing for an example /assets directory.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-light.png&w=3840&q=75)![Directory Listing for an example /assets directory.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fprojects%2Fdirectory-listing-dark.png&w=3840&q=75)

Directory Listing for an example /assets directory.

When enabled, the Directory Listing will be displayed. When disabled, a "Not Found" error will be displayed with status code `404`.

If Directory Listing isn't working, navigate to your deployment in the dashboard and select the **Source** tab to view the contents of your project. Ensure the expected directory and files are listed.

### [Disabling Directory Listing on a specific directory](#disabling-directory-listing-on-a-specific-directory)

To prevent Directory Listing for a specific path, you can either:

*   Add an index file with any extension except `.css`, such as `index.html`. This file will be displayed instead of the Directory Listing
*   Or, [set up a custom 404 error](/guides/custom-404-page)

--------------------------------------------------------------------------------
title: "Directory Sync"
description: "Learn how to configure Directory Sync for your Vercel Team."
last_updated: "null"
source: "https://vercel.com/docs/directory-sync"
--------------------------------------------------------------------------------

# Directory Sync

Copy page

Ask AI about this page

Last updated October 30, 2025

Directory Sync is available on [Enterprise plans](/docs/plans/enterprise)

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

Directory Sync helps teams manage their organization membership from a third-party identity provider like Google Directory or Okta. Directory Sync is only available for Enterprise Teams and can only be configured by [Team Owners](/docs/rbac/access-roles#owner-role).

When Directory Sync is configured, changes to your Directory Provider will automatically be synced with your [team members](/docs/rbac/managing-team-members). The previously existing permissions/roles will be overwritten by Directory Sync, including current user performing the sync.

Make sure that you still have the right permissions/role after configuring Directory Sync, [otherwise you might lock yourself out.](#preventing-account-lockout)

All team members will receive an email detailing the change. For example, if a new user is added to your Okta directory, that user will automatically be invited to join your Vercel Team. If a user is removed, they will automatically be removed from the Vercel Team.

You can configure a mapping between your Directory Provider's groups and a Vercel Team role. For example, your Engineers group on Okta can be configured with the [member](/docs/rbac/access-roles#member-role) role on Vercel, and your Admin group can use the [owner](/docs/rbac/access-roles#owner-role) role.

## [Configuring Directory Sync](#configuring-directory-sync)

To configure directory sync for your team:

1.  Ensure your team is selected in the [scope selector](/docs/dashboard-features)
2.  From your team's dashboard, select the Settings tab, and then Security & Privacy
3.  Under SAML Single Sign-On, select the Configure button. This opens a dialog to guide you through configuring Directory Sync for your Team with your Directory Provider.
4.  Once you have completed the configuration walkthrough, configure how Directory Groups should map to Vercel Team roles:
    
    ![Setting the Okta Admins group as Vercel owners and the Engineers group as Vercel Members.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fdsync-roles.png&w=1080&q=75)![Setting the Okta Admins group as Vercel owners and the Engineers group as Vercel Members.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fdsync-roles-dark.png&w=1080&q=75)
    
    Setting the Okta Admins group as Vercel owners and the Engineers group as Vercel Members.
    
5.  Finally, an overview of all synced members is shown. Click Confirm and Sync to complete the syncing:
    
    ![An overview of Team owners and Members that will be added.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fdsync-confirmation.png&w=1080&q=75)![An overview of Team owners and Members that will be added.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fdsync-confirmation-dark.png&w=1080&q=75)
    
    An overview of Team owners and Members that will be added.
    
6.  Once confirmed, Directory Sync will be successfully configured for your Vercel Team.

SAML Single Sign-On is optionally available on the Enterprise plan, or as a paid add-on for the Pro plan. To enable, Enterprise teams can contact [sales](https://vercel.com/contact/sales), and Pro teams can purchase the add-on from their team's [Billing settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling%23paid-add-ons).

### [Supported providers](#supported-providers)

See [SAML Single Sign-On](/docs/saml#saml-providers) for a list of all the SAML providers that Vercel supports.

## [Preventing account lockout](#preventing-account-lockout)

To prevent account lockout ensure that at least one person in your team has the owner role, and that they are not removed from the team.

If access is lost due to removal of team owners, use the following group names to automatically allocate the corresponding roles to individuals in that group:

| Group name | Role |
| --- | --- |
| `vercel-role-owner` | [Owner](/docs/rbac/access-roles#owner-role) |
| `vercel-role-member` | [Member](/docs/rbac/access-roles#member-role) |
| `vercel-role-developer` | [Developer](/docs/rbac/access-roles#developer-role) |
| `vercel-role-billing` | [Billing](/docs/rbac/access-roles#billing-role) |
| `vercel-role-viewer` | [Viewer Pro](/docs/rbac/access-roles#pro-viewer-role) or [Viewer Enterprise](/docs/rbac/access-roles#enterprise-viewer-role) |
| `vercel-role-contributor` | [Contributor](/docs/rbac/access-roles#contributor-role) |

--------------------------------------------------------------------------------
title: "Domains Overview"
description: "Learn the fundamentals of how domains, DNS, and nameservers work on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/domains"
--------------------------------------------------------------------------------

# Domains Overview

Copy page

Ask AI about this page

Last updated September 24, 2025

A domain is a user-friendly way of referring to the address access a website on the internet. For example, the domain you're reading this on is `vercel.com`. Domains can be analogous to the address where your house is. When someone sends a letter to your house, they don't need to know exactly _where_ it is, they just need the address and the relevant post office handles routing the letter.

The system that manages the details about where a site is located on the internet, is known as DNS or the Domain Name System. At its most basic, DNS maps human-readable domain names to computer-friendly IP addresses. When you request a site in your browser, the first step is converting the domain address to an IP address. That process is handled by DNS and called DNS Resolution. Understanding how DNS works is important to ensure that you are configuring your domain correctly.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-request.png&w=3840&q=75)

Diagram showing the a basic DNS query.

1.  You enter `vercel.com` in your browser. Your browser will first check its local DNS cache to see if it knows the IP address of `vercel.com`. If it does, it will request the site from that address.
    
2.  Your browser initiates a DNS query through a server known as a recursive resolver, usually provided by your ISP or a third-party. The recursive resolver acts as a middleman between the browser and DNS server and is used to increase the speed and efficiency of the resolution process. The resolver will check its cache first to see if it already has the IP address. If it doesn't, it'll request the IP address from a DNS server.
    
3.  There is a network of DNS servers, in a hierarchy, located all around the world. The recursive resolver will query in the following pattern:
    
    *   At the entrance to the network are 13 root nameservers. These are the servers that will be contacted first. The root server will look at the domain name, and based on the TLD or top-level domain (.com, .co.uk, etc.), will direct the resolver to the correct TLD server.
    *   The TLD nameservers store information about domain names that belong to the same TLD. For example, when searching for `vercel.com`, once the recursive resolver receives a response from the root nameserver, it will query the `.com` TLD nameserver.
    *   This TLD server will then respond resolver with details about the authoritative nameserver that has the IP address mapping for `vercel.com` stored in an A record. The authoritative nameserver returns this record to the recursive resolver, which will cache the result and return it to your browser.
4.  Once your browser has the IP address, an HTTP request is made by the browser to the web server located at that IP address.
    

This list is just a general overview and doesn't happen every time. Most of us tend to visit the same sites over and over. Therefore, the request will first check the cache from your browser and then from the recursive resolver, allowing for quicker load times. In addition, this example describes a basic unicast DNS network. In reality, when using Vercel, you're using anycast servers on the Vercel CDN.

This overview shows a point of view of a user visiting your site. But what does this look like when you're the developer creating a site?

When you've created a Project and deployed it on Vercel, your site lives on Vercel's web servers, which we know to be at the IP address `76.76.21.21`. However, your user's browser doesn't know that. For this reason, the browser will perform a DNS Lookup to retrieve the correct IP mapping to `yoursiteaddress.com` from a DNS server.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fvercel-dns-request.png&w=3840&q=75)

Diagram showing the Vercel-hosted query.

This is where, as a developer, you may have to configure the DNS settings to tell the authoritative server exactly where your site lives. Vercel [guides you through](/docs/domains/add-a-domain) exactly what information you need to set, within your Dashboard. There are a number of different settings that you should be aware of:

*   DNS records: DNS records are an entry in a database that maps the domain with the IP address, which is then stored on the authoritative server. Some of the most common record types are: CNAME (Canonical name), A (Address), NS (nameserver), and MX (mail exchange). These are all described in more detail in [Working with DNS](/docs/domains/working-with-dns).
*   Nameserver: Nameservers are an important part of the DNS. They refer to the _actual_ server that maintains and manages the DNS records. There are three types of nameservers: root nameserver, TLD nameserver, and the authoritative server. You can learn more about using a nameserver with Vercel in [Working with nameservers](/docs/domains/working-with-nameservers).
*   SSL Certificates: SSL Certificates are a way to show that there is a secure connection from your domain to your website. These are described in more detail in [Working with SSL certificates](/docs/domains/working-with-ssl).

## [More resources](#more-resources)

*   [Working with domains](/docs/domains/working-with-domains)
*   [Working with DNS](/docs/domains/working-with-dns)
*   [Working with nameservers](/docs/domains/working-with-nameservers)
*   [Working with SSL](/docs/domains/working-with-ssl)
*   [Troubleshooting domains](/docs/domains/troubleshooting)

--------------------------------------------------------------------------------
title: "Uploading Custom SSL Certificates"
description: "By default, Vercel provides all domains with a custom SSL certificates. However, Enterprise teams can upload their own custom SSL certificate."
last_updated: "null"
source: "https://vercel.com/docs/domains/custom-SSL-certificate"
--------------------------------------------------------------------------------

# Uploading Custom SSL Certificates

Copy page

Ask AI about this page

Last updated September 24, 2025

Uploading Custom SSL Certificates are available on [Enterprise plans](/docs/plans/enterprise)

By default, Vercel provides all domains with custom SSL certificates. However, Enterprise teams can upload a custom SSL certificate. This allows for Enterprise teams to serve their own SSL certificate on a Custom Domain at Vercel's edge network, rather than the automatically generated certificate.

Custom SSL certificates can be uploaded through the [Domains tab on your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page), or by using the [Vercel REST API](/docs/rest-api/reference/endpoints/certs/upload-a-cert#upload-a-cert).

Uploading a custom certificate follows a three step process:

1.  Providing the private key for the certificate
2.  Providing the certificate itself
3.  Providing the Certificate Authority root certificate such as one of [Let's Encrypt's ISRG root certificates](https://letsencrypt.org/certificates/). This will be provided by your certificate issuer and is different to the core certificate. This may be included in their download process or available for download on their website.

The content of each element must be copied and pasted into the input box directly. The certificate and private key can be extracted from the [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) files that are provided by your certificate issuer, and should be in the following format:

certificate.pem

```
-----BEGIN CERTIFICATE-----
<Certificate body will be here>
-----END CERTIFICATE-----
```

private-key.pem

```
-----BEGIN PRIVATE KEY-----
<Private key body will be here>
-----END PRIVATE KEY-----
```

## [SSL best practices](#ssl-best-practices)

When uploading your SSL certificate, you should note the following:

1.  The automatically generated certificate will remain in place, but a custom certificate is prioritized over the existing certificate. This means that if a custom certificate is uploaded and then later removed, Vercel will revert to the automatically generated certificate.
2.  You can include canonical names CN's (CN's) for other subdomains on the certificate without needing to add these domains to Vercel. The certificate will be served on these domains if or when they are added.
3.  Wildcards certificates can be uploaded.
4.  Certificates with an explicitly defined subdomain are prioritized over a wildcard certificate when both are valid for a given subdomain.
5.  Vercel cannot automatically renew custom certificates. If a custom certificate is within 5 days of expiration, an automatically generated certificate will be served in its place to prevent downtime.

--------------------------------------------------------------------------------
title: "Managing DNS Records"
description: "Learn how to add, verify, and remove DNS records for your domains on Vercel with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/managing-dns-records"
--------------------------------------------------------------------------------

# Managing DNS Records

Copy page

Ask AI about this page

Last updated September 24, 2025

Once you've added a domain and it's using Vercel's nameservers, you can view its DNS records from your team's [Domains page](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page). From there, you can view, [add](#adding-dns-records), [verify](#verifying-dns-records), [remove the records](#removing-dns-records), or add [presets](#dns-presets).

To make sure DNS records are applied, and to allow you to manage them, your domain needs to use [Vercel's nameservers](/docs/domains/managing-nameservers) . If you are using a third-party domain, you will be provided with the Vercel nameservers to copy and use with your registrar.

## [Adding DNS Records](#adding-dns-records)

1.  ### [Selecting your Domain](#selecting-your-domain)
    
    On your team's [dashboard](/dashboard), select the Domains tab. From the Domains page, click on a domain of your choice to view its Advanced Settings page.
    
2.  ### [Add DNS Record](#add-dns-record)
    
    Once on the Advanced Settings page of your domain, select the Enable Vercel DNS button to fill out the DNS Record form. Once complete, click on the Add button.
    
    ![DNS Records form to add a new DNS Record.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-records-form.png&w=3840&q=75)![DNS Records form to add a new DNS Record.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-records-form-dark.png&w=3840&q=75)
    
    DNS Records form to add a new DNS Record.
    
    You can then create a new DNS record with the following data:
    
    *   Name: The prefix or location of the record. For [www.example.com](http://www.example.com), the name argument would be [www](http://www).
        
    *   Type: Types can be `A`, `AAAA`, `ALIAS`, `CAA`, `CNAME`, `HTTPS`, `MX`, `NS`, `SRV`, or `TXT`.
        
    *   Value: The value of the record.
        
    *   TTL: Default is 60 seconds. For advanced users, this value can be customized.
        
    *   Comment: An optional comment to provide context on what this record is for.
        
    *   More: Some records will require more data. MX records, for example, will request "priority".
        
        Once a DNS record has been added, it can take up to 24 hours to the DNS records to fully update and any local caches to be cleared.
        

## [Verifying DNS Records](#verifying-dns-records)

Once DNS records have been changed, you may wish to check that these have been set correctly. There are many third-party tools that do this, such as DNS Checker and DNS Map - these show the state of your DNS records in different regions of the world.

You can also use the `dig` command to check the DNS record for your domain:

terminal

```
$ dig A api.example.com +short
```

Verifying the A record set for a domain using the terminal.

terminal

```
$ dig MX example.com +short
```

Verifying the MX record set for a domain using the terminal.

## [Removing DNS Records](#removing-dns-records)

To remove DNS records:

1.  On your team's [dashboard](/dashboard), select the [Domains tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page). From the Domains page, click on a domain of your choice to view its Advanced Settings page.
2.  Select the ellipsis (⋯) to access the context menu and select Delete DNS Zone. Follow the prompts to delete the record.

Default records can't be removed. However, new records can override them if required.

![Removing a DNS record from the DNS UI.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdelete-dns-record.png&w=3840&q=75)![Removing a DNS record from the DNS UI.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdelete-dns-record-dark.png&w=3840&q=75)

Removing a DNS record from the DNS UI.

## [DNS Presets](#dns-presets)

Vercel does not provide an email service. To be able to receive emails or add specific DNS configurations through a domain that you've added to Vercel, you need to add the respective DNS Records, such as MX for email or TXT for other services.

Vercel streamlines this process for common third-party services by allowing you to add missing DNS Records using DNS Presets on your dashboard.

1.  From your [dashboard](/dashboard), navigate to the Domains tab.
2.  Select the domain you wish to add a preset to and click the Add DNS Preset dropdown on the right:
    
    ![Adding a DNS Preset by clicking the Add DNS Preset button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-presents-light.png&w=640&q=75)![Adding a DNS Preset by clicking the Add DNS Preset button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-presets-dark.png&w=640&q=75)
    
    Adding a DNS Preset by clicking the Add DNS Preset button.
    
3.  You will be presented with a list of commonly used third-party providers. If your provider is listed, select it, and the necessary DNS Records—such as MX for email or TXT for other services like [Bluesky](/guides/use-my-domain-bluesky) will automatically be configured on your domain.

If your provider is not listed, please refer to their documentation to find out which DNS Records you need to add.

## [Migrating DNS records from an external registrar](#migrating-dns-records-from-an-external-registrar)

Once you have added a [domain to your Vercel project](https://vercel.com/docs/concepts/projects/custom-domains) and also verified the certificate is working as expected, you can choose three options of records to finally complete the migration: A, CNAME, or Nameservers. In case you decide to use an A or a CNAME record, then you can change those records in your DNS provider to make Vercel serve your deployment from the selected domain, as instructed on your dashboard.

If you decide to change the Nameservers of your domain, you can follow the below instructions which will help you migrate your DNS configuration from any provider and avoid downtime.

### [Clone the Current DNS Configuration](#clone-the-current-dns-configuration)

To locate the current DNS provider of your domain, you can run the following command:

terminal

```
$ dig NS example.com +short
```

Checking the DNS authority for a domain using the terminal.

The result will show the current DNS authority. Next, you'll need to locate your DNS records from the provider's dashboard.

After you've successfully located all records associated with your domain, you may now add them to Vercel. You can either do this manually or by importing a zone file.

Importing a zone file

If you have downloaded a zone file from your existing file, you may use the following comand to upload that to Vercel:

```
vercel dns import [your-domain] [zonefile]
```

If you do not apply a custom zone file, transferring in a domain automatically applies the default Vercel DNS settings.

### [Verify the Records](#verify-the-records)

To verify the records, you can now query the DNS configuration that will be served by Vercel:

terminal

```
$ dig A api.example.com +short @ns1.vercel-dns.com
```

Checking the DNS configuration of the A record under "api" served by Vercel.

Then, check the DNS records from the existing provider to make sure they match. If you were moving your DNS from [Cloudflare](https://vercel.com/docs/integrations/cloudflare), for example, the correct command would be:

terminal

```
$ dig A api.example.com +short @example.ns.cloudflare.com
```

Checking the DNS configuration of the A record under "api" served by Cloudflare. The example should be replaced with the authoritative nameserver given by your provider.

Before proceeding, we recommend checking every record you moved. For more insight into the DNS resolution, remove the `+short` flag.

### [Switch the Nameservers](#switch-the-nameservers)

In your registrar's dashboard (where you bought the domain), change the Nameservers to your new provider. Nameserver changes can take up to 48 hours to propagate. If you bought the domain from Vercel, you can [manage nameservers](https://vercel.com/docs/concepts/projects/domains/managing-nameservers) from the [domains page](https://vercel.com/dashboard/domains).

--------------------------------------------------------------------------------
title: "Managing Nameservers"
description: "Learn how to add custom nameservers and restore original nameservers for your domains on Vercel with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/managing-nameservers"
--------------------------------------------------------------------------------

# Managing Nameservers

Copy page

Ask AI about this page

Last updated September 24, 2025

[Nameservers](/docs/domains/working-with-nameservers) are used to resolve domain names to IP addresses. For domains with Vercel as the registrar, nameservers can be viewed, edited, and reset by selecting the domain from the [Domains tab of your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page).

Sometimes, however, you may need to delegate nameserver management to another host. For domains registered with Vercel, you can [add custom nameservers](#add-custom-nameservers) to your Vercel-hosted domain, directly from the dashboard, allowing for delegation to other DNS providers. You can add up to four nameservers at once, and [revert to your previous settings](#restore-original-nameservers) if necessary.

For domains that are not registered with Vercel, you can change the nameservers directly from the domain registrar's dashboard.

Nameserver changes can take up to 48 hours to complete due to [DNS propagation](https://ns1.com/resources/dns-propagation).

## [Add custom nameservers](#add-custom-nameservers)

1.  Ensure your account or team is selected in the scope selector
    
2.  Navigate to the Domains tab and select the domain
    
3.  On your domain's settings page, under Nameservers, click the Edit button:
    
    ![Nameservers section showing the Edit button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fnameservers.png&w=3840&q=75)![Nameservers section showing the Edit button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fnameservers-dark.png&w=3840&q=75)
    
    Nameservers section showing the Edit button.
    
4.  In the Edit Nameservers modal, add the new nameservers:
    
    ![Adding custom nameservers on the Edit Nameservers modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fedit-nameservers.png&w=1080&q=75)![Adding custom nameservers on the Edit Nameservers modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fedit-nameservers-dark.png&w=1080&q=75)
    
    Adding custom nameservers on the Edit Nameservers modal.
    

## [Add Vercel's nameservers](#add-vercel's-nameservers)

Before using Vercel's nameservers, you should ensure that you own the domain.

1.  Ensure your account or team is selected in the scope selector
2.  Navigate to the Domains tab and select the domain
3.  On your domain's settings page, under DNS Records, click the Enable Vercel DNS button to opt in
4.  You then must configure the following nameservers from the domain registrar's dashboard

*   `ns1.vercel-dns.com`
*   `ns2.vercel-dns.com`

## [Restore original nameservers](#restore-original-nameservers)

1.  Ensure your account or team is selected in the scope selector
2.  Navigate to the Domains tab and select the domain
3.  Under Nameservers, select the Restore Original Nameservers button
4.  On the Restore Original Nameservers modal confirm the nameservers that will be present after the change

Vercel will present a message when you have successfully submitted the nameserver change.

![Restoring original nameservers by clicking the Restore button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Frestore-original-nameservers.png&w=1080&q=75)![Restoring original nameservers by clicking the Restore button.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Frestore-original-nameservers-dark.png&w=1080&q=75)

Restoring original nameservers by clicking the Restore button.

--------------------------------------------------------------------------------
title: "Pre-Generate SSL Certificates"
description: "test"
last_updated: "null"
source: "https://vercel.com/docs/domains/pre-generating-ssl-certs"
--------------------------------------------------------------------------------

# Pre-Generate SSL Certificates

Copy page

Ask AI about this page

Last updated October 2, 2025

This page is part the domains transfer experience. See [this page](/docs/domains/working-with-domains/transfer-your-domain#transfer-a-domain-to-vercel) for the full set of steps to transfer a domain to Vercel.

This article guides you through all the steps necessary to set up SSL certificates for a domain being migrated to Vercel without downtime. Your domain should be serving content from 3rd party servers that are unrelated to Vercel, and you need to be prepared to make the necessary DNS changes.

You can do this using either the Vercel Domains dashboard, or the [Vercel CLI](/docs/cli).

## [Generating a Certificate](#generating-a-certificate)

In order to issue certificates through the dashboard for a domain, first ensure the domain belongs to a team. You can then click into the domain management page, scroll down to "SSL Certificates" and click "Pre-generate SSL certificates". Please note this option is only available if you do not already have any SSL certificates issued for the domain.

![Pre-Generate button found under the SSL Certificates section of the Domain configuration page](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fssl-pregen-light.png&w=3840&q=75)![Pre-Generate button found under the SSL Certificates section of the Domain configuration page](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fssl-pregen-dark.png&w=3840&q=75)

Pre-Generate button found under the SSL Certificates section of the Domain configuration page

If you choose to do this through the terminal, you can run the following command to get the challenge records for your domain:

terminal

```
vercel certs issue "*.example.com" example.com --challenge-only
```

Creating the challenge for the certificate that will be used for \*.example.com and example.com.

## [Setting your DNS records and finalizing](#setting-your-dns-records-and-finalizing)

In order to verify ownership of your domain, copy the TXT records into your DNS on the registrar you are using.

Click "Verify" to verify that the records have been set and issue the certificate. DNS records can take time to propagate, so if it doesn't work immediately, it's worth waiting for the records to propagate before taking further action.

![Copy certificates modal containing the TXT records to copy into your DNS registrar](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fcopy-challenges-light.png&w=750&q=75)![Copy certificates modal containing the TXT records to copy into your DNS registrar](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fcopy-challenges-dark.png&w=750&q=75)

Copy certificates modal containing the TXT records to copy into your DNS registrar

To check whether the TXT records have propagated, you can use the following command in a terminal of your choice:

terminal

```
nslookup -type=TXT example.com
```

Looking up the TXT records for example.com

Once TXT records have propagated, you can click "Verify" to issue the SSL certificates.

If you choose to issue SSL certificates through the terminal, you can run the command previously used without the `--challenge-only` flag:

terminal

```
vercel certs issue "*.example.com" example.com
```

Issuing a certificate that covers both \*.example.com and example.com.

## [Verifying the Certificate](#verifying-the-certificate)

Before you change the DNS records of your domain, you can verify if the certificate is correct and will be accepted by browsers. Run the following command:

terminal

```
curl https://example.com --resolve example.com:443:76.76.21.21 -I
```

curl command that sends a request directly to Vercel, ignoring the DNS configuration of the domain.

If the request is successful, the certificate is working and you can proceed with the migration.

## [Finishing connecting your domain to Vercel](#finishing-connecting-your-domain-to-vercel)

To migrate your deployment to Vercel, add the provided A or CNAME record from your project’s Domain Settings page to your DNS configuration so your domain points to Vercel webservers. See [this detailed guide](/guides/a-record-and-caa-with-vercel) on using domains with A records for more information.

For more details on performing a migration, see [this guide](/docs/domains/managing-dns-records#migrating-dns-records-from-an-external-registrar).

--------------------------------------------------------------------------------
title: "Programmatic Domain Management"
description: "Programmatically search, price, purchase, renew, and manage domains with Vercel's domains registrar API endpoints."
last_updated: "null"
source: "https://vercel.com/docs/domains/registrar-api"
--------------------------------------------------------------------------------

# Programmatic Domain Management

Copy page

Ask AI about this page

Last updated October 8, 2025

The domains registrar API enables you to programmatically manage your domain lifecycle from search to renewal.

## [Getting started with the API](#getting-started-with-the-api)

You can start using the REST API by:

1.  [Creating a token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token)
    
2.  Using the token in either of the following ways:
    
    *   Use the [Vercel SDK](https://vercel.com/docs/rest-api/reference/sdk)
    
    In the following example, use the Vercel SDK to get the supported TLDs.
    
    index.ts
    
    ```
    import { Vercel } from '@vercel/sdk';
     
    const vercel = new Vercel({
      bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
    });
     
    const result = await vercel.domainsRegistrar.getSupportedTlds();
    ```
    
    *   Use the language of your choice by calling the endpoints directly and providing your token.
    
    In the following example, we use `cURL` to get the supported TLDs.
    
    terminal
    
    ```
    curl --request GET \
      --url https://api.vercel.com/v1/registrar/tlds/supported \
      --header 'Authorization: Bearer <token>'
    ```
    

You can use the domains registrar API to do the following:

### [Catalog & pricing](#catalog-&-pricing)

*   [List all supported top-level domains (TLDs)](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-supported-tlds)
*   [Get pricing for specific TLDs](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-tld-price-data)
*   [Retrieve per-domain pricing information](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain)

### [Availability](#availability)

*   [Check single domain availability](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-a-domain)
*   [Perform bulk availability checks for multiple domains](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-multiple-domains)

### [Orders & purchases](#orders-&-purchases)

*   [Purchase a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain)
*   [Execute bulk domain purchases](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains)
*   [Fetch order status by ID](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domain-order)

### [Transfers](#transfers)

*   [Retrieve authorization codes for domain transfers](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-the-auth-code-for-a-domain)
*   [Initiate domain transfers to Vercel](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain)
*   [Track transfer status and completion](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domains-transfer-status)

### [Management](#management)

*   [Renew domains before expiration](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/renew-a-domain)
*   [Enable or disable automatic renewal](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
*   [Update nameserver configurations](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain)
*   [Fetch TLD-specific contact information schemas](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema)

## [Deprecations and migration](#deprecations-and-migration)

The following legacy domains API endpoints are now deprecated and will be sunset on November 8, 2025:

*   [Purchase a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains/purchase-a-domain-deprecated)
*   [Check the price for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains/check-the-price-for-a-domain-deprecated)
*   [Check a Domain Availability](https://vercel.com/docs/rest-api/reference/endpoints/domains/check-a-domain-availability-deprecated)
*   [Get domain transfer info](https://vercel.com/docs/rest-api/reference/endpoints/domains/get-domain-transfer-info-deprecated)

If you are currently using the Vercel CLI for domain purchases, pricing, or availability, upgrade to CLI version `48.2.8` or later.

--------------------------------------------------------------------------------
title: "Supported domains for purchase"

last_updated: "null"
source: "https://vercel.com/docs/domains/supported-domains"
--------------------------------------------------------------------------------

# Supported domains for purchase

Copy page

Ask AI about this page

Last updated March 4, 2025

Vercel supports the following top-level domains (TLDs) for [purchase](/docs/domains/working-with-domains#buying-a-domain-through-vercel) as custom domains:

## [A](#a)

*   .ac
*   .academy
*   .accountant
*   .accountants
*   .actor
*   .adult
*   .ag
*   .agency
*   .ai
*   .airforce
*   .am
*   .apartments
*   .app
*   .archi
*   .army
*   .art
*   .asia
*   .associates
*   .attorney
*   .auction
*   .audio
*   .auto
*   .autos

## [B](#b)

*   .baby
*   .band
*   .bar
*   .bargains
*   .bayern
*   .be
*   .beauty
*   .beer
*   .best
*   .bet
*   .bid
*   .bike
*   .bingo
*   .bio
*   .biz
*   .black
*   .blackfriday
*   .blog
*   .blue
*   .boats
*   .bond
*   .boo
*   .boston
*   .bot
*   .boutique
*   .br.com
*   .broker
*   .build
*   .builders
*   .business
*   .buzz
*   .bz

## [C](#c)

*   .ca
*   .cab
*   .cafe
*   .cam
*   .camera
*   .camp
*   .capital
*   .car
*   .cards
*   .care
*   .careers
*   .cars
*   .casa
*   .cash
*   .casino
*   .catering
*   .cc
*   .center
*   .ceo
*   .cfd
*   .ch
*   .channel
*   .charity
*   .chat
*   .cheap
*   .christmas
*   .church
*   .city
*   .cl
*   .claims
*   .cleaning
*   .click
*   .clinic
*   .clothing
*   .cloud
*   .club
*   .cm
*   .cn
*   .cn.com
*   .co
*   .co.com
*   .co.nz
*   .coach
*   .codes
*   .coffee
*   .college
*   .com
*   .com.cn
*   .com.co
*   .com.mx
*   .com.tw
*   .community
*   .company
*   .computer
*   .condos
*   .construction
*   .consulting
*   .contact
*   .contractors
*   .cooking
*   .cool
*   .country
*   .coupons
*   .courses
*   .credit
*   .creditcard
*   .cricket
*   .cruises
*   .cx
*   .cz

## [D](#d)

*   .dad
*   .dance
*   .date
*   .dating
*   .day
*   .de.com
*   .deal
*   .dealer
*   .deals
*   .degree
*   .delivery
*   .democrat
*   .dental
*   .dentist
*   .design
*   .dev
*   .diamonds
*   .diet
*   .digital
*   .direct
*   .directory
*   .discount
*   .diy
*   .dk
*   .doctor
*   .dog
*   .domains
*   .download

## [E](#e)

*   .earth
*   .ec
*   .education
*   .email
*   .energy
*   .engineer
*   .engineering
*   .enterprises
*   .equipment
*   .esq
*   .estate
*   .eu.com
*   .eus
*   .events
*   .exchange
*   .expert
*   .exposed
*   .express

## [F](#f)

*   .fail
*   .faith
*   .family
*   .fan
*   .fans
*   .farm
*   .fashion
*   .feedback
*   .film
*   .finance
*   .financial
*   .fish
*   .fishing
*   .fit
*   .fitness
*   .flights
*   .florist
*   .flowers
*   .fm
*   .foo
*   .food
*   .football
*   .forex
*   .forsale
*   .forum
*   .foundation
*   .free
*   .fun
*   .fund
*   .furniture
*   .futbol
*   .fyi

## [G](#g)

*   .gallery
*   .game
*   .games
*   .garden
*   .gay
*   .gent
*   .gift
*   .gifts
*   .gives
*   .giving
*   .glass
*   .global
*   .gmbh
*   .gold
*   .golf
*   .gr.com
*   .graphics
*   .gratis
*   .green
*   .gripe
*   .group
*   .gs
*   .guide
*   .guitars
*   .guru
*   .gy

## [H](#h)

*   .hair
*   .hamburg
*   .haus
*   .healthcare
*   .help
*   .hiphop
*   .hiv
*   .hn
*   .hockey
*   .holdings
*   .holiday
*   .homes
*   .horse
*   .hospital
*   .host
*   .hosting
*   .hot
*   .house
*   .how

## [I](#i)

*   .icu
*   .im
*   .immo
*   .immobilien
*   .inc
*   .industries
*   .info
*   .ing
*   .ink
*   .institute
*   .insure
*   .international
*   .investments
*   .io
*   .irish

## [J](#j)

*   .jetzt
*   .jewelry
*   .jobs
*   .jpn.com
*   .juegos

## [K](#k)

*   .kaufen
*   .kids
*   .kim
*   .kitchen
*   .kiwi

## [L](#l)

*   .la
*   .land
*   .lat
*   .lawyer
*   .lease
*   .legal
*   .lgbt
*   .li
*   .life
*   .lifestyle
*   .lighting
*   .limited
*   .limo
*   .link
*   .live
*   .living
*   .llc
*   .loan
*   .loans
*   .lol
*   .london
*   .lotto
*   .love
*   .ltd
*   .ltda
*   .luxe
*   .luxury

## [M](#m)

*   .maison
*   .makeup
*   .management
*   .market
*   .marketing
*   .markets
*   .mba
*   .me
*   .med
*   .media
*   .melbourne
*   .meme
*   .memorial
*   .men
*   .menu
*   .miami
*   .mn
*   .mobi
*   .moda
*   .moe
*   .moi
*   .mom
*   .money
*   .monster
*   .mortgage
*   .motorcycles
*   .mov
*   .movie
*   .mx
*   .my

## [N](#n)

*   .nagoya
*   .name
*   .navy
*   .net
*   .net.cn
*   .net.nz
*   .network
*   .new
*   .news
*   .nexus
*   .ngo
*   .ninja
*   .now
*   .nz

## [O](#o)

*   .observer
*   .okinawa
*   .one
*   .ong
*   .onl
*   .online
*   .ooo
*   .org
*   .org.nz
*   .organic
*   .osaka

## [P](#p)

*   .page
*   .paris
*   .partners
*   .parts
*   .party
*   .pet
*   .phd
*   .photo
*   .photography
*   .photos
*   .pics
*   .pictures
*   .pink
*   .pizza
*   .pl
*   .place
*   .plumbing
*   .plus
*   .pm
*   .poker
*   .porn
*   .press
*   .pro
*   .productions
*   .prof
*   .promo
*   .properties
*   .property
*   .pub
*   .pw

## [Q](#q)

*   .qpon
*   .quest

## [R](#r)

*   .racing
*   .radio.am
*   .radio.fm
*   .realty
*   .recipes
*   .red
*   .rehab
*   .reise
*   .reisen
*   .rent
*   .rentals
*   .repair
*   .report
*   .republican
*   .rest
*   .restaurant
*   .review
*   .reviews
*   .rich
*   .rip
*   .rocks
*   .rodeo
*   .rsvp
*   .ru.com
*   .run
*   .ryukyu

## [S](#s)

*   .sa.com
*   .sale
*   .salon
*   .sarl
*   .sbs
*   .sc
*   .school
*   .schule
*   .science
*   .se
*   .se.net
*   .services
*   .sex
*   .sexy
*   .sh
*   .shiksha
*   .shoes
*   .shop
*   .shopping
*   .show
*   .singles
*   .site
*   .ski
*   .skin
*   .so
*   .soccer
*   .social
*   .software
*   .solar
*   .solutions
*   .soy
*   .space
*   .spot
*   .srl
*   .storage
*   .store
*   .stream
*   .studio
*   .study
*   .style
*   .supplies
*   .supply
*   .support
*   .surf
*   .surgery
*   .sydney
*   .systems

## [T](#t)

*   .tattoo
*   .tax
*   .taxi
*   .team
*   .tech
*   .technology
*   .tel
*   .tennis
*   .theater
*   .theatre
*   .tickets
*   .tienda
*   .tips
*   .tires
*   .tl
*   .today
*   .tokyo
*   .tools
*   .top
*   .tours
*   .town
*   .toys
*   .trade
*   .trading
*   .training
*   .travel
*   .tube
*   .tv
*   .tw

## [U](#u)

*   .uk
*   .uk.com
*   .uk.net
*   .university
*   .uno
*   .us
*   .us.com

## [V](#v)

*   .vacations
*   .vana
*   .vc
*   .vegas
*   .ventures
*   .vet
*   .viajes
*   .video
*   .villas
*   .vin
*   .vip
*   .vision
*   .vodka
*   .vote
*   .voting
*   .voto
*   .voyage

## [W](#w)

*   .watch
*   .watches
*   .webcam
*   .website
*   .wedding
*   .wiki
*   .win
*   .wine
*   .work
*   .works
*   .world
*   .ws
*   .wtf

## [X](#x)

*   .xn--3ds443g
*   .xn--5tzm5g
*   .xn--6frz82g
*   .xn--80asehdb
*   .xn--80aswg
*   .xn--9dbq2a
*   .xn--czrs0t
*   .xn--e1a4c
*   .xn--fiq228c5hs
*   .xn--fjq720a
*   .xn--mk1bu44c
*   .xn--ngbc5azd
*   .xn--q9jyb4c
*   .xn--t60b56a
*   .xn--tckwe
*   .xn--unup4y
*   .xn--vhquv
*   .xyz

## [Y](#y)

*   .yachts
*   .yoga
*   .yokohama

## [Z](#z)

*   .za.com
*   .zip
*   .zone

--------------------------------------------------------------------------------
title: "Troubleshooting domains"
description: "Learn about common reasons for domain misconfigurations and how to troubleshoot your domain on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/domains/troubleshooting"
--------------------------------------------------------------------------------

# Troubleshooting domains

Copy page

Ask AI about this page

Last updated September 24, 2025

There are many common reasons why your domain configuration may not be working. Check the following:

*   Is your domain [added](/docs/domains/add-a-domain#add-and-configure-domain) to your Vercel project?
*   Is your custom domain pointed to the provided Vercel `CNAME`/`A` record correctly? You can check it by using `dig [example.com]` in your Terminal.
*   If you use the [nameservers method](/docs/domains/troubleshooting#configuring-nameservers-for-wildcard-domains) on your apex domain, please refer to your DNS provider's documentation for the exact instructions on how to change authoritative nameservers.
*   Is the issue only local to you? Try to clear your browser cache, and flush DNS caches on your machine/network if possible.

## [Misconfigured domain issues](#misconfigured-domain-issues)

When you add a domain to Vercel that you have purchased from a third-party DNS provider, you may see an Invalid Configuration alert. There are many reasons why this could be the case:

*   You need to configure the [DNS](#common-dns-issues) records of your domain with your DNS provider so they can be used with your project. To resolve this, follow the steps to [configure your domain](/docs/domains/add-a-domain#configure-the-domain).
*   If your domain is in use by another Vercel account, you may be prompted to [verify access to the domain](/docs/domains/add-a-domain#verify-domain-access) by adding a TXT record. This will not move the domain into your account, but will allow you to use it in your project.
*   There was an issue generating the SSL certificate for your domain. The most common reason for this is [missing CAA records](#missing-caa-records). For information on other issues that may cause this, see the [common SSL certificate issues](#common-ssl-certificate-issues) section.
*   You have configured [wildcard subdomains](/docs/domains/add-a-domain#using-wildcard-domain) on your project, but their nameservers aren’t with Vercel. When using a wildcard domain, you must use the [nameservers method](/docs/domains/troubleshooting#configuring-nameservers-for-wildcard-domains).

## [Common DNS issues](#common-dns-issues)

Vercel is expecting either an `A` record or a `CNAME` record. In your Project Settings under the Domain page, you’ll find the precise `CNAME` or `A` record values tailored to your project and plan. Once added, you can use the following commands on your Terminal to check the DNS records are correctly configured:

*   `dig ns [domain]` to get a domain’s nameservers
*   `dig a [apex domain e.g. example.com]` to get a domain’s `A` record
*   `dig cname [subdomain e.g. www.example.com]` to get a domain’s `CNAME` record

If you prefer a non-command-line interface, you can use a free online tool, such as [Google Public DNS](https://dns.google/). If any of these results do not match what is expected, follow the steps to [configure your domain](/docs/domains/add-a-domain#configure-the-domain).

### [Why are my DNS records taking so long to update?](#why-are-my-dns-records-taking-so-long-to-update)

DNS changes can take a while to propagate across the globe, depending on the previous DNS record TTL length. This may mean that certain regions can access your site as intended, while others wait until the DNS changes have reached them. Please allow some time for these changes to take effect.

For more information on [propagation times](/docs/domains/working-with-dns#dns-propagation) for nameservers and other DNS records, see "[How long will it take for my Vercel DNS records to update?](/guides/how-long-to-update-dns-records)"

Before changing your DNS records to point to Vercel, we recommend updating your existing DNS record to "lower" the TTL (for example 60 seconds) and waiting for the old TTL to expire. Lowering the current TTL and changing a DNS record after its TTL expiration period can ensure that you can quickly roll back the change if you encounter an issue. You can then increase the DNS record TTL to its original value once you confirm everything is working as expected.

### [IPv6 support](#ipv6-support)

While we allow the [creation](/docs/domains/managing-dns-records#adding-dns-records) of AAAA records when using Vercel's nameservers, we do not support IPv6 yet. This means if you are adding a [custom domain](/docs/domains/add-a-domain) from a [third-party](/docs/domains/working-with-domains#buying-a-domain-through-a-third-party), you won't be able to point an `AAAA` record to Vercel.

### [Syntax errors debugging](#syntax-errors-debugging)

When working with DNS records, you may make minor errors in the syntax. These errors can be difficult to debug. Below is a list of common errors made when adding DNS records and the steps required to resolve them.

#### [Using the domain as part of the Name argument](#using-the-domain-as-part-of-the-name-argument)

When you add a new DNS record to a domain, the Name field should use the prefix or location of the record. For `www.example.com`, the name argument would be `www`.

If you have already added a record with this, [remove the record](/docs/domains/managing-dns-records#removing-dns-records) from the DNS Records section of the Domains tab, and add the record again without the domain as the Name argument.

#### [Absolute CNAME records](#absolute-cname-records)

When you add a custom domain with a subdomain to your project, we'll prompt you to add a CNAME DNS record in order to configure the domain. This record _includes_ a period (.) at the end of the Value field. This is intentional to denote that it is an absolute, fully qualified domain name.

This means that when you add a new CNAME record to your DNS provider, you must copy the value exactly as it appears, including the period.

## [Common Nameserver issues](#common-nameserver-issues)

### [Configuring nameservers for wildcard domains](#configuring-nameservers-for-wildcard-domains)

When you add any custom domain to your Vercel project you must [configure](/docs/domains/add-a-domain#configure-the-domain) the DNS records with your DNS provider so it can be used with your project. When you add a wildcard domain (such as `*.example.com`), you must [use the Nameservers method](/docs/domains/add-a-domain#vercel-nameservers).

This is because Vercel needs to be able to set DNS records in order to generate the wildcard certificates. The service that Vercel uses to [generate the certificates](/docs/domains/working-with-ssl) requires us to verify the domain ownership by using the [DNS-01 challenge method](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge). By changing the nameservers, Vercel will handle the DNS-01 challenge for you automatically, and you don't need to update your verification DNS record upon your certificate renewal each time.

For more information, see [Why must we use the Domain Nameservers method for Wildcard Domains on Vercel?](https://vercel.com/guides/why-use-domain-nameservers-method-wildcard-domains)

## [Common domain issues](#common-domain-issues)

### [Domains and emails](#domains-and-emails)

When you buy a new domain, you may want to also set up an email address with this domain. Vercel does not provide a mail service for domains purchased with or transferred into it. To learn how to set up email, see [How do I send and receive emails with my Vercel purchased domain?](https://vercel.com/guides/using-email-with-your-vercel-domain)

When you add your custom domain to a project and use Vercel's nameservers, you will need to add `MX` records to continue receiving email. To learn how to add `MX` records, see [Why am I no longer receiving email after adding my domain to Vercel?](https://vercel.com/guides/why-has-email-stopped-working)

### [Purchasing a domain through Vercel](#purchasing-a-domain-through-vercel)

All domain purchases and renewals through Vercel are final and cannot be refunded once processed. For more information, see [Can I get a refund for a domain purchased or renewed with Vercel?](https://vercel.com/guides/can-i-get-a-refund-for-a-domain-purchased-or-renewed-with-vercel)

### [Pending domain purchases](#pending-domain-purchases)

It can take 3-5 days for a domain to fully register. If the domain is still not showing after 5 days, you can [contact support](/help).

### [Pending verification](#pending-verification)

If verification is needed, you will receive an email with instructions from Vercel. You will also see an alert on your team's domain page, which you can access through the [Domain Dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains%2F&title=). From there, you can resend the verification email or update your registrant information and email address.

### [Emoji and ASCII support](#emoji-and-ascii-support)

You will need to convert the domain to [punycode](https://www.punycoder.com) in order to add it to your project. For example, a user looking to add a domain such as `jérémie.fr` can do so in the form of `xn--jrmie-bsab.fr`.

### [Unable to transfer-in a domain](#unable-to-transfer-in-a-domain)

[ICANN](https://www.icann.org/) forces domain registrars to wait 60 days:

*   between transfers
*   between a new registration and a subsequent transfer

If you transfer before this time, the transfer will fail. Besides this restriction, some DNS providers may further restrict domain transferring by default as a security measure, unless the owner explicitly turns off their protection setting. Please refer to the DNS provider's documentation for more details.

### [Working with Apex domain](#working-with-apex-domain)

When you add an [apex domain](/docs/domains/working-with-domains#subdomains-wildcard-domains-and-apex-domains) (e.g. `example.com`) to your project, Vercel provides you with details, including an IP address, to add as an `A` record in your DNS configuration, as opposed to a `CNAME` record.

The main reason for that is the DNS [RFC1034](https://www.ietf.org/rfc/rfc1034.txt) (section 3.6.2) states that `If a CNAME RR is present at a node, no other data should be present`. Because an apex domain requires `NS` records and usually some other records, such as `MX` (for a mail service), adding a `CNAME` at the zone apex would violate this rule and likely cause an issue on your domain. Therefore, we encourage you to use an `A` record at your zone apex instead.

### [Does my domain IP address on Vercel resolve to a geographic region?](#does-my-domain-ip-address-on-vercel-resolve-to-a-geographic-region)

When you configure an apex domain (example.com) as a custom domain for your project on Vercel, Vercel will be give you an IP address to add as an A record in your DNS configuration. Although this IP address resolves to a specific geographic location, it does not mean that when your users point to your domain, they will be sent to this specific geographic location to resolve the domain.

This is because Vercel uses [Anycast](https://en.wikipedia.org/wiki/Anycast) IP addresses, which are shared across all regions. That means even if your users access your domain resolving to the same IP addresses from different geographic locations, they will be routed to the closest CDN region relative to your users, based on the BGP (Border Gateway Protocol).

### [Domain ownership errors](#domain-ownership-errors)

When you add a domain to your project, Vercel checks if it is already associated with a [Personal Account or Team](/docs/accounts). A domain can only be associated with _one_ Personal Account or Team at a time.

The following table shows errors that can be encountered when adding a domain to your project:

| Error Text | Description |
| --- | --- |
| `This team has already registered this domain` | The domain you are trying to add is already connected to the team you have selected. |
| `You have already registered this domain` | The domain you are trying to add is already connected to the Personal Account you have selected. |
| `The domain mydomain.com is not available` or `Another Vercel account is using this domain` | This error message states that the domain is owned by another Vercel account that you do not have access to. If you have ownership of the domain in question, contact Vercel [support](/help). |

## [Common SSL certificate issues](#common-ssl-certificate-issues)

There are many reasons why a certificate may not be generated. As the first starting point, we recommend testing your domain with:

1.  [Let's Debug](https://letsdebug.net): Let's Debug is a diagnostic tool/website to help figure out why you might not be able to issue a certificate for Let's Encrypt
2.  [DNSViz](https://dnsviz.net/): DNSViz is a tool suite for analysis and visualization of Domain Name System (DNS) behavior, including its security extensions (DNSSEC). They can also tell you about possible DNS misconfiguration.

For non-wildcard domains, we use [HTTP-01](https://letsencrypt.org/docs/challenge-types/#http-01-challenge) challenge by default, which Vercel handles automatically by intercepting the challenge requests from Let's Encrypt to your domain as long as the domain points to Vercel.

For wildcard domains, only [DNS-01](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) challenge is supported, which Vercel requires you to use the [nameservers method](/docs/domains/troubleshooting#configuring-nameservers-for-wildcard-domains) to handle DNS-01 challenge requests with Vercel's nameservers automatically.

### [Missing `CAA` records](#missing-caa-records)

Since we use Let's Encrypt for our automatic SSL certificates, you must add a `CAA` record with the value `0 issue "letsencrypt.org"` if other `CAA` records already exist on your domain.

You can check if your domain currently has any `CAA` records by running the `dig -t CAA +noall +ans example.com` command on your terminal, or check with [Google Public DNS](https://dns.google/) (change the `RR Type` to `CAA` and resolve).

For more information, see [Why is my domain not automatically generating an SSL certificate?](/guides/domain-not-generating-ssl-certificate)

### [Existing `_acme-challenge` record](#existing-_acme-challenge-record)

An `_acme-challenge` record allows Let's Encrypt to verify the domain ownership using [DNS-01](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) challenge. This may exist on your apex or subdomains, so can be checked with `dig -t TXT _acme-challenge.example.com` or `dig -t TXT _acme-challenge.subdomain.example.com`

If the domain was previously hosted on a different provider, and if the `_acme-challenge` record resolves to something, please consider [removing the DNS record](/docs/domains/managing-dns-records#removing-dns-records). This will prevent any provider (other than the one in the DNS record) from provisioning certificates for that domain.

### [Rewriting or redirecting `/.well-known`](#rewriting-or-redirecting-/.well-known)

The /.well-known path is reserved and cannot be redirected or rewritten. Only Enterprise teams can configure custom SSL. [Contact sales](/contact/sales) to learn more.

--------------------------------------------------------------------------------
title: "Working with DNS"
description: "Learn how DNS works in order to properly configure your domain."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-dns"
--------------------------------------------------------------------------------

# Working with DNS

Copy page

Ask AI about this page

Last updated October 2, 2025

DNS is the system used to connect domain names to IP addresses. When you make a request for a website, the browser performs a DNS query. It's usually the recursive resolver that carries out this work, going to the root DNS nameserver, TLD nameserver, and the authoritative server, if it isn't found in the cache.

![DNS configuration with multiple DNS record types](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-record-example.png&w=1920&q=75)![DNS configuration with multiple DNS record types](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fdns-record-example-dark.png&w=1920&q=75)

DNS configuration with multiple DNS record types

### [DNS records](#dns-records)

There are a number of different types of DNS records that can be used together to create a DNS configuration. Some of the common information that you might see in a DNS record are:

*   Host Name: The hostname of `www`
*   IP Address or URL: The IP address (or domain or in the case of a CNAME record), for example, `76.76.21.21` or `cname.vercel-dns-0.com`.
*   TTL (Time to live): The length of time the recursive server should keep a particular record in its cache. You should set this time based on how often people are visiting your site and how often your site may change. For more information, see the [DNS propagation](#dns-propagation) section.
*   Record Type: For example, `CNAME`. There are many different types of records, some of the most common are listed below.

To learn more about adding, verifying, and removing DNS records, see "[Managing DNS records](/docs/domains/managing-dns-records)".

| Type | Description |
| --- | --- |
| A | This is used to translate domain names into IPv4 addresses. It is the most common type of DNS record. |
| AAAA | Similar to `A`, but this is used to translate domain names into IPv6 addresses. IPv6 is not supported on Vercel. See [IPv6 support](/docs/domains/troubleshooting#ipv6-support) for more information. |
| ALIAS | This is used to map a domain name to another domain name. It is similar to a `CNAME` record, but can only be used at the zone apex. The target domain must return `A` or `AAAA` record. |
| CAA | This is used to specify which certificate authorities are allowed to issue certificates for a domain. Vercel automatically adds a CAA record for Let's Encrypt at the zone apex. |
| CNAME | This is used to specify that the domain name is an alias for another domain name. It cannot be used at the zone apex. See [Working with Apex domain](/docs/domains/troubleshooting#working-with-apex-domain) for more information. |
| HTTPS | This is used to achieve a CNAME-like functionality, but can be used at the zone apex. This is designed specifically for HTTP protocol to improve client performance in establishing secure connections. The record includes additional information about the target server, such as supported ALPN protocols (e.g., HTTP/2, HTTP/3, etc). This is a fairly new record type, and not all clients can support. See [RFC 9460](https://datatracker.ietf.org/doc/rfc9460/) for more details. |
| MX | This is used to specify the mail server for the domain. |
| NS | This is used to specify the authoritative name server for the domain. |
| TXT | This is used to provide information about the domain in text format. Commonly used for verification purposes. |
| SRV | This is used to specify the location of the service. The record contains priority, weight, port, target, and other information. |

### [DNS propagation](#dns-propagation)

When you're configuring or making changes to your DNS settings, you should be aware that it doesn't happen instantaneously. There's a whole network of servers, each of which has their own cache, and each of these will need to be updated to any new values that you set. For this reason, it can be normal to take up to 24-48 hours to see changes fully propagate through the network.

As we described earlier, when you set a record, you normally set a TTL value, or Time to Live, on a DNS record. This value, set in seconds, is the length of time a DNS cache will store information about your site, before it requests a new copy of the record from the authoritative server.

When you set the TTL value in your DNS record, you need to find the balance between serving your users the site quickly, and ensuring they're not seeing outdated information. A short TTL (minimum 30s) is beneficial if you are constantly updating the content, but will cause slower load times for your site. Using a longer TTL (max 86400 seconds, or 24 hours) means that records are cached for longer, so the site can load quickly for your users. Vercel defaults to 60s for a DNS record.

### [DNS best practices](#dns-best-practices)

When you are transferring an existing (in-use) domain to Vercel, it's a good practice to check the existing DNS record and its TTL before switching. Ideally, about 24 hours in advance of changes, you should shorten the DNS TTL to 60s. Once it's propagated, you can then change the DNS record to Vercel so that traffic quickly moves over to the new site because now the DNS TTL is much shorter.

You can use tools such as [https://www.whatsmydns.net](https://www.whatsmydns.net) to determine if your DNS settings have been fully propagated.

## [Troubleshooting](#troubleshooting)

To learn more about common DNS issues, see the [troubleshooting](/docs/domains/troubleshooting#common-dns-issues) doc.

## [Related](#related)

[

#### Domains overview

Learn the concepts behind how domains work

](/docs/domains)

[

#### Working with Domains

Learn how domains work and the options Vercel provides for managing them.

](/docs/domains/working-with-domains)

[

#### Working with Nameservers

Learn about nameservers and the benefits Vercel nameservers provide.

](/docs/domains/working-with-nameservers)

[

#### Working with SSL

Learn how Vercel uses SSL certificates to keep your site secure.

](/docs/domains/working-with-ssl)

[

#### Troubleshooting Domains

Learn about common reasons for domain misconfigurations and how to troubleshoot your domain on Vercel.

](/docs/domains/troubleshooting)

--------------------------------------------------------------------------------
title: "Working with domains"
description: "Learn how domains work and the options Vercel provides for managing them."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains"
--------------------------------------------------------------------------------

# Working with domains

Copy page

Ask AI about this page

Last updated September 24, 2025

You can [buy a domain through Vercel](#buying-a-domain-through-vercel) by going to the [Vercel.com domains page](https://vercel.com/domains) and using our fast search to [find one or more domains](/docs/getting-started-with-vercel/buy-domain) that fit your brand and needs. The price of available domains is the same as the registrar's pricing and Vercel does not keep a log of your search history for marketing purposes.

## [Buying a domain name](#buying-a-domain-name)

When you create a deployment on Vercel, we automatically assign it a domain based on your project name and ending in `.vercel.app`. Your site will be available to anyone that you share the domain with. Deployment URLs with the domain `.vercel.app` are allocated on a first-come, first-served basis and cannot be reserved.

More often than not, you will want to assign a domain to a project that reflects its nature better. You can buy a domain name either [through Vercel](#buying-a-domain-through-vercel) or [through a third-party](#buying-a-domain-through-a-third-party). Depending on which option you choose, will dictate how and when you'll need to make configurations:

### [Buying a domain through Vercel](#buying-a-domain-through-vercel)

When you buy a domain through Vercel, we configure and set the nameservers, which means you do not need to set any DNS records or make any configurations. It just works. In addition, if you choose to make configurations, such as setting up email, it's all maintained from the [Domains tab of your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page). Finally, all renewals, including domain and SSL certificate renewals are automatically handled by Vercel.

### [Buying a domain through a third-party](#buying-a-domain-through-a-third-party)

When you buy a custom domain through a third-party, you can use the [add a custom domain](/docs/domains/add-a-domain) workflow to configure the DNS records. If you are using Vercel's nameservers, you can manage certain settings, such as records for email providers or additional DNS records through the [Domains tab of your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page). Otherwise, you must configure nameservers and DNS records through your domain registrar.

## [Domain ownership and Project assignment](#domain-ownership-and-project-assignment)

When you are using domains with Vercel, there are two areas of the dashboard that you may need to go to in order to configure them correctly. The first relates to your ownership and the second relates to configuring the domain for your Project:

*   Domain ownership: Domains are owned by a specific team and can be accessed from the [Domains tab on your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page). All your domains, regardless of where they are registered, are _listed_ here and are owned by the owner of the team. If you are using Vercel's nameservers, which is the case by default if you buy your domain through Vercel, you can manage DNS records, custom nameservers, and SSL certificates here. Domains that are registered by a third-party should manage DNS records and nameservers with the third-party.
    
*   Project assignment: This is accessed by selecting the project that you wish to assign the domain to and navigating to Settings > Domains. From here you can add an apex domain or subdomain to the Project. When a user visits your domain, they will see the most recent production deployment of your site, unless you [assign the domain to a Git branch](/docs/domains/working-with-domains/assign-domain-to-a-git-branch) or [add redirection](/docs/domains/deploying-and-redirecting).
    

When you add a domain to Vercel for the first time, it will appear as an **apex domain** in your team's **Domains** tab. If you add that domain (for example, `yourdomain.com`, or `docs.yourdomain.com`) to a project on a different Vercel team, that domain will require a TXT Verification step and will only show up at the project level. The **apex domain** will still appear in the original account's **Domains** tab.

## [Subdomains, wildcard domains, and apex domains](#subdomains-wildcard-domains-and-apex-domains)

### [Apex Domain](#apex-domain)

The apex domain is the root-level domain, such as `acme.com`. When you add an apex domain, Vercel will recommend that you add a [redirect](/docs/domains/deploying-and-redirecting#redirecting-www-domains) to a `www` subdomain. This is because `www` records allow for better control over your domain. Anything configured on the apex domain (for example, cookies or CAA records), will usually apply to all subdomains, rather than setting it on the `www` subdomain, which will only apply to your `www` record. In addition, because Vercel's servers use anycast networking, it can handle CNAME records differently, allowing for quicker DNS resolution and therefore a faster website experience for the end user.

### [Subdomain](#subdomain)

A subdomain is a more specific part of that domain that can be assigned to a particular part of your site, for example, `blog.acme.com`, `help.acme.com`. This helps to blend both your brand, with the specificity of where the user may need to go. To add a subdomain to your Project, follow the instructions in the [Add a custom domain](/docs/domains/add-a-domain#subdomains) doc. If you have bought the domain through Vercel, you can also [point a subdomain to an external service](/guides/pointing-subdomains-to-external-services) through the Domains section of the dashboard. Subdomains are set through a _CNAME_ DNS record.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Furl-structure.png&w=750&q=75)

Image showing the fully-qualified domain name (FQDN).

### [Wildcard domain](#wildcard-domain)

You can also configure wildcard domains. Using a wildcard domain, such as `*.acme.com`, is a way to scale and customize your project on Vercel. Rather than specifying a particular subdomain, you can add a wildcard domain to your project, and then you need to set the nameservers to the intended nameservers, allowing the domain to be resolved. See our [multi-tenant SaaS template](https://vercel.com/templates/next.js/platforms-starter-kit) for an example of using wildcard domains on Vercel.

To add a wildcard domain, follow the steps in [Adding a domain](/docs/domains/add-a-domain#using-wildcard-domain).

Wildcard domains must be configured with the [nameservers method](/docs/domains/add-a-domain#vercel-nameservers). This is because in order to generate the wildcard certificates, Vercel needs to be able to set DNS records, since the service that Vercel uses to generate those requires us to solve a challenge to verify ownership.

## [Using email with domains](#using-email-with-domains)

When you create a domain, you may want to also set up a way for users to contact you through an email address that is pointed at that domain. Vercel does not provide a mail service for domains purchased with or transferred into it.

Because many domain providers do not offer a mail service, several third-party services specifically offer this type of functionality and are enabled by adding MX records. Examples of this type of service include [ImproxMX](https://improvmx.com/) and [Forward Email](https://forwardemail.net/en), however there are many more options available. For each provider, different DNS records are required to be added. For information on how to set up email, see [How do I send and receive emails with my Vercel purchased domain?](https://vercel.com/guides/using-email-with-your-vercel-domain)

## [Troubleshooting](#troubleshooting)

[Invalid domain configurations](/docs/domains/troubleshooting#misconfigured-domain-issues) are one of the most common types of domain issues on Vercel. To learn more about other common domain issues, see the [troubleshooting](/docs/domains/troubleshooting#common-domain-issues) doc.

## [More resources](#more-resources)

*   [Domains overview: Learn the concepts behind how domains work](/docs/domains)
*   [Learn how DNS works in order to properly configure your domain](/docs/domains/working-with-dns)
*   [Learn about nameservers and the benefits Vercel nameservers provide](/docs/domains/working-with-nameservers)
*   [Learn how Vercel uses SSL certificates to keep your site secure](/docs/domains/working-with-ssl)
*   [Learn how to troubleshoot your domain on Vercel](/docs/domains/troubleshooting)
*   [What is a Domain Name?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_domain_name)

--------------------------------------------------------------------------------
title: "Adding & Configuring a Custom Domain"
description: "Learn how to add a custom domain to your Vercel project, verify it, and correctly set the DNS or Nameserver values."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/add-a-domain"
--------------------------------------------------------------------------------

# Adding & Configuring a Custom Domain

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel provides all deployments with a `vercel.app` URL, which enables you to share Deployments with your Team for collaboration. However, to provide greater personalization and flexibility to your project, you can instead add a custom domain. If you don't own a domain yet, you can [purchase it with Vercel](/domains).

You can manage all domain settings related to a project in the Domains section of the Settings tab of the project, regardless of whether you are using [apex domains](#apex-domains) or [subdomains](#subdomains) in your project. This document will guide you through both options.

Hobby teams have a limit of 50 custom domains per project.

## [Add and configure domain](#add-and-configure-domain)

The following steps provide an overview of how to add and configure a custom domain in Vercel:

1.  ### [Navigate to Domain Settings](#navigate-to-domain-settings)
    
    On the [dashboard](/dashboard), pick the project to which you would like to assign your domain.
    
    Once you have selected your project, click on the Settings tab and then select the Domains menu item:
    
    ![Selecting the Domains menu item from the Project Settings page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fselect-domains-light.png&w=828&q=75)![Selecting the Domains menu item from the Project Settings page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fselect-domains-dark.png&w=828&q=75)
    
    Selecting the Domains menu item from the Project Settings page.
    
2.  ### [Add your domain](#add-your-domain)
    
    From the Domains page, click the Add Domain button:
    
    ![The button to click on the domains page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fadd-domain-button-light.png&w=1920&q=75)![The button to click on the domains page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fadd-domain-button-dark.png&w=1920&q=75)
    
    The button to click on the domains page.
    
    Input the domain you wish to include in the project:
    
    ![Text input on the add domain page to input your domain name in.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fenter-domain-input-light.png&w=1920&q=75)![Text input on the add domain page to input your domain name in.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fenter-domain-input-dark.png&w=1920&q=75)
    
    Text input on the add domain page to input your domain name in.
    
    If you add an apex domain (e.g. `example.com`) to the project, Vercel will prompt you to add the `www` subdomain prefix. For more information about why we recommend using a `www` domain, see "[Redirecting `www` domains](/docs/domains/deploying-and-redirecting#redirecting-www-domains)".
    
3.  ### [Using wildcard domain](#using-wildcard-domain)
    
    You can also use your custom domain as a wildcard domain by prefixing it with `*.`.
    
    If using your custom domain as a wildcard domain, you must use the nameservers method for verification.
    
    To add a wildcard domain, use the prefix `*`, for example `*.acme.com`.
    
    ![A wildcard domain being deployed.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fwildcard-domain.png&w=1920&q=75)![A wildcard domain being deployed.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fwildcard-domain-dark.png&w=1920&q=75)
    
    A wildcard domain being deployed.
    
4.  ### [Configure the domain](#configure-the-domain)
    
    Once you have added your custom domain, you will need to configure the DNS records of your domain with your registrar so it can be used with your Project. The dashboard will automatically display different methods for configuring it:
    
    *   If the domain is in use by another Vercel account, you will need to [verify access to the domain](#verify-domain-access), with a TXT record
    *   If you're using an [Apex domain](#apex-domains) (e.g. example.com), you will need to configure it with an A record
    *   If you're using a [Subdomain](#subdomains) (e.g. docs.example.com), you will need to configure it with a CNAME record
    
    Both apex domains and subdomains can also be configured using the [Nameservers](#vercel-nameservers) method.
    
    If you are verifying your domain by changing nameservers, you will need to add any DNS records to Vercel that you wish to keep from your previous DNS provider.
    
    #### [Apex domains](#apex-domains)
    
    You can configure apex domains with an A record.
    
    ![DNS configuration for an apex domain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fnew-domain-apex-light.png&w=1920&q=75)![DNS configuration for an apex domain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fnew-domain-apex-dark.png&w=1920&q=75)
    
    DNS configuration for an apex domain.
    
    #### [Subdomains](#subdomains)
    
    You can configure subdomains with a CNAME record. Each project has a unique CNAME record e.g. `d1d4fc829fe7bc7c.vercel-dns-017.com`.
    
    ![DNS configuration for a subdomain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fnew-domain-app-light.png&w=1920&q=75)![DNS configuration for a subdomain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fnew-domain-app-dark.png&w=1920&q=75)
    
    DNS configuration for a subdomain.
    
    #### [Vercel Nameservers](#vercel-nameservers)
    
    If you choose to use a wildcard domain Vercel's nameservers will be automatically enabled for you on saving the domain settings. You will then be provided with the Vercel nameservers to copy and use with your registrar.
    
    ![DNS configuration for Vercel nameservers.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fconfigure-dns-ns-light.png&w=1920&q=75)![DNS configuration for Vercel nameservers.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fconfigure-dns-ns-dark.png&w=1920&q=75)
    
    DNS configuration for Vercel nameservers.
    
5.  ### [Verify domain access](#verify-domain-access)
    
    If the domain is in use by another Vercel account, you may be prompted to verify access to the domain. Note that this will not move the domain into your account, but will allow you to use it in your project. If you have multiple domains to verify, be aware that you can only set up one TXT record at a time, but you can modify it after the domain is transferred.
    
    ![Verify domain access.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fverify-domain-light.png&w=1920&q=75)![Verify domain access.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fverify-domain-dark.png&w=1920&q=75)
    
    Verify domain access.
    

Once the domain has been configured and Vercel has verified it, the status of the domain will be updated within the UI to confirm that it is ready for use.

![Properly configured domain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fdomain-properly-configured-light.png&w=1200&q=75)![Properly configured domain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fdomain-properly-configured-dark.png&w=1200&q=75)

Properly configured domain.

If a someone visits your domain with or without the "www" subdomain prefix, Vercel will attempt to redirect them to your domain. For more robust protection, you should explicitly add this domain and [redirect it](/docs/domains/deploying-and-redirecting#redirecting-domains).

--------------------------------------------------------------------------------
title: "Assigning a custom domain to an environment"
description: "Learn how to add a custom domain to your Vercel project, verify it, and correctly set the DNS or Nameserver values."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/add-a-domain-to-environment"
--------------------------------------------------------------------------------

# Assigning a custom domain to an environment

Copy page

Ask AI about this page

Last updated March 12, 2025

1.  From the [dashboard](/dashboard), pick the project to which you would like to assign your domain and select the Settings tab.
2.  Click on the Environments menu item.
3.  Select the environment to which you would like to assign your domain. Users on Pro and Enterprise plans can create [custom environments](/docs/deployments/environments#custom-environments) to which they can assign custom domains.
4.  Once you've added your domain, you will need to configure the DNS records of your domain with your registrar so it can be used with your environment:
    *   If the domain is in use by another Vercel account, you will need to [verify access to the domain](/docs/domains/add-a-domain#verify-domain-access), with a TXT record.

*   If you're using an [Apex domain](/docs/domains/add-a-domain#apex-domains) (e.g. example.com), you will need to configure it with an A record.
*   If you're using a [Subdomain](/docs/domains/add-a-domain#subdomains) (e.g. docs.example.com), you will need to configure it with a CNAME record.

--------------------------------------------------------------------------------
title: "Assigning a domain to a Git branch"
description: "Learn how to assign a domain to a different Git branch with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch"
--------------------------------------------------------------------------------

# Assigning a domain to a Git branch

Copy page

Ask AI about this page

Last updated September 24, 2025

Every commit pushed to the [Production Branch](/docs/git#production-branch) of your [connected Git repository](/docs/git) will be assigned the domains configured in your project.

To automatically assign a domain to a different branch:

1.  From the [dashboard](/dashboard), pick the project to which you would like to assign your domain and select the Settings tab.
2.  Click on the Domains menu item.
3.  Select the Edit dropdown item for the domain to which you would like to assign your branch.
4.  Select Preview from the Connect to an environment section
5.  In the Git Branch field, enter the branch name to which you would like to assign the domain:

![Assign domain to branch modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fassign-domain-to-git-branch-light.png&w=1200&q=75)![Assign domain to branch modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fassign-domain-to-git-branch-dark.png&w=1200&q=75)

Assign domain to branch modal.

Pro and Enterprise teams can also set branch tracking for their [custom environments](/docs/deployments/environments#custom-environments).

If you prefer to do this using the Vercel REST API instead, you can use the ["Update a project domain"](/docs/rest-api/reference/endpoints/projects/update-a-project-domain) PATCH endpoint.

--------------------------------------------------------------------------------
title: "Deploying & Redirecting Domains"
description: "Learn how to deploy your domains and set up domain redirects with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/deploying-and-redirecting"
--------------------------------------------------------------------------------

# Deploying & Redirecting Domains

Copy page

Ask AI about this page

Last updated October 3, 2025

## [Deploying your Domain](#deploying-your-domain)

Once the domain has been added to your project and configured, it is automatically applied to your latest production deployment.

The first deployment of a new project will be marked as production and subsequently assigned with your custom domain automatically.

When you assign a custom domain to a project that's using [Git](/docs/git), each push (including merges) that you make to the [production branch](/docs/git#production-branch) (commonly `main`) will trigger a deployment to the domain.

When you assign a domain to a _different_ branch, you'll need to make a new deployment to the desired branch for the domain to resolve correctly.

Reverts take effect immediately, assigning the Custom Domain to the deployment made prior to the point the revert is effective from.

## [Redirecting domains](#redirecting-domains)

You can add domain redirects from the Domains tab when more than one domain is present in the project. This provides a way to, for example, redirect a `www` subdomain to an apex domain, but can be used in a variety of ways.

If a user visits your domain with or without the "www" subdomain prefix, we will attempt to redirect automatically. You might still want to add this redirect explicitly.

To add a redirect, navigate to the Domains tab within Project Settings, then select Edit on the domain you want to redirect from. Use the Redirect to dropdown to select the domain you want to redirect to:

![Edit domain modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fredirect-domain-light.png&w=1200&q=75)![Edit domain modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fredirect-domain-dark.png&w=1200&q=75)

Edit domain modal.

A domain redirect that redirects requests made to `www.acme.com` to `acme.com`.

## [Redirecting `www` domains](#redirecting-www-domains)

Adding an [apex domain](/docs/domains/working-with-domains#apex-domain) to a [Project](/docs/projects/overview) on Vercel will automatically suggest adding its `www` counterpart. Using both of these domains ensures that visitors can always access your site, regardless of whether or not they use `www` when entering the URL.

We recommend using the `www` subdomain as your primary domain, with a redirect from the non-`www` domain to it. This allows the [Vercel CDN](/docs/cdn) more control over incoming traffic for improved reliability, speed, and security. The redirect is also cached on visitor's browsers for faster subsequent visits.

Some browsers like Google Chrome automatically hide the `www` subdomain from the address bar, so this redirect may not affect your URL appearance.

Choosing to redirect the `www` domain to the non-`www` also works but provides Vercel less control over incoming traffic. Alternatively, you can choose to add only the domain you typed.

## [Additional technical information about Domain redirects](#additional-technical-information-about-domain-redirects)

The DNS spec forbids using CNAME records on apex domains like `example.com`. They are, however, allowed for subdomains like `www.example.com`. This is why Vercel recommends primarily using a `www` domain with a CNAME record, and adding a redirect from the non-`www` domain to it.

Using CNAME instead of A records ensures that domains on Vercel are fast, reliable, and fault-tolerant. Unlike A records, CNAME records avoid hard-coding a specific IP address in favor of an additional lookup at the DNS level. This means that Vercel can quickly steer traffic in the case of DDoS attacks or for performance optimizations.

While we recommend using `www` as described above, Vercel maximizes the reliability and performance of your apex domain if you choose to use it as your primary domain by leveraging the [Anycast methodology](https://en.wikipedia.org/wiki/Anycast). This means Vercel still supports geographically routed traffic at infinite scale if you use an A record.

## [Programmatic redirects](#programmatic-redirects)

You can also add redirects programmatically using frameworks and Vercel Functions. [Learn more](/docs/redirects).

--------------------------------------------------------------------------------
title: "Removing a Domain from a Project"
description: "Learn how to remove a domain from a Project and from your account completely with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/remove-a-domain"
--------------------------------------------------------------------------------

# Removing a Domain from a Project

Copy page

Ask AI about this page

Last updated September 24, 2025

When you add a domain to any project, it will be connected to your account until you choose to delete it. This guide demonstrates how to remove a domain from a Project and from your account completely.

1.  ### [Navigate to the Domains tab](#navigate-to-the-domains-tab)
    
    To remove a domain that is assigned to a project, navigate to the Domains tab from the Project Overview and click the More Options button for the domain you want to remove.
    
2.  ### [Click remove button](#click-remove-button)
    
    Once the • • • menu button has been clicked, you will be presented with further options. Click the Delete menu button to remove the domain from the project.
    
3.  ### [Remove domain from your account](#remove-domain-from-your-account)
    
    Optionally, if you wish to remove a domain from all Projects, as well as your Account, navigate to the Domains section of your dashboard. In the list of all the domains under your account, find the domain you wish to remove. Then, from the context menu, click the Delete menu item.
    
    ![Option to delete domain(s) from the Domains tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fremove-domains.png&w=1920&q=75)![Option to delete domain(s) from the Domains tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Fremove-domains-dark.png&w=1920&q=75)
    
    Option to delete domain(s) from the Domains tab.
    
    If the domain was purchased through Vercel, you must first wait for the domain to expire before you can remove it from your account.
    

## [Using cURL](#using-curl)

To remove a domain from a project using cURL, you can use the following command. To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

cURL

```
curl --request DELETE \
  --url https://api.vercel.com/v9/projects/<project-id-or-name>/domains/<domain-name> \
  --header "Authorization: Bearer $VERCEL_TOKEN"
```

--------------------------------------------------------------------------------
title: "Managing Domain Renewals and Redemptions"
description: "Learn how to manage automatic and manual renewals for custom domains purchased through or registered with Vercel, and how to redeem expired domains with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/renew-a-domain"
--------------------------------------------------------------------------------

# Managing Domain Renewals and Redemptions

Copy page

Ask AI about this page

Last updated September 24, 2025

Custom domains purchased through or registered with Vercel are [automatically renewed](#auto-renewal) by default with the option to [manually renew](#manual-renewal) them.

You can see the expiration or [renewal date](#filter-on-renewal-status) of your Vercel-managed domains in the list of domains on the [Domains tab of your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page).

## [Auto renewal](#auto-renewal)

To enable automatic renewal, follow these steps:

1.  ### [Select the Domains tab](#select-the-domains-tab)
    
    You can choose to prevent the automatic renewal of a Domain from the [Domains tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+Domains) on the Vercel Dashboard.
    
2.  ### [View the auto renewal status](#view-the-auto-renewal-status)
    
    From the list of domains, find the domain you want to enable automatic renewal for. You can use the search bar or filter button to find it if you have many domains. You'll see the auto-renewal or expiry status of the domain in the domain's row.
    
    ![Domain row with auto renewal status.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fdomains-list-item-light.png&w=2048&q=75)![Domain row with auto renewal status.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fdomains-list-item-dark.png&w=2048&q=75)
    
    Domain row with auto renewal status.
    
3.  ### [Toggle the auto renewal status](#toggle-the-auto-renewal-status)
    
    Click on the hamburger menu icon to the right of the domain and toggle the Auto Renewal to on or off.
    

### [Auto renewal off](#auto-renewal-off)

If auto renewal is off, Vercel will not try to re-register the Domain when it expires at the end of the registration period. You will not be charged for the Domain any longer, but you will lose access to the Domain when it expires. Recovering the Domain, if even possible, may be subject to a redemption fee. Please [contact our support team](/help#issues) as soon as possible.

Vercel will send you three emails regarding the Domain before this happens. 24 and 14 days before the Domain is set to expire, you will be notified that auto renewal is off and the Domain will expire soon. A final email will notify you when the Domain expires.

### [Auto renewal on](#auto-renewal-on)

If auto renewal is on, Vercel will use the following process to renew the domain:

1.  60 days before expiration, Vercel will send you a warning email that the domain will expire and that we will try to renew it
2.  30 days before expiration, Vercel will try to renew the domain
3.  Starting at 29 days before expiration, Vercel will check for any failed renewals and try to renew them again

## [Manual renewal](#manual-renewal)

1.  ### [Select the Domains Tab](#select-the-domains-tab)
    
    Navigate to the [Domains tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+Domains) on the Vercel Dashboard.
    
2.  ### [Find your domain from the list](#find-your-domain-from-the-list)
    
    From the list of domains, find the domain you want to renew. You can use the search bar or filter button to find it if you have many domains. You'll see the auto renewal or expiry status of the domain in the domain's row.
    
3.  ### [Click the Renew button](#click-the-renew-button)
    
    Click on the hamburger menu icon to the right of the domain and click the Renew button.
    
    Your domain must be within 1 year of expiration to be eligible for renewal.
    
4.  ### [Confirm your renewal](#confirm-your-renewal)
    
    ![The Renew Domain Modal](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Frenew-domain-modal-light.png&w=1080&q=75)![The Renew Domain Modal](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Frenew-domain-modal-dark.png&w=1080&q=75)
    
    The Renew Domain Modal
    

## [Domain redemptions](#domain-redemptions)

For expired domains with a redemption period (typically 30 days), you can now recover them directly in the dashboard:

![The Redeem Domain Modal](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fredeem-domain-modal-light.png&w=1080&q=75)![The Redeem Domain Modal](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fredeem-domain-modal-dark.png&w=1080&q=75)

The Redeem Domain Modal

A redemption fee will be applied, depending on the domain registry.

Not all top-level domains (TLDs) support redemptions.

## [Filter on renewal status](#filter-on-renewal-status)

You can filter your Vercel owned domains by their renewal status by clicking the filter icon in the top right of the Domains table:

![Filter Domains table by renewal status.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Frenew-domain-light.png&w=1080&q=75)![Filter Domains table by renewal status.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Frenew-domain-dark.png&w=1080&q=75)

Filter Domains table by renewal status.

## [Renewing third-party domains](#renewing-third-party-domains)

Third-Party Domains (ones not purchased with or transferred into Vercel) are not subject to auto-renewal. Please refer to your Domain name registrar's policy regarding renewals.

--------------------------------------------------------------------------------
title: "Transferring Domains to Another Team or Project"
description: "Domains can be transferred to another team or project within Vercel, or to and from a third-party registrar. Learn how to transfer domains with this guide."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/transfer-your-domain"
--------------------------------------------------------------------------------

# Transferring Domains to Another Team or Project

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Transfer a domain to another Vercel user or Team](#transfer-a-domain-to-another-vercel-user-or-team)

1.  ### [Select the Domains tab](#select-the-domains-tab)
    
    You can move domains to another team using the [Domains tab of your team's dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page).
    
2.  ### [Select the domain](#select-the-domain)
    
    Once on the Domains tab, select the context menu next to the domain you wish to move, and click Move. You can also use checkbox next to each domain to select more than one domain
    
    ![Selecting which domains to move from the Domains tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdomains%2Fmove-light.png&w=1920&q=75)![Selecting which domains to move from the Domains tab.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdomains%2Fmove-dark.png&w=1920&q=75)
    
    Selecting which domains to move from the Domains tab.
    
3.  ### [Select the team](#select-the-team)
    
    After selecting the domain(s) and clicking Move, you will be asked to confirm which profile or team you wish to move them to.
    
    ![Entering a new profile or team destination for a domain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdomains%2Fmove-modal.png&w=1080&q=75)![Entering a new profile or team destination for a domain.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdomains%2Fmove-modal-dark.png&w=1080&q=75)
    
    Entering a new profile or team destination for a domain.
    
    When selecting the input field, you will be provided with a list of teams you belong to. If the profile or team you wish to move the domain(s) to is not present, enter the `slug` value instead. You can find the `slug` value in Settings page for both profiles and teams.
    
    When moving domains to another team or user, all existing project domains associated with them will remain and not be moved to prevent service disruption. However, any [custom aliases](/docs/cli/alias) that are not part of project domains will be removed immediately.
    
4.  ### [Confirm the change](#confirm-the-change)
    
    To confirm the change, select Move. The domains will be transferred to the new profile of team immediately.
    

## [Transferring domains between projects](#transferring-domains-between-projects)

You can use the Dashboard to remove a domain from a project and then re-add it to another. However, this could potentially end up with some site down-time. For more information on transferring domains with zero downtime, see [How to move a domain between Vercel projects with "Zero Downtime"?](/guides/how-to-move-a-domain-between-vercel-projects-with-zero-downtime)

## [Transferring domains out of Vercel](#transferring-domains-out-of-vercel)

1.  ### [Verifying Transfer Eligibility](#verifying-transfer-eligibility)
    
    Due to [ICANN rules](https://www.icann.org/resources/pages/text-2012-02-25-en#:~:text=Please%20note%20that%20you%20may,60%20days%20after%20a%20transfer), a domain must be registered with a registrar for 60 days before it can be transferred to another.
    
    You can verify that your domain has been registered with Vercel for at least 60 days by visiting the team's [Domains Dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fdomains&title=Go+to+team%27s+domains+page). If the registrar is Vercel and the age greater than 60 days, it is eligible to transfer.
    
2.  ### [Select the **Domains** tab](#select-the-domains-tab)
    
    For domains that are registered with Vercel, you can retrieve an authorization code for transferring out to another registrar from the **Domains** tab of the Dashboard.
    
3.  ### [Select the "Transfer out" option](#select-the-transfer-out-option)
    
    Once on the **Domains** tab, click on the triple-dot menu button for the relevant domain. A menu-item button to transfer the domain out will be presented if the domain is registered with Vercel.
    
    ![Menu item button for getting domain's transfer authorization code.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdomains%2Ftransfer-light.png&w=1920&q=75)![Menu item button for getting domain's transfer authorization code.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fdomains%2Ftransfer-dark.png&w=1920&q=75)
    
    Menu item button for getting domain's transfer authorization code.
    
    If under a Team scope, only [Team Owners](/docs/rbac/access-roles#owner-role) will see the menu-item button.
    
4.  ### [Use the authorization code with the new registrar](#use-the-authorization-code-with-the-new-registrar)
    
    After clicking the menu-item button, a modal will open up with the authorization code required to transfer the domain. Use this authorization code with your new registrar to confirm that you want to transfer the domain. There is no additional confirmation that you need to do on the Vercel side. Transferring a domain can take up to a week.
    
    If you encounter problems with the transfer code, ensure you've entered it correctly without typos or extra spaces. If the code seems correct but still doesn't work, please contact [Vercel support](/help) for further assistance.
    
    ![Modal for domain's transfer authorization code.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Ftransfer-out-modal.png&w=1080&q=75)![Modal for domain's transfer authorization code.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fcustom-domains%2Ftransfer-out-modal-dark.png&w=1080&q=75)
    
    Modal for domain's transfer authorization code.
    

## [Transfer a domain to Vercel](#transfer-a-domain-to-vercel)

By transferring your domain into Vercel, you allow Vercel to manage the DNS records for the domain and can use it with any Projects listed under the account the domain is owned by.

1.  ### [Verifying Transfer Eligibility](#verifying-transfer-eligibility)
    
    Due to [ICANN rules](https://www.icann.org/resources/pages/text-2012-02-25-en#:~:text=Please%20note%20that%20you%20may,60%20days%20after%20a%20transfer), a domain must be registered with a registrar for 60 days before it can be transferred to another. You will need to confirm this with your registrar before attempting the transfer to Vercel.
    
    If the domain has not been registered with the current registrar for at least 60 days, the domain transfer will fail.
    
    NOTE: To find further information on ICANN rules, visit the [ICANN website](https://www.icann.org/resources/pages/text-2012-02-25-en#:~:text=Please%20note%20that%20you%20may,60%20days%20after%20a%20transfer).
    
2.  ### [Unlock the Domain](#unlock-the-domain)
    
    Once you have verified your domain's eligibility to transfer, proceed with unlocking your domain in your registrar's domain settings. Most domains are usually locked by default to prevent unauthorized changes.
    
    The domain lock feature appears in different forms across registrars. Sign into the host where your domain is registered and look for a Domain Lock or similar option to unlock your domain. If this option is not available, contact your registrar to change this.
    
3.  ### [Obtain Authorization Code](#obtain-authorization-code)
    
    After unlocking the domain, you will need to obtain an authorization code. The code will be sent to the email address associated with your domain by your registrar. In some cases, your authorization code pops up on your dashboard. This may be available in the domain registrars dashboard. If it is not available, contact your registrar to obtain this.
    
4.  ### [Transferring to Vercel](#transferring-to-vercel)
    
    When transferring a domain, you will have two options to choose from. Either using the Vercel Dashboard or Vercel CLI.
    
    Option 1: Using Vercel Dashboard
    
    After obtaining the authorization code, click on the Transfer in button in the Vercel Domains Dashboard and enter in your domain and respective authorization code.
    
    Option 2: Using Vercel CLI
    
    With Vercel CLI, you can run the following command from your terminal.
    
    ```
    vercel domains transfer-in [your-domain]
    ```
    
    You will be requested to provide an authorization code from your registrar after running this command. Once you get the authorization code from your registrar, paste it into the prompt and the transfer will begin.
    
    In a case where your domain cannot be transferred, check that it has been over 60 days since the domain has been registered or previously transferred. If it still does not work, contact your registrar.
    
5.  ### [Configure domain](#configure-domain)
    
    Follow these steps to ensure that there is no downtime while the domain is transferred to Vercel.
    
    Pre-generate SSL certificates
    
    If you are migrating a deployment to Vercel, require zero downtime, and aren't using Vercel's nameservers, you can pre-generate and issue SSL certificates to your domain. If you have enabled Vercel DNS by pointing your domain's nameserver to Vercel and have generated an SSL certificate, you can ignore this step.
    
    Follow the [detailed guide](/docs/domains/pre-generating-ssl-certs) to set up SSL certificates before finalizing the domain transfer.
    
    Set DNS records in your registrar
    
    Once you have pre-generated the SSL certificates, you need to add the new TXT records to your DNS records in your domain registrar dashboard. Learn how to do that [here](/docs/domains/managing-dns-records#migrating-dns-records-from-an-external-registrar).
    
6.  ### [Deploy the domain](#deploy-the-domain)
    
    You can deploy your app with Vercel once the domain has been successfully added to your account.
    
    By setting a production domain from your projects' Domains dashboard, you will be able to use the following command with Vercel CLI:
    
    ```
    vercel --prod
    ```
    
    This command will deploy your project and make it accessible at the production domain that you have setup.

--------------------------------------------------------------------------------
title: "Viewing & Searching Domains"
description: "Learn how to view and search all registered domains that are assigned to Vercel Projects through the Vercel dashboard."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-domains/view-and-search-domains"
--------------------------------------------------------------------------------

# Viewing & Searching Domains

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Viewing domains](#viewing-domains)

To view all your registered domains, go to the Domains tab in your Vercel dashboard.

The domains list will show you all domains that are currently active on your account, and display the following information:

*   Domain - The domain name
*   Registrar and status - The domain registrar (Vercel or Third Party). If the registrar is Vercel, you will see the renewal or expiry status of the domain
*   Creator - The person who created the domain, indicated by their avatar and username and include the creation date

## [Searching domains](#searching-domains)

You can search for a specific domain by using the search bar above the domains list.

It is not possible to search a multi-level wildcard subdomain. It is only possible to search a subdomain at one level down.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fdomains-settings-search-light.png&w=2048&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdomains%2Fdomains-settings-search-dark.png&w=2048&q=75)

--------------------------------------------------------------------------------
title: "Working with nameservers"
description: "Learn about nameservers and the benefits Vercel nameservers provide."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-nameservers"
--------------------------------------------------------------------------------

# Working with nameservers

Copy page

Ask AI about this page

Last updated September 24, 2025

Before moving your domain to use Vercel's nameservers, you should ensure that you own the domain listed on the [Domains](/domains) page of your account."

Nameservers are the actual servers on the network that are responsible for resolving domain names to the IP addresses where your site is hosted. Most domain registrars, including Vercel, [provide their own nameservers](/docs/domains/managing-nameservers). For Vercel these are:

*   `ns1.vercel-dns.com`
*   `ns2.vercel-dns.com`

When you purchase your domain through Vercel, we can set all the DNS records, including nameserver records, that tell anyone looking for your site where it can be found.

### [Benefits of using Vercel nameservers](#benefits-of-using-vercel-nameservers)

*   Automatic DNS Records: Domains with nameservers pointed to Vercel don't need explicit DNS records created for the apex domain or first-level subdomains since they will be created automatically. This means that you can add a domain or subdomain to a project without thinking about DNS records at all. Not only does this reduce the potential for mistakes, but if you have multiple subdomains that you would like to use for your project, it takes away the need for manual entry of CNAME records for each of them.
*   Wildcard Domains: When using Vercel's nameservers you can add [wildcard domains](/docs/domains/working-with-domains#subdomains-wildcard-domains-and-apex-domains) without any further configuration.
*   Custom nameservers: For domains registered with Vercel, you can add custom nameservers to your Vercel-hosted domain directly from the dashboard, allowing for delegation to other DNS providers. Add up to four nameservers at once, and revert to your previous settings if necessary.

For domains that are not registered with Vercel, you can change the nameservers directly from the domain registrar's dashboard. For more information, see [Add Vercel's nameservers](/docs/domains/managing-nameservers#add-vercel's-nameservers).

Before using Vercel's nameservers, you should ensure that you own the domain.

## [Troubleshooting](#troubleshooting)

To learn more about common nameserver issues, see the [troubleshooting](/docs/domains/troubleshooting#common-nameserver-issues) doc.

## [Related](#related)

[

#### Domains overview

Learn the concepts behind how domains work

](/docs/domains)

[

#### Working with Domains

Learn how domains work and the options Vercel provides for managing them.

](/docs/domains/working-with-domains)

[

#### Working with DNS

Learn how DNS works in order to properly configure your domain.

](/docs/domains/working-with-dns)

[

#### Working with SSL

Learn how Vercel uses SSL certificates to keep your site secure.

](/docs/domains/working-with-ssl)

[

#### Troubleshooting Domains

Learn about common reasons for domain misconfigurations and how to troubleshoot your domain on Vercel.

](/docs/domains/troubleshooting)

--------------------------------------------------------------------------------
title: "Working with SSL Certificates"
description: "Learn how Vercel uses SSL certification to keep your site secure."
last_updated: "null"
source: "https://vercel.com/docs/domains/working-with-ssl"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./05-no-cors-headers.md) | [Index](./index.md) | [Next →](./07-working-with-ssl-certificates.md)
