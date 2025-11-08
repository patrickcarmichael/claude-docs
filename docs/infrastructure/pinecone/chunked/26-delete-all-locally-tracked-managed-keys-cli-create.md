**Navigation:** [← Previous](./25-list-available-models.md) | [Index](./index.md) | [Next →](./27-install-the-latest-version.md)

# Delete all locally tracked managed keys (CLI-created and user-created)
pc auth local-keys prune


# Delete only CLI-created managed keys
pc auth local-keys prune --origin cli


# Delete only user-created managed keys
pc auth local-keys prune --origin user
```

**Delete a specific API key by ID (local and remote)**:

```bash  theme={null}
pc api-key delete --id "YOUR_API_KEY_ID"
```

This deletes any API key (managed or not) and cleans up the local record if it exists.

**Automatic deletion when creating a new key**:

When you run `pc api-key create --store` for a project that already has a CLI-created managed key, the CLI automatically deletes the old remote key before storing the new one. This prevents accumulating multiple managed keys per project.

<Note>
  `pc auth logout` deletes only the local references to managed keys. The keys remain active remotely in Pinecone. To fully clean up, run `pc auth local-keys prune` before logging out.
</Note>


## Local data storage

Authentication data is stored in `~/.config/pinecone/` with restricted permissions (0600):

**`secrets.yaml`** - Sensitive data:

* `oauth2_token`: Token associated with a user login (`pc auth login`)
* `client_id`, `client_secret`: Service account credentials
* `api_key`: Default (manually specified) API key
* `project_api_keys`: Managed keys per project

**`state.yaml`** - Context:

* `target_org`: Current organization (name and ID)
* `target_project`: Current project (name and ID)

**`config.yaml`** - Settings:

* `color`: Enable/disable colored output
* `environment`: Production or staging


## Check authentication status

```bash  theme={null}
pc auth status
```

Shows:

* Current authentication method
* Target organization and project
* Token expiration (for user login)
* Environment configuration



# CLI command reference
Source: https://docs.pinecone.io/reference/cli/command-reference



<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This document provides a complete reference for all Pinecone CLI commands.


## Command structure

The Pinecone CLI uses a hierarchical command structure. Each command consists of a primary command followed by one or more subcommands and optional flags.

```bash  theme={null}
pc <command> <subcommand> [flags]
pc <command> <subcommand> <subcommand> [flags]
```

For example:

```bash  theme={null}

# Top-level command with flags
pc target -o "organization-name" -p "project-name"


# Command (index) and subcommand (list)
pc index list


# Command (index) and subcommand (create) with flags
pc index create \
  --name my-index \
  --dimension 1536 \
  --metric cosine \
  --cloud aws \
  --region us-east-1


# Command (auth) and nested subcommands (local-keys prune) with flags
pc auth local-keys prune --id proj-abc123 --skip-confirmation
```


## Getting help

The CLI provides help for commands at every level:

```bash  theme={null}

# top-level help
pc --help
pc -h


# command help
pc auth --help
pc index --help
pc project --help


# subcommmand help
pc index create --help
pc project create --help
pc auth configure --help


# nested subcommand help
pc auth local-keys prune --help
```


## Exit codes

All commands return exit code `0` for success and `1` for error.


## Available commands

This section describes all commands offered by the Pinecone CLI.

### Top-level commands

<AccordionGroup>
  <Accordion title="pc login (Authenticate via user login)">
    **Description**

    Authenticate via a web browser. After login, set a [target org and project](/reference/cli/target-context) with `pc target` before accessing data. This command defaults to an initial organization and project to which
    you have access (these values display in the terminal), but you can change them with `pc target`.

    **Usage**

    ```bash  theme={null}
    pc login
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Log in via browser
    pc login

    # Then set target context
    pc target -o "my-org" -p "my-project"
    ```

    <Note>
      This is an alias for `pc auth login`. Both commands perform the same operation.
    </Note>
  </Accordion>

  <Accordion title="pc logout (Clear credentials / log out)">
    **Description**

    Clears all authentication data from local storage, including:

    * User login token
    * Service account credentials (client ID and secret)
    * Default (manually specified) API key
    * Locally managed keys (for all projects)
    * Target organization and project context

    **Usage**

    ```bash  theme={null}
    pc logout
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Clear all credentials and context
    pc logout
    ```

    <Note>
      This is an alias for `pc auth logout`. Both commands perform the same operation. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.
    </Note>
  </Accordion>

  <Accordion title="pc target (Set target organization and project)">
    **Description**

    Set the target organization and project for the CLI. Supports interactive organization and project selection or direct specification via flags.  For details, see [CLI target context](/reference/cli/target-context).

    **Usage**

    ```bash  theme={null}
    pc target [flags]
    ```

    **Flags**

    | Long flag           | Short flag | Description                    |
    | :------------------ | :--------- | :----------------------------- |
    | `--clear`           |            | Clear target context           |
    | `--json`            |            | Output in JSON format          |
    | `--org`             | `-o`       | Organization name              |
    | `--organization-id` |            | Organization ID                |
    | `--project`         | `-p`       | Project name                   |
    | `--project-id`      |            | Project ID                     |
    | `--show`            | `-s`       | Display current target context |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Interactive targeting after login
    pc login
    pc target

    # Set specific organization and project
    pc target -o "my-org" -p "my-project"

    # Show current context
    pc target --show

    # Clear all context
    pc target --clear
    ```
  </Accordion>

  <Accordion title="pc version (Show CLI version)">
    **Description**

    Displays version information for the CLI, including the version number, commit SHA, and build date.

    **Usage**

    ```bash  theme={null}
    pc version
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Display version information
    pc version
    ```
  </Accordion>

  <Accordion title="pc whoami (Show current user)">
    **Description**

    Displays information about the currently authenticated user. To use this command, you must be authenticated via user login.

    **Usage**

    ```bash  theme={null}
    pc whoami
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    pc whoami
    ```

    <Note>
      This is an alias for `pc auth whoami`. Both commands perform the same operation.
    </Note>
  </Accordion>
</AccordionGroup>

### Authentication

<AccordionGroup>
  <Accordion title="pc auth clear (Clear specific credentials)">
    **Description**

    Selectively clears specific authentication data without affecting other credentials. At least one flag is required.

    **Usage**

    ```bash  theme={null}
    pc auth clear [flags]
    ```

    **Flags**

    | Long flag           | Short flag | Description                                         |
    | :------------------ | :--------- | :-------------------------------------------------- |
    | `--api-key`         |            | Clear only the default (manually specified) API key |
    | `--service-account` |            | Clear only service account credentials              |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Clear only the default (manually specified) API key
    pc auth clear --api-key
    pc auth status

    # Clear service account
    pc auth clear --service-account
    ```

    <Note>
      More surgical than `pc auth logout`. Does not clear user login token or managed keys. For those, use `pc auth logout` or `pc auth local-keys prune`.
    </Note>
  </Accordion>

  <Accordion title="pc auth configure (Configure service account or API key)">
    **Description**

    Configures service account credentials or a default (manually specified) API key.

    Service accounts automatically target the organization and prompt for project selection, unless there is only one project. A default API key overrides any previously specified target organization/project context. When setting a service account, this operation clears the user login token, if one exists.
    For details, see [CLI target context](/reference/cli/target-context).

    **Usage**

    ```bash  theme={null}
    pc auth configure [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                          |
    | :---------------------- | :--------- | :--------------------------------------------------- |
    | `--api-key`             |            | Default API key to use for authentication            |
    | `--client-id`           |            | Service account client ID                            |
    | `--client-secret`       |            | Service account client secret                        |
    | `--client-secret-stdin` |            | Read client secret from stdin                        |
    | `--json`                |            | Output in JSON format                                |
    | `--project-id`          | `-p`       | Target project ID (optional, interactive if omitted) |
    | `--prompt-if-missing`   |            | Prompt for missing credentials                       |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Service account setup (auto-targets org and prompts for project)
    pc auth configure --client-id my-id --client-secret my-secret

    # Service account with specific project
    pc auth configure \
      --client-id my-id \
      --client-secret my-secret \
      -p proj-123

    # Default API key (overrides any target context)
    pc auth configure --api-key pcsk_abc123
    ```

    <Note>
      `pc auth configure --api-key "YOUR_API_KEY"` does the same thing as `pc config set-api-key "YOUR_API_KEY"`. To learn about targeting a project after authenticating with a service account, see [CLI target context](/reference/cli/target-context).
    </Note>
  </Accordion>

  <Accordion title="pc auth local-keys list (List managed keys)">
    **Description**

    Displays all [managed API keys](/reference/cli/authentication#managed-keys) stored locally by the CLI, with various details.

    **Usage**

    ```bash  theme={null}
    pc auth local-keys list [flags]
    ```

    **Flags**

    | Long flag  | Short flag | Description                                |
    | :--------- | :--------- | :----------------------------------------- |
    | `--json`   |            | Output in JSON format                      |
    | `--reveal` |            | Show the actual API key values (sensitive) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all locally managed keys
    pc auth local-keys list

    # Show key values
    pc auth local-keys list --reveal

    # After storing a key
    pc api-key create -n "my-key" --store
    pc auth local-keys list
    ```
  </Accordion>

  <Accordion title="pc auth local-keys prune (Delete managed keys)">
    **Description**

    Deletes locally stored [managed API keys](/reference/cli/authentication#managed-keys) from local storage and Pinecone's servers. Filters by origin (`cli`/`user`/`all`) or project ID.

    **Usage**

    ```bash  theme={null}
    pc auth local-keys prune [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                 |
    | :-------------------- | :--------- | :---------------------------------------------------------- |
    | `--dry-run`           |            | Preview deletions without applying                          |
    | `--id`                |            | Prune keys for specific project ID only                     |
    | `--json`              |            | Output in JSON format                                       |
    | `--origin`            | `-o`       | Filter by origin - `cli`, `user`, or `all` (default: `all`) |
    | `--skip-confirmation` |            | Skip confirmation prompt                                    |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Preview deletions
    pc auth local-keys prune --dry-run

    # Delete CLI-created keys only
    pc auth local-keys prune -o cli --skip-confirmation

    # Delete for specific project
    pc auth local-keys prune --id proj-abc123

    # Before/after check
    pc auth local-keys list
    pc auth local-keys prune -o cli
    pc auth local-keys list
    ```

    <Note>
      This deletes keys from both local storage and Pinecone servers. Use `--dry-run` to preview before committing.
    </Note>
  </Accordion>

  <Accordion title="pc auth login (Authenticate via user login)">
    **Description**

    Authenticate via user login in the web browser. After login, [set a target org and project](/reference/cli/target-context).

    **Usage**

    ```bash  theme={null}
    pc auth login
    pc login  # shorthand
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Login and set target
    pc auth login
    pc target -o "my-org" -p "my-project"
    pc index list
    ```

    <Note>
      Tokens expire after 30 minutes, but they refresh automatically for up to 24 hours. After that point, you must re-authenticate. Logging in clears any existing service account credentials. This command does the same thing as `pc login`.
    </Note>
  </Accordion>

  <Accordion title="pc auth logout (Clear authentication credentials)">
    **Description**

    Clears all authentication data from local storage, including:

    * User login token
    * Service account credentials (client ID and secret)
    * Default (manually specified) API key
    * Locally managed keys (for all projects)
    * Target organization and project context

    **Usage**

    ```bash  theme={null}
    pc auth logout
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Clear all credentials and context
    pc auth logout
    ```

    <Note>
      This command does the same thing as `pc logout`. Does not delete managed API keys from Pinecone's servers. Run `pc auth local-keys prune` before logging out to fully clean up.
    </Note>
  </Accordion>

  <Accordion title="pc auth status (Show authentication status)">
    **Description**

    Shows details about all configured authentication methods.

    **Usage**

    ```bash  theme={null}
    pc auth status [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Check status after login
    pc auth login
    pc auth status

    # JSON output for scripting
    pc auth status --json
    ```
  </Accordion>

  <Accordion title="pc auth whoami (Show current user information)">
    **Description**

    Displays information about the currently authenticated user. To use this command, you must be authenticated via user login.

    **Usage**

    ```bash  theme={null}
    pc auth whoami
    ```

    **Flags**

    None

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    pc auth whoami
    ```

    <Note>
      This command does the same thing as `pc whoami`.
    </Note>
  </Accordion>
</AccordionGroup>

### Indexes

<AccordionGroup>
  <Accordion title="pc index configure (Update index configuration)">
    **Description**

    Modifies the configuration of an existing index.

    **Usage**

    ```bash  theme={null}
    pc index configure [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                                    |
    | :---------------------- | :--------- | :------------------------------------------------------------- |
    | `--deletion_protection` | `-p`       | Enable or disable deletion protection -`enabled` or `disabled` |
    | `--json`                |            | Output in JSON format                                          |
    | `--name`                | `-n`       | Index name (required)                                          |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Enable deletion protection
    pc index configure -n my-index -p enabled

    # Verify changes
    pc index describe -n my-index
    ```

    <Note>
      Configuration changes may take some time to take effect.
    </Note>
  </Accordion>

  <Accordion title="pc index create (Create a new index)">
    **Description**

    Creates a new serverless index in your Pinecone project, with various configuration optons.

    **Usage**

    ```bash  theme={null}
    pc index create [flags]
    ```

    **Flags**

    | Long flag               | Short flag | Description                                                               |
    | :---------------------- | :--------- | :------------------------------------------------------------------------ |
    | `--cloud`               | `-c`       | Cloud provider - `aws`, `gcp`, or `azure` (required for serverless)       |
    | `--deletion_protection` |            | Deletion protection - `enabled` or `disabled`                             |
    | `--dimension`           | `-d`       | Vector dimension (required for standard indexes, optional for integrated) |
    | `--field_map`           |            | Field mapping for integrated embedding (JSON map)                         |
    | `--json`                |            | Output in JSON format                                                     |
    | `--metric`              | `-m`       | Similarity metric - `cosine`, `euclidean`, or `dotproduct` (required)     |
    | `--model`               |            | Integrated embedding model name                                           |
    | `--name`                | `-n`       | Index name (required)                                                     |
    | `--read_parameters`     |            | Read parameters for embedding model (JSON map)                            |
    | `--region`              | `-r`       | Cloud region                                                              |
    | `--source_collection`   |            | Name of the source collection from which to create the index              |
    | `--tags`                |            | Custom user tags (key=value pairs)                                        |
    | `--vector_type`         | `-v`       | Vector type - `dense` or `sparse` (serverless only)                       |
    | `--write_parameters`    |            | Write parameters for embedding model (JSON map)                           |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Create serverless index
    pc index create -n my-index -d 1536 -m cosine -c aws -r us-east-1

    # With integrated embedding model
    pc index create \
      -n my-index \
      -m cosine \
      -c aws \
      -r us-east-1 \
      --model multilingual-e5-large

    # With deletion protection
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r us-west-2 \
      --deletion_protection enabled

    # From collection
    pc index create \
      -n my-index \
      -d 1536 \
      -m cosine \
      -c aws \
      -r eu-west-1 \
      --source_collection my-collection
    ```

    <Note>
      For a list of valid regions for a serverless index, see [Create a serverless index](/guides/index-data/create-an-index).
    </Note>
  </Accordion>

  <Accordion title="pc index delete (Delete an index)">
    **Description**

    Permanently deletes an index and all its data. This operation cannot be undone.

    **Usage**

    ```bash  theme={null}
    pc index delete [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--name`  | `-n`       | Index name (required) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete an index
    pc index delete -n my-index

    # List before and after
    pc index list
    pc index delete -n test-index
    pc index list
    ```
  </Accordion>

  <Accordion title="pc index describe (Show index details)">
    **Description**

    Displays detailed configuration and status information for a specific index.

    **Usage**

    ```bash  theme={null}
    pc index describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |
    | `--name`  | `-n`       | Index name (required) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe an index
    pc index describe -n my-index

    # JSON output
    pc index describe -n my-index --json

    # Check newly created index
    pc index create -n test-index -d 1536 -m cosine -c aws -r us-east-1
    pc index describe -n test-index
    ```
  </Accordion>

  <Accordion title="pc index list (List all indexes)">
    **Description**

    Displays all indexes in your current target project, including various details.

    **Usage**

    ```bash  theme={null}
    pc index list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all indexes
    pc index list

    # JSON output for scripting
    pc index list --json

    # After creating indexes
    pc index create -n test-1 -d 768 -m cosine -c aws -r us-east-1
    pc index list
    ```
  </Accordion>
</AccordionGroup>

### Projects

<AccordionGroup>
  <Accordion title="pc project create (Create a new project)">
    **Description**

    Creates a new project in your [target organization](/reference/cli/target-context), using the specified configuration.

    **Usage**

    ```bash  theme={null}
    pc project create [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                                                    |
    | :------------------- | :--------- | :------------------------------------------------------------- |
    | `--force-encryption` |            | Enable encryption with CMEK                                    |
    | `--json`             |            | Output in JSON format                                          |
    | `--name`             | `-n`       | Project name (required)                                        |
    | `--target`           |            | Automatically target the project in the CLI after it's created |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Basic project creation
    pc project create -n "demo-project"
    ```
  </Accordion>

  <Accordion title="pc project delete (Delete a project)">
    **Description**

    Permanently deletes a project and all its resources. This operation cannot be undone.

    **Usage**

    ```bash  theme={null}
    pc project delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                                                 |
    | :-------------------- | :--------- | :---------------------------------------------------------- |
    | `--id`                | `-i`       | Project ID (optional, uses target project if not specified) |
    | `--json`              |            | Output in JSON format                                       |
    | `--skip-confirmation` |            | Skip confirmation prompt                                    |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete target project
    pc project delete

    # Delete specific project
    pc project delete -i proj-abc123

    # Skip confirmation
    pc project delete -i proj-abc123 --skip-confirmation
    ```

    <Note>
      Must delete all indexes and collections in the project first. If the deleted project is your current target, set a new target after deleting it.
    </Note>
  </Accordion>

  <Accordion title="pc project describe (Show project details)">
    **Description**

    Displays detailed information about a specific project, including various details.

    **Usage**

    ```bash  theme={null}
    pc project describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | Project ID (required) |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe a project
    pc project describe -i proj-abc123

    # JSON output
    pc project describe -i proj-abc123 --json

    # Find ID and describe
    pc project list
    pc project describe -i proj-abc123
    ```
  </Accordion>

  <Accordion title="pc project list (List all projects)">
    **Description**

    Displays all projects in your [target organization](/reference/cli/target-context), including various details.

    **Usage**

    ```bash  theme={null}
    pc project list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all projects
    pc project list

    # JSON output
    pc project list --json

    # List after login
    pc auth login
    pc auth target -o "my-org"
    pc project list
    ```
  </Accordion>

  <Accordion title="pc project update (Update project settings)">
    **Description**

    Modifies the configuration of the [target project](/reference/cli/target-context), or a specific project ID.

    **Usage**

    ```bash  theme={null}
    pc project update [flags]
    ```

    **Flags**

    | Long flag            | Short flag | Description                         |
    | :------------------- | :--------- | :---------------------------------- |
    | `--force-encryption` | `-f`       | Enable/disable encryption with CMEK |
    | `--id`               | `-i`       | Project ID (required)               |
    | `--json`             |            | Output in JSON format               |
    | `--name`             | `-n`       | New project name                    |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Update name
    pc project update -i proj-abc123 -n "new-name"
    ```
  </Accordion>
</AccordionGroup>

### Organizations

<AccordionGroup>
  <Accordion title="pc organization delete (Delete an organization)">
    **Description**

    Permanently deletes an organization and all its resources. This operation cannot be undone.

    **Usage**

    ```bash  theme={null}
    pc organization delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description                |
    | :-------------------- | :--------- | :------------------------- |
    | `--id`                | `-i`       | Organization ID (required) |
    | `--json`              |            | Output in JSON format      |
    | `--skip-confirmation` |            | Skip confirmation prompt   |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete an organization
    pc organization delete -i org-abc123

    # Skip confirmation
    pc organization delete -i org-abc123 --skip-confirmation
    ```

    <Note>
      This is a highly destructive action. Deletion is permanent. If the deleted organization is your current [target](/reference/cli/target-context), set a new target after deleting.
    </Note>
  </Accordion>

  <Accordion title="pc organization describe (Show organization details)">
    **Description**

    Displays detailed information about a specific organization, including name, ID, creation date, payment status, plan, and support tier.

    **Usage**

    ```bash  theme={null}
    pc organization describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                |
    | :-------- | :--------- | :------------------------- |
    | `--id`    | `-i`       | Organization ID (required) |
    | `--json`  |            | Output in JSON format      |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe an organization
    pc organization describe -i org-abc123

    # JSON output
    pc organization describe -i org-abc123 --json

    # Find ID and describe
    pc organization list
    pc organization describe -i org-abc123
    ```
  </Accordion>

  <Accordion title="pc organization list (List organizations)">
    **Description**

    Displays all organizations that the authenticated user has access to, including name, ID, creation date, payment status, plan, and support tier.

    **Usage**

    ```bash  theme={null}
    pc organization list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List all organizations
    pc organization list

    # JSON output
    pc organization list --json

    # List after login
    pc auth login
    pc organization list
    ```
  </Accordion>

  <Accordion title="pc organization update (Update organization settings)">
    **Description**

    Modifies the configuration of the [target organization](/reference/cli/target-context), or a specific organization ID.

    **Usage**

    ```bash  theme={null}
    pc organization update [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                |
    | :-------- | :--------- | :------------------------- |
    | `--id`    | `-i`       | Organization ID (required) |
    | `--json`  |            | Output in JSON format      |
    | `--name`  | `-n`       | New organization name      |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Update name
    pc organization update -i org-abc123 -n "new-name"

    # Verify changes
    pc organization update -i org-abc123 -n "Acme Corp"
    pc organization describe -i org-abc123
    ```
  </Accordion>
</AccordionGroup>

### API keys

<AccordionGroup>
  <Accordion title="pc api-key create (Create a new API key)">
    **Description**

    Creates a new API key for the current [target project](/reference/cli/target-context) or a specific project ID. Optionally stores the key locally for CLI use.

    **Usage**

    ```bash  theme={null}
    pc api-key create [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                                                             |
    | :-------- | :--------- | :-------------------------------------------------------------------------------------- |
    | `--id`    | `-i`       | Project ID (optional, uses target project if not specified)                             |
    | `--json`  |            | Output in JSON format                                                                   |
    | `--name`  | `-n`       | Key name (required)                                                                     |
    | `--roles` |            | Roles to assign (default: `ProjectEditor`)                                              |
    | `--store` |            | Store the key locally for CLI use (automatically replaces any existing CLI-managed key) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Basic key creation
    pc api-key create -n "my-key"

    # Create and store locally
    pc api-key create -n "my-key" --store

    # Create with specific role
    pc api-key create -n "my-key" --store --roles ProjectEditor

    # Create for specific project
    pc api-key create -n "my-key" -i proj-abc123
    ```

    <Note>
      API keys are scoped to a specific organization and project.
    </Note>
  </Accordion>

  <Accordion title="pc api-key delete (Delete an API key)">
    **Description**

    Permanently deletes an API key. Applications using this key immediately lose access.

    **Usage**

    ```bash  theme={null}
    pc api-key delete [flags]
    ```

    **Flags**

    | Long flag             | Short flag | Description              |
    | :-------------------- | :--------- | :----------------------- |
    | `--id`                | `-i`       | API key ID (required)    |
    | `--skip-confirmation` |            | Skip confirmation prompt |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Delete an API key
    pc api-key delete -i key-abc123

    # Skip confirmation
    pc api-key delete -i key-abc123 --skip-confirmation

    # Delete and clean up local storage
    pc api-key delete -i key-abc123
    pc auth local-keys prune --skip-confirmation
    ```

    <Note>
      Deletion is permanent. Applications using this key immediately lose access to Pinecone.
    </Note>
  </Accordion>

  <Accordion title="pc api-key describe (Show API key details)">
    **Description**

    Displays detailed information about a specific API key, including its name, ID, project ID, and roles.

    **Usage**

    ```bash  theme={null}
    pc api-key describe [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | API key ID (required) |
    | `--json`  |            | Output in JSON format |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Describe an API key
    pc api-key describe -i key-abc123

    # JSON output
    pc api-key describe -i key-abc123 --json

    # Find ID and describe
    pc api-key list
    pc api-key describe -i key-abc123
    ```

    <Note>
      Does not display the actual key value.
    </Note>
  </Accordion>

  <Accordion title="pc api-key list (List all API keys)">
    **Description**

    Displays a list of all of the [target project's](/reference/cli/target-context) API keys, as found in  Pinecone (regardless of whether they are stored locally by the CLI). Displays various details about each key, including name, ID, project ID, and roles.

    **Usage**

    ```bash  theme={null}
    pc api-key list [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description                                                 |
    | :-------- | :--------- | :---------------------------------------------------------- |
    | `--id`    | `-i`       | Project ID (optional, uses target project if not specified) |
    | `--json`  |            | Output in JSON format                                       |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # List keys for target project
    pc api-key list

    # List for specific project
    pc api-key list -i proj-abc123

    # JSON output
    pc api-key list --json
    ```

    <Note>
      Does not display key values.
    </Note>
  </Accordion>

  <Accordion title="pc api-key update (Update API key settings)">
    **Description**

    Updates the name and roles of an API key.

    **Usage**

    ```bash  theme={null}
    pc api-key update [flags]
    ```

    **Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--id`    | `-i`       | API key ID (required) |
    | `--json`  | `-j`       | Output in JSON format |
    | `--name`  | `-n`       | New key name          |
    | `--roles` | `-r`       | Roles to assign       |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Update name
    pc api-key update -i key-abc123 -n "new-name"

    # Update roles
    pc api-key update -i key-abc123 -r ProjectEditor

    # Verify changes
    pc api-key update -i key-abc123 -n "production-key"
    pc api-key describe -i key-abc123
    ```

    <Note>
      Cannot change the actual key. If you need a different key, create a new one.
    </Note>
  </Accordion>
</AccordionGroup>

### Config

<AccordionGroup>
  <Accordion title="pc config get-api-key (Show configured API key)">
    **Description**

    Displays the currently configured default (manually specified) API key, if set. By default, the full value of the key is not displayed.

    **Usage**

    ```bash  theme={null}
    pc config get-api-key
    ```

    **Flags**

    | Long flag  | Short flag | Description                               |
    | :--------- | :--------- | :---------------------------------------- |
    | `--reveal` |            | Show the actual API key value (sensitive) |

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Get current API key
    pc config get-api-key

    # Verify after setting
    pc config set-api-key pcsk_abc123
    pc config get-api-key
    ```
  </Accordion>

  <Accordion title="pc config set-api-key (Set default API key)">
    **Description**

    Sets a default API key for the CLI to use for authentication. Provides direct access to control plane operations, but not Admin API operations.

    **Usage**

    ```bash  theme={null}
    pc config set-api-key "YOUR_API_KEY"
    ```

    **Flags**

    None (takes API key as argument)

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Set default API key
    pc config set-api-key pcsk_abc123

    # Use immediately without targeting
    pc config set-api-key pcsk_abc123
    pc index list

    # Verify it's set
    pc auth status
    ```

    <Note>
      `pc config set-api-key "YOUR_API_KEY"` does the same thing as `pc auth configure --api-key "YOUR_API_KEY"`. For control plane operations, a default API key implicitly overrides any previously set [target context](/reference/cli/target-context), because Pinecone API keys are scoped to a specific organization and project.
    </Note>
  </Accordion>

  <Accordion title="pc config set-color (Enable/disable colored output)">
    **Description**

    Enables or disables colored output in CLI responses. Useful for terminal compatibility or log file generation.

    **Usage**

    ```bash  theme={null}
    pc config set-color true
    pc config set-color false
    ```

    **Flags**

    None (takes boolean as argument)

    **Global Flags**

    | Long flag | Short flag | Description           |
    | :-------- | :--------- | :-------------------- |
    | `--help`  | `-h`       | Show help information |
    | `--quiet` | `-q`       | Suppress output       |

    **Example**

    ```bash  theme={null}
    # Enable colored output
    pc config set-color true

    # Disable colored output for CI/CD
    pc config set-color false

    # Test the change
    pc config set-color false
    pc index list
    ```
  </Accordion>
</AccordionGroup>



# CLI installation
Source: https://docs.pinecone.io/reference/cli/installation



<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This document describes how to install the Pinecone CLI on your local machine.


## Platforms

Pinecone's CLI is available for the following platforms:

* **macOS**: Intel (x86\_64) and Apple Silicon (ARM64)
* **Linux**: x86\_64, ARM64, and i386 architectures
* **Windows**: x86\_64 and i386 architectures


## Installation

### Homebrew (macOS)

The most convenient way to install the CLI on Mac:

```bash  theme={null}
brew tap pinecone-io/tap
brew install pinecone-io/tap/pinecone
```

To upgrade to the latest version:

```bash  theme={null}
brew update
brew upgrade pinecone
```

### Direct download (all platforms)

Pre-built binaries for all supported platforms are available on the [GitHub Releases page](https://github.com/pinecone-io/cli/releases).

### Build from source

To build from source, see the [CONTRIBUTING.md](https://github.com/pinecone-io/cli/blob/main/CONTRIBUTING.md) file for detailed instructions. To build from source, you need Go v1.23+.



# CLI overview
Source: https://docs.pinecone.io/reference/cli/overview



<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

The Pinecone CLI (`pc`) is a command-line tool for managing Pinecone infrastructure (projects, organizations, indexes, and API keys) directly from your terminal.

Use it to:

* Automate infrastructure operations
* Integrate Pinecone into CI/CD pipelines
* Manage resources without using the web console


## Supported

The CLI currently supports the following features:

* Authentication (user login, service account, API key)
* Projects and organizations (create, update, delete, list)
* Indexes (create, configure, delete, list)
* API key management


## Not yet supported

The CLI does not yet support the following features:

* Vector and namespace operations
* Bulk data imports
* Index statistics
* Inference (embeddings, reranking)
* Assistant operations
* Dedicated read nodes

<Tip>
  For these features, use Pinecone's [REST API](/reference/api) or SDKs: [Python](/reference/python-sdk), [Node.js](/reference/node-sdk), [Java](/reference/java-sdk), [Go](/reference/go-sdk), [.NET](/reference/dotnet-sdk), or [Rust](/reference/rust-sdk) (alpha).
</Tip>



# CLI quickstart
Source: https://docs.pinecone.io/reference/cli/quickstart



<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

1. Install the Pinecone CLI:

   <CodeGroup>
     ```shell macOS theme={null}
     # Using Homebrew (https://brew.sh)
     brew tap pinecone-io/tap
     brew install pinecone-io/tap/pinecone
     ```

     ```shell Linux/Windows theme={null}
     Download pre-build binaries from https://github.com/pinecone-io/cli/releases
     ```
   </CodeGroup>

2. Authenticate the CLI with Pinecone by [user login](/reference/cli/authentication#user-login):

   ```bash  theme={null}
   # Authenticate in a web browser
   pc auth login
   ```

   To authenticate with Pinecone, visit the URL displayed in the terminal. After you sign in, the terminal displays a success message:

   ```
   [SUCCESS] Logged in as user@example.com. Defaulted to organization ID: <ORGANIZATION_ID>

   [INFO] Target org set to <ORGANIZATION_NAME>
   [INFO] Target project set to <PROJECT_NAME>
   ```

   <Note>
     As shown by the `[INFO]` messages, this command automatically sets a [target organization and project](/reference/cli/target-context) for the CLI.
   </Note>

3. If necessary, target a different organization and/or project:

   ```bash  theme={null}
   pc auth target -o "my-org-name" -p "my-project-name"
   ```

4. List the indexes in the project:

   ```bash  theme={null}
   pc index list
   ```


## Next steps

See the [command reference](/reference/cli/command-reference) to learn about the various commands offered by the CLI.



# CLI target context
Source: https://docs.pinecone.io/reference/cli/target-context



<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Most CLI operations happen within the context of a specific organization and project. The **target context** is the organization and project scope that the CLI uses when running commands.

Before setting target context, you must authenticate with the CLI. See [CLI authentication](/reference/cli/authentication) for details on authentication methods.


## Why target context matters

By specifying a target organization and/or project, you're telling the CLI which resources to operate on.

* **Control plane operations** (creating indexes, listing indexes): Always happen within a specific project.
* **Admin API operations**:
  * Organization operations don't require target context. They operate on organizations you have access to.
  * Project management operations are scoped to your target organization. For example, running `pc project list` shows projects in the target org.
  * API key operations are scoped to the target project, unless you specify `--id`.


## How target context works

How the CLI sets and uses target context depends on your authentication method and how you configure it.

### User login

When you authenticate with `pc auth login`, the CLI automatically [targets](/reference/cli/target-context):

* The default organization returned by the server for your user.
* The first project in the list of that organization's projects.

However, you can change organization and project as needed:

```bash  theme={null}
pc auth login
pc target -o "my-org" -p "my-project"
```

### Service account

**Configured via CLI command**

When you configure a service account with `pc auth configure --client-id --client-secret`, the CLI automatically targets the organization associated with the service account (service accounts belong to a single organization). Then, to target a project:

* If the selected organization has only one project, the CLI automatically targets it.
* If that organization has multiple projects, the CLI prompts you to select one (or you can use the `--project-id` flag).
* If it doesn't have any projects, create one and then target it manually.

To change to a specific target project:

```bash  theme={null}
pc target -p "different-project"
```

Or, to select a project interactively:

```bash  theme={null}
pc target
```

**Configured via environment variables**

If you set service account credentials via environment variables (`PINECONE_CLIENT_ID` and `PINECONE_CLIENT_SECRET`) without running `pc auth configure`, the CLI does **not** automatically set any target context. You must explicitly set it with `pc target`.

Service accounts are scoped to a single organization. You can only target the organization associated with your service account credentials. To do this, and also target a specific project within that organization:

```bash  theme={null}
pc target -o "my-org" -p "my-project"
```

Or, to select a project interactively (the CLI discovers the organization automatically):

```bash  theme={null}
pc target
```

### API key

When you set a default API key (with `pc auth configure --api-key` or the `PINECONE_API_KEY` environment variable), the CLI does **not** change or clear its stored target context. However, in this scenario, control plane operations **do** use the API key's organization and project — not the CLI's saved target context (regardless of any calls you've made to `pc target`, or the output of `pc target --show`). This happens because Pinecone API keys are always scoped to a specific organization and project, and they cannot access resources outside of that scope.

<Note>
  Because Pinecone API keys cannot be used to authenticate calls to the Admin API, Admin API operations still authentiate with your user login token or service account credentials (if available).
</Note>

```bash  theme={null}
pc auth login
pc target -o "my-org" -p "my-project"

# Setting an API key doesn't change stored target context
pc auth configure --api-key "YOUR_API_KEY"
pc target --show  # Still shows my-org and my-project, but they're not used for control plane operations
```


## Viewing and managing target context

To view your current target organization and project:

```bash  theme={null}

# Show current target context
pc target --show


# Clear target context
pc target --clear
```



# .NET SDK
Source: https://docs.pinecone.io/reference/dotnet-sdk



<Tip>
  See the [.NET SDK documentation](https://github.com/pinecone-io/pinecone-dotnet-client/blob/main/README.md) for full installation instructions and usage examples.

  To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/pinecone-dotnet-client/issues).
</Tip>


## Requirements

To use this Python .NET SDK, ensure that your project is targeting one of the following:

* .NET Standard 2.0+
* .NET Core 3.0+
* .NET Framework 4.6.2+
* .NET 6.0+


## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and .NET SDK versions are as follows:

| API version        | SDK version |
| :----------------- | :---------- |
| `2025-04` (latest) | v4.x        |
| `2025-01`          | v3.x        |
| `2024-10`          | v2.x        |
| `2024-07`          | v1.x        |
| `2024-04`          | v0.x        |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.


## Install

To add the latest version of the [.NET SDK](https://github.com/pinecone-io/pinecone-dotnet-client) to your project, run the following command:

<CodeGroup>
  ```shell .NET Core CLI theme={null}
  dotnet add package Pinecone.Client 
  ```

  ```shell NuGet CLI theme={null}
  nuget install Pinecone.Client
  ```
</CodeGroup>

To add a specific version of the [.NET SDK](https://github.com/pinecone-io/pinecone-dotnet-client) to your project, run the following command:

<CodeGroup>
  ```shell .NET Core CLI theme={null}
  dotnet add package Pinecone.Client --version <version>
  ```

  ```shell NuGet CLI theme={null}
  nuget install Pinecone.Client -Version <version>
  ```
</CodeGroup>

To check your SDK version, run the following command:

<CodeGroup>
  ```shell .NET Core CLI theme={null}
  dotnet list package
  ```

  ```shell NuGet CLI theme={null}
  nuget list 
  ```
</CodeGroup>


## Upgrade

<Warning>
  Before upgrading to `v4.0.0`, update all relevant code to account for the breaking changes explained [here](/release-notes/2025#2025-05-14-2).
</Warning>

If you are already using `Pinecone.Client` in your project, upgrade to the latest version as follows:

<CodeGroup>
  ```shell .NET Core CLI theme={null}
  dotnet add package Pinecone.Client 
  ```

  ```shell NuGet CLI theme={null}
  nuget install Pinecone.Client
  ```
</CodeGroup>


## Initialize

Once installed, you can import the SDK and then use an [API key](/guides/production/security-overview#api-keys) to initialize a client instance:

```csharp C# theme={null}
using Pinecone;

var pinecone = new PineconeClient("YOUR_API_KEY");
```


## Proxy configuration

If your network setup requires you to interact with Pinecone through a proxy, configure the HTTP client as follows:

```csharp  theme={null}
using System.Net;
using Pinecone;

var pinecone = new PineconeClient("PINECONE_API_KEY", new ClientOptions
{
    HttpClient = new HttpClient(new HttpClientHandler
    {
        Proxy = new WebProxy("PROXY_HOST:PROXY_PORT")
    })
});
```

If you're building your HTTP client using the [HTTP client factory](https://learn.microsoft.com/en-us/dotnet/core/extensions/httpclient-factory#configure-the-httpmessagehandler), use the `ConfigurePrimaryHttpMessageHandler` method to configure the proxy:

```csharp  theme={null}
   .ConfigurePrimaryHttpMessageHandler(() => new HttpClientHandler
       {
           Proxy = new WebProxy("PROXY_HOST:PROXY_PORT")
       });
```



# Go SDK
Source: https://docs.pinecone.io/reference/go-sdk



<Tip>
  See the [Go SDK documentation](https://github.com/pinecone-io/go-pinecone/blob/main/README.md) for full installation instructions and usage examples.

  To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/go-pinecone/issues).
</Tip>


## Requirements

The Pinecone Go SDK requires a Go version with [modules](https://go.dev/wiki/Modules) support.


## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and Go SDK versions are as follows:

| API version | SDK version |
| :---------- | :---------- |
| `2025-04`   | v4.x        |
| `2025-01`   | v3.x        |
| `2024-10`   | v2.x        |
| `2024-07`   | v1.x        |
| `2024-04`   | v0.x        |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.


## Install

To install the latest version of the [Go SDK](https://github.com/pinecone-io/go-pinecone), add a dependency to the current module:

```shell  theme={null}
go get github.com/pinecone-io/go-pinecone/v4/pinecone
```

To install a specific version of the Go SDK, run the following command:

```shell  theme={null}
go get github.com/pinecone-io/go-pinecone/v4/pinecone@<version>
```

To check your SDK version, run the following command:

```shell  theme={null}
go list -u -m all | grep go-pinecone
```


## Upgrade

<Warning>
  Before upgrading to `v3.0.0` or later, update all relevant code to account for the breaking changes explained [here](/release-notes/2025#2025-02-07-4).
</Warning>

If you already have the Go SDK, upgrade to the latest version as follows:

```shell  theme={null}
go get -u github.com/pinecone-io/go-pinecone/v4/pinecone@latest
```


## Initialize

Once installed, you can import the SDK and then use an [API key](/guides/production/security-overview#api-keys) to initialize a client instance:

```Go  theme={null}
package main

import (
    "context"
    "log"

    "github.com/pinecone-io/go-pinecone/v4/pinecone"
)

func main() {
    ctx := context.Background()

    pc, err := pinecone.NewClient(pinecone.NewClientParams{
        ApiKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatalf("Failed to create Client: %v", err)
    }
} 
```



# Java SDK
Source: https://docs.pinecone.io/reference/java-sdk



<Tip>
  See the [Pinecone Java SDK
  documentation](https://github.com/pinecone-io/pinecone-java-client/blob/main/README.md) for full installation
  instructions and usage examples.

  To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/pinecone-java-client/issues).
</Tip>


## Requirements

The Pinecone Java SDK Java 1.8 or later.


## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and Java SDK versions are as follows:

| API version        | SDK version |
| :----------------- | :---------- |
| `2025-04` (latest) | v5.x        |
| `2025-01`          | v4.x        |
| `2024-10`          | v3.x        |
| `2024-07`          | v2.x        |
| `2024-04`          | v1.x        |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.


## Install

To install the latest version of the [Java SDK](https://github.com/pinecone-io/pinecone-java-client), add a dependency to the current module:

```shell Java theme={null}

# Maven
<dependency>
  <groupId>io.pinecone</groupId>
  <artifactId>pinecone-client</artifactId>
  <version>5.0.0</version>
</dependency>


# Gradle
implementation "io.pinecone:pinecone-client:5.0.0"
```

Alternatively, you can download the standalone uberjar [pinecone-client-4.0.0-all.jar](https://repo1.maven.org/maven2/io/pinecone/pinecone-client/4.0.0/pinecone-client-4.0.0-all.jar), which bundles the Pinecone SDK and all dependencies together. You can include this in your classpath like you do with any third-party JAR without having to obtain the `pinecone-client` dependencies separately.


## Upgrade

<Warning>
  Before upgrading to `v4.0.0`, update all relevant code to account for the breaking changes explained [here](/release-notes/2025#2025-02-07-3).
</Warning>

If you are already using the Java SDK, upgrade the dependency in the current module to the latest version:

```shell Java theme={null}

# Maven
<dependency>
  <groupId>io.pinecone</groupId>
  <artifactId>pinecone-client</artifactId>
  <version>5.0.0</version>
</dependency>


# Gradle
implementation "io.pinecone:pinecone-client:5.0.0"
```


## Initialize

Once installed, you can import the SDK and then use an [API key](/guides/production/security-overview#api-keys) to initialize a client instance:

```Java  theme={null}
import io.pinecone.clients.Pinecone;
import org.openapitools.db_control.client.model.*;

public class InitializeClientExample {
    public static void main(String[] args) {
        Pinecone pc = new Pinecone.Builder("YOUR_API_KEY").build();
    }
}
```



# Node.js SDK
Source: https://docs.pinecone.io/reference/node-sdk



<Tip>
  See the [Pinecone Node.js SDK
  documentation](https://sdk.pinecone.io/typescript/) for full installation
  instructions, usage examples, and reference information.

  To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/pinecone-ts-client/issues).
</Tip>


## Requirements

The Pinecone Node SDK requires TypeScript 4.1 or later and Node 18.x or later.


## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and Node.js SDK versions are as follows:

| API version        | SDK version |
| :----------------- | :---------- |
| `2025-04` (latest) | v6.x        |
| `2025-01`          | v5.x        |
| `2024-10`          | v4.x        |
| `2024-07`          | v3.x        |
| `2024-04`          | v2.x        |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.


## Install

To install the latest version of the [Node.js SDK](https://github.com/pinecone-io/pinecone-ts-client), written in TypeScript, run the following command:

```Shell  theme={null}
npm install @pinecone-database/pinecone
```

To check your SDK version, run the following command:

```Shell  theme={null}
npm list | grep @pinecone-database/pinecone
```


## Upgrade

If you already have the Node.js SDK, upgrade to the latest version as follows:

```Shell  theme={null}
npm install @pinecone-database/pinecone@latest
```


## Initialize

Once installed, you can import the library and then use an [API key](/guides/projects/manage-api-keys) to initialize a client instance:

```JavaScript  theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({
    apiKey: 'YOUR_API_KEY'
});
```


## Proxy configuration

If your network setup requires you to interact with Pinecone through a proxy, you can pass a custom `ProxyAgent` from the [`undici` library](https://undici.nodejs.org/#/). Below is an example of how to construct an `undici` `ProxyAgent` that routes network traffic through a [`mitm` proxy server](https://mitmproxy.org/) while hitting Pinecone's `/indexes` endpoint.

<Note>
  The following strategy relies on Node's native [`fetch`](https://nodejs.org/docs/latest/api/globals.html#fetch) implementation, released in Node v16 and stabilized in Node v21. If you are running Node versions 18-21, you may experience issues stemming from the instability of the feature. There are currently no known issues related to proxying in Node v18+.
</Note>

```JavaScript JavaScript theme={null}
import {
  Pinecone,
  type PineconeConfiguration,
} from '@pinecone-database/pinecone';
import { Dispatcher, ProxyAgent } from 'undici';
import * as fs from 'fs';

const cert = fs.readFileSync('path/to/mitmproxy-ca-cert.pem');

const client = new ProxyAgent({
  uri: 'https://your-proxy.com',
  requestTls: {
    port: 'YOUR_PROXY_SERVER_PORT',
    ca: cert,
    host: 'YOUR_PROXY_SERVER_HOST',
  },
});

const customFetch = (
  input: string | URL | Request,
  init: RequestInit | undefined
) => {
  return fetch(input, {
    ...init,
    dispatcher: client as Dispatcher,
    keepalive: true,  # optional
  });
};

const config: PineconeConfiguration = {
  apiKey:
    'YOUR_API_KEY',
  fetchApi: customFetch,
};

const pc = new Pinecone(config);

const indexes = async () => {
  return await pc.listIndexes();
};

indexes().then((response) => {
  console.log('My indexes: ', response);
});
```



# Introduction
Source: https://docs.pinecone.io/reference/pinecone-sdks




## Pinecone SDKs

Official Pinecone SDKs provide convenient access to the [Pinecone APIs](/reference/api/introduction).

<CardGroup cols={3}>
  <Card title="Python SDK" icon="python" href="/reference/python-sdk" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/node-sdk" />

  <Card title="Java SDK" icon="java" href="/reference/java-sdk" />

  <Card title="Go SDK" icon="golang" href="/reference/go-sdk" />

  <Card title=".NET SDK" icon="microsoft" href="/reference/dotnet-sdk" />

  <Card title="Rust SDK" icon="rust" href="/reference/rust-sdk" />
</CardGroup>


## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and SDK versions are as follows:

|                                     | `2025-04` | `2025-01` | `2024-10` | `2024-07`     | `2024-04` |
| ----------------------------------- | :-------- | :-------- | :-------- | :------------ | :-------- |
| [Python SDK](/reference/python-sdk) | v7.x      | v6.x      | v5.3.x    | v5.0.x-v5.2.x | v4.x      |
| [Node.js SDK](/reference/node-sdk)  | v6.x      | v5.x      | v4.x      | v3.x          | v2.x      |
| [Java SDK](/reference/java-sdk)     | v5.x      | v4.x      | v3.x      | v2.x          | v1.x      |
| [Go SDK](/reference/go-sdk)         | v4.x      | v3.x      | v2.x      | v1.x          | v0.x      |
| [.NET SDK](/reference/dotnet-sdk)   | v4.x      | v3.x      | v2.x      | v1.x          | v0.x      |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.

<Note>
  SDK versions are not available for the current release candidate API (`2025-10`).
</Note>


## Limitations

While Pinecone tracks read unit usage with decimal precision, the Pinecone API and SDKs round these values up to the nearest whole number in query, fetch, and list responses. For example, if a query uses 0.45 read units, the API and SDKs will report it as 1 read unit.

For precise read unit reporting, see [index-level metrics](/guides/production/monitoring) or the organization-wide [Usage dashboard](/guides/manage-cost/monitor-usage-and-costs#monitor-organization-level-usage-and-costs).


## Community SDKs

Find community-contributed SDKs for Pinecone. These libraries are not supported by Pinecone.

* [Ruby SDK](https://github.com/ScotterC/pinecone) (contributed by [ScotterC](https://github.com/ScotterC))

* [Scala SDK](https://github.com/cequence-io/pinecone-scala) (contributed by [cequence-io](https://github.com/cequence-io))

* [PHP SDK](https://github.com/probots-io/pinecone-php) (contributed by [protobots-io](https://github.com/probots-io))



# Python SDK
Source: https://docs.pinecone.io/reference/python-sdk



The Pinecone Python SDK is distributed on PyPI using the package name `pinecone`. By default, the `pinecone` package has a minimal set of dependencies and interacts with Pinecone via HTTP requests. However, you can install the following extras to unlock additional functionality:

* `pinecone[grpc]` adds dependencies on `grpcio` and related libraries needed to run data operations such as upserts and queries over [gRPC](https://grpc.io/) for a modest performance improvement.

* `pinecone[asyncio]` adds a dependency on `aiohttp` and enables usage of `async` methods for use with [asyncio](https://docs.python.org/3/library/asyncio.html). For more details, see [Asyncio support](#async-requests).

<Tip>
  See the [Pinecone Python SDK
  documentation](https://sdk.pinecone.io/python/)
  for full installation instructions, usage examples, and reference information.

  To make a feature request or report an issue, please [file an issue](https://github.com/pinecone-io/pinecone-python-client/issues).
</Tip>


## Requirements

The Pinecone Python SDK requires Python 3.9 or later. It has been tested with CPython versions from 3.9 to 3.13.


## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and Python SDK versions are as follows:

| API version        | SDK version   |
| :----------------- | :------------ |
| `2025-04` (latest) | v7.x          |
| `2025-01`          | v6.x          |
| `2024-10`          | v5.3.x        |
| `2024-07`          | v5.0.x-v5.2.x |
| `2024-04`          | v4.x          |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.


## Install

To install the latest version of the [Python SDK](https://github.com/pinecone-io/pinecone-python-client), run the following command:

```shell  theme={null}

---
**Navigation:** [← Previous](./25-list-available-models.md) | [Index](./index.md) | [Next →](./27-install-the-latest-version.md)
