**Navigation:** [← Previous](./08-routejs.md) | [Index](./index.md) | [Next →](./10-usesearchparams.md)

---

# generateMetadata

You can use the `metadata` object or the `generateMetadata` function to define metadata.

## The `metadata` object

To define static metadata, export a [`Metadata` object](#metadata-fields) from a `layout.js` or `page.js` file.

```tsx filename="layout.tsx | page.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: '...',
  description: '...',
}

export default function Page() {}
```

```jsx filename="layout.js | page.js" switcher
export const metadata = {
  title: '...',
  description: '...',
}

export default function Page() {}
```

> See the [Metadata Fields](#metadata-fields) for a complete list of supported options.

## `generateMetadata` function

Dynamic metadata depends on **dynamic information**, such as the current route parameters, external data, or `metadata` in parent segments, can be set by exporting a `generateMetadata` function that returns a [`Metadata` object](#metadata-fields).

Resolving `generateMetadata` is part of rendering the page. If the page can be pre-rendered and `generateMetadata` doesn't introduce dynamic behavior, the resulting metadata is included in the page’s initial HTML.

Otherwise the metadata resolved from `generateMetadata` [can be streamed](/docs/app/api-reference/functions/generate-metadata.md#streaming-metadata) after sending the initial UI.

```tsx filename="app/products/[id]/page.tsx" switcher
import type { Metadata, ResolvingMetadata } from 'next'

type Props = {
  params: Promise<{ id: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  // read route params
  const { id } = await params

  // fetch data
  const product = await fetch(`https://.../${id}`).then((res) => res.json())

  // optionally access and extend (rather than replace) parent metadata
  const previousImages = (await parent).openGraph?.images || []

  return {
    title: product.title,
    openGraph: {
      images: ['/some-specific-page-image.jpg', ...previousImages],
    },
  }
}

export default function Page({ params, searchParams }: Props) {}
```

```jsx filename="app/products/[id]/page.js" switcher
export async function generateMetadata({ params, searchParams }, parent) {
  // read route params
  const { id } = await params

  // fetch data
  const product = await fetch(`https://.../${id}`).then((res) => res.json())

  // optionally access and extend (rather than replace) parent metadata
  const previousImages = (await parent).openGraph?.images || []

  return {
    title: product.title,
    openGraph: {
      images: ['/some-specific-page-image.jpg', ...previousImages],
    },
  }
}

export default function Page({ params, searchParams }) {}
```

For type completion of `params` and `searchParams`, you can type the first argument with [`PageProps<'/route'>`](/docs/app/api-reference/file-conventions/page.md#page-props-helper) or [`LayoutProps<'/route'>`](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper) for pages and layouts respectively.

> **Good to know**:
>
> * Metadata can be added to `layout.js` and `page.js` files.
> * Next.js will automatically resolve the metadata, and create the relevant `<head>` tags for the page.
> * The `metadata` object and `generateMetadata` function exports are **only supported in Server Components**.
> * You cannot export both the `metadata` object and `generateMetadata` function from the same route segment.
> * `fetch` requests inside `generateMetadata` are automatically [memoized](/docs/app/guides/caching.md#request-memoization) for the same data across `generateMetadata`, `generateStaticParams`, Layouts, Pages, and Server Components.
> * React [`cache` can be used](/docs/app/guides/caching.md#react-cache-function) if `fetch` is unavailable.
> * [File-based metadata](/docs/app/api-reference/file-conventions/metadata.md) has the higher priority and will override the `metadata` object and `generateMetadata` function.

## Reference

### Parameters

`generateMetadata` function accepts the following parameters:

* `props` - An object containing the parameters of the current route:
  * `params` - An object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) object from the root segment down to the segment `generateMetadata` is called from. Examples:

    | Route                           | URL         | `params`                  |
    | ------------------------------- | ----------- | ------------------------- |
    | `app/shop/[slug]/page.js`       | `/shop/1`   | `{ slug: '1' }`           |
    | `app/shop/[tag]/[item]/page.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |
    | `app/shop/[...slug]/page.js`    | `/shop/1/2` | `{ slug: ['1', '2'] }`    |

  * `searchParams` - An object containing the current URL's [search params](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters). Examples:

    | URL             | `searchParams`       |
    | --------------- | -------------------- |
    | `/shop?a=1`     | `{ a: '1' }`         |
    | `/shop?a=1&b=2` | `{ a: '1', b: '2' }` |
    | `/shop?a=1&a=2` | `{ a: ['1', '2'] }`  |

* `parent` - A promise of the resolved metadata from parent route segments.

### Returns

`generateMetadata` should return a [`Metadata` object](#metadata-fields) containing one or more metadata fields.

> **Good to know**:
>
> * If metadata doesn't depend on runtime information, it should be defined using the static [`metadata` object](#the-metadata-object) rather than `generateMetadata`.
> * `fetch` requests are automatically [memoized](/docs/app/guides/caching.md#request-memoization) for the same data across `generateMetadata`, `generateStaticParams`, Layouts, Pages, and Server Components. React [`cache` can be used](/docs/app/guides/caching.md#react-cache-function) if `fetch` is unavailable.
> * `searchParams` are only available in `page.js` segments.
> * The [`redirect()`](/docs/app/api-reference/functions/redirect.md) and [`notFound()`](/docs/app/api-reference/functions/not-found.md) Next.js methods can also be used inside `generateMetadata`.

### Metadata Fields

The following fields are supported:

#### `title`

The `title` attribute is used to set the title of the document. It can be defined as a simple [string](#string) or an optional [template object](#template).

##### String

```jsx filename="layout.js | page.js"
export const metadata = {
  title: 'Next.js',
}
```

```html filename="<head> output" hideLineNumbers
<title>Next.js</title>
```

##### `default`

`title.default` can be used to provide a **fallback title** to child route segments that don't define a `title`.

```tsx filename="app/layout.tsx"
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    default: 'Acme',
  },
}
```

```tsx filename="app/about/page.tsx"
import type { Metadata } from 'next'

export const metadata: Metadata = {}

// Output: <title>Acme</title>
```

##### `template`

`title.template` can be used to add a prefix or a suffix to `titles` defined in **child** route segments.

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    template: '%s | Acme',
    default: 'Acme', // a default is required when creating a template
  },
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: {
    template: '%s | Acme',
    default: 'Acme', // a default is required when creating a template
  },
}
```

```tsx filename="app/about/page.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'About',
}

// Output: <title>About | Acme</title>
```

```jsx filename="app/about/page.js" switcher
export const metadata = {
  title: 'About',
}

// Output: <title>About | Acme</title>
```

> **Good to know**:
>
> * `title.template` applies to **child** route segments and **not** the segment it's defined in. This means:
>   * `title.default` is **required** when you add a `title.template`.
>   * `title.template` defined in `layout.js` will not apply to a `title` defined in a `page.js` of the same route segment.
>   * `title.template` defined in `page.js` has no effect because a page is always the terminating segment (it doesn't have any children route segments).
> * `title.template` has **no effect** if a route has not defined a `title` or `title.default`.

##### `absolute`

`title.absolute` can be used to provide a title that **ignores** `title.template` set in parent segments.

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    template: '%s | Acme',
  },
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: {
    template: '%s | Acme',
  },
}
```

```tsx filename="app/about/page.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    absolute: 'About',
  },
}

// Output: <title>About</title>
```

```jsx filename="app/about/page.js" switcher
export const metadata = {
  title: {
    absolute: 'About',
  },
}

// Output: <title>About</title>
```

> **Good to know**:
>
> * `layout.js`
>   * `title` (string) and `title.default` define the default title for child segments (that do not define their own `title`). It will augment `title.template` from the closest parent segment if it exists.
>   * `title.absolute` defines the default title for child segments. It ignores `title.template` from parent segments.
>   * `title.template` defines a new title template for child segments.
> * `page.js`
>   * If a page does not define its own title the closest parents resolved title will be used.
>   * `title` (string) defines the routes title. It will augment `title.template` from the closest parent segment if it exists.
>   * `title.absolute` defines the route title. It ignores `title.template` from parent segments.
>   * `title.template` has no effect in `page.js` because a page is always the terminating segment of a route.

### `description`

```jsx filename="layout.js | page.js"
export const metadata = {
  description: 'The React Framework for the Web',
}
```

```html filename="<head> output" hideLineNumbers
<meta name="description" content="The React Framework for the Web" />
```

### Other fields

```jsx filename="layout.js | page.js"
export const metadata = {
  generator: 'Next.js',
  applicationName: 'Next.js',
  referrer: 'origin-when-cross-origin',
  keywords: ['Next.js', 'React', 'JavaScript'],
  authors: [{ name: 'Seb' }, { name: 'Josh', url: 'https://nextjs.org' }],
  creator: 'Jiachi Liu',
  publisher: 'Sebastian Markbåge',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="application-name" content="Next.js" />
<meta name="author" content="Seb" />
<link rel="author" href="https://nextjs.org" />
<meta name="author" content="Josh" />
<meta name="generator" content="Next.js" />
<meta name="keywords" content="Next.js,React,JavaScript" />
<meta name="referrer" content="origin-when-cross-origin" />
<meta name="color-scheme" content="dark" />
<meta name="creator" content="Jiachi Liu" />
<meta name="publisher" content="Sebastian Markbåge" />
<meta name="format-detection" content="telephone=no, address=no, email=no" />
```

#### `metadataBase`

`metadataBase` is a convenience option to set a base URL prefix for `metadata` fields that require a fully qualified URL.

* `metadataBase` allows URL-based `metadata` fields defined in the **current route segment and below** to use a **relative path** instead of an otherwise required absolute URL.
* The field's relative path will be composed with `metadataBase` to form a fully qualified URL.

```jsx filename="layout.js | page.js"
export const metadata = {
  metadataBase: new URL('https://acme.com'),
  alternates: {
    canonical: '/',
    languages: {
      'en-US': '/en-US',
      'de-DE': '/de-DE',
    },
  },
  openGraph: {
    images: '/og-image.png',
  },
}
```

```html filename="<head> output" hideLineNumbers
<link rel="canonical" href="https://acme.com" />
<link rel="alternate" hreflang="en-US" href="https://acme.com/en-US" />
<link rel="alternate" hreflang="de-DE" href="https://acme.com/de-DE" />
<meta property="og:image" content="https://acme.com/og-image.png" />
```

> **Good to know**:
>
> * `metadataBase` is typically set in root `app/layout.js` to apply to URL-based `metadata` fields across all routes.
> * All URL-based `metadata` fields that require absolute URLs can be configured with a `metadataBase` option.
> * `metadataBase` can contain a subdomain e.g. `https://app.acme.com` or base path e.g. `https://acme.com/start/from/here`
> * If a `metadata` field provides an absolute URL, `metadataBase` will be ignored.
> * Using a relative path in a URL-based `metadata` field without configuring a `metadataBase` will cause a build error.
> * Next.js will normalize duplicate slashes between `metadataBase` (e.g. `https://acme.com/`) and a relative field (e.g. `/path`) to a single slash (e.g. `https://acme.com/path`)

#### URL Composition

URL composition favors developer intent over default directory traversal semantics.

* Trailing slashes between `metadataBase` and `metadata` fields are normalized.
* An "absolute" path in a `metadata` field (that typically would replace the whole URL path) is treated as a "relative" path (starting from the end of `metadataBase`).

For example, given the following `metadataBase`:

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  metadataBase: new URL('https://acme.com'),
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  metadataBase: new URL('https://acme.com'),
}
```

Any `metadata` fields that inherit the above `metadataBase` and set their own value will be resolved as follows:

| `metadata` field                 | Resolved URL                     |
| -------------------------------- | -------------------------------- |
| `/`                              | `https://acme.com`               |
| `./`                             | `https://acme.com`               |
| `payments`                       | `https://acme.com/payments`      |
| `/payments`                      | `https://acme.com/payments`      |
| `./payments`                     | `https://acme.com/payments`      |
| `../payments`                    | `https://acme.com/payments`      |
| `https://beta.acme.com/payments` | `https://beta.acme.com/payments` |

### `openGraph`

```jsx filename="layout.js | page.js"
export const metadata = {
  openGraph: {
    title: 'Next.js',
    description: 'The React Framework for the Web',
    url: 'https://nextjs.org',
    siteName: 'Next.js',
    images: [
      {
        url: 'https://nextjs.org/og.png', // Must be an absolute URL
        width: 800,
        height: 600,
      },
      {
        url: 'https://nextjs.org/og-alt.png', // Must be an absolute URL
        width: 1800,
        height: 1600,
        alt: 'My custom alt',
      },
    ],
    videos: [
      {
        url: 'https://nextjs.org/video.mp4', // Must be an absolute URL
        width: 800,
        height: 600,
      },
    ],
    audio: [
      {
        url: 'https://nextjs.org/audio.mp3', // Must be an absolute URL
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta property="og:title" content="Next.js" />
<meta property="og:description" content="The React Framework for the Web" />
<meta property="og:url" content="https://nextjs.org/" />
<meta property="og:site_name" content="Next.js" />
<meta property="og:locale" content="en_US" />
<meta property="og:image" content="https://nextjs.org/og.png" />
<meta property="og:image:width" content="800" />
<meta property="og:image:height" content="600" />
<meta property="og:image" content="https://nextjs.org/og-alt.png" />
<meta property="og:image:width" content="1800" />
<meta property="og:image:height" content="1600" />
<meta property="og:image:alt" content="My custom alt" />
<meta property="og:video" content="https://nextjs.org/video.mp4" />
<meta property="og:video:width" content="800" />
<meta property="og:video:height" content="600" />
<meta property="og:audio" content="https://nextjs.org/audio.mp3" />
<meta property="og:type" content="website" />
```

```jsx filename="layout.js | page.js"
export const metadata = {
  openGraph: {
    title: 'Next.js',
    description: 'The React Framework for the Web',
    type: 'article',
    publishedTime: '2023-01-01T00:00:00.000Z',
    authors: ['Seb', 'Josh'],
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta property="og:title" content="Next.js" />
<meta property="og:description" content="The React Framework for the Web" />
<meta property="og:type" content="article" />
<meta property="article:published_time" content="2023-01-01T00:00:00.000Z" />
<meta property="article:author" content="Seb" />
<meta property="article:author" content="Josh" />
```

> **Good to know**:
>
> * It may be more convenient to use the [file-based Metadata API](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#image-files-jpg-png-gif) for Open Graph images. Rather than having to sync the config export with actual files, the file-based API will automatically generate the correct metadata for you.

### `robots`

```tsx filename="layout.tsx | page.tsx"
import type { Metadata } from 'next'

export const metadata: Metadata = {
  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: {
      index: true,
      follow: true,
      noimageindex: false,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="robots" content="index, follow" />
<meta
  name="googlebot"
  content="index, follow, max-video-preview:-1, max-image-preview:large, max-snippet:-1"
/>
```

### `icons`

> **Good to know**: We recommend using the [file-based Metadata API](/docs/app/api-reference/file-conventions/metadata/app-icons.md#image-files-ico-jpg-png) for icons where possible. Rather than having to sync the config export with actual files, the file-based API will automatically generate the correct metadata for you.

```jsx filename="layout.js | page.js"
export const metadata = {
  icons: {
    icon: '/icon.png',
    shortcut: '/shortcut-icon.png',
    apple: '/apple-icon.png',
    other: {
      rel: 'apple-touch-icon-precomposed',
      url: '/apple-touch-icon-precomposed.png',
    },
  },
}
```

```html filename="<head> output" hideLineNumbers
<link rel="shortcut icon" href="/shortcut-icon.png" />
<link rel="icon" href="/icon.png" />
<link rel="apple-touch-icon" href="/apple-icon.png" />
<link
  rel="apple-touch-icon-precomposed"
  href="/apple-touch-icon-precomposed.png"
/>
```

```jsx filename="layout.js | page.js"
export const metadata = {
  icons: {
    icon: [
      { url: '/icon.png' },
      new URL('/icon.png', 'https://example.com'),
      { url: '/icon-dark.png', media: '(prefers-color-scheme: dark)' },
    ],
    shortcut: ['/shortcut-icon.png'],
    apple: [
      { url: '/apple-icon.png' },
      { url: '/apple-icon-x3.png', sizes: '180x180', type: 'image/png' },
    ],
    other: [
      {
        rel: 'apple-touch-icon-precomposed',
        url: '/apple-touch-icon-precomposed.png',
      },
    ],
  },
}
```

```html filename="<head> output" hideLineNumbers
<link rel="shortcut icon" href="/shortcut-icon.png" />
<link rel="icon" href="/icon.png" />
<link rel="icon" href="https://example.com/icon.png" />
<link rel="icon" href="/icon-dark.png" media="(prefers-color-scheme: dark)" />
<link rel="apple-touch-icon" href="/apple-icon.png" />
<link
  rel="apple-touch-icon-precomposed"
  href="/apple-touch-icon-precomposed.png"
/>
<link
  rel="apple-touch-icon"
  href="/apple-icon-x3.png"
  sizes="180x180"
  type="image/png"
/>
```

> **Good to know**: The `msapplication-*` meta tags are no longer supported in Chromium builds of Microsoft Edge, and thus no longer needed.

### `themeColor`

> **Deprecated**: The `themeColor` option in `metadata` is deprecated as of Next.js 14. Please use the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport.md) instead.

### `colorScheme`

> **Deprecated**: The `colorScheme` option in `metadata` is deprecated as of Next.js 14. Please use the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport.md) instead.

### `manifest`

A web application manifest, as defined in the [Web Application Manifest specification](https://developer.mozilla.org/docs/Web/Manifest).

```jsx filename="layout.js | page.js"
export const metadata = {
  manifest: 'https://nextjs.org/manifest.json',
}
```

```html filename="<head> output" hideLineNumbers
<link rel="manifest" href="https://nextjs.org/manifest.json" />
```

### `twitter`

The Twitter specification is (surprisingly) used for more than just X (formerly known as Twitter).

Learn more about the [Twitter Card markup reference](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/markup).

```jsx filename="layout.js | page.js"
export const metadata = {
  twitter: {
    card: 'summary_large_image',
    title: 'Next.js',
    description: 'The React Framework for the Web',
    siteId: '1467726470533754880',
    creator: '@nextjs',
    creatorId: '1467726470533754880',
    images: ['https://nextjs.org/og.png'], // Must be an absolute URL
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site:id" content="1467726470533754880" />
<meta name="twitter:creator" content="@nextjs" />
<meta name="twitter:creator:id" content="1467726470533754880" />
<meta name="twitter:title" content="Next.js" />
<meta name="twitter:description" content="The React Framework for the Web" />
<meta name="twitter:image" content="https://nextjs.org/og.png" />
```

```jsx filename="layout.js | page.js"
export const metadata = {
  twitter: {
    card: 'app',
    title: 'Next.js',
    description: 'The React Framework for the Web',
    siteId: '1467726470533754880',
    creator: '@nextjs',
    creatorId: '1467726470533754880',
    images: {
      url: 'https://nextjs.org/og.png',
      alt: 'Next.js Logo',
    },
    app: {
      name: 'twitter_app',
      id: {
        iphone: 'twitter_app://iphone',
        ipad: 'twitter_app://ipad',
        googleplay: 'twitter_app://googleplay',
      },
      url: {
        iphone: 'https://iphone_url',
        ipad: 'https://ipad_url',
      },
    },
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="twitter:site:id" content="1467726470533754880" />
<meta name="twitter:creator" content="@nextjs" />
<meta name="twitter:creator:id" content="1467726470533754880" />
<meta name="twitter:title" content="Next.js" />
<meta name="twitter:description" content="The React Framework for the Web" />
<meta name="twitter:card" content="app" />
<meta name="twitter:image" content="https://nextjs.org/og.png" />
<meta name="twitter:image:alt" content="Next.js Logo" />
<meta name="twitter:app:name:iphone" content="twitter_app" />
<meta name="twitter:app:id:iphone" content="twitter_app://iphone" />
<meta name="twitter:app:id:ipad" content="twitter_app://ipad" />
<meta name="twitter:app:id:googleplay" content="twitter_app://googleplay" />
<meta name="twitter:app:url:iphone" content="https://iphone_url" />
<meta name="twitter:app:url:ipad" content="https://ipad_url" />
<meta name="twitter:app:name:ipad" content="twitter_app" />
<meta name="twitter:app:name:googleplay" content="twitter_app" />
```

### `viewport`

> **Deprecated**: The `viewport` option in `metadata` is deprecated as of Next.js 14. Please use the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport.md) instead.

### `verification`

```jsx filename="layout.js | page.js"
export const metadata = {
  verification: {
    google: 'google',
    yandex: 'yandex',
    yahoo: 'yahoo',
    other: {
      me: ['my-email', 'my-link'],
    },
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="google-site-verification" content="google" />
<meta name="y_key" content="yahoo" />
<meta name="yandex-verification" content="yandex" />
<meta name="me" content="my-email" />
<meta name="me" content="my-link" />
```

### `appleWebApp`

```jsx filename="layout.js | page.js"
export const metadata = {
  itunes: {
    appId: 'myAppStoreID',
    appArgument: 'myAppArgument',
  },
  appleWebApp: {
    title: 'Apple Web App',
    statusBarStyle: 'black-translucent',
    startupImage: [
      '/assets/startup/apple-touch-startup-image-768x1004.png',
      {
        url: '/assets/startup/apple-touch-startup-image-1536x2008.png',
        media: '(device-width: 768px) and (device-height: 1024px)',
      },
    ],
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta
  name="apple-itunes-app"
  content="app-id=myAppStoreID, app-argument=myAppArgument"
/>
<meta name="mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-title" content="Apple Web App" />
<link
  href="/assets/startup/apple-touch-startup-image-768x1004.png"
  rel="apple-touch-startup-image"
/>
<link
  href="/assets/startup/apple-touch-startup-image-1536x2008.png"
  media="(device-width: 768px) and (device-height: 1024px)"
  rel="apple-touch-startup-image"
/>
<meta
  name="apple-mobile-web-app-status-bar-style"
  content="black-translucent"
/>
```

### `alternates`

```jsx filename="layout.js | page.js"
export const metadata = {
  alternates: {
    canonical: 'https://nextjs.org',
    languages: {
      'en-US': 'https://nextjs.org/en-US',
      'de-DE': 'https://nextjs.org/de-DE',
    },
    media: {
      'only screen and (max-width: 600px)': 'https://nextjs.org/mobile',
    },
    types: {
      'application/rss+xml': 'https://nextjs.org/rss',
    },
  },
}
```

```html filename="<head> output" hideLineNumbers
<link rel="canonical" href="https://nextjs.org" />
<link rel="alternate" hreflang="en-US" href="https://nextjs.org/en-US" />
<link rel="alternate" hreflang="de-DE" href="https://nextjs.org/de-DE" />
<link
  rel="alternate"
  media="only screen and (max-width: 600px)"
  href="https://nextjs.org/mobile"
/>
<link
  rel="alternate"
  type="application/rss+xml"
  href="https://nextjs.org/rss"
/>
```

### `appLinks`

```jsx filename="layout.js | page.js"
export const metadata = {
  appLinks: {
    ios: {
      url: 'https://nextjs.org/ios',
      app_store_id: 'app_store_id',
    },
    android: {
      package: 'com.example.android/package',
      app_name: 'app_name_android',
    },
    web: {
      url: 'https://nextjs.org/web',
      should_fallback: true,
    },
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta property="al:ios:url" content="https://nextjs.org/ios" />
<meta property="al:ios:app_store_id" content="app_store_id" />
<meta property="al:android:package" content="com.example.android/package" />
<meta property="al:android:app_name" content="app_name_android" />
<meta property="al:web:url" content="https://nextjs.org/web" />
<meta property="al:web:should_fallback" content="true" />
```

### `archives`

Describes a collection of records, documents, or other materials of historical interest ([source](https://www.w3.org/TR/2011/WD-html5-20110113/links.html#rel-archives)).

```jsx filename="layout.js | page.js"
export const metadata = {
  archives: ['https://nextjs.org/13'],
}
```

```html filename="<head> output" hideLineNumbers
<link rel="archives" href="https://nextjs.org/13" />
```

### `assets`

```jsx filename="layout.js | page.js"
export const metadata = {
  assets: ['https://nextjs.org/assets'],
}
```

```html filename="<head> output" hideLineNumbers
<link rel="assets" href="https://nextjs.org/assets" />
```

### `bookmarks`

```jsx filename="layout.js | page.js"
export const metadata = {
  bookmarks: ['https://nextjs.org/13'],
}
```

```html filename="<head> output" hideLineNumbers
<link rel="bookmarks" href="https://nextjs.org/13" />
```

### `category`

```jsx filename="layout.js | page.js"
export const metadata = {
  category: 'technology',
}
```

```html filename="<head> output" hideLineNumbers
<meta name="category" content="technology" />
```

### `facebook`

You can connect a Facebook app or Facebook account to your webpage for certain Facebook Social Plugins [Facebook Documentation](https://developers.facebook.com/docs/plugins/comments/#moderation-setup-instructions)

> **Good to know**: You can specify either appId or admins, but not both.

```jsx filename="layout.js | page.js"
export const metadata = {
  facebook: {
    appId: '12345678',
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta property="fb:app_id" content="12345678" />
```

```jsx filename="layout.js | page.js"
export const metadata = {
  facebook: {
    admins: '12345678',
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta property="fb:admins" content="12345678" />
```

If you want to generate multiple fb:admins meta tags you can use array value.

```jsx filename="layout.js | page.js"
export const metadata = {
  facebook: {
    admins: ['12345678', '87654321'],
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta property="fb:admins" content="12345678" />
<meta property="fb:admins" content="87654321" />
```

### `pinterest`

You can enable or disable [Pinterest Rich Pins](https://developers.pinterest.com/docs/web-features/rich-pins-overview/) on your webpage.

```jsx filename="layout.js | page.js"
export const metadata = {
  pinterest: {
    richPin: true,
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="pinterest-rich-pin" content="true" />
```

### `other`

All metadata options should be covered using the built-in support. However, there may be custom metadata tags specific to your site, or brand new metadata tags just released. You can use the `other` option to render any custom metadata tag.

```jsx filename="layout.js | page.js"
export const metadata = {
  other: {
    custom: 'meta',
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="custom" content="meta" />
```

If you want to generate multiple same key meta tags you can use array value.

```jsx filename="layout.js | page.js"
export const metadata = {
  other: {
    custom: ['meta1', 'meta2'],
  },
}
```

```html filename="<head> output" hideLineNumbers
<meta name="custom" content="meta1" /> <meta name="custom" content="meta2" />
```

### Types

You can add type safety to your metadata by using the `Metadata` type. If you are using the [built-in TypeScript plugin](/docs/app/api-reference/config/typescript.md) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

#### `metadata` object

```tsx filename="layout.tsx | page.tsx"
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Next.js',
}
```

#### `generateMetadata` function

##### Regular function

```tsx filename="layout.tsx | page.tsx"
import type { Metadata } from 'next'

export function generateMetadata(): Metadata {
  return {
    title: 'Next.js',
  }
}
```

##### Async function

```tsx filename="layout.tsx | page.tsx"
import type { Metadata } from 'next'

export async function generateMetadata(): Promise<Metadata> {
  return {
    title: 'Next.js',
  }
}
```

##### With segment props

```tsx filename="layout.tsx | page.tsx"
import type { Metadata } from 'next'

type Props = {
  params: Promise<{ id: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export function generateMetadata({ params, searchParams }: Props): Metadata {
  return {
    title: 'Next.js',
  }
}

export default function Page({ params, searchParams }: Props) {}
```

##### With parent metadata

```tsx filename="layout.tsx | page.tsx"
import type { Metadata, ResolvingMetadata } from 'next'

export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  return {
    title: 'Next.js',
  }
}
```

##### JavaScript Projects

For JavaScript projects, you can use JSDoc to add type safety.

```js filename="layout.js | page.js"
/** @type {import("next").Metadata} */
export const metadata = {
  title: 'Next.js',
}
```

### Unsupported Metadata

The following metadata types do not currently have built-in support. However, they can still be rendered in the layout or page itself.

| Metadata                      | Recommendation                                                                                                                                                                                                                               |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<meta http-equiv="...">`     | Use appropriate HTTP Headers via [`redirect()`](/docs/app/api-reference/functions/redirect.md), [Proxy](/docs/app/api-reference/file-conventions/proxy.md#nextresponse), [Security Headers](/docs/app/api-reference/config/next-config-js/headers.md) |
| `<base>`                      | Render the tag in the layout or page itself.                                                                                                                                                                                                 |
| `<noscript>`                  | Render the tag in the layout or page itself.                                                                                                                                                                                                 |
| `<style>`                     | Learn more about [styling in Next.js](/docs/app/getting-started/css.md).                                                                                                                                                                        |
| `<script>`                    | Learn more about [using scripts](/docs/app/guides/scripts.md).                                                                                                                                                                                  |
| `<link rel="stylesheet" />`   | `import` stylesheets directly in the layout or page itself.                                                                                                                                                                                  |
| `<link rel="preload />`       | Use [ReactDOM preload method](#link-relpreload)                                                                                                                                                                                              |
| `<link rel="preconnect" />`   | Use [ReactDOM preconnect method](#link-relpreconnect)                                                                                                                                                                                        |
| `<link rel="dns-prefetch" />` | Use [ReactDOM prefetchDNS method](#link-reldns-prefetch)                                                                                                                                                                                     |

### Resource hints

The `<link>` element has a number of `rel` keywords that can be used to hint to the browser that an external resource is likely to be needed. The browser uses this information to apply preloading optimizations depending on the keyword.

While the Metadata API doesn't directly support these hints, you can use new [`ReactDOM` methods](https://github.com/facebook/react/pull/26237) to safely insert them into the `<head>` of the document.

```tsx filename="app/preload-resources.tsx" switcher
'use client'

import ReactDOM from 'react-dom'

export function PreloadResources() {
  ReactDOM.preload('...', { as: '...' })
  ReactDOM.preconnect('...', { crossOrigin: '...' })
  ReactDOM.prefetchDNS('...')

  return '...'
}
```

```jsx filename="app/preload-resources.js" switcher
'use client'

import ReactDOM from 'react-dom'

export function PreloadResources() {
  ReactDOM.preload('...', { as: '...' })
  ReactDOM.preconnect('...', { crossOrigin: '...' })
  ReactDOM.prefetchDNS('...')

  return '...'
}
```

#### `<link rel="preload">`

Start loading a resource early in the page rendering (browser) lifecycle. [MDN Docs](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/preload).

```tsx
ReactDOM.preload(href: string, options: { as: string })
```

```html filename="<head> output" hideLineNumbers
<link rel="preload" href="..." as="..." />
```

##### `<link rel="preconnect">`

Preemptively initiate a connection to an origin. [MDN Docs](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/preconnect).

```tsx
ReactDOM.preconnect(href: string, options?: { crossOrigin?: string })
```

```html filename="<head> output" hideLineNumbers
<link rel="preconnect" href="..." crossorigin />
```

#### `<link rel="dns-prefetch">`

Attempt to resolve a domain name before resources get requested. [MDN Docs](https://developer.mozilla.org/docs/Web/HTML/Attributes/rel/dns-prefetch).

```tsx
ReactDOM.prefetchDNS(href: string)
```

```html filename="<head> output" hideLineNumbers
<link rel="dns-prefetch" href="..." />
```

> **Good to know**:
>
> * These methods are currently only supported in Client Components, which are still Server Side Rendered on initial page load.
> * Next.js in-built features such as `next/font`, `next/image` and `next/script` automatically handle relevant resource hints.

## Behavior

### Default Fields

There are two default `meta` tags that are always added even if a route doesn't define metadata:

* The [meta charset tag](https://developer.mozilla.org/docs/Web/HTML/Element/meta#attr-charset) sets the character encoding for the website.
* The [meta viewport tag](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag) sets the viewport width and scale for the website to adjust for different devices.

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

> **Good to know**: You can overwrite the default [`viewport`](/docs/app/api-reference/functions/generate-metadata.md#viewport) meta tag.

### Streaming metadata

Streaming metadata allows Next.js to render and send the initial UI to the browser, without waiting for `generateMetadata` to complete.

When `generateMetadata` resolves, the resulting metadata tags are appended to the `<body>` tag. We have verified that metadata is interpreted correctly by bots that execute JavaScript and inspect the full DOM (e.g. `Googlebot`).

For **HTML-limited bots** that can’t execute JavaScript (e.g. `facebookexternalhit`), metadata continues to block page rendering. The resulting metadata will be available in the `<head>` tag.

Next.js automatically detects **HTML-limited bots** by looking at the User Agent header. You can use the [`htmlLimitedBots`](/docs/app/api-reference/config/next-config-js/htmlLimitedBots.md) option in your Next.js config file to override the default [User Agent list](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts).

To fully disable streaming metadata:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const config: NextConfig = {
  htmlLimitedBots: /.*/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /.*/,
}
```

Streaming metadata improves perceived performance by reducing [TTFB](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) and can help lowering [LCP](https://developer.mozilla.org/docs/Glossary/Largest_contentful_paint) time.

Overriding `htmlLimitedBots` could lead to longer response times. Streaming metadata is an advanced feature, and the default should be sufficient for most cases.

### Ordering

Metadata is evaluated in order, starting from the root segment down to the segment closest to the final `page.js` segment. For example:

1. `app/layout.tsx` (Root Layout)
2. `app/blog/layout.tsx` (Nested Blog Layout)
3. `app/blog/[slug]/page.tsx` (Blog Page)

### Merging

Following the [evaluation order](#ordering), Metadata objects exported from multiple segments in the same route are **shallowly** merged together to form the final metadata output of a route. Duplicate keys are **replaced** based on their ordering.

This means metadata with nested fields such as [`openGraph`](/docs/app/api-reference/functions/generate-metadata.md#opengraph) and [`robots`](/docs/app/api-reference/functions/generate-metadata.md#robots) that are defined in an earlier segment are **overwritten** by the last segment to define them.

#### Overwriting fields

```jsx filename="app/layout.js"
export const metadata = {
  title: 'Acme',
  openGraph: {
    title: 'Acme',
    description: 'Acme is a...',
  },
}
```

```jsx filename="app/blog/page.js"
export const metadata = {
  title: 'Blog',
  openGraph: {
    title: 'Blog',
  },
}

// Output:
// <title>Blog</title>
// <meta property="og:title" content="Blog" />
```

In the example above:

* `title` from `app/layout.js` is **replaced** by `title` in `app/blog/page.js`.
* All `openGraph` fields from `app/layout.js` are **replaced** in `app/blog/page.js` because `app/blog/page.js` sets `openGraph` metadata. Note the absence of `openGraph.description`.

If you'd like to share some nested fields between segments while overwriting others, you can pull them out into a separate variable:

```jsx filename="app/shared-metadata.js"
export const openGraphImage = { images: ['http://...'] }
```

```jsx filename="app/page.js"
import { openGraphImage } from './shared-metadata'

export const metadata = {
  openGraph: {
    ...openGraphImage,
    title: 'Home',
  },
}
```

```jsx filename="app/about/page.js"
import { openGraphImage } from '../shared-metadata'

export const metadata = {
  openGraph: {
    ...openGraphImage,
    title: 'About',
  },
}
```

In the example above, the OG image is shared between `app/layout.js` and `app/about/page.js` while the titles are different.

#### Inheriting fields

```jsx filename="app/layout.js"
export const metadata = {
  title: 'Acme',
  openGraph: {
    title: 'Acme',
    description: 'Acme is a...',
  },
}
```

```jsx filename="app/about/page.js"
export const metadata = {
  title: 'About',
}

// Output:
// <title>About</title>
// <meta property="og:title" content="Acme" />
// <meta property="og:description" content="Acme is a..." />
```

**Notes**

* `title` from `app/layout.js` is **replaced** by `title` in `app/about/page.js`.
* All `openGraph` fields from `app/layout.js` are **inherited** in `app/about/page.js` because `app/about/page.js` doesn't set `openGraph` metadata.

## Version History

| Version   | Changes                                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v15.2.0` | Introduced streaming support to `generateMetadata`.                                                                                                     |
| `v13.2.0` | `viewport`, `themeColor`, and `colorScheme` deprecated in favor of the [`viewport` configuration](/docs/app/api-reference/functions/generate-viewport.md). |
| `v13.2.0` | `metadata` and `generateMetadata` introduced.                                                                                                           |
## Next Steps

View all the Metadata API options.

- [Metadata Files](/docs/app/api-reference/file-conventions/metadata.md)
  - API documentation for the metadata file conventions.
- [generateViewport](/docs/app/api-reference/functions/generate-viewport.md)
  - API Reference for the generateViewport function.


--------------------------------------------------------------------------------
title: "generateSitemaps"
description: "Learn how to use the generateSiteMaps function to create multiple sitemaps for your application."
source: "https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps"
--------------------------------------------------------------------------------

# generateSitemaps

You can use the `generateSitemaps` function to generate multiple sitemaps for your application.

## Returns

The `generateSitemaps` returns an array of objects with an `id` property.

## URLs

Your generated sitemaps will be available at `/.../sitemap/[id].xml`. For example, `/product/sitemap/1.xml`.

## Example

For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.

```ts filename="app/product/sitemap.ts" switcher
import type { MetadataRoute } from 'next'
import { BASE_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap(props: {
  id: Promise<number>
}): Promise<MetadataRoute.Sitemap> {
  const id = await props.id
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
  )
  return products.map((product) => ({
    url: `${BASE_URL}/product/${product.id}`,
    lastModified: product.date,
  }))
}
```

```js filename="app/product/sitemap.js" switcher
import { BASE_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap(props) {
  const id = await props.id
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
  )
  return products.map((product) => ({
    url: `${BASE_URL}/product/${product.id}`,
    lastModified: product.date,
  }))
}
```

## Version History

| Version   | Changes                                                                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | The `id` values returned from `generateSitemaps` are now passed as a promise to the sitemap function.                                                |
| `v15.0.0` | `generateSitemaps` now generates consistent URLs between development and production                                                                  |
| `v13.3.2` | `generateSitemaps` introduced. In development, you can view the generated sitemap on `/.../sitemap.xml/[id]`. For example, `/product/sitemap.xml/1`. |
## Next Steps

Learn how to create sitemaps for your Next.js application.

- [sitemap.xml](/docs/app/api-reference/file-conventions/metadata/sitemap.md)
  - API Reference for the sitemap.xml file.


--------------------------------------------------------------------------------
title: "generateStaticParams"
description: "API reference for the generateStaticParams function."
source: "https://nextjs.org/docs/app/api-reference/functions/generate-static-params"
--------------------------------------------------------------------------------

# generateStaticParams

The `generateStaticParams` function can be used in combination with [dynamic route segments](/docs/app/api-reference/file-conventions/dynamic-routes.md) to [**statically generate**](/docs/app/guides/caching.md#static-rendering) routes at build time instead of on-demand at request time.

```tsx filename="app/blog/[slug]/page.tsx" switcher
// Return a list of `params` to populate the [slug] dynamic segment
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

// Multiple versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
// Return a list of `params` to populate the [slug] dynamic segment
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

// Multiple versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
export default async function Page({ params }) {
  const { slug } = await params
  // ...
}
```

> **Good to know**:
>
> * You can use the [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) segment config option to control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.
> * You must return [an empty array from `generateStaticParams`](#all-paths-at-build-time) or utilize [`export const dynamic = 'force-static'`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamic) in order to revalidate (ISR) [paths at runtime](#all-paths-at-runtime).
> * During `next dev`, `generateStaticParams` will be called when you navigate to a route.
> * During `next build`, `generateStaticParams` runs before the corresponding Layouts or Pages are generated.
> * During revalidation (ISR), `generateStaticParams` will not be called again.
> * `generateStaticParams` replaces the [`getStaticPaths`](/docs/pages/api-reference/functions/get-static-paths.md) function in the Pages Router.

## Parameters

`options.params` (optional)

If multiple dynamic segments in a route use `generateStaticParams`, the child `generateStaticParams` function is executed once for each set of `params` the parent generates.

The `params` object contains the populated `params` from the parent `generateStaticParams`, which can be used to [generate the `params` in a child segment](#multiple-dynamic-segments-in-a-route).

## Returns

`generateStaticParams` should return an array of objects where each object represents the populated dynamic segments of a single route.

* Each property in the object is a dynamic segment to be filled in for the route.
* The properties name is the segment's name, and the properties value is what that segment should be filled in with.

| Example Route                    | `generateStaticParams` Return Type        |
| -------------------------------- | ----------------------------------------- |
| `/product/[id]`                  | `{ id: string }[]`                        |
| `/products/[category]/[product]` | `{ category: string, product: string }[]` |
| `/products/[...slug]`            | `{ slug: string[] }[]`                    |

## Single Dynamic Segment

```tsx filename="app/product/[id]/page.tsx" switcher
export function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/1
// - /product/2
// - /product/3
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  // ...
}
```

```jsx filename="app/product/[id]/page.js" switcher
export function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }, { id: '3' }]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/1
// - /product/2
// - /product/3
export default async function Page({ params }) {
  const { id } = await params
  // ...
}
```

## Multiple Dynamic Segments

```tsx filename="app/products/[category]/[product]/page.tsx" switcher
export function generateStaticParams() {
  return [
    { category: 'a', product: '1' },
    { category: 'b', product: '2' },
    { category: 'c', product: '3' },
  ]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /products/a/1
// - /products/b/2
// - /products/c/3
export default async function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  const { category, product } = await params
  // ...
}
```

```jsx filename="app/products/[category]/[product]/page.js" switcher
export function generateStaticParams() {
  return [
    { category: 'a', product: '1' },
    { category: 'b', product: '2' },
    { category: 'c', product: '3' },
  ]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /products/a/1
// - /products/b/2
// - /products/c/3
export default async function Page({ params }) {
  const { category, product } = await params
  // ...
}
```

## Catch-all Dynamic Segment

```tsx filename="app/product/[...slug]/page.tsx" switcher
export function generateStaticParams() {
  return [{ slug: ['a', '1'] }, { slug: ['b', '2'] }, { slug: ['c', '3'] }]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/a/1
// - /product/b/2
// - /product/c/3
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string[] }>
}) {
  const { slug } = await params
  // ...
}
```

```jsx filename="app/product/[...slug]/page.js" switcher
export function generateStaticParams() {
  return [{ slug: ['a', '1'] }, { slug: ['b', '2'] }, { slug: ['c', '3'] }]
}

// Three versions of this page will be statically generated
// using the `params` returned by `generateStaticParams`
// - /product/a/1
// - /product/b/2
// - /product/c/3
export default async function Page({ params }) {
  const { slug } = await params
  // ...
}
```

## Examples

### Static Rendering

#### All paths at build time

To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:

```tsx filename="app/blog/[slug]/page.tsx" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

#### Subset of paths at build time

To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:

```tsx filename="app/blog/[slug]/page.tsx" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  // Render the first 10 posts at build time
  return posts.slice(0, 10).map((post) => ({
    slug: post.slug,
  }))
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  // Render the first 10 posts at build time
  return posts.slice(0, 10).map((post) => ({
    slug: post.slug,
  }))
}
```

Then, by using the [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) segment config option, you can control what happens when a dynamic segment is visited that was not generated with `generateStaticParams`.

```tsx filename="app/blog/[slug]/page.tsx" switcher
// All posts besides the top 10 will be a 404
export const dynamicParams = false

export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
  const topPosts = posts.slice(0, 10)

  return topPosts.map((post) => ({
    slug: post.slug,
  }))
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
// All posts besides the top 10 will be a 404
export const dynamicParams = false

export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())
  const topPosts = posts.slice(0, 10)

  return topPosts.map((post) => ({
    slug: post.slug,
  }))
}
```

#### All paths at runtime

To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize [`export const dynamic = 'force-static'`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamic):

```jsx filename="app/blog/[slug]/page.js"
export async function generateStaticParams() {
  return []
}
```

> **Good to know:** You must always return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.

```jsx filename="app/changelog/[slug]/page.js"
export const dynamic = 'force-static'
```

### Disable rendering for unspecified paths

To prevent unspecified paths from being statically rendered at runtime, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and unspecified routes will 404 or match (in the case of [catch-all routes](/docs/app/api-reference/file-conventions/dynamic-routes.md#catch-all-segments)).

### Multiple Dynamic Segments in a Route

You can generate params for dynamic segments above the current layout or page, but **not below**. For example, given the `app/products/[category]/[product]` route:

* `app/products/[category]/[product]/page.js` can generate params for **both** `[category]` and `[product]`.
* `app/products/[category]/layout.js` can **only** generate params for `[category]`.

There are two approaches to generating params for a route with multiple dynamic segments:

#### Generate params from the bottom up

Generate multiple dynamic segments from the child route segment.

```tsx filename="app/products/[category]/[product]/page.tsx" switcher
// Generate segments for both [category] and [product]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())

  return products.map((product) => ({
    category: product.category.slug,
    product: product.id,
  }))
}

export default function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  // ...
}
```

```jsx filename="app/products/[category]/[product]/page.js" switcher
// Generate segments for both [category] and [product]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())

  return products.map((product) => ({
    category: product.category.slug,
    product: product.id,
  }))
}

export default function Page({ params }) {
  // ...
}
```

#### Generate params from the top down

Generate the parent segments first and use the result to generate the child segments.

```tsx filename="app/products/[category]/layout.tsx" switcher
// Generate segments for [category]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())

  return products.map((product) => ({
    category: product.category.slug,
  }))
}

export default function Layout({
  params,
}: {
  params: Promise<{ category: string }>
}) {
  // ...
}
```

```jsx filename="app/products/[category]/layout.js" switcher
// Generate segments for [category]
export async function generateStaticParams() {
  const products = await fetch('https://.../products').then((res) => res.json())

  return products.map((product) => ({
    category: product.category.slug,
  }))
}

export default function Layout({ params }) {
  // ...
}
```

A child route segment's `generateStaticParams` function is executed once for each segment a parent `generateStaticParams` generates.

The child `generateStaticParams` function can use the `params` returned from the parent `generateStaticParams` function to dynamically generate its own segments.

```tsx filename="app/products/[category]/[product]/page.tsx" switcher
// Generate segments for [product] using the `params` passed from
// the parent segment's `generateStaticParams` function
export async function generateStaticParams({
  params: { category },
}: {
  params: { category: string }
}) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())

  return products.map((product) => ({
    product: product.id,
  }))
}

export default function Page({
  params,
}: {
  params: Promise<{ category: string; product: string }>
}) {
  // ...
}
```

```jsx filename="app/products/[category]/[product]/page.js" switcher
// Generate segments for [product] using the `params` passed from
// the parent segment's `generateStaticParams` function
export async function generateStaticParams({ params: { category } }) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())

  return products.map((product) => ({
    product: product.id,
  }))
}

export default function Page({ params }) {
  // ...
}
```

Notice that the params argument can be accessed synchronously and includes only parent segment params.

For type completion, you can make use of the TypeScript `Awaited` helper in combination with either [`Page Props helper`](/docs/app/api-reference/file-conventions/page.md#page-props-helper) or [`Layout Props helper`](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper):

```ts filename="app/products/[category]/[product]/page.tsx" switcher
export async function generateStaticParams({
  params: { category },
}: {
  params: Awaited<LayoutProps<'/products/[category]'>['params']>
}) {
  const products = await fetch(
    `https://.../products?category=${category}`
  ).then((res) => res.json())

  return products.map((product) => ({
    product: product.id,
  }))
}
```

> **Good to know**: `fetch` requests are automatically [memoized](/docs/app/guides/caching.md#request-memoization) for the same data across all `generate`-prefixed functions, Layouts, Pages, and Server Components. React [`cache` can be used](/docs/app/guides/caching.md#react-cache-function) if `fetch` is unavailable.

## Version History

| Version   | Changes                            |
| --------- | ---------------------------------- |
| `v13.0.0` | `generateStaticParams` introduced. |


--------------------------------------------------------------------------------
title: "generateViewport"
description: "API Reference for the generateViewport function."
source: "https://nextjs.org/docs/app/api-reference/functions/generate-viewport"
--------------------------------------------------------------------------------

# generateViewport

You can customize the initial viewport of the page with the static `viewport` object or the dynamic `generateViewport` function.

> **Good to know**:
>
> * The `viewport` object and `generateViewport` function exports are **only supported in Server Components**.
> * You cannot export both the `viewport` object and `generateViewport` function from the same route segment.
> * If you're coming from migrating `metadata` exports, you can use [metadata-to-viewport-export codemod](/docs/app/guides/upgrading/codemods.md#metadata-to-viewport-export) to update your changes.

## The `viewport` object

To define the viewport options, export a `viewport` object from a `layout.jsx` or `page.jsx` file.

```tsx filename="layout.tsx | page.tsx" switcher
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: 'black',
}

export default function Page() {}
```

```jsx filename="layout.jsx | page.jsx" switcher
export const viewport = {
  themeColor: 'black',
}

export default function Page() {}
```

## `generateViewport` function

`generateViewport` should return a [`Viewport` object](#viewport-fields) containing one or more viewport fields.

```tsx filename="layout.tsx | page.tsx" switcher
export function generateViewport({ params }) {
  return {
    themeColor: '...',
  }
}
```

In TypeScript, the `params` argument can be typed via [`PageProps<'/route'>`](/docs/app/api-reference/file-conventions/page.md#page-props-helper) or [`LayoutProps<'/route'>`](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper) depending on where `generateViewport` is defined.

```jsx filename="layout.js | page.js" switcher
export function generateViewport({ params }) {
  return {
    themeColor: '...',
  }
}
```

> **Good to know**:
>
> * If the viewport doesn't depend on runtime information, it should be defined using the static [`viewport` object](#the-viewport-object) rather than `generateViewport`.

## Viewport Fields

### `themeColor`

Learn more about [`theme-color`](https://developer.mozilla.org/docs/Web/HTML/Element/meta/name/theme-color).

**Simple theme color**

```tsx filename="layout.tsx | page.tsx" switcher
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: 'black',
}
```

```jsx filename="layout.jsx | page.jsx" switcher
export const viewport = {
  themeColor: 'black',
}
```

```html filename="<head> output" hideLineNumbers
<meta name="theme-color" content="black" />
```

**With media attribute**

```tsx filename="layout.tsx | page.tsx" switcher
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: 'cyan' },
    { media: '(prefers-color-scheme: dark)', color: 'black' },
  ],
}
```

```jsx filename="layout.jsx | page.jsx" switcher
export const viewport = {
  themeColor: [
    { media: '(prefers-color-scheme: light)', color: 'cyan' },
    { media: '(prefers-color-scheme: dark)', color: 'black' },
  ],
}
```

```html filename="<head> output" hideLineNumbers
<meta name="theme-color" media="(prefers-color-scheme: light)" content="cyan" />
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="black" />
```

### `width`, `initialScale`, `maximumScale` and `userScalable`

> **Good to know**: The `viewport` meta tag is automatically set, and manual configuration is usually unnecessary as the default is sufficient. However, the information is provided for completeness.

```tsx filename="layout.tsx | page.tsx" switcher
import type { Viewport } from 'next'

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  // Also supported but less commonly used
  // interactiveWidget: 'resizes-visual',
}
```

```jsx filename="layout.jsx | page.jsx" switcher
export const viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  // Also supported but less commonly used
  // interactiveWidget: 'resizes-visual',
}
```

```html filename="<head> output" hideLineNumbers
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"
/>
```

### `colorScheme`

Learn more about [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta/name#:~:text=color%2Dscheme%3A%20specifies,of%20the%20following%3A).

```tsx filename="layout.tsx | page.tsx" switcher
import type { Viewport } from 'next'

export const viewport: Viewport = {
  colorScheme: 'dark',
}
```

```jsx filename="layout.jsx | page.jsx" switcher
export const viewport = {
  colorScheme: 'dark',
}
```

```html filename="<head> output" hideLineNumbers
<meta name="color-scheme" content="dark" />
```

## Types

You can add type safety to your viewport object by using the `Viewport` type. If you are using the [built-in TypeScript plugin](/docs/app/api-reference/config/typescript.md) in your IDE, you do not need to manually add the type, but you can still explicitly add it if you want.

### `viewport` object

```tsx
import type { Viewport } from 'next'

export const viewport: Viewport = {
  themeColor: 'black',
}
```

### `generateViewport` function

#### Regular function

```tsx
import type { Viewport } from 'next'

export function generateViewport(): Viewport {
  return {
    themeColor: 'black',
  }
}
```

#### With segment props

```tsx
import type { Viewport } from 'next'

type Props = {
  params: Promise<{ id: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export function generateViewport({ params, searchParams }: Props): Viewport {
  return {
    themeColor: 'black',
  }
}

export default function Page({ params, searchParams }: Props) {}
```

#### JavaScript Projects

For JavaScript projects, you can use JSDoc to add type safety.

```js
/** @type {import("next").Viewport} */
export const viewport = {
  themeColor: 'black',
}
```

## Version History

| Version   | Changes                                       |
| --------- | --------------------------------------------- |
| `v14.0.0` | `viewport` and `generateViewport` introduced. |
## Next Steps

View all the Metadata API options.

- [Metadata Files](/docs/app/api-reference/file-conventions/metadata.md)
  - API documentation for the metadata file conventions.


--------------------------------------------------------------------------------
title: "headers"
description: "API reference for the headers function."
source: "https://nextjs.org/docs/app/api-reference/functions/headers"
--------------------------------------------------------------------------------

# headers

`headers` is an **async** function that allows you to **read** the HTTP incoming request headers from a [Server Component](/docs/app/getting-started/server-and-client-components.md).

```tsx filename="app/page.tsx" switcher
import { headers } from 'next/headers'

export default async function Page() {
  const headersList = await headers()
  const userAgent = headersList.get('user-agent')
}
```

```jsx filename="app/page.js" switcher
import { headers } from 'next/headers'

export default async function Page() {
  const headersList = await headers()
  const userAgent = headersList.get('user-agent')
}
```

## Reference

### Parameters

`headers` does not take any parameters.

### Returns

`headers` returns a **read-only** [Web Headers](https://developer.mozilla.org/docs/Web/API/Headers) object.

* [`Headers.entries()`](https://developer.mozilla.org/docs/Web/API/Headers/entries): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing to go through all key/value pairs contained in this object.
* [`Headers.forEach()`](https://developer.mozilla.org/docs/Web/API/Headers/forEach): Executes a provided function once for each key/value pair in this `Headers` object.
* [`Headers.get()`](https://developer.mozilla.org/docs/Web/API/Headers/get): Returns a [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) sequence of all the values of a header within a `Headers` object with a given name.
* [`Headers.has()`](https://developer.mozilla.org/docs/Web/API/Headers/has): Returns a boolean stating whether a `Headers` object contains a certain header.
* [`Headers.keys()`](https://developer.mozilla.org/docs/Web/API/Headers/keys): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all keys of the key/value pairs contained in this object.
* [`Headers.values()`](https://developer.mozilla.org/docs/Web/API/Headers/values): Returns an [`iterator`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Iteration_protocols) allowing you to go through all values of the key/value pairs contained in this object.

## Good to know

* `headers` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
  * In version 14 and earlier, `headers` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* Since `headers` is read-only, you cannot `set` or `delete` the outgoing request headers.
* `headers` is a [Dynamic API](/docs/app/guides/caching.md#dynamic-rendering) whose returned values cannot be known ahead of time. Using it in will opt a route into **[dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering)**.

## Examples

### Using the Authorization header

```jsx filename="app/page.js"
import { headers } from 'next/headers'

export default async function Page() {
  const authorization = (await headers()).get('authorization')
  const res = await fetch('...', {
    headers: { authorization }, // Forward the authorization header
  })
  const user = await res.json()

  return <h1>{user.name}</h1>
}
```

## Version History

| Version      | Changes                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| `v15.0.0-RC` | `headers` is now an async function. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available. |
| `v13.0.0`    | `headers` introduced.                                                                                  |


--------------------------------------------------------------------------------
title: "ImageResponse"
description: "API Reference for the ImageResponse constructor."
source: "https://nextjs.org/docs/app/api-reference/functions/image-response"
--------------------------------------------------------------------------------

# ImageResponse

The `ImageResponse` constructor allows you to generate dynamic images using JSX and CSS. This is useful for generating social media images such as Open Graph images, Twitter cards, and more.

## Reference

### Parameters

The following parameters are available for `ImageResponse`:

```jsx
import { ImageResponse } from 'next/og'

new ImageResponse(
  element: ReactElement,
  options: {
    width?: number = 1200
    height?: number = 630
    emoji?: 'twemoji' | 'blobmoji' | 'noto' | 'openmoji' = 'twemoji',
    fonts?: {
      name: string,
      data: ArrayBuffer,
      weight: number,
      style: 'normal' | 'italic'
    }[]
    debug?: boolean = false

    // Options that will be passed to the HTTP response
    status?: number = 200
    statusText?: string
    headers?: Record<string, string>
  },
)
```

> Examples are available in the [Vercel OG Playground](https://og-playground.vercel.app/).

### Supported HTML and CSS features

`ImageResponse` supports common CSS properties including flexbox and absolute positioning, custom fonts, text wrapping, centering, and nested images.

Please refer to [Satori’s documentation](https://github.com/vercel/satori#css) for a list of supported HTML and CSS features.

## Behavior

* `ImageResponse` uses [@vercel/og](https://vercel.com/docs/concepts/functions/edge-functions/og-image-generation), [Satori](https://github.com/vercel/satori), and Resvg to convert HTML and CSS into PNG.
* Only flexbox and a subset of CSS properties are supported. Advanced layouts (e.g. `display: grid`) will not work.
* Maximum bundle size of `500KB`. The bundle size includes your JSX, CSS, fonts, images, and any other assets. If you exceed the limit, consider reducing the size of any assets or fetching at runtime.
* Only `ttf`, `otf`, and `woff` font formats are supported. To maximize the font parsing speed, `ttf` or `otf` are preferred over `woff`.

## Examples

### Route Handlers

`ImageResponse` can be used in Route Handlers to generate images dynamically at request time.

```js filename="app/api/route.js"
import { ImageResponse } from 'next/og'

export async function GET() {
  try {
    return new ImageResponse(
      (
        <div
          style={{
            height: '100%',
            width: '100%',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            backgroundColor: 'white',
            padding: '40px',
          }}
        >
          <div
            style={{
              fontSize: 60,
              fontWeight: 'bold',
              color: 'black',
              textAlign: 'center',
            }}
          >
            Welcome to My Site
          </div>
          <div
            style={{
              fontSize: 30,
              color: '#666',
              marginTop: '20px',
            }}
          >
            Generated with Next.js ImageResponse
          </div>
        </div>
      ),
      {
        width: 1200,
        height: 630,
      }
    )
  } catch (e) {
    console.log(`${e.message}`)
    return new Response(`Failed to generate the image`, {
      status: 500,
    })
  }
}
```

### File-based Metadata

You can use `ImageResponse` in a [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md) file to generate Open Graph images at build time or dynamically at request time.

```tsx filename="app/opengraph-image.tsx"
import { ImageResponse } from 'next/og'

// Image metadata
export const alt = 'My site'
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image() {
  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        My site
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can re-use the exported opengraph-image
      // size config to also set the ImageResponse's width and height.
      ...size,
    }
  )
}
```

### Custom fonts

You can use custom fonts in your `ImageResponse` by providing a `fonts` array in the options.

```tsx filename="app/opengraph-image.tsx"
import { ImageResponse } from 'next/og'
import { readFile } from 'node:fs/promises'
import { join } from 'node:path'

// Image metadata
export const alt = 'My site'
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image() {
  // Font loading, process.cwd() is Next.js project directory
  const interSemiBold = await readFile(
    join(process.cwd(), 'assets/Inter-SemiBold.ttf')
  )

  return new ImageResponse(
    (
      // ...
    ),
    // ImageResponse options
    {
      // For convenience, we can re-use the exported opengraph-image
      // size config to also set the ImageResponse's width and height.
      ...size,
      fonts: [
        {
          name: 'Inter',
          data: interSemiBold,
          style: 'normal',
          weight: 400,
        },
      ],
    }
  )
}
```

## Version History

| Version   | Changes                                               |
| --------- | ----------------------------------------------------- |
| `v14.0.0` | `ImageResponse` moved from `next/server` to `next/og` |
| `v13.3.0` | `ImageResponse` can be imported from `next/server`.   |
| `v13.0.0` | `ImageResponse` introduced via `@vercel/og` package.  |


--------------------------------------------------------------------------------
title: "NextRequest"
description: "API Reference for NextRequest."
source: "https://nextjs.org/docs/app/api-reference/functions/next-request"
--------------------------------------------------------------------------------

# NextRequest

NextRequest extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional convenience methods.

## `cookies`

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the request.

### `set(name, value)`

Given a name, set a cookie with the given value on the request.

```ts
// Given incoming request /home
// Set a cookie to hide the banner
// request will have a `Set-Cookie:show-banner=false;path=/home` header
request.cookies.set('show-banner', 'false')
```

### `get(name)`

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

```ts
// Given incoming request /home
// { name: 'show-banner', value: 'false', Path: '/home' }
request.cookies.get('show-banner')
```

### `getAll()`

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.

```ts
// Given incoming request /home
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
request.cookies.getAll('experiments')
// Alternatively, get all cookies for the request
request.cookies.getAll()
```

### `delete(name)`

Given a cookie name, delete the cookie from the request.

```ts
// Returns true for deleted, false is nothing is deleted
request.cookies.delete('experiments')
```

### `has(name)`

Given a cookie name, return `true` if the cookie exists on the request.

```ts
// Returns true if cookie exists, false if it does not
request.cookies.has('experiments')
```

### `clear()`

Remove the `Set-Cookie` header from the request.

```ts
request.cookies.clear()
```

## `nextUrl`

Extends the native [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API with additional convenience methods, including Next.js specific properties.

```ts
// Given a request to /home, pathname is /home
request.nextUrl.pathname
// Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
request.nextUrl.searchParams
```

The following options are available:

| Property       | Type                    | Description                                                                                                                          |
| -------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `basePath`     | `string`                | The [base path](/docs/app/api-reference/config/next-config-js/basePath.md) of the URL.                                                  |
| `buildId`      | `string` | `undefined` | The build identifier of the Next.js application. Can be [customized](/docs/app/api-reference/config/next-config-js/generateBuildId.md). |
| `pathname`     | `string`                | The pathname of the URL.                                                                                                             |
| `searchParams` | `Object`                | The search parameters of the URL.                                                                                                    |

> **Note:** The internationalization properties from the Pages Router are not available for usage in the App Router. Learn more about [internationalization with the App Router](/docs/app/guides/internationalization.md).

## Version History

| Version   | Changes                 |
| --------- | ----------------------- |
| `v15.0.0` | `ip` and `geo` removed. |


--------------------------------------------------------------------------------
title: "NextResponse"
description: "API Reference for NextResponse."
source: "https://nextjs.org/docs/app/api-reference/functions/next-response"
--------------------------------------------------------------------------------

# NextResponse

NextResponse extends the [Web Response API](https://developer.mozilla.org/docs/Web/API/Response) with additional convenience methods.

## `cookies`

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the response.

### `set(name, value)`

Given a name, set a cookie with the given value on the response.

```ts
// Given incoming request /home
let response = NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show-banner', 'false')
// Response will have a `Set-Cookie:show-banner=false;path=/home` header
return response
```

### `get(name)`

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

```ts
// Given incoming request /home
let response = NextResponse.next()
// { name: 'show-banner', value: 'false', Path: '/home' }
response.cookies.get('show-banner')
```

### `getAll()`

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.

```ts
// Given incoming request /home
let response = NextResponse.next()
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
```

### `delete(name)`

Given a cookie name, delete the cookie from the response.

```ts
// Given incoming request /home
let response = NextResponse.next()
// Returns true for deleted, false if nothing is deleted
response.cookies.delete('experiments')
```

## `json()`

Produce a response with the given JSON body.

```ts filename="app/api/route.ts" switcher
import { NextResponse } from 'next/server'

export async function GET(request: Request) {
  return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
```

```js filename="app/api/route.js" switcher
import { NextResponse } from 'next/server'

export async function GET(request) {
  return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
```

## `redirect()`

Produce a response that redirects to a [URL](https://developer.mozilla.org/docs/Web/API/URL).

```ts
import { NextResponse } from 'next/server'

return NextResponse.redirect(new URL('/new', request.url))
```

The [URL](https://developer.mozilla.org/docs/Web/API/URL) can be created and modified before being used in the `NextResponse.redirect()` method. For example, you can use the `request.nextUrl` property to get the current URL, and then modify it to redirect to a different URL.

```ts
import { NextResponse } from 'next/server'

// Given an incoming request...
const loginUrl = new URL('/login', request.url)
// Add ?from=/incoming-url to the /login URL
loginUrl.searchParams.set('from', request.nextUrl.pathname)
// And redirect to the new URL
return NextResponse.redirect(loginUrl)
```

## `rewrite()`

Produce a response that rewrites (proxies) the given [URL](https://developer.mozilla.org/docs/Web/API/URL) while preserving the original URL.

```ts
import { NextResponse } from 'next/server'

// Incoming request: /about, browser shows /about
// Rewritten request: /proxy, browser shows /about
return NextResponse.rewrite(new URL('/proxy', request.url))
```

## `next()`

The `next()` method is useful for Proxy, as it allows you to return early and continue routing.

```ts
import { NextResponse } from 'next/server'

return NextResponse.next()
```

You can also forward `headers` upstream when producing the response, using `NextResponse.next({ request: { headers } })`:

```ts
import { NextResponse } from 'next/server'

// Given an incoming request...
const newHeaders = new Headers(request.headers)
// Add a new header
newHeaders.set('x-version', '123')
// Forward the modified request headers upstream
return NextResponse.next({
  request: {
    // New request headers
    headers: newHeaders,
  },
})
```

This forwards `newHeaders` upstream to the target page, route, or server action, and does not expose them to the client. While this pattern is useful for passing data upstream, it should be used with caution because the headers containing this data may be forwarded to external services.

In contrast, `NextResponse.next({ headers })` is a shorthand for sending headers from proxy to the client. This is **NOT** good practice and should be avoided. Among other reasons because setting response headers like `Content-Type`, can override framework expectations (for example, the `Content-Type` used by Server Actions), leading to failed submissions or broken streaming responses.

```ts
import { type NextRequest, NextResponse } from 'next/server'

async function proxy(request: NextRequest) {
  const headers = await injectAuth(request.headers)
  // DO NOT forward headers like this
  return NextResponse.next({ headers })
}
```

In general, avoid copying all incoming request headers because doing so can leak sensitive data to clients or upstream services.

Prefer a defensive approach by creating a subset of incoming request headers using an allow-list. For example, you might discard custom `x-*` headers and only forward known-safe headers:

```ts
import { type NextRequest, NextResponse } from 'next/server'

function proxy(request: NextRequest) {
  const incoming = new Headers(request.headers)
  const forwarded = new Headers()

  for (const [name, value] of incoming) {
    const headerName = name.toLowerCase()
    // Keep only known-safe headers, discard custom x-* and other sensitive ones
    if (
      !headerName.startsWith('x-') &&
      headerName !== 'authorization' &&
      headerName !== 'cookie'
    ) {
      // Preserve original header name casing
      forwarded.set(name, value)
    }
  }

  return NextResponse.next({
    request: {
      headers: forwarded,
    },
  })
}
```


--------------------------------------------------------------------------------
title: "notFound"
description: "API Reference for the notFound function."
source: "https://nextjs.org/docs/app/api-reference/functions/not-found"
--------------------------------------------------------------------------------

# notFound

The `notFound` function allows you to render the [`not-found file`](/docs/app/api-reference/file-conventions/not-found.md) within a route segment as well as inject a `<meta name="robots" content="noindex" />` tag.

## `notFound()`

Invoking the `notFound()` function throws a `NEXT_HTTP_ERROR_FALLBACK;404` error and terminates rendering of the route segment in which it was thrown. Specifying a [**not-found** file](/docs/app/api-reference/file-conventions/not-found.md) allows you to gracefully handle such errors by rendering a Not Found UI within the segment.

```jsx filename="app/user/[id]/page.js"
import { notFound } from 'next/navigation'

async function fetchUser(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({ params }) {
  const { id } = await params
  const user = await fetchUser(id)

  if (!user) {
    notFound()
  }

  // ...
}
```

> **Good to know**: `notFound()` does not require you to use `return notFound()` due to using the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

## Version History

| Version   | Changes                |
| --------- | ---------------------- |
| `v13.0.0` | `notFound` introduced. |


--------------------------------------------------------------------------------
title: "permanentRedirect"
description: "API Reference for the permanentRedirect function."
source: "https://nextjs.org/docs/app/api-reference/functions/permanentRedirect"
--------------------------------------------------------------------------------

# permanentRedirect

The `permanentRedirect` function allows you to redirect the user to another URL. `permanentRedirect` can be used in Server Components, Client Components, [Route Handlers](/docs/app/api-reference/file-conventions/route.md), and [Server Actions](/docs/app/getting-started/updating-data.md).

When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 308 (Permanent) HTTP redirect response to the caller.

If a resource doesn't exist, you can use the [`notFound` function](/docs/app/api-reference/functions/not-found.md) instead.

> **Good to know**: If you prefer to return a 307 (Temporary) HTTP redirect instead of 308 (Permanent), you can use the [`redirect` function](/docs/app/api-reference/functions/redirect.md) instead.

## Parameters

The `permanentRedirect` function accepts two arguments:

```js
permanentRedirect(path, type)
```

| Parameter | Type                                                          | Description                                                 |
| --------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| `path`    | `string`                                                      | The URL to redirect to. Can be a relative or absolute path. |
| `type`    | `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform.                            |

By default, `permanentRedirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](/docs/app/getting-started/updating-data.md) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.

The `type` parameter has no effect when used in Server Components.

## Returns

`permanentRedirect` does not return a value.

## Example

Invoking the `permanentRedirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.

```jsx filename="app/team/[id]/page.js"
import { permanentRedirect } from 'next/navigation'

async function fetchTeam(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({ params }) {
  const { id } = await params
  const team = await fetchTeam(id)
  if (!team) {
    permanentRedirect('/login')
  }

  // ...
}
```

> **Good to know**: `permanentRedirect` does not require you to use `return permanentRedirect()` as it uses the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.
- [redirect](/docs/app/api-reference/functions/redirect.md)
  - API Reference for the redirect function.


--------------------------------------------------------------------------------
title: "redirect"
description: "API Reference for the redirect function."
source: "https://nextjs.org/docs/app/api-reference/functions/redirect"
--------------------------------------------------------------------------------

# redirect

The `redirect` function allows you to redirect the user to another URL. `redirect` can be used while rendering in [Server and Client Components](/docs/app/getting-started/server-and-client-components.md), [Route Handlers](/docs/app/api-reference/file-conventions/route.md), and [Server Actions](/docs/app/getting-started/updating-data.md).

When used in a [streaming context](/docs/app/getting-started/linking-and-navigating.md#streaming), this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.

If a resource doesn't exist, you can use the [`notFound` function](/docs/app/api-reference/functions/not-found.md) instead.

## Reference

### Parameters

The `redirect` function accepts two arguments:

```js
redirect(path, type)
```

| Parameter | Type                                                          | Description                                                 |
| --------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| `path`    | `string`                                                      | The URL to redirect to. Can be a relative or absolute path. |
| `type`    | `'replace'` (default) or `'push'` (default in Server Actions) | The type of redirect to perform.                            |

By default, `redirect` will use `push` (adding a new entry to the browser history stack) in [Server Actions](/docs/app/getting-started/updating-data.md) and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.

The `RedirectType` object contains the available options for the `type` parameter.

```ts
import { redirect, RedirectType } from 'next/navigation'

redirect('/redirect-to', RedirectType.replace)
// or
redirect('/redirect-to', RedirectType.push)
```

The `type` parameter has no effect when used in Server Components.

### Returns

`redirect` does not return a value.

## Behavior

* In Server Actions and Route Handlers, redirect should be called **outside** the `try` block when using `try/catch` statements.
* If you prefer to return a 308 (Permanent) HTTP redirect instead of 307 (Temporary), you can use the [`permanentRedirect` function](/docs/app/api-reference/functions/permanentRedirect.md) instead.
* `redirect` throws an error so it should be called **outside** the `try` block when using `try/catch` statements.
* `redirect` can be called in Client Components during the rendering process but not in event handlers. You can use the [`useRouter` hook](/docs/app/api-reference/functions/use-router.md) instead.
* `redirect` also accepts absolute URLs and can be used to redirect to external links.
* If you'd like to redirect before the render process, use [`next.config.js`](/docs/app/guides/redirecting.md#redirects-in-nextconfigjs) or [Proxy](/docs/app/guides/redirecting.md#nextresponseredirect-in-proxy).

## Example

### Server Component

Invoking the `redirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.

```tsx filename="app/team/[id]/page.tsx" switcher
import { redirect } from 'next/navigation'

async function fetchTeam(id: string) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const team = await fetchTeam(id)

  if (!team) {
    redirect('/login')
  }

  // ...
}
```

```jsx filename="app/team/[id]/page.js" switcher
import { redirect } from 'next/navigation'

async function fetchTeam(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({ params }) {
  const { id } = await params
  const team = await fetchTeam(id)

  if (!team) {
    redirect('/login')
  }

  // ...
}
```

> **Good to know**: `redirect` does not require you to use `return redirect()` as it uses the TypeScript [`never`](https://www.typescriptlang.org/docs/handbook/2/functions.html#never) type.

### Client Component

`redirect` can be directly used in a Client Component.

```tsx filename="components/client-redirect.tsx" switcher
'use client'

import { redirect, usePathname } from 'next/navigation'

export function ClientRedirect() {
  const pathname = usePathname()

  if (pathname.startsWith('/admin') && !pathname.includes('/login')) {
    redirect('/admin/login')
  }

  return <div>Login Page</div>
}
```

```jsx filename="components/client-redirect.jsx" switcher
'use client'

import { redirect, usePathname } from 'next/navigation'

export function ClientRedirect() {
  const pathname = usePathname()

  if (pathname.startsWith('/admin') && !pathname.includes('/login')) {
    redirect('/admin/login')
  }

  return <div>Login Page</div>
}
```

> **Good to know**: When using `redirect` in a Client Component on initial page load during Server-Side Rendering (SSR), it will perform a server-side redirect.

`redirect` can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the [`useRouter`](/docs/app/api-reference/functions/use-router.md) hook.

```tsx filename="app/client-redirect.tsx" switcher
'use client'

import { navigate } from './actions'

export function ClientRedirect() {
  return (
    <form action={navigate}>
      <input type="text" name="id" />
      <button>Submit</button>
    </form>
  )
}
```

```jsx filename="app/client-redirect.jsx" switcher
'use client'

import { navigate } from './actions'

export function ClientRedirect() {
  return (
    <form action={navigate}>
      <input type="text" name="id" />
      <button>Submit</button>
    </form>
  )
}
```

```ts filename="app/actions.ts" switcher
'use server'

import { redirect } from 'next/navigation'

export async function navigate(data: FormData) {
  redirect(`/posts/${data.get('id')}`)
}
```

```js filename="app/actions.js" switcher
'use server'

import { redirect } from 'next/navigation'

export async function navigate(data) {
  redirect(`/posts/${data.get('id')}`)
}
```

## FAQ

### Why does `redirect` use 307 and 308?

When using `redirect()` you may notice that the status codes used are `307` for a temporary redirect, and `308` for a permanent redirect. While traditionally a `302` was used for a temporary redirect, and a `301` for a permanent redirect, many browsers changed the request method of the redirect, from a `POST` to `GET` request when using a `302`, regardless of the origins request method.

Taking the following example of a redirect from `/users` to `/people`, if you make a `POST` request to `/users` to create a new user, and are conforming to a `302` temporary redirect, the request method will be changed from a `POST` to a `GET` request. This doesn't make sense, as to create a new user, you should be making a `POST` request to `/people`, and not a `GET` request.

The introduction of the `307` status code means that the request method is preserved as `POST`.

* `302` - Temporary redirect, will change the request method from `POST` to `GET`
* `307` - Temporary redirect, will preserve the request method as `POST`

The `redirect()` method uses a `307` by default, instead of a `302` temporary redirect, meaning your requests will *always* be preserved as `POST` requests.

[Learn more](https://developer.mozilla.org/docs/Web/HTTP/Redirections) about HTTP Redirects.

## Version History

| Version   | Changes                |
| --------- | ---------------------- |
| `v13.0.0` | `redirect` introduced. |
- [permanentRedirect](/docs/app/api-reference/functions/permanentRedirect.md)
  - API Reference for the permanentRedirect function.


--------------------------------------------------------------------------------
title: "refresh"
description: "API Reference for the refresh function."
source: "https://nextjs.org/docs/app/api-reference/functions/refresh"
--------------------------------------------------------------------------------

# refresh

`refresh` allows you to refresh the client router from within a [Server Action](/docs/app/getting-started/updating-data.md).

## Usage

`refresh` can **only** be called from within Server Actions. It cannot be used in Route Handlers, Client Components, or any other context.

## Parameters

```tsx
refresh(): void;
```

## Returns

`refresh` does not return a value.

## Examples

```ts filename="app/actions.ts" switcher
'use server'

import { refresh } from 'next/cache'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  refresh()
}
```

```js filename="app/actions.js" switcher
'use server'

import { refresh } from 'next/cache'

export async function createPost(formData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  refresh()
}
```

### Error when used outside Server Actions

```ts filename="app/api/posts/route.ts" switcher
import { refresh } from 'next/cache'

export async function POST() {
  // This will throw an error
  refresh()
}
```


--------------------------------------------------------------------------------
title: "revalidatePath"
description: "API Reference for the revalidatePath function."
source: "https://nextjs.org/docs/app/api-reference/functions/revalidatePath"
--------------------------------------------------------------------------------

# revalidatePath

`revalidatePath` allows you to invalidate [cached data](/docs/app/guides/caching.md) on-demand for a specific path.

## Usage

`revalidatePath` can be called in Server Functions and Route Handlers.

`revalidatePath` cannot be called in Client Components or Proxy, as it only works in server environments.

> **Good to know**:
>
> * **Server Functions**: Updates the UI immediately (if viewing the affected path). Currently, it also causes all previously visited pages to refresh when navigated to again. This behavior is temporary and will be updated in the future to apply only to the specific path.
> * **Route Handlers**: Marks the path for revalidation. The revalidation is done on the next visit to the specified path. This means calling `revalidatePath` with a dynamic route segment will not immediately trigger many revalidations at once. The invalidation only happens when the path is next visited.

## Parameters

```tsx
revalidatePath(path: string, type?: 'page' | 'layout'): void;
```

* `path`: Either a route pattern corresponding to the data you want to revalidate, for example `/product/[slug]`, or a specific URL, `/product/123`. Do not append `/page` or `/layout`, use the `type` parameter instead. Must not exceed 1024 characters. This value is case-sensitive.
* `type`: (optional) `'page'` or `'layout'` string to change the type of path to revalidate. If `path` contains a dynamic segment, for example `/product/[slug]`, this parameter is required. If `path` is a specific URL, `/product/1`, omit `type`.

Use a specific URL when you want to refresh a [single page](#revalidating-a-specific-url). Use a route pattern plus `type` to refresh [multiple URLs](#revalidating-a-page-path).

## Returns

`revalidatePath` does not return a value.

## What can be invalidated

The path parameter can point to pages, layouts, or route handlers:

* **Pages**: Invalidates the specific page
* **Layouts**: Invalidates the layout (the `layout.tsx` at that segment), all nested layouts beneath it, and all pages beneath them
* **Route Handlers**: Invalidates Data Cache entries accessed within route handlers. For example `revalidatePath("/api/data")` invalidates this GET handler:

```ts filename="app/api/data/route.ts"
export async function GET() {
  const data = await fetch('https://api.vercel.app/blog', {
    cache: 'force-cache',
  })

  return Response.json(await data.json())
}
```

## Relationship with `revalidateTag` and `updateTag`

`revalidatePath`, [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) and [`updateTag`](/docs/app/api-reference/functions/updateTag.md) serve different purposes:

* **`revalidatePath`**: Invalidates a specific page or layout path
* **`revalidateTag`**: Marks data with specific tags as **stale**. Applies across all pages that use those tags
* **`updateTag`**: Expires data with specific tags. Applies across all pages that use those tags

When you call `revalidatePath`, only the specified path gets fresh data on the next visit. Other pages that use the same data tags will continue to serve cached data until those specific tags are also revalidated:

```tsx
// Page A: /blog
const posts = await fetch('https://api.vercel.app/blog', {
  next: { tags: ['posts'] },
})

// Page B: /dashboard
const recentPosts = await fetch('https://api.vercel.app/blog?limit=5', {
  next: { tags: ['posts'] },
})
```

After calling `revalidatePath('/blog')`:

* **Page A (/blog)**: Shows fresh data (page re-rendered)
* **Page B (/dashboard)**: Still shows stale data (cache tag 'posts' not invalidated)

Learn about the difference between [`revalidateTag` and `updateTag`](/docs/app/api-reference/functions/updateTag.md#differences-from-revalidatetag).

### Building revalidation utilities

`revalidatePath` and `updateTag` are complementary primitives that are often used together in utility functions to ensure comprehensive data consistency across your application:

```ts
'use server'

import { revalidatePath, updateTag } from 'next/cache'

export async function updatePost() {
  await updatePostInDatabase()

  revalidatePath('/blog') // Refresh the blog page
  updateTag('posts') // Refresh all pages using 'posts' tag
}
```

This pattern ensures that both the specific page and any other pages using the same data remain consistent.

## Examples

### Revalidating a specific URL

```ts
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/post-1')
```

This will invalidate one specific URL for revalidation on the next page visit.

### Revalidating a Page path

```ts
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/[slug]', 'page')
// or with route groups
revalidatePath('/(main)/blog/[slug]', 'page')
```

This will invalidate any URL that matches the provided `page` file for revalidation on the next page visit. This will *not* invalidate pages beneath the specific page. For example, `/blog/[slug]` won't invalidate `/blog/[slug]/[author]`.

### Revalidating a Layout path

```ts
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/[slug]', 'layout')
// or with route groups
revalidatePath('/(main)/post/[slug]', 'layout')
```

This will invalidate any URL that matches the provided `layout` file for revalidation on the next page visit. This will cause pages beneath with the same layout to be invalidated and revalidated on the next visit. For example, in the above case, `/blog/[slug]/[another]` would also be invalidated and revalidated on the next visit.

### Revalidating all data

```ts
import { revalidatePath } from 'next/cache'

revalidatePath('/', 'layout')
```

This will purge the Client-side Router Cache, and invalidate the Data Cache for revalidation on the next page visit.

### Server Function

```ts filename="app/actions.ts" switcher
'use server'

import { revalidatePath } from 'next/cache'

export default async function submit() {
  await submitForm()
  revalidatePath('/')
}
```

### Route Handler

```ts filename="app/api/revalidate/route.ts" switcher
import { revalidatePath } from 'next/cache'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const path = request.nextUrl.searchParams.get('path')

  if (path) {
    revalidatePath(path)
    return Response.json({ revalidated: true, now: Date.now() })
  }

  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing path to revalidate',
  })
}
```

```js filename="app/api/revalidate/route.js" switcher
import { revalidatePath } from 'next/cache'

export async function GET(request) {
  const path = request.nextUrl.searchParams.get('path')

  if (path) {
    revalidatePath(path)
    return Response.json({ revalidated: true, now: Date.now() })
  }

  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing path to revalidate',
  })
}
```


--------------------------------------------------------------------------------
title: "revalidateTag"
description: "API Reference for the revalidateTag function."
source: "https://nextjs.org/docs/app/api-reference/functions/revalidateTag"
--------------------------------------------------------------------------------

# revalidateTag

`revalidateTag` allows you to invalidate [cached data](/docs/app/guides/caching.md) on-demand for a specific cache tag.

This function is ideal for content where a slight delay in updates is acceptable, such as blog posts, product catalogs, or documentation. Users receive stale content while fresh data loads in the background.

## Usage

`revalidateTag` can be called in Server Functions and Route Handlers.

`revalidateTag` cannot be called in Client Components or Proxy, as it only works in server environments.

### Revalidation Behavior

The revalidation behavior depends on whether you provide the second argument:

* **With `profile="max"` (recommended)**: The tag entry is marked as stale, and the next time a resource with that tag is visited, it will use stale-while-revalidate semantics. This means the stale content is served while fresh content is fetched in the background.
* **With a custom cache life profile**: For advanced usage, you can specify any cache life profile that your application has defined, allowing for custom revalidation behaviors tailored to your specific caching requirements.
* **Without the second argument (deprecated)**: The tag entry is expired immediately, and the next request to that resource will be a blocking revalidate/cache miss. This behavior is now deprecated, and you should either use `profile="max"` or migrate to [`updateTag`](/docs/app/api-reference/functions/updateTag.md).

> **Good to know**: When using `profile="max"`, `revalidateTag` marks tagged data as stale, but fresh data is only fetched when pages using that tag are next visited. This means calling `revalidateTag` will not immediately trigger many revalidations at once. The invalidation only happens when any page using that tag is next visited.

## Parameters

```ts
revalidateTag(tag: string, profile: string | { expire?: number }): void;
```

* `tag`: A string representing the cache tag associated with the data you want to revalidate. Must not exceed 256 characters. This value is case-sensitive.
* `profile`: A string that specifies the revalidation behavior. The recommended value is `"max"` which provides stale-while-revalidate semantics, or any of the other default or custom profiles defined in [`cacheLife`](/docs/app/api-reference/config/next-config-js/cacheLife.md). Alternatively, you can pass an object with an `expire` property for custom expiration behavior.

Tags must first be assigned to cached data. You can do this in two ways:

* Using the [`next.tags`](/docs/app/guides/caching.md#fetch-optionsnexttags-and-revalidatetag) option with `fetch` for caching external API requests:

```tsx
fetch(url, { next: { tags: ['posts'] } })
```

* Using [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) inside cached functions or components with the `'use cache'` directive:

```tsx
import { cacheTag } from 'next/cache'

async function getData() {
  'use cache'
  cacheTag('posts')
  // ...
}
```

> **Good to know**: The single-argument form `revalidateTag(tag)` is deprecated. It currently works if TypeScript errors are suppressed, but this behavior may be removed in a future version. Update to the two-argument signature.

## Returns

`revalidateTag` does not return a value.

## Relationship with `revalidatePath`

`revalidateTag` invalidates data with specific tags across all pages that use those tags, while [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md) invalidates specific page or layout paths.

> **Good to know**: These functions serve different purposes and may need to be used together for comprehensive data consistency. For detailed examples and considerations, see [relationship with revalidateTag and updateTag](/docs/app/api-reference/functions/revalidatePath.md#relationship-with-revalidatetag-and-updatetag) for more information.

## Examples

The following examples demonstrate how to use `revalidateTag` in different contexts. In both cases, we're using `profile="max"` to mark data as stale and use stale-while-revalidate semantics, which is the recommended approach for most use cases.

### Server Action

```ts filename="app/actions.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('posts', 'max')
}
```

```js filename="app/actions.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('posts', 'max')
}
```

### Route Handler

```ts filename="app/api/revalidate/route.ts" switcher
import type { NextRequest } from 'next/server'
import { revalidateTag } from 'next/cache'

export async function GET(request: NextRequest) {
  const tag = request.nextUrl.searchParams.get('tag')

  if (tag) {
    revalidateTag(tag, 'max')
    return Response.json({ revalidated: true, now: Date.now() })
  }

  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing tag to revalidate',
  })
}
```

```js filename="app/api/revalidate/route.js" switcher
import { revalidateTag } from 'next/cache'

export async function GET(request) {
  const tag = request.nextUrl.searchParams.get('tag')

  if (tag) {
    revalidateTag(tag, 'max')
    return Response.json({ revalidated: true, now: Date.now() })
  }

  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing tag to revalidate',
  })
}
```

> **Good to know**: For webhooks or third-party services that need immediate expiration, you can pass `{ expire: 0 }` as the second argument: `revalidateTag(tag, { expire: 0 })`. This pattern is necessary when external systems call your Route Handlers and require data to expire immediately. For all other cases, it's recommended to use [`updateTag`](/docs/app/api-reference/functions/updateTag.md) in Server Actions for immediate updates instead.


--------------------------------------------------------------------------------
title: "unauthorized"
description: "API Reference for the unauthorized function."
source: "https://nextjs.org/docs/app/api-reference/functions/unauthorized"
--------------------------------------------------------------------------------

# unauthorized

> This feature is currently experimental and subject to change, it is not recommended for production.

The `unauthorized` function throws an error that renders a Next.js 401 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`unauthorized.js` file](/docs/app/api-reference/file-conventions/unauthorized.md).

To start using `unauthorized`, enable the experimental [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts.md) configuration option in your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  experimental: {
    authInterrupts: true,
  },
}
```

`unauthorized` can be invoked in [Server Components](/docs/app/getting-started/server-and-client-components.md), [Server Actions](/docs/app/getting-started/updating-data.md), and [Route Handlers](/docs/app/api-reference/file-conventions/route.md).

```tsx filename="app/dashboard/page.tsx" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  // Render the dashboard for authenticated users
  return (
    <main>
      <h1>Welcome to the Dashboard</h1>
      <p>Hi, {session.user.name}.</p>
    </main>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  // Render the dashboard for authenticated users
  return (
    <main>
      <h1>Welcome to the Dashboard</h1>
      <p>Hi, {session.user.name}.</p>
    </main>
  )
}
```

## Good to know

* The `unauthorized` function cannot be called in the [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout).

## Examples

### Displaying login UI to unauthenticated users

You can use `unauthorized` function to display the `unauthorized.js` file with a login UI.

```tsx filename="app/dashboard/page.tsx" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  return <div>Dashboard</div>
}
```

```jsx filename="app/dashboard/page.js" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  return <div>Dashboard</div>
}
```

```tsx filename="app/unauthorized.tsx" switcher
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

```jsx filename="app/unauthorized.js" switcher
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

### Mutations with Server Actions

You can invoke `unauthorized` in Server Actions to ensure only authenticated users can perform specific mutations.

```ts filename="app/actions/update-profile.ts" switcher
'use server'

import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateProfile(data: FormData) {
  const session = await verifySession()

  // If the user is not authenticated, return a 401
  if (!session) {
    unauthorized()
  }

  // Proceed with mutation
  // ...
}
```

```js filename="app/actions/update-profile.js" switcher
'use server'

import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateProfile(data) {
  const session = await verifySession()

  // If the user is not authenticated, return a 401
  if (!session) {
    unauthorized()
  }

  // Proceed with mutation
  // ...
}
```

### Fetching data with Route Handlers

You can use `unauthorized` in Route Handlers to ensure only authenticated users can access the endpoint.

```tsx filename="app/api/profile/route.ts" switcher
import { NextRequest, NextResponse } from 'next/server'
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export async function GET(req: NextRequest): Promise<NextResponse> {
  // Verify the user's session
  const session = await verifySession()

  // If no session exists, return a 401 and render unauthorized.tsx
  if (!session) {
    unauthorized()
  }

  // Fetch data
  // ...
}
```

```jsx filename="app/api/profile/route.js" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export async function GET() {
  const session = await verifySession()

  // If the user is not authenticated, return a 401 and render unauthorized.tsx
  if (!session) {
    unauthorized()
  }

  // Fetch data
  // ...
}
```

## Version History

| Version   | Changes                    |
| --------- | -------------------------- |
| `v15.1.0` | `unauthorized` introduced. |
- [unauthorized.js](/docs/app/api-reference/file-conventions/unauthorized.md)
  - API reference for the unauthorized.js special file.


--------------------------------------------------------------------------------
title: "unstable_cache"
description: "API Reference for the unstable_cache function."
source: "https://nextjs.org/docs/app/api-reference/functions/unstable_cache"
--------------------------------------------------------------------------------

# unstable_cache

> **Warning:** This API will be replaced by [`use cache`](/docs/app/api-reference/directives/use-cache.md) when it reaches stability.

`unstable_cache` allows you to cache the results of expensive operations, like database queries, and reuse them across multiple requests.

```jsx
import { getUser } from './data';
import { unstable_cache } from 'next/cache';

const getCachedUser = unstable_cache(
  async (id) => getUser(id),
  ['my-app-user']
);

export default async function Component({ userID }) {
  const user = await getCachedUser(userID);
  ...
}
```

> **Good to know**:
>
> * Accessing dynamic data sources such as `headers` or `cookies` inside a cache scope is not supported. If you need this data inside a cached function use `headers` outside of the cached function and pass the required dynamic data in as an argument.
> * This API uses Next.js' built-in [Data Cache](/docs/app/guides/caching.md#data-cache) to persist the result across requests and deployments.

## Parameters

```jsx
const data = unstable_cache(fetchData, keyParts, options)()
```

* `fetchData`: This is an asynchronous function that fetches the data you want to cache. It must be a function that returns a `Promise`.
* `keyParts`: This is an extra array of keys that further adds identification to the cache. By default, `unstable_cache` already uses the arguments and the stringified version of your function as the cache key. It is optional in most cases; the only time you need to use it is when you use external variables without passing them as parameters. However, it is important to add closures used within the function if you do not pass them as parameters.
* `options`: This is an object that controls how the cache behaves. It can contain the following properties:
  * `tags`: An array of tags that can be used to control cache invalidation. Next.js will not use this to uniquely identify the function.
  * `revalidate`: The number of seconds after which the cache should be revalidated. Omit or pass `false` to cache indefinitely or until matching `revalidateTag()` or `revalidatePath()` methods are called.

## Returns

`unstable_cache` returns a function that when invoked, returns a Promise that resolves to the cached data. If the data is not in the cache, the provided function will be invoked, and its result will be cached and returned.

## Example

```tsx filename="app/page.tsx" switcher
import { unstable_cache } from 'next/cache'

export default async function Page({
  params,
}: {
  params: Promise<{ userId: string }>
}) {
  const { userId } = await params
  const getCachedUser = unstable_cache(
    async () => {
      return { id: userId }
    },
    [userId], // add the user ID to the cache key
    {
      tags: ['users'],
      revalidate: 60,
    }
  )

  //...
}
```

```jsx filename="app/page.jsx" switcher
import { unstable_cache } from 'next/cache';

export default async function Page({ params } }) {
  const { userId } = await params
  const getCachedUser = unstable_cache(
    async () => {
      return { id: userId };
    },
    [userId], // add the user ID to the cache key
    {
      tags: ["users"],
      revalidate: 60,
    }
  );

  //...
}
```

## Version History

| Version   | Changes                      |
| --------- | ---------------------------- |
| `v14.0.0` | `unstable_cache` introduced. |


--------------------------------------------------------------------------------
title: "unstable_noStore"
description: "API Reference for the unstable_noStore function."
source: "https://nextjs.org/docs/app/api-reference/functions/unstable_noStore"
--------------------------------------------------------------------------------

# unstable_noStore

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

**In version 15, we recommend using [`connection`](/docs/app/api-reference/functions/connection.md) instead of `unstable_noStore`.**

`unstable_noStore` can be used to declaratively opt out of static rendering and indicate a particular component should not be cached.

```jsx
import { unstable_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

> **Good to know**:
>
> * `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
> * `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per-component basis

* Using `unstable_noStore` inside [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache.md) will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.

## Usage

If you prefer not to pass additional options to `fetch`, like `cache: 'no-store'`, `next: { revalidate: 0 }` or in cases where `fetch` is not available, you can use `noStore()` as a replacement for all of these use cases.

```jsx
import { unstable_noStore as noStore } from 'next/cache';

export default async function ServerComponent() {
  noStore();
  const result = await db.query(...);
  ...
}
```

## Version History

| Version   | Changes                                         |
| --------- | ----------------------------------------------- |
| `v15.0.0` | `unstable_noStore` deprecated for `connection`. |
| `v14.0.0` | `unstable_noStore` introduced.                  |


--------------------------------------------------------------------------------
title: "unstable_rethrow"
description: "API Reference for the unstable_rethrow function."
source: "https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow"
--------------------------------------------------------------------------------

# unstable_rethrow

> This feature is currently unstable and subject to change, it is not recommended for production.

`unstable_rethrow` can be used to avoid catching internal errors thrown by Next.js when attempting to handle errors thrown in your application code.

For example, calling the `notFound` function will throw an internal Next.js error and render the [`not-found.js`](/docs/app/api-reference/file-conventions/not-found.md) component. However, if used inside the `try` block of a `try/catch` statement, the error will be caught, preventing `not-found.js` from rendering:

```tsx filename="@/app/ui/component.tsx"
import { notFound } from 'next/navigation'

export default async function Page() {
  try {
    const post = await fetch('https://.../posts/1').then((res) => {
      if (res.status === 404) notFound()
      if (!res.ok) throw new Error(res.statusText)
      return res.json()
    })
  } catch (err) {
    console.error(err)
  }
}
```

You can use `unstable_rethrow` API to re-throw the internal error and continue with the expected behavior:

```tsx filename="@/app/ui/component.tsx"
import { notFound, unstable_rethrow } from 'next/navigation'

export default async function Page() {
  try {
    const post = await fetch('https://.../posts/1').then((res) => {
      if (res.status === 404) notFound()
      if (!res.ok) throw new Error(res.statusText)
      return res.json()
    })
  } catch (err) {
    unstable_rethrow(err)
    console.error(err)
  }
}
```

The following Next.js APIs rely on throwing an error which should be rethrown and handled by Next.js itself:

* [`notFound()`](/docs/app/api-reference/functions/not-found.md)
* [`redirect()`](/docs/app/guides/redirecting.md#redirect-function)
* [`permanentRedirect()`](/docs/app/guides/redirecting.md#permanentredirect-function)

If a route segment is marked to throw an error unless it's static, a Dynamic API call will also throw an error that should similarly not be caught by the developer. Note that Partial Prerendering (PPR) affects this behavior as well. These APIs are:

* [`cookies`](/docs/app/api-reference/functions/cookies.md)
* [`headers`](/docs/app/api-reference/functions/headers.md)
* [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional)
* `fetch(..., { cache: 'no-store' })`
* `fetch(..., { next: { revalidate: 0 } })`

> **Good to know**:
>
> * This method should be called at the top of the catch block, passing the error object as its only argument. It can also be used within a `.catch` handler of a promise.
> * You may be able to avoid using `unstable_rethrow` if you encapsulate your API calls that throw and let the **caller** handle the exception.
> * Only use `unstable_rethrow` if your caught exceptions may include both application errors and framework-controlled exceptions (like `redirect()` or `notFound()`).
> * Any resource cleanup (like clearing intervals, timers, etc) would have to either happen prior to the call to `unstable_rethrow` or within a `finally` block.


--------------------------------------------------------------------------------
title: "updateTag"
description: "API Reference for the updateTag function."
source: "https://nextjs.org/docs/app/api-reference/functions/updateTag"
--------------------------------------------------------------------------------

# updateTag

`updateTag` allows you to update [cached data](/docs/app/guides/caching.md) on-demand for a specific cache tag from within [Server Actions](/docs/app/getting-started/updating-data.md).

This function is designed for **read-your-own-writes** scenarios, where a user makes a change (like creating a post), and the UI immediately shows the change, rather than stale data.

## Usage

`updateTag` can **only** be called from within [Server Actions](/docs/app/getting-started/updating-data.md). It cannot be used in Route Handlers, Client Components, or any other context.

If you need to invalidate cache tags in Route Handlers or other contexts, use [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) instead.

> **Good to know**: `updateTag` immediately expires the cached data for the specified tag. The next request will wait to fetch fresh data rather than serving stale content from the cache, ensuring users see their changes immediately.

## Parameters

```tsx
updateTag(tag: string): void;
```

* `tag`: A string representing the cache tag associated with the data you want to update. Must not exceed 256 characters. This value is case-sensitive.

Tags must first be assigned to cached data. You can do this in two ways:

* Using the [`next.tags`](/docs/app/guides/caching.md#fetch-optionsnexttags-and-revalidatetag) option with `fetch` for caching external API requests:

```tsx
fetch(url, { next: { tags: ['posts'] } })
```

* Using [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) inside cached functions or components with the `'use cache'` directive:

```tsx
import { cacheTag } from 'next/cache'

async function getData() {
  'use cache'
  cacheTag('posts')
  // ...
}
```

## Returns

`updateTag` does not return a value.

## Differences from revalidateTag

While both `updateTag` and `revalidateTag` invalidate cached data, they serve different purposes:

* **`updateTag`**:
  * Can only be used in Server Actions
  * Next request waits for fresh data (no stale content served)
  * Designed for read-your-own-writes scenarios

* **`revalidateTag`**:
  * Can be used in Server Actions and Route Handlers
  * With `profile="max"` (recommended): Serves cached data while fetching fresh data in the background (stale-while-revalidate)
  * With custom profile: Can be configured to any cache life profile for advanced usage
  * Without profile: legacy behavior which is equivalent to `updateTag`

## Examples

### Server Action with Read-Your-Own-Writes

```ts filename="app/actions.ts" switcher
'use server'

import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  // Invalidate cache tags so the new post is immediately visible
  // 'posts' tag: affects any page that displays a list of posts
  updateTag('posts')
  // 'post-{id}' tag: affects the individual post detail page
  updateTag(`post-${post.id}`)

  // Redirect to the new post - user will see fresh data, not cached
  redirect(`/posts/${post.id}`)
}
```

```js filename="app/actions.js" switcher
'use server'

import { updateTag } from 'next/cache'
import { redirect } from 'next/navigation'

export async function createPost(formData) {
  const title = formData.get('title')
  const content = formData.get('content')

  // Create the post in your database
  const post = await db.post.create({
    data: { title, content },
  })

  // Invalidate cache tags so the new post is immediately visible
  // 'posts' tag: affects any page that displays a list of posts
  updateTag('posts')
  // 'post-{id}' tag: affects the individual post detail page
  updateTag(`post-${post.id}`)

  // Redirect to the new post - user will see fresh data, not cached
  redirect(`/posts/${post.id}`)
}
```

### Error when used outside Server Actions

```ts filename="app/api/posts/route.ts" switcher
import { updateTag } from 'next/cache'

export async function POST() {
  // This will throw an error
  updateTag('posts')
  // Error: updateTag can only be called from within a Server Action

  // Use revalidateTag instead in Route Handlers
  revalidateTag('posts', 'max')
}
```

## When to use updateTag

Use `updateTag` when:

* You're in a Server Action
* You need immediate cache invalidation for read-your-own-writes
* You want to ensure the next request sees updated data

Use `revalidateTag` instead when:

* You're in a Route Handler or other non-action context
* You want stale-while-revalidate semantics
* You're building a webhook or API endpoint for cache invalidation

## Related

* [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) - For invalidating tags in Route Handlers
* [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md) - For invalidating specific paths


--------------------------------------------------------------------------------
title: "useLinkStatus"
description: "API Reference for the useLinkStatus hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-link-status"
--------------------------------------------------------------------------------

# useLinkStatus

The `useLinkStatus` hook lets you track the **pending** state of a `<Link>`. Use it for subtle, inline feedback, for example a shimmer effect over the clicked link, while navigation completes. Prefer route-level fallbacks with `loading.js`, and prefetching for instant transitions.

`useLinkStatus` is useful when:

* [Prefetching](/docs/app/getting-started/linking-and-navigating.md#prefetching) is disabled or in progress meaning navigation is blocked.
* The destination route is dynamic **and** doesn't include a [`loading.js`](/docs/app/api-reference/file-conventions/loading.md) file that would allow an instant navigation.

```tsx filename="app/hint.tsx" switcher
'use client'

import Link from 'next/link'
import { useLinkStatus } from 'next/link'

function Hint() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}

export default function Header() {
  return (
    <header>
      <Link href="/dashboard" prefetch={false}>
        <span className="label">Dashboard</span> <Hint />
      </Link>
    </header>
  )
}
```

```jsx filename="app/hint.js" switcher
'use client'

import Link from 'next/link'
import { useLinkStatus } from 'next/link'

function Hint() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}

export default function Header() {
  return (
    <header>
      <Link href="/dashboard" prefetch={false}>
        <span className="label">Dashboard</span> <Hint />
      </Link>
    </header>
  )
}
```

> **Good to know**:
>
> * `useLinkStatus` must be used within a descendant component of a `Link` component
> * The hook is most useful when `prefetch={false}` is set on the `Link` component
> * If the linked route has been prefetched, the pending state will be skipped
> * When clicking multiple links in quick succession, only the last link's pending state is shown
> * This hook is not supported in the Pages Router and always returns `{ pending: false }`
> * Inline indicators can easily introduce layout shifts. Prefer a fixed-size, always-rendered hint element and toggle its opacity, or use an animation.

## You might not need `useLinkStatus`

Before adding inline feedback, consider if:

* The destination is static and prefetched in production, so the pending phase may be skipped.
* The route has a `loading.js` file, enabling instant transitions with a route-level fallback.

Navigation is typically fast. Use `useLinkStatus` as a quick patch when you identify a slow transition, then iterate to fix the root cause with prefetching or a `loading.js` fallback.

## Parameters

```tsx
const { pending } = useLinkStatus()
```

`useLinkStatus` does not take any parameters.

## Returns

`useLinkStatus` returns an object with a single property:

| Property | Type    | Description                                  |
| -------- | ------- | -------------------------------------------- |
| pending  | boolean | `true` before history updates, `false` after |

## Example

### Inline link hint

Add a subtle, fixed-size hint that doesn’t affect layout to confirm a click when prefetching hasn’t completed.

```tsx filename="app/components/loading-indicator.tsx" switcher
'use client'

import { useLinkStatus } from 'next/link'

export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

```jsx filename="app/components/loading-indicator.js" switcher
'use client'

import { useLinkStatus } from 'next/link'

export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

```tsx filename="app/shop/layout.tsx" switcher
import Link from 'next/link'
import LoadingIndicator from './components/loading-indicator'

const links = [
  { href: '/shop/electronics', label: 'Electronics' },
  { href: '/shop/clothing', label: 'Clothing' },
  { href: '/shop/books', label: 'Books' },
]

function Menubar() {
  return (
    <div>
      {links.map((link) => (
        <Link key={link.label} href={link.href}>
          <span className="label">{link.label}</span> <LoadingIndicator />
        </Link>
      ))}
    </div>
  )
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <Menubar />
      {children}
    </div>
  )
}
```

```jsx filename="app/shop/layout.js" switcher
import Link from 'next/link'
import LoadingIndicator from './components/loading-indicator'

const links = [
  { href: '/shop/electronics', label: 'Electronics' },
  { href: '/shop/clothing', label: 'Clothing' },
  { href: '/shop/books', label: 'Books' },
]

function Menubar() {
  return (
    <div>
      {links.map((link) => (
        <Link key={link.label} href={link.href}>
          <span className="label">{link.label}</span> <LoadingIndicator />
        </Link>
      ))}
    </div>
  )
}

export default function Layout({ children }) {
  return (
    <div>
      <Menubar />
      {children}
    </div>
  )
}
```

## Gracefully handling fast navigation

If the navigation to a new route is fast, users may see an unnecessary flash of the hint. One way to improve the user experience and only show the hint when the navigation takes time to complete is to add an initial animation delay (e.g. 100ms) and start the animation as invisible (e.g. `opacity: 0`).

```css filename="app/styles/global.css"
.link-hint {
  display: inline-block;
  width: 0.6em;
  height: 0.6em;
  margin-left: 0.25rem;
  border-radius: 9999px;
  background: currentColor;
  opacity: 0;
  visibility: hidden; /* reserve space without showing the hint */
}

.link-hint.is-pending {
  /* Animation 1: fade in after 100ms and keep final opacity */
  /* Animation 2: subtle pulsing while pending */
  visibility: visible;
  animation-name: fadeIn, pulse;
  animation-duration: 200ms, 1s;
  /* Appear only if navigation actually takes time */
  animation-delay: 100ms, 100ms;
  animation-timing-function: ease, ease-in-out;
  animation-iteration-count: 1, infinite;
  animation-fill-mode: forwards, none;
}

@keyframes fadeIn {
  to {
    opacity: 0.35;
  }
}
@keyframes pulse {
  50% {
    opacity: 0.15;
  }
}
```

## Version History

| Version   | Changes                     |
| --------- | --------------------------- |
| `v15.3.0` | `useLinkStatus` introduced. |
## Next Steps

Learn more about the features mentioned in this page by reading the API Reference.

- [Link Component](/docs/app/api-reference/components/link.md)
  - Enable fast client-side navigation with the built-in `next/link` component.
- [loading.js](/docs/app/api-reference/file-conventions/loading.md)
  - API reference for the loading.js file.


--------------------------------------------------------------------------------
title: "useParams"
description: "API Reference for the useParams hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-params"
--------------------------------------------------------------------------------

# useParams

`useParams` is a **Client Component** hook that lets you read a route's [dynamic params](/docs/app/api-reference/file-conventions/dynamic-routes.md) filled in by the current URL.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const params = useParams<{ tag: string; item: string }>()

  // Route -> /shop/[tag]/[item]
  // URL -> /shop/shoes/nike-air-max-97
  // `params` -> { tag: 'shoes', item: 'nike-air-max-97' }
  console.log(params)

  return '...'
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const params = useParams()

  // Route -> /shop/[tag]/[item]
  // URL -> /shop/shoes/nike-air-max-97
  // `params` -> { tag: 'shoes', item: 'nike-air-max-97' }
  console.log(params)

  return '...'
}
```

## Parameters

```tsx
const params = useParams()
```

`useParams` does not take any parameters.

## Returns

`useParams` returns an object containing the current route's filled in [dynamic parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md).

* Each property in the object is an active dynamic segment.
* The properties name is the segment's name, and the properties value is what the segment is filled in with.
* The properties value will either be a `string` or array of `string`'s depending on the [type of dynamic segment](/docs/app/api-reference/file-conventions/dynamic-routes.md).
* If the route contains no dynamic parameters, `useParams` returns an empty object.
* If used in Pages Router, `useParams` will return `null` on the initial render and updates with properties following the rules above once the router is ready.

For example:

| Route                           | URL         | `useParams()`             |
| ------------------------------- | ----------- | ------------------------- |
| `app/shop/page.js`              | `/shop`     | `{}`                      |
| `app/shop/[slug]/page.js`       | `/shop/1`   | `{ slug: '1' }`           |
| `app/shop/[tag]/[item]/page.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |
| `app/shop/[...slug]/page.js`    | `/shop/1/2` | `{ slug: ['1', '2'] }`    |

## Version History

| Version   | Changes                 |
| --------- | ----------------------- |
| `v13.3.0` | `useParams` introduced. |


--------------------------------------------------------------------------------
title: "usePathname"
description: "API Reference for the usePathname hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-pathname"
--------------------------------------------------------------------------------

# usePathname

`usePathname` is a **Client Component** hook that lets you read the current URL's **pathname**.

> **Good to know**: When [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) is enabled `usePathname` may require a `Suspense` boundary around it if your route has a dynamic param. If you use `generateStaticParams` the `Suspense` boundary is optional

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { usePathname } from 'next/navigation'

export default function ExampleClientComponent() {
  const pathname = usePathname()
  return <p>Current pathname: {pathname}</p>
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { usePathname } from 'next/navigation'

export default function ExampleClientComponent() {
  const pathname = usePathname()
  return <p>Current pathname: {pathname}</p>
}
```

`usePathname` intentionally requires using a [Client Component](/docs/app/getting-started/server-and-client-components.md). It's important to note Client Components are not a de-optimization. They are an integral part of the [Server Components](/docs/app/getting-started/server-and-client-components.md) architecture.

For example, a Client Component with `usePathname` will be rendered into HTML on the initial page load. When navigating to a new route, this component does not need to be re-fetched. Instead, the component is downloaded once (in the client JavaScript bundle), and re-renders based on the current state.

> **Good to know**:
>
> * Reading the current URL from a [Server Component](/docs/app/getting-started/server-and-client-components.md) is not supported. This design is intentional to support layout state being preserved across page navigations.
> * If your page is being statically pre-rendered and your app has [rewrites](/docs/app/api-reference/config/next-config-js/rewrites.md) in `next.config` or a [Proxy](/docs/app/api-reference/file-conventions/proxy.md) file, reading the pathname with `usePathname()` can result in hydration mismatch errors—because the initial value comes from the server and may not match the actual browser pathname after routing. See our [example](#avoid-hydration-mismatch-with-rewrites) for a way to mitigate this issue.

<details>
<summary>Compatibility with Pages Router</summary>

If you have components that use `usePathname` and they are imported into routes within the Pages Router, be aware that `usePathname` may return `null` if the router is not yet initialized. This can occur in cases such as [fallback routes](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true) or during [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/static#automatic-static-optimization) in the Pages Router.

To enhance compatibility between routing systems, if your project contains both an `app` and a `pages` directory, Next.js will automatically adjust the return type of `usePathname`.

</details>

## Parameters

```tsx
const pathname = usePathname()
```

`usePathname` does not take any parameters.

## Returns

`usePathname` returns a string of the current URL's pathname. For example:

| URL                 | Returned value        |
| ------------------- | --------------------- |
| `/`                 | `'/'`                 |
| `/dashboard`        | `'/dashboard'`        |
| `/dashboard?v=2`    | `'/dashboard'`        |
| `/blog/hello-world` | `'/blog/hello-world'` |

## Examples

### Do something in response to a route change

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'

function ExampleClientComponent() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
  useEffect(() => {
    // Do something here...
  }, [pathname, searchParams])
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'

function ExampleClientComponent() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
  useEffect(() => {
    // Do something here...
  }, [pathname, searchParams])
}
```

### Avoid hydration mismatch with rewrites

When a page is pre-rendered, the HTML is generated for the source pathname. If the page is then reached through a rewrite using `next.config` or `Proxy`, the browser URL may differ, and `usePathname()` will read the rewritten pathname on the client.

To avoid hydration mismatches, design the UI so that only a small, isolated part depends on the client pathname. Render a stable fallback on the server and update that part after mount.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useEffect, useState } from 'react'
import { usePathname } from 'next/navigation'

export default function PathnameBadge() {
  const pathname = usePathname()
  const [clientPathname, setClientPathname] = useState('')

  useEffect(() => {
    setClientPathname(pathname)
  }, [pathname])

  return (
    <p>
      Current pathname: <span>{clientPathname}</span>
    </p>
  )
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useEffect, useState } from 'react'
import { usePathname } from 'next/navigation'

export default function PathnameBadge() {
  const pathname = usePathname()
  const [clientPathname, setClientPathname] = useState('')

  useEffect(() => {
    setClientPathname(pathname)
  }, [pathname])

  return (
    <p>
      Current pathname: <span>{clientPathname}</span>
    </p>
  )
}
```

| Version   | Changes                   |
| --------- | ------------------------- |
| `v13.0.0` | `usePathname` introduced. |


--------------------------------------------------------------------------------
title: "useReportWebVitals"
description: "API Reference for the useReportWebVitals function."
source: "https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals"
--------------------------------------------------------------------------------

# useReportWebVitals

The `useReportWebVitals` hook allows you to report [Core Web Vitals](https://web.dev/vitals/), and can be used in combination with your analytics service.

New functions passed to `useReportWebVitals` are called with the available metrics up to that point. To prevent reporting duplicated data, ensure that the callback function reference does not change (as shown in the code examples below).

```jsx filename="app/_components/web-vitals.js"
'use client'

import { useReportWebVitals } from 'next/web-vitals'

const logWebVitals = (metric) => {
  console.log(metric)
}

export function WebVitals() {
  useReportWebVitals(logWebVitals)

  return null
}
```

```jsx filename="app/layout.js"
import { WebVitals } from './_components/web-vitals'

export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  )
}
```

> Since the `useReportWebVitals` hook requires the `'use client'` directive, the most performant approach is to create a separate component that the root layout imports. This confines the client boundary exclusively to the `WebVitals` component.

## useReportWebVitals

The `metric` object passed as the hook's argument consists of a number of properties:

* `id`: Unique identifier for the metric in the context of the current page load
* `name`: The name of the performance metric. Possible values include names of [Web Vitals](#web-vitals) metrics (TTFB, FCP, LCP, FID, CLS) specific to a web application.
* `delta`: The difference between the current value and the previous value of the metric. The value is typically in milliseconds and represents the change in the metric's value over time.
* `entries`: An array of [Performance Entries](https://developer.mozilla.org/docs/Web/API/PerformanceEntry) associated with the metric. These entries provide detailed information about the performance events related to the metric.
* `navigationType`: Indicates the [type of navigation](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming/type) that triggered the metric collection. Possible values include `"navigate"`, `"reload"`, `"back_forward"`, and `"prerender"`.
* `rating`: A qualitative rating of the metric value, providing an assessment of the performance. Possible values are `"good"`, `"needs-improvement"`, and `"poor"`. The rating is typically determined by comparing the metric value against predefined thresholds that indicate acceptable or suboptimal performance.
* `value`: The actual value or duration of the performance entry, typically in milliseconds. The value provides a quantitative measure of the performance aspect being tracked by the metric. The source of the value depends on the specific metric being measured and can come from various [Performance API](https://developer.mozilla.org/docs/Web/API/Performance_API)s.

## Web Vitals

[Web Vitals](https://web.dev/vitals/) are a set of useful metrics that aim to capture the user
experience of a web page. The following web vitals are all included:

* [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
* [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
* [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
* [First Input Delay](https://web.dev/fid/) (FID)
* [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
* [Interaction to Next Paint](https://web.dev/inp/) (INP)

You can handle all the results of these metrics using the `name` property.

```tsx filename="app/components/web-vitals.tsx" switcher
'use client'

import { useReportWebVitals } from 'next/web-vitals'

type ReportWebVitalsCallback = Parameters<typeof useReportWebVitals>[0]

const handleWebVitals: ReportWebVitalsCallback = (metric) => {
  switch (metric.name) {
    case 'FCP': {
      // handle FCP results
    }
    case 'LCP': {
      // handle LCP results
    }
    // ...
  }
}

export function WebVitals() {
  useReportWebVitals(handleWebVitals)
}
```

```jsx filename="app/components/web-vitals.js" switcher
'use client'

import { useReportWebVitals } from 'next/web-vitals'

const handleWebVitals = (metric) => {
  switch (metric.name) {
    case 'FCP': {
      // handle FCP results
    }
    case 'LCP': {
      // handle LCP results
    }
    // ...
  }
}

export function WebVitals() {
  useReportWebVitals(handleWebVitals)
}
```

## Sending results to external systems

You can send results to any endpoint to measure and track
real user performance on your site. For example:

```js
function postWebVitals(metrics) {
  const body = JSON.stringify(metric)
  const url = 'https://example.com/analytics'

  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url, body)
  } else {
    fetch(url, { body, method: 'POST', keepalive: true })
  }
}

useReportWebVitals(postWebVitals)
```

> **Good to know**: If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the
> `id` value can allow you to construct metric distributions manually (to calculate percentiles,
> etc.)

> ```js
> useReportWebVitals(metric => {
>   // Use `window.gtag` if you initialized Google Analytics as this example:
>   // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>   window.gtag('event', metric.name, {
>     value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value), // values must be integers
>     event_label: metric.id, // id unique to current page load
>     non_interaction: true, // avoids affecting bounce rate.
>   });
> }
> ```
>
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).


--------------------------------------------------------------------------------
title: "useRouter"
description: "API reference for the useRouter hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-router"
--------------------------------------------------------------------------------

# useRouter

The `useRouter` hook allows you to programmatically change routes inside [Client Components](/docs/app/getting-started/server-and-client-components.md).

> **Recommendation:** Use the [`<Link>` component](/docs/app/api-reference/components/link.md) for navigation unless you have a specific requirement for using `useRouter`.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

## `useRouter()`

* `router.push(href: string, { scroll: boolean })`: Perform a client-side navigation to the provided route. Adds a new entry into the [browser's history stack](https://developer.mozilla.org/docs/Web/API/History_API).
* `router.replace(href: string, { scroll: boolean })`: Perform a client-side navigation to the provided route without adding a new entry into the browser’s history stack.
* `router.refresh()`: Refresh the current route. Making a new request to the server, re-fetching data requests, and re-rendering Server Components. The client will merge the updated React Server Component payload without losing unaffected client-side React (e.g. `useState`) or browser state (e.g. scroll position).
* `router.prefetch(href: string, options?: { onInvalidate?: () => void })`: [Prefetch](/docs/app/getting-started/linking-and-navigating.md#prefetching) the provided route for faster client-side transitions. The optional `onInvalidate` callback is called when the [prefetched data becomes stale](/docs/app/guides/prefetching.md#extending-or-ejecting-link).
* `router.back()`: Navigate back to the previous route in the browser’s history stack.
* `router.forward()`: Navigate forwards to the next page in the browser’s history stack.

> **Good to know**:
>
> * You must not send untrusted or unsanitized URLs to `router.push` or `router.replace`, as this can open your site to cross-site scripting (XSS) vulnerabilities. For example, `javascript:` URLs sent to `router.push` or `router.replace` will be executed in the context of your page.
> * The `<Link>` component automatically prefetch routes as they become visible in the viewport.
> * `refresh()` could re-produce the same result if fetch requests are cached. Other Dynamic APIs like `cookies` and `headers` could also change the response.
> * The `onInvalidate` callback is called at most once per prefetch request. It signals when you may want to trigger a new prefetch for updated route data.

### Migrating from `next/router`

* The `useRouter` hook should be imported from `next/navigation` and not `next/router` when using the App Router
* The `pathname` string has been removed and is replaced by [`usePathname()`](/docs/app/api-reference/functions/use-pathname.md)
* The `query` object has been removed and is replaced by [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md)
* `router.events` has been replaced. [See below.](#router-events)

[View the full migration guide](/docs/app/guides/migrating/app-router-migration.md).

## Examples

### Router events

You can listen for page changes by composing other Client Component hooks like `usePathname` and `useSearchParams`.

```jsx filename="app/components/navigation-events.js"
'use client'

import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'

export function NavigationEvents() {
  const pathname = usePathname()
  const searchParams = useSearchParams()

  useEffect(() => {
    const url = `${pathname}?${searchParams}`
    console.log(url)
    // You can now use the current URL
    // ...
  }, [pathname, searchParams])

  return '...'
}
```

Which can be imported into a layout.

```jsx filename="app/layout.js" highlight={2,10-12}
import { Suspense } from 'react'
import { NavigationEvents } from './components/navigation-events'

export default function Layout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}

        <Suspense fallback={null}>
          <NavigationEvents />
        </Suspense>
      </body>
    </html>
  )
}
```

> **Good to know**: `<NavigationEvents>` is wrapped in a [`Suspense` boundary](/docs/app/api-reference/file-conventions/loading.md#examples) because[`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md) causes client-side rendering up to the closest `Suspense` boundary during [static rendering](/docs/app/guides/caching.md#static-rendering). [Learn more](/docs/app/api-reference/functions/use-search-params.md#behavior).

### Disabling scroll to top

By default, Next.js will scroll to the top of the page when navigating to a new route. You can disable this behavior by passing `scroll: false` to `router.push()` or `router.replace()`.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button
      type="button"
      onClick={() => router.push('/dashboard', { scroll: false })}
    >
      Dashboard
    </button>
  )
}
```

```jsx filename="app/example-client-component.jsx" switcher
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button
      type="button"
      onClick={() => router.push('/dashboard', { scroll: false })}
    >
      Dashboard
    </button>
  )
}
```

## Version History

| Version   | Changes                                                           |
| --------- | ----------------------------------------------------------------- |
| `v15.4.0` | Optional `onInvalidate` callback for `router.prefetch` introduced |
| `v13.0.0` | `useRouter` from `next/navigation` introduced.                    |


--------------------------------------------------------------------------------
title: "useSearchParams"
description: "API Reference for the useSearchParams hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-search-params"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./08-routejs.md) | [Index](./index.md) | [Next →](./10-usesearchparams.md)
