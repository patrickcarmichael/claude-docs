---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

**Authentication Errors**

* Ensure your Microsoft account has the necessary permissions for Teams access.
* Required scopes include: `Team.ReadBasic.All`, `Channel.ReadBasic.All`, `ChannelMessage.Send`, `ChannelMessage.Read.All`, `OnlineMeetings.ReadWrite`, `OnlineMeetings.Read`.
* Verify that the OAuth connection includes all required scopes.

**Team and Channel Access**

* Ensure you are a member of the teams you're trying to access.
* Double-check team IDs and channel IDs for correctness.
* Team and channel IDs can be obtained using the `get_teams` and `get_channels` actions.

**Message Sending Issues**

* Ensure `team_id`, `channel_id`, and `message` are provided for `send_message`.
* Verify that you have permissions to send messages to the specified channel.
* Choose appropriate `content_type` (text or html) based on your message format.

**Meeting Creation**

* Ensure `subject`, `startDateTime`, and `endDateTime` are provided.
* Use proper ISO 8601 format with timezone for datetime fields (e.g., '2024-01-20T10:00:00-08:00').
* Verify that the meeting times are in the future.

**Message Retrieval Limitations**

* The `get_messages` action can retrieve a maximum of 50 messages per request.
* Messages are returned in reverse chronological order (newest first).

**Meeting Search**

* For `search_online_meetings_by_join_url`, ensure the join URL is exact and properly formatted.
* The URL should be the complete Teams meeting join URL.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Microsoft Teams integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a meeting](./1864-task-to-create-a-meeting.md)

**Next:** [Microsoft Word Integration →](./1866-microsoft-word-integration.md)
