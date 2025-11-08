**Navigation:** [← Previous](./03-mermaid.md) | [Index](./index.md) | [Next →](./05-gitlab.md)

# Fonts
Source: https://mintlify.com/docs/customize/fonts

Configure custom fonts

Set a custom font for your entire site or separately for headings and body text. Use Google Fonts, local font files, or externally hosted fonts. The default font varies by theme.

Fonts are controlled by the [fonts property](/organize/settings#param-fonts) in your `docs.json`.


## Google Fonts

Mintlify automatically loads [Google Fonts](https://fonts.google.com) when you specify a font family name in your `docs.json`.

```json docs.json theme={null}
"fonts": {
  "family": "Inter"
}
```


## Local fonts

To use local fonts, place your font files in your project directory and reference them in your `docs.json` configuration.

### Setting up local fonts

<Steps>
  <Step title="Add font files to your project">
    For example, create a `fonts` directory and add your font files:

    ```text  theme={null}
    your-project/
    ├── fonts/
    │   ├── InterDisplay-Regular.woff2
    │   └── InterDisplay-Bold.woff2
    ├── docs.json
    └── ...
    ```
  </Step>

  <Step title="Configure fonts in docs.json">
    Reference your local fonts using relative paths from your project root:

    ```json docs.json theme={null}
    {
      "fonts": {
        "family": "InterDisplay",
        "source": "/fonts/InterDisplay-Regular.woff2",
        "format": "woff2",
        "weight": 400
      }
    }
    ```
  </Step>
</Steps>

### Local fonts for headings and body

Configure separate local fonts for headings and body text in your `docs.json`:

```json docs.json theme={null}
{
  "fonts": {
    "heading": {
      "family": "InterDisplay",
      "source": "/fonts/InterDisplay-Bold.woff2",
      "format": "woff2",
      "weight": 700
    },
    "body": {
      "family": "InterDisplay",
      "source": "/fonts/InterDisplay-Regular.woff2",
      "format": "woff2",
      "weight": 400
    }
  }
}
```


## Externally hosted fonts

Use externally hosted fonts by referencing a font source URL in your `docs.json`:

```json docs.json theme={null}
{
  "fonts": {
    "family": "Hubot Sans",
    "source": "https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2",
    "format": "woff2",
    "weight": 400
  }
}
```


## Font configuration reference

<ResponseField name="fonts" type="object">
  Font configuration for your documentation.

  <Expandable title="Fonts">
    <ResponseField name="family" type="string" required>
      Font family name, such as "Inter" or "Playfair Display".
    </ResponseField>

    <ResponseField name="weight" type="number">
      Font weight, such as 400 or 700. Variable fonts support precise weights such as 550.
    </ResponseField>

    <ResponseField name="source" type="string (uri)">
      URL to your font source, such as `https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2`, or path to your local font file, such as `/assets/fonts/InterDisplay.woff2`. Google Fonts are loaded automatically when you specify a Google Font `family` name, so no source URL is needed.
    </ResponseField>

    <ResponseField name="format" type="'woff' | 'woff2'">
      Font file format. Required when using the `source` field.
    </ResponseField>

    <ResponseField name="heading" type="object">
      Override font settings specifically for headings.

      <Expandable title="Heading">
        <ResponseField name="family" type="string" required>
          Font family name for headings.
        </ResponseField>

        <ResponseField name="weight" type="number">
          Font weight for headings.
        </ResponseField>

        <ResponseField name="source" type="string (uri)">
          URL to your font source, such as `https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2`, or path to your local font file for headings. Google Fonts are loaded automatically when you specify a Google Font `family` name, so no source URL is needed.
        </ResponseField>

        <ResponseField name="format" type="'woff' | 'woff2'">
          Font file format for headings. Required when using the `source` field.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="body" type="object">
      Override font settings specifically for body text.

      <Expandable title="Body">
        <ResponseField name="family" type="string" required>
          Font family name for body text.
        </ResponseField>

        <ResponseField name="weight" type="number">
          Font weight for body text.
        </ResponseField>

        <ResponseField name="source" type="string (uri)">
          URL to your font source, such as `https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2`, or path to your local font file for body text. Google Fonts are loaded automatically when you specify a Google Font `family` name, so no source URL is needed.
        </ResponseField>

        <ResponseField name="format" type="'woff' | 'woff2'">
          Font file format for body text. Required when using the `source` field.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>



# React
Source: https://mintlify.com/docs/customize/react-components

Build interactive and reusable elements with React components

export const ColorGenerator = () => {
  const [hue, setHue] = useState(165);
  const [saturation, setSaturation] = useState(84);
  const [lightness, setLightness] = useState(31);
  const [colors, setColors] = useState([]);
  useEffect(() => {
    const newColors = [];
    for (let i = 0; i < 5; i++) {
      const l = Math.max(10, Math.min(90, lightness - 20 + i * 10));
      newColors.push(`hsl(${hue}, ${saturation}%, ${l}%)`);
    }
    setColors(newColors);
  }, [hue, saturation, lightness]);
  const copyToClipboard = color => {
    navigator.clipboard.writeText(color).then(() => {
      console.log(`Copied ${color} to clipboard!`);
    }).catch(err => {
      console.error("Failed to copy: ", err);
    });
  };
  return <div className="p-4 border dark:border-white/10 rounded-2xl not-prose">
      <div className="space-y-4">
        <div className="space-y-2">
          <label className="block text-sm text-zinc-950/70 dark:text-white/70">
            Hue: {hue}°
            <input type="range" min="0" max="360" value={hue} onChange={e => setHue(Number.parseInt(e.target.value))} className="w-full h-2 bg-zinc-950/20 rounded-lg appearance-none cursor-pointer dark:bg-white/20 mt-1" style={{
    background: `linear-gradient(to right, 
                  hsl(0, ${saturation}%, ${lightness}%), 
                  hsl(60, ${saturation}%, ${lightness}%), 
                  hsl(120, ${saturation}%, ${lightness}%), 
                  hsl(180, ${saturation}%, ${lightness}%), 
                  hsl(240, ${saturation}%, ${lightness}%), 
                  hsl(300, ${saturation}%, ${lightness}%), 
                  hsl(360, ${saturation}%, ${lightness}%))`
  }} />
          </label>

          <label className="block text-sm text-zinc-950/70 dark:text-white/70">
            Saturation: {saturation}%
            <input type="range" min="0" max="100" value={saturation} onChange={e => setSaturation(Number.parseInt(e.target.value))} className="w-full h-2 bg-zinc-950/20 rounded-lg appearance-none cursor-pointer dark:bg-white/20 mt-1" style={{
    background: `linear-gradient(to right, 
                  hsl(${hue}, 0%, ${lightness}%), 
                  hsl(${hue}, 50%, ${lightness}%), 
                  hsl(${hue}, 100%, ${lightness}%))`
  }} />
          </label>

          <label className="block text-sm text-zinc-950/70 dark:text-white/70">
            Lightness: {lightness}%
            <input type="range" min="0" max="100" value={lightness} onChange={e => setLightness(Number.parseInt(e.target.value))} className="w-full h-2 bg-zinc-950/20 rounded-lg appearance-none cursor-pointer dark:bg-white/20 mt-1" style={{
    background: `linear-gradient(to right, 
                  hsl(${hue}, ${saturation}%, 0%), 
                  hsl(${hue}, ${saturation}%, 50%), 
                  hsl(${hue}, ${saturation}%, 100%))`
  }} />
          </label>
        </div>

        <div className="flex space-x-2">
          {colors.map((color, idx) => <div key={idx} className="h-16 rounded flex-1 cursor-pointer transition-transform hover:scale-105" style={{
    backgroundColor: color
  }} title={`Click to copy: ${color}`} onClick={() => copyToClipboard(color)} />)}
        </div>

        <div className="text-sm font-mono text-zinc-950/70 dark:text-white/70">
          <p>
            Base color: hsl({hue}, {saturation}%, {lightness}%)
          </p>
        </div>
      </div>
    </div>;
};

[React components](https://react.dev) are a powerful way to create interactive and reusable elements in your documentation.


## Using React components

You can build React components directly in your `MDX` files using [React hooks](https://react.dev/reference/react/hooks).

### Example

This example declares a `Counter` component and then uses it with `<Counter />`.

```mdx  theme={null}
export const Counter = () => {
  const [count, setCount] = useState(0)

  const increment = () => setCount(count + 1)
  const decrement = () => setCount(count - 1)

  return (
  <div className="flex items-center justify-center">
      <div className="flex items-center rounded-xl overflow-hidden border border-zinc-950/20 dark:border-white/20">
        <button
          onClick={decrement}
          className="flex items-center justify-center h-8 w-8 text-zinc-950/80 dark:text-white/80 border-r border-zinc-950/20 dark:border-white/20"
          aria-label="Decrease"
        >
          -
        </button>

        <div className="flex text-sm items-center justify-center h-8 px-6 text-zinc-950/80 dark:text-white/80 font-medium min-w-[4rem] text-center">
          {count}
        </div>

        <button
          onClick={increment}
          className="flex items-center justify-center h-8 w-8 text-zinc-950/80 dark:text-white/80 border-l border-zinc-950/20 dark:border-white/20"
          aria-label="Increase"
        >
          +
        </button>
      </div>
    </div>
  )
}

<Counter />
```

export const Counter = () => {
  const [count, setCount] = useState(0);
  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);
  return <div className="flex items-center justify-center">
      <div className="flex items-center rounded-xl overflow-hidden border border-zinc-950/20 dark:border-white/20">
        <button onClick={decrement} className="flex items-center justify-center h-8 w-8 text-zinc-950/80 dark:text-white/80 border-r border-zinc-950/20 dark:border-white/20" aria-label="Decrease">
          -
        </button>

        <div className="flex text-sm items-center justify-center h-8 px-6 text-zinc-950/80 dark:text-white/80 font-medium min-w-[4rem] text-center">
          {count}
        </div>

        <button onClick={increment} className="flex items-center justify-center h-8 w-8 text-zinc-950/80 dark:text-white/80 border-l border-zinc-950/20 dark:border-white/20" aria-label="Increase">
          +
        </button>
      </div>
    </div>;
};


The counter renders as an interactive React component.

<Counter />


## Importing components

To import React components in your `MDX` files, the component files must be located in the `snippets` folder. You can then import them into any `MDX` page in your documentation. Learn more about [reusable snippets](/create/reusable-snippets).

### Example

This example declares a `ColorGenerator` component that uses multiple React hooks and then uses it in an `MDX` file.

Create `color-generator.jsx` file in the `snippets` folder:

```mdx /snippets/color-generator.jsx [expandable] theme={null}
export const ColorGenerator = () => {
  const [hue, setHue] = useState(180)
  const [saturation, setSaturation] = useState(50)
  const [lightness, setLightness] = useState(50)
  const [colors, setColors] = useState([])

  useEffect(() => {
    const newColors = []
    for (let i = 0; i < 5; i++) {
      const l = Math.max(10, Math.min(90, lightness - 20 + i * 10))
      newColors.push(`hsl(${hue}, ${saturation}%, ${l}%)`)
    }
    setColors(newColors)
  }, [hue, saturation, lightness])

  const copyToClipboard = (color) => {
    navigator.clipboard
      .writeText(color)
      .then(() => {
        console.log(`Copied ${color} to clipboard!`)
      })
      .catch((err) => {
        console.error("Failed to copy: ", err)
      })
  }

  return (
    <div className="p-4 border dark:border-zinc-950/80 rounded-xl not-prose">
      <div className="space-y-4">
        <div className="space-y-2">
          <label className="block text-sm text-zinc-950/70 dark:text-white/70">
            Hue: {hue}°
            <input
              type="range"
              min="0"
              max="360"
              value={hue}
              onChange={(e) => setHue(Number.parseInt(e.target.value))}
              className="w-full h-2 bg-zinc-950/20 rounded-lg appearance-none cursor-pointer dark:bg-white/20 mt-1"
              style={{
                background: `linear-gradient(to right, 
                  hsl(0, ${saturation}%, ${lightness}%), 
                  hsl(60, ${saturation}%, ${lightness}%), 
                  hsl(120, ${saturation}%, ${lightness}%), 
                  hsl(180, ${saturation}%, ${lightness}%), 
                  hsl(240, ${saturation}%, ${lightness}%), 
                  hsl(300, ${saturation}%, ${lightness}%), 
                  hsl(360, ${saturation}%, ${lightness}%))`,
              }}
            />
          </label>

          <label className="block text-sm text-zinc-950/70 dark:text-white/70">
            Saturation: {saturation}%
            <input
              type="range"
              min="0"
              max="100"
              value={saturation}
              onChange={(e) => setSaturation(Number.parseInt(e.target.value))}
              className="w-full h-2 bg-zinc-950/20 rounded-lg appearance-none cursor-pointer dark:bg-white/20 mt-1"
              style={{
                background: `linear-gradient(to right, 
                  hsl(${hue}, 0%, ${lightness}%), 
                  hsl(${hue}, 50%, ${lightness}%), 
                  hsl(${hue}, 100%, ${lightness}%))`,
              }}
            />
          </label>

          <label className="block text-sm text-zinc-950/70 dark:text-white/70">
            Lightness: {lightness}%
            <input
              type="range"
              min="0"
              max="100"
              value={lightness}
              onChange={(e) => setLightness(Number.parseInt(e.target.value))}
              className="w-full h-2 bg-zinc-950/20 rounded-lg appearance-none cursor-pointer dark:bg-white/20 mt-1"
              style={{
                background: `linear-gradient(to right, 
                  hsl(${hue}, ${saturation}%, 0%), 
                  hsl(${hue}, ${saturation}%, 50%), 
                  hsl(${hue}, ${saturation}%, 100%))`,
              }}
            />
          </label>
        </div>

        <div className="flex space-x-1">
          {colors.map((color, idx) => (
            <div
              key={idx}
              className="h-16 rounded flex-1 cursor-pointer transition-transform hover:scale-105"
              style={{ backgroundColor: color }}
              title={`Click to copy: ${color}`}
              onClick={() => copyToClipboard(color)}
            />
          ))}
        </div>

        <div className="text-sm font-mono text-zinc-950/70 dark:text-white/70">
          <p>
            Base color: hsl({hue}, {saturation}%, {lightness}%)
          </p>
        </div>
      </div>
    </div>
  )
}
```

Import the `ColorGenerator` component and use it in an `MDX` file:

```mdx  theme={null}
import { ColorGenerator } from "/snippets/color-generator.jsx"

<ColorGenerator />
```

The color generator renders as an interactive React component.

<ColorGenerator />


## Considerations

<AccordionGroup>
  <Accordion title="Client-side rendering impact">
    React hook components render on the client-side, which has several implications:

    * **SEO**: Search engines might not fully index dynamic content.
    * **Initial load**: Visitors may experience a flash of loading content before components render.
    * **Accessibility**: Ensure dynamic content changes are announced to screen readers.
  </Accordion>

  <Accordion title="Performance best practices">
    * **Optimize dependency arrays**: Include only necessary dependencies in your `useEffect` dependency arrays.
    * **Memoize complex calculations**: Use `useMemo` or `useCallback` for expensive operations.
    * **Reduce re-renders**: Break large components into smaller ones to prevent cascading re-renders.
    * **Lazy loading**: Consider lazy loading complex components to improve initial page load time.
  </Accordion>
</AccordionGroup>



# Themes
Source: https://mintlify.com/docs/customize/themes

Customize the appearance of your documentation

export const ThemeCard = ({title, value, description, href}) => {
  return <a className="mt-4 gap-10 group cursor-pointer" href={href}>
      <div>
        <img className="mt-0 rounded-2xl group-hover:scale-105 transition-all block dark:hidden" src={`https://mintlify.s3.us-west-1.amazonaws.com/mintlify/images/themes/${value}-light.png`} alt={title} noZoom />
        <img className="mt-0 rounded-2xl group-hover:scale-105 transition-all hidden dark:block" src={`https://mintlify.s3.us-west-1.amazonaws.com/mintlify/images/themes/${value}-dark.png`} alt={title} noZoom />
      </div>
      <div>
        <div className="mt-4 flex space-x-2 items-center">
        <h4 className="text-base font-medium text-gray-900 dark:text-gray-200">{title}</h4>
        <label className="text-sm text-gray-500 dark:text-gray-400">"{value}"</label>
      </div>
        <div class="mt-1 prose-sm prose-gray mb-2 text-gray-500 dark:text-gray-400">{description}</div>
        <div className="flex items-center gap-1 mt-2 text-green-600 group-hover:text-green-800 dark:text-green-500 dark:group-hover:text-green-400">
          <span className="text-sm font-medium">
            See preview
          </span>
          <svg className="size-3 group-hover:translate-x-0.5 transition-all" width="14" height="15" viewBox="0 0 14 15" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M5.05566 2.70996L9.91678 7.57107L5.05566 12.4322" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </div>
      </div>
    </a>;
};


<div className="pt-10 pb-24 px-4 px-4 max-w-3xl mx-auto prose prose-gray">
  <label className="eyebrow h-5 text-primary dark:text-primary-light text-sm font-semibold">Core Concepts</label>
  <h1 className="mt-1 mb-2 text-2xl sm:text-3xl text-gray-900 tracking-tight dark:text-gray-200 font-semibold">Themes</h1>
  <label className="text-lg prose prose-gray dark:prose-invert">Customize the appearance of your documentation<br /><br />Configure [theme](/organize/settings#param-theme) in docs.json using one of the following themes.</label>

  <br />

  <div className="mt-10 grid grid-cols-1 sm:grid-cols-2 gap-8 not-prose">
    <ThemeCard title="Mint" value="mint" description="Classic documentation theme with time-tested layouts and familiar navigation." href="https://mint.mintlify.app" />

    <ThemeCard title="Maple" value="maple" description="Modern, clean aesthetics perfect for AI and SaaS products." href="https://maple.mintlify.app" />

    <ThemeCard title="Palm" value="palm" description="Sophisticated fintech theme with deep customization for enterprise documentation." href="https://palm.mintlify.app" />

    <ThemeCard title="Willow" value="willow" description="Stripped-back essentials for distraction-free documentation." href="https://willow.mintlify.app" />

    <ThemeCard title="Linden" value="linden" description="Retro terminal vibes with monospace fonts for that 80s hacker aesthetic." href="https://linden.mintlify.app" />

    <ThemeCard title="Almond" value="almond" description="Card-based organization meets minimalist design for intuitive navigation." href="https://almond.mintlify.app" />

    <ThemeCard title="Aspen" value="aspen" description="Modern documentation crafted for complex navigation and custom components." href="https://aspen.mintlify.app" />
  </div>
</div>



# Editor permissions
Source: https://mintlify.com/docs/dashboard/permissions

Allow more members of your team to update your docs

An editor has access to your dashboard and web editor.

Anyone can contribute to your documentation by working locally and pushing changes to your repository, but there are key differences in how changes get deployed:

* **Editor changes**: When an editor publishes through the web editor or merges a pull request into your docs repository, changes deploy to your live site automatically.
* **Non-editor changes**: When a non-editor merges a pull request into your repository, you must manually trigger a deployment from your dashboard for those changes to appear on your live site.


## Add editors

By default, the team member who created your Mintlify organization has editor access. Add additional editors in the [Members](https://dashboard.mintlify.com/settings/organization/members) page of your dashboard.

Editor seats are billed based on usage, and you can have as many editors as you need. See our [pricing page](https://mintlify.com/pricing) for more details.



# Roles
Source: https://mintlify.com/docs/dashboard/roles

Control access to your dashboard with roles.

<Info>
  RBAC functionality is available on [Enterprise plan](https://mintlify.com/pricing?ref=rbac).
</Info>

Mintlify provides two dashboard access levels: Editor and Admin.

The following describes actions that are limited to the Admin role:

|                         | Editor | Admin |
| ----------------------- | :----: | :---: |
| Update user roles       |    ❌   |   ✅   |
| Delete users            |    ❌   |   ✅   |
| Invite admin users      |    ❌   |   ✅   |
| Manage & update billing |    ❌   |   ✅   |
| Update custom domain    |    ❌   |   ✅   |
| Update Git source       |    ❌   |   ✅   |
| Delete org              |    ❌   |   ✅   |

Other actions on the dashboard are available to both roles.

You can invite as many admins as you want, but we recommend limiting admin
access to users who need it.



# Single sign-on (SSO)
Source: https://mintlify.com/docs/dashboard/sso

Customize how your team can login to your admin dashboard

<Info>
  SSO functionality is available on [Enterprise plan](https://mintlify.com/pricing?ref=sso).
</Info>

Use single sign-on to your dashboard via SAML and OIDC. If you use Okta, Google Workspace, or Microsoft Entra, we have provider-specific documentation for setting up SSO. If you use another provider, please [contact us](mailto:support@mintlify.com).


## Okta

<Tabs>
  <Tab title="SAML">
    <Steps>
      <Step title="Create an application">
        Under `Applications`, click to create a new app integration using SAML 2.0.
      </Step>

      <Step title="Configure integration">
        Enter the following:

        * Single sign-on URL (provided by Mintlify)
        * Audience URI (provided by Mintlify)
        * Name ID Format: `EmailAddress`
        * Attribute Statements:
          | Name        | Name format | Value            |
          | ----------- | ----------- | ---------------- |
          | `firstName` | Basic       | `user.firstName` |
          | `lastName`  | Basic       | `user.lastName`  |
      </Step>

      <Step title="Send us your IdP information">
        Once the application is set up, navigate to the sign-on tab and send us the metadata URL.
        We'll enable the connection from our side using this information.
      </Step>
    </Steps>
  </Tab>

  <Tab title="OIDC">
    <Steps>
      <Step title="Create an application">
        Under `Applications`, click to create a new app integration using OIDC.
        You should choose the `Web Application` application type.
      </Step>

      <Step title="Configure integration">
        Select the authorization code grant type and enter the Redirect URI provided by Mintlify.
      </Step>

      <Step title="Send us your IdP information">
        Once the application is set up, navigate to the General tab and locate the client ID & client secret.
        Please securely provide us with these, along with your Okta instance URL (for example, `<your-tenant-name>.okta.com`). You can send these via a service like 1Password or SendSafely.
      </Step>
    </Steps>
  </Tab>
</Tabs>


## Google Workspace

<Tabs>
  <Tab title="SAML">
    <Steps>
      <Step title="Create an application">
        Under `Web and mobile apps`, select `Add custom SAML app` from the `Add app` dropdown.

        <Frame>
                    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2c06c394d98ccd65df92aefceaeb75bd" alt="Screenshot of the Google Workspace SAML application creation page with the &#x22;Add custom SAML app&#x22; menu item highlighted" data-og-width="3804" width="3804" data-og-height="1860" height="1860" data-path="images/gsuite-add-custom-saml-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=58b064984b59e740ca9582b2a38cb0b5 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=f75867bfc7b0e654f04279d7a00bdec2 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7d0fd19fd1ac1179f7aabad274a68e99 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=07236708f5e41547a94a37e66c329eee 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=370f4a956ba1cdc9a68462b30dcafbe4 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-add-custom-saml-app.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=86bf0fe1bd0cc718d664de30562572ad 2500w" />
        </Frame>
      </Step>

      <Step title="Send us your IdP information">
        Copy the provided SSO URL, Entity ID, and x509 certificate and send it to the Mintlify team.

        <Frame>
                    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e9e47998599205dc051e9402cba63756" alt="Screenshot of the Google Workspace SAML application page with the SSO URL, Entity ID, and x509 certificate highlighted. The specific values for each of these are blurred out." data-og-width="3800" width="3800" data-og-height="1850" height="1850" data-path="images/gsuite-saml-metadata.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a469394b3fbf66b8d441e2a3e863da09 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1a301ea732963fff823ddce7e2eef92f 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=00000d64cf4aacf28853dec9c7c91196 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ce6f9c692ca3c1c44c8d4c78f0640c55 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5b4eb469d04332f194a0c7f36a17c81e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-saml-metadata.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4d2ec0991511cfd65f6fe159954d53db 2500w" />
        </Frame>
      </Step>

      <Step title="Configure integration">
        On the Service provider details page, enter the following:

        * ACS URL (provided by Mintlify)
        * Entity ID (provided by Mintlify)
        * Name ID format: `EMAIL`
        * Name ID: `Basic Information > Primary email`

        <Frame>
                    <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a410a25f000fe2bc4d735a6ebe7754da" alt="Screenshot of the Service provider details page with the ACS URL and Entity ID input fields highlighted." data-og-width="3788" width="3788" data-og-height="1864" height="1864" data-path="images/gsuite-sp-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9aa71205fdffa7fd1fa0ae6f3e62bc40 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=fbf8277d0af0c0bbbc20f75cd59b0087 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0ef2f4b39b42c91fc26b34082dc9f928 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=98d60575ac7013ac2632d505a4d66a32 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1f97959e4cad04acfb8741400a701694 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gsuite-sp-details.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b76f846f6f82dcb3d897e21786c8dc24 2500w" />
        </Frame>

        On the next page, enter the following attribute statements:

        | Google Directory Attribute | App Attribute |
        | -------------------------- | ------------- |
        | `First name`               | `firstName`   |
        | `Last name`                | `lastName`    |

        Once this step is complete and users are assigned to the application, let our team know and we'll enable SSO for your account!
      </Step>
    </Steps>
  </Tab>
</Tabs>


## Microsoft Entra

<Tabs>
  <Tab title="SAML">
    <Steps>
      <Step title="Create an application">
        1. Under "Enterprise applications," select **New application**.
        2. Select **Create your own application** and choose "Integrate any other application you don't find in the gallery (Non-gallery)."
      </Step>

      <Step title="Configure SAML">
        Navigate to the Single Sign-On setup page and select **SAML**. Under "Basic SAML Configuration," enter the following:

        * Identifier (Entity ID): The Audience URI provided by Mintlify.
        * Reply URL (Assertion Consumer Service URL): The ACS URL provided by Mintlify.

        Leave the other values blank and select **Save**.
      </Step>

      <Step title="Configure Attributes & Claims">
        Edit the Attributes & Claims section:

        1. Select **Unique User Identifier (Name ID)** under "Required Claim."
        2. Change the Source attribute to use `user.primaryauthoritativeemail`.
        3. Under Additional claims, create the following claims:
           | Name        | Value            |
           | ----------- | ---------------- |
           | `firstName` | `user.givenname` |
           | `lastName`  | `user.surname`   |
      </Step>

      <Step title="Send Mintlify your IdP information">
        Once the application is set up, navigate to the "SAML Certificates" section and send us the App Federation Metadata URL.
        We'll enable the connection from our side using this information.
      </Step>

      <Step title="Assign Users">
        Navigate to "Users and groups" in your Entra application and add the users who should have access to your dashboard.
      </Step>
    </Steps>
  </Tab>
</Tabs>



# Authentication setup
Source: https://mintlify.com/docs/deploy/authentication-setup

Control the privacy of your docs by authenticating users

<Info>
  [Pro plans](https://mintlify.com/pricing?ref=authentication) include password authentication.

  [Custom plans](https://mintlify.com/pricing?ref=authentication) include all authentication methods.
</Info>

Authentication requires users to log in before accessing your documentation.


## Authentication modes

Choose between full and partial authentication modes based on your access control needs.

**Full authentication**: All pages are protected. Users must log in before accessing any content.

**Partial authentication**: Some pages are publicly viewable while others require authentication. Users can browse public content freely and authenticate only when accessing protected pages.

When configuring any handshake method below, you'll select either **Full authentication** or **Partial authentication** in your dashboard settings.


## Configuring authentication

Select the handshake method that you want to configure.

<Tabs>
  <Tab title="Password">
    <Info>
      Password authentication provides access control only and does **not** support content personalization.
    </Info>

    ### Prerequisites

    * Your security requirements allow sharing passwords among users.

    ### Implementation

    <Steps>
      <Step title="Create a password.">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Full Authentication** or **Partial Authentication**.
        3. Select **Password**.
        4. Enter a secure password.
        5. Select **Save changes**.
      </Step>

      <Step title="Distribute access.">
        Securely share the password and documentation URL with authorized users.
      </Step>
    </Steps>

    ## Example

    Your documentation is hosted at `docs.foo.com` and you need basic access control without tracking individual users. You want to prevent public access while keeping setup simple.

    **Create a strong password** in your dashboard. **Share credentials** with authorized users. That's it!
  </Tab>

  <Tab title="Mintlify Dashboard">
    ### Prerequisites

    * Your documentation users are also your documentation editors.

    ### Implementation

    <Steps>
      <Step title="Enable Mintlify dashboard authentication.">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Full Authentication** or **Partial Authentication**.
        3. Select **Mintlify Auth**.
        4. Select **Enable Mintlify Auth**.
      </Step>

      <Step title="Add authorized users.">
        1. In your dashboard, go to [Members](https://dashboard.mintlify.com/settings/organization/members).
        2. Add each person who should have access to your documentation.
        3. Assign appropriate roles based on their editing permissions.
      </Step>
    </Steps>

    ### Example

    Your documentation is hosted at `docs.foo.com` and your team uses the dashboard to edit your docs. You want to restrict access to team members only.

    **Enable Mintlify authentication** in your dashboard settings.

    **Verify team access** by checking that all team members are added to your organization.
  </Tab>

  <Tab title="OAuth 2.0">
    ### Prerequisites

    * An OAuth or OIDC server that supports the Authorization Code Flow.
    * Ability to create an API endpoint accessible by OAuth access tokens (optional, to enable personalization features).

    ### Implementation

    <Steps>
      <Step title="Configure your OAuth settings.">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Full Authentication** or **Partial Authentication**.
        3. Select **OAuth** and configure these fields:

        * **Authorization URL**: Your OAuth endpoint.
        * **Client ID**: Your OAuth 2.0 client identifier.
        * **Client Secret**: Your OAuth 2.0 client secret.
        * **Scopes**: Permissions to request. Copy the **entire** scope string (for example, for a scope like `provider.users.docs`, copy the complete `provider.users.docs`). Use multiple scopes if you need different access levels.
        * **Token URL**: Your OAuth token exchange endpoint.
        * **Info API URL** (optional): Endpoint to retrieve user info for personalization. If omitted, the OAuth flow will only be used to verify identity and the user info will be empty.
        * **Logout URL**: The native logout URL for your OAuth provider. If your provider has a `returnTo` or similar parameter, point it back to your docs URL.

        4. Select **Save changes**.
      </Step>

      <Step title="Configure your OAuth server.">
        1. Copy the **Redirect URL** from your [authentication settings](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Add the redirect URL as an authorized redirect URL for your OAuth server.
      </Step>

      <Step title="Create your user info endpoint (optional).">
        To enable personalization features, create an API endpoint that:

        * Accepts OAuth access tokens for authentication.
        * Returns user data in the `User` format. See [User data format](/deploy/personalization-setup#user-data-format) for more information.

        Add this endpoint URL to the **Info API URL** field in your [authentication settings](https://dashboard.mintlify.com/settings/deployment/authentication).
      </Step>
    </Steps>

    ### Example

    Your documentation is hosted at `foo.com/docs` and you have an existing OAuth server at `auth.foo.com` that supports the Authorization Code Flow.

    **Configure your OAuth server details** in your dashboard:

    * **Authorization URL**: `https://auth.foo.com/authorization`
    * **Client ID**: `ydybo4SD8PR73vzWWd6S0ObH`
    * **Scopes**: `['provider.users.docs']`
    * **Token URL**: `https://auth.foo.com/exchange`
    * **Info API URL**: `https://api.foo.com/docs/user-info`
    * **Logout URL**: `https://auth.foo.com/logout?returnTo=https%3A%2F%2Ffoo.com%2Fdocs`

    **Create a user info endpoint** at `api.foo.com/docs/user-info`, which requires an OAuth access token with the `provider.users.docs` scope, and returns:

    ```json  theme={null}
    {
      "content": {
        "firstName": "Jane",
        "lastName": "Doe"
      },
      "groups": ["engineering", "admin"]
    }
    ```

    **Configure your OAuth server to allow redirects** to your callback URL.
  </Tab>

  <Tab title="JWT">
    ### Prerequisites

    * An authentication system that can generate and sign JWTs.
    * A backend service that can create redirect URLs.

    ### Implementation

    <Steps>
      <Step title="Generate a private key.">
        1. In your dashboard, go to [Authentication](https://dashboard.mintlify.com/settings/deployment/authentication).
        2. Select **Full Authentication** or **Partial Authentication**.
        3. Select **JWT**.
        4. Enter the URL of your existing login flow and select **Save changes**.
        5. Select **Generate new key**.
        6. Store your key securely where it can be accessed by your backend.
      </Step>

      <Step title="Integrate Mintlify authentication into your login flow.">
        Modify your existing login flow to include these steps after user authentication:

        * Create a JWT containing the authenticated user's info in the `User` format. See [User data format](/deploy/personalization-setup#user-data-format) for more information.
        * Sign the JWT with your secret key, using the EdDSA algorithm.
        * Create a redirect URL back to the `/login/jwt-callback` path of your docs, including the JWT as the hash.
      </Step>
    </Steps>

    ### Example

    Your documentation is hosted at `docs.foo.com` with an existing authentication system at `foo.com`. You want to extend your login flow to grant access to the docs while keeping your docs separate from your dashboard (or you don't have a dashboard).

    Create a login endpoint at `https://foo.com/docs-login` that extends your existing authentication.

    After verifying user credentials:

    * Generate a JWT with user data in Mintlify's format.
    * Sign the JWT and redirect to `https://docs.foo.com/login/jwt-callback#{SIGNED_JWT}`.

    <CodeGroup>
      ```ts TypeScript theme={null}
      import * as jose from 'jose';
      import { Request, Response } from 'express';

      const TWO_WEEKS_IN_MS = 1000 * 60 * 60 * 24 * 7 * 2;

      const signingKey = await jose.importPKCS8(process.env.MINTLIFY_PRIVATE_KEY, 'EdDSA');

      export async function handleRequest(req: Request, res: Response) {
        const user = {
          expiresAt: Math.floor((Date.now() + TWO_WEEKS_IN_MS) / 1000), // 2 week session expiration
          groups: res.locals.user.groups,
          content: {
            firstName: res.locals.user.firstName,
            lastName: res.locals.user.lastName,
          },
        };

        const jwt = await new jose.SignJWT(user)
          .setProtectedHeader({ alg: 'EdDSA' })
          .setExpirationTime('10 s') // 10 second JWT expiration
          .sign(signingKey);

        return res.redirect(`https://docs.foo.com/login/jwt-callback#${jwt}`);
      }
      ```

      ```python Python theme={null}
      import jwt # pyjwt
      import os

      from datetime import datetime, timedelta
      from fastapi.responses import RedirectResponse

      private_key = os.getenv(MINTLIFY_JWT_PEM_SECRET_NAME, '')

      @router.get('/auth')
      async def return_mintlify_auth_status(current_user):
        jwt_token = jwt.encode(
          payload={
            'exp': int((datetime.now() + timedelta(seconds=10)).timestamp()),    # 10 second JWT expiration
            'expiresAt': int((datetime.now() + timedelta(weeks=2)).timestamp()), # 1 week session expiration
            'groups': ['admin'] if current_user.is_admin else [],
            'content': {
              'firstName': current_user.first_name,
              'lastName': current_user.last_name,
            },
          },
          key=private_key,
          algorithm='EdDSA'
        )

        return RedirectResponse(url=f'https://docs.foo.com/login/jwt-callback#{jwt_token}', status_code=302)
      ```
    </CodeGroup>

    ### Redirecting unauthenticated users

    When an unauthenticated user tries to access a protected page, their intended destination is preserved in the redirect to your login URL:

    1. User attempts to visit a protected page: `https://docs.foo.com/quickstart`.
    2. Redirect to your login URL with a redirect query parameter: `https://foo.com/docs-login?redirect=%2Fquickstart`.
    3. After authentication, redirect to `https://docs.foo.com/login/jwt-callback?redirect=%2Fquickstart#{SIGNED_JWT}`.
    4. User lands in their original destination.
  </Tab>
</Tabs>


## Making pages public

When using partial authentication, all pages are protected by default. You can make specific pages viewable without authentication at the page or group level with the `public` property.

### Page level

To make a page public, add `public: true` to the page's frontmatter.

```mdx Public page example theme={null}
---
title: "Public page"
public: true
---
```

### Group level

To make all pages in a group public, add `"public": true` beneath the group's name in the `navigation` object of your `docs.json`.

```json Public group example theme={null}
{
  "navigation": {
    "groups": [
      {
        "group": "Public group",
        "public": true,
        "icon": "play",
        "pages": [
          "quickstart",
          "installation",
          "settings"
        ]
      },
      {
        "group": "Private group",
        "icon": "pause",
        "pages": [
          "private-information",
          "secret-settings"
        ]
      }
    ]
  }
}
```



# CI checks
Source: https://mintlify.com/docs/deploy/ci

Add checks for broken links, linting, and grammar to the updating process

<Info>
  [Pro and Enterprise plans](https://mintlify.com/pricing?ref=docs-ci) include CI checks for GitHub repositories.
</Info>

Use CI checks to lint your docs for errors and provide warnings before you deploy. Mintlify CI checks run on pull requests against a configured deployment branch.


## Installation

To begin, follow the steps on the [GitHub](/deploy/github) page.

<Tip>
  Only access to the repository where your documentation content exists is required, so it is highly recommended to only grant access to that repository.
</Tip>


## Configuration

Configure the CI checks enabled for a deployment by navigating to the [Add-ons](https://dashboard.mintlify.com/products/addons) page of your dashboard. Enable the checks that you want to run.

When enabling checks, you can choose to run them at a `Warning` or `Blocking` level.

* A `Warning` level check will never provide a failure status, even if there is an error or suggestions.
* A `Blocking` level check will provide a failure status if there is an error or suggestions.


## Available CI checks

### Broken links

Similar to how the [CLI link checker](/create/broken-links#broken-links) works on your local machine, the
broken link CI check automatically searches your documentation content for broken internal links.

To see the results of this check, visit GitHub's check results page for a specific commit.

### Vale

[Vale](https://vale.sh/) is an open source rule-based prose linter which supports a range of document types, including Markdown and MDX.

Mintlify supports automatically running Vale in a CI check and displaying the results as a check status.

#### Configuration

If you have a `.vale.ini` file in the root content directory for your deployment, the Vale CI check uses that configuration file and any configuration files in your specified `stylesPath`.

If you don't have a Vale config file, the default configuration automatically loads.

```mdx Default vale.ini configuration expandable theme={null}

# Top level styles
StylesPath = /app/styles
MinAlertLevel = suggestion
IgnoredScopes = code, tt, img, url, a
SkippedScopes = script, style, pre, figure, code


# Vocabularies
Vocab = Mintlify


# This is required since Vale doesn't officially support MDX
[formats]
mdx = md


# MDX support
[*.mdx]
BasedOnStyles = Vale
Vale.Terms = NO # Enforces really harsh capitalization rules, keep off


# `import ...`, `export ...`

# `<Component ... />`

# `<Component>...</Component>`

# `{ ... }`
TokenIgnores = (?sm)((?:import|export) .+?$), \
(?<!`)(<\w+ ?.+ ?\/>)(?!`), \
(<[A-Z]\w+>.+?<\/[A-Z]\w+>)


# Exclude:

# `<Component \n ... />`
BlockIgnores = (?sm)^(<\w+\n .*\s\/>)$, \
(?sm)^({.+.*})

CommentDelimiters = {/*, */}
```

```text Default Vale vocabulary expandable theme={null}
Mintlify
mintlify
VSCode
openapi
OpenAPI
Github
APIs

repo
npm
dev

Lorem
ipsum
impsum
amet

const
myName
myObject
bearerAuth
favicon
topbar
url
borderRadius
args
modeToggle
ModeToggle
isHidden
autoplay

_italic_
Strikethrough
Blockquotes
Blockquote
Singleline
Multiline

onboarding

async
await
boolean
enum
func
impl
init
instanceof
typeof
params
stdin
stdout
stderr
stdout
stdin
var
const
let
null
undefined
struct
bool

cors
csrf
env
xhr
xhr2
jwt
oauth
websocket
localhost
middleware
runtime
webhook
stdin
stdout

json
yaml
yml
md
txt
tsx
jsx
css
scss
html
png
jpg
svg

cdn
cli
css
dom
dto
env
git
gui
http
https
ide
jvm
mvc
orm
rpc
sdk
sql
ssh
ssl
tcp
tls
uri
url
ux
ui

nodejs
npm
yarn
pnpm
eslint
pytest
golang
rustc
kubectl
mongo
postgres
redis

JavaScript
TypeScript
Python
Ruby
Rust
Go
Golang
Java
Kotlin
Swift
Node.js
NodeJS
Deno

React
Vue
Angular
Next.js
Nuxt
Express
Django
Flask
Spring
Laravel
Redux
Vuex
TensorFlow
PostgreSQL
MongoDB
Redis
PNPM

Docker
Kubernetes
AWS
Azure
GCP
Terraform
Jenkins
CircleCI
GitLab
Heroku

Git
git
GitHub
GitLab
Bitbucket
VSCode
Visual Studio Code
IntelliJ
WebStorm
ESLint
eslint
Prettier
prettier
Webpack
webpack
Vite
vite
Babel
babel
Jest
jest
Mocha
Cypress
Postman

HTTP
HTTPS
OAuth
JWT
GraphQL
REST
WebSocket
TCP/IP

NPM
Yarn
PNPM
Pip
PIP
Cargo
RubyGems

Swagger
OpenAPI
Markdown
MDX
Storybook
TypeDoc
JSDoc

MySQL
PostgreSQL
MongoDB
Redis
Elasticsearch
DynamoDB

Linux
Unix
macOS
iOS

Firefox
Chromium
WebKit

config
ctx
desc
dir
elem
err
len
msg
num
obj
prev
proc
ptr
req
res
str
tmp
val
vars

todo
href
lang
nav
prev
next
toc
```

```text Example Vale file structure theme={null}
  - docs.json
  - .vale.ini
  - styles/...
  - text.md
```

```text Example monorepo Vale file structure theme={null}
  - main.ts
  - docs/
    - docs.json
    - .vale.ini
    - styles/...
    - text.md
  - test/
```

<Note>
  Please note that for security reasons, absolute `stylesPath`, or `stylesPath` which include `..` values aren't supported. Please use relative paths and include the `stylesPath` in your repository.
</Note>

#### Packages

Vale supports a range of [packages](https://vale.sh/docs/keys/packages), which can be used to check for spelling and style errors.
Any packages you include in your repository under the correct `stylesPath` are automatically installed and used in your Vale configuration.

For packages not included in your repository, you may specify any packages from the [Vale package registry](https://vale.sh/explorer), and they're automatically downloaded and used in your Vale configuration.

<Note>
  Please note that for security reasons, automatically downloading packages that aren't from the [Vale package registry](https://vale.sh/explorer) is not supported.
</Note>

#### Vale with `MDX`

Vale doesn't natively support `MDX`, but Vale's author has provided a [custom extension](https://github.com/errata-ai/MDX) to support it.

If you prefer not to use this extension, the following lines can be added to the configured `.vale.ini` file:

```ini  theme={null}
[formats]
mdx = md

[*.mdx]
CommentDelimiters = {/*, */}

TokenIgnores = (?sm)((?:import|export) .+?$), \
(?<!`)(<\w+ ?.+ ?\/>)(?!`), \
(<[A-Z]\w+>.+?<\/[A-Z]\w+>)

BlockIgnores = (?sm)^(<\w+\n .*\s\/>)$, \
(?sm)^({.+.*})
```

To use Vale's in-document comments, use MDX-style comments `{/* ... */}`. If you use the `CommentDelimiters = {/*, */}` [setting](https://vale.sh/docs/keys/commentdelimiters) in your configuration, Vale automatically interprets these comments while linting. This means you can easily use Vale's built-in features, like skipping lines or sections.

```mdx  theme={null}
{/* vale off */}

This text is ignored by Vale

{/* vale on */}
```

If you choose not to use `CommentDelimiters` but still choose to use Vale's comments, you must wrap any Vale comments in MDX comments `{/* ... */}`. For example:

```mdx  theme={null}
{/* <!-- vale off --> */}

This text is ignored by Vale

{/* <!-- vale on --> */}
```

These comment tags aren't supported within Mintlify components but will function correctly anywhere at the base level of a document.



# Cloudflare
Source: https://mintlify.com/docs/deploy/cloudflare

Host documentation at a custom subpath using Cloudflare Workers

To host your documentation at a custom subpath such as `yoursite.com/docs` using Cloudflare, you will need to create and configure a Cloudflare Worker.

<Info>
  Before you begin, you need a Cloudflare account and a domain name (can be managed on or off Cloudflare).
</Info>


## Repository structure

Your documentation files must be organized within your repository to match your chosen subpath structure. For example, if you want your documentation at `yoursite.com/docs`, you would create a `docs/` directory with all of your documentation files.


## Set up a Cloudflare Worker

Create a Cloudflare Worker by following the [Cloudflare Workers getting started guide](https://developers.cloudflare.com/workers/get-started/dashboard/), if you have not already.

<Tip>
  If your DNS provider is Cloudflare, disable proxying for the CNAME record to avoid potential configuration issues.
</Tip>

### Proxies with Vercel deployments

If you use Cloudflare as a proxy with Vercel deployments, you must ensure proper configuration to avoid conflicts with Vercel's domain verification and SSL certificate provisioning.

Improper proxy configuration can prevent Vercel from provisioning Let's Encrypt SSL certificates and cause domain verification failures.

#### Required path allowlist

Your Cloudflare Worker must allow traffic to these specific paths without blocking or redirecting:

* `/.well-known/acme-challenge/*` - Required for Let's Encrypt certificate verification
* `/.well-known/vercel/*` - Required for Vercel domain verification

While Cloudflare automatically handles many verification rules, creating additional custom rules may inadvertently block this critical traffic.

#### Header forwarding requirements

Ensure that the `HOST` header is correctly forwarded in your Worker configuration. Failure to properly forward headers will cause verification requests to fail.

### Configure routing

In your Cloudflare dashboard, select **Edit Code** and add the following script into your Worker's code. See the [Cloudflare documentation](https://developers.cloudflare.com/workers-ai/get-started/dashboard/#development) for more information on editing a Worker.

<Tip>
  Replace `[SUBDOMAIN]` with your unique subdomain, `[YOUR_DOMAIN]` with your website's base URL, and `/docs` with your desired subpath if different.
</Tip>

```javascript  theme={null}
addEventListener("fetch", (event) => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  try {
    const urlObject = new URL(request.url);
    
    // If the request is to a Vercel verification path, allow it to pass through
    if (urlObject.pathname.startsWith('/.well-known/')) {
      return await fetch(request);
    }
    
    // If the request is to the docs subdirectory
    if (/^\/docs/.test(urlObject.pathname)) {
      // Then Proxy to Mintlify
      const DOCS_URL = "[SUBDOMAIN].mintlify.dev";
      const CUSTOM_URL = "[YOUR_DOMAIN]";

      let url = new URL(request.url);
      url.hostname = DOCS_URL;

      let proxyRequest = new Request(url, request);

      proxyRequest.headers.set("Host", DOCS_URL);
      proxyRequest.headers.set("X-Forwarded-Host", CUSTOM_URL);
      proxyRequest.headers.set("X-Forwarded-Proto", "https");
      // If deploying to Vercel, preserve client IP
      proxyRequest.headers.set("CF-Connecting-IP", request.headers.get("CF-Connecting-IP"));

      return await fetch(proxyRequest);
    }
  } catch (error) {
    // If no action found, play the regular request
    return await fetch(request);
  }
}
```

Select **Deploy** and wait for the changes to propagate.

<Note>
  After configuring your DNS, custom subdomains are usually available within a few minutes. DNS propagation can sometimes take 1-4 hours, and in rare cases up to 48 hours. If your subdomain is not immediately available, please wait before troubleshooting.
</Note>

### Test your Worker

After your code deploys, test your Worker to ensure it routes to your Mintlify docs.

1. Test using the Worker's preview URL: `your-worker.your-subdomain.workers.dev/docs`
2. Verify the Worker routes to your Mintlify docs and your website.

### Add custom domain

1. In your [Cloudflare dashboard](https://dash.cloudflare.com/), navigate to your Worker.
2. Go to **Settings > Domains & Routes > Add > Custom Domain**.
3. Add your domain.

<Tip>
  We recommend you add your domain both with and without `www.` prepended.
</Tip>

See [Add a custom domain](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/#add-a-custom-domain) in the Cloudflare documentation for more information.

### Resolve DNS conflicts

If your domain already points to another service, you must remove the existing DNS record. Your Cloudflare Worker must be configured to control all traffic for your domain.

1. Delete the existing DNS record for your domain. See [Delete DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records) in the Cloudflare documentation for more information.
2. Return to your Worker and add your custom domain.


## Webflow custom routing

If you use Webflow to host your main site and want to serve Mintlify docs at `/docs` on the same domain, you'll need to configure custom routing through Cloudflare Workers to proxy all non-docs traffic to your main site.

<Warning>
  Make sure your main site is set up on a landing page before deploying this Worker, or visitors to your main site will see errors.
</Warning>

1. In Webflow, set up a landing page for your main site like `landing.yoursite.com`. This will be the page that visitors see when they visit your site.
2. Deploy your main site to the landing page. This ensures that your main site remains accessible while you configure the Worker.
3. To avoid conflicts, update any absolute URLs in your main site to be relative.
4. In Cloudflare, select **Edit Code** and add the following script into your Worker's code.

<Tip> Replace `[SUBDOMAIN]` with your unique subdomain, `[YOUR_DOMAIN]` with your website's base URL, `[LANDING_DOMAIN]` with your landing page URL, and `/docs` with your desired subpath if different. </Tip>

```javascript  theme={null}
addEventListener("fetch", (event) => {
event.respondWith(handleRequest(event.request));
});
async function handleRequest(request) {
try {
  const urlObject = new URL(request.url);
  
  // If the request is to a Vercel verification path, allow it to pass through
  if (urlObject.pathname.startsWith('/.well-known/')) {
    return await fetch(request);
  }
  
  // If the request is to the docs subdirectory
  if (/^\/docs/.test(urlObject.pathname)) {
    // Proxy to Mintlify
    const DOCS_URL = "[SUBDOMAIN].mintlify.dev";
    const CUSTOM_URL = "[YOUR_DOMAIN]";
    let url = new URL(request.url);
    url.hostname = DOCS_URL;
    let proxyRequest = new Request(url, request);
    proxyRequest.headers.set("Host", DOCS_URL);
    proxyRequest.headers.set("X-Forwarded-Host", CUSTOM_URL);
    proxyRequest.headers.set("X-Forwarded-Proto", "https");
    // If deploying to Vercel, preserve client IP
    proxyRequest.headers.set("CF-Connecting-IP", request.headers.get("CF-Connecting-IP"));
    return await fetch(proxyRequest);
  }
  // Route everything else to main site
  const MAIN_SITE_URL = "[LANDING_DOMAIN]";
  if (MAIN_SITE_URL && MAIN_SITE_URL !== "[LANDING_DOMAIN]") {
    let mainSiteUrl = new URL(request.url);
    mainSiteUrl.hostname = MAIN_SITE_URL;
    return await fetch(mainSiteUrl, {
      method: request.method,
      headers: request.headers,
      body: request.body
    });
  }
} catch (error) {
  // If no action found, serve the regular request
  return await fetch(request);
}
}
```

5. Select **Deploy** and wait for the changes to propagate.

<Note>
  After configuring your DNS, custom subdomains are usually available within a few minutes. DNS propagation can sometimes take 1-4 hours, and in rare cases up to 48 hours. If your subdomain is not immediately available, please wait before troubleshooting.
</Note>



# Content Security Policy (CSP) configuration
Source: https://mintlify.com/docs/deploy/csp-configuration

Domain whitelist and header configurations for reverse proxies, firewalls, and networks that enforce strict security policies

Content Security Policy (CSP) is a security standard that helps prevent cross-site scripting (XSS) attacks by controlling which resources a web page can load. Mintlify serves a default CSP that protects most sites. If you host your documentation behind a reverse proxy or firewall, that overwrites the default CSP, you may need to configure CSP headers for features to function properly.


## CSP directives

The following CSP directives are used to control which resources can be loaded:

* `script-src`: Controls which scripts can be executed
* `style-src`: Controls which stylesheets can be loaded
* `font-src`: Controls which fonts can be loaded
* `img-src`: Controls which images, icons, and logos can be loaded
* `connect-src`: Controls which URLs can be connected to for API calls and WebSocket connections
* `frame-src`: Controls which URLs can be embedded in frames or iframes
* `default-src`: Fallback for other directives when not explicitly set


## Domain whitelist

| Domain                          | Purpose                        | CSP directive               | Required |
| :------------------------------ | :----------------------------- | :-------------------------- | :------- |
| `d4tuoctqmanu0.cloudfront.net`  | KaTeX CSS, fonts               | `style-src`, `font-src`     | Required |
| `*.mintlify.dev`                | Documentation content          | `connect-src`, `frame-src`  | Required |
| `*.mintlify.com`                | Dashboard, API, insights proxy | `connect-src`               | Required |
| `leaves.mintlify.com`           | Assistant API                  | `connect-src`               | Required |
| `d3gk2c5xim1je2.cloudfront.net` | Icons, images, logos           | `img-src`                   | Required |
| `d1ctpt7j8wusba.cloudfront.net` | Mint version and release files | `connect-src`               | Required |
| `mintcdn.com`                   | Images, favicons               | `img-src`, `connect-src`    | Required |
| `*.mintcdn.com`                 | Images, favicons               | `img-src`, `connect-src`    | Required |
| `api.mintlifytrieve.com`        | Search API                     | `connect-src`               | Required |
| `cdn.jsdelivr.net`              | Emoji assets for OG images     | `script-src`, `img-src`     | Required |
| `fonts.googleapis.com`          | Google Fonts                   | `style-src`, `font-src`     | Optional |
| `www.googletagmanager.com`      | Google Analytics/GTM           | `script-src`, `connect-src` | Optional |
| `cdn.segment.com`               | Segment analytics              | `script-src`, `connect-src` | Optional |
| `plausible.io`                  | Plausible analytics            | `script-src`, `connect-src` | Optional |
| `us.posthog.com`                | PostHog analytics              | `connect-src`               | Optional |
| `tag.clearbitscripts.com`       | Clearbit tracking              | `script-src`                | Optional |
| `cdn.heapanalytics.com`         | Heap analytics                 | `script-src`                | Optional |
| `chat.cdn-plain.com`            | Plain chat widget              | `script-src`                | Optional |
| `chat-assets.frontapp.com`      | Front chat widget              | `script-src`                | Optional |
| `browser.sentry-cdn.com`        | Sentry error tracking          | `script-src`, `connect-src` | Optional |
| `js.sentry-cdn.com`             | Sentry JavaScript SDK          | `script-src`                | Optional |


## Example CSP configuration

<Note>
  Only include domains for services that you use. Remove any analytics domains that you have not configured for your documentation.
</Note>

```text wrap theme={null}
Content-Security-Policy:
default-src 'self';
script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net www.googletagmanager.com cdn.segment.com plausible.io
us.posthog.com tag.clearbitscripts.com cdn.heapanalytics.com chat.cdn-plain.com chat-assets.frontapp.com
browser.sentry-cdn.com js.sentry-cdn.com;
style-src 'self' 'unsafe-inline' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com;
font-src 'self' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com;
img-src 'self' data: blob: d3gk2c5xim1je2.cloudfront.net mintcdn.com *.mintcdn.com cdn.jsdelivr.net;
connect-src 'self' *.mintlify.dev *.mintlify.com d1ctpt7j8wusba.cloudfront.net mintcdn.com *.mintcdn.com
api.mintlifytrieve.com www.googletagmanager.com cdn.segment.com plausible.io us.posthog.com browser.sentry-cdn.com;
frame-src 'self' *.mintlify.dev;
```


## Common configurations by proxy type

Most reverse proxies support adding custom headers.

### Cloudflare configuration

Create a Response Header Transform Rule:

1. In your Cloudflare dashboard, go to **Rules > Overview**.
2. Select **Create rule > Response Header Transform Rule**.
3. Configure the rule:

* **Modify response header**: Set static
* **Header name**: `Content-Security-Policy`
* **Header value**:
  ```text wrap theme={null}
  default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com; font-src 'self' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com; img-src 'self' data: blob: d3gk2c5xim1je2.cloudfront.net mintcdn.com *.mintcdn.com cdn.jsdelivr.net; connect-src 'self' *.mintlify.dev *.mintlify.com d1ctpt7j8wusba.cloudfront.net mintcdn.com *.mintcdn.com api.mintlifytrieve.com; frame-src 'self' *.mintlify.dev;
  ```

4. Deploy your rule.

### AWS CloudFront configuration

Add a response headers policy in CloudFront:

```json  theme={null}
{
"ResponseHeadersPolicy": {
    "Name": "MintlifyCSP",
    "Config": {
    "SecurityHeadersConfig": {
        "ContentSecurityPolicy": {
        "ContentSecurityPolicy": "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com; font-src 'self' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com; img-src 'self' data: blob: d3gk2c5xim1je2.cloudfront.net mintcdn.com *.mintcdn.com cdn.jsdelivr.net; connect-src 'self' *.mintlify.dev *.mintlify.com d1ctpt7j8wusba.cloudfront.net mintcdn.com *.mintcdn.com api.mintlifytrieve.com; frame-src 'self' *.mintlify.dev;",
        "Override": true
        }
      }
    }
  }
}
```

### Vercel configuration

Add to your `vercel.json`:

```json  theme={null}
{
"headers": [
    {
    "source": "/(.*)",
    "headers": [
        {
        "key": "Content-Security-Policy",
        "value": "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com; font-src 'self' d4tuoctqmanu0.cloudfront.net fonts.googleapis.com; img-src 'self' data: blob: d3gk2c5xim1je2.cloudfront.net mintcdn.com *.mintcdn.com cdn.jsdelivr.net; connect-src 'self' *.mintlify.dev *.mintlify.com d1ctpt7j8wusba.cloudfront.net mintcdn.com *.mintcdn.com api.mintlifytrieve.com; frame-src 'self' *.mintlify.dev;"
        }
      ]
    }
  ]
}
```


## Troubleshooting

Identify CSP violations in your browser console:

1. Open your browser's Developer Tools.
2. Go to the **Console** tab.
3. Look for errors starting with:
   * `Content Security Policy: The page's settings blocked the loading of a resource`
   * `Refused to load the script/stylesheet because it violates the following Content Security Policy directive`
   * `Refused to connect to because it violates the following Content Security Policy directive`



# Deployments
Source: https://mintlify.com/docs/deploy/deployments

Troubleshoot your deployments

Your documentation site automatically deploys when you push changes to your connected repository. This requires the Mintlify GitHub app to be properly installed and connected.

If your latest changes are not appearing on your live site, first check that the GitHub app is installed on the account or organization that owns your docs repository. See [GitHub troubleshooting](/deploy/github#troubleshooting) for more information.

If the GitHub app is connected, but changes are still not deploying, you can manually trigger a rebuild from your dashboard.


## Manually triggering a deployment

<Steps>
  <Step title="Verify your latest commit was successful.">
    Check that your latest commit appears in your docs repository and did not encounter any errors.
  </Step>

  <Step title="Manually trigger a deployment.">
    Go to your [dashboard](https://dashboard.mintlify.com) and select the deploy button.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=23715eadbebd74b3bfa5b5c197479e51" alt="The manual update button emphasized with an orange rectangle." className="block dark:hidden" data-og-width="1354" width="1354" data-og-height="192" height="192" data-path="images/deployments/manual-update-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a07e04ba4929e511f17aa6f68a437c17 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=68025b15f00c2ff85952800ee93cec77 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=bf4bb3a51ab09c117f69ee8c94199ff9 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=5d95d206d3fc26989433326aa4dd9f25 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=691130c9e7ff6508de9d02730930ba0d 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-light.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=84fa9f1a584e54a9961b9cf6849d4f49 2500w" />

      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0e7abcfbc9fdadbcf12a781a45d6a938" alt="The manual update button emphasized with an orange rectangle." className="hidden dark:block" data-og-width="1354" width="1354" data-og-height="192" height="192" data-path="images/deployments/manual-update-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=409ba006e2b58becda7f4b270ad40f55 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9662f8b68920ebda5a76db18efbb99d7 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9224bebc75c5a53c947a72c250b4429c 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4fa3b57bafc403d471c675dda4486ae2 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0cfcab0c682481b8df4d293417c8466b 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/deployments/manual-update-dark.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=23f6e97550e66bc49fc4284c96d73837 2500w" />
    </Frame>
  </Step>
</Steps>



# GitHub
Source: https://mintlify.com/docs/deploy/github

Sync your docs with a GitHub repo

Mintlify uses a GitHub App to automatically sync your documentation with your GitHub repository.


## Installing the GitHub App

<Note>
  You must have organization ownership or administrator permissions in a repository to install the app. If you lack the necessary permissions, the repository owner must approve the installation request.
</Note>

Install the Mintlify GitHub App through your [dashboard](https://dashboard.mintlify.com/settings/organization/github-app).

<Tip>
  We recommend granting access only to the repository where your docs are hosted.
</Tip>

<Frame>
  <img className="h-80" alt="Mintlify GitHub App installation page with the 'Only select repositories' option selected." src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=35cc7fc3564471ccef7a54029ef18cd4" data-og-width="2980" width="2980" data-og-height="1702" height="1702" data-path="images/github/select-repos.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2bc537826e2a4b843f5550650a488b61 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1ee9087af342383e3e3600b3a21e5e26 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3b36b83d3d85a31b64cedb0886a79ab3 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4b05fcc79d53b9401c2bbe937ff5667f 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=799d62da575693367a5fa9c787064968 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cab163dcf7b60ff032f7c7ae09a712de 2500w" />
</Frame>


## Permissions

When you install the GitHub app, you will be prompted to grant the following permissions:

Read permissions:

* `metadata`: Basic repository information

Read and write permissions:

* `checks`: Create status checks on pull requests
* `code`: Read file changes when you commit to your docs branch
* `deployments`: Generate preview deployments for pull requests
* `pull requests`: Create branches and pull requests from the web editor

<Info>
  The app only accesses repositories that you explicitly grant it access to. If you have branch protection rules enabled, the app can't push directly to protected branches.
</Info>


## Managing repository access

When installing our GitHub App, you can grant access to all of your repositories or specific ones. We recommend only granting access to the repositories where your documentation is located. You can modify this selection anytime in your [GitHub app settings](https://github.com/apps/mintlify/installations/new).


## Configuring docs source

Change the organization, repository, or branch that your documentation is built from in the [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) section of your dashboard.


## Troubleshooting

### GitHub app connection issues

If you encounter problems with the GitHub app, resetting the connection can solve most problems.

<Steps>
  <Step title="Uninstall the Mintlify app through GitHub.">
    1. In GitHub, go to [installations](https://github.com/settings/installations) and select **Configure** next to the Mintlify app. Scroll down and select **Uninstall**.
    2. Go to [Authorized GitHub Apps](https://github.com/settings/apps/authorizations) and select **Revoke** next to the Mintlify app.
  </Step>

  <Step title="Reinstall the Mintlify app.">
    1. In your Mintlify dashboard, go to [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) and install the GitHub app.
    2. Authorize your account in the [My Profile](https://dashboard.mintlify.com/settings/account) section of your dashboard.
  </Step>
</Steps>

### Feedback add-ons are unavailable

If you cannot enable the edit suggestions or raise issues options in your dashboard and your repository is public, revalidate your Git settings.

<Steps>
  <Step title="Navigate to Git Settings">
    Go to [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) in your dashboard.
  </Step>

  <Step title="Revalidate your settings">
    Click the green check mark in the corner of the Git settings box to revalidate your repository settings. This will force update your repository settings to reflect whether your repository is public or private.

    <Frame>
      <img src="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=b3c7c421876bb4a2921ece22fc4b4777" alt="The Git Settings page in the Mintlify dashboard. An orange arrow points to the green check mark that revalidates the repository settings." className="block dark:hidden" data-og-width="1996" width="1996" data-og-height="1168" height="1168" data-path="images/github/revalidate-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=280&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=5788d2b87586e6ae6b96b25a27c6d00f 280w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=560&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=e872c3b592d441835267a344b0024a17 560w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=840&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=cd4b7c7445b9b080a00687d341f4819c 840w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=1100&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=0707fcbc7f54ce1f4655ea14de94b001 1100w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=1650&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=e08810b8c1987134bb191385722f77e4 1650w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=2500&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=12ba6216beb5594c78bfafa9fb8c36d2 2500w" />

      <img src="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=9d2462cd3e07c9e7cf0835b3c50e3020" alt="The Git Settings page in the Mintlify dashboard. An orange arrow points to the green check mark that revalidates the repository settings." className="hidden dark:block" data-og-width="1998" width="1998" data-og-height="1170" height="1170" data-path="images/github/revalidate-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=280&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=7d5e0e13ef18a79ad21177dca48c0516 280w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=560&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=a23c2cb529ab4a6764aa21a65dd1bc42 560w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=840&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=d9ee92ccb7afbfea87ab21d47235da92 840w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=1100&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=39fd714f39b4583a1f7c5dc8c5922765 1100w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=1650&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=4bc8a85bfc148c6864423611db134c29 1650w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=2500&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=2b00909bd2105e7ebbf59381c7bb9156 2500w" />
    </Frame>
  </Step>
</Steps>



---
**Navigation:** [← Previous](./03-mermaid.md) | [Index](./index.md) | [Next →](./05-gitlab.md)
