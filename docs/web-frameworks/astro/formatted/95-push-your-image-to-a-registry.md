---
title: "Push your image to a registry"
section: 95
---

# Push your image to a registry
docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
```jsx
Change the following values in the commands above to match your project:

* `SOURCE_IMAGE`: the local image name or image ID.
* `HOSTNAME`: the registry host (`gcr.io`, `eu.gcr.io`, `asia.gcr.io`, `us.gcr.io`, `docker.io`).
* `PROJECT`: your Google Cloud project ID.
* `TARGET-IMAGE`: the name for the image when it’s stored in the registry.
* `TAG` is the version associated with the image.

[Read more in the Google Cloud docs.](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling)

**Using another tool**:

You can use a CI/CD tool that supports Docker, like [GitHub Actions](https://github.com/marketplace/actions/push-to-gcr-github-action).

**Build using [Cloud Build](https://cloud.google.com/build)**:

Instead of building the Dockerfile locally, you can instruct Google Cloud to build the image remotely. See the [Google Cloud Build documentation here](https://cloud.google.com/build/docs/build-push-docker-image).

#### Deploying the container

[Section titled “Deploying the container”](#deploying-the-container)

Deployment can be handled manually in your terminal [using `gcloud`](https://cloud.google.com/run/docs/deploying#service) or automatically using [Cloud Build](https://cloud.google.com/build) or any other CI/CD system.

Need public access?

Don’t forget to add the permission `Cloud Run Invoker` to the `allUsers` group in the Cloud Run permissions settings!

---

[← Previous](94-build-your-container.md) | [Index](index.md) | [Next →](index.md)
