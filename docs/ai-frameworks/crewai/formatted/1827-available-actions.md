---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="microsoft_outlook/get_messages">
    **Description:** Get email messages from the user's mailbox.

    **Parameters:**

    * `top` (integer, optional): Number of messages to retrieve (max 1000). Default is `10`.
    * `filter` (string, optional): OData filter expression (e.g., "isRead eq false").
    * `search` (string, optional): Search query string.
    * `orderby` (string, optional): Order by field (e.g., "receivedDateTime desc"). Default is "receivedDateTime desc".
    * `select` (string, optional): Select specific properties to return.
    * `expand` (string, optional): Expand related resources inline.
  </Accordion>

  <Accordion title="microsoft_outlook/send_email">
    **Description:** Send an email message.

    **Parameters:**

    * `to_recipients` (array, required): Array of recipient email addresses.
    * `cc_recipients` (array, optional): Array of CC recipient email addresses.
    * `bcc_recipients` (array, optional): Array of BCC recipient email addresses.
    * `subject` (string, required): Email subject.
    * `body` (string, required): Email body content.
    * `body_type` (string, optional): Body content type. Enum: `Text`, `HTML`. Default is `HTML`.
    * `importance` (string, optional): Message importance level. Enum: `low`, `normal`, `high`. Default is `normal`.
    * `reply_to` (array, optional): Array of reply-to email addresses.
    * `save_to_sent_items` (boolean, optional): Whether to save the message to Sent Items folder. Default is `true`.
  </Accordion>

  <Accordion title="microsoft_outlook/get_calendar_events">
    **Description:** Get calendar events from the user's calendar.

    **Parameters:**

    * `top` (integer, optional): Number of events to retrieve (max 1000). Default is `10`.
    * `skip` (integer, optional): Number of events to skip. Default is `0`.
    * `filter` (string, optional): OData filter expression (e.g., "start/dateTime ge '2024-01-01T00:00:00Z'").
    * `orderby` (string, optional): Order by field (e.g., "start/dateTime asc"). Default is "start/dateTime asc".
  </Accordion>

  <Accordion title="microsoft_outlook/create_calendar_event">
    **Description:** Create a new calendar event.

    **Parameters:**

    * `subject` (string, required): Event subject/title.
    * `body` (string, optional): Event body/description.
    * `start_datetime` (string, required): Start date and time in ISO 8601 format (e.g., '2024-01-20T10:00:00').
    * `end_datetime` (string, required): End date and time in ISO 8601 format.
    * `timezone` (string, optional): Time zone (e.g., 'Pacific Standard Time'). Default is `UTC`.
    * `location` (string, optional): Event location.
    * `attendees` (array, optional): Array of attendee email addresses.
  </Accordion>

  <Accordion title="microsoft_outlook/get_contacts">
    **Description:** Get contacts from the user's address book.

    **Parameters:**

    * `top` (integer, optional): Number of contacts to retrieve (max 1000). Default is `10`.
    * `skip` (integer, optional): Number of contacts to skip. Default is `0`.
    * `filter` (string, optional): OData filter expression.
    * `orderby` (string, optional): Order by field (e.g., "displayName asc"). Default is "displayName asc".
  </Accordion>

  <Accordion title="microsoft_outlook/create_contact">
    **Description:** Create a new contact in the user's address book.

    **Parameters:**

    * `displayName` (string, required): Contact's display name.
    * `givenName` (string, optional): Contact's first name.
    * `surname` (string, optional): Contact's last name.
    * `emailAddresses` (array, optional): Array of email addresses. Each item is an object with `address` (string) and `name` (string).
    * `businessPhones` (array, optional): Array of business phone numbers.
    * `homePhones` (array, optional): Array of home phone numbers.
    * `jobTitle` (string, optional): Contact's job title.
    * `companyName` (string, optional): Contact's company name.
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Microsoft Outlook Integration](./1826-setting-up-microsoft-outlook-integration.md)

**Next:** [Usage Examples →](./1828-usage-examples.md)
