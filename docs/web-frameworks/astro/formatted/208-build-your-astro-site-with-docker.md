---
title: "Build your Astro site with Docker"
section: 208
---

# Build your Astro site with Docker

> Learn how to build your Astro site using Docker.

[Docker](https://docker.com) is a tool to build, deploy, and run applications using containers.

Docker images and containers can be deployed to many different platforms, like AWS, Azure, and [Google Cloud](/en/guides/deploy/google-cloud/#cloud-run-ssr-and-static). This recipe won’t cover how to deploy your site to a specific platform but will show you how to set up Docker for your project.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Docker installed on your local machine. You can find [installation instructions for your operating system here](https://docs.docker.com/get-docker/).
* A Dockerfile in your project. You can [learn more about Dockerfiles here](https://docs.docker.com/engine/reference/builder/) and use the Dockerfiles in the following section as a starting point.

## Creating a Dockerfile

[Section titled “Creating a Dockerfile”](#creating-a-dockerfile)

Create a file called `Dockerfile` in your project’s root directory. This file contains the instructions to build your site, which will differ depending on your needs. This guide can’t show all possible options but will give you starting points for SSR and static mode.

If you’re using another package manager than npm, you’ll need to adjust the commands accordingly.

### SSR

[Section titled “SSR”](#ssr)

This Dockerfile will build your site and serve it using Node.js on port `4321` and therefore requires the [Node adapter](/en/guides/integrations-guide/node/) installed in your Astro project.

Dockerfile

```docker
FROM node:lts AS runtime
WORKDIR /app


COPY . .


RUN npm install
RUN npm run build


ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD ["node", "./dist/server/entry.mjs"]
```jsx
Keep this in mind

These are just examples of Dockerfiles. You can customize them to your needs. For example, you could use another image, like `node:lts-alpine`:

Dockerfile

```diff
-FROM node:lts as runtime
+FROM node:lts-alpine as runtime
```jsx
### Adding a .dockerignore

[Section titled “Adding a .dockerignore”](#adding-a-dockerignore)

Adding a `.dockerignore` file to your project is best practice. This file describes which files or folders should be ignored in the Docker `COPY` or `ADD` commands, very similar to how `.gitignore` works. This speeds up the build process and reduces the size of the final image.

.dockerignore

```docker
.DS_Store
node_modules
dist
```jsx
This file should go in the same directory as the `Dockerfile` itself. [Read the `.dockerignore` documentation for extra info](https://docs.docker.com/engine/reference/builder/#dockerignore-file)

### Static

[Section titled “Static”](#static)

#### Apache (httpd)

[Section titled “Apache (httpd)”](#apache-httpd)

The following Dockerfile will build your site and serve it using Apache httpd on port `80` with the default configuration.

Dockerfile

```docker
FROM node:lts AS build
WORKDIR /app
COPY . .
RUN npm i
RUN npm run build


FROM httpd:2.4 AS runtime
COPY --from=build /app/dist /usr/local/apache2/htdocs/
EXPOSE 80
```jsx
Recommendation

Use this approach for simple websites that don’t need any special configuration. For more complex websites, it is recommended to use a custom configuration, either in Apache or NGINX.

#### NGINX

[Section titled “NGINX”](#nginx)

Dockerfile

```docker
FROM node:lts AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


FROM nginx:alpine AS runtime
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8080
```jsx
In order to build the Dockerfile above, you’ll also need to create a configuration file for NGINX. Create a folder called `nginx` in your project’s root directory and create a file called `nginx.conf` inside.

nginx.conf

```nginx
worker_processes  1;


events {
  worker_connections  1024;
}


http {
  server {
    listen 8080;
    server_name   _;


    root   /usr/share/nginx/html;
    index  index.html index.htm;
    include /etc/nginx/mime.types;


    gzip on;
    gzip_min_length 1000;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss text/javascript;


    error_page 404 /404.html;
    location = /404.html {
            root /usr/share/nginx/html;
            internal;
    }


    location / {
            try_files $uri $uri/index.html =404;
    }
  }
}
```jsx
### Multi-stage build (using SSR)

[Section titled “Multi-stage build (using SSR)”](#multi-stage-build-using-ssr)

Here’s an example of a more advanced Dockerfile that, thanks to Docker’s [multi-stage builds](https://docs.docker.com/build/building/multi-stage/), optimizes the build process for your site by not reinstalling the npm dependencies when only the source code changes. This can reduce the build time even by minutes, depending on the size of your dependencies.

Dockerfile

```docker
FROM node:lts AS base
WORKDIR /app

---

[← Previous](207-customize-file-names-in-the-build-output.md) | [Index](index.md) | [Next →](index.md)
