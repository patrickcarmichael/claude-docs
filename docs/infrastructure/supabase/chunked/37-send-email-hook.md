**Navigation:** [← Previous](./36-error-codes.md) | [Index](./index.md) | [Next →](./38-supabase-auth-with-the-nextjs-app-router.md)

# Send Email Hook

Use a custom email provider to send authentication messages

The Send Email Hook runs before an email is sent and allows for flexibility around email sending. You can use this hook to configure a back-up email provider or add internationalization to your emails.



## Email sending behavior

Email sending depends on two settings: Email Provider and Auth Hook status.

| Email Provider | Auth Hook | Result                                                               |
| -------------- | --------- | -------------------------------------------------------------------- |
| Enabled        | Enabled   | Auth Hook handles email sending (SMTP not used)                      |
| Enabled        | Disabled  | SMTP handles email sending (custom if configured, default otherwise) |
| Disabled       | Enabled   | Email Signups Disabled                                               |
| Disabled       | Disabled  | Email Signups Disabled                                               |



## Email change behavior and token hash mapping

When `email_action_type` is `email_change`, the hook payload can include one or two OTPs and their hashes. This depends on your [Secure Email Change](/dashboard/project/_/auth/providers?provider=Email) setting.

*   Secure Email Change enabled: two OTPs are generated, one for the current email (`user.email`) and one for the new email (`user.email_new`). You must send two emails.
*   Secure Email Change disabled: only one OTP is generated for the new email. You send a single email.

<Admonition type="note">
  Important quirk (backward compatibility):

  *   `email_data.token_hash_new` = Hash(`user.email`, `email_data.token`)
  *   `email_data.token_hash` = Hash(`user.email_new`, `email_data.token_new`)

  This naming is historical and kept for backward compatibility. Do not assume that the `_new` suffix refers to the new email.
</Admonition>


### What to send

If both `token_hash` and `token_hash_new` are present, send two messages:

*   To the current email (`user.email`): use `token` with `token_hash_new`.
*   To the new email (`user.email_new`): use `token_new` with `token_hash`.

If only one token/hash pair is present, send a single email. In non-secure mode, this is typically the new email OTP. Use `token` with `token_hash` or `token_new` with `token_hash`, depending on which fields are present in the payload.

**Inputs**

| Field   | Type                                              | Description                                                                        |
| ------- | ------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `user`  | [`User`](/docs/guides/auth/users#the-user-object) | The user attempting to sign in.                                                    |
| `email` | `object`                                          | Metadata specific to the email sending process. Includes the OTP and `token_hash`. |

<Tabs scrollable size="small" type="underlined">
  <TabPanel id="send-email-json" label="JSON">
    ```json
    {
      "user": {
        "id": "8484b834-f29e-4af2-bf42-80644d154f76",
        "aud": "authenticated",
        "role": "authenticated",
        "email": "valid.email@supabase.io",
        "phone": "",
        "app_metadata": {
          "provider": "email",
          "providers": ["email"]
        },
        "user_metadata": {
          "email": "valid.email@supabase.io",
          "email_verified": false,
          "phone_verified": false,
          "sub": "8484b834-f29e-4af2-bf42-80644d154f76"
        },
        "identities": [
          {
            "identity_id": "bc26d70b-517d-4826-bce4-413a5ff257e7",
            "id": "8484b834-f29e-4af2-bf42-80644d154f76",
            "user_id": "8484b834-f29e-4af2-bf42-80644d154f76",
            "identity_data": {
              "email": "valid.email@supabase.io",
              "email_verified": false,
              "phone_verified": false,
              "sub": "8484b834-f29e-4af2-bf42-80644d154f76"
            },
            "provider": "email",
            "last_sign_in_at": "2024-05-14T12:56:33.824231484Z",
            "created_at": "2024-05-14T12:56:33.824261Z",
            "updated_at": "2024-05-14T12:56:33.824261Z",
            "email": "valid.email@supabase.io"
          }
        ],
        "created_at": "2024-05-14T12:56:33.821567Z",
        "updated_at": "2024-05-14T12:56:33.825595Z",
        "is_anonymous": false
      },
      "email_data": {
        "token": "305805",
        "token_hash": "7d5b7b1964cf5d388340a7f04f1dbb5eeb6c7b52ef8270e1737a58d0",
        "redirect_to": "http://localhost:3000/",
        "email_action_type": "signup",
        "site_url": "http://localhost:9999",
        "token_new": "",
        "token_hash_new": ""
      }
    }
    ```
  </TabPanel>

  <TabPanel id="send-email-json-schema" label="JSON Schema">
    ```json
    {
      "type": "object",
      "properties": {
        "user": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "x-faker": "random.uuid"
            },
            "aud": {
              "type": "string",
              "enum": ["authenticated"]
            },
            "role": {
              "type": "string",
              "enum": ["anon", "authenticated"]
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
              "properties": {
                "provider": {
                  "type": "string",
                  "enum": ["email"]
                },
                "providers": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "enum": ["email"]
                  },
                  "minItems": 1,
                  "maxItems": 1
                }
              }
            },
            "user_metadata": {
              "type": "object",
              "properties": {
                "email": {
                  "type": "string",
                  "x-faker": "internet.email"
                },
                "email_verified": {
                  "type": "boolean",
                  "x-faker": "random.boolean"
                },
                "phone_verified": {
                  "type": "boolean",
                  "x-faker": "random.boolean"
                },
                "sub": {
                  "type": "string",
                  "x-faker": "random.uuid"
                }
              }
            },
            "identities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "identity_id": {
                    "type": "string",
                    "x-faker": "random.uuid"
                  },
                  "id": {
                    "type": "string",
                    "x-faker": "random.uuid"
                  },
                  "user_id": {
                    "type": "string",
                    "x-faker": "random.uuid"
                  },
                  "identity_data": {
                    "type": "object",
                    "properties": {
                      "email": {
                        "type": "string",
                        "x-faker": "internet.email"
                      },
                      "email_verified": {
                        "type": "boolean",
                        "x-faker": "random.boolean"
                      },
                      "phone_verified": {
                        "type": "boolean",
                        "x-faker": "random.boolean"
                      },
                      "sub": {
                        "type": "string",
                        "x-faker": "random.uuid"
                      }
                    }
                  },
                  "provider": {
                    "type": "string",
                    "enum": ["email"]
                  },
                  "last_sign_in_at": {
                    "type": "string",
                    "format": "date-time",
                    "x-faker": "date.recent"
                  },
                  "created_at": {
                    "type": "string",
                    "format": "date-time",
                    "x-faker": "date.recent"
                  },
                  "updated_at": {
                    "type": "string",
                    "format": "date-time",
                    "x-faker": "date.recent"
                  },
                  "email": {
                    "type": "string",
                    "x-faker": "internet.email"
                  }
                },
                "required": [
                  "identity_id",
                  "id",
                  "user_id",
                  "identity_data",
                  "provider",
                  "last_sign_in_at",
                  "created_at",
                  "updated_at",
                  "email"
                ]
              }
            },
            "created_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "updated_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "is_anonymous": {
              "type": "boolean",
              "x-faker": "random.boolean"
            }
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
        },
        "email_data": {
          "type": "object",
          "properties": {
            "token": {
              "type": "string",
              "pattern": "^[0-9]{6}$",
              "x-faker": {
                "fake": "{{helpers.replaceSymbols('######')}}"
              }
            },
            "token_hash": {
              "type": "string",
              "minLength": 16,
              "maxLength": 30,
              "x-faker": {
                "fake": "{{random.alphaNumeric(30)}}"
              }
            },
            "redirect_to": {
              "type": "string",
              "x-faker": "internet.url"
            },
            "email_action_type": {
              "type": "string",
              "enum": [
                "signup",
                "invite",
                "magiclink",
                "recovery",
                "email_change",
                "email",
                "reauthentication"
              ]
            },
            "site_url": {
              "type": "string",
              "x-faker": "internet.url"
            },
            "token_new": {
              "type": "string",
              "minLength": 16,
              "maxLength": 30,
              "x-faker": {
                "fake": "{{random.alphaNumeric(30)}}"
              }
            },
            "token_hash_new": {
              "type": "string",
              "minLength": 16,
              "maxLength": 30,
              "x-faker": {
                "fake": "{{random.alphaNumeric(30)}}"
              }
            }
          },
          "required": [
            "token",
            "token_hash",
            "redirect_to",
            "email_action_type",
            "site_url",
            "token_new",
            "token_hash_new"
          ]
        }
      },
      "required": ["user", "email_data"]
    }
    ```
  </TabPanel>
</Tabs>

**Outputs**

*   No outputs are required. An empty response with a status code of 200 is taken as a successful response.

<Tabs scrollable size="small" type="underlined" defaultActiveId="http" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="sql-queue-email-messages">
      <TabPanel id="sql-queue-email-messages" label="Queue Email Messages">
        Your company uses a worker to manage all emails related jobs. For performance reasons, the messaging system sends emails in batches via a job queue. Instead of sending a message immediately, messages are queued and sent in periodic intervals via `pg_cron`.

        Create a table to store jobs

        ```sql
        create table job_queue (
          job_id uuid primary key default gen_random_uuid(),
          job_data jsonb not null,
          created_at timestamp default now(),
          status text default 'pending',
          priority int default 0,
          retry_count int default 0,
          max_retries int default 2,
          scheduled_at timestamp default now()
        );
        ```

        Create the hook

        ```sql
        create or replace function send_email(event jsonb) returns jsonb as $$
        declare
            job_data jsonb;
            scheduled_time timestamp;
            priority int;
        begin
            -- Extract email details from the event JSON
            job_data := jsonb_build_object(
                'email_action_type', event->'email_data'->>'email_action_type',
                'token_hash', event->'email_data'->>'token_hash',
                'token', event->'email_data'->>'token',
                'email', event->'user'->>'email'
            );

            -- Calculate the nearest 5-minute window for scheduled_time
            scheduled_time := date_trunc('minute', now()) + interval '5 minute' * floor(extract('epoch' from (now() - date_trunc('minute', now())) / 60) / 5);

            -- Assign priority dynamically (example logic: higher priority for earlier scheduled time)
            priority := extract('epoch' from (scheduled_time - now()))::int;

            insert into public.job_queue (job_data, priority, scheduled_at, max_retries)
            values (job_data, priority, scheduled_time, 2);

            return '{}'::jsonb;
        end;
        $$ language plpgsql;

        grant all
          on table public.job_queue
          to supabase_auth_admin;

        revoke all
          on table public.job_queue
          from authenticated, anon;
        ```

        Create a function to periodically run and dequeue all jobs

        ```sql
        create or replace function dequeue_and_run_jobs() returns void as $$
        declare
            job record;
        begin
            for job in
                select * from job_queue
                where status = 'pending'
                  and scheduled_at <= now()
                order by priority desc, created_at
                for update skip locked
            loop
                begin
                    -- add job processing logic here.
                    -- for demonstration, we'll just update the job status to 'completed'.
                    update job_queue
                    set status = 'completed'
                    where job_id = job.job_id;

                exception when others then
                    -- handle job failure and retry logic
                    if job.retry_count < job.max_retries then
                        update job_queue
                        set retry_count = retry_count + 1,
                            scheduled_at = now() + interval '1 minute'  -- delay retry by 1 minute
                        where job_id = job.job_id;
                    else
                        update job_queue
                        set status = 'failed'
                        where job_id = job.job_id;
                    end if;
                end;
            end loop;
        end;
        $$ language plpgsql;

        grant execute
          on function public.dequeue_and_run_jobs
          to supabase_auth_admin;

        revoke execute
          on function public.dequeue_and_run_jobs
          from authenticated, anon;
        ```

        Configure `pg_cron` to run the job on an interval. You can use a tool like [crontab.guru](https://crontab.guru/) to check that your job is running on an appropriate schedule. Ensure that `pg_cron` is enabled under `Database > Extensions`

        ```sql
        select
          cron.schedule(
            '* * * * *', -- this cron expression means every minute.
            'select dequeue_and_run_jobs();'
          );
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="http-send-email-with-resend">
      <TabPanel id="http-send-email-with-resend" label="Use Resend as an email provider">
        You can configure [Resend](https://resend.com/) as the custom email provider through the "Send Email" hook. This allows you to take advantage of Resend's developer-friendly APIs to send emails and leverage [React Email](https://react.email/) for managing your email templates. For a more advanced React Email tutorial, refer to [this guide](/docs/guides/functions/examples/auth-send-email-hook-react-email-resend).

        If you want to send emails through the Supabase Resend integration, which uses Resend's SMTP server, check out [this integration](/partners/integrations/resend) instead.

        Create a `.env` file with the following environment variables:

        ```ini
        RESEND_API_KEY="your_resend_api_key"
        SEND_EMAIL_HOOK_SECRET="v1,whsec_<base64_secret>"
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
        supabase functions new send-email
        ```

        Add the following code to your edge function:

        ```javascript
        import { Webhook } from "https://esm.sh/standardwebhooks@1.0.0";
        import { Resend } from "npm:resend";

        const resend = new Resend(Deno.env.get("RESEND_API_KEY") as string);
        const hookSecret = (Deno.env.get("SEND_EMAIL_HOOK_SECRET") as string).replace("v1,whsec_", "");

        Deno.serve(async (req) => {
          if (req.method !== "POST") {
            return new Response("not allowed", { status: 400 });
          }

          const payload = await req.text();
          const headers = Object.fromEntries(req.headers);
          const wh = new Webhook(hookSecret);
          try {
            const { user, email_data } = wh.verify(payload, headers) as {
              user: {
                email: string;
              };
              email_data: {
                token: string;
                token_hash: string;
                redirect_to: string;
                email_action_type: string;
                site_url: string;
                token_new: string;
                token_hash_new: string;
              };
            };

            const { error } = await resend.emails.send({
              from: "welcome <onboarding@example.com>",
              to: [user.email],
              subject: "Welcome to my site!",
              text: `Confirm you signup with this code: ${email_data.token}`,
            });
            if (error) {
              throw error;
            }
          } catch (error) {
            return new Response(
              JSON.stringify({
                error: {
                  http_code: error.code,
                  message: error.message,
                },
              }),
              {
                status: 401,
                headers: { "Content-Type": "application/json" },
              },
            );
          }

          const responseHeaders = new Headers();
          responseHeaders.set("Content-Type", "application/json");
          return new Response(JSON.stringify({}), {
            status: 200,
            headers: responseHeaders,
          });
        });
        ```

        Deploy your edge function and [configure it as a hook](/dashboard/project/_/auth/hooks):

        ```bash
        supabase functions deploy send-email --no-verify-jwt
        ```
      </TabPanel>

      <TabPanel id="http-internationalization-for-emails" label="Add Internationalization for Email Templates">
        Your company is expanding to France and Spain. As part of expansion efforts, the company would like to deliver internationalized email templates to best support local users in their native language. Ensure that you have configured `POSTMARK_SERVER_TOKEN` and `SEND_EMAIL_HOOK_SECRET` in your `.env` file.

        ```javascript
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'
        import { readAll } from 'https://deno.land/std/io/read_all.ts'

        const postmarkEndpoint = 'https://api.postmarkapp.com/email'
        // Replace this with your email
        const FROM_EMAIL = 'myemail@gmail.com'
        const PROJECT_REF = '<your-project-ref>'

        // Email Subjects
        const subjects = {
          en: {
            signup: 'Confirm Your Email',
            recovery: 'Reset Your Password',
            invite: 'You have been invited',
            magiclink: 'Your Magic Link',
            email_change: 'Confirm Email Change',
            email_change_new: 'Confirm New Email Address',
            reauthentication: 'Confirm Reauthentication',
          },
          es: {
            signup: 'Confirma tu correo electrónico',
            recovery: 'Restablece tu contraseña',
            invite: 'Has sido invitado',
            magiclink: 'Tu enlace mágico',
            email_change: 'Confirma el cambio de correo electrónico',
            email_change_new: 'Confirma la Nueva Dirección de Correo',
            reauthentication: 'Confirma la reautenticación',
          },
          fr: {
            signup: 'Confirmez votre adresse e-mail',
            recovery: 'Réinitialisez votre mot de passe',
            invite: 'Vous avez été invité',
            magiclink: 'Votre Lien Magique',
            email_change: 'Confirmez le changement d’adresse e-mail',
            email_change_new: 'Confirmez la nouvelle adresse e-mail',
            reauthentication: 'Confirmez la réauthentification',
          },
        }

        // HTML Body
        const templates = {
          en: {
            signup: `<h2>Confirm your email</h2><p>Follow this link to confirm your email:</p><p><a href="{{confirmation_url}}">Confirm your email address</a></p><p>Alternatively, enter the code: {{token}}</p>`,
            recovery: `<h2>Reset password</h2><p>Follow this link to reset the password for your user:</p><p><a href="{{confirmation_url}}">Reset password</a></p><p>Alternatively, enter the code: {{token}}</p>`,
            invite: `<h2>You have been invited</h2><p>You have been invited to create a user on {{site_url}}. Follow this link to accept the invite:</p><p><a href="{{confirmation_url}}">Accept the invite</a></p><p>Alternatively, enter the code: {{token}}</p>`,
            magiclink: `<h2>Magic Link</h2><p>Follow this link to login:</p><p><a href="{{confirmation_url}}">Log In</a></p><p>Alternatively, enter the code: {{token}}</p>`,
            email_change: `<h2>Confirm email address change</h2><p>Follow this link to confirm the update of your email address from {{old_email}} to {{new_email}}:</p><p><a href="{{confirmation_url}}">Change email address</a></p><p>Alternatively, enter the codes: {{token}} and {{new_token}}</p>`,
            email_change_new: `<h2>Confirm New Email Address</h2><p>Follow this link to confirm your new email address:</p><p><a href="{{confirmation_url}}">Confirm new email address</a></p><p>Alternatively, enter the code: {{new_token}}</p>`,
            reauthentication: `<h2>Confirm reauthentication</h2><p>Enter the code: {{token}}</p>`,
          },
          es: {
            signup: `<h2>Confirma tu correo electrónico</h2><p>Sigue este enlace para confirmar tu correo electrónico:</p><p><a href="{{confirmation_url}}">Confirma tu correo electrónico</a></p><p>Alternativamente, ingresa el código: {{token}}</p>`,
            recovery: `<h2>Restablece tu contraseña</h2><p>Sigue este enlace para restablecer la contraseña de tu usuario:</p><p><a href="{{confirmation_url}}">Restablece tu contraseña</a></p><p>Alternativamente, ingresa el código: {{token}}</p>`,
            invite: `<h2>Has sido invitado</h2><p>Has sido invitado para crear un usuario en {{site_url}}. Sigue este enlace para aceptar la invitación:</p><p><a href="{{confirmation_url}}">Aceptar la invitación</a></p><p>Alternativamente, ingresa el código: {{token}}</p>`,
            magiclink: `<h2>Tu enlace mágico</h2><p>Sigue este enlace para iniciar sesión:</p><p><a href="{{confirmation_url}}">Iniciar sesión</a></p><p>Alternativamente, ingresa el código: {{token}}</p>`,
            email_change: `<h2>Confirma el cambio de correo electrónico</h2><p>Sigue este enlace para confirmar la actualización de tu correo electrónico de {{old_email}} a {{new_email}}:</p><p><a href="{{confirmation_url}}">Cambiar correo electrónico</a></p><p>Alternativamente, ingresa los códigos: {{token}} y {{new_token}}</p>`,
            email_change_new: `<h2>Confirma la Nueva Dirección de Correo</h2><p>Sigue este enlace para confirmar tu nueva dirección de correo electrónico:</p><p><a href="{{confirmation_url}}">Confirma la nueva dirección de correo</a></p><p>Alternativamente, ingresa el código: {{new_token}}</p>`,
            reauthentication: `<h2>Confirma la reautenticación</h2><p>Ingresa el código: {{token}}</p>`,
          },
          fr: {
            signup: `<h2>Confirmez votre adresse e-mail</h2><p>Suivez ce lien pour confirmer votre adresse e-mail :</p><p><a href="{{confirmation_url}}">Confirmez votre adresse e-mail</a></p><p>Vous pouvez aussi saisir le code : {{token}}</p>`,
            recovery: `<h2>Réinitialisez votre mot de passe</h2><p>Suivez ce lien pour réinitialiser votre mot de passe :</p><p><a href="{{confirmation_url}}">Réinitialisez votre mot de passe</a></p><p>Vous pouvez aussi saisir le code : {{token}}</p>`,
            invite: `<h2>Vous avez été invité</h2><p>Vous avez été invité à créer un utilisateur sur {{site_url}}. Suivez ce lien pour accepter l'invitation :</p><p><a href="{{confirmation_url}}">Acceptez l'invitation</a></p><p>Vous pouvez aussi saisir le code : {{token}}</p>`,
            magiclink: `<h2>Votre Lien Magique</h2><p>Suivez ce lien pour vous connecter :</p><p><a href="{{confirmation_url}}">Connectez-vous</a></p><p>Vous pouvez aussi saisir le code : {{token}}</p>`,
            email_change: `<h2>Confirmez le changement d’adresse e-mail</h2><p>Suivez ce lien pour confirmer la mise à jour de votre adresse e-mail de {{old_email}} à {{new_email}} :</p><p><a href="{{confirmation_url}}">Changez d’adresse e-mail</a></p><p>Vous pouvez aussi saisir les codes : {{token}} et {{new_token}}</p>`,
            email_change_new: `<h2>Confirmez la nouvelle adresse e-mail</h2><p>Suivez ce lien pour confirmer votre nouvelle adresse e-mail :</p><p><a href="{{confirmation_url}}">Confirmez la nouvelle adresse e-mail</a></p><p>Vous pouvez aussi saisir le code : {{new_token}}</p>`,
            reauthentication: `<h2>Confirmez la réauthentification</h2><p>Saisissez le code : {{token}}</p>`,
          },
        }

        function generateConfirmationURL(email_data) {
          const baseUrl = `https://${PROJECT_REF}.supabase.co/auth/v1/verify`
          const params = new URLSearchParams({
            token: email_data.token_hash,
            type: email_data.email_action_type,
            redirect_to: email_data.redirect_to,
          })

          return `${baseUrl}?${params.toString()}`
        }

        Deno.serve(async (req) => {
          const payload = await req.text()
          const serverToken = Deno.env.get('POSTMARK_SERVER_TOKEN')
          const headers = Object.fromEntries(req.headers)
          const base64_secret = Deno.env.get('SEND_EMAIL_HOOK_SECRET').replace('v1,whsec_', '')
          const wh = new Webhook(base64_secret)
          const { user, email_data } = wh.verify(payload, headers)

          const language = (user.user_metadata && user.user_metadata.i18n) || 'en'
          const subject = subjects[language][email_data.email_action_type] || 'Notification'

          let template = templates[language][email_data.email_action_type]
          const confirmation_url = generateConfirmationURL(email_data)
          let htmlBody = template
            .replace('{{confirmation_url}}', confirmation_url)
            .replace('{{token}}', email_data.token || '')
            .replace('{{new_token}}', email_data.new_token || '')
            .replace('{{site_url}}', email_data.site_url || '')
            .replace('{{old_email}}', email_data.email || '')
            .replace('{{new_email}}', email_data.new_email || '')

          const requestOptions = {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Accept: 'application/json',
              'X-Postmark-Server-Token': serverToken,
            },
            body: JSON.stringify({
              From: FROM_EMAIL,
              To: user.email,
              Subject: subject,
              HtmlBody: htmlBody,
            }),
          }

          try {
            const response = await fetch(postmarkEndpoint, requestOptions)
            if (!response.ok) {
              const errorData = await response.json()
              throw new Error(`Failed to send email: ${errorData.Message}`)
            }
            return new Response(
              JSON.stringify({
                message: 'Email sent successfully.',
              }),
              {
                headers: {
                  'Content-Type': 'application/json',
                },
              }
            )
          } catch (error) {
            return new Response(
              JSON.stringify({
                error: `Failed to process the request: ${error.message}`,
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

      {/* <TabPanel id="http-backup-email-provider" label="Add Backup Email Provider">
            Your company is rapidly growing and depends heavily on email signups. You'd like to configure a backup email provider in case the email provider runs out of credits during your new product launch. Postmark and Sengrid are used as examples but in practice you can use any email provider.
            Ensure that you have configured `POSTMARK_SERVER_TOKEN`, `SENDGRID_API_KEY` and `SEND_EMAIL_HOOK_SECRET` in your `.env` file.

            ```javascript
            import {
                Webhook
            } from "https://esm.sh/standardwebhooks@1.0.0";
            import {
                readAll
            } from "https://deno.land/std/io/read_all.ts";

            const postmarkEndpoint = 'https://api.postmarkapp.com/email';
            const sendGridEndpoint = 'https://api.sendgrid.com/v3/mail/send';
            const FROM_EMAIL = 'myemail@gmail.com'

            // Email Subjects
            const subjects = {
                signup: 'Confirm Your Email',
                recovery: 'Reset Your Password',
                invite: 'You have been invited',
                magiclink: 'Your Magic Link',
                email_change: 'Confirm Email Change',
                email_change_new: 'Confirm New Email Address',
                reauthentication: 'Confirm Reauthentication'
            };

            // HTML Body
            const templates = {
                signup: `<h2>Confirm your email</h2><p>Follow this link to confirm your email:</p><p><a href="{{confirmation_url}}">Confirm your email address</a></p><p>Alternatively, enter the code: {{token}}</p>`,
                recovery: `<h2>Reset password</h2><p>Follow this link to reset the password for your user:</p><p><a href="{{confirmation_url}}">Reset password</a></p><p>Alternatively, enter the code: {{token}}</p>`,
                invite: `<h2>You have been invited</h2><p>You have been invited to create a user on {{site_url}}. Follow this link to accept the invite:</p><p><a href="{{confirmation_url}}">Accept the invite</a></p><p>Alternatively, enter the code: {{token}}</p>`,
                magiclink: `<h2>Magic Link</h2><p>Follow this link to login:</p><p><a href="{{confirmation_url}}">Log In</a></p><p>Alternatively, enter the code: {{token}}</p>`,
                email_change: `<h2>Confirm email address change</h2><p>Follow this link to confirm the update of your email address from {{old_email}} to {{new_email}}:</p><p><a href="{{confirmation_url}}">Change email address</a></p><p>Alternatively, enter the codes: {{token}} and {{new_token}}</p>`,
                email_change_new: `<h2>Confirm New Email Address</h2><p>Follow this link to confirm your new email address:</p><p><a href="{{confirmation_url}}">Confirm new email address</a></p><p>Alternatively, enter the code: {{new_token}}</p>`,
                reauthentication: `<h2>Confirm reauthentication</h2><p>Enter the code: {{token}}</p>`
            };

            function generateConfirmationURL(email_data) {
               // TODO: replace the ref with your project ref
               return `https://<ref>.supabase.co/auth/v1/verify?token=${email_data.token_hash}&type=${email_data.email_action_type}&redirect_to=${email_data.redirect_to}`
            }

            async function sendEmailWithPostmark(user: any, email_data: any, serverToken: string): Promise<Response> {
                const subject = subjects[email_data.email_action_type] || 'Notification';
                const confirmation_url = generateConfirmationURL(email_data)
                let template = templates[email_data.email_action_type];
                let htmlBody = template.replace('{{confirmation_url}}', confirmation_url)
                    .replace('{{token}}', email_data.token || '')
                    .replace('{{new_token}}', email_data.new_token || '')
                    .replace('{{site_url}}', email_data.site_url || '')
                    .replace('{{old_email}}', email_data.email || '')
                    .replace('{{new_email}}', email_data.new_email || '');

                const requestOptions = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-Postmark-Server-Token': serverToken
                    },
                    body: JSON.stringify({
                        From: FROM_EMAIL,
                        To: user.email,
                        Subject: subject,
                        HtmlBody: htmlBody
                    })
                };

                return await fetch(postmarkEndpoint, requestOptions);
            }

            async function sendEmailWithSendGrid(user: any, email_data: any, apiKey: string): Promise<Response> {
                const subject = subjects[email_data.email_action_type] || 'Notification';
                let template = templates[email_data.email_action_type];
                cont confirmation_url = generateConfirmationURL(email_data)
                let htmlBody = template.replace('{{confirmation_url}}', confirmation_url)
                    .replace('{{token}}', email_data.token || '')
                    .replace('{{new_token}}', email_data.new_token || '')
                    .replace('{{site_url}}', email_data.site_url || '')
                    .replace('{{old_email}}', email_data.email || '')
                    .replace('{{new_email}}', email_data.new_email || '');

                const requestOptions = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${apiKey}`
                    },
                    body: JSON.stringify({
                        personalizations: [{
                            to: [{
                                email: user.email
                            }],
                            subject: subject
                        }],
                        from: {
                            email: FROM_EMAIL
                        },
                        content: [{
                            type: "text/html",
                            value: htmlBody
                        }]
                    })
                };

                return await fetch(sendGridEndpoint, requestOptions);
            }

            Deno.serve(async (req) => {
                const payload = await req.text();
                const postmarkServerToken = Deno.env.get("POSTMARK_SERVER_TOKEN");
                const sendGridApiKey = Deno.env.get("SENDGRID_API_KEY");
                const headers = Object.fromEntries(req.headers);
                const base64_secret = Deno.env.get('SEND_EMAIL_HOOK_SECRET').replace('v1,whsec_', '');
                const wh = new Webhook(base64_secret);
                const {
                    user,
                    email_data
                } = wh.verify(payload, headers);

                try {
                    // Try sending email using Postmark
                    let response = await sendEmailWithPostmark(user, email_data, postmarkServerToken!);

                    if (!response.ok) {
                        // If Postmark fails, try SendGrid
                        console.error(`Primary email send failed: ${await response.text()}`);
                        response = await sendEmailWithSendGrid(user, email_data, sendGridApiKey!);

                        if (!response.ok) {
                            const errorData = await response.json();
                            throw new Error(`Failed to send email via backup: ${errorData.errors[0].message}`);
                        }
                    }

                    return new Response(JSON.stringify({
                        message: "Email sent successfully."
                    }), {
                        headers: {
                            "Content-Type": "application/json"
                        }
                    });
                } catch (error) {
                    return new Response(JSON.stringify({
                        error: `Failed to process the request: ${error.message}`
                    }), {
                        status: 500,
                        headers: {
                            "Content-Type": "application/json"
                        }
                    });
                }
            });
            ```

            </TabPanel> */}
    </Tabs>
  </TabPanel>
</Tabs>



# Send SMS Hook

Use a custom SMS provider to send authentication messages

Runs before a message is sent. Use the hook to:

*   Use a regional SMS Provider
*   Use alternate messaging channels such as WhatsApp
*   Adjust the message body to include platform specific fields such as the [`AppHash`](https://developers.google.com/identity/sms-retriever/overview)

**Inputs**

| Field  | Type                                              | Description                                                     |
| ------ | ------------------------------------------------- | --------------------------------------------------------------- |
| `user` | [`User`](/docs/guides/auth/users#the-user-object) | The user attempting to sign in.                                 |
| `sms`  | `object`                                          | Metadata specific to the SMS sending process. Includes the OTP. |

<Tabs scrollable size="small" type="underlined">
  <TabPanel id="send-sms-json" label="JSON">
    ```json
    {
      "user": {
        "id": "6481a5c1-3d37-4a56-9f6a-bee08c554965",
        "aud": "authenticated",
        "role": "authenticated",
        "email": "",
        "phone": "+1333363128",
        "phone_confirmed_at": "2024-05-13T11:52:48.157306Z",
        "confirmation_sent_at": "2024-05-14T12:31:52.824573Z",
        "confirmed_at": "2024-05-13T11:52:48.157306Z",
        "phone_change_sent_at": "2024-05-13T11:47:02.183064Z",
        "last_sign_in_at": "2024-05-13T11:52:48.162518Z",
        "app_metadata": {
          "provider": "phone",
          "providers": ["phone"]
        },
        "user_metadata": {},
        "identities": [
          {
            "identity_id": "3be5e552-65aa-41d9-9db9-2a502f845459",
            "id": "6481a5c1-3d37-4a56-9f6a-bee08c554965",
            "user_id": "6481a5c1-3d37-4a56-9f6a-bee08c554965",
            "identity_data": {
              "email_verified": false,
              "phone": "+1612341244428",
              "phone_verified": true,
              "sub": "6481a5c1-3d37-4a56-9f6a-bee08c554965"
            },
            "provider": "phone",
            "last_sign_in_at": "2024-05-13T11:52:48.155562Z",
            "created_at": "2024-05-13T11:52:48.155599Z",
            "updated_at": "2024-05-13T11:52:48.159391Z"
          }
        ],
        "created_at": "2024-05-13T11:45:33.7738Z",
        "updated_at": "2024-05-14T12:31:52.82475Z",
        "is_anonymous": false
      },
      "sms": {
        "otp": "561166"
      }
    }
    ```
  </TabPanel>

  <TabPanel id="send-sms-json-schema" label="JSON Schema">
    ```json
    {
      "type": "object",
      "properties": {
        "user": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "x-faker": "random.uuid"
            },
            "aud": {
              "type": "string",
              "enum": ["authenticated"]
            },
            "role": {
              "type": "string",
              "enum": ["anon", "authenticated"]
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
            "phone_confirmed_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "confirmation_sent_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "confirmed_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "phone_change_sent_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "last_sign_in_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "app_metadata": {
              "type": "object",
              "properties": {
                "provider": {
                  "type": "string",
                  "enum": ["phone"]
                },
                "providers": {
                  "type": "array",
                  "items": {
                    "type": "string",
                    "enum": ["phone"]
                  }
                }
              }
            },
            "user_metadata": {
              "type": "object",
              "x-faker": "random.objectElement"
            },
            "identities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "identity_id": {
                    "type": "string",
                    "x-faker": "random.uuid"
                  },
                  "id": {
                    "type": "string",
                    "x-faker": "random.uuid"
                  },
                  "user_id": {
                    "type": "string",
                    "x-faker": "random.uuid"
                  },
                  "identity_data": {
                    "type": "object",
                    "properties": {
                      "email_verified": {
                        "type": "boolean",
                        "x-faker": "random.boolean"
                      },
                      "phone": {
                        "type": "string",
                        "x-faker": {
                          "fake": "{{phone.phoneNumber('+1##########')}}"
                        }
                      },
                      "phone_verified": {
                        "type": "boolean",
                        "x-faker": "random.boolean"
                      },
                      "sub": {
                        "type": "string",
                        "x-faker": "random.uuid"
                      }
                    }
                  },
                  "provider": {
                    "type": "string",
                    "enum": ["phone", "email", "google"]
                  },
                  "last_sign_in_at": {
                    "type": "string",
                    "format": "date-time",
                    "x-faker": "date.recent"
                  },
                  "created_at": {
                    "type": "string",
                    "format": "date-time",
                    "x-faker": "date.recent"
                  },
                  "updated_at": {
                    "type": "string",
                    "format": "date-time",
                    "x-faker": "date.recent"
                  }
                },
                "required": [
                  "identity_id",
                  "id",
                  "user_id",
                  "identity_data",
                  "provider",
                  "last_sign_in_at",
                  "created_at",
                  "updated_at"
                ]
              }
            },
            "created_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "updated_at": {
              "type": "string",
              "format": "date-time",
              "x-faker": "date.recent"
            },
            "is_anonymous": {
              "type": "boolean",
              "x-faker": "random.boolean"
            }
          },
          "required": [
            "id",
            "aud",
            "role",
            "email",
            "phone",
            "phone_confirmed_at",
            "confirmation_sent_at",
            "confirmed_at",
            "phone_change_sent_at",
            "last_sign_in_at",
            "app_metadata",
            "user_metadata",
            "identities",
            "created_at",
            "updated_at",
            "is_anonymous"
          ]
        },
        "sms": {
          "type": "object",
          "properties": {
            "otp": {
              "type": "string",
              "pattern": "^[0-9]{6}$",
              "x-faker": {
                "fake": "{{helpers.replaceSymbols(######)}}"
              }
            }
          },
          "required": ["otp"]
        }
      },
      "required": ["user", "sms"]
    }
    ```
  </TabPanel>
</Tabs>

**Outputs**

*   No outputs are required. An empty response with a status code of 200 is taken as a successful response.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="sql-send-message-via-job-queue">
      <TabPanel id="sql-send-message-via-job-queue" label="Queue SMS Messages">
        Your company uses a worker to manage all messaging related jobs. For performance reasons, the messaging system sends messages in intervals via a job queue. Instead of sending a message immediately, messages are queued and sent in periodic intervals via `pg_cron`.

        Create a table to store jobs

        ```sql
        create table job_queue (
          job_id uuid primary key default gen_random_uuid(),
          job_data jsonb not null,
          created_at timestamp default now(),
          status text default 'pending',
          priority int default 0,
          retry_count int default 0,
          max_retries int default 2,
          scheduled_at timestamp default now()
        );
        ```

        Create the hook:

        ```sql
        create or replace function send_sms(event jsonb) returns void as $$
        declare
            job_data jsonb;
            scheduled_time timestamp;
            priority int;
        begin
            -- extract phone and otp from the event json
            job_data := jsonb_build_object(
                'phone', event->'user'->>'phone',
                'otp', event->'sms'->>'otp'
            );

            -- calculate the nearest 5-minute window for scheduled_time
            scheduled_time := date_trunc('minute', now()) + interval '5 minute' * floor(extract('epoch' from (now() - date_trunc('minute', now())) / 60) / 5);

            -- assign priority dynamically (example logic: higher priority for earlier scheduled time)
            priority := extract('epoch' from (scheduled_time - now()))::int;

            -- insert the job into the job_queue table
            insert into job_queue (job_data, priority, scheduled_at, max_retries)
            values (job_data, priority, scheduled_time, 2);
        end;
        $$ language plpgsql;

        grant all
          on table public.job_queue
          to supabase_auth_admin;

        revoke all
          on table public.job_queue
          from authenticated, anon;
        ```

        Create a function to periodically run and dequeue all jobs

        ```sql
        create or replace function dequeue_and_run_jobs() returns void as $$
        declare
            job record;
        begin
            for job in
                select * from job_queue
                where status = 'pending'
                  and scheduled_at <= now()
                order by priority desc, created_at
                for update skip locked
            loop
                begin
                    -- add job processing logic here.
                    -- for demonstration, we'll just update the job status to 'completed'.
                    update job_queue
                    set status = 'completed'
                    where job_id = job.job_id;

                exception when others then
                    -- handle job failure and retry logic
                    if job.retry_count < job.max_retries then
                        update job_queue
                        set retry_count = retry_count + 1,
                            scheduled_at = now() + interval '1 minute'  -- delay retry by 1 minute
                        where job_id = job.job_id;
                    else
                        update job_queue
                        set status = 'failed'
                        where job_id = job.job_id;
                    end if;
                end;
            end loop;
        end;
        $$ language plpgsql;

        grant execute
          on function public.dequeue_and_run_jobs
          to supabase_auth_admin;

        revoke execute
          on function public.dequeue_and_run_jobs
          from authenticated, anon;
        ```

        Configure `pg_cron` to run the job on an interval. You can use a tool like [crontab.guru](https://crontab.guru/) to check that your job is running on an appropriate schedule. Ensure that `pg_cron` is enabled under `Database > Extensions`

        ```sql
        select
          cron.schedule(
            '* * * * *', -- this cron expression means every minute.
            'select dequeue_and_run_jobs();'
          );
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="http-alternate-message-provider">
      <TabPanel id="http-alternate-message-provider" label="Alternate message provider">
        Your company would like to use an alternate message provider. Some examples of alternate message providers include [Msg91](https://msg91.com/) for India and [Africa's Talking](https://africastalking.com/). The example uses Twilio as it is widely available and does not require a regional number.

        ```javascript
        import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'
        import { readAll } from 'https://deno.land/std/io/read_all.ts'
        import { Twilio } from 'https://cdn.skypack.dev/twilio'
        import * as base64 from 'https://denopkg.com/chiefbiiko/base64/mod.ts'

        const accountSid: string | undefined = Deno.env.get('TWILIO_ACCOUNT_SID')
        const authToken: string | undefined = Deno.env.get('TWILIO_AUTH_TOKEN')
        const fromNumber: string = Deno.env.get('TWILIO_PHONE_NUMBER')

        const sendTextMessage = async (
          messageBody: string,
          accountSid: string | undefined,
          authToken: string | undefined,
          fromNumber: string,
          toNumber: string
        ): Promise<any> => {
          if (!accountSid || !authToken) {
            console.log('Your Twilio account credentials are missing. Please add them.')
            return
          }
          const url: string = `https://api.twilio.com/2010-04-01/Accounts/${accountSid}/Messages.json`

          const encodedCredentials: string = base64.fromUint8Array(
            new TextEncoder().encode(`${accountSid}:${authToken}`)
          )

          const body: URLSearchParams = new URLSearchParams({
            To: `+${toNumber}`,
            From: fromNumber,
            // Uncomment when testing with a fixed number
            Body: messageBody,
          })

          const response = await fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              Authorization: `Basic ${encodedCredentials}`,
            },
            body,
          })

          return response.json()
        }

        Deno.serve(async (req) => {
          const payload = await req.text()
          const base64_secret = Deno.env.get('SEND_SMS_HOOK_SECRET').replace('v1,whsec_', '')
          const headers = Object.fromEntries(req.headers)
          const wh = new Webhook(base64_secret)
          try {
            const { user, sms } = wh.verify(payload, headers)
            const messageBody = `Your OTP is: ${sms.otp}`
            const response = await sendTextMessage(
              messageBody,
              accountSid,
              authToken,
              fromNumber,
              user.phone
            )
            if (response.status !== 'queued') {
              return new Response(
                JSON.stringify({
                  error: {
                    http_code: response.code,
                    message: `Failed to send SMS: ${response.message}. More info: ${response.more_info}`,
                  },
                }),
                {
                  status: response.status,
                  headers: {
                    'Content-Type': 'application/json',
                  },
                }
              )
            }
            return new Response(
              JSON.stringify({}),
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
                error: {
                  http_code: 500,
                  message: `Failed to send sms: ${JSON.stringify(error)}`,
                }
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

      <TabPanel id="http-whatsapp-and-sms-messages" label="Use WhatsApp with SMS">
        Your company is expanding into Latin America and would like to use WhatsApp for higher deliverability. Write a hook to send WhatsApp messages to requests from the continent and SMS messages to all other numbers.

        ```javascript
        import { Webhook } from "https://esm.sh/standardwebhooks@1.0.0";
        import { readAll } from "https://deno.land/std/io/read_all.ts";
        import * as base64 from "https://denopkg.com/chiefbiiko/base64/mod.ts";

        const accountSid: string | undefined = Deno.env.get("TWILIO_ACCOUNT_SID");
        const authToken: string | undefined = Deno.env.get("TWILIO_AUTH_TOKEN");
        const fromNumber: string = Deno.env.get("TWILIO_WHATSAPP_NUMBER");
        const smsFromNumber: string = Deno.env.get("TWILIO_SMS_NUMBER");

        const latinAmericanCountryCodes = ['54', '55', '56', '57', '58', '501', '502', '503', '504', '505', '506', '507', '508', '509', '51', '52', '53', '591', '592', '593', '594', '595', '596', '597', '598', '599'];

        const sendMessage = async (
            messageBody: string,
            accountSid: string | undefined,
            authToken: string | undefined,
            fromNumber: string,
            toNumber: string,
            useWhatsApp: boolean,
        ): Promise < any > => {
            if (!accountSid || !authToken) {
                console.log("Your Twilio account credentials are missing. Please add them.");
                return;
            }
            const url: string = `https://api.twilio.com/2010-04-01/Accounts/${accountSid}/Messages.json`;

            const encodedCredentials: string = base64.fromUint8Array(
                new TextEncoder().encode(`${accountSid}:${authToken}`),
            );

            const body: URLSearchParams = new URLSearchParams({
                To: useWhatsApp ? `whatsapp:${toNumber}` : toNumber,
                From: useWhatsApp ? `whatsapp:${fromNumber}` : smsFromNumber,
                Body: messageBody,
            });

            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": `Basic ${encodedCredentials}`,
                },
                body,
            });

            return response.json();
        };

        Deno.serve(async (req) => {
            const payload = await req.text();
            const base64_secret = Deno.env.get("SEND_SMS_HOOK_SECRET").replace('v1,whsec_', '');
            const headers = Object.fromEntries(req.headers);
            const wh = new Webhook(base64_secret);
            try {
                const {
                    user,
                    sms
                } = wh.verify(payload, headers);
                const messageBody = `Your OTP is: ${sms.otp}`;
                const userPhoneNumber = user.phone;
                const countryCode = userPhoneNumber.substring(1, userPhoneNumber.indexOf(userPhoneNumber.match(/\d/)!));

                const useWhatsApp = latinAmericanCountryCodes.includes(countryCode);

                const response = await sendMessage(
                    messageBody,
                    accountSid,
                    authToken,
                    fromNumber,
                    userPhoneNumber,
                    useWhatsApp,
                );

                if (response.status !== "queued") {
                    return new Response(
                        JSON.stringify({
                            error: `Failed to send message, Error Code: ${response.code} ${response.message} ${response.more_info}`,
                        }), {
                            status: response.status,
                            headers: {
                                "Content-Type": "application/json",
                            },
                        },
                    );
                }
                return new Response(
                    JSON.stringify({
                        message: "Message sent successfully."
                    }), {
                        headers: {
                            "Content-Type": "application/json",
                        },
                    },
                );
            } catch (error) {
                return new Response(
                    JSON.stringify({
                        error: `Failed to process the request: ${error}`
                    }), {
                        status: 500,
                        headers: {
                            "Content-Type": "application/json",
                        },
                    },
                );
            }
        });
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



# Auth UI



<Admonition type="caution">
  As of 7th Feb 2024, [this repository](https://github.com/supabase-community/auth-ui) is no longer maintained by the Supabase Team. At the moment, the team does not have capacity to give the expected level of care to this repository. We may revisit Auth UI in the future but regrettably have to leave it on hold for now as we focus on other priorities such as improving the Server-Side Rendering (SSR) package and advanced Auth primitives.

  As an alternative you can use the [Supabase UI Library](/ui) which has auth ready blocks to use in your projects.
</Admonition>

Auth UI is a pre-built React component for authenticating users.
It supports custom themes and extensible styles to match your brand and aesthetic.

<video width="99%" muted playsInline controls={true}>
  <source src="https://supabase.com/images/blog/lw5-one-more/auth-ui-demo.mp4" type="video/mp4" />
</video>



## Set up Auth UI

Install the latest version of [supabase-js](/docs/reference/javascript) and the Auth UI package:

```bash
npm install @supabase/supabase-js @supabase/auth-ui-react @supabase/auth-ui-shared
```


### Import the Auth component

Pass `supabaseClient` from `@supabase/supabase-js` as a prop to the component.

```js /src/index.js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => <Auth supabaseClient={supabase} />
```

This renders the Auth component without any styling.
We recommend using one of the predefined themes to style the UI.
Import the theme you want to use and pass it to the `appearance.theme` prop.

```js
import { Auth } from '@supabase/auth-ui-react'
import {
  // Import predefined theme
  ThemeSupa,
} from '@supabase/auth-ui-shared'

const supabase = createClient(
  '<INSERT PROJECT URL>',
  '<INSERT PROJECT ANON API KEY>'
)

const App = () => (
  <Auth
    supabaseClient={supabase}
    {/* Apply predefined theme */}
    appearance={{ theme: ThemeSupa }}
  />
)
```


### Social providers

The Auth component also supports login with [official social providers](../../auth#providers).

```js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{ theme: ThemeSupa }}
    providers={['google', 'facebook', 'twitter']}
  />
)
```


### Options

Options are available via `queryParams`:

```jsx
<Auth
  supabaseClient={supabase}
  providers={['google']}
  queryParams={{
    access_type: 'offline',
    prompt: 'consent',
    hd: 'domain.com',
  }}
  onlyThirdPartyProviders
/>
```


### Provider scopes

Provider Scopes can be requested through `providerScope`;

```jsx
<Auth
  supabaseClient={supabase}
  providers={['google']}
  queryParams={{
    access_type: 'offline',
    prompt: 'consent',
    hd: 'domain.com',
  }}
  providerScopes={{
    google: 'https://www.googleapis.com/auth/calendar.readonly',
  }}
/>
```


### Supported views

The Auth component is currently shipped with the following views:

*   [Email Login](../auth-email)
*   [Magic Link login](../auth-magic-link)
*   [Social Login](../social-login)
*   Update password
*   Forgotten password

We are planning on adding more views in the future. Follow along on that [repo](https://github.com/supabase/auth-ui).



## Customization

There are several ways to customize Auth UI:

*   Use one of the [predefined themes](#predefined-themes) that comes with Auth UI
*   Extend a theme by [overriding the variable tokens](#override-themes) in a theme
*   [Create your own theme](#create-theme)
*   [Use your own CSS classes](#custom-css-classes)
*   [Use inline styles](#custom-inline-styles)
*   [Use your own labels](#custom-labels)


### Predefined themes

Auth UI comes with several themes to customize the appearance. Each predefined theme comes with at least two variations, a `default` variation, and a `dark` variation. You can switch between these themes using the `theme` prop. Import the theme you want to use and pass it to the `appearance.theme` prop.

```js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient(
  '<INSERT PROJECT URL>',
  '<INSERT PROJECT ANON API KEY>'
)

const App = () => (
  <Auth
    supabaseClient={supabase}
    {/* Apply predefined theme */}
    appearance={{ theme: ThemeSupa }}
  />
)
```

<Admonition type="note">
  Currently there is only one predefined theme available, but we plan to add more.
</Admonition>


### Switch theme variations

Auth UI comes with two theme variations: `default` and `dark`. You can switch between these themes with the `theme` prop.

```js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient(
  '<INSERT PROJECT URL>',
  '<INSERT PROJECT ANON API KEY>'
)

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{ theme: ThemeSupa }}
    {/* Set theme to dark */}
    theme="dark"
  />
)
```

If you don't pass a value to `theme` it uses the `"default"` theme. You can pass `"dark"` to the theme prop to switch to the `dark` theme. If your theme has other variations, use the name of the variation in this prop.


### Override themes

Auth UI themes can be overridden using variable tokens. See the [list of variable tokens](https://github.com/supabase/auth-ui/blob/main/packages/shared/src/theming/Themes.ts).

```js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'
import { ThemeSupa } from '@supabase/auth-ui-shared'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{
      theme: ThemeSupa,
      variables: {
        default: {
          colors: {
            brand: 'red',
            brandAccent: 'darkred',
          },
        },
      },
    }}
  />
)
```

If you created your own theme, you may not need to override any of them.


### Create your own theme \[#create-theme]

You can create your own theme by following the same structure within a `appearance.theme` property.
See the list of [tokens within a theme](https://github.com/supabase/auth-ui/blob/main/packages/shared/src/theming/Themes.ts).

```js /src/index.js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const customTheme = {
  default: {
    colors: {
      brand: 'hsl(153 60.0% 53.0%)',
      brandAccent: 'hsl(154 54.8% 45.1%)',
      brandButtonText: 'white',
      // ..
    },
  },
  dark: {
    colors: {
      brandButtonText: 'white',
      defaultButtonBackground: '#2e2e2e',
      defaultButtonBackgroundHover: '#3e3e3e',
      //..
    },
  },
  // You can also add more theme variations with different names.
  evenDarker: {
    colors: {
      brandButtonText: 'white',
      defaultButtonBackground: '#1e1e1e',
      defaultButtonBackgroundHover: '#2e2e2e',
      //..
    },
  },
}

const App = () => (
  <Auth
    supabaseClient={supabase}
    theme="default" // can also be "dark" or "evenDarker"
    appearance={{ theme: customTheme }}
  />
)
```

You can switch between different variations of your theme with the ["theme" prop](#switch-theme-variations).


### Custom CSS classes \[#custom-css-classes]

You can use custom CSS classes for the following elements:
`"button"`, `"container"`, `"anchor"`, `"divider"`, `"label"`, `"input"`, `"loader"`, `"message"`.

```js /src/index.js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{
      // If you want to extend the default styles instead of overriding it, set this to true
      extend: false,
      // Your custom classes
      className: {
        anchor: 'my-awesome-anchor',
        button: 'my-awesome-button',
        //..
      },
    }}
  />
)
```


### Custom inline CSS \[#custom-inline-styles]

You can use custom CSS inline styles for the following elements:
`"button"`, `"container"`, `"anchor"`, `"divider"`, `"label"`, `"input"`, `"loader"`, `"message"`.

```js /src/index.js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    appearance={{
      style: {
        button: { background: 'red', color: 'white' },
        anchor: { color: 'blue' },
        //..
      },
    }}
  />
)
```


### Custom labels \[#custom-labels]

You can use custom labels with `localization.variables` like so:

```js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => (
  <Auth
    supabaseClient={supabase}
    localization={{
      variables: {
        sign_in: {
          email_label: 'Your email address',
          password_label: 'Your strong password',
        },
      },
    }}
  />
)
```

A full list of the available variables is below:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sign-up">
  <TabPanel id="sign-up" label="Sign Up">
    | Label Tag                    | Default Label                              |
    | ---------------------------- | ------------------------------------------ |
    | `email_label`                | Email address                              |
    | `password_label`             | Create a Password                          |
    | `email_input_placeholder`    | Your email address                         |
    | `password_input_placeholder` | Your password                              |
    | `button_label`               | Sign up                                    |
    | `loading_button_label`       | Signing up ...                             |
    | `social_provider_text`       | Sign in with `{{provider}}`                |
    | `link_text`                  | Don't have an account? Sign up             |
    | `confirmation_text`          | Check your email for the confirmation link |
  </TabPanel>

  <TabPanel id="sign-in" label="Sign In">
    | Label Tag                    | Default Label                    |
    | ---------------------------- | -------------------------------- |
    | `email_label`                | Email address                    |
    | `password_label`             | Your Password                    |
    | `email_input_placeholder`    | Your email address               |
    | `password_input_placeholder` | Your password                    |
    | `button_label`               | Sign in                          |
    | `loading_button_label`       | Signing in ...                   |
    | `social_provider_text`       | Sign in with `{{provider}}`      |
    | `link_text`                  | Already have an account? Sign in |
  </TabPanel>

  <TabPanel id="magic_link" label="Magic Link">
    | Label Tag                 | Default Label                       |
    | ------------------------- | ----------------------------------- |
    | `email_input_label`       | Email address                       |
    | `email_input_placeholder` | Your email address                  |
    | `button_label`            | Sign in                             |
    | `loading_button_label`    | Signing in ...                      |
    | `link_text`               | Send a magic link email             |
    | `confirmation_text`       | Check your email for the magic link |
  </TabPanel>

  <TabPanel id="forgotten-password" label="Forgotten Password">
    | Label Tag                 | Default Label                                |
    | ------------------------- | -------------------------------------------- |
    | `email_label`             | Email address                                |
    | `password_label`          | Your Password                                |
    | `email_input_placeholder` | Your email address                           |
    | `button_label`            | Send reset password instructions             |
    | `loading_button_label`    | Sending reset instructions ...               |
    | `link_text`               | Forgot your password?                        |
    | `confirmation_text`       | Check your email for the password reset link |
  </TabPanel>

  <TabPanel id="update-password" label="Update Password">
    | Label Tag                    | Default Label                  |
    | ---------------------------- | ------------------------------ |
    | `password_label`             | New Password                   |
    | `password_input_placeholder` | Your new password              |
    | `button_label`               | Update password                |
    | `loading_button_label`       | Updating password ...          |
    | `confirmation_text`          | Your password has been updated |
  </TabPanel>

  <TabPanel id="verify-otp" label="Verify OTP">
    | Label Tag                 | Default Label      |
    | ------------------------- | ------------------ |
    | `email_input_label`       | Email address      |
    | `email_input_placeholder` | Your email address |
    | `phone_input_label`       | Phone number       |
    | `phone_input_placeholder` | Your phone number  |
    | `token_input_label`       | Token              |
    | `token_input_placeholder` | Your OTP token     |
    | `button_label`            | Verify token       |
    | `loading_button_label`    | Signing in ...     |
  </TabPanel>
</Tabs>

<Admonition type="caution">
  Currently, translating error messages (e.g. "Invalid credentials") is not supported. Check [related issue.](https://github.com/supabase/auth-ui/issues/86)
</Admonition>


### Hiding links \[#hiding-links]

You can hide links by setting the `showLinks` prop to `false`

```js
import { createClient } from '@supabase/supabase-js'
import { Auth } from '@supabase/auth-ui-react'

const supabase = createClient('<INSERT PROJECT URL>', '<INSERT PROJECT ANON API KEY>')

const App = () => <Auth supabaseClient={supabase} showLinks={false} />
```

Setting `showLinks` to `false` will hide the following links:

*   Don't have an account? Sign up
*   Already have an account? Sign in
*   Send a magic link email
*   Forgot your password?


### Sign in and sign up views

Add `sign_in` or `sign_up` views with the `view` prop:

```
<Auth
  supabaseClient={supabase}
  view="sign_up"
/>
```



# Flutter Auth UI



Flutter Auth UI is a Flutter package containing pre-built widgets for authenticating users.
It is unstyled and can match your brand and aesthetic.

![Flutter Auth UI](https://raw.githubusercontent.com/supabase-community/flutter-auth-ui/main/screenshots/supabase_auth_ui.png)



## Add Flutter Auth UI

Add the latest version of the package [supabase-auth-ui](https://pub.dev/packages/supabase_auth_ui) to pubspec.yaml:

```bash
flutter pub add supabase_auth_ui
```


### Initialize the Flutter Auth package

```dart
import 'package:flutter/material.dart';
import 'package:supabase_auth_ui/supabase_auth_ui.dart';

void main() async {
  await Supabase.initialize(
    url: dotenv.get('SUPABASE_URL'),
    anonKey: dotenv.get('SUPABASE_PUBLISHABLE_KEY'),
  );

  runApp(const MyApp());
}
```


### Email Auth

Use a `SupaEmailAuth` widget to create an email and password signin and signup form. It also contains a button to toggle to display a forgot password form.

You can pass `metadataFields` to add additional fields to the form to pass as metadata to Supabase.

```dart
SupaEmailAuth(
  redirectTo: kIsWeb ? null : 'io.mydomain.myapp://callback',
  onSignInComplete: (response) {},
  onSignUpComplete: (response) {},
  metadataFields: [
    MetaDataField(
    prefixIcon: const Icon(Icons.person),
    label: 'Username',
    key: 'username',
    validator: (val) {
            if (val == null || val.isEmpty) {
            return 'Please enter something';
            }
            return null;
          },
        ),
    ],
)
```


### Magic link Auth

Use `SupaMagicAuth` widget to create a magic link signIn form.

```dart
SupaMagicAuth(
  redirectUrl: kIsWeb ? null : 'io.mydomain.myapp://callback',
  onSuccess: (Session response) {},
  onError: (error) {},
)
```


### Reset password

Use `SupaResetPassword` to create a password reset form.

```dart
SupaResetPassword(
  accessToken: supabase.auth.currentSession?.accessToken,
  onSuccess: (UserResponse response) {},
  onError: (error) {},
)
```


### Phone Auth

Use `SupaPhoneAuth` to create a phone authentication form.

```dart
SupaPhoneAuth(
  authAction: SupaAuthAction.signUp,
  onSuccess: (AuthResponse response) {},
),
```


### Social Auth

The package supports login with [official social providers](../../auth#providers).

Use `SupaSocialsAuth` to create list of social login buttons.

```dart
SupaSocialsAuth(
  socialProviders: [
    OAuthProvider.apple,
    OAuthProvider.google,
  ],
  colored: true,
  redirectUrl: kIsWeb
    ? null
    : 'io.mydomain.myapp://callback',
  onSuccess: (Session response) {},
  onError: (error) {},
)
```


### Theming

This package uses plain Flutter components allowing you to control the appearance of the components using your own theme.



# Supabase Auth with Next.js Pages Directory



<Admonition type="caution">
  The Auth helpers package is deprecated. Use the new `@supabase/ssr` package for Server Side Authentication. `@supabase/ssr` takes the core concepts of the Auth Helpers package and makes them available to any server framework. Read the [migration doc](/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers) to learn more.

  We recommend setting up Auth for your Next.js app with `@supabase/ssr` instead. Read the [Next.js Server-Side Auth guide](/docs/guides/auth/server-side/nextjs?router=pages) to learn how.
</Admonition>

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light border-b mt-8 pb-2">
  <AccordionItem header="See legacy docs" id="legacy-docs">
    This submodule provides convenience helpers for implementing user authentication in Next.js applications using the pages directory.

    <Admonition type="note">
      Note: As of [Next.js 13.4](https://nextjs.org/blog/next-13-4), the App Router has reached stable status. This is now the recommended path for new Next.js app. Check out our guide on using [Auth Helpers with the Next.js App Directory](/docs/guides/auth/auth-helpers/nextjs).
    </Admonition>

    ## Install the Next.js helper library

    ```sh Terminal
    npm install @supabase/auth-helpers-nextjs @supabase/supabase-js
    ```

    This library supports the following tooling versions:

    *   Node.js: `^10.13.0 || >=12.0.0`
    *   Next.js: `>=10`

    Additionally, install the **React Auth Helpers** for components and hooks that can be used across all React-based frameworks.

    ```sh Terminal
    npm install @supabase/auth-helpers-react
    ```

    ## Set up environment variables

    Retrieve your project URL and anon key in your project's [API settings](/dashboard/project/_/settings/api) in the Dashboard to set up the following environment variables. For local development you can set them in a `.env.local` file. See an [example](https://github.com/supabase/auth-helpers/blob/main/examples/nextjs/.env.local.example).

    ```bash .env.local
    NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
    NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=your-supabase-publishable-key
    ```

    ## Basic setup

    <Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        Wrap your `pages/_app.js` component with the `SessionContextProvider` component:

        ```jsx pages/_app.js
        import { createPagesBrowserClient } from '@supabase/auth-helpers-nextjs'
        import { SessionContextProvider } from '@supabase/auth-helpers-react'
        import { useState } from 'react'

        function MyApp({ Component, pageProps }) {
          // Create a new supabase browser client on every first render.
          const [supabaseClient] = useState(() => createPagesBrowserClient())

          return (
            <SessionContextProvider
              supabaseClient={supabaseClient}
              initialSession={pageProps.initialSession}
            >
              <Component {...pageProps} />
            </SessionContextProvider>
          )
        }
        ```
      </TabPanel>

      <TabPanel id="ts" label="TypeScript">
        Wrap your `pages/_app.tsx` component with the `SessionContextProvider` component:

        ```tsx
        import { type AppProps } from 'next/app'
        import { createPagesBrowserClient } from '@supabase/auth-helpers-nextjs'
        import { SessionContextProvider, Session } from '@supabase/auth-helpers-react'
        import { useState } from 'react'

        function MyApp({
          Component,
          pageProps,
        }: AppProps<{
          initialSession: Session
        }>) {
          // Create a new supabase browser client on every first render.
          const [supabaseClient] = useState(() => createPagesBrowserClient())

          return (
            <SessionContextProvider
              supabaseClient={supabaseClient}
              initialSession={pageProps.initialSession}
            >
              <Component {...pageProps} />
            </SessionContextProvider>
          )
        }
        export default MyApp
        ```
      </TabPanel>
    </Tabs>

    You can now determine if a user is authenticated by checking that the `user` object returned by the `useUser()` hook is defined.

    ### Code Exchange API route

    The `Code Exchange` API route is required for the [server-side auth flow](/docs/guides/auth/server-side-rendering) implemented by the Next.js Auth Helpers. It exchanges an auth `code` for the user's `session`, which is set as a cookie for future requests made to Supabase.

    <Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        Create a new file at `pages/api/auth/callback.js` and populate with the following:

        ```jsx pages/api/auth/callback.js
        import { NextApiHandler } from 'next'
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        const handler = async (req, res) => {
          const { code } = req.query

          if (code) {
            const supabase = createPagesServerClient({ req, res })
            await supabase.auth.exchangeCodeForSession(String(code))
          }

          res.redirect('/')
        }

        export default handler
        ```
      </TabPanel>

      <TabPanel id="ts" label="TypeScript">
        Create a new file at `pages/api/auth/callback.ts` and populate with the following:

        ```tsx pages/api/auth/callback.ts
        import { NextApiHandler } from 'next'
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        const handler: NextApiHandler = async (req, res) => {
          const { code } = req.query

          if (code) {
            const supabase = createPagesServerClient({ req, res })
            await supabase.auth.exchangeCodeForSession(String(code))
          }

          res.redirect('/')
        }

        export default handler
        ```
      </TabPanel>
    </Tabs>

    ## Usage with TypeScript

    You can pass types that were [generated with the Supabase CLI](/docs/reference/javascript/typescript-support#generating-types) to the Supabase Client to get enhanced type safety and auto completion:

    ### Browser client

    Creating a new `supabase` client object:

    ```tsx
    import { createPagesBrowserClient } from '@supabase/auth-helpers-nextjs'
    import { Database } from '../database.types'

    const supabaseClient = createPagesBrowserClient<Database>()
    ```

    Retrieving a `supabase` client object from the `SessionContext`:

    ```tsx
    import { useSupabaseClient } from '@supabase/auth-helpers-react'
    import { Database } from '../database.types'

    const supabaseClient = useSupabaseClient<Database>()
    ```

    ### Server client

    ```tsx
    // Creating a new supabase server client object (e.g. in API route):
    import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'
    import type { NextApiRequest, NextApiResponse } from 'next'
    import type { Database } from 'types_db'

    export default async (req: NextApiRequest, res: NextApiResponse) => {
      const supabaseServerClient = createPagesServerClient<Database>({
        req,
        res,
      })
      const {
        data: { user },
      } = await supabaseServerClient.auth.getUser()

      res.status(200).json({ name: user?.name ?? '' })
    }
    ```

    ## Client-side data fetching with RLS

    For [row level security](/docs/learn/auth-deep-dive/auth-row-level-security) to work properly when fetching data client-side, you need to make sure to use the `supabaseClient` from the `useSupabaseClient` hook and only run your query once the user is defined client-side in the `useUser()` hook:

    ```jsx
    import { Auth } from '@supabase/auth-ui-react'
    import { ThemeSupa } from '@supabase/auth-ui-shared'
    import { useUser, useSupabaseClient } from '@supabase/auth-helpers-react'
    import { useEffect, useState } from 'react'

    const LoginPage = () => {
      const supabaseClient = useSupabaseClient()
      const user = useUser()
      const [data, setData] = useState()

      useEffect(() => {
        async function loadData() {
          const { data } = await supabaseClient.from('test').select('*')
          setData(data)
        }
        // Only run query once user is logged in.
        if (user) loadData()
      }, [user])

      if (!user)
        return (
          <Auth
            redirectTo="http://localhost:3000/"
            appearance={{ theme: ThemeSupa }}
            supabaseClient={supabaseClient}
            providers={['google', 'github']}
            socialLayout="horizontal"
          />
        )

      return (
        <>
          <button onClick={() => supabaseClient.auth.signOut()}>Sign out</button>
          <p>user:</p>
          <pre>{JSON.stringify(user, null, 2)}</pre>
          <p>client-side data fetching with RLS</p>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </>
      )
    }

    export default LoginPage
    ```

    ## Server-side rendering (SSR)

    Create a server Supabase client to retrieve the logged in user's session:

    ```jsx pages/profile.js
    import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

    export default function Profile({ user }) {
      return <div>Hello {user.name}</div>
    }

    export const getServerSideProps = async (ctx) => {
      // Create authenticated Supabase Client
      const supabase = createPagesServerClient(ctx)
      // Check if we have a user
      const {
        data: { user },
      } = await supabase.auth.getUser()

      if (!user)
        return {
          redirect: {
            destination: '/',
            permanent: false,
          },
        }

      return {
        props: {
          user,
        },
      }
    }
    ```

    ## Server-side data fetching with RLS

    You can use the server Supabase client to run [row level security](/docs/learn/auth-deep-dive/auth-row-level-security) authenticated queries server-side:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        ```jsx
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        export default function ProtectedPage({ user, data }) {
          return (
            <>
              <div>Protected content for {user.email}</div>
              <pre>{JSON.stringify(data, null, 2)}</pre>
              <pre>{JSON.stringify(user, null, 2)}</pre>
            </>
          )
        }

        export const getServerSideProps = async (ctx) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient(ctx)
          // Check if we have a session
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (!session)
            return {
              redirect: {
                destination: '/',
                permanent: false,
              },
            }

          // Run queries with RLS on the server
          const { data } = await supabase.from('users').select('*')

          return {
            props: {
              user,
              data: data ?? [],
            },
          }
        }
        ```
      </TabPanel>

      <TabPanel id="ts" label="TypeScript">
        ```tsx
        import { User, createPagesServerClient } from '@supabase/auth-helpers-nextjs'
        import { GetServerSidePropsContext } from 'next'

        export default function ProtectedPage({ user, data }: { user: User; data: any }) {
          return (
            <>
              <div>Protected content for {user.email}</div>
              <pre>{JSON.stringify(data, null, 2)}</pre>
              <pre>{JSON.stringify(user, null, 2)}</pre>
            </>
          )
        }

        export const getServerSideProps = async (ctx: GetServerSidePropsContext) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient(ctx)
          // Check if we have a session
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (!user)
            return {
              redirect: {
                destination: '/',
                permanent: false,
              },
            }

          // Run queries with RLS on the server
          const { data } = await supabase.from('users').select('*')

          return {
            props: {
              user,
              data: data ?? [],
            },
          }
        }
        ```
      </TabPanel>
    </Tabs>

    ## Server-side data fetching to OAuth APIs using `provider token` {`#oauth-provider-token`}

    When using third-party auth providers, sessions are initiated with an additional `provider_token` field which is persisted in the auth cookie and can be accessed within the session object. The `provider_token` can be used to make API requests to the OAuth provider's API endpoints on behalf of the logged-in user.

    Note that the server accesses data on the session object returned by `auth.getSession`. This data should normally not be trusted, because it is read from the local storage medium. It is not revalidated against the Auth server unless the session is expired, which means the sender can tamper with it.

    In this case, the third-party API will validate the `provider_token`, and a malicious actor is unable to forge one.

    <Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        ```jsx
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        export default function ProtectedPage({ user, allRepos }) {
          return (
            <>
              <div>Protected content for {user.email}</div>
              <p>Data fetched with provider token:</p>
              <pre>{JSON.stringify(allRepos, null, 2)}</pre>
              <p>user:</p>
              <pre>{JSON.stringify(user, null, 2)}</pre>
            </>
          )
        }

        export const getServerSideProps = async (ctx) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient(ctx)
          // Check if we have a session
          const {
            data: { session },
          } = await supabase.auth.getSession()

          if (!session)
            return {
              redirect: {
                destination: '/',
                permanent: false,
              },
            }

          // Retrieve provider_token & logged in user's third-party id from metadata
          const { provider_token, user } = session
          const userId = user.user_metadata.user_name

          const allRepos = await (
            await fetch(`https://api.github.com/search/repositories?q=user:${userId}`, {
              method: 'GET',
              headers: {
                Authorization: `token ${provider_token}`,
              },
            })
          ).json()

          return { props: { user, allRepos } }
        }
        ```
      </TabPanel>

      <TabPanel id="ts" label="TypeScript">
        ```tsx
        import { User, createPagesServerClient } from '@supabase/auth-helpers-nextjs'
        import { GetServerSidePropsContext } from 'next'

        export default function ProtectedPage({ user, allRepos }: { user: User; allRepos: any }) {
          return (
            <>
              <div>Protected content for {user.email}</div>
              <p>Data fetched with provider token:</p>
              <pre>{JSON.stringify(allRepos, null, 2)}</pre>
              <p>user:</p>
              <pre>{JSON.stringify(user, null, 2)}</pre>
            </>
          )
        }

        export const getServerSideProps = async (ctx: GetServerSidePropsContext) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient(ctx)
          // Check if we have a session
          const {
            data: { session },
          } = await supabase.auth.getSession()

          if (!session)
            return {
              redirect: {
                destination: '/',
                permanent: false,
              },
            }

          // Retrieve provider_token & logged in user's third-party id from metadata
          const { provider_token, user } = session
          const userId = user.user_metadata.user_name

          const allRepos = await (
            await fetch(`https://api.github.com/search/repositories?q=user:${userId}`, {
              method: 'GET',
              headers: {
                Authorization: `token ${provider_token}`,
              },
            })
          ).json()

          return { props: { user, allRepos } }
        }
        ```
      </TabPanel>
    </Tabs>

    ## Protecting API routes

    Create a server Supabase client to retrieve the logged in user's session:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
      <TabPanel id="js" label="JavaScript">
        ```jsx pages/api/protected-route.js
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        const ProtectedRoute = async (req, res) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient({ req, res })
          // Check if we have a user
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (!user)
            return res.status(401).json({
              error: 'not_authenticated',
              description: 'The user does not have an active session or is not authenticated',
            })

          // Run queries with RLS on the server
          const { data } = await supabase.from('test').select('*')
          res.json(data)
        }

        export default ProtectedRoute
        ```
      </TabPanel>

      <TabPanel id="ts" label="TypeScript">
        ```tsx pages/api/protected-route.ts
        import { NextApiHandler } from 'next'
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        const ProtectedRoute: NextApiHandler = async (req, res) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient({ req, res })
          // Check if we have a session
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (!user)
            return res.status(401).json({
              error: 'not_authenticated',
              description: 'The user does not have an active session or is not authenticated',
            })

          // Run queries with RLS on the server
          const { data } = await supabase.from('test').select('*')
          res.json(data)
        }

        export default ProtectedRoute
        ```
      </TabPanel>
    </Tabs>

    ## Auth with Next.js middleware

    As an alternative to protecting individual pages you can use a [Next.js Middleware](https://nextjs.org/docs/middleware) to protect the entire directory or those that match the config object. In the following example, all requests to `/middleware-protected/*` will check whether a user is signed in, if successful the request will be forwarded to the destination route, otherwise the user will be redirected:

    ```ts middleware.ts
    import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs'
    import { NextResponse } from 'next/server'
    import type { NextRequest } from 'next/server'

    export async function middleware(req: NextRequest) {
      // We need to create a response and hand it to the supabase client to be able to modify the response headers.
      const res = NextResponse.next()
      // Create authenticated Supabase Client.
      const supabase = createMiddlewareClient({ req, res })
      // Check if we have a session
      const {
        data: { user },
      } = await supabase.auth.getUser()

      // Check auth condition
      if (user?.email?.endsWith('@gmail.com')) {
        // Authentication successful, forward request to protected route.
        return res
      }

      // Auth condition not met, redirect to home page.
      const redirectUrl = req.nextUrl.clone()
      redirectUrl.pathname = '/'
      redirectUrl.searchParams.set(`redirectedFrom`, req.nextUrl.pathname)
      return NextResponse.redirect(redirectUrl)
    }

    export const config = {
      matcher: '/middleware-protected/:path*',
    }
    ```

    ## Migration guide

    ### Migrating to v0.7.X

    #### PKCE Auth flow

    PKCE is the new server-side auth flow implemented by the Next.js Auth Helpers. It requires a new API route for `/api/auth/callback` that exchanges an auth `code` for the user's `session`.

    Check the [Code Exchange API Route steps](/docs/guides/auth/auth-helpers/nextjs-pages#code-exchange-api-route) above to implement this route.

    #### Authentication

    For authentication methods that have a `redirectTo` or `emailRedirectTo`, this must be set to this new code exchange API Route - `/api/auth/callback`. This is an example with the `signUp` function:

    ```jsx
    supabase.auth.signUp({
      email: 'valid.email@supabase.io',
      password: 'sup3rs3cur3',
      options: {
        emailRedirectTo: 'http://localhost:3000/auth/callback',
      },
    })
    ```

    #### Deprecated functions

    With v0.7.x of the Next.js Auth Helpers a new naming convention has been implemented for `createClient` functions. The `createBrowserSupabaseClient` and `createServerSupabaseClient` functions have been marked as deprecated, and will be removed in a future version of the Auth Helpers.

    *   `createBrowserSupabaseClient` has been replaced with `createPagesBrowserClient`
    *   `createServerSupabaseClient` has been replaced with `createPagesServerClient`

    ### Migrating to v0.5.X

    To make these helpers more flexible as well as more maintainable and easier to upgrade for new versions of Next.js, we're stripping them down to the most useful part which is managing the cookies and giving you an authenticated supabase-js client in any environment (client, server, middleware/edge).

    Therefore we're marking the `withApiAuth`, `withPageAuth`, and `withMiddlewareAuth` higher order functions as deprecated and they will be removed in the next **minor** release (v0.6.X).

    Follow the steps below to update your API routes, pages, and middleware handlers. Thanks!

    #### `withApiAuth` deprecated!

    Use `createPagesServerClient` within your `NextApiHandler`:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="before" queryGroup="migration-side">
      <TabPanel id="before" label="Before">
        ```tsx pages/api/protected-route.ts
        import { withApiAuth } from '@supabase/auth-helpers-nextjs'

        export default withApiAuth(async function ProtectedRoute(req, res, supabase) {
          // Run queries with RLS on the server
          const { data } = await supabase.from('test').select('*')
          res.json(data)
        })
        ```
      </TabPanel>

      <TabPanel id="after" label="After">
        ```tsx pages/api/protected-route.ts
        import { NextApiHandler } from 'next'
        import { createPagesServerClient } from '@supabase/auth-helpers-nextjs'

        const ProtectedRoute: NextApiHandler = async (req, res) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient({ req, res })
          // Check if we have a session
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (!user)
            return res.status(401).json({
              error: 'not_authenticated',
              description: 'The user does not have an active session or is not authenticated',
            })

          // Run queries with RLS on the server
          const { data } = await supabase.from('test').select('*')
          res.json(data)
        }

        export default ProtectedRoute
        ```
      </TabPanel>
    </Tabs>

    #### `withPageAuth` deprecated!

    Use `createPagesServerClient` within `getServerSideProps`:

    <Tabs scrollable size="small" type="underlined" defaultActiveId="before" queryGroup="migration-side">
      <TabPanel id="before" label="Before">
        ```tsx pages/profile.tsx
        import { withPageAuth, User } from '@supabase/auth-helpers-nextjs'

        export default function Profile({ user }: { user: User }) {
          return <pre>{JSON.stringify(user, null, 2)}</pre>
        }

        export const getServerSideProps = withPageAuth({ redirectTo: '/' })
        ```
      </TabPanel>

      <TabPanel id="after" label="After">
        ```tsx pages/profile.js
        import { createPagesServerClient, User } from '@supabase/auth-helpers-nextjs'
        import { GetServerSidePropsContext } from 'next'

        export default function Profile({ user }: { user: User }) {
          return <pre>{JSON.stringify(user, null, 2)}</pre>
        }

        export const getServerSideProps = async (ctx: GetServerSidePropsContext) => {
          // Create authenticated Supabase Client
          const supabase = createPagesServerClient(ctx)
          // Check if we have a session
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (!user)
            return {
              redirect: {
                destination: '/',
                permanent: false,
              },
            }

          return {
            props: {
              initialSession: session,
              user: session.user,
            },
          }
        }
        ```
      </TabPanel>
    </Tabs>

    #### `withMiddlewareAuth` deprecated!

    <Tabs scrollable size="small" type="underlined" defaultActiveId="before" queryGroup="migration-side">
      <TabPanel id="before" label="Before">
        ```tsx middleware.ts
        import { withMiddlewareAuth } from '@supabase/auth-helpers-nextjs'

        export const middleware = withMiddlewareAuth({
          redirectTo: '/',
          authGuard: {
            isPermitted: async (user) => {
              return user.email?.endsWith('@gmail.com') ?? false
            },
            redirectTo: '/insufficient-permissions',
          },
        })

        export const config = {
          matcher: '/middleware-protected',
        }
        ```
      </TabPanel>

      <TabPanel id="after" label="After">
        ```tsx middleware.ts
        import { createMiddlewareClient } from '@supabase/auth-helpers-nextjs'
        import { NextResponse } from 'next/server'
        import type { NextRequest } from 'next/server'

        export async function middleware(req: NextRequest) {
          // We need to create a response and hand it to the supabase client to be able to modify the response headers.
          const res = NextResponse.next()
          // Create authenticated Supabase Client.
          const supabase = createMiddlewareClient({ req, res })
          // Check if we have a session
          const {
            data: { user },
          } = await supabase.auth.getUser()

          // Check auth condition
          if (user?.email?.endsWith('@gmail.com')) {
            // Authentication successful, forward request to protected route.
            return res
          }

          // Auth condition not met, redirect to home page.
          const redirectUrl = req.nextUrl.clone()
          redirectUrl.pathname = '/'
          redirectUrl.searchParams.set(`redirectedFrom`, req.nextUrl.pathname)
          return NextResponse.redirect(redirectUrl)
        }

        export const config = {
          matcher: '/middleware-protected',
        }
        ```
      </TabPanel>
    </Tabs>

    ### Migrating to v0.4.X and supabase-js v2

    With the update to `supabase-js` v2 the `auth` API routes are no longer required, therefore you can go ahead and delete your `auth` directory under the `/pages/api/` directory. Refer to the [v2 migration guide](/docs/reference/javascript/v1/upgrade-guide) for the full set of changes within supabase-js.

    The `/api/auth/logout` API route has been removed, use the `signout` method instead:

    ```jsx
    <button
      onClick={async () => {
        await supabaseClient.auth.signOut()
        router.push('/')
      }}
    >
      Logout
    </button>
    ```

    The `supabaseClient` and `supabaseServerClient` have been removed in favor of the `createPagesBrowserClient` and `createPagesServerClient` methods. This allows you to provide the CLI-generated types to the client:

    ```tsx
    // client-side
    import type { Database } from 'types_db'
    const [supabaseClient] = useState(() => createPagesBrowserClient<Database>())

    // server-side API route
    import type { NextApiRequest, NextApiResponse } from 'next'
    import type { Database } from 'types_db'

    export default async (req: NextApiRequest, res: NextApiResponse) => {
      const supabaseServerClient = createPagesServerClient<Database>({
        req,
        res,
      })
      const {
        data: { user },
      } = await supabaseServerClient.auth.getUser()

      res.status(200).json({ name: user?.name ?? '' })
    }
    ```

    *   The `UserProvider` has been replaced by the `SessionContextProvider`. Make sure to wrap your `pages/_app.js` component with the `SessionContextProvider`. Then, throughout your application you can use the `useSessionContext` hook to get the `session` and the `useSupabaseClient` hook to get an authenticated `supabaseClient`.
    *   The `useUser` hook now returns the `user` object or `null`.
    *   Usage with TypeScript: You can pass types that were [generated with the Supabase CLI](/docs/reference/javascript/typescript-support#generating-types) to the Supabase Client to get enhanced type safety and auto completion:

    Creating a new `supabase` client object:

    ```tsx
    import { Database } from '../database.types'

    const [supabaseClient] = useState(() => createPagesBrowserClient<Database>())
    ```

    Retrieving a `supabase` client object from the `SessionContext`:

    ```tsx
    import { useSupabaseClient } from '@supabase/auth-helpers-react'
    import { Database } from '../database.types'

    const supabaseClient = useSupabaseClient<Database>()
    ```
  </AccordionItem>
</Accordion>



---
**Navigation:** [← Previous](./36-error-codes.md) | [Index](./index.md) | [Next →](./38-supabase-auth-with-the-nextjs-app-router.md)
