---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameter types support

### Supported schema features

The Structured Outputs feature (both JSON and Tools mode) relies on the JSON Schema notation for defining the parameters. JSON Schema allows developers to specify the expected format of JSON objects, ensuring that the data adheres to predefined rules and constraints.

Structured Outputs supports a subset of the JSON Schema specification, detailed in the tables below. This is broken down into three categories:

* Structured Outputs (JSON)
* Structured Outputs (Tools) - When `strict_tools` is set to `True`
* Tool Use - When `strict_tools` is set to `False`

#### Basic types

| Parameter | [Structured Outputs (JSON)](#) | [Structured Outputs (Tools)](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) | [Tool Use](https://docs.cohere.com/v2/docs/tool-use) |
| --------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| String    | Yes                            | Yes                                                                                             | Yes                                                  |
| Integer   | Yes                            | Yes                                                                                             | Yes                                                  |
| Float     | Yes                            | Yes                                                                                             | Yes                                                  |
| Boolean   | Yes                            | Yes                                                                                             | Yes                                                  |

See usage examples for [JSON](https://docs.cohere.com/v2/docs/parameter-types-in-json#basic-types) and [Tools](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use#basic-types).

#### Arrays

| Parameter                       | [Structured Outputs (JSON)](#) | [Structured Outputs (Tools)](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) | [Tool Use](https://docs.cohere.com/v2/docs/tool-use) |
| ------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Arrays - With specific types    | Yes                            | Yes                                                                                             | Yes                                                  |
| Arrays - Without specific types | Yes                            | Yes                                                                                             | Yes                                                  |
| Arrays - List of lists          | Yes                            | Yes                                                                                             | Yes                                                  |

See usage examples for [JSON](https://docs.cohere.com/v2/docs/parameter-types-in-json#arrays) and [Tools](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use#arrays).

#### Others

| Parameter            | [Structured Outputs (JSON)](#) | [Structured Outputs (Tools)](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) | [Tool Use](https://docs.cohere.com/v2/docs/tool-use) |
| -------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Nested objects       | Yes                            | Yes                                                                                             | Yes                                                  |
| Enum                 | Yes                            | Yes                                                                                             | Yes                                                  |
| Const¹               | Yes                            | Yes                                                                                             | Yes                                                  |
| Pattern              | Yes                            | Yes                                                                                             | Yes                                                  |
| Format²              | Yes                            | Yes                                                                                             | Yes                                                  |
| \$ref                | Yes                            | Yes                                                                                             | Yes                                                  |
| \$def                | Yes                            | Yes                                                                                             | Yes                                                  |
| additionalProperties | Yes³                           | Yes⁴                                                                                            | Yes                                                  |
| uniqueItems          | No                             | No                                                                                              | Yes                                                  |
| anyOf                | Yes                            | Yes                                                                                             | Yes                                                  |

¹ Const is supported for these types: `int`, `float`, `bool`, `type(None)`, `str`.

² Format is supported for these values: `date-time`, `uuid`, `date`, `time`.

³ In Structured Outputs (JSON), `additionalProperties` does not enforce `required`, `dependencies`, `propertyNames`, `anyOf`, `allOf`, `oneOf`.

⁴ In Structured Outputs (Tools), `additionalProperties` does not enforce `required`, `dependencies`, `propertyNames`, `any Of`, `all Of`, `one Of`.

See usage examples for [JSON](https://docs.cohere.com/v2/docs/parameter-types-in-json#others) and [Tools](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use#others).

### Unsupported schema features

We do not support the entirety of the [JSON Schema specification](https://json-schema.org/specification).  Below is a list of some unsupported features:

* [Schema Composition](https://json-schema.org/understanding-json-schema/reference/combining#schema-composition) (`allOf`, `oneOf` and `not`)
* [Numeric Ranges](https://json-schema.org/understanding-json-schema/reference/numeric#range) (`maximum` and  `minimum`)
* [Array Length Ranges](https://json-schema.org/understanding-json-schema/reference/array#length) (`minItems` and `maxItems`)
* String limitations:
  * [String Length](https://json-schema.org/understanding-json-schema/reference/string#length) (`maxLength` and `minLength`)
  * The following are not supported in [Regular Expressions](https://json-schema.org/understanding-json-schema/reference/string#regexp)
    * `^`
    * `$`
    * `?=`
    * `?!`
  * The following [formats](https://json-schema.org/understanding-json-schema/reference/string#format) are the only supported ones
    * `date-time`
    * `uuid`
    * `date`
    * `time`

<Info title="Important">
  Note: Using Structured Outputs (in both JSON Schema and Tools modes) will incur a latency overhead required for processing the structured schema. This increase in latency only applies for the first few requests, since the schema is cached afterwards.
</Info>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
