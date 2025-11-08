**Navigation:** [← Previous](./05-authenticated-access.md) | [Index](./index.md) | Next →

# Authenticated access

GitBook offers out-of-the box solutions to protect your docs. Integrations for Auth0, Okta, Azure AD, and AWS Cognito allow you install an integration to enforce a log-in screen before being able to access your published site.

Depending on which authenticated access method you’re using, you’ll still need to configure a few more things depending on which integration you’re using in order to send the right data to GitBook.

Head to the relevant guide for full instructions on setting up adaptive content with authenticated access.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Setting up Auth0</strong></td><td>Configure Auth0 with authenticated access and adaptive content.</td><td><a href="../../authenticated-access/setting-up-auth0">setting-up-auth0</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FRC8ah9trT3HsKVau1mnH%2Fcard_auth0.svg?alt=media&#x26;token=66d83098-b07c-4ee1-b41d-f9766dfdf703">card_auth0.svg</a></td></tr><tr><td><strong>Setting up Azure AD</strong></td><td>Configure Azure AD with authenticated access and adaptive content.</td><td><a href="../../authenticated-access/setting-up-azure-ad">setting-up-azure-ad</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FKrbZXlJ3dMpfRu87FMGS%2Fcard_azure_ad.svg?alt=media&#x26;token=9ab99f1f-bd44-4a01-829b-3572d4559dff">card_azure_ad.svg</a></td></tr><tr><td><strong>Setting up AWS Cognito</strong></td><td>Configure AWS Cognito with authenticated access and adaptive content.</td><td><a href="../../authenticated-access/setting-up-aws-cognito">setting-up-aws-cognito</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FiWvq26r9Mxig2qbWMJJ4%2Fcard_aws_cognito.svg?alt=media&#x26;token=f275b67c-fbcc-46e2-8eb6-b46f9629ef0e">card_aws_cognito.svg</a></td></tr><tr><td><strong>Setting up Okta</strong></td><td>Configure Okta with authenticated access and adaptive content.</td><td><a href="../../authenticated-access/setting-up-okta">setting-up-okta</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fb1BCMkshEsKD26yyp0Wt%2Fcard_okta.svg?alt=media&#x26;token=81133f4d-0a34-40e3-958e-616a268a12c1">card_okta.svg</a></td></tr><tr><td><strong>Setting up a custom backend</strong></td><td>Configure a custom backend with authenticated access and adaptive content.</td><td><a href="../../authenticated-access/setting-up-a-custom-backend">setting-up-a-custom-backend</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FkiyIjK7tW99zVp1y1ksI%2Fcard_custom_backend.svg?alt=media&#x26;token=03687058-22d1-462e-8d4a-c42f6b51a1df">card_custom_backend.svg</a></td></tr></tbody></table>



# Adapting your content

Tailor your content for different users.

After setting up your authentication method, you’ll be able to use the data to adapt the content in your site for different users.

You can adapt and personalize many parts of your docs, including:

* Hiding or showing [pages](https://gitbook.com/docs/documentation/creating-content/content-structure/page)
* Hiding or showing site [variants](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/variants)
* Hiding or showing site [sections](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections)
* Hiding or showing [header links](https://gitbook.com/docs/documentation/customization/layout-and-structure#header)
* Adding personalized content to [inline expressions](https://gitbook.com/docs/documentation/creating-content/variables-and-expressions)

### Working with the condition editor

The condition editor is where you’ll set the conditions for showing or hiding a page, variant, or section. After opening the condition editor, you’ll be able to write your condition as an [expression](https://gitbook.com/docs/documentation/creating-content/variables-and-expressions) that will run against data coming from visitors to your site.&#x20;

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FOuXuIopG1ewhME0Kzeo2%2F28_07_25_condition_editor.svg?alt=media&#x26;token=b342b145-893e-4237-aad7-98f0ebdff208" alt=""><figcaption></figcaption></figure>

#### Example

The data you pass through your users to GitBook is attached to an object called `visitor.claims`.&#x20;

Let’s take a look at an example if we want to write a conditional statement to **only show a page for users who are part of a beta program** you might define.&#x20;

```javascript
visitor.claims.isBetaUser == true
```

The expression above means that any user who matches this claim (i.e. `isBetaUser` is `true` in the user’s claim), will be able to see and access the page. Any user who does not match this claim (including visitors without any claims set), will not be able to see or access the page.

The condition editor also comes built in with autocomplete, which suggests claims or attributes that have been found on previous visitors to your site, helping you craft the conditional statement for your pages, variants, or sections.&#x20;

As you use the autocomplete, you'll notice that [variables](https://gitbook.com/docs/documentation/creating-content/variables-and-expressions#use-variables-in-your-content) are also available to use. You can combine variables that you have defined together with claims that come from user data to write conditional expressions. For example, you could:

1. Set a variable for the latest version of your product
2. Then, configure a claim that shows which version of your product is being used by a visitor to your docs
3. Finally, write an expression to only show certain pages when a user is on the latest version of your docs

You can write many different kinds of expressions , as long as they are written in valid Javascript. For instance, you can combine multiple claims into the condition editor to match specific users by using the `&&` or `||` operator. You can read more about operators [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators).

### Testing with segments

Segments represent mock user data that you can configure to test your conditions.&#x20;

For example, you could set up a segment that represents a developer on your enterprise plan, or a sign-in user on a free plan, and then see which pages would be visible to them.&#x20;

[You can read more about setting up and using segments here.](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content/testing-with-segments)

### Conditional pages

To launch the condition editor for a page, head to the actions menu <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to a page, and click **Add condition.** You can also launch the condition editor from a [page’s options](https://gitbook.com/docs/documentation/resources/gitbook-ui#page-options).

You can see which pages in your space have conditions set if the page has a page condition icon <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> next to it.

{% if visitor.claims.unsigned.bucket.IF\_BLOCK === true %}

### Conditional blocks

To add a conditional block, begin a new line in the editor, type <kbd>/</kbd>, then select  <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> **Conditional content**.&#x20;

In the top right of the block, click on the  <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> **Condition** button to edit the condition and control the visibility of the block. Not all block types are supported within conditional blocks.
{% endif %}

### Conditional variants

To launch the condition editor for a variant, head to the actions menu <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to a variant, and click **Add condition**.

You can see which variants in your docs have conditions set if the variant has a page condition icon <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> next to it.

### Conditional sections

To launch the condition editor for a section, head to the actions menu <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to a section, and click **Add condition**.

You can see which sections in your docs have conditions set if the section has a page condition icon <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> next to it.

### Conditional page header links

To launch the condition editor for a page header link, head to the actions menu <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to a header link, and click **Add condition**.

You can see which links in your docs have conditions set if the section has a page condition icon <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG1cXfAVYBRLW0aRpIDRJ%2Fpage-condition%20-%20dark.svg?alt=media&#x26;token=dd656a89-387d-41c7-adf8-994848ec3440" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F51vQZhUqnkdsYpyUo1Pj%2Fpage-condition.svg?alt=media&#x26;token=31dd334a-5097-4081-915c-db460e610ec6" alt="The Page condition icon in GitBook"></picture> next to it.

### Inline expressions

In addition to controlling the visibility of content, you can also use claims inline using [expressions](https://gitbook.com/docs/documentation/creating-content/variables-and-expressions), just like page and space variables.&#x20;

To reference a claim inline using an expression, type <kbd>/</kbd> in the editor, then select <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FuPn7EFzfXAeRof6dIxwZ%2FExpression%20-%20dark%20mode.svg?alt=media&#x26;token=de1419bc-04f5-4b29-9397-b4b62d1aa4c0" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FyV0YSeHof9IkW4nnHQ4C%2FExpression.svg?alt=media&#x26;token=47e912c2-1ff1-4882-825f-5c3c79b4e6c0" alt=""></picture> **Expression**. Claims will be accessible in the expression editor as properties on `visitor` .

### Working with Git Sync

Conditions set in GitBook are synced through Git Sync and appear in the synced Markdown pages. This means blocks and pages with conditions set on their visibility are still visible in your synced repo.

&#x20;Data passed through claims is never visible in Markdown, and is securely passed to GitBook.



# Testing with segments

Test your conditions with mock data.

Segments allow you to test the conditions you set by defining claims on a mock user.

For example, you might want to only show a page or section to beta users. By creating a segment and defining the properties associated with this group of mock users, you can mimic a segment that is specific to the users you’re targeting.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FqHAwiqV4PhzJbqXNCEZP%2F18_07_25_segment_editor.svg?alt=media&#x26;token=cdc742cf-e1d6-4e0f-8f26-e8b0c9878dd7" alt="A GitBook screenshot showing the segment editor"><figcaption><p>The segment editor in GitBook.</p></figcaption></figure>

### Create a segment

To create a new segment, head to the condition editor, and click the settings icon <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F6uYUpJto7WTkJf9BUPHv%2Fsettings%20-%20dark.svg?alt=media&#x26;token=bf52415f-e999-43a2-9a1a-c85176a014cd" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwkBqgOPry9HAcW4cxJk0%2Fsettings.svg?alt=media&#x26;token=67bdbb00-ebf3-4a2d-9df8-0c822406f71c" alt="The Settings icon in GitBook"></picture> next to an existing segment in the segment dropdown.

Here you’ll be able to define the data that will appear on a mock user. Because this is the data that’s being represented, the `visitor.claims` key is omitted.

#### Example

To create a segment for beta users following the examples in our docs, you would create a new segment, and add the following data.

```json
{
  "isBetaUser": true
}
```

When heading back to the condition editor, selecting the beta segment we created should show that the page we’re viewing **would** be accessible to our test user.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FifSD7Ja6jOfCECLlyxAK%2F21_03_25_testing_segments.svg?alt=media&#x26;token=aad7a05c-ca4e-4eae-9715-ce25bcaf398d" alt="A GitBook screenshot showing how to test a segment"><figcaption><p>Testing a segment in GitBook.</p></figcaption></figure>

### Detected segments

Detected segments allow you to get a sense of the type of claims you are receiving from visitors to your site.

These segments are not editable, but allow you to copy/paste claims from the segment editor to create your own user segments.

### Testing segments in the preview

In addition to testing segments in the segment editor, you’ll be able to use your segments in real time in the preview when viewing changes for your site.

Use the dropdown in the upper left corner when in preview mode for your site to choose a segment to see how your site will look for your chosen segment.



# AI Search

Help your users find the information they need faster with powerful AI search tools for your published content

Help your users find the information they need faster with powerful knowledge discovery tools for your published content

### Choose your site’s search experience

GitBook sites offer different search experiences depending on what you want for your users:

* **Keyword search** – A standard search experience based on keywords. Automatically enabled on all sites.
* **GitBook AI search** – Users get short answers to questions directly from the search box.
* **GitBook Assistant** – Users get an advanced, interactive chat experience with GitBook’s AI agent. Head to [GitBook Assistant](https://gitbook.com/docs/documentation/publishing-documentation/gitbook-ai-assistant) to learn more.

To choose your site’s search experience, open your site’s dashboard, navigate to the **Settings** page and choose **AI & MCP** from the menu on the left. Here you can choose your preferred experience.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FZLKjSnbd8AfcHZEDkQIJ%2F29_07_25_search_ai.svg?alt=media&#x26;token=82ca3fbb-0dee-407a-9bf7-b2473b774e06" alt=""><figcaption><p>Choose the search experience you want in your published docs</p></figcaption></figure>

{% hint style="warning" %}
When GitBook Assistant is enabled, AI search is disabled. Standard keyword searches will always provide the results in the search bar no matter which experience you choose.
{% endhint %}


## Searching published documentation

**​**Users can open the **Ask or search…** bar by pressing <kbd>⌘</kbd> + <kbd>K</kbd> on Mac or <kbd>Ctrl</kbd> + <kbd>K</kbd> on PC.

Your users can search for keywords within your docs site and jump quickly to specific pages or page sections across your entire site.

If your docs site has multiple [sections](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections), the search results will contain pages from all of these sections so that you users can jump straight to the page they need.


## GitBook AI search

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

GitBook AI search offers basic AI-powered answers in the **Search and find…** bar of your site. It’s trained on the content of your docs site, but cannot pull in information from external sources.

### Using GitBook AI search

If you have enabled GitBook AI search from your site’s settings page, your users can access it by asking a question directly in the **Ask or search…** bar at the top of the page.

They can open this by clicking it directly, or by pressing <kbd>⌘</kbd> + <kbd>K</kbd> on a Mac or <kbd>Ctrl</kbd> + <kbd>K</kbd> on a PC.

As well as a summarized answer, below your users will also see an expandable section that shows the sources that GitBook AI used to create its answer, plus related questions you can click as a follow-up.

{% hint style="warning" %}
GitBook AI does not work across individual published spaces on different [docs sites](https://gitbook.com/docs/documentation/publishing-documentation/publish-a-docs-site).

Multi-space search is only available when viewing published spaces that live as [site sections](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections) within the same site.
{% endhint %}

* Press <kbd>⌘</kbd> + <kbd>I</kbd> on Mac or <kbd>Ctrl</kbd> + <kbd>I</kbd> on PC
* Click the **GitBook Assistant** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FFdcFnImj64xwVYVPFZZp%2Fgitbook-assistant-dark.svg?alt=media&#x26;token=6d5690e2-8587-4646-886a-dfd49caee6d5" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FRPCVZqnhQlwvRJbvEgM9%2Fgitbook-assistant.svg?alt=media&#x26;token=0506ce84-b363-481b-aefb-e0fa47357226" alt=""></picture> button next to the **Ask or search…** bar
* Type a question into the **Ask or search…** bar and choose the ‘Ask…’ option at the top of the menu.



# GitBook Assistant

GitBook Assistant offers users answers based on your docs and tailored to their situation — not just generic responses

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FSYnigoIgRCsPtDbJ4UKr%2F23_07_25_gitbook_assistant.svg?alt=media&#x26;token=384d57b1-fe51-464f-b000-fd7450f250a7" alt="GitBook Assistant"><figcaption><p>The GitBook Assistant</p></figcaption></figure>

GitBook Assistant gives your users fast, accurate answers about your documentation using natural language. It's personalized to your users, can be embedded into your website or product, and is available in the sidebar of your published docs.

Think of it as a product expert available to all of your users, in the places and times they need it most.

The Assistant uses agentic retrieval to understand the context of queries based on the user's current page, previously-read pages, and previous conversations.

<p align="center"><a href="https://gitbook.com/docs/publishing-documentation/gitbook-ai-assistant?ask=how+does+the+gitbook+assistant+help+tie+product+knowledge+closer+to+users+in+my+product" class="button primary">Test GitBook Assistant</a></p>

### Enable GitBook Assistant <a href="#how-do-i-use-gitbook-ai" id="how-do-i-use-gitbook-ai"></a>

To enable GitBook Assistant, open your site's dashboard, navigate to the **Settings** page and choose **AI & MCP** from the menu on the left. Here you can enable GitBook Assistant from the options available.

### Using GitBook Assistant in published docs <a href="#how-do-i-use-gitbook-ai" id="how-do-i-use-gitbook-ai"></a>

Users can access GitBook Assistant in three ways:

* Press <kbd>⌘</kbd> + <kbd>I</kbd> on Mac or <kbd>Ctrl</kbd> + <kbd>I</kbd> on PC
* Click the **GitBook Assistant**&#x20;

  <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FFdcFnImj64xwVYVPFZZp%2Fgitbook-assistant-dark.svg?alt=media&#x26;token=6d5690e2-8587-4646-886a-dfd49caee6d5" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FRPCVZqnhQlwvRJbvEgM9%2Fgitbook-assistant.svg?alt=media&#x26;token=0506ce84-b363-481b-aefb-e0fa47357226" alt=""></picture>

  &#x20;button next to the **Ask or search…** bar
* Type a question into the **Ask or search…** bar and choose the 'Ask…' option at the top of the menu

{% if visitor.claims.unsigned.reflag.EMBED\_ASSISTANT\_PANEL == true %}

#### Embed GitBook Assistant in your product

You can embed GitBook Assistant to help you bring your product and product knowledge closer together. Choose the embedding method that fits your stack:

* [**Script tag**](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – Quick setup with a `<script>` tag
* [**Node.js/NPM**](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – Server-side or build-time integration
* [**React component**](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – Prebuilt React components

**Additional guides:**

* [Using with authenticated docs](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – Required if your docs need sign-in
* [Customizing the Assistant](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – Welcome messages, buttons, and suggestions
* [Creating custom tools](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – Connect Assistant to your APIs
* [API Reference](https://gitbook.com/docs/documentation/publishing-documentation/broken-reference) – All available methods and events
  {% endif %}

### Extend GitBook Assistant with MCP servers

You can also add external data sources to GitBook Assistant to give it more context and data to pull answers from. You can do this by connecting Assistant to MCP servers for external platforms, such as:

* Your community (Slack, Discord, GitHub Communities etc)
* Support tools (Intercom etc)
* Your future product roadmap (GitHub, Linear etc)
* Docs for external integrations with products

To add an MCP server to GitBook Assistant, follow these steps:

{% stepper %}
{% step %}
**Open your site's settings**

Navigate to your site dashboard and choose the **Settings** option from the site header. Then choose the **AI & MCP** section from the left-hand menu
{% endstep %}

{% step %}
**Add a new server**

At the bottom of the page is a table showing all the connected MCP servers. To add a new server, click **Add MCP server**
{% endstep %}

{% step %}
**Choose your MCP server**

To add your server you'll need to give it a name, add the URL for the server, and configure the HTTP headers that will be sent along with the request to the server when a user submits a query.
{% endstep %}
{% endstepper %}



# LLM-ready docs

Providing an LLM-friendly version of your docs site

We’re building features that make it easier for Large Language Models (LLMs) to ingest and work with your documentation content.

As LLMs become increasingly important for information retrieval and knowledge assistance, ensuring your documentation is LLM-friendly can significantly improve how these models understand and represent your products or services.

LLM-optimized documentation ensures that AI systems like ChatGPT, Claude, Cursor, and Copilot can retrieve and provide accurate, contextual responses about your product or API.


## .md pages

With GitBook, all of the pages of your docs site are automatically available as markdown files. If you add the `.md` extension to any page, you will see the content of that page rendered in markdown which you can pass to an LLM for more efficient processing than an HTML file.

<a href="https://gitbook.com/docs/publishing-documentation/llm-ready-docs.md" class="button primary">Check out the .md file for this page</a>


## llms.txt

[llms.txt](https://llmstxt.org/) is a proposed standard for making web content available in text-based formats that are easier for LLMs to process. You can access the `llms.txt` page by appending `/llms.txt` to the root URL of your docs site.

The `llms.txt` file serves as an index for your documentation site, providing a comprehensive list of all available markdown-formatted pages. With this file, you make it easier for LLMs to efficiently discover and process your documentation content.

<a href="https://gitbook.com/docs/llms.txt" class="button primary">Check out the /llms.txt for the GitBook docs</a>


## llms-full.txt

Where the `llms.txt` file contains an index of all the page URLs and titles of of your documentation site, the `llms-full.txt` contains the full content of your documentation site in one file that can be passed to LLMs as context.

<a href="https://gitbook.com/docs/llms-full.txt" class="button primary">Check out the /llms-full.txt file for the GitBook docs</a>

LLMs can use this index to navigate directly to the markdown versions of your pages, allowing them to incorporate your documentation into their context without needing to parse HTML.


## MCP server

GitBook automatically exposes a Model Context Protocol (MCP) server for every published space. MCP gives AI tools a structured way to discover and retrieve your docs as resources — no scraping required.

Your MCP server can be reached by appending `/~gitbook/mcp` to the URL of the root of your docs site. For instance, the GitBook docs MCP server is located at `https://gitbook.com/docs/~gitbook/mcp`.&#x20;

{% hint style="info" %}
Visiting this URL in your browser will result in an error. Instead, you can share this with tools that can make HTTP requests, like LLMs or IDEs.
{% endhint %}

Learn more by reading [mcp-servers-for-published-docs](https://gitbook.com/docs/documentation/publishing-documentation/mcp-servers-for-published-docs "mention").


## Tips for optimizing your docs for LLMs

Now that your GitBook site automatically generates `.md` pages, `llms.txt`, and `llms-full.txt` files, these best practices will help LLMs effectively understand and work with your content.

By using these optimizations, you may also improve your documentation’s performance in AI-powered search engines and generative engine optimization (GEO).

The best part? These guidelines will generally make your docs easier for people to read as well.

### Use clear, hierarchical structure

Break up your content with good headings (H1, H2, H3) and don’t just write giant walls of text. Bullet points, numbered lists and shorter paragraphs make everything easier to read.

### Write concise, jargon-free content

Keep it simple and skip complex technical terms unless you really need them. LLMs do much better when you say what you mean without adding fluff.

### Include practical examples

Show, don’t just tell. Code snippets, API examples, and real scenarios help LLMs — and your users — understand how things actually work in practice.

### Keep content current and accurate

Nobody likes outdated docs. Regular updates mean LLMs won’t give people wrong information about your latest features and updates.

### Test with AI tools

Actually try asking ChatGPT or Claude questions about your docs to see how well they understand your content. You might be surprised by what works and what doesn’t.



# MCP servers for published docs

Docs published on GitBook automatically generate an MCP server you can hook up to external tools.

Every published GitBook site automatically includes a Model Context Protocol (MCP) server.&#x20;

This allows AI assistants to access your documentation content directly, making it easy for tools like Claude Desktop, Cursor, and VS Code extensions to answer questions using your docs.

The MCP server is available at your site’s URL with `/~gitbook/mcp` appended. For example, GitBook’s docs are located at `https://gitbook.com/docs`, so the MCP server is at `https://gitbook.com/docs/~gitbook/mcp`.

{% hint style="info" %}
Visiting this URL in your browser will result in an error. Instead, you can share this with tools that can make HTTP requests, like LLMs or IDEs.
{% endhint %}

### Connecting an AI assistant

{% stepper %}
{% step %}

#### Find your MCP server URL

Take your published GitBook site URL and add `/~gitbook/mcp` to the end.
{% endstep %}

{% step %}

#### Configure your AI tool

Add the MCP server URL to your AI assistant’s settings. Each tool has a slightly different setup process, so you should check out the docs for your tool of choice to see how to configure an MCP server for it.
{% endstep %}

{% step %}

#### Start using your docs

Once connected, your AI assistant can search through your documentation, retrieve specific pages, and answer questions using your content. The assistant will have real-time access to your published documentation.
{% endstep %}
{% endstepper %}

### Requirements

Your GitBook site must be published for the MCP server to work. The server only provides access to published content, never drafts or unpublished changes.

Your AI tool needs to support the Model Context Protocol and be able to make HTTP requests to your site. Most modern AI assistants that support MCP will work with GitBook’s servers.

The MCP server respects your site’s visibility settings. If your site is public, the MCP server is publicly accessible. If your site requires authentication, the MCP server will too.

The MCP server uses HTTP transport only. Tools that require stdio or SSE transport are not supported.

### Enable or disable easy MCP linking

In the **Page actions** section of your [Customization](https://gitbook.com/docs/documentation/publishing-documentation/customization) settings, you can enable the **Connect with MCP server** option. This enables visitors to your docs site to quickly copy a link to your site's MCP server right from [the Page actions menu](https://gitbook.com/docs/documentation/customization/extra-configuration#page-actions).

### Privacy and access

The MCP server only provides read-only access to your published documentation. It doesn’t expose any user data, analytics, or internal GitBook information.

Only the latest published version of your content is available through the MCP server. Draft content and unpublished changes remain private until you publish them.

### Common issues

If your AI assistant can’t connect to your MCP server, first check that your GitBook site is published and accessible. The URL should respond when you visit it in a browser.

Make sure you’re using the correct URL format with `/~gitbook/mcp` at the end. The URL should match exactly what you see when you visit your published site.

Some AI tools require specific transport methods or have particular MCP configuration requirements. Check your AI tool’s documentation for MCP setup instructions.



# Live edits

Edit pages in real-time with other collaborators

With live edits enabled, members in your org can edit a space without creating [a change request](https://gitbook.com/docs/documentation/collaboration/change-requests). When editing content, you can see the avatars of anyone currently viewing the space in the top-right corner.

GitBook supports live collaboration, meaning you’ll be able to work on the same document with multiple members at the same time.

{% hint style="info" %}
**Live edits are locked** by default in any newly created space. To edit the content, you will either need to [create a change request](https://gitbook.com/docs/documentation/collaboration/change-requests), or toggle live edits on.
{% endhint %}

### Toggling live edit mode

You can toggle live edit mode in a space by selecting **Lock live edits** or **Unlock live edits** from the [space header’s](https://gitbook.com/docs/documentation/resources/gitbook-ui#space-header) **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fpn5vEw7bYFrMPpdyvpSu%2Factions-horizontal%20-%20dark.svg?alt=media&#x26;token=ec39eefe-a391-4fe2-828a-082b79f2847d" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture>.

When a space is in **Live edits** mode, the space header will show the **Editor** tab. When it is in **Locked live edits** mode, the space header will show a **Read-only** tab. When the Read-only tab appears in the space header, you will need to open a change request to edit the content of the page, or unlock live edits.

### When is live editing *not* available?

You cannot unlock live editing if:

1. a space is published with the **In collection**, **Public**, or **Unlisted** visibility option.
2. a space has [GitHub or GitLab Sync](https://gitbook.com/docs/documentation/getting-started/git-sync) enabled.

{% hint style="info" %}
Only [administrators and creators](https://gitbook.com/docs/documentation/account-management/member-management/roles) can lock or unlock live edits.
{% endhint %}



# Change requests

Collaborate on content edits through change requests

A change request is a copy of your main content. It comes from the simple concept of [**branching**](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell), and will feel familiar to anyone who uses pull requests in GitHub or merge requests in GitLab.

In a change request, you can edit, update and delete elements of your content, request reviews on your changes, then merge them back into your main version to apply all the changes you made.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fv592QQLN4jEiNNAt6KBX%2Fcollaboration-change-requests.svg?alt=media&#x26;token=2c4764d8-5f8d-4c03-854d-6bb2a329af63" alt="A GitBook screenshot showing the change requests panel"><figcaption><p>Edit your content through change requests.</p></figcaption></figure>

### Creating a change request

Inside a space where live edits are disabled, click the **Edit** button in the [space header](https://gitbook.com/docs/documentation/resources/gitbook-ui#space-header) to start a new change request.

This will open a new change request, where you can edit or delete content as needed. Your changes are saved automatically, and other people can join you in a change request to collaborate in real-time.

Once you’re happy with your changes, you can use the button in the header bar to **Request a review** of your change request, or **Merge** it directly into the main branch.

### Preview a change request

You can preview the changes you’ve made in a change request by clicking the **Preview** option in the [space header](https://gitbook.com/docs/documentation/resources/gitbook-ui#space-header). This will switch to a preview of your published docs with the proposed changes included, so you can see your changes in the entire context of your published documentation.

Below the **Preview** button is a URL for your site preview. Click this and your site preview will open in full in a new tab.&#x20;

When you open a preview URL in a new tab, you will also see [the Preview toolbar](https://gitbook.com/docs/documentation/resources/gitbook-ui/toolbar-on-published-sites-and-site-previews) at the bottom of the browser window. This toolbar lets you quickly jump back into GitBook to view, edit, or comment on the change request, or open the live version of your site.

{% hint style="info" %}
You can only preview change requests for spaces added to a [published docs site](https://gitbook.com/docs/documentation/publishing-documentation/publish-a-docs-site).
{% endhint %}

{% hint style="warning" %}
If your content is published using share links or authenticated access, the preview function won't appear.
{% endhint %}

### Request a review on a change request

Request a review on your change request when you want to ask members of your team to check your content before you merge the changes into the main branch.

You can add a description to your change request to give your reviewers some context, and tag specific people that you want to check your work.

When you click **Request a review**, the change request’s status will change to **In review**, and anyone you tagged in your review request will get a notification.

If your changes don’t require a review, you can merge your changes into the main version directly instead.

{% hint style="info" %}
If you don’t tag anyone in your review request, everyone with reviewer permissions will get a notification about your request. If no reviewers are in the space, the next role above reviewer will be notified.
{% endhint %}

### Reviewing a change request

If you get a request to review a change request, you'll be able to edit the content and leave feedback to make sure it's in good shape before it’s merged to the main version. You can either request changes if you think it still needs work, or approve the change request, to signal it's ready to merge.

Most reviews will take place in the change request’s [comments](https://gitbook.com/docs/documentation/collaboration/comments), where collaborators can share feedback and have discussions about specific content blocks, or the change request as a whole.

#### Diff view <a href="#diff-mode" id="diff-mode"></a>

When you open the **Changes** tab in the space header, the diff view will appear. Diff view highlights every page and block that’s been edited in a change request. It will highlight any edited pages in the table of contents, and on the pages it will show the specific blocks that have been added, edited or removed.

There are two options when using diff view:

1. **Show all pages** – This is the default mode for diff view, which will show both modified and non-modified pages in the table of contents. This is good for seeing which pages have been edited in the context of the entire space.
2. **Show only changed pages** – This mode will show only the modified pages in the table of contents, which helps you focus on the changed content. This is particularly helpful in larger spaces with many pages and sub-pages.

You can switch to the **Changes** tab to check the diff view in any change request.

### Merging a change request

Merging a change request will add the change request’s changes into the main branch of content, creating an updated version and a new entry in the space’s [version history](https://gitbook.com/docs/documentation/creating-content/version-control#see-the-activity-of-a-specific-draft).

#### Scheduling merges

If you prefer to merge change requests at a scheduled time—for example, to align with your product release cycles—you can use external tools like GitHub Actions or automation platforms such as Zapier, connected through [GitBook’s API](https://gitbook.com/docs/developers/gitbook-api/api-reference/change-requests#post-spaces-spaceid-change-requests-changerequestid-merge).

As an example, adding this GitHub workflow would merege a change request once a week:

{% code title=".github/workflows/scheduled-gitbook-merge.yml" %}

```yaml
name: Scheduled GitBook Merge

on:
  schedule:
    - cron: '0 9 * * 3'  # Runs every Wednesday at 09:00 UTC

jobs:
  merge_changes:
    runs-on: ubuntu-latest
    steps:
      - name: Merge Change Request
        run: |
          curl -X POST https://api.gitbook.com/v1/spaces/{space-id}/change-requests/{change-request-id}/merge \
          -H 'Authorization: Bearer YOUR_API_KEY' \
          -H 'Content-Type: application/json'
```

{% endcode %}

{% hint style="info" %}
Only [administrators, creators, and reviewers](https://gitbook.com/docs/documentation/account-management/member-management/roles) can merge change requests.
{% endhint %}

### Handling merge conflicts

Sometimes, when you want to merge a change request, you may discover conflicts between the main content and the content you’re trying to merge. In the simplest form, a conflict is a piece of content that could not be merged automatically.

If this happens, you’ll be presented with a conflict alert, and a list of the conflicts you’ll need to resolve before continuing the merge.

### Resolving merge conflicts

You have two options when it comes to resolving a merge conflict — **selecting a version to merge** or **manually** **editing the content**.

#### Selecting a version to merge

You can resolve a merge conflict by selecting a version you want to merge — either your incoming content, or the content that was previously there. This allows you to choose between one change and another — either your recent work, or the original content.

If you’re dealing with a merge conflict that can be resolved this way, you can select the version you want to keep, and the other version will be deleted.

#### Manually editing

If you don’t want to choose between versions, you can resolve a merge conflict by manually editing the conflict. You’ll be able to delete the blocks you don’t need, or even rewrite them entirely. Once you’re happy with the changes, you can move on to the next conflict until they’re all resolved.

### Archiving a change request

If you decide not to merge a change request and want to remove it from the queue, you can archive it.

To archive a change request, first open it up. Then click the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fpn5vEw7bYFrMPpdyvpSu%2Factions-horizontal%20-%20dark.svg?alt=media&#x26;token=ec39eefe-a391-4fe2-828a-082b79f2847d" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture> next to the change request’s title and choose **Archive**. You can find and reopen archived change requests later by opening the **Change Requests** menu and selecting the **Archived** tab.



# PDF export

Export a PDF copy of your GitBook content

### Allow readers to export a PDF version of your published content

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

To enable or disable PDF export for visitors to your [published docs site](https://github.com/GitbookIO/public-docs/blob/main/collaboration/broken-reference/README.md), open the docs site’s dashboard, open the **Customization** tab, and navigate to **Configure → Page actions**. From there, you can toggle **Export as PDF** on or off.

This setting determines whether or not **readers of your published content can download it in PDF format**. This feature is only available for **Premium and Ultimate sites**.

### Export your own internal content as PDF

However you decide to configure your published docs sites, all logged-in members of an organization on a Pro or Enterprise can export a page — or an entire space — from your internal knowledge base as a PDF file.

{% hint style="warning" %}
Note that links across spaces are not currently supported when exporting internal content to PDF.
{% endhint %}

#### Export an individual page

1. Open the page you want to export, then open the page’s [Actions menu](https://gitbook.com/docs/documentation/resources/gitbook-ui#the-actions-menu) <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to the page title.
2. Select **Export to PDF > Current page**.
3. Wait for the page to load, then click the **Print or save as PDF** button in the upper right to open your browsers Print menu.
4. From here, you can save the page as a PDF or open it in your PDF viewer using the typical process for your browser.

#### Export an entire space

1. Open the[ Actions menu](https://gitbook.com/docs/documentation/creating-content/content-structure) <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> next to the page title and choose **Export as PDF > All pages**. Alternatively, open the space’s **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fpn5vEw7bYFrMPpdyvpSu%2Factions-horizontal%20-%20dark.svg?alt=media&#x26;token=ec39eefe-a391-4fe2-828a-082b79f2847d" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPnnI41SqLSaKBNwT98fW%2Factions-horizontal.svg?alt=media&#x26;token=99754200-a354-4ffe-931e-aa6322ea7395" alt="The Actions menu icon in GitBook"></picture> in the [space header](https://gitbook.com/docs/documentation/resources/gitbook-ui#space-header) and choose **Export as PDF** in the drop-down menu.\
   \
   \&#xNAN;*Note: This action is not available within a change request.*
2. Wait for the page to load, then click the **Print or save as PDF** button in the upper right to open your browsers Print menu.
3. From here, you can save the page as a PDF or open it in your PDF viewer using the typical process for your browser.




---

[Next Page](/docs/llms-full.txt/1)



---
**Navigation:** [← Previous](./05-authenticated-access.md) | [Index](./index.md) | Next →
