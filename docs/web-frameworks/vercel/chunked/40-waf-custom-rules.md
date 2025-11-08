**Navigation:** [← Previous](./39-session-tracing.md) | [Index](./index.md) | Next →

---

# WAF Custom Rules

Copy page

Ask AI about this page

Last updated September 24, 2025

You can [configure](#custom-rule-configuration) specific rules to log, deny, challenge, bypass, or [rate limit](/docs/security/vercel-waf/rate-limiting) traffic to your site. When you apply the configuration, it takes effect immediately and does not require re-deployment.

[Get started](#get-started) by reviewing the [Best practices for applying rules](#best-practices-for-applying-rules) section.

WAF Custom Rules are available on [all plans](/docs/plans)

Those with the [member](/docs/rbac/access-roles#member-role), [viewer](/docs/rbac/access-roles#viewer-role), [developer](/docs/rbac/access-roles#developer-role) and [administrator](/docs/rbac/access-roles#project-administrators) roles can access this feature

## [Access roles](#access-roles)

*   You need to be a [Developer](/docs/rbac/access-roles#developer-role) or viewer ([Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) or [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role)) in the team to view the Firewall overview page and list the rules
*   You need to be a [Project administrator](/docs/rbac/access-roles#project-administrators) or [Team member](/docs/rbac/access-roles#member-role) to configure, save and apply any rule and configuration

## [Custom Rule configuration](#custom-rule-configuration)

You can create multiple Custom Rules for the same project. Each rule can perform the following actions according to one or more logical condition(s) that you set based on the value of specific [parameters](/docs/security/vercel-waf/rule-configuration) in the incoming request:

*   [log](/docs/vercel-firewall/firewall-concepts#log)
*   [deny](/docs/vercel-firewall/firewall-concepts#deny)
*   [challenge](/docs/vercel-firewall/firewall-concepts#challenge)
*   [bypass](/docs/vercel-firewall/firewall-concepts#bypass)
*   redirect

You can save, delete, or disable a rule at any time and these actions have immediate effect. You also have the ability to re-order the precedence of each custom rule.

## [Custom Rule execution](#custom-rule-execution)

When a rule denies or challenges the traffic to your site and the client has not previously solved the challenge (in the case of challenge mode), the rule execution stops and blocks or challenges the request.

After a Log rule runs, the rule execution continues. If no other rule matches and acts on the request, the Log rule that is last matched is reported.

When you apply a [rate limiting](/docs/security/vercel-waf/rate-limiting) rule, you need to include a follow up action that will log, deny, challenge, or return a 429 response.

## [Persistent actions](#persistent-actions)

Persistent Actions are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

When a custom rule blocks a client's request, future requests that do not match the rule's condition from the same client, are allowed through. If you want to deny all requests from the client whose first request was blocked, you will need to identify who this client is through [traffic monitoring](/docs/security/vercel-waf#traffic-monitoring) and create an IP Address rule for that purpose.

With persistent actions, you can automatically block potential bad actors by adding a time-based block to the Challenge or Deny action of your custom rule. When you do so, any client whose request is challenged or denied, will be blocked for a period of time that you specify.

Notes about this time-based block:

*   It is applied to the IP address of the client that originally triggered the rule to match.
*   It happens before the firewall processes the request, so that none of the requests blocked by persistent actions count towards your [CDN](/docs/cdn) and traffic usage.

### [Enable persistent actions](#enable-persistent-actions)

You can enable persistent actions for any challenge, deny or rate limit action when you create or edit a custom rule. From your project's page in the dashboard:

1.  Select the Firewall tab followed by Configure on the top right of the Firewall overview page.
2.  Select a Custom Rule you would like to edit from the list or select \+ New Rule and follow the [steps](#get-started) for configuring a rule.

When you select challenge, deny or rate limit for the [action](/docs/vercel-firewall/vercel-waf/rule-configuration#actions) dropdown (Then) of any condition, you will see an additional dropdown for timeframe (for) that defaults to 1 minute. You have the following options:

1.  Select a time value from the available options
2.  Remove the timeframe (If you don't want to enable persistent actions)

Once you're happy with the changes:

1.  Select Save Rule to apply it
2.  Apply the changes with the Review Changes button

## [Best practices for applying rules](#best-practices-for-applying-rules)

To ensure your Custom Rule behaves as intended:

1.  Test a Custom Rule by setting it up with a log action
2.  Observe the 10-minute live traffic to check the behavior
3.  Update the Custom Rule condition if needed. Once you're happy with the behavior, update the rule with a challenge, deny, or bypass, or rate limit action

## [Get started](#get-started)

Learn how to create, test, and apply a Custom Rule.

1.  From your dashboard, select the project that you'd like to configure a rule for and then select the Firewall tab
2.  Select Configure on the top right of the Firewall overview page
3.  Select \+ New Rule
4.  Type a name to help you identify the purpose of this rule for future reference
5.  In the Configure section, add as many If conditions as needed. For each condition you add, choose how you will combine it with the previous condition using the AND (Both conditions need to be met) or the OR operator (One of the conditions need to be met).
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-and-or-light.png&w=2048&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-and-or-dark.png&w=2048&q=75)
    
6.  Select Log for the Then action
    *   For Rate Limit, review [WAF Rate Limiting](/docs/security/vercel-waf/rate-limiting#get-started)
7.  Select Save Rule to apply it
8.  Apply the changes:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment
9.  Go to the Firewall overview page, select your Custom Rule from the traffic grouping drop-down and select the paramater(s) related to the condition(s) of your Custom Rule to observe the traffic:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-dark.png&w=3840&q=75)
    
10.  If you are satisfied with the traffic behavior, select Configure
11.  Select the Custom Rule that you created
12.  Update the Then action to Challenge, Deny or Bypass as needed
13.  Select Save Rule to apply it
14.  Apply the changes with the Review Changes button

Review [Common Examples](/docs/security/vercel-waf/examples) for the application of specific rules in common situations.

## [Configuration in vercel.json](#configuration-in-vercel.json)

You can configure custom WAF rules directly in your `vercel.json` file using the `routes` property. This allows you to define firewall rules as part of your deployment configuration.

### [Supported actions](#supported-actions)

When configuring WAF rules in `vercel.json`, you can use the following actions:

*   challenge: Challenge the request with a security check
*   deny: Block the request entirely

This is a subset of the actions available in the dashboard - `log`, `bypass`, and `redirect` actions are not supported in `vercel.json` configuration.

### [Example configuration](#example-configuration)

The following example shows how to deny requests that contain a specific header:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "routes": [
    {
      "src": "/(.*)",
      "has": [
        {
          "type": "header",
          "key": "x-react-router-prerender-data"
        }
      ],
      "mitigate": {
        "action": "deny"
      }
    }
  ]
}
```

In this example:

*   The route matches all paths (`/(.*)`)
*   The `has` condition checks for the presence of a specific header
*   The `mitigate` property specifies the action to take (deny the request)

### [Route configuration](#route-configuration)

For complete documentation on route configuration options, including `has`, `missing`, and other conditional matching properties, see the [routes documentation](/docs/project-configuration#routes).

--------------------------------------------------------------------------------
title: "WAF Examples"
description: "Learn how to use Vercel WAF to protect your site in specific situations."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/examples"
--------------------------------------------------------------------------------

# WAF Examples

Copy page

Ask AI about this page

Last updated May 13, 2025

| Example | Category | Template |
| --- | --- | --- |
| [Suspicious traffic in specific countries](/guides/suspicious-traffic-in-specific-countries) | [Custom Rule](/docs/security/vercel-waf/custom-rules) | [Add Custom Rule](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Fconfigure%2Frule%2Fnew%3Ftemplate%3D%257B%2522name%2522%253A%2522Log%2BIreland%2BTraffic%2522%252C%2522active%2522%253Atrue%252C%2522description%2522%253A%2522Understand%2BIreland%2Btraffic%2Bspike%2522%252C%2522action%2522%253A%257B%2522mitigate%2522%253A%257B%2522redirect%2522%253Anull%252C%2522action%2522%253A%2522log%2522%252C%2522rateLimit%2522%253Anull%252C%2522actionDuration%2522%253Anull%257D%257D%252C%2522id%2522%253A%2522%2522%252C%2522conditionGroup%2522%253A%255B%257B%2522conditions%2522%253A%255B%257B%2522op%2522%253A%2522eq%2522%252C%2522type%2522%253A%2522geo_country%2522%252C%2522value%2522%253A%2522IE%2522%257D%255D%257D%255D%257D%26sig%3D12b37a6616c355602ccb7cd892057fe73f618207&title=Add+Firewall+Rule+from+Template) |
| [Emergency redirect](/guides/emergency-redirect) | [Custom Rule](/docs/security/vercel-waf/custom-rules) | [Add Custom Rule](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Fconfigure%2Frule%2Fnew%3Ftemplate%3D%257B%2522name%2522%253A%2522Emergency%2Bredirect%2522%252C%2522active%2522%253Atrue%252C%2522description%2522%253A%2522%2522%252C%2522action%2522%253A%257B%2522mitigate%2522%253A%257B%2522redirect%2522%253A%257B%2522location%2522%253A%2522%252Fold-conf-login%2522%252C%2522permanent%2522%253Afalse%257D%252C%2522action%2522%253A%2522redirect%2522%252C%2522rateLimit%2522%253Anull%252C%2522actionDuration%2522%253Anull%257D%257D%252C%2522id%2522%253A%2522%2522%252C%2522conditionGroup%2522%253A%255B%257B%2522conditions%2522%253A%255B%257B%2522op%2522%253A%2522eq%2522%252C%2522type%2522%253A%2522path%2522%252C%2522value%2522%253A%2522%252Fconference-login%2522%257D%255D%257D%255D%257D%26sig%3D27dcd2df3ed1c4c770bbe22a900d08bf9097342f&title=Add+Firewall+Rule+from+Template) |
| [Limit abuse with rate limiting](/guides/limit-abuse-with-rate-limiting) | [Custom Rule](/docs/security/vercel-waf/custom-rules) | [Add Custom Rule](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Fconfigure%2Frule%2Fnew%3Ftemplate%3D%257B%2522name%2522%253A%2522Auth%2BAbuse%2BPrevention%2522%252C%2522active%2522%253Atrue%252C%2522description%2522%253A%2522Limits%2Brequests%2Bto%2Bregistration%2Band%2Blogin%2Bendpoints%2Bto%2Bprevent%2Babuse%2Band%2Bbrute%2Bforce%2Battacks%2522%252C%2522action%2522%253A%257B%2522mitigate%2522%253A%257B%2522redirect%2522%253Anull%252C%2522action%2522%253A%2522rate_limit%2522%252C%2522rateLimit%2522%253A%257B%2522algo%2522%253A%2522fixed_window%2522%252C%2522window%2522%253A60%252C%2522limit%2522%253A10%252C%2522keys%2522%253A%255B%2522IP%2BAddress%2522%255D%252C%2522action%2522%253A%2522deny%2522%257D%252C%2522actionDuration%2522%253Anull%257D%257D%252C%2522id%2522%253A%2522%2522%252C%2522conditionGroup%2522%253A%255B%257B%2522conditions%2522%253A%255B%257B%2522op%2522%253A%2522re%2522%252C%2522type%2522%253A%2522path%2522%252C%2522value%2522%253A%2522%255E%252Fapi%252Fauth%252F%2528%253F%253Aregister%257Csignup%257Clogin%257Csignin%2529%2524%2522%257D%255D%257D%255D%257D%26sig%3D6086757b4a1248dc1ffed2b8b1a0ab936726c167&title=Add+Firewall+Rule+from+Template) |
| [Block AI bots](/docs/vercel-waf/managed-rulesets#configure-ai-bots-managed-ruleset) | [Managed Ruleset](/docs/vercel-waf/managed-rulesets) |  |
| [Block `.php` requests](/guides/block-php-requests) | [Custom Rule](/docs/security/vercel-waf/custom-rules) | [Add Custom Rule](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Fconfigure%2Frule%2Fnew%3Ftemplate%3D%257B%2522name%2522%253A%2522Block%2B.php%2Brequest%2Bpaths%2522%252C%2522active%2522%253Atrue%252C%2522description%2522%253A%2522Adds%2Ba%2Brule%2Bthat%2Bblocks%2Bany%2Brequests%2Bcontaining%2B%2527.php%2527.%2522%252C%2522action%2522%253A%257B%2522mitigate%2522%253A%257B%2522redirect%2522%253Anull%252C%2522action%2522%253A%2522deny%2522%252C%2522rateLimit%2522%253Anull%252C%2522actionDuration%2522%253Anull%257D%257D%252C%2522id%2522%253A%2522%2522%252C%2522conditionGroup%2522%253A%255B%257B%2522conditions%2522%253A%255B%257B%2522type%2522%253A%2522path%2522%252C%2522op%2522%253A%2522sub%2522%252C%2522value%2522%253A%2522.php%2522%257D%255D%257D%255D%257D%26sig%3D7afc375dc668c1b24db94335b95b3a08a2883ad5&title=Add+Firewall+Rule+from+Template) |
| [Block traffic from a specific IP address](/guides/traffic-spikes) | [IP Blocking](/docs/security/vercel-waf/ip-blocking) |  |
| [Challenge `cURL` requests](/guides/challenge-curl-requests) | [Firewall REST API](/docs/rest-api/reference/endpoints/security) |  |
| [Challenge cookieless requests on a specific path](/guides/challenge-cookieless-requests-on-a-specific-path) | [Firewall REST API](/docs/rest-api/reference/endpoints/security) |  |
| [Deny non-browser traffic or blocklisted ASNs](/guides/deny-non-browser-traffic-or-blocklisted-asns) | [Firewall REST API](/docs/rest-api/reference/endpoints/security) |  |
| [Deny traffic from a set of IP addresses](/guides/deny-traffic-from-a-set-of-ip-addresses) | [Firewall REST API](/docs/rest-api/reference/endpoints/security) |  |

--------------------------------------------------------------------------------
title: "WAF IP Blocking"
description: "Learn how to customize the Vercel WAF to restrict access to certain IP addresses."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/ip-blocking"
--------------------------------------------------------------------------------

# WAF IP Blocking

Copy page

Ask AI about this page

Last updated September 24, 2025

You can create custom rules to block a specific IP address or multiple IP addresses by CIDR, effectively preventing unauthorized access or unwanted traffic. This security measure allows you to restrict access to your applications or websites based on the IP addresses of incoming requests.

Common use cases for IP blocking on Vercel include:

*   Blocking known malicious IP addresses
*   Preventing competitors or scrapers from accessing your content

In cases such as blocking based on complying with specific laws and regulations or to restrict access to or from a particular geographic area, we recommend using [Custom Rules](/docs/security/vercel-waf/custom-rules).

## [Access roles](#access-roles)

*   You need to be a [Developer](/docs/rbac/access-roles#developer-role) or viewer ([Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) or [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role)) in the team to view the Firewall overview page and list the rules
*   You need to be a [Project administrator](/docs/rbac/access-roles#project-administrators) or [Team member](/docs/rbac/access-roles#member-role) to configure, save and apply any rule and configuration

## [Project level IP Blocking](#project-level-ip-blocking)

Project level IP Blocking is available on [all plans](/docs/plans)

Those with the [member](/docs/rbac/access-roles#member-role), [viewer](/docs/rbac/access-roles#viewer-role), [developer](/docs/rbac/access-roles#developer-role) and [administrator](/docs/rbac/access-roles#project-administrators) roles can access this feature

To block an IP address, navigate to the Firewall tab of your project and follow these steps:

1.  Select Configure on the top right of the Firewall overview page
2.  Scroll down to the IP Blocking section
3.  Select the \+ Add IP button
4.  Complete the required IP Address Or CIDR and Host fields in the Configure New Domain Protection modal
    *   The host is the domain name of the site you want to block the IP address from accessing. It should match the domain(s) associated with your project
    *   You can copy this value from the URL of the site you want to block without the `https` prefix
    *   It must match the exact domain you want to block, for example `my-site.com`, `www.my-site.com` or `docs.my-site.com`
    *   You should add an entry for all subdomains that you wish block, such as `blog.my-site.com` and `docs.my-site.com`
5.  Select the Create IP Block Rule button
6.  Apply the changes:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment

## [Account-level IP Blocking](#account-level-ip-blocking)

Account-level IP Blocking is available on [Enterprise plans](/docs/plans/enterprise)

Those with the [owner](/docs/rbac/access-roles#owner-role) and [member](/docs/rbac/access-roles#member-role) roles can access this feature

### [How to add an IP block rule](#how-to-add-an-ip-block-rule)

To block an IP address, you can create an IP Blocking rule in your dashboard:

1.  On your Team's [dashboard](/dashboard), navigate to Settings and select the Security tab
2.  On the IP Blocking section, select Create New Rule to create a new rule set
3.  Add the IP address you want to block and the host you want to block it from. The host is the domain name of the site you want to block the IP address from accessing
    *   You can copy this value from the URL of the site you want to block without the `https` prefix
    *   It must match the exact domain you want to block, for example `my-site.com`, `www.my-site.com` or `docs.my-site.com`
    *   You should add a separate entry for each subdomain that you wish to block, such as `blog.my-site.com` and `docs.my-site.com`
4.  Select the Create IP Block Rule button

## [More resources](#more-resources)

*   [Geolocation region block](/guides/suspicious-traffic-in-specific-countries)

--------------------------------------------------------------------------------
title: "WAF Managed Rulesets"
description: "Learn how to use managed rulesets with the Vercel Web Application Firewall (WAF)"
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets"
--------------------------------------------------------------------------------

# WAF Managed Rulesets

Copy page

Ask AI about this page

Last updated September 24, 2025

Managed rulesets are collections of predefined WAF rules based on standards such as [Open Worldwide Application Security Project (OWASP) Top Ten](https://owasp.org/www-project-top-ten/) that you can enable and configure in your project's Firewall dashboard.

The following ruleset(s) are currently available:

*   [OWASP core ruleset](#configure-owasp-core-ruleset)
*   [Bot protection managed ruleset](#configure-bot-protection-managed-ruleset)
*   [AI Bots managed ruleset](#configure-ai-bots-managed-ruleset)

## [Access roles](#access-roles)

*   You need to be a [Developer](/docs/rbac/access-roles#developer-role) or viewer ([Viewer Pro](/docs/rbac/access-roles#viewer-pro-role) or [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role)) in the team to view the Firewall overview page and list the rules
*   You need to be a [Project administrator](/docs/rbac/access-roles#project-administrators) or [Team member](/docs/rbac/access-roles#member-role) to configure, save and apply any rule and configuration

## [Configure OWASP core ruleset](#configure-owasp-core-ruleset)

OWASP core ruleset is available on [Enterprise plans](/docs/plans/enterprise) . [Review pricing information here](/docs/security/vercel-waf/usage-and-pricing#managed-ruleset-pricing).

To enable and configure [OWASP Core Ruleset](https://owasp.org/www-project-top-ten/) for your project, follow these steps:

1.  From your [project's dashboard](/docs/projects/project-dashboard), select the Firewall tab
2.  Select the Configure button
3.  From the Managed Rulesets section, enable OWASP Core Ruleset
4.  You can apply the changes with the OWASP rules enabled by default:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment
5.  Or select what OWASP rules to enable first by selecting Configure from the OWASP Core Ruleset list item
6.  For the OWASP Core Ruleset configuration page, enable or disable the rule that you would like to apply
7.  For each enabled rule, select Log or Deny from the action drop-down
    *   Use Log first and monitor the live traffic on the Firewall overview page to check that the rule has the desired effect when applied
8.  Apply the changes
9.  Monitor the live traffic on the Firewall overview page

## [Configure bot protection managed ruleset](#configure-bot-protection-managed-ruleset)

Bot protection managed ruleset is available on [all plans](/docs/plans)

To enable and configure [bot protection](/docs/bot-management#bot-protection-managed-ruleset) for your project, follow these steps:

1.  From your [project's dashboard](/docs/projects/project-dashboard), select the [Firewall](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall&title=Firewall+tab) tab.
2.  Select the Configure button.
3.  From the Bot Management section, select Log or Challenge on the Bot Protection rule to choose what action should be performed when an unwanted bot is identified.
    *   When enabled in challenge mode, the Vercel WAF will serve a JavaScript challenge to traffic that is unlikely to be a browser.
4.  You can then apply as follows:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment

## [Configure AI Bots managed ruleset](#configure-ai-bots-managed-ruleset)

AI bots managed ruleset is available on [all plans](/docs/plans)

To manage AI bots for your project, follow these steps:

1.  From your [project's dashboard](/docs/projects/project-dashboard), select the [Firewall](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall&title=Firewall+tab) tab.
2.  Select the Configure button.
3.  From the Bot Management section, select Log or Deny on the AI Bots rule to choose what action should be performed when an AI bot is identified.
    *   Log: This action records AI bot traffic without blocking it. Its useful for monitoring.
    *   Deny: This action blocks all traffic identified as coming from AI bots.
4.  You can then apply as follows:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment

## [Bypassing rulesets](#bypassing-rulesets)

Sometimes, you may need to allow specific requests that a managed ruleset is blocking. For example, [Bot Protection](/docs/bot-management#bot-protection-managed-ruleset) could be blocking a custom user agent that you are using. In this case, use the [bypass](/docs/vercel-firewall/firewall-concepts#bypass) [action](/docs/vercel-firewall/vercel-waf/rule-configuration#actions) in a [WAF Custom Rule](/docs/vercel-firewall/vercel-waf/custom-rules) to target the traffic you want to allow. In the case of the custom user agent, you would use the "User Agent" parameter with a value of the user agent name in the custom rule.

### [Bypassing custom rules](#bypassing-custom-rules)

If you need to allow requests being blocked by your own custom rule set up in your project, you can add another custom rule with a bypass action targeting the blocked requests. Make sure that the bypass rule executes before the blocking custom rule by placing it higher in the custom rules section of the [Firewall rules page](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Ffirewall%2Fconfigure&title=Go+to+the+Firewall+Rules) of your project dashboard.

### [Rules execution order](#rules-execution-order)

The Vercel WAF executes rules on incoming traffic in the following order:

1.  Custom rules set up in the project
2.  Managed rulesets configured in the project

--------------------------------------------------------------------------------
title: "WAF Rate Limiting"
description: "Learn how to configure custom rate limiting rules with the Vercel Web Application Firewall (WAF)."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting"
--------------------------------------------------------------------------------

# WAF Rate Limiting

Copy page

Ask AI about this page

Last updated September 24, 2025

WAF Rate Limiting is available on [all plans](/docs/plans)

Rate limiting allows you to control the number of times that a request from the same source can hit your application within a specific timeframe. This could happen due to multiple reasons, such as malicious activity or a software bug.

The use of rate limiting rules helps ensure that only intended traffic reaches your resources such as API endpoints or external services, giving you better control over usage costs.

## [Get started](#get-started)

1.  From your [dashboard](https://vercel.com/dashboard/), select the project that you'd like to configure rate limiting for. Then select the Firewall tab
2.  Select Configure on the top right of the Firewall overview page. Then, select \+ New Rule
3.  Complete the fields for the rule as follows
    1.  Type a name to help you identify the purpose of this rule for future reference
    2.  In the Configure section, add as many If conditions as needed:
        
        All conditions must be true for the action to happen.
        
        ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-custom-rule-configure-dark.png&w=1920&q=75)
        
    3.  For the Then action, select Rate Limit
        *   If this is the first time you are creating a rate limit rule, you will need to review the Rate Limiting Pricing dialog and select Continue
    4.  Select Fixed Window (all plans) or Token Bucket (Enterprise) for the limiting strategy
        
        ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-rate-limit-light.png&w=2048&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fvercel-waf-rate-limit-dark.png&w=2048&q=75)
        
    5.  Update the Time Window field as needed (defaults to 60s) and the Request Limit field as needed (defaults to 100 requests)
        *   The Request Limit defines the maximum number of requests allowed in the selected time window from a common source
    6.  Select the key(s) from the request's source that you want to match against
    7.  For the Then action, you can leave the Default (429) action or choose between Log, Deny and Challenge
        
        The Log action will not perform any blocks. You can use it to first monitor the effect before applying a rate limit or block action.
        
4.  Select Save Rule
5.  Apply the changes:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment
6.  Go to the Firewall overview page, select your Custom Rule from the traffic grouping drop-down and select the paramater(s) related to the condition(s) of your Custom Rule to observe the traffic and check whether it's working as expected:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fsecurity%2Fwaf-overview-custom-rule-dark.png&w=3840&q=75)
    

## [Limits](#limits)

| Resource | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| Included counting keys | IP, JA4 Digest | IP, JA4 Digest | IP, JA4 Digest, User Agent and arbitrary Header keys |
| Counting algorithm | Fixed window | Fixed window | Fixed window, Token bucket |
| Counting window | Minimum: 10s, Maximum: 10mins | Minimum: 10s, Maximum: 10mins | Minimum: 10s, Maximum: 1hr |
| Number of rules | 1 per project | 40 per project | 1000 per project |
| Included requests | 1,000,000 Allowed requests | 1,000,000 Allowed requests |  |

## [Pricing](#pricing)

The pricing is based on the region(s) from which the requests come from.

Select a Region

Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dubai, UAE (dxb1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, UK (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)

Managed Infrastructure pricing
| 
Resource

 | 

Measurement Metric

 | 

Price

 |
| --- | --- | --- |
| 

WAF Rate Limiting

 | 1,000,000 Allowed Requests | $0.50 |

--------------------------------------------------------------------------------
title: "Rate Limiting SDK"
description: "Learn how to configure a custom rule with rate limit in your code."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting-sdk"
--------------------------------------------------------------------------------

# Rate Limiting SDK

Copy page

Ask AI about this page

Last updated September 24, 2025

You can configure a custom rule with rate limit in your code by using the [`@vercel/firewall`](https://github.com/vercel/vercel/tree/main/packages/firewall/docs) package. This can be useful in the following cases:

*   You need to set a rate limit on requests in your backend
*   You want to use additional conditions with the rate limit that are not possible in the custom rule configuration of the dashboard

## [Using `@vercel/firewall`](#using-@vercel/firewall)

1.  ### [Create a `@vercel/firewall` rule](#create-a-@vercel/firewall-rule)
    
    1.  From your [dashboard](https://vercel.com/dashboard/), select the project that you'd like to configure rate limiting for. Then select the Firewall tab
    2.  Select Configure on the top right of the Firewall overview page. Then, select \+ New Rule
    3.  Complete the fields for the rule as follows
        1.  Type a name such as "Firewall api rule"
        2.  In the Configure section, for the first If condition, select `@vercel/firewall`
        3.  Use `update-object` as the Rate limit ID
        4.  Use the default values for Rate Limit and Then
    4.  Select Save Rule
    5.  Apply the changes:
        *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
        *   Select Review Changes and review the changes to be applied
        *   Select Publish to apply the changes to your production deployment
2.  ### [Configure rate limiting in code](#configure-rate-limiting-in-code)
    
    You can now use the Rate limit ID `update-object` set up above with `@vercel/firewall` to rate limit any request based on your own conditions. In the example below, you rate limit a request based on its IP.
    
    rate-limit.ts
    
    ```
    import { checkRateLimit } from '@vercel/firewall';
     
    export async function POST(request: Request) {
      const { rateLimited } = await checkRateLimit('update-object', { request });
      if (rateLimited) {
        return new Response(
          JSON.stringify({
            error: 'Rate limit exceeded',
          }),
          {
            status: 429,
            headers: {
              'Content-Type': 'application/json',
            },
          },
        );
      }
      // Otherwise, continue with other tasks
    }
    ```
    
3.  ### [Test in a preview deployment](#test-in-a-preview-deployment)
    
    For your code to run when deployed in a preview deployment, you need to:
    
    *   Enable [Protection Bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) in your project
    *   Ensure [System Environment Variables are automatically exposed](/docs/environment-variables/system-environment-variables#system-environment-variables)

## [Target a user's organization](#target-a-user's-organization)

For example, you can include an additional filter for a request header and check whether this header matches a key from the user's authentication, to apply the rate limit. This filter is not possible in the custom rule dashboard.

### [Update the custom rule filters](#update-the-custom-rule-filters)

Edit the custom rule in the dashboard and add an If condition with the following values, and click Save Rule:

*   Filter dropdown: #Request Header
*   Value: `xrr-internal-header`
*   Operator: Equals
*   Match value: `internal`

### [Use the `rateLimitKey` in code](#use-the-ratelimitkey-in-code)

Use the following code to apply the rate limit only to users of the organization.

rate-limit.ts

```
import { checkRateLimit } from '@vercel/firewall';
import { authenticateUser } from './auth';
 
export async function POST(request: Request) {
  const auth = await authenticateUser(request);
  const { rateLimited } = await checkRateLimit('update-object', {
    request,
    rateLimitKey: auth.orgId,
  });
  if (rateLimited) {
    return new Response(
      JSON.stringify({
        error: 'Rate limit exceeded',
      }),
      {
        status: 429,
        headers: {
          'Content-Type': 'application/json',
        },
      },
    );
  }
}
```

--------------------------------------------------------------------------------
title: "Rule Configuration Reference"
description: "List of configurable options with the Vercel WAF"
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/rule-configuration"
--------------------------------------------------------------------------------

# Rule Configuration Reference

Copy page

Ask AI about this page

Last updated April 21, 2025

For each custom rule that you create, you can configure one or more conditions with [parameters](#parameters) from the incoming traffic that you compare with specific values using [operators](#operators). For each new condition, you can choose how you combine it with the previous condition using the AND (Both conditions need to be met) or the OR operator (One of the conditions need to be met).

You also specify an [action](#actions) executed when all the conditions are met.

## [Parameters](#parameters)

Custom Rule Parameters
| 
Parameter

 | 

Description

 | 

Example

 | 

Note

 |
| --- | --- | --- | --- |
| 

Request Path

 | 

The full request path on the incoming request, always starting with a leading `/`

 | `/api`, `/signup/new` | 

 |
| 

Route

 | 

The framework determined `x-matched-path`

 | `/blog/[slug]` | 

When matching on the route, the custom rule will run after middleware. If the rule blocks a request, middleware charges could be incurred

 |
| 

Server Action Name

 | 

The Next.js server action name as defined by your codebase

 | `app/auth/actions.ts#getUser` | 

Requires Next.js 15.5. When matching on the server action name, the custom rule will run after middleware. If the rule blocks a request, middleware charges could be incurred

 |
| 

Raw Path

 | 

The raw request path, ignoring any parsing or normalizing that might be done at the framework level

 | `/api/`, `/signup/new/` | 

 |
| 

Method

 | 

The HTTP method used to make the request

 | `GET`, `POST` | 

 |
| 

User Agent

 | 

The HTTP user agent used to make the request

 | `curl` | 

 |
| 

Request Header

 | 

The request header on the original request. Define both the header key and value you want to match

 |  | 

You cannot match headers set by middleware, as the rule runs before middleware is invoked

 |
| 

Query

 | 

Any incoming query parameter on the original request. Define both the query key and value you want to match

 |  | 

 |
| 

Cookie

 | 

Any incoming cookie on the original request. Define both the query key and value you want to match

 |  | 

 |
| 

Hostname

 | 

The hostname used for the incoming request

 |  | 

This applies to projects with multiple domains such as platforms that assign a domain to each user of the platform

 |
| 

IP Address

 | 

The original or forwarded IP address on the incoming request

 | `10.0.0.1`, `10.0.0.1/32` | 

 |
| 

Protocol

 | 

The HTTP protocol of the original request

 | `HTTP/1.1`, `HTTP/2.0` | 

 |
| 

Environment

 | 

The Vercel Environment that received this request

 |  | 

Preview or Production

 |
| 

Vercel Region

 | 

The Vercel region that received this request

 | [Regions list](/docs/regions#region-list) | 

 |
| 

Continent

 | 

The continent based on the client IP address

 |  | 

A shorthand for the `x-vercel-ip-continent` header

 |
| 

State

 | 

The state (Country Region) based on the client IP address

 |  | 

A shorthand for the `x-vercel-ip-country-region` header

 |
| 

Country

 | 

The country based on the client IP address

 |  | 

A shorthand for the `x-vercel-ip-country` header

 |
| 

City

 | 

The city based on the client IP address

 |  | 

A shorthand for the `x-vercel-ip-city` header

 |
| 

AS Number

 | 

The Autonomous System Number based on the client IP address

 | Digits only, e.g. `12345` | 

Digits only

 |
| 

JA3 Digest

 | 

The calculated TLS digest of the incoming request

 |  | 

 |
| 

JA4 Digest

 | 

The calculated TLS digest of the incoming request

 |  | 

 |
| 

@vercel/firewall

 | 

ID for a rate limit instrumented in code via the \`@vercel/firewall\` package

 |  | 

 |

## [Operators](#operators)

All operators are case insensitive.

Operators Rule Parameters
| 
Parameter

 | 

Value

 | 

Description

 |
| --- | --- | --- |
| 

Equals

 | 

`eq`

 | 

*   An exact string match

 |
| 

Does not equal

 | 

`neq`

 | 

Inverse of **Equals**

 |
| 

Is any of

 | 

`inc`

 | 

*   An exact string match, matching any of the provided values
*   Acts like a `SQL IN` query

 |
| 

Is not any of

 | 

`ninc`

 | 

*   Ensures the source is not a match with any of the provided values
*   Acts like a `SQL NOT IN` query

 |
| 

Contains

 | 

`sub`

 | 

*   Includes the provided value

 |
| 

Does not contain

 | 

`sub`

 | 

Inverse of **Contains**. Set the `neg` parameter to `true`

 |
| 

Starts with

 | 

`pre`

 | 

*   A string operator matching the start of the string
*   Optimized for performance. It's preferred to use this over a regex prefix expression

 |
| 

Ends with

 | 

`suf`

 | 

*   A string operator matching the end of the string
*   Optimized for performance. It's preferred to use this over a regex suffix expression

 |
| 

Matches expression

 | 

`re`

 | 

*   A PCRE ([Perl Compatible Regular Expression](https://www.pcre.org/)) compliant regular expression
*   Useful for negative matches like “does not contain” or similar strict matching criteria

 |
| 

Does not match expression

 | 

`re`

 | 

Inverse of **Matches expression**. Set the `neg` parameter to `true`

 |

## [Actions](#actions)

| Name | Description | Note |
| --- | --- | --- |
| Log | Tracks the matching of this rule without blocking traffic. Requests matching this rule are visible in the Firewall overview page. | 
*   If another rule blocks the traffic **before** a log rule executes, the request is not considered a match for that log rule
*   If another rule blocks the traffic **after** a log rule executes, the request is tagged to the rule that blocked the traffic and does not appear in the log rule

 |
| Challenge | Conditionally blocks traffic with [browser challenge](/docs/vercel-firewall/firewall-concepts#challenge). | 

*   If the client fails to solve the challenge, the rule continues to block the traffic
*   Once the client solves the challenge, the rule is bypassed and remaining rules (if any) are evaluated. The request is allowed if none of the remaining rules block

 |
| Deny | Blocks the request and no further rules are evaluated. |  |
| Bypass | If matched, it bypasses any remaining custom rules. | WAF bypass rules **do not** bypass system-level mitigations such as [DDoS Mitigation](/docs/security/ddos-mitigation). To do so, you can use the [Bypass System-level Mitigations](/docs/security/ddos-mitigation#bypass-system-level-mitigations) feature. |
| Redirect | If matched, it redirects the client to the target path set in the `to` field. | 

*   Redirects the request and no further rules are evaluated
*   The target path in the `to` field can be absolute or relative to the project deployment's root
*   It's a temporary redirect (307)

 |

--------------------------------------------------------------------------------
title: "WAF System Bypass Rules"
description: "Learn how to configure IP-based system bypass rules with the Vercel Web Application Firewall (WAF)."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules"
--------------------------------------------------------------------------------

# WAF System Bypass Rules

Copy page

Ask AI about this page

Last updated September 24, 2025

WAF System Bypass Rules are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

While Vercel's system-level mitigations (such as [DDoS protection](/docs/security/ddos-mitigation)) safeguard your websites and applications, it can happen that they block traffic from legitimate sources like proxies or shared networks in situations where traffic from these sources was identified as malicious.

You can ensure that specific IP addresses or CIDR ranges are never blocked by the Vercel Firewall's system mitigations with System Bypass Rules.

If you need to allow requests blocked by your own [WAF Custom Rules](/docs/vercel-waf/custom-rules), use another [custom rule with a bypass action](/docs/vercel-firewall/vercel-waf/managed-rulesets#bypassing-custom-rules).

## [Get started](#get-started)

To add an IP address that should bypass system mitigations, navigate to the Firewall tab of your project and follow these steps:

1.  Select Configure on the top right of the Firewall overview page
2.  Scroll down to the System Bypass Rules section
3.  Select the \+ Add Rule button
4.  Complete the following fields in the Configure New System Bypass modal:
    *   IP Address Or CIDR (required)
    *   Domain (required): The domain connected to the project or use `*` to specify all domains connected to a project
    *   Note: For future reference
5.  Select the Create System Bypass button
6.  Apply the changes:
    *   When you make any change, you will see a Review Changes button appear or update on the top right with the number of changes requested
    *   Select Review Changes and review the changes to be applied
    *   Select Publish to apply the changes to your production deployment

## [Limits](#limits)

System Bypass Rules have limits based on your [account plan](/docs/plans).

| Resource | [Hobby](/docs/plans/hobby) | [Pro](/docs/plans/pro) | [Enterprise](/docs/plans/enterprise) |
| --- | --- | --- | --- |
| Number of system bypass rules per project | N/A | 25 | 100 |

--------------------------------------------------------------------------------
title: "Usage & Pricing for Vercel WAF"
description: "Learn how the Vercel WAF can affect your usage and how specific features are priced."
last_updated: "null"
source: "https://vercel.com/docs/vercel-firewall/vercel-waf/usage-and-pricing"
--------------------------------------------------------------------------------

# Usage & Pricing for Vercel WAF

Copy page

Ask AI about this page

Last updated September 9, 2025

Vercel Firewall features that are available under all plans, are free to use. This includes [DDoS mitigation](/docs/security/ddos-mitigation), [IP blocking](/docs/security/vercel-waf/ip-blocking), and [custom rules](/docs/security/vercel-waf/custom-rules). Vercel WAF plan-specific features such as [rate limiting](/docs/security/vercel-waf/rate-limiting) and [managed rulesets](/docs/security/vercel-waf/managed-rulesets) are priced as described in [priced features](#priced-features-usage).

## [Free features usage](#free-features-usage)

Although you are not charged for Firewall features available under all plans, you may incur [Edge Requests (ER)](/docs/manage-cdn-usage#edge-requests) and [incoming Fast Data Transfer (FDT)](/docs/manage-cdn-usage#fast-data-transfer) charges as described below.

| Feature | ER | FDT | Note |
| --- | --- | --- | --- |
| [WAF custom rule](/docs/security/vercel-waf/custom-rules) | Charged | Charged | When a custom rule is active, you incur usage for every challenged or denied request. |
| [WAF custom rule with persistent actions](/docs/security/vercel-waf/custom-rules#persistent-actions) | Not charged | Not charged | As the requests are now blocked before being processed by the firewall, they do not count towards usage. |
| [DDoS mitigation](/docs/security/ddos-mitigation) | Not charged | Not charged | Review [Do I get billed for DDoS?](/docs/security/ddos-mitigation#do-i-get-billed-for-ddos) for an explanation. |
| [Attack Challenge Mode](/docs/attack-challenge-mode) | Not charged | Not charged | When attack challenge mode is turned on, requests that do not pass the challenge will not count towards usage. |
| [Account level IP Blocking](/docs/security/vercel-waf/ip-blocking#account-level-ip-blocking) | Not charged | Not charged | Requests originating from these blocked IP addresses do not count towards usage. |
| [Project level IP Blocking](/docs/security/vercel-waf/ip-blocking#project-level-ip-blocking) | Charged | Charged | This falls under custom rules. |

## [Priced features usage](#priced-features-usage)

Enterprise only features are priced as described below.

### [Rate limiting pricing](#rate-limiting-pricing)

Select a Region

Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dubai, UAE (dxb1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, UK (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)

Managed Infrastructure pricing
| 
Resource

 | 

Measurement Metric

 | 

Price

 |
| --- | --- | --- |
| 

WAF Rate Limiting

 | 1,000,000 Allowed Requests | $0.50 |

### [Managed ruleset pricing](#managed-ruleset-pricing)

Select a Region

Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dubai, UAE (dxb1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, UK (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)

Managed Infrastructure pricing
| 
Resource

 | 

Measurement Metric

 | 

Price

 |
| --- | --- | --- |
| 

OWASP CRS per request number

 | 1,000,000 Inspected Requests | $0.80 |
| 

OWASP CRS per request size

 | 1 GB of inspected request payload | $0.20 |

--------------------------------------------------------------------------------
title: "Vercel Sandbox"
description: "Vercel Sandbox allows you to run arbitrary code in isolated, ephemeral Linux VMs."
last_updated: "null"
source: "https://vercel.com/docs/vercel-sandbox"
--------------------------------------------------------------------------------

# Vercel Sandbox

Copy page

Ask AI about this page

Last updated October 23, 2025

Vercel Sandbox is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

Vercel Sandbox is an ephemeral compute primitive designed to safely run untrusted or user-generated code on Vercel. It supports dynamic, real-time workloads for AI agents, code generation, and developer experimentation.

With Vercel Sandbox, you can:

*   Execute untrusted or third-party code: When you need to run code that has not been reviewed, such as AI agent output or user uploads, without exposing your production systems.
    
*   Build dynamic, interactive experiences: If you are creating tools that generate or modify code on the fly, such as AI-powered UI builders or developer sandboxes such as language playgrounds.
    
*   Test backend logic in isolation: Preview how user-submitted or agent-generated code behaves in a self-contained environment with access to logs, file edits, and live previews.
    
*   Run a development server to test your application.
    

## [Using Vercel Sandbox](#using-vercel-sandbox)

*   Get started with using Vercel Sandbox with the [getting started guide](#getting-started) and [examples](/docs/vercel-sandbox/examples)
*   Learn about [authentication methods](#authentication) and the [SDK reference](/docs/vercel-sandbox/reference/globals)
*   [Understand how to monitor your sandboxes](#observability)
*   Review [pricing](/docs/vercel-sandbox/pricing#pricing), [resource limits](/docs/vercel-sandbox/pricing#resource-limits) and [system specifications](/docs/vercel-sandbox#system-specifications)

## [Getting started](#getting-started)

### [Pre-requisites](#pre-requisites)

*   [The Vercel CLI](https://vercel.com/docs/cli)

### [Create a sandbox](#create-a-sandbox)

You can create sandboxes using our TypeScript SDK or Python SDK.

TypeScriptPython

In the steps below, you will create a sandbox with 4 vCPUs that uses `node22` runtime to run a Next.js application.

1.  ### [Set up your environment](#set-up-your-environment)
    
    Create a new directory `sandbox-test` and install the `@vercel/sandbox` and `ms` packages:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/sandbox ms
    ```
    
    Add the required type definitions for `ms` and `node`:
    
    terminal
    
    ```
    pnpm add -D @types/ms @types/node
    ```
    
2.  #### [Set up authentication](#set-up-authentication)
    
    From the `sandbox-test` directory you just created, link a new or existing project:
    
    terminal
    
    ```
    vercel link
    ```
    
    Then pull the project's environment variables:
    
    terminal
    
    ```
    vercel env pull
    ```
    
    This pulls a Vercel OIDC token into your `.env.local` file that the SDK will use to authenticate with.
    
3.  ### [Create the set up file](#create-the-set-up-file)
    
    In the code below, you will:
    
    *   Clone a Github repository of a Next.js application (Review [Using a private repository](/docs/vercel-sandbox/examples#using-a-private-repository) to clone a private repository)
    *   Install the dependencies for the application
    *   Run a `next dev` server and listen to port `3000`
    *   Open the sandbox URL (`sandbox.domain(3000)`) in a browser and stream logs to your terminal
    *   The sandbox will stop after the configurable 10 minute timeout.
    
    next-dev.ts
    
    ```
    import ms from 'ms';
    import { Sandbox } from '@vercel/sandbox';
    import { setTimeout } from 'timers/promises';
    import { spawn } from 'child_process';
     
    async function main() {
      const sandbox = await Sandbox.create({
        source: {
          url: 'https://github.com/vercel/sandbox-example-next.git',
          type: 'git',
        },
        resources: { vcpus: 4 },
        // Timeout in milliseconds: ms('10m') = 600000
        // Defaults to 5 minutes. The maximum is 5 hours for Pro/Enterprise, and 45 minutes for Hobby.
        timeout: ms('10m'),
        ports: [3000],
        runtime: 'node22',
      });
     
      console.log(`Installing dependencies...`);
      const install = await sandbox.runCommand({
        cmd: 'npm',
        args: ['install', '--loglevel', 'info'],
        stderr: process.stderr,
        stdout: process.stdout,
      });
     
      if (install.exitCode != 0) {
        console.log('installing packages failed');
        process.exit(1);
      }
     
      console.log(`Starting the development server...`);
      await sandbox.runCommand({
        cmd: 'npm',
        args: ['run', 'dev'],
        stderr: process.stderr,
        stdout: process.stdout,
        detached: true,
      });
     
      await setTimeout(500);
      spawn('open', [sandbox.domain(3000)]);
    }
     
    main().catch(console.error);
    ```
    
4.  ### [Start the sandbox](#start-the-sandbox)
    
    Run the following command in your terminal:
    
    terminal
    
    ```
    node --env-file .env.local --experimental-strip-types ./next-dev.ts
    ```
    
    Once the application opens in your browser, you can view the logs in the terminal as you interact with it.
    
5.  ### [Access the sandbox](#access-the-sandbox)
    
    The script opens the `next dev` server in your browser. The public URL is resolved using the `sandbox.domain(3000)` method.
    
    You'll see the development server logs streaming in real-time to your terminal as you interact with the application.
    
6.  ### [Stop the sandbox](#stop-the-sandbox)
    
    To stop a sandbox, you can:
    
    *   Navigate to the [Observability tab](#observability) of your project
    *   Find your sandbox in the list, and click Stop
    
    If you do not stop the sandbox, it will stop after the 10 minute timeout has elapsed.
    
    The SDK also provides the [`stop`](/docs/vercel-sandbox/reference/classes/sandbox#stop) method to programmatically stop a running sandbox.
    

## [Authentication](#authentication)

### [Vercel OIDC token](#vercel-oidc-token)

The SDK uses Vercel OIDC tokens to authenticate whenever available. This is the most straightforward and recommended way to authenticate.

When developing locally, you can download a development token to `.env.local` using `vercel env pull`. After 12 hours the development token expires, meaning you will have to call `vercel env pull` again.

In production, Vercel manages token expiration for you.

### [Using access tokens](#using-access-tokens)

If you want to use the SDK from an environment where `VERCEL_OIDC_TOKEN` is unavailable, you can also authenticate using an access token. You will need

*   your [Vercel team ID](https://vercel.com/docs/accounts#find-your-team-id)
*   your [Vercel project ID](https://vercel.com/docs/project-configuration/general-settings#project-id)
*   a [Vercel access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) with access to the above team

Set your team ID, project ID, and token to the environment variables `VERCEL_TEAM_ID`, `VERCEL_PROJECT_ID`, and `VERCEL_TOKEN`. Then pass these to the `create` method:

TypeScriptPython

```
const sandbox = await Sandbox.create({
  teamId: process.env.VERCEL_TEAM_ID!,
  projectId: process.env.VERCEL_PROJECT_ID!,
  token: process.env.VERCEL_TOKEN!,
  source: {
    url: 'https://github.com/vercel/sandbox-example-next.git',
    type: 'git',
  },
  resources: { vcpus: 4 },
  timeout: ms('5m'), // timeout in milliseconds: ms('5m') = 300000
  ports: [3000],
  runtime: 'node22',
});
```

## [System specifications](#system-specifications)

Sandbox includes a `node22` and `python3.13` image. In both of these images:

*   User code is executed as the `vercel-sandbox` user.
*   The default working directory is `/vercel/sandbox`.
*   `sudo` access is available.

|  | Runtime | Package managers |
| --- | --- | --- |
| `node22` | `/vercel/runtimes/node22` | `npm`, `pnpm` |
| `python3.13` | `/vercel/runtimes/python` | `pip`, `uv` |

### [Available packages](#available-packages)

The base system is Amazon Linux 2023 with the following additional packages:

`bind-utils bzip2 findutils git gzip iputils libicu libjpeg libpng ncurses-libs openssl openssl-libs procps tar unzip which whois zstd`

Users can install additional packages using the `dnf` package manager:

TypeScriptPython

install-packages.ts

```
import { Sandbox } from '@vercel/sandbox';
 
const sandbox = await Sandbox.create();
await sandbox.runCommand({
  cmd: 'dnf',
  args: ['install', '-y', 'golang'],
  sudo: true,
});
```

You can find the [list of available packages](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.7.html) on the Amazon Linux documentation.

### [Sudo config](#sudo-config)

The sandbox sudo configuration is designed to be easy to use:

*   `HOME` is set to `/root`. Commands executed with sudo will source root's configuration files (e.g. `.gitconfig`, `.bashrc`, etc).
*   `PATH` is left unchanged. Local or project-specific binaries will still be available when running with elevated privileges.
*   The executed command inherits all other environment variables that were set.

## [Observability](#observability)

To view sandboxes that were started per project, inspect the command history and view the sandbox URLs, access the Sandboxes [insights](/docs/observability/insights#sandbox) page by:

*   From the Vercel dashboard, go to the project where you created the sandbox
*   Click the Observability tab
*   Click Sandboxes on the left side of the Observability page

To track compute usage for your sandboxes across projects, go to the [Usage](/docs/pricing/manage-and-optimize-usage#viewing-usage) tab of your Vercel dashboard.

--------------------------------------------------------------------------------
title: "Vercel Sandbox examples"
description: "Vercel Sandbox allows you to run arbitrary code in isolated, ephemeral Linux VMs."
last_updated: "null"
source: "https://vercel.com/docs/vercel-sandbox/examples"
--------------------------------------------------------------------------------

# Vercel Sandbox examples

Copy page

Ask AI about this page

Last updated October 23, 2025

Vercel Sandbox is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

Learn how to use the Sandbox SDK through real-life examples.

## [Using a private repository](#using-a-private-repository)

In this example, you create an isolated environment from a private Git repository by authenticating with a [GitHub personal access token](#fine-grained-personal-access-token) or [GitHub App token](#other-github-methods), and run a simple command inside the sandbox.

The `Sandbox.create()` method initializes the environment with the provided repository and configuration options, including authentication credentials, `timeout`, and exposed `ports`. Once created, you can execute commands inside the sandboxed environment using `runCommand`.

TypeScriptPython

private-repo.ts

```
import { Sandbox } from '@vercel/sandbox';
import ms from 'ms';
 
async function main() {
  const sandbox = await Sandbox.create({
    source: {
      url: 'https://github.com/vercel/some-private-repo.git',
      type: 'git',
      // For GitHub, you can use a fine grained, classic personal access token or GitHub App installation access token
      username: 'x-access-token',
      password: process.env.GIT_ACCESS_TOKEN!,
    },
    timeout: ms('5m'),
    ports: [3000],
  });
 
  const echo = await sandbox.runCommand('echo', ['Hello sandbox!']);
  console.log(`Message: ${await echo.stdout()}`);
}
 
main().catch(console.error);
```

### [GitHub access token options](#github-access-token-options)

There are several ways to authenticate with private GitHub repositories.

#### [Fine-grained personal access token](#fine-grained-personal-access-token)

Fine-grained tokens provide repository-specific access and enhanced security:

1.  Go to [GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/personal-access-tokens)
2.  Click Generate new token
3.  Configure the token:
    *   Token name: Give it a descriptive name (e.g., "Vercel Sandbox Access")
    *   Expiration: Set an appropriate expiration date
    *   Resource owner: Select your account or organization
    *   Repository access: Choose "Selected repositories" and select your private repo
    *   Repository permissions: Grant at minimum:
        *   Contents: Read (to clone the repository)
        *   Metadata: Read (for basic repository information)
4.  Click "Generate token" and copy the token
5.  Set it as an environment variable and run your sandbox script:

TypeScriptPython

terminal

```
export GIT_ACCESS_TOKEN=ghp_your_token_here
node --experimental-strip-types ./private-repo.ts
```

#### [Other Github methods](#other-github-methods)

*   [Create a classic personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
*   [Create a GitHub App installation token](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)

## [Install system packages](#install-system-packages)

You can install system packages using the `dnf` system package manager:

TypeScriptPython

install-packages.ts

```
import { Sandbox } from '@vercel/sandbox';
 
const sandbox = await Sandbox.create();
await sandbox.runCommand({
  cmd: 'dnf',
  args: ['install', '-y', 'golang'],
  sudo: true,
});
```

You can find the [list of available packages](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.7.html) on the Amazon Linux documentation.

In the example, `sudo: true` allows the command to run with elevated privileges.

## [Extend the timeout of a running sandbox](#extend-the-timeout-of-a-running-sandbox)

You can extend the timeout of a running sandbox using the `extendTimeout` method, which takes a duration in milliseconds:

TypeScriptPython

sandbox-timeout.ts

```
const sandbox = await Sandbox.create({
  // 15 minute timeout
  timeout: 15 * 60 * 1000,
});
 
// Extend by 10 minutes
await sandbox.extendTimeout(10 * 60 * 1000);
```

You can extend the timeout as many times as you'd like, until the [max timeout for your plan](/docs/vercel-sandbox/pricing#maximum-runtime-duration) has been reached.

--------------------------------------------------------------------------------
title: "Vercel Sandbox pricing and limits"
description: "Vercel Sandbox allows you to run arbitrary code in isolated, ephemeral Linux VMs."
last_updated: "null"
source: "https://vercel.com/docs/vercel-sandbox/pricing"
--------------------------------------------------------------------------------

# Vercel Sandbox pricing and limits

Copy page

Ask AI about this page

Last updated October 23, 2025

Vercel Sandbox is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

## [Resource limits](#resource-limits)

*   Each sandbox can use a maximum of 8 vCPUs with 2 GB of memory allocated per vCPU
*   Sandboxes have a maximum runtime duration of 5 hours for Pro/Enterprise and 45 minutes for Hobby, with a default of 5 minutes. You can configure this using the `timeout` option of `Sandbox.create()`.
*   You can run Node.js or Python runtimes. Review the [system specifications](/docs/vercel-sandbox#system-specifications).
*   Sandboxes can have up to 4 open ports.

## [Pricing](#pricing)

Vercel tracks sandbox usage by:

*   Active CPU: The amount of CPU time your code consumes, measured in milliseconds. Waiting for I/O (e.g. calling AI models, database queries) does not count towards Active CPU.
*   Provisioned memory: The memory size of your sandbox instances (in GB), multiplied by the time they are running (measured in hours).
*   Network bandwidth: The incoming and outgoing network traffic in and out of your sandbox for tasks such as installing packages and sandbox usage by external traffic through the sandbox listening port.
*   Sandbox creations: The number of times you started a sandbox.

### [Included allotment](#included-allotment)

| Metric | Monthly amount included for Hobby |
| --- | --- |
| CPU (hour) | 5 |
| Provisioned Memory (GB-hr) | 420 |
| Network (GB) | 20 |
| Sandbox creations | 5000 |

You can use sandboxes under Pro and Enterprise plans based on the following regional pricing:

| Active CPU time (per hour) | Provisioned Memory (per GB-hr) | Network (per GB) | Sandbox creations (per 1M) |
| --- | --- | --- | --- |
| $0.128 | $0.0106 | $0.15 | $0.60 |

Currently, Vercel Sandbox is only available in the `iad1` region.

### [Maximum runtime duration](#maximum-runtime-duration)

Sandboxes can run for up to several hours based on your plan. The default is 5 minutes.

| Plan | Duration limit |
| --- | --- |
| Hobby | 45 minutes |
| Pro | 5 hours |
| Enterprise | 5 hours |

You can configure the maximum runtime duration using the `timeout` option of `Sandbox.create()` and extend it later using `sandbox.extendTimeout()`:

TypeScriptPython

sandbox-timeout.ts

```
const sandbox = await Sandbox.create({
  // 3 hours timeout
  timeout: 3 * 60 * 60 * 1000,
});
 
// Extend by 2 hours
await sandbox.extendTimeout(2 * 60 * 60 * 1000);
```

You can extend the timeout as many times as you need, until the maximum timeout has been reached.

### [Concurrent sandboxes limit](#concurrent-sandboxes-limit)

At any time, based on your plan, you can run up to a maximum number of sandboxes at the same time. You can [upgrade](/docs/plans/hobby#upgrading-to-pro) if you're on Hobby. For Pro and Enterprise, this limit will only apply during the [Beta](/docs/release-phases#beta) period.

| Plan | Concurrent sandboxes limit |
| --- | --- |
| Hobby | 10 |
| Pro | 2000 |
| Enterprise | 2000 |

Please [get in touch with our sales team](/contact/sales) if you need more concurrent sandboxes.

--------------------------------------------------------------------------------
title: "Vercel Toolbar"
description: "Learn how to use the Vercel Toolbar to leave feedback, navigate through important dashboard pages, share deployments, use Draft Mode for previewing unpublished content, and Edit Mode for editing content in real-time."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar"
--------------------------------------------------------------------------------

# Vercel Toolbar

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel Toolbar is available on [all plans](/docs/plans)

The Vercel Toolbar is a tool that assists in the iteration and development process. Through the toolbar, you can:

*   Leave feedback on deployments with [Comments](/docs/comments)
*   Navigate [through dashboard pages](/docs/vercel-toolbar#using-the-toolbar-menu), and [share deployments](/docs/vercel-toolbar#sharing-deployments)
*   Read and set [Feature Flags](/docs/feature-flags)
*   Use [Draft Mode](/docs/draft-mode) for previewing unpublished content
*   Edit content in real-time using [Edit Mode](/docs/edit-mode)
*   Inspect for [Layout Shifts](/docs/vercel-toolbar/layout-shift-tool) and [Interaction Timing](/docs/vercel-toolbar/interaction-timing-tool)
*   Check for accessibility issues with the [Accessibility Audit Tool](/docs/vercel-toolbar/accessibility-audit-tool)

## [Activating the Toolbar](#activating-the-toolbar)

By default, when the toolbar first shows up on your deployments it is sleeping. This means it will not run any tools in the background or show comments on pages. You can activate it by clicking it or using ctrl. It will start activated if a tool is needed to show you the link you’re visiting, like a link to a comment thread or a link with flags overrides.

Users who have installed the browser extension can toggle on Always Activate in Preferences from the Toolbar menu.

## [Enabling or Disabling the toolbar](#enabling-or-disabling-the-toolbar)

The Vercel Toolbar is enabled by default for all preview deployments. You can disable the toolbar at the [team](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-team-wide), [project](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-project-wide), or [session](/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-session) level.

You can also manage its visibility for [automation](/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-automation) with HTTP headers and through [environment variables](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-for-a-specific-branch). To learn more, see [Managing the toolbar](/docs/vercel-toolbar/managing-toolbar).

To enable the toolbar for your local or production environments, see [Adding the toolbar to your environment](/docs/vercel-toolbar/in-production-and-localhost).

## [Using the Toolbar Menu](#using-the-toolbar-menu)

You can access the Toolbar Menu by pressing ctrl on your keyboard.

Alternatively, you can also access the Toolbar Menu through the Vercel Toolbar by clicking the menu icon. If you haven't activated the toolbar yet, log in first to display the menu.

| Feature | Description |
| --- | --- |
| Search | Quickly search the toolbar and access dashboard pages. |
| Quick branch access | View the current branch and commit hash. |
| Switch branches | Quickly switch between branches (on preview and production branches - not locally). |
| [Layout shifts](/docs/vercel-toolbar/layout-shift-tool) | Open the Layout Shift Tool to identify elements causing layout shifts. |
| [Interaction timing](/docs/vercel-toolbar/interaction-timing-tool) | Inspect in detail each interaction's latency and view your current session's INP. |
| [Accessibility audit tool](/docs/vercel-toolbar/accessibility-audit-tool) | Automatically check the Web Content Accessibility Guidelines 2.0 level A and AA rules. |
| Open Graph | View [open graph](https://ogp.me/#metadata) properties for the page you are on and see what the link preview will look like. |
| [Comments](/docs/comments) | Access the Comments panel to leave or view feedback. |
| [View inbox](/docs/comments/using-comments#comment-threads) | View all open comments. |
| Navigate to your team | Navigate to your team's dashboard. |
| Navigate to your project | Navigate to your project's dashboard. |
| Navigate to your deployment | Navigate to your deployment's dashboard. |
| [Hide Toolbar](#enabling-or-disabling-the-toolbar) | Hide the toolbar. |
| [Disable for session](#enabling-or-disabling-the-toolbar) | Disable the toolbar for the current session. |
| [Set preferences](#toolbar-menu-preferences) | Set personal preferences for the toolbar. |
| Logout | Logout of the toolbar. |

## [Setting Custom Keyboard Shortcuts](#setting-custom-keyboard-shortcuts)

You can set your own keyboard shortcuts to quickly access specific tools. Additionally, you can change the default keyboard shortcuts for the Toolbar Menu ctrl and for showing/hiding the toolbar  . by following these steps:

1.  Select Preferences in the Toolbar Menu
2.  Select Configure next to Keyboard Shortcuts
3.  Select Record shortcut… (or click the X if you have an existing keyboard shortcut set) next to the tool you’d like to set it for
4.  Press the keys you’d like to use as the shortcut for that tool
5.  To change the keyboard shortcuts for opening the Toolbar Menu and for showing and hiding the toolbar, you must have the [Browser Extension](https://vercel.com/docs/vercel-toolbar/browser-extension) installed.

## [Sharing deployments](#sharing-deployments)

You can use the Share button in deployments with the Vercel Toolbar enabled, as well as in all preview deployments, to share your deployment's [generated URL](/docs/deployments/generated-urls). When you use the Share button from the toolbar, the URL will contain any relevant query parameters.

To share a deployment:

1.  Go to the deployment you want to share and ensure you're logged into the Vercel Toolbar.
2.  Find the Share button in the Toolbar Menu and select it.
3.  From the Share dialog, ensure you're allowing the right permissions and click Copy Link to copy the deployment URL to your clipboard. To learn more, see [Sharing Deployments](/docs/deployments/sharing-deployments).

If you're on an [Enterprise](/docs/plans/enterprise) team, you will be able to see who shared deployment URLs in your [audit logs](/docs/observability/audit-log).

## [Reposition toolbar](#reposition-toolbar)

You can reposition the toolbar by dragging it to either side of your screen. It will snap into place and appear there across deployments until you move it again. Repositioning only affects where you see the toolbar, it does not change the toolbar position for your collaborators.

## [Toolbar Menu preferences](#toolbar-menu-preferences)

When logged into the Vercel Toolbar, you'll find a Preferences button in the Toolbar Menu. In this menu, you can update the following settings:

| Setting | Description |
| --- | --- |
| [Notifications](/docs/comments/managing-comments#notifications) | Set when you will receive notifications for comments in the deployment you're viewing |
| Theme | Select your color theme |
| Layout Shift Detection | Enable or disable the [Layout Shift Tool](/docs/vercel-toolbar/layout-shift-tool) |
| [Keyboard Shortcuts](#setting-custom-keyboard-shortcuts) | Set custom keyboard shortcuts for tools and change the default keyboard shortcuts |
| Accessibility Audit | Enable or disable the [Accessibility Audit Tool](/docs/vercel-toolbar/accessibility-audit-tool) |
| Measure Interaction Timing | Enable or disable the [Interaction Timing Tool](/docs/vercel-toolbar/interaction-timing-tool) |
| [Browser Extension](/docs/vercel-toolbar/browser-extension) | Add Vercel's extension to your browser to take screenshots, enable the toolbar in production, and access Always Activate and Start Hidden preferences. |
| Always Activate | Sets the toolbar to activate anytime you are authenticated as your Vercel user instead of waiting to be clicked. |
| Start Hidden | Sets the toolbar to start hidden. Read more about [hiding and showing the toolbar](/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-session). |

## [More resources](#more-resources)

*   [Preview deployments](/docs/deployments/environments#preview-environment-pre-production)
*   [Comments](/docs/comments)
*   [Draft Mode](/docs/draft-mode)
*   [Edit Mode](/docs/edit-mode)

--------------------------------------------------------------------------------
title: "Accessibility Audit Tool"
description: "Learn how to use the Accessibility Audit Tool to automatically check the Web Content Accessibility Guidelines 2.0 level A and AA rules."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/accessibility-audit-tool"
--------------------------------------------------------------------------------

# Accessibility Audit Tool

Copy page

Ask AI about this page

Last updated September 24, 2025

Accessibility Audit Tool is available on [all plans](/docs/plans)

The accessibility audit tool automatically checks the [Web Content Accessibility Guidelines 2.0](https://www.w3.org/TR/WCAG20/) level A and AA rules, grouping them by impact as defined by [deque axe](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md#wcag-21-level-a--aa-rules), and runs in the background on [all environments the toolbar and added to](/docs/vercel-toolbar/in-production-and-localhost).

## [Accessing the accessibility audit tool](#accessing-the-accessibility-audit-tool)

To access the accessibility audit tool:

1.  [Open the Toolbar Menu](/docs/vercel-toolbar#using-the-toolbar-menu)
2.  Select the Accessibility Audit option. If there are accessibility issues detected on the page, a badge will display next to the option. The number inside the badge details the number of issues detected
3.  The Accessibility panel will open on the right side of the screen. Here you can filter by All, Critical, Serious, Moderate, and Minor issues

## [Enabling or disabling the accessibility audit tool](#enabling-or-disabling-the-accessibility-audit-tool)

The accessibility audit tool is enabled by default. To disable it:

1.  Open the Preferences panel by selecting the toolbar menu icon, then scrolling down to the Preferences section
2.  Toggle the Accessibility Audit option to enable or disable the tool

## [Inspecting accessibility issues](#inspecting-accessibility-issues)

To inspect an accessibility issue select the filter option you want to inspect. A list of issues will are displayed as dropdowns. You can select each dropdown to view the issue details, including an explanation of the issue and a link to the relevant WCAG guideline. Hovering over the failing elements markup will highlight the element on the page, while clicking on the element will log it to the devtools console.

![Using the Accessibility Audit Tool](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fvercel-toolbar%2Faccessibility-audit-panel-light.png&w=1080&q=75)![Using the Accessibility Audit Tool](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fvercel-toolbar%2Faccessibility-audit-panel-dark.png&w=1080&q=75)

Using the Accessibility Audit Tool

## [Recording accessibility issues](#recording-accessibility-issues)

By default the accessibility audit tool will log issues on page load. To test ephemeral states, such as hover or focus, you can record issues by interacting with the page. To record issues select the Start Recording button in the Accessibility panel. This will start recording issues as you interact with the page. To stop recording, select the Stop Recording button. Recording persists for your session, so you can refresh the page, or navigate to a new page and it will continue to record issues while your tab is active.

## [More resources](#more-resources)

*   [Interaction Timing Tool](/docs/vercel-toolbar/interaction-timing-tool)
*   [Layout Shift Tool](/docs/vercel-toolbar/layout-shift-tool)

--------------------------------------------------------------------------------
title: "Toolbar Browser Extensions"
description: "The browser extensions enable you to use the toolbar in production environments, take screenshots and attach them to comments, and set personal preferences for how the toolbar behaves."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/browser-extension"
--------------------------------------------------------------------------------

# Toolbar Browser Extensions

Copy page

Ask AI about this page

Last updated March 4, 2025

The browser extensions are available on [all plans](/docs/plans)

The browser extension is supported in Chrome, Firefox, Opera, Microsoft Edge, in addition to other Chromium-based browsers that support extensions and enhances the toolbar in the following ways:

*   Enables the toolbar to detect when you are logged in to Vercel.
*   Operates faster and with fewer network requests.
*   Remembers your [personal preferences](#setting-user-preferences) for when the toolbar hides and activates.
*   Allows you to [take screenshots](#taking-screenshots-with-the-extension) and attach them to comments.
*   Click the extension to hide and show the toolbar, and pin it to your browser bar for quick access.

## [Installing the browser extension](#installing-the-browser-extension)

Install the browser extension from your browser's extension page:

*   [
    
    Chrome
    
    ](https://chromewebstore.google.com/detail/vercel/lahhiofdgnbcgmemekkmjnpifojdaelb)
*   [
    
    Firefox
    
    ](https://addons.mozilla.org/en-US/firefox/addon/vercel)

You can also install the Chrome extension using the link above in Opera and Microsoft Edge.

## [Setting user preferences](#setting-user-preferences)

With the browser extension you are able to toggle on the following preferences that affect how the toolbar behaves for you without altering its behavior for your team members:

| Setting | Description |
| --- | --- |
| Always Activate | Sets the toolbar to activate anytime you are authenticated as your Vercel user instead of waiting to be clicked. |
| Start Hidden | Sets the toolbar to start hidden. Read more about [hiding and showing the toolbar](/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-session). |

## [Taking screenshots with the extension](#taking-screenshots-with-the-extension)

The extension enables you to leave comments with screenshots attached by clicking, dragging, and releasing to select the area of the page you'd like to screenshot and comment on. To do this:

1.  Select Comment in the toolbar menu.
2.  Click, drag, and release to select the area of the page you'd like to screenshot.
3.  Compose your comment and click the send icon.

--------------------------------------------------------------------------------
title: "Add the Vercel Toolbar to local and production environments"
description: "Learn how to use the Vercel Toolbar in production and local environments."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/in-production-and-localhost"
--------------------------------------------------------------------------------

# Add the Vercel Toolbar to local and production environments

Copy page

Ask AI about this page

Last updated May 23, 2025

The Vercel Toolbar is available by default on all [preview environments](/docs/deployments/environments#preview-environment-pre-production). In production environments the toolbar supports ongoing team collaboration and project iteration. When used in development environments, you can see and resolve preview comments during development, streamlining the process of iterating on your project.

All toolbar features such as [Comments](/docs/comments/using-comments), [Feature Flags](/docs/feature-flags), [Draft Mode](/docs/draft-mode), and [Edit Mode](/docs/edit-mode), are available in both production and development environments.

*   [Add the toolbar to your local or production environment](/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost)

--------------------------------------------------------------------------------
title: "Add the Vercel Toolbar to your local environment"
description: "Learn how to use the Vercel Toolbar in your local environment."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost"
--------------------------------------------------------------------------------

# Add the Vercel Toolbar to your local environment

Copy page

Ask AI about this page

Last updated September 24, 2025

To enable the toolbar in your local environment, add it to your project using the [`@vercel/toolbar`](https://www.npmjs.com/package/@vercel/toolbar) package, or with an injection script.

1.  ### [Install the `@vercel/toolbar` package and link your project](#install-the-@vercel/toolbar-package-and-link-your-project)
    
    Install the package using the following command:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/toolbar
    ```
    
    Then link your local project to your Vercel project with the [`vercel link`](/docs/cli/link) command using [Vercel CLI](/docs/cli).
    
    terminal
    
    ```
    vercel link [path-to-directory]
    ```
    
2.  ### [Add the toolbar to your project](#add-the-toolbar-to-your-project)
    
    To use the Vercel Toolbar locally in a Next.js project, define `withVercelToolbar` in your `next.config.js` file and export it, as shown below:
    
    next.config.js
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitNuxtOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    /** @type {import('next').NextConfig} */
    const createWithVercelToolbar = require('@vercel/toolbar/plugins/next');
    const nextConfig = {
      // Config options here
    };
     
    const withVercelToolbar = createWithVercelToolbar();
    // Instead of module.exports = nextConfig, do this:
    module.exports = withVercelToolbar(nextConfig);
    ```
    
    Then add the following code to your `layout.tsx` or `layout.jsx` file:
    
    app/layout.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitNuxtOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { VercelToolbar } from '@vercel/toolbar/next';
     
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode;
    }) {
      const shouldInjectToolbar = process.env.NODE_ENV === 'development';
      return (
        <html lang="en">
          <body>
            {children}
            {shouldInjectToolbar && <VercelToolbar />}
          </body>
        </html>
      );
    }
    ```

--------------------------------------------------------------------------------
title: "Add the Vercel Toolbar to your production environment"
description: "Learn how to add the Vercel Toolbar to your production environment and how your team members can use tooling to access the toolbar."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-production"
--------------------------------------------------------------------------------

# Add the Vercel Toolbar to your production environment

Copy page

Ask AI about this page

Last updated October 9, 2025

As a [team owner](/docs/rbac/access-roles#owner-role) or [member](/docs/rbac/access-roles#member-role), you can enable the toolbar in your production environment for sites that your team(s) own, either [through the dashboard](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-project-wide) or by [adding the `@vercel/toolbar` package](/docs/vercel-toolbar/in-production-and-localhost/add-to-production#adding-the-toolbar-using-the-@vercel/toolbar-package) to your project.

## [Adding the toolbar using the browser extension](#adding-the-toolbar-using-the-browser-extension)

For team members that use supported browsers and want the most straightforward experience, we recommend using the [Vercel Browser Extension](/docs/vercel-toolbar/browser-extension) to get access to the toolbar on your team's production sites.

For team members that use browsers for which a Vercel extension is not available, to allow toolbar access for everyone that accesses your site, or if you have more complex rules for when it shows in production, you'll need to [add the `@vercel/toolbar` package](/docs/vercel-toolbar/in-production-and-localhost/add-to-production#adding-the-toolbar-using-the-@vercel/toolbar-package) to your project.

## [Adding the toolbar using the `@vercel/toolbar` package](#adding-the-toolbar-using-the-@vercel/toolbar-package)

For team members that do not use the browser extension or if you have more complex rules for when the toolbar shows in production, you can add the `@vercel/toolbar` package to your project:

1.  ### [Install the `@vercel/toolbar` package and link your project](#install-the-@vercel/toolbar-package-and-link-your-project)
    
    Install the package in your project using the following command:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/toolbar
    ```
    
    Then link your local project to your Vercel project with the [`vercel link`](/docs/cli/link) command using [Vercel CLI](/docs/cli).
    
    terminal
    
    ```
    vercel link [path-to-directory]
    ```
    
2.  ### [Add the toolbar to your project](#add-the-toolbar-to-your-project)
    
    Before using the Vercel Toolbar in a production deployment Vercel recommends conditionally injecting the toolbar. Otherwise, all visitors will be prompted to log in when visiting your site.
    
    The following example demonstrates code that will show the Vercel Toolbar to a team member on a production deployment.
    
    components/staff-toolbar.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitNuxtOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    'use client';
     
    import { VercelToolbar } from '@vercel/toolbar/next';
     
    function useIsEmployee() {
      // Replace this stub with your auth library hook
      return false;
    }
     
    export function StaffToolbar() {
      const isEmployee = useIsEmployee();
      return isEmployee ? <VercelToolbar /> : null;
    }
    ```
    
    app/layout.tsx
    
    Next.js (/app)
    
    Next.js (/app)Next.js (/pages)SvelteKitNuxtOther frameworks
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { Suspense, type ReactNode } from 'react';
    import { StaffToolbar } from '../components/staff-toolbar';
     
    export default function RootLayout({ children }: { children: ReactNode }) {
      return (
        <html lang="en">
          <body>
            {children}
            <Suspense fallback={null}>
              <StaffToolbar />
            </Suspense>
          </body>
        </html>
      );
    }
    ```
    
3.  ### [Managing notifications and integrations for Comments on production](#managing-notifications-and-integrations-for-comments-on-production)
    
    Unlike comments on preview deployments, alerts for new comments won't be sent to a specific user by default. Vercel recommends [linking your project to Slack with the integration](/docs/comments/integrations#use-the-vercel-slack-app), or directly mentioning someone when starting a new comment thread in production to ensure new comments are seen.
    

## [Enabling the Vercel Toolbar](#enabling-the-vercel-toolbar)

Alternatively to using the package, you can enable access to the Vercel Toolbar for your production environment at the team or project level. Once enabled, team members can access the toolbar using the [Vercel Browser Extension](/docs/vercel-toolbar/browser-extension) or by [enabling it in the toolbar menu](#accessing-the-toolbar-using-the-toolbar-menu).

1.  Navigate to [your Vercel dashboard](/dashboard) and make sure that you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector). To manage the toolbar at the project level, ensure that you have selected the project.
2.  From your [dashboard](/dashboard), select the Settings tab.
3.  In the General section, find Vercel Toolbar.
4.  Under each environment (Preview and Production), select either On or Off from the dropdown to determine the visibility of the Vercel Toolbar for that environment.
5.  Once set at the team level, you can optionally choose to allow the setting to be overridden at the project level.

![The dashboard setting to enable or disable the toolbar at the team level.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar at the team level.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-dark.png&w=1920&q=75)

The dashboard setting to enable or disable the toolbar at the team level.

### [Disabling the toolbar](#disabling-the-toolbar)

If you have noticed that the toolbar is showing up for team members on your production sites, you can disable it at either the team or project level:

1.  Navigate to [your Vercel dashboard](/dashboard) and make sure that you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector). To manage the toolbar at the project level, ensure that you have selected the project.
2.  From your [dashboard](/dashboard), select the Settings tab.
3.  In the General section, find Vercel Toolbar.
4.  Under Production select Off from the dropdown.

## [Acessing the toolbar using the Vercel dashboard](#acessing-the-toolbar-using-the-vercel-dashboard)

You can send team members and users a production deployment with the Vercel Toolbar included from the dashboard. To do so:

1.  From your dashboard, go to your project and select the Projects tab. Alternatively, you can also use the deployment overview page.
2.  Click the dropdown on the Visit button and select Visit with Toolbar. This will take you to your production deployment with the toolbar showing and active.

This will not show for users who have the browser extension installed, as the extension will already show the toolbar whenever you visit your production deployment unless it is disabled in team or project settings.

## [Accessing the toolbar using the Browser extension](#accessing-the-toolbar-using-the-browser-extension)

Provided [the Vercel toolbar is enabled](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-project-wide) for your project, any team member can use the Vercel Toolbar in your production environment by installing the [Vercel Browser Extension](/docs/vercel-toolbar/browser-extension). The extension allows you to access the toolbar on any website hosted on Vercel that your team(s) own:

1.  Install the [Vercel Browser Extension](/docs/vercel-toolbar/browser-extension).
2.  Ensure that you are logged in to your Vercel account on vercel.com. You must be signed in for the extension to know which domains you own.
3.  Ensure that you have deployed to production. Older deployments do not support injection through the browser extension.
4.  Ensure that any team members that need access to the toolbar in production follow these steps to install the domain.

## [Accessing the toolbar using the toolbar menu](#accessing-the-toolbar-using-the-toolbar-menu)

Provided [the Vercel toolbar is enabled](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-project-wide) for your project, you can enable the toolbar on production environments from the toolbar menu:

1.  Open a preview deployment of your project.
2.  Select the menu icon in the toolbar.
3.  Scroll down to Enable Vercel Toolbar in Production and select it.
4.  Choose the domain you want to enable the toolbar on.

--------------------------------------------------------------------------------
title: "Interaction Timing Tool"
description: "The interaction timing tool allows you to inspect in detail each interaction's latency and get notified for interactions taking >200ms."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/interaction-timing-tool"
--------------------------------------------------------------------------------

# Interaction Timing Tool

Copy page

Ask AI about this page

Last updated July 18, 2025

Interaction Timing Tool is available on [all plans](/docs/plans)

As you navigate your site, the interaction timing tool allows you to inspect in detail each interaction's latency and get notified with toasts for interactions taking > 200ms. This can help you ensure your site's [Interaction to Next Paint (INP)](/blog/first-input-delay-vs-interaction-to-next-paint) (a Core Web Vitals) has a good score.

## [Accessing the Interaction Timing Tool](#accessing-the-interaction-timing-tool)

To access the interaction timing tool:

1.  [Open the Toolbar Menu](/docs/vercel-toolbar#using-the-toolbar-menu)
2.  Select the Interaction Timing option. If any interaction has been detected on the page, a badge will display next to the option. The number inside the badge is the current INP
3.  The Interaction Timing popover will open on the right side of the screen. As you navigate your site, each interaction will appear in this panel. Mouse over the interaction timeline to understand how the duration of input delay, processing (event handlers), and rendering are affecting the interaction's latency

## [Interaction Timing Tool Preferences](#interaction-timing-tool-preferences)

To change preferences for the interaction timing tool:

1.  [Open the Toolbar Menu](/docs/vercel-toolbar#using-the-toolbar-menu)
2.  Select the Preferences option
3.  Select your desired setting for Measure Interaction Timing
    *   On will show the toasts for interactions taking >200ms
    *   On (Silent) will not show toasts, but will still track interaction timing and display it in the interaction timing side panel when opened
    *   Off will turn off tracking for interaction timing

## [More resources](#more-resources)

*   [Preview deployments overview](/docs/deployments/environments#preview-environment-pre-production)
*   [Using comments with preview deployments](/docs/comments/using-comments)
*   [Draft mode](/docs/draft-mode)

--------------------------------------------------------------------------------
title: "Layout Shift Tool"
description: "The layout shift tool gives you insight into any elements that may cause layout shifts on the page."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/layout-shift-tool"
--------------------------------------------------------------------------------

# Layout Shift Tool

Copy page

Ask AI about this page

Last updated September 24, 2025

Layout Shift Tool is available on [all plans](/docs/plans)

The layout shift tool gives you insight into any elements that may cause layout shifts on the page. The cause for a layout shift could be many things:

*   Elements that change in height or width
*   Custom font loading
*   Media embeds (images, iframes, videos, etc.) that do not have set dimensions
*   Dynamic content that's injected at runtime
*   Animations that affect layout

Layout shifts play a part in [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained) and contribute to [Speed Insights](/docs/speed-insights/metrics#core-web-vitals-explained) scores. With the layout shift tool, you can see which elements are contributing to a layout shift and by how much.

## [Accessing the layout shift tool](#accessing-the-layout-shift-tool)

To access the layout shift tool:

1.  [Open the toolbar menu](/docs/vercel-toolbar#using-the-toolbar-menu)
2.  Select the Layout Shifts option. If there are layout shifts detected on the page, a badge will display next to the option. The number inside the badge details the number of shifts detected
3.  The Layout Shifts popover will open on the right side of the screen. Here you can filter, inspect, and replay any detected layout shifts

Each shift details its impact, the responsible element, and a description of the shift if available. For example, "became taller when its text changed and shifted another element". Hovering over a layout shift will highlight the affected element. You can also replay layout shifts to get a better understanding of what's happening.

## [Inspecting layout shifts](#inspecting-layout-shifts)

You can replay a layout shift by either:

*   Double-clicking it
*   Selecting it and using the Replay selected shift button

You can also select more than one shift and play them at the same time. You may want to do this to see the combined effect of element shifts on the page.

When you replay layout shifts, the Vercel Toolbar will become your stop button. Press this to stop replaying layout shifts. Alternatively, press the  esc key.

You can also disable layout shift detection on a per element basis. You can do this by adding a `data-allow-shifts` attribute to an element. This will affect the element and its descendants.

## [Disabling the layout shift tool](#disabling-the-layout-shift-tool)

To disable the layout shift tool completely:

1.  [Open the Toolbar Menu](/docs/vercel-toolbar#using-the-toolbar-menu)
2.  Select Preferences
3.  Toggle the setting for Layout Shift Detection

## [More resources](#more-resources)

*   [Preview deployments overview](/docs/deployments/environments#preview-environment-pre-production)
*   [Using comments with preview deployments](/docs/comments/using-comments)
*   [Draft mode](/docs/draft-mode)

--------------------------------------------------------------------------------
title: "Managing the visibility of the Vercel Toolbar"
description: "Learn how to enable or disable the Vercel Toolbar for your team, project, and session."
last_updated: "null"
source: "https://vercel.com/docs/vercel-toolbar/managing-toolbar"
--------------------------------------------------------------------------------

# Managing the visibility of the Vercel Toolbar

Copy page

Ask AI about this page

Last updated July 18, 2025

Vercel Toolbar is available on [all plans](/docs/plans)

## [Viewing the toolbar](#viewing-the-toolbar)

When the toolbar is enabled, you'll be able to view it on any preview or enabled environment. By default, the toolbar will appear as a circle with a menu icon. Clicking activates it, at which point you will see any comments on the page and notifications for issues detected by tools running in the background. When the toolbar has not been activated it will show a small Vercel icon over the menu icon.

Once a tool is used, the toolbar will show a second icon next to the menu, so you can access your most recently used tool.

## [Enable or disable the toolbar team-wide](#enable-or-disable-the-toolbar-team-wide)

To disable the toolbar by default for all projects in your team:

1.  Navigate to [your Vercel dashboard](/dashboard) and make sure that you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector).
2.  From your [dashboard](/dashboard), select the Settings tab.
3.  In the General section, find Vercel Toolbar.
4.  Under each environment (Preview and Production), select either On or Off from the dropdown to determine the visibility of the Vercel Toolbar for that environment.
5.  You can optionally choose to allow the setting to be overridden at the project level.

![The dashboard setting to enable or disable the toolbar at the team level.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar at the team level.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-dark.png&w=1920&q=75)

The dashboard setting to enable or disable the toolbar at the team level.

## [Enable or disable the toolbar project-wide](#enable-or-disable-the-toolbar-project-wide)

To disable the toolbar project-wide:

1.  From your [dashboard](/dashboard), select the project you want to enable or disable Vercel Toolbar for.
2.  Navigate to Settings tab.
3.  In the General section, find Vercel Toolbar.
4.  Under each environment (Preview and Production), select either an option from the dropdown to determine the visibility of Vercel Toolbar for that environment. The options are:
    *   Default: Respect team-level visibility settings.
    *   On: Enable the toolbar for the environment.
    *   Off: Disable the toolbar for the environment.

![The dashboard setting to enable or disable the toolbar in a project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fproject-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar in a project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fproject-level-toolbar-management-dark.png&w=1920&q=75)

The dashboard setting to enable or disable the toolbar in a project.

## [Disable toolbar for session](#disable-toolbar-for-session)

To disable the toolbar in the current browser tab:

1.  Activate the Vercel Toolbar by clicking on it
2.  In the toolbar menu, scroll down the list and select Disable for Session.

To show the toolbar again, open a new browser session.

Alternatively, you can also hide the toolbar in any of the following ways:

*   Select the toolbar icon and drag it to the X that appears at the bottom of the screen.
*   Click the [browser extension](/docs/vercel-toolbar/browser-extension) icon if you have it pinned to your browser bar.
*   Use  ..

To show the toolbar when it is hidden you can use that same key command or click the browser extension.

Users with the browser extension can set the toolbar to start hidden by toggling on Start Hidden in Preferences from the Toolbar menu.

## [Disable toolbar for automation](#disable-toolbar-for-automation)

You can use the `x-vercel-skip-toolbar` header to prevent interference with automated end-to-end tests:

1.  Add the `x-vercel-skip-toolbar` header to the request sent to [the preview deployment URL](/docs/deployments/environments#preview-environment-pre-production#preview-urls)
2.  Optionally, you can assign the value `1` to the header. However, presence of the header itself triggers Vercel to disable the toolbar

## [Enable or disable the toolbar for a specific branch](#enable-or-disable-the-toolbar-for-a-specific-branch)

You can use Vercel's [preview environment variables](/docs/environment-variables#preview-environment-variables) to manage the toolbar for specific branches or environments

To enable the toolbar for an individual branch, add the following to the environment variables for the desired preview branch:

.env

```
VERCEL_PREVIEW_FEEDBACK_ENABLED=1
```

To disable the toolbar for an individual branch, set the above environment variable's value to `0`:

.env

```
VERCEL_PREVIEW_FEEDBACK_ENABLED=0
```

## [Using the toolbar with a custom alias domain](#using-the-toolbar-with-a-custom-alias-domain)

To use the toolbar with preview deployments that have [custom alias domains](/docs/domains/add-a-domain), you must opt into the toolbar explicitly in your project settings on [the dashboard](/dashboard).

## [Using a Content Security Policy](#using-a-content-security-policy)

If you have a [Content Security Policy (CSP)](https://developer.mozilla.org/docs/Web/HTTP/CSP) configured, you may need to adjust the CSP to enable access to the Vercel Toolbar or Comments.

You can make the following adjustments to the `Content-Security-Policy` [response header](/docs/headers/cache-control-headers#custom-response-headers):

*   Add the following to `script-src` (Most commonly used):
    
    ```
    script-src https://vercel.live
    ```
    
*   Add the following to `connect-src`:
    
    ```
    connect-src https://vercel.live wss://ws-us3.pusher.com
    ```
    
*   Add the following to `img-src`:
    
    ```
    img-src https://vercel.live https://vercel.com data: blob:
    ```
    
*   Add the following to `frame-src`:
    
    ```
    frame-src https://vercel.live
    ```
    
*   Add the following to `style-src`:
    
    ```
    style-src https://vercel.live 'unsafe-inline'
    ```
    
*   Add the following to `font-src`:
    
    ```
    font-src https://vercel.live https://assets.vercel.com
    ```

--------------------------------------------------------------------------------
title: "Setting Up Webhooks"
description: "Learn how to set up webhooks and use them with Vercel Integrations."
last_updated: "null"
source: "https://vercel.com/docs/webhooks"
--------------------------------------------------------------------------------

# Setting Up Webhooks

Copy page

Ask AI about this page

Last updated September 24, 2025

A webhook is a trigger-based HTTP endpoint configured to receive HTTP POST requests through events. When an event happens, a webhook is sent to another third-party app, which can then take appropriate action.

Webhooks configured with Vercel can trigger a deployment when a specific event occurs. Vercel integrations receive platform events through webhooks.

## [Account Webhooks](#account-webhooks)

Account Webhooks are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Vercel allows you to add a generic endpoint for events from your dashboard. [Pro](/docs/plans/pro) and [Enterprise](/docs/plans/enterprise) teams will be able to configure these webhooks at the account level.

### [Configure a webhook](#configure-a-webhook)

1.  ### [Go to your team settings](#go-to-your-team-settings)
    
    Choose your team scope on the dashboard, and go to Settings ➞ Webhooks.
    
2.  ### [Select the events to listen to](#select-the-events-to-listen-to)
    
    ![Select events for your webhooks to listen.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fwebhooks-add-events-light.png&w=1920&q=75)![Select events for your webhooks to listen.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fwebhooks-add-events-dark.png&w=1920&q=75)
    
    Select events for your webhooks to listen.
    
    The configured webhook listens to one or more events before it triggers the function request. Vercel supports event selections from the following categories:
    
    #### [Deployment Events](#deployment-events)
    
    Configurable webhooks listen to the following deployment-based events:
    
    *   Deployment Created: Listens for when any new deployment is initiated
    *   Deployment Succeeded: Listens for a successful deployment
    *   Deployment Promoted: Listens for when a deployment is promoted
    *   Deployment Error: Listens for any failed deployment
    *   Deployment Cancelled: Listens for a canceled deployment due to any failure
    
    #### [Project Events](#project-events)
    
    Project events are only available when "All Team Projects" is selected as the [project scope](#choose-your-target-projects).
    
    Configurable webhooks listen to the following project-based events:
    
    *   Project Created: Listens whenever a new project is created
    *   Project Removed: Listens whenever any project is deleted from the team account
    
    #### [Firewall events](#firewall-events)
    
    Configurable webhooks listen to the following firewall-based events:
    
    *   Attack Detected: Listens for when the [Vercel Firewall](/docs/vercel-firewall) detects and mitigates a [DDoS attack](/docs/security/ddos-mitigation)
    
    The events you select should depend on your use case and the workflow you want to implement.
    
3.  ### [Choose your target projects](#choose-your-target-projects)
    
    ![Choose the scope of project(s) for webhooks.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fproject-scope.png&w=1920&q=75)![Choose the scope of project(s) for webhooks.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fproject-scope-dark.png&w=1920&q=75)
    
    Choose the scope of project(s) for webhooks.
    
    After selecting the event types, choose the scope of team projects for which webhooks will listen for events.
    
4.  ### [Enter your endpoint URL](#enter-your-endpoint-url)
    
    The endpoint URL is the destination that triggers the events. All events are forwarded to this URL as a POST request. In case of an event, your webhook initiates an HTTP callback to this endpoint that you must configure to receive data. In order to be accessible, make sure these endpoint URLs are public.
    
    ![Define the endpoint URL for the webhooks to listen.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fenter-endpoint-light.png&w=1920&q=75)![Define the endpoint URL for the webhooks to listen.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fenter-endpoint-dark.png&w=1920&q=75)
    
    Define the endpoint URL for the webhooks to listen.
    
    Once you have configured your webhook, click the Create Webhook button.
    
    The Webhook Created dialog will display a secret key, which won't be shown again. You should secure your webhooks by comparing the [`x-vercel-signature`](/docs/headers/request-headers#x-vercel-signature) header of an incoming request with this client secret. See [Securing webhooks](/docs/integrations/webhooks-overview/webhooks-api#securing-webhooks) to learn how to do this.
    
    ![Confirmation to create the webhook.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fwebhook-created-light.png&w=1080&q=75)![Confirmation to create the webhook.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fwebhook-created-dark.png&w=1080&q=75)
    
    Confirmation to create the webhook.
    
    Once complete, click Done.
    
    To view all your new and existing webhooks, go to the Webhooks section of your team's dashboard. To remove any webhook, click the cross icon next to the webhook. You can create and use up to 20 custom webhooks per team.
    

## [Integration Webhooks](#integration-webhooks)

Webhooks can also be created through [Integrations](/docs/integrations). When [creating a new integration](/docs/integrations/create-integration), you can add webhooks using the [Integration Console](/dashboard/integrations/create). Inside your Integration's settings page locate the text field for setting the webhook URL. This is where you should add the HTTP endpoint to listen for events. Next, you can select one or more of these checkboxes to specify which events to listen to.

![Specifying the webhook URL and events to listen to.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fwebhooks-url-integrations-light.png&w=1920&q=75)![Specifying the webhook URL and events to listen to.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fwebhooks%2Fwebhooks-url-integrations-dark.png&w=1920&q=75)

Specifying the webhook URL and events to listen to.

## [Events](#events)

The webhook URL receives an HTTP POST request with a JSON payload for each event. All the events have the following format:

webhook-payload

```
"id": <eventId>,
  "type": <event-type>,
  "createdAt": <javascript-timestamp>,
  "payload": <payload for the event>,
  "region": <RegionId>,
```

Here's a [list of supported event types](/docs/integrations/webhooks-overview/webhooks-api#supported-event-types) and their [`payload`](/docs/integrations/webhooks-overview/webhooks-api#payload).

--------------------------------------------------------------------------------
title: "Webhooks API Reference"
description: "Vercel Integrations allow you to subscribe to certain trigger-based events through webhooks. Learn about the supported webhook events and how to use them."
last_updated: "null"
source: "https://vercel.com/docs/webhooks/webhooks-api"
--------------------------------------------------------------------------------

# Webhooks API Reference

Copy page

Ask AI about this page

Last updated October 21, 2025

Vercel Integrations allow you to subscribe to certain trigger-based events through webhooks. An example use-cases for webhooks might be cleaning up resources after someone removes your Integration.

## [Payload](#payload)

The webhook payload is a JSON object with the following keys.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| type | [String](/docs/rest-api/reference/welcome#types) | The [event type](#supported-event-types). |
| id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the webhook delivery. |
| createdAt | [Date](/docs/rest-api/reference/welcome#types) | The webhook delivery timestamp. |
| region | [String](/docs/rest-api/reference/welcome#types) | The region the event occurred in (possibly null). |
| payload | [Object](/docs/rest-api/reference/welcome#types) | The payload of the webhook. See [Supported Event Types](#supported-event-types) for more information. |

## [Supported Event Types](#supported-event-types)

### [deployment.canceled](#deployment.canceled)

Occurs whenever a deployment is canceled.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment.check-rerequested](#deployment.check-rerequested)

Occurs when a user has requested for a [check](/docs/integrations/checks-overview) to be rerun after it failed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.check.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the check. |

### [deployment.cleanup](#deployment.cleanup)

Occurs whenever a deployment is cleaned up after it has been fully removed either due to explicit removal or retention rules.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.deployment.alias | [List](/docs/rest-api/reference/welcome#types) | An array of aliases that will get assigned when the deployment is ready. |
| payload.deployment.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.deployment.customEnvironmentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the custom environment, if the custom environment is used. |
| payload.deployment.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |

### [deployment.created](#deployment.created)

Occurs whenever a deployment is created.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.alias | [List](/docs/rest-api/reference/welcome#types) | An array of aliases that will get assigned when the deployment is ready. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment.error](#deployment.error)

Occurs whenever a deployment has failed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment.integration.action.cancel](#deployment.integration.action.cancel)

Occurs when an integration deployment action or the deployment itself is canceled.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.resourceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration resource for which the action is canceled. |
| payload.action | [String](/docs/rest-api/reference/welcome#types) | The action slug, declared by the integration |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |

### [deployment.integration.action.cleanup](#deployment.integration.action.cleanup)

Occurs when a deployment that executed an integration deployment action is cleaned up, such as due to the deployment retention policy.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.resourceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration resource for which the action is cleaned up. |
| payload.action | [String](/docs/rest-api/reference/welcome#types) | The action slug, declared by the integration |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |

### [deployment.integration.action.start](#deployment.integration.action.start)

Occurs when a deployment starts an integration deployment action.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.resourceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration resource for which the action is started. |
| payload.action | [String](/docs/rest-api/reference/welcome#types) | The action slug, declared by the integration |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |

### [deployment.promoted](#deployment.promoted)

Occurs whenever a deployment is promoted.

This event gets fired after a production deployment is [promoted](/docs/deployments/promoting-a-deployment#staging-and-promoting-a-production-deployment) to start serving production traffic. This can happen automatically after a successful build, or after running the [promote](/docs/cli/promote) command.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment.ready](#deployment.ready)

Occurs whenever a deployment is successfully built and your integration has registered at least one [check](/docs/integrations/checks-overview).

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment.succeeded](#deployment.succeeded)

Occurs whenever a deployment is ready.

This event gets fired after all blocking Checks have passed. See [`deployment-prepared`](/docs/integrations#webhooks/events/deployment-prepared) if you registered Checks.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [domain.created](#domain.created)

Occurs whenever a domain has been created.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The Domain name created. |
| payload.domain.delegated | [Boolean](/docs/rest-api/reference/welcome#types) | Whether or not the domain was delegated/shared. |

### [domain.auto-renew-changed](#domain.auto-renew-changed)

Occurs whenever a domain's auto-renewal setting is changed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain. |
| payload.previous | [Boolean](/docs/rest-api/reference/welcome#types) | The previous auto-renewal setting. |
| payload.next | [Boolean](/docs/rest-api/reference/welcome#types) | The new auto-renewal setting. |

### [domain.certificate-add](#domain.certificate-add)

Occurs whenever a new SSL certificate is added for a domain.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.cert | [Object](/docs/rest-api/reference/welcome#types) | The certificate object containing certificate details. |

### [domain.certificate-add-failed](#domain.certificate-add-failed)

Occurs whenever adding a new SSL certificate for a domain fails.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.dnsNames | [List](/docs/rest-api/reference/welcome#types) | An array of DNS names for which the certificate addition failed. |

### [domain.certificate-deleted](#domain.certificate-deleted)

Occurs whenever an SSL certificate is deleted for a domain.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.cert | [Object](/docs/rest-api/reference/welcome#types) | The certificate object containing certificate details. |

### [domain.certificate-renew](#domain.certificate-renew)

Occurs whenever an SSL certificate is renewed for a domain.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.cert | [Object](/docs/rest-api/reference/welcome#types) | The certificate object containing certificate details. |

### [domain.certificate-renew-failed](#domain.certificate-renew-failed)

Occurs whenever renewing an SSL certificate for a domain fails.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.dnsNames | [List](/docs/rest-api/reference/welcome#types) | An array of DNS names for which the certificate renewal failed. |

### [domain.dns-records-changed](#domain.dns-records-changed)

Occurs whenever DNS records for a domain are modified.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.zone | [String](/docs/rest-api/reference/welcome#types) | The DNS zone that was modified. |
| payload.changes | [List](/docs/rest-api/reference/welcome#types) | An array of changes made to the DNS records. |

### [domain.renewal](#domain.renewal)

Occurs whenever a domain is renewed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that was renewed. |
| payload.price | [String](/docs/rest-api/reference/welcome#types) | The renewal price as a decimal number. |
| payload.expirationDate | [Date](/docs/rest-api/reference/welcome#types) | The new expiration date of the domain. |
| payload.renewedAt | [Date](/docs/rest-api/reference/welcome#types) | The timestamp when the domain was renewed. |

### [domain.renewal-failed](#domain.renewal-failed)

Occurs whenever a domain renewal fails.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain for which renewal failed. |
| payload.errorReason | [String](/docs/rest-api/reference/welcome#types) | The reason why the renewal failed. |
| payload.failedAt | [Date](/docs/rest-api/reference/welcome#types) | The timestamp when the renewal failed. |

### [domain.transfer-in-completed](#domain.transfer-in-completed)

Occurs whenever a domain transfer into Vercel is completed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that was transferred. |

### [domain.transfer-in-failed](#domain.transfer-in-failed)

Occurs whenever a domain transfer into Vercel fails.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain for which the transfer failed. |

### [domain.transfer-in-started](#domain.transfer-in-started)

Occurs whenever a domain transfer into Vercel is initiated.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain for which the transfer was started. |

### [project.domain-created](#project.domain-created)

Occurs whenever a domain is added to a project.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that was added to the project. |

### [project.domain-deleted](#project.domain-deleted)

Occurs whenever a domain is removed from a project.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that was removed from the project. |

### [project.domain-moved](#project.domain-moved)

Occurs whenever a domain is moved from one project to another.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that was moved. |
| payload.from.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project the domain was moved from. |
| payload.to.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project the domain was moved to. |
| payload.isRedirect | [Boolean](/docs/rest-api/reference/welcome#types) | Whether the move created a redirect. |

### [project.domain-unverified](#project.domain-unverified)

Occurs whenever a project domain becomes unverified.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that became unverified. |

### [project.domain-updated](#project.domain-updated)

Occurs whenever a project domain is updated.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.previous.domain | [String](/docs/rest-api/reference/welcome#types) | The previous domain name. |
| payload.previous.redirect | [String](/docs/rest-api/reference/welcome#types) | The previous redirect URL (possibly null). |
| payload.previous.redirectStatusCode | [Number](/docs/rest-api/reference/welcome#types) | The previous redirect status code (possibly null). |
| payload.previous.gitBranch | [String](/docs/rest-api/reference/welcome#types) | The previous git branch (possibly null). |
| payload.next.domain | [String](/docs/rest-api/reference/welcome#types) | The new domain name. |
| payload.next.redirect | [String](/docs/rest-api/reference/welcome#types) | The new redirect URL (possibly null). |
| payload.next.redirectStatusCode | [Number](/docs/rest-api/reference/welcome#types) | The new redirect status code (possibly null). |
| payload.next.gitBranch | [String](/docs/rest-api/reference/welcome#types) | The new git branch (possibly null). |

### [project.domain-verified](#project.domain-verified)

Occurs whenever a project domain is verified.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The name of the domain that was verified. |

### [integration-configuration.permission-upgraded](#integration-configuration.permission-upgraded)

Occurs whenever the user changes the project permission for an integration.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the configuration. |
| payload.configuration.projectSelection | [String](/docs/rest-api/reference/welcome#types) | A String representing the permission for projects. Possible values are `all` or `selected`. |
| payload.configuration.projects | [List](/docs/rest-api/reference/welcome#types) | An array of project IDs. |
| payload.projects.added | [List](/docs/rest-api/reference/welcome#types) | An array of added project IDs. |
| payload.projects.removed | [List](/docs/rest-api/reference/welcome#types) | An array of removed project IDs. |

### [integration-configuration.removed](#integration-configuration.removed)

Occurs whenever an integration has been removed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the configuration. |
| payload.configuration.projectSelection | [String](/docs/rest-api/reference/welcome#types) | A String representing the permission for projects. Possible values are `all` or `selected`. |
| payload.configuration.projects | [List](/docs/rest-api/reference/welcome#types) | An array of project IDs. |

### [integration-configuration.scope-change-confirmed](#integration-configuration.scope-change-confirmed)

Occurs whenever the user confirms pending scope changes.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the configuration. |
| payload.configuration.scopes | [List](/docs/rest-api/reference/welcome#types) | List of all scopes (after confirmation). |

### [integration-resource.project-connected](#integration-resource.project-connected)

Occurs whenever the user connects the integration resource to a project.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.resourceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the resource. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | The name of the project. |
| payload.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project (same as project.id). |
| payload.targets | [List](/docs/rest-api/reference/welcome#types) | The list of the deployment targets. |

### [integration-resource.project-disconnected](#integration-resource.project-disconnected)

Occurs whenever the user disconnects the integration resource to a project.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.resourceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the resource. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project (same as project.id). |
| payload.targets | [List](/docs/rest-api/reference/welcome#types) | The list of the deployment targets. |

### [marketplace.invoice.created](#marketplace.invoice.created)

Occurs when an invoice was created and sent to the customer.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.invoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice. |
| payload.externalInvoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice, provided by integrator. Possibly `null`. |
| payload.period.start | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period start date. |
| payload.period.end | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period end date. |
| payload.invoiceDate | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's date. |
| payload.invoiceTotal | [String](/docs/rest-api/reference/welcome#types) | The invoice's total as a decimal number. |

### [marketplace.invoice.notpaid](#marketplace.invoice.notpaid)

Occurs when an invoice was not paid after a grace period.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.invoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice. |
| payload.externalInvoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice, provided by integrator. Possibly `null`. |
| payload.period.start | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period start date. |
| payload.period.end | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period end date. |
| payload.invoiceDate | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's date. |
| payload.invoiceTotal | [String](/docs/rest-api/reference/welcome#types) | The invoice's total as a decimal number. |

### [marketplace.invoice.paid](#marketplace.invoice.paid)

Occurs when an invoice was paid.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.invoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice. |
| payload.externalInvoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice, provided by integrator. Possibly `null`. |
| payload.period.start | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period start date. |
| payload.period.end | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period end date. |
| payload.invoiceDate | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's date. |
| payload.invoiceTotal | [String](/docs/rest-api/reference/welcome#types) | The invoice's total as a decimal number. |

### [marketplace.invoice.refunded](#marketplace.invoice.refunded)

Occurs when an invoice is refunded.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.invoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice. |
| payload.externalInvoiceId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the Marketplace invoice, provided by integrator. Possibly `null`. |
| payload.period.start | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period start date. |
| payload.period.end | [IsoDate](/docs/rest-api/reference/welcome#types) | The invoice's period end date. |
| payload.amount | [String](/docs/rest-api/reference/welcome#types) | The amount being refunded as a decimal number. |
| payload.reason | [String](/docs/rest-api/reference/welcome#types) | The reason for why the refund has been issued. |

### [marketplace.member.changed](#marketplace.member.changed)

Occurs whenever a member is added, removed, or their role changed for an installation.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation. |
| payload.installationId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the integration installation (same as `configuration.id`). |
| payload.memberId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the member. |
| payload.role | [String](/docs/rest-api/reference/welcome#types) | The member's role: "ADMIN", "USER" or "NONE". "NONE" indicates the member has been removed. |

### [observability.usage-anomaly](#observability.usage-anomaly)

Occurs whenever your project's usage exceeds a dynamic threshold.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.teamId | [String](/docs/rest-api/reference/welcome#types) | The ID of the team. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.startedAt | [Number](/docs/rest-api/reference/welcome#types) | Timestamp when the anomaly started (milliseconds since epoch). |
| payload.links.observability | [String](/docs/rest-api/reference/welcome#types) | URL to the observability dashboard for this alert. |
| payload.projectSlug | [String](/docs/rest-api/reference/welcome#types) | The project slug. |
| payload.teamSlug | [String](/docs/rest-api/reference/welcome#types) | The team slug. |
| payload.groupId | [String](/docs/rest-api/reference/welcome#types) | Optional group identifier for related alerts. |
| payload.alerts\[\].startedAt | [String](/docs/rest-api/reference/welcome#types) | ISO 8601 timestamp when this specific alert started. |
| payload.alerts\[\].title | [String](/docs/rest-api/reference/welcome#types) | Human-readable title for the alert. |
| payload.alerts\[\].unit | [String](/docs/rest-api/reference/welcome#types) | Unit of measurement (e.g., `requests`). |
| payload.alerts\[\].formattedValues | [Object](/docs/rest-api/reference/welcome#types) | Formatted values for display purposes. |
| payload.alerts\[\].count | [Number](/docs/rest-api/reference/welcome#types) | Total count of events during the anomaly period. |
| payload.alerts\[\].average | [Number](/docs/rest-api/reference/welcome#types) | Average value during the anomaly period. |
| payload.alerts\[\].stddev | [Number](/docs/rest-api/reference/welcome#types) | Standard deviation of the metric. |
| payload.alerts\[\].zscore | [Number](/docs/rest-api/reference/welcome#types) | Z-score indicating how many standard deviations from the mean. |
| payload.alerts\[\].zscoreThreshold | [Number](/docs/rest-api/reference/welcome#types) | Z-score threshold that triggered the alert. |
| payload.alerts\[\].alertId | [String](/docs/rest-api/reference/welcome#types) | Unique identifier for this alert. |
| payload.alerts\[\].type | [String](/docs/rest-api/reference/welcome#types) | Alert type, always `usage_anomaly` for this event. |
| payload.alerts\[\].metric | [String](/docs/rest-api/reference/welcome#types) | Metric identifier, for example, `edge_requests`. |

See the [Alerts documentation](/docs/alerts) for more details and examples.

### [observability.error-anomaly](#observability.error-anomaly)

Occurs whenever your project's error rate (5xx) exceeds a dynamic threshold.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.teamId | [String](/docs/rest-api/reference/welcome#types) | The ID of the team. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.startedAt | [Number](/docs/rest-api/reference/welcome#types) | Timestamp when the anomaly started (milliseconds since epoch). |
| payload.links.observability | [String](/docs/rest-api/reference/welcome#types) | URL to the observability dashboard for this alert. |
| payload.projectSlug | [String](/docs/rest-api/reference/welcome#types) | The project slug. |
| payload.teamSlug | [String](/docs/rest-api/reference/welcome#types) | The team slug. |
| payload.groupId | [String](/docs/rest-api/reference/welcome#types) | Optional group identifier for related alerts. |
| payload.alerts\[\].startedAt | [String](/docs/rest-api/reference/welcome#types) | ISO 8601 timestamp when this specific alert started. |
| payload.alerts\[\].title | [String](/docs/rest-api/reference/welcome#types) | Human-readable title for the alert. |
| payload.alerts\[\].unit | [String](/docs/rest-api/reference/welcome#types) | Unit of measurement (e.g., `errors`). |
| payload.alerts\[\].formattedValues | [Object](/docs/rest-api/reference/welcome#types) | Formatted values for display purposes. |
| payload.alerts\[\].count | [Number](/docs/rest-api/reference/welcome#types) | Total count of errors during the anomaly period. |
| payload.alerts\[\].average | [Number](/docs/rest-api/reference/welcome#types) | Average error rate during the anomaly period. |
| payload.alerts\[\].stddev | [Number](/docs/rest-api/reference/welcome#types) | Standard deviation of the metric. |
| payload.alerts\[\].zscore | [Number](/docs/rest-api/reference/welcome#types) | Z-score indicating how many standard deviations from the mean. |
| payload.alerts\[\].zscoreThreshold | [Number](/docs/rest-api/reference/welcome#types) | Z-score threshold that triggered the alert. |
| payload.alerts\[\].alertId | [String](/docs/rest-api/reference/welcome#types) | Unique identifier for this alert. |
| payload.alerts\[\].type | [String](/docs/rest-api/reference/welcome#types) | Alert type, always `error_anomaly` for this event. |
| payload.alerts\[\].route | [String](/docs/rest-api/reference/welcome#types) | Route pattern or path where the errors were observed. |
| payload.alerts\[\].statusGroup | [String](/docs/rest-api/reference/welcome#types) | Status code group, always `5xx` for error anomalies. |
| payload.alerts\[\].cause | [String](/docs/rest-api/reference/welcome#types) | The failing runtime, either `function` or `middleware`. |
| payload.alerts\[\].errorCode | [String](/docs/rest-api/reference/welcome#types) | Optional error code if available (e.g., `FUNCTION_INVOCATION_ERROR`). |

See the [Alerts documentation](/docs/alerts) for more details and examples.

### [project.created](#project.created)

Occurs whenever a project has been created.

This event is sent only when the Integration has access to all projects in a Vercel scope.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |

### [project.removed](#project.removed)

Occurs whenever a project has been removed.

This event is sent only when the integration has access to all projects in a Vercel scope.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |

### [project.rolling-release.approved](#project.rolling-release.approved)

Occurs whenever a rolling release stage is approved and progresses to the next stage.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |
| payload.rollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The current rolling release configuration. |
| payload.rollingRelease.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.rollingRelease.ownerId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the team or user that owns the rolling release. |
| payload.rollingRelease.deploymentIds | [List](/docs/rest-api/reference/welcome#types) | Array of deployment IDs involved in the rolling release. |
| payload.rollingRelease.state | [String](/docs/rest-api/reference/welcome#types) | The current state of the rolling release. Possible values are `ACTIVE`, `COMPLETE`, `ABORTED`. |
| payload.rollingRelease.activeStageIndex | [Number](/docs/rest-api/reference/welcome#types) | The index of the currently active stage. |
| payload.rollingRelease.default | [Object](/docs/rest-api/reference/welcome#types) | The default deployment configuration. |
| payload.rollingRelease.default.baseDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the base deployment. |
| payload.rollingRelease.default.targetDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the target deployment. |
| payload.rollingRelease.default.targetPercentage | [Number](/docs/rest-api/reference/welcome#types) | The target percentage of traffic to route to the target deployment. |
| payload.rollingRelease.default.targetStartAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the target deployment started. |
| payload.rollingRelease.default.targetUpdatedAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the target deployment was last updated. |
| payload.rollingRelease.config | [Object](/docs/rest-api/reference/welcome#types) | The rolling release configuration. |
| payload.rollingRelease.config.target | [String](/docs/rest-api/reference/welcome#types) | The target environment for the rolling release. |
| payload.rollingRelease.config.stages | [List](/docs/rest-api/reference/welcome#types) | Array of stage configurations. |
| payload.rollingRelease.writtenBy | [String](/docs/rest-api/reference/welcome#types) | The source that triggered the rolling release update. |
| payload.prevRollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The previous rolling release configuration before the approval. |

### [project.rolling-release.completed](#project.rolling-release.completed)

Occurs whenever a rolling release is completed successfully.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |
| payload.rollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The completed rolling release configuration. |
| payload.rollingRelease.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.rollingRelease.ownerId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the team or user that owns the rolling release. |
| payload.rollingRelease.deploymentIds | [List](/docs/rest-api/reference/welcome#types) | Array of deployment IDs involved in the rolling release. |
| payload.rollingRelease.state | [String](/docs/rest-api/reference/welcome#types) | The state of the rolling release (will be `COMPLETE`). |
| payload.rollingRelease.activeStageIndex | [Number](/docs/rest-api/reference/welcome#types) | The index of the final stage. |
| payload.rollingRelease.default | [Object](/docs/rest-api/reference/welcome#types) | The final deployment configuration. |
| payload.rollingRelease.default.baseDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the base deployment. |
| payload.rollingRelease.default.targetDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the target deployment. |
| payload.rollingRelease.default.targetPercentage | [Number](/docs/rest-api/reference/welcome#types) | The final target percentage (will be 100). |
| payload.rollingRelease.default.targetStartAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the target deployment started. |
| payload.rollingRelease.default.targetUpdatedAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the target deployment was last updated. |
| payload.rollingRelease.config | [Object](/docs/rest-api/reference/welcome#types) | The rolling release configuration. |
| payload.rollingRelease.config.target | [String](/docs/rest-api/reference/welcome#types) | The target environment for the rolling release. |
| payload.rollingRelease.config.stages | [List](/docs/rest-api/reference/welcome#types) | Array of stage configurations. |
| payload.rollingRelease.writtenBy | [String](/docs/rest-api/reference/welcome#types) | The source that completed the rolling release. |
| payload.prevRollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The previous rolling release configuration before completion. |

### [project.rolling-release.aborted](#project.rolling-release.aborted)

Occurs whenever a rolling release is aborted.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |
| payload.rollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The aborted rolling release configuration. |
| payload.rollingRelease.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.rollingRelease.ownerId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the team or user that owns the rolling release. |
| payload.rollingRelease.deploymentIds | [List](/docs/rest-api/reference/welcome#types) | Array of deployment IDs involved in the rolling release. |
| payload.rollingRelease.state | [String](/docs/rest-api/reference/welcome#types) | The state of the rolling release (will be `ABORTED`). |
| payload.rollingRelease.activeStageIndex | [Number](/docs/rest-api/reference/welcome#types) | The index of the stage when aborted. |
| payload.rollingRelease.default | [Object](/docs/rest-api/reference/welcome#types) | The deployment configuration at the time of abortion. |
| payload.rollingRelease.default.baseDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the base deployment. |
| payload.rollingRelease.default.targetDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the target deployment. |
| payload.rollingRelease.default.targetStartAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the target deployment started. |
| payload.rollingRelease.default.targetUpdatedAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the rolling release was aborted. |
| payload.rollingRelease.config | [Object](/docs/rest-api/reference/welcome#types) | The rolling release configuration. |
| payload.rollingRelease.config.target | [String](/docs/rest-api/reference/welcome#types) | The target environment for the rolling release. |
| payload.rollingRelease.config.stages | [List](/docs/rest-api/reference/welcome#types) | Array of stage configurations. |
| payload.rollingRelease.writtenBy | [String](/docs/rest-api/reference/welcome#types) | The source that aborted the rolling release. |
| payload.prevRollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The previous rolling release configuration before abortion. |

### [project.rolling-release.started](#project.rolling-release.started)

Occurs whenever a rolling release is started.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.team.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| payload.user.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's user. |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |
| payload.rollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The started rolling release configuration. |
| payload.rollingRelease.projectId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.rollingRelease.ownerId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the team or user that owns the rolling release. |
| payload.rollingRelease.deploymentIds | [List](/docs/rest-api/reference/welcome#types) | Array of deployment IDs involved in the rolling release. |
| payload.rollingRelease.state | [String](/docs/rest-api/reference/welcome#types) | The state of the rolling release (will be `ACTIVE`). |
| payload.rollingRelease.activeStageIndex | [Number](/docs/rest-api/reference/welcome#types) | The index of the initial stage (usually 0). |
| payload.rollingRelease.default | [Object](/docs/rest-api/reference/welcome#types) | The initial deployment configuration. |
| payload.rollingRelease.default.baseDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the base deployment. |
| payload.rollingRelease.default.targetDeploymentId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the target deployment. |
| payload.rollingRelease.default.targetPercentage | [Number](/docs/rest-api/reference/welcome#types) | The initial target percentage for the first stage. |
| payload.rollingRelease.default.targetStartAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the rolling release started. |
| payload.rollingRelease.default.targetUpdatedAt | [Number](/docs/rest-api/reference/welcome#types) | The timestamp when the rolling release was last updated. |
| payload.rollingRelease.config | [Object](/docs/rest-api/reference/welcome#types) | The rolling release configuration. |
| payload.rollingRelease.config.target | [String](/docs/rest-api/reference/welcome#types) | The target environment for the rolling release. |
| payload.rollingRelease.config.stages | [List](/docs/rest-api/reference/welcome#types) | Array of stage configurations. |
| payload.rollingRelease.writtenBy | [String](/docs/rest-api/reference/welcome#types) | The source that started the rolling release. |
| payload.prevRollingRelease | [Object](/docs/rest-api/reference/welcome#types) | The previous rolling release configuration (if any) before starting the new one. |

## [Legacy Payload](#legacy-payload)

The legacy webhook payload is a JSON object with the following keys.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| type | [String](/docs/rest-api/reference/welcome#types) | The [legacy event type](#legacy-event-types). |
| id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the webhook delivery. |
| createdAt | [Number](/docs/rest-api/reference/welcome#types) | The webhook delivery timestamp. |
| region | [String](/docs/rest-api/reference/welcome#types) | The region the event occurred in (possibly null). |
| clientId | [ID](/docs/rest-api/reference/welcome#types) | The ID of integration's client. |
| ownerId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event owner (user or team). |
| teamId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's team (possibly null). |
| userId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the event's users. |
| webhookId | [ID](/docs/rest-api/reference/welcome#types) | The ID of the webhook. |
| payload | [Object](/docs/rest-api/reference/welcome#types) | The payload of the webhook. See [Legacy Event Types](#legacy-event-types) for more information. |

## [Legacy Event Types](#legacy-event-types)

The following event types have been deprecated and webhooks that listen for them can no longer be created. Vercel will continue to deliver the deprecated events to existing webhooks.

### [deployment](#deployment)

This event is replaced by [deployment.created](#deployment.created).

Occurs whenever a deployment is created.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.alias | [List](/docs/rest-api/reference/welcome#types) | An array of aliases that will get assigned when the deployment is ready. |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment-ready](#deployment-ready)

This event is replaced by [deployment.succeeded](#deployment.succeeded).

Occurs whenever a deployment is ready.

This event gets fired after all blocking checks have passed. See [`deployment-prepared`](/docs/integrations#webhooks/events-types/deployment-prepared) if you registered Checks.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment-prepared](#deployment-prepared)

This event is replaced by [deployment.ready](#deployment.ready).

Occurs whenever a deployment is successfully built and your integration has registered at least one [check](/docs/integrations/checks-overview).

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment-canceled](#deployment-canceled)

This event is replaced by [deployment.canceled](#deployment.canceled).

Occurs whenever a deployment is canceled.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment-error](#deployment-error)

This event is replaced by [deployment.error](#deployment.error).

Occurs whenever a deployment has failed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.deployment.meta | [Map](/docs/rest-api/reference/welcome#types) | A Map of deployment metadata. |
| payload.deployment.url | [String](/docs/rest-api/reference/welcome#types) | The URL of the deployment. |
| payload.deployment.name | [String](/docs/rest-api/reference/welcome#types) | The project name used in the deployment URL. |
| payload.links.deployment | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to inspect the deployment. |
| payload.links.project | [String](/docs/rest-api/reference/welcome#types) | The URL on the Vercel Dashboard to the project. |
| payload.target | [String](/docs/rest-api/reference/welcome#types) | A String that indicates the target. Possible values are `production`, `staging` or `null`. |
| payload.projectId | [String](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.plan | [String](/docs/rest-api/reference/welcome#types) | The plan type of the deployment. |
| payload.regions | [List](/docs/rest-api/reference/welcome#types) | An array of the supported regions for the deployment. |

### [deployment-check-rerequested](#deployment-check-rerequested)

This event is replaced by [deployment.check-rerequested](#deployment.check-rerequested).

Occurs when a user has requested for a [check](/docs/integrations/checks-overview) to be rerun after it failed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.check.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the check. |

### [deployment-checks-completed](#deployment-checks-completed)

This event has been removed. [deployment.succeeded](#deployment.succeeded) can be used for the same purpose.

Occurs when all checks for a deployment have completed. This does not indicate that they have all passed, only that they are no longer running. It is possible for webhook to occur multiple times for a single deployment if any checks are [re-requested](/docs/observability/checks-overview/creating-checks#rerunning-checks).

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.deployment.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the deployment. |
| payload.checks | [List](/docs/rest-api/reference/welcome#types) | Information about the Checks. |

Each item in `checks` has the following properties:

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.id | [ID](/docs/rest-api/reference/welcome#types) | The unique identifier of the check. Always prepended with `check_`. |
| payload.name | [String](/docs/rest-api/reference/welcome#types) | The name of the check. |
| payload.status | [String](/docs/rest-api/reference/welcome#types) | The status of the check. One of `registered`, `running` or `completed` |
| payload.conclusion | [String](/docs/rest-api/reference/welcome#types) | The conclusion of the check. One of `cancelled`, `failed`, `neutral`, `succeeded` or `skipped`. |
| payload.blocking | [Boolean](/docs/rest-api/reference/welcome#types) | Whether a deployment should be blocked or not. |
| payload.integrationId | [String](/docs/rest-api/reference/welcome#types) | The unique identifier of the integration. |

### [project-created](#project-created)

This event is replaced by [project.created](#project.created).

Occurs whenever a project has been created.

This event is sent only when the Integration has access to all projects in a Vercel scope.

  

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |

### [project-removed](#project-removed)

This event is replaced by [project.removed](#project.removed).

Occurs whenever a Project has been removed.

This event is sent only when the Integration has access to all Projects in a Vercel scope.

  

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.project.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the project. |
| payload.project.name | [String](/docs/rest-api/reference/welcome#types) | Name of the project. |

### [integration-configuration-removed](#integration-configuration-removed)

This event is replaced by [integration-configuration.removed](#integration-configuration.removed).

Occurs whenever an integration has been removed.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the configuration. |
| payload.configuration.projects | [List](/docs/rest-api/reference/welcome#types) | An array of project IDs. |

### [integration-configuration-permission-updated](#integration-configuration-permission-updated)

This event is replaced by [integration-configuration.permission-upgraded](#integration-configuration.permission-upgraded) .

Occurs whenever the user changes the project permission for an integration.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the configuration. |
| payload.configuration.projectSelection | [String](/docs/rest-api/reference/welcome#types) | A String representing the permission for projects. Possible values are `all` or `selected`. |
| payload.configuration.projects | [List](/docs/rest-api/reference/welcome#types) | An array of project IDs. |
| payload.projects.added | [List](/docs/rest-api/reference/welcome#types) | An array of added project IDs. |
| payload.projects.removed | [List](/docs/rest-api/reference/welcome#types) | An array of removed project IDs. |

### [integration-configuration-scope-change-confirmed](#integration-configuration-scope-change-confirmed)

This event is replaced by [integration-configuration.scope-change-confirmed](#integration-configuration.scope-change-confirmed) .

Occurs whenever the user confirms pending scope changes.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.configuration.id | [ID](/docs/rest-api/reference/welcome#types) | The ID of the configuration. |
| payload.configuration.scopes | [List](/docs/rest-api/reference/welcome#types) | List of all scopes (after confirmation). |

### [domain-created](#domain-created)

This event is replaced by [domain.created](#domain.created).

Occurs whenever a domain has been created.

| Key | [Type](/docs/rest-api/reference/welcome#types) | Description |
| --- | --- | --- |
| payload.domain.name | [String](/docs/rest-api/reference/welcome#types) | The Domain name created. |
| payload.domain.delegated | [String](/docs/rest-api/reference/welcome#types) | Whether or not the domain was delegated/shared. |

## [Securing webhooks](#securing-webhooks)

Once your server is configured to receive payloads, it will listen for any payload sent to the endpoint you configured. By knowing the URL of your webhook, anybody can send you requests. Therefore, it is recommended to check whether the requests are coming from Vercel or not.

The recommended method to check is to use the [`x-vercel-signature`](/docs/headers/request-headers#x-vercel-signature) security header you receive with each request. The value of this header corresponds to the `sha1` of the request body using your [client secret](/docs/webhooks#enter-your-endpoint-url).

For example, you can validate a webhook request as follows:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/webhook-validator-example/route.ts

TypeScript

TypeScriptJavaScript

```
import crypto from 'crypto';
 
export async function GET(request: Request) {
  const { INTEGRATION_SECRET } = process.env;
 
  if (typeof INTEGRATION_SECRET != 'string') {
    throw new Error('No integration secret found');
  }
 
  const rawBody = await request.text();
  const rawBodyBuffer = Buffer.from(rawBody, 'utf-8');
  const bodySignature = sha1(rawBodyBuffer, INTEGRATION_SECRET);
 
  if (bodySignature !== request.headers.get('x-vercel-signature')) {
    return Response.json({
      code: 'invalid_signature',
      error: "signature didn't match",
    });
  }
 
  const json = JSON.parse(rawBodyBuffer.toString('utf-8'));
 
  switch (json.type) {
    case 'project.created':
    // ...
  }
 
  return new Response('Webhook request validated', {
    status: 200,
  });
}
 
function sha1(data: Buffer, secret: string): string {
  return crypto.createHmac('sha1', secret).update(data).digest('hex');
}
```

Example on how to validate a webhook message.

You can compute the signature using an HMAC hexdigest from the secret token of OAuth2 and request body, then compare it with the value of the [`x-vercel-signature`](/docs/headers/request-headers#x-vercel-signature) header to validate the payload.

## [HTTP Response](#http-response)

You should consider this HTTP request to be an event. Once you receive the request, you should schedule a task for your action.

This request has a timeout of 30 seconds. That means if a `2XX` HTTP response is not received within 30 seconds, the request will be aborted.

## [Delivery Attempts and Retries](#delivery-attempts-and-retries)

If your HTTP endpoint does not respond with a `2XX` HTTP status code, we attempt to deliver the webhook event up to 24 hours with an exponential backoff. Events that could not be delivered within 24 hours will not be retried and will be discarded.

--------------------------------------------------------------------------------
title: "Vercel Workflow"
description: "Build durable, reliable, and observable applications and AI agents with the Workflow Development Kit (WDK)."
last_updated: "null"
source: "https://vercel.com/docs/workflow"
--------------------------------------------------------------------------------

# Vercel Workflow

Copy page

Ask AI about this page

Last updated October 30, 2025

Vercel Workflow is available in [Beta](/docs/release-phases#beta) on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Vercel Workflow is a fully managed platform built on top of the open-source [Workflow Development Kit (WDK)](https://useworkflow.dev), a TypeScript framework for building apps and AI agents that can pause, resume, and maintain state.

With Workflow, Vercel manages the infrastructure for you so you can focus on writing business logic. Vercel Functions execute your workflow and step code, [Vercel Queues](https://vercel.com/changelog/vercel-queues-is-now-in-limited-beta) enqueue and execute those routes with reliability, and managed persistence stores all state and event logs in an optimized database.

This means your functions are:

*   Resumable: Pause for minutes or months, then resume from the exact point.
*   Durable: Survive deployments and crashes with deterministic replays.
*   Observable: Use built-in logs, metrics, and tracing and view them in your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fai%2Fworkflows&title=Vercel+Workflow).
*   Idiomatic: Write async/await JavaScript with two directives. No YAML or state machines.

![Workflow diagram.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow%2Fworkflow-diagram-light.avif&w=1920&q=75)![Workflow diagram.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow%2Fworkflow-diagram-dark.avif&w=1920&q=75)

Workflow diagram.

## [Getting started](#getting-started)

Install the WDK package:

pnpmyarnnpmbun

```
pnpm i workflow
```

Start writing your own workflows by following the [Workflow DevKit getting started guide](https://useworkflow.dev/docs/getting-started).

## [Concepts](#concepts)

Workflow introduces two directives that turn ordinary async functions into durable workflows. You write async/await code as usual, and the framework handles queues, retry logic, and state persistence automatically.

### [Workflow](#workflow)

A workflow is a stateful function that coordinates multi-step logic over time. The `'use workflow'` directive marks a function as durable, which means it remembers its progress and can resume exactly where it left off, even after pausing, restarting, or deploying new code.

Use a workflow when your logic needs to pause, resume, or span minutes to months:

app/workflows/ai-content-workflow.ts

```
export async function aiContentWorkflow(topic: string) {
  'use workflow';
 
  const draft = await generateDraft(topic);
 
  const summary = await summarizeDraft(draft);
 
  return { draft, summary };
}
```

Under the hood, the workflow function compiles into a route that orchestrates execution. All inputs and outputs are recorded in an event log. If a deploy or crash happens, the system replays execution deterministically from where it stopped.

### [Step](#step)

A step is a stateless function that runs a unit of durable work inside a workflow. The `'use step'` directive marks a function as a step, which gives it built-in retries and makes it survive failures like network errors or process crashes.

Use a step when calling external APIs or performing isolated operations:

app/steps/generate-draft.ts

```
async function generateDraft(topic: string) {
  'use step';
 
  const draft = await aiGenerate({
    prompt: `Write a blog post about ${topic}`,
  });
 
  return draft;
}
 
async function summarizeDraft(draft: string) {
  'use step';
 
  const summary = await aiSummarize({ text: draft });
 
  if (Math.random() < 0.3) {
    throw new Error('Transient AI provider error');
  }
 
  return summary;
}
```

Each step compiles into an isolated API route. While the step executes, the workflow suspends without consuming resources. When the step completes, the workflow resumes automatically right where it left off.

### [Sleep](#sleep)

Sleep pauses a workflow for a specified duration without consuming compute resources. This is useful when you need to wait for hours or days before continuing, like delaying a follow-up email or waiting to issue a reward.

Use sleep to delay execution without keeping any infrastructure running:

app/workflows/ai-refine.ts

```
import { sleep } from 'workflow';
 
export async function aiRefineWorkflow(draftId: string) {
  'use workflow';
 
  const draft = await fetchDraft(draftId);
 
  await sleep('7 days'); // Wait 7 days to gather more signals; no resources consumed
 
  const refined = await refineDraft(draft);
 
  return { draftId, refined };
}
```

During sleep, no resources are consumed. The workflow simply pauses and resumes when the time expires.

### [Hook](#hook)

A hook lets a workflow wait for external events such as user actions, webhooks, or third-party API responses. This is useful for human-in-the-loop workflows where you need to pause until someone approves, confirms, or provides input.

Use hooks to pause execution until external data arrives:

app/workflows/approval.ts

```
import { defineHook } from 'workflow';
 
// Human approval for AI-generated drafts
const approvalHook = defineHook<{
  decision: 'approved' | 'changes';
  notes?: string;
}>();
 
export async function aiApprovalWorkflow(topic: string) {
  'use workflow';
 
  const draft = await generateDraft(topic);
 
  // Wait for human approval events
  const events = approvalHook.create({
    token: 'draft-123',
  });
 
  for await (const event of events) {
    if (event.decision === 'approved') {
      await publishDraft(draft);
      break;
    } else {
      const revised = await refineDraft(draft, event.notes);
      await publishDraft(revised);
      break;
    }
  }
}
```

app/api/resume/route.ts

```
// Resume the workflow when an approval is received
export async function POST(req: Request) {
  const data = await req.json();
 
  await approvalHook.resume('draft-123', {
    decision: data.decision,
    notes: data.notes,
  });
 
  return new Response('OK');
}
```

When a hook receives data, the workflow resumes automatically. No polling, message queues, or manual state management required.

## [Observability](#observability)

Every step, input, output, sleep, and error inside a workflow is recorded automatically.

You can track runs in real time, trace failures, and analyze performance without writing extra code.

To inspect your runs, go to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fai%2Fworkflows&title=Vercel+Workflow) , select your project and navigate to AI, then Workflows.

## [Pricing](#pricing)

Workflow pricing is divided into two resources:

*   Workflow Steps: Individual units of durable work executed inside a workflow.
*   Workflow Storage: The amount of data stored in the managed persistence layer for workflow state.

During the Beta period, Workflow observability is free for all plans. Workflow Steps and Workflow Storage remain priced. Advance notice will be given before any charges begin when Workflow goes to General Availability (GA).

All resources are billed based on usage with each plan having an [included allotment](/docs/pricing).

The pricing for each resource is based on the region from which requests to your site come. Use the dropdown to select your preferred region and see the pricing for each resource.

Select a Region

Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dubai, UAE (dxb1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, UK (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)

Managed Infrastructure pricing
| 
Resource

 | 

Hobby Included

 | 

On-demand Rates

 |
| --- | --- | --- |
| 

[Workflow Storage](/docs/workflow#pricing)

 | 1 GB | $0.50 per 1 GB per month |
| 

[Workflow Steps](/docs/workflow#pricing)

 | 50,000 | $25.00 per 1,000,000 Steps |

Functions invoked by Workflows continue to be charged at the [existing compute rates](/docs/functions/usage-and-pricing). We encourage you to use [Fluid compute](/docs/fluid-compute) with Workflow.

## [More resources](#more-resources)

*   [Workflow Development Kit (WDK)](https://useworkflow.dev)
*   [Stateful Slack bots with Vercel Workflow Guide](/guides/stateful-slack-bots-with-vercel-workflow)
---

**Navigation:** [← Previous](./39-session-tracing.md) | [Index](./index.md) | Next →
