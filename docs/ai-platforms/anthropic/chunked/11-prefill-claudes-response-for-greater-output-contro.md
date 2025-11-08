**Navigation:** [← Previous](./10-let-claude-think-chain-of-thought-prompting-to-inc.md) | [Index](./index.md) | [Next →](./12-streaming-messages.md)

---

# Prefill Claude's response for greater output control
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

<Note>
  Prefilling is only available for non-extended thinking modes. It's not currently supported with extended thinking.
</Note>

When using Claude, you have the unique ability to guide its responses by prefilling the `Assistant` message. This powerful technique allows you to direct Claude's actions, skip preambles, enforce specific formats like JSON or XML, and even help Claude maintain character consistency in role-play scenarios.

In some cases where Claude is not performing as expected, a few prefilled sentences can vastly improve Claude's performance. A little prefilling goes a long way!

## How to prefill Claude's response

To prefill, include the desired initial text in the `Assistant` message (Claude's response will continue from where the `Assistant` message leaves off):

```python  theme={null}
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is your favorite color?"},
        {"role": "assistant", "content": "As an AI assistant, I don't have a favorite color, But if I had to pick, it would be green because"}  # Prefill here
    ]
)
```

<Warning>
  The prefill content cannot end with trailing whitespace. A prefill like `"As an AI assistant, I "` (with a space at the end) will result in an error.
</Warning>

### Examples

#### Example 1: Controlling output formatting and skipping the preamble

<Tip>**Power user tip**: Prefilling `{` forces Claude to skip the preamble and directly output the JSON object. This is cleaner, more concise, and easier for programs to parse without additional processing.</Tip>

<AccordionGroup>
  <Accordion title="Example: Structured data extraction without prefilling">
    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | Extract the name, size, price, and color from this product description as a JSON object:<br /><br />\<description><br />The SmartHome Mini is a compact smart home assistant available in black or white for only \$49.99. At just 5 inches wide, it lets you control lights, thermostats, and other connected devices via voice or app—no matter where you place it in your home. This affordable little hub brings convenient hands-free control to your smart devices.<br />\</description>                                                                                                                                      |
    | Assistant | Here's the extracted information in JSON format:<br /><br />\`\`\`json<br />\{<br />  "name": "SmartHome Mini",<br />  "size": "5 inches wide",<br />  "price": "\$49.99",<br />  "colors": \["black", "white"]<br />}<br />\`\`\`<br /><br />I've extracted the following details from the product description:<br />- **Name**: SmartHome Mini<br />- **Size**: 5 inches wide<br />- **Price**: \$49.99<br />- **Colors**: Available in black and white<br /><br />The JSON object provides a structured format that's easy for programs to parse and use. Let me know if you need any modifications or have any other questions! |
  </Accordion>

  <Accordion title="Example: Structured data extraction with prefilling">
    | Role                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User                          | Extract the name, size, price, and color from this product description as a JSON object:<br /><br />\<description><br />The SmartHome Mini is a compact smart home assistant available in black or white for only \$49.99. At just 5 inches wide, it lets you control lights, thermostats, and other connected devices via voice or app—no matter where you place it in your home. This affordable little hub brings convenient hands-free control to your smart devices.<br />\</description> |
    | Assistant (prefill)           | \{                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | Assistant (Claude's response) | "name": "SmartHome Mini",<br />"size": "5 inches wide",<br />"price": "\$49.99",<br />"colors": \[<br />  "black",<br />  "white"<br />]<br />}                                                                                                                                                                                                                                                                                                                                                |
  </Accordion>
</AccordionGroup>

#### Example 2: Maintaining character in roleplay scenarios

<Tip>**Role-play tip**: Prefilling a bracketed `[ROLE_NAME]` can remind Claude stay in character, even for longer and more complex conversations. This is especially powerful when combined with role prompting in the `system` parameter.</Tip>

<AccordionGroup>
  <Accordion title="Example: Maintaining character without role prompting">
    | Role                                                          | Content                                                                                                                     |
    | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
    | User (50 conversation turns in with "Sherlock Holmes" Claude) | What do you deduce about the owner of this shoe? \<image>muddy\_shoe.jpg\</image>                                           |
    | Assistant                                                     | As an AI assistant, I would be happy to analyze the image of a muddy shoe as if you had provided it. Here's my deduction... |
  </Accordion>

  <Accordion title="Example: Maintaining character with role prompting">
    | Role                                                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User (50 conversation turns in with "Sherlock Holmes" Claude) | What do you deduce about the owner of this shoe? <br />\<image>muddy\_shoe.jpg\</image>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | Assistant (prefill)                                           | \[Sherlock Holmes]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | Assistant (Claude's response)                                 | Ah, what have we here? A most curious specimen, Watson! Let us examine this shoe with a discerning eye. The mud, you see, is not your common London clay, but rather the distinctive reddish hue of the iron-rich soil found only in the environs of Hampstead Heath. And yet, the wear on the sole suggests a gait more suited to the cobblestones of Whitechapel than the gentle slopes of the Heath.<br /><br />Now, observe the laces! They are tied with a particular knot favored by those in the medical profession—doubtless a habit acquired during years of tying surgical gowns. But the scuff marks on the toe box tell a different tale: they are consistent with the kicking motion one might employ in the martial arts, specifically Baritsu.<br /><br />We may conclude, then, that our absent shoe owner is a doctor, possibly a surgeon, who resides in Whitechapel but frequents Hampstead Heath—perhaps for a secret Baritsu practice, away from prying eyes. A most intriguing case, Watson! We must make haste; the game is afoot! |
  </Accordion>
</AccordionGroup>

***

<CardGroup cols={3}>
  <Card title="Working with Messages" icon="messages" href="/en/docs/build-with-claude/working-with-messages">
    See more examples of prefill and other Messages API patterns.
  </Card>

  <Card title="Prompt library" icon="link" href="/en/resources/prompt-library/library">
    Get inspired by a curated selection of prompts for various tasks and use cases.
  </Card>

  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>

  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>


# Automatically generate first draft prompt templates
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-generator



<Note>
  Our prompt generator is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see [here](/en/docs/build-with-claude/extended-thinking).
</Note>

Sometimes, the hardest part of using an AI model is figuring out how to prompt it effectively. To help with this, we've created a prompt generation tool that guides Claude to generate high-quality prompt templates tailored to your specific tasks. These templates follow many of our prompt engineering best practices.

The prompt generator is particularly useful as a tool for solving the "blank page problem" to give you a jumping-off point for further testing and iteration.

<Tip>Try the prompt generator now directly on the [Console](https://console.anthropic.com/dashboard).</Tip>

If you're interested in analyzing the underlying prompt and architecture, check out our [prompt generator Google Colab notebook](https://anthropic.com/metaprompt-notebook/). There, you can easily run the code to have Claude construct prompts on your behalf.

<Note>Note that to run the Colab notebook, you will need an [API key](https://console.anthropic.com/settings/keys).</Note>

***

## Next steps

<CardGroup cols={2}>
  <Card title="Start prompt engineering" icon="link" href="/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct">
    Get inspired by a curated selection of prompts for various tasks and use cases.
  </Card>

  <Card title="Prompt library" icon="link" href="/en/resources/prompt-library/library">
    Get inspired by a curated selection of prompts for various tasks and use cases.
  </Card>

  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>

  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>


# Use our prompt improver to optimize your prompts
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-improver



<Note>
  Our prompt improver is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see [here](/en/docs/build-with-claude/extended-thinking).
</Note>

The prompt improver helps you quickly iterate and improve your prompts through automated analysis and enhancement. It excels at making prompts more robust for complex tasks that require high accuracy.

<Frame>
  <img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=01479d382e45cc5cdec882d53f3bbf87" data-og-width="1210" width="1210" data-og-height="498" height="498" data-path="images/prompt_improver.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=a8a5e551ed73c52fa522a558f07b1a68 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=425bc1825e1a95df7b9c419eb4d2ccdc 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=73e7bcf8692fa22632c26c34ebef281f 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=06b64cdc47098cb8bf1fb68cbe9212a5 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=0373ee302a7fb52d64fee13d0a3d5dc4 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt_improver.png?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=94ecf75d5241f3e68a6dbf2137f447a4 2500w" />
</Frame>

## Before you begin

You'll need:

* A [prompt template](/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables) to improve
* Feedback on current issues with Claude's outputs (optional but recommended)
* Example inputs and ideal outputs (optional but recommended)

## How the prompt improver works

The prompt improver enhances your prompts in 4 steps:

1. **Example identification**: Locates and extracts examples from your prompt template
2. **Initial draft**: Creates a structured template with clear sections and XML tags
3. **Chain of thought refinement**: Adds and refines detailed reasoning instructions
4. **Example enhancement**: Updates examples to demonstrate the new reasoning process

You can watch these steps happen in real-time in the improvement modal.

## What you get

The prompt improver generates templates with:

* Detailed chain-of-thought instructions that guide Claude's reasoning process and typically improve its performance
* Clear organization using XML tags to separate different components
* Standardized example formatting that demonstrates step-by-step reasoning from input to output
* Strategic prefills that guide Claude's initial responses

<Note>
  While examples appear separately in the Workbench UI, they're included at the start of the first user message in the actual API call. View the raw format by clicking "**\</> Get Code**" or insert examples as raw text via the Examples box.
</Note>

## How to use the prompt improver

1. Submit your prompt template
2. Add any feedback about issues with Claude's current outputs (e.g., "summaries are too basic for expert audiences")
3. Include example inputs and ideal outputs
4. Review the improved prompt

## Generate test examples

Don't have examples yet? Use our [Test Case Generator](/en/docs/test-and-evaluate/eval-tool#creating-test-cases) to:

1. Generate sample inputs
2. Get Claude's responses
3. Edit the responses to match your ideal outputs
4. Add the polished examples to your prompt

## When to use the prompt improver

The prompt improver works best for:

* Complex tasks requiring detailed reasoning
* Situations where accuracy is more important than speed
* Problems where Claude's current outputs need significant improvement

<Note>
  For latency or cost-sensitive applications, consider using simpler prompts. The prompt improver creates templates that produce longer, more thorough, but slower responses.
</Note>

## Example improvement

Here's how the prompt improver enhances a basic classification prompt:

<Accordion title="Original prompt">
  ```
  From the following list of Wikipedia article titles, identify which article this sentence came from.
  Respond with just the article title and nothing else.

  Article titles:
  {{titles}}

  Sentence to classify:
  {{sentence}}
  ```
</Accordion>

<Accordion title="Improved prompt">
  ```
  You are an intelligent text classification system specialized in matching sentences to Wikipedia article titles. Your task is to identify which Wikipedia article a given sentence most likely belongs to, based on a provided list of article titles.

  First, review the following list of Wikipedia article titles:
  <article_titles>
  {{titles}}
  </article_titles>

  Now, consider this sentence that needs to be classified:
  <sentence_to_classify>
  {{sentence}}
  </sentence_to_classify>

  Your goal is to determine which article title from the provided list best matches the given sentence. Follow these steps:

  1. List the key concepts from the sentence
  2. Compare each key concept with the article titles
  3. Rank the top 3 most relevant titles and explain why they are relevant
  4. Select the most appropriate article title that best encompasses or relates to the sentence's content

  Wrap your analysis in <analysis> tags. Include the following:
  - List of key concepts from the sentence
  - Comparison of each key concept with the article titles
  - Ranking of top 3 most relevant titles with explanations
  - Your final choice and reasoning

  After your analysis, provide your final answer: the single most appropriate Wikipedia article title from the list.

  Output only the chosen article title, without any additional text or explanation.
  ```
</Accordion>

Notice how the improved prompt:

* Adds clear step-by-step reasoning instructions
* Uses XML tags to organize content
* Provides explicit output formatting requirements
* Guides Claude through the analysis process

## Troubleshooting

Common issues and solutions:

* **Examples not appearing in output**: Check that examples are properly formatted with XML tags and appear at the start of the first user message
* **Chain of thought too verbose**: Add specific instructions about desired output length and level of detail
* **Reasoning steps don't match your needs**: Modify the steps section to match your specific use case

***

## Next steps

<CardGroup cols={3}>
  <Card title="Prompt library" icon="link" href="/en/resources/prompt-library/library">
    Get inspired by example prompts for various tasks.
  </Card>

  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    Learn prompting best practices with our interactive tutorial.
  </Card>

  <Card title="Test your prompts" icon="link" href="/en/docs/test-and-evaluate/eval-tool">
    Use our evaluation tool to test your improved prompts.
  </Card>
</CardGroup>


# Use prompt templates and variables
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables



When deploying an LLM-based application with Claude, your API calls will typically consist of two types of content:

* **Fixed content:** Static instructions or context that remain constant across multiple interactions
* **Variable content:** Dynamic elements that change with each request or conversation, such as:
  * User inputs
  * Retrieved content for Retrieval-Augmented Generation (RAG)
  * Conversation context such as user account history
  * System-generated data such as tool use results fed in from other independent calls to Claude

A **prompt template** combines these fixed and variable parts, using placeholders for the dynamic content. In the [Claude Console](https://console.anthropic.com/), these placeholders are denoted with **\{\{double brackets}}**, making them easily identifiable and allowing for quick testing of different values.

***

# When to use prompt templates and variables

You should always use prompt templates and variables when you expect any part of your prompt to be repeated in another call to Claude (only via the API or the [Claude Console](https://console.anthropic.com/). [claude.ai](https://claude.ai/) currently does not support prompt templates or variables).

Prompt templates offer several benefits:

* **Consistency:** Ensure a consistent structure for your prompts across multiple interactions
* **Efficiency:** Easily swap out variable content without rewriting the entire prompt
* **Testability:** Quickly test different inputs and edge cases by changing only the variable portion
* **Scalability:** Simplify prompt management as your application grows in complexity
* **Version control:** Easily track changes to your prompt structure over time by keeping tabs only on the core part of your prompt, separate from dynamic inputs

The [Claude Console](https://console.anthropic.com/) heavily uses prompt templates and variables in order to support features and tooling for all the above, such as with the:

* **[Prompt generator](/en/docs/build-with-claude/prompt-engineering/prompt-generator):** Decides what variables your prompt needs and includes them in the template it outputs
* **[Prompt improver](/en/docs/build-with-claude/prompt-engineering/prompt-improver):** Takes your existing template, including all variables, and maintains them in the improved template it outputs
* **[Evaluation tool](/en/docs/test-and-evaluate/eval-tool):** Allows you to easily test, scale, and track versions of your prompts by separating the variable and fixed portions of your prompt template

***

# Example prompt template

Let's consider a simple application that translates English text to Spanish. The translated text would be variable since you would expect this text to change between users or calls to Claude. This translated text could be dynamically retrieved from databases or the user's input.

Thus, for your translation app, you might use this simple prompt template:

```
Translate this text from English to Spanish: {{text}}
```

***

## Next steps

<CardGroup cols={2}>
  <Card title="Generate a prompt" icon="link" href="/en/docs/build-with-claude/prompt-engineering/prompt-generator">
    Learn about the prompt generator in the Claude Console and try your hand at getting Claude to generate a prompt for you.
  </Card>

  <Card title="Apply XML tags" icon="link" href="/en/docs/build-with-claude/prompt-engineering/use-xml-tags">
    If you want to level up your prompt variable game, wrap them in XML tags.
  </Card>

  <Card title="Claude Console" icon="link" href="https://console.anthropic.com/">
    Check out the myriad prompt development tools available in the Claude Console.
  </Card>
</CardGroup>


# Giving Claude a role with a system prompt
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

When using Claude, you can dramatically improve its performance by using the `system` parameter to give it a role. This technique, known as role prompting, is the most powerful way to use system prompts with Claude.

The right role can turn Claude from a general assistant into your virtual domain expert!

<Tip>**System prompt tips**: Use the `system` parameter to set Claude's role. Put everything else, like task-specific instructions, in the `user` turn instead.</Tip>

## Why use role prompting?

* **Enhanced accuracy:** In complex scenarios like legal analysis or financial modeling, role prompting can significantly boost Claude's performance.
* **Tailored tone:** Whether you need a CFO's brevity or a copywriter's flair, role prompting adjusts Claude's communication style.
* **Improved focus:** By setting the role context, Claude stays more within the bounds of your task's specific requirements.

***

## How to give Claude a role

Use the `system` parameter in the [Messages API](/en/api/messages) to set Claude's role:

```python  theme={null}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=2048,
    system="You are a seasoned data scientist at a Fortune 500 company.", # <-- role prompt
    messages=[
        {"role": "user", "content": "Analyze this dataset for anomalies: <dataset>{{DATASET}}</dataset>"}
    ]
)

print(response.content)
```

<Tip>**Role prompting tip**: Experiment with roles! A `data scientist` might see different insights than a `marketing strategist` for the same data. A `data scientist specializing in customer insight analysis for Fortune 500 companies` might yield different results still!</Tip>

***

## Examples

### Example 1: Legal contract analysis

Without a role, Claude might miss critical issues:

<Accordion title="Legal contract analysis without role prompting">
  | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User      | Analyze this software licensing agreement for potential risks:<br />\<contract><br />\{\{CONTRACT}}<br />\</contract><br /><br />Focus on indemnification, liability, and IP ownership.                                                                                                                                                                                                                                                                                                                              |
  | Assistant | Here's a summary of the key points in the software licensing agreement:<br /><br />1. Indemnification (Section 8):<br />   - We indemnify the vendor against claims arising from our use.<br /><br />2. Limitation of Liability (Section 9):<br />   - Damages capped at \$500.<br /><br />3. IP Ownership (Section 12):<br />   - We retain ownership of our modifications.<br /><br />Overall, the agreement seems standard. The indemnification and liability clauses are typical, and we maintain our IP rights. |
</Accordion>

With a role, Claude catches critical issues that could cost millions:

<Accordion title="Legal contract analysis with role prompting">
  | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User      | You are the General Counsel of a Fortune 500 tech company. We're considering this software licensing agreement for our core data infrastructure:<br />\<contract><br />\{\{CONTRACT}}<br />\</contract><br /><br />Analyze it for potential risks, focusing on indemnification, liability, and IP ownership. Give your professional opinion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | Assistant | I've reviewed the software licensing agreement, and I have serious concerns that could expose our company to significant risks:<br /><br />1. Indemnification (Section 8):<br />   - Critical Issue: We indemnify the vendor against "any and all claims" arising from our use.<br />   - Risk: This could hold us liable even for the vendor's negligence or product defects.<br />   - Recommendation: Reject. Limit our indemnity to claims arising from our violation of the agreement.<br /><br />2. Limitation of Liability (Section 9):<br />   - Critical Issue: Damages capped at \$500, including direct damages.<br />   - Risk: Grossly inadequate. A critical failure in our data infrastructure could cost us millions in lost revenue and reputational damage.<br />   - Recommendation: Reject. Negotiate for cap at 12 months of fees for direct damages, and carve-outs for data breaches.<br /><br />3. IP Ownership (Section 12):<br />   - Critical Issue: Vendor gains joint ownership of our modifications and integrations.<br />   - Risk: They could use or sell our proprietary algorithms or data insights to competitors.<br />   - Recommendation: Reject. We must retain full ownership of our work.<br /><br />Professional Opinion: Do not sign this agreement. It is grossly unfavorable and exposes us to unacceptable levels of risk. If the vendor refuses to renegotiate these terms, I strongly advise exploring alternative providers or accelerating our in-house solution. The potential costs of proceeding with this agreement far outweigh any short-term gains. |
</Accordion>

### Example 2: Financial analysis

Without a role, Claude's analysis lacks depth:

<Accordion title="Financial analysis without role prompting">
  | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User      | Analyze this dataset of our Q2 financials:<br />\<data><br />\{\{FINANCIALS}}<br />\</data><br /><br />Highlight key trends and recommend actions.                                                                                                                                                                                                                                                                                                                               |
  | Assistant | Here's a summary of your Q2 financials:<br /><br />1. Revenue: \$15.2M, up 22% YoY. Enterprise client base grew 30%.<br />2. Gross Margin: 72%, up 3% from Q1.<br />3. EBITDA Margin: 18%, down 2% due to R\&D investments.<br />4. Cash Flow: \$4.1M operating, \$28M in reserves.<br /><br />Overall, financials look strong with revenue growth and healthy margins. Increased R\&D spending is impacting profitability but could pay off long-term. Maintain current course. |
</Accordion>

With a role, Claude delivers actionable insights:

<Accordion title="Financial analysis with role prompting">
  | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User      | You are the CFO of a high-growth B2B SaaS company. We're in a board meeting discussing our Q2 financials:<br />\<data><br />\{\{FINANCIALS}}<br />\</data><br /><br />Analyze key trends, flag concerns, and recommend strategic actions. Our investors want aggressive growth but are wary of our burn rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | Assistant | Board members, here's my analysis of our Q2 financials:<br /><br />1. Revenue (\$15.2M, +22% YoY):<br />   - Insight: Enterprise growth (+30%) is outpacing overall growth.<br />   - Flag: SMB segment declined 5%.<br />   - Action: Reallocate 20% of SMB marketing budget to enterprise sales. Task product to simplify SMB onboarding.<br /><br />2. Margins (Gross: 72%, +3% QoQ; EBITDA: 18%, -2% QoQ):<br />   - Insight: Infrastructure optimizations boosted gross margins.<br />   - Flag: R\&D spend on AI features dented EBITDA.<br />   - Action: No change. Our AI roadmap is critical for enterprise stickiness.<br /><br />3. Cash (\$4.1M OCF, \$28M reserves):<br />   - Insight: 15-month runway at current burn.<br />   - Flag: CAC up 20%, eroding LTV/CAC.<br />   - Action: Freeze non-essential hires. Implement sales funnel analytics to cut CAC by 15% in Q3.<br /><br />Strategic Stance: We're threading the needle between growth and burn. Enterprise focus is our growth engine—invest there. But watch SMB churn; it could bleed into enterprise. Our AI bet is sound, but we must convert it to ARR by Q4, or we cut R\&D by 30%.<br /><br />In sum: Double down on enterprise, streamline SMB, optimize sales, and monetize AI. Questions? |
</Accordion>

***

<CardGroup cols={3}>
  <Card title="Prompt library" icon="link" href="/en/resources/prompt-library/library">
    Get inspired by a curated selection of prompts for various tasks and use cases.
  </Card>

  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>

  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>


# Use XML tags to structure your prompts
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

When your prompts involve multiple components like context, instructions, and examples, XML tags can be a game-changer. They help Claude parse your prompts more accurately, leading to higher-quality outputs.

<Tip>**XML tip**: Use tags like `<instructions>`, `<example>`, and `<formatting>` to clearly separate different parts of your prompt. This prevents Claude from mixing up instructions with examples or context.</Tip>

## Why use XML tags?

* **Clarity:** Clearly separate different parts of your prompt and ensure your prompt is well structured.
* **Accuracy:** Reduce errors caused by Claude misinterpreting parts of your prompt.
* **Flexibility:** Easily find, add, remove, or modify parts of your prompt without rewriting everything.
* **Parseability:** Having Claude use XML tags in its output makes it easier to extract specific parts of its response by post-processing.

<Note>There are no canonical "best" XML tags that Claude has been trained with in particular, although we recommend that your tag names make sense with the information they surround.</Note>

***

## Tagging best practices

1. **Be consistent**: Use the same tag names throughout your prompts, and refer to those tag names when talking about the content (e.g, `Using the contract in <contract> tags...`).
2. **Nest tags**: You should nest tags `<outer><inner></inner></outer>` for hierarchical content.

<Tip>**Power user tip**: Combine XML tags with other techniques like multishot prompting (`<examples>`) or chain of thought (`<thinking>`, `<answer>`). This creates super-structured, high-performance prompts.</Tip>

### Examples

<AccordionGroup>
  <Accordion title="Example: Generating financial reports">
    Without XML tags, Claude misunderstands the task and generates a report that doesn't match the required structure or tone. After substitution, there is also a chance that Claude misunderstands where one section (like the the Q1 report example) stops and another begins.

    | Role      | No XML Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | With XML Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | You're a financial analyst at AcmeCorp. Generate a Q2 financial report for our investors. Include sections on Revenue Growth, Profit Margins, and Cash Flow, like with this example from last year: \{\{Q1\_REPORT}}. Use data points from this spreadsheet: \{\{SPREADSHEET\_DATA}}. The report should be extremely concise, to the point, professional, and in list format. It should and highlight both strengths and areas for improvement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | You're a financial analyst at AcmeCorp. Generate a Q2 financial report for our investors.<br /><br />AcmeCorp is a B2B SaaS company. Our investors value transparency and actionable insights.<br /><br />Use this data for your report:\<data>\{\{SPREADSHEET\_DATA}}\</data><br /><br />\<instructions><br />1. Include sections: Revenue Growth, Profit Margins, Cash Flow.<br />2. Highlight strengths and areas for improvement.<br />\</instructions><br /><br />Make your tone concise and professional. Follow this structure:<br />\<formatting\_example>\{\{Q1\_REPORT}}\</formatting\_example>                                                                                                                                                                                                                  |
    | Assistant | Q2 Financial Report for AcmeCorp Investors<br /><br />Dear Valued Investors,<br /><br />I am pleased to present our Q2 financial report, showcasing AcmeCorp's continued growth and resilience in the B2B SaaS market.<br /><br />1. Revenue Growth:<br />Our Q2 revenue reached \$15.2M, a 22% YoY increase. This growth is primarily driven by a 30% expansion in our enterprise client base. However, our SMB segment saw a slight decline of 5%, which we aim to address through targeted marketing initiatives in Q3.<br /><br />2. Profit Margins:<br />Gross margin improved to 72% (up 3% from Q1) due to infrastructure optimizations. EBITDA margin, however, dipped to 18% (down 2%) as we invested heavily in R\&D for our upcoming AI-driven features.<br /><br />3. Cash Flow:<br />Operating cash flow remains strong at \$4.1M. Our cash reserves stand at \$28M, providing a 15-month runway at current burn rate. We did see a 20% increase in customer acquisition costs, which we're addressing through more efficient sales strategies.<br /><br />In summary, AcmeCorp's core financials remain robust. We're balancing growth investments with prudent cash management. Our focus for Q3 will be revitalizing SMB growth and optimizing sales efficiency.<br /><br />Thank you for your continued trust.<br /><br />Sincerely,<br />CFO, AcmeCorp | Q2 Financial Report for AcmeCorp Investors\</output><br /><br />Revenue Growth:<br />- Q2 revenue: \$15.2M (22% YoY ↑)<br />- Enterprise clients: 30% ↑<br />- SMB segment: 5% ↓<br />  Action: Targeted Q3 marketing<br /><br />Profit Margins:<br />- Gross margin: 72% (3% ↑ from Q1)<br />  Reason: Infrastructure optimizations<br />- EBITDA margin: 18% (2% ↓)<br />  Reason: R\&D investment in AI features<br /><br />Cash Flow:<br />- Operating cash flow: \$4.1M (strong)<br />- Cash reserves: \$28M (15-month runway)<br />- Customer acquisition cost: 20% ↑<br />  Action: Optimize sales strategies<br /><br />Outlook:<br />- Core financials: Robust<br />- Q3 focus: Revitalize SMB, optimize sales<br /><br />Management remains committed to balancing growth investments with financial discipline. |
  </Accordion>

  <Accordion title="Example: Legal contract analysis">
    Without XML tags, Claude's analysis is disorganized and misses key points. With tags, it provides a structured, thorough analysis that a legal team can act on.

    | Role      | No XML Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | With XML Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | User      | Analyze this software licensing agreement for potential risks and liabilities: \{\{CONTRACT}}. Focus on indemnification, limitation of liability, and IP ownership clauses. Also, note any unusual or concerning terms. Here's our standard contract for reference: \{\{STANDARD\_CONTRACT}}. Give a summary of findings and recommendations for our legal team.                                                                                                                                                                                                                                                                                                                    | Analyze this software licensing agreement for legal risks and liabilities.<br /><br />We're a multinational enterprise considering this agreement for our core data infrastructure.<br /><br />\<agreement><br />\{\{CONTRACT}}\</agreement><br /><br />This is our standard contract for reference:<br />\<standard\_contract>\{\{STANDARD\_CONTRACT}}\</standard\_contract><br /><br />\<instructions><br />1. Analyze these clauses:<br />   - Indemnification<br />   - Limitation of liability<br />   - IP ownership<br /><br />2. Note unusual or concerning terms.<br /><br />3. Compare to our standard contract.<br /><br />4. Summarize findings in \<findings> tags.<br /><br />5. List actionable recommendations in \<recommendations> tags.\</instructions>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | Assistant | The provided software licensing agreement presents several concerning aspects. The indemnification clause is overly broad, potentially exposing us to significant liabilities. The limitation of liability section caps damages at a mere \$500, which is inadequate for our enterprise-level usage. Regarding IP, the agreement grants the vendor joint ownership of any modifications or integrations we create.<br /><br />In summary, this agreement is not in our best interest. It exposes us to undue risk, limits our recourse in case of failures, and compromises our intellectual property rights. I recommend renegotiating these terms or seeking alternative vendors. | \<findings><br />1. Indemnification (Clause 8):<br />   - Issue: Overly broad. We indemnify vendor against "any and all claims" arising from our use.<br />   - Risk: Could hold us liable even for vendor's negligence or product defects.<br />   - Deviation: Our standard limits indemnity to claims arising from our violation of agreement.<br /><br />2. Limitation of Liability (Clause 9):<br />   - Issue: Caps all damages at \$500, including direct damages.<br />   - Risk: Grossly inadequate for enterprise use. A critical failure could cost millions.<br />   - Deviation: Our standard allows for direct damages up to 12 months of fees paid.<br /><br />3. IP Ownership (Clause 12):<br />   - Issue: Grants vendor joint ownership of our modifications/integrations.<br />   - Risk: Vendor could use or sell our proprietary algorithms or data insights.<br />   - Deviation: Our standard retains full ownership of our work.<br /><br />4. Unusual Terms:<br />   - Clause 5.3: Vendor can use our usage data for "any purpose."<br />   - Clause 7.2: Vendor can terminate for "convenience" with only 7 days' notice.<br />   - Clause 11: No warranties of any kind, even for basic merchantability.<br />\</findings><br /><br />\<recommendations><br />1. Reject this agreement. Risks far outweigh benefits for an enterprise.<br />2. Counter-propose:<br />   - Indemnification: Limit to claims arising from our violation of agreement.<br />   - Liability: Cap at 12 months' fees for direct damages; negotiate for indirect.<br />   - IP: Full ownership of our modifications/integrations.<br />   - Data Use: Restrict to service improvement only.<br />   - Termination: Minimum 90 days' notice; only for cause.<br />   - Warranties: Demand basic merchantability and fitness for purpose.<br />3. If vendor refuses, explore alternative providers or in-house solutions.<br />4. Engage legal counsel for contract negotiation given high stakes.<br />\</recommendations> |
  </Accordion>
</AccordionGroup>

***

<CardGroup cols={3}>
  <Card title="Prompt library" icon="link" href="/en/resources/prompt-library/library">
    Get inspired by a curated selection of prompts for various tasks and use cases.
  </Card>

  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>

  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>


# Search results
Source: https://docs.claude.com/en/docs/build-with-claude/search-results

Enable natural citations for RAG applications by providing search results with source attribution

Search result content blocks enable natural citations with proper source attribution, bringing web search-quality citations to your custom applications. This feature is particularly powerful for RAG (Retrieval-Augmented Generation) applications where you need Claude to cite sources accurately.

The search results feature is available on the following models:

* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)
* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)
* Claude Sonnet 3.7 ([deprecated](/en/docs/about-claude/model-deprecations)) (`claude-3-7-sonnet-20250219`)
* Claude 3.5 Haiku (`claude-3-5-haiku-20241022`)

## Key benefits

* **Natural citations** - Achieve the same citation quality as web search for any content
* **Flexible integration** - Use in tool returns for dynamic RAG or as top-level content for pre-fetched data
* **Proper source attribution** - Each result includes source and title information for clear attribution
* **No document workarounds needed** - Eliminates the need for document-based workarounds
* **Consistent citation format** - Matches the citation quality and format of Claude's web search functionality

## How it works

Search results can be provided in two ways:

1. **From tool calls** - Your custom tools return search results, enabling dynamic RAG applications
2. **As top-level content** - You provide search results directly in user messages for pre-fetched or cached content

In both cases, Claude can automatically cite information from the search results with proper source attribution.

### Search result schema

Search results use the following structure:

```json  theme={null}
{
  "type": "search_result",
  "source": "https://example.com/article",  // Required: Source URL or identifier
  "title": "Article Title",                  // Required: Title of the result
  "content": [                               // Required: Array of text blocks
    {
      "type": "text",
      "text": "The actual content of the search result..."
    }
  ],
  "citations": {                             // Optional: Citation configuration
    "enabled": true                          // Enable/disable citations for this result
  }
}
```

### Required fields

| Field     | Type   | Description                                           |
| --------- | ------ | ----------------------------------------------------- |
| `type`    | string | Must be `"search_result"`                             |
| `source`  | string | The source URL or identifier for the content          |
| `title`   | string | A descriptive title for the search result             |
| `content` | array  | An array of text blocks containing the actual content |

### Optional fields

| Field           | Type   | Description                                            |
| --------------- | ------ | ------------------------------------------------------ |
| `citations`     | object | Citation configuration with `enabled` boolean field    |
| `cache_control` | object | Cache control settings (e.g., `{"type": "ephemeral"}`) |

Each item in the `content` array must be a text block with:

* `type`: Must be `"text"`
* `text`: The actual text content (non-empty string)

## Method 1: Search results from tool calls

The most powerful use case is returning search results from your custom tools. This enables dynamic RAG applications where tools fetch and return relevant content with automatic citations.

### Example: Knowledge base tool

<CodeGroup>
  ```python Python theme={null}
  from anthropic import Anthropic
  from anthropic.types import (
      MessageParam,
      TextBlockParam,
      SearchResultBlockParam,
      ToolResultBlockParam
  )

  client = Anthropic()

  # Define a knowledge base search tool
  knowledge_base_tool = {
      "name": "search_knowledge_base",
      "description": "Search the company knowledge base for information",
      "input_schema": {
          "type": "object",
          "properties": {
              "query": {
                  "type": "string",
                  "description": "The search query"
              }
          },
          "required": ["query"]
      }
  }

  # Function to handle the tool call
  def search_knowledge_base(query):
      # Your search logic here
      # Returns search results in the correct format
      return [
          SearchResultBlockParam(
              type="search_result",
              source="https://docs.company.com/product-guide",
              title="Product Configuration Guide",
              content=[
                  TextBlockParam(
                      type="text",
                      text="To configure the product, navigate to Settings > Configuration. The default timeout is 30 seconds, but can be adjusted between 10-120 seconds based on your needs."
                  )
              ],
              citations={"enabled": True}
          ),
          SearchResultBlockParam(
              type="search_result",
              source="https://docs.company.com/troubleshooting",
              title="Troubleshooting Guide",
              content=[
                  TextBlockParam(
                      type="text",
                      text="If you encounter timeout errors, first check the configuration settings. Common causes include network latency and incorrect timeout values."
                  )
              ],
              citations={"enabled": True}
          )
      ]

  # Create a message with the tool
  response = client.messages.create(
      model="claude-sonnet-4-5",  # Works with all supported models
      max_tokens=1024,
      tools=[knowledge_base_tool],
      messages=[
          MessageParam(
              role="user",
              content="How do I configure the timeout settings?"
          )
      ]
  )

  # When Claude calls the tool, provide the search results
  if response.content[0].type == "tool_use":
      tool_result = search_knowledge_base(response.content[0].input["query"])
      
      # Send the tool result back
      final_response = client.messages.create(
          model="claude-sonnet-4-5",  # Works with all supported models
          max_tokens=1024,
          messages=[
              MessageParam(role="user", content="How do I configure the timeout settings?"),
              MessageParam(role="assistant", content=response.content),
              MessageParam(
                  role="user",
                  content=[
                      ToolResultBlockParam(
                          type="tool_result",
                          tool_use_id=response.content[0].id,
                          content=tool_result  # Search results go here
                      )
                  ]
              )
          ]
      )
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Define a knowledge base search tool
  const knowledgeBaseTool = {
    name: "search_knowledge_base",
    description: "Search the company knowledge base for information",
    input_schema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "The search query"
        }
      },
      required: ["query"]
    }
  };

  // Function to handle the tool call
  function searchKnowledgeBase(query: string) {
    // Your search logic here
    // Returns search results in the correct format
    return [
      {
        type: "search_result" as const,
        source: "https://docs.company.com/product-guide",
        title: "Product Configuration Guide",
        content: [
          {
            type: "text" as const,
            text: "To configure the product, navigate to Settings > Configuration. The default timeout is 30 seconds, but can be adjusted between 10-120 seconds based on your needs."
          }
        ],
        citations: { enabled: true }
      },
      {
        type: "search_result" as const,
        source: "https://docs.company.com/troubleshooting",
        title: "Troubleshooting Guide",
        content: [
          {
            type: "text" as const,
            text: "If you encounter timeout errors, first check the configuration settings. Common causes include network latency and incorrect timeout values."
          }
        ],
        citations: { enabled: true }
      }
    ];
  }

  // Create a message with the tool
  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-5", // Works with all supported models
    max_tokens: 1024,
    tools: [knowledgeBaseTool],
    messages: [
      {
        role: "user",
        content: "How do I configure the timeout settings?"
      }
    ]
  });

  // Handle tool use and provide results
  if (response.content[0].type === "tool_use") {
    const toolResult = searchKnowledgeBase(response.content[0].input.query);
    
    const finalResponse = await anthropic.messages.create({
      model: "claude-sonnet-4-5", // Works with all supported models
      max_tokens: 1024,
        messages: [
        { role: "user", content: "How do I configure the timeout settings?" },
        { role: "assistant", content: response.content },
        {
          role: "user",
          content: [
            {
              type: "tool_result" as const,
              tool_use_id: response.content[0].id,
              content: toolResult  // Search results go here
            }
          ]
        }
      ]
    });
  }
  ```
</CodeGroup>

## Method 2: Search results as top-level content

You can also provide search results directly in user messages. This is useful for:

* Pre-fetched content from your search infrastructure
* Cached search results from previous queries
* Content from external search services
* Testing and development

### Example: Direct search results

<CodeGroup>
  ```python Python theme={null}
  from anthropic import Anthropic
  from anthropic.types import (
      MessageParam,
      TextBlockParam,
      SearchResultBlockParam
  )

  client = Anthropic()

  # Provide search results directly in the user message
  response = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          MessageParam(
              role="user",
              content=[
                  SearchResultBlockParam(
                      type="search_result",
                      source="https://docs.company.com/api-reference",
                      title="API Reference - Authentication",
                      content=[
                          TextBlockParam(
                              type="text",
                              text="All API requests must include an API key in the Authorization header. Keys can be generated from the dashboard. Rate limits: 1000 requests per hour for standard tier, 10000 for premium."
                          )
                      ],
                      citations={"enabled": True}
                  ),
                  SearchResultBlockParam(
                      type="search_result",
                      source="https://docs.company.com/quickstart",
                      title="Getting Started Guide",
                      content=[
                          TextBlockParam(
                              type="text",
                              text="To get started: 1) Sign up for an account, 2) Generate an API key from the dashboard, 3) Install our SDK using pip install company-sdk, 4) Initialize the client with your API key."
                          )
                      ],
                      citations={"enabled": True}
                  ),
                  TextBlockParam(
                      type="text",
                      text="Based on these search results, how do I authenticate API requests and what are the rate limits?"
                  )
              ]
          )
      ]
  )

  print(response.model_dump_json(indent=2))
  ```

  ```typescript TypeScript theme={null}
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  // Provide search results directly in the user message
  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "search_result" as const,
            source: "https://docs.company.com/api-reference",
            title: "API Reference - Authentication",
            content: [
              {
                type: "text" as const,
                text: "All API requests must include an API key in the Authorization header. Keys can be generated from the dashboard. Rate limits: 1000 requests per hour for standard tier, 10000 for premium."
              }
            ],
            citations: { enabled: true }
          },
          {
            type: "search_result" as const,
            source: "https://docs.company.com/quickstart",
            title: "Getting Started Guide",
            content: [
              {
                type: "text" as const,
                text: "To get started: 1) Sign up for an account, 2) Generate an API key from the dashboard, 3) Install our SDK using pip install company-sdk, 4) Initialize the client with your API key."
              }
            ],
            citations: { enabled: true }
          },
          {
            type: "text" as const,
            text: "Based on these search results, how do I authenticate API requests and what are the rate limits?"
          }
        ]
      }
    ]
  });

  console.log(response);
  ```

  ```bash Shell theme={null}
  #!/bin/sh
  curl https://api.anthropic.com/v1/messages \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01" \
       --header "content-type: application/json" \
       --data \
  '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
          {
              "role": "user",
              "content": [
                  {
                      "type": "search_result",
                      "source": "https://docs.company.com/api-reference",
                      "title": "API Reference - Authentication",
                      "content": [
                          {
                              "type": "text",
                              "text": "All API requests must include an API key in the Authorization header. Keys can be generated from the dashboard. Rate limits: 1000 requests per hour for standard tier, 10000 for premium."
                          }
                      ],
                      "citations": {
                          "enabled": true
                      }
                  },
                  {
                      "type": "search_result",
                      "source": "https://docs.company.com/quickstart",
                      "title": "Getting Started Guide",
                      "content": [
                          {
                              "type": "text",
                              "text": "To get started: 1) Sign up for an account, 2) Generate an API key from the dashboard, 3) Install our SDK using pip install company-sdk, 4) Initialize the client with your API key."
                          }
                      ],
                      "citations": {
                          "enabled": true
                      }
                  },
                  {
                      "type": "text",
                      "text": "Based on these search results, how do I authenticate API requests and what are the rate limits?"
                  }
              ]
          }
      ]
  }'
  ```
</CodeGroup>

## Claude's response with citations

Regardless of how search results are provided, Claude automatically includes citations when using information from them:

```json  theme={null}
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "To authenticate API requests, you need to include an API key in the Authorization header",
      "citations": [
        {
          "type": "search_result_location",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "cited_text": "All API requests must include an API key in the Authorization header",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 0
        }
      ]
    },
    {
      "type": "text",
      "text": ". You can generate API keys from your dashboard",
      "citations": [
        {
          "type": "search_result_location",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "cited_text": "Keys can be generated from the dashboard",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 0
        }
      ]
    },
    {
      "type": "text",
      "text": ". The rate limits are 1,000 requests per hour for the standard tier and 10,000 requests per hour for the premium tier.",
      "citations": [
        {
          "type": "search_result_location",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "cited_text": "Rate limits: 1000 requests per hour for standard tier, 10000 for premium",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 0
        }
      ]
    }
  ]
}
```

### Citation fields

Each citation includes:

| Field                 | Type           | Description                                                   |
| --------------------- | -------------- | ------------------------------------------------------------- |
| `type`                | string         | Always `"search_result_location"` for search result citations |
| `source`              | string         | The source from the original search result                    |
| `title`               | string or null | The title from the original search result                     |
| `cited_text`          | string         | The exact text being cited                                    |
| `search_result_index` | integer        | Index of the search result (0-based)                          |
| `start_block_index`   | integer        | Starting position in the content array                        |
| `end_block_index`     | integer        | Ending position in the content array                          |

Note: The `search_result_index` refers to the index of the search result content block (0-based), regardless of how the search results were provided (tool call or top-level content).

## Multiple content blocks

Search results can contain multiple text blocks in the `content` array:

```json  theme={null}
{
  "type": "search_result",
  "source": "https://docs.company.com/api-guide",
  "title": "API Documentation",
  "content": [
    {
      "type": "text",
      "text": "Authentication: All API requests require an API key."
    },
    {
      "type": "text",
      "text": "Rate Limits: The API allows 1000 requests per hour per key."
    },
    {
      "type": "text",
      "text": "Error Handling: The API returns standard HTTP status codes."
    }
  ]
}
```

Claude can cite specific blocks using the `start_block_index` and `end_block_index` fields.

## Advanced usage

### Combining both methods

You can use both tool-based and top-level search results in the same conversation:

```python  theme={null}
# First message with top-level search results
messages = [
    MessageParam(
        role="user",
        content=[
            SearchResultBlockParam(
                type="search_result",
                source="https://docs.company.com/overview",
                title="Product Overview",
                content=[
                    TextBlockParam(type="text", text="Our product helps teams collaborate...")
                ],
                citations={"enabled": True}
            ),
            TextBlockParam(
                type="text",
                text="Tell me about this product and search for pricing information"
            )
        ]
    )
]

# Claude might respond and call a tool to search for pricing
# Then you provide tool results with more search results
```

### Combining with other content types

Both methods support mixing search results with other content:

```python  theme={null}
# In tool results
tool_result = [
    SearchResultBlockParam(
        type="search_result",
        source="https://docs.company.com/guide",
        title="User Guide",
        content=[TextBlockParam(type="text", text="Configuration details...")],
        citations={"enabled": True}
    ),
    TextBlockParam(
        type="text",
        text="Additional context: This applies to version 2.0 and later."
    )
]

# In top-level content
user_content = [
    SearchResultBlockParam(
        type="search_result",
        source="https://research.com/paper",
        title="Research Paper",
        content=[TextBlockParam(type="text", text="Key findings...")],
        citations={"enabled": True}
    ),
    {
        "type": "image",
        "source": {"type": "url", "url": "https://example.com/chart.png"}
    },
    TextBlockParam(
        type="text",
        text="How does the chart relate to the research findings?"
    )
]
```

### Cache control

Add cache control for better performance:

```json  theme={null}
{
  "type": "search_result",
  "source": "https://docs.company.com/guide",
  "title": "User Guide",
  "content": [{"type": "text", "text": "..."}],
  "cache_control": {
    "type": "ephemeral"
  }
}
```

### Citation control

By default, citations are disabled for search results. You can enable citations by explicitly setting the `citations` configuration:

```json  theme={null}
{
  "type": "search_result",
  "source": "https://docs.company.com/guide",
  "title": "User Guide",
  "content": [{"type": "text", "text": "Important documentation..."}],
  "citations": {
    "enabled": true  // Enable citations for this result
  }
}
```

When `citations.enabled` is set to `true`, Claude will include citation references when using information from the search result. This enables:

* Natural citations for your custom RAG applications
* Source attribution when interfacing with proprietary knowledge bases
* Web search-quality citations for any custom tool that returns search results

If the `citations` field is omitted, citations are disabled by default.

<Warning>
  Citations are all-or-nothing: either all search results in a request must have citations enabled, or all must have them disabled. Mixing search results with different citation settings will result in an error. If you need to disable citations for some sources, you must disable them for all search results in that request.
</Warning>

## Best practices

### For tool-based search (Method 1)

* **Dynamic content**: Use for real-time searches and dynamic RAG applications
* **Error handling**: Return appropriate messages when searches fail
* **Result limits**: Return only the most relevant results to avoid context overflow

### For top-level search (Method 2)

* **Pre-fetched content**: Use when you already have search results
* **Batch processing**: Ideal for processing multiple search results at once
* **Testing**: Great for testing citation behavior with known content

### General best practices

1. **Structure results effectively**
   * Use clear, permanent source URLs
   * Provide descriptive titles
   * Break long content into logical text blocks

2. **Maintain consistency**
   * Use consistent source formats across your application
   * Ensure titles accurately reflect content
   * Keep formatting consistent

3. **Handle errors gracefully**
   ```python  theme={null}
   def search_with_fallback(query):
       try:
           results = perform_search(query)
           if not results:
               return {"type": "text", "text": "No results found."}
           return format_as_search_results(results)
       except Exception as e:
           return {"type": "text", "text": f"Search error: {str(e)}"}
   ```

## Limitations

* Search result content blocks are available on Claude API and Google Cloud's Vertex AI
* Only text content is supported within search results (no images or other media)
* The `content` array must contain at least one text block


# Using Agent Skills with the API
Source: https://docs.claude.com/en/docs/build-with-claude/skills-guide

Learn how to use Agent Skills to extend Claude's capabilities through the API.

Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.

<Note>
  For complete API reference including request/response schemas and all parameters, see:

  * [Skill Management API Reference](/en/api/skills/list-skills) - CRUD operations for Skills
  * [Skill Versions API Reference](/en/api/skills/list-skill-versions) - Version management
</Note>

## Quick Links

<CardGroup cols={2}>
  <Card title="Get started with Agent Skills" icon="rocket" href="/en/docs/agents-and-tools/agent-skills/quickstart">
    Create your first Skill
  </Card>

  <Card title="Create Custom Skills" icon="hammer" href="/en/docs/agents-and-tools/agent-skills/best-practices">
    Best practices for authoring Skills
  </Card>
</CardGroup>

## Overview

<Note>
  For a deep dive into the architecture and real-world applications of Agent Skills, read our engineering blog: [Equipping agents for the real world with Agent Skills](https://https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills-skills).
</Note>

Skills integrate with the Messages API through the code execution tool. Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical—both require code execution and use the same `container` structure.

### Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.

**You can use Skills from two sources:**

| Aspect             | Anthropic Skills                           | Custom Skills                                                   |
| ------------------ | ------------------------------------------ | --------------------------------------------------------------- |
| **Type value**     | `anthropic`                                | `custom`                                                        |
| **Skill IDs**      | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv`                     |
| **Version format** | Date-based: `20251013` or `latest`         | Epoch timestamp: `1759178010641129` or `latest`                 |
| **Management**     | Pre-built and maintained by Anthropic      | Upload and manage via [Skills API](/en/api/skills/create-skill) |
| **Availability**   | Available to all users                     | Private to your workspace                                       |

Both skill sources are returned by the [List Skills endpoint](/en/api/skills/list-skills) (use the `source` parameter to filter). The integration shape and execution environment are identical—the only difference is where the Skills come from and how they're managed.

### Prerequisites

To use Skills, you need:

1. **Anthropic API key** from the [Console](https://console.anthropic.com/settings/keys)
2. **Beta headers**:
   * `code-execution-2025-08-25` - Enables code execution (required for Skills)
   * `skills-2025-10-02` - Enables Skills API
   * `files-api-2025-04-14` - For uploading/downloading files to/from container
3. **Code execution tool** enabled in your requests

***

## Using Skills in Messages

### Container Parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills per request.

The structure is identical for both Anthropic and custom Skills—specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "pptx",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Create a presentation about renewable energy"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'pptx',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Create a presentation about renewable energy'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
  ```

  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "anthropic",
            "skill_id": "pptx",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Create a presentation about renewable energy"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
  ```
</CodeGroup>

### Downloading Generated Files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**

1. Skills create files during code execution
2. Response includes `file_id` for each created file
3. Use Files API to download the actual file content
4. Save locally or process as needed

**Example: Creating and downloading an Excel file**

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Step 1: Use a Skill to create a file
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=[{
          "role": "user",
          "content": "Create an Excel file with a simple budget spreadsheet"
      }],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Step 2: Extract file IDs from the response
  def extract_file_ids(response):
      file_ids = []
      for item in response.content:
          if item.type == 'bash_code_execution_tool_result':
              content_item = item.content
              if content_item.type == 'bash_code_execution_result':
                  for file in content_item.content:
                      if hasattr(file, 'file_id'):
                          file_ids.append(file.file_id)
      return file_ids

  # Step 3: Download the file using Files API
  for file_id in extract_file_ids(response):
      file_metadata = client.beta.files.retrieve_metadata(
          file_id=file_id,
          betas=["files-api-2025-04-14"]
      )
      file_content = client.beta.files.download(
          file_id=file_id,
          betas=["files-api-2025-04-14"]
      )

      # Step 4: Save to disk
      file_content.write_to_file(file_metadata.filename)
      print(f"Downloaded: {file_metadata.filename}")
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  // Step 1: Use a Skill to create a file
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages: [{
      role: 'user',
      content: 'Create an Excel file with a simple budget spreadsheet'
    }],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Step 2: Extract file IDs from the response
  function extractFileIds(response: any): string[] {
    const fileIds: string[] = [];
    for (const item of response.content) {
      if (item.type === 'bash_code_execution_tool_result') {
        const contentItem = item.content;
        if (contentItem.type === 'bash_code_execution_result') {
          for (const file of contentItem.content) {
            if ('file_id' in file) {
              fileIds.push(file.file_id);
            }
          }
        }
      }
    }
    return fileIds;
  }

  // Step 3: Download the file using Files API
  const fs = require('fs');
  for (const fileId of extractFileIds(response)) {
    const fileMetadata = await client.beta.files.retrieve_metadata(fileId, {
      betas: ['files-api-2025-04-14']
    });
    const fileContent = await client.beta.files.download(fileId, {
      betas: ['files-api-2025-04-14']
    });

    // Step 4: Save to disk
    fs.writeFileSync(fileMetadata.filename, Buffer.from(await fileContent.arrayBuffer()));
    console.log(`Downloaded: ${fileMetadata.filename}`);
  }
  ```

  ```bash Shell theme={null}
  # Step 1: Use a Skill to create a file
  RESPONSE=$(curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Create an Excel file with a simple budget spreadsheet"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }')

  # Step 2: Extract file_id from response (using jq)
  FILE_ID=$(echo "$RESPONSE" | jq -r '.content[] | select(.type=="bash_code_execution_tool_result") | .content | select(.type=="bash_code_execution_result") | .content[] | select(.file_id) | .file_id')

  # Step 3: Get filename from metadata
  FILENAME=$(curl "https://api.anthropic.com/v1/files/$FILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" | jq -r '.filename')

  # Step 4: Download the file using Files API
  curl "https://api.anthropic.com/v1/files/$FILE_ID/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    --output "$FILENAME"

  echo "Downloaded: $FILENAME"
  ```
</CodeGroup>

**Additional Files API operations:**

<CodeGroup>
  ```python Python theme={null}
  # Get file metadata
  file_info = client.beta.files.retrieve_metadata(
      file_id=file_id,
      betas=["files-api-2025-04-14"]
  )
  print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

  # List all files
  files = client.beta.files.list(betas=["files-api-2025-04-14"])
  for file in files.data:
      print(f"{file.filename} - {file.created_at}")

  # Delete a file
  client.beta.files.delete(
      file_id=file_id,
      betas=["files-api-2025-04-14"]
  )
  ```

  ```typescript TypeScript theme={null}
  // Get file metadata
  const fileInfo = await client.beta.files.retrieve_metadata(fileId, {
    betas: ['files-api-2025-04-14']
  });
  console.log(`Filename: ${fileInfo.filename}, Size: ${fileInfo.size_bytes} bytes`);

  // List all files
  const files = await client.beta.files.list({
    betas: ['files-api-2025-04-14']
  });
  for (const file of files.data) {
    console.log(`${file.filename} - ${file.created_at}`);
  }

  // Delete a file
  await client.beta.files.delete(fileId, {
    betas: ['files-api-2025-04-14']
  });
  ```

  ```bash Shell theme={null}
  # Get file metadata
  curl "https://api.anthropic.com/v1/files/$FILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"

  # List all files
  curl "https://api.anthropic.com/v1/files" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"

  # Delete a file
  curl -X DELETE "https://api.anthropic.com/v1/files/$FILE_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14"
  ```
</CodeGroup>

<Note>
  For complete details on the Files API, see the [Files API documentation](/en/api/files-content).
</Note>

### Multi-Turn Conversations

Reuse the same container across multiple messages by specifying the container ID:

<CodeGroup>
  ```python Python theme={null}
  # First request creates container
  response1 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=[{"role": "user", "content": "Analyze this sales data"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Continue conversation with same container
  messages = [
      {"role": "user", "content": "Analyze this sales data"},
      {"role": "assistant", "content": response1.content},
      {"role": "user", "content": "What was the total revenue?"}
  ]

  response2 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "id": response1.container.id,  # Reuse container
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=messages,
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
  ```

  ```typescript TypeScript theme={null}
  // First request creates container
  const response1 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages: [{role: 'user', content: 'Analyze this sales data'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Continue conversation with same container
  const messages = [
    {role: 'user', content: 'Analyze this sales data'},
    {role: 'assistant', content: response1.content},
    {role: 'user', content: 'What was the total revenue?'}
  ];

  const response2 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      id: response1.container.id,  // Reuse container
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages,
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
  ```
</CodeGroup>

### Long-Running Operations

Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:

<CodeGroup>
  ```python Python theme={null}
  messages = [{"role": "user", "content": "Process this large dataset"}]
  max_retries = 10

  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
          ]
      },
      messages=messages,
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Handle pause_turn for long operations
  for i in range(max_retries):
      if response.stop_reason != "pause_turn":
          break

      messages.append({"role": "assistant", "content": response.content})
      response = client.beta.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=4096,
          betas=["code-execution-2025-08-25", "skills-2025-10-02"],
          container={
              "id": response.container.id,
              "skills": [
                  {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
              ]
          },
          messages=messages,
          tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
      )
  ```

  ```typescript TypeScript theme={null}
  let messages = [{role: 'user' as const, content: 'Process this large dataset'}];
  const maxRetries = 10;

  let response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'custom', skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv', version: 'latest'}
      ]
    },
    messages,
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Handle pause_turn for long operations
  for (let i = 0; i < maxRetries; i++) {
    if (response.stop_reason !== 'pause_turn') {
      break;
    }

    messages.push({role: 'assistant', content: response.content});
    response = await client.beta.messages.create({
      model: 'claude-sonnet-4-5-20250929',
      max_tokens: 4096,
      betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
      container: {
        id: response.container.id,
        skills: [
          {type: 'custom', skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv', version: 'latest'}
        ]
      },
      messages,
      tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
    });
  }
  ```

  ```bash Shell theme={null}
  # Initial request
  RESPONSE=$(curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Process this large dataset"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }')

  # Check stop_reason and handle pause_turn in a loop
  STOP_REASON=$(echo "$RESPONSE" | jq -r '.stop_reason')
  CONTAINER_ID=$(echo "$RESPONSE" | jq -r '.container.id')

  while [ "$STOP_REASON" = "pause_turn" ]; do
    # Continue with same container
    RESPONSE=$(curl https://api.anthropic.com/v1/messages \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
      -H "content-type: application/json" \
      -d "{
        \"model\": \"claude-sonnet-4-5-20250929\",
        \"max_tokens\": 4096,
        \"container\": {
          \"id\": \"$CONTAINER_ID\",
          \"skills\": [{
            \"type\": \"custom\",
            \"skill_id\": \"skill_01AbCdEfGhIjKlMnOpQrStUv\",
            \"version\": \"latest\"
          }]
        },
        \"messages\": [/* include conversation history */],
        \"tools\": [{
          \"type\": \"code_execution_20250825\",
          \"name\": \"code_execution\"
        }]
      }")

    STOP_REASON=$(echo "$RESPONSE" | jq -r '.stop_reason')
  done
  ```
</CodeGroup>

<Note>
  The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation and provide additional guidance.
</Note>

### Using Multiple Skills

Combine multiple Skills in a single request to handle complex workflows:

<CodeGroup>
  ```python Python theme={null}
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {
                  "type": "anthropic",
                  "skill_id": "xlsx",
                  "version": "latest"
              },
              {
                  "type": "anthropic",
                  "skill_id": "pptx",
                  "version": "latest"
              },
              {
                  "type": "custom",
                  "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                  "version": "latest"
              }
          ]
      },
      messages=[{
          "role": "user",
          "content": "Analyze sales data and create a presentation"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
  ```

  ```typescript TypeScript theme={null}
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {
          type: 'anthropic',
          skill_id: 'xlsx',
          version: 'latest'
        },
        {
          type: 'anthropic',
          skill_id: 'pptx',
          version: 'latest'
        },
        {
          type: 'custom',
          skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv',
          version: 'latest'
        }
      ]
    },
    messages: [{
      role: 'user',
      content: 'Analyze sales data and create a presentation'
    }],
    tools: [{
      type: 'code_execution_20250825',
      name: 'code_execution'
    }]
  });
  ```

  ```bash Shell theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {
            "type": "anthropic",
            "skill_id": "xlsx",
            "version": "latest"
          },
          {
            "type": "anthropic",
            "skill_id": "pptx",
            "version": "latest"
          },
          {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest"
          }
        ]
      },
      "messages": [{
        "role": "user",
        "content": "Analyze sales data and create a presentation"
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
  ```
</CodeGroup>

***

## Managing Custom Skills

### Creating a Skill

Upload your custom Skill to make it available in your workspace. You can upload using either a directory path or individual file objects.

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  # Option 1: Using files_from_dir helper (Python only, recommended)
  from anthropic.lib import files_from_dir

  skill = client.beta.skills.create(
      display_title="Financial Analysis",
      files=files_from_dir("/path/to/financial_analysis_skill"),
      betas=["skills-2025-10-02"]
  )

  # Option 2: Using a zip file
  skill = client.beta.skills.create(
      display_title="Financial Analysis",
      files=[("skill.zip", open("financial_analysis_skill.zip", "rb"))],
      betas=["skills-2025-10-02"]
  )

  # Option 3: Using file tuples (filename, file_content, mime_type)
  skill = client.beta.skills.create(
      display_title="Financial Analysis",
      files=[
          ("financial_skill/SKILL.md", open("financial_skill/SKILL.md", "rb"), "text/markdown"),
          ("financial_skill/analyze.py", open("financial_skill/analyze.py", "rb"), "text/x-python"),
      ],
      betas=["skills-2025-10-02"]
  )

  print(f"Created skill: {skill.id}")
  print(f"Latest version: {skill.latest_version}")
  ```

  ```typescript TypeScript theme={null}
  import Anthropic, { toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const client = new Anthropic();

  // Option 1: Using a zip file
  const skill = await client.beta.skills.create({
    displayTitle: 'Financial Analysis',
    files: [
      await toFile(
        fs.createReadStream('financial_analysis_skill.zip'),
        'skill.zip'
      )
    ],
    betas: ['skills-2025-10-02']
  });

  // Option 2: Using individual file objects
  const skill = await client.beta.skills.create({
    displayTitle: 'Financial Analysis',
    files: [
      await toFile(
        fs.createReadStream('financial_skill/SKILL.md'),
        'financial_skill/SKILL.md',
        { type: 'text/markdown' }
      ),
      await toFile(
        fs.createReadStream('financial_skill/analyze.py'),
        'financial_skill/analyze.py',
        { type: 'text/x-python' }
      ),
    ],
    betas: ['skills-2025-10-02']
  });

  console.log(`Created skill: ${skill.id}`);
  console.log(`Latest version: ${skill.latest_version}`);
  ```

  ```bash Shell theme={null}
  curl -X POST "https://api.anthropic.com/v1/skills" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02" \
    -F "display_title=Financial Analysis" \
    -F "files[]=@financial_skill/SKILL.md;filename=financial_skill/SKILL.md" \
    -F "files[]=@financial_skill/analyze.py;filename=financial_skill/analyze.py"
  ```
</CodeGroup>

**Requirements:**

* Must include a SKILL.md file at the top level
* All files must specify a common root directory in their paths
* Total upload size must be under 8MB
* YAML frontmatter requirements:
  * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  * `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](/en/api/skills/create-skill).

### Listing Skills

Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:

<CodeGroup>
  ```python Python theme={null}
  # List all Skills
  skills = client.beta.skills.list(
      betas=["skills-2025-10-02"]
  )

  for skill in skills.data:
      print(f"{skill.id}: {skill.display_title} (source: {skill.source})")

  # List only custom Skills
  custom_skills = client.beta.skills.list(
      source="custom",
      betas=["skills-2025-10-02"]
  )
  ```

  ```typescript TypeScript theme={null}
  // List all Skills
  const skills = await client.beta.skills.list({
    betas: ['skills-2025-10-02']
  });

  for (const skill of skills.data) {
    console.log(`${skill.id}: ${skill.display_title} (source: ${skill.source})`);
  }

  // List only custom Skills
  const customSkills = await client.beta.skills.list({
    source: 'custom',
    betas: ['skills-2025-10-02']
  });
  ```

  ```bash Shell theme={null}
  # List all Skills
  curl "https://api.anthropic.com/v1/skills" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"

  # List only custom Skills
  curl "https://api.anthropic.com/v1/skills?source=custom" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
  ```
</CodeGroup>

See the [List Skills API reference](/en/api/skills/list-skills) for pagination and filtering options.

### Retrieving a Skill

Get details about a specific Skill:

<CodeGroup>
  ```python Python theme={null}
  skill = client.beta.skills.retrieve(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      betas=["skills-2025-10-02"]
  )

  print(f"Skill: {skill.display_title}")
  print(f"Latest version: {skill.latest_version}")
  print(f"Created: {skill.created_at}")
  ```

  ```typescript TypeScript theme={null}
  const skill = await client.beta.skills.retrieve(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    { betas: ['skills-2025-10-02'] }
  );

  console.log(`Skill: ${skill.display_title}`);
  console.log(`Latest version: ${skill.latest_version}`);
  console.log(`Created: ${skill.created_at}`);
  ```

  ```bash Shell theme={null}
  curl "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
  ```
</CodeGroup>

### Deleting a Skill

To delete a Skill, you must first delete all its versions:

<CodeGroup>
  ```python Python theme={null}
  # Step 1: Delete all versions
  versions = client.beta.skills.versions.list(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      betas=["skills-2025-10-02"]
  )

  for version in versions.data:
      client.beta.skills.versions.delete(
          skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
          version=version.version,
          betas=["skills-2025-10-02"]
      )

  # Step 2: Delete the Skill
  client.beta.skills.delete(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      betas=["skills-2025-10-02"]
  )
  ```

  ```typescript TypeScript theme={null}
  // Step 1: Delete all versions
  const versions = await client.beta.skills.versions.list(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    { betas: ['skills-2025-10-02'] }
  );

  for (const version of versions.data) {
    await client.beta.skills.versions.delete(
      'skill_01AbCdEfGhIjKlMnOpQrStUv',
      version.version,
      { betas: ['skills-2025-10-02'] }
    );
  }

  // Step 2: Delete the Skill
  await client.beta.skills.delete(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    { betas: ['skills-2025-10-02'] }
  );
  ```

  ```bash Shell theme={null}
  # Delete all versions first, then delete the Skill
  curl -X DELETE "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02"
  ```
</CodeGroup>

Attempting to delete a Skill with existing versions will return a 400 error.

### Versioning

Skills support versioning to manage updates safely:

**Anthropic-Managed Skills**:

* Versions use date format: `20251013`
* New versions released as updates are made
* Specify exact versions for stability

**Custom Skills**:

* Auto-generated epoch timestamps: `1759178010641129`
* Use `"latest"` to always get the most recent version
* Create new versions when updating Skill files

<CodeGroup>
  ```python Python theme={null}
  # Create a new version
  from anthropic.lib import files_from_dir

  new_version = client.beta.skills.versions.create(
      skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
      files=files_from_dir("/path/to/updated_skill"),
      betas=["skills-2025-10-02"]
  )

  # Use specific version
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [{
              "type": "custom",
              "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
              "version": new_version.version
          }]
      },
      messages=[{"role": "user", "content": "Use updated Skill"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Use latest version
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [{
              "type": "custom",
              "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
              "version": "latest"
          }]
      },
      messages=[{"role": "user", "content": "Use latest Skill version"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
  ```

  ```typescript TypeScript theme={null}
  // Create a new version using a zip file
  const fs = require('fs');

  const newVersion = await client.beta.skills.versions.create(
    'skill_01AbCdEfGhIjKlMnOpQrStUv',
    {
      files: [
        fs.createReadStream('updated_skill.zip')
      ],
      betas: ['skills-2025-10-02']
    }
  );

  // Use specific version
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [{
        type: 'custom',
        skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv',
        version: newVersion.version
      }]
    },
    messages: [{role: 'user', content: 'Use updated Skill'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Use latest version
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [{
        type: 'custom',
        skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv',
        version: 'latest'
      }]
    },
    messages: [{role: 'user', content: 'Use latest Skill version'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
  ```

  ```bash Shell theme={null}
  # Create a new version
  NEW_VERSION=$(curl -X POST "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv/versions" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02" \
    -F "files[]=@updated_skill/SKILL.md;filename=updated_skill/SKILL.md")

  VERSION_NUMBER=$(echo "$NEW_VERSION" | jq -r '.version')

  # Use specific version
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d "{
      \"model\": \"claude-sonnet-4-5-20250929\",
      \"max_tokens\": 4096,
      \"container\": {
        \"skills\": [{
          \"type\": \"custom\",
          \"skill_id\": \"skill_01AbCdEfGhIjKlMnOpQrStUv\",
          \"version\": \"$VERSION_NUMBER\"
        }]
      },
      \"messages\": [{\"role\": \"user\", \"content\": \"Use updated Skill\"}],
      \"tools\": [{\"type\": \"code_execution_20250825\", \"name\": \"code_execution\"}]
    }"

  # Use latest version
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [{
          "type": "custom",
          "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
          "version": "latest"
        }]
      },
      "messages": [{"role": "user", "content": "Use latest Skill version"}],
      "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
    }'
  ```
</CodeGroup>

See the [Create Skill Version API reference](/en/api/skills/create-skill-version) for complete details.

***

## How Skills Are Loaded

When you specify Skills in a container:

1. **Metadata Discovery**: Claude sees metadata for each Skill (name, description) in the system prompt
2. **File Loading**: Skill files are copied into the container at `/skills/{directory}/`
3. **Automatic Use**: Claude automatically loads and uses Skills when relevant to your request
4. **Composition**: Multiple Skills compose together for complex workflows

The progressive disclosure architecture ensures efficient context usage—Claude only loads full Skill instructions when needed.

***

## Use Cases

### Organizational Skills

**Brand & Communications**

* Apply company-specific formatting (colors, fonts, layouts) to documents
* Generate communications following organizational templates
* Ensure consistent brand guidelines across all outputs

**Project Management**

* Structure notes with company-specific formats (OKRs, decision logs)
* Generate tasks following team conventions
* Create standardized meeting recaps and status updates

**Business Operations**

* Create company-standard reports, proposals, and analyses
* Execute company-specific analytical procedures
* Generate financial models following organizational templates

### Personal Skills

**Content Creation**

* Custom document templates
* Specialized formatting and styling
* Domain-specific content generation

**Data Analysis**

* Custom data processing pipelines
* Specialized visualization templates
* Industry-specific analytical methods

**Development & Automation**

* Code generation templates
* Testing frameworks
* Deployment workflows

### Example: Financial Modeling

Combine Excel and custom DCF analysis Skills:

<CodeGroup>
  ```python Python theme={null}
  # Create custom DCF analysis Skill
  from anthropic.lib import files_from_dir

  dcf_skill = client.beta.skills.create(
      display_title="DCF Analysis",
      files=files_from_dir("/path/to/dcf_skill"),
      betas=["skills-2025-10-02"]
  )

  # Use with Excel to create financial model
  response = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
              {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"}
          ]
      },
      messages=[{
          "role": "user",
          "content": "Build a DCF valuation model for a SaaS company with the attached financials"
      }],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
  ```

  ```typescript TypeScript theme={null}
  // Create custom DCF analysis Skill
  import { toFile } from '@anthropic-ai/sdk';
  import fs from 'fs';

  const dcfSkill = await client.beta.skills.create({
    displayTitle: 'DCF Analysis',
    files: [
      await toFile(fs.createReadStream('dcf_skill.zip'), 'skill.zip')
    ],
    betas: ['skills-2025-10-02']
  });

  // Use with Excel to create financial model
  const response = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'},
        {type: 'custom', skill_id: dcfSkill.id, version: 'latest'}
      ]
    },
    messages: [{
      role: 'user',
      content: 'Build a DCF valuation model for a SaaS company with the attached financials'
    }],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
  ```

  ```bash Shell theme={null}
  # Create custom DCF analysis Skill
  DCF_SKILL=$(curl -X POST "https://api.anthropic.com/v1/skills" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: skills-2025-10-02" \
    -F "display_title=DCF Analysis" \
    -F "files[]=@dcf_skill/SKILL.md;filename=dcf_skill/SKILL.md")

  DCF_SKILL_ID=$(echo "$DCF_SKILL" | jq -r '.id')

  # Use with Excel to create financial model
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d "{
      \"model\": \"claude-sonnet-4-5-20250929\",
      \"max_tokens\": 4096,
      \"container\": {
        \"skills\": [
          {
            \"type\": \"anthropic\",
            \"skill_id\": \"xlsx\",
            \"version\": \"latest\"
          },
          {
            \"type\": \"custom\",
            \"skill_id\": \"$DCF_SKILL_ID\",
            \"version\": \"latest\"
          }
        ]
      },
      \"messages\": [{
        \"role\": \"user\",
        \"content\": \"Build a DCF valuation model for a SaaS company with the attached financials\"
      }],
      \"tools\": [{
        \"type\": \"code_execution_20250825\",
        \"name\": \"code_execution\"
      }]
    }"
  ```
</CodeGroup>

***

## Limits and Constraints

### Request Limits

* **Maximum Skills per request**: 8
* **Maximum Skill upload size**: 8MB (all files combined)
* **YAML frontmatter requirements**:
  * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words
  * `description`: Maximum 1024 characters, non-empty, no XML tags

### Environment Constraints

Skills run in the code execution container with these limitations:

* **No network access** - Cannot make external API calls
* **No runtime package installation** - Only pre-installed packages available
* **Isolated environment** - Each request gets a fresh container

See the [code execution tool documentation](/en/docs/agents-and-tools/tool-use/code-execution-tool) for available packages.

***

## Best Practices

### When to Use Multiple Skills

Combine Skills when tasks involve multiple document types or domains:

**Good use cases:**

* Data analysis (Excel) + presentation creation (PowerPoint)
* Report generation (Word) + export to PDF
* Custom domain logic + document generation

**Avoid:**

* Including unused Skills (impacts performance)

### Version Management Strategy

**For production:**

```python  theme={null}
# Pin to specific versions for stability
container={
    "skills": [{
        "type": "custom",
        "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
        "version": "1759178010641129"  # Specific version
    }]
}
```

**For development:**

```python  theme={null}
# Use latest for active development
container={
    "skills": [{
        "type": "custom",
        "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
        "version": "latest"  # Always get newest
    }]
}
```

### Prompt Caching Considerations

When using prompt caching, note that changing the Skills list in your container will break the cache:

<CodeGroup>
  ```python Python theme={null}
  # First request creates cache
  response1 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
          ]
      },
      messages=[{"role": "user", "content": "Analyze sales data"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )

  # Adding/removing Skills breaks cache
  response2 = client.beta.messages.create(
      model="claude-sonnet-4-5-20250929",
      max_tokens=4096,
      betas=["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
      container={
          "skills": [
              {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
              {"type": "anthropic", "skill_id": "pptx", "version": "latest"}  # Cache miss
          ]
      },
      messages=[{"role": "user", "content": "Create a presentation"}],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
  )
  ```

  ```typescript TypeScript theme={null}
  // First request creates cache
  const response1 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02', 'prompt-caching-2024-07-31'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'}
      ]
    },
    messages: [{role: 'user', content: 'Analyze sales data'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });

  // Adding/removing Skills breaks cache
  const response2 = await client.beta.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 4096,
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02', 'prompt-caching-2024-07-31'],
    container: {
      skills: [
        {type: 'anthropic', skill_id: 'xlsx', version: 'latest'},
        {type: 'anthropic', skill_id: 'pptx', version: 'latest'}  // Cache miss
      ]
    },
    messages: [{role: 'user', content: 'Create a presentation'}],
    tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
  });
  ```

  ```bash Shell theme={null}
  # First request creates cache
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02,prompt-caching-2024-07-31" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
      },
      "messages": [{"role": "user", "content": "Analyze sales data"}],
      "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
    }'

  # Adding/removing Skills breaks cache
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02,prompt-caching-2024-07-31" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5-20250929",
      "max_tokens": 4096,
      "container": {
        "skills": [
          {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
          {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
        ]
      },
      "messages": [{"role": "user", "content": "Create a presentation"}],
      "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
    }'
  ```
</CodeGroup>

For best caching performance, keep your Skills list consistent across requests.

### Error Handling

Handle Skill-related errors gracefully:

<CodeGroup>
  ```python Python theme={null}
  try:
      response = client.beta.messages.create(
          model="claude-sonnet-4-5-20250929",
          max_tokens=4096,
          betas=["code-execution-2025-08-25", "skills-2025-10-02"],
          container={
              "skills": [
                  {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
              ]
          },
          messages=[{"role": "user", "content": "Process data"}],
          tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
      )
  except anthropic.BadRequestError as e:
      if "skill" in str(e):
          print(f"Skill error: {e}")
          # Handle skill-specific errors
      else:
          raise
  ```

  ```typescript TypeScript theme={null}
  try {
    const response = await client.beta.messages.create({
      model: 'claude-sonnet-4-5-20250929',
      max_tokens: 4096,
      betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
      container: {
        skills: [
          {type: 'custom', skill_id: 'skill_01AbCdEfGhIjKlMnOpQrStUv', version: 'latest'}
        ]
      },
      messages: [{role: 'user', content: 'Process data'}],
      tools: [{type: 'code_execution_20250825', name: 'code_execution'}]
    });
  } catch (error) {
    if (error instanceof Anthropic.BadRequestError && error.message.includes('skill')) {
      console.error(`Skill error: ${error.message}`);
      // Handle skill-specific errors
    } else {
      throw error;
    }
  }
  ```
</CodeGroup>

***

## Next Steps

<CardGroup cols={2}>
  <Card title="API Reference" icon="book" href="/en/api/skills/create-skill">
    Complete API reference with all endpoints
  </Card>

  <Card title="Authoring Guide" icon="pen" href="/en/docs/agents-and-tools/agent-skills/best-practices">
    Best practices for writing effective Skills
  </Card>

  <Card title="Code Execution Tool" icon="terminal" href="/en/docs/agents-and-tools/tool-use/code-execution-tool">
    Learn about the code execution environment
  </Card>
</CardGroup>



---

**Navigation:** [← Previous](./10-let-claude-think-chain-of-thought-prompting-to-inc.md) | [Index](./index.md) | [Next →](./12-streaming-messages.md)
