---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## instructions

{instructions}"""
```
Next, we build the instructions. Because each instruction may have a different objective and modifiers, we track them using metadata. This will later be required for evaluation (i.e. to know what the prompt is asking).
```python PYTHON

instruction_objectives = {
    "general_summarization": "Summarize the meeting based on the transcript.",
    "action_items": "What are the follow-up items based on the meeting transcript?",
}

format_length_modifiers = {
    "paragraphs_short": {
        "text": "In paragraph form, output your response. Use at least 10 words and at most 50 words in total.",
        "objectives": ["general_summarization"],
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 10,
            "max_length": 50,
        },
    },
    "paragraphs_medium": {
        "text": "Return the answer in the form of paragraphs. Make sure your answer is between 50 and 200 words long.",
        "objectives": ["general_summarization"],
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 50,
            "max_length": 200,
        },
    },
    "bullets_short_3": {
        "text": "Format your answer in the form of bullets. Use exactly 3 bullets. Each bullet should be at least 10 words and at most 20 words.",
        "objectives": ["general_summarization", "action_items"],
        "eval_metadata": {
            "format": "bullets",
            "number": 3,
            "min_length": 10,
            "max_length": 20,
        },
    },
    "bullets_medium_2": {
        "text": "In bullets, output your response. Make sure to use exactly 2 bullets. Make sure each bullet is between 20 and 80 words long.",
        "objectives": ["general_summarization", "action_items"],
        "eval_metadata": {
            "format": "bullets",
            "number": 2,
            "min_length": 20,
            "max_length": 80,
        },
    },
}
```
Let's combine the objectives and format/length modifiers to finish building the instructions.
```python PYTHON
instructions = []
for obj_name, obj_text in instruction_objectives.items():
    for mod_data in format_length_modifiers.values():
        for mod_obj in mod_data["objectives"]:
            if mod_obj == obj_name:
                instruction = {
                        "instruction": f"{obj_text} {mod_data['text']}",
                        "eval_metadata": mod_data["eval_metadata"],
                        "objective": obj_name,
                    }
                instructions.append(instruction)

print(json.dumps(instructions[:2], indent=4))
```
```python title="Output"
[
    {
        "instruction": "Summarize the meeting based on the transcript. In paragraph form, output your response. Use at least 10 words and at most 50 words in total.",
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 10,
            "max_length": 50
        },
        "objective": "general_summarization"
    },
    {
        "instruction": "Summarize the meeting based on the transcript. Return the answer in the form of paragraphs. Make sure your answer is between 50 and 200 words long.",
        "eval_metadata": {
            "format": "paragraphs",
            "min_length": 50,
            "max_length": 200
        },
        "objective": "general_summarization"
    }
]
```
Finally, let's build the final prompts by semi-randomly pairing the instructions with transcripts from the QMSum dataset.
```python PYTHON
data = pd.DataFrame(instructions)

transcripts = sorted(transcripts, key=lambda x: len(x), reverse=True)[:int(len(transcripts) * 0.25)]
random.seed(42)
random.shuffle(transcripts)
data["transcript"] = transcripts[:len(data)]

data["prompt"] = data.apply(lambda x: prompt_template.format(transcript=x["transcript"], instructions=x["instruction"]), axis=1)
```
```python PYTHON
data["transcript_token_len"] = [len(x) for x in co.batch_tokenize(data["transcript"].tolist(), model=co_model)]
```
```python PYTHON
print(data["prompt"][0])
```
```txt title="Output"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
