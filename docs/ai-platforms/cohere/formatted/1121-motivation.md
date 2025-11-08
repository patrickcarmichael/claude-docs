---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Motivation

Agents can play a crucial role in different enterprise scenarios. One such example is creating a request to fetch results from an existing enterprise API with specific requirements. For example, given a user query:

`Retrieve id 7410e652-639d-402e-984e-8fd7025f0aac 8bb21b93-2ddf-4a63-af63-ddb6b1be49a1, ref GLPNT0005GUJOGGE GLSBR000BGASOBRE, nmg 0000234GLCHL0200ARTINDIUS'`

The expected API request is:

`[{"uuid":["7410e652-639d-402e-984e-8fd7025f0aac","8bb21b93-2ddf-4a63-af63-ddb6b1be49a1"],"page":0,"size":10}, {"objref":["GLPNT0005GUJOGGE","GLSBR000BGASOBRE"],"page":0,"size":10},{"nmgs":["0000234GLCHL0200ARTINDIUS"],"page":0,"size":10}]`

This kind of task poses a major challenge, namely, the model must be very precise at identifying the codes in the query, based on their alphanumeric patterns, and matching these codes with the right parameter - for example, the code `GLSBR000BGASOBRE` needs to map to
`objref`. The task is even more challenging when multiple APIs are available, and the model has to deal with a plethora of parameters.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
