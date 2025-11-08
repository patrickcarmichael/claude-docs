**Navigation:** [← Previous](./16-são-paulo-brazil-gru1-pricing.md) | [Index](./index.md) | [Next →](./18-list-aliases.md)

---

# Monitoring Quickstart

Copy page

Ask AI about this page

Last updated September 15, 2025

Monitoring will be [sunset](/docs/query/monitoring#monitoring-sunset) for Pro plans at the end of your next billing cycle in November 2025. To continue using full query abilities, consider migrating to [Observability Query](/docs/observability/query), which is included with [Observability Plus](/docs/observability/observability-plus).

## [Prerequisites](#prerequisites)

*   Make sure you upgrade to [Pro](/docs/plans/pro) or [Enterprise](/docs/plans/enterprise) plan.
*   Pro and Enterprise teams should [Upgrade to Observability Plus](/docs/observability#enabling-observability-plus) to access Monitoring.

## [Create a new query](#create-a-new-query)

In the following guide you will learn how to view the most requested posts on your website.

1.  ### [Go to the dashboard](#go-to-the-dashboard)
    
    1.  Navigate to the Monitoring tab from your Vercel dashboard
    2.  Click the Create New Query button to open the query builder
    3.  Click the Edit Query button to configure your query with clauses
    
    ![Add clauses through query editor.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fedit-query-light.png&w=3840&q=75)![Add clauses through query editor.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fedit-query-dark.png&w=3840&q=75)
    
    Add clauses through query editor.
    
2.  ### [Add Visualize clause](#add-visualize-clause)
    
    The [Visualize](/docs/observability/monitoring/monitoring-reference#visualize%22) clause specifies which field in your query will be calculated. Set the Visualize clause to `requests` to monitor the most popular posts on your website.
    
    Click the Run Query button, and the [Monitoring chart](/docs/observability/monitoring#monitoring-chart) will display the total number of requests made.
    
    ![Configure Visualize clause to fetch requests.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-visualize-light.png&w=1920&q=75)![Configure Visualize clause to fetch requests.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-visualize-dark.png&w=1920&q=75)
    
    Configure Visualize clause to fetch requests.
    
3.  ### [Add Where clause](#add-where-clause)
    
    To filter the query data, use the [Where](/docs/observability/monitoring/monitoring-reference#where) clause and specify the conditions you want to match against. You can use a combination of [variables and operators](/docs/observability/monitoring/monitoring-reference#where) to fetch the most requested posts. Add the following query statement to the Where clause:
    
    ```
    host = 'my-site.com' and like(request_path, '/posts%')
    ```
    
    This query retrieves data with a host field of `my-site.com` and a `request_path` field that starts with /posts.
    
    The `%` character can be used as a wildcard to match any sequence of characters after `/posts`, allowing you to capture all `request_path` values that start with that substring.
    
    ![Configure Where clause to filter requests.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-where-light.png&w=1920&q=75)![Configure Where clause to filter requests.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-where-dark.png&w=1920&q=75)
    
    Configure Where clause to filter requests.
    
4.  ### [Add Group By clause](#add-group-by-clause)
    
    Define a criteria that groups the data based on the selected attributes. The grouping mechanism is supported through the [Group By](/docs/observability/monitoring/monitoring-reference#group-by) clause.
    
    Set the Group By clause to `request_path`.
    
    With Visualize, Where, and Group By fields set, the [Monitoring chart](/docs/observability/monitoring#monitoring-chart) now shows the sum of `requests` that are filtered based on the `request_path`.
    
    ![Configure Group By clause to segment events into groups.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-groupby-light.png&w=1920&q=75)![Configure Group By clause to segment events into groups.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-groupby-dark.png&w=1920&q=75)
    
    Configure Group By clause to segment events into groups.
    
5.  ### [Add Limit clause](#add-limit-clause)
    
    To control the number of results returned by the query, use the [Limit](/docs/observability/monitoring/monitoring-reference#limit) clause and specify the desired number of results. You can choose from a few options, such as 5, 10, 25, 50, or 100 query results. For this example, set the limit to 5 query results.
    
    ![Configure Group By clause to segment events into groups.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-limit-light.png&w=1920&q=75)![Configure Group By clause to segment events into groups.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fset-limit-dark.png&w=1920&q=75)
    
    Configure Group By clause to segment events into groups.
    
6.  ### [Save and Run Query](#save-and-run-query)
    
    Save your query and click the **Run Query** button to generate the final results. The Monitoring chart will display a comprehensive view of the top 5 most requested posts on your website.
    
    ![In-depth and full-scale monitoring for your five most requested posts.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Ftop-posts-eg-light.png&w=1920&q=75)![In-depth and full-scale monitoring for your five most requested posts.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Ftop-posts-eg-dark.png&w=1920&q=75)
    
    In-depth and full-scale monitoring for your five most requested posts.

--------------------------------------------------------------------------------
title: "Query Reference"
description: "This reference covers the dimensions and operators used to create a query."
last_updated: "null"
source: "https://vercel.com/docs/query/reference"
--------------------------------------------------------------------------------

# Query Reference

Copy page

Ask AI about this page

Last updated September 9, 2025

## [Metric](#metric)

The metric selects what query data is displayed. You can choose one field at a time, and the same metric can be applied to different event types. For instance, Function Wall Time can be selected for edge, serverless, or middleware functions, aggregating each field in various ways.

| Field Name | Description | Aggregations |
| --- | --- | --- |
| Edge Requests | The number of [Edge Requests](/docs/pricing/networking#edge-requests) | Count, Count per Second, Percentages |
| Duration | The time spent serving a request, as measured by Vercel's CDN | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Incoming Fast Data Transfer | The incoming amount of [Fast Data Transfer](/docs/pricing/networking#fast-data-transfer) used by the request. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Outgoing Fast Data Transfer | The outgoing amount of [Fast Data Transfer](/docs/pricing/networking#fast-data-transfer) used by the response. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Total Fast Data Transfer | The total amount of [Fast Data Transfer](/docs/pricing/networking#fast-data-transfer) used by the response. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Function Invocations | The number of [Function invocations](/docs/functions/usage-and-pricing#managing-function-invocations) | Count, Count per Second, Percentages |
| Function Duration | The amount of [Function duration](/docs/functions/usage-and-pricing#managing-function-duration), as measured in GB-hours. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Function CPU Time | The amount of CPU time a Vercel Function has spent responding to requests, as measured in milliseconds. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Incoming Fast Origin Transfer | The amount of [Fast Origin Transfer](/docs/pricing/networking#fast-origin-transfer) used by the request. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Outgoing Fast Origin Transfer | The amount of [Fast Origin Transfer](/docs/pricing/networking#fast-origin-transfer) used by the response. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Provisioned Memory | The amount of memory provisioned to a Vercel Function. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Peak Memory | The maximum amount of memory used by Vercel Function at any point in time. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Requests Blocked | All requests blocked by either the system or user. | Count, Count per Second, Percentages |
| ISR Read Units | The amount of [Read Units](/docs/pricing/incremental-static-regeneration) used to access ISR data | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| ISR Write Units | The amount of [Write Units](/docs/pricing/incremental-static-regeneration) used to store new ISR data | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| ISR Read/Write | The amount of ISR operations | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Time to First Byte | The time between the request for a resource and when the first byte of a response begins to arrive. | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Function Wall Time | The duration that a Vercel Function has run | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Firewall Actions | The incoming web traffic observed by firewall rules. | Sum, Sum per Second, Unique, Percentages, |
| Optimizations | The number of image transformations | Sum, Sum per Second, Unique, Percentages, |
| Source Size | The source size of image optimizations | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Optimized Size | The optimized size of image optimizations | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Compression Ratio | The compression ratio of image optimizations | Sum, Sum per Second, Min/Max, Percentages, Percentiles |
| Size Change | The size change of image optimizations | Sum, Sum per Second, Min/Max, Percentages, Percentiles |

### [Aggregations](#aggregations)

Metrics can be aggregated in the following ways:

| Aggregation | Description |
| --- | --- |
| Count | The number of requests that occurred |
| Count per Second | The average rate of requests that occurred |
| Sum | The sum of the field value across all requests |
| Sum per Second | The sum of the field value as a rate per second |
| Minimum | The smallest observed field value |
| Maximum | The largest observed field value |
| Percentiles (75th, 90th, 95th, 99th) | Percentiles for the field values. For example, 90% of requests will have a duration that is less than the 90th percentile of duration. |
| Percentages | Each group is reported as a percentage of the ungrouped whole. For example, if a query for request groups by hosts, one host may have 10% of the total request count. Anything excluded by the `where` clause is not counted towards the ungrouped whole. |

Aggregations are calculated within each point on the chart (hourly, daily, etc) and also across the entire query window.

## [Filter](#filter)

The filter bar defines the conditions to filter your query data. It only fetches data that meets a specified condition based on several [fields](/docs/query/monitoring/monitoring-reference#group-by-and-where-fields) and operators:

| Operator | Description |  |
| --- | --- | --- |
| `is`, `is not` | The operator that allows you to specify a single value |  |
| `is any of` , `is not any of` | The operator that allows you to specify multiple values. For example, `host in ('vercel.com', 'nextjs.com')` |  |
| `startsWith` | Filter data values that begin with some specific characters |  |
| `endsWith` | Filter data values that end with specific characters |  |
| `>,>=,<,<=` | Numerical operators that allow numerical comparisons |  |

## [Group by](#group-by)

The `Group By` clause calculates statistics for each combination of [field](#group-by-and-where-fields) values. Each group is displayed as a separate color in the chart view, and has a separate row in the table view.

For example, grouping by `Request HostName` and `HTTP Status` will display data broken down by each combination of `Request Hostname` and `HTTP Status`.

## [Group by and where fields](#group-by-and-where-fields)

There are several fields available for use within the [Filter](#filter) and [group by](#group-by):

| Field Name | Description |  |
| --- | --- | --- |
| `Request Hostname` | Group by the request's domains and subdomains |  |
| `project` | Group by the request's project |  |
| `Deployment ID` | Group by the request's deployment ID |  |
| `HTTP Status` | Group by the request's HTTP response code |  |
| `route` | The mapped path used by the request. For example, if you have a dynamic route like `/blog/[slug]` and a blog post is `/blog/my-blog-post`, the `route` is `/blog/[slug]` |  |
| `Request Path` | The path used by the request. For example, if you have a dynamic route like `/blog/[slug]` and a blog post is `/blog/my-blog-post`, the `request_path` is `/blog/my-blog-post` |  |
| `Cache Result` | The [cache](/docs/edge-cache#x-vercel-cache) status for the request |  |
| `environment` | Group by the environment (`production` or [`preview`](/docs/deployments/environments#preview-environment-pre-production)) |  |
| `Request Method` | Group by the HTTP request method (`GET`, `POST`, `PUT`, etc.) |  |
| `Referrer URL` | Group by the HTTP referrer URL |  |
| `Referrer Hostname` | Group by the HTTP referrer domain |  |
| `Client IP` | Group by the request's IP address |  |
| `Client IP Country` | Group by the request's IP country |  |
| `Client User Agent` | Group by the request's user agent |  |
| `AS Number` | The autonomous system number (ASN) for the request. This is related to what network the request came from (either a home network or a cloud provider) |  |
| `CDN Region` | Group by the [region](/docs/regions) the request was routed to |  |
| `ISR Cache Region` | Group by the ISR cache region |  |
| `Cache Result` | Group by cache result |  |
| `WAF Action` | Group by the WAF action taken by the [Vercel Firewall](/docs/security/vercel-waf) (`deny`, `challenge`, `rate_limit`, `bypass` or `log`) |  |
| `WAF Rule ID` | Group by the firewall rule ID |  |
| `Skew Protection` | When `active`, the request would have been subject to [version skew](/docs/skew-protection) but was protected, otherwise `inactive`. |  |

--------------------------------------------------------------------------------
title: "Role-based access control (RBAC)"
description: "Learn how to manage team members on Vercel, and how to assign roles to each member with role-based access control (RBAC)."
last_updated: "null"
source: "https://vercel.com/docs/rbac"
--------------------------------------------------------------------------------

# Role-based access control (RBAC)

Copy page

Ask AI about this page

Last updated May 23, 2025

Team roles are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Teams consist of members, and each member of a team can get assigned a role. These roles define what you can and cannot do within a team on Vercel.

As your project scales and you add more team members, you can assign them roles to ensure that they have the right permissions to work on your projects.

Vercel offers a range of roles for your team members. When deciding what role a member should have on your team, consider the following:

*   What projects does this team member need to access?
*   What actions does this team member need to perform on these projects?
*   What actions does this team member need to perform on the team itself?

See the [Managing team members](/docs/rbac/managing-team-members) section for information on setting up and managing team members.

For specific information on the different access roles available on each plan, see the [Access Roles](/docs/rbac/access-roles) section.

## [More resources](#more-resources)

*   [Managing team members](/docs/rbac/managing-team-members)
*   [Access groups](/docs/rbac/access-groups)
*   [Access roles](/docs/rbac/access-roles)

--------------------------------------------------------------------------------
title: "Access Groups"
description: "Learn how to configure access groups for team members on a Vercel account."
last_updated: "null"
source: "https://vercel.com/docs/rbac/access-groups"
--------------------------------------------------------------------------------

# Access Groups

Copy page

Ask AI about this page

Last updated September 24, 2025

Access Groups are available on [Enterprise plans](/docs/plans/enterprise)

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

Access Groups provide a way to manage groups of Vercel users across projects on your team. They are a set of project role assignations, a combination of Vercel users and the projects they work on.

An Access Group consists of one or many projects in a team and assigns project roles to team members. Any team member included in an Access Group gets assigned the projects in that Access Group. They also get a default role.

Team administrators can apply automatic role assignments for default roles. And for more restricted projects, you can ensure only a subset of users have access to those projects. This gets handled with project-level role-based access control (RBAC).

![Example access group relationship diagram](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Faccess-groups-light.png%3Flightbox&w=3840&q=75)![Example access group relationship diagram](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Faccess-groups-dark.png%3Flightbox&w=3840&q=75)

Example access group relationship diagram

Zoom Image

![Example access group relationship diagram](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Faccess-groups-light.png%3Flightbox&w=3840&q=75)![Example access group relationship diagram](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Faccess-groups-dark.png%3Flightbox&w=3840&q=75)

Example access group relationship diagram

## [Create an Access Group](#create-an-access-group)

1.  Navigate to your team’s Settings tab and then Access Groups (`<team-name>/~/settings/access-groups`)
2.  Select Create Access Group
3.  Create a name for your Access Group
4.  Select the projects and [project roles](/docs/rbac/access-roles/project-level-roles) to assign
5.  Select the Members tab
6.  Add members with the Developer and Contributor role to the Access Group
7.  Create your Access Group by pressing Create

## [Edit projects of an Access Group](#edit-projects-of-an-access-group)

1.  Navigate to your team’s Settings tab and then Access Groups (`<team-name>/~/settings/access-groups`)
2.  Press the Edit Access Group button for the Access Group you wish to edit from your list of Access Groups
3.  Either:
    *   Remove a project using the remove button to the right of a project
    *   Add more projects using the Add more button below the project list and using the selection controls

## [Add and remove members from an Access Group](#add-and-remove-members-from-an-access-group)

1.  Navigate to your team’s Settings tab and then Access Groups (`<team-name>/~/settings/access-groups`)
2.  Press the Edit Access Group button for the Access Group you wish to edit from your list of Access Groups
3.  Select the Members tab
4.  Either:
    *   Remove an Access Group member using the remove button to the right of a member
    *   Add more members using the Add more button and the search controls

## [Modifying Access Groups for a single team member](#modifying-access-groups-for-a-single-team-member)

You can do this in two ways:

1.  From within your team's members page using the Manage Access button (recommended for convenience). Access this by navigating to your team's Settings tab and then Members
2.  By [editing each Access Group](#add-and-remove-members-from-an-access-group) using the Edit Access Group button and editing the Members list

## [Access Group behavior](#access-group-behavior)

When configuring Access Groups, there are some key things to be aware of:

*   Team roles cannot be overridden. An Access Group manages project roles only
*   Only a subset of team role and project role combinations are valid:
    *   [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role), [Billing](/docs/rbac/access-roles#billing-role), [Viewer Pro](/docs/rbac/access-roles#viewer-pro-role), [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role): All project role assignments are ignored
    *   [Developer](/docs/rbac/access-roles#developer-role): [Admin](/docs/rbac/access-roles#project-administrators) assignment is valid on selected projects. [Project Developer](/docs/rbac/access-roles#project-developer) and [Project Viewer](/docs/rbac/access-roles#project-viewer) role assignments are ignored
    *   [Contributor](/docs/rbac/access-roles#contributor-role): `Admin`, `Project Developer`, or `Project Viewer` roles are valid in selected projects
*   When a `Contributor` belongs to multiple access groups the computed role will be:
    *   `Admin` permissions in the project if any of the access groups they get assigned has a project mapping to `Admin`
    *   `Project Developer` permissions in the project if any of the access groups they get assigned has a project mapping to `Project Developer` and there is none to `Admin` for that project
    *   `Project Viewer` permissions in the project if any of the access groups they get assigned has a project mapping to `Project Viewer` and there is none to `Admin` and none to `Project Developer` for that project
*   When a `Developer` belongs to multiple access groups the role assignation will be:
    *   `Admin` permissions in the project if any of the access groups they get assigned has a project mapping to Admin
    *   In all other cases the member will have `Developer` permissions
*   Access Group assignations are not deleted when a team role gets changed. This allows a temporal increase of permissions without having to modify all Access Group assignations
*   Direct project assignations also affect member roles. Consider these examples:
    *   A direct project assignment assigns a member as `Admin`. That member is within an Access Group that assigns `Developer`. The computed role is `Admin`.
    *   A direct project assignment assigns a member as `Developer`. That member is within an Access Group that assigns `Admin`. The computed role is `Admin`.

Contributors and Developers can increase their level of permissions in a project but they can never reduce their level of permissions

## [Directory sync](#directory-sync)

If you use [Directory sync](/docs/security/directory-sync), you are able to map a Directory Group with an Access Group. This will grant all users that belong to the Directory Group access to the projects that get assigned in the Access Group.

Some things to note:

*   The final role the user will have in a specific project will depend on the mappings of all Access Groups the user belongs to
*   Assignations using directory sync can lead to `Owners`, `Members` `Billing` and `Viewers` being part of an Access Group dependent on these mappings. In this scenario, access groups assignations will get ignored
*   When a Directory Group is mapped to an Access Group, members of that group will default to `Contributor` role at team level. This is unless another Directory Group assignation overrides the team role

--------------------------------------------------------------------------------
title: "Access Roles"
description: "Learn about the different roles available for team members on a Vercel account."
last_updated: "null"
source: "https://vercel.com/docs/rbac/access-roles"
--------------------------------------------------------------------------------

# Access Roles

Copy page

Ask AI about this page

Last updated October 27, 2025

Vercel distinguishes between different roles to help manage team members' access levels and permissions. These roles are categorized into two groups: team level and project level roles. Team level roles are applicable to the entire team, affecting all projects within that team. Project level roles are confined to individual projects.

The two groups are further divided into specific roles, each with its own set of permissions and responsibilities. These roles are designed to provide a balance between autonomy and security, ensuring that team members have the access they need to perform their tasks while maintaining the integrity of the team and its resources.

*   [Team level roles](#team-level-roles): Users who have access to all projects within a team
    *   [Owner](#owner-role)
    *   [Member](#member-role)
    *   [Developer](#developer-role)
    *   [Security](#security-role)
    *   [Billing](#billing-role)
    *   [Pro Viewer](#pro-viewer-role)
    *   [Enterprise Viewer](#enterprise-viewer-role)
    *   [Contributor](#contributor-role)
*   [Project level roles](#project-level-roles): Users who have restricted access at the project level. Only contributors can have configurable project roles
    *   [Project Administrator](#project-administrators)
    *   [Project Developer](#project-developer)
    *   [Project Viewer](#project-viewer)

## [Team level roles](#team-level-roles)

Team level roles are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Team level roles are designed to provide a broad level of control and access to the team as a whole. These roles are assigned to individuals and apply to all projects within the team, ensuring centralized control and access while upholding the team's security and integrity.

| Role | Description |
| --- | --- |
| [Owner](#owner-role) | Have the highest level of control. They can manage, modify, and oversee the team's settings, all projects, team members and roles. |
| [Member](#member-role) | Have full control over projects and most team settings, but cannot invite or manage users by default. |
| [Developer](#developer-role) | Can deploy to projects and manage environment settings but lacks the comprehensive team oversight that an owner or member possesses. |
| [Security](#security-role) | Can manage security features, IP blocking, firewall. Cannot create deployments by default. |
| [Billing](#billing-role) | Primarily responsible for the team's financial management and oversight. The billing role also gets read-only access to every project. |
| [Pro Viewer](#pro-viewer-role) | Has limited read-only access to projects and deployments, ideal for stakeholder collaboration |
| [Enterprise Viewer](#enterprise-viewer-role) | Has read-only access to the team's resources and projects. |
| [Contributor](#contributor-role) | A unique role that can be configured to have any of the project level roles or none. If a contributor has no assigned project role, they won't be able to access that specific project. Only contributors can have configurable project roles. |

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Owner role](#owner-role)

The owner role is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

| About | Details |
| --- | --- |
| Description | The owner role is the highest level of authority within a team, possessing comprehensive access and control over all team and [project settings](/docs/projects/overview#project-settings). |
| Key Responsibilities | \- Oversee and manage all team resources and projects  
\- Modify team settings, including [billing](#billing-role) and [member](#member-role) roles  
\- Grant or revoke access to team projects and determine project-specific roles for members  
\- Access and modify all projects, including their settings and deployments |
| Access and Permissions | Owners have unrestricted access to all team functionalities, can modify all settings, and change other members' roles.  
Team owners inherently act as [project administrators](#project-administrators) for every project within the team, ensuring that they can manage individual projects' settings and deployments. |

Teams can have more than one owner. For continuity, we recommend that at least two individuals have owner permissions. Additional owners can be added without any impact on existing ownership. Keep in mind that role changes, including assignment and revocation of team member roles, are an exclusive capability of those with the owner role.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Member role](#member-role)

The member role is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Members play a pivotal role in team operations and project management.

Key responsibilities

*   Create [deployments](/docs/deployments) and manage projects
*   Set up [integrations](/docs/integrations) and manage project-specific [domains](/docs/domains)
*   Handle [deploy hooks](/docs/deploy-hooks) and adjust [Vercel Function](/docs/functions) settings
*   Administer security settings for their assigned projects

Access and permissions

Certain team-level settings remain exclusive to owners. Members cannot edit critical team settings like billing information or [invite new users to the team](/docs/rbac/managing-team-members), this keeps a clear boundary between the responsibilities of members and owners.

| About | Details |
| --- | --- |
| Description | Members play a pivotal role in team operations and project management. |
| Key Responsibilities | \- Create [deployments](/docs/deployments) and manage projects  
\- Set up [integrations](/docs/integrations) and manage project-specific [domains](/docs/domains)  
\- Handle [deploy hooks](/docs/deploy-hooks) and adjust [Serverless Function](/docs/functions/serverless-functions) settings  
\- Administer security settings for their assigned projects |
| Access and Permissions | Certain team-level settings remain exclusive to owners. Members cannot edit critical team settings like billing information or [invite new users to the team](/docs/rbac/managing-team-members), keeping a clear boundary between the responsibilities of members and owners. |

To assign the member role to a team member, refer to our [Adding team members and assigning roles](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) documentation.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Developer role](#developer-role)

The developer role is available on [Enterprise plans](/docs/plans/enterprise)

| About | Details |
| --- | --- |
| Description | Central to the team's operational functionality, developers ensure a balance between project autonomy and the safeguarding of essential settings. |
| Key Responsibilities | \- Create [deployments](/docs/deployments) and manage projects  
\- Control [environment variables](/docs/environment-variables), particularly for preview and development environments  
\- Manage project [domains](/docs/domains)  
\- Create a [production build](/docs/deployments/environments#production) by committing to the `main` branch of a project. Developers can also create preview branches and [preview deployments](/docs/deployments/environments#preview-environment-pre-production) by committing to any branch other than `main` |
| Access and Permissions | While developers have significant access to project functionalities, they are restricted from altering production environment variables and team-specific settings. They cannot invite new team members.  
Only contributors can be assigned [project level roles](#project-level-roles); developers cannot.  
Developers can deploy to production by merging to the production branch in Git-based workflows. |

Central to the team's operational functionality, developers ensure a balance between project autonomy and the safeguarding of essential settings.

Key responsibilities

*   Create [deployments](/docs/deployments) and manage projects
*   Control [environment variables](/docs/environment-variables), particularly for preview and development environments
*   Manage project [domains](/docs/domains)
*   Create a [production build](/docs/deployments/environments#production-environment) by committing to the `main` branch of a project. Note that developers can create preview branches and [preview deployments](/docs/deployments/environments#preview-environment-pre-production) by committing to any branch other than `main`

Access and permissions

While Developers have significant access to project functionalities, they are restricted from altering production environment variables and team-specific settings. They are also unable to invite new team members. Note that the capability to become a project administrator is reserved for the contributor role. Those with the developer role cannot be assigned [project level roles](#project-level-roles).

Developers can deploy to production through merging to the production branch for Git projects.

Additional information

To assign the developer role to a team member, refer to our [Adding team members and assigning roles](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) documentation.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Contributor role](#contributor-role)

The contributor role is available on [Enterprise plans](/docs/plans/enterprise)

Contributors offer flexibility in access control at the project level. To limit team members' access at the project level, they must first be assigned the contributor role. Only after being assigned the contributor role can they receive project-level roles. Contributors have no access to projects unless explicitly assigned.

Contributors may have project-specific role assignments, with the potential for comprehensive control over assigned projects only.

Key responsibilities

*   Typically assigned to specific projects based on expertise and needs
*   Initiate [deployments](/docs/deployments) - _Depending on their assigned [project role](#project-level-roles)_
*   Manage [domains](/docs/domains) and set up [integrations](/docs/integrations) for projects if they have the [project administrator](#project-administrators) role assigned
*   Adjust [Vercel functions](/docs/functions) and oversee [deploy hooks](/docs/deploy-hooks)

Access and permissions

Contributors can be assigned to specific projects and have the same permissions as [project administrators](#project-administrators), [project developers](#project-developer), or [project viewers](#project-viewer). They can also be assigned no project role, which means they won't be able to access that specific project.

| About | Details |
| --- | --- |
| Description | Contributors offer flexibility in access control at the project level. To limit team members' access at the project level, they must first be assigned the contributor role. Only after being assigned the contributor role can they receive project-level roles.  
\- Contributors have no access to projects unless explicitly assigned.  
\- Contributors may have project-specific role assignments, with the potential for comprehensive control over assigned projects only. |
| Key Responsibilities | \- Typically assigned to specific projects based on expertise and needs  
\- Initiate [deployments](/docs/deployments) — _Depending on their assigned [project role](#project-level-roles)_  
\- Manage [domains](/docs/domains) and set up [integrations](/docs/integrations) for projects if they have the [project administrator](#project-administrators) role assigned  
\- Adjust [Serverless Functions](/docs/functions/serverless-functions) and oversee [deploy hooks](/docs/deploy-hooks) |
| Access and Permissions | Contributors can be assigned to specific projects and have the same permissions as [project administrators](#project-administrators), [project developers](#project-developer), or [project viewers](#project-viewer).  
They can also be assigned no project role, which means they won't be able to access that specific project.  
See the [Project level roles](#project-level-roles) section for more information on project roles. |

To assign the contributor role to a team member, refer to our [Adding team members and assigning roles](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) documentation.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Security role](#security-role)

The security role is available on [Enterprise plans](/docs/plans/enterprise)

| About | Details |
| --- | --- |
| Description | Inspect and manage Vercel security features. |
| Key Responsibilities | \- Manage Firewall  
\- Rate Limiting  
\- Deployment Protection |
| Access and Permissions | The security role is designed to provide focused access to security features and settings.  
This role also has read-only access to all projects within the team. |

This role does not offer deployment permissions by default.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Billing role](#billing-role)

The billing role is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

| About | Details |
| --- | --- |
| Description | Specialized for financial operations, the billing role oversees financial operations and team resources management. |
| Key Responsibilities | \- Oversee and manage the team's billing information  
\- Review and manage team and project costs  
\- Handle the team's payment methods |
| Access and Permissions | The billing role is designed to provide financial oversight and management, with access to the team's billing information and payment methods.  
This role also has read-only access to all projects within the team. |

The billing role can be assigned at no extra cost. For [Pro teams](/docs/plans/pro), it's limited to one member while for [Enterprise teams](/docs/plans/enterprise), it can be assigned to multiple members.

To assign the billing role to a team member, refer to our [Adding team members and assigning roles](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) documentation.

Compatible permission group: `UsageViewer`.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Pro Viewer role](#pro-viewer-role)

The Pro Viewer role is available on [Pro plans](/docs/plans/pro)

An observational role designed for Pro teams, Pro Viewer members can monitor team activities and collaborate on projects with limited administrative visibility.

Key responsibilities

*   Monitor and inspect all team [projects](/docs/projects/overview) and deployments
*   Collaborate on [preview deployments](/docs/deployments/environments#preview-environment-pre-production) with commenting and feedback capabilities
*   Review project-level performance data and analytics

Access and permissions

Pro Viewer members have read-only access to core project functionality but cannot view sensitive team data. They are restricted from:

*   Viewing observability and log data
*   Accessing team settings and configurations
*   Viewing detailed usage data and billing information

Pro Viewer members cannot make changes to any settings or configurations.

Additional information

Pro Viewer seats are provided free of charge on Pro teams, making them ideal for stakeholders who need project visibility without full administrative access.

To assign the Pro Viewer role to a team member, refer to the [adding team members and assigning roles](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) documentation.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

### [Enterprise Viewer role](#enterprise-viewer-role)

The viewer role is available on [Enterprise plans](/docs/plans/enterprise)

| About | Details |
| --- | --- |
| Description | An observational role, viewers are informed on team activities without direct intervention. |
| Key Responsibilities | \- Monitor and inspect all team [projects](/docs/projects/overview)  
\- Review shared team resources  
\- Observe team settings and configurations |
| Access and Permissions | Viewers have broad viewing privileges but are restricted from making changes. |

The Enterprise Viewer role is available on [Enterprise plans](/docs/plans/enterprise)

An observational role with enhanced visibility for Enterprise teams, Enterprise Viewer members have comprehensive read-only access to team activities and operational data.

Key responsibilities

*   Monitor and inspect all team [projects](/docs/projects/overview) and deployments
*   Collaborate on [preview deployments](/docs/deployments/environments#preview-environment-pre-production) with commenting and feedback capabilities
*   Review project-level performance data and analytics
*   Access observability and log data for troubleshooting and monitoring
*   View team settings and configurations for governance and compliance
*   Monitor usage data and resource consumption patterns

Access and permissions

Enterprise Viewer members have comprehensive read-only access across the team, including sensitive operational data that Pro viewers cannot access. This enhanced visibility supports Enterprise governance and compliance requirements.

Enterprise Viewer members cannot make changes to any settings or configurations but have visibility into all team operations.

Additional information

The enhanced access provided by Enterprise Viewer roles makes them ideal for compliance officers, auditors, and senior stakeholders who need full operational visibility.

To assign the Enterprise Viewer role to a team member, refer to the [adding team members and assigning roles](/docs/rbac/managing-team-members#adding-team-members-and-assigning-roles) documentation.

Compatible permission group: `UsageViewer`.

See the [Team Level Roles Reference](/docs/rbac/access-roles/team-level-roles) for a complete list of roles and their permissions.

## [Project level roles](#project-level-roles)

Project level roles are available on [Enterprise plans](/docs/plans/enterprise)

Project level roles provide fine-grained control and access to specific projects within a team. These roles are assigned to individuals and are restricted to the projects they're assigned to, allowing for precise access control while preserving the overarching security and integrity of the team.

| Role | Description |
| --- | --- |
| [Project Administrator](#project-administrators) | Team owners and members inherently act as project administrators for every project. Project administrators can create production deployments, manage all [project settings](/docs/projects/overview#project-settings), and manage production [environment variables](/docs/environment-variables). |
| [Project Developer](#project-developer) | Can deploy to the project and manage its environment settings. Team developers inherently act as project developers. |
| [Project Viewer](#project-viewer) | Has read-only access to a specific project. Both team billing and viewer members automatically act as project viewers for every project. |

See the [Project Level Roles Reference](/docs/rbac/access-roles/project-level-roles) for a complete list of roles and their permissions.

### [Project administrators](#project-administrators)

The project administrator role is available on [Enterprise plans](/docs/plans/enterprise)

| About | Details |
| --- | --- |
| Description | Project administrators hold significant authority at the project level, operating as the project-level counterparts to team [members](#owner-role) and [owners](#owner-role). |
| Key Responsibilities | \- Govern [project settings](/docs/projects/overview#project-settings)  
\- Deploy to all [environments](/docs/deployments/environments)  
\- Manage all [environment variables](/docs/environment-variables) and oversee [domains](/docs/domains) |
| Access and Permissions | Their authority doesn't extend across all [projects](/docs/projects/overview) within the team. Project administrators are restricted to the projects they're assigned to. |

To assign the project administrator role to a team member, refer to our [Assigning project roles](/docs/rbac/managing-team-members#assigning-project-roles) documentation.

See the [Project Level Roles Reference](/docs/rbac/access-roles/project-level-roles) for a complete list of roles and their permissions.

### [Project developer](#project-developer)

The project developer role is available on [Enterprise plans](/docs/plans/enterprise)

| About | Details |
| --- | --- |
| Description | Project developers play a key role in working on projects, mirroring the functions of [team developers](#developer-role), but with a narrowed project focus. |
| Key Responsibilities | \- Initiate [deployments](/docs/deployments)  
\- Manage [environment variables](/docs/environment-variables) for development and [preview environments](/docs/deployments/environments#preview-environment-pre-production)  
\- Handle project [domains](/docs/domains) |
| Access and Permissions | Project developers have limited scope, with access restricted to only the projects they're assigned to. |

To assign the project developer role to a team member, refer to our [Assigning project roles](/docs/rbac/managing-team-members#assigning-project-roles) documentation.

See the [Project Level Roles Reference](/docs/rbac/access-roles/project-level-roles) for a complete list of roles and their permissions.

### [Project viewer](#project-viewer)

The project viewer role is available on [Enterprise plans](/docs/plans/enterprise)

| About | Details |
| --- | --- |
| Description | Adopting an observational role within the project scope, they ensure transparency and understanding across projects. |
| Key Responsibilities | \- View and inspect all [deployments](/docs/deployments)  
\- Review [project settings](/docs/projects/overview#project-settings)  
\- Examine [environment variables](/docs/environment-variables) across all environments and view project [domains](/docs/domains) |
| Access and Permissions | They have a broad view but can't actively make changes. |

To assign the project viewer role to a team member, refer to our [Assigning project roles](/docs/rbac/managing-team-members#assigning-project-roles) documentation.

See the [Project Level Roles Reference](/docs/rbac/access-roles/project-level-roles) for a complete list of roles and their permissions.

## [Permission groups](#permission-groups)

Existing team roles can be combined with permission groups to create custom access configurations based on your team's specific needs. This allows for more granular control over what different team members can do within the Vercel platform. The table below outlines key permissions that can be assigned to customize roles.

| Permission | Description | Compatible Roles | Already Included in |
| --- | --- | --- | --- |
| Create Project | Allows the user to create a new project. | Developer, Contributor | Owner, Member |
| Full Production Deployment | Deploy to production from CLI, rollback and promote any deployment. | Developer, Contributor | Owner, Member |
| Usage Viewer | Read-only usage team-wide including prices and invoices. | Developer, Security, Billing, Viewer | Owner |
| Environment Manager | Create and manage project environments. | Developer | Owner |
| Environment Variable Manager | Create and manage environment variables. | Developer | Owner, Member |
| Deployment Protection Manager | Configure password protection, deployment protection by pass, and Vercel Authentication for projects. | Developer | Owner, Member |

See [project level roles](/docs/rbac/access-roles/project-level-roles) and [team level roles](/docs/rbac/access-roles/team-level-roles) for a complete list of roles, their permissions, and how they can be combined.

--------------------------------------------------------------------------------
title: "Extended permissions"
description: "Learn about extended permissions in Vercel's RBAC system. Understand how to combine roles and permissions for precise access control."
last_updated: "null"
source: "https://vercel.com/docs/rbac/access-roles/extended-permissions"
--------------------------------------------------------------------------------

# Extended permissions

Copy page

Ask AI about this page

Last updated October 10, 2025

Vercel's Role-Based Access Control (RBAC) system consists of three main components:

*   Team roles: Core roles that define a user's overall access level within a team
*   Project roles: Roles that apply to specific projects rather than the entire team
*   Extended permissions: Granular permissions that can be combined with roles for fine-tuned access control

These components can be combined to create precise access patterns tailored to your organization's needs.

## [Project roles for specific access](#project-roles-for-specific-access)

Project roles apply only to specific projects and include:

| Project Role | Compatible Team Roles | Permissions Enabled Through Role |
| --- | --- | --- |
| [Admin](/docs/rbac/access-roles#project-administrators) | [Contributor](/docs/rbac/access-roles#contributor-role), [Developer](/docs/rbac/access-roles#developer-role) | Full control over a specific project including production deployments and settings |
| [Project Developer](/docs/rbac/access-roles#project-developer) | [Contributor](/docs/rbac/access-roles#contributor-role) | Can deploy to assigned project and manage dev/preview environment variables |
| [Project Viewer](/docs/rbac/access-roles#project-viewer) | [Contributor](/docs/rbac/access-roles#contributor-role) | Read-only access to assigned project |

## [Extended permissions for granular access](#extended-permissions-for-granular-access)

Extended permissions add granular capabilities that can be combined with roles:

| Extended permission | Description | Compatible Roles | Already Included in |
| --- | --- | --- | --- |
| 
Create Project

 | Allows the user to create a new project. | [Developer](/docs/rbac/access-roles#developer-role) | [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role) |
| 

Full Production Deployment

 | Deploy to production from CLI, rollback and promote any deployment. | [Developer](/docs/rbac/access-roles#developer-role), [Contributor](/docs/rbac/access-roles#contributor-role) | [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role) |
| 

Usage Viewer

 | Read-only usage team-wide including prices and invoices. | [Developer](/docs/rbac/access-roles#developer-role), [Security](/docs/rbac/access-roles#security-role), [Member](/docs/rbac/access-roles#member-role), [Viewer](/docs/rbac/access-roles#viewer-role) | [Owner](/docs/rbac/access-roles#owner-role), [Billing](/docs/rbac/access-roles#billing-role) |
| 

Integration Manager

 | Install and use Vercel integrations, marketplace integrations, and storage. | [Developer](/docs/rbac/access-roles#developer-role), [Security](/docs/rbac/access-roles#security-role), [Billing](/docs/rbac/access-roles#billing-role), [Viewer](/docs/rbac/access-roles#viewer-role), [Contributor](/docs/rbac/access-roles#contributor-role) | [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role) |
| 

Environment Manager

 | Create and manage project environments. | [Developer](/docs/rbac/access-roles#developer-role), [Member](/docs/rbac/access-roles#member-role) | [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role) |
| 

Environment Variable Manager

 | Create and manage environment variables. | [Developer](/docs/rbac/access-roles#developer-role) | [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#member-role) |

Extended permissions work when the user has at least one compatible team role.

### [How roles fit together](#how-roles-fit-together)

Team roles provide the foundation of access control. Each role has a specific scope of responsibilities:

| Team Role | Role Capabilities | Compatible Extended Permissions |
| --- | --- | --- |
| [Owner](/docs/rbac/access-roles#owner-role) | Complete control over all team and project settings | All extended permissions (already includes all permissions by default) |
| [Member](/docs/rbac/access-roles#member-role) | Can manage projects but not team settings | \- [Environment Manager](#environment-manager)  
\- [Usage Viewer](#usage-viewer) |
| [Developer](/docs/rbac/access-roles#developer-role) | Can deploy and manage projects with limitations on production settings | \- [Create Project](#create-project)  
\- [Full Production Deployment](#full-production-deployment)  
\- [Usage Viewer](#usage-viewer)  
\- [Integration Manager](#integration-manager)  
\- [Environment Manager](#environment-manager)  
\- [Environment Variable Manager](#environment-variable-manager) |
| [Billing](/docs/rbac/access-roles#billing-role) | Manages financial aspects only | \- [Integration Manager](#integration-manager) |
| [Security](/docs/rbac/access-roles#security-role) | Manages security features team-wide | \- [Usage Viewer](#usage-viewer)  
\- [Integration Manager](#integration-manager) |
| [Viewer](/docs/rbac/access-roles#viewer-role) | Read-only access to all projects | \- [Usage Viewer](#usage-viewer)  
\- [Integration Manager](#integration-manager) |
| [Contributor](/docs/rbac/access-roles#contributor-role) | Configurable role that can be assigned project-level roles | \- [Full Production Deployment](#full-production-deployment)  
\- [Integration Manager](#integration-manager)  
See project-level table for compatible project roles and permissions |

## [How combinations work](#how-combinations-work)

The multi-role system allows users to have multiple roles simultaneously. When roles are combined:

*   Users inherit the most permissive combination of all their assigned roles and permissions
*   A user gets all the capabilities of each assigned role
*   Extended permissions can supplement roles with additional capabilities
*   Project roles can be assigned alongside team roles for project-specific access

The following table outlines various use cases and the role combinations that enable them. Each combination is designed to provide specific capabilities while maintaining security and access control.

| Use Case | Role Combinations | Key Permissions | Outcome |
| --- | --- | --- | --- |
| DevOps engineer | [Developer](/docs/rbac/access-roles#developer-role) + [Environment Variable Manager](#environment-variable-manager) + [Full Production Deployment](#full-production-deployment) | \- Deploy to both preview and production environments  
\- Manage preview and production environment variables  
\- Full deployment capabilities incl. CLI and rollbacks | Manages deployments and config without billing or team access |
| Technical team lead | [Member](/docs/rbac/access-roles#member-role) + [Security](/docs/rbac/access-roles#security-role) | \- Create/manage projects and team members  
\- Configure deployment protection, rate limits  
\- Manage log drains and monitoring | Leads projects and enforces security without [Owner](/docs/rbac/access-roles#owner-role) access |
| External contractor | [Contributor](/docs/rbac/access-roles#contributor-role) + [Project Developer](/docs/rbac/access-roles#project-developer) (for specific projects only) | \- Can deploy to assigned projects only  
\- No access to team settings or other projects | Limited project access for external collaborators |
| Finance manager | [Billing](/docs/rbac/access-roles#billing-role) + [Usage Viewer](#usage-viewer) | \- Manage billing and payment methods  
\- View usage metrics across projects  
\- Read-only project access | Monitors costs and handles billing with no dev access |
| Product owner | [Viewer](/docs/rbac/access-roles#viewer-role) + [Create Project](#create-project) + [Environment Manager](#environment-manager) | \- Read-only access to all projects  
\- Create new projects  
\- Manage environments, but not deployments or settings | Oversees product workflows, supports setup but not execution |

## [Role compatibility and constraints](#role-compatibility-and-constraints)

Not all roles and permissions can be meaningfully combined. For example:

*   The [Owner](/docs/rbac/access-roles#owner-role) role already includes all permissions, so adding additional roles doesn't grant more access
*   Some extended permissions are only compatible with specific roles (e.g. [Full Production Deployment](#full-production-deployment) works with [Developer](/docs/rbac/access-roles#developer-role), [Member](/docs/rbac/access-roles#member-role), and [Owner](/docs/rbac/access-roles#owner-role) roles)
*   Project roles are primarily assigned to [Contributors](/docs/rbac/access-roles#contributor-role) or via Access Groups

--------------------------------------------------------------------------------
title: "Project Level Roles"
description: "Learn about the project level roles and their permissions."
last_updated: "null"
source: "https://vercel.com/docs/rbac/access-roles/project-level-roles"
--------------------------------------------------------------------------------

# Project Level Roles

Copy page

Ask AI about this page

Last updated October 10, 2025

Project level roles are available on [Enterprise plans](/docs/plans/enterprise)

Project level roles are assigned to a team member on a project level. This means that the role is only valid for the project it is assigned to. The role is not valid for other projects in the team.

## [Equivalency roles](#equivalency-roles)

In the table below, the relationship between team and project roles is indicated by the column headers. For example, the team role "Developer" is equivalent to the "Project Developer" role.

*   The [Developer](/docs/rbac/access-roles#developer-role) team role is equivalent to the [Project Developer](/docs/rbac/access-roles#project-developer) role
*   The [Viewer Pro](/docs/rbac/access-roles#viewer-pro-role), [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role), and [Billing](/docs/rbac/access-roles#billing-role) team roles are equivalent to the [Project Viewer](/docs/rbac/access-roles#project-viewer) role
*   The [Owner](/docs/rbac/access-roles#owner-role) and [Member](/docs/rbac/access-roles#member-role) team roles are equivalent to the [Project Admin](/docs/rbac/access-roles#project-administrators) role

All project level roles can be assigned to those with the [Contributor](/docs/rbac/access-roles#team-level-roles) team role.

See our [Access roles docs](/docs/rbac/access-roles) for a more comprehensive breakdown of the different roles.

## [Project level permissions](#project-level-permissions)

--------------------------------------------------------------------------------
title: "Team Level Roles"
description: "Learn about the different team level roles and the permissions they provide."
last_updated: "null"
source: "https://vercel.com/docs/rbac/access-roles/team-level-roles"
--------------------------------------------------------------------------------

# Team Level Roles

Copy page

Ask AI about this page

Last updated October 10, 2025

Team level roles are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Team level roles are designed to provide a comprehensive level of control and access to the team as a whole. These roles are assigned to individuals and are applicable to all projects within the team. This allows for a centralized level of control and access, while still maintaining the security and integrity of the team as a whole.

While the [Enterprise](/docs/plans/enterprise) plan supports all the below roles, the [Pro](/docs/plans/pro) plan only supports [Owner](/docs/rbac/access-roles#owner-role), [Member](/docs/rbac/access-roles#owner-role), and [Billing](/docs/rbac/access-roles#billing-role).

--------------------------------------------------------------------------------
title: "Managing Team Members"
description: "Learn how to manage team members on Vercel, and how to assign roles to each member with role-based access control (RBAC)."
last_updated: "null"
source: "https://vercel.com/docs/rbac/managing-team-members"
--------------------------------------------------------------------------------

# Managing Team Members

Copy page

Ask AI about this page

Last updated September 24, 2025

As the team owner, you have the ability to manage your team's composition and the roles of its members, controlling the actions they can perform. These role assignments, governed by Role-Based Access Control (RBAC) permissions, define the access level each member has across all projects within the team's scope. Details on the various roles and the permissions they entail can be found in the [Access Roles section](/docs/rbac/access-roles).

## [Adding team members and assigning roles](#adding-team-members-and-assigning-roles)

Inviting new team members is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

1.  From the dashboard, select your team from the [scope selector](/docs/dashboard-features#scope-selector)
    
2.  Select the Settings tab and go to the Members section
    
3.  Enter the email address of the person you would like to invite, assign their [role](/docs/rbac/access-roles), and select the Invite button. You can invite multiple people at once using the Add more button:
    
    ![Inviting new members to your team.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Frbac-settings-members-light.png&w=1920&q=75)![Inviting new members to your team.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Frbac-settings-members-dark.png&w=1920&q=75)
    
    Inviting new members to your team.
    
4.  By default only the team level roles are visible in the dropdown. If you choose to assign the [contributor role](/docs/rbac/access-roles#contributor-role) to the new member, a second dropdown will be accessible by selecting the Assign Project Roles button. You can then select the project, and their role on that project you want to assign the contributor to:
    
    Assigning project roles is available on [Enterprise plans](/docs/plans/enterprise)
    
    Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature
    
    ![Assigning a contributor role to a new member.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Frbac-settings-assign-contributor-light.png&w=1920&q=75)![Assigning a contributor role to a new member.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Frbac-settings-assign-contributor-dark.png&w=1920&q=75)
    
    Assigning a contributor role to a new member.
    
5.  You can view all pending invites in the Pending Invitations tab. When you issue an invite the recipient is not automatically added to the team. They have 72 hours to accept the invite and join the team. After 72 hours, the invite will show as expired in the Pending Invitations tab. Once a member has accepted an invitation to the team, they'll be displayed as team members with their assigned role.
    
6.  Once a member has been accepted onto the team, you can edit their role using the Manage Role button located alongside their assigned role in the Team Members tab.
    
    ![Changing a member's role.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Fproject-rbac-settings-manage-team-role-light.png&w=1080&q=75)![Changing a member's role.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Fproject-rbac-settings-manage-team-role-dark.png&w=1080&q=75)
    
    Changing a member's role.
    

### [Invite link](#invite-link)

Team owners can also share an invite link with others to allow them to join the team without needing to be invited individually.

To generate an invite link:

1.  Ensure you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector)
2.  Select the Settings tab and go to the Members section
3.  Select the Invite Link button and use the icon to copy the invite link:
    
    ![Adding members to team using the Invite Link.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Fproject-rbac-invite-link-light.png&w=1080&q=75)![Adding members to team using the Invite Link.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Fproject-rbac-invite-link-dark.png&w=1080&q=75)
    
    Adding members to team using the Invite Link.
    
4.  Optionally, you can select Reset Invite Link to generate a new link. After doing this, all other invite links will become invalid.
5.  Share the link with others. Those who join from an invite link will be given the lowest permissions for that team. For the Enterprise plan, they will be assigned the [Viewer Enterprise](/docs/rbac/access-roles#viewer-enterprise-role) role. For the Pro plan, they will be assigned the [Member](/docs/rbac/access-roles#member-role) role.

## [Assigning project roles](#assigning-project-roles)

Assigning project roles is available on [Enterprise plans](/docs/plans/enterprise)

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

Team [owners](/docs/rbac/access-roles#owner-role) can assign project roles to team members with the [contributor role](/docs/rbac/access-roles#contributor-role), enabling control over their project-related actions. You can assign these roles during team invitations or to existing members.

1.  Ensure you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector)
2.  Select the project you want to assign a member to
3.  Select Access from the left navigation, then inside the Project Access section select the team members email from the dropdown
4.  Select the role you want to assign to the member on the project
    
    ![Assigning a project role to a member.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Frbac-project-settings-assign-role-light.png&w=3840&q=75)![Assigning a project role to a member.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Frbac%2Frbac-project-settings-assign-role-dark.png&w=3840&q=75)
    
    Assigning a project role to a member.
    

## [Delete a member](#delete-a-member)

Team owners can delete members from a team. You can also remove yourself from a team.

1.  Ensure you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector)
2.  Select the Settings tab and go to the Members section
3.  Next to the name of the person you'd like to remove, select the ellipses (…) and then select Remove from Team from the menu

Vercel is also SCIM compliant. This means that if you are using SAML SSO, de-provisioning from the third-party provider will also remove the member from Vercel.

--------------------------------------------------------------------------------
title: "Redirects"
description: "Learn how to use redirects on Vercel to instruct Vercel's platform to redirect incoming requests to a new URL."
last_updated: "null"
source: "https://vercel.com/docs/redirects"
--------------------------------------------------------------------------------

# Redirects

Copy page

Ask AI about this page

Last updated October 31, 2025

Redirects are rules that instruct Vercel to send users to a different URL than the one they requested. For example, if you rename a public route in your application, adding a redirect ensures there are no broken links for your users. There are two types of redirects you can use on Vercel:

*   [Dynamic](#dynamic-redirects): Dynamic redirects are used to redirect users to a different domain. They can be implemented using Vercel Functions, or Middleware.
*   [Static](#static-redirects): Static redirects are used to redirect users to a different page on the same domain. They can be implemented using the Vercel dashboard or configuration-based redirects.

With redirects on Vercel, you can define HTTP redirects in your application's configuration, regardless of the [framework](/docs/frameworks) that you are using, including both [dynamic](#dynamic-redirects) and [static](#static-redirects) redirects. Redirects are processed at the Edge across all regions.

## [Use cases](#use-cases)

*   Moving to a new domain: Redirects help maintain a seamless user experience when moving a website to a new domain by ensuring that visitors and search engines are aware of the new location.
*   Replacing a removed page: If a page has been moved, temporarily or permanently, you can use redirects to send users to a relevant new page, thus avoiding any negative impact on user experience.
*   Canonicalization of multiple URLs: If your website can be accessed through several URLs (e.g., `acme.com/home`, `home.acme.com`, or `www.acme.com`), you can choose a canonical URL and use redirects to guide traffic from the other URLs to the chosen one.
*   Geolocation-based redirects: Redirects can be configured to consider the source country of requests, enabling tailored experiences for users based on their geographic location.

## [Dynamic redirects](#dynamic-redirects)

We recommend using the framework-native solution for dynamic redirects.

### [Vercel Functions](#vercel-functions)

app/api/route.ts

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtOther frameworks

TypeScript

TypeScriptJavaScript

```
import { redirect } from 'next/navigation';
 
export async function GET(request: Request) {
  redirect('https://nextjs.org/');
}
```

### [Middleware](#middleware)

For dynamic, critical redirects that need to run on every request, you can use [Middleware](/docs/routing-middleware) and [Edge Config](/docs/storage/edge-config).

Redirects can be stored in an Edge Config and instantly read from Middleware. This enables you to update redirect values without having to redeploy your website.

[Deploy a template](https://vercel.com/templates/next.js/maintenance-page) to get started.

## [Static redirects](#static-redirects)

### [Dashboard redirects](#dashboard-redirects)

You can redirect a `www` subdomain to an apex domain, or other domain redirects, through the [Domains](/docs/projects/domains/deploying-and-redirecting#redirecting-domains) section of the dashboard.

### [Configuration redirects](#configuration-redirects)

You can use configuration-based redirects to generate routing rules during the build process. This includes temporary redirects (`307`), permanent redirects (`308`), and geolocation-based redirects.

Configuration-based redirects can be defined in framework-specific config file or in the `vercel.json` file, which is located in the root of your application. The `vercel.json` should contain a `redirects` field, which is an array of redirect rules. For more information on all available properties, see the [project configuration](/docs/projects/project-configuration#redirects) docs.

When using Next.js, you do _not_ need to use `vercel.json`. Instead, use the framework-native `next.config.js` to define configuration-based redirects.

next.config.js

```
module.exports = {
  async redirects() {
    return [
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
      {
        source: '/old-blog/:slug',
        destination: '/news/:slug',
        permanent: true,
      },
      {
        source: '/:path((?!uk/).*)',
        has: [
          {
            type: 'header',
            key: 'x-vercel-ip-country',
            value: 'GB',
          },
        ],
        permanent: false,
        destination: '/uk/:path*',
      },
    ];
  },
};
```

Learn more in the [Next.js documentation](https://nextjs.org/docs/app/building-your-application/routing/redirecting).

When deployed, these redirect rules will be deployed to every [region](/docs/regions) in Vercel's CDN.

### [Firewall redirects](#firewall-redirects)

In emergency situations, you can also define redirects using [Firewall rules](/docs/security/vercel-waf/examples#emergency-redirect) to redirect requests to a new page. Firewall redirects execute before CDN configuration redirects (e.g. `vercel.json` or `next.config.js`) are evaluated.

## [Redirect status codes](#redirect-status-codes)

Vercel supports both temporary and permanent redirects.

*   307 Temporary Redirect: Not cached by client, the method and body never changed. This type of redirect does not affect SEO and search engines will treat them as normal redirects.
*   302 Found: Not cached by client, the method may or may not be changed to `GET`.
*   308 Permanent Redirect: Cached by client, the method and body never changed. This type of redirect does not affect SEO and search engines will treat them as normal redirects.
*   301 Moved Permanently: Cached by client, the method may or may not be changed to `GET`.

We recommend using status code `307` or `308` to avoid the ambiguity of non `GET` methods, which is necessary when your application needs to redirect a public API.

## [Observing redirects](#observing-redirects)

You can observe your redirect performance using Observability. The Edge Requests tab shows request counts and cache status for your redirected routes, helping you understand traffic patterns and validate that redirects are working as expected. You can filter by redirect location to analyze specific redirect paths.

Learn more in the [Observability Insights](/docs/observability/insights#edge-requests) documentation.

## [Draining redirects](#draining-redirects)

You can export redirect data by draining logs from your application. Redirect events appear in your runtime logs, allowing you to analyze redirect patterns, debug redirect chains, and track how users move through your site.

To get started, configure a [logs drain](/docs/drains/using-drains).

## [Limits](#limits)

The /.well-known path is reserved and cannot be redirected or rewritten. Only Enterprise teams can configure custom SSL. [Contact sales](/contact/sales) to learn more.

### [Configuration](#configuration)

If you are exceeding the limits below, we recommend using Middleware and Edge Config to [dynamically read redirect values](/docs/redirects#edge-middleware).

| Limit | Maximum |
| --- | --- |
| Number of redirects in the array | 1,024 |
| String length for `source` and `destination` | 4,096 |

## [Best practices for implementing redirects](#best-practices-for-implementing-redirects)

There are some best practices to keep in mind when implementing redirects in your application:

1.  Test thoroughly: Test your redirects thoroughly to ensure they work as expected. Use a [preview deployment](/docs/deployments/environments#preview-environment-pre-production) to test redirects before deploying them to production
2.  Use relative paths: Use relative paths in your `destination` field to avoid hardcoding your domain name
3.  Use permanent redirects: Use [permanent redirects](#adding-redirects) for permanent URL changes and [temporary redirects](#adding-redirects) for temporary changes
4.  Use wildcards carefully: Wildcards can be powerful but should be used with caution. For example, if you use a wildcard in a source rule that matches any URL path, you could inadvertently redirect all incoming requests to a single destination, effectively breaking your site.
5.  Prioritize HTTPS: Use redirects to enforce HTTPS for all requests to your domain

--------------------------------------------------------------------------------
title: "Redis on Vercel"
description: "Learn how to use Redis stores through the Vercel Marketplace."
last_updated: "null"
source: "https://vercel.com/docs/redis"
--------------------------------------------------------------------------------

# Redis on Vercel

Copy page

Ask AI about this page

Last updated July 22, 2025

Vercel lets you connect external Redis databases through the [Marketplace](/marketplace), allowing you to integrate high-performance caching and real-time data storage into your Vercel projects without managing Redis servers.

*   Explore [Marketplace storage redis integrations](/marketplace?category=storage&search=redis).
*   Learn how to [add a Marketplace native integration](/docs/integrations/install-an-integration/product-integration).

## [Connecting to the Marketplace](#connecting-to-the-marketplace)

Vercel enables you to use Redis by integrating with external database providers. By using the Marketplace, you can:

*   Select a [Redis provider](/marketplace?category=storage&search=redis)
*   Provision and configure a Redis database with minimal setup.
*   Have credentials and [environment variables](/docs/environment-variables) injected into your Vercel project.

--------------------------------------------------------------------------------
title: "Vercel Regions"
description: "View the list of regions supported by Vercel's CDN and learn about our global infrastructure."
last_updated: "null"
source: "https://vercel.com/docs/regions"
--------------------------------------------------------------------------------

# Vercel Regions

Copy page

Ask AI about this page

Last updated September 15, 2025

Vercel's CDN is a globally distributed platform that stores content and runs compute close to your users and data, reducing latency and improving performance. This page details the [supported regions](#region-list) and explains our global infrastructure.

![Our global CDN has 126 Points of Presence in 94 cities across 51 countries.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fedge-network%2Fcdn-pops-light.png&w=3840&q=75)![Our global CDN has 126 Points of Presence in 94 cities across 51 countries.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fedge-network%2Fcdn-pops-dark.png&w=3840&q=75)

Our global CDN has 126 Points of Presence in 94 cities across 51 countries.

## [Global infrastructure](#global-infrastructure)

Vercel's CDN is built on a sophisticated global infrastructure designed to optimize performance and reliability:

*   Points of Presence (PoPs): We operate over 126 PoPs distributed across the globe. These PoPs serve as the first point of contact for incoming requests, ensuring low-latency access for users worldwide.
*   Vercel Regions: Behind these PoPs, we maintain 19 compute-capable regions where your code can run close to your data.
*   Private Network: Traffic flows from PoPs to the nearest region through private, low-latency connections, ensuring fast and efficient data transfer.

This architecture balances the benefits of widespread geographical distribution with the efficiency of concentrated caching and compute resources.

### [Caching strategy](#caching-strategy)

Our approach to caching is designed to maximize efficiency and performance:

*   By maintaining fewer, dense regions, we increase cache hit probability. This means that popular content is more likely to be available in each region's cache.
*   The extensive PoP network ensures that users can quickly access regional caches, minimizing latency.
*   This concentrated caching strategy results in higher cache hit ratios, reducing the need for requests to go back to the origin server and significantly improving response times.

## [Region list](#region-list)

Regions table
| 
Region Code

 | 

Region Name

 | 

Reference Location

 |
| --- | --- | --- |
| arn1 | eu-north-1 | Stockholm, Sweden |
| bom1 | ap-south-1 | Mumbai, India |
| cdg1 | eu-west-3 | Paris, France |
| cle1 | us-east-2 | Cleveland, USA |
| cpt1 | af-south-1 | Cape Town, South Africa |
| dub1 | eu-west-1 | Dublin, Ireland |
| dxb1 | me-central-1 | Dubai, United Arab Emirates |
| fra1 | eu-central-1 | Frankfurt, Germany |
| gru1 | sa-east-1 | São Paulo, Brazil |
| hkg1 | ap-east-1 | Hong Kong |
| hnd1 | ap-northeast-1 | Tokyo, Japan |
| iad1 | us-east-1 | Washington, D.C., USA |
| icn1 | ap-northeast-2 | Seoul, South Korea |
| kix1 | ap-northeast-3 | Osaka, Japan |
| lhr1 | eu-west-2 | London, United Kingdom |
| pdx1 | us-west-2 | Portland, USA |
| sfo1 | us-west-1 | San Francisco, USA |
| sin1 | ap-southeast-1 | Singapore |
| syd1 | ap-southeast-2 | Sydney, Australia |

For information on different resource pricing based on region, see the [regional pricing](/docs/pricing/regional-pricing) page.

### [Points of Presence (PoPs)](#points-of-presence-pops)

In addition to our 19 compute-capable regions, Vercel's CDN includes 126 PoPs distributed across the globe. These PoPs serve several crucial functions:

1.  Request routing: PoPs intelligently route requests to the nearest or most appropriate edge region with single-digit millisecond latency.
2.  DDoS protection: They provide a first line of defense against distributed denial-of-service attacks.
3.  SSL termination: PoPs handle SSL/TLS encryption and decryption, offloading this work from origin servers.

The extensive PoP network ensures that users worldwide can access your content with minimal latency, even if compute resources are concentrated in fewer regions.

## [Local development regions](#local-development-regions)

When you use [the `vercel dev` CLI command to mimic your deployment environment locally](/docs/cli/dev), the region is assigned `dev1` to mimic the Vercel platform infrastructure.

| Region Code | Reference Location |
| --- | --- |
| dev1 | localhost |

## [Compute defaults](#compute-defaults)

*   Vercel Functions default to running in the `iad1` (Washington, D.C., USA) region. Learn more about [changing function regions](/docs/functions/regions)

Functions should be executed in the same region as your database, or as close to it as possible, [for the lowest latency](/guides/choosing-deployment-regions).

## [Outage resiliency](#outage-resiliency)

Vercel's CDN is designed with high availability and fault tolerance in mind:

*   In the event of regional downtime, application traffic is automatically rerouted to the next closest region. This ensures that your application remains available to users even during localized outages.
*   Traffic will be rerouted to the next closest region in the following order:

## Regions by priority

Select region

arn1bom1bru1cdg1cle1cpt1dub1dxb1fra1gru1hkg1hnd1iad1icn1kix1lhr1pdx1sfo1sin1syd1

P0iad1

P1cle1

P2pdx1

P3sfo1

P4dub1

P5lhr1

P6cdg1

P7fra1

P8bru1

P9arn1

P10gru1

P11hnd1

P12kix1

P13icn1

P14bom1

P15hkg1

P16syd1

P17sin1

P18cpt1

*   For Enterprise customers, Vercel functions can automatically failover to a different region if the region they are running in becomes unavailable. Learn more about [Vercel Function failover](/docs/functions/configuring-functions/region#automatic-failover).

This multi-layered approach to resiliency, combining our extensive PoP network with intelligent routing and regional failover capabilities, ensures high availability and consistent performance for your applications.

--------------------------------------------------------------------------------
title: "Release Phases for Vercel"
description: "Learn about the different phases of the Vercel Product release cycle and the requirements that a Product must meet before being assigned to a specific phase."
last_updated: "null"
source: "https://vercel.com/docs/release-phases"
--------------------------------------------------------------------------------

# Release Phases for Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

This page outlines the different phases of the Vercel product release cycle. Each phase has a different set of requirements that a product must meet before being assigned to a phase.

Although a product doesn't have to pass through each stage in sequential order, there is a default flow to how products are released:

*   Alpha
*   Beta
*   General Availability (GA).

## [Alpha](#alpha)

The Alpha phase is the first phase of the release cycle. A product in the Alpha phase lacks the essential features that are required to be ready for GA. The product is considered to still be under development, and is being built to be ready for Beta phase.

The product is under development.

## [Beta](#beta)

A Beta state generally means that the feature does not yet meet our quality standards for GA or limited availability. An example of this is when there is a need for more information or feedback from external customers to validate that this feature solves a specific pain point.

Releases in the Beta state have a committed timeline for getting to GA and are actively worked on.

Products in a Beta state, are **not** covered under the [Service Level Agreement](https://vercel.com/legal/sla) (SLA) for Enterprise plans. Vercel **does not** recommend using Beta products in a full production environment.

### [Private Beta](#private-beta)

When a product is in Private Beta, it is still considered to be under development. While some customers may have access, this access sometimes includes a Non-disclosure agreement (NDA)

The product is under active development with limited customer access - may include an NDA.

### [Limited Beta](#limited-beta)

A Limited Beta is still under active development, but has been publicly announced, and is potentially available to a limited number of customers.

This phase is generally used when there is a need to control adoption of a feature. For example, when underlying capacity is limited, if there are known severe caveats then additional guidance may be required.

The product is under active development, and has been publicly announced. Limited customer access - may include an NDA.

### [Public Beta](#public-beta)

Once a product has been publicly announced, optionally tested in the field by selected customers, and meets Vercel's quality standards, it is considered to be in the Public Beta phase.

Public Beta is the final phase of the release cycle before a product goes GA. At this stage the product can be used by a wider audience for load testing, and onboarding.

For a product to move from Public Beta to GA, the following requirements must be met. Note that these are general requirements, and that each feature may have it's own set of requirements to meet:

*   Fully load tested
*   All bugs resolved
*   Security analysis completed
*   At least 10 customers have been on-boarded

The product is under active development, and has been publicly announced. Available to the public without special invitation.

See the [Public Beta Agreement](/docs/release-phases/public-beta-agreement) for detailed information.

## [General Availability](#general-availability)

When the product reaches the General Availability (GA) phase, it is considered to be battle tested, and ready for use by the community.

Publicly available with full support and guaranteed uptime.

## [Deprecated and Sunset](#deprecated-and-sunset)

A Deprecated state means that the product team is in the process of removing a product or feature. Deprecated states are accompanied by documentation instructing existing users of remediation next steps, and information on when to expect the feature to be in a Sunset state.

The ultimate state after Deprecation is Sunset. Sunset implies that there should be no customers using the Product and any artifacts within, but not limited to, code, documentation, and marketing have been removed.

--------------------------------------------------------------------------------
title: "Public Beta Agreement"
description: "The following is the Public Beta Agreement for Vercel products in the Public Beta release phase, including any services or functionality that may be made available to You that are not yet generally available, but are designated as beta, pilot, limited release, early access, preview, pilot, evaluation, or similar description."
last_updated: "null"
source: "https://vercel.com/docs/release-phases/public-beta-agreement"
--------------------------------------------------------------------------------

# Public Beta Agreement

Copy page

Ask AI about this page

Last updated February 7, 2025

This Public Beta Agreement (“Agreement”) is made and entered into effective as of the date You first agree to this Agreement (“Effective Date”) and is made by and between You and Vercel Inc. with a principal place of business at 440 N Barranca Ave, #4133, Covina, CA 91723 (“Vercel,” “us,” “our”). By clicking to use or enable the Product, You are confirming that You understand and accept all of this Agreement.

If You are entering into these terms on behalf of a company or other legal entity, You represent that You have the legal authority to bind the entity to this Agreement, in which case “You” will mean the entity you represent. If You do not have such authority, or if You do not agree with the terms of this Agreement, You should not accept this Agreement and may not use the Product. Except as may be expressly set forth herein, Your use of the Product is governed by this Agreement, and not by the Terms (as defined below).

## [1\. Definitions](#1.-definitions)

### [1.1 “Authorized User”](#1.1-“authorized-user”)

Any employee, contractor, or member of your organization (if applicable) who has been authorized to use the Services in accordance with the terms set forth herein. “You” as used in these Terms also includes Your “Authorized Users,” if any.

### [1.2 “Public Beta Period”](#1.2-“public-beta-period”)

The period commencing on the Effective Date and ending upon the release by Vercel of a generally available version of the Product or termination in accordance with this Agreement.

### [1.3 “Product”](#1.3-“product”)

The public beta version of any features, functionality, Software, SaaS, and all associated documentation (if any) (“Documentation”), collectively, made available by Vercel to you pursuant to this Agreement. This includes any services or functionality that may be made available to You that are not yet generally available, but are designated as beta, pilot, limited release, early access, preview, pilot, evaluation, or similar description.

### [1.4 “Software”](#1.4-“software”)

The public beta version of Vercel's proprietary software, if any, provided hereunder.

### [1.5 “Terms”](#1.5-“terms”)

Our Terms of Service or Enterprise Terms and Conditions, or any other agreements you have entered into with us for the provision of our services.

## [2\. License Grant](#2.-license-grant)

Subject to your compliance with the Terms and this Agreement, Vercel hereby grants You a non-exclusive, non-transferable, limited license (without the right to sublicense), solely for the Beta Period, to:

*   (i) access and use the Product and/or any associated Software;
*   (ii) use all associated Documentation in connection with such authorized use of the Product and/or Software; and
*   (iii) make one copy of any Documentation solely for archival and backup purposes.

In all cases of (i) - (iii) solely for Your personal or internal business use purposes.

## [3\. Open Source Software](#3.-open-source-software)

The Software may contain open source software components (“Open Source Components”). Such Open Source Components are not licensed under this Agreement, but are instead licensed under the terms of the applicable open source license. Your use of each Open Source Component is subject to the terms of each applicable license which are available to You in the readme or license.txt file, or “About” box, of the Software or on request from Vercel.

## [4\. Permissions and Restrictions](#4.-permissions-and-restrictions)

By agreeing to this Agreement, You allow the Product to connect to Your Vercel account. You must have a valid and active Vercel account in good standing to use or access the Product. You shall not use the Product in violation of the Terms that govern Your Vercel account. You are responsible for each of Your Authorized Users hereunder and their compliance with the terms of this Agreement. You shall not, and shall not permit any Authorized User or any third party to:

*   (i) reverse engineer, reverse assemble, or otherwise attempt to discover the source code of all or any portion of the Product;
*   (ii) reproduce, modify, translate or create derivative works of all or any portion of the Product;
*   (iii) export the Software or assist any third party to gain access, license, sublicense, resell distribute, assign, transfer or use the Product;
*   (iv) remove or destroy any proprietary notices contained on or in the Product or any copies thereof; or
*   (v) publish or disclose the results of any benchmarking of the Product, or use such results for Your own competing software development activities, in each case of (i) - (v) unless You have prior written permission from Vercel.

## [5\. Disclaimer of Warranty](#5.-disclaimer-of-warranty)

The Product made available to You is in "Beta” form, pre-release, and time limited. The Product may be incomplete and may contain errors or inaccuracies that could cause failures, corruption and/or loss of data or information. You expressly acknowledge and agree that, to the extent permitted by applicable law, all use of the Product is at your sole risk and the entire risk as to satisfactory quality, performance, accuracy, and effort is with You. You are responsible for the security of the environment in which You use the Software and You agree to follow best practices with respect to security. You acknowledge that Vercel has not publicly announced the availability of the Product, that Vercel has not promised or guaranteed to you that the Product will be announced or made available to anyone in the future, and that Vercel has no express or implied obligation to You to announce or introduce the Product or any similar or compatible product or to continue to offer or support the Product in the future.

YOU AGREE THAT VERCEL AND ITS LICENSORS PROVIDE THE PRODUCTS ON AN “AS IS” AND “WHERE IS” BASIS. NEITHER VERCEL NOR ITS LICENSORS MAKE ANY WARRANTIES WITH RESPECT TO THE PERFORMANCE OF THE PRODUCT OR RESULTS OBTAINED THEREFROM, WHETHER EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, AND VERCEL AND ITS LICENSORS EXPRESSLY DISCLAIM ALL OTHER WARRANTIES, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF NON-INFRINGEMENT OF THIRD PARTY RIGHTS, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

## [6\. Intellectual Property Rights; Support and Feedback](#6.-intellectual-property-rights;-support-and-feedback)

### [6.1 Intellectual Property Rights](#6.1-intellectual-property-rights)

All rights, title and interest in and to the Product and any improved, updated, modified or additional parts thereof, shall at all times remain the property of Vercel or its licensors. Nothing herein shall give or be deemed to give You any right, title or interest in or to the same except as expressly provided in this Agreement. Vercel reserves all rights not expressly granted herein.

### [6.2 Support](#6.2-support)

Notwithstanding the disclaimer of warranty above, Vercel may, but is not required to provide You with support on the use of the Product in accordance with Vercel’s standard support terms.

### [6.3 Feedback](#6.3-feedback)

You agree to use reasonable efforts to provide Vercel with oral feedback and/or written feedback related to Your use of the Product, including, but not limited to, a report of any errors which You discover in any Software or related Documentation. Such reports, and any other materials, information, ideas, concepts, feedback and know-how provided by You to Vercel concerning the Product and any information reported automatically through the Product to Vercel (“Feedback”) will be the property of Vercel. You agree to assign, and hereby assign, all right, title and interest worldwide in the Feedback, and the related intellectual property rights, to Vercel for Vercel to use and exploit in any manner and for any purpose, including to improve Vercel's products and services.

## [7\. Limitation of Liability; Allocation of Risk](#7.-limitation-of-liability;-allocation-of-risk)

### [7.1 Limitation of Liability](#7.1-limitation-of-liability)

NEITHER VERCEL NOR ITS LICENSORS SHALL BE LIABLE FOR SPECIAL, INCIDENTAL, CONSEQUENTIAL OR INDIRECT DAMAGES, RELATED TO THIS AGREEMENT, INCLUDING WITHOUT LIMITATION, LOST PROFITS, LOST SAVINGS, OR DAMAGES ARISING FROM LOSS OF USE, LOSS OF CONTENT OR DATA OR ANY ACTUAL OR ANTICIPATED DAMAGES, REGARDLESS OF THE LEGAL THEORY ON WHICH SUCH DAMAGES MAY BE BASED, AND EVEN IF VERCEL OR ITS LICENSORS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. IN NO EVENT SHALL VERCEL'S TOTAL LIABILITY RELATED TO THIS AGREEMENT EXCEED ONE HUNDRED DOLLARS (US $100.00). ADDITIONALLY, IN NO EVENT SHALL VERCEL'S LICENSORS BE LIABLE FOR ANY DAMAGES OF ANY KIND.

### [7.2 Allocation of Risk](#7.2-allocation-of-risk)

You and Vercel agree that the foregoing Section 7.1 on limitation of liability and the Section 5 above on warranty disclaimer fairly allocate the risks in the Agreement between the parties. You and Vercel further agree that this allocation is an essential element of the basis of the bargain between the parties and that the limitations specified in this Section 7 shall apply notwithstanding any failure of the essential purpose of this Agreement or any limited remedy hereunder.

## [8\. Term and Termination](#8.-term-and-termination)

### [8.1 Term and Termination](#8.1-term-and-termination)

This Agreement will continue in effect until the expiration of the Public Beta Period, unless otherwise extended in writing by Vercel, in its sole discretion, or the termination of this Agreement in accordance with this Section 8. Upon termination of this Agreement, You must cease use of the Product, unless You and Vercel have entered into a subsequent written license agreement that permits you to use or access the Product thereafter.

### [8.2 Termination](#8.2-termination)

You may terminate this Agreement at any time by ceasing use of the Product. This Agreement will terminate immediately upon written notice from Vercel if You fail to comply with any provision of this Agreement, including the confidentiality provisions set forth herein. Vercel may terminate this Agreement or any use of the Product at any time, with or without cause, immediately on written notice to you. Except for Section 2 (“License Grant”), all Sections of this Agreement shall survive termination for a period of three (3) years from the date hereof.

## [9\. Government End Users](#9.-government-end-users)

Software provided under this Agreement is commercial computer software programs developed solely at private expense. As defined in U.S. Federal Acquisition Regulations (FAR) section 2.101 and U.S. Defense Federal Acquisition Regulations (DFAR) sections 252.227-7014(a)(1) and 252.227-7014(a)(5) (or otherwise as applicable to You), the Software licensed in this Agreement is deemed to be “commercial items” and “commercial computer software” and “commercial computer software documentation.” Consistent with FAR section 12.212 and DFAR section 227.7202, (or such other similar provisions as may be applicable to You), any use, modification, reproduction, release, performance, display, or disclosure of such commercial Software or commercial Software documentation by the U.S. government (or any agency or contractor thereof) shall be governed solely by the terms of this Agreement and shall be prohibited except to the extent expressly permitted by the terms of this Agreement.

## [10\. General Provisions](#10.-general-provisions)

All notices under this Agreement will be in writing and will be deemed to have been duly given when received, if personally delivered; when receipt is electronically confirmed, if transmitted by email; the day after it is sent, if sent for next day delivery by recognized overnight delivery service; and upon receipt, if sent by certified or registered mail, return receipt requested. This Agreement shall be governed by the laws of the State of California, U.S.A. without regard to conflict of laws principles.

The parties agree that the United Nations Convention on Contracts for the International Sale of Goods is specifically excluded from application to this Agreement. If any provision hereof shall be held illegal, invalid or unenforceable, in whole or in part, such provision shall be modified to the minimum extent necessary to make it legal, valid and enforceable, and the remaining provisions of this Agreement shall not be affected thereby. The failure of either party to enforce any right or provision of this Agreement shall not constitute a waiver of such right or provision. Nothing contained herein shall be construed as creating an agency, partnership, or other form of joint enterprise between the parties.

This Agreement may not be assigned, sublicensed or otherwise transferred by either party without the other party's prior written consent except that either party may assign this Agreement without the other party's consent to any entity that acquires all or substantially all of such party's business or assets, whether by merger, sale of assets, or otherwise, provided that such entity assumes and agrees in writing to be bound by all of such party's obligations under this Agreement. This Agreement constitutes the parties' entire understanding regarding the Product, and supersedes any and all other prior or contemporaneous agreements, whether written or oral. Except as expressly set forth herein, all other terms and conditions of the Terms shall remain in full force and effect with respect to your access and use of Vercel's services, including the Product. If any terms of this Agreement conflict with the Terms, the conflicting terms in this Agreement shall control with respect to the Product.

--------------------------------------------------------------------------------
title: "Request Collapsing"
description: "Learn how Vercel's CDN shields your origin during traffic surges for uncached routes."
last_updated: "null"
source: "https://vercel.com/docs/request-collapsing"
--------------------------------------------------------------------------------

# Request Collapsing

Copy page

Ask AI about this page

Last updated September 15, 2025

Vercel uses request collapsing to protect uncached routes during high traffic. It reduces duplicate work by combining concurrent requests into a single function invocation within the same region. This feature is especially valuable for high-scale applications.

## [How request collapsing works](#how-request-collapsing-works)

When a request for an uncached path arrives, Vercel invokes the origin [function](/docs/functions) and stores the response in the [cache](/docs/edge-cache). In most cases, any following requests are served from this cached response.

However, if multiple requests arrive while the initial function is still processing, the cache is still empty. Instead of triggering additional invocations, Vercel's CDN collapses these concurrent requests into the original one. They wait for the first response to complete, then all receive the same result.

This prevents overwhelming the origin with duplicate work during traffic spikes and helps ensure faster, more stable performance.

Vercel also applies request collapsing when serving [STALE](/docs/headers/response-headers#stale) responses (with [stale-while-revalidate](/docs/headers/cache-control-headers#stale-while-revalidate) semantics), ensuring that concurrent background revalidation of multiple requests is collapsed into a single invocation.

### [Example](#example)

Suppose a new blog post is published and receives 1,000 requests at once. Without request collapsing, each request would trigger a separate function invocation, which could overload the backend and slow down responses, causing a [cache stampede](https://en.wikipedia.org/wiki/Cache_stampede).

With request collapsing, Vercel handles the first request, then holds the remaining 999 requests until the initial response is ready. Once cached, the response is sent to all users who requested the post.

## [Supported features](#supported-features)

Request collapsing is supported for:

*   [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration)
*   [Image Optimization](/docs/image-optimization)

--------------------------------------------------------------------------------
title: "Create an access group project"

last_updated: "2025-11-07T00:37:04.555Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/create-an-access-group-project"
--------------------------------------------------------------------------------

# Create an access group project

> Allows creation of an access group project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups/{accessGroupIdOrName}/projects
paths:
  path: /v1/access-groups/{accessGroupIdOrName}/projects
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        accessGroupIdOrName:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              projectId:
                allOf:
                  - type: string
                    maxLength: 256
                    example: prj_ndlgr43fadlPyCtREAqxxdyFK
                    description: The ID of the project.
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - PROJECT_VIEWER
                      - PROJECT_DEVELOPER
                    example: ADMIN
                    description: The project role that will be added to this Access Group.
            required: true
            requiredProperties:
              - role
              - projectId
            additionalProperties: false
        examples:
          example:
            value:
              projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
              role: ADMIN
    codeSamples:
      - label: createAccessGroupProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.createAccessGroupProject({
              accessGroupIdOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                role: "ADMIN",
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              teamId:
                allOf:
                  - type: string
              accessGroupId:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - PROJECT_DEVELOPER
                      - PROJECT_VIEWER
              createdAt:
                allOf:
                  - type: string
              updatedAt:
                allOf:
                  - type: string
            requiredProperties:
              - teamId
              - accessGroupId
              - projectId
              - role
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              teamId: <string>
              accessGroupId: <string>
              projectId: <string>
              role: ADMIN
              createdAt: <string>
              updatedAt: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Creates an access group"

last_updated: "2025-11-07T00:37:05.132Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/creates-an-access-group"
--------------------------------------------------------------------------------

# Creates an access group

> Allows to create an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups
paths:
  path: /v1/access-groups
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The name of the access group
                    maxLength: 50
                    pattern: ^[A-z0-9_ -]+$
                    example: My access group
              projects:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - role
                        - projectId
                      properties:
                        projectId:
                          type: string
                          maxLength: 256
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                          example: ADMIN
                          description: >-
                            The project role that will be added to this Access
                            Group. \"null\" will remove this project level role.
                          nullable: true
              membersToAdd:
                allOf:
                  - description: List of members to add to the access group.
                    type: array
                    items:
                      type: string
                    example:
                      - usr_1a2b3c4d5e6f7g8h9i0j
                      - usr_2b3c4d5e6f7g8h9i0j1k
            required: true
            requiredProperties:
              - name
            additionalProperties: false
        examples:
          example:
            value:
              name: My access group
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
              membersToAdd:
                - usr_1a2b3c4d5e6f7g8h9i0j
                - usr_2b3c4d5e6f7g8h9i0j1k
    codeSamples:
      - label: createAccessGroup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.CreateAccessGroup(ctx, nil, nil, &operations.CreateAccessGroupRequestBody{\n        Name: \"My access group\",\n        Projects: []operations.CreateAccessGroupProjects{\n            operations.CreateAccessGroupProjects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.CreateAccessGroupRoleAdmin.ToPointer(),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createAccessGroup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.createAccessGroup({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "My access group",
                projects: [
                  {
                    projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                    role: "ADMIN",
                  },
                ],
                membersToAdd: [
                  "usr_1a2b3c4d5e6f7g8h9i0j",
                  "usr_2b3c4d5e6f7g8h9i0j1k",
                ],
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              entitlements:
                allOf:
                  - items:
                      type: string
                      enum:
                        - v0
                    type: array
              membersCount:
                allOf:
                  - type: number
              projectsCount:
                allOf:
                  - type: number
              name:
                allOf:
                  - type: string
                    description: The name of this access group.
                    example: my-access-group
              createdAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was
                      created.
                    example: 1588720733602
              teamId:
                allOf:
                  - type: string
                    description: ID of the team that this access group belongs to.
                    example: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was last
                      updated.
                    example: 1588720733602
              accessGroupId:
                allOf:
                  - type: string
                    description: ID of the access group.
                    example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              teamRoles:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Roles that the team has in the access group.
                    example:
                      - DEVELOPER
                      - BILLING
              teamPermissions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Permissions that the team has in the access group.
                    example:
                      - CreateProject
            requiredProperties:
              - entitlements
              - membersCount
              - projectsCount
              - name
              - createdAt
              - teamId
              - updatedAt
              - accessGroupId
        examples:
          example:
            value:
              entitlements:
                - v0
              membersCount: 123
              projectsCount: 123
              name: my-access-group
              createdAt: 1588720733602
              teamId: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt: 1588720733602
              accessGroupId: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              teamRoles:
                - DEVELOPER
                - BILLING
              teamPermissions:
                - CreateProject
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete an access group project"

last_updated: "2025-11-07T00:37:04.483Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/delete-an-access-group-project"
--------------------------------------------------------------------------------

# Delete an access group project

> Allows deletion of an access group project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
paths:
  path: /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        accessGroupIdOrName:
          schema:
            - type: string
              required: true
        projectId:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteAccessGroupProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.accessGroups.deleteAccessGroupProject({
              accessGroupIdOrName: "ag_1a2b3c4d5e6f7g8h9i0j",
              projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '200': {}
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Deletes an access group"

last_updated: "2025-11-07T00:37:07.634Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/deletes-an-access-group"
--------------------------------------------------------------------------------

# Deletes an access group

> Allows to delete an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/access-groups/{idOrName}
paths:
  path: /v1/access-groups/{idOrName}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteAccessGroup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.DeleteAccessGroup(ctx, \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: deleteAccessGroup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            await vercel.accessGroups.deleteAccessGroup({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });


          }

          run();
  response:
    '200': {}
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "List access groups for a team, project or member"

last_updated: "2025-11-07T00:37:04.525Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/list-access-groups-for-a-team-project-or-member"
--------------------------------------------------------------------------------

# List access groups for a team, project or member

> List access groups

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups
paths:
  path: /v1/access-groups
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        projectId:
          schema:
            - type: string
              description: Filter access groups by project.
              example: prj_pavWOn1iLObbx3RowVvzmPrTWyTf
        search:
          schema:
            - type: string
              description: Search for access groups by name.
              example: example
        membersLimit:
          schema:
            - type: integer
              description: Number of members to include in the response.
              maximum: 100
              minimum: 1
              example: 20
        projectsLimit:
          schema:
            - type: integer
              description: Number of projects to include in the response.
              maximum: 100
              minimum: 1
              example: 20
        limit:
          schema:
            - type: integer
              description: Limit how many access group should be returned.
              maximum: 100
              minimum: 1
              example: 20
        next:
          schema:
            - type: string
              description: Continuation cursor to retrieve the next page of results.
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listAccessGroups
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.ListAccessGroups(ctx, operations.ListAccessGroupsRequest{\n        ProjectID: vercel.String(\"prj_pavWOn1iLObbx3RowVvzmPrTWyTf\"),\n        Search: vercel.String(\"example\"),\n        MembersLimit: vercel.Int64(20),\n        ProjectsLimit: vercel.Int64(20),\n        Limit: vercel.Int64(20),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.OneOf != nil {\n        // handle response\n    }\n}"
      - label: listAccessGroups
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.listAccessGroups({
              projectId: "prj_pavWOn1iLObbx3RowVvzmPrTWyTf",
              search: "example",
              membersLimit: 20,
              projectsLimit: 20,
              limit: 20,
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
          - type: object
            properties:
              accessGroups:
                allOf:
                  - items:
                      properties:
                        members:
                          items:
                            type: string
                          type: array
                        projects:
                          items:
                            type: string
                          type: array
                        entitlements:
                          items:
                            type: string
                          type: array
                        teamPermissions:
                          items:
                            type: string
                          type: array
                        isDsyncManaged:
                          type: boolean
                        name:
                          type: string
                          description: The name of this access group.
                          example: my-access-group
                        createdAt:
                          type: string
                          description: >-
                            Timestamp in milliseconds when the access group was
                            created.
                          example: 1588720733602
                        teamId:
                          type: string
                          description: ID of the team that this access group belongs to.
                          example: team_123a6c5209bc3778245d011443644c8d27dc2c50
                        updatedAt:
                          type: string
                          description: >-
                            Timestamp in milliseconds when the access group was
                            last updated.
                          example: 1588720733602
                        accessGroupId:
                          type: string
                          description: ID of the access group.
                          example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
                        membersCount:
                          type: number
                          description: Number of members in the access group.
                          example: 5
                        projectsCount:
                          type: number
                          description: Number of projects in the access group.
                          example: 2
                        teamRoles:
                          items:
                            type: string
                          type: array
                          description: Roles that the team has in the access group.
                          example:
                            - DEVELOPER
                            - BILLING
                      required:
                        - isDsyncManaged
                        - name
                        - createdAt
                        - teamId
                        - updatedAt
                        - accessGroupId
                        - membersCount
                        - projectsCount
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      count:
                        type: number
                      next:
                        nullable: true
                        type: string
                    required:
                      - count
                      - next
                    type: object
            requiredProperties:
              - accessGroups
              - pagination
        examples:
          example:
            value: {}
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "List members of an access group"

last_updated: "2025-11-07T00:37:04.469Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/list-members-of-an-access-group"
--------------------------------------------------------------------------------

# List members of an access group

> List members of an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}/members
paths:
  path: /v1/access-groups/{idOrName}/members
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
              description: The ID or name of the Access Group.
              example: ag_pavWOn1iLObbXLRiwVvzmPrTWyTf
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Limit how many access group members should be returned.
              maximum: 100
              minimum: 1
              example: 20
        next:
          schema:
            - type: string
              required: false
              description: Continuation cursor to retrieve the next page of results.
        search:
          schema:
            - type: string
              required: false
              description: Search project members by their name, username, and email.
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listAccessGroupMembers
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.ListAccessGroupMembers(ctx, operations.ListAccessGroupMembersRequest{\n        IDOrName: \"ag_pavWOn1iLObbXLRiwVvzmPrTWyTf\",\n        Limit: vercel.Int64(20),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAccessGroupMembers
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.listAccessGroupMembers({
              idOrName: "ag_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              limit: 20,
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              members:
                allOf:
                  - items:
                      properties:
                        avatar:
                          type: string
                        email:
                          type: string
                        uid:
                          type: string
                        username:
                          type: string
                        name:
                          type: string
                        createdAt:
                          type: string
                        teamRole:
                          type: string
                          enum:
                            - OWNER
                            - MEMBER
                            - DEVELOPER
                            - SECURITY
                            - BILLING
                            - VIEWER
                            - VIEWER_FOR_PLUS
                            - CONTRIBUTOR
                      required:
                        - email
                        - uid
                        - username
                        - teamRole
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      count:
                        type: number
                      next:
                        nullable: true
                        type: string
                    required:
                      - count
                      - next
                    type: object
            requiredProperties:
              - members
              - pagination
        examples:
          example:
            value:
              members:
                - avatar: <string>
                  email: <string>
                  uid: <string>
                  username: <string>
                  name: <string>
                  createdAt: <string>
                  teamRole: OWNER
              pagination:
                count: 123
                next: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "List projects of an access group"

last_updated: "2025-11-07T00:37:07.453Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/list-projects-of-an-access-group"
--------------------------------------------------------------------------------

# List projects of an access group

> List projects of an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}/projects
paths:
  path: /v1/access-groups/{idOrName}/projects
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
              description: The ID or name of the Access Group.
              example: ag_pavWOn1iLObbXLRiwVvzmPrTWyTf
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Limit how many access group projects should be returned.
              maximum: 100
              minimum: 1
              example: 20
        next:
          schema:
            - type: string
              required: false
              description: Continuation cursor to retrieve the next page of results.
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: listAccessGroupProjects
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.ListAccessGroupProjects(ctx, operations.ListAccessGroupProjectsRequest{\n        IDOrName: \"ag_pavWOn1iLObbXLRiwVvzmPrTWyTf\",\n        Limit: vercel.Int64(20),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: listAccessGroupProjects
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.listAccessGroupProjects({
              idOrName: "ag_pavWOn1iLObbXLRiwVvzmPrTWyTf",
              limit: 20,
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              projects:
                allOf:
                  - items:
                      properties:
                        projectId:
                          type: string
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_DEVELOPER
                            - PROJECT_VIEWER
                        createdAt:
                          type: string
                        updatedAt:
                          type: string
                        project:
                          properties:
                            name:
                              type: string
                            framework:
                              nullable: true
                              type: string
                            latestDeploymentId:
                              type: string
                          type: object
                      required:
                        - projectId
                        - role
                        - createdAt
                        - updatedAt
                        - project
                      type: object
                    type: array
              pagination:
                allOf:
                  - properties:
                      count:
                        type: number
                      next:
                        nullable: true
                        type: string
                    required:
                      - count
                      - next
                    type: object
            requiredProperties:
              - projects
              - pagination
        examples:
          example:
            value:
              projects:
                - projectId: <string>
                  role: ADMIN
                  createdAt: <string>
                  updatedAt: <string>
                  project:
                    name: <string>
                    framework: <string>
                    latestDeploymentId: <string>
              pagination:
                count: 123
                next: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Reads an access group"

last_updated: "2025-11-07T00:37:04.697Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/reads-an-access-group"
--------------------------------------------------------------------------------

# Reads an access group

> Allows to read an access group

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}
paths:
  path: /v1/access-groups/{idOrName}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: readAccessGroup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.ReadAccessGroup(ctx, \"<value>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: readAccessGroup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.readAccessGroup({
              idOrName: "ag_1a2b3c4d5e6f7g8h9i0j",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              teamPermissions:
                allOf:
                  - items:
                      type: string
                      enum:
                        - IntegrationManager
                        - CreateProject
                        - FullProductionDeployment
                        - UsageViewer
                        - EnvVariableManager
                        - EnvironmentManager
                        - V0Builder
                        - V0Chatter
                        - V0Viewer
                    type: array
              entitlements:
                allOf:
                  - items:
                      type: string
                      enum:
                        - v0
                    type: array
              isDsyncManaged:
                allOf:
                  - type: boolean
              name:
                allOf:
                  - type: string
                    description: The name of this access group.
                    example: my-access-group
              createdAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was
                      created.
                    example: 1588720733602
              teamId:
                allOf:
                  - type: string
                    description: ID of the team that this access group belongs to.
                    example: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was last
                      updated.
                    example: 1588720733602
              accessGroupId:
                allOf:
                  - type: string
                    description: ID of the access group.
                    example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              membersCount:
                allOf:
                  - type: number
                    description: Number of members in the access group.
                    example: 5
              projectsCount:
                allOf:
                  - type: number
                    description: Number of projects in the access group.
                    example: 2
              teamRoles:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Roles that the team has in the access group.
                    example:
                      - DEVELOPER
                      - BILLING
            requiredProperties:
              - isDsyncManaged
              - name
              - createdAt
              - teamId
              - updatedAt
              - accessGroupId
              - membersCount
              - projectsCount
        examples:
          example:
            value:
              teamPermissions:
                - IntegrationManager
              entitlements:
                - v0
              isDsyncManaged: true
              name: my-access-group
              createdAt: 1588720733602
              teamId: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt: 1588720733602
              accessGroupId: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              membersCount: 5
              projectsCount: 2
              teamRoles:
                - DEVELOPER
                - BILLING
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Reads an access group project"

last_updated: "2025-11-07T00:37:07.506Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/reads-an-access-group-project"
--------------------------------------------------------------------------------

# Reads an access group project

> Allows reading an access group project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
paths:
  path: /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        accessGroupIdOrName:
          schema:
            - type: string
              required: true
        projectId:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: readAccessGroupProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.readAccessGroupProject({
              accessGroupIdOrName: "ag_1a2b3c4d5e6f7g8h9i0j",
              projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              teamId:
                allOf:
                  - type: string
              accessGroupId:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - PROJECT_DEVELOPER
                      - PROJECT_VIEWER
              createdAt:
                allOf:
                  - type: string
              updatedAt:
                allOf:
                  - type: string
            requiredProperties:
              - teamId
              - accessGroupId
              - projectId
              - role
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              teamId: <string>
              accessGroupId: <string>
              projectId: <string>
              role: ADMIN
              createdAt: <string>
              updatedAt: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update an access group"

last_updated: "2025-11-07T00:37:07.172Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group"
--------------------------------------------------------------------------------

# Update an access group

> Allows to update an access group metadata

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups/{idOrName}
paths:
  path: /v1/access-groups/{idOrName}
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrName:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The name of the access group
                    maxLength: 50
                    pattern: ^[A-z0-9_ -]+$
                    example: My access group
              projects:
                allOf:
                  - type: array
                    items:
                      type: object
                      additionalProperties: false
                      required:
                        - role
                        - projectId
                      properties:
                        projectId:
                          type: string
                          maxLength: 256
                          example: prj_ndlgr43fadlPyCtREAqxxdyFK
                          description: The ID of the project.
                        role:
                          type: string
                          enum:
                            - ADMIN
                            - PROJECT_VIEWER
                            - PROJECT_DEVELOPER
                            - null
                          example: ADMIN
                          description: >-
                            The project role that will be added to this Access
                            Group. \"null\" will remove this project level role.
                          nullable: true
              membersToAdd:
                allOf:
                  - description: List of members to add to the access group.
                    type: array
                    items:
                      type: string
                    example:
                      - usr_1a2b3c4d5e6f7g8h9i0j
                      - usr_2b3c4d5e6f7g8h9i0j1k
              membersToRemove:
                allOf:
                  - description: List of members to remove from the access group.
                    type: array
                    items:
                      type: string
                    example:
                      - usr_1a2b3c4d5e6f7g8h9i0j
                      - usr_2b3c4d5e6f7g8h9i0j1k
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              name: My access group
              projects:
                - projectId: prj_ndlgr43fadlPyCtREAqxxdyFK
                  role: ADMIN
              membersToAdd:
                - usr_1a2b3c4d5e6f7g8h9i0j
                - usr_2b3c4d5e6f7g8h9i0j1k
              membersToRemove:
                - usr_1a2b3c4d5e6f7g8h9i0j
                - usr_2b3c4d5e6f7g8h9i0j1k
    codeSamples:
      - label: updateAccessGroup
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.AccessGroups.UpdateAccessGroup(ctx, \"<value>\", nil, nil, &operations.UpdateAccessGroupRequestBody{\n        Name: vercel.String(\"My access group\"),\n        Projects: []operations.Projects{\n            operations.Projects{\n                ProjectID: \"prj_ndlgr43fadlPyCtREAqxxdyFK\",\n                Role: operations.RoleAdmin.ToPointer(),\n            },\n        },\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: updateAccessGroup
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.updateAccessGroup({
              idOrName: "<value>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                name: "My access group",
                projects: [
                  {
                    projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
                    role: "ADMIN",
                  },
                ],
                membersToAdd: [
                  "usr_1a2b3c4d5e6f7g8h9i0j",
                  "usr_2b3c4d5e6f7g8h9i0j1k",
                ],
                membersToRemove: [
                  "usr_1a2b3c4d5e6f7g8h9i0j",
                  "usr_2b3c4d5e6f7g8h9i0j1k",
                ],
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              entitlements:
                allOf:
                  - items:
                      type: string
                      enum:
                        - v0
                    type: array
              name:
                allOf:
                  - type: string
                    description: The name of this access group.
                    example: my-access-group
              createdAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was
                      created.
                    example: 1588720733602
              teamId:
                allOf:
                  - type: string
                    description: ID of the team that this access group belongs to.
                    example: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt:
                allOf:
                  - type: string
                    description: >-
                      Timestamp in milliseconds when the access group was last
                      updated.
                    example: 1588720733602
              accessGroupId:
                allOf:
                  - type: string
                    description: ID of the access group.
                    example: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              membersCount:
                allOf:
                  - type: number
                    description: Number of members in the access group.
                    example: 5
              projectsCount:
                allOf:
                  - type: number
                    description: Number of projects in the access group.
                    example: 2
              teamRoles:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Roles that the team has in the access group.
                    example:
                      - DEVELOPER
                      - BILLING
              teamPermissions:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: Permissions that the team has in the access group.
                    example:
                      - CreateProject
            requiredProperties:
              - entitlements
              - name
              - createdAt
              - teamId
              - updatedAt
              - accessGroupId
              - membersCount
              - projectsCount
        examples:
          example:
            value:
              entitlements:
                - v0
              name: my-access-group
              createdAt: 1588720733602
              teamId: team_123a6c5209bc3778245d011443644c8d27dc2c50
              updatedAt: 1588720733602
              accessGroupId: ag_123a6c5209bc3778245d011443644c8d27dc2c50
              membersCount: 5
              projectsCount: 2
              teamRoles:
                - DEVELOPER
                - BILLING
              teamPermissions:
                - CreateProject
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Update an access group project"

last_updated: "2025-11-07T00:37:04.438Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group-project"
--------------------------------------------------------------------------------

# Update an access group project

> Allows update of an access group project

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
paths:
  path: /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
  method: patch
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        accessGroupIdOrName:
          schema:
            - type: string
              required: true
        projectId:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - PROJECT_VIEWER
                      - PROJECT_DEVELOPER
                    example: ADMIN
                    description: The project role that will be added to this Access Group.
            required: true
            requiredProperties:
              - role
            additionalProperties: false
        examples:
          example:
            value:
              role: ADMIN
    codeSamples:
      - label: updateAccessGroupProject
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.accessGroups.updateAccessGroupProject({
              accessGroupIdOrName: "ag_1a2b3c4d5e6f7g8h9i0j",
              projectId: "prj_ndlgr43fadlPyCtREAqxxdyFK",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                role: "ADMIN",
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              teamId:
                allOf:
                  - type: string
              accessGroupId:
                allOf:
                  - type: string
              projectId:
                allOf:
                  - type: string
              role:
                allOf:
                  - type: string
                    enum:
                      - ADMIN
                      - PROJECT_DEVELOPER
                      - PROJECT_VIEWER
              createdAt:
                allOf:
                  - type: string
              updatedAt:
                allOf:
                  - type: string
            requiredProperties:
              - teamId
              - accessGroupId
              - projectId
              - role
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              teamId: <string>
              accessGroupId: <string>
              projectId: <string>
              role: ADMIN
              createdAt: <string>
              updatedAt: <string>
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Assign an Alias"

last_updated: "2025-11-07T00:37:04.077Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/aliases/assign-an-alias"
--------------------------------------------------------------------------------

# Assign an Alias

> Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/deployments/{id}/aliases
paths:
  path: /v2/deployments/{id}/aliases
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the deployment the aliases should be listed for
              example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              alias:
                allOf:
                  - description: >-
                      The alias we want to assign to the deployment defined in
                      the URL
                    example: my-alias.vercel.app
                    type: string
              redirect:
                allOf:
                  - description: >-
                      The redirect property will take precedence over the
                      deployment id from the URL and consists of a hostname
                      (like test.com) to which the alias should redirect using
                      status code 307
                    example: null
                    type: string
                    nullable: true
            required: true
        examples:
          example:
            value:
              alias: my-alias.vercel.app
              redirect: null
    codeSamples:
      - label: assignAlias
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.AssignAlias(ctx, \"<id>\", nil, nil, &operations.AssignAliasRequestBody{\n        Alias: vercel.String(\"my-alias.vercel.app\"),\n        Redirect: nil,\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: assignAlias
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.assignAlias({
              id: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                alias: "my-alias.vercel.app",
                redirect: null,
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              uid:
                allOf:
                  - type: string
                    description: The unique identifier of the alias
                    example: 2WjyKQmM8ZnGcJsPWMrHRHrE
              alias:
                allOf:
                  - type: string
                    description: The assigned alias name
                    example: my-alias.vercel.app
              created:
                allOf:
                  - type: string
                    format: date-time
                    description: The date when the alias was created
                    example: '2017-04-26T23:00:34.232Z'
              oldDeploymentId:
                allOf:
                  - nullable: true
                    type: string
                    description: >-
                      The unique identifier of the previously aliased
                      deployment, only received when the alias was used before
                    example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
            requiredProperties:
              - uid
              - alias
              - created
        examples:
          example:
            value:
              uid: 2WjyKQmM8ZnGcJsPWMrHRHrE
              alias: my-alias.vercel.app
              created: '2017-04-26T23:00:34.232Z'
              oldDeploymentId: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
        description: The alias was successfully assigned to the deployment
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              One of the provided values in the request body is invalid.
              One of the provided values in the request query is invalid.
              The cert for the provided alias is not ready
              The deployment is not READY and can not be aliased
              The supplied alias is invalid
        examples: {}
        description: |-
          One of the provided values in the request body is invalid.
          One of the provided values in the request query is invalid.
          The cert for the provided alias is not ready
          The deployment is not READY and can not be aliased
          The supplied alias is invalid
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '402':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The account was soft-blocked for an unhandled reason.
              The account is missing a payment so payment method must be updated
        examples: {}
        description: |-
          The account was soft-blocked for an unhandled reason.
          The account is missing a payment so payment method must be updated
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              You do not have permission to access this resource.
              If no .vercel.app alias exists then we fail (nothing to mirror)
        examples: {}
        description: |-
          You do not have permission to access this resource.
          If no .vercel.app alias exists then we fail (nothing to mirror)
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The domain used for the alias was not found
              The deployment was not found
        examples: {}
        description: |-
          The domain used for the alias was not found
          The deployment was not found
    '409':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: |-
              The provided alias is already assigned to the given deployment
              The domain is not allowed to be used
        examples: {}
        description: |-
          The provided alias is already assigned to the given deployment
          The domain is not allowed to be used
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Delete an Alias"

last_updated: "2025-11-07T00:37:04.503Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/aliases/delete-an-alias"
--------------------------------------------------------------------------------

# Delete an Alias

> Delete an Alias with the specified ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v2/aliases/{aliasId}
paths:
  path: /v2/aliases/{aliasId}
  method: delete
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        aliasId:
          schema:
            - type: string
              required: true
              description: The ID or alias that will be removed
              example: 2WjyKQmM8ZnGcJsPWMrHRHrE
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: deleteAlias
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.DeleteAlias(ctx, \"<id>\", nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: deleteAlias
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.deleteAlias({
              aliasId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    enum:
                      - SUCCESS
            requiredProperties:
              - status
        examples:
          example:
            value:
              status: SUCCESS
        description: The alias was successfully removed
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The alias was not found
        examples: {}
        description: The alias was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "Get an Alias"

last_updated: "2025-11-07T00:37:06.956Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/aliases/get-an-alias"
--------------------------------------------------------------------------------

# Get an Alias

> Retrieves an Alias for the given host name or alias ID.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/aliases/{idOrAlias}
paths:
  path: /v4/aliases/{idOrAlias}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        idOrAlias:
          schema:
            - type: string
              required: true
              description: The alias or alias ID to be retrieved
              example: example.vercel.app
      query:
        from:
          schema:
            - type: number
              required: false
              description: >-
                Get the alias only if it was created after the provided
                timestamp
              deprecated: true
              example: 1540095775951
        projectId:
          schema:
            - type: string
              required: false
              description: Get the alias only if it is assigned to the provided project ID
              example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
        since:
          schema:
            - type: number
              required: false
              description: >-
                Get the alias only if it was created after this JavaScript
                timestamp
              example: 1540095775941
        until:
          schema:
            - type: number
              required: false
              description: >-
                Get the alias only if it was created before this JavaScript
                timestamp
              example: 1540095775951
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getAlias
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"github.com/vercel/vercel/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Aliases.GetAlias(ctx, operations.GetAliasRequest{\n        From: vercel.Float64(1540095775951),\n        IDOrAlias: \"example.vercel.app\",\n        ProjectID: vercel.String(\"prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB\"),\n        Since: vercel.Float64(1540095775941),\n        Until: vercel.Float64(1540095775951),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: getAlias
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.aliases.getAlias({
              from: 1540095775951,
              idOrAlias: "example.vercel.app",
              projectId: "prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB",
              since: 1540095775941,
              until: 1540095775951,
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - properties:
                    alias:
                      type: string
                      description: >-
                        The alias name, it could be a `.vercel.app` subdomain or
                        a custom domain
                      example: my-alias.vercel.app
                    created:
                      type: string
                      format: date-time
                      description: The date when the alias was created
                      example: '2017-04-26T23:00:34.232Z'
                    createdAt:
                      type: number
                      description: >-
                        The date when the alias was created in milliseconds
                        since the UNIX epoch
                      example: 1540095775941
                    creator:
                      properties:
                        uid:
                          type: string
                          description: ID of the user who created the alias
                          example: 96SnxkFiMyVKsK3pnoHfx3Hz
                        email:
                          type: string
                          description: Email of the user who created the alias
                          example: john-doe@gmail.com
                        username:
                          type: string
                          description: Username of the user who created the alias
                          example: john-doe
                      required:
                        - uid
                        - email
                        - username
                      type: object
                      description: Information of the user who created the alias
                    deletedAt:
                      type: number
                      description: >-
                        The date when the alias was deleted in milliseconds
                        since the UNIX epoch
                      example: 1540095775941
                    deployment:
                      properties:
                        id:
                          type: string
                          description: The deployment unique identifier
                          example: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                        url:
                          type: string
                          description: The deployment unique URL
                          example: my-instant-deployment-3ij3cxz9qr.now.sh
                        meta:
                          type: string
                          description: The deployment metadata
                          example: {}
                      required:
                        - id
                        - url
                      type: object
                      description: A map with the deployment ID, URL and metadata
                    deploymentId:
                      nullable: true
                      type: string
                      description: The deployment ID
                      example: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                    projectId:
                      nullable: true
                      type: string
                      description: The unique identifier of the project
                      example: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                    redirect:
                      nullable: true
                      type: string
                      description: >-
                        Target destination domain for redirect when the alias is
                        a redirect
                    redirectStatusCode:
                      nullable: true
                      type: number
                      enum:
                        - 301
                        - 302
                        - 307
                        - 308
                      description: Status code to be used on redirect
                    uid:
                      type: string
                      description: The unique identifier of the alias
                    updatedAt:
                      type: number
                      description: >-
                        The date when the alias was updated in milliseconds
                        since the UNIX epoch
                      example: 1540095775941
                    protectionBypass:
                      additionalProperties:
                        oneOf:
                          - properties:
                              createdAt:
                                type: number
                              createdBy:
                                type: string
                              scope:
                                type: string
                                enum:
                                  - shareable-link
                              expires:
                                type: number
                            required:
                              - createdAt
                              - createdBy
                              - scope
                            type: object
                            description: The protection bypass for the alias
                          - properties:
                              createdAt:
                                type: number
                              lastUpdatedAt:
                                type: number
                              lastUpdatedBy:
                                type: string
                              access:
                                type: string
                                enum:
                                  - requested
                                  - granted
                              scope:
                                type: string
                                enum:
                                  - user
                            required:
                              - createdAt
                              - lastUpdatedAt
                              - lastUpdatedBy
                              - access
                              - scope
                            type: object
                            description: The protection bypass for the alias
                          - properties:
                              createdAt:
                                type: number
                              createdBy:
                                type: string
                              scope:
                                type: string
                                enum:
                                  - alias-protection-override
                            required:
                              - createdAt
                              - createdBy
                              - scope
                            type: object
                            description: The protection bypass for the alias
                          - properties:
                              createdAt:
                                type: number
                              lastUpdatedAt:
                                type: number
                              lastUpdatedBy:
                                type: string
                              scope:
                                type: string
                                enum:
                                  - email_invite
                            required:
                              - createdAt
                              - lastUpdatedAt
                              - lastUpdatedBy
                              - scope
                            type: object
                            description: The protection bypass for the alias
                      type: object
                      description: The protection bypass for the alias
                    microfrontends:
                      properties:
                        defaultApp:
                          properties:
                            projectId:
                              type: string
                          required:
                            - projectId
                          type: object
                        applications:
                          oneOf:
                            - items:
                                properties:
                                  fallbackHost:
                                    type: string
                                    description: >-
                                      This is always set. In production it is
                                      used as a pointer to each apps production
                                      deployment. For pre-production, it's used
                                      as the fallback if there is no deployment
                                      for the branch.
                                  projectId:
                                    type: string
                                    description: >-
                                      The project ID of the microfrontends
                                      application.
                                required:
                                  - fallbackHost
                                  - projectId
                                type: object
                                description: >-
                                  A list of the deployment routing information
                                  for each project.
                              type: array
                              description: >-
                                A list of the deployment routing information for
                                each project.
                            - items:
                                properties:
                                  fallbackHost:
                                    type: string
                                    description: >-
                                      This is always set. For branch aliases,
                                      it's used as the fallback if there is no
                                      deployment for the branch.
                                  branchAlias:
                                    type: string
                                    description: >-
                                      Could point to a branch without a
                                      deployment if the project was never
                                      deployed. The proxy will fallback to the
                                      fallbackHost if there is no deployment.
                                  projectId:
                                    type: string
                                    description: >-
                                      The project ID of the microfrontends
                                      application.
                                required:
                                  - fallbackHost
                                  - branchAlias
                                  - projectId
                                type: object
                                description: >-
                                  A list of the deployment routing information
                                  for each project.
                              type: array
                              description: >-
                                A list of the deployment routing information for
                                each project.
                            - items:
                                properties:
                                  deploymentId:
                                    type: string
                                    description: >-
                                      This is the deployment for the same
                                      commit, it could be a cancelled
                                      deployment. The proxy will fallback to the
                                      branchDeploymentId and then the
                                      fallbackDeploymentId.
                                  branchDeploymentId:
                                    type: string
                                    description: >-
                                      This is the latest non-cancelled
                                      deployment of the branch alias at the time
                                      the commit alias was created. It is
                                      possible there is no deployment for the
                                      branch, or this was set before the
                                      deployment was canceled, in which case
                                      this will point to a cancelled deployment,
                                      in either case the proxy will fallback to
                                      the fallbackDeploymentId.
                                  fallbackDeploymentId:
                                    type: string
                                    description: >-
                                      This is the deployment of the fallback
                                      host at the time the commit alias was
                                      created. It is possible for this to be a
                                      deleted deployment, in which case the
                                      proxy will show that the deployment is
                                      deleted. It will not use the fallbackHost,
                                      as a future deployment on the fallback
                                      host could be invalid for this deployment,
                                      and it could lead to confusion / incorrect
                                      behavior for the commit alias.
                                  fallbackHost:
                                    type: string
                                    description: >-
                                      Temporary for backwards compatibility. Can
                                      remove when metadata change is released
                                  branchAlias:
                                    type: string
                                  projectId:
                                    type: string
                                    description: >-
                                      The project ID of the microfrontends
                                      application.
                                required:
                                  - projectId
                                type: object
                                description: >-
                                  A list of the deployment routing information
                                  for each project.
                              type: array
                              description: >-
                                A list of the deployment routing information for
                                each project.
                      required:
                        - defaultApp
                        - applications
                      type: object
                      description: >-
                        The microfrontends for the alias including the routing
                        configuration
                  required:
                    - alias
                    - created
                    - deploymentId
                    - projectId
                    - uid
                  type: object
        examples:
          example:
            value:
              - alias: my-alias.vercel.app
                created: '2017-04-26T23:00:34.232Z'
                createdAt: 1540095775941
                creator:
                  uid: 96SnxkFiMyVKsK3pnoHfx3Hz
                  email: john-doe@gmail.com
                  username: john-doe
                deletedAt: 1540095775941
                deployment:
                  id: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                  url: my-instant-deployment-3ij3cxz9qr.now.sh
                  meta: {}
                deploymentId: dpl_5m8CQaRBm3FnWRW1od3wKTpaECPx
                projectId: prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                redirect: <string>
                redirectStatusCode: 301
                uid: <string>
                updatedAt: 1540095775941
                protectionBypass: {}
                microfrontends:
                  defaultApp:
                    projectId: <string>
                  applications:
                    - fallbackHost: <string>
                      projectId: <string>
        description: The alias information
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request query is invalid.
        examples: {}
        description: One of the provided values in the request query is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The alias was not found
        examples: {}
        description: The alias was not found
  deprecated: false
  type: path
components:
  schemas: {}

````

--------------------------------------------------------------------------------
title: "List aliases"

last_updated: "2025-11-07T00:37:04.515Z"
source: "https://vercel.com/docs/rest-api/reference/endpoints/aliases/list-aliases"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./16-são-paulo-brazil-gru1-pricing.md) | [Index](./index.md) | [Next →](./18-list-aliases.md)
