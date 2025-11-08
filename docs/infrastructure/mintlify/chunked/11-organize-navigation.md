**Navigation:** [← Previous](./10-create-agent-job.md) | [Index](./index.md) | Next →

# Organize navigation
Source: https://mintlify.com/docs/guides/navigation

Guidelines for designing information architecture that works for your users

<Tip>
  This page explains why and how to organize your documentation in a way that makes sense for your users.
</Tip>


## Why is navigation important?

Navigation might seem unimportant because experienced users looking for specific answers typically navigate directly to pages via a search engine or your documentation site's search bar.

But the information architecture of your documentation helps people build a mental model for how to think about your product, and provides structure for people and AI tools that use your documentation. Well designed navigation helps people quickly grasp your product and succeed when using your documentation.


## Map the foundation with stakeholders

Align with key stakeholders like your founders, product managers, or engineering leads on how your product works, what's most important, and how users should interact with it.

Example questions to ask:

* What's the simplest way to explain how the product works?
* What are the product's core building blocks?
* How do users typically adopt the product? Where do people most often get stuck?
* How does the product's architecture influence how people use it?
* What are the most important integrations or dependencies?
* What is changing or evolving in the product?
* If the product was broken into different layers, what would they be? Would it be by tasks that people perform or by features that people use?


## Validate your assumptions

Once you've established a structure, you need to validate whether it actually works for real users. The way people navigate your documentation often reveals gaps in your information architecture that internal teams might overlook.

### Track real user journeys

Use tools like session replays (for example, [FullStory](https://www.fullstory.com), [Hotjar](https://www.hotjar.com)) or analytics (for example, [Mixpanel](https://mixpanel.com)) to study how users move through your docs. Pay attention to:

* **Entry points:** Where do users start their journey? Are they coming from search, a support ticket, or directly from your product?
* **Navigation patterns:** Do they follow the expected navigation structure, or do they take unexpected detours?
* **Friction points:** Where do users pause, loop back, or abandon their session? These could indicate unclear organization or missing content.
* **Search behavior:** Are users searching for terms that don't exist in your documentation? This might highlight gaps in your content or misalignment in terminology.

### Test with real users

Analytics help surface trends, but direct conversations provide deeper insights.

Get on research calls where customers attempt to find answers to specific questions. Ask them to narrate their thought process as they navigate.

New hires are also a great proxy for users since they don't have as much prior context as tenured members of your team. Before they get too familiar with your product from the inside, ask them to complete a task using only the documentation.

Have them outline in detail how they approached the task. Where they clicked first, how they interpreted section names, and where they got stuck. Their instincts can reveal whether your docs are intuitive or if they assume too much knowledge.


## Identify common challenges

Based on your observations, look for these common navigation problems:

* **Overloaded categories:** Too many top-level sections can overwhelm users. Consider grouping related topics together.
* **Hidden essential content:** Don't bury critical information. Prioritize frequently accessed content.
* **Unclear section names:** If users hesitate before clicking, your labels might not be intuitive. Align terminology with how your audience naturally thinks.

Try to design an elegant and functional information architecture, but remember, it's hard to make documentation that works for absolutely everyone. Consider the majority of your users and what will help them succeed.


## Iterate over time

Above all, stay flexible. Your navigation should evolve with your product and user needs. You don't have to be right on the first try.



# SEO
Source: https://mintlify.com/docs/guides/seo

How to improve SEO for your documentation site

<Tip>
  This page explains fundamental strategies to optimize your documentation SEO.
</Tip>


## Content basics

Make your writing and structure easy for search engines to scan.

* **Headings and subheadings:** Use sequential, meaningful headers to structure your content. Each page has an H1 created from the `title:` property in the frontmatter.
* **Short paragraphs and bullet points:** Break down large chunks of text into easily readable sections. Use bullet points and numbered lists where appropriate.
* **Internal linking:** Link to related content using descriptive anchor text. For example, "Learn more about rate limiting" instead of "Click here."


## Technical SEO basics

Once your content is optimized, ensure your documentation performs well from a technical standpoint.

These basic technical SEO practices help make your docs more discoverable:

* **Meta tags and descriptions:** Craft SEO-friendly titles (50-60 characters) and descriptions (150-160 characters) for each page. Most [meta tags](/optimize/seo) are automatically generated.
* **Alt text for images:** Provide descriptive alt text for images with relevant keywords. For example, "OAuth 2.0 API authentication flow" instead of just "diagram". This enhances SEO and accessibility.
* **Sitemaps:** Ensure your sitemap is up-to-date. Mintlify automatically generates a sitemap. However, you can manually create a sitemap if you prefer a custom format. Once created, search engines index site maps over time, but you can submit your sitemap directly to Google Search Console to speed up the process.


## Page performance

Use tools like [Google PageSpeed Insights](https://pagespeed.web.dev) to identify areas for technical SEO improvement.

Examples of more advanced optimizations:

* **Optimize media for speed:** Compress images using formats like WebP or AVIF and ensure your pages load quickly (ideally under 3 seconds).
* **Structured data (schema markup):** Add schema markup (like HowTo, FAQ) to your pages to help search engines better understand and rank your content.


## Keyword research

To increase organic traffic, invest time into understanding which keywords help users land on your documentation.

* **Keyword research:** Use free tools like [Google Keyword Planner](https://ads.google.com/intl/en_us/home/tools/keyword-planner/) or [Keywords Everywhere](https://keywordseverywhere.com) to identify common phrases or long-tail keywords.
* **Integrate keywords naturally:** Add keywords naturally into headings, subheadings, and throughout the body text. Don't overstuff keywords. Your documentation should be written for your users, not search engines.



# Style and tone
Source: https://mintlify.com/docs/guides/style-and-tone

Principles for writing effective technical documentation

<Tip>
  This page explains stylistic choices, common mistakes, and implementation tips for writing technical documentation.
</Tip>


## Writing principles

* **Be concise.** People are reading documentation to achieve a goal. Get to the point quickly.
* **Clarity over cleverness.** Be simple, direct, and avoid jargon or complex sentence structure.
* **Use active voice.** Instead of saying "A configuration file should be created," use "Create a configuration file."
* **Be skimmable.** Use headlines to orient readers. Break up text-heavy paragraphs. Use bullet points and lists to make it easier to scan.
* **Write in second person.** Referring to your reader makes it easier to follow instructions and makes the documentation feel more personal.


## Common writing mistakes

* **Spelling and grammar mistakes.** Even a few spelling and grammar mistakes in your documentation make it less credible and harder to read.
* **Inconsistent terminology.** Calling something an “API key” in one paragraph then “API token” in the next makes it difficult for users to follow along.
* **Product-centric terminology.** Your users don't have the full context of your product. Use language that users are familiar with.
* **Colloquialisms.** Especially for localization, colloquialisms hurt clarity.


## Tips for enforcing style

Leverage existing style guides to standardize your documentation:

* [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
* [Splunk Style Guide](https://docs.splunk.com/Documentation/StyleGuide/current/StyleGuide/Howtouse)
* [Google Developer Documentation Style Guide](https://developers.google.com/style)

When you know which writing principles you want to implement, automate as much as you can. You can use  [CI checks](/deploy/ci) or linters like [Vale](https://vale.sh).



# Understand your audience
Source: https://mintlify.com/docs/guides/understand-your-audience

Keep user goals at the center of your writing

<Tip>
  This page explains how to identify your audience, conduct user research, and write with their needs in mind.
</Tip>


## Identify your primary audience

Writing for multiple audiences leads to compromises that satisfy no one. Each piece of content should be focused on one specific user persona.

Your audience might be:

* Technical decision makers evaluating your product who want to understand higher level details like architecture overviews.
* New users who want to start using your product for the first time.
* Developers responsible for integrating your product who need instructions for a specific task.

Before writing any page, ask what is your reader trying to accomplish and what is their prior knowledge?


## User research is key

Your team should agree on who your primary audience is, but don't rely on intuition alone. The best insights come from talking directly to users. There can be a disconnect between how we think about our own products and how people actually use them.

Talk to users to understand:

* How do they describe what your product does?
* Do they use any unexpected words or names to describe your product?
* What do they wish they had more knowledge of?
* What is explicitly missing from your documentation?

Talking to users directly helps ground your writing from their perspective so that you write documentation that is helpful to them and gets them closer to their goals.


## Tips and tricks for understanding your audience

1. **Get embedded with support.** You'll see the pain points that incomplete documentation causes. Ask your support team how people think about the product and what are the most common problems people encounter.
2. **Incorporate feedback mechanisms.** Whether it's thumbs up/down or plain text fields, give users the opportunity to provide feedback as they read your documentation.
3. **Use analytics to guide you.** Review feedback and insights to understand where users are struggling and where they are successful. Make updates to the documentation that people struggle with or is most connected to the key tasks for your product.

There will always be edge cases that are not covered by your documentation. Prioritize the most impactful pages to help the most people. Too much content becomes difficult to navigate and maintain, so trying to document every possible scenario can be counterproductive.



# Windsurf
Source: https://mintlify.com/docs/guides/windsurf

Configure Windsurf to be your writing assistant

Transform Windsurf into a documentation expert that understands your style guide, components, and project context through workspace rules and memories.


## Using Windsurf with Mintlify

Windsurf's Cascade AI assistant can be tuned to write documentation according to your standards using Mintlify components. Workspace rules and memories provide persistent context about your project, ensuring more consistent suggestions from Cascade.

* **Workspace rules** are stored in your documentation repository and shared with your team.
* **Memories** provide individual context that builds up over time.

We recommend setting up workspace rules for shared documentation standards. You can develop memories as you work, but since they are not shared, they will not be consistent across team members.

Create workspace rules in the `.windsurf/rules` directory of your docs repo. See [Memories & Rules](https://docs.windsurf.com/windsurf/cascade/memories) in the Windsurf documentation for more information.


## Example workspace rule

This rule provides Cascade with context about Mintlify components and general technical writing best practices.

You can use this example rule as-is or customize it for your documentation:

* **Writing standards**: Update language guidelines to match your style guide.
* **Component patterns**: Add project-specific components or modify existing examples.
* **Code examples**: Replace generic examples with real API calls and responses for your product.
* **Style and tone preferences**: Adjust terminology, formatting, and other rules.

Save your rule as a `.md` file in the `.windsurf/rules` directory of your docs repo.

````mdx  theme={null}

# Mintlify technical writing rule


## Project context

- This is a documentation project on the Mintlify platform
- We use MDX files with YAML frontmatter  
- Navigation is configured in `docs.json`
- We follow technical writing best practices


## Writing standards

- Use second person ("you") for instructions
- Write in active voice and present tense
- Start procedures with prerequisites
- Include expected outcomes for major steps
- Use descriptive, keyword-rich headings
- Keep sentences concise but informative


## Required page structure

Every page must start with frontmatter:

```yaml
---
title: "Clear, specific title"
description: "Concise description for SEO and navigation"
---
```


## Mintlify components

### docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation

### Callouts

- `<Note>` for helpful supplementary information
- `<Warning>` for important cautions and breaking changes
- `<Tip>` for best practices and expert advice  
- `<Info>` for neutral contextual information
- `<Check>` for success confirmations

### Code examples

- When appropriate, include complete, runnable examples
- Use `<CodeGroup>` for multiple language examples
- Specify language tags on all code blocks
- Include realistic data, not placeholders
- Use `<RequestExample>` and `<ResponseExample>` for API docs

### Procedures

- Use `<Steps>` component for sequential instructions
- Include verification steps with `<Check>` components when relevant
- Break complex procedures into smaller steps

### Content organization

- Use `<Tabs>` for platform-specific content
- Use `<Accordion>` for progressive disclosure
- Use `<Card>` and `<CardGroup>` for highlighting content
- Wrap images in `<Frame>` components with descriptive alt text


## API documentation requirements

- Document all parameters with `<ParamField>` 
- Show response structure with `<ResponseField>`
- Include both success and error examples
- Use `<Expandable>` for nested object properties
- Always include authentication examples


## Quality standards

- Test all code examples before publishing
- Use relative paths for internal links
- Include alt text for all images
- Ensure proper heading hierarchy (start with h2)
- Check existing patterns for consistency
````


## Working with Cascade

Once your rules are set up, you can use Cascade to assist with various documentation tasks. See [Cascade](https://docs.windsurf.com/windsurf/cascade) in the Windsurf documentation for more information.

### Example prompts

**Writing new content**:

```text wrap theme={null}
Create a new page explaining how to authenticate with our API. Include code examples in JavaScript, Python, and cURL.
```

**Improving existing content**:

```text wrap theme={null}
Review this page and suggest improvements for clarity and component usage. Focus on making the steps easier to follow.
```

**Creating code examples**:

```text wrap theme={null}
Generate a complete code example showing error handling for this API endpoint. Use realistic data and include expected responses.
```

**Maintaining consistency**:

```text wrap theme={null}
Check if this new page follows our documentation standards and suggest any needed changes.
```



# Osano
Source: https://mintlify.com/docs/integrations/privacy/osano



Add the following to your `docs.json` file to add the [Osano](https://www.osano.com/) cookie consent manager.

<CodeGroup>
  ```json Integration options in docs.json theme={null}
  "integrations": {
      "osano": "SOURCE"
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "osano": "https://cmp.osano.com/2sUB2dqwqdkks/8dqwd-dwd86£-4a9b/osano.js"
  }
  ```
</CodeGroup>

The `SOURCE` can be found as the `src` value in the code snippet generated by Osano. It always starts with `https://cmp.osano.com/`.

```html Code snippet from Osano theme={null}
<script src="https://cmp.osano.com/placeholder/placeholder/osano.js"/>
```


## Troubleshooting

<Accordion title="Pages not loading with Strict compliance mode">
  If your documentation pages aren't loading properly when using Osano's **Strict** compliance mode, you'll need to whitelist Mintlify's domain to allow images and other assets to load.

  <Steps>
    <Step title="Navigate to Managed Rules">
      In your Osano dashboard, go to **Scripts** → **Managed Rules**.
    </Step>

    <Step title="Add Mintlify domain">
      Add `.mintlify.app/` as a managed rule.

      <Frame>
        <img src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=66a71862fce8aa19564959a171927597" alt="Osano managed rule" data-og-width="1980" width="1980" data-og-height="738" height="738" data-path="images/integrations/osano-managed-rule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9e6e4322d56a45cad03b50c4d4aa9d83 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2478ca64cdea2c69570abcf155158b55 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ec5d708605279fd0dbc8db758b01be0e 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2e5c86284c552c01dafc6419ff2fbcd7 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=059d9d98c9e7c5b3159e36a04dd5a67b 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/integrations/osano-managed-rule.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1f7d274c25d4598cf744973e16e86a58 2500w" />
      </Frame>

      <Info>
        This ensures that all Mintlify-served assets (including images, stylesheets, and other documentation resources) are treated as essential and will load even when Osano blocks uncategorized third-party content.
      </Info>
    </Step>
  </Steps>
</Accordion>




---
**Navigation:** [← Previous](./10-create-agent-job.md) | [Index](./index.md) | Next →
