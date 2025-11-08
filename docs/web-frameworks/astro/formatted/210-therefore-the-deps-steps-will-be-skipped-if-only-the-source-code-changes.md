---
title: "Therefore, the `-deps` steps will be skipped if only the source code changes."
section: 210
---

# Therefore, the `-deps` steps will be skipped if only the source code changes.
COPY package.json package-lock.json ./


FROM base AS prod-deps
RUN npm install --omit=dev


FROM base AS build-deps
RUN npm install


FROM build-deps AS build
COPY . .
RUN npm run build


FROM base AS runtime
COPY --from=prod-deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist


ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD ["node", "./dist/server/entry.mjs"]
```jsx
## Recipe

[Section titled “Recipe”](#recipe)

1. Build your container by running the following command in your project’s root directory. Use any name for `<your-astro-image-name>`:

   ```bash
   docker build -t <your-astro-image-name> .
   ```jsx
   This will output an image, which you can run locally or deploy to a platform of your choice.

2. To run your image as a local container, use the following command.

   Replace `<local-port>` with an open port on your machine. Replace `<container-port>` with the port exposed by your Docker container (`4321`, `80`, or `8080` in the above examples.)

   ```bash
   docker run -p <local-port>:<container-port> <your-astro-image-name>
   ```jsx
   You should be able to access your site at `http://localhost:<local-port>`.

3. Now that your website is successfully built and packaged in a container, you can deploy it to a cloud provider. See the [Google Cloud](/en/guides/deploy/google-cloud/#cloud-run-ssr-and-static) deployment guide for one example, and the [Deploy your app](https://docs.docker.com/language/nodejs/deploy/) page in the Docker docs.

---

[← Previous](209-by-copying-only-the-packagejson-and-package-lockjson-here-we-ensure-that-the-following-deps-steps-are-independent-of-the-source-code.md) | [Index](index.md) | [Next →](index.md)
