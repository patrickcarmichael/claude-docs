---
title: "Deploy your Astro Site to Fleek"
section: 88
---

# Deploy your Astro Site to Fleek

> How to deploy your Astro site to the web on Fleek.

You can use [Fleek](http://fleek.xyz/) to deploy a static Astro site to their edge-optimized decentralized network.

This guide gives a complete walkthrough of deploying your Astro site to Fleek using the Fleek UI and CLI.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Fleek as a static site.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Fleek through the website UI or using Fleek’s CLI (command line interface).

### Platform UI Deployment

[Section titled “Platform UI Deployment”](#platform-ui-deployment)

1. Create a [Fleek](https://app.fleek.xyz) account.

2. Push your code to your online Git repository (GitHub).

3. Import your project into Fleek.

4. Fleek will automatically detect Astro and then you can configure the correct settings.

5. Your application is deployed!

### Fleek CLI

[Section titled “Fleek CLI”](#fleek-cli)

1. Install the Fleek CLI.

   ```bash
   # You need to have Nodejs >= 18.18.2
   npm install -g @fleek-platform/cli
   ```jsx
2. Log in to your Fleek account from your terminal.

   ```bash
   fleek login
   ```jsx
3. Run the build command to generate the static files. By default, these will be located in the `dist/` directory.

   ```bash
   npm run build
   ```jsx
4. Initialize your project. This will generate a configuration file.

   ```bash
   fleek sites init
   ```jsx
5. You will be prompted to either create a new Fleek Site or use an existing one. Give the site a name and select the directory where your project is located.

6. Deploy your site.

   ```bash
   fleek sites deploy
   ```jsx
## Learn more

[Section titled “Learn more”](#learn-more)

[Deploy site from Fleek UI](https://fleek.xyz/docs/platform/deployments/)

[Deploy site from Fleek CLI](https://fleek.xyz/docs/cli/hosting/)

---

[← Previous](87-deploy-your-astro-site-with-deployhq.md) | [Index](index.md) | [Next →](index.md)
