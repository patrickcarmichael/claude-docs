---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 6: Display the results

```python PYTHON
for idx, r in enumerate(final_result):
  print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.5f}")
  print("\n")
```
```txt title="Output"
Document Rank: 1, Document Index: 0
Document: YouTube began as a venture capital–funded technology startup. Between November 2005 and April 2006, the company raised money from various investors, with Sequoia Capital, $11.5 million, and Artis Capital Management, $8 million, being the largest two. YouTube's early headquarters were situated above a pizzeria and a Japanese restaurant in San Mateo, California. In February 2005, the company activated codice_1. The first video was uploaded April 23, 2005. Titled "Me at the zoo", it shows co-founder Jawed Karim at the San Diego Zoo and can still be viewed on the site. In May, the company launched a public beta and by November, a Nike ad featuring Ronaldinho became the first video to reach one million total views. The site launched officially on December 15, 2005, by which time the site was receiving 8 million views a day. Clips at the time were limited to 100 megabytes, as little as 30 seconds of footage.
Relevance Score: 0.94815


Document Rank: 2, Document Index: 1
Document: Karim said the inspiration for YouTube first came from the Super Bowl XXXVIII halftime show controversy when Janet Jackson's breast was briefly exposed by Justin Timberlake during the halftime show. Karim could not easily find video clips of the incident and the 2004 Indian Ocean Tsunami online, which led to the idea of a video-sharing site. Hurley and Chen said that the original idea for YouTube was a video version of an online dating service, and had been influenced by the website Hot or Not. They created posts on Craigslist asking attractive women to upload videos of themselves to YouTube in exchange for a $100 reward. Difficulty in finding enough dating videos led to a change of plans, with the site's founders deciding to accept uploads of any video.
Relevance Score: 0.91626


Document Rank: 3, Document Index: 2
Document: YouTube was not the first video-sharing site on the Internet; Vimeo was launched in November 2004, though that site remained a side project of its developers from CollegeHumor at the time and did not grow much, either. The week of YouTube's launch, NBC-Universal's "Saturday Night Live" ran a skit "Lazy Sunday" by The Lonely Island. Besides helping to bolster ratings and long-term viewership for "Saturday Night Live", "Lazy Sunday"'s status as an early viral video helped establish YouTube as an important website. Unofficial uploads of the skit to YouTube drew in more than five million collective views by February 2006 before they were removed when NBCUniversal requested it two months later based on copyright concerns. Despite eventually being taken down, these duplicate uploads of the skit helped popularize YouTube's reach and led to the upload of more third-party content. The site grew rapidly; in July 2006, the company announced that more than 65,000 new videos were being uploaded every day and that the site was receiving 100 million video views per day.
Relevance Score: 0.90665
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
