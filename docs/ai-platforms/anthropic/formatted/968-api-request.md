---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API Request

***

<Tabs>
  <Tab title="Python">
```Python
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")

      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists: \n \nCustomers: \n- customer_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- address (VARCHAR) \n- city (VARCHAR) \n- state (VARCHAR) \n- zip_code (VARCHAR) \n \nProducts: \n- product_id (INT, PRIMARY KEY) \n- product_name (VARCHAR) \n- description (TEXT) \n- category (VARCHAR) \n- price (DECIMAL) \n- stock_quantity (INT) \n \nOrders: \n- order_id (INT, PRIMARY KEY) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- order_date (DATE) \n- total_amount (DECIMAL) \n- status (VARCHAR) \n \nOrder_Items: \n- order_item_id (INT, PRIMARY KEY) \n- order_id (INT, FOREIGN KEY REFERENCES Orders) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- quantity (INT) \n- price (DECIMAL) \n \nReviews: \n- review_id (INT, PRIMARY KEY) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- rating (INT) \n- comment (TEXT) \n- review_date (DATE) \n \nEmployees: \n- employee_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- hire_date (DATE) \n- job_title (VARCHAR) \n- department (VARCHAR) \n- salary (DECIMAL) \n \nProvide the SQL query that would retrieve the data based on the natural language request.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
            }
          ]
        }
      ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="TypeScript">
```TypeScript
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 0,
      system: "Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists:  \n  \nCustomers:  \n- customer_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- address (VARCHAR)  \n- city (VARCHAR)  \n- state (VARCHAR)  \n- zip_code (VARCHAR)  \n  \nProducts:  \n- product_id (INT, PRIMARY KEY)  \n- product_name (VARCHAR)  \n- description (TEXT)  \n- category (VARCHAR)  \n- price (DECIMAL)  \n- stock_quantity (INT)  \n  \nOrders:  \n- order_id (INT, PRIMARY KEY)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- order_date (DATE)  \n- total_amount (DECIMAL)  \n- status (VARCHAR)  \n  \nOrder_Items:  \n- order_item_id (INT, PRIMARY KEY)  \n- order_id (INT, FOREIGN KEY REFERENCES Orders)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- quantity (INT)  \n- price (DECIMAL)  \n  \nReviews:  \n- review_id (INT, PRIMARY KEY)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- rating (INT)  \n- comment (TEXT)  \n- review_date (DATE)  \n  \nEmployees:  \n- employee_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- hire_date (DATE)  \n- job_title (VARCHAR)  \n- department (VARCHAR)  \n- salary (DECIMAL)  \n  \nProvide the SQL query that would retrieve the data based on the natural language request.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>

  <Tab title="AWS Bedrock Python">
```Python
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

    # for authentication options

    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=0,
        system="Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists:  \n  \nCustomers:  \n- customer_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- address (VARCHAR)  \n- city (VARCHAR)  \n- state (VARCHAR)  \n- zip_code (VARCHAR)  \n  \nProducts:  \n- product_id (INT, PRIMARY KEY)  \n- product_name (VARCHAR)  \n- description (TEXT)  \n- category (VARCHAR)  \n- price (DECIMAL)  \n- stock_quantity (INT)  \n  \nOrders:  \n- order_id (INT, PRIMARY KEY)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- order_date (DATE)  \n- total_amount (DECIMAL)  \n- status (VARCHAR)  \n  \nOrder_Items:  \n- order_item_id (INT, PRIMARY KEY)  \n- order_id (INT, FOREIGN KEY REFERENCES Orders)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- quantity (INT)  \n- price (DECIMAL)  \n  \nReviews:  \n- review_id (INT, PRIMARY KEY)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- rating (INT)  \n- comment (TEXT)  \n- review_date (DATE)  \n  \nEmployees:  \n- employee_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- hire_date (DATE)  \n- job_title (VARCHAR)  \n- department (VARCHAR)  \n- salary (DECIMAL)  \n  \nProvide the SQL query that would retrieve the data based on the natural language request.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
                    }
                ]
            }
        ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
```TypeScript
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 0,
      system: "Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists:  \n  \nCustomers:  \n- customer_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- address (VARCHAR)  \n- city (VARCHAR)  \n- state (VARCHAR)  \n- zip_code (VARCHAR)  \n  \nProducts:  \n- product_id (INT, PRIMARY KEY)  \n- product_name (VARCHAR)  \n- description (TEXT)  \n- category (VARCHAR)  \n- price (DECIMAL)  \n- stock_quantity (INT)  \n  \nOrders:  \n- order_id (INT, PRIMARY KEY)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- order_date (DATE)  \n- total_amount (DECIMAL)  \n- status (VARCHAR)  \n  \nOrder_Items:  \n- order_item_id (INT, PRIMARY KEY)  \n- order_id (INT, FOREIGN KEY REFERENCES Orders)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- quantity (INT)  \n- price (DECIMAL)  \n  \nReviews:  \n- review_id (INT, PRIMARY KEY)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- rating (INT)  \n- comment (TEXT)  \n- review_date (DATE)  \n  \nEmployees:  \n- employee_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- hire_date (DATE)  \n- job_title (VARCHAR)  \n- department (VARCHAR)  \n- salary (DECIMAL)  \n  \nProvide the SQL query that would retrieve the data based on the natural language request.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>

  <Tab title="Vertex AI Python">
```Python
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=1000,
        temperature=0,
        system="Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists:  \n  \nCustomers:  \n- customer_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- address (VARCHAR)  \n- city (VARCHAR)  \n- state (VARCHAR)  \n- zip_code (VARCHAR)  \n  \nProducts:  \n- product_id (INT, PRIMARY KEY)  \n- product_name (VARCHAR)  \n- description (TEXT)  \n- category (VARCHAR)  \n- price (DECIMAL)  \n- stock_quantity (INT)  \n  \nOrders:  \n- order_id (INT, PRIMARY KEY)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- order_date (DATE)  \n- total_amount (DECIMAL)  \n- status (VARCHAR)  \n  \nOrder_Items:  \n- order_item_id (INT, PRIMARY KEY)  \n- order_id (INT, FOREIGN KEY REFERENCES Orders)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- quantity (INT)  \n- price (DECIMAL)  \n  \nReviews:  \n- review_id (INT, PRIMARY KEY)  \n- product_id (INT, FOREIGN KEY REFERENCES Products)  \n- customer_id (INT, FOREIGN KEY REFERENCES Customers)  \n- rating (INT)  \n- comment (TEXT)  \n- review_date (DATE)  \n  \nEmployees:  \n- employee_id (INT, PRIMARY KEY)  \n- first_name (VARCHAR)  \n- last_name (VARCHAR)  \n- email (VARCHAR)  \n- phone (VARCHAR)  \n- hire_date (DATE)  \n- job_title (VARCHAR)  \n- department (VARCHAR)  \n- salary (DECIMAL)  \n  \nProvide the SQL query that would retrieve the data based on the natural language request.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
                    }
                ]
            }
        ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="Vertex AI TypeScript">
```TypeScript
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 0,
    system: "Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists: \n \nCustomers: \n- customer_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- address (VARCHAR) \n- city (VARCHAR) \n- state (VARCHAR) \n- zip_code (VARCHAR) \n \nProducts: \n- product_id (INT, PRIMARY KEY) \n- product_name (VARCHAR) \n- description (TEXT) \n- category (VARCHAR) \n- price (DECIMAL) \n- stock_quantity (INT) \n \nOrders: \n- order_id (INT, PRIMARY KEY) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- order_date (DATE) \n- total_amount (DECIMAL) \n- status (VARCHAR) \n \nOrder_Items: \n- order_item_id (INT, PRIMARY KEY) \n- order_id (INT, FOREIGN KEY REFERENCES Orders) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- quantity (INT) \n- price (DECIMAL) \n \nReviews: \n- review_id (INT, PRIMARY KEY) \n- product_id (INT, FOREIGN KEY REFERENCES Products) \n- customer_id (INT, FOREIGN KEY REFERENCES Customers) \n- rating (INT) \n- comment (TEXT) \n- review_date (DATE) \n \nEmployees: \n- employee_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- phone (VARCHAR) \n- hire_date (DATE) \n- job_title (VARCHAR) \n- department (VARCHAR) \n- salary (DECIMAL) \n \nProvide the SQL query that would retrieve the data based on the natural language request.",
    messages: [
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders."
    }
    ]
    }
    ]
    });
    console.log(msg);
```
  </Tab>
</Tabs>
```
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
