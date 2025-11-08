**Navigation:** [← Previous](./06-realtime-quotas.md) | [Index](./index.md) | [Next →](./08-hipaa-projects.md)

# AWS Marketplace



You can purchase Supabase through the AWS Marketplace. Buying through AWS Marketplace can mean simpler billing, faster progress toward your AWS spend commitments, and centralized purchasing across all your AWS accounts. Start the purchase process from our marketplace [product page](https://aws.amazon.com/marketplace/pp/prodview-zjciuce2qsb3q).

When you make a purchase on AWS Marketplace, AWS will calculate sales taxes, VAT, GST, service tax, etc. (“Indirect Taxes”), if applicable, based on the location of your AWS account. You can find more details in the [AWS tax help guide](https://aws.amazon.com/tax-help/marketplace-buyers/).


### Plans available through the AWS Marketplace

*   Free Plan: not available
*   Pro Plan: available, self-serve
*   Team Plan: available, self-serve
*   Enterprise Plan: available, via AWS Marketplace Private Offer. [Contact us](https://forms.supabase.com/enterprise) for more information.



## More information

*   Implications of managing your Supabase organization through the AWS Marketplace. Refer to the [Account Setup guide](./aws-marketplace/account-setup#implications-of-linking-a-supabase-organization-to-a-marketplace-subscription).
*   [AWS Marketplace FAQ](./aws-marketplace/faq)
*   General guidance on using the AWS Marketplace as a buyer. Refer to the [AWS documentation](https://docs.aws.amazon.com/marketplace/latest/buyerguide/using-aws-marketplace-as-a-subscriber.html).



## Next steps

*   Purchase Supabase through the AWS Marketplace. Refer to the [Getting Started guide](./aws-marketplace/getting-started).



# Database Backups



Database backups are an integral part of any disaster recovery plan. Disasters come in many shapes and sizes. It could be as simple as accidentally deleting a table column, the database crashing, or even a natural calamity wiping out the underlying hardware a database is running on. The risks and impact brought by these scenarios can never be fully eliminated, but only minimized or even mitigated. Having database backups is a form of insurance policy. They are essentially snapshots of the database at various points in time. When disaster strikes, database backups allow the project to be brought back to any of these points in time, therefore averting the crisis.

<Admonition type="note">
  The Supabase team regularly monitors the status of backups. In case of any issues, you can [contact support](/dashboard/support/new). Also you can check out our [status page](https://status.supabase.com/) at any time.
</Admonition>

<Admonition type="note">
  Once a project is deleted all associated data will be permanently removed, including any backups stored in S3. This action is irreversible and should be carefully considered before proceeding.
</Admonition>



## Types of backups

Database backups can be categorized into two types: **logical** and **physical**. You can learn more about them [here](/blog/postgresql-physical-logical-backups).

<Admonition type="note" label="Physical backups are not enabled by default">
  To enable physical backups, you have three options:

  *   Enable [Point-in-Time Recovery (PITR)](#point-in-time-recovery)
  *   [Increase your database size](/docs/guides/platform/database-size) to greater than 15GB
  *   [Create a read replica](/docs/guides/platform/read-replicas)

  Once a project satisfies at least one of the requirements for physical backups then logical backups are no longer made. However, your project may revert back to logical backups if you remove add-ons.
</Admonition>

You can confirm your project's backup type by navigating to [**Database Backups > Scheduled backups**](/dashboard/project/_/database/backups/scheduled) and if you can download a backup then it is logical, otherwise it is physical.

However, if your project has the Point-in-Time Recovery (PITR) add-on then the backups are physical and you can view them in [Database Backups > Point in time](/dashboard/project/_/database/backups/pitr).



## Frequency of backups

When deciding how often a database should be backed up, the key business metric Recovery Point Objective (RPO) should be considered. RPO is the threshold for how much data, measured in time, a business could lose when disaster strikes. This amount is fully dependent on a business and its underlying requirements. A low RPO would mean that database backups would have to be taken at an increased cadence throughout the day. Each Supabase project has access to two forms of backups, Daily Backups and Point-in-Time Recovery (PITR). The agreed upon RPO would be a deciding factor in choosing which solution best fits a project.

<Admonition type="note">
  If you enable PITR, Daily Backups will no longer be taken. PITR provides a finer granularity than Daily Backups, so it's unnecessary to run both.
</Admonition>

<Admonition type="note">
  Database backups do not include objects stored via the Storage API, as the database only includes metadata about these objects. Restoring an old backup does not restore objects that have been deleted since then.
</Admonition>



## Daily backups

All Pro, Team and Enterprise Plan Supabase projects are backed up automatically on a daily basis. In terms of Recovery Point Objective (RPO), Daily Backups would be suitable for projects willing to lose up to 24 hours worth of data if disaster hits at the most inopportune time. If a lower RPO is required, enabling Point-in-Time Recovery should be considered.

<Admonition type="note">
  For security purposes, passwords for custom roles are not stored in daily backups, and will not be found in downloadable files. As such, if you are restoring from a daily backup and are using custom roles, you will need to set their passwords once more following a completed restoration.
</Admonition>


### Backup process \[#daily-backups-process]

The Postgres utility [pg\_dumpall](https://www.postgresql.org/docs/current/app-pg-dumpall.html) is used to perform daily backups. An SQL file is generated, zipped up, and sent to our storage servers for safe keeping.

You can access daily backups in the [Scheduled backups](/dashboard/project/_/database/backups/scheduled) settings in the Dashboard. Pro Plan projects can access the last 7 days' worth of daily backups. Team Plan projects can access the last 14 days' worth of daily backups, while Enterprise Plan projects can access up to 30 days' worth of daily backups. Users can restore their project to any one of the backups. If you wish to generate a logical backup on your own, you can do so through the [Supabase CLI](/docs/reference/cli/supabase-db-dump).

You can also manage backups programmatically using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# List all available backups
curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  "https://api.supabase.com/v1/projects/$PROJECT_REF/database/backups"


# Restore from a PITR (not logical) backup (replace ISO timestamp with desired restore point)
curl -X POST "https://api.supabase.com/v1/projects/$PROJECT_REF/database/backups/restore-pitr" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "recovery_time_target_unix": "1735689600"
  }'
```


#### Backup process for large databases

Databases larger than 15GB\[^1], if they're on a recent build\[^2] of the Supabase platform, get automatically transitioned\[^3] to use daily physical backups. Physical backups are a more performant backup mechanism that lowers the overhead and impact on the database being backed up, and also avoids holding locks on objects in your database for a long period of time. While restores are unaffected, the backups created using this method cannot be downloaded from the Backups section of the dashboard.

This class of physical backups only allows for recovery to a fixed time each day, similar to daily backups. You can upgrade to [PITR](#point-in-time-recovery) for access to more granular recovery options.

Once a database is transitioned to using physical backups, it continues to use physical backups, even if the database size falls back below the threshold for the transition.

\[^1]: The threshold for transitioning will be slowly lowered over time. Eventually, all projects will be transitioned to using physical backups.

\[^2]: Projects created or upgraded after the 14th of July 2022 are eligible.

\[^3]: The transition to physical backups is handled transparently and does not require any user intervention. It involves a single restart of the database to pick up new configuration that can only be loaded at start; the expected downtime for the restart is a few seconds.


### Restoration process \[#daily-backups-restoration-process]

When selecting a backup to restore to, select the closest available one made before the desired point in time to restore to. Earlier backups can always be chosen too but do consider the number of days' worth of data that could be lost.

The Dashboard will then prompt for a confirmation before proceeding with the restoration. The project will be inaccessible following this. As such, do ensure to allot downtime beforehand. This is dependent on the size of the database. The larger it is, the longer the downtime will be. Once the confirmation has been given, the underlying SQL of the chosen backup is then run against the project. The Postgres utility [psql](https://www.postgresql.org/docs/current/app-psql.html) is used to facilitate the restoration. The Dashboard will display a notification once the restoration completes.

If your project is using subscriptions or replication slots, you will need to drop them prior to the restoration, and re-create them afterwards. The slot used by Realtime is exempted from this, and will be handled automatically.

{/* screenshot of the Dashboard of the project completing restoration */}



## Point-in-Time recovery

Point-in-Time Recovery (PITR) allows a project to be backed up at much shorter intervals. This provides users an option to restore to any chosen point of up to seconds in granularity. Even with daily backups, a day's worth of data could still be lost. With PITR, backups could be performed up to the point of disaster.

<Admonition type="note">
  Pro, Team and Enterprise Plan projects can enable PITR as an add-on.

  Projects interested in PITR will also need to use at least a Small compute add-on, in order to ensure smooth functioning.
</Admonition>

<Admonition type="note">
  If you enable PITR, Daily Backups will no longer be taken. PITR provides a finer granularity than Daily Backups, so it's unnecessary to run both.
</Admonition>

When you disable PITR, all new backups will still be taken as physical backups only. Physical backups can still be used for restoration, but they are not available for direct download. If you need to download a backup after PITR is disabled, you’ll need to take a manual [logical backup using the Supabase CLI or pg\_dump](/docs/guides/platform/migrating-within-supabase/backup-restore#backup-database-using-the-cli).

<Admonition type="note">
  If PITR has been disabled, logical backups remain available until they pass the backup retention period for your plan. After that window passes, only physical backups will be shown.
</Admonition>


### Backup process \[#pitr-backup-process]

As discussed [here](/blog/postgresql-physical-logical-backups), PITR is made possible by a combination of taking physical backups of a project, as well as archiving [Write Ahead Log (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) files. Physical backups provide a snapshot of the underlying directory of the database, while WAL files contain records of every change made in the database.

Supabase uses [WAL-G](https://github.com/wal-g/wal-g), an open source archival and restoration tool, to handle both aspects of PITR. On a daily basis, a snapshot of the database is taken and sent to our storage servers. Throughout the day, as database transactions occur, WAL files are generated and uploaded.

By default, WAL files are backed up at two minute intervals. If these files cross a certain file size threshold, they are backed up immediately. As such, during periods of high amount of transactions, WAL file backups become more frequent. Conversely, when there is no activity in the database, WAL file backups are not made. Overall, this would mean that at the worst case scenario or disaster, the PITR achieves a Recovery Point Objective (RPO) of two minutes.

![PITR dashboard](/docs/img/backups-pitr-dashboard.png)

You can access PITR in the [Point in Time](/dashboard/project/_/database/backups/pitr) settings in the Dashboard. The recovery period of a project is indicated by the earliest and latest points of recoveries displayed in your preferred timezone. If need be, the maximum amount of this recovery period can be modified accordingly.

Note that the latest restore point of the project could be significantly far from the current time. This occurs when there has not been any recent activity in the database, and therefore no WAL file backups have been made recently. This is perfectly fine as the state of the database at the latest point of recovery would still be indicative of the state of the database at the current time given that no transactions have been made in between.


### Restoration process \[#pitr-restoration-process]

![PITR: Calendar view](/docs/img/backups-pitr-calendar-view.png)

A date and time picker will be provided upon pressing the `Start a restore` button. The process will only proceed if the selected date and time fall within the earliest and latest points of recoveries.

![PITR: Confirmation modal](/docs/img/backups-pitr-confirmation-modal.png)

After locking in the desired point in time to recover to, The Dashboard will then prompt for a review and confirmation before proceeding with the restoration. The project will be inaccessible following this. As such, do ensure to allot for downtime beforehand. This is dependent on the size of the database. The larger it is, the longer the downtime will be. Once the confirmation has been given, the latest physical backup available is downloaded to the project and the database is partially restored. WAL files generated after this physical backup up to the specified point-in-time are then downloaded. The underlying records of transactions in these files are replayed against the database to complete the restoration. The Dashboard will display a notification once the restoration completes.


### Pricing

Pricing depends on the recovery retention period, which determines how many days back you can restore data to any chosen point of up to seconds in granularity.

| Recovery Retention Period in Days | Hourly Price USD        | Monthly Price USD     |
| --------------------------------- | ----------------------- | --------------------- |
| 7                                 | <Price price="0.137" /> | <Price price="100" /> |
| 14                                | <Price price="0.274" /> | <Price price="200" /> |
| 28                                | <Price price="0.55" />  | <Price price="400" /> |

For a detailed breakdown of how charges are calculated, refer to [Manage Point-in-Time Recovery usage](/docs/guides/platform/manage-your-usage/point-in-time-recovery).



## Restore to a new project

See the [Duplicate Project docs](/docs/guides/platform/clone-project).



## Troubleshooting


### Logical backups


#### `search_path` issues

During the `pg_restore` process, the `search_path` is set to an empty string for predictability, and security. Using unqualified references to functions or relations can cause restorations using logical backups to fail, as the database will not be able to locate the function or relation being referenced. This can happen even if the database functions without issues during normal operations, as the `search_path` is usually set to include several schemas during normal operations. Therefore, you should always use schema-qualified names within your SQL code.

You can refer to [an example PR](https://github.com/supabase/supabase/pull/28393/files) on how to update SQL code to use schema-qualified names.


#### Invalid check constraints

Postgres requires that [check constraints](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-CHECK-CONSTRAINTS) be:

1.  immutable
2.  not reference table data other than the new or updated row being checked

Violating these requirements can result in numerous failure scenarios, including during logical restorations.

Common examples of check constraints that can result in such failures are:

*   validating against the current time, e.g. that the row being inserted references a future event
*   validating the contents of a row against the contents of another table


#### Views that reference themselves

Views that directly or indirectly reference themselves will cause logical restores to fail due to cyclic dependency errors. These views are also invalid and unusable in Postgres, and any query against them will result in a runtime error.

**Example:**

```
-- Direct self-reference
CREATE VIEW my_view AS
  SELECT * FROM my_view;

-- Indirect circular reference
CREATE VIEW v1 AS SELECT * FROM v2;
CREATE VIEW v2 AS SELECT * FROM v1;
```

\-- Drop the offending view from your database, or delete them from the logical backup to make it restorable.

Postgres documentation [views](https://www.postgresql.org/docs/current/sql-createview.html)



# Billing FAQ

This documentation covers frequently asked questions around subscription plans, payments, invoices and billing in general

{/* supa-mdx-lint-disable Rule004ExcludeWords */}



## Organizations and projects


#### What are organizations and projects?

The Supabase Platform has "organizations" and "projects". An organization may contain multiple projects. Each project is a dedicated Supabase instance with all of its sub-services including Storage, Auth, Functions and Realtime.
Each organization only has a single subscription with a single plan (Free, Pro, Team or Enterprise). Project add-ons such as [Compute](/docs/guides/platform/compute-add-ons), [IPv4](/docs/guides/platform/ipv4-address), [Log Drains](/docs/guides/platform/log-drains), [Advanced MFA](/docs/guides/auth/auth-mfa/phone), [Custom Domains](/docs/guides/platform/custom-domains) and [PITR](/docs/guides/platform/backups#point-in-time-recovery) are configured per project and are added to your organization subscription.

Read more on [About billing on Supabase](/docs/guides/platform/billing-on-supabase#organization-based-billing).


#### How many free projects can I have?

You are entitled to two active free projects. Paused projects do not count towards your quota. Note that within an organization, we count the free project limits from all members that are either Owner or Admin. If you’ve got another organization member with the Admin or Owner role that has already exhausted their free project quota, you won’t be able to launch another free project in that organization. You can create another Free Plan organization or change the role of the affected member in your [organization’s team settings](/dashboard/org/_/team).


#### Can I mix free and paid projects in a single organization?

The subscription plan is set on the organization level and it is not possible to mix paid and non-paid projects inside a single organization. However, you can have a paid and a free organization and make use of the [self-serve project transfers](/docs/guides/platform/project-transfer) to organize your projects. All projects in an organization benefit from the subscription plan. If your organization is on the Pro Plan, all projects within the organization benefit from no project pausing, automated backups and so on.


#### Can I transfer my projects to another organization?

Yes, you can transfer your projects to another organization. You can find instructions on how to transfer your projects [here](/docs/guides/platform/project-transfer).


#### Can I transfer my credits to another organization?

Yes, you can transfer the credits to another organization. Submit a [support ticket](https://supabase.help).



## Pricing

See the [Pricing page](/pricing) for details.


#### Are there any charges for paused projects?

No, we do not charge for paused projects. Compute hours are only counted for active instances. Paused projects do not incur any compute usage charges.


#### How are multiple projects billed under a paid organization?

We provide a dedicated server for every Supabase project. Each paid organization comes with <Price price="10" /> in Compute Credits to cover one project on the default compute size. Additional projects start at ~<Price price="10" /> a month (billed hourly).

Running 3 projects in a Pro Plan organization on the default Micro instance:

*   <Price price="25" /> Pro Plan
*   <Price price="30" /> for 3 projects on the default compute size
*   <Price price="10" /> Compute credits ⇒ <Price price="45" /> / month

Refer to our [Compute](/docs/guides/platform/manage-your-usage/compute#billing-examples) docs for more examples and insights.


#### How does compute billing work?

Each Supabase project is a dedicated VM and Postgres database. By default, your instance runs on the Micro compute instance. You have the option to upgrade your compute size in your [Project settings](/dashboard/project/_/settings/addons). See [Compute Add-ons](/docs/guides/platform/compute-add-ons) for available options.

When you change your compute size, there are no immediate upfront charges. Instead, you will be billed based on the compute hours during your billing cycle reset.

If you launch additional instances on your paid plan, we will add the corresponding compute hours to your final invoice.

If you upgrade your project to a larger instance for 10 hours and then downgrade, you’ll only pay for the larger instance for the 10 hours of usage at the end of your billing cycle. You can see your current compute usage on your [organization’s usage page](/dashboard/org/_/usage).

Read more about [Compute usage](/docs/guides/platform/manage-your-usage/compute).


#### What is egress and how is it billed?

Egress refers to the total bandwidth (network traffic) quota available to each organization. This quota can be utilized for various purposes such as Storage, Realtime, Auth, Functions, Supavisor, Log Drains and Database. Each plan includes a specific egress quota, and any additional usage beyond that quota is billed accordingly.

We differentiate between cached (served via our CDN from cache hits) and uncached egress and give quotas for each type and have varying pricing (cached egress is cheaper). Cached egress only applies to Storage.

Read more about [Egress usage](/docs/guides/platform/manage-your-usage/egress).



## Plans and subscriptions


#### How do I change my subscription plan?

Change your subscription plan in your [organization's billing settings](/dashboard/org/_/billing). To upgrade to an Enterprise Plan, complete the [Enterprise request form](https://forms.supabase.com/enterprise).


#### What happens if I cancel my subscription?

The organization is given [credits](/docs/guides/platform/credits) for unused time on the subscription plan. The credits will not expire and can be used again in the future. You may see an additional charge for unbilled excessive usage charges from your previous billing cycle.

Read more about [downgrades](/docs/guides/platform/manage-your-subscription#downgrade).


#### I mistakenly upgraded the wrong organization and then downgraded it. Could you issue a refund?

We can transfer the amount as [credits](/docs/guides/platform/credits) to another organization of your choice. You can use these credits to upgrade the organization, or if you have already upgraded, the credits will be used to pay the next month's invoice. Please create a [support ticket](https://supabase.help) for this case.



## Quotas and spend caps


#### What will happen when I exceed the Free Plan quota?

You will be notified when you exceed the Free Plan quota. It is important to take action at this point. If you continue to exceed the limits without reducing your usage, service restrictions will apply. To avoid service restrictions, you have two options: reduce your usage or upgrade to a paid plan. Learn more about restrictions in the [Fair Use Policy](#fair-use-policy) section.


#### What will happen when I exceed the Pro Plan quota and have the spend cap on?

You will be notified when you exceed your Pro Plan quota. To unblock yourself, you can toggle off your spend cap in your [organization's billing settings](/dashboard/org/_/billing) to pay for over-usage beyond the Pro plans limits. If you continue to exceed the limits without reducing your usage or turning off the spend cap, restrictions will apply. Learn more about restrictions in the [Fair Use Policy](#fair-use-policy) section.


#### How do I scale beyond the limits of my Pro Plan?

The Pro Plan has a Spend Cap enabled by default to keep costs under control. If you want to scale beyond the plan's included quota, switch off the Spend Cap to pay for additional usage beyond the plans included limits. You can toggle the Spend Cap in the [organization's billing settings](/dashboard/org/_/billing). Read more about the [Spend Cap](/docs/guides/platform/cost-control#spend-cap).



## Fair Use Policy


#### What is the Fair Use Policy?

Our Fair Use Policy gives developers the freedom to build and experiment with Supabase, while protecting our infrastructure. Under the Fair Use policy, service restrictions may apply to your organization if:

*   You continually exceed the Free Plan quota
*   You continually exceed Pro Plan quota and have the spend cap enabled
*   You have overdue invoices
*   You have an expired credit card

You will receive a notification before Fair Use Policy restrictions are applied. However, in some cases, like suspected abuse of our services, restrictions may be applied without prior notice.


#### What is a grace period and does it reset after usage drops?

When your organization exceeds plan limits, you receive a grace period before fair use policy applies. After this grace period ends, the dashboard will continue to show a notice indicating that your grace period is over, even if you have dropped back under plan limits. This is a warning that serves as an indicator that your organization previously exceeded usage limits.

This persistent warning means that if you exceed your plan limits again, you will not receive another grace period and your project will be restricted. The notice and indicator will automatically clear if you continue to stay under plan limits for multiple billing cycles.


#### How is the Fair Use Policy applied?

The Fair Use Policy is applied through service restrictions. This could mean:

*   Pausing projects
*   Switching databases to read-only mode
*   Disabling new project launches/transfers
*   Responding with a [402 status code](/docs/guides/platform/http-status-codes#402-service-restriction) for all API requests

The Fair Use Policy is generally applied to all projects of the restricted organization.


#### How can I remove restrictions applied from the Fair Use Policy?

To remove restrictions, you will need to address the issue that caused the restriction. This could be reducing your usage, paying overdue invoices, updating your payment method, or any other issue that caused the restriction. Once the issue is resolved, the restriction will be lifted.

Restrictions due to usage limits are lifted with the next billing cycle as your quota refills at the beginning of each cycle. You can see when your current billing cycle ends on the [billing page](/dashboard/org/_/billing) under "Upcoming Invoice". You can also lift restrictions immediately by [upgrading](/dashboard/org/_/billing?panel=subscriptionPlan) to Pro (if on Free Plan) or by [disabling spend cap](/dashboard/org/_/billing?panel=costControl) (if on Pro Plan with spend cap enabled).



## Reports and invoices


#### Where do I find my invoices?

You can find all invoices from your organization on your [organization’s invoices page](/dashboard/org/_/billing#invoices).


#### Where can I see a breakdown of usage?

You can find the breakdown of your usage on your [organization’s usage page](/dashboard/org/_/usage).


#### Where can I check my credit balance?

You can check your Credit balance on the [organization’s billing page](/dashboard/org/_/billing). Credits will be used on future invoices before charging your payment method. If you have enough credits to cover an invoice, there is no charge at all.


#### Can I include the VAT number?

You can update your VAT number in the Tax ID section of your [organization’s billing page](/dashboard/org/_/billing).


#### Can I change the details of an existing invoice?

Any changes made to your billing details will only be reflected in your upcoming invoices. Our payment provider cannot regenerate previous invoices. Therefore, make sure to update the billing details before the upcoming invoices are finalized.



## Payments and billing cycle


#### What payment methods are available?

We accept credit card payments only. If you cannot pay via credit card, we do offer alternatives for larger upfront payments. Create a [support ticket](https://supabase.help) in case you’re interested.


#### What credit card brands are supported?

Visa, Mastercard, American Express, Japan Credit Bureau (JCB), China UnionPay (CUP), Cartes Bancaires


#### What currency can I pay in?

All our invoices are issued in USD, but you can pay in any currency so long as the credit card provider allows charging in USD after conversion.


#### Can I change the payment method?

Yes, you will have to add the new payment method before being allowed to remove the old one.
This can be done from your dashboard on the [organization’s billing page](/dashboard/org/_/billing).

Read more on [Manage your payment methods](/docs/guides/platform/manage-your-subscription#manage-your-payment-methods).


#### Can I pay upfront for multiple months?

You can top up your credit balance to cover multiple months through your [organization’s billing page](/dashboard/org/_/billing).

Read more on [Credit top-ups](/docs/guides/platform/credits#credit-top-ups).


#### When are payments taken?

Payments are taken at the beginning of each billing cycle. You will be charged once a month. You can see the current billing cycle and upcoming invoice in your [organization's billing settings](/dashboard/org/_/billing). The subscription plan fee is charged upfront, whereas usage-charges, including compute, are charged in arrears based on your usage.

Read more on [Your monthly invoice](/docs/guides/platform/your-monthly-invoice).


#### Where can I change my billing details?

You can update your billing details on the [organization’s billing page](/dashboard/org/_/billing).
Note that any changes made to your billing details will only be reflected in your upcoming invoices. Our payment provider cannot regenerate previous invoices.


#### What happens if I am unable to make the payment?

When an invoice becomes overdue, we will pause your projects and downgrade your organization to the Free Plan. You will be able to restore your projects once you have paid all outstanding invoices.


#### Why am I overdue?

We were unable to charge your payment method. This likely means that the payment was not successfully processed with the credit card on your account profile.
You can be overdue when

*   A card is expired
*   The bank declined the payment
*   You had insufficient funds
*   There was no card on record

Check your payment methods in your [organization’s billing page](/dashboard/org/_/billing) to ensure there are no expired payment methods and the correct payment method is marked as default.
If you are still facing issues, raise a [support ticket](https://supabase.help).

Payments are always in USD and may show up as coming from Singapore, given our payment entity is in Singapore. Make sure you allow payments from Singapore and in USD


#### Can I delay my payment?

No, you cannot delay your payment.


#### Can I get a refund of my unused credits?

No, we do not provide refunds. Please refer to our [Terms of Service](/terms#1-fees).


#### What do I do if my bill looks wrong?

Take a moment to review our [Your monthly invoice](/docs/guides/platform/your-monthly-invoice) page, which may help clarify any questions about your invoice. If it still looks wrong, submit a [support ticket](https://supabase.help) through the dashboard. Select the affected organization and provide the invoice number for us to look at your case.



# About billing on Supabase




## Subscription plans

Supabase offers different subscription plans—Free, Pro, Team, and Enterprise. For a closer look at each plan's features and pricing, visit our [pricing page](/pricing).


### Free Plan

The Free Plan helps you get started and explore the platform. You are granted two free projects. The project limit applies across all organizations where you are an Owner or Administrator. This means you could have two Free Plan organizations with one project each, or one Free Plan organization with two projects. Paused projects do not count towards your free project limit.


### Paid plans

Upgrading your organization to a paid plan provides additional features, and you receive a higher [usage quota](/docs/guides/platform/billing-on-supabase#variable-usage-fees-and-quotas). You unlock the benefits of the paid plan for all projects within your organization - for example, no projects in your Pro Plan organization will be paused.



## Organization-based billing

Supabase bills separately for each organization. Each organization has its own subscription, including a unique subscription plan (Free, Pro, Team, or Enterprise), payment method, billing cycle, and invoices.

Different plans cannot be mixed within a single organization. For example, you cannot have both a Pro Plan project and a Free Plan project in the same organization. To have projects on different plans, you must create separate organizations. See [Project Transfers](/docs/guides/platform/project-transfer) if you need to move a project to a different organization.

<div className="text-center">
  <Image
    alt="Organization-based billing"
    src={{
      light: '/docs/img/guides/platform/billing-overview--light.png',
      dark: '/docs/img/guides/platform/billing-overview.png',
    }}
    className="max-w-[600px] inline-block"
    zoomable
  />
</div>



## Costs

Monthly costs for paid plans include a fixed subscription fee based on your chosen plan and variable usage fees. To learn more about billing and cost management, refer to the following resources.

*   [Your monthly invoice](/docs/guides/platform/your-monthly-invoice) - For a detailed breakdown of what a monthly invoice includes
*   [Manage your usage](/docs/guides/platform/manage-your-usage) - For details on how the different usage items are billed, and how to optimize usage and reduce costs
*   [Control your costs]() - For details on how you can control your costs in case unexpected high usage occurs


### Compute costs for projects

An organization can have multiple projects. Each project includes a dedicated Postgres instance running on its own server. You are charged for the Compute resources of that server, independent of your database usage.

<Admonition type="caution">
  Each project you launch increases your monthly Compute costs.
</Admonition>

Read more about [Compute costs](/docs/guides/platform/manage-your-usage/compute).



## Variable Usage Fees and Quotas

Each subscription plan includes a built-in quota for some selected usage items, such as [Egress](/docs/guides/platform/manage-your-usage/egress), [Storage Size](/docs/guides/platform/manage-your-usage/storage-size), or [Edge Function Invocations](/docs/guides/platform/manage-your-usage/edge-function-invocations). This quota represents your free usage allowance. If you stay within it, you incur no extra charges for these items. Only usage beyond the quota is billed as overage.

For usage items without a quota, such as [Compute](/docs/guides/platform/manage-your-usage/compute) or [Custom Domains](/docs/guides/platform/manage-your-usage/custom-domains), you are charged for your entire usage.

The quota is applied to your entire organization, independent of how many projects you launch within that organization. For billing purposes, we sum the usage across all projects in a monthly invoice.

| Usage Item                       | Free                     | Pro/Team                                                            | Enterprise |
| -------------------------------- | ------------------------ | ------------------------------------------------------------------- | ---------- |
| Egress                           | 5 GB                     | 250 GB included, then <Price price="0.09" /> per GB                 | Custom     |
| Database Size                    | 500 MB per project       | 8 GB disk per project included, then <Price price="0.125" /> per GB | Custom     |
| Monthly Active Users             | 50,000 MAU               | 100,000 MAU included, then <Price price="0.00325" /> per MAU        | Custom     |
| Monthly Active Third-Party Users | 50,000 MAU               | 100,000 MAU included, then <Price price="0.00325" /> per MAU        | Custom     |
| Monthly Active SSO Users         | Unavailable on Free Plan | 50 MAU included, then <Price price="0.015" /> per MAU               | Custom     |
| Storage Size                     | 1 GB                     | 100 GB included, then <Price price="0.021" /> per GB                | Custom     |
| Storage Images Transformed       | Unavailable on Free Plan | 100 included, then <Price price="5" /> per 1000                     | Custom     |
| Edge Function Invocations        | 500,000                  | 2 million included, then <Price price="2" /> per million            | Custom     |
| Realtime Message Count           | 2 million                | 5 million included, then <Price price="2.5" /> per million          | Custom     |
| Realtime Peak Connections        | 200                      | 500 included, then <Price price="10" /> per 1000                    | Custom     |

You can find a detailed breakdown of all usage items and how they are billed on the [Manage your usage](/docs/guides/platform/manage-your-usage) page.



## Project add-ons

While your subscription plan applies to your entire organization and is charged only once, you can enhance individual projects by opting into various add-ons.

*   [Compute](/docs/guides/platform/compute-and-disk#compute) to scale your database up to 64 cores and 256 GB RAM
*   [Read Replicas](/docs/guides/platform/read-replicas) to scale read operations and provide resiliency
*   [Disk](/docs/guides/platform/compute-and-disk#disk) to provision extra IOPS/throughput or use a high-performance SSD
*   [Log Drains](/docs/guides/telemetry/log-drains) to sync Supabase logs to a logging system of your choice
*   [Custom Domains](/docs/guides/platform/custom-domains) to provide a branded experience
*   [PITR](/docs/guides/platform/backups#point-in-time-recovery) to roll back to any specific point in time, down to the minute
*   [IPv4](/docs/guides/platform/ipv4-address) for a dedicated IPv4 address
*   [Advanced MFA](/docs/guides/auth/auth-mfa/phone) to provide other options than TOTP



# Restore to a new project

How to clone your existing Supabase project

<Admonition type="note" label="Beta Version">
  You can clone your Supabase project by restoring your data from an existing project into a completely new one. This process creates a database-only copy and requires manual reconfiguration to fully replicate your original project.
</Admonition>

**What will be transferred?**

*   Database schema (tables, views, procedures)
*   All data and indexes
*   Database roles, permissions and users
*   Auth user data (user accounts, hashed passwords, and authentication records from the auth schema)

**What needs manual reconfiguration?**

*   Storage objects & settings (Your S3/storage files and bucket configurations are **NOT** copied)
*   Edge Functions
*   Auth settings & API keys
*   Realtime settings
*   Database extensions and settings
*   Read replicas

Whether you're using physical backups or Point-in-Time recovery (PITR), this feature allows you to duplicate project data with ease, perform testing safely, or recover data for analysis. Access to this feature is exclusive to users on paid plans and requires that physical backups are enabled for the source project.

<Admonition type="note">
  PITR is an additional add-on available for organizations on a paid plan with physical backups enabled.
</Admonition>

To begin, switch to the source project—the project containing the data you wish to restore—and go to the [database backups](/dashboard/project/_/database/backups/restore-to-new-project) page. Select the **Restore to a New Project** tab.

A list of available backups is displayed. Select the backup you want to use and click the "Restore" button. For projects with PITR enabled, use the date and time selector to specify the exact point in time from which you wish to restore data.

Once you’ve made your choice, Supabase takes care of the rest. A new project is automatically created, replicating key configurations from the original, including the compute instance size, disk attributes, SSL enforcement settings, and network restrictions. The data will remain in the same region as the source project to ensure compliance with data residency requirements. The entire process is fully automated.

<Admonition type="note">
  The time required to complete the restoration can vary depending largely on the volume of data involved. If you have a large amount of data you can opt for higher performing disk attributes on the source project *before* starting a clone operation. These disk attributes will be replicated to the new project. This incurs additional costs which will be displayed before starting.
</Admonition>

There are a few important restrictions to be aware of with the "Restore to a New Project" process:

*   Projects that are created through the restoration process cannot themselves be used as a source for further clones at this time.
*   The feature is only accessible to paid plan users with physical backups enabled, ensuring that the necessary resources and infrastructure are available for the restore process.

Before starting the restoration, you’ll be presented with an overview of the costs associated with creating the new project. The new project will incur additional monthly expenses based on the mirrored resources from the source project. It’s important to review these costs carefully before proceeding.

Once the restoration is complete, the new project will be available in your dashboard and will include all data, tables, schemas, and selected settings from the chosen backup source. It is recommended to thoroughly review the new project and perform any necessary tests to ensure everything has been restored as expected.

New projects are completely independent of their source, and as such can be modified and used as desired.

<Admonition type="note">
  As the entire database is copied to the new project, this will include all extensions that were enabled at the source. If the source project included extensions that are configured to carry out external operations—for example pg\_net, pg\_cron, wrappers—these should be disabled once the copy process has completed to avoid any unwanted actions from taking place.
</Admonition>

Restoring to a new project is an excellent way to manage environments more effectively. You can use this feature to create staging environments for testing, experiment with changes without risk to production data, or swiftly recover from unexpected data loss scenarios.



# Compute and Disk




## Compute

Every project on the Supabase Platform comes with its own dedicated Postgres instance.

The following table describes the base instances, Nano (free plan) and Micro (paid plans), with additional compute instance sizes available if you need extra performance when scaling up.

<Admonition type="note" label="Nano instances in paid plan organizations">
  In paid organizations, Nano Compute are billed at the same price as Micro Compute. It is recommended to upgrade your Project from Nano Compute to Micro Compute when it's convenient for you. Compute sizes are not auto-upgraded because of the downtime incurred. See [Supabase Pricing](/pricing) for more information. You cannot launch Nano instances on paid plans, only Micro and above - but you might have Nano instances after upgrading from Free Plan.
</Admonition>

| Compute Size | Hourly Price USD          | Monthly Price USD                                                                                        | CPU                     | Memory       | Max DB Size (Recommended)\[^2] |
| ------------ | ------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------- | ------------ | ----------------------------- |
| Nano\[^3]     | <Price price="0" />       | <Price price="0" />                                                                                      | Shared                  | Up to 0.5 GB | 500 MB                        |
| Micro        | <Price price="0.01344" /> | ~<Price price="10" />                                                                                   | 2-core ARM (shared)     | 1 GB         | 10 GB                         |
| Small        | <Price price="0.0206" />  | ~<Price price="15" />                                                                                   | 2-core ARM (shared)     | 2 GB         | 50 GB                         |
| Medium       | <Price price="0.0822" />  | ~<Price price="60" />                                                                                   | 2-core ARM (shared)     | 4 GB         | 100 GB                        |
| Large        | <Price price="0.1517" />  | ~<Price price="110" />                                                                                  | 2-core ARM (dedicated)  | 8 GB         | 200 GB                        |
| XL           | <Price price="0.2877" />  | ~<Price price="210" />                                                                                  | 4-core ARM (dedicated)  | 16 GB        | 500 GB                        |
| 2XL          | <Price price="0.562" />   | ~<Price price="410" />                                                                                  | 8-core ARM (dedicated)  | 32 GB        | 1 TB                          |
| 4XL          | <Price price="1.32" />    | ~<Price price="960" />                                                                                  | 16-core ARM (dedicated) | 64 GB        | 2 TB                          |
| 8XL          | <Price price="2.562" />   | ~<Price price="1" />,870                                                                                | 32-core ARM (dedicated) | 128 GB       | 4 TB                          |
| 12XL         | <Price price="3.836" />   | ~<Price price="2" />,800                                                                                | 48-core ARM (dedicated) | 192 GB       | 6 TB                          |
| 16XL         | <Price price="5.12" />    | ~<Price price="3" />,730                                                                                | 64-core ARM (dedicated) | 256 GB       | 10 TB                         |
| >16XL        | -                         | [Contact Us](/dashboard/support/new?category=sales\&subject=Enquiry%20about%20larger%20instance%20sizes) | Custom                  | Custom       | Custom                        |

\[^1]: Database max connections are recommended values and can be customized depending on your use case.

\[^2]: Database size for each compute instance is the default recommendation but the actual performance of your database has many contributing factors, including resources available to it and the size of the data contained within it. See the [shared responsibility model](/docs/guides/platform/shared-responsibility-model) for more information.

\[^3]: Compute resources on the Free plan are subject to change.

Compute sizes can be changed by first selecting your project in the dashboard [here](/dashboard/project/_/settings/compute-and-disk) and the upgrade process will [incur downtime](/docs/guides/platform/compute-and-disk#upgrades).

<Image
  alt="Compute Size Selection"
  src={{
    light: '/docs/img/guides/platform/compute-size-selection--light.png',
    dark: '/docs/img/guides/platform/compute-size-selection--dark.png',
  }}
  zoomable
  className="max-w-[500px]"
/>

We charge hourly for additional compute based on your usage. Read more about [usage-based billing for compute](/docs/guides/platform/manage-your-usage/compute).


### Dedicated vs shared CPU

All Postgres databases on Supabase run in isolated environments. Compute instances smaller than `Large` compute size have CPUs which can burst to higher performance levels for short periods of time. Instances bigger than `Large` have predictable performance levels and do not exhibit the same burst behavior.


### Compute upgrades \[#upgrades]

<Admonition type="caution">
  Compute instance changes are usually applied with less than 2 minutes of downtime, but can take longer depending on the underlying Cloud Provider.
</Admonition>

When considering compute upgrades, assess whether your bottlenecks are hardware-constrained or software-constrained. For example, you may want to look into [optimizing the number of connections](/docs/guides/platform/performance#optimizing-the-number-of-connections) or [examining query performance](/docs/guides/platform/performance#examining-query-performance). When you're happy with your Postgres instance's performance, then you can focus on additional compute resources. For example, you can load test your application in staging to understand your compute requirements. You can also start out on a smaller tier, [create a report](/dashboard/project/_/reports) in the Dashboard to monitor your CPU utilization, and upgrade as needed.



## Disk

Supabase databases are backed by high performance SSD disks. The *effective performance* depends on a combination of all the following factors:

*   Compute size
*   Provisioned Disk Throughput
*   Provisioned Disk IOPS: Input/Output Operations per Second, which measures the number of read and write operations.
*   Disk type: io2 or gp3
*   Disk size

<Admonition type="note">
  The disk size and the disk type dictate the maximum IOPS and throughput that can be provisioned. The effective IOPS is the lower of the IOPS supported by the compute size or the provisioned IOPS of the disk. Similarly, the effective throughout is the lower of the throughput supported by the compute size and the provisioned throughput of the disk.
</Admonition>

The following sections explain how these attributes affect disk performance.


### Compute size

The compute size of your project sets the upper limit for disk throughput and IOPS. The table below shows the limits for each instance size. For instance, an 8XL compute instance has a maximum throughput of 9,500 Mbps and a maximum IOPS of 40,000.

| Compute Instance | Disk Throughput | IOPS        |
| ---------------- | --------------- | ----------- |
| Nano (free)      | 43 Mbps         | 250 IOPS    |
| Micro            | 87 Mbps         | 500 IOPS    |
| Small            | 174 Mbps        | 1,000 IOPS  |
| Medium           | 347 Mbps        | 2,000 IOPS  |
| Large            | 630 Mbps        | 3,600 IOPS  |
| XL               | 1,188 Mbps      | 6,000 IOPS  |
| 2XL              | 2,375 Mbps      | 12,000 IOPS |
| 4XL              | 4,750 Mbps      | 20,000 IOPS |
| 8XL              | 9,500 Mbps      | 40,000 IOPS |
| 12XL             | 14,250 Mbps     | 50,000 IOPS |
| 16XL             | 19,000 Mbps     | 80,000 IOPS |

Smaller compute instances like Nano, Micro, Small, and Medium have baseline performance levels that can occasionally be exceeded for short periods of time. If it does exceed the baseline, you should consider upgrading your instance size for a more reliable performance.

Larger compute instances (4XL and above) are designed for sustained, high performance with specific IOPS and throughput limits which you can [configure](/docs/guides/platform/manage-your-usage/disk-throughput). If you hit your IOPS or throughput limit, throttling will occur.


### Choosing the right compute instance for consistent disk performance

If you need consistent disk performance, choose the 4XL or larger compute instance. If you're unsure of how much throughput or IOPS your application requires, you can load test your project and inspect these [metrics in the Dashboard](/dashboard/project/_/reports). If the `Disk IO % consumed` stat is more than 1%, it indicates that your workload has exceeded the baseline IO throughput during the day. If this metric goes to 100%, the workload has used up all available disk IO budget. Projects that use any disk IO budget are good candidates for upgrading to a larger compute instance with higher throughput.


### Provisioned disk throughput and IOPS

The default disk type is gp3, which comes with a baseline throughput of 125 MB/s and a default IOPS of 3,000. You can provision additional IOPS and throughput from the [Database Settings](/dashboard/project/_/settings/compute-and-disk) page, but keep in mind that the effective IOPS and throughput will be limited by the compute instance size. This requires Large compute size or above.

<Admonition type="caution">
  Be aware that increasing IOPS or throughput incurs additional charges.
</Admonition>


### Disk types

When selecting your disk, it's essential to focus on the performance needs of your workload. Here's a comparison of our available disk types:

|                   | General Purpose SSD (gp3)                                                                                                                                                                          | High Performance SSD (io2)                                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Use Case**      | General workloads, development environments, small to medium databases                                                                                                                             | High-performance needs, large-scale databases, mission-critical applications                                                             |
| **Max Disk Size** | 16 TB                                                                                                                                                                                              | 60 TB                                                                                                                                    |
| **Max IOPS**      | 16,000 IOPS (at 32 GB disk size)                                                                                                                                                                   | 80,000 IOPS (at 80 GB disk size)                                                                                                         |
| **Throughput**    | 125 MB/s (default) to 1,000 MB/s (maximum)                                                                                                                                                         | Automatically scales with IOPS                                                                                                           |
| **Best For**      | Great value for most use cases                                                                                                                                                                     | Low latency and very high IOPS requirements                                                                                              |
| **Pricing**       | Disk: 8 GB included, then <Price price="0.125" /> per GB<br />IOPS: 3,000 included, then <Price price="0.024" /> per IOPS<br />Throughput: 125 MB/s included, then <Price price="0.95" /> per MB/s | Disk: <Price price="0.195" /> per GB<br />IOPS: <Price price="0.119" /> per IOPS<br />Throughput: Scales with IOPS at no additional cost |

For general, day-to-day operations, gp3 should be more than enough. If you need high throughput and IOPS for critical systems, io2 will provide the performance required.

<Admonition type="note">
  Compute instance size changes will not change your selected disk type or disk size, but your IO limits may change according to what your selected compute instance size supports.
</Admonition>


### Disk size

*   General Purpose (gp3) disks come with a baseline of 3,000 IOPS and 125 MB/s. You can provision additional 500 IOPS for every GB of disk size and additional 0.25 MB/s throughput per provisioned IOPS.
*   High Performance (io2) disks can be provisioned with 1,000 IOPS per GB of disk size.



## Limits and constraints


### Postgres replication slots, WAL senders, and connections

[Replication Slots](https://postgresqlco.nf/doc/en/param/max_replication_slots) and [WAL Senders](https://postgresqlco.nf/doc/en/param/max_wal_senders/) are used to enable [Postgres Replication](/docs/guides/database/replication). Each compute instance also has limits on the maximum number of database connections and connection pooler clients it can handle.

The maximum number of replication slots, WAL senders, database connections, and pooler clients depends on your compute instance size, as follows:

| Compute instance | Max Replication Slots | Max WAL Senders | Database Max Connections\[^1] | Connection Pooler Max Clients |
| ---------------- | --------------------- | --------------- | ---------------------------- | ----------------------------- |
| Nano (free)      | 5                     | 5               | 60                           | 200                           |
| Micro            | 5                     | 5               | 60                           | 200                           |
| Small            | 5                     | 5               | 90                           | 400                           |
| Medium           | 5                     | 5               | 120                          | 600                           |
| Large            | 8                     | 8               | 160                          | 800                           |
| XL               | 24                    | 24              | 240                          | 1,000                         |
| 2XL              | 80                    | 80              | 380                          | 1,500                         |
| 4XL              | 80                    | 80              | 480                          | 3,000                         |
| 8XL              | 80                    | 80              | 490                          | 6,000                         |
| 12XL             | 80                    | 80              | 500                          | 9,000                         |
| 16XL             | 80                    | 80              | 500                          | 12,000                        |

<Admonition type="caution">
  As mentioned in the Postgres [documentation](https://postgresqlco.nf/doc/en/param/max_replication_slots/), setting `max_replication_slots` to a lower value than the current number of replication slots will prevent the server from starting. If you are downgrading your compute instance, ensure that you are using fewer slots than the maximum number of replication slots available for the new compute instance.
</Admonition>


### Constraints

*   After **any** disk attribute change, there is a cooldown period of approximately six hours before you can make further adjustments. During this time, no changes are allowed. If you encounter throttling, you’ll need to wait until the cooldown period concludes before making additional modifications.
*   You can increase disk size but cannot decrease it.



# Control your costs




## Spend Cap

The Spend Cap determines whether your organization can exceed your subscription plan's quota for any usage item. Scenarios that could lead to high usage—and thus high costs—include system attacks or bugs in your software. The Spend Cap can protect you from these unexpected costs for certain usage items.

This feature is available only with the Pro Plan. However, you will not be charged while using the Free Plan.


### What happens when the Spend Cap is on?

After exceeding the quota for a usage item, further usage of that item is disallowed until the next billing cycle. You don't get charged for over-usage but your services will be restricted according to our [Fair Use Policy](/docs/guides/platform/billing-faq#fair-use-policy) if you consistently exceed the quota.

<Admonition type="note">
  Note that only certain usage items are covered by the Spend Cap.
</Admonition>


### What happens when the Spend Cap is off?

Your projects will continue to operate after exceeding the quota for a usage item. Any additional usage will be charged based on the item's cost per unit, as outlined on the [pricing page](/pricing).

<Admonition type="note">
  When the Spend Cap is off, we recommend monitoring your usage and costs on the [organization's usage page](/dashboard/org/_/usage).
</Admonition>


### Usage items covered by the Spend Cap

*   [Disk Size](/docs/guides/platform/manage-your-usage/disk-size)
*   [Egress](/docs/guides/platform/manage-your-usage/egress)
*   [Edge Function Invocations](/docs/guides/platform/manage-your-usage/edge-function-invocations)
*   [Monthly Active Users](/docs/guides/platform/manage-your-usage/monthly-active-users)
*   [Monthly Active SSO Users](/docs/guides/platform/manage-your-usage/monthly-active-users-sso)
*   [Monthly Active Third Party Users](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party)
*   [Realtime Messages](/docs/guides/platform/manage-your-usage/realtime-messages)
*   [Realtime Peak Connections](/docs/guides/platform/manage-your-usage/realtime-peak-connections)
*   [Storage Image Transformations](/docs/guides/platform/manage-your-usage/storage-image-transformations)
*   [Storage Size](/docs/guides/platform/manage-your-usage/storage-size)


### Usage items not covered by the Spend Cap

Usage items that are predictable and explicitly opted into by the user are excluded.

*   [Compute](/docs/guides/platform/manage-your-usage/compute)
*   [Branching Compute](/docs/guides/platform/manage-your-usage/branching)
*   [Read Replica Compute](/docs/guides/platform/manage-your-usage/read-replicas)
*   [Custom Domain](/docs/guides/platform/manage-your-usage/custom-domains)
*   Additionally provisioned [Disk IOPS](/docs/guides/platform/manage-your-usage/disk-iops)
*   Additionally provisioned [Disk Throughput](/docs/guides/platform/manage-your-usage/disk-throughput)
*   [IPv4 address](/docs/guides/platform/manage-your-usage/ipv4)
*   [Log Drain Hours](/docs/guides/platform/manage-your-usage/log-drains#log-drain-hours)
*   [Log Drain Events](/docs/guides/platform/manage-your-usage/log-drains#log-drain-events)
*   [Multi-Factor Authentication Phone](/docs/guides/platform/manage-your-usage/advanced-mfa-phone)
*   [Point-in-Time-Recovery](/docs/guides/platform/manage-your-usage/point-in-time-recovery)


### What the Spend Cap is not

The Spend Cap doesn't allow for fine-grained cost control, such as setting budgets for specific usage item or receiving notifications when certain costs are reached. We plan to make cost control more flexible in the future.


### Configure the Spend Cap

You can configure the Spend Cap when creating an organization on the Pro Plan or at any time in the Cost Control section of the [organization's billing page](/dashboard/org/_/billing).



## Keep track of your usage and costs

You can monitor your usage on the [organization's usage page](/dashboard/org/_/usage). The Upcoming Invoice section of the [organization's billing page](/dashboard/org/_/billing) shows your current spending and provides an estimate of your total costs for the billing cycle based on your usage.



# Credits




## Credit balance

Each organization has a credit balance. Credits are applied to future invoices to reduce the amount due. As long as the credit balance is greater than <Price price="0" />, credits will be used before charging your payment method on file.

<Image
  alt="Subscription upgrade modal"
  src={{
    light: '/docs/img/guides/platform/credit-balance--light.png',
    dark: '/docs/img/guides/platform/credit-balance--dark.png',
  }}
  zoomable
/>

You can find the credit balance on the [organization's billing page](/dashboard/org/_/billing).


### What causes the credit balance to change?

**Subscription plan downgrades:** Upon subscription downgrade, any prepaid subscription fee will be credited back to your organization for unused time in the billing cycle.\
As an example, if you start a Pro Plan subscription on January 1 and downgrade to the Free Plan on January 15, your organization will receive about 50% of the subscription fee as credits for the unused time between January 15 and January 31.

**Credit top-ups:** You self-served a credit top-up or have signed an upfront credits deal with our growth team.



## Credit top-ups

You can top up credits at any time, with a maximum of <Price price="2000" /> per top-up. These credits do not expire and are non-refundable.
You may want to consider this option to avoid issues with recurring payments, gain more control over how often your credit card is charged, and potentially make things easier for your accounting department.

<Admonition type="note">
  If you are interested in larger (> <Price price="2000" />) credit packages, [reach out](/dashboard/support/new?subject=I%20would%20like%20to%20inquire%20about%20larger%20credit%20packages\&category=Sales).
</Admonition>


### How to top up credits

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Credit Balance**
2.  Click **Top Up**
3.  Choose the amount
4.  Choose a payment method or add a new payment method
5.  Click **Top Up**

<Image
  alt="Subscription upgrade modal"
  src={{
    light: '/docs/img/guides/platform/credit-top-up--light.png',
    dark: '/docs/img/guides/platform/credit-top-up--dark.png',
  }}
  zoomable
  className="max-w-[500px]"
/>



## Credit FAQ

{/* supa-mdx-lint-disable Rule004ExcludeWords */}


### Will I get an invoice for the credits purchase?

Yes, once the payment is confirmed, you will get a matching invoice that can be accessed through your [organization's invoices page](/dashboard/org/_/billing#invoices).


### Can I transfer credits to another organization?

Yes, you can transfer credits to another organization. Submit a [support ticket](https://supabase.help).


### Can I get a refund of my unused credits?

No, we do not provide refunds. Please refer to our [Terms of Service](/terms#1-fees).



# Custom Domains



Custom domains allow you to present a branded experience to your users. These are available as a [paid add-on for projects on a paid plan](/dashboard/project/_/settings/addons?panel=customDomain).

There are two types of domains supported by Supabase:

1.  Custom domains, where you use a domain such as `api.example.com` instead of the project's default domain.
2.  Vanity subdomains (experimental), where you can set up a different subdomain on `supabase.co` for your project.

You can choose either a custom domain or vanity subdomain for each project.



## Custom domains

Custom domains change the way your project's URLs appear to your users. This is useful when:

*   You are using [OAuth (Social Login)](/docs/guides/auth/social-login) with Supabase Auth and the project's URL is shown on the OAuth consent screen.
*   You are creating APIs for third-party systems, for example, implementing webhooks or external API calls to your project via [Edge Functions](/docs/guides/functions).
*   You are storing URLs in a database or encoding them in QR codes.

Custom domains help you keep your APIs portable for the long term. By using a custom domain you can migrate from one Supabase project to another, or make it easier to version APIs in the future.


### Limitations

*   Custom domains are not intended to enable hosting of frontend applications through [Edge Functions](/docs/guides/functions).
*   You can only attach a single custom domain to any given Supabase project. It is not possible to break out your project's resources into multiple custom domains.
*   Custom domains can only be powered by CNAME records.


### Configure a custom domain using the Supabase dashboard

Follow the **Custom Domains** steps in the [General Settings](/dashboard/project/_/settings/general) page in the Dashboard to set up a custom domain for your project.


### Configure a custom domain using the Supabase CLI

This example assumes your Supabase project is `abcdefghijklmnopqrst` with a corresponding API URL `abcdefghijklmnopqrst.supabase.co` and configures a custom domain at `api.example.com`.

To get started:

1.  [Install](/docs/guides/resources/supabase-cli) the latest version of the Supabase CLI.
2.  [Log in](/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3.  Ensure you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project.
4.  Get a custom domain from a DNS provider. Currently, only subdomains are supported.
    *   Use `api.example.com` instead of `example.com`.


### Add a CNAME record

You need to add a CNAME record to your domain's DNS settings to ensure your custom domain points to the Supabase project.

If your project's default domain is `abcdefghijklmnopqrst.supabase.co` you should:

*   Create a CNAME record for `api.example.com` that resolves to `abcdefghijklmnopqrst.supabase.co.`.
*   Use a low TTL value to quickly propagate changes in case you make a mistake.


### Verify ownership of the domain

Register your domain with Supabase to prove that you own it. You need to download two TXT records and add them to your DNS settings.

In the CLI, run [`domains create`](/docs/reference/cli/supabase-domains-create) to register the domain and Supabase and get your verification records:

```bash
supabase domains create --project-ref abcdefghijklmnopqrst --custom-hostname api.example.com
```

A single TXT records is returned. For example:

```text
[...]
Required outstanding validation records:
        _acme-challenge.api.example.com. TXT -> ca3-F1HvR9i938OgVwpCFwi1jTsbhe1hvT0Ic3efPY3Q
```

Add the record to your domains' DNS settings. Make sure to trim surrounding whitespace. Use a low TTL value so you can quickly change the records if you make a mistake.

Some DNS registrars automatically append your domain name to the DNS entries being created. As such, creating a DNS record for `api.example.com` might instead create a record for `api.example.com.example.com`. In such cases, remove the domain name from the records you're creating; as an example, you would create a TXT record for `api`, instead of `api.example.com`.


### Verify your domain

Make sure you've configured all required DNS settings:

*   CNAME for your custom domain pointing to the Supabase project domain.
*   TXT record for `_acme-challenge.<your-custom-domain>`.

Use the [`domains reverify`](/docs/reference/cli/supabase-domains-reverify) command to begin the verification process of your domain. You may need to run this command a few times because DNS records take a while to propagate.

```bash
supabase domains reverify --project-ref abcdefghijklmnopqrst
```

In the background, Supabase will check your DNS records and use [Let's Encrypt](https://letsencrypt.org) to issue a SSL certificate for your domain. This process can take up to 30 minutes.


### Prepare to activate your domain

Before you activate your domain, prepare your applications and integrations for the domain change:

*   The project's Supabase domain remains active.
    *   You do not need to change the Supabase URL in your applications immediately.
    *   You can use it interchangeably with the custom domain.
*   Supabase Auth will use the custom domain immediately once activated.
    *   OAuth flows will advertise the custom domain as a callback URL.
    *   SAML will use the custom domain instead. This means that the `EntityID` of your project has changed, and this may cause SAML with existing identity providers to stop working.

To prevent issues for your users, follow these steps:

1.  For each of your Supabase OAuth providers:
    *   In the provider's developer console (not in the Supabase dashboard), find the OAuth application and add the custom domain Supabase Auth callback URL **in addition to the Supabase project URL.** Example:
        *   `https://abcdefghijklmnopqrst.supabase.co/auth/v1/callback` **and**
        *   `https://api.example.com/auth/v1/callback`
    *   [Sign in with Twitter](/docs/guides/auth/social-login/auth-twitter) uses cookies bound to the project's domain. Make sure your frontend code uses the custom domain instead of the default project's domain.
2.  For each of your SAML identity providers:
    *   Contact your provider and ask them to update the metadata for the SAML application. They should use `https://api.example.com/auth/v1/...` instead of `https://abcdefghijklmnopqrst.supabase.co/auth/v1/sso/saml/{metadata,acs,slo}`.
    *   Once these changes are made, SAML Single Sign-On will likely stop working until the domain is activated. Plan for this ahead of time.


### Activate your domain

Once you've done the necessary preparations to activate the new domain for your project, you can activate it using the [`domains activate`](/docs/reference/cli/supabase-domains-activate) CLI command.

```bash
supabase domains activate --project-ref abcdefghijklmnopqrst
```

When this step completes, Supabase will serve the requests from your new domain. The Supabase project domain **continues to work** and serve requests so you do not need to rush to change client code URLs.

If you wish to use the new domain in client code, change the URL used in your Supabase client libraries:

```js
import { createClient } from '@supabase/supabase-js'

// Use a custom domain as the supabase URL
const supabase = createClient('https://api.example.com', 'publishable-or-anon-key')
```

Similarly, your Edge Functions will now be available at `https://api.example.com/functions/v1/your_function_name`, and your Storage objects at `https://api.example.com/storage/v1/object/public/your_file_path.ext`.


### Remove a custom domain

Removing a custom domain may cause some issues when using Supabase Auth with OAuth or SAML. You may have to reverse the changes made in the *[Prepare to activate your domain](#prepare-to-activate-your-domain)* step above.

To remove an activated custom domain you can use the [`domains delete`](/docs/reference/cli/supabase-domains-delete) CLI command.

```bash
supabase domains delete --project-ref abcdefghijklmnopqrst
```



## Vanity subdomains

Vanity subdomains allow you to present a basic branded experience, compared to custom domains. They allow you to host your services at a custom subdomain on Supabase (e.g., `my-example-brand.supabase.co`) instead of the default, randomly assigned `abcdefghijklmnopqrst.supabase.co`.

To get started:

1.  [Install](/docs/guides/resources/supabase-cli) the latest version of the Supabase CLI.
2.  [Log in](/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.
3.  Ensure that you have [Owner or Admin permissions](/docs/guides/platform/access-control#manage-team-members) for the project you'd like to set up a vanity subdomain for.
4.  Ensure that your organization is on a paid plan (Pro/Team/Enterprise Plan) in the [Billing page of the Dashboard](/dashboard/org/_/billing).


### Configure a vanity subdomain

You can configure vanity subdomains via the CLI only.

Let's assume your Supabase project's domain is `abcdefghijklmnopqrst.supabase.co` and you wish to configure a vanity subdomain at `my-example-brand.supabase.co`.


### Check subdomain availability

Use the [`vanity-subdomains check-availability`](/docs/reference/cli/supabase-vanity-subdomains-check-availability) command of the CLI to check if your desired subdomain is available for use:

```bash
supabase vanity-subdomains --project-ref abcdefghijklmnopqrst check-availability --desired-subdomain my-example-brand --experimental
```


### Prepare to activate the subdomain

Before you activate your vanity subdomain, prepare your applications and integrations for the subdomain change:

*   The project's Supabase domain remains active and will not go away.
    *   You do not need to change the Supabase URL in your applications immediately or at once.
    *   You can use it interchangeably with the custom domain.
*   Supabase Auth will use the subdomain immediately once activated.
    *   OAuth flows will advertise the subdomain as a callback URL.
    *   SAML will use the subdomain instead. This means that the `EntityID` of your project has changed, and this may cause SAML with existing identity providers to stop working.

To prevent issues for your users, make sure you have gone through these steps:

1.  Go through all of your Supabase OAuth providers:
    *   In the provider's developer console (not in the Supabase dashboard!), find the OAuth application and add the subdomain Supabase Auth callback URL **in addition to the Supabase project URL.** Example:
        *   `https://abcdefghijklmnopqrst.supabase.co/auth/v1/callback` **and**
        *   `https://my-example-brand.supabase.co/auth/v1/callback`
    *   [Sign in with Twitter](/docs/guides/auth/social-login/auth-twitter) uses cookies bound to the project's domain. In this case make sure your frontend code uses the subdomain instead of the default project's domain.
2.  Go through all of your SAML identity providers:
    *   You will need to reach out via email to all of your existing identity providers and ask them to update the metadata for the SAML application (your project). Use `https://example-brand.supabase.co/auth/v1/...` instead of `https://abcdefghijklmnopqrst.supabase.co/auth/v1/sso/saml/{metadata,acs,slo}`.
    *   Once these changes are made, SAML Single Sign-On will likely stop working until the domain is activated. Plan for this ahead of time.


### Activate a subdomain

Once you've chosen an available subdomain and have done all the necessary preparations for it, you can reconfigure your Supabase project to start using it.

Use the [`vanity-subdomains activate`](/docs/reference/cli/supabase-vanity-subdomains-activate) command to activate and claim your subdomain:

```bash
supabase vanity-subdomains --project-ref abcdefghijklmnopqrst activate --desired-subdomain my-example-brand --experimental
```

If you wish to use the new domain in client code, you can set it up like so:

```js
import { createClient } from '@supabase/supabase-js'

// Use a custom domain as the supabase URL
const supabase = createClient('https://my-example-brand.supabase.co', 'publishable-or-anon-key')
```

When using [Sign in with Twitter](/docs/guides/auth/social-login/auth-twitter) make sure your frontend code is using the subdomain only.


### Remove a vanity subdomain

Removing a subdomain may cause some issues when using Supabase Auth with OAuth or SAML. You may have to reverse the changes made in the *[Prepare to activate the subdomain](#prepare-to-activate-the-subdomain)* step above.

Use the [`vanity-subdomains delete`](/docs/reference/cli/supabase-vanity-subdomains-delete) command of the CLI to remove the subdomain `my-example-brand.supabase.co` from your project.

```bash
supabase vanity-subdomains delete --project-ref abcdefghijklmnopqrst --experimental
```



## Pricing

For a detailed breakdown of how charges are calculated, refer to [Manage Custom Domain usage](/docs/guides/platform/manage-your-usage/custom-domains).



# Understanding Database and Disk Size



Disk metrics refer to the storage usage reported by Postgres. These metrics are updated daily. As you read through this document, we will refer to "database size" and "disk size":

*   *Database size*: Displays the actual size of the data within your Postgres database. This can be found on the [Database Reports page](/dashboard/project/_/reports/database).

*   *Disk size*: Shows the overall disk space usage, which includes both the database size and additional files required for Postgres to function like the Write Ahead Log (WAL) and other system log files. You can view this on the [Database Settings page](/dashboard/project/_/database/settings).



## Database size

This SQL query will show the size of all databases in your Postgres cluster:

```sql
select
  pg_size_pretty(sum(pg_database_size(pg_database.datname)))
from pg_database;
```

This value is reported in the [database report page](/dashboard/project/_/reports/database).

Database size is consumed primarily by your data, indexes, and materialized views. You can reduce your database size by removing any of these and running a Vacuum operation.

<Admonition type="note">
  Depending on your billing plan, your database can go into read-only mode which can prevent you inserting and deleting data. There are instructions for managing read-only mode in the [Disk Management](#disk-management) section.
</Admonition>


### Disk space usage

Your database size is part of the disk usage for your Supabase project, there are many components to Postgres that consume additional disk space. One of the primary components, is the [Write Ahead Log (WAL)](https://www.postgresql.org/docs/current/wal-intro.html). Postgres will store database changes in log files that are cleared away after they are applied to the database. These same files are also used by [Read Replicas](/docs/guides/platform/read-replicas) or other replication methods.

If you would like to determine the size of the WAL files stored on disk, Postgres provides `pg_ls_waldir` as a helper function; the following query can be run:

```sql
select pg_size_pretty(sum(size)) as wal_size from pg_ls_waldir();
```


### Vacuum operations

Postgres does not immediately reclaim the physical space used by dead tuples (i.e., deleted rows) in the DB. They are marked as "removed" until a [vacuum operation](https://www.postgresql.org/docs/current/routine-vacuuming.html) is executed. As a result, deleting data from your database may not immediately reduce the reported disk usage. You can use the [Supabase CLI](/docs/guides/cli/getting-started) `inspect db bloat` command to view all dead tuples in your database. Alternatively, you can run the [query](https://github.com/supabase/cli/blob/c9cce58025fded16b4c332747f819a44f45c3b83/internal/inspect/bloat/bloat.go#L17) found in the CLI's GitHub repo in the [SQL Editor](/dashboard/project/_/sql/)

```bash

# Login to the CLI
npx supabase login


# Initialize a local supabase directory
npx supabase init


# Link a project
npx supabase link


# Detect bloat
npx supabase inspect db bloat --linked
```

If you find a table you would like to immediately clean, you can run the following in the [SQL Editor](/dashboard/project/_/sql/new):

```sql
vacuum full <table name>;
```

<Admonition type="note">
  Vacuum operations can temporarily increase resource utilization, which may adversely impact the observed performance of your project until the maintenance is completed. The [vacuum full](https://www.postgresql.org/docs/current/sql-vacuum.html) command will lock the table until the operation concludes.
</Admonition>

Supabase projects have automatic vacuuming enabled, which ensures that these operations are performed regularly to keep the database healthy and performant.
It is possible to [fine-tune](https://www.percona.com/blog/2018/08/10/tuning-autovacuum-in-postgresql-and-autovacuum-internals/) the [autovacuum parameters](https://www.enterprisedb.com/blog/postgresql-vacuum-and-analyze-best-practice-tips), or [manually initiate](https://www.postgresql.org/docs/current/sql-vacuum.html) vacuum operations.
Running a manual vacuum after deleting large amounts of data from your DB could help reduce the database size reported by Postgres.


### Preoccupied space

New Supabase projects have a database size of ~40-60mb. This space includes pre-installed extensions, schemas, and default Postgres data. Additional database size is used when installing extensions, even if those extensions are inactive.



## Disk size

Supabase uses network-attached storage to balance performance with scalability. The disk scaling behavior depends on your billing plan.


### Paid plan behavior

Projects on the Pro Plan and higher have auto-scaling disks.

Disk size expands automatically when the database reaches 90% of the allocated disk size. The disk is expanded to be 50% larger (for example, 8 GB -> 12 GB). Auto-scaling can only take place once every 6 hours. If within those 6 hours you reach 95% of the disk space, your project will enter read-only mode.

<Admonition type="note">
  The automatic resize operation will add an additional 50% capped to a maximum of 200 GB. If 50% of your current usage is more than 200 GB then only 200 GB will be added to your disk (for example a size of 1500 GB will resize to 1700 GB).
</Admonition>

Disk size can also be manually expanded on the [Database Settings page](/dashboard/project/_/database/settings). The maximum disk size for the Pro/Team Plan is 60 TB. If you need more than this, [contact us](https://forms.supabase.com/enterprise) to learn more about the Enterprise Plan.

<Admonition type="note">
  You may want to import a lot of data into your database which requires multiple disk expansions. for example, uploading more than 1.5x the current size of your database storage will put your database into [read-only mode](#read-only-mode). If so, it is highly recommended you increase the disk size manually on the [Database Settings page](/dashboard/project/_/database/settings).

  Due to restrictions on the underlying cloud provider, disk expansions can occur only once every six hours. During the six hour cool down window, the disk cannot be resized again.
</Admonition>


### Free Plan behavior

Free Plan projects enter [read-only](#read-only-mode) mode when you exceed the 500 MB limit. Once in read-only mode, you have these options:

*   [Upgrade to the Pro Plan](/dashboard/org/_/billing) to increase the limit to 8 GB. [Disable the Spend Cap](https://app.supabase.com/org/_/billing?panel=costControl) if you want your Pro instance to auto-scale beyond the 8 GB disk size limit.
*   [Disable read-only mode](#disabling-read-only-mode) and reduce your database size.


### Read-only mode

In some cases Supabase may put your database into read-only mode to prevent your database from exceeding the billing or disk limitations.

In read-only mode, clients will encounter errors such as `cannot execute INSERT in a read-only transaction`. Regular operation (read-write mode) is automatically re-enabled once usage is below 95% of the disk size,


### Disabling read-only mode

You manually override read-only mode to reduce disk size. To do this, run the following in the [SQL Editor](/dashboard/project/_/sql):

First, change the [transaction access mode](https://www.postgresql.org/docs/current/sql-set-transaction.html):

```sql
set session characteristics as transaction read write;
```

This allows you to delete data from within the session. After deleting data, consider running a vacuum to reclaim as much space as possible:

```sql
vacuum;
```

Once you have reclaimed space, you can run the following to disable [read-only](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-DEFAULT-TRANSACTION-READ-ONLY) mode:

```sql
set default_transaction_read_only = 'off';
```


### Disk size distribution

You can check the distribution of your disk size on your [project's compute and disk page](/dashboard/_/settings/compute-and-disk).

![Disk Size Distribution](/docs/img/guides/platform/database-size/disk-size-distribution.png)

Your disk size usage falls in three categories:

*   **Database** - Disk usage by the database. This includes the actual data, indexes, materialized views, ...
*   **WAL** - Disk usage by the write-ahead log. The usage depends on your WAL settings and the amount of data being written to the database.
*   **System** - Disk usage reserved by the system to ensure the database can operate smoothly. Users cannot modify this and it should only take very little space.


### Reducing disk size

Disks don't automatically downsize during normal operation. Once you have [reduced your database size](/docs/guides/platform/database-size#database-size), they *will* automatically "right-size" during a [project upgrade](/docs/guides/platform/upgrading). The final disk size after the upgrade is 1.2x the size of the database with a minimum of 8 GB. For example, if your database size is 100GB, and you have a 200GB disk, the size after a project upgrade will be 120 GB.

In case you have a large WAL directory, you may [modify WAL settings](/docs/guides/database/custom-postgres-config) such as `max_wal_size`. Use at your own risk as changing these settings can have side effects. To query your current WAL size, use `SELECT SUM(size) FROM pg_ls_waldir()`.

In the event that your project is already on the latest version of Postgres and cannot be upgraded, a new version of Postgres will be released approximately every week which you can then upgrade to once it becomes available.



# Get set up for billing



Correct billing settings are essential for ensuring successful payment processing and uninterrupted services. Additionally, it's important to configure all invoicing-related data early, as this information cannot be changed once an invoice is issued. Review these key points to ensure everything is set up correctly from the start.



## Payments


### Ensuring valid credit card details

Paid plans require a credit card to be on file. Ensure the correct credit card is set as active and

*   has not expired
*   has sufficient funds
*   has a sufficient transaction limit

For more information on managing payment methods, see [Manage your payment methods](/docs/guides/platform/manage-your-subscription#manage-your-payment-methods).


### Alternatives to monthly charges

Instead of having your credit card charged every month, you can make an upfront payment by topping up your credit balance.

You may want to consider this option to avoid issues with recurring payments, gain more control over how often your credit card is charged, and potentially make things easier for your accounting department.

For more information on credits and credit top-ups, see the [Credits page](/docs/guides/platform/credits).



## Billing details

Billing details cannot be changed once an invoice is issued, so it's crucial to configure them correctly from the start.

You can update your billing email address, billing address and tax ID on the [organization's billing page](/dashboard/org/_/billing).



---
**Navigation:** [← Previous](./06-realtime-quotas.md) | [Index](./index.md) | [Next →](./08-hipaa-projects.md)
