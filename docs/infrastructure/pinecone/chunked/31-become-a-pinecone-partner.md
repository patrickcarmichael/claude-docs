**Navigation:** [← Previous](./30-use-an-assistant-mcp-server.md) | [Index](./index.md) | [Next →](./32-2023-releases.md)

# Become a Pinecone partner
Source: https://docs.pinecone.io/integrations/build-integration/become-a-partner



Anyone can use the [Pinecone SDKs](/reference/pinecone-sdks) or the [Pinecone API](/reference/api/introduction) to build a native Pinecone integration into a third-party service or tool. However, becoming an official Pinecone partner can help accelerate your go-to-market and add value to your customers.

To start the process, fill out our [application form](https://www.pinecone.io/partners/#sales-contact-form-submissions).


## Additional information

* [Attribute usage to your integration](/integrations/build-integration/attribute-usage-to-your-integration)
* [Connect your users to Pinecone](/integrations/build-integration/connect-your-users-to-pinecone)



# Connect your users to Pinecone
Source: https://docs.pinecone.io/integrations/build-integration/connect-your-users-to-pinecone



To reduce friction for users using your integration, you can create a [custom object](#custom-object), like a button or link, to trigger a **Connect to Pinecone** popup from your app, website, or [Colab](https://colab.google/) notebook. Within this popup, your users can sign up for or log in to Pinecone, select or create an organization and project to connect to, and generate an API key. The API key is then communicated back to the user to copy or directly sent to the hosting page, app, or notebook.

Alternatively, you can embed our [pre-built widget](#pre-built-widget), which provides the same functionality, but with the ease of a drop-in component.

To start, [create an integration ID](#create-an-integration-id) for your app.

<Note>
  Only [organization owners](/guides/organizations/manage-organization-members) can add or manage integrations.
</Note>


## Create an integration ID

Create a unique `integrationId` to enable usage of the **Connect to Pinecone** [popup](#custom-object) and [widget](#pre-built-widget):

1. On the the [**Integrations**](https://app.pinecone.io/organizations/-/settings/integrations) tab in the Pinecone console, click the **Create Integration** button.

   <Note>The **Integrations** tab does not display unless your organization already has integrations. [Follow this link to create your first integration](https://app.pinecone.io/organizations/-/settings/integrations?create=true).</Note>

2. Fill out the **Create integration** form:
   * **Integration name**: Give your integration a name.

   * **URL Slug**: This is your `integrationID`. Enter a human-readable string that uniquely identifies your integration and that may appear in URLs. Your integration URL slug is public and cannot be changed.

   * **Logo**: Upload a logo for your integration.

   * **Return mechanism**: Select one of the following return methods for the generated API key:
     * **Web Message**: Your application will receive the Pinecone API key via a web message. Select this option if you are using the [@pinecone-database/connect library](/integrations/build-integration/connect-your-users-to-pinecone#javascript). The API key will only be provided to the allowed origin(s) specified below.
     * **Copy/Paste**: The API key will display in the success message, and users will need to copy and paste their Pinecone API keys into your application.

   * **Allowed origin**: If you selected **Web Message** as your **Return mechanism**, list the URL origin(s) where your integration is hosted. The [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) is the part of the URL that specifies the protocol, hostname, and port.

3. Click **Create**.

<Note>
  Anyone can create an integration, but [becoming an official Pinecone partner](/integrations/build-integration/become-a-partner) can help accelerate your go-to-market and add value to your customers.
</Note>


## Custom object

[Once you have created your `integrationId`](#create-an-integration-id), you can create a custom object, like a button or link, that loads a **Connect to Pinecone** popup that displays as follows:

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f8fd4a551afc7bf73657dc8af27c214f" alt="Connect popup" data-og-width="624" width="624" data-og-height="657" height="657" data-path="images/connect-popup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=52daa926896ec46a4e7d214943a4566b 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=40250701b646e305df925ee05377bd8b 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=db918eb1651a56bb1f1718aaa9188355 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a59d709c3dbf79357cc08c740503feff 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=074b7adcb2c5b4ebc8674df31f3afe9f 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-popup.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=d1a171eb825d863d5c81ee0a736daf39 2500w" />

The `ConnectPopup` function can be called with either the JavaScript library or script. The JavaScript library is the most commonly used method, but the script can be used in instances where you cannot build and use a custom library, like within the constraints of a content management system (CMS).

The function includes the following **required** configuration option:

* `integrationId`: The slug assigned to the integration. If `integrationId` is not passed, the widget will not render.

  <Note>To create a unique `integrationId`, fill out the [Create Integration form](#create-an-integration-id).</Note>

The function returns an object containing the following:

* `open`: A function that opens the popup. Suitable for use as an on-click handler.

Example usage of the library and script:

<CodeGroup>
  ```javascript JavaScriptlibrary theme={null}
  import { ConnectPopup } from '@pinecone-database/connect'

  /*  Define a function called connectWithAPIKey */
  const connectWithAPIKey = () => {
    return new Promise((resolve, reject) => {
      /* Call ConnectPopup function with an object containing options */
      const popup = ConnectPopup({
        onConnect: (key) => {
          resolve(key);
        },
        integrationId: 'myApp'
      }).open();
    });
  };

  /* Handle button click event */
  document.getElementById('connectButton').addEventListener('click', () => {
    connectWithAPIKey()
      .then(apiKey => {
        console.log("API Key:", apiKey);
      })
      .catch(error => {
        console.error("Error:", error);
      });
  });
  ```

  ```html JavaScript script theme={null}
  <head>
  ...
  <script src="https://connect.pinecone.io/embed.js"></script>
  <script>
    const pineconePopup = ConnectPopup({
      onConnect: (key) => console.log(key),
      onCancel: () => console.log("Cancelled"),
      integrationId: 'myApp'
    });
  </script>
  ...
  </head>
  <body>
  ...
  <button onclick="pineconePopup.open()">Connect to Pinecone!</button>
  ...
  </body>
  ```
</CodeGroup>

Once you have created your integration, be sure to [attribute usage to your integration](/integrations/build-integration/attribute-usage-to-your-integration).


## Pre-built widget

The pre-built **Connect** widget displays as follows:

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=83c1d4eea967cabb4eef94ace9088943" alt="Connect widget" data-og-width="514" width="514" data-og-height="192" height="192" data-path="images/connect-widget.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=d7c1d97bdb81c2542cf83676b8349faa 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=d153f812aad16c9d59a202000eddddfd 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=b55b5cf20017205db4e78ee6fb963a9e 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=a214f92f4f9689d8d53e4d7407182b89 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=4cde4082bde874f202bea09125632cb0 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/connect-widget.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=f739d78c95b0ef344f850e25a0f02e60 2500w" />

[Once you have created your `integrationId`](#create-an-integration-id), you can embed the **Connect** widget multiple ways:

* [JavaScript](#javascript) library (`@pinecone-database/connect`) or script: Renders the widget in apps and websites.
* [Colab](#colab) (`pinecone-notebooks`): Renders the widget in Colab notebooks using Python.

Once you have created your integration, be sure to [attribute usage to your integration](/integrations/build-integration/attribute-usage-to-your-integration).

### JavaScript

To embed the **Connect to Pinecone** widget in your app or website using the [`@pinecone-database/connect` library](https://www.npmjs.com/package/@pinecone-database/connect), install the necessary dependencies:

```shell Shell theme={null}

# Install dependencies
npm i -S @pinecone-database/connect
```

You can use the JavaScript library to render the **Connect to Pinecone** widget and obtain the API key with the [`connectToPinecone` function](#connecttopinecone-function). It displays the widget and calls the provided callback function with the Pinecone API key, once the user completes the flow.

The function includes the following **required** configuration options:

* `integrationId`: The slug assigned to the integration. If `integrationId` is not passed, the widget will not render.

  <Note>To create a unique `integrationId`, [fill out the Create Integration form](#create-an-integration-id) with Pinecone.</Note>

* `container`: The HTML element where the **Connect** widget will render.

Example usage:

```JavaScript JavaScript theme={null}
import {connectToPinecone} from '@pinecone-database/connect'

const setupPinecone = (apiKey) => { /* Set up a Pinecone client using the API key */ }

connectToPinecone(
  setupPinecone,
  {
    integrationId: 'myApp',
    container: document.getElementById('connect-widget')
  }
)
```

If you cannot use the JavaScript library, you can directly call the script. For example:

```html HTML theme={null}
<head>
  ...
  <script src="https://connect.pinecone.io/embed.js">
  ...
</head>
<body>

<div id="widgetContainer"></div>
...

<script>
  connectToPinecone(
    (apiKey) => {/* Use the apiKey to create an index*/},
    {
      integrationId: 'myApp',
      container: document.getElementById('widgetContainer'),
    }
  );
</script>

...
</body>
```

### Colab

To embed the **Connect** widget in your Colab notebook, use the [`pinecone-notebooks` Python library](https://pypi.org/project/pinecone-notebooks/#description):

```shell  theme={null}

# Install dependencies using Colab syntax

pip install -qU pinecone-notebooks pinecone[grpc]
```

```python  theme={null}

# Render the Connect widget for the user to authenticate and generate an API key

from pinecone_notebooks.colab import Authenticate

Authenticate()


# The generated API key is available in the PINECONE_API_KEY environment variable

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os

api_key = os.environ.get('PINECONE_API_KEY')


# Use the API key to initialize the Pinecone client
pc = Pinecone(api_key=api_key)
```

<Tip>
  To see this flow in practice, see our [example notebook](https://colab.research.google.com/drive/1VZ-REFRbleJG4tfJ3waFIrSveqrYQnNx?usp=sharing).
</Tip>


## Manage generated API keys

Your users can [manage the API keys](/guides/projects/manage-api-keys) generated by your integration in the Pinecone console.



# Create an API key
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/create_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml post /admin/projects/{project_id}/api-keys
Create a new API key for a project. Developers can use the API key to authenticate requests to Pinecone's Data Plane and Control Plane APIs.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X POST "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -d '{ 
             "name": "example-api-key", 
             "roles": ["ProjectEditor"] 
           }'
  ```

  ```bash CLI theme={null}
  # Target the project for which you want to create an API key.
  pc target -o "example-org" -p "example-project"
  # Create the API key
  pc api-key create -n "example-api-key" --roles ProjectEditor
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "key": {
      "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
      "name": "example-api-key",
      "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
      "roles": [
        "ProjectEditor"
      ],
      "created_at": "2025-10-20T23:40:27.069075Z"
    },
    "value": "..."
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE     VALUE
  Name          example-api-key
  ID            62b0dbfe-3489-4b79-b850-34d911527c88
  Value         ...
  Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
  Roles         ProjectEditor
  ```
</ResponseExample>



# Create a new project
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/create_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml post /admin/projects
Creates a new project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X POST "https://api.pinecone.io/admin/projects" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -d '{ "name":"example-project" }'
  ```

  ```bash CLI theme={null}
  # Target the organization for which you want to create 
  # a project.
  pc target -o "example-org"
  # Create the project.
  pc project create -n "example-project"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "example-project",
    "max_pods": 20,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-20T20:16:09.144497Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                example-project
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-20 20:19:51.448431 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</ResponseExample>



# Delete an API key
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/delete_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml delete /admin/api-keys/{api_key_id}
Delete an API key from a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X DELETE "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```

  ```bash CLI theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

  # Delete the API key. Use --skip-confirmation to skip 
  # the confirmation prompt.
  pc api-key delete -i $PINECONE_API_KEY_ID
  ```
</RequestExample>

<ResponseExample>
  ```text curl theme={null}
  No response payload
  ```

  ```text CLI theme={null}
  [WARN] This operation will delete API key example-api-key from project example-project.
  [WARN] Any integrations that authenticate with this API key will immediately stop working.
  [WARN] This action cannot be undone.
  Do you want to continue? (y/N): y
  [INFO] You chose to continue delete.
  [SUCCESS] API key example-api-key deleted
  ```
</ResponseExample>



# Delete a project
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/delete_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml delete /admin/projects/{project_id}
Delete a project and all its associated configuration.
Before deleting a project, you must delete all indexes, assistants, backups, and collections associated with the project. Other project resources, such as API keys, are automatically deleted when the project is deleted.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X DELETE "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN"
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Delete the project. Use --skip-confirmation to skip 
  # the confirmation prompt.
  pc project delete -i $PINECONE_PROJECT_ID
  ```
</RequestExample>

<ResponseExample>
  ```text curl theme={null}
  No response payload
  ```

  ```text CLI theme={null}
  [WARN] This will delete the project example-project in organization Pinecone Mesh.
  [WARN] This action cannot be undone.
  Do you want to continue? (y/N): y
  [INFO] You chose to continue delete.
  [SUCCESS] Project example-project deleted.
  ```
</ResponseExample>



# Get API key details
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/fetch_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/api-keys/{api_key_id}
Get the details of an API key, excluding the API key secret.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "accept: application/json" \
       -H "X-Pinecone-Api-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

  pc api-key describe -i $PINECONE_API_KEY_ID
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
    "name": "example-api-key",
    "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "roles": [
      "ProjectEditor"
    ],
    "created_at": "2025-10-22T19:27:21.202955Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE     VALUE
  Name          example-api-key
  ID            62b0dbfe-3489-4b79-b850-34d911527c88622094031e06
  Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
  Roles         ProjectEditor
  ```
</ResponseExample>



# Get project details
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/fetch_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects/{project_id}
Get details about a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "accept: application/json" 
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Fetch the project details.
  pc project describe -i $PINECONE_PROJECT_ID
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "example-project",
    "max_pods": 5,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-16T23:32:18.014693Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                example-project
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-16 23:32:18.014693 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</ResponseExample>



# List API keys
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/list_api_keys

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects/{project_id}/api-keys
List all API keys in a project.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID/api-keys" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  pc api-key list -i $PINECONE_PROJECT_ID
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
        "name": "example-api-key",
        "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "roles": [
          "ProjectEditor"
        ],
        "created_at": "2025-10-20T23:39:43.665754Z"
      },
      {
        "id": "0d0d3678-81b4-4e0d-a4f0-70ba488acfb7",
        "name": "example-api-key-2",
        "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "roles": [
          "ProjectEditor"
        ],
        "created_at": "2025-10-20T23:43:13.176422Z"
      }
    ]
  }
  ```

  ```text CLI theme={null}
  Organization: example-organization (ID: -NM7af6f234168c4e44a)
  Project: example-project (ID: 32c8235a-5220-4a80-a9f1-69c24109e6f2)

  API Keys

  NAME                 ID                                      PROJECT ID                              ROLES
  example-api-key      62b0dbfe-3489-4b79-b850-34d911527c88    32c8235a-5220-4a80-a9f1-69c24109e6f2    ProjectEditor
  example-api-key-2    0d0d3678-81b4-4e0d-a4f0-70ba488acfb7    32c8235a-5220-4a80-a9f1-69c24109e6f2    ProjectEditor
  ```
</ResponseExample>



# List projects
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/list_projects

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml get /admin/projects
List all projects in an organization.

<RequestExample>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X GET "https://api.pinecone.io/admin/projects" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04"
  ```

  ```bash CLI theme={null}
  # Target the organization for which you want to list 
  # projects.
  pc target -o "example-org"
  # List projects in the target organization  
  pc project list
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "data": [
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "example-project",
        "max_pods": 20,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-10-20T20:16:09.144497Z"
      }
      {
        "id": "f060b981-6e6e-48a8-9f82-63b9610cc139",
        "name": "example-project-2",
        "max_pods": 20,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-07-01T13:45:00.357928Z"
      }
    ]
  }
  ```

  ```text CLI theme={null}
  NAME               ID                                     ORGANIZATION ID        CREATED AT                             FORCE ENCRYPTION   MAX PODS
  example-project    32c8235a-5220-4a80-a9f1-69c24109e6f2   -NM7af6f234168c4e44a   2025-10-20 20:19:51.448431 +0000 UTC   false              20 
  example-project-2  f060b981-6e6e-48a8-9f82-63b9610cc139   -NM7af6f234168c4e44a   2024-10-16 14:24:35.170627 +0000 UTC   false              20
  ```
</ResponseExample>



# Update an API key
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/update_api_key

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml patch /admin/api-keys/{api_key_id}
Update the name and roles of an API key.


<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X PATCH "https://api.pinecone.io/admin/api-keys/$PINECONE_API_KEY_ID" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -d '{
             "name": "new-api-key-name",
             "roles": ["ProjectEditor"]
           }'
  ```

  ```bash CLI theme={null}
  PINECONE_API_KEY_ID="62b0dbfe-3489-4b79-b850-34d911527c88"

  # Target the organization that contains the API key.
  pc target -o "example-org" 
  # Update the API key name.
  pc api-key update -i $PINECONE_API_KEY_ID -n "new-api-key-name"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "62b0dbfe-3489-4b79-b850-34d911527c88",
    "name": "new-api-key-name",
    "project_id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "roles": [
      "ProjectEditor"
    ],
    "created_at": "2025-10-22T19:27:21.202955Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE     VALUE
  Name          new-api-key-name
  ID            62b0dbfe-3489-4b79-b850-34d911527c88
  Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
  Roles         ProjectEditor
  ```
</ResponseExample>



# Update a project
Source: https://docs.pinecone.io/reference/api/2025-04/admin-assistant/update_project

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/admin_2025-04.oas.yaml patch /admin/projects/{project_id}
Update a project's configuration details.
You can update the project's name, maximum number of Pods, or enable encryption with a customer-managed encryption key (CMEK).


<RequestExample>
  ```bash curl theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

  curl -X PATCH "https://api.pinecone.io/admin/projects/$PINECONE_PROJECT_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "accept: application/json" \
       -H "Content-Type: application/json" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -d '{ "name": "new-project-name" }'
  ```

  ```bash CLI theme={null}
  PINECONE_PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Update the project name.
  pc project update -i $PINECONE_PROJECT_ID -n "new-project-name"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "new-project-name",
    "max_pods": 5,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-20T20:19:51.448431Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                new-project-name
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-20 20:19:51.448431 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</ResponseExample>



# Chat with an assistant
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/chat_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml post /chat/{assistant_name}
Chat with an assistant and get back citations in structured form. 

This is the recommended way to chat with an assistant, as it offers more functionality and control over the assistant's responses and references than the OpenAI-compatible chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

<RequestExample>
  ```python Python | Default theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="What is the inciting incident of Pride and Prejudice?")
  resp = assistant.chat(messages=[msg])

  print(resp)
  ```

  ```python Python | Streaming theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  msg = Message(role="user", content="What is the inciting incident of Pride and Prejudice?")

  chunks = assistant.chat(messages=[msg], stream=True)

  for chunk in chunks:
      if chunk:
          print(chunk)
  ```

  ```javascript JavaScript | Default theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chat({
    messages: [{ role: 'user', content: 'What is the inciting incident of Pride and Prejudice?' }]
  });
  console.log(chatResp);
  ```

  ```javascript JavaScript | Streaming theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatStream({
        messages: [{ role: 'user', content: 'What is the inciting incident of Pride and Prejudice?' }]
      });
  for await (const response of chatResp) {
      if (response) {
          console.log(response);
      }
  }
  ```

  ```bash curl | Default theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the inciting incident of Pride and Prejudice?"
      }
    ],
    "stream": false,
    "model": "gpt-4o"
  }'
  ```

  ```bash curl | Streaming theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-01" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the inciting incident of Pride and Prejudice?"
      }
    ],
    "stream": true,
    "model": "gpt-4o"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json Default response theme={null}
  {
    "finish_reason": "stop",
    "message": {
      "role": "assistant",
      "content": "The inciting incident of \"Pride and Prejudice\" occurs when Mrs. Bennet informs Mr. Bennet that Netherfield Park has been let at last, and she is eager to share the news about the new tenant, Mr. Bingley, who is wealthy and single. This sets the stage for the subsequent events of the story, including the introduction of Mr. Bingley and Mr. Darcy to the Bennet family and the ensuing romantic entanglements."
    },
    "id": "00000000000000004ac3add5961aa757",
    "model": "gpt-4o-2024-05-13",
    "usage": {
      "prompt_tokens": 9736,
      "completion_tokens": 105,
      "total_tokens": 9841
    },
    "citations": [
      {
        "position": 406,
        "references": [
          {
            "file": {
              "status": "Available",
              "id": "ae79e447-b89e-4994-994b-3232ca52a654",
              "name": "Pride-and-Prejudice.pdf",
              "size": 2973077,
              "metadata": null,
              "updated_on": "2024-06-14T15:01:57.385425746Z",
              "created_on": "2024-06-14T15:01:02.910452398Z",
              "percent_done": 0,
              "signed_url": "https://storage.googleapis.com/...",
              "error_message": null
            },
            "pages": [
              1
            ]
          }
        ]
      }
    ]
  }

  ```

  ```shell Streaming response theme={null}
  data:{
    "type":"message_start",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "role":"assistant"
  }

  data:
  {
    "type":"content_chunk",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "delta":
    {
      "content":"The"
      }
  }

  ...

  data:
  {
    "type":"citation",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "citation":
    {
      "position":406,
      "references":
      [
        {
          "file":{
            "status":"Available",
            "id":"ae79e447-b89e-4994-994b-3232ca52a654",
            "name":"Pride-and-Prejudice.pdf",
            "size":2973077,
            "metadata":null,
            "updated_on":"2024-06-14T15:01:57.385425746Z", 
            "created_on":"2024-06-14T15:01:02.910452398Z",
            "percent_done":0.0,
            "signed_url":"https://storage.googleapis.com/...",
            "error_message":null
            }, 
        "pages":[1]
        }
      ]
    }
  }

  data:
  {
    "type":"message_end",
    "id":"0000000000000000111b35de85e8a8f9",
    "model":"gpt-4o-2024-05-13",
    "finish_reason":"stop",
    "usage":
    {
      "prompt_tokens":9736,
      "completion_tokens":102,
      "total_tokens":9838
      }
  }
  ```
</ResponseExample>



# Chat through an OpenAI-compatible interface
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/chat_completion_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml post /chat/{assistant_name}/chat/completions
Chat with an assistant. This endpoint is based on the OpenAI Chat Completion API, a commonly used and adopted API. 

It is useful if you need inline citations or OpenAI-compatible responses, but has limited functionality compared to the standard chat interface.

For guidance and examples, see [Chat with an assistant](https://docs.pinecone.io/guides/assistant/chat-with-assistant).

<RequestExample>
  ```python Python | Default theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Chat with the assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  response = assistant.chat_completions(messages=chat_context)
  ```

  ```python Python | Streaming theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  from pinecone_plugins.assistant.models.chat import Message

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant" 
  )

  # Streaming chat with the Assistant.
  chat_context = [Message(role="user", content="What is the maximum height of a red pine?")]
  chunks = assistant.chat_completions(messages=[chat_context], stream=True, model="gpt-4o")

  for chunk in chunks:
      if chunk:
          print(chunk)
  ```

  ```javascript JavaScript | Default theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletion({
        messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }]
      });
  console.log(JSON.stringify(chatResp.choices[0].message, null, 2));
  ```

  ```javascript JavaScript | Streaming theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const chatResp = await assistant.chatCompletionStream({
        messages: [{ role: 'user', content: 'What is the maximum height of a red pine?' }]
      });

  for await (const response of chatResp) {
      if (response) {
          console.log(response);
      }
  }
  ```

  ```bash curl | Default theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ]
  }'
  ```

  ```bash curl | Streaming theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/chat/completions" \
    -H "Api-Key: $PINECONE_API_KEY "\
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-01" \
    -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the maximum height of a red pine?"
      }
    ],
    "stream": true
  }'
  ```
</RequestExample>

<ResponseExample>
  ```JSON Default response theme={null}
  {"chat_completion":
    {
      "id":"chatcmpl-9OtJCcR0SJQdgbCDc9JfRZy8g7VJR",
      "choices":[
        {
          "finish_reason":"stop",
          "index":0,
          "message":{
            "role":"assistant",
            "content":"The maximum height of a red pine (Pinus resinosa) is up to 25 meters."
          }
        }
      ],
      "model":"my_assistant"
    }
  }
  ```

  ```shell Streaming response theme={null}
  {
    'id': '000000000000000009de65aa87adbcf0', 
    'choices': [
        {
        'index': 0, 
        'delta': 
          {
          'role': 'assistant', 
          'content': 'The'
          }, 
        'finish_reason': None
        }
      ], 
    'model': 'gpt-4o-2024-05-13'
  }

  ...

  {
    'id': '00000000000000007a927260910f5839',
    'choices': [
        {
        'index': 0,
        'delta':
          {
            'role': '', 
            'content': 'The'
          }, 
        'finish_reason': None
        }
      ], 
    'model': 'gpt-4o-2024-05-13'
  }

  ...

  {
    'id': '00000000000000007a927260910f5839', 
    'choices': [
      {
        'index': 0, 
        'delta': 
          {
          'role': None, 
          'content': None
          }, 
        'finish_reason': 'stop'
        }
      ], 
    'model': 'gpt-4o-2024-05-13'
  }
  ```
</ResponseExample>



# Retrieve context from an assistant
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/context_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml post /chat/{assistant_name}/context
Retrieve context snippets from an assistant to use as part of RAG or any agentic flow.

For guidance and examples, see [Retrieve context snippets](https://docs.pinecone.io/guides/assistant/retrieve-context-snippets).

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")
  assistant = pc.assistant.Assistant(assistant_name="example-assistant")

  response = assistant.context(query="Who is the CFO of Netflix?")

  for snippet in response.snippets:
      print(snippet)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const response = await assistant.context({
    query: 'Who is the CFO of Netflix?',
  });
  console.log(response);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl "https://prod-1-data.ke.pinecone.io/assistant/chat/$ASSISTANT_NAME/context" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "query": "Who is the CFO of Netflix?"
  }'
  ```
</RequestExample>

<ResponseExample>
  ```json JSON theme={null}
  {
      "snippets":
      [
          {
              "type":"text",
              "content":"EXHIBIT 31.3\nCERTIFICATION OF CHIEF FINANCIAL OFFICER\nPURSUANT TO SECTION 302 OF THE SARBANES-OXLEY ACT OF 2002\nI, Spencer Neumann, certify that: ...",
              "score":0.9960699,
              "reference":
              {
                  "type":"pdf",
                  "file":
                  {
                      "status":"Available","id":"e6034e51-0bb9-4926-84c6-70597dbd07a7",
                      "name":"Netflix-10-K-01262024.pdf", 
                      "size":1073470,
                      "metadata":null,
                      "updated_on":"2024-11-21T22:59:10.426001030Z",
                      "created_on":"2024-11-21T22:58:35.879120257Z", 
                      "percent_done":1.0,
                      "signed_url":"https://storage.googleapis.com...",
                      "error_message":null
                      },
                  "pages":[78]
              }
          },
  {
      "type":"text",
      "content":"EXHIBIT 32.1\n..."
  ...
  ```
</ResponseExample>



# Create an assistant
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/create_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_control_2025-04.oas.yaml post /assistants
Create an assistant. This is where you specify the underlying training model, which cloud provider you would like to deploy with, and more.

For guidance and examples, see [Create an assistant](https://docs.pinecone.io/guides/assistant/create-assistant)

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.create_assistant(
      assistant_name="example-assistant",
      instructions="Use American English for spelling and grammar.",
      region="us", # Region to deploy assistant. Options: "us" (default) or "eu".
      timeout=30 # Maximum seconds to wait for assistant status to become "Ready" before timing out.
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistant = await pc.createAssistant({
    name: 'example-assistant',
    instructions: 'Use American English for spelling and grammar.',
    region: 'us'
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "name": "example-assistant",
    "instructions": "Use American English for spelling and grammar.",
    "region":"us"
  }'
  ```
</RequestExample>



# Delete an assistant
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/delete_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_control_2025-04.oas.yaml delete /assistants/{assistant_name}
Delete an existing assistant.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#delete-an-assistant)

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  pc.assistant.delete_assistant(
      assistant_name="example-assistant", 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  await pc.deleteAssistant('example-assistant');
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X DELETE "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \ 
    -H "X-Pinecone-API-Version: 2025-04" 
  ```
</RequestExample>



# Delete an uploaded file
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/delete_file

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml delete /files/{assistant_name}/{assistant_file_id}
Delete an uploaded file from an assistant.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#delete-a-file).

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Delete a file from your assistant.
  assistant.delete_file(file_id="070513b3-022f-4966-b583-a9b12e0290ff")
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);

  const file = await assistant.deleteFile("070513b3-022f-4966-b583-a9b12e0290ff")
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="070513b3-022f-4966-b583-a9b12e0290ff"

  curl -X DELETE "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>



# Check assistant status
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/describe_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_control_2025-04.oas.yaml get /assistants/{assistant_name}
Get the status of an assistant.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#get-the-status-of-an-assistant)

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  assistant = pc.assistant.describe_assistant(
      assistant_name="example-assistant", 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistant = await pc.describeAssistant('example-assistant');
  console.log(assistant);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \ 
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>



# Describe a file upload
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/describe_file

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml get /files/{assistant_name}/{assistant_file_id}
Get the status and metadata of a file uploaded to an assistant.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#get-the-status-of-a-file).

<RequestExample>
  ```python Python theme={null}
  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get an assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `True`.
  file = assistant.describe_file(file_id="3c90c3cc-0d44-4b50-8888-8dd25736052a", include_url=True)
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const fileId = "3c90c3cc-0d44-4b50-8888-8dd25736052a";

  // Describe a file. Returns a signed URL by default. 
  const file = await assistant.describeFile(fileId)
  // To exclude signed URL, set `includeUrl` to `false`.
  // const includeUrl = false;
  // const file = await assistant.describeFile(fileId, includeUrl)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `true`.
  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID?include_url=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>



# List assistants
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/list_assistants

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_control_2025-04.oas.yaml get /assistants
List of all assistants in a project.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#list-assistants-for-a-project).

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  assistants = pc.assistant.list_assistants()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistants = await pc.listAssistants();
  console.log(assistants);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/assistant/assistants" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>



# List Files
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/list_files

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml get /files/{assistant_name}
List all files in an assistant, with an option to filter files with metadata.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#list-files-in-an-assistant).

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get your assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # List files in your assistant.
  files = assistant.list_files()
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });
  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  const files = await assistant.listFiles();
  console.log(files);
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-04"
  ```
</RequestExample>



# Evaluate an answer
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/metrics_alignment

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_evaluation_2025-04.oas.yaml post /evaluation/metrics/alignment
Evaluate the correctness and completeness of a response from an assistant or a RAG system. The correctness and completeness are evaluated based on the precision and recall of the generated answer with respect to the ground truth answer facts. Alignment is the harmonic mean of correctness and completeness.

For guidance and examples, see [Evaluate answers](https://docs.pinecone.io/guides/assistant/evaluate-answers).

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant
  # pip install requests

  import requests
  from pinecone_plugins.assistant.models.chat import Message

  qa_data = {
          "question": "What are the capital cities of France, England and Spain?",
          "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain"
      }

  for qa in qa_data:
      chat_context = [Message(role="user", content=qa["question"])]
      response = assistant.chat(messages=chat_context)
      
      answer = response.message.content # The answer from the Assistant - see https://docs.pinecone.io/guides/assistant/chat-with-assistant
      
      eval_data = {
          "question": qa["question"],
          "answer": answer,
          "ground_truth_answer": qa["ground_truth_answer"]
      }

      response = requests.post(
          "https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment",
          headers={
              "Api-Key": os.environ["PINECONE_API_KEY"],
              "Content-Type": "application/json"
          },
          json=eval_data
      )

  print(response.text)
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://prod-1-data.ke.pinecone.io/assistant/evaluation/metrics/alignment \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
      "question": "What are the capital cities of France, England and Spain?",
      "answer": "Paris is the capital city of France and Barcelona of Spain",
      "ground_truth_answer": "Paris is the capital city of France, London of England and Madrid of Spain"
  }'
  ```
</RequestExample>



# Update an assistant
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/update_assistant

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_control_2025-04.oas.yaml patch /assistants/{assistant_name}
Update an existing assistant. You can modify the assistant's instructions.

For guidance and examples, see [Manage assistants](https://docs.pinecone.io/guides/assistant/manage-assistants#add-instructions-to-an-assistant).

<RequestExample>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key=YOUR_API_KEY)

  assistant = pc.assistant.update_assistant(
      assistant_name="test", 
      instructions="Use American English for spelling and grammar.",
      region="us" # Region to deploy assistant. Options: "us" (default) or "eu".
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  await pc.updateAssistant('example-assistant', {
    instructions: 'Use American English for spelling and grammar.',
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"

  curl -X PATCH "https://api.pinecone.io/assistant/assistants/$ASSISTANT_NAME" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-API-Version: 2025-04" \
    -d '{
    "instructions": "Use American English for spelling and grammar.",
    "region":"us"
  }'
  ```
</RequestExample>



# Upload file to assistant
Source: https://docs.pinecone.io/reference/api/2025-04/assistant/upload_file

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/assistant_data_2025-04.oas.yaml post /files/{assistant_name}
Upload a file to the specified assistant.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#upload-a-local-file).

<RequestExample>
  ```Python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone
  pc = Pinecone(api_key="YOUR_API_KEY")

  # Get the assistant.
  assistant = pc.assistant.Assistant(
      assistant_name="example-assistant", 
  )

  # Upload a file from a local path.
  response = assistant.upload_file(
      file_path="/Users/jdoe/Downloads/example_file.txt",
      metadata={"published": "2024-01-01", "document_type": "manuscript"},
      timeout=None
  )

  # Upload from an in-memory binary stream.
  from io import BytesIO

  # Create a BytesIO stream with some content.
  md_text = "# Title\n\ntext"
  stream = BytesIO(md_text.encode("utf-8"))

  # Upload the stream.
  response_bytes_stream = assistant.upload_bytes_stream(
      stream=stream,
      file_name="example_file.md",
      timeout=None
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone'

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  const assistantName = 'example-assistant';
  const assistant = pc.Assistant(assistantName);
  await assistant.uploadFile({
    path: '/Users/jdoe/Downloads/example_file.txt',
    metadata: { 'published': '2024-01-01', 'document_type': 'manuscript' },
  });
  ```

  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  ENCODED_METADATA="%7B%22published%22%3A%222024-01-01%22%2C%22document_type%22%3A%22script%22%7D" # URL encoded metadata - See w3schools.com/tags/ref_urlencode.ASP
  LOCAL_FILE_PATH="/Users/jdoe/Downloads/example_file.txt"

  curl -X "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME?metadata=$ENCODED_METADATA" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -F "file=@$LOCAL_FILE_PATH"
  ```
</RequestExample>

<ResponseExample>
  ```json  theme={null}
  {
    "name": "example-file.txt",
    "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
    "metadata": "{ 'published': '2024-01-01', 'document_type': 'manuscript' }",
    "created_on": "2023-11-07T05:31:56Z",
    "updated_on": "2023-11-07T05:31:56Z",
    "status": "Processing",
    "percent_done": 50,
    "signed_url": "https://storage.googleapis.com/bucket/file.pdf",
    "error_message": "<string>"
  }
  ```
</ResponseExample>



# Pinecone Assistant limits
Source: https://docs.pinecone.io/reference/api/assistant/assistant-limits



Pinecone Assistant limits vary based on [subscription plan](https://www.pinecone.io/pricing/).

### Object limits

Object limits are restrictions on the number or size of assistant-related objects.

| Metric                               | Starter plan  | Standard plan | Enterprise plan |
| :----------------------------------- | :------------ | :------------ | :-------------- |
| Assistants per project               | 5             | Unlimited     | Unlimited       |
| File storage per project             | 1 GB          | Unlimited     | Unlimited       |
| Chat input tokens per project        | 1,500,000     | Unlimited     | Unlimited       |
| Chat output tokens per project       | 200,000       | Unlimited     | Unlimited       |
| Context retrieval tokens per project | 500,000       | Unlimited     | Unlimited       |
| Evaluation input tokens per project  | Not available | 150,000       | 500,000         |
| Files per assistant                  | 100           | 10,000        | 10,000          |
| File size (.docx, .json, .md, .txt)  | 10 MB         | 10 MB         | 10 MB           |
| File size (.pdf)                     | 10 MB         | 100 MB        | 100 MB          |
| Metadata size per file               | 16 KB         | 16 KB         | 16 KB           |

Additionally, the following limits apply to [multimodal PDFs](/guides/assistant/multimodal) (currently in [public preview](/release-notes/feature-availability)):

| Metric                        | Starter plan | Standard plan | Enterprise plan |
| :---------------------------- | :----------- | :------------ | :-------------- |
| Max file size                 | 10 MB        | 50 MB         | 50 MB           |
| Page limit                    | 100          | 100           | 100             |
| Multimodal PDFs per assistant | 1            | 20            | 20              |

### Rate limits

Rate limits help protect your applications from misuse and maintain the health of our shared infrastructure. These limits are designed to support typical production workloads while ensuring reliable performance for all users.

**Most rate limits can be adjusted upon request.** If you need higher limits to scale your application, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) with details about your use case.

Requests that exceed a rate limit fail and return a `429 - TOO_MANY_REQUESTS` status.

<Tip>To handle rate limits, implement [retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic).</Tip>

| Metric                                      | Starter plan | Standard plan | Enterprise plan |
| :------------------------------------------ | :----------- | :------------ | :-------------- |
| Assistant list/get requests per minute      | 40           | 100           | 500             |
| Assistant create/update requests per minute | 20           | 50            | 100             |
| Assistant delete requests per minute        | 20           | 50            | 100             |
| File list/get requests per minute           | 100          | 300           | 6000            |
| File upload requests per minute             | 5            | 20            | 300             |
| File delete requests per minute             | 5            | 20            | 300             |
| Chat input tokens per minute                | 100,000      | 300,000       | 1,000,000       |
| Chat history tokens per query               | 64,000       | 64,000        | 64,000          |



# Authentication
Source: https://docs.pinecone.io/reference/api/assistant/authentication



All requests to the [Pinecone Assistant API](/reference/api/assistant/introduction) must contain a valid [API key](/guides/production/security-overview#api-keys) for the target project.


## Get an API key

[Create a new API key](https://app.pinecone.io/organizations/-/projects/-/keys) in the Pinecone console, or use the connect widget below to generate a key.

<div style={{minWidth: '450px', minHeight:'152px'}}>
  <div id="pinecone-connect-widget">
    <div class="connect-widget-skeleton">
      <div class="skeleton-content" />
    </div>
  </div>
</div>

Copy your generated key:

```
PINECONE_API_KEY="{{YOUR_API_KEY}}"


# This API key has ReadWrite access to all indexes in your project.
```


## Initialize a client

When using a Pinecone SDK, initialize a client object with your API key and then reuse the authenicated client in subsquent function calls. For example:

<CodeGroup>
  ```python Python theme={null}
  # To use the Python SDK, install the plugin:
  # pip install --upgrade pinecone pinecone-plugin-assistant

  from pinecone import Pinecone

  pc = Pinecone(api_key="YOUR_API_KEY")

  # Creates an assistant using the API key stored in the client 'pc'.
  assistant = pc.assistant.create_assistant(
      assistant_name="example-assistant",
      instructions="Use American English for spelling and grammar.",
      region="us" 
  )
  ```

  ```javascript JavaScript theme={null}
  import { Pinecone } from '@pinecone-database/pinecone';

  const pc = new Pinecone({ apiKey: 'YOUR_API_KEY' });

  // Creates an index using the API key stored in the client 'pc'.
  const assistant = await pc.createAssistant({
    name: 'example-assistant',
    instructions: 'Use American English for spelling and grammar.',
    region: 'us'
  });
  ```
</CodeGroup>


## Add headers to an HTTP request

All HTTP requests to the Pinecone Assistant API must contain an `Api-Key` header that specifies a valid [API key](/guides/production/security-overview#api-keys) and must be encoded as JSON with the `Content-Type: application/json` header. For example:

```bash curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl "https://api.pinecone.io/assistant/assistants" \
  -H "Api-Key: $PINECONE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Pinecone-API-Version: 2025-01" \
  -d '{
  "name": "example-assistant",
  "instructions": "Use American English for spelling and grammar.",
  "region":"us"
}'
```



# Assistant API reference
Source: https://docs.pinecone.io/reference/api/assistant/introduction



Use the [Assistant API](/guides/assistant/quickstart) to upload documents, ask questions, and receive responses that reference your documents. This is known as [retrieval-augmented generation (RAG)](https://www.pinecone.io/learn/retrieval-augmented-generation/).


## SDK support

The following Pinecone SDKs support the Assistant API:

<CardGroup cols={3}>
  <Card title="Python SDK" icon="python" href="/reference/python-sdk" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/node-sdk" />
</CardGroup>


## Versioning

The Assistant API is versioned to ensure that your applications continue to work as expected as the platform evolves. For more details, see [API versioning](/reference/api/versioning) in the Pinecone Database documentation.



# 2022 releases
Source: https://docs.pinecone.io/release-notes/2022




## December 22, 2022

#### Pinecone is now available in Google Cloud Marketplace

You can now [sign up for Pinecone billing through Google Cloud Marketplace](/guides/organizations/manage-billing/upgrade-billing-plan).


## December 6, 2022

#### Organizations are generally available

Pinecone now features [organizations](/guides/organizations/understanding-organizations), which allow one or more users to control billing and project settings across multiple projects owned by the same organization.

#### p2 pod type is generally available

The [p2 pod type](/guides/index-data/indexing-overview#p2-pods) is now generally available and ready for production workloads. p2 pods are now available in the Starter plan and support the [dotproduct distance metric](/guides/index-data/create-an-index#dotproduct).

#### Performance improvements

* [Bulk vector\_deletes](/guides/index-data/upsert-data/#deleting-vectors) are now up to 10x faster in many circumstances.
* [Creating collections](/guides/manage-data/back-up-an-index) is now faster.


## October 31, 2022

#### Hybrid search (Early access)

Pinecone now supports keyword-aware semantic search with the new hybrid search indexes and endpoints. Hybrid search enables improved relevance for semantic search results by combining them with keyword search.

This is an **early access** feature and is available only by [signing up](https://www.pinecone.io/hybrid-search-early-access/).


## October 17, 2022

#### Status page

The new [Pinecone Status Page](https://status.pinecone.io/) displays information about the status of the Pinecone service, including the status of individual cloud regions and a log of recent incidents.


## September 16, 2022

#### Public collections

You can now create indexes from public collections, which are collections containing public data from real-world data sources. Currently, public collections include the Glue - SSTB collection, the TREC Question classification collection, and the SQuAD collection.


## August 16, 2022

#### Collections (Public preview)("Beta")

You can now \[make static copies of your index]\(/guides/manage-data/back-up-an-index using collections]\(/guides/manage-data/back-up-an-index#pod-based-index-backups-using-collections). After you create a collection from an index, you can create a new index from that collection. The new index can use any pod type and any number of pods. Collections only consume storage.

This is a **public preview** feature and is not appropriate for production workloads.

#### Vertical scaling

You can now [change the size of the pods](/guides/indexes/pods/scale-pod-based-indexes#increase-pod-size) for a live index to accommodate more vectors or queries without interrupting reads or writes. The p1 and s1 pod types are now available in [4 different sizes](/guides/index-data/indexing-overview/#pods-pod-types-and-pod-sizes): `1x`, `2x`, `4x`, and `8x`. Capacity and compute per pod double with each size increment.

#### p2 pod type (Public preview)("Beta")

The new [p2 pod type](/guides/index-data/indexing-overview/#p2-pods) provides search speeds of around 5ms and throughput of 200 queries per second per replica, or approximately 10x faster speeds and higher throughput than the p1 pod type, depending on your data and network conditions.

This is a **public preview** feature and is not appropriate for production workloads.

#### Improved p1 and s1 performance

The [s1](/guides/index-data/indexing-overview/#s1-pods) and [p1](/guides/index-data/indexing-overview/#p1-pods) pod types now offer approximately 50% higher query throughput and 50% lower latency, depending on your workload.


## July 26, 2022

You can now specify a [metadata filter](/guides/index-data/indexing-overview#metadata/) to get results for a subset of the vectors in your index by calling [describe\_index\_stats](/reference/api/2024-07/control-plane/describe_index) with a [filter](/reference/api/2024-07/control-plane/describe_index#!path=filter\&t=request) object.

The `describe_index_stats` operation now uses the `POST` HTTP request type. The `filter` parameter is only accepted by `describe_index_stats` calls using the `POST` request type. Calls to `describe_index_stats` using the `GET` request type are now deprecated.


## July 12, 2022

#### Pinecone Console Guided Tour

You can now choose to follow a guided tour in the [Pinecone console](https://app.pinecone.io). This interactive tutorial walks you through creating your first index, upserting vectors, and querying your data. The purpose of the tour is to show you all the steps you need to start your first project in Pinecone.


## June 24, 2022

#### Updated response codes

The [create\_index](/reference/api/2024-07/control-plane/create_index), [delete\_index](/reference/api/2024-07/control-plane/delete_index), and `scale_index` operations now use more specific HTTP response codes that describe the type of operation that succeeded.


## June 7, 2022

#### Selective metadata indexing

You can now store more metadata and more unique metadata values! [Select which metadata fields you want to index for filtering](/guides/indexes/pods/manage-pod-based-indexes#selective-metadata-indexing) and which fields you only wish to store and retrieve. When you index metadata fields, you can filter vector search queries using those fields. When you store metadata fields without indexing them, you keep memory utilization low, especially when you have many unique metadata values, and therefore can fit more vectors per pod.

#### Single-vector queries

You can now [specify a single query vector using the vector input](/reference/api/2024-07/data-plane/query/#!path=vector\&t=request). We now encourage all users to query using a single vector rather than a batch of vectors, because batching queries can lead to long response messages and query times, and single queries execute just as fast on the server side.

#### Query by ID

You can now [query your Pinecone index using only the ID for another vector](/reference/api/2024-07/data-plane/query/#!path=id\&t=request). This is useful when you want to search for the nearest neighbors of a vector that is already stored in Pinecone.

#### Improved index fullness accuracy

The index fullness metric in [describe\_index\_stats()](/reference/api/2024-07/control-plane/describe_index#!c=200\&path=indexFullness\&t=response) results is now more accurate.


## April 25, 2022

#### Partial updates (Public preview)

You can now perform a partial update by ID and individual value pairs. This allows you to update individual metadata fields without having to upsert a matching vector or update all metadata fields at once.

#### New metrics

Users on all plans can now see metrics for the past one (1) week in the Pinecone console. Users on the Enterprise plan now have access to the following metrics via the [Prometheus metrics endpoint](/guides/production/monitoring/):

* `pinecone_vector_count`
* `pinecone_request_count_total`
* `pinecone_request_error_count_total`
* `pinecone_request_latency_seconds`
* `pinecone_index_fullness` (Public preview)

**Note:** The accuracy of the `pinecone_index_fullness` metric is improved. This may result in changes from historic reported values. This metric is in public preview.

#### Spark Connector

Spark users who want to manage parallel upserts into Pinecone can now use the [official Spark connector for Pinecone](https://github.com/pinecone-io/spark-pinecone#readme) to upsert their data from a Spark dataframe.

#### Support for Boolean and float metadata in Pinecone indexes

You can now add `Boolean` and `float64` values to [metadata JSON objects associated with a Pinecone index.](/guides/index-data/indexing-overview#metadata)

#### New state field in describe\_index results

The [describe\_index](/reference/api/2024-07/control-plane/describe_index/) operation results now contain a value for `state`, which describes the state of the index. The possible values for `state` are `Initializing`, `ScalingUp`, `ScalingDown`, `Terminating`, and `Ready`.

##### Delete by metadata filter

The [Delete](/reference/api/2024-07/data-plane/delete/) operation now supports filtering my metadata.



---
**Navigation:** [← Previous](./30-use-an-assistant-mcp-server.md) | [Index](./index.md) | [Next →](./32-2023-releases.md)
