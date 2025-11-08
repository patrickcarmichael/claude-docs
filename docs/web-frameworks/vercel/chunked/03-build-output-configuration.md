**Navigation:** [← Previous](./02-usage-billing.md) | [Index](./index.md) | [Next →](./04-vercel-remove.md)

---

# Build Output Configuration

Copy page

Ask AI about this page

Last updated August 15, 2025

`   .vercel/output/config.json   `

  

Schema (as TypeScript):

```
type Config = {
  version: 3;
  routes?: Route[];
  images?: ImagesConfig;
  wildcard?: WildcardConfig;
  overrides?: OverrideConfig;
  cache?: string[];
  crons?: CronsConfig;
};
```

Config Types:

*   [Route](#routes)
*   [ImagesConfig](#images)
*   [WildcardConfig](#wildcard)
*   [OverrideConfig](#overrides)
*   [CronsConfig](#crons)

  

The `config.json` file contains configuration information and metadata for a Deployment. The individual properties are described in greater detail in the sub-sections below.

At a minimum, a `config.json` file with a `"version"` property is _required_.

## [`config.json` supported properties](#config.json-supported-properties)

### [version](#version)

`   .vercel/output/config.json   `

  

The `version` property indicates which version of the Build Output API has been implemented. The version described in this document is version `3`.

#### [`version` example](#version-example)

```
"version": 3
```

### [routes](#routes)

`   .vercel/output/config.json   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/routes)[`   vercel/examples/build-output-api/routes   `](https://github.com/vercel/examples/tree/main/build-output-api/routes)

  

The `routes` property describes the routing rules that will be applied to the Deployment. It uses the same syntax as the [`routes` property of the `vercel.json` file](/docs/project-configuration#routes).

Routes may be used to point certain URL paths to others on your Deployment, attach response headers to paths, and various other routing-related use-cases.

```
type Route = Source | Handler;
```

#### [`Source` route](#source-route)

```
type Source = {
  src: string;
  dest?: string;
  headers?: Record<string, string>;
  methods?: string[];
  continue?: boolean;
  caseSensitive?: boolean;
  check?: boolean;
  status?: number;
  has?: HasField;
  missing?: HasField;
  locale?: Locale;
  middlewareRawSrc?: string[];
  middlewarePath?: string;
  mitigate?: Mitigate;
  transforms?: Transform[];
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| src | [String](/docs/rest-api/reference#types) | Yes | A PCRE-compatible regular expression that matches each incoming pathname (excluding querystring). |
| dest | [String](/docs/rest-api/reference#types) | No | A destination pathname or full URL, including querystring, with the ability to embed capture groups as $1, $2, or named capture value $name. |
| headers | [Map](/docs/rest-api/reference#types) | No | A set of headers to apply for responses. |
| methods | [String\[\]](/docs/rest-api/reference#types) | No | A set of HTTP method types. If no method is provided, requests with any HTTP method will be a candidate for the route. |
| continue | [Boolean](/docs/rest-api/reference#types) | No | A boolean to change matching behavior. If true, routing will continue even when the src is matched. |
| caseSensitive | [Boolean](/docs/rest-api/reference#types) | No | Specifies whether or not the route `src` should match with case sensitivity. |
| check | [Boolean](/docs/rest-api/reference#types) | No | If `true`, the route triggers `handle: 'filesystem'` and `handle: 'rewrite'` |
| status | [Number](/docs/rest-api/reference#types) | No | A status code to respond with. Can be used in tandem with Location: header to implement redirects. |
| has | HasField | No | Conditions of the HTTP request that must exist to apply the route. |
| missing | HasField | No | Conditions of the HTTP request that must NOT exist to match the route. |
| locale | Locale | No | Conditions of the Locale of the requester that will redirect the browser to different routes. |
| middlewareRawSrc | [String\[\]](/docs/rest-api/reference#types) | No | A list containing the original routes used to generate the `middlewarePath`. |
| middlewarePath | [String](/docs/rest-api/reference#types) | No | Path to an Edge Runtime function that should be invoked as middleware. |
| mitigate | Mitigate | No | A mitigation action to apply to the route. |
| transforms | Transform\[\] | No | A list of transforms to apply to the route. |

###### Source route: `MatchableValue`

```
type MatchableValue = {
  eq?: string | number;
  neq?: string;
  inc?: string[];
  ninc?: string[];
  pre?: string;
  suf?: string;
  re?: string;
  gt?: number;
  gte?: number;
  lt?: number;
  lte?: number;
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| eq | [String](/docs/rest-api/reference#types) | [Number](/docs/rest-api/reference#types) | No | Value must equal this exact value. |
| neq | [String](/docs/rest-api/reference#types) | No | Value must not equal this value. |
| inc | [String\[\]](/docs/rest-api/reference#types) | No | Value must be included in this array. |
| ninc | [String\[\]](/docs/rest-api/reference#types) | No | Value must not be included in this array. |
| pre | [String](/docs/rest-api/reference#types) | No | Value must start with this prefix. |
| suf | [String](/docs/rest-api/reference#types) | No | Value must end with this suffix. |
| re | [String](/docs/rest-api/reference#types) | No | Value must match this regular expression. |
| gt | [Number](/docs/rest-api/reference#types) | No | Value must be greater than this number. |
| gte | [Number](/docs/rest-api/reference#types) | No | Value must be greater than or equal to this number. |
| lt | [Number](/docs/rest-api/reference#types) | No | Value must be less than this number. |
| lte | [Number](/docs/rest-api/reference#types) | No | Value must be less than or equal to this number. |

###### Source route: `HasField`

```
type HasField = Array<
  | { type: 'host'; value: string | MatchableValue }
  | {
      type: 'header' | 'cookie' | 'query';
      key: string;
      value?: string | MatchableValue;
    }
>;
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| type | "host" | "header" | "cookie" | "query" | Yes | Determines the HasField type. |
| key | [String](/docs/rest-api/reference#types) | No\* | Required for header, cookie, and query types. The key to match against. |
| value | [String](/docs/rest-api/reference#types) | MatchableValue | No | The value to match against using string or MatchableValue conditions. |

###### Source route: `Locale`

```
type Locale = {
  redirect?: Record<string, string>;
  cookie?: string;
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| redirect | [Map](/docs/rest-api/reference#types) | Yes | An object of keys that represent locales to check for (`en`, `fr`, etc.) that map to routes to redirect to (`/`, `/fr`, etc.). |
| cookie | [String](/docs/rest-api/reference#types) | No | Cookie name that can override the Accept-Language header for determining the current locale. |

###### Source route: `Mitigate`

```
type Mitigate = {
  action: 'challenge' | 'deny';
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| action | "challenge" | "deny" | Yes | The action to take when the route is matched. |

###### Source route: `Transform`

```
type Transform = {
  type: 'request.headers' | 'request.query' | 'response.headers';
  op: 'append' | 'set' | 'delete';
  target: {
    key: string | Omit<MatchableValue, 're'>; // re is not supported for transforms
  };
  args?: string | string[];
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| type | "request.headers" | "response.headers" | "request.query" | Yes | The type of transform to apply. |
| op | "append" | "set" | "delete" | Yes | The operation to perform on the target. |
| target | `{ key: string | Omit<MatchableValue, 're'> }` | Yes | The target of the transform. Regular expression matching is not supported. |
| args | [String](/docs/rest-api/reference#types) | [String\[\]](/docs/rest-api/reference#types) | No | The arguments to pass to the transform. |

#### [Handler route](#handler-route)

The routing system has multiple phases. The `handle` value indicates the start of a phase. All following routes are only checked in that phase.

```
type HandleValue =
  | 'rewrite'
  | 'filesystem' // check matches after the filesystem misses
  | 'resource'
  | 'miss' // check matches after every filesystem miss
  | 'hit'
  | 'error'; //  check matches after error (500, 404, etc.)
 
type Handler = {
  handle: HandleValue;
  src?: string;
  dest?: string;
  status?: number;
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| handle | HandleValue | Yes | The phase of routing when all subsequent routes should apply. |
| src | [String](/docs/rest-api/reference#types) | No | A PCRE-compatible regular expression that matches each incoming pathname (excluding querystring). |
| dest | [String](/docs/rest-api/reference#types) | No | A destination pathname or full URL, including querystring, with the ability to embed capture groups as $1, $2. |
| status | [String](/docs/rest-api/reference#types) | No | A status code to respond with. Can be used in tandem with `Location:` header to implement redirects. |

#### [Routing rule example](#routing-rule-example)

The following example shows a routing rule that will cause the `/redirect` path to perform an HTTP redirect to an external URL:

```
"routes": [
    {
      "src": "/redirect",
      "status": 308,
      "headers": { "Location": "https://example.com/" }
    }
  ]
```

### [images](#images)

`   .vercel/output/config.json   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/image-optimization)[`   vercel/examples/build-output-api/image-optimization   `](https://github.com/vercel/examples/tree/main/build-output-api/image-optimization)

  

The `images` property defines the behavior of Vercel's native [Image Optimization API](/docs/image-optimization), which allows on-demand optimization of images at runtime.

```
type ImageFormat = 'image/avif' | 'image/webp';
 
type RemotePattern = {
  protocol?: 'http' | 'https';
  hostname: string;
  port?: string;
  pathname?: string;
  search?: string;
};
 
type LocalPattern = {
  pathname?: string;
  search?: string;
};
 
type ImagesConfig = {
  sizes: number[];
  domains: string[];
  remotePatterns?: RemotePattern[];
  localPatterns?: LocalPattern[];
  qualities?: number[];
  minimumCacheTTL?: number; // seconds
  formats?: ImageFormat[];
  dangerouslyAllowSVG?: boolean;
  contentSecurityPolicy?: string;
  contentDispositionType?: string;
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| sizes | [Number\[\]](/docs/rest-api/reference#types) | Yes | Allowed image widths. |
| domains | [String\[\]](/docs/rest-api/reference#types) | Yes | Allowed external domains that can use Image Optimization. Leave empty for only allowing the deployment domain to use Image Optimization. |
| remotePatterns | RemotePattern\[\] | No | Allowed external patterns that can use Image Optimization. Similar to `domains` but provides more control with RegExp. |
| localPatterns | LocalPattern\[\] | No | Allowed local patterns that can use Image Optimization. Leave undefined to allow all or use empty array to deny all. |
| qualities | [Number\[\]](/docs/rest-api/reference#types) | No | Allowed image qualities. Leave undefined to allow all possibilities, 1 to 100. |
| minimumCacheTTL | [Number](/docs/rest-api/reference#types) | No | Cache duration (in seconds) for the optimized images. |
| formats | ImageFormat\[\] | No | Supported output image formats |
| dangerouslyAllowSVG | [Boolean](/docs/rest-api/reference#types) | No | Allow SVG input image URLs. This is disabled by default for security purposes. |
| contentSecurityPolicy | [String](/docs/rest-api/reference#types) | No | Change the [Content Security Policy](https://developer.mozilla.org/docs/Web/HTTP/CSP) of the optimized images. |
| contentDispositionType | [String](/docs/rest-api/reference#types) | No | Specifies the value of the `"Content-Disposition"` response header. |

#### [`images` example](#images-example)

The following example shows an image optimization configuration that specifies allowed image size dimensions, external domains, caching lifetime and file formats:

```
"images": {
    "sizes": [640, 750, 828, 1080, 1200],
    "domains": [],
    "minimumCacheTTL": 60,
    "formats": ["image/avif", "image/webp"],
    "qualities": [25, 50, 75],
    "localPatterns": [{
      "pathname": "^/assets/.*$",
      "search": ""
    }]
    "remotePatterns": [{
      "protocol": "https",
      "hostname": "^via\\.placeholder\\.com$",
      "port": "",
      "pathname": "^/1280x640/.*$",
      "search": "?v=1"
    }]
  }
```

#### [API](#api)

When the `images` property is defined, the Image Optimization API will be available by visiting the `/_vercel/image` path. When the `images` property is undefined, visiting the `/_vercel/image` path will respond with 404 Not Found.

The API accepts the following query string parameters:

| Key | [Type](/docs/rest-api/reference#types) | Required | Example | Description |
| --- | --- | --- | --- | --- |
| url | [String](/docs/rest-api/reference#types) | Yes | `/assets/me.png` | The URL of the source image that should be optimized. Absolute URLs must match a pattern defined in the `remotePatterns` configuration. |
| w | [Integer](/docs/rest-api/reference#types) | Yes | `200` | The width (in pixels) that the source image should be resized to. Must match a value defined in the `sizes` configuration. |
| q | [Integer](/docs/rest-api/reference#types) | Yes | `75` | The quality that the source image should be reduced to. Must be between 1 (lowest quality) to 100 (highest quality). |

### [wildcard](#wildcard)

`   .vercel/output/config.json   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/wildcard)[`   vercel/examples/build-output-api/wildcard   `](https://github.com/vercel/examples/tree/main/build-output-api/wildcard)

  

The `wildcard` property relates to Vercel's Internationalization feature. The way it works is the domain names listed in this array are mapped to the `$wildcard` routing variable, which can be referenced by the [`routes` configuration](#routes).

Each of the domain names specified in the `wildcard` configuration will need to be assigned as [Production Domains in the Project Settings](/docs/domains).

```
type WildCard = {
  domain: string;
  value: string;
};
 
type WildcardConfig = Array<WildCard>;
```

#### [`wildcard` supported properties](#wildcard-supported-properties)

Objects contained within the `wildcard` configuration support the following properties:

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| domain | [String](/docs/rest-api/reference#types) | Yes | The domain name to match for this wildcard configuration. |
| value | [String](/docs/rest-api/reference#types) | Yes | The value of the `$wildcard` match that will be available for `routes` to utilize. |

#### [`wildcard` example](#wildcard-example)

The following example shows a wildcard configuration where the matching domain name will be served the localized version of the blog post HTML file:

```
"wildcard": [
    {
      "domain": "example.com",
      "value": "en-US"
    },
    {
      "domain": "example.nl",
      "value": "nl-NL"
    },
    {
      "domain": "example.fr",
      "value": "fr"
    }
  ],
  "routes": [
    { "src": "/blog", "dest": "/blog.$wildcard.html" }
  ]
```

### [overrides](#overrides)

`   .vercel/output/config.json   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/overrides)[`   vercel/examples/build-output-api/overrides   `](https://github.com/vercel/examples/tree/main/build-output-api/overrides)

  

The `overrides` property allows for overriding the output of one or more [static files](/docs/build-output-api/v3/primitives#static-files) contained within the `.vercel/output/static` directory.

The main use-cases are to override the `Content-Type` header that will be served for a static file, and/or to serve a static file in the Vercel Deployment from a different URL path than how it is stored on the file system.

```
type Override = {
  path?: string;
  contentType?: string;
};
 
type OverrideConfig = Record<string, Override>;
```

#### [`overrides` supported properties](#overrides-supported-properties)

Objects contained within the `overrides` configuration support the following properties:

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| path | [String](/docs/rest-api/reference#types) | No | The URL path where the static file will be accessible from. |
| contentType | [String](/docs/rest-api/reference#types) | No | The value of the `Content-Type` HTTP response header that will be served with the static file. |

#### [`overrides` example](#overrides-example)

The following example shows an override configuration where an HTML file can be accessed without the `.html` file extension:

```
"overrides": {
    "blog.html": {
      "path": "blog"
    }
  }
```

### [cache](#cache)

`   .vercel/output/config.json   `

  

The `cache` property is an array of file paths and/or glob patterns that should be re-populated within the build sandbox upon subsequent Deployments.

Note that this property is only relevant when Vercel is building a Project from source code, meaning it is not relevant when building locally or when creating a Deployment from "prebuilt" build artifacts.

```
type Cache = string[];
```

#### [`cache` example](#cache-example)

```
"cache": [
    ".cache/**",
    "node_modules/**"
  ]
```

### [framework](#framework)

`   .vercel/output/config.json   `

  

The optional `framework` property is an object describing the framework of the built outputs.

This value is used for display purposes only.

```
type Framework = {
  version: string;
};
```

#### [`framework` example](#framework-example)

```
"framework": {
    "version": "1.2.3"
  }
```

### [crons](#crons)

`   .vercel/output/config.json   `

  

The optional `crons` property is an object describing the [cron jobs](/docs/cron-jobs) for the production deployment of a project.

```
type Cron = {
  path: string;
  schedule: string;
};
 
type CronsConfig = Cron[];
```

#### [`crons` example](#crons-example)

```
"crons": [{
    "path": "/api/cron",
    "schedule": "0 0 * * *"
  }]
```

## [Full `config.json` example](#full-config.json-example)

```
{
  "version": 3,
  "routes": [
    {
      "src": "/redirect",
      "status": 308,
      "headers": { "Location": "https://example.com/" }
    },
    {
      "src": "/blog",
      "dest": "/blog.$wildcard.html"
    }
  ],
  "images": {
    "sizes": [640, 750, 828, 1080, 1200],
    "domains": [],
    "minimumCacheTTL": 60,
    "formats": ["image/avif", "image/webp"],
    "qualities": [25, 50, 75],
    "localPatterns": [{
      "pathname": "^/assets/.*$",
      "search": ""
    }]
    "remotePatterns": [
      {
        "protocol": "https",
        "hostname": "^via\\.placeholder\\.com$",
        "port": "",
        "pathname": "^/1280x640/.*$",
        "search": "?v=1"
      }
    ]
  },
  "wildcard": [
    {
      "domain": "example.com",
      "value": "en-US"
    },
    {
      "domain": "example.nl",
      "value": "nl-NL"
    },
    {
      "domain": "example.fr",
      "value": "fr"
    }
  ],
  "overrides": {
    "blog.html": {
      "path": "blog"
    }
  },
  "cache": [".cache/**", "node_modules/**"],
  "framework": {
    "version": "1.2.3"
  },
  "crons": [
    {
      "path": "/api/cron",
      "schedule": "* * * * *"
    }
  ]
}
```

--------------------------------------------------------------------------------
title: "Features"
description: "Learn how to implement common Vercel platform features through the Build Output API."
last_updated: "null"
source: "https://vercel.com/docs/build-output-api/features"
--------------------------------------------------------------------------------

# Features

Copy page

Ask AI about this page

Last updated March 4, 2025

This section describes how to implement common Vercel platform features through the Build Output API through a combination of platform primitives, configuration and helper functions.

## [High-level routing](#high-level-routing)

The `vercel.json` file supports an [easier-to-use syntax for routing through properties like `rewrites`, `headers`, etc](/docs/project-configuration). However, the [`config.json` "routes" property](/docs/build-output-api/v3/configuration#routes) supports a lower-level syntax.

The `getTransformedRoutes()` function from the [`@vercel/routing-utils` npm package](https://www.npmjs.com/package/@vercel/routing-utils) can be used to convert this higher-level syntax into the lower-level format that is supported by the Build Output API. For example:

```
import { writeFileSync } from 'fs';
import { getTransformedRoutes } from '@vercel/routing-utils';
 
const { routes } = getTransformedRoutes({
  trailingSlash: false,
  redirects: [
    { source: '/me', destination: '/profile.html' },
    { source: '/view-source', destination: 'https://github.com/vercel/vercel' },
  ],
});
 
const config = {
  version: 3,
  routes,
};
writeFileSync('.vercel/output/config.json', JSON.stringify(config));
```

#### [`cleanUrls`](#cleanurls)

The [`cleanUrls: true` routing feature](/docs/project-configuration#cleanurls) is a special case because, in addition to the routes generated with the helper function above, it _also_ requires that the static HTML files have their `.html` suffix removed.

This can be achieved by utilizing the [`"overrides"` property in the `config.json` file](/docs/build-output-api/v3/configuration#overrides):

```
import { writeFileSync } from 'fs';
import { getTransformedRoutes } from '@vercel/routing-utils';
 
const { routes } = getTransformedRoutes({
  cleanUrls: true,
});
 
const config = {
  version: 3,
  routes,
  overrides: {
    'blog.html': {
      path: 'blog',
    },
  },
};
writeFileSync('.vercel/output/config.json', JSON.stringify(config));
```

## [Edge Middleware](#edge-middleware)

[](https://github.com/vercel/examples/tree/main/build-output-api/edge-middleware)[`   vercel/examples/build-output-api/edge-middleware   `](https://github.com/vercel/examples/tree/main/build-output-api/edge-middleware)

  

An Edge Runtime function can act as a "middleware" in the HTTP request lifecycle for a Deployment. Middleware is useful for implementing functionality that may be shared by many URL paths in a Project (e.g. authentication), before passing the request through to the underlying resource (such as a page or asset) at that path.

An Edge Middleware is represented on the file system in the same format as an [Edge Function](/docs/build-output-api/v3#vercel-primitives/edge-functions). To use the middleware, add additional rules in the [`routes` configuration](/docs/build-output-api/v3/configuration#routes) mapping URLs (using the `src` property) to the middleware (using the `middlewarePath` property).

### [Edge Middleware example](#edge-middleware-example)

The following example adds a rule that calls the `auth` middleware for any URL that starts with `/api`, before continuing to the underlying resource:

```
"routes": [
    {
      "src": "/api/(.*)",
      "middlewareRawSrc": ["/api"],
      "middlewarePath": "auth",
      "continue": true
    }
  ]
```

## [Draft Mode](#draft-mode)

[](https://github.com/vercel/examples/tree/main/build-output-api/draft-mode)[`   vercel/examples/build-output-api/preview-mode   `](https://github.com/vercel/examples/tree/main/build-output-api/draft-mode)

  

When using [Prerender Functions](/docs/build-output-api/v3/primitives#prerender-functions), you may want to implement "Draft Mode" which would allow you to bypass the caching aspect of prerender functions. For example, while writing draft blog posts before they are ready to be published.

To implement this, the `bypassToken` of the `<name>.prerender-config.json` file should be set to a randomized string that you generate at build-time. This string should not be exposed to users / the client-side, except under authenticated circumstances.

To enable "Draft Mode", a cookie with the name `__prerender_bypass` needs to be set (i.e. by a Vercel Function) with the value of the `bypassToken`. When the Prerender Function endpoint is accessed while the cookie is set, then "Draft Mode" will be activated, bypassing any caching that Vercel would normally provide when not in draft mode.

## [On-Demand Incremental Static Regeneration (ISR)](#on-demand-incremental-static-regeneration-isr)

[](https://github.com/vercel/examples/tree/main/build-output-api/on-demand-isr)[`   vercel/examples/build-output-api/on-demand-isr   `](https://github.com/vercel/examples/tree/main/build-output-api/on-demand-isr)

  

When using [Prerender Functions](/docs/build-output-api/v3/primitives#prerender-functions), you may want to implement "On-Demand Incremental Static Regeneration (ISR)" which would allow you to invalidate the cache at any time.

To implement this, the `bypassToken` of the `<name>.prerender-config.json` file should be set to a randomized string that you generate at build-time. This string should not be exposed to users / the client-side, except under authenticated circumstances.

To trigger "On-Demand Incremental Static Regeneration (ISR)" and revalidate a path to a Prerender Function, make a `GET` or `HEAD` request to that path with a header of `x-prerender-revalidate: <bypassToken>`. When that Prerender Function endpoint is accessed with this header set, the cache will be revalidated. The next request to that function should return a fresh response.

--------------------------------------------------------------------------------
title: "Vercel Primitives"
description: "Learn about the Vercel platform primitives and how they work together to create a Vercel Deployment."
last_updated: "null"
source: "https://vercel.com/docs/build-output-api/primitives"
--------------------------------------------------------------------------------

# Vercel Primitives

Copy page

Ask AI about this page

Last updated March 4, 2025

The following directories, code files, and configuration files represent all Vercel platform primitives. These primitives are the "building blocks" that make up a Vercel Deployment.

Files outside of these directories are ignored and will not be served to visitors.

## [Static files](#static-files)

`   .vercel/output/static   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/static-files)[`   vercel/examples/build-output-api/static-files   `](https://github.com/vercel/examples/tree/main/build-output-api/static-files)

  

Static files that are _publicly accessible_ from the Deployment URL should be placed in the `.vercel/output/static` directory.

These files are served with the [Vercel Edge CDN](/docs/cdn).

Files placed within this directory will be made available at the root (`/`) of the Deployment URL and neither their contents, nor their file name or extension will be modified in any way. Sub directories within `static` are also retained in the URL, and are appended before the file name.

### [Configuration](#configuration)

There is no standalone configuration file that relates to static files.

However, certain properties of static files (such as the `Content-Type` response header) can be modified by utilizing the [`overrides` property of the `config.json` file](/docs/build-output-api/v3/configuration#overrides).

### [Directory structure for static files](#directory-structure-for-static-files)

The following example shows static files placed into the `.vercel/output/static` directory:

  
  

*   .vercel
    *   output
        *   static
            *   images
                *   avatar.png
            *   favicon.png
            *   client-side-bundle.js
            *   robots.txt

## [Serverless Functions](#serverless-functions)

`   .vercel/output/functions   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/serverless-functions)[`   vercel/examples/build-output-api/serverless-functions   `](https://github.com/vercel/examples/tree/main/build-output-api/serverless-functions)

  

A [Vercel Function](/docs/functions) is represented on the file system as a directory with a `.func` suffix on the name, contained within the `.vercel/output/functions` directory.

Conceptually, you can think of this `.func` directory as a filesystem mount for a Vercel Function: the files below the `.func` directory are included (recursively) and files above the `.func` directory are not included. Private files may safely be placed within this directory because they will not be directly accessible to end-users. However, they can be referenced by code that will be executed by the Vercel Function.

A `.func` directory may be a symlink to another `.func` directory in cases where you want to have more than one path point to the same underlying Vercel Function.

A configuration file named `.vc-config.json` must be included within the `.func` directory, which contains information about how Vercel should construct the Vercel Function.

The `.func` suffix on the directory name is _not included_ as part of the URL path of Vercel Function on the Deployment. For example, a directory located at `.vercel/output/functions/api/posts.func` will be accessible at the URL path `/api/posts` of the Deployment.

### [Serverless function configuration](#serverless-function-configuration)

`   .vercel/output/functions/<name>.func/.vc-config.json   `

  

The `.vc-config.json` configuration file contains information related to how the Vercel Function will be created by Vercel.

#### [Base config](#base-config)

```
type ServerlessFunctionConfig = {
  handler: string;
  runtime: string;
  memory?: number;
  maxDuration?: number;
  environment: Record<string, string>[];
  regions?: string[];
  supportsWrapper?: boolean;
  supportsResponseStreaming?: boolean;
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| runtime | [String](/docs/rest-api/reference#types) | Yes | Specifies which "runtime" will be used to execute the Vercel Function. See [Runtimes](/docs/functions/runtimes) for more information. |
| handler | [String](/docs/rest-api/reference#types) | Yes | Indicates the initial file where code will be executed for the Vercel Function. |
| memory | [Integer](/docs/rest-api/reference#types) | No | Amount of memory (RAM in MB) that will be allocated to the Vercel Function. See [size limits](/docs/functions/runtimes#size-limits) for more information. |
| architecture | [String](/docs/rest-api/reference#types) | No | Specifies the instruction set "architecture" the Vercel Function supports. Either `x86_64` or `arm64`. The default value is `x86_64`. |
| maxDuration | [Integer](/docs/rest-api/reference#types) | No | Maximum duration (in seconds) that will be allowed for the Vercel Function. See [size limits](/docs/functions/runtimes#size-limits) for more information. |
| environment | [Map](/docs/rest-api/reference#types) | No | Map of additional environment variables that will be available to the Vercel Function, in addition to the env vars specified in the Project Settings. |
| regions | [String\[\]](/docs/rest-api/reference#types) | No | List of Vercel Regions where the Vercel Function will be deployed to. |
| supportsWrapper | [Boolean](/docs/rest-api/reference#types) | No | True if a custom runtime has support for Lambda runtime wrappers. |
| supportsResponseStreaming | [Boolean](/docs/rest-api/reference#types) | No | When true, the Vercel Function will stream the response to the client. |

#### [Node.js config](#node.js-config)

This extends the [Base Config](#base-config) for Node.js Serverless Functions.

```
type NodejsServerlessFunctionConfig = ServerlessFunctionConfig & {
  launcherType: 'Nodejs';
  shouldAddHelpers?: boolean; // default: false
  shouldAddSourcemapSupport?: boolean; // default: false
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| launcherType | "Nodejs" | Yes | Specifies which launcher to use. Currently only "Nodejs" is supported. |
| shouldAddHelpers | [Boolean](/docs/rest-api/reference#types) | No | Enables request and response helpers methods. |
| shouldAddSourcemapSupport | [Boolean](/docs/rest-api/reference#types) | No | Enables source map generation. |
| awsLambdaHandler | [String](/docs/rest-api/reference#types) | No | [AWS Handler Value](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-handler.html) for when the serverless function uses AWS Lambda syntax. |

#### [Node.js config example](#node.js-config-example)

This is what the `.vc-config.json` configuration file could look like in a real scenario:

```
{
  "runtime": "nodejs22.x",
  "handler": "serve.js",
  "maxDuration": 3,
  "launcherType": "Nodejs",
  "shouldAddHelpers": true,
  "shouldAddSourcemapSupport": true
}
```

### [Directory structure for Serverless Functions](#directory-structure-for-serverless-functions)

The following example shows a directory structure where the Vercel Function will be accessible at the `/serverless` URL path of the Deployment:

*   .vercel
    *   output
        *   functions
            *   serverless.func
                *   node\_modules
                    *   ...
                *   .vc-config.json
                *   serve.js
                *   data.sqlite

  
  

## [Edge Functions](#edge-functions)

`   .vercel/output/functions   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/edge-functions)[`   vercel/examples/build-output-api/edge-functions   `](https://github.com/vercel/examples/tree/main/build-output-api/edge-functions)

  

An [Edge Function](/docs/functions/edge-functions) is represented on the file system as a directory with a `.func` suffix on the name, contained within the `.vercel/output/functions` directory.

The `.func` directory requires at least one JavaScript or TypeScript source file which will serve as the `entrypoint` of the function. Additional source files may also be included in the `.func` directory. All imported source files will be _bundled_ at build time.

WebAssembly (Wasm) files may also be placed in this directory for an Edge Function to import. See [Using a WebAssembly file](/docs/functions/runtimes/wasm) for more information.

A configuration file named `.vc-config.json` must be included within the `.func` directory, which contains information about how Vercel should configure the Edge Function.

The `.func` suffix is _not included_ in the URL path. For example, a directory located at `.vercel/output/functions/api/edge.func` will be accessible at the URL path `/api/edge` of the Deployment.

### [Supported content types](#supported-content-types)

Edge Functions will bundle an `entrypoint` and all supported source files that are imported by that `entrypoint`. The following list includes all supported content types by their common file extensions.

*   `.js`
*   `.json`
*   `.wasm`

### [Edge Function configuration](#edge-function-configuration)

`   .vercel/output/functions/<name>.func/.vc-config.json   `

  

The `.vc-config.json` configuration file contains information related to how the Edge Function will be created by Vercel.

```
type EdgeFunctionConfig = {
  runtime: 'edge';
  entrypoint: string;
  envVarsInUse?: string[];
  regions?: 'all' | string | string[];
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| runtime | ["edge"](/docs/rest-api/reference#types) | Yes | The `runtime: "edge"` property is required to indicate that this directory represents an Edge Function. |
| entrypoint | [String](/docs/rest-api/reference#types) | Yes | Indicates the initial file where code will be executed for the Edge Function. |
| envVarsInUse | [String\[\]](/docs/rest-api/reference#types) | No | List of environment variable names that will be available for the Edge Function to utilize. |
| regions | [String\[\]](/docs/rest-api/reference#types) | No | List of regions or a specific region that the edge function will be available in, defaults to `all`. [View available regions](/docs/regions#region-list). |

#### [Edge Function config example](#edge-function-config-example)

This is what the `.vc-config.json` configuration file could look like in a real scenario:

```
{
  "runtime": "edge",
  "entrypoint": "index.js",
  "envVarsInUse": ["DATABASE_API_KEY"]
}
```

### [Directory structure for Edge Functions](#directory-structure-for-edge-functions)

The following example shows a directory structure where the Edge Function will be accessible at the `/edge` URL path of the Deployment:

*   .vercel
    *   output
        *   functions
            *   edge.func
                *   .vc-config.json
                *   index.js

## [Prerender Functions](#prerender-functions)

`   .vercel/output/functions   `

  

[](https://github.com/vercel/examples/tree/main/build-output-api/prerender-functions)[`   vercel/examples/build-output-api/prerender-functions   `](https://github.com/vercel/examples/tree/main/build-output-api/prerender-functions)

  

A Prerender asset is a Vercel Function that will be cached by the Vercel CDN in the same way as a static file. This concept is also known as [Incremental Static Regeneration](/docs/incremental-static-regeneration).

On the file system, a Prerender is represented in the same way as a Vercel Function, with an additional configuration file that describes the cache invalidation rules for the Prerender asset.

An optional "fallback" static file can also be specified, which will be served when there is no cached version available.

### [Prerender configuration file](#prerender-configuration-file)

`   .vercel/output/functions/<name>.prerender-config.json   `

  

The `<name>.prerender-config.json` configuration file contains information related to how the Edge Function will be created by Vercel.

```
type PrerenderFunctionConfig = {
  expiration: number | false;
  group?: number;
  bypassToken?: string;
  fallback?: string;
  allowQuery?: string[];
  passQuery?: boolean;
};
```

| Key | [Type](/docs/rest-api/reference#types) | Required | Description |
| --- | --- | --- | --- |
| expiration | [Integer | false](/docs/rest-api/reference#types) | Yes | Expiration time (in seconds) before the cached asset will be re-generated by invoking the Vercel Function. Setting the value to `false` means it will never expire. |
| group | [Integer](/docs/rest-api/reference#types) | No | Option group number of the asset. Prerender assets with the same group number will all be re-validated at the same time. |
| bypassToken | [String](/docs/draft-mode) | No | Random token assigned to the `__prerender_bypass` cookie when [Draft Mode](/docs/draft-mode) is enabled, in order to safely bypass the CDN cache |
| fallback | [String](/docs/rest-api/reference#types) | No | Name of the optional fallback file relative to the configuration file. |
| allowQuery | [String\[\] | undefined](/docs/rest-api/reference#types) | No | List of query string parameter names that will be cached independently. If an empty array, query values are not considered for caching. If undefined each unique query value is cached independently |
| passQuery | [Boolean | undefined](/docs/rest-api/reference#types) | No | When true, the query string will be present on the `request` argument passed to the invoked function. The `allowQuery` filter still applies. |

#### [Fallback static file](#fallback-static-file)

`   .vercel/output/functions/<name>.prerender-fallback.<ext>   `

  

A Prerender asset may also include a static "fallback" version that is generated at build-time. The fallback file will be served by Vercel while there is not yet a cached version that was generated during runtime.

When the fallback file is served, the Vercel Function will also be invoked "out-of-band" to re-generate a new version of the asset that will be cached and served for future HTTP requests.

#### [Prerender config example](#prerender-config-example)

This is what an `example.prerender-config.json` file could look like in a real scenario:

```
{
  "expiration": 60,
  "group": 1,
  "bypassToken": "03326da8bea31b919fa3a31c85747ddc",
  "fallback": "example.prerender-fallback.html",
  "allowQuery": ["id"]
}
```

### [Directory structure for Prerender Functions](#directory-structure-for-prerender-functions)

The following example shows a directory structure where the Prerender will be accessible at the `/blog` URL path of the Deployment:

*   .vercel
    *   output
        *   functions
            *   blog.func
                *   .vc-config.json
                *   index.js
            *   blog.prerender-config.json
            *   blog.prerender-fallback.html

--------------------------------------------------------------------------------
title: "Builds"
description: "Understand how the build step works when creating a Vercel Deployment."
last_updated: "null"
source: "https://vercel.com/docs/builds"
--------------------------------------------------------------------------------

# Builds

Copy page

Ask AI about this page

Last updated September 9, 2025

Vercel automatically performs a build every time you deploy your code, whether you're pushing to a Git repository, importing a project via the dashboard, or using the [Vercel CLI](/docs/cli). This process compiles, bundles, and optimizes your application so it's ready to serve to your users.

## [Build infrastructure](#build-infrastructure)

When you initiate a build, Vercel creates a secure, isolated virtual environment for your project:

*   Your code is built in a clean, consistent environment
*   Build processes can't interfere with other users' applications
*   Security is maintained through complete isolation
*   Resources are efficiently allocated and cleaned up after use

This infrastructure handles millions of builds daily, supporting everything from individual developers to large enterprises, while maintaining strict security and performance standards.

Most frontend frameworks—like Next.js, SvelteKit, and Nuxt—are auto-detected, with defaults applied for Build Command, Output Directory, and other settings. To see if your framework is included, visit the [Supported Frameworks](/docs/frameworks) page.

## [How builds are triggered](#how-builds-are-triggered)

Builds can be initiated in the following ways:

1.  Push to Git: When you connect a GitHub, GitLab, or Bitbucket repository, each commit to a tracked branch initiates a new build and deployment. By default, Vercel performs a _shallow clone_ of your repo (`git clone --depth=10`) to speed up build times.
    
2.  Vercel CLI: Running `vercel` locally deploys your project. By default, this creates a preview build unless you add the `--prod` flag (for production).
    
3.  Dashboard deploy: Clicking Deploy in the dashboard or creating a new project also triggers a build.
    

## [Build customization](#build-customization)

Depending on your framework, Vercel automatically sets the Build Command, Install Command, and Output Directory. If needed, you can customize these in your project's Settings:

1.  Build Command: Override the default (`npm run build`, `next build`, etc.) for custom workflows.
    
2.  Output Directory: Specify the folder containing your final build output (e.g., `dist` or `build`).
    
3.  Install Command: Control how dependencies are installed (e.g., `pnpm install`, `yarn install`) or skip installing dev dependencies if needed.
    

To learn more, see [Configuring a Build](/docs/deployments/configure-a-build).

## [Skipping the build step](#skipping-the-build-step)

For static websites—HTML, CSS, and client-side JavaScript only—no build step is required. In those cases:

1.  Set Framework Preset to Other.
2.  Leave the build command blank.
3.  (Optionally) override the Output Directory if you want to serve a folder other than `public` or `.`.

## [Monorepos](#monorepos)

When working in a monorepo, you can connect multiple Vercel projects within the same repository. By default, each project will build and deploy whenever you push a commit. Vercel can optimize this by:

1.  Skipping unaffected projects: Vercel automatically detects whether a project's files (or its dependencies) have changed and skips deploying projects that are unaffected. This feature reduces unnecessary builds and doesn't occupy concurrent build slots. Learn more about [skipping unaffected projects](/docs/monorepos#skipping-unaffected-projects).
    
2.  Ignored build step: You can also write a script that cancels the build for a project if no relevant changes are detected. This approach still counts toward your concurrent build limits, but may be useful in certain scenarios. See the [Ignored Build Step](/docs/project-configuration/git-settings#ignored-build-step) documentation for details.
    

For monorepo-specific build tools, see:

*   [Turborepo](/docs/monorepos/turborepo)
*   [Nx](/docs/monorepos/nx)

## [Concurrency and queues](#concurrency-and-queues)

When multiple builds are requested, Vercel manages concurrency and queues for you:

1.  Concurrency Slots: Each plan has a limit on how many builds can run at once. If all slots are busy, new builds wait until a slot is free.
    
2.  Branch-Based Queue: If new commits land on the same branch, Vercel skips older queued builds and prioritizes only the most recent commit. This ensures that the latest changes are always deployed first.
    
3.  On-Demand Concurrency: If you need more concurrent build slots or want certain production builds to jump the queue, consider enabling [On-Demand Concurrent Builds](/docs/deployments/managing-builds#on-demand-concurrent-builds).
    

## [Environment variables](#environment-variables)

Vercel can automatically inject environment variables such as API keys, database connections, or feature flags during the build:

1.  Project-Level Variables: Define variables under Settings for each environment (Preview, Production, or any custom environment).
    
2.  Pull Locally: Use `vercel env pull` to download environment variables for local development. This command populates your `.env.local` file.
    
3.  Security: Environment variables remain private within the build environment and are never exposed in logs.
    

## [Ignored files and folders](#ignored-files-and-folders)

Some files (e.g., large datasets or personal configuration) might not be needed in your deployment:

*   Vercel automatically ignores certain files (like `.git`) for performance and security.
*   You can read more about how to specify [ignored files and folders](/docs/builds/build-features#ignored-files-and-folders).

## [Build output and deployment](#build-output-and-deployment)

Once the build completes successfully:

1.  Vercel uploads your build artifacts (static files, Vercel Functions, and other assets) to the CDN.
2.  A unique deployment URL is generated for Preview or updated for Production domains.
3.  Logs and build details are available in the Deployments section of the dashboard.

If the build fails or times out, Vercel provides diagnostic logs in the dashboard to help you troubleshoot. For common solutions, see our [build troubleshooting](/docs/deployments/troubleshoot-a-build) docs.

## [Build infrastructure](#build-infrastructure)

Behind the scenes, Vercel manages a sophisticated global infrastructure that:

*   Creates isolated build environments on-demand
*   Handles automatic regional failover
*   Manages hardware resources efficiently
*   Pre-warms containers to improve build start times
*   Synchronizes OS and runtime environments with your deployment targets

## [Limits and resources](#limits-and-resources)

Vercel enforces certain limits to ensure reliable builds for all users:

*   Build timeout: The maximum build time is 45 minutes. If your build exceeds this limit, it will be terminated, and the deployment fails.
    
*   Build cache: Each build cache can be up to 1 GB. The [cache](/docs/deployments/troubleshoot-a-build#caching-process) is retained for one month. Restoring a build cache can speed up subsequent deployments.
    
*   Container resources: Vercel creates a [build container](/docs/builds/build-image) with different resources depending on your plan:
    
    |  | Hobby | Pro | Enterprise |
    | --- | --- | --- | --- |
    | Memory | 8192 MB | 8192 MB | Custom |
    | Disk Space | 23 GB | 23 GB | Custom |
    | CPUs | 2 | 4 | Custom |
    

For more information, visit [Build Container Resources](/docs/deployments/troubleshoot-a-build#build-container-resources) and [Cancelled Builds](/docs/deployments/troubleshoot-a-build#cancelled-builds-due-to-limits).

## [Learn more about builds](#learn-more-about-builds)

To explore more features and best practices for building and deploying with Vercel:

*   [Configure your build](/docs/builds/configure-a-build): Customize commands, output directories, environment variables, and more.
*   [Troubleshoot builds](/docs/deployments/troubleshoot-a-build): Get help with build cache, resource limits, and common errors.
*   [Manage builds](/docs/builds/managing-builds): Control how many builds run in parallel and prioritize critical deployments.
*   [Working with Monorepos](/docs/monorepos): Set up multiple projects in a single repository and streamline deployments.

## [Pricing](#pricing)

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Build Time](/docs/builds/managing-builds#managing-build-time) | The amount of time your Deployments have spent being queued or building | No | [Learn More](/docs/builds/managing-builds#managing-build-time) |
| [Number of Builds](/docs/builds/managing-builds#number-of-builds) | How many times a build was issued for one of your Deployments | No | N/A |

--------------------------------------------------------------------------------
title: "Build Features for Customizing Deployments"
description: "Learn how to customize your deployments using Vercel's build features."
last_updated: "null"
source: "https://vercel.com/docs/builds/build-features"
--------------------------------------------------------------------------------

# Build Features for Customizing Deployments

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel provides the following features to customize your deployments:

*   [Private npm packages](#private-npm-packages)
*   [Ignored files and folders](#ignored-files-and-folders)
*   [Special paths](#special-paths)
*   [Git submodules](#git-submodules)

## [Private npm packages](#private-npm-packages)

When your project's code is using private `npm` modules that require authentication, you need to perform an additional step to install private modules.

To install private `npm` modules, define `NPM_TOKEN` as an [Environment Variable](/docs/environment-variables) in your project. Alternatively, define `NPM_RC` as an [Environment Variable](/docs/environment-variables) in the contents of the project's npmrc config file that resides at the root of the project folder and is named `~/.npmrc`. This file defines the config settings of `npm` at the level of the project.

To learn more, check out the [guide here](/guides/using-private-dependencies-with-vercel) if you need help configuring private dependencies.

## [Ignored files and folders](#ignored-files-and-folders)

Vercel ignores certain files and folders by default and prevents them from being uploaded during the deployment process for security and performance reasons. Please note that these ignored files are only relevant when using Vercel CLI.

ignored-files

```
.hg
.git
.gitmodules
.svn
.cache
.next
.now
.vercel
.npmignore
.dockerignore
.gitignore
.*.swp
.DS_Store
.wafpicke-*
.lock-wscript
.env.local
.env.*.local
.venv
.yarn/cache
npm-debug.log
config.gypi
node_modules
__pycache__
venv
CVS
```

A complete list of files and folders ignored by Vercel during the Deployment process.

The `.vercel/output` directory is not ignored when [`vercel deploy --prebuilt`](/docs/cli/deploying-from-cli#deploying-from-local-build-prebuilt) is used to deploy a prebuilt Vercel Project, according to the [Build Output API](/docs/build-output-api/v3) specification.

You do not need to add any of the above files and folders to your `.vercelignore` file because it is done automatically by Vercel.

## [Special paths](#special-paths)

Vercel allows you to access the source code and build logs for your deployment using special pathnames for Build Logs and Source Protection. You can access this option from your project's Security settings.

All deployment URLs have two special pathnames to access the source code and the build logs:

*   `/_src`
*   `/_logs`

By default, these routes are protected so that they can only be accessed by you and the members of your Vercel Team.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-step%2Flogs-and-sources-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-step%2Flogs-and-sources-dark.png&w=3840&q=75)

Build Logs and Source Protection is enabled by default.

### [Source View](#source-view)

By appending `/_src` to a Deployment URL or [Custom Domain](/docs/domains/add-a-domain) in your web browser, you will be redirected to the Deployment inspector and be able to browse the sources and [build](/docs/deployments/configure-a-build) outputs.

### [Logs View](#logs-view)

By appending `/_logs` to a Deployment URL or [Custom Domain](/docs/domains/add-a-domain) in your web browser, you can see a real-time stream of logs from your deployment build processes by clicking on the Build Logs accordion.

### [Security considerations](#security-considerations)

The pathnames `/_src` and `/_logs` redirect to `https://vercel.com` and require logging into your Vercel account to access any sensitive information. By default, a third-party can never access your source or logs by crafting a deployment URL with one of these paths.

You can configure these paths to make them publicly accessible under the Security tab on the Project Settings page. You can learn more about making paths publicly accessible in the [Build Logs and Source Protection](/docs/projects/overview#logs-and-source-protection) section.

## [Git submodules](#git-submodules)

On Vercel, you can deploy [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) with a [Git provider](/docs/git) as long as the submodule is publicly accessible through the HTTP protocol. Git submodules that are private or requested over SSH will fail during the Build step. However, you can reference private repositories formatted as npm packages in your `package.json` file dependencies. Private repository modules require a special link syntax that varies according to the Git provider. For more information on this syntax, see "[How do I use private dependencies with Vercel?](/guides/using-private-dependencies-with-vercel)".

--------------------------------------------------------------------------------
title: "Build image overview"
description: "Learn about the container image used for Vercel builds."
last_updated: "null"
source: "https://vercel.com/docs/builds/build-image"
--------------------------------------------------------------------------------

# Build image overview

Copy page

Ask AI about this page

Last updated September 24, 2025

When you initiate a deployment, Vercel will [build your project](/docs/builds) within a container using the build image. Vercel supports [multiple runtimes](/docs/functions/runtimes).

| Runtime | [Build image](/docs/builds/build-image) |
| --- | --- |
| [Node.js](/docs/functions/runtimes/node-js) | `22.x` `20.x` |
| [Edge](/docs/functions/runtimes/edge-runtime) |  |
| [Python](/docs/functions/runtimes/python) | `3.12` |
| [Ruby](/docs/functions/runtimes/ruby) | `3.3.x` |
| [Go RuntimeGo](/docs/functions/runtimes/go) |  |
| [Community Runtimes](/docs/functions/runtimes#community-runtimes) |  |

The build image uses [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/) as its base image.

## [Pre-installed packages](#pre-installed-packages)

The following packages are pre-installed in the build image with `dnf`, the default package manager for Amazon Linux 2023.

<table class="table_docsTable__eeHl2"><tbody class="table-body_docsTbody__jjwpP"><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">alsa-lib</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">at-spi2-atk</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">atk</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">autoconf</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">automake</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">brotli</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">bsdtar</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">bzip2</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">bzip2-devel</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">cups-libs</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">expat-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">gcc</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">gcc-c++</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">git</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">glib2-devel</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">glibc-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">gtk3</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">gzip</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">ImageMagick-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">iproute</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">java-11-amazon-corretto-headless</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libXScrnSaver</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libXcomposite</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libXcursor</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libXi</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libXrandr</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libXtst</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libffi-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libglvnd-glx</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libicu</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libjpeg</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libjpeg-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libpng</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libpng-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libstdc++</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libtool</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libwebp-tools</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">libzstd-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">make</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">nasm</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">ncurses-libs</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">ncurses-compat-libs</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">openssl</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">openssl-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">openssl-libs</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">pango</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">procps</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">perl</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">readline-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">ruby-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">strace</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">sysstat</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">tar</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">unzip</code></td></tr><tr aria-roledescription="row" class="row"><td><code class="code_code__TTx9V code_inlineCode__DZHMn">which</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">zlib-devel</code></td><td><code class="code_code__TTx9V code_inlineCode__DZHMn">zstd</code></td></tr></tbody></table>

You can install these packages using the [`dnf`](https://dnf.readthedocs.io/) package manager with the following command:

terminal

```
dnf alsa-lib at-spi2-atk atk autoconf automake brotli bsdtar bzip2 bzip2-devel cups-libs expat-devel gcc gcc-c++ git glib2-devel glibc-devel gtk3 gzip ImageMagick-devel iproute java-11-amazon-corretto-headless libXScrnSaver libXcomposite libXcursor libXi libXrandr libXtst libffi-devel libglvnd-glx libicu libjpeg libjpeg-devel libpng libpng-devel libstdc++ libtool libwebp-tools libzstd-devel make nasm ncurses-libs ncurses-compat-libs openssl openssl-devel openssl-libs pango procps perl readline-devel ruby-devel strace sysstat tar unzip which zlib-devel zstd --yes
```

## [Running the build image locally](#running-the-build-image-locally)

Vercel does not provide the build image itself, but you can use the Amazon Linux 2023 base image to test things locally:

terminal

```
docker run --rm -it amazonlinux:2023.2.20231011.0 sh
```

When you are done, run `exit` to return.

## [Installing additional packages](#installing-additional-packages)

You can install additional packages into the build container by configuring the [Install Command](/docs/deployments/configure-a-build#install-command) within the dashboard or the `["installCommand"](/docs/project-configuration#installcommand)` in your `vercel.json` to use any of the following commands.

The build image includes access to repositories with stable versions of popular packages. You can list all packages with the following command:

terminal

```
dnf list
```

You can search for a package by name with the following command:

terminal

```
dnf search my-package-here
```

You can install a package by name with the following command:

terminal

```
dnf install -y my-package-here
```

--------------------------------------------------------------------------------
title: "Build Queues"
description: "Understand how concurrency and same branch build queues manage multiple simultaneous deployments."
last_updated: "null"
source: "https://vercel.com/docs/builds/build-queues"
--------------------------------------------------------------------------------

# Build Queues

Copy page

Ask AI about this page

Last updated October 15, 2025

Build queueing is when a build must wait for resources to become available before starting. This creates more time between when the code is committed and the deployment being ready.

*   [With On-Demand Concurrent Builds](#with-on-demand-concurrent-builds), builds will never queue.
*   [Without On-Demand Concurrent Builds](#without-on-demand-concurrent-builds), builds can queue under the conditions specified below.

## [With On-Demand Concurrent Builds](#with-on-demand-concurrent-builds)

[On-Demand Concurrent Builds](/docs/deployments/managing-builds#on-demand-concurrent-builds) prevent all build queueing so your team can build faster. Your builds will never be queued becuase Vercel will dynamically scale the amount of builds that can run simultaneously.

If you're experiencing build queues, we strongly recommend [enabling On-Demand Concurrent Builds](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbuild-and-deployment%23on-demand-concurrent-builds&title=Enable+On-Demand+Concurrent+Builds). For billing information, [visit the usage and limits section for builds](/docs/builds/managing-builds#usage-and-limits).

## [Without On-Demand Concurrent Builds](#without-on-demand-concurrent-builds)

When multiple deployments are started concurrently from code changes, Vercel's build system places deployments into one of the following queues:

*   [Concurrency queue](#concurrency-queue): The basics of build resource management
*   [Git branch queue](#git-branch-queue): How builds to the same branch are managed

## [Concurrency queue](#concurrency-queue)

This queue manages how many builds can run in parallel based on the number of [concurrent build slots](/docs/builds/managing-builds#concurrent-builds) available to the team. If all concurrent build slots are in use, new builds are queued until a slot becomes available unless you have On-Demand Concurrent Builds [enabled at the project level](/docs/deployments/managing-builds#project-level-on-demand-concurrent-builds).

### [How concurrent build slots work](#how-concurrent-build-slots-work)

Concurrent build slots are the key factor in concurrent build queuing. They control how many builds can run at the same time and ensure efficient use of resources while prioritizing the latest changes.

Each account plan comes with a predefined number of build slots:

*   Hobby accounts allow one build at a time.
*   Pro accounts support up to 12 simultaneous builds.
*   Enterprise accounts can have [custom limits](/docs/deployments/concurrent-builds#usage-and-limits) based on their plan.

## [Git branch queue](#git-branch-queue)

Builds are handled sequentially. If new commits are pushed while a build is in progress:

1.  The current build is completed first.
2.  Queued builds for earlier commits are skipped.
3.  The most recent commit is built and deployed.

This means that commits in between the current build and most recent commit will not produce builds.

Enterprise users can use [Urgent On-Demand Concurrency](/docs/deployments/managing-builds#urgent-on-demand-concurrent-builds) to skip the Git branch queue for specific builds.

--------------------------------------------------------------------------------
title: "Configuring a Build"
description: "Vercel automatically configures the build settings for many front-end frameworks, but you can also customize the build according to your requirements."
last_updated: "null"
source: "https://vercel.com/docs/builds/configure-a-build"
--------------------------------------------------------------------------------

# Configuring a Build

Copy page

Ask AI about this page

Last updated September 24, 2025

When you make a [deployment](/docs/deployments), Vercel builds your project. During this time, Vercel performs a "shallow clone" on your Git repository using the command `git clone --depth=10 (...)` and fetches ten levels of git commit history. This means that only the latest ten commits are pulled and not the entire repository history.

Vercel automatically configures the build settings for many front-end frameworks, but you can also customize the build according to your requirements.

To configure your Vercel build with customized settings, choose a project from the [dashboard](/dashboard) and go to its Settings tab.

The Build and Deployment section of the Settings tab offers the following options to customize your build settings:

*   [Framework Settings](#framework-settings)
*   [Root Directory](#root-directory)
*   [Node.js Version](/docs/functions/runtimes/node-js/node-js-versions#setting-the-node.js-version-in-project-settings)
*   [Prioritizing Production Builds](/docs/deployments/concurrent-builds#prioritize-production-builds)
*   [On-Demand Concurrent Builds](/docs/deployments/managing-builds#on-demand-concurrent-builds)

## [Framework Settings](#framework-settings)

If you'd like to override the settings or specify a different framework, you can do so from the Build & Development Settings section.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-step%2Fframework-settings-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-step%2Fframework-settings-dark.png&w=1920&q=75)

Framework settings.

### [Framework Preset](#framework-preset)

You have a wide range of frameworks to choose from, including Next.js, Svelte, and Nuxt. In several use cases, Vercel automatically detects your project's framework and sets the best settings for you.

Inside the Framework Preset settings, use the drop-down menu to select the framework of your choice. This selection will be used for all deployments within your Project. The available frameworks are listed below:

Show More

However, if no framework is detected, "Other" will be selected. In this case, the Override toggle for the Build Command will be enabled by default so that you can enter the build command manually. The remaining deployment process is that for default frameworks.

If you would like to override Framework Preset for a specific deployment, add [`framework`](/docs/project-configuration#framework) to your `vercel.json` configuration.

### [Build Command](#build-command)

Vercel automatically configures the Build Command based on the framework. Depending on the framework, the Build Command can refer to the project’s `package.json` file.

For example, if [Next.js](https://nextjs.org) is your framework:

*   Vercel checks for the `build` command in `scripts` and uses this to build the project
*   If not, the `next build` will be triggered as the default Build Command

If you'd like to override the Build Command for all deployments in your Project, you can turn on the Override toggle and specify the custom command.

If you would like to override the Build Command for a specific deployment, add [`buildCommand`](/docs/project-configuration#buildcommand) to your `vercel.json` configuration.

If you update the **Override** setting, it will be applied on your next deployment.

### [Output Directory](#output-directory)

After building a project, most frameworks output the resulting build in a directory. Only the contents of this Output Directory will be served statically by Vercel.

If Vercel detects a framework, the output directory will automatically be configured.

If you update the **Override** setting, it will be applied on your next deployment.

For projects that [do not require building](#skip-build-step), you might want to serve the files in the root directory. In this case, do the following:

*   Choose "Other" as the Framework Preset. This sets the output directory as `public` if it exists or `.` (root directory of the project) otherwise
*   If your project doesn’t have a `public` directory, it will serve the files from the root directory
*   Alternatively, you can turn on the Override toggle and leave the field empty (in which case, the build step will be skipped)

If you would like to override the Output Directory for a specific deployment, add [`outputDirectory`](/docs/project-configuration#outputdirectory) to your `vercel.json` configuration.

### [Install Command](#install-command)

Vercel auto-detects the install command during the build step. It installs dependencies from `package.json`, including `devDependencies` ([which can be excluded](/docs/deployments/troubleshoot-a-build#excluding-development-dependencies)). The install path is set by the [root directory](#root-directory).

The install command can be managed in two ways: through a project override, or per-deployment. See [manually specifying a package manager](/docs/package-managers#manually-specifying-a-package-manager) for more details.

To learn what package managers are supported on Vercel, see the [package manager support](/docs/package-managers) documentation.

#### [Corepack](#corepack)

Corepack is considered [experimental](https://nodejs.org/docs/latest-v16.x/api/documentation.html#stability-index) and therefore, breaking changes or removal may occur in any future release of Node.js.

[Corepack](https://nodejs.org/docs/latest-v16.x/api/corepack.html) is an experimental tool that allows a Node.js project to pin a specific version of a package manager.

You can enable Corepack by adding an [environment variable](/docs/environment-variables) with name `ENABLE_EXPERIMENTAL_COREPACK` and value `1` to your Project.

Then, set the [`packageManager`](https://nodejs.org/docs/latest-v16.x/api/packages.html#packagemanager) property in the `package.json` file in the root of your repository. For example:

package.json

```
{
  "packageManager": "pnpm@7.5.1"
}
```

A `package.json` file with [pnpm](https://pnpm.io) version 7.5.1

#### [Custom Install Command for your API](#custom-install-command-for-your-api)

The Install Command defined in the Project Settings will be used for front-end frameworks that support Vercel functions for APIs.

If you're using [Vercel functions](/docs/functions) defined in the natively supported `api` directory, a different Install Command will be used depending on the language of the Vercel Function. You cannot customize this Install Command.

### [Development Command](#development-command)

This setting is relevant only if you’re using `vercel dev` locally to develop your project. Use `vercel dev` only if you need to use Vercel platform features like [Vercel functions](/docs/functions). Otherwise, it's recommended to use the development command your framework provides (such as `next dev` for Next.js).

The Development Command settings allow you to customize the behavior of `vercel dev`. If Vercel detects a framework, the development command will automatically be configured.

If you’d like to use a custom command for `vercel dev`, you can turn on the Override toggle. Please note the following:

*   If you specify a custom command, your command must pass your framework's `$PORT` variable (which contains the port number). For example, in [Next.js](https://nextjs.org/) you should use: `next dev --port $PORT`
*   If the development command is not specified, `vercel dev` will fail. If you've selected "Other" as the framework preset, the default development command will be empty
*   You must create a deployment and have your local project linked to the project on Vercel (using `vercel`). Otherwise, `vercel dev` will not work correctly

If you would like to override the Development Command, add [`devCommand`](/docs/project-configuration#devcommand) to your `vercel.json` configuration.

### [Skip Build Step](#skip-build-step)

Some static projects do not require building. For example, a website with only HTML/CSS/JS source files can be served as-is.

In such cases, you should:

*   Specify "Other" as the framework preset
*   Enable the Override option for the Build Command
*   Leave the Build Command empty

This prevents running the build, and your content is served directly.

## [Root Directory](#root-directory)

In some projects, the top-level directory of the repository may not be the root directory of the app you’d like to build. For example, your repository might have a front-end directory containing a stand-alone [Next.js](https://nextjs.org/) app.

For such cases, you can specify the project Root Directory. If you do so, please note the following:

*   Your app will not be able to access files outside of that directory. You also cannot use `..` to move up a level
*   This setting also applies to [Vercel CLI](/docs/cli). Instead of running `vercel <directory-name>` to deploy, specify `<directory-name>` here so you can just run `vercel`

To configure the Root Directory:

1.  Navigate to the Build and Deployment page of your Project Settings
2.  Scroll down to Root Directory
3.  Enter the path to the root directory of your app
4.  Click Save to apply the changes

If you update the root directory setting, it will be applied on your next deployment.

#### [Skipping unaffected projects](#skipping-unaffected-projects)

In a monorepo, you can [skip deployments](/docs/monorepos#skipping-unaffected-projects) for projects that were not affected by a commit. To configure:

1.  Navigate to the Build and Deployment page of your Project Settings
2.  Scroll down to Root Directory
3.  Enable the Skip deployment switch

--------------------------------------------------------------------------------
title: "Managing Builds"
description: "Vercel allows you to increase the speed of your builds when needed in specific situations and workflows."
last_updated: "null"
source: "https://vercel.com/docs/builds/managing-builds"
--------------------------------------------------------------------------------

# Managing Builds

Copy page

Ask AI about this page

Last updated October 22, 2025

When you build your application code, Vercel runs compute to install dependencies, run your build script, and upload the build output to our [CDN](/docs/cdn). There are several ways in which you can manage your build compute.

*   If you need faster build machines or more memory, you can purchase [Enhanced or Turbo build machines](#larger-build-machines).
*   If you are deploying frequently and seeing [build queues](/docs/builds/build-queues), you can enable [On-Demand Concurrent Builds](#on-demand-concurrent-builds) where you pay for build compute so your builds always start immediately.

[Visit Build Diagnostics in the Observability tab of the Vercel Dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fbuild-diagnostics&title=Visit+Build+Diagnostics) to find your build durations. You can also use this table to quickly identify which solution fits your needs:

| Your situation | Solution | Best for |
| --- | --- | --- |
| Builds are slow or running out of resources | [Enhanced/Turbo build machines](#larger-build-machines) | Large apps, complex dependencies |
| Builds are frequently queued | [On-demand Concurrent Builds](#on-demand-concurrent-builds) | Teams with frequent deployments |
| Specific projects are frequently queued | [Project-level on-demand](#project-level-on-demand-concurrent-builds) | Fast-moving projects |
| Occasional urgent deploy stuck in queue | [Force an on-demand build](#force-an-on-demand-build) | Ad-hoc critical fixes |
| Production builds stuck behind preview builds | [Prioritize production builds](#prioritize-production-builds) | All production-heavy workflows |

## [Larger build machines](#larger-build-machines)

Enhanced and Turbo build machines are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

For Pro and Enterprise customers, we offer two higher-tier build machines with more vCPUs, memory and disk space than Standard.

| Build machine type | Number of vCPUs | Memory (GB) | Disk size (GB) |
| --- | --- | --- | --- |
| Standard | 4 | 8 | 23 |
| Enhanced | 8 | 16 | 56 |
| Turbo | 30 | 60 | 64 |

You can set the build machine type under Project Settings > Build and Deployment > Build Machine.

For Enterprise customers, using Enhanced or Turbo build machines will also enable [On-demand Concurrent Builds](#on-demand-concurrent-builds).

Enterprise customers who have Enhanced build machines enabled via contract will always use them by default. You can view if you have this enabled under Team Settings > Billing > Enhanced Build Machines. To update it, you need to contact your account manager.

## [On-demand concurrent builds](#on-demand-concurrent-builds)

On-demand concurrent builds is available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

Those with the [owner](/docs/rbac/access-roles#owner-role) role can access this feature

By default, only one concurrent build is executed at a time. Other builds will be queued and handled in chronological order (FIFO Order). On-demand concurrent builds allow all builds to be executed in parallel, with no queues.

When enabled, you are charged for On-demand Concurrent Builds based on the number of concurrent builds required to allow the builds to proceed as explained in [usage and limits](#usage-and-limits).

### [Project-level on-demand concurrent builds](#project-level-on-demand-concurrent-builds)

When you enable on-demand build concurrency at the level of a project, any queued builds in that project will automatically be allowed to proceed.

You can enable it on the project's [Build and Deployment Settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment&title=Go+to+Build+and+Deployment+Settings) page:

DashboardcURLSDK

1.  From your Vercel dashboard, select the project you wish to enable it for.
2.  Select the Settings tab, and go to the Build and Deployment section of your [Project Settings](/docs/projects/overview#project-settings).
3.  Under On-Demand Concurrent Builds, toggle the switch to Enabled.
4.  The standard option is selected by default with 4 vCPUs and 8 GB of memory. You can switch to [Enhanced or Turbo build machines](#larger-build-machines) with up to 30 vCPUs and 60 GB of memory.
5.  Click Save.

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

cURL

```
curl --request PATCH \
  --url https://api.vercel.com/v9/projects/YOUR_PROJECT_ID?teamId=YOUR_TEAM_ID \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "resourceConfig": {
      "elasticConcurrencyEnabled": true,
      "buildMachineType": "enhanced",
    }
  }'
```

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

updateProject

```
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.projects.updateProject({
    idOrName: 'YOUR_PROJECT_ID',
    teamId: 'YOUR_TEAM_ID',
    requestBody: {
      resourceConfig: {
        elasticConcurrencyEnabled: true,
        buildMachineType: 'enhanced',
      },
    },
  });
 
  // Handle the result
  console.log(result);
}
 
run();
```

New projects on Enterprise teams will have on-demand concurrency turned on by default.

### [Force an on-demand build](#force-an-on-demand-build)

For individual deployments, you can force build execution using the Start Building Now button. Regardless of the reason why this build was queued, it will proceed.

1.  Select your project from the [dashboard](/dashboard).
    
2.  From the top navigation, select the Deployments tab.
    
3.  Find the queued deployment that you would like to build from the list. You can use the Status filter to help find it. You have 2 options:
    
    *   Select the three dots to the right of the deployment and select Start Building Now.
    *   Click on the deployment list item to go to the deployment's detail page and click Start Building Now.
4.  Confirm that you would like to build this deployment in the Start Building Now dialog.
    

## [Optimizing builds](#optimizing-builds)

Some other considerations to take into account when optimizing your builds include:

*   [Understand](/docs/deployments/troubleshoot-a-build#understanding-build-cache) and [manage](/docs/deployments/troubleshoot-a-build#managing-build-cache) the build cache. By default, Vercel caches the dependencies of your project, based on your framework, to speed up the build process
*   You may choose to [Ignore the Build Step](/docs/project-configuration/git-settings#ignored-build-step) on redeployments if you know that the build step is not necessary under certain conditions
*   Use the most recent version of your runtime, particularly Node.js, to take advantage of the latest performance improvements. To learn more, see [Node.js](/docs/functions/runtimes/node-js#default-and-available-versions)

## [Prioritize production builds](#prioritize-production-builds)

Prioritize production builds is available on [all plans](/docs/plans)

If a build has to wait for queued preview deployments to finish, it can delay the production release process. When Vercel queues builds, we'll processes them in chronological order (FIFO Order).

For any new projects created after December 12, 2024, Vercel will prioritize production builds by default.

To ensure that changes to the [production environment](/docs/deployments/environments#production-environment) are prioritized over [preview deployments](/docs/deployments/environments#preview-environment-pre-production) in the queue, you can enable Prioritize Production Builds:

1.  From your Vercel dashboard, select the project you wish to enable it for
2.  Select the Settings tab, and go to the [Build and Deployment section](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment&title=Prioritize+Production+Builds+Setting) of your [Project Settings](/docs/projects/overview#project-settings)
3.  Under Prioritize Production Builds, toggle the switch to Enabled

## [Usage and limits](#usage-and-limits)

The on-demand build usage is based on the amount of time it took for a deployment to build when using a concurrent build.

### [Pro plan](#pro-plan)

On-demand concurrent builds are priced in $ per minute of build time and is based on the type of build machines used.

| Build machine type | Price per build minute |
| --- | --- |
| Standard | $0.014 |
| Enhanced | $0.030 |
| Turbo | $0.113 |

### [Enterprise plan](#enterprise-plan)

On-demand concurrent builds are priced in [MIUs](/docs/pricing/understanding-my-invoice#managed-infrastructure-units-miu) per minute of build time used and the rate depends on the number of contracted concurrent builds and the machine type.

| Concurrent builds contracted | Cost ([MIU](/docs/pricing/understanding-my-invoice#managed-infrastructure-units-miu) per minute) for Standard build machines | Cost ([MIU](/docs/pricing/understanding-my-invoice#managed-infrastructure-units-miu) per minute) for Enhanced build machines | Cost ([MIU](/docs/pricing/understanding-my-invoice#managed-infrastructure-units-miu) per minute) for Turbo build machines |
| --- | --- | --- | --- |
| 1-5 | 0.014 MIUs | 0.030 MIUs | 0.113 MIUs |
| 6-10 | 0.012 MIUs | 0.026 MIUs | 0.098 MIUs |
| 10+ | 0.010 MIUs | 0.022 MIUs | 0.083 MIUs |

--------------------------------------------------------------------------------
title: "Vercel CDN overview"
description: "Vercel's CDN enables you to store content close to your customers and run compute in regions close to your data, reducing latency and improving end-user performance."
last_updated: "null"
source: "https://vercel.com/docs/cdn"
--------------------------------------------------------------------------------

# Vercel CDN overview

Copy page

Ask AI about this page

Last updated September 15, 2025

Vercel's CDN is a globally distributed platform that stores content near your customers and runs compute in [regions](/docs/regions) close to your data, reducing latency and improving end-user performance.

If you're deploying an app on Vercel, you already use our CDN. These docs will teach you how to optimize your apps and deployment configuration to get the best performance for your use case.

![Our global CDN has 126 Points of Presence in 94 cities across 51 countries.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fedge-network%2Fcdn-pops-light.png&w=3840&q=75)![Our global CDN has 126 Points of Presence in 94 cities across 51 countries.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fedge-network%2Fcdn-pops-dark.png&w=3840&q=75)

Our global CDN has 126 Points of Presence in 94 cities across 51 countries.

## [Global network architecture](#global-network-architecture)

Vercel's CDN is built on a robust global infrastructure designed for optimal performance and reliability:

*   Points of Presence (PoPs): Our network includes 126 PoPs distributed worldwide. These PoPs act as the first point of contact for incoming requests and route requests to the nearest region.
*   Vercel Regions: Behind these PoPs, we maintain [19 compute-capable regions](/docs/regions) where your code runs close to your data.
*   Private Network: Traffic flows through private, low-latency connections from PoPs to the nearest region, ensuring fast and efficient data transfer.

This architecture balances the widespread geographical distribution benefits with the efficiency of concentrated caching and computing resources. By maintaining fewer, dense regions, we increase cache hit probabilities while ensuring low-latency access through our extensive PoP network.

## [Features](#features)

*   [Redirects](/docs/redirects): Redirects tell the client to make a new request to a different URL. They are useful for enforcing HTTPS, redirecting users, and directing traffic.
*   [Rewrites](/docs/rewrites): Rewrites change the URL the server uses to fetch the requested resource internally, allowing for dynamic content and improved routing.
*   [Headers](/docs/headers): Headers can modify the request and response headers, improving security, performance, and functionality.
*   [Caching](/docs/edge-cache): Caching stores responses at the edge, reducing latency and improving performance
*   [Streaming](/docs/functions/streaming-functions): Streaming enhances your user's perception of your app's speed and performance.
*   [HTTPS / SSL](/docs/encryption): Vercel serves every deployment over an HTTPS connection by automatically provisioning SSL certificates.
*   [Compression](/docs/compression): Compression reduces data transfer and improves performance, supporting both gzip and brotli compression.

## [Pricing](#pricing)

Vercel's CDN pricing is divided into three resources:

*   Fast Data Transfer: Data transfer between the Vercel CDN and the user's device.
*   Fast Origin Transfer: Data transfer between the CDN and Vercel Functions.
*   Edge Requests: Requests made to the CDN.

![An overview of how items relate to the CDN](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fcdn%2Fsite-cdn-data-light.png&w=3840&q=75)![An overview of how items relate to the CDN](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fcdn%2Fsite-cdn-data-dark.png&w=3840&q=75)

An overview of how items relate to the CDN

All resources are billed based on usage with each plan having an [included allotment](/docs/pricing). Those on the Pro plan are billed according to additional allotments.

The pricing for each resource is based on the region from which requests to your site come. Use the dropdown to select your preferred region and see the pricing for each resource.

Select a Region

Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dubai, UAE (dxb1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, UK (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)

Managed Infrastructure pricing
| 
Resource

 | 

Hobby Included

 | 

On-demand Rates

 |
| --- | --- | --- |
| 

[Fast Data Transfer](/docs/pricing/regional-pricing)

 | First 100 GB | $0.15 per 1 GB |
| 

[Fast Origin Transfer](/docs/pricing/regional-pricing)

 | First 10 GB | $0.06 per 1 GB |
| 

[Edge Requests](/docs/pricing/regional-pricing)

 | First 1,000,000 | $2.00 per 1,000,000 Requests |

## [Usage](#usage)

The table below shows the metrics for the [Networking](/docs/pricing/networking) section of the Usage dashboard.

To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.

Manage and Optimize pricing
| 
Metric

 | 

Description

 | 

Priced

 | 

Optimize

 |
| --- | --- | --- | --- |
| [Top Paths](/docs/manage-cdn-usage#top-paths) | The paths that consume the most resources on your team | N/A | N/A |
| [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer) | The data transfer between Vercel's CDN and your sites' end users. | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/manage-cdn-usage#optimizing-fast-data-transfer) |
| [Fast Origin Transfer](/docs/manage-cdn-usage#fast-origin-transfer) | The data transfer between Vercel's CDN to Vercel Compute | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/manage-cdn-usage#optimizing-fast-origin-transfer) |
| [Edge Requests](/docs/manage-cdn-usage#edge-requests) | The number of cached and uncached requests that your deployments have received | [Yes](/docs/pricing/regional-pricing) | [Learn More](/docs/manage-cdn-usage#optimizing-edge-requests) |

See the [manage and optimize networking usage](/docs/pricing/networking) section for more information on how to optimize your usage.

## [Supported protocols](#supported-protocols)

The CDN supports the following protocols (negotiated with [ALPN](https://tools.ietf.org/html/rfc7301)):

*   [HTTPS](https://en.wikipedia.org/wiki/HTTPS)
*   [HTTP/1.1](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
*   [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2)

## [Using Vercel's CDN locally](#using-vercel's-cdn-locally)

Vercel supports 35 [frontend frameworks](/docs/frameworks). These frameworks provide a local development environment used to test your app before deploying to Vercel.

Through [framework-defined infrastructure](https://vercel.com/blog/framework-defined-infrastructure), Vercel then transforms your framework build outputs into globally [managed infrastructure](/products/managed-infrastructure) for production.

If you are using [Vercel Functions](/docs/functions) or other compute on Vercel _without_ a framework, you can use the [Vercel CLI](/docs/cli) to test your code locally with [`vercel dev`](/docs/cli/dev).

## [Using Vercel's CDN with other CDNs](#using-vercel's-cdn-with-other-cdns)

While sometimes necessary, proceed with caution when you place another CDN in front of Vercel:

*   Vercel's CDN is designed to deploy new releases of your site without downtime by purging the [Edge Cache](/docs/edge-cache) globally and replacing the current deployment.
*   If you use an additional CDN in front of Vercel, it can cause issues because Vercel has no control over the other provider, leading to the serving of stale content or returning 404 errors.
*   To avoid these problems while still using another CDN, we recommend you either configure a short cache time or disable the cache entirely. Visit the documentation for your preferred CDN to learn how to do either option or learn more about [using a proxy](/guides/can-i-use-a-proxy-on-top-of-my-vercel-deployment) in front of Vercel.

--------------------------------------------------------------------------------
title: "Working with Checks"
description: "Vercel automatically keeps an eye on various aspects of your web application using the Checks API. Learn how to use Checks in your Vercel workflow here."
last_updated: "null"
source: "https://vercel.com/docs/checks"
--------------------------------------------------------------------------------

# Working with Checks

Copy page

Ask AI about this page

Last updated September 15, 2025

Checks are tests and assertions created and run after every successful deployment. Checks API defines your application's quality metrics, runs end-to-end tests, investigates APIs' reliability, and checks your deployment.

Most testing and CI/CD flows occur in synthetic environments. This leads to false results, overlooked performance degradation, and missed broken connections.

## [Types of flows enabled by Checks API](#types-of-flows-enabled-by-checks-api)

| Flow Type | Description |
| --- | --- |
| Core | Checks `200` responses on specific pages or APIs. Determine the deployment's health and identify issues with code, errors, or broken connections |
| Performance | Collects [core web vital](/docs/speed-insights) information for specific pages and compares it with the new deployment. It helps you decide whether to build the deployment or block it for further investigation |
| End-to-end | Validates that your deployment has all the required components to build successfully. And identifies any broken pages, missing images, or other assets |
| Optimization | Optimizes information about the bundle size. Ensures that your website manages large assets like package and image size |

## [Checks lifecycle](#checks-lifecycle)

![The depiction of how the Checks lifecycle works.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fchecks%2Fchecks-overview-light.png&w=3840&q=75)![The depiction of how the Checks lifecycle works.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fchecks%2Fchecks-overview-dark.png&w=3840&q=75)

The depiction of how the Checks lifecycle works.

The diagram shows the complete lifecycle of how a check works:

1.  When a [deployment](/docs/deployments) is created, Vercel triggers the `deployment.created` webhook. This tells integrators that checks can now be registered
2.  Next, an integrator uses the Checks API to create checks defined in the integration configuration
3.  When the deployment is built, Vercel triggers the `deployment.ready` webhook. This notifies integrators to begin checks on the deployment
4.  Vercel waits until all the created checks receive an update
5.  Once all checks receive a `conclusion`, aliases will apply, and the deployment will go live

Learn more about this process in the [Anatomy of Checks API](/docs/integrations/checks-overview/creating-checks)

## [Checks integrations](#checks-integrations)

You can create a [native](/docs/integrations#native-integrations) or [connectable account](/docs/integrations#connectable-accounts) integration that works with the checks API to facilitate testing of deployments for Vercel users.

### [Install integrations](#install-integrations)

Vercel users can find and install your integration from the [Marketplace](/marketplace) under [testing](/marketplace/category/testing), [monitoring](/marketplace/category/monitoring) or [observability](/marketplace/category/observability).

### [Build your Checks integration](#build-your-checks-integration)

Once you have [created your integration](/docs/integrations/create-integration/marketplace-product), [publish](/docs/integrations/create-integration/submit-integration) it to the marketplace by following these guidelines:

*   Provide low or no configuration solutions for developers to run checks
*   A guided onboarding process for developers from the installation to the end result
*   Provide relevant information about the outcome of the test on the Vercel dashboard
*   Document how to go beyond the default behavior to build custom tests for advanced users

--------------------------------------------------------------------------------
title: "Checks API Reference"
description: "The Vercel Checks API let you create tests and assertions that run after each deployment has been built, and are powered by Vercel Integrations."
last_updated: "null"
source: "https://vercel.com/docs/checks/checks-api"
--------------------------------------------------------------------------------

# Checks API Reference

Copy page

Ask AI about this page

Last updated September 24, 2025

API endpoints allow integrations to interact with the Vercel platform. Integrations can run checks every time you create a deployment.

The `post` and `patch` endpoints must be called with an OAuth2, or it will produce a `400` error.

### [Create a new check](#using-the-checks-api/endpoints/create-a-new-check)

Allows the integration to create and register checks. When the "deployment" event triggers, the endpoint registers new checks. It runs until the "deployment.succeeded" event. The endpoint will then set the check "status" to "running".

| Action | Endpoint |
| --- | --- |
| 
Read/Write

 | 

POST

[

/v1/deployments/{deploymentId}/checks

](/docs/rest-api#endpoints/checks/creates-a-new-check)

 |

### [Update a check](#using-the-checks-api/endpoints/update-a-check)

Allows the integration to update existing checks with a new status or conclusion. This endpoint sets the status to “completed”. The value for the conclusion can be "canceled", "failed", "neutral", "succeeded", or "skipped".

| Action | Endpoint |
| --- | --- |
| 
Read/Write

 | 

PATCH

[

/v1/deployments/{deploymentId}/checks/{checkId}

](/docs/rest-api#endpoints/checks/update-a-check)

 |

### [Get all checks](#using-the-checks-api/endpoints/get-all-checks)

Allows integration to fetch all existing checks with all their attributes. For comparison purposes, you can use it to get information from a previous deployment.

| Action | Endpoint |
| --- | --- |
| 
Read

 | 

GET

[

/v1/deployments/{deploymentId}/checks

](/docs/rest-api#endpoints/checks/retrieve-a-list-of-all-checks)

 |

### [Get one check](#using-the-checks-api/endpoints/get-one-check)

Allows integration to fetch only a single check with all the attributes. For comparison purposes, you can use it to get information from a previous deployment.

| Action | Endpoint |
| --- | --- |
| 
Read

 | 

GET

[

/v1/deployments/{deploymentId}/checks/{checkId}

](/docs/rest-api#endpoints/checks/get-a-single-check)

 |

### [Rerequest a failed check](#using-the-checks-api/endpoints/rerequest-a-failed-check)

Allows integration to return a new outcome or rewrite an existing check result. This endpoint is used for check reruns.

| Action | Endpoint |
| --- | --- |
| 
Read/Write

 | 

POST

[

/v1/deployments/{deploymentId}/checks/{checkId}/rerequest

](/docs/rest-api#endpoints/checks/rerequest-a-check)

 |

--------------------------------------------------------------------------------
title: "Anatomy of the Checks API"
description: "Learn how to create your own Checks with Vercel Integrations. You can build your own Integration in order to register any arbitrary Check for your deployments."
last_updated: "null"
source: "https://vercel.com/docs/checks/creating-checks"
--------------------------------------------------------------------------------

# Anatomy of the Checks API

Copy page

Ask AI about this page

Last updated September 24, 2025

Checks API extends the build and deploy process once your deployment is ready. Each check behaves like a webhook that triggers specific events, such as `deployment.created`, `deployment.ready`, and `deployment.succeeded`. The test are verified before domains are assigned.

To learn more, see the [Supported Webhooks Events docs](/docs/integrations/webhooks-overview/webhooks-api#supported-event-types).

The workflow for registering and running a check is as follows:

1.  A check is created after the `deployment.created` event
2.  When the `deployment.ready` event triggers, the check updates its `status` to `running`
3.  When the check is finished, the `status` updates to `completed`

If a check is "rerequestable", your integration users get an option to [rerequest and rerun the failing checks](#rerunning-checks).

### [Types of Checks](#types-of-checks)

Depending on the type, checks can block the domain assignment stage of deployments.

*   Blocking Checks: Prevents a successful deployment and returns a `conclusion` with a `state` value of `canceled` or `failed`. For example, a [Core Check](/docs/observability/checks-overview#types-of-flows-enabled-by-checks-api) returning a `404` error results in a `failed` `conclusion` for a deployment
*   Non-blocking Checks: Return test results with a successful deployment regardless of the `conclusion`

A blocking check with a `failed` state is configured by the developer (and not the integration).

### [Associations](#associations)

Checks are always associated with a specific deployment that is tested and validated.

### [Body attributes](#body-attributes)

| Attributes | Format | Purpose |
| --- | --- | --- |
| `blocking` | Boolean | Tells Vercel if this check needs to block the deployment |
| `name` | String | Name of the check |
| `detailsUrl` | String (optional) | URL to display in the Vercel dashboard |
| `externalID` | String (optional) | ID used for external use |
| `path` | String (optional) | Path of the page that is being checked |
| `rerequestable` | Boolean (optional) | Tells Vercel if the check can rerun. Users can trigger a `deployment.check-rerequested` [webhook](/docs/webhooks/webhooks-api#deployment.check-rerequested), through a button on the deployment page |
| `conclusion` | String (optional) | The result of a running check. For [blocking checks](#types-of-checks) the values can be `canceled`, `failed`, `neutral`, `succeeded`, `skipped`. `canceled` and `failed` |
| `status` | String (optional) | Tells Vercel the status of the check with values: `running` and `completed` |
| `output` | Object (optional) | Details about the result of the check. Vercel uses this data to display actionable information for developers. This helps them debug failed checks |

The check gets a `stale` status if there is no status update for more than one hour (`status = registered`). The same applies if the check is running (`status = running`) for more than five minutes.

### [Response](#response)

| Response | Format | Purpose |
| --- | --- | --- |
| `status` | String | The status of the check. It expects specific values like `running` or `completed` |
| `state` | String | Tells the current state of the connection |
| `connectedAt` | Number | Timestamp (in milliseconds) of when the configuration was connected |
| `type` | String | Name of the integrator performing the check |

### [Response codes](#response-codes)

| Status | Outcome |
| --- | --- |
| `200` | Success |
| `400` | One of the provided values in the request body is invalid, OR one of the provided values in the request query is invalid |
| `403` | The provided token is not from an OAuth2 client OR you do not have permission to access this resource OR the API token doesn't have permission to perform the request |
| `404` | The check was not found OR the deployment was not found |
| `413` | The output provided is too large |

## [Rich results](#rich-results)

### [Output](#output)

The `output` property can store any data like [Web Vitals](/docs/speed-insights) and [Virtual Experience Score](/docs/speed-insights/metrics#predictive-performance-metrics-with-virtual-experience-score). It is defined under a `metrics` field:

| Key | [Type](#api-basics/types) | Description |
| --- | --- | --- |
| `TBT` | [Map](#api-basics/types) | The [Total Blocking Time](/docs/speed-insights/metrics#total-blocking-time-tbt), measured by the check |
| `LCP` | [Map](#api-basics/types) | The [Largest Contentful Paint](/docs/speed-insights/metrics#largest-contentful-paint-lcp), measured by the check |
| `FCP` | [Map](#api-basics/types) | The [First Contentful Paint](/docs/speed-insights/metrics#first-contentful-paint-fcp), measured by the check |
| `CLS` | [Map](#api-basics/types) | The [Cumulative Layout Shift](/docs/speed-insights/metrics#cumulative-layout-shift-cls), measured by the check |
| `virtualExperienceScore` | [Map](#api-basics/types) | The overall [Virtual Experience Score](/docs/speed-insights/metrics#predictive-performance-metrics-with-virtual-experience-score) measured by the check |

Each of these keys has the following properties:

| Key | [Type](#api-basics/types) | Description |
| --- | --- | --- |
| `value` | [Float](#api-basics/types) | The value measured for a particular metric, in milliseconds. For `virtualExperienceScore` this value is the percentage between 0 and 1 |
| `previousValue` | [Float](#api-basics/types) | A previous value for comparison purposes |
| `source` | [Enum](#api-basics/types) | `web-vitals` |

### [Metrics](#metrics)

`metrics` makes [Web Vitals](/docs/speed-insights) visible on checks. It is defined inside `output` as follows:

checks-metrics.json

```
{
  "path": "/",
  "output": {
    "metrics": {
        "FCP": {
          "value": 1200,
          "previousValue": 1400,
          "source": "web-vitals"
        }
        "LCP": {
          "value": 1200,
          "previousValue": 1400,
          "source": "web-vitals"
        },
        "CLS": {
          "value": 1200,
          "previousValue": 1400,
          "source": "web-vitals"
        },
        "TBT": {
          "value": 1200,
          "previousValue": 1400,
          "source": "web-vitals"
        }
      }
    }
  }
}
```

All fields are required except `previousValue`. If `previousValue` is present, the delta will be shown.

### [Rerunning checks](#rerunning-checks)

A check can be "rerequested" using the `deployment.check-rerequested` webhook. Add the `rerequestable` attribute, and you can rerequest failed checks.

A rerequested check triggers the`deployment.check-rerequested` webhook. It updates the check `status` to `running` and resets the `conclusion`, `detailsUrl`, `externalId`, and `output` fields.

### [Skipping Checks](#skipping-checks)

You can "Skip" to stop and ignore check results without affecting the alias assignment. You cannot skip active checks. They continue running until built successfully, and assign domains as the last step.

### [Availability of URLs](#availability-of-urls)

For "Running Checks", only the [Automatic Deployment URL](/docs/deployments/generated-urls) is available. [Automatic Branch URL](/docs/deployments/generated-urls#generated-from-git) and [Custom Domains](/docs/domains/add-a-domain) will apply once the checks finish.

### [Order of execution](#order-of-execution)

Checks may take different times to run. Each integrator determines the running order of the checks. While [Vercel REST API](/docs/rest-api/vercel-api-integrations) determines the order of check results.

### [Status and conclusion](#status-and-conclusion)

When Checks API begins running on your deployment, the `status` is set to `running`. Once it gets a `conclusion`, the `status` updates to `completed`. This results in a successful deployment.

However, your deployment will fail if the `conclusion` updates to one of the following values:

| Conclusion | `blocking=true` |
| --- | --- |
| `canceled` | Yes |
| `failed` | Yes |
| `neutral` | No |
| `succeeded` | No |
| `skipped` | No |

--------------------------------------------------------------------------------
title: "Vercel CLI Overview"
description: "Learn how to use the Vercel command-line interface (CLI) to manage and configure your Vercel Projects from the command line."
last_updated: "null"
source: "https://vercel.com/docs/cli"
--------------------------------------------------------------------------------

# Vercel CLI Overview

Copy page

Ask AI about this page

Last updated March 12, 2025

Vercel gives you multiple ways to interact with and configure your Vercel Projects. With the command-line interface (CLI) you can interact with the Vercel platform using a terminal, or through an automated system, enabling you to [retrieve logs](/docs/cli/logs), manage [certificates](/docs/cli/certs), replicate your deployment environment [locally](/docs/cli/dev), manage Domain Name System (DNS) [records](/docs/cli/dns), and more.

If you'd like to interface with the platform programmatically, check out the [REST API documentation](/docs/rest-api).

## [Installing Vercel CLI](#installing-vercel-cli)

To download and install Vercel CLI, run the following command:

pnpmyarnnpmbun

```
pnpm i -g vercel
```

## [Updating Vercel CLI](#updating-vercel-cli)

When there is a new release of Vercel CLI, running any command will show you a message letting you know that an update is available.

If you have installed our command-line interface through [npm](http://npmjs.org/) or [Yarn](https://yarnpkg.com), the easiest way to update it is by running the installation command yet again.

pnpmyarnnpmbun

```
pnpm i -g vercel@latest
```

If you see permission errors, please read npm's [official guide](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally). Yarn depends on the same configuration as npm.

## [Checking the version](#checking-the-version)

The `--version` option can be used to verify the version of Vercel CLI currently being used.

terminal

```
vercel --version
```

Using the `vercel` command with the `--version` option.

## [Using in a CI/CD environment](#using-in-a-ci/cd-environment)

Vercel CLI requires you to log in and authenticate before accessing resources or performing administrative tasks. In a terminal environment, you can use [`vercel login`](/docs/cli/login), which requires manual input. In a CI/CD environment where manual input is not possible, you can create a token on your [tokens page](/account/tokens) and then use the [`--token` option](/docs/cli/global-options#token) to authenticate.

## [Available Commands](#available-commands)

[\- alias](/docs/cli/alias)

[\- bisect](/docs/cli/bisect)

[\- blob](/docs/cli/blob)

[\- build](/docs/cli/build)

[\- certs](/docs/cli/certs)

[\- curl](/docs/cli/curl)

[\- deploy](/docs/cli/deploy)

[\- dev](/docs/cli/dev)

[\- dns](/docs/cli/dns)

[\- domains](/docs/cli/domains)

[\- env](/docs/cli/env)

[\- git](/docs/cli/git)

[\- help](/docs/cli/help)

[\- init](/docs/cli/init)

[\- inspect](/docs/cli/inspect)

[\- link](/docs/cli/link)

[\- list](/docs/cli/list)

[\- login](/docs/cli/login)

[\- logout](/docs/cli/logout)

[\- logs](/docs/cli/logs)

[\- project](/docs/cli/project)

[\- promote](/docs/cli/promote)

[\- pull](/docs/cli/pull)

[\- redeploy](/docs/cli/redeploy)

[\- remove](/docs/cli/remove)

[\- rollback](/docs/cli/rollback)

[\- rolling-release](/docs/cli/rolling-release)

[\- switch](/docs/cli/switch)

[\- teams](/docs/cli/teams)

[\- whoami](/docs/cli/whoami)

--------------------------------------------------------------------------------
title: "Telemetry"
description: "Vercel CLI collects telemetry data about general usage."
last_updated: "null"
source: "https://vercel.com/docs/cli/about-telemetry"
--------------------------------------------------------------------------------

# Telemetry

Copy page

Ask AI about this page

Last updated September 24, 2025

Participation in this program is optional, and you may [opt-out](#how-do-i-opt-out-of-vercel-cli-telemetry) if you would prefer not to share any telemetry information.

## [Why is telemetry collected?](#why-is-telemetry-collected)

Vercel CLI Telemetry provides an accurate gauge of Vercel CLI feature usage, pain points, and customization across all users. This data enables tailoring the Vercel CLI to your needs, supports its continued growth relevance, and optimal developer experience, as well as verifies if improvements are enhancing the baseline performance of all applications.

## [What is being collected?](#what-is-being-collected)

Vercel takes privacy and security seriously. Vercel CLI Telemetry tracks general usage information, such as commands and arguments used. Specifically, the following are tracked:

*   Command invoked (`vercel build`, `vercel deploy`, `vercel login`, etc.)
*   Version of the Vercel CLI
*   General machine information (e.g. number of CPUs, macOS/Windows/Linux, whether or not the command was run within CI)

This list is regularly audited to ensure its accuracy.

You can view exactly what is being collected by setting the following environment variable: `VERCEL_TELEMETRY_DEBUG=1`.

When this environment variable is set, data will not be sent to Vercel. The data will only be printed out to the [_stderr_ stream](https://en.wikipedia.org/wiki/Standard_streams), prefixed with `[telemetry]`.

An example telemetry event looks like this:

```
{
  "id": "cf9022fd-e4b3-4f67-bda2-f02dba5b2e40",
  "eventTime": 1728421688109,
  "key": "subcommand:ls",
  "value": "ls",
  "teamId": "team_9Cdf9AE0j9ef09FaSdEU0f0s",
  "sessionId": "e29b9b32-3edd-4599-92d2-f6886af005f6"
}
```

## [What about sensitive data?](#what-about-sensitive-data)

Vercel CLI Telemetry does not collect any metrics which may contain sensitive data, including, but not limited to: environment variables, file paths, contents of files, logs, or serialized JavaScript errors.

For more information about Vercel's privacy practices, please see our [Privacy Notice](https://vercel.com/legal/privacy-policy) and if you have any questions, feel free to reach out to [privacy@vercel.com](mailto:privacy@vercel.com).

## [How do I opt-out of Vercel CLI telemetry?](#how-do-i-opt-out-of-vercel-cli-telemetry)

You may use the [vercel telemetry](/docs/cli/telemetry) command to manage the telemetry collection status. This sets a global configuration value on your computer.

You may opt-out of telemetry data collection by running `vercel telemetry disable`:

terminal

```
vercel telemetry disable
```

You may check the status of telemetry collection at any time by running `vercel telemetry status`:

terminal

```
vercel telemetry status
```

You may re-enable telemetry if you'd like to re-join the program by running the following:

terminal

```
vercel telemetry enable
```

Alternatively, you may opt-out by setting an environment variable: `VERCEL_TELEMETRY_DISABLED=1`. This will only apply for runs where the environment variable is set and will not change your configured telemetry status.

--------------------------------------------------------------------------------
title: "vercel alias"
description: "Learn how to apply custom domain aliases to your Vercel deployments using the vercel alias CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/alias"
--------------------------------------------------------------------------------

# vercel alias

Copy page

Ask AI about this page

Last updated March 17, 2025

The `vercel alias` command allows you to apply [custom domains](/docs/projects/custom-domains) to your deployments.

When a new deployment is created (with our [Git Integration](/docs/git), Vercel CLI, or the [REST API](/docs/rest-api)), the platform will automatically apply any [custom domains](/docs/projects/custom-domains) configured in the project settings.

Any custom domain that doesn't have a [custom preview branch](/docs/domains/working-with-domains/assign-domain-to-a-git-branch) configured (there can only be one Production Branch and it's [configured separately](/docs/git#production-branch) in the project settings) will be applied to production deployments created through any of the available sources.

Custom domains that do have a custom preview branch configured, however, only get applied when using the [Git Integration](/docs/git).

If you're not using the [Git Integration](/docs/git), `vercel alias` is a great solution if you still need to apply custom domains based on Git branches, or other heuristics.

## [Preferred production commands](#preferred-production-commands)

The `vercel alias` command is not the recommended way to promote production deployments to specific domains. Instead, you can use the following commands:

*   [`vercel --prod --skip-domain`](/docs/cli/deploy#prod): Use to skip custom domain assignment when deploying to production and creating a staged deployment
*   [`vercel promote [deployment-id or url]`](/docs/cli/promote): Use to promote your staged deployment to your custom domains
*   [`vercel rollback [deployment-id or url]`](/docs/cli/rollback): Use to alias an earlier production deployment to your custom domains

## [Usage](#usage)

In general, the command allows for assigning custom domains to any deployment.

Make sure to not include the HTTP protocol (e.g. `https://`) for the `[custom-domain]` parameter.

terminal

```
vercel alias set [deployment-url] [custom-domain]
```

Using the `vercel alias` command to assign a custom domain to a deployment.

terminal

```
vercel alias rm [custom-domain]
```

Using the `vercel alias` command to remove a custom domain from a deployment.

terminal

```
vercel alias ls
```

Using the `vercel alias` command to list custom domains that were assigned to deployments.

## [Unique options](#unique-options)

These are options that only apply to the `vercel alias` command.

### [Yes](#yes)

The `--yes` option can be used to bypass the confirmation prompt when removing an alias.

terminal

```
vercel alias rm [custom-domain] --yes
```

Using the `vercel alias rm` command with the `--yes` option.

### [Limit](#limit)

The `--limit` option can be used to specify the maximum number of aliases returned when using `ls`. The default value is `20` and the maximum is `100`.

terminal

```
vercel alias ls --limit 100
```

Using the `vercel alias ls` command with the `--limit` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel alias` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

## [Related guides](#related-guides)

*   [How do I resolve alias related errors on Vercel?](/guides/how-to-resolve-alias-errors-on-vercel)

--------------------------------------------------------------------------------
title: "vercel bisect"
description: "Learn how to perform a binary search on your deployments to help surface issues using the vercel bisect CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/bisect"
--------------------------------------------------------------------------------

# vercel bisect

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel bisect` command can be used to perform a [binary search](https://wikipedia.org/wiki/Binary_search_algorithm) upon a set of deployments in a Vercel Project for the purpose of determining when a bug was introduced.

This is similar to [git bisect](https://git-scm.com/docs/git-bisect) but faster because you don't need to wait to rebuild each commit, as long as there is a corresponding Deployment. The command works by specifing both a _bad_ Deployment and a _good_ Deployment. Then, `vercel bisect` will retrieve all the deployments in between, and step by them one by one. At each step, you will perform your check and specify whether or not the issue you are investigating is present in the Deployment for that step.

Note that if an alias URL is used for either the _good_ or _bad_ deployment, then the URL will be resolved to the current target of the alias URL. So if your Project is currently in promote/rollback state, then the alias URL may not be the newest chronological Deployment.

The good and bad deployments provided to `vercel bisect` must be production deployments.

## [Usage](#usage)

terminal

```
vercel bisect
```

Using the `vercel bisect` command will initiate an interactive prompt where you specify a good deployment, followed by a bad deployment and step through the deployments in between to find the first bad deployment.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel bisect` command.

### [Good](#good)

The `--good` option, shorthand `-g`, can be used to specify the initial "good" deployment from the command line. When this option is present, the prompt will be skipped at the beginning of the bisect session. A production alias URL may be specified for convenience.

terminal

```
vercel bisect --good https://example.com
```

Using the `vercel bisect` command with the `--good` option.

### [Bad](#bad)

The `--bad` option, shorthand `-b`, can be used to specify the "bad" deployment from the command line. When this option is present, the prompt will be skipped at the beginning of the bisect session. A production alias URL may be specified for convenience.

terminal

```
vercel bisect --bad https://example-s93n1nfa.vercel.app
```

Using the `vercel bisect` command with the `--bad` option.

### [Path](#path)

The `--path` option, shorthand `-p`, can be used to specify a subpath of the deployment where the issue occurs. The subpath will be appended to each URL during the bisect session.

terminal

```
vercel bisect --path /blog/first-post
```

Using the `vercel bisect` command with the `--path` option.

### [Open](#open)

The `--open` option, shorthand `-o`, will attempt to automatically open each deployment URL in your browser window for convenience.

terminal

```
vercel bisect --open
```

Using the `vercel bisect` command with the `--open` option.

### [Run](#run)

The `--run` option, shorthand `-r`, provides the ability for the bisect session to be automated using a shell script or command that will be invoked for each deployment URL. The shell script can run an automated test (for example, using the `curl` command to check the exit code) which the bisect command will use to determine whether each URL is good (exit code 0), bad (exit code non-0), or should be skipped (exit code 125).

terminal

```
vercel bisect --run ./test.sh
```

Using the `vercel bisect` command with the `--run` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel bisect` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

## [Related guides](#related-guides)

*   [How to determine which Vercel Deployment introduced an issue?](/guides/how-to-determine-which-vercel-deployment-introduced-an-issue)

--------------------------------------------------------------------------------
title: "vercel blob"
description: "Learn how to interact with Vercel Blob storage using the vercel blob CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/blob"
--------------------------------------------------------------------------------

# vercel blob

Copy page

Ask AI about this page

Last updated August 13, 2025

The `vercel blob` command is used to interact with [Vercel Blob](/docs/storage/vercel-blob) storage, providing functionality to upload, list, delete, and copy files, as well as manage Blob stores.

For more information about Vercel Blob, see the [Vercel Blob documentation](/docs/storage/vercel-blob) and [Vercel Blob SDK reference](/docs/storage/vercel-blob/using-blob-sdk).

## [Usage](#usage)

The `vercel blob` command supports the following operations:

*   [`list`](#list-ls) - List all files in the Blob store
*   [`put`](#put) - Upload a file to the Blob store
*   [`del`](#del) - Delete a file from the Blob store
*   [`copy`](#copy-cp) - Copy a file in the Blob store
*   [`store add`](#store-add) - Add a new Blob store
*   [`store remove`](#store-remove-rm) - Remove a Blob store
*   [`store get`](#store-get) - Get a Blob store

For authentication, the CLI reads the `BLOB_READ_WRITE_TOKEN` value from your env file or you can use the [`--rw-token` option](#rw-token).

### [list (ls)](#list-ls)

terminal

```
vercel blob list
```

Using the `vercel blob list` command to list all files in the Blob store.

### [put](#put)

terminal

```
vercel blob put [path-to-file]
```

Using the `vercel blob put` command to upload a file to the Blob store.

### [del](#del)

terminal

```
vercel blob del [url-or-pathname]
```

Using the `vercel blob del` command to delete a file from the Blob store.

### [copy (cp)](#copy-cp)

terminal

```
vercel blob copy [from-url-or-pathname] [to-pathname]
```

Using the `vercel blob copy` command to copy a file in the Blob store.

### [store add](#store-add)

terminal

```
vercel blob store add [name] [--region <region>]
```

Using the `vercel blob store add` command to add a new Blob store. The default region is set to `iad1` when not specified.

### [store remove (rm)](#store-remove-rm)

terminal

```
vercel blob store remove [store-id]
```

Using the `vercel blob store remove` command to remove a Blob store.

### [store get](#store-get)

terminal

```
vercel blob store get [store-id]
```

Using the `vercel blob store get` command to get a Blob store.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel blob` command.

### [Rw token](#rw-token)

You can use the `--rw-token` option to specify your Blob read-write token.

terminal

```
vercel blob put image.jpg --rw-token [rw-token]
```

Using the `vercel blob put` command with the `--rw-token` option.

### [Limit](#limit)

You can use the `--limit` option to specify the number of results to return per page when using `list`. The default value is `10` and the maximum is `1000`.

terminal

```
vercel blob list --limit 100
```

Using the `vercel blob list` command with the `--limit` option.

### [Cursor](#cursor)

You can use the `--cursor` option to specify the cursor from a previous page to start listing from.

terminal

```
vercel blob list --cursor [cursor-value]
```

Using the `vercel blob list` command with the `--cursor` option.

### [Prefix](#prefix)

You can use the `--prefix` option to filter Blobs by a specific prefix.

terminal

```
vercel blob list --prefix images/
```

Using the `vercel blob list` command with the `--prefix` option.

### [Mode](#mode)

You can use the `--mode` option to filter Blobs by either folded or expanded mode. The default is `expanded`.

terminal

```
vercel blob list --mode folded
```

Using the `vercel blob list` command with the `--mode` option.

### [Add Random Suffix](#add-random-suffix)

You can use the `--add-random-suffix` option to add a random suffix to the file name when using `put` or `copy`.

terminal

```
vercel blob put image.jpg --add-random-suffix
```

Using the `vercel blob put` command with the `--add-random-suffix` option.

### [Pathname](#pathname)

You can use the `--pathname` option to specify the pathname to upload the file to. The default is the filename.

terminal

```
vercel blob put image.jpg --pathname assets/images/hero.jpg
```

Using the `vercel blob put` command with the `--pathname` option.

### [Content Type](#content-type)

You can use the `--content-type` option to overwrite the content-type when using `put` or `copy`. It will be inferred from the file extension if not provided.

terminal

```
vercel blob put data.txt --content-type application/json
```

Using the `vercel blob put` command with the `--content-type` option.

### [Cache Control Max Age](#cache-control-max-age)

You can use the `--cache-control-max-age` option to set the `max-age` of the cache-control header directive when using `put` or `copy`. The default is `2592000` (30 days).

terminal

```
vercel blob put image.jpg --cache-control-max-age 86400
```

Using the `vercel blob put` command with the `--cache-control-max-age` option.

### [Force](#force)

You can use the `--force` option to overwrite the file if it already exists when uploading. The default is `false`.

terminal

```
vercel blob put image.jpg --force
```

Using the `vercel blob put` command with the `--force` option.

### [Multipart](#multipart)

You can use the `--multipart` option to upload the file in multiple small chunks for performance and reliability. The default is `true`.

terminal

```
vercel blob put large-file.zip --multipart false
```

Using the `vercel blob put` command with the `--multipart` option.

### [Region](#region)

You can use the `--region` option to specify the region where your Blob store should be created. The default is `iad1`. This option is only applicable when using the `store add` command.

terminal

```
vercel blob store add my-store --region sfo1
```

Using the `vercel blob store add` command with the `--region` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel blob` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel build"
description: "Learn how to build a Vercel Project locally or in your own CI environment using the vercel build CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/build"
--------------------------------------------------------------------------------

# vercel build

Copy page

Ask AI about this page

Last updated March 12, 2025

The `vercel build` command can be used to build a Vercel Project locally or in your own CI environment. Build artifacts are placed into the `.vercel/output` directory according to the [Build Output API](/docs/build-output-api/v3).

When used in conjunction with the `vercel deploy --prebuilt` command, this allows a Vercel Deployment to be created _without_ sharing the Vercel Project's source code with Vercel.

This command can also be helpful in debugging a Vercel Project by receiving error messages for a failed build locally, or by inspecting the resulting build artifacts to get a better understanding of how Vercel will create the Deployment.

It is recommended to run the `vercel pull` command before invoking `vercel build` to ensure that you have the most recent Project Settings and Environment Variables stored locally.

## [Usage](#usage)

terminal

```
vercel build
```

Using the `vercel build` command to build a Vercel Project.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel build` command.

### [Production](#production)

The `--prod` option can be specified when you want to build the Vercel Project using Production Environment Variables. By default, the Preview Environment Variables will be used.

terminal

```
vercel build --prod
```

Using the `vercel build` command with the `--prod` option.

### [Yes](#yes)

The `--yes` option can be used to bypass the confirmation prompt and automatically pull environment variables and Project Settings if not found locally.

terminal

```
vercel build --yes
```

Using the `vercel build` command with the `--yes` option.

### [target](#target)

Use the `--target` option to define the environment you want to build against. This could be production, preview, or a [custom environment](/docs/deployments/environments#custom-environments).

terminal

```
vercel build --target=staging
```

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel build` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

## [Related guides](#related-guides)

*   [How can I use the Vercel CLI for custom workflows?](/guides/using-vercel-cli-for-custom-workflows)

--------------------------------------------------------------------------------
title: "vercel cache"
description: "Learn how to manage cache for your project using the vercel cache CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/cache"
--------------------------------------------------------------------------------

# vercel cache

Copy page

Ask AI about this page

Last updated October 31, 2025

The `vercel cache` command is used to manage the cache for your project, such as [CDN cache](https://vercel.com/docs/edge-cache) and [Data cache](https://vercel.com/docs/data-cache).

## [Usage](#usage)

terminal

```
vercel cache purge
```

Using the `vercel cache purge` command to purge the CDN cache and Data cache for the current project.

## [Extended Usage](#extended-usage)

terminal

```
vercel cache purge --type cdn
```

Using the `vercel cache purge --type cdn` command to purge the CDN cache for the currenet project.

terminal

```
vercel cache purge --type data
```

Using the `vercel cache purge --type data` command to purge the Data cache for the current project.

terminal

```
vercel cache invalidate --tag blog-posts
```

Using the `vercel cache invalidate --tag blog-posts` command to invalidate the cached content associated with tag "blog-posts" for the current project. Subsequent requests for this cached content will serve STALE and revalidate in the background.

terminal

```
vercel cache dangerously-delete --tag blog-posts
```

Using the `vercel cache dangerously-delete --tag blog-posts` command to dangerously delete the cached content associated with tag "blog-posts" for the current project. Subsequent requests for this cached content will serve MISS and therefore block while revalidating.

terminal

```
vercel cache invalidate --srcimg /api/avatar/1
```

Using the `vercel cache invalidate --srcimg /api/avatar/1` command to invalidate all cached content associated with the source image "/api/avatar/1" for the current project. Subsequent requests for this cached content will serve STALE and revalidate in the background.

terminal

```
vercel cache dangerously-delete --srcimg /api/avatar/1
```

Using the `vercel cache dangerously-delete --srcimg /api/avatar/1` command to dangerously delete all cached content associated with the source image "/api/avatar/1" for the current project. Subsequent requests for this cached content will serve MISS and therefore block while revalidating.

terminal

```
vercel cache dangerously-delete --srcimg /api/avatar/1 --revalidation-deadline-seconds 604800
```

Using the `vercel cache dangerously-delete --srcimg /api/avatar/1 --revalidation-deadline-seconds 604800` command to dangerously delete all cached content associated with the source image "/api/avatar/1" for the current project if not accessed in the next 604800 seconds (7 days).

## [Unique Options](#unique-options)

These are options that only apply to the `vercel cache` command.

### [tag](#tag)

The `--tag` option specifies which tag to invalidate or delete from the cache. You can provide a single tag or multiple comma-separated tags. This option works with both `invalidate` and `dangerously-delete` subcommands.

terminal

```
vercel cache invalidate --tag blog-posts,user-profiles,homepage
```

Using the `vercel cache invalidate` command with multiple tags.

### [srcimg](#srcimg)

The `--srcimg` option specifies a source image path to invalidate or delete from the cache. This invalidates or deletes all cached variants of the source image. This option works with both `invalidate` and `dangerously-delete` subcommands.

You can't use both `--tag` and `--srcimg` options together. Choose one based on whether you're invalidating cached content by tag or by source image.

terminal

```
vercel cache invalidate --srcimg /api/avatar/1
```

Using the `vercel cache invalidate` command with a source image path.

### [revalidation-deadline-seconds](#revalidation-deadline-seconds)

The `--revalidation-deadline-seconds` option specifies the revalidation deadline in seconds. When used with `dangerously-delete`, cached content will only be deleted if it hasn't been accessed within the specified time period.

terminal

```
vercel cache dangerously-delete --tag blog-posts --revalidation-deadline-seconds 3600
```

Using the `vercel cache dangerously-delete` command with a 1-hour (3600 seconds) revalidation deadline.

### [Yes](#yes)

The `--yes` option can be used to bypass the confirmation prompt when purging the cache or dangerously deleting cached content.

terminal

```
vercel cache purge --yes
```

Using the `vercel cache purge` command with the `--yes` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel cache` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel certs"
description: "Learn how to manage certificates for your domains using the vercel certs CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/certs"
--------------------------------------------------------------------------------

# vercel certs

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel certs` command is used to manage certificates for domains, providing functionality to list, issue, and remove them. Vercel manages certificates for domains automatically.

## [Usage](#usage)

terminal

```
vercel certs ls
```

Using the `vercel certs` command to list all certificates under the current scope.

## [Extended Usage](#extended-usage)

terminal

```
vercel certs issue [domain1, domain2, domain3]
```

Using the `vercel certs` command to issue certificates for multiple domains.

terminal

```
vercel certs rm [certificate-id]
```

Using the `vercel certs` command to remove a certificate by ID.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel certs` command.

### [Challenge Only](#challenge-only)

The `--challenge-only` option can be used to only show the challenges needed to issue a certificate.

terminal

```
vercel certs issue foo.com --challenge-only
```

Using the `vercel certs` command with the `--challenge-only` option.

### [Limit](#limit)

The `--limit` option can be used to specify the maximum number of certs returned when using `ls`. The default value is `20` and the maximum is `100`.

terminal

```
vercel certs ls --limit 100
```

Using the `vercel certs ls` command with the `--limit` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel certs` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel curl"
description: "Learn how to make HTTP requests to your Vercel deployments with automatic deployment protection bypass using the vercel curl CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/curl"
--------------------------------------------------------------------------------

# vercel curl

Copy page

Ask AI about this page

Last updated November 7, 2025

The `vercel curl` command is currently in beta. Features and behavior may change.

The `vercel curl` command works like `curl`, but automatically handles deployment protection bypass tokens for you. When your project has [Deployment Protection](/docs/security/deployment-protection) enabled, this command lets you test protected deployments without manually managing bypass secrets.

The command runs the system `curl` command with the same arguments you provide, but adds an [`x-vercel-protection-bypass`](/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation#using-protection-bypass-for-automation) header with a valid token. This makes it simple to test API endpoints, check responses, or debug issues on protected deployments.

This command is available in Vercel CLI v48.8.0 and later. If you're using an older version, see [Updating Vercel CLI](/docs/cli#updating-vercel-cli).

## [Usage](#usage)

terminal

```
vercel curl [path]
```

Using the `vercel curl` command to make an HTTP request to a deployment.

## [Examples](#examples)

### [Basic request](#basic-request)

Make a GET request to your production deployment:

terminal

```
vercel curl /api/hello
```

Making a GET request to the `/api/hello` endpoint on your production deployment.

### [POST request with data](#post-request-with-data)

Send a POST request with JSON data:

terminal

```
vercel curl /api/users -X POST -H "Content-Type: application/json" -d '{"name":"John"}'
```

Making a POST request with JSON data to create a new user.

### [Request specific deployment](#request-specific-deployment)

Test a specific deployment by its URL:

terminal

```
vercel curl /api/status --deployment https://my-app-abc123.vercel.app
```

Making a request to a specific deployment instead of the production deployment.

### [Verbose output](#verbose-output)

See detailed request information:

terminal

```
vercel curl /api/data -v
```

Using curl's `-v` flag for verbose output, which shows headers and connection details.

## [How it works](#how-it-works)

When you run `vercel curl`:

1.  The CLI finds your linked project (or you can specify one with [`--scope`](/docs/cli/global-options#scope))
2.  It gets the latest production deployment URL (or uses the deployment you specified)
3.  It retrieves or generates a deployment protection bypass token
4.  It runs the system `curl` command with the bypass token in the `x-vercel-protection-bypass` header

The command requires `curl` to be installed on your system.

## [Unique options](#unique-options)

These are options that only apply to the `vercel curl` command.

### [Deployment](#deployment)

The `--deployment` option, shorthand `-d`, lets you specify a deployment URL to request instead of using the production deployment.

terminal

```
vercel curl /api/hello --deployment https://my-app-abc123.vercel.app
```

Using the `--deployment` option to target a specific deployment.

### [Protection Bypass](#protection-bypass)

The `--protection-bypass` option, shorthand `-b`, lets you provide your own deployment protection bypass secret instead of automatically generating one. This is useful when you already have a bypass secret configured.

terminal

```
vercel curl /api/hello --protection-bypass your-secret-here
```

Using the `--protection-bypass` option with a manual secret.

You can also use the [`VERCEL_AUTOMATION_BYPASS_SECRET`](/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation#using-protection-bypass-for-automation) environment variable:

terminal

```
export VERCEL_AUTOMATION_BYPASS_SECRET=your-secret-here
vercel curl /api/hello
```

Setting the bypass secret as an environment variable.

## [Troubleshooting](#troubleshooting)

### [curl command not found](#curl-command-not-found)

Make sure `curl` is installed on your system:

terminal

```
# macOS (using Homebrew)
brew install curl
 
# Ubuntu/Debian
sudo apt-get install curl
 
# Windows (using Chocolatey)
choco install curl
```

Installing curl on different operating systems.

### [No deployment found for the project](#no-deployment-found-for-the-project)

Make sure you're in a directory with a linked Vercel project and that the project has at least one deployment:

terminal

```
# Link your project
vercel link
 
# Deploy your project
vercel deploy
```

Linking your project and creating a deployment.

### [Failed to get deployment protection bypass token](#failed-to-get-deployment-protection-bypass-token)

If automatic token creation fails, you can create a bypass secret manually in the Vercel Dashboard:

1.  Go to your project's Settings → Deployment Protection
2.  Find "Protection Bypass for Automation"
3.  Click "Create" or "Generate" to create a new secret
4.  Copy the generated secret
5.  Use it with the `--protection-bypass` flag or [`VERCEL_AUTOMATION_BYPASS_SECRET`](/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation#using-protection-bypass-for-automation) environment variable

### [No deployment found for ID](#no-deployment-found-for-id)

When using `--deployment`, verify that:

*   The deployment ID or URL is correct
*   The deployment belongs to your linked project
*   The deployment hasn't been deleted

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel curl` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

## [Related](#related)

*   [Deployment Protection](/docs/security/deployment-protection)
*   [vercel deploy](/docs/cli/deploy)
*   [vercel inspect](/docs/cli/inspect)

--------------------------------------------------------------------------------
title: "vercel deploy"
description: "Learn how to deploy your Vercel projects using the vercel deploy CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/deploy"
--------------------------------------------------------------------------------

# vercel deploy

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel deploy` command deploys Vercel projects, executable from the project's root directory or by specifying a path. You can omit 'deploy' in `vercel deploy`, as `vercel` is the only command that operates without a subcommand. This document will use 'vercel' to refer to `vercel deploy`.

## [Usage](#usage)

terminal

```
vercel
```

Using the `vercel` command from the root of a Vercel project directory.

## [Extended usage](#extended-usage)

terminal

```
vercel --cwd [path-to-project]
```

Using the `vercel` command and supplying a path to the root directory of the Vercel project.

terminal

```
vercel deploy --prebuilt
```

Using the `vercel` command to deploy a prebuilt Vercel project, typically with `vercel build`. See [vercel build](/docs/cli/build) and [Build Output API](/docs/build-output-api/v3) for more details.

## [Standard output usage](#standard-output-usage)

When deploying, `stdout` is always the Deployment URL.

terminal

```
vercel > deployment-url.txt
```

Using the `vercel` command to deploy and write `stdout` to a text file. When deploying, `stdout` is always the Deployment URL.

### [Deploying to a custom domain](#deploying-to-a-custom-domain)

In the following example, you create a bash script that you include in your CI/CD workflow. The goal is to have all preview deployments be aliased to a custom domain so that developers can bookmark the preview deployment URL. Note that you may need to [define the scope](/docs/cli/global-options#scope) when using `vercel alias`

deployDomain.sh

```
# save stdout and stderr to files
vercel deploy >deployment-url.txt 2>error.txt
 
# check the exit code
code=$?
if [ $code -eq 0 ]; then
    # Now you can use the deployment url from stdout for the next step of your workflow
    deploymentUrl=`cat deployment-url.txt`
    vercel alias $deploymentUrl my-custom-domain.com
else
    # Handle the error
    errorMessage=`cat error.txt`
    echo "There was an error: $errorMessage"
fi
```

The script deploys your project and assigns the deployment URL saved in `stdout` to the custom domain using `vercel alias`.

## [Standard error usage](#standard-error-usage)

If you need to check for errors when the command is executed such as in a CI/CD workflow, use `stderr`. If the exit code is anything other than `0`, an error has occurred. The following example demonstrates a script that checks if the exit code is not equal to 0:

checkDeploy.sh

```
# save stdout and stderr to files
vercel deploy >deployment-url.txt 2>error.txt
 
# check the exit code
code=$?
if [ $code -eq 0 ]; then
    # Now you can use the deployment url from stdout for the next step of your workflow
    deploymentUrl=`cat deployment-url.txt`
    echo $deploymentUrl
else
    # Handle the error
    errorMessage=`cat error.txt`
    echo "There was an error: $errorMessage"
fi
```

## [Unique options](#unique-options)

These are options that only apply to the `vercel` command.

### [Prebuilt](#prebuilt)

The `--prebuilt` option can be used to upload and deploy the results of a previous `vc build` execution located in the .vercel/output directory. See [vercel build](/docs/cli/build) and [Build Output API](/docs/build-output-api/v3) for more details.

#### [When not to use --prebuilt](#when-not-to-use---prebuilt)

When using the `--prebuilt` flag, no deployment ID will be made available for supported frameworks (like Next.js) to use, which means [Skew Protection](/docs/skew-protection) will not be enabled. Additionally, [System Environment Variables](/docs/environment-variables/system-environment-variables) will be missing at build time, so frameworks that rely on them at build time may not function correctly. If you need Skew Protection or System Environment Variables, do not use the `--prebuilt` flag or use Git-based deployments.

terminal

```
vercel --prebuilt
```

You should also consider using the [archive](/docs/cli/deploy#archive) option to minimize the number of files uploaded and avoid hitting upload limits:

terminal

```
# Build the project locally
vercel build
 
# Deploy the pre-built project, archiving it as a .tgz file
vercel deploy --prebuilt --archive=tgz
```

This example uses the `vercel build` command to build your project locally. It then uses the `--prebuilt` and `--archive=tgz` options on the `deploy` command to compress the build output and then deploy it.

### [Build env](#build-env)

The `--build-env` option, shorthand `-b`, can be used to provide environment variables to the [build step](/docs/deployments/configure-a-build).

terminal

```
vercel --build-env KEY1=value1 --build-env KEY2=value2
```

Using the `vercel` command with the `--build-env` option.

### [Yes](#yes)

The `--yes` option can be used to skip questions you are asked when setting up a new Vercel project. The questions will be answered with the provided defaults, inferred from `vercel.json` and the folder name.

terminal

```
vercel --yes
```

Using the `vercel` command with the `--yes` option.

### [Env](#env)

The `--env` option, shorthand `-e`, can be used to provide [environment variables](/docs/environment-variables) at runtime.

terminal

```
vercel --env KEY1=value1 --env KEY2=value2
```

Using the `vercel` command with the `--env` option.

### [Name](#name)

The `--name` option has been deprecated in favor of [Vercel project linking](/docs/cli/project-linking), which allows you to link a Vercel project to your local codebase when you run `vercel`.

The `--name` option, shorthand `-n`, can be used to provide a Vercel project name for a deployment.

terminal

```
vercel --name foo
```

Using the `vercel` command with the `--name` option.

### [Prod](#prod)

The `--prod` option can be used to create a deployment for a production domain specified in the Vercel project dashboard.

terminal

```
vercel --prod
```

Using the `vercel` command with the `--prod` option.

### [Skip Domain](#skip-domain)

This CLI option will override the [Auto-assign Custom Production Domains](/docs/deployments/promoting-a-deployment#staging-and-promoting-a-production-deployment) project setting.

Must be used with [`--prod`](#prod). The `--skip-domain` option will disable the automatic promotion (aliasing) of the relevant domains to a new production deployment. You can use [`vercel promote`](/docs/cli/promote) to complete the domain-assignment process later.

terminal

```
vercel --prod --skip-domain
```

Using the `vercel` command with the `--skip-domain` option.

### [Public](#public)

The `--public` option can be used to ensures the source code is publicly available at the `/_src` path.

terminal

```
vercel --public
```

Using the `vercel` command with the `--public` option.

### [Regions](#regions)

The `--regions` option can be used to specify which [regions](/docs/regions) the deployments [Vercel functions](/docs/functions) should run in.

terminal

```
vercel --regions sfo1
```

Using the `vercel` command with the `--regions` option.

### [No wait](#no-wait)

The `--no-wait` option does not wait for a deployment to finish before exiting from the `deploy` command.

terminal

```
vercel --no-wait
```

### [Force](#force)

The `--force` option, shorthand `-f`, is used to force a new deployment without the [build cache](/docs/deployments/troubleshoot-a-build#what-is-cached).

terminal

```
vercel --force
```

### [With cache](#with-cache)

The `--with-cache` option is used to retain the [build cache](/docs/deployments/troubleshoot-a-build#what-is-cached) when using `--force`.

terminal

```
vercel --force --with-cache
```

### [Archive](#archive)

The `--archive` option compresses the deployment code into one or more files before uploading it. This option should be used when deployments include thousands of files to avoid rate limits such as the [files limit](https://vercel.com/docs/limits#files).

In some cases, `--archive` makes deployments slower. This happens because the caching of source files to optimize file uploads in future deployments is negated when source files are archived.

terminal

```
vercel deploy --archive=tgz
```

### [Logs](#logs)

The `--logs` option, shorthand `-l`, also prints the build logs.

terminal

```
vercel deploy --logs
```

Using the `vercel deploy` command with the `--logs` option, to view logs from the build process.

### [Meta](#meta)

The `--meta` option, shorthand `-m`, is used to add metadata to the deployment.

terminal

```
vercel deploy --meta KEY1=value1
```

Deployments can be filtered using this data with [`vercel list --meta`](/docs/cli/list#meta).

### [target](#target)

Use the `--target` option to define the environment you want to deploy to. This could be production, preview, or a [custom environment](/docs/deployments/environments#custom-environments).

terminal

```
vercel deploy --target=staging
```

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel deploy` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "Deploying Projects from Vercel CLI"
description: "Learn how to deploy your Vercel Projects from Vercel CLI using the vercel or vercel deploy commands."
last_updated: "null"
source: "https://vercel.com/docs/cli/deploying-from-cli"
--------------------------------------------------------------------------------

# Deploying Projects from Vercel CLI

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Deploying from source](#deploying-from-source)

The `vercel` command is used to [deploy](/docs/cli/deploy) Vercel Projects and can be used from either the root of the Vercel Project directory or by providing a path.

terminal

```
vercel
```

Deploys the current Vercel project, when run from the Vercel Project root.

You can alternatively use the [`vercel deploy` command](/docs/cli/deploy) for the same effect, if you want to be more explicit.

terminal

```
vercel [path-to-project]
```

Deploys the Vercel project found at the provided path, when it's a Vercel Project root.

When deploying, stdout is always the Deployment URL.

terminal

```
vercel > deployment-url.txt
```

Writes the Deployment URL output from the `deploy` command to a text file.

### [Relevant commands](#relevant-commands)

*   [deploy](/docs/cli/deploy)

## [Deploying a staged production build](#deploying-a-staged-production-build)

By default, when you promote a deployment to production, your domain will point to that deployment. If you want to create a production deployment without assigning it to your domain, for example to avoid sending all of your traffic to it, you can:

1.  Turn off the auto-assignment of domains for the current production deployment:

terminal

```
vercel --prod --skip-domain
```

1.  When you are ready, manually promote the staged deployment to production:

terminal

```
vercel promote [deployment-id or url]
```

### [Relevant commands](#relevant-commands)

*   [promote](/docs/cli/promote)
*   [deploy](/docs/cli/deploy)

## [Deploying from local build (prebuilt)](#deploying-from-local-build-prebuilt)

You can build Vercel projects locally to inspect the build outputs before they are [deployed](/docs/cli/deploy). This is a great option for producing builds for Vercel that do not share your source code with the platform.

It's also useful for debugging build outputs.

terminal

```
vercel build
```

Using the `vercel` command to deploy and write stdout to a text file.

This produces `.vercel/output` in the [Build Output API](/docs/build-output-api/v3) format. You can review the output, then [deploy](/docs/cli/deploy) with:

terminal

```
vercel deploy --prebuilt
```

Deploy the build outputs in `.vercel/output` produced by `vercel build`.

Review the [When not to use --prebuilt](/docs/cli/deploy#when-not-to-use---prebuilt) section to understand when you should not use the `--prebuilt` flag.

See more details at [Build Output API](/docs/build-output-api/v3).

### [Relevant commands](#relevant-commands)

*   [build](/docs/cli/build)
*   [deploy](/docs/cli/deploy)

--------------------------------------------------------------------------------
title: "vercel dev"
description: "Learn how to replicate the Vercel deployment environment locally and test your Vercel Project before deploying using the vercel dev CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/dev"
--------------------------------------------------------------------------------

# vercel dev

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel dev` command is used to replicate the Vercel deployment environment locally, allowing you to test your [Vercel Functions](/docs/functions) and [Middleware](/docs/routing-middleware) without requiring you to deploy each time a change is made.

If the [Development Command](/docs/deployments/configure-a-build#development-command) is configured in your Project Settings, it will affect the behavior of `vercel dev` for everyone on that team.

Before running `vercel dev`, make sure to install your dependencies by running `npm install`.

## [When to Use This Command](#when-to-use-this-command)

If you're using a framework and your framework's [Development Command](/docs/deployments/configure-a-build#development-command) already provides all the features you need, we do not recommend using `vercel dev`.

For example, [Next.js](/docs/frameworks/nextjs)'s Development Command (`next dev`) provides native support for Functions, [redirects](/docs/redirects#configuration-redirects), rewrites, headers and more.

## [Usage](#usage)

terminal

```
vercel dev
```

Using the `vercel dev` command from the root of a Vercel Project directory.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel dev` command.

### [Listen](#listen)

The `--listen` option, shorthand `-l`, can be used to specify which port `vercel dev` runs on.

terminal

```
vercel dev --listen 5005
```

Using the `vercel dev` command with the `--listen` option.

### [Yes](#yes)

The `--yes` option can be used to skip questions you are asked when setting up a new Vercel Project. The questions will be answered with the default scope and current directory for the Vercel Project name and location.

terminal

```
vercel dev --yes
```

Using the `vercel dev` command with the `--yes` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel dev` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel dns"
description: "Learn how to manage your DNS records for your domains using the vercel dns CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/dns"
--------------------------------------------------------------------------------

# vercel dns

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel dns` command is used to manage DNS record for domains, providing functionality to list, add, remove, and import records.

When adding DNS records, please wait up to 24 hours for new records to propagate.

## [Usage](#usage)

terminal

```
vercel dns ls
```

Using the `vercel dns` command to list all DNS records under the current scope.

## [Extended Usage](#extended-usage)

terminal

```
vercel dns add [domain] [subdomain] [A || AAAA || ALIAS || CNAME || TXT] [value]
```

Using the `vercel dns` command to add an A record for a subdomain.

terminal

```
vercel dns add [domain] '@' MX [record-value] [priority]
```

Using the `vercel dns` command to add an MX record for a domain.

terminal

```
vercel dns add [domain] [name] SRV [priority] [weight] [port] [target]
```

Using the `vercel dns` command to add an SRV record for a domain.

terminal

```
vercel dns add [domain] [name] CAA '[flags] [tag] "[value]"'
```

Using the `vercel dns` command to add a CAA record for a domain.

terminal

```
vercel dns rm [record-id]
```

Using the `vercel dns` command to remove a record for a domain.

terminal

```
vercel dns import [domain] [path-to-zonefile]
```

Using the `vercel dns` command to import a zonefile for a domain.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel dns` command.

### [Limit](#limit)

The `--limit` option can be used to specify the maximum number of dns records returned when using `ls`. The default value is `20` and the maximum is `100`.

terminal

```
vercel dns ls --limit 100
```

Using the `vercel dns ls` command with the `--limit` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel dns` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel domains"
description: "Learn how to buy, sell, transfer, and manage your domains using the vercel domains CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/domains"
--------------------------------------------------------------------------------

# vercel domains

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel domains` command is used to manage domains under the current scope, providing functionality to list, inspect, add, remove, purchase, move, transfer-in, and verify domains.

You can manage domains with further options and greater control under a Vercel Project's Domains tab from the Vercel Dashboard.

## [Usage](#usage)

terminal

```
vercel domains ls
```

Using the `vercel domains` command to list all domains under the current scope.

## [Extended Usage](#extended-usage)

terminal

```
vercel domains inspect [domain]
```

Using the `vercel domains` command to retrieve information about a specific domain.

terminal

```
vercel domains add [domain] [project]
```

Using the `vercel domains` command to add a domain to the current scope or a Vercel Project.

terminal

```
vercel domains rm [domain]
```

Using the `vercel domains` command to remove a domain from the current scope.

terminal

```
vercel domains buy [domain]
```

Using the `vercel domains` command to buy a domain for the current scope.

terminal

```
vercel domains move [domain] [scope-name]
```

Using the `vercel domains` command to move a domain to another scope.

terminal

```
vercel domains transfer-in [domain]
```

Using the `vercel domains` command to transfer in a domain to the current scope.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel domains` command.

### [Yes](#yes)

The `--yes` option can be used to bypass the confirmation prompt when removing a domain.

terminal

```
vercel domains rm [domain] --yes
```

Using the `vercel domains rm` command with the `--yes` option.

### [Limit](#limit)

The `--limit` option can be used to specify the maximum number of domains returned when using `ls`. The default value to `20` and the maximum is `100`.

terminal

```
vercel domains ls --limit 100
```

Using the `vercel domains ls` command with the `--limit` option.

### [Force](#force)

The `--force` option forces a domain on a project, removing it from an existing one.

terminal

```
vercel domains add my-domain.com my-project --force
```

Using the `vercel domains add` command with the `--force` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel domains` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel env"
description: "Learn how to manage your environment variables in your Vercel Projects using the vercel env CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/env"
--------------------------------------------------------------------------------

# vercel env

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel env` command is used to manage [Environment Variables](/docs/environment-variables) of a Project, providing functionality to list, add, remove, and export.

To leverage environment variables in local tools (like `next dev` or `gatsby dev`) that want them in a file (like `.env`), run `vercel env pull <file>`. This will export your Project's environment variables to that file. After updating environment variables on Vercel (through the dashboard, `vercel env add`, or `vercel env rm`), you will have to run `vercel env pull <file>` again to get the updated values.

### [Exporting Development Environment Variables](#exporting-development-environment-variables)

Some frameworks make use of environment variables during local development through CLI commands like `next dev` or `gatsby dev`. The `vercel env pull` sub-command will export development environment variables to a local `.env` file or a different file of your choice.

terminal

```
vercel env pull [file]
```

To override environment variable values temporarily, use:

terminal

```
MY_ENV_VAR="temporary value" next dev
```

  

If you are using [`vercel build`](/docs/cli/build) or [`vercel dev`](/docs/cli/dev), you should use [`vercel pull`](/docs/cli/pull) instead. Those commands operate on a local copy of environment variables and Project settings that are saved under `.vercel/`, which `vercel pull` provides.

## [Usage](#usage)

terminal

```
vercel env ls
```

Using the `vercel env` command to list all Environment Variables in a Vercel Project.

terminal

```
vercel env add
```

Using the `vercel env` command to add an Environment Variable to a Vercel Project.

terminal

```
vercel env rm
```

Using the `vercel env` command to remove an Environment Variable from a Vercel Project.

## [Extended Usage](#extended-usage)

terminal

```
vercel env ls [environment]
```

Using the `vercel env` command to list Environment Variables for a specific Environment in a Vercel Project.

terminal

```
vercel env ls [environment] [gitbranch]
```

Using the `vercel env` command to list Environment Variables for a specific Environment and Git branch.

terminal

```
vercel env add [name]
```

Using the `vercel env` command to add an Environment Variable to all Environments to a Vercel Project.

terminal

```
vercel env add [name] [environment]
```

Using the `vercel env` command to add an Environment Variable for a specific Environment to a Vercel Project.

terminal

```
vercel env add [name] [environment] [gitbranch]
```

Using the `vercel env` command to add an Environment Variable to a specific Git branch.

terminal

```
vercel env add [name] [environment] < [file]
```

Using the `vercel env` command to add an Environment Variable to a Vercel Project using a local file's content as the value.

terminal

```
echo [value] | vercel env add [name] [environment]
```

Using the `echo` command to generate the value of the Environment Variable and piping that value into the `vercel dev` command. Warning: this will save the value in bash history, so this is not recommend for secrets.

terminal

```
vercel env add [name] [environment] [gitbranch] < [file]
```

Using the `vercel env` command to add an Environment Variable with Git branch to a Vercel Project using a local file's content as the value.

terminal

```
vercel env rm [name] [environment]
```

Using the `vercel env` command to remove an Environment Variable from a Vercel Project.

terminal

```
vercel env pull [file]
```

Using the `vercel env` command to download Development Environment Variables from the cloud and write to a specific file.

terminal

```
vercel env pull --environment=preview
```

Using the `vercel env` command to download Preview Environment Variables from the cloud and write to the `.env.local` file.

terminal

```
vercel env pull --environment=preview --git-branch=feature-branch
```

Using the `vercel env` command to download "feature-branch" Environment Variables from the cloud and write to the `.env.local` file.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel env` command.

### [Yes](#yes)

The `--yes` option can be used to bypass the confirmation prompt when overwriting an environment file or removing an environment variable.

terminal

```
vercel env pull --yes
```

Using the `vercel env pull` command with the `--yes` option to overwrite an existing environment file.

terminal

```
vercel env rm [name] --yes
```

Using the `vercel env rm` command with the `--yes` option to skip the remove confirmation.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel env` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel git"
description: "Learn how to manage your Git provider connections using the vercel git CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/git"
--------------------------------------------------------------------------------

# vercel git

Copy page

Ask AI about this page

Last updated March 4, 2025

The `vercel git` command is used to manage a Git provider repository for a Vercel Project, enabling deployments to Vercel through Git.

When run, Vercel CLI searches for a local `.git` config file containing at least one remote URL. If found, you can connect it to the Vercel Project linked to your directory.

[Learn more about using Git with Vercel](/docs/git).

## [Usage](#usage)

terminal

```
vercel git connect
```

Using the `vercel git` command to connect a Git provider repository from your local Git config to a Vercel Project.

terminal

```
vercel git disconnect
```

Using the `vercel git` command to disconnect a connected Git provider repository from a Vercel Project.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel git` command.

### [Yes](#yes)

The `--yes` option can be used to skip connect confirmation.

terminal

```
vercel git connect --yes
```

Using the `vercel git connect` command with the `--yes` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel git` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "Vercel CLI Global Options"
description: "Global options are commonly available to use with multiple Vercel CLI commands. Learn about Vercel CLI's global options here."
last_updated: "null"
source: "https://vercel.com/docs/cli/global-options"
--------------------------------------------------------------------------------

# Vercel CLI Global Options

Copy page

Ask AI about this page

Last updated March 4, 2025

Global options are commonly available to use with multiple Vercel CLI commands.

## [Current Working Directory](#current-working-directory)

The `--cwd` option can be used to provide a working directory (that can be different from the current directory) when running Vercel CLI commands.

This option can be a relative or absolute path.

terminal

```
vercel --cwd ~/path-to/project
```

Using the `vercel` command with the `--cwd` option.

## [Debug](#debug)

The `--debug` option, shorthand `-d`, can be used to provide a more verbose output when running Vercel CLI commands.

terminal

```
vercel --debug
```

Using the `vercel` command with the `--debug` option.

## [Global config](#global-config)

The `--global-config` option, shorthand `-Q`, can be used set the path to the [global configuration directory](/docs/project-configuration/global-configuration).

terminal

```
vercel --global-config /path-to/global-config-directory
```

Using the `vercel` command with the `--global-config` option.

## [Help](#help)

The `--help` option, shorthand `-h`, can be used to display more information about [Vercel CLI](/cli) commands.

terminal

```
vercel --help
```

Using the `vercel` command with the `--help` option.

terminal

```
vercel alias --help
```

Using the `vercel alias` command with the `--help` option.

## [Local config](#local-config)

The `--local-config` option, shorthand `-A`, can be used to set the path to a local `vercel.json` file.

terminal

```
vercel --local-config /path-to/vercel.json
```

Using the `vercel` command with the `--local-config` option.

## [Scope](#scope)

The `--scope` option, shorthand `-S`, can be used to execute Vercel CLI commands from a scope that’s not currently active.

terminal

```
vercel --scope my-team-slug
```

Using the `vercel` command with the `--scope` option.

## [Token](#token)

The `--token` option, shorthand `-t`, can be used to execute Vercel CLI commands with an [authorization token](/account/tokens).

terminal

```
vercel --token iZJb2oftmY4ab12HBzyBXMkp
```

Using the `vercel` command with the `--token` option.

## [No Color](#no-color)

The `--no-color` option, or `NO_COLOR=1` environment variable, can be used to execute Vercel CLI commands with no color or emoji output. This respects the [NO\_COLOR standard](https://no-color.org).

terminal

```
vercel login --no-color
```

Using the `vercel` command with the `--no-color` option.

--------------------------------------------------------------------------------
title: "vercel help"
description: "Learn how to use the vercel help CLI command to get information about all available Vercel CLI commands."
last_updated: "null"
source: "https://vercel.com/docs/cli/help"
--------------------------------------------------------------------------------

# vercel help

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel help` command generates a list of all available Vercel CLI commands and [options](/docs/cli/global-options) in the terminal. When combined with a second argument - a valid Vercel CLI command - it outputs more detailed information about that command.

Alternatively, the [`--help` global option](/docs/cli/global-options#help) can be added to commands to get help information about that command.

## [Usage](#usage)

terminal

```
vercel help
```

Using the `vercel help` command to generate a list of Vercel CLI commands and options.

## [Extended Usage](#extended-usage)

terminal

```
vercel help [command]
```

Using the `vercel help` command to generate detailed information about a specific Vercel CLI command.

--------------------------------------------------------------------------------
title: "vercel init"
description: "Learn how to initialize Vercel supported framework examples locally using the vercel init CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/init"
--------------------------------------------------------------------------------

# vercel init

Copy page

Ask AI about this page

Last updated September 10, 2025

The `vercel init` command is used to initialize [Vercel supported framework](/docs/frameworks) examples locally from the examples found in the [Vercel examples repository](https://github.com/vercel/vercel/tree/main/examples).

## [Usage](#usage)

terminal

```
vercel init
```

Using the `vercel init` command to initialize a Vercel supported framework example locally. You will be prompted with a list of supported frameworks to choose from.

## [Extended Usage](#extended-usage)

terminal

```
vercel init [framework-name]
```

Using the `vercel init` command to initialize a specific [framework](/docs/frameworks) example from the Vercel examples repository locally.

terminal

```
vercel init [framework-name] [new-local-directory-name]
```

Using the `vercel init` command to initialize a specific Vercel framework example locally and rename the directory.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel env` command.

### [Force](#force)

The `--force` option, shorthand `-f`, is used to forcibly replace an existing local directory.

terminal

```
vercel init --force
```

Using the `vercel init` command with the `--force` option.

terminal

```
vercel init gatsby my-project-directory --force
```

Using the `vercel init` command with the `--force` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel init` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel inspect"
description: "Learn how to retrieve information about your Vercel deployments using the vercel inspect CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/inspect"
--------------------------------------------------------------------------------

# vercel inspect

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel inspect` command is used to retrieve information about a deployment referenced either by its deployment URL or ID.

You can use this command to view either a deployment's information or its [build logs](/docs/cli/inspect#logs).

## [Usage](#usage)

terminal

```
vercel inspect [deployment-id or url]
```

Using the `vercel inspect` command to retrieve information about a specific deployment.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel inspect` command.

### [Timeout](#timeout)

The `--timeout` option sets the time to wait for deployment completion. It defaults to 3 minutes.

Any valid time string for the [ms](https://www.npmjs.com/package/ms) package can be used.

terminal

```
vercel inspect https://example-app-6vd6bhoqt.vercel.app --timeout=5m
```

Using the `vercel inspect` command with the `--timeout` option.

### [Wait](#wait)

The `--wait` option will block the CLI until the specified deployment has completed.

terminal

```
vercel inspect https://example-app-6vd6bhoqt.vercel.app --wait
```

Using the `vercel inspect` command with the `--wait` option.

### [Logs](#logs)

The `--logs` option, shorthand `-l`, prints the build logs instead of the deployment information.

terminal

```
vercel inspect https://example-app-6vd6bhoqt.vercel.app --logs
```

Using the `vercel inspect` command with the `--logs` option, to view available build logs.

If the deployment is queued or canceled, there will be no logs to display.

If the deployment is building, you may want to specify `--wait` option. The command will wait for build completion, and will display build logs as they are emitted.

terminal

```
vercel inspect https://example-app-6vd6bhoqt.vercel.app --logs --wait
```

Using the `vercel inspect` command with the `--logs` and `--wait` options, to view all build logs until the deployement is ready.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel inspect` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel install"
description: "Learn how to install native integrations with the vercel install CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/install"
--------------------------------------------------------------------------------

# vercel install

Copy page

Ask AI about this page

Last updated February 26, 2025

The `vercel install` command is used to install a [native integration](/docs/integrations/create-integration#native-integrations) with the option of [adding a product](/docs/integrations/marketplace-product#create-your-product) to an existing installation.

If you have not installed the integration before, you will asked to open the Vercel dashboard and accept the Vercel Marketplace terms. You can then decide to continue and add a product through the dashboard or cancel the product addition step.

If you have an existing installation with the provider, you can add a product directly from the CLI by answering a series of questions that reflect the choices you would make in the dashboard.

## [Usage](#usage)

terminal

```
vercel install acme
```

Using the `vercel install` command install the ACME integration.

You can get the value of `acme` by looking at the slug of the integration provider from the marketplace URL. For example, for `https://vercel.com/marketplace/gel`, `acme` is `gel`.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel install` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel integration"
description: "Learn how to perform key integration tasks using the vercel integration CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/integration"
--------------------------------------------------------------------------------

# vercel integration

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel integration` command needs to be used with one of the following actions:

*   `vercel integration add`
*   `vercel integration open`
*   `vercel integration list`
*   `vercel integration remove`

For the `integration-name` in all the commands below, use the [URL slug](/docs/integrations/create-integration/submit-integration#url-slug) value of the integration.

## [vercel integration add](#vercel-integration-add)

The `vercel integration add` command initializes the setup wizard for creating an integration resource. This command is used when you want to add a new resource from one of your installed integrations. This functionality is the same as `vercel install [integration-name]`.

If you have not installed the integration for the resource or accepted the terms & conditions of the integration through the web UI, this command will open your browser to the Vercel dashboard and start the installation flow for that integration.

terminal

```
vercel integration add [integration-name]
```

Using the `vercel integration add` command to create a new integration resource

## [vercel integration open](#vercel-integration-open)

The `vercel integration open` command opens a deep link into the provider's dashboard for a specific integration. It's useful when you need quick access to the provider's resources from your development environment.

terminal

```
vercel integration open [integration-name]
```

Using the `vercel integration open` command to open the provider's dashboard

## [vercel integration list](#vercel-integration-list)

The `vercel integration list` command displays a list of all installed resources with their associated integrations for the current team or project. It's useful for getting an overview of what integrations are set up in the current scope of your development environment.

terminal

```
vercel integration list
```

Using the `vercel integration list` command to list the integration resources.

The output shows the name, status, product, and integration for each installed resource.

## [vercel integration remove](#vercel-integration-remove)

The `vercel integration remove` command uninstalls the specified integration from your Vercel account. It's useful in automation workflows.

terminal

```
vercel integration remove [integration-name]
```

Using the `vercel integration remove` command to uninstall an integration

You are required to [remove all installed resources](/docs/cli/integration-resource#vercel-integration-resource-remove) from this integration before using this command.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel integration` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel integration-resource"
description: "Learn how to perform native integration product resources tasks using the vercel integration-resource CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/integration-resource"
--------------------------------------------------------------------------------

# vercel integration-resource

Copy page

Ask AI about this page

Last updated February 7, 2025

The `vercel integration-resource` command needs to be used with one of the following actions:

*   `vercel integration-resource remove`
*   `vercel integration-resource disconnect`

For the `resource-name` in all the commands below, use the [URL slug](/docs/integrations/create-integration#create-product-form-details) value of the product for this installed resource.

## [vercel integration-resource remove](#vercel-integration-resource-remove)

The `vercel integration-resource remove` command uninstalls the product for this resource from the integration.

terminal

```
vercel integration-resource remove [resource-name] (--disconnect-all)
```

Using the `vercel integration-resource remove` command to uninstall a resource's product from an integration.

When you include the `--disconnect-all` parameter, all connected projects are disconnected before removal.

## [vercel integration-resource disconnect](#vercel-integration-resource-disconnect)

The `vercel integration-resource disconnect` command disconnects a product's resource from a project where it is currently associated.

terminal

```
vercel integration-resource disconnect [resource-name] (--all)
```

When you include the `--all` parameter, all connected projects are disconnected.

Using the `vercel integration-resource disconnect` command to disconnect a resource from it's connected project(s)

terminal

```
vercel integration-resource disconnect [resource-name] [project-name]
```

Using the `vercel integration-resource disconnect` command to disconnect a resource from a specific connected project where `project-name` is the URL slug of the project.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel integration` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel link"
description: "Learn how to link a local directory to a Vercel Project using the vercel link CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/link"
--------------------------------------------------------------------------------

# vercel link

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel link` command links your local directory to a [Vercel Project](/docs/projects/overview).

## [Usage](#usage)

terminal

```
vercel link
```

Using the `vercel link` command to link the current directory to a Vercel Project.

## [Extended Usage](#extended-usage)

terminal

```
vercel link [path-to-directory]
```

Using the `vercel link` command and supplying a path to the local directory of the Vercel Project.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel link` command.

### [Repo

Alpha

](#repo-alpha)

The `--repo` option can be used to link all projects in your repository to their respective Vercel projects in one command. This command requires that your Vercel projects are using the [Git integration](/docs/git).

terminal

```
vercel link --repo
```

Using the `vercel link` command with the `--repo` option.

### [Yes](#yes)

The `--yes` option can be used to skip questions you are asked when setting up a new Vercel Project. The questions will be answered with the default scope and current directory for the Vercel Project name and location.

terminal

```
vercel link --yes
```

Using the `vercel link` command with the `--yes` option.

### [Project](#project)

The `--project` option can be used to specify a project name. In non-interactive usage, `--project` allows you to set a project name that does not match the name of the current working directory.

terminal

```
vercel link --yes --project foo
```

Using the `vercel link` command with the `--project` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel link` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel list"
description: "Learn how to list out all recent deployments for the current Vercel Project using the vercel list CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/list"
--------------------------------------------------------------------------------

# vercel list

Copy page

Ask AI about this page

Last updated October 7, 2025

The `vercel list` command, which can be shortened to `vercel ls`, provides a list of recent deployments for the currently-linked Vercel Project.

## [Usage](#usage)

terminal

```
vercel list
```

Using the `vercel list` command to retrieve information about multiple deployments for the currently-linked Vercel Project.

## [Extended Usage](#extended-usage)

terminal

```
vercel list [project-name]
```

Using the `vercel list` command to retrieve information about deployments for a specific Vercel Project.

terminal

```
vercel list [project-name] [--status READY,BUILDING]
```

Using the `vercel list` command to retrieve information about deployments filtered by status.

terminal

```
vercel list [project-name] [--meta foo=bar]
```

Using the `vercel list` command to retrieve information about deployments filtered by metadata.

terminal

```
vercel list [project-name] [--policy errored=6m]
```

Using the `vercel list` command to retrieve information about deployments including retention policy.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel list` command.

### [Meta](#meta)

The `--meta` option, shorthand `-m`, can be used to filter results based on Vercel deployment metadata.

terminal

```
vercel list --meta key1=value1 key2=value2
```

Using the `vercel list` command with the `--meta` option.

To see the meta values for a deployment, use [GET /deployments/{idOrUrl}](https://vercel.com/docs/rest-api/reference/endpoints/deployments/get-a-deployment-by-id-or-url) .

### [Policy](#policy)

The `--policy` option, shorthand `-p`, can be used to display expiration based on [Vercel project deployment retention policy](/docs/security/deployment-retention).

terminal

```
vercel list --policy canceled=6m -p errored=6m -p preview=6m -p production=6m
```

Using the `vercel list` command with the `--policy` option.

### [Yes](#yes)

The `--yes` option can be used to skip questions you are asked when setting up a new Vercel Project. The questions will be answered with the default scope and current directory for the Vercel Project name and location.

terminal

```
vercel list --yes
```

Using the `vercel list` command with the `--yes` option.

### [Status](#status)

The `--status` option, shorthand `-s`, can be used to filter deployments by their status.

terminal

```
vercel list --status READY
```

Using the `vercel list` command with the `--status` option to filter by a single status.

You can filter by multiple status values using comma-separated values:

terminal

```
vercel list --status READY,BUILDING
```

Using the `vercel list` command to filter by multiple status values.

The supported status values are:

*   `BUILDING` - Deployments currently being built
*   `ERROR` - Deployments that failed during build or runtime
*   `INITIALIZING` - Deployments in the initialization phase
*   `QUEUED` - Deployments waiting to be built
*   `READY` - Successfully deployed and available
*   `CANCELED` - Deployments that were canceled before completion

### [environment](#environment)

Use the `--environment` option to list the deployments for a specific environment. This could be production, preview, or a [custom environment](/docs/deployments/environments#custom-environments).

terminal

```
vercel list my-app --environment=staging
```

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel list` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel login"
description: "Learn how to login into your Vercel account using the vercel login CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/login"
--------------------------------------------------------------------------------

# vercel login

Copy page

Ask AI about this page

Last updated September 12, 2025

The `vercel login` command allows you to login to your Vercel account through Vercel CLI.

## [Usage](#usage)

terminal

```
vercel login
```

Using the `vercel login` command to login to a Vercel account.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel login` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

## [Related guides](#related-guides)

*   [Why is Vercel CLI asking me to log in?](/guides/why-is-vercel-cli-asking-me-to-log-in)

--------------------------------------------------------------------------------
title: "vercel logout"
description: "Learn how to logout from your Vercel account using the vercel logout CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/logout"
--------------------------------------------------------------------------------

# vercel logout

Copy page

Ask AI about this page

Last updated February 14, 2025

The `vercel logout` command allows you to logout of your Vercel account through Vercel CLI.

## [Usage](#usage)

terminal

```
vercel logout
```

Using the `vercel logout` command to logout of a Vercel account.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel logout` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel logs"
description: "Learn how to list out all runtime logs for a specific deployment using the vercel logs CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/logs"
--------------------------------------------------------------------------------

# vercel logs

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel logs` command displays and follows runtime logs data for a specific deployment. [Runtime logs](/docs/runtime-logs) are produced by [Middleware](/docs/routing-middleware) and [Vercel Functions](/docs/functions). You can find more detailed runtime logs on the [Logs](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Flogs&title=Open+Logs) page from the Vercel Dashboard.

From the moment you run this command, all newly emitted logs will display in your terminal, for up to 5 minutes, unless you interrupt it.

Logs are pretty-printed by default, but you can use the `--json` option to display them in JSON format, which makes the output easier to parse programmatically.

## [Usage](#usage)

terminal

```
vercel logs [deployment-url | deployment-id]
```

Using the `vercel logs` command to retrieve runtime logs for a specific deployment.

## [Unique options](#unique-options)

These are options that only apply to the `vercel logs` command.

### [Json](#json)

The `--json` option, shorthand `-j`, changes the format of the logs output from pretty print to JSON objects. This makes it possible to pipe the output to other command-line tools, such as [jq](https://jqlang.github.io/jq/), to perform your own filtering and formatting.

terminal

```
vercel logs [deployment-url | deployment-id] --json | jq 'select(.level == "warning")'
```

Using the `vercel logs` command with the `--json` option, together with `jq`, to display only warning logs.

### [Follow](#follow)

The `--follow` option has been deprecated since it's now the default behavior.

The `--follow` option, shorthand `-f`, can be used to watch for additional logs output.

### [Limit](#limit)

The `--limit` option has been deprecated as the command displays all newly emitted logs by default.

The `--limit` option, shorthand `-n`, can be used to specify the number of log lines to output.

### [Output](#output)

The `--output` option has been deprecated in favor of the `--json` option.

The `--output` option, shorthand `-o`, can be used to specify the format of the logs output, this can be either `short` (default) or `raw`.

### [Since](#since)

The `--since` option has been deprecated. Logs are displayed from when you started the command.

The `--since` option can be used to return logs only after a specific date, using the ISO 8601 format.

### [Until](#until)

The `--since` option has been deprecated. Logs are displayed until the command is interrupted, either by you or after 5 minutes.

The `--until` option can be used to return logs only up until a specific date, using the ISO 8601 format.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel logs` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel project"
description: "Learn how to list, add, remove, and manage your Vercel Projects using the vercel project CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/project"
--------------------------------------------------------------------------------

# vercel project

Copy page

Ask AI about this page

Last updated July 28, 2025

The `vercel project` command is used to manage your Vercel Projects, providing functionality to list, add, and remove.

## [Usage](#usage)

terminal

```
vercel project ls
 
# Output as JSON
vercel project ls --json
```

Using the `vercel project` command to list all Vercel Project.

terminal

```
vercel project ls --update-required
 
# Output as JSON
vercel project ls --update-required --json
```

Using the `vercel project` command to list all Vercel Project that are affected by an upcoming Node.js runtime deprecation.

terminal

```
vercel project add
```

Using the `vercel project` command to create a new Vercel Project.

terminal

```
vercel project rm
```

Using the `vercel project` command to remove a Vercel Project.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel project` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "Linking Projects with Vercel CLI"
description: "Learn how to link existing Vercel Projects with Vercel CLI."
last_updated: "null"
source: "https://vercel.com/docs/cli/project-linking"
--------------------------------------------------------------------------------

# Linking Projects with Vercel CLI

Copy page

Ask AI about this page

Last updated July 18, 2025

When running `vercel` in a directory for the first time, Vercel CLI needs to know which [scope](/docs/dashboard-features#scope-selector) and [Vercel Project](/docs/projects/overview) you want to [deploy](/docs/cli/deploy) your directory to. You can choose to either [link](/docs/cli/link) an existing Vercel Project or to create a new one.

terminal

```
vercel
? Set up and deploy "~/web/my-lovely-project"? [Y/n] y
? Which scope do you want to deploy to? My Awesome Team
? Link to existing project? [y/N] y
? What’s the name of your existing project? my-lovely-project
🔗 Linked to awesome-team/my-lovely-project (created .vercel and added it to .gitignore)
```

Linking an existing Vercel Project when running Vercel CLI in a new directory.

Once set up, a new `.vercel` directory will be added to your directory. The `.vercel` directory contains both the organization and `id` of your Vercel Project. If you want [unlink](/docs/cli/link) your directory, you can remove the `.vercel` directory.

You can use the [`--yes` option](/docs/cli/deploy#yes) to skip these questions.

## [Framework detection](#framework-detection)

When you create a new Vercel Project, Vercel CLI will [link](/docs/cli/link) the Vercel Project and automatically detect the framework you are using and offer default Project Settings accordingly.

terminal

```
vercel
? Set up and deploy "~/web/my-new-project"? [Y/n] y
? Which scope do you want to deploy to? My Awesome Team
? Link to existing project? [y/N] n
? What’s your project’s name? my-new-project
? In which directory is your code located? my-new-project/
Auto-detected project settings (Next.js):
- Build Command: \`next build\` or \`build\` from \`package.json\`
- Output Directory: Next.js default
- Development Command: next dev --port $PORT
? Want to override the settings? [y/N]
```

Creating a new Vercel Project with the `vercel` command.

You will be provided with default Build Command, Output Directory, and Development Command options.

You can continue with the default Project Settings or overwrite them. You can also edit your Project Settings later in your Vercel Project dashboard.

## [Relevant commands](#relevant-commands)

*   [deploy](/docs/cli/deploy)
*   [link](/docs/cli/link)

--------------------------------------------------------------------------------
title: "vercel promote"
description: "Learn how to promote an existing deployment using the vercel promote CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/promote"
--------------------------------------------------------------------------------

# vercel promote

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel promote` command is used to promote an existing deployment to be the current deployment.

Deployments built for the Production environment are the typical promote target. You can promote Deployments built for the Preview environment, but you will be asked to confirm that action and will result in a new production deployment. You can bypass this prompt by using the `--yes` option.

## [Usage](#usage)

terminal

```
vercel promote [deployment-id or url]
```

Using `vercel promote` will promote an existing deployment to be current.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel promote` command.

### [Timeout](#timeout)

The `--timeout` option is the time that the `vercel promote` command will wait for the promotion to complete. When a timeout occurs, it does not affect the actual promotion which will continue to proceed.

When promoting a deployment, a timeout of `0` will immediately exit after requesting the promotion. The default timeout is `3m`.

terminal

```
vercel promote https://example-app-6vd6bhoqt.vercel.app --timeout=5m
```

Using the `vercel promote` command with the `--timeout` option.

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel promote` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel pull"
description: "Learn how to update your local project with remote environment variables using the vercel pull CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/pull"
--------------------------------------------------------------------------------

# vercel pull

Copy page

Ask AI about this page

Last updated September 24, 2025

The `vercel pull` command is used to store [Environment Variables](/docs/environment-variables) and Project Settings in a local cache (under `.vercel/.env.$target.local.`) for offline use of `vercel build` and `vercel dev`. If you aren't using those commands, you don't need to run `vercel pull`.

When environment variables or project settings are updated on Vercel, remember to use `vercel pull` again to update your local environment variable and project settings values under `.vercel/`.

To download [Environment Variables](/docs/environment-variables) to a specific file (like `.env`), use [`vercel env pull`](/docs/cli/env#exporting-development-environment-variables)   instead.

## [Usage](#usage)

terminal

```
vercel pull
```

Using the `vercel pull` fetches the latest "development" Environment Variables and Project Settings from the cloud.

terminal

```
vercel pull --environment=preview
```

Using the `vercel pull` fetches the latest "preview" Environment Variables and Project Settings from the cloud.

terminal

```
vercel pull --environment=preview --git-branch=feature-branch
```

Using the `vercel pull` fetches the "feature-branch" Environment Variables and Project Settings from the cloud.

terminal

```
vercel pull --environment=production
```

Using the `vercel pull` fetches the latest "production" Environment Variables and Project Settings from the cloud.

## [Unique Options](#unique-options)

These are options that only apply to the `vercel pull` command.

### [Yes](#yes)

The `--yes` option can be used to skip questions you are asked when setting up a new Vercel Project. The questions will be answered with the default scope and current directory for the Vercel Project name and location.

terminal

```
vercel pull --yes
```

Using the `vercel pull` command with the `--yes` option.

### [environment](#environment)

Use the `--environment` option to define the environment you want to pull environment variables from. This could be production, preview, or a [custom environment](/docs/deployments/environments#custom-environments).

terminal

```
vercel pull --environment=staging
```

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel pull` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel redeploy"
description: "Learn how to redeploy your project using the vercel redeploy CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/redeploy"
--------------------------------------------------------------------------------

# vercel redeploy

Copy page

Ask AI about this page

Last updated March 12, 2025

The `vercel redeploy` command is used to rebuild and [redeploy an existing deployment](/docs/deployments/managing-deployments).

## [Usage](#usage)

terminal

```
vercel redeploy [deployment-id or url]
```

Using `vercel redeploy` will rebuild and deploys an existing deployment.

## [Standard output usage](#standard-output-usage)

When redeploying, `stdout` is always the Deployment URL.

terminal

```
vercel redeploy https://example-app-6vd6bhoqt.vercel.app > deployment-url.txt
```

Using the `vercel redeploy` command to redeploy and write `stdout` to a text file. When redeploying, `stdout` is always the Deployment URL.

## [Standard error usage](#standard-error-usage)

If you need to check for errors when the command is executed such as in a CI/CD workflow, use `stderr`. If the exit code is anything other than `0`, an error has occurred. The following example demonstrates a script that checks if the exit code is not equal to 0:

check-redeploy.sh

```
# save stdout and stderr to files
vercel redeploy https://example-app-6vd6bhoqt.vercel.app >deployment-url.txt 2>error.txt
 
# check the exit code
code=$?
if [ $code -eq 0 ]; then
    # Now you can use the deployment url from stdout for the next step of your workflow
    deploymentUrl=`cat deployment-url.txt`
    echo $deploymentUrl
else
    # Handle the error
    errorMessage=`cat error.txt`
    echo "There was an error: $errorMessage"
fi
```

## [Unique Options](#unique-options)

These are options that only apply to the `vercel redeploy` command.

### [No Wait](#no-wait)

The `--no-wait` option does not wait for a deployment to finish before exiting from the `redeploy` command.

terminal

```
vercel redeploy https://example-app-6vd6bhoqt.vercel.app --no-wait
```

Using the `vercel redeploy` command with the `--no-wait` option.

### [target](#target)

Use the `--target` option to define the environment you want to redeploy to. This could be production, preview, or a [custom environment](/docs/deployments/environments#custom-environments).

terminal

```
vercel redeploy https://example-app-6vd6bhoqt.vercel.app --target=staging
```

## [Global Options](#global-options)

The following [global options](/docs/cli/global-options) can be passed when using the `vercel redeploy` command:

*   [`--cwd`](/docs/cli/global-options#current-working-directory)
*   [`--debug`](/docs/cli/global-options#debug)
*   [`--global-config`](/docs/cli/global-options#global-config)
*   [`--help`](/docs/cli/global-options#help)
*   [`--local-config`](/docs/cli/global-options#local-config)
*   [`--no-color`](/docs/cli/global-options#no-color)
*   [`--scope`](/docs/cli/global-options#scope)
*   [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).

--------------------------------------------------------------------------------
title: "vercel remove"
description: "Learn how to remove a deployment using the vercel remove CLI command."
last_updated: "null"
source: "https://vercel.com/docs/cli/remove"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./02-usage-billing.md) | [Index](./index.md) | [Next →](./04-vercel-remove.md)
