---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Download PDF and Extract Contents

Here we will load in an academic paper that proposes the use of many open source language models in a collaborative manner together to outperform proprietary models that are much larger!

We will use the text in the PDF as content to generate the podcast with!

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=caffab5ada2f163e753291e76586bb05" alt="" data-og-width="1410" width="1410" data-og-height="1150" height="1150" data-path="images/guides/24.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=97c884d170b731472a20dff0e619f660 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=82d39461d40964d6377072712a316fba 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95bf71e40b9f039606cca195de30e816 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=267eeb92db3688b931fa1e881c30cf9b 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=882994d0c0996005ad598c15a0a1785f 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/24.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7cb93cda496d12c431cd9599ca35d143 2500w" /></Frame>

Download the PDF file and then extract text contents using the function below.
```bash
!wget https://arxiv.org/pdf/2406.04692
!mv 2406.04692 MoA.pdf
```
```py
from pypdf import PdfReader


def get_PDF_text(file: str):
    text = ""

    # Read the PDF file and extract text

    try:
        with Path(file).open("rb") as f:
            reader = PdfReader(f)
            text = "\n\n".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        raise f"Error reading the PDF file: {str(e)}"

        # Check if the PDF has more than ~400,000 characters

        # The context lenght limit of the model is 131,072 tokens and thus the text should be less than this limit

        # Assumes that 1 token is approximately 4 characters

    if len(text) > 400000:
        raise "The PDF is too long. Please upload a PDF with fewer than ~131072 tokens."

    return text


text = get_PDF_text("MoA.pdf")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
