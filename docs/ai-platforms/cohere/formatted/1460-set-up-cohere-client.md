---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Set up Cohere client

co_model = 'command-r'
co_api_key = getpass("Enter your Cohere API key: ")
co = cohere.Client(api_key=co_api_key)
```
```python PYTHON
def load_long_pdf(file_path):
    """
    Load a long PDF file and extract its text content.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text content of the PDF file.
    """
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        full_text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            full_text += page.extract_text()
    return full_text

def save_pdf_from_url(pdf_url, save_path):
    try:
        # Send a GET request to the PDF URL

        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Open the local file for writing in binary mode

        with open(save_path, 'wb') as file:
            # Write the content of the response to the local file

            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"PDF saved successfully to '{save_path}'")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
```
In this example we use the Proposal for a Regulation of the European Parliament and of the Council defining rules on Artificial Intelligence from 26 January 2024, [link](https://data.consilium.europa.eu/doc/document/ST-5662-2024-INIT/en/pdf).
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
