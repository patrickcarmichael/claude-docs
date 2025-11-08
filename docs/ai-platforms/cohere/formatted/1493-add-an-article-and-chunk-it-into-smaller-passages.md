---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Add an article and chunk it into smaller passages

```python PYTHON

!wget 'https://docs.google.com/uc?export=download&amp;id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F' -O steve-jobs-commencement.txt
```
```txt title="Output"
--2023-06-08 06:11:19--  https://docs.google.com/uc?export=download&amp;id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F
Resolving docs.google.com (docs.google.com)... 74.125.200.101, 74.125.200.138, 74.125.200.102, ...
Connecting to docs.google.com (docs.google.com)|74.125.200.101|:443... connected.
HTTP request sent, awaiting response... 303 See Other
Location: https://doc-0g-84-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/84t4moii9dmg08hmrh6rfpp8ecrjh6jq/1686204675000/12721472133292131824/*/1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F?e=download&amp;uuid=a26288c7-ad0c-4707-ae0b-72cb94c224dc [following]
Warning: wildcards not supported in HTTP.
--2023-06-08 06:11:19--  https://doc-0g-84-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/84t4moii9dmg08hmrh6rfpp8ecrjh6jq/1686204675000/12721472133292131824/*/1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F?e=download&amp;uuid=a26288c7-ad0c-4707-ae0b-72cb94c224dc
Resolving doc-0g-84-docs.googleusercontent.com (doc-0g-84-docs.googleusercontent.com)... 74.125.130.132, 2404:6800:4003:c01::84
Connecting to doc-0g-84-docs.googleusercontent.com (doc-0g-84-docs.googleusercontent.com)|74.125.130.132|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 11993 (12K) [text/plain]
Saving to: ‘steve-jobs-commencement.txt’

steve-jobs-commence 100%[===================>]  11.71K  --.-KB/s    in 0s

2023-06-08 06:11:20 (115 MB/s) - ‘steve-jobs-commencement.txt’ saved [11993/11993]
```
```python PYTHON
loader = TextLoader("steve-jobs-commencement.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
