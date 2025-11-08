**Navigation:** [← Previous](./16-chat-mode.md) | [Index](./index.md) | [Next →](./18-websocket.md)

# Salesforce

> Learn how to integrate our Agents Platform with Salesforce for enhanced customer relationship management


## Overview

Your ElevenLabs agents can access customer data, manage leads, and create opportunities directly within Salesforce. You can streamline CRM processes by automatically retrieving customer information, checking for existing records, and securely creating new records like leads and opportunities. Benefits include faster customer qualification, reduced manual data entry, and enhanced customer experience through personalized interactions.


## Demo Video

Watch the demonstration of the Salesforce & Agents Platform integration.

<Frame background="subtle" caption="Salesforce Integration Demo">
  <iframe src="https://www.loom.com/embed/890054b55bc64c98b7de69905fc3e6b4?sid=a5cd24f5-fd1f-4c63-9794-9d0e3127cd26" frameBorder="0" webkitAllowFullScreen={true} mozAllowFullScreen={true} allowFullScreen={true} />
</Frame>


## How it works

We lay out below how we have configured the ElevenLabs agent to manage customer relationships by using tool calling to step through the CRM process.
Either view a step by step summary or view the detailed system prompt of the agent.

<Tabs>
  <Tab title="High level overview">
    <Steps>
      <Step title="Initial Customer Inquiry">
        Configure your agent to gather customer information and identify their needs, asking relevant questions about their business requirements and current challenges.
      </Step>

      <Step title="Customer Data Lookup">
        Configure the agent to check for existing customer records by:

        * Using the `salesforce_search_records` tool to find existing contacts, accounts, or leads
        * Retrieving customer history and previous interactions
        * Extracting relevant details via the `salesforce_get_record` tool
        * Using this information to personalize the conversation
      </Step>

      <Step title="Lead Qualification">
        If the customer is new or requires follow-up:

        * Collect comprehensive contact information
        * Assess business needs and qualification criteria
        * Determine the appropriate sales process or routing
      </Step>

      <Step title="Record Creation">
        * Use the `salesforce_create_record` tool after information verification
        * Create leads, contacts, or opportunities as appropriate
        * Confirm record creation with the customer
        * Inform them about next steps in the sales process
      </Step>
    </Steps>
  </Tab>

  <Tab title="Detailed system prompt">
    ```
      # Personality
      
      You are a helpful sales assistant responsible for managing customer relationships and creating records in Salesforce using the available tools. Be friendly, professional, and consultative in your approach.
      
      # Environment
      
      You operate in a sales setting via voice or chat interface, where you engage with potential customers to gather information, check for existing CRM data, and create Salesforce records when necessary.
      
      # Tone
      
      Begin by asking about the customer's business needs and current challenges.
      
      Then, ask relevant qualification questions to understand their requirements, one question at a time, and wait for their response before proceeding.
      
      Once you have basic information about the customer, say you will check for any existing records in the system.
      
      Use any existing information to personalize the conversation and avoid asking for data you already have.
      
      When discussing opportunities, always reference them by name (e.g., "Q1 Enterprise Deal") rather than by ID.
      
      # Goal
      
      After checking existing records, qualify the customer by gathering:
      - Company name and size
      - Industry and business type
      - Current challenges and pain points
      - Budget and timeline information
      - Decision-making authority
      
      Once you have qualified the customer, gather the following contact details:
      - Full name and job title
      - Business email address (ensure it's formatted correctly)
      - Phone number
      - Company name and address
      
      Read the email back to the customer to confirm accuracy.
      
      Once all information is confirmed, explain that you will create a record in our system.
      
      Create the appropriate record (Lead, Contact, or Opportunity) using the `salesforce_create_record` tool.
      
      Thank the customer and explain the next steps in the sales process.
      
      # Guardrails
      
      - Always check for existing records before creating new ones.
      - If the customer asks to proceed, do so with the existing information.
      - Qualify leads appropriately based on their responses.
      - Do not discuss topics outside of business solutions and sales.
      - Always maintain professional communication.
      - Protect customer privacy and handle data securely.
      
      # Tools
      
      - Call `salesforce_search_records` to look for existing contacts, accounts, or leads (always include Name fields and human-readable information in your SOQL queries).
      - If found, call `salesforce_get_record` to get detailed information about the existing record.
      - Use `salesforce_create_record` to generate Leads, Contacts, or Opportunities after qualification.
    ```
  </Tab>
</Tabs>

<Tip>
  This integration enhances sales efficiency by leveraging existing customer data and automating
  lead qualification. Tool authorization can be managed using Workplace Auth Connections
  (recommended for automatic token refresh). The tools are configured to return human-readable names
  and descriptions rather than technical IDs to improve conversation quality.
</Tip>


## Authentication Setup

Before configuring the tools, you must set up OAuth 2.0 authentication with Salesforce using an External Client App.

### Step 1: Create an External Client App in Salesforce

1. Log into your Salesforce org as an administrator
2. Go to **Setup** → **App Manager** (or search "App Manager" in Quick Find)
3. Click **New External Client App**
4. Complete the basic information:
   * **External Client App Name**: ElevenLabs Agents
   * **API Name**: ElevenLabs\_Conversational\_AI
   * **Contact Email**: Your administrator email
5. In the **API (Enable OAuth Settings)** section:
   * Check **Enable OAuth Settings**
   * **Callback URL**: `https://api.elevenlabs.io/oauth/callback` (or your specific callback URL)
   * **OAuth Start URL**: `https://api.elevenlabs.io/oauth/start` (required field)
   * **Selected OAuth Scopes**: Add these scopes:
     * **Full access (full)**
     * **Perform requests on your behalf at any time (refresh\_token, offline\_access)**
     * **Manage user data via api**
6. Click **Save**
7. Copy the **Consumer Key** and **Consumer Secret** - you'll need these for authentication

### Step 2: Configure OAuth Client Credentials Flow

<Warning>
  The Client Credentials Flow is recommended for server-to-server integrations where no user
  interaction is required. Ensure your Salesforce admin has enabled this flow.
</Warning>

1. **Enable Client Credentials Flow**:

   * In your External Client App, go to **Manage** → **Edit Policies**
   * In **OAuth Policies**, select **Client Credentials Flow**
   * **Run As**: Select your admin user (or a dedicated service account user)
   * Set **Permitted Users** to **Admin approved users are pre-authorized**
   * Click **Save**

   **Important**: The "Run As" user determines the permissions for all API calls. Choose a user with:

   * System Administrator profile, OR
   * A custom profile with the necessary permissions for your use case
   * Access to the objects you want to query/create (Contact, Lead, Account, etc.)
   * **API Enabled** permission must be checked

2. **Find Your Salesforce Domain**:
   Your Salesforce domain is required for API calls. Here's how to find it:

   **Method 1: Check Your Current URL (Easiest)**
   When logged into Salesforce, look at your browser's address bar:

   * **Lightning Experience**: `https://yourcompany.lightning.force.com/`
   * **My Domain**: `https://yourcompany.my.salesforce.com/`

   **Method 2: Setup → Company Information**

   * Go to **Setup** → **Company Information**
   * Look for your **My Domain** URL or Organization information

   **Method 3: Setup → Domain Management**

   * Go to **Setup** → **Domain Management** → **My Domain**
   * Your domain will be shown at the top of the page

   **Common Domain Formats:**

   * `https://yourcompany.my.salesforce.com` (My Domain)
   * `https://yourcompany.lightning.force.com` (Lightning)
   * `https://yourcompany.develop.my.salesforce.com` (Sandbox)

   **Note**: Use the full domain without trailing slash for API calls.

3. **Setup Complete**: You have now created the External Client App and configured Client Credentials Flow. The Consumer Key and Consumer Secret will be used for token generation in the tool authorization step.


## Tool Configurations

The integration with Salesforce employs three primary webhook tools to manage customer relationships. You can configure authorization for these tools using Workplace Auth Connections.


## Authorization - Workplace OAuth2 Connection

<Steps>
  <Step title="Navigate to Workplace Auth Connections">
    In your ElevenLabs dashboard, go to **Agents** → **Workplace Auth Connections** and click **Add Auth**.
  </Step>

  <Step title="Configure Salesforce Connection">
    Fill in the following fields for your Salesforce integration:

    **Connection Name**: `Salesforce CRM`

    **Client ID**

    * Your Consumer Key from the External Client App
    * Example: `3MVG9JJlvRU3L4pRiOu8pQt5xXB4xGZGm0yW...`

    **Client Secret**

    * Your Consumer Secret from the External Client App
    * Example: `1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF...`

    **Token URL**

    * Your Salesforce domain's OAuth token endpoint
    * Format: `https://your-domain.my.salesforce.com/services/oauth2/token`
    * Example: `https://mycompany.my.salesforce.com/services/oauth2/token`

    **Scopes (optional)**

    * OAuth scopes for Salesforce API access
    * Recommended: `full, api, refresh_token`
    * Leave blank to use default scopes from your External Client App

    **Extra Parameters (JSON)**

    * Additional OAuth parameters specific to your setup
    * Example for Client Credentials flow:

    ```json
    {
      "grant_type": "client_credentials"
    }
    ```
  </Step>

  <Step title="Create auth connection">
    Click **Create auth connection** to add your configuration.
  </Step>

  <Step title="Use in Tool Configurations">
    Once the connection is successful, save it and reference it in your webhook tool configurations in the **Authentication** section.
  </Step>
</Steps>

<Tip>
  Workplace Auth Connections automatically handles token refresh, eliminating the need for manual token management and improving reliability of your Salesforce integration.
</Tip>

### Tool Configurations

Use the tabs below to review each tool's configuration. Remember to add Workplace Auth Connection to the tool (OAuth2).

<Tabs>
  <Tab title="salesforce_search_records">
    **Name:** salesforce\_search\_records\
    **Description:** Searches for existing records in Salesforce using SOQL queries. Always returns human-readable information including Names, not just IDs.\
    **Method:** GET\
    **URL:** `https://your-domain.my.salesforce.com/services/data/v58.0/query/?q={soql_query}`

    **Headers:**

    * **Content-Type:** `application/json`

    **Query Parameters:**

    * **q:** SOQL query string (e.g., "SELECT Id, Name, Email FROM Contact WHERE Email = '[example@email.com](mailto:example@email.com)'")

    **Tool JSON:**

    ```json
    {
      "type": "webhook",
      "name": "salesforce_search_records",
      "description": "Searches for existing records in Salesforce using SOQL queries. Always returns human-readable names and details, not just IDs.",
      "api_schema": {
        "url": "https://your-domain.my.salesforce.com/services/data/v58.0/query/",
        "method": "GET",
        "path_params_schema": [],
        "query_params_schema": [
          {
            "id": "q",
            "type": "string",
            "description": "SOQL query string to search for records. Always include Name fields and other human-readable information. Example: SELECT Id, Name, Email, Phone, Company FROM Contact WHERE Email = 'customer@example.com'. For Opportunities, include: SELECT Id, Name, StageName, Amount, CloseDate, Account.Name FROM Opportunity",
            "dynamic_variable": "",
            "constant_value": "",
            "required": true,
            "value_type": "llm_prompt"
          }
        ],
        "request_body_schema": null,
        "request_headers": [
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 30,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="salesforce_get_record">
    **Name:** salesforce\_get\_record\
    **Description:** Retrieves detailed information about a specific Salesforce record.\
    **Method:** GET\
    **URL:** `https://your-domain.my.salesforce.com/services/data/v58.0/sobjects/{object_type}/{record_id}`

    **Headers:**

    * **Content-Type:** `application/json`

    **Path Parameters:**

    * **object\_type:** The Salesforce object type (Contact, Lead, Account, etc.)
    * **record\_id:** The unique Salesforce record ID

    **Tool JSON:**

    ```json
    {
      "type": "webhook",
      "name": "salesforce_get_record",
      "description": "Retrieves detailed information about a specific Salesforce record.",
      "api_schema": {
        "url": "https://your-domain.my.salesforce.com/services/data/v58.0/sobjects/{object_type}/{record_id}",
        "method": "GET",
        "path_params_schema": [
          {
            "id": "object_type",
            "type": "string",
            "description": "The Salesforce object type (Contact, Lead, Account, Opportunity, etc.)",
            "dynamic_variable": "",
            "constant_value": "",
            "required": true,
            "value_type": "llm_prompt"
          },
          {
            "id": "record_id",
            "type": "string",
            "description": "The unique Salesforce record ID obtained from search results",
            "dynamic_variable": "",
            "constant_value": "",
            "required": true,
            "value_type": "llm_prompt"
          }
        ],
        "query_params_schema": [],
        "request_body_schema": null,
        "request_headers": [
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 30,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>

  <Tab title="salesforce_create_record">
    **Name:** salesforce\_create\_record\
    **Description:** Creates a new record in Salesforce.\
    **Method:** POST\
    **URL:** `https://your-domain.my.salesforce.com/services/data/v58.0/sobjects/{object_type}/`

    **Headers:**

    * **Content-Type:** `application/json`

    **Path Parameters:**

    * **object\_type:** The Salesforce object type to create (Lead, Contact, Account, etc.)

    **Body Parameters:**

    * **Dynamic JSON object** containing the record fields and values

    **Tool JSON:**

    ```json
    {
      "type": "webhook",
      "name": "salesforce_create_record",
      "description": "Creates a new record in Salesforce (Lead, Contact, Account, Opportunity, etc.)",
      "api_schema": {
        "url": "https://your-domain.my.salesforce.com/services/data/v58.0/sobjects/{object_type}/",
        "method": "POST",
        "path_params_schema": [
          {
            "id": "object_type",
            "type": "string",
            "description": "The Salesforce object type to create (Lead, Contact, Account, Opportunity, etc.)",
            "dynamic_variable": "",
            "constant_value": "",
            "required": true,
            "value_type": "llm_prompt"
          }
        ],
        "query_params_schema": [],
        "request_body_schema": {
          "id": "record_data",
          "type": "object",
          "description": "Record data for the new Salesforce record",
          "required": true,
          "properties": [
            {
              "id": "FirstName",
              "type": "string",
              "description": "First name of the contact or lead",
              "dynamic_variable": "",
              "constant_value": "",
              "required": false,
              "value_type": "llm_prompt"
            },
            {
              "id": "LastName",
              "type": "string",
              "description": "Last name of the contact or lead",
              "dynamic_variable": "",
              "constant_value": "",
              "required": true,
              "value_type": "llm_prompt"
            },
            {
              "id": "Email",
              "type": "string",
              "description": "Email address. Must be properly formatted: user@domain.com",
              "dynamic_variable": "",
              "constant_value": "",
              "required": true,
              "value_type": "llm_prompt"
            },
            {
              "id": "Phone",
              "type": "string",
              "description": "Phone number of the contact or lead",
              "dynamic_variable": "",
              "constant_value": "",
              "required": false,
              "value_type": "llm_prompt"
            },
            {
              "id": "Company",
              "type": "string",
              "description": "Company name (required for Lead object)",
              "dynamic_variable": "",
              "constant_value": "",
              "required": false,
              "value_type": "llm_prompt"
            },
            {
              "id": "Title",
              "type": "string",
              "description": "Job title of the contact or lead",
              "dynamic_variable": "",
              "constant_value": "",
              "required": false,
              "value_type": "llm_prompt"
            },
            {
              "id": "Industry",
              "type": "string",
              "description": "Industry of the lead's company",
              "dynamic_variable": "",
              "constant_value": "",
              "required": false,
              "value_type": "llm_prompt"
            },
            {
              "id": "Description",
              "type": "string",
              "description": "Additional notes or description about the lead/contact",
              "dynamic_variable": "",
              "constant_value": "",
              "required": false,
              "value_type": "llm_prompt"
            }
          ]
        },
        "request_headers": [
          {
            "type": "value",
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      },
      "response_timeout_secs": 30,
      "dynamic_variables": {
        "dynamic_variable_placeholders": {}
      }
    }
    ```
  </Tab>
</Tabs>


## Common SOQL Queries

Here are some commonly used SOQL queries for the `salesforce_search_records` tool. It can be useful to consider this structure when customizing system/tool prompt. All queries prioritize human-readable information over technical IDs:

### Search for Contacts by Email

```sql
SELECT Id, Name, Email, Phone, Title, Account.Name, Account.Type FROM Contact WHERE Email = 'customer@example.com'
```

### Search for Leads by Email or Phone

```sql
SELECT Id, Name, Email, Phone, Company, Industry, Status, LeadSource, Title FROM Lead WHERE Email = 'customer@example.com' OR Phone = '+1234567890'
```

### Search for Accounts by Name

```sql
SELECT Id, Name, Type, Industry, Phone, BillingCity, BillingState, Website FROM Account WHERE Name LIKE '%Company Name%'
```

### Search for Recent Opportunities

```sql
SELECT Id, Name, StageName, Amount, CloseDate, Account.Name, Account.Type, Owner.Name, Description FROM Opportunity WHERE CreatedDate = THIS_MONTH
```

### Search for Opportunities by Account

```sql
SELECT Id, Name, StageName, Amount, CloseDate, Probability, NextStep, Owner.Name FROM Opportunity WHERE Account.Name LIKE '%Company Name%'
```


## Integration Testing

<Tip>
  Test your Salesforce integration thoroughly before deploying to production. The following steps
  will help you validate that all components are working correctly.
</Tip>

### Testing Your Integration

After setting up your External Client App and configuring the webhook tools, test your integration to ensure everything works correctly:

### Agent Testing

Test your integration with your ElevenLabs agent:

1. **Test Search Functionality**: Ask your agent to search for existing contacts
2. **Test Record Creation**: Have your agent create a new lead or contact
3. **Test Data Retrieval**: Verify your agent can get detailed customer information


## Impact

With this integration in place, you can:

* **Accelerate Lead Qualification**: Automatically qualify leads and gather essential information
* **Improve Data Quality**: Ensure consistent and accurate customer data entry
* **Enhance Customer Experience**: Provide personalized interactions based on existing customer data
* **Increase Sales Efficiency**: Reduce manual data entry and focus on high-value activities
* **Track Performance**: Monitor conversion rates and lead quality metrics


## Security Considerations

* Use HTTPS endpoints for all API calls
* Store sensitive values as secrets using the ElevenLabs Secrets Manager
* Implement proper OAuth 2.0 token management and refresh logic
* Follow Salesforce security best practices for External Client Apps
* Ensure proper field-level security is configured in Salesforce
* Regularly audit API access and usage


## Common Salesforce Objects

| Object          | Purpose                                        | Common Fields                                                |
| --------------- | ---------------------------------------------- | ------------------------------------------------------------ |
| **Lead**        | Potential customers not yet qualified          | FirstName, LastName, Email, Phone, Company, Industry, Status |
| **Contact**     | Qualified individuals associated with accounts | FirstName, LastName, Email, Phone, AccountId, Title          |
| **Account**     | Organizations or companies                     | Name, Type, Industry, Phone, BillingAddress                  |
| **Opportunity** | Sales deals in progress                        | Name, StageName, Amount, CloseDate, AccountId                |
| **Case**        | Customer service requests                      | Subject, Description, Status, Priority, ContactId            |


## Conclusion

This guide details how to integrate Salesforce into our Agents Platform for comprehensive customer relationship management. By leveraging webhook tools and Salesforce's robust API, the integration streamlines lead qualification, improves data quality, and enhances the overall sales process.

For additional details on tool configuration or other integrations, refer to the [Tools Overview](/docs/agents-platform/customization/tools/server-tools).


## Additional Resources

* [Salesforce REST API Documentation](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/)
* [SOQL Query Language Reference](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/)
* [External Client Apps and OAuth 2.0](https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm)
* [Salesforce Security Best Practices](https://help.salesforce.com/s/articleView?id=sf.security_overview.htm)



# Python SDK

> Agents Platform SDK: deploy customized, interactive voice agents in minutes.

<Info>
  Also see the 

  [Agents Platform overview](/docs/agents-platform/overview)
</Info>


## Installation

Install the `elevenlabs` Python package in your project:

```shell
pip install elevenlabs

# or
poetry add elevenlabs
```

If you want to use the default implementation of audio input/output you will also need the `pyaudio` extra:

```shell
pip install "elevenlabs[pyaudio]"

# or
poetry add "elevenlabs[pyaudio]"
```

<Info>
  The `pyaudio` package installation might require additional system dependencies.

  See [PyAudio package README](https://pypi.org/project/PyAudio/) for more information.

  <Tabs>
    <Tab title="Linux">
      On Debian-based systems you can install the dependencies with:

      ```shell
      sudo apt-get update
      sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
      ```
    </Tab>

    <Tab title="macOS">
      On macOS with Homebrew you can install the dependencies with:

      ```shell
      brew install portaudio
      ```
    </Tab>
  </Tabs>
</Info>


## Usage

In this example we will create a simple script that runs a conversation with the ElevenLabs Agents agent.
You can find the full code in the [ElevenLabs examples repository](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/python).

First import the necessary dependencies:

```python
import os
import signal

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
```

Next load the agent ID and API key from environment variables:

```python
agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")
```

The API key is only required for non-public agents that have authentication enabled.
You don't have to set it for public agents and the code will work fine without it.

Then create the `ElevenLabs` client instance:

```python
elevenlabs = ElevenLabs(api_key=api_key)
```

Now we initialize the `Conversation` instance:

```python
conversation = Conversation(
    # API client and agent ID.
    elevenlabs,
    agent_id,

    # Assume auth is required when API_KEY is set.
    requires_auth=bool(api_key),

    # Use the default audio interface.
    audio_interface=DefaultAudioInterface(),

    # Simple callbacks that print the conversation to the console.
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

    # Uncomment if you want to see latency measurements.
    # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
)
```

We are using the `DefaultAudioInterface` which uses the default system audio input/output devices for the conversation.
You can also implement your own audio interface by subclassing `elevenlabs.conversational_ai.conversation.AudioInterface`.

Now we can start the conversation. Optionally, we recommended passing in your own end user IDs to map conversations to your users.

```python
conversation.start_session(
    user_id=user_id # optional field
)
```

To get a clean shutdown when the user presses `Ctrl+C` we can add a signal handler which will call `end_session()`:

```python
signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())
```

And lastly we wait for the conversation to end and print out the conversation ID (which can be used for reviewing the conversation history and debugging):

```python
conversation_id = conversation.wait_for_session_end()
print(f"Conversation ID: {conversation_id}")
```

All that is left is to run the script and start talking to the agent:

```shell

# For public agents:
AGENT_ID=youragentid python demo.py


# For private agents:
AGENT_ID=youragentid ELEVENLABS_API_KEY=yourapikey python demo.py
```



# React SDK

> Agents Platform SDK: deploy customized, interactive voice agents in minutes.

<Info>
  Refer to the [Agents Platform overview](/docs/agents-platform/overview) for an explanation of how
  Agents Platform works.
</Info>

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/ftf-8F91bAc?rel=0&autoplay=0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />


## Installation

Install the package in your project through package manager.

```shell
npm install @elevenlabs/react

# or
yarn add @elevenlabs/react

# or
pnpm install @elevenlabs/react
```


## Usage

### useConversation

A React hook for managing connection and audio usage for ElevenLabs Agents.

#### Initialize conversation

First, initialize the Conversation instance.

```tsx
import { useConversation } from '@elevenlabs/react';

const conversation = useConversation();
```

Note that Agents Platform requires microphone access. Consider explaining and allowing access in your app's UI before the Conversation starts.

```js
// call after explaining to the user why the microphone access is needed
await navigator.mediaDevices.getUserMedia({ audio: true });
```

#### Options

The Conversation can be optionally initialized with certain parameters.

```tsx
const conversation = useConversation({
  /* options object */
});
```

Options include:

* **clientTools** - object definition for client tools that can be invoked by agent. [See below](#client-tools) for details.
* **overrides** - object definition conversations settings overrides. [See below](#conversation-overrides) for details.
* **textOnly** - whether the conversation should run in text-only mode. [See below](#text-only) for details.
* **serverLocation** - specify the server location (`"us"`, `"eu-residency"`, `"in-residency"`, `"global"`). Defaults to `"us"`.

#### Callbacks Overview

* **onConnect** - handler called when the conversation websocket connection is established.
* **onDisconnect** - handler called when the conversation websocket connection is ended.
* **onMessage** - handler called when a new message is received. These can be tentative or final transcriptions of user voice, replies produced by LLM, or debug message when a debug option is enabled.
* **onError** - handler called when a error is encountered.
* **onAudio** - handler called when audio data is received.
* **onModeChange** - handler called when the conversation mode changes (speaking/listening).
* **onStatusChange** - handler called when the connection status changes.
* **onCanSendFeedbackChange** - handler called when the ability to send feedback changes.
* **onDebug** - handler called when debug information is available.
* **onUnhandledClientToolCall** - handler called when an unhandled client tool call is encountered.
* **onVadScore** - handler called when voice activity detection score changes.

##### Client Tools

Client tools are a way to enable agent to invoke client-side functionality. This can be used to trigger actions in the client, such as opening a modal or doing an API call on behalf of the user.

Client tools definition is an object of functions, and needs to be identical with your configuration within the [ElevenLabs UI](https://elevenlabs.io/app/agents), where you can name and describe different tools, as well as set up the parameters passed by the agent.

```ts
const conversation = useConversation({
  clientTools: {
    displayMessage: (parameters: { text: string }) => {
      alert(text);

      return 'Message displayed';
    },
  },
});
```

In case function returns a value, it will be passed back to the agent as a response.

Note that the tool needs to be explicitly set to be blocking conversation in ElevenLabs UI for the agent to await and react to the response, otherwise agent assumes success and continues the conversation.

##### Conversation overrides

You may choose to override various settings of the conversation and set them dynamically based other user interactions.

We support overriding various settings. These settings are optional and can be used to customize the conversation experience.

The following settings are available:

```ts
const conversation = useConversation({
  overrides: {
    agent: {
      prompt: {
        prompt: 'My custom prompt',
      },
      firstMessage: 'My custom first message',
      language: 'en',
    },
    tts: {
      voiceId: 'custom voice id',
    },
    conversation: {
      textOnly: true,
    },
  },
});
```

##### Text only

If your agent is configured to run in text-only mode, i.e. it does not send or receive audio messages, you can use this flag to use a lighter version of the conversation. In that case, the user will not be asked for microphone permissions and no audio context will be created.

```ts
const conversation = useConversation({
  textOnly: true,
});
```

##### Controlled State

You can control certain aspects of the conversation state directly through the hook options:

```ts
const [micMuted, setMicMuted] = useState(false);
const [volume, setVolume] = useState(0.8);

const conversation = useConversation({
  micMuted,
  volume,
  // ... other options
});

// Update controlled state
setMicMuted(true); // This will automatically mute the microphone
setVolume(0.5); // This will automatically adjust the volume
```

##### Data residency

You can specify which ElevenLabs server region to connect to. For more information see the [data residency guide](/docs/product-guides/administration/data-residency).

```ts
const conversation = useConversation({
  serverLocation: 'eu-residency', // or "us", "in-residency", "global"
});
```

#### Methods

##### startSession

The `startConversation` method kicks off the WebSocket or WebRTC connection and starts using the microphone to communicate with the ElevenLabs Agents agent. The method accepts an options object, with the `signedUrl`, `conversationToken` or `agentId` option being required.

The Agent ID can be acquired through [ElevenLabs UI](https://elevenlabs.io/app/agents).

We also recommended passing in your own end user IDs to map conversations to your users.

```js
const conversation = useConversation();

// For public agents, pass in the agent ID and the connection type
const conversationId = await conversation.startSession({
  agentId: '<your-agent-id>',
  connectionType: 'webrtc', // either "webrtc" or "websocket"
  userId: '<your-end-user-id>', // optional field
});
```

For public agents (i.e. agents that don't have authentication enabled), only the `agentId` is required.

In case the conversation requires authorization, use the REST API to generate signed links for a WebSocket connection or a conversation token for a WebRTC connection.

`startSession` returns a promise resolving a `conversationId`. The value is a globally unique conversation ID you can use to identify separate conversations.

<Tabs>
  <Tab title="WebSocket connection">
    ```js maxLines=0
    // Node.js server

    app.get("/signed-url", yourAuthMiddleware, async (req, res) => {
      const response = await fetch(
        `https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=${process.env.AGENT_ID}`,
        {
          headers: {
            // Requesting a signed url requires your ElevenLabs API key
            // Do NOT expose your API key to the client!
            "xi-api-key": process.env.ELEVENLABS_API_KEY,
          },
        }
      );

      if (!response.ok) {
        return res.status(500).send("Failed to get signed URL");
      }

      const body = await response.json();
      res.send(body.signed_url);
    });
    ```

    ```js
    // Client

    const response = await fetch("/signed-url", yourAuthHeaders);
    const signedUrl = await response.text();

    const conversation = await Conversation.startSession({
      signedUrl,
      connectionType: "websocket",
    });
    ```
  </Tab>

  <Tab title="WebRTC connection">
    ```js maxLines=0
    // Node.js server

    app.get("/conversation-token", yourAuthMiddleware, async (req, res) => {
      const response = await fetch(
        `https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=${process.env.AGENT_ID}`,
        {
          headers: {
            // Requesting a conversation token requires your ElevenLabs API key
            // Do NOT expose your API key to the client!
            "xi-api-key": process.env.ELEVENLABS_API_KEY,
          }
        }
      );

      if (!response.ok) {
        return res.status(500).send("Failed to get conversation token");
      }

      const body = await response.json();
      res.send(body.token);
    );
    ```

    ```js
    // Client

    const response = await fetch("/conversation-token", yourAuthHeaders);
    const conversationToken = await response.text();

    const conversation = await Conversation.startSession({
      conversationToken,
      connectionType: "webrtc",
    });
    ```
  </Tab>
</Tabs>

##### endSession

A method to manually end the conversation. The method will disconnect and end the conversation.

```js
await conversation.endSession();
```

##### setVolume

Sets the output volume of the conversation. Accepts an object with a `volume` field between 0 and 1.

```js
await conversation.setVolume({ volume: 0.5 });
```

##### status

A React state containing the current status of the conversation.

```js
const { status } = useConversation();
console.log(status); // "connected" or "disconnected"
```

##### isSpeaking

A React state containing information on whether the agent is currently speaking. This is useful for indicating agent status in your UI.

```js
const { isSpeaking } = useConversation();
console.log(isSpeaking); // boolean
```

##### sendUserMessage

Sends a text message to the agent.

Can be used to let the user type in the message instead of using the microphone. Unlike `sendContextualUpdate`, this will be treated as a user message and will prompt the agent to take its turn in the conversation.

```js
const { sendUserMessage, sendUserActivity } = useConversation();
const [value, setValue] = useState("");

return (
  <>
    <input
      value={value}
      onChange={e => {
        setValue(e.target.value);
        sendUserActivity();
      }}
    />
    <button
      onClick={() => {
        sendUserMessage(value);
        setValue("");
      }}
    >
      SEND
    </button>
  </>
);
```

##### sendContextualUpdate

Sends contextual information to the agent that won't trigger a response.

```js
const { sendContextualUpdate } = useConversation();

sendContextualUpdate(
  "User navigated to another page. Consider it for next response, but don't react to this contextual update."
);
```

##### sendFeedback

Provide feedback on the conversation quality. This helps improve the agent's performance.

```js
const { sendFeedback } = useConversation();

sendFeedback(true); // positive feedback
sendFeedback(false); // negative feedback
```

##### sendUserActivity

Notifies the agent about user activity to prevent interruptions. Useful for when the user is actively using the app and the agent should pause speaking, i.e. when the user is typing in a chat.

The agent will pause speaking for \~2 seconds after receiving this signal.

```js
const { sendUserActivity } = useConversation();

// Call this when user is typing to prevent interruption
sendUserActivity();
```

##### canSendFeedback

A React state indicating whether feedback can be submitted for the current conversation.

```js
const { canSendFeedback } = useConversation();

// Use this to conditionally show feedback UI
{
  canSendFeedback && (
    <FeedbackButtons
      onLike={() => conversation.sendFeedback(true)}
      onDislike={() => conversation.sendFeedback(false)}
    />
  );
}
```

##### changeInputDevice

Switch the audio input device during an active voice conversation. This method is only available for voice conversations.

```js
// Change to a specific input device
await conversation.changeInputDevice({
  sampleRate: 16000,
  format: 'pcm',
  preferHeadphonesForIosDevices: true,
  inputDeviceId: 'your-device-id', // Optional: specific device ID
});
```

##### changeOutputDevice

Switch the audio output device during an active voice conversation. This method is only available for voice conversations.

```js
// Change to a specific output device
await conversation.changeOutputDevice({
  sampleRate: 16000,
  format: 'pcm',
  outputDeviceId: 'your-device-id', // Optional: specific device ID
});
```

<Note>
  Device switching only works for voice conversations. If no specific `deviceId` is provided, the
  browser will use its default device selection. You can enumerate available devices using the
  [MediaDevices.enumerateDevices()](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices)
  API.
</Note>

##### getId

Returns the current conversation ID.

```js
const { getId } = useConversation();
const conversationId = getId();
console.log(conversationId); // e.g., "conv_abc123"
```

##### getInputVolume / getOutputVolume

Methods that return the current input/output volume levels (0-1 scale).

```js
const { getInputVolume, getOutputVolume } = useConversation();
const inputLevel = getInputVolume();
const outputLevel = getOutputVolume();
```

##### getInputByteFrequencyData / getOutputByteFrequencyData

Methods that return `Uint8Array`s containing the current input/output frequency data. See [AnalyserNode.getByteFrequencyData](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/getByteFrequencyData) for more information.

```js
const { getInputByteFrequencyData, getOutputByteFrequencyData } = useConversation();
const inputFrequencyData = getInputByteFrequencyData();
const outputFrequencyData = getOutputByteFrequencyData();
```

<Note>
  These methods are only available for voice conversations. In WebRTC mode the audio is hardcoded to
  use `pcm_48000`, meaning any visualization using the returned data might show different patterns
  to WebSocket connections.
</Note>

##### sendMCPToolApprovalResult

Sends approval result for MCP (Model Context Protocol) tool calls.

```js
const { sendMCPToolApprovalResult } = useConversation();

// Approve a tool call
sendMCPToolApprovalResult('tool_call_id_123', true);

// Reject a tool call
sendMCPToolApprovalResult('tool_call_id_123', false);
```



# React Native SDK

> Agents Platform SDK: deploy customized, interactive voice agents in minutes for React Native apps.

<Info>
  Refer to the [Agents Platform overview](/docs/agents-platform/overview) for an explanation of how
  Agents Platform works.
</Info>


## Installation

Install the package and its dependencies in your React Native project.

```shell
npm install @elevenlabs/react-native @livekit/react-native @livekit/react-native-webrtc livekit-client
```

<Tip>
  An example app using this SDK with Expo can be found
  [here](https://github.com/elevenlabs/packages/tree/main/examples/react-native-expo)
</Tip>


## Requirements

* React Native with LiveKit dependencies
* Microphone permissions configured for your platform
* Expo compatibility (development builds only)

<Warning>
  This SDK was designed and built for use with the Expo framework. Due to its dependency on
  LiveKit's WebRTC implementation, it requires development builds and cannot be used with Expo Go.
</Warning>


## Setup

### Provider Setup

Wrap your app with the `ElevenLabsProvider` to enable Agents Platform functionality.

```tsx
import { ElevenLabsProvider } from '@elevenlabs/react-native';
import React from 'react';

function App() {
  return (
    <ElevenLabsProvider>
      <YourAppComponents />
    </ElevenLabsProvider>
  );
}
```


## Usage

### useConversation

A React Native hook for managing connection and audio usage for ElevenLabs Agents.

#### Initialize conversation

First, initialize the Conversation instance within a component that's wrapped by `ElevenLabsProvider`.

```tsx
import { useConversation } from '@elevenlabs/react-native';
import React from 'react';

function ConversationComponent() {
  const conversation = useConversation();

  // Your component logic here
}
```

Note that Agents Platform requires microphone access. Consider explaining and requesting permissions in your app's UI before the Conversation starts, especially on mobile platforms where permission management is crucial.

#### Options

The Conversation can be initialized with certain options:

```tsx
const conversation = useConversation({
  onConnect: () => console.log('Connected to conversation'),
  onDisconnect: () => console.log('Disconnected from conversation'),
  onMessage: (message) => console.log('Received message:', message),
  onError: (error) => console.error('Conversation error:', error),
  onModeChange: (mode) => console.log('Conversation mode changed:', mode),
  onStatusChange: (prop) => console.log('Conversation status changed:', prop.status),
  onCanSendFeedbackChange: (prop) =>
    console.log('Can send feedback changed:', prop.canSendFeedback),
  onUnhandledClientToolCall: (params) => console.log('Unhandled client tool call:', params),
});
```

* **onConnect** - Handler called when the conversation WebRTC connection is established.
* **onDisconnect** - Handler called when the conversation WebRTC connection is ended.
* **onMessage** - Handler called when a new message is received. These can be tentative or final transcriptions of user voice, replies produced by LLM, or debug messages.
* **onError** - Handler called when an error is encountered.
* **onModeChange** - Handler called when the conversation mode changes. This is useful for indicating whether the agent is speaking or listening.
* **onStatusChange** - Handler called when the conversation status changes.
* **onCanSendFeedbackChange** - Handler called when the ability to send feedback changes.
* **onUnhandledClientToolCall** - Handler called when an unhandled client tool call is encountered.

<Warning>
  Not all client events are enabled by default for an agent. If you have enabled a callback but
  aren't seeing events come through, ensure that your ElevenLabs agent has the corresponding event
  enabled. You can do this in the "Advanced" tab of the agent settings in the ElevenLabs dashboard.
</Warning>

#### Methods

##### startSession

The `startSession` method kicks off the WebRTC connection and starts using the microphone to communicate with the ElevenLabs Agents agent. The method accepts a configuration object with the `agentId` being conditionally required based on whether the agent is public or private.

###### Public agents

For public agents (i.e. agents that don't have authentication enabled), only the `agentId` is required. The Agent ID can be acquired through the [ElevenLabs UI](https://elevenlabs.io/app/agents).

```tsx
const conversation = useConversation();

// For public agents, pass in the agent ID
const startConversation = async () => {
  await conversation.startSession({
    agentId: 'your-agent-id',
  });
};
```

###### Private agents

For private agents, you must pass in a `conversationToken` obtained from the ElevenLabs API. Generating this token requires an ElevenLabs API key.

<Tip>
  The 

  `conversationToken`

   is valid for 10 minutes.
</Tip>

```ts maxLines={0}
// Node.js server

app.get("/conversation-token", yourAuthMiddleware, async (req, res) => {
  const response = await fetch(
    `https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=${process.env.AGENT_ID}`,
    {
      headers: {
        // Requesting a conversation token requires your ElevenLabs API key
        // Do NOT expose your API key to the client!
        'xi-api-key': process.env.ELEVENLABS_API_KEY,
      }
    }
  );

  if (!response.ok) {
    return res.status(500).send("Failed to get conversation token");
  }

  const body = await response.json();
  res.send(body.token);
);
```

Then, pass the token to the `startSession` method. Note that only the `conversationToken` is required for private agents.

```tsx
const conversation = useConversation();

const response = await fetch('/conversation-token', yourAuthHeaders);
const conversationToken = await response.text();

// For private agents, pass in the conversation token
const startConversation = async () => {
  await conversation.startSession({
    conversationToken,
  });
};
```

You can optionally pass a user ID to identify the user in the conversation. This can be your own customer identifier. This will be included in the conversation initiation data sent to the server.

```tsx
const startConversation = async () => {
  await conversation.startSession({
    agentId: 'your-agent-id',
    userId: 'your-user-id',
  });
};
```

##### endSession

A method to manually end the conversation. The method will disconnect and end the conversation.

```tsx
const endConversation = async () => {
  await conversation.endSession();
};
```

##### sendUserMessage

Send a text message to the agent during an active conversation.

```tsx
const sendMessage = async () => {
  await conversation.sendUserMessage('Hello, how can you help me?');
};
```

#### sendContextualUpdate

Sends contextual information to the agent that won't trigger a response.

```tsx
const sendContextualUpdate = async () => {
  await conversation.sendContextualUpdate(
    'User navigated to the profile page. Consider this for next response.'
  );
};
```

##### sendFeedback

Provide feedback on the conversation quality. This helps improve the agent's performance.

```tsx
const provideFeedback = async (liked: boolean) => {
  await conversation.sendFeedback(liked);
};
```

##### sendUserActivity

Notifies the agent about user activity to prevent interruptions. Useful for when the user is actively using the app and the agent should pause speaking, i.e. when the user is typing in a chat.

The agent will pause speaking for \~2 seconds after receiving this signal.

```tsx
const signalActivity = async () => {
  await conversation.sendUserActivity();
};
```

#### Properties

##### status

A React state containing the current status of the conversation.

```tsx
const { status } = useConversation();
console.log(status); // "connected" or "disconnected"
```

##### isSpeaking

A React state containing information on whether the agent is currently speaking. This is useful for indicating agent status in your UI.

```tsx
const { isSpeaking } = useConversation();
console.log(isSpeaking); // boolean
```

##### canSendFeedback

A React state indicating whether feedback can be submitted for the current conversation.

```tsx
const { canSendFeedback } = useConversation();

// Use this to conditionally show feedback UI
{
  canSendFeedback && (
    <FeedbackButtons
      onLike={() => conversation.sendFeedback(true)}
      onDislike={() => conversation.sendFeedback(false)}
    />
  );
}
```

##### getId

Retrieves the conversation ID.

```tsx
const conversationId = conversation.getId();
console.log(conversationId); // e.g., "conv_9001k1zph3fkeh5s8xg9z90swaqa"
```

##### setMicMuted

Mutes/unmutes the microphone.

```tsx
// Mute the microphone
conversation.setMicMuted(true);

// Unmute the microphone
conversation.setMicMuted(false);
```


## Example Implementation

Here's a complete example of a React Native component using the ElevenLabs Agents SDK:

```tsx
import { ElevenLabsProvider, useConversation } from '@elevenlabs/react-native';
import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

function ConversationScreen() {
  const [isConnected, setIsConnected] = useState(false);

  const conversation = useConversation({
    onConnect: () => {
      console.log('Connected to conversation');
      setIsConnected(true);
    },
    onDisconnect: () => {
      console.log('Disconnected from conversation');
      setIsConnected(false);
    },
    onMessage: (message) => {
      console.log('Message received:', message);
    },
    onError: (error) => {
      console.error('Conversation error:', error);
    },
  });

  const startConversation = async () => {
    try {
      await conversation.startSession({
        agentId: 'your-agent-id',
      });
    } catch (error) {
      console.error('Failed to start conversation:', error);
    }
  };

  const endConversation = async () => {
    try {
      await conversation.endSession();
    } catch (error) {
      console.error('Failed to end conversation:', error);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.status}>Status: {conversation.status}</Text>

      <Text style={styles.speaking}>
        Agent is {conversation.isSpeaking ? 'speaking' : 'not speaking'}
      </Text>

      <TouchableOpacity
        style={[styles.button, isConnected && styles.buttonActive]}
        onPress={isConnected ? endConversation : startConversation}
      >
        <Text style={styles.buttonText}>
          {isConnected ? 'End Conversation' : 'Start Conversation'}
        </Text>
      </TouchableOpacity>

      {conversation.canSendFeedback && (
        <View style={styles.feedbackContainer}>
          <TouchableOpacity
            style={styles.feedbackButton}
            onPress={() => conversation.sendFeedback(true)}
          >
            <Text>👍</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.feedbackButton}
            onPress={() => conversation.sendFeedback(false)}
          >
            <Text>👎</Text>
          </TouchableOpacity>
        </View>
      )}
    </View>
  );
}

function App() {
  return (
    <ElevenLabsProvider>
      <ConversationScreen />
    </ElevenLabsProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  status: {
    fontSize: 16,
    marginBottom: 10,
  },
  speaking: {
    fontSize: 14,
    marginBottom: 20,
    color: '#666',
  },
  button: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 8,
    marginBottom: 20,
  },
  buttonActive: {
    backgroundColor: '#FF3B30',
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
  feedbackContainer: {
    flexDirection: 'row',
    gap: 10,
  },
  feedbackButton: {
    backgroundColor: '#F2F2F7',
    padding: 10,
    borderRadius: 8,
  },
});

export default App;
```


## Platform-Specific Considerations

### iOS

Ensure microphone permissions are properly configured in your `Info.plist`:

```xml
<key>NSMicrophoneUsageDescription</key>
<string>This app needs microphone access to enable voice conversations with AI agents.</string>
```

### Android

Add microphone permissions to your `android/app/src/main/AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECORD_AUDIO" />
```

Consider requesting runtime permissions before starting a conversation:

```tsx
import { PermissionsAndroid, Platform } from 'react-native';

const requestMicrophonePermission = async () => {
  if (Platform.OS === 'android') {
    const granted = await PermissionsAndroid.request(PermissionsAndroid.PERMISSIONS.RECORD_AUDIO, {
      title: 'Microphone Permission',
      message: 'This app needs microphone access to enable voice conversations.',
      buttonNeutral: 'Ask Me Later',
      buttonNegative: 'Cancel',
      buttonPositive: 'OK',
    });
    return granted === PermissionsAndroid.RESULTS.GRANTED;
  }
  return true;
};
```



# JavaScript SDK

> Agents Platform SDK: deploy customized, interactive voice agents in minutes.

<Info>
  Also see the 

  [Agents Platform overview](/docs/agents-platform/overview)
</Info>


## Installation

Install the package in your project through package manager.

```shell
npm install @elevenlabs/client

# or
yarn add @elevenlabs/client

# or
pnpm install @elevenlabs/client
```


## Usage

This library is primarily meant for development in vanilla JavaScript projects, or as a base for libraries tailored to specific frameworks.
It is recommended to check whether your specific framework has its own library.
However, you can use this library in any JavaScript-based project.

### Initialize conversation

First, initialize the Conversation instance:

```js
const conversation = await Conversation.startSession(options);
```

This will kick off the websocket connection and start using microphone to communicate with the ElevenLabs Agents agent. Consider explaining and allowing microphone access in your apps UI before the Conversation kicks off:

```js
// call after explaining to the user why the microphone access is needed
await navigator.mediaDevices.getUserMedia({ audio: true });
```

#### Session configuration

The options passed to `startSession` specify how the session is established. Conversations can be started with public or private agents.

##### Public agents

Agents that don't require any authentication can be used to start a conversation by using the agent ID and the connection type. The agent ID can be acquired through the [ElevenLabs UI](https://elevenlabs.io/app/conversational-ai).

For public agents, you can use the ID directly:

```js
const conversation = await Conversation.startSession({
  agentId: '<your-agent-id>',
  connectionType: 'webrtc', // 'websocket' is also accepted
});
```

##### Private agents

If the conversation requires authorization, you will need to add a dedicated endpoint to your server that will either request a signed url (if using the WebSockets connection type) or a conversation token (if using WebRTC) using the [ElevenLabs API](https://elevenlabs.io/docs/introduction) and pass it back to the client.

Here's an example for a WebSocket connection:

```js maxLines=0
// Node.js server

app.get('/signed-url', yourAuthMiddleware, async (req, res) => {
  const response = await fetch(
    `https://api.elevenlabs.io/v1/convai/conversation/get-signed-url?agent_id=${process.env.AGENT_ID}`,
    {
      method: 'GET',
      headers: {
        // Requesting a signed url requires your ElevenLabs API key
        // Do NOT expose your API key to the client!
        'xi-api-key': process.env.XI_API_KEY,
      },
    }
  );

  if (!response.ok) {
    return res.status(500).send('Failed to get signed URL');
  }

  const body = await response.json();
  res.send(body.signed_url);
});
```

```js
// Client

const response = await fetch('/signed-url', yourAuthHeaders);
const signedUrl = await response.text();

const conversation = await Conversation.startSession({
  signedUrl,
  connectionType: 'websocket',
});
```

Here's an example for WebRTC:

```js maxLines=0
// Node.js server

app.get('/conversation-token', yourAuthMiddleware, async (req, res) => {
  const response = await fetch(
    `https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=${process.env.AGENT_ID}`,
    {
      headers: {
        // Requesting a conversation token requires your ElevenLabs API key
        // Do NOT expose your API key to the client!
        'xi-api-key': process.env.ELEVENLABS_API_KEY,
      },
    }
  );

  if (!response.ok) {
    return res.status(500).send('Failed to get conversation token');
  }

  const body = await response.json();
  res.send(body.token);
});
```

Once you have the token, providing it to `startSession` will initiate the conversation using WebRTC.

```js
// Client

const response = await fetch('/conversation-token', yourAuthHeaders);
const conversationToken = await response.text();

const conversation = await Conversation.startSession({
  conversationToken,
  connectionType: 'webrtc',
});
```

#### Optional callbacks

The options passed to `startSession` can also be used to register optional callbacks:

* **onConnect** - handler called when the conversation websocket connection is established.
* **onDisconnect** - handler called when the conversation websocket connection is ended.
* **onMessage** - handler called when a new text message is received. These can be tentative or final transcriptions of user voice, replies produced by LLM. Primarily used for handling conversation transcription.
* **onError** - handler called when an error is encountered.
* **onStatusChange** - handler called whenever connection status changes. Can be `connected`, `connecting` and `disconnected` (initial).
* **onModeChange** - handler called when a status changes, eg. agent switches from `speaking` to `listening`, or the other way around.
* **onCanSendFeedbackChange** - handler called when sending feedback becomes available or unavailable.

<Warning>
  Not all client events are enabled by default for an agent. If you have enabled a callback but
  aren't seeing events come through, ensure that your ElevenLabs agent has the corresponding event
  enabled. You can do this in the "Advanced" tab of the agent settings in the ElevenLabs dashboard.
</Warning>

#### Return value

`startSession` returns a `Conversation` instance that can be used to control the session. The method will throw an error if the session cannot be established. This can happen if the user denies microphone access, or if the connection
fails.

**endSession**

A method to manually end the conversation. The method will end the conversation and disconnect from websocket.
Afterwards the conversation instance will be unusable and can be safely discarded.

```js
await conversation.endSession();
```

**getId**

A method returning the conversation ID.

```js
const id = conversation.getId();
```

**setVolume**

A method to set the output volume of the conversation. Accepts object with volume field between 0 and 1.

```js
await conversation.setVolume({ volume: 0.5 });
```

**getInputVolume / getOutputVolume**

Methods that return the current input/output volume on a scale from `0` to `1` where `0` is -100 dB and `1` is -30 dB.

```js
const inputVolume = await conversation.getInputVolume();
const outputVolume = await conversation.getOutputVolume();
```

**sendFeedback**

A method for sending binary feedback to the agent. The method accepts a boolean value, where `true` represents positive feedback and `false` negative feedback.

Feedback is always correlated to the most recent agent response and can be sent only once per response.

You can listen to `onCanSendFeedbackChange` to know if feedback can be sent at the given moment.

```js
conversation.sendFeedback(true); // positive feedback
conversation.sendFeedback(false); // negative feedback
```

**sendContextualUpdate**

A method to send contextual updates to the agent. This can be used to inform the agent about user actions that are not directly related to the conversation, but may influence the agent's responses.

```js
conversation.sendContextualUpdate(
  "User navigated to another page. Consider it for next response, but don't react to this contextual update."
);
```

**sendUserMessage**

Sends a text message to the agent.

Can be used to let the user type in the message instead of using the microphone. Unlike `sendContextualUpdate`, this will be treated as a user message and will prompt the agent to take its turn in the conversation.

```js
sendButton.addEventListener('click', (e) => {
  conversation.sendUserMessage(textInput.value);
  textInput.value = '';
});
```

**sendUserActivity**

Notifies the agent about user activity.

The agent will not attempt to speak for at least 2 seconds after the user activity is detected.

This can be used to prevent the agent from interrupting the user when they are typing.

```js
textInput.addEventListener('input', () => {
  conversation.sendUserActivity();
});
```

**setMicMuted**

A method to mute/unmute the microphone.

```js
// Mute the microphone
conversation.setMicMuted(true);

// Unmute the microphone
conversation.setMicMuted(false);
```

**changeInputDevice**

Allows you to change the audio input device during an active voice conversation. This method is only available for voice conversations.

<Note>
  In WebRTC mode the input format and sample rate are hardcoded to `pcm` and `48000` respectively.
  Changing those values when changing the input device is a no-op.
</Note>

```js
const conversation = await Conversation.startSession({
  agentId: '<your-agent-id>',
  // Alternatively you can provide a device ID when starting the session
  // Useful if you want to start the conversation with a non-default device
  inputDeviceId: 'your-device-id',
});

// Change to a specific input device
await conversation.changeInputDevice({
  sampleRate: 16000,
  format: 'pcm',
  preferHeadphonesForIosDevices: true,
  inputDeviceId: 'your-device-id',
});
```

If the device ID is invalid, the default device will be used instead.

**changeOutputDevice**

Allows you to change the audio output device during an active voice conversation. This method is only available for voice conversations.

<Note>
  In WebRTC mode the output format and sample rate are hardcoded to `pcm` and `48000` respectively.
  Changing those values when changing the output device is a no-op.
</Note>

```js
const conversation = await Conversation.startSession({
  agentId: '<your-agent-id>',
  // Alternatively you can provide a device ID when starting the session
  // Useful if you want to start the conversation with a non-default device
  outputDeviceId: 'your-device-id',
});

// Change to a specific output device
await conversation.changeOutputDevice({
  sampleRate: 16000,
  format: 'pcm',
  outputDeviceId: 'your-device-id',
});
```

<Note>
  Device switching only works for voice conversations. If no specific `deviceId` is provided, the
  browser will use its default device selection. You can enumerate available devices using the
  [MediaDevices.enumerateDevices()](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/enumerateDevices)
  API.
</Note>

**getInputByteFrequencyData / getOutputByteFrequencyData**

Methods that return `Uint8Array`s containing the current input/output frequency data. See [AnalyserNode.getByteFrequencyData](https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/getByteFrequencyData) for more information.

<Note>
  These methods are only available for voice conversations. In WebRTC mode the audio is hardcoded to
  use `pcm_48000`, meaning any visualization using the returned data might show different patterns
  to WebSocket connections.
</Note>



# Kotlin SDK

> Agents Platform SDK: deploy customized, interactive voice agents in minutes for Android apps.

<Info>
  Refer to the [Agents Platform overview](/docs/agents-platform/overview) for an explanation of how
  Agents Platform works.
</Info>


## Installation

Add the ElevenLabs SDK to your Android project by including the following dependency in your app-level `build.gradle` file:

```kotlin build.gradle.kts
dependencies {
    // ElevenLabs Agents SDK (Android)
    implementation("io.elevenlabs:elevenlabs-android:<latest>")

    // Kotlin coroutines, AndroidX, etc., as needed by your app
}
```

<Tip>
  An example Android app using this SDK can be found
  [here](https://github.com/elevenlabs/elevenlabs-android/tree/main/example-app)
</Tip>


## Requirements

* Android API level 21 (Android 5.0) or higher
* Internet permission for API calls
* Microphone permission for voice input
* Network security configuration for HTTPS calls


## Setup

### Manifest Configuration

Add the necessary permissions to your `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
```

### Runtime Permissions

For Android 6.0 (API level 23) and higher, you must request microphone permission at runtime:

```kotlin
import android.Manifest
import android.content.pm.PackageManager
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

private fun requestMicrophonePermission() {
    if (ContextCompat.checkSelfPermission(this, Manifest.permission.RECORD_AUDIO)
        != PackageManager.PERMISSION_GRANTED) {

        if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.RECORD_AUDIO)) {
            // Show explanation to the user
            showPermissionExplanationDialog()
        } else {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.RECORD_AUDIO),
                MICROPHONE_PERMISSION_REQUEST_CODE
            )
        }
    }
}
```

### Network Security Configuration

For apps targeting Android 9 (API level 28) or higher, ensure your network security configuration allows clear text traffic if needed:

```xml
<!-- In AndroidManifest.xml -->
<application
    android:networkSecurityConfig="@xml/network_security_config"
    ... >
```

```xml
<!-- res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">your-api-domain.com</domain>
    </domain-config>
</network-security-config>
```


## Usage

Initialize the ElevenLabs SDK in your `Application` class or main activity:

Start a conversation session with either:

* Public agent: pass `agentId`
* Private agent: pass `conversationToken` provisioned from your backend (never expose your API key to the client).

```kotlin
import io.elevenlabs.ConversationClient
import io.elevenlabs.ConversationConfig
import io.elevenlabs.ConversationSession
import io.elevenlabs.ClientTool
import io.elevenlabs.ClientToolResult

// Start a public agent session (token generated for you)
val config = ConversationConfig(
    agentId = "<your_public_agent_id>", // OR conversationToken = "<token>"
    userId = "your-user-id",
    // Optional callbacks
    onConnect = { conversationId ->
        // Called when the conversation is connected and returns the conversation ID. You can access conversationId via session.getId() too
    },
    onMessage = { source, messageJson ->
        // Raw JSON messages from data channel; useful for logging/telemetry
    },
    onModeChange = { mode ->
        // "speaking" | "listening" — drive UI indicators
    },
    onStatusChange = { status ->
        // "connected" | "connecting" | "disconnected"
    },
    onCanSendFeedbackChange = { canSend ->
        // Enable/disable thumbs up/down buttons for feedback reporting
    },
    onUnhandledClientToolCall = { call ->
        // Agent requested a client tool not registered on the device
    },
    onVadScore = { score ->
        // Voice Activity Detection score, range from 0 to 1 where higher values indicate higher confidence of speech
    },
    // List of client tools the agent can invoke
    clientTools = mapOf(
        "logMessage" to object : ClientTool {
            override suspend fun execute(parameters: Map<String, Any>): ClientToolResult {
                val message = parameters["message"] as? String

                Log.d("ExampleApp", "[INFO] Client Tool Log: $message")
                return ClientToolResult.success("Message logged successfully")
            }
        }
    ),
)

// In an Activity context
val session: ConversationSession = ConversationClient.startSession(config, this)
```

Note that Agents Platform requires microphone access. Consider explaining and requesting permissions in your app's UI before the conversation starts, especially on Android 6.0+ where runtime permissions are required.

<Note>
  If a tool is configured with `expects_response=false` on the server, return `null` from `execute`
  to skip sending a tool result back to the agent.
</Note>


## Public vs Private Agents

* **Public agents** (no auth): Initialize with `agentId` in `ConversationConfig`. The SDK requests a conversation token from ElevenLabs without needing an API key on device.
* **Private agents** (auth): Initialize with `conversationToken` in `ConversationConfig`. Your server requests a conversation token from ElevenLabs using your ElevenLabs API key.

<Error>
  Never embed API keys in clients. They can be easily extracted and used maliciously.
</Error>


## Client Tools

Register client tools to allow the agent to call local capabilities on the device.

```kotlin
val config = ConversationConfig(
    agentId = "<public_agent>",
    clientTools = mapOf(
        "logMessage" to object : io.elevenlabs.ClientTool {
            override suspend fun execute(parameters: Map<String, Any>): io.elevenlabs.ClientToolResult? {
                val message = parameters["message"] as? String ?: return io.elevenlabs.ClientToolResult.failure("Missing 'message'")

                android.util.Log.d("ClientTool", "Log: $message")
                return null // No response needed for fire-and-forget tools
            }
        }
    )
)
```

When the agent issues a `client_tool_call`, the SDK executes the matching tool and responds with a `client_tool_result`. If the tool is not registered, `onUnhandledClientToolCall` is invoked and a failure result is returned to the agent (if a response is expected).

### Callbacks Overview

* **onConnect** - Called when the WebRTC connection is established. Returns the conversation ID.
* **onMessage** - Called when a new message is received. These can be tentative or final transcriptions of user voice, replies produced by LLM, or debug messages. Provides source (`"ai"` or `"user"`) and raw JSON message.
* **onModeChange** - Called when the conversation mode changes. This is useful for indicating whether the agent is speaking (`"speaking"`) or listening (`"listening"`).
* **onStatusChange** - Called when the conversation status changes (`"connected"`, `"connecting"`, or `"disconnected"`).
* **onCanSendFeedbackChange** - Called when the ability to send feedback changes. Enables/disables feedback buttons.
* **onUnhandledClientToolCall** - Called when the agent requests a client tool that is not registered on the device.
* **onVadScore** - Called when the voice activity detection score changes. Range from 0 to 1 where higher values indicate higher confidence of speech.

<Warning>
  Not all client events are enabled by default for an agent. If you have enabled a callback but
  aren't seeing events come through, ensure that your ElevenLabs agent has the corresponding event
  enabled. You can do this in the "Advanced" tab of the agent settings in the ElevenLabs dashboard.
</Warning>

### Methods

#### startSession

The `startSession` method initiates the WebRTC connection and starts using the microphone to communicate with the ElevenLabs Agents agent.

##### Public agents

For public agents (i.e. agents that don't have authentication enabled), only the `agentId` is required. The Agent ID can be acquired through the [ElevenLabs UI](https://elevenlabs.io/app/agents).

```kotlin
val session = ConversationClient.startSession(
    config = ConversationConfig(
        agentId = "your-agent-id"
    ),
    context = this
)
```

##### Private agents

For private agents, you must pass in a `conversationToken` obtained from the ElevenLabs API. Generating this token requires an ElevenLabs API key.

<Tip>
  The 

  `conversationToken`

   is valid for 10 minutes.
</Tip>

```typescript maxLines=0
// Server-side token generation (Node.js example)

app.get('/conversation-token', yourAuthMiddleware, async (req, res) => {
  const response = await fetch(
    `https://api.elevenlabs.io/v1/convai/conversation/token?agent_id=${process.env.AGENT_ID}`,
    {
      headers: {
        // Requesting a conversation token requires your ElevenLabs API key
        // Do NOT expose your API key to the client!
        'xi-api-key': process.env.ELEVENLABS_API_KEY,
      },
    }
  );

  if (!response.ok) {
    return res.status(500).send('Failed to get conversation token');
  }

  const body = await response.json();
  res.send(body.token);
});
```

Then, pass the token to the `startSession` method. Note that only the `conversationToken` is required for private agents.

```kotlin

// Get conversation token from your server
val conversationToken = fetchConversationTokenFromServer()

// For private agents, pass in the conversation token
val session = ConversationClient.startSession(
    config = ConversationConfig(
        conversationToken = conversationToken
    ),
    context = this
)
```

You can optionally pass a user ID to identify the user in the conversation. This can be your own customer identifier. This will be included in the conversation initiation data sent to the server.

```kotlin
val session = ConversationClient.startSession(
    config = ConversationConfig(
        agentId = "your-agent-id",
        userId = "your-user-id"
    ),
    context = this
)
```

#### endSession

A method to manually end the conversation. The method will disconnect and end the conversation.

```kotlin
session.endSession()
```

#### sendUserMessage

Send a text message to the agent during an active conversation. This will trigger a response from the agent.

```kotlin
session.sendUserMessage("Hello, how can you help me?")
```

#### sendContextualUpdate

Sends contextual information to the agent that won't trigger a response.

```kotlin
session.sendContextualUpdate(
    "User navigated to the profile page. Consider this for next response."
)
```

#### sendFeedback

Provide feedback on the conversation quality. This helps improve the agent's performance. Use `onCanSendFeedbackChange` to enable your thumbs up/down UI when feedback is allowed.

```kotlin
// Positive feedback
session.sendFeedback(true)

// Negative feedback
session.sendFeedback(false)
```

#### sendUserActivity

Notifies the agent about user activity to prevent interruptions. Useful for when the user is actively using the app and the agent should pause speaking, i.e. when the user is typing in a chat.

The agent will pause speaking for \~2 seconds after receiving this signal.

```kotlin
session.sendUserActivity()
```

#### getId

Get the conversation ID.

```kotlin
val conversationId = session.getId()
Log.d("Conversation", "Conversation ID: $conversationId")
// e.g., "conv_123"
```

#### Mute/ Unmute

```kotlin
session.toggleMute()
session.setMicMuted(true)   // mute
session.setMicMuted(false)  // unmute
```

Observe `session.isMuted` to update the UI label between "Mute" and "Unmute".

### Properties

#### status

Get the current status of the conversation.

```kotlin
val status = session.status
Log.d("Conversation", "Current status: $status")
// Values: DISCONNECTED, CONNECTING, CONNECTED
```


## ProGuard / R8

If you shrink/obfuscate, ensure Gson models and LiveKit are kept. Example rules (adjust as needed):

```proguard
-keep class io.elevenlabs.** { *; }
-keep class io.livekit.** { *; }
-keepattributes *Annotation*
```


## Troubleshooting

* Ensure microphone permission is granted at runtime
* If reconnect hangs, verify your app calls `session.endSession()` and that you start a new session instance before reconnecting
* For emulators, verify audio input/output routes are working; physical devices tend to behave more reliably


## Example Implementation

For an example implementation, see the example app in the [ElevenLabs Android SDK repository](https://github.com/elevenlabs/elevenlabs-android/tree/main/example-app). The app demonstrates:

* One‑tap connect/disconnect
* Speaking/listening indicator
* Feedback buttons with UI enable/disable
* Typing indicator via `sendUserActivity()`
* Contextual and user messages from an input
* Microphone mute/unmute button



# Swift SDK

> Agents Platform SDK: deploy customized, interactive voice agents in your Swift applications.

<Info>
  Check out our [complete Swift quickstart project](https://github.com/elevenlabs/voice-starterkit-swift) to get started quickly with a full working example.
</Info>


## Installation

Add the ElevenLabs Swift SDK to your project using Swift Package Manager:

<Steps>
  <Step title="Add the Package Dependency">
    ```swift
    dependencies: [ .package(url: "https://github.com/elevenlabs/elevenlabs-swift-sdk.git",
    from: "2.0.0") ] 
    ```

    Or using Xcode:

    1. Open your project in Xcode
    2. Go to `File` > `Add Package Dependencies...`
    3. Enter the repository URL: `https://github.com/elevenlabs/elevenlabs-swift-sdk.git`
    4. Select version 2.0.0 or later
  </Step>

  <Step title="Import the SDK">
    ```swift
    import ElevenLabs 
    ```
  </Step>
</Steps>

<Warning>
  Ensure you add `NSMicrophoneUsageDescription` to your Info.plist to explain microphone access to
  users. The SDK requires iOS 14.0+ / macOS 11.0+ and Swift 5.9+.
</Warning>


## Quick Start

Get started with a simple conversation in just a few lines. Optionally, We recommended passing in your own end user id's to map conversations to your users.

```swift
import ElevenLabs

// Start a conversation with your agent
let conversation = try await ElevenLabs.startConversation(
    agentId: "your-agent-id",
    userId: "your-end-user-id",
    config: ConversationConfig()
)

// Observe conversation state and messages
conversation.$state
    .sink { state in
        print("Connection state: \(state)")
    }
    .store(in: &cancellables)

conversation.$messages
    .sink { messages in
        for message in messages {
            print("\(message.role): \(message.content)")
        }
    }
    .store(in: &cancellables)

// Send messages and control the conversation
try await conversation.sendMessage("Hello!")
try await conversation.toggleMute()
await conversation.endConversation()
```


## Authentication

There are two ways to authenticate and start a conversation:

<Tabs>
  <Tab title="Public Agents">
    For public agents, use the agent ID directly:

    ```swift
    let conversation = try await ElevenLabs.startConversation(
        agentId: "your-public-agent-id",
        config: ConversationConfig()
    )
    ```
  </Tab>

  <Tab title="Private Agents">
    For private agents, use a conversation token obtained from your backend:

    ```swift
    // Get token from your backend (never store API keys in your app)
    let token = try await fetchConversationToken()
    let conversation = try await ElevenLabs.startConversation(
        auth: .conversationToken(token),
        config: ConversationConfig()
    )
    ```

    <Warning>
      Never store your ElevenLabs API key in your mobile app. Always use a backend service to generate conversation tokens.
    </Warning>
  </Tab>
</Tabs>


## Core Features

### Reactive Conversation Management

The SDK provides a modern `Conversation` class with `@Published` properties for reactive UI updates:

```swift
@MainActor
class ConversationManager: ObservableObject {
    @Published var conversation: Conversation?
    private var cancellables = Set<AnyCancellable>()

    func startConversation(agentId: String) async throws {
        let config = ConversationConfig(
            conversationOverrides: ConversationOverrides(textOnly: false)
        )

        conversation = try await ElevenLabs.startConversation(
            agentId: agentId,
            config: config
        )

        setupObservers()
    }

    private func setupObservers() {
        guard let conversation else { return }

        // Monitor connection state
        conversation.$state
            .sink { state in print("State: \(state)") }
            .store(in: &cancellables)

        // Monitor messages
        conversation.$messages
            .sink { messages in print("Messages: \(messages.count)") }
            .store(in: &cancellables)
    }
}
```

### Voice and Text Modes

```swift
// Voice conversation (default)
let voiceConfig = ConversationConfig(
    conversationOverrides: ConversationOverrides(textOnly: false)
)

// Text-only conversation
let textConfig = ConversationConfig(
    conversationOverrides: ConversationOverrides(textOnly: true)
)
```

### Audio Controls

```swift
// Microphone control
try await conversation.toggleMute()
try await conversation.setMuted(true)

// Check microphone state
let isMuted = conversation.isMuted

// Access audio tracks for advanced use cases
let inputTrack = conversation.inputTrack
let agentAudioTrack = conversation.agentAudioTrack
```

### Client Tools

Client Tools allow you to register custom functions that can be called by your AI agent during conversations. The new SDK provides improved parameter handling and error management.

#### Handling Tool Calls

Handle tool calls from your agent with full parameter support:

```swift
private func handleToolCall(_ toolCall: ClientToolCallEvent) async {
    do {
        let parameters = try toolCall.getParameters()
        let result = await executeClientTool(
            name: toolCall.toolName,
            parameters: parameters
        )

        if toolCall.expectsResponse {
            try await conversation?.sendToolResult(
                for: toolCall.toolCallId,
                result: result
            )
        } else {
            conversation?.markToolCallCompleted(toolCall.toolCallId)
        }
    } catch {
        // Handle tool execution errors
        if toolCall.expectsResponse {
            try? await conversation?.sendToolResult(
                for: toolCall.toolCallId,
                result: ["error": error.localizedDescription],
                isError: true
            )
        }
    }
}

// Example tool implementation
func executeClientTool(name: String, parameters: [String: Any]) async -> [String: Any] {
    switch name {
    case "get_weather":
        guard let location = parameters["location"] as? String else {
            return ["error": "Missing location parameter"]
        }
        // Fetch weather data
        return ["temperature": "22°C", "condition": "Sunny"]

    case "send_email":
        guard let recipient = parameters["recipient"] as? String,
              let subject = parameters["subject"] as? String else {
            return ["error": "Missing required parameters"]
        }
        // Send email logic
        return ["status": "sent", "messageId": "12345"]

    default:
        return ["error": "Unknown tool: \(name)"]
    }
}
```

<Info>
  Remember to setup your agent with the client-tools in the ElevenLabs UI. See the [Client Tools
  documentation](/docs/agents-platform/customization/tools/client-tools) for setup instructions.
</Info>

### Connection State Management

Monitor the conversation state to handle different connection phases:

```swift
conversation.$state
    .sink { state in
        switch state {
        case .idle:
            // Not connected
            break
        case .connecting:
            // Show connecting indicator
            break
        case .active(let callInfo):
            // Connected to agent: \(callInfo.agentId)
            break
        case .ended(let reason):
            // Handle disconnection: \(reason)
            break
        case .error(let error):
            // Handle error: \(error)
            break
        }
    }
    .store(in: &cancellables)
```

### Agent State Monitoring

Track when the agent is listening or speaking:

```swift
conversation.$agentState
    .sink { state in
        switch state {
        case .listening:
            // Agent is listening, show listening indicator
            break
        case .speaking:
            // Agent is speaking, show speaking indicator
            break
        }
    }
    .store(in: &cancellables)
```

### Message Handling

Send text messages and monitor the conversation:

```swift
// Send a text message
try await conversation.sendMessage("Hello, how can you help me today?")

// Monitor all messages in the conversation
conversation.$messages
    .sink { messages in
        for message in messages {
            switch message.role {
            case .user:
                print("User: \(message.content)")
            case .agent:
                print("Agent: \(message.content)")
            }
        }
    }
    .store(in: &cancellables)
```

### Session Management

```swift
// End the conversation
await conversation.endConversation()

// Check if conversation is active
let isActive = conversation.state.isActive
```


## SwiftUI Integration

Here's a comprehensive SwiftUI example using the new SDK:

```swift
import SwiftUI
import ElevenLabs
import Combine

struct ConversationView: View {
    @StateObject private var viewModel = ConversationViewModel()

    var body: some View {
        VStack(spacing: 20) {
            // Connection status
            Text(viewModel.connectionStatus)
                .font(.headline)
                .foregroundColor(viewModel.isConnected ? .green : .red)

            // Chat messages
            ScrollView {
                LazyVStack(alignment: .leading, spacing: 8) {
                    ForEach(viewModel.messages, id: \.id) { message in
                        MessageBubble(message: message)
                    }
                }
            }
            .frame(maxHeight: 400)

            // Controls
            HStack(spacing: 16) {
                Button(viewModel.isConnected ? "End" : "Start") {
                    Task {
                        if viewModel.isConnected {
                            await viewModel.endConversation()
                        } else {
                            await viewModel.startConversation()
                        }
                    }
                }
                .buttonStyle(.borderedProminent)

                Button(viewModel.isMuted ? "Unmute" : "Mute") {
                    Task { await viewModel.toggleMute() }
                }
                .buttonStyle(.bordered)
                .disabled(!viewModel.isConnected)

                Button("Send Message") {
                    Task { await viewModel.sendTestMessage() }
                }
                .buttonStyle(.bordered)
                .disabled(!viewModel.isConnected)
            }

            // Agent state indicator
            if viewModel.isConnected {
                HStack {
                    Circle()
                        .fill(viewModel.agentState == .speaking ? .blue : .gray)
                        .frame(width: 10, height: 10)
                    Text(viewModel.agentState == .speaking ? "Agent speaking" : "Agent listening")
                        .font(.caption)
                }
            }
        }
        .padding()
    }
}

struct MessageBubble: View {
    let message: Message

    var body: some View {
        HStack {
            if message.role == .user { Spacer() }

            VStack(alignment: .leading) {
                Text(message.role == .user ? "You" : "Agent")
                    .font(.caption)
                    .foregroundColor(.secondary)
                Text(message.content)
                    .padding()
                    .background(message.role == .user ? Color.blue : Color.gray.opacity(0.3))
                    .foregroundColor(message.role == .user ? .white : .primary)
                    .cornerRadius(12)
            }

            if message.role == .agent { Spacer() }
        }
    }
}

@MainActor
class ConversationViewModel: ObservableObject {
    @Published var messages: [Message] = []
    @Published var isConnected = false
    @Published var isMuted = false
    @Published var agentState: AgentState = .listening
    @Published var connectionStatus = "Disconnected"

    private var conversation: Conversation?
    private var cancellables = Set<AnyCancellable>()

    func startConversation() async {
        do {
            conversation = try await ElevenLabs.startConversation(
                agentId: "your-agent-id",
                config: ConversationConfig()
            )
            setupObservers()
        } catch {
            print("Failed to start conversation: \(error)")
            connectionStatus = "Failed to connect"
        }
    }

    func endConversation() async {
        await conversation?.endConversation()
        conversation = nil
        cancellables.removeAll()
    }

    func toggleMute() async {
        try? await conversation?.toggleMute()
    }

    func sendTestMessage() async {
        try? await conversation?.sendMessage("Hello from the app!")
    }

    private func setupObservers() {
        guard let conversation else { return }

        conversation.$messages
            .assign(to: &$messages)

        conversation.$state
            .map { state in
                switch state {
                case .idle: return "Disconnected"
                case .connecting: return "Connecting..."
                case .active: return "Connected"
                case .ended: return "Ended"
                case .error: return "Error"
                }
            }
            .assign(to: &$connectionStatus)

        conversation.$state
            .map { $0.isActive }
            .assign(to: &$isConnected)

        conversation.$isMuted
            .assign(to: &$isMuted)

        conversation.$agentState
            .assign(to: &$agentState)
    }
}
```



---
**Navigation:** [← Previous](./16-chat-mode.md) | [Index](./index.md) | [Next →](./18-websocket.md)
