---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using Base64 Encoded PDFs

For local PDF files or when you need to send PDF content directly, you can base64 encode the file:

<Template
  data={{
  API_KEY_REF,
  MODEL: 'google/gemma-3-27b-it',
  ENGINE: PDFParserEngine.PDFText,
  DEFAULT_PDF_ENGINE,
}}
>
```python
    import requests
    import json
    import base64
    from pathlib import Path

    def encode_pdf_to_base64(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY_REF}",
        "Content-Type": "application/json"
    }

    # Read and encode the PDF

    pdf_path = "path/to/your/document.pdf"
    base64_pdf = encode_pdf_to_base64(pdf_path)
    data_url = f"data:application/pdf;base64,{base64_pdf}"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What are the main points in this document?"
                },
                {
                    "type": "file",
                    "file": {
                        "filename": "document.pdf",
                        "file_data": data_url
                    }
                },
            ]
        }
    ]

    # Optional: Configure PDF processing engine

    # PDF parsing will still work even if the plugin is not explicitly set

    plugins = [
        {
            "id": "file-parser",
            "pdf": {
                "engine": "{{ENGINE}}"  # defaults to "{{DEFAULT_PDF_ENGINE}}". See Pricing above

            }
        }
    ]

    payload = {
        "model": "{{MODEL}}",
        "messages": messages,
        "plugins": plugins
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
```
```typescript
    async function encodePDFToBase64(pdfPath: string): Promise<string> {
      const pdfBuffer = await fs.promises.readFile(pdfPath);
      const base64PDF = pdfBuffer.toString('base64');
      return `data:application/pdf;base64,${base64PDF}`;
    }

    // Read and encode the PDF
    const pdfPath = 'path/to/your/document.pdf';
    const base64PDF = await encodePDFToBase64(pdfPath);

    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${API_KEY_REF}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: '{{MODEL}}',
        messages: [
          {
            role: 'user',
            content: [
              {
                type: 'text',
                text: 'What are the main points in this document?',
              },
              {
                type: 'file',
                file: {
                  filename: 'document.pdf',
                  file_data: base64PDF,
                },
              },
            ],
          },
        ],
        // Optional: Configure PDF processing engine
        // PDF parsing will still work even if the plugin is not explicitly set
        plugins: [
          {
            id: 'file-parser',
            pdf: {
              engine: '{{ENGINE}}', // defaults to "{{DEFAULT_PDF_ENGINE}}". See Pricing above
            },
          },
        ],
      }),
    });

    const data = await response.json();
    console.log(data);
```
</Template>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
