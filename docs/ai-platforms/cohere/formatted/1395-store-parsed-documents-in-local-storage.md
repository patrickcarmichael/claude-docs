---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Store parsed documents in local storage.

for filename, doc_content in parsed_documents:
 file_path = "{}/{}-parsed-{}.txt".format(data_dir, "gcp", source_filename)
 store_document(file_path, doc_content)
"""
```

#### Visualize the parsed document

```python PYTHON
filename = "gcp-parsed-{}.txt".format(source_filename)
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```typescript

### Solution 2: AWS Textract [\[Back to Solutions\]](#top) \[#aws]

[Amazon Textract](https://aws.amazon.com/textract/) is an OCR service offered by AWS. It can detect text, forms, tables, and more in PDFs and images. In this section, we go over how to use Textract's asynchronous API.

#### Parsing the document

We assume that you are working within the AWS ecosystem (from a SageMaker notebook, EC2 instance, a Lambda function, etc.) with valid credentials. Much of the code here is from supplemental materials created by AWS and offered here:

* [https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example\_code/textract](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/textract)
* [https://github.com/aws-samples/textract-paragraph-identification/tree/main](https://github.com/aws-samples/textract-paragraph-identification/tree/main)

At minimum, you will need access to the following AWS resources to get started:

* Textract
* an S3 bucket containing the document(s) to process - in this case, our `fda-approved-drug.pdf` file
* an SNS topic that Textract can publish to. This is used to send a notification that parsing is complete.
* an IAM role that Textract will assume, granting access to the S3 bucket and SNS topic

First, we bring in the `TextractWrapper` class provided in the [AWS Code Examples repository](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/textract/textract_wrapper.py). This class makes it simpler to interface with the Textract service.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
