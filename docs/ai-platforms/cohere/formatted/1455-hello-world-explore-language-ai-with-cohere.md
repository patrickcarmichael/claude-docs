---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hello World! Explore Language AI with Cohere

> This page contains a breakdown of some of what can be achieved with Cohere's LLM platform.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Hello_World_Meet_Language_AI.ipynb" />

Here we take a quick tour of what’s possible with language AI via Cohere’s Large Language Model (LLM) API. This is the Hello, World! of language AI, written for developers with little or no background in AI. In fact, we’ll do that by exploring the Hello, World! phrase itself.

Read the accompanying [blog post here](https://cohere.com/blog/hello-world-p1/).

<img alt="Hello World! Meet Language AI" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/hello-world/hello-world-feat.png" />

We’ll cover three groups of tasks that you will typically work on when dealing with language data, including:

* Generating text
* Classifying text
* Analyzing text

The first step is to install the Cohere Python SDK. Next, create an API key, which you can generate from the Cohere [dashboard](https://dashboard.cohere.com/register).
```python PYTHON
! pip install cohere altair umap-learn -q
```
```python PYTHON
import cohere
import pandas as pd
import numpy as np
import altair as alt

co = cohere.Client("COHERE_API_KEY") # Get your API key: https://dashboard.cohere.com/api-keys

```
The Cohere Generate endpoint generates text given an input, called “prompt”. The prompt provides a context of what we want the model to generate text. To illustrate this, let’s start with a simple prompt as the input.

### Try a Simple Prompt

```python PYTHON
prompt = "What is a Hello World program."

response = co.chat(
  message=prompt,
  model='command-r')

print(response.text)
```
````
A "Hello World" program is a traditional and simple program that is often used as an introduction to a new programming language. The program typically displays the message "Hello World" as its output. The concept of a "Hello World" program originated from the book *The C Programming Language* written by Kernighan and Ritchie, where the example program in the book displayed the message using the C programming language.

The "Hello World" program serves as a basic and straightforward way to verify that your development environment is set up correctly and to familiarize yourself with the syntax and fundamentals of the programming language. It's a starting point for learning how to write and run programs in a new language.

The program's simplicity makes it accessible to programmers of all skill levels, and it's often one of the first programs beginners write when learning to code. The exact implementation of a "Hello World" program varies depending on the programming language being used, but the core idea remains the same—to display the "Hello World" message.

Here's how a "Hello World" program can be written in a few select languages:
1. **C**:
```c
##include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
```
2. **Python**:
```python PYTHON
print("Hello World")
```
3. **Java**:
```java JAVA
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
4. **JavaScript**:
```javascript
console.log("Hello World");
```
5. **C#**:
```csharp
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello World");
    }
}
```
The "Hello World" program is a testament to the power of programming, as a simple and concise message can be displayed in numerous languages with just a few lines of code. It's an exciting first step into the world of software development!
````

### Create a Better Prompt

The output is not bad, but it can be better. We need to find a way to make the output tighter to how we want it to be, which is where we leverage *prompt engineering*.
```python PYTHON
prompt = """
Write the first paragraph of a blog post given a blog title.
--
Blog Title: Best Activities in Toronto
First Paragraph: Looking for fun things to do in Toronto? When it comes to exploring Canada's
largest city, there's an ever-evolving set of activities to choose from. Whether you're looking to
visit a local museum or sample the city's varied cuisine, there is plenty to fill any itinerary. In
this blog post, I'll share some of my favorite recommendations
--
Blog Title: Mastering Dynamic Programming
First Paragraph: In this piece, we'll help you understand the fundamentals of dynamic programming,
and when to apply this optimization technique. We'll break down bottom-up and top-down approaches to
solve dynamic programming problems.
--
Blog Title: Learning to Code with Hello, World!
First Paragraph:"""

response = co.chat(
  message=prompt,
  model='command-r')

print(response.text)
```
```
Starting to code can be daunting, but it's actually simpler than you think! The famous first program, "Hello, World!" is a rite of passage for all coders, and an excellent starting point to begin your coding journey. This blog will guide you through the process of writing your very first line of code, and help you understand why learning to code is an exciting and valuable skill to have, covering the fundamentals and the broader implications of this seemingly simple phrase.
```

### Automating the Process

In real applications, you will likely need to produce these text generations on an ongoing basis, given different inputs. Let’s simulate that with our example.
```python PYTHON
def generate_text(topic):
  prompt = f"""
Write the first paragraph of a blog post given a blog title.
--
Blog Title: Best Activities in Toronto
First Paragraph: Looking for fun things to do in Toronto? When it comes to exploring Canada's
largest city, there's an ever-evolving set of activities to choose from. Whether you're looking to
visit a local museum or sample the city's varied cuisine, there is plenty to fill any itinerary. In
this blog post, I'll share some of my favorite recommendations
--
Blog Title: Mastering Dynamic Programming
First Paragraph: In this piece, we'll help you understand the fundamentals of dynamic programming,
and when to apply this optimization technique. We'll break down bottom-up and top-down approaches to
solve dynamic programming problems.
--
Blog Title: {topic}
First Paragraph:"""
  # Generate text by calling the Chat endpoint

  response = co.chat(
    message=prompt,
    model='command-r')

  return response.text
```
```python PYTHON
topics = ["How to Grow in Your Career",
          "The Habits of Great Software Developers",
          "Ideas for a Relaxing Weekend"]
```
```python PYTHON
paragraphs = []

for topic in topics:
  paragraphs.append(generate_text(topic))

for topic,para in zip(topics,paragraphs):
  print(f"Topic: {topic}")
  print(f"First Paragraph: {para}")
  print("-"*10)
```
```
Topic: How to Grow in Your Career
First Paragraph: Advancing in your career can seem like a daunting task, especially if you're unsure of the path ahead. In this ever-changing professional landscape, there are numerous factors to consider. This blog aims to shed light on the strategies and skills that can help you navigate the complexities of career progression and unlock your full potential. Whether you're looking to secure a promotion or explore new opportunities, these insights will help you chart a course for your future. Let's embark on this journey of self-improvement and professional growth, equipping you with the tools to succeed in your career aspirations.
----------
Topic: The Habits of Great Software Developers
First Paragraph: Great software developers are renowned for their ability to write robust code and create innovative applications, but what sets them apart from their peers? In this blog, we'll delve into the daily habits that contribute to their success. From their approach to coding challenges to the ways they stay organized, we'll explore the routines and practices that help them excel in the fast-paced world of software development. Understanding these habits can help you elevate your own skills and join the ranks of these industry leaders.
----------
Topic: Ideas for a Relaxing Weekend
First Paragraph: Life can be stressful, and sometimes we just need a relaxing weekend to unwind and recharge. In this fast-paced world, taking some time to slow down and rejuvenate is essential. This blog post is here to help you plan the perfect low-key weekend with some easy and accessible ideas. From cozy indoor activities to peaceful outdoor adventures, I'll share some ideas to help you renew your mind, body, and spirit. Whether you're a homebody or an adventure seeker, there's something special for everyone. So, grab a cup of tea, sit back, and get ready to dive into a calming weekend of self-care and relaxation!
----------
```
Cohere’s Classify endpoint makes it easy to take a list of texts and predict their categories, or classes. A typical machine learning model requires many training examples to perform text classification, but with the Classify endpoint, you can get started with as few as 5 examples per class.

### Sentiment Analysis

```python PYTHON
from cohere import ClassifyExample

examples = [
    ClassifyExample(text="I’m so proud of you", label="positive"),
    ClassifyExample(text="What a great time to be alive", label="positive"),
    ClassifyExample(text="That’s awesome work", label="positive"),
    ClassifyExample(text="The service was amazing", label="positive"),
    ClassifyExample(text="I love my family", label="positive"),
    ClassifyExample(text="They don't care about me", label="negative"),
    ClassifyExample(text="I hate this place", label="negative"),
    ClassifyExample(text="The most ridiculous thing I've ever heard", label="negative"),
    ClassifyExample(text="I am really frustrated", label="negative"),
    ClassifyExample(text="This is so unfair", label="negative"),
    ClassifyExample(text="This made me think", label="neutral"),
    ClassifyExample(text="The good old days", label="neutral"),
    ClassifyExample(text="What's the difference", label="neutral"),
    ClassifyExample(text="You can't ignore this", label="neutral"),
    ClassifyExample(text="That's how I see it", label="neutral")
]
```
```python PYTHON
inputs=["Hello, world! What a beautiful day",
        "It was a great time with great people",
        "Great place to work",
        "That was a wonderful evening",
        "Maybe this is why",
        "Let's start again",
        "That's how I see it",
        "These are all facts",
        "This is the worst thing",
        "I cannot stand this any longer",
        "This is really annoying",
        "I am just plain fed up"
        ]
```
```python PYTHON
def classify_text(inputs, examples):
  """
  Classify a list of input texts
  Arguments:
    inputs(list[str]): a list of input texts to be classified
    examples(list[Example]): a list of example texts and class labels
  Returns:
    classifications(list): each result contains the text, labels, and conf values
  """
  # Classify text by calling the Classify endpoint

  response = co.classify(
    model='embed-v4.0',
    inputs=inputs,
    examples=examples)

  classifications = response.classifications

  return classifications
```
```python PYTHON
predictions = classify_text(inputs,examples)

classes = ["positive","negative","neutral"]
for inp,pred in zip(inputs,predictions):
  class_pred = pred.predictions[0]
  class_idx = classes.index(class_pred)
  class_conf = pred.confidences[0]

  print(f"Input: {inp}")
  print(f"Prediction: {class_pred}")
  print(f"Confidence: {class_conf:.2f}")
  print("-"*10)
```
```
Input: Hello, world! What a beautiful day
Prediction: positive
Confidence: 0.84
----------
Input: It was a great time with great people
Prediction: positive
Confidence: 0.99
----------
Input: Great place to work
Prediction: positive
Confidence: 0.91
----------
Input: That was a wonderful evening
Prediction: positive
Confidence: 0.96
----------
Input: Maybe this is why
Prediction: neutral
Confidence: 0.70
----------
Input: Let's start again
Prediction: neutral
Confidence: 0.83
----------
Input: That's how I see it
Prediction: neutral
Confidence: 1.00
----------
Input: These are all facts
Prediction: neutral
Confidence: 0.78
----------
Input: This is the worst thing
Prediction: negative
Confidence: 0.93
----------
Input: I cannot stand this any longer
Prediction: negative
Confidence: 0.93
----------
Input: This is really annoying
Prediction: negative
Confidence: 0.99
----------
Input: I am just plain fed up
Prediction: negative
Confidence: 1.00
----------
```
Cohere’s Embed endpoint takes a piece of text and turns it into a vector embedding. Embeddings represent text in the form of numbers that capture its meaning and context. What it means is that it gives you the ability to turn unstructured text data into a structured form. It opens up ways to analyze and extract insights from them.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
