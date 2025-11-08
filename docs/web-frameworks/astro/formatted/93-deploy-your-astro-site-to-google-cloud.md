---
title: "Deploy your Astro Site to Google Cloud"
section: 93
---

# Deploy your Astro Site to Google Cloud

> How to deploy your Astro site to the web using Google Cloud.

[Google Cloud](https://cloud.google.com/) is a full-featured web app hosting platform that can be used to deploy an Astro site.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

### Cloud Storage (static only)

[Section titled “Cloud Storage (static only)”](#cloud-storage-static-only)

1. [Create a new GCP project](https://console.cloud.google.com/projectcreate), or select one you already have.

2. Create a new bucket under [Cloud Storage](https://cloud.google.com/storage).

3. Give it a name and the other required settings.

4. Upload your `dist` folder into it or upload using [Cloud Build](https://cloud.google.com/build).

5. Enable public access by adding a new permission to `allUsers` called `Storage Object Viewer`.

6. Edit the website configuration and add `ìndex.html` as the entrypoint and `404.html` as the error page.

### Cloud Run (SSR and static)

[Section titled “Cloud Run (SSR and static)”](#cloud-run-ssr-and-static)

Cloud Run is a serverless platform that allows you to run a container without having to manage any infrastructure. It can be used to deploy both static and SSR sites.

#### Prepare the Service

[Section titled “Prepare the Service”](#prepare-the-service)

1. [Create a new GCP project](https://console.cloud.google.com/projectcreate), or select one you already have.

2. Make sure the [Cloud Run API](https://console.cloud.google.com/apis/library/run.googleapis.com) is enabled.

3. Create a new service.

#### Create Dockerfile & Build the Container

[Section titled “Create Dockerfile & Build the Container”](#create-dockerfile--build-the-container)

Before you can deploy your Astro site to Cloud Run, you need to create a Dockerfile that will be used to build the container. Find more information about [how to use Docker with Astro](/en/recipes/docker/#creating-a-dockerfile) in our recipe section.

Once the Dockerfile is created, build it into an image and push it to Google Cloud. There are a few ways to accomplish this:

**Build locally using Docker**:

Use the `docker build` command to build the image, `docker tag` to give it a tag, then `docker push` to push it to a registry. In the case of Google Cloud, [`Artifact Registry`](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) is the easiest option, but you can also use [Docker Hub](https://hub.docker.com/).

```bash

---

[← Previous](92-deploy-your-astro-site-to-gitlab-pages.md) | [Index](index.md) | [Next →](index.md)
