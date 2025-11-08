---
title: "Build forms with API routes"
section: 201
---

# Build forms with API routes

> Learn how to use JavaScript to send form submissions to an API Route.

An HTML form causes the browser to refresh the page or navigate to a new one. To send form data to an API endpoint instead, you must intercept the form submission using JavaScript.

This recipe shows you how to send form data to an API endpoint and handle that data.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [an adapter for on-demand rendering](/en/guides/on-demand-rendering/)
* A [UI Framework integration](/en/guides/framework-components/) installed

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `POST` API endpoint at `/api/feedback` that will receive the form data. Use `request.formData()` to process it. Be sure to validate the form values before you use them.

   This example sends a JSON object with a message back to the client.

   src/pages/api/feedback.ts

   ```ts
   export const prerender = false; // Not needed in 'server' mode
   import type { APIRoute } from "astro";


   export const POST: APIRoute = async ({ request }) => {
     const data = await request.formData();
     const name = data.get("name");
     const email = data.get("email");
     const message = data.get("message");
     // Validate the data - you'll probably want to do more than this
     if (!name || !email || !message) {
       return new Response(
         JSON.stringify({
           message: "Missing required fields",
         }),
         { status: 400 }
       );
     }
     // Do something with the data, then return a success response
     return new Response(
       JSON.stringify({
         message: "Success!"
       }),
       { status: 200 }
     );
   };
   ```jsx
2. Create a form component using your UI framework. Each input should have a `name` attribute that describes the value of that input.

   Be sure to include a `<button>` or `<input type="submit">` element to submit the form.

   * Preact

     src/components/FeedbackForm.tsx

     ```tsx
     export default function Form() {
       return (
         <form>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
         </form>
       );
     }
     ```jsx
   * React

     src/components/FeedbackForm.tsx

     ```tsx
     export default function Form() {
       return (
         <form>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
         </form>
       );
     }
     ```jsx
   * Solid

     src/components/FeedbackForm.tsx

     ```tsx
     export default function Form() {
       return (
         <form>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
         </form>
       );
     }
     ```jsx
   * Svelte

     src/components/FeedbackForm.svelte

     ```svelte
     <form>
       <label>
         Name
         <input type="text" id="name" name="name" required />
       </label>
       <label>
         Email
         <input type="email" id="email" name="email" required />
       </label>
       <label>
         Message
         <textarea id="message" name="message" required />
       </label>
       <button>Send</button>
     </form>
     ```jsx
   * Vue

     src/components/FeedbackForm.vue

     ```vue
     <template>
       <form>
         <label>
           Name
           <input type="text" id="name" name="name" required />
         </label>
         <label>
           Email
           <input type="email" id="email" name="email" required />
         </label>
         <label>
           Message
           <textarea id="message" name="message" required />
         </label>
         <button>Send</button>
       </form>
     </template>
     ```jsx
3. Create a function that accepts a submit event, then pass it as a `submit` handler to your form.

   In the function:

   * Call `preventDefault()` on the event to override the browser’s default submission process.
   * Create a `FormData` object and send it in a `POST` request to your endpoint using `fetch()`.

   - Preact

     src/components/FeedbackForm.tsx

     ```diff
     +import { useState } from "preact/hooks";


     export default function Form() {
       +const [responseMessage, setResponseMessage] = useState("");


       +async function submit(e: SubmitEvent) {
     +    e.preventDefault();
         +const formData = new FormData(e.target as HTMLFormElement);
         +const response = await fetch("/api/feedback", {
           method: "POST",
           body: formData,
         });
         +const data = await response.json();
         +if (data.message) {
           +setResponseMessage(data.message);
     +    }
     +  }


       return (
         <form onSubmit={submit}>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
           +{responseMessage && <p>{responseMessage}</p>}
         </form>
       );
     }
     ```jsx
   - React

     src/components/FeedbackForm.tsx

     ```diff
     +import { useState } from "react";
     +import type { FormEvent } from "react";


     export default function Form() {
       +const [responseMessage, setResponseMessage] = useState("");


       +async function submit(e: FormEvent<HTMLFormElement>) {
     +    e.preventDefault();
         +const formData = new FormData(e.target as HTMLFormElement);
         +const response = await fetch("/api/feedback", {
           method: "POST",
           body: formData,
         });
         +const data = await response.json();
         +if (data.message) {
           +setResponseMessage(data.message);
     +    }
     +  }


       return (
         <form onSubmit={submit}>
           <label htmlFor="name">
             Name
             <input type="text" id="name" name="name" autoComplete="name" required />
           </label>
           <label htmlFor="email">
             Email
             <input type="email" id="email" name="email" autoComplete="email" required />
           </label>
           <label htmlFor="message">
             Message
             <textarea id="message" name="message" autoComplete="off" required />
           </label>
           <button>Send</button>
           +{responseMessage && <p>{responseMessage}</p>}
         </form>
       );
     }
     ```jsx
   - Solid

     src/components/FeedbackForm.tsx

     ```diff
     +import { createSignal, createResource, Suspense } from "solid-js";


     +async function postFormData(formData: FormData) {
       +const response = await fetch("/api/feedback", {
         method: "POST",
         body: formData,
       });
       +const data = await response.json();
       +return data;
     }


     export default function Form() {
       +const [formData, setFormData] = createSignal<FormData>();
       +const [response] = createResource(formData, postFormData);


       +function submit(e: SubmitEvent) {
     +    e.preventDefault();
         +setFormData(new FormData(e.target as HTMLFormElement));
     +  }


       return (
         <form onSubmit={submit}>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
           +<Suspense>{response() && <p>{response().message}</p>}</Suspense>
         </form>
       );
     }
     ```jsx
   - Svelte

     src/components/FeedbackForm.svelte

     ```diff
     <script lang="ts">
       +let responseMessage: string;


       +async function submit(e: SubmitEvent) {
     +    e.preventDefault();
         +const formData = new FormData(e.currentTarget as HTMLFormElement);
         +const response = await fetch("/api/feedback", {
           method: "POST",
           body: formData,
         });
         +const data = await response.json();
     +    responseMessage = data.message;
     +  }
     </script>


     <form on:submit={submit}>
       <label>
         Name
         <input type="text" id="name" name="name" required />
       </label>
       <label>
         Email
         <input type="email" id="email" name="email" required />
       </label>
       <label>
         Message
         <textarea id="message" name="message" required />
       </label>
       <button>Send</button>
     +  {#if responseMessage}
         <p>{responseMessage}</p>
     +  {/if}
     </form>
     ```jsx
   - Vue

     src/components/FeedbackForm.vue

     ```diff
     <script setup lang="ts">
     +import { ref } from "vue";


     +const responseMessage = ref<string>();


     +async function submit(e: Event) {
     +  e.preventDefault();
       +const formData = new FormData(e.currentTarget as HTMLFormElement);
       +const response = await fetch("/api/feedback", {
         method: "POST",
         body: formData,
       });
       +const data = await response.json();
     +  responseMessage.value = data.message;
     +}
     </script>


     <template>
       <form @submit="submit">
         <label>
           Name
           <input type="text" id="name" name="name" required />
         </label>
         <label>
           Email
           <input type="email" id="email" name="email" required />
         </label>
         <label>
           Message
           <textarea id="message" name="message" required />
         </label>
         <button>Send</button>
         <p v-if="responseMessage">{{ responseMessage }}</p>
       </form>
     </template>
     ```jsx
4. Import and include your `<FeedbackForm />` component on a page. Be sure to use a `client:*` directive to ensure that the form logic is hydrated when you want it to be.

   * Preact

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm"
     ---
     <FeedbackForm client:load />
     ```jsx
   * React

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm"
     ---
     <FeedbackForm client:load />
     ```jsx
   * Solid

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm"
     ---
     <FeedbackForm client:load />
     ```jsx
   * Svelte

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm.svelte"
     ---
     <FeedbackForm client:load />
     ```jsx
   * Vue

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm.vue"
     ---
     <FeedbackForm client:load />
     ```

---

[← Previous](200-build-html-forms-in-astro-pages.md) | [Index](index.md) | [Next →](index.md)
