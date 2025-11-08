**Navigation:** [← Previous](./11-understanding-organizations.md) | [Index](./index.md) | [Next →](./13-create-a-project.md)

# Configure audit logs
Source: https://docs.pinecone.io/guides/production/configure-audit-logs

Enable audit logging to Amazon S3 for compliance

This page describes how to configure audit logs in Pinecone. Audit logs provide a detailed record of user, service account, and API actions that occur within Pinecone. Pinecone supports Amazon S3 as a destination for audit logs.

<Note>
  To enable and manage audit logs, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-roles). This feature is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>


## Enable audit logs

1. Set up a [IAM policy and role in Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3).
2. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging) in the Pinecone console.
3. Enter the **Role ARN** of the IAM role you created.
4. Enter the name of the Amazon S3 bucket you created.
   <Note>
     **Targeting a subdirectory:** You can write audit logs to a specific subdirectory by entering `bucket-name/subdirectory-path` in the bucket name field. For example: `my-bucket/pinecone-logs`. Make sure your [IAM policy is configured for subdirectory access](/guides/operations/integrations/integrate-with-amazon-s3#targeting-a-subdirectory-optional).
   </Note>
5. Click **Enable audit logging**.

Once you enable audit logs, Pinecone will start writing logs to the S3 bucket. In your bucket, you will also see a file named `audit-log-access-test`, which is a test file that Pinecone writes to verify that it has the necessary permissions to write logs to the bucket.


## View audit logs

Logs are written to the S3 bucket approximately every 30 minutes. Each log batch will be saved into its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled will be saved.

For more information about the log schema and captured events, see [Understanding security - Audit logs](/guides/production/security-overview#audit-logs).


## Edit audit log integration details

You can edit the details of the audit log integration in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Enter the new **Role ARN** or **AWS Bucket**.
3. Click **Update settings**.


## Disable audit logs

If you disable audit logs, logs not yet saved will be lost. You can disable audit logs in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. Click the toggle next to **Audit logs are active**.
3. Click **Confirm**.


## Remove audit log integration

If you remove the audit log integration, logs not yet saved will be lost. You can remove the audit log integration in the Pinecone console:

1. Go to [**Settings > Audit logs**](https://app.pinecone.io/organizations/-/settings/logging).
2. At the top of the page, click the **ellipsis (...) menu > Remove integration**.
3. Click **Remove integration**.



# Configure customer-managed encryption keys
Source: https://docs.pinecone.io/guides/production/configure-cmek

Use customer-managed encryption keys with AWS KMS.

This page describes how to set up and use customer-managed encryption keys (CMEK) to secure data within a Pinecone project. CMEK allows you to encrypt your data using keys that you manage in your cloud provider's key management system (KMS). Pinecone supports CMEK using Amazon Web Services (AWS) KMS.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>


## Set up CMEK using AWS KMS

### Before you begin

The following steps assume you have:

* Access to the [AWS console](https://console.aws.amazon.com/console/home).
* A [Pinecone Enterprise plan](https://www.pinecone.io/pricing/).

### 1. Create a role

In the [AWS console](https://console.aws.amazon.com/console/home), create a role that Pinecone can use to access the AWS Key Management System (KMS) key. You can either grant Pinecone access to a key in your account, or if your customers provide their own keys, you can grant access to keys that are outside of your account.

<Tabs>
  <Tab title="Grant access to key in your account">
    1. Open the [Amazon Identity and Access Management (IAM) console](https://console.aws.amazon.com/iam/).

    2. In the navigation pane, click **Roles**.

    3. Click **Create role**.

    4. In the **Trusted entity type** section, select **Custom trust policy**.

    5. In the **Custom trust policy** section, enter one of the following JSON snippets.

       Pick a snippet based on whether you want to allow Pinecone to assume a role from all regions or from explicit regions. Add an optional external ID for additional security. If you use an external ID, you must provide it to Pinecone when [adding a CMEK key](#add-a-key).

       <AccordionGroup>
         <Accordion title="Explicit regions + external ID">
           ```json JSON theme={null}
           {
               "Version": "2012-10-17",
               "Statement": [
                   {
                       "Sid": "AllowPineconeToAssumeIntoRoleFromExplicitRegionswithID",
                       "Effect": "Allow",
                       "Principal": {
                           "AWS": [
                               // Explicit role per Pinecone region. Replace XXXXXXXXXXXX with Pinecone's AWS account number.
                               "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_us-east-1",
                               "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_us-west-2",
                               "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_eu-west-1"
                           ]
                       },
                       "Action": "sts:AssumeRole",
                       "Condition": {
                           "StringEquals": {
                               // Optional. Replace with a UUID v4 for additional security. If you use an external ID, you must provide it to Pinecone when adding an API key.
                               "sts:ExternalId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
                           }
                       }
                   }
               ]
           }
           ```
         </Accordion>

         <Accordion title="Explicit regions + no external ID">
           ```json JSON theme={null}
           {
               "Version": "2012-10-17",
               "Statement": [
                   {
                       "Sid": "AllowPineconeToAssumeIntoRoleFromExplicitRegions",
                       "Effect": "Allow",
                       "Principal": {
                           "AWS": [
                               // Explicit role per Pinecone region. Replace XXXXXXXXXXXX with Pinecone's AWS account number.
                               "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_us-east-1",
                               "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_us-west-2",
                               "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_eu-west-1"
                           ]
                       },
                       "Action": "sts:AssumeRole"
                   }
               ]
           }
           ```
         </Accordion>

         <Accordion title="All regions + external ID">
           ```json JSON theme={null}
           {
               "Version": "2012-10-17",
               "Statement": [
                   {
                       "Sid": "AllowPineconeToAssumeIntoRoleFromAllRegions",
                       "Effect": "Allow",
                       "Principal": {
                           "AWS": "*"
                       },
                       "Action": "sts:AssumeRole",
                       "Condition": {
                           "StringEquals": {
                               // Optional. Replace with a UUID v4 for additional security. If you use an external ID, you must provide it to Pinecone when adding an API key.
                               "sts:ExternalId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
                           },
                           "StringLike": {
                               // Replace XXXXXXXXXXXX with Pinecone's AWS account number.
                               "aws:PrincipalArn": "arn:aws:iam::XXXXXXXXXXXX:role/pinecone_cmek_access_*"
                           }
                       }
                   }
               ]
           }
           ```
         </Accordion>
       </AccordionGroup>

       <Note>
         Replace `XXXXXXXXXXXX` with Pinecone's AWS account number, which can be found by going to [**Manage > CMEK**](https://app.pinecone.io/organizations/-/projects/-/cmek-encryption) in the Pinecone console and clicking **Add CMEK**.
       </Note>

    6. Click **Next**.

    7. Keep the default permissions as is and click **Next**.

    8. Enter a **Role name** and click **Create role**.

    9. Copy the **Role ARN** (e.g., `arn:aws:iam::XXXXXX:role/YYYYYY`). This will be used to [create a CMEK-enabled project](#3-create-a-cmek-enabled-project).
  </Tab>

  <Tab title="Grant access to keys outside your account">
    1. Open the [Amazon Identity and Access Management (IAM) console](https://console.aws.amazon.com/iam/).

    2. In the navigation pane, click **Roles**.

    3. Click **Create role**.

    4. In the **Trusted entity type** section, select **Custom trust policy**.

    5. In the **Custom trust policy** section, enter the following JSON:

       ```json JSON theme={null}
       {
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Sid": "VisualEditor0",
                   "Effect": "Allow",
                   "Action": [
                       "kms:Decrypt",
                       "kms:Encrypt"
                   ],
                   "Resource": "arn:aws:kms:*:XXXXXX:key/*"
               }
           ]
       }
       ```

       * Replace `XXXXXX` with the account ID of the customer who owns the key.
       * Add a `Statement` array for each customer account ID.

    6. Click **Next**.

    7. Keep the default permissions as is and click **Next**.

    8. Enter a **Role name** and click **Create role**.

    9. Copy the **Role ARN** (e.g., `arn:aws:iam::XXXXXX:role/YYYYYY`). This will be used to [create a CMEK-enabled project](#3-create-a-cmek-enabled-project).
  </Tab>
</Tabs>

### 2. Create an AWS KMS key

In the [AWS console](https://console.aws.amazon.com/console/home), create the KMS key that Pinecone will use to encrypt your data:

1. Open the [Amazon Key Management Service (KMS) console](https://console.aws.amazon.com/kms/home).

2. In the navigation pane, click **Customer managed keys**.

3. Click **Create key**.

4. In the **Key type** section, select **Symmetric**.

5. In the **Key usage** section, select **Encrypt and decrypt**.

6. Under **Advanced options > Key material origin**, select **KMS**.

7. In the **Regionality** section, select **Single-Region key**.

   <Note>
     You can create a multi-regional key to safeguard against data loss in case of regional failure. However, Pinecone only accepts one Key ARN per project. If you set a multi-regional key and need to change the Key ARN to switch region, please [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) for help.
   </Note>

8. Click **Next**.

9. Enter an **Alias** and click **Next**.

10. Keep the default administrators as is and click **Next**.

11. Select the [role you created](#1-create-a-role) from the **Key users** list and click **Next**.

12. Click **Finish**.

13. Copy the **Key ARN** (e.g., `arn:aws:kms:us-east-1:XXXXXXX:key/YYYYYYY`). This will be used to [create a CMEK-enabled project](#create-a-cmek-enabled-project).

### 3. Create a CMEK-enabled project

Once your [role and key is configured](#set-up-cmek-using-aws-kms), you can create a CMEK-enabled project using the Pinecone console:

1. Go to [**Settings > Organization settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).

2. Click **+Create project**.

3. Enter a **Name**.

4. Select **Encrypt with Customer Managed Encryption Key**.

5. Click **Create project**.

6. Copy and save the generated API key in a secure place for future use.

   <Warning>
     You will not be able to see the API key again after you close the dialog.
   </Warning>

7. Click **Close**.


## Add a key

To start encrypting your data with a customer-managed key, you need to add the key to the [CMEK-enabled project](#3-create-a-cmek-enabled-project) using the Pinecone console:

1. Go to [**Manage > CMEK**](https://app.pinecone.io/organizations/-/projects/-/cmek-encryption) for the CMEK-enabled project.

2. Click **Add CMEK**.

   <Warning>
     You can only add one key per project, and you cannot change the key in Pinecone once it is set.
   </Warning>

3. Enter a **Key name**.

4. Enter the **Role ARN** for the [role you created](#1-create-a-role).

5. Enter a **Key ARN** for the [key you created](#2-create-a-aws-kms-key).

6. If you [created a role](#1-create-a-role) with an external ID, enter the **External ID**. If not, leave this field blank.

7. Click **Create key**.


## Delete a key

Before a key can be deleted from a project, all indexes in the project must be deleted. Then, you can delete the key using the Pinecone console:

1. Go to the [Manage > CMEK tab](https://app.pinecone.io/organizations/-/projects/-/cmek-encryption) for the project in which the key was created.
2. For the key you want to delete, click the **ellipsis (...) menu > Delete**.
3. Enter the key name to confirm deletion.
4. Click **Delete key**.


## Limitations

* CMEK can be enabled for serverless indexes in AWS regions only.
* [Backups](/guides/manage-data/back-up-an-index) are unavailable for indexes created in a CMEK-enabled project.
* You cannot change a key once it is set.
* You can add only one key per project.



# Configure SSO with Okta
Source: https://docs.pinecone.io/guides/production/configure-single-sign-on/okta

Configure SAML SSO with Okta for enterprise.

This page describes how to set up Pinecone with Okta as the single sign-on (SSO) provider. These instructions can be adapted for any provider with SAML 2.0 support.

<Note>SSO is available on Standard and Enterprise plans.</Note>


## Before you begin

This page assumes you have the following:

* Access to your organization's [Pinecone console](https://login.pinecone.io) as an [organization owner](/guides/organizations/understanding-organizations#organization-owners).
* Access to your organization's [Okta Admin console](https://login.okta.com/).


## 1. Start SSO setup in Pinecone

First, start setting up SSO in Pinecone. In this step, you'll capture a couple values necessary for configuring Okta in [Step 2](#2-create-an-app-integration-in-okta).

1. In the Pinecone console, go to [**Settings > Manage**](https://app.pinecone.io/organizations/-/settings/manage).
2. In the **Single Sign-On** section, click **Enable SSO**.
3. In the **Setup SSO** dialog, copy the **Entity ID** and the **Assertion Consumer Service (ACS) URL**. You'll need these values in [Step 2](#2-create-an-app-integration-in-okta).
4. Click **Next**.

Keep this window or browser tab open. You'll come back to it in [Step 4](#4-complete-sso-setup-in-pinecone).


## 2. Create an app integration in Okta

In [Okta](https://login.okta.com/), follow these steps to create and configure a Pinecone app integration:

1. If you're not already on the Okta Admin console, navigate there by clicking the **Admin** button.

2. Navigate to **Applications > Applications**.

3. Click **Create App Integration**.

4. Select **SAML 2.0**.

5. Click **Next**.

6. Enter the **General Settings**:

   * **App name**: `Pinecone`
   * **App logo**: (optional)
   * **App visibility**: Set according to your organization's needs.

7. Click **Next**.

8. For **SAML Settings**, enter values you copied in [Step 1](#1-start-sso-setup-in-pinecone):

   * **Single sign-on URL**: Your **Assertion Consumer Service (ACS) URL**
   * **Audience URI (SP Entity ID)**: Your **Entity ID**
   * **Name ID format**: `EmailAddress`
   * **Application username**: `Okta username`
   * **Update application username on**: `Create and update`

9. In the **Attribute Statements** section, create the following attribute:

   * **Name**: `email`
   * **Value**: `user.email`

10. Click **Next**.

11. Click **Finish**.


## 3. Get the sign on URL and certificate from Okta

Next, in Okta, get the URL and certificate for the Pinecone application you just created. You'll use these in [Step 4](#4-complete-sso-setup-in-pinecone).

1. In the Okta Admin console, navigate to **Applications > Pinecone > Sign On**. If you're continuing from the previous step, you should already be on the right page.
2. In the **SAML 2.0** section, expand **More details**.
3. Copy the **Sign on URL**.
4. Download the **Signing Certificate**.

   <Warning>
     Download the certificate, don't copy it. The downloaded version contains necessary `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
   </Warning>


## 4. Complete SSO setup in Pinecone

In the browser tab or window you kept open in [Step 1](#1-start-sso-setup-in-pinecone), complete the SSO setup in Pinecone:

1. In the **SSO Setup** window, enter the following values:

   * **Login URL**: The URL copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).
   * **Email domain**: Your company's email domain. To target multiple domains, enter each domain separated by a comma.
   * **Certificate**: The contents of the certificate file you copied in [Step 3](#3-get-the-sign-on-url-and-certificate-from-okta).

     <Warning>
       When pasting the certificate, be sure to include the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines.
     </Warning>

2. Choose whether or not to **Enforce SSO for all users**.

   * If enabled, all members of your organization must use SSO to log in to Pinecone.
   * If disabled, members can choose to log in with SSO or with their Pinecone credentials.

3. Click **Next**.

4. Select a **Default role** for all users who log in with SSO. You can change user roles later.

Okta is now ready to be used for single sign-on. Follow the [Okta docs](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-main.htm) to learn how to add users and groups.



# Configure Private Endpoints for AWS PrivateLink
Source: https://docs.pinecone.io/guides/production/connect-to-aws-privatelink

Secure Pinecone with private VPC endpoints.

This page describes how to create and use [Private Endpoints](/guides/production/security-overview#private-endpoints-for-aws-privatelink) to connect AWS PrivateLink to Pinecone while keeping your VPC private from the public internet.


## Use Private Endpoints to connect to PrivateLink

### Before you begin

The following steps assume you have:

* Access to the [AWS console](https://console.aws.amazon.com/console/home).

* [Created an Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources) in the same AWS [region](/guides/index-data/create-an-index#cloud-regions) as the index you want to connect to. You can optionally enable DNS hostnames and resolution, if you want your VPC to automatically discover the DNS CNAME for your PrivateLink and do not want configure a CNAME.

  * To [configure the routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) yourself, use one of Pinecone's DNS entry for the corresponding region:

  | Index region              | Pinecone DNS entry                     |
  | ------------------------- | -------------------------------------- |
  | `us-east-1` (N. Virginia) | `*.private.aped-4627-b74a.pinecone.io` |
  | `us-west-2` (Oregon)      | `*.private.apw5-4e34-81fa.pinecone.io` |
  | `eu-west-1` (Ireland)     | `*.private.apu-57e2-42f6.pinecone.io`  |

* A [Pinecone Enterprise plan](https://www.pinecone.io/pricing/).

* [Created a serverless index](/guides/index-data/create-an-index#create-a-serverless-index) in the same AWS [region](/guides/index-data/create-an-index#cloud-regions) as your Amazon VPC.

<Note>
  Private Endpoints are configured at the project-level and you can add up to 10 endpoints per project. If you have multiple projects in your organization, Private Endpoints need to be set up separately for each.
</Note>

### 1. Create an Amazon VPC endpoint

In the [AWS console](https://console.aws.amazon.com/console/home):

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/).

2. In the navigation pane, click **Endpoint**.

3. Click **Create endpoint**.

4. For **Service category**, select **Other endpoint services**.

5. In **Service settings**, enter the **Service name**, based on the region your Pinecone index is in:
   | Index region              | Service name                                              |
   | ------------------------- | --------------------------------------------------------- |
   | `us-east-1` (N. Virginia) | `com.amazonaws.vpce.us-east-1.vpce-svc-05ef6f1f0b9130b54` |
   | `us-west-2` (Oregon)      | `com.amazonaws.vpce.us-west-2.vpce-svc-04ecb9a0e0d5aab01` |
   | `eu-west-1` (Ireland)     | `com.amazonaws.vpce.eu-west-1.vpce-svc-03c6b7e17ff02a70f` |

6. Click **Verify service**.

7. Select the **VPC** to host the endpoint.

8. (Optional) In **Additional settings**, **Enable DNS name**.
   The enables you to access our service with the DNS name we configure. An additional CNAME record is needed if you disable this option.

9. Select the **Subnets** and **Subnet ID** for the endpoint.

10. Select the **Security groups** to apply to the endpoint.

11. Click **Create endpoint**.

12. Copy the **VPC endpoint ID** (e.g., `vpce-XXXXXXX`).
    This will be used to [add a Private Endpoint in Pinecone](#2-add-a-private-endpoint-in-pinecone).

### 2. Add a Private Endpoint in Pinecone

To add a Private Endpoint using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
3. Click **Add a connection**.
4. Select your VPC region.
   Only indexes in the selected region in this project will be affected.
5. Click **Next**.
6. Enter the AWS VPC endpoint ID you copied in the [section above](#create-an-amazon-vpc-endpoint).
7. Click **Next**.
8. (optional) To **enable VPC endpoint access only**, turn the toggle on.
   This can also be enabled later. For more information, see [Manage internet access to your project](#optional-manage-internet-access-to-your-project).
9. Click **Finish setup**.

<Note>
  Private Endpoints only affect [data plane](/reference/api/latest/data-plane) access. [Control plane](/reference/api/latest/control-plane) access will continue over the public internet.
</Note>


## Read and write data

Once your private endpoint is configured, you can run data operations against an index as usual, but you must target the index using its private endpoint URL. The only difference in the URL is that `.svc.` is changed to `.svc.private.`.

You can get the private endpoint URL for an index from the Pinecone console or API.

<Tabs>
  <Tab title="Console">
    To get the private endpoint URL for an index from the Pinecone console:

    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select the project containing the index.
    3. Select the index.
    4. Copy the URL under **PRIVATE ENDPOINT**.
  </Tab>

  <Tab title="API">
    To get the private endpoint URL for an index from the API, use the [`describe_index`](/reference/api/latest/control-plane/describe_index) operation, which returns the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone';

      const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

      await pc.describeIndex('docs-example');
      ```

      ```go Go theme={null}
      package main

      import (
          "context"
          "encoding/json"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func prettifyStruct(obj interface{}) string {
          bytes, _ := json.MarshalIndent(obj, "", "  ")
          return string(bytes)
      }

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          idx, err := pc.DescribeIndex(ctx, "docs-example")
          if err != nil {
              log.Fatalf("Failed to describe index \"%v\": %v", idx.Name, err)
          } else {
              fmt.Printf("index: %v\n", prettifyStruct(idx))
          }
      }
      ```

      ```bash curl theme={null}
      PINECONE_API_KEY="YOUR_API_KEY"

      curl -i -X GET "https://api.pinecone.io/indexes/docs-example" \
          -H "Api-Key: YOUR_API_KEY" \
          -H "X-Pinecone-API-Version: 2025-04"
      ```
    </CodeGroup>

    The response includes the private endpoint URL as the `private_host` value:

    <CodeGroup>
      ```json JavaScript {6} theme={null}
      {
        name: 'docs-example',
        dimension: 1536,
        metric: 'cosine',
        host: 'docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io',
        privateHost: 'docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io',
        deletionProtection: 'disabled',
        tags: { environment: 'production' },
        embed: undefined,
        spec: {
          byoc: undefined,
          pod: undefined,
          serverless: { cloud: 'aws', region: 'us-east-1' }
        },
        status: { ready: true, state: 'Ready' },
        vectorType: 'dense'
      }
      ```

      ```go Go {5} theme={null}
      index: {
        "name": "docs-example",
        "dimension": 1536,
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "metric": "cosine",
        "deletion_protection": "disabled",
        "spec": {
          "serverless": {
            "cloud": "aws",
            "region": "us-east-1"
          }
        },
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "tags": {
          "environment": "production"
        }
      }
      ```

      ```json curl {12} theme={null}
      {
        "id": "025117b3-e683-423c-b2d1-6d30fbe5027f",
        "vector_type": "dense",
        "name": "docs-example",
        "metric": "cosine",
        "dimension": 1536,
        "status": {
          "ready": true,
          "state": "Ready"
        },
        "host": "docs-example-jl7boae.svc.aped-4627-b74a.pinecone.io",
        "private_host": "docs-example-jl7boae.svc.private.aped-4627-b74a.pinecone.io",
        "spec": {
          "serverless": {
            "region": "us-east-1",
            "cloud": "aws"
          }
        },
        "deletion_protection": "disabled",
        "tags": {
          "environment": "production"
        }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Note>
  If you run data operations against an index from outside the Private Endpoint, you will get an `Unauthorized` response.
</Note>


## Manage internet access to your project

Once your Private Endpoint is configured, you can turn off internet access to your project. To enable VPC endpoint access only:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select your project.
3. Go to **Network > Access**.
4. Turn the **VPC endpoint access only** toggle on.
   This will turn off internet access to the project. This can be turned off at any point.

   <Warning>
     This access control is set at the *project-level* and can unintentionally affect Pinecone indexes that communicate via the internet in the same project. Only indexes communicating through Private Endpoints will continue to work.
   </Warning>


## Manage Private Endpoints

In addition to [creating Private Endpoints](#2-add-a-private-endpoint-in-pinecone), you can also:

* [View Private Endpoints](#view-private-endpoints)
* [Delete a Private Endpoint](#delete-a-private-endpoint)

### View Private Endpoints

To view Private Endpoints using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
   A list of Private Endpoints displays with the associated **VPC ID** and **Cloud** provider.

### Delete a Private Endpoint

To delete a Private Endpoint using the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to **Manage > Network**.
3. For the Private Endpoint you want to delete, click the *...* (Actions) icon.
4. Click **Delete**.
5. Enter the endpoint name.
6. Click **Delete Endpoint**.



# Data deletion on Pinecone
Source: https://docs.pinecone.io/guides/production/data-deletion

Understand Pinecone's secure data deletion process.

Pinecone follows a secure process to ensure that customer data is permanently deleted from our system. This page gives an overview of the process.

As defined in the [Master Subscription Agreement](https://www.pinecone.io/legal/master-subscription-agreement/), customer data is data that you provide to Pinecone through the services of the Pinecone system, or such data provided on your behalf by connected systems. This includes objects such as [records](/guides/get-started/concepts#record), [indexes](/guides/get-started/concepts#index), [backups](/guides/get-started/concepts#backup-or-collection), [projects](/guides/get-started/concepts#project), [API keys](/guides/get-started/concepts#api-key), [users](/guides/get-started/concepts#user), [assistants](/guides/get-started/concepts#pinecone-assistant), and [organizations](/guides/get-started/concepts#organization).


## Deletion request

The deletion of customer data begins when you initiate a deletion request through the Pinecone API, console, or a connected service. A deletion request can delete a single resource, such as a record, or can delete a resource and all its dependent resources, such as an index and all its records.

Deletion of your customer data also occurs automatically when you end your relationship with Pinecone.


## Soft deletion

After you initiate a deletion request, Pinecone marks the data for deletion. The data is not immediately removed from the system. Instead, Pinecone retains the data for a maximum of 90 days. During this period, the data is not accessible to you or any other user.


## Permanent deletion

Before the end of the 90-day retention window, Pinecone permanently deletes the data from its system. Once the data is permanently deleted, it is no longer recoverable.

<Note>
  Pinecone creates an [audit log](/guides/production/security-overview#audit-logs) of user, service account, and API events. Events are captured within two hours of occurrence and are retained for 90 days, after which they are permanently deleted.
</Note>


## See also

* [Delete records](/guides/manage-data/delete-data)
* [Delete an index](/guides/manage-data/manage-indexes#delete-an-index)
* [Delete a project](/guides/projects/manage-projects#delete-a-project)
* [Delete an API key](/guides/projects/manage-api-keys#delete-an-api-key)
* [Delete a user](/guides/projects/manage-project-members#remove-members)
* [Delete an organization](/troubleshooting/delete-your-organization)
* [Master Subscription Agreement](https://www.pinecone.io/legal/master-subscription-agreement/)



# Error handling
Source: https://docs.pinecone.io/guides/production/error-handling

Handle errors with retry logic and best practices.


## Understand error types

Pinecone uses [conventional HTTP response codes](/reference/api/errors) to indicate the success or failure of API requests:

* **2xx codes** indicate success
* **4xx codes** indicate client errors (issues with your request)
* **5xx codes** indicate server errors (issues with Pinecone's servers)

### Client errors (4xx)

Client errors indicate problems with your request. These errors typically require changes to your code or configuration:

* **400 - Invalid Argument**: Your request contains invalid parameters. Check your request format and parameters.
* **401 - Unauthenticated**: Your API key is missing or invalid. Verify your [API key](/guides/projects/manage-api-keys).
* **402 - Payment Required**: Your account has a payment issue. Check your billing status in the [console](https://app.pinecone.io).
* **403 - Forbidden**: You've exceeded a [quota](/reference/api/database-limits#object-limits) or hit [deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).
* **404 - Not Found**: The requested resource doesn't exist. Verify the resource name and that it hasn't been deleted.
* **409 - Already Exists**: You're trying to create a resource that already exists.
* **429 - Too Many Requests**: You're being [rate-limited](/reference/api/database-limits#rate-limits). Implement [backoff and retry logic](#implement-retry-logic).

### Server errors (5xx)

Server errors indicate temporary issues with Pinecone's infrastructure:

* **500 - Unknown**: An internal server error occurred.
* **502 - Bad Gateway**: The API gateway received an invalid response from a backend service.
* **503 - Unavailable**: The service is currently unavailable.
* **504 - Gateway Timeout**: The API gateway did not receive a timely response from the backend server. This can occur due to slow requests or backend processing delays.

**Best practice for 5xx errors**: [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic). These errors are typically transient.


## Capture errors

Each SDK provides error handling mechanisms specific to the language:

### Python SDK

The Python SDK raises exceptions that you can catch and handle:

```python  theme={null}
from pinecone import Pinecone
from pinecone.exceptions import PineconeException

pc = Pinecone(api_key="YOUR_API_KEY")
index = pc.Index("your-index")

try:
    index.upsert(
        vectors=[
            {"id": "vec1", "values": [0.1, 0.2, 0.3]}
        ]
    )
except PineconeException as e:
    # Handle Pinecone-specific errors
    print(f"Pinecone error: {e}")
except Exception as e:
    # Handle other errors
    print(f"Unexpected error: {e}")
```

See the [Python SDK documentation](https://sdk.pinecone.io/python/) for more details on exception handling.

### Node.js SDK

The Node.js SDK uses standard JavaScript error handling:

```javascript  theme={null}
const { Pinecone } = require('@pinecone-database/pinecone');

const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

try {
  const index = pc.index('your-index');
  await index.upsert([
    { id: 'vec1', values: [0.1, 0.2, 0.3] }
  ]);
} catch (error) {
  console.error('Error upserting data:', error);
  // Handle the error appropriately
}
```

See the [Node.js SDK documentation](https://sdk.pinecone.io/typescript/) for more information.

### Other SDKs

For SDK-specific error handling patterns, see the documentation for your language:

* [Go SDK](/reference/go-sdk)
* [Java SDK](/reference/java-sdk)
* [.NET SDK](/reference/dotnet-sdk)


## Implement retry logic

For transient errors (5xx codes and 429 rate limiting), implement retry logic. Start with basic retries for simple use cases, or use exponential backoff for production systems.

### Basic retry logic

For simple use cases, start with a basic retry loop with fixed delays:

```python  theme={null}
import time
from pinecone.exceptions import PineconeException

def simple_retry(func, max_retries=3, delay=2):
    """
    Retry a function with a fixed delay between attempts.

    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts
        delay: Delay in seconds between retries
    """
    for attempt in range(max_retries):
        try:
            return func()
        except PineconeException as e:
            if attempt == max_retries - 1:
                raise  # Last attempt, re-raise the exception

            print(f"Attempt {attempt + 1} failed, retrying in {delay}s...")
            time.sleep(delay)


# Usage
try:
    simple_retry(lambda: index.upsert(vectors))
except Exception as e:
    print(f"Failed after {max_retries} attempts: {e}")
```

This basic approach works well for occasional transient errors, but for production systems with higher traffic, use exponential backoff instead.

### Exponential backoff

Exponential backoff progressively increases the wait time between retries to avoid overwhelming the service:

```python  theme={null}
import time
import random

def exponential_backoff_retry(func, max_retries=5, base_delay=1, max_delay=60):
    """
    Retry a function with exponential backoff.

    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay between retries
    """
    for attempt in range(max_retries):
        try:
            return func()
        except PineconeException as e:
            if attempt == max_retries - 1:
                raise  # Last attempt, re-raise the exception

            # Get status code if available
            status_code = getattr(e, 'status', None)

            # Only retry on 5xx errors or 429 (rate limiting)
            if status_code and (status_code >= 500 or status_code == 429):
                # Calculate delay with exponential backoff and jitter
                delay = min(base_delay * (2 ** attempt), max_delay)
                jitter = random.uniform(0, delay * 0.1)  # Add 10% jitter
                wait_time = delay + jitter

                print(f"Retry attempt {attempt + 1}/{max_retries} after {wait_time:.2f}s")
                time.sleep(wait_time)
            else:
                # Don't retry client errors (4xx except 429)
                raise


# Usage
try:
    exponential_backoff_retry(lambda: index.upsert(vectors))
except Exception as e:
    print(f"Failed after retries: {e}")
```

### Key retry principles

1. **Add jitter**: Random variation in retry timing helps avoid thundering herd problems.
2. **Set max retries**: Prevent infinite retry loops.
3. **Cap delay time**: Don't wait indefinitely between retries.
4. **Don't retry client errors**: 4xx errors (except 429) won't resolve with retries.
5. **Log retry attempts**: Track retry behavior for monitoring and debugging.


## Handle rate limits (429)

When you receive a 429 error, you're being rate-limited. See [Rate limits](/reference/api/database-limits#rate-limits) for current limits.

Rate limits help protect your applications and maintain the health of the serverless infrastructure. **Most limits can be adjusted upon request**—if you need higher limits to scale, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

**Best practices**:

* Implement exponential backoff as described above.
* Proactively [monitor request metrics](/guides/production/monitoring) and reduce the request rate if you're approaching limits.
* Use [batching](/guides/index-data/upsert-data#upsert-in-batches) to reduce the number of requests.
* For high-throughput needs, see [Increase throughput](/guides/optimize/increase-throughput).


## Getting support

If you've implemented error handling and retry logic but continue to experience issues:

1. Review [How to work with Support](/troubleshooting/how-to-work-with-support) for best practices.
2. Gather the following information:
   * Index name and project name
   * Error messages and stack traces
   * Timestamp of errors
   * Request/response examples (without sensitive data)
   * Whether the issue is reproducible
3. [Contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).

Ensure your [plan tier](https://www.pinecone.io/pricing/) provides the support SLA you need for production workloads.


## See also

* [API error codes](/reference/api/errors)
* [Database limits](/reference/api/database-limits)
* [Assistant limits](/reference/api/assistant/assistant-limits)
* [Monitoring](/guides/production/monitoring)
* [Production checklist](/guides/production/production-checklist)



# Monitor performance
Source: https://docs.pinecone.io/guides/production/monitoring

Monitor performance metrics in the Pinecone console or with Prometheus or Datadog.

Pinecone generates time-series performance metrics for each Pinecone index. You can monitor these metrics directly in the Pinecone console or with tools like Prometheus or Datadog.


## Monitor in the Pinecone Console

To view performance metrics in the Pinecone console:

1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
2. Select the project containing the index you want to monitor.
3. Go to **Database > Indexes**.
4. Select the index.
5. Go to the **Metrics** tab.


## Monitor with Datadog

To monitor Pinecone with Datadog, use Datadog's [Pinecone integration](/integrations/datadog).

<Note>
  This feature is available on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>


## Monitor with Prometheus

<Note>
  This feature is available on [Standard and  Enterprise plans](https://www.pinecone.io/pricing/). When using [Bring Your Own Cloud](/guides/production/bring-your-own-cloud), you must configure Prometheus monitoring within your VPC.
</Note>

To monitor all serverless indexes in a project, insert the following snippet into the [`scrape_configs`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) section of your `prometheus.yml` file and update it with values for your Prometheus integration:

<Note>
  This method uses [HTTP service discovery](https://prometheus.io/docs/prometheus/latest/http_sd/) to automatically discover and target all serverless indexes across all regions in a project.
</Note>

```YAML  theme={null}
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'pinecone-serverless-metrics'
    http_sd_configs:
      - url: https://api.pinecone.io/prometheus/projects/PROJECT_ID/metrics/discovery
        refresh_interval: 1m
        authorization:
          type: Bearer
          credentials: API_KEY
    authorization:
      type: Bearer
      credentials: API_KEY
```

* Replace `PROJECT_ID` with the unique ID of the project you want to monitor. You can [find the project ID](/guides/projects/understanding-projects#project-ids) in the Pinecone console.

* Replace both instances of `API_KEY` with an API key for the project you want to monitor. The first instance is for service discovery, and the second instance is for the discovered targets. If necessary, you can [create an new API key](/guides/projects/manage-api-keys) in the Pinecone console.

For more configuration details, see the [Prometheus docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

### Available metrics

The following metrics are available when you integrate Pinecone with Prometheus:

| Name                                   | Type    | Description                                                                                                    |
| :------------------------------------- | :------ | :------------------------------------------------------------------------------------------------------------- |
| `pinecone_db_record_total`             | gauge   | The total number of records in the index.                                                                      |
| `pinecone_db_op_upsert_total`          | counter | The number of [upsert](/guides/index-data/upsert-data) requests made to an index.                              |
| `pinecone_db_op_upsert_duration_total` | counter | The total time taken processing upsert requests for an index in milliseconds.                                  |
| `pinecone_db_op_query_total`           | counter | The number of [query](/guides/search/search-overview) requests made to an index.                               |
| `pinecone_db_op_query_duration_total`  | counter | The total time taken processing [query](/guides/search/search-overview) requests for an index in milliseconds. |
| `pinecone_db_op_fetch_total`           | counter | The number of [fetch](/guides/manage-data/fetch-data) requests made to an index.                               |
| `pinecone_db_op_fetch_duration_total`  | counter | The total time taken processing fetch requests for an index in milliseconds.                                   |
| `pinecone_db_op_update_total`          | counter | The number of [update](/guides/manage-data/update-data) requests made to an index.                             |
| `pinecone_db_op_update_duration_total` | counter | The total time taken processing update requests for an index in milliseconds.                                  |
| `pinecone_db_op_delete_total`          | counter | The number of [delete](/guides/manage-data/delete-data) requests made to an index.                             |
| `pinecone_db_op_delete_duration_total` | counter | The total time taken processing delete requests for an index in milliseconds.                                  |
| `pinecone_db_write_unit_total`         | counter | The total number of [write units](/guides/manage-cost/understanding-cost#write-units) consumed by an index.    |
| `pinecone_db_read_unit_total`          | counter | The total number of [read units](/guides/manage-cost/understanding-cost#read-units) consumed by an index.      |
| `pinecone_db_storage_size_bytes`       | gauge   | The total size of the index in bytes.                                                                          |

### Metric labels

Each metric contains the following labels:

| Label           | Description                                                  |
| :-------------- | :----------------------------------------------------------- |
| `index_name`    | Name of the index to which the metric applies.               |
| `cloud`         | Cloud where the index is deployed: `aws`, `gcp`, or `azure`. |
| `region`        | Region where the index is deployed.                          |
| `capacity_mode` | Type of index: `serverless` or `byoc`.                       |

### Example queries

Return the total number of records per index:

```shell  theme={null}
sum by (index_name) (pinecone_db_record_total)
```

Return the total number of records in Pinecone index `docs-example`:

```shell  theme={null}
pinecone_db_record_total{index_name="docs-example"}
```

Return the total number of upsert requests per index:

```shell  theme={null}
sum by (index_name) (pinecone_db_op_upsert_total)
```

Return the average processing time in millisconds for upsert requests per index:

```shell  theme={null}
sum by (index_name) (pinecone_db_op_upsert_duration_total/pinecone_db_op_upsert_total) 
```

Return the total read units consumed per index:

```shell  theme={null}
sum by (index_name) (pinecone_db_read_unit_total)
```

Return the total write units consumed for the Pinecone index `docs-example`:

```shell  theme={null}
pinecone_db_write_unit_total{index_name="docs-example"}
```



# Production checklist
Source: https://docs.pinecone.io/guides/production/production-checklist

Prepare your indexes for production with best practices.

This page provides recommendations and best practices for preparing your Pinecone indexes for production, anticipating production issues, and enabling reliability and growth.


## Prepare your project structure

One of the first steps towards building a production-ready Pinecone index is configuring your project correctly.

* Consider [creating a separate project](/guides/projects/create-a-project) for your development and production indexes, to allow for testing changes to your index before deploying them to production.
* Ensure that you have properly [configured user access](/guides/projects/understanding-projects#project-roles) to the Pinecone console, so that only those users who need to access the production index can do so.
* Ensure that you have properly configured access through the API by [managing API keys](/guides/projects/manage-api-keys) and using API key permissions.

Consider how best to [manage the API keys](/guides/projects/manage-api-keys) associated with your production project. In order to [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.


## Enforce security

Use Pinecone's [security features](/guides/production/security-overview) to protect your production data:

* Data security
  * Private endpoints
  * Customer-managed encryption keys (CMEK)
* Authorization
  * API keys
  * Role-based access control (RBAC)
  * Organization single sign-on (SSO)
* Audit logs
* Bring your own cloud


## Design your indexes for scale

Follow these best practices when designing and populating your indexes:

* **Data ingestion**: For large datasets (10M+ records), [import from object storage](/guides/index-data/import-data) for the most efficient and cost-effective ingestion. For ongoing ingestion, [upsert in batches](/guides/index-data/upsert-data#upsert-in-batches) to optimize speed and efficiency. See the [data ingestion overview](/guides/index-data/data-ingestion-overview) for details.
* **Dimensionality**: Consider the dimensionality of your vectors. Higher dimensions can offer more accuracy but require more resources.
* **Data modeling**: Use [structured IDs](/guides/index-data/data-modeling#use-structured-ids) (e.g., `document_id#chunk_number`) for efficient operations. Design [metadata](/guides/index-data/data-modeling#include-metadata) to support filtering, linking related chunks, and traceability. See the [data modeling guide](/guides/index-data/data-modeling) for details.
* **Namespaces**: When indexing, try to [use namespaces to keep your data among tenants separate](/guides/index-data/implement-multitenancy), and do not use multiple indexes for this purpose. Namespaces are more efficient and more affordable in the long run.


## Understand database limits

Architect your application to work within Pinecone's [database limits](/reference/api/database-limits):

* **Rate limits**: Serverless indexes have per-second operation limits for queries, upserts, updates, and deletes. [Implement error handling with exponential backoff](/guides/production/error-handling) to handle rate limit errors gracefully.
* **Size limits**: Be aware of constraints on vector dimensionality, metadata size per record, record ID length, maximum `top_k` values, and query result sizes. Design your [data model](/guides/index-data/data-modeling) accordingly.
* **Index limits**: Plan for index capacity based on your [plan tier](https://www.pinecone.io/pricing/). Use [namespaces](/guides/index-data/implement-multitenancy) to partition data within indexes rather than creating multiple indexes.
* **Plan limits**: Starter plans have monthly read/write unit limits. Upgrade to Standard or Enterprise for unlimited read/write units and higher throughput needs.


## Test your query results

Before you move your index to production, make sure that your index is returning accurate results in the context of your application by [identifying the appropriate metrics](https://www.pinecone.io/learn/offline-evaluation/) for evaluating your results.


## Optimize performance

Before serving production workloads, optimize your Pinecone implementation:

* **Increase search relevance**: Use techniques like reranking, metadata filtering, hybrid search, and chunking strategies to improve result quality. See [increase search relevance](/guides/optimize/increase-relevance) for details.
* **Increase throughput**: Import from object storage, upsert in batches, use parallel operations, and leverage Python SDK optimizations like gRPC. See [increase throughput](/guides/optimize/increase-throughput) for details.
* **Decrease latency**: Use namespaces, filter by metadata, target indexes by host, reuse connections, and deploy in the same cloud region as your index. See [decrease latency](/guides/optimize/decrease-latency) for details.


## Backup up your indexes

In order to enable long-term retention, compliance archiving, and deployment of new indexes, consider backing up your production indexes by [creating a backup or collection](/guides/manage-data/back-up-an-index).


## Implement error handling

Prepare your application to handle errors gracefully:

* Implement [error handling and retry logic](/guides/production/error-handling) with exponential backoff
* Handle different error types appropriately (4xx vs 5xx)
* Monitor error rates and set up alerts
* Check [status.pinecone.io](https://status.pinecone.io) before escalating issues


## Configure monitoring

Prepare to [monitor the production performance and availability of your indexes](/guides/production/monitoring).


## Configure CI/CD

Use [Pinecone in CI/CD](/guides/production/automated-testing) to safely test changes before deploying them to production.


## Know how to get support

If you need help, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket), or talk to the [Pinecone community](https://www.pinecone.io/community/). Ensure that your [plan tier](https://www.pinecone.io/pricing/) matches the support and availability SLAs you need. This may require you to upgrade to Enterprise.



# Security overview
Source: https://docs.pinecone.io/guides/production/security-overview

Understand Pinecone's security features, including authentication, encryption, and audit logs.


## Access management

### API keys

Each Pinecone [project](/guides/projects/understanding-projects) has one or more [API keys](/guides/projects/manage-api-keys). In order to make calls to the Pinecone API, a user must provide a valid API key for the relevant Pinecone project.

You can [manage API key permissions](/guides/projects/manage-api-keys) in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/keys). The available permission roles are as follows:

#### General permissions

<Tabs>
  <Tab title="Pinecone console">
    | Role | Permissions                                     |
    | :--- | :---------------------------------------------- |
    | All  | Permissions to read and write all project data. |
  </Tab>

  <Tab title="API">
    | Role            | Permissions                                      |
    | :-------------- | :----------------------------------------------- |
    | `ProjectEditor` | Permissions to read  and write all project data. |
    | `ProjectViewer` | Permissions to read all project data.            |
  </Tab>
</Tabs>

#### Control plane permissions

<Tabs>
  <Tab title="Pinecone console">
    | Role      | Permissions                                                                                                 |
    | :-------- | :---------------------------------------------------------------------------------------------------------- |
    | ReadWrite | Permissions to list, describe, create, delete, and configure indexes, backups, collections, and assistants. |
    | ReadOnly  | Permissions to list and describe indexes, backups, collections, and assistants.                             |
    | None      | No control plane permissions.                                                                               |
  </Tab>

  <Tab title="API">
    | Role                 | Permissions                                                                                                 |
    | :------------------- | :---------------------------------------------------------------------------------------------------------- |
    | `ControlPlaneEditor` | Permissions to list, describe, create, delete, and configure indexes, backups, collections, and assistants. |
    | `ControlPlaneViewer` | Permissions to list and describe indexes, backups, collections, and assistants.                             |
    | None                 | No control plane permissions.                                                                               |
  </Tab>
</Tabs>

#### Data plane permissions

<Tabs>
  <Tab title="Pinecone console">
    | Role      | Permissions                                                                                                                                                                                                                                                                                                            |
    | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ReadWrite | <ul><li>Indexes: Permissions to query, import, fetch, add, update, and delete index data.</li><li>Pinecone Assistant: Permissions to add, list, view, and delete files; chat with an assistant, and evaluate responses.</li><li>Pinecone Inference: Permissions to generate embeddings and rerank documents.</li></ul> |
    | ReadOnly  | <ul><li>Indexes: Permissions to query, fetch, list ID, and view stats.</li><li>Pinecone Assistant: Permissions to list and view files, chat with an assistant, and evaluate responses.</li></ul>                                                                                                                       |
    | None      | No data plane permissions.                                                                                                                                                                                                                                                                                             |
  </Tab>

  <Tab title="API">
    | Role              | Permissions                                                                                                                                                                                                                                                                                                            |
    | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `DataPlaneEditor` | <ul><li>Indexes: Permissions to query, import, fetch, add, update, and delete index data.</li><li>Pinecone Assistant: Permissions to add, list, view, and delete files; chat with an assistant, and evaluate responses.</li><li>Pinecone Inference: Permissions to generate embeddings and rerank documents.</li></ul> |
    | `DataPlaneViewer` | <ul><li>Indexes: Permissions to query, fetch, list ID, and view stats.</li><li>Pinecone Assistant: Permissions to list and view files, chat with an assistant, and evaluate responses.</li></ul>                                                                                                                       |
    | None              | No data plane permissions.                                                                                                                                                                                                                                                                                             |
  </Tab>
</Tabs>

### Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can require that users from your domain sign in through SSO, and you can specify a default role for teammates when they sign up. SSO is available on Standard and Enterprise plans.

For more information, see [configure single sign on](/guides/production/configure-single-sign-on/okta).

### Role-based access controls (RBAC)

Pinecone uses role-based access controls (RBAC) to manage access to resources.

Service accounts, API keys, and users are all *principals*. A principal's access is determined by the *roles* assigned to it. Roles are assigned to a principal for a *resource*, either a project or an organization. The roles available to be assigned depend on the type of principal and resource.

#### Service account roles

A service account can be assigned roles for the organization it belongs to, and any projects within that organization. For more information, see [Organization roles](/guides/organizations/understanding-organizations#organization-roles) and [Project roles](/guides/projects/understanding-projects#project-roles).

#### API key roles

An API key can only be assigned permissions for the projects it belongs to. For more information, see [API keys](#api-keys).

#### User roles

A user can be assigned roles for each organization they belong to, and any projects within that organization. For more information, see [Organization roles](/guides/organizations/understanding-organizations#organization-roles) and [Project roles](/guides/projects/understanding-projects#project-roles).


## Compliance

<Note>
  To learn more about data privacy and compliance at Pinecone, visit the [Pinecone Trust and Security Center](https://security.pinecone.io/).
</Note>

### Audit logs

<Note>
  To enable and manage audit logs, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-roles). This feature is available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

[Audit logs](/guides/production/configure-audit-logs) provide a detailed record of user and API actions that occur within Pinecone.

Events are captured every 30 minutes and each log batch will be saved into its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled will be saved.

Audit log events adhere to a standard JSON schema and include the following fields:

```json JSON theme={null}
{
    "id": "00000000-0000-0000-0000-000000000000",
    "organization_id": "AA1bbbbCCdd2EEEe3FF",
    "organization_name": "example-org",
    "client": {
        "userAgent": "rawUserAgent"
    },
    "actor": {
        "principal_id": "00000000-0000-0000-0000-000000000000",
        "principal_name": "example@pinecone.io",
        "principal_type": "user", // user, api_key, service_account
        "display_name": "Example Person" // Only in case of user
    },
	"event": {
        "time": "2024-10-21T20:51:53.697Z",
        "action": "create",
        "resource_type": "index",
        "resource_id": "uuid",
        "resource_name": "docs-example",
        "outcome": {
            "result": "success",
            "reason": "", // Only displays for "result": "failure"
            "error_code": "", // Only displays for "result": "failure"
        },
        "parameters": { // Varies based on event
        }
	}
}
```

The following events are captured in the audit logs:

* [Organization events](#organization-events)
* [Project events](#project-events)
* [Index events](#index-events)
* [User and API key events](#user-and-api-key-events)
* [Security and governance events](#security-and-governance-events)

#### Organization events

| Action            | Query parameters                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| Rename org        | `event.action: update`, `event.resource_type: organization`, `event.resource_id: NEW_ORG_NAME`                 |
| Delete org        | `event.action: delete`, `event.resource_type: organization`, `event.resource_id: DELETED_ORG_NAME`             |
| Create org member | `event.action: create`, `event.resource_type: user`, `event.resource_id: [ARRAY_OF_USER_EMAILS]`               |
| Update org member | `event.action: update`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, role: NEW_ROLE }` |
| Delete org member | `event.action: delete`, `event.resource_type: user`, `event.resource_id: USER_EMAIL`                           |

#### Project events

| Action                     | Query parameters                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Create project             | `event.action: create`, `event.resource_type: project`, `event.resouce_id: PROJ_NAME`                              |
| Update project             | `event.action: update`, `event.resource_type: project`, `event.resource_id: PROJECT_NAME`                          |
| Delete project             | `event.action: delete`, `event.resource_type: project`, `event.resource_id: PROJECT_NAME`                          |
| Invite project member      | `event.action: create`, `event.resource_type: user`, `event.resource_id: [ARRAY_OF_USER_EMAILS]`                   |
| Update project member role | `event.action: update`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, role: NEW_ROLE }`     |
| Delete project member      | `event.action: delete`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, project: PROJ_NAME }` |

#### Index events

| Action        | Query parameters                                                                        |
| ------------- | --------------------------------------------------------------------------------------- |
| Create index  | `event.action: create`, `event.resource_type: index`, `event.resouce_id: INDEX_NAME`    |
| Update index  | `event.action: update`, `event.resource_type: index`, `event.resource_id: INDEX_NAME`   |
| Delete index  | `event.action: delete`, `event.resource_type: index`, `event.resource_id: INDEX_NAME`   |
| Create backup | `event.action: create`, `event.resource_type: backup`, `event.resource_id: BACKUP_NAME` |
| Delete backup | `event.action: delete`, `event.resource_type: backup`, `event.resource_id: BACKUP_NAME` |

#### User and API key events

| Action         | Query parameters                                                                        |
| -------------- | --------------------------------------------------------------------------------------- |
| User login     | `event.action: login`, `event.resource_type: user`, `event.resouce_id: USERNAME`        |
| Create API key | `event.action: create`, `event.resource_type: api-key`, `event.resource_id: API_KEY_ID` |
| Delete API key | `event.action: delete`, `event.resource_type: api-key`, `event.resource_id: API_KEY_ID` |

#### Security and governance events

| Action                  | Query parameters                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| Create Private Endpoint | `event.action: create`, `event.resource_type: private-endpoints`, `event.resource_id: PRIVATE_ENDPOINT_ID` |
| Delete Private Endpoint | `event.action: delete`, `event.resource_type: private-endpoints`, `event.resource_id: PRIVATE_ENDPOINT_ID` |


## Data protection

### Customer-managed encryption keys (CMEK)

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Data within a Pinecone project can be encrypted using [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek). This allows you to encrypt your data using keys that you manage in your cloud provider's key management system (KMS). Pinecone supports CMEK using Amazon Web Services (AWS) KMS.

### Backup and recovery

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

A backup is a static copy of your index that only consumes storage. It is a non-queryable representation of a set of records. You can [create a backup](/guides/manage-data/back-up-an-index) of an index, and you can [create a new index from a backup](/guides/manage-data/restore-an-index). This allows you to restore the index with the same or different configurations.

For more information, see [Understanding backups](/guides/manage-data/backups-overview).

### Encryption at rest

Pinecone encrypts stored data using the 256-bit Advanced Encryption Standard (AES-256) encryption algorithm.

### Encryption in transit

Pinecone uses standard protocols to encrypt user data in transit. Clients open HTTPS or gRPC connections to the Pinecone API; the Pinecone API gateway uses gRPC connections to user deployments in the cloud. These HTTPS and gRPC connections use the TLS 1.2 protocol with 256-bit Advanced Encryption Standard (AES-256) encryption.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6da22e2916d66cf6ff03a4cfd7623705" alt="Diagram showing encryption protocols for user data in transit" data-og-width="4134" width="4134" data-og-height="2570" height="2570" data-path="images/encryption-in-transit-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=25e7ed0c6201c3a1f706cedf0ed823a5 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=ec43f21a1237d675e4c382352b673457 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3bda7ada10d9343161aa691602ca5a5b 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=39f360b1bea6b4865d7508dc30741987 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=633cf84c092a6a9997b0b8e7daff1311 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0035c658e3af1f534e4281e92391716b 2500w" />

Traffic is also encrypted in transit between the Pinecone backend and cloud infrastructure services, such as S3 and GCS. For more information, see [Google Cloud Platform](https://cloud.google.com/docs/security/encryption-in-transit) and [AWS security documentation](https://docs.aws.amazon.com/AmazonS3/userguide/UsingEncryption.html).


## Network security

### Private Endpoints for AWS PrivateLink

Use [Private Endpoints to connect to Amazon Web Services (AWS) PrivateLink](/guides/production/connect-to-aws-privatelink). This establishes private connectivity between your Pinecone serverless indexes and supported AWS services while keeping your VPC private from the public internet.

<img src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=20101bb766f1d56a181a967adf4fa9f3" alt="PrivateLink diagram" data-og-width="2080" width="2080" data-og-height="1320" height="1320" data-path="images/privatelink.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=ef22970fb8b1e78abc8cc1f7a44f7ae7 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=9b8047e780915823c669cfa0080224c8 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=5013e59775dc67278bf574a9978883ec 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=679e8e0f2b26be94c7122de8745d6020 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=05278ed22e5e8a84b7a7e64369d92719 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/privatelink.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=64aa1106b31ff456753518e4389ea188 2500w" />

Private Endpoints are additive to other Pinecone security features: data is also [encrypted in transit](#encryption-in-transit), [encrypted at rest](#encryption-at-rest), and an [API key](#api-keys) is required to authenticate.

### Proxies

The following Pinecone SDKs support the use of proxies:

* [Python SDK](/reference/python-sdk#proxy-configuration)
* [Node.js SDK](/reference/node-sdk#proxy-configuration)



---
**Navigation:** [← Previous](./11-understanding-organizations.md) | [Index](./index.md) | [Next →](./13-create-a-project.md)
