**Navigation:** [← Previous](./32-2023-releases.md) | [Index](./index.md) | [Next →](./34-2025-releases.md)

# Feature availability
Source: https://docs.pinecone.io/release-notes/feature-availability



This page defines the different availability phases of a feature in Pinecone.

The availability phases are used to communicate the maturity and stability of a feature. The availability phases are:

* **Early access**: In active development and may change at any time. Intended for user feedback only. In some cases, users must be granted explicit access to the API by Pinecone.

* **Public preview**: Unlikely to change between public preview and general availability. Not recommended for production usage. Available to all users.

* **Limited availability**: Available to select customers in a subset of regions and providers for production usage.

* **General availability**: Will not change on short notice. Recommended for production usage. Officially [supported by Pinecone](/troubleshooting/pinecone-support-slas) for non-production and production usage.

* **Deprecated**: Still supported, but no longer under active development, except for critical security fixes. Existing usage will continue to function, but migration following the upgrade guide is strongly recommended. Will be removed in the future at an announced date.

* **End of life (EOL)**: Removed, and no longer supported or available.

<Note>
  A feature is in **general availability** unless explicitly marked otherwise.
</Note>



# Billing disputes and refunds
Source: https://docs.pinecone.io/troubleshooting/billing-disputes-and-refunds



As a rule, Pinecone does not offer refunds for unused indexes. If you use a pod-based index, we charge only for the pods you use to create it, not per API call or query. Whether you have used your index or not does not factor into our billing.

Our serverless indexes are a better fit if you don't plan to use your index on a regular basis. Serverless indexes are billed by the number of reads and writes you run and how much storage your index consumes. If your bill for your pod-based index is too high, we recommend [migrating to a serverless index](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless) instead.

Our billing policies are detailed in our [user agreement](https://www.pinecone.io/user-agreement/) and [pricing page](https://pinecone.io/pricing).

We have several resources available to help you manage your bill:

* [Change your billing plan](/guides/organizations/manage-billing/upgrade-billing-plan)
* [Monitor your usage and costs](/guides/manage-cost/monitor-usage-and-costs)
* [Understand cost](/guides/manage-cost/understanding-cost)
* [Manage cost](/guides/manage-cost/manage-cost)



# Contact Support
Source: https://docs.pinecone.io/troubleshooting/contact-support



Pinecone Support is available to customers on the **Standard** billing plan.

First-response SLAs only apply to tickets created by users in an organization subscribed to a [support plan](https://www.pinecone.io/pricing/?plans=support). To upgrade your support plan, go to [Manage your support plan](https://app.pinecone.io/organizations/-/settings/support/plans) in the console and select your desired plan. Before subscribing to a support plan, you must [Upgrade your billing plan](/guides/organizations/manage-billing/upgrade-billing-plan) to the **Standard** tier.

Our business hours are Monday to Friday from 8:00 AM to 8:00 PM Eastern Time. We are closed on US federal holidays. Customers subscribed to the **Pro** or **Premium** support plan have 24/7/365 on-call availability, which is triggered by creating a SEV-1 ticket.

All customers subscribed to a support plan can create tickets in the Pinecone console. To create a ticket, go to the [Help center](https://app.pinecone.io/organizations/-/settings/support/ticket), select [Create a ticket](https://app.pinecone.io/organizations/-/settings/support/ticket/create), and fill out the form.

If you are not subscribed to a support plan and need help logging into the console, upgrading your support or billing plan, or have questions about billing, please complete the [public support contact form](https://www.pinecone.io/contact/support/) and we will respond if necessary.

If you have general questions about the platform, pricing, events, and more, [contact our sales team](https://www.pinecone.io/contact/). For inquiries about partnerships, please [contact the Pinecone Partner Program](https://www.pinecone.io/partners/#sales-contact-form-submissions).



# CORS Issues
Source: https://docs.pinecone.io/troubleshooting/cors-issues



Cross-Origin Resource Sharing (CORS) is an HTTP-header based security feature that
allows a server to indicate which domains, schemes or ports a browser should accept
content from. When a browser-based app, by default, only loads content from the same
origin as the original request, CORS errors can appear if the responses come from
a different origin. Pinecone's current implementation of CORS can cause this mismatch
and display the following error:

```console console theme={null}
No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

This error occurs in response to cross-origin requests. Most commonly, it occurs when a user is running a local web server with the hostname `localhost`, which Pinecone's Same Origin Policy (SOP) treats as distinct from the IP address of the local machine.

To resolve this issue, host your web server on an external server with a public IP address and DNS name entry.

### About Localhost (running a web server locally)

Localhost is not inherently a problem. However, when running a web server on a local machine (e.g., laptop or desktop computer), using "localhost" as the hostname can cause issues with cross-origin resource sharing (CORS).

The reason for this is that the Same-Origin Policy (SOP) enforced by web browsers treats "localhost" as a different origin than the actual IP address of the machine. For example, if a web application running on "localhost" makes a cross-origin request to a server running on the actual IP address of the machine, the browser will treat it as a cross-origin request and enforce the SOP.

To allow cross-origin requests between "localhost" and the actual IP address of the machine, the server needs to explicitly allow them by including the appropriate CORS headers in its response. However, as mentioned earlier, running a web server on a local machine can present security risks and is generally not recommended for production use.

Therefore, while "localhost" itself is not a problem, using it as the hostname for a web server can cause CORS issues that need to be properly addressed. Additionally, running a web server on a local machine should be done with caution and only for development or testing purposes, rather than for production use.



# Create and manage vectors with metadata
Source: https://docs.pinecone.io/troubleshooting/create-and-manage-vectors-with-metadata



Performing deletes by metadata filtering can be a very expensive process for any database. By using a hierarchical naming convention for vector IDs, you can avoid this process and perform deletes by ID. This is more efficient and will reduce the impact on the compute resources, minimize query latency, and maintain a more consistent user experience.


## 1. Upsert

* Generate a hierarchical naming convention for vector IDs.
  * One recommended pattern may be `parentId-chunkId` where parentId is the ID of the document and `chunkId` is an integer starting with 0 to the total number of chunks
  * While capturing embeddings and preparing upserts for Pinecone, capture the total number of chunks for each `parentId`.
  * Append the `chunkCount` to the metadata field of the `parentId-0` vector, or you may append them to all chunks if desired. This should be an integer and cardinality will naturally be low.
  * Upsert the vectors with the `parentId-chunkId` as the ID.
  * Reverse lookups can be created where you find a chunk and want to find the parent document or sibling chunks.


## 2. Delete by ID (to avoid delete by metadata filter)

* Identify the `parentId`
  * This could be an internal process to identify documents that have been modified or deleted.
  * Or, this could be a end-user initiated process to delete a document based on a query that finds a sibling chunk or `parentId`.

* Once the `parentId` is identified, use the [`fetch`](/reference/api/2024-10/data-plane/fetch) endpoint to retrieve the `chunkCount` from the metadata field by sending the `parentId-0` vector ID.

* Build a list of IDs using the pattern of `parentId` and `chunkCount`.

* Batch these together and send them to the [`delete`](/reference/api/2024-10/data-plane/delete) endpoint using the IDs of the vectors.

  ```shell  theme={null}
  INDEX_NAME="docs-example"
  PROJECT_ID="example-project-id"

  curl "https://$INDEX_NAME-$PROJECT_ID.svc.environment.pinecone.io/vectors/delete" \
    -H "accept: application/json" \
    -H "content-type: application/json"\
    -H "X-Pinecone-API-Version: 2024-07" \
    -d '
    {
      "deleteAll": "false",
      "ids": [
        "someParentDoc-0",
        "someParentDoc-1",
        "someParentDoc-2"
      ]
    }'
  ```

* You may then [upsert](/reference/api/2024-10/data-plane/upsert) the new version of the document with the new vectors and metadata or if it is a delete-only process, you are finished.


## 3. Updates

* [Updates](/reference/api/2024-10/data-plane/update) are intended to apply small changes to a record whether that means updating the vector, or more commonly, the metadata.
* In cases where you are chunking data, you are more likely going to need to delete and re-upsert using the steps above.
* If you are only performing very small changes to a small number of vectors, the update process is ideal.
* If you are updating a large number of vectors, you may want to consider batching and slowing down the updates to avoid rate limiting or affecting query latency and response times.



# Custom data processing agreements
Source: https://docs.pinecone.io/troubleshooting/custom-data-processing-agreements



If you need a data processing agreement (DPA) with Pinecone you can get started by filling out the form in our [Security Center](https://security.pinecone.io/). You'll need to request access first. Simply click the "Get Access" box on that page and enter your information. You should receive a link with further instructions shortly.



# Debug model vs. Pinecone recall issues
Source: https://docs.pinecone.io/troubleshooting/debug-model-vs-pinecone-recall-issues




## **Step 1: Establish the evaluation framework**

Before starting, establish an evaluation framework for your model and Pinecone recall issues. You will need to query a dataset of at least 10 samples and a source dataset of 100k samples, and choose an evaluation metric that is appropriate for your use case. Pinecone recommends [Evaluation Measures in Information Retrieval](https://www.pinecone.io/learn/offline-evaluation/) as a guide for choosing an evaluation metric. Label the "right answers" in the source dataset for each query.


## **Step 2: Generate embeddings for queries + source dataset with the model**

Use your model to generate embeddings for your queries and the source dataset. Run the model on the source dataset to create the vector dataset and query vectors.


## **Step 3: Calculate brute force vector distance to evaluate model quality**

Run a brute force search using query vectors over the vector dataset via FAISS or numpy and record the record IDs for each query. Evaluate the returned list using your evaluation metric and the set of "right answers" labeled in step 1. If this metric is unacceptable, it indicates a model issue.


## **Step 4: Upload vector dataset to Pinecone + query**

Upload the vector dataset to Pinecone and query it using your queries. Record the vector IDs returned for each query.


## **Step 5: Calculate Pinecone recall**

For each query, compare the % of vector IDs that Pinecone recalled compared to the brute force search. This will be the % recall for each query. You can then average across all queries to get average recall. Typically, average recall should be close to 0.99 for s1/p1 indexes.


## **Step 6: If recall is too low, reach out to Pinecone Support (reproducible dataset and queries)**

If the recall metric is too low for your use case, reach out to Pinecone product and engineering with the query and vector dataset that reproduces the issue for further investigation. Pinecone's team will investigate.



# Delete your account
Source: https://docs.pinecone.io/troubleshooting/delete-your-account



To delete your Pinecone account, you need to remove your user from all organizations and delete any organizations in which you are the sole member.

<Warning>These actions cannot be undone.</Warning>

* [How do I remove myself from an organization?](/guides/organizations/manage-organization-members#remove-a-member)
* [How do I delete an organization?](/troubleshooting/delete-your-organization)

Once you've removed yourself from or deleted all organizations associated with your user, your Pinecone account no longer exists.



# Delete your organization
Source: https://docs.pinecone.io/troubleshooting/delete-your-organization



If you want to delete your Pinecone organization entirely, you'll need to delete all projects, which first requires deleting all indexes and collections, and downgrade to the Starter plan.

* [Delete an index](/guides/manage-data/manage-indexes#delete-an-index)
* [Delete a project](/guides/projects/manage-projects#delete-a-project)
* [Downgrade to the Starter plan](/guides/organizations/manage-billing/downgrade-billing-plan)

Once you've downgraded to the Starter plan and deleted your indexes and projects, you can delete your organization.

<Note>This action cannot be undone.</Note>

1. Go to [Settings > Manage](https://app.pinecone.io/organizations/-/settings/manage) in the Pinecone console.
2. Click **Delete this organization**.
3. Type the organization name and confirm the deletion.



# Differences between Lexical and Semantic Search regarding relevancy
Source: https://docs.pinecone.io/troubleshooting/differences-between-lexical-semantic-search



When it comes to searching for information in a large corpus of text, there are two main approaches that search engines use: keyword or lexical search and vector semantic similarity search. While both methods aim to retrieve relevant documents, they use different techniques to do so.

Keyword or lexical search relies on matching exact words or phrases that appear in a query with those in the documents. This approach is relatively simple and fast, but it has limitations. For example, it may not be able to handle misspellings, synonyms, or polysemy (when a word has multiple meanings). In addition, it does not take into account the context or meaning of the words, which can lead to irrelevant results.

On the other hand, vector semantic similarity search uses natural language processing (NLP) techniques to analyze the meaning of words and their relationships. It represents words as vectors in a high-dimensional space, where the distance between vectors indicates their semantic similarity. This approach can handle misspellings, synonyms, and polysemy, and it can also capture more subtle relationships between words, such as antonyms, hypernyms, and meronyms. As a result, it can produce more accurate and relevant results.

However, there is a caveat to using vector semantic similarity search. It requires a large amount of data to train the NLP models, which can be computationally expensive and time-consuming. As a result, it may not be as effective for short documents or queries that do not contain enough context to determine the meaning of the words. In such cases, a simple keyword or lexical search may be more suitable and effective.

In fact, in some cases, a short document may actually show higher in a vector space for a given query, even if it is not as relevant as a longer document. This is because short documents typically have fewer words, which means that their word vectors are more likely to be closer to the query vector in the high-dimensional space. As a result, they may have a higher cosine similarity score than longer documents, even if they do not contain as much information or context. This phenomenon is known as the "curse of dimensionality" and it can affect the performance of vector semantic similarity search in certain scenarios.

In conclusion, both keyword or lexical search and vector semantic similarity search have their strengths and weaknesses. Depending on the nature of the corpus, the type of queries, and the computational resources available, one approach may be more appropriate than the other. It is important to understand the differences between the two methods and use them judiciously to achieve the best results.



# Embedding values changed when upserted
Source: https://docs.pinecone.io/troubleshooting/embedding-values-changed-when-upserted



There are two distinct cases in which you might notice that the values of your embeddings appear different in Pinecone than the floats you upserted.

If you use a pod-based index with `p2` pods, we use quantization to enable the [Pinecone Graph Algorithm.](https://www.pinecone.io/blog/hnsw-not-enough/#:~:text=built%20vector%20databases.-,The%20Pinecone%20Graph%20Algorithm,-In%20order%20to) This is utilized only in `p2` indexes and powers faster query paths and greater QPS capacities.

For all serverless and other pod-based indexes, you may see slightly different values in Pinecone for high-precision floats. What’s happening here is a result of the fact that fractions can’t be accurately represented in fixed amounts of memory. Different numbers might be mapped to the same bit representation, according to a standard known as [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754). More specifically, at Pinecone, we use Rust’s `f32` type, which is more commonly known as a `float` in Java, C, C++, and Python.

If you take these numbers and look at their physical memory representation, you’ll see that each float maps to the same representation before and after we upsert the vector to Pinecone. Our team built a [small demonstration in Rust](https://play.rust-lang.org/?version=stable\&mode=debug\&edition=2021\&gist=3584c20894714c5cba47127a036678fa) that you can use to explore some examples. We've also included a sample result in the attached screenshot.

This behavior is common across every system in the world, and the general trend in machine learning has been to reduce accuracy even more (see Google’s [bfloat16](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format), which is now also standardized).

<img src="https://mintlify.s3.us-west-1.amazonaws.com/pinecone/troubleshooting/images/float_memory_representation.png" alt="A screenshot of the Rust demonstration, showing that two different floats have the same memory representation in bits." />



# Error: Cannot import name 'Pinecone' from 'pinecone'
Source: https://docs.pinecone.io/troubleshooting/error-cannot-import-name-pinecone




## Problem

When using an older version of the [Python SDK](https://github.com/pinecone-io/pinecone-python-client/blob/main/README.md) (earlier than 3.0.0), trying to import the `Pinecone` class raises the following error:

```console console theme={null}
ImportError: cannot import name 'Pinecone' from 'pinecone'
```


## Solution

Upgrade the SDK version and try again:

```Shell Shell theme={null}

# If you're interacting with Pinecone via HTTP requests, use:
pip install pinecone --upgrade
```

```Shell Shell theme={null}

# If you're interacting with Pinecone via gRPC, use:
pip install "pinecone[grpc]" --upgrade
```



# Error: Handshake read failed when connecting
Source: https://docs.pinecone.io/troubleshooting/error-handshake-read-failed




## Problem

When trying to connect to Pinecone server, some users may receive an error message that says `Handshake read failed` and their connection attempt fails. This error can prevent them from running queries against their Pinecone indexes.


## Solution

If you encounter this error message, it means that your computer is not properly connecting with the Pinecone server. The error is often due to a misconfiguration of your Pinecone client or API key. Here is a recommended solution:

1. Make sure your firewall is not blocking any traffic and your internet connection is working fine. If you are unsure about how to do this, please consult your IT team.
2. Check that you have set up the Pinecone client and API key correctly. Double-check that you have followed the instructions in our [documentation](/guides/get-started/quickstart) correctly.
3. If you are still having issues, try creating a new index on Pinecone and populating it with data by running another script on your computer. This will verify that your computer can access the Pinecone servers for some tasks.
4. If the error persists, you may need to check your code for any misconfigurations. Make sure you are setting up your Pinecone client correctly and passing the right parameters when running queries against your indexes.
5. If you are still unable to resolve the issue, you can reach out to Pinecone support for assistance. They will be able to help you diagnose and resolve the issue.


## Conclusion

If you encounter the `Handshake read failed` error when trying to connect to Pinecone server, there are several steps you can take to resolve the issue. First, double-check that you have set up the Pinecone client and API key correctly. Then, check for any misconfigurations in your code. If the error persists, [contact Pinecone Support](/troubleshooting/contact-support) for assistance.



# Export indexes
Source: https://docs.pinecone.io/troubleshooting/export-indexes



Pinecone does not support an export function. It is on our roadmap for the future, however.

In the meantime, we recommend keeping a copy of your source data in case you need to move from one project to another, in which case you'll need to reindex the data.

For backup purposes, we recommend that you take periodic backups. Please see [Back up indexes](/guides/manage-data/back-up-an-index) in our documentation for more details on doing so.



# How to work with Support
Source: https://docs.pinecone.io/troubleshooting/how-to-work-with-support



There are several best practices for working with Pinecone Support that can lead to faster resolutions and more relevant recommendations. Please note that Pinecone Support is reserved for users in organizations on the Standard or Enterprise plan. First-response SLAs only apply to tickets created by users in an organization subscribed to a [support plan](https://www.pinecone.io/pricing/?plans=support). To upgrade your support plan, go to [Manage your support plan](https://app.pinecone.io/organizations/-/settings/support/plans) in the console and select your desired plan.


## Utilize Pinecone AI Support

Our [support chatbot](https://app.pinecone.io/organizations/-/settings/support) is knowledgeable of our documentation, troubleshooting articles, website and more. Many of your questions can be answered immediately using this resource. We also review all interactions with the support chatbot and constantly make improvements.


## Use the email associated with your Pinecone account

We map your account information to the tier of your organization to assign appropriate SLAs. If you open tickets using an email not associated with your Pinecone account, we will close your request and suggest alternative contact methods.


## Create tickets using the support portal

Instead of creating tickets via email, use the [Help center](https://app.pinecone.io/organizations/-/settings/support) in the Pinecone console to create tickets. The form allows you to provide helpful information such as severity and category. Furthermore, the conversation format will be much more digestible in the portal, especially when involving code snippets and other attachments.


## Select an appropriate severity

Pinecone Support reserves the right to change the ticket severity after our initial response and assessment of the case. Note that a Sev-1 ticket indicates that your production environment is completely unavailable, and a Sev-2 ticket indicates that your production environment has degraded performance. If your issue does not involve a production-level usage or application, please refrain from opening Sev-1 or Sev-2 tickets.


## Provide the exact names of impacted indexes and projects

When opening a ticket that involves specific resources in your organization, please specify the name of the impacted index(es) and project(s).


## Provide as detailed a description as possible

Please include code snippets, version specifications, and the full stack trace of error messages you encounter. Whenever possible, please include screenshots or screen recordings. The more information you provide, the more likely we can effectively assist you in our first response, and you can return to building with Pinecone.



# Serverless index creation error - max serverless indexes
Source: https://docs.pinecone.io/troubleshooting/index-creation-error-max-serverless




## Problem

Each project is limited to 20 serverless indexes. Trying to create more than 20 serverless indexes in a project raises the following `403 (FORBIDDEN)` error:

```console console theme={null}
This project already contains 20 serverless indexes, the maximum per project. 
Delete any unused indexes and try again, or create a new project for more serverless indexes. 
For additional help, please contact support@pinecone.io.
```


## Solution

[Delete any unused serverless indexes](/guides/manage-data/manage-indexes#delete-an-index) in the project and try again, or create a new project to hold additional serverless indexes.

Also consider using [namespaces](/guides/index-data/indexing-overview#namespaces) to partition vectors of the same dimensionality within a single index. Namespaces can help speed up queries as well as comply with [multitenancy](/guides/index-data/implement-multitenancy) requirements.



# Index creation error - missing spec parameter
Source: https://docs.pinecone.io/troubleshooting/index-creation-error-missing-spec




## Problem

Using the [new API](/reference/api), creating an index requires passing appropriate values into the `spec` parameter. Without this `spec` parameter, the `create_index` method raises the following error:

```console console theme={null}
TypeError: Pinecone.create_index() missing 1 required positional argument: 'spec'
```


## Solution

Set the `spec` parameter. For guidance on how to set this parameter, see [Create an index](/guides/index-data/create-an-index#create-a-serverless-index).



# Keep customer data separate in Pinecone
Source: https://docs.pinecone.io/troubleshooting/keep-customer-data-separate



Some use cases require vectors to be segmented by their customers, either physically or logically. The table below describes three techniques to accomplish this and the pros and cons of considering each:

| **Techniques**                                                                                                    | **Pros**                                                                                                                                                                         | **Cons**                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Separate Indexes**<br />Each customer would have a separate index                                               | • Customer data is truly separated physically by indexes                                                                                                                         | • You cannot query across customers if you wish<br />• Cost and maintenance of several indexes |
| **Namespaces**<br />You can isolate data within a single index using namespaces                                   | • You can only query one namespace at a time, which would keep customer data separate logically<br />• Cheaper than #1 potentially by making more efficient use of index storage | • You cannot query across namespaces<br />• Customer data is only separated logically          |
| **Metadata Filtering**<br />All data is kept in a single index and logically separated by filtering at query time | • Most versatile if you wish to query across customers<br />• As with namespaces cheaper than #1 potentially                                                                     | • Customer data is separated only by filtering at query time                                   |



# Limitations of querying by ID
Source: https://docs.pinecone.io/troubleshooting/limitations-of-querying-by-id



When [querying by record ID](/guides/search/semantic-search#search-with-a-record-id), even with a high `topK`, the response is not guaranteed to include the record with the specified ID.


## Approximate nearest neighbor (ANN)

Approximate nearest neighbor algorithms are designed to quickly find the closest matches to a given data point within large datasets with reasonable accuracy rather than perfect precision. Depending on the data, ANN may have a slightly lower accuracy than Known Nearest Neighbor (KNN) algorithms, but will have significantly lower read costs and latency than KNN. This is one of the key features of ANN.

ANN algorithms assess broad data clusters to find matches. Some of these clusters might be ignored even if they contain relevant records simply because their overall similarity to the query is lower, because the algorithm aims to optimize the search by focusing on areas with a higher density of potential matches.

See our learning center for more information on [ANN algorithms](https://www.pinecone.io/learn/a-developers-guide-to-ann-algorithms/).


## Recommendations

### Perform a fetch instead of a query

Results from [Fetch](/guides/manage-data/fetch-data) are guaranteed to include the record with the specified ID.

### Use metadata filtering

A [metadata filter](/guides/index-data/indexing-overview#metadata) in an ANN search effectively narrows the dataset to a more relevant subset, fine-tuning the search process. By explicitly excluding less relevant clusters from the outset, the search is performed among a group of records more closely related to the query, thereby increasing the efficiency and accuracy of the search.



# Login code issues
Source: https://docs.pinecone.io/troubleshooting/login-code-issues



If the email token you received from Pinecone is not accepted when logging in there may be a few different reasons why:


## The code has expired

A code is only valid for 10 hours, so if you enter it after that time it will no longer be accepted.


## The code has already been used

If you're using a shared email account or distribution list, please check with your teammates to see if anyone else has used your code.


## A subsequent request was made

Similar to the first reason, if you're using a shared account, it's possible that someone else requested a code after you did, rendering the first code invalid.


## Your computer's system clock time is offset

User authentication with a verification code relies on your device’s system clock to verify the time. If your computer’s clock is more than 10 minutes off from your time zone, the login will fail. If you see the below error message, please set your system clock to the correct time and time zone before trying again.

```
Please check your computer's system clock time. See https://docs.pinecone.io/troubleshooting/login-code-issues for more information.
```


## Your anti-spam filter followed the links in the email to check their validity

If your anti-spam filter followed the links in the email to check their validity, and one of them submitted the code as part of the URL, please check with your anti-spam system admin or vendor to see if this might be the cause.



# Minimize latencies
Source: https://docs.pinecone.io/troubleshooting/minimize-latencies



There are many aspects to consider to minimize latencies:


## Slow uploads or high latencies

To minimize latency when accessing Pinecone:

* Switch to a cloud environment. For example: EC2, GCE, [Google Colab](https://colab.research.google.com), [GCP AI Platform Notebook](https://cloud.google.com/ai-platform-notebooks), or [SageMaker Notebook](https://docs.aws.amazon.com/sagemaker/dg/nbi.html). If you experience slow uploads or high query latencies, it might be because you are accessing Pinecone from your home network.
* Consider deploying your application in the same environment as your Pinecone service.
* See [Decrease latency](/guides/optimize/decrease-latency) for more tips.


## High query latencies with batching

If you're batching queries, try reducing the number of queries per call to 1 query vector. You can make these [calls in parallel](/troubleshooting/parallel-queries) and expect roughly the same performance as with batching.



# Python AttributeError: module pinecone has no attribute init
Source: https://docs.pinecone.io/troubleshooting/module-pinecone-has-no-attribute-init




## Problem

If you are using Pinecone serverless and getting the error `"AttributeError: module 'pinecone' has no attribute 'init'`, first check that you are using the latest version of the Python SDK.

You can check the version of the client by running:

```shell  theme={null}
pip show pinecone
```


## Solution

Serverless requires a minimum version of 3.0. To upgrade to the latest version, run:

```shell  theme={null}

# If you're interacting with Pinecone via HTTP:
pip install pinecone --upgrade


# If you're using gRPC:

# pip install "pinecone[grpc]" --upgrade
```

If you're on the right version and getting this error, you just have to make some slight changes to your code to make use of serverless. Instead of calling:

```python  theme={null}
import pinecone

pinecone.init(api_key=api_key,environment=environment)
```

Use the following if you're interacting with Pinecone via HTTP requests:

```python  theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key=api_key)
```

Or, use the following if you're using gRPC:

```python  theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key=api_key)
```

You no longer need to specify the cloud environment your index is hosted in; the API key is all you need.



# Node.js Troubleshooting
Source: https://docs.pinecone.io/troubleshooting/nodejs-troubleshooting



There could be several reasons why a [Node.js application](/reference/node-sdk) works in development mode but not in deployment.

In order to troubleshoot the issue, it's important to identify where the application is failing and compare the development and deployment environments to see what differences exist. It's also important to review any error messages or logs that are generated to help identify the issue.

You may also reach out to our [community of Pinecone users](https://community.pinecone.io) for help.

Here are a few aspects to troubleshoot:


## Dependency version mismatch

Sometimes, different environments have different versions of dependencies installed. If the application was developed using a specific version of a dependency, and that version is not installed on the deployment environment, the application may not work as expected.


## Environment configuration

The development environment may have different configurations from the deployment environment. For example, the development environment may have different environment variables set or different network settings. If the application relies on specific configuration settings that are not present in the deployment environment, it may not work.


## Permissions

The application may require permissions to access certain resources that are only granted in the development environment. For example, if the application needs to write to a specific directory, the permissions to write to that directory may only be granted in the development environment.


## Database connection

If the application relies on a database connection, it's possible that the connection settings are different in the deployment environment. For example, the database may have a different hostname or port number.


## Code optimization

During development, the application may have been running on a development server that did not optimize the code. However, when deployed, the application may be running on a production server that is optimized for performance. If there are code issues or performance bottlenecks, they may only appear when the application is deployed.


## Install fetch

It may be necessary to install the `fetch` Python library for compatibility with node.js.



# Parallel queries
Source: https://docs.pinecone.io/troubleshooting/parallel-queries



There are many approaches to perform parallel queries in your application, from using the Python SDK to making REST calls. Below is one example of an approach using multi-threaded, asynchronous requests in Python. For guidance on using `asyncio` for single-threaded, asynchronous requests in Python, see [Asyncio support](/reference/python-sdk#asyncio-support).

This example assumes the following:

* You have a 1536-dimension serverless index called `docs-example`.
* You have the [Pinecone Python SDK](/reference/python-sdk) and [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) and [`numpy`](https://numpy.org/) packages installed.

```python  theme={null}
import os
from pinecone import Pinecone
from concurrent.futures import ThreadPoolExecutor


# Get the API key from the environment variable and initialize Pinecone
api_key = os.environ.get("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)


# Define the index name
index_name = "docs-example"


# Define the index
index = pc.Index(index_name)


# Define the function to run parallel queries
def run_parallel_queries(vectors):
    """
    Run a list of vectors in parallel using ThreadPoolExecutor.
    
    Parameters:
    vectors (list): A list of vectors.
    
    Returns:
    list: A list of query results.
    """
    
    # Define the maximum number of concurrent queries
    MAX_CONCURRENT_QUERIES = 4

    def run_query(vector):
        """
        Run a single query.
        """
        return index.query(
            namespace="",
            vector=vector,
            top_k=3,
            include_values=True
        )
    
    # Run the queries in parallel
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_QUERIES) as executor:
        """
        Run the queries in parallel.
        """
        results = list(executor.map(run_query, vectors))
    
    return results

def test_parallel_queries():
    """
    Test the run_parallel_queries function with 20 random vectors.
    """
    import numpy as np

    # Generate 20 random vectors of size 1536 and convert them to lists
    vectors = [np.random.rand(1536).tolist() for _ in range(20)]

    # Define the batch size
    QUERY_BATCH_SIZE = 20
    
    # Run the parallel queries
    results = run_parallel_queries(vectors)

    # Print the results
    for i, result in enumerate(results):
        print(f"Query {i+1} results: {result}")

if __name__ == "__main__":
    test_parallel_queries()
```



# PineconeAttribute errors with LangChain
Source: https://docs.pinecone.io/troubleshooting/pinecone-attribute-errors-with-langchain




## Problem

When using an outdated version of LangChain, you may encounter errors like the following:

```console  theme={null}
Pinecone has no attribute 'from_texts'
```

```console  theme={null}
Pinecone has no attribute `from_documents'
```


## Solution

Previously, the Python classes for both LangChain and Pinecone had objects named `Pinecone`, but this is no longer an issue in the latest LangChain version. To resolve these errors, upgrade LangChain to >=0.0.3:

```shell  theme={null}
pip install --upgrade langchain-pinecone
```

Depending on which version of LangChain you are upgrading from, you may need to update your code. You can find more information about using LangChain with Pinecone in our [documentation](/integrations/langchain#4-initialize-a-langchain-vector-store).



# Pinecone Support SLAs
Source: https://docs.pinecone.io/troubleshooting/pinecone-support-slas



<Note>
  New first-response SLAs went into effect on September 16th, 2024. See the [pricing page](https://www.pinecone.io/pricing/?plans=support) for more details.
</Note>

Pinecone Support has first-response SLAs based on the support plan of the ticket requester's organization and the selected severity. These SLAs are as follows:

### Premium

* **Sev-1**: 30 minutes
* **Sev-2**: 2 business hours
* **Sev-3**: 8 business hours
* **Sev-4**: 12 business hours

### Pro

* **Sev-1**: 2 hours
* **Sev-2**: 4 business hours
* **Sev-3**: 12 business hours
* **Sev-4**: 2 business days

### Developer

* **Sev-1**: 8 business hours
* **Sev-2**: 12 business hours
* **Sev-3**: 2 business days
* **Sev-4**: 3 business days

The current business hours for Pinecone Support are 8 AM to 8 PM Eastern Time. SLAs only apply outside of our business hours for Sev-1 tickets created by users subscribed to Pro or Premium support. All first-response SLAs only apply to tickets created by users in an organization subscribed to a [support plan](https://www.pinecone.io/pricing/?plans=support).

Pinecone Support is reserved for customers on the Standard billing plan. However, you may find helpful resources on our [community page](https://community.pinecone.io). This is a great place to ask questions and find answers from other Pinecone users and our community moderators.



# Remove a metadata field from a record
Source: https://docs.pinecone.io/troubleshooting/remove-metadata-field



You must perform an [`upsert`](/reference/api/2024-10/data-plane/upsert) operation to remove existing metadata fields from a record.

You will need to provide the existing ID and values of the vector. The metadata you provide in the upsert operation will replace any existing metadata, thus clearing the fields you seek to drop.

Metadata fields cannot be removed using the `update` operation.



# Restrictions on index names
Source: https://docs.pinecone.io/troubleshooting/restrictions-on-index-names



There are two main restrictions on index names in Pinecone: **character restrictions** and a **maximum length**.


## Character restrictions

Index names can only use UTF-8 lowercase alphanumeric Latin characters and dashes. Non-Latin characters (such as Chinese or Cyrillic) and emojis are not supported. Additionally, they cannot contain dots, as these are used to separate hosts and subnets in DNS, which Pinecone uses to route requests and queries.


## Maximum length

The maximum length of your index name is a factor of limits imposed by the infrastructure Pinecone uses behind the scenes. The combination of your index name and project ID (normally a seven-character, alphanumeric string) cannot exceed 52 characters, plus a dash to separate them. Your project ID is different from your project name, which is often longer than seven characters. You can identify your project ID by the hostname used to connect to your index; it's the last set of characters after the final `-`. For example, if your index is `foo` and your project ID is `abc1234` in the `us-east1-gcp` environment, your index's hostname would be `foo-abc1234.svc.us-east1-gcp.pinecone.io`, and its length would be 11 characters (3 for the index name, 1 for the dash, 7 for the project ID).



# Return all vectors in an index
Source: https://docs.pinecone.io/troubleshooting/return-all-vectors-in-an-index



Pinecone is designed to find vectors that are similar to a given set of conditions, either by comparing a new vector to the ones in the index or by comparing a vector in the index to all of the others using the [query by ID feature](/reference/api/2024-10/data-plane/query). Because the Pinecone query function relies on performing this similarity search, there isn't a way to return all of the vectors currently stored in the index with a single query.

There isn't a guaranteed workaround for this type of query today but providing the ability to query all or export the entire index is on our roadmap for the future.



# Serverless index connection errors
Source: https://docs.pinecone.io/troubleshooting/serverless-index-connection-errors




## Problem

To connect to a serverless index, you must use an updated Pinecone client. Trying to connect to a serverless index with an outdated client will raise errors similar to one of the following:

```console console theme={null}
Failed to resolve 'controller.us-west-2.pinecone.io'

controller.us-west-2-aws.pinecone.io not found

Request failed to reach Pinecone while calling https://controller.us-west-2.pinecone.io/actions/whoami
```


## Solution

Upgrade to the latest [Python](https://github.com/pinecone-io/pinecone-python-client/blob/main/README.md) or [Node.js](https://sdk.pinecone.io/typescript/) client and try again:

<CodeGroup>
  ```python Python theme={null}
  pip install "pinecone[grpc]" --upgrade
  ```

  ```js JavaScript theme={null}
  npm install @pinecone-database/pinecone@latest
  ```
</CodeGroup>



# Unable to pip install
Source: https://docs.pinecone.io/troubleshooting/unable-to-pip-install



Python `3.x` uses `pip3`. Use the following commands in your terminal to install the latest version of the [Pinecone Python SDK](/reference/python-sdk):

```Shell Shell theme={null}

# If you are connecting to Pinecone via gRPC:
pip3 install -U pinecone[grpc]
```

```Shell Shell theme={null}

# If you are connecting to Pinecone via HTTP:
pip3 install -U pinecone
```



# Wait for index creation to be complete
Source: https://docs.pinecone.io/troubleshooting/wait-for-index-creation



Pinecone index creation involves several different subsystems, including one which accepts the job of creating the index and one that actually performs the action. The Python SDK and the REST API are designed to interact with the first system during index creation but not the second.

This means that when a request call to [`create_index()`](/reference/api/latest/control-plane/create_index) is made, what's actually happening is that the job is being submitted to the queue to be completed. We do it this way for several reasons, including enforcing separation between the control and data planes.

If you need your application to wait for the index to be created before continuing to its next step, there is a way to ensure this happens, though. [`describe_index()`](/reference/api/latest/control-plane/describe_index) returns data about the state of the index, including whether it is ready to accept data. You simply call that method until it returns a 200 status code and the status object reports that the index is ready. Because the return is a tuple, we just have to access the slice containing the status object and check the boolean state of the ready variable. This is one possible method of doing so using the Python SDK:

```python  theme={null}
import pinecone
from time import sleep

def wait_on_index(index: str):
  """
  Takes the name of the index to wait for and blocks until it's available and ready.
  """
  ready = False
  while not ready:
    try:
      desc = pinecone.describe_index(index)
      if desc[7]['ready']:
        return True
    except pinecone.core.client.exceptions.NotFoundException:
      # NotFoundException means the index is created yet.
      pass
    sleep(5)
```

Calling `wait_on_index()` would then allow your application to only continue to upsert data once the index is fully online and available to accept data, avoiding potential 403 or 404 errors.



# 2022 releases
Source: https://docs.pinecone.io/assistant-release-notes/2022




## December 22, 2022

#### Pinecone is now available in Google Cloud Marketplace

You can now [sign up for Pinecone billing through Google Cloud Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).


## December 6, 2022

#### Organizations are generally available

Pinecone now features [organizations](/guides/organizations/understanding-organizations), which allow one or more users to control billing and project settings across multiple projects owned by the same organization.

#### p2 pod type is generally available

The [p2 pod type](/guides/index-data/indexing-overview#p2-pods) is now generally available and ready for production workloads. p2 pods are now available in the Starter plan and support the [dotproduct distance metric](/guides/index-data/create-an-index#dotproduct).

#### Performance improvements

* [Bulk vector\_deletes](/guides/index-data/upsert-data/#deleting-vectors) are now up to 10x faster in many circumstances.
* [Creating collections](/guides/manage-data/back-up-an-index) is now faster.


## October 31, 2022

#### Hybrid search (Early access)

Pinecone now supports keyword-aware semantic search with the new hybrid search indexes and endpoints. Hybrid search enables improved relevance for semantic search results by combining them with keyword search.

This is an **early access** feature and is available only by [signing up](https://www.pinecone.io/hybrid-search-early-access/).


## October 17, 2022

#### Status page

The new [Pinecone Status Page](https://status.pinecone.io/) displays information about the status of the Pinecone service, including the status of individual cloud regions and a log of recent incidents.


## September 16, 2022

#### Public collections

You can now create indexes from public collections, which are collections containing public data from real-world data sources. Currently, public collections include the Glue - SSTB collection, the TREC Question classification collection, and the SQuAD collection.


## August 16, 2022

#### Collections (Public preview)("Beta")

You can now \[make static copies of your index]\(/guides/manage-data/back-up-an-index using collections]\(/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections). After you create a collection from an index, you can create a new index from that collection. The new index can use any pod type and any number of pods. Collections only consume storage.

This is a **public preview** feature and is not appropriate for production workloads.

#### Vertical scaling

You can now [change the size of the pods](/guides/indexes/pods/scale-pod-based-indexes#increase-pod-size) for a live index to accommodate more vectors or queries without interrupting reads or writes. The p1 and s1 pod types are now available in [4 different sizes](/guides/index-data/indexing-overview/#pods-pod-types-and-pod-sizes): `1x`, `2x`, `4x`, and `8x`. Capacity and compute per pod double with each size increment.

#### p2 pod type (Public preview)("Beta")

The new [p2 pod type](/guides/index-data/indexing-overview/#p2-pods) provides search speeds of around 5ms and throughput of 200 queries per second per replica, or approximately 10x faster speeds and higher throughput than the p1 pod type, depending on your data and network conditions.

This is a **public preview** feature and is not appropriate for production workloads.

#### Improved p1 and s1 performance

The [s1](/guides/index-data/indexing-overview/#s1-pods) and [p1](/guides/index-data/indexing-overview/#p1-pods) pod types now offer approximately 50% higher query throughput and 50% lower latency, depending on your workload.


## July 26, 2022

You can now specify a [metadata filter](/guides/index-data/indexing-overview#metadata/) to get results for a subset of the vectors in your index by calling [describe\_index\_stats](/reference/api/2024-07/control-plane/describe_index) with a [filter](/reference/api/2024-07/control-plane/describe_index#!path=filter\&t=request) object.

The `describe_index_stats` operation now uses the `POST` HTTP request type. The `filter` parameter is only accepted by `describe_index_stats` calls using the `POST` request type. Calls to `describe_index_stats` using the `GET` request type are now deprecated.


## July 12, 2022

#### Pinecone Console Guided Tour

You can now choose to follow a guided tour in the [Pinecone console](https://app.pinecone.io). This interactive tutorial walks you through creating your first index, upserting vectors, and querying your data. The purpose of the tour is to show you all the steps you need to start your first project in Pinecone.


## June 24, 2022

#### Updated response codes

The [create\_index](/reference/api/2024-07/control-plane/create_index), [delete\_index](/reference/api/2024-07/control-plane/delete_index), and `scale_index` operations now use more specific HTTP response codes that describe the type of operation that succeeded.


## June 7, 2022

#### Selective metadata indexing

You can now store more metadata and more unique metadata values! [Select which metadata fields you want to index for filtering](/guides/indexes/pods/manage-pod-based-indexes#selective-metadata-indexing) and which fields you only wish to store and retrieve. When you index metadata fields, you can filter vector search queries using those fields. When you store metadata fields without indexing them, you keep memory utilization low, especially when you have many unique metadata values, and therefore can fit more vectors per pod.

#### Single-vector queries

You can now [specify a single query vector using the vector input](/reference/api/2024-07/data-plane/query/#!path=vector\&t=request). We now encourage all users to query using a single vector rather than a batch of vectors, because batching queries can lead to long response messages and query times, and single queries execute just as fast on the server side.

#### Query by ID

You can now [query your Pinecone index using only the ID for another vector](/reference/api/2024-07/data-plane/query/#!path=id\&t=request). This is useful when you want to search for the nearest neighbors of a vector that is already stored in Pinecone.

#### Improved index fullness accuracy

The index fullness metric in [describe\_index\_stats()](/reference/api/2024-07/control-plane/describe_index#!c=200\&path=indexFullness\&t=response) results is now more accurate.


## April 25, 2022

#### Partial updates (Public preview)

You can now perform a partial update by ID and individual value pairs. This allows you to update individual metadata fields without having to upsert a matching vector or update all metadata fields at once.

#### New metrics

Users on all plans can now see metrics for the past one (1) week in the Pinecone console. Users on the Enterprise plan now have access to the following metrics via the [Prometheus metrics endpoint](/guides/production/monitoring/):

* `pinecone_vector_count`
* `pinecone_request_count_total`
* `pinecone_request_error_count_total`
* `pinecone_request_latency_seconds`
* `pinecone_index_fullness` (Public preview)

**Note:** The accuracy of the `pinecone_index_fullness` metric is improved. This may result in changes from historic reported values. This metric is in public preview.

#### Spark Connector

Spark users who want to manage parallel upserts into Pinecone can now use the [official Spark connector for Pinecone](https://github.com/pinecone-io/spark-pinecone#readme) to upsert their data from a Spark dataframe.

#### Support for Boolean and float metadata in Pinecone indexes

You can now add `Boolean` and `float64` values to [metadata JSON objects associated with a Pinecone index.](/guides/index-data/indexing-overview#metadata)

#### New state field in describe\_index results

The [describe\_index](/reference/api/2024-07/control-plane/describe_index/) operation results now contain a value for `state`, which describes the state of the index. The possible values for `state` are `Initializing`, `ScalingUp`, `ScalingDown`, `Terminating`, and `Ready`.

##### Delete by metadata filter

The [Delete](/reference/api/2024-07/data-plane/delete/) operation now supports filtering my metadata.



# 2023 releases
Source: https://docs.pinecone.io/assistant-release-notes/2023




## December 2023

### Features

* The free Starter plan now supports up to 100 namespaces. [Namespaces](/guides/index-data/indexing-overview#namespaces) let you partition vectors within an index to speed up queries or comply with [multitenancy](/guides/index-data/implement-multitenancy) requirements.


## November 2023

### Features

* The new [Pinecone AWS Reference Architecture](https://github.com/pinecone-io/aws-reference-architecture-pulumi/tree/main) is an open-source, distributed system that performs vector-database-enabled semantic search over Postgres records. You can use it as a learning resource or as a starting point for high-scale use cases.

### SDKs

* [Canopy](https://github.com/pinecone-io/canopy/blob/main/README.md) is a new open-source Retrieval Augmented Generation (RAG) framework and context engine built on top of Pinecone. It enables you to start chatting with your documents or text data with a few simple commands.\
  The latest version of the Canopy SDK (v0.2.0) adds support for OpenAI SDK v1.2.3. See the [release notes](https://github.com/pinecone-io/canopy/releases/tag/V0.2.0) in GitHub for more details.

### Billing

* Pinecone is now registered to collect Value Added Tax (VAT) or Goods and Services Tax (GST) for accounts based in various global regions. If applicable, add your VAT or GST number to your account under **Settings > Billing**.

### October 2023

### Features

* [Collections](/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections) are now generally available (GA).

### Regions

* Pinecone Azure support via the [‘eastus-azure\` region](/guides/projects/understanding-projects#project-environments) is now generally available (GA).

### SDKs

* The latest version of our Node SDK is v1.1.2. See the [release notes](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v1.1.2) in GitHub for more details.

### Console

* The Index Browser is now available in the console. This allows you to preview, query, and filter by metadata directly from the console. The Index Browser can be found within the index detail page.
* We’re improved the design of our metrics page to include new charts for record and error count plus additional latencies (p90, p99) to help triage and understand issues.

### Integrations

* Knowledge Base for Amazon Bedrock is now available in private preview. Integrate your enterprise data via retrieval augmented generation (RAG) when building search and GenAI applications. [Learn more](https://www.pinecone.io/blog/amazon-bedrock-integration/).
* Pinecone Sink Connector for Confluent is now available in public preview. Gain access to data streams from across your business to build a real-time knowledge base for your AI applications. [Learn more](https://www.pinecone.io/confluent-integration).

### Billing

* You can now [sign up for Pinecone billing through Microsoft Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).

### Privacy

* Pinecone is now HIPAA compliant across all of our cloud providers (AWS, Azure, and GCP).


## September 11, 2023

Pinecone Azure support via the [eastus-azure region](/guides/projects/understanding-projects#project-environments) is now generally available (GA).


## August 14, 2023

Pinecone now supports deploying projects to Azure using the new [eastus-azure region](/guides/projects/understanding-projects#project-environments). This is a public preview environment, so test thoroughly before deploying to production.


## June 21, 2023

The new `gcp-starter` region is now in public preview. This region has distinct limitations from other Starter Plan regions. `gcp-starter` is the default region for some new users.


## April 26, 2023

[Indexes in the starter plan](/guides/index-data/indexing-overview#starter-plan) now support approximately 100,000 1536-dimensional embeddings with metadata. Capacity is proportional for other dimensionalities.


## April 3, 2023

Pinecone now supports [new US and EU cloud regions](/guides/projects/understanding-projects#project-environments).


## March 21, 2023

Pinecone now supports SSO on some Enterprise plans. [Contact Support](https://app.pinecone.io/organizations/-/settings/support) to set up your integration.


## March 1, 2023

Pinecone now supports [40kb of metadata per vector](/guides/index-data/indexing-overview#metadata#supported-metadata-size).


## February 22, 2023

#### Sparse-dense embeddings are now in public preview.

Pinecone now supports [vectors with sparse and dense values](/guides/search/hybrid-search#use-a-single-hybrid-index). To use sparse-dense embeddings in Python, upgrade to Python SDK version 2.2.0.

#### Pinecone Python SDK version 2.2.0 is available

Python SDK version 2.2.0 with support for sparse-dense embeddings is now available on [GitHub](https://github.com/pinecone-io/pinecone-python-client) and [PYPI](https://pypi.org/project/pinecone-client/2.2.0/).


## February 15, 2023

#### New Node.js SDK is now available in public preview

You can now try out our new [Node.js SDK for Pinecone](https://sdk.pinecone.io/typescript/).


## February 14, 2023

#### New usage reports in the Pinecone console

You can now monitor your current and projected Pinecone usage with the [**Usage** dashboard](/guides/manage-cost/monitor-usage-and-costs).


## January 31, 2023

#### Pinecone is now available in AWS Marketplace

You can now [sign up for Pinecone billing through Amazon Web Services Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).


## January 3, 2023

#### Pinecone Python SDK version 2.1.0 is now available on GitHub.

The [latest release of the Python SDK](https://github.com/pinecone-io/pinecone-python-client/releases/tag/2.1.0) makes the following changes:

* Fixes "Connection Reset by peer" error after long idle periods
* Adds typing and explicit names for arguments in all client operations
* Adds docstrings to all client operations
* Adds Support for batch upserts by passing `batch_size` to the upsert method
* Improves gRPC query results parsing performance



# 2024 releases
Source: https://docs.pinecone.io/assistant-release-notes/2024




## December 2024

<Update label="2024-12-23" tags={["Database"]}>
  ### Increased namespaces limit

  Customers on the [Standard plan](https://www.pinecone.io/pricing/) can now have up to 25,000 namespaces per index.
</Update>

<Update label="2024-12-19" tags={["Assistant"]}>
  ### Pinecone Assistant JSON mode and EU region deployment

  Pinecone Assistant can now [return a JSON response](/guides/assistant/chat-with-assistant#json-response).

  ***

  You can now [create an assistant](/reference/api/2025-01/assistant/create_assistant) in the `eu` region.
</Update>

<Update label="2024-12-17" tags={["Database"]}>
  ### Released Spark-Pinecone connector v1.2.0

  Released [`v1.2.0`](https://github.com/pinecone-io/spark-pinecone/releases/tag/v1.2.0) of the [Spark-Pinecone connector](/reference/tools/pinecone-spark-connector). This version introduces support for stream upserts with structured streaming. This enhancement allows users to seamlessly stream data into Pinecone for upsert operations.
</Update>

<Update label="2024-12-10" tags={["Docs"]}>
  ### New integration with HoneyHive

  Added the [HoneyHive](/integrations/honeyhive) integration page.
</Update>

<Update label="2024-12-09" tags={["SDK"]}>
  ### Released Python SDK v5.4.2

  Released [`v5.4.2`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.4.2) of the [Pinecone Python SDK](/reference/python-sdk). This release adds a required keyword argument, `metric`, to the `query_namespaces` method. This change enables the SDK to merge results no matter how many results are returned.
</Update>

<Update label="2024-12-06" tags={["General"]}>
  <img className="block max-w-full" noZoom src="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=3155e298e3d3636631238d3b3ac05a9f" data-og-width="2038" width="2038" data-og-height="1050" height="1050" data-path="images/release-notes/launch-week.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=280&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=36944215c7e424e0c03bdbffc71be67a 280w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=560&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=020d85488acfadd9554e2ae19e975fdf 560w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=840&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6b7e05cd22f72c3afb3e01c8ab37d11f 840w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=1100&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=e195d61caa0cd69d12339738d532225d 1100w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=1650&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=32e430d71f4226fc3045bd2dff063ac9 1650w, https://mintcdn.com/pinecone/r0TaYXrfSrAYZYUj/images/release-notes/launch-week.png?w=2500&fit=max&auto=format&n=r0TaYXrfSrAYZYUj&q=85&s=6267312f97e819865dfa7db6ce869cdd 2500w" />

  ### Launch week: Pinecone Local

  Pinecone now offers Pinecone Local, an in-memory database emulator available as a Docker image. You can use Pinecone Local to [develop your applications locally](/guides/operations/local-development), or to [test your applications in CI/CD](/guides/production/automated-testing), without connecting to your Pinecone account, affecting production data, or incurring any usage or storage fees. Pinecone Local is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-12-05" tags={["General"]}>
  ### Launch week: Enhanced security and access controls

  Support for [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) is now in [public preview](/release-notes/feature-availability).

  ***

  You can now [change API key permissions](/guides/projects/manage-api-keys#update-an-api-key).

  ***

  Private Endpoints are now in [general availability](/release-notes/feature-availability). Use Private Endpoints to [connect AWS PrivateLink](/guides/production/connect-to-aws-privatelink) to Pinecone while keeping your VPC private from the public internet.

  ***

  [Audit logs](/guides/production/security-overview#audit-logs), now in early access, provide a detailed record of user and API actions that occur within the Pinecone platform.
</Update>

<Update label="2024-12-04" tags={["Database"]}>
  ### Launch week: `pinecone-rerank-v0` and `cohere-rerank-3.5` on Pinecone Inference

  Released [`pinecone-rerank-v0`](/guides/search/rerank-results#pinecone-rerank-v0), Pinecone's state of the art reranking model that out-performs competitors on widely accepted benchmarks. This model is in [public preview](/release-notes/feature-availability).

  ***

  Pinecone Inference now hosts [`cohere-rerank-3.5`](/guides/search/rerank-results#cohere-rerank-3.5), Cohere's leading reranking model.
</Update>

<Update label="2024-12-03" tags={["Database"]}>
  ### Launch week: Integrated Inference

  You can now use [embedding models](/guides/index-data/create-an-index#embedding-models) and [reranking models](/guides/search/rerank-results#reranking-models) hosted on Pinecone as an integrated part of upserting and searching.
</Update>

<Update label="2024-12-05" tags={["SDK"]}>
  ### Released .NET SDK v2.1.0

  Released [`v2.1.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/2.1.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version adds support for [index tags](/guides/manage-data/manage-indexes#configure-index-tags) and introduces the `ClientOptions.IsTlsEnabled` property, which must be set to `false` for non-secure client connections.
</Update>

<Update label="2024-12-05" tags={["Docs"]}>
  ### Improved batch deletion guidance

  Improved the guidance and example code for [deleting records in batches](/guides/manage-data/delete-data#delete-records-in-batches).
</Update>

<Update label="2024-12-02" tags={["Database"]}>
  ### Launch week: Released `pinecone-sparse-english-v0`

  Pinecone Inference now supports [`pinecone-sparse-english-v0`](/guides/search/rerank-results#pinecone-sparse-english-v0), Pinecone's sparse embedding model, which estimates the lexical importance of tokens by leveraging their context, unlike traditional retrieval models like BM25, which rely solely on term frequency. This model is in [public preview](/release-notes/feature-availability).
</Update>


## November 2024

<Update label="2024-11-30" tags={["Docs"]}>
  ### Pinecone docs: New workflows and best practices

  Added typical [Pinecone Database and Pinecone Assistant workflows](/guides/get-started/overview) to the Docs landing page.

  ***

  Updated various examples to use the production best practice of [targeting an index by host](/guides/manage-data/target-an-index) instead of name.

  ***

  Updated the [Amazon Bedrock integration setup guide](/integrations/amazon-bedrock#setup-guide). It now utilizes Bedrock Agents.
</Update>

<Update label="2024-11-27" tags={["SDK"]}>
  ### Released Java SDK v3.1.0

  Released [`v3.1.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v3.1.0) of the [Pinecone Java SDK](/reference/java-sdk). This version introduces support for specifying a base URL for control and data plane operations.
</Update>

<Update label="2024-11-25" tags={["Assistant"]}>
  ### Pinecone Assistant: Context snippets and structured data files

  You can now [retrieve the context snippets](/guides/assistant/retrieve-context-snippets) that Pinecone Assistant uses to generate its responses. This data includes relevant chunks, relevancy scores, and references.

  ***

  You can now [upload JSON (.json) and Markdown (.md) files](/guides/assistant/manage-files#upload-a-local-file) to an assistant.
</Update>

<Update label="2024-11-14" tags={["General"]}>
  ### Monthly spend alerts

  You can now set an organization-wide [monthly spend alert](/guides/manage-cost/manage-cost#set-a-monthly-spend-alert). When your organization's spending reaches the specified limit, you will receive an email notification.
</Update>

<Update label="2024-11-14" tags={["SDK"]}>
  ### Released .NET SDK v2.0.0

  Released [`v2.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/2.0.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [embedding](/reference/api/2025-01/inference/generate-embeddings), [reranking](https://docs.pinecone.io/reference/api/2025-01/inference/rerank), and [import](/guides/index-data/import-data). It also adds support for using the .NET SDK with [proxies](/reference/dotnet-sdk#proxy-configuration).
</Update>

<Update label="2024-11-13" tags={["SDK"]}>
  ### Released Python SDK v5.4.0 and v5.4.1

  Released [`v5.4.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.4.0) and [`v5.4.1`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.4.1) of the [Pinecone Python SDK](/reference/python-sdk). `v5.4.0` adds a `query_namespaces` utility method to [run a query in parallel across multiple namespaces](/reference/python-sdk#query-across-multiple-namespaces) in an index and then merge the result sets into a single ranked result set with the `top_k` most relevant results. `v5.4.1` adds support for the `pinecone-plugin-inference` package required for some [integrated inference](/reference/api/introduction#inference) operations.
</Update>

<Update label="2024-11-08" tags={["General"]}>
  ### Enabled CSV export of usage and costs

  You can now download a CSV export of your organization's usage and costs from the [Pinecone console](https://app.pinecone.io/organizations/-/settings/usage).
</Update>

<Update label="2024-11-07" tags={["General"]}>
  ### Added Support chat in the console

  You can now chat with the Pinecone support bot and submit support requests directly from the [Pinecone console](https://app.pinecone.io/organizations/-/settings/support).
</Update>

<Update label="2024-11-05" tags={["Docs"]}>
  ### Published Assistant quickstart guide

  Added an [Assistant quickstart](/guides/assistant/quickstart).
</Update>


## October 2024

<Update label="2024-10-31" tags={["SDK"]}>
  ### Cequence released updated Scala SDK

  [Cequence](https://github.com/cequence-io) released a new version of their community-supported [Scala SDK](https://github.com/cequence-io/pinecone-scala) for Pinecone. See their [blog post](https://cequence.io/blog/industry-know-how/introducing-the-pinecone-scala-client-async-intuitive-and-ready-for-action) for details.
</Update>

<Update label="2024-10-28" tags={["Database"]}>
  ### Added index tagging for categorization

  You can now [add index tags](/guides/manage-data/manage-indexes#configure-index-tags) to categorize and identify indexes.
</Update>

<Update label="2024-10-24" tags={["SDK"]}>
  ### Released major SDK updates: Node.js, Go, Java, and Python

  Released [`v4.0.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v4.0.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [reranking](/guides/search/rerank-results) and [import](/guides/index-data/import-data).

  ***

  Released [`v2.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v2.0.0) of the [Pinecone Go SDK](/reference/go-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [reranking](/guides/search/rerank-results) and [import](/guides/index-data/import-data).

  ***

  Released [`v3.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v3.0.0) of the [Pinecone Java SDK](/reference/java-sdk). This version uses the latest stable API version, `2024-10`, and adds support for [embedding](/reference/api/2025-01/inference/generate-embeddings), [reranking](/reference/api/2025-01/inference/rerank), and [import](/guides/index-data/import-data).

  <Warning>
    `v3.0.0` also includes the following [breaking change](/reference/api/versioning#breaking-changes): The `control` class has been renamed `db_control`. Before upgrading to this version, be sure to update all relevant `import` statements to account for this change.

    For example, you would change `import org.openapitools.control.client.model.*;` to `import org.openapitools.db_control.client.model.*;`.
  </Warning>

  ***

  `v5.3.0` and `v5.3.1` of the [Pinecone Python SDK](/reference/python-sdk) use the latest stable API version, `2024-10`. These versions were release previously.
</Update>

<Update label="2024-10-24" tags={["API"]}>
  ### Pinecone API version `2024-10` is now the latest stable version

  `2024-10` is now the latest [stable version](/reference/api/versioning#release-schedule) of the [Database API](/reference/api/2024-10/data-plane/) and [Inference API](/reference/api/2024-10/inference/). For highlights, see [SDKs](#sdks) below.
</Update>

<Update label="2024-10-17" tags={["General"]}>
  ### Pinecone Inference now available on the free Starter plan

  The free [Starter plan](https://www.pinecone.io/pricing/) now supports [reranking documents with Pinecone Inference](/guides/search/rerank-results).
</Update>

<Update label="2024-10-17" tags={["Database"]}>
  ### Customer-managed encryption keys (CMEK) in early access

  You can now use [customer-managed encryption keys (CMEK)](/guides/production/configure-cmek) to secure indexes within a Pinecone project. This feature is in [early access](/release-notes/feature-availability).
</Update>

<Update label="2024-10-07" tags={["Database"]}>
  ### Serverless index monitoring generally available

  Monitoring serverless indexes with [Prometheus](/guides/production/monitoring#monitor-with-prometheus) or [Datadog](/integrations/datadog) is now in [general availability](/release-notes/feature-availability).
</Update>

<Update label="2024-10-03" tags={["Database"]}>
  ### Data import from Amazon S3 in public preview

  You can now [import data](/guides/index-data/import-data) into an index from [Amazon S3](/guides/operations/integrations/integrate-with-amazon-s3). This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-10-02" tags={["Assistant"]}>
  ### Chat and update features added to Assistant

  Added the [`chat_assistant`](/reference/api/2025-01/assistant/chat_assistant) endpoint to the Assistant API. It can be used to chat with your assistant, and get responses and citations back in a structured form.

  ***

  You can now add instructions when [creating](/guides/assistant/create-assistant) or [updating](/guides/assistant/manage-assistants#update-an-existing-assistant) an assistant. Instructions are a short description or directive for the assistant to apply to all of its responses. For example, you can update the instructions to reflect the assistant's role or purpose.

  ***

  You can now [update an existing assistant](/guides/assistant/manage-assistants#update-an-existing-assistant) with new instructions or metadata.
</Update>


## September 2024

<Update label="2024-09-25" tags={["Docs"]}>
  Added the [Matillion](/integrations/matillion) integration page.
</Update>

<Update label="2024-09-23" tags={["Docs"]}>
  Added guidance on using the Node.js SDK with [proxies](/reference/node-sdk#proxy-configuration).
</Update>

<Update label="2024-09-19" tags={["SDK"]}>
  Released [`v5.3.1`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.3.1) of the [Pinecone Python SDK](/reference/python-sdk). This version adds a missing `python-dateutil` dependency.

  ***

  Released [`v1.1.1`](https://github.com/pinecone-io/go-pinecone/releases/tag/v1.1.1) of the [Pinecone Go SDK](/reference/go-sdk). This version adds support for non-secure client connections.

  ***

  Released [`v2.1.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v2.1.0) of the [Pinecone Java SDK](/reference/java-sdk). This version adds support for non-secure client connections.
</Update>

<Update label="2024-09-18" tags={["SDK"]}>
  Released [`v5.3.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.3.0) of the [Pinecone Python SDK](/reference/python-sdk). This version adds support for [import](/guides/index-data/import-data) operations. This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-09-18" tags={["Assistant"]}>
  Added the `metrics_alignment` operation, which provides a way to [evaluate the correctness and completeness of a response](/guides/assistant/evaluate-answers) from a RAG system. This feature is in [public preview](/release-notes/feature-availability).

  ***

  When using Pinecone Assistant, you can now [choose an LLM](/guides/assistant/chat-with-assistant#choose-a-model-for-your-assistant) for the assistant to use and [filter the assistant's responses by metadata](/guides/assistant/chat-with-assistant#filter-chat-with-metadata).
</Update>

<Update label="2024-09-18" tags={["Docs"]}>
  Added the [Datavolo](/integrations/datavolo) integration pages.
</Update>

<Update label="2024-09-17" tags={["SDK"]}>
  Released [`v5.2.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.2.0) of the [Pinecone Python SDK](/reference/python-sdk). This version adds support for [reranking documents with Pinecone Inference](/guides/search/rerank-results); it is no longer necessary to install the `pinecone-plugin-inference` package separately. This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-09-16" tags={["Database"]}>
  [Prometheus monitoring for serverless indexes](/guides/production/monitoring#monitor-with-prometheus) is now in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-09-12" tags={["SDK"]}>
  Released [`v3.0.3`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/3.0.3) of the [Pinecone Node.js SDK](/reference/node-sdk). This version removes extra logging and makes general internal enhancements.
</Update>

<Update label="2024-09-11" tags={["General"]}>
  If you are upgrading from the [Starter plan](https://www.pinecone.io/pricing/), you can now connect your Pinecone organization to the [AWS Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan), [Google Cloud Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan), or [Microsoft Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan) for billing purposes.
</Update>

<Update label="2024-09-11" tags={["General"]}>
  Refreshed the navigation and overall visual interface of the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/).
</Update>

<Update label="2024-09-11" tags={["Docs"]}>
  Added Go examples for [batch upserts](/guides/index-data/upsert-data#upsert-in-batches), [parallel upserts](/guides/index-data/upsert-data#send-upserts-in-parallel), and [deleting all records for a parent document](/guides/index-data/data-modeling#delete-chunks).
</Update>


## August 2024

<Update label="2024-08-28" tags={["Docs"]}>
  Added the [Aryn](/integrations/aryn) integration page.
</Update>

<Update label="2024-08-28" tags={["SDK"]}>
  Released [`v3.0.2`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/3.0.2) of the [Pinecone Node.js SDK](/reference/node-sdk). This version removes a native Node utility function that was causing issues for users running in `Edge`. There are no downstream affects of its removal; existing code should not be impacted.
</Update>

<Update label="2024-08-27" tags={["SDK"]}>
  Released [`v5.1.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.1.0) of the [Pinecone Python SDK](/reference/python-sdk). With this version, the SDK can now be installed with `pip install pinecone` / `pip install "pinecone[grpc]"`. This version also includes a `has_index()` helper function to check if an index exists.

  ***

  Released [`v0.1.0`](https://github.com/pinecone-io/pinecone-rust-client/releases/tag/v0.1.0) and [`v0.1.1`](https://github.com/pinecone-io/pinecone-rust-client/releases/tag/v0.1.1) of the [Pinecone Rust SDK](/reference/rust-sdk). The Rust SDK is in "alpha" and is under active development. The SDK should be considered unstable and should not be used in production. Before a 1.0 release, there are no guarantees of backward compatibility between minor versions. See the [Rust SDK README](https://github.com/pinecone-io/pinecone-rust-client/blob/main/README.md) for full installation instructions and usage examples.
</Update>

<Update label="2024-08-27" tags={["SDK"]}>
  Released [`v1.0.0`](https://github.com/pinecone-io/pinecone-dotnet-client/releases/tag/1.0.0) of the [Pinecone .NET SDK](/reference/dotnet-sdk). For usage examples, see [our guides](/guides/get-started/quickstart) or the [GitHub README](https://github.com/pinecone-io/pinecone-dotnet-client/blob/main/README.md).
</Update>

<Update label="2024-08-26" tags={["Database"]}>
  You can now [back up](/guides/manage-data/back-up-an-index) and [restore](/guides/manage-data/restore-an-index) serverless indexes. This feature is in public preview.

  ***

  Serverless indexes are now in [general availability on GCP and Azure](/guides/index-data/create-an-index#cloud-regions) for Standard and Enterprise plans.

  ***

  You can now deploy [serverless indexes](/guides/index-data/indexing-overview) in the `europe-west1` (Netherlands) region of GCP.
</Update>

<Update label="2024-08-26" tags={["SDK"]}>
  Released [`v1.1.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v1.1.0) of the [Pinecone Go SDK](/reference/go-sdk). This version adds support for generating embeddings via [Pinecone Inference](/reference/api/introduction#inference).
</Update>

<Update label="2024-08-21" tags={["Docs"]}>
  Added the [Nexla](/integrations/nexla) integration page.
</Update>

<Update label="2024-08-15" tags={["Assistant"]}>
  [Pinecone Assistant](/guides/assistant/overview) is now in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-08-13" tags={["API"]}>
  The Pinecone Inference API now supports [reranking](https://docs.pinecone.io/guides/search/rerank-results). This feature is in [public preview](/release-notes/feature-availability).
</Update>

<Update label="2024-08-06" tags={["SDK"]}>
  Released [`v1.0.0`](https://github.com/pinecone-io/go-pinecone/releases/tag/v1.0.0) of the [Pinecone Go SDK](/reference/go-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). With this version, the Go SDK is [officially supported](/troubleshooting/pinecone-support-slas) by Pinecone.
</Update>

<Update label="2024-08-05" tags={["Docs"]}>
  Added the [Nuclia](/integrations/nuclia) integration page
</Update>


## July 2024

<Update label="2024-07-30" tags={["Docs"]}>
  Added the [Redpanda](/integrations/redpanda) integration page.
</Update>

<Update label="2024-07-26" tags={["Docs"]}>
  Updated the [Build a RAG chatbot](/guides/get-started/build-a-rag-chatbot) guide to use Pinecone Inference for generating embeddings.
</Update>

<Update label="2024-07-19" tags={["Database"]}>
  Added the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection).
</Update>

<Update label="2024-07-19" tags={["SDK"]}>
  Released [`v5.0.0`](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v5.0.0) of the [Pinecone Python SDK](/reference/python-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). Additionally, the `pinecone-plugin-inference` package required to [generate embeddings with Pinecone Inference](/reference/api/2025-01/inference/generate-embeddings) is now included by default; it is no longer necessary to install the plugin separately.

  ***

  Released [`v3.0.0`](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v3.0.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). Additionally, this version supports generating embeddings via [Pinecone Inference](/reference/api/2025-01/inference/generate-embeddings).

  ***

  Released [`v2.0.0`](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v2.0.0) of the [Pinecone Java SDK](/reference/java-sdk). This version depends on Pinecone API version `2024-07` and includes the ability to [prevent accidental index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection). Additionally, this version includes the following **breaking changes**:

  * `createServerlessIndex()` now requires a new argument: `DeletionProtection.ENABLED` or `DeletionProtection.DISABLED`.
  * `configureIndex()` has been renamed `configurePodsIndex()`.

  For more details, see the [Java SDK v2.0.0 migration guide](https://github.com/pinecone-io/pinecone-java-client/blob/main/v2-migration.md).
</Update>

<Update label="2024-07-19" tags={["API"]}>
  Released version `2024-07` of the [Database API](/reference/api/2024-07/data-plane/) and Inference API. This version includes the following highlights:

  * The [`create_index`](/reference/api/2024-07/control-plane/create_index) and [`configure_index`](/reference/api/2024-07/control-plane/configure_index) endpoints now support the `deletion_protection` parameter. Setting this parameter to `"enabled"` prevents an index from accidental deletion. For more details, see [Prevent index deletion](/guides/manage-data/manage-indexes#configure-deletion-protection).

  * The [`describe_index`](/reference/api/2024-07/control-plane/describe_index) and [`list_index`](/reference/api/2024-07/control-plane/list_indexes) responses now include the `deletion_protection` field. This field indicates whether deletion protection is enabled for an index.

  * The `spec.serverless.cloud` and `spec.serverless.region` parameters of [`create_index`](/reference/api/2024-07/control-plane/create_index) now support `gcp` / `us-central` and `azure` / `eastus2` as part of the serverless public preview on GCP and Azure.
</Update>

<Update label="2024-07-17" tags={["Database"]}>
  Serverless indexes are now in [public preview on Azure](/guides/index-data/create-an-index#cloud-regions) for Standard and Enterprise plans.
</Update>

<Update label="2024-07-10" tags={["Database"]}>
  Released [version 1.1.0](https://github.com/pinecone-io/spark-pinecone/releases/tag/v1.1.0) of the official Spark connector for Pinecone. In this release, you can now set a [source tag](/integrations/build-integration/attribute-usage-to-your-integration). Additionally, you can now [upsert records](/guides/index-data/upsert-data) with 40KB of metadata, increased from 5KB.
</Update>

<Update label="2024-07-01" tags={["Database"]}>
  Serverless indexes are now in [public preview on GCP](/guides/index-data/create-an-index#cloud-regions) for Standard and Enterprise plans.
</Update>

<Update label="2024-07-01" tags={["Docs"]}>
  Added an introduction to [key concepts in Pinecone](/guides/get-started/concepts) and how they relate to each other.

  ***

  Added the [Twelve Labs](/integrations/twelve-labs) integration page.
</Update>


## June 2024

<Update label="2024-06-30" tags={["Docs"]}>
  Added a [model gallery](/models/overview) with details and guidance on popular embedding and reranking models, including models hosted on Pinecone's infrastructure.
</Update>

<Update label="2024-06-28" tags={["SDK"]}>
  Released [version 1.2.2](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.2.2) of the Pinecone Java SDK. This release simplifies the proxy configuration process. It also fixes an issue where the user agent string was not correctly setup for gRPC calls. Now, if the source tag is set by the user, it is appended to the custom user agent string.
</Update>

<Update label="2024-06-27" tags={["Database"]}>
  You can now load a [sample dataset](/guides/data/use-sample-datasets) into a new project.

  ***

  Simplified the process for [migrating paid pod indexes to serverless](/guides/indexes/pods/migrate-a-pod-based-index-to-serverless).
</Update>

<Update label="2024-06-25" tags={["Assistant"]}>
  The [Assistant API](/guides/assistant/overview) is now in beta release.
</Update>

<Update label="2024-06-20" tags={["Database"]}>
  The [Inference API](/reference/api/introduction#inference) is now in public preview.
</Update>

<Update label="2024-06-18" tags={["Docs"]}>
  Added a new [legal semantic search](https://docs.pinecone.io/examples/sample-apps/legal-semantic-search) sample app that demonstrates low-latency natural language search over a knowledge base of legal documents.
</Update>

<Update label="2024-06-17" tags={["Docs"]}>
  Added the [Instill](/integrations/instill) integration page.
</Update>

<Update label="2024-06-07" tags={["Docs"]}>
  Added the [Langtrace](/integrations/langtrace) integration page.
</Update>

<Update label="2024-06-06" tags={["Docs"]}>
  Updated Python code samples to use the gRPC version of the [Python SDK](/reference/python-sdk), which is more performant than the Python SDK that interacts with Pinecone via HTTP requests.
</Update>

<Update label="2024-06-06" tags={["SDK"]}>
  Released [version 4.1.1](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v4.1.1) of the Pinecone Python SDK. In this release, you can now use colons inside source tags. Additionally, the gRPC version of the Python SDK now allows retries of up to `MAX_MSG_SIZE`.
</Update>

<Update label="2024-06-05" tags={["Database"]}>
  The Enterprise [quota for namespaces per serverless index](/reference/api/database-limits#namespaces-per-serverless-index) has increased from 50,000 to 100,000.
</Update>

<Update label="2024-06-04" tags={["Docs"]}>
  Added the [Fleak](/integrations/fleak) integration page.
</Update>


## May 2024

<Update label="2024-05-31" tags={["SDK"]}>
  Released [version 1.2.1](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.2.1) of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). This version fixes the error `Could Not Find NameResolverProvider` using uber jar.
</Update>

<Update label="2024-05-31" tags={["Docs"]}>
  Added the [Gathr](/integrations/gathr) integration page.
</Update>

<Update label="2024-05-30" tags={["SDK"]}>
  Released [version 1.1.0](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.1.0) of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). This version adds the ability to [list record IDs with a common prefix](/guides/manage-data/list-record-ids#list-the-ids-of-records-with-a-common-prefix).
</Update>

<Update label="2024-05-29" tags={["SDK"]}>
  Released version [1.2.0](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.2.0) of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). This version adds the ability to [list all record IDs in a namespace](/guides/manage-data/list-record-ids#list-the-ids-of-all-records-in-a-namespace).
</Update>

<Update label="2024-05-29" tags={["Docs"]}>
  Added the following integration pages:

  * [Apify](/integrations/apify)
  * [Context Data](/integrations/context-data)
  * [Estuary](/integrations/estuary)
  * [GitHub Copilot](/integrations/github-copilot)
  * [Jina](/integrations/jina)
  * [FlowiseAI](/integrations/flowise)
  * [OctoAI](/integrations/octoai)
  * [Streamnative](/integrations/streamnative)
  * [Traceloop](/integrations/traceloop)
  * [Unstructured](/integrations/unstructured)
  * [VoyageAI](/integrations/voyage)
</Update>

<Update label="2024-05-21" tags={["General"]}>
  You can now use the `ConnectPopup` function to bypass the [**Connect** widget](/integrations/build-integration/connect-your-users-to-pinecone) and open the "Connect to Pinecone" flow in a popup. This can be used in an app or website for a seamless Pinecone signup and login process.
</Update>

<Update label="2024-05-16" tags={["Database"]}>
  Released [version 1.0.0](https://github.com/pinecone-io/spark-pinecone/releases/tag/v1.0.0) of the official Spark connector for Pinecone. In this release, you can now upsert records into [serverless indexes](/guides/index-data/indexing-overview).
</Update>

<Update label="2024-05-08" tags={["Database"]}>
  Pinecone now supports [AWS PrivateLink](/guides/production/connect-to-aws-privatelink). Create and use [Private Endpoints](/guides/production/connect-to-aws-privatelink#manage-private-endpoints) to connect AWS PrivateLink to Pinecone while keeping your VPC private from the public internet.
</Update>

<Update label="2024-05-01" tags={["SDK"]}>
  Released [version 4.0.0](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v4.0.0) of the Pinecone Python SDK. In this release, we are upgrading the `protobuf` dependency in our optional `grpc` extras from `3.20.3` to `4.25.3`. Significant performance improvements have been made with this update. This is a breaking change for users of the optional GRPC addon ([installed with `pinecone[grpc]`](https://github.com/pinecone-io/pinecone-python-client?tab=readme-ov-file#working-with-grpc-for-improved-performance)).
</Update>


## April 2024

<Update label="2024-04-30" tags={["Docs"]}>
  * The docs now have a new AI chatbot. Use the search bar at the top of our docs to find related content across all of our resources.
  * We've updated the look and feel of our [example notebooks](/examples/notebooks) and [sample apps](/examples/sample-apps). A new sample app, [Namespace Notes](/examples/sample-apps/namespace-notes), a simple multi-tenant RAG app that uploads documents, has also been added.
</Update>

<Update label="2024-04-30" tags={["Database"]}>
  The free [Starter plan](https://www.pinecone.io/pricing/) now includes 1 project, 5 serverless indexes in the `us-east-1` region of AWS, and up to 2 GB of storage. Although the Starter plan has stricter [limits](/reference/api/database-limits) than other plans, you can [upgrade](/guides/organizations/manage-billing/upgrade-billing-plan) whenever you're ready.
</Update>

<Update label="2024-04-26" tags={["General"]}>
  Pinecone now provides a [**Connect** widget](/integrations/build-integration/connect-your-users-to-pinecone) that can be embedded into an app, website, or Colab notebook for a seamless signup and login process.
</Update>

<Update label="2024-04-22" tags={["Docs"]}>
  Added the [lifecycle policy of the Pinecone API](/release-notes/feature-availability), which describes the availability phases applicable to APIs, features, and SDK versions.
</Update>

<Update label="2024-04-22" tags={["Database"]}>
  As announced in January 2024, [control plane](/reference/api/2024-07/control-plane) operations like `create_index`, `describe_index`, and `list_indexes` now use a single global URL, `https://api.pinecone.io`, regardless of the cloud environment where an index is hosted. This is now in general availability. As a result, the legacy version of the API, which required regional URLs for control plane operations, is deprecated as of April 15, 2024 and will be removed in a future, to be announced, release.
</Update>

<Update label="2024-04-15" tags={["Docs"]}>
  Added the [Terraform](/integrations/terraform) integration page.
</Update>

<Update label="2024-04-15" tags={["SDK"]}>
  Released version 0.9.0 of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md). This version adds support for OctoAI LLM and embeddings, and Qdrant as a supported knowledge base. See the [v0.9.0 release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.9.0) in GitHub for more details.
</Update>

<Update label="2024-04-12" tags={["Database"]}>
  You can now deploy [serverless indexes](/guides/index-data/indexing-overview) in the `eu-west-1` region of AWS.
</Update>

<Update label="2024-04-12" tags={["SDK"]}>
  Released version 1.0.0 of the [Pinecone Java SDK](/reference/pinecone-sdks#java-client). With this version, the Java SDK is [officially supported](/troubleshooting/pinecone-support-slas) by Pinecone. For full details on the release, see the [v1.0.0 release notes](https://github.com/pinecone-io/pinecone-java-client/releases/tag/v1.0.0) in GitHub. For usage examples, see [our guides](/guides/get-started/quickstart) or the [GitHub README](https://github.com/pinecone-io/pinecone-java-client/blob/main/README.md). To migrate to v1.0.0 from version 0.8.x or below, see the [Java v1.0.0 migration guide](https://github.com/pinecone-io/pinecone-java-client/blob/main/v1-migration.md).
</Update>


## March 2024

<Update label="2024-03-31" tags={["Docs"]}>
  Added a [Troubleshooting](https://docs.pinecone.io/troubleshooting/) section, which includes content on best practices, troubleshooting, and how to address common errors.

  ***

  Added an explanation of the [Pinecone serverless architecture](/guides/get-started/database-architecture), including descriptions of the high-level components and explanations of the distinct paths for writes and reads.

  ***

  Added [considerations for querying serverless indexes with metadata filters](/guides/index-data/indexing-overview#metadata#considerations-for-serverless-indexes).
</Update>

<Update label="2024-03-30" tags={["SDK"]}>
  Released [version 3.2.2](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.2) of the [Pinecone Python SDK](/reference/python-sdk). This version fixes a minor issue introduced in v3.2.0 that resulted in a `DeprecationWarning` being incorrectly shown to users who are not passing in the deprecated `openapi_config` property. This warning can safely be ignored by anyone who is not preparing to upgrade.
</Update>

<Update label="2024-03-29" tags={["SDK"]}>
  Released [version 3.2.0](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.2.0) of the [Pinecone Python SDK](/reference/python-sdk). This version adds four optional configuration properties that enable the use of Pinecone [via proxy](/reference/python-sdk#proxy-configuration).
</Update>

<Update label="2024-03-28" tags={["SDK"]}>
  Released [version 2.2.0](https://github.com/pinecone-io/pinecone-ts-client/releases/tag/v2.2.0) of the [Pinecone Node.js SDK](/reference/node-sdk). This releases adds an optional `sourceTag` that you can set when constructing a Pinecone client to help Pinecone associate API activity to the specified source.
</Update>

<Update label="2024-03-27" tags={["SDK"]}>
  Released version 0.4.1 of the [Pinecone Go SDK](/reference/pinecone-sdks#go-client). This version adds an optional `SourceTag` that you can set when constructing a Pinecone client to help Pinecone associate API activity to the specified source.

  ***

  Released version 2.2.0 of the [Pinecone Node.js SDK](/reference/node-sdk).

  ***

  Released [version 0.4.1](https://github.com/pinecone-io/go-pinecone/releases/tag/v0.4.1) of the [Pinecone Go SDK](/reference/go-sdk).
</Update>

<Update label="2024-03-25" tags={["SDK"]}>
  Released version 3.2.1 of the [Pinecone Python SDK](/reference/python-sdk). This version adds an optional `source_tag` that you can set when constructing a Pinecone client to help Pinecone associate API activity to the specified source. See the [v3.2.1 release notes](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.2.1) in GitHub for more details.
</Update>

<Update label="2024-03-21" tags={["SDK"]}>
  Released version 0.8.1 of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md). This version includes bug fixes, the removal of an unused field for Cohere chat calls, and added guidance on creating a knowledge base with a specified record encoder when using the core library. See the [v0.8.1 release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.8.1) in GitHub for more details.
</Update>

<Update label="2024-03-20" tags={["Database"]}>
  The [Pinecone console](https://app.pinecone.io) has a new look and feel, with a brighter, minimalist design; reorganized menu items for quicker, more intuitive navigation; and easy access to recently viewed indexes in the sidebar.

  ***

  When viewing the list of indexes in a project, you can now search indexes by index name; sort indexes alphabetically, by how recently they were viewed or created, or by status; and filter indexes by index type (serverless, pod-based, or starter).
</Update>

<Update label="2024-03-15" tags={["SDK"]}>
  Released version 0.4.0 of the [Pinecone Go SDK](/reference/pinecone-sdks#go-client). This version is a comprehensive re-write and adds support for all current [Pinecone API operations](/reference/api/introduction).
</Update>

<Update label="2024-03-14" tags={["Database"]}>
  Fixed a bug that caused inaccurate index fullness reporting for some pod-based indexes on GCP.

  ***

  You can now deploy [serverless indexes](/guides/index-data/indexing-overview) in the `us-east-1` region of AWS.
</Update>

<Update label="2024-03-06" tags={["SDK"]}>
  Released version 2.1.0 of the [Pinecone Node.js SDK](/reference/node-sdk). This version adds support for [listing the IDs of records in a serverless index](/guides/manage-data/list-record-ids). You can list all records or just those with a common ID prefix.
</Update>

<Update label="2024-03-05" tags={["General"]}>
  You can now [configure single single-on](/guides/production/configure-single-sign-on/okta) to manage your teams' access to Pinecone through any identity management solution with SAML 2.0 support, such as Okta. This feature is available on the [Enterprise plan](https://www.pinecone.io/pricing/) only.
</Update>


## February 2024

<Update label="2024-02-29" tags={["Docs"]}>
  Updated the [Langchain integration guide](/integrations/langchain) to avoid a [namespace collision issue](/troubleshooting/pinecone-attribute-errors-with-langchain).
</Update>

<Update label="2024-02-27" tags={["SDK"]}>
  The latest version of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md) (v0.8.0) adds support for Pydantic v2. For applications depending on Pydantic v1, this is a breaking change; review the [Pydantic v1 to v2 migration guide](https://docs.pydantic.dev/latest/migration/) and make the necessary changes before upgrading. See the [Canopy SDK release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.8.0) in GitHub for more details.
</Update>

<Update label="2024-02-23" description="SDK">
  The latest version of Pinecone's Python SDK (v3.1.0) adds support for [listing the IDs of records in a serverless index](/guides/manage-data/list-record-ids). You can list all records or just those with a [common ID prefix](/guides/index-data/data-modeling#use-structured-ids). See the [Python SDK release notes](https://github.com/pinecone-io/pinecone-python-client/releases/tag/v3.1.0) in GitHub for more details.
</Update>

<Update label="2024-02-22" tags={["Docs"]}>
  Improved the docs for [setting up billing through the AWS Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan) and [Google Cloud Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).
</Update>

<Update label="2024-02-16" tags={["Database"]}>
  It is now possible to convert a pod-based starter index to a serverless index. For organizations on the Starter plan, this requires upgrading to Standard or Enterprise; however, upgrading comes with \$100 in serverless credits, which will cover the cost of a converted index for some time.
</Update>

<Update label="2024-02-01" tags={["Docs"]}>
  Added a [Llamaindex integration guide](/integrations/llamaindex) on building a RAG pipeline with LlamaIndex and Pinecone.
</Update>


## January 2024

<Update label="2024-01-31" tags={["SDK"]}>
  The latest version of the [Canopy SDK](https://github.com/pinecone-io/canopy/blob/main/README.md) (v0.6.0) adds support for the new API mentioned above as well as namespaces, LLMs that do not have function calling functionality for query generation, and more. See the [release notes](https://github.com/pinecone-io/canopy/releases/tag/v0.6.0) in GitHub for more details.
</Update>

<Update label="2024-01-09" tags={["SDK"]}>
  The latest versions of Pinecone's Python SDK (v3.0.0) and Node.js SDK (v2.0.0) support the new API. To use the new API, existing users must upgrade to the new client versions and adapt some code. For guidance, see the [Python SDK v3 migration guide](https://canyon-quilt-082.notion.site/Pinecone-Python-SDK-v3-0-0-Migration-Guide-056d3897d7634bf7be399676a4757c7b) and [Node.js SDK v2 migration guide](https://github.com/pinecone-io/pinecone-ts-client/blob/main/v2-migration.md).
</Update>

<Update label="2024-01-09" tags={["Docs"]}>
  The Pinecone documentation is now versioned. The default "latest" version reflects the new Pinecone API. The "legacy" version reflects the previous API, which requires regional URLs for control plane operations and does not support serverless indexes.
</Update>

<Update label="2024-01-09" tags={["API"]}>
  The [new Pinecone API](/reference/api) gives you the same great vector database but with a drastically improved developer experience. The most significant improvements include:

  * [Serverless indexes](/guides/index-data/indexing-overview): With serverless indexes, you don't configure or manage compute and storage resources. You just load your data and your indexes scale automatically based on usage. Likewise, you don't pay for dedicated resources that may sometimes lay idle. Instead, the pricing model for serverless indexes is consumption-based: You pay only for the amount of data stored and operations performed, with no minimums.

  * [Multi-region projects](/guides/projects/understanding-projects): Instead of choosing a cloud region for an entire project, you now [choose a region for each index](/guides/index-data/create-an-index#create-a-serverless-index) in a project. This makes it possible to consolidate related indexes in the same project, even when they are hosted in different regions.

  * [Global URL for control plane operations](/reference): Control plane operations like `create_index`, `describe_index`, and `list_indexes` now use a single global URL, `https://api.pinecone.io`, regardless of the cloud environment where an index is hosted. This simplifies the experience compared to the legacy API, where each environment has a unique URL.
</Update>



---
**Navigation:** [← Previous](./32-2023-releases.md) | [Index](./index.md) | [Next →](./34-2025-releases.md)
