---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="github/create_issue">
    **Description:** Create an issue in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `title` (string, required): Issue Title - Specify the title of the issue to create.
    * `body` (string, optional): Issue Body - Specify the body contents of the issue to create.
    * `assignees` (string, optional): Assignees - Specify the assignee(s)' GitHub login as an array of strings for this issue. (example: `["octocat"]`).
  </Accordion>

  <Accordion title="github/update_issue">
    **Description:** Update an issue in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `issue_number` (string, required): Issue Number - Specify the number of the issue to update.
    * `title` (string, required): Issue Title - Specify the title of the issue to update.
    * `body` (string, optional): Issue Body - Specify the body contents of the issue to update.
    * `assignees` (string, optional): Assignees - Specify the assignee(s)' GitHub login as an array of strings for this issue. (example: `["octocat"]`).
    * `state` (string, optional): State - Specify the updated state of the issue.
      * Options: `open`, `closed`
  </Accordion>

  <Accordion title="github/get_issue_by_number">
    **Description:** Get an issue by number in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `issue_number` (string, required): Issue Number - Specify the number of the issue to fetch.
  </Accordion>

  <Accordion title="github/lock_issue">
    **Description:** Lock an issue in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `issue_number` (string, required): Issue Number - Specify the number of the issue to lock.
    * `lock_reason` (string, required): Lock Reason - Specify a reason for locking the issue or pull request conversation.
      * Options: `off-topic`, `too heated`, `resolved`, `spam`
  </Accordion>

  <Accordion title="github/search_issue">
    **Description:** Search for issues in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Issue. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Issue.
    * `filter` (object, required): A filter in disjunctive normal form - OR of AND groups of single conditions.
      ```json  theme={null}
      {
        "operator": "OR",
        "conditions": [
          {
            "operator": "AND",
            "conditions": [
              {
                "field": "assignee",
                "operator": "$stringExactlyMatches",
                "value": "octocat"
              }
            ]
          }
        ]
      }
      ```
      Available fields: `assignee`, `creator`, `mentioned`, `labels`
  </Accordion>

  <Accordion title="github/create_release">
    **Description:** Create a release in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `tag_name` (string, required): Name - Specify the name of the release tag to be created. (example: "v1.0.0").
    * `target_commitish` (string, optional): Target - Specify the target of the release. This can either be a branch name or a commit SHA. Defaults to the main branch. (example: "master").
    * `body` (string, optional): Body - Specify a description for this release.
    * `draft` (string, optional): Draft - Specify whether the created release should be a draft (unpublished) release.
      * Options: `true`, `false`
    * `prerelease` (string, optional): Prerelease - Specify whether the created release should be a prerelease.
      * Options: `true`, `false`
    * `discussion_category_name` (string, optional): Discussion Category Name - If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository.
    * `generate_release_notes` (string, optional): Release Notes - Specify whether the created release should automatically create release notes using the provided name and body specified.
      * Options: `true`, `false`
  </Accordion>

  <Accordion title="github/update_release">
    **Description:** Update a release in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `id` (string, required): Release ID - Specify the ID of the release to update.
    * `tag_name` (string, optional): Name - Specify the name of the release tag to be updated. (example: "v1.0.0").
    * `target_commitish` (string, optional): Target - Specify the target of the release. This can either be a branch name or a commit SHA. Defaults to the main branch. (example: "master").
    * `body` (string, optional): Body - Specify a description for this release.
    * `draft` (string, optional): Draft - Specify whether the created release should be a draft (unpublished) release.
      * Options: `true`, `false`
    * `prerelease` (string, optional): Prerelease - Specify whether the created release should be a prerelease.
      * Options: `true`, `false`
    * `discussion_category_name` (string, optional): Discussion Category Name - If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository.
    * `generate_release_notes` (string, optional): Release Notes - Specify whether the created release should automatically create release notes using the provided name and body specified.
      * Options: `true`, `false`
  </Accordion>

  <Accordion title="github/get_release_by_id">
    **Description:** Get a release by ID in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `id` (string, required): Release ID - Specify the release ID of the release to fetch.
  </Accordion>

  <Accordion title="github/get_release_by_tag_name">
    **Description:** Get a release by tag name in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `tag_name` (string, required): Name - Specify the tag of the release to fetch. (example: "v1.0.0").
  </Accordion>

  <Accordion title="github/delete_release">
    **Description:** Delete a release in GitHub.

    **Parameters:**

    * `owner` (string, required): Owner - Specify the name of the account owner of the associated repository for this Release. (example: "abc").
    * `repo` (string, required): Repository - Specify the name of the associated repository for this Release.
    * `id` (string, required): Release ID - Specify the ID of the release to delete.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up GitHub Integration](./1644-setting-up-github-integration.md)

**Next:** [Usage Examples →](./1646-usage-examples.md)
