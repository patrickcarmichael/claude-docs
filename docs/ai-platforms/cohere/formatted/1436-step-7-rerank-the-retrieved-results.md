---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 7: Rerank the retrieved results

```python PYTHON
docs =[match['metadata']['text'] for match in res['matches']]

rerank_response = co.rerank(
  model = 'rerank-english-v2.0',
  query = query,
  documents = docs,
  top_n = 3,
)
for response in rerank_response:
  print(f"{response.relevance_score:.2f}: {response.document['text']}")
```
```txt title="Output"
0.99: Microsoft Office, or simply Office, is the former name of a family of client software, server software, and services developed by Microsoft. It was first announced by Bill Gates on August 1, 1988, at COMDEX in Las Vegas. Initially a marketing term for an office suite (bundled set of productivity applications), the first version of Office contained Microsoft Word, Microsoft Excel, and Microsoft PowerPoint. Over the years, Office applications have grown substantially closer with shared features such as a common spell checker, Object Linking and Embedding data integration and Visual Basic for Applications scripting language. Microsoft also positions Office as a development platform for line-of-business software under the Office Business Applications brand.
0.93: On January 21, 2015, during the "Windows 10: The Next Chapter" press event, Microsoft unveiled Office for Windows 10, Windows Runtime ports of the Android and iOS versions of the Office Mobile suite. Optimized for smartphones and tablets, they are universal apps that can run on both Windows and Windows for phones, and share similar underlying code. A simplified version of Outlook was also added to the suite. They will be bundled with Windows 10 mobile devices, and available from the Windows Store for the PC version of Windows 10. Although the preview versions were free for most editing, the release versions will require an Office 365 subscription on larger tablets (screen size larger than 10.1 inches) and desktops for editing, as with large Android tablets. Smaller tablets and phones will have most editing features for free.
0.87: In October 2022, Microsoft announced that it will phase out the Microsoft Office brand in favor of "Microsoft 365" by January 2023. The name will continue to be used for legacy product offerings.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
