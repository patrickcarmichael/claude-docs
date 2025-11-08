---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

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
     >   **📝 Note**
>
> This will require that Claude have the necessary information in its context, and might imply that a [RAG integration](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/retrieval_augmented_generation/guide.ipynb) is necessary.
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
