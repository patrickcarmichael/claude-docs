---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## kick off a text detection job. This returns a job ID.

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
