---
title: "Create your first Astro project"
section: 398
---

# Create your first Astro project

> Tutorial: Build your first Astro blog —
Create a new project for the Astro tutorial and get ready to code

Get ready to…

* Run the `create astro` setup wizard to create a new Astro project
* Start the Astro server in development (dev) mode
* View a live preview of your website in your browser

## Launch the Astro setup wizard

[Section titled “Launch the Astro setup wizard”](#launch-the-astro-setup-wizard)

The preferred way to create a new Astro site is through our `create astro` setup wizard.

1. In the command line of your terminal, run the following command using your preferred package manager:

   * npm

     ```shell
     # create a new project with npm
     npm create astro@latest
     ```jsx
   * pnpm

     ```shell
     # create a new project with pnpm
     pnpm create astro@latest
     ```jsx
   * Yarn

     ```shell
     # create a new project with yarn
     yarn create astro
     ```jsx
2. Enter `y` to install `create-astro`.

3. When the prompt asks you where to create the project, type in the name of a folder to create a new directory for your project, e.g. `./tutorial`

   Note

   A new Astro project can only be created in a completely empty folder, so choose a name for your folder that does not already exist!

4. You will see a short list of starter templates to choose from. Use the arrow keys (up and down) to navigate to the minimal (empty) template, and then press return (enter) to submit your choice.

5. When the prompt asks you whether or not to install dependencies, enter `y`.

6. When the prompt asks you whether or not to initialize a new git repository, enter `y`.

When the install wizard is complete, you no longer need this terminal. You can now open VS Code to continue.

## Open your project in VS Code

[Section titled “Open your project in VS Code”](#open-your-project-in-vs-code)

7. Open VS Code. You will be prompted to open a folder. Choose the folder that you created during the setup wizard.

8. If this is your first time opening an Astro project, you should see a notification asking if you would like to install recommended extensions. Click to see the recommended extensions, and choose the [Astro language support extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode). This will provide syntax highlighting and autocompletions for your Astro code.

9. Make sure the terminal is visible and that you can see the command prompt, such as:

   ```sh
   user@machine:~/tutorial$
   ```jsx
   Keyboard shortcut

   To toggle the visibility of the terminal, use `Ctrl + J` (macOS: `Cmd ⌘ + J`).

You can now use the terminal built right into this window, instead of your computer’s Terminal app, for the rest of this tutorial.

## Run Astro in dev mode

[Section titled “Run Astro in dev mode”](#run-astro-in-dev-mode)

In order to preview your project files *as a website* while you work, you will need Astro to be running in development (dev) mode.

### Start the dev server

[Section titled “Start the dev server”](#start-the-dev-server)

10. Run the command to start the Astro dev server by typing into VS Code’s terminal:

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
    Now you should see confirmation in the terminal that Astro is running in dev mode. 🚀

## View a preview of your website

[Section titled “View a preview of your website”](#view-a-preview-of-your-website)

Your project files contain all the code necessary to display an Astro website, but the browser is responsible for displaying your code as web pages.

11. Click on the `localhost` link in your terminal window to see a live preview of your new Astro website!

    (Astro uses `http://localhost:4321` by default if port `4321` is available.)

    Here’s what the Astro “Empty Project” starter website should look like in the browser preview:

    ![A blank white page with the word Astro at the top.](/tutorial/minimal.png)

Using the Astro dev server

While the Astro server is running in dev mode, you will NOT be able to run commands in your terminal window. Instead, this pane will give you feedback as you preview your site.

You can stop the dev server at any time and return to the command prompt by typing `Ctrl + C` in the terminal.

Sometimes the dev server will stop on its own while you are working. If your live preview stops working, go back to the terminal and restart the dev server by typing `npm run dev`.

## Checklist

[Section titled “Checklist”](#checklist)

* I can create a new Astro project.
* I can start the Astro dev server.

### Resources

[Section titled “Resources”](#resources)

* [Getting Started with Visual Studio Code](https://code.visualstudio.com/docs/introvideos/basics) external — a video tutorial for installing, setting up and working with VS Code

---

[← Previous](397-prepare-your-dev-environment.md) | [Index](index.md) | [Next →](index.md)
