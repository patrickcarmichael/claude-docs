---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## install the required packages

!pip install -qU together arcadepy
```

Gmail Configuration:
```bash
  import os
  from arcadepy import Arcade
  from together import Together

  ## Set environment variables

  os.environ["TOGETHER_API_KEY"] = "XXXXXXXXXXXXX"  # Replace with your actual Together API key

  os.environ["ARCADE_API_KEY"] = "arc_XXXXXXXXXXX"    # Replace with your actual Arcade API key

  ## Initialize clients

  together_client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
  arcade_client = Arcade()  # Automatically finds the ARCADE_API_KEY env variable

  ## Set up user ID (your email)

  USER_ID = "your_email@example.com"  # Change this to your email

  ## Authorize Gmail access

  auth_response = arcade_client.tools.authorize(
      tool_name="Google.SendEmail",
      user_id=USER_ID,
  )

  if auth_response.status != "completed":
      print(f"Click this link to authorize: {auth_response.url}")
      # Wait for the authorization to complete

      arcade_client.auth.wait_for_completion(auth_response)

  print("Authorization completed!")
```

Learn more in our [Arcade guide](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Arcade.dev/Agents_Arcade.ipynb) notebook.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
