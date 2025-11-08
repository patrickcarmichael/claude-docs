---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="notion/list_users">
    **Description:** List all users in the workspace.

    **Parameters:**

    * `page_size` (integer, optional): Number of items returned in the response. Minimum: 1, Maximum: 100, Default: 100
    * `start_cursor` (string, optional): Cursor for pagination. Return results after this cursor.
  </Accordion>

  <Accordion title="notion/get_user">
    **Description:** Retrieve a specific user by ID.

    **Parameters:**

    * `user_id` (string, required): The ID of the user to retrieve.
  </Accordion>

  <Accordion title="notion/create_comment">
    **Description:** Create a comment on a page or discussion.

    **Parameters:**

    * `parent` (object, required): The parent page or discussion to comment on.
      ```json  theme={null}
      {
        "type": "page_id",
        "page_id": "PAGE_ID_HERE"
      }
      ```
      or
      ```json  theme={null}
      {
        "type": "discussion_id",
        "discussion_id": "DISCUSSION_ID_HERE"
      }
      ```
    * `rich_text` (array, required): The rich text content of the comment.
      ```json  theme={null}
      [
        {
          "type": "text",
          "text": {
            "content": "This is my comment text"
          }
        }
      ]
      ```
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Notion Integration](./1883-setting-up-notion-integration.md)

**Next:** [Usage Examples →](./1885-usage-examples.md)
