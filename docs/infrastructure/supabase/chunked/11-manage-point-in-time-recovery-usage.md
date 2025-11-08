**Navigation:** [← Previous](./10-set-supabase-connection-session-pooler-on-port-543.md) | [Index](./index.md) | [Next →](./12-advanced-pgtap-testing.md)

# Manage Point-in-Time Recovery usage




## What you are charged for

You can configure [Point-in-Time Recovery (PITR)](/docs/guides/platform/backups#point-in-time-recovery) for a project by enabling the [PITR add-on](/dashboard/project/_/settings/addons?panel=pitr). You are charged for every enabled PITR add-on across your projects.



## How charges are calculated

PITR is charged by the hour, meaning you are charged for the exact number of hours that PITR is active for a project. If PITR is active for part of an hour, you are still charged for the full hour.


### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you activate PITR for your project. At the end of the billing cycle you are billed for 512 hours.

| Time Window                                 | PITR Activated | Hours Billed | Description         |
| ------------------------------------------- | -------------- | ------------ | ------------------- |
| January 1, 00:00 AM - January 10, 4:00 PM   | No             | 0            |                     |
| January 10, 04:00 PM - January 10, 4:30 PM  | No             | 0            |                     |
| January 10, 04:30 PM - January 10, 5:00 PM  | Yes            | 1            | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Yes            | 511          |                     |


### Usage on your invoice

Usage is shown as "Point-in-time recovery Hours" on your invoice.



## Pricing


### Pricing

Pricing depends on the recovery retention period, which determines how many days back you can restore data to any chosen point of up to seconds in granularity.

| Recovery Retention Period in Days | Hourly Price USD        | Monthly Price USD     |
| --------------------------------- | ----------------------- | --------------------- |
| 7                                 | <Price price="0.137" /> | <Price price="100" /> |
| 14                                | <Price price="0.274" /> | <Price price="200" /> |
| 28                                | <Price price="0.55" />  | <Price price="400" /> |

For a detailed breakdown of how charges are calculated, refer to [Manage Point-in-Time Recovery usage](/docs/guides/platform/manage-your-usage/point-in-time-recovery).



## Billing examples


### One project

The project has PITR with a recovery retention period of 7 days activated throughout the entire billing cycle.

| Line Item                     | Hours | Costs                     |
| ----------------------------- | ----- | ------------------------- |
| Pro Plan                      | -     | <Price price="25" />      |
| Compute Hours Small Project 1 | 744   | <Price price="15" />      |
| PITR Hours                    | 744   | <Price price="100" />     |
| **Subtotal**                  |       | **<Price price="140" />** |
| Compute Credits               |       | -<Price price="10" />     |
| **Total**                     |       | **<Price price="130" />** |


### Multiple projects

All projects have PITR with a recovery retention period of 14 days activated throughout the entire billing cycle.

| Line Item                     | Hours | Costs                     |
| ----------------------------- | ----- | ------------------------- |
| Pro Plan                      | -     | <Price price="25" />      |
|                               |       |                           |
| Compute Hours Small Project 1 | 744   | <Price price="15" />      |
| PITR Hours Project 1          | 744   | <Price price="200" />     |
|                               |       |                           |
| Compute Hours Small Project 2 | 744   | <Price price="15" />      |
| PITR Hours Project 2          | 744   | <Price price="200" />     |
|                               |       |                           |
| **Subtotal**                  |       | **<Price price="455" />** |
| Compute Credits               |       | -<Price price="10" />     |
| **Total**                     |       | **<Price price="445" />** |



## Optimize usage

*   Review your [backup frequency](/docs/guides/platform/backups#frequency-of-backups) needs to determine whether you require PITR or free Daily Backups are sufficient
*   Regularly check your projects and disable PITR where no longer needed
*   Consider disabling PITR for non-production databases



# Manage Read Replica usage




## What you are charged for

Each [Read Replica](/docs/guides/platform/read-replicas) is a dedicated database. You are charged for its resources: [Compute](/docs/guides/platform/compute-and-disk#compute), [Disk Size](/docs/guides/platform/database-size#disk-size), provisioned [Disk IOPS](/docs/guides/platform/compute-and-disk#provisioned-disk-throughput-and-iops), provisioned [Disk Throughput](/docs/guides/platform/compute-and-disk#provisioned-disk-throughput-and-iops), and [IPv4](/docs/guides/platform/ipv4-address).



## How charges are calculated

Read Replica charges are the total of the charges listed below.

**Compute**
Compute is charged by the hour, meaning you are charged for the exact number of hours that a Read Replica is running and, therefore, incurring Compute usage. If a Read Replica runs for part of an hour, you are still charged for the full hour.

Read Replicas run on the same Compute size as the primary database.

**Disk Size**
Refer to [Manage Disk Size usage](/docs/guides/platform/manage-your-usage/disk-size) for details on how charges are calculated. The disk size of a Read Replica is 1.25x the size of the primary disk to account for WAL archives. With a Read Replica you go beyond your subscription plan's quota for Disk Size.

**Provisioned Disk IOPS (optional)**
Read Replicas inherit any additional provisioned Disk IOPS from the primary database. Refer to [Manage Disk IOPS usage](/docs/guides/platform/manage-your-usage/disk-iops) for details on how charges are calculated.

**Provisioned Disk Throughput (optional)**
Read Replicas inherit any additional provisioned Disk Throughput from the primary database. Refer to [Manage Disk Throughput usage](/docs/guides/platform/manage-your-usage/disk-throughput) for details on how charges are calculated.

**IPv4 (optional)**
If the primary database has a configured IPv4 address, its Read Replicas are also assigned one, with charges for each. Refer to [Manage IPv4 usage](/docs/guides/platform/manage-your-usage/ipv4) for details on how charges are calculated.


### Usage on your invoice

Compute incurred by Read Replicas is shown as "Replica Compute Hours" on your invoice. Disk Size, Disk IOPS, Disk Throughput and IPv4 are not shown separately for Read Replicas and are rolled up into the project.



## Billing examples


### No additional resources configured

The project has one Read Replica and no IPv4 and no additional Disk IOPS and Disk Throughput configured.

| Line Item                     | Units     | Costs                       |
| ----------------------------- | --------- | --------------------------- |
| Pro Plan                      | 1         | <Price price="25" />        |
|                               |           |                             |
| Compute Hours Small Project 1 | 744 hours | <Price price="15" />        |
| Disk Size Project 1           | 8 GB      | <Price price="0" />         |
|                               |           |                             |
| Compute Hours Small Replica   | 744 hours | <Price price="15" />        |
| Disk Size Replica             | 10 GB     | <Price price="1.25" />      |
|                               |           |                             |
| **Subtotal**                  |           | **<Price price="56.25" />** |
| Compute Credits               |           | -<Price price="10" />       |
| **Total**                     |           | **<Price price="46.25" />** |


### Additional resources configured

The project has two Read Replicas and IPv4 and additional Disk IOPS and Disk Throughput configured.

| Line Item                     | Units     | Costs                        |
| ----------------------------- | --------- | ---------------------------- |
| Pro Plan                      | 1         | <Price price="25" />         |
|                               |           |                              |
| Compute Hours Large Project 1 | 744 hours | <Price price="110" />        |
| Disk Size Project 1           | 8 GB      | <Price price="0" />          |
| Disk IOPS Project 1           | 3600      | <Price price="14.40" />      |
| Disk Throughput Project 1     | 200 MB/s  | <Price price="7.13" />       |
| IPv4 Hours Project 1          | 744 hours | <Price price="4" />          |
|                               |           |                              |
| Compute Hours Large Replica 1 | 744 hours | <Price price="110" />        |
| Disk Size Replica 1           | 10 GB     | <Price price="1.25" />       |
| Disk IOPS Replica 1           | 3600      | <Price price="14.40" />      |
| Disk Throughput Replica 1     | 200 MB/s  | <Price price="7.13" />       |
| IPv4 Hours Replica 1          | 744 hours | <Price price="4" />          |
|                               |           |                              |
| Compute Hours Large Replica 2 | 744 hours | <Price price="110" />        |
| Disk Size Replica 2           | 10 GB     | <Price price="1.25" />       |
| Disk IOPS Replica 2           | 3600      | <Price price="14.40" />      |
| Disk Throughput Replica 2     | 200 MB/s  | <Price price="7.13" />       |
| IPv4 Hours Replica 2          | 744 hours | <Price price="4" />          |
|                               |           |                              |
| **Subtotal**                  |           | **<Price price="434.09" />** |
| Compute Credits               |           | -<Price price="10" />        |
| **Total**                     |           | **<Price price="424.09" />** |



## FAQ


### Do Compute Credits apply to Read Replica Compute?

No, Compute Credits do not apply to Read Replica Compute.



# Manage Realtime Messages usage




## What you are charged for

You are charged for the number of messages going through Supabase Realtime throughout the billing cycle. Includes database changes, Broadcast and Presence.

**Database changes**
Each database change counts as one message per client that listens to the event. For example, if a database change occurs and 5 clients listen to that database event, it counts as 5 messages.

**Broadcast**
Each broadcast message counts as one message sent plus one message per subscribed client that receives it. For example, if you broadcast a message and 4 clients listen to it, it counts as 5 messages—1 sent and 4 received.



## How charges are calculated

Realtime Messages are billed using Package pricing, with each package representing 1 million messages. If your usage falls between two packages, you are billed for the next whole package.


### Example

For simplicity, let's assume a package size of 1,000,000 and a charge of <Price price="2.50" /> per package without quota.

| Messages  | Packages Billed | Costs                  |
| --------- | --------------- | ---------------------- |
| 999,999   | 1               | <Price price="2.50" /> |
| 1,000,000 | 1               | <Price price="2.50" /> |
| 1,000,001 | 2               | <Price price="5.00" /> |
| 1,500,000 | 2               | <Price price="5.00" /> |


### Usage on your invoice

Usage is shown as "Realtime Messages" on your invoice.



## Pricing

<Price price="2.50" /> per 1 million messages. You are only charged for usage exceeding your subscription
plan's quota.

| Plan       | Quota     | Over-Usage                                    |
| ---------- | --------- | --------------------------------------------- |
| Free       | 2 million | -                                             |
| Pro        | 5 million | <Price price="2.50" /> per 1 million messages |
| Team       | 5 million | <Price price="2.50" /> per 1 million messages |
| Enterprise | Custom    | Custom                                        |



## Billing examples


### Within quota

The organization's Realtime messages are within the quota, so no charges apply.

| Line Item           | Units                | Costs                    |
| ------------------- | -------------------- | ------------------------ |
| Pro Plan            | 1                    | <Price price="25" />     |
| Compute Hours Micro | 744 hours            | <Price price="10" />     |
| Realtime Messages   | 1.8 million messages | <Price price="0" />      |
| **Subtotal**        |                      | **<Price price="35" />** |
| Compute Credits     |                      | -<Price price="10" />    |
| **Total**           |                      | **<Price price="25" />** |


### Exceeding quota

The organization's Realtime messages exceed the quota by 3.5 million, incurring charges for this additional usage.

| Line Item           | Units                | Costs                    |
| ------------------- | -------------------- | ------------------------ |
| Pro Plan            | 1                    | <Price price="25" />     |
| Compute Hours Micro | 744 hours            | <Price price="10" />     |
| Realtime Messages   | 8.5 million messages | <Price price="10" />     |
| **Subtotal**        |                      | **<Price price="45" />** |
| Compute Credits     |                      | -<Price price="10" />    |
| **Total**           |                      | **<Price price="35" />** |



## View usage

You can view Realtime Messages usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Realtime Messages section, you can see the usage for the selected time period.

<Image
  alt="Usage page Realtime Messages section"
  src={{
    light: '/docs/img/guides/platform/usage-realtime-messages--light.png',
    dark: '/docs/img/guides/platform/usage-realtime-messages--dark.png',
  }}
  zoomable
/>



# Manage Realtime Peak Connections usage




## What you are charged for

Realtime Peak Connections are measured by tracking the highest number of concurrent connections for each project during the billing cycle. Regardless of fluctuations, only the peak count per project is used for billing, and the totals from all projects are summed. Only successful connections are counted, connection attempts are not included.


### Example

For simplicity, this example assumes a billing cycle of only three days.

| Project   | Peak Connections Day 1 | Peak Connections Day 2 | Peak Connections Day 3 |
| --------- | ---------------------- | ---------------------- | ---------------------- |
| Project A | 80                     | 100                    | 90                     |
| Project B | 120                    | 110                    | 150                    |

**Total billed connections:** 100 (Project A) + 150 (Project B) = **250 connections**



## How charges are calculated

Realtime Peak Connections are billed using Package pricing, with each package representing 1,000 peak connections. If your usage falls between two packages, you are billed for the next whole package.


### Example

For simplicity, let's assume a package size of 1,000 and a charge of <Price price="10" /> per package with no quota.

| Peak Connections | Packages Billed | Costs                |
| ---------------- | --------------- | -------------------- |
| 999              | 1               | <Price price="10" /> |
| 1,000            | 1               | <Price price="10" /> |
| 1,001            | 2               | <Price price="20" /> |
| 1,500            | 2               | <Price price="20" /> |


### Usage on your invoice

Usage is shown as "Realtime Peak Connections" on your invoice.



## Pricing

<Price price="10" /> per 1,000 peak connections. You are only charged for usage exceeding your subscription
plan's quota.

| Plan       | Quota  | Over-Usage                                      |
| ---------- | ------ | ----------------------------------------------- |
| Free       | 200    | -                                               |
| Pro        | 500    | <Price price="10" /> per 1,000 peak connections |
| Team       | 500    | <Price price="10" /> per 1,000 peak connections |
| Enterprise | Custom | Custom                                          |



## Billing examples


### Within quota

The organization's connections are within the quota, so no charges apply.

| Line Item                 | Units           | Costs                    |
| ------------------------- | --------------- | ------------------------ |
| Pro Plan                  | 1               | <Price price="25" />     |
| Compute Hours Micro       | 744 hours       | <Price price="10" />     |
| Realtime Peak Connections | 350 connections | <Price price="0" />      |
| **Subtotal**              |                 | **<Price price="35" />** |
| Compute Credits           |                 | -<Price price="10" />    |
| **Total**                 |                 | **<Price price="25" />** |


### Exceeding quota

The organization's connections exceed the quota by 1,200, incurring charges for this additional usage.

| Line Item                 | Units             | Costs                    |
| ------------------------- | ----------------- | ------------------------ |
| Pro Plan                  | 1                 | <Price price="25" />     |
| Compute Hours Micro       | 744 hours         | <Price price="10" />     |
| Realtime Peak Connections | 1,700 connections | <Price price="20" />     |
| **Subtotal**              |                   | **<Price price="45" />** |
| Compute Credits           |                   | -<Price price="10" />    |
| **Total**                 |                   | **<Price price="35" />** |



## View usage

You can view Realtime Peak Connections usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Realtime Peak Connections section, you can see the usage for the selected time period.

<Image
  alt="Usage page Realtime Peak Connections section"
  src={{
    light: '/docs/img/guides/platform/usage-realtime-peak-connections--light.png',
    dark: '/docs/img/guides/platform/usage-realtime-peak-connections--dark.png',
  }}
  zoomable
/>



# Manage Storage Image Transformations usage




## What you are charged for

You are charged for the number of distinct images transformed during the billing period, regardless of how many transformations each image undergoes. We refer to these images as "origin" images.


### Example

With these four transformations applied to `image-1.jpg` and `image-2.jpg`, the origin images count is 2.

```javascript
supabase.storage.from('bucket').createSignedUrl('image-1.jpg', 60000, {
  transform: {
    width: 200,
    height: 200,
  },
})
```

```javascript
supabase.storage.from('bucket').createSignedUrl('image-2.jpg', 60000, {
  transform: {
    width: 400,
    height: 300,
  },
})
```

```javascript
supabase.storage.from('bucket').createSignedUrl('image-2.jpg', 60000, {
  transform: {
    width: 600,
    height: 250,
  },
})
```

```javascript
supabase.storage.from('bucket').download('image-2.jpg', {
  transform: {
    width: 800,
    height: 300,
  },
})
```



## How charges are calculated

Storage Image Transformations are billed using Package pricing, with each package representing 1000 origin images. If your usage falls between two packages, you are billed for the next whole package.


### Example

For simplicity, let's assume a package size of 1,000 and a charge of <Price price="5" /> per package with no quota.

| Origin Images | Packages Billed | Costs                |
| ------------- | --------------- | -------------------- |
| 999           | 1               | <Price price="5" />  |
| 1,000         | 1               | <Price price="5" />  |
| 1,001         | 2               | <Price price="10" /> |
| 1,500         | 2               | <Price price="10" /> |


### Usage on your invoice

Usage is shown as "Storage Image Transformations" on your invoice.



## Pricing



## Pricing

<Price price="5" /> per 1,000 origin images. You are only charged for usage exceeding your subscription
plan's quota.

<Admonition type="note">
  The count resets at the start of each billing cycle.
</Admonition>

| Plan       | Quota  | Over-Usage                                  |
| ---------- | ------ | ------------------------------------------- |
| Pro        | 100    | <Price price="5" /> per 1,000 origin images |
| Team       | 100    | <Price price="5" /> per 1,000 origin images |
| Enterprise | Custom | Custom                                      |

For a detailed breakdown of how charges are calculated, refer to [Manage Storage Image Transformations usage](/docs/guides/platform/manage-your-usage/storage-image-transformations).



## Billing examples


### Within quota

The organization's number of origin images for the billing cycle is within the quota, so no charges apply.

| Line Item             | Units            | Costs                    |
| --------------------- | ---------------- | ------------------------ |
| Pro Plan              | 1                | <Price price="25" />     |
| Compute Hours Micro   | 744 hours        | <Price price="10" />     |
| Image Transformations | 74 origin images | <Price price="0" />      |
| **Subtotal**          |                  | **<Price price="35" />** |
| Compute Credits       |                  | -<Price price="10" />    |
| **Total**             |                  | **<Price price="25" />** |


### Exceeding quota

The organization's number of origin images for the billing cycle exceeds the quota by 750, incurring charges for this additional usage.

| Line Item             | Units             | Costs                    |
| --------------------- | ----------------- | ------------------------ |
| Pro Plan              | 1                 | <Price price="25" />     |
| Compute Hours Micro   | 744 hours         | <Price price="10" />     |
| Image Transformations | 850 origin images | <Price price="5" />      |
| **Subtotal**          |                   | **<Price price="40" />** |
| Compute Credits       |                   | -<Price price="10" />    |
| **Total**             |                   | **<Price price="30" />** |



## View usage

You can view Storage Image Transformations usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Storage Image Transformations section, you can see how many origin images were transformed during the selected time period.

<Image
  alt="Usage page Storage Image Transformations section"
  src={{
    light: '/docs/img/guides/platform/usage-image-transformations--light.png',
    dark: '/docs/img/guides/platform/usage-image-transformations--dark.png',
  }}
  zoomable
/>



## Optimize usage

*   Pre-generate common variants – instead of transforming images on the fly, generate and store commonly used sizes in advance
*   Optimize original image sizes – upload images in an optimized format and resolution to reduce the need for excessive transformations
*   Leverage [Smart CDN](/docs/guides/storage/cdn/smart-cdn) caching or any other caching solution to serve transformed images efficiently and avoid unnecessary repeated transformations
*   Control how long assets are stored in the browser using the `Cache-Control` header



# Manage Storage size usage




## What you are charged for

You are charged for the total size of all assets in your buckets.



## How charges are calculated

Storage size is charged by Gigabyte-Hours (GB-Hrs). 1 GB-Hr represents the use of 1 GB of storage for 1 hour.
For example, storing 10 GB of data for 5 hours results in 50 GB-Hrs (10 GB × 5 hours).


### Usage on your invoice

Usage is shown as "Storage Size GB-Hrs" on your invoice.



## Pricing

<Price price="0.00002919" /> per GB-Hr (<Price price="0.021" /> per GB per month). You are only
charged for usage exceeding your subscription plan's quota.

| Plan       | Quota in GB | Over-Usage per GB       | Quota in GB-Hrs | Over-Usage per GB-Hr         |
| ---------- | ----------- | ----------------------- | --------------- | ---------------------------- |
| Free       | 1           | -                       | 744             | -                            |
| Pro        | 100         | <Price price="0.021" /> | 74,400          | <Price price="0.00002919" /> |
| Team       | 100         | <Price price="0.021" /> | 74,400          | <Price price="0.00002919" /> |
| Enterprise | Custom      | Custom                  | Custom          | Custom                       |



## Billing examples


### Within quota

The organization's Storage size usage is within the quota, so no charges for Storage size apply.

| Line Item           | Units     | Costs                    |
| ------------------- | --------- | ------------------------ |
| Pro Plan            | 1         | <Price price="25" />     |
| Compute Hours Micro | 744 hours | <Price price="10" />     |
| Storage Size        | 85 GB     | <Price price="0" />      |
| **Subtotal**        |           | **<Price price="35" />** |
| Compute Credits     |           | -<Price price="10" />    |
| **Total**           |           | **<Price price="25" />** |


### Exceeding quota

The organization's Storage size usage exceeds the quota by 257 GB, incurring charges for this additional usage.

| Line Item           | Units     | Costs                      |
| ------------------- | --------- | -------------------------- |
| Pro Plan            | 1         | <Price price="25" />       |
| Compute Hours Micro | 744 hours | <Price price="10" />       |
| Storage Size        | 357 GB    | <Price price="5.4" />      |
| **Subtotal**        |           | **<Price price="40.4" />** |
| Compute Credits     |           | -<Price price="10" />      |
| **Total**           |           | **<Price price="30.4" />** |



## View usage


### Usage page

You can view Storage size usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Storage size section, you can see how much storage your projects have used during the selected time period.

<Image
  alt="Usage page Storage Size section"
  src={{
    light: '/docs/img/guides/platform/usage-storage-size--light.png',
    dark: '/docs/img/guides/platform/usage-storage-size--dark.png',
  }}
  zoomable
/>


### SQL Editor

Since we designed Storage to work as an integrated part of your Postgres database on Supabase, you can query information about your Storage objects in the `storage` schema.

List files larger than 5 MB:

```sql
select
    name,
    bucket_id as bucket,
    case
        when (metadata->>'size')::int >= 1073741824 then
            ((metadata->>'size')::int / 1073741824.0)::numeric(10, 2) || ' GB'
        when (metadata->>'size')::int >= 1048576 then
            ((metadata->>'size')::int / 1048576.0)::numeric(10, 2) || ' MB'
        when (metadata->>'size')::int >= 1024 then
            ((metadata->>'size')::int / 1024.0)::numeric(10, 2) || ' KB'
        else
            (metadata->>'size')::int || ' bytes'
        end as size
from
    storage.objects
where
    (metadata->>'size')::int > 1048576 * 5
order by (metadata->>'size')::int desc
```

List buckets with their total size:

```sql
select
    bucket_id,
    (sum((metadata->>'size')::int) / 1048576.0)::numeric(10, 2) as total_size_megabyte
from
    storage.objects
group by
    bucket_id
order by
    total_size_megabyte desc;
```



## Optimize usage

*   [Limit the upload size](/docs/guides/storage/production/scaling#limit-the-upload-size) for your buckets
*   [Delete assets](/docs/guides/storage/management/delete-objects) that are no longer in use



# Account Setup



After purchasing a Supabase subscription on the AWS Marketplace, the next and final step is to link the newly purchased subscription to a Supabase organization. This can either be an existing organization or a newly created one.

An AWS Marketplace subscription is linked to exactly one Supabase organization. If you want to manage multiple organizations through the AWS Marketplace, you must purchase a separate marketplace subscription for each organization.

<Image
  alt="Supabase product subscribe"
  src={{
    dark: '/docs/img/guides/platform/aws-marketplace-onboarding-page-extended--dark.png',
    light: '/docs/img/guides/platform/aws-marketplace-onboarding-page-extended--light.png',
  }}
  zoomable
/>



## Implications of linking a Supabase organization to a marketplace subscription

*   The billing details from your AWS account, such as the billing address and tax ID, are used. These details are managed through the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing).
*   The subscription plan is managed through the AWS Marketplace. You can read more about this in the [Manage your subscription](./manage-your-subscription#manage-your-subscription-plan) guide.
*   Charges will come from AWS rather than Supabase, using the default payment method set in your AWS account.
*   The [Spend Cap](/docs/guides/platform/cost-control#spend-cap) for the organization is disabled. The Spend Cap is not available for organizations managed through AWS.
*   When you downgrade your plan to the Free Plan, all projects within the organization will be paused if you exceed the [free projects limit](/docs/guides/platform/billing-on-supabase#free-plan).


### Linking an existing Supabase organization

Linking an existing organization will result in the following:

*   The organization will be upgraded or downgraded to the plan purchased on the AWS Marketplace.
*   The organization’s billing cycle will be adjusted. The start date will be set to the date your marketplace subscription became active.
*   The credit card you have on file with Supabase may receive a closing charge. This charge covers usage costs incurred up until the point when the marketplace subscription became active.



## Prerequisites for linking a Supabase organization to a marketplace subscription

*   The Supabase user must have the Owner or Admin role
*   There must be no overdue invoices within the organization
*   The organization must not already be managed through another marketplace (e.g. Vercel Marketplace)



# AWS Marketplace FAQ



#### The payment for completing the subscription on the AWS Marketplace fails.

For more information on payment errors, refer to the [AWS documentation](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-paying-for-products.html#payment-methods).


#### How can the Spend Cap for an organization managed through the AWS Marketplace be enabled?

For organizations on the Pro Plan that are managed through the AWS Marketplace, the Spend Cap is not available.
In your AWS account, you can set up a budget for marketplace purchases (or for a specific marketplace product) and receive notifications once the budget is exceeded.


#### How to cancel your AWS Marketplace subscription

You can cancel your marketplace subscription within 48 hours of purchase. To do so, open a support ticket via the Supabase dashboard. After the 48-hour period, cancellation is no longer possible. If you cancel within the first 48 hours, the upfront charge for the fixed subscription fee will be refunded. Any usage costs incurred up to that point will not be refunded.


#### Does purchasing Supabase through the AWS Marketplace count toward your AWS spend commitment?

Yes, marketplace purchases do count toward the spend commitment.



# Getting Started




## Before you start

Depending on whether a Supabase organization is managed and billed through the AWS Marketplace or directly through the Supabase platform, there are differences. To help you make an informed decision about which approach is better suited for your needs, you can find an overview of these differences in the table below.

| Feature/Aspect       | Managed via AWS Marketplace                                                                                                                                       | Managed directly via Supabase platform                                                                                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available Plans      | Pro, Team, Enterprise                                                                                                                                             | Free, Pro, Team, Enterprise                                                                                                                                                                           |
| Mid-cycle downgrades | No                                                                                                                                                                | Yes                                                                                                                                                                                                   |
| Cost Control         | Spend Cap not available                                                                                                                                           | Spend Cap available                                                                                                                                                                                   |
| Downgrade Behaviour  | If a downgrade to the Free Plan causes you to exceed the [free projects limit](/docs/guides/platform/billing-on-supabase#free-plan), all projects will be paused. | If a downgrade to the Free Plan causes you to exceed the [free projects limit](/docs/guides/platform/billing-on-supabase#free-plan), you have the option to prevent pausing by transferring projects. |
| Invoicing            | Separate invoices, one for fixed costs and one for usage costs                                                                                                    | One invoice for both fixed costs and usage costs                                                                                                                                                      |



## Purchase Supabase through the AWS Marketplace

Purchasing Supabase through the AWS Marketplace involves two steps. First, you purchase the corresponding subscription on the marketplace. Then, to complete the setup, you must link this subscription to a Supabase organization on the Supabase platform.

For more details on completing the setup and what it means to link an organization, see our [Account Setup guide](./account-setup).

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Go to the AWS Marketplace" fullWidth>
      Go to the [Supabase product page on the AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-zjciuce2qsb3q) and click "View purchase options".

      <Image alt="Supabase product overview on the AWS Marketplace" src="/docs/img/guides/platform/aws-marketplace-listing-overview.png" zoomable />
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Configure the subscription" fullWidth>
      Select the desired plan (Pro Plan or Team Plan) and configure whether the subscription should automatically renew after one month.

      <Admonition type="danger">
        Disabling auto-renewal means that the subscription will be downgraded to the Free Plan after one month.

        If the downgrade causes you to exceed the [free projects limit](/docs/guides/platform/billing-on-supabase#free-plan), **all** projects within the organization will be paused. We do not make the decision about which projects continue to run and which are paused. You must then decide which projects you want to keep active and manually reactivate them through the Supabase dashboard.
      </Admonition>

      <Image alt="Supabase purchase options on the AWS Marketplace" src="/docs/img/guides/platform/aws-marketplace-listing-purchase-options.png" zoomable />
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Subscribe" fullWidth>
      Click "Subscribe" at the bottom of the page.

      <Image alt="Supabase product subscribe" src="/docs/img/guides/platform/aws-marketplace-listing-subscribe.png" zoomable />
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Go to the Supabase platform" fullWidth>
      After the payment has been confirmed and your marketplace subscription is active, click "Set up your account" to be redirected to the Supabase platform.

      <Image alt="Supabase product subscribe" src="/docs/img/guides/platform/aws-marketplace-listing-success.png" zoomable />
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Complete the setup on the Supabase platform" fullWidth>
      Complete the setup by linking a Supabase organization to the AWS Marketplace subscription.

      <Image
        alt="Supabase product subscribe"
        src={{
            dark: '/docs/img/guides/platform/aws-marketplace-onboarding-page--dark.png',
            light: '/docs/img/guides/platform/aws-marketplace-onboarding-page--light.png',
          }}
        zoomable
      />
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Invoices




## Where to find your invoices

You can view your invoices in the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/home#/bills) under the "Bills" section.

<Image alt="Subscription upgrade modal" src="/docs/img/guides/platform/aws-marketplace-invoices.png" zoomable />



## What invoices you get from AWS

You'll receive two invoices for your marketplace subscription.


### Invoice 1 - charge type "subscription"

*   What for: The fixed subscription fee paid in advance
*   When: At the time of subscription, and in subsequent months on the same day of the month the subscription was started


### Invoice 2 - charge type "usage"

*   What for: Usage that exceeds the quota included in the plan, or usage not covered by the plan (e.g. Custom Domain add-on, IPv4 add-on, additionally provisioned Disk IOPS).
*   When: No later than the third day of the month for the previous month. This is independent of your subscription’s billing cycle and instead covers the period from the first to the last day of the previous month.



## More information

*   Detailed explanations of how each usage item is billed, independent of the AWS Marketplace. Refer to the [Manage Your Usage guide](../manage-your-usage).



# Manage your subscription




## Manage your subscription plan

Plan changes are not made on the Supabase dashboard, but instead through the AWS Marketplace. The easiest way to navigate to the corresponding page on the marketplace is through the Supabase dashboard.

1.  On the [organization's billing page](/dashboard/org/_/billing), go to section **Subscription Plan**
2.  Click **Change subscription plan**
3.  On the side panel, follow the link to the AWS Marketplace


### Upgrade

You can upgrade your plan at any time. The new plan will be active immediately, and you will be charged a prorated amount for the remainder of the current billing cycle. The charge for the upgrade also factors in the upfront payment you have already made for your existing plan.

<Image
  alt="AWS Marketplace modify contract page"
  src={{
    light: '/docs/img/guides/platform/aws-marketplace-change-plan.png',
    dark: '/docs/img/guides/platform/aws-marketplace-change-plan.png',
  }}
  zoomable
/>


### Downgrade

Downgrades are only possible at the end of the billing cycle, not in the middle of a billing cycle.


#### Downgrade to the Free Plan

If you want your subscription to be downgraded to the Free Plan at the end of the current billing cycle, you need to disable auto-renewal for the marketplace subscription.

<Admonition type="danger">
  If the downgrade causes you to exceed the [free projects limit](/docs/guides/platform/billing-on-supabase#free-plan), **all** projects within the organization will be paused. We do not make the decision about which projects continue to run and which are paused. You must then decide which projects you want to keep active and manually reactivate them through the Supabase dashboard.
</Admonition>

<Image
  alt="AWS Marketplace modify contract page"
  src={{
    light: '/docs/img/guides/platform/aws-marketplace-configure-auto-renewal.png',
    dark: '/docs/img/guides/platform/aws-marketplace-configure-auto-renewal.png',
  }}
  zoomable
/>


#### Downgrade to a paid plan

A downgrade to a paid plan (Pro Plan / Team Plan) involves two steps.

**Step 1:** Let the current subscription on the higher plan expire, meaning turn off auto-renewal
**Step 2:** Start a new subscription on the lower plan



## Manage your payment methods

You can manage your payment methods through the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing).



## Manage your billing details

You can manage billing details, such as the billing address or tax ID, through the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing).



# Customizing email templates

Customizing local email templates using config.toml.

You can customize the email templates for local development [using the `config.toml` settings](/docs/guides/cli/config#auth-config).



## Configuring templates

You should provide a relative URL to the `content_path` parameter, pointing to an HTML file which contains the template. For example

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="supabase/config.toml" label="supabase/config.toml">
    ```toml name=supabase/config.toml
    [auth.email.template.invite]
    subject = "You are invited to Acme Inc"
    content_path = "./supabase/templates/invite.html"
    ```
  </TabPanel>

  <TabPanel id="supabase/templates/invite.html" label="supabase/templates/invite.html">
    ```html name=supabase/templates/invite.html
    <html>
      <body>
        <h2>Confirm your signup</h2>
        <p><a href="{{ .ConfirmationURL }}">Confirm your email</a></p>
      </body>
    </html>
    ```
  </TabPanel>
</Tabs>



## Available email templates

There are several Auth email templates which can be configured. Each template serves a specific authentication flow:


### `auth.email.template.invite`

**Default subject**: "You have been invited"
**When sent**: When a user is invited to join your application via email invitation
**Purpose**: Allows administrators to invite users who don't have accounts yet
**Content**: Contains a link for the invited user to accept the invitation and create their account


### `auth.email.template.confirmation`

**Default subject**: "Confirm Your Signup"
**When sent**: When a user signs up and needs to verify their email address
**Purpose**: Email verification for new user registrations
**Content**: Contains a confirmation link to verify the user's email address


### `auth.email.template.recovery`

**Default subject**: "Reset Your Password"
**When sent**: When a user requests a password reset
**Purpose**: Password recovery flow for users who forgot their password
**Content**: Contains a link to reset the user's password


### `auth.email.template.magic_link`

**Default subject**: "Your Magic Link"
**When sent**: When a user requests a magic link for passwordless authentication
**Purpose**: Passwordless login using email links
**Content**: Contains a secure link that automatically logs the user in when clicked


### `auth.email.template.email_change`

**Default subject**: "Confirm Email Change"
**When sent**: When a user requests to change their email address
**Purpose**: Verification for email address changes
**Content**: Contains a confirmation link to verify the new email address


### `auth.email.template.reauthentication`

**Default subject**: "Confirm Reauthentication"
**When sent**: When a user needs to re-authenticate for sensitive operations
**Purpose**: Additional verification for sensitive actions (like changing password, deleting account)
**Content**: Contains a 6-digit OTP code for verification



## Template variables

The templating system provides the following variables for use:


### `ConfirmationURL`

Contains the confirmation URL. For example, a signup confirmation URL would look like:

```
https://project-ref.supabase.co/auth/v1/verify?token={{ .TokenHash }}&type=email&redirect_to=https://example.com/path
```

**Usage**

```html
<p>Click here to confirm: {{ .ConfirmationURL }}</p>
```


### `Token`

Contains a 6-digit One-Time-Password (OTP) that can be used instead of the `ConfirmationURL`.

**Usage**

```html
<p>Here is your one time password: {{ .Token }}</p>
```


### `TokenHash`

Contains a hashed version of the `Token`. This is useful for constructing your own email link in the email template.

**Usage**

```html
<p>Follow this link to confirm your user:</p>
<p>
  <a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email"
    >Confirm your email</a
  >
</p>
```


### `SiteURL`

Contains your application's Site URL. This can be configured in your project's [authentication settings](/dashboard/project/_/auth/url-configuration).

**Usage**

```html
<p>Visit <a href="{{ .SiteURL }}">here</a> to log in.</p>
```


### `Email`

Contains the user's email address.

**Usage**

```html
<p>A recovery request was sent to {{ .Email }}.</p>
```


### `NewEmail`

Contains the new user's email address. This is only available in the `email_change` email template.

**Usage**

```html
<p>You are requesting to update your email address to {{ .NewEmail }}.</p>
```



## Deploying email templates

These settings are for local development. To apply the changes locally, stop and restart the Supabase containers:

```sh
supabase stop && supabase start
```

For hosted projects managed by Supabase, copy the templates into the [Email Templates](/dashboard/project/_/auth/templates) section of the Dashboard.



# Declarative database schemas

Manage your database schemas in one place and generate versioned migrations.


## Overview

Declarative schemas provide a developer-friendly way to maintain <InfoTooltip tooltipContent={<><p>Files of SQL statements that track the evolution of your database schema over time.<br />They allow you to version control your database schema alongside your application code.</p><p>See the <Link href="/guides/deployment/database-migrations" className="underline">database migrations</Link> guide to learn more.</p></>}>schema migrations</InfoTooltip>.

[Migrations](/docs/guides/deployment/database-migrations) are traditionally managed imperatively (you provide the instructions on how exactly to change the database). This can lead to related information being scattered over multiple migration files. With declarative schemas, you instead declare the state you want your database to be in, and the instructions are generated for you.



## Schema migrations

Schema migrations are SQL statements written in Data Definition Language. They are versioned in your `supabase/migrations` directory to ensure schema consistency between local and remote environments.


### Declaring your schema

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create your first schema file">
      Create a SQL file in `supabase/schemas` directory that defines an `employees` table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="supabase/schemas/employees.sql" label="supabase/schemas/employees.sql">
          ```sql name=supabase/schemas/employees.sql
          create table "employees" (
            "id" integer not null,
            "name" text
          );
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Generate a migration file">
      Generate a migration file by diffing against your declared schema.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase db diff -f create_employees_table
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Start the local database and apply migrations">
      Start the local database first. Then, apply the migration manually to see your schema changes in the local Dashboard.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase start
          supabase migration up
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>


### Updating your schema

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Add a new column">
      Edit `supabase/schemas/employees.sql` file to add a new column to `employees` table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="supabase/schemas/employees.sql" label="supabase/schemas/employees.sql">
          ```sql name=supabase/schemas/employees.sql
          create table "employees" (
            "id" integer not null,
            "name" text,
            "age" smallint not null
          );
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<Admonition type="tip">
  Some entities like views and enums expect columns to be declared in a specific order. To avoid messy diffs, always append new columns to the end of the table.
</Admonition>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Generate a new migration">
      Diff existing migrations against your declared schema.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase db diff -f add_age
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Review the generated migration">
      Verify that the generated migration contain a single incremental change.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="supabase/migrations/<timestamp>_add_age.sql" label="supabase/migrations/<timestamp>_add_age.sql">
          ```sql name=supabase/migrations/<timestamp>_add_age.sql
          alter table "public"."employees" add column "age" smallint not null;
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Apply the pending migration">
      Start the database locally and apply the pending migration.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase migration up
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>


### Deploying your schema changes

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Log in to the Supabase CLI">
      [Log in](/docs/reference/cli/supabase-login) via the Supabase CLI.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase login
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Link your remote project">
      Follow the on-screen prompts to [link](/docs/reference/cli/supabase-link) your remote project.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase link
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Deploy database changes">
      [Push](/docs/reference/cli/supabase-db-push) your changes to the remote database.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="Terminal" label="Terminal">
          ```bash name=Terminal
          supabase db push
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>


### Managing dependencies

As your database schema evolves, you will probably start using more advanced entities like views and functions. These entities are notoriously verbose to manage using plain migrations because the entire body must be recreated whenever there is a change. Using declarative schema, you can now edit them in-place so it’s much easier to review.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="supabase/schemas/employees.sql" label="supabase/schemas/employees.sql">
    ```sql name=supabase/schemas/employees.sql
    create table "employees" (
      "id" integer not null,
      "name" text,
      "age" smallint not null
    );

    create view "profiles" as
      select id, name from "employees";

    create function "get_age"(employee_id integer) RETURNS smallint
      LANGUAGE "sql"
    AS $$
      select age
      from employees
      where id = employee_id;
    $$;
    ```
  </TabPanel>
</Tabs>

Your schema files are run in lexicographic order by default. The order is important when you have foreign keys between multiple tables as the parent table must be created first. For example, your `supabase` directory may end up with the following structure.

```bash
.
└── supabase/
    ├── schemas/
    │   ├── employees.sql
    │   └── managers.sql
    └── migrations/
        ├── 20241004112233_create_employees_table.sql
        ├── 20241005112233_add_employee_age.sql
        └── 20241006112233_add_managers_table.sql
```

For small projects with only a few tables, the default schema order may be sufficient. However, as your project grows, you might need more control over the order in which schemas are applied. To specify a custom order for applying the schemas, you can declare them explicitly in `config.toml`. Any glob patterns will evaluated, deduplicated, and sorted in lexicographic order. For example, the following pattern ensures `employees.sql` is always executed first.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="supabase/config.toml" label="supabase/config.toml">
    ```toml name=supabase/config.toml
    [db.migrations]
    schema_paths = [
      "./schemas/employees.sql",
      "./schemas/*.sql",
    ]
    ```
  </TabPanel>
</Tabs>


### Pulling in your production schema

To set up declarative schemas on a existing project, you can pull in your production schema by running:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="Terminal" label="Terminal">
    ```bash name=Terminal
    supabase db dump > supabase/schemas/prod.sql
    ```
  </TabPanel>
</Tabs>

From there, you can start breaking down your schema into smaller files and generate migrations. You can do this all at once, or incrementally as you make changes to your schema.


### Rolling back a schema change

During development, you may want to rollback a migration to keep your new schema changes in a single migration file. This can be done by resetting your local database to a previous version.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="Terminal" label="Terminal">
    ```bash name=Terminal
    supabase db reset --version 20241005112233
    ```
  </TabPanel>
</Tabs>

After a reset, you can [edit the schema](#updating-your-schema) and regenerate a new migration file. Note that you should not reset a version that's already deployed to production.

If you need to rollback a migration that's already deployed, you should first revert changes to the schema files. Then you can generate a new migration file containing the down migration. This ensures your production migrations are always rolling forward.

<Admonition type="danger">
  SQL statements generated in a down migration are usually destructive. You must review them carefully to avoid unintentional data loss.
</Admonition>



## Known caveats

The `migra` diff tool used for generating schema diff is capable of tracking most database changes. However, there are edge cases where it can fail.

If you need to use any of the entities below, remember to add them through [versioned migrations](/docs/guides/deployment/database-migrations) instead.


### Data manipulation language

*   DML statements such as `insert`, `update`, `delete`, etc., are not captured by schema diff


### View ownership

*   [view owner and grants](https://github.com/djrobstep/migra/issues/160#issuecomment-1702983833)
*   [security invoker on views](https://github.com/djrobstep/migra/issues/234)
*   [materialized views](https://github.com/djrobstep/migra/issues/194)
*   doesn’t recreate views when altering column type


### RLS policies

*   [alter policy statements](https://github.com/djrobstep/schemainspect/blob/master/schemainspect/pg/obj.py#L228)
*   [column privileges](https://github.com/djrobstep/schemainspect/pull/67)


### Other entities

*   schema privileges are not tracked because each schema is diffed separately
*   [comments are not tracked](https://github.com/djrobstep/migra/issues/69)
*   [partitions are not tracked](https://github.com/djrobstep/migra/issues/186)
*   [`alter publication ... add table ...`](https://github.com/supabase/cli/issues/883)
*   [create domain statements are ignored](https://github.com/supabase/cli/issues/2137)
*   [grant statements are duplicated from default privileges](https://github.com/supabase/cli/issues/1864)



# Managing config and secrets



The Supabase CLI uses a `config.toml` file to manage local configuration. This file is located in the `supabase` directory of your project.



## Config reference

The `config.toml` file is automatically created when you run `supabase init`.

There are a wide variety of options available, which can be found in the [CLI Config Reference](/docs/guides/cli/config).

For example, to enable the "Apple" OAuth provider for local development, you can append the following information to `config.toml`:

```toml
[auth.external.apple]
enabled = false
client_id = ""
secret = ""
redirect_uri = "" # Overrides the default auth redirectUrl.
```



## Using secrets inside config.toml

You can reference environment variables within the `config.toml` file using the `env()` function. This will detect any values stored in an `.env` file at the root of your project directory. This is particularly useful for storing sensitive information like API keys, and any other values that you don't want to check into version control.

```
.
├── .env
├── .env.example
└── supabase
    └── config.toml
```

<Admonition type="danger">
  Do NOT commit your `.env` into git. Be sure to configure your `.gitignore` to exclude this file.
</Admonition>

For example, if your `.env` contained the following values:

```bash
GITHUB_CLIENT_ID=""
GITHUB_SECRET=""
```

Then you would reference them inside of our `config.toml` like this:

```toml
[auth.external.github]
enabled = true
client_id = "env(GITHUB_CLIENT_ID)"
secret = "env(GITHUB_SECRET)"
redirect_uri = "" # Overrides the default auth redirectUrl.
```


### Going further

For more advanced secrets management workflows, including:

*   **Using dotenvx for encrypted secrets**: Learn how to securely manage environment variables across different branches and environments
*   **Branch-specific secrets**: Understand how to manage secrets for different deployment environments
*   **Encrypted configuration values**: Use encrypted values directly in your `config.toml`

See the [Managing secrets for branches](/docs/guides/deployment/branching#managing-secrets-for-branches) section in our branching documentation, or check out the [dotenvx example repository](https://github.com/supabase/supabase/blob/master/examples/slack-clone/nextjs-slack-clone-dotenvx/README.md) for a complete implementation.



# Local development with schema migrations

Develop locally with the Supabase CLI and schema migrations.

Supabase is a flexible platform that lets you decide how you want to build your projects. You can use the Dashboard directly to get up and running quickly, or use a proper local setup. We suggest you work locally and deploy your changes to a linked project on the [Supabase Platform](https://app.supabase.io/).

Develop locally using the CLI to run a local Supabase stack. You can use the integrated Studio Dashboard to make changes, then capture your changes in schema migration files, which can be saved in version control.

Alternatively, if you're comfortable with migration files and SQL, you can write your own migrations and push them to the local database for testing before sharing your changes.



## Database migrations

Database changes are managed through "migrations." Database migrations are a common way of tracking changes to your database over time.

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/Kx5nHBmIxyQ" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>

For this guide, we'll create a table called `employees` and see how we can make changes to it.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create your first migration file">
      To get started, generate a [new migration](/docs/reference/cli/supabase-migration-new) to store the SQL needed to create our `employees` table
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase migration new create_employees_table
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Add the SQL to your migration file">
      This creates a new migration: supabase/migrations/\<timestamp>
      \_create\_employees\_table.sql.

      To that file, add the SQL to create this `employees` table
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="20250101000000_create_employees_table.sql">
        ```sql name=20250101000000_create_employees_table.sql
        create table employees (
          id bigint primary key generated always as identity,
          name text,
          email text,
          created_at timestamptz default now()
        );
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Apply your migration">
      Now that you have a migration file, you can run this migration and create the `employees` table.

      Use the `reset` command here to reset the database to the current migrations
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db reset
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Modify your employees table">
      Now you can visit your new `employees` table in the Dashboard.

      Next, modify your `employees` table by adding a column for department. Create a new migration file for that.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase migration new add_department_to_employees_table
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Add a new column to your table">
      This creates a new migration file: supabase/migrations/\<timestamp>
      \_add\_department\_to\_employees\_table.sql.

      To that file, add the SQL to create a new department column
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="20250101000001_add_department_to_employees_table.sql">
        ```sql name=20250101000001_add_department_to_employees_table.sql
        alter table if exists public.employees
        add department text default 'Hooli';
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>


### Add sample data

Now that you are managing your database with migrations scripts, it would be great have some seed data to use every time you reset the database.

For this, you can create a seed script in `supabase/seed.sql`.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Populate your table">
      Insert data into your `employees` table with your `supabase/seed.sql` file.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="supabase/seed.sql">
        ```sql name=supabase/seed.sql
        insert into public.employees
          (name)
        values
          ('Erlich Bachman'),
          ('Richard Hendricks'),
          ('Monica Hall');
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Reset your database">
      Reset your database (apply current migrations), and populate with seed data
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        supabase db reset
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

You should now see the `employees` table, along with your seed data in the Dashboard! All of your database changes are captured in code, and you can reset to a known state at any time, complete with seed data.


### Diffing changes

This workflow is great if you know SQL and are comfortable creating tables and columns. If not, you can still use the Dashboard to create tables and columns, and then use the CLI to diff your changes and create migrations.

Create a new table called `cities`, with columns `id`, `name` and `population`. To see the corresponding SQL for this, you can use the `supabase db diff --schema public` command. This will show you the SQL that will be run to create the table and columns. The output of `supabase db diff` will look something like this:

```
Diffing schemas: public
Finished supabase db diff on branch main.

create table "public"."cities" (
    "id" bigint primary key generated always as identity,
    "name" text,
    "population" bigint
);

```

Alternately, you can view your table definitions directly from the Table Editor:

![SQL Definition](/docs/img/guides/cli/sql-definitions.png)

You can then copy this SQL into a new migration file, and run `supabase db reset` to apply the changes.

The last step is deploying these changes to a live Supabase project.



## Deploy your project

You've been developing your project locally, making changes to your tables via migrations. It's time to deploy your project to the Supabase Platform and start scaling up to millions of users! Head over to [Supabase](/dashboard) and create a new project to deploy to.


### Log in to the Supabase CLI

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="Terminal" label="Terminal">
    ```bash name=Terminal
    supabase login
    ```
  </TabPanel>

  <TabPanel id="npx" label="npx">
    ```bash name=npx
    npx supabase login
    ```
  </TabPanel>
</Tabs>


### Link your project

Associate your project with your remote project using [`supabase link`](/docs/reference/cli/usage#supabase-link).

```bash
supabase link --project-ref <project-id>

# You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>

supabase db pull

# Capture any changes that you have made to your remote database before you went through the steps above

# If you have not made any changes to the remote database, skip this step
```

`supabase/migrations` is now populated with a migration in `<timestamp>_remote_schema.sql`.
This migration captures any changes required for your local database to match the schema of your remote Supabase project.

Review the generated migration file and once happy, apply the changes to your local instance:

```bash

# To apply the new migration to your local database:
supabase migration up


# To reset your local database completely:
supabase db reset
```

<Admonition type="note">
  There are a few commands required to link your project. We are in the process of consolidating these commands into a single command. Bear with us!
</Admonition>


### Deploy database changes

Deploy any local database migrations using [`db push`](/docs/reference/cli/usage#supabase-db-push):

```sh
supabase db push
```

Visiting your live project on [Supabase](/dashboard), you'll see a new `employees` table, complete with the `department` column you added in the second migration above.


### Deploy Edge Functions

If your project uses Edge Functions, you can deploy these using [`functions deploy`](/docs/reference/cli/usage#supabase-functions-deploy):

```sh
supabase functions deploy <function_name>
```


### Use Auth locally

To use Auth locally, update your project's `supabase/config.toml` file that gets created after running `supabase init`. Add any providers you want, and set enabled to `true`.

```bash supabase/config.toml
[auth.external.github]
enabled = true
client_id = "env(SUPABASE_AUTH_GITHUB_CLIENT_ID)"
secret = "env(SUPABASE_AUTH_GITHUB_SECRET)"
redirect_uri = "http://localhost:54321/auth/v1/callback"
```

As a best practice, any secret values should be loaded from environment variables. You can add them to `.env` file in your project's root directory for the CLI to automatically substitute them.

```bash .env
SUPABASE_AUTH_GITHUB_CLIENT_ID="redacted"
SUPABASE_AUTH_GITHUB_SECRET="redacted"
```

For these changes to take effect, you need to run `supabase stop` and `supabase start` again.

If you have additional triggers or RLS policies defined on your `auth` schema, you can pull them as a migration file locally.

```bash
supabase db pull --schema auth
```


### Sync storage buckets

Your RLS policies on storage buckets can be pulled locally by specifying `storage` schema. For example,

```bash
supabase db pull --schema storage
```

The buckets and objects themselves are rows in the storage tables so they won't appear in your schema. You can instead define them via `supabase/config.toml` file. For example,

```bash supabase/config.toml
[storage.buckets.images]
public = false
file_size_limit = "50MiB"
allowed_mime_types = ["image/png", "image/jpeg"]
objects_path = "./images"
```

This will upload files from `supabase/images` directory to a bucket named `images` in your project with one command.

```bash
supabase seed buckets
```


### Sync any schema with `--schema`

You can synchronize your database with a specific schema using the `--schema` option as follows:

```bash
supabase db pull --schema <schema_name>
```

<Admonition type="caution">
  Using `--schema`

  If the local `supabase/migrations` directory is empty, the `db pull` command will ignore the `--schema` parameter.

  To fix this, you can pull twice:

  ```bash
  supabase db pull
  supabase db pull --schema <schema_name>
  ```
</Admonition>



## Limitations and considerations

The local development environment is not as feature-complete as the Supabase Platform. Here are some of the differences:

*   You cannot update your project settings in the Dashboard. This must be done using the local config file.
*   The CLI version determines the local version of Studio used, so make sure you keep your local [Supabase CLI up to date](https://github.com/supabase/cli#getting-started). We're constantly adding new features and bug fixes.



# Restoring a downloaded backup locally

Restore a backup of a remote database on a local instance to inspect and extract data

If your paused project has exceeded its [restoring time limit](/docs/guides/platform/upgrading#time-limits), you can download a backup from the dashboard and restore it to your local development environment. This might be useful for inspecting and extracting data from your paused project.

<Admonition type="caution">
  If you want to restore your backup to a hosted Supabase project, follow the [Migrating within Supabase guide](/docs/guides/platform/migrating-within-supabase) instead.
</Admonition>



## Downloading your backup

First, download your project's backup file from dashboard and identify its backup image version (following the `PG:` prefix):

<Image zoomable alt="Project Paused: 90 Days Remaining" src="/docs/img/guides/platform/paused-dl-image-version.png" />



## Restoring your backup

Given Postgres version `15.6.1.115`, start Postgres locally with `db_cluster.backup` being the path to your backup file.

```sh
supabase init
echo '15.6.1.115' > supabase/.temp/postgres-version
supabase db start --from-backup db_cluster.backup
```

Note that the earliest Supabase Postgres version that supports a local restore is `15.1.0.55`. If your hosted project was running on earlier versions, you will likely run into errors during restore. Before submitting any support ticket, make sure you have attached the error logs from `supabase_db_*` docker container.

Once your local database starts up successfully, you can connect using psql to verify that all your data is restored.

```sh
psql 'postgresql://postgres:postgres@localhost:54322/postgres'
```

If you want to use other services like Auth, Storage, and Studio dashboard together with your restored database, restart the local development stack.

```sh
supabase stop
supabase start
```

A Postgres database started with Supabase CLI is not production ready and should not be used outside of local development.



# Seeding your database

Populate your database with initial data for reproducible environments across local and testing.


## What is seed data?

Seeding is the process of populating a database with initial data, typically used to provide sample or default records for testing and development purposes. You can use this to create "reproducible environments" for local development, staging, and production.



## Using seed files

Seed files are executed the first time you run `supabase start` and every time you run `supabase db reset`. Seeding occurs *after* all database migrations have been completed. As a best practice, only include data insertions in your seed files, and avoid adding schema statements.

By default, if no specific configuration is provided, the system will look for a seed file matching the pattern `supabase/seed.sql`. This maintains backward compatibility with earlier versions, where the seed file was placed in the `supabase` folder.

You can add any SQL statements to this file. For example:

```sql
insert into countries
  (name, code)
values
  ('United States', 'US'),
  ('Canada', 'CA'),
  ('Mexico', 'MX');
```

If you want to manage multiple seed files or organize them across different folders, you can configure additional paths or glob patterns in your `config.toml` (see the [next section](#splitting-up-your-seed-file) for details).


### Splitting up your seed file

For better modularity and maintainability, you can split your seed data into multiple files. For example, you can organize your seeds by table and include files such as `countries.sql` and `cities.sql`. Configure them in `config.toml` like so:

```toml supabase/config.toml
[db.seed]
enabled = true
sql_paths = ['./countries.sql', './cities.sql']
```

Or to include all `.sql` files under a specific folder you can do:

```toml supabase/config.toml
[db.seed]
enabled = true
sql_paths = ['./seeds/*.sql']
```

<Admonition type="tip">
  The CLI processes seed files in the order they are declared in the `sql_paths` array. If a glob pattern is used and matches multiple files, those files are sorted in lexicographic order to ensure consistent execution. Additionally:

  *   The base folder for the pattern matching is `supabase` so `./countries.sql` will search for `supabase/countries.sql`
  *   Files matched by multiple patterns will be deduplicated to prevent redundant seeding.
  *   If a pattern does not match any files, a warning will be logged to help you troubleshoot potential configuration issues.
</Admonition>



## Generating seed data

You can generate seed data for local development using [Snaplet](https://github.com/snaplet/seed).

<Admonition type="tip">
  To use Snaplet, you need to have Node.js and npm installed. You can add Node.js to your project by running `npm init -y` in your project directory.
</Admonition>

If this is your first time using Snaplet to seed your project, you'll need to set up Snaplet with the following command:

```bash
npx @snaplet/seed init
```

This command will analyze your database and its structure, and then generate a JavaScript client which can be used to define exactly how your data should be generated using code. The `init` command generates a configuration file, `seed.config.ts` and an example script, `seed.ts`, as a starting point.

<Admonition type="tip">
  During `init` if you are not using an Object Relational Mapper (ORM) or your ORM is not in the supported list, choose `node-postgres`.
</Admonition>

In most cases you only want to generate data for specific schemas or tables. This is defined with `select`. Here is an example `seed.config.ts` configuration file:

```ts
export default defineConfig({
  adapter: async () => {
    const client = new Client({
      connectionString: 'postgresql://postgres:postgres@localhost:54322/postgres',
    })
    await client.connect()
    return new SeedPg(client)
  },
  // We only want to generate data for the public schema
  select: ['!*', 'public.*'],
})
```

Suppose you have a database with the following schema:

![An example schema](/docs/img/guides/cli/snaplet-example-schema.png)

You can use the seed script example generated by Snaplet `seed.ts` to define the values you want to generate. For example:

*   A `Post` with the title `"There is a lot of snow around here!"`
*   The `Post.createdBy` user with an email address ending in `"@acme.org"`
*   Three `Post.comments` from three different users.

```ts seed.ts
import { createSeedClient } from '@snaplet/seed'
import { copycat } from '@snaplet/copycat'

async function main() {
  const seed = await createSeedClient({ dryRun: true })

  await seed.Post([
    {
      title: 'There is a lot of snow around here!',
      createdBy: {
        email: (ctx) =>
          copycat.email(ctx.seed, {
            domain: 'acme.org',
          }),
      },
      Comment: (x) => x(3),
    },
  ])

  process.exit()
}

main()
```

Running `npx tsx seed.ts > supabase/seed.sql` generates the relevant SQL statements inside your `supabase/seed.sql` file:

```sql
-- The `Post.createdBy` user with an email address ending in `"@acme.org"`
INSERT INTO "User" (name, email) VALUES ("John Snow", "snow@acme.org")

--- A `Post` with the title `"There is a lot of snow around here!"`
INSERT INTO "Post" (title, content, createdBy) VALUES (
  "There is a lot of snow around here!",
  "Lorem ipsum dolar",
  1)

--- Three `Post.Comment` from three different users.
INSERT INTO "User" (name, email) VALUES ("Stephanie Shadow", "shadow@domain.com")
INSERT INTO "Comment" (text, userId, postId) VALUES ("I love cheese", 2, 1)

INSERT INTO "User" (name, email) VALUES ("John Rambo", "rambo@trymore.dev")
INSERT INTO "Comment" (text, userId, postId) VALUES ("Lorem ipsum dolar sit", 3, 1)

INSERT INTO "User" (name, email) VALUES ("Steven Plank", "s@plank.org")
INSERT INTO "Comment" (text, userId, postId) VALUES ("Actually, that's not correct...", 4, 1)
```

Whenever your database structure changes, you will need to regenerate `@snaplet/seed` to keep it in sync with the new structure. You can do this by running:

```bash
npx @snaplet/seed sync
```

You can further enhance your seed script by using Large Language Models to generate more realistic data. To enable this feature, set one of the following environment variables in your `.env` file:

```plaintext
OPENAI_API_KEY=<your_openai_api_key>
GROQ_API_KEY=<your_groq_api_key>
```

After setting the environment variables, run the following commands to sync and generate the seed data:

```bash
npx @snaplet/seed sync
npx tsx seed.ts > supabase/seed.sql
```

For more information, check out Snaplet's [seed documentation](https://snaplet-seed.netlify.app/seed/integrations/supabase)



# Testing Overview



Testing is a critical part of database development, especially when working with features like Row Level Security (RLS) policies. This guide provides a comprehensive approach to testing your Supabase database.



## Testing approaches


### Database unit testing with pgTAP

[pgTAP](https://pgtap.org) is a unit testing framework for Postgres that allows testing:

*   Database structure: tables, columns, constraints
*   Row Level Security (RLS) policies
*   Functions and procedures
*   Data integrity

This example demonstrates setting up and testing RLS policies for a simple todo application:

1.  Create a test table with RLS enabled:

    ```sql
    -- Create a simple todos table
    create table todos (
    id uuid primary key default gen_random_uuid(),
    task text not null,
    user_id uuid references auth.users not null,
    completed boolean default false
    );

    -- Enable RLS
    alter table todos enable row level security;

    -- Create a policy
    create policy "Users can only access their own todos"
    on todos for all -- this policy applies to all operations
    to authenticated
    using ((select auth.uid()) = user_id);
    ```

2.  Set up your testing environment:

    ```bash
    # Create a new test for our policies using supabase cli
    supabase test new todos_rls.test
    ```

3.  Write your RLS tests:

    ```sql
    begin;
    -- install tests utilities
    -- install pgtap extension for testing
    create extension if not exists pgtap with schema extensions;
    -- Start declare we'll have 4 test cases in our test suite
    select plan(4);

    -- Setup our testing data
    -- Set up auth.users entries
    insert into auth.users (id, email) values
    	('123e4567-e89b-12d3-a456-426614174000', 'user1@test.com'),
    	('987fcdeb-51a2-43d7-9012-345678901234', 'user2@test.com');

    -- Create test todos
    insert into public.todos (task, user_id) values
    	('User 1 Task 1', '123e4567-e89b-12d3-a456-426614174000'),
    	('User 1 Task 2', '123e4567-e89b-12d3-a456-426614174000'),
    	('User 2 Task 1', '987fcdeb-51a2-43d7-9012-345678901234');

    -- as User 1
    set local role authenticated;
    set local request.jwt.claim.sub = '123e4567-e89b-12d3-a456-426614174000';

    -- Test 1: User 1 should only see their own todos
    select results_eq(
    	'select count(*) from todos',
    	ARRAY[2::bigint],
    	'User 1 should only see their 2 todos'
    );

    -- Test 2: User 1 can create their own todo
    select lives_ok(
    	$$insert into todos (task, user_id) values ('New Task', '123e4567-e89b-12d3-a456-426614174000'::uuid)$$,
    	'User 1 can create their own todo'
    );

    -- as User 2
    set local request.jwt.claim.sub = '987fcdeb-51a2-43d7-9012-345678901234';

    -- Test 3: User 2 should only see their own todos
    select results_eq(
    	'select count(*) from todos',
    	ARRAY[1::bigint],
    	'User 2 should only see their 1 todo'
    );

    -- Test 4: User 2 cannot modify User 1's todo
    SELECT results_ne(
    	$$ update todos set task = 'Hacked!' where user_id = '123e4567-e89b-12d3-a456-426614174000'::uuid returning 1 $$,
    	$$ values(1) $$,
    	'User 2 cannot modify User 1 todos'
    );

    select * from finish();
    rollback;
    ```

4.  Run the tests:

    ```bash
    supabase test db
    psql:todos_rls.test.sql:4: NOTICE:  extension "pgtap" already exists, skipping
    ./todos_rls.test.sql .. ok
    All tests successful.
    Files=1, Tests=6,  0 wallclock secs ( 0.01 usr +  0.00 sys =  0.01 CPU)
    Result: PASS
    ```


### Application-Level testing

Testing through application code provides end-to-end verification. Unlike database-level testing with pgTAP, application-level tests cannot use transactions for isolation.

<Admonition type="caution">
  Application-level tests should not rely on a clean database state, as resetting the database before each test can be slow and makes tests difficult to parallelize.
  Instead, design your tests to be independent by using unique user IDs for each test case.
</Admonition>

Here's an example using TypeScript that mirrors the pgTAP tests above:

```typescript
import { createClient } from '@supabase/supabase-js'
import { beforeAll, describe, expect, it } from 'vitest'
import crypto from 'crypto'

describe('Todos RLS', () => {
  // Generate unique IDs for this test suite to avoid conflicts with other tests
  const USER_1_ID = crypto.randomUUID()
  const USER_2_ID = crypto.randomUUID()

  const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_PUBLISHABLE_KEY!)

  beforeAll(async () => {
    // Setup test data specific to this test suite
    const adminSupabase = createClient(process.env.SUPABASE_URL!, process.env.SERVICE_ROLE_KEY!)

    // Create test users with unique IDs
    await adminSupabase.auth.admin.createUser({
      id: USER_1_ID,
      email: `user1-${USER_1_ID}@test.com`,
      password: 'password123',
      // We want the user to be usable right away without email confirmation
      email_confirm: true,
    })
    await adminSupabase.auth.admin.createUser({
      id: USER_2_ID,
      email: `user2-${USER_2_ID}@test.com`,
      password: 'password123',
      email_confirm: true,
    })

    // Create initial todos
    await adminSupabase.from('todos').insert([
      { task: 'User 1 Task 1', user_id: USER_1_ID },
      { task: 'User 1 Task 2', user_id: USER_1_ID },
      { task: 'User 2 Task 1', user_id: USER_2_ID },
    ])
  })

  it('should allow User 1 to only see their own todos', async () => {
    // Sign in as User 1
    await supabase.auth.signInWithPassword({
      email: `user1-${USER_1_ID}@test.com`,
      password: 'password123',
    })

    const { data: todos } = await supabase.from('todos').select('*')

    expect(todos).toHaveLength(2)
    todos?.forEach((todo) => {
      expect(todo.user_id).toBe(USER_1_ID)
    })
  })

  it('should allow User 1 to create their own todo', async () => {
    await supabase.auth.signInWithPassword({
      email: `user1-${USER_1_ID}@test.com`,
      password: 'password123',
    })

    const { error } = await supabase.from('todos').insert({ task: 'New Task', user_id: USER_1_ID })

    expect(error).toBeNull()
  })

  it('should allow User 2 to only see their own todos', async () => {
    // Sign in as User 2
    await supabase.auth.signInWithPassword({
      email: `user2-${USER_2_ID}@test.com`,
      password: 'password123',
    })

    const { data: todos } = await supabase.from('todos').select('*')
    expect(todos).toHaveLength(1)
    todos?.forEach((todo) => {
      expect(todo.user_id).toBe(USER_2_ID)
    })
  })

  it('should prevent User 2 from modifying User 1 todos', async () => {
    await supabase.auth.signInWithPassword({
      email: `user2-${USER_2_ID}@test.com`,
      password: 'password123',
    })

    // Attempt to update the todos we shouldn't have access to
    // result will be a no-op
    await supabase.from('todos').update({ task: 'Hacked!' }).eq('user_id', USER_1_ID)

    // Log back in as User 1 to verify their todos weren't changed
    await supabase.auth.signInWithPassword({
      email: `user1-${USER_1_ID}@test.com`,
      password: 'password123',
    })

    // Fetch User 1's todos
    const { data: todos } = await supabase.from('todos').select('*')

    // Verify that none of the todos were changed to "Hacked!"
    expect(todos).toBeDefined()
    todos?.forEach((todo) => {
      expect(todo.task).not.toBe('Hacked!')
    })
  })
})
```


#### Test isolation strategies

For application-level testing, consider these approaches for test isolation:

1.  **Unique Identifiers**: Generate unique IDs for each test suite to prevent data conflicts
2.  **Cleanup After Tests**: If necessary, clean up created data in an `afterAll` or `afterEach` hook
3.  **Isolated Data Sets**: Use prefixes or namespaces in data to separate test cases


### Continuous integration testing

Set up automated database testing in your CI pipeline:

1.  Create a GitHub Actions workflow `.github/workflows/db-tests.yml`:

```yaml
name: Database Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Supabase CLI
        uses: supabase/setup-cli@v1

      - name: Start Supabase
        run: supabase start

      - name: Run Tests
        run: supabase test db
```



## Best practices

1.  **Test Data Setup**

    *   Use begin and rollback to ensure test isolation
    *   Create realistic test data that covers edge cases
    *   Use different user roles and permissions in tests

2.  **RLS Policy Testing**

    *   Test Create, Read, Update, Delete operations
    *   Test with different user roles: anonymous and authenticated
    *   Test edge cases and potential security bypasses
    *   Always test negative cases: what users should not be able to do

3.  **CI/CD Integration**
    *   Run tests automatically on every pull request
    *   Include database tests in deployment pipeline
    *   Keep test runs fast using transactions



## Real-World examples

For more complex, real-world examples of database testing, check out:

*   [Database Tests Example Repository](https://github.com/usebasejump/basejump/tree/main/supabase/tests/database) - A production-grade example of testing RLS policies
*   [RLS Guide and Best Practices](https://github.com/orgs/supabase/discussions/14576)



## Troubleshooting

Common issues and solutions:

1.  **Test Failures Due to RLS**

    *   Ensure you've set the correct role `set local role authenticated;`
    *   Verify JWT claims are set `set local "request.jwt.claims"`
    *   Check policy definitions match your test assumptions

2.  **CI Pipeline Issues**
    *   Verify Supabase CLI is properly installed
    *   Ensure database migrations are run before tests
    *   Check for proper test isolation using transactions



## Additional resources

*   [pgTAP Documentation](https://pgtap.org)
*   [Supabase CLI Reference](/docs/reference/cli/supabase-test)
*   [pgTAP Supabase reference](/docs/guides/database/extensions/pgtap?queryGroups=database-method\&database-method=sql#testing-rls-policies)
*   [Database testing reference](/docs/guides/database/testing)



---
**Navigation:** [← Previous](./10-set-supabase-connection-session-pooler-on-port-543.md) | [Index](./index.md) | [Next →](./12-advanced-pgtap-testing.md)
