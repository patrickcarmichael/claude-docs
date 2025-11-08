---
title: "Share state between islands"
section: 219
---

# Share state between islands

> Learn how to share state across framework components with Nano Stores.

When building an Astro website with [islands architecture / partial hydration](/en/concepts/islands/), you may have run into this problem: **I want to share state between my components.**

UI frameworks like React or Vue may encourage [“context” providers](https://react.dev/learn/passing-data-deeply-with-context) for other components to consume. But when [partially hydrating components](/en/guides/framework-components/#hydrating-interactive-components) within Astro or Markdown, you can’t use these context wrappers.

Astro recommends a different solution for shared client-side storage: [**Nano Stores**](https://github.com/nanostores/nanostores).

![](/houston_chef.webp) **Related recipe:** [Share state between Astro components](/en/recipes/sharing-state/)

## Why Nano Stores?

[Section titled “Why Nano Stores?”](#why-nano-stores)

The [Nano Stores](https://github.com/nanostores/nanostores) library allows you to author stores that any component can interact with. We recommend Nano Stores because:

* **They’re lightweight.** Nano Stores ship the bare minimum JS you’ll need (less than 1 KB) with zero dependencies.
* **They’re framework-agnostic.** This means sharing state between frameworks will be seamless! Astro is built on flexibility, so we love solutions that offer a similar developer experience no matter your preference.

Still, there are a number of alternatives you can explore. These include:

* [Svelte’s built-in stores](https://svelte.dev/tutorial/writable-stores)
* [Solid signals](https://www.solidjs.com/docs/latest) outside of a component context
* [Vue’s reactivity API](https://vuejs.org/guide/scaling-up/state-management.html#simple-state-management-with-reactivity-api)
* [Sending custom browser events](https://developer.mozilla.org/en-US/docs/Web/Events/Creating_and_triggering_events) between components

FAQ

**🙋 Can I use Nano Stores in `.astro` files or other server-side components?**

Nano Stores can be used in `<script>` tags to [share state between `.astro` components](/en/recipes/sharing-state/). However, Using Nano Stores in the frontmatter of server-side components is not recommended because of the following restrictions:

* Writing to a store from a `.astro` file or [non-hydrated component](/en/guides/framework-components/#hydrating-interactive-components) will *not* affect the value received by [client-side components](/en/reference/directives-reference/#client-directives).
* You cannot pass a Nano Store as a “prop” to client-side components.
* You cannot subscribe to store changes from a `.astro` file, since Astro components do not re-render.

If you understand these restrictions and still find a use case, you can give Nano Stores a try! Just remember that Nano Stores are built for reactivity to changes on the **client** specifically.

**🙋 How do Svelte stores compare to Nano Stores?**

**Nano Stores and [Svelte stores](https://svelte.dev/tutorial/writable-stores) are very similar!** In fact, [nanostores allow you to use the same `$` shortcut](https://github.com/nanostores/nanostores#svelte) for subscriptions that you might use with Svelte stores.

If you want to avoid third-party libraries, [Svelte stores](https://svelte.dev/tutorial/writable-stores) are a great cross-island communication tool on their own. Still, you might prefer Nano Stores if a) you like their add-ons for [“objects”](https://github.com/nanostores/nanostores#maps) and [async state](https://github.com/nanostores/nanostores#lazy-stores), or b) you want to communicate between Svelte and other UI frameworks like Preact or Vue.

**🙋 How do Solid signals compare to Nano Stores?**

If you’ve used Solid for a while, you may have tried moving [signals](https://www.solidjs.com/docs/latest#createsignal) or [stores](https://www.solidjs.com/docs/latest#createstore) outside of your components. This is a great way to share state between Solid islands! Try exporting signals from a shared file:

sharedStore.js

```js
import { createSignal } from 'solid-js';


export const sharedCount = createSignal(0);
```jsx
…and all components importing `sharedCount` will share the same state. Though this works well, you might prefer Nano Stores if a) you like their add-ons for [“objects”](https://github.com/nanostores/nanostores#maps) and [async state](https://github.com/nanostores/nanostores#lazy-stores), or b) you want to communicate between Solid and other UI frameworks like Preact or Vue.

## Installing Nano Stores

[Section titled “Installing Nano Stores”](#installing-nano-stores)

To get started, install Nano Stores alongside their helper package for your favorite UI framework:

* Preact

  ```shell
  npm install nanostores @nanostores/preact
  ```jsx
* React

  ```shell
  npm install nanostores @nanostores/react
  ```jsx
* Solid

  ```shell
  npm install nanostores @nanostores/solid
  ```jsx
* Svelte

  ```shell
  npm install nanostores
  ```jsx
  Note

  No helper package here! Nano Stores can be used like standard Svelte stores.

* Vue

  ```shell
  npm install nanostores @nanostores/vue
  ```jsx
You can jump into the [Nano Stores usage guide](https://github.com/nanostores/nanostores#guide) from here, or follow along with our example below!

## Usage example - ecommerce cart flyout

[Section titled “Usage example - ecommerce cart flyout”](#usage-example---ecommerce-cart-flyout)

Let’s say we’re building a simple ecommerce interface with three interactive elements:

* An “add to cart” submission form
* A cart flyout to display those added items
* A cart flyout toggle

[](/videos/stores-example.mp4)

*[**Try the completed example**](https://github.com/withastro/astro/tree/main/examples/with-nanostores) on your machine or online via StackBlitz.*

Your base Astro file may look like this:

src/pages/index.astro

```astro
---
import CartFlyoutToggle from '../components/CartFlyoutToggle';
import CartFlyout from '../components/CartFlyout';
import AddToCartForm from '../components/AddToCartForm';
---


<!DOCTYPE html>
<html lang="en">
<head>...</head>
<body>
  <header>
    <nav>
      <a href="/">Astro storefront</a>
      <CartFlyoutToggle client:load />
    </nav>
  </header>
  <main>
    <AddToCartForm client:load>
    <!-- ... -->
    </AddToCartForm>
  </main>
  <CartFlyout client:load />
</body>
</html>
```jsx
### Using “atoms”

[Section titled “Using “atoms””](#using-atoms)

Let’s start by opening our `CartFlyout` whenever `CartFlyoutToggle` is clicked.

First, create a new JS or TS file to contain our store. We’ll use an [“atom”](https://github.com/nanostores/nanostores#atoms) for this:

src/cartStore.js

```js
import { atom } from 'nanostores';


export const isCartOpen = atom(false);
```jsx
Now, we can import this store into any file that needs to read or write. We’ll start by wiring up our `CartFlyoutToggle`:

* Preact

  src/components/CartFlyoutToggle.jsx

  ```jsx
  import { useStore } from '@nanostores/preact';
  import { isCartOpen } from '../cartStore';


  export default function CartButton() {
    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
    // write to the imported store using `.set`
    return (
      <button onClick={() => isCartOpen.set(!$isCartOpen)}>Cart</button>
    )
  }
  ```jsx
* React

  src/components/CartFlyoutToggle.jsx

  ```jsx
  import { useStore } from '@nanostores/react';
  import { isCartOpen } from '../cartStore';


  export default function CartButton() {
    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
    // write to the imported store using `.set`
    return (
      <button onClick={() => isCartOpen.set(!$isCartOpen)}>Cart</button>
    )
  }
  ```jsx
* Solid

  src/components/CartFlyoutToggle.jsx

  ```jsx
  import { useStore } from '@nanostores/solid';
  import { isCartOpen } from '../cartStore';


  export default function CartButton() {
    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
    // write to the imported store using `.set`
    return (
      <button onClick={() => isCartOpen.set(!$isCartOpen())}>Cart</button>
    )
  }
  ```jsx
* Svelte

  src/components/CartFlyoutToggle.svelte

  ```svelte
  <script>
    import { isCartOpen } from '../cartStore';
  </script>


  <!--use "$" to read the store value-->
  <button on:click={() => isCartOpen.set(!$isCartOpen)}>Cart</button>
  ```jsx
* Vue

  src/components/CartFlyoutToggle.vue

  ```vue
  <template>
    <!--write to the imported store using `.set`-->
    <button @click="isCartOpen.set(!$isCartOpen)">Cart</button>
  </template>


  <script setup>
    import { isCartOpen } from '../cartStore';
    import { useStore } from '@nanostores/vue';


    // read the store value with the `useStore` hook
    const $isCartOpen = useStore(isCartOpen);
  </script>
  ```jsx
Then, we can read `isCartOpen` from our `CartFlyout` component:

* Preact

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/preact';
  import { isCartOpen } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);


    return $isCartOpen ? <aside>...</aside> : null;
  }
  ```jsx
* React

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/react';
  import { isCartOpen } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);


    return $isCartOpen ? <aside>...</aside> : null;
  }
  ```jsx
* Solid

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/solid';
  import { isCartOpen } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);


    return $isCartOpen() ? <aside>...</aside> : null;
  }
  ```jsx
* Svelte

  src/components/CartFlyout.svelte

  ```svelte
  <script>
    import { isCartOpen } from '../cartStore';
  </script>


  {#if $isCartOpen}
  <aside>...</aside>
  {/if}
  ```jsx
* Vue

  src/components/CartFlyout.vue

  ```vue
  <template>
    <aside v-if="$isCartOpen">...</aside>
  </template>


  <script setup>
    import { isCartOpen } from '../cartStore';
    import { useStore } from '@nanostores/vue';


    const $isCartOpen = useStore(isCartOpen);
  </script>
  ```jsx
### Using “maps”

[Section titled “Using “maps””](#using-maps)

Tip

**[Maps](https://github.com/nanostores/nanostores#maps) are a great choice for objects you write to regularly!** Alongside the standard `get()` and `set()` helpers an `atom` provides, you’ll also have a `.setKey()` function to efficiently update individual object keys.

Now, let’s keep track of the items inside your cart. To avoid duplicates and keep track of “quantity,” we can store your cart as an object with the item’s ID as a key. We’ll use a [Map](https://github.com/nanostores/nanostores#maps) for this.

Let’s add a `cartItem` store to our `cartStore.js` from earlier. You can also switch to a TypeScript file to define the shape if you’re so inclined.

* JavaScript

  src/cartStore.js

  ```js
  import { atom, map } from 'nanostores';


  export const isCartOpen = atom(false);


  /**
   * @typedef {Object} CartItem
   * @property {string} id
   * @property {string} name
   * @property {string} imageSrc
   * @property {number} quantity
   */


  /** @type {import('nanostores').MapStore<Record<string, CartItem>>} */
  export const cartItems = map({});
  ```jsx
* TypeScript

  src/cartStore.ts

  ```ts
  import { atom, map } from 'nanostores';


  export const isCartOpen = atom(false);


  export type CartItem = {
    id: string;
    name: string;
    imageSrc: string;
    quantity: number;
  }


  export const cartItems = map<Record<string, CartItem>>({});
  ```jsx
Now, let’s export an `addCartItem` helper for our components to use.

* **If that item doesn’t exist in your cart**, add the item with a starting quantity of 1.
* **If that item *does* already exist**, bump the quantity by 1.

- JavaScript

  src/cartStore.js

  ```js
  ...
  export function addCartItem({ id, name, imageSrc }) {
    const existingEntry = cartItems.get()[id];
    if (existingEntry) {
      cartItems.setKey(id, {
        ...existingEntry,
        quantity: existingEntry.quantity + 1,
      })
    } else {
      cartItems.setKey(
        id,
        { id, name, imageSrc, quantity: 1 }
      );
    }
  }
  ```jsx
- TypeScript

  src/cartStore.ts

  ```ts
  ...
  type ItemDisplayInfo = Pick<CartItem, 'id' | 'name' | 'imageSrc'>;
  export function addCartItem({ id, name, imageSrc }: ItemDisplayInfo) {
    const existingEntry = cartItems.get()[id];
    if (existingEntry) {
      cartItems.setKey(id, {
        ...existingEntry,
        quantity: existingEntry.quantity + 1,
      });
    } else {
      cartItems.setKey(
        id,
        { id, name, imageSrc, quantity: 1 }
      );
    }
  }
  ```jsx
Note

**🙋 Why use `.get()` here instead of a `useStore` helper?**

You may have noticed we’re calling `cartItems.get()` here, instead of grabbing that `useStore` helper from our React / Preact / Solid / Vue examples. This is because **useStore is meant to trigger component re-renders.** In other words, `useStore` should be used whenever the store value is being rendered to the UI. Since we’re reading the value when an **event** is triggered (`addToCart` in this case), and we aren’t trying to render that value, we don’t need `useStore` here.

With our store in place, we can call this function inside our `AddToCartForm` whenever that form is submitted. We’ll also open the cart flyout so you can see a full cart summary.

* Preact

  src/components/AddToCartForm.jsx

  ```jsx
  import { addCartItem, isCartOpen } from '../cartStore';


  export default function AddToCartForm({ children }) {
    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }


    return (
      <form onSubmit={addToCart}>
        {children}
      </form>
    )
  }
  ```jsx
* React

  src/components/AddToCartForm.jsx

  ```jsx
  import { addCartItem, isCartOpen } from '../cartStore';


  export default function AddToCartForm({ children }) {
    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }


    return (
      <form onSubmit={addToCart}>
        {children}
      </form>
    )
  }
  ```jsx
* Solid

  src/components/AddToCartForm.jsx

  ```jsx
  import { addCartItem, isCartOpen } from '../cartStore';


  export default function AddToCartForm({ children }) {
    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }


    return (
      <form onSubmit={addToCart}>
        {children}
      </form>
    )
  }
  ```jsx
* Svelte

  src/components/AddToCartForm.svelte

  ```svelte
  <form on:submit|preventDefault={addToCart}>
    <slot></slot>
  </form>


  <script>
    import { addCartItem, isCartOpen } from '../cartStore';


    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart() {
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }
  </script>
  ```jsx
* Vue

  src/components/AddToCartForm.vue

  ```vue
  <template>
    <form @submit="addToCart">
      <slot></slot>
    </form>
  </template>


  <script setup>
    import { addCartItem, isCartOpen } from '../cartStore';


    // we'll hardcode the item info for simplicity!
    const hardcodedItemInfo = {
      id: 'astronaut-figurine',
      name: 'Astronaut Figurine',
      imageSrc: '/images/astronaut-figurine.png',
    }


    function addToCart(e) {
      e.preventDefault();
      isCartOpen.set(true);
      addCartItem(hardcodedItemInfo);
    }
  </script>
  ```jsx
Finally, we’ll render those cart items inside our `CartFlyout`:

* Preact

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/preact';
  import { isCartOpen, cartItems } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);


    return $isCartOpen ? (
      <aside>
        {Object.values($cartItems).length ? (
          <ul>
            {Object.values($cartItems).map(cartItem => (
              <li>
                <img src={cartItem.imageSrc} alt={cartItem.name} />
                <h3>{cartItem.name}</h3>
                <p>Quantity: {cartItem.quantity}</p>
              </li>
            ))}
          </ul>
        ) : <p>Your cart is empty!</p>}
      </aside>
    ) : null;
  }
  ```jsx
* React

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/react';
  import { isCartOpen, cartItems } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);


    return $isCartOpen ? (
      <aside>
        {Object.values($cartItems).length ? (
          <ul>
            {Object.values($cartItems).map(cartItem => (
              <li>
                <img src={cartItem.imageSrc} alt={cartItem.name} />
                <h3>{cartItem.name}</h3>
                <p>Quantity: {cartItem.quantity}</p>
              </li>
            ))}
          </ul>
        ) : <p>Your cart is empty!</p>}
      </aside>
    ) : null;
  }
  ```jsx
* Solid

  src/components/CartFlyout.jsx

  ```jsx
  import { useStore } from '@nanostores/solid';
  import { isCartOpen, cartItems } from '../cartStore';


  export default function CartFlyout() {
    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);


    return $isCartOpen() ? (
      <aside>
        {Object.values($cartItems()).length ? (
          <ul>
            {Object.values($cartItems()).map(cartItem => (
              <li>
                <img src={cartItem.imageSrc} alt={cartItem.name} />
                <h3>{cartItem.name}</h3>
                <p>Quantity: {cartItem.quantity}</p>
              </li>
            ))}
          </ul>
        ) : <p>Your cart is empty!</p>}
      </aside>
    ) : null;
  }
  ```jsx
* Svelte

  src/components/CartFlyout.svelte

  ```svelte
  <script>
    import { isCartOpen, cartItems } from '../cartStore';
  </script>


  {#if $isCartOpen}
    {#if Object.values($cartItems).length}
      <aside>
        {#each Object.values($cartItems) as cartItem}
        <li>
          <img src={cartItem.imageSrc} alt={cartItem.name} />
          <h3>{cartItem.name}</h3>
          <p>Quantity: {cartItem.quantity}</p>
        </li>
        {/each}
      </aside>
    {:else}
      <p>Your cart is empty!</p>
    {/if}
  {/if}
  ```jsx
* Vue

  src/components/CartFlyout.vue

  ```vue
  <template>
    <aside v-if="$isCartOpen">
      <ul v-if="Object.values($cartItems).length">
        <li v-for="cartItem in Object.values($cartItems)" v-bind:key="cartItem.name">
          <img :src=cartItem.imageSrc :alt=cartItem.name />
          <h3>{{cartItem.name}}</h3>
          <p>Quantity: {{cartItem.quantity}}</p>
        </li>
      </ul>
      <p v-else>Your cart is empty!</p>
    </aside>
  </template>


  <script setup>
    import { cartItems, isCartOpen } from '../cartStore';
    import { useStore } from '@nanostores/vue';


    const $isCartOpen = useStore(isCartOpen);
    const $cartItems = useStore(cartItems);
  </script>
  ```jsx
Now, you should have a fully interactive ecommerce example with the smallest JS bundle in the galaxy 🚀

[**Try the completed example**](https://github.com/withastro/astro/tree/main/examples/with-nanostores) on your machine or online via StackBlitz!

---

[← Previous](218-share-state-between-astro-components.md) | [Index](index.md) | [Next →](index.md)
