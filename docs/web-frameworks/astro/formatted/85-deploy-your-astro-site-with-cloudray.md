---
title: "Deploy your Astro Site with CloudRay"
section: 85
---

# Deploy your Astro Site with CloudRay

> How to deploy your Astro site to your Ubuntu Server using CloudRay

You can deploy your Astro project using [CloudRay](https://cloudray.io), a centralized platform that helps you manage your servers, organize Bash scripts, and automate deployment tasks across virtual machines and cloud servers.

Note

CloudRay itself does not host your site. Instead, it provides automation tools to run deployment scripts on your own infrastructure (e.g., Ubuntu servers) using a connected agent.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

* A [CloudRay Account](https://app.cloudray.io)
* Your app code stored in a [GitHub](https://github.com/) repository

## How to Deploy through CloudRay Dashboard

[Section titled “How to Deploy through CloudRay Dashboard”](#how-to-deploy-through-cloudray-dashboard)

Deploying with CloudRay typically involves three main steps:

1. Install the [CloudRay Agent](https://cloudray.io/docs/agent) on your server to securely register your machine and enable remote automation.

2. In your CloudRay Dashboard, write a reusable Bash script that clones your Astro repo, installs dependencies, builds your site, and configures a web server. Define any repo-specific values using [CloudRay’s variable groups](https://cloudray.io/docs/variable-groups).

3. Use CloudRay’s Runlog interface to execute your script on your connected server and monitor the deployment in real time.

## Official Resources

[Section titled “Official Resources”](#official-resources)

Check out [the Astro guide in CloudRay’s docs](https://cloudray.io/articles/how-to-deploy-your-astro-site).

---

[← Previous](84-deploy-your-astro-site-to-cloudflare.md) | [Index](index.md) | [Next →](index.md)
