---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Initial Test

Before we touch any fine-tuning or reward functions, we first run the task with an off‑the‑shelf model and record how its raw summaries perform. This baseline reveals the model’s natural tendencies—what it captures well, what it omits, and where it drifts from our goals.

Let’s define a system prompt:
```python
sys_prompt = """
Your job is to read a long document and produce a single, fluent English paragraph ≤ 50 GPT-2 tokens that captures the document’s four most important facts.

Rules you must obey for every response

1. Token limit – maximum 50 tokens
2. Importance – include the most critical factual points; leave out everything else.
3. No PII – never output emails, phone numbers, SSNs, or other personally identifying strings that may occur in the input.
4. Fluency – write clear, grammatical English in a single paragraph.
5. Output only the paragraph – no explanations, bullet lists, or metadata.

If the rules conflict, the priority is: Length > Coverage > No PII > Fluency.
"""
```

And try a sample document (I’m using a news article):
```python
long_document = """
MONTEREY PARK (KABC) -- Authorities are investigating an apparent explosion at an LASD training facility in Monterey Park where at least three deputies were killed.

The incident was reported just before 7:30 a.m. Friday at what looked to be LASD's SEB compound, which houses the sheriff's department's special enforcement units and bomb squad.

It appears the Sheriff's Enforcement Bureau personnel were handling some kind of explosives when there was a blast, according to preliminary information from sources. Three deputies were killed in the incident.

The Los Angeles County Fire Department responded to the scene. It's unclear if there were any other injuries.

It is believed to have been an accident. More is expected soon from the sheriff.

There were no other details immediately available regarding this incident.

L.A. City Mayor Karen Bass confirmed that the LAPD bomb squad is responding to the scene and assisting with the incident.

Governor Gavin Newsom's Office said the governor has been briefed on the apparent explosion and that the Governor's Office of Emergency Services is in contact with LASD while closely monitoring the situation.

L.A. County Supervisor Kathryn Barger issued the following statement regarding the deadly incident:

"I am heartbroken to hear of the terrible tragedy that has unfolded today at an L.A. County Sheriff's Department facility. I am closely tracking the situation as we learn more about what occurred and the condition of those affected. My heart is heavy, and my thoughts are with the brave men and women of the Sheriff's Department during this difficult time. We stand with them and their families as they navigate the hours and days ahead."

L.A. County Supervisor Hilda Solis also issued a statement:

"I am deeply saddened by the tragic incident that occurred this morning at the Los Angeles County Sheriff's Department Biscailuz Training Academy in East Los Angeles. My heart goes out to the families, friends, and colleagues of the three individuals who lost their lives in what appears to have been a devastating explosion. I am in contact with Sheriff Robert Luna and closely monitoring the situation as we await further details. My thoughts are with all those grieving and the first responders who are on the scene."

The FBI and ATF responded to the scene, according to a post from U.S. Attorney General Pam Bondi posted on X.

"Our federal agents are at the scene and we are working to learn more. Please pray for the families of the sheriff's deputies killed," the post said.
"""
```
```python
response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": long_document}
    ],
    max_tokens=100, # can't set it to 50 as the model might just stop in the middle of a sentence

)

print(response.choices[0].message.content)
```
```python
"An apparent explosion occurred at the Los Angeles County Sheriff's Department training facility in Monterey Park, resulting in the deaths of at least three deputies. The incident occurred during a training exercise involving explosives, and authorities are investigating the cause as an accident. The Los Angeles County Fire Department and LAPD bomb squad responded to the scene, with the FBI and ATF also arriving to assist. L.A. County Supervisors Kathryn Barger and Hilda Solis expressed their condolences to the families of the victims, while Governor"
```

Pretty clear that the “summary” is hardly concise and starts simply copy the input text after a little bit, even though we specified to limit itself to 50 tokens in the system prompt. Not what we want from a summary.

To get around this, we’ll need to fine-tune our model. To understand the fundamentals of RFT and how the fireworks platform makes it easy, check out our course on Knowledge Distillation.

We’ll need to set up a reward function that gives the fireworks training kernel a signal on how *good* a certain response is. It’s our job to figure out what “good” means. Let’s get started!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
