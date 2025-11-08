**Navigation:** [← Previous](./16-creating-a-qa-bot-from-technical-documentation.md) | [Index](./index.md) | [Next →](./18-employing-a-smaller-context-window-also-has-the-ad.md)

---

# credentials_file = "populate if you are running in a non Vertex AI environment."
gcs_input_prefix = ""


def batch_process_documents(
    project_id: str,
    location: str,
    processor_id: str,
    gcs_output_uri: str,
    gcs_input_prefix: str,
    timeout: int = 400
) -> None:
    parsed_documents = []

    # Client configs
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    # With credentials
    # opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com", credentials_file=credentials_file)

    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    processor_name = client.processor_path(project_id, location, processor_id)

    # Input storage configs
    gcs_prefix = documentai.GcsPrefix(gcs_uri_prefix=gcs_input_prefix)
    input_config = documentai.BatchDocumentsInputConfig(gcs_prefix=gcs_prefix)

    # Output storage configs
    gcs_output_config = documentai.DocumentOutputConfig.GcsOutputConfig(gcs_uri=gcs_output_uri, field_mask=None)
    output_config = documentai.DocumentOutputConfig(gcs_output_config=gcs_output_config)
    storage_client = storage.Client()
    # With credentials
    # storage_client = storage.Client.from_service_account_json(json_credentials_path=credentials_file)

    # Batch process docs request
    request = documentai.BatchProcessRequest(
        name=processor_name,
        input_documents=input_config,
        document_output_config=output_config,
    )

    # batch_process_documents returns a long running operation
    operation = client.batch_process_documents(request)

    # Continually polls the operation until it is complete.
    # This could take some time for larger files
    try:
        print(f"Waiting for operation {operation.operation.name} to complete...")
        operation.result(timeout=timeout)
    except (RetryError, InternalServerError) as e:
        print(e.message)

    # Get output document information from completed operation metadata
    metadata = documentai.BatchProcessMetadata(operation.metadata)
    if metadata.state != documentai.BatchProcessMetadata.State.SUCCEEDED:
        raise ValueError(f"Batch Process Failed: {metadata.state_message}")

    print("Output files:")
    # One process per Input Document
    for process in list(metadata.individual_process_statuses):
        matches = re.match(r"gs://(.*?)/(.*)", process.output_gcs_destination)
        if not matches:
            print("Could not parse output GCS destination:", process.output_gcs_destination)
            continue

        output_bucket, output_prefix = matches.groups()
        output_blobs = storage_client.list_blobs(output_bucket, prefix=output_prefix)

        # Document AI may output multiple JSON files per source file
        # (Large documents get split in multiple file "versions" doc --> parsed_doc_0 + parsed_doc_1 ...)
        for blob in output_blobs:
            # Document AI should only output JSON files to GCS
            if blob.content_type != "application/json":
                print(f"Skipping non-supported file: {blob.name} - Mimetype: {blob.content_type}")
                continue

            # Download JSON file as bytes object and convert to Document Object
            print(f"Fetching {blob.name}")
            document = documentai.Document.from_json(blob.download_as_bytes(), ignore_unknown_fields=True)
            # Store the filename and the parsed versioned document content as a tuple
            parsed_documents.append((blob.name.split("/")[-1].split(".")[0], document.text))

    print("Finished document parsing process.")
    return parsed_documents

# Call service
# versioned_parsed_documents = batch_process_documents(
#     project_id=project_id,
#     location=location,
#     processor_id=processor_id,
#     gcs_output_uri=gcs_output_uri,
#     gcs_input_prefix=gcs_input_prefix
# )
```

```python PYTHON
"""
Post process parsed document and store it locally.
Make sure to run this in a Google Vertex AI environment or include a credentials file.
"""

"""
from pathlib import Path
from collections import defaultdict

parsed_documents = []
combined_versioned_parsed_documents = defaultdict(list)

# Assemble versioned documents together ({"doc_name": [(0, doc_content_0), (1, doc_content_1), ...]}).
for filename, doc_content in versioned_parsed_documents:
  filename, version = "-".join(filename.split("-")[:-1]), filename.split("-")[-1]
  combined_versioned_parsed_documents[filename].append((version, doc_content))

# Sort documents by version and join the content together.
for filename, docs in combined_versioned_parsed_documents.items():
  doc_content = " ".join([x[1] for x in sorted(docs, key=lambda x: x[0])])
  parsed_documents.append((filename, doc_content))

# Store parsed documents in local storage.
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
```

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
# source: https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/textract

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose

Shows how to use the AWS SDK for Python (Boto3) with Amazon Textract to
detect text, form, and table elements in document images.
"""

import json
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


# snippet-start:[python.example_code.textract.TextractWrapper]
class TextractWrapper:
    """Encapsulates Textract functions."""

    def __init__(self, textract_client, s3_resource, sqs_resource):
        """
        :param textract_client: A Boto3 Textract client.
        :param s3_resource: A Boto3 Amazon S3 resource.
        :param sqs_resource: A Boto3 Amazon SQS resource.
        """
        self.textract_client = textract_client
        self.s3_resource = s3_resource
        self.sqs_resource = sqs_resource

    # snippet-end:[python.example_code.textract.TextractWrapper]

    # snippet-start:[python.example_code.textract.DetectDocumentText]
    def detect_file_text(self, *, document_file_name=None, document_bytes=None):
        """
        Detects text elements in a local image file or from in-memory byte data.
        The image must be in PNG or JPG format.

        :param document_file_name: The name of a document image file.
        :param document_bytes: In-memory byte data of a document image.
        :return: The response from Amazon Textract, including a list of blocks
                 that describe elements detected in the image.
        """
        if document_file_name is not None:
            with open(document_file_name, "rb") as document_file:
                document_bytes = document_file.read()
        try:
            response = self.textract_client.detect_document_text(
                Document={"Bytes": document_bytes}
            )
            logger.info("Detected %s blocks.", len(response["Blocks"]))
        except ClientError:
            logger.exception("Couldn't detect text.")
            raise
        else:
            return response

    # snippet-end:[python.example_code.textract.DetectDocumentText]

    # snippet-start:[python.example_code.textract.AnalyzeDocument]
    def analyze_file(
        self, feature_types, *, document_file_name=None, document_bytes=None
    ):
        """
        Detects text and additional elements, such as forms or tables, in a local image
        file or from in-memory byte data.
        The image must be in PNG or JPG format.

        :param feature_types: The types of additional document features to detect.
        :param document_file_name: The name of a document image file.
        :param document_bytes: In-memory byte data of a document image.
        :return: The response from Amazon Textract, including a list of blocks
                 that describe elements detected in the image.
        """
        if document_file_name is not None:
            with open(document_file_name, "rb") as document_file:
                document_bytes = document_file.read()
        try:
            response = self.textract_client.analyze_document(
                Document={"Bytes": document_bytes}, FeatureTypes=feature_types
            )
            logger.info("Detected %s blocks.", len(response["Blocks"]))
        except ClientError:
            logger.exception("Couldn't detect text.")
            raise
        else:
            return response

    # snippet-end:[python.example_code.textract.AnalyzeDocument]

    # snippet-start:[python.example_code.textract.helper.prepare_job]
    def prepare_job(self, bucket_name, document_name, document_bytes):
        """
        Prepares a document image for an asynchronous detection job by uploading
        the image bytes to an Amazon S3 bucket. Amazon Textract must have permission
        to read from the bucket to process the image.

        :param bucket_name: The name of the Amazon S3 bucket.
        :param document_name: The name of the image stored in Amazon S3.
        :param document_bytes: The image as byte data.
        """
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            bucket.upload_fileobj(document_bytes, document_name)
            logger.info("Uploaded %s to %s.", document_name, bucket_name)
        except ClientError:
            logger.exception("Couldn't upload %s to %s.", document_name, bucket_name)
            raise

    # snippet-end:[python.example_code.textract.helper.prepare_job]

    # snippet-start:[python.example_code.textract.helper.check_job_queue]
    def check_job_queue(self, queue_url, job_id):
        """
        Polls an Amazon SQS queue for messages that indicate a specified Textract
        job has completed.

        :param queue_url: The URL of the Amazon SQS queue to poll.
        :param job_id: The ID of the Textract job.
        :return: The status of the job.
        """
        status = None
        try:
            queue = self.sqs_resource.Queue(queue_url)
            messages = queue.receive_messages()
            if messages:
                msg_body = json.loads(messages[0].body)
                msg = json.loads(msg_body["Message"])
                if msg.get("JobId") == job_id:
                    messages[0].delete()
                    status = msg.get("Status")
                    logger.info(
                        "Got message %s with status %s.", messages[0].message_id, status
                    )
            else:
                logger.info("No messages in queue %s.", queue_url)
        except ClientError:
            logger.exception("Couldn't get messages from queue %s.", queue_url)
        else:
            return status

    # snippet-end:[python.example_code.textract.helper.check_job_queue]

    # snippet-start:[python.example_code.textract.StartDocumentTextDetection]
    def start_detection_job(
        self, bucket_name, document_file_name, sns_topic_arn, sns_role_arn
    ):
        """
        Starts an asynchronous job to detect text elements in an image stored in an
        Amazon S3 bucket. Textract publishes a notification to the specified Amazon SNS
        topic when the job completes.
        The image must be in PNG, JPG, or PDF format.

        :param bucket_name: The name of the Amazon S3 bucket that contains the image.
        :param document_file_name: The name of the document image stored in Amazon S3.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of an Amazon SNS topic
                              where the job completion notification is published.
        :param sns_role_arn: The ARN of an AWS Identity and Access Management (IAM)
                             role that can be assumed by Textract and grants permission
                             to publish to the Amazon SNS topic.
        :return: The ID of the job.
        """
        try:
            response = self.textract_client.start_document_text_detection(
                DocumentLocation={
                    "S3Object": {"Bucket": bucket_name, "Name": document_file_name}
                },
                NotificationChannel={
                    "SNSTopicArn": sns_topic_arn,
                    "RoleArn": sns_role_arn,
                },
            )
            job_id = response["JobId"]
            logger.info(
                "Started text detection job %s on %s.", job_id, document_file_name
            )
        except ClientError:
            logger.exception("Couldn't detect text in %s.", document_file_name)
            raise
        else:
            return job_id

    # snippet-end:[python.example_code.textract.StartDocumentTextDetection]

    # snippet-start:[python.example_code.textract.GetDocumentTextDetection]
    def get_detection_job(self, job_id):
        """
        Gets data for a previously started text detection job.

        :param job_id: The ID of the job to retrieve.
        :return: The job data, including a list of blocks that describe elements
                 detected in the image.
        """
        try:
            response = self.textract_client.get_document_text_detection(JobId=job_id)
            job_status = response["JobStatus"]
            logger.info("Job %s status is %s.", job_id, job_status)
        except ClientError:
            logger.exception("Couldn't get data for job %s.", job_id)
            raise
        else:
            return response

    # snippet-end:[python.example_code.textract.GetDocumentTextDetection]

    # snippet-start:[python.example_code.textract.StartDocumentAnalysis]
    def start_analysis_job(
        self,
        bucket_name,
        document_file_name,
        feature_types,
        sns_topic_arn,
        sns_role_arn,
    ):
        """
        Starts an asynchronous job to detect text and additional elements, such as
        forms or tables, in an image stored in an Amazon S3 bucket. Textract publishes
        a notification to the specified Amazon SNS topic when the job completes.
        The image must be in PNG, JPG, or PDF format.

        :param bucket_name: The name of the Amazon S3 bucket that contains the image.
        :param document_file_name: The name of the document image stored in Amazon S3.
        :param feature_types: The types of additional document features to detect.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of an Amazon SNS topic
                              where job completion notification is published.
        :param sns_role_arn: The ARN of an AWS Identity and Access Management (IAM)
                             role that can be assumed by Textract and grants permission
                             to publish to the Amazon SNS topic.
        :return: The ID of the job.
        """
        try:
            response = self.textract_client.start_document_analysis(
                DocumentLocation={
                    "S3Object": {"Bucket": bucket_name, "Name": document_file_name}
                },
                NotificationChannel={
                    "SNSTopicArn": sns_topic_arn,
                    "RoleArn": sns_role_arn,
                },
                FeatureTypes=feature_types,
            )
            job_id = response["JobId"]
            logger.info(
                "Started text analysis job %s on %s.", job_id, document_file_name
            )
        except ClientError:
            logger.exception("Couldn't analyze text in %s.", document_file_name)
            raise
        else:
            return job_id

    # snippet-end:[python.example_code.textract.StartDocumentAnalysis]

    # snippet-start:[python.example_code.textract.GetDocumentAnalysis]
    def get_analysis_job(self, job_id):
        """
        Gets data for a previously started detection job that includes additional
        elements.

        :param job_id: The ID of the job to retrieve.
        :return: The job data, including a list of blocks that describe elements
                 detected in the image.
        """
        try:
            response = self.textract_client.get_document_analysis(JobId=job_id)
            job_status = response["JobStatus"]
            logger.info("Job %s status is %s.", job_id, job_status)
        except ClientError:
            logger.exception("Couldn't get data for job %s.", job_id)
            raise
        else:
            return response


# snippet-end:[python.example_code.textract.GetDocumentAnalysis]
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
# kick off a text detection job. This returns a job ID.
job_id = textractWrapper.start_detection_job(bucket_name=bucket_name, document_file_name=file_name,
                                    sns_topic_arn=sns_topic_arn, sns_role_arn=sns_role_arn)
```

Once the job completes, this will return a dictionary with the following keys:

`dict_keys(['DocumentMetadata', 'JobStatus', 'NextToken', 'Blocks', 'AnalyzeDocumentModelVersion', 'ResponseMetadata'])`

This response corresponds to one chunk of information parsed by Textract. The number of chunks a document is parsed into depends on the length of the document. The two keys we are most interested in are `Blocks` and `NextToken`. `Blocks` contains all of the information that was extracted from this chunk, while `NextToken` tells us what chunk comes next, if any.

Textract returns an information-rich representation of the extracted text, such as their position on the page and hierarchical relationships with other entities, all the way down to the individual word level. Since we are only interested in the raw text, we need a way to parse through all of the chunks and their `Blocks`. Lucky for us, Amazon provides some [helper functions](https://github.com/aws-samples/textract-paragraph-identification/tree/main) for this purpose, which we utilize below.

```python PYTHON
def get_text_results_from_textract(job_id):
    response = textract_client.get_document_text_detection(JobId=job_id)
    collection_of_textract_responses = []
    pages = [response]

    collection_of_textract_responses.append(response)

    while 'NextToken' in response:
        next_token = response['NextToken']
        response = textract_client.get_document_text_detection(JobId=job_id, NextToken=next_token)
        pages.append(response)
        collection_of_textract_responses.append(response)
    return collection_of_textract_responses

def get_the_text_with_required_info(collection_of_textract_responses):
    total_text = []
    total_text_with_info = []
    running_sequence_number = 0

    font_sizes_and_line_numbers = {}
    for page in collection_of_textract_responses:
        per_page_text = []
        blocks = page['Blocks']
        for block in blocks:
            if block['BlockType'] == 'LINE':
                block_text_dict = {}
                running_sequence_number += 1
                block_text_dict.update(text=block['Text'])
                block_text_dict.update(page=block['Page'])
                block_text_dict.update(left_indent=round(block['Geometry']['BoundingBox']['Left'], 2))
                font_height = round(block['Geometry']['BoundingBox']['Height'], 3)
                line_number = running_sequence_number
                block_text_dict.update(font_height=round(block['Geometry']['BoundingBox']['Height'], 3))
                block_text_dict.update(indent_from_top=round(block['Geometry']['BoundingBox']['Top'], 2))
                block_text_dict.update(text_width=round(block['Geometry']['BoundingBox']['Width'], 2))
                block_text_dict.update(line_number=running_sequence_number)

                if font_height in font_sizes_and_line_numbers:
                    line_numbers = font_sizes_and_line_numbers[font_height]
                    line_numbers.append(line_number)
                    font_sizes_and_line_numbers[font_height] = line_numbers
                else:
                    line_numbers = []
                    line_numbers.append(line_number)
                    font_sizes_and_line_numbers[font_height] = line_numbers

                total_text.append(block['Text'])
                per_page_text.append(block['Text'])
                total_text_with_info.append(block_text_dict)

    return total_text, total_text_with_info, font_sizes_and_line_numbers

def get_text_with_line_spacing_info(total_text_with_info):
    i = 1
    text_info_with_line_spacing_info = []
    while (i < len(total_text_with_info) - 1):
        previous_line_info = total_text_with_info[i - 1]
        current_line_info = total_text_with_info[i]
        next_line_info = total_text_with_info[i + 1]
        if current_line_info['page'] == next_line_info['page'] and previous_line_info['page'] == current_line_info[
            'page']:
            line_spacing_after = round((next_line_info['indent_from_top'] - current_line_info['indent_from_top']), 2)
            spacing_with_prev = round((current_line_info['indent_from_top'] - previous_line_info['indent_from_top']), 2)
            current_line_info.update(line_space_before=spacing_with_prev)
            current_line_info.update(line_space_after=line_spacing_after)
            text_info_with_line_spacing_info.append(current_line_info)
        else:
            text_info_with_line_spacing_info.append(None)
        i += 1
    return text_info_with_line_spacing_info
```

We feed in the Job ID from before into the function `get_text_results_from_textract` to fetch all of the chunks associated with this job. Then, we pass the resulting list into `get_the_text_with_required_info` and `get_text_with_line_spacing_info` to organize the text into lines.

Finally, we can concatenate the lines into one string to pass into our downstream RAG pipeline.

```python PYTHON
all_text = "\n".join([line["text"] if line else "" for line in text_info_with_line_spacing])

with open(f"aws-parsed-{source_filename}.txt", "w") as f:
  f.write(all_text)
```

#### Visualize the parsed document

```python PYTHON
filename = "aws-parsed-{}.txt".format(source_filename)
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

### Solution 3: Unstructured.io [\[Back to Solutions\]](#top) \[#unstructured]

Unstructured.io provides libraries with open-source components for pre-processing text documents such as PDFs, HTML and Word Documents.

External documentation: [https://github.com/Unstructured-IO/unstructured-api](https://github.com/Unstructured-IO/unstructured-api)

#### Parsing the document

The guide assumes an endpoint exists that hosts this service. The API is offered in two forms

1. [a hosted version](https://unstructured.io/)
2. [an OSS docker image](https://github.com/Unstructured-IO/unstructured-api?tab=readme-ov-file#dizzy-instructions-for-using-the-docker-image)

**Note: You can skip to the next block if you want to use the pre-existing parsed version.**

```python PYTHON
import os
import requests

UNSTRUCTURED_URL = "" # enter service endpoint, for example "http://localhost:9500/general/v0/general" (assuming the container is running locally and exposing the service with a -p 9500:9500 port mapping)


parsed_documents = []

input_path = "{}/{}.{}".format(data_dir, source_filename, extension)
with open(input_path, 'rb') as file_data:
    response = requests.post(
        url=UNSTRUCTURED_URL,
        files={"files": ("{}.{}".format(source_filename, extension), file_data)},
        data={
            "output_format": (None, "application/json"),
            "strategy": "fast",
            "pdf_infer_table_structure": "true",
            "include_page_breaks": "true"
        },
        headers={"Accept": "application/json"}
    )

parsed_response = response.json()

parsed_document = " ".join([parsed_entry["text"] for parsed_entry in parsed_response])
print("Parsed {}".format(source_filename))
```

```python PYTHON
"""
Post process parsed document and store it locally.
"""

file_path = "{}/{}-parsed-fda-approved-drug.txt".format(data_dir, "unstructured-io")
store_document(file_path, parsed_document)
```

#### Visualize the parsed document

```python PYTHON
filename = "unstructured-io-parsed-{}.txt".format(source_filename)
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

### Solution 4: LlamaParse [\[Back to Solutions\]](#top) \[#llama]

LlamaParse is an API created by LlamaIndex to efficiently parse and represent files for efficient retrieval and context augmentation using LlamaIndex frameworks.

External documentation: [https://github.com/run-llama/llama\_parse](https://github.com/run-llama/llama_parse)

#### Parsing the document

The following block uses the LlamaParse cloud offering. You can learn more and fetch a respective API key for the service [here](https://cloud.llamaindex.ai/parse).

Parsing documents with LlamaParse offers an option for two output modes both of which we will explore and compare below

* Text
* Markdown

**Note: You can skip to the next block if you want to use the pre-existing parsed version.**

```python PYTHON
import os
from llama_parse import LlamaParse

import nest_asyncio # needed to notebook env
nest_asyncio.apply() # needed to notebook env

llama_index_api_key = "{API_KEY}"
input_path = "{}/{}.{}".format(data_dir, source_filename, extension)
```

```python PYTHON
# Text mode
text_parser = LlamaParse(
    api_key=llama_index_api_key,
    result_type="text"
)

text_response = text_parser.load_data(input_path)
text_parsed_document = " ".join([parsed_entry.text for parsed_entry in text_response])

print("Parsed {} to text".format(source_filename))
```

```python PYTHON
"""
Post process parsed document and store it locally.
"""

file_path = "{}/{}-text-parsed-fda-approved-drug.txt".format(data_dir, "llamaparse")
store_document(file_path, text_parsed_document)
```

```python PYTHON
# Markdown mode
markdown_parser = LlamaParse(
    api_key=llama_index_api_key,
    result_type="markdown"
)

markdown_response = markdown_parser.load_data(input_path)
markdown_parsed_document = " ".join([parsed_entry.text for parsed_entry in markdown_response])

print("Parsed {} to markdown".format(source_filename))
```

```python PYTHON
"""
Post process parsed document and store it locally.
"""

file_path = "{}/{}-markdown-parsed-fda-approved-drug.txt".format(data_dir, "llamaparse")
store_document(file_path, markdown_parsed_document)
```

#### Visualize the parsed document

```python PYTHON
# Text parsing

filename = "llamaparse-text-parsed-{}.txt".format(source_filename)

with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

```python PYTHON
# Markdown parsing

filename = "llamaparse-markdown-parsed-fda-approved-drug.txt"
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

### Solution 5: pdf2image + pytesseract [\[Back to Solutions\]](#top) \[#pdf2image]

The final parsing method we examine does not rely on cloud services, but rather relies on two libraries: `pdf2image`, and `pytesseract`. `pytesseract` lets you perform OCR locally on images, but not PDF files. So, we first convert our PDF into a set of images via `pdf2image`.

#### Parsing the document

```python PYTHON
from matplotlib import pyplot as plt
from pdf2image import convert_from_path
import pytesseract
```

```python PYTHON
# pdf2image extracts as a list of PIL.Image objects
pages = convert_from_path(filename)
```

```python PYTHON
# we look at the first page as a sanity check:

plt.imshow(pages[0])
plt.axis('off')
plt.show()
```

Now, we can process the image of each page with `pytesseract` and concatenate the results to get our parsed document.

```python PYTHON
label_ocr_pytesseract = "".join([pytesseract.image_to_string(page) for page in pages])
```

```python PYTHON
print(label_ocr_pytesseract[:200])
```

```txt title="Output"
HIGHLIGHTS OF PRESCRIBING INFORMATION

These highlights do not include all the information needed to use
IWILFIN™ safely and effectively. See full prescribing information for
IWILFIN.

IWILFIN™ (eflor
```

```python PYTHON
label_ocr_pytesseract = "".join([pytesseract.image_to_string(page) for page in pages])

with open(f"pytesseract-parsed-{source_filename}.txt", "w") as f:
  f.write(label_ocr_pytesseract)
```

#### Visualize the parsed document

```python PYTHON
filename = "pytesseract-parsed-{}.txt".format(source_filename)
with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```

## Document Questions \[#document-questions]

We can now ask a set of simple + complex questions and see how each parsing solution performs with Command-R. The questions are

* **What are the most common adverse reactions of Iwilfin?**
  * Task: Simple information extraction
* **What is the recommended dosage of IWILFIN on body surface area between 0.5 and 0.75?**
  * Task: Tabular data extraction
* **I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin.**
  * Task: Overall document summary

```python PYTHON
import cohere
co = cohere.Client(api_key="{API_KEY}")
```

```python PYTHON
"""
Document Questions
"""
prompt = "What are the most common adverse reactions of Iwilfin?"
# prompt = "What is the recommended dosage of Iwilfin on body surface area between 0.5 m2 and 0.75 m2?"
# prompt = "I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin."

"""
Choose one of the above solutions
"""
source = "gcp"
# source = "aws"
# source = "unstructured-io"
# source = "llamaparse-text"
# source = "llamaparse-markdown"
# source = "pytesseract"
```

## Data Ingestion \[#ingestion]

In order to set up our RAG implementation, we need to separate the parsed text into chunks and load the chunks to an index. The index will allow us to retrieve relevant passages from the document for different queries. Here, we use a simple implementation of indexing using the `hnswlib` library. Note that there are many different indexing solutions that are appropriate for specific production use cases.

```python PYTHON
"""
Read parsed document content and chunk data
"""

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = []

with open("{}/{}-parsed-fda-approved-drug.txt".format(data_dir, source), "r") as doc:
    doc_content = doc.read()

"""
Personal notes on chunking
https://medium.com/@ayhamboucher/llm-based-context-splitter-for-large-documents-445d3f02b01b
"""


# Chunk doc content
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False
)

# Split the text into chunks with some overlap
chunks_ = text_splitter.create_documents([doc_content])
documents = [c.page_content for c in chunks_]

print("Source document has been broken down to {} chunks".format(len(documents)))
```

```python PYTHON
"""
Embed document chunks
"""
document_embeddings = co.embed(texts=documents, model="embed-v4.0", input_type="search_document").embeddings
```

```python PYTHON
"""
Create document index and add embedded chunks
"""

import hnswlib

index = hnswlib.Index(space='ip', dim=1536) # space: inner product
index.init_index(max_elements=len(document_embeddings), ef_construction=512, M=64)
index.add_items(document_embeddings, list(range(len(document_embeddings))))
print("Count:", index.element_count)
```

```txt title="Output"
Count: 115
```

## Retrieval

In this step, we use k-nearest neighbors to fetch the most relevant documents for our query. Once the nearest neighbors are retrieved, we use Cohere's reranker to reorder the documents in the most relevant order with regards to our input search query.

```python PYTHON
"""
Embed search query
Fetch k nearest neighbors
"""

query_emb = co.embed(texts=[prompt], model='embed-v4.0', input_type="search_query").embeddings
default_knn = 10
knn = default_knn if default_knn <= index.element_count else index.element_count
result = index.knn_query(query_emb, k=knn)
neighbors = [(result[0][0][i], result[1][0][i]) for i in range(len(result[0][0]))]
relevant_docs = [documents[x[0]] for x in sorted(neighbors, key=lambda x: x[1])]
```

```python PYTHON
"""
Rerank retrieved documents
"""

rerank_results = co.rerank(query=prompt, documents=relevant_docs, top_n=3, model='rerank-english-v2.0').results
reranked_relevant_docs = format_docs_for_chat([x.document["text"] for x in rerank_results])
```

## Final Step: Call Command-A + RAG!

```python PYTHON
"""
Call the /chat endpoint with command-a
"""

response = co.chat(
    message=prompt,
    model="command-a-03-2025",
    documents=reranked_relevant_docs
)

cited_response, citations_reference = insert_citations_in_order(response.text, response.citations, reranked_relevant_docs)
print(cited_response)
print("\n")
print("References:")
print(citations_reference)
```

## Head-to-head Comparisons

Run the code cells below to make head to head comparisons of the different parsing techniques across different questions.

```python PYTHON
import pandas as pd
results = pd.read_csv("{}/results-table.csv".format(data_dir))
```

```python PYTHON
question = input("""
Question 1: What are the most common adverse reactions of Iwilfin?
Question 2: What is the recommended dosage of Iwilfin on body surface area between 0.5 m2 and 0.75 m2?
Question 3: I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin.

Pick which question you want to see (1,2,3):  """)
references = input("Do you want to see the references as well? References are long and noisy (y/n): ")
print("\n\n")

index = {"1": 0, "2": 3, "3": 6}[question]

for src in ["gcp", "aws", "unstructured-io", "llamaparse-text", "llamaparse-markdown", "pytesseract"]:
  print("| {} |".format(src))
  print("\n")
  print(results[src][index])
  if references == "y":
    print("\n")
    print("References:")
    print(results[src][index+1])
  print("\n")
```

```txt title="Output"
Question 1: What are the most common adverse reactions of Iwilfin?
Question 2: What is the recommended dosage of Iwilfin on body surface area between 0.5 m2 and 0.75 m2?
Question 3: I need a succinct summary of the compound name, indication, route of administration, and mechanism of action of Iwilfin.

Pick which question you want to see (1,2,3):  3
Do you want to see the references as well? References are long and noisy (y/n): n



| gcp |


Compound Name: eflornithine hydrochloride ([0], [1], [2]) (IWILFIN ([1])™)

Indication: used to reduce the risk of relapse in adult and paediatric patients with high-risk neuroblastoma (HRNB) ([1], [3]), who have responded at least partially to prior multiagent, multimodality therapy. ([1], [3], [4])

Route of Administration: IWILFIN™ tablets ([1], [3], [4]) are taken orally twice daily ([3], [4]), with doses ranging from 192 to 768 mg based on body surface area. ([3], [4])

Mechanism of Action: IWILFIN™ is an ornithine decarboxylase inhibitor. ([0], [2])



| aws |


Compound Name: eflornithine ([0], [1], [2], [3]) (IWILFIN ([0])™)

Indication: used to reduce the risk of relapse ([0], [3]) in adults ([0], [3]) and paediatric patients ([0], [3]) with high-risk neuroblastoma (HRNB) ([0], [3]) who have responded to prior therapies. ([0], [3], [4])

Route of Administration: Oral ([2], [4])

Mechanism of Action: IWILFIN is an ornithine decarboxylase inhibitor. ([1])


| unstructured-io |


Compound Name: Iwilfin ([1], [2], [3], [4]) (eflornithine) ([0], [2], [3], [4])

Indication: Iwilfin is indicated to reduce the risk of relapse ([1], [3]) in adult and paediatric patients ([1], [3]) with high-risk neuroblastoma (HRNB) ([1], [3]), who have responded to prior anti-GD2 ([1]) immunotherapy ([1], [4]) and multi-modality therapy. ([1])

Route of Administration: Oral ([0], [3])

Mechanism of Action: Iwilfin is an ornithine decarboxylase inhibitor. ([1], [2], [3], [4])


| llamaparse-text |


Compound Name: IWILFIN ([2], [3]) (eflornithine) ([3])

Indication: IWILFIN is used to reduce the risk of relapse ([1], [2], [3]) in adult and paediatric patients ([1], [2], [3]) with high-risk neuroblastoma (HRNB) ([1], [2], [3]), who have responded at least partially to certain prior therapies. ([2], [3])

Route of Administration: IWILFIN is administered as a tablet. ([2])

Mechanism of Action: IWILFIN is an ornithine decarboxylase inhibitor. ([0], [1], [4])


| llamaparse-markdown |


Compound Name: IWILFIN ([1], [2]) (eflornithine) ([1])

Indication: IWILFIN is indicated to reduce the risk of relapse ([1], [2]) in adult and paediatric patients ([1], [2]) with high-risk neuroblastoma (HRNB) ([1], [2]), who have responded at least partially ([1], [2], [3]) to prior anti-GD2 immunotherapy ([1], [2]) and multiagent, multimodality therapy. ([1], [2], [3])

Route of Administration: Oral ([0], [1], [3], [4])

Mechanism of Action: IWILFIN acts as an ornithine decarboxylase inhibitor. ([1])


| pytesseract |


Compound Name: IWILFIN™ ([0], [2]) (eflornithine) ([0], [2])

Indication: IWILFIN is indicated to reduce the risk of relapse ([0], [2]) in adult and paediatric patients ([0], [2]) with high-risk neuroblastoma (HRNB) ([0], [2]), who have responded positively to prior anti-GD2 immunotherapy and multiagent, multimodality therapy. ([0], [2], [4])

Route of Administration: IWILFIN is administered orally ([0], [1], [3], [4]), in the form of a tablet. ([1])

Mechanism of Action: IWILFIN acts as an ornithine decarboxylase inhibitor. ([0])
```


# End-to-end RAG using Elasticsearch and Cohere

> This page contains a basic tutorial on how to get Cohere and ElasticSearch to work well together.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Cohere_Elastic_Guide.ipynb" />

Learn how to use the [Inference API](https://www.elastic.co/guide/en/elasticsearch/reference/current/inference-apis.html) for semantic search and use [Cohere's APIs](https://docs.cohere.com/docs/the-cohere-platform) for RAG.

For this example, you will need:

* An Elastic Serverless account through [Elastic Cloud](https://www.elastic.co/guide/en/cloud/current/ec-getting-started.html), available with a [free trial](https://cloud.elastic.co/registration?utm_source=github\&utm_content=elasticsearch-labs-notebook)

* A [Cohere account](https://cohere.com/) with a production API key

* Python 3.7 or higher

Note: While this tutorial integrates Cohere with an Elastic Cloud serverless project, you can also integrate with your self-managed Elasticsearch deployment or Elastic Cloud deployment by simply switching from using a Serverless endpoint in the Elasticsearch client.

If you don't have an Elastic Cloud deployment, sign up [here](https://cloud.elastic.co/registration?utm_source=github\&utm_content=elasticsearch-labs-notebook) for a free trial and request access to Elastic Serverless

To get started, we'll need to connect to our Elastic Serverless deployment using the Python client.

First we need to `pip` install the following packages:

* `elasticsearch_serverless`
* `cohere`

After installing, in the Serverless dashboard, find your endpoint URL, and create your API key.

```python PYTHON
pip install elasticsearch_serverless cohere
```

Next, we need to import the modules we need. 🔐 NOTE: getpass enables us to securely prompt the user for credentials without echoing them to the terminal, or storing it in memory.

```python PYTHON
from elasticsearch_serverless import Elasticsearch, helpers
from getpass import getpass
import cohere
import json
import requests
```

Now we can instantiate the Python Elasticsearch client.

First we prompt the user for their endpoint and encoded API key.
Then we create a `client` object that instantiates an instance of the `Elasticsearch` class.

When creating your Elastic Serverless API key make sure to turn on Control security privileges, and edit cluster privileges to specify `"cluster": ["all"]`

```python PYTHON
ELASTICSEARCH_ENDPOINT = getpass("Elastic Endpoint: ")
ELASTIC_API_KEY = getpass("Elastic encoded API key: ") # Use the encoded API key

client = Elasticsearch(
  ELASTICSEARCH_ENDPOINT,
  api_key=ELASTIC_API_KEY
)
```

Confirm that the client has connected with this test:

```python PYTHON
print(client.info())
```

## Create the inference endpoint

Let's create the inference endpoint by using the [Create inference API](https://www.elastic.co/guide/en/elasticsearch/reference/current/put-inference-api.html).

You'll need an Cohere API key for this that you can find in your Cohere account under the [API keys section](https://dashboard.cohere.com/api-keys). A production key is required to complete the steps in this notebook as the Cohere free trial API usage is limited.

```python PYTHON
COHERE_API_KEY = getpass("Enter Cohere API key:  ")

client.options(ignore_status=[404]).inference.delete_model(inference_id="cohere_embeddings")

client.inference.put_model(
    task_type="text_embedding",
    inference_id="cohere_embeddings",
    body={
        "service": "cohere",
        "service_settings": {
            "api_key": COHERE_API_KEY,
            "model_id": "embed-v4.0",
            "embedding_type": "int8",
            "similarity": "cosine"
        },
        "task_settings": {},
    },
)
```

## Create an ingest pipeline with an inference processor

Create an ingest pipeline with an inference processor by using the [`put_pipeline`](https://www.elastic.co/guide/en/elasticsearch/reference/current/put-pipeline-api.html) method. Reference the inference endpoint created above as the `model_id` to infer against the data that is being ingested in the pipeline.

```python PYTHON
client.options(ignore_status=[404]).ingest.delete_pipeline(id="cohere_embeddings")

client.ingest.put_pipeline(
    id="cohere_embeddings",
    description="Ingest pipeline for Cohere inference.",
    processors=[
        {
            "inference": {
                "model_id": "cohere_embeddings",
                "input_output": {
                    "input_field": "text",
                    "output_field": "text_embedding",
                },
            }
        }
    ],
)
```

Let's note a few important parameters from that API call:

* `inference`: A processor that performs inference using a machine learning model.
* `model_id`: Specifies the ID of the inference endpoint to be used. In this example, the model ID is set to `cohere_embeddings`.
* `input_output`: Specifies input and output fields.
* `input_field`: Field name from which the `dense_vector` representation is created.
* `output_field`: Field name which contains inference results.

## Create index

The mapping of the destination index – the index that contains the embeddings that the model will create based on your input text – must be created. The destination index must have a field with the [dense\_vector](https://www.elastic.co/guide/en/elasticsearch/reference/current/dense-vector.html) field type to index the output of the Cohere model.

Let's create an index named `cohere-wiki-embeddings` with the mappings we need.

```python PYTHON
client.indices.delete(index="cohere-wiki-embeddings", ignore_unavailable=True)
client.indices.create(
    index="cohere-wiki-embeddings",
    settings={"index": {"default_pipeline": "cohere_embeddings"}},
    mappings={
        "properties": {
            "text_embedding": {
                "type": "dense_vector",
                "dims": 1024,
                "element_type": "byte"
            },
            "text": {"type": "text"},
            "wiki_id": {"type": "integer"},
            "url": {"type": "text"},
            "views": {"type": "float"},
            "langs": {"type": "integer"},
            "title": {"type": "text"},
            "paragraph_id": {"type": "integer"},
            "id": {"type": "integer"}
        }
    },
)
```

## Insert Documents

Let's insert our example wiki dataset. You need a production Cohere account to complete this step, otherwise the documentation ingest will time out due to the API request rate limits.

```python PYTHON
url = "https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/embed_jobs_sample_data.jsonl"
response = requests.get(url)

jsonl_data = response.content.decode('utf-8').splitlines()

documents = []
for line in jsonl_data:
    data_dict = json.loads(line)
    documents.append({
        "_index": "cohere-wiki-embeddings",
        "_source": data_dict,
        }
      )

helpers.bulk(client, documents)

print("Done indexing documents into `cohere-wiki-embeddings` index!")
```

## Hybrid search

After the dataset has been enriched with the embeddings, you can query the data using hybrid search.

Pass a `query_vector_builder` to the k-nearest neighbor (kNN) vector search API, and provide the query text and the model you have used to create the embeddings.

```python PYTHON
query = "When were the semi-finals of the 2022 FIFA world cup played?"

response = client.search(
    index="cohere-wiki-embeddings",
    size=100,
    knn={
        "field": "text_embedding",
        "query_vector_builder": {
            "text_embedding": {
                "model_id": "cohere_embeddings",
                "model_text": query,
            }
        },
        "k": 10,
        "num_candidates": 50,
    },
    query={
      "multi_match": {
          "query": query,
          "fields": ["text", "title"]
        }
      }
)

raw_documents = response["hits"]["hits"]

for document in raw_documents[0:10]:
  print(f'Title: {document["_source"]["title"]}\nText: {document["_source"]["text"]}\n')

documents = []
for hit in response["hits"]["hits"]:
    documents.append(hit["_source"]["text"])
```

## Ranking

In order to effectively combine the results from our vector and BM25 retrieval, we can use Cohere's Rerank 3 model through the inference API to provide a final, more precise, semantic reranking of our results.

First, create an inference endpoint with your Cohere API key. Make sure to specify a name for your endpoint, and the model\_id of one of the rerank models. In this example we will use Rerank 3.

```python PYTHON
client.options(ignore_status=[404]).inference.delete_model(inference_id="cohere_rerank")

client.inference.put_model(
    task_type="rerank",
    inference_id="cohere_rerank",
    body={
        "service": "cohere",
        "service_settings":{
            "api_key": COHERE_API_KEY,
            "model_id": "rerank-english-v3.0"
           },
        "task_settings": {
            "top_n": 10,
        },
    }
)
```

You can now rerank your results using that inference endpoint. Here we will pass in the query we used for retrieval, along with the documents we just retrieved using hybrid search.

The inference service will respond with a list of documents in descending order of relevance. Each document has a corresponding index (reflecting to the order the documents were in when sent to the inference endpoint), and if the “return\_documents” task setting is True, then the document texts will be included as well.

In this case we will set the response to False and will reconstruct the input documents based on the index returned in the response.

```python PYTHON
response = client.inference.inference(
    inference_id="cohere_rerank",
    body={
        "query": query,
        "input": documents,
        "task_settings": {
            "return_documents": False
            }
        }
)

ranked_documents = []
for document in response.body["rerank"]:
  ranked_documents.append({
      "title": raw_documents[int(document["index"])]["_source"]["title"],
      "text": raw_documents[int(document["index"])]["_source"]["text"]
  })

for document in ranked_documents[0:10]:
  print(f"Title: {document['title']}\nText: {document['text']}\n")
```

Now that we have ranked our results, we can easily turn this into a RAG system with Cohere's Chat API. Pass in the retrieved documents, along with the query and see the grounded response using Cohere's newest generative model Command R+.

First, we will create the Cohere client.

```python PYTHON
co = cohere.Client(COHERE_API_KEY)
```

Next, we can easily get a grounded generation with citations from the Cohere Chat API. We simply pass in the user query and documents retrieved from Elastic to the API, and print out our grounded response.

```python PYTHON
response = co.chat(
    message=query,
    documents=ranked_documents,
    model='command-a-03-2025'
)

source_documents = []
for citation in response.citations:
  for document_id in citation.document_ids:
    if document_id not in source_documents:
      source_documents.append(document_id)

print(f"Query: {query}")
print(f"Response: {response.text}")
print("Sources:")
for document in response.documents:
  if document['id'] in source_documents:
    print(f"{document['title']}: {document['text']}")
```

And there you have it! A quick and easy implementation of hybrid search and RAG with Cohere and Elastic.


# Serverless Semantic Search with Cohere and Pinecone

> This page contains a basic tutorial on how to get Cohere and the Pinecone vector database to work well together.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Embed_Jobs_Serverless_Pinecone_Semantic_Search.ipynb" />

```python PYTHON
import os
import json
import time
import numpy as np
import cohere
from pinecone import Pinecone

co = cohere.Client('COHERE_API_KEY')
pc = Pinecone(
    api_key="PINECONE_API_KEY",
    source_tag="cohere"
)
```

```txt title="Output"
/usr/local/lib/python3.10/dist-packages/pinecone/data/index.py:1: TqdmExperimentalWarning: Using `tqdm.autonotebook.tqdm` in notebook mode. Use `tqdm.tqdm` instead to force console mode (e.g. in jupyter console)
    from tqdm.autonotebook import tqdm
```

## Step 1: Upload a dataset

```python PYTHON
dataset_file_path = "data/embed_jobs_sample_data.jsonl" # Full path - https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/embed_jobs_sample_data.jsonl

ds=co.create_dataset(
	name='sample_file',
	# insert your file path here - you can upload it on the right - we accept .csv and jsonl files
	data=open(dataset_file_path, 'rb'),
	dataset_type="embed-input"
	)

print(ds.await_validation())
```

```txt title="Output"
uploading file, starting validation...
sample-file-2gwgxq was uploaded
...


cohere.Dataset {
    id: sample-file-2gwgxq
    name: sample_file
    dataset_type: embed-input
    validation_status: validated
    created_at: 2024-01-13 02:47:32.563080
    updated_at: 2024-01-13 02:47:32.563081
    download_urls: ['']
    validation_error: None
    validation_warnings: []
}
```

## Step 2: Create embeddings via Cohere's Embed Jobs endpoint

```python PYTHON
job = co.create_embed_job(dataset_id=ds.id,
                          input_type='search_document',
                          model='embed-english-v3.0',
                          embeddings_types=['float'])

job.wait() # poll the server until the job is completed
```

```txt title="Output"
...
...
```

```python PYTHON
print(job)
```

```bash title="Output"
cohere.EmbedJob {
    job_id: 6d691fbe-e026-436a-826a-16e70b293e51
    status: complete
    created_at: 2024-01-13T02:47:46.385016Z
    input_dataset_id: sample-file-2gwgxq
    output_urls: None
    model: embed-english-v3.0
    truncate: RIGHT
    percent_complete: 100
    output: cohere.Dataset {
      id: embeded-sample-file-mdse2h
      name: embeded-sample-file
      dataset_type: embed-result
      validation_status: validated
      created_at: 2024-01-13 02:47:47.850097
      updated_at: 2024-01-13 02:47:47.850097
      download_urls: ['']
      validation_error: None
      validation_warnings: []
  }
}
```

## Step 3: Prepare embeddings for upsert

```python PYTHON
output_dataset=co.get_dataset(job.output.id)
data_array = []
for record in output_dataset:
  data_array.append(record)

ids = [str(i) for i in range(len(data_array))]
meta = [{'text':str(data_array[i]['text'])} for i in range(len(data_array))]
embeds=[np.float32(data_array[i]['embeddings']['float']) for i in range(len(data_array))]

to_upsert = list(zip(ids, embeds, meta))
```

## Step 4: Initialize Pinecone vector database

```python PYTHON
from pinecone import ServerlessSpec

index_name = "embed-jobs-serverless-test-example"

pc.create_index(
name=index_name,
dimension=1024,
metric="cosine",
spec=ServerlessSpec(cloud='aws', region='us-west-2')
)

idx = pc.Index(index_name)
```

## Step 5: Upsert embeddings into the index

```python PYTHON
batch_size = 128

for i in range(0, len(data_array), batch_size):
    i_end = min(i+batch_size, len(data_array))
    idx.upsert(vectors=to_upsert[i:i_end])

print(idx.describe_index_stats())
```

```txt title="Output"
{'dimension': 1024,
'index_fullness': 0.0,
'namespaces': {'': {'vector_count': 3664}},
'total_vector_count': 3664}
```

## Step 6: Query the index

```python PYTHON
query = "What did Microsoft announce in Las Vegas?"

xq = co.embed(
    texts=[query],
    model='embed-english-v3.0',
    input_type='search_query',
    truncate='END'
).embeddings

print(np.array(xq).shape)

res = idx.query(xq, top_k=20, include_metadata=True)
```

```txt title="Output"
(1, 1024)
```

```python PYTHON
for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```txt title="Output"
0.48: On October 22, 2012, Microsoft announced the release of new features including co-authoring, performance improvements and touch support.
0.45: On May 2, 2019, at F8, the company announced its new vision with the tagline "the future is private". A redesign of the website and mobile app was introduced, dubbed as "FB5". The event also featured plans for improving groups, a dating platform, end-to-end encryption on its platforms, and allowing users on Messenger to communicate directly with WhatsApp and Instagram users.
0.42: On July 13, 2009, Microsoft announced at its Worldwide Partners Conference 2009 in New Orleans that Microsoft Office 2010 reached its "Technical Preview" development milestone and features of Office Web Apps were demonstrated to the public for the first time. Additionally, Microsoft announced that Office Web Apps would be made available to consumers online and free of charge, while Microsoft Software Assurance customers will have the option of running them on premises. Office 2010 beta testers were not given access to Office Web Apps at this date, and it was announced that it would be available for testers during August 2009. However, in August 2009, a Microsoft spokesperson stated that there had been a delay in the release of Office Web Apps Technical Preview and it would not be available by the end of August.
0.42: On January 17, 2017, Facebook COO Sheryl Sandberg planned to open Station F, a startup incubator campus in Paris, France. On a six-month cycle, Facebook committed to work with ten to 15 data-driven startups there. On April 18, Facebook announced the beta launch of at its annual F8 developer conference. Facebook Spaces is a virtual reality version of Facebook for Oculus VR goggles. In a virtual and shared space, users can access a curated selection of 360-degree photos and videos using their avatar, with the support of the controller. Users can access their own photos and videos, along with media shared on their newsfeed. In September, Facebook announced it would spend up to US$1 billion on original shows for its Facebook Watch platform. On October 16, it acquired the anonymous compliment app tbh, announcing its intention to leave the app independent.
0.41: On September 26, 2017, Microsoft announced that the next version of the suite for Windows desktop, Office 2019, was in development. On April 27, 2018, Microsoft released Office 2019 Commercial Preview for Windows 10. It was released to general availability for Windows 10 and for macOS on September 24, 2018.
0.41: Microsoft Office, or simply Office, is the former name of a family of client software, server software, and services developed by Microsoft. It was first announced by Bill Gates on August 1, 1988, at COMDEX in Las Vegas. Initially a marketing term for an office suite (bundled set of productivity applications), the first version of Office contained Microsoft Word, Microsoft Excel, and Microsoft PowerPoint. Over the years, Office applications have grown substantially closer with shared features such as a common spell checker, Object Linking and Embedding data integration and Visual Basic for Applications scripting language. Microsoft also positions Office as a development platform for line-of-business software under the Office Business Applications brand.
0.40: On August 12, 2009, it was announced that Office Mobile would also be released for the Symbian platform as a joint agreement between Microsoft and Nokia. It was the first time Microsoft would develop Office mobile applications for another smartphone platform. The first application to appear on Nokia Eseries smartphones was Microsoft Office Communicator. In February 2012, Microsoft released OneNote, Lync 2010, Document Connection and PowerPoint Broadcast for Symbian. In April, Word Mobile, PowerPoint Mobile and Excel Mobile joined the Office Suite.
0.40: In 2010, Microsoft introduced a software as a service platform known as Office 365, to provide cloud-hosted versions of Office's server software, including Exchange e-mail and SharePoint, on a subscription basis (competing in particular with Google Apps). Following the release of Office 2013, Microsoft began to offer Office 365 plans for the consumer market, with access to Microsoft Office software on multiple devices with free feature updates over the life of the subscription, as well as other services such as OneDrive storage.
0.40: On April 12, 2016, Zuckerberg outlined his 10-year vision, which rested on three main pillars: artificial intelligence, increased global connectivity, and virtual and augmented reality. In July, a suit was filed against the company alleging that it permitted Hamas to use it to perform assaults that cost the lives of four people. Facebook released its blueprints of Surround 360 camera on GitHub under an open-source license. In September, it won an Emmy for its animated short "Henry". In October, Facebook announced a fee-based communications tool called Workplace that aims to "connect everyone" at work. Users can create profiles, see updates from co-workers on their news feed, stream live videos and participate in secure group chats.
0.40: On January 22, 2015, the Microsoft Office blog announced that the next version of the suite for Windows desktop, Office 2016, was in development. On May 4, 2015, a public preview of Microsoft Office 2016 was released. Office 2016 was released for Mac OS X on July 9, 2015 and for Windows on September 22, 2015.
0.39: On November 6, 2013, Microsoft announced further new features including "real-time" co-authoring and an Auto-Save feature in Word (replacing the save button).
0.39: In February 2014, Office Web Apps were re-branded Office Online and incorporated into other Microsoft web services, including Calendar, OneDrive, Outlook.com, and People. Microsoft had previously attempted to unify its online services suite (including Microsoft Passport, Hotmail, MSN Messenger, and later SkyDrive) under a brand known as Windows Live, first launched in 2005. However, with the impending launch of Windows 8 and its increased use of cloud services, Microsoft dropped the Windows Live brand to emphasize that these services would now be built directly into Windows and not merely be a "bolted on" add-on. Critics had criticized the Windows Live brand for having no clear vision, as it was being applied to an increasingly broad array of unrelated services. At the same time, Windows Live Hotmail was re-launched as Outlook.com (sharing its name with the Microsoft Outlook personal information manager).
0.39: On February 18, 2021, Microsoft announced that the next version of the suite for Windows desktop, Office 2021, was in development. This new version will be supported for five years and was released on October 5, 2021.
0.38: Since Office 2013, Microsoft has promoted Office 365 as the primary means of obtaining Microsoft Office: it allows the use of the software and other services on a subscription business model, and users receive feature updates to the software for the lifetime of the subscription, including new features and cloud computing integration that are not necessarily included in the "on-premises" releases of Office sold under conventional license terms. In 2017, revenue from Office 365 overtook conventional license sales. Microsoft also rebranded most of their standard Office 365 editions as "Microsoft 365" to reflect their inclusion of features and services beyond the core Microsoft Office suite.
0.38: Microsoft has since promoted Office 365 as the primary means of purchasing Microsoft Office. Although there are still "on-premises" releases roughly every three years, Microsoft marketing emphasizes that they do not receive new features or access to new cloud-based services as they are released unlike Office 365, as well as other benefits for consumer and business markets. Office 365 revenue overtook traditional license sales for Office in 2017.
0.38: A technical preview of Microsoft Office 2013 (Build 15.0.3612.1010) was released on January 30, 2012, and a Customer Preview version was made available to consumers on July 16, 2012. It sports a revamped application interface; the interface is based on Metro, the interface of Windows Phone and Windows 8. Microsoft Outlook has received the most pronounced changes so far; for example, the Metro interface provides a new visualization for scheduled tasks. PowerPoint includes more templates and transition effects, and OneNote includes a new splash screen.
0.38: On January 21, 2015, during the "Windows 10: The Next Chapter" press event, Microsoft unveiled Office for Windows 10, Windows Runtime ports of the Android and iOS versions of the Office Mobile suite. Optimized for smartphones and tablets, they are universal apps that can run on both Windows and Windows for phones, and share similar underlying code. A simplified version of Outlook was also added to the suite. They will be bundled with Windows 10 mobile devices, and available from the Windows Store for the PC version of Windows 10. Although the preview versions were free for most editing, the release versions will require an Office 365 subscription on larger tablets (screen size larger than 10.1 inches) and desktops for editing, as with large Android tablets. Smaller tablets and phones will have most editing features for free.
0.38: In May 2018 at F8, the company announced it would offer its own dating service. Shares in competitor Match Group fell by 22%. Facebook Dating includes privacy features and friends are unable to view their friends' dating profile. In July, Facebook was charged £500,000 by UK watchdogs for failing to respond to data erasure requests. On July 18, Facebook established a subsidiary named Lianshu Science &amp; Technology in Hangzhou City, China, with $30 million ($ in dollars) of capital. All its shares are held by Facebook Hong. Approval of the registration of the subsidiary was then withdrawn, due to a disagreement between officials in Zhejiang province and the Cyberspace Administration of China. On July 26, Facebook became the first company to lose over $100 billion ($ in dollars) worth of market capitalization in one day, dropping from nearly $630 billion to $510 billion after disappointing sales reports. On July 31, Facebook said that the company had deleted 17 accounts related to the 2018 U.S. midterm elections. On September 19, Facebook announced that, for news distribution outside the United States, it would work with U.S. funded democracy promotion organizations, International Republican Institute and the National Democratic Institute, which are loosely affiliated with the Republican and Democratic parties. Through the Digital Forensic Research Lab Facebook partners with the Atlantic Council, a NATO-affiliated think tank. In November, Facebook launched smart displays branded Portal and Portal Plus (Portal+). They support Amazon's Alexa (intelligent personal assistant service). The devices include video chat function with Facebook Messenger.
0.37: The first Preview version of Microsoft Office 2016 for Mac was released on March 5, 2015. On July 9, 2015, Microsoft released the final version of Microsoft Office 2016 for Mac which includes Word, Excel, PowerPoint, Outlook and OneNote. It was immediately made available for Office 365 subscribers with either a Home, Personal, Business, Business Premium, E3 or ProPlus subscription. A non–Office 365 edition of Office 2016 was made available as a one-time purchase option on September 22, 2015.
0.37: In October 2022, Microsoft announced that it will phase out the Microsoft Office brand in favor of "Microsoft 365" by January 2023. The name will continue to be used for legacy product offerings.
```

## Step 7: Rerank the retrieved results

```python PYTHON
docs =[match['metadata']['text'] for match in res['matches']]

rerank_response = co.rerank(
  model = 'rerank-english-v2.0',
  query = query,
  documents = docs,
  top_n = 3,
)
for response in rerank_response:
  print(f"{response.relevance_score:.2f}: {response.document['text']}")
```

```txt title="Output"
0.99: Microsoft Office, or simply Office, is the former name of a family of client software, server software, and services developed by Microsoft. It was first announced by Bill Gates on August 1, 1988, at COMDEX in Las Vegas. Initially a marketing term for an office suite (bundled set of productivity applications), the first version of Office contained Microsoft Word, Microsoft Excel, and Microsoft PowerPoint. Over the years, Office applications have grown substantially closer with shared features such as a common spell checker, Object Linking and Embedding data integration and Visual Basic for Applications scripting language. Microsoft also positions Office as a development platform for line-of-business software under the Office Business Applications brand.
0.93: On January 21, 2015, during the "Windows 10: The Next Chapter" press event, Microsoft unveiled Office for Windows 10, Windows Runtime ports of the Android and iOS versions of the Office Mobile suite. Optimized for smartphones and tablets, they are universal apps that can run on both Windows and Windows for phones, and share similar underlying code. A simplified version of Outlook was also added to the suite. They will be bundled with Windows 10 mobile devices, and available from the Windows Store for the PC version of Windows 10. Although the preview versions were free for most editing, the release versions will require an Office 365 subscription on larger tablets (screen size larger than 10.1 inches) and desktops for editing, as with large Android tablets. Smaller tablets and phones will have most editing features for free.
0.87: In October 2022, Microsoft announced that it will phase out the Microsoft Office brand in favor of "Microsoft 365" by January 2023. The name will continue to be used for legacy product offerings.
```

## Another example - query and rerank

```python PYTHON
query = "What was the first youtube video about?"

xq = co.embed(
    texts=[query],
    model='embed-english-v3.0',
    input_type='search_query',
    truncate='END'
).embeddings

print(np.array(xq).shape)

res = idx.query(xq, top_k=20, include_metadata=True)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```txt title="Output"
(1, 1024)
0.66: YouTube began as a venture capital–funded technology startup. Between November 2005 and April 2006, the company raised money from various investors, with Sequoia Capital, $11.5 million, and Artis Capital Management, $8 million, being the largest two. YouTube's early headquarters were situated above a pizzeria and a Japanese restaurant in San Mateo, California. In February 2005, the company activated codice_1. The first video was uploaded April 23, 2005. Titled "Me at the zoo", it shows co-founder Jawed Karim at the San Diego Zoo and can still be viewed on the site. In May, the company launched a public beta and by November, a Nike ad featuring Ronaldinho became the first video to reach one million total views. The site launched officially on December 15, 2005, by which time the site was receiving 8 million views a day. Clips at the time were limited to 100 megabytes, as little as 30 seconds of footage.
0.58: Karim said the inspiration for YouTube first came from the Super Bowl XXXVIII halftime show controversy when Janet Jackson's breast was briefly exposed by Justin Timberlake during the halftime show. Karim could not easily find video clips of the incident and the 2004 Indian Ocean Tsunami online, which led to the idea of a video-sharing site. Hurley and Chen said that the original idea for YouTube was a video version of an online dating service, and had been influenced by the website Hot or Not. They created posts on Craigslist asking attractive women to upload videos of themselves to YouTube in exchange for a $100 reward. Difficulty in finding enough dating videos led to a change of plans, with the site's founders deciding to accept uploads of any video.
0.55: YouTube was not the first video-sharing site on the Internet; Vimeo was launched in November 2004, though that site remained a side project of its developers from CollegeHumor at the time and did not grow much, either. The week of YouTube's launch, NBC-Universal's "Saturday Night Live" ran a skit "Lazy Sunday" by The Lonely Island. Besides helping to bolster ratings and long-term viewership for "Saturday Night Live", "Lazy Sunday"'s status as an early viral video helped establish YouTube as an important website. Unofficial uploads of the skit to YouTube drew in more than five million collective views by February 2006 before they were removed when NBCUniversal requested it two months later based on copyright concerns. Despite eventually being taken down, these duplicate uploads of the skit helped popularize YouTube's reach and led to the upload of more third-party content. The site grew rapidly; in July 2006, the company announced that more than 65,000 new videos were being uploaded every day and that the site was receiving 100 million video views per day.
0.55: According to a story that has often been repeated in the media, Hurley and Chen developed the idea for YouTube during the early months of 2005, after they had experienced difficulty sharing videos that had been shot at a dinner party at Chen's apartment in San Francisco. Karim did not attend the party and denied that it had occurred, but Chen remarked that the idea that YouTube was founded after a dinner party "was probably very strengthened by marketing ideas around creating a story that was very digestible".
0.53: In December 2009, YouTube partnered with Vevo. In April 2010, Lady Gaga's "Bad Romance" became the most viewed video, becoming the first video to reach 200 million views on May 9, 2010.
0.53: YouTube is a global online video sharing and social media platform headquartered in San Bruno, California. It was launched on February 14, 2005, by Steve Chen, Chad Hurley, and Jawed Karim. It is owned by Google, and is the second most visited website, after Google Search. YouTube has more than 2.5 billion monthly users who collectively watch more than one billion hours of videos each day. , videos were being uploaded at a rate of more than 500 hours of content per minute.
0.53: YouTube has faced numerous challenges and criticisms in its attempts to deal with copyright, including the site's first viral video, Lazy Sunday, which had to be taken down, due to copyright concerns. At the time of uploading a video, YouTube users are shown a message asking them not to violate copyright laws. Despite this advice, many unauthorized clips of copyrighted material remain on YouTube. YouTube does not view videos before they are posted online, and it is left to copyright holders to issue a DMCA takedown notice pursuant to the terms of the Online Copyright Infringement Liability Limitation Act. Any successful complaint about copyright infringement results in a YouTube copyright strike. Three successful complaints for copyright infringement against a user account will result in the account and all of its uploaded videos being deleted. From 2007 to 2009 organizations including Viacom, Mediaset, and the English Premier League have filed lawsuits against YouTube, claiming that it has done too little to prevent the uploading of copyrighted material.
0.51: Some YouTube videos have themselves had a direct effect on world events, such as "Innocence of Muslims" (2012) which spurred protests and related anti-American violence internationally. TED curator Chris Anderson described a phenomenon by which geographically distributed individuals in a certain field share their independently developed skills in YouTube videos, thus challenging others to improve their own skills, and spurring invention and evolution in that field. Journalist Virginia Heffernan stated in "The New York Times" that such videos have "surprising implications" for the dissemination of culture and even the future of classical music.
0.50: Observing that face-to-face communication of the type that online videos convey has been "fine-tuned by millions of years of evolution," TED curator Chris Anderson referred to several YouTube contributors and asserted that "what Gutenberg did for writing, online video can now do for face-to-face communication." Anderson asserted that it is not far-fetched to say that online video will dramatically accelerate scientific advance, and that video contributors may be about to launch "the biggest learning cycle in human history." In education, for example, the Khan Academy grew from YouTube video tutoring sessions for founder Salman Khan's cousin into what "Forbes" Michael Noer called "the largest school in the world," with technology poised to disrupt how people learn. YouTube was awarded a 2008 George Foster Peabody Award, the website being described as a Speakers' Corner that "both embodies and promotes democracy." "The Washington Post" reported that a disproportionate share of YouTube's most subscribed channels feature minorities, contrasting with mainstream television in which the stars are largely white. A Pew Research Center study reported the development of "visual journalism," in which citizen eyewitnesses and established news organizations share in content creation. The study also concluded that YouTube was becoming an important platform by which people acquire news.
0.50: YouTube was founded by Steve Chen, Chad Hurley, and Jawed Karim. The trio were early employees of PayPal, which left them enriched after the company was bought by eBay. Hurley had studied design at the Indiana University of Pennsylvania, and Chen and Karim studied computer science together at the University of Illinois Urbana-Champaign.
0.49: In 2013, YouTube teamed up with satirical newspaper company "The Onion" to claim in an uploaded video that the video-sharing website was launched as a contest which had finally come to an end, and would shut down for ten years before being re-launched in 2023, featuring only the winning video. The video starred several YouTube celebrities, including Antoine Dodson. A video of two presenters announcing the nominated videos streamed live for 12 hours.
0.48: Since its purchase by Google, YouTube has expanded beyond the core website into mobile apps, network television, and the ability to link with other platforms. Video categories on YouTube include music videos, video clips, news, short films, feature films, documentaries, audio recordings, movie trailers, teasers, live streams, vlogs, and more. Most content is generated by individuals, including collaborations between YouTubers and corporate sponsors. Established media corporations such as Disney, Paramount, and Warner Bros. Discovery have also created and expanded their corporate YouTube channels to advertise to a larger audience.
0.47: YouTube has enabled people to more directly engage with government, such as in the CNN/YouTube presidential debates (2007) in which ordinary people submitted questions to U.S. presidential candidates via YouTube video, with a techPresident co-founder saying that Internet video was changing the political landscape. Describing the Arab Spring (2010–2012), sociologist Philip N. Howard quoted an activist's succinct description that organizing the political unrest involved using "Facebook to schedule the protests, Twitter to coordinate, and YouTube to tell the world." In 2012, more than a third of the U.S. Senate introduced a resolution condemning Joseph Kony 16 days after the "Kony 2012" video was posted to YouTube, with resolution co-sponsor Senator Lindsey Graham remarking that the video "will do more to lead to (Kony's) demise than all other action combined."
0.47: YouTube carried out early experiments with live streaming, including a concert by U2 in 2009, and a question-and-answer session with US President Barack Obama in February 2010. These tests had relied on technology from 3rd-party partners, but in September 2010, YouTube began testing its own live streaming infrastructure. In April 2011, YouTube announced the rollout of "YouTube Live". The creation of live streams was initially limited to select partners. It was used for real-time broadcasting of events such as the 2012 Olympics in London. In October 2012, more than 8 million people watched Felix Baumgartner's jump from the edge of space as a live stream on YouTube.
0.46: In June 2007, YouTube began trials of a system for automatic detection of uploaded videos that infringe copyright. Google CEO Eric Schmidt regarded this system as necessary for resolving lawsuits such as the one from Viacom, which alleged that YouTube profited from content that it did not have the right to distribute. The system, which was initially called "Video Identification" and later became known as Content ID, creates an ID File for copyrighted audio and video material, and stores it in a database. When a video is uploaded, it is checked against the database, and flags the video as a copyright violation if a match is found. When this occurs, the content owner has the choice of blocking the video to make it unviewable, tracking the viewing statistics of the video, or adding advertisements to the video.
0.46: In January 2009, YouTube launched "YouTube for TV", a version of the website tailored for set-top boxes and other TV-based media devices with web browsers, initially allowing its videos to be viewed on the PlayStation 3 and Wii video game consoles.
0.46: In September 2012, YouTube launched its first app for the iPhone, following the decision to drop YouTube as one of the preloaded apps in the iPhone 5 and iOS 6 operating system. According to GlobalWebIndex, YouTube was used by 35% of smartphone users between April and June 2013, making it the third-most used app.
0.46: Conversely, YouTube has also allowed government to more easily engage with citizens, the White House's official YouTube channel being the seventh top news organization producer on YouTube in 2012 and in 2013 a healthcare exchange commissioned Obama impersonator Iman Crosson's YouTube music video spoof to encourage young Americans to enroll in the Affordable Care Act (Obamacare)-compliant health insurance. In February 2014, U.S. President Obama held a meeting at the White House with leading YouTube content creators to not only promote awareness of Obamacare but more generally to develop ways for government to better connect with the "YouTube Generation." Whereas YouTube's inherent ability to allow presidents to directly connect with average citizens was noted, the YouTube content creators' new media savvy was perceived necessary to better cope with the website's distracting content and fickle audience.
0.46: Later that year, YouTube came under criticism for showing inappropriate videos targeted at children and often featuring popular characters in violent, sexual or otherwise disturbing situations, many of which appeared on YouTube Kids and attracted millions of views. The term "Elsagate" was coined on the Internet and then used by various news outlets to refer to this controversy. On November 11, 2017, YouTube announced it was strengthening site security to protect children from unsuitable content. Later that month, the company started to mass delete videos and channels that made improper use of family-friendly characters. As part of a broader concern regarding child safety on YouTube, the wave of deletions also targeted channels that showed children taking part in inappropriate or dangerous activities under the guidance of adults. Most notably, the company removed "Toy Freaks", a channel with over 8.5 million subscribers, that featured a father and his two daughters in odd and upsetting situations. According to analytics specialist SocialBlade, it earned up to £8.7 million annually prior to its deletion.
0.45: In September 2020, YouTube announced that it would be launching a beta version of a new platform of 15-second videos, similar to TikTok, called YouTube Shorts. The platform was first tested in India but as of March 2021 has expanded to other countries including the United States with videos now able to be up to 1 minute long. The platform is not a standalone app, but is integrated into the main YouTube app. Like TikTok, it gives users access to built-in creative tools, including the possibility of adding licensed music to their videos. The platform had its global beta launch in July 2021.
```

```python PYTHON
docs =[match['metadata']['text'] for match in res['matches']]

rerank_response = co.rerank(
  model = 'rerank-english-v2.0',
  query = query,
  documents = docs,
  top_n = 3,
)
for response in rerank_response:
  print(f"{response.relevance_score:.2f}: {response.document['text']}")
```

```txt title="Output"
0.95: YouTube began as a venture capital–funded technology startup. Between November 2005 and April 2006, the company raised money from various investors, with Sequoia Capital, $11.5 million, and Artis Capital Management, $8 million, being the largest two. YouTube's early headquarters were situated above a pizzeria and a Japanese restaurant in San Mateo, California. In February 2005, the company activated codice_1. The first video was uploaded April 23, 2005. Titled "Me at the zoo", it shows co-founder Jawed Karim at the San Diego Zoo and can still be viewed on the site. In May, the company launched a public beta and by November, a Nike ad featuring Ronaldinho became the first video to reach one million total views. The site launched officially on December 15, 2005, by which time the site was receiving 8 million views a day. Clips at the time were limited to 100 megabytes, as little as 30 seconds of footage.
0.92: Karim said the inspiration for YouTube first came from the Super Bowl XXXVIII halftime show controversy when Janet Jackson's breast was briefly exposed by Justin Timberlake during the halftime show. Karim could not easily find video clips of the incident and the 2004 Indian Ocean Tsunami online, which led to the idea of a video-sharing site. Hurley and Chen said that the original idea for YouTube was a video version of an online dating service, and had been influenced by the website Hot or Not. They created posts on Craigslist asking attractive women to upload videos of themselves to YouTube in exchange for a $100 reward. Difficulty in finding enough dating videos led to a change of plans, with the site's founders deciding to accept uploads of any video.
0.91: YouTube was not the first video-sharing site on the Internet; Vimeo was launched in November 2004, though that site remained a side project of its developers from CollegeHumor at the time and did not grow much, either. The week of YouTube's launch, NBC-Universal's "Saturday Night Live" ran a skit "Lazy Sunday" by The Lonely Island. Besides helping to bolster ratings and long-term viewership for "Saturday Night Live", "Lazy Sunday"'s status as an early viral video helped establish YouTube as an important website. Unofficial uploads of the skit to YouTube drew in more than five million collective views by February 2006 before they were removed when NBCUniversal requested it two months later based on copyright concerns. Despite eventually being taken down, these duplicate uploads of the skit helped popularize YouTube's reach and led to the upload of more third-party content. The site grew rapidly; in July 2006, the company announced that more than 65,000 new videos were being uploaded every day and that the site was receiving 100 million video views per day.
```


# Semantic Search with Cohere Embed Jobs

> This page contains a basic tutorial on how to use Cohere's Embed Jobs functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Embed_Jobs_Semantic_Search.ipynb" />

```python PYTHON
import time
import cohere
import hnswlib
co = cohere.Client('COHERE_API_KEY')
```

## Step 1: Upload a dataset

```python PYTHON

dataset_file_path = "data/embed_jobs_sample_data.jsonl" # Full path - https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/embed_jobs_sample_data.jsonl

ds=co.create_dataset(
	name='sample_file',
	data=open(dataset_file_path, 'rb'),
	keep_fields = ['id','wiki_id'],
	dataset_type="embed-input"
	)
```

```txt title="Output"
uploading file, starting validation...
sample-file-hca4x0 was uploaded
...
```

```python PYTHON
print(ds.await_validation())
```

```txt title="Output"
cohere.Dataset {
    id: sample-file-hca4x0
    name: sample_file
    dataset_type: embed-input
    validation_status: validated
    created_at: 2024-01-13 02:51:48.215973
    updated_at: 2024-01-13 02:51:48.215973
    download_urls: ['']
    validation_error: None
    validation_warnings: []
}
```

## Step 2: Create embeddings via Cohere's Embed Jobs endpoint

```python PYTHON
job = co.create_embed_job(
    dataset_id=ds.id,
    input_type='search_document' ,
    model='embed-english-v3.0',
    embeddings_types=['float'])

job.wait() # poll the server until the job is completed
```

```txt title="Output"
...
...
```

```python PYTHON
print(job)
```

```txt title="Output"
cohere.EmbedJob {
    job_id: 792bbc1a-561b-48c2-8a97-0c80c1914ea8
    status: complete
    created_at: 2024-01-13T02:53:31.879719Z
    input_dataset_id: sample-file-hca4x0
    output_urls: None
    model: embed-english-v3.0
    truncate: RIGHT
    percent_complete: 100
    output: cohere.Dataset {
    id: embeded-sample-file-drtjf9
    name: embeded-sample-file
    dataset_type: embed-result
    validation_status: validated
    created_at: 2024-01-13 02:53:33.569362
    updated_at: 2024-01-13 02:53:33.569362
    download_urls: ['']
    validation_error: None
    validation_warnings: []
}
}
```

## Step 3: Download and prepare the embeddings

```python PYTHON
embeddings_file_path = 'embed_jobs_output.csv'
output_dataset=co.get_dataset(job.output.id)
output_dataset.save(filepath=embeddings_file_path, format="csv")
```

```python PYTHON
embeddings=[]
texts=[]
for record in output_dataset:
  embeddings.append(record['embeddings']['float'])
  texts.append(record['text'])
```

## Step 4: Initialize Hnwslib index and add embeddings

```python PYTHON
index = hnswlib.Index(space='ip', dim=1024)
index.init_index(max_elements=len(embeddings), ef_construction=512, M=64)
index.add_items(embeddings,list(range(len(embeddings))))
```

## Step 5: Query the index and rerank the results

```python PYTHON
query = "What was the first youtube video about?"

query_emb=co.embed(
    texts=[query], model="embed-english-v3.0", input_type="search_query"
        ).embeddings

doc_index = index.knn_query(query_emb, k=10)[0][0]

docs_to_rerank = []
for index in doc_index:
  docs_to_rerank.append(texts[index])

final_result = co.rerank(
    query= query,
    documents=docs_to_rerank,
    model="rerank-english-v2.0",
    top_n=3)
```

## Step 6: Display the results

```python PYTHON
for idx, r in enumerate(final_result):
  print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.5f}")
  print("\n")
```

```txt title="Output"
Document Rank: 1, Document Index: 0
Document: YouTube began as a venture capital–funded technology startup. Between November 2005 and April 2006, the company raised money from various investors, with Sequoia Capital, $11.5 million, and Artis Capital Management, $8 million, being the largest two. YouTube's early headquarters were situated above a pizzeria and a Japanese restaurant in San Mateo, California. In February 2005, the company activated codice_1. The first video was uploaded April 23, 2005. Titled "Me at the zoo", it shows co-founder Jawed Karim at the San Diego Zoo and can still be viewed on the site. In May, the company launched a public beta and by November, a Nike ad featuring Ronaldinho became the first video to reach one million total views. The site launched officially on December 15, 2005, by which time the site was receiving 8 million views a day. Clips at the time were limited to 100 megabytes, as little as 30 seconds of footage.
Relevance Score: 0.94815


Document Rank: 2, Document Index: 1
Document: Karim said the inspiration for YouTube first came from the Super Bowl XXXVIII halftime show controversy when Janet Jackson's breast was briefly exposed by Justin Timberlake during the halftime show. Karim could not easily find video clips of the incident and the 2004 Indian Ocean Tsunami online, which led to the idea of a video-sharing site. Hurley and Chen said that the original idea for YouTube was a video version of an online dating service, and had been influenced by the website Hot or Not. They created posts on Craigslist asking attractive women to upload videos of themselves to YouTube in exchange for a $100 reward. Difficulty in finding enough dating videos led to a change of plans, with the site's founders deciding to accept uploads of any video.
Relevance Score: 0.91626


Document Rank: 3, Document Index: 2
Document: YouTube was not the first video-sharing site on the Internet; Vimeo was launched in November 2004, though that site remained a side project of its developers from CollegeHumor at the time and did not grow much, either. The week of YouTube's launch, NBC-Universal's "Saturday Night Live" ran a skit "Lazy Sunday" by The Lonely Island. Besides helping to bolster ratings and long-term viewership for "Saturday Night Live", "Lazy Sunday"'s status as an early viral video helped establish YouTube as an important website. Unofficial uploads of the skit to YouTube drew in more than five million collective views by February 2006 before they were removed when NBCUniversal requested it two months later based on copyright concerns. Despite eventually being taken down, these duplicate uploads of the skit helped popularize YouTube's reach and led to the upload of more third-party content. The site grew rapidly; in July 2006, the company announced that more than 65,000 new videos were being uploaded every day and that the site was receiving 100 million video views per day.
Relevance Score: 0.90665
```


# Fueling Generative Content with Keyword Research

> This page contains a basic workflow for using Cohere's models to come up with keyword content ideas.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Fueling_Generative_Content_with_Keyword_Research.ipynb" />

Generative models have proven extremely useful in content idea generation. But they don’t take into account user search demand and trends. In this notebook, let’s see how we can solve that by adding keyword research into the equation.

Read the accompanying [blog post here](https://cohere.com/blog/generative-content-keyword-research/).

```python PYTHON
! pip install cohere -q
```

```python PYTHON
import cohere
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

import cohere
co = cohere.Client("COHERE_API_KEY") # Get your API key: https://dashboard.cohere.com/api-keys
```

```python PYTHON
#@title Enable text wrapping in Google Colab

from IPython.display import HTML, display

def set_css():
  display(HTML('''

  '''))
get_ipython().events.register('pre_run_cell', set_css)
```

First, we need to get a supply of high-traffic keywords for a given topic. We can get this via keyword research tools, of which are many available. We’ll use Google Keyword Planner, which is free to use.

```python PYTHON

import wget
wget.download("https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/data/remote_teams.csv", "remote_teams.csv")
```

```
'remote_teams.csv'
```

```python PYTHON
df = pd.read_csv('remote_teams.csv')
df.columns = ["keyword","volume"]
df.head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          keyword
        </th>

        <th>
          volume
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          managing remote teams
        </td>

        <td>
          1000
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          remote teams
        </td>

        <td>
          390
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          collaboration tools for remote teams
        </td>

        <td>
          320
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          online games for remote teams
        </td>

        <td>
          320
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          how to manage remote teams
        </td>

        <td>
          260
        </td>
      </tr>
    </tbody>
  </table>
</div>

We now have a list of keywords, but this list is still raw. For example, “managing remote teams” is the top-ranking keyword in this list. But at the same time, there are many similar keywords further down in the list, such as “how to effectively manage remote teams.”

We can do that by clustering them into topics. For this, we’ll leverage Cohere’s Embed endpoint and scikit-learn.

### Embed the Keywords with Cohere Embed

The Cohere Embed endpoint turns a text input into a text embedding.

```python PYTHON
def embed_text(texts):
  output = co.embed(
                texts=texts,
                model='embed-v4.0',
                input_type="search_document",
                )
  return output.embeddings

embeds = np.array(embed_text(df['keyword'].tolist()))
```

### Cluster the Keywords into Topics with scikit-learn

We then use these embeddings to cluster the keywords. A common term used for this exercise is “topic modeling.” Here, we can leverage scikit-learn’s KMeans module, a machine learning algorithm for clustering.

```python PYTHON
NUM_TOPICS = 4
kmeans = KMeans(n_clusters=NUM_TOPICS, random_state=21, n_init="auto").fit(embeds)
df['topic'] = list(kmeans.labels_)
df.head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          keyword
        </th>

        <th>
          volume
        </th>

        <th>
          topic
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          managing remote teams
        </td>

        <td>
          1000
        </td>

        <td>
          0
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          remote teams
        </td>

        <td>
          390
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          collaboration tools for remote teams
        </td>

        <td>
          320
        </td>

        <td>
          1
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          online games for remote teams
        </td>

        <td>
          320
        </td>

        <td>
          3
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          how to manage remote teams
        </td>

        <td>
          260
        </td>

        <td>
          0
        </td>
      </tr>
    </tbody>
  </table>
</div>

### Generate Topic Names with Cohere Chat

We use the Chat to generate a topic name for that cluster.

```python PYTHON
topic_keywords_dict = {topic: list(set(group['keyword'])) for topic, group in df.groupby('topic')}
```

```python PYTHON
def generate_topic_name(keywords):
    # Construct the prompt
    prompt = f"""Generate a concise topic name that best represents these keywords.\
Provide just the topic name and not any additional details.

Keywords: {', '.join(keywords)}"""

    # Call the Cohere API
    response = co.chat(
        model='command-a-03-2025',  # Choose the model size
        message=prompt,
        preamble="")

    # Return the generated text
    return response.text
```

```python PYTHON
topic_name_mapping = {topic: generate_topic_name(keywords) for topic, keywords in topic_keywords_dict.items()}

df['topic_name'] = df['topic'].map(topic_name_mapping)

df.head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          keyword
        </th>

        <th>
          volume
        </th>

        <th>
          topic
        </th>

        <th>
          topic_name
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          managing remote teams
        </td>

        <td>
          1000
        </td>

        <td>
          0
        </td>

        <td>
          Remote Team Management
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          remote teams
        </td>

        <td>
          390
        </td>

        <td>
          1
        </td>

        <td>
          Remote Team Tools and Tips
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          collaboration tools for remote teams
        </td>

        <td>
          320
        </td>

        <td>
          1
        </td>

        <td>
          Remote Team Tools and Tips
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          online games for remote teams
        </td>

        <td>
          320
        </td>

        <td>
          3
        </td>

        <td>
          Remote Team Fun
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          how to manage remote teams
        </td>

        <td>
          260
        </td>

        <td>
          0
        </td>

        <td>
          Remote Team Management
        </td>
      </tr>
    </tbody>
  </table>
</div>

```python PYTHON
for topic, name in topic_name_mapping.items():
    print(f"Topic {topic}: {name}")
```

```
Topic 0: Remote Team Management
Topic 1: Remote Team Tools and Tips
Topic 2: Remote Team Resources
Topic 3: Remote Team Fun
```

Now that we have the keywords nicely grouped into topics, we can proceed to generate the content ideas.

### Take the Top Keywords from Each Topic

Here we can implement a filter to take just the top N keywords from each topic, sorted by the search volume. In our case, we use 10.

```python PYTHON
TOP_N = 10

top_keywords = (df.groupby('topic')
                        .apply(lambda x: x.nlargest(TOP_N, 'volume'))
                        .reset_index(drop=True))


content_by_topic = {}
for topic, group in top_keywords.groupby('topic'):
    keywords = ', '.join(list(group['keyword']))
    topic2name = topic2name = dict(df.groupby('topic')['topic_name'].first())
    topic_name = topic2name[topic]
    content_by_topic[topic] = {'topic_name': topic_name, 'keywords': keywords}
```

```python PYTHON
content_by_topic
```

```
{0: {'topic_name': 'Remote Team Management',
  'keywords': 'managing remote teams, how to manage remote teams, leading remote teams, managing remote teams best practices, remote teams best practices, best practices for managing remote teams, manage remote teams, building culture in remote teams, culture building for remote teams, managing remote teams training'},
 1: {'topic_name': 'Remote Team Tools and Tips',
  'keywords': 'remote teams, collaboration tools for remote teams, team building for remote teams, scrum remote teams, tools for remote teams, zapier remote teams, working agreements for remote teams, working with remote teams, free collaboration tools for remote teams, free retrospective tools for remote teams'},
 2: {'topic_name': 'Remote Team Resources',
  'keywords': 'best collaboration tools for remote teams, slack best practices for remote teams, best communication tools for remote teams, best tools for remote teams, always on video for remote teams, best apps for remote teams, best free collaboration tools for remote teams, best games for remote teams, best gifts for remote teams, best ice breaker questions for remote teams'},
 3: {'topic_name': 'Remote Team Fun',
  'keywords': 'online games for remote teams, team building activities for remote teams, games for remote teams, retrospective ideas for remote teams, team building ideas for remote teams, fun retrospective ideas for remote teams, retro ideas for remote teams, team building exercises for remote teams, trust building exercises for remote teams, activities for remote teams'}}
```

### Create a Prompt with These Keywords

Next, we use the Chat endpoint to produce the content ideas. The prompt we’ll use is as follows

```python PYTHON
def generate_blog_ideas(keywords):
  prompt = f"""{keywords}\n\nThe above is a list of high-traffic keywords obtained from a keyword research tool.
Suggest three blog post ideas that are highly relevant to these keywords.
For each idea, write a one paragraph abstract about the topic.
Use this format:
Blog title: <text>
Abstract: <text>"""

  response = co.chat(
    model='command-r',
    message = prompt)
  return response.text

```

### Generate Content Ideas

Next, we generate the blog post ideas. It takes in a string of keywords, calls the Chat endpoint, and returns the generated text.

```python PYTHON
for key,value in content_by_topic.items():
  value['ideas'] = generate_blog_ideas(value['keywords'])


for key,value in content_by_topic.items():
  print(f"Topic Name: {value['topic_name']}\n")
  print(f"Top Keywords: {value['keywords']}\n")
  print(f"Blog Post Ideas: {value['ideas']}\n")
  print("-"*50)
```

```
Topic Name: Remote Team Management

Top Keywords: managing remote teams, how to manage remote teams, leading remote teams, managing remote teams best practices, remote teams best practices, best practices for managing remote teams, manage remote teams, building culture in remote teams, culture building for remote teams, managing remote teams training

Blog Post Ideas: Here are three blog post ideas:

1. Blog title: "Leading Remote Teams: Strategies for Effective Management"
   Abstract: Effective management of remote teams is crucial for success, but it comes with unique challenges. This blog will explore practical strategies for leading dispersed employees, focusing on building a cohesive and productive virtual workforce. It will cover topics such as establishing clear communication protocols, fostering a collaborative environment, and the importance of trusting and empowering your remote employees for enhanced performance.

2. Blog title: "Remote Teams' Best Practices: Creating a Vibrant and Engaging Culture"
   Abstract: Building a rich culture in a remote team setting is essential for employee engagement and retention. The blog will delve into creative ways to foster a sense of community and connection among team members who may be scattered across the globe. It will offer practical tips on creating virtual rituals, fostering open communication, and harnessing the power of technology for cultural development, ensuring remote employees feel valued and engaged.

3. Blog title: "Managing Remote Teams: A Comprehensive Guide to Training and Development"
   Abstract: Training and developing remote teams present specific challenges and opportunities. This comprehensive guide will arm managers with techniques to enhance their remote team's skills and knowledge. It will explore the latest tools and methodologies for remote training, including virtual workshops, e-learning platforms, and performance coaching. Additionally, the blog will discuss the significance of ongoing development and how to create an environment that encourages self-improvement and learning.

Each of these topics explores a specific aspect of managing remote teams, providing valuable insights and practical guidance for leaders and managers in the evolving remote work landscape.

--------------------------------------------------
Topic Name: Remote Team Tools and Tips

Top Keywords: remote teams, collaboration tools for remote teams, team building for remote teams, scrum remote teams, tools for remote teams, zapier remote teams, working agreements for remote teams, working with remote teams, free collaboration tools for remote teams, free retrospective tools for remote teams

Blog Post Ideas: 1. Blog title: "The Ultimate Guide to Building Effective Remote Teams"
   Abstract: Building a cohesive and productive remote team can be challenging. This blog will serve as a comprehensive guide, offering practical tips and insights on how to create a united and successful virtual workforce. It will cover essential topics such as building a strong team culture, utilizing collaboration tools, and fostering effective communication strategies, ensuring remote teams can thrive and achieve their full potential.

2. Blog title: "The Best Collaboration Tools for Remote Teams: A Comprehensive Review"
   Abstract: With the rapid rise of remote work, collaboration tools have become essential for teams' productivity and efficiency. This blog aims to review and compare the most popular collaboration tools, providing an in-depth analysis of their features, ease of use, and benefits. It will offer insights into choosing the right tools for remote collaboration, helping teams streamline their workflows and enhance their overall performance.

3. Blog title: "Remote Retrospective: A Guide to Reflect and Grow as a Remote Team"
   Abstract: Conducting effective retrospectives is crucial for remote teams to reflect on their experiences, learn from the past, and chart a course for the future. This blog will focus on remote retrospectives, exploring different formats, techniques, and free tools that teams can use to foster continuous improvement. It will also provide tips on creating a safe and inclusive environment, encouraging honest feedback and productive discussions.

--------------------------------------------------
Topic Name: Remote Team Resources

Top Keywords: best collaboration tools for remote teams, slack best practices for remote teams, best communication tools for remote teams, best tools for remote teams, always on video for remote teams, best apps for remote teams, best free collaboration tools for remote teams, best games for remote teams, best gifts for remote teams, best ice breaker questions for remote teams

Blog Post Ideas: 1. Blog title: "The Ultimate Guide to Remote Team Collaboration Tools"
   Abstract: With the rise of remote work, choosing the right collaboration tools can be crucial to a team's success and productivity. This blog aims to be an comprehensive guide, outlining the various types of tools available, from communication platforms like Slack to project management software and online collaboration tools. It will offer best practices and guidelines for selecting and utilizing these tools, ensuring remote teams can work seamlessly together and maximize their output.

2. Blog title: "Remote Team Management: Tips for Leading a Successful Virtual Workforce"
   Abstract: Managing a remote team comes with its own set of challenges. This blog will provide an in-depth exploration of best practices for leading and motivating virtual teams. Covering topics such as effective communication strategies, performance evaluation, and maintaining a cohesive team culture, it will offer practical tips for managers and leaders to ensure their remote teams are engaged, productive, and well-managed.

3. Blog title: "The Fun Side of Remote Work: Games, Icebreakers, and Team Building Activities"
   Abstract: Remote work can be isolating, and this blog aims to provide some fun and creative solutions. It will offer a comprehensive guide to the best online games, icebreaker questions, and virtual team building activities that remote teams can use to connect and bond. From virtual escape rooms to interactive games and thought-provoking icebreakers, these ideas will help enhance team spirit, foster collaboration, and create a enjoyable remote work experience.

--------------------------------------------------
Topic Name: Remote Team Fun

Top Keywords: online games for remote teams, team building activities for remote teams, games for remote teams, retrospective ideas for remote teams, team building ideas for remote teams, fun retrospective ideas for remote teams, retro ideas for remote teams, team building exercises for remote teams, trust building exercises for remote teams, activities for remote teams

Blog Post Ideas: 1. Blog title: "The Great Remote Retro: Fun Games and Activities for Your Team"
   Abstract: Remote work can make team building challenging. This blog post will be a fun guide to hosting interactive retro games and activities that bring your remote team together. From online escape rooms to virtual scavenger hunts, we'll explore the best ways to engage and unite your team, fostering collaboration and camaraderie. Virtual icebreakers and retrospective ideas will also be included to make your remote meetings more interactive and enjoyable.

2. Blog title: "Trust Falls: Building Trust Among Remote Teams"
   Abstract: Trust is the foundation of every successful team, but how do you build it when everyone is scattered across different locations? This blog will focus on trust-building exercises and activities designed specifically for remote teams. From virtual trust falls to transparent communication practices, we'll discover innovative ways to strengthen team bonds and foster a culture of trust. You'll learn how to create an environment where your remote team can thrive and collaborate effectively.

3. Blog title: "Game Night for Remote Teams: A Guide to Online Games and Activities"
   Abstract: Miss the old office game nights? This blog will bring the fun back with a guide to hosting online game nights and activities that are perfect for remote teams. From trivia games to virtual board games and even remote-friendly outdoor adventures, we'll keep your team engaged and entertained. With tips on setting up online tournaments and ideas for encouraging participation, your virtual game nights will be the highlight of your team's week. Keep your remote team spirit high!

--------------------------------------------------
```


# Grounded Summarization Using Command R

> This page contains a basic tutorial on how to do grounded summarization with Cohere's models.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Grounded_summarisation_using_Command_R.ipynb" />

Note: we are in the process of updating the links in this notebook. If a link doesn't work, please open an issue and we'll rectify it ASAP. Thanks for your understanding!

Links to add:

* Cell 1: long-form, grounded summarisation blog post
* Section 4: to text-rank method (context filtering)

This notebook provides the code to produce the outputs described in [this blog post](https://docs.google.com/document/d/1Eeakpz_FZoeMzJnQieqQWCpPtQuNiTGW4fueU9J0QHA/edit).

## 1. Setup \[#setup]

```python PYTHON
%%capture

import cohere
import networkx as nx
import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize
import numpy as np
import spacy

from collections import deque
from getpass import getpass
import re
from typing import List, Tuple

co_api_key = getpass("Enter your Cohere API key: ")
co_model = "command-a-03-2025"
co = cohere.Client(co_api_key)

```

```python PYTHON

from google.colab import drive
drive.mount("/content/drive", force_remount=True)

fpath = "drive/Shareddrives/FDE/Cookbooks/Long-form summarisation/ai_and_future_of_work.txt"
with open(fpath, "r") as f:
  text = f.read()

num_tokens = co.tokenize(text).length
print(f"Loaded IMF report with {num_tokens} tokens")


```

### Aside: define utils

```python PYTHON

def split_text_into_sentences(text: str) -> List[str]:
    sentences =  sent_tokenize(text)
    return sentences

def group_sentences_into_passages(sentence_list: List[str], n_sentences_per_passage: int = 10):
    """
    Group sentences into passages of n_sentences sentences.
    """
    passages = []
    passage = ""
    for i, sentence in enumerate(sentence_list):
        passage += sentence + " "
        if (i + 1) % n_sentences_per_passage == 0:
            passages.append(passage)
            passage = ""
    return passages

def build_simple_chunks(text, n_sentences: int = 10):
    """
    Build chunks of text from the input text.
    """
    sentences = split_text_into_sentences(text)
    chunks = group_sentences_into_passages(sentences, n_sentences_per_passage=n_sentences)
    return chunks



def insert_citations(text: str, citations: List[dict]):
    """
    A helper function to pretty print citations.
    """
    offset = 0
    # Process citations in the order they were provided
    for citation in citations:
        # Adjust start/end with offset
        start, end = citation['start'] + offset, citation['end'] + offset
        placeholder = "[" + ", ".join(doc[4:] for doc in citation["document_ids"]) + "]"
        # ^ doc[4:] removes the 'doc_' prefix, and leaves the quoted document
        modification = f'{text[start:end]} {placeholder}'
        # Replace the cited text with its bolded version + placeholder
        text = text[:start] + modification + text[end:]
        # Update the offset for subsequent replacements
        offset += len(modification) - (end - start)

    return text



def textrank(text: str, co, max_tokens: int, n_sentences_per_passage: int) -> str:
    """
    Shortens `text` by extracting key units of text from `text` based on their centrality and concatenating them.
    The output is the concatenation of those key units, in their original order. Centrality is graph-theoretic
    measure of connectedness of a node; the more connected a node is to surrounding nodes (and the more sparsely
    those neighbours are connected), the higher centrality.

    Key passages are identified via clustering in a three-step process:
    1. Break up `long` into chunks (either sentences or passages, based on `unit`)
    2. Embed each chunk using Cohere's embedding model and construct a similarity matrix
    3. Compute the centrality of each chunk
    4. Keep the highest-centrality chunks until `max_tokens` is reached
    5. Put together shorterned text by reordering chunks in their original order

    This approach is based on summarise.long_doc_summarization.extraction::extract_single_doc with sorting by
    centrality. Adapted here because installing the `summarise` repo would have added a lot of unused functionalities
    and dependencies.
    """

    # 1. Chunk text into units
    chunks = build_simple_chunks(text, n_sentences_per_passage)

    # 2. Embed and construct similarity matrix
    embeddings = np.array(
        co.embed(
            texts=chunks,
            model="embed-v4.0",
            input_type="clustering",
        ).embeddings
    )
    similarities = np.dot(embeddings, embeddings.T)

    # 3. Compute centrality and sort sentences by centrality
    # Easiest to use networkx's `degree` function with similarity as weight
    g = nx.from_numpy_array(similarities, edge_attr="weight")
    centralities = g.degree(weight="weight")
    idcs_sorted_by_centrality = [node for node, degree in sorted(centralities, key=lambda item: item[1], reverse=True)]

    # 4. Add chunks back in order of centrality
    selected = _add_chunks_by_priority(co, chunks, idcs_sorted_by_centrality, max_tokens)

    # 5. Put condensed text back in original order
    separator = "\n"
    short = separator.join([chunk for index, chunk in sorted(selected, key=lambda item: item[0], reverse=False)])

    return short


def _add_chunks_by_priority(
    co, chunks: List[str], idcs_sorted_by_priority: List[int], max_tokens: int
) -> List[Tuple[int, str]]:
    """
    Given chunks of text and their indices sorted by priority (highest priority first), this function
    fills the model context window with as many highest-priority chunks as possible.

    The output is a list of (index, chunk) pairs, ordered by priority. To stitch back the chunks into
    a cohesive text that preserves chronological order, sort the output on its index.
    """

    selected = []
    num_tokens = 0
    idcs_queue = deque(idcs_sorted_by_priority)

    while num_tokens < max_tokens and len(idcs_queue) > 0:
        next_idx = idcs_queue.popleft()
        num_tokens += co.tokenize(chunks[next_idx]).length - 2
        # num_tokens += len(tokenizer.encode(chunks[next_idx]).ids) - 2
        # ^ removing BOS and EOS tokens from count
        selected.append((next_idx, chunks[next_idx]))
        # ^ keep index and chunk, to reorder chronologically
    if num_tokens > max_tokens:
        selected.pop()

    return selected

```

## 2. Out-of-the-box summarization with Command-R \[#out-of-the-box-summarization-with-command-r]

First, let's see Command-R's out-of-the-box performance. It's a 128k-context model, so we can pass the full IMF report in a single call. We replicate the exact instructions from the original tweet (correcting for a minor typo) for enabling fair comparisons.

```python PYTHON
prompt_template = """\
## text
{text}

## instructions
Step 1. Read the entire text from the first to the last page.
Step 2. Create a summary of every chapter from the first to the last page.

## summary
"""

prompt = prompt_template.format(text=text)
resp = co.chat(
  message=prompt,
  model=co_model,
  temperature=0.3,
  return_prompt=True
)

num_tokens_in = co.tokenize(resp.prompt).length
num_tokens_out = resp.meta["billed_units"]["output_tokens"]
print(f"Generated summary with {num_tokens_in} tokens in, {num_tokens_out} tokens out")
print()
print("--- Out-of-the-box summary with Command-R ---")
print()
print(resp.text)

```

# 3. Introduce citations to the summary for grounding \[#introduce-citations-to-the-summary-for-grounding]

When summarizing long documents, introducing citations is one simple method for checking the factuality of the summary without needing to read the full document.

We've trained Command-R to introduce citations whenever prompted by our grounded generations instructions. Triggering this grounded mode is straightforward. Starting from the previous snippet, we only need to make two changes:

1. Pass our text to the `documents` argument
2. Pass our instructions to the `message` argument

For more information on how to enable grounded generation via our `co.chat` API, please refer to our [documentation](https://docs.cohere.com/reference/chat).

Finally, note that we chunk the IMF report into multiple documents before passing them to `co.chat`. This isn't necessary (`co.chat` annotates citations at the character level), but allows for more human-readable citations.

```python PYTHON
summarize_preamble = """\
You will receive a series of text fragments from an article that are presented in chronological order. \
As the assistant, you must generate responses to user's requests based on the information given in the fragments. \
Ensure that your responses are accurate and truthful, and that you reference your sources where appropriate to answer \
the queries, regardless of their complexity.\
"""

instructions = """\
## instructions
Step 1. Read the entire text from the first to the last page.
Step 2. Create a summary of every chapter from the first to the last page.
"""

chunked = build_simple_chunks(text, n_sentences=30)
resp = co.chat(
  preamble=summarize_preamble,
  message=instructions,
  documents=[{"text": chunk} for chunk in chunked],
  model=co_model,
  temperature=0.3,
  return_prompt=True
)

num_tokens_in = co.tokenize(resp.prompt).length
num_tokens_out = resp.meta["billed_units"]["output_tokens"]
print(f"Generated summary with {num_tokens_in} tokens in, {num_tokens_out} tokens out")
print()
print("--- Summary with citations using grounded generation in Command-R ---")
print()
print(resp.text)

```

Let's display the citations inside our answer:

```python PYTHON
print(insert_citations(resp.text, resp.citations))
```

We can now visualise which section of the answer is based on which passage in the main text. Verifying factuality is straightforward: pick a section and verify that the relevant information is contained in the cited chunk.

For instance, let's verify the statement

```
Around 40% of employment worldwide is exposed to AI [1, 6]
```

by checking its chunk:

```python PYTHON
print(chunked[6])
```

Seems convincing!
By repeating such checks, it's straightforward to build trust in your summaries.

# 4. Reduce the cost of summarization calls \[#reduce-the-cost-of-summarization-calls]

Even though Command-R is an efficient, light-weight model, for some applications we may accept trading off some summarization quality for lower costs. To do this, we must reduce the amount of tokens sent to the model -- but how do we select the most relevant bits?

We have a whole notebook dedicated to methods for reducing context length. Here, we call our 'text-rank' method to select maximally central chunks in a graph based on the chunk-to-chunk similarties. For more detail, please refer [to this cookbook](https://colab.research.google.com/drive/1zxSAbruOWwWJHNsj3N56uxZtUeiS7Evd).

```python PYTHON
num_tokens = 8192
shortened = textrank(text, co, num_tokens, n_sentences_per_passage=30)

chunked = build_simple_chunks(shortened)
resp = co.chat(
  message=instructions,
  documents=[{"text": chunk} for chunk in chunked],
  model=co_model,
  temperature=0.3,
  return_prompt=True
)

num_tokens_in = co.tokenize(resp.prompt).length
num_tokens_out = resp.meta["billed_units"]["output_tokens"]
print(f"Generated summary with {num_tokens_in} tokens in, {num_tokens_out} tokens out")
print()
print("--- Summary with citations using text-rank + grounding in Command-R ---")
print()
print(resp.text)

```

The summary is looking convincing! In practice, the trade-off between cost-efficiency and performance should be considered carefully.


# Hello World! Explore Language AI with Cohere

> This page contains a breakdown of some of what can be achieved with Cohere's LLM platform.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Hello_World_Meet_Language_AI.ipynb" />

Here we take a quick tour of what’s possible with language AI via Cohere’s Large Language Model (LLM) API. This is the Hello, World! of language AI, written for developers with little or no background in AI. In fact, we’ll do that by exploring the Hello, World! phrase itself.

Read the accompanying [blog post here](https://cohere.com/blog/hello-world-p1/).

<img alt="Hello World! Meet Language AI" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/hello-world/hello-world-feat.png" />

We’ll cover three groups of tasks that you will typically work on when dealing with language data, including:

* Generating text
* Classifying text
* Analyzing text

The first step is to install the Cohere Python SDK. Next, create an API key, which you can generate from the Cohere [dashboard](https://dashboard.cohere.com/register).

```python PYTHON
! pip install cohere altair umap-learn -q
```

```python PYTHON
import cohere
import pandas as pd
import numpy as np
import altair as alt

co = cohere.Client("COHERE_API_KEY") # Get your API key: https://dashboard.cohere.com/api-keys
```

The Cohere Generate endpoint generates text given an input, called “prompt”. The prompt provides a context of what we want the model to generate text. To illustrate this, let’s start with a simple prompt as the input.

### Try a Simple Prompt

```python PYTHON
prompt = "What is a Hello World program."

response = co.chat(
  message=prompt,
  model='command-r')

print(response.text)
```

````
A "Hello World" program is a traditional and simple program that is often used as an introduction to a new programming language. The program typically displays the message "Hello World" as its output. The concept of a "Hello World" program originated from the book *The C Programming Language* written by Kernighan and Ritchie, where the example program in the book displayed the message using the C programming language.

The "Hello World" program serves as a basic and straightforward way to verify that your development environment is set up correctly and to familiarize yourself with the syntax and fundamentals of the programming language. It's a starting point for learning how to write and run programs in a new language.

The program's simplicity makes it accessible to programmers of all skill levels, and it's often one of the first programs beginners write when learning to code. The exact implementation of a "Hello World" program varies depending on the programming language being used, but the core idea remains the same—to display the "Hello World" message.

Here's how a "Hello World" program can be written in a few select languages:
1. **C**:
```c
#include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
```
2. **Python**:
```python PYTHON
print("Hello World")
```
3. **Java**:
```java JAVA
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
4. **JavaScript**:
```javascript
console.log("Hello World");
```
5. **C#**:
```csharp
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello World");
    }
}
```
The "Hello World" program is a testament to the power of programming, as a simple and concise message can be displayed in numerous languages with just a few lines of code. It's an exciting first step into the world of software development!
````

### Create a Better Prompt

The output is not bad, but it can be better. We need to find a way to make the output tighter to how we want it to be, which is where we leverage *prompt engineering*.

```python PYTHON
prompt = """
Write the first paragraph of a blog post given a blog title.
--
Blog Title: Best Activities in Toronto
First Paragraph: Looking for fun things to do in Toronto? When it comes to exploring Canada's
largest city, there's an ever-evolving set of activities to choose from. Whether you're looking to
visit a local museum or sample the city's varied cuisine, there is plenty to fill any itinerary. In
this blog post, I'll share some of my favorite recommendations
--
Blog Title: Mastering Dynamic Programming
First Paragraph: In this piece, we'll help you understand the fundamentals of dynamic programming,
and when to apply this optimization technique. We'll break down bottom-up and top-down approaches to
solve dynamic programming problems.
--
Blog Title: Learning to Code with Hello, World!
First Paragraph:"""

response = co.chat(
  message=prompt,
  model='command-r')

print(response.text)
```

```
Starting to code can be daunting, but it's actually simpler than you think! The famous first program, "Hello, World!" is a rite of passage for all coders, and an excellent starting point to begin your coding journey. This blog will guide you through the process of writing your very first line of code, and help you understand why learning to code is an exciting and valuable skill to have, covering the fundamentals and the broader implications of this seemingly simple phrase.
```

### Automating the Process

In real applications, you will likely need to produce these text generations on an ongoing basis, given different inputs. Let’s simulate that with our example.

```python PYTHON
def generate_text(topic):
  prompt = f"""
Write the first paragraph of a blog post given a blog title.
--
Blog Title: Best Activities in Toronto
First Paragraph: Looking for fun things to do in Toronto? When it comes to exploring Canada's
largest city, there's an ever-evolving set of activities to choose from. Whether you're looking to
visit a local museum or sample the city's varied cuisine, there is plenty to fill any itinerary. In
this blog post, I'll share some of my favorite recommendations
--
Blog Title: Mastering Dynamic Programming
First Paragraph: In this piece, we'll help you understand the fundamentals of dynamic programming,
and when to apply this optimization technique. We'll break down bottom-up and top-down approaches to
solve dynamic programming problems.
--
Blog Title: {topic}
First Paragraph:"""
  # Generate text by calling the Chat endpoint
  response = co.chat(
    message=prompt,
    model='command-r')

  return response.text
```

```python PYTHON
topics = ["How to Grow in Your Career",
          "The Habits of Great Software Developers",
          "Ideas for a Relaxing Weekend"]
```

```python PYTHON
paragraphs = []

for topic in topics:
  paragraphs.append(generate_text(topic))

for topic,para in zip(topics,paragraphs):
  print(f"Topic: {topic}")
  print(f"First Paragraph: {para}")
  print("-"*10)
```

```
Topic: How to Grow in Your Career
First Paragraph: Advancing in your career can seem like a daunting task, especially if you're unsure of the path ahead. In this ever-changing professional landscape, there are numerous factors to consider. This blog aims to shed light on the strategies and skills that can help you navigate the complexities of career progression and unlock your full potential. Whether you're looking to secure a promotion or explore new opportunities, these insights will help you chart a course for your future. Let's embark on this journey of self-improvement and professional growth, equipping you with the tools to succeed in your career aspirations.
----------
Topic: The Habits of Great Software Developers
First Paragraph: Great software developers are renowned for their ability to write robust code and create innovative applications, but what sets them apart from their peers? In this blog, we'll delve into the daily habits that contribute to their success. From their approach to coding challenges to the ways they stay organized, we'll explore the routines and practices that help them excel in the fast-paced world of software development. Understanding these habits can help you elevate your own skills and join the ranks of these industry leaders.
----------
Topic: Ideas for a Relaxing Weekend
First Paragraph: Life can be stressful, and sometimes we just need a relaxing weekend to unwind and recharge. In this fast-paced world, taking some time to slow down and rejuvenate is essential. This blog post is here to help you plan the perfect low-key weekend with some easy and accessible ideas. From cozy indoor activities to peaceful outdoor adventures, I'll share some ideas to help you renew your mind, body, and spirit. Whether you're a homebody or an adventure seeker, there's something special for everyone. So, grab a cup of tea, sit back, and get ready to dive into a calming weekend of self-care and relaxation!
----------
```

Cohere’s Classify endpoint makes it easy to take a list of texts and predict their categories, or classes. A typical machine learning model requires many training examples to perform text classification, but with the Classify endpoint, you can get started with as few as 5 examples per class.

### Sentiment Analysis

```python PYTHON
from cohere import ClassifyExample

examples = [
    ClassifyExample(text="I’m so proud of you", label="positive"),
    ClassifyExample(text="What a great time to be alive", label="positive"),
    ClassifyExample(text="That’s awesome work", label="positive"),
    ClassifyExample(text="The service was amazing", label="positive"),
    ClassifyExample(text="I love my family", label="positive"),
    ClassifyExample(text="They don't care about me", label="negative"),
    ClassifyExample(text="I hate this place", label="negative"),
    ClassifyExample(text="The most ridiculous thing I've ever heard", label="negative"),
    ClassifyExample(text="I am really frustrated", label="negative"),
    ClassifyExample(text="This is so unfair", label="negative"),
    ClassifyExample(text="This made me think", label="neutral"),
    ClassifyExample(text="The good old days", label="neutral"),
    ClassifyExample(text="What's the difference", label="neutral"),
    ClassifyExample(text="You can't ignore this", label="neutral"),
    ClassifyExample(text="That's how I see it", label="neutral")
]
```

```python PYTHON
inputs=["Hello, world! What a beautiful day",
        "It was a great time with great people",
        "Great place to work",
        "That was a wonderful evening",
        "Maybe this is why",
        "Let's start again",
        "That's how I see it",
        "These are all facts",
        "This is the worst thing",
        "I cannot stand this any longer",
        "This is really annoying",
        "I am just plain fed up"
        ]
```

```python PYTHON
def classify_text(inputs, examples):
  """
  Classify a list of input texts
  Arguments:
    inputs(list[str]): a list of input texts to be classified
    examples(list[Example]): a list of example texts and class labels
  Returns:
    classifications(list): each result contains the text, labels, and conf values
  """
  # Classify text by calling the Classify endpoint
  response = co.classify(
    model='embed-v4.0',
    inputs=inputs,
    examples=examples)

  classifications = response.classifications

  return classifications
```

```python PYTHON
predictions = classify_text(inputs,examples)

classes = ["positive","negative","neutral"]
for inp,pred in zip(inputs,predictions):
  class_pred = pred.predictions[0]
  class_idx = classes.index(class_pred)
  class_conf = pred.confidences[0]

  print(f"Input: {inp}")
  print(f"Prediction: {class_pred}")
  print(f"Confidence: {class_conf:.2f}")
  print("-"*10)
```

```
Input: Hello, world! What a beautiful day
Prediction: positive
Confidence: 0.84
----------
Input: It was a great time with great people
Prediction: positive
Confidence: 0.99
----------
Input: Great place to work
Prediction: positive
Confidence: 0.91
----------
Input: That was a wonderful evening
Prediction: positive
Confidence: 0.96
----------
Input: Maybe this is why
Prediction: neutral
Confidence: 0.70
----------
Input: Let's start again
Prediction: neutral
Confidence: 0.83
----------
Input: That's how I see it
Prediction: neutral
Confidence: 1.00
----------
Input: These are all facts
Prediction: neutral
Confidence: 0.78
----------
Input: This is the worst thing
Prediction: negative
Confidence: 0.93
----------
Input: I cannot stand this any longer
Prediction: negative
Confidence: 0.93
----------
Input: This is really annoying
Prediction: negative
Confidence: 0.99
----------
Input: I am just plain fed up
Prediction: negative
Confidence: 1.00
----------
```

Cohere’s Embed endpoint takes a piece of text and turns it into a vector embedding. Embeddings represent text in the form of numbers that capture its meaning and context. What it means is that it gives you the ability to turn unstructured text data into a structured form. It opens up ways to analyze and extract insights from them.

## Get embeddings

Here we have a list of 50 top web search keywords about Hello, World! taken from a keyword tool. Let’s look at a few examples:

```python PYTHON
df = pd.read_csv("https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/data/hello-world-kw.csv", names=["search_term"])
df.head()
```

<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          search_term
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          how to print hello world in python
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          what is hello world
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          how do you write hello world in an alert box
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          how to print hello world in java
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          how to write hello world in eclipse
        </td>
      </tr>
    </tbody>
  </table>
</div>

We use the Embed endpoint to get the embeddings for each of these keywords.

```python PYTHON
def embed_text(texts, input_type):
  """
  Turns a piece of text into embeddings
  Arguments:
    text(str): the text to be turned into embeddings
  Returns:
    embedding(list): the embeddings
  """
  # Embed text by calling the Embed endpoint
  response = co.embed(
                model="embed-v4.0",
                input_type=input_type,
                texts=texts)

  return response.embeddings
```

```python PYTHON
df["search_term_embeds"] = embed_text(texts=df["search_term"].tolist(),
                                      input_type="search_document")
doc_embeds = np.array(df["search_term_embeds"].tolist())
```

### Semantic Search

We’ll look at a couple of example applications. The first example is semantic search. Given a new query, our "search engine" must return the most similar FAQs, where the FAQs are the 50 search terms we uploaded earlier.

```python PYTHON
query = "what is the history of hello world"

query_embeds = embed_text(texts=[query],
                          input_type="search_query")[0]
```

We use cosine similarity to compare the similarity of the new query with each of the FAQs

```python PYTHON

from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(target, candidates):
  """
  Computes the similarity between a target text and a list of other texts
  Arguments:
    target(list[float]): the target text
    candidates(list[list[float]]): a list of other texts, or candidates
  Returns:
    sim(list[tuple]): candidate IDs and the similarity scores
  """
  # Turn list into array
  candidates = np.array(candidates)
  target = np.expand_dims(np.array(target),axis=0)

  # Calculate cosine similarity
  sim = cosine_similarity(target,candidates)
  sim = np.squeeze(sim).tolist()

  # Sort by descending order in similarity
  sim = list(enumerate(sim))
  sim = sorted(sim, key=lambda x:x[1], reverse=True)

  # Return similarity scores
  return sim
```

Finally, we display the top 5 FAQs that match the new query

```python PYTHON
similarity = get_similarity(query_embeds,doc_embeds)

print("New query:")
print(new_query,'\n')

print("Similar queries:")
for idx,score in similarity[:5]:
  print(f"Similarity: {score:.2f};", df.iloc[idx]["search_term"])
```

```
New query:
what is the history of hello world

Similar queries:
Similarity: 0.58; how did hello world originate
Similarity: 0.56; where did hello world come from
Similarity: 0.54; why hello world
Similarity: 0.53; why is hello world so famous
Similarity: 0.53; what is hello world
```

### Semantic Exploration

In the second example, we take the same idea as semantic search and take a broader look, which is exploring huge volumes of text and analyzing their semantic relationships.

We'll use the same 50 top web search terms about Hello, World! There are different techniques we can use to compress the embeddings down to just 2 dimensions while retaining as much information as possible. We'll use a technique called UMAP. And once we can get it down to 2 dimensions, we can plot these embeddings on a 2D chart.

```python PYTHON
import umap
reducer = umap.UMAP(n_neighbors=49)
umap_embeds = reducer.fit_transform(doc_embeds)

df['x'] = umap_embeds[:,0]
df['y'] = umap_embeds[:,1]
```

```python PYTHON
chart = alt.Chart(df).mark_circle(size=500).encode(
  x=
  alt.X('x',
      scale=alt.Scale(zero=False),
      axis=alt.Axis(labels=False, ticks=False, domain=False)
  ),

  y=
  alt.Y('y',
      scale=alt.Scale(zero=False),
      axis=alt.Axis(labels=False, ticks=False, domain=False)
  ),

  tooltip=['search_term']
  )

text = chart.mark_text(align='left', dx=15, size=12, color='black'
          ).encode(text='search_term', color= alt.value('black'))

result = (chart + text).configure(background="#FDF7F0"
      ).properties(
      width=1000,
      height=700,
      title="2D Embeddings"
      )

result
```


# Long-Form Text Strategies with Cohere

> This discusses ways of getting Cohere's LLM platform to perform well in generating long-form text.

<AuthorsContainer
  authors={[
    {
      name: "Ania Bialas",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/c5dc5a3-Ania.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Long_form_General_Strategies.ipynb" />

Large Language Models (LLMs) are becoming increasingly capable of comprehending text, among others excelling in document analysis. The new Cohere model, [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-v01), boasts a context length of 128k, which makes it particularly effective for such tasks. Nevertheless, even with the extended context window, some documents might be too lengthy to accommodate in full.

In this cookbook, we'll explore techniques to address cases when relevant information doesn't fit in the model context window.

We'll show you three potential mitigation strategies: truncating the document, query-based retrieval, and a "text rank" approach we use internally at Cohere.

## Summary

| Approach              | Description                                                                                            | Pros                                                                           | Cons                                                                           | When to use?                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Truncation            | Truncate the document to fit the context window.                                                       | - Simplicity of implementation<br />(does not rely on extrenal infrastructure) | - Loses information at the end of the document                                 | Utilize when all relevant information is contained<br /> at the beginning of the document. |
| Query Based Retrieval | Utilize semantic similarity to retrieve text chunks<br /> that are most relevant to the query.         | - Focuses on sections directly relevant to<br /> the query                     | - Relies on a semantic similarity algorithm.<br />- Might lose broader context | Employ when seeking specific<br /> information within the text.                            |
| Text Rank             | Apply graph theory to generate a cohesive set<br /> of chunks that effectively represent the document. | - Preserves the broader picture.                                               | - Might lose detailed information.                                             | Utilize in summaries and when the question<br /> requires broader context.                 |

## Getting Started \[#getting-started]

```python PYTHON
%%capture
!pip install cohere
!pip install python-dotenv
!pip install tokenizers
!pip install langchain
!pip install nltk
!pip install networkx
!pip install pypdf2
```

```python PYTHON
import os
import requests
from collections import deque
from typing import List, Tuple

import cohere

import numpy as np

import PyPDF2
from dotenv import load_dotenv

from tokenizers import Tokenizer

import nltk
nltk.download('punkt')  # Download the necessary data for sentence tokenization
from nltk.tokenize import sent_tokenize

import networkx as nx
from getpass import getpass
from IPython.display import HTML, display
```

```txt title="Output"
[nltk_data] Downloading package punkt to
[nltk_data]     /home/anna_cohere_com/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
```

```python PYTHON
# Set up Cohere client
co_model = 'command-r'
co_api_key = getpass("Enter your Cohere API key: ")
co = cohere.Client(api_key=co_api_key)
```

```python PYTHON
def load_long_pdf(file_path):
    """
    Load a long PDF file and extract its text content.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content of the PDF file.
    """
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        full_text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            full_text += page.extract_text()
    return full_text

def save_pdf_from_url(pdf_url, save_path):
    try:
        # Send a GET request to the PDF URL
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Open the local file for writing in binary mode
        with open(save_path, 'wb') as file:
            # Write the content of the response to the local file
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"PDF saved successfully to '{save_path}'")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
```

In this example we use the Proposal for a Regulation of the European Parliament and of the Council defining rules on Artificial Intelligence from 26 January 2024, [link](https://data.consilium.europa.eu/doc/document/ST-5662-2024-INIT/en/pdf).

```python PYTHON
# Download the PDF file from the URL
pdf_url = 'https://data.consilium.europa.eu/doc/document/ST-5662-2024-INIT/en/pdf'
save_path = 'example.pdf'
save_pdf_from_url(pdf_url, save_path)

# Load the PDF file and extract its text content
long_text = load_long_pdf(save_path)
long_text = long_text.replace('\n', ' ')

# Print the length of the document
print("Document length - #tokens:", len(co.tokenize(text=long_text, model=co_model).tokens))
```

```txt title="Output"
PDF saved successfully to 'example.pdf'
Document length - #tokens: 134184
```

## Summarizing the text

```python PYTHON
def generate_response(message, max_tokens=300, temperature=0.2, k=0):
  """
  A wrapper around the Cohere API to generate a response based on a given prompt.

  Args:
    messsage (str): The input message for generating the response.
    max_tokens (int, optional): The maximum number of tokens in the generated response. Defaults to 300.
    temperature (float, optional): Controls the randomness of the generated response. Higher values (e.g., 1.0) make the output more random, while lower values (e.g., 0.2) make it more deterministic. Defaults to 0.2.
    k (int, optional): Controls the diversity of the generated response. Higher values (e.g., 5) make the output more diverse, while lower values (e.g., 0) make it more focused. Defaults to 0.

  Returns:
    str: The generated response.

  """
  response = co.chat(
    model = co_model,
    message=message,
    max_tokens=max_tokens,
    temperature=temperature,
    return_prompt=True
    )
  return response.text
```

```python PYTHON
# Example summary prompt.
prompt_template = """
## Instruction
Summarize the following Document in 3-5 sentences. Only answer based on the information provided in the document.

## Document
{document}

## Summary
""".strip()
```

If you run the cell below, an error will occur. Therefore, in the following sections, we will explore some techniques to address this limitation.

Error: :`CohereAPIError: too many tokens:`

```python PYTHON
prompt = prompt_template.format(document=long_text)
# print(generate_response(message=prompt))
```

Therefore, in the following sections, we will explore some techniques to address this limitation.

## Approach 1 - Truncate \[#approach-1]

First we try to truncate the document so that it meets the length constraints. This approach is simple to implement and understand. However, it drops potentially important information contained towards the end of the document.

```python PYTHON
# The new Cohere model has a context limit of 128k tokens. However, for the purpose of this exercise, we will assume a smaller context window.

---

**Navigation:** [← Previous](./16-creating-a-qa-bot-from-technical-documentation.md) | [Index](./index.md) | [Next →](./18-employing-a-smaller-context-window-also-has-the-ad.md)
