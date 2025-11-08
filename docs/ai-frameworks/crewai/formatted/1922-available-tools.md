---
title: "Crewai: Available Tools"
description: "Available Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Tools


### **User Management**

<AccordionGroup>
  <Accordion title="slack/list_members">
    **Description:** List all members in a Slack channel.

    **Parameters:**

    * No parameters required - retrieves all channel members
  </Accordion>

  <Accordion title="slack/get_user_by_email">
    **Description:** Find a user in your Slack workspace by their email address.

    **Parameters:**

    * `email` (string, required): The email address of a user in the workspace
  </Accordion>

  <Accordion title="slack/get_users_by_name">
    **Description:** Search for users by their name or display name.

    **Parameters:**

    * `name` (string, required): User's real name to search for
    * `displayName` (string, required): User's display name to search for
    * `paginationParameters` (object, optional): Pagination settings
      * `pageCursor` (string, optional): Page cursor for pagination
  </Accordion>
</AccordionGroup>

### **Channel Management**

<AccordionGroup>
  <Accordion title="slack/list_channels">
    **Description:** List all channels in your Slack workspace.

    **Parameters:**

    * No parameters required - retrieves all accessible channels
  </Accordion>
</AccordionGroup>

### **Messaging**

<AccordionGroup>
  <Accordion title="slack/send_message">
    **Description:** Send a message to a Slack channel.

    **Parameters:**

    * `channel` (string, required): Channel name or ID - Use Connect Portal Workflow Settings to allow users to select a channel, or enter a channel name to create a new channel
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>

  <Accordion title="slack/send_direct_message">
    **Description:** Send a direct message to a specific user in Slack.

    **Parameters:**

    * `memberId` (string, required): Recipient user ID - Use Connect Portal Workflow Settings to allow users to select a workspace member
    * `message` (string, required): The message text to send
    * `botName` (string, required): The name of the bot that sends this message
    * `botIcon` (string, required): Bot icon - Can be either an image URL or an emoji (e.g., ":dog:")
    * `blocks` (object, optional): Slack Block Kit JSON for rich message formatting with attachments and interactive elements
    * `authenticatedUser` (boolean, optional): If true, message appears to come from your authenticated Slack user instead of the application (defaults to false)
  </Accordion>
</AccordionGroup>

### **Search & Discovery**

<AccordionGroup>
  <Accordion title="slack/search_messages">
    **Description:** Search for messages across your Slack workspace.

    **Parameters:**

    * `query` (string, required): Search query using Slack search syntax to find messages that match specified criteria

    **Search Query Examples:**

    * `"project update"` - Search for messages containing "project update"
    * `from:@john in:#general` - Search for messages from John in the #general channel
    * `has:link after:2023-01-01` - Search for messages with links after January 1, 2023
    * `in:@channel before:yesterday` - Search for messages in a specific channel before yesterday
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Slack Integration](./1921-setting-up-slack-integration.md)

**Next:** [Block Kit Integration →](./1923-block-kit-integration.md)
