**Navigation:** [← Previous](./35-use-supabase-auth-with-nextjs.md) | [Index](./index.md) | [Next →](./37-send-email-hook.md)

# Error Codes

Learn about the Auth error codes and how to resolve them


## Auth error codes

Supabase Auth can return various errors when using its API. This guide explains how to handle these errors effectively across different programming languages.



## Error types

Supabase Auth errors are generally categorized into two main types:

*   API Errors: Originate from the Supabase Auth API.
*   Client Errors: Originate from the client library's state.

Client errors differ by language so do refer to the appropriate section below:

<Tabs scrollable size="small" type="underlined">
  <TabPanel id="javascript" label="JavaScript">
    All errors originating from the `supabase.auth` namespace of the client library will be wrapped by the `AuthError` class.

    Error objects are split in a few classes:

    *   `AuthApiError` -- errors which originate from the Supabase Auth API.
        *   Use `isAuthApiError` instead of `instanceof` checks to see if an error you caught is of this type.
    *   `CustomAuthError` -- errors which generally originate from state in the client library.
        *   Use the `name` property on the error to identify the class of error received.

    Errors originating from the server API classed as `AuthApiError` always have a `code` property that can be used to identify the error returned by the server. The `status` property is also present, encoding the HTTP status code received in the response.
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    All errors originating from the `supabase.auth` namespace of the client library will be wrapped by the `AuthException` class.

    Error objects are split in a few classes. `AuthApiException` is an exception which originates from the Supabase Auth API.

    Errors originating from the server API classed as `AuthApiException` always have a `code` property that can be used to identify the error returned by the server. The `statusCode` property is also present, encoding the HTTP status code received in the response.
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    All errors originating from the `supabase.auth` namespace of the client library will be a case of the `AuthError` enum.

    The `api(message:errorCode:underlyingData:underlyingResponse:)` case is a special case for errors which originates from the Supabase Auth API, this error always have an `errorCode` property that can be used to identify the error returned by the server.
  </TabPanel>

  <TabPanel id="python" label="Python">
    All errors originating from the `supabase.auth` namespace of the client library will be wrapped by the `AuthError` class.

    Error objects are split in a few classes. `AuthApiError` is an error which originate from the Supabase Auth API.

    Errors originating from the server API classed as `AuthApiError` always have a `code` property that can be used to identify the error returned by the server. The `status` property is also present, encoding the HTTP status code received in the response.
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    All exceptions originating from the `supabase.auth` namespace of the Kotlin client library will be a subclass of `RestException`.

    Rest exceptions are split into a few classes:

    *   `AuthRestException` -- exceptions which originate from the Supabase Auth API and have a `errorCode` property that can be used to identify the error returned by the server.
    *   `AuthWeakPasswordException` -- an `AuthRestException` which indicates that the password is too weak.
    *   `AuthSessionMissingException` -- an `AuthRestException` which indicates that the session is missing, if the user was logged out or deleted.

    All instances and subclasses of a `AuthRestException` have a `errorCode` property that can be used to identify the error returned by the server.
  </TabPanel>
</Tabs>



## HTTP status codes

Below are the most common HTTP status codes you might encounter, along with their meanings in the context of Supabase Auth:

{/* supa-mdx-lint-disable Rule001HeadingCase */}


### [403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403)

Sent out in rare situations where a certain Auth feature is not available for the user, and you as the developer are not checking a precondition whether that API is available for the user.


### [422 Unprocessable Entity](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422)

Sent out when the API request is accepted, but cannot be processed because the user or Auth server is in a state where it cannot satisfy the request.


### [429 Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)

Sent out when rate-limits are breached for an API. You should handle this status code often, especially in functions that authenticate a user.


### [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)

Indicate that the Auth server's service is degraded. Most often it points to issues in your database setup such as a misbehaving trigger on a schema, function, view or other database object.


### [501 Not Implemented](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/501)

Sent out when a feature is not enabled on the Auth server, and you are trying to use an API which requires it.

{/* supa-mdx-lint-enable Rule001HeadingCase */}



## Auth error codes table

The following table provides a comprehensive list of error codes you may encounter when working with Supabase Auth. Each error code is associated with a specific issue and includes a description to help you understand and resolve the problem efficiently.

<ErrorCodes service="auth" />



## Best practices for error handling

*   Always use `error.code` and `error.name` to identify errors, not string matching on error messages.
*   Avoid relying solely on HTTP status codes, as they may change unexpectedly.



# Multi-Factor Authentication (Phone)




## How does phone multi-factor-authentication work?

Phone multi-factor authentication involves a shared code generated by Supabase Auth and the end user. The code is delivered via a messaging channel, such as SMS or WhatsApp, and the user uses the code to authenticate to Supabase Auth.

The phone messaging configuration for MFA is shared with [phone auth login](/docs/guides/auth/phone-login). The same provider configuration that is used for phone login is used for MFA. You can also use the [Send SMS Hook](/docs/guides/auth/auth-hooks/send-sms-hook) if you need to use an MFA (Phone) messaging provider different from what is supported natively.

Below is a flow chart illustrating how the Enrollment and Verify APIs work in the context of MFA (Phone).

<Image
  alt="Diagram showing the flow of Multi-Factor authentication"
  src={{
    light: '/docs/img/guides/auth-mfa/auth-mfa-phone-flow.svg',
    dark: '/docs/img/guides/auth-mfa/auth-mfa-phone-flow.svg',
  }}
  containerClassName="max-w-[700px]"
/>


### Add enrollment flow

An enrollment flow provides a UI for users to set up additional authentication factors. Most applications add the enrollment flow in two places within their app:

1.  Right after login or sign up.
    This allows users quickly set up Multi Factor Authentication (MFA) post login or account creation. Where possible, encourage all users to set up MFA. Many applications offer this as an opt-in step in an
    effort to reduce onboarding friction.
2.  From within a settings page.
    Allows users to set up, disable or modify their MFA settings.

As far as possible, maintain a generic flow that you can reuse in both cases with minor modifications.

Enrolling a factor for use with MFA takes three steps for phone MFA:

1.  Call `supabase.auth.mfa.enroll()`.
2.  Calling the `supabase.auth.mfa.challenge()` API. This sends a code via SMS or WhatsApp and prepares Supabase Auth to accept a verification code from the user.
3.  Calling the `supabase.auth.mfa.verify()` API. `supabase.auth.mfa.challenge()` returns a challenge ID.
    This verifies that the code issued by Supabase Auth matches the code input by the user. If the verification succeeds, the factor
    immediately becomes active for the user account. If not, you should repeat
    steps 2 and 3.


#### Example: React

Below is an example that creates a new `EnrollMFA` component that illustrates the important pieces of the MFA enrollment flow.

*   When the component appears on screen, the `supabase.auth.mfa.enroll()` API is
    called once to start the process of enrolling a new factor for the current
    user.
*   A challenge is created using the `supabase.auth.mfa.challenge()` API and the
    code from the user is submitted for verification using the
    `supabase.auth.mfa.verify()` challenge.
*   `onEnabled` is a callback that notifies the other components that enrollment
    has completed.
*   `onCancelled` is a callback that notifies the other components that the user
    has clicked the `Cancel` button.

```tsx
export function EnrollMFA({
  onEnrolled,
  onCancelled,
}: {
  onEnrolled: () => void
  onCancelled: () => void
}) {
  const [phoneNumber, setPhoneNumber] = useState('')
  const [factorId, setFactorId] = useState('')
  const [verifyCode, setVerifyCode] = useState('')
  const [error, setError] = useState('')
  const [challengeId, setChallengeId] = useState('')

  const onEnableClicked = () => {
    setError('')
    ;(async () => {
      const verify = await auth.mfa.verify({
        factorId,
        challengeId,
        code: verifyCode,
      })
      if (verify.error) {
        setError(verify.error.message)
        throw verify.error
      }

      onEnrolled()
    })()
  }
  const onEnrollClicked = async () => {
    setError('')
    try {
      const factor = await auth.mfa.enroll({
        phone: phoneNumber,
        factorType: 'phone',
      })
      if (factor.error) {
        setError(factor.error.message)
        throw factor.error
      }

      setFactorId(factor.data.id)
    } catch (error) {
      setError('Failed to Enroll the Factor.')
    }
  }

  const onSendOTPClicked = async () => {
    setError('')
    try {
      const challenge = await auth.mfa.challenge({ factorId })
      if (challenge.error) {
        setError(challenge.error.message)
        throw challenge.error
      }

      setChallengeId(challenge.data.id)
    } catch (error) {
      setError('Failed to resend the code.')
    }
  }

  return (
    <>
      {error && <div className="error">{error}</div>}
      <input
        type="text"
        placeholder="Phone Number"
        value={phoneNumber}
        onChange={(e) => setPhoneNumber(e.target.value.trim())}
      />
      <input
        type="text"
        placeholder="Verification Code"
        value={verifyCode}
        onChange={(e) => setVerifyCode(e.target.value.trim())}
      />
      <input type="button" value="Enroll" onClick={onEnrollClicked} />
      <input type="button" value="Submit Code" onClick={onEnableClicked} />
      <input type="button" value="Send OTP Code" onClick={onSendOTPClicked} />
      <input type="button" value="Cancel" onClick={onCancelled} />
    </>
  )
}
```


### Add a challenge step to login

Once a user has logged in via their first factor (email+password, magic link, one time password, social login etc.) you need to perform a check if any additional factors need to be verified.

This can be done by using the `supabase.auth.mfa.getAuthenticatorAssuranceLevel()` API. When the user signs in and is redirected back to your app, you should call this method to extract the user's current and next authenticator assurance level (AAL).

Therefore if you receive a `currentLevel` which is `aal1` but a `nextLevel` of `aal2`, the user should be given the option to go through MFA.

Below is a table that explains the combined meaning.

| Current Level | Next Level | Meaning                                                  |
| ------------: | :--------- | :------------------------------------------------------- |
|        `aal1` | `aal1`     | User does not have MFA enrolled.                         |
|        `aal1` | `aal2`     | User has an MFA factor enrolled but has not verified it. |
|        `aal2` | `aal2`     | User has verified their MFA factor.                      |
|        `aal2` | `aal1`     | User has disabled their MFA factor. (Stale JWT.)         |


#### Example: React

Adding the challenge step to login depends heavily on the architecture of your app. However, a fairly common way to structure React apps is to have a large component (often named `App`) which contains most of the authenticated application logic.

This example will wrap this component with logic that will show an MFA challenge screen if necessary, before showing the full application. This is illustrated in the `AppWithMFA` example below.

```tsx
function AppWithMFA() {
  const [readyToShow, setReadyToShow] = useState(false)
  const [showMFAScreen, setShowMFAScreen] = useState(false)

  useEffect(() => {
    ;(async () => {
      try {
        const { data, error } = await supabase.auth.mfa.getAuthenticatorAssuranceLevel()
        if (error) {
          throw error
        }

        console.log(data)

        if (data.nextLevel === 'aal2' && data.nextLevel !== data.currentLevel) {
          setShowMFAScreen(true)
        }
      } finally {
        setReadyToShow(true)
      }
    })()
  }, [])

  if (readyToShow) {
    if (showMFAScreen) {
      return <AuthMFA />
    }

    return <App />
  }

  return <></>
}
```

*   `supabase.auth.mfa.getAuthenticatorAssuranceLevel()` does return a promise.
    Don't worry, this is a very fast method (microseconds) as it rarely uses the
    network.
*   `readyToShow` only makes sure the AAL check completes before showing any
    application UI to the user.
*   If the current level can be upgraded to the next one, the MFA screen is
    shown.
*   Once the challenge is successful, the `App` component is finally rendered on
    screen.

Below is the component that implements the challenge and verify logic.

```tsx
function AuthMFA() {
  const [verifyCode, setVerifyCode] = useState('')
  const [error, setError] = useState('')
  const [factorId, setFactorId] = useState('')
  const [challengeId, setChallengeId] = useState('')
  const [phoneNumber, setPhoneNumber] = useState('')

  const startChallenge = async () => {
    setError('')
    try {
      const factors = await supabase.auth.mfa.listFactors()
      if (factors.error) {
        throw factors.error
      }

      const phoneFactor = factors.data.phone[0]

      if (!phoneFactor) {
        throw new Error('No phone factors found!')
      }

      const factorId = phoneFactor.id
      setFactorId(factorId)
      setPhoneNumber(phoneFactor.phone)

      const challenge = await supabase.auth.mfa.challenge({ factorId })
      if (challenge.error) {
        setError(challenge.error.message)
        throw challenge.error
      }

      setChallengeId(challenge.data.id)
    } catch (error) {
      setError(error.message)
    }
  }

  const verifyCode = async () => {
    setError('')
    try {
      const verify = await supabase.auth.mfa.verify({
        factorId,
        challengeId,
        code: verifyCode,
      })
      if (verify.error) {
        setError(verify.error.message)
        throw verify.error
      }
    } catch (error) {
      setError(error.message)
    }
  }

  return (
    <>
      <div>Please enter the code sent to your phone.</div>
      {phoneNumber && <div>Phone number: {phoneNumber}</div>}
      {error && <div className="error">{error}</div>}
      <input
        type="text"
        value={verifyCode}
        onChange={(e) => setVerifyCode(e.target.value.trim())}
      />
      {!challengeId ? (
        <input type="button" value="Start Challenge" onClick={startChallenge} />
      ) : (
        <input type="button" value="Verify Code" onClick={verifyCode} />
      )}
    </>
  )
}
```

*   You can extract the available MFA factors for the user by calling
    `supabase.auth.mfa.listFactors()`. Don't worry this method is also very quick
    and rarely uses the network.
*   If `listFactors()` returns more than one factor (or of a different type) you
    should present the user with a choice. For simplicity this is not shown in
    the example.
*   Phone numbers are unique per user. Users can only have one verified phone factor with a given phone number.
    Attempting to enroll a new phone factor alongside an existing verified factor with the same number will result in an error.
*   Each time the user presses the "Submit" button a new challenge is created for
    the chosen factor (in this case the first one)
*   On successful verification, the client library will refresh the session in
    the background automatically and finally call the `onSuccess` callback, which
    will show the authenticated `App` component on screen.


### Security configuration

Each code is valid for up to 5 minutes, after which a new one can be sent. Successive codes remain valid until expiry. When possible choose the longest code length acceptable to your use case, at a minimum of 6. This can be configured in the [Authentication Settings](/dashboard/project/_/auth/mfa).

Be aware that Phone MFA is vulnerable to SIM swap attacks where an attacker will call a mobile provider and ask to port the target's phone number to a new SIM card and then use the said SIM card to intercept an MFA code. Evaluate the your application's tolerance for such an attack. You can read more about SIM swapping attacks [here](https://en.wikipedia.org/wiki/SIM_swap_scam)



## Pricing

<Price price="0.1027" /> per hour (<Price price="75" /> per month) for the first project. <Price price="0.0137" /> per
hour (<Price price="10" /> per month) for every additional project.

| Plan       | Project 1 per month  | Project 2 per month  | Project 3 per month  |
| ---------- | -------------------- | -------------------- | -------------------- |
| Pro        | <Price price="75" /> | <Price price="10" /> | <Price price="10" /> |
| Team       | <Price price="75" /> | <Price price="10" /> | <Price price="10" /> |
| Enterprise | Custom               | Custom               | Custom               |

For a detailed breakdown of how charges are calculated, refer to [Manage Advanced MFA Phone usage](/docs/guides/platform/manage-your-usage/advanced-mfa-phone).



# Multi-Factor Authentication (TOTP)




## How does app authenticator multi-factor authentication work?

App Authenticator (TOTP) multi-factor authentication involves a timed one-time password generated from an authenticator app in the control of users. It uses a QR Code which to transmit a shared secret used to generate a One Time Password. A user can scan a QR code with their phone to capture a shared secret required for subsequent authentication.

The use of a QR code was [initially introduced by Google Authenticator](https://github.com/google/google-authenticator/wiki/Key-Uri-Format) but is now universally accepted by all authenticator apps. The QR code has an alternate representation in URI form following the `otpauth` scheme such as: `otpauth://totp/supabase:alice@supabase.com?secret=<secret>&issuer=supabase` which a user can manually input in cases where there is difficulty rendering a QR Code.

Below is a flow chart illustrating how the Enrollment, Challenge, and Verify APIs work in the context of MFA (TOTP).

<Image
  alt="Diagram showing the flow of Multi-Factor authentication"
  src={{
    light: '/docs/img/guides/auth-mfa/auth-mfa-flow.svg',
    dark: '/docs/img/guides/auth-mfa/auth-mfa-flow.svg',
  }}
  containerClassName="max-w-[700px]"
/>

[TOTP MFA API](/docs/reference/javascript/auth-mfa-api) is free to use and is enabled on all Supabase projects by default.


### Add enrollment flow

An enrollment flow provides a UI for users to set up additional authentication factors. Most applications add the enrollment flow in two places within their app:

1.  Right after login or sign up.
    This lets users quickly set up MFA immediately after they log in or create an
    account. We recommend encouraging all users to set up MFA if that makes sense
    for your application. Many applications offer this as an opt-in step in an
    effort to reduce onboarding friction.
2.  From within a settings page.
    Allows users to set up, disable or modify their MFA settings.

Enrolling a factor for use with MFA takes three steps:

1.  Call `supabase.auth.mfa.enroll()`.
    This method returns a QR code and a secret. Display the QR
    code to the user and ask them to scan it with their authenticator application.
    If they are unable to scan the QR code, show the secret in plain text which
    they can type or paste into their authenticator app.
2.  Calling the `supabase.auth.mfa.challenge()` API.
    This prepares Supabase Auth to accept a verification code from the user
    and returns a challenge ID. In the case of Phone MFA this step also sends the verification code to the user.
3.  Calling the `supabase.auth.mfa.verify()` API.
    This verifies that the user has indeed added the secret from step (1) into
    their app and is working correctly. If the verification succeeds, the factor
    immediately becomes active for the user account. If not, you should repeat
    steps 2 and 3.


#### Example: React

Below is an example that creates a new `EnrollMFA` component that illustrates the important pieces of the MFA enrollment flow.

*   When the component appears on screen, the `supabase.auth.mfa.enroll()` API is
    called once to start the process of enrolling a new factor for the current
    user.
*   This API returns a QR code in the SVG format, which is shown on screen using
    a normal `<img>` tag by encoding the SVG as a data URL.
*   Once the user has scanned the QR code with their authenticator app, they
    should enter the verification code within the `verifyCode` input field and
    click on `Enable`.
*   A challenge is created using the `supabase.auth.mfa.challenge()` API and the
    code from the user is submitted for verification using the
    `supabase.auth.mfa.verify()` challenge.
*   `onEnabled` is a callback that notifies the other components that enrollment
    has completed.
*   `onCancelled` is a callback that notifies the other components that the user
    has clicked the `Cancel` button.

```tsx
/**
 * EnrollMFA shows a simple enrollment dialog. When shown on screen it calls
 * the `enroll` API. Each time a user clicks the Enable button it calls the
 * `challenge` and `verify` APIs to check if the code provided by the user is
 * valid.
 * When enrollment is successful, it calls `onEnrolled`. When the user clicks
 * Cancel the `onCancelled` callback is called.
 */
export function EnrollMFA({
  onEnrolled,
  onCancelled,
}: {
  onEnrolled: () => void
  onCancelled: () => void
}) {
  const [factorId, setFactorId] = useState('')
  const [qr, setQR] = useState('') // holds the QR code image SVG
  const [verifyCode, setVerifyCode] = useState('') // contains the code entered by the user
  const [error, setError] = useState('') // holds an error message

  const onEnableClicked = () => {
    setError('')
    ;(async () => {
      const challenge = await supabase.auth.mfa.challenge({ factorId })
      if (challenge.error) {
        setError(challenge.error.message)
        throw challenge.error
      }

      const challengeId = challenge.data.id

      const verify = await supabase.auth.mfa.verify({
        factorId,
        challengeId,
        code: verifyCode,
      })
      if (verify.error) {
        setError(verify.error.message)
        throw verify.error
      }

      onEnrolled()
    })()
  }

  useEffect(() => {
    ;(async () => {
      const { data, error } = await supabase.auth.mfa.enroll({
        factorType: 'totp',
      })
      if (error) {
        throw error
      }

      setFactorId(data.id)

      // Supabase Auth returns an SVG QR code which you can convert into a data
      // URL that you can place in an <img> tag.
      setQR(data.totp.qr_code)
    })()
  }, [])

  return (
    <>
      {error && <div className="error">{error}</div>}
      <img src={qr} />
      <input
        type="text"
        value={verifyCode}
        onChange={(e) => setVerifyCode(e.target.value.trim())}
      />
      <input type="button" value="Enable" onClick={onEnableClicked} />
      <input type="button" value="Cancel" onClick={onCancelled} />
    </>
  )
}
```


### Add a challenge step to login

Once a user has logged in via their first factor (email+password, magic link, one time password, social login etc.) you need to perform a check if any additional factors need to be verified.

This can be done by using the `supabase.auth.mfa.getAuthenticatorAssuranceLevel()` API. When the user signs in and is redirected back to your app, you should call this method to extract the user's current and next authenticator assurance level (AAL).

Therefore if you receive a `currentLevel` which is `aal1` but a `nextLevel` of `aal2`, the user should be given the option to go through MFA.

Below is a table that explains the combined meaning.

| Current Level | Next Level | Meaning                                                  |
| ------------: | :--------- | :------------------------------------------------------- |
|        `aal1` | `aal1`     | User does not have MFA enrolled.                         |
|        `aal1` | `aal2`     | User has an MFA factor enrolled but has not verified it. |
|        `aal2` | `aal2`     | User has verified their MFA factor.                      |
|        `aal2` | `aal1`     | User has disabled their MFA factor. (Stale JWT.)         |


#### Example: React

Adding the challenge step to login depends heavily on the architecture of your app. However, a fairly common way to structure React apps is to have a large component (often named `App`) which contains most of the authenticated application logic.

This example will wrap this component with logic that will show an MFA challenge screen if necessary, before showing the full application. This is illustrated in the `AppWithMFA` example below.

```tsx
function AppWithMFA() {
  const [readyToShow, setReadyToShow] = useState(false)
  const [showMFAScreen, setShowMFAScreen] = useState(false)

  useEffect(() => {
    ;(async () => {
      try {
        const { data, error } = await supabase.auth.mfa.getAuthenticatorAssuranceLevel()
        if (error) {
          throw error
        }

        console.log(data)

        if (data.nextLevel === 'aal2' && data.nextLevel !== data.currentLevel) {
          setShowMFAScreen(true)
        }
      } finally {
        setReadyToShow(true)
      }
    })()
  }, [])

  if (readyToShow) {
    if (showMFAScreen) {
      return <AuthMFA />
    }

    return <App />
  }

  return <></>
}
```

*   `supabase.auth.mfa.getAuthenticatorAssuranceLevel()` does return a promise.
    Don't worry, this is a very fast method (microseconds) as it rarely uses the
    network.
*   `readyToShow` only makes sure the AAL check completes before showing any
    application UI to the user.
*   If the current level can be upgraded to the next one, the MFA screen is
    shown.
*   Once the challenge is successful, the `App` component is finally rendered on
    screen.

Below is the component that implements the challenge and verify logic.

```tsx
function AuthMFA() {
  const [verifyCode, setVerifyCode] = useState('')
  const [error, setError] = useState('')

  const onSubmitClicked = () => {
    setError('')
    ;(async () => {
      const factors = await supabase.auth.mfa.listFactors()
      if (factors.error) {
        throw factors.error
      }

      const totpFactor = factors.data.totp[0]

      if (!totpFactor) {
        throw new Error('No TOTP factors found!')
      }

      const factorId = totpFactor.id

      const challenge = await supabase.auth.mfa.challenge({ factorId })
      if (challenge.error) {
        setError(challenge.error.message)
        throw challenge.error
      }

      const challengeId = challenge.data.id

      const verify = await supabase.auth.mfa.verify({
        factorId,
        challengeId,
        code: verifyCode,
      })
      if (verify.error) {
        setError(verify.error.message)
        throw verify.error
      }
    })()
  }

  return (
    <>
      <div>Please enter the code from your authenticator app.</div>
      {error && <div className="error">{error}</div>}
      <input
        type="text"
        value={verifyCode}
        onChange={(e) => setVerifyCode(e.target.value.trim())}
      />
      <input type="button" value="Submit" onClick={onSubmitClicked} />
    </>
  )
}
```

*   You can extract the available MFA factors for the user by calling
    `supabase.auth.mfa.listFactors()`. Don't worry this method is also very quick
    and rarely uses the network.
*   If `listFactors()` returns more than one factor (or of a different type) you
    should present the user with a choice. For simplicity this is not shown in
    the example.
*   Each time the user presses the "Submit" button a new challenge is created for
    the chosen factor (in this case the first one) and it is immediately
    verified. Any errors are displayed to the user.
*   On successful verification, the client library will refresh the session in
    the background automatically and finally call the `onSuccess` callback, which
    will show the authenticated `App` component on screen.



## Frequently asked questions

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6 [&>div]:space-y-4">
  <AccordionItem header={<span className="text-foreground">What's inside the QR code?</span>} id="what-is-inside-the-qr-code" />

  <AccordionItem header={<span className="text-foreground">How long is the TOTP code valid for?</span>} id="how-long-is-the-totp-code-valid-for">
    In our TOTP implementation, each generated code remains valid for one interval, which spans 30 seconds. To account for minor time discrepancies, we allow for a one-interval clock skew. This ensures that users can successfully authenticate within this timeframe, even if there are slight variations in system clocks.
  </AccordionItem>
</Accordion>



# Before User Created Hook

Prevent unwanted signups by inspecting and rejecting user creation requests

This hook runs before a new user is created. It allows developers to inspect the incoming user object and optionally reject the request. Use this to enforce custom signup policies that Supabase Auth does not handle natively - such as blocking disposable email domains, restricting access by region or IP, or requiring that users belong to a specific email domain.

You can implement this hook using an HTTP endpoint or a Postgres function. If the hook returns an error object, the signup is denied and the user is not created. If the hook responds successfully (HTTP 200 or 204 with no error), the request proceeds as usual. This gives you full control over which users are allowed to register — and the flexibility to apply that logic server-side.



## Inputs

Supabase Auth will send a payload containing these fields to your hook:

| Field      | Type     | Description                                                                               |
| ---------- | -------- | ----------------------------------------------------------------------------------------- |
| `metadata` | `object` | Metadata about the request. Includes IP address, request ID, and hook type.               |
| `user`     | `object` | The user record that is about to be created. Matches the shape of the `auth.users` table. |

<Admonition type="note">
  Because the hook is ran just before the insertion into the database, this user will not be found in Postgres at the time the hook is called.
</Admonition>

<Tabs scrollable size="small" type="underlined">
  <TabPanel id="before-user-created-json" label="JSON">
    ```json
    {
      "metadata": {
        "uuid": "8b34dcdd-9df1-4c10-850a-b3277c653040",
        "time": "2025-04-29T13:13:24.755552-07:00",
        "name": "before-user-created",
        "ip_address": "127.0.0.1"
      },
      "user": {
        "id": "ff7fc9ae-3b1b-4642-9241-64adb9848a03",
        "aud": "authenticated",
        "role": "",
        "email": "valid.email@supabase.com",
        "phone": "",
        "app_metadata": {
          "provider": "email",
          "providers": ["email"]
        },
        "user_metadata": {},
        "identities": [],
        "created_at": "0001-01-01T00:00:00Z",
        "updated_at": "0001-01-01T00:00:00Z",
        "is_anonymous": false
      }
    }
    ```
  </TabPanel>

  <TabPanel id="before-user-created-json-schema" label="JSON Schema">
    ```json
    {
      "type": "object",
      "properties": {
        "metadata": {
          "type": "object",
          "properties": {
            "uuid": {
              "type": "string",
              "format": "uuid"
            },
            "time": {
              "type": "string",
              "format": "date-time"
            },
            "ip_address": {
              "type": "string",
              "format": "ipv4"
            },
            "name": {
              "type": "string",
              "enum": ["before-user-created"]
            }
          },
          "required": ["uuid", "time", "ip_address", "name"]
        },
        "user": {
          "type": "object",
          "properties": {
            "id": { "type": "string", "format": "uuid" },
            "aud": { "type": "string" },
            "role": { "type": "string" },
            "email": { "type": "string", "format": "email" },
            "phone": { "type": "string" },
            "app_metadata": {
              "type": "object",
              "properties": {
                "provider": { "type": "string" },
                "providers": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              },
              "required": ["provider", "providers"]
            },
            "user_metadata": { "type": "object" },
            "identities": {
              "type": "array",
              "items": { "type": "object" }
            },
            "created_at": { "type": "string", "format": "date-time" },
            "updated_at": { "type": "string", "format": "date-time" },
            "is_anonymous": { "type": "boolean" }
          },
          "required": [
            "id",
            "aud",
            "role",
            "email",
            "phone",
            "app_metadata",
            "user_metadata",
            "identities",
            "created_at",
            "updated_at",
            "is_anonymous"
          ]
        }
      },
      "required": ["metadata", "user"]
    }
    ```
  </TabPanel>
</Tabs>



## Outputs

Your hook must return a response that either allows or blocks the signup request.

| Field   | Type     | Description                                                                                           |
| ------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `error` | `object` | (Optional) Return this to reject the signup. Includes a code, message, and optional HTTP status code. |

Returning an empty object with a `200` or `204` status code allows the request to proceed. Returning a JSON response with an `error` object and a `4xx` status code blocks the request and propagates the error message to the client. See the [error handling documentation](/docs/guides/auth/auth-hooks#error-handling) for more details.


### Allow the signup

```json
{}
```

or with a `204 No Content` response:

```http
HTTP/1.1 204 No Content
```


### Reject the signup with an error

```json
{
  "error": {
    "http_code": 400,
    "message": "Only company emails are allowed to sign up."
  }
}
```

This response will block the user creation and return the error message to the client that attempted signup.



## Examples

Each of the following examples shows how to use the `before-user-created` hook to control signup behavior. Each use case includes both a HTTP implementation (e.g. using an Edge Function) and a SQL implementation (Postgres function).

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="sql-allow-by-domain">
      <TabPanel id="sql-allow-by-domain" label="Allow by Domain">
        Allow signups only from specific domains like supabase.com or example.test. Reject all others. This is useful for private/internal apps, enterprise gating, or invite-only beta access.

        The `before-user-created` hook solves this by:

        *   Detecting that a user is about to be created
        *   Providing the email address in the `user.email` field

        Run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `signup_email_domains` table with some sample data and a `hook_restrict_signup_by_email_domain` function to be called by the `before-user-created` auth hook.

        ```sql
        -- Create ENUM type for domain rule classification
        do $$ begin
          create type signup_email_domain_type as enum ('allow', 'deny');
        exception
          when duplicate_object then null;
        end $$;

        -- Create the signup_email_domains table
        create table if not exists public.signup_email_domains (
          id serial primary key,
          domain text not null,
          type signup_email_domain_type not null,
          reason text default null,
          created_at timestamptz not null default now(),
          updated_at timestamptz not null default now()
        );

        -- Create a trigger to maintain updated_at
        create or replace function update_signup_email_domains_updated_at()
        returns trigger as $$
        begin
          new.updated_at = now();
          return new;
        end;
        $$ language plpgsql;

        drop trigger if exists trg_signup_email_domains_set_updated_at on public.signup_email_domains;

        create trigger trg_signup_email_domains_set_updated_at
        before update on public.signup_email_domains
        for each row
        execute procedure update_signup_email_domains_updated_at();

        -- Seed example data
        insert into public.signup_email_domains (domain, type, reason) values
          ('supabase.com', 'allow', 'Internal signups'),
          ('gmail.com', 'deny', 'Public email provider'),
          ('yahoo.com', 'deny', 'Public email provider');

        -- Create the function
        create or replace function public.hook_restrict_signup_by_email_domain(event jsonb)
        returns jsonb
        language plpgsql
        as $$
        declare
          email text;
          domain text;
          is_allowed int;
          is_denied int;
        begin
          email := event->'user'->>'email';
          domain := split_part(email, '@', 2);

          -- Check for allow match
          select count(*) into is_allowed
          from public.signup_email_domains
          where type = 'allow' and lower(domain) = lower($1);

          if is_allowed > 0 then
            return '{}'::jsonb;
          end if;

          -- Check for deny match
          select count(*) into is_denied
          from public.signup_email_domains
          where type = 'deny' and lower(domain) = lower($1);

          if is_denied > 0 then
            return jsonb_build_object(
              'error', jsonb_build_object(
                'message', 'Signups from this email domain are not allowed.',
                'http_code', 403
              )
            );
          end if;

          -- No match, allow by default
          return '{}'::jsonb;
        end;
        $$;

        -- Permissions
        grant execute
          on function public.hook_restrict_signup_by_email_domain
          to supabase_auth_admin;

        revoke execute
          on function public.hook_restrict_signup_by_email_domain
          from authenticated, anon, public;
        ```
      </TabPanel>

      <TabPanel id="sql-block-by-oauth-provider" label="Block by OAuth Provider">
        Some applications want to **allow sign-ins with a provider like Discord only for users who already exist**, while blocking new account creation via that provider. This prevents unwanted signups through OAuth flows and enables tighter control over who can join the app.

        The `before-user-created` hook solves this by:

        *   Detecting that a user is about to be created
        *   Allowing you to inspect the `app_metadata.provider`
        *   Knowing the request came from an OAuth flow

        Run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `hook_reject_discord_signups` function to be called by the `before-user-created` auth hook.

        ```sql
        -- Create the function
        create or replace function public.hook_reject_discord_signups(event jsonb)
        returns jsonb
        language plpgsql
        as $$
        declare
          provider text;
        begin
          provider := event->'user'->'app_metadata'->>'provider';

          if provider = 'discord' then
            return jsonb_build_object(
              'error', jsonb_build_object(
                'message', 'Signups with Discord are not allowed.',
                'http_code', 403
              )
            );
          end if;

          return '{}'::jsonb;
        end;
        $$;

        -- Permissions
        grant execute
          on function public.hook_reject_discord_signups
          to supabase_auth_admin;

        revoke execute
          on function public.hook_reject_discord_signups
          from authenticated, anon, public;
        ```
      </TabPanel>

      <TabPanel id="sql-allow-deny-by-cidr" label="Allow/Deny by IP or CIDR">
        This example shows how you might restrict sign up from a single IP address or a range of them using [PostgreSQL’s built-in](https://www.postgresql.org/docs/current/datatype-net-types.html) `inet` and `<<` operators for [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) -- a method of representing IP address ranges.
        For instance: `123.123.123.123/32` represents only a single IP address, while `123.123.123.0/24` means all IP addresses starting with `123.123.123.`.

        The `before-user-created` hook solves this by:

        *   Detecting that a user is about to be created
        *   Providing the IP address in the `metadata.ip_address` field

        Run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `signup_networks` table with some sample data and a `hook_restrict_signup_by_network` function to be called by the `before-user-created` auth hook.

        ```sql SQL_EDITOR
        -- Create ENUM type for network rule classification
        create type signup_network_type as enum ('allow', 'deny');

        -- Create the signup_networks table for controlling sign-up access by CIDR
        create table if not exists public.signup_networks (
          id serial primary key,
          cidr cidr not null,
          type public.signup_network_type not null,
          reason text default null,
          note text default null,
          created_at timestamp with time zone not null default now(),
          constraint signup_networks_cidr_key unique (cidr)
        );

        -- Assign appropriate permissions
        grant all
          on table public.signup_networks
          to supabase_auth_admin;

        revoke all
          on table public.signup_networks
          from authenticated, anon, public;

        -- Insert some sample data into the table
        insert into public.signup_networks (cidr, type, reason, note)
        values
          ('192.0.2.0/24', 'allow', '', 'Corporate VPN'),
          ('198.51.100.158/32', 'deny',
            'Your IP Address has been blocked for abuse.',
            'blocked by abuse: (Ticket: ABUSE-185)'),
          ('203.0.113.0/24', 'deny',
            'Your network has been blocked for abuse.',
            'blocked by abuse: (Ticket: ABUSE-212)');

        -- Create the hook function to be called by the auth server
        create or replace function public.hook_restrict_signup_by_network(event jsonb)
        returns jsonb
        language plpgsql
        as $$
        declare
          ip inet;
          allow_count int;
          deny_count int;
        begin
          ip := event->'metadata'->>'ip_address';

          -- Step 1: Check for explicit allow
          select count(*) into allow_count
          from public.signup_networks
          where type = 'allow' and ip::inet << cidr;

          if allow_count > 0 then
            -- If explicitly allowed, allow signup
            return '{}'::jsonb;
          end if;

          -- Step 2: Check for explicit deny
          select count(*) into deny_count
          from public.signup_networks
          where type = 'deny' and ip::inet << cidr;

          if deny_count > 0 then
            return jsonb_build_object(
              'error', jsonb_build_object(
                'message', 'Signups are not allowed from your network.',
                'http_code', 403
              )
            );
          end if;

          -- Step 3: No match: allow by default
          return '{}'::jsonb;
        end;
        $$;

        -- Assign permissions
        grant execute
          on function public.hook_restrict_signup_by_network
          to supabase_auth_admin;

        revoke execute
          on function public.hook_restrict_signup_by_network
          from authenticated, anon, public;
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="http-allow-by-domain">
      <TabPanel id="http-allow-by-domain" label="Allow by Domain">
        Allow signups only from specific domains like supabase.com or example.test. Reject all others. This is useful for private/internal apps, enterprise gating, or invite-only beta access.

        The `before-user-created` hook solves this by:

        *   Detecting that a user is about to be created
        *   Providing the email address in the `user.email` field

        Create a `.env` file with the following environment variables:

        ```ini
        BEFORE_USER_CREATED_HOOK_SECRET="v1,whsec_<base64_secret>"
        ```

        <Admonition type="note">
          You can generate the secret in the [Auth Hooks](/dashboard/project/_/auth/hooks) section of the Supabase dashboard.
        </Admonition>

        Set the secrets in your Supabase project:

        ```bash
        supabase secrets set --env-file .env
        ```

        Create a new edge function:

        ```bash
        supabase functions new before-user-created-hook
        ```

        Add the following code to your edge function:

        ```ts
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'

        const allowedDomains = ['supabase.com', 'example.test']

        Deno.serve(async (req) => {
          const payload = await req.text()
          const secret = Deno.env.get('BEFORE_USER_CREATED_HOOK_SECRET')?.replace('v1,whsec_', '')
          const headers = Object.fromEntries(req.headers)
          const wh = new Webhook(secret)

          try {
            const { user } = wh.verify(payload, headers)
            const email = user.email || ''
            const domain = email.split('@')[1] || ''

            if (!allowedDomains.includes(domain)) {
              return new Response(
                JSON.stringify({
                  error: {
                    message: 'Please sign up with a company email address.',
                    http_code: 400,
                  },
                }),
                { status: 400, headers: { 'Content-Type': 'application/json' } }
              )
            }

            return new Response('{}', { status: 200, headers: { 'Content-Type': 'application/json' } })
          } catch (error) {
            return new Response(JSON.stringify({ error: { message: 'Invalid request format' } }), {
              status: 400,
              headers: { 'Content-Type': 'application/json' },
            })
          }
        })
        ```
      </TabPanel>

      <TabPanel id="http-block-by-oauth-provider" label="Block by OAuth Provider">
        Some applications want to **allow sign-ins with a provider like Discord only for users who already exist**, while blocking new account creation via that provider. This prevents unwanted signups through OAuth flows and enables tighter control over who can join the app.

        The `before-user-created` hook solves this by:

        *   Allowing you to inspect the `app_metadata.provider`
        *   Detecting that a user is about to be created
        *   Knowing the request came from an OAuth flow

        Create a `.env` file with the following environment variables:

        ```ini
        BEFORE_USER_CREATED_HOOK_SECRET="v1,whsec_<base64_secret>"
        ```

        <Admonition type="note">
          You can generate the secret in the [Auth Hooks](/dashboard/project/_/auth/hooks) section of the Supabase dashboard.
        </Admonition>

        Set the secrets in your Supabase project:

        ```bash
        supabase secrets set --env-file .env
        ```

        Create a new edge function:

        ```bash
        supabase functions new before-user-created-hook
        ```

        Add the following code to your edge function:

        ```ts
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'

        const blockedProviders = ['discord']

        Deno.serve(async (req) => {
          const payload = await req.text()
          const secret = Deno.env.get('BEFORE_USER_CREATED_HOOK_SECRET')?.replace('v1,whsec_', '')
          const headers = Object.fromEntries(req.headers)
          const wh = new Webhook(secret)

          try {
            const { user } = wh.verify(payload, headers)
            const provider = user.app_metadata?.provider

            if (blockedProviders.includes(provider)) {
              return new Response(
                JSON.stringify({
                  error: {
                    message: `Signups with ${provider} are not allowed.`,
                    http_code: 403,
                  },
                }),
                { status: 403, headers: { 'Content-Type': 'application/json' } }
              )
            }

            return new Response('{}', { status: 200, headers: { 'Content-Type': 'application/json' } })
          } catch {
            return new Response('{}', { status: 400 })
          }
        })
        ```
      </TabPanel>

      <TabPanel id="http-allow-deny-by-cidr" label="Allow/Deny by IP or CIDR">
        This example shows how you might restrict sign up from a single IP address or a range of them using [PostgreSQL’s built-in](https://www.postgresql.org/docs/current/datatype-net-types.html) `inet` and `<<` operators for [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) -- a method of representing IP address ranges.
        For instance: `123.123.123.123/32` represents only a single IP address, while `123.123.123.0/24` means all IP addresses starting with `123.123.123.`.

        The `before-user-created` hook solves this by:

        *   Detecting that a user is about to be created
        *   Providing the IP address in the `metadata.ip_address` field

        Before creating the edge function run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `signup_networks` table with some sample data and a `hook_restrict_signup_by_network` function to be called by the `before-user-created` auth hook.

        ```sql SQL_EDITOR
        -- Create ENUM type for network rule classification
        create type signup_network_type as enum ('allow', 'deny');

        -- Create the signup_networks table for controlling sign-up access by CIDR
        create table if not exists public.signup_networks (
          id serial primary key,
          cidr cidr not null,
          type public.signup_network_type not null,
          reason text default null,
          note text default null,
          created_at timestamp with time zone not null default now(),
          constraint signup_networks_cidr_key unique (cidr)
        );

        -- Assign appropriate permissions
        grant all
          on table public.signup_networks
          to supabase_auth_admin;

        revoke all
          on table public.signup_networks
          from authenticated, anon, public;

        -- Insert some sample data into the table
        insert into public.signup_networks (cidr, type, reason, note)
        values
          ('192.0.2.0/24', 'allow', '', 'Corporate VPN'),
          ('198.51.100.158/32', 'deny',
            'Your IP Address has been blocked for abuse.',
            'blocked by abuse: (Ticket: ABUSE-185)'),
          ('203.0.113.0/24', 'deny',
            'Your network has been blocked for abuse.',
            'blocked by abuse: (Ticket: ABUSE-212)');

        -- Create the hook function to be called by the auth server
        create or replace function public.hook_restrict_signup_by_network(event jsonb)
        returns jsonb
        language plpgsql
        as $$
        declare
          ip inet;
          allow_count int;
          deny_count int;
        begin
          ip := event->'metadata'->>'ip_address';

          -- Step 1: Check for explicit allow
          select count(*) into allow_count
          from public.signup_networks
          where type = 'allow' and ip::inet << cidr;

          if allow_count > 0 then
            -- If explicitly allowed, allow signup
            return '{}'::jsonb;
          end if;

          -- Step 2: Check for explicit deny
          select count(*) into deny_count
          from public.signup_networks
          where type = 'deny' and ip::inet << cidr;

          if deny_count > 0 then
            return jsonb_build_object(
              'error', jsonb_build_object(
                'message', 'Signups are not allowed from your network.',
                'http_code', 403
              )
            );
          end if;

          -- Step 3: No match: allow by default
          return '{}'::jsonb;
        end;
        $$;

        -- Assign permissions
        grant execute
          on function public.hook_restrict_signup_by_network
          to supabase_auth_admin;

        revoke execute
          on function public.hook_restrict_signup_by_network
          from authenticated, anon, public;
        ```

        Create a `.env` file with the following environment variables:

        ```ini
        BEFORE_USER_CREATED_HOOK_SECRET="v1,whsec_<base64_secret>"
        ```

        <Admonition type="note">
          You can generate the secret in the [Auth Hooks](/dashboard/project/_/auth/hooks) section of the Supabase dashboard.
        </Admonition>

        Set the secrets in your Supabase project:

        ```bash
        supabase secrets set --env-file .env
        ```

        Create a new edge function:

        ```bash
        supabase functions new before-user-created-hook
        ```

        Add the following code to your edge function:

        ```ts
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'
        import { createClient } from 'https://esm.sh/@supabase/supabase-js'

        const whSecret = Deno.env.get('BEFORE_USER_CREATED_HOOK_SECRET')?.replace('v1,whsec_', '')
        const supabaseUrl = Deno.env.get('SUPABASE_URL')
        const supabaseKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')

        const wh = new Webhook(whSecret)
        const supabase = createClient(supabaseUrl, supabaseKey)

        Deno.serve(async (req) => {
          const payload = await req.text()
          const headers = Object.fromEntries(req.headers)
          try {
            const event = wh.verify(payload, headers)

            // Call the same Postgres function as in the SQL example.
            const { data, error } = await supabase.rpc('hook_restrict_signup_by_network', {
              event: JSON.parse(payload),
            })
            if (error) {
              console.error('RPC call failed:', error)
              return new Response(
                JSON.stringify({
                  error: {
                    message: 'Internal error processing signup restriction',
                    http_code: 500,
                  },
                }),
                {
                  status: 500,
                  headers: {
                    'Content-Type': 'application/json',
                  },
                }
              )
            }
            return new Response(JSON.stringify(data ?? {}), {
              status: 200,
              headers: {
                'Content-Type': 'application/json',
              },
            })
          } catch (err) {
            console.error('Webhook verification failed:', err)
            return new Response(
              JSON.stringify({
                error: {
                  message: 'Invalid request format or signature',
                },
              }),
              {
                status: 400,
                headers: {
                  'Content-Type': 'application/json',
                },
              }
            )
          }
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



# Custom Access Token Hook

Customize the access token issued by Supabase Auth

The custom access token hook runs before a token is issued and allows you to add additional claims based on the authentication method used.

Claims returned must conform to our specification. Supabase Auth will check for these claims after the hook is run and return an error if they are not present.

These are the fields currently available on an access token:

Required Claims: `iss`, `aud`, `exp`, `iat`, `sub`, `role`, `aal`, `session_id`, `email`, `phone`, `is_anonymous`

Optional Claims: `jti`, `nbf`, `app_metadata`, `user_metadata`, `amr`,

**Inputs**

| Field                   | Type     | Description                                                                                                                                                                                                                           |
| ----------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`               | `string` | Unique identifier for the user attempting to sign in.                                                                                                                                                                                 |
| `claims`                | `object` | Claims which are included in the access token.                                                                                                                                                                                        |
| `authentication_method` | `string` | The authentication method used to request the access token. Possible values include: `oauth`, `password`, `otp`, `totp`, `recovery`, `invite`, `sso/saml`, `magiclink`, `email/signup`, `email_change`, `token_refresh`, `anonymous`. |

<Tabs scrollable size="small" type="underlined">
  <TabPanel id="custom-access-token-json" label="JSON">
    ```json
    {
      "user_id": "8ccaa7af-909f-44e7-84cb-67cdccb56be6",
      "claims": {
        "aud": "authenticated",
        "exp": 1715690221,
        "iat": 1715686621,
        "sub": "8ccaa7af-909f-44e7-84cb-67cdccb56be6",
        "email": "",
        "phone": "",
        "app_metadata": {},
        "user_metadata": {},
        "role": "authenticated",
        "aal": "aal1",
        "amr": [ { "method": "anonymous", "timestamp": 1715686621 } ],
        "session_id": "4b938a09-5372-4177-a314-cfa292099ea2",
        "is_anonymous": true
      },
      "authentication_method": "anonymous"
    }
    ```
  </TabPanel>

  <TabPanel id="custom-access-token-json-schema" label="JSON Schema">
    ```json
    {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "string",
          "x-faker": "random.uuid"
        },
        "claims": {
          "type": "object",
          "properties": {
            "aud": {
              "type": "string",
              "x-faker": "random.word"
            },
            "exp": {
              "type": "integer",
              "x-faker": "date.future"
            },
            "iat": {
              "type": "integer",
              "x-faker": "date.past"
            },
            "sub": {
              "type": "string",
              "x-faker": "random.uuid"
            },
            "email": {
              "type": "string",
              "x-faker": "internet.email"
            },
            "phone": {
              "type": "string",
              "x-faker": {
                "fake": "{{phone.phoneNumber('+1##########')}}"
              }
            },
            "app_metadata": {
              "type": "object",
              "x-faker": "random.objectElement"
            },
            "user_metadata": {
              "type": "object",
              "x-faker": "random.objectElement"
            },
            "role": {
              "type": "string",
              "enum": ["anon", "authenticated"]
            },
            "aal": {
              "type": "string",
              "enum": ["aal1", "aal2", "aal3"]
            },
            "amr": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "method": {
                    "type": "string",
                    "enum": [
                      "oauth",
                      "password",
                      "otp",
                      "totp",
                      "recovery",
                      "invite",
                      "sso/saml",
                      "magiclink",
                      "email/signup",
                      "email_change",
                      "token_refresh",
                      "anonymous"
                    ]
                  },
                  "timestamp": {
                    "type": "integer",
                    "x-faker": "date.past"
                  }
                },
                "required": ["method", "timestamp"]
              }
            },
            "session_id": {
              "type": "string",
              "x-faker": "random.uuid"
            },
            "is_anonymous": {
              "type": "boolean",
              "x-faker": "random.boolean"
            }
          },
          "required": [
            "aud",
            "exp",
            "iat",
            "sub",
            "email",
            "phone",
            "app_metadata",
            "user_metadata",
            "role",
            "aal",
            "amr",
            "session_id",
            "is_anonymous"
          ]
        },
        "authentication_method": {
          "type": "string",
          "enum": [
            "oauth",
            "password",
            "otp",
            "totp",
            "recovery",
            "invite",
            "sso/saml",
            "magiclink",
            "email/signup",
            "email_change",
            "token_refresh",
            "anonymous"
          ]
        }
      },
      "required": ["user_id", "claims", "authentication_method"]
    }
    ```
  </TabPanel>
</Tabs>

**Outputs**

Return these only if your hook processed the input without errors.

| Field    | Type     | Description                                     |
| -------- | -------- | ----------------------------------------------- |
| `claims` | `object` | The updated claims after the hook has been run. |

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="minimal-jwt">
      <TabPanel id="minimal-jwt" label="Minimal JWT">
        Sometimes the size of the JWT can be a problem especially if you're using a [Server-Side Rendering framework](/docs/guides/auth/server-side). Common situations where the JWT can get too large include:

        *   The user has a particularly large name, email address or phone number
        *   The default JWT has too many claims coming from OAuth providers
        *   A large avatar URL is included

        To lower the size of the JWT you can define a Custom Access Token hook like the one below which will instruct the Auth server to issue a JWT with only the listed claims. Check the documentation above on what JWT claims must be present and cannot be removed.

        Refer to the [Postgres JSON functions](https://www.postgresql.org/docs/current/functions-json.html) on how to manipulate `jsonb` objects.

        ```sql
        create or replace function public.custom_access_token_hook(event jsonb)
        returns jsonb
        language plpgsql
        as $$
          declare
            original_claims jsonb;
            new_claims jsonb;
            claim text;
          begin
            original_claims = event->'claims';
            new_claims = '{}'::jsonb;

            foreach claim in array array[
              -- add claims you want to keep here
              'iss',
              'aud',
              'exp',
              'iat',
              'sub',
              'role',
              'aal',
              'session_id',
              'email',
              'phone',
              'is_anonymous'
           ] loop
              if original_claims ? claim then
                -- original_claims contains one of the listed claims, set it on new_claims
                new_claims = jsonb_set(new_claims, array[claim], original_claims->claim);
              end if;
            end loop;

            return jsonb_build_object('claims', new_claims);
          end
        $$;
        ```
      </TabPanel>

      <TabPanel id="add-admin-role" label="Add admin role">
        You can allow registered admin users to perform restricted actions by granting an `admin` claim to their token.

        Create a profiles table with an `is_admin` flag:

        ```sql
        create table profiles (
          user_id uuid not null primary key references auth.users (id),
          is_admin boolean not null default false
        );
        ```

        Create a hook:

        ```sql
        create or replace function public.custom_access_token_hook(event jsonb)
        returns jsonb
        language plpgsql
        as $$
          declare
            claims jsonb;
            is_admin boolean;
          begin
            -- Check if the user is marked as admin in the profiles table
            select is_admin into is_admin from profiles where user_id = (event->>'user_id')::uuid;

            -- Proceed only if the user is an admin
            if is_admin then
              claims := event->'claims';

              -- Check if 'app_metadata' exists in claims
              if jsonb_typeof(claims->'app_metadata') is null then
                -- If 'app_metadata' does not exist, create an empty object
                claims := jsonb_set(claims, '{app_metadata}', '{}');
              end if;

              -- Set a claim of 'admin'
              claims := jsonb_set(claims, '{app_metadata, admin}', 'true');

              -- Update the 'claims' object in the original event
              event := jsonb_set(event, '{claims}', claims);
            end if;

            -- Return the modified or original event
            return event;
          end;
        $$;

        grant all
          on table public.profiles
          to supabase_auth_admin;

        revoke all
          on table public.profiles
          from authenticated, anon, public;
        ```
      </TabPanel>

      <TabPanel id="restrict-access-to-sso-users" label="Restrict access to SSO users">
        You can restrict access to internal applications with a hook. For example, you can require that employees log in via [SAML Single Sign On (SSO)](/docs/guides/auth/sso/auth-sso-saml). You can exempt select employees from the policy via an allowlist.

        ```sql
        create or replace function public.restrict_application_access(event jsonb)
         returns jsonb
         language plpgsql
        as $function$
        declare
            authentication_method text;
            email_claim text;
            allowed_emails text[] := array['myemail@company.com', 'example@company.com'];
        begin
            -- Extract email claim and authentication method
            email_claim = event->'claims'->>'email';
            authentication_method = event->'authentication_method';
            -- Authentication methods come double quoted (e.g. "otp")
            authentication_method = replace(authentication_method, '"', '');

            if email_claim ilike '%@supabase.io' or authentication_method = 'sso/saml' or email_claim = any(allowed_emails) then
                return event;
            end if;

            -- If none of the conditions are met, return an error
            return jsonb_build_object(
                'error', jsonb_build_object(
                    'http_code', 403,
                    'message', 'Staging access is only allowed to team members. Please use your @company.com account instead'
                )
            );
        end;
        $function$
        ;
        -- manually added
        grant execute
          on function public.restrict_application_access
          to supabase_auth_admin;

        revoke execute
          on function public.restrict_application_access
          from authenticated, anon, public;
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="http-add-metadata-claim">
      <TabPanel id="http-add-metadata-claim" label="Add claim">
        Your company wishes to add assign permissions via the role claim on the `app_metadata` field. Add the role claim to the token via a Hook.

        ```javascript
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'
        import { readAll } from 'https://deno.land/std/io/read_all.ts'
        import * as base64 from 'https://denopkg.com/chiefbiiko/base64/mod.ts'

        Deno.serve(async (req) => {
          const payload = await req.text()
          const base64_secret = Deno.env.get('CUSTOM_ACCESS_TOKEN_SECRET').replace('v1,whsec_', '')
          const headers = Object.fromEntries(req.headers)
          const wh = new Webhook(base64_secret)
          try {
            const { user_id, claims, authentication_method } = wh.verify(payload, headers)
            if (claims.app_metadata && claims.app_metadata.role) {
              claims['role'] = claims.app_metadata.role
            }
            return new Response(
              JSON.stringify({
                claims,
              }),
              {
                status: 200,
                headers: {
                  'Content-Type': 'application/json',
                },
              }
            )
          } catch (error) {
            return new Response(
              JSON.stringify({
                error: `Failed to process the request: ${error}`,
              }),
              {
                status: 500,
                headers: {
                  'Content-Type': 'application/json',
                },
              }
            )
          }
        })
        ```
      </TabPanel>

      <TabPanel id="http-restrict-access-to-sso-users" label="Restrict access to SSO users">
        You can restrict access to internal applications with a hook. For example, you can require that employees log in via [SAML Single Sign On (SSO)](/docs/guides/auth/sso/auth-sso-saml). You can exempt select employees from the policy via an allowlist.

        ```javascript
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'
        import { readAll } from 'https://deno.land/std/io/read_all.ts'
        import * as base64 from 'https://denopkg.com/chiefbiiko/base64/mod.ts'

        Deno.serve(async (req) => {
          const payload = await req.text()
          const base64_secret = Deno.env.get('CUSTOM_ACCESS_TOKEN_SECRET').replace('v1,whsec_', '')
          const headers = Object.fromEntries(req.headers)
          const wh = new Webhook(base64_secret)
          try {
            const { user_id, claims, authentication_method } = wh.verify(payload, headers)

            // Check the condition
            const allowedEmails = ['myemail@company.com', 'example@company.com']
            if (authentication_method === 'sso/saml' || allowedEmails.includes(claims.email)) {
              return new Response(
                JSON.stringify({
                  claims,
                }),
                {
                  status: 200,
                  headers: {
                    'Content-Type': 'application/json',
                  },
                }
              )
            } else {
              return new Response(
                JSON.stringify({
                  error: 'Unauthorized',
                }),
                {
                  status: 500,
                  headers: {
                    'Content-Type': 'application/json',
                  },
                }
              )
            }
          } catch (error) {
            return new Response(
              JSON.stringify({
                error: `Failed to process the request: ${error}`,
              }),
              {
                status: 500,
                headers: {
                  'Content-Type': 'application/json',
                },
              }
            )
          }
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



# MFA Verification Hook



You can add additional checks to the [Supabase MFA implementation](/docs/guides/auth/auth-mfa) with hooks. For example, you can:

*   Limit the number of verification attempts performed over a period of time.
*   Sign out users who have too many invalid verification attempts.
*   Count, rate limit, or ban sign-ins.

**Inputs**

Supabase Auth will send a payload containing these fields to your hook:

| Field         | Type      | Description                                                                                                                       |
| ------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `factor_id`   | `string`  | Unique identifier for the MFA factor being verified                                                                               |
| `factor_type` | `string`  | `totp` or `phone`                                                                                                                 |
| `user_id`     | `string`  | Unique identifier for the user                                                                                                    |
| `valid`       | `boolean` | Whether the verification attempt was valid. For TOTP, this means that the six digit code was correct (true) or incorrect (false). |

<Tabs scrollable size="small" type="underlined" defaultActiveId="mfa-verification-attempt-json">
  <TabPanel id="mfa-verification-attempt-json" label="JSON">
    ```json
    {
      "factor_id": "6eab6a69-7766-48bf-95d8-bd8f606894db",
      "user_id": "3919cb6e-4215-4478-a960-6d3454326cec",
      "valid": true
    }
    ```
  </TabPanel>

  <TabPanel id="mfa-verification-attempt-json-schema" label="JSON Schema">
    ```json
    {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "string",
          "x-faker": "random.uuid"
        },
        "valid": {
          "type": "boolean",
          "x-faker": "random.boolean"
        }
      },
      "required": ["user_id", "valid"]
    }
    ```
  </TabPanel>
</Tabs>

**Outputs**

Return this if your hook processed the input without errors.

| Field      | Type     | Description                                                                                                                                                                                                           |
| ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `decision` | `string` | The decision on whether to allow authentication to move forward. Use `reject` to deny the verification attempt and log the user out of all active sessions. Use `continue` to use the default Supabase Auth behavior. |
| `message`  | `string` | The message to show the user if the decision was `reject`.                                                                                                                                                            |

```json
{
  "decision": "reject",
  "message": "You have exceeded maximum number of MFA attempts."
}
```

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="sql-limit-failed-mfa-verification-attempts">
      <TabPanel id="sql-limit-failed-mfa-verification-attempts" label="Limit failed MFA verification attempts">
        Your company requires that a user can input an incorrect MFA Verification code no more than once every 2 seconds.

        Create a table to record the last time a user had an incorrect MFA verification attempt for a factor.

        ```sql
        create table public.mfa_failed_verification_attempts (
          user_id uuid not null,
          factor_id uuid not null,
          last_failed_at timestamp not null default now(),
          primary key (user_id, factor_id)
        );
        ```

        Create a hook to read and write information to this table. For example:

        ```sql
        create function public.hook_mfa_verification_attempt(event jsonb)
          returns jsonb
          language plpgsql
        as $$
          declare
            last_failed_at timestamp;
          begin
            if event->'valid' is true then
              -- code is valid, accept it
              return jsonb_build_object('decision', 'continue');
            end if;

            select last_failed_at into last_failed_at
              from public.mfa_failed_verification_attempts
              where
                user_id = event->'user_id'
                  and
                factor_id = event->'factor_id';

            if last_failed_at is not null and now() - last_failed_at < interval '2 seconds' then
              -- last attempt was done too quickly
              return jsonb_build_object(
                'error', jsonb_build_object(
                  'http_code', 429,
                  'message',   'Please wait a moment before trying again.'
                )
              );
            end if;

            -- record this failed attempt
            insert into public.mfa_failed_verification_attempts
              (
                user_id,
                factor_id,
                last_refreshed_at
              )
              values
              (
                event->'user_id',
                event->'factor_id',
                now()
              )
              on conflict do update
                set last_refreshed_at = now();

            -- finally let Supabase Auth do the default behavior for a failed attempt
            return jsonb_build_object('decision', 'continue');
          end;
        $$;

        -- Assign appropriate permissions and revoke access
        grant all
          on table public.mfa_failed_verification_attempts
          to supabase_auth_admin;

        revoke all
          on table public.mfa_failed_verification_attempts
          from authenticated, anon, public;
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



# Password Verification Hook



Your company wishes to increase security beyond the requirements of the default password implementation in order to fulfill security or compliance requirements. You plan to track the status of a password sign-in attempt and take action via an email or a restriction on logins where necessary.

As this hook runs on unauthenticated requests, malicious users can abuse the hook by calling it multiple times. Pay extra care when using the hook as you can unintentionally block legitimate users from accessing your application.

Check if a password is valid prior to taking any additional action to ensure the user is legitimate. Where possible, send an email or notification instead of blocking the user.

**Inputs**

| Field     | Type      | Description                                                                                     |
| --------- | --------- | ----------------------------------------------------------------------------------------------- |
| `user_id` | `string`  | Unique identifier for the user attempting to sign in. Correlate this to the `auth.users` table. |
| `valid`   | `boolean` | Whether the password verification attempt was valid.                                            |

<Tabs scrollable size="small" type="underlined">
  <TabPanel id="password-verification-attempt-json" label="JSON">
    ```json
    {
      "user_id": "3919cb6e-4215-4478-a960-6d3454326cec",
      "valid": true
    }
    ```
  </TabPanel>

  <TabPanel id="password-verification-attempt-json-schema" label="JSON Schema">
    ```json
    {
      "type": "object",
      "properties": {
        "user_id": {
          "type": "string",
          "x-faker": "random.uuid"
        },
        "valid": {
          "type": "boolean",
          "x-faker": "random.boolean"
        }
      },
      "required": ["user_id", "valid"]
    }
    ```
  </TabPanel>
</Tabs>

**Outputs**

Return these only if your hook processed the input without errors.

| Field                | Type      | Description                                                                                                                                                                                                           |
| -------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `decision`           | `string`  | The decision on whether to allow authentication to move forward. Use `reject` to deny the verification attempt and log the user out of all active sessions. Use `continue` to use the default Supabase Auth behavior. |
| `message`            | `string`  | The message to show the user if the decision was `reject`.                                                                                                                                                            |
| `should_logout_user` | `boolean` | Whether to log out the user if a `reject` decision is issued. Has no effect when a `continue` decision is issued.                                                                                                     |

```json
{
  "decision": "reject",
  "message": "You have exceeded maximum number of password sign-in attempts.",
  "should_logout_user": "false"
}
```

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="sql-limit-failed-password-verification-attempts">
      <TabPanel id="sql-limit-failed-password-verification-attempts" label="Limit failed password verification attempts">
        As part of new security measures within the company, users can only input an incorrect password every 10 seconds and not more than that. You want to write a hook to enforce this.

        Create a table to record each user's last incorrect password verification attempt.

        ```sql
        create table public.password_failed_verification_attempts (
          user_id uuid not null,
          last_failed_at timestamp not null default now(),
          primary key (user_id)
        );
        ```

        Create a hook to read and write information to this table. For example:

        ```sql
        create function public.hook_password_verification_attempt(event jsonb)
        returns jsonb
        language plpgsql
        as $$
          declare
            last_failed_at timestamp;
          begin
            if event->'valid' is true then
              -- password is valid, accept it
              return jsonb_build_object('decision', 'continue');
            end if;

            select last_failed_at into last_failed_at
              from public.password_failed_verification_attempts
              where
                user_id = event->'user_id';

            if last_failed_at is not null and now() - last_failed_at < interval '10 seconds' then
              -- last attempt was done too quickly
              return jsonb_build_object(
                'error', jsonb_build_object(
                  'http_code', 429,
                  'message',   'Please wait a moment before trying again.'
                )
              );
            end if;

            -- record this failed attempt
            insert into public.password_failed_verification_attempts
              (
                user_id,
                last_failed_at
              )
              values
              (
                event->'user_id',
                now()
              )
              on conflict do update
                set last_failed_at = now();

            -- finally let Supabase Auth do the default behavior for a failed attempt
            return jsonb_build_object('decision', 'continue');
          end;
        $$;

        -- Assign appropriate permissions
        grant all
          on table public.password_failed_verification_attempts
          to supabase_auth_admin;

        revoke all
          on table public.password_failed_verification_attempts
          from authenticated, anon, public;
        ```
      </TabPanel>

      <TabPanel id="sql-send-email-on-failed-password-attempt" label="Send email notification on failed password attempts">
        You can notify a user via email instead of blocking the user. To do so, make use of [Supabase Vault](/docs/guides/database/vault) to store the API Key of our mail provider and use [`pg_net`](/docs/guides/database/extensions/pg_net) to send a HTTP request to our email provider to send the email. Ensure that you have configured a sender signature for the email account which you are sending emails from.

        First, create a table to track sign in attempts.

        ```sql
        create table public.password_sign_in_attempts (
          user_id uuid not null,
          attempt_id uuid not null,
          last_attempt_at timestamp not null default now(),
          attempt_successful boolean not null,
          primary key (user_id, attempt_id)
        );
        ```

        Next, store the API key of our email API provider:

        ```sql
        select vault.create_secret('my_api_key', 'my_api_key_name', 'description_of_my_api_key');
        ```

        Create the hook:

        ```sql
        create or replace function public.hook_notify_user_on_failed_attempts(event jsonb)
        returns jsonb
        language plpgsql
        as $$
          declare
            user_id uuid;
            server_token text;
            user_email_address text;
            email_body jsonb;
            response_id int; -- Variable to store the response ID
            http_code int;
            error_message jsonb;
            attempt_count int;
            max_attempts int := 5; -- Set the threshold for failed attempts
          begin
            user_id := (event->>'user_id')::uuid;

            -- Record the attempt
            insert into public.password_sign_in_attempts (user_id, attempt_id, last_attempt_at, attempt_successful)
            values (user_id, (event->>'attempt_id')::uuid, now(), (event->>'valid')::boolean)
            on conflict (user_id, attempt_id)
            do update set last_attempt_at = now(), attempt_successful = (event->>'valid')::boolean;

            -- Check failed attempts and fetch user email
            select count(*), u.email into attempt_count, user_email_address
            from public.password_sign_in_attempts a
            join auth.users u on a.user_id = u.id
            where a.user_id = user_id and attempt_successful = false and last_attempt_at > (now() - interval '1 day');

            -- Notify user if the number of failed attempts exceeds the threshold
            if attempt_count >= max_attempts then
              -- Fetch the server token
              select decrypted_secret into server_token from vault.decrypted_secrets where name = 'my_api_key_name';

              -- Prepare the email body
              email_body := format('{
                "from": "yoursenderemail@example.com",
                "to": "%s",
                "subject": "Security Alert: Repeated Login Attempts Detected",
                "textbody": "We have detected repeated login attempts for your account. If this was not you, please secure your account.",
                "htmlbody": "<html><body><strong>Security Alert:</strong> We have detected repeated login attempts for your account. If this was not you, please secure your account.</body></html>",
                "messagestream": "outbound"
              }', user_email_address)::jsonb;

              -- Perform the HTTP POST request using Postmark
              select id into response_id from net.http_post(
                'https://api.youremailprovider.com/email',
                email_body,
                'application/json',
                array['Accept: application/json', 'X-Postmark-Server-Token: ' || server_token]
              );

              -- Fetch the response from net._http_response using the obtained id
              select status_code, content into http_code, error_message from net._http_response where id = response_id;

              -- Handle email sending errors
              if http_code is null or (http_code < 200 or http_code >= 300) then
                return jsonb_build_object(
                  'error', jsonb_build_object(
                    'http_code', coalesce(http_code, 0),
                    'message', coalesce(error_message ->> 'message', 'error sending email')
                  )
                );
              end if;
            end if;

            -- Continue with default behavior
            return jsonb_build_object('decision', 'continue');
          end;
        $$;

        -- Assign appropriate permissions
        grant execute
          on function public.hook_notify_user_on_failed_attempts
          to supabase_auth_admin;

        revoke execute
          on function public.hook_notify_user_on_failed_attempts
          from authenticated, anon, public;

        grant all
          on table public.password_sign_in_attempts
          to supabase_auth_admin;

        revoke all
          on table public.password_sign_in_attempts
          from authenticated, anon, public;
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



---
**Navigation:** [← Previous](./35-use-supabase-auth-with-nextjs.md) | [Index](./index.md) | [Next →](./37-send-email-hook.md)
