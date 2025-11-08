**Navigation:** [← Previous](./03-build-output-configuration.md) | [Index](./index.md) | [Next →](./05-no-cors-headers.md)

---

# vercel remove

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel remove` command, which can be shortened to `vercel rm`, is used to remove deployments either by ID or for a specific Vercel Project.

You can also remove deployments from the Project Overview page on the Vercel Dashboard.

## [Usage](#usage)

terminal

```
vercel remove [deployment-url]
```

Using the `vercel remove` command to remove a deployment from the Vercel platform.

## [Extended Usage](#extended-usage)

terminal

```
vercel remove [deployment-url-1 deployment-url-2]
```

Using the `vercel remove` command to remove multiple deployments from the Vercel platform.

terminal

```
vercel remove [project-name]
```

Using the `vercel remove` command to remove all deployments for a Vercel Project from the Vercel platform.

By using the [project name](/docs/projects/overview), the entire Vercel Project will be removed from the current scope unless the `--safe` is used.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel remove` command.

### [Safe](#safe)

The `--safe` option, shorthand `-s`, can be used to skip the removal of deployments with an active preview URL or production domain when a Vercel Project is provided as the parameter.

terminal

```
vercel remove my-project --safe
```

Using the `vercel remove` command with the `--safe` option.

### [Yes](#yes)

The `--yes` option, shorthand `-y`, can be used to skip the confirmation step for a deployment or Vercel Project removal.

terminal

```
vercel remove my-deployment.com --yes
```

Using the `vercel remove` command with the `--yes` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel remove` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel rollback"
description: "Learn how to roll back your production deployments to previous deployments using the vercel rollback CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/rollback"
--------------------------------------------------------------------------------

# vercel rollback

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel rollback` command is used to [roll back production deployments](/docs/instant-rollback) to previous deployments.

## [Usage](#usage)

terminal

```
vercel rollback
```

Using `vercel rollback` fetches the status of any rollbacks in progress.

terminal

```
vercel rollback [deployment-id or url]
```

Using `vercel rollback` rolls back to previous deployment.

On the hobby plan, you can only [roll back](/docs/instant-rollback#who-can-roll-back-deployments) to the previous production deployment. If you attempt to pass in a deployment id or url from an earlier deployment, you will be given an error:

`   To roll back further than the previous production deployment, upgrade to pro   `

.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel rollback` command.

### [Timeout](#timeout)

The `--timeout` option is the time that the `vercel rollback` command will wait for the rollback to complete. It does not affect the actual rollback which will continue to proceed.

When rolling back a deployment, a timeout of `0` will immediately exit after requesting the rollback.

terminal

```
vercel rollback https://example-app-6vd6bhoqt.vercel.app
```

Using the `vercel rollback` command to the `[https://example-app-6vd6bhoqt.vercel.app](https://example-app-6vd6bhoqt.vercel.app)` deployment.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel rollback` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel rolling-release"
description: "Learn how to manage your project's rolling releases using the vercel rolling-release CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/rolling-release"
--------------------------------------------------------------------------------

# vercel rolling-release

Copy page

Ask AI about this page

Last updated June 24, 2025

The `vercel rolling-release` command (also available as `vercel rr`) is used to manage your project's rolling releases. [Rolling releases](/docs/rolling-releases) allow you to gradually roll out new deployments to a small fraction of your users before promoting them to everyone.

## [Usage](#usage)

terminal

```
vercel rolling-release [command]
```

Using `vercel rolling-release` with a specific command to manage rolling releases.

## [Commands](#commands)

### [configure](#configure)

Configure rolling release settings for a project.

terminal

```
vercel rolling-release configure --cfg='{"enabled":true, "advancementType":"manual-approval", "stages":[{"targetPercentage":10},{"targetPercentage":50},{"targetPercentage":100}]}'
```

Using the `vercel rolling-release configure` command to set up a rolling release with manual approval stages.

### [start](#start)

Start a rolling release for a specific deployment.

terminal

```
vercel rolling-release start --dpl=dpl_abc //Where "dpl_abc" is the deployment id or URL
```

Using the `vercel rolling-release start` command to begin a rolling release for a deployment.

### [approve](#approve)

Approve the current stage of an active rolling release.

terminal

```
vercel rolling-release approve --dpl=dpl_abc --currentStageIndex=0
```

Using the `vercel rolling-release approve` command to approve the current stage and advance to the next stage.

### [abort](#abort)

Abort an active rolling release.

terminal

```
vercel rolling-release abort --dpl=dpl_abc
```

Using the `vercel rolling-release abort` command to stop an active rolling release.

### [complete](#complete)

Complete an active rolling release, promoting the deployment to 100% of traffic.

terminal

```
vercel rolling-release complete --dpl=dpl_abc
```

Using the `vercel rolling-release complete` command to finish a rolling release and fully promote the deployment.

### [fetch](#fetch)

Fetch details about a rolling release.

terminal

```
vercel rolling-release fetch
```

Using the `vercel rolling-release fetch` command to get information about the current rolling release.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel rolling-release` command.

### [Configuration](#configuration)

The `--cfg` option is used to configure rolling release settings. It accepts a JSON string or the value `'disable'` to turn off rolling releases.

terminal

```
vercel rolling-release configure --cfg='{"enabled":true, "advancementType":"automatic", "stages":[{"targetPercentage":10,"duration":5},{"targetPercentage":100}]}'
```

Using the `vercel rolling-release configure` command with automatic advancement.

### [Deployment](#deployment)

The `--dpl` option specifies the deployment ID or URL for rolling release operations.

terminal

```
vercel rolling-release start --dpl=https://example.vercel.app
```

Using the `vercel rolling-release start` command with a deployment URL.

### [Current Stage Index](#current-stage-index)

The `--currentStageIndex` option specifies the current stage index when approving a rolling release stage.

terminal

```
vercel rolling-release approve --currentStageIndex=0 --dpl=dpl_123
```

Using the `vercel rolling-release approve` command with a specific stage index.

## [Examples](#examples)

### [Configure a rolling release with automatic advancement](#configure-a-rolling-release-with-automatic-advancement)

terminal

```
vercel rolling-release configure --cfg='{"enabled":true, "advancementType":"automatic", "stages":[{"targetPercentage":10,"duration":5},{"targetPercentage":100}]}'
```

This configures a rolling release that starts at 10% traffic, automatically advances after 5 minutes, and then goes to 100%.

### [Configure a rolling release with manual approval](#configure-a-rolling-release-with-manual-approval)

terminal

```
vercel rolling-release configure --cfg='{"enabled":true, "advancementType":"manual-approval","stages":[{"targetPercentage":10},{"targetPercentage":100}]}'
```

This configures a rolling release that starts at 10% traffic and requires manual approval to advance to 100%.

### [Configure a multi-stage rolling release](#configure-a-multi-stage-rolling-release)

terminal

```
vercel rolling-release configure --cfg='{"enabled":true, "advancementType":"manual-approval", "stages":[{"targetPercentage":10},{"targetPercentage":50},{"targetPercentage":100}]}'
```

This configures a rolling release with three stages: 10%, 50%, and 100% traffic, each requiring manual approval.

### [Disable rolling releases](#disable-rolling-releases)

terminal

```
vercel rolling-release configure --cfg='disable'
```

This disables rolling releases for the project.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel rolling-release` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel switch"
description: "Learn how to switch between different team scopes using the vercel switch CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/switch"
--------------------------------------------------------------------------------

# vercel switch

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel switch` command is used to switch to a different team scope when logged in with Vercel CLI. You can choose to select a team from a list of all those you are part of or specify a team when entering the command.

## [Usage](#usage)

terminal

```
vercel switch
```

Using the `vercel switch` command to change team scope with Vercel CLI.

## [Extended Usage](#extended-usage)

terminal

```
vercel switch [team-name]
```

Using the `vercel switch` command to change to a specific team scope with Vercel CLI.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel switch` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel teams"
description: "Learn how to list, add, remove, and manage your teams using the vercel teams CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/teams"
--------------------------------------------------------------------------------

# vercel teams

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel teams` command is used to manage [Teams](/docs/accounts/create-a-team), providing functionality to list, add, and invite new [Team Members](/docs/rbac/managing-team-members).

You can manage Teams with further options and greater control from the Vercel Dashboard.

## [Usage](#usage)

terminal

```
vercel teams list
```

Using the `vercel teams` command to list all teams you’re a member of.

## [Extended Usage](#extended-usage)

terminal

```
vercel teams add
```

Using the `vercel teams` command to create a new team.

terminal

```
vercel teams invite [email]
```

Using the `vercel teams` command to invite a new [Team Member](/docs/accounts/team-members-and-roles).

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel teams` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel telemetry"
description: "Learn how to manage telemetry collection."
last_updated: "null"
source: "https://vercel.com/docs/cli/telemetry"
--------------------------------------------------------------------------------

# vercel telemetry

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel telemetry` command allows you to enable or disable telemetry collection.

## [Usage](#usage)

terminal

```
vercel telemetry status
```

Using the `vercel telemetry status` command to show whether telemetry collection is enabled or disabled.

terminal

```
vercel telemetry enable
```

Using the `vercel telemetry enable` command to enable telemetry collection.

terminal

```
vercel telemetry disable
```

Using the `vercel telemetry disable` command to disable telemetry collection.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel telemetry` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel whoami"
description: "Learn how to display the username of the currently logged in user with the vercel whoami CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/whoami"
--------------------------------------------------------------------------------

# vercel whoami

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel whoami` command is used to show the username of the user currently logged into [Vercel CLI](/cli).

## [Usage](#usage)

terminal

```
vercel whoami
```

Using the `vercel whoami` command to view the username of the user currently logged into Vercel CLI.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel whoami` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "Code Owners"
description: "Use Code Owners to define users or teams that are responsible for directories and files in your codebase"
last_updated: "null"
source: "https://vercel.com/docs/code-owners"
--------------------------------------------------------------------------------

# Code Owners

Copy page

Ask AI about this page

Last updated March 19, 2025

Code Owners are available on [Enterprise plans](/docs/plans/enterprise)

As a company grows, it can become difficult for any one person to be familiar with the entire codebase. As growing teams start to specialize, it's hard to track which team and members are responsible for any given piece of code. Code Owners works with GitHub to let you automatically assign the right developer for the job by implementing features like:

*   Colocated owners files: Owners files live right next to the code, making it straightforward to find who owns a piece of code right from the context
*   Mirrored organization dynamics: Code Owners mirrors the structure of your organization. Code owners who are higher up in the directory tree act as broader stewards over the codebase and are the fallback if owners files go out of date, such as when developers switch teams
*   Customizable code review algorithms: Modifiers allow organizations to tailor their code review process to their needs. For example, you can assign reviews in a round-robin style, based on who's on call, or to the whole team

## [Get Started](#get-started)

Code Owners is only available for use with GitHub.

To get started with Code Owners, follow the instructions on the [Getting Started](/docs/code-owners/getting-started) page.

## [Code Approvers](#code-approvers)

Code Approvers are a list of [GitHub usernames or teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams) that can review and accept pull request changes to a directory or file.

You can enable Code Approvers by adding a `.vercel.approvers` file to a directory in your codebase. To learn more about how the code approvers file works and the properties it takes, see the [Code Approvers](/docs/code-owners/code-approvers) reference.

--------------------------------------------------------------------------------
title: "Code Owners changelog"
description: "Find out what's new in each release of Code Owners."
last_updated: "null"
source: "https://vercel.com/docs/code-owners/changelog"
--------------------------------------------------------------------------------

# Code Owners changelog

Copy page

Ask AI about this page

Last updated March 4, 2025

Code Owners is available on [Enterprise plans](/docs/plans/enterprise)

## [Upgrade instructions](#upgrade-instructions)

pnpmyarnnpmbun

```
pnpm update --latest --recursive @vercel-private/code-owners
```

## [Releases](#releases)

### [`1.0.7`](#1.0.7)

This patch adds support for underscores in usernames and team slugs to match Github.

### [`1.0.6`](#1.0.6)

This patch updates the minimum length of Github username to match Github's validation.

### [`1.0.5`](#1.0.5)

This patch updates some dependencies for performance and security.

### [`1.0.4`](#1.0.4)

This patch updates some dependencies for performance and security.

### [`1.0.3`](#1.0.3)

This patch updates some dependencies for performance and security, and fixes an issue where CLI output was colorless in GitHub Actions.

### [`1.0.2`](#1.0.2)

This patch updates some dependencies for performance and security.

### [`1.0.1`](#1.0.1)

This patch delivers improvements to our telemetry. While these improvements are not directly user-facing, they enhance our ability to monitor and optimize performance.

### [`1.0.0`](#1.0.0)

Initial release of Code Owners.

--------------------------------------------------------------------------------
title: "vercel-code-owners"
description: "Learn how to use Code Owners with the CLI."
last_updated: "null"
source: "https://vercel.com/docs/code-owners/cli"
--------------------------------------------------------------------------------

# vercel-code-owners

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `vercel-code-owners` command provides functionality to initialize and validate Code Owners in your repository.

## [Using the CLI](#using-the-cli)

The Code Owners CLI is separate to the [Vercel CLI](/docs/cli). However you must ensure that the Vercel CLI is [installed](/docs/cli#installing-vercel-cli) and that you are [logged in](/docs/cli/login) to use the Code Owners CLI.

## [Sub-commands](#sub-commands)

The following sub-commands are available for this CLI.

### [`init`](#init)

The `init` command sets up code owners files in the repository. See [Getting Started](/docs/code-owners/getting-started#initalizing-code-owners) for more information on using this command.

### [`validate`](#validate)

The `validate` command checks the syntax for all Code Owners files in the repository for errors.

pnpmyarnnpmbun

```
pnpm vercel-code-owners validate
```

--------------------------------------------------------------------------------
title: "Code Approvers"
description: "Use Code Owners to define users or teams that are responsible for directories and files in your codebase"
last_updated: "null"
source: "https://vercel.com/docs/code-owners/code-approvers"
--------------------------------------------------------------------------------

# Code Approvers

Copy page

Ask AI about this page

Last updated September 24, 2025

Code Owners are available on [Enterprise plans](/docs/plans/enterprise)

Code Approvers are a list of [GitHub usernames or teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams) that can review and accept pull request changes to a directory or file.

You can enable Code Approvers for a directory by adding a `.vercel.approvers` file to that directory in your codebase. For example, this `.vercel.approvers` file defines the GitHub team `vercel/ui-team` as an approver for the `packages/design` directory:

packages/design/.vercel.approvers

```
@vercel/ui-team
```

When a team is declared as an approver, all members of that team will be able to approve changes to the directory or file and at least one member of the team must approve the changes.

## [Enforcing Code Approvals](#enforcing-code-approvals)

Code Approvals by the correct owners are enforced through the `Vercel – Code Owners` GitHub check added by the Vercel GitHub App.

When a pull request is opened, the GitHub App will check if the pull request contains changes to a directory or file that has Code Approvers defined.

If no Code Approvers are defined for the changes then the check will pass. Otherwise, the check will fail until the correct Code Approvers have approved the changes.

To make Code Owners required, follow the [GitHub required status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/troubleshooting-required-status-checks) documentation to add `Vercel – Code Owners` as a required check to your repository.

## [Inheritance](#inheritance)

Code Approvers are inherited from parent directories. If a directory does not have a `.vercel.approvers` file, then the approvers from the parent directory will be used. Furthermore, even if a directory does have a `.vercel.approvers` file, then the approvers from a parent directory with a `.vercel.approvers` file can also approve the changed files. This structure allows the most specific approver to review most of the code, but allows other approvers who have broader context and approval power to still review and approve the code when appropriate.

To illustrate the inheritance, the following example has two `.vercel.approvers` files.

The first file defines owners for the `packages/design` directory. The `@vercel/ui-team` can approve any change to a file under `packages/design/...`:

packages/design/.vercel.approvers

```
@vercel/ui-team
```

A second `.vercel.approvers` file is declared at the root of the codebase and allows users `elmo` and `oscar` to approve changes to any part of the repository, including the `packages/design` directory.

.vercel.approvers

```
@elmo
@oscar
```

The hierarchical nature of Code Owners enables many configurations in larger codebases, such as allowing individuals to approve cross-cutting changes or creating an escalation path when an approver is unavailable.

## [Reviewer Selection](#reviewer-selection)

When a pull request is opened, the Vercel GitHub App will select the approvers for the changed files. `.vercel.approvers` files allow extensive definitions of file mappings to possible approvers. In many cases, there will be multiple approvers for the same changed file. The Vercel GitHub app selects the best reviewers for the pull request based on affinity of `.vercel.approvers` definitions and overall coverage of the changed files.

### [Bypassing Reviewer Selection](#bypassing-reviewer-selection)

You can skip automatic assignment of reviewers by adding `vercel:skip:owners` to your pull request description.

To request specific reviewers, you can override the automatic selection by including special text in your pull request description:

```
[vercel:approver:@owner1]
[vercel:approver:@owner2]
```

Code Owners will still ensure that the appropriate code owners have approved the pull request before it can pass. Therefore, make sure to select reviewers who provide sufficient coverage for all files in the pull request.

## [Modifiers](#modifiers)

Modifiers enhance the behavior of Code Owners by giving more control over the behavior of approvals and reviewer selection. The available modifiers are:

*   [silent](#silent)
*   [notify](#notify)
*   [optional](#optional)
*   [team](#team)
*   [members](#members-default)
    *   [not](#excluding-team-members-from-review)
*   [required](#required)

Modifiers are appended to the end of a line to modify the behavior of the owner listed for that line:

.vercel.approvers

```
# Approver with no modifier
@owner1
# Approver with optional modifier
@owner2:optional
```

### [`silent`](#silent)

The user or team is an owner for the provided code but is never requested for review. If the user is a non-silent approver in another `.vercel.approvers` file that is closer to the changed files in the directory structure, then they will still be requested for review. The `:silent` modifier can be useful when there's an individual that should be able to approve code, but does not want to receive requests, such as a manager or an old team member.

.vercel.approvers

```
# This person will never be requested to review code but can still approve for owners coverage.
@owner:silent
```

### [`notify`](#notify)

The user or team is always notified through a comment on the pull request. These owners may still be requested for review as part of [reviewer selection](#reviewer-selection), but will still be notified even if not requested. This can be useful for teams that want to be notified on every pull request that affects their code.

.vercel.approvers

```
# my-team is always notified even if leerob is selected as the reviewer.
@vercel/my-team:notify
@leerob
```

### [`optional`](#optional)

The user or team is never requested for review, and they are ignored as owners when computing review requirements. The owner can still approve files they have coverage over, including those that have other owners.

This can be useful while in the process of adding code owners to an existing repository or when you want to designate an owner for a directory but not block pull request reviewers on this person or team.

.vercel.approvers

```
@owner:optional
```

### [`members` (default)](#members-default)

The `:members` modifier can be used with GitHub teams to select an individual member of the team for reviewer rather than assigning it to the entire team. This can be useful when teams want to distribute the code review load across everyone on the team. This is the default behavior for team owners if the [`:team`](#team) modifier is not specified.

.vercel.approvers

```
# An individual from the @acme/eng-team will be requested as a reviewer.
@acme/eng-team:members
```

#### [Excluding team members from review](#excluding-team-members-from-review)

The `:not` modifier can be used with `:members` to exclude certain individuals on the team from review. This can be useful when there is someone on the team who shouldn't be selected for reviews, such as a person who is out of office or someone who doesn't review code every day.

.vercel.approvers

```
# An individual from the @acme/eng-team, except for leerob will be requested as a reviewer.
@acme/eng-team:members:not(leerob)
# Both leerob and mknichel will not be requested for review.
@acme/eng-team:members:not(leerob):not(mknichel)
```

### [`team`](#team)

The `:team` modifier can be used with GitHub teams to request the entire team for review instead of individual members from the team. This modifier must be used with team owners and can not be used with the [`:members`](#members-default) modifier.

.vercel.approvers

```
# The @acme/eng-team will be requested as a reviewer.
@acme/eng-team:team
```

### [`required`](#required)

This user or team is always notified (through a comment) and is a required approver on the pull request regardless of the approvals coverage of other owners. Since the owner specified with `:required` is always required regardless of the owners hierarchy, this should be rarely used because it can make some changes such as global refactorings challenging. `:required` should be usually reserved for highly sensitive changes, such as security, privacy, billing, or critical systems.

Most of the time you don't need to specify required approvers. Non-modified approvers are usually enough so that correct reviews are enforced.

.vercel.approvers

```
# Always notifed and are required reviewers.
# The check won't pass until both `owner1` and `owner2` approve.
@owner1:required
@owner2:required
```

When you specify a team as a required reviewer only one member of that team is required to approve.

.vercel.approvers

```
# The team is notifed and are required reviewers.
# The check won't pass until one member of the team approves.
@vercel/my-team:required
```

## [Patterns](#patterns)

The `.vercel.approvers` file supports specifying files with a limited set of glob patterns:

*   [Directory](#directory-default)
*   [Current Directory](#current-directory-pattern)
*   [Globstar](#globstar-pattern)
*   [Specifying multiple owners](#specifying-multiple-owners-for-the-same-pattern)

The patterns are case-insensitive.

### [Directory (default)](#directory-default)

The default empty pattern represents ownership of the current directory and all subdirectories.

.vercel.approvers

```
# Matches all files in the current directory and all subdirectories.
@owner
```

### [Current Directory Pattern](#current-directory-pattern)

A pattern that matches a file or set of files in the current directory.

.vercel.approvers

```
# Matches the single `package.json` file in the current directory only.
package.json @package-owner
 
# Matches all javascript files in the current directory only.
*.js @js-owner
```

### [Globstar Pattern](#globstar-pattern)

The globstar pattern begins with `**/`. And represents ownership of files matching the glob in the current directory and its subdirectories.

.vercel.approvers

```
# Matches all `package.json` files in the current directory and its subdirectories.
**/package.json @package-owner
 
# Matches all javascript files in the current directory and its subdirectories.
**/*.js @js-owner
```

Code Owners files are meant to encourage distributed ownership definitions across a codebase. Thus, the globstar `**/` and `/` can only be used at the start of a pattern. They cannot be used in the middle of a pattern to enumerate subdirectories.

For example, the following patterns are not allowed:

.vercel.approvers

```
# Instead add a `.vercel.approvers` file in the `src` directory.
src/**/*.js @js-owner
 
# Instead add a `.vercel.approvers` file in the `src/pages` directory.
src/pages/index.js @js-owner
```

### [Specifying multiple owners for the same pattern](#specifying-multiple-owners-for-the-same-pattern)

Each owner for the same pattern should be specified on separate lines. All owners listed will be able to approve for that pattern.

.vercel.approvers

```
# Both @package-owner and @org/team will be able to approve changes to the
# package.json file.
package.json @package-owner
package.json @org/team
```

## [Wildcard Approvers](#wildcard-approvers)

If you would like to allow a certain directory or file to be approved by anyone, you can use the wildcard owner `*`. This is useful for files that are not owned by a specific team or individual. The wildcard owner cannot be used with [modifiers](#modifiers).

.vercel.approvers

```
# Changes to the `pnpm-lock.yaml` file in the current directory can be approved by anyone.
pnpm-lock.yaml *
 
# Changes to any README in the current directory or its subdirectories can be approved by anyone.
**/readme.md *
```

--------------------------------------------------------------------------------
title: "Getting Started with Code Owners"
description: "Learn how to set up Code Owners for your codebase."
last_updated: "null"
source: "https://vercel.com/docs/code-owners/getting-started"
--------------------------------------------------------------------------------

# Getting Started with Code Owners

Copy page

Ask AI about this page

Last updated October 23, 2025

Code Owners are available on [Enterprise plans](/docs/plans/enterprise)

To [set up Code Owners](#setting-up-code-owners-in-your-repository) in your repository, you'll need to do the following:

*   Set up [Vercel's private npm registry](/docs/private-registry) to install the necessary packages
*   [Install and initialize](#setting-up-code-owners-in-your-repository) Code Owners in your repository
*   [Add your repository](#adding-your-repository-to-the-vercel-dashboard) to your Vercel dashboard

If you've already set up Conformance, you may have already completed some of these steps.

## [Prerequisites](#prerequisites)

### [Get access to Code Owners](#get-access-to-code-owners)

To enable Code Owners for your Enterprise team, you'll need to request access through your Vercel account administrator.

### [Setting up Vercel's private npm registry](#setting-up-vercel's-private-npm-registry)

Vercel distributes packages with the `@vercel-private` scope through our private npm registry, and requires that each user using the package authenticates through a Vercel account.

To use the private npm registry, you'll need to follow the documentation to:

*   [Set up your local environment](/docs/private-registry#setting-up-your-local-environment) – This should be completed by the team owner, but each member of your team will need to log in
*   [Set up Vercel](/docs/private-registry#setting-up-vercel) – This should be completed by the team owner
*   [Set up Code Owners for use with CI](/docs/private-registry#setting-up-your-ci-provider) – This should be completed by the team owner

## [Setting up Code Owners in your repository](#setting-up-code-owners-in-your-repository)

A GitHub App enables Code Owners functionality by adding reviewers and enforcing review checks for merging PRs.

1.  ### [Set up the Vercel CLI](#set-up-the-vercel-cli)
    
    The Code Owners CLI is separate to the [Vercel CLI](/docs/cli), however it uses the Vercel CLI for authentication.
    
    Before continuing, please ensure that the Vercel CLI is [installed](/docs/cli#installing-vercel-cli) and that you are [logged in](/docs/cli/login).
    
2.  ### [Initalizing Code Owners](#initalizing-code-owners)
    
    If you have an existing `CODEOWNERS` file in your repository, you can use the CLI to automatically migrate your repository to use Vercel Code Owners. Otherwise, you can skip this step.
    
    Start by running this command in your repository's root:
    
    pnpmyarnnpmbun
    
    ```
    pnpm --package=@vercel-private/code-owners dlx vercel-code-owners init
    ```
    
    `yarn dlx` only works with Yarn version 2 or newer, for Yarn v1 use the npx command.
    
    After running, check the installation success by executing:
    
    pnpmyarnnpmbun
    
    ```
    pnpm vercel-code-owners
    ```
    
3.  ### [Install the GitHub App into a repository](#install-the-github-app-into-a-repository)
    
    To install, you must be an organization owner or have the GitHub App Manager permissions.
    
    1.  Go to [https://github.com/apps/vercel/installations/new](https://github.com/apps/vercel/installations/new)
    2.  Choose your organization for the app installation.
    3.  Select repositories for the app installation.
    4.  Click `Install` to complete the app installation in the chosen repositories.
4.  ### [Define Code Owners files](#define-code-owners-files)
    
    After installation, define Code Owners files in your repository. Pull requests with changes in specified directories will automatically have reviewers added.
    
    Start by adding a `.vercel.approvers` file in a directory in your repository. List GitHub usernames or team names in the file, each on a new line:
    
    .vercel.approvers
    
    ```
    @username1
    @org/team1
    ```
    
    Then, run the [`validate`](/docs/code-owners/cli#validate) command to check the syntax and merge your changes into your repository:
    
    pnpmyarnnpmbun
    
    ```
    pnpm vercel-code-owners validate
    ```
    
5.  ### [Test Code Owners on a new pull request](#test-code-owners-on-a-new-pull-request)
    
    With the `.vercel.approvers` file merged into the main branch, test the flow by modifying any file within the same or child directory. Create a pull request as usual, and the system will automatically add one of the listed users as a reviewer.
    
6.  ### [Add the Code Owners check as required](#add-the-code-owners-check-as-required)
    
    This step is optional
    
    By default, GitHub checks are optional and won't block merging. To make the Code Owners check mandatory, go to `Settings > Branches > [Edit] > Require status checks to pass before merging` in your repository settings.
    

## [Adding your repository to the Vercel dashboard](#adding-your-repository-to-the-vercel-dashboard)

Adding your repository to your team's Vercel [dashboard](/dashboard), allows you to access the Conformance dashboard and see an overview of your Conformance stats.

1.  ### [Import your repository](#import-your-repository)
    
    1.  Ensure your team is selected in the [scope selector](/docs/dashboard-features#scope-selector).
    2.  From your [dashboard](/dashboard), select the Add New button and from the dropdown select Repository.
    3.  Then, from the Add a new repository screen, find your Git repository that you wish to import and select Connect.
2.  ### [Configure your repository](#configure-your-repository)
    
    Before you can connect a repository, you must ensure that the Vercel GitHub app has been [installed for your team](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party#installing-a-github-app). You should ensure it is installed for either all repositories or for the repository you are trying to connect.
    
    Once installed, you'll be able to connect your repository.
    

## [More resources](#more-resources)

*   [Code Owners CLI](/docs/code-owners/cli)
*   [Conformance](/docs/conformance)

--------------------------------------------------------------------------------
title: "Comments Overview"
description: "Comments allow teams and invited participants to give direct feedback on preview deployments. Learn more about Comments in this overview."
last_updated: "null"
source: "https://vercel.com/docs/comments"
--------------------------------------------------------------------------------

# Comments Overview

Copy page

Ask AI about this page

Last updated September 15, 2025

Comments are available on [all plans](/docs/plans)

Comments allow teams [and invited participants](/docs/comments/how-comments-work#sharing) to give direct feedback on [preview deployments](/docs/deployments/environments#preview-environment-pre-production) or other environments through the Vercel Toolbar. Comments can be added to any part of the UI, opening discussion threads that [can be linked to Slack threads](/docs/comments/integrations#use-the-vercel-slack-app). This feature is enabled by default on _all_ preview deployments, for all account plans, free of charge. The only requirement is that all users must have a Vercel account.

![Comments on a preview deployment of the Vercel Docs homepage.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fcomments%2Fcomment-light.png&w=3840&q=75)![Comments on a preview deployment of the Vercel Docs homepage.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fcomments%2Fcomment-dark.png&w=3840&q=75)

Comments on a preview deployment of the Vercel Docs homepage.

Pull request owners receive emails when a new comment is created. Comment creators and participants in comment threads will receive email notifications alerting them to new activity within those threads. Anyone in your Vercel team can leave comments on your previews by default. On Pro and Enterprise plans, you can [invite external users](/docs/deployments/sharing-deployments#sharing-a-preview-deployment-with-external-collaborators) to view your deployment and leave comments.

When changes are pushed to a PR, and a new preview deployment has been generated, a popup modal in the bottom-right corner of the deployment will prompt you to refresh your view:

![The popup modal that alerts you when you are viewing an outdated deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fcomments%2Fnew-deployment-is-ready-light.png&w=828&q=75)![The popup modal that alerts you when you are viewing an outdated deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fcomments%2Fnew-deployment-is-ready-dark.png&w=828&q=75)

The popup modal that alerts you when you are viewing an outdated deployment.

Comments are a feature of the [Vercel Toolbar](/docs/vercel-toolbar) and the toolbar must be active to see comments left on a page. You can activate the toolbar by clicking on it. For users who intend to use comments frequently, we recommend downloading the [browser extension](/docs/vercel-toolbar/in-production-and-localhost/add-to-production#accessing-the-toolbar-using-the-chrome-extension) and toggling on Always Activate in Preferences from the Toolbar menu. This sets the toolbar to always activate so you will see comments on pages without needing to click to activate it.

To leave a comment:

1.  Open the toolbar menu and select Comment or the comment bubble icon in shortcuts.
2.  Then, click on the page or highlight text to place your comment.

## [More resources](#more-resources)

*   [Enabling or Disabling Comments](/docs/comments/how-comments-work)
*   [Using Comments](/docs/comments/using-comments)
*   [Managing Comments](/docs/comments/managing-comments)
*   [Comments Integrations](/docs/comments/integrations)
*   [Using Comments in production and localhost](/docs/vercel-toolbar/in-production-and-localhost)

--------------------------------------------------------------------------------
title: "Enabling and Disabling Comments"
description: "Learn when and where Comments are available, and how to enable and disable Comments at the account, project, and session or interface levels."
last_updated: "null"
source: "https://vercel.com/docs/comments/how-comments-work"
--------------------------------------------------------------------------------

# Enabling and Disabling Comments

Copy page

Ask AI about this page

Last updated September 24, 2025

Comments are enabled by default for all preview deployments on all new projects. By default, only members of [your Vercel team](/docs/accounts/create-a-team) can contribute comments.

The comments toolbar will only render on sites with HTML set as the `Content-Type`. Additionally, on Next.js sites, the comments toolbar will only render on Next.js pages and not on API routes or static files.

### [At the account level](#at-the-account-level)

You can enable or disable comments at the account level with certain permissions:

1.  Navigate to [your Vercel dashboard](/dashboard) and make sure that you have selected your team from the [scope selector](/docs/dashboard-features#scope-selector).
2.  From your [dashboard](/dashboard), select the Settings tab.
3.  In the General section, find Vercel Toolbar.
4.  Under each environment (Preview and Production), select either On or Off from the dropdown to determine the visibility of the Vercel Toolbar for that environment.
5.  You can optionally choose to allow the setting to be overridden at the project level.

![The dashboard setting to enable or disable the toolbar at the team level.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar at the team level.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fteam-level-toolbar-management-dark.png&w=1920&q=75)

The dashboard setting to enable or disable the toolbar at the team level.

### [At the project level](#at-the-project-level)

1.  From your [dashboard](/dashboard), select the project you want to enable or disable Vercel Toolbar for.
2.  Navigate to Settings tab.
3.  In the General section, find Vercel Toolbar.
4.  Under each environment (Preview and Production), select either an option from the dropdown to determine the visibility of Vercel Toolbar for that environment. The options are:
    *   Default: Respect team-level visibility settings.
    *   On: Enable the toolbar for the environment.
    *   Off: Disable the toolbar for the environment.

![The dashboard setting to enable or disable the toolbar in a project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fproject-level-toolbar-management-light.png&w=1920&q=75)![The dashboard setting to enable or disable the toolbar in a project.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fproject-level-toolbar-management-dark.png&w=1920&q=75)

The dashboard setting to enable or disable the toolbar in a project.

### [At the session or interface level](#at-the-session-or-interface-level)

To disable comments for the current browser session, you must [disable the toolbar](/docs/vercel-toolbar/managing-toolbar#disable-toolbar-for-session).

### [With environment variables](#with-environment-variables)

You can enable or disable comments for specific branches or environments with [preview environment variables](/docs/vercel-toolbar/managing-toolbar#enable-or-disable-the-toolbar-for-a-specific-branch).

See [Managing the toolbar](/docs/vercel-toolbar/managing-toolbar) for more information.

### [In production and localhost](#in-production-and-localhost)

To use comments in a production deployment, or link comments in your local development environment to a preview deployment, see [our docs on using comments in production and localhost](/docs/vercel-toolbar/in-production-and-localhost).

See [Managing the toolbar](/docs/vercel-toolbar/managing-toolbar) for more information.

## [Sharing](#sharing)

To learn how to share deployments with comments enabled, see the [Sharing Deployments](/docs/deployments/sharing-deployments) docs.

--------------------------------------------------------------------------------
title: "Integrations for Comments"
description: "Learn how Comments integrates with Git providers like GitHub, GitLab, and BitBucket, as well as Vercel's Slack app."
last_updated: "null"
source: "https://vercel.com/docs/comments/integrations"
--------------------------------------------------------------------------------

# Integrations for Comments

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Git provider integration](#git-provider-integration)

Comments are available for projects using any Git provider. Github, BitBucket and GitLab [are supported automatically](/docs/git#supported-git-providers) with the same level of integration.

Pull requests (PRs) with deployments enabled receive [generated PR messages from Vercel bot](/docs/git/vercel-for-github). These PR messages contain the deployment URL.

The generated PR message will also display an Add your feedback URL, which lets people visit the deployment and automatically log in. The PR message tracks how many comments have been resolved.

![A message from Vercel bot in a GitHub PR.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fvercel-bot-light.png&w=1920&q=75)![A message from Vercel bot in a GitHub PR.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fvercel-bot-dark.png&w=1920&q=75)

A message from Vercel bot in a GitHub PR.

Vercel will also add a check to PRs with comments enabled. This check reminds the author of any unresolved comments, and is not required by default.

![A failing check for unresolved Comments on a GitHub PR.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Ffailed-check-light.png&w=1200&q=75)![A failing check for unresolved Comments on a GitHub PR.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Ffailed-check-dark.png&w=1200&q=75)

A failing check for unresolved Comments on a GitHub PR.

To make this check required, check the docs for your favorite Git provider. Docs on required checks for the most popular git providers are listed below.

*   [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule#creating-a-branch-protection-rule)
*   [BitBucket](https://support.atlassian.com/bitbucket-cloud/docs/suggest-or-require-checks-before-a-merge/)
*   [GitLab](https://docs.gitlab.com/ee/user/project/merge_requests/status_checks.html#block-merges-of-merge-requests-unless-all-status-checks-have-passed)

### [Vercel CLI deployments](#vercel-cli-deployments)

Commenting is available for deployments made with [the Vercel CLI](/docs/cli). The following git providers are supported for comments with Vercel CLI deployments:

*   GitHub
*   GitLab
*   BitBucket

See [the section on Git provider integration information](#git-provider-integration) to learn more.

Commenting is available in production and localhost when you use [the Vercel Toolbar package](/docs/vercel-toolbar/in-production-and-localhost).

## [Use the Vercel Slack app](#use-the-vercel-slack-app)

The [Vercel Slack app](https://vercel.com/integrations/slack) connects Vercel deployments to Slack channels. Any new activity will create corresponding Slack threads, which are synced between the deployment and Slack so that the entire discussion can be viewed and responded to on either platform.

To get started:

1.  Go to [our Vercel Slack app in the Vercel Integrations Marketplace](https://vercel.com/integrations/slack)
2.  Select the Add Integration button from within the Marketplace, then select which Vercel account and project the integration should be scoped to
3.  Confirm the installation by selecting the Add Integration button
4.  From the pop-up screen, you'll be prompted to provide permission to access your Slack workspace. Select the Allow button
5.  In the new pop-up screen, select the Connect your Vercel account to Slack button. When successful, the button will change to text that says, "Your Vercel account is connected to Slack"

Private Slack channels will not appear in the dropdown list when setting up the Slack integration unless you have already invited the Vercel app to the channel. Do so by sending `/invite @Vercel` as a message to the channel.

### [Linking Vercel and Slack users](#linking-vercel-and-slack-users)

1.  In any channel on your Team's Slack instance enter `/vercel login`
2.  Select Continue with Vercel to open a new browser window
3.  From the new browser window, select Authorize Vercel to Slack
4.  Once the connection is successful, you'll receive a "Successfully authenticated" message in the Slack channel.
5.  You can use `/vercel whoami` at any time to check that you're successfully linked

Linking Slack and Vercel does the following:

*   Allows Vercel to translate `@` mentions across messages/platforms
*   Allows you to take extra actions
*   Allows user replies to be correctly attributed to their Vercel user instead of a `slack-{slackusername}` user when replying in a thread

### [Updating your Slack integration](#updating-your-slack-integration)

If you configured the Slack app before October 4th, 2023, the updated app requires new permissions. You must reconfigure the app to subscribe to new comment threads and link new channels.

To do so:

1.  Visit your team's dashboard and select the Integrations tab
2.  Select Manage next to Slack in your list of integrations. On the next page, select Configure
3.  Configure your Slack app and re-authorize it

Your previous linked channels and subscriptions will continue to work even if you don't reconfigure the app in Slack.

### [Connecting a project to a Slack channel](#connecting-a-project-to-a-slack-channel)

To see a specific project's comments in a Slack channel, send the following command as a message to the channel:

```
/vercel subscribe
```

This will open a modal that allows you to configure the subscription, including:

*   Subscribing to comments for specific branches
*   Subscribing to comments on specific pages

You can specify pages using a glob pattern, and branches with regex, to match multiple options.

You can also configure your subscription with options when using the `/vercel subscribe` command. You can use the `/vercel help` command to see all available options.

### [Commenting in Slack](#commenting-in-slack)

When a new comment is created on a PR, the Vercel Slack app will create a matching thread in each of the subscribed Slack channels. The first post will include:

*   A link to the newly-created comment thread
*   A preview of the text of the first comment in the thread
*   A ✅ Resolve button near the bottom of the Slack post
    *   You may resolve comment threads without viewing them
    *   You may reopen resolved threads at any time

Replies and edits in either Slack or the original comment thread will be reflected on both platforms.

Your custom Slack emojis will also be available on linked deployments. Search for them by typing `:`, then inputting the name of the emoji.

Use the following Slack command to list all available options for your Vercel Slack integration:

```
/vercel help
```

### [Receiving notifications as Slack DMs](#receiving-notifications-as-slack-dms)

To receive comment notifications as DMs from Vercel's Slack app, you must link your Vercel account in Slack by entering the following command in any Slack channel, thread or DM:

```
/vercel login
```

### [Vercel Slack app command reference](#vercel-slack-app-command-reference)

| Command | Function |
| --- | --- |
| `/vercel help` | List all commands and options |
| `/vercel subscribe` | Subscribe using the UI interface |
| `/vercel subscribe team/project` | Subscribe the current Slack channel to a project |
| `/vercel subscribe list` | List all projects the current Slack channel is subscribed to |
| `/vercel unsubscribe team/project` | Unsubscribe the current Slack channel from a project |
| `/vercel whoami` | Check which account you're logged into the Vercel Slack app with |
| `/vercel logout` | Log out of your Vercel account |
| `/vercel login` (or `link` or `signin`) | Log into your Vercel account |

## [Adding Comments to your issue tracker](#adding-comments-to-your-issue-tracker)

Adding Comments to your issue tracker is available on [all plans](/docs/plans)

Any member of your team can covert comments to an issue in Linear, Jira, or GitHub. This is useful for tracking bugs, feature requests, and other issues that arise during development. To get started:

1.  ### [Install the Vercel integration for your issue tracker](#install-the-vercel-integration-for-your-issue-tracker)
    
    The following issue trackers are supported:
    
    *   [Linear](/integrations/linear)
    *   [Jira Cloud](/integrations/jira)
    *   [GitHub](/integrations/github)
    
    Once you open the integration, select the Add Integration button to install it. Select which Vercel team and project(s) the integration should be scoped to and follow the prompts to finish installing the integration.
    
    On Jira, issues will be marked as reported by the user who converted the thread and marked as created by the user who set up the integration. You may want to consider using a dedicated account to connect the integration.
    
2.  ### [Convert a comment to an issue](#convert-a-comment-to-an-issue)
    
    On the top-right hand corner of a comment thread, select the icon for your issue tracker. A Convert to Issue dialog will appear.
    
    If you have more than one issue tracker installed, the most recently used issue tracker will appear on a comment. To select a different one, select the ellipsis icon (⋯) and select the issue tracker you want to use:
    
    ![The context menu showing issue tracker options.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fconvert-to-issue-light.png&w=640&q=75)![The context menu showing issue tracker options.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fconvert-to-issue-dark.png&w=640&q=75)
    
    The context menu showing issue tracker options.
    
3.  ### [Fill out the issue details](#fill-out-the-issue-details)
    
    Fill out the relevant information for the issue. The issue description will be populated with the comment text and any images in the comment thread. You can add additional text to the description if needed.
    
    The fields you will see are dependant on the issue tracker you use and the scope it has. When you are done, select Create Issue.
    
    Linear
    
    Users can set the team, project, and issue title. Only publicly available teams can be selected as Private Linear teams are not supported at this time.
    
    Jira
    
    Users can set the project, issue type, and issue title.
    
    You can't currently convert a comment into a child issue. After converting a comment into an issue, you may assign it a parent issue in Jira.
    
    GitHub
    
    Users can set the repository and issue title. If you installed the integration to a Github Organization, there will be an optional field to select the project to add your issue to.
    
4.  ### [Confirm the issue was created](#confirm-the-issue-was-created)
    
    Vercel will display a confirmation toast at the bottom-right corner of the page. You can click the toast to open the relevant issue in a new browser tab. The converted issue contains all previous discussion and images, and a link back to the comment thread.
    
    When you create an issue from a comment thread, Vercel will resolve the thread. The thread cannot be unresolved so we recommend only converting a thread to an issue once the relevant discussion is done.
    
    Linear
    
    If the email on your Linear account matches the Vercel account and you follow a thread converted to an issue, you will be added as a subscriber on the converted Linear issue.
    
    Jira
    
    On Jira, issues will be marked as _reported_ by the user who converted the thread and marked as _created_ by the user who set up the integration. You may wish to consider using a dedicated account to connect the integration.
    
    GitHub
    
    The issue will be marked as created by the `vercel-toolbar` bot and will have a label generated based on the Vercel project it was converted from. For example `Vercel: acme/website`.
    
    If selected, the converted issue will be added to the project or board you selected when creating the issue.

--------------------------------------------------------------------------------
title: "Managing Comments on Preview Deployments"
description: "Learn how to manage Comments on your Preview Deployments from Team members and invited collaborators."
last_updated: "null"
source: "https://vercel.com/docs/comments/managing-comments"
--------------------------------------------------------------------------------

# Managing Comments on Preview Deployments

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Resolve comments](#resolve-comments)

You can resolve comments by selecting the ☐ Resolve checkbox that appears under each thread or comment. You can access this checkbox by selecting a comment wherever it appears on the page, or by selecting the thread associated with the comment in the Inbox.

Participants in a thread will receive a notification when that thread is resolved.

## [Notifications](#notifications)

By default, the activity within a comment thread triggers a notification for all participants in the thread. PR owners will also receive notifications for all newly-created comment threads.

Activities that trigger a notification include:

*   Someone creating a comment thread
*   Someone replying in a comment thread you have enabled notifications for or participated in
*   Someone resolving a comment thread you're receiving notifications for

Whenever there's new activity within a comment thread, you'll receive a new notification. Notifications can be sent to:

*   [Your Vercel Dashboard](#dashboard-notifications)
*   [Email](#email)
*   [Slack](#slack)

### [Customizing notifications for deployments](#customizing-notifications-for-deployments)

To customize notifications for a deployment:

1.  Visit the deployment
2.  Log into the Vercel toolbar
3.  Select the Menu button (☰)
4.  Select Preferences (⚙)
5.  In the dropdown beside Notifications, select:
    *   Never: To disable notifications
    *   All: To enable notifications
    *   Replies and Mentions: To enable only some notifications

### [Customizing thread notifications](#customizing-thread-notifications)

You can manage notifications for threads in the Inbox:

1.  Select the three dots (ellipses) near the top of the first comment in a thread
2.  Select Unfollow to mute the thread, or Follow to subscribe to the thread

### [Dashboard notifications](#dashboard-notifications)

While logged into Vercel, select the notification bell icon and select the Comments tab to see new Comments notifications. To view specific comments, you can:

*   Filter based on:
    *   Author
    *   Status
    *   Project
    *   Page
    *   Branch
*   Search: Search for comments containing specific text

Comments left on pages with query params in the URL may not appear on the page when you visit the base URL. Filter by page and search with a `*` wildcard to see all pages with similar URLs. For example, you might search for `/docs/conformance/rules/req*`.

You can also resolve comments from your notifications.

To reply to a comment, or view the deployment it was made on, select it and select the link to the deployment.

### [Email](#email)

Email notifications will be sent to the email address associated with your Vercel account. Multiple notifications within a short period will be batched into a single email.

### [Slack](#slack)

When you configure Vercel's Slack integration, comment threads on linked branches will create Slack threads. New activity on Slack or in the comment thread will be reflected on both platforms. See [our Slack integration docs](/docs/comments/integrations#commenting-in-slack) to learn more.

## [Troubleshooting comments](#troubleshooting-comments)

Sometimes, issues appear on a webpage for certain browsers and devices, but not for others. It's also possible for users to leave comments on a preview while viewing an outdated deployment.

To get around this issue, you can select the screen icon beside a commenter's name to copy their session info to your clipboard. Doing so will yield a JSON object similar to the following:

session-data

```
{
  "browserInfo": {
    "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 9_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "browser": {
      "name": "Chrome",
      "version": "106.0.0.0",
      "major": "106"
    },
    "engine": {
      "name": "Blink",
      "version": "106.0.0.0"
    },
    "os": {
      "name": "Mac OS",
      "version": "10.15.7"
    },
    "device": {},
    "cpu": {}
  },
  "screenWidth": 1619,
  "screenHeight": 1284,
  "devicePixelRatio": 1.7999999523162842,
  "deploymentUrl": "vercel-site-7p6d5t8vq.vercel.sh"
}
```

On desktop, you can hover your cursor over a comment's timestamp to view less detailed session information at a glance, including:

*   Browser name and version
*   Window dimensions in pixels
*   Device pixel ratio
*   Which deployment they were viewing

![A comment's browsing session information.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fdebug-info-light.png&w=1920&q=75)![A comment's browsing session information.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fdebug-info-dark.png&w=1920&q=75)

A comment's browsing session information.

--------------------------------------------------------------------------------
title: "Using Comments with Preview Deployments"
description: "This guide will help you get started with using Comments with your Vercel Preview Deployments."
last_updated: "null"
source: "https://vercel.com/docs/comments/using-comments"
--------------------------------------------------------------------------------

# Using Comments with Preview Deployments

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Add comments](#add-comments)

You must be logged in to create a comment. You can press `c` to enable the comment placement cursor.

Alternatively, select the Comment option in the toolbar menu. You can then select a location to place your comment with your cursor.

### [Mention users](#mention-users)

You can use `@` to mention team members and alert them to your comment. For example, you might want to request Jennifer's input by writing "Hey @Jennifer, how do you feel about this?"

![A comment using the @ symbol to mention someone.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fcomment-light.png&w=828&q=75)![A comment using the @ symbol to mention someone.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Fcomment-dark.png&w=828&q=75)

A comment using the @ symbol to mention someone.

### [Add emojis to a comment](#add-emojis-to-a-comment)

You can add emojis by entering `:` (the colon symbol) into your comment input box, then entering the name of the emoji. For example, add a smile by entering `:smile:`. As you enter the name of the emoji you want, suggestions will be offered in a popup modal above the input box. You can select one of the suggestions with your cursor.

![Emoji suggestions appear as you type.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Femojis-light.png&w=640&q=75)![Emoji suggestions appear as you type.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Femojis-dark.png&w=640&q=75)

Emoji suggestions appear as you type.

To add a reaction, select the emoji icon to the right of the name of the commenter whose comment you want to react to. You can then search for the emoji you want to react with.

![A comment with reactions.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Freaction-screenshot-light.png&w=828&q=75)![A comment with reactions.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fcomments%2Freaction-screenshot-dark.png&w=828&q=75)

A comment with reactions.

Custom emoji from your Slack organization are supported when you integrate the [Vercel Slack app](/docs/comments/integrations#use-the-vercel-slack-app).

### [Add screenshots to a comment](#add-screenshots-to-a-comment)

You can add screenshots to a comment in any of the following ways:

*   Click the plus icon that shows when drafting a comment to upload a file.
*   Click the camera icon to take a screenshot of the page you are on.
*   Click and drag while in commenting mode to automatically screenshot a portion of the page and start a comment with it attached.

The latter two options are only available to users with the [browser extension](/docs/vercel-toolbar/in-production-and-localhost/add-to-production#accessing-the-toolbar-using-the-chrome-extension) installed.

### [Use Markdown in a comment](#use-markdown-in-a-comment)

Markdown is a markup language that allows you to format text, and you can use it to make your comments more readable and visually pleasing.

Supported formatting includes:

### [Supported markdown formatting options](#supported-markdown-formatting-options)

| Command | Keyboard Shortcut (Windows) | Keyboard Shortcut (Mac) | Example Input | Example Output |
| --- | --- | --- | --- | --- |
| Bold | `Ctrl+B` | `⌘+B` | `*Bold text*` | Bold text |
| Italic | `Ctrl+I` | `⌘+I` | `_Italic text_` | _Italic text_ |
| Strikethrough | `Ctrl+Shift+X` | `⌘+⇧+X` | `~Strikethrough text~` | ~Strikethrough text~ |
| Code-formatted text | `Ctrl+E` | `⌘+E` | `` `Code-formatted text` `` | `Code-formatted text` |
| Bulleted list | `-` or `*` | `-` or `*` | `- Item 1 - Item 2` | • Item 1 • Item 2 |
| Numbered list | `1.` | `1.` | `1. Item 1 2. Item 2` | 1\. Item 1 2. Item 2 |
| Embedded links | N/A | N/A | `[A link](https://example.com)` | [A link](#supported-markdown-formatting-options) |
| Quotes | `>` | `>` | `> Quote` | │ Quote |

## [Comment threads](#comment-threads)

Every new comment placed on a page begins a thread. The comment author, PR owner, and anyone participating in the conversation will see the thread listed in their Inbox.

The Inbox can be opened by selecting the Inbox option in the toolbar menu. A small badge will indicate if any comments have been added since you last checked. You can navigate between threads using the up and down arrows near the top of the inbox.

You can move the Inbox to the left or right side of the screen by selecting the top of the Inbox modal and dragging it.

### [Thread filtering](#thread-filtering)

You can filter threads by selecting the branch name at the top of the Inbox. A modal will appear, with the following filter options:

*   Filter by page: Show comments across all pages in the inbox, or only those that appear on the page you're currently viewing
*   Filter by status: Show comments in the inbox regardless of status, or either show resolved or unresolved

### [Copy comment links](#copy-comment-links)

You can copy a link to a comment in two ways:

*   Select a comment in the Inbox. When you do, the URL will update with an anchor to the selected comment
*   Select the ellipses (three dots) icon to the right of the commenter's name, then select the Copy Link option in the menu that pops up

--------------------------------------------------------------------------------
title: "Vercel CDN Compression"
description: "Vercel helps reduce data transfer and improve performance by supporting both Gzip and Brotli compression"
last_updated: "null"
source: "https://vercel.com/docs/compression"
--------------------------------------------------------------------------------

# Vercel CDN Compression

Copy page

Ask AI about this page

Last updated September 9, 2025

Vercel helps reduce data transfer and improve performance by supporting both Gzip and Brotli compression. These algorithms are widely used to compress files, such as HTML, CSS, and JavaScript, to reduce their size and improve performance.

## [Compression algorithms](#compression-algorithms)

While `gzip` has been around for quite some time, `brotli` is a newer compression algorithm built by Google that best serves text compression. If your client supports [brotli](https://en.wikipedia.org/wiki/Brotli), it takes precedence over [gzip](https://en.wikipedia.org/wiki/LZ77_and_LZ78#LZ77) because:

*   `brotli` compressed JavaScript files are 14% smaller than `gzip`
*   HTML files are 21% smaller than `gzip`
*   CSS files are 17% smaller than `gzip`

`brotli` has an advantage over `gzip` since it uses a dictionary of common keywords on both the client and server-side, which gives a better compression ratio.

## [Compression negotiation](#compression-negotiation)

Many clients (e.g., browsers like Chrome, Firefox, and Safari) include the `Accept-Encoding` [request header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept-Encoding) by default. This automatically enables compression for Vercel's CDN.

You can verify if a response was compressed by checking the `Content-Encoding` [response header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Encoding) has a value of `gzip` or `brotli`.

### [Clients that don't use `Accept-Encoding`](#clients-that-don't-use-accept-encoding)

The following clients may not include the `Accept-Encoding` header by default:

*   Custom applications, such as Python scripts, Node.js servers, or other software that can send HTTP requests to your deployment
*   HTTP libraries, such as [`http`](https://nodejs.org/api/http.html) in Node.js, and networking tools, like `curl` or `wget`
*   Older browsers. Check [MDN's browser compatibility list](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept-Encoding#browser_compatibility) to see if your client supports `Accept-Encoding` by default
*   Bots and crawlers sometimes do not specify `Accept-Encoding` in their headers by default when visiting your deployment

When writing a client that doesn't run in a browser, for example a CLI, you will need to set the `Accept-Encoding` request header in your client code to opt into compression.

### [Automatically compressed MIME types](#automatically-compressed-mime-types)

When the `Accept-Encoding` request header is present, only the following list of MIME types will be automatically compressed.

#### [Application types](#application-types)

*   `json`
*   `x-web-app-manifest+json`
*   `geo+json`
*   `manifest+json`
*   `ld+json`
*   `atom+xml`
*   `rss+xml`
*   `xhtml+xml`
*   `xml`
*   `rdf+xml`
*   `javascript`
*   `tar`
*   `vnd.ms-fontobject`
*   `wasm`

#### [Font types](#font-types)

*   `otf`
*   `ttf`

#### [Image types](#image-types)

*   `svg+xml`
*   `bmp`
*   `x-icon`

#### [Text types](#text-types)

*   `cache-manifest`
*   `css`
*   `csv`
*   `dns`
*   `javascript`
*   `plain`
*   `markdown`
*   `vcard`
*   `calendar`
*   `vnd.rim.location.xloc`
*   `vtt`
*   `x-component`
*   `x-cross-domain-policy`

### [Why doesn't Vercel compress all MIME types?](#why-doesn't-vercel-compress-all-mime-types)

The compression allowlist above is necessary to avoid accidentally increasing the size of non-compressible files, which can negatively impact performance.

For example, most image formats are already compressed such as JPEG, PNG, WebP, etc. If you want to compress an image even further, consider lowering the quality using [Vercel Image Optimization](/docs/image-optimization).

--------------------------------------------------------------------------------
title: "Introduction to Conformance"
description: "Learn how Conformance improves collaboration, productivity, and software quality at scale."
last_updated: "null"
source: "https://vercel.com/docs/conformance"
--------------------------------------------------------------------------------

# Introduction to Conformance

Copy page

Ask AI about this page

Last updated October 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Conformance provides tools that run automated checks on your code for product critical issues, such as performance, security, and code health. Conformance runs in the development workflow to help you:

*   Prevent issues from being merged into your codebase: Conformance runs locally and on Continuous Integration (CI) to notify developers early and prevent issues from ever reaching production
*   Learn from expert guidance directly in your development workflow: Conformance rules were created based on years of experience in large codebases and frontend applications, and with Vercel's deep knowledge of the framework ecosystem
*   Burn down existing issues over time: Conformance allowlists enable you to identify and allowlist all existing errors, unblocking development and facilitating gradual error fixing over time. Developers can then incrementally improve the codebase when they have the time to work on the issues

## [Getting Started](#getting-started)

To get started with Conformance, follow the instructions on the [Getting Started](/docs/conformance/getting-started) page.

## [Conformance Rules](#conformance-rules)

Conformance comes with a curated suite of rules that look for common issues. These rules were created based on the decades of combined experience that we have building high quality web applications.

You can lean more about the built-in Conformance rules on the [Conformance Rules](/docs/conformance/rules) page.

## [Conformance Allowlists](#conformance-allowlists)

A core feature in Conformance is the ability to provide allowlists. This mechanism allows organizations to have developers review their conformance violations with an expert on the team before deciding whether it should be allowed. Conformance allowlists can also be added to existing issues, helping to make sure that new code follows the best practices.

Learn more about how this mechanism works on the [Allowlists](/docs/conformance/allowlist) page.

## [Customizing Conformance](#customizing-conformance)

Conformance can be customized to meet your repository's needs. See [Customizing Conformance](/docs/conformance/customize) for more information.

## [More resources](#more-resources)

*   [Learn how Vercel helps organizations grow with Conformance and Code owners](https://www.youtube.com/watch?v=IFkZz3_7Poo)

--------------------------------------------------------------------------------
title: "Conformance Allowlists"
description: "Learn how to use allowlists to bypass your Conformance rules to merge changes into your codebase."
last_updated: "null"
source: "https://vercel.com/docs/conformance/allowlist"
--------------------------------------------------------------------------------

# Conformance Allowlists

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Conformance allowlists enable developers to integrate code into the codebase, bypassing specific Conformance rules when necessary. This helps with collaboration, ensures gradual rule implementation, and serves as a systematic checklist for addressing issues.

## [Anatomy of an allowlist entry](#anatomy-of-an-allowlist-entry)

An allowlist entry looks like the following:

my-site/.allowlists

```
{
  "testName": "NEXTJS_MISSING_SECURITY_HEADERS",
  "entries": [
    {
      "testName": "NEXTJS_MISSING_SECURITY_HEADERS",
      "reason": "TODO: This existed before the Conformance test was added but should be fixed.",
      "location": {
        "workspace": "dashboard",
        "filePath": "next.config.js"
      },
      "details": {
        "missingField": "headers"
      }
    }
  ]
}
```

The allowlist entry contains the following fields:

*   `testName`: The name of the triggered test
*   `needsResolution`: Whether the allowlist entry needs to be resolved
*   `reason`: Why this code instance is allowed despite Conformance catching it
*   `location`: The file path containing the error
*   `details` (optionally): Details about the Conformance error

An allowlist entry will match an existing one when the `testName`, `location`, and `details` fields all match. The `reason` is only used for documentation purposes.

## [The `needsResolution` field](#the-needsresolution-field)

This field is used by the CLI and our metrics to assess if an allowlisted issue is something that needs to be resolved. The default value is `true`. When set to `false`, this issue is considered to be "accepted" by the team and will not show up in future metrics.

As this field was added after the release of Conformance, the value of this field is considered `true` when the field is missing from an allowlist entry.

## [Allowlists location](#allowlists-location)

In a monorepo, Conformance allowlists are located in an `.allowlists/` directory in the root directory of each workspace. For repository-wide rules, place allowlist entries in the top-level `.allowlists/` directory.

## [Allowlisting all errors](#allowlisting-all-errors)

The Conformance CLI can add an allowlist entry for all the active errors. This can be useful when adding a new entry to the allowlist for review, or when a new check is being added to the codebase. To add an allowlist entry for all active errors in a package:

From the package directory:

pnpmyarnnpmbun

```
pnpm conformance --allowlist-errors
```

From the root of a monorepo:

pnpmyarnnpmbun

```
pnpm --filter=<package-name> conformance --allowlist-errors
```

## [Configuring Code Owners for Allowlists](#configuring-code-owners-for-allowlists)

You can use [Code Owners](/docs/code-owners) with allowlists for specific team reviews on updates. For instance, have the security team review security-related entries.

To configure Code Owners for all tests at the top level for the entire repository:

.vercel.approvers

```
**/*.allowlist.json @org/team:required
**/NO_CORS_HEADERS.* @org/security-team:required
```

For a specific workspace, add a `.vercel.approvers` file in the `.allowlists` sub-directory:

apps/docs/.allowlists/.vercel.approvers

```
NO_EXTERNAL_CSS_AT_IMPORTS.* @org/performance-team:required
```

The `:required` check ensures any modifications need the specified owners' review.

--------------------------------------------------------------------------------
title: "Conformance changelog"
description: "Find out what's new in each release of Conformance."
last_updated: "null"
source: "https://vercel.com/docs/conformance/changelog"
--------------------------------------------------------------------------------

# Conformance changelog

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

## [Upgrade instructions](#upgrade-instructions)

pnpmyarnnpmbun

```
pnpm update --latest --recursive @vercel-private/conformance
```

## [Releases](#releases)

### [`1.12.3`](#1.12.3)

*   Support for Turborepo v2 configuration

### [`1.12.2`](#1.12.2)

*   Update dependencies listed in `THIRD_PARTY_LICENSES.md` file
*   Update `NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE` rule to not treat `react` as just a client dependency

### [`1.12.1`](#1.12.1)

*   Adds a `THIRD_PARTY_LICENSES.md` file listing third party licenses

### [`1.12.0`](#1.12.0)

*   Update `NO_SERIAL_ASYNC_CALLS` rule to highlight the awaited call expression instead of the entire function

### [`1.11.0`](#1.11.0)

*   Update rule logic for detecting duplicate allowlist entries based on the details field

### [`1.10.3`](#1.10.3)

This patch update has the following changes:

*   Optimize checking allowlists for existing Conformance issues
*   Isolate some work by moving it to a worker thread
*   Fix error when trying to parse empty JavaScript/TypeScript files

### [`1.10.2`](#1.10.2)

This patch update has the following changes:

*   Parse ESLint JSON config with a JSONC parser
*   Fix retrieving latest version of CLI during `init`

### [`1.10.1`](#1.10.1)

This patch update has the following changes:

*   Fix updating allowlist files when entries conflict or already exist

### [`1.10.0`](#1.10.0)

This minor update has the following changes:

*   Replace [`NEXTJS_MISSING_MODULARIZE_IMPORTS`](/docs/conformance/rules/NEXTJS_MISSING_MODULARIZE_IMPORTS) Next.js rule with [`NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS`](/docs/conformance/rules/NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS)
*   Fix showing error messages for rules
*   Update allowlist entry details for [`REQUIRE_CARET_DEPENDENCIES`](/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES)

### [`1.9.0`](#1.9.0)

This minor update has the following changes:

*   Ensure in-memory objects are cleaned up after each run
*   Fix detection of Next.js apps in certain edge cases
*   Bump dependencies for performance and security

### [`1.8.1`](#1.8.1)

This patch update has the following changes:

*   Fix the init command for Yarn classic (v1)
*   Update AST caching to prevent potential out of memory issues
*   Fix requesting git authentication when sending Conformance metrics

### [`1.8.0`](#1.8.0)

This minor update has the following changes:

*   Support non-numeric Node version numbers like `lts` in [`REQUIRE_NODE_VERSION_FILE`](/docs/conformance/rules/REQUIRE_NODE_VERSION_FILE).
*   Add version range support for [`forbidden-packages`](/docs/conformance/custom-rules/forbidden-packages) custom rules.
*   Updates dependencies for performance and security.

New rules:

*   [`REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS`](/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS). Requires that all exported functions have JSDoc comments.

### [`1.7.0`](#1.7.0)

This minor update captures and sends Conformance runs metrics to Vercel. Your team will be able to view those metrics in the Vercel dashboard.

The following rules also include these fixes:

*   [`NEXTJS_REQUIRE_EXPLICIT_DYNAMIC`](/docs/conformance/rules/NEXTJS_REQUIRE_EXPLICIT_DYNAMIC): Improved error messaging.
*   [`NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE`](/docs/conformance/rules/NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE): Improved error messaging.

### [`1.6.0`](#1.6.0)

This minor update introduces multiple new rules, fixes and improvements for existing rules and the CLI, and updates to some dependencies for performance and security.

Notably, this release introduces a new `needsResolution` flag. This is used by the CLI and will be used in future metrics as a mechanism to opt-out of further tracking of this issue.

The following new rules have been added:

*   [`NO_UNNECESSARY_PROP_SPREADING`](/docs/conformance/rules/NO_UNNECESSARY_PROP_SPREADING): Disallows the usage of object spreading in JSX components.

The following rules had fixes and improvements:

*   [`REQUIRE_CARET_DEPENDENCIES`](/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES): Additional cases are now covered by this rule.
*   [`NO_INSTANCEOF_ERROR`](/docs/conformance/rules/NO_INSTANCEOF_ERROR): Multiple issues in the same file are no longer reported as a single issue.
*   [`NO_INLINE_SVG`](/docs/conformance/rules/NO_INLINE_SVG): Multiple issues in the same file are no longer reported as a single issue.
*   [`REQUIRE_ONE_VERSION_POLICY`](/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY): Multiple issues in the same file are now differentiated by the package name and the location of the entry in `package.json`.

### [`1.5.0`](#1.5.0)

This minor update introduces a new rule and improvements to our telemetry.

The following new rules have been added:

*   [`NO_INSTANCEOF_ERROR`](/docs/conformance/rules/NO_INSTANCEOF_ERROR): Disallows using `error instanceof Error` comparisons due to risk of false negatives.

### [`1.4.0`](#1.4.0)

This minor update introduces multiple new rules, fixes and improvements for existing rules and the CLI, and updates to some dependencies for performance and security.

The following new rules have been added:

*   [`NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE`](/docs/conformance/rules/NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE): Requires allowlist entries for any usage of `NEXT_PUBLIC_*` environment variables.
*   [`NO_POSTINSTALL_SCRIPT`](/docs/conformance/rules/NO_POSTINSTALL_SCRIPT): Prevents the use of `"postinstall"` script in package for performance reasons.
*   [`REQUIRE_CARET_DEPENDENCIES`](/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES): Requires that all `dependencies` and `devDependencies` have a `^` prefix.

The following rules had fixes and improvements:

*   [`PACKAGE_MANAGEMENT_REQUIRED_README`](/docs/conformance/rules/PACKAGE_MANAGEMENT_REQUIRED_README): Lowercase `readme.md` files are now considered valid.
*   [`REQUIRE_NODE_VERSION_FILE`](/docs/conformance/rules/REQUIRE_NODE_VERSION_FILE): Resolved an issue preventing this rule from correctly reporting issues.
*   [`NO_INLINE_SVG`](/docs/conformance/rules/NO_INLINE_SVG): Detection logic now handles template strings alongside string literals.
*   The [`forbidden-imports`](/docs/conformance/custom-rules/forbidden-imports) custom rule type now supports `paths` being defined in [rule configuration](/docs/conformance/custom-rules/forbidden-imports#configuring-this-rule-type).

### [`1.3.0`](#1.3.0)

This minor update introduces new rules to improve Next.js app performance, resolves an issue where TypeScript's `baseUrl` wasn't respected when traversing files, and fixes an issue with dependency traversal which caused some rules to return false positives in specific cases.

The following new rules have been added:

*   [`NEXTJS_REQUIRE_EXPLICIT_DYNAMIC`](/docs/conformance/rules/NEXTJS_REQUIRE_EXPLICIT_DYNAMIC): Requires explicitly setting the `dynamic` route segment option for Next.js pages and routes.
*   [`NO_INLINE_SVG`](/docs/conformance/rules/NO_INLINE_SVG): Prevents the use of `svg` tags inline, which can negatively impact the performance of both browser and server rendering.

### [`1.2.1`](#1.2.1)

This patch updates some Conformance dependencies for performance and security, and improves handling of edge case for both [`NEXTJS_NO_ASYNC_LAYOUT`](/docs/conformance/rules/NEXTJS_NO_ASYNC_LAYOUT) and [`NEXTJS_NO_ASYNC_PAGE`](/docs/conformance/rules/NEXTJS_NO_ASYNC_PAGE).

### [`1.2.0`](#1.2.0)

This minor update introduces a new rule, and improvements to both `NEXTJS_NO_ASYNC_LAYOUT` and `NEXTJS_NO_ASYNC_PAGE`.

The following new rules have been added:

*   [`REQUIRE_NODE_VERSION_FILE`](/docs/conformance/rules/REQUIRE_NODE_VERSION_FILE): Requires that workspaces have a valid Node.js version file (`.node-version` or `.nvmrc`) file defined.

### [`1.1.0`](#1.1.0)

This minor update introduces new rules to improve Next.js app performance, enhancements to the CLI output, and improvements to our telemetry. While telemetry improvements are not directly user-facing, they enhance our ability to monitor and optimize performance.

The following new rules have been added:

*   [`NEXTJS_NO_ASYNC_PAGE`](/docs/conformance/rules/NEXTJS_NO_ASYNC_PAGE): Ensures that the exported Next.js page component and its transitive dependencies are not asynchronous, as that blocks the rendering of the page.
*   [`NEXTJS_NO_ASYNC_LAYOUT`](/docs/conformance/rules/NEXTJS_NO_ASYNC_LAYOUT): Ensures that the exported Next.js layout component and its transitive dependencies are not asynchronous, as that can block the rendering of the layout and the rest of the page.
*   [`NEXTJS_USE_NATIVE_FETCH`](/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH): Requires using native `fetch` which Next.js polyfills, removing the need for third-party fetch libraries.
*   [`NEXTJS_USE_NEXT_FONT`](/docs/conformance/rules/NEXTJS_USE_NEXT_FONT): Requires using `next/font` (when possible), which optimizes fonts for improved privacy and performance.
*   [`NEXTJS_USE_NEXT_IMAGE`](/docs/conformance/rules/NEXTJS_USE_NEXT_IMAGE): Requires that `next/image` is used for all images for improved performance.
*   [`NEXTJS_USE_NEXT_SCRIPT`](/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT): Requires that `next/script` is used for all scripts for improved performance.

### [`1.0.0`](#1.0.0)

Initial release of Conformance.

--------------------------------------------------------------------------------
title: "vercel-conformance"
description: "Learn how Conformance improves collaboration, productivity, and software quality at scale."
last_updated: "null"
source: "https://vercel.com/docs/conformance/cli"
--------------------------------------------------------------------------------

# vercel-conformance

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `vercel-conformance` command is used to run [Conformance](/docs/conformance) on your code.

## [Using the CLI](#using-the-cli)

The Conformance CLI is separate to the [Vercel CLI](/docs/cli). However you must ensure that the Vercel CLI is [installed](/docs/cli#installing-vercel-cli) and that you are [logged in](/docs/cli/login) to use the Conformance CLI.

## [Sub-commands](#sub-commands)

The following sub-commands are available for this CLI.

### [`audit`](#audit)

The `audit` command runs Conformance on code without needing to install any NPM dependencies or build any of the code. This is useful for viewing Conformance results on a repository that you don't own and may not have permissions to modify or build.

pnpmyarnnpmbun

```
pnpm --package=@vercel-private/conformance dlx vercel-conformance audit
```

`yarn dlx` only works with Yarn version 2 or newer, for Yarn v1 use the npx command.

If you would like to store the results of the conformance audit in a file, you can redirect `stderr` to a file:

pnpmyarnnpmbun

```
pnpm --package=@vercel-private/conformance dlx vercel-conformance audit
&> /tmp/conformance-results.txt
```

### [`init`](#init)

The `init` command installs Conformance in the repository. See [Getting Started](/docs/conformance/getting-started#initialize-conformance) for more information on using this command.

--------------------------------------------------------------------------------
title: "Conformance Custom Rules"
description: "Learn how Conformance improves collaboration, productivity, and software quality at scale."
last_updated: "null"
source: "https://vercel.com/docs/conformance/custom-rules"
--------------------------------------------------------------------------------

# Conformance Custom Rules

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Vercel's built-in Conformance rules are crafted from extensive experience in developing large-scale codebases and high-quality web applications. Recognizing the unique needs of different companies, teams, and products, Vercel offers configurable, no-code custom rules. These allow for tailored solutions to specific challenges.

Custom rules in Vercel feature unique error names and messages, providing deeper context and actionable resolution guidance. For example, they may include:

*   Links to internal documentation
*   Alternative methods for logging issues
*   Information on who to contact for help

You can use custom rules to proactively prevent future issues, to reactively prevent issues from reoccuring, and/or as a mitigation tool.

## [Available custom rule types](#available-custom-rule-types)

We support the following custom rules types:

| Type | Description |
| --- | --- |
| [`forbidden-code`](/docs/conformance/custom-rules/forbidden-code) | Disallows code and code patterns through string and regular expression matches. |
| [`forbidden-properties`](/docs/conformance/custom-rules/forbidden-properties) | Disallows properties from being read, written, and/or called. |
| [`forbidden-dependencies`](/docs/conformance/custom-rules/forbidden-dependencies) | Disallows one or more files from depending on one or more predefined modules. |
| [`forbidden-imports`](/docs/conformance/custom-rules/forbidden-imports) | Disallows one or more files from importing one or more predefined modules. |
| [`forbidden-packages`](/docs/conformance/custom-rules/forbidden-packages) | Disallows packages from being listed as dependencies in `package.json` files. |

## [Getting started](#getting-started)

The no-code custom rules are defined and [configured](/docs/conformance/customize) in `conformance.config.jsonc`.

In this example, you will set up a custom rule with the [`forbidden-imports`](/docs/conformance/custom-rules/forbidden-imports) type. This rule disallows importing a package called `api-utils`, and suggests to users that they should instead use a newer version of that package.

1.  ### [Create your config file](#create-your-config-file)
    
    At the root of your directory, create a file named `conformance.config.jsonc`. If one already exists, skip to the next step.
    
2.  ### [Define a custom rule](#define-a-custom-rule)
    
    First, define a new custom rule in `conformance.customRules`.
    
    All custom rules require the properties:
    
    *   `ruleType`
    *   `ruleName`
    *   `errorMessage`
    
    Other required and optional configuration depends on the custom rule type. In this example, we're using the `forbidden-imports` type, which requires an `moduleNames` property.
    
    conformance.config.jsonc
    
    ```
    {
      "customRules": [
        {
          "ruleType": "forbidden-imports",
          "ruleName": "NO_API_UTILS",
          "categories": ["code-health"],
          "errorMessage": "The `api-utils` package has been deprecated. Please use 'api-utils-v2' instead, which includes more features.",
          "errorLink": "https://vercel.com/docs",
          "description": "Don't allow importing the deprecated `api-utils` package.",
          "severity": "major",
          "moduleNames": ["my-utils"],
        },
      ],
    }
    ```
    
3.  ### [Enable the custom rule](#enable-the-custom-rule)
    
    As all custom rules are disabled by default, you'll need to [enable rules](/docs/conformance/customize#managing-a-conformance-rule) in `conformance.overrides`. Refer to the documentation for each custom rule type for more information.
    
    Rule names must be prefixed with `"CUSTOM"` when enabled, and any allowlist files and entries will also be prefixed with `"CUSTOM"`. This prefix is added to ensure that the names of custom rules don't conflict with built-in rules.
    
    In the example below, we're enabling the rule for the entire project by providing it with the required configuration (targeting all files in `src`).
    
    conformance.config.jsonc
    
    ```
    {
      "overrides": [
        {
          "rules": {
            "CUSTOM.NO_API_UTILS": {
              "paths": ["src"],
            },
          },
        },
      ],
      "customRules": [
        // ...
      ],
    }
    ```
    
    In this example, we've used the same configuration as above, but have also restricted the rule and configuration to the `api-teams` workspace.
    
    conformance.config.jsonc
    
    ```
    {
      "overrides": [
        {
          "restrictTo": {
            "workspaces": ["api-teams"],
          },
          "rules": {
            "CUSTOM.NO_API_UTILS": {
              "paths": ["src", "!src/**/*.test.ts"],
            },
          },
        },
      ],
      "customRules": [
        // ...
      ],
    }
    ```
    
4.  ### [Restrict the rule to a workspace](#restrict-the-rule-to-a-workspace)
    
    In this example used the same configuration as above, but have also restricted the rule and configuration to the `api-teams` workspace:
    
    conformance.config.jsonc
    
    ```
    {
      "overrides": [
        {
          "restrictTo": {
            "workspaces": ["api-teams"],
          },
          "rules": {
            "CUSTOM.NO_API_UTILS": {
              "paths": ["src", "!src/**/*.test.ts"],
            },
          },
        },
      ],
      "customRules": [
        // ...
      ],
    }
    ```

--------------------------------------------------------------------------------
title: "forbidden-code"
description: "Learn how to set custom rules to disallow code and code patterns through string and regular expression matches."
last_updated: "null"
source: "https://vercel.com/docs/conformance/custom-rules/forbidden-code"
--------------------------------------------------------------------------------

# forbidden-code

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `forbidden-code` rule type enables you to disallow code and code patterns through string and regular expression matches.

## [When to use this rule type](#when-to-use-this-rule-type)

*   Disallowing comments
    *   You want to disallow `// TODO` comments
    *   You want to disallow usage of `@ts-ignore`
*   Disallowing specific strings
    *   You want to enforce a certain casing for one or more strings
    *   You want to disallow specific strings from being used within code

If you want to disallow specific operations on a property, you should instead use the [`forbidden-properties`](/docs/conformance/custom-rules/forbidden-properties) rule type.

## [Configuring this rule type](#configuring-this-rule-type)

To create a custom `forbidden-code` rule, you'll need to configure the below required properties:

| Property | Type | Description |
| --- | --- | --- |
| `ruleType` | `"forbidden-code"` | The custom rule's type. |
| `ruleName` | `string` | The custom rule's name. |
| `categories` | `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`. |
| `errorMessage` | `string` | The error message, which is shown to users when they encounter this rule. |
| `errorLink` | `string` (optional) | An optional link to show alongside the error message. |
| `description` | `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files. |
| `severity` | `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score. |
| `patterns` | `(string | { pattern: string, flags: string })[]` | An array of regular expression patterns to match against. |
| `strings` | `string[]` | An array of exact string to match against (case sensitive). |

Multi-line strings and patterns are currently unsupported by this custom rule type.

### [Example configuration](#example-configuration)

The example below configures a rule named `NO_DISALLOWED_USAGE` that disallows:

*   Any usage of `"and"` at the start of a line (case-sensitive).
*   Any usage of `"but"` in any case.
*   Any usage of `"TODO"` (case-sensitive).

conformance.config.jsonc

```
{
  "customRules": [
    {
      "ruleType": "forbidden-imports",
      "ruleName": "NO_DISALLOWED_USAGE",
      "categories": ["code-health"],
      "errorMessage": "References to \"and\" at the start of a line are not allowed.",
      "description": "Disallows using \"and\" at the start of a line.",
      "severity": "major",
      "patterns": ["^and", { "pattern": "but", "flags": "i" }],
      "strings": ["TODO"],
    },
  ],
}
```

### [Using flags with patterns](#using-flags-with-patterns)

This custom rule type always sets the `"g"` (or global) flag for regular expressions. This ensures that all regular expression matches are reported, opposed to only reporting on the first match.

When providing flags through an object in `patterns`, you can omit the `"g"` as this will automatically be set.

To learn more about regular expression flags, see [the MDN guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions#advanced_searching_with_flags) on advanced searching with flags.

### [Writing patterns](#writing-patterns)

If you're not familiar with regular expressions, you can use tools like [regex101](https://regex101.com/) and/or [RegExr](https://regexr.com/) to help you understand and write regular expressions.

Regular expressions can vary in complexity, depending on what you're trying to achieve. We've added some examples below to help you get started.

| Pattern | Description |
| --- | --- |
| `^and` | Matches `"and"`, but only if it occurs at the start of a line (`^`). |
| `(B|a)ar$` | Matches `"But"` and `"but"`, but only if it occurs at the end of a line (`$`). |
| `regexp?` | Matches `"regexp"` and `"regex"`, with or without the `"p"` (`?`). |
| `(?<!-)so` | Matches `"so"`, but only when not following a hyphen (`(?<!-)`). |

## [Enabling this rule type](#enabling-this-rule-type)

To enable this rule type, you can set the rule to `true`, or provide the following configuration.

| Property | Type | Description |
| --- | --- | --- |
| `paths` | `string[]` (optional) | An optional array of exact paths or glob expressions\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |

The example below enables the `NO_DISALLOWED_USAGE` custom rule for all files in the `src/` directory, excluding files in `src/legacy/`. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_DISALLOWED_USAGE": {
          "paths": ["src", "!src/legacy"],
        },
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

This next example enables the `NO_DISALLOWED_USAGE` custom rule for all files, and without workspace restrictions.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "rules": {
        "CUSTOM.NO_DISALLOWED_USAGE": true,
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

;

--------------------------------------------------------------------------------
title: "forbidden-dependencies"
description: "Learn how to set custom rules to disallow one or more files from depending on one or more predefined module"
last_updated: "null"
source: "https://vercel.com/docs/conformance/custom-rules/forbidden-dependencies"
--------------------------------------------------------------------------------

# forbidden-dependencies

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `forbidden-dependencies` rule type enables you to disallow one or more files from depending on one or more predefined modules.

Unlike [`forbidden-imports`](/docs/conformance/custom-rules/forbidden-imports), this rule type will check for indirect (or transitive) dependencies, where a module may not directly import the disallowed dependency, but the disallowed dependency is present in the dependency chain. This makes it slower, but more powerful than the `forbidden-imports` rule type.

For example, below we have a `logger` utility that imports a package that may cause security keys to be exposed.

src/utils/logger.ts

```
import { SECURITY_KEY } from 'secret-package';
```

We can use this rule type to create a custom rule that prevents any module in `src/app` from importing any file that depends on our potentially dangerous `secret-package`.

src/app/page.ts

```
import { log } from '../utils/logger';
// Would result in an error
```

## [When to use this rule type](#when-to-use-this-rule-type)

*   Performance
    *   You want to prevent importing packages that are known to increase the size of your client side code
    *   You want to prevent using a package that is known to perform poorly in specific environments
*   Security
    *   You want to disallow client-side code from depending on a file that exposes secrets
*   Error prevention
    *   You want to prevent errors by disallowing server-side code from importing a module where some methods require browser APIs

## [Configuring this rule type](#configuring-this-rule-type)

To create a custom `forbidden-dependencies` rule, you'll need to configure the required properties below:

| Property | Type | Description |
| --- | --- | --- |
| `ruleType` | `"forbidden-dependencies"` | The custom rule's type. |
| `ruleName` | `string` | The custom rule's name. |
| `categories` | `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`. |
| `errorMessage` | `string` | The error message, which is shown to users when they encounter this rule. |
| `errorLink` | `string` (optional) | An optional link to show alongside the error message. |
| `description` | `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files. |
| `severity` | `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score. |
| `moduleNames` | `string[]` | An array of exact module names or glob expressions\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |
| `paths` | `string[]` (optional) | An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to. This acts as the overridable default value for `paths`\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |
| `traverseNodeModules` | `boolean` (optional) | When `true`, this rule will also traverse `node_modules` for transient dependencies. |

When using `traverseNodeModules`, module names currently need to be prefixed with `node_modules` (i.e., `["disallowed", "node_modules/disallowed"]`). We're working to improve this.

### [Example configuration](#example-configuration)

The example below configures a rule named `NO_SUPER_SECRET_IN_CLIENT` that disallows depending on any package from the `super-secret` workspace except for `@super-secret/safe-exports`.

conformance.config.jsonc

```
{
  "customRules": [
    {
      "ruleType": "forbidden-dependencies",
      "ruleName": "NO_SUPER_SECRET_IN_CLIENT",
      "categories": ["code-health"],
      "errorMessage": "Depending on packages from the 'super-secret' workspace may result in secrets being exposed in client-side code. Please use '@super-secret/safe-exports' instead.",
      "description": "Prevents depending on packages from the 'super-secret' workspace.",
      "severity": "major",
      "moduleNames": ["@super-secret/*", "!@super-secret/safe-exports"],
    },
  ],
}
```

## [Enabling this rule type](#enabling-this-rule-type)

To enable this rule type, you can set the rule to `true`, or provide the following configuration.

| Property | Type | Description |
| --- | --- | --- |
| `paths` | `string[]` (optional) | An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |

The example below enables the `NO_SUPER_SECRET_IN_CLIENT` custom rule for all files in the `src/` directory, excluding test files. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_SUPER_SECRET_IN_CLIENT": {
          "paths": ["src", "!src/**/*.test.ts"],
        },
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

This next example enables the `NO_SUPER_SECRET_IN_CLIENT` custom rule for all files, and without workspace restrictions.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "rules": {
        "CUSTOM.NO_SUPER_SECRET_IN_CLIENT": true,
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

--------------------------------------------------------------------------------
title: "forbidden-imports"
description: "Learn how to set custom rules to disallow one or more files from importing one or more predefined modules"
last_updated: "null"
source: "https://vercel.com/docs/conformance/custom-rules/forbidden-imports"
--------------------------------------------------------------------------------

# forbidden-imports

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `forbidden-imports` rule type enables you to disallow one or more files from importing one or more predefined modules.

Unlike [`forbidden-dependencies`](/docs/conformance/custom-rules/forbidden-dependencies), this rule type won't check for indirect (transitive) dependencies. This makes this rule faster, but limits its effectiveness.

## [When to use this rule type](#when-to-use-this-rule-type)

*   Deprecating packages or versions
    *   You want to disallow importing a deprecated package, and to recommend a different approach
*   Recommending an alternative package
    *   You want to require that users import custom/wrapped methods from `test-utils` instead of directly from a testing library

If you want to prevent depending on a module for performance or security reasons, you should instead use the [`forbidden-dependencies`](/docs/conformance/custom-rules/forbidden-dependencies) rule type.

## [Configuring this rule type](#configuring-this-rule-type)

To create a custom `forbidden-imports` rule, you'll need to configure the below required properties:

| Property | Type | Description |
| --- | --- | --- |
| `ruleType` | `"forbidden-imports"` | The custom rule's type. |
| `ruleName` | `string` | The custom rule's name. |
| `categories` | `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`. |
| `errorMessage` | `string` | The error message, which is shown to users when they encounter this rule. |
| `errorLink` | `string` (optional) | An optional link to show alongside the error message. |
| `description` | `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files. |
| `severity` | `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score. |
| `moduleNames` | `string[]` | An array of exact module names or glob expressions\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |
| `importNames` | `string[]` (optional) | An array of exact module names of import names. |
| `paths` | `string[]` (optional) | Added in Conformance `1.4.0`. An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to. This acts as the overridable default value for `paths`\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |
| `disallowDefaultImports` | `boolean` (optional) | Flags default imports (i.e. `import foo from 'foo';`) as errors. |
| `disallowNamespaceImports` | `boolean` (optional) | Flags namespace imports (i.e. `import * as foo from 'foo';`) as errors. |

Note that when using `moduleNames` alone, imports are not allowed at all from that module. When used with conditions like `importNames`, the custom rule will only report an error when those conditions are also met.

### [Example configuration](#example-configuration)

The example below configures a rule named `NO_TEAM_IMPORTS` that disallows importing any package from the `team` workspace except for `@team/utils`. It also configures a rule that disallows importing `oldMethod` from `@team/utils`, but restricts that rule to the `src/new/` directory.

conformance.config.jsonc

```
{
  "customRules": [
    {
      "ruleType": "forbidden-imports",
      "ruleName": "NO_TEAM_IMPORTS",
      "categories": ["security"],
      "errorMessage": "Packages from the team workspace have been deprecated in favour of '@team/utils'.",
      "description": "Disallows importing packages from the team workspace.",
      "severity": "major",
      "moduleNames": ["@team/*", "!@team/utils"],
    },
    {
      "ruleType": "forbidden-imports",
      "ruleName": "NO_TEAM_OLD_METHOD_IMPORTS",
      "categories": ["performance"],
      "errorMessage": "'oldMethod' has been deprecated in favour of 'newMethod'.",
      "description": "Disallows using the deprecated method 'oldMethod' from '@team/utils'.",
      "severity": "minor",
      "moduleNames": ["@team/utils"],
      "importNames": ["oldMethod"],
      "paths": ["src/new/**"],
    },
  ],
}
```

## [Enabling this rule type](#enabling-this-rule-type)

To enable this rule type, you can set the rule to `true`, or provide the following configuration.

| Property | Type | Description |
| --- | --- | --- |
| `paths` | `string[]` (optional) | An optional array of exact paths or glob expressions, which restricts the paths that this custom rule applies to\*.  
  
_\*Note that paths containing square brackets need to be escaped, i.e. `[folder-name]\page.tsx` would become `\[folder-name\]\page.tsx`._ |

The example below enables the `NO_TEAM_IMPORTS` custom rule for all files in the `src/` directory, excluding files in `src/legacy/`. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_TEAM_IMPORTS": {
          "paths": ["src", "!src/legacy"],
        },
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

;

--------------------------------------------------------------------------------
title: "forbidden-packages"
description: "Learn how to set custom rules to disallow packages from being listed as dependencies."
last_updated: "null"
source: "https://vercel.com/docs/conformance/custom-rules/forbidden-packages"
--------------------------------------------------------------------------------

# forbidden-packages

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `forbidden-packages` rule type enables you to disallow packages from being listed as dependencies in `package.json`.

## [When to use this rule type](#when-to-use-this-rule-type)

*   Deprecating packages
    *   You want to disallow importing a deprecated package, and to recommend a different approach
*   Standardization
    *   You want to ensure that projects depend on the same set of packages when performing similar tasks (i.e. using `jest` or `vitest` consistently across a monorepo)
*   Visibility and approval
    *   You want to enable a workflow where team-owned packages can't be depended upon without acknowledgement or approval from that team. This helps owning teams to better plan and understand the impacts of their work

## [Configuring this rule type](#configuring-this-rule-type)

To create a custom `forbidden-packages` rule, you'll need to configure the below required properties:

| Property | Type | Description |
| --- | --- | --- |
| `ruleType` | `"forbidden-packages"` | The custom rule's type. |
| `ruleName` | `string` | The custom rule's name. |
| `categories` | `("nextjs" | "performance" | "security" | "code-health")[]` (optional) | The custom rule's categories. Default is `["code-health"]`. |
| `errorMessage` | `string` | The error message, which is shown to users when they encounter this rule. |
| `errorLink` | `string` (optional) | An optional link to show alongside the error message. |
| `description` | `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files. |
| `severity` | `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score. |
| `packageNames` | `string[]` | An array of exact package names or glob expressions. |
| `packageVersions` | `string[]` (optional) | Added in Conformance `1.8.0`. An optional array of exact package versions or [semver](https://docs.npmjs.com/cli/v6/using-npm/semver) ranges. |

### [Example configuration](#example-configuration)

The example below configures a rule named `NO_TEAM_PACKAGES` that disallows importing any package from the `team` workspace except for `@team/utils`.

conformance.config.jsonc

```
{
  "customRules": [
    {
      "ruleType": "forbidden-packages",
      "ruleName": "NO_TEAM_PACKAGES",
      "errorMessage": "Packages from the team workspace have been deprecated in favour of '@team/utils'.",
      "description": "Disallow importing packages from the team workspace.",
      "severity": "major",
      "packageNames": ["@team/*", "!@team/utils"],
    },
  ],
}
```

The next example restricts the `utils` package, only allowing versions equal to or above `2.0.0`. This option requires Conformance `1.8.0` or later.

conformance.config.jsonc

```
{
  "customRules": [
    {
      "ruleType": "forbidden-packages",
      "ruleName": "NO_OLD_UTIL_PACKAGES",
      "errorMessage": "Versions of `utils` below `2.0.0` are not allowed for security reasons.",
      "description": "Disallow importing `utils` versions below version `2.0.0`.",
      "severity": "major",
      "packageNames": ["utils"],
      "packageVersions: ["<=2.0.0"]
    },
  ],
}
```

## [Enabling this rule type](#enabling-this-rule-type)

The example below enables the `NO_TEAM_PACKAGES` custom rule. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_TEAM_PACKAGES": true,
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

--------------------------------------------------------------------------------
title: "forbidden-properties"
description: "Learn how to set custom rules to disallow reading from,
writing to, and/or calling one or more properties"
last_updated: "null"
source: "https://vercel.com/docs/conformance/custom-rules/forbidden-properties"
--------------------------------------------------------------------------------

# forbidden-properties

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The `forbidden-properties` rule type enables you to disallow reading from, writing to, and/or calling one or more properties.

## [When to use this rule type](#when-to-use-this-rule-type)

*   Disallowing use of global properties
    *   You want to disallow calling `document.write`
    *   You want to disallow using browser-only APIs in a component library that may be server-rendered
    *   You want to disallow calls to usage of `window.location` in favor of another solution.
*   Disallowing use of deprecated features
    *   You want to disallow using `event.keyCode`
    *   You want to disallow specific strings from being used within code

## [Configuring this rule type](#configuring-this-rule-type)

To create a custom `forbidden-properties` rule, you'll need to configure the below required properties:

| Property | Type | Description |
| --- | --- | --- |
| `ruleType` | `"forbidden-properties"` | The custom rule's type. |
| `ruleName` | `string` | The custom rule's name. |
| `errorMessage` | `string` | The error message, which is shown to users when they encounter this rule. |
| `errorLink` | `string` (optional) | An optional link to show alongside the error message. |
| `description` | `string` (optional) | The rule description, which is shown in the Vercel Compass dashboard and included in allowlist files. |
| `severity` | `"major" | "minor"` (optional) | The rule severity added to the allowlists and used to calculate a project's conformance score. |
| `forbiddenProperties` | [`ForbiddenProperty[]`](#forbiddenproperty) | One or more properties and their forbidden operations. |

### [`ForbiddenProperty`](#forbiddenproperty)

| Property | Type | Description |
| --- | --- | --- |
| `property` | `string` | The property to target. |
| `operations` | `{ call?: boolean, read?: boolean, write?: boolean }` | The operation(s) to target. At least one operation is required. |

### [Example configuration](#example-configuration)

The example below configures a rule named `NO_DOCUMENT_WRITE_CALLS` that disallows calling `document.write`.

conformance.config.jsonc

```
{
  "customRules": [
    {
      "ruleType": "forbidden-properties",
      "ruleName": "NO_DOCUMENT_WRITE_CALLS",
      "errorMessage": "Calling 'document.write' is not allowed.",
      "description": "Disallows calls to `document.write`.",
      "severity": "major",
      "forbiddenProperties": [
        {
          "property": "document.write",
          "operations": {
            "call": true,
          },
        },
      ],
    },
  ],
}
```

### [Property assignments](#property-assignments)

Note that a property's assignments are tracked by this custom rule type.

Using our example `NO_DOCUMENT_WRITE_CALLS` rule (above), the following calls will both result in errors.

```
document.write();
 
const writer = document.write;
writer();
```

## [Enabling this rule type](#enabling-this-rule-type)

The example below enables the `NO_DOCUMENT_WRITE_CALLS` custom rule. In this example, the custom rule is also restricted to the `dashboard` and `marketing-site` workspaces, which is optional.

conformance.config.jsonc

```
{
  "overrides": [
    {
      "restrictTo": {
        "workspaces": ["dashboard", "marketing-site"],
      },
      "rules": {
        "CUSTOM.NO_DOCUMENT_WRITE_CALLS": true,
      },
    },
  ],
  "customRules": [
    // ...
  ],
}
```

;

--------------------------------------------------------------------------------
title: "Customizing Conformance"
description: "Learn how to manage and configure your Conformance rules."
last_updated: "null"
source: "https://vercel.com/docs/conformance/customize"
--------------------------------------------------------------------------------

# Customizing Conformance

Copy page

Ask AI about this page

Last updated October 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The Conformance framework may be customized so that you can manage rules for different workspaces in your repository or to pass configuration to the rules.

To customize Conformance, first define a `conformance.config.jsonc` file in the root of your directory.

Both `conformance.config.jsonc` and `conformance.config.json` are supported, and both support JSONC (JSON with JavaScript-style comments). We recommend using the `.jsonc` extension as it helps other tools (for example, VS Code) to provide syntax highlighting and validation.

## [Enabling all rules By default](#enabling-all-rules-by-default)

To enable all Conformance rules by default, add the `defaultRules` field to the top level `configuration` section of the config file:

conformance.config.jsonc

```
{
  "configuration": {
    "defaultRules": "all",
  },
}
```

## [Ignoring files](#ignoring-files)

To exclude one or more files from Conformance, use the `ignorePatterns` field in the top level of the config file:

conformance.config.jsonc

```
{
  "ignorePatterns": ["generated/**/*.js"],
}
```

This field accepts an array of glob patterns as strings.

## [Configuring specific workspaces](#configuring-specific-workspaces)

Each Conformance override accepts a `restrictTo` parameter which controls what workspaces the configuration will apply to. If no `restrictTo` is specified, then the configuration will apply globally to every workspace.

conformance.config.jsonc

```
{
  "overrides": [
    {
      // NOTE: No `restrictTo` is specified here so this applies globally.
      "rules": {},
    },
  ],
}
```

Conformance configuration can be applied to specific workspaces using either the name of the workspace or the directory of the workspace on the `restrictTo` field:

*   Use the `workspaces` field, which accepts a list of workspace names:
    
    conformance.config.jsonc
    
    ```
    {
      "overrides": [
        {
          "restrictTo": {
            "workspaces": ["eslint-config-custom"],
          },
          "rules": {},
        },
      ],
    }
    ```
    
*   Use the `directories` field to specify a directory. All workspaces that live under that directory will be matched:
    
    conformance.config.json
    
    ```
    {
      "overrides": [
        {
          "restrictTo": {
            "directories": ["configs/"],
          },
          "rules": {},
        },
      ],
    }
    ```
    
    This will match `configs/tsconfig` and `configs/eslint-config-custom`.
*   Set the `root` field to true to match the root of the repository:
    
    conformance.config.jsonc
    
    ```
    {
      "overrides": [
        {
          "restrictTo": {
            "root": true,
          },
          "rules": {},
        },
      ],
    }
    ```
    

### [Configuration cascade](#configuration-cascade)

If multiple overrides are specified that affect the same workspace, the configurations will be unioned together. If there are conflicts between the overrides, the last specified value will be used.

## [Managing a Conformance rule](#managing-a-conformance-rule)

To enable or disable a Conformance rule, use the `rules` field. This field is an object literal where the keys are the name of the [rule](/docs/conformance/rules) and the values are booleans or another object literal containing a [rule-specific configuration](#configuring-a-conformance-rule).

For example, this configuration will disable the `TYPESCRIPT_CONFIGURATION` rule:

conformance.config.jsonc

```
{
  "overrides": [
    {
      "rules": {
        "TYPESCRIPT_CONFIGURATION": false,
      },
    },
  ],
}
```

All rules are enabled by default unless explicitly disabled in the config.

## [Configuring a Conformance rule](#configuring-a-conformance-rule)

Some Conformance rules can be configured to alter behavior based on the project settings. Instead of a `boolean` being provided in the `rules` configuration, an object literal could be passed with the configuration for that rule.

For example, this configuration will require a specific list of ESLint plugins in every workspace:

conformance.config.jsonc

```
{
  "overrides": [
    {
      "rules": {
        "ESLINT_CONFIGURATION": {
          "requiredPlugins": ["@typescript-eslint"],
        },
      },
    },
  ],
}
```

## [Adding custom error messages to Conformance rules](#adding-custom-error-messages-to-conformance-rules)

If you want to specify additional information or link to project-specific documentation, you can add custom error messages to the output of any conformance rule. These messages can be added globally to all rules or on a per-rule basis.

To add an error message to the output of all rules, add `globalErrorMessage` to the `configuration` section of the override:

conformance.config.jsonc

```
{
  "overrides": [
    {
      "configuration": {
        "globalErrorMessage": "See link_to_docs for more information.",
      },
    },
  ],
}
```

To add an error message to the output of one specific rule, add an entry for that test to the `additionalErrorMessages` field:

conformance.config.jsonc

```
{
  "overrides": [
    {
      "configuration": {
        "additionalErrorMessages": {
          "TYPESCRIPT_CONFIGURATION": "Please see project_link_to_typescript_docs for more information.",
        },
      },
    },
  ],
}
```

--------------------------------------------------------------------------------
title: "Getting Started with Conformance"
description: "Learn how to set up Conformance for your codebase."
last_updated: "null"
source: "https://vercel.com/docs/conformance/getting-started"
--------------------------------------------------------------------------------

# Getting Started with Conformance

Copy page

Ask AI about this page

Last updated October 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

To [set up Conformance](#setting-up-conformance-in-your-repository) in your repository, you must:

*   Set up [Vercel's private npm registry](/docs/private-registry) to install the necessary packages
*   [Install and initialize](/docs/conformance/getting-started#setting-up-conformance-in-your-repository) Conformance in your repository

If you've already set up Code Owners, you may have already completed some of these steps.

## [Prerequisites](#prerequisites)

### [Get access to Conformance](#get-access-to-conformance)

To enable Conformance for your Enterprise team, you'll need to request access through your Vercel account administrator.

### [Setting up Vercel's private npm registry](#setting-up-vercel's-private-npm-registry)

Vercel distributes packages with the `@vercel-private` scope through our private npm registry, and requires that each user using the package authenticates through a Vercel account.

To use the private npm registry, you'll need to follow the documentation to:

*   [Set up your local environment](/docs/private-registry#setting-up-your-local-environment) – This should be completed by the team owner, but each member of your team will need to log in
*   [Set up Vercel](/docs/private-registry#setting-up-vercel) – This should be completed by the team owner
*   [Optionally, set up Conformance for use with CI](/docs/private-registry#setting-up-your-ci-provider) – This should be completed by the team owner

## [Setting up Conformance in your repository](#setting-up-conformance-in-your-repository)

This section guides you through setting up Conformance for your repository.

1.  ### [Set up the Vercel CLI](#set-up-the-vercel-cli)
    
    The Conformance CLI is separate to the [Vercel CLI](/docs/cli), however it uses the Vercel CLI for authentication.
    
    Before continuing, please ensure that the Vercel CLI is [installed](/docs/cli#installing-vercel-cli) and that you are [logged in](/docs/cli/login).
    
2.  ### [Initialize Conformance](#initialize-conformance)
    
    Use the CLI to automatically initialize Conformance in your project. Start by running this command in your repository's root:
    
    pnpmyarnnpmbun
    
    ```
    pnpm --package=@vercel-private/conformance dlx vercel-conformance init
    ```
    
    `yarn dlx` only works with Yarn version 2 or newer, for Yarn v1 use  
    `yarn -DW add @vercel-private/conformance && yarn vercel-conformance init`
    
    After running, check the installation success by executing:
    
    pnpmyarnnpmbun
    
    ```
    pnpm conformance
    ```
    
3.  ### [Review the generated changes](#review-the-generated-changes)
    
    The Conformance `init` command creates the following changes:
    
    *   First, it installs the CLI package in your root `package.json` and every workspace `package.json`, if your monorepo uses workspaces.
    *   It also adds a `conformance` script to the `scripts` field of every `package.json`. This script runs Conformance.
    *   It adds any existing Conformance errors to allowlists, letting you start using Conformance without immediate fixes and allowing you to gradually resolve these allowlist entries over time. Learn more about Conformance Allowlists in the [documentation](/docs/conformance/allowlist).
    
    Once you've reviewed these, open a pull request with the changes and merge it.
    
4.  ### [Add owners for allowlist files](#add-owners-for-allowlist-files)
    
    \*\* This step assumes you have [set up Code Owners](/docs/code-owners/getting-started).\*\*
    
    Conformance allows specific individuals to review modifications to allowlist files. Add a `.vercel.approvers` file at your repository's root:
    
    .vercel.approvers
    
    ```
    **/*.allowlist.json @org/team:required
    ```
    
    Now, changes to allowlist files need a review from someone on `@org/team` before merging.
    
    Learn more about [wildcard syntax](/docs/code-owners/code-approvers#globstar-pattern) and [`:required` syntax](/docs/code-owners/code-approvers#required) from Code Owners.
    
5.  ### [Add Conformance to your CI system](#add-conformance-to-your-ci-system)
    
    You can integrate Conformance in your CI to avoid merging errors into your code. To learn more, see [Setting up your CI provider](/docs/private-registry#setting-up-your-ci-provider).
    

## [More resources](#more-resources)

*   [Code Owners](/docs/code-owners)
*   [Conformance](/docs/conformance)

--------------------------------------------------------------------------------
title: "Conformance Rules"
description: "Learn how Conformance improves collaboration, productivity, and software quality at scale."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules"
--------------------------------------------------------------------------------

# Conformance Rules

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This page lists all the built-in rules that Conformance will check for by default in your application.

Next.jsPerformanceSecurityCode Health

These Conformance rules catch common issues that can happen in Next.js applications.

| Test Name | Description |
| --- | --- |
| [ESLINT\_NEXT\_RULES\_REQUIRED](/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED) | Requires that ESLint is configured for Next.js. |
| [NEXTJS\_MISSING\_MODULARIZE\_IMPORTS](/docs/conformance/rules/NEXTJS_MISSING_MODULARIZE_IMPORTS) | Requires that Next.js applications that use libraries with barrel exports use `modularizeImports` to minimize impact on dev compilation speed and bundle size. |
| [NEXTJS\_MISSING\_OPTIMIZE\_PACKAGE\_IMPORTS](/docs/conformance/rules/NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS) | Requires that Next.js applications that use libraries with barrel exports use `optimizePackageImports` to minimize impact on dev compilation speed and bundle size. |
| [NEXTJS\_MISSING\_NEXT13\_TYPESCRIPT\_PLUGIN](/docs/conformance/rules/NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN) | Applications using Next 13 should use the "next" TypeScript plugin for an improved Next.js experience. |
| [NEXTJS\_MISSING\_REACT\_STRICT\_MODE](/docs/conformance/rules/NEXTJS_MISSING_REACT_STRICT_MODE) | Applications using Next.js should enable React Strict Mode to identify unsafe lifecycles and legacy API usage. |
| [NEXTJS\_MISSING\_SECURITY\_HEADERS](/docs/conformance/rules/NEXTJS_MISSING_SECURITY_HEADERS) | Requires that important security headers are set correctly for Next.js apps and contain valid directives. |
| [NEXTJS\_NO\_ASYNC\_LAYOUT](/docs/conformance/rules/NEXTJS_NO_ASYNC_LAYOUT) | Ensures that the exported Next.js `layout` component and its transitive dependencies are not asynchronous, as that can block the rendering of the layout and the rest of the page. |
| [NEXTJS\_NO\_ASYNC\_PAGE](/docs/conformance/rules/NEXTJS_NO_ASYNC_PAGE) | Ensures that the exported Next.js `page` component and its transitive dependencies are not asynchronous, as that blocks the rendering of the page. |
| [NEXTJS\_NO\_BEFORE\_INTERACTIVE](/docs/conformance/rules/NEXTJS_NO_BEFORE_INTERACTIVE) | Requires review of usage of the `beforeInteractive` strategy in `Script` (`next/script`) elements as this can cause performance issues. |
| [NEXTJS\_NO\_CLIENT\_DEPS\_IN\_MIDDLEWARE](/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE) | Disallows dependencies on client libraries to improve bundle size and execution time of Next.js middleware. |
| [NEXTJS\_NO\_DYNAMIC\_AUTO](/docs/conformance/rules/NEXTJS_NO_DYNAMIC_AUTO) | Prevent usage of `force-dynamic` as a dynamic page rendering strategy. |
| [NEXTJS\_NO\_FETCH\_IN\_SERVER\_PROPS](/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS) | Prevent relative `fetch` calls in `getServerSideProps` from being added to Next.js applications. |
| [NEXTJS\_NO\_GET\_INITIAL\_PROPS](/docs/conformance/rules/NEXTJS_NO_GET_INITIAL_PROPS) | Requires any use of `getInitialProps` in Next.js pages be reviewed and approved, and encourages using `getServerSideProps` or `getStaticProps` instead. |
| [NEXTJS\_NO\_PRODUCTION\_SOURCE\_MAPS](/docs/conformance/rules/NEXTJS_NO_PRODUCTION_SOURCE_MAPS) | Applications using Next.js should not enable production source maps so that they don't publicly share source code. |
| [NEXTJS\_NO\_SELF\_HOSTED\_VIDEOS](/docs/conformance/rules/NEXTJS_NO_SELF_HOSTED_VIDEOS) | Prevent video files from being added to Next.js applications to improve performance and bandwidth usage. |
| [NEXTJS\_NO\_TURBO\_CACHE](/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE) | Prevent Turborepo from caching the Next.js `.next/cache` folder to prevent an oversized cache. |
| [NEXTJS\_REQUIRE\_EXPLICIT\_DYNAMIC](/docs/conformance/rules/NEXTJS_REQUIRE_EXPLICIT_DYNAMIC) | Requires explicitly setting the `dynamic` route segment option for Next.js pages and routes. |
| [NEXTJS\_SAFE\_NEXT\_PUBLIC\_ENV\_USAGE](/docs/conformance/rules/NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE) | Usage process.env.NEXT_PUBLIC_\* environment variables must be allowlisted. |
| [NEXTJS\_SAFE\_SVG\_IMAGES](/docs/conformance/rules/NEXTJS_SAFE_SVG_IMAGES) | Prevent `dangerouslyAllowSVG` without Content Security Policy in Next.js applications. |
| [NEXTJS\_SAFE\_URL\_IMPORTS](/docs/conformance/rules/NEXTJS_SAFE_URL_IMPORTS) | Prevent unsafe URL Imports from being added to Next.js applications. |
| [NEXTJS\_UNNEEDED\_GET\_SERVER\_SIDE\_PROPS](/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS) | Catches usages of `getServerSideProps` that could use static rendering instead, improving the performance of those pages. |
| [NEXTJS\_USE\_NATIVE\_FETCH](/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH) | Requires using native `fetch` which Next.js provides, removing the need for third-party fetch libraries. |
| [NEXTJS\_USE\_NEXT\_FONT](/docs/conformance/rules/NEXTJS_USE_NEXT_FONT) | Requires using `next/font` (when possible), which optimizes fonts for improved privacy and performance. |
| [NEXTJS\_USE\_NEXT\_IMAGE](/docs/conformance/rules/NEXTJS_USE_NEXT_IMAGE) | Requires that `next/image` is used for all images for improved performance. |
| [NEXTJS\_USE\_NEXT\_SCRIPT](/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT) | Requires that `next/script` is used for all scripts for improved performance. |
| [NO\_FETCH\_FROM\_MIDDLEWARE](/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE) | Requires that any `fetch` call that is depended on transitively by Next.js middleware be reviewed and approved before use for performance reasons. |
| [REACT\_NO\_STATIC\_IMPORTS\_IN\_EVENT\_HANDLERS](/docs/conformance/rules/REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS) | Prevent static imports that are referenced only in React event handlers from being eagerly loaded in React components. |

These Conformance rules catch issues that negatively affect the performance of your website.

| Test Name | Description |
| --- | --- |
| [BFCACHE\_INTEGRITY\_NO\_UNLOAD\_LISTENERS](/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS) | Disallows the use of the `unload` event to eliminate a source of eviction from the browser's Back-Forward Cache. |
| [BFCACHE\_INTEGRITY\_REQUIRE\_NOOPENER\_ATTRIBUTE](/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE) | Requires that links opened with `window.open` use the `noopener` attribute to eliminate a source of eviction from the browser's Back-Forward Cache. |
| [NEXTJS\_NO\_ASYNC\_LAYOUT](/docs/conformance/rules/NEXTJS_NO_ASYNC_LAYOUT) | Ensures that the exported Next.js `layout` component and its transitive dependencies are not asynchronous, as that can block the rendering of the layout and the rest of the page. |
| [NEXTJS\_NO\_ASYNC\_PAGE](/docs/conformance/rules/NEXTJS_NO_ASYNC_PAGE) | Ensures that the exported Next.js `page` component and its transitive dependencies are not asynchronous, as that blocks the rendering of the page. |
| [NEXTJS\_NO\_BEFORE\_INTERACTIVE](/docs/conformance/rules/NEXTJS_NO_BEFORE_INTERACTIVE) | Requires review of usage of the `beforeInteractive` strategy in `Script` (`next/script`) elements as this can cause performance issues. |
| [NEXTJS\_NO\_CLIENT\_DEPS\_IN\_MIDDLEWARE](/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE) | Disallows dependencies on client libraries to improve bundle size and execution time of Next.js middleware. |
| [NEXTJS\_NO\_DYNAMIC\_AUTO](/docs/conformance/rules/NEXTJS_NO_DYNAMIC_AUTO) | Prevent usage of `force-dynamic` as a dynamic page rendering strategy. |
| [NEXTJS\_NO\_FETCH\_IN\_SERVER\_PROPS](/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS) | Prevent relative `fetch` calls in `getServerSideProps` from being added to Next.js applications. |
| [NEXTJS\_NO\_GET\_INITIAL\_PROPS](/docs/conformance/rules/NEXTJS_NO_GET_INITIAL_PROPS) | Requires any use of `getInitialProps` in Next.js pages be reviewed and approved, and encourages using `getServerSideProps` or `getStaticProps` instead. |
| [NEXTJS\_REQUIRE\_EXPLICIT\_DYNAMIC](/docs/conformance/rules/NEXTJS_REQUIRE_EXPLICIT_DYNAMIC) | Requires explicitly setting the `dynamic` route segment option for Next.js pages and routes. |
| [NEXTJS\_UNNEEDED\_GET\_SERVER\_SIDE\_PROPS](/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS) | Catches usages of `getServerSideProps` that could use static rendering instead, improving the performance of those pages. |
| [NEXTJS\_USE\_NATIVE\_FETCH](/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH) | Requires using native `fetch` which Next.js provides, removing the need for third-party fetch libraries. |
| [NEXTJS\_USE\_NEXT\_IMAGE](/docs/conformance/rules/NEXTJS_USE_NEXT_IMAGE) | Requires that `next/image` is used for all images for improved performance. |
| [NEXTJS\_USE\_NEXT\_SCRIPT](/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT) | Requires that `next/script` is used for all scripts for improved performance. |
| [NO\_EXTERNAL\_CSS\_AT\_IMPORTS](/docs/conformance/rules/NO_EXTERNAL_CSS_AT_IMPORTS) | Disallows `@import` at-rules that import from external URLs. |
| [NO\_FETCH\_FROM\_MIDDLEWARE](/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE) | Requires that any `fetch` call that is depended on transitively by Next.js middleware be reviewed and approved before use for performance reasons. |
| [NO\_INLINE\_SVG](/docs/conformance/rules/NO_INLINE_SVG) | Prevent the use of `svg` tags inline. |
| [NO\_MIXED\_ASYNC\_MODULES](/docs/conformance/rules/NO_MIXED_ASYNC_MODULES) | Prevent imports to modules that contain top-level awaits in your applications. |
| [NO\_POSTINSTALL\_SCRIPT](/docs/conformance/rules/NO_POSTINSTALL_SCRIPT) | Prevent the use of `"postinstall"` script in packages. |
| [NO\_SERIAL\_ASYNC\_CALLS](/docs/conformance/rules/NO_SERIAL_ASYNC_CALLS) | Prevent blocking serial async await calls in your applications. |
| [REACT\_NO\_STATIC\_IMPORTS\_IN\_EVENT\_HANDLERS](/docs/conformance/rules/REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS) | Prevent static imports that are referenced only in React event handlers from being eagerly loaded in React components. |
| [REACT\_STABLE\_CONTEXT\_PROVIDER\_VALUE](/docs/conformance/rules/REACT_STABLE_CONTEXT_PROVIDER_VALUE) | Prevent non-stable values from being used in React Context providers that could cause unnecessary re-renders. |

These Conformance rules catch issues that could become security vulnerabilities in your application.

| Test Name | Description |
| --- | --- |
| [NEXTJS\_MISSING\_SECURITY\_HEADERS](/docs/conformance/rules/NEXTJS_MISSING_SECURITY_HEADERS) | Requires that important security headers are set correctly for Next.js apps and contain valid directives. |
| [NEXTJS\_NO\_PRODUCTION\_SOURCE\_MAPS](/docs/conformance/rules/NEXTJS_NO_PRODUCTION_SOURCE_MAPS) | Applications using Next.js should not enable production source maps so that they don't publicly share source code. |
| [NEXTJS\_SAFE\_NEXT\_PUBLIC\_ENV\_USAGE](/docs/conformance/rules/NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE) | Usage process.env.NEXT_PUBLIC_\* environment variables must be allowlisted. |
| [NEXTJS\_SAFE\_SVG\_IMAGES](/docs/conformance/rules/NEXTJS_SAFE_SVG_IMAGES) | Prevent `dangerouslyAllowSVG` without Content Security Policy in Next.js applications. |
| [NEXTJS\_SAFE\_URL\_IMPORTS](/docs/conformance/rules/NEXTJS_SAFE_URL_IMPORTS) | Prevent unsafe URL Imports from being added to Next.js applications |
| [NO\_ASSIGN\_WINDOW\_LOCATION](/docs/conformance/rules/NO_ASSIGN_WINDOW_LOCATION) | Prevent unsafe assignment to `window.location.href` in your application. |
| [NO\_CORS\_HEADERS](/docs/conformance/rules/NO_CORS_HEADERS) | Requires that CORS header configuration is reviewed and allowlisted since these headers can open up servers to security vulnerabilities. |
| [NO\_DANGEROUS\_HTML](/docs/conformance/rules/NO_DANGEROUS_HTML) | Prevent the unsafe creation of DOM through HTML methods in your application which could lead to security vulnerabilities. |
| [NO\_DOCUMENT\_WRITE](/docs/conformance/rules/NO_DOCUMENT_WRITE) | Prevent unsafe usage of `document.write()` in your application. |
| [NO\_EVAL](/docs/conformance/rules/NO_EVAL) | Prevent unsafe usage of `eval()` in your application since this allows arbitrary code execution. |
| [NO\_VARIABLE\_IMPORT\_REFERENCES](/docs/conformance/rules/NO_VARIABLE_IMPORT_REFERENCES) | Prevents loading of arbitrary modules from `import` or `require` statements which could lead to security vulnerabilities. |
| [REQUIRE\_CARET\_DEPENDENCIES](/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES) | Prevent the use of dependencies without a caret ("^") as a prefix. |
| [SET\_COOKIE\_VALIDATION](/docs/conformance/rules/SET_COOKIE_VALIDATION) | Prevents usage of cookies that do not conform to the allowed cookie policy. |

These Conformance rules catch issues that can negatively affect your codebase or code health.

| Test Name | Description |
| --- | --- |
| [ESLINT\_CONFIGURATION](/docs/conformance/rules/ESLINT_CONFIGURATION) | Requires that a workspace package is configured with ESLint. |
| [ESLINT\_REACT\_RULES\_REQUIRED](/docs/conformance/rules/ESLINT_REACT_RULES_REQUIRED) | Requires that ESLint is configured for React. |
| [ESLINT\_RULES\_REQUIRED](/docs/conformance/rules/ESLINT_RULES_REQUIRED) | Requires that ESLint has plugins and rules configured correctly. |
| [NEXTJS\_MISSING\_MODULARIZE\_IMPORTS](/docs/conformance/rules/NEXTJS_MISSING_MODULARIZE_IMPORTS) | Requires that Next.js applications that use libraries with barrel exports use `modularizeImports` to minimize impact on dev compilation speed and bundle size. |
| [NO\_ASSIGN\_WINDOW\_LOCATION](/docs/conformance/rules/NO_ASSIGN_WINDOW_LOCATION) | Prevent unsafe assignment to `window.location.href` in your application. |
| [NO\_INSTANCEOF\_ERROR](/docs/conformance/rules/NO_INSTANCEOF_ERROR) | Disallows using `error instanceof Error` comparisons due to risk of false negatives. |
| [NO\_UNNECESSARY\_PROP\_SPREADING](/docs/conformance/rules/NO_UNNECESSARY_PROP_SPREADING) | Prevent the use of object spreading as a prop in a JSX component |
| [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED) | Requires that every `package.json` file has the `description` field set. |
| [PACKAGE\_JSON\_DUPLICATE\_DEPENDENCIES](/docs/conformance/rules/PACKAGE_JSON_DUPLICATE_DEPENDENCIES) | Found duplicate dependencies between the list of `dependencies` and `devDependencies` or `peerDependencies` in a `package.json` file. |
| [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED) | Requires that every `package.json` file has the `name` field set to ensure each workspace has a unique identifier. |
| [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED) | Requires that every `package.json` file has the `private` field set to prevent accidental publishing to npm. |
| [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED) | Requires that every `package.json` file has the `sideEffects` field set to ensure tree-shaking works optimally. |
| [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED) | Requires that every `package.json` file has the `type` field set to encourage using `esm` since `commonjs` is the default. |
| [PACKAGE\_MANAGEMENT\_NO\_CIRCULAR\_IMPORTS](/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS) | Circular imports between two files are not allowed. |
| [PACKAGE\_MANAGEMENT\_NO\_UNRESOLVED\_IMPORTS](/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_UNRESOLVED_IMPORTS) | Import statements that can not be resolved to a local file or a package from `package.json` dependencies are not allowed. |
| [PACKAGE\_MANAGEMENT\_REQUIRED\_README](/docs/conformance/rules/PACKAGE_MANAGEMENT_REQUIRED_README) | Requires that every workspace has a `README.md` file in the root of the workspace. |
| [REQUIRE\_DOCS\_ON\_EXPORTED\_FUNCTIONS](/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS) | Requires that all exported functions have JSDoc comments. |
| [REQUIRE\_NODE\_VERSION\_FILE](/docs/conformance/rules/REQUIRE_NODE_VERSION_FILE) | Requires that workspaces have a valid Node.js version file (`.node-version` or `.nvmrc`) file defined. |
| [REQUIRE\_ONE\_VERSION\_POLICY](/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY) | Requires all dependencies in a monorepo to have the same version policy. |
| [TESTS\_NO\_CONDITIONAL\_ASSERTIONS](/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS) | Requires that assertions are not conditional, or that `expect.assertions` is used. |
| [TESTS\_NO\_ONLY](/docs/conformance/rules/TESTS_NO_ONLY) | Requires that focused tests (i.e. `it.only()`) are unfocused. |
| [TYPESCRIPT\_CONFIGURATION](/docs/conformance/rules/TYPESCRIPT_CONFIGURATION) | Requires that a workspace package that uses TypeScript files has configured TypeScript correctly for that workspace. |
| [TYPESCRIPT\_ONLY](/docs/conformance/rules/TYPESCRIPT_ONLY) | Requires that a workspace package may only contain TypeScript files and no JavaScript or JSX files. |
| [WORKSPACE\_MISSING\_CONFORMANCE\_SCRIPT](/docs/conformance/rules/WORKSPACE_MISSING_CONFORMANCE_SCRIPT) | All packages must define a `conformance` script that invokes the CLI binary. |
| [WORKSPACE\_MISSING\_PACKAGE\_JSON](/docs/conformance/rules/WORKSPACE_MISSING_PACKAGE_JSON) | All directories that match a workspace glob must include a `package.json` file. |

--------------------------------------------------------------------------------
title: "BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS"
description: "Disallows the use of the unload and beforeunload events to eliminate a source of eviction from the browser's Back-Forward Cache."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS"
--------------------------------------------------------------------------------

# BFCACHE\_INTEGRITY\_NO\_UNLOAD\_LISTENERS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule disallows the use of the `unload` and `beforeunload` events to improve the integrity of the Back-Forward Cache in browsers.

The Back-Forward Cache (bfcache) is a browser feature that allows pages to be cached in memory when the user navigates away from them. When the user navigates back to the page, it can be loaded almost instantly from the cache instead of having to be reloaded from the network. Breaking the bfcache's integrity can cause a page to be reloaded from the network when the user navigates back to it, which can be slow and jarring.

The most important rule for maintaining the integrity of the bfcache is to not use the `unload` event. This event is fired when the user navigates away from the page, but it is unreliable and disables the cache on most browsers.

The `beforeunload` event can also make your page ineligible for the cache in browsers so it is better to avoid using. However there are some legitimate use cases for this event, such as checking if the user has unsaved work before they exit the page. In this case it is recommended to add the listener conditionally and remove it as soon as the work as been saved.

Alternative events that can be considered are `pagehide` or `visibilitychange`, which are more reliable events that do not break the bfcache and will fire when the user navigates away from or unfocuses the page.

To learn more about the bfcache, see the [web.dev docs](https://web.dev/bfcache).

## [Related Rules](#related-rules)

*   [BFCACHE\_INTEGRITY\_REQUIRE\_NOOPENER\_ATTRIBUTE](/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE)

## [Example](#example)

Two examples of when this check would fail:

src/utils/handle-user-navigation.ts

```
export function handleUserNavigatingAway() {
  window.onunload = (event) => {
    console.log('Page has unloaded.');
  };
}
 
export function handleUserAboutToNavigateAway() {
  window.onbeforeunload = (event) => {
    console.log('Page is about to be unloaded.');
  };
}
```

src/utils/handle-user-navigation.ts

```
export function handleUserNavigatingAway() {
  window.addEventListener('unload', (event) => {
    console.log('Page has unloaded.');
  });
}
 
export function handleUserAboutToNavigateAway() {
  window.addEventListener('beforeunload', (event) => {
    console.log('Page is about to be unloaded.');
  });
}
```

## [How to fix](#how-to-fix)

Instead, we can use the `pagehide` event to detect when the user navigates away from the page.

src/utils/handle-user-navigation.ts

```
export function handleUserNavigatingAway() {
  window.onpagehide = (event) => {
    console.log('Page is about to be hidden.');
  };
}
```

src/utils/handle-user-navigation.ts

```
export function handleUserNavigatingAway() {
  window.addEventListener('pagehide', (event) => {
    console.log('Page is about to be hidden.');
  });
}
```

--------------------------------------------------------------------------------
title: "BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE"
description: "Requires that links opened with window.open use the noopener attribute to eliminate a source of eviction from the browser's Back-Forward Cache."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/BFCACHE_INTEGRITY_REQUIRE_NOOPENER_ATTRIBUTE"
--------------------------------------------------------------------------------

# BFCACHE\_INTEGRITY\_REQUIRE\_NOOPENER\_ATTRIBUTE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The Back-Forward Cache (bfcache) is a browser feature that allows pages to be cached in memory when the user navigates away from them. When the user navigates back to the page, it can be loaded almost instantly from the cache instead of having to be reloaded from the network. Breaking the bfcache's integrity can cause a page to be reloaded from the network when the user navigates back to it, which can be slow and jarring.

Pages opened with `window.open` that do not use the `noopener` attribute can both be a security risk and also will prevent browsers from caching the page in the bfcache. This is because the new window can access the `window.opener` property of the original window, so putting the original page into the bfcache could break the new window when attempting to access it.

Using the `noreferrer` attribute will also set the `noopener` attribute to true, so it can also be used to ensure the page is placed into the bfcache.

To learn more about the bfcache, see the [web.dev docs](https://web.dev/bfcache).

## [Related Rules](#related-rules)

*   [BFCACHE\_INTEGRITY\_NO\_UNLOAD\_LISTENERS](/docs/conformance/rules/BFCACHE_INTEGRITY_NO_UNLOAD_LISTENERS)

## [Example](#example)

Examples of when this check would fail:

```
window.open('https://example.com', '_blank');
window.open('https://example.com');
```

## [How to fix](#how-to-fix)

Instead, use the `noopener` or `noreferrer` attributes:

```
window.open('https://example.com', '_blank', 'noopener');
window.open('https://example.com', '_top', 'noreferrer');
```

--------------------------------------------------------------------------------
title: "ESLINT_CONFIGURATION"
description: "Requires that a workspace package has ESLint installed and configured correctly"
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/ESLINT_CONFIGURATION"
--------------------------------------------------------------------------------

# ESLINT\_CONFIGURATION

Copy page

Ask AI about this page

Last updated April 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

[ESLint](https://eslint.org/) is a tool to statically analyze code to find and report problems. ESLint is required to be enabled for every workspace package in a monorepo so that all code in the monorepo is checked for these problems. Additionally, repositories can enforce that particular ESLint plugins are installed and that specific rules are treated as errors.

This rule requires that:

*   An ESLint config exists in the current workspace.
*   A script to run ESLint exists in `package.json` in the current workspace.
*   `reportUnusedDisableDirectives` is set to `true`, which detects and can autofix unused ESLint disable comments.
*   `root` is set to `true`, which ensures that workspaces don't inherit unintended rules and configuration from ESLint configuration files in parent directories.

## [Example](#example)

```
A Conformance error occurred in test "ESLINT_CONFIGURATION".
 
ESLint configuration must specify `reportUnusedDisableDirectives` to be `true`
 
To find out more information and how to fix this error, visit
/docs/conformance/rules/ESLINT_CONFIGURATION.
 
If this violation should be ignored, add the following entry to
/apps/dashboard/.allowlists/ESLINT_CONFIGURATION.allowlist.json and get approval from the appropriate person.
 
{
  "testName": "ESLINT_CONFIGURATION",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "dashboard"
  }
}
```

See the [ESLint docs](https://eslint.org/docs/latest/use/configure/) for more information on how to configure ESLint, including plugins and rules.

## [How To Fix](#how-to-fix)

The recommended approach for configuring ESLint in a monorepo is to have a shared ESLint config in an internal package. See the [Turbo docs on ESLint](https://turborepo.com/docs/handbook/linting/eslint) to get started.

Once your monorepo has a shared ESLint config, you can add a `.eslintrc.cjs` file to the root folder of your workspace with the contents:

.eslintrc.cjs

```
module.exports = {
  root: true,
  extends: ['eslint-config-custom/base'],
};
```

You should also add `"eslint-config-custom": "workspace:*"` to your `devDependencies`.

--------------------------------------------------------------------------------
title: "ESLINT_NEXT_RULES_REQUIRED"
description: "Requires that a workspace package is configured with required Next.js plugins and rules"
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED"
--------------------------------------------------------------------------------

# ESLINT\_NEXT\_RULES\_REQUIRED

Copy page

Ask AI about this page

Last updated April 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This Conformance check requires that ESLint plugins for Next.js are configured correctly in your application, including:

*   [@next/next](https://nextjs.org/docs/basic-features/eslint#eslint-plugin)

These plugins help to catch common Next.js issues, including performance.

## [Example](#example)

```
A Conformance error occurred in test "ESLINT_NEXT_RULES_REQUIRED".
 
These ESLint plugins must have rules configured to run: @next/next
 
To find out more information and how to fix this error, visit
https://vercel.com/docs/conformance/rules/ESLINT_NEXT_RULES_REQUIRED.
 
If this violation should be ignored, add the following entry to
/apps/dashboard/.allowlists/ESLINT_NEXT_RULES_REQUIRED.allowlist.json and
get approval from the appropriate person.
 
{
  "testName": "ESLINT_NEXT_RULES_REQUIRED",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "dashboard"
  },
}
```

This check requires that certain ESLint plugins are installed and rules within those plugins are configured to be errors. If you are missing required plugins, you will receive an error such as:

```
ESLint configuration is missing required security plugins:
  Missing plugins: @next/next
  Registered plugins: import and @typescript-eslint
```

For more information on ESLint plugins and rules, see [plugins](https://eslint.org/docs/latest/user-guide/configuring/plugins) and [rules](https://eslint.org/docs/latest/user-guide/configuring/rules).

## [How To Fix](#how-to-fix)

The recommended approach for configuring ESLint in a monorepo is to have a shared ESLint config in an internal package. See the [Turbo docs on ESLint](https://turborepo.com/docs/handbook/linting/eslint) to get started.

Once your monorepo has a shared ESLint config, you can add a `.eslintrc.cjs` file to the root folder of your workspace with the contents:

.eslintrc.cjs

```
module.exports = {
  root: true,
  extends: ['eslint-config-custom/base'],
};
```

You should also add `"eslint-config-custom": "workspace:*"` to your `devDependencies`.

--------------------------------------------------------------------------------
title: "ESLINT_REACT_RULES_REQUIRED"
description: "Requires that a workspace package is configured with required React plugins and rules"
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/ESLINT_REACT_RULES_REQUIRED"
--------------------------------------------------------------------------------

# ESLINT\_REACT\_RULES\_REQUIRED

Copy page

Ask AI about this page

Last updated April 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This Conformance check requires that ESLint plugins for React are configured correctly in your application, including:

*   [react](https://github.com/jsx-eslint/eslint-plugin-react)
*   [react-hooks](https://github.com/facebook/react/tree/main/packages/eslint-plugin-react-hooks)
*   [jsx-a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y)

These plugins help to catch common React issues, such as incorrect React hooks usage, helping to reduce bugs and to improve application accessibility.

## [Example](#example)

```
A Conformance error occurred in test "ESLINT_REACT_RULES_REQUIRED".
 
These ESLint plugins must have rules configured to run: @next/next
 
To find out more information and how to fix this error, visit
https://vercel.com/docs/conformance/rules/ESLINT_REACT_RULES_REQUIRED.
 
If this violation should be ignored, add the following entry to
/apps/dashboard/.allowlists/ESLINT_REACT_RULES_REQUIRED.allowlist.json and
get approval from the appropriate person.
 
{
  "testName": "ESLINT_REACT_RULES_REQUIRED",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "dashboard"
  },
}
```

This check requires that certain ESLint plugins are installed and rules within those plugins are configured to be errors. If you are missing required plugins, you will receive an error such as:

```
ESLint configuration is missing required security plugins:
  Missing plugins: react, react-hooks, and jsx-a11y
  Registered plugins: import and @typescript-eslint
```

For more information on ESLint plugins and rules, see [plugins](https://eslint.org/docs/latest/user-guide/configuring/plugins) and [rules](https://eslint.org/docs/latest/user-guide/configuring/rules).

## [How To Fix](#how-to-fix)

The recommended approach for configuring ESLint in a monorepo is to have a shared ESLint config in an internal package. See the [Turbo docs on ESLint](https://turborepo.com/docs/handbook/linting/eslint) to get started.

Once your monorepo has a shared ESLint config, you can add a `.eslintrc.cjs` file to the root folder of your workspace with the contents:

.eslintrc.cjs

```
module.exports = {
  root: true,
  extends: ['eslint-config-custom/base'],
};
```

You should also add `"eslint-config-custom": "workspace:*"` to your `devDependencies`.

--------------------------------------------------------------------------------
title: "ESLINT_RULES_REQUIRED"
description: "Requires that a workspace package is configured with required ESLint plugins and rules"
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/ESLINT_RULES_REQUIRED"
--------------------------------------------------------------------------------

# ESLINT\_RULES\_REQUIRED

Copy page

Ask AI about this page

Last updated April 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This Conformance check requires that ESLint plugins are configured correctly in your application, including:

*   [@typescript-eslint](https://typescript-eslint.io/)
*   [eslint-comments](https://mysticatea.github.io/eslint-plugin-eslint-comments/)
*   [import](https://github.com/import-js/eslint-plugin-import)

These plugins help to catch common issues, and ensure that ESLint is set up to work with TypeScript where applicable.

## [Example](#example)

```
A Conformance error occurred in test "ESLINT_RULES_REQUIRED".
 
These ESLint plugins must have rules configured to run: @typescript-eslint and import
 
To find out more information and how to fix this error, visit
https://vercel.com/docs/conformance/rules/ESLINT_RULES_REQUIRED.
 
If this violation should be ignored, add the following entry to
/apps/dashboard/.allowlists/ESLINT_RULES_REQUIRED.allowlist.json and
get approval from the appropriate person.
 
{
  "testName": "ESLINT_RULES_REQUIRED",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "dashboard"
  },
}
```

This check requires that certain ESLint plugins are installed and rules within those plugins are configured to be errors. If you are missing required plugins, you will receive an error such as:

```
ESLint configuration is missing required security plugins:
  Missing plugins: eslint-comments
  Registered plugins: import and @typescript-eslint
```

If all the required plugins are installed but some rules are not configured to run or configured to be errors, you will receive an error such as:

```
`eslint-comments/no-unlimited-disable` must be specified as an error in the ESLint configuration, but is specified as off.
```

As a part of this test, some rules are forbidden from being disabled. If you disable those rules, you will receive an error such as:

```
Disabling these ESLint rules is not allowed.
Please see the ESLint documentation for each rule for how to fix.
eslint-comments/disable-enable-pair
eslint-comments/no-restricted-disable
```

For more information on ESLint plugins and rules, see [plugins](https://eslint.org/docs/latest/user-guide/configuring/plugins) and [rules](https://eslint.org/docs/latest/user-guide/configuring/rules).

## [How To Fix](#how-to-fix)

The recommended approach for configuring ESLint in a monorepo is to have a shared ESLint config in an internal package. See the [Turbo docs on ESLint](https://turborepo.com/docs/handbook/linting/eslint) to get started.

Once your monorepo has a shared ESLint config, you can add a `.eslintrc.cjs` file to the root folder of your workspace with the contents:

.eslintrc.cjs

```
module.exports = {
  root: true,
  extends: ['eslint-config-custom/base'],
};
```

You should also add `"eslint-config-custom": "workspace:*"` to your `devDependencies`.

--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_MODULARIZE_IMPORTS"
description: "modularizeImports can improve dev compilation speed for packages that use barrel files."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_MODULARIZE_IMPORTS"
--------------------------------------------------------------------------------

# NEXTJS\_MISSING\_MODULARIZE\_IMPORTS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule has been deprecated as of version [1.10.0](/docs/conformance/changelog#1.10.0)and will be removed in 1.10.0.

`modularizeImports` is a feature of Next 13 that can reduce dev compilation times when importing packages that are exported as barrel files. Barrel files are convenient ways to export code from a package from a single file to make it straightforward to import any of the code from the package. However, since they export a lot of code from the same file, importing these packages can cause tools to do a lot of additional work analyzing files that are unused in the application.

## [How to fix](#how-to-fix)

To fix this, you can add a `modularizeImports` config to `next.config.js` for the package that uses barrel files. For example:

next.config.js

```
modularizeImports: {
  lodash: {
    transform: 'lodash/{{member}}';
  }
}
```

The exact format of the transform may differ by package, so double check how the package uses barrel files first.

See the [Next.js docs](https://nextjs.org/docs/architecture/nextjs-compiler#modularize-imports) for more information.

## [Custom configuration](#custom-configuration)

You can also specify required `modularizeImports` config for your own packages.

In your `conformance.config.jsonc` file, add:

conformance.config.jsonc

```
NEXTJS_MISSING_MODULARIZE_IMPORTS: {
  requiredModularizeImports: [
    {
      moduleDependency: 'your-package-name',
      requiredConfig: {
        transform: 'your-package-name/{{member}}',
      },
    },
  ];
}
```

This will require that any workspace in your monorepo that uses the `your-package-name` package must use the provided `modularizeImports` config in their `next.config.js` file.

See [Customizing Conformance](/docs/conformance/customize) for more information.

--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN"
description: "Applications using Next 13 should use the "next" TypeScript plugin."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_NEXT13_TYPESCRIPT_PLUGIN"
--------------------------------------------------------------------------------

# NEXTJS\_MISSING\_NEXT13\_TYPESCRIPT\_PLUGIN

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Next 13 introduced a TypeScript plugin to provide richer information for Next.js applications using TypeScript. See the [Next.js docs](https://nextjs.org/docs/app/building-your-application/configuring/typescript#using-the-typescript-plugin) for more information.

## [How to fix](#how-to-fix)

Add the following to `plugins` in the `compilerOptions` of your `tsconfig.json` file.

tsconfig.json

```
"compilerOptions": {
    "plugins": [{ "name": "next" }]
  }
```

--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS"
description: "optimizePackageImports improves compilation speed for packages that use barrel files or export many modules."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_OPTIMIZE_PACKAGE_IMPORTS"
--------------------------------------------------------------------------------

# NEXTJS\_MISSING\_OPTIMIZE\_PACKAGE\_IMPORTS

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

[`optimizePackageImports`](https://nextjs.org/docs/pages/api-reference/next-config-js/optimizePackageImports) is a feature added in Next 13.5 that improves compilation speed when importing packages that use barrel exports and export many named exports. This replaces the [`modularizeImports`](https://nextjs.org/docs/architecture/nextjs-compiler#modularize-imports) configuration option as it optimizes many of the most popular open source libraries automatically.

Barrel files make the process of exporting code from a package convenient by allowing all the code to be exported from a single file. This makes it easier to import any part of the package into your application. However, since they export a lot of code from the same file, importing these packages can cause tools to do additional work analyzing files that are unused in the application.

For further reading, see:

*   [How we optimized package imports in Next.js](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js)
*   [`optimizePackageImports`](https://nextjs.org/docs/pages/api-reference/next-config-js/optimizePackageImports)

As of Next.js 14.2.3, this configuration option is still experimental. Check the Next.js documentation for the latest information here: [`optimizePackageImports`](https://nextjs.org/docs/pages/api-reference/next-config-js/optimizePackageImports).

## [How to fix](#how-to-fix)

To fix this, you can add a `modularizeImports` config to `next.config.js` for the package that uses barrel files. For example:

next.config.js

```
experimental: {
  optimizePackageImports: ['@vercel/geistcn/components'];
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_REACT_STRICT_MODE"
description: "Applications using Next.js should enable React Strict Mode"
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_REACT_STRICT_MODE"
--------------------------------------------------------------------------------

# NEXTJS\_MISSING\_REACT\_STRICT\_MODE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

We strongly suggest you enable Strict Mode in your Next.js application to better prepare your application for the future of React. See the [Next.js doc on React Strict Mode](https://nextjs.org/docs/api-reference/next.config.js/react-strict-mode) for more information.

## [How to fix](#how-to-fix)

Add the following to your `next.config.js` file.

next.config.js

```
module.exports = {
  reactStrictMode: true,
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_MISSING_SECURITY_HEADERS"
description: "Requires that security headers are set correctly for Next.js apps and contain valid directives."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_MISSING_SECURITY_HEADERS"
--------------------------------------------------------------------------------

# NEXTJS\_MISSING\_SECURITY\_HEADERS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Security headers are important to set to improve the security of your application. Security headers can be set for all routes in \[`next.config.js` files\] ([https://nextjs.org/docs/advanced-features/security-headers](https://nextjs.org/docs/advanced-features/security-headers)). This conformance check requires that the security headers are set and use a valid value.

Required headers:

*   Content-Security-Policy
*   Strict-Transport-Security
*   X-Frame-Options
*   X-Content-Type-Options
*   Referrer-Policy

## [Example](#example)

```
Conformance errors found!
 
A Conformance error occurred in test "NEXTJS_MISSING_SECURITY_HEADERS".
 
The security header "Strict-Transport-Security" is not set correctly. The "includeSubDomains" directive should be used in conjunction with the "preload" directive.
 
To find out more information and how to fix this error, visit
/docs/conformance/rules/NEXTJS_MISSING_SECURITY_HEADERS.
 
If this violation should be ignored, add the following entry to
/apps/docs/.allowlists/NEXTJS_MISSING_SECURITY_HEADERS.allowlist.json
and get approval from the appropriate person.
 
{
  "testName": "NEXTJS_MISSING_SECURITY_HEADERS",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "docs"
  },
  "details": {
    "header": "Strict-Transport-Security"
  }
}
```

## [How to fix](#how-to-fix)

Follow the [Next.js security headers documentation](https://nextjs.org/docs/advanced-features/security-headers) to fix this Conformance test. That document will walk through each of the headers and also links to further documentation to understand what the headers do and how to set the best values for your application.

--------------------------------------------------------------------------------
title: "NEXTJS_NO_ASYNC_LAYOUT"
description: "Ensures that the exported Next.js `layout` component and its transitive dependencies are not asynchronous, as that can block the rendering of the layout and the rest of the page."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_ASYNC_LAYOUT"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_ASYNC\_LAYOUT

Copy page

Ask AI about this page

Last updated June 27, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is in preview, please give us your feedback!

  

This rule is available from version 1.1.0.

This rule examines all Next.js app router layout files and their transitive dependencies to ensure none are asynchronous or return new Promise instances. Even if the layout component itself is not asynchronous, importing an asynchronous component somewhere in the layout's dependency tree can silently cause the layout to render dynamically. This can cause a blank layout to be displayed to the user while Next.js waits for long promises to resolve.

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

For further reading, these resources may be helpful:

*   [Loading UI and Streaming in Next.js](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming): This guide discusses strategies for loading UI components and streaming content in Next.js applications.
*   [Next.js Layout File Conventions](https://nextjs.org/docs/app/api-reference/file-conventions/layout): This document provides an overview of file conventions related to layout in Next.js.
*   [Next.js Parallel Routes](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes): This guide discusses how to use parallel routes to improve performance in Next.js applications.
*   [Next.js Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic): This document provides an overview of the `dynamic` export and how it can be used to force the dynamic behavior of a layout.

## [Examples](#examples)

This rule will catch the following code.

app/layout.tsx

```
export default async function RootLayout() {
  const data = await fetch();
  return <div>{data}</div>;
}
```

app/layout.jsx

```
async function AuthButton() {
  const isAuthorized = await auth();
  return <div>{isAuthorized ? 'Authorized' : 'Unauthorized'}</div>;
}
 
export default function Layout() {
  return <AuthButton />;
}
```

## [How to fix](#how-to-fix)

You can fix this error by wrapping your async component with a `<Suspense/>` boundary that has a fallback UI to indicate to Next.js that it should use the fallback until the promise resolves.

You can also move the asynchronous component to a [parallel route](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) which allows Next.js to render one or more pages within the same layout.

Alternatively, you can manually force the dynamic behavior of the layout by exporting a `dynamic` value. This rule will only error if `dynamic` is not specified or is set to `auto`. Read more [here](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic).

app/layout.tsx

```
export const dynamic = 'force-static';
 
export default async function RootLayout() {
  const data = await fetch();
  return <div>{data}</div>;
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_NO_ASYNC_PAGE"
description: "Ensures that the exported Next.js page component and its transitive dependencies are not asynchronous, as that blocks the rendering of the page."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_ASYNC_PAGE"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_ASYNC\_PAGE

Copy page

Ask AI about this page

Last updated June 27, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is in preview, please give us your feedback!

  

This rule is available from version 1.1.0.

This rule examines all Next.js app router page files and their transitive dependencies to ensure none are asynchronous or return new Promise instances. Even if the page component itself is not asynchronous, importing an asynchronous component somewhere in the page's dependency tree can silently cause the page to render dynamically. This can cause a blank page to be displayed to the user while Next.js waits for long promises to resolve.

This rule will not error if it detects a sibling [loading.js](https://nextjs.org/docs/app/api-reference/file-conventions/loading) file beside the page.

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

For further reading, you may find these resources helpful:

*   [Loading UI and Streaming in Next.js](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming): This guide discusses strategies for loading UI components and streaming content in Next.js applications.
*   [Next.js Loading File Conventions](https://nextjs.org/docs/app/api-reference/file-conventions/loading): This document provides an overview of file conventions related to loading in Next.js.
*   [Next.js Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic): This document provides an overview of the `dynamic` export and how it can be used to force the dynamic behavior of a layout.

## [Examples](#examples)

This rule will catch the following code.

app/page.tsx

```
export default async function Page() {
  const data = await fetch();
  return <div>{data}</div>;
}
```

app/page.jsx

```
async function AuthButton() {
  const isAuthorized = await auth();
  return <div>{isAuthorized ? 'Authorized' : 'Unauthorized'}</div>;
}
 
export default function Page() {
  return <AuthButton />;
}
```

## [How to fix](#how-to-fix)

You can fix this error by wrapping your async component with a `<Suspense/>` boundary that has a fallback UI to indicate to Next.js that it should use the fallback until the promise resolves.

Alternatively, you can manually force the dynamic behavior of the page by exporting a `dynamic` value. This rule will only error if `dynamic` is not specified or is set to `auto`. Read more [here](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic).

app/page.tsx

```
export const dynamic = 'force-static';
 
export default async function Page() {
  const data = await fetch();
  return <div>{data}</div>;
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_NO_BEFORE_INTERACTIVE"
description: "Requires review of usage of the beforeInteractive strategy in Script (next/script) elements."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_BEFORE_INTERACTIVE"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_BEFORE\_INTERACTIVE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

The default [loading strategy](https://nextjs.org/docs/basic-features/script#strategy) for [`next/script`](https://nextjs.org/docs/basic-features/script) is optimised for fast page loads.

Setting the strategy to [`beforeInteractive`](https://nextjs.org/docs/api-reference/next/script#beforeinteractive) forces the script to load before any Next.js code and before hydration occurs, which delays the page from becoming interactive.

For further reading, see:

*   [Loading strategy in Next.js](https://nextjs.org/docs/basic-features/script#strategy)
*   [`next/script` docs](https://nextjs.org/docs/api-reference/next/script#beforeinteractive)
*   [Chrome blog on the Next.js Script component](https://developer.chrome.com/blog/script-component/#the-nextjs-script-component)

## [Examples](#examples)

This rule will catch the following code.

```
import Script from 'next/script';
 
export default function MyPage() {
  return (
    <Script src="https://example.com/script.js" strategy="beforeInteractive" />
  );
}
```

## [How to fix](#how-to-fix)

This rule flags any usage of `beforeInteractive` for review. If approved, the exception should be added to the allowlist.

--------------------------------------------------------------------------------
title: "NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE"
description: "Disallows dependency on client libraries inside of middleware to improve performance of middleware."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_CLIENT_DEPS_IN_MIDDLEWARE"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_CLIENT\_DEPS\_IN\_MIDDLEWARE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check disallows dependencies on client libraries, such as `react` and `next/router` in Next.js middleware. Since middleware runs on the server and runs on every request, this code is not able to run any client side code and it should have a small bundle size to improve loading and execution times.

## [Example](#example)

An example of when this check could manifest is when middleware transitively depends on a file that also uses `react` within the same file.

For example:

experiments.ts

```
import { createContext, type Context } from 'react';
 
export function createExperimentContext(): Context<ExperimentContext> {
  return createContext<ExperimentContext>({
    experiments: () => {
      return EXPERIMENT_DEFAULTS;
    },
  });
}
 
export async function getExperiments() {
  return activeExperiments;
}
```

middleware.ts

```
export async function middleware(
  request: NextRequest,
  event: NextFetchEvent,
): Promise<Response> {
  const experiments = await getExperiments();
 
  if (experiments.includes('new-marketing-page)) {
    return NextResponse.rewrite(MARKETING_PAGE_URL);
  }
  return NextResponse.next();
}
```

In this example, the `experiments.ts` file both fetches the active experiments as well as provides helper functions to use experiments on the client in React.

## [How to fix](#how-to-fix)

Client dependencies used or transitively depended on by middleware files should be refactored to avoid depending on the client libraries. In the example above, the code that is used by middleware to fetch experiments should be moved to a separate file from the code that provides the React functionality.

--------------------------------------------------------------------------------
title: "NEXTJS_NO_DYNAMIC_AUTO"
description: "Prevent usage of force-dynamic as a dynamic page rendering strategy."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_DYNAMIC_AUTO"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_DYNAMIC\_AUTO

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Changing the dynamic behavior of a layout or page using "force-dynamic" is not recommended in App Router. This is because this will force only dynamic rendering of those pages and opt-out "fetch" request from the fetch cache. Furthermore, opting out will also prevent future optimizations such as partially static subtrees and hybrid server-side rendering, which can significantly improve performance.

See [Next.js Segment Config docs](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) for more information on the different migration strategies that can be used and how they work.

## [How to fix](#how-to-fix)

Usage of `force-dynamic` can be avoided and instead `no-store` or `fetch` calls can be used instead. Alternatively, usage of `cookies()` can also avoid the need to use `force-dynamic`.

```
// Example of how to use `no-store` on `fetch` calls.
const data = fetch(someURL, { cache: 'no-store' });
```

--------------------------------------------------------------------------------
title: "NEXTJS_NO_FETCH_IN_SERVER_PROPS"
description: "Prevent relative fetch calls in getServerSideProps from being added to Next.js applications."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_FETCH_IN_SERVER_PROPS"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_FETCH\_IN\_SERVER\_PROPS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Since both `getServerSideProps` and API routes run on the server, calling `fetch` on a non-relative URL will trigger an additional network request.

## [How to fix](#how-to-fix)

Instead of using `fetch` to make a call to the API route, you can instead share the code in a shared library or module to avoid another network request. You can then import this hared logic and call directly within your `getServerSideProps` function, avoiding additional network requests entirely.

--------------------------------------------------------------------------------
title: "NEXTJS_NO_GET_INITIAL_PROPS"
description: "Requires any use of getInitialProps in Next.js pages be reviewed and approved, and encourages using getServerSideProps or getStaticProps instead."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_GET_INITIAL_PROPS"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_GET\_INITIAL\_PROPS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

`getInitialProps` is an older Next.js API for server-side rendering that can usually be replaced with `getServerSideProps` or `getStaticProps` for more performant and secure code.

`getInitialProps` runs on both the server and the client after page load, so the JavaScript bundle will contain any dependencies used by `getInitialProps`. This means that it is possible for unintended code to be included in the client side bundle, for example, code that should only be used on the server such as database connections.

If you need to avoid a server-round trip when performing a client side transition, `getInitialProps` could be used. However, if you do not, `getServerSideProps` is a good API to use instead so that the code remains on the server and does not bloat the JavaScript bundle, or `getStaticProps` can be used if the page can be statically generated at build time.

This rule is for highlighting these concerns and while there are still valid use cases for using `getInitialProps` if you do need to do data fetching on both the client and the server, they should be reviewed and approved.

## [Example](#example)

An example of when this check would fail:

src/pages/index.tsx

```
import { type NextPage } from 'next';
 
const Home: NextPage = ({ users }) => {
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
 
Home.getInitialProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return { stars: json.stargazers_count };
};
 
export default Home;
```

In this example, the `getInitialProps` function is used to fetch data from an API, but it isn't necessary that we fetch the data on both the client and the server so we can fix it below.

## [How to fix](#how-to-fix)

Instead, we should use `getServerSideProps` instead of `getInitialProps`:

src/pages/index.tsx

```
import { type GetServerSideProps } from 'next';
 
const Home = ({ users }) => {
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
 
export getServerSideProps: GetServerSideProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: {
      stars: json.stargazers_count
    },
  };
};
 
export default Home;
```

--------------------------------------------------------------------------------
title: "NEXTJS_NO_PRODUCTION_SOURCE_MAPS"
description: "Applications using Next.js should not enable production source maps so that they don't publicly share source code."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_PRODUCTION_SOURCE_MAPS"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_PRODUCTION\_SOURCE\_MAPS

Copy page

Ask AI about this page

Last updated May 23, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.1.0.

Enabling production source maps in your Next.js application will publicly share your application's source code and should be done with caution. This rule flags any usage of `productionBrowserSourceMaps` for review. If intentional, the exception should be added to an allowlist.

For further reading, see:

*   [`productionBrowserSourceMaps` documentation](https://nextjs.org/docs/app/api-reference/next-config-js/productionBrowserSourceMaps)

## [Examples](#examples)

This rule will catch the following code.

```
module.exports = {
  productionBrowserSourceMaps: true,
};
```

## [How to fix](#how-to-fix)

To fix this issue, either set the value of `productionBrowserSourceMaps` configuration to false, or if intentional add an exception to an allowlist.

## [Considerations](#considerations)

### [Tradeoffs of Disabling Source Maps](#tradeoffs-of-disabling-source-maps)

Disabling source maps in production has the benefit of not exposing your source code publicly, but it also means that errors in production will lack helpful stack traces, complicating the debugging process.

### [Protected Deployments](#protected-deployments)

For [protected deployments](/docs/security/deployment-protection/methods-to-protect-deployments), it is generally safe to enable source maps, as these deployments are only accessible by authorized users who would already have access to your source code. Preview deployments are protected by default, making them a safe environment for enabling source maps.

### [Third-Party Error Tracking Services](#third-party-error-tracking-services)

If you use a third-party error tracking service like [Sentry](https://sentry.io/), you can safely enable source maps by:

1.  Uploading the source maps to your error tracking service
2.  Emptying or deleting the source maps before deploying to production

Many third-party providers like Sentry offer built-in configuration options to automatically delete sourcemaps after uploading them. Check your provider's documentation for these features before implementing a manual solution.

If you need to implement this manually, you can use an approach like this:

```
// Empty the source maps after uploading them to your error tracking service
const sourcemapFiles = await findFiles('.next', /\.js\.map$/);
await Promise.all(
  sourcemapFiles.map(async (file) => {
    await writeFile(file, '', 'utf8');
  }),
);
```

--------------------------------------------------------------------------------
title: "NEXTJS_NO_SELF_HOSTED_VIDEOS"
description: "Prevent video files from being added to Next.js applications."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_SELF_HOSTED_VIDEOS"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_SELF\_HOSTED\_VIDEOS

Copy page

Ask AI about this page

Last updated May 26, 2025

Video files, which are typically large, can consume a lot of bandwidth for your Next.js application. Video files are better served from a dedicated video CDN that is optimized for serving videos.

## [How to fix](#how-to-fix)

Vercel Blob can be used for storing and serving large files such as videos.

You can use either [server uploads or client uploads](/docs/storage/vercel-blob#server-and-client-uploads) depending on the file size:

*   [Server uploads](/docs/storage/vercel-blob/server-upload) are suitable for files up to 4.5 MB
*   [Client uploads](/docs/storage/vercel-blob/client-upload) allow for uploading larger files directly from the browser to Vercel Blob, supporting files up to 5 TB (5,000 GB)

See the [best practices for hosting videos on Vercel](/guides/best-practices-for-hosting-videos-on-vercel-nextjs-mp4-gif) guide to learn more about various other options for hosting videos.

--------------------------------------------------------------------------------
title: "NEXTJS_NO_TURBO_CACHE"
description: "Prevent Turborepo from caching the Next.js .next/cache folder to prevent an oversized cache."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_TURBO_CACHE"
--------------------------------------------------------------------------------

# NEXTJS\_NO\_TURBO\_CACHE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule prevents the `.next/cache` folder from being added to the Turborepo cache. This is important because including the `.next/cache` folder in the Turborepo cache can cause the cache to grow to an excessive size. Vercel also already includes this cache in the build container cache.

## [Examples](#examples)

The following `turbo.json` config will be caught by this rule for Next.js apps:

turbo.json

```
{
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**"]
    }
  }
}
```

## [How to fix](#how-to-fix)

To fix, add `"!.next/cache/**"` to the list of outputs for the task.

turbo.json

```
{
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**"]
    }
  }
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_REQUIRE_EXPLICIT_DYNAMIC"
description: "Requires explicitly setting the `dynamic` route segment option for Next.js pages and routes."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_REQUIRE_EXPLICIT_DYNAMIC"
--------------------------------------------------------------------------------

# NEXTJS\_REQUIRE\_EXPLICIT\_DYNAMIC

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.3.0.

  

This rule conflicts with the experimental Next.js feature [Partial Prerendering (PPR)](https://vercel.com/blog/partial-prerendering-with-next-js-creating-a-new-default-rendering-model). If you enable PPR in your Next.js app, you should not enable this rule.

For convenience, Next.js defaults to automatically selecting the rendering mode for pages and routes.

Whilst this works well, it also means that rendering modes can be changed unintentionally (i.e. through an update to a component that a page depends on). These changes can lead to unexpected behaviors, including performance issues.

To mitigate the chance that rendering modes change unexpectedly, you should explicitly set the `dynamic` route segment option to the desired mode. Note that the default value is `auto`, which will not satisfy this rule.

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

For further reading, see:

*   [Next.js File Conventions: Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic)

## [Examples](#examples)

This rule will catch any pages or routes that:

*   Do not have the `dynamic` option set to a valid value.
*   Have the `dynamic` option set to `'auto'` (which is the default value).

In the following example, the page component does not have the `dynamic` route segment option set.

app/page.tsx

```
export default function Page() {
  // ...
}
```

The next example sets the `dynamic` route segment option, however it sets it to `'auto'`, which is already the default behavior and will not satisfy this rule.

app/dashboard/page.tsx

```
export const dynamic = 'auto';
 
export default function Page() {
  // ...
}
```

## [How to fix](#how-to-fix)

If you see this issue in your codebase, you can resolve it by explicitly setting the `dynamic` route segment option for the page or route.

In this example, the `dynamic` route segment option is set to `error`, which forces the page to static, and will throw an error if any components use [dynamic functions](https://nextjs.org/docs/app/building-your-application/rendering/server-components#server-rendering-strategies#dynamic-functions) or uncached data.

app/page.tsx

```
export const dynamic = 'error';
 
export default function Page() {
  const text = 'Hello world';
  return <div>{text}</div>;
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE"
description: "Usage process.env.NEXT_PUBLIC_* environment variables must be allowlisted."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_NEXT_PUBLIC_ENV_USAGE"
--------------------------------------------------------------------------------

# NEXTJS\_SAFE\_NEXT\_PUBLIC\_ENV\_USAGE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.4.0.

The use of `process.env.NEXT_PUBLIC_*` environment variables may warrant a review from other developers to ensure there are no unintended leakage of environment variables.

When enabled, this rule requires that all usage of `NEXT_PUBLIC_*` must be included in the [allowlist](https://vercel.com/docs/conformance/allowlist).

## [Examples](#examples)

This rule will catch any pages or routes that are using `process.env.NEXT_PUBLIC_*` environment variables.

In the following example, we are using a local variable to initialize our analytics service. As the variable will be visible in the client, a review of the code is required, and the usage should be added to the [allowlist](https://vercel.com/docs/conformance/allowlist).

app/dashboard/page.tsx

```
setupAnalyticsService(process.env.NEXT_PUBLIC_ANALYTICS_ID);
 
function HomePage() {
  return <h1>Hello World</h1>;
}
 
export default HomePage;
```

## [How to fix](#how-to-fix)

If you hit this issue, include the entry in the [Conformance allowlist file](https://vercel.com/docs/conformance/allowlist).

--------------------------------------------------------------------------------
title: "NEXTJS_SAFE_SVG_IMAGES"
description: "Prevent dangerouslyAllowSVG without Content Security Policy in Next.js applications."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_SVG_IMAGES"
--------------------------------------------------------------------------------

# NEXTJS\_SAFE\_SVG\_IMAGES

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

SVG can do many of the same things that HTML/JS/CSS can, meaning that it can be dangerous to execute SVG as this can lead to vulnerabilities without proper [Content Security Policy](https://nextjs.org/docs/advanced-features/security-headers) (CSP) headers.

## [How to fix](#how-to-fix)

If you need to serve SVG images with the default Image Optimization API, you can set `dangerouslyAllowSVG` inside your `next.config.js`:

next.config.js

```
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
};
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.

--------------------------------------------------------------------------------
title: "NEXTJS_SAFE_URL_IMPORTS"
description: "Prevent unsafe URL Imports from being added to Next.js applications."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_SAFE_URL_IMPORTS"
--------------------------------------------------------------------------------

# NEXTJS\_SAFE\_URL\_IMPORTS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

URL imports are an experimental feature that allows you to import modules directly from external servers (instead of from the local disk). When you opt-in, and supply URL prefixes inside `next.config.js`, like so:

next.config.js

```
module.exports = {
  experimental: {
    urlImports: ['https://example.com/assets/', 'https://cdn.skypack.dev'],
  },
};
```

If any of the URLs have not been added to the safe import comformance configuration, then this will cause this rule to fail.

## [How to fix](#how-to-fix)

Engineers should reach out to the appropriate engineer(s) or team(s) for a security review of the URL import configuration.

When requesting a review, please provide as much information as possible around the proposed URL being added, and if there any security implications for using the URL.

If this URL is deemed safe for general use, it can be added to the list of approved URL imports. This can be done by following the [Customizing Conformance](/docs/conformance/customize#configuring-a-conformance-rule) docs to add the URL to your `conformance.config.jsonc` file:

conformance.config.jsonc

```
"NEXTJS_SAFE_URL_IMPORTS": {
  urlImports: [theUrlToAdd],
}
```

--------------------------------------------------------------------------------
title: "NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS"
description: "Catches usages of getServerSideProps that could use static rendering instead, improving the performance of those pages."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS"
--------------------------------------------------------------------------------

# NEXTJS\_UNNEEDED\_GET\_SERVER\_SIDE\_PROPS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule will analyze each Next.js page's `getServerSideProps` to see if the context parameter is being used and if not then it will fail.

When using `getServerSideProps` to render a Next.js page on the server, if the page doesn't require any information from the request, consider using [SSG](https://nextjs.org/docs/basic-features/data-fetching/get-static-props) with `getStaticProps`. If you are using `getServerSideProps` to refresh the data on each page load, consider using [ISR](https://nextjs.org/docs/basic-features/data-fetching/incremental-static-regeneration) instead with a `revalidate` property to control how often the page is regenerated. If you are using `getServerSideProps` to randomize the data on each page load, consider moving that logic to the client instead and use `getStaticProps` to reuse the statically generated page.

## [Example](#example)

An example of when this check would fail:

src/pages/index.tsx

```
import { type GetServerSideProps } from 'next';
 
export const getServerSideProps: GetServerSideProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: { stargazersCount: json.stargazers_count },
  };
};
 
function Home({ stargazersCount }) {
  return <h1>The Next.js repo has {stargazersCount} stars.</h1>;
}
 
export default Home;
```

In this example, the `getServerSideProps` function is used to pass data from an API to the page, but it isn't using any information from the context argument so `getServerSideProps` is unnecessary.

## [How to fix](#how-to-fix)

Instead, we can convert the page to use [SSG](https://nextjs.org/docs/basic-features/data-fetching/get-static-props) with `getStaticProps`. This will generate the page at build time and serve it statically. If you need the page to be updated more frequently, then you can also use [ISR](https://nextjs.org/docs/basic-features/data-fetching/incremental-static-regeneration) with the revalidate option:

src/pages/index.tsx

```
import { type GetStaticProps } from 'next';
 
export const getStaticProps: GetStaticProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: { stargazersCount: json.stargazers_count },
    revalidate: 60, // Using ISR, regenerate the page every 60 seconds
  };
};
 
function Home({ stargazersCount }) {
  return <h1>The Next.js repo has {stargazersCount} stars.</h1>;
}
 
export default Home;
```

Or, you can use information from the context argument to customize the page:

src/pages/index.tsx

```
import { type GetServerSideProps } from 'next';
 
export const getServerSideProps: GetServerSideProps = async (context) => {
  const res = await fetch(
    `https://api.github.com/repos/vercel/${context.query.repoName}`,
  );
  const json = await res.json();
  return {
    props: {
      repoName: context.query.repoName,
      stargazersCount: json.stargazers_count,
    },
  };
};
 
function Home({ repoName, stargazersCount }) {
  return (
    <h1>
      The {repoName} repo has {stargazersCount} stars.
    </h1>
  );
}
 
export default Home;
```

--------------------------------------------------------------------------------
title: "NEXTJS_USE_NATIVE_FETCH"
description: "Requires using native `fetch` which Next.js provides, removing the need for third-party fetch libraries."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_USE_NATIVE_FETCH"
--------------------------------------------------------------------------------

# NEXTJS\_USE\_NATIVE\_FETCH

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.1.0.

Next.js extends the native [Web `fetch` API](https://nextjs.org/docs/app/api-reference/functions/fetch) with additional caching capabilities which means third-party fetch libraries are not needed. Including these libraries in your app can increase bundle size and negatively impact performance.

This rule will detect any usage of the following third-party fetch libraries:

*   `isomorphic-fetch`
*   `whatwg-fetch`
*   `node-fetch`
*   `cross-fetch`
*   `axios`

If there are more libraries you would like to restrict, consider using a [custom rule](https://vercel.com/docs/conformance/custom-rules).

By default, this rule is disabled. You can enable it by [customizing Conformance](/docs/conformance/customize).

For further reading, see:

*   [https://nextjs.org/docs/app/api-reference/functions/fetch](https://nextjs.org/docs/app/api-reference/functions/fetch)
*   [https://developer.mozilla.org/en-US/docs/Web/API/Fetch\_API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

## [Examples](#examples)

This rule will catch the following code.

```
import fetch from 'isomorphic-fetch';
 
export async function getAuth() {
  const auth = await fetch('/api/auth');
  return auth.json();
}
```

## [How to fix](#how-to-fix)

Replace the third-party fetch library with the native `fetch` API Next.js provides.

--------------------------------------------------------------------------------
title: "NEXTJS_USE_NEXT_FONT"
description: "Requires using next/font to load local fonts and fonts from supported CDNs."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_FONT"
--------------------------------------------------------------------------------

# NEXTJS\_USE\_NEXT\_FONT

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.1.0.

[`next/font`](https://nextjs.org/docs/pages/api-reference/components/font) automatically optimizes fonts and removes external network requests for improved privacy and performance.

By default, this rule is disabled. Enable it by [customizing Conformance](/docs/conformance/customize).

This means you can optimally load web fonts with zero layout shift, thanks to the underlying CSS size-adjust property used.

For further reading, see:

*   [https://nextjs.org/docs/basic-features/font-optimization](https://nextjs.org/docs/basic-features/font-optimization)
*   [https://nextjs.org/docs/pages/api-reference/components/font](https://nextjs.org/docs/pages/api-reference/components/font)
*   [https://www.lydiahallie.io/blog/optimizing-webfonts-in-nextjs-13](https://www.lydiahallie.io/blog/optimizing-webfonts-in-nextjs-13)

## [Examples](#examples)

This rule will catch the following code.

```
@font-face {
  font-family: Foo;
  src:
    url(https://fonts.gstatic.com/s/roboto/v30/KFOiCnqEu92Fr1Mu51QrEz0dL-vwnYh2eg.woff2)
      format('woff2'),
    url(/custom-font.ttf) format('truetype');
  font-display: block;
  font-style: normal;
  font-weight: 400;
}
```

```
function App() {
  return (
    <link
      href="https://fonts.googleapis.com/css2?family=Krona+One&display=optional"
      rel="stylesheet"
    />
  );
}
```

## [How to fix](#how-to-fix)

Replace any `@font-face` at-rules and `link` elements that are caught by this rule with [`next/font`](https://nextjs.org/docs/api-reference/next/font).

--------------------------------------------------------------------------------
title: "NEXTJS_USE_NEXT_IMAGE"
description: "Requires that next/image is used for all images."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_IMAGE"
--------------------------------------------------------------------------------

# NEXTJS\_USE\_NEXT\_IMAGE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.1.0.

The Next.js Image component ([`next/image`](https://nextjs.org/docs/pages/api-reference/components/image)) extends the HTML `<img>` element with features for automatic image optimization.

It optimizes image sizes for different devices using modern image formats, improves visual stability by preventing layout shifts during image loading, and speeds up page loads with lazy loading and optional blur-up placeholders.

Additionally, it provides the flexibility of on-demand image resizing, even for images hosted on remote servers. This may incur costs from your managed hosting provider (see [below](#important-note-on-costs) for more information)

By default, this rule is disabled. Enable it by [customizing Conformance](/docs/conformance/customize).

For further reading, see:

*   [https://nextjs.org/docs/app/building-your-application/optimizing/images](https://nextjs.org/docs/app/building-your-application/optimizing/images)
*   [https://nextjs.org/docs/pages/api-reference/components/image](https://nextjs.org/docs/pages/api-reference/components/image)

## [Important note on costs](#important-note-on-costs)

Using image optimization may incur costs from your managed hosting provider. You can opt out of image optimization by setting the optional [`unoptimized` prop](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized).

Please check with your hosting provider for details.

*   [Vercel pricing](https://vercel.com/pricing)
*   [Cloudinary pricing](https://cloudinary.com/pricing)
*   [imgix pricing](https://imgix.com/pricing)

## [Important note on self-hosting](#important-note-on-self-hosting)

If self-hosting, you'll need to install the optional package [`sharp`](https://www.npmjs.com/package/sharp), which Next.js will use to optimize images. Optimized images will require more available storage on your server.

## [Examples](#examples)

This rule will catch the following code.

```
function App() {
  return <img src="/media/image.png" alt="Example" />;
}
```

The following code will not be caught by this rule.

```
function App() {
  return (
    <picture>
      <source srcSet="/hero.avif" type="image/avif" />
      <source srcSet="/hero.webp" type="image/webp" />
      <img src="/hero.jpg" alt="Landscape picture" width={800} height={500} />
    </picture>
  );
}
```

## [How to fix](#how-to-fix)

Replace any `<img>` elements that are caught by this rule with [`next/image`](https://nextjs.org/docs/pages/api-reference/components/image).

Again, please check with your managed hosting provider for image optimization costs.

--------------------------------------------------------------------------------
title: "NEXTJS_USE_NEXT_SCRIPT"
description: "Requires that next/script is used for all scripts."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_USE_NEXT_SCRIPT"
--------------------------------------------------------------------------------

# NEXTJS\_USE\_NEXT\_SCRIPT

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.1.0.

[`next/script`](https://nextjs.org/docs/pages/api-reference/components/script) automatically optimizes scripts for improved performance through customizable loading strategies. By default, `next/script` loads scripts so that they're non-blocking, meaning that they load after the page has loaded.

Additionally, `next/script` has built in event handlers for common events such as `onLoad` and `onError`.

By default, this rule is disabled. Enable it by [customizing Conformance](/docs/conformance/customize).

For further reading, see:

*   [https://nextjs.org/docs/pages/building-your-application/optimizing/scripts](https://nextjs.org/docs/pages/building-your-application/optimizing/scripts)
*   [https://nextjs.org/docs/pages/api-reference/components/script](https://nextjs.org/docs/pages/api-reference/components/script)

## [Examples](#examples)

This rule will catch the following code.

```
function insertScript() {
  const script = document.createElement('script');
  script.src = process.env.SCRIPT_PATH;
  document.body.appendChild(script);
}
```

```
function App() {
  return (
    <script
      dangerouslySetInnerHTML={{ __html: "console.log('Hello world');" }}
    />
  );
}
```

## [How to fix](#how-to-fix)

Replace any `document.createElement('script')` calls and `<script>` elements that are caught by this rule with [`next/script`](https://nextjs.org/docs/pages/api-reference/components/script).

--------------------------------------------------------------------------------
title: "NO_ASSIGN_WINDOW_LOCATION"
description: "Prevent unsafe assignment to window.location.href in your application."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_ASSIGN_WINDOW_LOCATION"
--------------------------------------------------------------------------------

# NO\_ASSIGN\_WINDOW\_LOCATION

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Direct assignments to "window.location.href" or "window.location" should be avoided due to possible XSS attacks that can occur from lack of sanitization of input to the "href".

## [How to fix](#how-to-fix)

The recommended approach for Next.js applications is to use a custom `redirectTo` function. This provides a clear way to use `router.push()` or `window.location.href` to provide an experience that is best for the user (client-side navigation only, or a full page refresh). Here's an example of how you might do this using Next.js:

Before:

my-site.js

```
windows.location.href = '/login';
```

After:

my-site.js

```
router.push('/login');
```

--------------------------------------------------------------------------------
title: "NO_CORS_HEADERS"
description: "Warns when CORS header (or header-like) configuration is detected, requiring that configuration to be allowlisted."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_CORS_HEADERS"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./03-build-output-configuration.md) | [Index](./index.md) | [Next →](./05-no-cors-headers.md)
