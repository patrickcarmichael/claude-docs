---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Define the chunk_split function (from earlier in your notebook)

def chunk_split(text, max_words, threshold=0.8):

    words = text.split()  # Turn the text into a list of words

    chunks = []  # Initialize an empty list to store our chunks

    start = 0  # Starting index for slicing the words list

    while start < len(words):
        # Determine the end index for the current chunk

        end = min(start + max_words, len(words))
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)  # Combine words back into a string

        # If we're at the end of the text or the chunk is too short, add it as is

        if end == len(words) or len(chunk_words) < max_words * threshold:
            chunks.append(chunk_text.strip())
            break

        # Try to find a natural breaking point within the chunk

        split_point = None
        for separator in ["\n", ".", ")", " "]:
            idx = chunk_text.rfind(separator)
            if idx != -1 and idx >= len(chunk_text) * threshold:
                split_point = idx + 1  # Position after the separator

                break

        if split_point:
            # If a good split point is found, add the chunk up to that point

            chunks.append(chunk_text[:split_point].strip())
            # Move the start index forward by the number of words consumed

            consumed = len(chunk_text[:split_point].split())
            start += consumed
        else:
            # If no good split point is found, add the entire chunk

            chunks.append(chunk_text.strip())
            start = end  # Move to the next chunk

    return chunks

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
