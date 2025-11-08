**Navigation:** [← Previous](./07-aws-marketplace.md) | [Index](./index.md) | [Next →](./09-set-up-sso-with-okta.md)

# HIPAA Projects



You can use Supabase to store and process Protected Health Information (PHI). If you want to start developing healthcare apps on Supabase, reach out to the Supabase team [here](https://forms.supabase.com/hipaa2) to sign the Business Associate Agreement (BAA).

<Admonition type="note">
  Organizations must have a signed BAA with Supabase and have the Health Insurance Portability and Accountability Act (HIPAA) add-on enabled when dealing with PHI.
</Admonition>



## Configuring a HIPAA project

When the HIPAA add-on is enabled on an organization, projects within the organization can be configured as *High Compliance*. This configuration can be found in the [General Project Settings page](/dashboard/project/_/settings) of the dashboard.
Once enabled, additional security checks will be run against the project to ensure the deployed configuration is compliant. These checks are performed on a continual basis and security warnings will appear in the [Security Advisor](/dashboard/project/_/advisors/security) if a non-compliant setting is detected.

The required project configuration is outlined in the [shared responsibility model](/docs/guides/deployment/shared-responsibility-model#managing-healthcare-data) for managing healthcare data.

These include:

*   Enabling [Point in Time Recovery](/docs/guides/platform/backups#point-in-time-recovery) which requires at least a [small compute add-on](/docs/guides/platform/compute-add-ons).
*   Turning on [SSL Enforcement](/docs/guides/platform/ssl-enforcement).
*   Enabling [Network Restrictions](/docs/guides/platform/network-restrictions).

Additional security checks and controls will be added as the security advisor is extended and additional security controls are made available.



# Dedicated IPv4 Address for Ingress

Attach an IPv4 address to your database

The Supabase IPv4 add-on provides a dedicated IPv4 address for your Postgres database connection. It can be configured in the [Add-ons Settings](/dashboard/project/_/settings/addons).



## Understanding IP addresses

The Internet Protocol (IP) addresses devices on the internet. There are two main versions:

*   **IPv4**: The older version, with a limited address space.
*   **IPv6**: The newer version, offering a much larger address space and the future-proof option.



## When you need the IPv4 add-on:

<Admonition type="caution">
  IPv4 addresses are guaranteed to be static for ingress traffic. If your database is making outbound connections, the outbound IP address is not static and cannot be guaranteed.
</Admonition>

*   When using the direct connection string in an IPv6-incompatible network instead of Supavisor or client libraries.
*   When you need a dedicated IP address for your direct connection string



## Enabling the IPv4 add-on

You can enable the IPv4 add-on in your project's [add-ons settings](/dashboard/project/_/settings/addons).

You can also manage the IPv4 add-on using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Get current IPv4 add-on status
curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/billing/addons" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"


# Enable IPv4 add-on
curl -X POST "https://api.supabase.com/v1/projects/$PROJECT_REF/addons" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "addon_type": "ipv4"
  }'


# Disable IPv4 add-on
curl -X DELETE "https://api.supabase.com/v1/projects/$PROJECT_REF/billing/addons/ipv4" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"
```

<Admonition type="caution">
  Note that direct database connections can experience a short amount of downtime when toggling the add-on due to DNS reconfiguration and propagation. Generally, this should be less than a minute.
</Admonition>



## Read replicas and IPv4 add-on

When using the add-on, each database (including read replicas) receives an IPv4 address. Each replica adds to the total IPv4 cost.



## Changes and updates

*   While the IPv4 address generally remains the same, actions like pausing/unpausing the project or enabling/disabling the add-on can lead to a new IPv4 address.



## Supabase and IPv6 compatibility

By default, Supabase Postgres use IPv6 addresses. If your system doesn't support IPv6, you have the following options:

1.  **Supavisor Connection Strings**: The Supavisor connection strings are IPv4-compatible alternatives to direct connections
2.  **Supabase Client Libraries**: These libraries are compatible with IPv4
3.  **Dedicated IPv4 Add-On (Pro Plans+)**: For a guaranteed IPv4 and static database address for the direct connection, enable this paid add-on.


### Checking your network IPv6 support

You can check if your personal network is IPv6 compatible at [https://test-ipv6.com](https://test-ipv6.com).


### Checking platforms for IPv6 support:

The majority of services are IPv6 compatible. However, there are a few prominent ones that only accept IPv4 connections:

*   [Retool](https://retool.com/)
*   [Vercel](https://vercel.com/)
*   [GitHub Actions](https://docs.github.com/en/actions)
*   [Render](https://render.com/)



## Finding your database's IP address

Use an IP lookup website or this command (replace `<PROJECT_REF>`):

```sh
nslookup db.<PROJECT_REF>.supabase.co
```



## Identifying your connections

The pooler and direct connection strings can be found in the [project connect page](/dashboard/project/_?showConnect=true):


#### Direct connection

IPv6 unless IPv4 Add-On is enabled

```sh

# Example direct connection string
postgresql://postgres:[YOUR-PASSWORD]@db.ajrbwkcuthywfihaarmflo.supabase.co:5432/postgres
```


#### Supavisor in transaction mode (port 6543)

Always uses an IPv4 address

```sh

# Example transaction string
postgresql://postgres.ajrbwkcuthywddfihrmflo:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```


#### Supavisor in session mode (port 5432)

Always uses an IPv4 address

```sh

# Example session string
postgresql://postgres.ajrbwkcuthywfddihrmflo:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
```



## Pricing

For a detailed breakdown of how charges are calculated, refer to [Manage IPv4 usage](/docs/guides/platform/manage-your-usage/ipv4).



# Manage your subscription




## Manage your subscription plan

To change your subscription plan

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Subscription Plan**
2.  Click **Change subscription plan**
3.  On the side panel, choose a subscription plan
4.  Follow the prompts


### Upgrade

Upgrades take effect immediately. During the process, you are informed of the associated costs.

<Image
  alt="Subscription upgrade modal"
  src={{
    light: '/docs/img/guides/platform/upgrade-to-pro-plan-modal--light.png',
    dark: '/docs/img/guides/platform/upgrade-to-pro-plan-modal--dark.png',
  }}
  className="max-w-[577px]"
  zoomable
/>

If you still have credits in your account, we will use the credits first before charging your card.


### Downgrade

Downgrades take effect immediately. During the process, you are informed of the implications.

<Image
  alt="Subscription downgrade modal"
  src={{
    light: '/docs/img/guides/platform/downgrade-to-free-plan-modal--light.png',
    dark: '/docs/img/guides/platform/downgrade-to-free-plan-modal--dark.png',
  }}
  className="max-w-[577px]"
  zoomable
/>


#### Credits upon downgrade

Upon subscription downgrade, any prepaid subscription fee will be credited back to your organization for unused time in the billing cycle. These credits do not expire and will be applied to future invoices.

**Example:**
If you start a Pro Plan subscription on January 1 and downgrade to the Free Plan on January 15, your organization will receive about 50% of the subscription fee as credits for the unused time between January 15 and January 31.

As stated in our [Terms of Service](/terms#1-fees), we do not offer refunds to the payment method on file.


#### Charges on downgrade

When you downgrade from a paid plan to the Free Plan, you will get credits for the unused time on the paid plan. However, you will also be charged for any excessive usage in the billing cycle.

The plan line item (e.g. Pro Plan) gets charged upfront, whereas all usage charges get charged in arrears, as we only know your usage by the end of the billing cycle. Excessive usage is charged whenever a billing cycle resets, so either when your monthly cycle resets, or whenever you do a plan change.

If you got charged after downgrading to the Free Plan, you had excessive usage in the previous billing cycle. You can check your invoices to see what exactly you were charged for.



## Manage your payment methods

You can add multiple payment methods, but only one can be active at a time.


### Add a payment method

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Payment Methods**
2.  Click **Add new card**
3.  Provide your credit card details
4.  Click **Add payment method**


### Delete a payment method

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Payment Methods**
2.  In the context menu of the payment method you want to delete, click **Delete card**
3.  Click **Confirm**


### Set a payment method as active

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Payment Methods**
2.  In the context menu of the payment method you want to delete, click **Use this card**
3.  Click **Confirm**



## Manage your billing details

You can update your billing email address, billing address and tax ID on the [organization's billing page](/dashboard/org/_/billing).

<Admonition type="note">
  Any changes made to your billing details will only be reflected in your upcoming invoices. Our payment provider cannot regenerate previous invoices.
</Admonition>



# Manage your usage



Each subpage breaks down a specific usage item and details what you're charged for, how costs are calculated, and how to optimize usage and reduce costs.

*   [Compute](/docs/guides/platform/manage-your-usage/compute)
*   [Read Replicas](/docs/guides/platform/manage-your-usage/read-replicas)
*   [Branching](/docs/guides/platform/manage-your-usage/branching)
*   [Egress](/docs/guides/platform/manage-your-usage/egress)
*   [Disk Size](/docs/guides/platform/manage-your-usage/disk-size)
*   [Disk Throughput](/docs/guides/platform/manage-your-usage/disk-throughput)
*   [Disk IOPS](/docs/guides/platform/manage-your-usage/disk-iops)
*   [Monthly Active Users](/docs/guides/platform/manage-your-usage/monthly-active-users)
*   [Monthly Active Third-Party Users](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party)
*   [Monthly Active SSO Users](/docs/guides/platform/manage-your-usage/monthly-active-users-sso)
*   [Storage Size](/docs/guides/platform/manage-your-usage/storage-size)
*   [Storage Image Transformations](/docs/guides/platform/manage-your-usage/storage-image-transformations)
*   [Edge Function Invocations](/docs/guides/platform/manage-your-usage/edge-function-invocations)
*   [Realtime Messages](/docs/guides/platform/manage-your-usage/realtime-messages)
*   [Realtime Peak Connections](/docs/guides/platform/manage-your-usage/realtime-peak-connections)
*   [Custom Domains](/docs/guides/platform/manage-your-usage/custom-domains)
*   [Point-in-Time Recovery](/docs/guides/platform/manage-your-usage/point-in-time-recovery)
*   [IPv4](/docs/guides/platform/manage-your-usage/ipv4)
*   [MFA Phone](/docs/guides/platform/manage-your-usage/advanced-mfa-phone)
*   [Log Drains](/docs/guides/platform/manage-your-usage/log-drains)



# Migrating to Supabase



Learn how to migrate to Supabase from another database service.



## Migration guides

<NavData data="migrationPages">
  {(migrationPages) => (
        <div className="grid grid-cols-[repeat(auto-fit,minmax(200px,1fr))] gap-6 mb-6 not-prose">
          {migrationPages.map((page) => (
            <Link href={`${page.url}`} key={page.url} passHref>
              <GlassPanel
                icon={page.icon}
                title={page.name}
                hasLightIcon={page.hasLightIcon}
                background={false}
                className="[&>div]:p-4"
              />
            </Link>
          ))}
        </div>
      )}
</NavData>



# Migrating within Supabase

Learn how to migrate from one Supabase project to another

If you are on a Paid Plan and have physical backups enabled, you should instead use the [Restore
to another project feature](/docs/guides/platform/clone-project).



## Database migration guides

If you need to migrate from one Supabase project to another, choose the appropriate guide below:


### Backup file from the dashboard (\*.backup)

Follow the [Restore dashboard backup guide](/docs/guides/platform/migrating-within-supabase/dashboard-restore)


### SQL backup files (\*.sql)

Follow the [Backup and Restore using the CLI guide](/docs/guides/platform/migrating-within-supabase/backup-restore)



## Transfer project to a different organization

Project migration is primarily for changing regions or upgrading to new major versions of the platform in some scenarios. If you need to move your project to a different organization without touching the infrastructure, see [project transfers](/docs/guides/platform/project-transfer).



# Multi-factor Authentication

Enable multi-factor authentication (MFA) to keep your account secure.

<Admonition type="note">
  This guide is for adding MFA to your Supabase user account. If you want to enable MFA for users in your Supabase project, refer to [**this guide**](/docs/guides/auth/auth-mfa) instead.
</Admonition>

Multi-factor authentication (MFA) adds an additional layer of security to your user account, by requiring a second factor to verify your user identity. Supabase allows users to enable MFA on their account and set it as a requirement for subsequent logins.



## Supported authentication factors

Currently, Supabase supports adding a unique time-based one-time password (TOTP) to your user account as an additional security factor. You can manage your TOTP factor using apps such as 1Password, Authy, Google Authenticator or Apple's Keychain.



## Enable MFA

You can enable MFA for your user account under your [Supabase account settings](/dashboard/account/security). Enabling MFA will result in all other user sessions to be automatically logged out and forced to sign-in again with MFA.

<Admonition type="note">
  Supabase does not return recovery codes. Instead, we recommend that you register a backup TOTP factor to use in an event that you lose access to your primary TOTP factor. Make sure you use a different device and app, or store the secret in a secure location different than your primary one.
</Admonition>

<Admonition type="caution">
  For security reasons, we will not be able to restore access to your account if you lose all your two-factor authentication credentials. Do register a backup factor if necessary.
</Admonition>



## Login with MFA

Once you've enabled MFA for your Supabase user account, you will be prompted to enter your second factor challenge code as seen in your preferred TOTP app.

If you are an organization owner and on the Pro, Team or Enterprise plan, you can enforce that all organization members [must have MFA enabled](/docs/guides/platform/org-mfa-enforcement).



## Disable MFA

You can disable MFA for your user account under your [Supabase account settings](/dashboard/account/security). On subsequent login attempts, you will not be prompted to enter a MFA code.

<Admonition type="caution">
  We strongly recommend that you do not disable MFA to avoid unauthorized access to your user account.
</Admonition>



# Network Restrictions



<Admonition type="note">
  If you can't find the Network Restrictions section at the bottom of your [Database Settings](/dashboard/project/_/database/settings), update your version of Postgres in the [Infrastructure Settings](/dashboard/project/_/settings/infrastructure).
</Admonition>

Each Supabase project comes with configurable restrictions on the IP ranges that are allowed to connect to Postgres and its pooler ("your database"). These restrictions are enforced before traffic reaches your database. If a connection is not restricted by IP, it still needs to authenticate successfully with valid database credentials.

If direct connections to your database [resolve to a IPv6 address](/dashboard/project/_/database/settings), you need to add both IPv4 and IPv6 CIDRs to the list of allowed CIDRs. Network Restrictions will be applied to all database connection routes, whether pooled or direct. You will need to add both the IPv4 and IPv6 networks you want to allow. There are two exceptions: If you have been granted an extension on the IPv6 migration OR if you have purchased the [IPv4 add-on](/dashboard/project/_/settings/addons), you need only add IPv4 CIDRs.



## To get started via the Dashboard:

Network restrictions can be configured in the [Database Settings](/dashboard/project/_/database/settings) page. Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling network restrictions.



## To get started via the Management API:

You can also manage network restrictions using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Get current network restrictions
curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/network-restrictions" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"


# Update network restrictions
curl -X POST "https://api.supabase.com/v1/projects/$PROJECT_REF/network-restrictions/apply" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "db_allowed_cidrs": [
      "192.168.0.1/24",
    ]
  }'
```



## To get started via the CLI:

1.  [Install](/docs/guides/cli) the Supabase CLI 1.22.0+.
2.  [Log in](/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3.  If your project was created before 23rd December 2022, it will need to be [upgraded to the latest Supabase version](/docs/guides/platform/migrating-and-upgrading-projects) before Network Restrictions can be used.
4.  Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling network restrictions.


### Check restrictions

You can use the `get` subcommand of the CLI to retrieve the restrictions currently in effect.

If restrictions have been applied, the output of the `get` command will reflect the IP ranges allowed to connect:

```bash
> supabase network-restrictions --project-ref {ref} get --experimental
DB Allowed IPv4 CIDRs: &[183.12.1.1/24]
DB Allowed IPv6 CIDRs: &[2001:db8:3333:4444:5555:6666:7777:8888/64]
Restrictions applied successfully: true
```

If restrictions have never been applied to your project, the list of allowed CIDRs will be empty, but they will also not have been applied ("Restrictions applied successfully: false"). As a result, all IPs are allowed to connect to your database:

```bash
> supabase network-restrictions --project-ref {ref} get --experimental
DB Allowed IPv4 CIDRs: []
DB Allowed IPv6 CIDRs: []
Restrictions applied successfully: false
```


### Update restrictions

The `update` subcommand is used to apply network restrictions to your project:

```bash
> supabase network-restrictions --project-ref {ref} update --db-allow-cidr 183.12.1.1/24 --db-allow-cidr 2001:db8:3333:4444:5555:6666:7777:8888/64 --experimental
DB Allowed IPv4 CIDRs: &[183.12.1.1/24]
DB Allowed IPv6 CIDRs: &[2001:db8:3333:4444:5555:6666:7777:8888/64]
Restrictions applied successfully: true
```

The restrictions specified (in the form of CIDRs) replaces any restrictions that might have been applied in the past.
To add to the existing restrictions, you must include the existing restrictions within the list of CIDRs provided to the `update` command.


### Remove restrictions

To remove all restrictions on your project, you can use the `update` subcommand with the CIDR `0.0.0.0/0`:

```bash
> supabase network-restrictions --project-ref {ref} update --db-allow-cidr 0.0.0.0/0 --db-allow-cidr ::/0 --experimental
DB Allowed IPv4 CIDRs: &[0.0.0.0/0]
DB Allowed IPv6 CIDRs: &[::/0]
Restrictions applied successfully: true
```



## Limitations

*   The current iteration of Network Restrictions applies to connections to Postgres and the database pooler; it doesn't currently apply to APIs offered over HTTPS (e.g., PostgREST, Storage, and Auth). This includes using Supabase client libraries like [supabase-js](/docs/reference/javascript).
*   If network restrictions are enabled, direct access to your database from Edge Functions will always be blocked. Using the Supabase client library [supabase-js](/docs/reference/javascript) is recommended to connect to a database with network restrictions from Edge Functions.



# Performance Tuning



The Supabase platform automatically optimizes your Postgres database to take advantage of the compute resources of the plan your project is on. However, these optimizations are based on assumptions about the type of workflow the project is being utilized for, and it is likely that better results can be obtained by tuning the database for your particular workflow.



## Examining query performance

Unoptimized queries are a major cause of poor database performance. To analyze the performance of your queries, see the [Debugging and monitoring guide](/docs/guides/database/inspect).



## Optimizing the number of connections

The default connection limits for Postgres and Supavisor is based on your compute size. See the default connection numbers in the [Compute Add-ons](/docs/guides/platform/compute-add-ons) section.

If the number of connections is insufficient, you will receive the following error upon connecting to the DB:

```shell
$ psql -U postgres -h ...
FATAL: remaining connection slots are reserved for non-replication superuser connections
```

In such a scenario, you can consider:

*   [upgrading to a larger compute add-on](/dashboard/project/_/settings/compute-and-disk)
*   configuring your clients to use fewer connections
*   manually configuring the database for a higher number of connections


### Configuring clients to use fewer connections

You can use the [pg\_stat\_activity](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW) view to debug which clients are holding open connections on your DB. `pg_stat_activity` only exposes information on direct connections to the database. Information on the number of connections to Supavisor is available [via the metrics endpoint](../platform/metrics).

Depending on the clients involved, you might be able to configure them to work with fewer connections (e.g. by imposing a limit on the maximum number of connections they're allowed to use), or shift specific workloads to connect via [Supavisor](/docs/guides/database/connecting-to-postgres#connection-pooler) instead. Transient workflows, which can quickly scale up and down in response to traffic (e.g. serverless functions), can especially benefit from using a connection pooler rather than connecting to the DB directly.


### Allowing higher number of connections

You can configure Postgres connection limit among other parameters by using [Custom Postgres Config](/docs/guides/platform/custom-postgres-config#custom-postgres-config).


### Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need help tuning your database for your specific workflow.



# Permissions



The Supabase platform offers additional services (e.g. Storage) on top of the Postgres database that comes with each project. These services default to storing their operational data within your database, to ensure that you retain complete control over it.

However, these services assume a base level of access to their data, in order to e.g. be able to run migrations over it. Breaking these assumptions runs the risk of rendering these services inoperational for your project:

*   all entities under the `storage` schema are owned by `supabase_storage_admin`
*   all entities under the `auth` schema are owned by `supabase_auth_admin`

It is possible for violations of these assumptions to not cause an immediate outage, but take effect at a later time when a newer migration becomes available.



# PrivateLink



<Admonition type="note">
  PrivateLink is currently in alpha and available exclusively to Enterprise customers. Contact your account manager or [reach out to our team](/contact/enterprise) to enable this feature.
</Admonition>

PrivateLink provides enterprise-grade private network connectivity between your AWS VPC and your Supabase database using AWS VPC Lattice. This eliminates exposure to the public internet by creating a secure, private connection that keeps your database traffic within the AWS network backbone.

By enabling PrivateLink, database connections never traverse the public internet, enabling the disablement of public facing connectivity and providing an additional layer of security and compliance for sensitive workloads. This infrastructure-level security feature helps organizations meet strict data governance requirements and reduces potential attack vectors.



## How PrivateLink works

Supabase PrivateLink is an organisation level configuration. It works by sharing a [VPC Lattice Resource Configuration](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html) to any number of AWS Accounts for each of your Supabase projects. Connectivity can be achieved by either associating the Resource Configuration to a PrivateLink endpoint, or a [VPC Lattice Service Network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html). This means:

*   Database traffic flows through private AWS infrastructure only
*   Connection latency is typically reduced compared to public internet routing
*   Network isolation provides enhanced security posture
*   Attack surface is minimized by eliminating public exposure

The connection architecture changes from public internet routing to a dedicated private path through AWS's secure network backbone.

Supabase PrivateLink is currently just for direct database and PgBouncer connections only. It does not support other Supabase services like API, Storage, Auth, or Realtime. These services will continue to operate over public internet connections.



## Requirements

To use PrivateLink with your Supabase project:

*   Enterprise Supabase subscription
*   AWS VPC in the same region as your Supabase project
*   Appropriate permissions to accept Resource Shares, and create and manage endpoints



## Getting started


#### Step 1: Contact Supabase support

Reach out to your Enterprise account manager or [contact our team](/contact/enterprise) to initiate PrivateLink setup. During this initial contact, be prepared to provide:

*   Your Supabase organization slug
*   The specific projects you want to enable PrivateLink for (optional)
*   Your AWS Account ID(s)


#### Step 2: Accept resource share

Supabase will send you an AWS Resource Share containing the VPC Lattice Resource Configurations for your projects. To accept this share:

1.  Login to your AWS Management Console, ensure you are in the AWS region where your Supabase project is located
2.  Navigate to the AWS Resource Access Manager (RAM) console
    {/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}
3.  Go to [Shared with me > Resource shares](https://console.aws.amazon.com/ram/home#SharedResourceShares)
4.  Locate the resource share from Supabase.
    *   The resource share will have the format `cust-prod-[region]-pl-[organisation]-rc-share`
5.  Click on the resource share name to view details. Review the list of resource shares - it should only include resources of type vpc-lattice:ResourceConfiguration.
6.  Click **Accept resource share**
7.  Confirm the acceptance in the dialog box

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

After accepting, you'll see the resource configurations appear in your [Shared with me > Shared resources](https://console.aws.amazon.com/ram/home#SharedResources) section of the RAM console and the [PrivateLink and Lattice > Resource configurations](https://console.aws.amazon.com/vpcconsole/home#ResourceConfigs) section of the VPC console.


#### Step 3: Configure security groups

Ensure your security groups allow traffic on the appropriate ports:

1.  Navigate to the [VPC console > Security Groups](https://console.aws.amazon.com/vpcconsole/home#SecurityGroups:)
2.  Create a new security group for the endpoint or service network by clicking [Create security group](https://console.aws.amazon.com/vpcconsole/home#CreateSecurityGroup:)
3.  Give your security group a descriptive name and select the appropriate VPC
4.  Add an inbound rule for:
    *   Type: Postgres (TCP, port 5432)
    *   Destination that is appropriate for your network. i.e. the subnet of your VPC or security group of your application instances
5.  Finish creating the security group by clicking **Create security group**


#### Step 4: Create connection

In your AWS account, you have two options to establish connectivity:


##### Option A: Create a PrivateLink endpoint

1.  Navigate to the VPC console in your AWS account
2.  Go to [Endpoints](https://console.aws.amazon.com/vpcconsole/home#Endpoints:) in the left sidebar
3.  Click [Create endpoint](https://console.aws.amazon.com/vpcconsole/home#CreateVpcEndpoint:)
4.  Give your endpoint a name (e.g. `supabase-privatelink-[project name]`)
5.  Under Type, select **Resources**
6.  In the **Resource configurations** section select the appropriate resource configuration
    *   The resource configuration name will be in the format `[organisation]-[project-ref]-rc`
7.  Select your VPC from the dropdown. This should match the VPC you selected for your security group in Step 3
8.  Enable the **Enable DNS name** option if you want to use a DNS record instead of the endpoints IP address(es)
9.  Choose the appropriate subnets for your network
    *   AWS will provision a private ENI for you in each selected subnet
    *   IP address type should be set to IPv4
10. Choose the security group you created in Step 3.
11. Click **Create endpoint**
12. After creation, you will see the endpoint in the [Endpoints](https://console.aws.amazon.com/vpcconsole/home#Endpoints:) section with a status of "Available"
13. For connectivity:
    *   The IP addresses of the endpoint will be listed in the **Subnets** section of the endpoint details
    *   The DNS record will be in the **Associations** section of the endpoint details in the **DNS Name** field if you enabled it in step 8


##### Option B: Attach resource configuration to an existing VPC lattice service network

1.  **This method is only recommended if you have an existing VPC Lattice Service Network**
2.  Navigate to the VPC Lattice console in your AWS account
3.  Go to [Service networks](https://console.aws.amazon.com/vpcconsole/home#ServiceNetworks) in the left sidebar and select your service network
4.  In the service network details, go to the **Resource configuration associations** tab
5.  Click **Create associations**
6.  Select the appropriate **Resource configuration** from the dropdown
7.  Click **Save changes**
8.  After creation, you will see the resource configuration in the Resource configurations section of your service network with the status "Active"
9.  For connectivity, click on the association details and the domain name will be listed in the **DNS entries** section


#### Step 5: Test connectivity

Verify the private connection is working correctly from your VPC:

1.  Launch an EC2 instance or use an existing instance in your VPC
2.  Install a Postgres client (e.g., `psql`)
3.  Test the connection using the private endpoint:

```bash
psql "postgresql://[username]:[password]@[private-endpoint]:5432/postgres"
```

You should see a successful connection without any public internet traffic.


#### Step 6: Update applications

Configure your applications to use the private connection details:

1.  Update your database connection strings to use the private endpoint hostname
2.  Ensure your application instances are in the same VPC or connected VPCs
3.  Update any database connection pooling configurations
4.  Test application connectivity thoroughly

Example connection string update:

```

# Before (public)
postgresql://user:pass@db.[project-ref].supabase.co:5432/postgres


# After (private)
postgresql://user:pass@your-private-endpoint.vpce.amazonaws.com:5432/postgres
```


#### Step 8: Disable public connectivity (optional)

For maximum security, you can disable public internet access for your database:

1.  Contact Supabase support to disable public connectivity
2.  Ensure all applications are successfully using the private connection
3.  Update any monitoring or backup tools to use the private endpoint



## Alpha limitations

During the alpha phase:

*   **Setup Coordination**: Configuration requires direct coordination with Supabase support team
*   **Feature Evolution**: The setup process and capabilities may evolve as we refine the offering



## Compatibility

The PrivateLink endpoint is a layer 3 solution so behaves like a standard Postgres endpoint, allowing you to connect using:

*   Direct Postgres connections using standard tools
*   Third-party database tools and ORMs (with the appropriate routing)



## Next steps

Ready to enhance your database security with PrivateLink? [Contact our Enterprise team](/contact/enterprise) to discuss your requirements and begin the setup process.

Our support team will guide you through the configuration and ensure your private database connectivity meets your security and performance requirements.



# Project Transfers



You can freely transfer projects between different organizations. Head to your [projects' general settings](/dashboard/project/_/settings/general) to initiate a project transfer.

<Image
  alt="Project Transfer: General Settings"
  src={{
    light: '/docs/img/guides/platform/project-transfer-overview--light.png',
    dark: '/docs/img/guides/platform/project-transfer-overview.png',
  }}
  className="max-w-[600px] !mx-auto border rounded-md"
  zoomable
/>

<Image
  alt="Project Transfer: Confirmation Modal"
  src={{
    light: '/docs/img/guides/platform/project-transfer-modal--light.png',
    dark: '/docs/img/guides/platform/project-transfer-modal.png',
  }}
  className="max-w-[600px] !mx-auto"
  zoomable
/>

Source organization - the organization the project currently belongs to
Target organization - the organization you want to move the project to



## Pre-Requirements

*   You need to be the owner of the source organization.
*   You need to be at least a member of the target organization you want to move the project to.
*   No active GitHub integration connection
*   No project-scoped roles pointing to the project (Team/Enterprise plan)
*   No log drains configured
*   Target organization is not managed by Vercel Marketplace (currently unsupported)



## Usage-billing and project add-ons

For usage metrics such as disk size, egress or image transformations and project add-ons such as [Compute Add-On](/docs/guides/platform/compute-add-ons), [Point-In-Time-Recovery](/docs/guides/platform/backups#point-in-time-recovery), [IPv4](/docs/guides/platform/ipv4-address), [Log Drains](/docs/guides/platform/log-drains), [Advanced MFA](/docs/guides/auth/auth-mfa/phone) or a [Custom Domain](/docs/guides/platform/custom-domains), the source organization will still be charged for the usage up until the transfer. The charges will be added to the invoice when the billing cycle resets.

The target organization will be charged at the end of the billing cycle for usage after the project transfer.



## Things to watch out for

*   Transferring a project might come with a short 1-2 minute downtime if you're moving a project from a paid to a Free Plan.
*   You could lose access to certain project features depending on the plan of the target organization, i.e. moving a project from a Pro Plan to a Free Plan.
*   When moving your project to a Free Plan, we also ensure you’re not exceeding your two free project limit. In these cases, it is best to upgrade your target organization to Pro Plan first.
*   You could have less rights on the project depending on your role in the target organization, i.e. you were an Owner in the previous organization and only have a Read-Only role in the target organization.



## Transfer to a different region

Note that project transfers are only transferring your projects across an organization and cannot be used to transfer between different regions. To move your project to a different region, see [migrating your project](/docs/guides/platform/migrating-within-supabase).



# Read Replicas

Deploy read-only databases across multiple regions, for lower latency and better resource management.

Read Replicas are additional databases that are kept in sync with your Primary database. You can read your data from a Read Replica, which helps with:

*   **Load balancing:** Read Replicas reduce load on the Primary database. For example, you can use a Read Replica for complex analytical queries and reserve the Primary for user-facing create, update, and delete operations.
*   **Improved latency:** For projects with a global user base, additional databases can be deployed closer to users to reduce latency.
*   **Redundancy:** Read Replicas provide data redundancy.

<Image alt="Map view of all project databases." src="/docs/img/guides/platform/read-replicas/map-view.png?v=1" containerClassName="max-w-[700px] !mx-auto" zoomable />



## About Read Replicas

The database you start with when launching a Supabase project is your Primary database. Read Replicas are kept in sync with the Primary through a process called "replication." Replication is asynchronous to ensure that transactions on the Primary aren't blocked. There is a delay between an update on the Primary and the time that a Read Replica receives the change. This delay is called "replication lag."

You can only read data from a Read Replica. This is in contrast to a Primary database, where you can both read and write:

|              | select | insert | update | delete |
| ------------ | ------ | ------ | ------ | ------ |
| Primary      | ✅      | ✅      | ✅      | ✅      |
| Read Replica | ✅      | -      | -      | -      |



## Prerequisites

<Admonition type="note">
  Read Replicas are available for all projects on the Pro, Team and Enterprise plans. Spin one up now over at the [Infrastructure Settings page](/dashboard/project/_/settings/infrastructure).
</Admonition>

Projects must meet these requirements to use Read Replicas:

1.  Running on AWS.
2.  Running on at least a [Small compute add-on](/docs/guides/platform/compute-add-ons).
    *   Read Replicas are started on the same compute instance as the Primary to keep up with changes.
3.  Running on Postgres 15+.
    *   For projects running on older versions of Postgres, you will need to [upgrade to the latest platform version](/docs/guides/platform/migrating-and-upgrading-projects#pgupgrade).
4.  Using [physical backups](/docs/guides/platform/backups#point-in-time-recovery)
    *   Physical backups are automatically enabled if using [PITR](/docs/guides/platform/backups#point-in-time-recovery)
    *   If you're not using PITR, you'll be able to switch to physical backups as part of the Read Replica setup process. Note that physical backups can't be downloaded from the dashboard in the way logical backups can.



## Getting started

To add a Read Replica, go to the [Infrastructure Settings page](/dashboard/project/_/settings/infrastructure) in your dashboard.

You can also manage Read Replicas using the Management API (beta functionality):

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Create a new Read Replica
curl -X POST "https://api.supabase.com/v1/projects/$PROJECT_REF/read-replicas/setup" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "region": "us-east-1"
  }'


# Delete a Read Replica
curl -X POST "https://api.supabase.com/v1/projects/$PROJECT_REF/read-replicas/remove" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "database_identifier": "abcdefghijklmnopqrst"
  }'
```

Projects on an XL compute add-on or larger can create up to five Read Replicas. Projects on compute add-ons smaller than XL can create up to two Read Replicas. All Read Replicas inherit the compute size of their Primary database.


### Deploying a Read Replica

A Read Replica is deployed by using a physical backup as a starting point, and a combination of WAL file archives and direct replication from the Primary database to catch up. Both components may take significant time to complete. The duration of restoring from a physical backup is roughly dependent and directly related to the database size of your project. The time taken to catch up to the primary using WAL archives and direct replication is dependent on the level of activity on the Primary database; a more active database will produce a larger number of WAL files that will need to be processed.

Along with the progress of the deployment, the dashboard displays rough estimates for each component.

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### What does it mean when "Init failed" is observed?

The status `Init failed` indicates that the Read Replica has failed to deploy. Some possible scenarios as to why a Read Replica may have failed to be deployed:

*   Underlying instance failed to come up.
*   Network issue leading to inability to connect to the Primary database.
*   Possible incompatible database settings between the Primary and Read Replica databases.
*   Platform issues.

It is safe to drop this failed Read Replica, and in the event of a transient issue, attempt to spin up another one. If however spinning up Read Replicas for your project consistently fails, do check out our [status page](https://status.supabase.com) for any ongoing incidents, or open a support ticket [here](/dashboard/support/new). To aid the investigation, do not bring down the recently failed Read Replica.



## Features

Read Replicas offer the following features:


### Dedicated endpoints

Each Read Replica has its own dedicated database and API endpoints.

*   Find the database endpoint on the projects [**Connect** panel](/dashboard/project/_?showConnect=true)
*   Find the API endpoint on the [API Settings page](/dashboard/project/_/settings/api) under **Project URL**

Read Replicas only support `GET` requests from the [REST API](/docs/guides/api). If you are calling a read-only Postgres function through the REST API, make sure to set the `get: true` [option](/docs/reference/javascript/rpc?queryGroups=example\&example=call-a-read-only-postgres-function).

Requests to other Supabase products, such as Auth, Storage, and Realtime, aren't able to use a Read Replica or its API endpoint. Support for more products will be added in the future.

If you're using an [IPv4 add-on](/docs/guides/platform/ipv4-address#read-replicas), the database endpoints for your Read Replicas will also use an IPv4 add-on.


### Dedicated connection pool

A connection pool through Supavisor is also available for each Read Replica. Find the connection string on the [Database Settings page](/dashboard/project/_/database/settings) under **Connection String**.


### API load balancer

A load balancer is deployed to automatically balance requests between your Primary database and Read Replicas. Find its endpoint on the [API Settings page](/dashboard/project/_/settings/api).

The load balancer enables geo-routing for Data API requests so that `GET` requests will automatically be routed to the database that is closest to your user ensuring the lowest latency. Non-`GET` requests can also be sent through this endpoint, and will be routed to the Primary database.

You can also interact with Supabase services (Auth, Edge Functions, Realtime, and Storage) through this load balancer so there's no need to worry about which endpoint to use and in which situations. However, geo-routing for these services are not yet available but is coming soon.

<Admonition type="note">
  Due to the requirements of the Auth service, all Auth requests are handled by the Primary, even when sent over the load balancer endpoint. This is similar to how non-Read requests for the Data API (PostgREST) are exclusively handled by the Primary.
</Admonition>

To call a read-only Postgres function on Read Replicas through the REST API, use the `get: true` [option](/docs/reference/javascript/rpc?queryGroups=example\&example=call-a-read-only-postgres-function).

If you remove all Read Replicas from your project, the load balancer and its endpoint are removed as well. Make sure to redirect requests back to your Primary database before removal.

<Admonition type="note">
  Starting on April 4th, 2025, we will be changing the routing behavior for eligible Data API requests:

  *   Old behavior: Round-Robin distribution among all databases (all read replicas + primary) of your project, regardless of location
  *   New behavior: Geo-routing, that directs requests to the closest available database (all read replicas + primary)

  The new behavior delivers a better experience for your users by minimizing the latency to your project. You can take full advantage of this by placing Read Replicas close to your major customer bases.
</Admonition>

<Admonition type="caution">
  If you use a [custom domain](/docs/guides/platform/custom-domains), requests will not be routed through the load balancer. You should instead use the dedicated endpoints provided in the dashboard.
</Admonition>


### Querying through the SQL editor

In the SQL editor, you can choose if you want to run the query on a particular Read Replica.

<Image alt="SQL editor view." src="/docs/img/guides/platform/read-replicas/sql-editor.png?v=1" containerClassName="max-w-[700px]" zoomable />


### Logging

When a Read Replica is deployed, it emits logs from the following services:

*   [API](/dashboard/project/_/logs/edge-logs)
*   [Postgres](/dashboard/project/_/logs/postgres-logs)
*   [PostgREST](/dashboard/project/_/logs/postgrest-logs)
*   [Supavisor](/dashboard/project/_/logs/pooler-logs)

Views on [Log Explorer](/docs/guides/platform/logs) are automatically filtered by databases, with the logs of the Primary database displayed by default. Viewing logs from other databases can be toggled with the `Source` button found on the upper-right part section of the Logs Explorer page.

For API logs, logs can originate from the API Load Balancer as well. The upstream database or the one that eventually handles the request can be found under the `Redirect Identifier` field. This is equivalent to `metadata.load_balancer_redirect_identifier` when querying the underlying logs.


### Metrics

Observability and metrics for Read Replicas are available on the Supabase Dashboard. Resource utilization for a specific Read Replica can be viewed on the [Database Reports page](/dashboard/project/_/reports/database) by toggling for `Source`. Likewise, metrics on API requests going through either a Read Replica or Load Balancer API endpoint are also available on the dashboard through the [API Reports page](/dashboard/project/_/reports/api-overview)

We recommend ingesting your [project's metrics](/docs/guides/platform/metrics#accessing-the-metrics-endpoint) into your own environment. If you have an existing ingestion pipeline set up for your project, you can [update it](https://github.com/supabase/supabase-grafana?tab=readme-ov-file#read-replica-support) to additionally ingest metrics from your Read Replicas.


### Centralized configuration management

All settings configured through the dashboard will be propagated across all databases of a project. This ensures that no Read Replica get out of sync with the Primary database or with other Read Replicas.



## Operations blocked by Read Replicas


### Project upgrades and data restorations

The following procedures require all Read Replicas for a project to be brought down before they can be performed:

1.  [Project upgrades](/docs/guides/platform/migrating-and-upgrading-projects#pgupgrade)
2.  [Data restorations](/docs/guides/platform/backups#pitr-restoration-process)

These operations need to be completed before Read Replicas can be re-deployed.



## About replication

We use a hybrid approach to replicate data from a Primary to its Read Replicas, combining the native methods of streaming replication and file-based log shipping.


### Streaming replication

Postgres generates a Write Ahead Log (WAL) as database changes occur. With streaming replication, these changes stream from the Primary to the Read Replica server. The WAL alone is sufficient to reconstruct the database to its current state.

This replication method is fast, since changes are streamed directly from the Primary to the Read Replica. On the other hand, it faces challenges when the Read Replica can't keep up with the WAL changes from its Primary. This can happen when the Read Replica is too small, running on degraded hardware, or has a heavier workload running.

To address this, Postgres does provide tunable configuration, like `wal_keep_size`, to adjust the WAL retained by the Primary. If the Read Replica fails to “catch up” before the WAL surpasses the `wal_keep_size` setting, the replication is terminated. Tuning is a bit of an art - the amount of WAL required is variable for every situation.


### File-based log shipping

In this replication method, the Primary continuously buffers WAL changes to a local file and then sends the file to the Read Replica. If multiple Read Replicas are present, files could also be sent to an intermediary location accessible by all. The Read Replica then reads the WAL files and applies those changes. There is higher replication lag than streaming replication since the Primary buffers the changes locally first. It also means there is a small chance that WAL changes do not reach Read Replicas if the Primary goes down before the file is transferred. In these cases, if the Primary fails a Replica using streaming replication would (in most cases) be more up-to-date than a Replica using file-based log shipping.


### File-based log shipping 🤝 streaming replication

<Image alt="Map view of Primary and Read Replica databases" caption="Map view of Primary and Read Replica databases" src="/docs/img/guides/platform/read-replicas/streaming-replication-dark.png?v=1" containerClassName="max-w-[700px] mx-auto" zoomable />

We bring these two methods together to achieve quick, stable, and reliable replication. Each method addresses the limitations of the other. Streaming replication minimizes replication lag, while file-based log shipping provides a fallback. For file-based log shipping, we use our existing Point In Time Recovery (PITR) infrastructure. We regularly archive files from the Primary using [WAL-G](https://github.com/wal-g/wal-g), an open source archival and restoration tool, and ship the WAL files to S3.

We combine it with streaming replication to reduce replication lag. Once WAL-G files have been synced from S3, Read Replicas connect to the Primary and stream the WAL directly.


### Monitoring replication lag

Replication lag for a specific Read Replica can be monitored through the dashboard. On the [Database Reports page](/dashboard/project/_/reports/database) Read Replicas will have an additional chart under `Replica Information` displaying historical replication lag in seconds. Realtime replication lag in seconds can be observed on the [Infrastructure Settings page](/dashboard/project/_/settings/infrastructure). This is the value on top of the Read Replica. Do note that there is no single threshold to indicate when replication lag should be addressed. It would be fully dependent on the requirements of your project.

If you are already ingesting your [project's metrics](/docs/guides/platform/metrics#accessing-the-metrics-endpoint) into your own environment, you can also keep track of replication lag and set alarms accordingly with the metric: `physical_replication_lag_physical_replica_lag_seconds`.

Some common sources of high replication lag include:

1.  Exclusive locks on tables on the Primary.
    Operations such as `drop table`, `reindex` (amongst others) take an Access Exclusive lock on the table. This can result in increasing replication lag for the duration of the lock.
2.  Resource Constraints on the database
    Heavy utilization on the primary or the replica, if run on an under-resourced project, can result in high replication lag. This includes the characteristics of the disk being utilized (IOPS, Throughput).
3.  Long-running transactions on the Primary.
    Transactions that run for a long-time on the primary can also result in high replication lag. You can use the `pg_stat_activity` view to identify and terminate such transactions if needed. `pg_stat_activity` is a live view, and does not offer historical data on transactions that might have been active for a long time in the past.

High replication lag can result in stale data being returned for queries being executed against the affected read replicas.

You can [consult](https://cloud.google.com/sql/docs/postgres/replication/replication-lag) [additional](https://repost.aws/knowledge-center/rds-postgresql-replication-lag) [resources](https://severalnines.com/blog/what-look-if-your-postgresql-replication-lagging/) on the subject as well.



## Misc


### Restart or compute add-on change behaviour

When a project that utilizes Read Replicas is restarted, or the compute add-on size is changed, the Primary database gets restarted first. During this period, the Read Replicas remain available.

Once the Primary database has completed restarting (or resizing, in case of a compute add-on change) and become available for usage, all the Read Replicas are restarted (and resized, if needed) concurrently.



## Pricing

For a detailed breakdown of how charges are calculated, refer to [Manage Read Replica usage](/docs/guides/platform/manage-your-usage/read-replicas).



# Available regions



Each Supabase project is deployed to one primary region. Choose the location closest to your users for the best performance.



## General regions

For most projects, we recommend choosing a general region. Supabase will deploy your project to an available AWS region within that area based on current infrastructure capacity.

<SmartRegionsList />

Note: General regions aren’t yet supported for read replicas or management via the API.



## Specific regions

If you prefer, you can choose an exact AWS region for your project.

<RegionsList />



# Postgres SSL Enforcement



Your Supabase project supports connecting to the Postgres DB without SSL enabled to maximize client compatibility. For increased security, you can prevent clients from connecting if they're not using SSL.

Disabling SSL enforcement only applies to connections to Postgres and Supavisor ("Connection Pooler"); all HTTP APIs offered by Supabase (e.g., PostgREST, Storage, Auth) automatically enforce SSL on all incoming connections.

<Admonition type="note">
  Projects need to be at least on Postgres 13.3.0 to enable SSL enforcement. You can find the Postgres version of your project in the [Infrastructure Settings page](/dashboard/project/_/settings/infrastructure). If your project is on an older version, you will need to [upgrade](/docs/guides/platform/migrating-and-upgrading-projects#upgrade-your-project) to use this feature.
</Admonition>



## Manage SSL enforcement via the dashboard

SSL enforcement can be configured via the "Enforce SSL on incoming connections" setting under the SSL Configuration section in [Database Settings page](/dashboard/project/_/database/settings) of the dashboard.



## Manage SSL enforcement via the Management API

You can also manage SSL enforcement using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Get current SSL enforcement status
curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/ssl-enforcement" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"


# Enable SSL enforcement
curl -X PUT "https://api.supabase.com/v1/projects/$PROJECT_REF/ssl-enforcement" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "requestedConfig": {
      "database": true
    }
  }'


# Disable SSL enforcement
curl -X PUT "https://api.supabase.com/v1/projects/$PROJECT_REF/ssl-enforcement" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "requestedConfig": {
      "database": false
    }
  }'
```



## Manage SSL enforcement via the CLI

To get started:

1.  [Install](/docs/guides/cli) the Supabase CLI 1.37.0+.
2.  [Log in](/docs/guides/getting-started/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3.  Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project that you are enabling SSL enforcement.


### Check enforcement status

You can use the `get` subcommand of the CLI to check whether SSL is currently being enforced:

```bash
supabase ssl-enforcement --project-ref {ref} get --experimental
```

Response if SSL is being enforced:

```bash
SSL is being enforced.
```

Response if SSL is not being enforced:

```bash
SSL is *NOT* being enforced.
```


### Update enforcement

The `update` subcommand is used to change the SSL enforcement status for your project:

```bash
supabase ssl-enforcement --project-ref {ref} update --enable-db-ssl-enforcement --experimental
```

Similarly, to disable SSL enforcement:

```bash
supabase ssl-enforcement --project-ref {ref} update --disable-db-ssl-enforcement --experimental
```


### A note about Postgres SSL modes

Postgres supports [multiple SSL modes](https://www.postgresql.org/docs/current/libpq-ssl.html#LIBPQ-SSL-PROTECTION) on the client side. These modes provide different levels of protection. Depending on your needs, it is important to verify that the SSL mode in use is performing the required level of enforcement and verification of SSL connections.

The strongest mode offered by Postgres is `verify-full` and this is the mode you most likely want to use when SSL enforcement is enabled. To use `verify-full` you will need to download the Supabase CA certificate for your database. The certificate is available through the dashboard under the SSL Configuration section in the [Database Settings page](/dashboard/project/_/database/settings).

Once the CA certificate has been downloaded, add it to the certificate authority list used by Postgres.

```bash
cat {location of downloaded prod-ca-2021.crt} >> ~/.postgres/root.crt
```

With the CA certificate added to the trusted certificate authorities list, use `psql` or your client library to connect to Supabase:

```bash
psql "postgresql://aws-0-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=verify-full" -U postgres.<user>
```



# Enable SSO for Your Organization



<Admonition type="tip">
  Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](/docs/guides/auth/enterprise-sso/auth-sso-saml).
</Admonition>

Supabase offers single sign-on (SSO) as a login option to provide additional account security for your team. This allows company administrators to enforce the use of an identity provider when logging into Supabase. SSO improves the onboarding and offboarding experience of the company as the employee only needs a single set of credentials to access third-party applications or tools which can also be revoked by an administrator.

<Admonition type="note">
  Supabase currently provides SAML SSO for [Team and Enterprise Plan customers](/pricing). If you are an existing Team or Enterprise Plan customer, continue with the setup below.
</Admonition>



## Supported providers

Supabase supports practically all identity providers that support the SAML 2.0 SSO protocol. We've prepared these guides for commonly used identity providers to help you get started. If you use a different provider, our support stands ready to support you.

*   [Google Workspaces (formerly G Suite)](/docs/guides/platform/sso/gsuite)
*   [Azure Active Directory](/docs/guides/platform/sso/azure)
*   [Okta](/docs/guides/platform/sso/okta)

Once configured, you can update your settings anytime via the [SSO tab](/dashboard/org/_/sso) under **Organization Settings**.

![SSO Example](/docs/img/sso-dashboard-enabled.png)



## Key configuration options

*   **Multiple domains** - You can associate one or more email domains with your SSO provider. Users with email addresses matching these domains are eligible to sign in via SSO.
*   **Auto-join** - Optionally allow users with a matching domain to be added to your organization automatically when they first sign in, without an invitation.
*   **Default role for auto-joined users** - Choose the role (e.g., `Read-only`, `Developer`, `Administrator`, `Owner`) that automatically joined users receive. Refer to [access control](/docs/guides/platform/access-control) for more information about roles.



## How SSO works in Supabase

When SSO is enabled for an organization:

*   Organization invites are restricted to company members belonging to the same identity provider.
*   Every user has an organization created by default. They can create as many projects as they want.
*   An SSO user will not be able to update or reset their password since the company administrator manages their access via the identity provider.
*   If an SSO user with the following email of `alice@foocorp.com` attempts to sign in with a GitHub account that uses the same email, a separate Supabase account is created and will not be linked to the SSO user's account.
*   SSO users will only see organizations/projects they've been invited to or auto-joined into. See [access control](/docs/guides/platform/access-control) for more details.



## Disabling SSO for an organization

If you disable the SSO provider for an organization, **all SSO users will immediately be unable to sign in**. Before disabling SSO, ensure you have at least one non-SSO owner account to prevent being locked out.



## Removing an individual SSO user's access

To revoke access for a specific SSO user without disabling the provider entirely you may:

*   Remove or disable the user's account in your identity provider
*   Downgrade or remove their permissions for any organizations in Supabase.



# Upgrading



Supabase ships fast and we endeavor to add all new features to existing projects wherever possible. In some cases, access to new features require upgrading or migrating your Supabase project.

<Admonition type="tip">
  This guide refers to upgrading the Postgres version of your Supabase Project. For scaling your compute size, refer to the [Compute and Disk page](/docs/guides/platform/compute-and-disk).
</Admonition>

You can upgrade your project using in-place upgrades or by pausing and restoring your project.

<ShowUntil date="2024-12-17">
  <Admonition type="tip">
    The Migrating and Upgrading guide has been divided into two sections. To migrate between Supabase projects, see [Migrating within Supabase](/docs/guides/platform/migrating-within-supabase).
  </Admonition>
</ShowUntil>



## In-place upgrades

<Admonition type="note">
  For security purposes, passwords for custom roles are not backed up and, following a restore, they would need to be reset. See [here](/docs/guides/platform/backups#daily-backups) for more details
</Admonition>

In-place upgrades uses `pg_upgrade`. For projects larger than 1GB, this method is generally faster than a pause and restore cycle, and the speed advantage grows with the size of the database.

1.  Plan for an appropriate downtime window, and ensure you have reviewed the [caveats](#caveats) section of this document before executing the upgrade.
2.  Use the "Upgrade project" button on the [Infrastructure](/dashboard/project/_/settings/infrastructure) section of your dashboard.

Additionally, if the upgrade should fail, your original database would be brought back up online and be able to service requests.

As a rough rule of thumb, pg\_upgrade operates at ~100MBps (when executing an upgrade on your data). Using the size of your database, you can use this metric to derive an approximate sense of the downtime window necessary for the upgrade. During this window, you should plan for your database and associated services to be unavailable.



## Pause and restore

<Admonition type="note">
  We recommend using the In-place upgrade method, as it is faster, and more reliable. Additionally, only Free-tier projects are eligible to use the Pause and Restore method.
</Admonition>

When you pause and restore a project, the restored database includes the latest features. This method *does* include downtime, so be aware that your project will be inaccessible for a short period of time.

1.  On the [General Settings](/dashboard/project/_/settings/general) page in the Dashboard, click **Pause project**. You will be redirected to the home screen as your project is pausing. This process can take several minutes.
2.  After your project is paused, click **Restore project**. The restoration can take several minutes depending on how much data your database has. You will receive an email once the restoration is complete.

Note that a pause + restore upgrade involves tearing down your project's resources before bringing them back up again. If the restore process should fail, manual intervention from Supabase support will be required to bring your project back online.



## Caveats

Regardless of the upgrade method, a few caveats apply:


### Logical replication

If you are using logical replication, the replication slots will not be preserved by the upgrade process. You will need to manually recreate them after the upgrade with the method `pg_create_logical_replication_slot`. Refer to the Postgres docs on [Replication Management Functions](https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-REPLICATION) for more details about the method.


### Breaking changes

Newer versions of services can break functionality or change the performance characteristics you rely on. If your project is eligible for an upgrade, you will be able to find your current service versions from within [the Supabase dashboard](/dashboard/project/_/settings/infrastructure).

Breaking changes are generally only present in major version upgrades of Postgres and PostgREST. You can find their respective release notes at:

*   [Postgres](https://www.postgresql.org/docs/release/)
*   [PostgREST](https://github.com/PostgREST/postgrest/releases)

If you are upgrading from a significantly older version, you will need to consider the release notes for any intermediary releases as well.


### Time limits

Starting from 2024-06-24, when a project is paused, users then have a 90-day window to restore the project on the platform from within Supabase Studio.

The 90-day window allows Supabase to introduce platform changes that may not be backwards compatible with older backups. Unlike active projects, static backups can't be updated to accommodate such changes.

During the 90-day restore window a paused project can be restored to the platform with a single button click from [Studio's dashboard page](/dashboard/projects).

<Image zoomable alt="Project Paused: 90 Days Remaining" src="/docs/img/guides/platform/paused-90-day.png" />

After the 90-day restore window, you can download your project's backup file, and Storage objects from the project dashboard. See [restoring a backup locally](/docs/guides/local-development/restoring-downloaded-backup) for instructions on how to load that backup locally to recover your data.

<Image zoomable alt="Project Paused: 90 Days Remaining" src="/docs/img/guides/platform/paused-dl-backup.png" />

If you upgrade to a paid plan while your project is paused, any expired one-click restore options are reenabled. Since the backup was taken outside the backwards compatibility window, it may fail to restore. If you have a problem restoring your backup after upgrading, contact [Support](/support).

<Image zoomable alt="Project Paused: 90 Days Remaining" src="/docs/img/guides/platform/paused-paid-tier.png" />


### Disk sizing

When upgrading, the Supabase platform will "right-size" your disk based on the current size of the database. For example, if your database is 100GB in size, and you have a 200GB disk, the upgrade will reduce the disk size to 120GB (1.2x the size of your database).


### Objects dependent on Postgres extensions

In-place upgrades do not support upgrading of databases containing reg\* data types referencing system OIDs.
If you have created any objects that depend on the following extensions, you will need to recreate them after the upgrade.


### `pg_cron` records

[pg\_cron](https://github.com/citusdata/pg_cron#viewing-job-run-details) does not automatically clean up historical records. This can lead to extremely large `cron.job_run_details` tables if the records are not regularly pruned; you should clean unnecessary records from this table prior to an upgrade.

During an in-place upgrade, the `pg_cron` extension gets dropped and recreated. Prior to this process, the `cron.job_run_details` table is duplicated to avoid losing historical logs. The instantaneous disk pressure created by duplicating an extremely large details table can cause at best unnecessary performance degradation, or at worst, upgrade process failures.


### Extensions

In-place upgrades do not currently support upgrading of databases using extensions older than the following versions:

*   TimescaleDB 2.16.1
*   plv8 3.1.10

To upgrade to a newer version of Postgres, you will need to drop the extensions before the upgrade, and recreate them after the upgrade.


#### Authentication method changes - deprecating md5 in favor of scram-sha-256

The md5 hashing method has [known weaknesses](https://en.wikipedia.org/wiki/MD5#Security) that make it unsuitable for cryptography.
As such, we are deprecating md5 in favor of [scram-sha-256](https://www.postgresql.org/docs/current/auth-password.html), which is the default and most secure authentication method used in the latest Postgres versions.

We automatically migrate Supabase-managed roles' passwords to scram-sha-256 during the upgrade process, but you will need to manually migrate the passwords of any custom roles you have created, else you won't be able to connect using them after the upgrade.

To identify roles using the md5 hashing method and migrate their passwords, you can use the following SQL statements after the upgrade:

```sql
-- List roles using md5 hashing method
SELECT
  rolname
FROM pg_authid
WHERE rolcanlogin = true
  AND rolpassword LIKE 'md5%';

-- Migrate a role's password to scram-sha-256
ALTER ROLE <role_name> WITH PASSWORD '<password>';
```


### Database size reduction

As part of the upgrade process, maintenance operations such as [vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html#ROUTINE-VACUUMING) are also executed. This can result in a reduction in the reported database size.


### Post-upgrade validation

Supabase performs extensive pre- and post-upgrade validations to ensure that the database has been correctly upgraded. However, you should plan for your own application-level validations, as there might be changes you might not have anticipated, and this should be budgeted for when planning your downtime window.



## Specific upgrade notes


### Upgrading to Postgres 17

In projects using Postgres 17, the following extensions are deprecated:

*   `plcoffee`
*   `plls`
*   `plv8`
*   `timescaledb`
*   `pgjwt`

Projects planning to upgrade from Postgres 15 to Postgres 17 need to first disable these extensions in the [Supabase Dashboard](/dashboard/project/_/database/extensions).

`pgjwt` was enabled by default on every Supabase project up until Postgres 17. If you weren’t explicitly using `pgjwt` in your project, it’s most likely safe to disable.

Existing projects on lower versions of Postgres are not impacted, and the extensions will continue to be supported on projects using Postgres 15, until the end of life of Postgres 15 on the Supabase platform.



# Your monthly invoice




## Billing cycle

When you sign up for a paid plan you get charged once a month at the beginning of the billing cycle. A billing cycle starts with the creation of a Supabase organization. If you create an organization on the sixth of January your billing cycle resets on the sixth of each month. If the anchored day is not present in the current month, then the last day of the month is used.



## Your invoice explained

When your billing cycle resets an invoice gets issued. That invoice contains line items from both the current and the previous billing cycle. Fixed fees for the current billing cycle, usage based fees for the previous billing cycle.


### Fixed fees

Fixed fees are independent of usage and paid in-advance. Whether you have one or several projects, hundreds or millions of active users, the fee is always the same, and doesn't vary. Examples are the subscription fee, the fee for HIPAA and for priority support.


### Usage based fees

Fees vary depending on usage and are paid in arrears. The more usage you have, the higher the fee. Examples are fees for monthly active users and storage size.


### Discounted line items

Paid plans come with a usage quota for certain line items. You only pay for usage that goes beyond the quota. The quota for Storage for example is 100 GB. If you use 105 GB, you pay for 5 GB. If you use 95 GB, you pay nothing. This quota is declared as a discount on your invoice.


#### Compute Credits

Paid plans come with <Price price="10" /> in Compute Credits per month. This suffices for a single project using a Nano or Micro compute instance. Every additional project adds compute fees to your monthly invoice though.


### Example invoice

The following invoice was issued on January 6, 2025 with the previous billing cycle from December 6, 2024 - January 5, 2025, and the current billing cycle from January 6 - February 5, 2025.

<Image
  alt="Example Invoice"
  src={{
    light: '/docs/img/guides/platform/example-invoice.png',
    dark: '/docs/img/guides/platform/example-invoice.png',
  }}
  zoomable
/>

1.  The final amount due
2.  Fixed subscription fee for the current billing cycle
3.  Usage based fee for Compute for the previous billing cycle. There were two projects (`wsmmedyqtlrvbcesxdew`, `wwxdpovgtfcmcnxwsaad`) running 744 hours (24 hours \* 31 days). These projects incurred <Price price="10" /> in Compute fees each. With <Price price="10" /> in Compute Credits deducted, the final Compute fees are <Price price="10." />
4.  Usage based fee for Custom Domain for the previous billing cycle. There is no free usage quota for Custom Domain. You get charged for the 744 hours (24 hours \* 31 days) a Custom Domain was active. The final Custom Domain fees are <Price price="10.19" />.
5.  Usage based fee for Egress for the previous billing cycle. There is a free usage quota of 250 GB for Egress. You get charged for usage beyond 250 GB only, meaning for 2,119.47 GB. The final Egress fees are <Price price="190.75" />.
6.  Usage based fee for Monthly Active Users for the previous billing cycle. There is a free usage quota of 100,000 users. With 141 users there is no charge for this line item.

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}


### Why is my invoice more than <Price price="25" />?

The amount due of your invoice being higher than the <Price price="25" /> subscription fee for the Pro Plan can have several reasons.

*   **Running several projects:** You had more than one project running in the previous billing cycle. Supabase provides a dedicated server and database for every project. That means that every project you launch incurs compute costs. While the <Price price="10" /> Compute Credits cover a single project using a Nano or Micro compute instance, every additional project adds at least <Price price="10" /> compute costs to your invoice.
*   **Usage beyond quota:** You exceeded the included usage quota for one or more line items in the previous billing cycle while having the Spend Cap disabled.
*   **Usage that is not covered by the Spend Cap:** You had usage in the previous billing cycle that is not covered by the [Spend Cap](/docs/guides/platform/cost-control#spend-cap). For example using an IPv4 address or a custom domain.



## How to settle your invoices

Monthly invoices are auto-collected by charging the payment method marked as "active" for an organization.


### Payment failure

If your payment fails, Supabase retries the charge several times. We send you a Payment Failure email with the reason for the failure. Follow the steps outlined in this email. You can manually trigger a charge at any time via

*   the link in the Payment Failure email
*   the "Pay Now" button on the [organization's invoices page](/dashboard/org/_/billing#invoices)



## Where to find your invoices

Your invoice is sent to you via email. You can also find your invoices on the [organization's invoices page](/dashboard/org/_/billing#invoices).



# Set Up SSO with Azure AD



<Admonition type="note">
  This feature is only available on the [Team and Enterprise Plans](/pricing). If you are an existing Team or Enterprise Plan customer, continue with the setup below.
</Admonition>

<Admonition type="tip">
  Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](/docs/guides/auth/enterprise-sso/auth-sso-saml).
</Admonition>

Supabase supports single sign-on (SSO) using Microsoft Azure AD.



## Step 1: Add and register an Enterprise application \[#add-and-register-enterprise-application]

Open up the [Azure Active Directory](https://portal.azure.com/#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/Overview) dashboard for your Azure account.

Click the *Add* button then *Enterprise application*.

![Azure AD console: Default Directory Overview](/docs/img/sso-azure-step-01.png)



## Step 2: Choose to create your own application \[#create-application]

You'll be using the custom enterprise application setup for Supabase.

![Azure AD console: Browse Azure AD Gallery, select: Create your own application](/docs/img/sso-azure-step-02.png)



## Step 3: Fill in application details \[#add-application-details]

In the modal titled *Create your own application*, enter a display name for Supabase. This is the name your Azure AD users will see when signing in to Supabase from Azure. `Supabase` works in most cases.

Make sure to choose the third option: *Integrate any other application you
don't find in the gallery (Non-gallery)*.

![Azure AD console: Create your own application modal](/docs/img/sso-azure-step-03.png)



## Step 4: Set up single sign-on \[#set-up-single-sign-on]

Before you get to assigning users and groups, which would allow accounts in Azure AD to access Supabase, you need to configure the SAML details that allows Supabase to accept sign in requests from Azure AD.

![Azure AD console: Supabase custom enterprise application, selected Set up single sign-on](/docs/img/sso-azure-step-04.png)



## Step 5: Select SAML single sign-on method \[#saml-sso]

Supabase only supports the SAML 2.0 protocol for Single Sign-On, which is an industry standard.

![Azure AD console: Supabase application, Single sign-on configuration screen, selected SAML](/docs/img/sso-azure-step-05.png)



## Step 6: Upload SAML-based sign-on metadata file \[#upload-saml-metadata]

First you need to download Supabase's SAML metadata file. Click the button below to initiate a download of the file.

<a href="https://alt.supabase.io/auth/v1/sso/saml/metadata?download=true">
  <Button size="large" icon={<IconArrowDown />}>
    Download Supabase SAML Metadata File
  </Button>
</a>

Alternatively, visit this page to initiate a download: `https://alt.supabase.io/auth/v1/sso/saml/metadata?download=true`

Click on the *Upload metadata file* option in the toolbar and select the file you just downloaded.

![Azure AD console: Supabase application, SAML-based Sign-on screen, selected Upload metadata file button](/docs/img/sso-azure-step-06-1.png)

All of the correct information should automatically populate the *Basic SAML Configuration* screen as shown.

![Azure AD console: Supabase application, SAML-based Sign-on screen, Basic SAML Configuration shown](/docs/img/sso-azure-step-06-2.png)

**Make sure you input these additional settings.**

| Setting     | Value                                        |
| ----------- | -------------------------------------------- |
| Sign on URL | `https://supabase.com/dashboard/sign-in-sso` |
| Relay State | `https://supabase.com/dashboard`             |

Finally, click the *Save* button to save the configuration.



## Step 7: Obtain metadata URL \[#idp-metadata-url]

Save the link under **App Federation Metadata URL** in \*section 3 **SAML Certificates\***. You will need to enter this URL later in [Step 10](#dashboard-configure-metadata).

![Azure AD console: Supabase application, SAML Certificates card shown, App Federation Metadata Url highlighted](/docs/img/sso-azure-step-07.png)



## Step 8: Enable SSO in the Dashboard \[#dashboard-enable-sso]

1.  Visit the [SSO tab](/dashboard/org/_/sso) under the Organization Settings page. ![SSO disabled](/docs/img/sso-dashboard-disabled.png)

2.  Toggle **Enable Single Sign-On** to begin configuration. Once enabled, the configuration form appears. ![SSO enabled](/docs/img/sso-dashboard-enabled.png)



## Step 9: Configure domains \[#dashboard-configure-domain]

Enter one or more domains associated with your users email addresses (e.g., `supabase.com`).
These domains determine which users are eligible to sign in via SSO.

![Domain configuration](/docs/img/sso-dashboard-configure-domain.png)

If your organization uses more than one email domain - for example, `supabase.com` for staff and `supabase.io` for contractors - you can add multiple domains here. All listed domains will be authorized for SSO sign-in.

![Domain configuration with multiple domains](/docs/img/sso-dashboard-configure-domain-multi.png)

<Admonition type="note">
  We do not permit use of public domains like `gmail.com`, `yahoo.com`.
</Admonition>



## Step 10: Configure metadata \[#dashboard-configure-metadata]

Enter the metadata URL you obtained from [Step 7](#idp-metadata-url) into the Metadata URL field:

![Metadata configuration with Azure AD](/docs/img/sso-dashboard-configure-metadata-azure.png)



## Step 11: Configure attribute mapping \[#dashboard-configure-attributes]

Fill out the Attribute Mapping section using the **Azure** preset.

![Attribute mapping configuration](/docs/img/sso-dashboard-configure-attributes-azure.png)



## Step 12: Join organization on signup (optional) \[#dashboard-configure-autojoin]

By default this setting is disabled, users logging in via SSO will not be added to your organization automatically.

![Auto-join disabled](/docs/img/sso-dashboard-configure-autojoin-disabled.png)

Toggle this on if you want SSO-authenticated users to be **automatically added to your organization** when they log in via SSO.

![Auto-join enable](/docs/img/sso-dashboard-configure-autojoin-enabled.png)

When auto-join is enabled, you can choose the **default role** for new users:

![Auto-join role selection](/docs/img/sso-dashboard-configure-autojoin-enabled-role.png)

Choose a role that fits the level of access you want to grant to new members.

<Admonition type="note">
  Visit [access-control](/docs/guides/platform/access-control) documentation for details about each role.
</Admonition>



## Step 13: Save changes and test single sign-on \[#dashboard-configure-save]

When you click **Save changes**, your new SSO configuration is applied immediately. From that moment, any user with an email address matching one of your configured domains who visits your organization's sign-in URL will be routed through the SSO flow.

We recommend asking a few users to test signing in via their Azure AD account. They can do this by entering their email address on the [Sign in with SSO](/dashboard/sign-in-sso) page.

If SSO sign-in doesn't work as expected, contact your Supabase support representative for assistance.



# Set Up SSO with Google Workspace



<Admonition type="note">
  This feature is only available on the [Team and Enterprise Plans](/pricing). If you are an existing Team or Enterprise Plan customer, continue with the setup below.
</Admonition>

<Admonition type="tip">
  Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](/docs/guides/auth/enterprise-sso/auth-sso-saml).
</Admonition>

Supabase supports single sign-on (SSO) using Google Workspace (formerly known as G Suite).



## Step 1: Open the Google Workspace web and mobile apps console \[#google-workspace-console]

![Google Workspace: Web and mobile apps admin console](/docs/img/sso-gsuite-step-01.png)



## Step 2: Choose to add custom SAML app \[#add-custom-saml-app]

From the *Add app* button in the toolbar choose *Add custom SAML app*.

![Google Workspace: Web and mobile apps admin console, Add custom SAML app selected](/docs/img/sso-gsuite-step-02.png)



## Step 3: Fill out app details \[#add-app-details]

The information you enter here is for visibility into your Google Workspace. You can choose any values you like. `Supabase` as a name works well for most use cases. Optionally enter a description.

![Google Workspace: Web and mobile apps admin console, Add custom SAML, App details screen](/docs/img/sso-gsuite-step-03.png)



## Step 4: Download IdP metadata \[#download-idp-metadata]

This is a very important step. Click on *DOWNLOAD METADATA* and save the file that was downloaded. You will need to upload this file later in [Step 10](#dashboard-configure-metadata).

![Google Workspace: Web and mobile apps admin console, Add custom SAML, Google Identity Provider details screen](/docs/img/sso-gsuite-step-04.png)

**Important: Make sure the certificate as shown on screen has at least 1 year before it expires. Mark down this date in your calendar so you will be reminded that you need to update the certificate without any downtime for your users.**



## Step 5: Add service provider details \[#add-service-provider-details]

Fill out these service provider details on the next screen.

| Detail         | Value                                               |
| -------------- | --------------------------------------------------- |
| ACS URL        | `https://alt.supabase.io/auth/v1/sso/saml/acs`      |
| Entity ID      | `https://alt.supabase.io/auth/v1/sso/saml/metadata` |
| Start URL      | `https://supabase.com/dashboard`                    |
| Name ID format | PERSISTENT                                          |
| Name ID        | *Basic Information > Primary email*                 |

![Google Workspace: Web and mobile apps admin console, Add custom SAML, Service provider details screen](/docs/img/sso-gsuite-step-05.png)



## Step 6: Configure attribute mapping \[#configure-attribute-mapping]

Attribute mappings allow Supabase to get information about your Google Workspace users on each login.

**A *Primary email* to `email` mapping is required.** Other mappings shown below are optional and configurable depending on your Google Workspace setup. If in doubt, replicate the same config as shown.

Any changes you make from this screen will be used later in [Step 10: Configure Attribute Mapping](#dashboard-configure-attributes).

![Google Workspace: Web and mobile apps admin console, Add custom SAML, Attribute mapping](/docs/img/sso-gsuite-step-06.png)



## Step 7: Configure user access \[#configure-user-access]

You can configure which Google Workspace user accounts will get access to Supabase. This is important if you wish to limit access to your software engineering teams.

You can configure this access by clicking on the *User access* card (or down-arrow). Follow the instructions on screen.

![Google Workspace: Web and mobile apps admin console, Supabase app screen](/docs/img/sso-gsuite-step-08.png)

<Admonition type="note">
  Changes from this step sometimes take a while to propagate across Google's systems. Wait at least 15 minutes before testing your changes.
</Admonition>



## Step 8: Enable SSO in the Dashboard \[#dashboard-enable-sso]

1.  Visit the [SSO tab](/dashboard/org/_/sso) under the Organization Settings page. ![SSO disabled](/docs/img/sso-dashboard-disabled.png)

2.  Toggle **Enable Single Sign-On** to begin configuration. Once enabled, the configuration form appears. ![SSO enabled](/docs/img/sso-dashboard-enabled.png)



## Step 9: Configure domains \[#dashboard-configure-domain]

Enter one or more domains associated with your users email addresses (e.g., `supabase.com`).
These domains determine which users are eligible to sign in via SSO.

![Domain configuration](/docs/img/sso-dashboard-configure-domain.png)

If your organization uses more than one email domain - for example, `supabase.com` for staff and `supabase.io` for contractors - you can add multiple domains here. All listed domains will be authorized for SSO sign-in.

![Domain configuration with multiple domains](/docs/img/sso-dashboard-configure-domain-multi.png)

<Admonition type="note">
  We do not permit use of public domains like `gmail.com`, `yahoo.com`.
</Admonition>



## Step 10: Configure metadata \[#dashboard-configure-metadata]

Upload the metadata file you downloaded in [Step 6](#download-idp-metadata) into the Metadata Upload File field.

![Metadata configuration with Google Workspace](/docs/img/sso-dashboard-configure-metadata-gsuite.png)



## Step 11: Configure attribute mapping \[#dashboard-configure-attributes]

Enter the SAML attributes you filled out in [Step 6](#configure-attribute-mapping) into the Attribute Mapping section.

![Attribute mapping configuration](/docs/img/sso-dashboard-configure-attributes-generic.png)

<Admonition type="note">
  If you did not customize your settings you may save some time by clicking the **G Suite** preset.
</Admonition>



## Step 12: Join organization on signup (optional) \[#dashboard-configure-autojoin]

By default this setting is disabled, users logging in via SSO will not be added to your organization automatically.

![Auto-join disabled](/docs/img/sso-dashboard-configure-autojoin-disabled.png)

Toggle this on if you want SSO-authenticated users to be **automatically added to your organization** when they log in via SSO.

![Auto-join enable](/docs/img/sso-dashboard-configure-autojoin-enabled.png)

When auto-join is enabled, you can choose the **default role** for new users:

![Auto-join role selection](/docs/img/sso-dashboard-configure-autojoin-enabled-role.png)

Choose a role that fits the level of access you want to grant to new members.

<Admonition type="note">
  Visit [access-control](/docs/guides/platform/access-control) documentation for details about each role.
</Admonition>



## Step 13: Save changes and test single sign-on \[#dashboard-configure-save]

When you click **Save changes**, your new SSO configuration is applied immediately. From that moment, any user with an email address matching one of your configured domains who visits your organization's sign-in URL will be routed through the SSO flow.

We recommend asking a few users to test signing in via their Google Workspace account. They can do this by entering their email address on the [Sign in with SSO](/dashboard/sign-in-sso) page.

If SSO sign-in doesn't work as expected, contact your Supabase support representative for assistance.



---
**Navigation:** [← Previous](./07-aws-marketplace.md) | [Index](./index.md) | [Next →](./09-set-up-sso-with-okta.md)
