**Navigation:** [← Previous](./03-variables-and-expressions.md) | [Index](./index.md) | [Next →](./05-authenticated-access.md)

# Content variants

Publish documentation for multiple product versions or languages in a single site

You can publish multiple versions of the same documentation as part of a single docs site. These variants will be available to the end users via the space switcher in the top-left corner of the published site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FZPZ8XR0WeDMpbBeiXD0b%2F18_07_25_publishing-documentation-site-structure.svg?alt=media&#x26;token=b192833c-6234-47c1-b35c-46fc3bd387f3" alt="A GitBook screenshot showing a docs site&#x27;s structure"><figcaption></figcaption></figure>

### Add multiple languages or versions

A site with multiple variants is useful if you need to group together the content of your spaces — such as if you’re documenting multiple versions of an API (v1, v2, v3, etc.), or documenting your content in different languages.

{% hint style="info" %}
The spaces you link can contain any content, but it’s recommended to use variants as *variations of the same content*. If the spaces you link are semantically different from each other, consider adding them as [site sections](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections) instead.
{% endhint %}

When adding a translation or multiple languages as a variant, it’s best practice to set the language of your variant to give your users the best experience when navigating your docs.

Adding multiple variants with languages set will move the language picker to the upper right, giving a cleaner, more direct experience from the default variant picker.

### Adding a variant to your docs site

From your docs site’s dashboard, open the **Settings** tab in the site header, then click **Structure**. Here you can see all the content of your site.

To add a variant, click the **Add variant** button in the section you'd like to add to, then choose a space to link. The new variant is then added to the list of variants within the chosen section and will be available to visitors in the variant dropdown on your site.

### Changing a variant

You can change the name and slug of each of your variants by clicking the <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> **Edit** button in the table row of the variant you’d like to edit. This will open a modal. Edit the field(s) you'd like to change, then click the **Save** button to save. You can also delete the variant by clicking the **Delete variant** button in the lower left.

{% hint style="info" %}
Changing a linked space's slug will change the space's canonical URL. GitBook will create an automatic redirect from the old URL to the new one. You can also [manually create redirects](https://gitbook.com/docs/documentation/publishing-documentation/site-redirects).
{% endhint %}

To replace a variant’s linked space with a different space, first delete it by clicking its **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> button, then click the **Delete** button in the lower left of the modal. Once the variant is deleted, click the **Add variant** button to add the new space.

### Reordering variants

Your site displays variants in the order that they appear in your **Site structure** table. Variants can be reordered by grabbing the **Drag handle** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> and moving it up or down. The changed order will be reflected on your site immediately.

You can also use the keyboard to select and move content: select a section or variant with the space bar, then use the arrow keys to move it up or down. Hit the space bar again to confirm the new position.

### Setting a default variant

If you have multiple variants within a section, one variant will be marked as the default. This variant is shown when visitors arrive on your site (or when they visit a section). Other variants each have a slug that is appended to the site's URL.

To set a variant as default, click on the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> in the variant’s table row and then click **Set as default**.

{% hint style="info" %}
Setting a variant as default removes its slug field, as it will be served from the section root instead. GitBook will redirect the variant's slug to the appropriate path, to ensure visitors keep seeing your content.
{% endhint %}

### Remove a variant from a site

To remove a variant from a site, open the **Settings** tab from your docs site dashboard, then click **Structure** to find the content you want to remove.

Open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the variant you want to remove and choose **Remove**.

{% hint style="success" %}
Removing a variant from your site will remove it from the published site, but **will not delete the space or the content within it**.
{% endhint %}



# Site sections

Add multiple products to your site as site sections and create a content hub with tabs to access all your content

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FFduOhhJv1OXwe96Dhu7L%2F14_03_25_site_sections_published.jpg?alt=media&#x26;token=a4e6f422-0e0f-4e3c-a676-c71fd8e4da7a" alt="A GitBook screenshot showing site sections on a docs site"><figcaption><p>Example of a GitBook site with site sections</p></figcaption></figure>

With site sections, you can centralize all your documentation and create a seamless experience for your users.

Site sections are perfect for organizing your documentation — whether you’re managing separate products, or catering to both end-users and developers with content tailored to each.

You can also [group site sections together](#create-a-site-section-group). Doing so will create a drop-down menu in your navigation bar — ideal for adding hierarchy to your site sections.

{% hint style="info" %}

### Sections or variants?

Each site section is a space in GitBook. You can create site sections from any space you like, but we recommend you use sections as semantically different parts of your docs.

If you want to add variations of the same content — such as localizations or historical versions of the same product — consider using [content variants](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/variants) instead.
{% endhint %}

### Adding a section to your docs site

From your docs site’s dashboard, open the **Settings** tab in the site header, then click **Structure**. Here you can see all the content of your site.

To add a site section, click the **New section** button underneath the table and choose a space to link as a section. The new section is then added to the table and will be available to visitors as a tab at the top of your site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FcEXoEuhxzIEBUgcwJU95%2F18_07_25_publishing-documentation-site-structure_sections.svg?alt=media&#x26;token=ccbd03e8-7ffd-466d-8cb4-b09b72f6c2f8" alt="A GitBook screenshot showing site section structure"><figcaption><p>Add structure to your docs with site sections.</p></figcaption></figure>

### Create a site section group

You can group site sections together under a single heading. Site section groups will appear as a drop-down in your site’s nav. Site sections in a group can also include an optional description, which appears below the section title in the drop-down menu.

To create a group, click the arrow next to the **New section** button and choose **New section group**. Give your new group a name, then click **Add section** in the modal to add sections to your group. You can add existing sections of your site to the new group, or select another space you want to add using the menu.

### Editing a section

You can change the name, icon and slug of each of your sections by tapping the <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> **Edit** button in the table row of the section you’d like to edit. This will open a modal. Edit the field(s) you’d like to change, then click the **Save** button. You can also delete the variant by clicking the **Delete variant** button in the lower left.

{% hint style="info" %}
Changing a section’s slug will change its canonical URL. GitBook will create an automatic redirect from the old URL to the new one. You can also [manually create redirects](https://gitbook.com/docs/documentation/publishing-documentation/site-redirects).
{% endhint %}

Site sections within a group can also optionally display a description, which will appear in the drop-down menu of your site’s nav bar when the section group is hovered. See the image at the top of this page to see an example of how this can look in your published documentation.

### Reordering sections

Your site displays sections in the order that they appear in your Site structure table. Sections can be reordered by grabbing the **Drag handle** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> and moving it up or down. All the spaces within that section will be moved with it. The changed order will be reflected on your site immediately.

You can also use the keyboard to select and move content: select a section with the space bar, then use the arrow keys to move it up or down. Hit the space bar again to confirm the new position.

### Setting a default section

If you have multiple sections in your site, one section will be marked as the default. This section is shown when visitors arrive on your site, and is served from your site’s root URL. Other sections each have a slug that is appended to the root URL.

To set a section as default, click on the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> in the section's table row and then click **Set as default**.

### Remove a section

To remove a section from a site, click the **Settings** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F6uYUpJto7WTkJf9BUPHv%2Fsettings%20-%20dark.svg?alt=media&#x26;token=bf52415f-e999-43a2-9a1a-c85176a014cd" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwkBqgOPry9HAcW4cxJk0%2Fsettings.svg?alt=media&#x26;token=67bdbb00-ebf3-4a2d-9df8-0c822406f71c" alt="The Settings icon in GitBook"></picture> button from your docs site dashboard, then click **Structure** to find the content you want to remove. Click the **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> button next to the section you want to remove, then click the **Delete** button in the lower left of the modal. This will remove the section, along with all the variants within it, from the published site. It will not delete the spaces itself, or the content within them.

To remove a section from a site, open the **Settings** tab from your docs site dashboard, then click **Structure** to find the content you want to remove.

Open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the space you want to remove and choose **Remove**.

{% hint style="success" %}
Removing a section from your site will remove it — and all variants within it — from the published site, but **will not delete any of the spaces or the content within them**.
{% endhint %}



# Site customization

Create branded documentation with a custom logo, fonts, colors, links and more

{% hint style="info" %}
Certain customization features are only available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

You can customize the appearance of your published documentation, match the user interface to the language of your content, and more.

You can apply customizations to your entire docs site as a site-wide theme, or to individual variants and site sections.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FPHDUX2Kbmd9wwUBpJqst%2Fcustomization-demo.png?alt=media&#x26;token=7586ba34-9cd2-47ee-9169-81b73dd40923" alt="A GitBook screenshot showing a customized docs site"><figcaption><p>You can create all kinds of site designs using GitBook’s built-in customization options.</p></figcaption></figure>

### Customizing sites with multiple sections or variants

If you have a docs site with with multiple sections or variants, you can control the customization of each one individually.

Select the whole site or a specific site section using the drop-down menu at the top of the **Customization** panel.

* **Site-wide settings** – These automatically apply to all linked spaces.
* **Section or variant specific settings** – If you’re using site sections or variants, you’re can set specific customization that will override the default site-wise setting.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F6cjcacmfApy0U5LyQsEu%2F19_02_2025_site_customization.svg?alt=media&#x26;token=0b8eeaaa-1ed1-4796-bc05-9f5be385ff44" alt="A GitBook screenshot showing the customization panel"><figcaption><p>The customization panel in GitBook.</p></figcaption></figure>

{% hint style="warning" %}
Changes you make to specific site sections will override the site-wide customization settings, even if you change the site-wide setting again later.

You can reset customization overrides back to the site-wide default by clicking the **Reset** button <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FR81SNitMgoyvkgwGRoR1%2Freset_icon_dark.svg?alt=media&#x26;token=bd09ce8a-e51f-483c-9b45-825cc123e89a" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FvKatj53oH4WPjv9G2pe5%2Freset_icon_light.svg?alt=media&#x26;token=e5632add-8f96-498f-87bc-a459aecf7d95" alt="The Reset icon in GitBook"></picture> next to the space selector.
{% endhint %}

### What counts as ‘Advanced customization’?

Every GitBook user can take advantage of basic customization options on their docs site. Premium or Ultimate site plan users can also use advanced customization features to further tweak their docs to match their brand.

Advanced customization options include:

* **Custom logo** – Add a logo that replaces the emoji and title at the top of your docs site.
* **Icons** - Change the weight and style of page icons in your docs site.
* **Custom font** – Change the font of your docs to one of the built-in options.
* **Footer** – Add a custom logo, copyright text and navigation to a footer at the bottom of your documentation.
* **Bold and Gradient themes** – Change the background color for your header, or add a gradient background to your entire site with these new themes.

### What cannot be customized?

The options above provide lots of ways for you to customize your space, but there are a few things that you won’t be able to customize, regardless of [your chosen plan](https://gitbook.com/docs/documentation/account-management/plans).

1. It’s not possible to customize the layout of the elements on the page (However, it *is* possible to [hide certain elements on specific pages](https://gitbook.com/docs/documentation/creating-content/content-structure/page)).
2. It’s not possible to insert custom code (such as CSS, HTML or JS) directly into your GitBook site. We already integrate with a number of popular tools, and offer [rich embeds](https://gitbook.com/docs/documentation/creating-content/blocks/embed-a-url) for many more.
3. It’s not possible to remove the small “Powered by GitBook” link that appears in published documentation.



# Icons, colors, and themes

Customize icons, colors, themes and more.

### Title, icon and logo

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FtvdryJLuBTbMvaFhUmUC%2F21_04_25_customization_title.svg?alt=media&#x26;token=5f8a64bb-1198-44cc-8987-4da4864ce474" alt="A GitBook screenshot showing title, icon and logo customization"><figcaption></figcaption></figure>

**Title**

You can set any title you choose for your space. Note: this setting will only affect the title that displays *in the published documentation*. If you want to edit the title in the GitBook app, close the customize menu and edit it at the top of the space.

**Icon**

You can set an emoji, or upload an icon of your own. The icon you set in the **Customization** menu will be used as the favicon for your docs site.

{% hint style="info" %}
This setting will only affect the icon that displays *in the published documentation*. If you want to edit the icon used within the GitBook app, you can do so when editing content in the space itself.
{% endhint %}

**Custom logo** <mark style="background-color:purple;">**(Premium & Ultimate)**</mark>

You can replace *both* the published space’s title and icon with a custom logo so that your documentation better reflects your own branding — and you can upload two versions: one for light mode, and one for dark mode.

{% hint style="info" %}

#### What’s the difference between the icon and logo options?

The icon setting lets you upload a small, 132×132 px image, which will appear *alongside* your space title and function as your site’s favicon. The custom logo option lets you upload a larger image (we recommend at least 600 px wide), which will completely replace any icon and title you’ve set.
{% endhint %}

### Themes

Themes let you customize the color scheme of your published content for both light and dark mode. There are four themes to choose from. The colors of your site will be directly impacted by the **primary color** and **tint** that you choose. These two selections affect various parts of the interface and can completely change the look and feel of your site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fg7f0edLNdKBJhMsTZUUG%2F21_04_25_customization_themes.svg?alt=media&#x26;token=e8530742-09ff-4779-8408-f2225a1db5ba" alt="A GitBook screenshot showing theme options"><figcaption></figcaption></figure>

#### Clean

A modern theme featuring translucency and minimally styled elements. Your primary color (or tint) affects links and other highlighted interface elements.\
\&#xNAN;*Clean is available for all sites and is the default theme.*

#### Muted

A sophisticated theme with decreased contrast between elements. The site background is more pronounced and blends in with the foreground, and some elements feature an inverted look — all based on your primary color (or tint).\
\&#xNAN;*Muted is available for all sites.*

#### Bold <mark style="background-color:purple;">**(Premium & Ultimate)**</mark>

A high‑impact theme with prominent colors and strong contrasts. Your primary color (or tint) will be used for the header of the site, and other highlighted elements like icons are colored along with it.\
\&#xNAN;*Bold is only available for Premium or Ultimate sites.*

#### Gradient <mark style="background-color:purple;">**(Premium & Ultimate)**</mark>

A trendsetting theme featuring a gradient background and splashes of color. The gradient and highlighted elements will be colored by your primary color (or tint).\
\&#xNAN;*Gradient is only available for Premium or Ultimate sites.*

### Colors

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FrtqfRxxCzos038sdCKeu%2F21_04_25_customization_colors.svg?alt=media&#x26;token=ca0b738e-1c26-43cb-bebf-bfa66f96003c" alt="A GitBook screenshot showing color customization"><figcaption></figcaption></figure>

#### Primary color

Your site’s primary color will affect the styling of highlighted interface items and navigational elements like links, the current page and section, breadcrumbs, and primary header buttons. GitBook automatically adjusts colors on individual elements for readability if the contrast with the background is too low or when a visitor’s system requests higher contrast.

#### Tint color

Your site’s tint color will subtly change the color of all text and icons across your entire site — including header links, icon color, and UI elements like the **Ask or search** bar. The tint color will *not* affect navigational elements like links and buttons, which always use the primary color. In the **Tint color** section you’ll see suggested colors based on your primary color selection; you can select one to preview it, choose your primary color as your tint, or pick a completely custom color with the color picker.

#### Semantic colors

Semantic colors are applied to hint blocks within your published content. You can change the background color of each hint style; these changes will only be reflected on the published site you’re customizing. Hint blocks in the GitBook editor will always remain in their assigned colors.

### Modes

**Show mode toggle**

Enable this if you want visitors to manually toggle between light and dark mode. Readers can find the toggle at the bottom of any published page, on both desktop and mobile.

**Default mode**

Choose whether visitors see your content in light or dark mode by default. If **Show mode toggle** is enabled, they can switch modes; if disabled, they’ll only see the mode you choose here.

*Note: to change the theme within the GitBook app, go to your Settings menu at the bottom of the sidebar.*

### Site styles

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fxsw0jToBjzuSfqusKuCv%2F21_04_25_customization_site_styles.svg?alt=media&#x26;token=2b541191-55d2-4790-874a-28d21a12ffa1" alt="A GitBook screenshot showing site style settings"><figcaption></figcaption></figure>

**Font family** <mark style="background-color:purple;">**(Premium & Ultimate)**</mark>

Choose a font family for your published content from a curated list of popular options.

**Custom fonts** <mark style="background-color:purple;">**(Ultimate)**</mark>

Upload your own fonts to align your published content with your brand’s style guide. To upload a font, click **Add custom font** and follow the instructions. You must upload a font file for both regular and bold weights.

GitBook currently supports `.woff` and `.woff2`. For other formats, please contact <support@gitbook.com>.

**Icons** <mark style="background-color:purple;">**(Premium & Ultimate)**</mark>

When using page icons, set the weight and style of the displayed icons here.

**Corner style**

Choose either rounded or straight corners to match your brand’s style preferences.

**Link style**

Choose between two link designs:

* **Default:** highlights the entire link in your primary or tint color.
* **Accent:** adds a colored underline to the link, leaving the text color unchanged.

### Sidebar styles

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F5JREt7PiS0R87mOj5Osa%2F21_04_25_customization_sidebar.svg?alt=media&#x26;token=c60321ec-22f6-4699-81e6-428e70d91598" alt="A GitBook screenshot showing sidebar style options"><figcaption></figcaption></figure>

**Background style**

Choose the background style for the sidebar container. The color is derived from your selected theme.

**List style**

Choose the style for the sidebar list and its selected items.



# Layout and structure

Customize the layout and structure of your published documentation.

### Header

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fgybcd1rVhFfDNcqhGdJR%2F21_04_25_customization_header.svg?alt=media&#x26;token=dfc98274-3428-4945-96be-7a41f67272da" alt="A GitBook screenshot showing header customization settings"><figcaption></figcaption></figure>

**Search bar**

Change the position and look of the search bar between prominent (centered in the header) and subtle (located in the upper right corner). Turning off the header entirely will place the search bar in the sidebar instead.

**Navigation**

Add header links to your site. You could use header links to point to important parts of your documentation, or link back to your main website.

You can choose what appearance you would like your link to have—normal link, primary button, or secondary button. When enabled, simply add a title and a URL for each link. We support two levels of header navigation, meaning you can have sub‑links that appear in a dropdown menu.

### Announcement (Premium & Ultimate)

Toggle this option on to add an announcement banner to the top of your published site. You can add a message and optionally include a link and call to action, which will appear after your message in the banner.

You can also change the announcement style using the same options as hint blocks—Info, Warning, Danger, and Success. The color of these styles is determined by your semantic colors settings.

### Pagination

Control the display of the “previous” and “next” buttons that appear at the bottom of each page in your space. You can also set this feature for specific pages.

### Footer (Premium & Ultimate)

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F4HFvBK50hoHi5h11CFy6%2F21_04_25_customization_footer.svg?alt=media&#x26;token=2ff4591c-6fd9-433b-bac1-aea97836f4b9" alt="A GitBook screenshot showing footer customization settings"><figcaption></figcaption></figure>

**Logo**

Add your logo or another image in the footer.

**Copyright text**

Add copyright information to your footer.

**Navigation**

Add links in your footer, organized into multiple sections. Similar to the header, add a title and URL for each link, and include a section title for each group of links.



# Extra configuration

Configure extra options for your published documentation.

### Localize user interface

You can select from a list of languages to localize the user interface of your published content. This applies translations to the non-custom areas of the interface.

This setting will *not* auto-translate your actual content, but it can help match the interface to the language you’re writing in. To learn more about translating your content, head to the [Translations](https://gitbook.com/docs/documentation/creating-content/translations) section.

Is there a language we don’t yet offer that you’d like to see included? [Let us know](https://github.com/GitbookIO/gitbook/issues), or [contribute your own translation](https://www.gitbook.com/solutions/open-source)!

### External Links

This setting controls the behaviour when your site users click an external link. By default, they will open in the same tab, but you can switch this to open in a new tab if that's your preference.

### Page actions

Page actions adds a page-level dropdown to every page of your docs, allowing users to perform quick actions on a page's content — ideal for using your docs content as context within an AI prompt.&#x20;

You can disable this option from the **Configure** tab if you do not wish to show page options in your published docs.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fd0Pk6IuD7GYRWTk1NpT3%2F01_08_2025_page_options.png?alt=media&#x26;token=4dc670ce-dd85-41d4-9ca0-c9ce5f29697d" alt=""><figcaption></figcaption></figure>

#### Open in AI providers

Displays an action to open ChatGPT or Claude with the page content.

#### Copy/View as Markdown

Displays an action to copy or view the page as Markdown.

#### Edit on GitHub/GitLab

If your space is connected to a Git repository, you can optionally show a link for your users to contribute to your documentation from your linked repository.

#### Export PDF

Allow visitors to export a PDF of your documentation. See [PDF export](https://gitbook.com/docs/documentation/collaboration/pdf-export) for more info.

### Privacy Policy

You can link to your own privacy policy to help visitors understand how your GitBook content uses cookies and how you protect their privacy. If you choose not to set one, your site will default to [GitBook’s privacy policy](https://gitbook.com/docs/policies/privacy-and-security/statement/cookies).



# Set a custom domain

Set a custom domain for your docs sites

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

{% hint style="warning" %}
This page shows how to configure a custom domain and subdomain. If you would like to configure a custom subdirectory (such as `example.com/docs`), see the [setting-a-custom-subdirectory](https://gitbook.com/docs/documentation/publishing-documentation/setting-a-custom-subdirectory "mention") page.
{% endhint %}

By default, your sites are accessible on a `[subdomain].gitbook.io` domain.&#x20;

You can customize this by setting a custom domain, meaning your audience can access your documentation on a chosen domain.

{% stepper %}
{% step %}

### Choose a subdomain

When choosing a subdomain, you can either use `www` or a custom one. Some commonly used subdomains are:

* `docs.example.com`
* `help.example.com`
* `developers.example.com`
  {% endstep %}

{% step %}

### Initiate the custom domain setup

Navigate to the site for which you want to set the custom domain. Click **Settings,** then choose **Set up a custom domain.**

From here, you'll see a window where you can enter the custom domain you chose in the first step. Type it out and click **Next.**
{% endstep %}

{% step %}

### Configure the DNS

At this stage, you'll see a window with three fields: **Type, Name, Target.**

Those are the details you'll use to set your custom domain in your DNS provider. This is done *outside* GitBook, in the provider you are using for your domain.

Copy the contents of the **Name** and **Target** fields to use in your DNS provider. Each provider is different, so when in doubt, check directly with them how to add this record. You should be able to pick the **Type** of record from a list in your provider.

After adding the record, it might take some time for the changes to propagate. We recommend **waiting at least 1 hour** before moving to the next step. Click **Next** when you are ready.
{% endstep %}

{% step %}

### Finalize your setup

After adding the record and it being propagated, it's time to go live! GitBook will verify the domain, the record you added and will automatically configure the SSL certificate for your domain.

Once done, you'll receive a notification and can click **Finish**. You can also close the window if you need, and we'll send you a notification once the process is done on our side.
{% endstep %}
{% endstepper %}

### Troubleshooting

Setting up a custom domain can occasionally run into obstacles. Below, we outline frequent problems encountered during this process and provide detailed solutions to each of them.

<details>

<summary>SSL error: an error occurred when provisioning your SSL certificate.</summary>

When a custom domain is set for your organization, collection, or space, we set up an SSL certificate on our end so that your documentation will load securely, over HTTPS. \
\
This happens automatically when you set your custom domain — you do not need to purchase or configure an SSL certificate.

Occasionally errors occur at this stage, usually when the CNAME record for the custom domain hasn't propagated.

In these cases, we can recommend the following:

1. Check that your CNAME record is set up correctly. \
   Please review our page about configuring DNS to help you with this. \
   If the CNAME record is incorrect, we won't be able to configure the SSL certificate and complete the custom domain set-up.&#x20;
2. Allow ***at least one hour*** between configuring the CNAME record and finalizing the custom domain setup.&#x20;
3. Verify if the CNAME has propagated. You can try using a third-party DNS lookup tool, such as [WhatsMyDNS](https://www.whatsmydns.net/), to find out what the servers believe to be correct for your correct CNAME record.&#x20;
4. If you are using Cloudflare, please confirm that you don’t have the record proxied [as explained here](https://developers.cloudflare.com/fundamentals/setup/manage-domains/pause-cloudflare/#disable-proxy-on-dns-records).

</details>

<details>

<summary>Domain already connected error: your subdomain is already configured for different content.</summary>

A custom domain assigned to a site must be unique. Attempting to use the same custom domain in more than one location will result in an error.

If this happens, you can click the link within the error message to look at the content the custom domain is already connected to. This may help you to decide what to do next.

It’s also possible that you might not have access to the content — if that’s the case, contact the support team and they can help you with your next steps.

The solution to this error will always be one of two things, however:

1. Choose a different custom domain; or
2. Disconnect the custom domain from the content it is already connected to, then reconnect it to the new content.

</details>



# Setting a custom subdirectory

Set a custom subdirectory for your docs sites

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

With a custom subdirectory, you can make your docs site accessible at `example.com/docs`. This is different from a [custom domain](https://gitbook.com/docs/documentation/publishing-documentation/custom-domain) which lets you make your docs site accessible at `docs.example.com`.&#x20;

One reason to do this is so that your docs URL is formatted in a consistent way with your other site URLs. Using a subdirectory may also be beneficial for SEO.

To configure a subdirectory, you'll need to set things up in your website's backend, then finalize the process in your GitBook site settings.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th><th data-hidden data-type="image">Cover image (dark)</th><th data-hidden data-card-cover-dark data-type="image">Cover image (dark)</th></tr></thead><tbody><tr><td>Configuring a subdirectory with Cloudflare</td><td><a href="setting-a-custom-subdirectory/configuring-a-subdirectory-with-cloudflare">configuring-a-subdirectory-with-cloudflare</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FM0E8QF3gdMCdwHMl107b%2FCloudflare.svg?alt=media&#x26;token=6a04f0d2-cccb-4668-93d3-98c9ec3890a6">Cloudflare.svg</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F3zWvv4mOHebRyQB34CHx%2FCloudflare.svg?alt=media&#x26;token=f4109747-5c4d-4039-8b33-168569f41d9d">Cloudflare.svg</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F3zWvv4mOHebRyQB34CHx%2FCloudflare.svg?alt=media&#x26;token=f4109747-5c4d-4039-8b33-168569f41d9d">Cloudflare.svg</a></td></tr><tr><td>Configuring a subdirectory with Vercel</td><td><a href="setting-a-custom-subdirectory/configuring-a-subdirectory-with-vercel">configuring-a-subdirectory-with-vercel</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FItwcojUHfxkmx4RofP6F%2FVercel.svg?alt=media&#x26;token=9cd8279b-d1f9-41f0-97e7-4f9a4eaa4a14">Vercel.svg</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F4Dra7NQYfLaHJdhBTful%2FVercel.svg?alt=media&#x26;token=e53c02a9-86fe-4ddc-8585-5cd0cef82ed4">Vercel.svg</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F4Dra7NQYfLaHJdhBTful%2FVercel.svg?alt=media&#x26;token=e53c02a9-86fe-4ddc-8585-5cd0cef82ed4">Vercel.svg</a></td></tr><tr><td>Configuring a subdirectory with AWS</td><td><a href="setting-a-custom-subdirectory/configuring-a-subdirectory-with-aws">configuring-a-subdirectory-with-aws</a></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Frq7lwbUlUQK8AOujefPf%2FAWS%20-%20light.png?alt=media&#x26;token=914054bd-a225-41f3-8f11-ff421d86fdd6">AWS - light.png</a></td><td></td><td><a href="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjY2LAVXbmW6RUmaTwXxF%2FAWS%20-%20dark.png?alt=media&#x26;token=ae589916-116d-4a29-8d59-985552addda5">AWS - dark.png</a></td></tr></tbody></table>



# Configuring a subdirectory with Cloudflare

Host your documentation with a /docs subdirectory using Cloudflare

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

{% stepper %}
{% step %}

### Configuring your GitBook site

In your GitBook organization, click on your docs site name in the sidebar, then click **Manage site** or open the **Settings** tab. Open the **Domain and redirects** section and under ‘Subdirectory’, click **Set up a subdirectory**.

Enter the URL where you would like to host your docs. Then specify the subdirectory for docs access, e.g. `tomatopy.pizza/docs`, and click **Configure**.

Under **Additional configuration**, you will now see a proxy URL. You'll use this in the next step when configuring your Cloudflare worker. Copy it to your clipboard.
{% endstep %}

{% step %}

### Create your Cloudflare worker

Sign into your Cloudflare account and navigate to **Workers & Pages**

Click the **Create** button.&#x20;

On the ‘Create an application’ screen, click the **Hello world** button in the ‘Start from a template’ card.

Give the worker a more descriptive name, like `mydocs-subpath-proxy`. Once you finish renaming the worker, click **Deploy**.&#x20;
{% endstep %}

{% step %}


## Configure your custom domain

Your worker will get a default URL that you can use. To configure your custom domain instead (such as `tomatopy.pizza`), click **Settings.** Then, in the ‘Domains & Routes’ section, click **+ Add**.

In the ‘Domains & Routes’ tray that opens, click **Custom domain**, then enter your custom domain in the textbox that follows. When you specify the custom domain, *do not* include the subdirectory. For example, `tomatopy.pizza` is correct, while `tomatopy.pizza/docs` is not.&#x20;
{% endstep %}

{% step %}

### Update the worker code

When the worker is finished deploying, click **Edit code**, or click **Continue to project**, and then the **Edit code** button in the upper right.&#x20;

In the code editor that opens, replace the sample code with the following snippet:

{% code lineNumbers="true" %}

```javascript
export default {
  fetch(request) { 
    const SUBDIRECTORY = '/docs';
    const url = new URL(request.url);
    const target = "<INSERT YOUR PROXY URL FROM GITBOOK>" + url.pathname.slice(SUBDIRECTORY.length);
    const proxy = new URL(
      target.endsWith('/') ? target.slice(0, -1) : target 
    )
    proxy.search = url.search;
    return fetch(new Request(proxy, request));
  }
};
```

{% endcode %}

{% hint style="info" %}
Be sure to update the URL on line 5 with the proxy URL you got from GitBook in the first step.
{% endhint %}

Once that’s done, click **Deploy**. This process may take a few moments. Once it’s complete, when visiting the URL, you should see your docs site!
{% endstep %}
{% endstepper %}



# Configuring a subdirectory with Vercel

Host your documentation with a /docs subdirectory using Vercel

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

{% stepper %}
{% step %}

### Configuring your GitBook site

In your GitBook organization, click on your docs site name in the sidebar, then **Manage site**, then **Domain and redirects**. Under ‘Subdirectory’, click **Set up a subdirectory**.

Enter the URL where you would like to host your docs. Then specify the subdirectory for docs access, e.g. `tomatopy.pizza/docs`, and click **Configure**.

Under **Additional configuration**, you will now see a proxy URL. You’ll use this in the next step when configuring your Vercel settings. Copy it to your clipboard.
{% endstep %}

{% step %}

### Update your vercel.json

In your Vercel app, open your `vercel.json`file (or create one in the root directory if you don't already have one). Then, add the following:

```json
{
    "rewrites": [
        {
            "source": "/docs",
            "destination": "<INSERT YOUR PROXY URL FROM GITBOOK>"
        },
        {
            "source": "/docs/:match*",
            "destination": "<INSERT YOUR PROXY URL FROM GITBOOK>/:match*"
        }
    ]
}
```

*Be sure to update the URL* on line 5 with the proxy URL you got from GitBook in the first step.
{% endstep %}

{% step %}

### Re-deploy your app and try it out!

Re-deploy your Vercel app with the update configuration. This may take a few moments. Now, when visiting the URL, you should see your docs site!
{% endstep %}
{% endstepper %}



# Configuring a subdirectory with AWS using CloudFront and Route 53

Host your documentation with a /docs subdirectory using AWS CloudFront and Route 53.

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

{% hint style="info" %}
This guide covers setting up a subdirectory using AWS CloudFront and Lambda\@Edge. This is one approach for AWS users. If you have a different AWS setup (such as a load balancer with EC2 instances running NGINX), you may need to configure your reverse proxy differently. Contact [support](https://gitbook.com/docs/help-center/further-help/how-do-i-contact-support) if you need guidance for alternative configurations.
{% endhint %}

{% stepper %}
{% step %}

#### Configuring your GitBook site

In your GitBook organization, click on your docs site name in the sidebar, then click **Manage site** or open the **Settings** tab. Open the **Domain and redirects** section and under ‘Subdirectory’, click **Set up a subdirectory**.

Enter the URL where you would like to host your docs. Then specify the subdirectory for docs access, e.g. `example.com/docs`, and click **Configure**.

Under **Additional configuration**, you will now see a proxy URL. You’ll use this in the next step when configuring your Lambda function. Copy it to your clipboard.
{% endstep %}

{% step %}

#### Create your Lambda\@Edge function

Sign into your AWS Console and navigate to **Lambda**.

Click the **Create function** button.

Choose **Author from scratch**, then:

* Give your function a descriptive name, like `gitbook-subpath-proxy.`
* Select **Node.js** as the runtime (use the latest available version).
* Leave the architecture and other settings as default.

Click **Create function**.
{% endstep %}

{% step %}

#### Update the Lambda function code

In the Lambda function editor, replace the default code with the following:

{% code lineNumbers="true" %}

```javascript
export const handler = async (event) => {
	const request = event.Records[0].cf.request;
	
	// update if your subdirectory is not /docs
	const subdirectory = '/docs';
	
	// update with your proxy URL below
	const target = new URL('<proxy URL you got from GitBook>');

	// rewrite: /docs* -> proxy.gitbook.site
	if (request.uri.startsWith(subdirectory)) {
		request.uri = target.pathname + request.uri.substring(subdirectory.length);

		// Remove trailing slash if present
		if (request.uri.endsWith('/')) {
			request.uri = request.uri.slice(0, -1);
		}

		request.origin = {
			custom: {
				domainName: target.host,
				port: 443,
				protocol: 'https',
				path: '',
				sslProtocols: ['TLSv1.2'],
				readTimeout: 30,
				keepaliveTimeout: 5,
				customHeaders: {},
			},
		};

		request.headers['host'] = [{ key: 'host', value: target.host }];
		request.headers['x-forwarded-host'] = [{ key: 'x-forwarded-host', value: target.host }];
	}
    
	return request;
};
```

{% endcode %}

{% hint style="warning" %}
Be sure to update `target` on line 8 with the proxy URL you got from GitBook in the first step. This will look like `https://proxy.gitbook.site/sites/site_XXXX`
{% endhint %}

{% hint style="warning" %}
Also be sure to update `subdirectory` on line 5 if you’re using a different subdirectory path than `/docs`.
{% endhint %}

Click **Deploy** to save your changes.
{% endstep %}

{% step %}

#### Configure Lambda permissions for Lambda\@Edge

Before you can use your Lambda function with CloudFront, you need to configure the execution role to allow Lambda\@Edge to assume it.

1. In your Lambda function, click on the **Configuration** tab
2. Click **Permissions** in the left sidebar
3. Under **Execution role**, click on the role name to open it in IAM
4. Click the **Trust relationships** tab
5. Click **Edit trust policy**
6. Replace the trust policy with the following:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "edgelambda.amazonaws.com",
                    "lambda.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Click **Update policy** to save.
{% endstep %}

{% step %}

#### Publish your Lambda function

Lambda\@Edge requires a published version (not just `$LATEST`).

1. In your Lambda function, click the **Actions** dropdown in the upper right
2. Select **Publish new version**
3. Optionally add a description like “Initial version for CloudFront”
4. Click **Publish**
5. **Important:** Copy the ARN of the published version that appears at the top of the page (it will include a version number at the end, like `arn:aws:lambda:us-east-1:123456789:function:gitbook-subpath-proxy:1`)

{% hint style="warning" %}
Lambda\@Edge functions must be created in the **us-east-1** (N. Virginia) region. If you created your function in a different region, you’ll need to recreate it in us-east-1.
{% endhint %}
{% endstep %}

{% step %}

#### Create your CloudFront distribution

Navigate to **CloudFront** in the AWS Console and click **Create distribution**.

Configure the following settings. Where settings are not specified, keep the default settings.

**Specify origin**

| Setting           | Value                                          |
| ----------------- | ---------------------------------------------- |
| **Origin type**   | Other                                          |
| **Custom origin** | Your main website domain (e.g., `example.com`) |

**Cache settings**

| Setting                   | Value                     |
| ------------------------- | ------------------------- |
| **Cache policy**          | CachingDisabled           |
| **Origin request policy** | AllViewerExceptHostHeader |

Click **Next,** select your preferred security protections, then click **Next** again.

Click **Create distribution**.

Wait for the distribution to deploy (status will change from “In Progress” to “Enabled”). This may take several minutes.
{% endstep %}

{% step %}

#### Associate Lambda\@Edge with CloudFront

Once your CloudFront distribution is deployed:

1. Click on your distribution ID to open its settings
2. Go to the **Behaviors** tab
3. Select the default behavior and click **Edit**
4. Scroll down to **Function associations**
5. Under **Origin request**, select **Lambda\@Edge**
6. In the **Lambda function ARN** field, paste the ARN of your published Lambda function (from step 5)
7. Check **Include body** to allow the function to access request bodies if needed
8. Click **Save changes**
   {% endstep %}

{% step %}

#### Configure domain and DNS records

1. On the main page of your CloudFront distribution, click the **General** tab, and under **Alternate domain names**, click **Add domain**
2. Enter the domain for which you are configuring your subdirectory e.g. `example.com` and click **Next**
3. Select your existing TLS certificate, or create a new one, if needed, and click **Next** again
   {% endstep %}

{% step %}

#### Configure Route 53 DNS records from CloudFront

If you’re using Route 53 for DNS, you’ll need to create or update your DNS records to point to your CloudFront distribution.

1. While remaining on the main page for your CloudFront distribution, make sure you are on the **General** tab, then below the URL that you have configured in **Alternate domain names,** click **Route domains to CloudFront.**
2. Click on **Set up routing automatically** to create A and AAAA DNS records for your domain

{% hint style="info" %}
If you’re not using Route 53, you’ll need to update your DNS provider’s settings to point your domain to your CloudFront distribution domain name. You can find this in the CloudFront distribution details under “Distribution domain name”.
{% endhint %}
{% endstep %}

{% step %}

#### Test your configuration

Once all changes have propagated (this can take 10–15 minutes):

1. Open a browser and navigate to your domain with the subdirectory path (e.g., `https://example.com/docs`)
2. You should see your GitBook documentation site!

If the site doesn’t load immediately, try:

* Waiting a few more minutes for DNS propagation
* Clearing your browser cache or trying an incognito window
* Running `nslookup yourdomain.com` in terminal to verify DNS is resolving correctly
* Checking CloudFront distribution status is “Enabled” and not “In Progress”

{% hint style="success" %}
Congratulations! Your GitBook documentation is now accessible via your custom subdirectory.
{% endhint %}
{% endstep %}
{% endstepper %}

### Troubleshooting

**Lambda function not triggering:**

* Ensure you published a version of your Lambda function (not using `$LATEST`)
* Verify the Lambda function is in the us-east-1 region
* Check that the trust policy includes `edgelambda.amazonaws.com`

**DNS not resolving:**

* DNS changes can take time to propagate (up to 48 hours, though usually much faster)
* Verify your Route 53 records are pointing to the correct CloudFront distribution
* Check that you deleted any old conflicting DNS records

**SSL certificate errors:**

* Ensure your SSL certificate in AWS Certificate Manager includes your custom domain
* Certificates for CloudFront must be created in the us-east-1 region

**Subdirectory not working:**

* Verify the `SUBDIRECTORY` value in your Lambda function matches what you configured in GitBook
* Check that the `target` in your Lambda function is correct
* Review CloudFront logs to see if requests are reaching the distribution



# Site settings

Customize and edit settings across your published site

{% hint style="info" %}
Certain customization features are only available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F0iwL31qTpzsWqGlbhlM1%2F18_07_25_publishing-documentation-site-settings.svg?alt=media&#x26;token=d79833ca-192f-4fea-838a-a27067b71c76" alt="A GitBook screenshot showing site settings"><figcaption><p>Update the settings for your published documentation.</p></figcaption></figure>

### General

<details>

<summary>Site title</summary>

Change the name of your site, if you don't have a custom logo this is the name that your site visitors will see.

</details>

<details>

<summary>Social preview</summary>

Here, you can upload a custom social preview image for your site. This will set the site’s `og:image` to your uploaded image, and it’ll show when the site’s link is shared to any platform or product that supports OpenGraph images, such as Slack or X.

If you don’t add a social preview, GitBook will automatically generate one using your theme color, page title and description.

If your site has multiple [site sections](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections), you can use the drop-down menu in this modal to add a custom social preview image for each one, or for your entire site.

</details>

<details>

<summary>Unpublish site</summary>

Unpublish your site, but keep its settings and customizations. You can publish your site again at any time.

</details>

<details>

<summary>Delete site</summary>

Unpublish and remove your site from the **Docs site** section in the GitBook app.

**Note:** Deleting a site is a permanent action and cannot be undone. Any settings and customizations will be lost, but your content will remain in its [space](https://gitbook.com/docs/documentation/creating-content/content-structure/space).

</details>

### Audience

<details>

<summary>Audience</summary>

Choose who sees your published content. See [publish-a-docs-site](https://gitbook.com/docs/documentation/publishing-documentation/publish-a-docs-site "mention") for more info.

</details>

<details>

<summary>Adaptive content <mark style="background-color:purple;">Ultimate</mark></summary>

Turn on adaptive content for your site pages, variants, and sections. [Adaptive content](https://gitbook.com/docs/documentation/publishing-documentation/adaptive-content) lets you hide or show content for different visitors, depending on their permissions.

Your visitor token signing key will also be displayed here.

</details>

### Domain and URL

<details>

<summary>Custom domain</summary>

Configure a custom domain to unify your site with your own branding. See [custom-domain](https://gitbook.com/docs/documentation/publishing-documentation/custom-domain "mention") for more info.

</details>

<details>

<summary>GitBook Subdirectory</summary>

Publish your content on a subdirectory (e.g. `yourcompany.com/docs`). See [#gitbook-subdirectory](#gitbook-subdirectory "mention") for more info

</details>

### Redirects

{% content-ref url="site-redirects" %}
[site-redirects](https://gitbook.com/docs/documentation/publishing-documentation/site-redirects)
{% endcontent-ref %}

### Features

<details>

<summary>PDF export <mark style="background-color:purple;">Premium &#x26; Ultimate</mark> </summary>

Let your visitors to export your GitBook as PDF. See [pdf-export](https://gitbook.com/docs/documentation/collaboration/pdf-export "mention") for more info.

</details>

<details>

<summary>Page ratings <mark style="background-color:purple;">Premium &#x26; Ultimate</mark> </summary>

Choose whether or not visitors to your published content can leave a rating on each page to let you know how they feel about it. They’ll be able to choose a sad, neutral, or happy face.

You can review the results of these ratings by opening the [**Insights**](https://gitbook.com/docs/documentation/publishing-documentation/insights) section of your docs site dashboard and selecting the [**Content scores**](https://gitbook.com/docs/documentation/insights#content-scores) tab.

</details>

### AI & MCP

<details>

<summary>Choose the AI experience <mark style="background-color:purple;">Premium &#x26; Ultimate</mark> </summary>

Let your site visitors ask GitBook anything with AI search or the GitBook assistant. See [ai-search](https://gitbook.com/docs/documentation/publishing-documentation/ai-search "mention") for more info.

</details>

<details>

<summary>Extend it with MCP connectors <mark style="background-color:purple;">Ultimate</mark> </summary>

Configure MCP servers that the AI assistant can use when answering user questions inside your docs. See [#how-do-i-use-gitbook-ai](https://gitbook.com/docs/documentation/ai-search#how-do-i-use-gitbook-ai "mention") for more info.

</details>

### Structure

{% content-ref url="site-structure" %}
[site-structure](https://gitbook.com/docs/documentation/publishing-documentation/site-structure)
{% endcontent-ref %}

### Plan

{% content-ref url="../account-management/plans" %}
[plans](https://gitbook.com/docs/documentation/account-management/plans)
{% endcontent-ref %}



# Site insights

View analytics and insights related to your published documentation’s traffic

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

Insights give you information on the content you've published and how it performs. It's split up between different sections — **Traffic**, **Pages & feedback**, **Search**, **Ask AI**, **Links**, and **OpenAPI**.

You can see a top-level overview of your insights on the **Overview** tab of your site’s dashboard, with a globe that shows views in the last hour by location.

Click the **Insights** tab in the site header to find more detailed insights for your site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2Fp2ytevUaxD0kXKzLq5qC%2F18_07_25_publishing-documentation-advanced-site-insights.svg?alt=media&#x26;token=27059941-01fd-489e-9129-73e1b5c8fdf2" alt="A GitBook screenshot showing the site insights dashboard"><figcaption><p>The site insights dashboard.</p></figcaption></figure>

### Filters & groups

You can add filters or group your data to view it in specific ways. For example, you could look at search data within a specific site section, or filter your traffic data by country, device, browser and more.

By combining filters and groups, you can drill down in to precise analytics data to track the events that you are important to you.

### View by custom time periods

You can use the drop-down menu on the right of the Insights screen to change the time period between the last 24 hours, 7 days, 30 days or 3 months.&#x20;

To view the data over a custom time period, click the **Select custom date range** button <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FkEJhwhMBwOZZGpDTRFku%2Fcalendar-dark.svg?alt=media&#x26;token=68119227-578c-4b03-920c-71c74fa2842b" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F1g9fFv9V674Y7JGjHOGw%2Fcalendar.svg?alt=media&#x26;token=d21fbc59-ac2a-46ab-82cc-2085e7d295df" alt=""></picture> to the right of the menu and choose your custom time period using the calendar that appears.

### Types of data

The Insights tab is split into six sections, each focused on a specific data type.

#### Traffic

GitBook tracks page views to help you understand the popularity and reach of your content. Each time a user visits a page on your docs site, it is counted as a page view.

Page views are critical for assessing the effectiveness of your content strategy and optimizing your documentation based on user interest. It’s split up between different views and profiles, including countries, languages, browsers, and more.

{% hint style="success" %}
Throughout the insights tab you will see Events and Visitor metrics. **Events** indicate the total number of instances for any given category, while **Visitors** indicates the unique users performing the actions.

In the context of page views, Events would be total amount of page views, and Visitors would be the count of distinct users performing a page view.
{% endhint %}

#### Pages & Feedback

Pages & feedback allow you to see a high-level representation of how your users rate your content. You’ll see an overview of all of your site’s sections and variants, and after enabling [page rating](https://gitbook.com/docs/documentation/site-settings#page-ratings-pro-and-enterprise-plans) in the **Customize** menu for a site, you can see each page’s average feedback rating.

If you want to use or analyze this data further outside of GitBook, click **Download CSV** to download a `.csv` file to your device.

You can also see a list of comments left from visitors who rate your pages, to get actionable insights on how your docs can be improved.

{% hint style="info" %}
**Why can’t I see any feedback data for my site?**\
We only display data for published sites with page ratings enabled. If your site is not published or does not have page ratings enabled, you won’t see any insights.
{% endhint %}

#### Broken URLs

Broken URLs shows any incoming links from external sources that are resulting in a ‘Page not found’ error. These may be mistyped URLs, outdated links with no redirects, or spam links.

If a broken link points to a topic that exists somewhere else in your documentation, or you simply want to direct the traffic to your primary docs, you can set up [site redirects](https://gitbook.com/docs/documentation/publishing-documentation/site-redirects) to point those visitors in the right direction.

#### Search

You can measure and improve your documentation by checking which keywords are used the most by users searching your documentation. This view allows you to see what keywords are performing the best, and which ones you could improve on.

The information here can be helpful for informing your content architecture, making certain parts of your documentation easier to find without search, or adding additional content to existing pages based on what your visitors are searching for.

#### Ask AI

The [Ask AI](https://gitbook.com/docs/documentation/creating-content/searching-your-content/gitbook-ai) section allows you to see what your users are asking for when using GitBook AI. This insight helps you identify common questions, uncover gaps in your documentation, and improve content to better meet user needs.

You can also see how users are rating the answers that AI gives to their questions. By looking at these queries and their ratings, you can refine your documentation structure, enhance discoverability, and identify areas that would benefit from more documented information.

#### Links

GitBook tracks links to help you understand how users interact with external resources in your documentation. This feature provides insights into external links, their domains, and their placement within your docs, such as in the header, footer, or sidebar. Analyzing link usage can help you optimize navigation, improve content accessibility, and refine your documentation strategy based on user engagement.

#### OpenAPI

The [OpenAPI](https://gitbook.com/docs/documentation/api-references/openapi) analytics view in GitBook provides insights into how users engage with your API documentation.

It tracks interactions such as endpoint views, parameter searches, and request explorations, helping you understand which parts of your API are most accessed and where users may need more clarity. These insights enable you to refine your documentation, improve developer experience, and ensure your API content is effectively meeting user needs.



# Site redirects

Set up site redirects to route traffic to content anywhere on your site.

{% hint style="info" %}
This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).
{% endhint %}

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FG4YuVeNPaMd8T5hsuudf%2FRedirects.svg?alt=media&#x26;token=b0de74e3-8610-442e-ba12-2a980b15425c" alt="A GitBook screenshot showing site redirects"><figcaption><p>Site redirects are useful when migrating documentation or restructuring content to avoid broken links, which can impact SEO.</p></figcaption></figure>

Redirects are commonly used when you are migrating your documentation from one provider to another — like when you just moved docs to GitBook. Broken links can impact SEO so we recommend setting up redirects where needed.

In addition to [automatic redirects created by GitBook](#about-automatic-redirects), you can create a redirect from any path in your site’s domain.


## Managing redirects on your site

To get started, view your site’s dashboard in GitBook and open the **Settings** tab, then click **Domain & redirects**.

### Creating redirects

Click **Add redirect** to begin. Fill in the source path — i.e. the URL slug that you wish to redirect somewhere else — and the destination content you wish to link to. You can pick any [section](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/site-sections), [variant](https://gitbook.com/docs/documentation/publishing-documentation/site-structure/variants), or [page](https://gitbook.com/docs/documentation/creating-content/content-structure/page) on to your site. Click **Add** to create the redirect.

If you want to add another redirect to the same page, you can toggle the **Add another redirect** option on before you hit **Add**. When you add your redirect, the modal will remain open with the destination content set to the previous selection so you can add another URL slug immediately.

### Editing redirects

To edit a redirect, press the **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> icon next to it in the list. Update the redirect and hit **Save**.

To delete a redirect, press the **Delete redirect** button and confirm.


## About automatic redirects

Whenever pages are moved or renamed, their canonical URL changes with them. In order to keep your content accessible, GitBook automatically creates a [HTTP 307](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/307) redirect from the old URL to the new one.

Every time a URL is loaded, GitBook resolves it through the following steps:

1. Site content is resolved to its canonical URL by following any of the automatically created redirects.
2. If the URL cannot be resolved, the URL is checked against [space-level redirects](https://gitbook.com/docs/documentation/getting-started/git-sync/content-configuration#redirects), defined in your repository's `.gitbook.yaml` file.
3. Finally, the URL is checked against site-level redirects, created via [the process above](#creating-redirects).



---
**Navigation:** [← Previous](./03-variables-and-expressions.md) | [Index](./index.md) | [Next →](./05-authenticated-access.md)
