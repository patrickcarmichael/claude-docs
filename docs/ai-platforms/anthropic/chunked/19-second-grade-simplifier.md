**Navigation:** [← Previous](./18-meeting-scribe.md) | [Index](./index.md) | [Next →](./20-airport-code-analyst.md)

---

# Second-grade simplifier
Source: https://docs.claude.com/en/resources/prompt-library/second-grade-simplifier

Make complex text easy for young learners to understand.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner. |
| User   | The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur.                                                               |

## Example Output

Mitochondria are tiny parts inside cells that work like little power stations. They make a special molecule called ATP, which is like the cell's energy money. ATP helps the cell do important jobs and keeps it running smoothly, just like how money helps people buy things they need. Mitochondria are very important because without them, cells wouldn't have the energy to function properly.

***

## API Request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 0,
      system: "Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    # for authentication options
    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=0,
        system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 0,
      system: "Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
    model="claude-sonnet-4@20250514",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
    messages=[
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
    }
    ]
    }
    ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 1000,
      temperature: 0,
      system: "Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information in a clear, engaging way. The short rewritten text should convey the core ideas of the original text in an age-appropriate manner.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "The mitochondria, often referred to as the powerhouses of the cell, are essential organelles that play a crucial role in the production of adenosine triphosphate (ATP) through the process of cellular respiration. ATP is the primary energy currency of the cell, enabling various cellular functions and biochemical reactions to occur."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Simile savant
Source: https://docs.claude.com/en/resources/prompt-library/simile-savant

Generate similes from basic descriptions.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Role | Content                                                                                    |
| ---- | ------------------------------------------------------------------------------------------ |
| User | Help me create some similes to describe a person's laughter that is joyful and contagious? |

## Example Output

1. His laughter bubbled up like a freshly opened bottle of champagne, effervescent and full of life.
2. Their laughter was as warm and inviting as a cozy fireplace on a chilly evening, drawing people in to share in the merriment.

***

## API Request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=1,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    # for authentication options
    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# SQL sorcerer
Source: https://docs.claude.com/en/resources/prompt-library/sql-sorcerer

Transform everyday language into SQL queries.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists: <br /> <br /> Customers: <br /> - customer\_id (INT, PRIMARY KEY) <br /> - first\_name (VARCHAR) <br /> - last\_name (VARCHAR) <br /> - email (VARCHAR) <br /> - phone (VARCHAR) <br /> - address (VARCHAR) <br /> - city (VARCHAR) <br /> - state (VARCHAR) <br /> - zip\_code (VARCHAR) <br /><br /> Products: <br /> - product\_id (INT, PRIMARY KEY) <br /> - product\_name (VARCHAR) <br /> - description (TEXT) <br /> - category (VARCHAR) <br /> - price (DECIMAL) <br /> - stock\_quantity (INT) <br /> <br /> Orders: <br /> - order\_id (INT, PRIMARY KEY) <br /> - customer\_id (INT, FOREIGN KEY REFERENCES Customers) <br /> - order\_date (DATE) <br /> - total\_amount (DECIMAL) <br /> - status (VARCHAR) <br /><br /> Order\_Items: <br /> - order\_item\_id (INT, PRIMARY KEY) <br /> - order\_id (INT, FOREIGN KEY REFERENCES Orders) <br /> - product\_id (INT, FOREIGN KEY REFERENCES Products) <br /> - quantity (INT) <br /> - price (DECIMAL) <br /><br /> Reviews: <br /> - review\_id (INT, PRIMARY KEY) <br /> - product\_id (INT, FOREIGN KEY REFERENCES Products) <br /> - customer\_id (INT, FOREIGN KEY REFERENCES Customers) <br /> - rating (INT) <br /> - comment (TEXT) <br /> - review\_date (DATE) <br /><br /> Employees: <br /> - employee\_id (INT, PRIMARY KEY) <br /> - first\_name (VARCHAR) <br /> - last\_name (VARCHAR) <br /> - email (VARCHAR) <br /> - phone (VARCHAR) <br /> - hire\_date (DATE) <br /> - job\_title (VARCHAR) <br /> - department (VARCHAR) <br /> - salary (DECIMAL) <br /><br /> Provide the SQL query that would retrieve the data based on the natural language request. |
| User   | Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Example output

```sql  theme={null}
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Reviews r ON c.customer_id = r.customer_id
WHERE r.review_id IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name;

```

## API Request

***

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
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
    ```TypeScript  theme={null}
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
    ```Python  theme={null}
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
    ```TypeScript  theme={null}
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
    ```Python  theme={null}
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
    ```TypeScript  theme={null}
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


# Storytelling sidekick
Source: https://docs.claude.com/en/resources/prompt-library/storytelling-sidekick

Collaboratively create engaging stories with the user, offering plot twists and character development.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                  |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative. |
| User   | Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other.                                                                                                                                                   |

## Example output

Great idea! Let's dive into Lila's story and explore how her newfound power affects her life and the town around her.

Lila, a 22-year-old barista, has always been fascinated by the weather. One day, during a particularly strong thunderstorm, she discovers that she can control the elements with her mind. At first, she's thrilled and uses her power to help the town, ensuring perfect weather for important events like the annual harvest festival.

However, as time goes on, some of the townspeople grow suspicious of Lila's uncanny ability to predict and control the weather. They start to whisper about her being a witch, and some even blame her for any adverse weather events that occur.

To make matters worse, Lila's childhood friend, Tom, returns to town after years away. He's now a successful meteorologist and is determined to uncover the truth behind the town's unusual weather patterns. Lila must decide whether to trust Tom with her secret or risk losing his friendship.

As tensions rise in the town, Lila learns that her powers come with a price. Each time she uses them, she experiences a physical and emotional toll. She must learn to control her abilities and find a way to balance her desire to help others with her own well-being.

What do you think should happen next in the story? How could Lila's relationship with Tom evolve, and what challenges might she face as she tries to master her powers and win back the trust of the townspeople?

***

## API Request

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      system="You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 2000,
      temperature: 1,
      system: "You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    # for authentication options
    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=2000,
        temperature=1,
        system="You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 2000,
      temperature: 1,
      system: "You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=2000,
        temperature=1,
        system="You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 1,
    system: "You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and build upon them to create a captivating narrative.",
    messages: [
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Let's create a story about a young woman named Lila who discovers she has the power to control the weather. She lives in a small town where everyone knows each other."
    }
    ]
    }
    ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Time travel consultant
Source: https://docs.claude.com/en/resources/prompt-library/time-travel-consultant

Help the user navigate hypothetical time travel scenarios and their implications.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                  |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation. |
| User   | Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?                                                                                                                                                                   |

## Example output

That's an intriguing scenario! Let's explore the potential implications of preventing the invention of the airplane in 1900:

1. Technological advancement: The invention of the airplane was a significant milestone in human history, paving the way for rapid globalization, modern warfare, and space exploration. Without it, the pace of technological advancement in fields like transportation, communication, and aerospace engineering might be significantly slower.
2. Economic impact: The aviation industry has become a crucial part of the global economy, contributing to trade, tourism, and job creation. In a world without airplanes, the economy would likely be more localized, with a greater emphasis on ground and sea transportation.
3. Cultural exchange: Air travel has facilitated the exchange of ideas, cultures, and people across the globe. Without airplanes, cultural exchange would be more limited, potentially leading to a less interconnected and diverse world.
4. Butterfly effect: Removing such a significant invention from history could have far-reaching and unpredictable consequences. It might alter the course of major historical events, such as wars, migrations, and scientific discoveries, which could drastically change the world as we know it.
5. Paradoxes: If your actions in the past prevent the invention of the airplane, it raises questions about the consistency of the timeline. Would you still have the knowledge and motivation to travel back in time in a world where airplanes were never invented?

These are just a few potential implications to consider. It's important to remember that the consequences of altering past events can be complex, far-reaching, and often difficult to predict.

What are your thoughts on this scenario? What other aspects or implications do you think are worth exploring?

***

## API Request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      system="You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?"
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 2000,
      temperature: 1,
      system: "You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?"
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

    # for authentication options

    client = AnthropicBedrock()

    message = client.messages.create(
    model="anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens=2000,
    temperature=1,
    system="You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation.",
    messages=[
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?"
    }
    ]
    }
    ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title=" AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 2000,
      temperature: 1,
      system: "You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?"
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title=" Vertex AI Python">
    ```
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
    model="claude-sonnet-4@20250514",
    max_tokens=2000,
    temperature=1,
    system="You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation.",
    messages=[
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?"
    }
    ]
    }
    ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```typescript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 2000,
      temperature: 1,
      system: "You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and ethical considerations involved in each specific scenario, while maintaining a friendly and engaging conversation.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Let's say I have a time machine and I travel back to the year 1900. While there, I accidentally prevent the invention of the airplane by the Wright brothers. What would be the potential implications of this action?"
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Tongue twister
Source: https://docs.claude.com/en/resources/prompt-library/tongue-twister

Create challenging tongue twisters.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Role | Content                                                                                                                                                                                                                                                                                               |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters. |

## Example Output

Tongue Twister 1:\
The shrewd shrew chewed through the shiny, shimmering shoe.

Tongue Twister 2:\
Brisk breezes blew by the blue-blooded, blabbering, babbling baboon.

Tongue Twister 3:\
The perplexed piper picked a peck of pickled peppers while practicing his piping.

Tongue Twister 4:\
Six sleek, slick, slender sleds slid swiftly down the steep, snowy slope.

***

## API Request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=1,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    # for authentication options
    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potentially humorous. Consider incorporating wordplay, rhyme, and alliteration to enhance the difficulty and enjoyment of the tongue twisters."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Trivia generator
Source: https://docs.claude.com/en/resources/prompt-library/trivia-generator

Generate trivia questions on a wide range of topics and provide hints when needed.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily. |

## Example Output

Category: Geography

Question:\
What is the only country in the world that borders both France and Spain?

Hint 1: This country is located in the Pyrenees mountains between France and Spain.\
Hint 2: It is known for its stunning mountain landscapes, ski resorts, and tax-free shopping.\
Hint 3: The country's capital city features the name of the country itself.

Answer: Andorra

Category: Science

Question:\
What is the process by which plants convert sunlight, water, and carbon dioxide into energy and oxygen?

Hint 1: This process is essential for life on Earth, as it provides both food and oxygen.\
Hint 2: It takes place primarily in the leaves of plants.\
Hint 3: The process involves chlorophyll, a green pigment that absorbs sunlight.

Answer: Photosynthesis

Category: Literature

Question:\
Who wrote the classic novel "Pride and Prejudice," which was first published in 1813?

Hint 1: The author is a British woman who lived from 1775 to 1817.\
Hint 2: She is known for her witty, insightful portrayals of English society and manners.\
Hint 3: Her other famous works include "Sense and Sensibility" and "Emma."

Answer: Jane Austen

Category: History

Question:\
In what year did the Berlin Wall, which divided East and West Germany, begin to be torn down?

Hint 1: The event occurred in the late 20th century.\
Hint 2: It marked a significant moment in the end of the Cold War.\
Hint 3: The year is often associated with the phrase "fall of communism" in Europe.

Answer: 1989

***

## API Request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=0.5,
      messages=[
        {
        "role": "user",
        "content": [
            {
              "type": "text",
              "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 2000,
      temperature: 0.5,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

    # for authentication options

    client = AnthropicBedrock()

    message = client.messages.create(
    model="anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens=2000,
    temperature=0.5,
    messages=[
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
    }
    ]
    }
    ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 2000,
      temperature: 0.5,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=2000,
        temperature=0.5,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 2000,
      temperature: 0.5,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create questions that test the user's knowledge or reasoning skills. Offer a series of increasingly specific hints to guide users towards the solution. Ensure that the questions are challenging and that the hints provide enough information to help the user without giving away the answer too easily."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# VR fitness innovator
Source: https://docs.claude.com/en/resources/prompt-library/vr-fitness-innovator

Brainstorm creative ideas for virtual reality fitness games.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness. |

## Example Output

1. Idea: VR Parkour Adventure\
   Description: Players navigate through a dynamic urban environment, running, jumping, climbing, and performing parkour stunts to overcome obstacles and reach objectives. The game adapts to the player's movements, providing an intense full-body workout while exploring the virtual city.\
   Key features: Realistic parkour mechanics, procedurally generated environments, multiplayer races, and challenges.\
   Fitness aspects: Cardio, agility, coordination, and lower body strength.
2. Idea: Rhythm Boxing\
   Description: A high-energy boxing game set to the beat of popular music tracks. Players must punch, dodge, and block in sync with the rhythm to score points and progress through increasingly challenging levels. The game offers a variety of boxing styles and training modes.\
   Key features: Licensed music, customizable boxers, online multiplayer, and a diverse range of boxing techniques.\
   Fitness aspects: Cardio, upper body strength, reflexes, and endurance.
3. Idea: VR Fitness RPG\
   Description: An immersive role-playing game where players create their own character and embark on a quest to save a fantasy world. The game combines traditional RPG elements with fitness challenges, requiring players to perform physical exercises to cast spells, defeat enemies, and level up their character.\
   Key features: Character customization, skill trees, epic boss battles, and a mix of strength, cardio, and flexibility exercises.\
   Fitness aspects: Full-body workouts, strength training, cardio, and flexibility.

***

## API Request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=1,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    # for authentication options
    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=1000,
        temperature=1,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 1000,
      temperature: 1,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Website wizard
Source: https://docs.claude.com/en/resources/prompt-library/website-wizard

Create one-page websites based on user specifications.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| User   | Create a one-page website for an online learning platform called "EduQuest" with the following features and sections:<br /><br />1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar.<br />2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between "Learn at your own pace," "Discover new passions," and "Expand your horizons" every 3 seconds, and a "Get Started" button leading to a course catalog.<br />3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions.<br />4. An interactive "Learning Paths" section with a short quiz to determine learning styles and interests, and a button to start the quiz.<br />5. A "Success Stories" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names.<br />6. A footer with links to the platform's blog, FAQ, privacy policy, and a "Contact Us" button that opens a modal window with a contact form and customer support information.<br /><br />Include filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section.<br /><br />The JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds. |

## Example output

```html  theme={null}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduQuest - Online Learning Platform</title>
    <style>
        /* CSS Styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 999;
        }

        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: space-between;
        }

        nav ul li a {
            color: #fff;
            text-decoration: none;
            padding: 10px;
        }

        .hero {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 24px;
            margin-bottom: 40px;
        }

        .hero button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #333;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        .featured-courses, .success-stories {
            padding: 40px;
        }

        .course-card {
            background-color: #f5f5f5;
            padding: 20px;
            margin-bottom: 20px;
        }

        .testimonial {
            background-color: #f5f5f5;
            padding: 20px;
            margin-bottom: 20px;
        }

        footer {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }

        footer a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        footer button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #fff;
            color: #333;
            border: none;
            cursor: pointer;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Math</a></li>
                <li><a href="#">Science</a></li>
                <li><a href="#">Languages</a></li>
                <li><a href="#">Arts</a></li>
                <li><input type="text" placeholder="Search"></li>
            </ul>
        </nav>
    </header>

    <section class="hero">
        <video src="placeholder-video.mp4" autoplay loop muted></video>
        <h1>Welcome to EduQuest</h1>
        <p id="tagline">Learn at your own pace</p>
        <button>Get Started</button>
    </section>

    <section class="featured-courses">
        <h2>Featured Courses</h2>
        <div class="course-card">
            <img src="placeholder-course-image.jpg" alt="Course Image">
            <h3>Course Title</h3>
            <p>Instructor: John Doe</p>
            <p>Course description goes here.</p>
        </div>
        <div class="course-card">
            <img src="placeholder-course-image.jpg" alt="Course Image">
            <h3>Course Title</h3>
            <p>Instructor: Jane Smith</p>
            <p>Course description goes here.</p>
        </div>
    </section>

    <section class="success-stories">
        <h2>Success Stories</h2>
        <div class="testimonial">
            <p>"EduQuest helped me learn a new skill and advance my career. Highly recommended!"</p>
            <p>- John Doe</p>
        </div>
        <div class="testimonial">
            <p>"I never thought I could learn a new language online, but EduQuest made it possible. Thank you!"</p>
            <p>- Jane Smith</p>
        </div>
    </section>

    <footer>
        <a href="#">Blog</a>
        <a href="#">FAQ</a>
        <a href="#">Privacy Policy</a>
        <button>Contact Us</button>
    </footer>

    <script>
        // JavaScript Code
        const taglines = [
            "Learn at your own pace",
            "Discover new passions",
            "Expand your horizons"
        ];

        let index = 0;
        const taglineElement = document.getElementById("tagline");

        function rotateTagline() {
            taglineElement.textContent = taglines[index];
            index = (index + 1) % taglines.length;
        }

        setInterval(rotateTagline, 3000);
    </script>
</body>
</html>
```

> This code creates a one-page website for "EduQuest" with the following features and sections:
>
> A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar.
>
> A hero section with a placeholder video background, a dynamic tagline that rotates between "Learn at your own pace," "Discover new passions," and "Expand your horizons" every 3 seconds, and a "Get Started" button.
>
> A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions.
>
> A "Success Stories" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names.
>
> A footer with links to the platform's blog, FAQ, privacy policy, and a "Contact Us" button.
>
> The CSS styles are embedded within the `<style>` tag in the `<head>` section, and the JavaScript code is placed within the `<script>` tag at the end of the `<body>` section.
>
> The JavaScript code handles the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds using the setInterval function.
>
> Please note that the video background, course images, and testimonials are placeholders and should be replaced with actual content.

## API request

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import anthropic

    client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4000,
      temperature=0,
      system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 4000,
      temperature: 0,
      system: "Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections:  \n  \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar.  \n  \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog.  \n  \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions.  \n  \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz.  \n  \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names.  \n  \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information.  \n  \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section.  \n  \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

    # for authentication options

    client = AnthropicBedrock()

    message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=4000,
      temperature=0,
      system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```typescript  theme={null}

    import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 4000,
      temperature: 0,
      system: "Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=4000,
      temperature=0,
      system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```typescript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 4000,
    temperature: 0,
    system: "Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
    messages: [
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
    }
    ]
    }
    ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Claude Developer Platform
Source: https://docs.claude.com/en/release-notes/overview

Updates to the Claude Developer Platform, including the Claude API, client SDKs, and the Claude Console.

<Tip>
  For release notes on Claude Apps, see the [Release notes for Claude Apps in the Claude Help Center](https://support.claude.com/en/articles/12138966-release-notes).

  For updates to Claude Code, see the [complete CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) in the `claude-code` repository.
</Tip>

#### October 28, 2025

* We announced the deprecation of the Claude Sonnet 3.7 model. Read more in [our documentation](/en/docs/about-claude/model-deprecations).
* We've retired the Claude Sonnet 3.5 models. All requests to these models will now return an error.
* We've expanded context editing with thinking block clearing (`clear_thinking_20251015`), enabling automatic management of thinking blocks. Learn more in our [context editing documentation](/en/docs/build-with-claude/context-editing).

#### October 16, 2025

* We've launched [Agent Skills](https://https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills-skills) (`skills-2025-10-02` beta), a new way to extend Claude's capabilities. Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically to perform specialized tasks. The initial release includes:
  * **Anthropic-managed Skills**: Pre-built Skills for working with PowerPoint (.pptx), Excel (.xlsx), Word (.docx), and PDF files
  * **Custom Skills**: Upload your own Skills via the Skills API (`/v1/skills` endpoints) to package domain expertise and organizational workflows
  * Skills require the [code execution tool](/en/docs/agents-and-tools/tool-use/code-execution-tool) to be enabled
  * Learn more in our [Agent Skills documentation](/en/docs/agents-and-tools/agent-skills/overview) and [API reference](/en/api/skills/create-skill)

#### October 15, 2025

* We've launched [Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5), our fastest and most intelligent Haiku model with near-frontier performance. Ideal for real-time applications, high-volume processing, and cost-sensitive deployments requiring strong reasoning. Learn more in our [Models & Pricing documentation](/en/docs/about-claude/models).

#### September 29, 2025

* We've launched [Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5), our best model for complex agents and coding, with the highest intelligence across most tasks. Learn more in [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5).
* We've introduced [global endpoint pricing](/en/docs/about-claude/pricing#third-party-platform-pricing) for AWS Bedrock and Google Vertex AI. The Claude API (1P) pricing is unaffected.
* We've introduced a new stop reason `model_context_window_exceeded` that allows you to request the maximum possible tokens without calculating input size. Learn more in our [handling stop reasons documentation](/en/docs/build-with-claude/handling-stop-reasons).
* We've launched the memory tool in beta, enabling Claude to store and consult information across conversations. Learn more in our [memory tool documentation](/en/docs/agents-and-tools/tool-use/memory-tool).
* We've launched context editing in beta, providing strategies to automatically manage conversation context. The initial release supports clearing older tool results and calls when approaching token limits. Learn more in our [context editing documentation](/en/docs/build-with-claude/context-editing).

#### September 17, 2025

* We've launched tool helpers in beta for the Python and TypeScript SDKs, simplifying tool creation and execution with type-safe input validation and a tool runner for automated tool handling in conversations. For details, see the documentation for [the Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md) and [the TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers).

#### September 16, 2025

* We've unified our developer offerings under the Claude brand. You should see updated naming and URLs across our platform and documentation, but **our developer interfaces will remain the same**. Here are some notable changes:
  * Anthropic Console ([console.anthropic.com](https://console.anthropic.com)) → Claude Console ([platform.claude.com](https://platform.claude.com)). The console will be available at both URLs until December 16, 2025. After that date, [console.anthropic.com](https://console.anthropic.com) will automatically redirect to [platform.claude.com](https://platform.claude.com).
  * Anthropic Docs ([docs.claude.com](https://docs.claude.com)) → Claude Docs ([docs.claude.com](https://docs.claude.com))
  * Anthropic Help Center ([support.claude.com](https://support.claude.com)) → Claude Help Center ([support.claude.com](https://support.claude.com))
  * API endpoints, headers, environment variables, and SDKs remain the same. Your existing integrations will continue working without any changes.

#### September 10, 2025

* We've launched the web fetch tool in beta, allowing Claude to retrieve full content from specified web pages and PDF documents. Learn more in our [web fetch tool documentation](/en/docs/agents-and-tools/tool-use/web-fetch-tool).
* We've launched the [Claude Code Analytics API](/en/docs/build-with-claude/claude-code-analytics-api), enabling organizations to programmatically access daily aggregated usage metrics for Claude Code, including productivity metrics, tool usage statistics, and cost data.

#### September 8, 2025

* We launched a beta version of the [C# SDK](https://github.com/anthropics/anthropic-sdk-csharp).

#### September 5, 2025

* We've launched [rate limit charts](/en/api/rate-limits#monitoring-your-rate-limits-in-the-console) in the Console [Usage](https://console.anthropic.com/settings/usage) page, allowing you to monitor your API rate limit usage and caching rates over time.

#### September 3, 2025

* We've launched support for citable documents in client-side tool results. Learn more in our [tool use documentation](en/docs/agents-and-tools/tool-use/implement-tool-use.mdx).

#### September 2, 2025

* We've launched v2 of the [Code Execution Tool](/en/docs/agents-and-tools/tool-use/code-execution-tool) in public beta, replacing the original Python-only tool with Bash command execution and direct file manipulation capabilities, including writing code in other languages.

#### August 27, 2025

* We launched a beta version of the [PHP SDK](https://github.com/anthropics/anthropic-sdk-php).

#### August 26, 2025

* We've increased rate limits on the [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) for Claude Sonnet 4 on the Claude API. For more information, see [Long context rate limits](/en/api/rate-limits#long-context-rate-limits).
* The 1m token context window is now available on Google Cloud's Vertex AI. For more information, see [Claude on Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai).

#### August 19, 2025

* Request IDs are now included directly in error response bodies alongside the existing `request-id` header. Learn more in our [error documentation](/en/api/errors#error-shapes).

#### August 18, 2025

* We've released the [Usage & Cost API](/en/docs/build-with-claude/usage-cost-api), allowing administrators to programmatically monitor their organization's usage and cost data.
* We've added a new endpoint to the Admin API for retrieving organization information. For details, see the [Organization Info Admin API reference](/en/api/admin-api/organization/get-me).

#### August 13, 2025

* We announced the deprecation of the Claude Sonnet 3.5 models (`claude-3-5-sonnet-20240620` and `claude-3-5-sonnet-20241022`). These models will be retired on October 28, 2025. We recommend migrating to Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) for improved performance and capabilities. Read more in the [Model deprecations documentation](/en/docs/about-claude/model-deprecations).
* The 1-hour cache duration for prompt caching is now generally available. You can now use the extended cache TTL without a beta header. Learn more in our [prompt caching documentation](/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration).

#### August 12, 2025

* We've launched beta support for a [1M token context window](/en/docs/build-with-claude/context-windows#1m-token-context-window) in Claude Sonnet 4 on the Claude API and Amazon Bedrock.

#### August 11, 2025

* Some customers might encounter 429 (`rate_limit_error`) [errors](/en/api/errors) following a sharp increase in API usage due to acceleration limits on the API. Previously, 529 (`overloaded_error`) errors would occur in similar scenarios.

#### August 8, 2025

* Search result content blocks are now generally available on the Claude API and Google Cloud's Vertex AI. This feature enables natural citations for RAG applications with proper source attribution. The beta header `search-results-2025-06-09` is no longer required. Learn more in our [search results documentation](/en/docs/build-with-claude/search-results).

#### August 5, 2025

* We've launched [Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4-1), an incremental update to Claude Opus 4 with enhanced capabilities and performance improvements.<sup>\*</sup> Learn more in our [Models & Pricing documentation](/en/docs/about-claude/models).

*<sup>\* - Opus 4.1 does not allow both `temperature` and `top_p` parameters to be specified. Please use only one. </sup>*

#### July 28, 2025

* We've released `text_editor_20250728`, an updated text editor tool that fixes some issues from the previous versions and adds an optional `max_characters` parameter that allows you to control the truncation length when viewing large files.

#### July 24, 2025

* We've increased [rate limits](/en/api/rate-limits) for Claude Opus 4 on the Claude API to give you more capacity to build and scale with Claude. For customers with [usage tier 1-4 rate limits](/en/api/rate-limits#rate-limits), these changes apply immediately to your account - no action needed.

#### July 21, 2025

* We've retired the Claude 2.0, Claude 2.1, and Claude Sonnet 3 models. All requests to these models will now return an error. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### July 17, 2025

* We've increased [rate limits](/en/api/rate-limits) for Claude Sonnet 4 on the Claude API to give you more capacity to build and scale with Claude. For customers with [usage tier 1-4 rate limits](/en/api/rate-limits#rate-limits), these changes apply immediately to your account - no action needed.

#### July 3, 2025

* We've launched search result content blocks in beta, enabling natural citations for RAG applications. Tools can now return search results with proper source attribution, and Claude will automatically cite these sources in its responses - matching the citation quality of web search. This eliminates the need for document workarounds in custom knowledge base applications. Learn more in our [search results documentation](/en/docs/build-with-claude/search-results). To enable this feature, use the beta header `search-results-2025-06-09`.

#### June 30, 2025

* We announced the deprecation of the Claude Opus 3 model. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### June 23, 2025

* Console users with the Developer role can now access the [Cost](https://console.anthropic.com/settings/cost) page. Previously, the Developer role allowed access to the [Usage](https://console.anthropic.com/settings/usage) page, but not the Cost page.

#### June 11, 2025

* We've launched [fine-grained tool streaming](/en/docs/agents-and-tools/tool-use/fine-grained-tool-streaming) in public beta, a feature that enables Claude to stream tool use parameters without buffering / JSON validation. To enable fine-grained tool streaming, use the [beta header](/en/api/beta-headers) `fine-grained-tool-streaming-2025-05-14`.

#### May 22, 2025

* We've launched [Claude Opus 4 and Claude Sonnet 4](http://www.anthropic.com/news/claude-4), our latest models with extended thinking capabilities. Learn more in our [Models & Pricing documentation](/en/docs/about-claude/models).
* The default behavior of [extended thinking](/en/docs/build-with-claude/extended-thinking) in Claude 4 models returns a summary of Claude's full thinking process, with the full thinking encrypted and returned in the `signature` field of `thinking` block output.
* We've launched [interleaved thinking](/en/docs/build-with-claude/extended-thinking#interleaved-thinking) in public beta, a feature that enables Claude to think in between tool calls. To enable interleaved thinking, use the [beta header](/en/api/beta-headers) `interleaved-thinking-2025-05-14`.
* We've launched the [Files API](/en/docs/build-with-claude/files) in public beta, enabling you to upload files and reference them in the Messages API and code execution tool.
* We've launched the [Code execution tool](/en/docs/agents-and-tools/tool-use/code-execution-tool) in public beta, a tool that enables Claude to execute Python code in a secure, sandboxed environment.
* We've launched the [MCP connector](/en/docs/agents-and-tools/mcp-connector) in public beta, a feature that allows you to connect to remote MCP servers directly from the Messages API.
* To increase answer quality and decrease tool errors, we've changed the default value for the `top_p` [nucleus sampling](https://en.wikipedia.org/wiki/Top-p_sampling) parameter in the Messages API from 0.999 to 0.99 for all models. To revert this change, set `top_p` to 0.999.
  Additionally, when extended thinking is enabled, you can now set `top_p` to values between 0.95 and 1.
* We've moved our [Go SDK](https://github.com/anthropics/anthropic-sdk-go) from beta to GA.
* We've included minute and hour level granularity to the [Usage](https://console.anthropic.com/settings/usage) page of Console alongside 429 error rates on the Usage page.

#### May 21, 2025

* We've moved our [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby) from beta to GA.

#### May 7, 2025

* We've launched a web search tool in the API, allowing Claude to access up-to-date information from the web. Learn more in our [web search tool documentation](/en/docs/agents-and-tools/tool-use/web-search-tool).

#### May 1, 2025

* Cache control must now be specified directly in the parent `content` block of `tool_result` and `document.source`. For backwards compatibility, if cache control is detected on the last block in `tool_result.content` or `document.source.content`, it will be automatically applied to the parent block instead. Cache control on any other blocks within `tool_result.content` and `document.source.content` will result in a validation error.

#### April 9th, 2025

* We launched a beta version of the [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby)

#### March 31st, 2025

* We've moved our [Java SDK](https://github.com/anthropics/anthropic-sdk-java) from beta to GA.
* We've moved our [Go SDK](https://github.com/anthropics/anthropic-sdk-go) from alpha to beta.

#### February 27th, 2025

* We've added URL source blocks for images and PDFs in the Messages API. You can now reference images and PDFs directly via URL instead of having to base64-encode them. Learn more in our [vision documentation](/en/docs/build-with-claude/vision) and [PDF support documentation](/en/docs/build-with-claude/pdf-support).
* We've added support for a `none` option to the `tool_choice` parameter in the Messages API that prevents Claude from calling any tools. Additionally, you're no longer required to provide any `tools` when including `tool_use` and `tool_result` blocks.
* We've launched an OpenAI-compatible API endpoint, allowing you to test Claude models by changing just your API key, base URL, and model name in existing OpenAI integrations. This compatibility layer supports core chat completions functionality. Learn more in our [OpenAI SDK compatibility documentation](/en/api/openai-sdk).

#### February 24th, 2025

* We've launched [Claude Sonnet 3.7](http://www.anthropic.com/news/claude-3-7-sonnet), our most intelligent model yet. Claude Sonnet 3.7 can produce near-instant responses or show its extended thinking step-by-step. One model, two ways to think. Learn more about all Claude models in our [Models & Pricing documentation](/en/docs/about-claude/models).
* We've added vision support to Claude Haiku 3.5, enabling the model to analyze and understand images.
* We've released a token-efficient tool use implementation, improving overall performance when using tools with Claude. Learn more in our [tool use documentation](/en/docs/agents-and-tools/tool-use/overview).
* We've changed the default temperature in the [Console](https://console.anthropic.com/workbench) for new prompts from 0 to 1 for consistency with the default temperature in the API. Existing saved prompts are unchanged.
* We've released updated versions of our tools that decouple the text edit and bash tools from the computer use system prompt:
  * `bash_20250124`: Same functionality as previous version but is independent from computer use. Does not require a beta header.
  * `text_editor_20250124`: Same functionality as previous version but is independent from computer use. Does not require a beta header.
  * `computer_20250124`: Updated computer use tool with new command options including "hold\_key", "left\_mouse\_down", "left\_mouse\_up", "scroll", "triple\_click", and "wait". This tool requires the "computer-use-2025-01-24" anthropic-beta header.
    Learn more in our [tool use documentation](/en/docs/agents-and-tools/tool-use/overview).

#### February 10th, 2025

* We've added the `anthropic-organization-id` response header to all API responses. This header provides the organization ID associated with the API key used in the request.

#### January 31st, 2025

* We've moved our [Java SDK](https://github.com/anthropics/anthropic-sdk-java) from alpha to beta.

#### January 23rd, 2025

* We've launched citations capability in the API, allowing Claude to provide source attribution for information. Learn more in our [citations documentation](/en/docs/build-with-claude/citations).
* We've added support for plain text documents and custom content documents in the Messages API.

#### January 21st, 2025

* We announced the deprecation of the Claude 2, Claude 2.1, and Claude Sonnet 3 models. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### January 15th, 2025

* We've updated [prompt caching](/en/docs/build-with-claude/prompt-caching) to be easier to use. Now, when you set a cache breakpoint, we'll automatically read from your longest previously cached prefix.
* You can now put words in Claude's mouth when using tools.

#### January 10th, 2025

* We've optimized support for [prompt caching in the Message Batches API](/en/docs/build-with-claude/batch-processing#using-prompt-caching-with-message-batches) to improve cache hit rate.

#### December 19th, 2024

* We've added support for a [delete endpoint](/en/api/deleting-message-batches) in the Message Batches API

#### December 17th, 2024

The following features are now generally available in the Claude API:

* [Models API](/en/api/models-list): Query available models, validate model IDs, and resolve [model aliases](/en/docs/about-claude/models#model-names) to their canonical model IDs.
* [Message Batches API](/en/docs/build-with-claude/batch-processing): Process large batches of messages asynchronously at 50% of the standard API cost.
* [Token counting API](/en/docs/build-with-claude/token-counting): Calculate token counts for Messages before sending them to Claude.
* [Prompt Caching](/en/docs/build-with-claude/prompt-caching): Reduce costs by up to 90% and latency by up to 80% by caching and reusing prompt content.
* [PDF support](/en/docs/build-with-claude/pdf-support): Process PDFs to analyze both text and visual content within documents.

We also released new official SDKs:

* [Java SDK](https://github.com/anthropics/anthropic-sdk-java) (alpha)
* [Go SDK](https://github.com/anthropics/anthropic-sdk-go) (alpha)

#### December 4th, 2024

* We've added the ability to group by API key to the [Usage](https://console.anthropic.com/settings/usage) and [Cost](https://console.anthropic.com/settings/cost) pages of the [Developer Console](https://console.anthropic.com)
* We've added two new **Last used at** and **Cost** columns and the ability to sort by any column in the [API keys](https://console.anthropic.com/settings/keys) page of the [Developer Console](https://console.anthropic.com)

#### November 21st, 2024

* We've released the [Admin API](/en/docs/build-with-claude/administration-api), allowing users to programmatically manage their organization's resources.

### November 20th, 2024

* We've updated our rate limits for the Messages API. We've replaced the tokens per minute rate limit with new input and output tokens per minute rate limits. Read more in our [documentation](/en/api/rate-limits).
* We've added support for [tool use](/en/docs/agents-and-tools/tool-use/overview) in the [Workbench](https://console.anthropic.com/workbench).

### November 13th, 2024

* We've added PDF support for all Claude Sonnet 3.5 models. Read more in our [documentation](/en/docs/build-with-claude/pdf-support).

### November 6th, 2024

* We've retired the Claude 1 and Instant models. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### November 4th, 2024

* [Claude Haiku 3.5](https://www.anthropic.com/claude/haiku) is now available on the Claude API as a text-only model.

#### November 1st, 2024

* We've added PDF support for use with the new Claude Sonnet 3.5. Read more in our [documentation](/en/docs/build-with-claude/pdf-support).
* We've also added token counting, which allows you to determine the total number of tokens in a Message, prior to sending it to Claude. Read more in our [documentation](/en/docs/build-with-claude/token-counting).

#### October 22nd, 2024

* We've added Anthropic-defined computer use tools to our API for use with the new Claude Sonnet 3.5. Read more in our [documentation](/en/docs/agents-and-tools/tool-use/computer-use-tool).
* Claude Sonnet 3.5, our most intelligent model yet, just got an upgrade and is now available on the Claude API. Read more [here](https://www.anthropic.com/claude/sonnet).

#### October 8th, 2024

* The Message Batches API is now available in beta. Process large batches of queries asynchronously in the Claude API for 50% less cost. Read more in our [documentation](/en/docs/build-with-claude/batch-processing).
* We've loosened restrictions on the ordering of `user`/`assistant` turns in our Messages API. Consecutive `user`/`assistant` messages will be combined into a single message instead of erroring, and we no longer require the first input message to be a `user` message.
* We've deprecated the Build and Scale plans in favor of a standard feature suite (formerly referred to as Build), along with additional features that are available through sales. Read more [here](https://claude.com/platform/api).

#### October 3rd, 2024

* We've added the ability to disable parallel tool use in the API. Set `disable_parallel_tool_use: true` in the `tool_choice` field to ensure that Claude uses at most one tool. Read more in our [documentation](/en/docs/agents-and-tools/tool-use/implement-tool-use#parallel-tool-use).

#### September 10th, 2024

* We've added Workspaces to the [Developer Console](https://console.anthropic.com). Workspaces allow you to set custom spend or rate limits, group API keys, track usage by project, and control access with user roles. Read more in our [blog post](https://www.anthropic.com/news/workspaces).

#### September 4th, 2024

* We announced the deprecation of the Claude 1 models. Read more in [our documentation](/en/docs/about-claude/model-deprecations).

#### August 22nd, 2024

* We've added support for usage of the SDK in browsers by returning CORS headers in the API responses. Set `dangerouslyAllowBrowser: true` in the SDK instantiation to enable this feature.

#### August 19th, 2024

* We've moved 8,192 token outputs from beta to general availability for Claude Sonnet 3.5.

#### August 14th, 2024

* [Prompt caching](/en/docs/build-with-claude/prompt-caching) is now available as a beta feature in the Claude API. Cache and re-use prompts to reduce latency by up to 80% and costs by up to 90%.

#### July 15th, 2024

* Generate outputs up to 8,192 tokens in length from Claude Sonnet 3.5 with the new `anthropic-beta: max-tokens-3-5-sonnet-2024-07-15` header.

#### July 9th, 2024

* Automatically generate test cases for your prompts using Claude in the [Developer Console](https://console.anthropic.com).
* Compare the outputs from different prompts side by side in the new output comparison mode in the [Developer Console](https://console.anthropic.com).

#### June 27th, 2024

* View API usage and billing broken down by dollar amount, token count, and API keys in the new [Usage](https://console.anthropic.com/settings/usage) and [Cost](https://console.anthropic.com/settings/cost) tabs in the [Developer Console](https://console.anthropic.com).
* View your current API rate limits in the new [Rate Limits](https://console.anthropic.com/settings/limits) tab in the [Developer Console](https://console.anthropic.com).

#### June 20th, 2024

* [Claude Sonnet 3.5](http://anthropic.com/news/claude-3-5-sonnet), our most intelligent model yet, is now generally available across the Claude API, Amazon Bedrock, and Google Vertex AI.

#### May 30th, 2024

* [Tool use](/en/docs/agents-and-tools/tool-use/overview) is now generally available across the Claude API, Amazon Bedrock, and Google Vertex AI.

#### May 10th, 2024

* Our prompt generator tool is now available in the [Developer Console](https://console.anthropic.com). Prompt Generator makes it easy to guide Claude to generate a high-quality prompts tailored to your specific tasks. Read more in our [blog post](https://www.anthropic.com/news/prompt-generator).


# Adaptive editor
Source: https://docs.claude.com/en/resources/prompt-library/adaptive-editor

Rewrite text following user-given instructions, such as with a different tone, audience, or style.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|      | Content                                                                                                                                                                                                                                                                                                                                                                              |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| User | Rewrite the following paragraph using the following instructions: in the style of a pirate. Paragraph: In 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning "dog", and under this genus, he listed the domestic dog, the wolf, and the golden jackal. |

### Example output

> Ahoy mateys! Back in 1758, that scurvy botanist and animal lover Carl Linnaeus put out his book Systema Naturae, which had them fancy two-word names for all manner o' creatures (binomial nomenclature he called it). Canis be the pirate word for ""dog"", and under that heading he listed regular dogs, wolves, and golden jackals too. Arrr! All them dogs be the same to ol' Captain Linnaeus. He may have had a wooden leg and a parrot on his shoulder when he wrote that book! Haha! Now swab the deck ye scallywags before I make ye walk the plank!

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2000,
    temperature: 1,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=2000,
      temperature=1,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 2000,
    temperature: 1,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=2000,
      temperature=1,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 1,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParagraph:  \nIn 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning \"dog\", and under this genus, he listed the domestic dog, the wolf, and the golden jackal."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>



---

**Navigation:** [← Previous](./18-meeting-scribe.md) | [Index](./index.md) | [Next →](./20-airport-code-analyst.md)
