**Navigation:** [← Previous](./05-scripts.md) | [Index](./index.md) | [Next →](./07-link-component.md)

---

# Videos

This page outlines how to use videos with Next.js applications, showing how to store and display video files without affecting performance.

## Using `<video>` and `<iframe>`

Videos can be embedded on the page using the HTML **`<video>`** tag for direct video files and **`<iframe>`** for external platform-hosted videos.

### `<video>`

The HTML [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) tag can embed self-hosted or directly served video content, allowing full control over the playback and appearance.

```jsx filename="app/ui/video.jsx"
export function Video() {
  return (
    <video width="320" height="240" controls preload="none">
      <source src="/path/to/video.mp4" type="video/mp4" />
      <track
        src="/path/to/captions.vtt"
        kind="subtitles"
        srcLang="en"
        label="English"
      />
      Your browser does not support the video tag.
    </video>
  )
}
```

### Common `<video>` tag attributes

| Attribute     | Description                                                                                               | Example Value                        |
| ------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `src`         | Specifies the source of the video file.                                                                   | `<video src="/path/to/video.mp4" />` |
| `width`       | Sets the width of the video player.                                                                       | `<video width="320" />`              |
| `height`      | Sets the height of the video player.                                                                      | `<video height="240" />`             |
| `controls`    | If present, it displays the default set of playback controls.                                             | `<video controls />`                 |
| `autoPlay`    | Automatically starts playing the video when the page loads. Note: Autoplay policies vary across browsers. | `<video autoPlay />`                 |
| `loop`        | Loops the video playback.                                                                                 | `<video loop />`                     |
| `muted`       | Mutes the audio by default. Often used with `autoPlay`.                                                   | `<video muted />`                    |
| `preload`     | Specifies how the video is preloaded. Values: `none`, `metadata`, `auto`.                                 | `<video preload="none" />`           |
| `playsInline` | Enables inline playback on iOS devices, often necessary for autoplay to work on iOS Safari.               | `<video playsInline />`              |

> **Good to know**: When using the `autoPlay` attribute, it is important to also include the `muted` attribute to ensure the video plays automatically in most browsers and the `playsInline` attribute for compatibility with iOS devices.

For a comprehensive list of video attributes, refer to the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video#attributes).

### Video best practices

* **Fallback Content:** When using the `<video>` tag, include fallback content inside the tag for browsers that do not support video playback.
* **Subtitles or Captions:** Include subtitles or captions for users who are deaf or hard of hearing. Utilize the [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track) tag with your `<video>` elements to specify caption file sources.
* **Accessible Controls:** Standard HTML5 video controls are recommended for keyboard navigation and screen reader compatibility. For advanced needs, consider third-party players like [react-player](https://github.com/cookpete/react-player) or [video.js](https://videojs.com/), which offer accessible controls and consistent browser experience.

### `<iframe>`

The HTML `<iframe>` tag allows you to embed videos from external platforms like YouTube or Vimeo.

```jsx filename="app/page.jsx"
export default function Page() {
  return (
    <iframe src="https://www.youtube.com/embed/19g66ezsKAg" allowFullScreen />
  )
}
```

### Common `<iframe>` tag attributes

| Attribute         | Description                                                            | Example Value                          |
| ----------------- | ---------------------------------------------------------------------- | -------------------------------------- |
| `src`             | The URL of the page to embed.                                          | `<iframe src="https://example.com" />` |
| `width`           | Sets the width of the iframe.                                          | `<iframe width="500" />`               |
| `height`          | Sets the height of the iframe.                                         | `<iframe height="300" />`              |
| `allowFullScreen` | Allows the iframe content to be displayed in full-screen mode.         | `<iframe allowFullScreen />`           |
| `sandbox`         | Enables an extra set of restrictions on the content within the iframe. | `<iframe sandbox />`                   |
| `loading`         | Optimize loading behavior (e.g., lazy loading).                        | `<iframe loading="lazy" />`            |
| `title`           | Provides a title for the iframe to support accessibility.              | `<iframe title="Description" />`       |

For a comprehensive list of iframe attributes, refer to the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attributes).

### Choosing a video embedding method

There are two ways you can embed videos in your Next.js application:

* **Self-hosted or direct video files:** Embed self-hosted videos using the `<video>` tag for scenarios requiring detailed control over the player's functionality and appearance. This integration method within Next.js allows for customization and control of your video content.
* **Using video hosting services (YouTube, Vimeo, etc.):** For video hosting services like YouTube or Vimeo, you'll embed their iframe-based players using the `<iframe>` tag. While this method limits some control over the player, it offers ease of use and features provided by these platforms.

Choose the embedding method that aligns with your application's requirements and the user experience you aim to deliver.

### Embedding externally hosted videos

To embed videos from external platforms, you can use Next.js to fetch the video information and React Suspense to handle the fallback state while loading.

**1. Create a Server Component for video embedding**

The first step is to create a [Server Component](/docs/app/getting-started/server-and-client-components.md) that generates the appropriate iframe for embedding the video. This component will fetch the source URL for the video and render the iframe.

```jsx filename="app/ui/video-component.jsx"
export default async function VideoComponent() {
  const src = await getVideoSrc()

  return <iframe src={src} allowFullScreen />
}
```

**2. Stream the video component using React Suspense**

After creating the Server Component to embed the video, the next step is to [stream](/docs/app/api-reference/file-conventions/loading.md) the component using [React Suspense](https://react.dev/reference/react/Suspense).

```jsx filename="app/page.jsx"
import { Suspense } from 'react'
import VideoComponent from '../ui/VideoComponent.jsx'

export default function Page() {
  return (
    <section>
      <Suspense fallback={<p>Loading video...</p>}>
        <VideoComponent />
      </Suspense>
      {/* Other content of the page */}
    </section>
  )
}
```

> **Good to know**: When embedding videos from external platforms, consider the following best practices:
>
> * Ensure the video embeds are responsive. Use CSS to make the iframe or video player adapt to different screen sizes.
> * Implement [strategies for loading videos](https://yoast.com/site-speed-tips-for-faster-video/) based on network conditions, especially for users with limited data plans.

This approach results in a better user experience as it prevents the page from blocking, meaning the user can interact with the page while the video component streams in.

For a more engaging and informative loading experience, consider using a loading skeleton as the fallback UI. So instead of showing a simple loading message, you can show a skeleton that resembles the video player like this:

```jsx filename="app/page.jsx"
import { Suspense } from 'react'
import VideoComponent from '../ui/VideoComponent.jsx'
import VideoSkeleton from '../ui/VideoSkeleton.jsx'

export default function Page() {
  return (
    <section>
      <Suspense fallback={<VideoSkeleton />}>
        <VideoComponent />
      </Suspense>
      {/* Other content of the page */}
    </section>
  )
}
```

## Self-hosted videos

Self-hosting videos may be preferable for several reasons:

* **Complete control and independence**: Self-hosting gives you direct management over your video content, from playback to appearance, ensuring full ownership and control, free from external platform constraints.
* **Customization for specific needs**: Ideal for unique requirements, like dynamic background videos, it allows for tailored customization to align with design and functional needs.
* **Performance and scalability considerations**: Choose storage solutions that are both high-performing and scalable, to support increasing traffic and content size effectively.
* **Cost and integration**: Balance the costs of storage and bandwidth with the need for easy integration into your Next.js framework and broader tech ecosystem.

### Using Vercel Blob for video hosting

[Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website) offers an efficient way to host videos, providing a scalable cloud storage solution that works well with Next.js. Here's how you can host a video using Vercel Blob:

**1. Uploading a video to Vercel Blob**

In your Vercel dashboard, navigate to the "Storage" tab and select your [Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website) store. In the Blob table's upper-right corner, find and click the "Upload" button. Then, choose the video file you wish to upload. After the upload completes, the video file will appear in the Blob table.

Alternatively, you can upload your video using a server action. For detailed instructions, refer to the Vercel documentation on [server-side uploads](https://vercel.com/docs/storage/vercel-blob/server-upload). Vercel also supports [client-side uploads](https://vercel.com/docs/storage/vercel-blob/client-upload). This method may be preferable for certain use cases.

**2. Displaying the video in Next.js**

Once the video is uploaded and stored, you can display it in your Next.js application. Here's an example of how to do this using the `<video>` tag and React Suspense:

```jsx filename="app/page.jsx"
import { Suspense } from 'react'
import { list } from '@vercel/blob'

export default function Page() {
  return (
    <Suspense fallback={<p>Loading video...</p>}>
      <VideoComponent fileName="my-video.mp4" />
    </Suspense>
  )
}

async function VideoComponent({ fileName }) {
  const { blobs } = await list({
    prefix: fileName,
    limit: 1,
  })
  const { url } = blobs[0]

  return (
    <video controls preload="none" aria-label="Video player">
      <source src={url} type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  )
}
```

In this approach, the page uses the video's `@vercel/blob` URL to display the video using the `VideoComponent`. React Suspense is used to show a fallback until the video URL is fetched and the video is ready to be displayed.

### Adding subtitles to your video

If you have subtitles for your video, you can easily add them using the `<track>` element inside your `<video>` tag. You can fetch the subtitle file from [Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website) in a similar way as the video file. Here's how you can update the `<VideoComponent>` to include subtitles.

```jsx filename="app/page.jsx"
async function VideoComponent({ fileName }) {
  const { blobs } = await list({
    prefix: fileName,
    limit: 2,
  })
  const { url } = blobs[0]
  const { url: captionsUrl } = blobs[1]

  return (
    <video controls preload="none" aria-label="Video player">
      <source src={url} type="video/mp4" />
      <track src={captionsUrl} kind="subtitles" srcLang="en" label="English" />
      Your browser does not support the video tag.
    </video>
  )
}
```

By following this approach, you can effectively self-host and integrate videos into your Next.js applications.

## Resources

To continue learning more about video optimization and best practices, please refer to the following resources:

* **Understanding video formats and codecs**: Choose the right format and codec, like MP4 for compatibility or WebM for web optimization, for your video needs. For more details, see [Mozilla's guide on video codecs](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Video_codecs).
* **Video compression**: Use tools like FFmpeg to effectively compress videos, balancing quality with file size. Learn about compression techniques at [FFmpeg's official website](https://www.ffmpeg.org/).
* **Resolution and bitrate adjustment**: Adjust [resolution and bitrate](https://www.dacast.com/blog/bitrate-vs-resolution/#:~:text=The%20two%20measure%20different%20aspects,yield%20different%20qualities%20of%20video) based on the viewing platform, with lower settings for mobile devices.
* **Content Delivery Networks (CDNs)**: Utilize a CDN to enhance video delivery speed and manage high traffic. When using some storage solutions, such as Vercel Blob, CDN functionality is automatically handled for you. [Learn more](https://vercel.com/docs/edge-network/overview?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website) about CDNs and their benefits.

Explore these video streaming platforms for integrating video into your Next.js projects:

### Open source `next-video` component

* Provides a `<Video>` component for Next.js, compatible with various hosting services including [Vercel Blob](https://vercel.com/docs/storage/vercel-blob?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website), S3, Backblaze, and Mux.
* [Detailed documentation](https://next-video.dev/docs) for using `next-video.dev` with different hosting services.

### Cloudinary Integration

* Official [documentation and integration guide](https://next.cloudinary.dev/) for using Cloudinary with Next.js.
* Includes a `<CldVideoPlayer>` component for [drop-in video support](https://next.cloudinary.dev/cldvideoplayer/basic-usage).
* Find [examples](https://github.com/cloudinary-community/cloudinary-examples/?tab=readme-ov-file#nextjs) of integrating Cloudinary with Next.js including [Adaptive Bitrate Streaming](https://github.com/cloudinary-community/cloudinary-examples/tree/main/examples/nextjs-cldvideoplayer-abr).
* Other [Cloudinary libraries](https://cloudinary.com/documentation) including a Node.js SDK are also available.

### Mux Video API

* Mux provides a [starter template](https://github.com/muxinc/video-course-starter-kit) for creating a video course with Mux and Next.js.
* Learn about Mux's recommendations for embedding [high-performance video for your Next.js application](https://www.mux.com/for/nextjs).
* Explore an [example project](https://with-mux-video.vercel.app/) demonstrating Mux with Next.js.

### Fastly

* Learn more about integrating Fastly's solutions for [video on demand](https://www.fastly.com/products/streaming-media/video-on-demand) and streaming media into Next.js.

### ImageKit.io Integration

* Check out the [official quick start guide](https://imagekit.io/docs/integration/nextjs) for integrating ImageKit with Next.js.
* The integration provides an `<IKVideo>` component, offering [seamless video support](https://imagekit.io/docs/integration/nextjs#rendering-videos).
* You can also explore other [ImageKit libraries](https://imagekit.io/docs), such as the Node.js SDK, which is also available.



--------------------------------------------------------------------------------
title: "API Reference"
description: "Next.js API Reference for the App Router."
source: "https://nextjs.org/docs/app/api-reference"
--------------------------------------------------------------------------------

# API Reference



 - [Directives](/docs/app/api-reference/directives.md)
 - [Components](/docs/app/api-reference/components.md)
 - [File-system conventions](/docs/app/api-reference/file-conventions.md)
 - [Functions](/docs/app/api-reference/functions.md)
 - [Configuration](/docs/app/api-reference/config.md)
 - [CLI](/docs/app/api-reference/cli.md)
 - [Edge Runtime](/docs/app/api-reference/edge.md)
 - [Turbopack](/docs/app/api-reference/turbopack.md)

--------------------------------------------------------------------------------
title: "Directives"
description: "Directives are used to modify the behavior of your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/directives"
--------------------------------------------------------------------------------

# Directives

The following directives are available:

 - [use cache](/docs/app/api-reference/directives/use-cache.md)
 - [use cache: private](/docs/app/api-reference/directives/use-cache-private.md)
 - [use cache: remote](/docs/app/api-reference/directives/use-cache-remote.md)
 - [use client](/docs/app/api-reference/directives/use-client.md)
 - [use server](/docs/app/api-reference/directives/use-server.md)

--------------------------------------------------------------------------------
title: "use cache"
description: "Learn how to use the use cache directive to cache data in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/directives/use-cache"
--------------------------------------------------------------------------------

# use cache

The `use cache` directive allows you to mark a route, React component, or a function as cacheable. It can be used at the top of a file to indicate that all exports in the file should be cached, or inline at the top of function or component to cache the return value.

> **Good to know:** For caching user-specific content that requires access to cookies or headers, see [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md).

## Usage

`use cache` is a Cache Components feature. To enable it, add the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) option to your `next.config.ts` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}

module.exports = nextConfig
```

Then, add `use cache` at the file, component, or function level:

```tsx
// File level
'use cache'

export default async function Page() {
  // ...
}

// Component level
export async function MyComponent() {
  'use cache'
  return <></>
}

// Function level
export async function getData() {
  'use cache'
  const data = await fetch('/api/data')
  return data
}
```

## How `use cache` works

### Cache keys

A cache entry's key is generated using a serialized version of its inputs, which includes:

* Build ID (generated for each build)
* Function ID (a secure identifier unique to the function)
* The [serializable](https://react.dev/reference/rsc/use-server#serializable-parameters-and-return-values) function arguments (or props).

The arguments passed to the cached function, as well as any values it reads from the parent scope automatically become a part of the key. This means, the same cache entry will be reused as long as its inputs are the same.

## Non-serializable arguments

Any non-serializable arguments, props, or closed-over values will turn into references inside the cached function, and can be only passed through and not inspected nor modified. These non-serializable values will be filled in at the request time and won't become a part of the cache key.

For example, a cached function can take in JSX as a `children` prop and return `<div>{children}</div>`, but it won't be able to introspect the actual `children` object. This allows you to nest uncached content inside a cached component.

```tsx filename="app/ui/cached-component.tsx" switcher
async function CachedComponent({ children }: { children: ReactNode }) {
  'use cache'
  return <div>{children}</div>
}
```

```jsx filename="app/ui/cached-component.js" switcher
async function CachedComponent({ children }) {
  'use cache'
  return <div>{children}</div>
}
```

## Return values

The return value of the cacheable function must be serializable props. This ensures that the cached data can be stored and retrieved correctly.

> **Good to know:** The supported types for arguments and the supported types for returned values are **not the same**. For more details, refer to [Serializable Parameters and Return Values](https://react.dev/reference/rsc/use-server#serializable-parameters-and-return-values) for function arguments and [Serializable Types](https://react.dev/reference/rsc/use-client#serializable-types) for return values.

## `use cache` at build time

When used at the top of a [layout](/docs/app/api-reference/file-conventions/layout.md) or [page](/docs/app/api-reference/file-conventions/page.md), the route segment will be prerendered, allowing it to later be [revalidated](#during-revalidation).

This means `use cache` cannot be used with [runtime data](/docs/app/getting-started/cache-components.md#1-suspense-for-runtime-data) like `cookies` or `headers`.

> **Note:** If you need to cache content that depends on cookies, headers, or search params, use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead.

## `use cache` at runtime

On the **server**, the cache entries of individual components or functions will be cached in-memory.

Then, on the **client**, any content returned from the server cache will be stored in the browser's memory for the duration of the session or until [revalidated](#during-revalidation).

## During revalidation

By default, `use cache` has server-side revalidation period of **15 minutes**. While this period may be useful for content that doesn't require frequent updates, you can use the `cacheLife` and `cacheTag` APIs to configure when the individual cache entries should be revalidated.

* [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md): Configure the cache entry lifetime.
* [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md): Create tags for on-demand revalidation.

Both of these APIs integrate across the client and server caching layers, meaning you can configure your caching semantics in one place and have them apply everywhere.

See the [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md) and [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) API docs for more information.

## Examples

### Caching an entire route with `use cache`

To pre-render an entire route, add `use cache` to the top of **both** the `layout` and `page` files. Each of these segments are treated as separate entry points in your application, and will be cached independently.

```tsx filename="app/layout.tsx" switcher
'use cache'

export default async function Layout({ children }: { children: ReactNode }) {
  return <div>{children}</div>
}
```

```jsx filename="app/page.tsx" switcher
'use cache'

export default async function Layout({ children }) {
  return <div>{children}</div>
}
```

Any components imported and nested in `page` file are part of the cache output associated with the `page`.

```tsx filename="app/page.tsx" switcher
'use cache'

async function Users() {
  const users = await fetch('/api/users')
  // loop through users
}

export default async function Page() {
  return (
    <main>
      <Users />
    </main>
  )
}
```

```jsx filename="app/page.js" switcher
'use cache'

async function Users() {
  const users = await fetch('/api/users')
  // loop through users
}

export default async function Page() {
  return (
    <main>
      <Users />
    </main>
  )
}
```

> **Good to know**:
>
> * If `use cache` is added only to the `layout` or the `page`, only that route segment and any components imported into it will be cached.
> * If any of the nested children in the route use [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering), then the route will opt out of pre-rendering.

### Caching a component's output with `use cache`

You can use `use cache` at the component level to cache any fetches or computations performed within that component. The cache entry will be reused as long as the serialized props produce the same value in each instance.

```tsx filename="app/components/bookings.tsx" highlight={2} switcher
export async function Bookings({ type = 'haircut' }: BookingsProps) {
  'use cache'
  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }
  return //...
}

interface BookingsProps {
  type: string
}
```

```jsx filename="app/components/bookings.js" highlight={2} switcher
export async function Bookings({ type = 'haircut' }) {
  'use cache'
  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }
  return //...
}
```

### Caching function output with `use cache`

Since you can add `use cache` to any asynchronous function, you aren't limited to caching components or routes only. You might want to cache a network request, a database query, or a slow computation.

```tsx filename="app/actions.ts" highlight={2} switcher
export async function getData() {
  'use cache'

  const data = await fetch('/api/data')
  return data
}
```

```jsx filename="app/actions.js" highlight={2} switcher
export async function getData() {
  'use cache'

  const data = await fetch('/api/data')
  return data
}
```

### Interleaving

In React, composition with `children` or slots is a well-known pattern for building flexible components. When using `use cache`, you can continue to compose your UI in this way. Anything included as `children`, or other compositional slots, in the returned JSX will be passed through the cached component without affecting its cache entry.

As long as you don't directly reference any of the JSX slots inside the body of the cacheable function itself, their presence in the returned output won't affect the cache entry.

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  const uncachedData = await getData()
  return (
    // Pass compositional slots as props, e.g. header and children
    <CacheComponent header={<h1>Home</h1>}>
      {/* DynamicComponent is provided as the children slot */}
      <DynamicComponent data={uncachedData} />
    </CacheComponent>
  )
}

async function CacheComponent({
  header, // header: a compositional slot, injected as a prop
  children, // children: another slot for nested composition
}: {
  header: ReactNode
  children: ReactNode
}) {
  'use cache'
  const cachedData = await fetch('/api/cached-data')
  return (
    <div>
      {header}
      <PrerenderedComponent data={cachedData} />
      {children}
    </div>
  )
}
```

```jsx filename="app/page.js" switcher
export default async function Page() {
  const uncachedData = await getData()
  return (
    // Pass compositional slots as props, e.g. header and children
    <CacheComponent header={<h1>Home</h1>}>
      {/* DynamicComponent is provided as the children slot */}
      <DynamicComponent data={uncachedData} />
    </CacheComponent>
  )
}

async function CacheComponent({
  header, // header: a compositional slot, injected as a prop
  children, // children: another slot for nested composition
}) {
  'use cache'
  const cachedData = await fetch('/api/cached-data')
  return (
    <div>
      {header}
      <PrerenderedComponent data={cachedData} />
      {children}
    </div>
  )
}
```

You can also pass Server Actions through cached components to Client Components without invoking them inside the cacheable function.

```tsx filename="app/page.tsx" switcher
import ClientComponent from './ClientComponent'

export default async function Page() {
  const performUpdate = async () => {
    'use server'
    // Perform some server-side update
    await db.update(...)
  }

  return <CacheComponent performUpdate={performUpdate} />
}

async function CachedComponent({
  performUpdate,
}: {
  performUpdate: () => Promise<void>
}) {
  'use cache'
  // Do not call performUpdate here
  return <ClientComponent action={performUpdate} />
}
```

```jsx filename="app/page.js" switcher
import ClientComponent from './ClientComponent'

export default async function Page() {
  const performUpdate = async () => {
    'use server'
    // Perform some server-side update
    await db.update(...)
  }

  return <CacheComponent performUpdate={performUpdate} />
}

async function CachedComponent({ performUpdate }) {
  'use cache'
  // Do not call performUpdate here
  return <ClientComponent action={performUpdate} />
}
```

```tsx filename="app/ClientComponent.tsx" switcher
'use client'

export default function ClientComponent({
  action,
}: {
  action: () => Promise<void>
}) {
  return <button onClick={action}>Update</button>
}
```

```jsx filename="app/ClientComponent.js" switcher
'use client'

export default function ClientComponent({ action }) {
  return <button onClick={action}>Update</button>
}
```

## Platform Support

| Deployment Option                                                   | Supported         |
| ------------------------------------------------------------------- | ----------------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes               |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes               |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No                |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Platform-specific |

Learn how to [configure caching](/docs/app/guides/self-hosting.md#caching-and-isr) when self-hosting Next.js.

## Version History

| Version   | Changes                                                     |
| --------- | ----------------------------------------------------------- |
| `v16.0.0` | `"use cache"` is enabled with the Cache Components feature. |
| `v15.0.0` | `"use cache"` is introduced as an experimental feature.     |
## Related

View related API references.

- [use cache: private](/docs/app/api-reference/directives/use-cache-private.md)
  - Learn how to use the `"use cache: private"` directive to enable runtime prefetching of personalized content in your Next.js application.
- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
  - Learn how to enable the cacheComponents flag in Next.js.
- [cacheLife](/docs/app/api-reference/config/next-config-js/cacheLife.md)
  - Learn how to set up cacheLife configurations in Next.js.
- [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
  - Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
- [cacheLife](/docs/app/api-reference/functions/cacheLife.md)
  - Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
  - API Reference for the revalidateTag function.


--------------------------------------------------------------------------------
title: "use cache: private"
description: "Learn how to use the `"use cache: private"` directive to enable runtime prefetching of personalized content in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/directives/use-cache-private"
--------------------------------------------------------------------------------

# use cache: private

The `'use cache: private'` directive works just like [`use cache`](/docs/app/api-reference/directives/use-cache.md), but allows you to use runtime APIs like cookies, headers, or search params.

> **Good to know:** Unlike `use cache`, private caches are not prerendered statically as they contain personalized data that is not shared between users.

## Usage

To use `'use cache: private'`, enable the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) flag in your `next.config.ts` file:

```tsx filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```jsx filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

Then add `'use cache: private'` to your function along with a `cacheLife` configuration.

### Basic example

```tsx filename="app/product/[id]/page.tsx" switcher
import { Suspense } from 'react'
import { cookies } from 'next/headers'
import { cacheLife, cacheTag } from 'next/cache'

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params

  return (
    <div>
      <ProductDetails id={id} />
      <Suspense fallback={<div>Loading recommendations...</div>}>
        <Recommendations productId={id} />
      </Suspense>
    </div>
  )
}

async function Recommendations({ productId }: { productId: string }) {
  const recommendations = await getRecommendations(productId)

  return (
    <div>
      {recommendations.map((rec) => (
        <ProductCard key={rec.id} product={rec} />
      ))}
    </div>
  )
}

async function getRecommendations(productId: string) {
  'use cache: private'
  cacheTag(`recommendations-${productId}`)
  cacheLife({ stale: 60 }) // Minimum 30 seconds required for runtime prefetch

  // Access cookies within private cache functions
  const sessionId = (await cookies()).get('session-id')?.value || 'guest'

  return getPersonalizedRecommendations(productId, sessionId)
}
```

```jsx filename="app/product/[id]/page.js" switcher
import { Suspense } from 'react'
import { cookies } from 'next/headers'
import { cacheLife, cacheTag } from 'next/cache'

export default async function ProductPage({ params }) {
  const { id } = await params

  return (
    <div>
      <ProductDetails id={id} />
      <Suspense fallback={<div>Loading recommendations...</div>}>
        <Recommendations productId={id} />
      </Suspense>
    </div>
  )
}

async function Recommendations({ productId }) {
  const recommendations = await getRecommendations(productId)

  return (
    <div>
      {recommendations.map((rec) => (
        <ProductCard key={rec.id} product={rec} />
      ))}
    </div>
  )
}

async function getRecommendations(productId) {
  'use cache: private'
  cacheTag(`recommendations-${productId}`)
  cacheLife({ stale: 60 }) // Minimum 30 seconds required for runtime prefetch

  // Access cookies within private cache functions
  const sessionId = (await cookies()).get('session-id')?.value || 'guest'

  return getPersonalizedRecommendations(productId, sessionId)
}
```

## Request APIs allowed in private caches

The following request-specific APIs can be used inside `'use cache: private'` functions:

| API            | Allowed in `use cache` | Allowed in `'use cache: private'` |
| -------------- | ---------------------- | --------------------------------- |
| `cookies()`    | No                     | Yes                               |
| `headers()`    | No                     | Yes                               |
| `searchParams` | No                     | Yes                               |
| `connection()` | No                     | No                                |

> **Note:** The [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) API is prohibited in both `use cache` and `'use cache: private'` as it provides connection-specific information that cannot be safely cached.

## Version History

| Version   | Changes                                                              |
| --------- | -------------------------------------------------------------------- |
| `v16.0.0` | `"use cache: private"` is enabled with the Cache Components feature. |
## Related

View related API references.

- [use cache](/docs/app/api-reference/directives/use-cache.md)
  - Learn how to use the use cache directive to cache data in your Next.js application.
- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
  - Learn how to enable the cacheComponents flag in Next.js.
- [cacheLife](/docs/app/api-reference/functions/cacheLife.md)
  - Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.
- [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
  - Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
- [Prefetching](/docs/app/guides/prefetching.md)
  - Learn how to configure prefetching in Next.js


--------------------------------------------------------------------------------
title: "use cache: remote"
description: "Learn how to use the `"use cache: remote"` directive to enable caching in dynamic contexts in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/directives/use-cache-remote"
--------------------------------------------------------------------------------

# use cache: remote

The `'use cache: remote'` directive enables caching of **shared data** in dynamic contexts where regular [`use cache`](/docs/app/api-reference/directives/use-cache.md) would not work, for example after calling [`await connection()`](/docs/app/api-reference/functions/connection.md), [`await cookies()`](/docs/app/api-reference/functions/cookies.md) or [`await headers()`](/docs/app/api-reference/functions/headers.md).

> **Good to know:**
>
> * Results are stored in server-side cache handlers and shared across all users.
> * For **user-specific data** that depends on [`await cookies()`](/docs/app/api-reference/functions/cookies.md) or [`await headers()`](/docs/app/api-reference/functions/headers.md), use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead.

## Usage

To use `'use cache: remote'`, enable the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) flag in your `next.config.ts` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

Then add `'use cache: remote'` to your function that needs to cache data in a dynamic context.

### Basic example

Cache product pricing that needs to be fetched at request time but can be shared across all users. Use [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md#custom-cache-profiles) to set the cache lifetime of the price.

```tsx filename="app/product/[id]/page.tsx" switcher
import { Suspense } from 'react'
import { connection } from 'next/server'
import { cacheTag, cacheLife } from 'next/cache'

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params

  return (
    <div>
      <ProductDetails id={id} />
      <Suspense fallback={<div>Loading price...</div>}>
        <ProductPrice productId={id} />
      </Suspense>
    </div>
  )
}

function ProductDetails({ id }: { id: string }) {
  return <div>Product: {id}</div>
}

async function ProductPrice({ productId }: { productId: string }) {
  // Calling connection() makes this component dynamic, preventing
  // it from being included in the static shell. This ensures the price
  // is always fetched at request time.
  await connection()

  // Now we can cache the price in a remote cache handler.
  // Regular 'use cache' would NOT work here because we're in a dynamic context.
  const price = await getProductPrice(productId)

  return <div>Price: ${price}</div>
}

async function getProductPrice(productId: string) {
  'use cache: remote'
  cacheTag(`product-price-${productId}`)
  cacheLife({ expire: 3600 }) // 1 hour

  // This database query is cached and shared across all users
  return db.products.getPrice(productId)
}
```

```jsx filename="app/product/[id]/page.js" switcher
import { Suspense } from 'react'
import { connection } from 'next/server'
import { cacheTag, cacheLife } from 'next/cache'

export default async function ProductPage({ params }) {
  const { id } = await params

  return (
    <div>
      <ProductDetails id={id} />
      <Suspense fallback={<div>Loading price...</div>}>
        <ProductPrice productId={id} />
      </Suspense>
    </div>
  )
}

function ProductDetails({ id }) {
  return <div>Product: {id}</div>
}

async function ProductPrice({ productId }) {
  // Calling connection() makes this component dynamic, preventing
  // it from being included in the static shell. This ensures the price
  // is always fetched at request time.
  await connection()

  // Now we can cache the price in a remote cache handler.
  // Regular 'use cache' would NOT work here because we're in a dynamic context.
  const price = await getProductPrice(productId)

  return <div>Price: ${price}</div>
}

async function getProductPrice(productId) {
  'use cache: remote'
  cacheTag(`product-price-${productId}`)
  cacheLife({ expire: 3600 }) // 1 hour

  // This database query is cached and shared across all users
  return db.products.getPrice(productId)
}
```

> **Note:** Regular [`use cache`](/docs/app/api-reference/directives/use-cache.md) will not cache anything when used in a dynamic context (after [`await connection()`](/docs/app/api-reference/functions/connection.md), [`await cookies()`](/docs/app/api-reference/functions/cookies.md), [`await headers()`](/docs/app/api-reference/functions/headers.md), etc.). Use `'use cache: remote'` to enable runtime caching in these scenarios.

## How `use cache: remote` differs from `use cache` and `use cache: private`

Next.js provides three caching directives, each designed for different use cases:

| Feature                          | `use cache`                         | `'use cache: remote'`                                     | `'use cache: private'`              |
| -------------------------------- | ----------------------------------- | --------------------------------------------------------- | ----------------------------------- |
| **Works in dynamic context**     | No (requires static context)        | Yes (designed for dynamic contexts)                       | Yes                                 |
| **Access to `await cookies()`**  | No                                  | No                                                        | Yes                                 |
| **Access to `await headers()`**  | No                                  | No                                                        | Yes                                 |
| **After `await connection()`**   | No (won't cache)                    | No                                                        | No                                  |
| **Stored in cache handler**      | Yes (server-side)                   | Yes (server-side)                                         | No (client-side only)               |
| **Cache scope**                  | Global (shared)                     | Global (shared)                                           | Per-user (isolated)                 |
| **Supports runtime prefetching** | N/A (pre-rendered at build)         | No                                                        | Yes (when configured)               |
| **Use case**                     | Static, shared content (build-time) | Dynamic, shared content in runtime contexts (per-request) | Personalized, user-specific content |

> **Note:** While you can't call `await cookies()` or `await headers()` inside `'use cache: remote'`, you can read the values before calling a function that is wrapped by `'use cache: remote'` and the arguments will be included in the cache key. Note that this is not recommended as it will dramatically increase the cache size and reduce the cache hit rate.

### When to use each directive

Choose the right caching directive based on your use case:

**Use [`use cache`](/docs/app/api-reference/directives/use-cache.md) when:**

* Content can be prerendered at build time
* Content is shared across all users
* Content doesn't depend on request-specific data

**Use `'use cache: remote'` when:**

* You need caching within dynamic context
* Content is shared across users but must be rendered per-request (after `await connection()`)
* You want to cache expensive operations in a server-side cache handler

**Use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) when:**

* Content is personalized per-user (depends on cookies, headers)
* You need [runtime prefetching](/docs/app/guides/prefetching.md) of user-specific content
* Content should never be shared between users

## How it works

The `'use cache: remote'` directive enables runtime caching of shared data in dynamic contexts by storing results in server-side cache handlers rather than prerendering at build time.

### Dynamic context detection

When Next.js encounters certain APIs like [`connection()`](/docs/app/api-reference/functions/connection.md), [`cookies()`](/docs/app/api-reference/functions/cookies.md), or [`headers()`](/docs/app/api-reference/functions/headers.md), the context becomes "dynamic". In a dynamic context:

1. **Regular `use cache` stops working** - it won't cache anything
2. **`'use cache: remote'` continues to work** - it is cached by a remote cache handler.
3. **Results are stored server-side** in a key-value store configured for your deployment
4. **Cached data is shared across requests** - reducing database load and origin requests

> **Good to know:** Without `'use cache: remote'`, functions in dynamic contexts would execute on every request, potentially creating performance bottlenecks. Remote caching eliminates this issue by storing results in server-side cache handlers.

### Storage behavior

Remote caches are **persisted using server-side cache handlers**, which may include:

* **Distributed key-value stores** (in-memory or persistent storage solutions)
* **File system or in-memory storage** (often used in development or for custom deployments)
* **Environment-specific caches** (provided by your hosting infrastructure)
* **Custom or configured cache handlers** (depending on your application's setup)

This means:

1. Cached data is shared across all users and requests
2. Cache entries persist beyond a single session
3. Cache invalidation works via [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) and [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md)
4. Cache expiration is controlled by [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md) configuration

### Dynamic context example

```tsx
async function UserDashboard() {
  // Calling connection() makes the context dynamic
  await connection()

  // Without any caching directive, this runs on every request
  const stats = await getStats()

  // With 'use cache: remote', this is cached in the remote handler
  const analytics = await getAnalytics()

  return (
    <div>
      <Stats data={stats} />
      <Analytics data={analytics} />
    </div>
  )
}

async function getAnalytics() {
  'use cache: remote'
  cacheLife({ expire: 300 }) // 5 minutes

  // This expensive operation is cached and shared across all requests
  return fetchAnalyticsData()
}
```

## Request APIs and remote caches

While `'use cache: remote'` technically allows access to request-specific data by calling API's like [`cookies()`](/docs/app/api-reference/functions/cookies.md) and [`headers()`](/docs/app/api-reference/functions/headers.md) before calling a function that is wrapped by `'use cache: remote'`, it's generally not recommended to use them together:

| API                                                                                   | Allowed in `use cache` | Allowed in `'use cache: remote'` | Recommended                                                                                |
| ------------------------------------------------------------------------------------- | ---------------------- | -------------------------------- | ------------------------------------------------------------------------------------------ |
| [`cookies()`](/docs/app/api-reference/functions/cookies.md)                              | No                     | No                               | Use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead |
| [`headers()`](/docs/app/api-reference/functions/headers.md)                              | No                     | No                               | Use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead |
| [`connection()`](/docs/app/api-reference/functions/connection.md)                        | No                     | No                               | No - these cannot ever be cached                                                           |
| [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) | No                     | No                               | Use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead |

> **Important:** If you need to cache based on cookies, headers, or search params, use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead. Remote caches are shared across all users, so caching user-specific data in them can lead to incorrect results being served to different users.

## Nesting rules

Remote caches have specific nesting rules:

* Remote caches **can** be nested inside other remote caches (`'use cache: remote'`)
* Remote caches **can** be nested inside regular caches (`'use cache'`)
* Remote caches **cannot** be nested inside private caches (`'use cache: private'`)
* Private caches **cannot** be nested inside remote caches

```tsx
// VALID: Remote inside remote
async function outerRemote() {
  'use cache: remote'
  const result = await innerRemote()
  return result
}

async function innerRemote() {
  'use cache: remote'
  return getData()
}

// VALID: Remote inside regular cache
async function outerCache() {
  'use cache'
  // If this is in a dynamic context, the inner remote cache will work
  const result = await innerRemote()
  return result
}

async function innerRemote() {
  'use cache: remote'
  return getData()
}

// INVALID: Remote inside private
async function outerPrivate() {
  'use cache: private'
  const result = await innerRemote() // Error!
  return result
}

async function innerRemote() {
  'use cache: remote'
  return getData()
}

// INVALID: Private inside remote
async function outerRemote() {
  'use cache: remote'
  const result = await innerPrivate() // Error!
  return result
}

async function innerPrivate() {
  'use cache: private'
  return getData()
}
```

## Examples

The following examples demonstrate common patterns for using `'use cache: remote'`. For details about `cacheLife` parameters (`stale`, `revalidate`, `expire`), see the [`cacheLife` API reference](/docs/app/api-reference/functions/cacheLife.md).

### Per-request database queries

Cache expensive database queries that are accessed in dynamic contexts, reducing load on your database:

```tsx filename="app/dashboard/page.tsx"
import { connection } from 'next/server'
import { cacheLife, cacheTag } from 'next/cache'

export default async function DashboardPage() {
  // Make context dynamic
  await connection()

  const stats = await getGlobalStats()

  return <StatsDisplay stats={stats} />
}

async function getGlobalStats() {
  'use cache: remote'
  cacheTag('global-stats')
  cacheLife({ expire: 60 }) // 1 minute

  // This expensive database query is cached and shared across all users,
  // reducing load on your database
  const stats = await db.analytics.aggregate({
    total_users: 'count',
    active_sessions: 'count',
    revenue: 'sum',
  })

  return stats
}
```

### API responses in streaming contexts

Cache API responses that are fetched during streaming or after dynamic operations:

```tsx filename="app/feed/page.tsx"
import { Suspense } from 'react'
import { connection } from 'next/server'
import { cacheLife, cacheTag } from 'next/cache'

export default async function FeedPage() {
  return (
    <div>
      <Suspense fallback={<Skeleton />}>
        <FeedItems />
      </Suspense>
    </div>
  )
}

async function FeedItems() {
  // Dynamic context
  await connection()

  const items = await getFeedItems()

  return items.map((item) => <FeedItem key={item.id} item={item} />)
}

async function getFeedItems() {
  'use cache: remote'
  cacheTag('feed-items')
  cacheLife({ expire: 120 }) // 2 minutes

  // This API call is cached, reducing requests to your external service
  const response = await fetch('https://api.example.com/feed')
  return response.json()
}
```

### Computed data after dynamic checks

Cache expensive computations that occur after dynamic security or feature checks:

```tsx filename="app/reports/page.tsx"
import { connection } from 'next/server'
import { cacheLife } from 'next/cache'

export default async function ReportsPage() {
  // Dynamic security check
  await connection()

  const report = await generateReport()

  return <ReportViewer report={report} />
}

async function generateReport() {
  'use cache: remote'
  cacheLife({ expire: 3600 }) // 1 hour

  // This expensive computation is cached and shared across all authorized users,
  // avoiding repeated calculations
  const data = await db.transactions.findMany()

  return {
    totalRevenue: calculateRevenue(data),
    topProducts: analyzeProducts(data),
    trends: calculateTrends(data),
  }
}
```

### Mixed caching strategies

Combine static, remote, and private caching for optimal performance:

```tsx filename="app/product/[id]/page.tsx"
import { Suspense } from 'react'
import { connection } from 'next/server'
import { cookies } from 'next/headers'
import { cacheLife, cacheTag } from 'next/cache'

// Static product data - prerendered at build time
async function getProduct(id: string) {
  'use cache'
  cacheTag(`product-${id}`)

  // This is cached at build time and shared across all users
  return db.products.find({ where: { id } })
}

// Shared pricing data - cached at runtime in remote handler
async function getProductPrice(id: string) {
  'use cache: remote'
  cacheTag(`product-price-${id}`)
  cacheLife({ expire: 300 }) // 5 minutes

  // This is cached at runtime and shared across all users
  return db.products.getPrice({ where: { id } })
}

// User-specific recommendations - private cache per user
async function getRecommendations(productId: string) {
  'use cache: private'
  cacheLife({ expire: 60 }) // 1 minute

  const sessionId = (await cookies()).get('session-id')?.value

  // This is cached per-user and never shared
  return db.recommendations.findMany({
    where: { productId, sessionId },
  })
}

export default async function ProductPage({ params }) {
  const { id } = await params

  // Static product data
  const product = await getProduct(id)

  return (
    <div>
      <ProductDetails product={product} />

      {/* Dynamic shared price */}
      <Suspense fallback={<PriceSkeleton />}>
        <ProductPriceComponent productId={id} />
      </Suspense>

      {/* Dynamic personalized recommendations */}
      <Suspense fallback={<RecommendationsSkeleton />}>
        <ProductRecommendations productId={id} />
      </Suspense>
    </div>
  )
}

function ProductDetails({ product }) {
  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
    </div>
  )
}

async function ProductPriceComponent({ productId }) {
  // Make this component dynamic
  await connection()

  const price = await getProductPrice(productId)
  return <div>Price: ${price}</div>
}

async function ProductRecommendations({ productId }) {
  const recommendations = await getRecommendations(productId)
  return <RecommendationsList items={recommendations} />
}

function PriceSkeleton() {
  return <div>Loading price...</div>
}

function RecommendationsSkeleton() {
  return <div>Loading recommendations...</div>
}

function RecommendationsList({ items }) {
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  )
}
```

> **Good to know**:
>
> * Remote caches are stored in server-side cache handlers and shared across all users
> * Remote caches work in dynamic contexts where regular [`use cache`](/docs/app/api-reference/directives/use-cache.md) would fail
> * Use [`cacheTag()`](/docs/app/api-reference/functions/cacheTag.md) and [`revalidateTag()`](/docs/app/api-reference/functions/revalidateTag.md) to invalidate remote caches on-demand
> * Use [`cacheLife()`](/docs/app/api-reference/functions/cacheLife.md) to configure cache expiration
> * For user-specific data, use [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private.md) instead of `'use cache: remote'`
> * Remote caches reduce origin load by storing computed or fetched data server-side

## Platform Support

| Deployment Option                                                   | Supported |
| ------------------------------------------------------------------- | --------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes       |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes       |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No        |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Yes       |

## Version History

| Version   | Changes                                                             |
| --------- | ------------------------------------------------------------------- |
| `v16.0.0` | `"use cache: remote"` is enabled with the Cache Components feature. |
## Related

View related API references.

- [use cache](/docs/app/api-reference/directives/use-cache.md)
  - Learn how to use the use cache directive to cache data in your Next.js application.
- [use cache: private](/docs/app/api-reference/directives/use-cache-private.md)
  - Learn how to use the `"use cache: private"` directive to enable runtime prefetching of personalized content in your Next.js application.
- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
  - Learn how to enable the cacheComponents flag in Next.js.
- [cacheLife](/docs/app/api-reference/functions/cacheLife.md)
  - Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.
- [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
  - Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.
- [connection](/docs/app/api-reference/functions/connection.md)
  - API Reference for the connection function.


--------------------------------------------------------------------------------
title: "use client"
description: "Learn how to use the use client directive to render a component on the client."
source: "https://nextjs.org/docs/app/api-reference/directives/use-client"
--------------------------------------------------------------------------------

# use client

The `'use client'` directive declares an entry point for the components to be rendered on the **client side** and should be used when creating interactive user interfaces (UI) that require client-side JavaScript capabilities, such as state management, event handling, and access to browser APIs. This is a React feature.

> **Good to know:**
>
> You do not need to add the `'use client'` directive to every file that contains Client Components. You only need to add it to the files whose components you want to render directly within Server Components. The `'use client'` directive defines the client-server [boundary](https://nextjs.org/docs/app/building-your-application/rendering#network-boundary), and the components exported from such a file serve as entry points to the client.

## Usage

To declare an entry point for the Client Components, add the `'use client'` directive **at the top of the file**, before any imports:

```tsx filename="app/components/counter.tsx" highlight={1} switcher
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

```jsx filename="app/components/counter.js" highlight={1} switcher
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  )
}
```

When using the `'use client'` directive, the props of the Client Components must be [serializable](https://react.dev/reference/rsc/use-client#serializable-types). This means the props need to be in a format that React can serialize when sending data from the server to the client.

```tsx filename="app/components/counter.tsx" highlight={4} switcher
'use client'

export default function Counter({
  onClick /* ❌ Function is not serializable */,
}) {
  return (
    <div>
      <button onClick={onClick}>Increment</button>
    </div>
  )
}
```

```jsx filename="app/components/counter.js" highlight={4} switcher
'use client'

export default function Counter({
  onClick /* ❌ Function is not serializable */,
}) {
  return (
    <div>
      <button onClick={onClick}>Increment</button>
    </div>
  )
}
```

## Nesting Client Components within Server Components

Combining Server and Client Components allows you to build applications that are both performant and interactive:

1. **Server Components**: Use for static content, data fetching, and SEO-friendly elements.
2. **Client Components**: Use for interactive elements that require state, effects, or browser APIs.
3. **Component composition**: Nest Client Components within Server Components as needed for a clear separation of server and client logic.

In the following example:

* `Header` is a Server Component handling static content.
* `Counter` is a Client Component enabling interactivity within the page.

```tsx filename="app/page.tsx" highlight={2,8} switcher
import Header from './header'
import Counter from './counter' // This is a Client Component

export default function Page() {
  return (
    <div>
      <Header />
      <Counter />
    </div>
  )
}
```

```jsx filename="app/page.js" highlight={2,8} switcher
import Header from './header'
import Counter from './counter' // This is a Client Component

export default function Page() {
  return (
    <div>
      <Header />
      <Counter />
    </div>
  )
}
```

## Reference

See the [React documentation](https://react.dev/reference/rsc/use-client) for more information on `'use client'`.


--------------------------------------------------------------------------------
title: "use server"
description: "Learn how to use the use server directive to execute code on the server."
source: "https://nextjs.org/docs/app/api-reference/directives/use-server"
--------------------------------------------------------------------------------

# use server

The `use server` directive designates a function or file to be executed on the **server side**. It can be used at the top of a file to indicate that all functions in the file are server-side, or inline at the top of a function to mark the function as a [Server Function](https://19.react.dev/reference/rsc/server-functions). This is a React feature.

## Using `use server` at the top of a file

The following example shows a file with a `use server` directive at the top. All functions in the file are executed on the server.

```tsx filename="app/actions.ts" highlight={1} switcher
'use server'
import { db } from '@/lib/db' // Your database client

export async function createUser(data: { name: string; email: string }) {
  const user = await db.user.create({ data })
  return user
}
```

```jsx filename="app/actions.js" highlight={1} switcher
'use server'
import { db } from '@/lib/db' // Your database client

export async function createUser(data) {
  const user = await db.user.create({ data })
  return user
}
```

### Using Server Functions in a Client Component

To use Server Functions in Client Components you need to create your Server Functions in a dedicated file using the `use server` directive at the top of the file. These Server Functions can then be imported into Client and Server Components and executed.

Assuming you have a `fetchUsers` Server Function in `actions.ts`:

```tsx filename="app/actions.ts" highlight={1} switcher
'use server'
import { db } from '@/lib/db' // Your database client

export async function fetchUsers() {
  const users = await db.user.findMany()
  return users
}
```

```jsx filename="app/actions.js" highlight={1} switcher
'use server'
import { db } from '@/lib/db' // Your database client

export async function fetchUsers() {
  const users = await db.user.findMany()
  return users
}
```

Then you can import the `fetchUsers` Server Function into a Client Component and execute it on the client-side.

```tsx filename="app/components/my-button.tsx" highlight={1,2,8} switcher
'use client'
import { fetchUsers } from '../actions'

export default function MyButton() {
  return <button onClick={() => fetchUsers()}>Fetch Users</button>
}
```

```jsx filename="app/components/my-button.js" highlight={1,2,8} switcher
'use client'
import { fetchUsers } from '../actions'

export default function MyButton() {
  return <button onClick={() => fetchUsers()}>Fetch Users</button>
}
```

## Using `use server` inline

In the following example, `use server` is used inline at the top of a function to mark it as a [Server Function](https://19.react.dev/reference/rsc/server-functions):

```tsx filename="app/posts/[id]/page.tsx" switcher highlight={8}
import { EditPost } from './edit-post'
import { revalidatePath } from 'next/cache'

export default async function PostPage({ params }: { params: { id: string } }) {
  const post = await getPost(params.id)

  async function updatePost(formData: FormData) {
    'use server'
    await savePost(params.id, formData)
    revalidatePath(`/posts/${params.id}`)
  }

  return <EditPost updatePostAction={updatePost} post={post} />
}
```

```jsx filename="app/posts/[id]/page.js" switcher highlight={8}
import { EditPost } from './edit-post'
import { revalidatePath } from 'next/cache'

export default async function PostPage({ params }) {
  const post = await getPost(params.id)

  async function updatePost(formData) {
    'use server'
    await savePost(params.id, formData)
    revalidatePath(`/posts/${params.id}`)
  }

  return <EditPost updatePostAction={updatePost} post={post} />
}
```

## Security considerations

When using the `use server` directive, it's important to ensure that all server-side logic is secure and that sensitive data remains protected.

### Authentication and authorization

Always authenticate and authorize users before performing sensitive server-side operations.

```tsx filename="app/actions.ts" highlight={1,7,8,9,10} switcher
'use server'

import { db } from '@/lib/db' // Your database client
import { authenticate } from '@/lib/auth' // Your authentication library

export async function createUser(
  data: { name: string; email: string },
  token: string
) {
  const user = authenticate(token)
  if (!user) {
    throw new Error('Unauthorized')
  }
  const newUser = await db.user.create({ data })
  return newUser
}
```

```jsx filename="app/actions.js" highlight={1,7,8,9,10} switcher
'use server'

import { db } from '@/lib/db' // Your database client
import { authenticate } from '@/lib/auth' // Your authentication library

export async function createUser(data, token) {
  const user = authenticate(token)
  if (!user) {
    throw new Error('Unauthorized')
  }
  const newUser = await db.user.create({ data })
  return newUser
}
```

## Reference

See the [React documentation](https://react.dev/reference/rsc/use-server) for more information on `use server`.


--------------------------------------------------------------------------------
title: "Components"
description: "API Reference for Next.js built-in components."
source: "https://nextjs.org/docs/app/api-reference/components"
--------------------------------------------------------------------------------

# Components



 - [Font](/docs/app/api-reference/components/font.md)
 - [Form Component](/docs/app/api-reference/components/form.md)
 - [Image Component](/docs/app/api-reference/components/image.md)
 - [Link Component](/docs/app/api-reference/components/link.md)
 - [Script Component](/docs/app/api-reference/components/script.md)

--------------------------------------------------------------------------------
title: "Font Module"
description: "Optimizing loading web fonts with the built-in `next/font` loaders."
source: "https://nextjs.org/docs/app/api-reference/components/font"
--------------------------------------------------------------------------------

# Font

[`next/font`](/docs/app/api-reference/components/font.md) automatically optimizes your fonts (including custom fonts) and removes external network requests for improved privacy and performance.

It includes **built-in automatic self-hosting** for any font file. This means you can optimally load web fonts with no [layout shift](https://web.dev/articles/cls).

You can also conveniently use all [Google Fonts](https://fonts.google.com/). CSS and font files are downloaded at build time and self-hosted with the rest of your static assets. **No requests are sent to Google by the browser.**

```tsx filename="app/layout.tsx" switcher
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

> **🎥 Watch:** Learn more about using `next/font` → [YouTube (6 minutes)](https://www.youtube.com/watch?v=L8_98i_bMMA).

## Reference

| Key                                         | `font/google`       | `font/local`        | Type                       | Required          |
| ------------------------------------------- | ------------------- | ------------------- | -------------------------- | ----------------- |
| [`src`](#src)                               |  |  | String or Array of Objects | Yes               |
| [`weight`](#weight)                         |  |  | String or Array            | Required/Optional |
| [`style`](#style)                           |  |  | String or Array            | -                 |
| [`subsets`](#subsets)                       |  |  | Array of Strings           | -                 |
| [`axes`](#axes)                             |  |  | Array of Strings           | -                 |
| [`display`](#display)                       |  |  | String                     | -                 |
| [`preload`](#preload)                       |  |  | Boolean                    | -                 |
| [`fallback`](#fallback)                     |  |  | Array of Strings           | -                 |
| [`adjustFontFallback`](#adjustfontfallback) |  |  | Boolean or String          | -                 |
| [`variable`](#variable)                     |  |  | String                     | -                 |
| [`declarations`](#declarations)             |  |  | Array of Objects           | -                 |

### `src`

The path of the font file as a string or an array of objects (with type `Array<{path: string, weight?: string, style?: string}>`) relative to the directory where the font loader function is called.

Used in `next/font/local`

* Required

Examples:

* `src:'./fonts/my-font.woff2'` where `my-font.woff2` is placed in a directory named `fonts` inside the `app` directory
* `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
* if the font loader function is called in `app/page.tsx` using `src:'../styles/fonts/my-font.ttf'`, then `my-font.ttf` is placed in `styles/fonts` at the root of the project

### `weight`

The font [`weight`](https://fonts.google.com/knowledge/glossary/weight) with the following possibilities:

* A string with possible values of the weights available for the specific font or a range of values if it's a [variable](https://fonts.google.com/variablefonts) font
* An array of weight values if the font is not a [variable google font](https://fonts.google.com/variablefonts). It applies to `next/font/google` only.

Used in `next/font/google` and `next/font/local`

* Required if the font being used is **not** [variable](https://fonts.google.com/variablefonts)

Examples:

* `weight: '400'`: A string for a single weight value - for the font [`Inter`](https://fonts.google.com/specimen/Inter?query=inter), the possible values are `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'` or `'variable'` where `'variable'` is the default)
* `weight: '100 900'`: A string for the range between `100` and `900` for a variable font
* `weight: ['100','400','900']`: An array of 3 possible values for a non variable font

### `style`

The font [`style`](https://developer.mozilla.org/docs/Web/CSS/font-style) with the following possibilities:

* A string [value](https://developer.mozilla.org/docs/Web/CSS/font-style#values) with default value of `'normal'`
* An array of style values if the font is not a [variable google font](https://fonts.google.com/variablefonts). It applies to `next/font/google` only.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `style: 'italic'`: A string - it can be `normal` or `italic` for `next/font/google`
* `style: 'oblique'`: A string - it can take any value for `next/font/local` but is expected to come from [standard font styles](https://developer.mozilla.org/docs/Web/CSS/font-style)
* `style: ['italic','normal']`: An array of 2 values for `next/font/google` - the values are from `normal` and `italic`

### `subsets`

The font [`subsets`](https://fonts.google.com/knowledge/glossary/subsetting) defined by an array of string values with the names of each subset you would like to be [preloaded](/docs/app/api-reference/components/font.md#specifying-a-subset). Fonts specified via `subsets` will have a link preload tag injected into the head when the [`preload`](#preload) option is true, which is the default.

Used in `next/font/google`

* Optional

Examples:

* `subsets: ['latin']`: An array with the subset `latin`

You can find a list of all subsets on the Google Fonts page for your font.

### `axes`

Some variable fonts have extra `axes` that can be included. By default, only the font weight is included to keep the file size down. The possible values of `axes` depend on the specific font.

Used in `next/font/google`

* Optional

Examples:

* `axes: ['slnt']`: An array with value `slnt` for the `Inter` variable font which has `slnt` as additional `axes` as shown [here](https://fonts.google.com/variablefonts?vfquery=inter#font-families). You can find the possible `axes` values for your font by using the filter on the [Google variable fonts page](https://fonts.google.com/variablefonts#font-families) and looking for axes other than `wght`

### `display`

The font [`display`](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display) with possible string [values](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display#values) of `'auto'`, `'block'`, `'swap'`, `'fallback'` or `'optional'` with default value of `'swap'`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `display: 'optional'`: A string assigned to the `optional` value

### `preload`

A boolean value that specifies whether the font should be [preloaded](/docs/app/api-reference/components/font.md#preloading) or not. The default is `true`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `preload: false`

### `fallback`

The fallback font to use if the font cannot be loaded. An array of strings of fallback fonts with no default.

* Optional

Used in `next/font/google` and `next/font/local`

Examples:

* `fallback: ['system-ui', 'arial']`: An array setting the fallback fonts to `system-ui` or `arial`

### `adjustFontFallback`

* For `next/font/google`: A boolean value that sets whether an automatic fallback font should be used to reduce [Cumulative Layout Shift](https://web.dev/cls/). The default is `true`.
* For `next/font/local`: A string or boolean `false` value that sets whether an automatic fallback font should be used to reduce [Cumulative Layout Shift](https://web.dev/cls/). The possible values are `'Arial'`, `'Times New Roman'` or `false`. The default is `'Arial'`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `adjustFontFallback: false`: for `next/font/google`
* `adjustFontFallback: 'Times New Roman'`: for `next/font/local`

### `variable`

A string value to define the CSS variable name to be used if the style is applied with the [CSS variable method](#css-variables).

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `variable: '--my-font'`: The CSS variable `--my-font` is declared

### `declarations`

An array of font face [descriptor](https://developer.mozilla.org/docs/Web/CSS/@font-face#descriptors) key-value pairs that define the generated `@font-face` further.

Used in `next/font/local`

* Optional

Examples:

* `declarations: [{ prop: 'ascent-override', value: '90%' }]`

## Examples

## Google Fonts

To use a Google font, import it from `next/font/google` as a function. We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility.

```tsx filename="app/layout.tsx" switcher
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

If you can't use a variable font, you will **need to specify a weight**:

```tsx filename="app/layout.tsx" switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
  display: 'swap',
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

```jsx filename="app/layout.js" switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

You can specify multiple weights and/or styles by using an array:

```jsx filename="app/layout.js"
const roboto = Roboto({
  weight: ['400', '700'],
  style: ['normal', 'italic'],
  subsets: ['latin'],
  display: 'swap',
})
```

> **Good to know**: Use an underscore (\_) for font names with multiple words. E.g. `Roboto Mono` should be imported as `Roboto_Mono`.

### Specifying a subset

Google Fonts are automatically [subset](https://fonts.google.com/knowledge/glossary/subsetting). This reduces the size of the font file and improves performance. You'll need to define which of these subsets you want to preload. Failing to specify any subsets while [`preload`](/docs/app/api-reference/components/font.md#preload) is `true` will result in a warning.

This can be done by adding it to the function call:

```tsx filename="app/layout.tsx" switcher
const inter = Inter({ subsets: ['latin'] })
```

```jsx filename="app/layout.js" switcher
const inter = Inter({ subsets: ['latin'] })
```

View the [Font API Reference](/docs/app/api-reference/components/font.md) for more information.

## Using Multiple Fonts

You can import and use multiple fonts in your application. There are two approaches you can take.

The first approach is to create a utility function that exports a font, imports it, and applies its `className` where needed. This ensures the font is preloaded only when it's rendered:

```ts filename="app/fonts.ts" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

export const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
})
```

```js filename="app/fonts.js" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

export const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
})
```

```tsx filename="app/layout.tsx" switcher
import { inter } from './fonts'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={inter.className}>
      <body>
        <div>{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { inter } from './fonts'

export default function Layout({ children }) {
  return (
    <html lang="en" className={inter.className}>
      <body>
        <div>{children}</div>
      </body>
    </html>
  )
}
```

```tsx filename="app/page.tsx" switcher
import { roboto_mono } from './fonts'

export default function Page() {
  return (
    <>
      <h1 className={roboto_mono.className}>My page</h1>
    </>
  )
}
```

```jsx filename="app/page.js" switcher
import { roboto_mono } from './fonts'

export default function Page() {
  return (
    <>
      <h1 className={roboto_mono.className}>My page</h1>
    </>
  )
}
```

In the example above, `Inter` will be applied globally, and `Roboto Mono` can be imported and applied as needed.

Alternatively, you can create a [CSS variable](/docs/app/api-reference/components/font.md#variable) and use it with your preferred CSS solution:

```tsx filename="app/layout.tsx" switcher
import { Inter, Roboto_Mono } from 'next/font/google'
import styles from './global.css'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  variable: '--font-roboto-mono',
  display: 'swap',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={`${inter.variable} ${roboto_mono.variable}`}>
      <body>
        <h1>My App</h1>
        <div>{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  variable: '--font-roboto-mono',
  display: 'swap',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${inter.variable} ${roboto_mono.variable}`}>
      <body>
        <h1>My App</h1>
        <div>{children}</div>
      </body>
    </html>
  )
}
```

```css filename="app/global.css"
html {
  font-family: var(--font-inter);
}

h1 {
  font-family: var(--font-roboto-mono);
}
```

In the example above, `Inter` will be applied globally, and any `<h1>` tags will be styled with `Roboto Mono`.

> **Recommendation**: Use multiple fonts conservatively since each new font is an additional resource the client has to download.

### Local Fonts

Import `next/font/local` and specify the `src` of your local font file. We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility.

```tsx filename="app/layout.tsx" switcher
import localFont from 'next/font/local'

// Font files can be colocated inside of `app`
const myFont = localFont({
  src: './my-font.woff2',
  display: 'swap',
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

// Font files can be colocated inside of `app`
const myFont = localFont({
  src: './my-font.woff2',
  display: 'swap',
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

View the [Font API Reference](/docs/app/api-reference/components/font.md) for more information.

### With Tailwind CSS

`next/font` integrates seamlessly with [Tailwind CSS](https://tailwindcss.com/) using [CSS variables](/docs/app/api-reference/components/font.md#css-variables).

In the example below, we use the `Inter` and `Roboto_Mono` fonts from `next/font/google` (you can use any Google Font or Local Font). Use the `variable` option to define a CSS variable name, such as `inter` and `roboto_mono` for these fonts, respectively. Then, apply `inter.variable` and `roboto_mono.variable` to include the CSS variables in your HTML document.

> **Good to know**: You can add these variables to the `<html>` or `<body>` tag, depending on your preference, styling needs or project requirements.

```tsx filename="app/layout.tsx" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-roboto-mono',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${roboto_mono.variable} antialiased`}
    >
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-roboto-mono',
})

export default function RootLayout({ children }) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${roboto_mono.variable} antialiased`}
    >
      <body>{children}</body>
    </html>
  )
}
```

Finally, add the CSS variable to your [Tailwind CSS config](/docs/app/getting-started/css.md#tailwind-css):

```css filename="global.css"
@import 'tailwindcss';

@theme inline {
  --font-sans: var(--font-inter);
  --font-mono: var(--font-roboto-mono);
}
```

### Tailwind CSS v3

```js filename="tailwind.config.js"
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        mono: ['var(--font-roboto-mono)'],
      },
    },
  },
  plugins: [],
}
```

You can now use the `font-sans` and `font-mono` utility classes to apply the font to your elements.

```html
<p class="font-sans ...">The quick brown fox ...</p>
<p class="font-mono ...">The quick brown fox ...</p>
```

### Applying Styles

You can apply the font styles in three ways:

* [`className`](#classname)
* [`style`](#style-1)
* [CSS Variables](#css-variables)

#### `className`

Returns a read-only CSS `className` for the loaded font to be passed to an HTML element.

```tsx
<p className={inter.className}>Hello, Next.js!</p>
```

#### `style`

Returns a read-only CSS `style` object for the loaded font to be passed to an HTML element, including `style.fontFamily` to access the font family name and fallback fonts.

```tsx
<p style={inter.style}>Hello World</p>
```

#### CSS Variables

If you would like to set your styles in an external style sheet and specify additional options there, use the CSS variable method.

In addition to importing the font, also import the CSS file where the CSS variable is defined and set the variable option of the font loader object as follows:

```tsx filename="app/page.tsx" switcher
import { Inter } from 'next/font/google'
import styles from '../styles/component.module.css'

const inter = Inter({
  variable: '--font-inter',
})
```

```jsx filename="app/page.js" switcher
import { Inter } from 'next/font/google'
import styles from '../styles/component.module.css'

const inter = Inter({
  variable: '--font-inter',
})
```

To use the font, set the `className` of the parent container of the text you would like to style to the font loader's `variable` value and the `className` of the text to the `styles` property from the external CSS file.

```tsx filename="app/page.tsx" switcher
<main className={inter.variable}>
  <p className={styles.text}>Hello World</p>
</main>
```

```jsx filename="app/page.js" switcher
<main className={inter.variable}>
  <p className={styles.text}>Hello World</p>
</main>
```

Define the `text` selector class in the `component.module.css` CSS file as follows:

```css filename="styles/component.module.css"
.text {
  font-family: var(--font-inter);
  font-weight: 200;
  font-style: italic;
}
```

In the example above, the text `Hello World` is styled using the `Inter` font and the generated font fallback with `font-weight: 200` and `font-style: italic`.

### Using a font definitions file

Every time you call the `localFont` or Google font function, that font will be hosted as one instance in your application. Therefore, if you need to use the same font in multiple places, you should load it in one place and import the related font object where you need it. This is done using a font definitions file.

For example, create a `fonts.ts` file in a `styles` folder at the root of your app directory.

Then, specify your font definitions as follows:

```ts filename="styles/fonts.ts" switcher
import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
import localFont from 'next/font/local'

// define your variable fonts
const inter = Inter()
const lora = Lora()
// define 2 weights of a non-variable font
const sourceCodePro400 = Source_Sans_3({ weight: '400' })
const sourceCodePro700 = Source_Sans_3({ weight: '700' })
// define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

```js filename="styles/fonts.js" switcher
import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
import localFont from 'next/font/local'

// define your variable fonts
const inter = Inter()
const lora = Lora()
// define 2 weights of a non-variable font
const sourceCodePro400 = Source_Sans_3({ weight: '400' })
const sourceCodePro700 = Source_Sans_3({ weight: '700' })
// define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

You can now use these definitions in your code as follows:

```tsx filename="app/page.tsx" switcher
import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

export default function Page() {
  return (
    <div>
      <p className={inter.className}>Hello world using Inter font</p>
      <p style={lora.style}>Hello world using Lora font</p>
      <p className={sourceCodePro700.className}>
        Hello world using Source_Sans_3 font with weight 700
      </p>
      <p className={greatVibes.className}>My title in Great Vibes font</p>
    </div>
  )
}
```

```jsx filename="app/page.js" switcher
import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

export default function Page() {
  return (
    <div>
      <p className={inter.className}>Hello world using Inter font</p>
      <p style={lora.style}>Hello world using Lora font</p>
      <p className={sourceCodePro700.className}>
        Hello world using Source_Sans_3 font with weight 700
      </p>
      <p className={greatVibes.className}>My title in Great Vibes font</p>
    </div>
  )
}
```

To make it easier to access the font definitions in your code, you can define a path alias in your `tsconfig.json` or `jsconfig.json` files as follows:

```json filename="tsconfig.json"
{
  "compilerOptions": {
    "paths": {
      "@/fonts": ["./styles/fonts"]
    }
  }
}
```

You can now import any font definition as follows:

```tsx filename="app/about/page.tsx" switcher
import { greatVibes, sourceCodePro400 } from '@/fonts'
```

```jsx filename="app/about/page.js" switcher
import { greatVibes, sourceCodePro400 } from '@/fonts'
```

### Preloading

When a font function is called on a page of your site, it is not globally available and preloaded on all routes. Rather, the font is only preloaded on the related routes based on the type of file where it is used:

* If it's a [unique page](/docs/app/api-reference/file-conventions/page.md), it is preloaded on the unique route for that page.
* If it's a [layout](/docs/app/api-reference/file-conventions/layout.md), it is preloaded on all the routes wrapped by the layout.
* If it's the [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout), it is preloaded on all routes.

## Version Changes

| Version   | Changes                                                               |
| --------- | --------------------------------------------------------------------- |
| `v13.2.0` | `@next/font` renamed to `next/font`. Installation no longer required. |
| `v13.0.0` | `@next/font` was added.                                               |


--------------------------------------------------------------------------------
title: "Form Component"
description: "Learn how to use the `<Form>` component to handle form submissions and search params updates with client-side navigation."
source: "https://nextjs.org/docs/app/api-reference/components/form"
--------------------------------------------------------------------------------

# Form Component

The `<Form>` component extends the HTML `<form>` element to provide [**prefetching**](/docs/app/getting-started/linking-and-navigating.md#prefetching) of [loading UI](/docs/app/api-reference/file-conventions/loading.md), **client-side navigation** on submission, and **progressive enhancement**.

It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.

Basic usage:

```tsx filename="/app/ui/search.tsx" switcher
import Form from 'next/form'

export default function Page() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?query=abc */}
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

```jsx filename="/app/ui/search.js" switcher
import Form from 'next/form'

export default function Search() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?query=abc */}
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

## Reference

The behavior of the `<Form>` component depends on whether the `action` prop is passed a `string` or `function`.

* When `action` is a **string**, the `<Form>` behaves like a native HTML form that uses a **`GET`** method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
  * [Prefetches](/docs/app/getting-started/linking-and-navigating.md#prefetching) the path when the form becomes visible, this preloads shared UI (e.g. `layout.js` and `loading.js`), resulting in faster navigation.
  * Performs a [client-side navigation](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions) instead of a full page reload when the form is submitted. This retains shared UI and client-side state.
* When `action` is a **function** (Server Action), `<Form>` behaves like a [React form](https://react.dev/reference/react-dom/components/form), executing the action when the form is submitted.

### `action` (string) Props

When `action` is a string, the `<Form>` component supports the following props:

| Prop       | Example            | Type                            | Required |
| ---------- | ------------------ | ------------------------------- | -------- |
| `action`   | `action="/search"` | `string` (URL or relative path) | Yes      |
| `replace`  | `replace={false}`  | `boolean`                       | -        |
| `scroll`   | `scroll={true}`    | `boolean`                       | -        |
| `prefetch` | `prefetch={true}`  | `boolean`                       | -        |

* **`action`**: The URL or path to navigate to when the form is submitted.
  * An empty string `""` will navigate to the same route with updated search params.
* **`replace`**: Replaces the current history state instead of pushing a new one to the [browser's history](https://developer.mozilla.org/en-US/docs/Web/API/History_API) stack. Default is `false`.
* **`scroll`**: Controls the scroll behavior during navigation. Defaults to `true`, this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.
* **`prefetch`**: Controls whether the path should be prefetched when the form becomes visible in the user's viewport. Defaults to `true`.

### `action` (function) Props

When `action` is a function, the `<Form>` component supports the following prop:

| Prop     | Example             | Type                       | Required |
| -------- | ------------------- | -------------------------- | -------- |
| `action` | `action={myAction}` | `function` (Server Action) | Yes      |

* **`action`**: The Server Action to be called when the form is submitted. See the [React docs](https://react.dev/reference/react-dom/components/form#props) for more.

> **Good to know**: When `action` is a function, the `replace` and `scroll` props are ignored.

### Caveats

* **`formAction`**: Can be used in a `<button>` or `<input type="submit">` fields to override the `action` prop. Next.js will perform a client-side navigation, however, this approach doesn't support prefetching.
  * When using [`basePath`](/docs/app/api-reference/config/next-config-js/basePath.md), you must also include it in the `formAction` path. e.g. `formAction="/base-path/search"`.
* **`key`**: Passing a `key` prop to a string `action` is not supported. If you'd like to trigger a re-render or perform a mutation, consider using a function `action` instead.

- **`onSubmit`**: Can be used to handle form submission logic. However, calling `event.preventDefault()` will override `<Form>` behavior such as navigating to the specified URL.
- **[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method), [`encType`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype), [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#target)**: Are not supported as they override `<Form>` behavior.
  * Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
  * If you need to use these props, use the HTML `<form>` element instead.
- **`<input type="file">`**: Using this input type when the `action` is a string will match browser behavior by submitting the filename instead of the file object.

## Examples

### Search form that leads to a search result page

You can create a search form that navigates to a search results page by passing the path as an `action`:

```tsx filename="/app/page.tsx" switcher
import Form from 'next/form'

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

```jsx filename="/app/page.js" switcher
import Form from 'next/form'

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

When the user updates the query input field and submits the form, the form data will be encoded into the URL as search params, e.g. `/search?query=abc`.

> **Good to know**: If you pass an empty string `""` to `action`, the form will navigate to the same route with updated search params.

On the results page, you can access the query using the [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) `page.js` prop and use it to fetch data from an external source.

```tsx filename="/app/search/page.tsx" switcher
import { getSearchResults } from '@/lib/search'

export default async function SearchPage({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const results = await getSearchResults((await searchParams).query)

  return <div>...</div>
}
```

```jsx filename="/app/search/page.js" switcher
import { getSearchResults } from '@/lib/search'

export default async function SearchPage({ searchParams }) {
  const results = await getSearchResults((await searchParams).query)

  return <div>...</div>
}
```

When the `<Form>` becomes visible in the user's viewport, shared UI (such as `layout.js` and `loading.js`) on the `/search` page will be prefetched. On submission, the form will immediately navigate to the new route and show loading UI while the results are being fetched. You can design the fallback UI using [`loading.js`](/docs/app/api-reference/file-conventions/loading.md):

```tsx filename="/app/search/loading.tsx" switcher
export default function Loading() {
  return <div>Loading...</div>
}
```

```jsx filename="/app/search/loading.js" switcher
export default function Loading() {
  return <div>Loading...</div>
}
```

To cover cases when shared UI hasn't yet loaded, you can show instant feedback to the user using [`useFormStatus`](https://react.dev/reference/react-dom/hooks/useFormStatus).

First, create a component that displays a loading state when the form is pending:

```tsx filename="/app/ui/search-button.tsx" switcher
'use client'
import { useFormStatus } from 'react-dom'

export default function SearchButton() {
  const status = useFormStatus()
  return (
    <button type="submit">{status.pending ? 'Searching...' : 'Search'}</button>
  )
}
```

```jsx filename="/app/ui/search-button.js" switcher
'use client'
import { useFormStatus } from 'react-dom'

export default function SearchButton() {
  const status = useFormStatus()
  return (
    <button type="submit">{status.pending ? 'Searching...' : 'Search'}</button>
  )
}
```

Then, update the search form page to use the `SearchButton` component:

```tsx filename="/app/page.tsx" switcher
import Form from 'next/form'
import { SearchButton } from '@/ui/search-button'

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <SearchButton />
    </Form>
  )
}
```

```jsx filename="/app/ui/search-button.js" switcher
import Form from 'next/form'
import { SearchButton } from '@/ui/search-button'

export default function Page() {
  return (
    <Form action="/search">
      <input name="query" />
      <SearchButton />
    </Form>
  )
}
```

### Mutations with Server Actions

You can perform mutations by passing a function to the `action` prop.

```tsx filename="/app/posts/create/page.tsx" switcher
import Form from 'next/form'
import { createPost } from '@/posts/actions'

export default function Page() {
  return (
    <Form action={createPost}>
      <input name="title" />
      {/* ... */}
      <button type="submit">Create Post</button>
    </Form>
  )
}
```

```jsx filename="/app/posts/create/page.js" switcher
import Form from 'next/form'
import { createPost } from '@/posts/actions'

export default function Page() {
  return (
    <Form action={createPost}>
      <input name="title" />
      {/* ... */}
      <button type="submit">Create Post</button>
    </Form>
  )
}
```

After a mutation, it's common to redirect to the new resource. You can use the [`redirect`](/docs/app/guides/redirecting.md) function from `next/navigation` to navigate to the new post page.

> **Good to know**: Since the "destination" of the form submission is not known until the action is executed, `<Form>` cannot automatically prefetch shared UI.

```tsx filename="/app/posts/actions.ts" switcher
'use server'
import { redirect } from 'next/navigation'

export async function createPost(formData: FormData) {
  // Create a new post
  // ...

  // Redirect to the new post
  redirect(`/posts/${data.id}`)
}
```

```jsx filename="/app/posts/actions.js" switcher
'use server'
import { redirect } from 'next/navigation'

export async function createPost(formData) {
  // Create a new post
  // ...

  // Redirect to the new post
  redirect(`/posts/${data.id}`)
}
```

Then, in the new page, you can fetch data using the `params` prop:

```tsx filename="/app/posts/[id]/page.tsx" switcher
import { getPost } from '@/posts/data'

export default async function PostPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const data = await getPost(id)

  return (
    <div>
      <h1>{data.title}</h1>
      {/* ... */}
    </div>
  )
}
```

```jsx filename="/app/posts/[id]/page.js" switcher
import { getPost } from '@/posts/data'

export default async function PostPage({ params }) {
  const { id } = await params
  const data = await getPost(id)

  return (
    <div>
      <h1>{data.title}</h1>
      {/* ... */}
    </div>
  )
}
```

See the [Server Actions](/docs/app/getting-started/updating-data.md) docs for more examples.


--------------------------------------------------------------------------------
title: "Image Component"
description: "Optimize Images in your Next.js Application using the built-in `next/image` Component."
source: "https://nextjs.org/docs/app/api-reference/components/image"
--------------------------------------------------------------------------------

# Image Component

The Next.js Image component extends the HTML `<img>` element for automatic image optimization.

```jsx filename="app/page.js"
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      width={500}
      height={500}
      alt="Picture of the author"
    />
  )
}
```

## Reference

### Props

The following props are available:

#### `src`

The source of the image. Can be one of the following:

An internal path string.

```jsx
<Image src="/profile.png" />
```

An absolute external URL (must be configured with [remotePatterns](#remotepatterns)).

```jsx
<Image src="https://example.com/profile.png" />
```

A static import.

```jsx
import profile from './profile.png'

export default function Page() {
  return <Image src={profile} />
}
```

> **Good to know**: For security reasons, the Image Optimization API using the default [loader](#loader) will *not* forward headers when fetching the `src` image.
> If the `src` image requires authentication, consider using the [unoptimized](#unoptimized) property to disable Image Optimization.

#### `alt`

The `alt` property is used to describe the image for screen readers and search engines. It is also the fallback text if images have been disabled or an error occurs while loading the image.

It should contain text that could replace the image [without changing the meaning of the page](https://html.spec.whatwg.org/multipage/images.html#general-guidelines). It is not meant to supplement the image and should not repeat information that is already provided in the captions above or below the image.

If the image is [purely decorative](https://html.spec.whatwg.org/multipage/images.html#a-purely-decorative-image-that-doesn't-add-any-information) or [not intended for the user](https://html.spec.whatwg.org/multipage/images.html#an-image-not-intended-for-the-user), the `alt` property should be an empty string (`alt=""`).

> Learn more about [image accessibility guidelines](https://html.spec.whatwg.org/multipage/images.html#alt).

#### `width` and `height`

The `width` and `height` properties represent the [intrinsic](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size) image size in pixels. This property is used to infer the correct **aspect ratio** used by browsers to reserve space for the image and avoid layout shift during loading. It does not determine the *rendered size* of the image, which is controlled by CSS.

```jsx
<Image src="/profile.png" width={500} height={500} />
```

You **must** set both `width` and `height` properties unless:

* The image is statically imported.
* The image has the [`fill` property](#fill)

If the height and width are unknown, we recommend using the [`fill` property](#fill).

#### `fill`

A boolean that causes the image to expand to the size of the parent element.

```js
<Image src="/profile.png" fill={true} />
```

**Positioning**:

* The parent element **must** assign `position: "relative"`, `"fixed"`, `"absolute"`.
* By default, the `<img>` element uses `position: "absolute"`.

**Object Fit**:

If no styles are applied to the image, the image will stretch to fit the container. You can use `objectFit` to control cropping and scaling.

* `"contain"`: The image will be scaled down to fit the container and preserve aspect ratio.
* `"cover"`: The image will fill the container and be cropped.

> Learn more about [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position) and [`object-fit`](https://developer.mozilla.org/docs/Web/CSS/object-fit).

#### `loader`

A custom function used to generate the image URL. The function receives the following parameters, and returns a URL string for the image:

* [`src`](#src)
* [`width`](#width-and-height)
* [`quality`](#quality)

```js
'use client'

import Image from 'next/image'

const imageLoader = ({ src, width, quality }) => {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}

export default function Page() {
  return (
    <Image
      loader={imageLoader}
      src="me.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

> **Good to know**: Using props like `onLoad`, which accept a function, requires using [Client Components](https://react.dev/reference/rsc/use-client) to serialize the provided function.

Alternatively, you can use the [loaderFile](#loaderfile) configuration in `next.config.js` to configure every instance of `next/image` in your application, without passing a prop.

#### `sizes`

Define the sizes of the image at different breakpoints. Used by the browser to choose the most appropriate size from the generated `srcset`.

```jsx
import Image from 'next/image'

export default function Page() {
  return (
    <div className="grid-element">
      <Image
        fill
        src="/example.png"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      />
    </div>
  )
}
```

`sizes` should be used when:

* The image is using the [`fill`](#fill) prop
* CSS is used to make the image responsive

If `sizes` is missing, the browser assumes the image will be as wide as the viewport (`100vw`). This can cause unnecessarily large images to be downloaded.

In addition, `sizes` affects how `srcset` is generated:

* Without `sizes`: Next.js generates a limited `srcset` (e.g. 1x, 2x), suitable for fixed-size images.
* With `sizes`: Next.js generates a full `srcset` (e.g. 640w, 750w, etc.), optimized for responsive layouts.

> Learn more about `srcset` and `sizes` on [web.dev](https://web.dev/learn/design/responsive-images/#sizes) and [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#sizes).

#### `quality`

An integer between `1` and `100` that sets the quality of the optimized image. Higher values increase file size and visual fidelity. Lower values reduce file size but may affect sharpness.

```jsx
// Default quality is 75
<Image quality={75} />
```

If you’ve configured [qualities](#qualities) in `next.config.js`, the value must match one of the allowed entries.

> **Good to know**: If the original image is already low quality, setting a high quality value will increase the file size without improving appearance.

#### `style`

Allows passing CSS styles to the underlying image element.

```jsx
const imageStyle = {
  borderRadius: '50%',
  border: '1px solid #fff',
  width: '100px',
  height: 'auto',
}

export default function ProfileImage() {
  return <Image src="..." style={imageStyle} />
}
```

> **Good to know**: If you’re using the `style` prop to set a custom width, be sure to also set `height: 'auto'` to preserve the image’s aspect ratio.

#### `preload`

A boolean that indicates if the image should be preloaded.

```jsx
// Default preload is false
<Image preload={false} />
```

* `true`: [Preloads](https://web.dev/preload-responsive-images/) the image by inserting a `<link>` in the `<head>`.
* `false`: Does not preload the image.

**When to use it:**

* The image is the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element.
* The image is above the fold, typically the hero image.
* You want to begin loading the image in the `<head>`, before its discovered later in the `<body>`.

**When not to use it:**

* When you have multiple images that could be considered the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element depending on the viewport.
* When the `loading` property is used.
* When the `fetchPriority` property is used.

In most cases, you should use `loading="eager"` or `fetchPriority="high"` instead of `preload`.

#### `priority`

Starting with Next.js 16, the `priority` property has been deprecated in favor of the [`preload`](#preload) property in order to make the behavior clear.

#### `loading`

Controls when the image should start loading.

```jsx
// Defaults to lazy
<Image loading="lazy" />
```

* `lazy`: Defer loading the image until it reaches a calculated distance from the viewport.
* `eager`: Load the image immediately, regardless of its position in the page.

Use `eager` only when you want to ensure the image is loaded immediately.

> Learn more about the [`loading` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#loading).

#### `placeholder`

Specifies a placeholder to use while the image is loading, improving the perceived loading performance.

```jsx
// defaults to empty
<Image placeholder="empty" />
```

* `empty`: No placeholder while the image is loading.
* `blur`: Use a blurred version of the image as a placeholder. Must be used with the [`blurDataURL`](#blurdataurl) property.
* `data:image/...`: Uses the [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) as the placeholder.

**Examples:**

* [`blur` placeholder](https://image-component.nextjs.gallery/placeholder)
* [Shimmer effect with data URL `placeholder` prop](https://image-component.nextjs.gallery/shimmer)
* [Color effect with `blurDataURL` prop](https://image-component.nextjs.gallery/color)

> Learn more about the [`placeholder` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#placeholder).

#### `blurDataURL`

A [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) to
be used as a placeholder image before the image successfully loads. Can be automatically set or used with the [`placeholder="blur"`](#placeholder) property.

```jsx
<Image placeholder="blur" blurDataURL="..." />
```

The image is automatically enlarged and blurred, so a very small image (10px or less) is recommended.

**Automatic**

If `src` is a static import of a `jpg`, `png`, `webp`, or `avif` file, `blurDataURL` is added automatically—unless the image is animated.

**Manually set**

If the image is dynamic or remote, you must provide `blurDataURL` yourself. To generate one, you can use:

* [A online tool like png-pixel.com](https://png-pixel.com)
* [A library like Plaiceholder](https://github.com/joe-bell/plaiceholder)

A large blurDataURL may hurt performance. Keep it small and simple.

**Examples:**

* [Default `blurDataURL` prop](https://image-component.nextjs.gallery/placeholder)
* [Color effect with `blurDataURL` prop](https://image-component.nextjs.gallery/color)

#### `onLoad`

A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

```jsx
<Image onLoad={(e) => console.log(e.target.naturalWidth)} />
```

The callback function will be called with one argument, the event which has a `target` that references the underlying `<img>` element.

> **Good to know**: Using props like `onLoad`, which accept a function, requires using [Client Components](https://react.dev/reference/rsc/use-client) to serialize the provided function.

#### `onError`

A callback function that is invoked if the image fails to load.

```jsx
<Image onError={(e) => console.error(e.target.id)} />
```

> **Good to know**: Using props like `onError`, which accept a function, requires using [Client Components](https://react.dev/reference/rsc/use-client) to serialize the provided function.

#### `unoptimized`

A boolean that indicates if the image should be optimized. This is useful for images that do not benefit from optimization such as small images (less than 1KB), vector images (SVG), or animated images (GIF).

```js
import Image from 'next/image'

const UnoptimizedImage = (props) => {
  // Default is false
  return <Image {...props} unoptimized />
}
```

* `true`: The source image will be served as-is from the `src` instead of changing quality, size, or format.
* `false`: The source image will be optimized.

Since Next.js 12.3.0, this prop can be assigned to all images by updating `next.config.js` with the following configuration:

```js filename="next.config.js"
module.exports = {
  images: {
    unoptimized: true,
  },
}
```

#### `overrideSrc`

When providing the `src` prop to the `<Image>` component, both the `srcset` and `src` attributes are generated automatically for the resulting `<img>`.

```jsx filename="input.js"
<Image src="/profile.jpg" />
```

```html filename="output.html"
<img
  srcset="
    /_next/image?url=%2Fprofile.jpg&w=640&q=75 1x,
    /_next/image?url=%2Fprofile.jpg&w=828&q=75 2x
  "
  src="/_next/image?url=%2Fprofile.jpg&w=828&q=75"
/>
```

In some cases, it is not desirable to have the `src` attribute generated and you may wish to override it using the `overrideSrc` prop.

For example, when upgrading an existing website from `<img>` to `<Image>`, you may wish to maintain the same `src` attribute for SEO purposes such as image ranking or avoiding recrawl.

```jsx filename="input.js"
<Image src="/profile.jpg" overrideSrc="/override.jpg" />
```

```html filename="output.html"
<img
  srcset="
    /_next/image?url=%2Fprofile.jpg&w=640&q=75 1x,
    /_next/image?url=%2Fprofile.jpg&w=828&q=75 2x
  "
  src="/override.jpg"
/>
```

#### `decoding`

A hint to the browser indicating if it should wait for the image to be decoded before presenting other content updates or not.

```jsx
// Default is async
<Image decoding="async" />
```

* `async`: Asynchronously decode the image and allow other content to be rendered before it completes.
* `sync`: Synchronously decode the image for atomic presentation with other content.
* `auto`: No preference. The browser chooses the best approach.

> Learn more about the [`decoding` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#decoding).

### Other Props

Other properties on the `<Image />` component will be passed to the underlying `img` element with the exception of the following:

* `srcSet`: Use [Device Sizes](#devicesizes) instead.

### Deprecated props

#### `onLoadingComplete`

> **Warning**: Deprecated in Next.js 14, use [`onLoad`](#onload) instead.

A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

The callback function will be called with one argument, a reference to the underlying `<img>` element.

```jsx
'use client'

<Image onLoadingComplete={(img) => console.log(img.naturalWidth)} />
```

> **Good to know**: Using props like `onLoadingComplete`, which accept a function, requires using [Client Components](https://react.dev/reference/rsc/use-client) to serialize the provided function.

### Configuration options

You can configure the Image Component in `next.config.js`. The following options are available:

#### `localPatterns`

Use `localPatterns` in your `next.config.js` file to allow images from specific local paths to be optimized and block all others.

```js filename="next.config.js"
module.exports = {
  images: {
    localPatterns: [
      {
        pathname: '/assets/images/**',
        search: '',
      },
    ],
  },
}
```

The example above will ensure the `src` property of `next/image` must start with `/assets/images/` and must not have a query string. Attempting to optimize any other path will respond with `400` Bad Request error.

> **Good to know**: Omitting the `search` property allows all search parameters which could allow malicious actors to optimize URLs you did not intend. Try using a specific value like `search: '?v=2'` to ensure an exact match.

#### `remotePatterns`

Use `remotePatterns` in your `next.config.js` file to allow images from specific external paths and block all others. This ensures that only external images from your account can be served.

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [new URL('https://example.com/account123/**')],
  },
}
```

You can also configure `remotePatterns` using the object:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        port: '',
        pathname: '/account123/**',
        search: '',
      },
    ],
  },
}
```

The example above will ensure the `src` property of `next/image` must start with `https://example.com/account123/` and must not have a query string. Any other protocol, hostname, port, or unmatched path will respond with `400` Bad Request.

**Wildcard Patterns:**

Wildcard patterns can be used for both `pathname` and `hostname` and have the following syntax:

* `*` match a single path segment or subdomain
* `**` match any number of path segments at the end or subdomains at the beginning. This syntax does not work in the middle of the pattern.

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.example.com',
        port: '',
        search: '',
      },
    ],
  },
}
```

This allows subdomains like `image.example.com`. Query strings and custom ports are still blocked.

> **Good to know**: When omitting `protocol`, `port`, `pathname`, or `search` then the wildcard `**` is implied. This is not recommended because it may allow malicious actors to optimize urls you did not intend.

**Query Strings**:

You can also restrict query strings using the `search` property:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'assets.example.com',
        search: '?v=1727111025337',
      },
    ],
  },
}
```

The example above will ensure the `src` property of `next/image` must start with `https://assets.example.com` and must have the exact query string `?v=1727111025337`. Any other protocol or query string will respond with `400` Bad Request.

#### `loaderFile`

`loaderFiles` allows you to use a custom image optimization service instead of Next.js.

```js filename="next.config.js"
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```

The path must be relative to the project root. The file must export a default function that returns a URL string:

```js filename="my/image/loader.js"
'use client'

export default function myImageLoader({ src, width, quality }) {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}
```

**Example:**

* [Custom Image Loader Configuration](/docs/app/api-reference/config/next-config-js/images.md#example-loader-configuration)

> Alternatively, you can use the [`loader` prop](#loader) to configure each instance of `next/image`.

#### `path`

If you want to change or prefix the default path for the Image Optimization API, you can do so with the `path` property. The default value for `path` is `/_next/image`.

```js filename="next.config.js"
module.exports = {
  images: {
    path: '/my-prefix/_next/image',
  },
}
```

#### `deviceSizes`

`deviceSizes` allows you to specify a list of device width breakpoints. These widths are used when the `next/image` component uses [`sizes`](#sizes) prop to ensure the correct image is served for the user's device.

If no configuration is provided, the default below is used:

```js filename="next.config.js"
module.exports = {
  images: {
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
  },
}
```

#### `imageSizes`

`imageSizes` allows you to specify a list of image widths. These widths are concatenated with the array of [device sizes](#devicesizes) to form the full array of sizes used to generate image [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset).

If no configuration is provided, the default below is used:

```js filename="next.config.js"
module.exports = {
  images: {
    imageSizes: [32, 48, 64, 96, 128, 256, 384],
  },
}
```

`imageSizes` is only used for images which provide a [`sizes`](#sizes) prop, which indicates that the image is less than the full width of the screen. Therefore, the sizes in `imageSizes` should all be smaller than the smallest size in `deviceSizes`.

#### `qualities`

`qualities` allows you to specify a list of image quality values.

If not configuration is provided, the default below is used:

```js filename="next.config.js"
module.exports = {
  images: {
    qualities: [75],
  },
}
```

> **Good to know**: This field is required starting with Next.js 16 because unrestricted access could allow malicious actors to optimize more qualities than you intended.

You can add more image qualities to the allowlist, such as the following:

```js filename="next.config.js"
module.exports = {
  images: {
    qualities: [25, 50, 75, 100],
  },
}
```

In the example above, only four qualities are allowed: 25, 50, 75, and 100.

If the [`quality`](#quality) prop does not match a value in this array, the closest allowed value will be used.

If the REST API is visited directly with a quality that does not match a value in this array, the server will return a 400 Bad Request response.

#### `formats`

`formats` allows you to specify a list of image formats to be used.

```js filename="next.config.js"
module.exports = {
  images: {
    // Default
    formats: ['image/webp'],
  },
}
```

Next.js automatically detects the browser's supported image formats via the request's `Accept` header in order to determine the best output format.

If the `Accept` header matches more than one of the configured formats, the first match in the array is used. Therefore, the array order matters. If there is no match (or the source image is animated), it will use the original image's format.

You can enable AVIF support, which will fallback to the original format of the src image if the browser [does not support AVIF](https://caniuse.com/avif):

```js filename="next.config.js"
module.exports = {
  images: {
    formats: ['image/avif'],
  },
}
```

> **Good to know**:
>
> * We still recommend using WebP for most use cases.
> * AVIF generally takes 50% longer to encode but it compresses 20% smaller compared to WebP. This means that the first time an image is requested, it will typically be slower, but subsequent requests that are cached will be faster.
> * If you self-host with a Proxy/CDN in front of Next.js, you must configure the Proxy to forward the `Accept` header.

#### `minimumCacheTTL`

`minimumCacheTTL` allows you to configure the Time to Live (TTL) in seconds for cached optimized images. In many cases, it's better to use a [Static Image Import](/docs/app/getting-started/images.md#local-images) which will automatically hash the file contents and cache the image forever with a `Cache-Control` header of `immutable`.

If no configuration is provided, the default below is used.

```js filename="next.config.js"
module.exports = {
  images: {
    minimumCacheTTL: 14400, // 4 hours
  },
}
```

You can increase the TTL to reduce the number of revalidations and potentially lower cost:

```js filename="next.config.js"
module.exports = {
  images: {
    minimumCacheTTL: 2678400, // 31 days
  },
}
```

The expiration (or rather Max Age) of the optimized image is defined by either the `minimumCacheTTL` or the upstream image `Cache-Control` header, whichever is larger.

If you need to change the caching behavior per image, you can configure [`headers`](/docs/app/api-reference/config/next-config-js/headers.md) to set the `Cache-Control` header on the upstream image (e.g. `/some-asset.jpg`, not `/_next/image` itself).

There is no mechanism to invalidate the cache at this time, so its best to keep `minimumCacheTTL` low. Otherwise you may need to manually change the [`src`](#src) prop or delete the cached file `<distDir>/cache/images`.

#### `disableStaticImages`

`disableStaticImages` allows you to disable static image imports.

The default behavior allows you to import static files such as `import icon from './icon.png'` and then pass that to the `src` property. In some cases, you may wish to disable this feature if it conflicts with other plugins that expect the import to behave differently.

You can disable static image imports inside your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  images: {
    disableStaticImages: true,
  },
}
```

#### `maximumRedirects`

The default image optimization loader will follow HTTP redirects when fetching remote images up to 3 times.

```js filename="next.config.js"
module.exports = {
  images: {
    maximumRedirects: 3,
  },
}
```

You can configure the number of redirects to follow when fetching remote images. Setting the value to `0` will disable following redirects.

```js filename="next.config.js"
module.exports = {
  images: {
    maximumRedirects: 0,
  },
}
```

#### `dangerouslyAllowLocalIP`

In rare cases when self-hosting Next.js on a private network, you may want to allow optimizing images from local IP addresses on the same network. This is not recommended for most users because it could allow malicious users to access content on your internal network.

By default, the value is false.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowLocalIP: false,
  },
}
```

If you need to optimize remote images hosted elsewhere in your local network, you can set the value to true.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowLocalIP: true,
  },
}
```

#### `dangerouslyAllowSVG`

`dangerouslyAllowSVG` allows you to serve SVG images.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
  },
}
```

By default, Next.js does not optimize SVG images for a few reasons:

* SVG is a vector format meaning it can be resized losslessly.
* SVG has many of the same features as HTML/CSS, which can lead to vulnerabilities without proper [Content Security Policy (CSP) headers](/docs/app/api-reference/config/next-config-js/headers.md#content-security-policy).

We recommend using the [`unoptimized`](#unoptimized) prop when the [`src`](#src) prop is known to be SVG. This happens automatically when `src` ends with `".svg"`.

```jsx
<Image src="/my-image.svg" unoptimized />
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
}
```

#### `contentDispositionType`

`contentDispositionType` allows you to configure the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) header.

```js filename="next.config.js"
module.exports = {
  images: {
    contentDispositionType: 'inline',
  },
}
```

#### `contentSecurityPolicy`

`contentSecurityPolicy` allows you to configure the [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) header for images. This is particularly important when using [`dangerouslyAllowSVG`](#dangerouslyallowsvg) to prevent scripts embedded in the image from executing.

```js filename="next.config.js"
module.exports = {
  images: {
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
}
```

By default, the [loader](#loader) sets the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) header to `attachment` for added protection since the API can serve arbitrary remote images.

The default value is `attachment` which forces the browser to download the image when visiting directly. This is particularly important when [`dangerouslyAllowSVG`](#dangerouslyallowsvg) is true.

You can optionally configure `inline` to allow the browser to render the image when visiting directly, without downloading it.

### Deprecated configuration options

#### `domains`

> **Warning**: Deprecated since Next.js 14 in favor of strict [`remotePatterns`](#remotepatterns) in order to protect your application from malicious users.

Similar to [`remotePatterns`](#remotepatterns), the `domains` configuration can be used to provide a list of allowed hostnames for external images. However, the `domains` configuration does not support wildcard pattern matching and it cannot restrict protocol, port, or pathname.

Since most remote image servers are shared between multiple tenants, it's safer to use `remotePatterns` to ensure only the intended images are optimized.

Below is an example of the `domains` property in the `next.config.js` file:

```js filename="next.config.js"
module.exports = {
  images: {
    domains: ['assets.acme.com'],
  },
}
```

## Functions

### `getImageProps`

The `getImageProps` function can be used to get the props that would be passed to the underlying `<img>` element, and instead pass them to another component, style, canvas, etc.

```jsx
import { getImageProps } from 'next/image'

const { props } = getImageProps({
  src: 'https://example.com/image.jpg',
  alt: 'A scenic mountain view',
  width: 1200,
  height: 800,
})

function ImageWithCaption() {
  return (
    <figure>
      <img {...props} />
      <figcaption>A scenic mountain view</figcaption>
    </figure>
  )
}
```

This also avoid calling React `useState()` so it can lead to better performance, but it cannot be used with the [`placeholder`](#placeholder) prop because the placeholder will never be removed.

## Known browser bugs

This `next/image` component uses browser native [lazy loading](https://caniuse.com/loading-lazy-attr), which may fallback to eager loading for older browsers before Safari 15.4. When using the blur-up placeholder, older browsers before Safari 12 will fallback to empty placeholder. When using styles with `width`/`height` of `auto`, it is possible to cause [Layout Shift](https://web.dev/cls/) on older browsers before Safari 15 that don't [preserve the aspect ratio](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes). For more details, see [this MDN video](https://www.youtube.com/watch?v=4-d_SoCHeWE).

* [Safari 15 - 16.3](https://bugs.webkit.org/show_bug.cgi?id=243601) display a gray border while loading. Safari 16.4 [fixed this issue](https://webkit.org/blog/13966/webkit-features-in-safari-16-4/#:~:text=Now%20in%20Safari%2016.4%2C%20a%20gray%20line%20no%20longer%20appears%20to%20mark%20the%20space%20where%20a%20lazy%2Dloaded%20image%20will%20appear%20once%20it%E2%80%99s%20been%20loaded.). Possible solutions:
  * Use CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }`
  * Use [`loading="eager"`](#loading) if the image is above the fold
* [Firefox 67+](https://bugzilla.mozilla.org/show_bug.cgi?id=1556156) displays a white background while loading. Possible solutions:
  * Enable [AVIF `formats`](#formats)
  * Use [`placeholder`](#placeholder)

## Examples

### Styling images

Styling the Image component is similar to styling a normal `<img>` element, but there are a few guidelines to keep in mind:

Use `className` or `style`, not `styled-jsx`. In most cases, we recommend using the `className` prop. This can be an imported [CSS Module](/docs/app/getting-started/css.md), a [global stylesheet](/docs/app/getting-started/css.md#global-css), etc.

```jsx
import styles from './styles.module.css'

export default function MyImage() {
  return <Image className={styles.image} src="/my-image.png" alt="My Image" />
}
```

You can also use the `style` prop to assign inline styles.

```jsx
export default function MyImage() {
  return (
    <Image style={{ borderRadius: '8px' }} src="/my-image.png" alt="My Image" />
  )
}
```

When using `fill`, the parent element must have `position: relative` or `display: block`. This is necessary for the proper rendering of the image element in that layout mode.

```jsx
<div style={{ position: 'relative' }}>
  <Image fill src="/my-image.png" alt="My Image" />
</div>
```

You cannot use [styled-jsx](/docs/app/guides/css-in-js.md) because it's scoped to the current component (unless you mark the style as `global`).

### Responsive images with a static export

When you import a static image, Next.js automatically sets its width and height based on the file. You can make the image responsive by setting the style:

![Responsive image filling the width and height of its parent container](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/responsive-image.png)

```jsx
import Image from 'next/image'
import mountains from '../public/mountains.jpg'

export default function Responsive() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
      <Image
        alt="Mountains"
        // Importing an image will
        // automatically set the width and height
        src={mountains}
        sizes="100vw"
        // Make the image display full width
        // and preserve its aspect ratio
        style={{
          width: '100%',
          height: 'auto',
        }}
      />
    </div>
  )
}
```

### Responsive images with a remote URL

If the source image is a dynamic or a remote URL, you must provide the width and height props so Next.js can calculate the aspect ratio:

```jsx filename="components/page.js"
import Image from 'next/image'

export default function Page({ photoUrl }) {
  return (
    <Image
      src={photoUrl}
      alt="Picture of the author"
      sizes="100vw"
      style={{
        width: '100%',
        height: 'auto',
      }}
      width={500}
      height={300}
    />
  )
}
```

Try it out:

* [Demo the image responsive to viewport](https://image-component.nextjs.gallery/responsive)

### Responsive image with `fill`

If you don't know the aspect ratio of the image, you can add the [`fill` prop](#fill) with the `objectFit` prop set to `cover`. This will make the image fill the full width of its parent container.

![Grid of images filling parent container width](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/fill-container.png)

```jsx
import Image from 'next/image'
import mountains from '../public/mountains.jpg'

export default function Fill() {
  return (
    <div
      style={{
        display: 'grid',
        gridGap: '8px',
        gridTemplateColumns: 'repeat(auto-fit, minmax(400px, auto))',
      }}
    >
      <div style={{ position: 'relative', width: '400px' }}>
        <Image
          alt="Mountains"
          src={mountains}
          fill
          sizes="(min-width: 808px) 50vw, 100vw"
          style={{
            objectFit: 'cover', // cover, contain, none
          }}
        />
      </div>
      {/* And more images in the grid... */}
    </div>
  )
}
```

### Background Image

Use the `fill` prop to make the image cover the entire screen area:

![Background image taking full width and height of page](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/background-image.png)

```jsx
import Image from 'next/image'
import mountains from '../public/mountains.jpg'

export default function Background() {
  return (
    <Image
      alt="Mountains"
      src={mountains}
      placeholder="blur"
      quality={100}
      fill
      sizes="100vw"
      style={{
        objectFit: 'cover',
      }}
    />
  )
}
```

For examples of the Image component used with the various styles, see the [Image Component Demo](https://image-component.nextjs.gallery).

### Remote images

To use a remote image, the `src` property should be a URL string.

```jsx filename="app/page.js"
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

Since Next.js does not have access to remote files during the build process, you'll need to provide the [`width`](/docs/app/api-reference/components/image.md#width-and-height), [`height`](/docs/app/api-reference/components/image.md#width-and-height) and optional [`blurDataURL`](/docs/app/api-reference/components/image.md#blurdataurl) props manually.

The `width` and `height` attributes are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. The `width` and `height` do *not* determine the rendered size of the image file.

To safely allow optimizing images, define a list of supported URL patterns in `next.config.js`. Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

```js filename="next.config.js"
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

### Theme detection

If you want to display a different image for light and dark mode, you can create a new component that wraps two `<Image>` components and reveals the correct one based on a CSS media query.

```css filename="components/theme-image.module.css"
.imgDark {
  display: none;
}

@media (prefers-color-scheme: dark) {
  .imgLight {
    display: none;
  }
  .imgDark {
    display: unset;
  }
}
```

```tsx filename="components/theme-image.tsx" switcher
import styles from './theme-image.module.css'
import Image, { ImageProps } from 'next/image'

type Props = Omit<ImageProps, 'src' | 'preload' | 'loading'> & {
  srcLight: string
  srcDark: string
}

const ThemeImage = (props: Props) => {
  const { srcLight, srcDark, ...rest } = props

  return (
    <>
      <Image {...rest} src={srcLight} className={styles.imgLight} />
      <Image {...rest} src={srcDark} className={styles.imgDark} />
    </>
  )
}
```

```jsx filename="components/theme-image.js" switcher
import styles from './theme-image.module.css'
import Image from 'next/image'

const ThemeImage = (props) => {
  const { srcLight, srcDark, ...rest } = props

  return (
    <>
      <Image {...rest} src={srcLight} className={styles.imgLight} />
      <Image {...rest} src={srcDark} className={styles.imgDark} />
    </>
  )
}
```

> **Good to know**: The default behavior of `loading="lazy"` ensures that only the correct image is loaded. You cannot use `preload` or `loading="eager"` because that would cause both images to load. Instead, you can use [`fetchPriority="high"`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/fetchPriority).

Try it out:

* [Demo light/dark mode theme detection](https://image-component.nextjs.gallery/theme)

### Art direction

If you want to display a different image for mobile and desktop, sometimes called [Art Direction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction), you can provide different `src`, `width`, `height`, and `quality` props to `getImageProps()`.

```jsx filename="app/page.js"
import { getImageProps } from 'next/image'

export default function Home() {
  const common = { alt: 'Art Direction Example', sizes: '100vw' }
  const {
    props: { srcSet: desktop },
  } = getImageProps({
    ...common,
    width: 1440,
    height: 875,
    quality: 80,
    src: '/desktop.jpg',
  })
  const {
    props: { srcSet: mobile, ...rest },
  } = getImageProps({
    ...common,
    width: 750,
    height: 1334,
    quality: 70,
    src: '/mobile.jpg',
  })

  return (
    <picture>
      <source media="(min-width: 1000px)" srcSet={desktop} />
      <source media="(min-width: 500px)" srcSet={mobile} />
      <img {...rest} style={{ width: '100%', height: 'auto' }} />
    </picture>
  )
}
```

### Background CSS

You can even convert the `srcSet` string to the [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/image/image-set) CSS function to optimize a background image.

```jsx filename="app/page.js"
import { getImageProps } from 'next/image'

function getBackgroundImage(srcSet = '') {
  const imageSet = srcSet
    .split(', ')
    .map((str) => {
      const [url, dpi] = str.split(' ')
      return `url("${url}") ${dpi}`
    })
    .join(', ')
  return `image-set(${imageSet})`
}

export default function Home() {
  const {
    props: { srcSet },
  } = getImageProps({ alt: '', width: 128, height: 128, src: '/img.png' })
  const backgroundImage = getBackgroundImage(srcSet)
  const style = { height: '100vh', width: '100vw', backgroundImage }

  return (
    <main style={style}>
      <h1>Hello World</h1>
    </main>
  )
}
```

## Version History

| Version    | Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `v16.0.0`  | `qualities` default configuration changed to `[75]`, `preload` prop added, `priority` prop deprecated, `dangerouslyAllowLocalIP` config added, `maximumRedirects` config added.                                                                                                                                                                                                                                                                                                            |
| `v15.3.0`  | `remotePatterns` added support for array of `URL` objects.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `v15.0.0`  | `contentDispositionType` configuration default changed to `attachment`.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `v14.2.23` | `qualities` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `v14.2.15` | `decoding` prop added and `localPatterns` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `v14.2.14` | `remotePatterns.search` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `v14.2.0`  | `overrideSrc` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `v14.1.0`  | `getImageProps()` is stable.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `v14.0.0`  | `onLoadingComplete` prop and `domains` config deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `v13.4.14` | `placeholder` prop support for `data:/image...`                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `v13.2.0`  | `contentDispositionType` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `v13.0.6`  | `ref` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `v13.0.0`  | The `next/image` import was renamed to `next/legacy/image`. The `next/future/image` import was renamed to `next/image`. A [codemod is available](/docs/app/guides/upgrading/codemods.md#next-image-to-legacy-image) to safely and automatically rename your imports. `<span>` wrapper removed. `layout`, `objectFit`, `objectPosition`, `lazyBoundary`, `lazyRoot` props removed. `alt` is required. `onLoadingComplete` receives reference to `img` element. Built-in loader config removed. |
| `v12.3.0`  | `remotePatterns` and `unoptimized` configuration is stable.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `v12.2.0`  | Experimental `remotePatterns` and experimental `unoptimized` configuration added. `layout="raw"` removed.                                                                                                                                                                                                                                                                                                                                                                                  |
| `v12.1.1`  | `style` prop added. Experimental support for `layout="raw"` added.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `v12.1.0`  | `dangerouslyAllowSVG` and `contentSecurityPolicy` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `v12.0.9`  | `lazyRoot` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `v12.0.0`  | `formats` configuration added.AVIF support added.Wrapper `<div>` changed to `<span>`.                                                                                                                                                                                                                                                                                                                                                                                            |
| `v11.1.0`  | `onLoadingComplete` and `lazyBoundary` props added.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `v11.0.0`  | `src` prop support for static import.`placeholder` prop added.`blurDataURL` prop added.                                                                                                                                                                                                                                                                                                                                                                                          |
| `v10.0.5`  | `loader` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `v10.0.1`  | `layout` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `v10.0.0`  | `next/image` introduced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |


--------------------------------------------------------------------------------
title: "Link Component"
description: "Enable fast client-side navigation with the built-in `next/link` component."
source: "https://nextjs.org/docs/app/api-reference/components/link"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./05-scripts.md) | [Index](./index.md) | [Next →](./07-link-component.md)
