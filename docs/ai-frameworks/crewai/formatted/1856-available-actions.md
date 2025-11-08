---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="microsoft_teams/get_teams">
    **Description:** Get all teams the user is a member of.

    **Parameters:**

    * No parameters required.
  </Accordion>

  <Accordion title="microsoft_teams/get_channels">
    **Description:** Get channels in a specific team.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
  </Accordion>

  <Accordion title="microsoft_teams/send_message">
    **Description:** Send a message to a Teams channel.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `message` (string, required): The message content.
    * `content_type` (string, optional): Content type (html or text). Enum: `html`, `text`. Default is `text`.
  </Accordion>

  <Accordion title="microsoft_teams/get_messages">
    **Description:** Get messages from a Teams channel.

    **Parameters:**

    * `team_id` (string, required): The ID of the team.
    * `channel_id` (string, required): The ID of the channel.
    * `top` (integer, optional): Number of messages to retrieve (max 50). Default is `20`.
  </Accordion>

  <Accordion title="microsoft_teams/create_meeting">
    **Description:** Create a Teams meeting.

    **Parameters:**

    * `subject` (string, required): Meeting subject/title.
    * `startDateTime` (string, required): Meeting start time (ISO 8601 format with timezone).
    * `endDateTime` (string, required): Meeting end time (ISO 8601 format with timezone).
  </Accordion>

  <Accordion title="microsoft_teams/search_online_meetings_by_join_url">
    **Description:** Search online meetings by Join Web URL.

    **Parameters:**

    * `join_web_url` (string, required): The join web URL of the meeting to search for.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Microsoft Teams Integration](./1855-setting-up-microsoft-teams-integration.md)

**Next:** [Usage Examples →](./1857-usage-examples.md)
