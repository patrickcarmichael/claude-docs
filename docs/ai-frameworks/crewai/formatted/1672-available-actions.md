---
title: "Crewai: Available Actions"
description: "Available Actions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Actions


<AccordionGroup>
  <Accordion title="google_calendar/get_availability">
    **Description:** Get calendar availability (free/busy information).

    **Parameters:**

    * `timeMin` (string, required): Start time (RFC3339 format)
    * `timeMax` (string, required): End time (RFC3339 format)
    * `items` (array, required): Calendar IDs to check
      ```json  theme={null}
      [
        {
          "id": "calendar_id"
        }
      ]
      ```
    * `timeZone` (string, optional): Time zone used in the response. The default is UTC.
    * `groupExpansionMax` (integer, optional): Maximal number of calendar identifiers to be provided for a single group. Maximum: 100
    * `calendarExpansionMax` (integer, optional): Maximal number of calendars for which FreeBusy information is to be provided. Maximum: 50
  </Accordion>

  <Accordion title="google_calendar/create_event">
    **Description:** Create a new event in the specified calendar.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `summary` (string, required): Event title/summary
    * `start_dateTime` (string, required): Start time in RFC3339 format (e.g., 2024-01-20T10:00:00-07:00)
    * `end_dateTime` (string, required): End time in RFC3339 format
    * `description` (string, optional): Event description
    * `timeZone` (string, optional): Time zone (e.g., America/Los\_Angeles)
    * `location` (string, optional): Geographic location of the event as free-form text.
    * `attendees` (array, optional): List of attendees for the event.
      ```json  theme={null}
      [
        {
          "email": "attendee@example.com",
          "displayName": "Attendee Name",
          "optional": false
        }
      ]
      ```
    * `reminders` (object, optional): Information about the event's reminders.
      ```json  theme={null}
      {
        "useDefault": true,
        "overrides": [
          {
            "method": "email",
            "minutes": 15
          }
        ]
      }
```bash
    * `conferenceData` (object, optional): The conference-related information, such as details of a Google Meet conference.
      ```json  theme={null}
      {
        "createRequest": {
          "requestId": "unique-request-id",
          "conferenceSolutionKey": {
            "type": "hangoutsMeet"
          }
        }
      }
      ```
    * `visibility` (string, optional): Visibility of the event. Options: default, public, private, confidential. Default: default
    * `transparency` (string, optional): Whether the event blocks time on the calendar. Options: opaque, transparent. Default: opaque
  </Accordion>

  <Accordion title="google_calendar/view_events">
    **Description:** Retrieve events for the specified calendar.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID (use 'primary' for main calendar)
    * `timeMin` (string, optional): Lower bound for events (RFC3339)
    * `timeMax` (string, optional): Upper bound for events (RFC3339)
    * `maxResults` (integer, optional): Maximum number of events (default 10). Minimum: 1, Maximum: 2500
    * `orderBy` (string, optional): The order of the events returned in the result. Options: startTime, updated. Default: startTime
    * `singleEvents` (boolean, optional): Whether to expand recurring events into instances and only return single one-off events and instances of recurring events. Default: true
    * `showDeleted` (boolean, optional): Whether to include deleted events (with status equals cancelled) in the result. Default: false
    * `showHiddenInvitations` (boolean, optional): Whether to include hidden invitations in the result. Default: false
    * `q` (string, optional): Free text search terms to find events that match these terms in any field.
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `timeZone` (string, optional): Time zone used in the response.
    * `updatedMin` (string, optional): Lower bound for an event's last modification time (RFC3339) to filter by.
    * `iCalUID` (string, optional): Specifies an event ID in the iCalendar format to be provided in the response.
  </Accordion>

  <Accordion title="google_calendar/update_event">
    **Description:** Update an existing event.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID
    * `eventId` (string, required): Event ID to update
    * `summary` (string, optional): Updated event title
    * `description` (string, optional): Updated event description
    * `start_dateTime` (string, optional): Updated start time
    * `end_dateTime` (string, optional): Updated end time
  </Accordion>

  <Accordion title="google_calendar/delete_event">
    **Description:** Delete a specified event.

    **Parameters:**

    * `calendarId` (string, required): Calendar ID
    * `eventId` (string, required): Event ID to delete
  </Accordion>

  <Accordion title="google_calendar/view_calendar_list">
    **Description:** Retrieve user's calendar list.

    **Parameters:**

    * `maxResults` (integer, optional): Maximum number of entries returned on one result page. Minimum: 1
    * `pageToken` (string, optional): Token specifying which result page to return.
    * `showDeleted` (boolean, optional): Whether to include deleted calendar list entries in the result. Default: false
    * `showHidden` (boolean, optional): Whether to show hidden entries. Default: false
    * `minAccessRole` (string, optional): The minimum access role for the user in the returned entries. Options: freeBusyReader, owner, reader, writer
  </Accordion>
</AccordionGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setting Up Google Calendar Integration](./1671-setting-up-google-calendar-integration.md)

**Next:** [Usage Examples →](./1673-usage-examples.md)
