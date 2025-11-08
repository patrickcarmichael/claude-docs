---
title: "Share state between Astro components"
section: 218
---

# Share state between Astro components

> Learn how to share state across Astro components with Nano Stores.

Tip

Using framework components? See [how to share state between Islands](/en/recipes/sharing-state-islands/)!

When building an Astro website, you may need to share state across components. Astro recommends the use of [Nano Stores](https://github.com/nanostores/nanostores) for shared client storage.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install Nano Stores:

   * npm

     ```shell
     npm install nanostores
     ```jsx
   * pnpm

     ```shell
     pnpm add nanostores
     ```jsx
   * Yarn

     ```shell
     yarn add nanostores
     ```jsx
2. Create a store. In this example, the store tracks whether a dialog is open or not:

   src/store.js

   ```ts
   import { atom } from 'nanostores';


   export const isOpen = atom(false);
   ```jsx
3. Import and use the store in a `<script>` tag in the components that will share state.

   The following `Button` and `Dialog` components each use the shared `isOpen` state to control whether a particular `<div>` is hidden or displayed:

   src/components/Button.astro

   ```astro
   <button id="openDialog">Open</button>


   <script>
     import { isOpen } from '../store.js';


     // Set the store to true when the button is clicked
     function openDialog() {
       isOpen.set(true);
     }


     // Add an event listener to the button
     document.getElementById('openDialog').addEventListener('click', openDialog);
   </script>
   ```jsx
   src/components/Dialog.astro

   ```astro
   <div id="dialog" style="display: none">Hello world!</div>


   <script>
     import { isOpen } from '../store.js';


     // Listen to changes in the store, and show/hide the dialog accordingly
     isOpen.subscribe(open => {
       if (open) {
         document.getElementById('dialog').style.display = 'block';
       } else {
         document.getElementById('dialog').style.display = 'none';
       }
     })
   </script>
   ```jsx
## Resources

[Section titled “Resources”](#resources)

* [Nano Stores on NPM](https://www.npmjs.com/package/nanostores)
* [Nano Stores documentation for Vanilla JS](https://github.com/nanostores/nanostores#vanilla-js)

---

[← Previous](217-add-an-rss-feed.md) | [Index](index.md) | [Next →](index.md)
