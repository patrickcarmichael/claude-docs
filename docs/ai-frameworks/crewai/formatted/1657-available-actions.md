---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="gmail/fetch_emails">
    **Description:** Retrieve a list of messages.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `q` (string, optional): Search query to filter messages (e.g., 'from:[someone@example.com](mailto:someone@example.com) is:unread').
    * `maxResults` (integer, optional): Maximum number of messages to return (1-500). (default: 100)
    * `pageToken` (string, optional): Page token to retrieve a specific page of results.
    * `labelIds` (array, optional): Only return messages with labels that match all of the specified label IDs.
    * `includeSpamTrash` (boolean, optional): Include messages from SPAM and TRASH in the results. (default: false)
  </Accordion>

  <Accordion title="gmail/send_email">
    **Description:** Send an email.

    **Parameters:**

    * `to` (string, required): Recipient email address.
    * `subject` (string, required): Email subject line.
    * `body` (string, required): Email message content.
    * `userId` (string, optional): The user's email address or 'me' for the authenticated user. (default: "me")
    * `cc` (string, optional): CC email addresses (comma-separated).
    * `bcc` (string, optional): BCC email addresses (comma-separated).
    * `from` (string, optional): Sender email address (if different from authenticated user).
    * `replyTo` (string, optional): Reply-to email address.
    * `threadId` (string, optional): Thread ID if replying to an existing conversation.
  </Accordion>

  <Accordion title="gmail/delete_email">
    **Description:** Delete an email by ID.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user.
    * `id` (string, required): The ID of the message to delete.
  </Accordion>

  <Accordion title="gmail/create_draft">
    **Description:** Create a new draft email.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user.
    * `message` (object, required): Message object containing the draft content.
      * `raw` (string, required): Base64url encoded email message.
  </Accordion>

  <Accordion title="gmail/get_message">
    **Description:** Retrieve a specific message by ID.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the message to retrieve.
    * `format` (string, optional): The format to return the message in. Options: "full", "metadata", "minimal", "raw". (default: "full")
    * `metadataHeaders` (array, optional): When given and format is METADATA, only include headers specified.
  </Accordion>

  <Accordion title="gmail/get_attachment">
    **Description:** Retrieve a message attachment.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `messageId` (string, required): The ID of the message containing the attachment.
    * `id` (string, required): The ID of the attachment to retrieve.
  </Accordion>

  <Accordion title="gmail/fetch_thread">
    **Description:** Retrieve a specific email thread by ID.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to retrieve.
    * `format` (string, optional): The format to return the messages in. Options: "full", "metadata", "minimal". (default: "full")
    * `metadataHeaders` (array, optional): When given and format is METADATA, only include headers specified.
  </Accordion>

  <Accordion title="gmail/modify_thread">
    **Description:** Modify the labels applied to a thread.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to modify.
    * `addLabelIds` (array, optional): A list of IDs of labels to add to this thread.
    * `removeLabelIds` (array, optional): A list of IDs of labels to remove from this thread.
  </Accordion>

  <Accordion title="gmail/trash_thread">
    **Description:** Move a thread to the trash.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to trash.
  </Accordion>

  <Accordion title="gmail/untrash_thread">
    **Description:** Remove a thread from the trash.

    **Parameters:**

    * `userId` (string, required): The user's email address or 'me' for the authenticated user. (default: "me")
    * `id` (string, required): The ID of the thread to untrash.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Gmail Integration](./1656-setting-up-gmail-integration.md)

**Next:** [Usage Examples →](./1658-usage-examples.md)
