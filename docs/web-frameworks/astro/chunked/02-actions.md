**Navigation:** [← Previous](./01-why-astro.md) | [Index](./index.md) | [Next →](./03-apostrophecms-astro.md)

---

# Actions

> Learn how to create type-safe server functions you can call from anywhere.

**Added in:** `astro@4.15`

Astro Actions allow you to define and call backend functions with type-safety. Actions perform data fetching, JSON parsing, and input validation for you. This can greatly reduce the amount of boilerplate needed compared to using an [API endpoint](/en/guides/endpoints/).

Use actions instead of API endpoints for seamless communication between your client and server code and to:

* Automatically validate JSON and form data inputs using [Zod validation](https://zod.dev/?id=primitives).
* Generate type-safe functions to call your backend from the client and even [from HTML form actions](#call-actions-from-an-html-form-action). No need for manual `fetch()` calls.
* Standardize backend errors with the [`ActionError`](/en/reference/modules/astro-actions/#actionerror) object.

## Basic usage

[Section titled “Basic usage”](#basic-usage)

Actions are defined in a `server` object exported from `src/actions/index.ts`:

src/actions/index.ts

```ts
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  myAction: defineAction({ /* ... */ })
}
```

Your actions are available as functions from the `astro:actions` module. Import `actions` and call them client-side within a [UI framework component](/en/guides/framework-components/), [a form POST request](#call-actions-from-an-html-form-action), or by using a `<script>` tag in an Astro component.

When you call an action, it returns an object with either `data` containing the JSON-serialized result, or `error` containing thrown errors.

src/pages/index.astro

```astro
---
---


<script>
import { actions } from 'astro:actions';


async () => {
  const { data, error } = await actions.myAction({ /* ... */ });
}
</script>
```

### Write your first action

[Section titled “Write your first action”](#write-your-first-action)

Follow these steps to define an action and call it in a `script` tag in your Astro page.

1. Create a `src/actions/index.ts` file and export a `server` object.

   src/actions/index.ts

   ```ts
   export const server = {
     // action declarations
   }
   ```

2. Import the `defineAction()` utility from `astro:actions`, and the `z` object from `astro:schema`.

   src/actions/index.ts

   ```diff
   +import { defineAction } from 'astro:actions';
   +import { z } from 'astro:schema';


   export const server = {
     // action declarations
   }
   ```

3. Use the `defineAction()` utility to define a `getGreeting` action. The `input` property will be used to validate input parameters with a [Zod](https://zod.dev) schema and the `handler()` function includes the backend logic to run on the server.

   src/actions/index.ts

   ```diff
   import { defineAction } from 'astro:actions';
   import { z } from 'astro:schema';


   export const server = {
     getGreeting: defineAction({
       input: z.object({
         name: z.string(),
       }),
       +handler: async (input) => {
         return `Hello, ${input.name}!`
       }
     })
   }
   ```

4. Create an Astro component with a button that will fetch a greeting using your `getGreeting` action when clicked.

   src/pages/index.astro

   ```astro
   ---
   ---


   <button>Get greeting</button>


   <script>
   const button = document.querySelector('button');
   button?.addEventListener('click', async () => {
     // Show alert pop-up with greeting from action
   });
   </script>
   ```

5. To use your action, import `actions` from `astro:actions` and then call `actions.getGreeting()` in the click handler. The `name` option will be sent to your action’s `handler()` on the server and, if there are no errors, the result will be available as the `data` property.

   src/pages/index.astro

   ```diff
   ---
   ---


   <button>Get greeting</button>


   <script>
   +import { actions } from 'astro:actions';


   const button = document.querySelector('button');
   button?.addEventListener('click', async () => {
     // Show alert pop-up with greeting from action
     +const { data, error } = await actions.getGreeting({ name: "Houston" });
     +if (!error) alert(data);
   })
   </script>
   ```

See the full Actions API documentation for details on [`defineAction()`](/en/reference/modules/astro-actions/#defineaction) and its properties.

## Organizing actions

[Section titled “Organizing actions”](#organizing-actions)

All actions in your project must be exported from the `server` object in the `src/actions/index.ts` file. You can define actions inline or you can move action definitions to separate files and import them. You can even group related functions in nested objects.

For example, to colocate all of your user actions, you can create a `src/actions/user.ts` file and nest the definitions of both `getUser` and `createUser` inside a single `user` object.

src/actions/user.ts

```ts
import { defineAction } from 'astro:actions';


export const user = {
  getUser: defineAction(/* ... */),
  createUser: defineAction(/* ... */),
}
```

Then, you can import this `user` object into your `src/actions/index.ts` file and add it as a top-level key to the `server` object alongside any other actions:

src/actions/index.ts

```diff
+import { user } from './user';


export const server = {
  myAction: defineAction({ /* ... */ }),
  +user,
}
```

Now, all of your user actions are callable from the `actions.user` object:

* `actions.user.getUser()`
* `actions.user.createUser()`

## Handling returned data

[Section titled “Handling returned data”](#handling-returned-data)

Actions return an object containing either `data` with the type-safe return value of your `handler()`, or an `error` with any backend errors. Errors may come from validation errors on the `input` property or thrown errors within the `handler()`.

Actions return a custom data format that can handle Dates, Maps, Sets, and URLs [using the Devalue library](https://github.com/Rich-Harris/devalue). Therefore, you can’t easily inspect the response from the network like you can with regular JSON. For debugging, you can instead inspect the `data` object returned by actions.

[See the `handler()` API reference](/en/reference/modules/astro-actions/#handler-property) for full details.

### Checking for errors

[Section titled “Checking for errors”](#checking-for-errors)

It’s best to check if an `error` is present before using the `data` property. This allows you to handle errors in advance and ensures `data` is defined without an `undefined` check.

```ts
const { data, error } = await actions.example();


if (error) {
  // handle error cases
  return;
}
// use `data`
```

### Accessing `data` directly without an error check

[Section titled “Accessing data directly without an error check”](#accessing-data-directly-without-an-error-check)

To skip error handling, for example while prototyping or using a library that will catch errors for you, use the `.orThrow()` property on your action call to throw errors instead of returning an `error`. This will return the action’s `data` directly.

This example calls a `likePost()` action that returns the updated number of likes as a `number` from the action `handler`:

```ts
const updatedLikes = await actions.likePost.orThrow({ postId: 'example' });
//    ^ type: number
```

### Handling backend errors in your action

[Section titled “Handling backend errors in your action”](#handling-backend-errors-in-your-action)

You can use the provided `ActionError` to throw an error from your action `handler()`, such as “not found” when a database entry is missing, or “unauthorized” when a user is not logged in. This has two main benefits over returning `undefined`:

* You can set a status code like `404 - Not found` or `401 - Unauthorized`. This improves debugging errors in both development and in production by letting you see the status code of each request.

* In your application code, all errors are passed to the `error` object on an action result. This avoids the need for `undefined` checks on data, and allows you to display targeted feedback to the user depending on what went wrong.

#### Creating an `ActionError`

[Section titled “Creating an ActionError”](#creating-an-actionerror)

To throw an error, import the [`ActionError()` class](/en/reference/modules/astro-actions/#actionerror) from the `astro:actions` module. Pass it a human-readable status `code` (e.g. `"NOT_FOUND"` or `"BAD_REQUEST"`), and an optional `message` to provide further information about the error.

This example throws an error from a `likePost` action when a user is not logged in, after checking a hypothetical “user-session” cookie for authentication:

src/actions/index.ts

```diff
import { defineAction, ActionError } from "astro:actions";
import { z } from "astro:schema";


export const server = {
  likePost: defineAction({
    input: z.object({ postId: z.string() }),
    handler: async (input, ctx) => {
      if (!ctx.cookies.has('user-session')) {
        throw new ActionError({
          code: "UNAUTHORIZED",
          message: "User must be logged in.",
        });
      }
      // Otherwise, like the post
    },
  }),
};
```

#### Handling an `ActionError`

[Section titled “Handling an ActionError”](#handling-an-actionerror)

To handle this error, you can call the action from your application and check whether an `error` property is present. This property will be of type `ActionError` and will contain your `code` and `message`.

In the following example, a `LikeButton.tsx` component calls the `likePost()` action when clicked. If an authentication error occurs, the `error.code` attribute is used to determine whether to display a login link:

src/components/LikeButton.tsx

```tsx
import { actions } from 'astro:actions';
import { useState } from 'preact/hooks';


export function LikeButton({ postId }: { postId: string }) {
  const [showLogin, setShowLogin] = useState(false);
  return (
    <>
      {
        showLogin && <a href="/signin">Log in to like a post.</a>
      }
      <button onClick={async () => {
        const { data, error } = await actions.likePost({ postId });
        if (error?.code === 'UNAUTHORIZED') setShowLogin(true);
        // Early return for unexpected errors
        else if (error) return;
        // update likes
      }}>
        Like
      </button>
    </>
  )
}
```

### Handling client redirects

[Section titled “Handling client redirects”](#handling-client-redirects)

When calling actions from the client, you can integrate with a client-side library like `react-router`, or you can use Astro’s [`navigate()` function](/en/guides/view-transitions/#trigger-navigation) to redirect to a new page when an action succeeds.

This example navigates to the homepage after a `logout` action returns successfully:

src/pages/LogoutButton.tsx

```tsx
import { actions } from 'astro:actions';
import { navigate } from 'astro:transitions/client';


export function LogoutButton() {
  return (
    <button onClick={async () => {
      const { error } = await actions.logout();
      if (!error) navigate('/');
    }}>
      Logout
    </button>
  );
}
```

## Accepting form data from an action

[Section titled “Accepting form data from an action”](#accepting-form-data-from-an-action)

Actions accept JSON data by default. To accept form data from an HTML form, set `accept: 'form'` in your `defineAction()` call:

src/actions/index.ts

```diff
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  comment: defineAction({
    accept: 'form',
    input: z.object(/* ... */),
    handler: async (input) => { /* ... */ },
  })
}
```

### Using validators with form inputs

[Section titled “Using validators with form inputs”](#using-validators-with-form-inputs)

When your action is [configured to accept form data](/en/reference/modules/astro-actions/#accept-property), you can use any Zod validators to validate your fields (e.g. `z.coerce.date()` for date inputs). Extension functions including `.refine()`, `.transform()`, and `.pipe()` are also supported on the `z.object()` validator.

Additionally, Astro provides special handling under the hood for your convenience to validate the following types of field inputs:

* Inputs of type `number` can be validated using `z.number()`
* Inputs of type `checkbox` can be validated using `z.coerce.boolean()`
* Inputs of type `file` can be validated using `z.instanceof(File)`
* Multiple inputs of the same `name` can be validated using `z.array(/* validator */)`
* All other inputs can be validated using `z.string()`

When your form is submitted with empty inputs, the output type may not match your `input` validator. Empty values are converted to `null` except when validating arrays or booleans. For example, if an input of type `text` is submitted with an empty value, the result will be `null` instead of an empty string (`""`).

To apply a union of different validators, use the `z.discriminatedUnion()` wrapper to narrow the type based on a specific form field. This example accepts a form submission to either “create” or “update” a user, using the form field with the name `type` to determine which object to validate against:

src/actions/index.ts

```ts
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  changeUser: defineAction({
    accept: 'form',
    input: z.discriminatedUnion('type', [
      z.object({
        // Matches when the `type` field has the value `create`
        type: z.literal('create'),
        name: z.string(),
        email: z.string().email(),
      }),
      z.object({
        // Matches when the `type` field has the value `update`
        type: z.literal('update'),
        id: z.number(),
        name: z.string(),
        email: z.string().email(),
      }),
    ]),
    async handler(input) {
      if (input.type === 'create') {
        // input is { type: 'create', name: string, email: string }
      } else {
        // input is { type: 'update', id: number, name: string, email: string }
      }
    },
  }),
};
```

### Validating form data

[Section titled “Validating form data”](#validating-form-data)

Actions will parse submitted form data to an object, using the value of each input’s `name` attribute as the object keys. For example, a form containing `<input name="search">` will be parsed to an object like `{ search: 'user input' }`. Your action’s `input` schema will be used to validate this object.

To receive the raw `FormData` object in your action handler instead of a parsed object, omit the `input` property in your action definition.

The following example shows a validated newsletter registration form that accepts a user’s email and requires a “terms of service” agreement checkbox.

1. Create an HTML form component with unique `name` attributes on each input:

   src/components/Newsletter.astro

   ```astro
   <form>
     <label for="email">E-mail</label>
     <input id="email" required type="email" name="email" />
     <label>
       <input required type="checkbox" name="terms">
       I agree to the terms of service
     </label>
     <button>Sign up</button>
   </form>
   ```

2. Define a `newsletter` action to handle the submitted form. Validate the `email` field using the `z.string().email()` validator, and the `terms` checkbox using `z.boolean()`:

   src/actions/index.ts

   ```diff
   import { defineAction } from 'astro:actions';
   import { z } from 'astro:schema';


   export const server = {
     newsletter: defineAction({
       accept: 'form',
       input: z.object({
         email: z.string().email(),
         terms: z.boolean(),
       }),
       +handler: async ({ email, terms }) => { /* ... */ },
     })
   }
   ```

   See the [`input` API reference](/en/reference/modules/astro-actions/#input-validator) for all available form validators.

3. Add a `<script>` to the HTML form to submit the user input. This example overrides the form’s default submit behavior to call `actions.newsletter()`, and redirects to `/confirmation` using the `navigate()` function:

   src/components/Newsletter.astro

   ```diff
   <form>
   7 collapsed lines
     <label for="email">E-mail</label>
     <input id="email" required type="email" name="email" />
     <label>
       <input required type="checkbox" name="terms">
       I agree to the terms of service
     </label>
     <button>Sign up</button>
   </form>


   <script>
     +import { actions } from 'astro:actions';
     +import { navigate } from 'astro:transitions/client';


     +const form = document.querySelector('form');
     +form?.addEventListener('submit', async (event) => {
       +event.preventDefault();
       +const formData = new FormData(form);
       +const { error } = await actions.newsletter(formData);
       +if (!error) navigate('/confirmation');
   +  })
   </script>
   ```

   See [“Call actions from an HTML form action”](#call-actions-from-an-html-form-action) for an alternative way to submit form data.

### Displaying form input errors

[Section titled “Displaying form input errors”](#displaying-form-input-errors)

You can validate form inputs before submission using [native HTML form validation attributes](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation#using_built-in_form_validation) like `required`, `type="email"`, and `pattern`. For more complex `input` validation on the backend, you can use the provided [`isInputError()`](/en/reference/modules/astro-actions/#isinputerror) utility function.

To retrieve input errors, use the `isInputError()` utility to check whether an error was caused by invalid input. Input errors contain a `fields` object with messages for each input name that failed to validate. You can use these messages to prompt your user to correct their submission.

The following example checks the error with `isInputError()`, then checks whether the error is in the email field, before finally creating a message from the errors. You can use JavaScript DOM manipulation or your preferred UI framework to display this message to users.

```js
import { actions, isInputError } from 'astro:actions';


const form = document.querySelector('form');
const formData = new FormData(form);
const { error } = await actions.newsletter(formData);
if (isInputError(error)) {
  // Handle input errors.
  if (error.fields.email) {
    const message = error.fields.email.join(', ');
  }
}
```

## Call actions from an HTML form action

[Section titled “Call actions from an HTML form action”](#call-actions-from-an-html-form-action)

Note

Pages must be on-demand rendered when calling actions using a form action. [Ensure prerendering is disabled on the page](/en/guides/on-demand-rendering/#enabling-on-demand-rendering) before using this API.

You can enable zero-JS form submissions with standard attributes on any `<form>` element. Form submissions without client-side JavaScript may be useful both as a fallback for when JavaScript fails to load, or if you prefer to handle forms entirely from the server.

Calling [Astro.getActionResult()](/en/reference/api-reference/#getactionresult) on the server returns the result of your form submission (`data` or `error`), and can be used to dynamically redirect, handle form errors, update the UI, and more.

To call an action from an HTML form, add `method="POST"` to your `<form>`, then set the form’s `action` attribute using your action, for example `action={actions.logout}`. This will set the `action` attribute to use a query string that is handled by the server automatically.

For example, this Astro component calls the `logout` action when the button is clicked and reloads the current page:

src/components/LogoutButton.astro

```astro
---
import { actions } from 'astro:actions';
---


<form method="POST" action={actions.logout}>
  <button>Log out</button>
</form>
```

Additional attributes on the `<form>` element may be necessary for proper schema validation with Zod. For example, to include file uploads, add `enctype="multipart/form-data"` to ensure that files are sent in a format correctly recognized by `z.instanceof(File)`:

src/components/FileUploadForm.astro

```astro
---
import { actions } from 'astro:actions';
---
<form method="POST" action={actions.upload} enctype="multipart/form-data" >
  <label for="file">Upload File</label>
  <input type="file" id="file" name="file" />
  <button type="submit">Submit</button>
</form>
```

### Redirect on action success

[Section titled “Redirect on action success”](#redirect-on-action-success)

If you need to redirect to a new route on success, you can use an action’s result on the server. A common example is creating a product record and redirecting to the new product’s page, e.g. `/products/[id]`.

For example, say you have a `createProduct` action that returns the generated product id:

src/actions/index.ts

```ts
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  createProduct: defineAction({
    accept: 'form',
    input: z.object({ /* ... */ }),
    handler: async (input) => {
      const product = await persistToDatabase(input);
      return { id: product.id };
    },
  })
}
```

You can retrieve the action result from your Astro component by calling `Astro.getActionResult()`. This returns an object containing `data` or `error` properties when an action is called, or `undefined` if the action was not called during this request.

Use the `data` property to construct a URL to use with `Astro.redirect()`:

src/pages/products/create.astro

```astro
---
import { actions } from 'astro:actions';


const result = Astro.getActionResult(actions.createProduct);
if (result && !result.error) {
  return Astro.redirect(`/products/${result.data.id}`);
}
---


<form method="POST" action={actions.createProduct}>
  <!--...-->
</form>
```

### Handle form action errors

[Section titled “Handle form action errors”](#handle-form-action-errors)

Calling `Astro.getActionResult()` in the Astro component containing your form gives you access to the `data` and `error` objects for custom error handling.

The following example displays a general failure message when a `newsletter` action fails:

src/pages/index.astro

```astro
---
import { actions } from 'astro:actions';


const result = Astro.getActionResult(actions.newsletter);
---


{result?.error && (
  <p class="error">Unable to sign up. Please try again later.</p>
)}
<form method="POST" action={actions.newsletter}>
  <label>
    E-mail
    <input required type="email" name="email" />
  </label>
  <button>Sign up</button>
</form>
```

For more customization, you can [use the `isInputError()` utility](#displaying-form-input-errors) to check whether an error is caused by invalid input.

The following example renders an error banner under the `email` input field when an invalid email is submitted:

src/pages/index.astro

```diff
---
import { actions, isInputError } from 'astro:actions';


const result = Astro.getActionResult(actions.newsletter);
+const inputErrors = isInputError(result?.error) ? result.error.fields : {};
---


<form method="POST" action={actions.newsletter}>
  <label>
    E-mail
    <input required type="email" name="email" aria-describedby="error" />
  </label>
  +{inputErrors.email && <p id="error">{inputErrors.email.join(',')}</p>}
  <button>Sign up</button>
</form>
```

#### Preserve input values on error

[Section titled “Preserve input values on error”](#preserve-input-values-on-error)

Inputs will be cleared whenever a form is submitted. To persist input values, you can [enable view transitions](/en/guides/view-transitions/#enabling-view-transitions-spa-mode) and apply the `transition:persist` directive to each input:

```astro
<input transition:persist required type="email" name="email" />
```

### Update the UI with a form action result

[Section titled “Update the UI with a form action result”](#update-the-ui-with-a-form-action-result)

To use an action’s return value to display a notification to the user on success, pass the action to `Astro.getActionResult()`. Use the returned `data` property to render the UI you want to display.

This example uses the `productName` property returned by an `addToCart` action to show a success message.

src/pages/products/\[slug].astro

```astro
---
import { actions } from 'astro:actions';


const result = Astro.getActionResult(actions.addToCart);
---


{result && !result.error && (
  <p class="success">Added {result.data.productName} to cart</p>
)}


<!--...-->
```

### Advanced: Persist action results with a session

[Section titled “Advanced: Persist action results with a session”](#advanced-persist-action-results-with-a-session)

**Added in:** `astro@5.0.0`

Action results are displayed as a POST submission. This means that the result will be reset to `undefined` when a user closes and revisits the page. The user will also see a “confirm form resubmission?” dialog if they attempt to refresh the page.

To customize this behavior, you can add middleware to handle the result of the action manually. You may choose to persist the action result using a cookie or session storage.

Start by [creating a middleware file](/en/guides/middleware/) and importing [the `getActionContext()` utility](/en/reference/modules/astro-actions/#getactioncontext) from `astro:actions`. This function returns an `action` object with information about the incoming action request, including the action handler and whether the action was called from an HTML form. `getActionContext()` also returns the `setActionResult()` and `serializeActionResult()` functions to programmatically set the value returned by `Astro.getActionResult()`:

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';


export const onRequest = defineMiddleware(async (context, next) => {
  const { action, setActionResult, serializeActionResult } = getActionContext(context);
  if (action?.calledFrom === 'form') {
    const result = await action.handler();
    // ... handle the action result
    setActionResult(action.name, serializeActionResult(result));
  }
  return next();
});
```

A common practice to persist HTML form results is the [POST / Redirect / GET pattern](https://en.wikipedia.org/wiki/Post/Redirect/Get). This redirect removes the “confirm form resubmission?” dialog when the page is refreshed, and allows action results to be persisted throughout the user’s session.

This example applies the POST / Redirect / GET pattern to all form submissions using session storage with the [Netlify server adapter](/en/guides/integrations-guide/netlify/) installed. Action results are written to a session store using [Netlify Blob](https://docs.netlify.com/blobs/overview/), and retrieved after a redirect using a session ID:

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';
import { randomUUID } from "node:crypto";
import { getStore } from "@netlify/blobs";


export const onRequest = defineMiddleware(async (context, next) => {
  // Skip requests for prerendered pages
  if (context.isPrerendered) return next();


  const { action, setActionResult, serializeActionResult } =
    getActionContext(context);
  // Create a Blob store to persist action results with Netlify Blob
  const actionStore = getStore("action-session");


  // If an action result was forwarded as a cookie, set the result
  // to be accessible from `Astro.getActionResult()`
  const sessionId = context.cookies.get("action-session-id")?.value;
  const session = sessionId
    ? await actionStore.get(sessionId, {
        type: "json",
      })
    : undefined;


  if (session) {
    setActionResult(session.actionName, session.actionResult);


    // Optional: delete the session after the page is rendered.
    // Feel free to implement your own persistence strategy
    await actionStore.delete(sessionId);
    context.cookies.delete("action-session-id");
    return next();
  }


  // If an action was called from an HTML form action,
  // call the action handler and redirect to the destination page
  if (action?.calledFrom === "form") {
    const actionResult = await action.handler();


    // Persist the action result using session storage
    const sessionId = randomUUID();
    await actionStore.setJSON(sessionId, {
      actionName: action.name,
      actionResult: serializeActionResult(actionResult),
    });


    // Pass the session ID as a cookie
    // to be retrieved after redirecting to the page
    context.cookies.set("action-session-id", sessionId);


    // Redirect back to the previous page on error
    if (actionResult.error) {
      const referer = context.request.headers.get("Referer");
      if (!referer) {
        throw new Error(
          "Internal: Referer unexpectedly missing from Action POST request.",
        );
      }
      return context.redirect(referer);
    }
    // Redirect to the destination page on success
    return context.redirect(context.originPathname);
  }


  return next();
});
```

## Security when using actions

[Section titled “Security when using actions”](#security-when-using-actions)

Actions are accessible as public endpoints based on the name of the action. For example, the action `blog.like()` will be accessible from `/_actions/blog.like`. This is useful for unit testing action results and debugging production errors. However, this means you **must** use same authorization checks that you would consider for API endpoints and on-demand rendered pages.

### Authorize users from an action handler

[Section titled “Authorize users from an action handler”](#authorize-users-from-an-action-handler)

To authorize action requests, add an authentication check to your action handler. You may want to use [an authentication library](/en/guides/authentication/) to handle session management and user information.

Actions expose [a subset of the `APIContext` object](/en/reference/modules/astro-actions/#actionapicontext) to access properties passed from middleware using `context.locals`. When a user is not authorized, you can raise an `ActionError` with the `UNAUTHORIZED` code:

src/actions/index.ts

```ts
import { defineAction, ActionError } from 'astro:actions';


export const server = {
  getUserSettings: defineAction({
    handler: async (_input, context) => {
      if (!context.locals.user) {
        throw new ActionError({ code: 'UNAUTHORIZED' });
      }
      return { /* data on success */ };
    }
  })
}
```

### Gate actions from middleware

[Section titled “Gate actions from middleware”](#gate-actions-from-middleware)

**Added in:** `astro@5.0.0`

Astro recommends authorizing user sessions from your action handler to respect permission levels and rate-limiting on a per-action basis. However, you can also gate requests to all actions (or a subset of actions) from middleware.

Use the [`getActionContext()` function](/en/reference/modules/astro-actions/#getactioncontext) from your middleware to retrieve information about any inbound action requests. This includes the action name and whether that action was called using a client-side remote procedure call (RPC) function (e.g. `actions.blog.like()`) or an HTML form.

The following example rejects all action requests that do not have a valid session token. If the check fails, a “Forbidden” response is returned. Note: this method ensures that actions are only accessible when a session is present, but is *not* a substitute for secure authorization.

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';


export const onRequest = defineMiddleware(async (context, next) => {
  const { action } = getActionContext(context);
  // Check if the action was called from a client-side function
  if (action?.calledFrom === 'rpc') {
    // If so, check for a user session token
    if (!context.cookies.has('user-session')) {
      return new Response('Forbidden', { status: 403 });
    }
  }


  context.cookies.set('user-session', /* session token */);
  return next();
});
```

## Call actions from Astro components and server endpoints

[Section titled “Call actions from Astro components and server endpoints”](#call-actions-from-astro-components-and-server-endpoints)

You can call actions directly from Astro component scripts using the `Astro.callAction()` wrapper (or `context.callAction()` when using a [server endpoint](/en/guides/endpoints/#server-endpoints-api-routes)). This is common to reuse logic from your actions in other server code.

Pass the action as the first argument and any input parameters as the second argument. This returns the same `data` and `error` objects you receive when calling actions on the client:

src/pages/products.astro

```astro
---
import { actions } from 'astro:actions';


const searchQuery = Astro.url.searchParams.get('search');
if (searchQuery) {
  const { data, error } = await Astro.callAction(actions.findProduct, { query: searchQuery });
  // handle result
}
---
```

# Astro DB

> Learn how to use Astro DB, a fully-managed SQL database designed exclusively for Astro.

Astro DB is a fully-managed SQL database designed for the Astro ecosystem. Develop locally in Astro and deploy to any libSQL-compatible database.

Astro DB is a complete solution to configuring, developing, and querying your data. A local database is created in `.astro/content.db` whenever you run `astro dev` to manage your data without the need for Docker or a network connection.

## Installation

[Section titled “Installation”](#installation)

Install the [`@astrojs/db` integration](/en/guides/integrations-guide/db/) using the built-in `astro add` command:

* npm

  ```sh
  npx astro add db
  ```

* pnpm

  ```sh
  pnpm astro add db
  ```

* Yarn

  ```sh
  yarn astro add db
  ```

## Define your database

[Section titled “Define your database”](#define-your-database)

Installing `@astrojs/db` with the `astro add` command will automatically create a `db/config.ts` file in your project where you will define your database tables:

db/config.ts

```ts
import { defineDb } from 'astro:db';


export default defineDb({
  tables: { },
})
```

### Tables

[Section titled “Tables”](#tables)

Data in Astro DB is stored using SQL tables. Tables structure your data into rows and columns, where columns enforce the type of each row value.

Define your tables in your `db/config.ts` file by providing the structure of the data in your existing libSQL database, or the data you will collect in a new database. This will allow Astro to generate a TypeScript interface to query that table from your project. The result is full TypeScript support when you access your data with property autocompletion and type-checking.

To configure a database table, import and use the `defineTable()` and `column` utilities from `astro:db`. Then, define a name (case-sensitive) for your table and the type of data in each column.

This example configures a `Comment` table with required text columns for `author` and `body`. Then, makes it available to your project through the `defineDb()` export.

db/config.ts

```ts
import { defineDb, defineTable, column } from 'astro:db';


const Comment = defineTable({
  columns: {
    author: column.text(),
    body: column.text(),
  }
})


export default defineDb({
  tables: { Comment },
})
```

See the [table configuration reference](/en/guides/integrations-guide/db/#table-configuration-reference) for a complete reference of table options.

### Columns

[Section titled “Columns”](#columns)

Astro DB supports the following column types:

db/config.ts

```ts
import { defineTable, column } from 'astro:db';


const Comment = defineTable({
  columns: {
    // A string of text.
    author: column.text(),
    // A whole integer value.
    likes: column.number(),
    // A true or false value.
    flagged: column.boolean(),
    // Date/time values queried as JavaScript Date objects.
    published: column.date(),
    // An untyped JSON object.
    metadata: column.json(),
  }
});
```

See the [table columns reference](/en/guides/integrations-guide/db/#table-configuration-reference) for more details.

### Table References

[Section titled “Table References”](#table-references)

Relationships between tables are a common pattern in database design. For example, a `Blog` table may be closely related to other tables of `Comment`, `Author`, and `Category`.

You can define these relations between tables and save them into your database schema using **reference columns**. To establish a relationship, you will need:

* An **identifier column** on the referenced table. This is usually an `id` column with the `primaryKey` property.
* A column on the base table to **store the referenced `id`**. This uses the `references` property to establish a relationship.

This example shows a `Comment` table’s `authorId` column referencing an `Author` table’s `id` column.

db/config.ts

```ts
const Author = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    name: column.text(),
  }
});


const Comment = defineTable({
  columns: {
    authorId: column.number({ references: () => Author.columns.id }),
    body: column.text(),
  }
});
```

## Seed your database for development

[Section titled “Seed your database for development”](#seed-your-database-for-development)

In development, Astro will use your DB config to generate local types according to your schemas. These will be generated fresh from your seed file each time the dev server is started, and will allow you to query and work with the shape of your data with type safety and autocompletion.

You will not have access to production data during development unless you [connect to a remote database](#connecting-to-remote-databases) during development. This protects your data while allowing you to test and develop with a working database with type-safety.

To seed development data for testing and debugging into your Astro project, create a `db/seed.ts` file. Import both the `db` object and your tables defined in `astro:db`. `insert` some initial data into each table. This development data should match the form of both your database schema and production data.

The following example defines two rows of development data for a `Comment` table, and an `Author` table:

db/seed.ts

```ts
import { db, Comment, Author } from 'astro:db';


export default async function() {
  await db.insert(Author).values([
    { id: 1, name: "Kasim" },
    { id: 2, name: "Mina" },
  ]);


  await db.insert(Comment).values([
    { authorId: 1, body: 'Hope you like Astro DB!' },
    { authorId: 2, body: 'Enjoy!'},
  ])
}
```

Your development server will automatically restart your database whenever this file changes, regenerating your types and seeding this development data from `seed.ts` fresh each time.

## Connect a libSQL database for production

[Section titled “Connect a libSQL database for production”](#connect-a-libsql-database-for-production)

Astro DB can connect to any local libSQL database or to any server that exposes the libSQL remote protocol, whether managed or self-hosted.

To connect Astro DB to a libSQL database, set the following environment variables obtained from your database provider:

* `ASTRO_DB_REMOTE_URL`: the connection URL to the location of your local or remote libSQL DB. This may include [URL configuration options](#remote-url-configuration-options) such as sync and encryption as parameters.
* `ASTRO_DB_APP_TOKEN`: the auth token to your libSQL server. This is required for remote databases, and not needed for [local DBs like files or in-memory](#url-scheme-and-host) databases

Depending on your service, you may have access to a CLI or web UI to retrieve these values. The following section will demonstrate connecting to Turso and setting these values as an example, but you are free to use any provider.

### Getting started with Turso

[Section titled “Getting started with Turso”](#getting-started-with-turso)

Turso is the company behind [libSQL](https://github.com/tursodatabase/libsql), the open-source fork of SQLite that powers Astro DB. They provide a fully managed libSQL database platform and are fully compatible with Astro.

The steps below will guide you through the process of installing the Turso CLI, logging in (or signing up), creating a new database, getting the required environmental variables, and pushing the schema to the remote database.

1. Install the [Turso CLI](https://docs.turso.tech/cli/installation).

2. [Log in or sign up](https://docs.turso.tech/cli/authentication) to Turso.

3. Create a new database. In this example the database name is `andromeda`.

   ```sh
   turso db create andromeda
   ```

4. Run the `show` command to see information about the newly created database:

   ```sh
   turso db show andromeda
   ```

   Copy the `URL` value and set it as the value for `ASTRO_DB_REMOTE_URL`.

   .env

   ```dotenv
   ASTRO_DB_REMOTE_URL=libsql://andromeda-houston.turso.io
   ```

5. Create a new token to authenticate requests to the database:

   ```sh
   turso db tokens create andromeda
   ```

   Copy the output of the command and set it as the value for `ASTRO_DB_APP_TOKEN`.

   .env

   ```diff
   ASTRO_DB_REMOTE_URL=libsql://andromeda-houston.turso.io
   +ASTRO_DB_APP_TOKEN=eyJhbGciOiJF...3ahJpTkKDw
   ```

6. Push your DB schema and metadata to the new Turso database.

   ```sh
   astro db push --remote
   ```

7. Congratulations, now you have a database connected! Give yourself a break. 👾

   ```sh
   turso relax
   ```

To explore more features of Turso, check out the [Turso docs](https://docs.turso.tech).

### Connecting to remote databases

[Section titled “Connecting to remote databases”](#connecting-to-remote-databases)

Astro DB allows you to connect to both local and remote databases. By default, Astro uses a local database file for `dev` and `build` commands, recreating tables and inserting development seed data each time.

To connect to a hosted remote database, use the `--remote` flag. This flag enables both readable and writable access to your remote database, allowing you to [accept and persist user data](#insert) in production environments.

Configure your build command to use the `--remote` flag:

package.json

```json
{
  "scripts": {
    "build": "astro build --remote"
  }
}
```

You can also use the flag directly in the command line:

```bash
# Build with a remote connection
astro build --remote


# Develop with a remote connection
astro dev --remote
```

Caution

Be careful when using `--remote` in development. This connects to your live production database, and all changes (inserts, updates, deletions) will be persisted.

The `--remote` flag uses the connection to the remote DB both locally during the build and on the server. Ensure you set the necessary environment variables in both your local development environment and your deployment platform. Additionally, you may need to [configure web mode](/en/guides/integrations-guide/db/#mode) for non-Node.js runtimes such as Cloudflare Workers or Deno.

When deploying your Astro DB project, make sure your deployment platform’s build command is set to `npm run build` (or the equivalent for your package manager) to utilize the `--remote` flag configured in your `package.json`.

### Remote URL configuration options

[Section titled “Remote URL configuration options”](#remote-url-configuration-options)

The `ASTRO_DB_REMOTE_URL` environment variable configures the location of your database as well as other options like sync and encryption.

#### URL scheme and host

[Section titled “URL scheme and host”](#url-scheme-and-host)

libSQL supports both HTTP and WebSockets as the transport protocol for a remote server. It also supports using a local file or an in-memory DB. Those can be configured using the following URL schemes in the connection URL:

* `memory:` will use an in-memory DB. The host must be empty in this case.
* `file:` will use a local file. The host is the path to the file (`file:path/to/file.db`).
* `libsql:` will use a remote server through the protocol preferred by the library (this might be different across versions). The host is the address of the server (`libsql://your.server.io`).
* `http:` will use a remote server through HTTP. `https:` can be used to enable a secure connection. The host is the same as for `libsql:`.
* `ws:` will use a remote server through WebSockets. `wss:` can be used to enable a secure connection. The host is the same as for `libsql:`.

Details of the libSQL connection (e.g. encryption key, replication, sync interval) can be configured as query parameters in the remote connection URL.

For example, to have an encrypted local file work as an embedded replica to a libSQL server, you can set the following environment variables:

.env

```dotenv
ASTRO_DB_REMOTE_URL=file://local-copy.db?encryptionKey=your-encryption-key&syncInterval=60&syncUrl=libsql%3A%2F%2Fyour.server.io
ASTRO_DB_APP_TOKEN=token-to-your-remote-url
```

Caution

Using a database file is an advanced feature, and care should be taken when deploying to prevent overriding your database and losing your production data.

Additionally, this method will not work in serverless deployments, as the file system is not persisted in those environments.

#### `encryptionKey`

[Section titled “encryptionKey”](#encryptionkey)

libSQL has native support for encrypted databases. Passing this search parameter will enable encryption using the given key:

.env

```dotenv
ASTRO_DB_REMOTE_URL=file:path/to/file.db?encryptionKey=your-encryption-key
```

#### `syncUrl`

[Section titled “syncUrl”](#syncurl)

Embedded replicas are a feature of libSQL clients that creates a full synchronized copy of your database on a local file or in memory for ultra-fast reads. Writes are sent to a remote database defined on the `syncUrl` and synchronized with the local copy.

Use this property to pass a separate connection URL to turn the database into an embedded replica of another database. This should only be used with the schemes `file:` and `memory:`. The parameter must be URL encoded.

For example, to have an in-memory embedded replica of a database on `libsql://your.server.io`, you can set the connection URL as such:

.env

```dotenv
ASTRO_DB_REMOTE_URL=memory:?syncUrl=libsql%3A%2F%2Fyour.server.io
```

#### `syncInterval`

[Section titled “syncInterval”](#syncinterval)

Interval between embedded replica synchronizations in seconds. By default it only synchronizes on startup and after writes.

This property is only used when `syncUrl` is also set. For example, to set an in-memory embedded replica to synchronize every minute set the following environment variable:

.env

```dotenv
ASTRO_DB_REMOTE_URL=memory:?syncUrl=libsql%3A%2F%2Fyour.server.io&syncInterval=60
```

## Query your database

[Section titled “Query your database”](#query-your-database)

You can query your database from any [Astro page](/en/basics/astro-pages/#astro-pages), [endpoint](/en/guides/endpoints/), or [action](/en/guides/actions/) in your project using the provided `db` ORM and query builder.

### Drizzle ORM

[Section titled “Drizzle ORM”](#drizzle-orm)

```ts
import { db } from 'astro:db';
```

Astro DB includes a built-in [Drizzle ORM](https://orm.drizzle.team/) client. There is no setup or manual configuration required to use the client. The Astro DB `db` client is automatically configured to communicate with your database (local or remote) when you run Astro. It uses your exact database schema definition for type-safe SQL queries with TypeScript errors when you reference a column or table that doesn’t exist.

### Select

[Section titled “Select”](#select)

The following example selects all rows of a `Comment` table. This returns the complete array of seeded development data from `db/seed.ts` which is then available for use in your page template:

src/pages/index.astro

```astro
---
import { db, Comment } from 'astro:db';


const comments = await db.select().from(Comment);
---


<h2>Comments</h2>


{
  comments.map(({ author, body }) => (
    <article>
      <p>Author: {author}</p>
      <p>{body}</p>
    </article>
  ))
}
```

See the [Drizzle `select()` API reference](https://orm.drizzle.team/docs/select) for a complete overview.

### Insert

[Section titled “Insert”](#insert)

To accept user input, such as handling form requests and inserting data into your remote hosted database, configure your Astro project for [on-demand rendering](/en/guides/on-demand-rendering/) and [add an adapter](/en/guides/on-demand-rendering/#add-an-adapter) for your deployment environment.

This example inserts a row into a `Comment` table based on a parsed form POST request:

src/pages/index.astro

```astro
---
import { db, Comment } from 'astro:db';


if (Astro.request.method === 'POST') {
  // Parse form data
  const formData = await Astro.request.formData();
  const author = formData.get('author');
  const body = formData.get('body');
  if (typeof author === 'string' && typeof body === 'string') {
    // Insert form data into the Comment table
    await db.insert(Comment).values({ author, body });
  }
}


// Render the new list of comments on each request
const comments = await db.select().from(Comment);
---


<form method="POST" style="display: grid">
  <label for="author">Author</label>
  <input id="author" name="author" />


  <label for="body">Body</label>
  <textarea id="body" name="body"></textarea>


  <button type="submit">Submit</button>
</form>


<!-- Render `comments` -->
```

You can also use [Astro actions](/en/guides/actions/) to insert data into an Astro DB table. The following example inserts a row into a `Comment` table using an action:

src/actions/index.ts

```ts
import { db, Comment } from 'astro:db';
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  addComment: defineAction({
    // Actions include type safety with Zod, removing the need
    // to check if typeof {value} === 'string' in your pages
    input: z.object({
      author: z.string(),
      body: z.string(),
    }),
    handler: async (input) => {
      const updatedComments = await db
        .insert(Comment)
        .values(input)
        .returning(); // Return the updated comments
      return updatedComments;
    },
  }),
};
```

See the [Drizzle `insert()` API reference](https://orm.drizzle.team/docs/insert) for a complete overview.

### Delete

[Section titled “Delete”](#delete)

You can also query your database from an API endpoint. This example deletes a row from a `Comment` table by the `id` parameter:

src/pages/api/comments/\[id].ts

```ts
import type { APIRoute } from "astro";
import { db, Comment, eq } from 'astro:db';


export const DELETE: APIRoute = async (ctx) => {
  await db.delete(Comment).where(eq(Comment.id, ctx.params.id ));
  return new Response(null, { status: 204 });
}
```

See the [Drizzle `delete()` API reference](https://orm.drizzle.team/docs/delete) for a complete overview.

### Filtering

[Section titled “Filtering”](#filtering)

To query for table results by a specific property, use [Drizzle options for partial selects](https://orm.drizzle.team/docs/select#partial-select). For example, add [a `.where()` call](https://orm.drizzle.team/docs/select#filtering) to your `select()` query and pass the comparison you want to make.

The following example queries for all rows in a `Comment` table that contain the phrase “Astro DB.” Use [the `like()` operator](https://orm.drizzle.team/docs/operators#like) to check if a phrase is present within the `body`:

src/pages/index.astro

```astro
---
import { db, Comment, like } from 'astro:db';


const comments = await db.select().from(Comment).where(
    like(Comment.body, '%Astro DB%')
);
---
```

### Drizzle utilities

[Section titled “Drizzle utilities”](#drizzle-utilities)

All Drizzle utilities for building queries are exposed from the `astro:db` module. This includes:

* [Filter operators](https://orm.drizzle.team/docs/operators) like `eq()` and `gt()`
* [Aggregation helpers](https://orm.drizzle.team/docs/select#aggregations-helpers) like `count()`
* [The `sql` helper](https://orm.drizzle.team/docs/sql) for writing raw SQL queries

```ts
import { eq, gt, count, sql } from 'astro:db';
```

### Relationships

[Section titled “Relationships”](#relationships)

You can query related data from multiple tables using a SQL join. To create a join query, extend your `db.select()` statement with a join operator. Each function accepts a table to join with and a condition to match rows between the two tables.

This example uses an `innerJoin()` function to join `Comment` authors with their related `Author` information based on the `authorId` column. This returns an array of objects with each `Author` and `Comment` row as top-level properties:

src/pages/index.astro

```astro
---
import { db, eq, Comment, Author } from 'astro:db';


const comments = await db.select()
  .from(Comment)
  .innerJoin(Author, eq(Comment.authorId, Author.id));
---


<h2>Comments</h2>


{
  comments.map(({ Author, Comment }) => (
    <article>
      <p>Author: {Author.name}</p>
      <p>{Comment.body}</p>
    </article>
  ))
}
```

See the [Drizzle join reference](https://orm.drizzle.team/docs/joins#join-types) for all available join operators and config options.

### Batch Transactions

[Section titled “Batch Transactions”](#batch-transactions)

All remote database queries are made as a network request. You may need to “batch” queries together into a single transaction when making a large number of queries, or to have automatic rollbacks if any query fails.

This example seeds multiple rows in a single request using the `db.batch()` method:

db/seed.ts

```ts
import { db, Author, Comment } from 'astro:db';


export default async function () {
  const queries = [];
  // Seed 100 sample comments into your remote database
  // with a single network request.
  for (let i = 0; i < 100; i++) {
    queries.push(db.insert(Comment).values({ body: `Test comment ${i}` }));
  }
  await db.batch(queries);
}
```

See the [Drizzle `db.batch()`](https://orm.drizzle.team/docs/batch-api) docs for more details.

## Pushing changes to your database

[Section titled “Pushing changes to your database”](#pushing-changes-to-your-database)

You can push changes made during development to your database.

### Pushing table schemas

[Section titled “Pushing table schemas”](#pushing-table-schemas)

Your table schema may change over time as your project grows. You can safely test configuration changes locally and push to your remote database when you deploy.

You can push your local schema changes to your remote database via the CLI using the `astro db push --remote` command:

* npm

  ```sh
  npm run astro db push --remote
  ```

* pnpm

  ```sh
  pnpm astro db push --remote
  ```

* Yarn

  ```sh
  yarn astro db push --remote
  ```

This command will verify that your local changes can be made without data loss and, if necessary, suggest how to safely make changes to your schema in order to resolve conflicts.

#### Pushing breaking schema changes

[Section titled “Pushing breaking schema changes”](#pushing-breaking-schema-changes)

Caution

**This will destroy your database**. Only perform this command if you do not need your production data.

If you must change your table schema in a way that is incompatible with your existing data hosted on your remote database, you will need to reset your production database.

To push a table schema update that includes a breaking change, add the `--force-reset` flag to reset all production data:

* npm

  ```sh
  npm run astro db push --remote --force-reset
  ```

* pnpm

  ```sh
  pnpm astro db push --remote --force-reset
  ```

* Yarn

  ```sh
  yarn astro db push --remote --force-reset
  ```

### Renaming tables

[Section titled “Renaming tables”](#renaming-tables)

It is possible to rename a table after pushing your schema to your remote database.

If you **do not have any important production data**, then you can [reset your database](#pushing-breaking-schema-changes) using the `--force-reset` flag. This flag will drop all of the tables in the database and create new ones so that it matches your current schema exactly.

To rename a table while preserving your production data, you must perform a series of non-breaking changes to push your local schema to your remote database safely.

The following example renames a table from `Comment` to `Feedback`:

1. In your database config file, add the `deprecated: true` property to the table you want to rename:

   db/config.ts

   ```diff
   const Comment = defineTable({
     deprecated: true,
     columns: {
       author: column.text(),
       body: column.text(),
     }
   });
   ```

2. Add a new table schema (matching the existing table’s properties exactly) with the new name:

   db/config.ts

   ```diff
   const Comment = defineTable({
     deprecated: true,
     columns: {
       author: column.text(),
       body: column.text(),
     }
   });
   +const Feedback = defineTable({
     columns: {
       author: column.text(),
       body: column.text(),
     }
   +});
   ```

3. [Push to your remote database](#pushing-table-schemas) with `astro db push --remote`. This will add the new table and mark the old as deprecated.

4. Update any of your local project code to use the new table instead of the old table. You might need to migrate data to the new table as well.

5. Once you are confident that the old table is no longer used in your project, you can remove the schema from your `config.ts`:

   db/config.ts

   ```diff
   -const Comment = defineTable({
     deprecated: true,
     columns: {
       author: column.text(),
       body: column.text(),
     }
   -});


   const Feedback = defineTable({
     columns: {
       author: column.text(),
       body: column.text(),
     }
   });
   ```

6. Push to your remote database again with `astro db push --remote`. The old table will be dropped, leaving only the new, renamed table.

### Pushing table data

[Section titled “Pushing table data”](#pushing-table-data)

You may need to push data to your remote database for seeding or data migrations. You can author a `.ts` file with the `astro:db` module to write type-safe queries. Then, execute the file against your remote database using the command `astro db execute <file-path> --remote`:

The following Comments can be seeded using the command `astro db execute db/seed.ts --remote`:

db/seed.ts

```ts
import { Comment } from 'astro:db';


export default async function () {
  await db.insert(Comment).values([
    { authorId: 1, body: 'Hope you like Astro DB!' },
    { authorId: 2, body: 'Enjoy!' },
  ])
}
```

See the [CLI reference](/en/guides/integrations-guide/db/#astro-db-cli-reference) for a complete list of commands.

## Building Astro DB integrations

[Section titled “Building Astro DB integrations”](#building-astro-db-integrations)

[Astro integrations](/en/reference/integrations-reference/) can extend user projects with additional Astro DB tables and seed data.

Use the `extendDb()` method in the `astro:db:setup` hook to register additional Astro DB config and seed files. The `defineDbIntegration()` helper provides TypeScript support and auto-complete for the `astro:db:setup` hook.

my-integration/index.ts

```js
import { defineDbIntegration } from '@astrojs/db/utils';


export default function MyIntegration() {
  return defineDbIntegration({
    name: 'my-astro-db-powered-integration',
    hooks: {
      'astro:db:setup': ({ extendDb }) => {
        extendDb({
          configEntrypoint: '@astronaut/my-package/config',
          seedEntrypoint: '@astronaut/my-package/seed',
        });
      },
      // Other integration hooks...
    },
  });
}
```

Integration [config](#define-your-database) and [seed](#seed-your-database-for-development) files follow the same format as their user-defined equivalents.

### Type safe operations in integrations

[Section titled “Type safe operations in integrations”](#type-safe-operations-in-integrations)

While working on integrations, you may not be able to benefit from Astro’s generated table types exported from `astro:db`. For full type safety, use the `asDrizzleTable()` utility to create a table reference object you can use for database operations.

For example, given an integration setting up the following `Pets` database table:

my-integration/config.ts

```js
import { defineDb, defineTable, column } from 'astro:db';


export const Pets = defineTable({
  columns: {
    name: column.text(),
    species: column.text(),
  },
});


export default defineDb({ tables: { Pets } });
```

The seed file can import `Pets` and use `asDrizzleTable()` to insert rows into your table with type checking:

my-integration/seed.ts

```js
import { asDrizzleTable } from '@astrojs/db/utils';
import { db } from 'astro:db';
import { Pets } from './config';


export default async function() {
  const typeSafePets = asDrizzleTable('Pets', Pets);


  await db.insert(typeSafePets).values([
    { name: 'Palomita', species: 'cat' },
    { name: 'Pan', species: 'dog' },
  ]);
}
```

The value returned by `asDrizzleTable('Pets', Pets)` is equivalent to `import { Pets } from 'astro:db'`, but is available even when Astro’s type generation can’t run. You can use it in any integration code that needs to query or insert into the database.

## Migrate from Astro Studio to Turso

[Section titled “Migrate from Astro Studio to Turso”](#migrate-from-astro-studio-to-turso)

1. In the [Studio dashboard](https://studio.astro.build/), navigate to the project you wish to migrate. In the settings tab, use the “Export Database” button to download a dump of your database.

2. Follow the official instructions to [install the Turso CLI](https://docs.turso.tech/cli/installation) and [sign up or log in](https://docs.turso.tech/cli/authentication) to your Turso account.

3. Create a new database on Turso using the `turso db create` command.

   ```sh
   turso db create [database-name]
   ```

4. Fetch the database URL using the Turso CLI, and use it as the environment variable `ASTRO_DB_REMOTE_URL`.

   ```sh
   turso db show [database-name]
   ```

   ```dotenv
   ASTRO_DB_REMOTE_URL=[your-database-url]
   ```

5. Create a token to access your database, and use it as the environment variable `ASTRO_DB_APP_TOKEN`.

   ```sh
   turso db tokens create [database-name]
   ```

   ```dotenv
   ASTRO_DB_APP_TOKEN=[your-app-token]
   ```

6. Push your DB schema and metadata to the new Turso database.

   ```sh
   astro db push --remote
   ```

7. Import the database dump from step 1 into your new Turso DB.

   ```sh
   turso db shell [database-name] < ./path/to/dump.sql
   ```

8. Once you have confirmed your project connects to the new database, you can safely delete the project from Astro Studio.

# Authentication

> An intro to authentication in Astro

Authentication and authorization are two security processes that manage access to your website or app. Authentication verifies a visitor’s identity, while authorization grants access to protected areas and resources.

Authentication allows you to customize areas of your site for logged-in individuals and provides the greatest protection for personal or private information. Authentication libraries (e.g. [Better Auth](https://better-auth.com/), [Clerk](https://clerk.com)) provide utilities for multiple authentication methods such as email sign-in and OAuth providers.

Tip

There is no official authentication solution for Astro, but you can find [community “auth” integrations](https://astro.build/integrations/?search=auth) in the integrations directory.

See how to [add authentication with Supabase](/en/guides/backend/supabase/#adding-authentication-with-supabase) or [add authentication with Firebase](/en/guides/backend/google-firebase/#adding-authentication-with-firebase) in our dedicated guides for these backend services.

## Better Auth

[Section titled “Better Auth”](#better-auth)

Better Auth is a framework-agnostic authentication (and authorization) framework for TypeScript. It provides a comprehensive set of features out of the box and includes a plugin ecosystem that simplifies adding advanced functionalities.

It supports Astro out of the box, and you can use it to add authentication to your astro project.

### Installation

[Section titled “Installation”](#installation)

* npm

  ```shell
  npm install better-auth
  ```

* pnpm

  ```shell
  pnpm add better-auth
  ```

* Yarn

  ```shell
  yarn add better-auth
  ```

For detailed setup instructions, check out the [Better Auth Installation Guide](https://www.better-auth.com/docs/installation).

### Configuration

[Section titled “Configuration”](#configuration)

Configure your database table to store user data and your preferred authentication methods as described in the [Better Auth Installation Guide](https://www.better-auth.com/docs/installation#configure-database). Then, you’ll need to mount the Better Auth handler in your Astro project.

src/pages/api/auth/\[...all].ts

```ts
import { auth } from "../../../lib/auth"; // import your Better Auth instance
import type { APIRoute } from "astro";


export const prerender = false; // Not needed in 'server' mode


export const ALL: APIRoute = async (ctx) => {
  return auth.handler(ctx.request);
};
```

Follow the [Better Auth Astro Guide](https://www.better-auth.com/docs/integrations/astro) to learn more.

### Usage

[Section titled “Usage”](#usage)

Better Auth offers a `createAuthClient` helper for various frameworks, including Vanilla JS, React, Vue, Svelte, and Solid.

For example, to create a client for React, import the helper from `'better-auth/react'`:

* React

  src/lib/auth-client.ts

  ```ts
  import { createAuthClient } from 'better-auth/react';


  export const authClient = createAuthClient();


  export const { signIn, signOut } = authClient;
  ```

* Solid

  src/lib/auth-client.ts

  ```ts
  import { createAuthClient } from 'better-auth/solid';


  export const authClient = createAuthClient();


  export const { signIn, signOut } = authClient;
  ```

* Svelte

  src/lib/auth-client.ts

  ```ts
  import { createAuthClient } from 'better-auth/svelte';


  export const authClient = createAuthClient();


  export const { signIn, signOut } = authClient;
  ```

* Vue

  src/lib/auth-client.ts

  ```ts
  import { createAuthClient } from 'better-auth/vue';


  export const authClient = createAuthClient();


  export const { signIn, signOut } = authClient;
  ```

Once your client is set up, you can use it to authenticate users in your Astro components or any framework-specific files. The following example adds the ability to log in or log out with your configured `signIn()` and `signOut()` functions.

src/pages/index.astro

```astro
---
import Layout from 'src/layouts/Base.astro';
---
<Layout>
  <button id="login">Login</button>
  <button id="logout">Logout</button>


  <script>
    const { signIn, signOut } = await import("./lib/auth-client")
    document.querySelector("#login").onclick = () => signIn.social({
      provider: "github",
      callbackURL: "/dashboard",
    })
    document.querySelector("#logout").onclick = () => signOut()
  </script>
</Layout>
```

You can then use the `auth` object to get the user’s session data in your server-side code. The following example personalizes page content by displaying an authenticated user’s name:

src/pages/index.astro

```astro
---
import { auth } from "../../../lib/auth"; // import your Better Auth instance


export const prerender = false; // Not needed in 'server' mode


const session = await auth.api.getSession({
  headers: Astro.request.headers,
});
---


<p>{session.user?.name}</p>
```

You can also use the `auth` object to protect your routes using middleware. The following example checks whether a user trying to access a logged-in dashboard route is authenticated, and redirects them to the home page if not.

src/middleware.ts

```ts
import { auth } from "../../../auth"; // import your Better Auth instance
import { defineMiddleware } from "astro:middleware";


export const onRequest = defineMiddleware(async (context, next) => {
  const isAuthed = await auth.api
    .getSession({
      headers: context.request.headers,
    })
  if (context.url.pathname === "/dashboard" && !isAuthed) {
    return context.redirect("/");
  }
  return next();
});
```

### Next Steps

[Section titled “Next Steps”](#next-steps)

* [Better Auth Astro Guide](https://www.better-auth.com/docs/integrations/astro)
* [Better Auth Astro Example](https://github.com/better-auth/examples/tree/main/astro-example)
* [Better Auth Documentation](https://www.better-auth.com/docs)
* [Better Auth GitHub Repository](https://github.com/better-auth/better-auth)

## Clerk

[Section titled “Clerk”](#clerk)

Clerk is a complete suite of embeddable UIs, flexible APIs, and admin dashboards to authenticate and manage your users. An [official Clerk SDK for Astro](https://clerk.com/docs/references/astro/overview) is available.

### Installation

[Section titled “Installation”](#installation-1)

Install `@clerk/astro` using the package manager of your choice.

* npm

  ```shell
  npm install @clerk/astro
  ```

* pnpm

  ```shell
  pnpm add @clerk/astro
  ```

* Yarn

  ```shell
  yarn add @clerk/astro
  ```

### Configuration

[Section titled “Configuration”](#configuration-1)

Follow [Clerk’s own Astro Quickstart guide](https://clerk.com/docs/quickstarts/astro) to set up Clerk integration and middleware in your Astro project.

### Usage

[Section titled “Usage”](#usage-1)

Clerk provides components that allow you to control the visibility of pages based on your user’s authentication state. Show logged out users a sign in button instead of the content available to users who are logged in:

src/pages/index.astro

```astro
---
import Layout from 'src/layouts/Base.astro';
import { SignedIn, SignedOut, UserButton, SignInButton } from '@clerk/astro/components';


export const prerender = false; // Not needed in 'server' mode
---


<Layout>
    <SignedIn>
        <UserButton />
    </SignedIn>
    <SignedOut>
        <SignInButton />
    </SignedOut>
</Layout>
```

Clerk also allows you to protect routes on the server using middleware. Specify which routes are protected, and prompt unauthenticated users to sign in:

src/middleware.ts

```ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/astro/server';


const isProtectedRoute = createRouteMatcher([
  '/dashboard(.*)',
  '/forum(.*)',
]);


export const onRequest = clerkMiddleware((auth, context) => {
  if (!auth().userId && isProtectedRoute(context.request)) {
    return auth().redirectToSignIn();
  }
});
```

### Next Steps

[Section titled “Next Steps”](#next-steps-1)

* Read the [official `@clerk/astro` documentation](https://clerk.com/docs/references/astro/overview)
* Start from a template with the [Clerk + Astro Quickstart project](https://github.com/clerk/clerk-astro-quickstart)

## Lucia

[Section titled “Lucia”](#lucia)

[Lucia](https://lucia-auth.com/) is a resource for implementing session-based authentication in a number of frameworks, including Astro.

### Guides

[Section titled “Guides”](#guides)

1. Create a [basic sessions API](https://lucia-auth.com/sessions/basic-api/) with your chosen database.
2. Add [session cookies](https://lucia-auth.com/sessions/cookies/astro) using endpoints and middleware.
3. Implement [GitHub OAuth](https://lucia-auth.com/tutorials/github-oauth/astro) using the APIs you implemented.

### Examples

[Section titled “Examples”](#examples)

* [GitHub OAuth example in Astro](https://github.com/lucia-auth/example-astro-github-oauth)
* [Google OAuth example in Astro](https://github.com/lucia-auth/example-astro-google-oauth)
* [Email and password example with 2FA in Astro](https://github.com/lucia-auth/example-astro-email-password-2fa)
* [Email and password example with 2FA and WebAuthn in Astro](https://github.com/lucia-auth/example-astro-email-password-webauthn)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Using Microsoft Entra Id EasyAuth with Astro and Azure Static Web App](https://agramont.net/blog/entra-id-easyauth-with-astro/)

# Use a backend service with Astro

> How to use a backend service to add authentication, storage and data

**Ready to add features like authentication, monitoring, storage, or data to your Astro project?** Follow one of our guides to integrate a backend service.

Tip

Find [community-maintained integrations](https://astro.build/integrations/) for adding popular features to your project in our integrations directory.

## Backend service guides

[Section titled “Backend service guides”](#backend-service-guides)

Note that many of these pages are **stubs**: they’re collections of resources waiting for your contribution!

* ![](/logos/appwriteio.svg)

  ### [Appwrite](/en/guides/backend/appwriteio/)

* ![](/logos/firebase.svg)

  ### [Firebase](/en/guides/backend/google-firebase/)

* ![](/logos/neon.svg)

  ### [Neon](/en/guides/backend/neon/)

* ![](/logos/prisma-postgres.svg)

  ### [Prisma Postgres](/en/guides/backend/prisma-postgres/)

* ![](/logos/sentry.svg)

  ### [Sentry](/en/guides/backend/sentry/)

* ![](/logos/supabase.svg)

  ### [Supabase](/en/guides/backend/supabase/)

* ![](/logos/turso.svg)

  ### [Turso](/en/guides/backend/turso/)

* ![](/logos/xata.svg)

  ### [Xata](/en/guides/backend/xata/)

## What is a backend service?

[Section titled “What is a backend service?”](#what-is-a-backend-service)

A backend service is a cloud-based system that helps you build and manage your backend infrastructure. It provides a set of tools and services for managing databases, user authentication, and other server-side functionality. This enables you to focus on building your applications without having to worry about managing the underlying infrastructure.

## Why would I use a backend service?

[Section titled “Why would I use a backend service?”](#why-would-i-use-a-backend-service)

You might want to consider a backend service if your project has complex server-side needs, for example:

* user sign-ups and authentication
* persistent data storage
* user-uploaded asset storage
* API generation
* realtime communication
* application monitoring

# Appwrite & Astro

> Add a backend to your project with Appwrite

[Appwrite](https://appwrite.io/) is a self-hosted backend-as-a-service platform that provides authentication and account management, user preferences, database and storage persistence, cloud functions, localization, image manipulation, and other server-side utilities.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Appwrite Demos for Astro](https://github.com/appwrite/demos-for-astro)

# Firebase & Astro

> Add a backend to your project with Firebase

[Firebase](https://firebase.google.com/) is an app development platform that provides a NoSQL database, authentication, realtime subscriptions, functions, and storage.

See our separate guide for [deploying to Firebase hosting](/en/guides/deploy/google-firebase/).

## Initializing Firebase in Astro

[Section titled “Initializing Firebase in Astro”](#initializing-firebase-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A [Firebase project with a web app configured](https://firebase.google.com/docs/web/setup).

* An Astro project with [`output: 'server'` for on-demand rendering](/en/guides/on-demand-rendering/) enabled.

* Firebase credentials: You will need two sets of credentials to connect Astro to Firebase:

  * Web app credentials: These credentials will be used by the client side of your app. You can find them in the Firebase console under *Project settings > General*. Scroll down to the **Your apps** section and click on the **Web app** icon.
  * Project credentials: These credentials will be used by the server side of your app. You can generate them in the Firebase console under *Project settings > Service accounts > Firebase Admin SDK > Generate new private key*.

### Adding Firebase credentials

[Section titled “Adding Firebase credentials”](#adding-firebase-credentials)

To add your Firebase credentials to Astro, create an `.env` file in the root of your project with the following variables:

.env

```ini
FIREBASE_PRIVATE_KEY_ID=YOUR_PRIVATE_KEY_ID
FIREBASE_PRIVATE_KEY=YOUR_PRIVATE_KEY
FIREBASE_PROJECT_ID=YOUR_PROJECT_ID
FIREBASE_CLIENT_EMAIL=YOUR_CLIENT_EMAIL
FIREBASE_CLIENT_ID=YOUR_CLIENT_ID
FIREBASE_AUTH_URI=YOUR_AUTH_URI
FIREBASE_TOKEN_URI=YOUR_TOKEN_URI
FIREBASE_AUTH_CERT_URL=YOUR_AUTH_CERT_URL
FIREBASE_CLIENT_CERT_URL=YOUR_CLIENT_CERT_URL
```

Now, these environment variables are available for use in your project.

If you would like to have IntelliSense for your Firebase environment variables, edit or create the file `env.d.ts` in your `src/` directory and configure your types:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly FIREBASE_PRIVATE_KEY_ID: string;
  readonly FIREBASE_PRIVATE_KEY: string;
  readonly FIREBASE_PROJECT_ID: string;
  readonly FIREBASE_CLIENT_EMAIL: string;
  readonly FIREBASE_CLIENT_ID: string;
  readonly FIREBASE_AUTH_URI: string;
  readonly FIREBASE_TOKEN_URI: string;
  readonly FIREBASE_AUTH_CERT_URL: string
  readonly FIREBASE_CLIENT_CERT_URL: string;
}


interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

Tip

Read more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your project should now include these new files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect Astro with Firebase, install the following packages using the single command below for your preferred package manager:

* `firebase` - the Firebase SDK for the client side
* `firebase-admin` - the Firebase Admin SDK for the server side

- npm

  ```shell
  npm install firebase firebase-admin
  ```

- pnpm

  ```shell
  pnpm add firebase firebase-admin
  ```

- Yarn

  ```shell
  yarn add firebase firebase-admin
  ```

Next, create a folder named `firebase` in the `src/` directory and add two new files to this folder: `client.ts` and `server.ts`.

In `client.ts`, add the following code to initialize Firebase in the client using your web app credentials and the `firebase` package:

src/firebase/client.ts

```ts
import { initializeApp } from "firebase/app";


const firebaseConfig = {
  apiKey: "my-public-api-key",
  authDomain: "my-auth-domain",
  projectId: "my-project-id",
  storageBucket: "my-storage-bucket",
  messagingSenderId: "my-sender-id",
  appId: "my-app-id",
};


export const app = initializeApp(firebaseConfig);
```

Note

Remember to replace the `firebaseConfig` object with your own web app credentials.

In `server.ts`, add the following code to initialize Firebase in the server using your project credentials and the `firebase-admin` package:

src/firebase/server.ts

```ts
import type { ServiceAccount } from "firebase-admin";
import { initializeApp, cert, getApps } from "firebase-admin/app";


const activeApps = getApps();
const serviceAccount = {
  type: "service_account",
  project_id: import.meta.env.FIREBASE_PROJECT_ID,
  private_key_id: import.meta.env.FIREBASE_PRIVATE_KEY_ID,
  private_key: import.meta.env.FIREBASE_PRIVATE_KEY,
  client_email: import.meta.env.FIREBASE_CLIENT_EMAIL,
  client_id: import.meta.env.FIREBASE_CLIENT_ID,
  auth_uri: import.meta.env.FIREBASE_AUTH_URI,
  token_uri: import.meta.env.FIREBASE_TOKEN_URI,
  auth_provider_x509_cert_url: import.meta.env.FIREBASE_AUTH_CERT_URL,
  client_x509_cert_url: import.meta.env.FIREBASE_CLIENT_CERT_URL,
};


const initApp = () => {
  if (import.meta.env.PROD) {
    console.info('PROD env detected. Using default service account.')
    // Use default config in firebase functions. Should be already injected in the server by Firebase.
    return initializeApp()
  }
  console.info('Loading service account from env.')
  return initializeApp({
    credential: cert(serviceAccount as ServiceAccount)
  })
}


export const app = activeApps.length === 0 ? initApp() : activeApps[0];
```

Note

Remember to replace the `serviceAccount` object with your own project credentials.

Finally, your project should now include these new files:

* src

  * env.d.ts

  * firebase

    * **client.ts**
    * **server.ts**

* .env

* astro.config.mjs

* package.json

## Adding authentication with Firebase

[Section titled “Adding authentication with Firebase”](#adding-authentication-with-firebase)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

* An Astro project [initialized with Firebase](#initializing-firebase-in-astro).
* A Firebase project with email/password authentication enabled in the Firebase console under *Authentication > Sign-in* method.

### Creating auth server endpoints

[Section titled “Creating auth server endpoints”](#creating-auth-server-endpoints)

Firebase authentication in Astro requires the following three [Astro server endpoints](/en/guides/endpoints/):

* `GET /api/auth/signin` - to sign in a user
* `GET /api/auth/signout` - to sign out a user
* `POST /api/auth/register` - to register a user

Create three endpoints related to authentication in a new directory `src/pages/api/auth/`: `signin.ts`, `signout.ts` and `register.ts`.

`signin.ts` contains the code to sign in a user using Firebase:

src/pages/api/auth/signin.ts

```ts
import type { APIRoute } from "astro";
import { app } from "../../../firebase/server";
import { getAuth } from "firebase-admin/auth";


export const GET: APIRoute = async ({ request, cookies, redirect }) => {
  const auth = getAuth(app);


  /* Get token from request headers */
  const idToken = request.headers.get("Authorization")?.split("Bearer ")[1];
  if (!idToken) {
    return new Response(
      "No token found",
      { status: 401 }
    );
  }


  /* Verify id token */
  try {
    await auth.verifyIdToken(idToken);
  } catch (error) {
    return new Response(
      "Invalid token",
      { status: 401 }
    );
  }


  /* Create and set session cookie */
  const fiveDays = 60 * 60 * 24 * 5 * 1000;
  const sessionCookie = await auth.createSessionCookie(idToken, {
    expiresIn: fiveDays,
  });


  cookies.set("__session", sessionCookie, {
    path: "/",
  });


  return redirect("/dashboard");
};
```

Caution

Firebase only allows the use of [one cookie, and it must be named `__session`](https://firebase.google.com/docs/hosting/manage-cache#using_cookies). Any other cookies the client sends will not be visible to your application.

Note

This is a basic implementation of the signin endpoint. You can add more logic to this endpoint to suit your needs.

`signout.ts` contains the code to log out a user by deleting the session cookie:

src/pages/api/auth/signout.ts

```ts
import type { APIRoute } from "astro";


export const GET: APIRoute = async ({ redirect, cookies }) => {
  cookies.delete("__session", {
    path: "/",
  });
  return redirect("/signin");
};
```

Note

This is a basic implementation of the signout endpoint. You can add more logic to this endpoint to suit your needs.

`register.ts` contains the code to register a user using Firebase:

src/pages/api/auth/register.ts

```ts
import type { APIRoute } from "astro";
import { getAuth } from "firebase-admin/auth";
import { app } from "../../../firebase/server";


export const POST: APIRoute = async ({ request, redirect }) => {
  const auth = getAuth(app);


  /* Get form data */
  const formData = await request.formData();
  const email = formData.get("email")?.toString();
  const password = formData.get("password")?.toString();
  const name = formData.get("name")?.toString();


  if (!email || !password || !name) {
    return new Response(
      "Missing form data",
      { status: 400 }
    );
  }


  /* Create user */
  try {
    await auth.createUser({
      email,
      password,
      displayName: name,
    });
  } catch (error: any) {
    return new Response(
      "Something went wrong",
      { status: 400 }
    );
  }
  return redirect("/signin");
};
```

Note

This is a basic implementation of the register endpoint. You can add more logic to this endpoint to suit your needs.

After creating server endpoints for authentication, your project directory should now include these new files:

* src

  * env.d.ts

  * firebase

    * client.ts
    * server.ts

  * pages

    * api

      * auth

        * **signin.ts**
        * **signout.ts**
        * **register.ts**

* .env

* astro.config.mjs

* package.json

### Creating pages

[Section titled “Creating pages”](#creating-pages)

Create the pages that will use the Firebase endpoints:

* `src/pages/register` - will contain a form to register a user
* `src/pages/signin` - will contain a form to sign in a user
* `src/pages/dashboard` - will contain a dashboard that can only be accessed by authenticated users

The example `src/pages/register.astro` below includes a form that will send a `POST` request to the `/api/auth/register` endpoint. This endpoint will create a new user using the data from the form and then will redirect the user to the `/signin` page.

src/pages/register.astro

```astro
---
import Layout from "../layouts/Layout.astro";
---


<Layout title="Register">
  <h1>Register</h1>
  <p>Already have an account? <a href="/signin">Sign in</a></p>
  <form action="/api/auth/register" method="post">
    <label for="name">Name</label>
    <input type="text" name="name" id="name" />
    <label for="email" for="email">Email</label>
    <input type="email" name="email" id="email" />
    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <button type="submit">Login</button>
  </form>
</Layout>
```

`src/pages/signin.astro` uses the Firebase server app to verify the user’s session cookie. If the user is authenticated, the page will redirect the user to the `/dashboard` page.

The example page below contains a form that will send a `POST` request to the `/api/auth/signin` endpoint with the ID token generated by the Firebase client app.

The endpoint will verify the ID token and create a new session cookie for the user. Then, the endpoint will redirect the user to the `/dashboard` page.

src/pages/signin.astro

```astro
---
import { app } from "../firebase/server";
import { getAuth } from "firebase-admin/auth";
import Layout from "../layouts/Layout.astro";


/* Check if the user is authenticated */
const auth = getAuth(app);
if (Astro.cookies.has("__session")) {
  const sessionCookie = Astro.cookies.get("__session")!.value;
  const decodedCookie = await auth.verifySessionCookie(sessionCookie);
  if (decodedCookie) {
    return Astro.redirect("/dashboard");
  }
}
---


<Layout title="Sign in">
  <h1>Sign in</h1>
  <p>New here? <a href="/register">Create an account</a></p>
  <form action="/api/auth/signin" method="post">
    <label for="email" for="email">Email</label>
    <input type="email" name="email" id="email" />
    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <button type="submit">Login</button>
  </form>
</Layout>
<script>
  import {
    getAuth,
    inMemoryPersistence,
    signInWithEmailAndPassword,
  } from "firebase/auth";
  import { app } from "../firebase/client";


  const auth = getAuth(app);
  // This will prevent the browser from storing session data
  auth.setPersistence(inMemoryPersistence);


  const form = document.querySelector("form") as HTMLFormElement;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const email = formData.get("email")?.toString();
    const password = formData.get("password")?.toString();


    if (!email || !password) {
      return;
    }
    const userCredential = await signInWithEmailAndPassword(
      auth,
      email,
      password
    );
    const idToken = await userCredential.user.getIdToken();
    const response = await fetch("/api/auth/signin", {
      method: "GET",
      headers: {
        Authorization: `Bearer ${idToken}`,
      },
    });


    if (response.redirected) {
      window.location.assign(response.url);
    }
  });
</script>
```

`src/pages/dashboard.astro` will verify the user’s session cookie using the Firebase server app. If the user is not authenticated, the page will redirect the user to the `/signin` page.

The example page below display the user’s name and a button to sign out. Clicking the button will send a `GET` request to the `/api/auth/signout` endpoint.

The endpoint will delete the user’s session cookie and redirect the user to the `/signin` page.

src/pages/dashboard.astro

```astro
---
import { app } from "../firebase/server";
import { getAuth } from "firebase-admin/auth";
import Layout from "../layouts/Layout.astro";


const auth = getAuth(app);


/* Check current session */
if (!Astro.cookies.has("__session")) {
  return Astro.redirect("/signin");
}
const sessionCookie = Astro.cookies.get("__session")!.value;
const decodedCookie = await auth.verifySessionCookie(sessionCookie);
const user = await auth.getUser(decodedCookie.uid);


if (!user) {
  return Astro.redirect("/signin");
}
---


<Layout title="dashboard">
  <h1>Welcome {user.displayName}</h1>
  <p>We are happy to see you here</p>
  <form action="/api/auth/signout">
    <button type="submit">Sign out</button>
  </form>
</Layout>
```

### Adding OAuth providers

[Section titled “Adding OAuth providers”](#adding-oauth-providers)

To add OAuth providers to your app, you need to enable them in the Firebase console.

In the Firebase console, go to the **Authentication** section and click on the **Sign-in method** tab. Then, click on the **Add a new provider** button and enable the providers you want to use.

The example below uses the **Google** provider.

Edit the `signin.astro` page to add:

* a button to sign in with Google underneath the existing form
* an event listener on the button to handle the sign in process in the existing `<script>`.

src/pages/signin.astro

```diff
---
import { app } from "../firebase/server";
import { getAuth } from "firebase-admin/auth";
import Layout from "../layouts/Layout.astro";


/* Check if the user is authenticated */
const auth = getAuth(app);
if (Astro.cookies.has("__session")) {
  const sessionCookie = Astro.cookies.get("__session")!.value;
  const decodedCookie = await auth.verifySessionCookie(sessionCookie);
  if (decodedCookie) {
    return Astro.redirect("/dashboard");
  }
}
---


<Layout title="Sign in">
  <h1>Sign in</h1>
  <p>New here? <a href="/register">Create an account</a></p>
  <form action="/api/auth/signin" method="post">
    <label for="email" for="email">Email</label>
    <input type="email" name="email" id="email" />
    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <button type="submit">Login</button>
  </form>
  <button id="google">Sign in with Google</button>
</Layout>
<script>
  import {
    getAuth,
    inMemoryPersistence,
    signInWithEmailAndPassword,
+    GoogleAuthProvider,
+    signInWithPopup,
  } from "firebase/auth";
  import { app } from "../firebase/client";


  const auth = getAuth(app);
  auth.setPersistence(inMemoryPersistence);


  const form = document.querySelector("form") as HTMLFormElement;
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const email = formData.get("email")?.toString();
    const password = formData.get("password")?.toString();


    if (!email || !password) {
      return;
    }
    const userCredential = await signInWithEmailAndPassword(
      auth,
      email,
      password
    );
    const idToken = await userCredential.user.getIdToken();
    const response = await fetch("/api/auth/signin", {
      headers: {
        Authorization: `Bearer ${idToken}`,
      },
    });


    if (response.redirected) {
      window.location.assign(response.url);
    }
  });


  +const googleSignin = document.querySelector("#google") as HTMLButtonElement;
  +googleSignin.addEventListener("click", async () => {
    +const provider = new GoogleAuthProvider();
    +const userCredential = await signInWithPopup(auth, provider);
    +const idToken = await userCredential.user.getIdToken();
    +const res = await fetch("/api/auth/signin", {
      headers: {
        Authorization: `Bearer ${idToken}`,
      },
    });


    +if (res.redirected) {
      +window.location.assign(res.url);
+    }
+  });
</script>
```

When clicked, the Google sign in button will open a popup window to sign in with Google. Once the user signs in, it will send a `POST` request to the `/api/auth/signin` endpoint with the ID token generated by OAuth provider.

The endpoint will verify the ID token and create a new session cookie for the user. Then, the endpoint will redirect the user to the `/dashboard` page.

## Connecting to Firestore database

[Section titled “Connecting to Firestore database”](#connecting-to-firestore-database)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-2)

* An Astro project initialized with Firebase as described in the [Initializing Firebase in Astro](#initializing-firebase-in-astro) section.

* A Firebase project with a Firestore database. You can follow the [Firebase documentation to create a new project and set up a Firestore database](https://firebase.google.com/docs/firestore/quickstart).

In this recipe, the Firestore collection will be called **friends** and will contain documents with the following fields:

* `id`: autogenerated by Firestore
* `name`: a string field
* `age`: a number field
* `isBestFriend`: a boolean field

### Creating the server endpoints

[Section titled “Creating the server endpoints”](#creating-the-server-endpoints)

Create two new files in a new directory `src/pages/api/friends/`: `index.ts` and `[id].ts`. These will create two server endpoints to interact with the Firestore database in the following ways:

* `POST /api/friends`: to create a new document in the friends collection.
* `POST /api/friends/:id`: to update a document in the friends collection.
* `DELETE /api/friends/:id`: to delete a document in the friends collection.

`index.ts` will contain the code to create a new document in the friends collection:

src/pages/api/friends/index.ts

```ts
import type { APIRoute } from "astro";
import { app } from "../../../firebase/server";
import { getFirestore } from "firebase-admin/firestore";


export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  const name = formData.get("name")?.toString();
  const age = formData.get("age")?.toString();
  const isBestFriend = formData.get("isBestFriend") === "on";


  if (!name || !age) {
    return new Response("Missing required fields", {
      status: 400,
    });
  }
  try {
    const db = getFirestore(app);
    const friendsRef = db.collection("friends");
    await friendsRef.add({
      name,
      age: parseInt(age),
      isBestFriend,
    });
  } catch (error) {
    return new Response("Something went wrong", {
      status: 500,
    });
  }
  return redirect("/dashboard");
};
```

Note

This is a basic implementation of the `friends` endpoint. You can add more logic to this endpoint to suit your needs.

`[id].ts` will contain the code to update and delete a document in the friends collection:

src/pages/api/friends/\[id].ts

```ts
import type { APIRoute } from "astro";
import { app } from "../../../firebase/server";
import { getFirestore } from "firebase-admin/firestore";


const db = getFirestore(app);
const friendsRef = db.collection("friends");


export const POST: APIRoute = async ({ params, redirect, request }) => {
  const formData = await request.formData();
  const name = formData.get("name")?.toString();
  const age = formData.get("age")?.toString();
  const isBestFriend = formData.get("isBestFriend") === "on";


  if (!name || !age) {
    return new Response("Missing required fields", {
      status: 400,
    });
  }


  if (!params.id) {
    return new Response("Cannot find friend", {
      status: 404,
    });
  }


  try {
    await friendsRef.doc(params.id).update({
      name,
      age: parseInt(age),
      isBestFriend,
    });
  } catch (error) {
    return new Response("Something went wrong", {
      status: 500,
    });
  }
  return redirect("/dashboard");
};


export const DELETE: APIRoute = async ({ params, redirect }) => {
  if (!params.id) {
    return new Response("Cannot find friend", {
      status: 404,
    });
  }


  try {
    await friendsRef.doc(params.id).delete();
  } catch (error) {
    return new Response("Something went wrong", {
      status: 500,
    });
  }
  return redirect("/dashboard");
};
```

Note

This is a basic implementation of the `friends/:id` endpoint. You can add more logic to this endpoint to suit your needs.

After creating server endpoints for Firestore, your project directory should now include these new files:

* src

  * env.d.ts

  * firebase

    * client.ts
    * server.ts

  * pages

    * api

      * friends

        * **index.ts**
        * **\[id].ts**

* .env

* astro.config.mjs

* package.json

### Creating pages

[Section titled “Creating pages”](#creating-pages-1)

Create the pages that will use the Firestore endpoints:

* `src/pages/add.astro` - will contain a form to add a new friend.
* `src/pages/edit/[id].astro` - will contain a form to edit a friend and a button to delete a friend.
* `src/pages/friend/[id].astro` - will contain the details of a friend.
* `src/pages/dashboard.astro` - will display a list of friends.

#### Add a new record

[Section titled “Add a new record”](#add-a-new-record)

The example `src/pages/add.astro` below includes a form that will send a `POST` request to the `/api/friends` endpoint. This endpoint will create a new friend using the data from the form and then will redirect the user to the `/dashboard` page.

src/pages/add.astro

```astro
---
import Layout from "../layouts/Layout.astro";
---


<Layout title="Add a new friend">
  <h1>Add a new friend</h1>
  <form method="post" action="/api/friends">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" />
    <label for="age">Age</label>
    <input type="number" id="age" name="age" />
    <label for="isBestFriend">Is best friend?</label>
    <input type="checkbox" id="isBestFriend" name="isBestFriend" />
    <button type="submit">Add friend</button>
  </form>
</Layout>
```

#### Edit or Delete a record

[Section titled “Edit or Delete a record”](#edit-or-delete-a-record)

`src/pages/edit/[id].astro` will contain a form to edit a friend data and a button to delete a friend. On submit, this page will send a `POST` request to the `/api/friends/:id` endpoint to update a friend data.

If the user clicks the delete button, this page will send a `DELETE` request to the `/api/friends/:id` endpoint to delete a friend.

src/pages/edit/\[id].astro

```astro
---
import Layout from "../../layouts/Layout.astro";
import { app } from "../../firebase/server";
import { getFirestore } from "firebase-admin/firestore";


interface Friend {
  name: string;
  age: number;
  isBestFriend: boolean;
}


const { id } = Astro.params;


if (!id) {
  return Astro.redirect("/404");
}


const db = getFirestore(app);
const friendsRef = db.collection("friends");
const friendSnapshot = await friendsRef.doc(id).get();


if (!friendSnapshot.exists) {
  return Astro.redirect("/404");
}


const friend = friendSnapshot.data() as Friend;
---


<Layout title="Edit {friend.name}">
  <h1>Edit {friend.name}</h1>
  <p>Here you can edit or delete your friend's data.</p>
  <form method="post" action={`/api/friends/${id}`}>
    <label for="name">Name</label>
    <input type="text" id="name" name="name" value={friend.name} />
    <label for="age">Age</label>
    <input type="number" id="age" name="age" value={friend.age} />
    <label for="isBestFriend">Is best friend?</label>
    <input
      type="checkbox"
      id="isBestFriend"
      name="isBestFriend"
      checked={friend.isBestFriend}
    />
    <button type="submit">Edit friend</button>
  </form>
  <button type="button" id="delete-document">Delete</button>
</Layout>
<script>
  const deleteButton = document.getElementById(
    "delete-document"
  ) as HTMLButtonElement;
  const url = document.querySelector("form")?.getAttribute("action") as string;
  deleteButton.addEventListener("click", async () => {
    const response = await fetch(url, {
      method: "DELETE",
    });
    if (response.redirected) {
      window.location.assign(response.url);
    }
  });
</script>
```

#### Display an individual record

[Section titled “Display an individual record”](#display-an-individual-record)

`src/pages/friend/[id].astro` will display the details of a friend.

src/pages/friend/\[id].astro

```astro
---
import Layout from "../../layouts/Layout.astro";
import { app } from "../../firebase/server";
import { getFirestore } from "firebase-admin/firestore";


interface Friend {
  name: string;
  age: number;
  isBestFriend: boolean;
}


const { id } = Astro.params;


if (!id) {
  return Astro.redirect("/404");
}


const db = getFirestore(app);
const friendsRef = db.collection("friends");
const friendSnapshot = await friendsRef.doc(id).get();


if (!friendSnapshot.exists) {
  return Astro.redirect("/404");
}


const friend = friendSnapshot.data() as Friend;
---


<Layout title={friend.name}>
  <h1>{friend.name}</h1>
  <p>Age: {friend.age}</p>
  <p>Is best friend: {friend.isBestFriend ? "Yes" : "No"}</p>
</Layout>
```

#### Display a list of records with an edit button

[Section titled “Display a list of records with an edit button”](#display-a-list-of-records-with-an-edit-button)

Finally, `src/pages/dashboard.astro` will display a list of friends. Each friend will have a link to their details page and an edit button that will redirect the user to the edit page.

src/pages/dashboard.astro

```astro
---
import { app } from "../firebase/server";
import { getFirestore } from "firebase-admin/firestore";
import Layout from "../layouts/Layout.astro";


interface Friend {
  id: string;
  name: string;
  age: number;
  isBestFriend: boolean;
}


const db = getFirestore(app);
const friendsRef = db.collection("friends");
const friendsSnapshot = await friendsRef.get();
const friends = friendsSnapshot.docs.map((doc) => ({
  id: doc.id,
  ...doc.data(),
})) as Friend[];
---


<Layout title="My friends">
  <h1>Friends</h1>
  <ul>
    {
      friends.map((friend) => (
        <li>
          <a href={`/friend/${friend.id}`}>{friend.name}</a>
          <span>({friend.age})</span>
          <strong>{friend.isBestFriend ? "Bestie" : "Friend"}</strong>
          <a href={`/edit/${friend.id}`}>Edit</a>
        </li>
      ))
    }
  </ul>
</Layout>
```

After creating all the pages, you should have the following file structure:

* src

  * env.d.ts

  * firebase

    * client.ts
    * server.ts

  * pages

    * dashboard.astro

    * add.astro

    * edit

      * \[id].astro

    * friend

      * \[id].astro

    * api

      * friends

        * index.ts
        * \[id].ts

* .env

* astro.config.mjs

* package.json

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Astro and Firebase SSR app example](https://github.com/kevinzunigacuellar/astro-firebase)
* [Using Firebase Realtime Database in Astro with Vue: A Step-by-Step Guide](https://www.launchfa.st/blog/vue-astro-firebase-realtime-database)

# Neon Postgres & Astro

> Add a serverless Postgres database to your Astro project with Neon

[Neon](https://neon.tech) is a fully managed serverless Postgres database. It separates storage and compute to offer autoscaling, branching, and bottomless storage.

## Adding Neon to your Astro project

[Section titled “Adding Neon to your Astro project”](#adding-neon-to-your-astro-project)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A [Neon](https://console.neon.tech/signup) account with a created project
* Neon database connection string
* An Astro project with [on-demand rendering (SSR)](/en/guides/on-demand-rendering/) enabled

### Environment configuration

[Section titled “Environment configuration”](#environment-configuration)

To use Neon with Astro, you will need to set a Neon environment variable. Create or edit the `.env` file in your project root, and add the following code, replacing your own project details:

.env

```ini
NEON_DATABASE_URL="postgresql://<user>:<password>@<endpoint_hostname>.neon.tech:<port>/<dbname>?sslmode=require"
```

For better TypeScript support, define environment variables in a `src/env.d.ts` file:

src/env.d.ts

```typescript
interface ImportMetaEnv {
  readonly NEON_DATABASE_URL: string;
}


interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

Learn more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Install the `@neondatabase/serverless` package to connect to Neon:

```bash
npm install @neondatabase/serverless
```

### Creating a Neon client

[Section titled “Creating a Neon client”](#creating-a-neon-client)

Create a new file `src/lib/neon.ts` with the following code to initialize your Neon client:

src/lib/neon.ts

```typescript
import { neon } from '@neondatabase/serverless';


export const sql = neon(import.meta.env.NEON_DATABASE_URL);
```

## Querying your Neon database

[Section titled “Querying your Neon database”](#querying-your-neon-database)

You can now use the Neon client to query your database from any `.astro` component. The following example fetches the current time from the Postgres database:

src/pages/index.astro

```astro
---
import { sql } from '../lib/neon';


const response =  await  sql`SELECT NOW() as current_time`;
const currentTime = response[0].current_time;
---


<h1>Current Time</h1>
<p>The time is: {currentTime}</p>
```

## Database branching with Neon

[Section titled “Database branching with Neon”](#database-branching-with-neon)

Neon’s branching feature lets you create copies of your database for development or testing. Use this in your Astro project by creating different environment variables for each branch:

.env.development

```ini
NEON_DATABASE_URL=your_development_branch_url
```

.env.production

```ini
NEON_DATABASE_URL=your_production_branch_url
```

## Resources

[Section titled “Resources”](#resources)

* [Neon documentation](https://neon.tech/docs/introduction)
* [Neon serverless driver GitHub](https://github.com/neondatabase/serverless)
* [Connect an Astro site or application to Neon Postgres](https://neon.tech/docs/guides/astro)

# Prisma Postgres & Astro

> Add a serverless Postgres database to your Astro project with Prisma Postgres

[Prisma Postgres](https://www.prisma.io/) is a fully managed, serverless Postgres database built for modern web apps.

## Connect via Prisma ORM (Recommended)

[Section titled “Connect via Prisma ORM (Recommended)”](#connect-via-prisma-orm-recommended)

[Prisma ORM](https://www.prisma.io/orm) is the recommended way to connect to your Prisma Postgres database. It provides type-safe queries, migrations, and global performance.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An Astro project with an adapter installed to enable [on-demand rendering (SSR)](/en/guides/on-demand-rendering/).

### Install dependencies and initialize Prisma

[Section titled “Install dependencies and initialize Prisma”](#install-dependencies-and-initialize-prisma)

Run the following commands to install the necessary Prisma dependencies:

```bash
npm install prisma tsx --save-dev
npm install @prisma/extension-accelerate @prisma/client
```

Once installed, initialize Prisma in your project with the following command:

```bash
npx prisma init --db --output ../src/generated/prisma
```

You’ll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database, like “My Astro Project.”

This will create:

* A `prisma/` directory with a `schema.prisma` file
* A `.env` file with a `DATABASE_URL` already set

### Define a Model

[Section titled “Define a Model”](#define-a-model)

Even if you don’t need any specific data models yet, Prisma requires at least one model in the schema in order to generate a client and apply migrations.

The following example defines a `Post` model as a placeholder. Add the model to your schema to get started. You can safely delete or replace it later with models that reflect your actual data.

Update the generator provider from `prisma-client-js` to `prisma-client` in your `prisma/schema.prisma` file:

prisma/schema.prisma

```diff
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}


datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}


+model Post {
  +id        Int     @id @default(autoincrement())
  +title     String
  +content   String?
  +published Boolean @default(false)
+}
```

Learn more about configuring your Prisma ORM setup in the [Prisma schema reference](https://www.prisma.io/docs/concepts/components/prisma-schema).

### Generate migration files

[Section titled “Generate migration files”](#generate-migration-files)

Run the following command to create the database tables and generate the Prisma Client from your schema. This will also create a `prisma/migrations/` directory with migration history files.

```bash
npx prisma migrate dev --name init
```

### Create a Prisma Client

[Section titled “Create a Prisma Client”](#create-a-prisma-client)

Inside of `/src/lib`, create a `prisma.ts` file. This file will initialize and export your Prisma Client instance so you can query your database throughout your Astro project.

src/lib/prisma.ts

```typescript
import { PrismaClient } from "../generated/prisma/client";
import { withAccelerate } from "@prisma/extension-accelerate";


const prisma = new PrismaClient({
  datasourceUrl: import.meta.env.DATABASE_URL,
}).$extends(withAccelerate());


export default prisma;
```

### Querying and displaying data

[Section titled “Querying and displaying data”](#querying-and-displaying-data)

The following example shows fetching only your published posts with the Prisma Client sorted by `id`, and then displaying titles and post content in your Astro template:

src/pages/posts.astro

```astro
---
import prisma from '../lib/prisma';


const posts = await prisma.post.findMany({
  where: { published: true },
  orderBy: { id: 'desc' }
});
---


<html>
  <head>
    <title>Published Posts</title>
  </head>
  <body>
    <h1>Published Posts</h1>
    <ul>
      {posts.map((post) => (
        <li>
          <h2>{post.title}</h2>
          {post.content && <p>{post.content}</p>}
        </li>
      ))}
    </ul>
  </body>
</html>
```

It is best practice to handle queries in an API route. For more information on how to use Prisma ORM in your Astro project, see the [Astro + Prisma ORM Guide](https://www.prisma.io/docs/guides/astro).

## Direct TCP connection

[Section titled “Direct TCP connection”](#direct-tcp-connection)

To connect to Prisma Postgres via direct TCP, you can create a direct connection string in your Prisma Console. This allows you to connect any other ORM, database library, or tool of your choice.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

* A [Prisma Postgres](https://pris.ly/ppg) database with a TCP enabled connection string

### Install dependencies

[Section titled “Install dependencies”](#install-dependencies)

This example will make a direct TCP connection using [`pg`, a PostgreSQL client for Node.js](https://github.com/brianc/node-postgres).

Run the following command to install the `pg` package:

```bash
npm install pg
```

### Query your database client

[Section titled “Query your database client”](#query-your-database-client)

Provide your connection string to the `pg` client to communicate with your SQL server and fetch data from your database.

The following example of creating a table and inserting data can be used to validate your query URL and TCP connection:

src/pages/index.astro

```astro
---
import { Client } from 'pg';
const client = new Client({
  connectionString: import.meta.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});
await client.connect();


await client.query(`
  CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT UNIQUE,
    content TEXT
  );


  INSERT INTO posts (title, content)
  VALUES ('Hello', 'World')
  ON CONFLICT (title) DO NOTHING;
`);


const { rows } = await client.query('SELECT * FROM posts');
await client.end();
---


<h1>Posts</h1>
<p>{rows[0].title}: {rows[0].content}</p>
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Astro + Prisma ORM Guide](https://www.prisma.io/docs/guides/astro)

# Monitor your Astro Site with Sentry

> How to monitor your Astro site with Sentry

[Sentry](https://sentry.io) offers a comprehensive application monitoring and error tracking service designed to help developers identify, diagnose, and resolve issues in real-time.

Read more on our blog about [Astro’s partnership with Sentry](https://astro.build/blog/sentry-official-monitoring-partner/) and Sentry’s Spotlight dev toolbar app that brings a rich debug overlay into your Astro development environment. Spotlight shows errors, traces, and important context right in your browser during local development.

Sentry’s Astro SDK enables automatic reporting of errors and tracing data in your Astro application.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

A full list of prerequisites can be found in [the Sentry guide for Astro](https://docs.sentry.io/platforms/javascript/guides/astro/#prerequisites).

## Install

[Section titled “Install”](#install)

Sentry captures data by using an SDK within your application’s runtime.

Install the SDK by running the following command for the package manager of your choice in the Astro CLI:

* npm

  ```shell
  npx astro add @sentry/astro
  ```

* pnpm

  ```shell
  pnpm astro add @sentry/astro
  ```

* Yarn

  ```shell
  yarn astro add @sentry/astro
  ```

The astro CLI installs the SDK package and adds the Sentry integration to your `astro.config.mjs` file.

## Configure

[Section titled “Configure”](#configure)

To configure the Sentry integration, you need to provide the following credentials in your `astro.config.mjs` file.

1. **Client key (DSN)** - You can find the DSN in your Sentry project settings under *Client keys (DSN)*.
2. **Project name** - You can find the project name in your Sentry project settings under *General settings*.
3. **Auth token** - You can create an auth token in your Sentry organization settings under *Auth tokens*.

Note

If you are creating a new Sentry project, select Astro as your platform to get all the necessary information to configure the SDK.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import sentry from '@sentry/astro';


export default defineConfig({
  integrations: [
    +sentry({
+      dsn: 'https://examplePublicKey@o0.ingest.sentry.io/0',
+      sourceMapsUploadOptions: {
+        project: 'example-project',
+        authToken: process.env.SENTRY_AUTH_TOKEN,
+      },
+    }),
  ],
});
```

Once you’ve configured your `sourceMapsUploadOptions` and added your `dsn`, the SDK will automatically capture and send errors and performance events to Sentry.

## Test your setup

[Section titled “Test your setup”](#test-your-setup)

Add the following `<button>` element to one of your `.astro` pages. This will allow you to manually trigger an error so you can test the error reporting process.

src/pages/index.astro

```astro
<button onclick="throw new Error('This is a test error')">Throw test error</button>
```

To view and resolve the recorded error, log into [sentry.io](https://sentry.io/) and open your project.

# Supabase & Astro

> Add a backend to your project with Supabase

[Supabase](https://supabase.com/) is an open source Firebase alternative. It provides a Postgres database, authentication, edge functions, realtime subscriptions, and storage.

## Initializing Supabase in Astro

[Section titled “Initializing Supabase in Astro”](#initializing-supabase-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A Supabase project. If you don’t have one, you can sign up for free at [supabase.com](https://supabase.com/) and create a new project.

* An Astro project with [`output: 'server'` for on-demand rendering](/en/guides/on-demand-rendering/) enabled.

* Supabase credentials for your project. You can find these in the **Settings > API** tab of your Supabase project.

  * `SUPABASE_URL`: The URL of your Supabase project.
  * `SUPABASE_ANON_KEY`: The anonymous key for your Supabase project.

### Adding Supabase credentials

[Section titled “Adding Supabase credentials”](#adding-supabase-credentials)

To add your Supabase credentials to your Astro project, add the following to your `.env` file:

.env

```ini
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
```

Now, these environment variables are available in your project.

If you would like to have IntelliSense for your environment variables, edit or create the `env.d.ts` in your `src/` directory and add the following:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly SUPABASE_URL: string
  readonly SUPABASE_ANON_KEY: string
}


interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

Tip

Read more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your project should now include these files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect to Supabase, you will need to install `@supabase/supabase-js` in your project.

* npm

  ```shell
  npm install @supabase/supabase-js
  ```

* pnpm

  ```shell
  pnpm add @supabase/supabase-js
  ```

* Yarn

  ```shell
  yarn add @supabase/supabase-js
  ```

Next, create a folder named `lib` in your `src/` directory. This is where you will add your Supabase client.

In `supabase.ts`, add the following to initialize your Supabase client:

src/lib/supabase.ts

```ts
import { createClient } from "@supabase/supabase-js";


export const supabase = createClient(
  import.meta.env.SUPABASE_URL,
  import.meta.env.SUPABASE_ANON_KEY,
);
```

Now, your project should include these files:

* src/

  * lib/

    * **supabase.ts**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

## Adding authentication with Supabase

[Section titled “Adding authentication with Supabase”](#adding-authentication-with-supabase)

Supabase provides authentication out of the box. It supports email/password authentication and OAuth authentication with many providers including GitHub, Google, and several others.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

* An Astro project [initialized with Supabase](#initializing-supabase-in-astro).
* A Supabase project with email/password authentication enabled. You can enable this in the **Authentication > Providers** tab of your Supabase project.

### Creating auth server endpoints

[Section titled “Creating auth server endpoints”](#creating-auth-server-endpoints)

To add authentication to your project, you will need to create a few server endpoints. These endpoints will be used to register, sign in, and sign out users.

* `POST /api/auth/register`: to register a new user.
* `POST /api/auth/signin`: to sign in a user.
* `GET /api/auth/signout`: to sign out a user.

Create these endpoints in the `src/pages/api/auth` directory of your project. If you are using `static` rendering mode, you must specify `export const prerender = false` at the top of each file to render these endpoints on demand. Your project should now include these new files:

* src/

  * lib/

    * supabase.ts

  * pages/

    * api/

      * auth/

        * **signin.ts**
        * **signout.ts**
        * **register.ts**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

`register.ts` creates a new user in Supabase. It accepts a `POST` request with the an email and password. It then uses the Supabase SDK to create a new user.

src/pages/api/auth/register.ts

```ts
// With `output: 'static'` configured:
// export const prerender = false;
import type { APIRoute } from "astro";
import { supabase } from "../../../lib/supabase";


export const POST: APIRoute = async ({ request, redirect }) => {
  const formData = await request.formData();
  const email = formData.get("email")?.toString();
  const password = formData.get("password")?.toString();


  if (!email || !password) {
    return new Response("Email and password are required", { status: 400 });
  }


  const { error } = await supabase.auth.signUp({
    email,
    password,
  });


  if (error) {
    return new Response(error.message, { status: 500 });
  }


  return redirect("/signin");
};
```

`signin.ts` signs in a user. It accepts a `POST` request with the an email and password. It then uses the Supabase SDK to sign in the user.

src/pages/api/auth/signin.ts

```ts
// With `output: 'static'` configured:
// export const prerender = false;
import type { APIRoute } from "astro";
import { supabase } from "../../../lib/supabase";


export const POST: APIRoute = async ({ request, cookies, redirect }) => {
  const formData = await request.formData();
  const email = formData.get("email")?.toString();
  const password = formData.get("password")?.toString();


  if (!email || !password) {
    return new Response("Email and password are required", { status: 400 });
  }


  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  });


  if (error) {
    return new Response(error.message, { status: 500 });
  }


  const { access_token, refresh_token } = data.session;
  cookies.set("sb-access-token", access_token, {
    path: "/",
  });
  cookies.set("sb-refresh-token", refresh_token, {
    path: "/",
  });
  return redirect("/dashboard");
};
```

`signout.ts` signs out a user. It accepts a `GET` request and removes the user’s access and refresh tokens.

src/pages/api/auth/signout.ts

```ts
// With `output: 'static'` configured:
// export const prerender = false;
import type { APIRoute } from "astro";


export const GET: APIRoute = async ({ cookies, redirect }) => {
  cookies.delete("sb-access-token", { path: "/" });
  cookies.delete("sb-refresh-token", { path: "/" });
  return redirect("/signin");
};
```

### Creating auth pages

[Section titled “Creating auth pages”](#creating-auth-pages)

Now that you have created your server endpoints, create the pages that will use them.

* `src/pages/register`: contains a form to register a new user.
* `src/pages/signin`: contains a form to sign in a user.
* `src/pages/dashboard`: contains a page that is only accessible to authenticated users.

Create these pages in the `src/pages` directory. Your project should now include these new files:

* src/

  * lib/

    * supabase.ts

  * pages/

    * api/

      * auth/

        * signin.ts
        * signout.ts
        * register.ts

    * **register.astro**

    * **signin.astro**

    * **dashboard.astro**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

`register.astro` contains a form to register a new user. It accepts an email and password and sends a `POST` request to `/api/auth/register`.

src/pages/register.astro

```astro
---
import Layout from "../layouts/Layout.astro";
---


<Layout title="Register">
  <h1>Register</h1>
  <p>Already have an account? <a href="/signin">Sign in</a></p>
  <form action="/api/auth/register" method="post">
    <label for="email">Email</label>
    <input type="email" name="email" id="email" />
    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <button type="submit">Register</button>
  </form>
</Layout>
```

`signin.astro` contains a form to sign in a user. It accepts an email and password and sends a `POST` request to `/api/auth/signin`. It also checks for the presence of the access and refresh tokens. If they are present, it redirects to the dashboard.

src/pages/signin.astro

```astro
---
import Layout from "../layouts/Layout.astro";


const { cookies, redirect } = Astro;


const accessToken = cookies.get("sb-access-token");
const refreshToken = cookies.get("sb-refresh-token");


if (accessToken && refreshToken) {
  return redirect("/dashboard");
}
---


<Layout title="Sign in">
  <h1>Sign in</h1>
  <p>New here? <a href="/register">Create an account</a></p>
  <form action="/api/auth/signin" method="post">
    <label for="email">Email</label>
    <input type="email" name="email" id="email" />
    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <button type="submit">Login</button>
  </form>
</Layout>
```

`dashboard.astro` contains a page that is only accessible to authenticated users. It checks for the presence of the access and refresh tokens. If they are not present or are invalid, it redirects to the sign in page.

src/pages/dashboard.astro

```astro
---
import Layout from "../layouts/Layout.astro";
import { supabase } from "../lib/supabase";


const accessToken = Astro.cookies.get("sb-access-token");
const refreshToken = Astro.cookies.get("sb-refresh-token");


if (!accessToken || !refreshToken) {
  return Astro.redirect("/signin");
}


let session;
try {
  session = await supabase.auth.setSession({
    refresh_token: refreshToken.value,
    access_token: accessToken.value,
  });
  if (session.error) {
    Astro.cookies.delete("sb-access-token", {
      path: "/",
    });
    Astro.cookies.delete("sb-refresh-token", {
      path: "/",
    });
    return Astro.redirect("/signin");
  }
} catch (error) {
  Astro.cookies.delete("sb-access-token", {
    path: "/",
  });
  Astro.cookies.delete("sb-refresh-token", {
    path: "/",
  });
  return Astro.redirect("/signin");
}


const email = session.data.user?.email;
---
<Layout title="dashboard">
  <h1>Welcome {email}</h1>
  <p>We are happy to see you here</p>
  <form action="/api/auth/signout">
    <button type="submit">Sign out</button>
  </form>
</Layout>
```

### Adding OAuth authentication

[Section titled “Adding OAuth authentication”](#adding-oauth-authentication)

To add OAuth authentication to your project, you will need to edit your Supabase client to enable authentication flow with `"pkce"`. You can read more about authentication flows in the [Supabase documentation](https://supabase.com/docs/guides/auth/server-side-rendering#understanding-the-authentication-flow).

src/lib/supabase.ts

```diff
import { createClient } from "@supabase/supabase-js";


export const supabase = createClient(
  import.meta.env.SUPABASE_URL,
  import.meta.env.SUPABASE_ANON_KEY,
  {
    auth: {
      flowType: "pkce",
    },
  },
);
```

Next, in the Supabase dashboard, enable the OAuth provider you would like to use. You can find the list of supported providers in the **Authentication > Providers** tab of your Supabase project.

The following example uses GitHub as the OAuth provider. To connect your project to GitHub, follow the steps in the [Supabase documentation](https://supabase.com/docs/guides/auth/social-login/auth-github).

Then, create a new server endpoint to handle the OAuth callback at `src/pages/api/auth/callback.ts`. This endpoint will be used to exchange the OAuth code for an access and refresh token.

src/pages/api/auth/callback.ts

```ts
import type { APIRoute } from "astro";
import { supabase } from "../../../lib/supabase";


export const GET: APIRoute = async ({ url, cookies, redirect }) => {
  const authCode = url.searchParams.get("code");


  if (!authCode) {
    return new Response("No code provided", { status: 400 });
  }


  const { data, error } = await supabase.auth.exchangeCodeForSession(authCode);


  if (error) {
    return new Response(error.message, { status: 500 });
  }


  const { access_token, refresh_token } = data.session;


  cookies.set("sb-access-token", access_token, {
    path: "/",
  });
  cookies.set("sb-refresh-token", refresh_token, {
    path: "/",
  });


  return redirect("/dashboard");
};
```

Next, edit the sign in page to include a new button to sign in with the OAuth provider. This button should send a `POST` request to `/api/auth/signin` with the `provider` set to the name of the OAuth provider.

src/pages/signin.astro

```diff
---
import Layout from "../layouts/Layout.astro";


const { cookies, redirect } = Astro;


const accessToken = cookies.get("sb-access-token");
const refreshToken = cookies.get("sb-refresh-token");


if (accessToken && refreshToken) {
  return redirect("/dashboard");
}
---


<Layout title="Sign in">
  <h1>Sign in</h1>
  <p>New here? <a href="/register">Create an account</a></p>
  <form action="/api/auth/signin" method="post">
    <label for="email">Email</label>
    <input type="email" name="email" id="email" />
    <label for="password">Password</label>
    <input type="password" name="password" id="password" />
    <button type="submit">Login</button>
    <button value="github" name="provider" type="submit">Sign in with GitHub</button>
  </form>
</Layout>
```

Finally, edit the sign in server endpoint to handle the OAuth provider. If the `provider` is present, it will redirect to the OAuth provider. Otherwise, it will sign in the user with the email and password.

src/pages/api/auth/signin.ts

```diff
import type { APIRoute } from "astro";
import { supabase } from "../../../lib/supabase";
import type { Provider } from "@supabase/supabase-js";


export const POST: APIRoute = async ({ request, cookies, redirect }) => {
  const formData = await request.formData();
  const email = formData.get("email")?.toString();
  const password = formData.get("password")?.toString();
  const provider = formData.get("provider")?.toString();


  const validProviders = ["google", "github", "discord"];


  if (provider && validProviders.includes(provider)) {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: provider as Provider,
      options: {
        redirectTo: "http://localhost:4321/api/auth/callback"
      },
    });


    if (error) {
      return new Response(error.message, { status: 500 });
    }


    return redirect(data.url);
  }


  if (!email || !password) {
    return new Response("Email and password are required", { status: 400 });
  }


  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  });


  if (error) {
    return new Response(error.message, { status: 500 });
  }


  const { access_token, refresh_token } = data.session;
  cookies.set("sb-access-token", access_token, {
    path: "/",
  });
  cookies.set("sb-refresh-token", refresh_token, {
    path: "/",
  });
  return redirect("/dashboard");
};
```

After creating the OAuth callback endpoint and editing the sign in page and server endpoint, your project should have the following file structure:

* src/

  * lib/

    * supabase.ts

  * pages/

    * api/

      * auth/

        * signin.ts
        * signout.ts
        * register.ts
        * callback.ts

    * register.astro

    * signin.astro

    * dashboard.astro

  * env.d.ts

* .env

* astro.config.mjs

* package.json

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Getting into the holiday spirit with Astro, React, and Supabase](https://www.aleksandra.codes/astro-supabase)
* [Astro and Supabase auth demo](https://github.com/kevinzunigacuellar/astro-supabase)

# Turso & Astro

> Build locally with a SQLite file and deploy globally using Turso.

[Turso](https://turso.tech) is a distributed database built on libSQL, a fork of SQLite. It is optimized for low query latency, making it suitable for global applications.

## Initializing Turso in Astro

[Section titled “Initializing Turso in Astro”](#initializing-turso-in-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* The [Turso CLI](https://docs.turso.tech/cli/introduction) installed and signed in
* A [Turso](https://turso.tech) Database with schema
* Your Database URL
* An Access Token

### Configure environment variables

[Section titled “Configure environment variables”](#configure-environment-variables)

Obtain your database URL using the following command:

```bash
turso db show <database-name> --url
```

Create an auth token for the database:

```bash
turso db tokens create <database-name>
```

Add the output from both commands above into your `.env` file at the root of your project. If this file does not exist, create one.

.env

```ini
TURSO_DATABASE_URL=libsql://...
TURSO_AUTH_TOKEN=
```

Caution

Do not use the `PUBLIC_` prefix when creating these private [environment variables](/en/guides/environment-variables/). This will expose these values on the client.

### Install LibSQL Client

[Section titled “Install LibSQL Client”](#install-libsql-client)

Install the `@libsql/client` to connect Turso to Astro:

* npm

  ```shell
  npm install @libsql/client
  ```

* pnpm

  ```shell
  pnpm add @libsql/client
  ```

* Yarn

  ```shell
  yarn add @libsql/client
  ```

### Initialize a new client

[Section titled “Initialize a new client”](#initialize-a-new-client)

Create a file `turso.ts` in the `src` folder and invoke `createClient`, passing it `TURSO_DATABASE_URL` and `TURSO_AUTH_TOKEN`:

src/turso.ts

```ts
import { createClient } from "@libsql/client/web";


export const turso = createClient({
  url: import.meta.env.TURSO_DATABASE_URL,
  authToken: import.meta.env.TURSO_AUTH_TOKEN,
});
```

## Querying your database

[Section titled “Querying your database”](#querying-your-database)

To access information from your database, import `turso` and [execute a SQL query](https://docs.turso.tech/sdk/ts/reference#simple-query) inside any `.astro` component.

The following example fetches all `posts` from your table, then displays a list of titles in a `<BlogIndex />` component:

src/components/BlogIndex.astro

```astro
---
import { turso } from '../turso'


const { rows } = await turso.execute('SELECT * FROM posts')
---


<ul>
  {rows.map((post) => (
    <li>{post.title}</li>
  ))}
</ul>
```

### SQL Placeholders

[Section titled “SQL Placeholders”](#sql-placeholders)

The `execute()` method can take [an object to pass variables to the SQL statement](https://docs.turso.tech/sdk/ts/reference#placeholders), such as `slug`, or pagination.

The following example fetches a single entry from the `posts` table `WHERE` the `slug` is the retrieved value from `Astro.params`, then displays the title of the post.

src/pages/index.astro

```astro
---
import { turso } from '../turso'


const { slug } = Astro.params


const { rows } = await turso.execute({
  sql: 'SELECT * FROM posts WHERE slug = ?',
  args: [slug!]
})
---


<h1>{rows[0].title}</h1>
```

## Turso Resources

[Section titled “Turso Resources”](#turso-resources)

* [Turso Docs](https://docs.turso.tech)
* [Turso on GitHub](https://github.com/tursodatabase)
* [Using Turso to serve a Server-side Rendered Astro blog’s content](https://blog.turso.tech/using-turso-to-serve-a-server-side-rendered-astro-blogs-content-58caa6188bd5)

# Xata & Astro

> Add a serverless database with full-text search to your project with Xata

[Xata](https://xata.io) is a **Serverless Data Platform** that combines the features of a relational database, a search engine, and an analytics engine by exposing a single consistent REST API.

## Adding a database with Xata

[Section titled “Adding a database with Xata”](#adding-a-database-with-xata)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A [Xata](https://app.xata.io/signin) account with a created database. (You can use the sample database from the Web UI.)
* An Access Token (`XATA_API_KEY`).
* Your Database URL.

After you update and initialize the [Xata CLI](https://xata.io/docs/getting-started/installation), you will have your API token in your `.env` file and database URL defined.

By the end of the setup, you should have:

.env

```ini
XATA_API_KEY=hash_key


# Xata branch that will be used
# if there's not a xata branch with
# the same name as your git branch
XATA_BRANCH=main
```

And the `databaseURL` defined:

.xatarc

```ini
{
  "databaseUrl": "https://your-database-url"
}
```

### Environment configuration

[Section titled “Environment configuration”](#environment-configuration)

To have IntelliSense and type safety for your environment variables, edit or create the file `env.d.ts` in your `src/` directory:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly XATA_API_KEY: string;
  readonly XATA_BRANCH?: string;
}


interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

Tip

Read more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Using the code generation from the Xata CLI and choosing the TypeScript option, generated an instance of the SDK for you, with types tailored to your database schema. Additionally, `@xata.io/client` was added to your `package.json`.

Your Xata environment variables and database url were automatically pulled by the SDK instance, so there’s no more setup work needed.

Now, your project should have the following structure:

* src/

  * **xata.ts**
  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

* **.xatarc**

## Create your queries

[Section titled “Create your queries”](#create-your-queries)

To query your posts, import and use `XataClient` class in a `.astro` file. The example below queries the first 50 posts from Xata’s Sample Blog Database.

src/pages/blog/index.astro

```astro
---
import { XataClient } from '../../xata';


const xata = new XataClient({
  apiKey: import.meta.env.XATA_API_KEY,
  branch: import.meta.env.XATA_BRANCH
});


const { records } = await xata.db.Posts.getPaginated({
  pagination: {
    size: 50
  }
})
---


<ul>
  {records.map((post) => (
    <li>{post.title}</li>
  ))}
</ul>
```

It’s important to note the SDK needs to be regenerated every time your schema changes. So, avoid making changes to the generated files the Xata CLI creates because once schema updates, your changes will be overwritten.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Xata Astro Starter](https://github.com/xataio/examples/tree/main/apps/getting-started-astro)
* [Xata Docs: Quick Start Guide](https://xata.io/docs/getting-started/quickstart-astro)

# Building Astro sites with AI tools

> Resources and tips for building Astro sites with AI assistance

AI-powered editors and agentic coding tools generally have good knowledge of Astro’s core APIs and concepts. However, some may use older APIs and may not be aware of newer features or recent changes to the framework.

This guide covers how to enhance AI tools with up-to-date Astro knowledge and provides best practices for building Astro sites with AI assistance.

## Context files

[Section titled “Context files”](#context-files)

Astro provides [`llms.txt`](https://docs.astro.build/llms.txt) and [`llms-full.txt`](https://docs.astro.build/llms-full.txt) files that contains the full docs content in a format optimized for AI consumption. These are static files of the Astro Docs content in a streamlined Markdown format. Some AI tools can auto-discover these files if you provide `https://docs.astro.build` as a docs source.

While these files provide a minimal, easy-to-parse version of Astro’s documentation, they are large files that will use a lot of tokens if used directly in context and will need to be updated regularly to stay current. They are best used as a fallback when the AI tool does not have access to the latest documentation in other ways. [The MCP server](#astro-docs-mcp-server) provides more efficient access to the full documentation with real-time search capabilities, making it the preferred option when available.

## Astro Docs MCP Server

[Section titled “Astro Docs MCP Server”](#astro-docs-mcp-server)

You can ensure your AI tools have current Astro knowledge through the Astro Docs MCP (Model Context Protocol) server. This provides real-time access to the latest documentation, helping AI tools avoid outdated recommendations and ensuring they understand current best practices.

What is MCP?

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is a standardized way for AI tools to access external tools and data sources.

Unlike AI models trained on static data, the MCP server provides access to the latest Astro documentation. The server is free, open-source, and runs remotely with nothing to install locally.

The Astro Docs MCP server uses the [kapa.ai](https://www.kapa.ai/) API to maintain an up-to-date index of the Astro documentation.

### Server Details

[Section titled “Server Details”](#server-details)

* **Name**: Astro Docs
* **URL**: `https://mcp.docs.astro.build/mcp`
* **Transport**: Streamable HTTP

### Installation

[Section titled “Installation”](#installation)

The setup process varies depending on your AI development tool. You may see some tools refer to MCP servers as connectors, adapters, extensions, or plugins.

#### Manual setup

[Section titled “Manual setup”](#manual-setup)

Many tools support a common JSON configuration format for MCP servers. If there are not specific instructions for your chosen tool, you may be able to add the Astro Docs MCP server by including the following configuration in your tool’s MCP settings:

* Streamable HTTP

  mcp.json

  ```json
  {
    "mcpServers": {
      "Astro docs": {
        "type": "http",
        "url": "https://mcp.docs.astro.build/mcp"
      }
    }
  }
  ```

* Local Proxy

  mcp.json

  ```json
  {
    "mcpServers": {
      "Astro docs": {
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
      }
    }
  }
  ```

#### Claude Code CLI

[Section titled “Claude Code CLI”](#claude-code-cli)

[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) is an agentic coding tool that runs on the command line. Enabling the Astro Docs MCP server allows it to access the latest documentation while generating Astro code.

Install using the terminal command:

```shell
claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp
```

[More info on using MCP servers with Claude Code](https://docs.anthropic.com/en/docs/claude-code/mcp)

#### Claude Code GitHub Action

[Section titled “Claude Code GitHub Action”](#claude-code-github-action)

Claude Code also provides a GitHub Action that can be used to run commands in response to GitHub events. Enabling the Astro Docs MCP server allows it to access the latest documentation while answering questions in comments or generating Astro code.

You can configure it to use the Astro Docs MCP server for documentation access by adding the following to the workflow file:

.github/workflows/claude.yml

```yaml
# ...rest of your workflow configuration
- uses: anthropics/claude-code-action@beta
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    mcp_config: |
      {
        "mcpServers": {
          "astro-docs": {
            "type": "http",
            "url": "https://mcp.docs.astro.build/mcp"
          }
        }
      }
    allowed_tools: "mcp__astro-docs__search_astro_docs"
```

[More info on using MCP servers with the Claude Code GitHub Action](https://github.com/anthropics/claude-code-action?tab=readme-ov-file#using-custom-mcp-configuration)

#### Cursor

[Section titled “Cursor”](#cursor)

[Cursor](https://cursor.com) is an AI code editor. Adding the Astro Docs MCP server allows Cursor to access the latest Astro documentation while performing development tasks.

Install by clicking the button below:

[Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=Astro%20docs\&config=eyJ1cmwiOiJodHRwczovL21jcC5kb2NzLmFzdHJvLmJ1aWxkL21jcCJ9)

[More info on using MCP servers with Cursor](https://docs.cursor.com/context/mcp)

#### Visual Studio Code

[Section titled “Visual Studio Code”](#visual-studio-code)

[Visual Studio Code](https://code.visualstudio.com) supports MCP servers when using Copilot Chat. Adding the Astro Docs MCP server allows VS Code to access the latest Astro documentation when answering questions or performing coding tasks.

Install by clicking the button below:

[Add to VS Code](vscode:mcp/install?%7B%22name%22%3A%22Astro%20docs%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.docs.astro.build%2Fmcp%22%7D)

[More info on using MCP servers with VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_add-an-mcp-server)

#### Warp

[Section titled “Warp”](#warp)

[Warp](https://warp.dev) (formerly Warp Terminal) is an agent development environment built for coding with multiple AI agents. Adding the Astro Docs MCP server allows Warp to access the latest Astro documentation when answering questions or performing coding tasks.

1. Open your Warp settings and go to AI > MCP Servers > Manage MCP Servers.

2. Click “Add”.

3. Enter the following configuration. You can optionally configure the Astro MCP server to activate on startup using the `start_on_launch` flag:

   MCP Configuration

   ```json
   {
     "mcpServers": {
       "Astro docs": {
         "command": "npx",
         "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"],
         "env": {},
         "working_directory": null,
         "start_on_launch": true
       }
     }
   }
   ```

4. Click “Save”.

[More info on using MCP servers with Warp](https://docs.warp.dev/knowledge-and-collaboration/mcp)

#### Claude.ai / Claude Desktop

[Section titled “Claude.ai / Claude Desktop”](#claudeai--claude-desktop)

[Claude.ai](https://claude.ai) is a general-purpose AI assistant. Adding the Astro Docs MCP server allows it to access the latest documentation when answering Astro questions or generating Astro code.

1. Navigate to the [Claude.ai connector settings](https://claude.ai/settings/connectors).
2. Click “Add custom connector”. You may need to scroll down to find this option.
3. Enter the server URL: `https://mcp.docs.astro.build/mcp`.
4. Set the name to “Astro docs”.

[More info on using MCP servers with Claude.ai](https://support.anthropic.com/en/articles/10168395-setting-up-integrations-on-claude-ai#h_cda40ecb32)

#### Windsurf

[Section titled “Windsurf”](#windsurf)

[Windsurf](https://windsurf.com/) is an AI-powered agentic coding tool, available as editor plugins or a standalone editor. It can use the Astro Docs MCP server to access documentation while performing coding tasks.

Windsurf doesn’t support streaming HTTP, so it requires a local proxy configuration:

1. Open `~/.codeium/windsurf/mcp_config.json` in your editor.

2. Add the following configuration to your Windsurf MCP settings:

   MCP Configuration

   ```json
   {
     "mcpServers": {
       "Astro docs": {
         "command": "npx",
         "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
       }
     }
   }
   ```

3. Save the configuration and restart Windsurf.

[More info on using MCP servers with Windsurf](https://docs.windsurf.com/windsurf/cascade/mcp#mcp-config-json)

#### Gemini CLI

[Section titled “Gemini CLI”](#gemini-cli)

Gemini CLI is a command-line AI coding tool that can use the Astro Docs MCP server to access documentation while generating Astro code.

You can configure MCP servers at the global level in the `~/.gemini/settings.json` file, or in a `.gemini/settings.json` file in a project root.

.gemini/settings.json

```json
{
  "mcpServers": {
    "Astro docs": {
      "httpUrl": "https://mcp.docs.astro.build/mcp",
    }
  }
}
```

[More info on using MCP servers with Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md)

#### Zed

[Section titled “Zed”](#zed)

[Zed](https://zed.dev) supports MCP servers when using its AI capabilities. It can use the Astro Docs MCP server to access documentation while performing coding tasks.

Zed doesn’t support streaming HTTP, so it requires a local proxy configuration:

1. Open `~/.config/zed/settings.json` in your editor.

2. Add the following configuration to your Zed MCP settings:

   MCP Configuration

   ```json
   {
     "context_servers": {
       "Astro docs": {
         "command": "npx",
         "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
       }
     }
   }
   ```

3. Save the configuration.

[More info on using MCP servers with Zed](https://zed.dev/docs/ai/mcp)

#### ChatGPT

[Section titled “ChatGPT”](#chatgpt)

Limited availability

MCP server integration is only available for ChatGPT Pro, Team, and Enterprise users. The setup process is more complex than other tools.

Refer to the [OpenAI MCP documentation](https://platform.openai.com/docs/mcp#test-and-connect-your-mcp-server) for specific setup instructions.

#### Raycast

[Section titled “Raycast”](#raycast)

[Raycast](https://www.raycast.com/) can connect to MCP servers to enhance its AI capabilities. AI features such as MCP require a [Raycast Pro](https://www.raycast.com/pro) account, so ensure you have upgraded before trying to install. Adding the Astro Docs MCP server allows Raycast to access the latest Astro documentation while answering questions.

Install by clicking the button below:

[Add to Raycast](raycast://mcp/install?%7B%22name%22%3A%22Astro%20docs%22%2C%22type%22%3A%22stdio%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%20%22mcp-remote%22%2C%20%22https%3A%2F%2Fmcp.docs.astro.build%2Fmcp%22%5D%7D)

[More info on using MCP servers with Raycast](https://manual.raycast.com/model-context-protocol)

### Usage

[Section titled “Usage”](#usage)

Once configured, you can ask your AI tool questions about Astro, and it will retrieve information directly from the latest docs. Coding agents will be able to consult the latest documentation when performing coding tasks, and chatbots will be able to accurately answer questions about Astro features, APIs, and best practices.

Remember

The Astro Docs MCP server provides access to current documentation, but your AI tools are still responsible for interpretation and code generation. AI makes mistakes, so always review generated code carefully and test thoroughly.

### Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

If you encounter issues:

* Verify that your tool supports streamable HTTP transport.
* Check that the server URL is correct: `https://mcp.docs.astro.build/mcp`.
* Ensure your tool has proper internet access.
* Consult your specific tool’s MCP integration documentation.

If you are still having problems, open an issue in the [Astro Docs MCP Server repository](https://github.com/withastro/docs-mcp/issues).

## Discord AI Support

[Section titled “Discord AI Support”](#discord-ai-support)

The same technology that powers Astro’s MCP server is also available as a chatbot in the [Astro Discord](https://astro.build/chat) for self-serve support. Visit the `#support-ai` channel to ask questions about Astro or your project code in natural language. Your conversation is automatically threaded, and you can ask an unlimited number of follow-up questions.

**Conversations with the chatbot are public, and are subject to the same server rules for language and behavior as the rest of our channels**, but they are not actively visited by our volunteer support members. For assistance from the community, please create a thread in our regular `#support` channel.

## Tips for AI-Powered Astro Development

[Section titled “Tips for AI-Powered Astro Development”](#tips-for-ai-powered-astro-development)

* **Start with templates**: Rather than building from scratch, ask AI tools to start with an existing [Astro template](https://astro.build/themes/) or use `npm create astro@latest` with a template option.
* **Use `astro add` for integrations**: Ask AI tools to use `astro add` for official integrations (e.g. `astro add tailwind`, `astro add react`). For other packages, install using the command for your preferred package manager rather than editing `package.json` directly.
* **Verify current APIs**: AI tools may use outdated patterns. Ask them to check the latest documentation, especially for newer features like sessions and actions. This is also important for features that have seen significant changes since their initial launch, such as content collections, or previously experimental features that may no longer be experimental.
* **Use project rules**: If your AI tool supports it, set up project rules to enforce best practices and coding standards, such as the ones listed above.

# Scripts and event handling

> How to add client-side interactivity to Astro components using native browser JavaScript APIs.

You can send JavaScript to the browser and add functionality to your Astro components using `<script>` tags in the component template.

Scripts add interactivity to your site, such as handling events or updating content dynamically, without the need for a [UI framework](/en/guides/framework-components/) like React, Svelte, or Vue. This avoids the overhead of shipping framework JavaScript and doesn’t require you to know any additional framework to create a full-featured website or application.

## Client-Side Scripts

[Section titled “Client-Side Scripts”](#client-side-scripts)

Scripts can be used to add event listeners, send analytics data, play animations, and everything else JavaScript can do on the web.

Astro automatically enhances the HTML standard `<script>` tag with bundling, TypeScript, and more. See [how astro processes scripts](#script-processing) for more details.

src/components/ConfettiButton.astro

```astro
<button data-confetti-button>Celebrate!</button>


<script>
  // Import from npm package.
  import confetti from 'canvas-confetti';


  // Find our component DOM on the page.
  const buttons = document.querySelectorAll('[data-confetti-button]');


  // Add event listeners to fire confetti when a button is clicked.
  buttons.forEach((button) => {
    button.addEventListener('click', () => confetti());
  });
</script>
```

See [when your scripts will not be processed](#unprocessed-scripts) to troubleshoot script behavior, or to learn how to opt-out of this processing intentionally.

## Script processing

[Section titled “Script processing”](#script-processing)

By default, Astro processes `<script>` tags that contain no attributes (other than `src`) in the following ways:

* **TypeScript support:** All scripts are TypeScript by default.
* **Import bundling:** Import local files or npm modules, which will be bundled together.
* **Type Module:** Processed scripts become [`type="module"`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) automatically.
* **Deduplication:** If a component that contains a `<script>` is used multiple times on a page, the script will only be included once.
* **Automatic inlining:** If the script is small enough, Astro will inline it directly into the HTML to reduce the number of requests.

src/components/Example.astro

```astro
<script>
  // Processed! Bundled! TypeScript!
  // Importing local scripts and from npm packages works.
</script>
```

### Unprocessed scripts

[Section titled “Unprocessed scripts”](#unprocessed-scripts)

Astro will not process a `<script>` tag if it has any attribute other than `src`.

You can add the [`is:inline`](/en/reference/directives-reference/#isinline) directive to intentionally opt out of processing for a script.

src/components/InlineScript.astro

```astro
<script is:inline>
  // Will be rendered into the HTML exactly as written!
  // Not transformed: no TypeScript and no import resolution by Astro.
  // If used inside a component, this code is duplicated for each instance.
</script>
```

### Include JavaScript files on your page

[Section titled “Include JavaScript files on your page”](#include-javascript-files-on-your-page)

You may want to write your scripts as separate `.js`/`.ts` files or need to reference an external script on another server. You can do this by referencing these in a `<script>` tag’s `src` attribute.

#### Import local scripts

[Section titled “Import local scripts”](#import-local-scripts)

**When to use this:** when your script lives inside of `src/`.

Astro will process these scripts according to the [script processing rules](#script-processing).

src/components/LocalScripts.astro

```astro
<!-- relative path to script at `src/scripts/local.js` -->
<script src="../scripts/local.js"></script>


<!-- also works for local TypeScript files -->
<script src="./script-with-types.ts"></script>
```

#### Load external scripts

[Section titled “Load external scripts”](#load-external-scripts)

**When to use this:** when your JavaScript file lives inside of `public/` or on a CDN.

To load scripts outside of your project’s `src/` folder, include the `is:inline` directive. This approach skips the JavaScript processing, bundling, and optimizations that are provided by Astro when you import scripts as described above.

src/components/ExternalScripts.astro

```astro
<!-- absolute path to a script at `public/my-script.js` -->
<script is:inline src="/my-script.js"></script>


<!-- full URL to a script on a remote server -->
<script is:inline src="https://my-analytics.com/script.js"></script>
```

## Common script patterns

[Section titled “Common script patterns”](#common-script-patterns)

### Handle `onclick` and other events

[Section titled “Handle onclick and other events”](#handle-onclick-and-other-events)

Some UI frameworks use custom syntax for event handling like `onClick={...}` (React/Preact) or `@click="..."` (Vue). Astro follows standard HTML more closely and does not use custom syntax for events.

Instead, you can use [`addEventListener`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) in a `<script>` tag to handle user interactions.

src/components/AlertButton.astro

```astro
<button class="alert">Click me!</button>


<script>
  // Find all buttons with the `alert` class on the page.
  const buttons = document.querySelectorAll('button.alert');


  // Handle clicks on each button.
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      alert('Button was clicked!');
    });
  });
</script>
```

If you have multiple `<AlertButton />` components on a page, Astro will not run the script multiple times. Scripts are bundled and only included once per page. Using `querySelectorAll` ensures that this script attaches the event listener to every button with the `alert` class found on the page.

### Web components with custom elements

[Section titled “Web components with custom elements”](#web-components-with-custom-elements)

You can create your own HTML elements with custom behavior using the Web Components standard. Defining a [custom element](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) in a `.astro` component allows you to build interactive components without needing a UI framework library.

In this example, we define a new `<astro-heart>` HTML element that tracks how many times you click the heart button and updates the `<span>` with the latest count.

src/components/AstroHeart.astro

```astro
<!-- Wrap the component elements in our custom element “astro-heart”. -->
<astro-heart>
  <button aria-label="Heart">💜</button> × <span>0</span>
</astro-heart>


<script>
  // Define the behaviour for our new type of HTML element.
  class AstroHeart extends HTMLElement {
    connectedCallback() {
      let count = 0;


      const heartButton = this.querySelector('button');
      const countSpan = this.querySelector('span');


      // Each time the button is clicked, update the count.
      heartButton.addEventListener('click', () => {
        count++;
        countSpan.textContent = count.toString();
      });
    }
  }


  // Tell the browser to use our AstroHeart class for <astro-heart> elements.
  customElements.define('astro-heart', AstroHeart);
</script>
```

There are two advantages to using a custom element here:

1. Instead of searching the whole page using `document.querySelector()`, you can use `this.querySelector()`, which only searches within the current custom element instance. This makes it easier to work with only the children of one component instance at a time.

2. Although a `<script>` only runs once, the browser will run our custom element’s `connectedCallback()` method each time it finds `<astro-heart>` on the page. This means you can safely write code for one component at a time, even if you intend to use this component multiple times on a page.

You can learn more about custom elements in [web.dev’s Reusable Web Components guide](https://web.dev/custom-elements-v1/) and [MDN’s introduction to custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements).

### Pass frontmatter variables to scripts

[Section titled “Pass frontmatter variables to scripts”](#pass-frontmatter-variables-to-scripts)

In Astro components, the code in [the frontmatter](/en/basics/astro-components/#the-component-script) (between the `---` fences) runs on the server and is not available in the browser.

To pass server-side variables to client-side scripts, store them in [`data-*` attributes](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes) on HTML elements. Scripts can then access these values using the `dataset` property.

In this example component, a `message` prop is stored in a `data-message` attribute, so the custom element can read `this.dataset.message` and get the value of the prop in the browser.

src/components/AstroGreet.astro

```astro
---
const { message = 'Welcome, world!' } = Astro.props;
---


<!-- Store the message prop as a data attribute. -->
<astro-greet data-message={message}>
  <button>Say hi!</button>
</astro-greet>


<script>
  class AstroGreet extends HTMLElement {
    connectedCallback() {
      // Read the message from the data attribute.
      const message = this.dataset.message;
      const button = this.querySelector('button');
      button.addEventListener('click', () => {
        alert(message);
      });
    }
  }


  customElements.define('astro-greet', AstroGreet);
</script>
```

Now we can use our component multiple times and be greeted by a different message for each one.

src/pages/example.astro

```astro
---
import AstroGreet from '../components/AstroGreet.astro';
---


<!-- Use the default message: “Welcome, world!” -->
<AstroGreet />


<!-- Use custom messages passed as a props. -->
<AstroGreet message="Lovely day to build components!" />
<AstroGreet message="Glad you made it! 👋" />
```

Did you know?

This is actually what Astro does behind the scenes when you pass props to a component written using a UI framework like React! For components with a `client:*` directive, Astro creates an `<astro-island>` custom element with a `props` attribute that stores your server-side props in the HTML output.

### Combining scripts and UI Frameworks

[Section titled “Combining scripts and UI Frameworks”](#combining-scripts-and-ui-frameworks)

Elements rendered by a UI framework may not be available yet when a `<script>` tag executes. If your script also needs to handle [UI framework components](/en/guides/framework-components/), using a custom element is recommended.

# Use a CMS with Astro

> How to use a CMS to add content to Astro

**Ready to connect a Headless CMS to your Astro project?** Follow one of our guides to integrate a CMS.

Tip

Find [community-maintained integrations](https://astro.build/integrations/?search=cms) for connecting a CMS to your project in our integrations directory.

## CMS Guides

[Section titled “CMS Guides”](#cms-guides)

Note that many of these pages are **stubs**: they’re collections of resources waiting for your contribution!

* ![](/logos/apostrophecms.svg)

  ### [Apostrophe](/en/guides/cms/apostrophecms/)

* ![](/logos/builderio.svg)

  ### [Builder.io](/en/guides/cms/builderio/)

* ![](/logos/buttercms.svg)

  ### [ButterCMS](/en/guides/cms/buttercms/)

* ![](/logos/caisy.svg)

  ### [Caisy](/en/guides/cms/caisy/)

* ![](/logos/cloudcannon.svg)

  ### [CloudCannon](/en/guides/cms/cloudcannon/)

* ![](/logos/contentful.svg)

  ### [Contentful](/en/guides/cms/contentful/)

* ![](/logos/cosmic.svg)

  ### [Cosmic](/en/guides/cms/cosmic/)

* ![](/logos/craft-cms.svg)

  ### [Craft CMS](/en/guides/cms/craft-cms/)

* ![](/logos/craft-cross-cms.svg)

  ### [Craft Cross CMS](/en/guides/cms/craft-cross-cms/)

* ![](/logos/crystallize.svg)

  ### [Crystallize](/en/guides/cms/crystallize/)

* ![](/logos/datocms.svg)

  ### [DatoCMS](/en/guides/cms/datocms/)

* ![](/logos/decap-cms.svg)

  ### [Decap CMS](/en/guides/cms/decap-cms/)

* ![](/logos/directus.svg)

  ### [Directus](/en/guides/cms/directus/)

* ![](/logos/drupal.svg)

  ### [Drupal](/en/guides/cms/drupal/)

* ![](/logos/flotiq.svg)

  ### [Flotiq](/en/guides/cms/flotiq/)

* ![](/logos/frontmatter-cms.svg)

  ### [Front Matter CMS](/en/guides/cms/frontmatter-cms/)

* ![](/logos/ghost.png)

  ### [Ghost](/en/guides/cms/ghost/)

* ![](/logos/gitcms.svg)

  ### [GitCMS](/en/guides/cms/gitcms/)

* ![](/logos/hashnode.png)

  ### [Hashnode](/en/guides/cms/hashnode/)

* ![](/logos/hygraph.svg)

  ### [Hygraph](/en/guides/cms/hygraph/)

* ![](/logos/keystatic.svg)

  ### [Keystatic](/en/guides/cms/keystatic/)

* ![](/logos/keystonejs.svg)

  ### [KeystoneJS](/en/guides/cms/keystonejs/)

* ![](/logos/kontent-ai.svg)

  ### [Kontent.ai](/en/guides/cms/kontent-ai/)

* ![](/logos/microcms.svg)

  ### [microCMS](/en/guides/cms/microcms/)

* ![](/logos/optimizely.svg)

  ### [Optimizely CMS](/en/guides/cms/optimizely/)

* ![](/logos/payload.svg)

  ### [Payload CMS](/en/guides/cms/payload/)

* ![](/logos/preprcms.svg)

  ### [Prepr CMS](/en/guides/cms/preprcms/)

* ![](/logos/prismic.svg)

  ### [Prismic](/en/guides/cms/prismic/)

* ![](/logos/sanity.svg)

  ### [Sanity](/en/guides/cms/sanity/)

* ![](/logos/sitecore.svg)

  ### [Sitecore XM](/en/guides/cms/sitecore/)

* ![](/logos/sitepins.svg)

  ### [Sitepins](/en/guides/cms/sitepins/)

* ![](/logos/spinal.svg)

  ### [Spinal](/en/guides/cms/spinal/)

* ![](/logos/statamic.svg)

  ### [Statamic](/en/guides/cms/statamic/)

* ![](/logos/storyblok.svg)

  ### [Storyblok](/en/guides/cms/storyblok/)

* ![](/logos/strapi.svg)

  ### [Strapi](/en/guides/cms/strapi/)

* ![](/logos/studiocms.svg)

  ### [StudioCMS](/en/guides/cms/studiocms/)

* ![](/logos/tina-cms.svg)

  ### [Tina CMS](/en/guides/cms/tina-cms/)

* ![](/logos/umbraco.svg)

  ### [Umbraco](/en/guides/cms/umbraco/)

* ![](/logos/wordpress.svg)

  ### [WordPress](/en/guides/cms/wordpress/)

## Why use a CMS?

[Section titled “Why use a CMS?”](#why-use-a-cms)

A Content Management System lets you write content and manage assets outside of your Astro project.

This unlocks new features for working with content. Most CMSes give you a visual content editor, the ability to specify standard types of content, and a way to collaborate with others.

A CMS can be useful for content that follows a particular structure, often giving you a dashboard-like experience and WYSIWYG editing tools. You might use a CMS to write blog posts using a CMS’s rich text editor instead of Markdown files. Or you might use a CMS to maintain product listings for an eCommerce shop, making certain fields required to avoid incomplete listings.

Your Astro project can then fetch your content from your CMS and display it, wherever and however you want on your site.

## Which CMSes work well with Astro?

[Section titled “Which CMSes work well with Astro?”](#which-cmses-work-well-with-astro)

Because Astro takes care of the *presentation* of your content, you’ll want to choose a *headless* CMS, like those in the list above. This means that the CMS helps you write your content, but doesn’t generate a site that displays it. Instead, you fetch the content data and use in your Astro project.

Some headless CMSes, like Storyblok, provide an Astro [integration](/en/guides/integrations-guide/) that helps fetch the content specifically for an Astro site. Others provide a JavaScript SDK, a library that you install and use to fetch your remote content.

Explore a [list of over 100 headless content management systems](https://jamstack.org/headless-cms/) External where you can filter by type (e.g. Git-based, API driven) and license (open-source or closed-source).

## Can I use Astro without a CMS?

[Section titled “Can I use Astro without a CMS?”](#can-i-use-astro-without-a-cms)

Yes! Astro provides built-in support for [Markdown](/en/guides/markdown-content/).


---

**Navigation:** [← Previous](./01-why-astro.md) | [Index](./index.md) | [Next →](./03-apostrophecms-astro.md)
