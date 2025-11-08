---
title: "Write your first line of Astro"
section: 399
---

# Write your first line of Astro

> Tutorial: Build your first Astro blog —
Make your first edits to your tutorial project's home page

Get ready to…

* Make your first edit to your new website

## Edit your home page

[Section titled “Edit your home page”](#edit-your-home-page)

1. In your code editor, navigate in the Explorer file pane to `src/pages/index.astro` and click on it to open the file’s contents in an editable tab.

   The contents of your `index.astro` file should look like this:

   src/pages/index.astro

   ```astro
   ---
   ---


   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
       <meta name="viewport" content="width=device-width" />
       <meta name="generator" content={Astro.generator} >
       <title>Astro</title>
     </head>
     <body>
       <h1>Astro</h1>
     </body>
   </html>
   ```jsx
2. Edit the content of your page `<body>`.

   Type in the editor to change the heading text on your page and save the change.

   src/pages/index.astro

   ```diff
   <body>
     <h1>Astro</h1>
     <h1>My Astro Site</h1>
   </body>
   ```jsx
3. Check the browser preview and you should see your page content updated to the new text.

Congratulations! You are now an Astro developer!

The rest of this unit will set you up for success with version control and a published website you can show off.

## Checklist

[Section titled “Checklist”](#checklist)

* I can make changes and see them in the browser.
* I am an Astro developer!

---

[← Previous](398-create-your-first-astro-project.md) | [Index](index.md) | [Next →](index.md)
