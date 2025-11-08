**Navigation:** [← Previous](./01-nextjs-documentation.md) | [Index](./index.md) | [Next →](./03-content-security-policy.md)

---

# Image Optimization

The Next.js [`<Image>`](/docs/app/api-reference/components/image.md) component extends the HTML `<img>` element to provide:

* **Size optimization:** Automatically serving correctly sized images for each device, using modern image formats like WebP.
* **Visual stability:** Preventing [layout shift](https://web.dev/articles/cls) automatically when images are loading.
* **Faster page loads:** Only loading images when they enter the viewport using native browser lazy loading, with optional blur-up placeholders.
* **Asset flexibility:** Resizing images on-demand, even images stored on remote servers.

To start using `<Image>`, import it from `next/image` and render it within your component.

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="" alt="" />
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="" alt="" />
}
```

The `src` property can be a [local](#local-images) or [remote](#remote-images) image.

> **🎥 Watch:** Learn more about how to use `next/image` → [YouTube (9 minutes)](https://youtu.be/IU_qq_c_lKA).

## Local images

You can store static files, like images and fonts, under a folder called [`public`](/docs/app/api-reference/file-conventions/public-folder.md) in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

![Folder structure showing app and public folders](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/public-folder.png)

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

If the image is statically imported, Next.js will automatically determine the intrinsic [`width`](/docs/app/api-reference/components/image.md#width-and-height) and [`height`](/docs/app/api-reference/components/image.md#width-and-height). These values are used to determine the image ratio and prevent [Cumulative Layout Shift](https://web.dev/articles/cls) while your image is loading.

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'
import ProfileImage from './profile.png'

export default function Page() {
  return (
    <Image
      src={ProfileImage}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'
import ProfileImage from './profile.png'

export default function Page() {
  return (
    <Image
      src={ProfileImage}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}
```

## Remote images

To use a remote image, you can provide a URL string for the `src` property.

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="https://s3.amazonaws.com/my-bucket/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="https://s3.amazonaws.com/my-bucket/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

Since Next.js does not have access to remote files during the build process, you'll need to provide the [`width`](/docs/app/api-reference/components/image.md#width-and-height), [`height`](/docs/app/api-reference/components/image.md#width-and-height) and optional [`blurDataURL`](/docs/app/api-reference/components/image.md#blurdataurl) props manually. The `width` and `height` are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. Alternatively, you can use the [`fill` property](/docs/app/api-reference/components/image.md#fill) to make the image fill the size of the parent element.

To safely allow images from remote servers, you need to define a list of supported URL patterns in [`next.config.js`](/docs/app/api-reference/config/next-config-js.md). Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const config: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 's3.amazonaws.com',
        port: '',
        pathname: '/my-bucket/**',
        search: '',
      },
    ],
  },
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 's3.amazonaws.com',
        port: '',
        pathname: '/my-bucket/**',
        search: '',
      },
    ],
  },
}
```
## API Reference

See the API Reference for the full feature set of Next.js Image.

- [Image Component](/docs/app/api-reference/components/image.md)
  - Optimize Images in your Next.js Application using the built-in `next/image` Component.


--------------------------------------------------------------------------------
title: "Font Optimization"
description: "Learn how to optimize fonts in Next.js"
source: "https://nextjs.org/docs/app/getting-started/fonts"
--------------------------------------------------------------------------------

# Font Optimization

The [`next/font`](/docs/app/api-reference/components/font.md) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.

To start using `next/font`, import it from [`next/font/local`](#local-fonts) or [`next/font/google`](#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example:

```tsx filename="app/layout.tsx" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }) {
  return (
    <html className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

Fonts are scoped to the component they're used in. To apply a font to your entire application, add it to the [Root Layout](/docs/app/api-reference/file-conventions/layout.md#root-layout).

## Google fonts

You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from `next/font/google`:

```tsx filename="app/layout.tsx" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:

```tsx filename="app/layout.tsx" highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js"  highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

## Local fonts

To use a local font, import your font from `next/font/local` and specify the [`src`](/docs/app/api-reference/components/font.md#src) of your local font file. Fonts can be stored in the [`public`](/docs/app/api-reference/file-conventions/public-folder.md) folder or co-located inside the `app` folder. For example:

```tsx filename="app/layout.tsx" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

If you want to use multiple files for a single font family, `src` can be an array:

```js
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
})
```
## API Reference

See the API Reference for the full feature set of Next.js Font

- [Font](/docs/app/api-reference/components/font.md)
  - Optimizing loading web fonts with the built-in `next/font` loaders.


--------------------------------------------------------------------------------
title: "Metadata and OG images"
description: "Learn how to add metadata to your pages and create dynamic OG images."
source: "https://nextjs.org/docs/app/getting-started/metadata-and-og-images"
--------------------------------------------------------------------------------

# Metadata and OG images

The Metadata APIs can be used to define your application metadata for improved SEO and web shareability and include:

1. [The static `metadata` object](#static-metadata)
2. [The dynamic `generateMetadata` function](#generated-metadata)
3. Special [file conventions](/docs/app/api-reference/file-conventions/metadata.md) that can be used to add static or dynamically generated [favicons](#favicons) and [OG images](#static-open-graph-images).

With all the options above, Next.js will automatically generate the relevant `<head>` tags for your page, which can be inspected in the browser's developer tools.

The `metadata` object and `generateMetadata` function exports are only supported in Server Components.

## Default fields

There are two default `meta` tags that are always added even if a route doesn't define metadata:

* The [meta charset tag](https://developer.mozilla.org/docs/Web/HTML/Element/meta#attr-charset) sets the character encoding for the website.
* The [meta viewport tag](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag) sets the viewport width and scale for the website to adjust for different devices.

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

The other metadata fields can be defined with the `Metadata` object (for [static metadata](#static-metadata)) or the `generateMetadata` function (for [generated metadata](#generated-metadata)).

## Static metadata

To define static metadata, export a [`Metadata` object](/docs/app/api-reference/functions/generate-metadata.md#metadata-object) from a static [`layout.js`](/docs/app/api-reference/file-conventions/layout.md) or [`page.js`](/docs/app/api-reference/file-conventions/page.md) file. For example, to add a title and description to the blog route:

```tsx filename="app/blog/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My Blog',
  description: '...',
}

export default function Layout() {}
```

```jsx filename="app/blog/layout.js" switcher
export const metadata = {
  title: 'My Blog',
  description: '...',
}

export default function Layout() {}
```

You can view a full list of available options, in the [`generateMetadata` documentation](/docs/app/api-reference/functions/generate-metadata.md#metadata-fields).

## Generated metadata

You can use [`generateMetadata`](/docs/app/api-reference/functions/generate-metadata.md) function to `fetch` metadata that depends on data. For example, to fetch the title and description for a specific blog post:

```tsx filename="app/blog/[slug]/page.tsx" switcher
import type { Metadata, ResolvingMetadata } from 'next'

type Props = {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}

export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  const slug = (await params).slug

  // fetch post information
  const post = await fetch(`https://api.vercel.app/blog/${slug}`).then((res) =>
    res.json()
  )

  return {
    title: post.title,
    description: post.description,
  }
}

export default function Page({ params, searchParams }: Props) {}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export async function generateMetadata({ params, searchParams }, parent) {
  const slug = (await params).slug

  // fetch post information
  const post = await fetch(`https://api.vercel.app/blog/${slug}`).then((res) =>
    res.json()
  )

  return {
    title: post.title,
    description: post.description,
  }
}

export default function Page({ params, searchParams }) {}
```

### Streaming metadata

For dynamically rendered pages, Next.js streams metadata separately, injecting it into the HTML once `generateMetadata` resolves, without blocking UI rendering.

Streaming metadata improves perceived performance by allowing visual content to stream first.

Streaming metadata is **disabled for bots and crawlers** that expect metadata to be in the `<head>` tag (e.g. `Twitterbot`, `Slackbot`, `Bingbot`). These are detected by using the User Agent header from the incoming request.

You can customize or **disable** streaming metadata completely, with the [`htmlLimitedBots`](/docs/app/api-reference/config/next-config-js/htmlLimitedBots.md#disabling) option in your Next.js config file.

Statically rendered pages don’t use streaming since metadata is resolved at build time.

Learn more about [streaming metadata](/docs/app/api-reference/functions/generate-metadata.md#streaming-metadata).

### Memoizing data requests

There may be cases where you need to fetch the **same** data for metadata and the page itself. To avoid duplicate requests, you can use React's [`cache` function](https://react.dev/reference/react/cache) to memoize the return value and only fetch the data once. For example, to fetch the blog post information for both the metadata and the page:

```ts filename="app/lib/data.ts" highlight={5} switcher
import { cache } from 'react'
import { db } from '@/app/lib/db'

// getPost will be used twice, but execute only once
export const getPost = cache(async (slug: string) => {
  const res = await db.query.posts.findFirst({ where: eq(posts.slug, slug) })
  return res
})
```

```js filename="app/lib/data.js" highlight={5} switcher
import { cache } from 'react'
import { db } from '@/app/lib/db'

// getPost will be used twice, but execute only once
export const getPost = cache(async (slug) => {
  const res = await db.query.posts.findFirst({ where: eq(posts.slug, slug) })
  return res
})
```

```tsx filename="app/blog/[slug]/page.tsx" switcher
import { getPost } from '@/app/lib/data'

export async function generateMetadata({
  params,
}: {
  params: { slug: string }
}) {
  const post = await getPost(params.slug)
  return {
    title: post.title,
    description: post.description,
  }
}

export default async function Page({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)
  return <div>{post.title}</div>
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
import { getPost } from '@/app/lib/data'

export async function generateMetadata({ params }) {
  const post = await getPost(params.slug)
  return {
    title: post.title,
    description: post.description,
  }
}

export default async function Page({ params }) {
  const post = await getPost(params.slug)
  return <div>{post.title}</div>
}
```

## File-based metadata

The following special files are available for metadata:

* [favicon.ico, apple-icon.jpg, and icon.jpg](/docs/app/api-reference/file-conventions/metadata/app-icons.md)
* [opengraph-image.jpg and twitter-image.jpg](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md)
* [robots.txt](/docs/app/api-reference/file-conventions/metadata/robots.md)
* [sitemap.xml](/docs/app/api-reference/file-conventions/metadata/sitemap.md)

You can use these for static metadata, or you can programmatically generate these files with code.

## Favicons

Favicons are small icons that represent your site in bookmarks and search results. To add a favicon to your application, create a `favicon.ico` and add to the root of the app folder.

![Favicon Special File inside the App Folder with sibling layout and page files](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/favicon-ico.png)

> You can also programmatically generate favicons using code. See the [favicon docs](/docs/app/api-reference/file-conventions/metadata/app-icons.md) for more information.

## Static Open Graph images

Open Graph (OG) images are images that represent your site in social media. To add a static OG image to your application, create a `opengraph-image.png` file in the root of the app folder.

![OG image special file inside the App folder with sibling layout and page files](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/opengraph-image.png)

You can also add OG images for specific routes by creating a `opengraph-image.png` deeper down the folder structure. For example, to create an OG image specific to the `/blog` route, add a `opengraph-image.jpg` file inside the `blog` folder.

![OG image special file inside the blog folder](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/opengraph-image-blog.png)

The more specific image will take precedence over any OG images above it in the folder structure.

> Other image formats such as `jpeg`, `png`, and `gif` are also supported. See the [Open Graph Image docs](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md) for more information.

## Generated Open Graph images

The [`ImageResponse` constructor](/docs/app/api-reference/functions/image-response.md) allows you to generate dynamic images using JSX and CSS. This is useful for OG images that depend on data.

For example, to generate a unique OG image for each blog post, add a `opengraph-image.tsx` file inside the `blog` folder, and import the `ImageResponse` constructor from `next/og`:

```tsx filename="app/blog/[slug]/opengraph-image.tsx" switcher
import { ImageResponse } from 'next/og'
import { getPost } from '@/app/lib/data'

// Image metadata
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image({ params }: { params: { slug: string } }) {
  const post = await getPost(params.slug)

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
        {post.title}
      </div>
    )
  )
}
```

```jsx filename="app/blog/[slug]/opengraph-image.js" switcher
import { ImageResponse } from 'next/og'
import { getPost } from '@/app/lib/data'

// Image metadata
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image({ params }) {
  const post = await getPost(params.slug)

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
        {post.title}
      </div>
    )
  )
}
```

`ImageResponse` supports common CSS properties including flexbox and absolute positioning, custom fonts, text wrapping, centering, and nested images. [See the full list of supported CSS properties](/docs/app/api-reference/functions/image-response.md).

> **Good to know**:
>
> * Examples are available in the [Vercel OG Playground](https://og-playground.vercel.app/).
> * `ImageResponse` uses [`@vercel/og`](https://vercel.com/docs/og-image-generation), [`satori`](https://github.com/vercel/satori), and `resvg` to convert HTML and CSS into PNG.
> * Only flexbox and a subset of CSS properties are supported. Advanced layouts (e.g. `display: grid`) will not work.
## API Reference

Learn more about the Metadata APIs mentioned in this page.

- [generateMetadata](/docs/app/api-reference/functions/generate-metadata.md)
  - Learn how to add Metadata to your Next.js application for improved search engine optimization (SEO) and web shareability.
- [generateViewport](/docs/app/api-reference/functions/generate-viewport.md)
  - API Reference for the generateViewport function.
- [ImageResponse](/docs/app/api-reference/functions/image-response.md)
  - API Reference for the ImageResponse constructor.
- [Metadata Files](/docs/app/api-reference/file-conventions/metadata.md)
  - API documentation for the metadata file conventions.
- [favicon, icon, and apple-icon](/docs/app/api-reference/file-conventions/metadata/app-icons.md)
  - API Reference for the Favicon, Icon and Apple Icon file conventions.
- [opengraph-image and twitter-image](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md)
  - API Reference for the Open Graph Image and Twitter Image file conventions.
- [robots.txt](/docs/app/api-reference/file-conventions/metadata/robots.md)
  - API Reference for robots.txt file.
- [sitemap.xml](/docs/app/api-reference/file-conventions/metadata/sitemap.md)
  - API Reference for the sitemap.xml file.
- [htmlLimitedBots](/docs/app/api-reference/config/next-config-js/htmlLimitedBots.md)
  - Specify a list of user agents that should receive blocking metadata.


--------------------------------------------------------------------------------
title: "Route Handlers"
description: "Learn how to use Route Handlers"
source: "https://nextjs.org/docs/app/getting-started/route-handlers"
--------------------------------------------------------------------------------

# Route Handlers

## Route Handlers

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

![Route.js Special File](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/route-special-file.png)

> **Good to know**: Route Handlers are only available inside the `app` directory. They are the equivalent of [API Routes](/docs/pages/building-your-application/routing/api-routes.md) inside the `pages` directory meaning you **do not** need to use API Routes and Route Handlers together.

### Convention

Route Handlers are defined in a [`route.js|ts` file](/docs/app/api-reference/file-conventions/route.md) inside the `app` directory:

```ts filename="app/api/route.ts" switcher
export async function GET(request: Request) {}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {}
```

Route Handlers can be nested anywhere inside the `app` directory, similar to `page.js` and `layout.js`. But there **cannot** be a `route.js` file at the same route segment level as `page.js`.

### Supported HTTP Methods

The following [HTTP methods](https://developer.mozilla.org/docs/Web/HTTP/Methods) are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`. If an unsupported method is called, Next.js will return a `405 Method Not Allowed` response.

### Extended `NextRequest` and `NextResponse` APIs

In addition to supporting the native [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs, Next.js extends them with [`NextRequest`](/docs/app/api-reference/functions/next-request.md) and [`NextResponse`](/docs/app/api-reference/functions/next-response.md) to provide convenient helpers for advanced use cases.

### Caching

Route Handlers are not cached by default. You can, however, opt into caching for `GET` methods. Other supported HTTP methods are **not** cached. To cache a `GET` method, use a [route config option](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamic) such as `export const dynamic = 'force-static'` in your Route Handler file.

```ts filename="app/items/route.ts" switcher
export const dynamic = 'force-static'

export async function GET() {
  const res = await fetch('https://data.mongodb-api.com/...', {
    headers: {
      'Content-Type': 'application/json',
      'API-Key': process.env.DATA_API_KEY,
    },
  })
  const data = await res.json()

  return Response.json({ data })
}
```

```js filename="app/items/route.js" switcher
export const dynamic = 'force-static'

export async function GET() {
  const res = await fetch('https://data.mongodb-api.com/...', {
    headers: {
      'Content-Type': 'application/json',
      'API-Key': process.env.DATA_API_KEY,
    },
  })
  const data = await res.json()

  return Response.json({ data })
}
```

> **Good to know**: Other supported HTTP methods are **not** cached, even if they are placed alongside a `GET` method that is cached, in the same file.

#### With Cache Components

When using [Cache Components](/docs/app/getting-started/cache-components.md), you can use the [`use cache`](/docs/app/api-reference/directives/use-cache.md) directive to cache data fetching within your Route Handlers. Route Handlers are dynamic by default, but can be pre-rendered at build time if they don't use runtime or dynamic data.

```ts filename="app/api/posts/route.ts" switcher
import { cacheTag } from 'next/cache'

async function getPosts() {
  'use cache'
  cacheTag('posts')

  const posts = await fetchPosts()
  return posts
}

export async function GET() {
  const posts = await getPosts()
  return Response.json(posts)
}
```

```js filename="app/api/posts/route.js" switcher
import { cacheTag } from 'next/cache'

async function getPosts() {
  'use cache'
  cacheTag('posts')

  const posts = await fetchPosts()
  return posts
}

export async function GET() {
  const posts = await getPosts()
  return Response.json(posts)
}
```

See the [Cache Components documentation](/docs/app/getting-started/cache-components.md#route-handlers-with-cache-components) for more details on caching strategies and revalidation.

### Special Route Handlers

Special Route Handlers like [`sitemap.ts`](/docs/app/api-reference/file-conventions/metadata/sitemap.md), [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md), and [`icon.tsx`](/docs/app/api-reference/file-conventions/metadata/app-icons.md), and other [metadata files](/docs/app/api-reference/file-conventions/metadata.md) remain static by default unless they use Dynamic APIs or dynamic config options.

### Route Resolution

You can consider a `route` the lowest level routing primitive.

* They **do not** participate in layouts or client-side navigations like `page`.
* There **cannot** be a `route.js` file at the same route as `page.js`.

| Page                 | Route              | Result                       |
| -------------------- | ------------------ | ---------------------------- |
| `app/page.js`        | `app/route.js`     |  Conflict |
| `app/page.js`        | `app/api/route.js` |  Valid    |
| `app/[user]/page.js` | `app/api/route.js` |  Valid    |

Each `route.js` or `page.js` file takes over all HTTP verbs for that route.

```ts filename="app/page.ts" switcher
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}

// Conflict
// `app/route.ts`
export async function POST(request: Request) {}
```

```js filename="app/page.js" switcher
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}

// Conflict
// `app/route.js`
export async function POST(request) {}
```

Read more about how Route Handlers [complement your frontend application](/docs/app/guides/backend-for-frontend.md), or explore the Route Handlers [API Reference](/docs/app/api-reference/file-conventions/route.md).

### Route Context Helper

In TypeScript, you can type the `context` parameter for Route Handlers with the globally available [`RouteContext`](/docs/app/api-reference/file-conventions/route.md#route-context-helper) helper:

```ts filename="app/users/[id]/route.ts" switcher
import type { NextRequest } from 'next/server'

export async function GET(_req: NextRequest, ctx: RouteContext<'/users/[id]'>) {
  const { id } = await ctx.params
  return Response.json({ id })
}
```

> **Good to know**
>
> * Types are generated during `next dev`, `next build` or `next typegen`.
## API Reference

Learn more about Route Handlers

- [route.js](/docs/app/api-reference/file-conventions/route.md)
  - API reference for the route.js special file.
- [Backend for Frontend](/docs/app/guides/backend-for-frontend.md)
  - Learn how to use Next.js as a backend framework


--------------------------------------------------------------------------------
title: "Proxy"
description: "Learn how to use Proxy"
source: "https://nextjs.org/docs/app/getting-started/proxy"
--------------------------------------------------------------------------------

# Proxy

## Proxy

> **Good to know**: Starting with Next.js 16, Middleware is now called Proxy to better reflect its purpose. The functionality remains the same.

Proxy allows you to run code before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

### Use cases

Some common scenarios where Proxy is effective include:

* Modifying headers for all pages or a subset of pages
* Rewriting to different pages based on A/B tests or experiments
* Programmatic redirects based on incoming request properties

For simple redirects, consider using the [`redirects`](/docs/app/api-reference/config/next-config-js/redirects.md) configuration in `next.config.ts` first. Proxy should be used when you need access to request data or more complex logic.

Proxy is *not* intended for slow data fetching. While Proxy can be helpful for [optimistic checks](/docs/app/guides/authentication.md#optimistic-checks-with-proxy-optional) such as permission-based redirects, it should not be used as a full session management or authorization solution.

Using fetch with `options.cache`, `options.next.revalidate`, or `options.next.tags`, has no effect in Proxy.

### Convention

Create a `proxy.ts` (or `.js`) file in the project root, or inside `src` if applicable, so that it is located at the same level as `pages` or `app`.

> **Note**: While only one `proxy.ts` file is supported per project, you can still organize your proxy logic into modules. Break out proxy functionalities into separate `.ts` or `.js` files and import them into your main `proxy.ts` file. This allows for cleaner management of route-specific proxy, aggregated in the `proxy.ts` for centralized control. By enforcing a single proxy file, it simplifies configuration, prevents potential conflicts, and optimizes performance by avoiding multiple proxy layers.

### Example

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url))
}

// See "Matching Paths" below to learn more
export const config = {
  matcher: '/about/:path*',
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request) {
  return NextResponse.redirect(new URL('/home', request.url))
}

// See "Matching Paths" below to learn more
export const config = {
  matcher: '/about/:path*',
}
```

Read more about [using `proxy`](/docs/app/guides/backend-for-frontend.md#proxy), or refer to the `proxy` [API reference](/docs/app/api-reference/file-conventions/proxy.md).
## API Reference

Learn more about Proxy

- [proxy.js](/docs/app/api-reference/file-conventions/proxy.md)
  - API reference for the proxy.js file.
- [Backend for Frontend](/docs/app/guides/backend-for-frontend.md)
  - Learn how to use Next.js as a backend framework


--------------------------------------------------------------------------------
title: "Deploying"
description: "Learn how to deploy your Next.js application."
source: "https://nextjs.org/docs/app/getting-started/deploying"
--------------------------------------------------------------------------------

# Deploying

Next.js can be deployed as a Node.js server, Docker container, static export, or adapted to run on different platforms.

| Deployment Option                | Feature Support   |
| -------------------------------- | ----------------- |
| [Node.js server](#nodejs-server) | All               |
| [Docker container](#docker)      | All               |
| [Static export](#static-export)  | Limited           |
| [Adapters](#adapters)            | Platform-specific |

## Node.js server

Next.js can be deployed to any provider that supports Node.js. Ensure your `package.json` has the `"build"` and `"start"` scripts:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

Then, run `npm run build` to build your application and `npm run start` to start the Node.js server. This server supports all Next.js features. If needed, you can also eject to a [custom server](/docs/app/guides/custom-server.md).

Node.js deployments support all Next.js features. Learn how to [configure them](/docs/app/guides/self-hosting.md) for your infrastructure.

### Templates

* [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)
* [Railway](https://github.com/nextjs/deploy-railway)
* [Replit](https://github.com/nextjs/deploy-replit)

## Docker

Next.js can be deployed to any provider that supports [Docker](https://www.docker.com/) containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker.

Docker deployments support all Next.js features. Learn how to [configure them](/docs/app/guides/self-hosting.md) for your infrastructure.

> **Note for development:** While Docker is excellent for production deployments, consider using local development (`npm run dev`) instead of Docker during development on Mac and Windows for better performance. [Learn more about optimizing local development](/docs/app/guides/local-development.md).

### Templates

* [Docker](https://github.com/vercel/next.js/tree/canary/examples/with-docker)
* [Docker Multi-Environment](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env)
* [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)
* [Fly.io](https://github.com/nextjs/deploy-fly)
* [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)
* [Render](https://github.com/nextjs/deploy-render)
* [SST](https://github.com/nextjs/deploy-sst)

## Static export

Next.js enables starting as a static site or [Single-Page Application (SPA)](/docs/app/guides/single-page-applications.md), then later optionally upgrading to use features that require a server.

Since Next.js supports [static exports](/docs/app/guides/static-exports.md), it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.

Running as a [static export](/docs/app/guides/static-exports.md) **does not** support Next.js features that require a server. [Learn more](/docs/app/guides/static-exports.md#unsupported-features).

### Templates

* [GitHub Pages](https://github.com/nextjs/deploy-github-pages)

## Adapters

Next.js can be adapted to run on different platforms to support their infrastructure capabilities.

Refer to each provider's documentation for information on supported Next.js features:

* [AWS Amplify Hosting](https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components)
* [Cloudflare](https://developers.cloudflare.com/workers/frameworks/framework-guides/nextjs)
* [Deno Deploy](https://docs.deno.com/examples/next_tutorial)
* [Netlify](https://docs.netlify.com/frameworks/next-js/overview/#next-js-support-on-netlify)
* [Vercel](https://vercel.com/docs/frameworks/nextjs)

> **Note:** We are working on a [Deployment Adapters API](https://github.com/vercel/next.js/discussions/77740) for all platforms to adopt. After completion, we will add documentation on how to write your own adapters.


--------------------------------------------------------------------------------
title: "Upgrading"
description: "Learn how to upgrade your Next.js application to the latest version or canary."
source: "https://nextjs.org/docs/app/getting-started/upgrading"
--------------------------------------------------------------------------------

# Upgrading

## Latest version

To update to the latest version of Next.js, you can use the `upgrade` codemod:

```bash filename="Terminal"
npx @next/codemod@latest upgrade latest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:

```bash package="pnpm"
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="npm"
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="yarn"
yarn add next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="bun"
bun add next@latest react@latest react-dom@latest eslint-config-next@latest
```

## Canary version

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

```bash filename="Terminal"
npm i next@canary
```

### Features available in canary

The following features are currently available in canary:

**Authentication**:

* [`forbidden`](/docs/app/api-reference/functions/forbidden.md)
* [`unauthorized`](/docs/app/api-reference/functions/unauthorized.md)
* [`forbidden.js`](/docs/app/api-reference/file-conventions/forbidden.md)
* [`unauthorized.js`](/docs/app/api-reference/file-conventions/unauthorized.md)
* [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts.md)
## Version guides

See the version guides for in-depth upgrade instructions.

- [Version 16](/docs/app/guides/upgrading/version-16.md)
  - Upgrade your Next.js Application from Version 15 to 16.
- [Version 15](/docs/app/guides/upgrading/version-15.md)
  - Upgrade your Next.js Application from Version 14 to 15.
- [Version 14](/docs/app/guides/upgrading/version-14.md)
  - Upgrade your Next.js Application from Version 13 to 14.



--------------------------------------------------------------------------------
title: "Guides"
description: "Learn how to implement common patterns and real-world use cases using Next.js"
source: "https://nextjs.org/docs/app/guides"
--------------------------------------------------------------------------------

# Guides



 - [Analytics](/docs/app/guides/analytics.md)
 - [Authentication](/docs/app/guides/authentication.md)
 - [Backend for Frontend](/docs/app/guides/backend-for-frontend.md)
 - [Caching](/docs/app/guides/caching.md)
 - [CI Build Caching](/docs/app/guides/ci-build-caching.md)
 - [Content Security Policy](/docs/app/guides/content-security-policy.md)
 - [CSS-in-JS](/docs/app/guides/css-in-js.md)
 - [Custom Server](/docs/app/guides/custom-server.md)
 - [Data Security](/docs/app/guides/data-security.md)
 - [Debugging](/docs/app/guides/debugging.md)
 - [Draft Mode](/docs/app/guides/draft-mode.md)
 - [Environment Variables](/docs/app/guides/environment-variables.md)
 - [Forms](/docs/app/guides/forms.md)
 - [ISR](/docs/app/guides/incremental-static-regeneration.md)
 - [Instrumentation](/docs/app/guides/instrumentation.md)
 - [Internationalization](/docs/app/guides/internationalization.md)
 - [JSON-LD](/docs/app/guides/json-ld.md)
 - [Lazy Loading](/docs/app/guides/lazy-loading.md)
 - [Development Environment](/docs/app/guides/local-development.md)
 - [Next.js MCP Server](/docs/app/guides/mcp.md)
 - [MDX](/docs/app/guides/mdx.md)
 - [Memory Usage](/docs/app/guides/memory-usage.md)
 - [Migrating](/docs/app/guides/migrating.md)
 - [Multi-tenant](/docs/app/guides/multi-tenant.md)
 - [Multi-zones](/docs/app/guides/multi-zones.md)
 - [OpenTelemetry](/docs/app/guides/open-telemetry.md)
 - [Package Bundling](/docs/app/guides/package-bundling.md)
 - [Prefetching](/docs/app/guides/prefetching.md)
 - [Production](/docs/app/guides/production-checklist.md)
 - [PWAs](/docs/app/guides/progressive-web-apps.md)
 - [Redirecting](/docs/app/guides/redirecting.md)
 - [Sass](/docs/app/guides/sass.md)
 - [Scripts](/docs/app/guides/scripts.md)
 - [Self-Hosting](/docs/app/guides/self-hosting.md)
 - [SPAs](/docs/app/guides/single-page-applications.md)
 - [Static Exports](/docs/app/guides/static-exports.md)
 - [Tailwind CSS v3](/docs/app/guides/tailwind-v3-css.md)
 - [Testing](/docs/app/guides/testing.md)
 - [Third Party Libraries](/docs/app/guides/third-party-libraries.md)
 - [Upgrading](/docs/app/guides/upgrading.md)
 - [Videos](/docs/app/guides/videos.md)

--------------------------------------------------------------------------------
title: "How to add analytics to your Next.js application"
description: "Measure and track page performance using Next.js Speed Insights"
source: "https://nextjs.org/docs/app/guides/analytics"
--------------------------------------------------------------------------------

# Analytics

Next.js has built-in support for measuring and reporting performance metrics. You can either use the [`useReportWebVitals`](/docs/app/api-reference/functions/use-report-web-vitals.md) hook to manage reporting yourself, or alternatively, Vercel provides a [managed service](https://vercel.com/analytics?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website) to automatically collect and visualize metrics for you.

## Client Instrumentation

For more advanced analytics and monitoring needs, Next.js provides a `instrumentation-client.js|ts` file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.

To use it, create an `instrumentation-client.js` or `instrumentation-client.ts` file in your application's root directory:

```js filename="instrumentation-client.js"
// Initialize analytics before the app starts
console.log('Analytics initialized')

// Set up global error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

## Build Your Own

```jsx filename="app/_components/web-vitals.js"
'use client'

import { useReportWebVitals } from 'next/web-vitals'

export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric)
  })
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

View the [API Reference](/docs/app/api-reference/functions/use-report-web-vitals.md) for more information.

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

```tsx filename="app/_components/web-vitals.tsx" switcher
'use client'

import { useReportWebVitals } from 'next/web-vitals'

export function WebVitals() {
  useReportWebVitals((metric) => {
    switch (metric.name) {
      case 'FCP': {
        // handle FCP results
      }
      case 'LCP': {
        // handle LCP results
      }
      // ...
    }
  })
}
```

```jsx filename="app/_components/web-vitals.js" switcher
'use client'

import { useReportWebVitals } from 'next/web-vitals'

export function WebVitals() {
  useReportWebVitals((metric) => {
    switch (metric.name) {
      case 'FCP': {
        // handle FCP results
      }
      case 'LCP': {
        // handle LCP results
      }
      // ...
    }
  })
}
```

## Sending results to external systems

You can send results to any endpoint to measure and track
real user performance on your site. For example:

```js
useReportWebVitals((metric) => {
  const body = JSON.stringify(metric)
  const url = 'https://example.com/analytics'

  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url, body)
  } else {
    fetch(url, { body, method: 'POST', keepalive: true })
  }
})
```

> **Good to know**: If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the
> `id` value can allow you to construct metric distributions manually (to calculate percentiles,
> etc.)

> ```js
> useReportWebVitals((metric) => {
>   // Use `window.gtag` if you initialized Google Analytics as this example:
>   // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>   window.gtag('event', metric.name, {
>     value: Math.round(
>       metric.name === 'CLS' ? metric.value * 1000 : metric.value
>     ), // values must be integers
>     event_label: metric.id, // id unique to current page load
>     non_interaction: true, // avoids affecting bounce rate.
>   })
> })
> ```
>
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).


--------------------------------------------------------------------------------
title: "How to implement authentication in Next.js"
description: "Learn how to implement authentication in your Next.js application."
source: "https://nextjs.org/docs/app/guides/authentication"
--------------------------------------------------------------------------------

# Authentication

Understanding authentication is crucial for protecting your application's data. This page will guide you through what React and Next.js features to use to implement auth.

Before starting, it helps to break down the process into three concepts:

1. **[Authentication](#authentication)**: Verifies if the user is who they say they are. It requires the user to prove their identity with something they have, such as a username and password.
2. **[Session Management](#session-management)**: Tracks the user's auth state across requests.
3. **[Authorization](#authorization)**: Decides what routes and data the user can access.

This diagram shows the authentication flow using React and Next.js features:

![Diagram showing the authentication flow with React and Next.js features](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/authentication-overview.png)

The examples on this page walk through basic username and password auth for educational purposes. While you can implement a custom auth solution, for increased security and simplicity, we recommend using an authentication library. These offer built-in solutions for authentication, session management, and authorization, as well as additional features such as social logins, multi-factor authentication, and role-based access control. You can find a list in the [Auth Libraries](#auth-libraries) section.

## Authentication

### Sign-up and login functionality

You can use the [`<form>`](https://react.dev/reference/react-dom/components/form) element with React's [Server Actions](/docs/app/getting-started/updating-data.md) and `useActionState` to capture user credentials, validate form fields, and call your Authentication Provider's API or database.

Since Server Actions always execute on the server, they provide a secure environment for handling authentication logic.

Here are the steps to implement signup/login functionality:

#### 1. Capture user credentials

To capture user credentials, create a form that invokes a Server Action on submission. For example, a signup form that accepts the user's name, email, and password:

```tsx filename="app/ui/signup-form.tsx" switcher
import { signup } from '@/app/actions/auth'

export function SignupForm() {
  return (
    <form action={signup}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  )
}
```

```jsx filename="app/ui/signup-form.js" switcher
import { signup } from '@/app/actions/auth'

export function SignupForm() {
  return (
    <form action={signup}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  )
}
```

```tsx filename="app/actions/auth.ts" switcher
export async function signup(formData: FormData) {}
```

```jsx filename="app/actions/auth.js" switcher
export async function signup(formData) {}
```

#### 2. Validate form fields on the server

Use the Server Action to validate the form fields on the server. If your authentication provider doesn't provide form validation, you can use a schema validation library like [Zod](https://zod.dev/) or [Yup](https://github.com/jquense/yup).

Using Zod as an example, you can define a form schema with appropriate error messages:

```ts filename="app/lib/definitions.ts" switcher
import * as z from 'zod'

export const SignupFormSchema = z.object({
  name: z
    .string()
    .min(2, { error: 'Name must be at least 2 characters long.' })
    .trim(),
  email: z.email({ error: 'Please enter a valid email.' }).trim(),
  password: z
    .string()
    .min(8, { error: 'Be at least 8 characters long' })
    .regex(/[a-zA-Z]/, { error: 'Contain at least one letter.' })
    .regex(/[0-9]/, { error: 'Contain at least one number.' })
    .regex(/[^a-zA-Z0-9]/, {
      error: 'Contain at least one special character.',
    })
    .trim(),
})

export type FormState =
  | {
      errors?: {
        name?: string[]
        email?: string[]
        password?: string[]
      }
      message?: string
    }
  | undefined
```

```js filename="app/lib/definitions.js" switcher
import * as z from 'zod'

export const SignupFormSchema = z.object({
  name: z
    .string()
    .min(2, { error: 'Name must be at least 2 characters long.' })
    .trim(),
  email: z.email({ error: 'Please enter a valid email.' }).trim(),
  password: z
    .string()
    .min(8, { error: 'Be at least 8 characters long' })
    .regex(/[a-zA-Z]/, { error: 'Contain at least one letter.' })
    .regex(/[0-9]/, { error: 'Contain at least one number.' })
    .regex(/[^a-zA-Z0-9]/, {
      error: 'Contain at least one special character.',
    })
    .trim(),
})
```

To prevent unnecessary calls to your authentication provider's API or database, you can `return` early in the Server Action if any form fields do not match the defined schema.

```ts filename="app/actions/auth.ts" switcher
import { SignupFormSchema, FormState } from '@/app/lib/definitions'

export async function signup(state: FormState, formData: FormData) {
  // Validate form fields
  const validatedFields = SignupFormSchema.safeParse({
    name: formData.get('name'),
    email: formData.get('email'),
    password: formData.get('password'),
  })

  // If any form fields are invalid, return early
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  // Call the provider or db to create a user...
}
```

```js filename="app/actions/auth.js" switcher
import { SignupFormSchema } from '@/app/lib/definitions'

export async function signup(state, formData) {
  // Validate form fields
  const validatedFields = SignupFormSchema.safeParse({
    name: formData.get('name'),
    email: formData.get('email'),
    password: formData.get('password'),
  })

  // If any form fields are invalid, return early
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  // Call the provider or db to create a user...
}
```

Back in your `<SignupForm />`, you can use React's `useActionState` hook to display validation errors while the form is submitting:

```tsx filename="app/ui/signup-form.tsx" switcher highlight={7,15,21,27-36}
'use client'

import { signup } from '@/app/actions/auth'
import { useActionState } from 'react'

export default function SignupForm() {
  const [state, action, pending] = useActionState(signup, undefined)

  return (
    <form action={action}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      {state?.errors?.name && <p>{state.errors.name}</p>}

      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" placeholder="Email" />
      </div>
      {state?.errors?.email && <p>{state.errors.email}</p>}

      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      {state?.errors?.password && (
        <div>
          <p>Password must:</p>
          <ul>
            {state.errors.password.map((error) => (
              <li key={error}>- {error}</li>
            ))}
          </ul>
        </div>
      )}
      <button disabled={pending} type="submit">
        Sign Up
      </button>
    </form>
  )
}
```

```jsx filename="app/ui/signup-form.js" switcher highlight={7,15,21,27-36}
'use client'

import { signup } from '@/app/actions/auth'
import { useActionState } from 'react'

export default function SignupForm() {
  const [state, action, pending] = useActionState(signup, undefined)

  return (
    <form action={action}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      {state?.errors?.name && <p>{state.errors.name}</p>}

      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" placeholder="Email" />
      </div>
      {state?.errors?.email && <p>{state.errors.email}</p>}

      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      {state?.errors?.password && (
        <div>
          <p>Password must:</p>
          <ul>
            {state.errors.password.map((error) => (
              <li key={error}>- {error}</li>
            ))}
          </ul>
        </div>
      )}
      <button disabled={pending} type="submit">
        Sign Up
      </button>
    </form>
  )
}
```

> **Good to know:**
>
> * In React 19, `useFormStatus` includes additional keys on the returned object, like data, method, and action. If you are not using React 19, only the `pending` key is available.
> * Before mutating data, you should always ensure a user is also authorized to perform the action. See [Authentication and Authorization](#authorization).

#### 3. Create a user or check user credentials

After validating form fields, you can create a new user account or check if the user exists by calling your authentication provider's API or database.

Continuing from the previous example:

```tsx filename="app/actions/auth.tsx" switcher
export async function signup(state: FormState, formData: FormData) {
  // 1. Validate form fields
  // ...

  // 2. Prepare data for insertion into database
  const { name, email, password } = validatedFields.data
  // e.g. Hash the user's password before storing it
  const hashedPassword = await bcrypt.hash(password, 10)

  // 3. Insert the user into the database or call an Auth Library's API
  const data = await db
    .insert(users)
    .values({
      name,
      email,
      password: hashedPassword,
    })
    .returning({ id: users.id })

  const user = data[0]

  if (!user) {
    return {
      message: 'An error occurred while creating your account.',
    }
  }

  // TODO:
  // 4. Create user session
  // 5. Redirect user
}
```

```jsx filename="app/actions/auth.js" switcher
export async function signup(state, formData) {
  // 1. Validate form fields
  // ...

  // 2. Prepare data for insertion into database
  const { name, email, password } = validatedFields.data
  // e.g. Hash the user's password before storing it
  const hashedPassword = await bcrypt.hash(password, 10)

  // 3. Insert the user into the database or call an Library API
  const data = await db
    .insert(users)
    .values({
      name,
      email,
      password: hashedPassword,
    })
    .returning({ id: users.id })

  const user = data[0]

  if (!user) {
    return {
      message: 'An error occurred while creating your account.',
    }
  }

  // TODO:
  // 4. Create user session
  // 5. Redirect user
}
```

After successfully creating the user account or verifying the user credentials, you can create a session to manage the user's auth state. Depending on your session management strategy, the session can be stored in a cookie or database, or both. Continue to the [Session Management](#session-management) section to learn more.

> **Tips:**
>
> * The example above is verbose since it breaks down the authentication steps for the purpose of education. This highlights that implementing your own secure solution can quickly become complex. Consider using an [Auth Library](#auth-libraries) to simplify the process.
> * To improve the user experience, you may want to check for duplicate emails or usernames earlier in the registration flow. For example, as the user types in a username or the input field loses focus. This can help prevent unnecessary form submissions and provide immediate feedback to the user. You can debounce requests with libraries such as [use-debounce](https://www.npmjs.com/package/use-debounce) to manage the frequency of these checks.

## Session Management

Session management ensures that the user's authenticated state is preserved across requests. It involves creating, storing, refreshing, and deleting sessions or tokens.

There are two types of sessions:

1. [**Stateless**](#stateless-sessions): Session data (or a token) is stored in the browser's cookies. The cookie is sent with each request, allowing the session to be verified on the server. This method is simpler, but can be less secure if not implemented correctly.
2. [**Database**](#database-sessions): Session data is stored in a database, with the user's browser only receiving the encrypted session ID. This method is more secure, but can be complex and use more server resources.

> **Good to know:** While you can use either method, or both, we recommend using a session management library such as [iron-session](https://github.com/vvo/iron-session) or [Jose](https://github.com/panva/jose).

### Stateless Sessions

To create and manage stateless sessions, there are a few steps you need to follow:

1. Generate a secret key, which will be used to sign your session, and store it as an [environment variable](/docs/app/guides/environment-variables.md).
2. Write logic to encrypt/decrypt session data using a session management library.
3. Manage cookies using the Next.js [`cookies`](/docs/app/api-reference/functions/cookies.md) API.

In addition to the above, consider adding functionality to [update (or refresh)](#updating-or-refreshing-sessions) the session when the user returns to the application, and [delete](#deleting-the-session) the session when the user logs out.

> **Good to know:** Check if your [auth library](#auth-libraries) includes session management.

#### 1. Generating a secret key

There are a few ways you can generate secret key to sign your session. For example, you may choose to use the `openssl` command in your terminal:

```bash filename="terminal"
openssl rand -base64 32
```

This command generates a 32-character random string that you can use as your secret key and store in your [environment variables file](/docs/app/guides/environment-variables.md):

```bash filename=".env"
SESSION_SECRET=your_secret_key
```

You can then reference this key in your session management logic:

```js filename="app/lib/session.js"
const secretKey = process.env.SESSION_SECRET
```

#### 2. Encrypting and decrypting sessions

Next, you can use your preferred [session management library](#session-management-libraries) to encrypt and decrypt sessions. Continuing from the previous example, we'll use [Jose](https://www.npmjs.com/package/jose) (compatible with the [Edge Runtime](/docs/app/api-reference/edge.md)) and React's [`server-only`](https://www.npmjs.com/package/server-only) package to ensure that your session management logic is only executed on the server.

```tsx filename="app/lib/session.ts" switcher
import 'server-only'
import { SignJWT, jwtVerify } from 'jose'
import { SessionPayload } from '@/app/lib/definitions'

const secretKey = process.env.SESSION_SECRET
const encodedKey = new TextEncoder().encode(secretKey)

export async function encrypt(payload: SessionPayload) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(encodedKey)
}

export async function decrypt(session: string | undefined = '') {
  try {
    const { payload } = await jwtVerify(session, encodedKey, {
      algorithms: ['HS256'],
    })
    return payload
  } catch (error) {
    console.log('Failed to verify session')
  }
}
```

```jsx filename="app/lib/session.js" switcher
import 'server-only'
import { SignJWT, jwtVerify } from 'jose'

const secretKey = process.env.SESSION_SECRET
const encodedKey = new TextEncoder().encode(secretKey)

export async function encrypt(payload) {
  return new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(encodedKey)
}

export async function decrypt(session) {
  try {
    const { payload } = await jwtVerify(session, encodedKey, {
      algorithms: ['HS256'],
    })
    return payload
  } catch (error) {
    console.log('Failed to verify session')
  }
}
```

> **Tips**:
>
> * The payload should contain the **minimum**, unique user data that'll be used in subsequent requests, such as the user's ID, role, etc. It should not contain personally identifiable information like phone number, email address, credit card information, etc, or sensitive data like passwords.

#### 3. Setting cookies (recommended options)

To store the session in a cookie, use the Next.js [`cookies`](/docs/app/api-reference/functions/cookies.md) API. The cookie should be set on the server, and include the recommended options:

* **HttpOnly**: Prevents client-side JavaScript from accessing the cookie.
* **Secure**: Use https to send the cookie.
* **SameSite**: Specify whether the cookie can be sent with cross-site requests.
* **Max-Age or Expires**: Delete the cookie after a certain period.
* **Path**: Define the URL path for the cookie.

Please refer to [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) for more information on each of these options.

```ts filename="app/lib/session.ts" switcher
import 'server-only'
import { cookies } from 'next/headers'

export async function createSession(userId: string) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  const session = await encrypt({ userId, expiresAt })
  const cookieStore = await cookies()

  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

```js filename="app/lib/session.js" switcher
import 'server-only'
import { cookies } from 'next/headers'

export async function createSession(userId) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  const session = await encrypt({ userId, expiresAt })
  const cookieStore = await cookies()

  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

Back in your Server Action, you can invoke the `createSession()` function, and use the [`redirect()`](/docs/app/guides/redirecting.md) API to redirect the user to the appropriate page:

```ts filename="app/actions/auth.ts" switcher
import { createSession } from '@/app/lib/session'

export async function signup(state: FormState, formData: FormData) {
  // Previous steps:
  // 1. Validate form fields
  // 2. Prepare data for insertion into database
  // 3. Insert the user into the database or call an Library API

  // Current steps:
  // 4. Create user session
  await createSession(user.id)
  // 5. Redirect user
  redirect('/profile')
}
```

```js filename="app/actions/auth.js" switcher
import { createSession } from '@/app/lib/session'

export async function signup(state, formData) {
  // Previous steps:
  // 1. Validate form fields
  // 2. Prepare data for insertion into database
  // 3. Insert the user into the database or call an Library API

  // Current steps:
  // 4. Create user session
  await createSession(user.id)
  // 5. Redirect user
  redirect('/profile')
}
```

> **Tips**:
>
> * **Cookies should be set on the server** to prevent client-side tampering.
> * 🎥 Watch: Learn more about stateless sessions and authentication with Next.js → [YouTube (11 minutes)](https://www.youtube.com/watch?v=DJvM2lSPn6w).

#### Updating (or refreshing) sessions

You can also extend the session's expiration time. This is useful for keeping the user logged in after they access the application again. For example:

```ts filename="app/lib/session.ts" switcher
import 'server-only'
import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'

export async function updateSession() {
  const session = (await cookies()).get('session')?.value
  const payload = await decrypt(session)

  if (!session || !payload) {
    return null
  }

  const expires = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)

  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expires,
    sameSite: 'lax',
    path: '/',
  })
}
```

```js filename="app/lib/session.js" switcher
import 'server-only'
import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'

export async function updateSession() {
  const session = (await cookies()).get('session')?.value
  const payload = await decrypt(session)

  if (!session || !payload) {
    return null
  }

  const expires = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)(
    await cookies()
  ).set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expires,
    sameSite: 'lax',
    path: '/',
  })
}
```

> **Tip:** Check if your auth library supports refresh tokens, which can be used to extend the user's session.

#### Deleting the session

To delete the session, you can delete the cookie:

```ts filename="app/lib/session.ts" switcher
import 'server-only'
import { cookies } from 'next/headers'

export async function deleteSession() {
  const cookieStore = await cookies()
  cookieStore.delete('session')
}
```

```js filename="app/lib/session.js" switcher
import 'server-only'
import { cookies } from 'next/headers'

export async function deleteSession() {
  const cookieStore = await cookies()
  cookieStore.delete('session')
}
```

Then you can reuse the `deleteSession()` function in your application, for example, on logout:

```ts filename="app/actions/auth.ts" switcher
import { cookies } from 'next/headers'
import { deleteSession } from '@/app/lib/session'

export async function logout() {
  await deleteSession()
  redirect('/login')
}
```

```js filename="app/actions/auth.js" switcher
import { cookies } from 'next/headers'
import { deleteSession } from '@/app/lib/session'

export async function logout() {
  await deleteSession()
  redirect('/login')
}
```

### Database Sessions

To create and manage database sessions, you'll need to follow these steps:

1. Create a table in your database to store session and data (or check if your Auth Library handles this).
2. Implement functionality to insert, update, and delete sessions
3. Encrypt the session ID before storing it in the user's browser, and ensure the database and cookie stay in sync (this is optional, but recommended for optimistic auth checks in [Proxy](#optimistic-checks-with-proxy-optional)).

For example:

```ts filename="app/lib/session.ts" switcher
import cookies from 'next/headers'
import { db } from '@/app/lib/db'
import { encrypt } from '@/app/lib/session'

export async function createSession(id: number) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)

  // 1. Create a session in the database
  const data = await db
    .insert(sessions)
    .values({
      userId: id,
      expiresAt,
    })
    // Return the session ID
    .returning({ id: sessions.id })

  const sessionId = data[0].id

  // 2. Encrypt the session ID
  const session = await encrypt({ sessionId, expiresAt })

  // 3. Store the session in cookies for optimistic auth checks
  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

```js filename="app/lib/session.js" switcher
import cookies from 'next/headers'
import { db } from '@/app/lib/db'
import { encrypt } from '@/app/lib/session'

export async function createSession(id) {
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)

  // 1. Create a session in the database
  const data = await db
    .insert(sessions)
    .values({
      userId: id,
      expiresAt,
    })
    // Return the session ID
    .returning({ id: sessions.id })

  const sessionId = data[0].id

  // 2. Encrypt the session ID
  const session = await encrypt({ sessionId, expiresAt })

  // 3. Store the session in cookies for optimistic auth checks
  const cookieStore = await cookies()
  cookieStore.set('session', session, {
    httpOnly: true,
    secure: true,
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}
```

> **Tips**:
>
> * For faster access, you may consider adding server caching for the lifetime of the session. You can also keep the session data in your primary database, and combine data requests to reduce the number of queries.
> * You may opt to use database sessions for more advanced use cases, such as keeping track of the last time a user logged in, or number of active devices, or give users the ability to log out of all devices.

After implementing session management, you'll need to add authorization logic to control what users can access and do within your application. Continue to the [Authorization](#authorization) section to learn more.

## Authorization

Once a user is authenticated and a session is created, you can implement authorization to control what the user can access and do within your application.

There are two main types of authorization checks:

1. **Optimistic**: Checks if the user is authorized to access a route or perform an action using the session data stored in the cookie. These checks are useful for quick operations, such as showing/hiding UI elements or redirecting users based on permissions or roles.
2. **Secure**: Checks if the user is authorized to access a route or perform an action using the session data stored in the database. These checks are more secure and are used for operations that require access to sensitive data or actions.

For both cases, we recommend:

* Creating a [Data Access Layer](#creating-a-data-access-layer-dal) to centralize your authorization logic
* Using [Data Transfer Objects (DTO)](#using-data-transfer-objects-dto) to only return the necessary data
* Optionally use [Proxy](#optimistic-checks-with-proxy-optional) to perform optimistic checks.

### Optimistic checks with Proxy (Optional)

There are some cases where you may want to use [Proxy](/docs/app/api-reference/file-conventions/proxy.md) and redirect users based on permissions:

* To perform optimistic checks. Since Proxy runs on every route, it's a good way to centralize redirect logic and pre-filter unauthorized users.
* To protect static routes that share data between users (e.g. content behind a paywall).

However, since Proxy runs on every route, including [prefetched](/docs/app/getting-started/linking-and-navigating.md#prefetching) routes, it's important to only read the session from the cookie (optimistic checks), and avoid database checks to prevent performance issues.

For example:

```tsx filename="proxy.ts" switcher
import { NextRequest, NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'

// 1. Specify protected and public routes
const protectedRoutes = ['/dashboard']
const publicRoutes = ['/login', '/signup', '/']

export default async function proxy(req: NextRequest) {
  // 2. Check if the current route is protected or public
  const path = req.nextUrl.pathname
  const isProtectedRoute = protectedRoutes.includes(path)
  const isPublicRoute = publicRoutes.includes(path)

  // 3. Decrypt the session from the cookie
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  // 4. Redirect to /login if the user is not authenticated
  if (isProtectedRoute && !session?.userId) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }

  // 5. Redirect to /dashboard if the user is authenticated
  if (
    isPublicRoute &&
    session?.userId &&
    !req.nextUrl.pathname.startsWith('/dashboard')
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }

  return NextResponse.next()
}

// Routes Proxy should not run on
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'

// 1. Specify protected and public routes
const protectedRoutes = ['/dashboard']
const publicRoutes = ['/login', '/signup', '/']

export default async function proxy(req) {
  // 2. Check if the current route is protected or public
  const path = req.nextUrl.pathname
  const isProtectedRoute = protectedRoutes.includes(path)
  const isPublicRoute = publicRoutes.includes(path)

  // 3. Decrypt the session from the cookie
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  // 5. Redirect to /login if the user is not authenticated
  if (isProtectedRoute && !session?.userId) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }

  // 6. Redirect to /dashboard if the user is authenticated
  if (
    isPublicRoute &&
    session?.userId &&
    !req.nextUrl.pathname.startsWith('/dashboard')
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }

  return NextResponse.next()
}

// Routes Proxy should not run on
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
}
```

While Proxy can be useful for initial checks, it should not be your only line of defense in protecting your data. The majority of security checks should be performed as close as possible to your data source, see [Data Access Layer](#creating-a-data-access-layer-dal) for more information.

> **Tips**:
>
> * In Proxy, you can also read cookies using `req.cookies.get('session').value`.
> * Proxy uses the Node.js runtime, check if your Auth library and session management library are compatible. You may need to use [Middleware](https://github.com/vercel/next.js/blob/v15.5.6/docs/01-app/03-api-reference/03-file-conventions/middleware.mdx) if your Auth library only supports [Edge Runtime](/docs/app/api-reference/edge.md)
> * You can use the `matcher` property in the Proxy to specify which routes Proxy should run on. Although, for auth, it's recommended Proxy runs on all routes.

### Creating a Data Access Layer (DAL)

We recommend creating a DAL to centralize your data requests and authorization logic.

The DAL should include a function that verifies the user's session as they interact with your application. At the very least, the function should check if the session is valid, then redirect or return the user information needed to make further requests.

For example, create a separate file for your DAL that includes a `verifySession()` function. Then use React's [cache](https://react.dev/reference/react/cache) API to memoize the return value of the function during a React render pass:

```tsx filename="app/lib/dal.ts" switcher
import 'server-only'

import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'

export const verifySession = cache(async () => {
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  if (!session?.userId) {
    redirect('/login')
  }

  return { isAuth: true, userId: session.userId }
})
```

```js filename="app/lib/dal.js" switcher
import 'server-only'

import { cookies } from 'next/headers'
import { decrypt } from '@/app/lib/session'

export const verifySession = cache(async () => {
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  if (!session.userId) {
    redirect('/login')
  }

  return { isAuth: true, userId: session.userId }
})
```

You can then invoke the `verifySession()` function in your data requests, Server Actions, Route Handlers:

```tsx filename="app/lib/dal.ts" switcher
export const getUser = cache(async () => {
  const session = await verifySession()
  if (!session) return null

  try {
    const data = await db.query.users.findMany({
      where: eq(users.id, session.userId),
      // Explicitly return the columns you need rather than the whole user object
      columns: {
        id: true,
        name: true,
        email: true,
      },
    })

    const user = data[0]

    return user
  } catch (error) {
    console.log('Failed to fetch user')
    return null
  }
})
```

```jsx filename="app/lib/dal.js" switcher
export const getUser = cache(async () => {
  const session = await verifySession()
  if (!session) return null

  try {
    const data = await db.query.users.findMany({
      where: eq(users.id, session.userId),
      // Explicitly return the columns you need rather than the whole user object
      columns: {
        id: true,
        name: true,
        email: true,
      },
    })

    const user = data[0]

    return user
  } catch (error) {
    console.log('Failed to fetch user')
    return null
  }
})
```

> **Tip**:
>
> * A DAL can be used to protect data fetched at request time. However, for static routes that share data between users, data will be fetched at build time and not at request time. Use [Proxy](#optimistic-checks-with-proxy-optional) to protect static routes.
> * For secure checks, you can check if the session is valid by comparing the session ID with your database. Use React's [cache](https://react.dev/reference/react/cache) function to avoid unnecessary duplicate requests to the database during a render pass.
> * You may wish to consolidate related data requests in a JavaScript class that runs `verifySession()` before any methods.

### Using Data Transfer Objects (DTO)

When retrieving data, it's recommended you return only the necessary data that will be used in your application, and not entire objects. For example, if you're fetching user data, you might only return the user's ID and name, rather than the entire user object which could contain passwords, phone numbers, etc.

However, if you have no control over the returned data structure, or are working in a team where you want to avoid whole objects being passed to the client, you can use strategies such as specifying what fields are safe to be exposed to the client.

```tsx filename="app/lib/dto.ts" switcher
import 'server-only'
import { getUser } from '@/app/lib/dal'

function canSeeUsername(viewer: User) {
  return true
}

function canSeePhoneNumber(viewer: User, team: string) {
  return viewer.isAdmin || team === viewer.team
}

export async function getProfileDTO(slug: string) {
  const data = await db.query.users.findMany({
    where: eq(users.slug, slug),
    // Return specific columns here
  })
  const user = data[0]

  const currentUser = await getUser(user.id)

  // Or return only what's specific to the query here
  return {
    username: canSeeUsername(currentUser) ? user.username : null,
    phonenumber: canSeePhoneNumber(currentUser, user.team)
      ? user.phonenumber
      : null,
  }
}
```

```js filename="app/lib/dto.js" switcher
import 'server-only'
import { getUser } from '@/app/lib/dal'

function canSeeUsername(viewer) {
  return true
}

function canSeePhoneNumber(viewer, team) {
  return viewer.isAdmin || team === viewer.team
}

export async function getProfileDTO(slug) {
  const data = await db.query.users.findMany({
    where: eq(users.slug, slug),
    // Return specific columns here
  })
  const user = data[0]

  const currentUser = await getUser(user.id)

  // Or return only what's specific to the query here
  return {
    username: canSeeUsername(currentUser) ? user.username : null,
    phonenumber: canSeePhoneNumber(currentUser, user.team)
      ? user.phonenumber
      : null,
  }
}
```

By centralizing your data requests and authorization logic in a DAL and using DTOs, you can ensure that all data requests are secure and consistent, making it easier to maintain, audit, and debug as your application scales.

> **Good to know**:
>
> * There are a couple of different ways you can define a DTO, from using `toJSON()`, to individual functions like the example above, or JS classes. Since these are JavaScript patterns and not a React or Next.js feature, we recommend doing some research to find the best pattern for your application.
> * Learn more about security best practices in our [Security in Next.js article](/blog/security-nextjs-server-components-actions).

### Server Components

Auth check in [Server Components](/docs/app/getting-started/server-and-client-components.md) are useful for role-based access. For example, to conditionally render components based on the user's role:

```tsx filename="app/dashboard/page.tsx" switcher
import { verifySession } from '@/app/lib/dal'

export default async function Dashboard() {
  const session = await verifySession()
  const userRole = session?.user?.role // Assuming 'role' is part of the session object

  if (userRole === 'admin') {
    return <AdminDashboard />
  } else if (userRole === 'user') {
    return <UserDashboard />
  } else {
    redirect('/login')
  }
}
```

```jsx filename="app/dashboard/page.jsx" switcher
import { verifySession } from '@/app/lib/dal'

export default async function Dashboard() {
  const session = await verifySession()
  const userRole = session?.user?.role // Assuming 'role' is part of the session object

  if (userRole === 'admin') {
    return <AdminDashboard />
  } else if (userRole === 'user') {
    return <UserDashboard />
  } else {
    redirect('/login')
  }
}
```

In the example, we use the `verifySession()` function from our DAL to check for 'admin', 'user', and unauthorized roles. This pattern ensures that each user interacts only with components appropriate to their role.

### Layouts and auth checks

Due to [Partial Rendering](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions), be cautious when doing checks in [Layouts](/docs/app/api-reference/file-conventions/layout.md) as these don't re-render on navigation, meaning the user session won't be checked on every route change.

Instead, you should do the checks close to your data source or the component that'll be conditionally rendered.

For example, consider a shared layout that fetches the user data and displays the user image in a nav. Instead of doing the auth check in the layout, you should fetch the user data (`getUser()`) in the layout and do the auth check in your DAL.

This guarantees that wherever `getUser()` is called within your application, the auth check is performed, and prevents developers forgetting to check the user is authorized to access the data.

```tsx filename="app/layout.tsx" switcher
export default async function Layout({
  children,
}: {
  children: React.ReactNode;
}) {
  const user = await getUser();

  return (
    // ...
  )
}
```

```jsx filename="app/layout.js" switcher
export default async function Layout({ children }) {
  const user = await getUser();

  return (
    // ...
  )
}
```

```ts filename="app/lib/dal.ts" switcher
export const getUser = cache(async () => {
  const session = await verifySession()
  if (!session) return null

  // Get user ID from session and fetch data
})
```

```js filename="app/lib/dal.js" switcher
export const getUser = cache(async () => {
  const session = await verifySession()
  if (!session) return null

  // Get user ID from session and fetch data
})
```

> **Good to know:**
>
> * A common pattern in SPAs is to `return null` in a layout or a top-level component if a user is not authorized. This pattern is **not recommended** since Next.js applications have multiple entry points, which will not prevent nested route segments and Server Actions from being accessed.

### Server Actions

Treat [Server Actions](/docs/app/getting-started/updating-data.md) with the same security considerations as public-facing API endpoints, and verify if the user is allowed to perform a mutation.

In the example below, we check the user's role before allowing the action to proceed:

```ts filename="app/lib/actions.ts" switcher
'use server'
import { verifySession } from '@/app/lib/dal'

export async function serverAction(formData: FormData) {
  const session = await verifySession()
  const userRole = session?.user?.role

  // Return early if user is not authorized to perform the action
  if (userRole !== 'admin') {
    return null
  }

  // Proceed with the action for authorized users
}
```

```js filename="app/lib/actions.js" switcher
'use server'
import { verifySession } from '@/app/lib/dal'

export async function serverAction() {
  const session = await verifySession()
  const userRole = session.user.role

  // Return early if user is not authorized to perform the action
  if (userRole !== 'admin') {
    return null
  }

  // Proceed with the action for authorized users
}
```

### Route Handlers

Treat [Route Handlers](/docs/app/api-reference/file-conventions/route.md) with the same security considerations as public-facing API endpoints, and verify if the user is allowed to access the Route Handler.

For example:

```ts filename="app/api/route.ts" switcher
import { verifySession } from '@/app/lib/dal'

export async function GET() {
  // User authentication and role verification
  const session = await verifySession()

  // Check if the user is authenticated
  if (!session) {
    // User is not authenticated
    return new Response(null, { status: 401 })
  }

  // Check if the user has the 'admin' role
  if (session.user.role !== 'admin') {
    // User is authenticated but does not have the right permissions
    return new Response(null, { status: 403 })
  }

  // Continue for authorized users
}
```

```js filename="app/api/route.js" switcher
import { verifySession } from '@/app/lib/dal'

export async function GET() {
  // User authentication and role verification
  const session = await verifySession()

  // Check if the user is authenticated
  if (!session) {
    // User is not authenticated
    return new Response(null, { status: 401 })
  }

  // Check if the user has the 'admin' role
  if (session.user.role !== 'admin') {
    // User is authenticated but does not have the right permissions
    return new Response(null, { status: 403 })
  }

  // Continue for authorized users
}
```

The example above demonstrates a Route Handler with a two-tier security check. It first checks for an active session, and then verifies if the logged-in user is an 'admin'.

## Context Providers

Using context providers for auth works due to [interleaving](/docs/app/getting-started/server-and-client-components.md#examples#interleaving-server-and-client-components). However, React `context` is not supported in Server Components, making them only applicable to Client Components.

This works, but any child Server Components will be rendered on the server first, and will not have access to the context provider’s session data:

```tsx filename="app/layout.ts" switcher
import { ContextProvider } from 'auth-lib'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <ContextProvider>{children}</ContextProvider>
      </body>
    </html>
  )
}
```

```tsx filename="app/ui/profile.ts switcher
'use client';

import { useSession } from "auth-lib";

export default function Profile() {
  const { userId } = useSession();
  const { data } = useSWR(`/api/user/${userId}`, fetcher)

  return (
    // ...
  );
}
```

```jsx filename="app/ui/profile.js switcher
'use client';

import { useSession } from "auth-lib";

export default function Profile() {
  const { userId } = useSession();
  const { data } = useSWR(`/api/user/${userId}`, fetcher)

  return (
    // ...
  );
}
```

If session data is needed in Client Components (e.g. for client-side data fetching), use React’s [`taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue) API to prevent sensitive session data from being exposed to the client.

## Resources

Now that you've learned about authentication in Next.js, here are Next.js-compatible libraries and resources to help you implement secure authentication and session management:

### Auth Libraries

* [Auth0](https://auth0.com/docs/quickstart/webapp/nextjs/01-login)
* [Better Auth](https://www.better-auth.com/docs/integrations/next)
* [Clerk](https://clerk.com/docs/quickstarts/nextjs)
* [Descope](https://docs.descope.com/getting-started/nextjs)
* [Kinde](https://kinde.com/docs/developer-tools/nextjs-sdk)
* [Logto](https://docs.logto.io/quick-starts/next-app-router)
* [NextAuth.js](https://authjs.dev/getting-started/installation?framework=next.js)
* [Ory](https://www.ory.sh/docs/getting-started/integrate-auth/nextjs)
* [Stack Auth](https://docs.stack-auth.com/getting-started/setup)
* [Supabase](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
* [Stytch](https://stytch.com/docs/guides/quickstarts/nextjs)
* [WorkOS](https://workos.com/docs/user-management/nextjs)

### Session Management Libraries

* [Iron Session](https://github.com/vvo/iron-session)
* [Jose](https://github.com/panva/jose)

## Further Reading

To continue learning about authentication and security, check out the following resources:

* [How to think about security in Next.js](/blog/security-nextjs-server-components-actions)
* [Understanding XSS Attacks](https://vercel.com/guides/understanding-xss-attacks)
* [Understanding CSRF Attacks](https://vercel.com/guides/understanding-csrf-attacks)
* [The Copenhagen Book](https://thecopenhagenbook.com/)


--------------------------------------------------------------------------------
title: "How to use Next.js as a backend for your frontend"
description: "Learn how to use Next.js as a backend framework"
source: "https://nextjs.org/docs/app/guides/backend-for-frontend"
--------------------------------------------------------------------------------

# Backend for Frontend

Next.js supports the "Backend for Frontend" pattern. This lets you create public endpoints to handle HTTP requests and return any content type—not just HTML. You can also access data sources and perform side effects like updating remote data.

If you are starting a new project, using `create-next-app` with the `--api` flag automatically includes an example `route.ts` in your new project’s `app/` folder, demonstrating how to create an API endpoint.

```bash filename="Terminal"
npx create-next-app@latest --api
```

> **Good to know**: Next.js backend capabilities are not a full backend replacement. They serve as an API layer that:
>
> * is publicly reachable
> * handles any HTTP request
> * can return any content type

To implement this pattern, use:

* [Route Handlers](/docs/app/api-reference/file-conventions/route.md)
* [`proxy`](/docs/app/api-reference/file-conventions/proxy.md)
* In Pages Router, [API Routes](/docs/pages/building-your-application/routing/api-routes.md)

## Public Endpoints

Route Handlers are public HTTP endpoints. Any client can access them.

Create a Route Handler using the `route.ts` or `route.js` file convention:

```ts filename="/app/api/route.ts" switcher
export function GET(request: Request) {}
```

```js filename="/app/api/route.js" switcher
export function GET(request) {}
```

This handles `GET` requests sent to `/api`.

Use `try/catch` blocks for operations that may throw an exception:

```ts filename="/app/api/route.ts" switcher
import { submit } from '@/lib/submit'

export async function POST(request: Request) {
  try {
    await submit(request)
    return new Response(null, { status: 204 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected error'

    return new Response(message, { status: 500 })
  }
}
```

```js filename="/app/api/route.js" switcher
import { submit } from '@/lib/submit'

export async function POST(request) {
  try {
    await submit(request)
    return new Response(null, { status: 204 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected error'

    return new Response(message, { status: 500 })
  }
}
```

Avoid exposing sensitive information in error messages sent to the client.

To restrict access, implement authentication and authorization. See [Authentication](/docs/app/guides/authentication.md).

## Content types

Route Handlers let you serve non-UI responses, including JSON, XML, images, files, and plain text.

Next.js uses file conventions for common endpoints:

* [`sitemap.xml`](/docs/app/api-reference/file-conventions/metadata/sitemap.md)
* [`opengraph-image.jpg`, `twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md)
* [favicon, app icon, and apple-icon](/docs/app/api-reference/file-conventions/metadata/app-icons.md)
* [`manifest.json`](/docs/app/api-reference/file-conventions/metadata/manifest.md)
* [`robots.txt`](/docs/app/api-reference/file-conventions/metadata/robots.md)

You can also define custom ones, such as:

* `llms.txt`
* `rss.xml`
* `.well-known`

For example, `app/rss.xml/route.ts` creates a Route Handler for `rss.xml`.

```ts filename="/app/rss.xml/route.ts" switcher
export async function GET(request: Request) {
  const rssResponse = await fetch(/* rss endpoint */)
  const rssData = await rssResponse.json()

  const rssFeed = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>${rssData.title}</title>
 <description>${rssData.description}</description>
 <link>${rssData.link}</link>
 <copyright>${rssData.copyright}</copyright>
 ${rssData.items.map((item) => {
   return `<item>
    <title>${item.title}</title>
    <description>${item.description}</description>
    <link>${item.link}</link>
    <pubDate>${item.publishDate}</pubDate>
    <guid isPermaLink="false">${item.guid}</guid>
 </item>`
 })}
</channel>
</rss>`

  const headers = new Headers({ 'content-type': 'application/xml' })

  return new Response(rssFeed, { headers })
}
```

```js filename="/app/rss.xml/route.js" switcher
export async function GET(request) {
  const rssResponse = await fetch(/* rss endpoint */)
  const rssData = await rssResponse.json()

  const rssFeed = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>${rssData.title}</title>
 <description>${rssData.description}</description>
 <link>${rssData.link}</link>
 <copyright>${rssData.copyright}</copyright>
 ${rssData.items.map((item) => {
   return `<item>
    <title>${item.title}</title>
    <description>${item.description}</description>
    <link>${item.link}</link>
    <pubDate>${item.publishDate}</pubDate>
    <guid isPermaLink="false">${item.guid}</guid>
 </item>`
 })}
</channel>
</rss>`

  const headers = new Headers({ 'content-type': 'application/xml' })

  return new Response(rssFeed, { headers })
}
```

Sanitize any input used to generate markup.

### Consuming request payloads

Use Request [instance methods](https://developer.mozilla.org/en-US/docs/Web/API/Request#instance_methods) like `.json()`, `.formData()`, or `.text()` to access the request body.

`GET` and `HEAD` requests don’t carry a body.

```ts filename="/app/api/echo-body/route.ts" switcher
export async function POST(request: Request) {
  const res = await request.json()
  return Response.json({ res })
}
```

```js filename="/app/api/echo-body/route.js" switcher
export async function POST(request) {
  const res = await request.json()
  return Response.json({ res })
}
```

> **Good to know**: Validate data before passing it to other systems

```ts filename="/app/api/send-email/route.ts" switcher
import { sendMail, validateInputs } from '@/lib/email-transporter'

export async function POST(request: Request) {
  const formData = await request.formData()
  const email = formData.get('email')
  const contents = formData.get('contents')

  try {
    await validateInputs({ email, contents })
    const info = await sendMail({ email, contents })

    return Response.json({ messageId: info.messageId })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

```js filename="/app/api/send-email/route.js" switcher
import { sendMail, validateInputs } from '@/lib/email-transporter'

export async function POST(request) {
  const formData = await request.formData()
  const email = formData.get('email')
  const contents = formData.get('contents')

  try {
    await validateInputs({ email, contents })
    const info = await sendMail({ email, contents })

    return Response.json({ messageId: info.messageId })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

You can only read the request body once. Clone the request if you need to read it again:

```ts filename="/app/api/clone/route.ts" switcher
export async function POST(request: Request) {
  try {
    const clonedRequest = request.clone()

    await request.body()
    await clonedRequest.body()
    await request.body() // Throws error

    return new Response(null, { status: 204 })
  } catch {
    return new Response(null, { status: 500 })
  }
}
```

```js filename="/app/api/clone/route.js" switcher
export async function POST(request) {
  try {
    const clonedRequest = request.clone()

    await request.body()
    await clonedRequest.body()
    await request.body() // Throws error

    return new Response(null, { status: 204 })
  } catch {
    return new Response(null, { status: 500 })
  }
}
```

## Manipulating data

Route Handlers can transform, filter, and aggregate data from one or more sources. This keeps logic out of the frontend and avoids exposing internal systems.

You can also offload heavy computations to the server and reduce client battery and data usage.

```ts file="/app/api/weather/route.ts" switcher
import { parseWeatherData } from '@/lib/weather'

export async function POST(request: Request) {
  const body = await request.json()
  const searchParams = new URLSearchParams({ lat: body.lat, lng: body.lng })

  try {
    const weatherResponse = await fetch(`${weatherEndpoint}?${searchParams}`)

    if (!weatherResponse.ok) {
      /* handle error */
    }

    const weatherData = await weatherResponse.text()
    const payload = parseWeatherData.asJSON(weatherData)

    return new Response(payload, { status: 200 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

```js file="/app/api/weather/route.js" switcher
import { parseWeatherData } from '@/lib/weather'

export async function POST(request) {
  const body = await request.json()
  const searchParams = new URLSearchParams({ lat: body.lat, lng: body.lng })

  try {
    const weatherResponse = await fetch(`${weatherEndpoint}?${searchParams}`)

    if (!weatherResponse.ok) {
      /* handle error */
    }

    const weatherData = await weatherResponse.text()
    const payload = parseWeatherData.asJSON(weatherData)

    return new Response(payload, { status: 200 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

> **Good to know**: This example uses `POST` to avoid putting geo-location data in the URL. `GET` requests may be cached or logged, which could expose sensitive info.

## Proxying to a backend

You can use a Route Handler as a `proxy` to another backend. Add validation logic before forwarding the request.

```ts filename="/app/api/[...slug]/route.ts" switcher
import { isValidRequest } from '@/lib/utils'

export async function POST(request: Request, { params }) {
  const clonedRequest = request.clone()
  const isValid = await isValidRequest(clonedRequest)

  if (!isValid) {
    return new Response(null, { status: 400, statusText: 'Bad Request' })
  }

  const { slug } = await params
  const pathname = slug.join('/')
  const proxyURL = new URL(pathname, 'https://nextjs.org')
  const proxyRequest = new Request(proxyURL, request)

  try {
    return fetch(proxyRequest)
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

```js filename="/app/api/[...slug]/route.js" switcher
import { isValidRequest } from '@/lib/utils'

export async function POST(request, { params }) {
  const clonedRequest = request.clone()
  const isValid = await isValidRequest(clonedRequest)

  if (!isValid) {
    return new Response(null, { status: 400, statusText: 'Bad Request' })
  }

  const { slug } = await params
  const pathname = slug.join('/')
  const proxyURL = new URL(pathname, 'https://nextjs.org')
  const proxyRequest = new Request(proxyURL, request)

  try {
    return fetch(proxyRequest)
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

Or use:

* `proxy` [rewrites](#proxy)
* [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites.md) in `next.config.js`.

## NextRequest and NextResponse

Next.js extends the [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) Web APIs with methods that simplify common operations. These extensions are available in both Route Handlers and Proxy.

Both provide methods for reading and manipulating cookies.

`NextRequest` includes the [`nextUrl`](/docs/app/api-reference/functions/next-request.md#nexturl) property, which exposes parsed values from the incoming request, for example, it makes it easier to access request pathname and search params.

`NextResponse` provides helpers like `next()`, `json()`, `redirect()`, and `rewrite()`.

You can pass `NextRequest` to any function expecting `Request`. Likewise, you can return `NextResponse` where a `Response` is expected.

```ts filename="/app/echo-pathname/route.ts" switcher
import { type NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const nextUrl = request.nextUrl

  if (nextUrl.searchParams.get('redirect')) {
    return NextResponse.redirect(new URL('/', request.url))
  }

  if (nextUrl.searchParams.get('rewrite')) {
    return NextResponse.rewrite(new URL('/', request.url))
  }

  return NextResponse.json({ pathname: nextUrl.pathname })
}
```

```js filename="/app/echo-pathname/route.js" switcher
import { NextResponse } from 'next/server'

export async function GET(request) {
  const nextUrl = request.nextUrl

  if (nextUrl.searchParams.get('redirect')) {
    return NextResponse.redirect(new URL('/', request.url))
  }

  if (nextUrl.searchParams.get('rewrite')) {
    return NextResponse.rewrite(new URL('/', request.url))
  }

  return NextResponse.json({ pathname: nextUrl.pathname })
}
```

Learn more about [`NextRequest`](/docs/app/api-reference/functions/next-request.md) and [`NextResponse`](/docs/app/api-reference/functions/next-response.md).

## Webhooks and callback URLs

Use Route Handlers to receive event notifications from third-party applications.

For example, revalidate a route when content changes in a CMS. Configure the CMS to call a specific endpoint on changes.

```ts filename="/app/webhook/route.ts" switcher
import { type NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get('token')

  if (token !== process.env.REVALIDATE_SECRET_TOKEN) {
    return NextResponse.json({ success: false }, { status: 401 })
  }

  const tag = request.nextUrl.searchParams.get('tag')

  if (!tag) {
    return NextResponse.json({ success: false }, { status: 400 })
  }

  revalidateTag(tag)

  return NextResponse.json({ success: true })
}
```

```js filename="/app/webhook/route.js" switcher
import { NextResponse } from 'next/server'

export async function GET(request) {
  const token = request.nextUrl.searchParams.get('token')

  if (token !== process.env.REVALIDATE_SECRET_TOKEN) {
    return NextResponse.json({ success: false }, { status: 401 })
  }

  const tag = request.nextUrl.searchParams.get('tag')

  if (!tag) {
    return NextResponse.json({ success: false }, { status: 400 })
  }

  revalidateTag(tag)

  return NextResponse.json({ success: true })
}
```

Callback URLs are another use case. When a user completes a third-party flow, the third party sends them to a callback URL. Use a Route Handler to verify the response and decide where to redirect the user.

```ts filename="/app/auth/callback/route.ts" switcher
import { type NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const token = request.nextUrl.searchParams.get('session_token')
  const redirectUrl = request.nextUrl.searchParams.get('redirect_url')

  const response = NextResponse.redirect(new URL(redirectUrl, request.url))

  response.cookies.set({
    value: token,
    name: '_token',
    path: '/',
    secure: true,
    httpOnly: true,
    expires: undefined, // session cookie
  })

  return response
}
```

```js filename="/app/auth/callback/route.js" switcher
import { NextResponse } from 'next/server'

export async function GET(request) {
  const token = request.nextUrl.searchParams.get('session_token')
  const redirectUrl = request.nextUrl.searchParams.get('redirect_url')

  const response = NextResponse.redirect(new URL(redirectUrl, request.url))

  response.cookies.set({
    value: token,
    name: '_token',
    path: '/',
    secure: true,
    httpOnly: true,
    expires: undefined, // session cookie
  })

  return response
}
```

## Redirects

```ts filename="app/api/route.ts" switcher
import { redirect } from 'next/navigation'

export async function GET(request: Request) {
  redirect('https://nextjs.org/')
}
```

```js filename="app/api/route.js" switcher
import { redirect } from 'next/navigation'

export async function GET(request) {
  redirect('https://nextjs.org/')
}
```

Learn more about redirects in [`redirect`](/docs/app/api-reference/functions/redirect.md) and [`permanentRedirect`](/docs/app/api-reference/functions/permanentRedirect.md)

## Proxy

Only one `proxy` file is allowed per project. Use `config.matcher` to target specific paths. Learn more about [`proxy`](/docs/app/api-reference/file-conventions/proxy.md).

Use `proxy` to generate a response before the request reaches a route path.

```ts filename="proxy.ts" switcher
import { isAuthenticated } from '@lib/auth'

export const config = {
  matcher: '/api/:function*',
}

export function proxy(request: Request) {
  if (!isAuthenticated(request)) {
    return Response.json(
      { success: false, message: 'authentication failed' },
      { status: 401 }
    )
  }
}
```

```js filename="proxy.js" switcher
import { isAuthenticated } from '@lib/auth'

export const config = {
  matcher: '/api/:function*',
}

export function proxy(request) {
  if (!isAuthenticated(request)) {
    return Response.json(
      { success: false, message: 'authentication failed' },
      { status: 401 }
    )
  }
}
```

You can also proxy requests using `proxy`:

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'

export function proxy(request: Request) {
  if (request.nextUrl.pathname === '/proxy-this-path') {
    const rewriteUrl = new URL('https://nextjs.org')
    return NextResponse.rewrite(rewriteUrl)
  }
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  if (request.nextUrl.pathname === '/proxy-this-path') {
    const rewriteUrl = new URL('https://nextjs.org')
    return NextResponse.rewrite(rewriteUrl)
  }
}
```

Another type of response `proxy` can produce are redirects:

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'

export function proxy(request: Request) {
  if (request.nextUrl.pathname === '/v1/docs') {
    request.nextUrl.pathname = '/v2/docs'
    return NextResponse.redirect(request.nextUrl)
  }
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  if (request.nextUrl.pathname === '/v1/docs') {
    request.nextUrl.pathname = '/v2/docs'
    return NextResponse.redirect(request.nextUrl)
  }
}
```

## Security

### Working with headers

Be deliberate about where headers go, and avoid directly passing incoming request headers to the outgoing response.

* **Upstream request headers**: In Proxy, `NextResponse.next({ request: { headers } })` modifies the headers your server receives and does not expose them to the client.
* **Response headers**: `new Response(..., { headers })`, `NextResponse.json(..., { headers })`, `NextResponse.next({ headers })`, or `response.headers.set(...)` send headers back to the client. If sensitive values were appended to these headers, they will be visible to clients.

Learn more in [NextResponse headers in Proxy](/docs/app/api-reference/functions/next-response.md#next).

### Rate limiting

You can implement rate limiting in your Next.js backend. In addition to code-based checks, enable any rate limiting features provided by your host.

```ts filename="/app/resource/route.ts" switcher
import { NextResponse } from 'next/server'
import { checkRateLimit } from '@/lib/rate-limit'

export async function POST(request: Request) {
  const { rateLimited } = await checkRateLimit(request)

  if (rateLimited) {
    return NextResponse.json({ error: 'Rate limit exceeded' }, { status: 429 })
  }

  return new Response(null, { status: 204 })
}
```

```js filename="/app/resource/route.js" switcher
import { NextResponse } from 'next/server'
import { checkRateLimit } from '@/lib/rate-limit'

export async function POST(request) {
  const { rateLimited } = await checkRateLimit(request)

  if (rateLimited) {
    return NextResponse.json({ error: 'Rate limit exceeded' }, { status: 429 })
  }

  return new Response(null, { status: 204 })
}
```

### Verify payloads

Never trust incoming request data. Validate content type and size, and sanitize against XSS before use.

Use timeouts to prevent abuse and protect server resources.

Store user-generated static assets in dedicated services. When possible, upload them from the browser and store the returned URI in your database to reduce request size.

### Access to protected resources

Always verify credentials before granting access. Do not rely on proxy alone for authentication and authorization.

Remove sensitive or unnecessary data from responses and backend logs.

Rotate credentials and API keys regularly.

## Preflight Requests

Preflight requests use the `OPTIONS` method to ask the server if a request is allowed based on origin, method, and headers.

If `OPTIONS` is not defined, Next.js adds it automatically and sets the `Allow` header based on the other defined methods.

* [CORS](/docs/app/api-reference/file-conventions/route.md#cors)

## Library patterns

Community libraries often use the factory pattern for Route Handlers.

```ts filename="/app/api/[...path]/route.ts"
import { createHandler } from 'third-party-library'

const handler = createHandler({
  /* library-specific options */
})

export const GET = handler
// or
export { handler as POST }
```

This creates a shared handler for `GET` and `POST` requests. The library customizes behavior based on the `method` and `pathname` in the request.

Libraries can also provide a `proxy` factory.

```ts filename="proxy.ts"
import { createMiddleware } from 'third-party-library'

export default createMiddleware()
```

> **Good to know**: Third-party libraries may still refer to `proxy` as `middleware`.

## More examples

See more examples on using [Router Handlers](/docs/app/api-reference/file-conventions/route.md#examples) and the [`proxy`](/docs/app/api-reference/file-conventions/proxy.md#examples) API references.

These examples include, working with [Cookies](/docs/app/api-reference/file-conventions/route.md#cookies), [Headers](/docs/app/api-reference/file-conventions/route.md#headers), [Streaming](/docs/app/api-reference/file-conventions/route.md#streaming), Proxy [negative matching](/docs/app/api-reference/file-conventions/proxy.md#negative-matching), and other useful code snippets.

## Caveats

### Server Components

Fetch data in Server Components directly from its source, not via Route Handlers.

For Server Components pre-rendered at build time, using Route Handlers will fail the build step. This is because, while building there is no server listening for these requests.

For Server Components rendered on demand, fetching from Route Handlers is slower due to the extra HTTP round trip between the handler and the render process.

> A server side `fetch` request uses absolute URLs. This implies an HTTP round trip, to an external server. During development, your own development server acts as the external server. At build time there is no server, and at runtime, the server is available through your public facing domain.

Server Components cover most data-fetching needs. However, fetching data client side might be necessary for:

* Data that depends on client-only Web APIs:
  * Geo-location API
  * Storage API
  * Audio API
  * File API
* Frequently polled data

For these, use community libraries like [`swr`](https://swr.vercel.app/) or [`react-query`](https://tanstack.com/query/latest/docs/framework/react/overview).

### Server Actions

Server Actions let you run server-side code from the client. Their primary purpose is to mutate data from your frontend client.

Server Actions are queued. Using them for data fetching introduces sequential execution.

### `export` mode

`export` mode outputs a static site without a runtime server. Features that require the Next.js runtime are [not supported](/docs/app/guides/static-exports.md#unsupported-features), because this mode produces a static site, and no runtime server.

In `export mode`, only `GET` Route Handlers are supported, in combination with the [`dynamic`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamic) route segment config, set to `'force-static'`.

This can be used to generate static HTML, JSON, TXT, or other files.

```js filename="app/hello-world/route.ts"
export const dynamic = 'force-static'

export function GET() {
  return new Response('Hello World', { status: 200 })
}
```

### Deployment environment

Some hosts deploy Route Handlers as lambda functions. This means:

* Route Handlers cannot share data between requests.
* The environment may not support writing to File System.
* Long-running handlers may be terminated due to timeouts.
* WebSockets won’t work because the connection closes on timeout, or after the response is generated.
## API Reference

Learn more about Route Handlers and Proxy

- [route.js](/docs/app/api-reference/file-conventions/route.md)
  - API reference for the route.js special file.
- [proxy.js](/docs/app/api-reference/file-conventions/proxy.md)
  - API reference for the proxy.js file.


--------------------------------------------------------------------------------
title: "Caching in Next.js"
description: "An overview of caching mechanisms in Next.js."
source: "https://nextjs.org/docs/app/guides/caching"
--------------------------------------------------------------------------------

# Caching

Next.js improves your application's performance and reduces costs by caching rendering work and data requests. This page provides an in-depth look at Next.js caching mechanisms, the APIs you can use to configure them, and how they interact with each other.

> **Good to know**: This page helps you understand how Next.js works under the hood but is **not** essential knowledge to be productive with Next.js. Most of Next.js' caching heuristics are determined by your API usage and have defaults for the best performance with zero or minimal configuration. If you instead want to jump to examples, [start here](/docs/app/getting-started/fetching-data.md).

## Overview

Here's a high-level overview of the different caching mechanisms and their purpose:

| Mechanism                                   | What                       | Where  | Purpose                                         | Duration                        |
| ------------------------------------------- | -------------------------- | ------ | ----------------------------------------------- | ------------------------------- |
| [Request Memoization](#request-memoization) | Return values of functions | Server | Re-use data in a React Component tree           | Per-request lifecycle           |
| [Data Cache](#data-cache)                   | Data                       | Server | Store data across user requests and deployments | Persistent (can be revalidated) |
| [Full Route Cache](#full-route-cache)       | HTML and RSC payload       | Server | Reduce rendering cost and improve performance   | Persistent (can be revalidated) |
| [Router Cache](#client-side-router-cache)   | RSC Payload                | Client | Reduce server requests on navigation            | User session or time-based      |

By default, Next.js will cache as much as possible to improve performance and reduce cost. This means routes are **statically rendered** and data requests are **cached** unless you opt out. The diagram below shows the default caching behavior: when a route is statically rendered at build time and when a static route is first visited.

![Diagram showing the default caching behavior in Next.js for the four mechanisms, with HIT, MISS and SET at build time and when a route is first visited.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/caching-overview.png)

Caching behavior changes depending on whether the route is statically or dynamically rendered, data is cached or uncached, and whether a request is part of an initial visit or a subsequent navigation. Depending on your use case, you can configure the caching behavior for individual routes and data requests.

Fetch caching is **not** supported in `proxy`. Any fetches done inside of your `proxy` will be uncached.

## Rendering Strategies

To understand how caching works in Next.js, it's helpful to understand the rendering strategies available. The rendering strategy determines when your route's HTML is generated, which directly impacts what can be cached.

### Static Rendering

With Static Rendering, routes are rendered at **build time** or in the background after [data revalidation](/docs/app/guides/incremental-static-regeneration.md). The result is cached and can be reused across requests. Static routes are fully cached in the [Full Route Cache](#full-route-cache).

### Dynamic Rendering

With Dynamic Rendering, routes are rendered at **request time**. This happens when your route uses request-specific information like cookies, headers, or search params.

A route becomes dynamic when it uses any of these APIs:

* [`cookies`](/docs/app/api-reference/functions/cookies.md)
* [`headers`](/docs/app/api-reference/functions/headers.md)
* [`connection`](/docs/app/api-reference/functions/connection.md)
* [`draftMode`](/docs/app/api-reference/functions/draft-mode.md)
* [`searchParams` prop](/docs/app/api-reference/file-conventions/page.md#searchparams-optional)
* [`unstable_noStore`](/docs/app/api-reference/functions/unstable_noStore.md)
* [`fetch`](/docs/app/api-reference/functions/fetch.md) with `{ cache: 'no-store' }`

Dynamic routes are not cached in the Full Route Cache, but can still use the [Data Cache](#data-cache) for data requests.

> **Good to know**: You can use [Cache Components](/docs/app/getting-started/cache-components.md) to mix static and dynamic rendering within the same route.

## Request Memoization

Next.js extends the [`fetch` API](#fetch) to automatically **memoize** requests that have the same URL and options. This means you can call a fetch function for the same data in multiple places in a React component tree while only executing it once.

![Deduplicated Fetch Requests](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/deduplicated-fetch-requests.png)

For example, if you need to use the same data across a route (e.g. in a Layout, Page, and multiple components), you do not have to fetch data at the top of the tree, and forward props between components. Instead, you can fetch data in the components that need it without worrying about the performance implications of making multiple requests across the network for the same data.

```tsx filename="app/example.tsx" switcher
async function getItem() {
  // The `fetch` function is automatically memoized and the result
  // is cached
  const res = await fetch('https://.../item/1')
  return res.json()
}

// This function is called twice, but only executed the first time
const item = await getItem() // cache MISS

// The second call could be anywhere in your route
const item = await getItem() // cache HIT
```

```jsx filename="app/example.js" switcher
async function getItem() {
  // The `fetch` function is automatically memoized and the result
  // is cached
  const res = await fetch('https://.../item/1')
  return res.json()
}

// This function is called twice, but only executed the first time
const item = await getItem() // cache MISS

// The second call could be anywhere in your route
const item = await getItem() // cache HIT
```

**How Request Memoization Works**

![Diagram showing how fetch memoization works during React rendering.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/request-memoization.png)

* While rendering a route, the first time a particular request is called, its result will not be in memory and it'll be a cache `MISS`.
* Therefore, the function will be executed, and the data will be fetched from the external source, and the result will be stored in memory.
* Subsequent function calls of the request in the same render pass will be a cache `HIT`, and the data will be returned from memory without executing the function.
* Once the route has been rendered and the rendering pass is complete, memory is "reset" and all request memoization entries are cleared.

> **Good to know**:
>
> * Request memoization is a React feature, not a Next.js feature. It's included here to show how it interacts with the other caching mechanisms.
> * Memoization only applies to the `GET` method in `fetch` requests.
> * Memoization only applies to the React Component tree, this means:
>   * It applies to `fetch` requests in `generateMetadata`, `generateStaticParams`, Layouts, Pages, and other Server Components.
>   * It doesn't apply to `fetch` requests in Route Handlers as they are not a part of the React component tree.
> * For cases where `fetch` is not suitable (e.g. some database clients, CMS clients, or GraphQL clients), you can use the [React `cache` function](#react-cache-function) to memoize functions.

### Duration

The cache lasts the lifetime of a server request until the React component tree has finished rendering.

### Revalidating

Since the memoization is not shared across server requests and only applies during rendering, there is no need to revalidate it.

### Opting out

Memoization only applies to the `GET` method in `fetch` requests, other methods, such as `POST` and `DELETE`, are not memoized. This default behavior is a React optimization and we do not recommend opting out of it.

To manage individual requests, you can use the [`signal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/signal) property from [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController).

```js filename="app/example.js"
const { signal } = new AbortController()
fetch(url, { signal })
```

## Data Cache

Next.js has a built-in Data Cache that **persists** the result of data fetches across incoming **server requests** and **deployments**. This is possible because Next.js extends the native `fetch` API to allow each request on the server to set its own persistent caching semantics.

> **Good to know**: In the browser, the `cache` option of `fetch` indicates how a request will interact with the browser's HTTP cache, in Next.js, the `cache` option indicates how a server-side request will interact with the server's Data Cache.

You can use the [`cache`](#fetch-optionscache) and [`next.revalidate`](#fetch-optionsnextrevalidate) options of `fetch` to configure the caching behavior.

In development mode, `fetch` data is [reused for Hot Module Replacement (HMR)](/docs/app/api-reference/functions/fetch.md#fetch-default-auto-no-store-and-cache-no-store-not-showing-fresh-data-in-development), and caching options are ignored for [hard refreshes](/docs/app/api-reference/functions/fetch.md#hard-refresh-and-caching-in-development).

**How the Data Cache Works**

![Diagram showing how cached and uncached fetch requests interact with the Data Cache. Cached requests are stored in the Data Cache, and memoized, uncached requests are fetched from the data source, not stored in the Data Cache, and memoized.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/data-cache.png)

* The first time a `fetch` request with the `'force-cache'` option is called during rendering, Next.js checks the Data Cache for a cached response.
* If a cached response is found, it's returned immediately and [memoized](#request-memoization).
* If a cached response is not found, the request is made to the data source, the result is stored in the Data Cache, and memoized.
* For uncached data (e.g. no `cache` option defined or using `{ cache: 'no-store' }`), the result is always fetched from the data source, and memoized.
* Whether the data is cached or uncached, the requests are always memoized to avoid making duplicate requests for the same data during a React render pass.

> **Differences between the Data Cache and Request Memoization**
>
> While both caching mechanisms help improve performance by re-using cached data, the Data Cache is persistent across incoming requests and deployments, whereas memoization only lasts the lifetime of a request.

### Duration

The Data Cache is persistent across incoming requests and deployments unless you revalidate or opt-out.

### Revalidating

Cached data can be revalidated in two ways, with:

* **Time-based Revalidation**: Revalidate data after a certain amount of time has passed and a new request is made. This is useful for data that changes infrequently and freshness is not as critical.
* **On-demand Revalidation:** Revalidate data based on an event (e.g. form submission). On-demand revalidation can use a tag-based or path-based approach to revalidate groups of data at once. This is useful when you want to ensure the latest data is shown as soon as possible (e.g. when content from your headless CMS is updated).

#### Time-based Revalidation

To revalidate data at a timed interval, you can use the `next.revalidate` option of `fetch` to set the cache lifetime of a resource (in seconds).

```js
// Revalidate at most every hour
fetch('https://...', { next: { revalidate: 3600 } })
```

Alternatively, you can use [Route Segment Config options](#segment-config-options) to configure all `fetch` requests in a segment or for cases where you're not able to use `fetch`.

**How Time-based Revalidation Works**

![Diagram showing how time-based revalidation works, after the revalidation period, stale data is returned for the first request, then data is revalidated.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/time-based-revalidation.png)

* The first time a fetch request with `revalidate` is called, the data will be fetched from the external data source and stored in the Data Cache.
* Any requests that are called within the specified timeframe (e.g. 60-seconds) will return the cached data.
* After the timeframe, the next request will still return the cached (now stale) data.
  * Next.js will trigger a revalidation of the data in the background.
  * Once the data is fetched successfully, Next.js will update the Data Cache with the fresh data.
  * If the background revalidation fails, the previous data will be kept unaltered.

This is similar to [**stale-while-revalidate**](https://web.dev/articles/stale-while-revalidate) behavior.

#### On-demand Revalidation

Data can be revalidated on-demand by path ([`revalidatePath`](#revalidatepath)) or by cache tag ([`revalidateTag`](#fetch-optionsnexttags-and-revalidatetag)).

**How On-Demand Revalidation Works**

![Diagram showing how on-demand revalidation works, the Data Cache is updated with fresh data after a revalidation request.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/on-demand-revalidation.png)

* The first time a `fetch` request is called, the data will be fetched from the external data source and stored in the Data Cache.
* When an on-demand revalidation is triggered, the appropriate cache entries will be purged from the cache.
  * This is different from time-based revalidation, which keeps the stale data in the cache until the fresh data is fetched.
* The next time a request is made, it will be a cache `MISS` again, and the data will be fetched from the external data source and stored in the Data Cache.

### Opting out

If you do *not* want to cache the response from `fetch`, you can do the following:

```js
let data = await fetch('https://api.vercel.app/blog', { cache: 'no-store' })
```

## Full Route Cache

> **Related terms**:
>
> You may see the terms **Automatic Static Optimization**, **Static Site Generation**, or **Static Rendering** being used interchangeably to refer to the process of rendering and caching routes of your application at build time.

Next.js automatically renders and caches routes at build time. This is an optimization that allows you to serve the cached route instead of rendering on the server for every request, resulting in faster page loads.

To understand how the Full Route Cache works, it's helpful to look at how React handles rendering, and how Next.js caches the result:

### 1. React Rendering on the Server

On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks: by individual routes segments and Suspense boundaries.

Each chunk is rendered in two steps:

1. React renders Server Components into a special data format, optimized for streaming, called the **React Server Component Payload**.
2. Next.js uses the React Server Component Payload and Client Component JavaScript instructions to render **HTML** on the server.

This means we don't have to wait for everything to render before caching the work or sending a response. Instead, we can stream a response as work is completed.

> **What is the React Server Component Payload?**
>
> The React Server Component Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The React Server Component Payload contains:
>
> * The rendered result of Server Components
> * Placeholders for where Client Components should be rendered and references to their JavaScript files
> * Any props passed from a Server Component to a Client Component
>
> To learn more, see the [Server Components](/docs/app/getting-started/server-and-client-components.md) documentation.

### 2. Next.js Caching on the Server (Full Route Cache)

![Default behavior of the Full Route Cache, showing how the React Server Component Payload and HTML are cached on the server for statically rendered routes.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/full-route-cache.png)

The default behavior of Next.js is to cache the rendered result (React Server Component Payload and HTML) of a route on the server. This applies to statically rendered routes at build time, or during revalidation.

### 3. React Hydration and Reconciliation on the Client

At request time, on the client:

1. The HTML is used to immediately show a fast non-interactive initial preview of the Client and Server Components.
2. The React Server Components Payload is used to reconcile the Client and rendered Server Component trees, and update the DOM.
3. The JavaScript instructions are used to [hydrate](https://react.dev/reference/react-dom/client/hydrateRoot) Client Components and make the application interactive.

### 4. Next.js Caching on the Client (Router Cache)

The React Server Component Payload is stored in the client-side [Router Cache](#client-side-router-cache) - a separate in-memory cache, split by individual route segment. This Router Cache is used to improve the navigation experience by storing previously visited routes and prefetching future routes.

### 5. Subsequent Navigations

On subsequent navigations or during prefetching, Next.js will check if the React Server Components Payload is stored in the Router Cache. If so, it will skip sending a new request to the server.

If the route segments are not in the cache, Next.js will fetch the React Server Components Payload from the server, and populate the Router Cache on the client.

### Static and Dynamic Rendering

Whether a route is cached or not at build time depends on whether it's statically or dynamically rendered. Static routes are cached by default, whereas dynamic routes are rendered at request time, and not cached.

This diagram shows the difference between statically and dynamically rendered routes, with cached and uncached data:

![How static and dynamic rendering affects the Full Route Cache. Static routes are cached at build time or after data revalidation, whereas dynamic routes are never cached](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/static-and-dynamic-routes.png)

Learn more about [static and dynamic rendering](#rendering-strategies).

### Duration

By default, the Full Route Cache is persistent. This means that the render output is cached across user requests.

### Invalidation

There are two ways you can invalidate the Full Route Cache:

* **[Revalidating Data](/docs/app/guides/caching.md#revalidating)**: Revalidating the [Data Cache](#data-cache), will in turn invalidate the Router Cache by re-rendering components on the server and caching the new render output.
* **Redeploying**: Unlike the Data Cache, which persists across deployments, the Full Route Cache is cleared on new deployments.

### Opting out

You can opt out of the Full Route Cache, or in other words, dynamically render components for every incoming request, by:

* **Using a [Dynamic API](#dynamic-apis)**: This will opt the route out from the Full Route Cache and dynamically render it at request time. The Data Cache can still be used.
* **Using the `dynamic = 'force-dynamic'` or `revalidate = 0` route segment config options**: This will skip the Full Route Cache and the Data Cache. Meaning components will be rendered and data fetched on every incoming request to the server. The Router Cache will still apply as it's a client-side cache.
* **Opting out of the [Data Cache](#data-cache)**: If a route has a `fetch` request that is not cached, this will opt the route out of the Full Route Cache. The data for the specific `fetch` request will be fetched for every incoming request. Other `fetch` requests that explicitly enable caching will still be cached in the Data Cache. This allows for a hybrid of cached and uncached data.

## Client-side Router Cache

Next.js has an in-memory client-side router cache that stores the RSC payload of route segments, split by layouts, loading states, and pages.

When a user navigates between routes, Next.js caches the visited route segments and [prefetches](/docs/app/getting-started/linking-and-navigating.md#prefetching) the routes the user is likely to navigate to. This results in instant back/forward navigation, no full-page reload between navigations, and preservation of browser state and React state in shared layouts.

With the Router Cache:

* **Layouts** are cached and reused on navigation ([partial rendering](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions)).
* **Loading states** are cached and reused on navigation for [instant navigation](/docs/app/api-reference/file-conventions/loading.md#instant-loading-states).
* **Pages** are not cached by default, but are reused during browser backward and forward navigation. You can enable caching for page segments by using the experimental [`staleTimes`](/docs/app/api-reference/config/next-config-js/staleTimes.md) config option.

> **Good to know:** This cache specifically applies to Next.js and Server Components, and is different to the browser's [bfcache](https://web.dev/bfcache/), though it has a similar result.

### Duration

The cache is stored in the browser's temporary memory. Two factors determine how long the router cache lasts:

* **Session**: The cache persists across navigation. However, it's cleared on page refresh.
* **Automatic Invalidation Period**: The cache of layouts and loading states is automatically invalidated after a specific time. The duration depends on how the resource was [prefetched](/docs/app/api-reference/components/link.md#prefetch), and if the resource was [statically generated](#static-rendering):
  * **Default Prefetching** (`prefetch={null}` or unspecified): not cached for dynamic pages, 5 minutes for static pages.
  * **Full Prefetching** (`prefetch={true}` or `router.prefetch`): 5 minutes for both static & dynamic pages.

While a page refresh will clear **all** cached segments, the automatic invalidation period only affects the individual segment from the time it was prefetched.

> **Good to know**: The experimental [`staleTimes`](/docs/app/api-reference/config/next-config-js/staleTimes.md) config option can be used to adjust the automatic invalidation times mentioned above.

### Invalidation

There are two ways you can invalidate the Router Cache:

* In a **Server Action**:
  * Revalidating data on-demand by path with ([`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md)) or by cache tag with ([`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md))
  * Using [`cookies.set`](/docs/app/api-reference/functions/cookies.md#setting-a-cookie) or [`cookies.delete`](/docs/app/api-reference/functions/cookies.md#deleting-cookies) invalidates the Router Cache to prevent routes that use cookies from becoming stale (e.g. authentication).
* Calling [`router.refresh`](/docs/app/api-reference/functions/use-router.md) will invalidate the Router Cache and make a new request to the server for the current route.

### Opting out

As of Next.js 15, page segments are opted out by default.

> **Good to know:** You can also opt out of [prefetching](/docs/app/getting-started/linking-and-navigating.md#prefetching) by setting the `prefetch` prop of the `<Link>` component to `false`.

## Cache Interactions

When configuring the different caching mechanisms, it's important to understand how they interact with each other:

### Data Cache and Full Route Cache

* Revalidating or opting out of the Data Cache **will** invalidate the Full Route Cache, as the render output depends on data.
* Invalidating or opting out of the Full Route Cache **does not** affect the Data Cache. You can dynamically render a route that has both cached and uncached data. This is useful when most of your page uses cached data, but you have a few components that rely on data that needs to be fetched at request time. You can dynamically render without worrying about the performance impact of re-fetching all the data.

### Data Cache and Client-side Router cache

* To immediately invalidate the Data Cache and Router cache, you can use [`revalidatePath`](#revalidatepath) or [`revalidateTag`](#fetch-optionsnexttags-and-revalidatetag) in a [Server Action](/docs/app/getting-started/updating-data.md).
* Revalidating the Data Cache in a [Route Handler](/docs/app/api-reference/file-conventions/route.md) **will not** immediately invalidate the Router Cache as the Route Handler isn't tied to a specific route. This means Router Cache will continue to serve the previous payload until a hard refresh, or the automatic invalidation period has elapsed.

## APIs

The following table provides an overview of how different Next.js APIs affect caching:

| API                                                                     | Router Cache               | Full Route Cache      | Data Cache            | React Cache          |
| ----------------------------------------------------------------------- | -------------------------- | --------------------- | --------------------- | -------------------- |
| [`<Link prefetch>`](#link)                                              | Cache                      |                       |                       |                      |
| [`router.prefetch`](#routerprefetch)                                    | Cache                      |                       |                       |                      |
| [`router.refresh`](#routerrefresh)                                      | Revalidate                 |                       |                       |                      |
| [`fetch`](#fetch)                                                       |                            |                       | Cache                 | Cache (GET and HEAD) |
| [`fetch` `options.cache`](#fetch-optionscache)                          |                            |                       | Cache or Opt out      |                      |
| [`fetch` `options.next.revalidate`](#fetch-optionsnextrevalidate)       |                            | Revalidate            | Revalidate            |                      |
| [`fetch` `options.next.tags`](#fetch-optionsnexttags-and-revalidatetag) |                            | Cache                 | Cache                 |                      |
| [`revalidateTag`](#fetch-optionsnexttags-and-revalidatetag)             | Revalidate (Server Action) | Revalidate            | Revalidate            |                      |
| [`revalidatePath`](#revalidatepath)                                     | Revalidate (Server Action) | Revalidate            | Revalidate            |                      |
| [`const revalidate`](#segment-config-options)                           |                            | Revalidate or Opt out | Revalidate or Opt out |                      |
| [`const dynamic`](#segment-config-options)                              |                            | Cache or Opt out      | Cache or Opt out      |                      |
| [`cookies`](#cookies)                                                   | Revalidate (Server Action) | Opt out               |                       |                      |
| [`headers`, `searchParams`](#dynamic-apis)                              |                            | Opt out               |                       |                      |
| [`generateStaticParams`](#generatestaticparams)                         |                            | Cache                 |                       |                      |
| [`React.cache`](#react-cache-function)                                  |                            |                       |                       | Cache                |
| [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache.md)    |                            |                       | Cache                 |                      |

### `<Link>`

By default, the `<Link>` component automatically prefetches routes from the Full Route Cache and adds the React Server Component Payload to the Router Cache.

To disable prefetching, you can set the `prefetch` prop to `false`. But this will not skip the cache permanently, the route segment will still be cached client-side when the user visits the route.

Learn more about the [`<Link>` component](/docs/app/api-reference/components/link.md).

### `router.prefetch`

The `prefetch` option of the `useRouter` hook can be used to manually prefetch a route. This adds the React Server Component Payload to the Router Cache.

See the [`useRouter` hook](/docs/app/api-reference/functions/use-router.md) API reference.

### `router.refresh`

The `refresh` option of the `useRouter` hook can be used to manually refresh a route. This completely clears the Router Cache, and makes a new request to the server for the current route. `refresh` does not affect the Data or Full Route Cache.

The rendered result will be reconciled on the client while preserving React state and browser state.

See the [`useRouter` hook](/docs/app/api-reference/functions/use-router.md) API reference.

### `fetch`

Data returned from `fetch` is *not* automatically cached in the Data Cache.

By default, when no `cache` or `next.revalidate` options are provided:

* [Dynamic rendering](#dynamic-rendering): Fetch runs on every request and always returns fresh data.
* [Static rendering](#static-rendering): Fetched data is stored in the [Data Cache](#data-cache), and the rendered output in the [Full Route Cache](#full-route-cache). Next.js serves this cached result until the path is revalidated.

See the [`fetch` API Reference](/docs/app/api-reference/functions/fetch.md) for more options.

### `fetch options.cache`

You can opt individual `fetch` into caching by setting the `cache` option to `force-cache`:

```jsx
// Opt into caching
fetch(`https://...`, { cache: 'force-cache' })
```

See the [`fetch` API Reference](/docs/app/api-reference/functions/fetch.md) for more options.

### `fetch options.next.revalidate`

You can use the `next.revalidate` option of `fetch` to set the revalidation period (in seconds) of an individual `fetch` request. This will revalidate the Data Cache, which in turn will revalidate the Full Route Cache. Fresh data will be fetched, and components will be re-rendered on the server.

```jsx
// Revalidate at most after 1 hour
fetch(`https://...`, { next: { revalidate: 3600 } })
```

See the [`fetch` API reference](/docs/app/api-reference/functions/fetch.md) for more options.

### `fetch options.next.tags` and `revalidateTag`

Next.js has a cache tagging system for fine-grained data caching and revalidation.

1. When using `fetch` or [`unstable_cache`](/docs/app/api-reference/functions/unstable_cache.md), you have the option to tag cache entries with one or more tags.
2. Then, you can call `revalidateTag` to purge the cache entries associated with that tag.

For example, you can set a tag when fetching data:

```jsx
// Cache data with a tag
fetch(`https://...`, { next: { tags: ['a', 'b', 'c'] } })
```

Then, call `revalidateTag` with a tag to purge the cache entry:

```jsx
// Revalidate entries with a specific tag
revalidateTag('a')
```

There are two places you can use `revalidateTag`, depending on what you're trying to achieve:

1. [Route Handlers](/docs/app/api-reference/file-conventions/route.md) - to revalidate data in response of a third party event (e.g. webhook). This will not invalidate the Router Cache immediately as the Router Handler isn't tied to a specific route.
2. [Server Actions](/docs/app/getting-started/updating-data.md) - to revalidate data after a user action (e.g. form submission). This will invalidate the Router Cache for the associated route.

### `revalidatePath`

`revalidatePath` allows you manually revalidate data **and** re-render the route segments below a specific path in a single operation. Calling the `revalidatePath` method revalidates the Data Cache, which in turn invalidates the Full Route Cache.

```jsx
revalidatePath('/')
```

There are two places you can use `revalidatePath`, depending on what you're trying to achieve:

1. [Route Handlers](/docs/app/api-reference/file-conventions/route.md) - to revalidate data in response to a third party event (e.g. webhook).
2. [Server Actions](/docs/app/getting-started/updating-data.md) - to revalidate data after a user interaction (e.g. form submission, clicking a button).

See the [`revalidatePath` API reference](/docs/app/api-reference/functions/revalidatePath.md) for more information.

> **`revalidatePath`** vs. **`router.refresh`**:
>
> Calling `router.refresh` will clear the Router cache, and re-render route segments on the server without invalidating the Data Cache or the Full Route Cache.
>
> The difference is that `revalidatePath` purges the Data Cache and Full Route Cache, whereas `router.refresh()` does not change the Data Cache and Full Route Cache, as it is a client-side API.

### Dynamic APIs

Dynamic APIs like `cookies` and `headers`, and the `searchParams` prop in Pages depend on runtime incoming request information. Using them will opt a route out of the Full Route Cache, in other words, the route will be dynamically rendered.

#### `cookies`

Using `cookies.set` or `cookies.delete` in a Server Action invalidates the Router Cache to prevent routes that use cookies from becoming stale (e.g. to reflect authentication changes).

See the [`cookies`](/docs/app/api-reference/functions/cookies.md) API reference.

### Segment Config Options

The Route Segment Config options can be used to override the route segment defaults or when you're not able to use the `fetch` API (e.g. database client or 3rd party libraries).

The following Route Segment Config options will opt out of the Full Route Cache:

* `const dynamic = 'force-dynamic'`

This config option will opt all fetches out of the Data Cache (i.e. `no-store`):

* `const fetchCache = 'default-no-store'`

See the [`fetchCache`](/docs/app/api-reference/file-conventions/route-segment-config.md#fetchcache) to see more advanced options.

See the [Route Segment Config](/docs/app/api-reference/file-conventions/route-segment-config.md) documentation for more options.

### `generateStaticParams`

For [dynamic segments](/docs/app/api-reference/file-conventions/dynamic-routes.md) (e.g. `app/blog/[slug]/page.js`), paths provided by `generateStaticParams` are cached in the Full Route Cache at build time. At request time, Next.js will also cache paths that weren't known at build time the first time they're visited.

To statically render all paths at build time, supply the full list of paths to `generateStaticParams`:

```jsx filename="app/blog/[slug]/page.js"
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

To statically render a subset of paths at build time, and the rest the first time they're visited at runtime, return a partial list of paths:

```jsx filename="app/blog/[slug]/page.js"
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  // Render the first 10 posts at build time
  return posts.slice(0, 10).map((post) => ({
    slug: post.slug,
  }))
}
```

To statically render all paths the first time they're visited, return an empty array (no paths will be rendered at build time) or utilize [`export const dynamic = 'force-static'`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamic):

```jsx filename="app/blog/[slug]/page.js"
export async function generateStaticParams() {
  return []
}
```

> **Good to know:** You must return an array from `generateStaticParams`, even if it's empty. Otherwise, the route will be dynamically rendered.

```jsx filename="app/changelog/[slug]/page.js"
export const dynamic = 'force-static'
```

To disable caching at request time, add the `export const dynamicParams = false` option in a route segment. When this config option is used, only paths provided by `generateStaticParams` will be served, and other routes will 404 or match (in the case of [catch-all routes](/docs/app/api-reference/file-conventions/dynamic-routes.md#catch-all-segments)).

### React `cache` function

The React `cache` function allows you to memoize the return value of a function, allowing you to call the same function multiple times while only executing it once.

`fetch` requests using the `GET` or `HEAD` methods are automatically memoized, so you do not need to wrap it in React `cache`. However, for other `fetch` methods, or when using data fetching libraries (such as some database, CMS, or GraphQL clients) that don't inherently memoize requests, you can use `cache` to manually memoize data requests.

```ts filename="utils/get-item.ts" switcher
import { cache } from 'react'
import db from '@/lib/db'

export const getItem = cache(async (id: string) => {
  const item = await db.item.findUnique({ id })
  return item
})
```

```js filename="utils/get-item.js" switcher
import { cache } from 'react'
import db from '@/lib/db'

export const getItem = cache(async (id) => {
  const item = await db.item.findUnique({ id })
  return item
})
```


--------------------------------------------------------------------------------
title: "How to configure Continuous Integration (CI) build caching"
description: "Learn how to configure CI to cache Next.js builds"
source: "https://nextjs.org/docs/app/guides/ci-build-caching"
--------------------------------------------------------------------------------

# CI Build Caching

To improve build performance, Next.js saves a cache to `.next/cache` that is shared between builds.

To take advantage of this cache in Continuous Integration (CI) environments, your CI workflow will need to be configured to correctly persist the cache between builds.

> If your CI is not configured to persist `.next/cache` between builds, you may see a [No Cache Detected](/docs/messages/no-cache.md) error.

Here are some example cache configurations for common CI providers:

## Vercel

Next.js caching is automatically configured for you. There's no action required on your part. If you are using Turborepo on Vercel, [learn more here](https://vercel.com/docs/monorepos/turborepo).

## CircleCI

Edit your `save_cache` step in `.circleci/config.yml` to include `.next/cache`:

```yaml
steps:
  - save_cache:
      key: dependency-cache-{{ checksum "yarn.lock" }}
      paths:
        - ./node_modules
        - ./.next/cache
```

If you do not have a `save_cache` key, please follow CircleCI's [documentation on setting up build caching](https://circleci.com/docs/2.0/caching/).

## Travis CI

Add or merge the following into your `.travis.yml`:

```yaml
cache:
  directories:
    - $HOME/.cache/yarn
    - node_modules
    - .next/cache
```

## GitLab CI

Add or merge the following into your `.gitlab-ci.yml`:

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .next/cache/
```

## Netlify CI

Use [Netlify Plugins](https://www.netlify.com/products/build/plugins/) with [`@netlify/plugin-nextjs`](https://www.npmjs.com/package/@netlify/plugin-nextjs).

## AWS CodeBuild

Add (or merge in) the following to your `buildspec.yml`:

```yaml
cache:
  paths:
    - 'node_modules/**/*' # Cache `node_modules` for faster `yarn` or `npm i`
    - '.next/cache/**/*' # Cache Next.js for faster application rebuilds
```

## GitHub Actions

Using GitHub's [actions/cache](https://github.com/actions/cache), add the following step in your workflow file:

```yaml
uses: actions/cache@v4
with:
  # See here for caching with `yarn`, `bun` or other package managers https://github.com/actions/cache/blob/main/examples.md or you can leverage caching with actions/setup-node https://github.com/actions/setup-node
  path: |
    ~/.npm
    ${{ github.workspace }}/.next/cache
  # Generate a new cache whenever packages or source files change.
  key: ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-${{ hashFiles('**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx') }}
  # If source files changed but packages didn't, rebuild from a prior cache.
  restore-keys: |
    ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-
```

## Bitbucket Pipelines

Add or merge the following into your `bitbucket-pipelines.yml` at the top level (same level as `pipelines`):

```yaml
definitions:
  caches:
    nextcache: .next/cache
```

Then reference it in the `caches` section of your pipeline's `step`:

```yaml
- step:
    name: your_step_name
    caches:
      - node
      - nextcache
```

## Heroku

Using Heroku's [custom cache](https://devcenter.heroku.com/articles/nodejs-support#custom-caching), add a `cacheDirectories` array in your top-level package.json:

```javascript
"cacheDirectories": [".next/cache"]
```

## Azure Pipelines

Using Azure Pipelines' [Cache task](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/cache), add the following task to your pipeline yaml file somewhere prior to the task that executes `next build`:

```yaml
- task: Cache@2
  displayName: 'Cache .next/cache'
  inputs:
    key: next | $(Agent.OS) | yarn.lock
    path: '$(System.DefaultWorkingDirectory)/.next/cache'
```

## Jenkins (Pipeline)

Using Jenkins' [Job Cacher](https://www.jenkins.io/doc/pipeline/steps/jobcacher/) plugin, add the following build step to your `Jenkinsfile` where you would normally run `next build` or `npm install`:

```yaml
stage("Restore npm packages") {
    steps {
        // Writes lock-file to cache based on the GIT_COMMIT hash
        writeFile file: "next-lock.cache", text: "$GIT_COMMIT"

        cache(caches: [
            arbitraryFileCache(
                path: "node_modules",
                includes: "**/*",
                cacheValidityDecidingFile: "package-lock.json"
            )
        ]) {
            sh "npm install"
        }
    }
}
stage("Build") {
    steps {
        // Writes lock-file to cache based on the GIT_COMMIT hash
        writeFile file: "next-lock.cache", text: "$GIT_COMMIT"

        cache(caches: [
            arbitraryFileCache(
                path: ".next/cache",
                includes: "**/*",
                cacheValidityDecidingFile: "next-lock.cache"
            )
        ]) {
            // aka `next build`
            sh "npm run build"
        }
    }
}
```


--------------------------------------------------------------------------------
title: "How to set a Content Security Policy (CSP) for your Next.js application"
description: "Learn how to set a Content Security Policy (CSP) for your Next.js application."
source: "https://nextjs.org/docs/app/guides/content-security-policy"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./01-nextjs-documentation.md) | [Index](./index.md) | [Next →](./03-content-security-policy.md)
