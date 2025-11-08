**Navigation:** [← Previous](./12-configure-audit-logs.md) | [Index](./index.md) | [Next →](./14-lexical-search.md)

# Create a project
Source: https://docs.pinecone.io/guides/projects/create-a-project

Create a new Pinecone project in your organization.

This page shows you how to create a project.

If you are an [organization owner or user](/guides/organizations/understanding-organizations#organization-roles), you can create a project in your organization:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**your profile > Organization settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).

    2. Click **+ Create Project**.

    3. Enter a **Name**.

       <Note>
         A project name can contain up to 512 characters. For more information, see [Object identifiers](/reference/api/database-limits#identifier-limits).
       </Note>

    4. (Optional) Tags are key-value pairs that you can use to categorize and identify the project. To add a tag, click **+ Add tag** and enter a tag key and value.

    5. (Optional) Select **Encrypt with Customer Managed Encryption Key**. For more information, see [Configure CMEK](/guides/production/configure-cmek).

    6. Click **Create project**.

       To load an index with a [sample dataset](/guides/data/use-sample-datasets), click **Load sample data** and follow the prompts.

    <Note>
      Organizations on the Starter plan are limited to one project. To create additional projects, [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
    </Note>
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl "https://api.pinecone.io/admin/projects" \
          -H "X-Pinecone-Api-Version: 2025-04" \
      	-H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
      	-d '{
                "name":"example-project"
              }'
      ```

      ```bash CLI theme={null}
      # Target the organization for which you want to 
      # create a project.
      pc target -o "example-org"
      # Create the project and set it as the target 
      # project for the CLI.
      pc project create -n "example-project" --target
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "example-project",
        "max_pods": 0,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-03-16T22:46:45.030Z"
      }
      ```

      ```text CLI theme={null}
      [SUCCESS] Project example-cli-project created successfully.

      ATTRIBUTE           VALUE
      Name                example-project
      ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
      Organization ID     -NM7af6f234168c4e44a
      Created At          2025-10-27 23:27:46.370088 +0000 UTC
      Force Encryption    false
      Max Pods            5

      [SUCCESS] Target project set to example-cli-project
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Next steps

* [Add users to your project](/guides/projects/manage-project-members#add-members-to-a-project)
* [Create an index](/guides/index-data/create-an-index)



# Manage API keys
Source: https://docs.pinecone.io/guides/projects/manage-api-keys

Create and manage API keys with custom permissions.

Each Pinecone [project](/guides/projects/understanding-projects) has one or more API keys. In order to [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.

This page shows you how to [create](#create-an-api-key), [view](#view-api-keys), [change permissions for](#change-api-key-permissions), and [delete](#delete-an-api-key) API keys.

<Warning>
  If you use custom API key permissions, ensure that you [target your index by host](/guides/manage-data/target-an-index#target-by-index-host-recommended) when performing data operations such as `upsert` and `query`.
</Warning>


## Create an API key

You can create a new API key for your project, as follows:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).

    2. Select your project.

    3. Go to **API keys**.

    4. Click **Create API key**.

    5. Enter an **API key name**.

    6. Select the **Permissions** to grant to the API key. For a description of the permission roles, see [API key permissions](/guides/production/security-overview#api-keys).

       <Note>
         Users on the Starter plan can set the permissions to **All** only. To customize the permissions further, [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
       </Note>

    7. Click **Create key**.

    8. Copy and save the generated API key in a secure place for future use.

       <Warning>
         You will not be able to see the API key again after you close the dialog.
       </Warning>

    9. Click **Close**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_PROJECT_ID="YOUR_PROJECT_ID"
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
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
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
    </CodeGroup>
  </Tab>
</Tabs>


## View project API keys

You can [view the API keys](/reference/api/latest/admin/list_api_keys) for your project:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select your project.
    3. Go to the **API keys** tab.

    You will see a list of all API keys for the project, including their names, IDs, and permissions.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
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
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
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
    </CodeGroup>
  </Tab>
</Tabs>


## View API key details

You can [view the details of an API key](/reference/api/latest/admin/fetch_api_key):

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select your project.
    3. Go to the **API keys** tab.
    4. In the row of the API key you want to change, in the **Actions** column, click **ellipsis (...) menu > Settings**.

    You will see the API key's name, ID, and permissions.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
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
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
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
      ID            62b0dbfe-3489-4b79-b850-34d911527c88
      Project ID    32c8235a-5220-4a80-a9f1-69c24109e6f2
      Roles         ProjectEditor
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Update an API key

<Note>
  Users on the Starter plan cannot change API key permissions once they are set. Instead, [create a new API key](#create-an-api-key) or [upgrade to the Standard or Enterprise plan](/guides/organizations/manage-billing/upgrade-billing-plan).
</Note>

If you are a [project owner](/guides/projects/understanding-projects#project-roles), you can update the name and roles of an API key:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).

    2. Select your project.

    3. Go to the **API keys** tab.

    4. In the row of the API key you want to change, in the **Actions** column, click **ellipsis (...) menu > Settings**.

    5. Change the name and/or permissions for the API key as needed.

       For information about the different API key permissions, refer to [Understanding security - API keys](/guides/production/security-overview#api-keys).

    6. Click **Update**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
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
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
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
    </CodeGroup>
  </Tab>
</Tabs>


## Delete an API key

If you are a [project owner](/guides/projects/understanding-projects#project-roles), you can delete your API key:

<Tabs>
  <Tab title="Pinecone console">
    1. Open the [Pinecone console](https://app.pinecone.io/organizations/-/projects).
    2. Select your project.
    3. Go to the **API keys** tab.
    4. In the row of the API key you want to change, in the **Actions** column, click **ellipsis (...) menu > Delete**.
    5. Enter the **API key name**.
    6. Click **Confirm deletion**.

       <Warning>
         Deleting an API key is irreversible and will immediately disable any applications using the API key.
       </Warning>
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/organizations/manage-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/release-notes/feature-availability).
    </Note>

    <CodeGroup>
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
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
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
    </CodeGroup>
  </Tab>
</Tabs>



# Manage project members
Source: https://docs.pinecone.io/guides/projects/manage-project-members

Add and manage project members with role-based access control.

[Organization owners](/guides/organizations/understanding-organizations#organization-roles) or [project owners](#project-roles) can manage members in a project. Members can be added to a project with different [roles](/guides/projects/understanding-projects#project-roles), which determine their permissions within the project.

<Tip>
  For information about managing members at the **organization-level**, see [Manage organization members](/guides/organizations/manage-organization-members).
</Tip>


## Add members to a project

You can add members to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. Enter the member's email address or name.
4. Select a [**Project role**](/guides/projects/understanding-projects#project-roles) for the member. The role determines the member's permissions within Pinecone.
5. Click **Invite**.

When you invite a member to join your project, Pinecone sends them an email containing a link that enables them to gain access to the project. If they already have a Pinecone account, they still receive an email, but they can also immediately view the project.


## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. In the row of the member you want to edit, click **ellipsis (...) menu > Edit role**.
4. Select a [**Project role**](/guides/projects/understanding-projects#project-roles) for the member.
5. Click **Edit role**.


## Remove a member

You can remove a member from a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. In the row of the member you want to remove, click **ellipsis (...) menu > Remove member**.
4. Click **Remove member**.

<Note>
  To remove yourself from a project, click the **Leave project** button in your user's row and confirm.
</Note>



# Manage projects
Source: https://docs.pinecone.io/guides/projects/manage-projects

View, rename, and delete projects in your organization.

This page shows you how to view project details, rename a project, and delete a project.

<Note>
  You must be an [organization owner](/guides/assistant/admin/organizations-overview#organization-roles) or [project owner](/guides/assistant/admin/projects-overview#project-roles) to edit project details or delete a project.
</Note>


## View project details

You can view the details of a project, as in the following example:

<Note>
  An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
</Note>

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
  PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  curl -X GET "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
       -H "Authorization: Bearer $PINECONE_ACCESS_TOKEN" \
       -H "X-Pinecone-Api-Version: 2025-04" \
       -H "accept: application/json"
  ```

  ```bash CLI theme={null}
  PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

  # Target the organization that contains the project.
  pc target -o "example-org" 
  # Fetch the project details.
  pc project describe -i $PROJECT_ID
  ```
</CodeGroup>

The example returns a response like the following:

<CodeGroup>
  ```json curl theme={null}
  {
    "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
    "name": "example-project",
    "max_pods": 5,
    "force_encryption_with_cmek": false,
    "organization_id": "-NM7af6f234168c4e44a",
    "created_at": "2025-10-27T23:27:46.370088Z"
  }
  ```

  ```text CLI theme={null}
  ATTRIBUTE           VALUE
  Name                example-project
  ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
  Organization ID     -NM7af6f234168c4e44a
  Created At          2025-10-27 23:27:46.370088 +0000 UTC
  Force Encryption    false
  Max Pods            5
  ```
</CodeGroup>

<Tip>
  You can view project details using the [Pinecone console](https://app.pinecone.io/organizations/-/settings/projects/-/indexes).
</Tip>


## Rename a project

You can change the name of your project:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**Settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).

    2. Click the **ellipsis (...) menu > Configure** icon next to the project you want to update.

    3. Enter a new **Project Name**.

       <Note>
         A project name can contain up to 512 characters.
       </Note>

    4. Click **Save Changes**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PROJECT_ID="YOUR_PROJECT_ID"
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

      curl -X PATCH "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
           -H "accept: application/json" \
           -H "Content-Type: application/json" \
           -H "X-Pinecone-Api-Version: 2025-04" \
           -d '{
                 "name": "updated-example-project"
               }'
      ```

      ```bash CLI theme={null}
      PROJECT_ID="YOUR_PROJECT_ID"

      # Target the project to update.
      pc target -o "example-org" "example-project"
      # Update the project name.
      pc project update -i $PROJECT_ID -n "updated-example-project"
      ```
    </CodeGroup>

    The example returns a response like the following:

    <CodeGroup>
      ```json curl theme={null}
      {
        "id": "32c8235a-5220-4a80-a9f1-69c24109e6f2",
        "name": "updated-example-project",
        "max_pods": 5,
        "force_encryption_with_cmek": false,
        "organization_id": "-NM7af6f234168c4e44a",
        "created_at": "2025-10-27T23:27:46.370088Z"
      }
      ```

      ```text CLI theme={null}
      [SUCCESS] Project 32c8235a-5220-4a80-a9f1-69c24109e6f2 updated successfully.
      ATTRIBUTE           VALUE
      Name                updated-example-project
      ID                  32c8235a-5220-4a80-a9f1-69c24109e6f2
      Organization ID     -NM7af6f234168c4e44a
      Created At          2025-10-27 23:27:46.370088 +0000 UTC
      Force Encryption    false
      Max Pods            5
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Add project tags

Project tags are key-value pairs that you can use to categorize and identify a project.

To add project tags, use the Pinecone console.

1. In the Pinecone console, go to [**Settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).
2. Click the **ellipsis (...) menu > Configure** icon next to the project you want to update.
3. Click **+ Add tag** and enter a tag key and value. Repeat for each tag you want to add.
4. Click **Save Changes**.

<Tip>
  You can also [add tags to indexes](/guides/manage-data/manage-indexes#configure-index-tags).
</Tip>


## Delete a project

To delete a project, you must first [delete all data](/guides/manage-data/delete-data), [indexes](/guides/manage-data/manage-indexes#delete-an-index), [collections](/guides/indexes/pods/back-up-a-pod-based-index#delete-a-collection), [backups](/guides/manage-data/back-up-an-index#delete-a-backup) and [assistants](/guides/assistant/manage-assistants#delete-an-assistant) associated with the project. Then, you can delete the project itself:

<Tabs>
  <Tab title="Pinecone console">
    1. In the Pinecone console, go to [**Settings > Projects**](https://app.pinecone.io/organizations/-/settings/projects).
    2. For the project you want to delete, click the **ellipsis (...) menu > Delete**.
    3. Enter the project name to confirm the deletion.
    4. Click **Delete Project**.
  </Tab>

  <Tab title="Code">
    <Note>
      An [access token](/guides/assistant/admin/manage-organization-service-accounts#retrieve-an-access-token) must be provided to complete this action through the Admin API. The Admin API is in [public preview](/assistant-release-notes/feature-availability).
    </Note>

    <CodeGroup>
      ```bash curl theme={null}
      PINECONE_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
      PROJECT_ID="32c8235a-5220-4a80-a9f1-69c24109e6f2"

      curl -X DELETE "https://api.pinecone.io/admin/projects/$PROJECT_ID" \
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
    </CodeGroup>
  </Tab>
</Tabs>



# Manage service accounts at the project-level
Source: https://docs.pinecone.io/guides/projects/manage-service-accounts

Enable service accounts for programmatic API access.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows how [organization owners](/guides/organizations/understanding-organizations#organization-roles) and [project owners](/guides/projects/understanding-projects#project-roles) can add and manage service accounts at the project-level. Service accounts enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.


## Add a service account to a project

After a service account has been [added to an organization](/guides/organizations/manage-service-accounts#create-a-service-account), it can be added to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Service accounts** tab](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts).
3. Select the service account to add.
4. Select a [**Project role**](/guides/projects/understanding-projects#project-roles) for the service account. The role determines its permissions within Pinecone.
5. Click **Connect**.


## Change project role

To change a service account's role in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Service accounts** tab](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts).
3. In the row of the service account you want to edit, click **ellipsis (...) menu > Edit role**.
4. Select a [**Project role**](/guides/projects/understanding-projects#project-roles) for the service account.
5. Click **Edit role**.


## Remove a service account from a project

To remove a service account from a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Service accounts** tab](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts).
3. In the row of the service account you want to remove, click **ellipsis (...) menu > Disconnect**.
4. Enter the service account name to confirm.
5. Click **Disconnect**.



# Understanding projects
Source: https://docs.pinecone.io/guides/projects/understanding-projects

Learn about projects, environments, and member roles.

A Pinecone project belongs to an [organization](/guides/organizations/understanding-organizations) and contains a number of [indexes](/guides/index-data/indexing-overview) and users. Only a user who belongs to the project can access the indexes in that project. Each project also has at least one project owner.


## Project environments

You choose a cloud environment for each index in a project. This makes it easy to manage related resources across environments and use the same API key to access them.


## Project roles

If you are an [organization owner](/guides/organizations/understanding-organizations#organization-roles) or project owner, you can manage members in your project. Project members are assigned a role, which determines their permissions within the project. The project roles are as follows:

* **Project owner**: Project owners have global permissions across projects they own.

* **Project user**: Project users have restricted permissions for the specific projects they are invited to.

The following table summarizes the permissions for each project role:

| Permission                  | Owner | User |
| :-------------------------- | ----- | ---- |
| Update project names        | ✓     |      |
| Delete projects             | ✓     |      |
| View project members        | ✓     | ✓    |
| Update project member roles | ✓     |      |
| Delete project members      | ✓     |      |
| View API keys               | ✓     | ✓    |
| Create API keys             | ✓     |      |
| Delete API keys             | ✓     |      |
| View indexes                | ✓     | ✓    |
| Create indexes              | ✓     | ✓    |
| Delete indexes              | ✓     | ✓    |
| Upsert vectors              | ✓     | ✓    |
| Query vectors               | ✓     | ✓    |
| Fetch vectors               | ✓     | ✓    |
| Update a vector             | ✓     | ✓    |
| Delete a vector             | ✓     | ✓    |
| List vector IDs             | ✓     | ✓    |
| Get index stats             | ✓     | ✓    |

Specific to pod-based indexes:

<Warning>
  Customers who sign up for a Standard or Enterprise plan on or after August 18, 2025 cannot create pod-based indexes. Instead, create [serverless indexes](/guides/index-data/create-an-index), and consider using [dedicated read nodes](/guides/index-data/dedicated-read-nodes) for large workloads (millions of records or more, and moderate or high query rates).
</Warning>

| Permission                | Owner | User |
| :------------------------ | ----- | ---- |
| Update project pod limits | ✓     |      |
| View project pod limits   | ✓     | ✓    |
| Update index size         | ✓     | ✓    |


## API keys

Each Pinecone [project](/guides/projects/understanding-projects) has one or more API keys. In order to [make calls to the Pinecone API](/guides/get-started/quickstart), you must provide a valid API key for the relevant Pinecone project.

For more information, see [Manage API keys](/guides/projects/manage-api-keys).


## Project IDs

Each Pinecone project has a unique product ID.

To find the ID of a project, go to the project list in the [Pinecone console](https://app.pinecone.io/organizations/-/projects).


## See also

* [Understanding organizations](guides/organizations/understanding-organizations)
* [Manage organization members](guides/organizations/manage-organization-members)



# Filter by metadata
Source: https://docs.pinecone.io/guides/search/filter-by-metadata

Narrow search results with metadata filtering.

export const word_0 = "vectors"

Every [record](/guides/get-started/concepts#record) in an index must contain an ID and a dense or sparse vector. In addition, you can include [metadata key-value pairs](/guides/index-data/indexing-overview#metadata) to store related information or context. When you search the index, you can then include a metadata filter to limit the search to records matching the filter expression.


## Search with a metadata filter

The following code searches for the 3 records that are most semantically similar to a query and that have a `category` metadata field with the value `digestive system`.

<Tabs>
  <Tab title="Search with text">
    <Note>
      Searching with text is supported only for [indexes with integrated embedding](/guides/index-data/indexing-overview#integrated-embedding).
    </Note>

    <CodeGroup>
      ```python Python theme={null}
      from pinecone import Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      # To get the unique host for an index, 
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      index = pc.Index(host="INDEX_HOST")

      filtered_results = index.search(
          namespace="example-namespace", 
          query={
              "inputs": {"text": "Disease prevention"}, 
              "top_k": 3,
              "filter": {"category": "digestive system"},
          },
          fields=["category", "chunk_text"]
      )

      print(filtered_results)
      ```

      ```javascript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const namespace = pc.index("INDEX_NAME", "INDEX_HOST").namespace("example-namespace");

      const response = await namespace.searchRecords({
        query: {
          topK: 3,
          inputs: { text: "Disease prevention" },
          filter: { category: "digestive system" }
        },
        fields: ['chunk_text', 'category']
      });

      console.log(response);
      ```

      ```java Java theme={null}
      import io.pinecone.clients.Index;
      import io.pinecone.configs.PineconeConfig;
      import io.pinecone.configs.PineconeConnection;
      import org.openapitools.db_data.client.ApiException;
      import org.openapitools.db_data.client.model.SearchRecordsResponse;

      import java.util.*;

      public class SearchText {
          public static void main(String[] args) throws ApiException {
              PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
              // To get the unique host for an index, 
              // see https://docs.pinecone.io/guides/manage-data/target-an-index
              config.setHost("INDEX_HOST");
              PineconeConnection connection = new PineconeConnection(config);

              Index index = new Index(config, connection, "integrated-dense-java");

              String query = "Disease prevention";
              List<String> fields = new ArrayList<>();
              fields.add("category");
              fields.add("chunk_text");

              Map<String, Object> filter = new HashMap<>();
              filter.put("category", "digestive system");

              // Search the dense index
              SearchRecordsResponse recordsResponse = index.searchRecordsByText(query,  "example-namespace", fields, 3, filter, null);

              // Print the results
              System.out.println(recordsResponse);
          }
      }
      ```

      ```go Go theme={null}
      package main

      import (
          "context"
          "encoding/json"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func prettifyStruct(obj interface{}) string {
        	bytes, _ := json.MarshalIndent(obj, "", "  ")
          return string(bytes)
      }

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
          } 

          metadataMap := map[string]interface{}{
              "category": map[string]interface{}{
                  "$eq": "digestive system",
              },
          }
          res, err := idxConnection.SearchRecords(ctx, &pinecone.SearchRecordsRequest{
              Query: pinecone.SearchRecordsQuery{
                  TopK: 3,
                  Inputs: &map[string]interface{}{
                      "text": "Disease prevention",
                  },
                  Filter: &metadataMap,
              },
              Fields: &[]string{"chunk_text", "category"},
          })
          if err != nil {
              log.Fatalf("Failed to search records: %v", err)
          }
          fmt.Printf(prettifyStruct(res))
      }
      ```

      ```csharp C# theme={null}
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      var index = pinecone.Index(host: "INDEX_HOST");

      var response = await index.SearchRecordsAsync(
          "example-namespace",
          new SearchRecordsRequest
          {
              Query = new SearchRecordsRequestQuery
              {
                  TopK = 4,
                  Inputs = new Dictionary<string, object?> { { "text", "Disease prevention" } },
                  Filter = new Dictionary<string, object?>
                  {
                      ["category"] = new Dictionary<string, object?>
                      {
                          ["$eq"] = "digestive system"
                      }
                  }
              },
              Fields = ["category", "chunk_text"],
          }
      );

      Console.WriteLine(response);
      ```

      ```shell curl theme={null}
      INDEX_HOST="INDEX_HOST"
      NAMESPACE="YOUR_NAMESPACE"
      PINECONE_API_KEY="YOUR_API_KEY"

      curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
        -H "Accept: application/json" \
        -H "Content-Type: application/json" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H "X-Pinecone-API-Version: unstable" \
        -d '{
              "query": {
                  "inputs": {"text": "Disease prevention"},
                  "top_k": 3,
                  "filter": {"category": "digestive system"}
              },
              "fields": ["category", "chunk_text"]
           }'
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Search with a vector">
    <CodeGroup>
      ```Python Python theme={null}
      from pinecone.grpc import PineconeGRPC as Pinecone

      pc = Pinecone(api_key="YOUR_API_KEY")

      # To get the unique host for an index, 
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      index = pc.Index(host="INDEX_HOST")

      index.query(
          namespace="example-namespace",
          vector=[0.0236663818359375,-0.032989501953125, ..., -0.01041412353515625,0.0086669921875], 
          top_k=3,
          filter={
              "category": {"$eq": "digestive system"}
          },
          include_metadata=True,
          include_values=False
      )
      ```

      ```JavaScript JavaScript theme={null}
      import { Pinecone } from '@pinecone-database/pinecone'

      const pc = new Pinecone({ apiKey: "YOUR_API_KEY" })

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      const index = pc.index("INDEX_NAME", "INDEX_HOST")

      const queryResponse = await index.namespace('example-namespace').query({
          vector: [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
          topK: 3,
          filter: {
              "category": { "$eq": "digestive system" }
          }
          includeValues: false,
          includeMetadata: true,
      });
      ```

      ```java Java theme={null}
      import com.google.protobuf.Struct;
      import com.google.protobuf.Value;
      import io.pinecone.clients.Index;
      import io.pinecone.configs.PineconeConfig;
      import io.pinecone.configs.PineconeConnection;
      import io.pinecone.unsigned_indices_model.QueryResponseWithUnsignedIndices;

      import java.util.Arrays;
      import java.util.List;

      public class QueryExample {
          public static void main(String[] args) {
              PineconeConfig config = new PineconeConfig("YOUR_API_KEY");
              // To get the unique host for an index, 
              // see https://docs.pinecone.io/guides/manage-data/target-an-index
              config.setHost("INDEX_HOST");
              PineconeConnection connection = new PineconeConnection(config);
              Index index = new Index(connection, "INDEX_NAME");
              List<Float> query = Arrays.asList(0.0236663818359375f, -0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f);
              Struct filter = Struct.newBuilder()
                      .putFields("category", Value.newBuilder()
                              .setStructValue(Struct.newBuilder()
                                      .putFields("$eq", Value.newBuilder()
                                              .setStringValue("digestive system")
                                              .build()))
                              .build())
                      .build();

              QueryResponseWithUnsignedIndices queryResponse = index.query(1, query, null, null, null, "example-namespace", filter, false, true);
              System.out.println(queryResponse);
          }
      }
      ```

      ```go Go theme={null}
      package main

      import (
          "context"
          "encoding/json"
          "fmt"
          "log"

          "github.com/pinecone-io/go-pinecone/v4/pinecone"
      )

      func prettifyStruct(obj interface{}) string {
      	bytes, _ := json.MarshalIndent(obj, "", "  ")
      	return string(bytes)
      }

      func main() {
          ctx := context.Background()

          pc, err := pinecone.NewClient(pinecone.NewClientParams{
              ApiKey: "YOUR_API_KEY",
          })
          if err != nil {
              log.Fatalf("Failed to create Client: %v", err)
          }

          // To get the unique host for an index, 
          // see https://docs.pinecone.io/guides/manage-data/target-an-index
          idxConnection, err := pc.Index(pinecone.NewIndexConnParams{Host: "INDEX_HOST", Namespace: "example-namespace"})
          if err != nil {
              log.Fatalf("Failed to create IndexConnection for Host: %v", err)
        	}

          queryVector := []float32{0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875}

          metadataMap := map[string]interface{}{
              "category": map[string]interface{}{
                  "$eq": "digestive system",
              }
          }

          metadataFilter, err := structpb.NewStruct(metadataMap)
          if err != nil {
              log.Fatalf("Failed to create metadata map: %v", err)
          }

          res, err := idxConnection.QueryByVectorValues(ctx, &pinecone.QueryByVectorValuesRequest{
              Vector:          queryVector,
              TopK:            3,
              MetadataFilter: metadataFilter,
              IncludeValues:   false,
              includeMetadata: true,
          })
          if err != nil {
              log.Fatalf("Error encountered when querying by vector: %v", err)
          } else {
              fmt.Printf(prettifyStruct(res))
          }
      }
      ```

      ```csharp C# theme={null}
      using Pinecone;

      var pinecone = new PineconeClient("YOUR_API_KEY");

      // To get the unique host for an index, 
      // see https://docs.pinecone.io/guides/manage-data/target-an-index
      var index = pinecone.Index(host: "INDEX_HOST");

      var queryResponse = await index.QueryAsync(new QueryRequest {
          Vector = new[] { 0.0236663818359375f ,-0.032989501953125f, ..., -0.01041412353515625f, 0.0086669921875f },
          Namespace = "example-namespace",
          TopK = 3,
          Filter = new Metadata
          {
              ["category"] =
                  new Metadata
                  {
                      ["$eq"] = "digestive system",
                  }
          },
          IncludeMetadata = true,
      });

      Console.WriteLine(queryResponse);
      ```

      ```bash curl theme={null}
      # To get the unique host for an index,
      # see https://docs.pinecone.io/guides/manage-data/target-an-index
      PINECONE_API_KEY="YOUR_API_KEY"
      INDEX_HOST="INDEX_HOST"

      curl "https://$INDEX_HOST/query" \
        -H "Api-Key: $PINECONE_API_KEY" \
        -H 'Content-Type: application/json' \
        -H "X-Pinecone-API-Version: 2025-04" \
        -d '{
              "vector": [0.0236663818359375,-0.032989501953125,...,-0.01041412353515625,0.0086669921875],
              "namespace": "example-namespace",
              "topK": 3,
              "filter": {"category": {"$eq": "digestive system"}},
              "includeMetadata": true,
              "includeValues": false
          }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>


## Metadata filter expressions

Pinecone's filtering language supports the following operators:

| Operator  | Function                                                                                                                           | Supported types         |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `$eq`     | Matches {word_0} with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}`            | Number, string, boolean |
| `$ne`     | Matches {word_0} with metadata values that are not equal to a specified value. Example: `{"genre": {"$ne": "drama"}}`              | Number, string, boolean |
| `$gt`     | Matches {word_0} with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}`                  | Number                  |
| `$gte`    | Matches {word_0} with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}`      | Number                  |
| `$lt`     | Matches {word_0} with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}`                     | Number                  |
| `$lte`    | Matches {word_0} with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}`        | Number                  |
| `$in`     | Matches {word_0} with metadata values that are in a specified array. Example: `{"genre": {"$in": ["comedy", "documentary"]}}`      | String, number          |
| `$nin`    | Matches {word_0} with metadata values that are not in a specified array. Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number          |
| `$exists` | Matches {word_0} with the specified metadata field. Example: `{"genre": {"$exists": true}}`                                        | Number, string, boolean |
| `$and`    | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`             | -                       |
| `$or`     | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`               | -                       |

<Note>
  Only `$and` and `$or` are allowed at the top level of the query expression.
</Note>

For example, the following has a `"genre"` metadata field with a list of strings:

```JSON JSON theme={null}
{ "genre": ["comedy", "documentary"] }
```

This means `"genre"` takes on both values, and requests with the following filters will match:

```JSON JSON theme={null}
{"genre":"comedy"}

{"genre": {"$in":["documentary","action"]}}

{"$and": [{"genre": "comedy"}, {"genre":"documentary"}]}
```

However, requests with the following filter will **not** match:

```JSON JSON theme={null}
{ "$and": [{ "genre": "comedy" }, { "genre": "drama" }] }
```

Additionally, requests with the following filters will **not** match because they are invalid. They will result in a compilation error:

```json JSON theme={null}

# INVALID QUERY:
{"genre": ["comedy", "documentary"]}
```

```json JSON theme={null}

# INVALID QUERY:
{"genre": {"$eq": ["comedy", "documentary"]}}
```



# Hybrid search
Source: https://docs.pinecone.io/guides/search/hybrid-search

Combine semantic and lexical search for better results.

[Semantic search](/guides/search/semantic-search) and [lexical search](/guides/search/lexical-search) are powerful information retrieval techniques, but each has notable limitations. For example, semantic search can miss results based on exact keyword matches, especially in scenarios involving domain-specific terminology, while lexical search can miss results based on relationships, such as synonyms and paraphrases.

This page shows you how to lift these limitations by combining semantic and lexical search. This is often called hybrid search.


## Hybrid search approaches

There are two ways to perform hybrid search in Pinecone:

* [Use separate dense and sparse indexes](#use-separate-dense-and-sparse-indexes). This is the **recommended** approach because it provides the most flexibility.
* [Use a single hybrid index](#use-a-single-hybrid-index). This approach is simpler to implement but doesn't support a few useful features.

The following table summarizes the pros and cons between the two approaches:

| Approach                          | Pros                                                                                                                                                                                                                                                                                       | Cons                                                                                                                                                                            |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Separate dense and sparse indexes | <ul><li>You can start with dense for semantic search and add sparse for lexical search later.</li><li>You can do sparse-only queries.</li><li>You can rerank at multiple levels (for each index and for merged results).</li><li>You can use integrated embedding and reranking.</li></ul> | <ul><li>You need to manage and make requests to two separate indexes.</li><li>You need to maintain the linkage between sparse and dense vectors in different indexes.</li></ul> |
| Single hybrid index               | <ul><li>You make requests to only a single index.</li><li>The linkage between dense and sparse vectors is implicit.</li></ul>                                                                                                                                                              | <ul><li>You can't do sparse-only queries.</li><li>You can't use integrated embedding and reranking.</li></ul>                                                                   |


## Use separate dense and sparse indexes

This is the recommended way to perform hybrid search in Pinecone. You create separate dense and sparse indexes, upsert dense vectors into the dense index and sparse vectors into the sparse index, and search each index separately. Then you combine and deduplicate the results, use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank them based on a unified relevance score, and return the most relevant matches.

<Steps>
  <Step title="Create dense and sparse indexes">
    [Create a dense index](/guides/index-data/create-an-index#create-a-dense-index) and [create a sparse index](/guides/index-data/create-an-index#create-a-sparse-index), either with integrated embedding or for vectors created with external models.

    For example, the following code creates indexes with integrated embedding models.

    ```python Python theme={null}
    from pinecone import Pinecone

    pc = Pinecone(api_key="YOUR_API_KEY")

    dense_index_name = "dense-for-hybrid-py"
    sparse_index_name = "sparse-for-hybrid-py"

    if not pc.has_index(dense_index_name):
        pc.create_index_for_model(
            name=dense_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"llama-text-embed-v2",
                "field_map":{"text": "chunk_text"}
            }
        )

    if not pc.has_index(sparse_index_name):
        pc.create_index_for_model(
            name=sparse_index_name,
            cloud="aws",
            region="us-east-1",
            embed={
                "model":"pinecone-sparse-english-v0",
                "field_map":{"text": "chunk_text"}
            }
        )
    ```
  </Step>

  <Step title="Upsert dense and sparse vectors">
    [Upsert dense vectors](/guides/index-data/upsert-data#upsert-dense-vectors) into the dense index and [upsert sparse vectors](/guides/index-data/upsert-data#upsert-sparse-vectors) into the sparse index.

    Make sure to establish a linkage between the dense and sparse vectors so you can merge and deduplicate search results later. For example, the following uses `_id` as the linkage, but you can use any other custom field as well. Because the indexes are integrated with embedding models, you provide the source texts and Pinecone converts them to vectors automatically.

    ```python Python [expandable] theme={null}
    # Define the records
    records = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python theme={null}
    # Target the dense and sparse indexes
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    dense_index = pc.Index(host="INDEX_HOST")
    sparse_index = pc.Index(host="INDEX_HOST")

    # Upsert the records
    # The `chunk_text` fields are converted to dense and sparse vectors
    dense_index.upsert_records("example-namespace", records)
    sparse_index.upsert_records("example-namespace", records)
    ```
  </Step>

  <Step title="Search the dense index">
    Perform a [semantic search](/guides/search/semantic-search) on the dense index.

    For example, the following code searches the dense index for 40 records most semantically related to the query "Q3 2024 us economic data". Because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a dense vector automatically.

    ```python Python theme={null}
    query = "Q3 2024 us economic data"

    dense_results = dense_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(dense_results)
    ```

    ```python Response [expandable] theme={null}
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 0.8629686832427979,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec36',
                          '_score': 0.8573639988899231,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec6',
                          '_score': 0.8535352945327759,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 0.8336166739463806,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec48',
                          '_score': 0.8328524827957153,
                          'fields': {'chunk_text': 'Wage growth outpaced inflation '
                                                   'for the first time in years, '
                                                   'signaling improved purchasing '
                                                   'power in 2024.'}},
                         {'_id': 'vec55',
                          '_score': 0.8322604298591614,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec45',
                          '_score': 0.8309446573257446,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec72',
                          '_score': 0.8275909423828125,
                          'fields': {'chunk_text': 'In early 2024, global GDP '
                                                   'growth slowed, driven by '
                                                   'weaker exports in Asia and '
                                                   'Europe.'}},
                         {'_id': 'vec29',
                          '_score': 0.8270887136459351,
                          'fields': {'chunk_text': 'Growth vs. value investing '
                                                   'strategies in 2024.'}},
                         {'_id': 'vec46',
                          '_score': 0.8263787627220154,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec79',
                          '_score': 0.8258304595947266,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec87',
                          '_score': 0.8257324695587158,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec40',
                          '_score': 0.8253997564315796,
                          'fields': {'chunk_text': 'Labor market trends show a '
                                                   'declining participation rate '
                                                   'despite record low '
                                                   'unemployment in 2024.'}},
                         {'_id': 'vec37',
                          '_score': 0.8235862255096436,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec58',
                          '_score': 0.8233317136764526,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec47',
                          '_score': 0.8231339454650879,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec41',
                          '_score': 0.8187897801399231,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec56',
                          '_score': 0.8155254125595093,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}},
                         {'_id': 'vec63',
                          '_score': 0.8136948347091675,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec52',
                          '_score': 0.8129132390022278,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec23',
                          '_score': 0.8126378655433655,
                          'fields': {'chunk_text': 'Top SPAC mergers in the '
                                                   'technology sector for 2024.'}},
                         {'_id': 'vec62',
                          '_score': 0.8116977214813232,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec64',
                          '_score': 0.8109902739524841,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec54',
                          '_score': 0.8092231154441833,
                          'fields': {'chunk_text': 'The global tourism sector '
                                                   'showed signs of recovery in '
                                                   'late 2024 after years of '
                                                   'pandemic-related setbacks.'}},
                         {'_id': 'vec96',
                          '_score': 0.8075559735298157,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec49',
                          '_score': 0.8062589764595032,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec7',
                          '_score': 0.8034461140632629,
                          'fields': {'chunk_text': 'The CPI index rose by 6% in '
                                                   'July 2024, raising concerns '
                                                   'about purchasing power.'}},
                         {'_id': 'vec84',
                          '_score': 0.8027160167694092,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec13',
                          '_score': 0.8010239601135254,
                          'fields': {'chunk_text': 'Credit card APRs reached an '
                                                   'all-time high of 22.8% in '
                                                   '2024.'}},
                         {'_id': 'vec53',
                          '_score': 0.8007135391235352,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec60',
                          '_score': 0.7980866432189941,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec91',
                          '_score': 0.7980680465698242,
                          'fields': {'chunk_text': 'The impact of ESG investing on '
                                                   'corporate strategies has been '
                                                   'a major focus in 2024.'}},
                         {'_id': 'vec68',
                          '_score': 0.797269880771637,
                          'fields': {'chunk_text': 'Cybersecurity spending reached '
                                                   'new highs in 2024, reflecting '
                                                   'the growing threat of digital '
                                                   'attacks on infrastructure.'}},
                         {'_id': 'vec59',
                          '_score': 0.795337438583374,
                          'fields': {'chunk_text': 'The adoption of digital '
                                                   'currencies by central banks '
                                                   'increased in 2024, reshaping '
                                                   'monetary policy frameworks.'}},
                         {'_id': 'vec39',
                          '_score': 0.793889045715332,
                          'fields': {'chunk_text': 'The rise in energy prices '
                                                   'significantly impacted '
                                                   'inflation trends during the '
                                                   'first half of 2024.'}},
                         {'_id': 'vec66',
                          '_score': 0.7919396162033081,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec57',
                          '_score': 0.7917722463607788,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec75',
                          '_score': 0.7907494306564331,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec51',
                          '_score': 0.790622889995575,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec89',
                          '_score': 0.7899052500724792,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}}]},
     'usage': {'embed_total_tokens': 12, 'read_units': 1}}
    ```
  </Step>

  <Step title="Search the sparse index">
    Perform a [lexical search](/guides/search/lexical-search).

    For example, the following code searches the sparse index for 40 records that most exactly match the words in the query. Again, because the index is integrated with an embedding model, you provide the query as text and Pinecone converts the text to a sparse vector automatically.

    ```python Python theme={null}
    sparse_results = sparse_index.search(
        namespace="example-namespace",
        query={
            "top_k": 40,
            "inputs": {
                "text": query
            }
        }
    )

    print(sparse_results)
    ```

    ```python Response [expandable] theme={null}
    {'result': {'hits': [{'_id': 'vec35',
                          '_score': 7.0625,
                          'fields': {'chunk_text': 'Unemployment hit at 2.4% in Q3 '
                                                   'of 2024.'}},
                         {'_id': 'vec46',
                          '_score': 7.041015625,
                          'fields': {'chunk_text': 'Economic recovery in Q2 2024 '
                                                   'relied heavily on government '
                                                   'spending in infrastructure and '
                                                   'green energy projects.'}},
                         {'_id': 'vec36',
                          '_score': 6.96875,
                          'fields': {'chunk_text': 'Unemployment is expected to '
                                                   'hit 2.5% in Q3 of 2024.'}},
                         {'_id': 'vec42',
                          '_score': 6.9609375,
                          'fields': {'chunk_text': 'Tech sector layoffs in Q3 2024 '
                                                   'have reshaped hiring trends '
                                                   'across high-growth '
                                                   'industries.'}},
                         {'_id': 'vec49',
                          '_score': 6.65625,
                          'fields': {'chunk_text': "China's economic growth in "
                                                   '2024 slowed to its lowest '
                                                   'level in decades due to '
                                                   'structural reforms and weak '
                                                   'exports.'}},
                         {'_id': 'vec63',
                          '_score': 6.4765625,
                          'fields': {'chunk_text': 'Population aging emerged as a '
                                                   'critical economic issue in '
                                                   '2024, especially in advanced '
                                                   'economies.'}},
                         {'_id': 'vec92',
                          '_score': 5.72265625,
                          'fields': {'chunk_text': 'Income inequality widened in '
                                                   '2024 despite strong economic '
                                                   'growth in developed nations.'}},
                         {'_id': 'vec52',
                          '_score': 5.599609375,
                          'fields': {'chunk_text': 'Record-breaking weather events '
                                                   'in early 2024 have highlighted '
                                                   'the growing economic impact of '
                                                   'climate change.'}},
                         {'_id': 'vec89',
                          '_score': 4.0078125,
                          'fields': {'chunk_text': 'Venture capital investments in '
                                                   '2024 leaned heavily toward AI '
                                                   'and automation startups.'}},
                         {'_id': 'vec62',
                          '_score': 3.99609375,
                          'fields': {'chunk_text': 'Private equity activity in '
                                                   '2024 focused on renewable '
                                                   'energy and technology sectors '
                                                   'amid shifting investor '
                                                   'priorities.'}},
                         {'_id': 'vec57',
                          '_score': 3.93359375,
                          'fields': {'chunk_text': 'Startups in 2024 faced tighter '
                                                   'funding conditions as venture '
                                                   'capitalists focused on '
                                                   'profitability over growth.'}},
                         {'_id': 'vec69',
                          '_score': 3.8984375,
                          'fields': {'chunk_text': 'The agricultural sector faced '
                                                   'challenges in 2024 due to '
                                                   'extreme weather and rising '
                                                   'input costs.'}},
                         {'_id': 'vec37',
                          '_score': 3.89453125,
                          'fields': {'chunk_text': 'In Q3 2025 unemployment for '
                                                   'the prior year was revised to '
                                                   '2.2%'}},
                         {'_id': 'vec60',
                          '_score': 3.822265625,
                          'fields': {'chunk_text': 'Healthcare spending in 2024 '
                                                   'surged as governments expanded '
                                                   'access to preventive care and '
                                                   'pandemic preparedness.'}},
                         {'_id': 'vec51',
                          '_score': 3.783203125,
                          'fields': {'chunk_text': 'The European Union introduced '
                                                   'new fiscal policies in 2024 '
                                                   'aimed at reducing public debt '
                                                   'without stifling growth.'}},
                         {'_id': 'vec55',
                          '_score': 3.765625,
                          'fields': {'chunk_text': 'Trade tensions between the '
                                                   'U.S. and China escalated in '
                                                   '2024, impacting global supply '
                                                   'chains and investment flows.'}},
                         {'_id': 'vec70',
                          '_score': 3.76171875,
                          'fields': {'chunk_text': 'Consumer spending patterns '
                                                   'shifted in 2024, with a '
                                                   'greater focus on experiences '
                                                   'over goods.'}},
                         {'_id': 'vec90',
                          '_score': 3.70703125,
                          'fields': {'chunk_text': 'The surge in e-commerce in '
                                                   '2024 was facilitated by '
                                                   'advancements in logistics '
                                                   'technology.'}},
                         {'_id': 'vec87',
                          '_score': 3.69140625,
                          'fields': {'chunk_text': "The U.S. labor market's "
                                                   'resilience in 2024 defied '
                                                   'predictions of a severe '
                                                   'recession.'}},
                         {'_id': 'vec78',
                          '_score': 3.673828125,
                          'fields': {'chunk_text': 'Consumer sentiment surveys in '
                                                   '2024 reflected optimism '
                                                   'despite high interest rates.'}},
                         {'_id': 'vec82',
                          '_score': 3.66015625,
                          'fields': {'chunk_text': 'Renewable energy subsidies in '
                                                   '2024 reduced the global '
                                                   'reliance on fossil fuels.'}},
                         {'_id': 'vec53',
                          '_score': 3.642578125,
                          'fields': {'chunk_text': 'Cryptocurrencies faced '
                                                   'regulatory scrutiny in 2024, '
                                                   'leading to volatility and '
                                                   'reduced market '
                                                   'capitalization.'}},
                         {'_id': 'vec94',
                          '_score': 3.625,
                          'fields': {'chunk_text': 'Cyberattacks targeting '
                                                   'financial institutions in 2024 '
                                                   'led to record cybersecurity '
                                                   'spending.'}},
                         {'_id': 'vec45',
                          '_score': 3.607421875,
                          'fields': {'chunk_text': 'Corporate earnings in Q4 2024 '
                                                   'were largely impacted by '
                                                   'rising raw material costs and '
                                                   'currency fluctuations.'}},
                         {'_id': 'vec47',
                          '_score': 3.576171875,
                          'fields': {'chunk_text': 'The housing market saw a '
                                                   'rebound in late 2024, driven '
                                                   'by falling mortgage rates and '
                                                   'pent-up demand.'}},
                         {'_id': 'vec84',
                          '_score': 3.5703125,
                          'fields': {'chunk_text': "The IMF's 2024 global outlook "
                                                   'highlighted risks of '
                                                   'stagflation in emerging '
                                                   'markets.'}},
                         {'_id': 'vec41',
                          '_score': 3.5546875,
                          'fields': {'chunk_text': 'Forecasts of global supply '
                                                   'chain disruptions eased in '
                                                   'late 2024, but consumer prices '
                                                   'remained elevated due to '
                                                   'persistent demand.'}},
                         {'_id': 'vec65',
                          '_score': 3.537109375,
                          'fields': {'chunk_text': 'The global shipping industry '
                                                   'experienced declining freight '
                                                   'rates in 2024 due to '
                                                   'overcapacity and reduced '
                                                   'demand.'}},
                         {'_id': 'vec96',
                          '_score': 3.53125,
                          'fields': {'chunk_text': 'New trade agreements signed '
                                                   '2022 will make an impact in '
                                                   '2024'}},
                         {'_id': 'vec86',
                          '_score': 3.52734375,
                          'fields': {'chunk_text': 'Digital transformation '
                                                   'initiatives in 2024 drove '
                                                   'productivity gains in the '
                                                   'services sector.'}},
                         {'_id': 'vec95',
                          '_score': 3.5234375,
                          'fields': {'chunk_text': 'Automation in agriculture in '
                                                   '2024 increased yields but '
                                                   'displaced rural workers.'}},
                         {'_id': 'vec64',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'Rising commodity prices in '
                                                   '2024 strained emerging markets '
                                                   'dependent on imports of raw '
                                                   'materials.'}},
                         {'_id': 'vec79',
                          '_score': 3.51171875,
                          'fields': {'chunk_text': 'The resurgence of industrial '
                                                   'policy in Q1 2024 focused on '
                                                   'decoupling critical supply '
                                                   'chains.'}},
                         {'_id': 'vec66',
                          '_score': 3.48046875,
                          'fields': {'chunk_text': 'Bank lending to small and '
                                                   'medium-sized enterprises '
                                                   'surged in 2024 as governments '
                                                   'incentivized '
                                                   'entrepreneurship.'}},
                         {'_id': 'vec6',
                          '_score': 3.4765625,
                          'fields': {'chunk_text': 'Unemployment hit a record low '
                                                   'of 3.7% in Q4 of 2024.'}},
                         {'_id': 'vec58',
                          '_score': 3.39453125,
                          'fields': {'chunk_text': 'Oil production cuts in Q1 2024 '
                                                   'by OPEC nations drove prices '
                                                   'higher, influencing global '
                                                   'energy policies.'}},
                         {'_id': 'vec80',
                          '_score': 3.390625,
                          'fields': {'chunk_text': 'Technological innovation in '
                                                   'the fintech sector disrupted '
                                                   'traditional banking in 2024.'}},
                         {'_id': 'vec75',
                          '_score': 3.37109375,
                          'fields': {'chunk_text': 'The collapse of Silicon Valley '
                                                   'Bank raised questions about '
                                                   'regulatory oversight in '
                                                   '2024.'}},
                         {'_id': 'vec67',
                          '_score': 3.357421875,
                          'fields': {'chunk_text': 'Renewable energy projects '
                                                   'accounted for a record share '
                                                   'of global infrastructure '
                                                   'investment in 2024.'}},
                         {'_id': 'vec56',
                          '_score': 3.341796875,
                          'fields': {'chunk_text': 'Consumer confidence indices '
                                                   'remained resilient in Q2 2024 '
                                                   'despite fears of an impending '
                                                   'recession.'}}]},
     'usage': {'embed_total_tokens': 9, 'read_units': 1}}
    ```
  </Step>

  <Step title="Merge and deduplicate the results">
    Merge the 40 dense and 40 sparse results and deduplicated them based on the field you used to link sparse and dense vectors.

    For example, the following code merges and deduplicates the results based on the `_id` field, resulting in 52 unique results.

    ```python Python theme={null}
    def merge_chunks(h1, h2):
        """Get the unique hits from two search results and return them as single array of {'_id', 'chunk_text'} dicts, printing each dict on a new line."""
        # Deduplicate by _id
        deduped_hits = {hit['_id']: hit for hit in h1['result']['hits'] + h2['result']['hits']}.values()
        # Sort by _score descending
        sorted_hits = sorted(deduped_hits, key=lambda x: x['_score'], reverse=True)
        # Transform to format for reranking
        result = [{'_id': hit['_id'], 'chunk_text': hit['fields']['chunk_text']} for hit in sorted_hits]
        return result

    merged_results = merge_chunks(sparse_results, dense_results)

    print('[\n   ' + ',\n   '.join(str(obj) for obj in merged_results) + '\n]')
    ```

    ```console Response [expandable] theme={null}
    [
       {'_id': 'vec92', 'chunk_text': 'Income inequality widened in 2024 despite strong economic growth in developed nations.'},
       {'_id': 'vec69', 'chunk_text': 'The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs.'},
       {'_id': 'vec70', 'chunk_text': 'Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods.'},
       {'_id': 'vec90', 'chunk_text': 'The surge in e-commerce in 2024 was facilitated by advancements in logistics technology.'},
       {'_id': 'vec78', 'chunk_text': 'Consumer sentiment surveys in 2024 reflected optimism despite high interest rates.'},
       {'_id': 'vec82', 'chunk_text': 'Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels.'},
       {'_id': 'vec94', 'chunk_text': 'Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending.'},
       {'_id': 'vec65', 'chunk_text': 'The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand.'},
       {'_id': 'vec86', 'chunk_text': 'Digital transformation initiatives in 2024 drove productivity gains in the services sector.'},
       {'_id': 'vec95', 'chunk_text': 'Automation in agriculture in 2024 increased yields but displaced rural workers.'},
       {'_id': 'vec80', 'chunk_text': 'Technological innovation in the fintech sector disrupted traditional banking in 2024.'},
       {'_id': 'vec67', 'chunk_text': 'Renewable energy projects accounted for a record share of global infrastructure investment in 2024.'},
       {'_id': 'vec35', 'chunk_text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
       {'_id': 'vec36', 'chunk_text': 'Unemployment is expected to hit 2.5% in Q3 of 2024.'},
       {'_id': 'vec6', 'chunk_text': 'Unemployment hit a record low of 3.7% in Q4 of 2024.'},
       {'_id': 'vec42', 'chunk_text': 'Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.'},
       {'_id': 'vec48', 'chunk_text': 'Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.'},
       {'_id': 'vec55', 'chunk_text': 'Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows.'},
       {'_id': 'vec45', 'chunk_text': 'Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations.'},
       {'_id': 'vec72', 'chunk_text': 'In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.'},
       {'_id': 'vec29', 'chunk_text': 'Growth vs. value investing strategies in 2024.'},
       {'_id': 'vec46', 'chunk_text': 'Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.'},
       {'_id': 'vec79', 'chunk_text': 'The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains.'},
       {'_id': 'vec87', 'chunk_text': "The U.S. labor market's resilience in 2024 defied predictions of a severe recession."},
       {'_id': 'vec40', 'chunk_text': 'Labor market trends show a declining participation rate despite record low unemployment in 2024.'},
       {'_id': 'vec37', 'chunk_text': 'In Q3 2025 unemployment for the prior year was revised to 2.2%'},
       {'_id': 'vec58', 'chunk_text': 'Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies.'},
       {'_id': 'vec47', 'chunk_text': 'The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand.'},
       {'_id': 'vec41', 'chunk_text': 'Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand.'},
       {'_id': 'vec56', 'chunk_text': 'Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession.'},
       {'_id': 'vec63', 'chunk_text': 'Population aging emerged as a critical economic issue in 2024, especially in advanced economies.'},
       {'_id': 'vec52', 'chunk_text': 'Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change.'},
       {'_id': 'vec23', 'chunk_text': 'Top SPAC mergers in the technology sector for 2024.'},
       {'_id': 'vec62', 'chunk_text': 'Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities.'},
       {'_id': 'vec64', 'chunk_text': 'Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials.'},
       {'_id': 'vec54', 'chunk_text': 'The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks.'},
       {'_id': 'vec96', 'chunk_text': 'New trade agreements signed 2022 will make an impact in 2024'},
       {'_id': 'vec49', 'chunk_text': "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports."},
       {'_id': 'vec7', 'chunk_text': 'The CPI index rose by 6% in July 2024, raising concerns about purchasing power.'},
       {'_id': 'vec84', 'chunk_text': "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets."},
       {'_id': 'vec13', 'chunk_text': 'Credit card APRs reached an all-time high of 22.8% in 2024.'},
       {'_id': 'vec53', 'chunk_text': 'Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization.'},
       {'_id': 'vec60', 'chunk_text': 'Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness.'},
       {'_id': 'vec91', 'chunk_text': 'The impact of ESG investing on corporate strategies has been a major focus in 2024.'},
       {'_id': 'vec68', 'chunk_text': 'Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure.'},
       {'_id': 'vec59', 'chunk_text': 'The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks.'},
       {'_id': 'vec39', 'chunk_text': 'The rise in energy prices significantly impacted inflation trends during the first half of 2024.'},
       {'_id': 'vec66', 'chunk_text': 'Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship.'},
       {'_id': 'vec57', 'chunk_text': 'Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth.'},
       {'_id': 'vec75', 'chunk_text': 'The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024.'},
       {'_id': 'vec51', 'chunk_text': 'The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth.'},
       {'_id': 'vec89', 'chunk_text': 'Venture capital investments in 2024 leaned heavily toward AI and automation startups.'}
    ]
    ```
  </Step>

  <Step title="Rerank the results">
    Use one of Pinecone's [hosted reranking models](/guides/search/rerank-results#reranking-models) to rerank the merged and deduplicated results based on a unified relevance score and then return a smaller set of the most highly relevant results.

    For example, the following code sends the 52 unique results from the last step to the `bge-reranker-v2-m3` reranking model and returns the top 10 most relevant results.

    ```python Python theme={null}
    result = pc.inference.rerank(
        model="bge-reranker-v2-m3",
        query=query,
        documents=merged_results,
        rank_fields=["chunk_text"],
        top_n=10,
        return_documents=True,
        parameters={
            "truncate": "END"
        }
    )

    print("Query", query)
    print('-----')
    for row in result.data:
        print(f"{row['document']['_id']} - {round(row['score'], 2)} - {row['document']['chunk_text']}")
    ```

    ```console Response [expandable] theme={null}
    Query Q3 2024 us economic data
    -----
    vec36 - 0.84 - Unemployment is expected to hit 2.5% in Q3 of 2024.
    vec35 - 0.76 - Unemployment hit at 2.4% in Q3 of 2024.
    vec48 - 0.33 - Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024.
    vec37 - 0.25 - In Q3 2025 unemployment for the prior year was revised to 2.2%
    vec42 - 0.21 - Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries.
    vec87 - 0.2 - The U.S. labor market's resilience in 2024 defied predictions of a severe recession.
    vec63 - 0.08 - Population aging emerged as a critical economic issue in 2024, especially in advanced economies.
    vec92 - 0.08 - Income inequality widened in 2024 despite strong economic growth in developed nations.
    vec72 - 0.07 - In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe.
    vec46 - 0.06 - Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects.
    ```
  </Step>
</Steps>


## Use a single hybrid index

You can perform hybrid search with a single hybrid index as follows:

<Steps>
  <Step title="Create a hybrid index">
    To store both dense and sparse vectors in a single index, use the [`create_index`](/reference/api/latest/control-plane/create_index) operation, setting the `vector_type` to `dense` and the `metric` to `dotproduct`. This is the only combination that supports dense/sparse search on a single index.

    ```python Python theme={null}
    from pinecone.grpc import PineconeGRPC as Pinecone
    from pinecone import ServerlessSpec

    pc = Pinecone(api_key="YOUR_API_KEY")

    index_name = "hybrid-index"

    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            vector_type="dense",
            dimension=1024,
            metric="dotproduct",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    ```
  </Step>

  <Step title="Generate vectors">
    Use Pinecone's [hosted embedding models](/guides/index-data/create-an-index#embedding-models) to [convert data into dense and sparse vectors](/reference/api/latest/inference/generate-embeddings).

    ```python Python [expandable] theme={null}
    # Define the records
    data = [
        { "_id": "vec1", "chunk_text": "Apple Inc. issued a $10 billion corporate bond in 2023." },
        { "_id": "vec2", "chunk_text": "ETFs tracking the S&P 500 outperformed active funds last year." },
        { "_id": "vec3", "chunk_text": "Tesla's options volume surged after the latest earnings report." },
        { "_id": "vec4", "chunk_text": "Dividend aristocrats are known for consistently raising payouts." },
        { "_id": "vec5", "chunk_text": "The Federal Reserve raised interest rates by 0.25% to curb inflation." },
        { "_id": "vec6", "chunk_text": "Unemployment hit a record low of 3.7% in Q4 of 2024." },
        { "_id": "vec7", "chunk_text": "The CPI index rose by 6% in July 2024, raising concerns about purchasing power." },
        { "_id": "vec8", "chunk_text": "GDP growth in emerging markets outpaced developed economies." },
        { "_id": "vec9", "chunk_text": "Amazon's acquisition of MGM Studios was valued at $8.45 billion." },
        { "_id": "vec10", "chunk_text": "Alphabet reported a 20% increase in advertising revenue." },
        { "_id": "vec11", "chunk_text": "ExxonMobil announced a special dividend after record profits." },
        { "_id": "vec12", "chunk_text": "Tesla plans a 3-for-1 stock split to attract retail investors." },
        { "_id": "vec13", "chunk_text": "Credit card APRs reached an all-time high of 22.8% in 2024." },
        { "_id": "vec14", "chunk_text": "A 529 college savings plan offers tax advantages for education." },
        { "_id": "vec15", "chunk_text": "Emergency savings should ideally cover 6 months of expenses." },
        { "_id": "vec16", "chunk_text": "The average mortgage rate rose to 7.1% in December." },
        { "_id": "vec17", "chunk_text": "The SEC fined a hedge fund $50 million for insider trading." },
        { "_id": "vec18", "chunk_text": "New ESG regulations require companies to disclose climate risks." },
        { "_id": "vec19", "chunk_text": "The IRS introduced a new tax bracket for high earners." },
        { "_id": "vec20", "chunk_text": "Compliance with GDPR is mandatory for companies operating in Europe." },
        { "_id": "vec21", "chunk_text": "What are the best-performing green bonds in a rising rate environment?" },
        { "_id": "vec22", "chunk_text": "How does inflation impact the real yield of Treasury bonds?" },
        { "_id": "vec23", "chunk_text": "Top SPAC mergers in the technology sector for 2024." },
        { "_id": "vec24", "chunk_text": "Are stablecoins a viable hedge against currency devaluation?" },
        { "_id": "vec25", "chunk_text": "Comparison of Roth IRA vs 401(k) for high-income earners." },
        { "_id": "vec26", "chunk_text": "Stock splits and their effect on investor sentiment." },
        { "_id": "vec27", "chunk_text": "Tech IPOs that disappointed in their first year." },
        { "_id": "vec28", "chunk_text": "Impact of interest rate hikes on bank stocks." },
        { "_id": "vec29", "chunk_text": "Growth vs. value investing strategies in 2024." },
        { "_id": "vec30", "chunk_text": "The role of artificial intelligence in quantitative trading." },
        { "_id": "vec31", "chunk_text": "What are the implications of quantitative tightening on equities?" },
        { "_id": "vec32", "chunk_text": "How does compounding interest affect long-term investments?" },
        { "_id": "vec33", "chunk_text": "What are the best assets to hedge against inflation?" },
        { "_id": "vec34", "chunk_text": "Can ETFs provide better diversification than mutual funds?" },
        { "_id": "vec35", "chunk_text": "Unemployment hit at 2.4% in Q3 of 2024." },
        { "_id": "vec36", "chunk_text": "Unemployment is expected to hit 2.5% in Q3 of 2024." },
        { "_id": "vec37", "chunk_text": "In Q3 2025 unemployment for the prior year was revised to 2.2%"},
        { "_id": "vec38", "chunk_text": "Emerging markets witnessed increased foreign direct investment as global interest rates stabilized." },
        { "_id": "vec39", "chunk_text": "The rise in energy prices significantly impacted inflation trends during the first half of 2024." },
        { "_id": "vec40", "chunk_text": "Labor market trends show a declining participation rate despite record low unemployment in 2024." },
        { "_id": "vec41", "chunk_text": "Forecasts of global supply chain disruptions eased in late 2024, but consumer prices remained elevated due to persistent demand." },
        { "_id": "vec42", "chunk_text": "Tech sector layoffs in Q3 2024 have reshaped hiring trends across high-growth industries." },
        { "_id": "vec43", "chunk_text": "The U.S. dollar weakened against a basket of currencies as the global economy adjusted to shifting trade balances." },
        { "_id": "vec44", "chunk_text": "Central banks worldwide increased gold reserves to hedge against geopolitical and economic instability." },
        { "_id": "vec45", "chunk_text": "Corporate earnings in Q4 2024 were largely impacted by rising raw material costs and currency fluctuations." },
        { "_id": "vec46", "chunk_text": "Economic recovery in Q2 2024 relied heavily on government spending in infrastructure and green energy projects." },
        { "_id": "vec47", "chunk_text": "The housing market saw a rebound in late 2024, driven by falling mortgage rates and pent-up demand." },
        { "_id": "vec48", "chunk_text": "Wage growth outpaced inflation for the first time in years, signaling improved purchasing power in 2024." },
        { "_id": "vec49", "chunk_text": "China's economic growth in 2024 slowed to its lowest level in decades due to structural reforms and weak exports." },
        { "_id": "vec50", "chunk_text": "AI-driven automation in the manufacturing sector boosted productivity but raised concerns about job displacement." },
        { "_id": "vec51", "chunk_text": "The European Union introduced new fiscal policies in 2024 aimed at reducing public debt without stifling growth." },
        { "_id": "vec52", "chunk_text": "Record-breaking weather events in early 2024 have highlighted the growing economic impact of climate change." },
        { "_id": "vec53", "chunk_text": "Cryptocurrencies faced regulatory scrutiny in 2024, leading to volatility and reduced market capitalization." },
        { "_id": "vec54", "chunk_text": "The global tourism sector showed signs of recovery in late 2024 after years of pandemic-related setbacks." },
        { "_id": "vec55", "chunk_text": "Trade tensions between the U.S. and China escalated in 2024, impacting global supply chains and investment flows." },
        { "_id": "vec56", "chunk_text": "Consumer confidence indices remained resilient in Q2 2024 despite fears of an impending recession." },
        { "_id": "vec57", "chunk_text": "Startups in 2024 faced tighter funding conditions as venture capitalists focused on profitability over growth." },
        { "_id": "vec58", "chunk_text": "Oil production cuts in Q1 2024 by OPEC nations drove prices higher, influencing global energy policies." },
        { "_id": "vec59", "chunk_text": "The adoption of digital currencies by central banks increased in 2024, reshaping monetary policy frameworks." },
        { "_id": "vec60", "chunk_text": "Healthcare spending in 2024 surged as governments expanded access to preventive care and pandemic preparedness." },
        { "_id": "vec61", "chunk_text": "The World Bank reported declining poverty rates globally, but regional disparities persisted." },
        { "_id": "vec62", "chunk_text": "Private equity activity in 2024 focused on renewable energy and technology sectors amid shifting investor priorities." },
        { "_id": "vec63", "chunk_text": "Population aging emerged as a critical economic issue in 2024, especially in advanced economies." },
        { "_id": "vec64", "chunk_text": "Rising commodity prices in 2024 strained emerging markets dependent on imports of raw materials." },
        { "_id": "vec65", "chunk_text": "The global shipping industry experienced declining freight rates in 2024 due to overcapacity and reduced demand." },
        { "_id": "vec66", "chunk_text": "Bank lending to small and medium-sized enterprises surged in 2024 as governments incentivized entrepreneurship." },
        { "_id": "vec67", "chunk_text": "Renewable energy projects accounted for a record share of global infrastructure investment in 2024." },
        { "_id": "vec68", "chunk_text": "Cybersecurity spending reached new highs in 2024, reflecting the growing threat of digital attacks on infrastructure." },
        { "_id": "vec69", "chunk_text": "The agricultural sector faced challenges in 2024 due to extreme weather and rising input costs." },
        { "_id": "vec70", "chunk_text": "Consumer spending patterns shifted in 2024, with a greater focus on experiences over goods." },
        { "_id": "vec71", "chunk_text": "The economic impact of the 2008 financial crisis was mitigated by quantitative easing policies." },
        { "_id": "vec72", "chunk_text": "In early 2024, global GDP growth slowed, driven by weaker exports in Asia and Europe." },
        { "_id": "vec73", "chunk_text": "The historical relationship between inflation and unemployment is explained by the Phillips Curve." },
        { "_id": "vec74", "chunk_text": "The World Trade Organization's role in resolving disputes was tested in 2024." },
        { "_id": "vec75", "chunk_text": "The collapse of Silicon Valley Bank raised questions about regulatory oversight in 2024." },
        { "_id": "vec76", "chunk_text": "The cost of living crisis has been exacerbated by stagnant wage growth and rising inflation." },
        { "_id": "vec77", "chunk_text": "Supply chain resilience became a top priority for multinational corporations in 2024." },
        { "_id": "vec78", "chunk_text": "Consumer sentiment surveys in 2024 reflected optimism despite high interest rates." },
        { "_id": "vec79", "chunk_text": "The resurgence of industrial policy in Q1 2024 focused on decoupling critical supply chains." },
        { "_id": "vec80", "chunk_text": "Technological innovation in the fintech sector disrupted traditional banking in 2024." },
        { "_id": "vec81", "chunk_text": "The link between climate change and migration patterns is increasingly recognized." },
        { "_id": "vec82", "chunk_text": "Renewable energy subsidies in 2024 reduced the global reliance on fossil fuels." },
        { "_id": "vec83", "chunk_text": "The economic fallout of geopolitical tensions was evident in rising defense budgets worldwide." },
        { "_id": "vec84", "chunk_text": "The IMF's 2024 global outlook highlighted risks of stagflation in emerging markets." },
        { "_id": "vec85", "chunk_text": "Declining birth rates in advanced economies pose long-term challenges for labor markets." },
        { "_id": "vec86", "chunk_text": "Digital transformation initiatives in 2024 drove productivity gains in the services sector." },
        { "_id": "vec87", "chunk_text": "The U.S. labor market's resilience in 2024 defied predictions of a severe recession." },
        { "_id": "vec88", "chunk_text": "New fiscal measures in the European Union aimed to stabilize debt levels post-pandemic." },
        { "_id": "vec89", "chunk_text": "Venture capital investments in 2024 leaned heavily toward AI and automation startups." },
        { "_id": "vec90", "chunk_text": "The surge in e-commerce in 2024 was facilitated by advancements in logistics technology." },
        { "_id": "vec91", "chunk_text": "The impact of ESG investing on corporate strategies has been a major focus in 2024." },
        { "_id": "vec92", "chunk_text": "Income inequality widened in 2024 despite strong economic growth in developed nations." },
        { "_id": "vec93", "chunk_text": "The collapse of FTX highlighted the volatility and risks associated with cryptocurrencies." },
        { "_id": "vec94", "chunk_text": "Cyberattacks targeting financial institutions in 2024 led to record cybersecurity spending." },
        { "_id": "vec95", "chunk_text": "Automation in agriculture in 2024 increased yields but displaced rural workers." },
        { "_id": "vec96", "chunk_text": "New trade agreements signed 2022 will make an impact in 2024"},
    ]
    ```

    ```python Python theme={null}
    # Convert the chunk_text into dense vectors
    dense_embeddings = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=[d['chunk_text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )

    # Convert the chunk_text into sparse vectors
    sparse_embeddings = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=[d['chunk_text'] for d in data],
        parameters={"input_type": "passage", "truncate": "END"}
    )
    ```
  </Step>

  <Step title="Upsert records with dense and sparse vectors">
    Use the [`upsert`](/reference/api/latest/data-plane/upsert) operation, specifying dense values in the `value` parameter and sparse values in the `sparse_values` parameter.

    <Note>
      Only dense indexes using the [dotproduct distance metric](/guides/index-data/indexing-overview#dotproduct) support dense and sparse vectors. Upserting records with dense and sparse vectors into dense indexes with a different distance metric will succeed, but querying will return an error.
    </Note>

    ```Python Python theme={null}
    # Target the hybrid index
    # To get the unique host for an index, 
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    index = pc.Index(host="INDEX_HOST")

    # Each record contains an ID, a dense vector, a sparse vector, and the original text as metadata
    records = []
    for d, de, se in zip(data, dense_embeddings, sparse_embeddings):
        records.append({
            "id": d['_id'],
            "values": de['values'],
            "sparse_values": {'indices': se['sparse_indices'], 'values': se['sparse_values']},
            "metadata": {'text': d['chunk_text']}
        })

    # Upsert the records into the hybrid index
    index.upsert(
        vectors=records,
        namespace="example-namespace"
    )
    ```
  </Step>

  <Step title="Search the hybrid index">
    Use the [`embed`](/reference/api/latest/inference/generate-embeddings) operation to convert your query into a dense vector and a sparse vector, and then use the [`query`](/reference/api/latest/data-plane/query) operation to search the hybrid index for the 40 most relevant records.

    ```Python Python theme={null}
    query = "Q3 2024 us economic data"

    # Convert the query into a dense vector
    dense_query_embedding = pc.inference.embed(
        model="llama-text-embed-v2",
        inputs=query,
        parameters={"input_type": "query", "truncate": "END"}
    )

    # Convert the query into a sparse vector
    sparse_query_embedding = pc.inference.embed(
        model="pinecone-sparse-english-v0",
        inputs=query,
        parameters={"input_type": "query", "truncate": "END"}
    )

    for d, s in zip(dense_query_embedding, sparse_query_embedding):
        query_response = index.query(
            namespace="example-namespace",
            top_k=40,
            vector=d['values'],
            sparse_vector={'indices': s['sparse_indices'], 'values': s['sparse_values']},
            include_values=False,
            include_metadata=True
        )
        print(query_response)
    ```

    ```python Response [expandable] theme={null}
    {'matches': [{'id': 'vec35',
                  'metadata': {'text': 'Unemployment hit at 2.4% in Q3 of 2024.'},
                  'score': 7.92519569,
                  'values': []},
                 {'id': 'vec46',
                  'metadata': {'text': 'Economic recovery in Q2 2024 relied '
                                       'heavily on government spending in '
                                       'infrastructure and green energy projects.'},
                  'score': 7.86733627,
                  'values': []},
                 {'id': 'vec36',
                  'metadata': {'text': 'Unemployment is expected to hit 2.5% in Q3 '
                                       'of 2024.'},
                  'score': 7.82636,
                  'values': []},
                 {'id': 'vec42',
                  'metadata': {'text': 'Tech sector layoffs in Q3 2024 have '
                                       'reshaped hiring trends across high-growth '
                                       'industries.'},
                  'score': 7.79465914,
                  'values': []},
                 {'id': 'vec49',
                  'metadata': {'text': "China's economic growth in 2024 slowed to "
                                       'its lowest level in decades due to '
                                       'structural reforms and weak exports.'},
                  'score': 7.46323156,
                  'values': []},
                 {'id': 'vec63',
                  'metadata': {'text': 'Population aging emerged as a critical '
                                       'economic issue in 2024, especially in '
                                       'advanced economies.'},
                  'score': 7.29055929,
                  'values': []},
                 {'id': 'vec92',
                  'metadata': {'text': 'Income inequality widened in 2024 despite '
                                       'strong economic growth in developed '
                                       'nations.'},
                  'score': 6.51210213,
                  'values': []},
                 {'id': 'vec52',
                  'metadata': {'text': 'Record-breaking weather events in early '
                                       '2024 have highlighted the growing economic '
                                       'impact of climate change.'},
                  'score': 6.4125514,
                  'values': []},
                 {'id': 'vec62',
                  'metadata': {'text': 'Private equity activity in 2024 focused on '
                                       'renewable energy and technology sectors '
                                       'amid shifting investor priorities.'},
                  'score': 4.8084693,
                  'values': []},
                 {'id': 'vec89',
                  'metadata': {'text': 'Venture capital investments in 2024 leaned '
                                       'heavily toward AI and automation '
                                       'startups.'},
                  'score': 4.7974205,
                  'values': []},
                 {'id': 'vec57',
                  'metadata': {'text': 'Startups in 2024 faced tighter funding '
                                       'conditions as venture capitalists focused '
                                       'on profitability over growth.'},
                  'score': 4.72518444,
                  'values': []},
                 {'id': 'vec37',
                  'metadata': {'text': 'In Q3 2025 unemployment for the prior year '
                                       'was revised to 2.2%'},
                  'score': 4.71824408,
                  'values': []},
                 {'id': 'vec69',
                  'metadata': {'text': 'The agricultural sector faced challenges '
                                       'in 2024 due to extreme weather and rising '
                                       'input costs.'},
                  'score': 4.66726208,
                  'values': []},
                 {'id': 'vec60',
                  'metadata': {'text': 'Healthcare spending in 2024 surged as '
                                       'governments expanded access to preventive '
                                       'care and pandemic preparedness.'},
                  'score': 4.62045908,
                  'values': []},
                 {'id': 'vec55',
                  'metadata': {'text': 'Trade tensions between the U.S. and China '
                                       'escalated in 2024, impacting global supply '
                                       'chains and investment flows.'},
                  'score': 4.59764862,
                  'values': []},
                 {'id': 'vec51',
                  'metadata': {'text': 'The European Union introduced new fiscal '
                                       'policies in 2024 aimed at reducing public '
                                       'debt without stifling growth.'},
                  'score': 4.57397079,
                  'values': []},
                 {'id': 'vec70',
                  'metadata': {'text': 'Consumer spending patterns shifted in '
                                       '2024, with a greater focus on experiences '
                                       'over goods.'},
                  'score': 4.55043507,
                  'values': []},
                 {'id': 'vec87',
                  'metadata': {'text': "The U.S. labor market's resilience in 2024 "
                                       'defied predictions of a severe recession.'},
                  'score': 4.51785707,
                  'values': []},
                 {'id': 'vec90',
                  'metadata': {'text': 'The surge in e-commerce in 2024 was '
                                       'facilitated by advancements in logistics '
                                       'technology.'},
                  'score': 4.47754288,
                  'values': []},
                 {'id': 'vec78',
                  'metadata': {'text': 'Consumer sentiment surveys in 2024 '
                                       'reflected optimism despite high interest '
                                       'rates.'},
                  'score': 4.46246624,
                  'values': []},
                 {'id': 'vec53',
                  'metadata': {'text': 'Cryptocurrencies faced regulatory scrutiny '
                                       'in 2024, leading to volatility and reduced '
                                       'market capitalization.'},
                  'score': 4.4435873,
                  'values': []},
                 {'id': 'vec45',
                  'metadata': {'text': 'Corporate earnings in Q4 2024 were largely '
                                       'impacted by rising raw material costs and '
                                       'currency fluctuations.'},
                  'score': 4.43836403,
                  'values': []},
                 {'id': 'vec82',
                  'metadata': {'text': 'Renewable energy subsidies in 2024 reduced '
                                       'the global reliance on fossil fuels.'},
                  'score': 4.43601322,
                  'values': []},
                 {'id': 'vec94',
                  'metadata': {'text': 'Cyberattacks targeting financial '
                                       'institutions in 2024 led to record '
                                       'cybersecurity spending.'},
                  'score': 4.41334057,
                  'values': []},
                 {'id': 'vec47',
                  'metadata': {'text': 'The housing market saw a rebound in late '
                                       '2024, driven by falling mortgage rates and '
                                       'pent-up demand.'},
                  'score': 4.39900732,
                  'values': []},
                 {'id': 'vec41',
                  'metadata': {'text': 'Forecasts of global supply chain '
                                       'disruptions eased in late 2024, but '
                                       'consumer prices remained elevated due to '
                                       'persistent demand.'},
                  'score': 4.37389421,
                  'values': []},
                 {'id': 'vec84',
                  'metadata': {'text': "The IMF's 2024 global outlook highlighted "
                                       'risks of stagflation in emerging markets.'},
                  'score': 4.37335157,
                  'values': []},
                 {'id': 'vec96',
                  'metadata': {'text': 'New trade agreements signed 2022 will make '
                                       'an impact in 2024'},
                  'score': 4.33860636,
                  'values': []},
                 {'id': 'vec79',
                  'metadata': {'text': 'The resurgence of industrial policy in Q1 '
                                       '2024 focused on decoupling critical supply '
                                       'chains.'},
                  'score': 4.33784199,
                  'values': []},
                 {'id': 'vec6',
                  'metadata': {'text': 'Unemployment hit a record low of 3.7% in '
                                       'Q4 of 2024.'},
                  'score': 4.33008051,
                  'values': []},
                 {'id': 'vec65',
                  'metadata': {'text': 'The global shipping industry experienced '
                                       'declining freight rates in 2024 due to '
                                       'overcapacity and reduced demand.'},
                  'score': 4.3228569,
                  'values': []},
                 {'id': 'vec64',
                  'metadata': {'text': 'Rising commodity prices in 2024 strained '
                                       'emerging markets dependent on imports of '
                                       'raw materials.'},
                  'score': 4.32269621,
                  'values': []},
                 {'id': 'vec95',
                  'metadata': {'text': 'Automation in agriculture in 2024 '
                                       'increased yields but displaced rural '
                                       'workers.'},
                  'score': 4.31127262,
                  'values': []},
                 {'id': 'vec86',
                  'metadata': {'text': 'Digital transformation initiatives in 2024 '
                                       'drove productivity gains in the services '
                                       'sector.'},
                  'score': 4.30181122,
                  'values': []},
                 {'id': 'vec66',
                  'metadata': {'text': 'Bank lending to small and medium-sized '
                                       'enterprises surged in 2024 as governments '
                                       'incentivized entrepreneurship.'},
                  'score': 4.27241945,
                  'values': []},
                 {'id': 'vec58',
                  'metadata': {'text': 'Oil production cuts in Q1 2024 by OPEC '
                                       'nations drove prices higher, influencing '
                                       'global energy policies.'},
                  'score': 4.21715498,
                  'values': []},
                 {'id': 'vec80',
                  'metadata': {'text': 'Technological innovation in the fintech '
                                       'sector disrupted traditional banking in '
                                       '2024.'},
                  'score': 4.17712116,
                  'values': []},
                 {'id': 'vec75',
                  'metadata': {'text': 'The collapse of Silicon Valley Bank raised '
                                       'questions about regulatory oversight in '
                                       '2024.'},
                  'score': 4.16192341,
                  'values': []},
                 {'id': 'vec56',
                  'metadata': {'text': 'Consumer confidence indices remained '
                                       'resilient in Q2 2024 despite fears of an '
                                       'impending recession.'},
                  'score': 4.15782213,
                  'values': []},
                 {'id': 'vec67',
                  'metadata': {'text': 'Renewable energy projects accounted for a '
                                       'record share of global infrastructure '
                                       'investment in 2024.'},
                  'score': 4.14623,
                  'values': []}],
     'namespace': 'example-namespace',
     'usage': {'read_units': 9}}
    ```
  </Step>

  <Step title="Search the hybrid index with explicit weighting">
    Because Pinecone views your sparse-dense vector as a single vector, it does not offer a built-in parameter to adjust the weight of a query's dense part against its sparse part; the index is agnostic to density or sparsity of coordinates in your vectors. You may, however, incorporate a linear weighting scheme by customizing your query vector, as we demonstrate in the function below.

    The following example transforms vector values using an alpha parameter.

    ```Python Python theme={null}
    def hybrid_score_norm(dense, sparse, alpha: float):
        """Hybrid score using a convex combination

        alpha * dense + (1 - alpha) * sparse

        Args:
            dense: Array of floats representing
            sparse: a dict of `indices` and `values`
            alpha: scale between 0 and 1
        """
        if alpha < 0 or alpha > 1:
            raise ValueError("Alpha must be between 0 and 1")
        hs = {
            'indices': sparse['indices'],
            'values':  [v * (1 - alpha) for v in sparse['values']]
        }
        return [v * alpha for v in dense], hs
    ```

    The following example transforms a vector using the above function, then queries a Pinecone index.

    ```Python Python theme={null}
    sparse_vector = {
       'indices': [10, 45, 16],
       'values':  [0.5, 0.5, 0.2]
    }
    dense_vector = [0.1, 0.2, 0.3]

    hdense, hsparse = hybrid_score_norm(dense_vector, sparse_vector, alpha=0.75)

    query_response = index.query(
        namespace="example-namespace",
        top_k=10,
        vector=hdense,
        sparse_vector=hsparse
    )
    ```
  </Step>
</Steps>



---
**Navigation:** [← Previous](./12-configure-audit-logs.md) | [Index](./index.md) | [Next →](./14-lexical-search.md)
