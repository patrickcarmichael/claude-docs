---
title: "Deploy your Astro Site to Google’s Firebase Hosting"
section: 96
---

# Deploy your Astro Site to Google’s Firebase Hosting

> How to deploy your Astro site to the web using Google’s Firebase Hosting.

[Firebase Hosting](https://firebase.google.com/products/hosting) is a service provided by Google’s [Firebase](https://firebase.google.com/) app development platform, which can be used to deploy an Astro site.

See our separate guide for [adding Firebase backend services](/en/guides/backend/google-firebase/) such as databases, authentication, and storage.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Firebase as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Firebase.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable SSR in your Astro project and deploy on Firebase add the [Node.js adapter](/en/guides/integrations-guide/node/).

Note

Deploying an SSR Astro site to Firebase requires the [Blaze plan](https://firebase.google.com/pricing) or higher.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install the [Firebase CLI](https://github.com/firebase/firebase-tools). This is a command-line tool that allows you to interact with Firebase from the terminal.

   * npm

     ```shell
     npm install firebase-tools
     ```jsx
   * pnpm

     ```shell
     pnpm add firebase-tools
     ```jsx
   * Yarn

     ```shell
     yarn add firebase-tools
     ```jsx
2. Authenticate the Firebase CLI with your Google account. This will open a browser window where you can log in to your Google account.

   * npm

     ```shell
     npx firebase login
     ```jsx
   * pnpm

     ```shell
     pnpm exec firebase login
     ```jsx
   * Yarn

     ```shell
     yarn firebase login
     ```jsx
3. Enable experimental web frameworks support. This is an experimental feature that allows the Firebase CLI to detect and configure your deployment settings for Astro.

   * npm

     ```shell
     npx firebase experiments:enable webframeworks
     ```jsx
   * pnpm

     ```shell
     pnpm exec firebase experiments:enable webframeworks
     ```jsx
   * Yarn

     ```shell
     yarn firebase experiments:enable webframeworks
     ```jsx
4. Initialize Firebase Hosting in your project. This will create a `firebase.json` and `.firebaserc` file in your project root.

   * npm

     ```shell
     npx firebase init hosting
     ```jsx
   * pnpm

     ```shell
     pnpm exec firebase init hosting
     ```jsx
   * Yarn

     ```shell
     yarn firebase init hosting
     ```jsx
5. Deploy your site to Firebase Hosting. This will build your Astro site and deploy it to Firebase.

   * npm

     ```shell
     npx firebase deploy --only hosting
     ```jsx
   * pnpm

     ```shell
     pnpm exec firebase deploy --only hosting
     ```jsx
   * Yarn

     ```shell
     yarn firebase deploy --only hosting
     ```

---

[← Previous](95-push-your-image-to-a-registry.md) | [Index](index.md) | [Next →](index.md)
