**Navigation:** [← Previous](./13-using-the-evaluation-tool.md) | [Index](./index.md) | [Next →](./15-system-prompts.md)

---

# Glossary
Source: https://docs.claude.com/en/docs/about-claude/glossary

These concepts are not unique to Anthropic’s language models, but we present a brief summary of key terms below.

## Context window

The "context window" refers to the amount of text a language model can look back on and reference when generating new text. This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model's ability to handle longer prompts or maintain coherence over extended conversations.

See our [guide to understanding context windows](/en/docs/build-with-claude/context-windows) to learn more.

## Fine-tuning

Fine-tuning is the process of further training a pretrained language model using additional data. This causes the model to start representing and mimicking the patterns and characteristics of the fine-tuning dataset. Claude is not a bare language model; it has already been fine-tuned to be a helpful assistant. Our API does not currently offer fine-tuning, but please ask your Anthropic contact if you are interested in exploring this option. Fine-tuning can be useful for adapting a language model to a specific domain, task, or writing style, but it requires careful consideration of the fine-tuning data and the potential impact on the model's performance and biases.

## HHH

These three H's represent Anthropic's goals in ensuring that Claude is beneficial to society:

* A **helpful** AI will attempt to perform the task or answer the question posed to the best of its abilities, providing relevant and useful information.
* An **honest** AI will give accurate information, and not hallucinate or confabulate. It will acknowledge its limitations and uncertainties when appropriate.
* A **harmless** AI will not be offensive or discriminatory, and when asked to aid in a dangerous or unethical act, the AI should politely refuse and explain why it cannot comply.

## Latency

Latency, in the context of generative AI and large language models, refers to the time it takes for the model to respond to a given prompt. It is the delay between submitting a prompt and receiving the generated output. Lower latency indicates faster response times, which is crucial for real-time applications, chatbots, and interactive experiences. Factors that can affect latency include model size, hardware capabilities, network conditions, and the complexity of the prompt and the generated response.

## LLM

Large language models (LLMs) are AI language models with many parameters that are capable of performing a variety of surprisingly useful tasks. These models are trained on vast amounts of text data and can generate human-like text, answer questions, summarize information, and more. Claude is a conversational assistant based on a large language model that has been fine-tuned and trained using RLHF to be more helpful, honest, and harmless.

## MCP (Model Context Protocol)

Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs. Like a USB-C port for AI applications, MCP provides a unified way to connect AI models to different data sources and tools. MCP enables AI systems to maintain consistent context across interactions and access external resources in a standardized manner. See our [MCP documentation](/en/docs/mcp) to learn more.

## MCP connector

The MCP connector is a feature that allows API users to connect to MCP servers directly from the Messages API without building an MCP client. This enables seamless integration with MCP-compatible tools and services through the Claude API. The MCP connector supports features like tool calling and is available in public beta. See our [MCP connector documentation](/en/docs/agents-and-tools/mcp-connector) to learn more.

## Pretraining

Pretraining is the initial process of training language models on a large unlabeled corpus of text. In Claude's case, autoregressive language models (like Claude's underlying model) are pretrained to predict the next word, given the previous context of text in the document. These pretrained models are not inherently good at answering questions or following instructions, and often require deep skill in prompt engineering to elicit desired behaviors. Fine-tuning and RLHF are used to refine these pretrained models, making them more useful for a wide range of tasks.

## RAG (Retrieval augmented generation)

Retrieval augmented generation (RAG) is a technique that combines information retrieval with language model generation to improve the accuracy and relevance of the generated text, and to better ground the model's response in evidence. In RAG, a language model is augmented with an external knowledge base or a set of documents that is passed into the context window. The data is retrieved at run time when a query is sent to the model, although the model itself does not necessarily retrieve the data (but can with [tool use](/en/docs/agents-and-tools/tool-use/overview) and a retrieval function). When generating text, relevant information first must be retrieved from the knowledge base based on the input prompt, and then passed to the model along with the original query. The model uses this information to guide the output it generates. This allows the model to access and utilize information beyond its training data, reducing the reliance on memorization and improving the factual accuracy of the generated text. RAG can be particularly useful for tasks that require up-to-date information, domain-specific knowledge, or explicit citation of sources. However, the effectiveness of RAG depends on the quality and relevance of the external knowledge base and the knowledge that is retrieved at runtime.

## RLHF

Reinforcement Learning from Human Feedback (RLHF) is a technique used to train a pretrained language model to behave in ways that are consistent with human preferences. This can include helping the model follow instructions more effectively or act more like a chatbot. Human feedback consists of ranking a set of two or more example texts, and the reinforcement learning process encourages the model to prefer outputs that are similar to the higher-ranked ones. Claude has been trained using RLHF to be a more helpful assistant. For more details, you can read [Anthropic's paper on the subject](https://arxiv.org/abs/2204.05862).

## Temperature

Temperature is a parameter that controls the randomness of a model's predictions during text generation. Higher temperatures lead to more creative and diverse outputs, allowing for multiple variations in phrasing and, in the case of fiction, variation in answers as well. Lower temperatures result in more conservative and deterministic outputs that stick to the most probable phrasing and answers. Adjusting the temperature enables users to encourage a language model to explore rare, uncommon, or surprising word choices and sequences, rather than only selecting the most likely predictions.

## TTFT (Time to first token)

Time to First Token (TTFT) is a performance metric that measures the time it takes for a language model to generate the first token of its output after receiving a prompt. It is an important indicator of the model's responsiveness and is particularly relevant for interactive applications, chatbots, and real-time systems where users expect quick initial feedback. A lower TTFT indicates that the model can start generating a response faster, providing a more seamless and engaging user experience. Factors that can influence TTFT include model size, hardware capabilities, network conditions, and the complexity of the prompt.

## Tokens

Tokens are the smallest individual units of a language model, and can correspond to words, subwords, characters, or even bytes (in the case of Unicode). For Claude, a token approximately represents 3.5 English characters, though the exact number can vary depending on the language used. Tokens are typically hidden when interacting with language models at the "text" level but become relevant when examining the exact inputs and outputs of a language model. When Claude is provided with text to evaluate, the text (consisting of a series of characters) is encoded into a series of tokens for the model to process. Larger tokens enable data efficiency during inference and pretraining (and are utilized when possible), while smaller tokens allow a model to handle uncommon or never-before-seen words. The choice of tokenization method can impact the model's performance, vocabulary size, and ability to handle out-of-vocabulary words.


# Content moderation
Source: https://docs.claude.com/en/docs/about-claude/use-case-guides/content-moderation

Content moderation is a critical aspect of maintaining a safe, respectful, and productive environment in digital applications. In this guide, we'll discuss how Claude can be used to moderate content within your digital application.

> Visit our [content moderation cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fmoderation%5Ffilter.ipynb) to see an example content moderation implementation using Claude.

<Tip>This guide is focused on moderating user-generated content within your application. If you're looking for guidance on moderating interactions with Claude, please refer to our [guardrails guide](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations).</Tip>

## Before building with Claude

### Decide whether to use Claude for content moderation

Here are some key indicators that you should use an LLM like Claude instead of a traditional ML or rules-based approach for content moderation:

<AccordionGroup>
  <Accordion title="You want a cost-effective and rapid implementation">Traditional ML methods require significant engineering resources, ML expertise, and infrastructure costs. Human moderation systems incur even higher costs. With Claude, you can have a sophisticated moderation system up and running in a fraction of the time for a fraction of the price.</Accordion>
  <Accordion title="You desire both semantic understanding and quick decisions">Traditional ML approaches, such as bag-of-words models or simple pattern matching, often struggle to understand the tone, intent, and context of the content. While human moderation systems excel at understanding semantic meaning, they require time for content to be reviewed. Claude bridges the gap by combining semantic understanding with the ability to deliver moderation decisions quickly.</Accordion>
  <Accordion title="You need consistent policy decisions">By leveraging its advanced reasoning capabilities, Claude can interpret and apply complex moderation guidelines uniformly. This consistency helps ensure fair treatment of all content, reducing the risk of inconsistent or biased moderation decisions that can undermine user trust.</Accordion>
  <Accordion title="Your moderation policies are likely to change or evolve over time">Once a traditional ML approach has been established, changing it is a laborious and data-intensive undertaking. On the other hand, as your product or customer needs evolve, Claude can easily adapt to changes or additions to moderation policies without extensive relabeling of training data.</Accordion>
  <Accordion title="You require interpretable reasoning for your moderation decisions">If you wish to provide users or regulators with clear explanations behind moderation decisions, Claude can generate detailed and coherent justifications. This transparency is important for building trust and ensuring accountability in content moderation practices.</Accordion>
  <Accordion title="You need multilingual support without maintaining separate models">Traditional ML approaches typically require separate models or extensive translation processes for each supported language. Human moderation requires hiring a workforce fluent in each supported language. Claude’s multilingual capabilities allow it to classify tickets in various languages without the need for separate models or extensive translation processes, streamlining moderation for global customer bases.</Accordion>
  <Accordion title="You require multimodal support">Claude's multimodal capabilities allow it to analyze and interpret content across both text and images. This makes it a versatile tool for comprehensive content moderation in environments where different media types need to be evaluated together.</Accordion>
</AccordionGroup>

<Note>Anthropic has trained all Claude models to be honest, helpful and harmless. This may result in Claude moderating content deemed particularly dangerous (in line with our [Acceptable Use Policy](https://www.anthropic.com/legal/aup)), regardless of the prompt used. For example, an adult website that wants to allow users to post explicit sexual content may find that Claude still flags explicit content as requiring moderation, even if they specify in their prompt not to moderate explicit sexual content. We recommend reviewing our AUP in advance of building a moderation solution.</Note>

### Generate examples of content to moderate

Before developing a content moderation solution, first create examples of content that should be flagged and content that should not be flagged. Ensure that you include edge cases and challenging scenarios that may be difficult for a content moderation system to handle effectively. Afterwards, review your examples to create a well-defined list of moderation categories.
For instance, the examples generated by a social media platform might include the following:

```python  theme={null}
allowed_user_comments = [
    'This movie was great, I really enjoyed it. The main actor really killed it!',
    'I hate Mondays.',
    'It is a great time to invest in gold!'
]

disallowed_user_comments = [
    'Delete this post now or you better hide. I am coming after you and your family.',
    'Stay away from the 5G cellphones!! They are using 5G to control you.',
    'Congratulations! You have won a $1,000 gift card. Click here to claim your prize!'
]

# Sample user comments to test the content moderation
user_comments = allowed_user_comments + disallowed_user_comments

# List of categories considered unsafe for content moderation
unsafe_categories = [
    'Child Exploitation',
    'Conspiracy Theories',
    'Hate',
    'Indiscriminate Weapons', 
    'Intellectual Property',
    'Non-Violent Crimes', 
    'Privacy',
    'Self-Harm',
    'Sex Crimes',
    'Sexual Content',
    'Specialized Advice',
    'Violent Crimes'
]
```

Effectively moderating these examples requires a nuanced understanding of language. In the comment, `This movie was great, I really enjoyed it. The main actor really killed it!`, the content moderation system needs to recognize that "killed it" is a metaphor, not an indication of actual violence. Conversely, despite the lack of explicit mentions of violence, the comment `Delete this post now or you better hide. I am coming after you and your family.` should be flagged by the content moderation system.

The `unsafe_categories` list can be customized to fit your specific needs. For example, if you wish to prevent minors from creating content on your website, you could append "Underage Posting" to the list.

***

## How to moderate content using Claude

### Select the right Claude model

When selecting a model, it’s important to consider the size of your data. If costs are a concern, a smaller model like Claude Haiku 3 is an excellent choice due to its cost-effectiveness. Below is an estimate of the cost to moderate text for a social media platform that receives one billion posts per month:

* **Content size**
  * Posts per month: 1bn
  * Characters per post: 100
  * Total characters: 100bn

* **Estimated tokens**
  * Input tokens: 28.6bn (assuming 1 token per 3.5 characters)
  * Percentage of messages flagged: 3%
  * Output tokens per flagged message: 50
  * Total output tokens: 1.5bn

* **Claude Haiku 3 estimated cost**
  * Input token cost: 2,860 MTok \* \$0.25/MTok = \$715
  * Output token cost: 1,500 MTok \* \$1.25/MTok = \$1,875
  * Monthly cost: \$715 + \$1,875 = \$2,590

* **Claude Sonnet 4.5 estimated cost**
  * Input token cost: 2,860 MTok \* \$3.00/MTok = \$8,580
  * Output token cost: 1,500 MTok \* \$15.00/MTok = \$22,500
  * Monthly cost: \$8,580 + \$22,500 = \$31,080

<Tip>Actual costs may differ from these estimates. These estimates are based on the prompt highlighted in the section on [batch processing](#consider-batch-processing). Output tokens can be reduced even further by removing the `explanation` field from the response.</Tip>

### Build a strong prompt

In order to use Claude for content moderation, Claude must understand the moderation requirements of your application. Let’s start by writing a prompt that allows you to define your moderation needs:

```python  theme={null}
import anthropic
import json

# Initialize the Anthropic client
client = anthropic.Anthropic()

def moderate_message(message, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)
    
    # Construct the prompt for Claude, including the message and unsafe categories
    assessment_prompt = f"""
    Determine whether the following message warrants moderation, 
    based on the unsafe categories outlined below.
    
    Message:
    <message>{message}</message>

    Unsafe Categories:
    <categories>
    {unsafe_category_str}
    </categories>

    Respond with ONLY a JSON object, using the format below:
    {{
    "violation": <Boolean field denoting whether the message should be moderated>,
    "categories": [Comma-separated list of violated categories],
    "explanation": [Optional. Only include if there is a violation.]
    }}"""

    # Send the request to Claude for content moderation
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=200,
        temperature=0,   # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )
    
    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)
    
    # Extract the violation status from the assessment
    contains_violation = assessment['violation']
    
    # If there's a violation, get the categories and explanation; otherwise, use empty defaults
    violated_categories = assessment.get('categories', []) if contains_violation else []
    explanation = assessment.get('explanation') if contains_violation else None
    
    return contains_violation, violated_categories, explanation

# Process each comment and print the results
for comment in user_comments:
    print(f"\nComment: {comment}")
    violation, violated_categories, explanation = moderate_message(comment, unsafe_categories)
    
    if violation:
        print(f"Violated Categories: {', '.join(violated_categories)}")
        print(f"Explanation: {explanation}")
    else:
        print("No issues detected.")
```

In this example, the `moderate_message` function contains an assessment prompt that includes the unsafe content categories and the message we wish to evaluate. The prompt asks Claude to assess whether the message should be moderated, based on the unsafe categories we defined.

The model's assessment is then parsed to determine if there is a violation. If there is a violation, Claude also returns a list of violated categories, as well as an explanation as to why the message is unsafe.

### Evaluate your prompt

Content moderation is a classification problem. Thus, you can use the same techniques outlined in our [classification cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb) to determine the accuracy of your content moderation system.

One additional consideration is that instead of treating content moderation as a binary classification problem, you may instead create multiple categories to represent various risk levels. Creating multiple risk levels allows you to adjust the aggressiveness of your moderation. For example, you might want to automatically block user queries that are deemed high risk, while users with many medium risk queries are flagged for human review.

```python  theme={null}
import anthropic
import json

# Initialize the Anthropic client
client = anthropic.Anthropic()

def assess_risk_level(message, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)
    
    # Construct the prompt for Claude, including the message, unsafe categories, and risk level definitions
    assessment_prompt = f"""
    Assess the risk level of the following message warrants moderation, 
    based on the unsafe categories listed below.
    
Message:
<message>{message}</message>

Unsafe Categories:
<categories>
{unsafe_category_str}
</categories>

Assign a risk level based on your confidence that the user's message should be moderated 
based on the defined unsafe categories:

0 - No risk
1 - Low risk
2 - Medium risk
3 - High risk

Respond with ONLY a JSON object, using the format below:
{{
  "risk_level": <Numerical field denoting the risk level>,
  "categories": [Comma-separated list of violated categories],
  "explanation": <Optional. Only include if risk level is greater than 0>
}}"""

    # Send the request to Claude for risk assessment
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=200,
        temperature=0,   # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )
    
    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)
    
    # Extract the risk level, violated categories, and explanation from the assessment
    risk_level = assessment["risk_level"]
    violated_categories = assessment["categories"]
    explanation = assessment.get("explanation")
    
    return risk_level, violated_categories, explanation

# Process each comment and print the results
for comment in user_comments:
    print(f"\nComment: {comment}")
    risk_level, violated_categories, explanation = assess_risk_level(comment, unsafe_categories)
    
    print(f"Risk Level: {risk_level}")
    if violated_categories:
        print(f"Violated Categories: {', '.join(violated_categories)}")
    if explanation:
        print(f"Explanation: {explanation}")
```

This code implements an `assess_risk_level` function that uses Claude to evaluate the risk level of a message. The function accepts a message and a list of unsafe categories as inputs.

Within the function, a prompt is generated for Claude, including the message to be assessed, the unsafe categories, and specific instructions for evaluating the risk level. The prompt instructs Claude to respond with a JSON object that includes the risk level, the violated categories, and an optional explanation.

This approach enables flexible content moderation by assigning risk levels. It can be seamlessly integrated into a larger system to automate content filtering or flag comments for human review based on their assessed risk level. For instance, when executing this code, the comment `Delete this post now or you better hide. I am coming after you and your family.` is identified as high risk due to its dangerous threat. Conversely, the comment `Stay away from the 5G cellphones!! They are using 5G to control you.` is categorized as medium risk.

### Deploy your prompt

Once you are confident in the quality of your solution, it's time to deploy it to production. Here are some best practices to follow when using content moderation in production:

1. **Provide clear feedback to users:** When user input is blocked or a response is flagged due to content moderation, provide informative and constructive feedback to help users understand why their message was flagged and how they can rephrase it appropriately. In the coding examples above, this is done through the `explanation` tag in the Claude response.

2. **Analyze moderated content:** Keep track of the types of content being flagged by your moderation system to identify trends and potential areas for improvement.

3. **Continuously evaluate and improve:** Regularly assess the performance of your content moderation system using metrics such as precision and recall tracking. Use this data to iteratively refine your moderation prompts, keywords, and assessment criteria.

***

## Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/en/docs/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:

### Define topics and provide examples

In addition to listing the unsafe categories in the prompt, further improvements can be made by providing definitions and phrases related to each category.

```python  theme={null}
import anthropic
import json

# Initialize the Anthropic client
client = anthropic.Anthropic()

# Dictionary of categories considered unsafe for content moderation, with their definitions
unsafe_category_definitions = {
    'Child Exploitation': 'Content that depicts child nudity or that enables, encourages, excuses, or depicts the sexual abuse of children.',
    'Conspiracy Theories': """Content that promotes or endorses unfounded, false, or misleading theories about events, situations, or individuals, 
        which can incite harm or undermine public trust in institutions or facts.""",
    'Hate': """Content that is hateful toward people on the basis of their protected characteristics 
        (race, color, ethnicity, national origin, disability, religious affiliation, caste, sexual orientation, sex, gender identity and serious disease), 
        or content that perpetuates negative stereotypes.""",
    'Indiscriminate Weapons': 'Content that enables the creation of weapons of mass destruction.', 
    'Intellectual Property': 'Content that violates the intellectual property rights of third parties.',
    'Non-Violent Crimes': 'Content that enables, encourages, or excuses the commission of non-violent crimes.', 
    'Privacy': 'Content that contains sensitive, personal information about private individuals.',
    'Self-Harm': 'Content that enables, encourages, or excuses acts of intentional self-harm.',
    'Sex Crimes': 'Content that enables, encourages, or excuses the commission of sex crimes.',
    'Sexual Content': 'Content that contains erotic descriptions or explicit depictions of sex acts.',
    'Specialized Advice': """Content that contains financial, medical, or legal advice. 
        Financial advice includes guidance on investments, stocks, bonds, or any financial planning.""",
    'Violent Crimes': 'Content that enables, encourages, or excuses the commission of violent crimes.', 
}


def moderate_message_with_definitions(message, unsafe_category_definitions):
    # Format unsafe categories string, with each category and its definition on a new line
    unsafe_category_str = '\n'.join(f'{category}: {definition}' 
        for category, definition in unsafe_category_definitions.items()
    )
    
    # Construct the prompt for Claude, including the message and unsafe categories
    assessment_prompt = f"""Determine whether the following message warrants moderation, based on the unsafe categories outlined below.

Message:
<message>{message}</message>

Unsafe Categories and Their Definitions:
<categories>
{unsafe_category_str}
</categories>

It's important that you remember all unsafe categories and their definitions.

Respond with ONLY a JSON object, using the format below:
{{
  "violation": <Boolean field denoting whether the message should be moderated>,
  "categories": [Comma-separated list of violated categories],
  "explanation": [Optional. Only include if there is a violation.]
}}"""

    # Send the request to Claude for content moderation
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=200,
        temperature=0,   # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )
    
    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)
    
    # Extract the violation status from the assessment
    contains_violation = assessment['violation']
    
    # If there's a violation, get the categories and explanation; otherwise, use empty defaults
    violated_categories = assessment.get('categories', []) if contains_violation else []
    explanation = assessment.get('explanation') if contains_violation else None
    
    return contains_violation, violated_categories, explanation


# Process each comment and print the results
for comment in user_comments:
    print(f"\nComment: {comment}")
    violation, violated_categories, explanation = moderate_message_with_definitions(comment, unsafe_category_definitions)
    
    if violation:
        print(f"Violated Categories: {', '.join(violated_categories)}")
        print(f"Explanation: {explanation}")
    else:
        print("No issues detected.")
```

The `moderate_message_with_definitions` function expands upon the earlier `moderate_message` function by allowing each unsafe category to be paired with a detailed definition. This occurs in the code by replacing the `unsafe_categories` list from the original function with an `unsafe_category_definitions` dictionary. This dictionary maps each unsafe category to its corresponding definition. Both the category names and their definitions are included in the prompt.

Notably, the definition for the `Specialized Advice` category now specifies the types of financial advice that should be prohibited. As a result, the comment `It's a great time to invest in gold!`, which previously passed the `moderate_message` assessment, now triggers a violation.

### Consider batch processing

To reduce costs in situations where real-time moderation isn't necessary, consider moderating messages in batches. Include multiple messages within the prompt's context, and ask Claude to assess which messages should be moderated.

```python  theme={null}
import anthropic
import json

# Initialize the Anthropic client
client = anthropic.Anthropic()

def batch_moderate_messages(messages, unsafe_categories):
    # Convert the list of unsafe categories into a string, with each category on a new line
    unsafe_category_str = '\n'.join(unsafe_categories)
    
    # Format messages string, with each message wrapped in XML-like tags and given an ID
    messages_str = '\n'.join([f'<message id={idx}>{msg}</message>' for idx, msg in enumerate(messages)])
    
    # Construct the prompt for Claude, including the messages and unsafe categories
    assessment_prompt = f"""Determine the messages to moderate, based on the unsafe categories outlined below.

Messages:
<messages>
{messages_str}
</messages>

Unsafe categories and their definitions:
<categories>
{unsafe_category_str}
</categories>

Respond with ONLY a JSON object, using the format below:
{{
  "violations": [
    {{
      "id": <message id>,
      "categories": [list of violated categories],
      "explanation": <Explanation of why there's a violation>
    }},
    ...
  ]
}}

Important Notes:
- Remember to analyze every message for a violation.
- Select any number of violations that reasonably apply."""

    # Send the request to Claude for content moderation
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the Haiku model for lower costs
        max_tokens=2048,  # Increased max token count to handle batches
        temperature=0,    # Use 0 temperature for increased consistency
        messages=[
            {"role": "user", "content": assessment_prompt}
        ]
    )
    
    # Parse the JSON response from Claude
    assessment = json.loads(response.content[0].text)
    return assessment


# Process the batch of comments and get the response
response_obj = batch_moderate_messages(user_comments, unsafe_categories)

# Print the results for each detected violation
for violation in response_obj['violations']:
    print(f"""Comment: {user_comments[violation['id']]}
Violated Categories: {', '.join(violation['categories'])}
Explanation: {violation['explanation']}
""")
```

In this example, the `batch_moderate_messages` function handles the moderation of an entire batch of messages with a single Claude API call.
Inside the function, a prompt is created that includes the list of messages to evaluate, the defined unsafe content categories, and their descriptions. The prompt directs Claude to return a JSON object listing all messages that contain violations. Each message in the response is identified by its id, which corresponds to the message's position in the input list.
Keep in mind that finding the optimal batch size for your specific needs may require some experimentation. While larger batch sizes can lower costs, they might also lead to a slight decrease in quality. Additionally, you may need to increase the `max_tokens` parameter in the Claude API call to accommodate longer responses. For details on the maximum number of tokens your chosen model can output, refer to the [model comparison page](/en/docs/about-claude/models#model-comparison-table).

<CardGroup cols={2}>
  <Card title="Content moderation cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fmoderation%5Ffilter.ipynb">
    View a fully implemented code-based example of how to use Claude for content moderation.
  </Card>

  <Card title="Guardrails guide" icon="link" href="/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations">
    Explore our guardrails guide for techniques to moderate interactions with Claude.
  </Card>
</CardGroup>


# Customer support agent
Source: https://docs.claude.com/en/docs/about-claude/use-case-guides/customer-support-chat

This guide walks through how to leverage Claude's advanced conversational capabilities to handle customer inquiries in real time, providing 24/7 support, reducing wait times, and managing high support volumes with accurate responses and positive interactions.

## Before building with Claude

### Decide whether to use Claude for support chat

Here are some key indicators that you should employ an LLM like Claude to automate portions of your customer support process:

<AccordionGroup>
  <Accordion title="High volume of repetitive queries">
    Claude excels at handling a large number of similar questions efficiently, freeing up human agents for more complex issues.
  </Accordion>

  <Accordion title="Need for quick information synthesis">
    Claude can quickly retrieve, process, and combine information from vast knowledge bases, while human agents may need time to research or consult multiple sources.
  </Accordion>

  <Accordion title="24/7 availability requirement">
    Claude can provide round-the-clock support without fatigue, whereas staffing human agents for continuous coverage can be costly and challenging.
  </Accordion>

  <Accordion title="Rapid scaling during peak periods">
    Claude can handle sudden increases in query volume without the need for hiring and training additional staff.
  </Accordion>

  <Accordion title="Consistent brand voice">
    You can instruct Claude to consistently represent your brand's tone and values, whereas human agents may vary in their communication styles.
  </Accordion>
</AccordionGroup>

Some considerations for choosing Claude over other LLMs:

* You prioritize natural, nuanced conversation: Claude's sophisticated language understanding allows for more natural, context-aware conversations that feel more human-like than chats with other LLMs.
* You often receive complex and open-ended queries: Claude can handle a wide range of topics and inquiries without generating canned responses or requiring extensive programming of permutations of user utterances.
* You need scalable multilingual support: Claude's multilingual capabilities allow it to engage in conversations in over 200 languages without the need for separate chatbots or extensive translation processes for each supported language.

### Define your ideal chat interaction

Outline an ideal customer interaction to define how and when you expect the customer to interact with Claude. This outline will help to determine the technical requirements of your solution.

Here is an example chat interaction for car insurance customer support:

* **Customer**: Initiates support chat experience
  * **Claude**: Warmly greets customer and initiates conversation
* **Customer**: Asks about insurance for their new electric car
  * **Claude**: Provides relevant information about electric vehicle coverage
* **Customer**: Asks questions related to unique needs for electric vehicle insurances
  * **Claude**: Responds with accurate and informative answers and provides links to the sources
* **Customer**: Asks off-topic questions unrelated to insurance or cars
  * **Claude**: Clarifies it does not discuss unrelated topics and steers the user back to car insurance
* **Customer**: Expresses interest in an insurance quote
  * **Claude**: Ask a set of questions to determine the appropriate quote, adapting to their responses
  * **Claude**: Sends a request to use the quote generation API tool along with necessary information collected from the user
  * **Claude**: Receives the response information from the API tool use, synthesizes the information into a natural response, and presents the provided quote to the user
* **Customer**: Asks follow up questions
  * **Claude**: Answers follow up questions as needed
  * **Claude**: Guides the customer to the next steps in the insurance process and closes out the conversation

<Tip>In the real example that you write for your own use case, you might find it useful to write out the actual words in this interaction so that you can also get a sense of the ideal tone, response length, and level of detail you want Claude to have.</Tip>

### Break the interaction into unique tasks

Customer support chat is a collection of multiple different tasks, from question answering to information retrieval to taking action on requests, wrapped up in a single customer interaction. Before you start building, break down your ideal customer interaction into every task you want Claude to be able to perform. This ensures you can prompt and evaluate Claude for every task, and gives you a good sense of the range of interactions you need to account for when writing test cases.

<Tip>Customers sometimes find it helpful to visualize this as an interaction flowchart of possible conversation inflection points depending on user requests.</Tip>

Here are the key tasks associated with the example insurance interaction above:

1. Greeting and general guidance
   * Warmly greet the customer and initiate conversation
   * Provide general information about the company and interaction

2. Product Information
   * Provide information about electric vehicle coverage
     <Note>This will require that Claude have the necessary information in its context, and might imply that a [RAG integration](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/retrieval_augmented_generation/guide.ipynb) is necessary.</Note>
   * Answer questions related to unique electric vehicle insurance needs
   * Answer follow-up questions about the quote or insurance details
   * Offer links to sources when appropriate

3. Conversation Management
   * Stay on topic (car insurance)
   * Redirect off-topic questions back to relevant subjects

4. Quote Generation
   * Ask appropriate questions to determine quote eligibility
   * Adapt questions based on customer responses
   * Submit collected information to quote generation API
   * Present the provided quote to the customer

### Establish success criteria

Work with your support team to [define clear success criteria](/en/docs/test-and-evaluate/define-success) and write [detailed evaluations](/en/docs/test-and-evaluate/develop-tests) with measurable benchmarks and goals.

Here are criteria and benchmarks that can be used to evaluate how successfully Claude performs the defined tasks:

<AccordionGroup>
  <Accordion title="Query comprehension accuracy">
    This metric evaluates how accurately Claude understands customer inquiries across various topics. Measure this by reviewing a sample of conversations and assessing whether Claude has the correct interpretation of customer intent, critical next steps, what successful resolution looks like, and more. Aim for a comprehension accuracy of 95% or higher.
  </Accordion>

  <Accordion title="Response relevance">
    This assesses how well Claude's response addresses the customer's specific question or issue. Evaluate a set of conversations and rate the relevance of each response (using LLM-based grading for scale). Target a relevance score of 90% or above.
  </Accordion>

  <Accordion title="Response accuracy">
    Assess the correctness of general company and product information provided to the user, based on the information provided to Claude in context. Target 100% accuracy in this introductory information.
  </Accordion>

  <Accordion title="Citation provision relevance">
    Track the frequency and relevance of links or sources offered. Target providing relevant sources in 80% of interactions where additional information could be beneficial.
  </Accordion>

  <Accordion title="Topic adherence">
    Measure how well Claude stays on topic, such as the topic of car insurance in our example implementation. Aim for 95% of responses to be directly related to car insurance or the customer's specific query.
  </Accordion>

  <Accordion title="Content generation effectiveness">
    Measure how successful Claude is at determining when to generate informational content and how relevant that content is. For example, in our implementation, we would be determining how well Claude understands when to generate a quote and how accurate that quote is. Target 100% accuracy, as this is vital information for a successful customer interaction.
  </Accordion>

  <Accordion title="Escalation efficiency">
    This measures Claude's ability to recognize when a query needs human intervention and escalate appropriately. Track the percentage of correctly escalated conversations versus those that should have been escalated but weren't. Aim for an escalation accuracy of 95% or higher.
  </Accordion>
</AccordionGroup>

Here are criteria and benchmarks that can be used to evaluate the business impact of employing Claude for support:

<AccordionGroup>
  <Accordion title="Sentiment maintenance">
    This assesses Claude's ability to maintain or improve customer sentiment throughout the conversation. Use sentiment analysis tools to measure sentiment at the beginning and end of each conversation. Aim for maintained or improved sentiment in 90% of interactions.
  </Accordion>

  <Accordion title="Deflection rate">
    The percentage of customer inquiries successfully handled by the chatbot without human intervention. Typically aim for 70-80% deflection rate, depending on the complexity of inquiries.
  </Accordion>

  <Accordion title="Customer satisfaction score">
    A measure of how satisfied customers are with their chatbot interaction. Usually done through post-interaction surveys. Aim for a CSAT score of 4 out of 5 or higher.
  </Accordion>

  <Accordion title="Average handle time">
    The average time it takes for the chatbot to resolve an inquiry. This varies widely based on the complexity of issues, but generally, aim for a lower AHT compared to human agents.
  </Accordion>
</AccordionGroup>

## How to implement Claude as a customer service agent

### Choose the right Claude model

The choice of model depends on the trade-offs between cost, accuracy, and response time.

For customer support chat, `claude-opus-4-1-20250805` is well suited to balance intelligence, latency, and cost. However, for instances where you have conversation flow with multiple prompts including RAG, tool use, and/or long-context prompts, `claude-3-haiku-20240307` may be more suitable to optimize for latency.

### Build a strong prompt

Using Claude for customer support requires Claude having enough direction and context to respond appropriately, while having enough flexibility to handle a wide range of customer inquiries.

Let's start by writing the elements of a strong prompt, starting with a system prompt:

```python  theme={null}
IDENTITY = """You are Eva, a friendly and knowledgeable AI assistant for Acme Insurance 
Company. Your role is to warmly welcome customers and provide information on 
Acme's insurance offerings, which include car insurance and electric car 
insurance. You can also help customers get quotes for their insurance needs."""
```

<Tip>While you may be tempted to put all your information inside a system prompt as a way to separate instructions from the user conversation, Claude actually works best with the bulk of its prompt content written inside the first `User` turn (with the only exception being role prompting). Read more at [Giving Claude a role with a system prompt](/en/docs/build-with-claude/prompt-engineering/system-prompts).</Tip>

It's best to break down complex prompts into subsections and write one part at a time. For each task, you might find greater success by following a step by step process to define the parts of the prompt Claude would need to do the task well. For this car insurance customer support example, we'll be writing piecemeal all the parts for a prompt starting with the "Greeting and general guidance" task. This also makes debugging your prompt easier as you can more quickly adjust individual parts of the overall prompt.

We'll put all of these pieces in a file called `config.py`.

```python  theme={null}
STATIC_GREETINGS_AND_GENERAL = """
<static_context>
Acme Auto Insurance: Your Trusted Companion on the Road

About:
At Acme Insurance, we understand that your vehicle is more than just a mode of transportation—it's your ticket to life's adventures. 
Since 1985, we've been crafting auto insurance policies that give drivers the confidence to explore, commute, and travel with peace of mind.
Whether you're navigating city streets or embarking on cross-country road trips, Acme is there to protect you and your vehicle. 
Our innovative auto insurance policies are designed to adapt to your unique needs, covering everything from fender benders to major collisions.
With Acme's award-winning customer service and swift claim resolution, you can focus on the joy of driving while we handle the rest. 
We're not just an insurance provider—we're your co-pilot in life's journeys.
Choose Acme Auto Insurance and experience the assurance that comes with superior coverage and genuine care. Because at Acme, we don't just 
insure your car—we fuel your adventures on the open road.

Note: We also offer specialized coverage for electric vehicles, ensuring that drivers of all car types can benefit from our protection.

Acme Insurance offers the following products:
- Car insurance
- Electric car insurance
- Two-wheeler insurance

Business hours: Monday-Friday, 9 AM - 5 PM EST
Customer service number: 1-800-123-4567
</static_context>
"""
```

We'll then do the same for our car insurance and electric car insurance information.

```python  theme={null}
STATIC_CAR_INSURANCE="""
<static_context>
Car Insurance Coverage:
Acme's car insurance policies typically cover:
1. Liability coverage: Pays for bodily injury and property damage you cause to others.
2. Collision coverage: Pays for damage to your car in an accident.
3. Comprehensive coverage: Pays for damage to your car from non-collision incidents.
4. Medical payments coverage: Pays for medical expenses after an accident.
5. Uninsured/underinsured motorist coverage: Protects you if you're hit by a driver with insufficient insurance.

Optional coverages include:
- Rental car reimbursement
- Roadside assistance
- New car replacement
</static_context>
"""

STATIC_ELECTRIC_CAR_INSURANCE="""
<static_context>
Electric Car Insurance:
Our specialized electric car insurance goes beyond traditional auto coverage, 
offering tailored protection for your high-tech investment. In addition to standard coverages, we offer:
- Safeguarding expensive battery systems
- Covering home charging equipment
- Adapting to the rapidly evolving world of electric vehicles

Whether you're driving a Rivian, Nissan Leaf, Chevrolet Bolt, 
or any other electric vehicle, our knowledgeable agents are ready to craft a policy 
that gives you the confidence to enjoy every electron-powered mile.
</static_context>
"""
```

Now that we have our static content, let's add at least 4-5 sample "good" interactions to guide Claude's responses. These examples should be representative of your ideal customer interaction and can include guardrails, tool calls, etc.

```python  theme={null}
EXAMPLES="""
Here are a few examples of how you can interact with customers:

<example 1>
H: Hi, do you offer commercial insurance for small businesses?

A: Ah! Unfortunately, we don't offer commercial insurance at this time. 
However, we do provide a range of personal insurance products including car insurance and electric car insurance. 
Would you like to know more about these offerings?
</example 1>

<example 2>
H: Hi, what are your business hours?

A: Our business hours are Monday to Friday, 9 AM to 5 PM EST. 
If you have any questions or need assistance, feel free to reach out during those times. 
How else can I assist you today?
</example 2>

<example 3>
H: I'm shopping for car insurance. What does Acme offer?

A: Great choice! Acme's car insurance policies typically include:
- Liability coverage: Protects you if you're at fault in an accident
- Collision coverage: Pays for damage to your car in an accident
- Comprehensive coverage: Covers non-collision incidents like theft or vandalism
- Medical payments coverage: Pays for medical expenses after an accident
- Uninsured/underinsured motorist coverage: Protects you from drivers with insufficient insurance

We also offer optional coverages like rental car reimbursement, roadside assistance, and new car replacement. 
Would you like more details on any of these coverages, or do you have specific questions about insuring your vehicle?
</example 3>

<example 4>
H: I'd like to hear about your electric car insurance.

A: Certainly! Our electric car insurance is specially designed to meet the unique needs of electric vehicle owners. 
In addition to all the standard coverages we offer for regular cars, our electric car policies include:

- Battery coverage: Protection against damage or degradation of your vehicle's expensive battery system
- Tech package: Covers repairs or replacement of advanced electronics and onboard computer systems
- Charging station coverage: Protects both home and portable charging equipment
- Cybersecurity protection: Coverage against hacking or digital threats
- Specialized roadside assistance: Includes flatbed towing to protect the vehicle's undercarriage

We cover a wide range of electric vehicles, including popular models from Tesla, Rivian, Nissan, Chevrolet, and more. 
Is there a specific electric vehicle you're looking to insure, or would you like more details on any of these coverages?
</example 4>

<example 5>
H: I'd like to get a quote for my car insurance.

A: Certainly! I'd be happy to help you get a quote for your car insurance. 
To provide you with an accurate quote, I'll need to collect some information about your vehicle and the primary driver. 
Let's start with the basics:

1. What is the make and model of your vehicle?
2. What year was it manufactured?
3. Approximately how many miles have you driven?
4. What is the age of the primary driver?

Once you provide this information, I'll use our quoting tool to generate a personalized insurance quote for you.
</example 5>
"""
```

You will also want to include any important instructions outlining Do's and Don'ts for how Claude should interact with the customer.
This may draw from brand guardrails or support policies.

```python  theme={null}
ADDITIONAL_GUARDRAILS = """Please adhere to the following guardrails:
1. Only provide information about insurance types listed in our offerings.
2. If asked about an insurance type we don't offer, politely state 
that we don't provide that service.
3. Do not speculate about future product offerings or company plans.
4. Don't make promises or enter into agreements it's not authorized to make.
You only provide information and guidance.
5. Do not mention any competitor's products or services.
"""
```

Now let’s combine all these sections into a single string to use as our prompt.

```python  theme={null}
TASK_SPECIFIC_INSTRUCTIONS = ' '.join([
   STATIC_GREETINGS_AND_GENERAL,
   STATIC_CAR_INSURANCE,
   STATIC_ELECTRIC_CAR_INSURANCE,
   EXAMPLES,
   ADDITIONAL_GUARDRAILS,
])
```

### Add dynamic and agentic capabilities with tool use

Claude is capable of taking actions and retrieving information dynamically using client-side tool use functionality. Start by listing any external tools or APIs the prompt should utilize.

For this example, we will start with one tool for calculating the quote.

<Tip>As a reminder, this tool will not perform the actual calculation, it will just signal to the application that a tool should be used with whatever arguments specified.</Tip>

Example insurance quote calculator:

```python  theme={null}
TOOLS = [{
  "name": "get_quote",
  "description": "Calculate the insurance quote based on user input. Returned value is per month premium.",
  "input_schema": {
    "type": "object",
    "properties": {
      "make": {"type": "string", "description": "The make of the vehicle."},
      "model": {"type": "string", "description": "The model of the vehicle."},
      "year": {"type": "integer", "description": "The year the vehicle was manufactured."},
      "mileage": {"type": "integer", "description": "The mileage on the vehicle."},
      "driver_age": {"type": "integer", "description": "The age of the primary driver."}
    },
    "required": ["make", "model", "year", "mileage", "driver_age"]
  }
}]

def get_quote(make, model, year, mileage, driver_age):
    """Returns the premium per month in USD"""
    # You can call an http endpoint or a database to get the quote.
    # Here, we simulate a delay of 1 seconds and return a fixed quote of 100.
    time.sleep(1)
    return 100
```

### Deploy your prompts

It's hard to know how well your prompt works without deploying it in a test production setting and [running evaluations](/en/docs/test-and-evaluate/develop-tests) so let's build a small application using our prompt, the Anthropic SDK, and streamlit for a user interface.

In a file called `chatbot.py`, start by setting up the ChatBot class, which will encapsulate the interactions with the Anthropic SDK.

The class should have two main methods: `generate_message` and `process_user_input`.

```python  theme={null}
from anthropic import Anthropic
from config import IDENTITY, TOOLS, MODEL, get_quote
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
   def __init__(self, session_state):
       self.anthropic = Anthropic()
       self.session_state = session_state

   def generate_message(
       self,
       messages,
       max_tokens,
   ):
       try:
           response = self.anthropic.messages.create(
               model=MODEL,
               system=IDENTITY,
               max_tokens=max_tokens,
               messages=messages,
               tools=TOOLS,
           )
           return response
       except Exception as e:
           return {"error": str(e)}

   def process_user_input(self, user_input):
       self.session_state.messages.append({"role": "user", "content": user_input})

       response_message = self.generate_message(
           messages=self.session_state.messages,
           max_tokens=2048,
       )

       if "error" in response_message:
           return f"An error occurred: {response_message['error']}"

       if response_message.content[-1].type == "tool_use":
           tool_use = response_message.content[-1]
           func_name = tool_use.name
           func_params = tool_use.input
           tool_use_id = tool_use.id

           result = self.handle_tool_use(func_name, func_params)
           self.session_state.messages.append(
               {"role": "assistant", "content": response_message.content}
           )
           self.session_state.messages.append({
               "role": "user",
               "content": [{
                   "type": "tool_result",
                   "tool_use_id": tool_use_id,
                   "content": f"{result}",
               }],
           })

           follow_up_response = self.generate_message(
               messages=self.session_state.messages,
               max_tokens=2048,
           )

           if "error" in follow_up_response:
               return f"An error occurred: {follow_up_response['error']}"

           response_text = follow_up_response.content[0].text
           self.session_state.messages.append(
               {"role": "assistant", "content": response_text}
           )
           return response_text
      
       elif response_message.content[0].type == "text":
           response_text = response_message.content[0].text
           self.session_state.messages.append(
               {"role": "assistant", "content": response_text}
           )
           return response_text
      
       else:
           raise Exception("An error occurred: Unexpected response type")

   def handle_tool_use(self, func_name, func_params):
       if func_name == "get_quote":
           premium = get_quote(**func_params)
           return f"Quote generated: ${premium:.2f} per month"
      
       raise Exception("An unexpected tool was used")
```

### Build your user interface

Test deploying this code with Streamlit using a main method. This `main()` function sets up a Streamlit-based chat interface.

We'll do this in a file called `app.py`

```python  theme={null}
import streamlit as st
from chatbot import ChatBot
from config import TASK_SPECIFIC_INSTRUCTIONS

def main():
   st.title("Chat with Eva, Acme Insurance Company's Assistant🤖")

   if "messages" not in st.session_state:
       st.session_state.messages = [
           {'role': "user", "content": TASK_SPECIFIC_INSTRUCTIONS},
           {'role': "assistant", "content": "Understood"},
       ]

   chatbot = ChatBot(st.session_state)

   # Display user and assistant messages skipping the first two
   for message in st.session_state.messages[2:]:
       # ignore tool use blocks
       if isinstance(message["content"], str):
           with st.chat_message(message["role"]):
               st.markdown(message["content"])

   if user_msg := st.chat_input("Type your message here..."):
       st.chat_message("user").markdown(user_msg)

       with st.chat_message("assistant"):
           with st.spinner("Eva is thinking..."):
               response_placeholder = st.empty()
               full_response = chatbot.process_user_input(user_msg)
               response_placeholder.markdown(full_response)

if __name__ == "__main__":
   main()
```

Run the program with:

```
streamlit run app.py
```

### Evaluate your prompts

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate the chatbot performance using a systematic process combining quantitative and qualitative methods. Creating a [strong empirical evaluation](/en/docs/test-and-evaluate/develop-tests#building-evals-and-test-cases) based on your defined success criteria will allow you to optimize your prompts.

<Tip>The [Claude Console](https://console.anthropic.com/dashboard) now features an Evaluation tool that allows you to test your prompts under various scenarios.</Tip>

### Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/en/docs/build-with-claude/prompt-engineering/overview) & [guardrail implementation strategies](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). Here are some common scenarios:

#### Reduce long context latency with RAG

When dealing with large amounts of static and dynamic context, including all information in the prompt can lead to high costs, slower response times, and reaching context window limits. In this scenario, implementing Retrieval Augmented Generation (RAG) techniques can significantly improve performance and efficiency.

By using [embedding models like Voyage](/en/docs/build-with-claude/embeddings) to convert information into vector representations, you can create a more scalable and responsive system. This approach allows for dynamic retrieval of relevant information based on the current query, rather than including all possible context in every prompt.

Implementing RAG for support use cases [RAG recipe](https://github.com/anthropics/anthropic-cookbook/blob/82675c124e1344639b2a875aa9d3ae854709cd83/skills/classification/guide.ipynb) has been shown to increase accuracy, reduce response times, and reduce API costs in systems with extensive context requirements.

#### Integrate real-time data with tool use

When dealing with queries that require real-time information, such as account balances or policy details, embedding-based RAG approaches are not sufficient. Instead, you can leverage tool use to significantly enhance your chatbot's ability to provide accurate, real-time responses. For example, you can use tool use to look up customer information, retrieve order details, and cancel orders on behalf of the customer.

This approach, [outlined in our tool use: customer service agent recipe](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb), allows you to seamlessly integrate live data into your Claude's responses and provide a more personalized and efficient customer experience.

#### Strengthen input and output guardrails

When deploying a chatbot, especially in customer service scenarios, it's crucial to prevent risks associated with misuse, out-of-scope queries, and inappropriate responses. While Claude is inherently resilient to such scenarios, here are additional steps to strengthen your chatbot guardrails:

* [Reduce hallucination](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations): Implement fact-checking mechanisms and [citations](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/using_citations.ipynb) to ground responses in provided information.
* Cross-check information: Verify that the agent's responses align with your company's policies and known facts.
* Avoid contractual commitments: Ensure the agent doesn't make promises or enter into agreements it's not authorized to make.
* [Mitigate jailbreaks](/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks): Use methods like harmlessness screens and input validation to prevent users from exploiting model vulnerabilities, aiming to generate inappropriate content.
* Avoid mentioning competitors: Implement a competitor mention filter to maintain brand focus and not mention any competitor's products or services.
* [Keep Claude in character](/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character): Prevent Claude from changing their style of context, even during long, complex interactions.
* Remove Personally Identifiable Information (PII): Unless explicitly required and authorized, strip out any PII from responses.

#### Reduce perceived response time with streaming

When dealing with potentially lengthy responses, implementing streaming can significantly improve user engagement and satisfaction. In this scenario, users receive the answer progressively instead of waiting for the entire response to be generated.

Here is how to implement streaming:

1. Use the [Anthropic Streaming API](/en/docs/build-with-claude/streaming) to support streaming responses.
2. Set up your frontend to handle incoming chunks of text.
3. Display each chunk as it arrives, simulating real-time typing.
4. Implement a mechanism to save the full response, allowing users to view it if they navigate away and return.

In some cases, streaming enables the use of more advanced models with higher base latencies, as the progressive display mitigates the impact of longer processing times.

#### Scale your Chatbot

As the complexity of your Chatbot grows, your application architecture can evolve to match. Before you add further layers to your architecture, consider the following less exhaustive options:

* Ensure that you are making the most out of your prompts and optimizing through prompt engineering. Use our [prompt engineering guides](/en/docs/build-with-claude/prompt-engineering/overview) to write the most effective prompts.
* Add additional [tools](/en/docs/build-with-claude/tool-use) to the prompt (which can include [prompt chains](/en/docs/build-with-claude/prompt-engineering/chain-prompts)) and see if you can achieve the functionality required.

If your Chatbot handles incredibly varied tasks, you may want to consider adding a [separate intent classifier](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/classification/guide.ipynb) to route the initial customer query. For the existing application, this would involve creating a decision tree that would route customer queries through the classifier and then to specialized conversations (with their own set of tools and system prompts). Note, this method requires an additional call to Claude that can increase latency.

### Integrate Claude into your support workflow

While our examples have focused on Python functions callable within a Streamlit environment, deploying Claude for real-time support chatbot requires an API service.

Here's how you can approach this:

1. Create an API wrapper: Develop a simple API wrapper around your classification function. For example, you can use Flask API or Fast API to wrap your code into a HTTP Service. Your HTTP service could accept the user input and return the Assistant response in its entirety. Thus, your service could have the following characteristics:
   * Server-Sent Events (SSE): SSE allows for real-time streaming of responses from the server to the client. This is crucial for providing a smooth, interactive experience when working with LLMs.
   * Caching: Implementing caching can significantly improve response times and reduce unnecessary API calls.
   * Context retention: Maintaining context when a user navigates away and returns is important for continuity in conversations.

2. Build a web interface: Implement a user-friendly web UI for interacting with the Claude-powered agent.

<CardGroup cols={2}>
  <Card title="Retrieval Augmented Generation (RAG) cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/skills/retrieval_augmented_generation/guide.ipynb">
    Visit our RAG cookbook recipe for more example code and detailed guidance.
  </Card>

  <Card title="Citations cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/misc/using_citations.ipynb">
    Explore our Citations cookbook recipe for how to ensure accuracy and explainability of information.
  </Card>
</CardGroup>


# Legal summarization
Source: https://docs.claude.com/en/docs/about-claude/use-case-guides/legal-summarization

This guide walks through how to leverage Claude's advanced natural language processing capabilities to efficiently summarize legal documents, extracting key information and expediting legal research. With Claude, you can streamline the review of contracts, litigation prep, and regulatory work, saving time and ensuring accuracy in your legal processes.

> Visit our [summarization cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/guide.ipynb) to see an example legal summarization implementation using Claude.

## Before building with Claude

### Decide whether to use Claude for legal summarization

Here are some key indicators that you should employ an LLM like Claude to summarize legal documents:

<AccordionGroup>
  <Accordion title="You want to review a high volume of documents efficiently and affordably">Large-scale document review can be time-consuming and expensive when done manually. Claude can process and summarize vast amounts of legal documents rapidly, significantly reducing the time and cost associated with document review. This capability is particularly valuable for tasks like due diligence, contract analysis, or litigation discovery, where efficiency is crucial.</Accordion>
  <Accordion title="You require automated extraction of key metadata">Claude can efficiently extract and categorize important metadata from legal documents, such as parties involved, dates, contract terms, or specific clauses. This automated extraction can help organize information, making it easier to search, analyze, and manage large document sets. It's especially useful for contract management, compliance checks, or creating searchable databases of legal information. </Accordion>
  <Accordion title="You want to generate clear, concise, and standardized summaries">Claude can generate structured summaries that follow predetermined formats, making it easier for legal professionals to quickly grasp the key points of various documents. These standardized summaries can improve readability, facilitate comparison between documents, and enhance overall comprehension, especially when dealing with complex legal language or technical jargon.</Accordion>
  <Accordion title="You need precise citations for your summaries">When creating legal summaries, proper attribution and citation are crucial to ensure credibility and compliance with legal standards. Claude can be prompted to include accurate citations for all referenced legal points, making it easier for legal professionals to review and verify the summarized information.</Accordion>
  <Accordion title="You want to streamline and expedite your legal research process">Claude can assist in legal research by quickly analyzing large volumes of case law, statutes, and legal commentary. It can identify relevant precedents, extract key legal principles, and summarize complex legal arguments. This capability can significantly speed up the research process, allowing legal professionals to focus on higher-level analysis and strategy development.</Accordion>
</AccordionGroup>

### Determine the details you want the summarization to extract

There is no single correct summary for any given document. Without clear direction, it can be difficult for Claude to determine which details to include. To achieve optimal results, identify the specific information you want to include in the summary.

For instance, when summarizing a sublease agreement, you might wish to extract the following key points:

```python  theme={null}
details_to_extract = [
    'Parties involved (sublessor, sublessee, and original lessor)',
    'Property details (address, description, and permitted use)', 
    'Term and rent (start date, end date, monthly rent, and security deposit)',
    'Responsibilities (utilities, maintenance, and repairs)',
    'Consent and notices (landlord\'s consent, and notice requirements)',
    'Special provisions (furniture, parking, and subletting restrictions)'
]
```

### Establish success criteria

Evaluating the quality of summaries is a notoriously challenging task. Unlike many other natural language processing tasks, evaluation of summaries often lacks clear-cut, objective metrics. The process can be highly subjective, with different readers valuing different aspects of a summary. Here are criteria you may wish to consider when assessing how well Claude performs legal summarization.

<AccordionGroup>
  <Accordion title="Factual correctness">The summary should accurately represent the facts, legal concepts, and key points in the document.</Accordion>
  <Accordion title="Legal precision">Terminology and references to statutes, case law, or regulations must be correct and aligned with legal standards.</Accordion>
  <Accordion title="Conciseness"> The summary should condense the legal document to its essential points without losing important details.</Accordion>
  <Accordion title="Consistency">If summarizing multiple documents, the LLM should maintain a consistent structure and approach to each summary.</Accordion>
  <Accordion title="Readability">The text should be clear and easy to understand. If the audience is not legal experts, the summarization should not include legal jargon that could confuse the audience.</Accordion>
  <Accordion title="Bias and fairness">The summary should present an unbiased and fair depiction of the legal arguments and positions.</Accordion>
</AccordionGroup>

See our guide on [establishing success criteria](/en/docs/test-and-evaluate/define-success) for more information.

***

## How to summarize legal documents using Claude

### Select the right Claude model

Model accuracy is extremely important when summarizing legal documents. Claude Sonnet 4.5 is an excellent choice for use cases such as this where high accuracy is required. If the size and quantity of your documents is large such that costs start to become a concern, you can also try using a smaller model like Claude Haiku 4.5.

To help estimate these costs, below is a comparison of the cost to summarize 1,000 sublease agreements using both Sonnet and Haiku:

* **Content size**
  * Number of agreements: 1,000
  * Characters per agreement: 300,000
  * Total characters: 300M

* **Estimated tokens**
  * Input tokens: 86M (assuming 1 token per 3.5 characters)
  * Output tokens per summary: 350
  * Total output tokens: 350,000

* **Claude Sonnet 4.5 estimated cost**
  * Input token cost: 86 MTok \* \$3.00/MTok = \$258
  * Output token cost: 0.35 MTok \* \$15.00/MTok = \$5.25
  * Total cost: \$258.00 + \$5.25 = \$263.25

* **Claude Haiku 3 estimated cost**
  * Input token cost: 86 MTok \* \$0.25/MTok = \$21.50
  * Output token cost: 0.35 MTok \* \$1.25/MTok = \$0.44
  * Total cost: \$21.50 + \$0.44 = \$21.96

<Tip>Actual costs may differ from these estimates. These estimates are based on the example highlighted in the section on [prompting](#build-a-strong-prompt).</Tip>

### Transform documents into a format that Claude can process

Before you begin summarizing documents, you need to prepare your data. This involves extracting text from PDFs, cleaning the text, and ensuring it's ready to be processed by Claude.

Here is a demonstration of this process on a sample pdf:

```python  theme={null}
from io import BytesIO
import re

import pypdf
import requests

def get_llm_text(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in reader.pages])

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text) 

    # Remove page numbers
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text) 

    return text


# Create the full URL from the GitHub repository
url = "https://raw.githubusercontent.com/anthropics/anthropic-cookbook/main/skills/summarization/data/Sample Sublease Agreement.pdf"
url = url.replace(" ", "%20")

# Download the PDF file into memory
response = requests.get(url)

# Load the PDF from memory
pdf_file = BytesIO(response.content)

document_text = get_llm_text(pdf_file) 
print(document_text[:50000]) 
```

In this example, we first download a pdf of a sample sublease agreement used in the [summarization cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/data/Sample%20Sublease%20Agreement.pdf). This agreement was sourced from a publicly available sublease agreement from the [sec.gov website](https://www.sec.gov/Archives/edgar/data/1045425/000119312507044370/dex1032.htm).

We use the pypdf library to extract the contents of the pdf and convert it to text. The text data is then cleaned by removing extra whitespace and page numbers.

### Build a strong prompt

Claude can adapt to various summarization styles. You can change the details of the prompt to guide Claude to be more or less verbose, include more or less technical terminology, or provide a higher or lower level summary of the context at hand.

Here’s an example of how to create a prompt that ensures the generated summaries follow a consistent structure when analyzing sublease agreements:

```python  theme={null}
import anthropic

# Initialize the Anthropic client
client = anthropic.Anthropic()

def summarize_document(text, details_to_extract, model="claude-sonnet-4-5", max_tokens=1000):

    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = '\n'.join(details_to_extract)
    
    # Prompt the model to summarize the sublease agreement
    prompt = f"""Summarize the following sublease agreement. Focus on these key aspects:

    {details_to_extract_str}

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>
    
    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

    Sublease agreement text:
    {text}
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "Here is the summary of the sublease agreement: <summary>"}
        ],
        stop_sequences=["</summary>"]
    )

    return response.content[0].text

sublease_summary = summarize_document(document_text, details_to_extract)
print(sublease_summary)
```

This code implements a `summarize_document` function that uses Claude to summarize the contents of a sublease agreement. The function accepts a text string and a list of details to extract as inputs. In this example, we call the function with the `document_text` and `details_to_extract` variables that were defined in the previous code snippets.

Within the function, a prompt is generated for Claude, including the document to be summarized, the details to extract, and specific instructions for summarizing the document. The prompt instructs Claude to respond with a summary of each detail to extract nested within XML headers.

Because we decided to output each section of the summary within tags, each section can easily be parsed out as a post-processing step. This approach enables structured summaries that can be adapted for your use case, so that each summary follows the same pattern.

### Evaluate your prompt

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate the quality of your summaries using a systematic process combining quantitative and qualitative methods. Creating a [strong empirical evaluation](/en/docs/test-and-evaluate/develop-tests#building-evals-and-test-cases) based on your defined success criteria will allow you to optimize your prompts. Here are some metrics you may wish to include within your empirical evaluation:

<AccordionGroup>
  <Accordion title="ROUGE scores">This measures the overlap between the generated summary and an expert-created reference summary. This metric primarily focuses on recall and is useful for evaluating content coverage.</Accordion>
  <Accordion title="BLEU scores">While originally developed for machine translation, this metric can be adapted for summarization tasks. BLEU scores measure the precision of n-gram matches between the generated summary and reference summaries. A higher score indicates that the generated summary contains similar phrases and terminology to the reference summary. </Accordion>
  <Accordion title="Contextual embedding similarity">This metric involves creating vector representations (embeddings) of both the generated and reference summaries. The similarity between these embeddings is then calculated, often using cosine similarity. Higher similarity scores indicate that the generated summary captures the semantic meaning and context of the reference summary, even if the exact wording differs.</Accordion>
  <Accordion title="LLM-based grading">This method involves using an LLM such as Claude to evaluate the quality of generated summaries against a scoring rubric. The rubric can be tailored to your specific needs, assessing key factors like accuracy, completeness, and coherence. For guidance on implementing LLM-based grading, view these [tips](/en/docs/test-and-evaluate/develop-tests#tips-for-llm-based-grading).</Accordion>
  <Accordion title="Human evaluation">In addition to creating the reference summaries, legal experts can also evaluate the quality of the generated summaries. While this is expensive and time-consuming at scale, this is often done on a few summaries as a sanity check before deploying to production.</Accordion>
</AccordionGroup>

### Deploy your prompt

Here are some additional considerations to keep in mind as you deploy your solution to production.

1. **Ensure no liability:** Understand the legal implications of errors in the summaries, which could lead to legal liability for your organization or clients. Provide disclaimers or legal notices clarifying that the summaries are generated by AI and should be reviewed by legal professionals.

2. **Handle diverse document types:** In this guide, we’ve discussed how to extract text from PDFs. In the real-world, documents may come in a variety of formats (PDFs, Word documents, text files, etc.). Ensure your data extraction pipeline can convert all of the file formats you expect to receive.

3. **Parallelize API calls to Claude:** Long documents with a large number of tokens may require up to a minute for Claude to generate a summary. For large document collections, you may want to send API calls to Claude in parallel so that the summaries can be completed in a reasonable timeframe. Refer to Anthropic’s [rate limits](/en/api/rate-limits#rate-limits) to determine the maximum amount of API calls that can be performed in parallel.

***

## Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/en/docs/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:

### Perform meta-summarization to summarize long documents

Legal summarization often involves handling long documents or many related documents at once, such that you surpass Claude’s context window. You can use a chunking method known as meta-summarization in order to handle this use case. This technique involves breaking down documents into smaller, manageable chunks and then processing each chunk separately. You can then combine the summaries of each chunk to create a meta-summary of the entire document.

Here's an example of how to perform meta-summarization:

```python  theme={null}
import anthropic

# Initialize the Anthropic client
client = anthropic.Anthropic()

def chunk_text(text, chunk_size=20000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_long_document(text, details_to_extract, model="claude-sonnet-4-5", max_tokens=1000):

    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = '\n'.join(details_to_extract)

    # Iterate over chunks and summarize each one
    chunk_summaries = [summarize_document(chunk, details_to_extract, model=model, max_tokens=max_tokens) for chunk in chunk_text(text)]
    
    final_summary_prompt = f"""
    
    You are looking at the chunked summaries of multiple documents that are all related. 
    Combine the following summaries of the document from different truthful sources into a coherent overall summary:

    <chunked_summaries>
    {"".join(chunk_summaries)}
    </chunked_summaries>

    Focus on these key aspects:
    {details_to_extract_str})

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>
    
    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal expert that summarizes notes on one document.",
        messages=[
            {"role": "user",  "content": final_summary_prompt},
            {"role": "assistant", "content": "Here is the summary of the sublease agreement: <summary>"}

        ],
        stop_sequences=["</summary>"]
    )
    
    return response.content[0].text

long_summary = summarize_long_document(document_text, details_to_extract)
print(long_summary)
```

The `summarize_long_document` function builds upon the earlier `summarize_document` function by splitting the document into smaller chunks and summarizing each chunk individually.

The code achieves this by applying the `summarize_document` function to each chunk of 20,000 characters within the original document. The individual summaries are then combined, and a final summary is created from these chunk summaries.

Note that the `summarize_long_document` function isn’t strictly necessary for our example pdf, as the entire document fits within Claude’s context window. However, it becomes essential for documents exceeding Claude’s context window or when summarizing multiple related documents together. Regardless, this meta-summarization technique often captures additional important details in the final summary that were missed in the earlier single-summary approach.

### Use summary indexed documents to explore a large collection of documents

Searching a collection of documents with an LLM usually involves retrieval-augmented generation (RAG). However, in scenarios involving large documents or when precise information retrieval is crucial, a basic RAG approach may be insufficient. Summary indexed documents is an advanced RAG approach that provides a more efficient way of ranking documents for retrieval, using less context than traditional RAG methods. In this approach, you first use Claude to generate a concise summary for each document in your corpus, and then use Clade to rank the relevance of each summary to the query being asked. For further details on this approach, including a code-based example, check out the summary indexed documents section in the [summarization cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/guide.ipynb).

### Fine-tune Claude to learn from your dataset

Another advanced technique to improve Claude's ability to generate summaries is fine-tuning. Fine-tuning involves training Claude on a custom dataset that specifically aligns with your legal summarization needs, ensuring that Claude adapts to your use case. Here’s an overview on how to perform fine-tuning:

1. **Identify errors:** Start by collecting instances where Claude’s summaries fall short - this could include missing critical legal details, misunderstanding context, or using inappropriate legal terminology.

2. **Curate a dataset:** Once you've identified these issues, compile a dataset of these problematic examples. This dataset should include the original legal documents alongside your corrected summaries, ensuring that Claude learns the desired behavior.

3. **Perform fine-tuning:** Fine-tuning involves retraining the model on your curated dataset to adjust its weights and parameters. This retraining helps Claude better understand the specific requirements of your legal domain, improving its ability to summarize documents according to your standards.

4. **Iterative improvement:** Fine-tuning is not a one-time process. As Claude continues to generate summaries, you can iteratively add new examples where it has underperformed, further refining its capabilities. Over time, this continuous feedback loop will result in a model that is highly specialized for your legal summarization tasks.

<Tip>Fine-tuning is currently only available via Amazon Bedrock. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/).</Tip>

<CardGroup cols={2}>
  <Card title="Summarization cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/skills/summarization/guide.ipynb">
    View a fully implemented code-based example of how to use Claude to summarize contracts.
  </Card>

  <Card title="Citations cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/blob/main/misc/using_citations.ipynb">
    Explore our Citations cookbook recipe for guidance on how to ensure accuracy and explainability of information.
  </Card>
</CardGroup>


# Guides to common use cases
Source: https://docs.claude.com/en/docs/about-claude/use-case-guides/overview



Claude is designed to excel in a variety of tasks. Explore these in-depth production guides to learn how to build common use cases with Claude.

<CardGroup cols={2}>
  <Card title="Ticket routing" icon="headset" href="/en/docs/about-claude/use-case-guides/ticket-routing">
    Best practices for using Claude to classify and route customer support tickets at scale.
  </Card>

  <Card title="Customer support agent" icon="robot" href="/en/docs/about-claude/use-case-guides/customer-support-chat">
    Build intelligent, context-aware chatbots with Claude to enhance customer support interactions.
  </Card>

  <Card title="Content moderation" icon="shield-check" href="/en/docs/about-claude/use-case-guides/content-moderation">
    Techniques and best practices for using Claude to perform content filtering and general content moderation.
  </Card>

  <Card title="Legal summarization" icon="book" href="/en/docs/about-claude/use-case-guides/legal-summarization">
    Summarize legal documents using Claude to extract key information and expedite research.
  </Card>
</CardGroup>


# Ticket routing
Source: https://docs.claude.com/en/docs/about-claude/use-case-guides/ticket-routing

This guide walks through how to harness Claude's advanced natural language understanding capabilities to classify customer support tickets at scale based on customer intent, urgency, prioritization, customer profile, and more.

## Define whether to use Claude for ticket routing

Here are some key indicators that you should use an LLM like Claude  instead of traditional ML approaches for your classification task:

<AccordionGroup>
  <Accordion title="You have limited labeled training data available">
    Traditional ML processes require massive labeled datasets. Claude's pre-trained model can effectively classify tickets with just a few dozen labeled examples, significantly reducing data preparation time and costs.
  </Accordion>

  <Accordion title="Your classification categories are likely to change or evolve over time">
    Once a traditional ML approach has been established, changing it is a laborious and data-intensive undertaking. On the other hand, as your product or customer needs evolve, Claude can easily adapt to changes in class definitions or new classes without extensive relabeling of training data.
  </Accordion>

  <Accordion title="You need to handle complex, unstructured text inputs">
    Traditional ML models often struggle with unstructured data and require extensive feature engineering. Claude's advanced language understanding allows for accurate classification based on content and context, rather than relying on strict ontological structures.
  </Accordion>

  <Accordion title="Your classification rules are based on semantic understanding">
    Traditional ML approaches often rely on bag-of-words models or simple pattern matching. Claude excels at understanding and applying underlying rules when classes are defined by conditions rather than examples.
  </Accordion>

  <Accordion title="You require interpretable reasoning for classification decisions">
    Many traditional ML models provide little insight into their decision-making process. Claude can provide human-readable explanations for its classification decisions, building trust in the automation system and facilitating easy adaptation if needed.
  </Accordion>

  <Accordion title="You want to handle edge cases and ambiguous tickets more effectively">
    Traditional ML systems often struggle with outliers and ambiguous inputs, frequently misclassifying them or defaulting to a catch-all category. Claude's natural language processing capabilities allow it to better interpret context and nuance in support tickets, potentially reducing the number of misrouted or unclassified tickets that require manual intervention.
  </Accordion>

  <Accordion title="You need multilingual support without maintaining separate models">
    Traditional ML approaches typically require separate models or extensive translation processes for each supported language. Claude's multilingual capabilities allow it to classify tickets in various languages without the need for separate models or extensive translation processes, streamlining support for global customer bases.
  </Accordion>
</AccordionGroup>

***

## Build and deploy your LLM support workflow

### Understand your current support approach

Before diving into automation, it's crucial to understand your existing ticketing system. Start by investigating how your support team currently handles ticket routing.

Consider questions like:

* What criteria are used to determine what SLA/service offering is applied?
* Is ticket routing used to determine which tier of support or product specialist a ticket goes to?
* Are there any automated rules or workflows already in place? In what cases do they fail?
* How are edge cases or ambiguous tickets handled?
* How does the team prioritize tickets?

The more you know about how humans handle certain cases, the better you will be able to work with Claude to do the task.

### Define user intent categories

A well-defined list of user intent categories is crucial for accurate support ticket classification with Claude. Claude’s ability to route tickets effectively within your system is directly proportional to how well-defined your system’s categories are.

Here are some example user intent categories and subcategories.

<AccordionGroup>
  <Accordion title="Technical issue">
    * Hardware problem
    * Software bug
    * Compatibility issue
    * Performance problem
  </Accordion>

  <Accordion title="Account management">
    * Password reset
    * Account access issues
    * Billing inquiries
    * Subscription changes
  </Accordion>

  <Accordion title="Product information">
    * Feature inquiries
    * Product compatibility questions
    * Pricing information
    * Availability inquiries
  </Accordion>

  <Accordion title="User guidance">
    * How-to questions
    * Feature usage assistance
    * Best practices advice
    * Troubleshooting guidance
  </Accordion>

  <Accordion title="Feedback">
    * Bug reports
    * Feature requests
    * General feedback or suggestions
    * Complaints
  </Accordion>

  <Accordion title="Order-related">
    * Order status inquiries
    * Shipping information
    * Returns and exchanges
    * Order modifications
  </Accordion>

  <Accordion title="Service request">
    * Installation assistance
    * Upgrade requests
    * Maintenance scheduling
    * Service cancellation
  </Accordion>

  <Accordion title="Security concerns">
    * Data privacy inquiries
    * Suspicious activity reports
    * Security feature assistance
  </Accordion>

  <Accordion title="Compliance and legal">
    * Regulatory compliance questions
    * Terms of service inquiries
    * Legal documentation requests
  </Accordion>

  <Accordion title="Emergency support">
    * Critical system failures
    * Urgent security issues
    * Time-sensitive problems
  </Accordion>

  <Accordion title="Training and education">
    * Product training requests
    * Documentation inquiries
    * Webinar or workshop information
  </Accordion>

  <Accordion title="Integration and API">
    * Integration assistance
    * API usage questions
    * Third-party compatibility inquiries
  </Accordion>
</AccordionGroup>

In addition to intent, ticket routing and prioritization may also be influenced by other factors such as urgency, customer type, SLAs, or language. Be sure to consider other routing criteria when building your automated routing system.

### Establish success criteria

Work with your support team to [define clear success criteria](/en/docs/test-and-evaluate/define-success) with measurable benchmarks, thresholds, and goals.

Here are some standard criteria and benchmarks when using LLMs for support ticket routing:

<AccordionGroup>
  <Accordion title="Classification consistency">
    This metric assesses how consistently Claude classifies similar tickets over time. It's crucial for maintaining routing reliability. Measure this by periodically testing the model with a set of standardized inputs and aiming for a consistency rate of 95% or higher.
  </Accordion>

  <Accordion title="Adaptation speed">
    This measures how quickly Claude can adapt to new categories or changing ticket patterns. Test this by introducing new ticket types and measuring the time it takes for the model to achieve satisfactory accuracy (e.g., >90%) on these new categories. Aim for adaptation within 50-100 sample tickets.
  </Accordion>

  <Accordion title="Multilingual handling">
    This assesses Claude's ability to accurately route tickets in multiple languages. Measure the routing accuracy across different languages, aiming for no more than a 5-10% drop in accuracy for non-primary languages.
  </Accordion>

  <Accordion title="Edge case handling">
    This evaluates Claude's performance on unusual or complex tickets. Create a test set of edge cases and measure the routing accuracy, aiming for at least 80% accuracy on these challenging inputs.
  </Accordion>

  <Accordion title="Bias mitigation">
    This measures Claude's fairness in routing across different customer demographics. Regularly audit routing decisions for potential biases, aiming for consistent routing accuracy (within 2-3%) across all customer groups.
  </Accordion>

  <Accordion title="Prompt efficiency">
    In situations where minimizing token count is crucial, this criteria assesses how well Claude performs with minimal context. Measure routing accuracy with varying amounts of context provided, aiming for 90%+ accuracy with just the ticket title and a brief description.
  </Accordion>

  <Accordion title="Explainability score">
    This evaluates the quality and relevance of Claude's explanations for its routing decisions. Human raters can score explanations on a scale (e.g., 1-5), with the goal of achieving an average score of 4 or higher.
  </Accordion>
</AccordionGroup>

Here are some common success criteria that may be useful regardless of whether an LLM is used:

<AccordionGroup>
  <Accordion title="Routing accuracy">
    Routing accuracy measures how often tickets are correctly assigned to the appropriate team or individual on the first try. This is typically measured as a percentage of correctly routed tickets out of total tickets. Industry benchmarks often aim for 90-95% accuracy, though this can vary based on the complexity of the support structure.
  </Accordion>

  <Accordion title="Time-to-assignment">
    This metric tracks how quickly tickets are assigned after being submitted. Faster assignment times generally lead to quicker resolutions and improved customer satisfaction. Best-in-class systems often achieve average assignment times of under 5 minutes, with many aiming for near-instantaneous routing (which is possible with LLM implementations).
  </Accordion>

  <Accordion title="Rerouting rate">
    The rerouting rate indicates how often tickets need to be reassigned after initial routing. A lower rate suggests more accurate initial routing. Aim for a rerouting rate below 10%, with top-performing systems achieving rates as low as 5% or less.
  </Accordion>

  <Accordion title="First-contact resolution rate">
    This measures the percentage of tickets resolved during the first interaction with the customer. Higher rates indicate efficient routing and well-prepared support teams. Industry benchmarks typically range from 70-75%, with top performers achieving rates of 80% or higher.
  </Accordion>

  <Accordion title="Average handling time">
    Average handling time measures how long it takes to resolve a ticket from start to finish. Efficient routing can significantly reduce this time. Benchmarks vary widely by industry and complexity, but many organizations aim to keep average handling time under 24 hours for non-critical issues.
  </Accordion>

  <Accordion title="Customer satisfaction scores">
    Often measured through post-interaction surveys, these scores reflect overall customer happiness with the support process. Effective routing contributes to higher satisfaction. Aim for CSAT scores of 90% or higher, with top performers often achieving 95%+ satisfaction rates.
  </Accordion>

  <Accordion title="Escalation rate">
    This measures how often tickets need to be escalated to higher tiers of support. Lower escalation rates often indicate more accurate initial routing. Strive for an escalation rate below 20%, with best-in-class systems achieving rates of 10% or less.
  </Accordion>

  <Accordion title="Agent productivity">
    This metric looks at how many tickets agents can handle effectively after implementing the routing solution. Improved routing should increase productivity. Measure this by tracking tickets resolved per agent per day or hour, aiming for a 10-20% improvement after implementing a new routing system.
  </Accordion>

  <Accordion title="Self-service deflection rate">
    This measures the percentage of potential tickets resolved through self-service options before entering the routing system. Higher rates indicate effective pre-routing triage. Aim for a deflection rate of 20-30%, with top performers achieving rates of 40% or higher.
  </Accordion>

  <Accordion title="Cost per ticket">
    This metric calculates the average cost to resolve each support ticket. Efficient routing should help reduce this cost over time. While benchmarks vary widely, many organizations aim to reduce cost per ticket by 10-15% after implementing an improved routing system.
  </Accordion>
</AccordionGroup>

### Choose the right Claude model

The choice of model depends on the trade-offs between cost, accuracy, and response time.

Many customers have found `claude-3-5-haiku-20241022` an ideal model for ticket routing, as it is the fastest and most cost-effective model in the Claude 3 family while still delivering excellent results. If your classification problem requires deep subject matter expertise or a large volume of intent categories complex reasoning, you may opt for the [larger Sonnet model](/en/docs/about-claude/models).

### Build a strong prompt

Ticket routing is a type of classification task. Claude analyzes the content of a support ticket and classifies it into predefined categories based on the issue type, urgency, required expertise, or other relevant factors.

Let’s write a ticket classification prompt. Our initial prompt should contain the contents of the user request and return both the reasoning and the intent.

<Tip>
  Try the [prompt generator](/en/docs/prompt-generator) on the [Claude Console](https://console.anthropic.com/login) to have Claude write a first draft for you.
</Tip>

Here's an example ticket routing classification prompt:

```python  theme={null}
def classify_support_request(ticket_contents):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. Your task is to analyze customer support requests and output the appropriate classification intent for each request, along with your reasoning. 

        Here is the customer support request you need to classify:

        <request>{ticket_contents}</request>

        Please carefully analyze the above request to determine the customer's core intent and needs. Consider what the customer is asking for has concerns about.

        First, write out your reasoning and analysis of how to classify this request inside <reasoning> tags.

        Then, output the appropriate classification label for the request inside a <intent> tag. The valid intents are:
        <intents>
        <intent>Support, Feedback, Complaint</intent>
        <intent>Order Tracking</intent>
        <intent>Refund/Exchange</intent>
        </intents>

        A request may have ONLY ONE applicable intent. Only include the intent that is most applicable to the request.

        As an example, consider the following request:
        <request>Hello! I had high-speed fiber internet installed on Saturday and my installer, Kevin, was absolutely fantastic! Where can I send my positive review? Thanks for your help!</request>

        Here is an example of how your output should be formatted (for the above example request):
        <reasoning>The user seeks information in order to leave positive feedback.</reasoning>
        <intent>Support, Feedback, Complaint</intent>

        Here are a few more examples:
        <examples>
        <example 2>
        Example 2 Input:
        <request>I wanted to write and personally thank you for the compassion you showed towards my family during my father's funeral this past weekend. Your staff was so considerate and helpful throughout this whole process; it really took a load off our shoulders. The visitation brochures were beautiful. We'll never forget the kindness you showed us and we are so appreciative of how smoothly the proceedings went. Thank you, again, Amarantha Hill on behalf of the Hill Family.</request>

        Example 2 Output:
        <reasoning>User leaves a positive review of their experience.</reasoning>
        <intent>Support, Feedback, Complaint</intent>
        </example 2>
        <example 3>

        ...

        </example 8>
        <example 9>
        Example 9 Input:
        <request>Your website keeps sending ad-popups that block the entire screen. It took me twenty minutes just to finally find the phone number to call and complain. How can I possibly access my account information with all of these popups? Can you access my account for me, since your website is broken? I need to know what the address is on file.</request>

        Example 9 Output:
        <reasoning>The user requests help accessing their web account information.</reasoning>
        <intent>Support, Feedback, Complaint</intent>
        </example 9>

        Remember to always include your classification reasoning before your actual intent output. The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """
```

Let's break down the key components of this prompt:

* We use Python f-strings to create the prompt template, allowing the `ticket_contents` to be inserted into the `<request>` tags.
* We give  Claude a clearly defined role as a classification system that carefully analyzes the ticket content to determine the customer's core intent and needs.
* We instruct Claude on proper output formatting, in this case to provide its reasoning and analysis inside `<reasoning>` tags, followed by the appropriate classification label inside `<intent>` tags.
* We specify the valid intent categories: "Support, Feedback, Complaint", "Order Tracking", and "Refund/Exchange".
* We include a few examples (a.k.a. few-shot prompting) to illustrate how the output should be formatted, which improves accuracy and consistency.

The reason we want to have Claude split its response into various XML tag sections is so that we can use regular expressions to separately extract the reasoning and intent from the output. This allows us to create targeted next steps in the ticket routing workflow, such as using only the intent to decide which person to route the ticket to.

### Deploy your prompt

It’s hard to know how well your prompt works without deploying it in a test production setting and [running evaluations](/en/docs/test-and-evaluate/develop-tests).

Let’s build the deployment structure. Start by defining the method signature for wrapping our call to Claude. We'll take the method we’ve already begun to write, which has `ticket_contents` as input, and now return a tuple of `reasoning` and `intent` as output. If you have an existing automation using traditional ML, you'll want to follow that method signature instead.

```python  theme={null}
import anthropic
import re

# Create an instance of the Claude API client
client = anthropic.Anthropic()

# Set the default model
DEFAULT_MODEL="claude-3-5-haiku-20241022"

def classify_support_request(ticket_contents):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. 
        ...
        ... The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """
    # Send the prompt to the API to classify the support request.
    message = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": classification_prompt}],
        stream=False,
    )
    reasoning_and_intent = message.content[0].text

    # Use Python's regular expressions library to extract `reasoning`.
    reasoning_match = re.search(
        r"<reasoning>(.*?)</reasoning>", reasoning_and_intent, re.DOTALL
    )
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""

    # Similarly, also extract the `intent`.
    intent_match = re.search(r"<intent>(.*?)</intent>", reasoning_and_intent, re.DOTALL)
    intent = intent_match.group(1).strip() if intent_match else ""

    return reasoning, intent
```

This code:

* Imports the Anthropic library and creates a client instance using your API key.
* Defines a `classify_support_request` function that takes a `ticket_contents` string.
* Sends the `ticket_contents` to Claude for classification using the `classification_prompt`
* Returns the model's `reasoning` and `intent` extracted from the response.

Since we need to wait for the entire reasoning and intent text to be generated before parsing, we set `stream=False` (the default).

***

## Evaluate your prompt

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate performance based on the success criteria and thresholds you established earlier.

To run your evaluation, you will need test cases to run it on. The rest of this guide assumes you have already [developed your test cases](/en/docs/test-and-evaluate/develop-tests).

### Build an evaluation function

Our example evaluation for this guide measures Claude’s performance along three key metrics:

* Accuracy
* Cost per classification

You may need to assess Claude on other axes depending on what factors that are important to you.

To assess this, we first have to modify the script we wrote and add a function to compare the predicted intent with the actual intent and calculate the percentage of correct predictions. We also have to add in cost calculation and time measurement functionality.

```python  theme={null}
import anthropic
import re

# Create an instance of the Claude API client
client = anthropic.Anthropic()

# Set the default model
DEFAULT_MODEL="claude-3-5-haiku-20241022"

def classify_support_request(request, actual_intent):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. 
        ...
        ...The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only the reasoning and the intent.
        """

    message = client.messages.create(
        model=DEFAULT_MODEL,
        max_tokens=500,
        temperature=0,
        messages=[{"role": "user", "content": classification_prompt}],
    )
    usage = message.usage  # Get the usage statistics for the API call for how many input and output tokens were used.
    reasoning_and_intent = message.content[0].text

    # Use Python's regular expressions library to extract `reasoning`.
    reasoning_match = re.search(
        r"<reasoning>(.*?)</reasoning>", reasoning_and_intent, re.DOTALL
    )
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""

    # Similarly, also extract the `intent`.
    intent_match = re.search(r"<intent>(.*?)</intent>", reasoning_and_intent, re.DOTALL)
    intent = intent_match.group(1).strip() if intent_match else ""

      # Check if the model's prediction is correct.
    correct = actual_intent.strip() == intent.strip()

    # Return the reasoning, intent, correct, and usage.
    return reasoning, intent, correct, usage
```

Let’s break down the edits we’ve made:

* We added the `actual_intent` from our test cases into the `classify_support_request` method and set up a comparison to assess whether Claude’s intent classification matches our golden intent classification.
* We extracted usage statistics for the API call to calculate cost based on input and output tokens used

### Run your evaluation

A proper evaluation requires clear thresholds and benchmarks to determine what is a good result. The script above will give us the runtime values for accuracy, response time, and cost per classification, but we still would need clearly established thresholds. For example:

* **Accuracy:** 95% (out of 100 tests)
* **Cost per classification:** 50% reduction on average (across 100 tests) from current routing method

Having these thresholds allows you to quickly and easily tell at scale, and with impartial empiricism, what method is best for you and what changes might need to be made to better fit your requirements.

***

## Improve performance

In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](/en/docs/build-with-claude/prompt-engineering/overview) & [guardrail implementation strategies](/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). Here are some common scenarios:

### Use a taxonomic hierarchy for cases with 20+ intent categories

As the number of classes grows, the number of examples required also expands, potentially making the prompt unwieldy. As an alternative, you can consider implementing a hierarchical classification system using a mixture of classifiers.

1. Organize your intents in a taxonomic tree structure.
2. Create a series of classifiers at every level of the tree, enabling a cascading routing approach.

For example, you might have a top-level classifier that broadly categorizes tickets into "Technical Issues," "Billing Questions," and "General Inquiries." Each of these categories can then have its own sub-classifier to further refine the classification.

<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=5289a8c92716a132311081bc9efed4fc" alt="" data-og-width="2998" width="2998" data-og-height="430" height="430" data-path="images/ticket-hierarchy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=6e2d5e710d722b23f00f43e14a9aa94c 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a6184c7df444a8c4bfbdbd7f5b46bb3e 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=31536d5d35e186e5cadf58d5b3657ce8 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=efc29d26d9808a8003c0bc66e7ac9ddb 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=4694bf9a36805541f14c2d33221a82ad 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/ticket-hierarchy.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=2ac2109b054a21342ae533e6098789d0 2500w" />

* **Pros - greater nuance and accuracy:** You can create different prompts for each parent path, allowing for more targeted and context-specific classification. This can lead to improved accuracy and more nuanced handling of customer requests.

* **Cons - increased latency:** Be advised that multiple classifiers can lead to increased latency, and we recommend implementing this approach with our fastest model, Haiku.

### Use vector databases and similarity search retrieval to handle highly variable tickets

Despite providing examples being the most effective way to improve performance, if support requests are highly variable, it can be hard to include enough examples in a single prompt.

In this scenario, you could employ a vector database to do similarity searches from a dataset of examples and retrieve the most relevant examples for a given query.

This approach, outlined in detail in our [classification recipe](https://github.com/anthropics/anthropic-cookbook/blob/82675c124e1344639b2a875aa9d3ae854709cd83/skills/classification/guide.ipynb), has been shown to improve performance from 71% accuracy to 93% accuracy.

### Account specifically for expected edge cases

Here are some scenarios where Claude may misclassify tickets (there may be others that are unique to your situation). In these scenarios,consider providing explicit instructions or examples in the prompt of how Claude should handle the edge case:

<AccordionGroup>
  <Accordion title="Customers make implicit requests">
    Customers often express needs indirectly. For example, "I've been waiting for my package for over two weeks now" may be an indirect request for order status.

    * **Solution:** Provide Claude with some real customer examples of these kinds of requests, along with what the underlying intent is. You can get even better results if you include a classification rationale for particularly nuanced ticket intents, so that Claude can better generalize the logic to other tickets.
  </Accordion>

  <Accordion title="Claude prioritizes emotion over intent">
    When customers express dissatisfaction, Claude may prioritize addressing the emotion over solving the underlying problem.

    * **Solution:** Provide Claude with directions on when to prioritize customer sentiment or not. It can be something as simple as “Ignore all customer emotions. Focus only on analyzing the intent of the customer’s request and what information the customer might be asking for.”
  </Accordion>

  <Accordion title="Multiple issues cause issue prioritization confusion">
    When customers present multiple issues in a single interaction, Claude may have difficulty identifying the primary concern.

    * **Solution:** Clarify the prioritization of intents so thatClaude can better rank the extracted intents and identify the primary concern.
  </Accordion>
</AccordionGroup>

***

## Integrate Claude into your greater support workflow

Proper integration requires that you make some decisions regarding how your Claude-based ticket routing script fits into the architecture of your greater ticket routing system.There are two ways you could do this:

* **Push-based:** The support ticket system you’re using (e.g. Zendesk) triggers your code by sending a webhook event to your routing service, which then classifies the intent and routes it.
  * This approach is more web-scalable, but needs you to expose a public endpoint.
* **Pull-Based:** Your code pulls for the latest tickets based on a given schedule and routes them at pull time.
  * This approach is easier to implement but might make unnecessary calls to the support ticket system when the pull frequency is too high or might be overly slow when the pull frequency is too low.

For either of these approaches, you will need to wrap your script in a service. The choice of approach depends on what APIs your support ticketing system provides.

***

<CardGroup cols={2}>
  <Card title="Classification cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/classification">
    Visit our classification cookbook for more example code and detailed eval guidance.
  </Card>

  <Card title="Claude Console" icon="link" href="https://console.anthropic.com/dashboard">
    Begin building and evaluating your workflow on the Claude Console.
  </Card>
</CardGroup>


# Model Context Protocol (MCP)
Source: https://docs.claude.com/en/docs/mcp



MCP is an open protocol that standardizes how applications provide context to LLMs.

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

## Build your own MCP products

<Card title="MCP Documentation" icon="book" href="https://modelcontextprotocol.io">
  Learn more about the protocol, how to build servers and clients, and discover those made by others.
</Card>

## MCP in Anthropic products

<CardGroup>
  <Card title="MCP in the Messages API" icon="cloud" href="/en/docs/agents-and-tools/mcp-connector">
    Use the MCP connector in the Messages API to connect to MCP servers.
  </Card>

  <Card title="MCP in Claude Code" icon="head-side-gear" href="https://code.claude.com/docs/mcp">
    Add your MCP servers to Claude Code, or use Claude Code as a server.
  </Card>

  <Card title="MCP in Claude.ai" icon="comments" href="https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp">
    Enable MCP connectors for your team in Claude.ai.
  </Card>

  <Card title="MCP in Claude Desktop" icon="desktop" href="https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop">
    Add MCP servers to Claude Desktop.
  </Card>
</CardGroup>



---

**Navigation:** [← Previous](./13-using-the-evaluation-tool.md) | [Index](./index.md) | [Next →](./15-system-prompts.md)
