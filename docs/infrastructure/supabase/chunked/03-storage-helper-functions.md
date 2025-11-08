**Navigation:** [← Previous](./02-metrics.md) | [Index](./index.md) | [Next →](./04-stop-and-remove-the-containers.md)

# Storage Helper Functions

Learn the storage schema

Supabase Storage provides SQL helper functions which you can use to write RLS policies.


### `storage.filename()`

Returns the name of a file. For example, if your file is stored in `public/subfolder/avatar.png` it would return: `'avatar.png'`

**Usage**

This example demonstrates how you would allow any user to download a file called `favicon.ico`:

```sql
create policy "Allow public downloads"
on storage.objects
for select
to public
using (
  storage.filename(name) = 'favicon.ico'
);
```


### `storage.foldername()`

Returns an array path, with all of the subfolders that a file belongs to. For example, if your file is stored in `public/subfolder/avatar.png` it would return: `[ 'public', 'subfolder' ]`

**Usage**

This example demonstrates how you would allow authenticated users to upload files to a folder called `private`:

```sql
create policy "Allow authenticated uploads"
on storage.objects
for insert
to authenticated
with check (
  (storage.foldername(name))[1] = 'private'
);
```


### `storage.extension()`

Returns the extension of a file. For example, if your file is stored in `public/subfolder/avatar.png` it would return: `'png'`

**Usage**

This example demonstrates how you would allow restrict uploads to only PNG files inside a bucket called `cats`:

```sql
create policy "Only allow PNG uploads"
on storage.objects
for insert
to authenticated
with check (
  bucket_id = 'cats' and storage.extension(name) = 'png'
);
```



# S3 Authentication

Learn about authenticating with Supabase Storage S3.

You have two options to authenticate with Supabase Storage S3:

*   Using the generated S3 access keys from your [project settings](/dashboard/project/_/storage/settings) (Intended exclusively for server-side use)
*   Using a Session Token, which will allow you to authenticate with a user JWT token and provide limited access via Row Level Security (RLS).



## S3 access keys

<Admonition type="danger" label="Keep these credentials secure">
  S3 access keys provide full access to all S3 operations across all buckets and bypass RLS policies. These are meant to be used only on the server.
</Admonition>

To authenticate with S3, generate a pair of credentials (Access Key ID and Secret Access Key), copy the endpoint and region from the [project settings page](/dashboard/project/_/storage/settings).

This is all the information you need to connect to Supabase Storage using any S3-compatible service.

<img alt="Storage S3 Access keys" src="/docs/img/storage/s3-credentials.png" width="100%" />

<Admonition type="note">
  For optimal performance when uploading large files you should always use the direct storage hostname. This provides several performance enhancements that will greatly improve performance when uploading large files.

  Instead of `https://project-id.supabase.co` use `https://project-id.storage.supabase.co`
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="javascript" queryGroup="language">
  <TabPanel id="javascript" label="aws-sdk-js">
    ```js
    import { S3Client } from '@aws-sdk/client-s3';

    const client = new S3Client({
      forcePathStyle: true,
      region: 'project_region',
      endpoint: 'https://project_ref.storage.supabase.co/storage/v1/s3',
      credentials: {
        accessKeyId: 'your_access_key_id',
        secretAccessKey: 'your_secret_access_key',
      }
    })
    ```
  </TabPanel>

  <TabPanel id="credentials" label="AWS Credentials">
    ```bash
    # ~/.aws/credentials

    [supabase]
    aws_access_key_id = your_access_key_id
    aws_secret_access_key = your_secret_access_key
    endpoint_url = https://project_ref.storage.supabase.co/storage/v1/s3
    region = project_region
    ```
  </TabPanel>
</Tabs>



## Session token

You can authenticate to Supabase S3 with a user JWT token to provide limited access via RLS to all S3 operations. This is useful when you want initialize the S3 client on the server scoped to a specific user, or use the S3 client directly from the client side.

All S3 operations performed with the Session Token are scoped to the authenticated user. RLS policies on the Storage Schema are respected.

To authenticate with S3 using a Session Token, use the following credentials:

*   access\_key\_id: `project_ref`
*   secret\_access\_key: `anonKey`
*   session\_token: `valid jwt token`

For example, using the `aws-sdk` library:

```javascript
import { S3Client } from '@aws-sdk/client-s3'

const {
  data: { session },
} = await supabase.auth.getSession()

const client = new S3Client({
  forcePathStyle: true,
  region: 'project_region',
  endpoint: 'https://project_ref.storage.supabase.co/storage/v1/s3',
  credentials: {
    accessKeyId: 'project_ref',
    secretAccessKey: 'anonKey',
    sessionToken: session.access_token,
  },
})
```



# S3 Compatibility

Learn about the compatibility of Supabase Storage with S3.

Supabase Storage is compatible with the S3 protocol. You can use any S3 client to interact with your Storage objects.

Storage supports [standard](/docs/guides/storage/uploads/standard-uploads), [resumable](/docs/guides/storage/uploads/resumable-uploads) and [S3 uploads](/docs/guides/storage/uploads/s3-uploads) and all these protocols are interoperable. You can upload a file with the S3 protocol and list it with the REST API or upload with Resumable uploads and list with S3.

Storage supports presigning a URL using query parameters. Specifically, Supabase Storage expects requests to be made using [AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html). To enable this feature, enable the S3 connection via S3 protocol in the Settings page for Supabase Storage.

<Admonition type="note">
  The S3 protocol is currently in Public Alpha. If you encounter any issues or have feature requests, [contact us](/dashboard/support/new).
</Admonition>



## Implemented endpoints

The most commonly used endpoints are implemented, and more will be added. Implemented S3 endpoints are marked with ✅ in the following tables.


### Bucket operations

{/* supa-mdx-lint-disable Rule003Spelling */}

| API Name                                                                                                                      | Feature                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ✅ [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)                                         |                                                                                                                                                                                                                                                                                                  |
| ✅ [HeadBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)                                           | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ✅ [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)                                       | ❌ ACL:<br /> ❌ x-amz-acl<br /> ❌ x-amz-grant-full-control<br /> ❌ x-amz-grant-read<br /> ❌ x-amz-grant-read-acp<br /> ❌ x-amz-grant-write<br /> ❌ x-amz-grant-write-acp<br />❌ Object Locking:<br /> ❌ x-amz-bucket-object-lock-enabled<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner |
| ✅ [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)                                       | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ✅ [GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html)                             | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ❌ [DeleteBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html)                               | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ❌ [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)                         | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ❌ [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html) | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ❌ [GetBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html)                                     | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                              |
| ❌ [PutBucketCors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html)                                     | ❌ Checksums:<br /> ❌ x-amz-sdk-checksum-algorithm<br /> ❌ x-amz-checksum-algorithm<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                      |
| ❌ [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html) | ❌ Checksums:<br /> ❌ x-amz-sdk-checksum-algorithm<br /> ❌ x-amz-checksum-algorithm<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                      |

{/* supa-mdx-lint-enable Rule003Spelling */}


### Object operations

{/* supa-mdx-lint-disable Rule003Spelling */}

| API Name                                                                                                      | Feature                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅ [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)                           | ✅ Conditional Operations:<br /> ✅ If-Match<br /> ✅ If-Modified-Since<br /> ✅ If-None-Match<br /> ✅ If-Unmodified-Since<br />✅ Range:<br /> ✅ Range (has no effect in HeadObject)<br /> ✅ partNumber<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ✅ [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)                         | Query Parameters:<br /> ✅ delimiter<br /> ✅ encoding-type<br /> ✅ marker<br /> ✅ max-keys<br /> ✅ prefix<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ✅ [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)                     | Query Parameters:<br /> ✅ list-type<br /> ✅ continuation-token<br /> ✅ delimiter<br /> ✅ encoding-type<br /> ✅ fetch-owner<br /> ✅ max-keys<br /> ✅ prefix<br /> ✅ start-after<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ✅ [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)                             | ✅ Conditional Operations:<br /> ✅ If-Match<br /> ✅ If-Modified-Since<br /> ✅ If-None-Match<br /> ✅ If-Unmodified-Since<br />✅ Range:<br /> ✅ Range<br /> ✅ PartNumber<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ✅ [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)                             | System Metadata:<br /> ✅ Content-Type<br /> ✅ Cache-Control<br /> ✅ Content-Disposition<br /> ✅ Content-Encoding<br /> ✅ Content-Language<br /> ✅ Expires<br /> ❌ Content-MD5<br />❌ Object Lifecycle<br />❌ Website:<br /> ❌ x-amz-website-redirect-location<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br /> ❌ x-amz-server-side-encryption-aws-kms-key-id<br /> ❌ x-amz-server-side-encryption-context<br /> ❌ x-amz-server-side-encryption-bucket-key-enabled<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Tagging:<br /> ❌ x-amz-tagging<br />❌ Object Locking:<br /> ❌ x-amz-object-lock-mode<br /> ❌ x-amz-object-lock-retain-until-date<br /> ❌ x-amz-object-lock-legal-hold<br />❌ ACL:<br /> ❌ x-amz-acl<br /> ❌ x-amz-grant-full-control<br /> ❌ x-amz-grant-read<br /> ❌ x-amz-grant-read-acp<br /> ❌ x-amz-grant-write-acp<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ✅ [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)                       | ❌ Multi-factor authentication:<br /> ❌ x-amz-mfa<br />❌ Object Locking:<br /> ❌ x-amz-bypass-governance-retention<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ✅ [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html)                     | ❌ Multi-factor authentication:<br /> ❌ x-amz-mfa<br />❌ Object Locking:<br /> ❌ x-amz-bypass-governance-retention<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ✅ [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html)       | ✅ Query Parameters:<br /> ✅ delimiter<br /> ✅ encoding-type<br /> ✅ key-marker<br /> ✅️ max-uploads<br /> ✅ prefix<br /> ✅ upload-id-marker                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ✅ [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)     | ✅ System Metadata:<br /> ✅ Content-Type<br /> ✅ Cache-Control<br /> ✅ Content-Disposition<br /> ✅ Content-Encoding<br /> ✅ Content-Language<br /> ✅ Expires<br /> ❌ Content-MD5<br />❌ Website:<br /> ❌ x-amz-website-redirect-location<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br /> ❌ x-amz-server-side-encryption-aws-kms-key-id<br /> ❌ x-amz-server-side-encryption-context<br /> ❌ x-amz-server-side-encryption-bucket-key-enabled<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Tagging:<br /> ❌ x-amz-tagging<br />❌ Object Locking:<br /> ❌ x-amz-object-lock-mode<br /> ❌ x-amz-object-lock-retain-until-date<br /> ❌ x-amz-object-lock-legal-hold<br />❌ ACL:<br /> ❌ x-amz-acl<br /> ❌ x-amz-grant-full-control<br /> ❌ x-amz-grant-read<br /> ❌ x-amz-grant-read-acp<br /> ❌ x-amz-grant-write-acp<br />❌ Storage class:<br /> ❌ x-amz-storage-class<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ✅ [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) | ❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner<br />❌ Request Payer:<br /> ❌ x-amz-request-payer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ✅ [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html)       | ❌ Request Payer:<br /> ❌ x-amz-request-payer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ✅ [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html)                           | ✅ Operation Metadata:<br /> ⚠️ x-amz-metadata-directive<br />✅ System Metadata:<br /> ✅ Content-Type<br /> ✅ Cache-Control<br /> ✅ Content-Disposition<br /> ✅ Content-Encoding<br /> ✅ Content-Language<br /> ✅ Expires<br />✅ Conditional Operations:<br /> ✅ x-amz-copy-source<br /> ✅ x-amz-copy-source-if-match<br /> ✅ x-amz-copy-source-if-modified-since<br /> ✅ x-amz-copy-source-if-none-match<br /> ✅ x-amz-copy-source-if-unmodified-since<br />❌ ACL:<br /> ❌ x-amz-acl<br /> ❌ x-amz-grant-full-control<br /> ❌ x-amz-grant-read<br /> ❌ x-amz-grant-read-acp<br /> ❌ x-amz-grant-write-acp<br />❌ Website:<br /> ❌ x-amz-website-redirect-location<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br /> ❌ x-amz-server-side-encryption-aws-kms-key-id<br /> ❌ x-amz-server-side-encryption-context<br /> ❌ x-amz-server-side-encryption-bucket-key-enabled<br /> ❌ x-amz-copy-source-server-side-encryption-customer-algorithm<br /> ❌ x-amz-copy-source-server-side-encryption-customer-key<br /> ❌ x-amz-copy-source-server-side-encryption-customer-key-MD5<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Tagging:<br /> ❌ x-amz-tagging<br /> ❌ x-amz-tagging-directive<br />❌ Object Locking:<br /> ❌ x-amz-object-lock-mode<br /> ❌ x-amz-object-lock-retain-until-date<br /> ❌ x-amz-object-lock-legal-hold<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner<br /> ❌ x-amz-source-expected-bucket-owner<br />❌ Checksums:<br /> ❌ x-amz-checksum-algorithm |
| ✅ [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html)                           | ✅ System Metadata:<br />❌ Content-MD5<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ✅ [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html)                   | ❌ Conditional Operations:<br /> ❌ x-amz-copy-source<br /> ❌ x-amz-copy-source-if-match<br /> ❌ x-amz-copy-source-if-modified-since<br /> ❌ x-amz-copy-source-if-none-match<br /> ❌ x-amz-copy-source-if-unmodified-since<br />✅ Range:<br /> ✅ x-amz-copy-source-range<br />❌ SSE-C:<br /> ❌ x-amz-server-side-encryption-customer-algorithm<br /> ❌ x-amz-server-side-encryption-customer-key<br /> ❌ x-amz-server-side-encryption-customer-key-MD5<br /> ❌ x-amz-copy-source-server-side-encryption-customer-algorithm<br /> ❌ x-amz-copy-source-server-side-encryption-customer-key<br /> ❌ x-amz-copy-source-server-side-encryption-customer-key-MD5<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner<br /> ❌ x-amz-source-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ✅ [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html)                             | Query Parameters:<br /> ✅ max-parts<br /> ✅ part-number-marker<br />❌ Request Payer:<br /> ❌ x-amz-request-payer<br />❌ Bucket Owner:<br /> ❌ x-amz-expected-bucket-owner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

{/* supa-mdx-lint-enable Rule003Spelling */}



# Storage Optimizations

Scaling Storage

Here are some optimizations that you can consider to improve performance and reduce costs as you start scaling Storage.



## Egress

If your project has high egress, these optimizations can help reducing it.


#### Resize images

Images typically make up most of your egress. By keeping them as small as possible, you can cut down on egress and boost your application's performance. You can take advantage of our [Image Transformation](/docs/guides/storage/serving/image-transformations) service to optimize any image on the fly.


#### Set a high cache-control value

Using the browser cache can effectively lower your egress since the asset remains stored in the user's browser after the initial download. Setting a high `cache-control` value ensures the asset stays in the user's browser for an extended period, decreasing the need to download it from the server repeatedly. Read more [here](/docs/guides/storage/cdn/smart-cdn#cache-duration)


#### Limit the upload size

You have the option to set a maximum upload size for your bucket. Doing this can prevent users from uploading and then downloading excessively large files. You can control the maximum file size by configuring this option at the [bucket level](/docs/guides/storage/buckets/creating-buckets).


#### Smart CDN

By leveraging our [Smart CDN](/docs/guides/storage/cdn/smart-cdn), you can achieve a higher cache hit rate and therefore lower your egress cached, as we charge less for cached egress (see [egress pricing](/docs/guides/platform/manage-your-usage/egress#pricing)).



## Optimize listing objects

Once you have a substantial number of objects, you might observe that the `supabase.storage.list()` method starts to slow down. This occurs because the endpoint is quite generic and attempts to retrieve both folders and objects in a single query. While this approach is very useful for building features like the Storage viewer on the Supabase dashboard, it can impact performance with a large number of objects.

If your application doesn't need the entire hierarchy computed you can speed up drastically the query execution for listing your objects by creating a Postgres function as following:

```sql
create or replace function list_objects(
    bucketid text,
    prefix text,
    limits int default 100,
    offsets int default 0
) returns table (
    name text,
    id uuid,
    updated_at timestamptz,
    created_at timestamptz,
    last_accessed_at timestamptz,
    metadata jsonb
) as $$
begin
    return query SELECT
        objects.name,
        objects.id,
        objects.updated_at,
        objects.created_at,
        objects.last_accessed_at,
        objects.metadata
    FROM storage.objects
    WHERE objects.name like prefix || '%'
    AND bucket_id = bucketid
    ORDER BY name ASC
    LIMIT limits
    OFFSET offsets;
end;
$$ language plpgsql stable;
```

You can then use the your Postgres function as following:

Using SQL:

```sql
select * from list_objects('bucket_id', '', 100, 0);
```

Using the SDK:

```js
const { data, error } = await supabase.rpc('list_objects', {
  bucketid: 'yourbucket',
  prefix: '',
  limit: 100,
  offset: 0,
})
```



## Optimizing RLS

When creating RLS policies against the storage tables you can add indexes to the interested columns to speed up the lookup



# Copy Objects

Learn how to copy and move objects


## Copy objects

You can copy objects between buckets or within the same bucket. Currently only objects up to 5 GB can be copied using the API.

When making a copy of an object, the owner of the new object will be the user who initiated the copy operation.


### Copying objects within the same bucket

To copy an object within the same bucket, use the `copy` method.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
await supabase.storage.from('avatars').copy('public/avatar1.png', 'private/avatar2.png')
```


### Copying objects across buckets

To copy an object across buckets, use the `copy` method and specify the destination bucket.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
await supabase.storage.from('avatars').copy('public/avatar1.png', 'private/avatar2.png', {
  destinationBucket: 'avatars2',
})
```



## Move objects

You can move objects between buckets or within the same bucket. Currently only objects up to 5GB can be moved using the API.

When moving an object, the owner of the new object will be the user who initiated the move operation. Once the object is moved, the original object will no longer exist.


### Moving objects within the same bucket

To move an object within the same bucket, you can use the `move` method.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const { data, error } = await supabase.storage
  .from('avatars')
  .move('public/avatar1.png', 'private/avatar2.png')
```


### Moving objects across buckets

To move an object across buckets, use the `move` method and specify the destination bucket.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
await supabase.storage.from('avatars').move('public/avatar1.png', 'private/avatar2.png', {
  destinationBucket: 'avatars2',
})
```



## Permissions

For a user to move and copy objects, they need `select` permission on the source object and `insert` permission on the destination object. For example:

```sql
create policy "User can select their own objects (in any buckets)"
on storage.objects
for select
to authenticated
using (
    owner_id = (select auth.uid())
);

create policy "User can upload in their own folders (in any buckets)"
on storage.objects
for insert
to authenticated
with check (
    (storage.folder(name))[1] = (select auth.uid())
);
```



# Delete Objects

Learn about deleting objects

When you delete one or more objects from a bucket, the files are permanently removed and not recoverable. You can delete a single object or multiple objects at once.

<Admonition type="note">
  Deleting objects should always be done via the **Storage API** and NOT via a **SQL query**. Deleting objects via a SQL query will not remove the object from the bucket and will result in the object being orphaned.
</Admonition>



## Delete objects

To delete one or more objects, use the `remove` method.

```javascript
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
await supabase.storage.from('bucket').remove(['object-path-2', 'folder/avatar2.png'])
```

<Admonition type="note">
  When deleting objects, there is a limit of 1000 objects at a time using the `remove` method.
</Admonition>



## RLS

To delete an object, the user must have the `delete` permission on the object. For example:

```sql
create policy "User can delete their own objects"
on storage.objects
for delete
TO authenticated
USING (
    owner = (select auth.uid()::text)
);
```



# Pricing



You are charged for the total size of all assets in your buckets.

<Price price="0.00002919" /> per GB-Hr (<Price price="0.021" /> per GB per month). You are only
charged for usage exceeding your subscription plan's quota.

| Plan       | Quota in GB | Over-Usage per GB       | Quota in GB-Hrs | Over-Usage per GB-Hr         |
| ---------- | ----------- | ----------------------- | --------------- | ---------------------------- |
| Free       | 1           | -                       | 744             | -                            |
| Pro        | 100         | <Price price="0.021" /> | 74,400          | <Price price="0.00002919" /> |
| Team       | 100         | <Price price="0.021" /> | 74,400          | <Price price="0.00002919" /> |
| Enterprise | Custom      | Custom                  | Custom          | Custom                       |

For a detailed explanation of how charges are calculated, refer to [Manage Storage size usage](/docs/guides/platform/manage-your-usage/storage-size).

<Admonition type="caution">
  If you use [Storage Image Transformations](/docs/guides/storage/serving/image-transformations), additional charges apply.
</Admonition>



# Error Codes

Learn about the Storage error codes and how to resolve them


## Storage error codes

<Admonition type="note">
  We are transitioning to a new error code system. For backwards compatibility you'll still be able to see the old error codes
</Admonition>

Error codes in Storage are returned as part of the response body. They are useful for debugging and understanding what went wrong with your request.
The error codes are returned in the following format:

```json
{
  "code": "error_code",
  "message": "error_message"
}
```

Here is the full list of error codes and their descriptions:

| `ErrorCode`                 | Description                                                     | `StatusCode` | Resolution                                                                                                                                                                                  |
| --------------------------- | --------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NoSuchBucket`              | The specified bucket does not exist.                            | 404          | Verify the bucket name and ensure it exists in the system, if it exists you don't have permissions to access it.                                                                            |
| `NoSuchKey`                 | The specified key does not exist.                               | 404          | Check the key name and ensure it exists in the specified bucket, if it exists you don't have permissions to access it.                                                                      |
| `NoSuchUpload`              | The specified upload does not exist.                            | 404          | The upload ID provided might not exists or the Upload was previously aborted                                                                                                                |
| `InvalidJWT`                | The provided JWT (JSON Web Token) is invalid.                   | 401          | The JWT provided might be expired or malformed, provide a valid JWT                                                                                                                         |
| `InvalidRequest`            | The request is not properly formed.                             | 400          | Review the request parameters and structure, ensure they meet the API's requirements, the error message will provide more details                                                           |
| `TenantNotFound`            | The specified tenant does not exist.                            | 404          | The Storage service had issues while provisioning, [Contact Support](/dashboard/support/new)                                                                                                |
| `EntityTooLarge`            | The entity being uploaded is too large.                         | 413          | Verify the max-file-limit is equal or higher to the resource you are trying to upload, you can change this value on the [Project Settings](/dashboard/project/_/storage/settings)           |
| `InternalError`             | An internal server error occurred.                              | 500          | Investigate server logs to identify the cause of the internal error. If you think it's a Storage error [Contact Support](/dashboard/support/new)                                            |
| `ResourceAlreadyExists`     | The specified resource already exists.                          | 409          | Use a different name or identifier for the resource to avoid conflicts. Use `x-upsert:true` header to overwrite the resource.                                                               |
| `InvalidBucketName`         | The specified bucket name is invalid.                           | 400          | Ensure the bucket name follows the naming conventions and does not contain invalid characters.                                                                                              |
| `InvalidKey`                | The specified key is invalid.                                   | 400          | Verify the key name and ensure it follows the naming conventions.                                                                                                                           |
| `InvalidRange`              | The specified range is not valid.                               | 416          | Make sure that range provided is within the file size boundary and follow the [HTTP Range spec](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range)                            |
| `InvalidMimeType`           | The specified MIME type is not valid.                           | 400          | Provide a valid MIME type, ensure using the standard MIME type format                                                                                                                       |
| `InvalidUploadId`           | The specified upload ID is invalid.                             | 400          | The upload ID provided is invalid or missing. Make sure to provide a active upload ID                                                                                                       |
| `KeyAlreadyExists`          | The specified key already exists.                               | 409          | Use a different key name to avoid conflicts with existing keys. Use `x-upsert:true` header to overwrite the resource.                                                                       |
| `BucketAlreadyExists`       | The specified bucket already exists.                            | 409          | Choose a unique name for the bucket that does not conflict with existing buckets.                                                                                                           |
| `DatabaseTimeout`           | Timeout occurred while accessing the database.                  | 504          | Investigate database performance and increase the default pool size. If this error still occurs, upgrade your instance                                                                      |
| `InvalidSignature`          | The signature provided does not match the calculated signature. | 403          | Check that you are providing the correct signature format, for more information refer to [SignatureV4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) |
| `SignatureDoesNotMatch`     | The request signature does not match the calculated signature.  | 403          | Check your credentials, access key id / access secret key / region that are all correct, refer to [S3 Authentication](/docs/guides/storage/s3/authentication).                              |
| `AccessDenied`              | Access to the specified resource is denied.                     | 403          | Check that you have the correct RLS policy to allow access to this resource                                                                                                                 |
| `ResourceLocked`            | The specified resource is locked.                               | 423          | This resource cannot be altered while there is a lock. Wait and try the request again                                                                                                       |
| `DatabaseError`             | An error occurred while accessing the database.                 | 500          | Investigate database logs and system configuration to identify and address the database error.                                                                                              |
| `MissingContentLength`      | The Content-Length header is missing.                           | 411          | Ensure the Content-Length header is included in the request with the correct value.                                                                                                         |
| `MissingParameter`          | A required parameter is missing in the request.                 | 400          | Provide all required parameters in the request to fulfill the API's requirements. The message field will contain more details                                                               |
| `InvalidUploadSignature`    | The provided upload signature is invalid.                       | 403          | The `MultiPartUpload` record was altered while the upload was ongoing, the signature do not match. Do not alter the upload record                                                           |
| `LockTimeout`               | Timeout occurred while waiting for a lock.                      | 423          | The lock couldn't be acquired within the specified timeout. Wait and try the request again                                                                                                  |
| `S3Error`                   | An error occurred related to Amazon S3.                         | -            | Refer to Amazon S3 documentation or [Contact Support](/dashboard/support/new) for assistance with resolving the S3 error.                                                                   |
| `S3InvalidAccessKeyId`      | The provided AWS access key ID is invalid.                      | 403          | Verify the AWS access key ID provided and ensure it is correct and active.                                                                                                                  |
| `S3MaximumCredentialsLimit` | The maximum number of credentials has been reached.             | 400          | The maximum limit of credentials is reached.                                                                                                                                                |
| `InvalidChecksum`           | The checksum of the entity does not match.                      | 400          | Recalculate the checksum of the entity and ensure it matches the one provided in the request.                                                                                               |
| `MissingPart`               | A part of the entity is missing.                                | 400          | Ensure all parts of the entity are included in the request before completing the operation.                                                                                                 |
| `SlowDown`                  | The request rate is too high and has been throttled.            | 503          | Reduce the request rate or implement exponential backoff and retry mechanisms to handle throttling.                                                                                         |



## Legacy error codes

As we are transitioning to a new error code system, you might still see the following error format:

```json
{
  "httpStatusCode": 400,
  "code": "error_code",
  "message": "error_message"
}
```

Here's a list of the most common error codes and their potential resolutions:


### 404 `not_found`

Indicates that the resource is not found or you don't have the correct permission to access it
**Resolution:**

*   Add a RLS policy to grant permission to the resource. See our [Access Control docs](/docs/guides/storage/uploads/access-control) for more information.
*   Ensure you include the user `Authorization` header
*   Verify the object exists


### 409 `already_exists`

Indicates that the resource already exists.
**Resolution:**

*   Use the `upsert` functionality in order to overwrite the file. Find out more [here](/docs/guides/storage/uploads/standard-uploads#overwriting-files).


### 403 `unauthorized`

You don't have permission to action this request
**Resolution:**

*   Add RLS policy to grant permission. See our [Access Control docs](/docs/guides/storage/security/access-control) for more information.
*   Ensure you include the user `Authorization` header


### 429 `too many requests`

This problem typically arises when a large number of clients are concurrently interacting with the Storage service, and the pooler has reached its `max_clients` limit.

**Resolution:**

*   Increase the max\_clients limits of the pooler.
*   Upgrade to a bigger project compute instance [here](/dashboard/project/_/settings/addons).


### 544 `database_timeout`

This problem arises when a high number of clients are concurrently using the Storage service, and Postgres doesn't have enough available connections to efficiently handle requests to Storage.

**Resolution:**

*   Increase the pool\_size limits of the pooler.
*   Upgrade to a bigger project compute instance [here](/dashboard/project/_/settings/addons).


### 500 `internal_server_error`

This issue occurs where there is a unhandled error.
**Resolution:**

*   File a support ticket to Storage team [here](/dashboard/support/new)



# Logs



Accessing the [Storage Logs](/dashboard/project/__/logs/explorer?q=select+id%2C+storage_logs.timestamp%2C+event_message+from+storage_logs%0A++%0A++order+by+timestamp+desc%0A++limit+100%0A++) allows you to examine all incoming request logs to your Storage service. You can also filter logs and delve into specific aspects of your requests.


### Common log queries


#### Filter by status 5XX error

```sql
select
  id,
  storage_logs.timestamp,
  event_message,
  r.statusCode,
  e.message as errorMessage,
  e.raw as rawError
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.res) as r
  cross join unnest(m.error) as e
where r.statusCode >= 500
order by timestamp desc
limit 100;
```


#### Filter by status 4XX error

```sql
select
  id,
  storage_logs.timestamp,
  event_message,
  r.statusCode,
  e.message as errorMessage,
  e.raw as rawError
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.res) as r
  cross join unnest(m.error) as e
where r.statusCode >= 400 and r.statusCode < 500
order by timestamp desc
limit 100;
```


#### Filter by method

```sql
select id, storage_logs.timestamp, event_message, r.method
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.req) as r
where r.method in ("POST")
order by timestamp desc
limit 100;
```


#### Filter by IP address

```sql
select id, storage_logs.timestamp, event_message, r.remoteAddress
from
  storage_logs
  cross join unnest(metadata) as m
  cross join unnest(m.req) as r
where r.remoteAddress in ("IP_ADDRESS")
order by timestamp desc
limit 100;
```



# Storage CDN



All assets uploaded to Supabase Storage are cached on a Content Delivery Network (CDN) to improve the latency for users all around the world. CDNs are a geographically distributed set of servers or **nodes** which cache content from an **origin server**. For Supabase Storage, the origin is the storage server running in the [same region as your project](/dashboard/project/_/settings/general). Aside from performance, CDNs also help with security and availability by mitigating Distributed Denial of Service (DDoS) and other application attacks.


### Example

Let's walk through an example of how a CDN helps with performance.

A new bucket is created for a Supabase project launched in Singapore. All requests to the Supabase Storage API are routed to the CDN first.

A user from the United States requests an object and is routed to the U.S. CDN. At this point, that CDN node does not have the object in its cache and pings the origin server in Singapore.
![CDN cache miss](/docs/img/cdn-cache-miss.png)

Another user, also in the United States, requests the same object and is served directly from the CDN cache in the United States instead of routing the request back to Singapore.
![CDN cache hit](/docs/img/cdn-cache-hit.png)

<Admonition type="note">
  Note that CDNs might still evict your object from their cache if it has not been requested for a while from a specific region. For example, if no user from United States requests your object, it will be removed from the CDN cache even if we set a very long cache control duration.
</Admonition>

The cache status of a particular request is sent in the `cf-cache-status` header. A cache status of `MISS` indicates that the CDN node did not have the object in its cache and had to ping the origin to get it. A cache status of `HIT` indicates that the object was sent directly from the CDN.


### Public vs private buckets

Objects in public buckets do not require any authorization to access objects. This leads to a better cache hit rate compared to private buckets.

For private buckets, permissions for accessing each object is checked on a per user level. For example, if two different users access the same object in a private bucket from the same region, it results in a cache miss for both the users since they might have different security policies attached to them.
On the other hand, if two different users access the same object in a public bucket from the same region, it results in a cache hit for the second user.



# Cache Metrics



Cache hits can be determined via the `metadata.response.headers.cf_cache_status` key in our [Logs Explorer](/docs/guides/platform/logs#logs-explorer). Any value that corresponds to either `HIT`, `STALE`, `REVALIDATED`, or `UPDATING` is categorized as a cache hit.
The following example query will show the top cache misses from the `edge_logs`:

```sql
select
  r.path as path,
  r.search as search,
  count(id) as count
from
  edge_logs as f
  cross join unnest(f.metadata) as m
  cross join unnest(m.request) as r
  cross join unnest(m.response) as res
  cross join unnest(res.headers) as h
where
  starts_with(r.path, '/storage/v1/object')
  and r.method = 'GET'
  and h.cf_cache_status in ('MISS', 'NONE/UNKNOWN', 'EXPIRED', 'BYPASS', 'DYNAMIC')
group by path, search
order by count desc
limit 50;
```

Try out [this query](/dashboard/project/_/logs/explorer?q=%0Aselect%0A++r.path+as+path%2C%0A++r.search+as+search%2C%0A++count%28id%29+as+count%0Afrom%0A++edge_logs+as+f%0A++cross+join+unnest%28f.metadata%29+as+m%0A++cross+join+unnest%28m.request%29+as+r%0A++cross+join+unnest%28m.response%29+as+res%0A++cross+join+unnest%28res.headers%29+as+h%0Awhere%0A++starts_with%28r.path%2C+%27%2Fstorage%2Fv1%2Fobject%27%29%0A++and+r.method+%3D+%27GET%27%0A++and+h.cf_cache_status+in+%28%27MISS%27%2C+%27NONE%2FUNKNOWN%27%2C+%27EXPIRED%27%2C+%27BYPASS%27%2C+%27DYNAMIC%27%29%0Agroup+by+path%2C+search%0Aorder+by+count+desc%0Alimit+50%3B) in the Logs Explorer.

Your cache hit ratio over time can then be determined using the following query:

```sql
select
  timestamp_trunc(timestamp, hour) as timestamp,
  countif(h.cf_cache_status in ('HIT', 'STALE', 'REVALIDATED', 'UPDATING')) / count(f.id) as ratio
from
  edge_logs as f
  cross join unnest(f.metadata) as m
  cross join unnest(m.request) as r
  cross join unnest(m.response) as res
  cross join unnest(res.headers) as h
where starts_with(r.path, '/storage/v1/object') and r.method = 'GET'
group by timestamp
order by timestamp desc;
```

Try out [this query](/dashboard/project/_/logs/explorer?q=%0Aselect%0A++timestamp_trunc%28timestamp%2C+hour%29+as+timestamp%2C%0A++countif%28h.cf_cache_status+in+%28%27HIT%27%2C+%27STALE%27%2C+%27REVALIDATED%27%2C+%27UPDATING%27%29%29+%2F+count%28f.id%29+as+ratio%0Afrom%0A++edge_logs+as+f%0A++cross+join+unnest%28f.metadata%29+as+m%0A++cross+join+unnest%28m.request%29+as+r%0A++cross+join+unnest%28m.response%29+as+res%0A++cross+join+unnest%28res.headers%29+as+h%0Awhere+starts_with%28r.path%2C+%27%2Fstorage%2Fv1%2Fobject%27%29+and+r.method+%3D+%27GET%27%0Agroup+by+timestamp%0Aorder+by+timestamp+desc%3B) in the Logs Explorer.



# Smart CDN



With Smart CDN caching enabled, the asset metadata in your database is synchronized to the edge. This automatically revalidates the cache when the asset is changed or deleted.

Moreover, the Smart CDN achieves a greater cache hit rate by shielding the origin server from asset requests that remain unchanged, even when different query strings are used in the URL.

<Admonition type="note">
  Smart CDN caching is automatically enabled for [Pro Plan and above](/pricing).
</Admonition>



## Cache duration

When Smart CDN is enabled, the asset is cached on the CDN for as long as possible. You can still control how long assets are stored in the browser using the [`cacheControl`](/docs/reference/javascript/storage-from-upload) option when uploading a file. Smart CDN caching works with all types of storage operations including signed URLs.

When a file is updated or deleted, the CDN cache is automatically invalidated to reflect the change (including transformed images). It can take **up to 60 seconds** for the CDN cache to be invalidated as the asset metadata has to propagate across all the data-centers around the globe.

When an asset is invalidated at the CDN level, browsers may not update its cache. This is where cache eviction comes into play.



## Cache eviction

Even when an asset is marked as invalidated at the CDN level, browsers may not refresh their cache for that asset.

If you have assets that undergo frequent updates, it is advisable to upload the new asset to a different path. This approach ensures that you always have the most up-to-date asset accessible.

If you anticipate that your asset might be deleted, it's advisable to set a shorter browser Time-to-Live (TTL) value using the `cacheControl` option. The default TTL is typically set to 1 hour, which is generally a reasonable default value.



## Bypassing cache

If you need to ensure assets refresh directly from the origin server and bypass the cache, you can achieve this by adding a unique query string to the URL.

For instance, you can use a URL like `/storage/v1/object/sign/profile-pictures/cat.jpg?version=1` with a long browser cache (e.g., 1 year). To update the picture, increment the version query parameter in the URL, like `/storage/v1/object/sign/profile-pictures/cat.jpg?version=2`. The CDN will recognize it as a new object and fetch the updated version from the origin.



# Creating Buckets



You can create a bucket using the Supabase Dashboard. Since storage is interoperable with your Postgres database, you can also use SQL or our client libraries.
Here we create a bucket called "avatars":

<Tabs scrollable size="small" type="underlined" defaultActiveId="javascript" queryGroup="language">
  <TabPanel id="javascript" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)

    // ---cut---
    // Use the JS library to create a bucket.

    const { data, error } = await supabase.storage.createBucket('avatars', {
      public: true, // default: false
    })
    ```

    [Reference.](/docs/reference/javascript/storage-createbucket)
  </TabPanel>

  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Storage](/dashboard/project/_/storage/buckets) page in the Dashboard.
    2.  Click **New Bucket** and enter a name for the bucket.
    3.  Click **Create Bucket**.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Use Postgres to create a bucket.

    insert into storage.buckets
      (id, name, public)
    values
      ('avatars', 'avatars', true);
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    void main() async {
      final supabase = SupabaseClient('supabaseUrl', 'supabaseKey');

      final storageResponse = await supabase
          .storage
          .createBucket('avatars');
    }
    ```

    [Reference.](https://pub.dev/documentation/storage_client/latest/storage_client/SupabaseStorageClient/createBucket.html)
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.storage.createBucket(
      "avatars",
      options: BucketOptions(public: true)
    )
    ```

    [Reference.](/docs/reference/swift/storage-createbucket)
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.storage.create_bucket(
      'avatars',
      options={"public": True}
    )
    ```

    [Reference.](/docs/reference/python/storage-createbucket)
  </TabPanel>
</Tabs>



## Restricting uploads

When creating a bucket you can add additional configurations to restrict the type or size of files you want this bucket to contain.

For example, imagine you want to allow your users to upload only images to the `avatars` bucket and the size must not be greater than 1MB. You can achieve the following by providing `allowedMimeTypes` and `maxFileSize`:

```js
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)

// ---cut---
// Use the JS library to create a bucket.

const { data, error } = await supabase.storage.createBucket('avatars', {
  public: true,
  allowedMimeTypes: ['image/*'],
  fileSizeLimit: '1MB',
})
```

If an upload request doesn't meet the above restrictions it will be rejected. See [File Limits](/docs/guides/storage/uploads/file-limits) for more information.



# Storage Buckets



Buckets allow you to keep your files organized and determines the [Access Model](#access-model) for your assets. [Upload restrictions](/docs/guides/storage/buckets/creating-buckets#restricting-uploads) like max file size and allowed content types are also defined at the bucket level.



## Access model

There are 2 access models for buckets, **public** and **private** buckets.


### Private buckets

When a bucket is set to **Private** all operations are subject to access control via [RLS policies](/docs/guides/storage/security/access-control). This also applies when downloading assets. Buckets are private by default.

The only ways to download assets within a private bucket is to:

*   Use the [download method](/docs/reference/javascript/storage-from-download) by providing a authorization header containing your user's JWT. The RLS policy you create on the `storage.objects` table will use this user to determine if they have access.
*   Create a signed URL with the [`createSignedUrl` method](/docs/reference/javascript/storage-from-createsignedurl) that can be accessed for a limited time.


#### Example use cases:

*   Uploading users' sensitive documents
*   Securing private assets by using RLS to set up fine-grain access controls


### Public buckets

When a bucket is designated as 'Public,' it effectively bypasses access controls for both retrieving and serving files within the bucket. This means that anyone who possesses the asset URL can readily access the file.

Access control is still enforced for other types of operations including uploading, deleting, moving, and copying.


#### Example use cases:

*   User profile pictures
*   User public media
*   Blog post content

Public buckets are more performant than private buckets since they are [cached differently](/docs/guides/storage/cdn/fundamentals#public-vs-private-buckets).



# Connecting to Analytics Buckets



<Admonition type="caution">
  This feature is in **Private Alpha**. API stability and backward compatibility are not guaranteed at this stage. Reach out from this [Form](https://forms.supabase.com/analytics-buckets) to request access
</Admonition>

When interacting with Analytics Buckets, you authenticate against two main services - the Iceberg REST Catalog and the S3-Compatible Storage Endpoint.

The **Iceberg REST Catalog** acts as the central management system for Iceberg tables. It allows Iceberg clients, such as PyIceberg and Apache Spark, to perform metadata operations including:

*   Creating and managing tables and namespaces
*   Tracking schemas and handling schema evolution
*   Managing partitions and snapshots
*   Ensuring transactional consistency and isolation

The REST Catalog itself does not store the actual data. Instead, it stores metadata describing the structure, schema, and partitioning strategy of Iceberg tables.

Actual data storage and retrieval operations occur through the separate S3-compatible endpoint, optimized for reading and writing large analytical datasets stored in Parquet files.



## Authentication

To connect to an Analytics Bucket, you will need

*   An Iceberg client (Spark, PyIceberg, etc) which supports the REST Catalog interface.

*   S3 credentials to authenticate your Iceberg client with the underlying S3 Bucket.
    To create S3 Credentials go to [**Project Settings > Storage**](/dashboard/project/_/storage/settings), for more information, see the [S3 Authentication Guide](/docs/guides/storage/s3/authentication). We will support other authentication methods in the future.

*   The project reference and Service key for your Supabase project.
    You can find your Service key in the Supabase Dashboard under [**Project Settings > API**.](/dashboard/project/_/settings/api-keys)

You will now have an **Access Key** and a **Secret Key** that you can use to authenticate your Iceberg client.



## Connecting via PyIceberg

PyIceberg is a Python client for Apache Iceberg, facilitating interaction with Iceberg Buckets.

**Installation**

```bash
pip install pyiceberg pyarrow
```

Here's a comprehensive example using PyIceberg with clearly separated configuration:

```python
from pyiceberg.catalog import load_catalog
import pyarrow as pa
import datetime


# Supabase project ref
PROJECT_REF = "<your-supabase-project-ref>"


# Configuration for Iceberg REST Catalog
WAREHOUSE = "your-analytics-bucket-name"
TOKEN = "SERVICE_KEY"


# Configuration for S3-Compatible Storage
S3_ACCESS_KEY = "KEY"
S3_SECRET_KEY = "SECRET"
S3_REGION = "PROJECT_REGION"

S3_ENDPOINT = f"https://{PROJECT_REF}.supabase.co/storage/v1/s3"
CATALOG_URI = f"https://{PROJECT_REF}.supabase.co/storage/v1/iceberg"


# Load the Iceberg catalog
catalog = load_catalog(
    "analytics-bucket",
    type="rest",
    warehouse=WAREHOUSE,
    uri=CATALOG_URI,
    token=TOKEN,
    **{
        "py-io-impl": "pyiceberg.io.pyarrow.PyArrowFileIO",
        "s3.endpoint": S3_ENDPOINT,
        "s3.access-key-id": S3_ACCESS_KEY,
        "s3.secret-access-key": S3_SECRET_KEY,
        "s3.region": S3_REGION,
        "s3.force-virtual-addressing": False,
    },
)


# Create namespace if it doesn't exist
catalog.create_namespace_if_not_exists("default")


# Define schema for your Iceberg table
schema = pa.schema([
    pa.field("event_id", pa.int64()),
    pa.field("event_name", pa.string()),
    pa.field("event_timestamp", pa.timestamp("ms")),
])


# Create table (if it doesn't exist already)
table = catalog.create_table_if_not_exists(("default", "events"), schema=schema)


# Generate and insert sample data
current_time = datetime.datetime.now()
data = pa.table({
    "event_id": [1, 2, 3],
    "event_name": ["login", "logout", "purchase"],
    "event_timestamp": [current_time, current_time, current_time],
})


# Append data to the Iceberg table
table.append(data)


# Scan table and print data as pandas DataFrame
df = table.scan().to_pandas()
print(df)
```



## Connecting via Apache Spark

Apache Spark allows distributed analytical queries against Iceberg Buckets.

```python
from pyspark.sql import SparkSession


# Supabase project ref
PROJECT_REF = "<your-supabase-ref>"


# Configuration for Iceberg REST Catalog
WAREHOUSE = "your-analytics-bucket-name"
TOKEN = "SERVICE_KEY"


# Configuration for S3-Compatible Storage
S3_ACCESS_KEY = "KEY"
S3_SECRET_KEY = "SECRET"
S3_REGION = "PROJECT_REGION"

S3_ENDPOINT = f"https://{PROJECT_REF}.supabase.co/storage/v1/s3"
CATALOG_URI = f"https://{PROJECT_REF}.supabase.co/storage/v1/iceberg"


# Initialize Spark session with Iceberg configuration
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("SupabaseIceberg") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config('spark.jars.packages', 'org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.6.1,org.apache.iceberg:iceberg-aws-bundle:1.6.1') \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.my_catalog.type", "rest") \
    .config("spark.sql.catalog.my_catalog.uri", CATALOG_URI) \
    .config("spark.sql.catalog.my_catalog.warehouse", WAREHOUSE) \
    .config("spark.sql.catalog.my_catalog.token", TOKEN) \
    .config("spark.sql.catalog.my_catalog.s3.endpoint", S3_ENDPOINT) \
    .config("spark.sql.catalog.my_catalog.s3.path-style-access", "true") \
    .config("spark.sql.catalog.my_catalog.s3.access-key-id", S3_ACCESS_KEY) \
    .config("spark.sql.catalog.my_catalog.s3.secret-access-key", S3_SECRET_KEY) \
    .config("spark.sql.catalog.my_catalog.s3.remote-signing-enabled", "false") \
    .config("spark.sql.defaultCatalog", "my_catalog") \
    .getOrCreate()


# SQL Operations
spark.sql("CREATE NAMESPACE IF NOT EXISTS analytics")

spark.sql("""
    CREATE TABLE IF NOT EXISTS analytics.users (
        user_id BIGINT,
        username STRING
    )
    USING iceberg
""")

spark.sql("""
    INSERT INTO analytics.users (user_id, username)
    VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')
""")

result_df = spark.sql("SELECT * FROM analytics.users")
result_df.show()
```



## Connecting to the Iceberg REST Catalog directly

To authenticate with the Iceberg REST Catalog directly, you need to provide a valid Supabase **Service key** as a Bearer token.

```
curl \
  --request GET -sL \
  --url 'https://<your-supabase-project>.supabase.co/storage/v1/iceberg/v1/config?warehouse=<bucket-name>' \
  --header 'Authorization: Bearer <your-service-key>'
```



# Creating Analytics Buckets



<Admonition type="caution">
  This feature is in **Private Alpha**. API stability and backward compatibility are not guaranteed at this stage. Reach out from this [Form](https://forms.supabase.com/analytics-buckets) to request access
</Admonition>

Analytics Buckets use [Apache Iceberg](https://iceberg.apache.org/), an open-table format for managing large analytical datasets.
You can interact with them using tools such as [PyIceberg](https://py.iceberg.apache.org/), [Apache Spark](https://spark.apache.org/) or any client which supports the [standard Iceberg REST Catalog API](https://editor-next.swagger.io/?url=https://raw.githubusercontent.com/apache/iceberg/main/open-api/rest-catalog-open-api.yaml).

You can create an Analytics Bucket using either the Supabase SDK or the Supabase Dashboard.


### Using the Supabase SDK

```ts
import { createClient } from '@supabase/supabase-js'

const supabase = createClient('https://your-project.supabase.co', 'your-service-key')

supabase.storage.createBucket('my-analytics-bucket', {
  type: 'ANALYTICS',
})
```


### Using the Supabase Dashboard

1.  Navigate to the Storage section in the Supabase Dashboard.
2.  Click on "Create Bucket".
3.  Enter a name for your bucket (e.g., my-analytics-bucket).
4.  Select "Analytics Bucket" as the bucket type.

<img alt="Storage schema design" src="/docs/img/storage/iceberg-bucket.png" />

Now, that you have created your Analytics Bucket, you can start [connecting to it](/docs/guides/storage/analytics/connecting-to-analytics-bucket) with Iceberg clients like PyIceberg or Apache Spark.



# Analytics Buckets



<Admonition type="caution">
  This feature is in **Private Alpha**. API stability and backward compatibility are not guaranteed at this stage. Reach out from this [Form](https://forms.supabase.com/analytics-buckets) to request access
</Admonition>

**Analytics Buckets** are designed for analytical workflows on large datasets without impacting your main database.

Postgres tables are optimized for handling real-time, transactional workloads with frequent inserts, updates, deletes and low-latency queries. **Analytical workloads** have very different requirements: processing large volumes of historical data, running complex queries and aggregations, minimizing storage costs, and ensuring these analytical queries do not interfere with the production traffic.

**Analytics Buckets** address these requirements using [Apache Iceberg](https://iceberg.apache.org/), an open-table format for managing large analytical datasets efficiently.

Analytics Buckets are ideal for
• Data warehousing and business intelligence
• Historical data archiving
• Periodically refreshed real-time analytics
• Complex analytical queries over large datasets

By separating transactional and analytical workloads, Supabase makes it easy to build scalable analytics pipelines without impacting your primary Postgres performance.



# Analytics Buckets Limits



<Admonition type="caution">
  This feature is in **Private Alpha**. API stability and backward compatibility are not guaranteed at this stage. Reach out from this [Form](https://forms.supabase.com/analytics-buckets) to request access
</Admonition>

The following default limits are applied when this feature is in the private alpha stage, they can be adjusted on a case-by-case basis:

| **Category**                            | **Limit** |
| --------------------------------------- | --------- |
| Number of Analytics Buckets per project | 2         |
| Number of namespaces per bucket         | 10        |
| Number of tables per namespace          | 10        |



## Pricing

Analytics Buckets are Free to use during the Private Alpha phase,
however, you'll still be charged for the underlying egress.



# Self-Hosting with Docker

Learn how to configure and deploy Supabase with Docker.

Docker is the easiest way to get started with self-hosted Supabase. It should only take you a few minutes to get up and running. This guide assumes you are running the command from the machine you intend to host from.



## Contents

1.  [Before you begin](#before-you-begin)
2.  [Installing and running Supabase](#installing-and-running-supabase)
3.  [Accessing your services](#accessing-supabase-studio)
4.  [Updating your services](#updating-your-services)
5.  [Securing your services](#securing-your-services)



## Before you begin

You need the following installed in your system: [Git](https://git-scm.com/downloads) and Docker ([Windows](https://docs.docker.com/desktop/install/windows-install/), [macOS](https://docs.docker.com/desktop/install/mac-install/), or [Linux](https://docs.docker.com/desktop/install/linux-install/)).



## Installing and running Supabase

Follow these steps to start Supabase on your machine:

<Tabs scrollable size="small" type="underlined" defaultActiveId="general">
  <TabPanel id="general" label="General">
    ```sh
    # Get the code
    git clone --depth 1 https://github.com/supabase/supabase

    # Make your new supabase project directory
    mkdir supabase-project

    # Tree should look like this
    # .
    # ├── supabase
    # └── supabase-project

    # Copy the compose files over to your project
    cp -rf supabase/docker/* supabase-project

    # Copy the fake env vars
    cp supabase/docker/.env.example supabase-project/.env

    # Switch to your project directory
    cd supabase-project

    # Pull the latest images
    docker compose pull

    # Start the services (in detached mode)
    docker compose up -d
    ```
  </TabPanel>

  <TabPanel id="advanced" label="Advanced">
    ```sh
    # Get the code using git sparse checkout
    git clone --filter=blob:none --no-checkout https://github.com/supabase/supabase
    cd supabase
    git sparse-checkout set --cone docker && git checkout master
    cd ..

    # Make your new supabase project directory
    mkdir supabase-project

    # Tree should look like this
    # .
    # ├── supabase
    # └── supabase-project

    # Copy the compose files over to your project
    cp -rf supabase/docker/* supabase-project

    # Copy the fake env vars
    cp supabase/docker/.env.example supabase-project/.env

    # Switch to your project directory
    cd supabase-project

    # Pull the latest images
    docker compose pull

    # Start the services (in detached mode)
    docker compose up -d
    ```
  </TabPanel>
</Tabs>

<Admonition type="tip">
  If you are using rootless docker, edit `.env` and set `DOCKER_SOCKET_LOCATION` to your docker socket location. For example: `/run/user/1000/docker.sock`. Otherwise, you will see an error like `container supabase-vector exited (0)`.
</Admonition>

After all the services have started you can see them running in the background:

```sh
docker compose ps
```

All of the services should have a status `running (healthy)`. If you see a status like `created` but not `running`, try starting that service manually with `docker compose start <service-name>`.

<Admonition type="danger">
  Your app is now running with default credentials.
  [Secure your services](#securing-your-services) as soon as possible using the instructions below.
</Admonition>


### Accessing Supabase Studio

You can access Supabase Studio through the API gateway on port `8000`. For example: `http://<your-ip>:8000`, or [localhost:8000](http://localhost:8000) if you are running Docker locally.

You will be prompted for a username and password. By default, the credentials are:

*   Username: `supabase`
*   Password: `this_password_is_insecure_and_should_be_updated`

You should change these credentials as soon as possible using the [instructions](#dashboard-authentication) below.


### Accessing the APIs

Each of the APIs are available through the same API gateway:

*   REST: `http://<your-ip>:8000/rest/v1/`
*   Auth: `http://<your-domain>:8000/auth/v1/`
*   Storage: `http://<your-domain>:8000/storage/v1/`
*   Realtime: `http://<your-domain>:8000/realtime/v1/`


### Accessing your Edge Functions

Edge Functions are stored in `volumes/functions`. The default setup has a `hello` Function that you can invoke on `http://<your-domain>:8000/functions/v1/hello`.

You can add new Functions as `volumes/functions/<FUNCTION_NAME>/index.ts`. Restart the `functions` service to pick up the changes: `docker compose restart functions --no-deps`


### Accessing Postgres

By default, the Supabase stack runs the [Supavisor](https://supabase.github.io/supavisor/development/docs/) connection pooler. Supavisor provides efficient management of database connections.

You can connect to the Postgres database using the following methods:

1.  For session-based connections (equivalent to direct Postgres connections):

```bash
psql 'postgres://postgres.your-tenant-id:your-super-secret-and-long-postgres-password@localhost:5432/postgres'
```

2.  For pooled transactional connections:

```bash
psql 'postgres://postgres.your-tenant-id:your-super-secret-and-long-postgres-password@localhost:6543/postgres'
```

The default tenant ID is `your-tenant-id`, and the default password is `your-super-secret-and-long-postgres-password`. You should change these as soon as possible using the [instructions below](#update-secrets).

By default, the database is not accessible from outside the local machine but the pooler is. You can [change this](#exposing-your-postgres-database) by updating the `docker-compose.yml` file.

You may also want to connect to your Postgres database via an ORM or another direct method other than `psql`.

For this you can use the standard Postgres connection string.
You can find the the environment values mentioned below in the `.env` file which will be covered in the next section.

```
postgres://postgres:[POSTGRES_PASSWORD]@[your-server-ip]:5432/[POSTGRES_DB]
```



## Updating your services

For security reasons, we "pin" the versions of each service in the docker-compose file (these versions are updated ~monthly). If you want to update any services immediately, you can do so by updating the version number in the docker compose file and then running `docker compose pull`. You can find all the latest docker images in the [Supabase Docker Hub](https://hub.docker.com/u/supabase).

You should update your services frequently to get the latest features and bug fixes and security patches. Note that you will need to restart the services to pick up the changes, which will result in some downtime for your services.

**Example**
You'll want to update the Studio(Dashboard) frequently to get the latest features and bug fixes. To update the Dashboard:

1.  Visit the [supabase/studio](https://hub.docker.com/r/supabase/studio/tags) image in the [Supabase Docker Hub](https://hub.docker.com/u/supabase)
2.  Find the latest version (tag) number. It will look something like `20241029-46e1e40`
3.  Update the `image` field in the `docker-compose.yml` file to the new version. It should look like this: `image: supabase/studio:20241028-a265374`
4.  Run `docker compose pull` and then `docker compose up -d` to restart the service with the new version.



## Securing your services

While we provided you with some example secrets for getting started, you should NEVER deploy your Supabase setup using the defaults we have provided. Follow all of the steps in this section to ensure you have a secure setup, and then [restart all services](#restarting-all-services) to pick up the changes.


### Generate API keys

We need to generate secure keys for accessing your services. We'll use the `JWT Secret` to generate `anon` and `service` API keys using the form below.

1.  **Obtain a Secret**: Use the 40-character secret provided, or create your own. If creating, ensure it's a strong, random string of 40 characters.
2.  **Store Securely**: Save the secret in a secure location on your local machine. Don't share this secret publicly or commit it to version control.
3.  **Generate a JWT**: Use the form below to generate a new `JWT` using your secret.

<JwtGenerator />


### Update API keys

Run this form twice to generate new `anon` and `service` API keys. Replace the values in the `./docker/.env` file:

*   `ANON_KEY` - replace with an `anon` key
*   `SERVICE_ROLE_KEY` - replace with a `service` key

You will need to [restart](#restarting-all-services) the services for the changes to take effect.


### Update secrets

Update the `./docker/.env` file with your own secrets. In particular, these are required:

*   `POSTGRES_PASSWORD`: the password for the `postgres` role.
*   `JWT_SECRET`: used by PostgREST and GoTrue, among others.
*   `SITE_URL`: the base URL of your site.
*   `SMTP_*`: mail server credentials. You can use any SMTP server.
*   `POOLER_TENANT_ID`: the tenant-id that will be used by Supavisor pooler for your connection string
*   `PG_META_CRYPTO_KEY`: encryption key for securing connection strings between Studio and postgres-meta
*   `SECRET_KEY_BASE`: encryption key for securing Realtime and Supavisor communications. (Must be at least 64 characters; generate with `openssl rand -base64 48`)

You will need to [restart](#restarting-all-services) the services for the changes to take effect.


### Dashboard authentication

The Dashboard is protected with basic authentication. The default user and password MUST be updated before using Supabase in production.
Update the following values in the `./docker/.env` file:

*   `DASHBOARD_USERNAME`: The default username for the Dashboard
*   `DASHBOARD_PASSWORD`: The default password for the Dashboard

You can also add more credentials for multiple users in `./docker/volumes/api/kong.yml`. For example:

```yaml docker/volumes/api/kong.yml
basicauth_credentials:
  - consumer: DASHBOARD
    username: user_one
    password: password_one
  - consumer: DASHBOARD
    username: user_two
    password: password_two
```

To enable all dashboard features outside of `localhost`, update the following value in the `./docker/.env` file:

*   `SUPABASE_PUBLIC_URL`: The URL or IP used to access the dashboard

You will need to [restart](#restarting-all-services) the services for the changes to take effect.



## Restarting all services

You can restart services to pick up any configuration changes by running:

```sh

---
**Navigation:** [← Previous](./02-metrics.md) | [Index](./index.md) | [Next →](./04-stop-and-remove-the-containers.md)
