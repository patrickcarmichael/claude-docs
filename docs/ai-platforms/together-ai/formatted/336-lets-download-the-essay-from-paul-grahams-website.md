---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Let's download the essay from Paul Graham's website

import requests
from bs4 import BeautifulSoup


def scrape_pg_essay():

    url = "https://paulgraham.com/foundermode.html"

    try:
        # Send GET request to the URL

        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content

        soup = BeautifulSoup(response.text, "html.parser")

        # Paul Graham's essays typically have the main content in a font tag

        # You might need to adjust this selector based on the actual HTML structure

        content = soup.find("font")

        if content:
            # Extract and clean the text

            text = content.get_text()
            # Remove extra whitespace and normalize line breaks

            text = " ".join(text.split())
            return text
        else:
            return "Could not find the main content of the essay."

    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
