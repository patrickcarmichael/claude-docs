# Supabase Documentation - Chunked Version

This documentation has been split into manageable chunks for easier navigation.

## Table of Contents

1. [AI & Vectors](./01-ai-vectors.md)
   - AI & Vectors
   - Search
   - Examples
   - Integrations
   - Case studies
   - ... and 74 more sections
2. [Metrics](./02-metrics.md)
   - Metrics
   - Accessing the metrics endpoint
   - Get your access token from https://supabase.com/dashboard/account/tokens
   - Get project API keys including service_role key
   - Supabase Grafana
   - ... and 59 more sections
3. [Storage Helper Functions](./03-storage-helper-functions.md)
   - Storage Helper Functions
   - S3 Authentication
   - S3 access keys
   - Session token
   - S3 Compatibility
   - ... and 58 more sections
4. [Stop and remove the containers](./04-stop-and-remove-the-containers.md)
   - Stop and remove the containers
   - Recreate and start the containers
   - Stopping all services
   - Uninstalling
   - Stop docker and remove volumes:
   - ... and 83 more sections
5. [Realtime Concepts](./05-realtime-concepts.md)
   - Realtime Concepts
   - Concepts
   - Channels
   - Database resources
   - Operational Error Codes
   - ... and 25 more sections
6. [Realtime Quotas](./06-realtime-quotas.md)
   - Realtime Quotas
   - Quotas by plan
   - Quota errors
   - Postgres changes payload quota
   - Listening to Postgres Changes with Flutter
   - ... and 23 more sections
7. [AWS Marketplace](./07-aws-marketplace.md)
   - AWS Marketplace
   - More information
   - Next steps
   - Database Backups
   - Types of backups
   - ... and 48 more sections
8. [HIPAA Projects](./08-hipaa-projects.md)
   - HIPAA Projects
   - Configuring a HIPAA project
   - Dedicated IPv4 Address for Ingress
   - Understanding IP addresses
   - When you need the IPv4 add-on:
   - ... and 122 more sections
9. [Set Up SSO with Okta](./09-set-up-sso-with-okta.md)
   - Set Up SSO with Okta
   - Step 1: Choose to create an app integration in the applications dashboard \[#create-app-integration]
   - Step 2: Choose SAML 2.0 in the app integration dialog \[#create-saml-app]
   - Step 3: Fill out general settings \[#add-general-settings]
   - Step 4: Fill out SAML settings \[#add-saml-settings]
   - ... and 90 more sections
10. [Set Supabase connection (Session Pooler on port 5432 or direct connection)](./10-set-supabase-connection-session-pooler-on-port-543.md)
   - Set Supabase connection (Session Pooler on port 5432 or direct connection)
   - Determine restore parallelization based on your Supabase compute size:
   - Free tier: 2 cores → use -j 2
   - Small compute: 2 cores → use -j 2
   - Medium compute: 4 cores → use -j 4
   - ... and 128 more sections
11. [Manage Point-in-Time Recovery usage](./11-manage-point-in-time-recovery-usage.md)
   - Manage Point-in-Time Recovery usage
   - What you are charged for
   - How charges are calculated
   - Pricing
   - Billing examples
   - ... and 82 more sections
12. [Advanced pgTAP Testing](./12-advanced-pgtap-testing.md)
   - Advanced pgTAP Testing
   - Using database.dev
   - Test helper benefits
   - Schema-wide Row Level Security testing
   - Test file organization
   - ... and 61 more sections
13. [Build a User Management App with Expo React Native](./13-build-a-user-management-app-with-expo-react-native.md)
   - Build a User Management App with Expo React Native
   - Project setup
   - Building the app
   - Bonus: Profile photos
   - Build a User Management App with Flutter
   - ... and 13 more sections
14. [Build a User Management App with Ionic Vue](./14-build-a-user-management-app-with-ionic-vue.md)
   - Build a User Management App with Ionic Vue
   - Project setup
   - Building the app
   - Bonus: Profile photos
   - Build a Product Management Android App with Jetpack Compose
   - ... and 8 more sections
15. [Build a User Management App with Nuxt 3](./15-build-a-user-management-app-with-nuxt-3.md)
   - Build a User Management App with Nuxt 3
   - Project setup
   - Building the app
   - Bonus: Profile photos
   - Build a User Management App with React
   - ... and 15 more sections
16. [Build a User Management App with SolidJS](./16-build-a-user-management-app-with-solidjs.md)
   - Build a User Management App with SolidJS
   - Project setup
   - Building the app
   - Bonus: Profile photos
   - Build a User Management App with Svelte
   - ... and 12 more sections
17. [Build a User Management App with Vue 3](./17-build-a-user-management-app-with-vue-3.md)
   - Build a User Management App with Vue 3
   - Project setup
   - Building the app
   - npm 6.x
   - npm 7+, extra double-dash is needed:
   - ... and 18 more sections
18. [Use Supabase with SvelteKit](./18-use-supabase-with-sveltekit.md)
   - Use Supabase with SvelteKit
   - Next steps
   - Use Supabase with Vue
   - Running AI Models
   - Setup
   - ... and 72 more sections
19. [Type-Safe SQL with Kysely](./19-type-safe-sql-with-kysely.md)
   - Type-Safe SQL with Kysely
   - Code
   - Limits
   - Runtime limits
   - Platform limits
   - ... and 83 more sections
20. [Custom Auth Emails with React Email and Resend](./20-custom-auth-emails-with-react-email-and-resend.md)
   - Custom Auth Emails with React Email and Resend
   - More resources
   - CAPTCHA support with Cloudflare Turnstile
   - Setup
   - Code
   - ... and 70 more sections
21. [Production Checklist](./21-production-checklist.md)
   - Production Checklist
   - Security
   - Performance
   - Availability
   - Rate limiting, resource allocation, & abuse prevention
   - ... and 88 more sections
22. [Connection management](./22-connection-management.md)
   - Connection management
   - Connections
   - Monitoring connections
   - Customizing Postgres configs
   - Configurable settings
   - ... and 37 more sections
23. [Debugging and monitoring](./23-debugging-and-monitoring.md)
   - Debugging and monitoring
   - Using the CLI
   - Using SQL
   - Querying Joins and Nested tables
   - One-to-many joins
   - ... and 47 more sections
24. [Securing your data](./24-securing-your-data.md)
   - Securing your data
   - Connecting your app securely
   - More information
   - Supavisor
   - Tables and Data
   - ... and 73 more sections
25. [Event Triggers](./25-event-triggers.md)
   - Event Triggers
   - Creating an event trigger
   - Disabling an event trigger
   - Dropping an event trigger
   - Resources
   - ... and 94 more sections
26. [pg_stat_statements: Query Performance Monitoring](./26-pg_stat_statements-query-performance-monitoring.md)
   - pg_stat_statements: Query Performance Monitoring
   - Enable the extension
   - Inspecting activity
   - Resources
   - PGAudit: Postgres Auditing
   - ... and 86 more sections
27. [Install](./27-install.md)
   - Install
   - Uninstall
   - Quickstart
   - Schedule a job
   - Edit a job
   - ... and 54 more sections
28. [Send emails with custom SMTP](./28-send-emails-with-custom-smtp.md)
   - Send emails with custom SMTP
   - How to set up a custom SMTP server?
   - Get your access token from https://supabase.com/dashboard/account/tokens
   - Configure custom SMTP
   - Dealing with abuse: How to maintain the sending reputation of your SMTP server?
   - ... and 42 more sections
29. [Phone Login](./29-phone-login.md)
   - Phone Login
   - Enabling phone login
   - Signing in with phone OTP
   - Verifying a phone OTP
   - Updating a phone number
   - ... and 48 more sections
30. [Clerk](./30-clerk.md)
   - Clerk
   - Getting started
   - Setup the Supabase client library
   - Using RLS policies
   - Deprecated integration with JWT templates
   - ... and 29 more sections
31. [Login with Bitbucket](./31-login-with-bitbucket.md)
   - Login with Bitbucket
   - Overview
   - Access your Bitbucket account
   - Find your callback URL
   - Create a Bitbucket OAuth app
   - ... and 49 more sections
32. [Login with Google](./32-login-with-google.md)
   - Login with Google
   - Prerequisites
   - Project setup
   - Signing users in
   - Login with Kakao
   - ... and 31 more sections
33. [Login with Notion](./33-login-with-notion.md)
   - Login with Notion
   - Overview
   - Create your notion integration
   - Add the redirect URI
   - Add your Notion credentials into your Supabase project
   - ... and 60 more sections
34. [Implicit flow](./34-implicit-flow.md)
   - Implicit flow
   - How it works
   - Limitations
   - PKCE flow
   - How it works
   - ... and 14 more sections
35. [Use Supabase Auth with Next.js](./35-use-supabase-auth-with-nextjs.md)
   - Use Supabase Auth with Next.js
   - Learn more
   - Use Supabase Auth with React Native
   - Use Supabase Auth with React
   - Build a Social Auth App with Expo React Native
   - ... and 10 more sections
36. [Error Codes](./36-error-codes.md)
   - Error Codes
   - Auth error codes
   - Error types
   - HTTP status codes
   - Auth error codes table
   - ... and 14 more sections
37. [Send Email Hook](./37-send-email-hook.md)
   - Send Email Hook
   - Email sending behavior
   - Email change behavior and token hash mapping
   - Send SMS Hook
   - Auth UI
   - ... and 5 more sections
38. [Supabase Auth with the Next.js App Router](./38-supabase-auth-with-the-nextjs-app-router.md)
   - Supabase Auth with the Next.js App Router
   - Supabase Auth with Remix
   - Supabase Auth with SvelteKit
39. [Understanding API keys](./39-understanding-api-keys.md)
   - Understanding API keys
   - Overview
   - `anon` and publishable keys
   - `service_role` and secret keys
   - Known limitations and compatibility differences
   - ... and 52 more sections
40. [Concepts](./40-concepts.md)
   - Concepts
   - What are embeddings?
   - Human language
   - How do embeddings work?
   - Using embeddings
   - ... and 87 more sections
41. [IVFFlat indexes](./41-ivfflat-indexes.md)
   - IVFFlat indexes
   - Choosing an index
   - Usage
   - How does IVFFlat work?
   - When should you create IVFFlat indexes?
   - ... and 106 more sections


---

[← Back to Supabase README](../README.md)
