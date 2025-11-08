# Overview

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-getting-started-with-teams-and-enterprise.md)

---

# Overview
Source: https://docs.windsurf.com/autocomplete/overview



**Windsurf Autocomplete** is powered by our own models, trained in-house from scratch to optimize for speed and accuracy.

<Frame>
  <img src="https://exafunction.github.io/public/autocomplete/autocomplete-speed-fast.gif" />
</Frame>

Our autocomplete makes in-line and multi-line suggestions based on the context of your code.

Suggestions appear in grey text as you type. You can press `esc` to cancel a suggestion.
Suggestions will also disappear if you continue typing or navigating without accepting them.

## Keyboard Shortcuts

### General Shortcuts

Here are the general shortcuts that apply for macOS.
Replace `⌘` with `Ctrl` and `⌥` with `Alt` to get the corresponding shortcuts on Windows/Linux.

* **Accept suggestion**: `⇥`
* **Cancel suggestion**: `esc`
* **Accept suggestion word-by-word**: `⌘+→` (VS Code), `⌥+⇧+\` (JetBrains)
* **Next/previous suggestion**: `⌥+]`/`⌥+[`
* **Trigger suggestion**: `⌥+\`

### JetBrains Shortcuts - 2.2.2 (stable) and 2.3.5 (pre-release) and later

<Tabs>
  <Tab title="macOS">
    * **Accept suggestion**: `⇥`
    * **Accept next word**: `⌥→`
    * **Accept current line**: `⌘→`
    * **Trigger suggestion**: `⌥\`
  </Tab>

  <Tab title="Windows/Linux">
    * **Accept suggestion**: `Tab`
    * **Accept next word**: `Ctrl+Right Arrow`
    * **Accept current line**: `End`
    * **Trigger suggestion**: `Alt+\`
  </Tab>
</Tabs>

<Note>
  You can customize these keyboard shortcuts by

  * Hover over any completion text and select "Custom" from the dropdown.
  * Navigate to Settings > Keymap > Main Menu > Code > Code Completion.
</Note>

## Autocomplete Speeds

You can set the speed of the Autocomplete in your settings.

<Note>Fast Autocomplete is currently only available to our Pro, Teams, and Enterprise Users.</Note>

<Frame>
  <img src="https://exafunction.github.io/public/autocomplete/autocomplete-speeds-select.png" />
</Frame>



# Tips
Source: https://docs.windsurf.com/autocomplete/tips



## Inline Comments

You can instruct autocomplete with the use of comments in your code.
Windsurf will read these comments and suggest the code to bring the comment to life.

<Frame>
  <img src="https://exafunction.github.io/public/autocomplete/minimize_boilerplate.gif" />
</Frame>

This method can get you good mileage, but if you're finding value in writing natural-language instructions and having the AI execute them,
consider using [Windsurf Command](/command/overview).

## Fill In The Middle (FIM)

Windsurf's Autocomplete can Fill In The Middle (FIM).

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://exafunction.github.io/public/videos/inline_fim/inline_fim_codeium.mp4" />

Read more about in-line FIM on our blog [here](https://windsurf.com/blog/inline-fim-code-suggestions).

## Snooze

Click the Windsurf widget in the status bar towards the bottom right of your editor to see the option to switch Autocomplete off,
either temporarily or until you reenable it.



# Prompt Engineering
Source: https://docs.windsurf.com/best-practices/prompt-engineering



If you're reading this, you're probably someone that already understands some of the use cases and limitations of LLMs. The better prompt and context that provide to the model, the better the outcome will be.

Similarly with Windsurf, there are best practices for crafting more effective prompts to get the most out of the tool, and get the best quality code possible to help you accelerate your workflows.

<Tip>For more complex tasks that may require you to [@-Mention](/chat/overview/#mentions) specific code blocks, use [Chat](/chat/overview) instead of [Command](/command/overview). </Tip>

## Components of a high quality prompt

* ***Clear objective or outcome***
  * What are you asking the model to produce?
  * Are you asking the model for a plan? For new code? Is it a refactor?
* ***All relevant context to perform the task(s)***
  * Have you properly used @-Mentions to ensure that the proper context is included?
  * Is there any context that is customer specific that may be unclear to Windsurf?
* ***Necessary constraints***
  * Are there any specific frameworks, libraries, or languages that must be utilized?
  * Are there any space or time complexity constraints?
  * Are there any security considerations?

## Examples

***Example #1:***

* **Bad**: Write unit tests for all test cases for an Order Book object.

* **Good**: Using `@class:unit-testing-module` write unit tests for `@func:src-order-book-add` testing for exceptions thrown when above or below stop loss

***Example #2***:

* **Bad**: Refactor rawDataTransform.

* **Good**: Refactor `@func:rawDataTransform` by turning the while loop into a for loop and using the same data structure output as `@func:otherDataTransformer`

***Example #3***:

* **Bad**: Create a new Button for the Contact Form.

* **Good**: Create a new Button component for the `@class:ContactForm` using the style guide in `@repo:frontend-components` that says “Continue”



# Common Use Cases
Source: https://docs.windsurf.com/best-practices/use-cases



Windsurf serves a variety of use cases at a high level. However, we see certain use cases to be more common than others, especially among our enterprise customers within their production codebases.

## Code generation

<AccordionGroup>
  <Accordion title="Boilerplate code">
    **Guidance:** Windsurf should work well for this use case. Windsurf features including single-line suggestions, multi-line suggestions, and fill-in-the-middle (FIM) completions.

    **Best Practices:** Ensuring usage of Next Completion (`⌥ + ]`), Context Pinning, @ Mentions, and Custom Context will provide best results.
  </Accordion>

  <Accordion title="Front-end development tasks">
    **Guidance:** Windsurf should work well for this use case. Windsurf features including single-line suggestions, multi-line suggestions, and fill-in-the-middle (FIM) completions.

    **Best Practices:** Ensuring usage of Next Completion (`⌥ + ]`), Context Pinning, @ Mentions, and Custom Context will provide best results.
  </Accordion>

  <Accordion title="Back-end development tasks">
    **Guidance:** Windsurf should work well for this use case. Windsurf features including single-line suggestions, multi-line suggestions, and fill-in-the-middle (FIM) completions.

    **Best Practices:** Ensuring usage of Next Completion (`⌥ + ]`), Context Pinning, @ Mentions, and Custom Context will provide best results.
  </Accordion>
</AccordionGroup>

## Unit Test generation

<AccordionGroup>
  <Accordion title="Generate unit tests and automatically remove redundant test cases">
    **Guidance:** Basic usage of Windsurf for generating unit tests should reliably generate 60-70% of unit tests. Edge case coverage will only be as good as the user prompting the model is.

    **Best Practices:** Use @ Mentions. Prompt Engineering best practices. Examples include:

    Write unit test for `@function-name` that tests all edge cases for X and for Y (e.g. email domain).

    Use `@testing-utility-class` to write a unit test for `@function-name`.
  </Accordion>

  <Accordion title="Generate sample data for test execution">
    **Guidance:** Good for low-hanging fruit use cases. For very specific API specs or in-house libraries, Windsurf will not know the intricacies well enough to ensure the quality of generated sample data.

    **Best Practices:** Be very specific about the interface you expect. Think about the complexity of the task (and if a single-shot LLM call will be sufficient to address).
  </Accordion>
</AccordionGroup>

## Internal Code Commentary

<AccordionGroup>
  <Accordion title="Generate in-line comments and code descriptions">
    **Guidance:** Windsurf should work well for this use case. Use Windsurf Command or Windsurf Chat to generate in-line comments and code descriptions.

    **Best Practices:** Use @ Mentions and use Code Lenses as much as possible to ensure the scope of the LLM call is correct.
  </Accordion>

  <Accordion title="Suggest improvements and clarifications">
    **Guidance:** Generally the Refactor button / Windsurf Command would be the best ways to prompt for improvements. Windsurf Chat is the best place to ask for explanations or clarifications. This is a little vague but Windsurf should be good at doing both.

    Windsurf Chat is the best place to ask for explanations or clarifications.

    This is a little vague but Windsurf should be good at doing both.

    **Best Practices**: Use the dropdown prompts (aka Windsurf's Refactor button) - we have custom prompts that are better engineered to deliver the answer you'd more likely expect.
  </Accordion>

  <Accordion title="Automate function headers (C/C++/C#)">
    **Guidance**: The best way to do this would be to create the header file, open chat, @ mention the function in the cpp file, and ask it to write the header function. Then do this iteratively for each in the cpp file. This is the best way to ensure no hallucinations along the way.

    **Best Practices**: Generally avoid trying to write a whole header file with one LLM call. Breaking down the granularity of the work makes the quality of the generated code significantly higher.
  </Accordion>
</AccordionGroup>

## API Documentation and Integration

<AccordionGroup>
  <Accordion title="Create documentation as APIs created and inform proper context">
    **Guidance**: This is similar to test coverage where parts of the API spec that are common across many libraries Windsurf would be able to accurately decorate. However, things that are built special for your in-house use case Windsurf might struggle to do at the quality that you expect.

    **Best Practices**: Similar to test coverage, as much as possible, walk Windsurf's model through the best way to think about what the API is doing and it will be able to decorate better.
  </Accordion>

  <Accordion title="Search repo for APIs with natural language and generate code for integrations">
    **Guidance**: Windsurf's context length for a single LLM call is 16,000 tokens. Thus, depending on the scope of your search, Windsurf's repo-wide search capability may not be sufficient. Repo-wide, multi-step, multi-edit tasks will be supported in upcoming future Windsurf products.

    This is fundamentally a multi-step problem that single-shot LLM calls (i.e. current functionality of all AI code assistants) are not well equipped to address. Additionally, accuracy of result must be much higher than other use cases as integrations are especially fragile.

    **Best Practices**: Windsurf is not well-equipped to solve this problem today. If you'd like to test the extent of Windsurf's existing functionality, build out a step-by-step plan and prompt Windsurf individually with each step and high level of details to guide the AI.
  </Accordion>
</AccordionGroup>

## Code Refactoring

<AccordionGroup>
  <Accordion title="Code simplification and modularization">
    **Guidance**: Ensure proper scoping using Windsurf Code Lenses or @ Mentions to make sure all of the necessary context is passed to the LLM.

    Context lengths for a single LLM call are finite. Thus, depending on the scope of your refactor, this finite context length may be an issue (and for that matter, any single-shot LLM paradigm). Repo-wide, multi-step, multi-edit tasks are now supported in Windsurf's [Cascade](/windsurf/cascade).

    **Best Practices**: Try to break down the prompt as much as possible. The simpler and shorter the command for refactoring the better.
  </Accordion>

  <Accordion title="Restructuring code to improve readability / maintainability">
    **Guidance**: Ensure proper scoping using Windsurf Code Lenses or @ Mentions to make sure all of the necessary context is passed to the LLM.

    Windsurf's context length for a single LLM call is 16,000 tokens. Thus, depending on the scope of your refactor, Windsurf's context length may be an issue (and for that matter, any single-shot LLM paradigm). Repo-wide, multi-step, multi-edit tasks will be supported in upcoming future Windsurf products.

    **Best Practices**: Try to break down the prompt as much as possible. The simpler and shorter the command for refactoring the better.
  </Accordion>
</AccordionGroup>



# Models
Source: https://docs.windsurf.com/chat/models



While we provide and train our own dedicated models for Chat, we also give you the flexibility choose your favorites.

It's worth noting that the Windsurf models are tightly integrated with our reasoning stack, leading to better quality suggestions than external models for coding-specific tasks.

<Frame>
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=504caae923d9dab71ddd06ea8aff7484" data-og-width="974" width="974" data-og-height="414" height="414" data-path="assets/chat_model_selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e2b781bb4aa44d76a83a43d842062560 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1fa4e50d6fe29cb154954ce18905a1e8 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9c3d4f42cf9b859d9adc3f83b638f2a7 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e766a40ec26ef7e24904f7e7cee80f06 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d241fd6283da8301e2d7c3a6143734be 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_model_selection.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ed8da2f18d8975148a20480ecf02fea3 2500w" />
</Frame>

Model selection can be found directly under the chat.

## Base Model ⚡

**Access:** All users

Available for unlimited use to all users is a fast, high-quality Windsurf Chat model based on Meta's [Llama 3.1 70B](https://ai.meta.com/blog/meta-llama-3-1/).

This model is optimized for speed, and is the **fastest** model available in Windsurf Chat. This is all while still being extremely accurate.

## Windsurf Premier 🚀

**Access:** Any paying users (Pro, Teams, Enterprise, etc.)

Available in our paid tier is unlimited usage of our premier Windsurf Chat model based on Meta's [Llama 3.1 405B](https://ai.meta.com/blog/meta-llama-3-1/).

This is the **highest-performing model** available for use in Windsurf, due to its size and integration with Windsurf's reasoning engine and native workflows.

## Other Models (GPT-4o, Claude 3.5 Sonnet)

**Access:** Any paying users (Pro, Teams, Enterprise, etc.)

Windsurf provides access to OpenAI's and Anthropic's flagship models.



# Overview
Source: https://docs.windsurf.com/chat/overview

Converse with a codebase-aware AI

<Note>
  Chat and its related features are only supported in: VS Code, JetBrains IDEs, Eclipse, X-Code, and Visual Studio.
</Note>

**Windsurf Chat** enables you to talk to your codebase from within your editor.
Chat is powered by our [context awareness](/context-awareness/overview.mdx) engine.
It combines built-in context retrieval with optional user guidance to provide accurate and grounded answers.

<Tabs>
  <Tab title="VS Code">
    In VS Code, Windsurf Chat can be found by default on the left sidebar.
    If you wish to move it elsewhere, you can click and drag the Windsurf icon and relocate it as desired.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7834d605c66fe4413718ad0d6e54ba29" data-og-width="1037" width="1037" data-og-height="702" height="702" data-path="assets/chat_vscode_where_to_find.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7a5d521234f9566acdcffd7b44639054 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6ac39537389f4c36e0e0bcf0c998cc88 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3d1fb062d8f5a0e5ecaedc2ed078a7fb 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7ca31423b43f8a27ea85b94f0c5ac83e 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f9c8f91b37219aa81348ced8e5cdb76f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_vscode_where_to_find.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=771b59b1da45de39e55fc8f579b40e9c 2500w" />
    </Frame>

    You can use `⌘+⇧+A` on Mac or `Ctrl+⇧+A` on Windows/Linux to open the chat panel and toggle focus between it and the editor.
    You can also pop the chat window out of the IDE entirely by clicking the page icon at the top of the chat panel.
  </Tab>

  <Tab title="JetBrains">
    In JetBrains IDEs, Windsurf Chat can be found by default on the right sidebar.
    If you wish to move it elsewhere, you can click and drag the Windsurf icon and relocate it as desired.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d2679679c30f27acf855984e168e9707" data-og-width="989" width="989" data-og-height="771" height="771" data-path="assets/chat_jetbrains_where_to_find.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=936a0dbdc0e9da439451a63238565681 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1e4bf489fb2a6f66b3bb63cea143c61e 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3649e5197cd42796a64ea9eec82dcad4 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=dca7d5401898aef03321bb29680d1d50 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b510f4cb1b276b4e60c2c2932ae92457 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_jetbrains_where_to_find.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4d352422c10737108cd2bfcdbe051153 2500w" />
    </Frame>

    You can use `⌘+⇧+L` on Mac or `Ctrl+⇧+L` on Windows/Linux to open the chat panel while you are typing in the editor.
    You can also open the chat in a popped-out browser window by clicking `Tools > Windsurf > Open Windsurf Chat in Browser` in the top menu bar.
  </Tab>
</Tabs>

## @-Mentions

<Tip>An @-mention is a deterministic way of bringing in context, and is guaranteed to be part of the context used to respond to a chat.</Tip>

In any given chat message you send, you can explicitly refer to context items from within the chat input by prefixing a word with `@`.

Context items available to be @-mentioned:

* Functions & classes
  * Only functions and classes in the local indexed
  * Also only available for languages we have built AST parsers for (Python, TypeScript, JavaScript, Go, Java, C, C++, PHP, Ruby, C#, Perl, Kotlin, Dart, Bash, COBOL, and more)
* Directories and files in your codebase
* Remote repositories
* The contents of your in-IDE terminal (VS Code only).

<Frame>
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=941c76f7691cd053706a4bc281112cc5" data-og-width="1456" width="1456" data-og-height="814" height="814" data-path="assets/at_mentions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b17499e00a66c3b95cf3b8df263d5ca3 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1298aa3619877ab24155a201a5ad5d6b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5417614970f16b9add22b087b1ab80b1 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=441ca49ce613783ab5d358e8a7c2e2db 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e1438fc87ade47cb3dbcbf6a620c0901 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/at_mentions.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7fdd33c52d96e9cccbb8772a0630c30f 2500w" />
</Frame>

You can also try `@diff`, which lets you chat about your repository's current `git diff` state.
The `@diff` feature is currently in beta.

<Tip>If you want to pull a section of code into the chat and you don't have @-Mentions available, you can: 1. highlight the code -> 2. right click -> 3. select 'Windsurf: Explain Selected Code Block'</Tip>

## Persistent Context

You can instruct the chat model to use certain context throughout a conversation and across different conversations
by clicking on the `Advanced` tab in the chat panel.

<Frame caption="Chat shows you the context it is considering.">
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=414beb483cf5725f5999ae090b01c986" data-og-width="1314" width="1314" data-og-height="624" height="624" data-path="assets/chat_context.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=121339f0f4c77b54027afa9f94fe3134 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d654f90f78945825c6b75e805190184a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=daf01b0d5d17b9ff09d0a2da033f93db 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9badbb464a1dd8f48dbf02e80740ae27 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=84e13b33be53ce5950d9d89e234eec0a 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_context.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=998839dcc4a2e446bc52108d2f0c4655 2500w" />
</Frame>

In this tab, you can see:

* **Custom Chat Instructions**: a short prompt guideline like "Respond in Kotlin and assume I have little familiarity with it" to orient the model towards a certain type of response.
* **Pinned Contexts**: items from your codebase like files, directories, and code snippets that you would like explicitly for the model to take into account.
  See also [Context Pinning](/context-awareness/overview#context-pinning).
* **Active Document**: a marker for your currently active file, which receives special focus.
* **Local Indexes**: a list of local repositories that the Windsurf context engine has indexed.

## Slash Commands

You can prefix a message with `/explain` to ask the model to explain something of your choice.
Currently, `/explain` is the only supported slash command.
[Let us know](https://codeium.canny.io/feature-requests/) if there are other common workflows you want wrapped in a slash command.

## Copy and Insert

Sometimes, Chat responses will contain code blocks. You can copy a code block to your clipboard or insert it directly into the editor
at your cursor position by clicking the appropriate button atop the code block.

<Note>
  If you would like the AI to enact a change directly in your editor based on an instruction,
  consider using [Windsurf Command](/command/overview).
</Note>

## Inline Citations

Chat is aware of code context items, and its responses often contain linked references to snippets of code in your files.

<Frame>
  <video autoPlay muted loop playsInline src="https://exafunction.github.io/public/videos/chat/inline-citations.mp4" />
</Frame>

## Regenerate with Context

By default, Windsurf makes a judgment call whether any given question is general or if it requires codebase context.

You can force the model to use codebase context by submitting your question with `⌘⏎`.
For a question that has already received a response, you rerun with context by clicking the sparkle icon.

<Frame>
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6da54122318e3b654ba4613abe6a68a1" data-og-width="440" width="440" data-og-height="206" height="206" data-path="assets/chat_regenerate_with_context.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2ca70708a90c6e97b389b08eeb60b26c 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=326e458558a6a57be9b521dc07963b54 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ebd00e0f95d8d560400bbb2656fb19f0 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8161fac3aa906991d1510eda1e75082c 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=174d713ca67d151027d309575771f342 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_regenerate_with_context.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3f8d542e05683a12054aa6a7e34d0922 2500w" />
</Frame>

## Stats for Nerds

Lots of things happen under the hood for every chat message. You can click the stats icon to see these statistics for yourself.

<Frame>
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=048a60359f0330d1281175296804fbcb" data-og-width="1634" width="1634" data-og-height="1180" height="1180" data-path="assets/chat_stats_for_nerds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d2196e0d69106a2968b1ad74d4a58b24 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=39ecd5c9e5a8c4e5f2022e620c4e96c7 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=859c020aae04741595aca4b14c16dd2b 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0abab7be0839b348c23b73bd27961bc0 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=96264b627b032f8ac6bbdafa748bb810 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_stats_for_nerds.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5518d27d397fce3c2c4b5d3ebe3a54a7 2500w" />
</Frame>

## Chat History

To revisit past conversations, click the history icon at the top of the chat panel.
You can click the `+` to create a new conversation, and
you can click the `⋮` button to export your conversation. This applies only for the Windsurf Plugins.

<Frame>
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2c18d444db63df1329fa744079e7a05d" data-og-width="828" width="828" data-og-height="210" height="210" data-path="assets/chat_history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5ba6db18a93a757a3543879cf087d2c2 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ff9fa87e8e4fdeb8ac8bfca0caff3b7d 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=89476debc7aecaf71a3689546f78291d 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f8208fecceea890b07205e4f41e5c9de 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cf57079f15d6cb6bc45ade9ff3ecd04f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_history.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a5c87ee97b6eb69739b3f1a03f0b935d 2500w" />
</Frame>

## Settings

Click on the gear icon to reach the `Settings` tab. Here, you can view settings that are applicable to your account. For example, you can update your theme preferences (light or dark), change autocomplete speed, view current plan, and change font size.
The settings panel also gives you an option to download diagnostics, which are debug logs that can be helpful for the Windsurf team to debug an issue, should you encounter one.

<Frame caption="On Windsurf Chat, click on the gear icon on the top right corner">
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d32c713a4055cf8f5c9cb0472671a5f0" data-og-width="1488" width="1488" data-og-height="1536" height="1536" data-path="assets/chat_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0e57e72ba502af91b5cc131a3b1d4477 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=100a22920312851b534aad48f94390f7 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6d3ce9a08bcbe10aafc3ab3c36c4e113 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=01081c274077a9c7bea2c18fdd2b25e5 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5d5999526b4b4daba82b61361ade1776 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/chat_settings.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cb0c379dacfca12e912a1a4901e0c587 2500w" />
</Frame>

## Telemetry

<Note>You may encounter issues with Chat if Telemetry is not enabled.</Note>

<Tabs>
  <Tab title="VS Code">
    To enable telemetry, open your VS Code settings and navigate to User > Application > Telemetry. In the following dropdown, select "all".

    <img width="350" src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=0d4cd0b8d2c1dfaf0fa5c3a87e9e639f" data-og-width="634" data-og-height="348" data-path="assets/vscode_telemetry_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=0ed5126c8fb51e98df309a6fc64ea276 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=2216ff691d5675b9c3875598d9e3af9e 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=69cc7901cfb5772f2a923e965a4af186 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=586d828c16de1d34eadef84cd957c3f4 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=237d861b04375c9e4ce5ca223f105d56 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/vscode_telemetry_settings.png?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=2e4453f2733662eacdb1605243d83c36 2500w" />
  </Tab>

  <Tab title="JetBrains">
    To enable telemetry in JetBrains IDEs, open your Settings and navigate to Appearance & Hehavior > System Settings > Data Sharing.

    <img width="350" src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=ded930e34656b692d02371b36b9d612b" data-og-width="922" data-og-height="436" data-path="assets/jetbrains_telemetry_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?w=280&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=bdc98fc2189716134e1cc2d50b2f30e5 280w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?w=560&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=c885517091a3049f3dbdcc779a80867d 560w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?w=840&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=0ad7ed77b6ff507743a3288a381ac092 840w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?w=1100&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=b8b728bba6045aed81b3a95fbae48ba0 1100w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?w=1650&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=3fc49a151dfd9d9ae951f8621caf3bb0 1650w, https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_telemetry_settings.png?w=2500&fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=77eb834b6a8abfea4d3d1dfc62de8937 2500w" />
  </Tab>
</Tabs>



# Overview
Source: https://docs.windsurf.com/command/plugins-overview

AI-powered in-line edits

**Windsurf Command** generates new or edits existing code via natural language inputs, directly in the editor window.

<Tabs>
  <Tab title="VS Code">
    To invoke Command, press `⌘+I` on Mac or `Ctrl+I` on Windows/Linux.
    From there, you can enter a prompt in natural language and hit the Submit button (or `⌘+⏎`/`Ctrl+⏎`) to forward the instruction to the AI.
    Windsurf will then provide a multiline suggestion that you can accept or reject.

    If you highlight a section of code before invoking Command, then the AI will edit the selection spanned by the highlighted lines.
    Otherwise, it will generate code at your cursor's location.

    <Frame>
      <video autoPlay muted loop playsInline src="https://exafunction.github.io/public/videos/codeium_command_vscode.mp4" />
    </Frame>

    You can accept, reject, or follow-up a generation by clicking the corresponding code lens above the generated diff,
    or by using the appropriate shortcuts (`⌥+A`/`Alt+A`, `⌥+R`/`Alt+R`, and `⌥+F`/`Alt+F`, respectively).
  </Tab>

  <Tab title="JetBrains">
    To invoke Command, press `⌘+I` on Mac or `Ctrl+I` on Windows/Linux.

    <Note>
      Some users have reported keyboard conflicts with this shortcut, so `⌘+⇧+I` and `⌘+\`on Mac (`Ctrl+⇧+I` and `Ctrl+\` on Windows/Linux)
      will also work.
    </Note>

    The Command invocation will open an interactive popup at the appropriate location in the code.
    You can enter a prompt in natural language and Windsurf will provide a multiline suggestion that you can accept or reject.
    If you highlight a section of code before invoking Command, then the AI will edit the selection spanned by the highlighted lines.
    Otherwise, it will generate code at your cursor's location.

    <Frame>
      <video autoPlay muted loop playsInline src="https://exafunction.github.io/public/videos/codeium_command_jetbrains.mp4" />
    </Frame>

    The Command popup will persist in the editor if you scroll around or focus your cursor elsewhere in the editor.
    It will act on your most recently highlighted selection of code or your most recent cursor position.
    While it is active, the Command popup gives you the following options:

    * **Cancel** (`Esc`): this will close the popup and undo any code changes that may have occured while the popup was open.
    * **Accept generation** (`⌘+⏎`): this option appears after submitting an instruction and receiving a generation.
      It will write the suggestion into the code editor and close the popup.
    * **Undo generation** (`⌘+⌫`): this option appears after submitting an instruction and receiving a generation.
      It will restore the code to its pre-Command state without closing the popup, while reinserting your most recent instruction
      into the input box.
    * **Follow-up**: this option appears after submitting an instruction and receiving a generation.
      You can enter a second (and third, fourth, etc.) instruction and submit it,
      which will undo the currently shown generation and rerun Command using your comma-concatenated instruction history.
  </Tab>
</Tabs>


# Best Practices

Windsurf Command is great for file-scoped, in-line changes that you can describe as an instruction in natural language.
Here are some pointers to keep in mind:

* The model that powers Command is larger than the one powering autocomplete.
  It is slower but more capable, and it is trained to be especially good at instruction-following.

* If you highlight a block of code before invoking Command, it will edit the selection. Otherwise, it will do a pure generation.

* Using Command effectively can be an art. Simple prompts like "Fix this" or "Refactor" will likely work
  thanks to Windsurf's context awareness.
  A specific prompt like "Write a function that takes two inputs of type `Diffable` and implements the Myers diff algorithm"
  that contains a clear objective and references to relevant context may help the model even more.



# Refactors, Docstrings, and More
Source: https://docs.windsurf.com/command/related-features

Features powered by Command

Command enables streamlined experiences for a few common operations.

## Function Refactors and Docstring Generation

Above functions and classes, Windsurf renders *code lenses*,
which are small, clickable text labels that invoke Windsurf's AI capabilities on the labeled item.

<Tip>You can disable code lenses by clicking the `✕` to the right of the code lens text.</Tip>

The `Refactor` and `Docstring` code lenses in particular will invoke Command.

* If you click `Refactor`, Windsurf will prompt you with a dropdown of selectable, pre-populated
  instructions that you can choose from. You can also write your own. This is equivalent to highlighting the function and invoking Command.
* If you click `Docstring`, Windsurf will generate a docstring for you above the function header.
  (In Python, the docstring will be correctly generated *underneath* the function header.)

<Frame caption="Encouraging readable and maintainable code, one docstring at a time.">
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/d8O4q6w3H2CjrirL/assets/jetbrains_docstrings.mp4?fit=max&auto=format&n=d8O4q6w3H2CjrirL&q=85&s=508c5797d57e88cf7b7db1c07a1e45c7" data-path="assets/jetbrains_docstrings.mp4" />
</Frame>

## Smart Paste

This feature allows you to copy code and paste it into a file in your IDE written in a different programming language.
Use `⌘+⌥+V` (Mac) or `Ctrl+Alt+V` (Windows/Linux) to invoke Smart Paste.
Behind the scenes, Windsurf will detect the language of the destination file and use Command to translate the code in your clipboard.
Windsurf's context awareness will try to write it to fit in your code, for example by referencing proper variable names.

<Frame>
  <video autoPlay muted loop playsInline src="https://exafunction.github.io/public/videos/demos/Smart_Paste_Demo_1080p.mp4" />
</Frame>

Some possible use cases:

* **Migrating code**: you're rewriting JavaScript into TypeScript, or Java into Kotlin.
* **Pasting from Stack Overflow**: you found a utility function online written in Go, but you're using Rust.
* **Learning a new language**: you're curious about Haskell and want to see what your would look like if written in it.



# Command
Source: https://docs.windsurf.com/command/windsurf-overview

Cmd/Ctrl + I for in-line code generations and edits

**Command** generates new or edits existing code via natural language inputs, directly in the editor window.

<Tip>Command does NOT consume any premium model credits.</Tip>

To invoke Command, press `⌘+I` on Mac or `Ctrl+I` on Windows/Linux.

You can enter a prompt in natural language and hit the Submit button (or `⌘+⏎`/`Ctrl+⏎`) to forward the instruction to the AI.

If you highlight a section of code before invoking Command, then the AI will edit the selection spanned by the highlighted lines.
Otherwise, it will generate code at your cursor's location.

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=355f106c06d14c5150b8fd6ade2544d8" data-og-width="1786" width="1786" data-og-height="1018" height="1018" data-path="assets/windsurf-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=927da1f69fbaabe5ba9a17e0f88cfefd 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=b4785a636080ad292d742119776f9538 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=63f27f54aae36f7c7c48b59ff86a1dc8 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=7c67b7a3910176da619cf57b45f2577f 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=8d30a6e68e175618f8b9dcd079cfcfd8 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command.png?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=c0964663193b983f1b612706b362cd2a 2500w" />
</Frame>

You can accept, reject, or follow-up a generation by clicking the corresponding code lens above the generated diff,or by using the appropriate shortcuts (`Cmd/Ctrl+Enter`/`Cmd/Ctrl+Delete`)


# Models

Command comes with its own set of models that are optimized for current-file edits.

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/windsurf-command-models.mp4?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=56ff76bccc777e7bb30af7d4a4991325" data-path="assets/windsurf-command-models.mp4" />
</Frame>

<Tip> Windsurf Fast is the fastest, most accurate model available.</Tip>


# Terminal Command

You can use Command in the terminal (`Cmd/Ctrl+I`) to generate the proper CLI syntax using prompts in natural language.

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=b03f1498ac0b7dc344270f975f9a234f" data-og-width="980" width="980" data-og-height="164" height="164" data-path="assets/windsurf-terminal-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=280&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ec94b782cbe3b3d0a3e8d44ce7b27c74 280w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=560&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=9e3839c701ba2308cbc754842c8472a4 560w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=840&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=25245a6097e94c63ed47cb382097f82b 840w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=1100&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=ecfdf898fe06e81255add438d3daff49 1100w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=1650&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=c46a449c560b98a2e295e904601a3c51 1650w, https://mintcdn.com/codeium/qJj_RRojefb93yIg/assets/windsurf-terminal-command.png?w=2500&fit=max&auto=format&n=qJj_RRojefb93yIg&q=85&s=44ec229230a00b642a4aa61f1d4c571c 2500w" />
</Frame>


# Best Practices

Command is great for file-scoped, in-line changes that you can describe as an instruction in natural language.
Here are some pointers to keep in mind:

* The model that powers Command is larger than the one powering autocomplete.
  It is slower but more capable, and it is trained to be especially good at instruction-following.

* If you highlight a block of code before invoking Command, it will edit the selection. Otherwise, it will do a pure generation.

* Using Command effectively can be an art. Simple prompts like "Fix this" or "Refactor" will likely work
  thanks to Windsurf's context awareness.
  A specific prompt like "Write a function that takes two inputs of type `Diffable` and implements the Myers diff algorithm"
  that contains a clear objective and references to relevant context may help the model even more.



# Code Lenses
Source: https://docs.windsurf.com/command/windsurf-related-features

Shortcuts for common operations

## Explain, Refactor, and Add Docstring

At the top of the text editor, Windsurf gives exposes *code lenses* on functions and classes.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=741eb72a40e5ae8eca97e8e2a493bd28" data-og-width="884" width="884" data-og-height="216" height="216" data-path="assets/windsurf/windsurf-code-lenses.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a5e987745a245a5f5590007017e2e4e0 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=7af9cdcc98aa12db8887762d00b73089 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=40525c3d300b9414df551b4d18be9bf7 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=fa91fe10929dbe193f549e4cd1165731 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=afd8a62eda36eb99b758e5503238be8c 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-code-lenses.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=3f7775b532340787a9a17dcdf8c0e590 2500w" />
</Frame>

The `Explain` code lens will invoke Cascade, which will simply explain what the function or class does and how it works.

The `Refactor` and `Docstring` code lenses in particular will invoke Command.

* If you click `Refactor`, Windsurf will prompt you with a dropdown of selectable, pre-populated
  instructions that you can choose from. You can also write your own. This is equivalent to highlighting the function and invoking Command.
* If you click `Docstring`, Windsurf will generate a docstring for you above the function header.
  (In Python, the docstring will be correctly generated *underneath* the function header.)

<Frame>
  <video autoPlay muted loop playsInline src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/windsurf-refactor-code-lens.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=484ec31a18bc46297583ca82ebb4a5fd" data-path="assets/windsurf/windsurf-refactor-code-lens.mp4" />
</Frame>



# Fast Context
Source: https://docs.windsurf.com/context-awareness/fast-context



Fast Context is a specialized subagent in Windsurf that retrieves relevant code from your codebase up to 20x faster than traditional agentic search. It powers Cascade's ability to quickly understand large codebases while maintaining the intelligence of frontier models.

<video autoPlay controls muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/4npKb0dOJvGVxGDm/assets/windsurf/cascade/fastcontext.mp4?fit=max&auto=format&n=4npKb0dOJvGVxGDm&q=85&s=7fa30dffb4eb96df65f8a302fc4cff50" data-path="assets/windsurf/cascade/fastcontext.mp4" />

## Using Fast Context

When Cascade receives a query that requires code search, Fast Context will trigger automatically. You can also force it to activate by using `Cmd+Enter` (Mac) or `Ctrl+Enter` (Windows/Linux) when submitting your query.

You'll notice Fast Context is working when:

* Cascade quickly identifies relevant files across your codebase
* Large codebase queries complete faster than before
* Cascade spends less time reading irrelevant code

## How It Works

Fast Context uses `SWE-grep` and `SWE-grep-mini`, custom models trained specifically for rapid code retrieval. These models combine the speed of traditional embedding search with the intelligence of agentic exploration.

When you make a query to Cascade that requires searching through your codebase, Fast Context automatically activates to:

1. Identify relevant files and code sections using parallel tool calls
2. Execute multiple searches simultaneously
3. Return targeted results in seconds rather than minutes

This approach prevents context pollution and aims to mitigate the traditional speed-accuracy tradeoff. By delegating retrieval to a specialized subagent, Cascade conserves its context budget and intelligence for the actual task at hand.

## SWE-grep Models

Fast Context is powered by the SWE-grep model family:

* **SWE-grep**: High-intelligence variant optimized for complex retrieval tasks
* **SWE-grep-mini**: Ultra-fast variant serving at over 2,800 tokens per second

Both models are trained using reinforcement learning to excel at parallel tool calling and efficient codebase navigation. They execute up to 8 parallel tool calls per turn over a maximum of 4 turns, allowing them to explore different parts of your codebase simultaneously.

The models use a restricted set of cross-platform compatible tools (grep, read, glob) to ensure consistent performance across different operating systems and development environments.



# Overview
Source: https://docs.windsurf.com/context-awareness/overview

On codebase context and related features

Windsurf's context engine builds a deep understanding of your codebase, past actions, and next intent.

Historically, code-generation approaches focused on fine-tuning large language models (LLMs) on a codebase,
which is difficult to scale to the needs of every individual user.
A more recent and popular approach leverages retrieval-augmented generation (RAG),
which focuses on techniques to construct highly relevant, context-rich prompts
to elicit accurate answers from an LLM.

We've implemented an optimized RAG approach to codebase context,
which produces higher quality suggestions and fewer hallucinations.

<Note>
  Windsurf offers full fine-tuning for enterprises, and the best solution
  combines fine-tuning with RAG.
</Note>

## Default Context

Out of the box, Windsurf takes multiple relevant sources of context into consideration.

* The current file and other open files in your IDE, which are often very relevant to the code you are currently writing.
* The entire local codebase is then indexed (including files that are not open),
  and relevant code snippets are sourced by Windsurf's retrieval engine as you write code, ask questions, or invoke commands.
* For Pro users, we offer expanded context lengths increased indexing limits, and higher limits on custom context and pinned context items.
* For Teams and Enterprise users, Windsurf can also index remote repositories.
  This is useful for companies whose development organization works across multiple repositories.

## Knowledge Base (Beta)

<Note>Only available for Teams and Enterprise customers. Currently not available to Hybrid customers.</Note>

This feature allows teams to pull in Google Docs as shared context or knowledge sources for their entire team.

Currently, only Google Docs are supported. Images are not imported, but charts, tables, and formatted text are fully supported.

<Card title="Knowledge Base" icon="people-group" href="https://windsurf.com/team/settings">
  Configure knowledge base settings for your team. This page will only be visible with admin privileges.
</Card>

Admins must manually connect with Google Drive via OAuth, after which they can add up to 50 Google Docs as team knowledge sources.

Cascade will have access to the docs specified in the Windsurf dashboard. These docs do not obey individual user access controls, meaning if an admin makes a doc available to the team, all users will have access to it regardless of access controls on the Google Drive side.

### Best Practices

Context Pinning is great when your task in your current file depends on information from other files.
Try to pin only what you need. Pinning too much may slow down or negatively impact model performance.

Here are some ideas for effective context pinning:

* Module Definitions: pinning class/struct definition files that are inside your repo but in a module separate from your currently active file.
* Internal Frameworks/Libraries: pinning directories with code examples for using frameworks/libraries.
* Specific Tasks: pinning a file or folder defining a particular interface (e.g., `.proto` files, abstract class files, config templates).
* Current Focus Area: pinning the "lowest common denominator" directory containing the majority of files needed for your current coding session.
* Testing: pinning a particular file with the class you are writing unit tests for.

## Chat-Specific Context Features

When conversing with Windsurf Chat, you have various ways of leveraging codebase context,
like [@-mentions](/chat/overview/#mentions) or custom guidelines.
See the [Chat page](/chat/overview) for more information.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://exafunction.github.io/public/videos/chat/inline-mention.mp4" />

## Frequently Asked Questions (FAQs)

### Does Windsurf index my codebase?

Yes, Windsurf does index your codebase. It also uses LLMs to perform retrieval-augmented generation (RAG) on your codebase using our own [M-Query](https://youtu.be/DuZXbinJ4Uc?feature=shared\&t=606) techniques.

Indexing performance and features vary based on your workflow and your Windsurf plan. For more information, please visit our [context awareness page](https://windsurf.com/context).



# Remote Indexing
Source: https://docs.windsurf.com/context-awareness/remote-indexing



<Note> This feature is only available in the Windsurf Plugins for Enterprise plans. </Note>

While Local Indexing works great, the user may want to index codebases that they do not have stored locally for our models to take in as context.

For this use case, organizations on Teams and Enterprise plans can use Windsurf's Indexing Service to globally import all the relevant repositories. The indexing and embedding is then performed by Windsurf's servers (on an isolated tenant), and once the index is created, it is available to be queried by any member of the Team.

## Adding a repository

From [https://windsurf.com/indexing](https://windsurf.com/indexing) you can add a repository to index. Currently we support Git repositories from GitHub, GitLab, and BitBucket.

<Frame>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=2e60f03d5cddbefc397174c35277273c" data-og-width="2016" width="2016" data-og-height="1488" height="1488" data-path="assets/remote-indexing-adding-repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=706990eab03d43fcfe45bbaf17c94d14 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=50bc0700ffde8ad79dacc1c3e48307c5 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=d5e1171d6491c0488d5e856b973b9105 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=01231efd308a7ead3b878cd9c003b1ab 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=aa6e287b5569982ca33152b253dc6430 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/remote-indexing-adding-repo.png?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=4844fcf2cc46856e33bce62e451b9b26 2500w" />
</Frame>

You can choose to index a particular branch and to automatically re-index the repository after some number of days.

## Security Guarantees

We clone the repository in order to create the index, but once we finish creating embeddings for the codebase we delete all the code and code snippets **assuming that the Store Snippets setting is unchecked.** We don't persist anything other than the embeddings themselves, from which you cannot derive the original code.

Furthermore, all indexing and embedding is performed on a single-tenant instance—nothing about the indexing process is shared between multiple Windsurf Teams customers.



# Windsurf Ignore
Source: https://docs.windsurf.com/context-awareness/windsurf-ignore



## WindsurfIgnore

By default, Windsurf Indexing will ignore:

* Paths specified in `gitignore`
* Files in `node_modules`
* Hidden pathnames (starting with ".")

When a file is ignored, it will not be indexed, and also does not count against the Indexing Max Workspace Size file counts.
Files included in .gtiignore cannot be edited by Cascade.

If you want to further configure files that Windsurf Indexing ignores, you can add a `.codeiumignore` file to your repo root, with the same syntax as `.gitignore`

<Frame>
  <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9b6143bd6f701e4f25cf93825ee6fde6" data-og-width="732" width="732" data-og-height="450" height="450" data-path="assets/codeiumignore.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3a85edaa177c7a7dbcc9da5008c4f10c 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=bdb51589e57ab2f816527319cfae67c1 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=bcca84dfb2a790c903dc623101a584d6 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6e9ca44d9d2a0b499caa90b2feedc74a 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f428e6545758fbd7ff766a673f004ca9 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/codeiumignore.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=27c03d11be18e5f83fe22b3491fe7cef 2500w" />
</Frame>

### Global .codeiumignore

For enterprise customers managing multiple repositories, you can enforce ignore rules across all repositories by placing a global `.codeiumignore` file in the `~/.codeium/` folder. This global configuration will apply to all Windsurf workspaces on your system.

The global `.codeiumignore` file uses the same syntax as `.gitignore` and works in addition to any repository-specific `.codeiumignore` files.

## System Requirements

When first enabled, Windsurf will consume a fraction of CPU while it indexes the workspace. Depending on your workspace size, this should take 5-10 minutes, and only needs to happen once per workspace. CPU usage will return to normal automatically. Windsurf Indexing also requires RAM (\~300MB for a 5000-file workspace).

The "Max Workspace Size (File Count)" setting determines the largest workspace for which Windsurf Indexing will try to index a particular workspace / module. If your workspace does not appear to be indexed, please try adjusting this number higher. For users with \~10GB of RAM, we recommend setting this no higher than 10,000 files.



# Overview
Source: https://docs.windsurf.com/context-awareness/windsurf-overview

On codebase context and related features

Windsurf's context engine builds a deep understanding of your codebase, past actions, and next intent.

Historically, code-generation approaches focused on fine-tuning large language models (LLMs) on a codebase,
which is difficult to scale to the needs of every individual user.
A more recent and popular approach leverages retrieval-augmented generation (RAG),
which focuses on techniques to construct highly relevant, context-rich prompts
to elicit accurate answers from an LLM.

We've implemented an optimized RAG approach to codebase context,
which produces higher quality suggestions and fewer hallucinations.

<Note>
  Windsurf offers full fine-tuning for enterprises, and the best solution
  combines fine-tuning with RAG.
</Note>

## Default Context

Out of the box, Windsurf takes multiple relevant sources of context into consideration.

* The current file and other open files in your IDE, which are often very relevant to the code you are currently writing.
* The entire local codebase is then indexed (including files that are not open),
  and relevant code snippets are sourced by Windsurf's retrieval engine as you write code, ask questions, or invoke commands.
* For Pro users, we offer expanded context lengths increased indexing limits, and higher limits on custom context and pinned context items.
* For Teams and Enterprise users, Windsurf can also index remote repositories.
  This is useful for companies whose development organization works across multiple repositories.

## Chat-Specific Context Features

When conversing with Windsurf Chat, you have various ways of leveraging codebase context,
like [@-mentions](/chat/overview/#mentions) or custom guidelines.
See the [Chat page](/chat/overview) for more information.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://exafunction.github.io/public/videos/chat/inline-mention.mp4" />

## Frequently Asked Questions (FAQs)

### Does Windsurf index my codebase?

Yes, Windsurf does index your codebase. It also uses LLMs to perform retrieval-augmented generation (RAG) on your codebase using our own [M-Query](https://youtu.be/DuZXbinJ4Uc?feature=shared\&t=606) techniques.

Indexing performance and features vary based on your workflow and your Windsurf plan. For more information, please visit our [context awareness page](https://windsurf.com/context).



# Analytics
Source: https://docs.windsurf.com/plugins/accounts/analytics



## Individuals

<Card title="User Analytics" horizontal={true} icon="user" href="https://windsurf.com/profile">
  User analytics are available for viewing and sharing on your own [profile](https://windsurf.com/profile) page.
</Card>

See your completion stats, [refer](https://windsurf.com/referral) your friends, look into your language breakdown, and unlock achievement badges by using Windsurf in your daily workflow.

## Teams

<Card title="Team Analytics" horizontal={true} icon="users" href="https://windsurf.com/team/analytics">
  Windsurf makes managing your team easy from one dashboard.
</Card>

<Note>
  You will need team admin privileges in order to view the following team links.
</Note>

Team leads and managers can also see an aggregate of their team members' usage patterns and analytics, including Percent of Code Written (PCW) by AI, total lines of code written, total tool calls, credit consumption, and more.

<Frame>
  <img src="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=55fc677bc12bf29fade2bd8152eb4712" data-og-width="1313" width="1313" data-og-height="985" height="985" data-path="assets/teams/team-analytics-pcw.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?w=280&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=b5e996e20bbde88e14ff033a56e89c69 280w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?w=560&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=42db5449e81d53614c0ac600f5625d6b 560w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?w=840&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=703e903949018491e3db70d5da873233 840w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?w=1100&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=abc9b188e2fdd9e2f5a395f594d1ba0d 1100w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?w=1650&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=f9544605eb542dc0c5ecf29836196670 1650w, https://mintcdn.com/codeium/vRt4FQOyBeZpD2Pu/assets/teams/team-analytics-pcw.jpg?w=2500&fit=max&auto=format&n=vRt4FQOyBeZpD2Pu&q=85&s=6f5b57d0857d14a96b33cdb131a72431 2500w" />
</Frame>



# Analytics API
Source: https://docs.windsurf.com/plugins/accounts/api-reference/analytics-api-introduction

Enterprise analytics API for querying Windsurf usage data

## Overview

The Windsurf Analytics API enables enterprise customers to programmatically access detailed usage analytics for their teams. Query data from autocomplete, chat, command features, and Cascade with flexible filtering, grouping, and aggregation options.

<Info>API data is refreshed every 3 hours</Info>

## Common Parameters

Most Analytics API endpoints support these common parameters:

| Parameter         | Type   | Required | Description                                                  |
| ----------------- | ------ | -------- | ------------------------------------------------------------ |
| `service_key`     | string | Yes      | Your service key for authentication                          |
| `group_name`      | string | No       | Filter results to a specific group                           |
| `start_timestamp` | string | Varies   | Start time in RFC 3339 format (e.g., `2023-01-01T00:00:00Z`) |
| `end_timestamp`   | string | Varies   | End time in RFC 3339 format (e.g., `2023-12-31T23:59:59Z`)   |

## Available Endpoints

The Analytics API provides three main endpoints:

1. **[User Page Analytics](/plugins/accounts/api-reference/user-page-analytics)** - Get user activity data from the teams page
2. **[Cascade Analytics](/plugins/accounts/api-reference/cascade-analytics)** - Query Cascade-specific usage metrics
3. **[Custom Analytics](/plugins/accounts/api-reference/custom-analytics)** - Flexible querying with custom selections, filters, and aggregations



# API Reference
Source: https://docs.windsurf.com/plugins/accounts/api-reference/api-introduction

Enterprise API for querying Windsurf usage data and managing configurations

## Overview

The Windsurf API enables enterprise customers to programmatically access detailed usage analytics and manage usage configurations for their teams.

<Note>The API is available for Enterprise plans only</Note>

## Base URL

All API requests should be made to:

```
https://server.codeium.com/api/v1/
```

## Authentication

The Windsurf API uses service keys for authentication. Service keys must be included in the request body of all API calls.

### Creating a Service Key

1. Navigate to your [team settings page](https://windsurf.com/team/settings)
2. Go to the "Service Keys" section
3. Create a new service key with appropriate permissions
4. Copy the generated service key for use in API requests

### Required Permissions

All Analytics API endpoints require "Teams Read-only" permissions.

All Usage API endpoints require "Billing Write" permissions.

### Using Service Keys

Include your service key in the request body of all API calls:

```json  theme={null}
{
  "service_key": "your_service_key_here",
  // ... other parameters
}
```

<Warning>Keep your service keys secure and never expose them in client-side code or public repositories</Warning>

## Rate Limits

API requests are subject to rate limiting to ensure service stability. If you exceed the rate limit, you'll receive a `429 Too Many Requests` response.

## Support

For API support and questions, please contact [Windsurf Support](https://windsurf.com/support).



# Get Cascade Analytics
Source: https://docs.windsurf.com/plugins/accounts/api-reference/cascade-analytics

POST https://server.codeium.com/api/v1/CascadeAnalytics
Query Cascade-specific usage metrics and data

## Overview

Retrieve Cascade-specific analytics data including lines suggested/accepted, model usage, credit consumption, and tool usage statistics.

## Request

<ParamField body="service_key" type="string" required>
  Your service key with "Teams Read-only" permissions
</ParamField>

<ParamField body="group_name" type="string">
  Filter results to users in a specific group. Cannot be used with `emails` parameter.
</ParamField>

<ParamField body="start_timestamp" type="string">
  Start time in RFC 3339 format (e.g., `2023-01-01T00:00:00Z`)
</ParamField>

<ParamField body="end_timestamp" type="string">
  End time in RFC 3339 format (e.g., `2023-12-31T23:59:59Z`)
</ParamField>

<ParamField body="emails" type="array">
  Array of email addresses to filter results. Cannot be used with `group_name` parameter.
</ParamField>

<ParamField body="ide_types" type="array">
  Filter by IDE type. Available options:

  * `"editor"` - Windsurf Editor
  * `"jetbrains"` - JetBrains Plugin

  If omitted, returns data for both IDEs.
</ParamField>

<ParamField body="query_requests" type="array" required>
  Array of data source queries to execute. Each object should contain one of the supported data sources.
</ParamField>

## Data Sources

### cascade\_lines

Query for daily Cascade lines suggested and accepted.

```json  theme={null}
{
  "cascade_lines": {}
}
```

**Response Fields:**

* `day` - Date in RFC 3339 format
* `linesSuggested` - Number of lines suggested
* `linesAccepted` - Number of lines accepted

### cascade\_runs

Query for model usage, credit consumption, and mode data.

```json  theme={null}
{
  "cascade_runs": {}
}
```

**Response Fields:**

* `day` - Date in RFC 3339 format
* `model` - Model name used
* `mode` - Cascade mode (see modes below)
* `messagesSent` - Number of messages sent
* `cascadeId` - Unique conversation ID
* `promptsUsed` - Credits consumed (in cents)

**Cascade Modes:**

* `CONVERSATIONAL_PLANNER_MODE_DEFAULT` - Write mode
* `CONVERSATIONAL_PLANNER_MODE_READ_ONLY` - Read mode
* `CONVERSATIONAL_PLANNER_MODE_NO_TOOL` - Legacy mode
* `UNKNOWN` - Unknown mode

### cascade\_tool\_usage

Query for tool usage statistics (aggregate counts).

```json  theme={null}
{
  "cascade_tool_usage": {}
}
```

**Response Fields:**

* `tool` - Tool identifier (see tool mappings below)
* `count` - Number of times tool was used

## Tool Usage Mappings

| Tool Identifier     | Display Name      |
| ------------------- | ----------------- |
| `CODE_ACTION`       | Code Edit         |
| `VIEW_FILE`         | View File         |
| `RUN_COMMAND`       | Run Command       |
| `FIND`              | Find tool         |
| `GREP_SEARCH`       | Grep Search       |
| `VIEW_FILE_OUTLINE` | View File Outline |
| `MQUERY`            | Riptide           |
| `WORKFLOWS_USED`    | Workflows Used    |
| `LIST_DIRECTORY`    | List Directory    |
| `MCP_TOOL`          | MCP Tool          |
| `PROPOSE_CODE`      | Propose Code      |
| `SEARCH_WEB`        | Search Web        |
| `MEMORY`            | Memory            |
| `PROXY_WEB_SERVER`  | Browser Preview   |
| `DEPLOY_WEB_APP`    | Deploy Web App    |

## Example Request

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "group_name": "engineering_team",
  "start_timestamp": "2025-01-01T00:00:00Z",
  "end_timestamp": "2025-01-02T00:00:00Z",
  "emails": ["user1@windsurf.com", "user2@windsurf.com"],
  "ide_types": ["editor"],
  "query_requests": [
    {
      "cascade_lines": {}
    },
    {
      "cascade_runs": {}
    },
    {
      "cascade_tool_usage": {}
    }
  ]
}' \
https://server.codeium.com/api/v1/CascadeAnalytics
```

## Response

<ResponseField name="queryResults" type="array">
  Array of query results, one for each query request

  <Expandable title="Cascade Lines Result">
    <ResponseField name="cascadeLines" type="object">
      <ResponseField name="cascadeLines" type="array">
        Array of daily line statistics

        <ResponseField name="day" type="string">
          Date in RFC 3339 format
        </ResponseField>

        <ResponseField name="linesSuggested" type="string">
          Number of lines suggested on this day
        </ResponseField>

        <ResponseField name="linesAccepted" type="string">
          Number of lines accepted on this day
        </ResponseField>
      </ResponseField>
    </ResponseField>
  </Expandable>

  <Expandable title="Cascade Runs Result">
    <ResponseField name="cascadeRuns" type="object">
      <ResponseField name="cascadeRuns" type="array">
        Array of model usage statistics

        <ResponseField name="day" type="string">
          Date in RFC 3339 format
        </ResponseField>

        <ResponseField name="model" type="string">
          Model name used for the run
        </ResponseField>

        <ResponseField name="mode" type="string">
          Cascade mode identifier
        </ResponseField>

        <ResponseField name="messagesSent" type="string">
          Number of messages sent
        </ResponseField>

        <ResponseField name="cascadeId" type="string">
          Unique conversation identifier
        </ResponseField>

        <ResponseField name="promptsUsed" type="string">
          Credits consumed in cents (e.g., "100" = 1 credit)
        </ResponseField>
      </ResponseField>
    </ResponseField>
  </Expandable>

  <Expandable title="Cascade Tool Usage Result">
    <ResponseField name="cascadeToolUsage" type="object">
      <ResponseField name="cascadeToolUsage" type="array">
        Array of tool usage statistics

        <ResponseField name="tool" type="string">
          Tool identifier
        </ResponseField>

        <ResponseField name="count" type="string">
          Number of times tool was used
        </ResponseField>
      </ResponseField>
    </ResponseField>
  </Expandable>
</ResponseField>

### Example Response

```json  theme={null}
{
  "queryResults": [
    {
      "cascadeLines": {
        "cascadeLines": [
          {
            "day": "2025-05-01T00:00:00Z",
            "linesSuggested": "206",
            "linesAccepted": "157"
          },
          {
            "day": "2025-05-02T00:00:00Z",
            "linesSuggested": "16"
          }
        ]
      }
    },
    {
      "cascadeRuns": {
        "cascadeRuns": [
          {
            "day": "2025-05-01T00:00:00Z",
            "model": "Claude 3.7 Sonnet (Thinking)",
            "mode": "CONVERSATIONAL_PLANNER_MODE_DEFAULT",
            "messagesSent": "1",
            "cascadeId": "0d35c1f7-0a85-41d0-ac96-a04cd2d64444"
          }
        ]
      }
    },
    {
      "cascadeToolUsage": {
        "cascadeToolUsage": [
          {
            "tool": "CODE_ACTION",
            "count": "15"
          },
          {
            "tool": "LIST_DIRECTORY",
            "count": "20"
          }
        ]
      }
    }
  ]
}
```

## Notes

* The API returns raw data which may contain "UNKNOWN" values
* For metrics analysis, aggregate by specific fields of interest (e.g., sum `promptsUsed` for usage patterns)
* Mode and prompt data may be split across multiple entries
* Credit consumption (`promptsUsed`) is returned in cents (100 = 1 credit)



# Custom Analytics Query
Source: https://docs.windsurf.com/plugins/accounts/api-reference/custom-analytics

POST https://server.codeium.com/api/v1/Analytics
Flexible analytics querying with custom selections, filters, and aggregations

## Overview

The Custom Analytics API provides flexible querying capabilities for autocomplete, chat, and command data with customizable selections, filters, aggregations, and orderings.

## Request

<ParamField body="service_key" type="string" required>
  Your service key with "Teams Read-only" permissions
</ParamField>

<ParamField body="group_name" type="string">
  Filter results to users in a specific group (optional)
</ParamField>

<ParamField body="query_requests" type="array" required>
  Array of query request objects defining the data to retrieve
</ParamField>

## Query Request Structure

Each query request object contains:

<ParamField body="data_source" type="string" required>
  Data source to query. Options:

  * `QUERY_DATA_SOURCE_USER_DATA` - Autocomplete data
  * `QUERY_DATA_SOURCE_CHAT_DATA` - Chat data
  * `QUERY_DATA_SOURCE_COMMAND_DATA` - Command data
  * `QUERY_DATA_SOURCE_PCW_DATA` - Percent Code Written data
</ParamField>

<ParamField body="selections" type="array" required>
  Array of field selections to retrieve (see Selections section)
</ParamField>

<ParamField body="filters" type="array">
  Array of filters to apply (see Filters section)
</ParamField>

<ParamField body="aggregations" type="array">
  Array of aggregations to group by (see Aggregations section)
</ParamField>

## Selections

Selections define which fields to retrieve and how to aggregate them.

<ParamField body="field" type="string" required>
  Field name to select (see Available Fields section)
</ParamField>

<ParamField body="name" type="string">
  Alias for the field. If not specified, defaults to `{aggregation_function}_{field_name}` (lowercase)
</ParamField>

<ParamField body="aggregation_function" type="string">
  Aggregation function to apply:

  * `QUERY_AGGREGATION_UNSPECIFIED` (default)
  * `QUERY_AGGREGATION_COUNT`
  * `QUERY_AGGREGATION_SUM`
  * `QUERY_AGGREGATION_AVG`
  * `QUERY_AGGREGATION_MAX`
  * `QUERY_AGGREGATION_MIN`
</ParamField>

### Selection Example

```json  theme={null}
{
  "field": "num_acceptances",
  "name": "total_acceptances",
  "aggregation_function": "QUERY_AGGREGATION_SUM"
}
```

## Filters

Filters narrow down data to elements meeting specific criteria.

<ParamField body="name" type="string" required>
  Field name to filter on
</ParamField>

<ParamField body="value" type="string" required>
  Value to compare against
</ParamField>

<ParamField body="filter" type="string" required>
  Filter operation:

  * `QUERY_FILTER_EQUAL`
  * `QUERY_FILTER_NOT_EQUAL`
  * `QUERY_FILTER_GREATER_THAN`
  * `QUERY_FILTER_LESS_THAN`
  * `QUERY_FILTER_GE` (greater than or equal)
  * `QUERY_FILTER_LE` (less than or equal)
</ParamField>

### Filter Example

```json  theme={null}
{
  "name": "language",
  "filter": "QUERY_FILTER_EQUAL",
  "value": "PYTHON"
}
```

## Aggregations

Aggregations group data by specified criteria.

<ParamField body="field" type="string" required>
  Field name to group by
</ParamField>

<ParamField body="name" type="string" required>
  Alias for the aggregation field
</ParamField>

### Aggregation Example

```json  theme={null}
{
  "field": "ide",
  "name": "ide_type"
}
```

## Available Fields

### User Data

All User Data is aggregated per user, per hour.

| Field Name                 | Description                                            | Valid Aggregations |
| -------------------------- | ------------------------------------------------------ | ------------------ |
| `api_key`                  | Hash of user API key                                   | UNSPECIFIED, COUNT |
| `date`                     | UTC date of autocompletion                             | UNSPECIFIED, COUNT |
| `date UTC-x`               | Date with timezone offset (e.g., "date UTC-8" for PST) | UNSPECIFIED, COUNT |
| `hour`                     | UTC hour of autocompletion                             | UNSPECIFIED, COUNT |
| `language`                 | Programming language                                   | UNSPECIFIED, COUNT |
| `ide`                      | IDE being used                                         | UNSPECIFIED, COUNT |
| `version`                  | Windsurf version                                       | UNSPECIFIED, COUNT |
| `num_acceptances`          | Number of autocomplete acceptances                     | SUM, MAX, MIN, AVG |
| `num_lines_accepted`       | Lines of code accepted                                 | SUM, MAX, MIN, AVG |
| `num_bytes_accepted`       | Bytes accepted                                         | SUM, MAX, MIN, AVG |
| `distinct_users`           | Distinct users                                         | UNSPECIFIED, COUNT |
| `distinct_developer_days`  | Distinct (user, day) tuples                            | UNSPECIFIED, COUNT |
| `distinct_developer_hours` | Distinct (user, hour) tuples                           | UNSPECIFIED, COUNT |

### Chat Data

All Chat Data represents chat model responses, not user questions.

| Field Name                | Description                               | Valid Aggregations |
| ------------------------- | ----------------------------------------- | ------------------ |
| `api_key`                 | Hash of user API key                      | UNSPECIFIED, COUNT |
| `model_id`                | Chat model ID                             | UNSPECIFIED, COUNT |
| `date`                    | UTC date of chat response                 | UNSPECIFIED, COUNT |
| `date UTC-x`              | Date with timezone offset                 | UNSPECIFIED, COUNT |
| `ide`                     | IDE being used                            | UNSPECIFIED, COUNT |
| `version`                 | Windsurf version                          | UNSPECIFIED, COUNT |
| `latest_intent_type`      | Chat intent type (see Intent Types below) | UNSPECIFIED, COUNT |
| `num_chats_received`      | Number of chat messages received          | SUM, MAX, MIN, AVG |
| `chat_accepted`           | Whether chat was accepted (thumbs up)     | SUM, COUNT         |
| `chat_inserted_at_cursor` | Whether "Insert" button was clicked       | SUM, COUNT         |
| `chat_applied`            | Whether "Apply Diff" button was clicked   | SUM, COUNT         |
| `chat_loc_used`           | Lines of code used from chat              | SUM, MAX, MIN, AVG |

#### Chat Intent Types

* `CHAT_INTENT_GENERIC` - Regular chat
* `CHAT_INTENT_FUNCTION_EXPLAIN` - Function explanation code lens
* `CHAT_INTENT_FUNCTION_DOCSTRING` - Function docstring code lens
* `CHAT_INTENT_FUNCTION_REFACTOR` - Function refactor code lens
* `CHAT_INTENT_CODE_BLOCK_EXPLAIN` - Code block explanation code lens
* `CHAT_INTENT_CODE_BLOCK_REFACTOR` - Code block refactor code lens
* `CHAT_INTENT_PROBLEM_EXPLAIN` - Problem explanation code lens
* `CHAT_INTENT_FUNCTION_UNIT_TESTS` - Function unit tests code lens

### Command Data

Command Data includes all commands, including declined ones. Use the `accepted` field to filter for accepted commands only.

| Field Name        | Description                                        | Valid Aggregations |
| ----------------- | -------------------------------------------------- | ------------------ |
| `api_key`         | Hash of user API key                               | UNSPECIFIED, COUNT |
| `date`            | UTC date of command                                | UNSPECIFIED, COUNT |
| `timestamp`       | UTC timestamp of command                           | UNSPECIFIED, COUNT |
| `language`        | Programming language                               | UNSPECIFIED, COUNT |
| `ide`             | IDE being used                                     | UNSPECIFIED, COUNT |
| `version`         | Windsurf version                                   | UNSPECIFIED, COUNT |
| `command_source`  | Command trigger source (see Command Sources below) | UNSPECIFIED, COUNT |
| `provider_source` | Generation or edit mode                            | UNSPECIFIED, COUNT |
| `lines_added`     | Lines of code added                                | SUM, MAX, MIN, AVG |
| `lines_removed`   | Lines of code removed                              | SUM, MAX, MIN, AVG |
| `bytes_added`     | Bytes added                                        | SUM, MAX, MIN, AVG |
| `bytes_removed`   | Bytes removed                                      | SUM, MAX, MIN, AVG |
| `selection_lines` | Lines selected (zero for generations)              | SUM, MAX, MIN, AVG |
| `selection_bytes` | Bytes selected (zero for generations)              | SUM, MAX, MIN, AVG |
| `accepted`        | Whether command was accepted                       | SUM, COUNT         |

#### Command Sources

* `COMMAND_REQUEST_SOURCE_LINE_HINT_CODE_LENS`
* `COMMAND_REQUEST_SOURCE_DEFAULT` - Typical command usage
* `COMMAND_REQUEST_SOURCE_RIGHT_CLICK_REFACTOR`
* `COMMAND_REQUEST_SOURCE_FUNCTION_CODE_LENS`
* `COMMAND_REQUEST_SOURCE_FOLLOWUP`
* `COMMAND_REQUEST_SOURCE_CLASS_CODE_LENS`
* `COMMAND_REQUEST_SOURCE_PLAN`
* `COMMAND_REQUEST_SOURCE_SELECTION_HINT_CODE_LENS`

#### Provider Sources

* `PROVIDER_SOURCE_COMMAND_GENERATE` - Generation mode
* `PROVIDER_SOURCE_COMMAND_EDIT` - Edit mode

### PCW Data

Percent Code Written data with separate tracking for autocomplete and command contributions.

| Field Name                      | Description                                                   | Valid Aggregations |
| ------------------------------- | ------------------------------------------------------------- | ------------------ |
| `percent_code_written`          | Calculated as codeium\_bytes / (codeium\_bytes + user\_bytes) | UNSPECIFIED        |
| `codeium_bytes`                 | Total Codeium-generated bytes                                 | UNSPECIFIED        |
| `user_bytes`                    | Total user-written bytes                                      | UNSPECIFIED        |
| `total_bytes`                   | codeium\_bytes + user\_bytes                                  | UNSPECIFIED        |
| `codeium_bytes_by_autocomplete` | Codeium bytes from autocomplete                               | UNSPECIFIED        |
| `codeium_bytes_by_command`      | Codeium bytes from command                                    | UNSPECIFIED        |

#### PCW Filters

| Field Name | Description          | Examples          |
| ---------- | -------------------- | ----------------- |
| `language` | Programming language | KOTLIN, GO, JAVA  |
| `ide`      | IDE being used       | jetbrains, vscode |
| `version`  | Windsurf version     | 1.28.0, 130.0     |

For date filtering in PCW queries, use `start_timestamp` and `end_timestamp` in the main request body.

## Example Requests

### User Data Example

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "query_requests": [
    {
      "data_source": "QUERY_DATA_SOURCE_USER_DATA",
      "selections": [
        {
          "field": "num_acceptances",
          "name": "total_acceptances",
          "aggregation_function": "QUERY_AGGREGATION_SUM"
        },
        {
          "field": "num_lines_accepted",
          "name": "total_lines",
          "aggregation_function": "QUERY_AGGREGATION_SUM"
        }
      ],
      "filters": [
        {
          "name": "hour",
          "filter": "QUERY_FILTER_GE",
          "value": "2024-01-01"
        },
        {
          "name": "hour",
          "filter": "QUERY_FILTER_LE",
          "value": "2024-02-01"
        }
      ]
    }
  ]
}' \
https://server.codeium.com/api/v1/Analytics
```

### Chat Data Example

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "query_requests": [
    {
      "data_source": "QUERY_DATA_SOURCE_CHAT_DATA",
      "selections": [
        {
          "field": "chat_loc_used",
          "name": "lines_used",
          "aggregation_function": "QUERY_AGGREGATION_SUM"
        }
      ],
      "filters": [
        {
          "name": "latest_intent_type",
          "filter": "QUERY_FILTER_EQUAL",
          "value": "CHAT_INTENT_FUNCTION_DOCSTRING"
        }
      ],
      "aggregations": [
        {
          "field": "ide",
          "name": "ide_type"
        }
      ]
    }
  ]
}' \
https://server.codeium.com/api/v1/Analytics
```

### Command Data Example

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "query_requests": [
    {
      "data_source": "QUERY_DATA_SOURCE_COMMAND_DATA",
      "selections": [
        {
          "field": "lines_added",
          "name": "total_lines_added",
          "aggregation_function": "QUERY_AGGREGATION_SUM"
        },
        {
          "field": "lines_removed",
          "name": "total_lines_removed",
          "aggregation_function": "QUERY_AGGREGATION_SUM"
        }
      ],
      "filters": [
        {
          "name": "provider_source",
          "filter": "QUERY_FILTER_EQUAL",
          "value": "PROVIDER_SOURCE_COMMAND_EDIT"
        },
        {
          "name": "accepted",
          "filter": "QUERY_FILTER_EQUAL",
          "value": "true"
        }
      ],
      "aggregations": [
        {
          "field": "language",
          "name": "programming_language"
        }
      ]
    }
  ]
}' \
https://server.codeium.com/api/v1/Analytics
```

### PCW Data Example

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "start_timestamp": "2024-01-01T00:00:00Z",
  "end_timestamp": "2024-12-22T00:00:00Z",
  "query_requests": [
    {
      "data_source": "QUERY_DATA_SOURCE_PCW_DATA",
      "selections": [
        {
          "field": "percent_code_written",
          "name": "pcw"
        },
        {
          "field": "codeium_bytes",
          "name": "ai_bytes"
        },
        {
          "field": "total_bytes",
          "name": "total"
        },
        {
          "field": "codeium_bytes_by_autocomplete",
          "name": "autocomplete_bytes"
        },
        {
          "field": "codeium_bytes_by_command",
          "name": "command_bytes"
        }
      ],
      "filters": [
        {
          "filter": "QUERY_FILTER_EQUAL",
          "name": "language",
          "value": "GO"
        }
      ]
    }
  ]
}' \
https://server.codeium.com/api/v1/Analytics
```

## Response

<ResponseField name="queryResults" type="array">
  Array of query results, one for each query request

  <ResponseField name="responseItems" type="array">
    Array of result items

    <ResponseField name="item" type="object">
      Object containing the selected fields and their values
    </ResponseField>
  </ResponseField>
</ResponseField>

### Example Responses

#### User Data Response

```json  theme={null}
{
  "queryResults": [
    {
      "responseItems": [
        {
          "item": {
            "total_acceptances": "125",
            "total_lines": "863"
          }
        }
      ]
    }
  ]
}
```

#### Chat Data Response

```json  theme={null}
{
  "queryResults": [
    {
      "responseItems": [
        {
          "item": {
            "lines_used": "74",
            "ide_type": "jetbrains"
          }
        },
        {
          "item": {
            "lines_used": "41",
            "ide_type": "vscode"
          }
        }
      ]
    }
  ]
}
```

#### Command Data Response

```json  theme={null}
{
  "queryResults": [
    {
      "responseItems": [
        {
          "item": {
            "programming_language": "PYTHON",
            "total_lines_added": "21",
            "total_lines_removed": "5"
          }
        },
        {
          "item": {
            "programming_language": "GO",
            "total_lines_added": "31",
            "total_lines_removed": "27"
          }
        }
      ]
    }
  ]
}
```

#### PCW Data Response

```json  theme={null}
{
  "queryResults": [
    {
      "responseItems": [
        {
          "item": {
            "ai_bytes": "6018",
            "autocomplete_bytes": "4593",
            "command_bytes": "1425",
            "pcw": "0.61",
            "total": "9900"
          }
        }
      ]
    }
  ]
}
```

## Important Notes

* PCW (Percent Code Written) has high variance within single days or users - aggregate over weeks for better insights
* All selection fields must either have aggregation functions or none should (cannot mix)
* Fields with "distinct\_\*" pattern cannot be used in aggregations
* Field aliases must be unique across all selections and aggregations
* If no aggregation function is specified, it defaults to UNSPECIFIED



# Error Handling
Source: https://docs.windsurf.com/plugins/accounts/api-reference/errors

Common error messages and debugging tips for the Analytics API

## Overview

The Analytics API returns detailed error messages to help debug invalid queries. This page covers common error scenarios and how to resolve them.

## Error Response Format

When an error occurs, the API returns an error response with a descriptive message:

```json  theme={null}
{
  "error": "Error message describing what went wrong"
}
```

## Common Errors

### Authentication Errors

<AccordionGroup>
  <Accordion title="Invalid service key">
    **Error:** `Invalid service key`

    **Cause:** The provided service key is not valid or has been revoked.

    **Solution:**

    * Verify your service key is correct
    * Check that the service key hasn't been revoked
    * Generate a new service key if needed
  </Accordion>

  <Accordion title="Insufficient permissions">
    **Error:** `Insufficient permissions`

    **Cause:** The service key doesn't have the required "Teams Read-only" permissions.

    **Solution:**

    * Update the service key permissions in team settings
    * Ensure the service key has "Teams Read-only" access
  </Accordion>
</AccordionGroup>

### Query Structure Errors

<AccordionGroup>
  <Accordion title="Missing selections">
    **Error:** `at least one field or aggregation is required`

    **Cause:** The query request doesn't contain any selections or aggregations.

    **Solution:** Add at least one selection to your query request:

    ```json  theme={null}
    "selections": [
      {
        "field": "num_acceptances",
        "aggregation_function": "QUERY_AGGREGATION_SUM"
      }
    ]
    ```
  </Accordion>

  <Accordion title="Invalid data source">
    **Error:** `invalid query table: QUERY_DATA_SOURCE_UNSPECIFIED`

    **Cause:** There's likely a typo in the `data_source` field.

    **Solution:** Double-check the spelling of your data source. Valid options:

    * `QUERY_DATA_SOURCE_USER_DATA`
    * `QUERY_DATA_SOURCE_CHAT_DATA`
    * `QUERY_DATA_SOURCE_COMMAND_DATA`
    * `QUERY_DATA_SOURCE_PCW_DATA`
  </Accordion>

  <Accordion title="Mixed aggregation functions">
    **Error:** `all selection fields should have an aggregation function, or none of them should`

    **Cause:** Some selections have aggregation functions while others don't.

    **Solution:** Either add aggregation functions to all selections or remove them from all:

    **Invalid:**

    ```json  theme={null}
    "selections": [
      {
        "field": "num_acceptances",
        "aggregation_function": "QUERY_AGGREGATION_SUM"
      },
      {
        "field": "num_lines_accepted",
        "aggregation_function": "QUERY_AGGREGATION_UNSPECIFIED"
      }
    ]
    ```

    **Valid:**

    ```json  theme={null}
    "selections": [
      {
        "field": "num_acceptances",
        "aggregation_function": "QUERY_AGGREGATION_SUM"
      },
      {
        "field": "num_lines_accepted",
        "aggregation_function": "QUERY_AGGREGATION_SUM"
      }
    ]
    ```
  </Accordion>
</AccordionGroup>

### Field and Aggregation Errors

<AccordionGroup>
  <Accordion title="Invalid aggregation function">
    **Error:** `invalid aggregation function for string type field ide: QUERY_AGGREGATION_SUM`

    **Cause:** The aggregation function is not supported for the specified field type.

    **Solution:** Check the [Available Fields](/plugins/accounts/api-reference/custom-analytics#available-fields) section to see which aggregation functions are valid for each field. String fields typically only support `COUNT` and `UNSPECIFIED`.
  </Accordion>

  <Accordion title="Distinct field aggregation">
    **Error:** `tried to aggregate on a distinct field: distinct_developer_days. Consider aggregating on the non-distinct fields instead: [api_key date]`

    **Cause:** Fields with the "distinct\_\*" pattern cannot be used in the aggregations section.

    **Solution:** Use the suggested alternative fields for aggregation:

    **Invalid:**

    ```json  theme={null}
    "aggregations": [
      {
        "field": "distinct_developer_days",
        "name": "distinct_developer_days"
      }
    ]
    ```

    **Valid:**

    ```json  theme={null}
    "aggregations": [
      {
        "field": "api_key",
        "name": "api_key"
      },
      {
        "field": "date",
        "name": "date"
      }
    ]
    ```
  </Accordion>

  <Accordion title="Duplicate field aliases">
    **Error:** `duplicate field alias for selection/aggregation: num_acceptances`

    **Cause:** Multiple selections or aggregations have the same name.

    **Solution:** Ensure all field aliases are unique. Remember that if no name is specified, it defaults to `{aggregation_function}_{field_name}`.
  </Accordion>
</AccordionGroup>

### Data Filtering Errors

<AccordionGroup>
  <Accordion title="Invalid group name">
    **Error:** `invalid group name: GroupName`

    **Cause:** The specified group name doesn't exist in your organization.

    **Solution:**

    * Double-check the group name spelling
    * Verify the group exists in your team settings
    * Use the exact group name as it appears in your team dashboard
  </Accordion>

  <Accordion title="Invalid timestamp format">
    **Error:** `invalid timestamp format`

    **Cause:** The timestamp is not in the correct RFC 3339 format.

    **Solution:** Use the correct timestamp format:

    ```
    2023-01-01T00:00:00Z
    ```

    **Valid examples:**

    * `2024-01-01T00:00:00Z`
    * `2024-12-31T23:59:59Z`
    * `2024-06-15T12:30:45Z`
  </Accordion>

  <Accordion title="Conflicting filters">
    **Error:** `Cannot use both group_name and emails parameters`

    **Cause:** Both `group_name` and `emails` parameters were provided in a Cascade Analytics request.

    **Solution:** Use either `group_name` OR `emails`, but not both:

    **Invalid:**

    ```json  theme={null}
    {
      "group_name": "engineering",
      "emails": ["user@example.com"]
    }
    ```

    **Valid:**

    ```json  theme={null}
    {
      "group_name": "engineering"
    }
    ```

    **Or:**

    ```json  theme={null}
    {
      "emails": ["user@example.com", "user2@example.com"]
    }
    ```
  </Accordion>
</AccordionGroup>

## Rate Limiting

<AccordionGroup>
  <Accordion title="Rate limit exceeded">
    **Error:** `429 Too Many Requests`

    **Cause:** You've exceeded the API rate limit.

    **Solution:**

    * Wait before making additional requests
    * Implement exponential backoff in your client
    * Consider batching multiple queries into single requests where possible
    * Contact support if you need higher rate limits
  </Accordion>
</AccordionGroup>

## Debugging Tips

### 1. Start Simple

Begin with basic queries and gradually add complexity:

```json  theme={null}
{
  "service_key": "your_key",
  "query_requests": [
    {
      "data_source": "QUERY_DATA_SOURCE_USER_DATA",
      "selections": [
        {
          "field": "num_acceptances",
          "aggregation_function": "QUERY_AGGREGATION_COUNT"
        }
      ]
    }
  ]
}
```

### 2. Validate Field Names

Double-check field names against the [Available Fields](/plugins/accounts/api-reference/custom-analytics#available-fields) documentation.

### 3. Check Aggregation Compatibility

Ensure your aggregation functions are compatible with the field types you're selecting.

### 4. Test Filters Separately

If your query isn't returning expected results, try removing filters one by one to isolate the issue.

### 5. Use Proper JSON Formatting

Ensure your JSON is properly formatted and all strings are quoted correctly.

## Getting Help

If you continue to experience issues:

1. **Check the error message carefully** - Most errors include specific guidance on how to fix the issue
2. **Review the examples** - Compare your query structure to the working examples in the documentation
3. **Contact support** - Reach out to [Windsurf Support](https://windsurf.com/support) with your specific error message and query

## API Version Notes

Error handling and validation have been improved in API version 1.10.0 and later. If you're using an older version, consider updating to get more detailed error messages.



# Set Usage Configuration
Source: https://docs.windsurf.com/plugins/accounts/api-reference/usage-config

POST https://server.codeium.com/api/v1/UsageConfig
Configure usage caps for add-on credits

## Overview

Set or clear usage caps on add-on credits for your organization. You can scope these configurations to the team level, specific groups, or individual users.

## Request

<ParamField body="service_key" type="string" required>
  Your service key with appropriate permissions
</ParamField>

### Credit Cap Configuration (Choose One)

<ParamField body="clear_add_on_credit_cap" type="boolean">
  Set to `true` to clear the existing add-on credit cap
</ParamField>

<ParamField body="set_add_on_credit_cap" type="integer">
  Set a new add-on credit cap (integer value)
</ParamField>

<Info>
  You must provide either `clear_add_on_credit_cap` or `set_add_on_credit_cap`, but not both.
</Info>

### Scope Configuration (Choose One)

<ParamField body="team_level" type="boolean">
  Set to `true` to apply the configuration at the team level
</ParamField>

<ParamField body="group_id" type="string">
  Apply the configuration to a specific group by providing the group ID
</ParamField>

<ParamField body="user_email" type="string">
  Apply the configuration to a specific user by providing their email address
</ParamField>

<Info>
  You must provide one of `team_level`, `group_id`, or `user_email` to define the scope.
</Info>

### Example Request - Set Credit Cap for Team

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "set_add_on_credit_cap": 10000,
  "team_level": true
}' \
https://server.codeium.com/api/v1/UsageConfig
```

### Example Request - Set Credit Cap for Group

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "set_add_on_credit_cap": 5000,
  "group_id": "engineering_team"
}' \
https://server.codeium.com/api/v1/UsageConfig
```

### Example Request - Set Credit Cap for User

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "set_add_on_credit_cap": 1000,
  "user_email": "user@example.com"
}' \
https://server.codeium.com/api/v1/UsageConfig
```

### Example Request - Clear Credit Cap

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "clear_add_on_credit_cap": true,
  "team_level": true
}' \
https://server.codeium.com/api/v1/UsageConfig
```

## Response

The response body is empty. A `200` status code indicates the operation was successful.

## Error Responses

Common error scenarios:

* Invalid service key or insufficient permissions
* Both `clear_add_on_credit_cap` and `set_add_on_credit_cap` provided
* Neither `clear_add_on_credit_cap` nor `set_add_on_credit_cap` provided
* Multiple scope parameters provided
* No scope parameter provided
* Invalid group ID or user email
* Rate limit exceeded



# Get User Page Analytics
Source: https://docs.windsurf.com/plugins/accounts/api-reference/user-page-analytics

POST https://server.codeium.com/api/v1/UserPageAnalytics
Retrieve user activity data from the teams page

## Overview

Get user activity statistics that appear on the teams page, including user names, emails, last activity times, and active days.

## Request

<ParamField body="service_key" type="string" required>
  Your service key with "Teams Read-only" permissions
</ParamField>

<ParamField body="group_name" type="string">
  Filter results to users in a specific group (optional)
</ParamField>

<ParamField body="start_timestamp" type="string">
  Start time in RFC 3339 format (e.g., `2023-01-01T00:00:00Z`)
</ParamField>

<ParamField body="end_timestamp" type="string">
  End time in RFC 3339 format (e.g., `2023-12-31T23:59:59Z`)
</ParamField>

### Example Request

```bash  theme={null}
curl -X POST --header "Content-Type: application/json" \
--data '{
  "service_key": "your_service_key_here",
  "group_name": "engineering_team",
  "start_timestamp": "2024-01-01T00:00:00Z",
  "end_timestamp": "2024-12-31T23:59:59Z"
}' \
https://server.codeium.com/api/v1/UserPageAnalytics
```

## Response

<ResponseField name="userTableStats" type="array">
  Array of user statistics objects

  <Expandable title="User Statistics Object">
    <ResponseField name="name" type="string">
      User's display name
    </ResponseField>

    <ResponseField name="email" type="string">
      User's email address
    </ResponseField>

    <ResponseField name="lastUpdateTime" type="string">
      Timestamp of user's last activity in RFC 3339 format
    </ResponseField>

    <ResponseField name="apiKey" type="string">
      Hashed version of the user's API key
    </ResponseField>

    <ResponseField name="activeDays" type="number">
      The total number of days the user has been active during the queried timeframe
    </ResponseField>

    <ResponseField name="disableCodeium" type="boolean">
      Indicates whether Windsurf access has been disabled for the user by an admin. This field is only present if access has been explicitly disabled, and will always be set to true in that case.
    </ResponseField>

    <ResponseField name="lastAutocompleteUsageTime" type="string">
      The most recent timestamp the Tab/Autocomplete modality was used in RFC 3339 format
    </ResponseField>

    <ResponseField name="lastChatUsageTime" type="string">
      The most recent timestamp the Cascade modality was used in RFC 3339 format
    </ResponseField>

    <ResponseField name="lastCommandUsageTime" type="string">
      The most recent timestamp the command modality was used in RFC 3339 format
    </ResponseField>
  </Expandable>
</ResponseField>

### Example Response

```json  theme={null}
{
  "userTableStats": [
    {
      "name": "Alice",
      "email": "alice@windsurf.com",
      "lastUpdateTime": "2024-10-10T22:56:10.771591Z",
      "apiKey": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
      "activeDays": 178
    },
    {
      "name": "Bob",
      "email": "bob@windsurf.com",
      "lastUpdateTime": "2024-10-10T18:11:23.980237Z",
      "apiKey": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
      "activeDays": 462
    },
    {
      "name": "Charlie",
      "email": "charlie@windsurf.com",
      "lastUpdateTime": "2024-10-10T16:43:46.117870Z",
      "apiKey": "cccccccc-cccc-cccc-cccc-cccccccccccc",
      "activeDays": 237
    }
  ]
}
```

## Error Responses

<ResponseField name="error" type="string">
  Error message describing what went wrong
</ResponseField>

Common error scenarios:

* Invalid service key or insufficient permissions
* Invalid timestamp format
* Group not found
* Rate limit exceeded



# Role Based Access & Management
Source: https://docs.windsurf.com/plugins/accounts/rbac-role-management

Configure and manage role-based access controls, permissions, and user management for your Windsurf team

Windsurf's Role-Based Access Control system provides granular, role-based access to enterprise resources, enabling administrators to assign permissions and roles dynamically for secure and efficient access management.

<Note>Role-based access features are available for Teams and Enterprise plans.</Note>

## Role Based Access Controls

Windsurf's role-based access system allows enterprise organizations to implement fine-grained access controls across all team resources. The system enables:

* **Granular Permission Management**: Control access to specific features and data based on user roles
* **Dynamic Role Assignment**: Administrators can assign and modify roles for individual users or user groups
* **Secure Resource Access**: Ensure users only have access to the resources they need for their responsibilities
* **Audit and Compliance**: Track user permissions and access patterns for security and compliance requirements

The role-based access system integrates seamlessly with Windsurf's existing authentication mechanisms, including SSO and SCIM, to provide a comprehensive security framework for enterprise deployments.

## Role Management

<Note>We are continually working to improve role management features and functionality.</Note>

Roles can be created and managed in the Windsurf admin console via the Settings tab. For Windsurf's SaaS offering, access the Settings tab at:

<Card title="Team Settings" horizontal={true} icon="gear" href="https://windsurf.com/team/settings">
  Manage roles, permissions, and team settings from the admin console.
</Card>

### Creating a New Role

<Steps>
  <Step title="Navigate to Role Management">
    Go to [windsurf.com/team/settings](https://windsurf.com/team/settings) and locate the Role Management section.
  </Step>

  <Step title="Create Role">
    Click the **"Create Role"** button to start creating a new role.
  </Step>

  <Step title="Configure Role">
    Enter a descriptive name for the role and select the appropriate permissions from the checkbox list.
  </Step>

  <Step title="Save Role">
    Review your selections and save the new role. It will now be available for assignment to users.
  </Step>
</Steps>

## Role Permissions

Windsurf provides two default roles out of the box:

* **Admin Role**: Includes all available permissions for complete system access
* **User Role**: Includes no permissions by default, providing a minimal access baseline

### Modifying Role Permissions

To modify permissions for custom roles, click the permissions dropdown next to the role name in the Role Management section. This allows you to add or remove specific permissions as needed.

### Available Permissions

Windsurf offers a comprehensive set of permissions organized into the following categories:

#### Attribution

* **Attribution Read**: Read access to the attribution page

#### Analytics

* **Analytics Read**: Read access to the analytics page

#### Teams

* **Teams Read-Only**: Read-only access to the teams page
* **Teams Update**: Allows updating user roles in the teams page
* **Teams Delete**: Allows deleting users from the teams page
* **Teams Invite**: Allows inviting users to the teams page

#### Indexing

* **Indexing Read**: Read access to the indexing page
* **Indexing Create**: Create access to the indexing page
* **Indexing Update**: Allows updating indexed repos
* **Indexing Delete**: Allows deleting indexes
* **Indexing Management**: Allows index database management and pruning

#### SSO

* **SSO Read**: Read access to the SSO page
* **SSO Write**: Write access to the SSO page

#### Service Key

* **Service Key Read**: Read access to the service keys page
* **Service Key Create**: Allows creating service keys
* **Service Key Update**: Allows updating service keys
* **Service Key Delete**: Allows deleting service keys

#### Billing

* **Billing Read**: Read access to the billing page
* **Billing Write**: Write access to the billing page

#### Role Management

* **Role Read**: Read access to the roles tab in settings
* **Role Create**: Able to create new roles
* **Role Update**: Allows updating roles
* **Role Delete**: Allows deleting roles

#### Team Settings

* **Team Settings Read**: Allows read access to team settings
* **Team Settings Update**: Allows updating team settings

### Disable Windsurf Access Feature

For administrators who need access to team analytics and audit/attribution logging but do not wish to consume a license, Windsurf provides a "disable Windsurf access" feature.

To access this feature:

<Steps>
  <Step title="Navigate to Manage Team">
    Go to the **"Manage Team"** tab in your team settings.
  </Step>

  <Step title="Edit User">
    Find the user you want to modify and click **"Edit"** next to their name.
  </Step>

  <Step title="Disable Access">
    In the user edit dialog, you can disable their Windsurf access while maintaining their administrative permissions for analytics and logging.
  </Step>
</Steps>

## User Groups

<Note>User Groups are available for Enterprise organizations with SCIM integration enabled.</Note>

For enterprise organizations, Windsurf offers the ability to split users into multiple user groups via SCIM (System for Cross-domain Identity Management) integration. This feature enables:

* **Organizational Structure**: Mirror your company's organizational structure within Windsurf
* **Group-Based Analytics**: View analytics and usage data filtered by specific user groups
* **Delegated Administration**: Assign group administrators who can manage specific user groups
* **Scalable Management**: Efficiently manage large numbers of users through group-based operations

User groups are automatically synchronized with your identity provider through SCIM, ensuring that organizational changes are reflected in Windsurf's access controls.

## User Management

Windsurf's role-based access functionality allows administrators to assign roles to individual users or user groups, providing flexible access control management.

### Assigning Roles to Users

User role management is performed in the Windsurf admin console at [windsurf.com/team/settings](https://windsurf.com/team/settings).

<Steps>
  <Step title="Navigate to User Management">
    Go to the team settings page and locate the user management section.
  </Step>

  <Step title="Find User">
    Scroll through the user list or use the search functionality to find the user you want to modify. Users can be sorted alphabetically by name, email, sign-up time, or last login.
  </Step>

  <Step title="Edit User Role">
    Click **"Edit"** next to the user's name to open the user management dialog.
  </Step>

  <Step title="Select Role">
    In the pop-out window, select the appropriate role from the dropdown menu.
  </Step>

  <Step title="Save Changes">
    Confirm your selection and save the changes. The new role will be applied immediately.
  </Step>
</Steps>

### Administrative Hierarchy

Windsurf's role-based access system recognizes different levels of administrative access:

* **Super Admin**: Users with the admin role in the "all users" group have complete system access and can modify any role or permission
* **Group Admins**: Administrators of specific user groups can only make role and permission changes within their assigned groups

This hierarchical structure ensures that administrative responsibilities can be delegated appropriately while maintaining security boundaries.

### User Sorting and Management

The user management interface provides several sorting options to help administrators efficiently manage large teams:

* **Alphabetical by Name**: Sort users by their display names
* **Email Address**: Sort users by their email addresses
* **Sign-up Time**: View users in order of when they joined the team
* **Last Login**: Sort by most recent activity to identify active users

These sorting options make it easier to find specific users and understand team engagement patterns.



# Setting up SSO & SCIM
Source: https://docs.windsurf.com/plugins/accounts/sso-scim



This feature is only available to Teams and Enterprise users.

<Tabs>
  <Tab title="Google SSO">
    Windsurf now supports sign in with Single Sign-On (SSO) via SAML. If your organization uses Microsoft Entra, Okta, Google Workspaces, or some other identity provider that supports SAML, you will be able to use SSO with Windsurf.

    <Note>Windsurf only supports SP-initiated SSO; IDP-initiated SSO is NOT currently supported.</Note>

    ### Configure IDP Application

    On the google admin console (admin.google.com) click **Apps -> Web and mobile apps** on the left.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9d300c86c609da6ee3fb630e91f4de3e" data-og-width="530" width="530" data-og-height="788" height="788" data-path="assets/auth/sso-google.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9403af117b9c97981fe559adb9b978fc 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=058d140139f82caca5fee61a7d1f68cf 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b94d0aaf6b28f8646827af8918d07df8 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f3898fed99df69da663658fd214d8676 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7a78f68f99b617431f0df9f765a8bec0 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=19da5d516023353f4cc46dba47ce5b25 2500w" />
    </Frame>

    Click on **Add app**, and then **Add custom SAML app**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=44375b535f269f130aea8c5bd6e736be" data-og-width="514" width="514" data-og-height="534" height="534" data-path="assets/auth/sso-google2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=15b8ea405f2270379d74bfc0f4f2d59b 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4a7a6ea30e5b1656dd8e92612494d632 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=db37dd58c7c32527476d114151bb7b66 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=baa8aaa599b97b9c59f45eb0796febb4 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5c1ae0fe3ac82b2965a2eea3601af438 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google2.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f67c6c78e1ff1bd171532584e4aa7c2f 2500w" />
    </Frame>

    Fill out **App name** with `Windsurf`, and click **Next**.

    The next screen (Google Identity Provider details) on Google’s console page has data you’ll need to copy to Windsurf’s SSO settings on [https://windsurf.com/team/settings](https://windsurf.com/team/settings).

    * Copy **SSO URL** from Google’s console page to Windsurf’s settings under **SSO URL**

    * Copy **Entity ID** from Google’s console page to Windsurf’s settings under **Idp Entity ID**

    * Copy **Certificate** from Google’s console page to Windsurf’s settings under **X509 Certificate**

    * Click **Continue** on Google’s console page

    The next screen on Google’s console page requires you to copy data from Codeium’s settings page

    * Copy **Callback URL** from Codeium’s settings page to Google’s console page under **ACS URL**
    * Copy **SP Entity ID** from Codeium’s settings page to Google’s console page under **SP Entity ID**
    * Change **Name ID** format to **EMAIL**
    * Click **Continue** on Google’s console page

    The next screen on Google’s console page requires some configuration

    * Click on **Add Mapping**, select **First name** and set the **App attributes** to **firstName**
    * Click on **Add Mapping**, select **Last name** and set the **App attributes** to **lastName**
    * Click **Finish**

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c29f0ebf5a05dd5fae3a1127c4111d29" data-og-width="2078" width="2078" data-og-height="862" height="862" data-path="assets/auth/sso-google3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=585b8d21d5b284ee28d9bd911c0d4295 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1a0dd06112db14e2acabe0750583dd71 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c82b1e1f6cf07b54049170ee5ac36eda 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fdac0e1950fd2e618710c99cee1c7656 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=45f58fd68db2619d5e87b3995c7103bf 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-google3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d6ae5462ed098ae48de0aa6b5801cacf 2500w" />
    </Frame>

    On Codeium’s settings page, click **Enable Login with SAML**, and then click **Save**. Make sure to click on **Test Login** to make sure login works as expected. All users now will have SSO login enforced.
  </Tab>

  <Tab title="Azure AD SSO">
    Windsurf Enterprise now supports sign in with Single Sign-On (SSO) via SAML. If your organization uses Microsoft Entra ID (formerly Azure AD), you will be able to use SSO with Windsurf.

    <Note>Windsurf only supports SP-initiated SSO; IDP-initiated SSO is NOT currently supported.</Note>

    ## Part 1: Create Enterprise Application in Microsoft Entra ID

    <Note>All steps in this section are performed in the **Microsoft Entra ID admin center**.</Note>

    1. In Microsoft Entra ID, click on **Add**, and then **Enterprise Application**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=70c1ef27e1870d1f95176d12cd7c9c47" data-og-width="854" width="854" data-og-height="384" height="384" data-path="assets/auth/sso-azure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1b88d7269fba84433a203348fd8a3920 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2f71d980824f058c3a36d499f4f488d6 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9bef7d83fd3afa0d42b25b81ab20d8e3 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b9c7eb219d3ff471f38175b0be2cdac8 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6802d42ea85adeb86d22f32e59ef8a5f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0eac589296d06ffcf16e6d2bdc771d0c 2500w" />
    </Frame>

    2. Click on **Create your own application**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d8d3d2b159172edef9033487d1167b52" data-og-width="680" width="680" data-og-height="202" height="202" data-path="assets/auth/sso-azure2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=66949d79e560dcf2c75bcafdcfb1b54a 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6ad3c318b6e47fa95b3e8677d01846ce 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=febe960a9ff782cebaf247868fd22bee 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f1c804a5b3dd2310840c95327f46241c 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7c4186eb8abb76e222579aae95f5b000 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure2.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1274eed53f279fbe64b0d52294708672 2500w" />
    </Frame>

    3. Name your application **Windsurf**, select *Integrate any other application you don't find in the gallery*, and then click **Create**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=38dd3186171705ca16387dfff4a5b24b" data-og-width="968" width="968" data-og-height="342" height="342" data-path="assets/auth/sso-azure3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6c9dc6a0601145171999431fb61e0c4d 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=87b686e30cea98fa1075ceffc0fa40f1 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b03c9c18b557b0f3d113d86fa8c30577 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=43bd3dc28697ed33fe0342dd456d2d3d 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=20d19e9d664e7c835253b775229a969f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-azure3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=abebde3954de441e86f120269ac6b092 2500w" />
    </Frame>

    ## Part 2: Configure SAML and User Attributes in Microsoft Entra ID

    <Note>All steps in this section are performed in the **Microsoft Entra ID admin center**.</Note>

    4. In your new Windsurf application, click on **Set up single sign on**, then click **SAML**.

    5. Click on **Edit** under **Basic SAML Configuration**.

    6. **Keep this Entra ID tab open** and open a new tab to navigate to the **Windsurf Teams SSO settings** at [https://windsurf.com/team/settings](https://windsurf.com/team/settings).

    7. In the **Microsoft Entra ID** SAML configuration form:
       * **Identifier (Entity ID)**: Copy the **SP Entity ID** value from the **Windsurf SSO settings page**
       * **Reply URL (Assertion Consumer Service URL)**: Copy the **Callback URL** value from the **Windsurf SSO settings page**
       * Click **Save** at the top

    8. Configure user attributes for proper name display. In **Microsoft Entra ID**, under **Attributes & Claims**, click **Edit**.

    9. Create 2 new claims by clicking **Add new claim** for each:
       * **First claim**: Name = `firstName`, Source attribute = `user.givenname`
       * **Second claim**: Name = `lastName`, Source attribute = `user.surname`

    ## Part 3: Configure SSO Settings in Windsurf Portal

    <Note>Complete the configuration in the **Windsurf portal** ([https://windsurf.com/team/settings](https://windsurf.com/team/settings)).</Note>

    10. In the **Windsurf SSO settings page**:
        * **Pick your SSO ID**: Choose a unique identifier for your team's login portal (this cannot be changed later)
        * **IdP Entity ID**: Copy the value from **Microsoft Entra ID** under **Set up Windsurf** → **Microsoft Entra Identifier**
        * **SSO URL**: Copy the **Login URL** value from **Microsoft Entra ID**
        * **X509 Certificate**: Download the **SAML certificate (Base64)** from **Microsoft Entra ID**, open the file, and paste the text content here

    11. In the **Windsurf portal**, click **Enable Login with SAML**, then click **Save**.

    12. **Test the configuration**: Click **Test Login** to verify the SSO configuration works as expected.

    <Note>**Important**: Do not log out or close the Windsurf settings page until you've successfully tested the login. If the test fails, you may need to troubleshoot your configuration before proceeding.</Note>
  </Tab>

  <Tab title="Okta SSO">
    Windsurf Enterprise now supports sign in with Single Sign-On (SSO) via SAML. If your organization uses Microsoft Entra, Okta, Google Workspaces, or some other identity provider that supports SAML, you will be able to use SSO with Windsurf.

    <Note>Windsurf only supports SP-initiated SSO; IDP-initiated SSO is NOT currently supported.</Note>

    ### Configure IDP Application

    Click on Applications on the left sidebar, and then Create App Integration

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e3f879d2fa7faeba003aa04e2c5d3a4a" data-og-width="1248" width="1248" data-og-height="962" height="962" data-path="assets/auth/sso-okta1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=07c6dc86816c5d6cf956401bee450128 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2f2d86ae21cdef97580a0824ca01ffc8 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ec432c4e43c969491df691687b1c8719 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4f42e54a6f8de42f3fa17349df08394e 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9f1cb10571d1c2ea02bf30638a762e9c 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta1.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5c76f872b9163ec64637213aa646ba30 2500w" />
    </Frame>

    Select SAML 2.0 as the sign-in method

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=df39e8a15a879d8f2798a4284087c567" data-og-width="1600" width="1600" data-og-height="1023" height="1023" data-path="assets/auth/sso-okta2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=26a63721d0018efa7b8a4800e6f408bb 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c052bfa279c58dc361223b5582a62c80 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=00ed32012a519da9011059476f423aa6 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=eb3839e1a82fa9bc1467a456a38a993b 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c678d8128c2aa8d5b42eb1ff185d80a8 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta2.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9586e95f5e7e3cc3f167548bdcec2b48 2500w" />
    </Frame>

    Set the app name as Windsurf (or to any other name), and click Next

    Configure the SAML settings as

    * Single sign-on URL to [https://auth.windsurf.com/\_\_/auth/handler](https://auth.windsurf.com/__/auth/handler)
    * Audience URI (SP Entity ID) to [www.codeium.com](http://www.codeium.com)
    * NameID format to EmailAddress
    * Application username to Email

    Configure the attribute statements as following, and then click **Next**.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0903972c21dd13147a1adfe8791f1679" data-og-width="1398" width="1398" data-og-height="602" height="602" data-path="assets/auth/sso-okta3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f247cb5627519ba2052a1c66bcabac11 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8b0e97b79dbe969605c026e1d42918bf 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2c9e0db1830545f4605ec52128d0c13f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f21b1c853cd6e3fb6234eaba4936714a 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e207e6d97821d5b568bcb3175aaa877c 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5b9415f606224a480a8a21fd39d3c6b7 2500w" />
    </Frame>

    In the feedback section, select “This is an internal app that we have created”, and click **Finish**.

    ### Register Okta as a SAML provider

    You should be redirected to the Sign on tab under your custom SAML application. Now you’ll want to take the info in this page and fill it out in Windsurf’s SSO settings.

    * Open [https://windsurf.com/team/settings](https://windsurf.com/team/settings), and click on Configure SAML
    * Copy the text after ‘Issuer’ in Okta’s application page and paste it under Idp Entity ID
    * Copy the text after ‘Sign on URL’ in Okta’s application page and paste it under SSO URL
    * Download the Signing Certificate and paste it under X509 certificate
    * Check Enable Login with SAML and then click Save
    * Test the login with the Test Login button. You should see a success message:

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=574e091c869162bc41dc0aa36cd209fa" data-og-width="1046" width="1046" data-og-height="270" height="270" data-path="assets/auth/sso-okta4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c0de67fc05d02d94917d0eb38a93bfc7 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8a4532d29bde6a981fcfa56b16d2089c 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b166bddfbf60fd9be17010aedbc5f300 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4cc97e1ce5cbce8fe4b68f5736943608 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=10278811dec7a4ace3e27dafafe4dfdf 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=85583cef85521726dc3daa5307b6d733 2500w" />
    </Frame>

    At this point everything should have been configured, and can now add users to the new Windsurf Okta application.

    You should share your organization's custom Login Portal URL with your users and ask them to sign in via that link.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f3ccced59b0cbc7d0f0b1b6b39f1ee1c" data-og-width="988" width="988" data-og-height="312" height="312" data-path="assets/auth/sso-okta5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=02f37508edd5db6db866fd78e4a7acb9 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c12ca954c3031664fbcd2ca960b5383b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=75b02544b99c1e0a578234b57a07ea34 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cb11ec40d15a57198f780ae701029f44 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e51d3d2475655aef87f71b8b6105fb55 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta5.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=46ba7597ae1b616f37354006d6c5f907 2500w" />
    </Frame>

    Users who login to Windsurf via SSO will be auto-approved into the team.

    ### Caveats

    Note that Windsurf does not currently support IDP-initiated login flows.

    We also do not yet support OIDC.

    # Troubleshooting

    ### Login with SAML config failed: Firebase: Error (auth/operation-not-allowed)

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f65534799dfd8f941a68dc9fc72236d4" data-og-width="617" width="617" data-og-height="92" height="92" data-path="assets/auth/sso-okta6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4f6a8118ceb9a6511557fb3d5a89cfd8 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0cc4bcb6da5527e085f1e95e7565b2f6 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f1b542a1a5d5f18a6f07ce1fef0099f8 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=5b8cdc47c2f5c742e4bef33ba4eb459a 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=087c32afb9c9f9850d596b218be3f923 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta6.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=02c760fbfa8d931d9781b596ede9d08d 2500w" />
    </Frame>

    This points to your an invalid SSO ID, or your SSO URL being incorrect, make sure it is alphanumeric and has no extra spaces or invalid characters. Please go over the steps in the guide again and make sure you use the correct values.

    ### Login with SAML config failed: Firebase: SAML Response \<Issuer> mismatch. (auth/invalid-credential)

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=446c8ad9510b7dcc8e744c7b80862c29" data-og-width="752" width="752" data-og-height="117" height="117" data-path="assets/auth/sso-okta7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=efd56e3400b53ceb05c2a6f3f16dca44 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f41a12504545c5f78998cb6f152564c9 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=21967311e74ec09546b31c6f49dc2dd8 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2d07267015603fb0e6d4ccd0ba3c1e81 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=619c0eaf530646e7b6dd294d5cc2712a 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/sso-okta7.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a6217bfd37b259f63112cf22c3bb098b 2500w" />
    </Frame>

    This points to your IdP entity ID being invalid, please make sure you copy it correctly from the Okta portal, without any extra characters or spaces before or after the string.

    ### Failed to verify the signature in samlresponse

    This points to an incorrect value of your X509 certificate, please make sure you copy the correct key, and that it is formatted as:

    ```
    -----BEGIN CERTIFICATE-----
    value
    ------END CERTIFICATE------
    ```
  </Tab>

  <Tab title="Azure SCIM">
    Windsurf supports SCIM synchronization for users and groups with Microsoft Entra ID / Azure AD. It isn't necessary to setup SSO to use SCIM synchronization, but it is highly recommended.

    You'll need:

    * Admin access to Microsoft Entra ID / Azure AD
    * Admin access to Windsurf
    * An existing Windsurf Application on Entra ID (normally from your existing SSO application)

    ## Step 1: Navigate to the existing Windsurf Application

    Go to Microsoft Entra ID on Azure, click on Enterprise applications on the left sidebar, and then click on the existing Windsurf application in the list.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c2425d24cadc8997c694a4b8a950169a" data-og-width="1258" width="1258" data-og-height="664" height="664" data-path="assets/auth/scim-azure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d2a0a5702a29ce1264d133bb5d3545c1 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f91fd83f53b34bab00d17c64358ac511 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4fc4661fa56013064005d8d923a13547 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=196d0489a6a5fdf4200ab92e7f5835d5 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fb03af9c8d156c0f5c2331ab5289d588 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=58bcf8651ea7dc34d4f7e561b7c6ab34 2500w" />
    </Frame>

    ## Step 2: Setup SCIM provisioning

    Click on Get started under Provision User Accounts in the middle (step 3), and then click on Get started again.

    <Frame>
      <img src="https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=1e9c8417da7568dc587941955f6d0ace" data-og-width="2582" width="2582" data-og-height="1858" height="1858" data-path="assets/auth/scim-azure2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=280&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=ce2a379d150e9b6383eeb48e52c96a01 280w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=560&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=4f51c287262043282173de0e1efc538c 560w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=840&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=21c65050cb093e453197eecbd348d773 840w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=1100&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=074fcdd9f2ef2e03ad23580185dd48fe 1100w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=1650&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=324c2d04d90956f34ee3c9a8c11ef548 1650w, https://mintcdn.com/codeium/s3SYO8XdSvmrABvq/assets/auth/scim-azure2.png?w=2500&fit=max&auto=format&n=s3SYO8XdSvmrABvq&q=85&s=cd3257cf044253173943f57c3b89a5b6 2500w" />
    </Frame>

    Under the Provisioning setup page, select the following options.

    Provisioning Mode:  Automatic

    Admin Credentials > Tenant URL: [https://server.codeium.com/scim/v2](https://server.codeium.com/scim/v2)

    Leave the Azure provisioning page open, now go to the Windsurf web portal, and click on the profile icon  in the NavBar on the top of the page. Under Team Settings, select Service Key and click on Add Service Key. Enter any key name (such as 'Azure Provisioning Key') and click Create Service Key. Copy the output key, go back to the Azure page, paste it to Secret Token.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=80477c2c0d31631e38e217b22e9f42a3" data-og-width="1612" width="1612" data-og-height="1013" height="1013" data-path="assets/auth/scim-azure3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c547369cd10d19d77dbdb3586045c027 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e375425a3fe55cc5425f53e78b34f32f 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f15b3e3d387acd4ac3371b882595252a 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=49e6c3e224944aef0dfa88b13b401a74 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7dd27466493288c1d49a4327070f9f6f 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4f40f4c6d50b15c421ba344a2013a8cc 2500w" />
    </Frame>

    (What you should see after creating the key on Windsurf)

    On the Provisioning page, click on Test Connection and that should have verified the SCIM connection.

    Now above the Provisioning form click on Save.

    ## Step 3: Configure SCIM Provisioning

    After clicking on Save, a new option Mappings should have appeared in the Provisioning page. Expand Mappings, and click on Provision Microsoft Entra ID Users

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=276791b068bd34c2bcbe5321e95abfd6" data-og-width="666" width="666" data-og-height="438" height="438" data-path="assets/auth/scim-azure4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6e36e1d72d4db00f49e114fdcc4a25be 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c11c14a5020abebd95bb43a970d88584 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=190236b1aaadafb15d6b7b7bc320ade2 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9d153d92aeb12bfaf4bd7868270d0e17 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=00ff52c3a669e6dbb4f7346e0831fa23 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=640997349e4672552c5f07b170e81d22 2500w" />
    </Frame>

    Under attribute Mappings, delete all fields under displayName, leaving only the fields userName, active, and displayName.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ddb9440614a4bc04f7c561bbf64a2d5a" data-og-width="1260" width="1260" data-og-height="190" height="190" data-path="assets/auth/scim-azure5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=394d02238802b10210ff30262a7e669e 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=da13a8c0a933b23e30d66c8a25c7509b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fef036d0c788f16fe95ebca4f360388d 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b3a2f8ec1b2b3482ec86aa26e3dad431 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b4c4b2f43e28978d2c3acafee01a3ed0 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure5.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3bf1b1e6d6863d74fd5344f25ac07ecc 2500w" />
    </Frame>

    For active, now click on Edit. Under Expression, modify the field to

    ```
    NOT([IsSoftDeleted])
    ```

    Then click Ok.

    Your user attributes should look like

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2beab12c979d3272d522293080634811" data-og-width="2826" width="2826" data-og-height="490" height="490" data-path="assets/auth/scim-azure6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4a8ee3358e95d0cd9d50bd0d538564a7 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a80cc215059b3780ca14c6ba370a6586 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=60057214f7d952812b598371e6c978d3 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e9bcab8fd1017d0892bea2a169ac02e9 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=786f7e9bf633dcbd60d8059a61caf106 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure6.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d4e9a7b532a2f85244bcaa90572ba06a 2500w" />
    </Frame>

    In the Attribute Mapping page, click on Save on top, and navigate back to the Provisioning page.

    Now click on the same page, under Mappings click on Provision Microsoft Entra ID Groups. Now only click delete for externalId, and click Save on top. Navigate back to the Provisioning page.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=11e89ce7d057c455ea00e0f469351b61" data-og-width="1258" width="1258" data-og-height="203" height="203" data-path="assets/auth/scim-azure7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cd56976ca792e265e725662085b17a19 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=bd115677b029f5e93699ab0a03768382 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d4bded4bf9d8689909e28c61ad510ce0 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d57065b32eff89171254875a8df64498 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b6360f57f064b8ef7a10b63de8cfc7ef 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure7.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=51e4b607b0652154956ce119600415ba 2500w" />
    </Frame>

    On the Provisioning page at the bottom, there should also be a Provisioning Status toggle. Set that to On to enable SCIM syncing. Now every 40 minutes your users and groups for the Entra ID application will be synced to Windsurf.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1214073ce82bd85a1c2a57834005608f" data-og-width="686" width="686" data-og-height="306" height="306" data-path="assets/auth/scim-azure8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=53139148e9394f611f436dc2128bcc33 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a227c181354a371f3ae4aa13673a5c89 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=b9f85d836d1f06eb19a365d2f0cd9106 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6dd2cc814ee02f9bd402348e8c202d38 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=35af8b5f5183e3d4bfda09ec4d7b092b 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/scim-azure8.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d69d23c955420b31547dabb0b0950863 2500w" />
    </Frame>

    Click on Save to finish, you have now enabled user and group syncing for SCIM. Only users and groups assigned to the application will be synced to Windsurf. Note that removing users only disables them access to Windsurf (and stops them from taking up a seat) rather than deleting users due to Azure's SCIM design.
  </Tab>

  <Tab title="Okta SCIM">
    Windsurf supports SCIM synchronization for users and groups with Okta. It isn't necessary to setup SSO to use SCIM synchronization, but it is highly recommended.

    You'll need:

    * Admin access to Okta
    * Admin access to Windsurf
    * An existing Windsurf Application on Okta (normally from your existing SSO application)

    ## Step 1: Navigate to the existing Windsurf Application

    Go to Okta, click on Applications, Applications on the left sidebar, and then click on the existing Windsurf application in the application list.

    ## Step 2: Enable SCIM Provisioning

    Under the general tab, App Settings click on Edit on the top right. Then tick the 'Enable SCIM Provisioning' checkbox, then click Save. A new provisioning tab should have showed up on the top.

    Now go to provisioning, click Edit and input in the following fields:

    SCIM connector base URL: [https://server.codeium.com/scim/v2](https://server.codeium.com/scim/v2)

    Unique identifier field for users: email

    Supported provisioning actions: Push New Users, Push Profile Updates, Push Groups

    Authentication Mode: HTTP Header

    For HTTP Header - Authorization, you can generate the token from

    * [https://windsurf.com/team/settings](https://windsurf.com/team/settings) and go to the Other Settings and find Service Key Configuration
    * Click on Add Service Key, and give your key a name
    * Copy the API key, go back to Okta and paste it to HTTP Header - Authorization

    Click on Save after filling out Provisioning Integration.

    ## Step 3: Setup Provisioning

    Under the provisioning tab, on the left there should be two new tabs. Click on To App, and Edit Provisioning to App. Tick the checkbox for Create Users, Update User Attributes, and Deactivate Users, and click Save.

    After this step, all users assigned to the group will now be synced to Windsurf.

    ## Step 4: Setup Group Provisioning (Optional)

    In order to sync groups to Windsurf, you will have to specify which groups to push. Under the application, click on the Push Groups tab on top. Now click on + Push Groups -> Find Groups by name. Filter for the group you would like to add, make sure Push group memberships immediately is checked, and then click Save. The group will be created and group members will be synced to Windsurf. Groups can then be used to filter for group analytics in the analytics page.
  </Tab>

  <Tab title="SCIM API">
    This guide shows how to create and maintain groups in Windsurf with the SCIM API.

    There are reasons one may want to provision groups manually rather than with their Identity Provider (Azure/Okta). Companies may want Groups provisioned from a different internal source (HR website, Sourcecode Management Tool etc.) that Windsurf doesn't have access to, or companies may finer control to Groups than what their Idendity Provider provides. Groups can thus be created with an API via HTTP request instead. The following provides examples on the HTTP request via CURL.

    There are 5 main APIs here, Create Group, Add group members, Replace group members, Delete Group, and List Users in a Group.

    ### Create Group

    ```
    curl -k -X POST https://server.codeium.com/scim/v2/Groups -d '{
    "displayName": "<group name>",
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"]
    }' -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### Add Group Members

    ```
    curl -X PATCH https://server.codeium.com/scim/v2/Groups/<group name> -d '{"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations":[
    {
    "op": "add",
    "path":"members",
    "value": [{"value": "<email 1>"}, {"value": "<email 2>"}]
    }]}' -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### Replace Group Members

    ```
    curl -X PATCH https://server.codeium.com/scim/v2/Groups/<group name> -d '{"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    "Operations":[
    {
    "op": "replace",
    "path":"members",
    "value": [{"value": "<email 1>"}, {"value": "<email 2>"}]
    }]}' -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### Delete Group

    ```
    curl -X DELETE https://server.codeium.com/scim/v2/Groups/<group name> -H "Authorization: Bearer <api secret key>" -H "Content-Type: application/scim+json"
    ```

    ### List Group

    ```
    curl -X GET -H "Authorization: Bearer <api secret key>" "https://server.codeium.com/scim/v2/Groups"
    ```

    ### List Users in a Group

    ```
    curl -X GET -H "Authorization: Bearer <api secret key>" "https://server.codeium.com/scim/v2/Groups/<group_id>"
    ```

    You'll have to at least create the group first, and then replace group to create a group with members in them. You'll also need to URL encode the group names if your group name has a special character like space, so a Group name such as 'Engineering Group' will have to be 'Engineering%20Group' in the URL.

    Note that users need to be created in Windsurf (through SCIM or manually creating the account) before they can be added to a group.

    ## User APIs

    There are also APIs for users as well. The following are some of the common SCIM APIs that Windsurf supports.

    Disable a user (Enable by replacing false to true):

    ```
    curl -X PATCH \
      https://server.codeium.com/scim/v2/Users/<user api key> \
      -H 'Content-Type: application/scim+json' \
      -H 'Authorization: Bearer <api secret key>' \
      -d '{
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
        "Operations": [
          {
            "op": "replace",
            "path": "active",
            "value": false
          }
        ]
      }'
    ```

    Create a user:

    ```
    curl -X POST \
      https://server.codeium.com/scim/v2/Users \
      -H 'Content-Type: application/scim+json' \
      -H 'Authorization: Bearer <api secret key>' \
      -d '{
        "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
        "userName": "<email>",
        "displayName": "<full name>",
        "active": true,
    }' 
    ```

    Update name:

    ```
    curl -X PATCH \
      'https://<enterprise portal url>/_route/api_server/scim/v2/Users/<user api key>' \
        -H 'Authorization: Bearer <service key>' \
        -H 'Content-Type: application/scim+json' \
        -d '{
          "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
          "Operations": [
            {
              "op": "Replace",
              "path": "displayName",
              "value": "<new name>"
            }
          ]
       }'
    ```

    ## Creating Api Secret Key

    Go to [https://windsurf.com/team/settings](https://windsurf.com/team/settings). Under Service Key Configuration, click on Configure, then Add Service Key. Enter any key name (such as 'Azure Provisioning Key') and click Create Service Key. Copy the output key and save it, you can now use the key to authorize the above APIs.
  </Tab>

  <Tab title="Duo">
    ## Prerequisites

    This guide assumes that you have Duo configured and acts as your organizational IDP, or has external IDP configured.

    You will need administrator access to both Duo and Windsurf accounts.

    ## Configure Duo for Windsurf

    1. Navigate to Applications, and add a Generic SAML service provider

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7e598d7e9a9ee2c3884caa1c60ba68ff" data-og-width="2230" width="2230" data-og-height="920" height="920" data-path="assets/auth/duo-sso-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=3aec1b67ffcd908e98ff8fdc8efb9f13 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6fae9b15acbd20d00ba1342e29c03566 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=2a92b9bd222d601f17445724a5740c4d 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=07e9adea00e0cab9016ad608222894f5 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=78b9eeb4b38c111b8a305442ecf22038 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-1.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f3fae806d80ac44e2feb9be6d623c311 2500w" />
    </Frame>

    2. Navigate to SSO in Team Settings

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=df8dde8b5b66a27532a3f42cdd803a17" data-og-width="1676" width="1676" data-og-height="1444" height="1444" data-path="assets/auth/windsurf-sso-team-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=24e65a0584ca92c5092e7a8b39d29a85 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a1aaf95ae69ecadbb071f972cf209d9a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8e0faad235bc863532c0cf5e8260d51f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c1d83d71116443257b524c595132a21d 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ad30f5f9af3dde7f95666544e8a483ef 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fcf587e6ef653eff95139a4d550e3e08 2500w" />
    </Frame>

    3. When enabling SAML for the first time, you will be required to set up your SSO ID. **You will not be able to change it later.**

       It is advised to set this to your organization or team name with alphanumeric characters only.

    4. Copy the `Entity ID` value from the Duo portal and paste it into the `IdP Entity ID` field in the Windsurf portal.

    5. Copy the `Single Sign-On URL` value from the Duo portal and paste it into the `SSO URL` field in the Windsurf portal.

    6. Copy the certificate value from the Duo portal and paste it in the `X509 Certificate` field in the Windsurf portal

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a7594c846a32e958a1bacfc01c5d3ef3" data-og-width="1536" width="1536" data-og-height="290" height="290" data-path="assets/auth/duo-sso-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=953a07d45101a639db53f6d22667c2a0 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1fbc8e990bebcbad0cd70f9bce288a8b 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=769ba894b06157867cba16e6c7c9858b 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0e65532cda4e2039dfe07c02fd55aa52 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=9095538c85e97051654d911b3bb10e91 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f907b2efbe7eaabdaa8aa8c6fb350d86 2500w" />
    </Frame>

    7. Copy the `SP Identity ID` value from the Windsurf portal and paste it into the `Entity ID` field in the Duo portal.

    8. Copy the `Callback URL (Assertion Consumer Service URL)` from the Windsurf portal and paste it into the `Assertion Consumer Service (ACS) URL` field in the Duo portal.

    9. In the Duo portal, configure the attribute statements as following:

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=bb3b514b94a6b0ebba19aa492c8be4a2" data-og-width="1676" width="1676" data-og-height="290" height="290" data-path="assets/auth/duo-sso-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a3de0ba0a3a188f34f178c200209cc17 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=88374d6e4f03ce1e45cb3094fe3e98e8 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=d94638ec8d0a22bfa7ec00eb6514ec58 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f1c7e2ae138409c19a56dd12287fdaec 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7cfe010d8214ae7e7b655b5b6efba472 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/duo-sso-4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=769ae9ad721e322e67f6d84bf139a33d 2500w" />
    </Frame>

    10. Enable the SAML login in the Windsurf portal so you can test it.

    **NOTE: DO NOT LOGOUT OR CLOSE THE WINDOW AT THIS POINT.**

    If you get an error or it times out, troubleshoot your settings, otherwise you have to disable your SAML Settings in the Windsurf portal.

    **If you logout or close the window without confirming a successful test - you may get locked out.**

    11. Once your test was successfully completed, you may logout. You can now use SSO sign in when browsing to your team/organization page with the SSO ID you have configured in step 3.

    [https://www.codeium.com/yourssoid/login](https://www.codeium.com/yourssoid/login)
  </Tab>

  <Tab title="PingID">
    ## Prerequisites

    This guide assumes that you have PingID configured and acts as your organizational IDP, or has external IDP configured.

    You will need administrator access to both PingID and Windsurf accounts.

    ## Configure PingID for Windsurf

    1. Navigate to Applications and add Windsurf as a SAML Application

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=f86f6145e0eac599178ca9d9ee66b776" data-og-width="2258" width="2258" data-og-height="1068" height="1068" data-path="assets/auth/pingid-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=0ad46a1b2741392e7b9317cb469e55ea 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=894534973d6592c29d157db78a542b26 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=cea5d47e23bcff6ef6811358f893533f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1e2f9e94729c777800b7b9e4dfe32082 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6b7ab758d275aa2b2e63a9c4e01bea62 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-1.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=dfb01b08c5fdd2ebe1d9e80e5052426b 2500w" />
    </Frame>

    2. Navigate to SSO in Team Settings

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=df8dde8b5b66a27532a3f42cdd803a17" data-og-width="1676" width="1676" data-og-height="1444" height="1444" data-path="assets/auth/windsurf-sso-team-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=24e65a0584ca92c5092e7a8b39d29a85 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=a1aaf95ae69ecadbb071f972cf209d9a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=8e0faad235bc863532c0cf5e8260d51f 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c1d83d71116443257b524c595132a21d 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=ad30f5f9af3dde7f95666544e8a483ef 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/windsurf-sso-team-settings.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fcf587e6ef653eff95139a4d550e3e08 2500w" />
    </Frame>

    3. When enabling SAML for the first time, you will be required to set up your SSO ID. **You will not be able to change it later.**

    It is advised to set this to your organization or team name with alphanumeric characters only.

    4. In PingID - choose to manually enter the configuration and fill out the fields with the following values:

    * ACS URLs - this is the `Callback URL (Assertion Consumer Service URL)` from the Windsurf portal.
    * Entity ID - this is the `SP Entity ID` from the Windsurf portal.

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=e33dc0b9d021309da0fcdb2ac4f08bbb" data-og-width="974" width="974" data-og-height="672" height="672" data-path="assets/auth/pingid-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=085f011d0ddf369d9b05502ccbfbb5dc 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=160eebad525ebc56527d0c9e9945492a 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=fccab270df675b3608a5e72afdcda1bc 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=dcab45be60955341f5e47e1746fd36f4 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=6819f76a0f703860f8f53fc486bf696d 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-3.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4d1dde99a6c5a62b6c1798f1c694e220 2500w" />
    </Frame>

    5. Copy the `Issuer ID` from PingID to the `IdP Entity ID` value in the Windsurf portal.

    6. Copy the `Single Signon Service` value from PingID to the `SSO URL` value in the Windsurf portal.

    7. Download the Signing Certificate from PingID as X509 PEM (.crt), open the file and copy its contents to the `X509 Certificate` value in the Windsurf portal.

    **Note**: make sure you have the fill begin and end lines with 5 dashes (-) and no other characters are copied!

    8. In attribute mappings, make sure to map:

    * `saml_subject` - Email Address
    * `firstName` - Given Name
    * `lastName` - Family Name

    <Frame>
      <img src="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4ff17f07bfb897072fb68e212ee2ac12" data-og-width="1398" width="1398" data-og-height="780" height="780" data-path="assets/auth/pingid-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=280&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=7af2eb21b83c86fa66ab0a93b744a81a 280w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=560&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=c817c9e4a5abbe3827baf40050108679 560w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=840&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=1f4f584e1f6586dadb0632457eb840f1 840w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=1100&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=062bae9cd58477962da4f51fb5590bc4 1100w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=1650&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=efa1fb0cc4d775c8695521195d31949e 1650w, https://mintcdn.com/codeium/DnGnXhZxl1qb2EWt/assets/auth/pingid-4.png?w=2500&fit=max&auto=format&n=DnGnXhZxl1qb2EWt&q=85&s=4fe0ba0d6cd6b3eb6796557696e9a08d 2500w" />
    </Frame>

    9. Add/edit any other policies and access as required by your setup/organization

    10. Enable the SAML login in the Windsurf portal so you can test it.

    **NOTE: DO NOT LOGOUT OR CLOSE THE WINDOW AT THIS POINT.**

    If you get an error or it times out, troubleshoot your settings, otherwise you have to disable your SAML Settings in the Windsurf portal.

    **If you logout or close the window without confirming a successful test - you may get locked out.**

    11. Once your test was successfully completed, you may logout. You can now use SSO sign in when browsing to your team/organization page with the SSO ID you have configured in step 3.

    [https://www.codeium.com/yourssoid/login](https://www.codeium.com/yourssoid/login)
  </Tab>
</Tabs>




---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-getting-started-with-teams-and-enterprise.md)