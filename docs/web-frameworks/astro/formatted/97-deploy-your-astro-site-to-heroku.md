---
title: "Deploy your Astro Site to Heroku"
section: 97
---

# Deploy your Astro Site to Heroku

> How to deploy your Astro site to the web using Heroku.

[Heroku](https://www.heroku.com/) is a platform-as-a-service for building, running, and managing modern apps in the cloud. You can deploy an Astro site to Heroku using this guide.

Danger

The following instructions use [the deprecated `heroku-static-buildpack`](https://github.com/heroku/heroku-buildpack-static#warning-heroku-buildpack-static-is-deprecated). Please see [Heroku’s documentation for using `heroku-buildpack-nginx`](https://github.com/dokku/heroku-buildpack-nginx) instead.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

2. Create a Heroku account by [signing up](https://signup.heroku.com/).

3. Run `heroku login` and fill in your Heroku credentials:

   ```bash
   $ heroku login
   ```jsx
4. Create a file called `static.json` in the root of your project with the below content:

   static.json

   ```json
   {
     "root": "./dist"
   }
   ```jsx
   This is the configuration of your site; read more at [heroku-buildpack-static](https://github.com/heroku/heroku-buildpack-static).

5. Set up your Heroku git remote:

   ```bash
   # version change
   $ git init
   $ git add .
   $ git commit -m "My site ready for deployment."


   # creates a new app with a specified name
   $ heroku apps:create example


   # set buildpack for static sites
   $ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-static.git
   ```jsx
6. Deploy your site:

   ```bash
   # publish site
   $ git push heroku master


   # opens a browser to view the Dashboard version of Heroku CI
   $ heroku open
   ```

---

[← Previous](96-deploy-your-astro-site-to-googles-firebase-hosting.md) | [Index](index.md) | [Next →](index.md)
