---
title: "Develop and build"
section: 05
---

# Develop and build

> How to start working on a new project.

Once you have an Astro project, now you’re ready to build with Astro! 🚀

## Edit your project

[Section titled “Edit your project”](#edit-your-project)

To make changes to your project, open your project folder in your code editor. Working in development mode with the dev server running allows you to see updates to your site as you edit the code.

You can also [customize aspects of your development environment](#configure-your-dev-environment) such as configuring TypeScript or installing the official Astro editor extensions.

### Start the Astro dev server

[Section titled “Start the Astro dev server”](#start-the-astro-dev-server)

Astro comes with a built-in development server that has everything you need for project development. The `astro dev` CLI command will start the local development server so that you can see your new website in action for the very first time.

Every starter template comes with a pre-configured script that will run `astro dev` for you. After navigating into your project directory, use your favorite package manager to run this command and start the Astro development server.

* npm

  ```shell
  npm run dev
  ```jsx
* pnpm

  ```shell
  pnpm run dev
  ```jsx
* Yarn

  ```shell
  yarn run dev
  ```jsx
If all goes well, Astro will now be serving your project on <http://localhost:4321/>. Visit that link in your browser and see your new site!

### Work in development mode

[Section titled “Work in development mode”](#work-in-development-mode)

Astro will listen for live file changes in your `src/` directory and update your site preview as you build, so you will not need to restart the server as you make changes during development. You will always be able to see an up-to-date version of your site in your browser when the dev server is running.

When viewing your site in the browser, you’ll have access to the [Astro dev toolbar](/en/guides/dev-toolbar/). As you build, it will help you inspect your [islands](/en/concepts/islands/), spot accessibility issues, and more.

If you aren’t able to open your project in the browser after starting the dev server, go back to the terminal where you ran the `dev` command and check the message displayed. It should tell you if an error occurred, or if your project is being served at a different URL than <http://localhost:4321/>.

## Build and preview your site

[Section titled “Build and preview your site”](#build-and-preview-your-site)

To check the version of your site that will be created at build time, quit the dev server (`Ctrl` + `C`) and run the appropriate build command for your package manager in your terminal:

* npm

  ```shell
  npm run build
  ```jsx
* pnpm

  ```shell
  pnpm build
  ```jsx
* Yarn

  ```shell
  yarn run build
  ```jsx
Astro will build a deploy-ready version of your site in a separate folder (`dist/` by default) and you can watch its progress in the terminal. This will alert you to any build errors in your project before you deploy to production. If TypeScript is configured to `strict` or `strictest`, the `build` script will also check your project for type errors.

When the build is finished, run the appropriate `preview` command (e.g. `npm run preview`) in your terminal and you can view the built version of your site locally in the same browser preview window.

Note that this previews your code as it existed when the build command was last run. This is meant to give you a preview of how your site will look when it is deployed to the web. Any later changes you make to your code after building will **not** be reflected while you preview your site until you run the build command again.

Use (`Ctrl` + `C`) to quit the preview and run another terminal command, such as restarting the dev server to go back to [working in development mode](#work-in-development-mode) which does update as you edit to show a live preview of your code changes.

Read more about [the Astro CLI](/en/reference/cli-reference/) and the terminal commands you will use as you build with Astro.

Tip

You may wish to [deploy your new site right away](/en/guides/deploy/), before you begin to add or change too much code. This is helpful to get a minimal, working version of your site published and can save you extra time and effort troubleshooting your deployment later.

## Next Steps

[Section titled “Next Steps”](#next-steps)

Success! You are now ready to start building with Astro! 🥳

Here are a few things that we recommend exploring next. You can read them in any order. You can even leave our documentation for a bit and go play in your new Astro project codebase, coming back here whenever you run into trouble or have a question.

### Configure your dev environment

[Section titled “Configure your dev environment”](#configure-your-dev-environment)

Explore the guides below to customize your development experience.

[Editor Setup ](/en/editor-setup/)Customize your code editor to improve the Astro developer experience and unlock new features.

[Dev Toolbar ](/en/guides/dev-toolbar/)Explore the helpful features of the dev toolbar.

[TypeScript Configuration ](/en/guides/typescript/)Configure options for type-checking, IntelliSense, and more.

### Explore Astro’s Features

[Section titled “Explore Astro’s Features”](#explore-astros-features)

[Understand your codebase ](/en/basics/project-structure/)Learn about Astro’s file structure in our Project Structure guide.

[Create content collections ](/en/guides/content-collections/)Add content to your new site with frontmatter validation and automatic type-safety.

[Add view transitions ](/en/guides/view-transitions/)Create seamless page transitions and animations.

[Learn about Islands ](/en/concepts/islands/)Read about Astro's islands architecture.

### Take the introductory tutorial

[Section titled “Take the introductory tutorial”](#take-the-introductory-tutorial)

Build a fully functional Astro blog starting from a single blank page in our [introductory tutorial](/en/tutorial/0-introduction/).

This is a great way to see how Astro works and walks you through the basics of pages, layouts, components, routing, islands, and more. It also includes an optional, beginner-friendly unit for those newer to web development concepts in general, which will guide you through installing the necessary applications on your computer, creating a GitHub account, and deploying your site.

---

[← Previous](04-project-structure.md) | [Index](index.md) | [Next →](index.md)
