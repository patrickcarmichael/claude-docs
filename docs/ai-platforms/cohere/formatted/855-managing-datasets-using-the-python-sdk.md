---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Managing Datasets using the Python SDK

### Getting Set up

First, let's install the SDK
```bash
pip install cohere
```
Import dependencies and set up the Cohere client.
```python PYTHON
import cohere

co = cohere.Client(api_key="Your API key")
```
(All the rest of the examples on this page will be in Python, but you can find more detailed instructions for getting set up by checking out the Github repositories for [Python](https://github.com/cohere-ai/cohere-python), [Typescript](https://github.com/cohere-ai/cohere-typescript), and [Go](https://github.com/cohere-ai/cohere-go).)

### Dataset Creation

Datasets are created by uploading files, specifying both a `name` for the dataset and the dataset `type`.

The file extension and file contents have to match the requirements for the selected dataset `type`. See the [table below](#supported-dataset-types) to learn more about the supported dataset types.

The dataset `name` is useful when browsing the datasets you've uploaded. In addition to its name, each dataset will also be assigned a unique `id` when it's created.

Here is an example code snippet illustrating the process of creating a dataset, with both the `name` and the dataset `type` specified.
```python PYTHON
my_dataset = co.datasets.create(
    name="shakespeare",
    data=open("./shakespeare.jsonl", "rb"),
    type="embed-input",
)

print(my_dataset.id)
```

### Dataset Validation

Whenever a dataset is created, the data is validated asynchronously against the rules for the specified dataset `type` . This validation is kicked off automatically on the backend, and must be completed before a dataset can be used with other endpoints.

Here's a code snippet showing how to check the validation status of a dataset you've created.
```python PYTHON
ds = co.wait(my_dataset)
print(ds.dataset.validation_status)
```
To help you interpret the results, here's a table specifying all the possible API error messages and what they mean:

| Error Code | Endpoint   | Error Explanation                                                          | Actions Required                                                                   |
| :--------- | :--------- | :------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| 400        | Create     | The name parameter must be set.                                            | Set a name parameter.                                                              |
| 400        | Create     | The type parameter must be set.                                            | Set a type parameter.                                                              |
| 400        | Create     | The dataset type is invalid.                                               | Set the type parameter to a supported type.                                        |
| 400        | Create     | You have exceeded capacity.                                                | Delete unused datasets to free up space.                                           |
| 400        | Create     | You have used an invalid csv delimiter.                                    | The csv delimiter must be one character long.                                      |
| 400        | Create     | The name must be less than 50 characters long.                             | Shorten your dataset name.                                                         |
| 400        | Create     | You used an invalid parameter for part: %v use file or an evaluation file. | The file parameters must be a named file or an evaluation file.                    |
| 499        | Create     | The upload connection was closed.                                          | Don't cancel the upload request.                                                   |
|            | Validation | The required field {} was not fund in the dataset (line: {})               | You are missing a required field, which must be supplied.                          |
|            | Validation | Custom validation rules per type                                           | There should be enough context in the validation error message to fix the dataset. |
|            | Validation | csv files must have a header with the required fields: \[{}, {}, ...].     | Fix your csv file to have a 'headers' row with the required field names.           |
| 404        | Get        | The dataset with id '{}' was not found.                                    | Make sure you're passing in the right id.                                          |

### Dataset Metadata Preservation

The Dataset API will preserve metadata if specified at time of upload. During the `create dataset` step, you can specify either `keep_fields` or `optional_fields` which are a list of strings which correspond to the field of the metadata you’d like to preserve. `keep_fields` is more restrictive, where if the field is missing from an entry, the dataset will fail validation whereas `optional_fields` will skip empty fields and validation will still pass.

#### Sample Dataset Input Format

```text JSONL
{"wiki_id": 69407798, "url": "https://en.wikipedia.org/wiki?curid=69407798", "views": 5674.4492597435465, "langs": 38, "title": "Deaths in 2022", "text": "The following notable deaths occurred in 2022. Names are reported under the date of death, in alphabetical order. A typical entry reports information in the following sequence:", "paragraph_id": 0, "id": 0}
{"wiki_id": 3524766, "url": "https://en.wikipedia.org/wiki?curid=3524766", "views": 5409.5609619796405, "title": "YouTube", "text": "YouTube is a global online video sharing and social media platform headquartered in San Bruno, California. It was launched on February 14, 2005, by Steve Chen, Chad Hurley, and Jawed Karim. It is owned by Google, and is the second most visited website, after Google Search. YouTube has more than 2.5 billion monthly users who collectively watch more than one billion hours of videos each day. , videos were being uploaded at a rate of more than 500 hours of content per minute.", "paragraph_id": 0, "id": 1}
```
As seen in the above example, the following would be a valid `create_dataset` call since `langs` is in the first entry but not in the second entry. The fields `wiki_id`, `url`, `views` and `title` are present in both JSONs.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
