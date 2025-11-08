---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## snippet-end:[python.example_code.textract.GetDocumentAnalysis]

```
Next, we set up Textract and S3, and provide this to an instance of `TextractWrapper`.
```python PYTHON
import boto3

textract_client = boto3.client('textract')
s3_client = boto3.client('s3')

textractWrapper = TextractWrapper(textract_client, s3_client, None)
```
We are now ready to make calls to Textract. At a high level, Textract has two modes: synchronous and asynchronous. Synchronous calls return the parsed output once it is completed. As of the time of writing (March 2024), however, multipage PDF processing is only supported [asynchronously](https://docs.aws.amazon.com/textract/latest/dg/sync.html). So for our purposes here, we will only explore the asynchronous route.

Asynchronous calls follow the below process:

1. Send a request to Textract with an SNS topic, S3 bucket, and the name (key) of the document inside that bucket to process. Textract returns a Job ID that can be used to track the status of the request
2. Textract fetches the document from S3 and processes it
3. Once the request is complete, Textract sends out a message to the SNS topic. This can be used in conjunction with other services such as Lambda or SQS for downstream processes.
4. The parsed results can be fetched from Textract in chunks via the job ID.
```python PYTHON
bucket_name = "your-bucket-name"
sns_topic_arn = "your-sns-arn" # this can be found under the topic you created in the Amazon SNS dashboard

sns_role_arn = "sns-role-arn" # this is an IAM role that allows Textract to interact with SNS

file_name = "fda-approved-drug.pdf"
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
