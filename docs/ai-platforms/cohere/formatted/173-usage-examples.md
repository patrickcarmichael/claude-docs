---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage examples

This section provides usage examples of the JSON Schema [parameters that are supported](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) in Structured Outputs (Tools).

<Accordion title="Helper code">
  The examples on this page each provide a tool schema and a `message` (the user message). To get an output, pass those values to a Chat endpoint call, as shown in the helper code below.

  <Tabs>
    <Tab title="Cohere platform">
```python PYTHON
      # ! pip install -U cohere

      import cohere

      co = cohere.ClientV2(
          "COHERE_API_KEY"
      )  # Get your free API key here: https://dashboard.cohere.com/api-keys

```
    </Tab>

    <Tab title="Private deployment">
```python PYTHON
      # ! pip install -U cohere

      import cohere

      co = cohere.ClientV2(
          api_key="",  # Leave this blank

          base_url="<YOUR_DEPLOYMENT_URL>",
      )
```
    </Tab>
  </Tabs>

  <CodeBlocks>
```python PYTHON
    response = co.chat(
        # The model name. Example: command-a-03-2025

        model="MODEL_NAME",
        # The user message. Optional - you can first add a `system_message` role

        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        # The tool schema that you define

        tools=tools,
        # This guarantees that the output will adhere to the schema

        strict_tools=True,
        # Typically, you'll need a low temperature for more deterministic outputs

        temperature=0,
    )

    for tc in response.message.tool_calls:
        print(f"{tc.function.name} | Parameters: {tc.function.arguments}")
```
```bash cURL
    curl --request POST \
      --url https://api.cohere.ai/v2/chat \
      --header 'accept: application/json' \
      --header 'content-type: application/json' \
      --header "Authorization: bearer $CO_API_KEY" \
      --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "What'\''s the weather in Toronto?"
        }
      ],
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather",
            "description": "Gets the weather of a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "the location to get the weather, example: San Francisco."
                }
              },
              "required": ["location"]
            }
          }
        }
      ],
      "strict_tools": true,
      "temperature": 0
    }'
```
  </CodeBlocks>
</Accordion>

### Basic types

#### String

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "the location to get the weather, example: San Francisco.",
                    }
                },
                "required": ["location"],
            },
        },
    },
]

message = "What's the weather in Toronto?"
```
Example response:
```mdx wordWrap
get_weather
{
  "location": "Toronto"
}
```

#### Integer

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Adds two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "first_number": {
                        "type": "integer",
                        "description": "The first number to add.",
                    },
                    "second_number": {
                        "type": "integer",
                        "description": "The second number to add.",
                    },
                },
                "required": ["first_number", "second_number"],
            },
        },
    }
]

message = "What is five plus two"
```
Example response:
```mdx wordWrap
add_numbers
{
  "first_number": 5,
  "second_number": 2
}
```

#### Float

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Adds two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "first_number": {
                        "type": "number",
                        "description": "The first number to add.",
                    },
                    "second_number": {
                        "type": "number",
                        "description": "The second number to add.",
                    },
                },
                "required": ["first_number", "second_number"],
            },
        },
    }
]

message = "What is 5.3 plus 2"
```
Example response:
```mdx wordWrap
add_numbers
{
  "first_number": 5.3,
  "second_number": 2
}
```

#### Boolean

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "reserve_tickets",
            "description": "Reserves a train ticket",
            "parameters": {
                "type": "object",
                "properties": {
                    "quantity": {
                        "type": "integer",
                        "description": "The quantity of tickets to reserve.",
                    },
                    "trip_protection": {
                        "type": "boolean",
                        "description": "Indicates whether to add trip protection.",
                    },
                },
                "required": ["quantity", "trip_protection"],
            },
        },
    }
]

message = "Book me 2 tickets. I don't need trip protection."
```
Example response:
```mdx wordWrap
reserve_tickets
{
  "quantity": 2,
  "trip_protection": false
}
```

### Array

#### With specific types

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "locations": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "The locations to get weather.",
                    }
                },
                "required": ["locations"],
            },
        },
    },
]

message = "What's the weather in Toronto and New York?"
```
Example response:
```mdx wordWrap
get_weather
{
  "locations": [
    "Toronto",
    "New York"
  ]
}
```

#### Without specific types

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "locations": {
                        "type": "array",
                        "description": "The locations to get weather.",
                    }
                },
                "required": ["locations"],
            },
        },
    },
]

message = "What's the weather in Toronto and New York?"
```
Example response:
```mdx wordWrap
get_weather
{
  "locations": [
    "Toronto",
    "New York"
  ]
}
```

#### Lists of lists

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "maxPoints",
            "description": "Finds the maximum number of points on a line.",
            "parameters": {
                "type": "object",
                "properties": {
                    "points": {
                        "type": "array",
                        "description": "The list of points. Points are 2 element lists [x, y].",
                        "items": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "A point represented by a 2 element list [x, y].",
                        },
                    }
                },
                "required": ["points"],
            },
        },
    }
]

message = "Please provide the maximum number of collinear points for this set of coordinates - [[1,1],[2,2],[3,4],[5,5]]."
```
Example response:
```mdx wordWrap
maxPoints
{
  "points": [
    [1,1],
    [2,2],
    [3,4],
    [5,5]
  ]
}
```

### Others

#### Nested objects

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_furniture_products",
            "description": "Searches for furniture products given the user criteria.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_type": {
                        "type": "string",
                        "description": "The type of the product to search for.",
                    },
                    "features": {
                        "type": "object",
                        "properties": {
                            "material": {"type": "string"},
                            "style": {"type": "string"},
                        },
                        "required": ["style"],
                    },
                },
                "required": ["product_type"],
            },
        },
    }
]

message = "I'm looking for a dining table made of oak in Scandinavian style."
```
Example response:
```mdx wordWrap
search_furniture_products
{
  "features": {
    "material": "oak",
    "style": "Scandinavian"
  },
  "product_type": "dining table"
}
```

#### Enums

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "fetch_contacts",
            "description": "Fetch a contact by type",
            "parameters": {
                "type": "object",
                "properties": {
                    "contact_type": {
                        "type": "string",
                        "description": "The type of contact to fetch.",
                        "enum": ["customer", "supplier"],
                    }
                },
                "required": ["contact_type"],
            },
        },
    }
]

message = "Give me vendor contacts."
```
Example response:
```mdx wordWrap
fetch_contacts
{
  "contact_type": "supplier"
}
```

#### Const

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location to get weather.",
                    },
                    "country": {
                        "type": "string",
                        "description": "The country for the weather lookup",
                        "const": "Canada",
                    },
                },
                "required": ["location", "country"],
            },
        },
    },
]

message = "What's the weather in Toronto and Vancouver?"
```
Example response:
```mdx wordWrap
get_weather
{
  "country": "Canada",
  "location": "Toronto"
}
---
get_weather
{
  "country": "Canada",
  "location": "Vancouver"
}
---
```

#### Pattern

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "query_product_by_sku",
            "description": "Queries products by SKU pattern",
            "parameters": {
                "type": "object",
                "properties": {
                    "sku_pattern": {
                        "type": "string",
                        "description": "Pattern to match SKUs",
                        "pattern": "[A-Z]{3}[0-9]{4}",
                    }
                },
                "required": ["sku_pattern"],
            },
        },
    }
]

message = "Check the stock level of this product - 7374 hgY"
```
Example response:
```mdx wordWrap
query_product_by_sku
{
  "sku_pattern": "HGY7374"
}
```

#### Format

```python PYTHON
tools = [
    {
        "type": "function",
        "function": {
            "name": "book_hotel",
            "description": "Books a hotel room for a specific check-in date",
            "parameters": {
                "type": "object",
                "properties": {
                    "hotel_name": {
                        "type": "string",
                        "description": "Name of the hotel",
                    },
                    "check_in_date": {
                        "type": "string",
                        "description": "Check-in date for the hotel",
                        "format": "date",
                    },
                },
                "required": ["hotel_name", "check_in_date"],
            },
        },
    }
]

message = "Book a room at the Grand Hotel with check-in on Dec 2 2024"
```
Example response:
```mdx wordWrap
book_hotel
{
  "check_in_date": "2024-12-02",
  "hotel_name": "Grand Hotel"
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
