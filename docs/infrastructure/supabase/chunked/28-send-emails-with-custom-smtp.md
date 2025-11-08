**Navigation:** [← Previous](./27-install.md) | [Index](./index.md) | [Next →](./29-phone-login.md)

# Send emails with custom SMTP



If you're using Supabase Auth with the following configuration:

*   Email and password accounts
*   Passwordless accounts using one-time passwords or links sent over email (OTP, magic link, invites)
*   Email-based user invitations from the [Users page](/dashboard/project/_/auth/users) or from the Auth admin APIs
*   Social login with email confirmation

You will need to set up a custom SMTP server to handle the delivery of messages to your users.

To get you started and let you explore and set up email message templates for your application, Supabase provides a simple SMTP server for all projects. This server imposes a few important restrictions and is not meant for production use.

**Send messages only to pre-authorized addresses.**

Unless you configure a custom SMTP server for your project, Supabase Auth will refuse to deliver messages to addresses that are not part of the project's team. You can manage this in the [Team tab](/dashboard/org/_/team) of the organization's settings.

For example, if your project's organization has these member accounts `person-a@example.com`, `person-b@example.com` and `person-c@example.com` then Supabase Auth will only send messages to these addresses. All other addresses will fail with the error message *Email address not authorized.*

**Significant rate-limits that can change over time.**

To maintain the health and reputation of the default SMTP sending service, the number of messages your project can send is limited and can change without notice. Currently this value is set to <SharedData data="config">auth.rate\_limits.email.inbuilt\_smtp\_per\_hour</SharedData> messages per hour.

**No SLA guarantee on message delivery or uptime for the default SMTP service.**

The default SMTP service is provided as best-effort only and intended for the following non-production use cases:

*   Exploring and getting started with Supabase Auth
*   Setting up and testing email templates with the members of the project's team
*   Building toy projects, demos or any non-mission-critical application

We urge all customers to set up custom SMTP server for all other use cases.



## How to set up a custom SMTP server?

Supabase Auth works with any email sending service that supports the SMTP protocol. First you will need to choose a service, create an account (if you already do not have one) and obtain the SMTP server settings and credentials for your account. These include: the SMTP server host, port, user and password. You will also need to choose a default From address, usually something like `no-reply@example.com`.

A non-exhaustive list of services that work with Supabase Auth is:

*   [Resend](https://resend.com/docs/send-with-supabase-smtp)
*   [AWS SES](https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html)
*   [Postmark](https://postmarkapp.com/developer/user-guide/send-email-with-smtp)
*   [Twilio SendGrid](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/getting-started-smtp)
*   [ZeptoMail](https://www.zoho.com/zeptomail/help/smtp-home.html)
*   [Brevo](https://help.brevo.com/hc/en-us/articles/7924908994450-Send-transactional-emails-using-Brevo-SMTP)

Once you've set up your account with an email sending service, head to the [Authentication settings page](/dashboard/project/_/auth/smtp) to enable and configure custom SMTP.

You can also configure custom SMTP using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure custom SMTP
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_email_enabled": true,
    "mailer_secure_email_change_enabled": true,
    "mailer_autoconfirm": false,
    "smtp_admin_email": "no-reply@example.com",
    "smtp_host": "smtp.example.com",
    "smtp_port": 587,
    "smtp_user": "your-smtp-user",
    "smtp_pass": "your-smtp-password",
    "smtp_sender_name": "Your App Name"
  }'
```

Once you save these settings, your project's Auth server will send messages to all addresses. To protect the reputation of your newly set up service a low rate-limit of 30 messages per hour is imposed. To adjust this to an acceptable value for your use case head to the [Rate Limits configuration page](/dashboard/project/_/auth/rate-limits).



## Dealing with abuse: How to maintain the sending reputation of your SMTP server?

As you make your application known to the public and it grows in popularity, you can expect to see a few types of abuse that can negatively impact the reputation of your sending domain.

A common source of abuse is bots or attackers signing up users to your application.

They use lists of known email addresses to sign up users to your project with pre-determined passwords. These can vary in scale and intensity: sometimes the bots slowly send sign up requests over many months, or they send a lot of requests at once.

Usually the goal for this behavior is:

*   To negatively affect your email sending reputation, after which they might ask for a ransom promising to stop the behavior.
*   To cause a short-term or even long-term Denial of Service attack on your service, by preventing new account creation, signins with magic links or one-time passwords, or to severely impact important security flows in your application (such as reset password or forgot password).
*   To force you to reduce the security posture of your project, such as by disabling email confirmations. At that point, they may target specific or a broad number of users by creating an account in their name. Then they can use social engineering techniques to trick them to use your application in such a way that both attacker and victim have access to the same account.

Mitigation strategies:

*   [Configure CAPTCHA protection](/docs/guides/auth/auth-captcha) for your project, which is the most effective way to control bots in this scenario. You can use CAPTCHA services which provide invisible challenges where real users won't be asked to solve puzzles most of the time.
*   Prefer social login (OAuth) or SSO with SAML instead of email-based authentication flows in your apps.
*   Prefer passwordless authentication (one-time password) as this limits the attacker's value to gain from this behavior.
*   Do not disable email confirmations under pressure.


### Additional best practices

**Set up and maintain DKIM, DMARC and SPF configurations.**

Work with your email sending service to configure [DKIM, DMARC and SPF](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/) for your sending domain. This will significantly increase the deliverability of your messages.

**Set up a custom domain.**

Authentication messages often contain links to your project's Auth server. [Setting up a custom domain](/docs/guides/platform/custom-domains) will reduce the likelihood of your messages being picked up as spam due to another Supabase project's bad reputation.

**Don't mix Auth emails with marketing emails.**

Use separate services for Auth and marketing messages. If the reputation of one falls, it won't affect your whole application or operation.

This includes:

*   Use a separate sending domain for authentication -- `auth.example.com` and a separate domain for marketing `marketing.example.com`.
*   Use a separate From address -- `no-reply@auth.example.com` vs `no-reply@marketing.example.com`.

**Have another SMTP service set up on stand-by.**

In case the primary SMTP service you're using is experiencing difficulty, or your account is under threat of being blocked due to spam, you have another service to quickly turn to.

**Use consistent branding and focused content.**

Make sure you've separated out authentication messages from marketing messages.

*   Don't include promotional content as part of authentication messages.
*   Avoid talking about what your application is inside authentication messages. This can be picked up by automated spam filters which will classify the message as marketing and increase its chances of being regarded as spam. This problem is especially apparent if your project is related to: Web3, Blockchain, AI, NFTs, Gambling, Pornography.
*   Avoid taglines or other short-form marketing material in authentication messages.
*   Reduce the number of links and call-to-actions in authentication messages.
*   Change the authentication messages templates infrequently. Prefer a single big change over multiple smaller changes.
*   Avoid A/B testing content in authentication messages.
*   Use a separate base template (HTML) from your marketing messages.
*   Avoid the use of email signatures in authentication messages. If you do, make sure the signatures are different in style and content from your marketing messages.
*   Use short and to-the-point subject lines. Avoid or reduce the number of emojis in subjects.
*   Reduce the number of images placed in authentication messages.
*   Avoid including user-provided data such as names, usernames, email addresses or salutations in authentication messages. If you do, make sure they are sanitized.

**Prepare for large surges ahead of time.**

If you are planning on having a large surge of users coming at a specific time, work with your email sending service to adjust the rate limits and their expectations accordingly. Most email sending services dislike spikes in the number of messages being sent, and this may affect your sending reputation.

Consider implementing additional protections for such events:

*   Build a queuing or waitlist system instead of allowing direct sign-up, which will help you control the number of messages being sent from the email sending service.
*   Disable email-based sign ups for the event and use social login only. Alternatively you can deprioritize the email-based sign-up flows for the event by hiding them in the UI or making them harder to reach.

**Use the Send Email Auth Hook for more control.**

If you need more control over the sending process, instead of using a SMTP server you can use the [Send Email Auth Hook](/docs/guides/auth/auth-hooks/send-email-hook). This can be useful in advanced scenarios such as:

*   You want to use React or a different email templating engine.
*   You want to use an email sending service that does not provide an SMTP service, or the non-SMTP API is more powerful.
*   You want to queue up messages instead of sending them immediately, in an effort to smooth out spikes in email sending or do additional filtering (avoid repetitive messages).
*   You want to use multiple email sending services to increase reliability (if primary service is unavailable, use backup service automatically).
*   You want to use different email sending services based on the email address or user data (e.g. service A for users in the USA, service B for users in the EU, service C for users in China).
*   You want to add or include additional email headers in messages, for tracking or other reasons.
*   You want to add attachments to the messages (generally not recommended).
*   You want to add [S/MIME signatures](https://en.wikipedia.org/wiki/S/MIME) to messages.
*   You want to use an email server not open to the Internet, such as some corporate or government mail servers.

**Increase the duration of user sessions.**

Having short lived [user sessions](/docs/guides/auth/sessions) can be problematic for email sending, as it forces active users to sign-in frequently, increasing the number of messages needed to be sent. Consider increasing the maximum duration of user sessions. If you do see an unnecessary increase in logins without a clear cause, check your frontend application for bugs.

If you are using a [SSR](/docs/guides/auth/server-side) framework on the frontend and are seeing an increased number of user logins without a clear cause, check your set up. Make sure to keep the `@supabase/ssr` package up to date and closely follow the guides we publish. Make sure that the middleware components of your SSR frontend works as intended and matches the guides we've published. Sometimes a misplaced `return` or conditional can cause early session termination.



# Sign in with Web3

Use your Web3 wallet to authenticate users with Supabase

[Enable Sign In with Web3](/dashboard/project/_/auth/providers) to allow users to sign in to your application using only their Web3 wallet.

Supported Web3 wallets:

*   All Solana wallets
*   All Ethereum wallets



## How does it work?

Sign in with Web3 utilizes the [EIP 4361](https://eips.ethereum.org/EIPS/eip-4361) standard to authenticate wallet addresses off-chain. This standard is widely supported by the Ethereum and Solana ecosystems, making it the best choice for verifying wallet ownership.

Authentication works by asking the Web3 wallet application to sign a predefined message with the user's wallet. This message is parsed both by the Web3 wallet application and Supabase Auth to verify its validity and purpose, before creating a user account or session.

An example of such a message is:

```
example.com wants you to sign in with your Ethereum account:
0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2

I accept the ExampleOrg Terms of Service: https://example.com/tos

URI: https://example.com/login
Version: 1
Chain ID: 1
Nonce: 32891756
Issued At: 2021-09-30T16:25:24Z
Resources:
- https://example.com/my-web2-claim.json
```

It defines the wallet address, timestamp, browser location where the sign-in occurred and includes a customizable statement (`I accept...`) which you can use to ask consent from the user.

Most Web3 wallets are able to recognize these messages and show a dedicated "Confirm Sign In" dialog validating and presenting the information in the message in a secure and responsible way to the user. Even if the wallet does not directly support these messages, it will use the message signature dialog instead.

Finally the Supabase Auth server validates both the message's contents and signature before issuing a valid [User session](/docs/guides/auth/sessions) to your application. Validation rules include:

*   Message structure validation
*   Cryptographic signature verification
*   Timestamp validation, ensuring the signature was created within 10 minutes of the sign-in call
*   URI and Domain validation, ensuring these match your server's defined [Redirect URLs](/docs/guides/auth/redirect-urls)

The wallet address is used as the identity identifier, and in the identity data you can also find the statement and additional metadata.



## Enable the Web3 provider

In the dashboard navigate to your project's [Authentication Providers](/dashboard/project/_/auth/providers) section and enable the Web3 Wallet provider.

In the CLI add the following config to your `supabase/config.toml` file:

```toml
[auth.web3.solana]
enabled = true

[auth.web3.ethereum]
enabled = true
```


### Potential for abuse

User accounts that sign in with their Web3 wallet will not have an email address or phone number associated with them. This can open your project to abuse as creating a Web3 wallet account is free and easy to automate and difficult to correlate with a real person's identity.

Control your project's exposure by configuring in the dashboard:

*   [Rate Limits for Web3](/dashboard/project/_/auth/rate-limits)
*   [Enable CAPTCHA protection](/docs/guides/auth/auth-captcha)

Or in the CLI:

```toml
[auth.rate_limit]

# Number of Web3 logins that can be made in a 5 minute interval per IP address.
web3 = 30

[auth.captcha]
enabled = true
provider = "hcaptcha" # or other supported providers
secret = "0x0000000000000000000000000000000000000000"
```

Many wallet applications will warn the user if the message sent for signing is not coming from the page they are currently visiting. To further prevent your Supabase project from receiving signed messages destined for other applications, you must register your application's URL using the [Redirect URL settings](/docs/guides/auth/redirect-urls).

For example if the user is signing in to the page `https://example.com/sign-in` you should add the following configurations in the Redirect URL settings:

*   `https://example.com/sign-in/` (last slash is important)
*   Alternatively set up a glob pattern such as `https://example.com/**`



## Sign in with Ethereum

Ethereum defines the [`window.ethereum` global scope object](https://eips.ethereum.org/EIPS/eip-1193) that your app uses to interact with Ethereum Wallets. Additionally there is a [wallet discovery mechanism (EIP-6963)](https://eips.ethereum.org/EIPS/eip-6963) that your app can use to discover all of the available wallets on the user's browser.

To sign in a user with their Ethereum wallet make sure that the user has installed a wallet application. There are two ways to do this:

1.  Detect the `window.ethereum` global scope object and ensure it's defined. This only works if your user has only one wallet installed on their browser.
2.  Use the wallet discovery mechanism (EIP-6963) to ask the user to choose a wallet before they continue to sign in. Read [the MetaMask guide on the best way to support this](https://docs.metamask.io/wallet/tutorials/react-dapp-local-state).

<Tabs scrollable size="small" type="underlined" defaultActiveId="window" queryGroup="ethWallet">
  <TabPanel id="window" label="Ethereum Window API (EIP-1193)">
    Use the following code to sign in a user, implicitly relying on the `window.ethereum` global scope wallet API:

    ```typescript
    const { data, error } = await supabase.auth.signInWithWeb3({
      chain: 'ethereum',
      statement: 'I accept the Terms of Service at https://example.com/tos',
    })
    ```
  </TabPanel>

  <TabPanel id="wallet" label="Ethereum Wallet API (EIP-6963)">
    Once you've obtained a wallet using the wallet detection (EIP-6963) mechanism, you can pass the selected wallet to the Supabase JavaScript SDK to continue the sign-in process.

    ```typescript
    const { data, error } = await supabase.auth.signInWithWeb3({
      chain: 'ethereum',
      statement: 'I accept the Terms of Service at https://example.com/tos',
      wallet: selectedWallet, // obtain this using the EIP-6963 mechanism
    })
    ```

    An excellent guide on using the [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) mechanism is available by [MetaMask](https://docs.metamask.io/wallet/tutorials/react-dapp-local-state).
  </TabPanel>

  <TabPanel id="custom" label="Ethereum Message and Signature">
    If your application relies on a custom Ethereum wallet API, you can pass a [Sign in with Ethereum (EIP-4361)](https://eips.ethereum.org/EIPS/eip-4361) message and signature to complete the sign in process.

    ```typescript
    const { data, error } = await supabase.auth.signInWithWeb3({
      chain: 'ethereum',
      message: '<sign in with ethereum message>',
      signature: '<hex of the ethereum signature over the message>',
    })
    ```
  </TabPanel>
</Tabs>



## Sign in with Solana

<Tabs scrollable size="small" type="underlined" defaultActiveId="window" queryGroup="solanaWallet">
  <TabPanel id="window" label="Solana Window API">
    Most Solana wallet applications expose their API via the `window.solana` global scope object in your web application.

    Supabase's JavaScript Client Library provides built-in support for this API.

    To sign in a user make sure that:

    1.  The user has installed a wallet application (by checking that the `window.solana` object is defined)
    2.  The wallet application is connected to your application by using the [`window.solana.connect()` API](https://docs.phantom.com/solana/establishing-a-connection)

    Use the following code to authenticate a user:

    ```typescript
    const { data, error } = await supabase.auth.signInWithWeb3({
      chain: 'solana',
      statement: 'I accept the Terms of Service at https://example.com/tos',
    })
    ```

    Providing a `statement` is required for most Solana wallets and this message will be shown to the user on the consent dialog. It will also be added to the identity data for your users.

    If you are using a non-standard Solana wallet that does not register the `window.solana` object, or your user has multiple Solana wallets attached to the page you can disambiguate by providing the wallet object like so:

    *   To use [Brave Wallet with Solana](https://wallet-docs.brave.com/solana):
        ```typescript
        const { data, error } = await supabase.auth.signInWithWeb3({
          chain: 'solana',
          statement: 'I accept the Terms of Service at https://example.com/tos',
          wallet: window.braveSolana,
        })
        ```
    *   To use [Phantom with Solana](https://docs.phantom.com/solana/detecting-the-provider):
        ```typescript
        const { data, error } = await supabase.auth.signInWithWeb3({
          chain: 'solana',
          statement: 'I accept the Terms of Service at https://example.com/tos',
          wallet: window.phantom,
        })
        ```
  </TabPanel>

  <TabPanel id="adapter" label="Solana Wallet Adapter">
    Although the `window.solana` global scope JavaScript API is an unofficial standard, there still are subtle differences between wallet applications. The Solana ecosystem has provided the [Solana Wallet Adapter](https://solana.com/developers/courses/intro-to-solana/interact-with-wallets#solanas-wallet-adapter) system based on the [Wallet Standard](https://github.com/wallet-standard/wallet-standard) to simplify ease of development.

    The Supabase JavaScript Client Library supports signing in with this approach too. Follow the [Solana Interact with Wallets](https://solana.com/developers/courses/intro-to-solana/interact-with-wallets) guide on how to install and configure your application.

    Below is a short example on using a `<SignInButton />` component that uses the `useWallet()` React hook to obtain the connected wallet and sign the user in with it:

    ```tsx
    function SignInButton() {
      const wallet = useWallet()

      return (
        <>
          {wallet.connected ? (
            <button
              onClick={() => {
                supabase.auth.signInWithWeb3({
                  chain: 'solana',
                  statement: 'I accept the Terms of Service at https://example.com/tos',
                  wallet,
                })
              }}
            >
              Sign in with Solana
            </button>
          ) : (
            <WalletMultiButton />
          )}
        </>
      )
    }

    function App() {
      const endpoint = clusterApiUrl('devnet')
      const wallets = useMemo(() => [], [])

      return (
        <ConnectionProvider endpoint={endpoint}>
          <WalletProvider wallets={wallets}>
            <WalletModalProvider>
              <SignInButton />
            </WalletModalProvider>
          </WalletProvider>
        </ConnectionProvider>
      )
    }
    ```
  </TabPanel>
</Tabs>



## Frequently asked questions


### How to associate an email address, phone number or social login to a user signing in with Web3?

Web3 wallets don't expose any identifying information about the user other than their wallet address (public key). This is why accounts that were created using Sign in with Web3 don't have any email address or phone number associated.

To associate an email address, phone number or other social login with their account you can use the `supabase.auth.updateUser()` or `supabase.auth.linkIdentity()` APIs.



# Enterprise Single Sign-On



Supabase Auth supports building enterprise applications that require Single Sign-On (SSO) authentication [with SAML 2.0](/docs/guides/auth/sso/auth-sso-saml).



# General configuration

General configuration options for Supabase Auth

This section covers the [general configuration options](/dashboard/project/_/auth) for Supabase Auth. If you are looking for another type of configuration, you may be interested in one of the following sections:

*   [Policies](/dashboard/project/_/auth/policies) to manage Row Level Security policies for your tables.
*   [Sign In / Providers](/dashboard/project/_/auth/providers) to configure authentication providers and login methods for your users.
*   [Third Party Auth](/dashboard/project/_/auth/third-party) to use third-party authentication (TPA) systems based on JWTs to access your project.
*   [Sessions](/dashboard/project/_/auth/sessions) to configure settings for user sessions and refresh tokens.
*   [Rate limits](/dashboard/project/_/auth/rate-limits) to safeguard against bursts of incoming traffic to prevent abuse and maximize stability.
*   [Email Templates](/dashboard/project/_/auth/templates) to configure what emails your users receive.
*   [Custom SMTP](/dashboard/project/_/auth/smtp) to configure how emails are sent.
*   [Multi-Factor](/dashboard/project/_/auth/mfa) to require users to provide additional verification factors to authenticate.
*   [URL Configuration](/dashboard/project/_/auth/url-configuration) to configure site URL and redirect URLs for authentication. Read more [in the redirect URLs documentation](/docs/guides/auth/redirect-urls).
*   [Attack Protection](/dashboard/project/_/auth/protection) to configure security settings to protect your project from attacks.
*   [Auth Hooks (BETA)](/dashboard/project/_/auth/auth-hooks) to use Postgres functions or HTTP endpoints to customize the behavior of Supabase Auth to meet your needs.
*   [Audit Logs (BETA)](/dashboard/project/_/auth/audit-logs) to track and monitor auth events in your project.
*   [Advanced](/dashboard/project/_/auth/advanced) to configure advanced authentication server settings.

Supabase Auth provides these [general configuration options](/dashboard/project/_/settings/auth) to control user access to your application:

*   **Allow new users to sign up**: Users will be able to sign up. If this config is disabled, only existing users can sign in.

*   **Confirm Email**: Users will need to confirm their email address before signing in for the first time.

    *   Having **Confirm Email** disabled assumes that the user's email does not need to be verified in order to login and implicitly confirms the user's email in the database.
    *   This option can be found in the email provider under the provider-specific configuration.
        {/* - If you previously relied on this config to autoconfirm a user's email address, you can switch to use **Allow unverified email sign in** instead. This new option allows the user to sign in with an unverified email which you can keep track of through the user object. It provides more versatility if you require your users to verify their email address in the future since you can structure your RLS policies to check the user's `email_verified` field. */}

*   **Allow anonymous sign-ins**: Allow anonymous users to be created.

*   **Allow manual linking**: Allow users to link their accounts manually.



# Identities



An identity is an authentication method associated with a user. Supabase Auth supports the following types of identity:

*   Email
*   Phone
*   OAuth
*   SAML

A user can have more than one identity. Anonymous users have no identity until they link an identity to their user.



## The user identity object

The user identity object contains the following attributes:

| Attributes         | Type     | Description                                                                                                                                                                                                                              |
| ------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| provider\_id       | `string` | The provider id returned by the provider. If the provider is an OAuth provider, the id refers to the user's account with the OAuth provider. If the provider is `email` or `phone`, the id is the user's id from the `auth.users` table. |
| user\_id           | `string` | The user's id that the identity is linked to.                                                                                                                                                                                            |
| identity\_data     | `object` | The identity metadata. For OAuth and SAML identities, this contains information about the user from the provider.                                                                                                                        |
| id                 | `string` | The unique id of the identity.                                                                                                                                                                                                           |
| provider           | `string` | The provider name.                                                                                                                                                                                                                       |
| email              | `string` | The email is a generated column that references the optional email property in the identity\_data                                                                                                                                        |
| created\_at        | `string` | The timestamp that the identity was created.                                                                                                                                                                                             |
| last\_sign\_in\_at | `string` | The timestamp that the identity was last used to sign in.                                                                                                                                                                                |
| updated\_at        | `string` | The timestamp that the identity was last updated.                                                                                                                                                                                        |



# JWT Claims Reference

Complete reference for claims appearing in JWTs created by Supabase Auth

This page provides a comprehensive reference for all JWT claims used in Supabase authentication tokens. This information is essential for server-side JWT validation and serialization, especially when implementing authentication in languages like Rust where field names like `ref` are reserved keywords.



## JWT structure overview

Supabase JWTs follow the standard JWT structure with three parts:

*   **Header**: Contains algorithm and key information
*   **Payload**: Contains the claims (user data and metadata)
*   **Signature**: Cryptographic signature for verification

The payload contains various claims that provide user identity, authentication level, and authorization information.



## Required claims

These claims are always present in Supabase JWTs and cannot be removed:

| Field          | Type                 | Description                                                 | Example                                       |
| -------------- | -------------------- | ----------------------------------------------------------- | --------------------------------------------- |
| `iss`          | `string`             | **Issuer** - The entity that issued the JWT                 | `"https://project-ref.supabase.co/auth/v1"`   |
| `aud`          | `string \| string[]` | **Audience** - The intended recipient of the JWT            | `"authenticated"` or `"anon"`                 |
| `exp`          | `number`             | **Expiration Time** - Unix timestamp when the token expires | `1640995200`                                  |
| `iat`          | `number`             | **Issued At** - Unix timestamp when the token was issued    | `1640991600`                                  |
| `sub`          | `string`             | **Subject** - The user ID (UUID)                            | `"123e4567-e89b-12d3-a456-426614174000"`      |
| `role`         | `string`             | **Role** - User's role in the system                        | `"authenticated"`, `"anon"`, `"service_role"` |
| `aal`          | `string`             | **Authenticator Assurance Level** - Authentication strength | `"aal1"`, `"aal2"`                            |
| `session_id`   | `string`             | **Session ID** - Unique session identifier                  | `"session-uuid"`                              |
| `email`        | `string`             | **Email** - User's email address                            | `"user@example.com"`                          |
| `phone`        | `string`             | **Phone** - User's phone number                             | `"+1234567890"`                               |
| `is_anonymous` | `boolean`            | **Anonymous Flag** - Whether the user is anonymous          | `false`                                       |



## Optional claims

These claims may be present depending on the authentication context:

| Field           | Type     | Description                                                                | Example                                             |
| --------------- | -------- | -------------------------------------------------------------------------- | --------------------------------------------------- |
| `jti`           | `string` | **JWT ID** - Unique identifier for the JWT                                 | `"jwt-uuid"`                                        |
| `nbf`           | `number` | **Not Before** - Unix timestamp before which the token is invalid          | `1640991600`                                        |
| `app_metadata`  | `object` | **App Metadata** - Application-specific user data                          | `{"provider": "email"}`                             |
| `user_metadata` | `object` | **User Metadata** - User-specific data                                     | `{"name": "John Doe"}`                              |
| `amr`           | `array`  | **Authentication Methods Reference** - List of authentication methods used | `[{"method": "password", "timestamp": 1640991600}]` |



## Special claims

| Field | Type     | Description                                         | Example                  | Context                       |
| ----- | -------- | --------------------------------------------------- | ------------------------ | ----------------------------- |
| `ref` | `string` | **Project Reference** - Supabase project identifier | `"abcdefghijklmnopqrst"` | Anon/Service role tokens only |



## Field value constraints


### Authenticator assurance level (`aal`)

| Value    | Description                                          |
| -------- | ---------------------------------------------------- |
| `"aal1"` | Single-factor authentication (password, OAuth, etc.) |
| `"aal2"` | Multi-factor authentication (password + TOTP, etc.)  |


### Role values (`role`)

| Value             | Description        | Use Case                            |
| ----------------- | ------------------ | ----------------------------------- |
| `"anon"`          | Anonymous user     | Public access with RLS policies     |
| `"authenticated"` | Authenticated user | Standard user access                |
| `"service_role"`  | Service role       | Admin privileges (server-side only) |


### Audience values (`aud`)

| Value             | Description                   |
| ----------------- | ----------------------------- |
| `"authenticated"` | For authenticated user tokens |
| `"anon"`          | For anonymous user tokens     |


### Authentication methods (`amr.method`)

| Value             | Description                   |
| ----------------- | ----------------------------- |
| `"oauth"`         | OAuth provider authentication |
| `"password"`      | Email/password authentication |
| `"otp"`           | One-time password             |
| `"totp"`          | Time-based one-time password  |
| `"recovery"`      | Account recovery              |
| `"invite"`        | Invitation-based signup       |
| `"sso/saml"`      | SAML single sign-on           |
| `"magiclink"`     | Magic link authentication     |
| `"email/signup"`  | Email signup                  |
| `"email_change"`  | Email change                  |
| `"token_refresh"` | Token refresh                 |
| `"anonymous"`     | Anonymous authentication      |



## JWT examples


### Authenticated user token

```json
{
  "aal": "aal1",
  "amr": [
    {
      "method": "password",
      "timestamp": 1640991600
    }
  ],
  "app_metadata": {
    "provider": "email",
    "providers": ["email"]
  },
  "aud": "authenticated",
  "email": "user@example.com",
  "exp": 1640995200,
  "iat": 1640991600,
  "iss": "https://abcdefghijklmnopqrst.supabase.co/auth/v1",
  "phone": "",
  "role": "authenticated",
  "session_id": "123e4567-e89b-12d3-a456-426614174000",
  "sub": "123e4567-e89b-12d3-a456-426614174000",
  "user_metadata": {
    "name": "John Doe"
  },
  "is_anonymous": false
}
```


### Anonymous user token

```json
{
  "iss": "supabase",
  "ref": "abcdefghijklmnopqrst",
  "role": "anon",
  "iat": 1640991600,
  "exp": 1640995200
}
```


### Service role token

```json
{
  "iss": "supabase",
  "ref": "abcdefghijklmnopqrst",
  "role": "service_role",
  "iat": 1640991600,
  "exp": 1640995200
}
```



## Language-Specific considerations


### Rust

In Rust, the `ref` field is a reserved keyword. When deserializing JWTs, you'll need to handle this:

```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize, Serialize)]
struct JwtClaims {
    iss: String,
    #[serde(rename = "ref")] // Handle reserved keyword
    project_ref: Option<String>,
    role: String,
    iat: i64,
    exp: i64,
    // ... other claims
}
```


### TypeScript/JavaScript

```typescript
interface JwtClaims {
  iss: string
  aud: string | string[]
  exp: number
  iat: number
  sub: string
  role: string
  aal: 'aal1' | 'aal2'
  session_id: string
  email: string
  phone: string
  is_anonymous: boolean
  jti?: string
  nbf?: number
  app_metadata?: Record<string, any>
  user_metadata?: Record<string, any>
  amr?: Array<{
    method: string
    timestamp: number
  }>
  ref?: string // Only in anon/service role tokens
}
```


### Python

```python
from typing import Optional, Union, List, Dict, Any
from dataclasses import dataclass

@dataclass
class AmrEntry:
    method: str
    timestamp: int

@dataclass
class JwtClaims:
    iss: str
    aud: Union[str, List[str]]
    exp: int
    iat: int
    sub: str
    role: str
    aal: str
    session_id: str
    email: str
    phone: str
    is_anonymous: bool
    jti: Optional[str] = None
    nbf: Optional[int] = None
    app_metadata: Optional[Dict[str, Any]] = None
    user_metadata: Optional[Dict[str, Any]] = None
    amr: Optional[List[AmrEntry]] = None
    ref: Optional[str] = None  # Only in anon/service role tokens
```


### Go

```go
type AmrEntry struct {
    Method    string `json:"method"`
    Timestamp int64  `json:"timestamp"`
}

type JwtClaims struct {
    Iss         string                 `json:"iss"`
    Aud         interface{}            `json:"aud"` // string or []string
    Exp         int64                  `json:"exp"`
    Iat         int64                  `json:"iat"`
    Sub         string                 `json:"sub"`
    Role        string                 `json:"role"`
    Aal         string                 `json:"aal"`
    SessionID   string                 `json:"session_id"`
    Email       string                 `json:"email"`
    Phone       string                 `json:"phone"`
    IsAnonymous bool                   `json:"is_anonymous"`
    Jti         *string                `json:"jti,omitempty"`
    Nbf         *int64                 `json:"nbf,omitempty"`
    AppMetadata map[string]interface{} `json:"app_metadata,omitempty"`
    UserMetadata map[string]interface{} `json:"user_metadata,omitempty"`
    Amr         []AmrEntry             `json:"amr,omitempty"`
    Ref         *string                `json:"ref,omitempty"` // Only in anon/service role tokens
}
```



## Validation guidelines

When implementing JWT validation on your server:

1.  **Check Required Fields**: Ensure all required claims are present
2.  **Validate Types**: Verify field types match expected types
3.  **Check Expiration**: Validate `exp` timestamp is in the future
4.  **Verify Issuer**: Ensure `iss` matches your Supabase project
5.  **Check Audience**: Validate `aud` matches expected audience
6.  **Handle Reserved Keywords**: Use field renaming for languages like Rust



## Security considerations

*   **Always validate the JWT signature** before trusting any claims
*   **Never expose service role tokens** to client-side code
*   **Validate all claims** before trusting the JWT
*   **Check token expiration** on every request
*   **Use HTTPS** for all JWT transmission
*   **Rotate JWT secrets** regularly
*   **Implement proper error handling** for invalid tokens



## Related documentation

*   [JWT Overview](/docs/guides/auth/jwts)
*   [Custom Access Token Hooks](/docs/guides/auth/auth-hooks/custom-access-token-hook)
*   [Row Level Security](/docs/guides/database/postgres/row-level-security)
*   [Server-Side Auth](/docs/guides/auth/server-side)



# JSON Web Token (JWT)

Information on how best to use JSON Web Tokens with Supabase

A [JSON Web Token](https://jwt.io/introduction) is a type of data structure, represented as a string, that usually contains identity and authorization information about a user. It encodes information about its lifetime and is signed with a cryptographic key to make it tamper-resistant.

Supabase Auth continuously issues a new JWT for each user session, for as long as the user remains signed in. Check the comprehensive guide on [Sessions](/docs/guides/auth/sessions) to find out how you can tailor this process for your needs.

JWTs provide the foundation for [Row Level Security](/docs/guides/database/row-level-security). Each Supabase product is able to securely decode and verify the validity of a JWT it receives before using Postgres policies and roles to authorize access to the project's data.

Supabase provides a comprehensive system of managing [JWT Signing Keys](/docs/guides/auth/signing-keys) used to create and verify JSON Web Tokens.



## Introduction

JWTs are strings that have the following structure:

```
<header>.<payload>.<signature>
```

Each part is a string of [Base64-URL](https://en.wikipedia.org/wiki/Base64#Variants_summary_table) encoded JSON, or bytes for the signature.

**Header**

```json
{
  "typ": "JWT",
  "alg": "<HS256 | ES256 | RS256>",
  "kid": "<unique key identifier>"
}
```

Gives some basic identifying information about the string, indicating its type `typ`, the cryptographic algorithm `alg` that can be used to verify the data, and optionally the unique key identifier that should be used when verifying it.

**Payload**

```json
{
  "iss": "https://project_id.supabase.co/auth/v1",
  "exp": 12345678,
  "sub": "<user ID>",
  "role": "authenticated",
  "email": "someone@example.com",
  "phone": "+15552368"
  // ...
}
```

Provides identifying information (called "claims") about the user (or other entity) that is represented by the token. Usually a JWT conveys information about what the user can access (then called Access Token) or who the user is (then called ID Token). You can use a [Custom Access Token Hook](/docs/guides/auth/auth-hooks/custom-access-token-hook) to add, remove or change claims present in the token. A few claims are important:

| Claim                                              | Description                                                                                                                                                                |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iss`                                              | Identifies the server which issued the token. If you append `/.well-known/jwks.json` to this URL you'll get access to the public keys with which you can verify the token. |
| `exp`                                              | Sets a time limit after which the token should not be trusted and is considered expired, even if it is properly signed.                                                    |
| `sub`                                              | Means *subject*, is the unique ID of the user represented by the token.                                                                                                    |
| <span className="whitespace-nowrap!">`role`</span> | The Postgres role to use when applying Row Level Security policies.                                                                                                        |
| ...                                                | All other claims are useful for quick access to profile information without having to query the database or send a request to the Auth server.                             |

**Signature**

A [digital signature](https://en.wikipedia.org/wiki/Digital_signature) using a [shared secret](https://en.wikipedia.org/wiki/HMAC) or [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography). The purpose of the signature is to verify the authenticity of the `<header>.<payload>` string without relying on database access, liveness or performance of the Auth server. To verify the signature avoid implementing the algorithms yourself and instead rely on `supabase.auth.getClaims()`, or other high-quality JWT verification libraries for your language.



## Supabase and JWTs

Supabase creates JWTs in these cases for you:

1.  When using Supabase Auth, an access token (JWT) is created for each user while they remain signed in. These are short lived, so they are continuously issued as your user interacts with Supabase APIs.
2.  As the legacy JWT-based [API keys](/docs/guides/api/api-keys) `anon` and `service_role`. These have a 10 year expiry and are signed with a shared secret, making them hard to rotate or expire. These JWTs express public access via the `anon` key, or elevated access via the `service_role` key. We strongly recommend switching to publishable and secret API keys.
3.  On-the-fly when using publishable or secret API keys. Each API key is transformed into a short-lived JWT that is then used to authorize access to your data. Accessing these short-lived tokens is generally not possible.

In addition to creating JWTs, Supabase can also accept JWTs from other Auth servers via the [Third-Party Auth](/docs/guides/auth/third-party/overview) feature or ones you've made yourself using the legacy JWT secret or if you've imported in [JWT Signing Key](/docs/guides/auth/signing-keys).



## Using custom or third-party JWTs

<Admonition type="note">
  The `supabase.auth.getClaims()` method is meant to be used only with JWTs issued by Supabase Auth. If you make your own JWTs using the legacy JWT secret or a key you've imported, the verification may fail. We strongly recommend using a JWT verification library for your language to verify this type of JWT based on the claims you're adding in them.
</Admonition>

Your Supabase project accepts a JWT in the `Authorization: Bearer <jwt>` header. If you're using the Supabase client library, it does this for you.

If you are already using Supabase Auth, when a user is signed in, their access token JWT is automatically managed and sent for you with every API call.

If you wish to send a JWT from a Third-Party Auth provider, or one you made yourself by using the legacy JWT secret or a JWT signing key you imported, you can pass it to the client library using the `accessToken` option.

<Tabs type="underlined" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```typescript
    import { createClient } from '@supabase/supabase-js'

    const supabase = createClient(
      'https://<supabase-project>.supabase.co',
      'SUPABASE_PUBLISHABLE_KEY',
      {
        accessToken: async () => {
          return '<your JWT here>'
        },
      }
    )
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    await Supabase.initialize(
      url: supabaseUrl,
      anonKey: supabaseKey,
      debug: false,
      accessToken: () async {
        return "<your JWT here>";
      },
    );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift (iOS)">
    ```swift
    import Supabase

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "https://<supabase-project>.supabase.co")!,
      supabaseKey: "SUPABASE_PUBLISHABLE_KEY",
      options: SupabaseClientOptions(
        auth: SupabaseClientOptions.AuthOptions(
          accessToken: {
            return "<your JWT here>"
          }
        )
      )
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val supabase = createSupabaseClient(
        "https://<supabase-project>.supabase.co",
        "SUPABASE_PUBLISHABLE_KEY"
    ) {
        accessToken = {
            "<your JWT here>"
        }
    }
    ```
  </TabPanel>

  <TabPanel id="bash" label="cURL">
    ```bash
    curl 'https://<supabase-project>.supabase.co/rest/v1/my_table?select=id' \
      -H "apikey: $SUPABASE_PUBLISHABLE_KEY" \
      -H "Authorization: Bearer <your JWT here>"
    ```
  </TabPanel>
</Tabs>

In the past there was a recommendation to set custom headers on the Supabase client with the `Authorization` header including your custom JWT. This is no longer recommended as it's less flexible and causes confusion when combined with a user session from Supabase Auth.



## Verifying a JWT from Supabase

If you're not able to use the Supabase client libraries, the following can be used to help you securely verify JWTs issued by Supabase.

Supabase Auth exposes a [JSON Web Key](https://datatracker.ietf.org/doc/html/rfc7517) Set URL for each Supabase project:

```http
GET https://project-id.supabase.co/auth/v1/.well-known/jwks.json
```

Which responds with JWKS object containing one or more asymmetric [JWT signing keys](/docs/guides/auth/signing-keys) (only their public keys). Be aware that this endpoint does not return any keys if you are not using asymmetric JWT signing keys.

```json
{
  "keys": [
    {
      "kid": "<match with kid from JWT header>",
      "alg": "<match with alg from JWT header>",
      "kty": "<RSA|EC|OKP>",
      "key_ops": ["verify"]
      // public key fields
    }
  ]
}
```

This endpoint is served directly from the Auth server, but is also additionally cached by the Supabase Edge for 10 minutes, significantly speeding up access to this data regardless of where you're performing the verification. It's important to be aware of the cache expiry time to prevent unintentionally rejecting valid user access tokens. We recommend waiting at least 20 minutes when creating a standby signing key, or revoking a previously used key.

Make sure that you do not cache this data for longer in your application, as it might make revocation difficult. If you do, make sure to provide a way to purge this cache when rotating signing keys to avoid unintentionally rejecting valid user access tokens.

Below is an example of how to use the [jose TypeScript JWT verification library](https://github.com/panva/jose) with Supabase JWTs:

```typescript
import { jwtVerify, createRemoteJWKSet } from 'jose'

const PROJECT_JWKS = createRemoteJWKSet(
  new URL('https://project-id.supabase.co/auth/v1/.well-known/jwks.json')
)

/**
 * Verifies the provided JWT against the project's JSON Web Key Set.
 */
async function verifyProjectJWT(jwt: string) {
  return jwtVerify(jwt, PROJECT_JWKS)
}
```


### Verifying with the legacy JWT secret or a shared secret signing key

If your project is still using the legacy JWT secret, or you're using a shared secret (HS256) signing key, we recommend always verifying a user access token directly with the Auth server by sending a request like so:

```http
GET https://project-id.supabase.co/auth/v1/user
apikey: publishable or anon legacy API key
Authorization: Bearer <JWT>
```

If the server responds with HTTP 200 OK, the JWT is valid, otherwise it is not.

Because the Auth server runs only in your project's specified region and is not globally distributed, doing this check can be quite slow depending on where you're performing the check. Avoid doing checks like this from servers or functions running on the edge, and prefer routing to a server within the same geographical region as your project.

If you are using the legacy JWT secret, or you've imported your own shared secret (HS256) signing key, you may wish to verify using the shared secret. **We strongly recommend against this approach.**

<Admonition type="caution">
  There is almost no benefit from using a JWT signed with a shared secret. Although it's computationally more efficient and verification is simpler to code by hand, using this approach can expose your project's data to significant security vulnerabilities or weaknesses.

  Consider the following:

  *   Using a shared secret can make it more difficult to keep aligned with security compliance frameworks such as SOC2, PCI-DSS, ISO27000, HIPAA, etc.
  *   A shared secret that is in the hands of a malicious actor can be used to impersonate your users, give them access to privileged actions or data.
  *   It is difficult to detect or identify when or how a shared secret has been given to a malicious actor.
  *   Consider who might have even accidental access to the shared secret: systems, staff, devices (and their disk encryption and vulnerability patch status).
  *   A malicious actor can use a shared secret **far into the future**, so lacking current evidence of compromise does not mean your data is secure.
  *   It can be very easy to accidentally leak the shared secret in publicly available source code such as in your website or frontend, mobile app package or other executable. This is especially true if you accidentally add the secret in environment variables prefixed with `NEXT_PUBLIC_`, `VITE_`, `PUBLIC_` or other conventions by web frameworks.
  *   Rotating shared secrets might require careful coordination to avoid downtime of your app.
</Admonition>

Check the JWT verification libraries for your language on how to securely verify JWTs signed with the legacy JWT secret or a shared secret (HS256) signing key. We strongly recommend relying on the Auth server as described above, or switching to a different signing key based on public key cryptography (RSA, Elliptic Curves) instead.



## Resources

*   JWT debugger: [https://jwt.io/](https://jwt.io/)
*   [JWT Signing Keys](/docs/guides/auth/signing-keys)
*   [JWT Claims Reference](/docs/guides/auth/jwt-fields) - Complete reference for all JWT claims used by Supabase Auth
*   [API keys](/docs/guides/api/api-keys)



# User Management

View, delete, and export user information.

You can view your users on the [Users page](/dashboard/project/_/auth/users) of the Dashboard. You can also view the contents of the Auth schema in the [Table Editor](/dashboard/project/_/editor).



## Accessing user data via API

For security, the Auth schema is not exposed in the auto-generated API. If you want to access users data via the API, you can create your own user tables in the `public` schema.

Make sure to protect the table by enabling [Row Level Security](/docs/guides/database/postgres/row-level-security). Reference the `auth.users` table to ensure data integrity. Specify `on delete cascade` in the reference. For example, a `public.profiles` table might look like this:

```sql
create table public.profiles (
  id uuid not null references auth.users on delete cascade,
  first_name text,
  last_name text,

  primary key (id)
);

alter table public.profiles enable row level security;
```

<Admonition type="caution">
  Only use primary keys as [foreign key references](https://www.postgresql.org/docs/current/tutorial-fk.html) for schemas and tables like `auth.users` which are managed by Supabase. Postgres lets you specify a foreign key reference for columns backed by a unique index (not necessarily primary keys).

  Primary keys are **guaranteed not to change**. Columns, indices, constraints or other database objects managed by Supabase **may change at any time** and you should be careful when referencing them directly.
</Admonition>

To update your `public.profiles` table every time a user signs up, set up a trigger. If the trigger fails, it could block signups, so test your code thoroughly.

```sql
-- inserts a row into public.profiles
create function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = ''
as $$
begin
  insert into public.profiles (id, first_name, last_name)
  values (new.id, new.raw_user_meta_data ->> 'first_name', new.raw_user_meta_data ->> 'last_name');
  return new;
end;
$$;

-- trigger the function every time a user is created
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```



## Adding and retrieving user metadata

You can assign metadata to users on sign up:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)

    // ---cut---
    const { data, error } = await supabase.auth.signUp({
      email: 'valid.email@supabase.io',
      password: 'example-password',
      options: {
        data: {
          first_name: 'John',
          age: 27,
        },
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final res = await supabase.auth.signUp(
      email: 'valid.email@supabase.io',
      password: 'example-password',
      data: {
        'first_name': 'John',
        'age': 27,
      },
    );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signUp(
      email: "valid.email@supabase.io",
      password: "example-password",
      data: [
        "first_name": .string("John"),
        "age": .integer(27),
      ]
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.auth.signUpWith(Email) {
        email = "valid.email@supabase.io"
        password = "example-password"
        data = buildJsonObject {
            put("first_name", "John")
            put("age", 27)
        }
    }
    ```
  </TabPanel>
</Tabs>

User metadata is stored on the `raw_user_meta_data` column of the `auth.users` table. To view the metadata:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_KEY!)

    // ---cut---
    const {
      data: { user },
    } = await supabase.auth.getUser()
    let metadata = user?.user_metadata
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final User? user = supabase.auth.currentUser;
    final Map<String, dynamic>? metadata = user?.userMetadata;
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let user = try await supabase.auth.user()
    let metadata = user.userMetadata
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val user = supabase.auth.retrieveUserForCurrentSession()
    //Or you can use the user from the current session:
    val user = supabase.auth.currentUserOrNull()
    val metadata = user?.userMetadata
    ```
  </TabPanel>
</Tabs>



## Deleting users

You may delete users directly or via the management console at Authentication > Users. Note that deleting a user from the `auth.users` table does not automatically sign out a user. As Supabase makes use of JSON Web Tokens (JWT), a user's JWT will remain "valid" until it has expired.

<Admonition type="caution">
  You cannot delete a user if they are the owner of any objects in Supabase Storage.

  You will encounter an error when you try to delete an Auth user that owns any Storage objects. If this happens, try deleting all the objects for that user, or reassign ownership to another user.
</Admonition>



## Exporting users

As Supabase is built on top of Postgres, you can query the `auth.users` and `auth.identities` table via the `SQL Editor` tab to extract all users:

```sql
select * from auth.users;
```

You can then export the results as CSV.



# Native Mobile Deep Linking

Set up Deep Linking for mobile applications.

Many Auth methods involve a redirect to your app. For example:

*   Signup confirmation emails, Magic Link signins, and password reset emails contain a link that redirects to your app.
*   In OAuth signins, an automatic redirect occurs to your app.

With Deep Linking, you can configure this redirect to open a specific page. This is necessary if, for example, you need to display a form for [password reset](/docs/guides/auth/passwords#resetting-a-users-password-forgot-password), or to manually exchange a token hash.



## Setting up deep linking

<Tabs scrollable size="large" type="underlined" defaultActiveId="react-native" queryGroup="platform">
  <TabPanel id="react-native" label="Expo React Native">
    To link to your development build or standalone app, you need to specify a custom URL scheme for your app. You can register a scheme in your app config (app.json, app.config.js) by adding a string under the `scheme` key:

    ```json
    {
      "expo": {
        "scheme": "com.supabase"
      }
    }
    ```

    In your project's [auth settings](/dashboard/project/_/auth/url-configuration) add the redirect URL, e.g. `com.supabase://**`.

    Finally, implement the OAuth and linking handlers. See the [supabase-js reference](/docs/reference/javascript/initializing?example=react-native-options-async-storage) for instructions on initializing the supabase-js client in React Native.

    ```tsx ./components/Auth.tsx
    import { Button } from "react-native";
    import { makeRedirectUri } from "expo-auth-session";
    import * as QueryParams from "expo-auth-session/build/QueryParams";
    import * as WebBrowser from "expo-web-browser";
    import * as Linking from "expo-linking";
    import { supabase } from "app/utils/supabase";

    WebBrowser.maybeCompleteAuthSession(); // required for web only
    const redirectTo = makeRedirectUri();

    const createSessionFromUrl = async (url: string) => {
      const { params, errorCode } = QueryParams.getQueryParams(url);

      if (errorCode) throw new Error(errorCode);
      const { access_token, refresh_token } = params;

      if (!access_token) return;

      const { data, error } = await supabase.auth.setSession({
        access_token,
        refresh_token,
      });
      if (error) throw error;
      return data.session;
    };

    const performOAuth = async () => {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: "github",
        options: {
          redirectTo,
          skipBrowserRedirect: true,
        },
      });
      if (error) throw error;

      const res = await WebBrowser.openAuthSessionAsync(
        data?.url ?? "",
        redirectTo
      );

      if (res.type === "success") {
        const { url } = res;
        await createSessionFromUrl(url);
      }
    };

    const sendMagicLink = async () => {
      const { error } = await supabase.auth.signInWithOtp({
        email: "valid.email@supabase.io",
        options: {
          emailRedirectTo: redirectTo,
        },
      });

      if (error) throw error;
      // Email sent.
    };

    export default function Auth() {
      // Handle linking into app from email app.
      const url = Linking.useURL();
      if (url) createSessionFromUrl(url);

      return (
        <>
          <Button onPress={performOAuth} title="Sign in with GitHub" />
          <Button onPress={sendMagicLink} title="Send Magic Link" />
        </>
      );
    }
    ```

    For the best user experience it is recommended to use universal links which require a more elaborate setup. You can find the detailed setup instructions in the [Expo docs](https://docs.expo.dev/guides/deep-linking/).
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    // Currently supabase\_flutter supports deep links on Android, iOS, Web, macOS and Windows.

    ### Deep link config

    *   Go to your [auth settings](/dashboard/project/_/auth/url-configuration) page.
    *   You need to enter your app redirect callback on `Additional Redirect URLs` field.

    The redirect callback URL should have this format `[YOUR_SCHEME]://[YOUR_HOSTNAME]`. Here, `io.supabase.flutterquickstart://login-callback` is just an example, you can choose whatever you would like for `YOUR_SCHEME` and `YOUR_HOSTNAME` as long as the scheme is unique across the user's device. For this reason, typically a reverse domain of your website is used.

    ![Supabase console deep link setting](/docs/img/deeplink-setting.png)

    ### Platform specific config

    <Tabs scrollable size="large" type="underlined" defaultActiveId="android" queryGroup="os">
      <TabPanel id="android" label="Android">
        ```xml
        <manifest ...>
          <!-- ... other tags -->
          <application ...>
            <activity ...>
              <!-- ... other tags -->

              <!-- Deep Links -->
              <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <!-- Accepts URIs that begin with YOUR_SCHEME://YOUR_HOST -->
                <data
                  android:scheme="YOUR_SCHEME"
                  android:host="YOUR_HOSTNAME" />
              </intent-filter>
            </activity>
          </application>
        </manifest>
        ```

        The `android:host` attribute is optional for Deep Links.

        For more info: [https://developer.android.com/training/app-links/deep-linking](https://developer.android.com/training/app-links/deep-linking)
      </TabPanel>

      <TabPanel id="ios" label="iOS">
        For **Custom URL schemes** you need to declare the scheme in
        `ios/Runner/Info.plist` (or through Xcode's Target Info editor,
        under URL Types):

        ```xml
        <!-- ... other tags -->
        <plist>
        <dict>
          <!-- ... other tags -->
          <key>CFBundleURLTypes</key>
          <array>
            <dict>
              <key>CFBundleTypeRole</key>
              <string>Editor</string>
              <key>CFBundleURLSchemes</key>
              <array>
                <string>[YOUR_SCHEME]</string>
              </array>
            </dict>
          </array>
          <!-- ... other tags -->
        </dict>
        </plist>
        ```

        For more info: [https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)
      </TabPanel>

      <TabPanel id="windows" label="Windows">
        Setting up deep links in Windows has few more steps than other platforms.
        [Learn more](https://pub.dev/packages/app_links#windows)

        Declare this method in `<PROJECT_DIR>\windows\runner\win32_window.h`

        ```cpp
          // Dispatches link if any.
          // This method enables our app to be with a single instance too.
          // This is optional but mandatory if you want to catch further links in same app.
          bool SendAppLinkToInstance(const std::wstring& title);
        ```

        Add this inclusion at the top of `<PROJECT_DIR>\windows\runner\win32_window.cpp`

        ```cpp
        #include "app_links_windows/app_links_windows_plugin.h"
        ```

        Add this method in `<PROJECT_DIR>\windows\runner\win32_window.cpp`

        ```cpp
        bool Win32Window::SendAppLinkToInstance(const std::wstring& title) {
          // Find our exact window
          HWND hwnd = ::FindWindow(kWindowClassName, title.c_str());

          if (hwnd) {
            // Dispatch new link to current window
            SendAppLink(hwnd);

            // (Optional) Restore our window to front in same state
            WINDOWPLACEMENT place = { sizeof(WINDOWPLACEMENT) };
            GetWindowPlacement(hwnd, &place);
            switch(place.showCmd) {
              case SW_SHOWMAXIMIZED:
                  ShowWindow(hwnd, SW_SHOWMAXIMIZED);
                  break;
              case SW_SHOWMINIMIZED:
                  ShowWindow(hwnd, SW_RESTORE);
                  break;
              default:
                  ShowWindow(hwnd, SW_NORMAL);
                  break;
            }
            SetWindowPos(0, HWND_TOP, 0, 0, 0, 0, SWP_SHOWWINDOW | SWP_NOSIZE | SWP_NOMOVE);
            SetForegroundWindow(hwnd);
            // END Restore

            // Window has been found, don't create another one.
            return true;
          }

          return false;
        }
        ```

        Add the call to the previous method in `CreateAndShow`

        ```cpp
        bool Win32Window::CreateAndShow(const std::wstring& title,
                                        const Point& origin,
                                        const Size& size) {
        if (SendAppLinkToInstance(title)) {
            return false;
        }

        ...
        ```

        At this point, you can register your own scheme.
        On Windows, URL protocols are setup in the Windows registry.

        This package won't do it for you.

        You can achieve it with [url\_protocol](https://pub.dev/packages/url_protocol) inside you app.

        The most relevant solution is to include those registry modifications into your installer to allow for deregistration.
      </TabPanel>

      <TabPanel id="macos" label="macOS">
        Add this XML chapter in your `macos/Runner/Info.plist` inside `<plist version="1.0"><dict>` chapter:

        ```xml
        <!-- ... other tags -->
        <plist version="1.0">
        <dict>
          <!-- ... other tags -->
          <key>CFBundleURLTypes</key>
          <array>
              <dict>
                  <key>CFBundleURLName</key>
                  <!-- abstract name for this URL type (you can leave it blank) -->
                  <string>sample_name</string>
                  <key>CFBundleURLSchemes</key>
                  <array>
                      <!-- your schemes -->
                      <string>sample</string>
                  </array>
              </dict>
          </array>
          <!-- ... other tags -->
        </dict>
        </plist>
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ### Deep link config

    1.  Go to your [auth settings](/dashboard/project/_/auth/url-configuration) page.
    2.  Enter your app redirect URL in the `Additional Redirect URLs` field. This is the URL that the user gets redirected to after clicking a magic link.

    The redirect callback URL should have the format `[YOUR_SCHEME]://[YOUR_HOSTNAME]`. Here, `io.supabase.user-management://login-callback` is just an example. You can choose whatever you would like for `YOUR_SCHEME` and `YOUR_HOSTNAME` as long as the scheme is unique across the user's device. For this reason, typically a reverse domain of your website is used.

    ![Supabase console deep link setting](/docs/img/deeplink-setting.png)

    Now add a custom URL to your application, so the OS knows how to redirect back your application once the user clicks the magic link.

    You have the option to use Xcode's Target Info Editor following [official Apple documentation](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#Register-your-URL-scheme).

    Or, declare the URL scheme manually in your `Info.plist` file.

    ```xml Info.plist
      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
      <plist version="1.0">
      <dict>
        <!-- other tags -->
        <key>CFBundleURLTypes</key>
        <array>
          <dict>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>CFBundleURLSchemes</key>
            <array>
              <string>io.supabase.user-management</string>
            </array>
          </dict>
        </array>
      </dict>
      </plist>
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Android Kotlin">
    ### Deep link config

    1.  Go to your [auth settings](/dashboard/project/_/auth/url-configuration) page.
    2.  Enter your app redirect URL in the `Additional Redirect URLs` field. This is the URL that the user gets redirected to after clicking a magic link.

    The redirect callback URL should have the format `[YOUR_SCHEME]://[YOUR_HOSTNAME]`. Here, `io.supabase.user-management://login-callback` is just an example. You can choose whatever you would like for `YOUR_SCHEME` and `YOUR_HOSTNAME` as long as the scheme is unique across the user's device. For this reason, typically a reverse domain of your website is used.

    Now, edit the Android manifest to make sure the app opens when the user clicks on the magic link.

    ```xml
    <manifest ...>
      <!-- ... other tags -->
      <application ...>
        <activity ...>
          <!-- ... other tags -->

          <!-- Deep Links -->
          <intent-filter>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.DEFAULT" />
            <category android:name="android.intent.category.BROWSABLE" />
            <!-- Accepts URIs that begin with YOUR_SCHEME://YOUR_HOST -->
            <data
              android:scheme="YOUR_SCHEME"
              android:host="YOUR_HOSTNAME" />
          </intent-filter>
        </activity>
      </application>
    </manifest>
    ```

    Check the [Android documentation](https://developer.android.com/training/app-links/deep-linking) for more information.

    Next, specify the scheme and host in the Supabase Client:

    ```kotlin
    install(Auth) {
       host = "login-callback"
       scheme = "io.supabase.user-management"
    }
    ```

    Finally, call `Auth#handleDeeplinks` when the app opens:

    ```kotlin
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        supabase.handleDeeplinks(intent)
    }
    ```

    The user will now be authenticated when your app receives a valid deep link!
  </TabPanel>
</Tabs>



# Password security

Help your users to protect their password security

A password is more secure if it is harder to guess or brute-force. In theory, a password is harder to guess if it is longer. It is also harder to guess if it uses a larger set of characters (for example, digits, lowercase and uppercase letters, and symbols).

This table shows the *minimum* number of guesses that need to be tried to access a user's account:

| Required characters                          | Length | Guesses           |
| -------------------------------------------- | ------ | ----------------- |
| Digits only                                  | 8      | ~ 2<sup>27</sup> |
| Digits and letters                           | 8      | ~ 2<sup>41</sup> |
| Digits, lower and uppercase letters          | 8      | ~ 2<sup>48</sup> |
| Digits, lower and uppercase letters, symbols | 8      | ~ 2<sup>52</sup> |

In reality though, passwords are not always generated at random. They often contain variations of names, words, dates, and common phrases. Malicious actors can use these properties to guess a password in fewer attempts.

There are hundreds of millions (and growing!) known passwords out there. Malicious actors can use these lists of leaked passwords to automate login attempts (known as credential stuffing) and steal or access sensitive user data.



## Password strength and leaked password protection

To help protect your users, Supabase Auth allows you fine-grained control over the strength of the passwords used on your project. You can configure these in your project's [Auth settings](/dashboard/project/_/auth/providers?provider=Email):

*   Set a large minimum password length. Anything less than 8 characters is not recommended.
*   Set the required characters that must appear at least once in a user's password. Use the strongest option of requiring digits, lowercase and uppercase letters, and symbols. The allowed symbols are: ``!@#$%^&*()_+-=[]{};'\:"|<>?,./`~``
*   Prevent the use of leaked passwords. Supabase Auth uses the open-source [HaveIBeenPwned.org Pwned Passwords API](https://haveibeenpwned.com/Passwords) to reject passwords that have been leaked and are known by malicious actors.

<Admonition type="note">
  Leaked password protection is available on the Pro Plan and above.
</Admonition>



## Additional recommendations

In addition to choosing suitable password strength settings and preventing the use of leaked passwords, consider asking your users to:

*   Use a password manager to store and generate passwords.
*   Avoid password reuse across websites and apps.
*   Avoid using personal information in passwords.
*   Use [Multi-Factor Authentication](/docs/guides/auth/auth-mfa).



## Frequently asked questions


### How are passwords stored?

Supabase Auth uses [bcrypt](https://en.wikipedia.org/wiki/Bcrypt), a strong password hashing function, to store hashes of users' passwords. Only hashed passwords are stored. You cannot impersonate a user with the password hash. Each hash is accompanied by a randomly generated salt parameter for extra security.

The hash is stored in the `encrypted_password` column of the `auth.users` table. The column's name is a misnomer (cryptographic hashing is not encryption), but is kept for backward compatibility.


### How will strengthened password requirements affect current users?

Existing users can still sign in with their current password even if it doesn't meet the new, strengthened password requirements. However, if their password falls short of these updated standards, they will encounter a `WeakPasswordError` during the `signInWithPassword` process, explaining why it's considered weak. This change is also applicable to new users and existing users changing their passwords, ensuring everyone adheres to the enhanced security standards.



# Password-based Auth

Allow users to sign in with a password connected to their email or phone number.

Users often expect to sign in to your site with a password. Supabase Auth helps you implement password-based auth safely, using secure configuration options and best practices for storing and verifying passwords.

Users can associate a password with their identity using their [email address](#with-email) or a [phone number](#with-phone).



## With email


### Enabling email and password-based authentication

Email authentication is enabled by default.

You can configure whether users need to verify their email to sign in. On hosted Supabase projects, this is true by default. On self-hosted projects or in local development, this is false by default.

Change this setting on the [Auth Providers page](/dashboard/project/_/auth/providers) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.email.enable_confirmations) for self-hosted projects.


### Signing up with an email and password

There are two possible flows for email signup: [implicit flow](/docs/guides/auth/sessions#implicit-flow) and [PKCE flow](/docs/guides/auth/sessions#pkce-flow). If you're using SSR, you're using the PKCE flow. If you're using client-only code, the default flow depends upon the client library. The implicit flow is the default in JavaScript and Dart, and the PKCE flow is the default in Swift.

The instructions in this section assume that email confirmations are enabled.

<Tabs
  scrollable
  stickyTabList={{
    style: {
      top: 'var(--header-height)',
      backgroundColor: 'hsl(var(--background-default) / var(--tw-bg-opacity))',
      maskImage: 'none',
      borderBottom: '1px solid hsl(var(--border-default) / 1)',
    }
  }}
  size="large"
  type="underlined"
  queryGroup="flow"
>
  <TabPanel id="implicit" label="Implicit flow">
    The implicit flow only works for client-only apps. Your site directly receives the access token after the user confirms their email.

    <Tabs scrollable size="small" type="underlined" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        To sign up the user, call [signUp()](/docs/reference/javascript/auth-signup) with their email address and password.

        You can optionally specify a URL to redirect to after the user clicks the confirmation link. This URL must be configured as a [Redirect URL](/docs/guides/auth/redirect-urls), which you can do in the [dashboard](/dashboard/project/_/auth/url-configuration) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.additional_redirect_urls) for self-hosted projects.

        If you don't specify a redirect URL, the user is automatically redirected to your site URL. This defaults to `localhost:3000`, but you can also configure this.

        ```js
        import { createClient } from '@supabase/supabase-js'
        const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

        // ---cut---
        async function signUpNewUser() {
          const { data, error } = await supabase.auth.signUp({
            email: 'valid.email@supabase.io',
            password: 'example-password',
            options: {
              emailRedirectTo: 'https://example.com/welcome',
            },
          })
        }
        ```
      </TabPanel>

      <TabPanel id="dart" label="Dart">
        To sign up the user, call [signUp()](/docs/reference/dart/auth-signup) with their email address and password:

        ```dart
        Future<void> signUpNewUser() async {
          final AuthResponse res = await supabase.auth.signUp(
            email: 'valid.email@supabase.io',
            password: 'example-password'
          );
        }
        ```
      </TabPanel>

      <TabPanel id="swift" label="Swift">
        To sign up the user, call [signUp()](/docs/reference/swift/auth-signup) with their email address and password.

        You can optionally specify a URL to redirect to after the user clicks the confirmation link. This URL must be configured as a [Redirect URL](/docs/guides/auth/redirect-urls), which you can do in the [dashboard](/dashboard/project/_/auth/url-configuration) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.additional_redirect_urls) for self-hosted projects.

        If you don't specify a redirect URL, the user is automatically redirected to your site URL. This defaults to `localhost:3000`, but you can also configure this.

        ```swift
        let response = try await supabase.auth.signUp(
          email: "valid.email@supabase.io",
          password: "example-password",
          redirectTo: URL(string: "https://example.com/welcome")
        )
        ```
      </TabPanel>

      <TabPanel id="kotlin" label="Kotlin">
        To sign up the user, call [signUpWith(Email)](/docs/reference/kotlin/auth-signup) with their email address and password:

        ```kotlin
        suspend fun signUpNewUser() {
        	supabase.auth.signUpWith(Email) {
        		email = "valid.email@supabase.io"
        		password = "example-password"
        	}
        }
        ```
      </TabPanel>

      <TabPanel id="python" label="Python">
        To sign up the user, call [signUp()](/docs/reference/python/auth-signup) with their email address and password.

        You can optionally specify a URL to redirect to after the user clicks the confirmation link. This URL must be configured as a [Redirect URL](/docs/guides/auth/redirect-urls), which you can do in the [dashboard](/dashboard/project/_/auth/url-configuration) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.additional_redirect_urls) for self-hosted projects.

        If you don't specify a redirect URL, the user is automatically redirected to your site URL. This defaults to `localhost:3000`, but you can also configure this.

        ```python
        data = await supabase.auth.sign_up({
          'email': 'valid.email@supabase.io',
          'password': 'example-password',
          'options': {
            'email_redirect_to': 'https://example.com/welcome',
          },
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="pkce" label="PKCE flow">
    The PKCE flow allows for server-side authentication. Unlike the implicit flow, which directly provides your app with the access token after the user clicks the confirmation link, the PKCE flow requires an intermediate token exchange step before you can get the access token.

    ##### Step 1: Update signup confirmation email

    Update your signup email template to send the token hash. For detailed instructions on how to configure your email templates, including the use of variables like `{{ .SiteURL }}`, `{{ .TokenHash }}`, and `{{ .RedirectTo }}`, refer to our [Email Templates](/docs/guides/auth/auth-email-templates) guide.

    Your signup email template should contain the following HTML:

    ```html
    <h2>Confirm your signup</h2>

    <p>Follow this link to confirm your user:</p>
    <p>
      <a
        href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email&next={{ .RedirectTo }}"
        >Confirm your email</a
      >
    </p>
    ```

    ##### Step 2: Create token exchange endpoint

    Create an API endpoint at `<YOUR_SITE_URL>/auth/confirm` to handle the token exchange.

    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    <Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
      <TabPanel id="nextjs" label="Next.js">
        Create a new file at `app/auth/confirm/route.ts` and populate with the following:

        ```ts app/auth/confirm/route.ts
        import { type EmailOtpType } from '@supabase/supabase-js'
        import { type NextRequest } from 'next/server'

        import { createClient } from '@/utils/supabase/server'
        import { redirect } from 'next/navigation'

        export async function GET(request: NextRequest) {
          const { searchParams } = new URL(request.url)
          const token_hash = searchParams.get('token_hash')
          const type = searchParams.get('type') as EmailOtpType | null
          const next = searchParams.get('next') ?? '/'

          if (token_hash && type) {
            const supabase = await createClient()

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })
            if (!error) {
              // redirect user to specified redirect URL or root of app
              redirect(next)
            }
          }

          // redirect the user to an error page with some instructions
          redirect('/auth/auth-code-error')
        }
        ```
      </TabPanel>

      <TabPanel id="sveltekit" label="SvelteKit">
        Create a new file at `src/routes/auth/confirm/+server.ts` and populate with the following:

        ```ts src/routes/auth/confirm/+server.ts
        import { redirect } from '@sveltejs/kit'
        import { type EmailOtpType } from '@supabase/supabase-js'

        export const GET = async (event) => {
          const {
            url,
            locals: { supabase },
          } = event
          const token_hash = url.searchParams.get('token_hash') as string
          const type = url.searchParams.get('type') as EmailOtpType | null
          const next = url.searchParams.get('next') ?? '/'

          /**
           * Clean up the redirect URL by deleting the Auth flow parameters.
           *
           * `next` is preserved for now, because it's needed in the error case.
           */
          const redirectTo = new URL(url)
          redirectTo.pathname = next
          redirectTo.searchParams.delete('token_hash')
          redirectTo.searchParams.delete('type')

          if (token_hash && type) {
            const { error } = await supabase.auth.verifyOtp({ token_hash, type })
            if (!error) {
              redirectTo.searchParams.delete('next')
              redirect(303, redirectTo)
            }
          }

          // return the user to an error page with some instructions
          redirectTo.pathname = '/auth/error'
          redirect(303, redirectTo)
        }
        ```
      </TabPanel>

      <TabPanel id="astro" label="Astro">
        Create a new file at `src/pages/auth/confirm.ts` and populate with the following:

        ```ts src/pages/auth/confirm.ts
        import { createServerClient, parseCookieHeader } from '@supabase/ssr'
        import { type EmailOtpType } from '@supabase/supabase-js'
        import { type APIRoute } from 'astro'

        export const GET: APIRoute = async ({ request, cookies, redirect }) => {
          const requestUrl = new URL(request.url)
          const token_hash = requestUrl.searchParams.get('token_hash')
          const type = requestUrl.searchParams.get('type') as EmailOtpType | null
          const next = requestUrl.searchParams.get('next') || '/'

          if (token_hash && type) {
            const supabase = createServerClient(
              import.meta.env.PUBLIC_SUPABASE_URL,
              import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
              {
                cookies: {
                  getAll() {
                    return parseCookieHeader(request.headers.get('Cookie') ?? '')
                  },
                  setAll(cookiesToSet) {
                    cookiesToSet.forEach(({ name, value, options }) => cookies.set(name, value, options))
                  },
                },
              }
            )

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })

            if (!error) {
              return redirect(next)
            }
          }

          // return the user to an error page with some instructions
          return redirect('/auth/auth-code-error')
        }
        ```
      </TabPanel>

      <TabPanel id="remix" label="Remix">
        Create a new file at `app/routes/auth.confirm.tsx` and populate with the following:

        ```ts app/routes/auth.confirm.tsx
        import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
        import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'
        import { type EmailOtpType } from '@supabase/supabase-js'

        export async function loader({ request }: LoaderFunctionArgs) {
          const requestUrl = new URL(request.url)
          const token_hash = requestUrl.searchParams.get('token_hash')
          const type = requestUrl.searchParams.get('type') as EmailOtpType | null
          const next = requestUrl.searchParams.get('next') || '/'
          const headers = new Headers()

          if (token_hash && type) {
            const supabase = createServerClient(
              process.env.SUPABASE_URL!,
              process.env.SUPABASE_PUBLISHABLE_KEY!,
              {
                cookies: {
                  getAll() {
                    return parseCookieHeader(request.headers.get('Cookie') ?? '')
                  },
                  setAll(key, value, options) {
                    headers.append('Set-Cookie', serializeCookieHeader(key, value, options))
                  },
                },
              }
            )

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })

            if (!error) {
              return redirect(next, { headers })
            }
          }

          // return the user to an error page with instructions
          return redirect('/auth/auth-code-error', { headers })
        }
        ```
      </TabPanel>

      <TabPanel id="express" label="Express">
        Create a new route in your express app and populate with the following:

        ```js app.js
        // The client you created from the Server-Side Auth instructions
        const { createClient } = require("./lib/supabase")
        ...
        app.get("/auth/confirm", async function (req, res) {
          const token_hash = req.query.token_hash
          const type = req.query.type
          const next = req.query.next ?? "/"

          if (token_hash && type) {
            const supabase = createClient({ req, res })
            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })
            if (!error) {
              res.redirect(303, `/${next.slice(1)}`)
            }
          }

          // return the user to an error page with some instructions
          res.redirect(303, '/auth/auth-code-error')
        })
        ```
      </TabPanel>
    </Tabs>

    ##### Step 3: Call the sign up function to initiate the flow

    <Tabs scrollable size="small" type="underlined" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        To sign up the user, call [signUp()](/docs/reference/javascript/auth-signup) with their email address and password:

        You can optionally specify a URL to redirect to after the user clicks the confirmation link. This URL must be configured as a [Redirect URL](/docs/guides/auth/redirect-urls), which you can do in the [dashboard](/dashboard/project/_/auth/url-configuration) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.additional_redirect_urls) for self-hosted projects.

        If you don't specify a redirect URL, the user is automatically redirected to your site URL. This defaults to `localhost:3000`, but you can also configure this.

        ```js
        import { createClient } from '@supabase/supabase-js'
        const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

        // ---cut---
        async function signUpNewUser() {
          const { data, error } = await supabase.auth.signUp({
            email: 'valid.email@supabase.io',
            password: 'example-password',
            options: {
              emailRedirectTo: 'https://example.com/welcome',
            },
          })
        }
        ```
      </TabPanel>

      <TabPanel id="dart" label="Dart">
        To sign up the user, call [signUp()](/docs/reference/dart/auth-signup) with their email address and password:

        ```dart
        Future<void> signUpNewUser() async {
          final AuthResponse res = await supabase.auth.signUp(
            email: 'valid.email@supabase.io',
            password: 'example-password'
          );
        }
        ```
      </TabPanel>

      <TabPanel id="swift" label="Swift">
        To sign up the user, call [signUp()](/docs/reference/swift/auth-signup) with their email address and password:

        ```swift
        let response = try await supabase.auth.signUp(
          email: "valid.email@supabase.io",
          password: "example-password",
        )
        ```
      </TabPanel>

      <TabPanel id="kotlin" label="Kotlin">
        To sign up the user, call [signUpWith(Email)](/docs/reference/kotlin/auth-signup) with their email address and password:

        ```kotlin
        suspend fun signUpNewUser() {
        	supabase.auth.signUpWith(Email) {
        		email = "valid.email@supabase.io"
        		password = "example-password"
        	}
        }
        ```
      </TabPanel>

      <TabPanel id="python" label="Python">
        To sign up the user, call [signUp()](/docs/reference/python/auth-signup) with their email address and password:

        ```python
        data = supabase.auth.sign_up({
          'email': 'valid.email@supabase.io',
          'password': 'example-password',
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Signing in with an email and password

<Tabs scrollable size="small" type="underlined" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs in, call [`signInWithPassword()`](/docs/reference/javascript/auth-signinwithpassword) with their email address and password:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    async function signInWithEmail() {
      const { data, error } = await supabase.auth.signInWithPassword({
        email: 'valid.email@supabase.io',
        password: 'example-password',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    When your user signs in, call [`signInWithPassword()`](/docs/reference/dart/auth-signinwithpassword) with their email address and password:

    ```dart
    Future<void> signInWithEmail() async {
      final AuthResponse res = await supabase.auth.signInWithPassword(
        email: 'valid.email@supabase.io',
        password: 'example-password'
      );
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    When your user signs in, call [signIn(email:password:)](/docs/reference/swift/auth-signinwithpassword) with their email address and password:

    ```swift
    try await supabase.auth.signIn(
      email: "valid.email@supabase.io",
      password: "example-password"
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Email)](/docs/reference/kotlin/auth-signinwithpassword) with their email address and password:

    ```kotlin
    suspend fun signInWithEmail() {
    	supabase.auth.signInWith(Email) {
    		email = "valid.email@supabase.io"
    		password = "example-password"
    	}
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    When your user signs in, call [sign\_in\_with\_password()](/docs/reference/python/auth-signinwithpassword) with their email address and password:

    ```python
    data = client.auth.sign_in_with_password({
      'email': 'valid.email@supabase.io',
      'password': 'example-password',
    })
    ```
  </TabPanel>
</Tabs>


### Resetting a password

<Tabs scrollable size="small" type="underlined" queryGroup="flow">
  <TabPanel id="implicit" label="Implicit flow">
    #### Step 1: Create a reset password page

    Create a **reset password** page. This page should be publicly accessible.

    Collect the user's email address and request a password reset email. Specify the redirect URL, which should point to the URL of a **change password** page. This URL needs to be configured in your [redirect URLs](/docs/guides/auth/redirect-urls).

    <Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        ```js
        import { createClient } from '@supabase/supabase-js'
        const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

        // ---cut---
        await supabase.auth.resetPasswordForEmail('valid.email@supabase.io', {
          redirectTo: 'http://example.com/account/update-password',
        })
        ```
      </TabPanel>

      <TabPanel id="swift" label="Swift">
        ```swift
        try await supabase.auth.resetPasswordForEmail(
           "valid.email@supabase.io",
           redirectTo: URL(string: "http://example.com/account/update-password")
        )
        ```
      </TabPanel>

      <TabPanel id="kotlin" label="Kotlin">
        ```kotlin
        supabase.auth.resetPasswordForEmail(
            email = "valid.email@supabase.io",
            redirectUrl = "http://example.com/account/update-password"
        )
        ```

        If you are on one of the Kotlin targets that have built-in support for redirect URL handling, such as Android, see [OAuth and OTP link verification](/docs/reference/kotlin/initializing).
      </TabPanel>

      <TabPanel id="python" label="Python">
        ```python
        client.auth.reset_password_email(
          'valid.email@supabase.io',
          {'redirect_to':'http://example.com/account/update-password'}
        )
        ```
      </TabPanel>

      <TabPanel id="dart" label="Dart">
        ```dart
        await supabase.auth.resetPasswordForEmail(
          'valid.email@supabase.io',
          redirectTo: 'http://example.com/account/update-password',
        );
        ```
      </TabPanel>
    </Tabs>

    #### Step 2: Create a change password page

    Create a **change password** page at the URL you specified in the previous step. This page should be accessible only to authenticated users.

    Collect the user's new password and call `updateUser` to update their password.
  </TabPanel>

  <TabPanel id="pkce" label="PKCE flow">
    The PKCE flow allows for server-side authentication. Unlike the implicit flow, which directly provides your app with the access token after the user clicks the confirmation link, the PKCE flow requires an intermediate token exchange step before you can get the access token.

    ##### Step 1: Update reset password email

    Update your reset password email template to send the token hash. See [Email Templates](/docs/guides/auth/auth-email-templates) for how to configure your email templates.

    Your reset password email template should contain the following HTML:

    ```html
    <h2>Reset Password</h2>

    <p>Follow this link to reset the password for your user:</p>
    <p>
      <a
        href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=recovery&next=/account/update-password"
        >Reset Password</a
      >
    </p>
    ```

    ##### Step 2: Create token exchange endpoint

    Create an API endpoint at `<YOUR_SITE_URL>/auth/confirm` to handle the token exchange.

    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    <Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
      <TabPanel id="nextjs" label="Next.js">
        Create a new file at `app/auth/confirm/route.ts` and populate with the following:

        ```ts app/auth/confirm/route.ts
        import { type EmailOtpType } from '@supabase/supabase-js'
        import { cookies } from 'next/headers'
        import { NextRequest, NextResponse } from 'next/server'
        // The client you created from the Server-Side Auth instructions
        import { createClient } from '@/utils/supabase/server'

        export async function GET(request: NextRequest) {
          const { searchParams } = new URL(request.url)
          const token_hash = searchParams.get('token_hash')
          const type = searchParams.get('type') as EmailOtpType | null
          const next = searchParams.get('next') ?? '/'
          const redirectTo = request.nextUrl.clone()
          redirectTo.pathname = next

          if (token_hash && type) {
            const supabase = await createClient()

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })
            if (!error) {
              return NextResponse.redirect(redirectTo)
            }
          }

          // return the user to an error page with some instructions
          redirectTo.pathname = '/auth/auth-code-error'
          return NextResponse.redirect(redirectTo)
        }
        ```
      </TabPanel>

      <TabPanel id="sveltekit" label="SvelteKit">
        Create a new file at `src/routes/auth/confirm/+server.ts` and populate with the following:

        ```ts src/routes/auth/confirm/+server.ts
        import { redirect } from '@sveltejs/kit'
        import { type EmailOtpType } from '@supabase/supabase-js'

        export const GET = async (event) => {
          const {
            url,
            locals: { supabase },
          } = event
          const token_hash = url.searchParams.get('token_hash') as string
          const type = url.searchParams.get('type') as EmailOtpType | null
          const next = url.searchParams.get('next') ?? '/'

          /**
           * Clean up the redirect URL by deleting the Auth flow parameters.
           *
           * `next` is preserved for now, because it's needed in the error case.
           */
          const redirectTo = new URL(url)
          redirectTo.pathname = next
          redirectTo.searchParams.delete('token_hash')
          redirectTo.searchParams.delete('type')

          if (token_hash && type) {
            const { error } = await supabase.auth.verifyOtp({ token_hash, type })
            if (!error) {
              redirectTo.searchParams.delete('next')
              redirect(303, redirectTo)
            }
          }

          // return the user to an error page with some instructions
          redirectTo.pathname = '/auth/error'
          redirect(303, redirectTo)
        }
        ```
      </TabPanel>

      <TabPanel id="astro" label="Astro">
        Create a new file at `src/pages/auth/confirm.ts` and populate with the following:

        ```ts src/pages/auth/confirm.ts
        import { createServerClient, parseCookieHeader } from '@supabase/ssr'
        import { type EmailOtpType } from '@supabase/supabase-js'
        import { type APIRoute } from 'astro'

        export const GET: APIRoute = async ({ request, cookies, redirect }) => {
          const requestUrl = new URL(request.url)
          const token_hash = requestUrl.searchParams.get('token_hash')
          const type = requestUrl.searchParams.get('type') as EmailOtpType | null
          const next = requestUrl.searchParams.get('next') || '/'

          if (token_hash && type) {
            const supabase = createServerClient(
              import.meta.env.PUBLIC_SUPABASE_URL,
              import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
              {
                cookies: {
                  getAll() {
                    return parseCookieHeader(request.headers.get('Cookie') ?? '')
                  },
                  setAll(cookiesToSet) {
                    cookiesToSet.forEach(({ name, value, options }) => cookies.set(name, value, options))
                  },
                },
              }
            )

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })

            if (!error) {
              return redirect(next)
            }
          }

          // return the user to an error page with some instructions
          return redirect('/auth/auth-code-error')
        }
        ```
      </TabPanel>

      <TabPanel id="remix" label="Remix">
        Create a new file at `app/routes/auth.confirm.tsx` and populate with the following:

        ```ts app/routes/auth.confirm.tsx
        import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
        import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'
        import { type EmailOtpType } from '@supabase/supabase-js'

        export async function loader({ request }: LoaderFunctionArgs) {
          const requestUrl = new URL(request.url)
          const token_hash = requestUrl.searchParams.get('token_hash')
          const type = requestUrl.searchParams.get('type') as EmailOtpType | null
          const next = requestUrl.searchParams.get('next') || '/'
          const headers = new Headers()

          if (token_hash && type) {
            const supabase = createServerClient(
              process.env.SUPABASE_URL!,
              process.env.SUPABASE_PUBLISHABLE_KEY!,
              {
                cookies: {
                  getAll() {
                    return parseCookieHeader(request.headers.get('Cookie') ?? '')
                  },
                  setAll(key, value, options) {
                    headers.append('Set-Cookie', serializeCookieHeader(key, value, options))
                  },
                },
              }
            )

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })

            if (!error) {
              return redirect(next, { headers })
            }
          }

          // return the user to an error page with instructions
          return redirect('/auth/auth-code-error', { headers })
        }
        ```
      </TabPanel>

      <TabPanel id="express" label="Express">
        Create a new route in your express app and populate with the following:

        ```js app.js
        // The client you created from the Server-Side Auth instructions
        const { createClient } = require("./lib/supabase")
        ...
        app.get("/auth/confirm", async function (req, res) {
          const token_hash = req.query.token_hash
          const type = req.query.type
          const next = req.query.next ?? "/"

          if (token_hash && type) {
            const supabase = createClient({ req, res })
            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })
            if (!error) {
              res.redirect(303, `/${next.slice(1)}`)
            }
          }

          // return the user to an error page with some instructions
          res.redirect(303, '/auth/auth-code-error')
        })
        ```
      </TabPanel>
    </Tabs>

    ##### Step 3: Call the reset password by email function to initiate the flow

    <Tabs scrollable size="small" type="underlined" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        ```js
        async function resetPassword() {
          const { data, error } = await supabase.auth.resetPasswordForEmail(email)
        }
        ```
      </TabPanel>

      <TabPanel id="swift" label="Swift">
        ```swift
        try await supabase.auth.resetPasswordForEmail("valid.email@supabase.io")
        ```
      </TabPanel>

      <TabPanel id="kotlin" label="Kotlin">
        ```kotlin
        supabase.gotrue.sendRecoveryEmail(
            email = "valid.email@supabase.io",
        )
        ```
      </TabPanel>

      <TabPanel id="python" label="Python">
        ```python
        supabase.auth.reset_password_email('valid.email@supabase.io')
        ```
      </TabPanel>

      <TabPanel id="dart" label="Dart">
        ```dart
        await supabase.auth.resetPasswordForEmail('valid.email@supabase.io');
        ```
      </TabPanel>
    </Tabs>

    Once you have a session, collect the user's new password and call `updateUser` to update their password.
  </TabPanel>
</Tabs>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    await supabase.auth.updateUser({ password: 'new_password' })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.updateUser(user: UserAttributes(password: newPassword))
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.updateUser {
        password = "new_password"
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.auth.update_user({'password': 'new_password'})
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final UserResponse res = await supabase.auth.updateUser(
      UserAttributes(password: 'new_password'),
    );
    ```
  </TabPanel>
</Tabs>


### Email sending

The signup confirmation and password reset flows require an SMTP server to send emails.

The Supabase platform comes with a default email-sending service for you to try out. The service has a rate limit of <SharedData data="config">auth.rate\_limits.email.inbuilt\_smtp\_per\_hour.value</SharedData> emails per hour, and availability is on a best-effort basis. For production use, you should consider configuring a custom SMTP server.

<Admonition type="tip">
  Consider configuring a custom SMTP server for production.
</Admonition>

See the [Custom SMTP guide](/docs/guides/auth/auth-smtp) for instructions.


#### Local development with Mailpit

You can test email flows on your local machine. The Supabase CLI automatically captures emails sent locally by using [Mailpit](https://github.com/axllent/mailpit).

In your terminal, run `supabase status` to get the Mailpit URL. Go to this URL in your browser, and follow the instructions to find your emails.



## With phone

You can use a user's mobile phone number as an identifier, instead of an email address, when they sign up with a password.

This practice is usually discouraged because phone networks recycle mobile phone numbers. Anyone receiving a recycled phone number gets access to the original user's account. To mitigate this risk, [implement MFA](/docs/guides/auth/auth-mfa).

<Admonition type="danger">
  Protect users who use a phone number as a password-based auth identifier by enabling MFA.
</Admonition>


### Enabling phone and password-based authentication

Enable phone authentication on the [Auth Providers page](/dashboard/project/_/auth/providers) for hosted Supabase projects.

For self-hosted projects or local development, use the [configuration file](/docs/guides/cli/config#auth.sms.enable_signup). See the configuration variables namespaced under `auth.sms`.

If you want users to confirm their phone number on signup, you need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

<AuthSmsProviderConfig />


### Signing up with a phone number and password

To sign up the user, call [`signUp()`](/docs/reference/javascript/auth-signup) with their phone number and password:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const { data, error } = await supabase.auth.signUp({
      phone: '+13334445555',
      password: 'some-password',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signUp(
      phone: "+13334445555",
      password: "some-password"
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.signUpWith(Phone) {
        phone = "+13334445555"
        password = "some-password"
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.auth.sign_up({
      'phone': "+13334445555",
      'password': "some-password"
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final AuthResponse res = await supabase.auth.signUp(
      phone: '+13334445555',
      password: 'some-password',
    );
    ```
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    ```bash
    curl -X POST 'https://cvwawazfelidkloqmbma.supabase.co/auth/v1/signup' \
    -H "apikey: SUPABASE_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "phone": "+13334445555",
      "password": "some-password"
    }'
    ```
  </TabPanel>
</Tabs>

If you have phone verification turned on, the user receives an SMS with a 6-digit pin that you must verify within 60 seconds:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOtp`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const {
      data: { session },
      error,
    } = await supabase.auth.verifyOtp({
      phone: '+13334445555',
      token: '123456',
      type: 'sms',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOTP`:

    ```swift
    try await supabase.auth.verifyOTP(
      phone: "+13334445555",
      token: "123456",
      type: .sms
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyPhoneOtp`:

    ```kotlin
    supabase.auth.verifyPhoneOtp(
        type = OtpType.Phone.SMS,
        phone = "+13334445555",
        token = "123456"
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verify_otp`:

    ```python
    supabase.auth.verify_otp({
      'phone': "+13334445555",
      'token': "123456",
      'type': "sms"
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOTP`:

    ```dart
    final AuthResponse res = await supabase.auth.verifyOTP(
      phone: '+13334445555',
      token: '123456',
      type: OtpType.sms,
    );
    ```
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    ```bash
    curl -X POST 'https://<PROJECT_REF>.supabase.co/auth/v1/verify' \
    -H "apikey: <SUPABASE_KEY>" \
    -H "Content-Type: application/json" \
    -d '{
      "type": "sms",
      "phone": "+13334445555",
      "token": "123456"
    }'
    ```
  </TabPanel>
</Tabs>


### Signing in a with a phone number and password

Call the function to sign in with the user's phone number and password:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const { data, error } = await supabase.auth.signInWithPassword({
      phone: '+13334445555',
      password: 'some-password',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signIn(
      phone: "+13334445555",
      password: "some-password"
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.signInWith(Phone) {
        phone = "+13334445555"
        password = "some-password"
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.auth.sign_in_with_password({
      'phone': "+13334445555",
      'password': "some-password"
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final AuthResponse res = await supabase.auth.signInWithPassword(
      phone: '+13334445555',
      password: 'some-password',
    );
    ```
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    ```bash
    curl -X POST 'https://cvwawazfelidkloqmbma.supabase.co/auth/v1/token?grant_type=password' \
    -H "apikey: SUPABASE_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "phone": "+13334445555",
      "password": "some-password"
    }'
    ```
  </TabPanel>
</Tabs>



---
**Navigation:** [← Previous](./27-install.md) | [Index](./index.md) | [Next →](./29-phone-login.md)
