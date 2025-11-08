---
title: "Set Usage Configuration"
source: "https://docs.windsurf.com/windsurf/accounts/api-reference/usage-config"
---

# Set Usage Configuration
Source: https://docs.windsurf.com/windsurf/accounts/api-reference/usage-config

POST https://server.codeium.com/api/v1/UsageConfig
Configure usage caps for add-on credits

## Overview

Set or clear usage caps on add-on credits for your organization. You can scope these configurations to the team level, specific groups, or individual users.

## Request

<ParamField body="service_key" type="string" required>
  Your service key with appropriate permissions
</ParamField>

### Credit Cap Configuration (Choose One)

<ParamField body="clear_add_on_credit_cap" type="boolean">
  Set to `true` to clear the existing add-on credit cap
</ParamField>

<ParamField body="set_add_on_credit_cap" type="integer">
  Set a new add-on credit cap (integer value)
</ParamField>

<Info>
  You must provide either `clear_add_on_credit_cap` or `set_add_on_credit_cap`, but not both.
</Info>

### Scope Configuration (Choose One)

<ParamField body="team_level" type="boolean">
  Set to `true` to apply the configuration at the team level
</ParamField>

<ParamField body="group_id" type="string">
  Apply the configuration to a specific group by providing the group ID
</ParamField>

<ParamField body="user_email" type="string">
  Apply the configuration to a specific user by providing their email address
</ParamField>

<Info>
  You must provide one of `team_level`, `group_id`, or `user_email` to define the scope.
</Info>

### Example Request - Set Credit Cap for Team

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "set_add_on_credit_cap": 10000,
  "team_level": true
}' \
https://server.codeium.com/api/v1/UsageConfig
```

### Example Request - Set Credit Cap for Group

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "set_add_on_credit_cap": 5000,
  "group_id": "engineering_team"
}' \
https://server.codeium.com/api/v1/UsageConfig
```

### Example Request - Set Credit Cap for User

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "set_add_on_credit_cap": 1000,
  "user_email": "user@example.com"
}' \
https://server.codeium.com/api/v1/UsageConfig
```

### Example Request - Clear Credit Cap

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "clear_add_on_credit_cap": true,
  "team_level": true
}' \
https://server.codeium.com/api/v1/UsageConfig
```

## Response

The response body is empty. A `200` status code indicates the operation was successful.

## Error Responses

Common error scenarios:

* Invalid service key or insufficient permissions
* Both `clear_add_on_credit_cap` and `set_add_on_credit_cap` provided
* Neither `clear_add_on_credit_cap` nor `set_add_on_credit_cap` provided
* Multiple scope parameters provided
* No scope parameter provided
* Invalid group ID or user email
* Rate limit exceeded

---

← Previous: [Error Handling](./error-handling.md) | [Index](./index.md) | Next: [Get User Page Analytics](./get-user-page-analytics.md) →