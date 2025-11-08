**Navigation:** [← Previous](./09-pdf-support.md) | [Index](./index.md) | [Next →](./11-prefill-claudes-response-for-greater-output-contro.md)

---

# Let Claude think (chain of thought prompting) to increase performance
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

When faced with complex tasks like research, analysis, or problem-solving, giving Claude space to think can dramatically improve its performance. This technique, known as chain of thought (CoT) prompting, encourages Claude to break down problems step-by-step, leading to more accurate and nuanced outputs.

## Before implementing CoT

### Why let Claude think?

* **Accuracy:** Stepping through problems reduces errors, especially in math, logic, analysis, or generally complex tasks.
* **Coherence:** Structured thinking leads to more cohesive, well-organized responses.
* **Debugging:** Seeing Claude's thought process helps you pinpoint where prompts may be unclear.

### Why not let Claude think?

* Increased output length may impact latency.
* Not all tasks require in-depth thinking. Use CoT judiciously to ensure the right balance of performance and latency.

<Tip>Use CoT for tasks that a human would need to think through, like complex math, multi-step analysis, writing complex documents, or decisions with many factors.</Tip>

***

## How to prompt for thinking

The chain of thought techniques below are **ordered from least to most complex**. Less complex methods take up less space in the context window, but are also generally less powerful.

<Tip>**CoT tip**: Always have Claude output its thinking. Without outputting its thought process, no thinking occurs!</Tip>

* **Basic prompt**: Include "Think step-by-step" in your prompt.
  * Lacks guidance on *how* to think (which is especially not ideal if a task is very specific to your app, use case, or organization)
  <Accordion title="Example: Writing donor emails (basic CoT)">
    | Role | Content                                                                                                                                                                                                                                                                                                                            |
    | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User | Draft personalized emails to donors asking for contributions to this year's Care for Kids program.<br /><br />Program information:<br />\<program>\{\{PROGRAM\_DETAILS}}<br />\</program><br /><br />Donor information:<br />\<donor>\{\{DONOR\_DETAILS}}<br />\</donor><br /><br />Think step-by-step before you write the email. |
  </Accordion>
* **Guided prompt**: Outline specific steps for Claude to follow in its thinking process.
  * Lacks structuring to make it easy to strip out and separate the answer from the thinking.
  <Accordion title="Example: Writing donor emails (guided CoT)">
    | Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User | Draft personalized emails to donors asking for contributions to this year's Care for Kids program.<br /><br />Program information:<br />\<program>\{\{PROGRAM\_DETAILS}}<br />\</program><br /><br />Donor information:<br />\<donor>\{\{DONOR\_DETAILS}}<br />\</donor><br /><br />Think before you write the email. First, think through what messaging might appeal to this donor given their donation history and which campaigns they've supported in the past. Then, think through what aspects of the Care for Kids program would appeal to them, given their history. Finally, write the personalized donor email using your analysis. |
  </Accordion>
* **Structured prompt**: Use XML tags like `<thinking>` and `<answer>` to separate reasoning from the final answer.
  <Accordion title="Example: Writing donor emails (structured guided CoT)">
    | Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | User | Draft personalized emails to donors asking for contributions to this year's Care for Kids program.<br /><br />Program information:<br />\<program>\{\{PROGRAM\_DETAILS}}<br />\</program><br /><br />Donor information:<br />\<donor>\{\{DONOR\_DETAILS}}<br />\</donor><br /><br />Think before you write the email in \<thinking> tags. First, think through what messaging might appeal to this donor given their donation history and which campaigns they've supported in the past. Then, think through what aspects of the Care for Kids program would appeal to them, given their history. Finally, write the personalized donor email in \<email> tags, using your analysis. |
  </Accordion>

### Examples

<AccordionGroup>
  <Accordion title="Example: Financial analysis without thinking">
    Without step-by-step thinking, Claude gives a recommendation that seems reasonable but lacks depth. It doesn't quantify the potential outcomes or consider historical market performance, which are crucial for making an informed decision.

    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | You're a financial advisor. A client wants to invest \$10,000. They can choose between two options: A) A stock that historically returns 12% annually but is volatile, or B) A bond that guarantees 6% annually. The client needs the money in 5 years for a down payment on a house. Which option do you recommend?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | Assistant | Based on the information provided, I would recommend option B, the bond that guarantees a 6% annual return. Here's why:<br /><br />1. Certainty: The bond offers a guaranteed 6% annual return, which provides certainty in financial planning. This is crucial when the client has a specific financial goal (down payment) with a fixed timeline (5 years).<br />2. Risk aversion: Since the client needs this money for an important life event (buying a house), they likely have a low risk tolerance. The volatility of the stock market could jeopardize their plans if there's a downturn close to when they need the funds.<br />3. Time horizon: With only 5 years, there's less time to recover from potential stock market downturns. Longer investment horizons (10+ years) are generally better suited for weathering stock market volatility.<br /><br />While the stock's historical 12% return is attractive, past performance doesn't guarantee future results. The guaranteed 6% from the bond ensures the client will have the funds they need when it's time to make the down payment. |
  </Accordion>

  <Accordion title="Example: Financial analysis with thinking">
    With step-by-step thinking, the advisor provides a much richer analysis. It calculates exact figures for both scenarios, considers historical market volatility, and deeply analyzes the client's risk tolerance. This thorough reasoning leads to a more confident and justifiable recommendation.

    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | You're a financial advisor. A client wants to invest \$10,000. They can choose between two options: A) A stock that historically returns 12% annually but is volatile, or B) A bond that guarantees 6% annually. The client needs the money in 5 years for a down payment on a house. Which option do you recommend? Think step-by-step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | Assistant | To determine the best investment option for our client, I'll consider several factors step-by-step:<br /><br />\<thinking><br />1. Understand the client's goal and timeline:<br />   - Goal: Down payment for a house<br />   - Timeline: 5 years<br />   - Implication: This is a short-term, high-priority financial goal. The client likely cannot afford significant risk or volatility.<br /><br />2. Analyze Option A (Stock):<br />   - Pro: Higher historical return (12% annually)<br />   - Con: Volatile (implying potential for significant gains or losses)<br />   - Calculate potential 5-year return:<br />     - Best case (12% annually): \$10,000 \* (1.12)^5 ≈ \$17,623.42<br />     - Worst case (market crash): Could lose a substantial portion, e.g., 50% crash = \$5,000<br /><br />3. Analyze Option B (Bond):<br />   - Pro: Guaranteed return (6% annually)<br />   - Con: Lower return compared to historical stock performance<br />   - Calculate 5-year return:<br />     - Guaranteed: \$10,000 \* (1.06)^5 ≈ \$13,382.25<br /><br />4. Consider risk tolerance:<br />   - Goal is a house down payment (essential, not discretionary)<br />   - Short timeline (5 years) limits ability to recover from market downturns<br />   - Conclusion: Client likely has low risk tolerance<br /><br />5. Historical perspective:<br />   - Stock's 12% is historical, not guaranteed<br />   - In 5-year periods, stock market can vary wildly:<br />     - 2003-2007 (pre-financial crisis): S\&P 500 up \~82%<br />     - 2007-2011 (during crisis): S\&P 500 down \~2%<br />   - Conclusion: Past performance doesn't guarantee future results, especially short-term<br /><br />6. Final analysis:<br />   - Option A (Stock): Higher potential return but unacceptable risk of not meeting the down payment goal<br />   - Option B (Bond): Guaranteed to meet \~80% of best-case stock scenario, 100% certainty of having funds<br />\</thinking><br /><br />\<answer><br />I recommend Option B, the bond with a guaranteed 6% annual return. While the stock's historical 12% return is tempting, the bond ensures you'll have \$13,382.25 in 5 years for your house down payment. Given the importance and short timeline of your goal, the stock's volatility poses an unacceptable risk. The bond provides certainty, which is invaluable for such a crucial financial milestone.<br />\</answer> |
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


# Chain complex prompts for stronger performance
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-prompts



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

When working with complex tasks, Claude can sometimes drop the ball if you try to handle everything in a single prompt. Chain of thought (CoT) prompting is great, but what if your task has multiple distinct steps that each require in-depth thought?

Enter prompt chaining: breaking down complex tasks into smaller, manageable subtasks.

## Why chain prompts?

1. **Accuracy**: Each subtask gets Claude's full attention, reducing errors.
2. **Clarity**: Simpler subtasks mean clearer instructions and outputs.
3. **Traceability**: Easily pinpoint and fix issues in your prompt chain.

***

## When to chain prompts

Use prompt chaining for multi-step tasks like research synthesis, document analysis, or iterative content creation. When a task involves multiple transformations, citations, or instructions, chaining prevents Claude from dropping or mishandling steps.

**Remember:** Each link in the chain gets Claude's full attention!

<Tip>**Debugging tip**: If Claude misses a step or performs poorly, isolate that step in its own prompt. This lets you fine-tune problematic steps without redoing the entire task.</Tip>

***

## How to chain prompts

1. **Identify subtasks**: Break your task into distinct, sequential steps.
2. **Structure with XML for clear handoffs**: Use XML tags to pass outputs between prompts.
3. **Have a single-task goal**: Each subtask should have a single, clear objective.
4. **Iterate**: Refine subtasks based on Claude's performance.

### Example chained workflows:

* **Multi-step analysis**: See the legal and business examples below.
* **Content creation pipelines**: Research → Outline → Draft → Edit → Format.
* **Data processing**: Extract → Transform → Analyze → Visualize.
* **Decision-making**: Gather info → List options → Analyze each → Recommend.
* **Verification loops**: Generate content → Review → Refine → Re-review.

<Tip>**Optimization tip**: For tasks with independent subtasks (like analyzing multiple docs), create separate prompts and run them in parallel for speed.</Tip>

### Advanced: Self-correction chains

You can chain prompts to have Claude review its own work! This catches errors and refines outputs, especially for high-stakes tasks.

<AccordionGroup>
  <Accordion title="Example: Self-correcting research summary">
    #### Prompt 1

    | Role                         | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | User                         | Summarize this medical research paper.<br /><br />\<paper>\{\{RESEARCH\_PAPER}}\</paper><br /><br />Focus on methodology, findings, and clinical implications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | Assistant<br />\{\{SUMMARY}} | Methodology: Double-blind RCT with 500 Type 2 diabetes patients. Group A (n=250) received novel GLP-1/GIP dual agonist; Group B (n=250) received standard GLP-1 agonist. 24-week trial, primary endpoint: HbA1c reduction.<br /><br />Findings:<br />- Group A: 1.8% mean HbA1c reduction<br />- Group B: 1.1% mean HbA1c reduction<br />- 68% of Group A vs. 52% of Group B achieved HbA1c \<7%<br />- Group A: 5.2kg mean weight loss<br />- Group B: 3.1kg mean weight loss<br /><br />Safety: Similar adverse event profiles, no serious events attributed to treatment.<br /><br />Clinical Implications: Dual agonist shows superior glycemic control and weight loss compared to standard therapy. Could be a game-changer, especially for obese diabetics. |

    #### Prompt 2

    | Role                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User                          | Your task is to provide feedback on a research paper summary. Here is a summary of a medical research paper:<br />\<summary><br />\{\{SUMMARY}}<br />\</summary><br /><br />Here is the research paper:<br />\<paper><br />\{\{RESEARCH\_PAPER}}<br />\</paper><br /><br />Review this summary for accuracy, clarity, and completeness on a graded A-F scale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | Assistant<br />\{\{FEEDBACK}} | 1. Accuracy: A<br />   - Correctly reported key stats: HbA1c reductions, weight loss.<br />   - Accurately noted safety profile and lack of serious adverse events.<br />   - Assertion of "game-changer" is justified by significantly better outcomes.<br /><br />2. Clarity: A-<br />   - Concise and well-structured with clear sections.<br />   - Good use of comparative language (e.g., "up 3% from Q1") for context.<br />   - Minor issue: Acronyms like "RCT," "GLP-1," and "GIP" not defined. Consider spelling out first use.<br /><br />3. Completeness: B+<br />   - Covers all requested areas: methodology, findings, clinical implications.<br />   - Missing: Baseline characteristics of groups (were they well-matched?).<br />   - Missing: Any secondary endpoints (e.g., blood pressure, lipids).<br />   - Consider: Long-term implications or need for further research.<br /><br />Overall, the summary is accurate and clear, providing key insights for a quick grasp of the study. To elevate to A+, define acronyms, mention group baseline stats, note any secondary outcomes, and briefly touch on the need for long-term studies. |

    #### Prompt 3

    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | Your task is to improve a paper summary given feedback. Here is the first draft of a medical research paper:<br />\<summary><br />\{\{SUMMARY}}<br />\</summary><br /><br />Here is the research paper:<br />\<paper><br />\{\{RESEARCH\_PAPER}}<br />\</paper><br /><br />Here is the feedback:<br />\<feedback><br />\{\{FEEDBACK}}<br />\</feedback><br /><br />Update the summary based on the feedback.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | Assistant | Methodology: Double-blind randomized controlled trial (RCT) with 500 Type 2 diabetes patients. Group A (n=250) received a novel glucagon-like peptide-1/glucose-dependent insulinotropic polypeptide (GLP-1/GIP) dual agonist; Group B (n=250) received a standard GLP-1 agonist. The 24-week trial's primary endpoint was HbA1c reduction. Groups were well-matched for age, BMI, and baseline HbA1c.<br /><br />Findings:<br />- Group A: 1.8% mean HbA1c reduction<br />- Group B: 1.1% mean HbA1c reduction<br />- 68% of Group A vs. 52% of Group B achieved HbA1c \<7%<br />- Group A: 5.2kg mean weight loss<br />- Group B: 3.1kg mean weight loss<br /><br />Secondary endpoints showed improvements in blood pressure and lipid profiles for both groups, with Group A showing slightly better results.<br /><br />Safety: Similar adverse event profiles, with no serious events attributed to either treatment.<br /><br />Clinical Implications: The dual GLP-1/GIP agonist demonstrates superior glycemic control and weight loss compared to standard GLP-1 therapy. These results suggest it could be a significant advancement, particularly for obese diabetics. However, longer-term studies are needed to confirm sustained efficacy and safety, as well as to investigate potential benefits on cardiovascular outcomes. |
  </Accordion>
</AccordionGroup>

***

## Examples

<AccordionGroup>
  <Accordion title="Example: Analyzing a legal contract (without chaining)">
    Note that Claude misses the instruction to provide proposed changes in its email draft.

    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | You're our Chief Legal Officer. Review this SaaS contract for risks, focusing on data privacy, SLAs, and liability caps.<br /><br />\<contract><br />\{\{CONTRACT}}<br />\</contract><br /><br />Then draft an email to the vendor with your concerns and proposed changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
    | Assistant | After reviewing the SaaS contract, I've identified several concerns:<br /><br />1. Data Privacy (Section 7):<br />   - Issue: Vendor has broad rights to use client data for "service improvement."<br />   - Risk: Could lead to unauthorized data sharing or monetization.<br /><br />2. SLAs (Section 5):<br />   - Issue: 99.5% uptime guarantee is below industry standard.<br />   - Risk: Excessive downtime could impact our operations.<br /><br />3. Liability (Section 9):<br />   - Issue: Cap set at 3 months of fees.<br />   - Risk: Inadequate for potential data breaches or service failures.<br /><br />Draft email:<br /><br />Dear \{\{VENDOR}},<br /><br />After reviewing the SaaS agreement, we have concerns:<br /><br />1. Data Privacy: We require that our data only be used for direct service provision, not broad "service improvement." Please amend Section 7.<br /><br />2. SLAs: 99.5% uptime is insufficient. We need 99.99% with clearly defined penalties. Please revise Section 5.<br /><br />3. Liability: The current cap of 3 months' fees is inadequate. We propose a cap of 12 months' fees, with no cap for data breaches or willful misconduct.<br /><br />We value our potential partnership and believe these changes will set us up for success. Please send a revised agreement.<br /><br />Best regards,<br />\{\{CLO\_NAME}} |
  </Accordion>

  <Accordion title="Example: Analyzing a legal contract (with chaining)">
    #### Prompt 1

    | Role                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User                          | You're our Chief Legal Officer. Review this SaaS contract for risks, focusing on data privacy, SLAs, and liability caps.<br /><br />\<contract><br />\{\{CONTRACT}}<br />\</contract><br /><br />Output your findings in \<risks> tags.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | Assistant<br />\{\{CONCERNS}} | 1. Data Privacy (Section 7):<br />   - Issue: Vendor has broad rights to use client data for "service improvement."<br />   - Risk: Could lead to unauthorized data sharing or monetization of client data.<br />   - Impact: Potential breach of client trust, regulatory fines (GDPR, CCPA).<br /><br />2. SLAs (Section 5):<br />   - Issue: 99.5% uptime guarantee is below industry standard (typically 99.99%).<br />   - Risk: Up to 43.8 hours of downtime per year vs. 52.6 minutes at 99.99%.<br />   - Impact: Operational disruptions, revenue loss, client dissatisfaction.<br /><br />3. Liability (Section 9):<br />   - Issue: Liability cap set at 3 months of fees.<br />   - Risk: Inadequate for potential data breaches, IP theft, or prolonged service failures.<br />   - Impact: Insufficient compensation for damages that could far exceed the cap, like class-action lawsuits or regulatory fines. |

    #### Prompt 2

    | Role                       | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User                       | Draft an email to a SaaS product vendor outlining the following concerns and proposing changes. Here are the concerns:<br />\<concerns><br />\{\{CONCERNS}}<br />\</concerns><br /><br />                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | Assistant<br />\{\{EMAIL}} | Dear \{\{VENDOR}},<br /><br />After a thorough review of the proposed SaaS agreement, our legal team has identified several high-priority concerns that must be addressed before we can proceed:<br /><br />1. Data Privacy (Section 7):<br />   - Current: Broad rights to use client data for "service improvement."<br />   - Concern: Potential unauthorized data sharing or monetization.<br />   - Proposed Change: Limit data use to direct service provision. Any use for improvement, analytics, or marketing must be opt-in, revocable, and anonymized.<br /><br />2. SLAs (Section 5):<br />   - Current: 99.5% uptime guarantee.<br />   - Concern: Up to 43.8 hours of downtime per year, risking operational disruptions.<br />   - Proposed Change: 99.99% uptime with tiered service credits. E.g., 10% credit for \<99.99%, 25% for \<99.9%, 50% for \<99.5%.<br /><br />3. Liability (Section 9):<br />   - Current: Cap at 3 months of fees.<br />   - Concern: Grossly inadequate for data breaches, IP theft, or prolonged outages.<br />   - Proposed Change: 12 months' fees for general liability. Uncapped for data breaches, willful misconduct, IP infringement.<br /><br />These changes are non-negotiable for us. They align with industry standards and our commitment to data security, operational excellence, and fiduciary responsibility. We value the potential of our partnership, and addressing these will set a strong foundation.<br /><br />Please have your legal team review and incorporate these changes. We're happy to discuss further to ensure mutual understanding and agreement.<br /><br />Best regards,<br />\{\{CLO\_NAME}} |

    #### Prompt 3

    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | User      | Your task is to review an email and provide feedback. Here is the email:<br />\<email><br />\{\{EMAIL}}<br />\</email><br /><br />Give feedback on tone, clarity, and professionalism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | Assistant | 1. Tone:<br />   - Professional and assertive without being confrontational.<br />   - Use of "non-negotiable" is strong but justified given the criticality of the issues.<br />   - Collaborative language ("we value," "happy to discuss") balances the firmness, maintaining a constructive tone.<br /><br />2. Clarity:<br />   - Excellent structuring: Current state, concern, and proposed change for each issue.<br />   - Technical terms (e.g., "EBITDA," "tiered service credits") are appropriate for a B2B SaaS context.<br />   - Action items are clear: vendor's legal team to review and incorporate changes.<br /><br />3. Professionalism:<br />   - Focuses on mutual benefit and industry standards, not just our demands.<br />   - Mentions broader responsibilities (data security, operational excellence, fiduciary duty), elevating the discussion.<br />   - Offers further discussion, showing commitment to understanding and resolving issues.<br /><br />Overall, the email strikes the right balance of assertiveness and collaboration. It clearly articulates our concerns, proposes specific solutions, and maintains a professional, partnership-oriented tone. No revisions needed; proceed with sending. |
  </Accordion>

  <Accordion title="Example: Multitenancy strategy review">
    #### Prompt 1

    | Role                          | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
    | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User                          | As a senior solutions architect, review and analyze this multitenancy strategy for our new enterprise SaaS product.<br /><br />\<strategy><br />\{\{STRATEGY}}<br />\</strategy><br /><br />Focus on scalability, security, and cost-effectiveness.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | Assistant<br />\{\{ANALYSIS}} | 1. Scalability:<br />   + Database sharding by tenant reduces contention, supports high growth.<br />   + Microservices allow independent scaling of components.<br />   - Shared app servers could bottleneck under extreme load.<br />   - No mention of auto-scaling or load balancing for app tier.<br /><br />2. Security:<br />   + Tenant data isolation via sharding mitigates data leaks.<br />   + JWT with short expiry and refresh tokens is industry best practice.<br />   - No mention of encryption (at rest, in transit) or key management.<br />   - IAM strategy lacks detail on roles, permissions, or RBAC.<br /><br />3. Cost-effectiveness:<br />   + Shared app servers reduce idle resource costs.<br />   + Serverless functions for infrequent tasks optimize costs.<br />   - Per-tenant DB could increase costs at scale vs. optimized multi-tenant DB.<br />   - No discussion of reserved instances or spot instances for cost saving. |

    #### Prompt 2

    | Role                               | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | User                               | Draft a strategy review document for engineering leadership based on this analysis of a multitenancy strategy.<br /><br />\<strategy><br />\{\{STRATEGY}}<br />\</strategy><br /><br />\<analysis><br />\{\{ANALYSIS}}<br />\</analysis><br /><br />Include an executive summary, detailed analysis, and recommendations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
    | Assistant<br />\{\{STRATEGY\_DOC}} | # Multitenancy Strategy Review: SaaS Enterprise Product<br /><br />## Executive Summary<br />The proposed strategy demonstrates a solid foundation in scalability and security principles but has gaps in implementation details. It excels in data isolation and component-level scaling but lacks robust app-tier scaling and advanced security measures. Cost optimizations are present but may falter at high scale. With targeted enhancements, this strategy can effectively support our enterprise SaaS ambitions.<br /><br />## Detailed Analysis<br /><br />### 1. Scalability: B+<br /><br />Strengths:<br />- Database sharding by tenant is excellent. It minimizes query latency, supports high data growth, and facilitates seamless per-tenant scaling.<br />- Microservices architecture allows scaling individual components based on demand, crucial for handling diverse enterprise workloads.<br /><br />Weaknesses:<br />- Shared application servers risk becoming a bottleneck. As tenant count and traffic grow, these could degrade performance across all tenants.<br />- Absence of auto-scaling and load balancing for the app tier is a critical oversight. These are essential for handling traffic spikes without over-provisioning.<br /><br />### 2. Security: B-<br /><br />Strengths:<br />- Sharded databases provide strong tenant data isolation, mitigating risks of data leaks or unauthorized access between tenants.<br />- JWT with short expiry and refresh tokens align with OWASP best practices, reducing token vulnerability windows.<br /><br />Weaknesses:<br />- No mention of data encryption at rest or in transit (TLS 1.3). This is non-negotiable for enterprise data.<br />- Key management strategy is missing. How are encryption keys, JWT secrets, and DB credentials managed and rotated?<br />- IAM lacks depth. We need RBAC with well-defined roles, attribute-based access control (ABAC) for fine-grained permissions, and integration with enterprise identity providers (SAML, OIDC).<br /><br />### 3. Cost-effectiveness: B<br /><br />Strengths:<br />- Shared app servers reduce idle capacity costs, good for steady-state traffic.<br />- Serverless for infrequent tasks (e.g., reporting) is smart; pay only when these resources are used.<br /><br />Weaknesses:<br />- Per-tenant databases may not be cost-effective at scale compared to a well-designed multi-tenant database with robust data partitioning.<br />- No mention of cost-saving measures like reserved instances for predictable workloads or spot instances for fault-tolerant tasks.<br />- Lack of app-tier auto-scaling could lead to over-provisioning, increasing costs.<br /><br />## Recommendations<br /><br />1. **App Tier Resilience**: Implement auto-scaling with Kubernetes or cloud-native services (EKS, GKE). Deploy across availability zones with a CDN for static assets.<br /><br />2. **Security Hardening**:<br />   a. Encrypt data at rest (AES-256) and in transit (TLS 1.3).<br />   b. Use a managed KMS (AWS KMS, GCP KMS) for key management.<br />   c. Enhance IAM with RBAC, ABAC, and SAML/OIDC for enterprise SSO.<br /><br />3. **Cost Optimization**:<br />   a. Evaluate columnar multi-tenant DB (e.g., Snowflake) vs. sharding at scale.<br />   b. Use reserved instances for app servers, spot instances for non-critical workloads.<br />   c. Implement proactive monitoring and right-sizing to avoid overprovisioning.<br /><br />4. **Proof of Concept (PoC)**: Before full implementation, conduct a PoC with a high-scale simulation:<br />   a. Test sharded DB vs. optimized multi-tenant DB for cost and performance.<br />   b. Stress-test app tier with simulated enterprise-level traffic spikes.<br />   c. Conduct third-party security audit, focusing on data isolation and access controls.<br /><br />With these enhancements, our multi-tenancy strategy will be enterprise-grade: scalable, secure, and cost-effective. The PoC will validate our design choices and instill confidence in our enterprise clients. |

    #### Prompt 3

    | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User      | Grade this strategy review document for clarity, actionability, and alignment with enterprise priorities. <br /><br />\<priorities><br />\{\{PRIORITIES}}<br />\</priorities><br /><br />\<strategy\_doc><br />\{\{STRATEGY\_DOC}}<br />\</strategy\_doc>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | Assistant | 1. Clarity: A<br />   + Clear structure with Executive Summary, Detailed Analysis, and Recommendations.<br />   + Analysis uses a grading system (B+, B-) for quick grasp of strengths/weaknesses.<br />   + Technical terms (RBAC, ABAC, TLS) are explained or contextualized, aiding non-technical leadership.<br />   + Visual aids (bullet points, indentation) enhance readability.<br /><br />2. Actionability: A-<br />   + Recommendations are specific and technical (e.g., "Implement auto-scaling with Kubernetes").<br />   + PoC plan with clear objectives provides a roadmap.<br />   + Missing: Timelines, resource requirements, or team assignments for each recommendation.<br />   + Consider: Add a "Next Steps" section with immediate actions, roles, and a high-level timeline.<br /><br />3. Enterprise Alignment: A+<br />   + Directly addresses enterprise priorities:<br />     - Scalability: Discusses handling enterprise-level traffic spikes.<br />     - Security: Focuses on data isolation, encryption, and enterprise IAM.<br />     - Cost: Strategies align with enterprise FinOps (reserved instances, right-sizing).<br />   + PoC with "high-scale simulation" and security audit shows commitment to enterprise-grade quality.<br />   + Language resonates with enterprise concerns: "unacceptable risk," "enterprise-grade," "instill confidence."<br /><br />Overall, the document excels in clarity and enterprise alignment. The actionability is strong but could be elevated to A+ with a "Next Steps" section. The technical depth, coupled with clear explanations, makes this highly effective for both technical and non-technical leadership. Great work! |
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


# Prompting best practices
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices



This guide provides specific prompt engineering techniques for Claude 4.x models, with specific guidance for Sonnet 4.5 and Haiku 4.5. These models have been trained for more precise instruction following than previous generations of Claude models.

<Tip>
  For an overview of Claude 4.5's new capabilities, see [What's new in Claude 4.5](/en/docs/about-claude/models/whats-new-claude-4-5). For migration guidance from previous models, see [Migrating to Claude 4.5](/en/docs/about-claude/models/migrating-to-claude-4).
</Tip>

## General principles

### Be explicit with your instructions

Claude 4.x models respond well to clear, explicit instructions. Being specific about your desired output can help enhance results. Customers who desire the "above and beyond" behavior from previous Claude models might need to more explicitly request these behaviors with newer models.

<Accordion title="Example: Creating an analytics dashboard">
  **Less effective:**

  ```text  theme={null}
  Create an analytics dashboard
  ```

  **More effective:**

  ```text  theme={null}
  Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.
  ```
</Accordion>

### Add context to improve performance

Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude 4.x models better understand your goals and deliver more targeted responses.

<Accordion title="Example: Formatting preferences">
  **Less effective:**

  ```text  theme={null}
  NEVER use ellipses
  ```

  **More effective:**

  ```text  theme={null}
  Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.
  ```
</Accordion>

Claude is smart enough to generalize from the explanation.

### Be vigilant with examples & details

Claude 4.x models pay close attention to details and examples as part of their precise instruction following capabilities. Ensure that your examples align with the behaviors you want to encourage and minimize behaviors you want to avoid.

### Long-horizon reasoning and state tracking

Claude 4.5 models excel at long-horizon reasoning tasks with exceptional state tracking capabilities. It maintains orientation across extended sessions by focusing on incremental progress—making steady advances on a few things at a time rather than attempting everything at once. This capability especially emerges over multiple context windows or task iterations, where Claude can work on a complex task, save the state, and continue with a fresh context window.

#### Context awareness and multi-window workflows

Claude 4.5 models feature [context awareness](/en/docs/build-with-claude/context-windows#context-awareness-in-claude-sonnet-4-5), enabling the model to track its remaining context window (i.e. "token budget") throughout a conversation. This enables Claude to execute tasks and manage context more effectively by understanding how much space it has to work.

**Managing context limits:**

If you are using Claude in an agent harness that compacts context or allows saving context to external files (like in Claude Code), we suggest adding this information to your prompt so Claude can behave accordingly. Otherwise, Claude may sometimes naturally try to wrap up work as it approaches the context limit. Below is an example prompt:

```text Sample prompt theme={null}
Your context window will be automatically compacted as it approaches its limit, allowing you to continue working indefinitely from where you left off. Therefore, do not stop tasks early due to token budget concerns. As you approach your token budget limit, save your current progress and state to memory before the context window refreshes. Always be as persistent and autonomous as possible and complete tasks fully, even if the end of your budget is approaching. Never artificially stop any task early regardless of the context remaining.
```

The [memory tool](/en/docs/agents-and-tools/tool-use/memory-tool) pairs naturally with context awareness for seamless context transitions.

#### Multi-context window workflows

For tasks spanning multiple context windows:

1. **Use a different prompt for the very first context window**: Use the first context window to set up a framework (write tests, create setup scripts), then use future context windows to iterate on a todo-list.

2. **Have the model write tests in a structured format**: Ask Claude to create tests before starting work and keep track of them in a structured format (e.g., `tests.json`). This leads to better long-term ability to iterate. Remind Claude of the importance of tests: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."

3. **Set up quality of life tools**: Encourage Claude to create setup scripts (e.g., `init.sh`) to gracefully start servers, run test suites, and linters. This prevents repeated work when continuing from a fresh context window.

4. **Starting fresh vs compacting**: When a context window is cleared, consider starting with a brand new context window rather than using compaction. Claude 4.5 models are extremely effective at discovering state from the local filesystem. In some cases, you may want to take advantage of this over compaction. Be prescriptive about how it should start:
   * "Call pwd; you can only read and write files in this directory."
   * "Review progress.txt, tests.json, and the git logs."
   * "Manually run through a fundamental integration test before moving on to implementing new features."

5. **Provide verification tools**: As the length of autonomous tasks grows, Claude needs to verify correctness without continuous human feedback. Tools like Playwright MCP server or computer use capabilities for testing UIs are helpful.

6. **Encourage complete usage of context**: Prompt Claude to efficiently complete components before moving on:

```text Sample prompt theme={null}
This is a very long task, so it may be beneficial to plan out your work clearly. It's encouraged to spend your entire output context working on the task - just make sure you don't run out of context with significant uncommitted work. Continue working systematically until you have completed this task.
```

#### State management best practices

* **Use structured formats for state data**: When tracking structured information (like test results or task status), use JSON or other structured formats to help Claude understand schema requirements
* **Use unstructured text for progress notes**: Freeform progress notes work well for tracking general progress and context
* **Use git for state tracking**: Git provides a log of what's been done and checkpoints that can be restored. Claude 4.5 models perform especially well in using git to track state across multiple sessions.
* **Emphasize incremental progress**: Explicitly ask Claude to keep track of its progress and focus on incremental work

<Accordion title="Example: State tracking">
  ```json  theme={null}
  // Structured state file (tests.json)
  {
    "tests": [
      {"id": 1, "name": "authentication_flow", "status": "passing"},
      {"id": 2, "name": "user_management", "status": "failing"},
      {"id": 3, "name": "api_endpoints", "status": "not_started"}
    ],
    "total": 200,
    "passing": 150,
    "failing": 25,
    "not_started": 25
  }
  ```

  ```text  theme={null}
  // Progress notes (progress.txt)
  Session 3 progress:
  - Fixed authentication token validation
  - Updated user model to handle edge cases
  - Next: investigate user_management test failures (test #2)
  - Note: Do not remove tests as this could lead to missing functionality
  ```
</Accordion>

### Communication style

Claude 4.5 models have a more concise and natural communication style compared to previous models:

* **More direct and grounded**: Provides fact-based progress reports rather than self-celebratory updates
* **More conversational**: Slightly more fluent and colloquial, less machine-like
* **Less verbose**: May skip detailed summaries for efficiency unless prompted otherwise

This communication style accurately reflects what has been accomplished without unnecessary elaboration.

## Guidance for specific situations

### Balance verbosity

Claude 4.5 models tend toward efficiency and may skip verbal summaries after tool calls, jumping directly to the next action. While this creates a streamlined workflow, you may prefer more visibility into its reasoning process.

If you want Claude to provide updates as it works:

```text Sample prompt theme={null}
After completing a task that involves tool use, provide a quick summary of the work you've done.
```

### Tool usage patterns

Claude 4.5 models are trained for precise instruction following and benefits from explicit direction to use specific tools. If you say "can you suggest some changes," it will sometimes provide suggestions rather than implementing them—even if making changes might be what you intended.

For Claude to take action, be more explicit:

<Accordion title="Example: Explicit instructions">
  **Less effective (Claude will only suggest):**

  ```text  theme={null}
  Can you suggest some changes to improve this function?
  ```

  **More effective (Claude will make the changes):**

  ```text  theme={null}
  Change this function to improve its performance.
  ```

  Or:

  ```text  theme={null}
  Make these edits to the authentication flow.
  ```
</Accordion>

To make Claude more proactive about taking action by default, you can add this to your system prompt:

```text Sample prompt for proactive action theme={null}
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is unclear, infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing. Try to infer the user's intent about whether a tool call (e.g., file edit or read) is intended or not, and act accordingly.
</default_to_action>
```

On the other hand, if you want the model to be more hesitant by default, less prone to jumping straight into implementations, and only take action if requested, you can steer this behavior with a prompt like the below:

```text Sample prompt for conservative action theme={null}
<do_not_act_before_instructions>
Do not jump into implementatation or changes files unless clearly instructed to make changes. When the user's intent is ambiguous, default to providing information, doing research, and providing recommendations rather than taking action. Only proceed with edits, modifications, or implementations when the user explicitly requests them.
</do_not_act_before_instructions>
```

### Control the format of responses

There are a few ways that we have found to be particularly effective in steering output formatting in Claude 4.x models:

1. **Tell Claude what to do instead of what not to do**

   * Instead of: "Do not use markdown in your response"
   * Try: "Your response should be composed of smoothly flowing prose paragraphs."

2. **Use XML format indicators**

   * Try: "Write the prose sections of your response in \<smoothly\_flowing\_prose\_paragraphs> tags."

3. **Match your prompt style to the desired output**

   The formatting style used in your prompt may influence Claude's response style. If you are still experiencing steerability issues with output formatting, we recommend as best as you can matching your prompt style to your desired output style. For example, removing markdown from your prompt can reduce the volume of markdown in the output.

4. **Use detailed prompts for specific formatting preferences**

   For more control over markdown and formatting usage, provide explicit guidance:

````text Sample prompt to minimize markdown theme={null}
<avoid_excessive_markdown_and_bullet_points>
When writing reports, documents, technical explanations, analyses, or any long-form content, write in clear, flowing prose using complete paragraphs and sentences. Use standard paragraph breaks for organization and reserve markdown primarily for `inline code`, code blocks (```...```), and simple headings (###, and ###). Avoid using **bold** and *italics*.

DO NOT use ordered lists (1. ...) or unordered lists (*) unless : a) you're presenting truly discrete items where a list format is the best option, or b) the user explicitly requests a list or ranking

Instead of listing items with bullets or numbers, incorporate them naturally into sentences. This guidance applies especially to technical writing. Using prose instead of excessive formatting will improve user satisfaction. NEVER output a series of overly short bullet points.

Your goal is readable, flowing text that guides the reader naturally through ideas rather than fragmenting information into isolated points.
</avoid_excessive_markdown_and_bullet_points>
````

### Research and information gathering

Claude 4.5 models demonstrate exceptional agentic search capabilities and can find and synthesize information from multiple sources effectively. For optimal research results:

1. **Provide clear success criteria**: Define what constitutes a successful answer to your research question

2. **Encourage source verification**: Ask Claude to verify information across multiple sources

3. **For complex research tasks, use a structured approach**:

```text Sample prompt for complex research theme={null}
Search for this information in a structured way. As you gather data, develop several competing hypotheses. Track your confidence levels in your progress notes to improve calibration. Regularly self-critique your approach and plan. Update a hypothesis tree or research notes file to persist information and provide transparency. Break down this complex research task systematically.
```

This structured approach allows Claude to find and synthesize virtually any piece of information and iteratively critique its findings, no matter the size of the corpus.

### Subagent orchestration

Claude 4.5 models demonstrate significantly improved native subagent orchestration capabilities. These models can recognize when tasks would benefit from delegating work to specialized subagents and do so proactively without requiring explicit instruction.

To take advantage of this behavior:

1. **Ensure well-defined subagent tools**: Have subagent tools available and described in tool definitions
2. **Let Claude orchestrate naturally**: Claude will delegate appropriately without explicit instruction
3. **Adjust conservativeness if needed**:

```text Sample prompt for conservative subagent usage theme={null}
Only delegate to subagents when the task clearly benefits from a separate agent with a new context window.
```

### Model self-knowledge

If you would like Claude to identify itself correctly in your application or use specific API strings:

```text Sample prompt for model identity theme={null}
The assistant is Claude, created by Anthropic. The current model is Claude Sonnet 4.5.
```

For LLM-powered apps that need to specify model strings:

```text Sample prompt for model string theme={null}
When an LLM is needed, please default to Claude Sonnet 4.5 unless the user requests otherwise. The exact model string for Claude Sonnet 4.5 is claude-sonnet-4-5-20250929.
```

### Leverage thinking & interleaved thinking capabilities

Claude 4.x models offer thinking capabilities that can be especially helpful for tasks involving reflection after tool use or complex multi-step reasoning. You can guide its initial or interleaved thinking for better results.

```text Example prompt theme={null}
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.
```

<Info>
  For more information on thinking capabilities, see [Extended thinking](/en/docs/build-with-claude/extended-thinking).
</Info>

### Document creation

Claude 4.5 models excel at creating presentations, animations, and visual documents. These models match or exceed Claude Opus 4.1 in this domain, with impressive creative flair and stronger instruction following. The models produce polished, usable output on the first try in most cases.

For best results with document creation:

```text Sample prompt theme={null}
Create a professional presentation on [topic]. Include thoughtful design elements, visual hierarchy, and engaging animations where appropriate.
```

### Optimize parallel tool calling

Claude 4.x models excel at parallel tool execution, with Sonnet 4.5 being particularly aggressive in firing off multiple operations simultaneously. Claude 4.x models will:

* Run multiple speculative searches during research
* Read several files at once to build context faster
* Execute bash commands in parallel (which can even bottleneck system performance)

This behavior is easily steerable. While the model has a high success rate in parallel tool calling without prompting, you can boost this to \~100% or adjust the aggression level:

```text Sample prompt for maximum parallel efficiency theme={null}
<use_parallel_tool_calls>
If you intend to call multiple tools and there are no dependencies between the tool calls, make all of the independent tool calls in parallel. Prioritize calling tools simultaneously whenever the actions can be done in parallel rather than sequentially. For example, when reading 3 files, run 3 tool calls in parallel to read all 3 files into context at the same time. Maximize use of parallel tool calls where possible to increase speed and efficiency. However, if some tool calls depend on previous calls to inform dependent values like the parameters, do NOT call these tools in parallel and instead call them sequentially. Never use placeholders or guess missing parameters in tool calls.
</use_parallel_tool_calls>
```

```text Sample prompt to reduce parallel execution theme={null}
Execute operations sequentially with brief pauses between each step to ensure stability.
```

### Reduce file creation in agentic coding

Claude 4.x models may sometimes create new files for testing and iteration purposes, particularly when working with code. This approach allows Claude to use files, especially python scripts, as a 'temporary scratchpad' before saving its final output. Using temporary files can improve outcomes particularly for agentic coding use cases.

If you'd prefer to minimize net new file creation, you can instruct Claude to clean up after itself:

```text Sample prompt theme={null}
If you create any temporary new files, scripts, or helper files for iteration, clean up these files by removing them at the end of the task.
```

### Enhance visual and frontend code generation

Claude 4.x models can generate high-quality, visually distinctive, functional user interfaces. However, without guidance, frontend code can default to generic patterns that lack visual interest. To elicit exceptional UI results:

1. **Provide explicit encouragement for creativity:**

```text Sample prompt theme={null}
Don't hold back. Give it your all. Create an impressive demonstration showcasing web development capabilities.
```

2. **Specify aesthetic direction and design constraints:**

```text Sample prompt theme={null}
Create a professional dashboard using a dark blue and cyan color palette, modern sans-serif typography (e.g., Inter for headings, system fonts for body), and card-based layouts with subtle shadows. Include thoughtful details like hover states, transitions, and micro-interactions. Apply design principles: hierarchy, contrast, balance, and movement.
```

3. **Encourage design diversity and fusion aesthetics:**

```text Sample prompt theme={null}
Provide multiple design options. Create fusion aesthetics by combining elements from different sources—one color scheme, different typography, another layout principle. Avoid generic centered layouts, simplistic gradients, and uniform styling.
```

4. **Request specific features explicitly:**

* "Include as many relevant features and interactions as possible"
* "Add animations and interactive elements"
* "Create a fully-featured implementation beyond the basics"

### Avoid focusing on passing tests and hard-coding

Claude 4.x models can sometimes focus too heavily on making tests pass at the expense of more general solutions, or may use workarounds like helper scripts for complex refactoring instead of using standard tools directly. To prevent this behavior and ensure robust, generalizable solutions:

```text Sample prompt theme={null}
Please write a high-quality, general-purpose solution using the standard tools available. Do not create helper scripts or workarounds to accomplish the task more efficiently. Implement a solution that works correctly for all valid inputs, not just the test cases. Do not hard-code values or create solutions that only work for specific test inputs. Instead, implement the actual logic that solves the problem generally.

Focus on understanding the problem requirements and implementing the correct algorithm. Tests are there to verify correctness, not to define the solution. Provide a principled implementation that follows best practices and software design principles.

If the task is unreasonable or infeasible, or if any of the tests are incorrect, please inform me rather than working around them. The solution should be robust, maintainable, and extendable.
```

### Minimizing hallucinations in agentic coding

Claude 4.x models are less prone to hallucinations and give more accurate, grounded, intelligent answers based on the code. To encourage this behavior even more and minimize hallucinations:

```text Sample prompt theme={null}
<investigate_before_answering>
Never speculate about code you have not opened. If the user references a specific file, you MUST read the file before answering. Make sure to investigate and read relevant files BEFORE answering questions about the codebase. Never make any claims about code before investigating unless you are certain of the correct answer - give grounded and hallucination-free answers.
</investigate_before_answering>
```

## Migration considerations

When migrating to Claude 4.5 models:

1. **Be specific about desired behavior**: Consider describing exactly what you'd like to see in the output.

2. **Frame your instructions with modifiers**: Adding modifiers that encourage Claude to increase the quality and detail of its output can help better shape Claude's performance. For example, instead of "Create an analytics dashboard", use "Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation."

3. **Request specific features explicitly**: Animations and interactive elements should be requested explicitly when desired.


# Extended thinking tips
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips



export const TryInConsoleButton = ({userPrompt, systemPrompt, maxTokens, thinkingBudgetTokens, buttonVariant = "primary", children}) => {
  const url = new URL("https://console.anthropic.com/workbench/new");
  if (userPrompt) {
    url.searchParams.set("user", userPrompt);
  }
  if (systemPrompt) {
    url.searchParams.set("system", systemPrompt);
  }
  if (maxTokens) {
    url.searchParams.set("max_tokens", maxTokens);
  }
  if (thinkingBudgetTokens) {
    url.searchParams.set("thinking.budget_tokens", thinkingBudgetTokens);
  }
  return <div style={{
    width: "100%",
    position: "relative",
    top: "-77px",
    textAlign: "right"
  }}>
      <a href={url.href} className={`btn size-xs ${buttonVariant}`} style={{
    position: "relative",
    right: "20px",
    zIndex: "10"
  }}>
        {children || "Try in Console"}{" "}
        <Icon icon="arrow-up-right" color="currentColor" size={14} />
      </a>
    </div>;
};

This guide provides advanced strategies and techniques for getting the most out of Claude's extended thinking features. Extended thinking allows Claude to work through complex problems step-by-step, improving performance on difficult tasks.

See [Extended thinking models](/en/docs/about-claude/models/extended-thinking-models) for guidance on deciding when to use extended thinking.

## Before diving in

This guide presumes that you have already decided to use extended thinking mode and have reviewed our basic steps on [how to get started with extended thinking](/en/docs/about-claude/models/extended-thinking-models#getting-started-with-extended-thinking-models) as well as our [extended thinking implementation guide](/en/docs/build-with-claude/extended-thinking).

### Technical considerations for extended thinking

* Thinking tokens have a minimum budget of 1024 tokens. We recommend that you start with the minimum thinking budget and incrementally increase to adjust based on your needs and task complexity.
* For workloads where the optimal thinking budget is above 32K, we recommend that you use [batch processing](/en/docs/build-with-claude/batch-processing) to avoid networking issues. Requests pushing the model to think above 32K tokens causes long running requests that might run up against system timeouts and open connection limits.
* Extended thinking performs best in English, though final outputs can be in [any language Claude supports](/en/docs/build-with-claude/multilingual-support).
* If you need thinking below the minimum budget, we recommend using standard mode, with thinking turned off, with traditional chain-of-thought prompting with XML tags (like `<thinking>`). See [chain of thought prompting](/en/docs/build-with-claude/prompt-engineering/chain-of-thought).

## Prompting techniques for extended thinking

### Use general instructions first, then troubleshoot with more step-by-step instructions

Claude often performs better with high level instructions to just think deeply about a task rather than step-by-step prescriptive guidance. The model's creativity in approaching problems may exceed a human's ability to prescribe the optimal thinking process.

For example, instead of:

<CodeGroup>
  ```text User theme={null}
  Think through this math problem step by step: 
  1. First, identify the variables
  2. Then, set up the equation
  3. Next, solve for x
  ...
  ```
</CodeGroup>

Consider:

<CodeGroup>
  ```text User theme={null}
  Please think about this math problem thoroughly and in great detail. 
  Consider multiple approaches and show your complete reasoning.
  Try different methods if your first approach doesn't work.
  ```

  />
</CodeGroup>

<TryInConsoleButton
  userPrompt={
  `Please think about this math problem thoroughly and in great detail. 
Consider multiple approaches and show your complete reasoning.
Try different methods if your first approach doesn't work.`
}
  thinkingBudgetTokens={16000}
>
  Try in Console
</TryInConsoleButton>

That said, Claude can still effectively follow complex structured execution steps when needed. The model can handle even longer lists with more complex instructions than previous versions. We recommend that you start with more generalized instructions, then read Claude's thinking output and iterate to provide more specific instructions to steer its thinking from there.

### Multishot prompting with extended thinking

[Multishot prompting](/en/docs/build-with-claude/prompt-engineering/multishot-prompting) works well with extended thinking. When you provide Claude examples of how to think through problems, it will follow similar reasoning patterns within its extended thinking blocks.

You can include few-shot examples in your prompt in extended thinking scenarios by using XML tags like `<thinking>` or `<scratchpad>` to indicate canonical patterns of extended thinking in those examples.

Claude will generalize the pattern to the formal extended thinking process. However, it's possible you'll get better results by giving Claude free rein to think in the way it deems best.

Example:

<CodeGroup>
  ```text User theme={null}
  I'm going to show you how to solve a math problem, then I want you to solve a similar one.

  Problem 1: What is 15% of 80?

  <thinking>
  To find 15% of 80:
  1. Convert 15% to a decimal: 15% = 0.15
  2. Multiply: 0.15 × 80 = 12
  </thinking>

  The answer is 12.

  Now solve this one:
  Problem 2: What is 35% of 240?
  ```

  />
</CodeGroup>

<TryInConsoleButton
  userPrompt={
  `I'm going to show you how to solve a math problem, then I want you to solve a similar one.

Problem 1: What is 15% of 80?

<thinking>
To find 15% of 80:
1. Convert 15% to a decimal: 15% = 0.15
2. Multiply: 0.15 × 80 = 12
</thinking>

The answer is 12.

Now solve this one:
Problem 2: What is 35% of 240?`
}
  thinkingBudgetTokens={16000}
>
  Try in Console
</TryInConsoleButton>

### Maximizing instruction following with extended thinking

Claude shows significantly improved instruction following when extended thinking is enabled. The model typically:

1. Reasons about instructions inside the extended thinking block
2. Executes those instructions in the response

To maximize instruction following:

* Be clear and specific about what you want
* For complex instructions, consider breaking them into numbered steps that Claude should work through methodically
* Allow Claude enough budget to process the instructions fully in its extended thinking

### Using extended thinking to debug and steer Claude's behavior

You can use Claude's thinking output to debug Claude's logic, although this method is not always perfectly reliable.

To make the best use of this methodology, we recommend the following tips:

* We don't recommend passing Claude's extended thinking back in the user text block, as this doesn't improve performance and may actually degrade results.
* Prefilling extended thinking is explicitly not allowed, and manually changing the model's output text that follows its thinking block is likely going to degrade results due to model confusion.

When extended thinking is turned off, standard `assistant` response text [prefill](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response) is still allowed.

<Note>
  Sometimes Claude may repeat its extended thinking in the assistant output text. If you want a clean response, instruct Claude not to repeat its extended thinking and to only output the answer.
</Note>

### Making the best of long outputs and longform thinking

For dataset generation use cases, try prompts such as "Please create an extremely detailed table of..." for generating comprehensive datasets.

For use cases such as detailed content generation where you may want to generate longer extended thinking blocks and more detailed responses, try these tips:

* Increase both the maximum extended thinking length AND explicitly ask for longer outputs
* For very long outputs (20,000+ words), request a detailed outline with word counts down to the paragraph level. Then ask Claude to index its paragraphs to the outline and maintain the specified word counts

<Warning>
  We do not recommend that you push Claude to output more tokens for outputting tokens' sake. Rather, we encourage you to start with a small thinking budget and increase as needed to find the optimal settings for your use case.
</Warning>

Here are example use cases where Claude excels due to longer extended thinking:

<AccordionGroup>
  <Accordion title="Complex STEM problems">
    Complex STEM problems require Claude to build mental models, apply specialized knowledge, and work through sequential logical steps—processes that benefit from longer reasoning time.

    <Tabs>
      <Tab title="Standard prompt">
        <CodeGroup>
          ```text User theme={null}
          Write a python script for a bouncing yellow ball within a square,
          make sure to handle collision detection properly.
          Make the square slowly rotate.
          ```

          />
        </CodeGroup>

        <TryInConsoleButton
          userPrompt={
          `Write a python script for a bouncing yellow ball within a square,
make sure to handle collision detection properly.
Make the square slowly rotate.`
        }
          thinkingBudgetTokens={16000}
        >
          Try in Console
        </TryInConsoleButton>

        <Note>
          This simpler task typically results in only about a few seconds of thinking time.
        </Note>
      </Tab>

      <Tab title="Enhanced prompt">
        <CodeGroup>
          ```text User theme={null}
          Write a Python script for a bouncing yellow ball within a tesseract, 
          making sure to handle collision detection properly. 
          Make the tesseract slowly rotate. 
          Make sure the ball stays within the tesseract.
          ```

          />
        </CodeGroup>

        <TryInConsoleButton
          userPrompt={
          `Write a Python script for a bouncing yellow ball within a tesseract, 
making sure to handle collision detection properly. 
Make the tesseract slowly rotate. 
Make sure the ball stays within the tesseract.`
        }
          thinkingBudgetTokens={16000}
        >
          Try in Console
        </TryInConsoleButton>

        <Note>
          This complex 4D visualization challenge makes the best use of long extended thinking time as Claude works through the mathematical and programming complexity.
        </Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Constraint optimization problems">
    Constraint optimization challenges Claude to satisfy multiple competing requirements simultaneously, which is best accomplished when allowing for long extended thinking time so that the model can methodically address each constraint.

    <Tabs>
      <Tab title="Standard prompt">
        <CodeGroup>
          ```text User theme={null}
          Plan a week-long vacation to Japan.
          ```

          />
        </CodeGroup>

        <TryInConsoleButton userPrompt="Plan a week-long vacation to Japan." thinkingBudgetTokens={16000}>
          Try in Console
        </TryInConsoleButton>

        <Note>
          This open-ended request typically results in only about a few seconds of thinking time.
        </Note>
      </Tab>

      <Tab title="Enhanced prompt">
        <CodeGroup>
          ```text User theme={null}
          Plan a 7-day trip to Japan with the following constraints:
          - Budget of $2,500
          - Must include Tokyo and Kyoto
          - Need to accommodate a vegetarian diet
          - Preference for cultural experiences over shopping
          - Must include one day of hiking
          - No more than 2 hours of travel between locations per day
          - Need free time each afternoon for calls back home
          - Must avoid crowds where possible
          ```

          />
        </CodeGroup>

        <TryInConsoleButton
          userPrompt={
          `Plan a 7-day trip to Japan with the following constraints:
- Budget of $2,500
- Must include Tokyo and Kyoto
- Need to accommodate a vegetarian diet
- Preference for cultural experiences over shopping
- Must include one day of hiking
- No more than 2 hours of travel between locations per day
- Need free time each afternoon for calls back home
- Must avoid crowds where possible`
        }
          thinkingBudgetTokens={16000}
        >
          Try in Console
        </TryInConsoleButton>

        <Note>
          With multiple constraints to balance, Claude will naturally perform best when given more space to think through how to satisfy all requirements optimally.
        </Note>
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Thinking frameworks">
    Structured thinking frameworks give Claude an explicit methodology to follow, which may work best when Claude is given long extended thinking space to follow each step.

    <Tabs>
      <Tab title="Standard prompt">
        <CodeGroup>
          ```text User theme={null}
          Develop a comprehensive strategy for Microsoft 
          entering the personalized medicine market by 2027.
          ```

          />
        </CodeGroup>

        <TryInConsoleButton
          userPrompt={
          `Develop a comprehensive strategy for Microsoft 
entering the personalized medicine market by 2027.`
        }
          thinkingBudgetTokens={16000}
        >
          Try in Console
        </TryInConsoleButton>

        <Note>
          This broad strategic question typically results in only about a few seconds of thinking time.
        </Note>
      </Tab>

      <Tab title="Enhanced prompt">
        <CodeGroup>
          ```text User theme={null}
          Develop a comprehensive strategy for Microsoft entering 
          the personalized medicine market by 2027.

          Begin with:
          1. A Blue Ocean Strategy canvas
          2. Apply Porter's Five Forces to identify competitive pressures

          Next, conduct a scenario planning exercise with four 
          distinct futures based on regulatory and technological variables.

          For each scenario:
          - Develop strategic responses using the Ansoff Matrix

          Finally, apply the Three Horizons framework to:
          - Map the transition pathway
          - Identify potential disruptive innovations at each stage
          ```

          />
        </CodeGroup>

        <TryInConsoleButton
          userPrompt={
          `Develop a comprehensive strategy for Microsoft entering 
the personalized medicine market by 2027.

Begin with:
1. A Blue Ocean Strategy canvas
2. Apply Porter's Five Forces to identify competitive pressures

Next, conduct a scenario planning exercise with four 
distinct futures based on regulatory and technological variables.

For each scenario:
- Develop strategic responses using the Ansoff Matrix

Finally, apply the Three Horizons framework to:
- Map the transition pathway
- Identify potential disruptive innovations at each stage`
        }
          thinkingBudgetTokens={16000}
        >
          Try in Console
        </TryInConsoleButton>

        <Note>
          By specifying multiple analytical frameworks that must be applied sequentially, thinking time naturally increases as Claude works through each framework methodically.
        </Note>
      </Tab>
    </Tabs>
  </Accordion>
</AccordionGroup>

### Have Claude reflect on and check its work for improved consistency and error handling

You can use simple natural language prompting to improve consistency and reduce errors:

1. Ask Claude to verify its work with a simple test before declaring a task complete
2. Instruct the model to analyze whether its previous step achieved the expected result
3. For coding tasks, ask Claude to run through test cases in its extended thinking

Example:

<CodeGroup>
  ```text User theme={null}
  Write a function to calculate the factorial of a number. 
  Before you finish, please verify your solution with test cases for:
  - n=0
  - n=1
  - n=5
  - n=10
  And fix any issues you find.
  ```

  />
</CodeGroup>

<TryInConsoleButton
  userPrompt={
  `Write a function to calculate the factorial of a number. 
Before you finish, please verify your solution with test cases for:
- n=0
- n=1
- n=5
- n=10
And fix any issues you find.`
}
  thinkingBudgetTokens={16000}
>
  Try in Console
</TryInConsoleButton>

## Next steps

<CardGroup>
  <Card title="Extended thinking cookbook" icon="book" href="https://github.com/anthropics/anthropic-cookbook/tree/main/extended_thinking">
    Explore practical examples of extended thinking in our cookbook.
  </Card>

  <Card title="Extended thinking guide" icon="code" href="/en/docs/build-with-claude/extended-thinking">
    See complete technical documentation for implementing extended thinking.
  </Card>
</CardGroup>


# Long context prompting tips
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/long-context-tips



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

Claude's extended context window (200K tokens for Claude 3 models) enables handling complex, data-rich tasks. This guide will help you leverage this power effectively.

## Essential tips for long context prompts

* **Put longform data at the top**: Place your long documents and inputs (\~20K+ tokens) near the top of your prompt, above your query, instructions, and examples. This can significantly improve Claude's performance across all models.

  <Note>Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs.</Note>

* **Structure document content and metadata with XML tags**: When using multiple documents, wrap each document in `<document>` tags with `<document_content>` and `<source>` (and other metadata) subtags for clarity.

  <Accordion title="Example multi-document structure">
    ```xml  theme={null}
    <documents>
      <document index="1">
        <source>annual_report_2023.pdf</source>
        <document_content>
          {{ANNUAL_REPORT}}
        </document_content>
      </document>
      <document index="2">
        <source>competitor_analysis_q2.xlsx</source>
        <document_content>
          {{COMPETITOR_ANALYSIS}}
        </document_content>
      </document>
    </documents>

    Analyze the annual report and competitor analysis. Identify strategic advantages and recommend Q3 focus areas.
    ```
  </Accordion>

* **Ground responses in quotes**: For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the "noise" of the rest of the document's contents.

  <Accordion title="Example quote extraction">
    ```xml  theme={null}
    You are an AI physician's assistant. Your task is to help doctors diagnose possible patient illnesses.

    <documents>
      <document index="1">
        <source>patient_symptoms.txt</source>
        <document_content>
          {{PATIENT_SYMPTOMS}}
        </document_content>
      </document>
      <document index="2">
        <source>patient_records.txt</source>
        <document_content>
          {{PATIENT_RECORDS}}
        </document_content>
      </document>
      <document index="3">
        <source>patient01_appt_history.txt</source>
        <document_content>
          {{PATIENT01_APPOINTMENT_HISTORY}}
        </document_content>
      </document>
    </documents>

    Find quotes from the patient records and appointment history that are relevant to diagnosing the patient's reported symptoms. Place these in <quotes> tags. Then, based on these quotes, list all information that would help the doctor diagnose the patient's symptoms. Place your diagnostic information in <info> tags.
    ```
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


# Use examples (multishot prompting) to guide Claude's behavior
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

Examples are your secret weapon shortcut for getting Claude to generate exactly what you need. By providing a few well-crafted examples in your prompt, you can dramatically improve the accuracy, consistency, and quality of Claude's outputs.
This technique, known as few-shot or multishot prompting, is particularly effective for tasks that require structured outputs or adherence to specific formats.

<Tip>**Power up your prompts**: Include 3-5 diverse, relevant examples to show Claude exactly what you want. More examples = better performance, especially for complex tasks.</Tip>

## Why use examples?

* **Accuracy**: Examples reduce misinterpretation of instructions.
* **Consistency**: Examples enforce uniform structure and style.
* **Performance**: Well-chosen examples boost Claude's ability to handle complex tasks.

## Crafting effective examples

For maximum effectiveness, make sure that your examples are:

* **Relevant**: Your examples mirror your actual use case.
* **Diverse**: Your examples cover edge cases and potential challenges, and vary enough that Claude doesn't inadvertently pick up on unintended patterns.
* **Clear**: Your examples are wrapped in `<example>` tags (if multiple, nested within `<examples>` tags) for structure.

<Tip>Ask Claude to evaluate your examples for relevance, diversity, or clarity. Or have Claude generate more examples based on your initial set.</Tip>

<Accordion title="Example: Analyzing customer feedback">
  Notice that in the "no examples" version, Claude does not list multiple options for each category, despite its written analysis indicating that there are multiple categories for certain feedback. It also includes a long explanation when we may not want it to.

  | Role                          | No Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | With Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User                          | Analyze this customer feedback and categorize the issues. Use these categories: UI/UX, Performance, Feature Request, Integration, Pricing, and Other. Also rate the sentiment (Positive/Neutral/Negative) and priority (High/Medium/Low).<br /><br />Here is the feedback: \{\{FEEDBACK}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Our CS team is overwhelmed with unstructured feedback. Your task is to analyze feedback and categorize issues for our product and engineering teams. Use these categories: UI/UX, Performance, Feature Request, Integration, Pricing, and Other. Also rate the sentiment (Positive/Neutral/Negative) and priority (High/Medium/Low). Here is an example:<br /><br />\<example><br />Input: The new dashboard is a mess! It takes forever to load, and I can't find the export button. Fix this ASAP!<br />Category: UI/UX, Performance<br />Sentiment: Negative<br />Priority: High\</example><br /><br />Now, analyze this feedback: \{\{FEEDBACK}}                                                                                                                                                                                                                                                                                                                                                                                               |
  | Assistant (Claude's response) | Here's the analysis of the customer feedback:<br /><br />Issue: UI/UX<br />Sentiment: Negative<br />Priority: High<br />The customer is frustrated with the new dashboard design, which they find cluttered and slow to load. They specifically call out the missing "export" button, which is likely a critical feature. This issue needs to be addressed as a high priority.<br /><br />Issue: Integration<br />Sentiment: Positive<br />Priority: Medium<br />The customer is pleased with the existing Salesforce integration but would like to see support for Hubspot as well. This is a feature request that could be considered for a future product update.<br /><br />Issue: Pricing<br />Sentiment: Negative<br />Priority: High<br />The customer finds the pricing to be unreasonable, especially for the basic features. They are threatening to switch to a competitor, so this is a high-priority issue that needs to be reviewed.<br /><br />Issue: Performance<br />Sentiment Negative<br />Priority: High<br />The customer is experiencing critical issues with the mobile app, where large file uploads consistently result in crashes. This is a significant problem that impacts the customer's ability to use the product effectively and should be addressed as a high priority.<br /><br />Issue: UI/UX<br />Sentiment: Positive<br />Priority: Low<br />The customer is overall satisfied with the product, specifically calling out the intuitive UI and excellent customer support. This is a positive piece of feedback that does not require any immediate action. | Here's the analysis of the customer feedback:<br /><br />1. The new dashboard is a mess! It takes forever to load, and I can't find the export button. Fix this ASAP!<br />Category: UI/UX, Performance<br />Sentiment: Negative<br />Priority: High<br /><br />2. Love the Salesforce integration! But it'd be great if you could add Hubspot too.<br />Category: Integration, Feature Request<br />Sentiment: Positive<br />Priority: Medium<br /><br />3. Your pricing is ridiculous! \$99/mo for basic features? I'm switching to Competitor X.<br />Category: Pricing<br />Sentiment: Negative<br />Priority: High<br /><br />4. The mobile app keeps crashing when I try to upload large files (>50MB). This is critical for our field agents.<br />Category: Performance<br />Sentiment: Negative<br />Priority: High<br /><br />5. Overall, I'm happy with the product. The UI is intuitive, and the customer support is top-notch. Keep it up!<br />Category: UI/UX, Other (Customer Support)<br />Sentiment: Positive<br />Priority: Low |
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


# Prompt engineering overview
Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview



<Note>
  While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).
</Note>

## Before prompt engineering

This guide assumes that you have:

1. A clear definition of the success criteria for your use case
2. Some ways to empirically test against those criteria
3. A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out [Define your success criteria](/en/docs/test-and-evaluate/define-success) and [Create strong empirical evaluations](/en/docs/test-and-evaluate/develop-tests) for tips and guidance.

<Card title="Prompt generator" icon="link" href="https://console.anthropic.com/dashboard">
  Don't have a first draft prompt? Try the prompt generator in the Claude Console!
</Card>

***

## When to prompt engineer

This guide focuses on success criteria that are controllable through prompt engineering.
Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

<Accordion title="Prompting vs. finetuning">
  Prompt engineering is far faster than other methods of model behavior control, such as finetuning, and can often yield leaps in performance in far less time. Here are some reasons to consider prompt engineering over finetuning:<br />

  * **Resource efficiency**: Fine-tuning requires high-end GPUs and large memory, while prompt engineering only needs text input, making it much more resource-friendly.
  * **Cost-effectiveness**: For cloud-based AI services, fine-tuning incurs significant costs. Prompt engineering uses the base model, which is typically cheaper.
  * **Maintaining model updates**: When providers update models, fine-tuned versions might need retraining. Prompts usually work across versions without changes.
  * **Time-saving**: Fine-tuning can take hours or even days. In contrast, prompt engineering provides nearly instantaneous results, allowing for quick problem-solving.
  * **Minimal data needs**: Fine-tuning needs substantial task-specific, labeled data, which can be scarce or expensive. Prompt engineering works with few-shot or even zero-shot learning.
  * **Flexibility & rapid iteration**: Quickly try various approaches, tweak prompts, and see immediate results. This rapid experimentation is difficult with fine-tuning.
  * **Domain adaptation**: Easily adapt models to new domains by providing domain-specific context in prompts, without retraining.
  * **Comprehension improvements**: Prompt engineering is far more effective than finetuning at helping models better understand and utilize external content such as retrieved documents
  * **Preserves general knowledge**: Fine-tuning risks catastrophic forgetting, where the model loses general knowledge. Prompt engineering maintains the model's broad capabilities.
  * **Transparency**: Prompts are human-readable, showing exactly what information the model receives. This transparency aids in understanding and debugging.
</Accordion>

***

## How to prompt engineer

The prompt engineering pages in this section have been organized from most broadly effective techniques to more specialized techniques. When troubleshooting performance, we suggest you try these techniques in order, although the actual impact of each technique will depend on your use case.

1. [Prompt generator](/en/docs/build-with-claude/prompt-engineering/prompt-generator)
2. [Be clear and direct](/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
3. [Use examples (multishot)](/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
4. [Let Claude think (chain of thought)](/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
5. [Use XML tags](/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
6. [Give Claude a role (system prompts)](/en/docs/build-with-claude/prompt-engineering/system-prompts)
7. [Prefill Claude's response](/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)
8. [Chain complex prompts](/en/docs/build-with-claude/prompt-engineering/chain-prompts)
9. [Long context tips](/en/docs/build-with-claude/prompt-engineering/long-context-tips)

***

## Prompt engineering tutorial

If you're an interactive learner, you can dive into our interactive tutorials instead!

<CardGroup cols={2}>
  <Card title="GitHub prompting tutorial" icon="link" href="https://github.com/anthropics/prompt-eng-interactive-tutorial">
    An example-filled tutorial that covers the prompt engineering concepts found in our docs.
  </Card>

  <Card title="Google Sheets prompting tutorial" icon="link" href="https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8">
    A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
  </Card>
</CardGroup>



---

**Navigation:** [← Previous](./09-pdf-support.md) | [Index](./index.md) | [Next →](./11-prefill-claudes-response-for-greater-output-contro.md)
