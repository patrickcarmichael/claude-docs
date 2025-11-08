---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 400 - Bad Request

400 responses are sent when the body of the request is not valid. This can happen when required fields are missing, or when the values provided are not valid.

To resolve this error, consult [the API spec](https://docs.cohere.com/reference/about) to ensure that you are providing the correct fields and values.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                                                                                                                                                                                                                             |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | invalid request: list of documents must not be empty                                                                                                                                                                                                                |
  | invalid request: prompt must be at least 1 token long.                                                                                                                                                                                                              |
  | too many tokens: total number of tokens in the prompt cannot exceed 4081 - received 4292. Try using a shorter prompt, or enabling prompt truncating. See [https://docs.cohere.com/reference/generate](https://docs.cohere.com/reference/generate) for more details. |
  | invalid request: valid input\_type must be provided with the provided model                                                                                                                                                                                         |
  | system turn must be the first in the list                                                                                                                                                                                                                           |
  | invalid request: all elements in history must have a message.                                                                                                                                                                                                       |
  | invalid request: message must be at least 1 token long or tool results must be specified.                                                                                                                                                                           |
  | invalid request: query must not be empty or be only whitespace                                                                                                                                                                                                      |
  | invalid request: model 'command-r' is not supported by the generate API                                                                                                                                                                                             |
  | invalid request: cannot specify both frequency\_penalty and presence\_penalty.                                                                                                                                                                                      |
  | invalid request: only one of 'presence\_penalty' and 'frequency\_penalty' can be specified for this model.                                                                                                                                                          |
  | message must not be empty in a turn                                                                                                                                                                                                                                 |
  | too many tokens: max tokens must be less than or equal to 4096, the maximum output for this model - received 8192.                                                                                                                                                  |
  | invalid request: response\_format is not supported with RAG.                                                                                                                                                                                                        |
  | too many tokens: size limit exceeded by 11326 tokens. Try using shorter or fewer inputs, or setting prompt\_truncation='AUTO'.                                                                                                                                      |
  | invalid request: number of total max chunks (number of documents \* max chunks per doc) must be less than 10000                                                                                                                                                     |
  | invalid request: min classes for classify request is 2 - received 0                                                                                                                                                                                                 |
  | invalid request: Invalid role in chat\_history at index 2. Role must be one of the following: User, Chatbot, System, Tool                                                                                                                                           |
  | invalid request: total number of texts must be at most 96 - received 104                                                                                                                                                                                            |
  | invalid request: temperature must be between 0 and 1.0 inclusive.                                                                                                                                                                                                   |
  | invalid request: presence\_penalty must be between 0 and 1 inclusive.                                                                                                                                                                                               |
  | invalid request: text must be longer than 250 characters                                                                                                                                                                                                            |
  | invalid request: inputs contains an element that is the empty string at index 0                                                                                                                                                                                     |
  | multi step limit reached - set a higher limit                                                                                                                                                                                                                       |
  | invalid request: return\_top\_n is invalid, value must be between 1 and 4                                                                                                                                                                                           |
  | invalid request: document at index 0 cannot be empty                                                                                                                                                                                                                |
  | embedding\_types parameter is required                                                                                                                                                                                                                              |
  | finetuneID is not a valid UUID: ''                                                                                                                                                                                                                                  |
  | invalid request: tool names can only contain certain characters (A-Za-z0-9\_) and can't begin with a digit (provided name: 'xyz').                                                                                                                                  |
  | invalid json syntax: invalid character '\a' in string literal                                                                                                                                                                                                       |
  | invalid request: RAG is not supported for this model.                                                                                                                                                                                                               |
  | tool call id not found in previous tool calls                                                                                                                                                                                                                       |
  | invalid request: each unique label must have at least 2 examples. Not enough examples for: awr\_report, create\_user, tablespace\_usage                                                                                                                             |
  | invalid request: multi step is not supported by the provided model: command.                                                                                                                                                                                        |
  | invalid request: invalid API version was passed in, for more information please refer to [https://docs.cohere.com/versioning-reference](https://docs.cohere.com/versioning-reference)                                                                               |
  | document does not have a 'snippet' or a 'text' field that can be used for chunking and reranking                                                                                                                                                                    |
  | finetuned model with name xyz is not ready for serving                                                                                                                                                                                                              |
  | invalid request: required 'text' param is missing or empty.                                                                                                                                                                                                         |
  | invalid request: rank\_fields cannot be empty, it must either contain at least one field or be omitted                                                                                                                                                              |
  | schema must be an object                                                                                                                                                                                                                                            |
  | a model parameter is required for this endpoint.                                                                                                                                                                                                                    |
  | cannot have duplicate tool ids                                                                                                                                                                                                                                      |
  | too many tokens: multi-hop prompt is too long even after truncation                                                                                                                                                                                                 |
  | connectors failed with continue on failure disabled: connector xyz failed with message 'failed to get auth token: user is not authenticated for connector xyz'                                                                                                      |
  | invalid request: the 'tool\_1' tool must have at least a description, input, or output.                                                                                                                                                                             |
  | tool call id must be provided with tool message                                                                                                                                                                                                                     |
  | invalid request: images must be used with input\_type=image                                                                                                                                                                                                         |
  | invalid request: format must be one of 'paragraph', or 'bullets'.                                                                                                                                                                                                   |
  | invalid request: finetuned model is not compatible with RAG functionality                                                                                                                                                                                           |
  | required field name not found in properties                                                                                                                                                                                                                         |
  | property title must have a type                                                                                                                                                                                                                                     |
  | tool call must be of type function                                                                                                                                                                                                                                  |
  | invalid request: length must be one of 'short', 'medium', or 'long'.                                                                                                                                                                                                |
  | invalid request: duplicate document ID adfasd at index 1 and 0                                                                                                                                                                                                      |
  | too many tokens: minimal context could not be added to prompt (size limit exceeded by 280 tokens)                                                                                                                                                                   |
  | invalid request: raw prompting is not supported with the following parameter(s): connectors, documents, search\_queries\_only, tools.                                                                                                                               |
  | invalid request: max\_tokens can only be 0 if return\_likelihoods is set to 'ALL' and prompt is longer than 1 token.                                                                                                                                                |
</details>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
