**Navigation:** [← Previous](./27-install-the-latest-version.md) | [Index](./index.md) | [Next →](./29-chat-through-the-openai-compatible-interface.md)

# Download a usage report
Source: https://docs.pinecone.io/guides/assistant/admin/download-usage-report

Export organization usage and cost reports.

<Note>
  To view usage and costs across your Pinecone organization, you must be an [organization owner](/guides/organizations/understanding-organizations#organization-owners). Also, this feature is available only to organizations on the Standard or Enterprise plans.
</Note>

The **Usage** dashboard in the Pinecone console gives you a detailed report of usage and costs across your organization, broken down by each billable SKU or aggregated by project or service. You can view the report in the console or download it as a CSV file for more detailed analysis.

1. Go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.
2. Select the time range to report on. This defaults to the last 30 days.
3. Select the scope for your report:
   * **SKU:** The usage and cost for each billable SKU, for example, read units per cloud region, storage size per cloud region, or tokens per embedding model.
   * **Project:** The aggregated cost for each project in your organization.
   * **Service:** The aggregated cost for each service your organization uses, for example, database (includes serverless back up and restore), assistants, inference (embedding and reranking), and collections.
4. Choose the specific SKUs, projects, or services you want to report on. This defaults to all.
5. To download the report as a CSV file, click **Download**.

   <Tip>
     The CSV download provides more granular detail than the console view, including breakdowns by individual index as well as project and index tags.
   </Tip>

Dates are shown in UTC to match billing invoices. Cost data is delayed up to three days from the actual usage date.



# Manage API keys
Source: https://docs.pinecone.io/guides/assistant/admin/manage-api-keys

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



# Manage organization members
Source: https://docs.pinecone.io/guides/assistant/admin/manage-organization-members

Invite and control organization member access levels.

This page shows how [organization owners](guides/assistant/admin/organizations-overview#organization-roles) can add and manage organization members.

<Tip>
  For information about managing members at the **project-level**, see [Manage project members](/guides/assistant/admin/manage-project-members).
</Tip>


## Add a member to an organization

You can add members to your organization in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the **Invite by email** field, enter the member's email address.
3. Choose an [**Organization role**](/guides/assistant/admin/organizations-overview#organization-roles) for the member. The role determines the member's permissions within Pinecone.
4. Click **Invite**.

When you invite a member to join your organization, Pinecone sends them an email containing a link that enables them to gain access to the organization or project. If they already have a Pinecone account, they still receive an email, but they can also immediately view the project.


## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member whose role you want to change, click **ellipsis (...) menu > Edit role**.
3. Select a [**Project role**](/guides/assistant/admin/projects-overview#project-roles) for the member.
4. Click **Edit role**.


## Remove a member

You can remove a member from your organization in the [Pinecone console](https://app.pinecone.io):

1. In the Pinecone console, go to [**Settings > Access > Members**](https://app.pinecone.io/organizations/-/settings/access/members).
2. In the row of the member you want to remove, click **ellipsis (...) menu > Remove member**.
3. Click **Remove Member**.

<Note>
  To remove yourself from an organization, click the **Leave organization** button in your user's row and confirm.
</Note>



# Manage service accounts at the organization-level
Source: https://docs.pinecone.io/guides/assistant/admin/manage-organization-service-accounts

Create service accounts for organization-level API access.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows how [organization owners](/guides/assistant/admin/organizations-overview#organization-roles) can add and manage service accounts at the organization-level. Service accounts enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.

<Tip>
  Once a service account is added at the organization-level, it can be added to a project. For more information, see [Manage service accounts at the project-level](/guides/assistant/admin/manage-project-service-accounts).
</Tip>


## Create a service account

You can create a service account in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/access/service-accounts).

2. Enter a **Name** for the service account.

3. Choose an [**Organization Role**](/guides/assistant/admin/organizations-overview#organization-roles) for the service account. The role determines the service account's permissions within Pinecone.

4. Click **Create**.

5. Copy and save the **Client secret** in a secure place for future use.

   <Warning>
     You will not be able to see the client secret again after you close the dialog.
   </Warning>

6. Click **Close**.

Once you have created a service account, [add it to a project](/guides/assistant/admin/manage-project-service-accounts#add-a-service-account-to-a-project) to allow it access to the project's resources.


## Retrieve an access token

To access the Admin API, you must provide an access token to authenticate. Retrieve the access token using the client secret of a service account, which was [provided at time of creation](#create-a-service-account).

You can retrieve an access token for a service account from the `https://login.pinecone.io/oauth/token` endpoint, as shown in the following example:

```bash curl theme={null}
curl "https://login.pinecone.io/oauth/token" \ # Note: Base URL is login.pinecone.io
	-H "X-Pinecone-Api-Version: 2025-04" \
	-H "Content-Type: application/json" \
	-d '{
		"grant_type": "client_credentials",
		"client_id": "YOUR_CLIENT_ID",
		"client_secret": "YOUR_CLIENT_SECRET",
		"audience": "https://api.pinecone.io/"
	}'
```

The response will include an `access_token` field, which you can use to authenticate with the Admin API.

```
{
    "access_token":"YOUR_ACCESS_TOKEN",
    "expires_in":86400,
    "token_type":"Bearer"
}
```


## Change a service account's role

You can change a service account's role in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Manage**.
3. Select an [**Organization role**](/guides/assistant/admin/organizations-overview#organization-roles) for the service account.
4. Click **Update**.


## Update service account name

You can change a service account's name in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Manage**.
3. Enter a new **Service account name**.
4. Click **Update**.


## Rotate a service account's secret

You can rotate a service account's client secret in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).

2. In the row of the service account you want to update, click **ellipsis (...) menu > Rotate secret**.

3. **Enter the service account name** to confirm.

4. Click **Rotate client secret**.

5. Copy and save the **Client secret** in a secure place for future use.

   <Warning>
     You will not be able to see the client secret again after you close the dialog.
   </Warning>

6. Click **Close**.


## Delete a service account

Deleting a service account will remove it from all projects and will disrupt any applications using it to access Pinecone. You delete a service account in the [Pinecone console](https://app.pinecone.io):

1. Go to [**Settings > Access > Service accounts**](https://app.pinecone.io/organizations/-/settings/service-accounts).
2. In the row of the service account you want to update, click **ellipsis (...) menu > Delete**.
3. **Enter the service account name** to confirm.
4. Click **Delete service account**.



# Manage project members
Source: https://docs.pinecone.io/guides/assistant/admin/manage-project-members

Add and manage team members in your project.

[Organization owners](/guides/assistant/admin/organizations-overview#organization-roles) or project owners can manage members in a project. Members can be added to a project with different [roles](/guides/assistant/admin/projects-overview#project-roles), which determine their permissions within the project.

<Tip>
  For information about managing members at the **organization-level**, see [Manage organization members](/guides/assistant/admin/manage-organization-members).
</Tip>


## Add members to a project

You can add members to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. Enter the member's email address or name.
4. Select a [Project role](/guides/assistant/admin/projects-overview#project-roles) for the member. The role determines the member's permissions within Pinecone.
5. Click **Invite**.

When you invite a member to join your project, Pinecone sends them an email containing a link that enables them to gain access to the project. If they already have a Pinecone account, they still receive an email, but they can also immediately view the project.


## Change a member's role

You can change a member's role in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. In the row of the member you want to edit, click **ellipsis (...) menu > Edit role**.
4. Select a [Project role](/guides/assistant/admin/projects-overview#project-roles) for the member.
5. Click **Edit role**.


## Remove a member

You can remove a member from a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Members** tab](https://app.pinecone.io/organizations/-/projects/-/access/members).
3. In the row of the member you want to delete, click **ellipsis (...) menu > Remove member**.
4. Click **Remove Member**.

<Note>
  To remove yourself from a project, click the **Leave organization** button in your user's row and confirm.
</Note>



# Manage service accounts at the project-level
Source: https://docs.pinecone.io/guides/assistant/admin/manage-project-service-accounts

Enable programmatic access with project-level service accounts.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

This page shows how [organization owners](/guides/assistant/admin/organizations-overview#organization-roles) and [project owners](/guides/assistant/admin/projects-overview#project-roles) can add and manage service accounts at the project-level. Service accounts enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.


## Add a service account to a project

After a service account has been [added to an organization](/guides/assistant/admin/manage-organization-service-accounts#create-a-service-account), it can be added to a project in the [Pinecone console](https://app.pinecone.io/organizations/-/projects):

1. Select your project.
2. Go to the [**Manage > Access > Service accounts** tab](https://app.pinecone.io/organizations/-/projects/-/access/service-accounts).
3. Select the service account to add.
4. Select a [**Project role**](/guides/assistant/admin/projects-overview#project-roles) for the service account. The role determines its permissions within Pinecone.
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



# Manage projects
Source: https://docs.pinecone.io/guides/assistant/admin/manage-projects

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



# Monitor usage and cost
Source: https://docs.pinecone.io/guides/assistant/admin/monitor-spend-and-usage

Set monthly spend alerts and monitor usage across your organization.


## Set monthly spend alerts

You can set up email alerts to monitor your organization's monthly spending. These alerts notify designated recipients when spending reaches specified thresholds. The alerts automatically reset at the start of each monthly billing cycle.

To set a spend alert:

1. Go to [Settings > Spend alerts](https://app.pinecone.io/organizations/-/settings/spend-alerts) in the Pinecone console
2. Click **+ Add Alert**.
3. Enter the dollar amount for the spend alert.
4. Enter the email addresses to send the alert to. [Organization owners](/guides/organizations/understanding-organizations#organization-roles) are listed by default.
5. Click **Create**.

To edit a spend alert:

1. In the row of the spend alert you want to edit, click **ellipsis (...) menu > Edit**.
2. Change the dollar amount and/or email addresses for the spend alert.
3. Click **Update**.

<Note>
  **Auto-spend spike alert**: To protect from unexpected cost increases, Pinecone sends an alert when spending exceeds double your previous month's invoice amount. While the alert threshold is fixed and the alert cannot be deleted, you can modify which email addresses receive the alert and enable or disable the alert notifications.
</Note>


## Monitor organization-level usage

<Note>
  You must be the [organization owner](/guides/organizations/understanding-organizations#organization-owners) to view usage across your Pinecone organization. Also, this feature is available only to organizations on the Standard or Enterprise plans.
</Note>

To view and download a report of your usage and costs for your Pinecone organization, go to [**Settings > Usage**](https://app.pinecone.io/organizations/-/settings/usage) in the Pinecone console.

All dates are given in UTC to match billing invoices.


## Monitor token usage

Requests to the [chat](/reference/api/latest/assistant/chat_assistant), [context retrieval](/reference/api/latest/assistant/context_assistant), and [evaluation](/reference/api/latest/assistant/metrics_alignment) API endpoints return a `usage` parameter with `prompt_tokens`, `completion_tokens`, and `total_tokens` generated.

<Tabs>
  <Tab title="Chat">
    For [chat](/guides/assistant/chat-with-assistant), tokens are defined as follows:

    * `prompt_tokens` are based on the messages sent to the assistant and the context snippets retrieved from the assistant and sent to a model. Messages sent to the assistant can include messages from the [chat history](/guides/assistant/chat-with-assistant#provide-conversation-history) in addition to the newest message.

      `prompt_tokens` appear as **Assistants Input Tokens** on invoices.
    * `completion_tokens` are based on the answer from the model.

      `completion_tokens` appear as **Assistants Output Tokens** on invoices.
    * `total_tokens` is the sum of `prompt_tokens` and `completion_tokens`.

    ```json Example chat response {9-13} theme={null}
    {
        "finish_reason": "stop",
        "message": {
            "role": "assistant",
            "content": "The Chief Financial Officer (CFO) of Netflix is Spencer Neumann."
        },
        "id": "000000000000000030513193ccc52814",
        "model": "gpt-4o-2024-11-20",
        "usage": {
            "prompt_tokens": 23626,
            "completion_tokens": 21,
            "total_tokens": 23647
        },
        "citations": [
            {
                "position": 63,
                "references": [
                    {
                        "file": {
                            "status": "Available",
                            "id": "99305805-3844-41b5-af56-ee693ab80527",
                            "name": "Netflix-10-K-01262024.pdf",
                            "size": 1073470,
                            "metadata": null,
                            "updated_on": "2025-07-29T20:07:53.171752661Z",
                            "created_on": "2025-07-29T20:07:36.361322699Z",
                            "percent_done": 1,
                            "signed_url": "https://storage.googleapis.com/...",
                            "error_message": null
                        },
                        "pages": [
                            78,
                            79,
                            80
                        ],
                        "highlight": null
                    },
                    {
                        "file": {
                            "status": "Available",
                            "id": "99305805-3844-41b5-af56-ee693ab80527",
                            "name": "Netflix-10-K-01262024.pdf",
                            "size": 1073470,
                            "metadata": null,
                            "updated_on": "2025-07-29T20:07:53.171752661Z",
                            "created_on": "2025-07-29T20:07:36.361322699Z",
                            "percent_done": 1,
                            "signed_url": "https://storage.googleapis.com/...",
                            "error_message": null
                        },
                        "pages": [
                            77,
                            78
                        ],
                        "highlight": null
                    }
                ]
            }
        ]
    }
    ```
  </Tab>

  <Tab title="Context retrieval">
    For [context retrieval](/guides/assistant/context-snippets-overview), tokens are defined as follows:

    * `prompt_tokens` are based on the messages sent to the assistant and the context snippets retrieved from the assistant. Messages sent to the assistant can include messages from the chat history in addition to the newest message.

      `prompt_tokens` appear as **Assistants Context Tokens Processed** on invoices.

    * `completion_tokens` do not apply for context retrieval because, unlike for chat, there is no answer from a model. `completion_tokens` will always be 0.

    * `total_tokens` is the sum of `prompt_tokens` and `completion_tokens`.

    ```json Example context response {30-34} theme={null}
    {
        "snippets": [
            {
                "type": "text",
                "content": "edures, or caused such disclosure controls and procedures to be designed under our supervision, to\r\nensure that material information relating to the registrant, including its consolidated subsidiaries, ...",
                "score": 0.86632514,
                "reference": {
                    "type": "pdf",
                    "file": {
                        "status": "Available",
                        "id": "99305805-3844-41b5-af56-ee693ab80527",
                        "name": "Netflix-10-K-01262024.pdf",
                        "size": 1073470,
                        "metadata": null,
                        "updated_on": "2025-07-29T20:07:53.171752661Z",
                        "created_on": "2025-07-29T20:07:36.361322699Z",
                        "percent_done": 1,
                        "signed_url": "https://storage.googleapis.com/...",
                        "error_message": null
                    },
                    "pages": [
                        78,
                        79,
                        80
                    ]
                }
            },
            ...
        ],
        "usage": {
            "prompt_tokens": 22914,
            "completion_tokens": 0,
            "total_tokens": 22914
        },
        "id": "00000000000000007b6ad859184a31b3"
    }
    ```
  </Tab>

  <Tab title="Response evaluation">
    For [response evaluation](/guides/assistant/evaluation-overview), tokens are defined as follows:

    * `prompt_tokens` are based on two requests to a model: The first request contains a question, answer, and ground truth answer, and the second request contains the same details plus generated facts returned by the model for the first request.

      `prompt_tokens` appear as **Assistants Evaluation Tokens Processed** on invoices.
    * `completion_tokens` are based on two responses from a model: The first response contains generated facts, and the second response contains evaluation metrics.

      `completion_tokens` appear as **Assistants Evaluation Tokens Out** on invoices.
    * `total_tokens` is the sum of `prompt_tokens` and `completion_tokens`.

    ```json Response evaluation response {17-21} theme={null}
    {
      "metrics": {
        "correctness": 123,
        "completeness": 123,
        "alignment": 123
      },
      "reasoning": {
        "evaluated_facts": [
          {
            "fact": {
              "content": "<string>"
            },
            "entailment": "entailed"
          }
        ]
      },
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 123,
        "total_tokens": 123
      }
    }
    ```
  </Tab>
</Tabs>



# Organizations overview
Source: https://docs.pinecone.io/guides/assistant/admin/organizations-overview

Understand organization structure, projects, and billing.

A Pinecone organization is a set of [projects](/guides/assistant/admin/projects-overview) that use the same billing. Organizations allow one or more users to control billing and project permissions for all of the projects belonging to the organization. Each project belongs to an organization.

<Note>
  While an email address can be associated with multiple organizations, it cannot be used to create more than one organization. For information about managing organization members, see [Manage organization members](/guides/assistant/admin/manage-organization-members).
</Note>


## Projects in an organization

Each organization contains one or more projects that share the same organization owners and billing settings. Each project belongs to exactly one organization. If you need to move a project from one organization to another, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket).


## Billing settings

All of the projects in an organization share the same billing method and settings. The billing settings for the organization are controlled by the organization owners.

Organization owners can update the billing contact information, update the payment method, and view and download invoices using the [Pinecone console](https://app.pinecone.io/organizations/-/settings/billing).


## Organization roles

Organization owners can manage access to their organizations and projects by assigning roles to organization members and service accounts. The role determines the entity's permissions within Pinecone. The organization roles are as follows:

* **Organization owner**: Organization owners have global permissions across the organization. This includes managing billing details, organization members, and all projects. Organization owners are automatically [project owners](/guides/assistant/admin/projects-overview#project-roles) and, therefore, have all project owner permissions as well.

* **Organization user**: Organization users have restricted organization-level permissions. When inviting organization users, you also choose the projects they belong to and the project role they should have. Organization users are automatically [project owners](/guides/assistant/admin/projects-overview#project-roles) and, therefore, have all project owner permissions as well.

* **Billing admin**: Billing admins have permissions to view and update billing details, but they cannot manage organization members. Billing admins cannot manage projects unless they are also [project owners](/guides/assistant/admin/projects-overview#project-roles).

The following table summarizes the permissions for each organization role:

| Permission                           | Org Owner | Org User | Billing Admin |
| ------------------------------------ | --------- | -------- | ------------- |
| View account details                 | ✓         | ✓        | ✓             |
| Update organization name             | ✓         |          |               |
| Delete the organization              | ✓         |          |               |
| View billing details                 | ✓         |          | ✓             |
| Update billing details               | ✓         |          | ✓             |
| View usage details                   | ✓         |          | ✓             |
| View support plans                   | ✓         |          | ✓             |
| Invite members to the organization   | ✓         |          |               |
| Delete pending member invites        | ✓         |          |               |
| Remove members from the organization | ✓         |          |               |
| Update organization member roles     | ✓         |          |               |
| Create projects                      | ✓         | ✓        |               |


## Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can specify a default role for teammates when they sign up.

For more information, see [Configure single sign-on](/guides/assistant/admin/configure-sso-with-okta).

<Note>SSO is available on Standard and Enterprise plans.</Note>


## Service accounts

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

[Service accounts](/guides/assistant/admin/manage-organization-service-accounts) enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.

Use service accounts to automate infrastructure management and integrate Pinecone into your deployment workflows, rather than through manual actions in the Pinecone console. Service accounts use the [organization roles](/guides/assistant/admin/organizations-overview#organization-roles) and [project role](/guides/assistant/admin/projects-overview#project-roles) for permissioning, and provide a secure and auditable way to handle programmatic access.


## See also

* [Manage organization members](/guides/assistant/admin/manage-organization-members)
* [Manage project members](/guides/assistant/admin/manage-project-members)
* [Project overview](/guides/assistant/admin/projects-overview)



# Projects overview
Source: https://docs.pinecone.io/guides/assistant/admin/projects-overview

Learn about projects, roles, and collaboration.

A Pinecone project belongs to an [organization](/guides/assistant/admin/organizations-overview) and contains a number of [assistants](/guides/assistant/overview) and users. Only a user who belongs to the project can access the indexes in that project. Each project also has at least one project owner.


## Project roles

If you are an [organization owner](/guides/assistant/admin/organizations-overview#organization-roles) or project owner, you can manage members in your project. You assign project members a specific role that determines the member's permissions within the Pinecone console.

When you invite a member at the project-level, you assign one of the following roles:

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

Each Pinecone [project](/guides/assistant/admin/projects-overview) has one or more API keys. In order to [make calls to the Pinecone API](/guides/assistant/quickstart), you must provide a valid API key for the relevant Pinecone project.

For more information, see [Manage API keys](/guides/assistant/admin/manage-api-keys).


## Service accounts

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

[Service accounts](/guides/assistant/admin/manage-organization-service-accounts) enable programmatic access to Pinecone's Admin API, which can be used to create and manage projects and API keys.

Use service accounts to automate infrastructure management and integrate Pinecone into your deployment workflows, rather than through manual actions in the Pinecone console. Service accounts use the [organization roles](/guides/assistant/admin/organizations-overview#organization-roles) and [project role](/guides/assistant/admin/projects-overview#project-roles) for permissioning, and provide a secure and auditable way to handle programmatic access.

To use service accounts, [add the account to your organization](/guides/assistant/admin/manage-organization-service-accounts) before [connecting it to a project](/guides/assistant/admin/manage-project-service-accounts).


## Project IDs

Each Pinecone project has a unique product ID.

To find the ID of a project, go to the project list in the [Pinecone console](https://app.pinecone.io/organizations/-/projects).


## See also

* [Create a project](guides/assistant/admin/create-a-project)
* [Manage project members](guides/assistant/admin/manage-project-members)
* [Organizations overview](guides/assistant/admin/organizations-overview)



# Security overview
Source: https://docs.pinecone.io/guides/assistant/admin/security-overview

Understand Pinecone's security features, including authentication, encryption, and audit logs.

This page describes Pinecone's security protocols, practices, and features.


## Access management

### API keys

Each Pinecone [project](/guides/assistant/admin/projects-overview) has one or more [API keys](/guides/assistant/admin/manage-api-keys). In order to make calls to the Pinecone API, a user must provide a valid API key for the relevant Pinecone project.

You can [manage API key permissions](/guides/assistant/admin/manage-api-keys) in the [Pinecone console](https://app.pinecone.io/organizations/-/projects/-/keys). The available permission roles are as follows:

#### General permissions

<Tabs>
  <Tab title="Pinecone console">
    | Role | Permissions                                     |
    | :--- | :---------------------------------------------- |
    | All  | Permissions to read and write all project data. |
  </Tab>

  <Tab title="API">
    | Role            | Permissions                                      |
    | :-------------- | :----------------------------------------------- |
    | `ProjectEditor` | Permissions to read  and write all project data. |
    | `ProjectViewer` | Permissions to read all project data.            |
  </Tab>
</Tabs>

#### Control plane permissions

<Tabs>
  <Tab title="Pinecone console">
    | Role      | Permissions                                                                                                 |
    | :-------- | :---------------------------------------------------------------------------------------------------------- |
    | ReadWrite | Permissions to list, describe, create, delete, and configure indexes, backups, collections, and assistants. |
    | ReadOnly  | Permissions to list and describe indexes, backups, collections, and assistants.                             |
    | None      | No control plane permissions.                                                                               |
  </Tab>

  <Tab title="API">
    | Role                 | Permissions                                                                                                 |
    | :------------------- | :---------------------------------------------------------------------------------------------------------- |
    | `ControlPlaneEditor` | Permissions to list, describe, create, delete, and configure indexes, backups, collections, and assistants. |
    | `ControlPlaneViewer` | Permissions to list and describe indexes, backups, collections, and assistants.                             |
    | None                 | No control plane permissions.                                                                               |
  </Tab>
</Tabs>

#### Data plane permissions

<Tabs>
  <Tab title="Pinecone console">
    | Role      | Permissions                                                                                                                                                                                                                                                                                                            |
    | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ReadWrite | <ul><li>Indexes: Permissions to query, import, fetch, add, update, and delete index data.</li><li>Pinecone Assistant: Permissions to add, list, view, and delete files; chat with an assistant, and evaluate responses.</li><li>Pinecone Inference: Permissions to generate embeddings and rerank documents.</li></ul> |
    | ReadOnly  | <ul><li>Indexes: Permissions to query, fetch, list ID, and view stats.</li><li>Pinecone Assistant: Permissions to list and view files, chat with an assistant, and evaluate responses.</li></ul>                                                                                                                       |
    | None      | No data plane permissions.                                                                                                                                                                                                                                                                                             |
  </Tab>

  <Tab title="API">
    | Role              | Permissions                                                                                                                                                                                                                                                                                                            |
    | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `DataPlaneEditor` | <ul><li>Indexes: Permissions to query, import, fetch, add, update, and delete index data.</li><li>Pinecone Assistant: Permissions to add, list, view, and delete files; chat with an assistant, and evaluate responses.</li><li>Pinecone Inference: Permissions to generate embeddings and rerank documents.</li></ul> |
    | `DataPlaneViewer` | <ul><li>Indexes: Permissions to query, fetch, list ID, and view stats.</li><li>Pinecone Assistant: Permissions to list and view files, chat with an assistant, and evaluate responses.</li></ul>                                                                                                                       |
    | None              | No data plane permissions.                                                                                                                                                                                                                                                                                             |
  </Tab>
</Tabs>

### Organization single sign-on (SSO)

SSO allows organizations to manage their teams' access to Pinecone through their identity management solution. Once your integration is configured, you can require that users from your domain sign in through SSO, and you can specify a default role for teammates when they sign up. SSO is available on Standard and Enterprise plans.

For more information, see [configure single sign on](/guides/assistant/admin/configure-sso-with-okta).

### Role-based access controls (RBAC)

Pinecone uses role-based access controls (RBAC) to manage access to resources.

Service accounts, API keys, and users are all *principals*. A principal's access is determined by the *roles* assigned to it. Roles are assigned to a principal for a *resource*, either a project or an organization. The roles available to be assigned depend on the type of principal and resource.

#### Service account roles

A service account can be assigned roles for the organization it belongs to, and any projects within that organization. A user can be assigned roles for each organization they belong to, and any projects within that organization. For more information, see [Organization roles](/guides/assistant/admin/organizations-overview#organization-roles) and [Project roles](/guides/assistant/admin/projects-overview#project-roles).

#### API key roles

An API key can only be assigned permissions for the projects it belongs to. For more information, see [API keys](#api-keys).

#### User roles

A user can be assigned roles for each organization they belong to, and any projects within that organization. For more information, see [Organization roles](/guides/assistant/admin/organizations-overview#organization-roles) and [Project roles](/guides/assistant/admin/projects-overview#project-roles).


## Compliance

<Note>
  To learn more about data privacy and compliance at Pinecone, visit the [Pinecone Trust and Security Center](https://security.pinecone.io/).
</Note>

### Audit logs

<publicPreviewEnt />

[Audit logs](/guides/assistant/admin/configure-audit-logs) provide a detailed record of user and API actions that occur within Pinecone.

Events are captured every 30 minutes and each log batch will be saved into its own file as a JSON blob, keyed by the time of the log to be written. Only logs since the integration was created and enabled will be saved.

Audit log events adhere to a standard JSON schema and include the following fields:

```json JSON theme={null}
{
    "id": "00000000-0000-0000-0000-000000000000",
    "organization_id": "AA1bbbbCCdd2EEEe3FF",
    "organization_name": "example-org",
    "client": {
        "userAgent": "rawUserAgent"
    },
    "actor": {
        "principal_id": "00000000-0000-0000-0000-000000000000",
        "principal_name": "example@pinecone.io",
        "principal_type": "user", // user, api_key, service_account
        "display_name": "Example Person" // Only in case of user
    },
	"event": {
        "time": "2024-10-21T20:51:53.697Z",
        "action": "create",
        "resource_type": "index",
        "resource_id": "uuid",
        "resource_name": "docs-example",
        "outcome": {
            "result": "success",
            "reason": "", // Only displays for "result": "failure"
            "error_code": "", // Only displays for "result": "failure"
        },
        "parameters": { // Varies based on event
        }
	}
}
```

The following events are captured in the audit logs:

* [Organization events](#organization-events)
* [Project events](#project-events)
* [Index events](#index-events)
* [User and API key events](#user-and-api-key-events)
* [Security and governance events](#security-and-governance-events)

#### Organization events

| Action            | Query parameters                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| Rename org        | `event.action: update`, `event.resource_type: organization`, `event.resource_id: NEW_ORG_NAME`                 |
| Delete org        | `event.action: delete`, `event.resource_type: organization`, `event.resource_id: DELETED_ORG_NAME`             |
| Create org member | `event.action: create`, `event.resource_type: user`, `event.resource_id: [ARRAY_OF_USER_EMAILS]`               |
| Update org member | `event.action: update`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, role: NEW_ROLE }` |
| Delete org member | `event.action: delete`, `event.resource_type: user`, `event.resource_id: USER_EMAIL`                           |

#### Project events

| Action                     | Query parameters                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Create project             | `event.action: create`, `event.resource_type: project`, `event.resouce_id: PROJ_NAME`                              |
| Update project             | `event.action: update`, `event.resource_type: project`, `event.resource_id: PROJECT_NAME`                          |
| Delete project             | `event.action: delete`, `event.resource_type: project`, `event.resource_id: PROJECT_NAME`                          |
| Invite project member      | `event.action: create`, `event.resource_type: user`, `event.resource_id: [ARRAY_OF_USER_EMAILS]`                   |
| Update project member role | `event.action: update`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, role: NEW_ROLE }`     |
| Delete project member      | `event.action: delete`, `event.resource_type: user`, `event.resource_id: { user: USER_EMAIL, project: PROJ_NAME }` |

#### Index events

| Action        | Query parameters                                                                        |
| ------------- | --------------------------------------------------------------------------------------- |
| Create index  | `event.action: create`, `event.resource_type: index`, `event.resouce_id: INDEX_NAME`    |
| Update index  | `event.action: update`, `event.resource_type: index`, `event.resource_id: INDEX_NAME`   |
| Delete index  | `event.action: delete`, `event.resource_type: index`, `event.resource_id: INDEX_NAME`   |
| Create backup | `event.action: create`, `event.resource_type: backup`, `event.resource_id: BACKUP_NAME` |
| Delete backup | `event.action: delete`, `event.resource_type: backup`, `event.resource_id: BACKUP_NAME` |

#### User and API key events

| Action         | Query parameters                                                                        |
| -------------- | --------------------------------------------------------------------------------------- |
| User login     | `event.action: login`, `event.resource_type: user`, `event.resouce_id: USERNAME`        |
| Create API key | `event.action: create`, `event.resource_type: api-key`, `event.resource_id: API_KEY_ID` |
| Delete API key | `event.action: delete`, `event.resource_type: api-key`, `event.resource_id: API_KEY_ID` |

#### Security and governance events

| Action                  | Query parameters                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------- |
| Create Private Endpoint | `event.action: create`, `event.resource_type: private-endpoints`, `event.resource_id: PRIVATE_ENDPOINT_ID` |
| Delete Private Endpoint | `event.action: delete`, `event.resource_type: private-endpoints`, `event.resource_id: PRIVATE_ENDPOINT_ID` |


## Data protection

### Encryption at rest

Pinecone encrypts stored data using the 256-bit Advanced Encryption Standard (AES-256) encryption algorithm.

### Encryption in transit

Pinecone uses standard protocols to encrypt user data in transit. Clients open HTTPS or gRPC connections to the Pinecone API; the Pinecone API gateway uses gRPC connections to user deployments in the cloud. These HTTPS and gRPC connections use the TLS 1.2 protocol with 256-bit Advanced Encryption Standard (AES-256) encryption.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=6da22e2916d66cf6ff03a4cfd7623705" alt="Diagram showing encryption protocols for user data in transit" data-og-width="4134" width="4134" data-og-height="2570" height="2570" data-path="images/encryption-in-transit-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=25e7ed0c6201c3a1f706cedf0ed823a5 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=ec43f21a1237d675e4c382352b673457 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=3bda7ada10d9343161aa691602ca5a5b 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=39f360b1bea6b4865d7508dc30741987 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=633cf84c092a6a9997b0b8e7daff1311 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/encryption-in-transit-2.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0035c658e3af1f534e4281e92391716b 2500w" />

Traffic is also encrypted in transit between the Pinecone backend and cloud infrastructure services, such as S3 and GCS. For more information, see [Google Cloud Platform](https://cloud.google.com/docs/security/encryption-in-transit) and [AWS security documentation](https://docs.aws.amazon.com/AmazonS3/userguide/UsingEncryption.html).


## Network security

### Proxies

The following Pinecone SDKs support the use of proxies:

* [Python SDK](/reference/python-sdk#proxy-configuration)
* [Node.js SDK](/reference/node-sdk#proxy-configuration)



# Upgrade your plan
Source: https://docs.pinecone.io/guides/assistant/admin/upgrade-billing-plan

Upgrade to a paid plan to access advanced features and limits.

This page describes how to upgrade from the free Starter plan to the [Standard or Enterprise plan](https://www.pinecone.io/pricing/), paying either with a credit/debit card or through a supported cloud marketplace.

<Note>
  To change your plan, you must be an [organization owner or billing admin](/guides/organizations/understanding-organizations#organization-roles).
</Note>

<Tip>
  To commit to annual spending, [contact Pinecone](https://www.pinecone.io/contact).
</Tip>


## Pay with a credit/debit card

To upgrade your plan to Standard or Enterprise and pay with a credit/debit card, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Credit / Debit card**.
4. Enter your credit card information.
5. Click **Upgrade**.

After upgrading, you will immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).


## Pay through the Google Cloud Marketplace

To upgrade your plan to Standard or Enterprise and pay through the Google Cloud Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through GCP**. This takes you to the [Pinecone listing](https://console.cloud.google.com/marketplace/product/pinecone-public/pinecone) in the Google Cloud Marketplace.
4. Click **Subscribe**.
5. On the **Order Summary** page, select a billing account, accept the terms and conditions, and click **Subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. On the **Your order request has been sent to Pinecone** modal, click **Sign up with Pinecone**. This takes you to a Google-specific Pinecone login page.
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).


## Pay through the AWS Marketplace

To upgrade your plan to Standard or Enterprise and pay through the AWS Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through AWS**. This takes you to the [Pinecone listing](https://aws.amazon.com/marketplace/pp/prodview-xhgyscinlz4jk) in the AWS Marketplace.
4. Click **View purchase options**.
5. On the **Subscribe to Pinecone Vector Database** page, review the offer and then click **Subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
6. You'll see a message stating that your subscription is in process. Click **Set up your account**. This takes you to an AWS-specific Pinecone login page.

   <Warning>
     If the [Pinecone subscription page](https://aws.amazon.com/marketplace/saas/ordering?productId=738798c3-eeca-494a-a2a9-161bee9450b2) shows a message stating, “You are currently subscribed to this offer,” contact your team members to request an invitation to the existing AWS-linked organization. The **Set up your account** button is clickable, but Pinecone does not create a new AWS-linked organization.
   </Warning>
7. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
8. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
9. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).


## Pay through the Microsoft Marketplace

To upgrade your plan to Standard or Enterprise and pay through the Microsoft Marketplace, do the following:

1. In the Pinecone console, go to [Settings > Billing > Plans](https://app.pinecone.io/organizations/-/settings/billing/plans).
2. Click **Upgrade** in the **Standard** or **Enterprise** plan section.
3. Click **Billing through Azure**. This takes you to the [Pinecone listing](https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas) in the Microsoft Marketplace.
4. Click **Get it now**.
5. Select the **Pinecone - Pay As You Go** plan.
6. Click **Subscribe**.
7. On the **Subscribe to Pinecone** page, select the required details and click **Review + subscribe**.

   <Note>The billing unit listed does not reflect the actual cost or metering of costs for Pinecone. See the [Pinecone Pricing page](https://www.pinecone.io/pricing/) for accurate details.</Note>
8. Click **Subscribe**.
9. After the subscription is approved, click **Configure account now**. This redirects you to an Microsoft-specific Pinecone login page.
10. Log in to your Pinecone account. Use the same authentication method as your existing Pinecone organization.
11. Select an organization from the list. You can only connect to organizations that are on the [Starter plan](https://www.pinecone.io/pricing/). Alternatively, you can opt to create a new organization.
12. Click **Connect to Pinecone** and follow the prompts.

Once your organization is connected and upgraded, you will receive a confirmation message. You will then immediately start paying for usage of your Pinecone indexes, including the serverless indexes that were free on the Starter plan. For more details about how costs are calculated, see [Understanding cost](/guides/manage-cost/understanding-cost).



---
**Navigation:** [← Previous](./27-install-the-latest-version.md) | [Index](./index.md) | [Next →](./29-chat-through-the-openai-compatible-interface.md)
