**Navigation:** [← Previous](./02-collections.md) | [Index](./index.md) | [Next →](./04-content-variants.md)

# Variables and expressions

Create reusable variables that can be referenced in pages and spaces

With variables you can create reusable text that can be conditionally referenced in [expressions](https://gitbook.com/docs/documentation/formatting/inline#expressions) and [conditions for adaptive content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/adapting-your-content#working-with-the-condition-editor).&#x20;

If you repeat the same name, phrase or version number multiple times within your content, you can create a **variable** to help keep all those instances in sync and accurate — which is useful if you ever need to update them, or they’re complex and often mistyped.

You can create variables that are scoped to a single page, or a single space.

### Create a new variable

To create a new variable, Click the **Variables** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FVJIUUkSBNSVvib2I7bZi%2Fvariables-dark.svg?alt=media&#x26;token=ea265cbe-43cb-4d30-8949-ccf584259eb0" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FLm9dLFUy5c3i4YOEwvSz%2Fvariables.svg?alt=media&#x26;token=ae18f815-541c-4b17-ae42-9c4d90897899" alt=""></picture> icon in the upper right corner when editing an open [change request](https://gitbook.com/docs/documentation/collaboration/change-requests). This will open the Variables side panel.

You can use the toggle at the top to view and create variables scoped either to the current page you’re on, or all pages within the current space.

Clicking **Create a variable** will launch a modal where you can give your variable a name and a value.

Click **Add variable** to save your variable.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FmyWu2r6UfxkMRCjcDZuc%2Fvariables.jpg?alt=media&#x26;token=40408b2f-bdb2-41bd-9763-bc8caf3bfd40" alt="A GitBook screenshot showing the Add variables screen. The variable Name box has been filled with the text ‘latest_version’ and the Value box has been filled with the text ‘v3.04.1’"><figcaption><p>You can add variables to a single page or an entire space. When you update the value of a variable, every instance of it will update.</p></figcaption></figure>

{% hint style="info" %}
Variable names must start with a letter, and can contain letters, numbers and underscores.
{% endhint %}

### Use variables in your content

Variables can be referenced and used within an [expression](https://gitbook.com/docs/documentation/formatting/inline#expressions) — which you can insert into your content inline. After inserting an expression, double click it to open the expression editor.

Variables defined under your page are accessible under the `page.vars` object. Similarly, variables defined across your entire space are accessible under the `space.vars` object.&#x20;

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FAYoxSMGR9BAtkV9aBszX%2Finsert-variables-expression.jpg?alt=media&#x26;token=ece25501-bfa2-4da8-82c1-f4e4f7ba3f89" alt="A GitBook screenshot showing an expression block within the editor. The expression editor is open below it and the ‘space.vars.latest_version’ variable has been selected"><figcaption><p>You can add variables to your content within expresions. The expression editor offers autocomplete options to help you find the variable you need.</p></figcaption></figure>

### Update a variable

You can update a variable at any point when within a change request. Updating its value will update the value across any expression blocks referencing it. The changed variable will go live to any published site once the change request is merged.



# Reusable content

Create reusable blocks of content that can be used across spaces, and all updated at once when you change an instance

{% hint style="info" %}
This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).
{% endhint %}

Reusable content lets you sync content across multiple pages and spaces, so you can edit all instances of the block at the same time.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FtNfvAgU9RZyYQ8JriVUu%2F04_02_25_reusable_content.svg?alt=media&#x26;token=efe90ad9-96e5-4378-b627-7c056869a280" alt="A GitBook screenshot showing reusable content"><figcaption><p>Create reusable content within a space.</p></figcaption></figure>


## Fundamentals

Reusable content works just like any other content—you can modify it via change requests, include it in review workflows, and it will render correctly on any published site.

While reusable content can be referenced across multiple spaces, it belongs to a single *parent space*.

### The "parent space" concept

The parent space is the space that owns the reusable content. It’s the only place where that content can be edited.

Even though updates to reusable content will appear instantly in all instances, all changes must originate from the parent space—either as a direct edit or through a change request.

Spaces are a core concept in GitBook, supporting both editorial workflows and security. Because GitBook enforces permission-based editing, reusable content can only be changed from its parent space. This ensures that editing rights are respected, even when the content is reused across the organization.

### Known limitations

#### Integrations

Blocks provided by integrations are not supported in reusable content. This is because integrations in GitBook are installed per space, and limiting access ensures that third-party integrations only have the permissions you grant. Referencing reusable content across spaces would break this security boundary.

#### Search

Currently, reusable content only appears in search results within its parent space. We’re actively working to remove this limitation so that reusable content shows up in search results wherever it’s referenced.


## In the app

### **Create reusable content**

To create reusable content, [select one or more blocks](https://gitbook.com/docs/documentation/blocks#selecting-blocks-and-interacting-with-selected-blocks), then open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> , select **Turn into**, and choose **Reusable content**. You can also give your block a name to make it easier to find and reuse later.

Alternatively, you can select one or more blocks and then hit **Cmd + C** to open a prompt asking if you want to create reusable content.

### **Insert reusable content**

You can insert reusable content as you would with any other block. Hit `/` on an empty line to open the **Insert palette** and search for your content by its name or simply searching for “reusable”. Alternatively, click the `+` on the left of any block or empty line.

You will also find the reusable content panel in the pages sidebar, where you can find a list of previously created content blocks in your current space.

### **Edit reusable content**

Reusable content is like any other content — you can edit any instance directly if [live edits](https://gitbook.com/docs/documentation/collaboration/live-edits) are enabled, or through [a change request](https://gitbook.com/docs/documentation/collaboration/change-requests) if not. Any changes you make will be synced everywhere the content is used.

If you’re making changes inside a change request, the content will be synced to all other instances once that change request is merged.

### **Detach reusable content**

You can detach reusable content by opening the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> and selecting **Detach**. Detaching will convert the content back to regular blocks.

Once detached, any changes you make to the block(s) will not be reflected across the other instances, and changes you make in those instances will not be reflected in the detached block(s). All other instances of the reusable content remain synced together.

### Delete reusable content

You can delete reusable content from your space entirely, if you wish. Find the reusable content in the page’s table of contents, then open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to the content you’d like to delete, and select **Delete**.

Deleting reusable content will **delete it from all pages it is used in**. This action cannot be undone.


## Syncing with GitHub & GitLab

Reusable content is fully supported when syncing to GitHub & GitLab. Your reusable content will be exported to a dedicated `includes` folder, each content being a separate Markdown file.

Your content is then referenced in your other pages using the `includes` directive.

{% hint style="info" %}
When syncing, the `.gitbook/includes` directory is created in the root of each synced space (which may not be the root of the whole repository). If your `.gitbook/includes` folder or its files appear in your space’s table of contents, you may need to hide them manually from the TOC.
{% endhint %}

#### Example

{% hint style="success" %}
If you're writing on the GitHub side, ensure the path to the include is relative to the file containing the reference (not the root of the repository).
{% endhint %}

```markdown
{% include "../../.gitbook/includes/reusable-block.md" %}
```



# Searching internal content

Find what you’re looking for faster with keyword search and AI-powered smart search

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FeqdESbrmoMR2WU0gAfG4%2Fcreating-content-searching-content.svg?alt=media&#x26;token=83d18fbb-6c55-4e7d-8a91-7ad088c8c646" alt="A GitBook screenshot showing the search bar"><figcaption><p>Ask questions or search through your content using the built in search bar.</p></figcaption></figure>

Whether you’re working within the GitBook app or your visitors are reading your published content, GitBook’s search functions help to make it easy to find what you’re looking for.

You can use quick find to look for specific words or phrases, or you can ask GitBook AI a question. It’ll scan through your docs and summarize an answer in seconds, with references to help you find out more.

{% hint style="success" %}

### Global search

If you’re publishing your documentation on [an Ultimate site plan](https://gitbook.com/docs/documentation/account-management/plans#site-plans), and add multiple spaces as [site sections](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections), your users will be able to use the **Ask or search** bar to find information across all your site sections.
{% endhint %}



# Search & Quick find

Search and navigate your documentation fast with quick find.

GitBook’s **Quick find** palette lets you search for content across all your organizations, and jump between them fast.

### Use Quick find

**​**You can open the **Quick find** palette by hitting the **Quick find** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FsR35vdoNcYMz1KzmQ8hM%2Fquick-find-1.svg?alt=media&#x26;token=ecb2b113-b737-4fd9-b5f1-730343a78332" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnAIpi7l7NOqFoTvAx11%2Fquick-find.svg?alt=media&#x26;token=7b2c5f2d-04d7-44de-9751-3a985679c2a1" alt=""></picture> button at the top of the sidebar or by pressing **⌘ + K** on Mac or **Ctrl + K** on PC.

### Search results <a href="#display-of-results" id="display-of-results"></a>

Results from the space you’re currently in appear at the top, followed by results from other spaces from the organization you’re currently working in — **as well as other organizations** you are a member of.

When you select a search result from an organization, you’ll switch to browsing that organization. To go back, use quick find to select a document in the organization you were in before, or use [the organization switcher](https://gitbook.com/docs/documentation/resources/gitbook-ui#the-sidebar) in the sidebar.

{% hint style="info" %}
We do not currently support the ability to prioritize certain content in Quick find results.
{% endhint %}

### Permissions <a href="#team-permissions" id="team-permissions"></a>

**Quick find** is compliant with your team’s permission settings, meaning that users will only be able to search the content they have permission to access.‌

### Content indexing <a href="#indexation" id="indexation"></a>

We index your content by grouping it into sections. Sections are denoted using [H1, H2 or H3 Headings](https://gitbook.com/docs/documentation/creating-content/blocks/heading), with the content that follows them forming part a section.

Each result shows the first three lines of information below the section header. If your section is too big,  your keyword match may not appear in the preview — but don’t worry, quick find still found a match!



# GitBook AI

GitBook uses AI to help you find the knowledge you need within your organization, faster

When engaging with GitBook AI, you have the ability to ask questions or elaborate on specific requirements. This AI-driven tool is designed to review your documentation in real-time, providing you with quick, direct answers.

{% hint style="info" %}
GitBook AI search is available both within the GitBook app to search internal content, and [in published content to search that specific docs site](https://gitbook.com/docs/documentation/publishing-documentation/ai-search).&#x20;
{% endhint %}


## GitBook AI helps you find answers in the GitBook app

{% hint style="info" %}
This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).
{% endhint %}

You can enable GitBook AI for your organization’s internal content, allowing you to ask questions and get semantic answers about your internal knowledge base.&#x20;

Head to the **Organization settings** page and, in the **General** tab, toggle the **Enable GitBook AI** setting on.

### Using GitBook AI search <a href="#how-do-i-use-gitbook-ai" id="how-do-i-use-gitbook-ai"></a>

Once GitBook AI is enabled, open the **Ask or search** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FsR35vdoNcYMz1KzmQ8hM%2Fquick-find-1.svg?alt=media&#x26;token=ecb2b113-b737-4fd9-b5f1-730343a78332" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnAIpi7l7NOqFoTvAx11%2Fquick-find.svg?alt=media&#x26;token=7b2c5f2d-04d7-44de-9751-3a985679c2a1" alt=""></picture> menu from the left sidebar and simply type out a question. GitBook AI will take a few seconds to scan your documentation and summarize the results.

### FAQs

#### How long does it take for GitBook AI to index changes?

When someone makes a change to your content — such as a merged [change request](https://gitbook.com/docs/documentation/collaboration/change-requests) — it can take **up to one hour** for GitBook to index the changes to and reflect them in AI search results.

#### How does GitBook AI handle my data?

We pass your content to OpenAI to index and process data. OpenAI **does not** use this content for service improvements (including model training). You can find out more about how OpenAI handles data [here](https://openai.com/blog/introducing-chatgpt-and-whisper-apis#developer-focus).

#### How do I prevent hallucinations with GitBook AI search?

If you’re seeing GitBook produce answers that are incorrect, the best method for correcting this is write explicit content around the topic so the AI does not have to guess.



# Writing with GitBook AI

Use GitBook AI to generate and build content for your page

{% hint style="info" %}
This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).
{% endhint %}

You can use GitBook AI to create content on any empty line on your page. It can create all kinds of content — formatted in Markdown — including code samples, templates, page summaries and more.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FeeahKyRVALviZl7n9U4u%2Fcreating-content-writing-with-gitbook-ai.svg?alt=media&#x26;token=045cabaa-36df-42a5-adc4-7eaf69092e29" alt="A GitBook screenshot showing the AI writing options"><figcaption><p>Write with GitBook AI.</p></figcaption></figure>

### Write with GitBook AI

Press `Space` on any empty line, or type `/` and choose **Write with AI** to enter GitBook AI’s writing mode.

You can instantly start typing any prompt you want. GitBook AI will analyze the prompt and generate content based on it. For example:

> Write me a two-paragraph overview of why documentation is important for product teams.

Alternatively, you can also choose from one of the suggested prompts or prompt starters:

#### Continue writing

If you click this option, GitBook AI will analyze the content on your current page and then generate more content based on that.

#### Explain…

Click this and then tell GitBook AI what you want it to explain. This isn’t limited by content on your page, so you can ask it to explain anything at all.

#### Summarize

As you can imagine, this option will summarize all the content on your page — great for writing a TL;DR at the bottom of a detailed document, or adding a quick summary at the top for people just checking in.

#### Explain this

This will break down the complex information on your page and explain it in simpler language — including explaining acronyms and other jargon. This is perfect if the page you’re reading involves a lot of complex information, or you want to add an explainer for less technical folks.

#### Translate

This mode will translate your current page into one of a set number of languages. If you want to translate into a language that’s not on the list, simply type it into the prompt box.

### FAQs

<details>

<summary>How does GitBook AI use my data?</summary>

We always follow [our data protection practices](https://gitbook.com/docs/policies/privacy-and-security/statement) to keep your data private.

GitBook AI does not use your data to train AI models. We will only share the information you add to GitBook AI with OpenAI for the sole purpose of providing you with GitBook AI’s features. Take a look at [OpenAI’s privacy policy](https://openai.com/enterprise-privacy) for more information.

</details>

<details>

<summary>How much does GitBook AI cost?</summary>

GitBook AI is available as part of GitBook’s Pro and Enterprise plans. If you have a Free or Plus plan, you’ll need to upgrade to use GitBook AI writing and editing. [Visit our pricing page](https://www.gitbook.com/pricing) to find out more about upgrading to Pro.

</details>



# Version control

Keep track of changes, roll back to a previous version and more

You can easily monitor all the changes people have made to your content using to the **Version history** side panel.

### Version history <a href="#see-the-activity-of-a-specific-draft" id="see-the-activity-of-a-specific-draft"></a>

In the Version history of a space, you can see a list of all the actions that changed the content within it. These include:

* When someone made [live edits](https://gitbook.com/docs/documentation/collaboration/live-edits) to the space.
* When someone merged a [change request](https://gitbook.com/docs/documentation/collaboration/change-requests).
* When someone performed a [Git Sync](https://gitbook.com/docs/documentation/getting-started/git-sync) operation.

### View historical versions of content

To view past versions of your content and see the changes that were made, click the **Version history** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F1Ntpa0YjoayuQOU0zbXt%2Fhistory%20-%20dark.svg?alt=media&#x26;token=a3d28850-951f-4a24-b4da-a44fe00b1319" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FVEyYlyeOFMIwGJkpdIWh%2Fhistory.svg?alt=media&#x26;token=60e30952-2289-4eec-b185-bcc7308347af" alt="The Version history icon in GitBook"></picture> button in the [space header](https://gitbook.com/docs/documentation/resources/gitbook-ui#space-header), or open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fpn5vEw7bYFrMPpdyvpSu%2Factions-horizontal%20-%20dark.svg?alt=media&#x26;token=ec39eefe-a391-4fe2-828a-082b79f2847d" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture> next to the space or change request title and choose **Version history**.

Click on any item in the list to see how your content looked at the point this change was made. This is very similar to how you view [change requests](https://gitbook.com/docs/documentation/collaboration/change-requests).

### Show changes

When you are viewing an old version of your content, you can choose to highlight the differences between the old and current content — similar to [diff view in a change request](https://gitbook.com/docs/documentation/collaboration/change-requests#diff-mode).

To enable or disable this, use the **Show changes** toggle at the bottom of the **Version history** side panel.

With show changes enabled, content that has changed will be highlighted by an icon on the left of its content block.

### Viewing historical published versions

If you're investigating the version history of a published space, you can also view previews of what the previous versions looked like in the published context (i.e. what the end user would see).

You can do this by:

{% stepper %}
{% step %}
From the version history side panel, select the revision
{% endstep %}

{% step %}
Copy the ID at the end of the URL
{% endstep %}

{% step %}
Add it at the end of your published docs URL as `/~/revisions/<id>`
{% endstep %}
{% endstepper %}

### Roll back to a previous version

Rolling back allows you to revert a space’s content to the way it was at a previous point in time. This is helpful if you’ve accidentally made a breaking change or deleted content and need to quickly get back to a previous version of the space.

To roll back to a previous version of your space, hover over the version in the side panel, click the **Actions button** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> and select **Rollback**.



# Translations

Auto-translate your content into multiple languages using AI and keep it synced.

{% hint style="warning" %}
Auto translations are currently in Beta. Let us know if you have any feedback or encounter any issues.
{% endhint %}

Auto translations make it easy to keep your documentation up-to-date in multiple languages, with minimal manual effort. You can create a space as a translation of another, and let AI handle the rest.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FqNWM1B8mSQTFFsJYm4cD%2F15_08_25_auto_translations.svg?alt=media&#x26;token=4c999b80-a46d-4756-a705-cd23ea07ae2d" alt=""><figcaption></figcaption></figure>


## How translations work

* **Create a translation space:** Set up a new space as a translation of an existing one. Choose your source space and target language.
* **Continuous updates:** Every time you make changes to the source content, the translation workflow only runs for the **pages that have been changed**.
* **Automatic sync:** After changes are merged, the translation workflow **runs automatically** and syncs with its source, so your translated space always reflects the latest updates.


## Set up an auto translation

To translate a space to a new language, start by creating a new [space](https://gitbook.com/docs/documentation/content-structure/space#create-a-space) in your organization. From the modal that appears, click “Translation” from the quick actions menu.

From the modal that appears, you’ll need to choose a:

* Source
* Source language
* Target language

These options will be used to translate your space into a duplicated, translated space in your organization. You’ll also see a quick overview on the cost of translating your space.

### Advanced configuration

**Custom AI instructions:** Add advanced instructions to guide the AI on tone of voice, style, or other preferences. This helps ensure your translations match your brand or audience.

{% hint style="info" %}
Adding custom instructions to your translation workflow can be helpful, but is limited in certain cases.

Custom instructions cannot be used to create new elements on a translated space, add extra text, or change the structure of the source content.
{% endhint %}

**Glossary support:** Define a glossary to control how specific terms are translated. This keeps terminology consistent across all supported languages.

{% hint style="warning" %}
**Changing your glossary will trigger a full re-translation of your content**. There is currently no workaround: we cannot reliably detect which pages might contain a glossary keyword, so the safest approach is to re-translate all pages. Updating the glossary may therefore be time- and cost-intensive.
{% endhint %}


## Add a translation to a variant

After creating a translation, you’ll be able to add it to published docs site as a [variant](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/variants). This will allow users to toggle between languages in the upper right corner when viewing your main docs site.

{% hint style="info" %}
To provide the best experience for your users, you’re able to set the default language of a variant when setting it in your settings.

It’s best practice to add the language of your translated space when setting up your variant.
{% endhint %}

Head to your site settings, under the structure tab to set up a new variant for any translations you have.


## Pricing

Translations are a paying **monthly** add-on:

* $25 for up to 50,000 translated words
* $0.20 per additional 1,000 words

Each month includes 50,000 words of translation for $25. After that, every additional 1,000 words costs $0.20. Your 50,000-word allowance resets at the start of each month.

In your first translation, every word will count towards your bill. After that, only new or updated words are charged. For example, if you edit your docs later, only the new words in the changed text will count towards your word limit — you won’t be re-billed for the entire document.


## FAQ

<details>

<summary>Why use auto-translations?</summary>

* **Effortless multilingual docs:** Reach a global audience without manual translation work.
* **Smart updates:** Only changed pages are re-translated, saving time and resources.
* **Full control:** Customize translations with advanced instructions and glossary management.

</details>

<details>

<summary>Can I edit the translation?</summary>

You currently can't edit translations.

As translations are done as a pure transformation of the source content, we can't reconcile potential edits made on the translation result with a new translation.

To workaround it, we recommend the following flow:

* Use the glossary to define specific translations that you want the AI to use
* Use the custom instructions to iterate on the output

</details>

<details>

<summary>How many translations do I need to create?</summary>

You should only create **one translation workflow per language** of any given source content. Creating multiple workflows will accrue extra, duplicated costs in your organization.

</details>

<details>

<summary>What are some current limitations?</summary>

* Translations do not localize UI elements in your variant automatically. Head to your site’s customization settings to [localize the interface](https://gitbook.com/docs/documentation/publishing-documentation/customization/extra-configuration#localize-user-interface) for a [specific variant](https://gitbook.com/docs/documentation/publishing-documentation/customization#customizing-sites-with-multiple-sections).
  * This includes user-input customizations, such as announcement banners.
* Translations cannot add extra content to the page - like a hint or a banner noting that a page was translated by AI. Consider adding an extra page in the translated space to note this, or the [announcement banner](https://gitbook.com/docs/documentation/publishing-documentation/customization/layout-and-structure#announcement-premium-and-ultimate) in your site variant.
* Changing the glossary triggers a full re-translation of all pages, which can increase processing time and cost. There is no partial re-translation based on glossary usage at this time.

</details>

If you need help getting started or want to learn more about configuring auto-translations, [contact our support team](https://gitbook.com/docs/help-center/further-help/how-do-i-contact-support).



# OpenAPI

Add an OpenAPI spec to a page and let your users test endpoints right on the page with interactive blocks.

Manually writing REST API documentation can be a time-consuming process. Fortunately, GitBook streamlines this task by allowing you to import OpenAPI documents, which detail your API’s structure and functionality.

The OpenAPI Specification (OAS) is a framework that developers use to document REST APIs. Written in JSON or YAML, it outlines all your endpoints, parameters, schemas, and authentication schemes.

Once imported into GitBook, these documents are transformed into interactive and testable API blocks that visually represent your API methods—whether the specification is provided as a file or loaded from a URL.

GitBook supports [Swagger 2.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md) or [OpenAPI 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md) compliant files.

{% openapi src="<https://petstore3.swagger.io/api/v3/openapi.json>" path="/pet" method="post" %}
<https://petstore3.swagger.io/api/v3/openapi.json>
{% endopenapi %}

### Test it (powered by Scalar)

GitBook's OpenAPI block also supports a "test it" functionality, which allows your users to test your API methods with data and parameters filled in from the editor.

Powered by [Scalar](https://scalar.com/), you won't need to leave the docs in order to see your API methods in action. See and example of this above.

#### FAQ

<details>

<summary>Why isn’t my spec loading?</summary>

If you can’t fetch the spec, your API is likely blocking cross-origin requests (CORS).  Please check your API’s response headers for: [`Access-Control-Allow-Origin: *`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) . If your API only allows specific origins, ensure that `*.gitbook.io` is permitted.

</details>



# Add an OpenAPI specification

Learn how to add and update an OpenAPI specification in GitBook application or from CLI.

If you have an OpenAPI spec, you can add it to your organization by uploading the file directly, linking to a hosted URL, or using the [GitBook CLI](https://gitbook.com/docs/developers/integrations/reference).

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FtQWk9u72H5YJX3Z0zpKG%2F02_04_25_add_api_spec.svg?alt=media&#x26;token=be82c2fa-7bed-419e-8172-44c5f72d09d5" alt="A GitBook screenshot showing the modal for generating API docs automatically"><figcaption></figcaption></figure>

### How to add a specification

1. Open the **OpenAPI** section in the sidebar
2. Click on **Add specification**
3. Give your specification a name. This helps identify it, especially if you manage multiple specs
4. Choose one of the following:
   * Upload a file (e.g. *openapi.yaml*)
   * Enter a URL to a hosted spec
   * Use the CLI to publish the spec

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FXHNiXo25u5A0fWdIRplr%2F03_04_25_api_spec_modal.svg?alt=media&#x26;token=ffc212b7-3be9-4df2-8da8-f6f2928f4c53" alt="A GitBook screenshot showing the Add an OpenAPI specification modal"><figcaption><p>Add an OpenAPI specification modal.</p></figcaption></figure>

### Update your specification

You can update your OpenAPI specification at any time using the GitBook UI or the CLI, regardless of how it was initially added.

#### In GitBook Application

In the OpenAPI panel:

* If your spec is linked to a URL:
  * GitBook checks for updates automatically **every 6 hours**.
  * To fetch updates immediately, click **Check for updates**.
* If your spec was uploaded as a file:
  * Click **Update** to upload a new version.
* You can switch from a File to a URL source by clicking on **Edit** in the breadcrumb actions menu.

#### Using the CLI

Use the same command to update your specification:

```bash
gitbook openapi publish --spec api-spec-name --organization organization_id <path-or-url>
```

You can also use the CLI to **Check for updates** by running the publish command on the same URL.

Read our [support-for-ci-cd-with-api-blocks](https://gitbook.com/docs/documentation/api-references/guides/support-for-ci-cd-with-api-blocks "mention") guide to learn how to automate the update of your specification.



# Insert API reference in your docs

Insert complete API reference from your OpenAPI spec or pick individual operation or schemas.

GitBook allows you to automatically generate pages related to the endpoints you have in your OpenAPI spec. These pages will contain OpenAPI operation blocks, allowing you and your visitors to test your endpoints and explore them further based on the information found in the spec.

{% hint style="success" %}
Endpoints added from your spec will continue to be updated anytime your spec is updated. See the [Update your specification](https://gitbook.com/docs/documentation/api-references/add-an-openapi-specification#update-your-specification) section for more info.
{% endhint %}

### Automatically create OpenAPI pages from your spec

After you’ve [added your OpenAPI spec](https://gitbook.com/docs/documentation/api-references/openapi/add-an-openapi-specification), you can generate endpoint pages by inserting an **OpenAPI Reference** in the table of contents of a Space.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FY5JiiQnDpjYVY50vq8xn%2F03_04_25_create_api_pages.svg?alt=media&#x26;token=e79084f5-f3e7-4dad-8e7f-c4b90767199e" alt="A GitBook screenshot showing how to insert API references into the table of contents of a space"><figcaption><p>Insert API References in the table of contents of a Space.</p></figcaption></figure>

{% stepper %}
{% step %}

#### Generate pages from OpenAPI

In the space you’d like to generate endpoint pages, click the **Add new\...** button from the bottom of your space’s [table of contents](https://gitbook.com/docs/documentation/resources/gitbook-ui#table-of-contents).

From here, click **OpenAPI Reference**.
{% endstep %}

{% step %}

#### Choose your OpenAPI spec

Choose your previously uploaded OpenAPI spec, and click **Insert** to automatically add your endpoints to your space. You can optionally choose to add a models page referencing all your OpenAPI schemas.
{% endstep %}

{% step %}

#### Manage your API operations

GitBook will automatically generate pages based on your OpenAPI spec and the tags set inside it’s definition.

Head to [structuring-your-api-reference](https://gitbook.com/docs/documentation/api-references/guides/structuring-your-api-reference "mention") to learn more about organizing your operations through your OpenAPI spec.
{% endstep %}
{% endstepper %}

### Add an individual OpenAPI block

Alternatively, you can add OpenAPI operations or schemas from your spec individually to pages throughout your docs.

{% stepper %}
{% step %}

#### Add a new OpenAPI block

Open the block selector by pressing **/**, and search for OpenAPI.
{% endstep %}

{% step %}

#### Choose your OpenAPI spec

Choose your previously uploaded OpenAPI spec, and click **Continue** to choose your the endpoints you’d like to use.
{% endstep %}

{% step %}

#### Choose the operations or schemas you’d like to insert

Pick the operations and the schemas you want to insert in your docs and click **Insert**.
{% endstep %}
{% endstepper %}



# Guides



# Structuring your API reference

Learn how to structure your API reference across multiple pages with icons and descriptions.

GitBook does more than just render your OpenAPI spec. It lets you customize your API reference for better clarity, navigation, and branding.

### Split operations across multiple pages

To keep your documentation organized, GitBook can split your API operations into separate pages. Each page is generated from a tag in your OpenAPI spec. To group operations into a page, assign the same tag to each operation:

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">paths:
  /pet:
    put:
<strong>      tags:
</strong><strong>        - pet
</strong>      summary: Update an existing pet.
      description: Update an existing pet by Id.
      operationId: updatePet
</code></pre>

### Reorder pages in your table of contents

The order of pages in GitBook matches the order of tags in your OpenAPI tags array:

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">tags:
<strong>  - name: pet
</strong><strong>  - name: store
</strong><strong>  - name: user
</strong></code></pre>

### Nest pages into groups

To build multi-level navigation, use `x-parent` (or `parent`) in tags to define hierarchy:

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">tags:
  - name: everything
  - name: pet
<strong>    x-parent: everything
</strong>  - name: store
<strong>    x-parent: everything
</strong></code></pre>

The above example will create a table of contents that looks like:

```
Everything
├── Pet
└── Store
```

If a page has no description, GitBook will automatically show a card-based layout for its sub-pages.

### Customize page titles, icons, and descriptions

You can enhance pages with titles, icons, and descriptions using custom extensions in the tags section. All [Font Awesome icons](https://fontawesome.com/search) are supported via `x-page-icon`.

{% code title="openapi.yaml" %}

```yaml
tags:
  - name: pet
    # Page title displayed in table of contents and page
    -x-page-title: Pet
    # Icon shown in table of contents and next to page title
    -x-page-icon: dog
    # Description shown just above the title
    -x-page-description: Pets are amazing!
    # Content of the page
    description: Everything about your Pets
```

{% endcode %}

### Build rich descriptions with GitBook Blocks

Tag description fields support GitBook markdown, including [advanced blocks](https://gitbook.com/docs/documentation/creating-content/blocks) like tabs:

{% code title="openapi.yaml" %}

```yaml
---
tags:
  - name: pet
    description: |
      Here is the detail of pets.

      {% tabs %}
      {% tab title="Dog" %}
      Here are the dogs
      {% endtab %}

      {% tab title="Cat" %}
      Here are the cats
      {% endtab %}

      {% tab title="Rabbit" %}
      Here are the rabbits
      {% endtab %}
      {% endtabs %}
```

{% endcode %}

### Highlight schemas

You can highlight a schema in a GitBook description by using GitBook markdown. Here is an example that highlights the “Pet” schema from the “petstore” specification:

{% code title="openapi.yaml" %}

```yaml
---
tags:
  - name: pet
      description: |
          {% openapi-schemas spec="petstore" schemas="Pet" grouped="false" %}
              The Pet object
          {% endopenapi-schemas %}
```

{% endcode %}

### Document a webhook endpoint

GitBook also supports documenting webhook endpoints when using OpenAPI 3.1.

You can define your webhooks directly in your OpenAPI file using the `webhooks` field, which works similarly to `paths` for regular API endpoints:

{% code title="openapi.yaml" %}

```yaml
---
openapi: 3.1.0 # Webhooks are available starting from OpenAPI 3.1

webhooks:
  newPet:
    post:
      summary: New pet event
      description: Information about a new pet in the system
      requestBody:
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Pet"
      responses:
        "200":
          description: Return a 200 status to indicate that the data was received successfully
```

{% endcode %}



# Adding custom code samples

Learn how to configure custom code samples to display alongside your API endpoints.

GitBook can automatically generate generic code examples for each API operation. If you’d prefer to showcase custom or more detailed snippets, add `x-codeSamples` to your OpenAPI definition. This way, you control how your endpoints are demonstrated and can offer language or SDK-specific examples.

{% code title="openapi.yaml" %}

```yaml
paths:
  /users:
    get:
      summary: Retrieve users
      x-codeSamples:
        - lang: JavaScript
          label: Node SDK
          source: |
            import { createAPIClient } from 'my-api-sdk';

            const client = createAPIClient({ apiKey: 'my-api-key' });
            client.users.list().then(users => {
              console.log(users);
            });
        - lang: Java
          label: Java SDK
          source: |
            MyApiClient client = new MyApiClient("my-api-key");
            List<User> users = client.getUsers();
            System.out.println(users);
```

{% endcode %}

**Key Points**

* `x-codeSamples` is an array of code sample objects.
* Each object defines:
  * `lang`: The language of the code (e.g., JavaScript, Java).
  * `label`: A short label for the code block.
  * `source`: The actual code snippet.



# Managing API operations

Learn how to mark an OpenAPI API operation as experimental, deprecated or hide it from your documentation.

It’s common to have operations that are not fully stable yet or that need to be phased out. GitBook supports several OpenAPI extensions to help you manage these scenarios.

### Marking operation as experimental, alpha, or beta

Use `x-stability` to communicate that an endpoint is unstable or in progress. It helps users avoid non-production-ready endpoints. Supported values: `experimental`, `alpha`, `beta`.

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">paths:
  /pet:
    put:
      operationId: updatePet
<strong>      x-stability: experimental
</strong></code></pre>

### Deprecating an operation

To mark an operation as deprecated, add the `deprecated: true` attribute.

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">paths:
  /pet:
    put:
      operationId: updatePet
<strong>      deprecated: true
</strong></code></pre>

Optionally specify when support ends by including `x-deprecated-sunset`&#x20;

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">paths:
  /pet:
    put:
      operationId: updatePet
<strong>      deprecated: true
</strong><strong>      x-deprecated-sunset: 2030-12-05
</strong></code></pre>

### Hiding an operation from the API reference

To hide an operation from your API reference, add `x-internal: true` or `x-gitbook-ignore: true` attribute.

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">paths:
  /pet:
    put:
      operationId: updatePet
<strong>      x-internal: true
</strong></code></pre>

### Hiding a response sample

Add the `x-hideSample: true` attribute to a response object to exclude it from the response samples section.

<pre class="language-yaml" data-title="openapi.yaml"><code class="lang-yaml">paths:
  /pet:
    put:
      operationId: updatePet
<strong>      responses:
</strong><strong>        200:
</strong><strong>          x-hideSample: true
</strong></code></pre>



# Configuring the “Test it” button

You can configure the "Test It" button and accompanying window in GitBook using several OpenAPI extensions. These extensions can help improve and configure the testing suite for users.

### Hiding the “Test it” button

You can hide the “Test it” button from your endpoints by adding the `x-hideTryItPanel` to an endpoint, or at the root of your OpenAPI spec.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      x-hideTryItPanel: true
```

{% endcode %}

### Enable authentication in the testing window

The request runner can only present and apply auth if your spec declares it. Define schemes under `components.securitySchemes`, then attach them either globally via `security` (applies to all operations) or per-operation (overrides global).

#### Declare your auth scheme

Below are common patterns. Use straight quotes in YAML.

{% tabs %}
{% tab title="HTTP Bearer (e.g., JWT)" %}

```yaml
openapi: '3.0.3'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

{% endtab %}

{% tab title="API Key in header" %}

```yaml
openapi: '3.0.3'
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
```

{% endtab %}

{% tab title="OAuth2 (authorizationCode)" %}

```yaml
openapi: '3.0.3'
components:
  securitySchemes:
    oauth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: 'https://auth.example.com/oauth/authorize'
          tokenUrl: 'https://auth.example.com/oauth/token'
          scopes:
            read:items: 'Read items'
            write:items: 'Write items'
```

{% endtab %}
{% endtabs %}

#### Apply schemes globally or per operation

{% tabs %}
{% tab title="Gloabl" %}

```yaml
openapi: '3.0.3'
security:
  - bearerAuth: []
paths: ...
```

{% endtab %}

{% tab title="Per-operation" %}

```yaml
paths:
  /reports:
    get:
      summary: Get reports
      security:
        - apiKeyAuth: []
      responses:
        '200':
          description: OK
```

{% endtab %}
{% endtabs %}

### Control the endpoint URL with `servers`

The request runner targets the URL(s) you define in the `servers` array. Declare one or more servers; you can also parameterize them with variables.

{% tabs %}
{% tab title="Single server" %}

```yaml
openapi: '3.0.3'
servers:
  - url: https://instance.api.region.example.cloud
```

{% endtab %}

{% tab title="Multiple servers" %}

```yaml
servers:
  - url: https://api.example.com
    description: Production
  - url: https://staging-api.example.com
    description: Staging
```

{% endtab %}

{% tab title="Server variables" %}

```yaml
servers:
  - url: https://{instance}.api.{region}.example.cloud
    variables:
      instance:
        default: acme
        description: Your tenant or instance slug
      region:
        default: eu
        enum:
          - eu
          - us
          - ap
        description: Regional deployment
```

{% endtab %}

{% tab title="Per-operation servers" %}

<pre class="language-yaml"><code class="lang-yaml"><strong>paths:
</strong>  /reports:
    get:
      summary: Get reports
      servers:
        - url: https://reports.api.example.com
      responses:
        '200':
          description: OK
</code></pre>

{% endtab %}
{% endtabs %}



# Describing enums

Learn how to add descriptions to enums.

When an API operation includes an enum, you can add `x-enumDescriptions` to provide more context about each option. GitBook will display the enum values and their descriptions in a table next to the operation.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
components:
  schemas:
    project_status:
      type: string
      enum:
        - LIVE
        - PENDING
        - REJECTED
      x-enumDescriptions:
        LIVE: The project is live.
        PENDING: The project is pending approval.
        REJECTED: The project was rejected.
```

{% endcode %}



# Integrating with CI/CD

Learn how to automate the update of your OpenAPI specification in GitBook.

GitBook can work with any CI/CD pipeline you already have for managing your OpenAPI specification. By using the GitBook CLI, you can automate updates to your API reference.

### Upload a specification file

If your OpenAPI spec is generated during your CI process, you can upload it directly from your build environment:

```bash

# Set your GitBook API token as an environment variable
export GITBOOK_TOKEN=<api-token>

gitbook openapi publish \
  --spec spec_name \
  --organization organization_id \
  example.openapi.yaml
```

### Set a new source URL or trigger a refresh

If your OpenAPI specification is hosted at a URL, GitBook automatically checks for updates. To force an update (for example, after a release), run:

```bash

# Set your GitBook API token as an environment variable
export GITBOOK_TOKEN=<api-token>

gitbook openapi publish \
  --spec spec_name \
  --organization organization_id \
  https://api.example.com/openapi.yaml
```

### Update your spec with GitHub Actions

If you’re setting up a workflow to publish your OpenAPI spec, complete these steps in your repository:

1. In your repo, go to “Settings → Secrets and variables → Actions”.
2. Add a secret: `GITBOOK_TOKEN` (your GitBook API token).
3. Add variables (or hardcode them in the workflow):
   * `GITBOOK_SPEC_NAME` → your spec’s name in GitBook
   * `GITBOOK_ORGANIZATION_ID` → your GitBook organization ID
4. Save the workflow file as `.github/workflows/gitbook-openapi-publish.yml`.
5. Push changes to “main” (or run the workflow manually).

You can then use this action to update your spec:

{% code title=".github/workflows/gitbook-openapi-publish.yml" %}

```yaml
name: Publish OpenAPI to GitBook

on:
  push:
    branches: [ "main" ]
    paths:
      - "**/*.yaml"
      - "**/*.yml"
      - "**/*.json"
  workflow_dispatch:

jobs:
  publish:
    runs-on: ubuntu-latest
    env:
      # Required secret
      GITBOOK_TOKEN: ${{ secrets.GITBOOK_TOKEN }}
      # Prefer repo/org variables; fallback to inline strings if you like
      GITBOOK_SPEC_NAME: ${{ vars.GITBOOK_SPEC_NAME }}
      GITBOOK_ORGANIZATION_ID: ${{ vars.GITBOOK_ORGANIZATION_ID }}

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Publish spec file to GitBook
        run: |
          npx -y @gitbook/cli@latest openapi publish \
            --spec "$GITBOOK_SPEC_NAME" \
            --organization "$GITBOOK_ORGANIZATION_ID" \
            <path_to_spec>
```

{% endcode %}



# Extensions reference

The complete reference of OpenAPI extensions supported by GitBook.

You can enhance your OpenAPI specification using extensions—custom fields that start with the `x-` prefix. These extensions let you add extra information and tailor your API documentation to suit different needs.

GitBook allows you to adjust how your API looks and works on your published site through a range of different extensions you can add to your OpenAPI spec.&#x20;

Head to our [guides section](https://gitbook.com/docs/documentation/api-references/guides) to learn more about using OpenAPI extensions to configure your documentation.

<details>

<summary><code>x-page-title | x-displayName</code></summary>

Change the display name of a tag used in the navigation and page title.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags:
  - name: users
    x-page-title: Users
```

{% endcode %}

</details>

<details>

<summary><code>x-page-description</code></summary>

Add a description to the page.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags:
  - name: "users"
    x-page-title: "Users"
    x-page-description: "Manage user accounts and profiles."
```

{% endcode %}

</details>

<details>

<summary><code>x-page-icon</code></summary>

Add a Font Awesome icon to the page. See available icons [here](https://fontawesome.com/search).

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags:
  - name: "users"
    x-page-title: "Users"
    x-page-description: "Manage user accounts and profiles."
    x-page-icon: "user"
```

{% endcode %}

</details>

<details>

<summary><code>x-parent | parent</code></summary>

Add hierarchy to tags to organize your pages in GitBook.&#x20;

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags:
  - name: organization
  - name: admin
    x-parent: organization
  - name: user
    x-parent: organization
```

{% endcode %}

</details>

<details>

<summary><code>x-hideTryItPanel</code></summary>

Show or hide the “Test it” button for an OpenAPI block.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      x-hideTryItPanel: true
```

{% endcode %}

</details>

<details>

<summary><code>x-codeSamples</code></summary>

Show, hide, or include custom code samples for an OpenAPI block.

#### Fields

<table><thead><tr><th width="103.625">Field Name</th><th width="88.07421875" align="center">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>lang</code></td><td align="center">string</td><td>Code sample language. Value should be one of the following <a href="https://github.com/github/linguist/blob/master/lib/linguist/popular.yml">list</a></td></tr><tr><td><code>label</code></td><td align="center">string</td><td>Code sample label, for example <code>Node</code> or <code>Python2.7</code>, <em>optional</em>, <code>lang</code> is used by default</td></tr><tr><td><code>source</code></td><td align="center">string</td><td>Code sample source code</td></tr></tbody></table>

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      x-codeSamples:
        - lang: 'cURL'
          label: 'CLI'
          source: |
            curl -L \
            -H 'Authorization: Bearer <token>' \
            'https://api.gitbook.com/v1/user'
```

{% endcode %}

</details>

<details>

<summary><code>x-enumDescriptions</code></summary>

Add an individual description for each of the `enum` values in your schema.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
components:
  schemas:
    project_status:
      type: string
      enum:
        - LIVE
        - PENDING
        - REJECTED
      x-enumDescriptions:
        LIVE: The project is live.
        PENDING: The project is pending approval.
        REJECTED: The project was rejected.
```

{% endcode %}

</details>

<details>

<summary><code>x-internal | x-gitbook-ignore</code></summary>

Hide an endpoint from your API reference.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      x-internal: true
```

{% endcode %}

</details>

<details>

<summary><code>x-stability</code></summary>

Mark endpoints that are unstable or in progress.&#x20;

Supported values: `experimental`, `alpha`, `beta`.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      x-stability: experimental
```

{% endcode %}

</details>

<details>

<summary><code>deprecated</code></summary>

Mark whether an endpoint is deprecated or not. Deprecated endpoints will give deprecation warnings in your published site.

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      deprecated: true
```

{% endcode %}

</details>

<details>

<summary><code>x-deprecated-sunset</code></summary>

Add a sunset date to a deprecated operation.&#x20;

Supported values: **ISO 8601** format (YYYY-MM-DD)

{% code title="openapi.yaml" %}

```yaml
openapi: '3.0'
info: ...
tags: [...]
paths:
  /example:
    get:
      summary: Example summary
      description: Example description
      operationId: examplePath
      responses: [...]
      parameters: [...]
      deprecated: true
      x-deprecated-sunset: 2030-12-05
```

{% endcode %}

</details>



# Publish a docs site

Publish your documentation to the internet as a docs site

Once you’ve finished writing, editing, or importing your content, you can publish your work to the web as a docs site. Your docs will be published on the web and available to your selected audience.

The content on your site comes from [spaces](https://gitbook.com/docs/documentation/creating-content/content-structure/space) in your organization. When you create a new docs site, you can create a new space, or link an existing one.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FMHFgq8cFWJlX99QPv02O%2F18_07_25_publishing-documentation-publish-docs.svg?alt=media&#x26;token=832dc431-6ae1-4f14-ae63-0b3b9d98ac99" alt="A GitBook screenshot showing the docs sites homepage"><figcaption><p>GitBook's docs sites homepage.</p></figcaption></figure>

### Create a docs site

To create a docs site, click the plus **+** icon next to Docs site in the sidebar to launch the docs site wizard.

Give your site a name, choose a starting point for your content, and select whether you want to publish your site now or later.

If you already have content in a space that you would like to use, you can create a docs site directly from that space by opening the space and clicking **Share** in the top-right corner of the window. Then choosing **Publish as a docs site** from the share modal.

### Publish a docs site

By default, your site will be published publicly. You can change your site’s visibility in your [site’s settings](https://gitbook.com/docs/documentation/publishing-documentation/site-settings).

There are three primary options to choose from when publishing your site:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Public</strong></td><td>Publish your docs publicly to the web.</td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fh07YAPTJAFEf2OChagKd%2FPublic.svg?alt=media&#x26;token=0ef630f6-f263-4acb-a3f9-e8c99d88ee96">card_publish_public.svg</a></td><td><a href="publish-a-docs-site/public-publishing">public-publishing</a></td></tr><tr><td><strong>Privately with share links</strong></td><td>Publish your docs with private share links.</td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FJiRinaF7WqJ8IBGdU8oE%2FPrivately.svg?alt=media&#x26;token=99376132-1d66-4125-8a18-1ab35e90e385">card_publish_privately.svg</a></td><td><a href="publish-a-docs-site/share-links">share-links</a></td></tr><tr><td><strong>Authenticated Access</strong></td><td>Protect your published docs behind an OAuth sign in.</td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FiSv6u28TbniLRbdoAqJg%2FVisitor%20Authentication.svg?alt=media&#x26;token=5a829cf4-9505-4320-9e80-ca24e5f89c4f">card_publish_visitor_authentication.svg</a></td><td><a href="authenticated-access">authenticated-access</a></td></tr></tbody></table>

### Delete or unpublish a docs site

To delete a docs site, you’ll need to open your site’s dashboard, then open [**Site settings**](https://gitbook.com/docs/documentation/site-settings#delete-site) from the top-right corner.

### Site editing permissions

Docs sites inherit the editing permissions from the [spaces](https://gitbook.com/docs/documentation/creating-content/content-structure/space) linked to them.

You can view all the permissions set for users with access to the docs site from the permissions modal from the docs site’s **Overview** page. You’ll also see which space the user’s permission was inherited from. If you’d like to change the permission settings, open the space, then click **Share**. Here you can edit the permissions from a modal.

Users with **Administrator** or **Creator** permissions on *any* space linked to a specific docs site will have full access permissions for the site. This means that they’ll be able to control any of the publishing and customization settings.

Users with **Reviewer**, **Editor**, **Commenter**, or **Reader** permissions on any space linked to a specific site will get read-only permissions. This means they will see the docs site in your organization, but won’t be able to access any of its settings.



# Public publishing

Publish your docs publicly to the web so that everyone can access them.

If you created your docs for a public audience, you can publish it on the web. Spaces that you publish on the web can be indexed by search engines and will be available to anyone. If you don’t want your content to be indexed by search engines, you can disable that too — read more about that [below](#publish-as-public).

However you publish your content, you’ll still retain control over who can *edit* your content. And only your primary content branch will be published, so any [change requests](https://gitbook.com/docs/documentation/collaboration/change-requests) will remain private until merged.

### Publish as public

To publish your docs publicly on the web head to the docs site you want to publish, click **Publish** button, and choose the **Public** option.

### **Publish without search engine indexing**

By default, your site will be indexed by search engines. You can alternatively choose to disable this — meaning the docs are still available to everyone on the web, but they *won’t* be indexed by search engines such as Google.&#x20;

They will still be accessible to anyone with a the link to your documentation. Docs sites that aren’t indexed can be particularly helpful if you want to publish a beta version of your docs, or do large-scale user testing without impacting your SEO with potentially duplicate content.

### Page-level search indexing controls

You can also control search indexing at the individual page level. GitBook provides two types of search indexing controls:

#### Internal search indexing

Controls whether pages are indexed in GitBook's internal search engine and Ask AI feature. This affects:

* Content search within your GitBook space
* Ask AI's ability to reference the page content

**External search indexing (Web crawlers)**

Controls whether search engines and web crawlers (Google, ChatGPT, etc.) can index your pages. This affects:

* SEO and discoverability through search engines
* Web crawler access to your content

#### **Hierarchical inheritance behavior**

**Search indexing settings follow a hierarchical inheritance pattern:**

* **Parent page controls**: When you disable search indexing on a parent page, it automatically disables indexing for ALL sub-pages beneath it.
* **Children cannot override**: Sub-pages cannot re-enable search indexing if their parent page has it disabled.
* **Cascading effect**: This creates a cascading effect down the entire page hierarchy - disabling indexing on a top-level page will disable it for the entire section.

This hierarchical behavior ensures consistent indexing policies across related content sections and prevents accidental exposure of content that should remain private within a section.

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}



# Private publishing with share links

Add greater control over who can view your published GitBook documentation.

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

You can share you content privately with customers or partners without needing to invite them to your organization by using share links.

### Publish with share links

To publish your docs privately, head to the [docs site’s ](https://gitbook.com/docs/documentation/publishing-documentation/site-settings)settings, click **Audience settings** button, and choose the **Share links** option.

Next, click on **Create link** to create a share link. You can review and name your share links, customize your domain and copy the link.

Once the link is active, a private token is generated within your URL, which is unique to your space. Sharing this link will give non-GitBook users access to your content in read mode only, with an interface that looks like any other published content.

You can generate as many links as you need from **Audience settings**.

{% hint style="info" %}
You can [revoked](#revoke-a-link) and regenerate share links at any time.
{% endhint %}

### Access and permissions

The content will be accessible to **anyone following the link**. Your team members can access your content from the **Docs sites** section of the sidebar, or by navigating to the space directly.

### Revoke a link

You can disable or regenerate your shareable by revoking it. You can see and revoke any previously generated link by opening the visibility menu and clicking through to link and domain settings.&#x20;

Once you revoke a link, anyone with that outdated link to your content will no longer have access.



# Site structure

Add structure to your published documentation using site sections and variants

The content on your site comes from [spaces](https://gitbook.com/docs/documentation/creating-content/content-structure/space) in your organization. You can link one or multiple spaces. GitBook will publish each one and handle the navigation between spaces.


## Content types

Linked spaces can serve as one of two different content types, which determine how GitBook treats them in relation to each other and shows them to visitors.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover-dark data-type="image">Cover image (dark)</th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden><select></select></th></tr></thead><tbody><tr><td><strong>Content variants</strong></td><td>Publish multiple versions of the same content — ideal for localization, versioning, and more.</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FuWpHiQp4LvA5wpM5Ovo8%2FContent%20variants.svg?alt=media&#x26;token=4b02400b-8994-4319-952d-db5e97661f02">Content variants.svg</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fn4cyj32rFyxmzb8md9MZ%2FContent%20variants.svg?alt=media&#x26;token=d4ebcb4d-c0e3-449a-aef7-cdbed54a15d0">card_variants.svg</a></td><td><a href="site-structure/variants">variants</a></td><td></td></tr><tr><td><strong>Site sections</strong></td><td>Split your site into distinct parts — ideal for multiple products or parts of your organization.</td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FVdIazRjl18hxN5SzpiqR%2FSite%20sections.svg?alt=media&#x26;token=2e1d4bae-4a54-4daa-96f8-b248203c6d6b">Site sections.svg</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FDdZMM5CW3YBw82UlXxxE%2FSite%20sections.svg?alt=media&#x26;token=26294748-75c0-4d32-83ad-1707c3fcf973">card_site_sections.svg</a></td><td><a href="site-structure/site-sections">site-sections</a></td><td></td></tr></tbody></table>


## Managing your site structure

By managing the structure of your site, you can also manage your site’s top navigation bar. This navigation bar allows users to jump to different site sections and site section groups.

From your docs site’s dashboard, open the **Settings** tab in the site header, then click **Structure**. Here you can see all the content of your site, divided into sections and variants.

Your site starts out with a single section with your site's name and a single variant with the space you linked during your site's set-up.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FvWn6UFQHs1t3HBe2kpRR%2F14_03_25_site_structure.png?alt=media&#x26;token=575843bc-0c40-413f-8813-d9db05fa7b74" alt="A GitBook screenshot showing a docs site&#x27;s structure"><figcaption><p>The structure of a published docs site.</p></figcaption></figure>

### Linking a space to your docs site

To add a [site section](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections), click the **Add section** button underneath the table and choose a space to link as a section. The new section is then added to the table and will be available to visitors as a tab at the top of your site.

To add a [variant](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/variants), click the **Add variant** button in the section you’d like to add to, then choose a space to link. The new variant is then added to the list of variants within the chosen section and will be available to visitors in the variant dropdown on your site.

When you add a space — as a variant or a section — a name and slug will be generated based on the space’s title.

### Changing sections or variants

<div data-full-width="false"><figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FmRlOLG1q8O0XUjrggwaB%2F04_02_25_edit_variant.svg?alt=media&#x26;token=69815267-2507-43c2-ad24-1b41844f02e5" alt="A GitBook screenshot showing how to edit a variant"><figcaption><p>Update a site section or variant.</p></figcaption></figure></div>

You can change the name and slug of each of sections and variants by clicking the **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> button in the table row of the item you’d like to edit. This will open a modal. Edit the field(s) you’d like to change, then click the **Save** button to save.

{% hint style="info" %}
Changing a linked space's slug will change the space's canonical URL. GitBook will create an automatic redirect from the old URL to the new one. You can also [manually create redirects](https://gitbook.com/docs/documentation/publishing-documentation/site-redirects).
{% endhint %}

To replace a section or variant, first delete it by clicking its **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> button, then click the **Delete** button in the lower left of the modal. Once the item is deleted, click the **Add section** or **Add variant** button to add it again.

### Reordering sections or variants

Your site displays sections and variants in the order that they appear in your **Site structure** table. They can be reordered by grabbing the **Drag handle** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> and moving it up or down. The changed order will be reflected on your site immediately.

You can also use the keyboard to select and move content. Select a section or variant with the space bar, then use the arrow keys to move it up or down. Hit the space bar again to confirm the new position.

### Setting default content

If you have multiple sections in your site, one section will be marked as **Default**. This section is shown when visitors arrive on your site, and is served from your site’s root URL. Other sections each have a slug that is appended to the root URL.

If you have multiple variants within a section, one variant will be marked as the default. Like sections, the default variant is shown when visitors arrive on your site, or when they visit a section. Other variants each have a slug that’s appended to the section’s URL.

To set a space as default, click on the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> in the space’s table row and then click **Set as default**.

{% hint style="info" %}
Setting a space as default removes its slug field, as it will be served from the section root instead. GitBooks redirects the space’s slug to the appropriate path, to ensure visitors keep seeing your content.
{% endhint %}

### Remove content from a site

To remove the content of a space from a site, open the **Settings** tab from your docs site dashboard, then click **Structure** to find the content you want to remove.

Open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the space you want to remove and choose **Remove**.

{% hint style="success" %}
Removing a space from your site will remove it from the published site, but **will not delete the space or the content within it**.
{% endhint %}



---
**Navigation:** [← Previous](./02-collections.md) | [Index](./index.md) | [Next →](./04-content-variants.md)
