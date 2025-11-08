---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run evaluations \[#run-evals]

Now that we have our evaluation dataset and defined our evaluation functions, let's run evaluations!

First, we generate completions to be graded. We will use Cohere's [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-v01) model, boasting a context length of 128K.
```python PYTHON
completions = []
for prompt in data["prompt"]:
    completion = co.chat(message=prompt, model="command-r", temperature=0.2).text
    completions.append(completion)

data["completion"] = completions
```
```python PYTHON
print(data["completion"][0])
```
PhD D is transcribing recorded sessions to locate overlapping speech zones and categorizing them as acoustic events. The team discusses the parameters PhD D should use and how to define these events, considering the number of speakers and silence.

Let's grade the completions using our LLM and non-LLM checks.
```python PYTHON
data["format_score"] = data.apply(
    lambda x: score_format(x["completion"], x["eval_metadata"]["format"]), axis=1
)

data["length_score"] = data.apply(
    lambda x: score_length(
        x["completion"],
        x["eval_metadata"]["format"],
        x["eval_metadata"].get("min_length"),
        x["eval_metadata"].get("max_length"),
    ),
    axis=1,
)

data["completeness_score"] = data.apply(
    lambda x: score_llm(x["prompt"], x["completion"], criteria_completeness), axis=1
)

data["correctness_score"] = data.apply(
    lambda x: score_llm(x["prompt"], x["completion"], criteria_correctness), axis=1
)

data["conciseness_score"] = data.apply(
    lambda x: score_llm(x["prompt"], x["completion"], criteria_conciseness), axis=1
)
```
```python PYTHON
data
```
<div>
  <table border="1" class="dataframe fern-table">
    <thead>
      <tr>
        <th />

        <th>
          instruction
        </th>

        <th>
          eval_metadata
        </th>

        <th>
          objective
        </th>

        <th>
          transcript
        </th>

        <th>
          prompt
        </th>

        <th>
          transcript_token_len
        </th>

        <th>
          completion
        </th>

        <th>
          format_score
        </th>

        <th>
          length_score
        </th>

        <th>
          completeness_score
        </th>

        <th>
          correctness_score
        </th>

        <th>
          conciseness_score
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <th>
          0
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'paragraphs', 'min_length': 10, 'ma...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          PhD F: As opposed to the rest of us \nPhD D: W...
        </td>

        <td>
          \## meeting transcript\nPhD F: As opposed to th...

        </td>

        <td>
          1378
        </td>

        <td>
          PhD D is transcribing recorded sessions to loc...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          1
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'paragraphs', 'min_length': 50, 'ma...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          Lynne Neagle AM: Thank you very much And the n...
        </td>

        <td>
          \## meeting transcript\nLynne Neagle AM: Thank ...

        </td>

        <td>
          1649
        </td>

        <td>
          The discussion focused on the impact of COVID1...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          2
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'bullets', 'number': 3, 'min_length...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          Industrial Designer: Yep So we are to mainly d...
        </td>

        <td>
          \## meeting transcript\nIndustrial Designer: Ye...

        </td>

        <td>
          1100
        </td>

        <td>
          \- The team is designing a remote control with ...
        </td>

        <td>
          1
        </td>

        <td>
          0
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          3
        </th>

        <td>
          Summarize the meeting based on the transcript....
        </td>

        <td>
          \{'format': 'bullets', 'number': 2, 'min_length...
        </td>

        <td>
          general_summarization
        </td>

        <td>
          Industrial Designer: Mm I think one of the ver...
        </td>

        <td>
          \## meeting transcript\nIndustrial Designer: Mm...

        </td>

        <td>
          2618
        </td>

        <td>
          \- The team discusses the target demographic fo...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          4
        </th>

        <td>
          What are the follow-up items based on the meet...
        </td>

        <td>
          \{'format': 'bullets', 'number': 3, 'min_length...
        </td>

        <td>
          action_items
        </td>

        <td>
          Marketing: so a lot of people have to be able ...
        </td>

        <td>
          \## meeting transcript\nMarketing: so a lot of ...

        </td>

        <td>
          2286
        </td>

        <td>
          \- Investigate how the remote will interact wit...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>

      <tr>
        <th>
          5
        </th>

        <td>
          What are the follow-up items based on the meet...
        </td>

        <td>
          \{'format': 'bullets', 'number': 2, 'min_length...
        </td>

        <td>
          action_items
        </td>

        <td>
          Project Manager: Alright So finance And we wil...
        </td>

        <td>
          \## meeting transcript\nProject Manager: Alrigh...

        </td>

        <td>
          1965
        </td>

        <td>
          \- The project manager will send the updated de...
        </td>

        <td>
          1
        </td>

        <td>
          1
        </td>

        <td>
          0.8
        </td>

        <td>
          1.0
        </td>

        <td>
          0.8
        </td>
      </tr>
    </tbody>
  </table>
</div>

Finally, let's print the average scores per critiera.
```python PYTHON
avg_scores = data[["format_score", "length_score", "completeness_score", "correctness_score", "conciseness_score"]].mean()
print(avg_scores)
```
```txt title="Output"
format_score          1.000000
length_score          0.833333
completeness_score    0.800000
correctness_score     1.000000
conciseness_score     0.800000
dtype: float64
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
