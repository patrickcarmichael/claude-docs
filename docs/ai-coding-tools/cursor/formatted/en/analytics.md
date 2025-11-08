---
title: "Analytics"
source: "https://docs.cursor.com/en/account/teams/analytics"
language: "en"
language_name: "English"
---

# Analytics
Source: https://docs.cursor.com/en/account/teams/analytics

Track team usage and activity metrics

Team admins can track metrics from the [dashboard](/en/account/teams/dashboard).

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

### Total Usage

View aggregate metrics across your team, including total tabs and premium requests. For teams under 30 days old, metrics reflect usage since creation, including team members' pre-join activity.

### Per Active User

See average metrics per active user: tabs accepted, lines of code, and premium requests.

### User Activity

Track weekly and monthly active users.

## Analytics Report Headers

When you export analytics data from the dashboard, the report includes detailed metrics about user behavior and feature usage. Here's what each header means:

### User Information

<ResponseField name="Date" type="ISO 8601 timestamp">
  The date when the analytics data was recorded (e.g., 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Unique identifier for each user in the system
</ResponseField>

<ResponseField name="Email" type="string">
  User's email address associated with their account
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Indicates if the user was active on this date
</ResponseField>

### AI-Generated Code Metrics

<ResponseField name="Chat Suggested Lines Added" type="number">
  Total lines of code suggested by the AI chat feature
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  Total lines of code suggested for deletion by the AI chat
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  AI-suggested lines that the user accepted and added to their code
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  AI-suggested deletions that the user accepted
</ResponseField>

### Feature Usage Metrics

<ResponseField name="Chat Total Applies" type="number">
  Times a user applied AI-generated changes from chat
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Times a user accepted AI suggestions
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Times a user rejected AI suggestions
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  Times AI suggestion tabs were displayed to the user
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  AI suggestion tabs that were accepted by the user
</ResponseField>

### Request Type Metrics

<ResponseField name="Edit Requests" type="number">
  Requests made through the composer/edit feature (Cmd+K inline edits)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Chat requests where users asked questions to the AI
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  Requests made to AI agents (specialized AI assistants)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Times the Cmd+K (or Ctrl+K) command palette was used
</ResponseField>

### Subscription and API Metrics

<ResponseField name="Subscription Included Reqs" type="number">
  AI requests covered under the user's subscription plan
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Requests made using API keys for programmatic access
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Requests that count toward usage-based billing
</ResponseField>

### Additional Features

<ResponseField name="Bugbot Usages" type="number">
  Times the bug detection/fixing AI feature was used
</ResponseField>

### Configuration Information

<ResponseField name="Most Used Model" type="string">
  The AI model that the user used most frequently (e.g., GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  File extension most commonly used when applying AI suggestions (e.g., .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  File extension most commonly used with tab completion features
</ResponseField>

<ResponseField name="Client Version" type="string">
  Version of the Cursor editor being used
</ResponseField>

### Calculated Metrics

The report also includes processed data that helps understand AI code contribution:

* **Total Lines Added/Deleted**: Raw count of all code changes
* **Accepted Lines Added/Deleted**: Lines that originated from AI suggestions and were accepted
* **Composer Requests**: Requests made through the inline composer feature
* **Chat Requests**: Requests made through the chat interface

<Note>
  All numeric values default to 0 if not present, boolean values default to
  false, and string values default to empty strings. Metrics are aggregated at
  the daily level per user.
</Note>

---

← Previous: [AI Code Tracking API](./ai-code-tracking-api.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →