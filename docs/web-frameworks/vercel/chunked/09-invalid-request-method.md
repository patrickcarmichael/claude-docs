**Navigation:** [← Previous](./08-framework-environment-variables.md) | [Index](./index.md) | [Next →](./10-frameworks-on-vercel.md)

---

# INVALID\_REQUEST\_METHOD

Copy page

Ask AI about this page

Last updated October 6, 2025

The `INVALID_REQUEST_METHOD` error occurs when a request is made with a method that is either invalid or not supported by the server. This error typically happens when trying to use an HTTP method that the endpoint does not accept or recognize.

405

INVALID\_REQUEST\_METHOD:

Method Not Allowed

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/INVALID\_REQUEST\_METHOD to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FINVALID_REQUEST_METHOD+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify request method: Ensure that the HTTP request method used is correct and supported by the endpoint. Common HTTP methods include `GET`, `POST`, `PUT`, `DELETE` etc
2.  Review code: Check the code where the request is being made to ensure the correct method is being used
3.  Test with different methods: If possible, test the endpoint with different HTTP methods to determine if the issue is with the method or another part of the request

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "MALFORMED_REQUEST_HEADER"
description: "The MALFORMED_REQUEST_HEADER error occurs when a request contains an improperly formatted or invalid header. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/MALFORMED_REQUEST_HEADER"
--------------------------------------------------------------------------------

# MALFORMED\_REQUEST\_HEADER

Copy page

Ask AI about this page

Last updated October 6, 2025

The `MALFORMED_REQUEST_HEADER` error signifies that a request made to the server includes a header that is incorrectly formatted or contains invalid data. This could be due to syntax errors, incorrect header field names, or incompatible header values.

400

MALFORMED\_REQUEST\_HEADER:

Bad Request

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/MALFORMED\_REQUEST\_HEADER to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FMALFORMED_REQUEST_HEADER+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Inspect request headers: Review the headers in your request. Ensure that they are correctly formatted and adhere to the [HTTP standard](https://developer.mozilla.org/en-US/docs/Glossary/Request_header)
2.  Validate UTF-8 encoding: Confirm that all request headers, especially cookie values, are valid UTF-8 strings. Non-UTF-8 characters in headers, particularly in the cookie header, often cause this error
3.  Examine Vercel Function behavior: Since this error is specific to Vercel functions, verify the functionality and responses of your Vercel functions. Ensure they are correctly handling request headers and not contributing to malformed responses

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "MICROFRONTENDS_MIDDLEWARE_ERROR"
description: "The microfrontend middleware returned an invalid application."
last_updated: "null"
source: "https://vercel.com/docs/errors/MICROFRONTENDS_MIDDLEWARE_ERROR"
--------------------------------------------------------------------------------

# MICROFRONTENDS\_MIDDLEWARE\_ERROR

Copy page

Ask AI about this page

Last updated October 6, 2025

The `MICROFRONTENDS_MIDDLEWARE_ERROR` error occurs when the middleware returned a header `x-vercel-mfe-zone` with an invalid value. The value must be a name of an application from `microfrontends.json`.

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/MICROFRONTENDS\_MIDDLEWARE\_ERROR to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FMICROFRONTENDS_MIDDLEWARE_ERROR+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  If you are setting the header, ensure that the value is a valid application name.
2.  If you are not setting the header, this is an error caused by the [@vercel/microfrontends](https://www.npmjs.com/package/@vercel/microfrontends) package. Please [open an issue](https://github.com/vercel/microfrontends/issues) and include the error message.

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "MICROFRONTENDS_MISSING_FALLBACK_ERROR"
description: "The microfrontend request did not have a fallback for the environment."
last_updated: "null"
source: "https://vercel.com/docs/errors/MICROFRONTENDS_MISSING_FALLBACK_ERROR"
--------------------------------------------------------------------------------

# MICROFRONTENDS\_MISSING\_FALLBACK\_ERROR

Copy page

Ask AI about this page

Last updated October 6, 2025

The `MICROFRONTENDS_MISSING_FALLBACK_ERROR` error occurs when a microfrontends request did not match any other deployments in the same environment, and no deployment could be found for the specified fallback.

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/MICROFRONTENDS\_MISSING\_FALLBACK\_ERROR to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FMICROFRONTENDS_MISSING_FALLBACK_ERROR+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

In the [Production](/docs/deployments/environments#production-environment) environment, this error should not occur since every request is routed to the Production environment of mcirofrontends projects. Make sure that every project in the microfrontends group has a production deployment.

In non-Production environments, the fallback is configured in the [Fallback Environment](/docs/microfrontends/managing-microfrontends#fallback-environment) setting. Based on the configured option, check that every project has a deployment for that environment.

If the issue persists after checking that every project has a deployment in the configured Fallback Environment setting, please contact Vercel support to reach out to the team.

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "MIDDLEWARE_INVOCATION_FAILED"
description: "The request for an Routing Middleware was not completed successfully. This is an application error."
last_updated: "null"
source: "https://vercel.com/docs/errors/MIDDLEWARE_INVOCATION_FAILED"
--------------------------------------------------------------------------------

# MIDDLEWARE\_INVOCATION\_FAILED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `MIDDLEWARE_INVOCATION_FAILED` error occurs when there is an issue with the Routing Middleware being invoked on the CDN. This error can be caused by a variety of issues, including unhandled exceptions.

500

MIDDLEWARE\_INVOCATION\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/MIDDLEWARE\_INVOCATION\_FAILED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FMIDDLEWARE_INVOCATION_FAILED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the Routing Middleware being invoked. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Use Vercel's status page: If you have tried the steps above and are still experiencing the error, check Vercel's [status page](https://www.vercel-status.com/) for any reported outages in the CDN, which can sometimes cause this error
3.  Check function code: Ensure that the code for the Routing Middleware is correct and does not contain any errors or infinite loops

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "MIDDLEWARE_INVOCATION_TIMEOUT"
description: "The Routing Middleware invocation timed out. This is an application error."
last_updated: "null"
source: "https://vercel.com/docs/errors/MIDDLEWARE_INVOCATION_TIMEOUT"
--------------------------------------------------------------------------------

# MIDDLEWARE\_INVOCATION\_TIMEOUT

Copy page

Ask AI about this page

Last updated October 6, 2025

The `MIDDLEWARE_INVOCATION_TIMEOUT` error occurs when an Routing Middleware takes [longer than the allowed execution time](/docs/functions/runtimes/edge#maximum-execution-duration) to complete or doesn't send a response chunk for a certain amount of time. This can be caused by long-running processes within the function or external dependencies that fail to respond in a timely manner.

If your backend API takes time to respond, we recommend [streaming the response](/docs/functions/streaming-functions) to avoid the idle timeout.

504

MIDDLEWARE\_INVOCATION\_TIMEOUT:

Gateway Timeout

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/MIDDLEWARE\_INVOCATION\_TIMEOUT to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FMIDDLEWARE_INVOCATION_TIMEOUT+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the Routing Middleware being invoked. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Review function code: Inspect the Routing Middleware code for any long-running operations or infinite loops that could cause a timeout
3.  Verify return value: Ensure the function returns a response within the specified time limit of [25 seconds](/docs/functions/limitations#max-duration)
4.  Optimize external calls: If the function makes calls to external services or APIs, ensure they are optimized and responding quickly. Consider specifying a fetch timeout for external calls using [`AbortSignal.timeout`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal/timeout_static).
5.  Consider streaming data: If the function is processing large amounts of data, consider using a [streaming approach](/docs/functions/streaming-functions) to avoid timeouts
6.  Implement error handling: Add error handling in the function to manage timeouts and other exceptions effectively

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "MIDDLEWARE_RUNTIME_DEPRECATED"
description: "A middleware is using a deprecated runtime."
last_updated: "null"
source: "https://vercel.com/docs/errors/MIDDLEWARE_RUNTIME_DEPRECATED"
--------------------------------------------------------------------------------

# MIDDLEWARE\_RUNTIME\_DEPRECATED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `MIDDLEWARE_RUNTIME_DEPRECATED` error occurs when a middleware is using a deprecated runtime. This error can occur when a middleware is using a runtime that is no longer supported by the platform.

503

MIDDLEWARE\_RUNTIME\_DEPRECATED:

Middleware Runtime Deprecated

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/MIDDLEWARE\_RUNTIME\_DEPRECATED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FMIDDLEWARE_RUNTIME_DEPRECATED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Identify the affected project: Use [Vercel Logs](/docs/observability/runtime-logs) to identify if your project is experiencing this error. Look for the `MIDDLEWARE_RUNTIME_DEPRECATED` error in your project's runtime logs.
2.  Locate the middleware: Once you've identified the project, check if it has a `middleware.js` or `middleware.ts` file in the root directory or uses Routing Middleware in any way.
3.  Redeploy the project: Redeploy the project to automatically upgrade to the latest supported runtime version. However, if the redeploy fails, you may need to:
    *   Update your Node.js version: Check your project's Node.js version setting in the Vercel dashboard or `package.json` and update it to a [supported version](/docs/functions/runtimes/node-js#node.js-version)
    *   Update dependencies: Outdated dependencies may not be compatible with newer Node.js versions. Update your `package.json` dependencies to their latest compatible versions before redeploying

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "NOT_FOUND"
description: "The requested resource was not found. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/NOT_FOUND"
--------------------------------------------------------------------------------

# NOT\_FOUND

Copy page

Ask AI about this page

Last updated October 6, 2025

The `NOT_FOUND` error occurs when a requested resource could not be found. This might happen if the resource has been moved, deleted, or if there is a typo in the URL.

404

NOT\_FOUND:

Not Found

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/NOT\_FOUND to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FNOT_FOUND+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check the deployment URL: Ensure that the deployment URL you are using is correct and does not contain any typos or incorrect paths
2.  Check deployment existence: Verify that the [deployment exists](/docs/projects/project-dashboard#deployments) and has not been deleted
3.  Review deployment logs: If the deployment exists, review the [deployment logs](/docs/deployments/logs) to identify any issues that might have caused the deployment to be unavailable
4.  Verify permissions: Ensure you have the necessary [permissions](/docs/accounts/team-members-and-roles) to access the deployment
5.  Contact support: If you've checked the above and are still unable to resolve the issue, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "NO_RESPONSE_FROM_FUNCTION"
description: "The application did not respond correctly, this is likely due to an exception being thrown from the function handler."
last_updated: "null"
source: "https://vercel.com/docs/errors/NO_RESPONSE_FROM_FUNCTION"
--------------------------------------------------------------------------------

# NO\_RESPONSE\_FROM\_FUNCTION

Copy page

Ask AI about this page

Last updated October 6, 2025

The `NO_RESPONSE_FROM_FUNCTION` error occurs when a function invocation completes without returning a response. This might happen if the function encounters an error that prevents it from responding, or if it fails to generate a response within the allowed execution time.

Potential causes include:

*   A global uncaught exception
*   A global unhandled rejection
*   A deployment that introduced incorrect syntax

502

NO\_RESPONSE\_FROM\_FUNCTION:

Bad Gateway

#### [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/NO\_RESPONSE\_FROM\_FUNCTION to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FNO_RESPONSE_FROM_FUNCTION+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify return statements: Ensure that the function has the necessary return statements to generate a response
2.  Check the function logs: Open the [realtime request logs](/guides/where-are-vercel-logs#function-logs) for the application in a separate tab - this tab must be kept open while reproducing the error
3.  Review realtime logs: Repeat the application behavior that led to the error being thrown and review the realtime request logs where it will now show
    *   Use the information contained within the error logs to understand where the function is failing
4.  Use Log Drains: Create a [Log Drain](/docs/drains) if you do not have one yet, to persist errors from Vercel functions
5.  Check external dependencies: If the function relies on external services or APIs, ensure they are responding in a timely manner

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "OPTIMIZED_EXTERNAL_IMAGE_REQUEST_FAILED"
description: "The request for an optimized external image failed. This is a server error."
last_updated: "null"
source: "https://vercel.com/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_REQUEST_FAILED"
--------------------------------------------------------------------------------

# OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_FAILED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `OPTIMIZED_EXTERNAL_IMAGE_REQUEST_FAILED` error occurs when the request for an optimized external image fails.

502

OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_FAILED:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_FAILED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FOPTIMIZED_EXTERNAL_IMAGE_REQUEST_FAILED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify external URL: Ensure that the external image URL is correct and accessible
2.  Check query parameters: Ensure that any query parameters are valid

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "OPTIMIZED_EXTERNAL_IMAGE_REQUEST_INVALID"
description: "The external image request is invalid. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_REQUEST_INVALID"
--------------------------------------------------------------------------------

# OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_INVALID

Copy page

Ask AI about this page

Last updated October 6, 2025

The `OPTIMIZED_EXTERNAL_IMAGE_REQUEST_INVALID` error occurs when the external image request is invalid.

502

OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_INVALID:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_INVALID to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FOPTIMIZED_EXTERNAL_IMAGE_REQUEST_INVALID+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify external URL: Ensure that the external image URL is absolute and correctly formatted
2.  Check query parameters: Ensure that any query parameters are valid
3.  Validate source configuration: Verify that the external source is configured correctly and accessible

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED"
description: "The external image request is unauthorized. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED"
--------------------------------------------------------------------------------

# OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_UNAUTHORIZED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED` error occurs when the external image request is unauthorized.

502

OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_UNAUTHORIZED:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_UNAUTHORIZED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FOPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check permissions: Ensure that you have the necessary permissions to access the external image
2.  Verify authentication: Check for any authentication or authorization issues with the external source
3.  Update credentials: Ensure that any required credentials or tokens are correctly set and not expired
4.  Remove filters: Remove any filters that may be blocking the request, such as headers or IP restrictions

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "OPTIMIZED_EXTERNAL_IMAGE_TOO_MANY_REDIRECTS"
description: "The external image request encountered too many redirects. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_TOO_MANY_REDIRECTS"
--------------------------------------------------------------------------------

# OPTIMIZED\_EXTERNAL\_IMAGE\_TOO\_MANY\_REDIRECTS

Copy page

Ask AI about this page

Last updated October 6, 2025

The `OPTIMIZED_EXTERNAL_IMAGE_TOO_MANY_REDIRECTS` error occurs when the external image request encounters too many redirects.

502

OPTIMIZED\_EXTERNAL\_IMAGE\_TOO\_MANY\_REDIRECTS:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/OPTIMIZED\_EXTERNAL\_IMAGE\_TOO\_MANY\_REDIRECTS to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FOPTIMIZED_EXTERNAL_IMAGE_TOO_MANY_REDIRECTS+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check URL for redirects: Verify the external image URL to ensure it does not cause an infinite redirect loop

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "RANGE_END_NOT_VALID"
description: "The end value of the Range header in the request is invalid. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/RANGE_END_NOT_VALID"
--------------------------------------------------------------------------------

# RANGE\_END\_NOT\_VALID

Copy page

Ask AI about this page

Last updated October 6, 2025

The `RANGE_END_NOT_VALID` error occurs when the end value of the `Range` header in a request is invalid. This header is used to request a specific portion of a resource from the server, which is useful for operations like resuming downloads or streaming media.

416

RANGE\_END\_NOT\_VALID:

Requested Range Not Satisfiable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/RANGE\_END\_NOT\_VALID to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FRANGE_END_NOT_VALID+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Validate Range header values: Ensure that the end value in the `Range` header is a valid integer. It should not be a letter, a decimal, or a scientific notation value
2.  Correct ordering: Ensure the start value is less than the end value in the `Range` header
3.  Omit end value if necessary: If you want to request all bytes from a certain start point to the end of the resource, you can omit the end value
4.  Check configuration: If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure it's being set correctly
5.  Debugging: If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "RANGE_GROUP_NOT_VALID"
description: "The group value of the Range header in the request is invalid. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/RANGE_GROUP_NOT_VALID"
--------------------------------------------------------------------------------

# RANGE\_GROUP\_NOT\_VALID

Copy page

Ask AI about this page

Last updated October 6, 2025

The `RANGE_GROUP_NOT_VALID` error occurs when the group value of the `Range` header in a request is invalid. This header is used to request a specific portion of a resource from the server, and the group value can be used to specify multiple ranges or a set of subranges.

416

RANGE\_GROUP\_NOT\_VALID:

Requested Range Not Satisfiable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/RANGE\_GROUP\_NOT\_VALID to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FRANGE_GROUP_NOT_VALID+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Validate Range header values: Ensure that the group value in the `Range` header is a valid format. It should correctly specify the range or subranges you wish to retrieve
2.  Correct grouping: Ensure that the group value is correctly formatted and contains valid range specifications
3.  Check configuration: If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure it's being set correctly
4.  Debugging: If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "RANGE_MISSING_UNIT"
description: "The unit identifier of the Range header in the request is missing. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/RANGE_MISSING_UNIT"
--------------------------------------------------------------------------------

# RANGE\_MISSING\_UNIT

Copy page

Ask AI about this page

Last updated October 6, 2025

The `RANGE_MISSING_UNIT` error occurs when the unit identifier of the `Range` header in a request is missing. The `Range` header is used to request a specific portion of a resource from the server, and the unit identifier indicates the unit in which the range is specified, such as bytes.

416

RANGE\_MISSING\_UNIT:

Requested Range Not Satisfiable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/RANGE\_MISSING\_UNIT to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FRANGE_MISSING_UNIT+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Specify unit identifier: Ensure that the `Range` header in your request specifies a unit identifier like `bytes`
2.  Check configuration: If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure the unit identifier is being included
3.  Verify syntax: Verify that the syntax of the `Range` header is correct and follows the format `unit=range-start-range-end`, for example, `bytes=0-999`
4.  Debugging: If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "RANGE_START_NOT_VALID"
description: "The start value of the Range header in the request is invalid. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/RANGE_START_NOT_VALID"
--------------------------------------------------------------------------------

# RANGE\_START\_NOT\_VALID

Copy page

Ask AI about this page

Last updated October 6, 2025

The `RANGE_START_NOT_VALID` error occurs when the start value of the `Range` header in a request is invalid. The `Range` header is used to request a specific portion of a resource from the server, and the start value should be a valid integer indicating the beginning of the requested range.

416

RANGE\_START\_NOT\_VALID:

Requested Range Not Satisfiable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/RANGE\_START\_NOT\_VALID to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FRANGE_START_NOT_VALID+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Validate Range header values: Ensure that the start value in the `Range` header is a valid integer. It should not be a letter, a decimal, or a scientific notation value
2.  Correct ordering: Ensure the start value is less than the end value in the `Range` header, if an end value is specified
3.  Check configuration: If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure it's being set correctly
4.  Debugging: If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "RANGE_UNIT_NOT_SUPPORTED"
description: "The unit identifier of the Range header in the request is not supported. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/RANGE_UNIT_NOT_SUPPORTED"
--------------------------------------------------------------------------------

# RANGE\_UNIT\_NOT\_SUPPORTED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `RANGE_UNIT_NOT_SUPPORTED` error occurs when the unit identifier of the `Range` header in a request is not supported by the server. The `Range` header is used to request a specific portion of a resource from the server, and the unit identifier indicates the unit in which the range is specified, such as bytes.

416

RANGE\_UNIT\_NOT\_SUPPORTED:

Requested Range Not Satisfiable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/RANGE\_UNIT\_NOT\_SUPPORTED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FRANGE_UNIT_NOT_SUPPORTED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify supported Range units: Check the documentation for the server or service you are interacting with to determine the supported range units
2.  Correct Range unit: If the `Range` header in your request specifies an unsupported unit, correct it to use a supported unit
3.  Check configuration: If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure a supported unit identifier is being used
4.  Debugging: If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "REQUEST_HEADER_TOO_LARGE"
description: "Request header size exceeds the permissible limit."
last_updated: "null"
source: "https://vercel.com/docs/errors/REQUEST_HEADER_TOO_LARGE"
--------------------------------------------------------------------------------

# REQUEST\_HEADER\_TOO\_LARGE

Copy page

Ask AI about this page

Last updated October 6, 2025

The `REQUEST_HEADER_TOO_LARGE` error occurs when the size of the request headers in your function and [Routing Middleware](/docs/routing-middleware) exceeds the allowed limits. Specifically, individual request headers must not exceed 16 KB, and the combined size of all headers, including the header names, must not exceed 32 KB.

This issue often arises from excessively large headers in a request. On Vercel, applications may have custom headers, which, if overly large, can trigger this error during server request processing.

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/REQUEST\_HEADER\_TOO\_LARGE to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FREQUEST_HEADER_TOO_LARGE+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Limit header size: Ensure that the size of each request header does not exceed 16 KB
2.  Manage total header size: Monitor and control the combined size of all headers, keeping it under 32 KB
3.  Review cookies: Since cookies are included in the header, it's crucial to limit their size as part of the overall header size

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "RESOURCE_NOT_FOUND"
description: "This error signifies that a specified resource could not be located."
last_updated: "null"
source: "https://vercel.com/docs/errors/RESOURCE_NOT_FOUND"
--------------------------------------------------------------------------------

# RESOURCE\_NOT\_FOUND

Copy page

Ask AI about this page

Last updated October 6, 2025

The `RESOURCE_NOT_FOUND` error indicates that a requested resource is not available or cannot be found. This error typically arises when a request is made for a resource that either does not exist or is currently inaccessible.

404

RESOURCE\_NOT\_FOUND:

Not Found

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/RESOURCE\_NOT\_FOUND to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FRESOURCE_NOT_FOUND+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify resource existence: Confirm that the resource you're attempting to access exists. Check for any typos or errors in the resource name or path
2.  Review access permissions: Ensure that your application or function has the necessary permissions to access the resource
3.  Inspect resource path: Double-check the path or URL to the resource. Ensure it is correctly formatted and corresponds to the intended resource
4.  Check application configuration: Review your application's configuration settings to ensure they are correctly set up to locate and access the resource
5.  Review logs: Consult your [application logs](/docs/runtime-logs) for more details or clues as to why the resource could not be found. This can provide insights into whether the issue is due to an incorrect path, permissions, or other reasons

Additionally, the error can also occur in the context of the [Vercel REST API](/docs/rest-api), where it is similar to the [HTTP 500 Internal Server Error](/docs/rest-api/reference/errors#resource-not-found). In this case, the error message will contain the details of the resource that could not be found.

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "ROUTER_CANNOT_MATCH"
description: "The router cannot match the route to any of the known patterns. This is a routing error."
last_updated: "null"
source: "https://vercel.com/docs/errors/ROUTER_CANNOT_MATCH"
--------------------------------------------------------------------------------

# ROUTER\_CANNOT\_MATCH

Copy page

Ask AI about this page

Last updated October 6, 2025

The `ROUTER_CANNOT_MATCH` error occurs when the router is unable to match the requested route to any of the known patterns. This could happen due to a misconfiguration in the routing setup or an erroneous request path.

502

ROUTER\_CANNOT\_MATCH:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/ROUTER\_CANNOT\_MATCH to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FROUTER_CANNOT_MATCH+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review routing configuration: Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure that it is correctly set up to handle the requested route
2.  Verify request path: Ensure that the request path is correct and adheres to the expected patterns defined in the routing configuration
3.  Check for typos: Look for any typos or misconfigurations in the routing setup that might be causing the mismatch
4.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR"
description: "Connection error occurred while routing to an external target. This is a routing error."
last_updated: "null"
source: "https://vercel.com/docs/errors/ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR"
--------------------------------------------------------------------------------

# ROUTER\_EXTERNAL\_TARGET\_CONNECTION\_ERROR

Copy page

Ask AI about this page

Last updated October 6, 2025

The `ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR` error occurs when there is a connection error while routing to an external target. This could happen due to network issues, incorrect routing configuration, or the external target being unreachable.

502

ROUTER\_EXTERNAL\_TARGET\_CONNECTION\_ERROR:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/ROUTER\_EXTERNAL\_TARGET\_CONNECTION\_ERROR to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FROUTER_EXTERNAL_TARGET_CONNECTION_ERROR+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check network connectivity: Ensure that the network connectivity between your deployment and the external target is stable
2.  Verify external target availability: Make sure the external target is online and reachable
3.  Review routing configuration: Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure that it is correctly set up to route to the external target
4.  Inspect firewall settings: Verify that there are no firewall settings blocking the connection to the external target
5.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing or network connectivity

[

### Not what you were looking for?

Return to the Errors documentation section

](/docs/errors)

--------------------------------------------------------------------------------
title: "ROUTER_EXTERNAL_TARGET_ERROR"
description: "Error occurred while routing to an external target. This is a routing error."
last_updated: "null"
source: "https://vercel.com/docs/errors/ROUTER_EXTERNAL_TARGET_ERROR"
--------------------------------------------------------------------------------

# ROUTER\_EXTERNAL\_TARGET\_ERROR

Copy page

Ask AI about this page

Last updated October 6, 2025

The `ROUTER_EXTERNAL_TARGET_ERROR` error occurs when there is an error while routing to an external target. This could happen due to incorrect routing configuration, an erroneous response from the external target, or other issues affecting the routing process. If the external server does not respond within the maximum timeout of 120 seconds (2 minutes), you will see this error.

502

ROUTER\_EXTERNAL\_TARGET\_ERROR:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/ROUTER\_EXTERNAL\_TARGET\_ERROR to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FROUTER_EXTERNAL_TARGET_ERROR+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review routing configuration: Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure that it is correctly set up to route to the external target
2.  Verify external target availability: Make sure the external target is online and reachable
3.  Check for errors in external target: Investigate the external target for any errors that might be causing the routing issue
4.  Inspect firewall settings: Verify that there are no firewall settings blocking the connection to the external target
5.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing or the external target

[

### Not what you were looking for?

Return to the Errors documentation section

](/docs/errors)

--------------------------------------------------------------------------------
title: "ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR"
description: "Error in establishing a connection with an external target."
last_updated: "null"
source: "https://vercel.com/docs/errors/ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR"
--------------------------------------------------------------------------------

# ROUTER\_EXTERNAL\_TARGET\_HANDSHAKE\_ERROR

Copy page

Ask AI about this page

Last updated October 6, 2025

The `ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR` error occurs when a connection cannot be successfully established with an external target. This error may result from issues during the SSL handshake process or due to a timeout, and is often attributed to one of the following causes:

*   SSL handshake failure: The SSL handshake may fail if the target has an invalid certificate or uses an unsupported Cipher Suite
*   Timeout: The error could also be due to a timeout, which might be caused by issues connecting to the target. Note that proxied requests to external targets have a maximum timeout of 120 seconds (2 minutes).

502

ROUTER\_EXTERNAL\_TARGET\_HANDSHAKE\_ERROR:

Unable to establish connection with external target

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/ROUTER\_EXTERNAL\_TARGET\_HANDSHAKE\_ERROR to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check SSL configuration: Ensure that the target's [SSL certificate](/docs/domains/custom-SSL-certificate) is valid and that it is not using an [unsupported Cipher Suite](/docs/security/encryption#supported-ciphers)
2.  Investigate connectivity issues: Look into potential connectivity problems between your application and the external target
3.  Monitor response times: Check if your application or the external target is experiencing unusual delays that might be contributing to the timeout

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "ROUTER_TOO_MANY_HAS_SELECTIONS"
description: "The router has too many selections. This is a routing error."
last_updated: "null"
source: "https://vercel.com/docs/errors/ROUTER_TOO_MANY_HAS_SELECTIONS"
--------------------------------------------------------------------------------

# ROUTER\_TOO\_MANY\_HAS\_SELECTIONS

Copy page

Ask AI about this page

Last updated October 6, 2025

The `ROUTER_TOO_MANY_HAS_SELECTIONS` error occurs when the router encounters too many selections while processing the request. This could happen due to misconfiguration or a complex routing setup that exceeds the router's capabilities.

502

ROUTER\_TOO\_MANY\_HAS\_SELECTIONS:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/ROUTER\_TOO\_MANY\_HAS\_SELECTIONS to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FROUTER_TOO_MANY_HAS_SELECTIONS+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review routing configuration: Check the [routing configuration](/docs/redirects#configuration-redirects) to ensure it's correctly set up and doesn't contain excessive selections
2.  Simplify routing setup: If possible, simplify the routing setup to reduce the number of selections the router has to process
3.  Check for recursive or looping logic: Ensure there isn't any recursive or looping logic in the routing configuration that could lead to excessive selections
4.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to routing or selections

[

### Not what you were looking for?

Return to the Errors documentation section

](/docs/errors)

--------------------------------------------------------------------------------
title: "SANBDOX_NOT_FOUND"
description: "The Sandbox could not be found on Vercel. This is a platform error."
last_updated: "null"
source: "https://vercel.com/docs/errors/SANDBOX_NOT_FOUND"
--------------------------------------------------------------------------------

# SANBDOX\_NOT\_FOUND

Copy page

Ask AI about this page

Last updated October 6, 2025

The `SANDBOX_NOT_FOUND` error occurs when you are trying to access a Sandbox that does not exist. This could happen if there is a typo in the URL.

404

SANDBOX\_NOT\_FOUND:

Not Found

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/SANDBOX\_NOT\_FOUND to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FSANDBOX_NOT_FOUND+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify the Sandbox URL: Navigate to the [Sandboxes dashboard](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fsandboxes&title=Go+to+Sandboxes), select the one you want to access, and copy the displayed URL
2.  Check for typos: Ensure that there are no typos in the Sandbox URL you are trying to access

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "SANBDOX_NOT_LISTENING"
description: "The Sandbox is not listening on the requested port. This is an application error."
last_updated: "null"
source: "https://vercel.com/docs/errors/SANDBOX_NOT_LISTENING"
--------------------------------------------------------------------------------

# SANBDOX\_NOT\_LISTENING

Copy page

Ask AI about this page

Last updated October 6, 2025

The `SANDBOX_NOT_LISTENING` error occurs when you are trying to access a Sandbox that is not listening on the requested port. This could happen if the port is malconfigured, or the process running on that port has exited.

502

SANDBOX\_NOT\_LISTENING:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/SANDBOX\_NOT\_LISTENING to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FSANDBOX_NOT_LISTENING+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify the configured port: Make sure that the `ports` field used in `Sandbox.create` matches the port your application is listening on. Follow the [documentation](/docs/vercel-sandbox) to learn more
2.  Check the Sandbox history: Navigate to the [Sandboxes dashboard](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fsandboxes&title=Go+to+Sandboxes), select the one you are accessing, and check the history section to see which commands were run and if any errors occurred

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "SANBDOX_STOPPED"
description: "The Sandbox was stopped and is no longer reachable. This is a platform error."
last_updated: "null"
source: "https://vercel.com/docs/errors/SANDBOX_STOPPED"
--------------------------------------------------------------------------------

# SANBDOX\_STOPPED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `SANDBOX_STOPPED` error occurs when you are trying to access a Sandbox that has been stopped. This could happen if the Sandbox was manually stopped by the owner, or if the Sandbox reached its configured timeout.

410

SANDBOX\_STOPPED:

Gone

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/SANDBOX\_STOPPED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FSANDBOX_STOPPED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Verify the Sandbox status: Navigate to the [Sandboxes dashboard](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fsandboxes&title=Go+to+Sandboxes), select the one you are accessing, and check the history section to know why it was stopped
2.  Increase the timeout: By default, Sandboxes have a timeout of 10 minutes. Follow the [documentation](/docs/vercel-sandbox#create-the-set-up-file) to increase this value

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "TOO_MANY_FILESYSTEM_CHECKS"
description: "Too many filesystem checks occurred while processing the request. This is a routing error."
last_updated: "null"
source: "https://vercel.com/docs/errors/TOO_MANY_FILESYSTEM_CHECKS"
--------------------------------------------------------------------------------

# TOO\_MANY\_FILESYSTEM\_CHECKS

Copy page

Ask AI about this page

Last updated October 6, 2025

The `TOO_MANY_FILESYSTEM_CHECKS` error occurs when there are excessive filesystem checks while processing a request. This could happen during the routing process, especially when using rewrites, redirects, or any other configuration that requires checking the filesystem repeatedly.

502

TOO\_MANY\_FILESYSTEM\_CHECKS:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/TOO\_MANY\_FILESYSTEM\_CHECKS to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FTOO_MANY_FILESYSTEM_CHECKS+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review routing configuration: Check the routing configuration to ensure that it is not causing excessive filesystem checks, especially in the case of [rewrites](/docs/rewrites) or [redirects](/docs/redirects#configuration-redirects).
2.  Optimize routing configuration: Reduce the number of has routes matched on a single path. You cannot have more than 5 has routes matched on a single path
3.  Check for Loops: Ensure there isn't any looping logic in the routing or filesystem access code that could lead to excessive filesystem checks
4.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to filesystem access or routing

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "TOO_MANY_FORKS"
description: "An error occurred in the application when matching too many conditional routes. You cannot have more than 5 `has` routes matched on a single path."
last_updated: "null"
source: "https://vercel.com/docs/errors/TOO_MANY_FORKS"
--------------------------------------------------------------------------------

# TOO\_MANY\_FORKS

Copy page

Ask AI about this page

Last updated October 6, 2025

The `TOO_MANY_FORKS` error occurs when too many forks are generated while processing the request. This usually happens when matching too many conditional routes, which could lead to a loop or excessive resource usage.

You cannot have more than 5 `has` routes matched on a single path.

502

TOO\_MANY\_FORKS:

Bad Gateway

#### [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/TOO\_MANY\_FORKS to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FTOO_MANY_FORKS+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review routing configuration: Reduce the number of [rewrites](/docs/rewrites), [redirects](/docs/redirects#configuration-redirects), or [headers](/docs/headers) with a `has` key (conditional route) that match the erroring request path
2.  Check for recursive logic: Ensure there isn't any recursive logic in the routing configuration that could lead to excessive forking
3.  Handle unhandled exceptions: Check the [application logs](/docs/deployments/logs) for any unhandled exceptions that may be causing the error

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "TOO_MANY_RANGES"
description: "Too many ranges have been specified in the Range header of the request. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/TOO_MANY_RANGES"
--------------------------------------------------------------------------------

# TOO\_MANY\_RANGES

Copy page

Ask AI about this page

Last updated October 6, 2025

The `TOO_MANY_RANGES` error occurs when too many ranges have been specified in the `Range` header of a request. The `Range` header is used to request specific portions of a resource from the server, and specifying too many ranges can lead to an excessive load on the server.

416

TOO\_MANY\_RANGES:

Requested Range Not Satisfiable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/TOO\_MANY\_RANGES to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FTOO_MANY_RANGES+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

To troubleshoot this error, follow these steps:

1.  Reduce number of Ranges: Reduce the number of ranges specified in the `Range` header to a reasonable amount
2.  Check configuration: If the `Range` header values are being set automatically by some part of your system, check the configuration to ensure a reasonable number of ranges are being specified
3.  Verify server capabilities: Check the documentation for the server or service you are interacting with to determine the maximum number of supported ranges
4.  Debugging: If the error persists, log the `Range` header values in your server logs to debug and understand what values are being sent in requests

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "URL_TOO_LONG"
description: "The URL of the request is too long. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/URL_TOO_LONG"
--------------------------------------------------------------------------------

# URL\_TOO\_LONG

Copy page

Ask AI about this page

Last updated October 6, 2025

The `URL_TOO_LONG` error occurs when the URL of the request exceeds the maximum length allowed by the CDN (14 KB). Long URLs can be a result of long query strings, lengthy path segments, or an excessive number of path segments.

414

URL\_TOO\_LONG:

Request-URI Too Long

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/URL\_TOO\_LONG to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FURL_TOO_LONG+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Shorten the URL: Simplify the URL by reducing the length of the path segments and the query string
2.  Reduce query parameters: If the URL has many query parameters, consider reducing the number of parameters or use `POST` method instead where the parameters can be sent in the body of the request
3.  Use POST method: If the long URL is a result of a form submission, consider changing the form method from `GET` to `POST`
4.  Check for unintended redirection: Ensure there isn't a redirection loop or logic that is appending to the URL causing it to grow in length with each redirect

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "Error List"
description: "You may encounter a variety of errors when you interact with the Vercel platform. This section focuses on errors that can happen when you interact with the Vercel Dashboard."
last_updated: "null"
source: "https://vercel.com/docs/errors/error-list"
--------------------------------------------------------------------------------

# Error List

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Missing public directory](#missing-public-directory)

The [build step](/docs/deployments/configure-a-build) will result in an error if the output directory is missing, empty, or invalid (for example, it is not a directory). To resolve this error, you can try the following steps:

*   Make sure the [output directory](/docs/deployments/configure-a-build#output-directory) is specified correctly in project settings
*   If the output directory is correct, check the build command ([documentation](/docs/deployments/configure-a-build#build-command)) or the [root directory](/docs/deployments/configure-a-build#root-directory))
*   Try running the build command locally and make sure that the files are correctly generated in the specified output directory

## [Missing build script](#missing-build-script)

This is only relevant if you’re using Vercel CLI 16.7.3 or older.

Suppose your project contains a `package.json` file, no `api` directory, and no `vercel.json` configuration. In that case, it is expected to provide a `build` [script](https://docs.npmjs.com/misc/scripts) that performs a static build of your frontend and outputs it to a `public` directory at the root of your project.

When properly configured, your `package.json` file would look similar to this:

package.json

```
{
  "scripts": {
    "build": "[my-framework] build --output public"
  }
}
```

An example `build` script in a `package.json` file that specifies the output directory.

Once you have defined the `build` [script](https://docs.npmjs.com/misc/scripts), this error will disappear. Furthermore, it will not be displayed if you are using `package.json` purely to provide dependencies for your Vercel functions located inside the `api` directory.

## [Maximum team member requests](#maximum-team-member-requests)

The maximum amount of open requests to join a team is 10. In order to allow for more requests, the existing requests need to be approved or declined by a [Team Owner](/docs/rbac/access-roles#owner-role).

This ensures the list always remains manageable and protected against spam.

## [Inviting users to team who requested access](#inviting-users-to-team-who-requested-access)

If a user has already requested access to a team, it's impossible to invite them. Instead, their request must be approved by a [Team Owner](/docs/rbac/access-roles#owner-role) for the user to gain access.

This ensures no team invites are accidentally accepted.

## [Request access with the required Git account](#request-access-with-the-required-git-account)

When the deployment for a commit fails with the message "Team access required to deploy.", the Git account of the commit author is not connected to a Hobby team that is a member of the team.

The link attached to the error allows someone to connect their Hobby team to the Git account of the commit author. If the Hobby team is connected to a different Git account, it will fail stating that a different Git account must be used to request access to the team.

Once the Git account is connected to the Hobby team on Vercel, it is possible to request access to the team. A [Team Owner](/docs/rbac/access-roles#owner-role) can then approve or decline this access request. If the request was approved, the failed commit would be retried, and the following commits would not fail due to missing team access.

## [Blocked scopes](#blocked-scopes)

A deployment, project, user, or team on Vercel can be blocked if it violates our [fair use guidelines](/docs/limits/fair-use-guidelines) or [Terms of Service](/legal/terms).

Blocked deployments and projects will result in your website returning a 451 error. Blocked users and teams cannot create new deployments, and blocked users cannot be invited to a team. Please reach out to [registration@vercel.com](mailto:registration@vercel.com) if you need help.

## [Unused build and development settings](#unused-build-and-development-settings)

A [Project](/docs/projects/overview) has several settings that can be found in the dashboard. One of those sections, Build & Development Settings, is used to change the way a Project is built.

However, the Build & Development Settings are only applied to [zero-configuration](/guides/upgrade-to-zero-configuration) deployments.

If a deployment defines the [`builds`](/docs/project-configuration#builds) configuration property, the Build & Development Settings are ignored.

## [Unused Vercel Function region setting](#unused-vercel-function-region-setting)

A [project](/docs/projects/overview) has several settings that can be found in the dashboard. One of those settings, Vercel Function Region, is used to select the [region](/docs/regions) where your Vercel functions execute.

If a deployment defines the [`regions`](/docs/project-configuration#regions) configuration property in `vercel.json`, the Vercel Function Region setting is ignored.

If a CLI Deployment defines the [`--regions`](/docs/cli/deploy#regions) option, the Vercel Function Region setting is ignored.

## [Invalid route source pattern](#invalid-route-source-pattern)

The `source` property follows the syntax from [path-to-regexp](https://github.com/pillarjs/path-to-regexp/tree/v6.1.0), not the `RegExp` syntax.

For example, negative lookaheads must be wrapped in a group.

Before

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/(?!general)",
  "destination": "/api/feedback/general"
}
```

After

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/((?!general).*)",
  "destination": "/api/feedback/general"
}
```

## [Invalid route destination segment](#invalid-route-destination-segment)

The `source` property follows the syntax from [path-to-regexp](https://github.com/pillarjs/path-to-regexp/tree/v6.1.0).

A colon (`:`) defines the start of a [named segment parameter](https://github.com/pillarjs/path-to-regexp/tree/v6.1.0#named-parameters).

A named segment parameter defined in the `destination` property must also be defined in the `source` property.

Before

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/:type",
  "destination": "/api/feedback/:id"
}
```

After

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "source": "/feedback/:id",
  "destination": "/api/feedback/:id"
}
```

## [Failed to install builder dependencies](#failed-to-install-builder-dependencies)

When running the `vercel build` or `vercel dev` commands, `npm install` errors can be encountered if `npm` was invoked to install Builders that are defined in your `vercel.json` file.

`npm install` may fail if:

*   [`npm`](https://www.npmjs.com/get-npm) is not installed
*   Your internet connection is unavailable
*   The Builder that is defined in your configuration is not published to the npm registry

Double-check that the name and version of the Builder you are requesting is correct.

## [Mixed routing properties](#mixed-routing-properties)

If you have [`rewrites`](/docs/project-configuration#rewrites), [`redirects`](/docs/project-configuration#redirects), [`headers`](/docs/project-configuration#headers), [`cleanUrls`](/docs/project-configuration#cleanurls) or [`trailingSlash`](/docs/project-configuration#trailingslash) defined in your [configuration](/docs/project-configuration) file, then [`routes`](/docs/project-configuration#routes) cannot be defined.

This is a necessary limitation because `routes` is a lower-level primitive that contains all of the other types. Therefore, it cannot be merged safely with the new properties.

See the [Upgrading Routes](/docs/project-configuration#upgrading-legacy-routes) section for examples of `routes` compared to the new properties.

## [Conflicting configuration files](#conflicting-configuration-files)

For backward compatibility purposes, there are two naming conventions for configuration files used by Vercel CLI (for example `vercel.json` and `now.json`). Both naming conventions are supported, however only _one_ may be defined at a time. Vercel CLI will output an error message if both naming conventions are used at the same time.

These conflicting configuration errors occur if:

*   Both `vercel.json` and `now.json` exist in your project.  
    Solution: Delete the `now.json` file
*   Both `.vercel` and `.now` directories exist in your project.  
    Solution: Delete the `.now` directory
*   Both `.vercelignore` and `.nowignore` files exist in your project.  
    Solution: Delete the `.nowignore` file
*   Environment Variables that begin with `VERCEL_` have a conflicting Environment Variable that begins with `NOW_`.  
    Solution: Only define the `VERCEL_` prefixed Environment Variable

## [Conflicting functions and builds configuration](#conflicting-functions-and-builds-configuration)

There are two ways to configure Vercel functions in your project: [functions](/docs/project-configuration#functions) _or_ [`builds`](/docs/project-configuration#builds). However, only one of them may be used at a time - they cannot be used in conjunction.

For most cases, it is recommended to use the `functions` property because it supports more features, such as:

*   Allows configuration of the amount of memory that the Vercel Function is provided with
*   More reliable because it requires a specific npm package version for the `runtime` property
*   Supports "clean URLs" by default, which means that the Vercel functions are automatically accessible without their file extension in the URL

However, the [`builds`](/docs/project-configuration#builds) property will remain supported for backward compatibility purposes.

## [Unsupported functions configuration with Nextjs](#unsupported-functions-configuration-with-nextjs)

When using Next.js, only `memory` and `maxDuration` can be configured within the [functions](/docs/project-configuration#functions) property. Next.js automatically handles the other configuration values for you.

## [Deploying Vercel functions to multiple regions](#deploying-vercel-functions-to-multiple-regions)

It's possible to deploy Vercel functions to multiple regions. This functionality is only available to [Enterprise teams](/docs/plans/enterprise).

On the [Pro plan](/docs/plans/pro), the limitation has existed since the [launch](/blog/simpler-pricing) of the current pricing model but was applied on July 10, 2020. For Projects created on or after the date, it's no longer possible to deploy to multiple regions.

To select the region closest to you, read our [guide](/guides/choosing-deployment-regions) on choosing deployment regions for Vercel functions.

## [Unmatched function pattern](#unmatched-function-pattern)

The [functions](/docs/project-configuration#functions) property uses a glob pattern for each key. This pattern must match Vercel Function source files within the `api` directory.

If you are using Next.js, Vercel functions source files can be created in the following:

*   `pages/api` directory
*   `src/pages/api` directory
*   `pages` directory when the module exports [getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props)
*   `src/pages` directory when the module exports [getServerSideProps](https://nextjs.org/docs/basic-features/data-fetching/get-server-side-props)

Additionally, if you'd like to use a Vercel Function that isn't written with Node.js, and in combination with Next.js, you can place it in the `api` directory (provided by the platform), since `pages/api` (provided by Next.js) only supports JavaScript.

Not Allowed

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "users/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

Allowed

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/users/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

Allowed (Next.js)

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "pages/api/users/**/*.js": {
      "maxDuration": 30
    }
  }
}
```

## [Cannot load project settings](#cannot-load-project-settings)

If the Project configuration in `.vercel` belongs to a team you are not a member of, attempting to deploy the project will result in an error.

This can occur if you clone a Git repository that includes the `.vercel` directory, or you are logged in to the wrong Vercel account. Additionally, authentication issues can occur if you don't comply with the [two-factor enforcement](/docs/two-factor-enforcement) policy of your team.

To fix, remove the `.vercel` directory and redeploy to link the project again by running these commands.

On macOS and Linux:

rm -rf .vercel

vercel

On Windows:

rmdir /s /q .vercel

vercel

## [Project name validation](#project-name-validation)

Project names can only consist of up to one hundred alphanumeric lowercase characters. Hyphens can be used in between words in the name, but never at the start or end.

## [Repository connection limitation](#repository-connection-limitation)

The amount of Vercel Projects that can be connected with the same Git repository is [limited depending on your plan](/docs/limits#general-limits).

If you have reached the limitation and would like to connect a new project to the repository, you will need to disconnect an existing project from the same Git repository.

To increase this limit, please [contact our Sales Team](/contact/sales).

## [Domain verification through CLI](#domain-verification-through-cli)

To verify your domain, point the domain to Vercel by configuring our nameservers or a DNS Record. You can learn more about what to do for your Domain by running `vercel domains inspect <domain>`, where `<domain>` is the domain you're interested in.

Alternatively, if you already added the domain to a project, read [the configuring a domain section](/docs/projects/custom-domains#step-4:-configuring-the-domain) of the custom domain documentation.

## [Leaving the team](#leaving-the-team)

You cannot leave a team if you are the last remaining [Owner](/docs/rbac/access-roles#owner-role) or the last confirmed [Member](/docs/rbac/access-roles#member-role). In order to leave the Team, first designate a different confirmed [Member](/docs/rbac/access-roles#member-role) to be an [Team Owner](/docs/rbac/access-roles#owner-role).

If you are the only remaining [Member](/docs/rbac/access-roles#member-role), you should instead delete the Team.

## [Git Default ignore list](#git-default-ignore-list)

Deployments created using Vercel CLI will automatically [ignore several files](/docs/deployments/build-features#ignored-files-and-folders) for security and performance reasons.

However, these files are _not_ ignored for deployments created using [Git](/docs/git) and a warning is printed instead. This is because `.gitignore` determines which files should be ignored.

If the file was intentionally committed to Git, you can ignore the warning.

If the file was accidentally committed to Git, you can remove it using the following commands:

terminal

```
git rm file.txt                   # remove the file
echo 'file.txt' >> .gitignore     # append file to .gitignore
git add .gitignore                # stage the change
git commit -m "Removed file.txt"  # commit the change
git push                          # deploy the change
```

## [GitHub app installation not found](#github-app-installation-not-found)

In some cases, signing up with GitHub fails due to GitHub's database inconsistencies.

When you connected your Hobby team with your GitHub account, the [Vercel GitHub App](https://github.com/apps/vercel) was installed on your GitHub account and then GitHub notified Vercel that the app was successfully installed.

However, Vercel was unable to retrieve the app installation from GitHub, which made it appear as if the [Vercel GitHub App](https://github.com/apps/vercel) was never installed.

In order to solve this issue, wait a couple of minutes and try connecting to GitHub again. If you are still unable to connect, please contact [GitHub Support](https://support.github.com/contact) to determine why the [Vercel GitHub App](https://github.com/apps/vercel) was not able to be installed.

## [Preview branch used as production branch](#preview-branch-used-as-production-branch)

If you have configured a custom Git branch for a domain or an environment variable, it is considered a preview domain and a preview environment variable. Because of this, the Git branch configured for it is considered a [preview branch](/docs/git#preview-branches).

When configuring the production branch in the project settings, it is not possible to use a preview branch.

If you still want to use this particular Git branch as a production branch, please follow these steps:

1.  Assign your affected domains to the production environment (clear out the Git branch you've defined for them)
2.  Assign your affected environment variables to the production environment (clear out the Git branch you've defined for them)

Afterwards, you can use the Git branch you originally wanted to use as a production branch.

## [Lost Git repository access](#lost-git-repository-access)

In order for Vercel to be able to deploy commits to your Git repository, a Project on Vercel has to be connected to it.

This connection is interrupted if the Git repository is deleted, archived, or if the Vercel App was uninstalled from the corresponding Git account or Git organization. Make sure none of these things apply.

Additionally, when using GitHub, the connection is also interrupted if you or a [Team Member](/docs/rbac/access-roles#member-role) modifies the access permissions of the Vercel GitHub App installed on the respective personal GitHub account or GitHub organization.

To verify the access permissions of the Vercel GitHub App installed on your personal GitHub account, navigate to the [Applications page](https://github.com/settings/installations) and select Vercel under Installed GitHub Apps. You will see a list of Git repositories that the GitHub App has access to. Make sure that the Git repository you're looking to connect to a Vercel Project is listed there.

To verify the access permissions of the Vercel GitHub App installed on your GitHub organization, select Vercel under Installed GitHub Apps in the organization settings. You will see a list of Git repositories that the GitHub App has access to. Make sure that the Git repository you're looking to connect to a Vercel Project is listed there.

## [Production deployment cannot be redeployed](#production-deployment-cannot-be-redeployed)

You cannot redeploy a production deployment if a more recent one exists.

The reason is that redeploying an old production deployment would result in overwriting the most recent source code you have deployed to production.

To force an explicit overwrite of the current production deployment, select Promote instead.

## [SSL certificate deletion denied](#ssl-certificate-deletion-denied)

Certain SSL Certificates associated with your Hobby team or team (i.e. Wildcard SSL Certificates for your Vercel Project's staging domains) are automatically generated by the Vercel platform.

Because these SSL Certificates are managed by the Vercel platform, they cannot be manually deleted on the Vercel Dashboard – nor through Vercel CLI.

Custom SSL Certificates may be uploaded to teams on the [Enteprise plan](/docs/plans/enterprise), which are allowed to be manually deleted.

## [Production branch used as preview branch](#production-branch-used-as-preview-branch)

The Git branch that is configured using the [production branch](/docs/git#production-branch) field in the project settings, is considered the branch that contains the code served to your visitors.

If you'd like to assign a domain or environment variable to that particular Git branch, there's no need to manually fill it in.

By default, if no custom Git branch is defined for them, domains are already assigned to the production branch. The same is true for environment variables: If no custom Git branch is defined for them and Production is selected as an environment, they're already assigned to the production branch.

If you still want to enter a specific Git branch for a domain or an environment variable, it has to be a [preview branch](/docs/git#preview-branches).

## [Command not found in vercel dev](#command-not-found-in-vercel-dev)

The _"Command not found"_ error message happens when a sub-process that `vercel dev` is attempting to create is not installed on your local machine. You need to install the particular program onto your operating system before `vercel dev` will work correctly.

For example, you may see the error _"Command not found: go"_ if you are writing a Vercel Function in Go, but do not have the `go` binary installed. In this case you need to [install `go`](https://golang.org/doc/install) first, and then try invoking your Vercel Function again.

## [Recursive invocation of commands](#recursive-invocation-of-commands)

### [Why this error occurred](#why-this-error-occurred)

You have configured one of the following for your Project:

*   The [Build Command](/docs/deployments/configure-a-build#build-command) defined in the Project Settings invokes `vercel build`
*   The [Development Command](/docs/deployments/configure-a-build#development-command) defined in the Project Settings invokes `vercel dev`

Because the Build Command is invoked by `vercel build` when deploying, it cannot invoke `vercel build` itself, as that would cause an infinite recursion.

The same applies to the Development Command: When developing locally, `vercel dev` invokes the Development Command, so it cannot invoke `vercel dev` itself.

### [Possible ways to fix it](#possible-ways-to-fix-it)

Adjust the Build and Development Commands defined for your Project to not invoke `vercel build` or `vercel dev`.

Instead, they should invoke the Build Command provided by your framework.

If you are unsure about which value to provide, disable the Override option in order to default to the preferred settings for the [Framework Preset](/docs/deployments/configure-a-build#framework-preset) you have selected.

## [Pnpm engine unsupported](#pnpm-engine-unsupported)

`ERR_PNPM_UNSUPPORTED_ENGINE` occurs when `package.json#engines.pnpm` does not match the currently running version of `pnpm`.

To fix, do one of the following:

*   [Set the env var `ENABLE_EXPERIMENTAL_COREPACK` to 1](https://vercel.com/docs/deployments/configure-a-build#corepack), and make sure the `packageManager` value is set correctly in your `package.json`

package.json

```
{
  "engines": {
    "pnpm": "^7.5.1"
  },
  "packageManager": "pnpm@7.5.1"
}
```

*   Remove the [`engines.pnpm`](https://pnpm.io/package_json#engines) value from your `package.json`

You cannot use [`engine-strict`](https://pnpm.io/npmrc#engine-strict) to solve this error. `engine-strict` only handles dependencies.

## [Yarn dynamic require of "util" is not supported](#yarn-dynamic-require-of-util-is-not-supported)

This error occurs when projects use yarn, corepack, and have a `package.json` with a `type` field set to `module`. This is a known [yarn issue](https://github.com/yarnpkg/berry/issues/5831).

To prevent this error, consider the following options:

*   Remove `"type": "module"` from the project's `package.json`
*   Install yarn into the project instead of using corepack with `yarn set version [desired-version] --yarn-path`

## [Invalid Edge Config connection string](#invalid-edge-config-connection-string)

This error occurs when attempting to create a deployment where at least one of its environment variables contains an outdated Edge Config connection string. A connection string can be outdated if either the Edge Config itself was deleted or if the token used in the connection string is invalid or has been deleted.

To resolve this error, delete or update the environment variable that contains the connection string. In most cases, the environment variable is named `EDGE_CONFIG`.

## [Globally installed `@vercel/speed-insights` or `@vercel/analytics` packages](#globally-installed-@vercel/speed-insights-or-@vercel/analytics-packages)

You must reference `@vercel/speed-insights` or `@vercel/analytics` packages in your application's `package.json` file. This error occurs when you deploy your application with these packages globally available, but not referenced in your `package.json` file, like in a monorepo.

To fix this error, add the packages to your `package.json` file as a dependency.

## [Oversized Incremental Static Regeneration page](#oversized-incremental-static-regeneration-page)

[Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration) (ISR) responses that are greater than 20 MB result in pages not rendering in production with a [`FALLBACK_BODY_TOO_LARGE`](/docs/errors/FALLBACK_BODY_TOO_LARGE) error. This affects all Next.js build time pre-rendering, and other frameworks that use [Prerender Functions](/docs/build-output-api/v3/primitives#prerender-functions).

--------------------------------------------------------------------------------
title: "Feature Flags"
description: "Learn how to use feature flags with Vercel's DX platform."
last_updated: "null"
source: "https://vercel.com/docs/feature-flags"
--------------------------------------------------------------------------------

# Feature Flags

Copy page

Ask AI about this page

Last updated June 2, 2025

Feature flags are a powerful tool that allows you to control the visibility of features in your application, enabling you to ship, test, and experiment with confidence. Vercel offers various options to integrate feature flags into your application.

## [Choose how you work with flags](#choose-how-you-work-with-flags)

Vercel provides a flexible approach to working with flags, allowing you to tailor the process to your team's workflow at any stage of the lifecycle. The options can be used independently or in combination, depending on the project's needs. You can:

*   [Implement flags as code](#implementing-feature-flags-in-your-codebase), using the [Flags SDK](/docs/feature-flags/feature-flags-pattern) in Next.js or SvelteKit, or use an SDK from your existing feature flag provider.
*   [Manage feature flags](#managing-feature-flags-from-the-toolbar) through the Vercel Toolbar to view, override, and share your application's feature flags.
*   [Observe your flags](#observing-your-flags) using Vercel's observability features.
*   [Optimize your feature flags](#optimizing-your-feature-flags) by using an [Edge Config integration](/docs/edge-config/integrations).

### [Implementing Feature Flags in your codebase](#implementing-feature-flags-in-your-codebase)

If you're using Next.js or SvelteKit for your application, you can implement feature flags directly in your codebase. In Next.js, this includes using feature flags for static pages by generating multiple variants and routing between them with middleware.

*   Vercel is compatible with any feature flag provider including [LaunchDarkly](https://launchdarkly.com/), [Optimizely](https://www.optimizely.com/), [Statsig](https://statsig.com/), [Hypertune](https://www.hypertune.com/), [Split](https://www.split.io/), and custom feature flag setups.
*   [Flags SDK](/docs/feature-flags/feature-flags-pattern): A free open-source library that gives you the tools you need to use feature flags in Next.js and SvelteKit applications

### [Managing Feature Flags from the Toolbar](#managing-feature-flags-from-the-toolbar)

Flags Explorer is available on [all plans](/docs/plans)

Using the [Vercel Toolbar](/docs/vercel-toolbar), you're able to view, override, and share feature flags for your application without leaving your browser tab.

You can manage feature flags from the toolbar in any development environment that your team has [enabled the toolbar for](/docs/vercel-toolbar/in-production-and-localhost). This includes local development, preview deployments, and production deployments.

*   [Using Feature Flags in the Vercel Toolbar](/docs/feature-flags/flags-explorer): Learn how to view and override your application's feature flags from the Vercel Toolbar.
*   [Implementing Feature Flags in the Vercel Toolbar](/docs/feature-flags/flags-explorer/getting-started): Learn how to set up the Vercel Toolbar so you can see and override your application's feature flags.

### [Observing your flags](#observing-your-flags)

Web Analytics are available on [all plans](/docs/plans)

Feature flags play a crucial role in the software development lifecycle, enabling safe feature rollouts, experimentation, and A/B testing. When you integrate your feature flags with the Vercel platform, you can improve your application by using Vercel's observability features.

*   [Integrate Feature Flags with Runtime Logs](/docs/feature-flags/integrate-with-runtime-logs): Learn how to send feature flag data to Vercel logs.
*   [Integrate Feature Flags with Web Analytics](/docs/feature-flags/integrate-with-web-analytics): Learn how to tag your page views and custom events with feature flags.

### [Optimizing your feature flags](#optimizing-your-feature-flags)

Edge Config is available on [all plans](/docs/plans)

An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking. It enables you to read data at the edge without querying an external database or hitting upstream servers. With [Vercel Integrations](/docs/integrations), you can connect with external providers to synchronize their flags into your Edge Config.

With Vercel's optimizations, you can read Edge Config data at negligible latency. The vast majority of your reads will complete within 15ms at P99, or often less than 1ms.

*   [Vercel Edge Config](/docs/edge-config): Experiment with A/B testing by storing feature flags in your Edge Config.
*   [Vercel Edge Config Quickstart](/docs/edge-config/get-started): Get started with reading data from Edge Config.

--------------------------------------------------------------------------------
title: "Flags SDK"
description: "The Flags SDK is a free open-source library that gives developers the tools they need to use feature flags in Next.js and SvelteKit applications."
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/feature-flags-pattern"
--------------------------------------------------------------------------------

# Flags SDK

Copy page

Ask AI about this page

Last updated June 25, 2025

*   Works with any [flag provider](https://flags-sdk.dev/docs/adapters/supported-providers), [custom setups](https://flags-sdk.dev/docs/adapters/custom-adapters) or no flag provider at all
*   Compatible with App Router, Pages Router, and Middleware
*   Built for feature flags and experimentation

Learn more about the [Flags SDK on flags-sdk.dev](https://flags-sdk.dev).

--------------------------------------------------------------------------------
title: "Flags Explorer"
description: "View and override your application's feature flags from the Vercel Toolbar"
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/flags-explorer"
--------------------------------------------------------------------------------

# Flags Explorer

Copy page

Ask AI about this page

Last updated September 24, 2025

Flags Explorer is available on [all plans](/docs/plans)

The Flags Explorer is a feature of the [Vercel Toolbar](/docs/vercel-toolbar) that allows you to view and override your application's feature flags without leaving your browser tab. You can also share and recommend overrides to team members. Follow the [Quickstart](/docs/feature-flags/flags-explorer/getting-started) to make the Flags Explorer aware of your application's feature flags.

Quickly override feature flags for your current session without signing into your feature flag provider, and without affecting team members or automated tests using the Flags Explorer.

Team members can access the Flags Explorer once they have activated the toolbar. The Flags Explorer is available in all environments your team has [enabled the toolbar for](/docs/vercel-toolbar/in-production-and-localhost).

![Flags Explorer](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-overview-filter-light.png&w=1080&q=75)![Flags Explorer](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-overview-filter-dark.png&w=1080&q=75)

Flags Explorer

## [View and override flags in the toolbar](#view-and-override-flags-in-the-toolbar)

Before you can use with the Flags Explorer, ensure that your team has set up both [feature flags](/docs/feature-flags/flags-explorer/getting-started) and the [Vercel Toolbar](/docs/vercel-toolbar/in-production-and-localhost) in the environment you are using,

To see and override feature flags for your application:

1.  You must log into the Vercel Toolbar to interact with your application's feature flag overrides.
2.  Select the Flags Explorer option () from the Vercel Toolbar menu.
3.  Find the desired feature flag in the modal by scrolling or using the search and filter controls.
4.  Select an override value for the desired feature flag. Note that by default, overrides are not persisted and only affect the user applying them, in the environment in which they were set. To share overrides, see [Sharing flag overrides](#sharing-flag-overrides).
5.  Apply the changes. This will trigger a soft reload. If you have applied changes, the Vercel Toolbar will turn blue.

## [Sharing flag overrides](#sharing-flag-overrides)

Any overrides you apply from Vercel Toolbar usually apply to your browser session only. However, you can recommend overrides to team members by either:

*   [Setting overrides as recommended for a given branch](#branch-based-recommendations)
*   Explicitly [sharing a set of overrides through a URL](#url-based-recommendations) with a team member

### [Branch based recommendations](#branch-based-recommendations)

This workflow is great when you start working on a new feature in a branch, as the recommended overrides will travel with the branch from local development through to the preview deployment.

1.  First configure the overrides you would like to share as usual
2.  Then, select the chevron next to the branch name at the top
3.  Choose Save Recommendations to recommend these overrides to any team member visiting your branch locally or on a preview deployment

When a team member visits that branch they will get a notification suggesting to apply the overrides you recommended. Notifications are displayed on all preview deployments, but not on your production deployment.

### [URL based recommendations](#url-based-recommendations)

This workflow is great when you want to share once-off overrides with team members to reproduce a bug under certain conditions or to share a new feature.

1.  First configure the overrides you would like to share as usual
2.  Choose Share to copy a link to the page you are on, along with a query parameter containing your overrides

You can send this link to team members. When they visit the link they will get a notification suggesting to apply the overrides you shared.

## [More resources](#more-resources)

*   [Flags Explorer reference](/docs/feature-flags/flags-explorer/reference)
*   [Flags SDK](/docs/feature-flags/feature-flags-pattern)

--------------------------------------------------------------------------------
title: "Getting started with Flags Explorer"
description: "Learn how to set up the Flags Explorer so you can see and override your application's feature flags"
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/flags-explorer/getting-started"
--------------------------------------------------------------------------------

# Getting started with Flags Explorer

Copy page

Ask AI about this page

Last updated September 15, 2025

Flags Explorer is available on [all plans](/docs/plans)

This guide walks you through connecting your application to the Flags Explorer, so you can use it to view and override your application's feature flags. This works with any framework, any feature flag provider and even custom setups.

## [Prerequisites](#prerequisites)

*   Set up the [Vercel Toolbar](/docs/vercel-toolbar) for development by following [adding the Vercel Toolbar to local and production environments](/docs/vercel-toolbar/in-production-and-localhost#)
*   You should have the latest version of Vercel CLI installed. To check your version, use `vercel --version`. To [install](/docs/cli#installing-vercel-cli) or update Vercel CLI, use:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i -g vercel@latest
    ```
    
*   Ensure your local directory [links](/docs/cli/link) to a Vercel project. You can use `vercel link` from root of your project to link it to your Vercel account or use:
    
    Terminal
    
    ```
    vercel link [path-to-directory]
    ```
    

## [Quickstart](#quickstart)

1.  ### [Add the Flags SDK to your project](#add-the-flags-sdk-to-your-project)
    
    Install the `flags` package. This package provides convenience methods, components, and types that allow your application to communicate with the Flags Explorer.
    
    pnpmyarnnpmbun
    
    ```
    pnpm i flags
    ```
    
2.  ### [Adding a `FLAGS_SECRET`](#adding-a-flags_secret)
    
    This secret is used to encrypt and sign overrides, and so Flags Explorer can make authenticated requests to the `/.well-known/vercel/flags` API endpoint we'll create in the next step.
    
    Run your application locally with Vercel Toolbar enabled and open Flags Explorer from the toolbar. Click on "Start setup" to begin the onboarding flow, then click on "Create secret" to automatically generate and add a new `FLAGS_SECRET` environment variable to your project.
    
    Pull your environment variables to make them available to your project locally.
    
    Terminal
    
    ```
    vercel env pull
    ```
    
    If you prefer to create the secret manually, see the instructions in the [Flags Explorer Reference](/docs/feature-flags/flags-explorer/reference#flags_secret-environment-variable).
    
3.  ### [Creating the Flags Discovery Endpoint](#creating-the-flags-discovery-endpoint)
    
    Your application needs to expose an API endpoint that Flags Explorer queries to get your feature flags. Flags Explorer will make an authenticated request to this API endpoint to receive your application's feature flag definitions. This endpoint can communicate the name, origin, description, and available options of your feature flags.
    
    Using the Flags SDK for Next.js
    
    Ensure you completed the setup of the [Flags SDK for Next.js](https://flags-sdk.dev/docs/getting-started/next). You should have installed the `flags` package and have a `flags.ts` file at the root of your project which exposes your feature flags as shown below.
    
    Next.js (/app)Next.js (/pages)
    
    flags.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { flag } from 'flags/next';
     
    export const exampleFlag = flag({
      key: 'example-flag',
      description: 'An example feature flag',
      decide() {
        return false;
      },
    });
    ```
    
    Create your Flags Discovery Endpoint using the snippet below.
    
    Next.js (/app)Next.js (/pages)
    
    app/.well-known/vercel/flags/route.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { getProviderData, createFlagsDiscoveryEndpoint } from 'flags/next';
    import * as flags from '../../../../flags';
     
    export const GET = createFlagsDiscoveryEndpoint(() => getProviderData(flags));
    ```
    
    This endpoint uses `verifyAccess` to prevent unauthorized requests, and the `getProviderData` function to automatically generate the feature flag definitions based on the feature flags you have defined in code. See the [Flags SDK API Reference](https://flags-sdk.dev/docs/api-reference/frameworks/next#getproviderdata) for more information.
    
    If you are using the Flags SDK with adapters, use the `getProviderData` function exported by your flag provider's adapter to load flag metadata from your flag providers. See the [Flags SDK Adapters API Reference](https://flags-sdk.dev/docs/adapters/supported-providers) for more information, and [mergeProviderData](https://flags-sdk.dev/docs/api-reference/core/core#mergeproviderdata) to combine the feature flags defined in code with the metadata of providers.
    
    Using the Flags SDK for SvelteKit
    
    If you are using the Flags SDK for SvelteKit then the `createHandle` function will automatically create the API endpoint for you. Learn more about [using the Flags SDK for SvelteKit](https://flags-sdk.dev/docs/getting-started/sveltekit).
    
    Using a custom setup
    
    Learn how to manually return feature flag definitions in the [Flags Explorer Reference](/docs/feature-flags/flags-explorer/reference#verifying-a-request-to-the-api-endpoint).
    
4.  ### [Handling overrides](#handling-overrides)
    
    You can now use the Flags Explorer to create feature flag overrides. When you create an override Flags Explorer will set a cookie containing those overrides. Your application can then read this cookie and respect those overrides. You can optionally check the signature on the overrides cookie to ensure it originated from a trusted source.
    
    Using the Flags SDK for Next.js
    
    Feature flags defined in code using the Flags SDK for Next.js will automatically handle overrides set by the Flags Explorer.
    
    Using the Flags SDK for SvelteKit
    
    Feature flags defined in code using the Flags SDK for SvelteKit will automatically handle overrides set by the Flags Explorer.
    
    Using a custom setup
    
    If you have a custom feature flag setup, or if you are using the SDKs of feature flag providers directly, you need to manually handle the overrides set by the Flags Explorer.
    
    Learn how to read the overrides cookie in the [Flags Explorer Reference](/docs/feature-flags/flags-explorer/reference#override-cookie).
    
5.  ### [Emitting flag values (optional)](#emitting-flag-values-optional)
    
    You can optionally make the Flags Explorer aware of the actual value each feature flag resolved to while rendering the current page by rendering a `<FlagValues />` component. This is useful for debugging. Learn how to emit flag values in the [Flags Explorer Reference](/docs/feature-flags/flags-explorer/reference#values).
    
    ![Flags Explorer showing flag values.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-default-value-light.png&w=1080&q=75)![Flags Explorer showing flag values.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-default-value-dark.png&w=1080&q=75)
    
    Flags Explorer showing flag values.
    
    If you emit flag values to the client it's further possible to annotate your Web Analytics events with the feature flags you emitted. Learn how to [integrate with Web Analytics](/docs/feature-flags/integrate-with-web-analytics).
    
6.  ### [Review](#review)
    
    You should now be able to see your feature flags in Flags Explorer. You should also be able to set overrides that your application can respect by using the Flags SDK or reading the `vercel-flag-overrides` cookie manually. If you added the `FlagValues` component, you should be able to see the actual value each flag resolved to while rendering the current page.
    

## [More resources](#more-resources)

*   [Flags Explorer Reference](/docs/feature-flags/flags-explorer/reference)
*   [Flags SDK](/docs/feature-flags/feature-flags-pattern)
*   [Feature Flags using Next.js example](/templates/next.js/shirt-shop-feature-flags)

--------------------------------------------------------------------------------
title: "Pricing for Flags Explorer"
description: "Learn about pricing for Flags Explorer."
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/flags-explorer/limits-and-pricing"
--------------------------------------------------------------------------------

# Pricing for Flags Explorer

Copy page

Ask AI about this page

Last updated May 9, 2025

Flags Explorer is available on [all plans](/docs/plans)

## [Pricing](#pricing)

The following table outlines the price for each resource according to the plan you are on:

| Resource | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| Unlimited Overrides | N/A | $250.00 per month | $250.00 per month |

Unlimited overrides can be managed in your [team's billing settings](/d?to=%2Fteams%2F%5Bteam%5D%2Fsettings%2Fbilling&title=Go+to+Billing+Settings). Alternatively, if you have the necessary permissions, you can enable this feature directly in the Flags Explorer once you reach the limit.

### [Limits per plan](#limits-per-plan)

When not subscribed to the unlimited option, Hobby, Pro and Enterprise have a limited amount of monthly overrides:

|  | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| Overrides | 150 per month | 150 per month | 150 per month |

One override directly translates to one click on the apply button of the Flags Explorer, which means that multiple flags can be overriden in one go.

--------------------------------------------------------------------------------
title: "Reference"
description: "In-depth reference for configuring the Flags Explorer"
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/flags-explorer/reference"
--------------------------------------------------------------------------------

# Reference

Copy page

Ask AI about this page

Last updated September 24, 2025

Flags Explorer is available on [all plans](/docs/plans)

The Flags Explorer has five main concepts: the [API Endpoint](/docs/feature-flags/flags-explorer/reference#api-endpoint), the [FLAGS\_SECRET environment variable](/docs/feature-flags/flags-explorer/reference#flags_secret-environment-variable), the [override cookie](/docs/feature-flags/flags-explorer/reference#override-cookie), [flag definitions](/docs/feature-flags/flags-explorer/reference#definitions), and [flag values](/docs/feature-flags/flags-explorer/reference#values).

## [Definitions](#definitions)

The Flags Explorer needs to know about your feature flags before it can display them.

Flag definitions are metadata for your feature flags, which communicate:

*   Name
*   URL for where your team can manage the flag
*   Description
*   Possible values and their (optional) labels

A definition can never communicate the value of a flag as they load independently from [flag values](/docs/feature-flags/flags-explorer/reference#values). See [flag definitions](/docs/feature-flags/flags-explorer/reference#definitions) for more information.

```
{
  "bannerFlag": {
    "origin": "https://example.com/flag/bannerFlag",
    "description": "Determines whether the banner is shown",
    "options": [
      { "value": true, "label": "on" },
      { "value": false, "label": "off" }
    ]
  }
}
```

This is how Vercel Toolbar shows flag definitions:

![Flags Explorer showing flag values.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-definitions-light.png&w=1080&q=75)![Flags Explorer showing flag values.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-definitions-dark.png&w=1080&q=75)

Flags Explorer showing flag values.

There are two ways to provide your feature flags to the Flags Explorer:

1.  [Returning definitions through the Flags API Endpoint](/docs/feature-flags/flags-explorer/reference#returning-definitions-through-the-flags-api-endpoint)
2.  [Embedding definitions through script tags](/docs/feature-flags/flags-explorer/reference#embedding-definitions-through-script-tags)

### [Returning definitions through the Flags API Endpoint](#returning-definitions-through-the-flags-api-endpoint)

The Flags API Endpoint is the recommended way to provide your feature flags to the Flags Explorer. The Flags Explorer will request your application's [Flags API Endpoint](/docs/feature-flags/flags-explorer/reference#api-endpoint) to fetch the feature flag definitions and other settings.

See [Definitions properties](/docs/feature-flags/flags-explorer/reference#definitions-properties) for a full list of properties you can return from your Flags API Endpoint.

### [Embedding definitions through script tags](#embedding-definitions-through-script-tags)

We strongly recommend communicating your feature flag definitions through the [Flags API Endpoint](/docs/feature-flags/flags-explorer/reference#api-endpoint). In rare cases, it can be useful to communicate feature flag definitions through the HTML response. Vercel Toolbar will pick up any script tags included in the DOM which have a `data-flag-definitions` attribute.

If you are using React or Next.js, use the [`FlagsDefinitions`](https://flags-sdk.dev/docs/api-reference/core/react#flagdefinitions) component. If you are using another framework or no framework at all you can render these script tags manually. The expected shape is:

```
type FlagDefinitionsType = Record<
  string,
  {
    options?: {
      value: any;
      label?: string;
    }[];
    origin?: string;
    description?: string;
  }
>;
```

This example shows how to communicate a feature flag definition through the DOM:

```
<script type="application/json" data-flag-definitions>
  {
    "showBanner": {
      "description": "Shows or hide the banner",
      "origin": "https://example.com/showBanner",
      "options": [
        { "value": false, "label": "Hide" },
        { "value": true, "label": "Show" }
      ]
    }
  }
</script>
```

You can also encrypt the definitions before emitting them to prevent leaking your feature flags through the DOM.

```
import { safeJsonStringify } from 'flags';
 
<script type="application/json" data-flag-definitions>
  ${safeJsonStringify(definitions)}
</script>;
```

Using `JSON.stringify` within script tags leads to [XSS vulnerabilities](https://owasp.org/www-community/attacks/xss/). Use `safeJsonStringify` exported by `flags` to stringify safely.

## [Values](#values)

Your Flags API Endpoint returns your application's feature flag definitions containing information like their key, description, origin, and available options. However the Flags API Endpoint can not return the value a flag evaluated to, since this value might depend on the request which rendered the page initially.

You can optionally provide the values of your feature flags to Flags Explorer in two ways:

1.  [Emitting values using the React components](/docs/feature-flags/flags-explorer/reference#emitting-values-using-the-flagvalues-react-component)
2.  [Embedding values through script tags](/docs/feature-flags/flags-explorer/reference#embedding-values-through-script-tags)

Emitted values will show up in the Flags Explorer, and will be used by [Web Analytics to annotate events](/docs/feature-flags/integrate-with-web-analytics).

This is how Vercel Toolbar shows flag values:

![Default Feature Flag Values in Vercel Toolbar.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-default-value-light.png&w=1080&q=75)![Default Feature Flag Values in Vercel Toolbar.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-explorer-default-value-dark.png&w=1080&q=75)

Default Feature Flag Values in Vercel Toolbar.

Any JSON-serializable values are supported. Flags Explorer combines these values with any definitions, if they are present.

```
{ "bannerFlag": true, "buttonColor": "blue" }
```

### [Emitting values using the FlagValues React component](#emitting-values-using-the-flagvalues-react-component)

The `flags` package exposes React components which allow making the Flags Explorer aware of your feature flag's values.

Next.js (/app)Next.js (/pages)

app/page.tsx

TypeScript

TypeScriptJavaScript

```
import { FlagValues } from 'flags/react';
 
export function Page() {
  return (
    <div>
      {/* Some other content */}
      <FlagValues values={{ exampleFlag: true }} />
    </div>
  );
}
```

The approaches above will add the names and values of your feature flags to the DOM in plain text. Use the `encrypt` function to keep your feature flags confidential.

Next.js (/app)Next.js (/pages)

app/page.tsx

TypeScript

TypeScriptJavaScript

```
import { Suspense } from 'react';
import { encryptFlagValues, type FlagValuesType } from 'flags';
import { FlagValues } from 'flags/react';
 
async function ConfidentialFlagValues({ values }: { values: FlagValuesType }) {
  const encryptedFlagValues = await encryptFlagValues(values);
  return <FlagValues values={encryptedFlagValues} />;
}
 
export default function Page() {
  const values: FlagValuesType = { exampleFlag: true };
 
  return (
    <div>
      {/* Some other content */}
      <Suspense fallback={null}>
        <ConfidentialFlagValues values={values} />
      </Suspense>
    </div>
  );
}
```

The `FlagValues` component will emit a script tag with a `data-flag-values` attribute, which get picked up by the Flags Explorer. Flags Explorer then combines the flag values with the definitions returned by your API endpoint. If you are not using React or Next.js you can render these script tags manually as shown in the next section.

### [Embedding values through script tags](#embedding-values-through-script-tags)

Flags Explorer scans the DOM for script tags with the `data-flag-values` attribute. Any changes to content get detected by a mutation observer.

You can emit the values of feature flags to the Flags Explorer by rendering script tags with the `data-flag-values` attribute.

```
<script type="application/json" data-flag-values>
  {
    "showBanner": true,
    "showAds": false,
    "pricing": 5
  }
</script>
```

Be careful when creating these script tags. Using `JSON.stringify` within script tags leads to [XSS vulnerabilities](https://owasp.org/www-community/attacks/xss/). Use `safeJsonStringify` exported by `flags` to stringify safely.

The expected shape is:

```
type FlagValues = Record<string, any>;
```

To prevent disclosing feature flag names and values to the client, the information can be encrypted. This keeps the feature flags confidential. Use the Flags SDK's `encryptFlagValues` function together with the `FLAGS_SECRET` environment variable to encrypt your flag values on the server before rendering them on the client. The Flags Explorer will then read these encrypted values and use the `FLAGS_SECRET` from your project to decrypt them.

```
import { encryptFlagValues, safeJsonStringify } from 'flags';
 
// Encrypt your flags and their values on the server.
const encryptedFlagValues = await encryptFlagValues({
  showBanner: true,
  showAds: false,
  pricing: 5,
});
 
// Render the encrypted values on the client.
// Note: Use `safeJsonStringify` to ensure `encryptedFlagValues` is correctly formatted as JSON.
//       This step may vary depending on your framework or setup.
<script type="application/json" data-flag-values>
  {safeJsonStringify(encryptedFlagValues)}
</script>;
```

## [`FLAGS_SECRET` environment variable](#flags_secret-environment-variable)

This secret gates access to the Flags API endpoint, and optionally enables signing and encrypting feature flag overrides set by Vercel Toolbar. As described below, you can ensure that the request is authenticated in your [Flags API endpoint](/docs/feature-flags/flags-explorer/reference#api-endpoint), by using [`verifyAccess`](https://flags-sdk.dev/docs/api-reference/core/core#verifyaccess).

You can create this secret by following the instructions in the [Flags Explorer Quickstart](/docs/feature-flags/flags-explorer/getting-started#adding-a-flags_secret). Alternatively, you can create the `FLAGS_SECRET` manually by following the instructions below.

Manually creating the `FLAGS_SECRET`

The `FLAGS_SECRET` value must have a specific length (32 random bytes encoded in base64) to work as an encryption key. You can create one using node:

Terminal

```
node -e "console.log(crypto.randomBytes(32).toString('base64url'))"
```

In your local environment, pull your environment variables with `vercel env pull` to make them available to your project.

The `FLAGS_SECRET` environment variable must be defined in your project settings on the Vercel dashboard. Defining the environment variable locally is not enough as Flags Explorer reads the environment variable from your project settings.

## [API endpoint](#api-endpoint)

When you have set the [`FLAGS_SECRET`](/docs/feature-flags/flags-explorer/reference#flags_secret-environment-variable) environment variable in your project, Flags Explorer will request your application's [Flags API endpoint](/docs/feature-flags/flags-explorer/reference#api-endpoint). This endpoint should return a configuration for the Flags Explorer that includes the flag definitions.

### [Verifying a request to the API endpoint](#verifying-a-request-to-the-api-endpoint)

Your endpoint should call `verifyAccess` to ensure the request to load flags originates from Vercel Toolbar. This prevents your feature flag definitions from being exposed publicly thorugh the API endpoint. The `Authorization` header sent by Vercel Toolbar contains proof that whoever made this request has access to `FLAGS_SECRET`. The secret itself is not sent over the network.

If the `verifyAccess` check fails, you should return status code `401` and no response body. When the `verifyAccess` check is successful, return the feature flag definitions and other configuration as JSON:

Using the Flags SDK

Next.js (/app)Next.js (/pages)

app/.well-known/vercel/flags/route.ts

TypeScript

TypeScriptJavaScript

```
import { getProviderData, createFlagsDiscoveryEndpoint } from 'flags/next';
import * as flags from '../../../../flags';
 
export const GET = createFlagsDiscoveryEndpoint(() => getProviderData(flags));
```

Using a custom setup

If you are not using the Flags SDK to define feature flags in code, or if you are not using Next.js or SvelteKit, you need to manually return the feature flag definitions from your API endpoint.

Next.js (/app)Next.js (/pages)

app/.well-known/vercel/flags/route.ts

TypeScript

TypeScriptJavaScript

```
import { NextResponse, type NextRequest } from 'next/server';
import { verifyAccess, type ApiData } from 'flags';
 
export async function GET(request: NextRequest) {
  const access = await verifyAccess(request.headers.get('Authorization'));
  if (!access) return NextResponse.json(null, { status: 401 });
 
  return NextResponse.json<ApiData>({
    definitions: {
      newFeature: {
        description: 'Controls whether the new feature is visible',
        origin: 'https://example.com/#new-feature',
        options: [
          { value: false, label: 'Off' },
          { value: true, label: 'On' },
        ],
      },
    },
  });
}
```

### [Valid JSON response](#valid-json-response)

The JSON response must have the following shape

```
type ApiData = {
  definitions: Record<
    string,
    {
      description?: string;
      origin?: string;
      options?: { value: any; label?: string }[];
    }
  >;
  hints?: { key: string; text: string }[];
  overrideEncryptionMode?: 'plaintext' | 'encrypted';
};
```

### [Definitions properties](#definitions-properties)

These are your application's feature flags. You can return the following data for each definition:

| Property | Type | Description |
| --- | --- | --- |
| `description` (optional) | string | A description of what this feature flag is for. |
| `origin` (optional) | string | The URL where feature flag is managed. This usually points to the flag details page in your feature flag provider. |
| `options` (optional) | `{ value: any, label?: string }[]` | An array of options. These options will be available as overrides in Vercel Toolbar. |

You can optionally tell Vercel Toolbar about the actual value flags resolved to. The Flags API Endpoint cannot return this as the value might differ for each request. See [Flag values](/docs/feature-flags/flags-explorer/reference#values) instead.

### [Hints](#hints)

In some cases you might need to fetch your feature flag definitions from your feature flag provider before you can return them from the Flags API Endpoint.

In case this request fails you can use `hints`. Any hints returned will show up in the UI.

This is useful when you are fetching your feature flags from multiple sources. In case one request fails you might still want to show the remaining flags on a best effort basis, while also displaying a hint that fetching a specific source failed. You can return `definitions` and `hints` simultaneously to do so.

### [Override mode](#override-mode)

When you create an override, Vercel Toolbar will set a cookie called `vercel-flag-overrides`. You can read this cookie in your applications to make your application respect the overrides set by Vercel Toolbar.

The `overrideEncryptionMode` setting controls the value of the cookie:

*   `plaintext`: The cookie will contain the overrides as plain JSON. Be careful not to trust those overrides as users can manipulate the value easily.
*   `encrypted`: Vercel Toolbar will encrypt overrides using the `FLAGS_SECRET` before storing them in the cookie. This prevents manipulation, but requries decrypting them on your end before usage.

We highly recommend using `encrypted` mode as it protects against manipulation.

## [Override cookie](#override-cookie)

The Flags Explorer will set a cookie called `vercel-flag-overrides` containing the overrides.

Using the Flags SDK

If you use the Flags SDK for Next.js or SvelteKit, the SDK will automatically handle the overrides set by the Flags Explorer.

Manual setup

Read this cookie and use the `decrypt` function to decrypt the overrides and use them in your application. The decrypted value is a JSON object containing the name and override value of each overridden flag.

Next.js (/app)Next.js (/pages)

app/getFlags.ts

TypeScript

TypeScriptJavaScript

```
import { type FlagOverridesType, decryptOverrides } from 'flags';
import { cookies } from 'next/headers';
 
async function getFlags() {
  const overrideCookie = cookies().get('vercel-flag-overrides')?.value;
  const overrides = overrideCookie
    ? await decryptOverrides<FlagOverridesType>(overrideCookie)
    : null;
 
  return {
    exampleFlag: overrides?.exampleFlag ?? false,
  };
}
```

## [Script tags](#script-tags)

Vercel Toolbar uses a [MutationObserver](https://developer.mozilla.org/docs/Web/API/MutationObserver) to find all script tags with `data-flag-values` and `data-flag-definitions` attributes. Any changes to content get detected by the toolbar.

For more information, see the following sections:

*   [Embedding definitions through script tags](/docs/feature-flags/flags-explorer/reference#embedding-definitions-through-script-tags)
*   [Embedding values through script tags](/docs/feature-flags/flags-explorer/reference#embedding-values-through-script-tags)

--------------------------------------------------------------------------------
title: "Integrating with the Vercel Platform"
description: "Integrate your feature flags with the Vercel Platform."
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/integrate-vercel-platform"
--------------------------------------------------------------------------------

# Integrating with the Vercel Platform

Copy page

Ask AI about this page

Last updated September 24, 2025

Feature flags play a crucial role in the software development lifecycle, enabling safe feature rollouts, experimentation, and A/B testing. When you integrate your feature flags with the Vercel platform, you can improve your application by using Vercel's observability features.

By making the Vercel platform aware of the feature flags used in your application, you can gain insights in the following ways:

*   Runtime Logs: See your feature flag's values in [Runtime Logs](/docs/runtime-logs)
*   Web Analytics: Break down your pageviews and custom events by feature flags in [Web Analytics](/docs/analytics)

To get started, follow these guides:

*   [Integrate Feature Flags with Runtime Logs](/docs/feature-flags/integrate-with-runtime-logs)
*   [Integrate Feature Flags with Web Analytics](/docs/feature-flags/integrate-with-web-analytics)

--------------------------------------------------------------------------------
title: "Integrate flags with Runtime Logs"
description: "Integrate your feature flag provider with runtime logs."
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/integrate-with-runtime-logs"
--------------------------------------------------------------------------------

# Integrate flags with Runtime Logs

Copy page

Ask AI about this page

Last updated September 24, 2025

Runtime Logs integration is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

On your dashboard, the [Logs](/docs/runtime-logs) tab displays your [runtime logs](/docs/runtime-logs#what-are-runtime-logs). It can also display any feature flags your application evaluated while handling requests.

![Feature Flags section in runtime logs](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Flogs-light.png&w=1080&q=75)![Feature Flags section in runtime logs](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Flogs-dark.png&w=1080&q=75)

Feature Flags section in runtime logs

To make the runtime logs aware of your feature flag call `reportValue(name, value)` with the flag name and value to be reported. Each call to `reportValue` will show up as a distinct entry, even when the same key is used:

Next.js (/app)Next.js (/pages)

app/api/test/route.ts

TypeScript

TypeScriptJavaScript

```
import { reportValue } from 'flags';
 
export async function GET() {
  reportValue('summer-sale', false);
  return Response.json({ ok: true });
}
```

If you are using an implementation of the [Feature Flags pattern](/docs/feature-flags/feature-flags-pattern) you don't need to call `reportValue`. The respective implementation will automatically call `reportValue` for you.

## [Limits](#limits)

The following limits apply to reported values:

*   Keys are truncated to 256 characters
*   Values are truncated to 256 characters
*   Reported values must be JSON serializable or they will be ignored

--------------------------------------------------------------------------------
title: "Integrate flags with Vercel Web Analytics"
description: "Learn how to tag your page views and custom events with feature flags"
last_updated: "null"
source: "https://vercel.com/docs/feature-flags/integrate-with-web-analytics"
--------------------------------------------------------------------------------

# Integrate flags with Vercel Web Analytics

Copy page

Ask AI about this page

Last updated September 24, 2025

Web Analytics integration is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

![Feature Flags section in Vercel Web Analytics](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-in-web-analytics-light.png&w=3840&q=75)![Feature Flags section in Vercel Web Analytics](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Ffeature-flags%2Fflags-in-web-analytics-dark.png&w=3840&q=75)

Feature Flags section in Vercel Web Analytics

## [Client-side tracking](#client-side-tracking)

Vercel Web Analytics can look up the values of evaluated feature flags in the DOM. It can then enrich page views and client-side events with these feature flags.

1.  ### [Emit feature flags and connect them to Vercel Web Analytics](#emit-feature-flags-and-connect-them-to-vercel-web-analytics)
    
    To share your feature flags with Web Analytics you have to emit your feature flag values to the DOM as described in [Supporting Feature Flags](/docs/feature-flags/flags-explorer/reference#values).
    
    This will automatically annotate all page views and client-side events with your feature flags.
    
2.  ### [Tracking feature flags in client-side events](#tracking-feature-flags-in-client-side-events)
    
    Client-side events in Web Analytics will now automatically respect your flags and attach those to custom events.
    
    To manually overwrite the tracked flags for a specific `track` event, call:
    
    component.ts
    
    ```
    import { track } from '@vercel/analytics';
     
    track('My Event', {}, { flags: ['summer-sale'] });
    ```
    
    If the flag values on the client are encrypted, the entire encrypted string becomes part of the event payload. This can lead to the event getting reported without any flags when the encrypted string exceeds size limits.
    

## [Server-side tracking](#server-side-tracking)

To track feature flags in server-side events:

1.  First, report the feature flag value using `reportValue` to make the flag show up in [Runtime Logs](/docs/runtime-logs):
    
    app/api/test/route.ts
    
    ```
    import { reportValue } from 'flags';
     
    export async function GET() {
      reportValue('summer-sale', false);
      return Response.json({ ok: true });
    }
    ```
    
2.  Once reported, any calls to `track` can look up the feature flag while handling a specific request:
    
    app/api/test/route.ts
    
    ```
    import { track } from '@vercel/analytics/server';
    import { reportValue } from 'flags';
     
    export async function GET() {
      reportValue('summer-sale', false);
      track('My Event', {}, { flags: ['summer-sale'] });
     
      return Response.json({ ok: true });
    }
    ```
    

If you are using an implementation of the [Feature Flags Pattern](/docs/feature-flags/feature-flags-pattern) you don't need to call `reportValue`. The respective implementation will automatically call `reportValue` for you.

--------------------------------------------------------------------------------
title: "Fluid compute"
description: "Learn about fluid compute, an execution model for Vercel Functions that provides a more flexible and efficient way to run your functions."
last_updated: "null"
source: "https://vercel.com/docs/fluid-compute"
--------------------------------------------------------------------------------

# Fluid compute

Copy page

Ask AI about this page

Last updated October 27, 2025

Fluid compute offers a blend of serverless flexibility and server-like capabilities. Unlike traditional [serverless architectures](/docs/fundamentals/what-is-compute#serverless), which can face issues such as cold starts and [limited functionalities](/docs/fundamentals/what-is-compute#serverless-disadvantages), fluid compute provides a hybrid solution. It overcomes the limitations of both serverless and server-based approaches, delivering the advantages of both worlds, including:

*   [Zero configuration out of the box](/docs/fluid-compute#default-settings-by-plan): Fluid compute comes with preset defaults that automatically optimize your functions for both performance and cost efficiency.
*   [Optimized concurrency](/docs/fluid-compute#optimized-concurrency): Optimize resource usage by handling multiple invocations within a single function instance. Can be used with the Node.js and Python runtimes.
*   Dynamic scaling: Fluid compute automatically optimizes existing resources before scaling up to meet traffic demands. This ensures low latency during high-traffic events and cost efficiency during quieter periods.
*   Background processing: After fulfilling user requests, you can continue executing background tasks using [`waitUntil`](/docs/functions/functions-api-reference/vercel-functions-package#waituntil). This allows for a responsive user experience while performing time-consuming operations like logging and analytics in the background.
*   Automatic cold start optimizations: Reduces the effects of cold starts through [automatic bytecode optimization](/docs/fluid-compute#bytecode-caching), and function pre-warming on production deployments.
*   Cross-region and availability zone failover: Ensure high availability by first failing over to [another availability zone (AZ)](/docs/functions/configuring-functions/region#automatic-failover) within the same region if one goes down. If all zones in that region are unavailable, Vercel automatically redirects traffic to the next closest region. Zone-level failover also applies to non-fluid deployments.
*   Error isolation: Unhandled errors won't crash other concurrent requests running on the same instance, maintaining reliability without sacrificing performance.

See [what is compute?](/docs/fundamentals/what-is-compute) to learn more about fluid compute and how it compares to traditional serverless models.

## [Enabling fluid compute](#enabling-fluid-compute)

As of April 23, 2025, fluid compute is enabled by default for new projects.

You can enable fluid compute through the Vercel dashboard or by configuring your `vercel.json` file for specific environments or deployments.

### [Enable for entire project](#enable-for-entire-project)

To enable fluid compute through the dashboard:

1.  Navigate to your project's [Functions Settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Ffunctions&title=Go+to+Functions+Settings) in the dashboard
2.  Locate the Fluid Compute section
3.  Toggle the switch to enable fluid compute for your project
4.  Click Save to apply the changes
5.  Deploy your project for the changes to take effect

When you enable it through the dashboard, fluid compute applies to all deployments for that project by default.

### [Enable for specific environments and deployments](#enable-for-specific-environments-and-deployments)

You can programmatically enable fluid compute using the [`fluid` property](/docs/project-configuration#fluid) in your `vercel.json` file. This approach is particularly useful for:

*   Testing on specific environments: Enable fluid compute only for custom environments environments when using branch tracking
*   Per-deployment configuration: Test fluid compute on individual deployments before enabling it project-wide

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "fluid": true
}
```

## [Available runtime support](#available-runtime-support)

Fluid compute is available for the following runtimes:

*   [Node.js](/docs/functions/runtimes/node-js)
*   [Python](/docs/functions/runtimes/python)
*   [Edge](/docs/functions/runtimes/edge)

## [Optimized concurrency](#optimized-concurrency)

Fluid compute allows multiple invocations to share a single function instance, this is especially valuable for AI applications, where tasks like fetching embeddings, querying vector databases, or calling external APIs can be I/O-bound. By allowing concurrent execution within the same instance, you can reduce cold starts, minimize latency, and lower compute costs.

![How multiple requests are processed in the fluid compute model with optimized concurrency.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Ffluid%2Fserverless-active-light.avif&w=3840&q=75)![How multiple requests are processed in the fluid compute model with optimized concurrency.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Ffluid%2Fserverless-active-dark.avif&w=3840&q=75)

How multiple requests are processed in the fluid compute model with optimized concurrency.

Vercel Functions prioritize existing idle resources before allocating new ones, reducing unnecessary compute usage. This in-function-concurrency is especially effective when multiple requests target the same function, leading to fewer total resources needed for the same workload.

Optimized concurrency in fluid compute is available when using Node.js or Python runtimes. See the [efficient serverless Node.js with in-function concurrency](/blog/serverless-servers-node-js-with-in-function-concurrency) blog post to learn more.

## [Bytecode caching](#bytecode-caching)

When using [Node.js version 20+](/docs/functions/runtimes/node-js/node-js-versions), Vercel Functions use bytecode caching to reduce cold start times. This stores the compiled bytecode of JavaScript files after their first execution, eliminating the need for recompilation during subsequent cold starts.

As a result, the first request isn't cached yet. However, subsequent requests benefit from the cached bytecode, enabling faster initialization. This optimization is especially beneficial for functions that are not invoked that often, as they will see faster cold starts and reduced latency for end users.

Bytecode caching is only applied to production environments, and is not available in development or preview deployments.

For [frameworks](/docs/frameworks) that output ESM, all CommonJS dependencies (for example, `react`, `node-fetch`) will be opted into bytecode caching.

## [Isolation boundaries and global state](#isolation-boundaries-and-global-state)

On traditional serverless compute, the isolation boundary refers to the separation of individual instances of a function to ensure they don't interfere with each other. This provides a secure execution environment for each function.

However, because each function uses a microVM for isolation, which can lead to slower start-up times, you can see an increase in resource usage due to idle periods when the microVM remains inactive.

Fluid compute uses a different approach to isolation. Instead of using a microVM for each function invocation, multiple invocations can share the same physical instance (a global state/process) concurrently. This allows functions to share resources and execute in the same environment, which can improve performance and reduce costs.

When [uncaught exceptions](https://nodejs.org/api/process.html#event-uncaughtexception) or [unhandled rejections](https://nodejs.org/api/process.html#event-unhandledrejection) happen in Node.js, Fluid compute logs the error and lets current requests finish before stopping the process. This means one broken request won't crash other requests running on the same instance and you get the reliability of traditional serverless with the performance benefits of shared resources.

## [Default settings by plan](#default-settings-by-plan)

Fluid Compute includes default settings that vary by plan:

| Settings | Hobby | Pro | Enterprise |
| --- | --- | --- | --- |
| [CPU configuration](/docs/functions/configuring-functions/memory#memory-/-cpu-type) | Standard | Standard / Performance | Standard / Performance |
| [Default / Max duration](/docs/functions/limitations#max-duration) | 300s (5 minutes) / 300s (5 minutes) | 300s (5 minutes) / 800s (13 minutes) | 300s (5 minutes) / 800s (13 minutes) |
| [Multi-region failover](/docs/functions/configuring-functions/region#automatic-failover) |  |  |  |
| [Multi-region functions](/docs/functions/runtimes#location) |  | Up to 3 | All |

## [Order of settings precedence](#order-of-settings-precedence)

The settings you configure in your [function code](/docs/functions/configuring-functions), [dashboard](/dashboard), or [`vercel.json`](/docs/project-configuration) file will override the default fluid compute settings.

The following order of precedence determines which settings take effect. Settings you define later in the sequence will always override those defined earlier:

| Precedence | Stage | Explanation | Can Override |
| --- | --- | --- | --- |
| 1 | Function code | Settings in your function code always take top priority. These include max duration defined directly in your code. | [`maxDuration`](/docs/functions/configuring-functions/duration) |
| 2 | `vercel.json` | Any settings in your [`vercel.json`](/docs/project-configuration) file, like max duration, and region, will override dashboard and Fluid defaults. | [`maxDuration`](/docs/functions/configuring-functions/duration), [`region`](/docs/functions/configuring-functions/region) |
| 3 | Dashboard | Changes made in the dashboard, such as max duration, region, or CPU, override Fluid defaults. | [`maxDuration`](/docs/functions/configuring-functions/duration), [`region`](/docs/functions/configuring-functions/region), [`memory`](/docs/functions/configuring-functions/memory) |
| 4 | Fluid defaults | These are the default settings applied automatically when fluid compute is enabled, and do not configure any other settings. |  |

## [Pricing and usage](#pricing-and-usage)

See the [fluid compute pricing](/docs/functions/usage-and-pricing) documentation for details on how fluid compute is priced, including active CPU, provisioned memory, and invocations.

--------------------------------------------------------------------------------
title: "Frameworks on Vercel"
description: "Vercel supports a wide range of the most popular frameworks, optimizing how your application builds and runs no matter what tool you use."
last_updated: "null"
source: "https://vercel.com/docs/frameworks"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./08-framework-environment-variables.md) | [Index](./index.md) | [Next →](./10-frameworks-on-vercel.md)
