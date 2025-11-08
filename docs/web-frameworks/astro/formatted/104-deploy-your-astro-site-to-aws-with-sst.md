---
title: "Deploy your Astro Site to AWS with SST"
section: 104
---

# Deploy your Astro Site to AWS with SST

> How to deploy your Astro site to AWS with SST

You can deploy an Astro site to AWS using [SST](https://sst.dev), an open-source framework for deploying modern full-stack applications with SSG and SSR support.

You can also use any additional SST components like cron jobs, Buckets, Queues, etc while maintaining type-safety.

## Quickstart

[Section titled “Quickstart”](#quickstart)

1. Create an astro project.

2. Run `npx sst@latest init`.

3. It should detect that you are using Astro and ask you to confirm.

4. Once you’re ready for deployment you can run `npx sst deploy --stage production`.

You can also read [the full Astro on AWS with SST tutorial](https://sst.dev/docs/start/aws/astro) that will guide you through the steps.

### SST components

[Section titled “SST components”](#sst-components)

To use any [additional SST components](https://sst.dev/docs/), add them to `sst.config.ts`.

sst.config.ts

```ts
const bucket = new sst.aws.Bucket("MyBucket", {
  access: "public",
});
new sst.aws.Astro("MyWeb", {
  link: [bucket],
});
```jsx
And then access them in your `.astro` file.

```astro
---
import { Resource } from "sst"
console.log(Resource.MyBucket.name)
---
```jsx
Consult the [SST docs on linking resources](https://sst.dev/docs/linking) to learn more.

If you have any questions, you can [ask in the SST Discord](https://discord.gg/sst).

---

[← Previous](103-deploy-your-astro-site-to-seenode.md) | [Index](index.md) | [Next →](index.md)
