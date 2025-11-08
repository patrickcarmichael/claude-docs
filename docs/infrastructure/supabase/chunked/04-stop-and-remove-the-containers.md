**Navigation:** [← Previous](./03-storage-helper-functions.md) | [Index](./index.md) | [Next →](./05-realtime-concepts.md)

# Stop and remove the containers
docker compose down


# Recreate and start the containers
docker compose up -d
```

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

Be aware that this will result in downtime. Simply restarting the services does not apply configuration changes.



## Stopping all services

You can stop Supabase by running `docker compose stop` in same directory as your `docker-compose.yml` file.



## Uninstalling

You can stop Supabase by running the following in same directory as your `docker-compose.yml` file:

```sh

# Stop docker and remove volumes:
docker compose down -v


# Remove Postgres data:
rm -rf volumes/db/data/
```

This will destroy all data in the database and storage volumes, so be careful!



## Managing your secrets

Many components inside Supabase use secure secrets and passwords. These are listed in the self-hosting [env file](https://github.com/supabase/supabase/blob/master/docker/.env.example), but we strongly recommend using a secrets manager when deploying to production. Plain text files like dotenv lead to accidental costly leaks.

Some suggested systems include:

*   [Doppler](https://www.doppler.com/)
*   [Infisical](https://infisical.com/)
*   [Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) by Azure (Microsoft)
*   [Secrets Manager](https://aws.amazon.com/secrets-manager/) by AWS
*   [Secrets Manager](https://cloud.google.com/secret-manager) by GCP
*   [Vault](https://www.hashicorp.com/products/vault) by HashiCorp



## Advanced

Everything beyond this point in the guide helps you understand how the system works and how you can modify it to suit your needs.


### Architecture

Supabase is a combination of open source tools, each specifically chosen for Enterprise-readiness.

If the tools and communities already exist, with an MIT, Apache 2, or equivalent open license, we will use and support that tool.
If the tool doesn't exist, we build and open source it ourselves.

<Image
  alt="Diagram showing the architecture of Supabase. The Kong API gateway sits in front of 7 services: GoTrue, PostgREST, Realtime, Storage, pg_meta, Functions, and pg_graphql. All the services talk to a single Postgres instance."
  src={{
    dark: "/docs/img/supabase-architecture.svg",
    light: "/docs/img/supabase-architecture--light.svg",
  }}
/>

*   [Kong](https://github.com/Kong/kong) is a cloud-native API gateway.
*   [GoTrue](https://github.com/supabase/gotrue) is an JWT based API for managing users and issuing JWT tokens.
*   [PostgREST](http://postgrest.org/) is a web server that turns your Postgres database directly into a RESTful API
*   [Realtime](https://github.com/supabase/realtime) is an Elixir server that allows you to listen to Postgres inserts, updates, and deletes using WebSockets. Realtime polls Postgres' built-in replication functionality for database changes, converts changes to JSON, then broadcasts the JSON over WebSockets to authorized clients.
*   [Storage](https://github.com/supabase/storage-api) provides a RESTful interface for managing Files stored in S3, using Postgres to manage permissions.
*   [`postgres-meta`](https://github.com/supabase/postgres-meta) is a RESTful API for managing your Postgres, allowing you to fetch tables, add roles, and run queries, etc.
*   [Postgres](https://www.postgresql.org/) is an object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
*   [Supavisor](https://github.com/supabase/supavisor) is a scalable connection pooler for Postgres, allowing for efficient management of database connections.

For the system to work cohesively, some services require additional configuration within the Postgres database. For example, the APIs and Auth system require several [default roles](/docs/guides/database/postgres/roles) and the `pgjwt` Postgres extension.

You can find all the default extensions inside the [schema migration scripts repo](https://github.com/supabase/postgres/tree/develop/migrations). These scripts are mounted at `/docker-entrypoint-initdb.d` to run automatically when starting the database container.


### Configuring services

Each system has a number of configuration options which can be found in the relevant product documentation.

*   [Postgres](https://hub.docker.com/_/postgres/)
*   [PostgREST](https://postgrest.org/en/stable/configuration.html)
*   [Realtime](https://github.com/supabase/realtime#server)
*   [Auth](https://github.com/supabase/auth)
*   [Storage](https://github.com/supabase/storage-api)
*   [Kong](https://docs.konghq.com/gateway/latest/install/docker/)
*   [Supavisor](https://supabase.github.io/supavisor/development/docs/)

These configuration items are generally added to the `env` section of each service, inside the `docker-compose.yml` section. If these configuration items are sensitive, they should be stored in a [secret manager](/docs/guides/self-hosting#managing-your-secrets) or using an `.env` file and then referenced using the `${}` syntax.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="docker-compose.yml" label="docker-compose.yml">
    ```yml name=docker-compose.yml
    services:
      rest:
        image: postgrest/postgrest
        environment:
          PGRST_JWT_SECRET: ${JWT_SECRET}
    ```
  </TabPanel>

  <TabPanel id=".env" label=".env">
    ```bash name=.env
    ## Never check your secrets into version control
    JWT_SECRET=${JWT_SECRET}
    ```
  </TabPanel>
</Tabs>


### Common configuration

Each system can be [configured](../self-hosting#configuration) independently. Some of the most common configuration options are listed below.


#### Configuring an email server

You will need to use a production-ready SMTP server for sending emails. You can configure the SMTP server by updating the following environment variables:

```sh .env
SMTP_ADMIN_EMAIL=
SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=
SMTP_SENDER_NAME=
```

We recommend using [AWS SES](https://aws.amazon.com/ses/). It's extremely cheap and reliable. Restart all services to pick up the new configuration.


#### Configuring S3 Storage

By default all files are stored locally on the server. You can configure the Storage service to use S3 by updating the following environment variables:

```yaml docker-compose.yml
storage:
  environment: STORAGE_BACKEND=s3
    GLOBAL_S3_BUCKET=name-of-your-s3-bucket
    REGION=region-of-your-s3-bucket
```

You can find all the available options in the [storage repository](https://github.com/supabase/storage-api/blob/master/.env.sample). Restart the `storage` service to pick up the changes: `docker compose restart storage --no-deps`


#### Configuring Supabase AI Assistant

Configuring the Supabase AI Assistant is optional. By adding your own `OPENAI_API_KEY`, you can enable AI services, which help with writing SQL queries, statements, and policies.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="docker-compose.yml" label="docker-compose.yml">
    ```yaml name=docker-compose.yml
    services:
      studio:
        image: supabase/studio
        environment:
          OPENAI_API_KEY: ${OPENAI_API_KEY:-}
    ```
  </TabPanel>

  <TabPanel id=".env" label=".env">
    ```bash name=.env
    ## Never check your secrets into version control
    `${OPENAI_API_KEY}`
    ```
  </TabPanel>
</Tabs>


#### Setting database's `log_min_messages`

By default, `docker compose` sets the database's `log_min_messages` configuration to `fatal` to prevent redundant logs generated by Realtime. You can configure `log_min_messages` using any of the Postgres [Severity Levels](https://www.postgresql.org/docs/current/runtime-config-logging.html#RUNTIME-CONFIG-SEVERITY-LEVELS).


#### Accessing Postgres through Supavisor

By default, the Postgres database is accessible through the Supavisor connection pooler. This allows for more efficient management of database connections. You can connect to the pooled database using the `POOLER_PROXY_PORT_TRANSACTION` port and `POSTGRES_PORT` for session based connections.

For more information on configuring and using Supavisor, see the [Supavisor documentation](https://supabase.github.io/supavisor/).


#### Exposing your Postgres database

If you need direct access to the Postgres database without going through Supavisor, you can expose it by updating the `docker-compose.yml` file:

```yaml docker-compose.yml

# Comment or remove the supavisor section of the docker-compose file

#  supavisor:

#    ports:

# ...
db:
  ports:
    - ${POSTGRES_PORT}:${POSTGRES_PORT}
```

This is less-secure, so make sure you are running a firewall in front of your server.


#### File storage backend on macOS

By default, Storage backend is set to `file`, which is to use local files as the storage backend. For macOS compatibility, you need to choose `VirtioFS` as the Docker container file sharing implementation (in Docker Desktop -> Preferences -> General).


#### Setting up logging with the Analytics server

Additional configuration is required for self-hosting the Analytics server. For the full setup instructions, see [Self Hosting Analytics](/docs/reference/self-hosting-analytics/introduction#getting-started).


### Upgrading Analytics

Due to the changes in the Analytics server, you will need to run the following commands to upgrade your Analytics server:

<Admonition type="caution">
  All data in analytics will be deleted when you run the commands below.
</Admonition>

```sh
### Destroy analytics to transition to postgres self hosted solution without other data loss


# Enter the container and use your .env POSTGRES_PASSWORD value to login
docker exec -it $(docker ps | grep supabase-db | awk '{print $1}') psql -U supabase_admin --password

# Drop all the data in the _analytics schema
DROP PUBLICATION logflare_pub; DROP SCHEMA _analytics CASCADE; CREATE SCHEMA _analytics;\q

# Drop the analytics container
docker rm supabase-analytics
```

***



## Demo

A minimal setup working on Ubuntu, hosted on DigitalOcean.

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/FqiQKRKsfZE" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>


### Demo using DigitalOcean

1.  A DigitalOcean Droplet with 1 GB memory and 25 GB solid-state drive (SSD) is sufficient to start
2.  To access the Dashboard, use the ipv4 IP address of your Droplet.
3.  If you're unable to access Dashboard, run `docker compose ps` to see if the Studio service is running and healthy.



# Enabling MCP Server Access

Configure secure access to the MCP server in your self-hosted Supabase instance.

The MCP (Model Context Protocol) server in [self-hosted Supabase](/docs/guides/self-hosting/docker) runs behind the internal API. Currently, it does not offer OAuth 2.1 authentication, and is not intended to be exposed to the Internet. The corresponding API route has to be protected by restricting network connections from the outside. By default, all connections to the MCP server are denied.

This guide explains how to securely enable access to your self-hosted MCP server.



## Security considerations

<Admonition type="caution">
  Do not allow connections to the self-hosted MCP server from the Internet. Only access it via:

  *   A VPN connection to the server running the Studio container
  *   An SSH tunnel from your local machine
</Admonition>



## Accessing via SSH tunnel


### Step 1: Determine the local IP address that will be used to access the MCP server

When connecting via an SSH tunnel to the Studio Docker container, the source IP will be that of the Docker bridge gateway. You need to allow connections from this IP address.

Determine the Docker bridge gateway IP on the host running your Supabase containers:

```bash
docker inspect supabase-kong \
  --format '{{range .NetworkSettings.Networks}}{{println .Gateway}}{{end}}'
```

This command will output an IP address, e.g., `172.18.0.1`.


### Step 2: Allow connections from the gateway IP

Add the IP address you discovered to the Kong configuration by editing the following section in `./volumes/api/kong.yml`:

1.  Comment out the request-termination section
2.  Remove the # symbols from the entire section starting with `- name: cors`, including `deny: []`
3.  Add your local IP to the 'allow' list.
4.  Your edited configuration should look like the example below.

```yaml

## MCP endpoint - local access
- name: mcp
  _comment: 'MCP: /mcp -> http://studio:3000/api/mcp (local access)'
  url: http://studio:3000/api/mcp
  routes:
    - name: mcp
      strip_path: true
      paths:
        - /mcp
  plugins:
    # Block access to /mcp by default
    #- name: request-termination
    #  config:
    #    status_code: 403
    #    message: "Access is forbidden."
    # Enable local access (danger zone!)
    # 1. Comment out the 'request-termination' section above
    # 2. Uncomment the entire section below, including 'deny'
    # 3. Add your local IPs to the 'allow' list
    - name: cors
    - name: ip-restriction
      config:
        allow:
          - 127.0.0.1
          - ::1
          # Add your Docker bridge gateway IP below
          - 172.18.0.1
        # Do not remove deny!
        deny: []
```


### Step 3: Restart API gateway

After you've added the local IP address as above, restart the Kong container:

```bash
docker compose restart kong
```


### Step 4: Create the SSH tunnel

From your local machine, create an SSH tunnel to your Supabase host:

```bash
ssh -L localhost:8080:localhost:8000 you@your-supabase-host
```

This command forwards local port `8080` to port `8000` on your Supabase host.


### Step 5: Configure your MCP client

Edit the settings for your MCP client and add the following to `"mcpServers": {}` or `"servers": {}`:

```json
{
  "mcpServers": {
    "supabase-self-hosted": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```


### Step 6: Start using the self-hosted MCP server

From your local machine, check that the MCP server is reachable:

```bash
curl http://localhost:8080/mcp \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "MCP-Protocol-Version: 2025-06-18" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2025-06-18",
      "capabilities": {
        "elicitation": {}
      },
      "clientInfo": {
        "name": "test-client",
        "title": "Test Client",
        "version": "1.0.0"
      }
    }
  }'
```

Start your MCP client (Claude Code, Cursor, etc.) and verify access to the MCP tools. For example, you can ask: "What is Supabase anon key? Use the Supabase MCP server tools."



## Troubleshooting

If you are unable to connect to the MCP server:

1.  Update Kong configuration file to the [latest version](https://github.com/supabase/supabase/blob/master/docker/volumes/api/kong.yml) and edit carefully
2.  Confirm the Docker bridge gateway IP is correctly added in `./volumes/api/kong.yml`
3.  Check Kong's logs for errors: `docker compose logs kong`
4.  Make sure your SSH tunnel is active



# HIPAA Compliance and Supabase



The [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html) is a comprehensive law that protects individuals' health information while ensuring the continuity of health insurance coverage. It sets standards for privacy and security that must be followed by all entities that handle Protected Health Information (PHI), also known as electronic PHI (ePHI). HIPAA is specific to the United States, however many countries have similar or laws already in place or under legislation.

Under HIPAA, both covered entities and business associates have distinct responsibilities to ensure the protection of PHI. Supabase acts as a business associate for customers (the covered entity) who wish to provide healthcare related services. As a business associate, Supabase has a number of obligations and has undergone auditing of the security and privacy controls that are in place to meet these. Supabase has signed a Business Associate Agreement (BAA) with all of our vendors who would have access to ePHI, such as AWS, and ensure that we follow their terms listed in the agreements. Similarly when a customer signs a BAA with us, they have some responsibilities they agree to when using Supabase to store PHI.

<Admonition type="caution">
  The hosted Supabase platform has the necessary controls to meet HIPAA requirements. These controls are not supported out of the box in self-hosted Supabase. HIPAA controls extend further than the Supabase product, encompassing legal agreements (BAAs) with providers, operating controls and policies. Achieving HIPAA compliance with self-hosted Supabase is out of scope for this documentation and you should consult your auditor for further guidance.
</Admonition>


### Customer responsibilities

Covered entities (the customer) are organizations that directly handle PHI, such as health plans, healthcare clearinghouses, and healthcare providers that conduct certain electronic transactions.

1.  **Compliance with HIPAA Rules**: Covered entities must comply with the [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html), [Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html), and [Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) to protect the privacy and security of ePHI.
2.  **Business Associate Agreements (BAAs)**: Customers must sign a BAA with Supabase. When the covered entity engages a business associate to help carry out its healthcare activities, it must have a written BAA. This agreement outlines the business associate's responsibilities and requires them to comply with HIPAA Rules.
3.  **Internal Compliance Programs**: Customers must [configure their HIPAA projects](/docs/guides/platform/hipaa-projects) and follow the guidance given by the security advisor. Covered entities are responsible for implementing internal processes and compliance programs to ensure they meet HIPAA requirements.


### Supabase responsibilities

Supabase as the business associate, and the vendors used by Supabase, are the entities that perform functions or activities on behalf of the customer.

1.  **Direct Liability**: Supabase is directly liable for compliance with certain provisions of the HIPAA Rules. This means Supabase has to implement safeguards to protect ePHI and report breaches to the customer.
2.  **Compliance with BAAs**: Supabase must comply with the terms of the BAA, which includes implementing appropriate administrative, physical, and technical safeguards to protect ePHI.
3.  **Vendor Management**: Supabase must also ensure that our vendors, who may have access to ePHI, comply with HIPAA Rules. This is done through a BAA with each vendor.



## Staying compliant and secure

Compliance is a continuous process and should not be treated as a point-in-time audit of controls. Supabase applies all the necessary privacy and security controls to ensure HIPAA compliance at audit time, but also has additional checks and monitoring in place to ensure those controls are not disabled or altered in between audit periods. Customers commit to doing the same in their HIPAA environments. Supabase provides a growing set of checks that warn customers of changes to their projects that disable or weaken HIPAA required controls. Customers will receive warnings and guidance via the Security Advisor, however the responsibility of applying the recommended controls falls directly to the customer.

Our [shared responsibility model](/docs/guides/deployment/shared-responsibility-model#managing-healthcare-data) document discusses both HIPAA and general data management best practices, how this responsibility is shared between customers and Supabase, and how to stay compliant.



## Frequently asked questions

**What is the difference between SOC 2 and HIPAA?**

Both are frameworks for protecting sensitive data, however they serve two different purposes. They share many security and privacy controls and meeting the controls of one normally means being close to complying with the other.

The main differentiator comes down to purpose and scope.

*   SOC 2 is not industry-specific and can be applied to any service organization that handles customer data.
*   HIPAA is a federal regulation in the United States. HIPAA sets standards for the privacy and security of PHI/ePHI, ensuring that patient data is handled confidentially and securely.

**Are Supabase HIPAA environments also SOC 2 compliant?**

Yes. Supabase applies the same SOC 2 controls to all environments, with additional controls being applied to HIPAA environments.

**How often is Supabase audited?**

Supabase undergoes annual audits. The HIPAA controls are audited during the same audit period as the SOC 2 controls.



## Resources

1.  [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)
2.  [HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html)
3.  [Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
4.  [Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html)
5.  [Configuring HIPAA projects](/docs/guides/platform/hipaa-projects) on Supabase
6.  [Shared Responsibility Model](/docs/guides/deployment/shared-responsibility-model)
7.  [HIPAA shared responsibility](/docs/guides/deployment/shared-responsibility-model#managing-healthcare-data)



# Secure configuration of Supabase platform



The Supabase hosted platform provides a secure by default configuration. Some organizations may however require further security controls to meet their own security policies or compliance requirements.

Access to additional security controls can be found under the [security tab](/dashboard/org/_/security) for organizations.



## Available controls

<Admonition type="note">
  Additional security controls are under active development. Any changes will be published here and
  in our [changelog](/changelog).
</Admonition>


### Enforce multi-factor authentication (MFA)

Organization owners can choose to enforce MFA for all team members.

For configuration information, see [Enforce MFA on Organization](/docs/guides/platform/mfa/org-mfa-enforcement)


### SSO for organizations

Supabase offers single sign-on (SSO) as a login option to provide additional account security for your team. This allows company administrators to enforce the use of an identity provider when logging into Supabase.

For configuration information, see [Enable SSO for Your Organization](/docs/guides/platform/sso).


### Postgres SSL enforcement

Supabase projects support connecting to the Postgres DB without SSL enforced to maximize client compatibility. For increased security, you can prevent clients from connecting if they're not using SSL.

For configuration information, see [Postgres SSL Enforcement](/docs/guides/platform/ssl-enforcement)

<Admonition type="note">
  Controlling this at the organization level is on our roadmap.
</Admonition>


### Network restrictions

Each Supabase project comes with configurable restrictions on the IP ranges that are allowed to connect to Postgres and its pooler ("your database"). These restrictions are enforced before traffic reaches the database. If a connection is not restricted by IP, it still needs to authenticate successfully with valid database credentials.

For configuration information, see [Network Restrictions](/docs/guides/platform/network-restrictions)

<Admonition type="note">
  Controlling this at the organization level is on our roadmap.
</Admonition>


### PrivateLink

PrivateLink provides enterprise-grade private network connectivity between your AWS VPC and your Supabase database using AWS VPC Lattice. This eliminates exposure to the public internet by creating a secure, private connection that keeps your database traffic within the AWS network backbone.

For configuration information, see [PrivateLink](/docs/guides/platform/privatelink)

<Admonition type="note">
  PrivateLink is currently in alpha and available exclusively to Enterprise customers.
</Admonition>



# Secure configuration of Supabase products



The Supabase [production checklist](/docs/guides/deployment/going-into-prod) provides detailed advice on preparing an app for production. While our [SOC 2](/docs/guides/security/soc-2-compliance) and [HIPAA](/docs/guides/security/hipaa-compliance) compliance documents outline the roles and responsibilities for building a secure and compliant app.

Various products at Supabase have their own hardening and configuration guides, below is a definitive list of these to help guide your way.



## Auth

*   [Password security](/docs/guides/auth/password-security)
*   [Rate limits](/docs/guides/auth/rate-limits)
*   [Bot detection / Prevention](/docs/guides/auth/auth-captcha)
*   [JWTs](/docs/guides/auth/jwts)



## Database

*   [Row Level Security](/docs/guides/database/postgres/row-level-security)
*   [Column Level Security](/docs/guides/database/postgres/column-level-security)
*   [Hardening the Data API](/docs/guides/database/hardening-data-api)
*   [Additional security controls for the Data API](/docs/guides/api/securing-your-api)
*   [Custom claims and role based access control](/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac)
*   [Managing Postgres roles](/docs/guides/database/postgres/roles)
*   [Managing secrets with Vault](/docs/guides/database/vault)
*   [Superuser access and unsupported operations](docs/guides/database/postgres/roles-superuser)



## Storage

*   [Object ownership](/docs/guides/storage/security/ownership)
*   [Access control](/docs/guides/storage/security/access-control)
    *   The Storage API docs contain hints about required [RLS policy permissions](/docs/reference/javascript/storage-createbucket)
*   [Custom roles with the storage schema](/docs/guides/storage/schema/custom-roles)



## Realtime

*   [Authorization](docs/guides/realtime/authorization)



# Security testing of your Supabase projects



Supabase customer support policy for penetration testing

Customers of Supabase are permitted to carry out security assessments or penetration tests of their hosted Supabase project components. This testing may be carried out without prior approval for the customer services listed under [permitted services](#permitted-services). Supabase does not permit hosting security tooling that may be perceived as malicious or part of a campaign against Supabase customers or external services. This section is covered by the [Supabase Acceptable Use Policy](/aup) (AUP).

It is the customer’s responsibility to ensure that testing activities are aligned with this policy. Any testing performed outside of the policy will be seen as testing directly against Supabase and may be flagged as abuse behaviour. If Supabase receives an abuse report for activities related to your security testing, we will forward these to you. If you discover a security issue within any of the Supabase products, contact [Supabase Security](mailto:security@supabase.io) immediately.

Furthermore, Supabase runs a [Vulnerability Disclosure Program](https://hackerone.com/ca63b563-9661-4ac3-8d23-7581582ef451/embedded_submissions/new) (VDP) with HackerOne, and external security researchers may report any bugs found within the scope of the aforementioned program. Customer penetration testing does not form part of this VDP.


### Permitted services

*   Authentication
*   Database
*   Edge Functions
*   Storage
*   Realtime
*   `https://<customer_project_ref>.supabase.co/*`
*   `https://db.<customer_project_ref>.supabase.co/*`


### Prohibited testing and activities

*   Any activity contrary to what is listed in the AUP.
*   Denial of Service (DoS) and Distributed Denial of Service (DDoS) testing.
*   Cross-tenant attacks, testing that directly targets other Supabase customers' accounts, organizations, and projects not under the customer’s control.
*   Request flooding.



## Terms and conditions

The customer agrees to the following,

Security testing:

*   Will be limited to the services within the customer’s project.
*   Is subject to the general [Terms of Service](/terms).
*   Is within the [Acceptable Usage Policy](/aup).
*   Will be stopped if contacted by Supabase due to a breach of the above or a negative impact on Supabase and Supabase customers.
*   Any vulnerabilities discovered directly in a Supabase product will be reported to Supabase Security within 24 hours of completion of testing.



# SOC 2 Compliance and Supabase



Supabase is Systems and Organization Controls 2 (SOC 2) Type 2 compliant and is assessed annually to ensure continued adherence to the SOC 2 security framework. SOC 2 assesses Supabase’s adherence to, and implementation of, controls governing the security, availability, processing integrity, confidentiality, and privacy on the Supabase platform. These controls define requirements for the management and storage of customer data on the platform. These controls applied to Supabase, as a service provider, serve two customer data environments.

The first environment is the customer relationship with Supabase, this refers to the data Supabase has on a customer of the platform. All billing, contact, usage and contract information is managed and stored according to SOC 2 requirements.

The second environment is the backend as a service (the product) that Supabase provides to customers. Supabase implements the controls from the SOC 2 framework to ensure the security of the platform, which hosts the backend as a service (the product), including the Postgres Database, Storage, Authentication, Realtime, Edge Functions and Data API features. Supabase can assert that the environment hosting customer data, stored within the product, adheres to SOC 2 requirements. And the management and storage of data within this environment (the product) is strictly controlled and kept secure.

Supabase’s SOC 2 compliance does not transfer to environments outside of the Supabase product or Supabase’s control. This is known as the security or compliance boundary and forms part of the Shared Responsibility Model that Supabase and their customers enter into.

<Admonition type="note">
  SOC 2 does not cover, nor is it a substitute for, compliance with the Health Insurance Portability and Accountability Act (HIPAA).
  Organizations must have a signed Business Associate Agreement (BAA) with Supabase and have the HIPAA add-on enabled when dealing with Protected Health Information (PHI).

  Our [HIPAA documentation](/docs/guides/security/hipaa-compliance) provides more information about the responsibilities and requirements for HIPAA on Supabase.
</Admonition>



# Meeting compliance requirements

SOC 2 compliance is a critical aspect of data security for Supabase and our customers. Being fully SOC 2 compliant is a shared responsibility and here’s a breakdown of the responsibilities for both parties:


### Supabase responsibilities

1.  **Security Measures**: Supabase implements robust security controls to protect customer data. These includes measures to prevent data breaches and ensure the confidentiality and integrity of the information managed and stored by the platform. Supabase is obliged to be vigilant about security risks and must demonstrate that our security measures meet industry standards through regular audits.
2.  **Compliance Audits**: Supabase undergoes SOC 2 audits yearly to verify that our data management practices comply with the Trust Services Criteria (TSC), which include security, availability, processing integrity, confidentiality, and privacy. These audits are conducted by an independent third party.
3.  **Incident Response**: Supabase has an incident response plan in place to handle data breaches efficiently. This plan outlines how the organization detects issues, responds to incidents, and manages system vulnerabilities.
4.  **Reporting**: Upon a successful audit, Supabase receive a SOC 2 report that details our compliance status. This report is available to customers as a SOC 2 Type 2 report, and allows customers and stakeholders to assure that Supabase has implemented adequate and the requisite safeguards to protect sensitive information.


### Customer responsibilities

1.  **Compliance Requirements**: Understand your own compliance requirements. While SOC 2 compliance is not a legal requirement, many enterprise customers require their providers to have a SOC 2 report. This is because it provides assurance that the provider has implemented robust controls to protect customer data.
2.  **Due Diligence**: Customers must perform due diligence when selecting Supabase as a provider. This includes reviewing the SOC 2 Type 2 report to ensure that Supabase meets the expected security standards. Customers should also understand the division of responsibilities between themselves and Supabase to avoid duplication of effort.
3.  **Monitoring and Review**: Customers should regularly monitor and review Supabase’s compliance status.
4.  **Control Compliance**: If a customer needs to be SOC 2 compliant, they should themselves implement the requisite controls and undergo a SOC 2 audit.


### Shared responsibilities

1.  **Data Security**: Both customers and Supabase share the responsibility of ensuring data security. While the Supabase, as the provider, implements the security controls, the customer must ensure that their use of the Supabase platform does not compromise these controls.
2.  **Control Compliance**: Supabase asserts through our SOC 2 that all requisite security controls are met. Customers wishing to also be SOC 2 compliant need to go through their own SOC 2 audit, verifying that security controls are met on the customer's side.

In summary, SOC 2 compliance involves a shared responsibility between Supabase and our customers to ensure the security and integrity of data. Supabase, as a provider, must implement and maintain robust security measures, customers must perform due diligence and monitor Supabase's compliance status, while also implement their own compliance controls to protect their sensitive information.



## Frequently asked questions

**How often is Supabase SOC 2 audited?**

Supabase has obtained SOC 2 Type 2 certification, which means Supabase's controls are fully audited annually. The auditor's reports on these examinations are issued as soon as they are ready after the audit. Supabase makes the SOC 2 Type 2 report available to [Enterprise and Team Plan](/pricing) customers. The audit report covers a rolling 12-month window, known as the audit period, and runs from 1 March to 28 February of the next calendar year.

**How to obtain Supabase's SOC 2 Type 2 report?**

To access the SOC 2 Type 2 report, you must be a Enterprise or Team Plan Supabase customer. The report is downloadable from the [Legal Documents](/dashboard/org/_/documents) section in the organization dashboard.

**Why does it matter that Supabase is SOC 2 Compliant?**

SOC 2 is used to assert that controls are in place to ensure the proper management and storage of data. SOC 2 provides a framework for measuring how secure a service provider is and re-evaluates the provider on an annual basis. This provides the confidence and assurance that data stored within the Supabase platform is correctly secured and managed.

**If Supabase’s SOC 2 does not transfer to the customer, why does it matter that Supabase has SOC 2?**

Even though Supabase’s SOC 2 compliance does not transfer outside of the product, it does provide the assurance that all data within the product is correctly managed and stored. Supabase can assert that only authorized persons have access to the data, and security controls are in place to prevent, detect and respond to data intrusions. This forms part of a customer’s own adherence to the SOC 2 framework and relieves part of the burden of data management and storage on the customer. In many organizations' security and risk departments require all vendors or sub-processors to be SOC 2 compliant.

**What is the security or compliance boundary?**

This defines the boundary or border between Supabase and customer responsibility for data security within the Shared Responsibility Model. Customer data stored within the Supabase product, on the Supabase side of the security boundary, is managed and secured by Supabase. Supabase ensures the safe handling and storage of data within this environment. This includes controls for preventing unauthorized access, monitoring data access, alerting, data backups and redundancy. Data on the customer side of the boundary, the data that enters and leaves the Supabase product, is the responsibility of the customer. Management and possible storage of such data outside of Supabase should be performed by the customer, and any security and compliance controls are the responsibility of the customer.

**We have strong data residency requirements. Does Supabase SOC 2 cover data residency?**

While SOC 2 itself does not mandate specific data residency requirements, organizations may still need to comply with other regulatory frameworks, such as GDPR, that do have such requirements. Ensuring projects are deployed in the correct region is a customer responsibility as each Supabase project is deployed into the region the customer specifies at creation time. All data will remain within the chosen region.
[Read replicas](/docs/guides/platform/read-replicas) can be created for multi-region availability, it remains the customer's responsibility to ensure regions chosen for read replicas are within the geographic area required by any additional regulatory frameworks.

**Does SOC 2 cover health related data (HIPAA)?**

SOC 2 is non-industry specific and provides a framework for the security and privacy of data. This is however not sufficient in most cases when dealing with Protected Healthcare Information (PHI), which requires additional privacy and legal controls.
When dealing with PHI in the United States or for United States customers, HIPAA is mandatory.



## Resources

1.  [System and Organization Controls: SOC Suite of Services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
2.  [Shared Responsibility Model](/docs/guides/deployment/shared-responsibility-model)



# Glossary



Definitions for terminology and acronyms used in the Supabase documentation.



## Access token

An access token is a short-lived (usually no more than 1 hour) token that authorizes a client to access resources on a server. It comes in the form of a [JSON Web Token (JWT)](#json-web-token-jwt).



## Authentication

Authentication (often abbreviated `authn.`) is the process of verifying the identity of a user. Verification of the identity of a user can happen in multiple ways:

1.  Asking users for something they know. For example: password, passphrase.
2.  Checking that users have access to something they own. For example: an email address, a phone number, a hardware key, recovery codes.
3.  Confirming that users have some biological features. For example: a fingerprint, a certain facial structure, an iris print.



## Authenticator app

An authenticator app generates time-based one-time passwords (TOTPs). These passwords are generated based off a long and difficult to guess secret string. The secret is initially passed to the application by scanning a QR code.



## Authorization

Authorization (often abbreviated `authz.`) is the process of verifying if a certain identity is allowed to access resources. Authorization often occurs by verifying an access token.



## Identity provider

An identity provider is software or service that allows third-party applications to identify users without the exchange of passwords. Social login and enterprise single-sign on won't be possible without identity providers.

Social login platforms typically use the OAuth protocol, while enterprise single-sign on is based on the OIDC or SAML protocols.



## JSON Web Token (JWT)

A [JSON Web Token](https://jwt.io/introduction) is a type of data structure, represented as a string, that usually contains identity and authorization information about a user. It encodes information about its lifetime and is signed with cryptographic key making it tamper resistant.

Access tokens are JWTs and by inspecting the information they contain you can allow or deny access to resources. Row level security policies are based on the information present in JWTs.



## JWT signing secret

JWTs issued by Supabase are signed using the HMAC-SHA256 algorithm. The secret key used in the signing is called the JWT signing secret. You should not share this secret with someone or some thing you don't trust, nor should you post it publicly. Anyone with access to the secret can create arbitrary JWTs.



## Multi-factor authentication (MFA or 2FA)

Multi-factor authentication is the process of authenticating a user's identity by using a combination of factors: something users know, something users have or something they are.



## Nonce

Nonce means number used once. In reality though, it is a unique and difficult to guess string used to either initialize a protocol or algorithm securely, or detect abuse in various forms of replay attacks.



## OAuth

OAuth is a protocol allowing third-party applications to request and receive authorization from their users. It is typically used to implement social login, and serves as a base for enterprise single-sign on in the OIDC protocol. Applications can request different levels of access, including basic user identification information such as name, email address, and user ID.



## OIDC

OIDC stands for OpenID Connect and is a protocol that enables single-sign on for enterprises. OIDC is based on modern web technologies such as OAuth and JSON Web Tokens. It is commonly used instead of the older SAML protocol.



## One-time password (OTP)

A one-time password is a short, randomly generated and difficult to guess password or code that is sent to a device (like a phone number) or generated by a device or application.



## Password hashing function

Password hashing functions are specially-designed algorithms that allow web servers to verify a password without storing it as-is. Unlike other difficult to guess strings generated from secure random number generators, passwords are picked by users and often are easy to guess by attackers. These algorithms slow down and make it very costly for attackers to guess passwords.

There are three generally accepted password hashing functions: Argon2, bcrypt and scrypt.



## Password strength

Password strength is a measurement of how difficult a password is to guess. Simple measurement includes calculating the number of possibilities given the types of characters used in the password. For example a password of only letters has fewer variations than ones with letters and digits. Better measurements include strategies such as looking for similarity to words, phrases or already known passwords.



## PKCE

Proof Key for Code Exchange is an extension to the OAuth protocol that enables secure exchange of refresh and access tokens between an application (web app, single-page app or mobile app) and the authorization server. It is used in places where the exchange of the refresh and access token may be intercepted by third parties such as other applications running in the operating system. This is a common problem on mobile devices where the operating system may hand out URLs to other applications. This can sometimes be also exploited in single-page apps too.



## Provider refresh token

A provider refresh token is a refresh token issued by a third-party identity provider which can be used to refresh the provider token returned.



## Provider tokens

A provider token is a long-lived token issued by a third-party identity provider. These are issued by social login services (e.g., Google, Twitter, Apple, Microsoft) and uniquely identify a user on those platforms.



## Refresh token

A refresh token is a long-lived (in most cases with an indefinite lifetime) token that is meant to be stored and exchanged for a new refresh and access tokens only once. Once a refresh token is exchanged it becomes invalid, and can't be exchanged again. In practice, though, a refresh token can be exchanged multiple times but in a short time window.



## Refresh token flow

The refresh token flow is a mechanism that issues a new refresh and access token on the basis of a valid refresh token. It is used to extend authorization access for an application. An application that is being constantly used will invoke the refresh token flow just before the access token expires.



## Replay attack

A replay attack is when sensitive information is stolen or intercepted by attackers who then attempt to use it again (thus replay) in an effort to compromise a system. Commonly replay attacks can be mitigated with the proper use of nonces.



## Row level security policies (RLS)

Row level security policies are special objects within the Postgres database that limit the available operations or data returned to clients. RLS policies use information contained in a JWT to identify users and the actions and data they are allowed to perform or view.



## SAML

SAML stands for Security Assertion Markup Language and is a protocol that enables single-sign on for enterprises. SAML was invented in the early 2000s and is based on XML technology. It is the de facto standard for enabling single-sign on for enterprises, although the more recent OIDC (OpenID Connect) protocol is gaining popularity.



## Session

A session or authentication session is the concept that binds a verified user identity to a web browser. A session usually is long-lived, and can be terminated by the user logging out. An access and refresh token pair represent a session in the browser, and they are stored in local storage or as cookies.



## Single-sign on (SSO)

Single-sign on allows enterprises to centrally manage accounts and access to applications. They use identity provider software or services to organize employee information in directories and connect those accounts with applications via OIDC or SAML protocols.



## Time-based one-time password (TOTP)

A time-based one-time password is a one-time password generated at regular time intervals from a secret, usually from an application in a mobile device (e.g., Google Authenticator, 1Password).



# Realtime Architecture



Realtime is a globally distributed Elixir cluster. Clients can connect to any node in the cluster via WebSockets and send messages to any other client connected to the cluster.

Realtime is written in [Elixir](https://elixir-lang.org/), which compiles to [Erlang](https://www.erlang.org/), and utilizes many tools the [Phoenix Framework](https://www.phoenixframework.org/) provides out of the box.

<Image
  alt="Architecture"
  src={{
    light: '/docs/img/guides/platform/realtime/architecture--light.png',
    dark: '/docs/img/guides/platform/realtime/architecture--dark.png',
  }}
/>



## Elixir & Phoenix

Phoenix is fast and able to handle millions of concurrent connections.

Phoenix can handle many concurrent connections because Elixir provides lightweight processes (not OS processes) to work with.

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

Client-facing WebSocket servers need to handle many concurrent connections. Elixir & Phoenix let the Supabase Realtime cluster do this easily.



## Channels

Channels are implemented using [Phoenix Channels](https://hexdocs.pm/phoenix/channels.html) which uses [Phoenix.PubSub](https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html) with the default `Phoenix.PubSub.PG2` adapter.

The PG2 adapter utilizes Erlang [process groups](https://www.erlang.org/docs/18/man/pg2.html) to implement the PubSub model where a publisher can send messages to many subscribers.



## Global cluster

Presence is an in-memory key-value store backed by a CRDT. When a user is connected to the cluster the state of that user is sent to all connected Realtime nodes.

Broadcast lets you send a message from any connected client to a Channel. Any other client connected to that same Channel will receive that message.

This works globally. A client connected to a Realtime node in the United States can send a message to another client connected to a node in Singapore. Connect two clients to the same Realtime Channel and they'll all receive the same messages.

Broadcast is useful for getting messages to users in the same location very quickly. If a group of clients are connected to a node in Singapore, the message only needs to go to that Realtime node in Singapore and back down. If users are close to a Realtime node they'll get Broadcast messages in the time it takes to ping the cluster.

Thanks to the Realtime cluster, you (an amazing Supabase user) don't have to think about which regions your clients are connected to.

If you're using Broadcast, Presence, or streaming database changes, messages will always get to your users via the shortest path possible.



## Connecting to a database

Realtime allows you to listen to changes from your Postgres database. When a new client connects to Realtime and initializes the `postgres_changes` Realtime Extension the cluster will connect to your Postgres database and start streaming changes from a replication slot.

Realtime knows the region your database is in, and connects to it from the closest region possible.

Every Realtime region has at least two nodes so if one node goes offline the other node should reconnect and start streaming changes again.



## Broadcast from Postgres

Realtime Broadcast sends messages when changes happen in your database. Behind the scenes, Realtime creates a publication on the `realtime.messages` table. It then reads the Write-Ahead Log (WAL) file for this table, and sends a message whenever an insert happens. Messages are sent as JSON packages over WebSockets.

The `realtime.messages` table is partitioned by day. This allows old messages to be deleted performantly, by dropping old partitions. Partitions are retained for 3 days before being deleted.

Broadcast uses [Realtime Authorization](/docs/guides/realtime/authorization) by default to protect your data.



## Streaming the Write-Ahead Log

A Postgres logical replication slot is acquired when connecting to your database.

Realtime delivers changes by polling the replication slot and appending channel subscription IDs to each wal record.

Subscription IDs are Erlang processes representing underlying sockets on the cluster. These IDs are globally unique and messages to processes are routed automatically by the Erlang virtual machine.

After receiving results from the polling query, with subscription IDs appended, Realtime delivers records to those clients.



# Realtime Authorization



You can control client access to Realtime [Broadcast](/docs/guides/realtime/broadcast) and [Presence](/docs/guides/realtime/presence) by adding Row Level Security policies to the `realtime.messages` table. Each RLS policy can map to a specific action a client can take:

*   Control which clients can broadcast to a Channel
*   Control which clients can receive broadcasts from a Channel
*   Control which clients can publish their presence to a Channel
*   Control which clients can receive messages about the presence of other clients

<Admonition type="caution">
  Realtime Authorization is in Public Beta. To use Authorization for your Realtime Channels, use `supabase-js` version `v2.44.0` or later.
</Admonition>

<Admonition type="note">
  To enforce private channels you need to disable the 'Allow public access' setting in [Realtime Settings](/dashboard/project/_/realtime/settings)
</Admonition>



## How it works

Realtime uses the `messages` table in your database's `realtime` schema to generate access policies for your clients when they connect to a Channel topic.

By creating RLS policies on the `realtime.messages` table you can control the access users have to a Channel topic, and features within a Channel topic.

The validation is done when the user connects. When their WebSocket connection is established and a Channel topic is joined, their permissions are calculated based on:

*   The RLS policies on the `realtime.messages` table
*   The user information sent as part of their [Auth JWT](/docs/guides/auth/jwts)
*   The request headers
*   The Channel topic the user is trying to connect to

When Realtime generates a policy for a client it performs a query on the `realtime.messages` table and then rolls it back. Realtime does not store any messages in your `realtime.messages` table.

Using Realtime Authorization involves two steps:

*   In your database, create RLS policies on the `realtime.messages`
*   In your client, instantiate the Realtime Channel with the `config` option `private: true`

<Admonition type="caution">
  Increased RLS complexity can impact database performance and connection time, leading to higher connection latency and decreased join rates.
</Admonition>



## Accessing request information


### `realtime.topic`

You can use the `realtime.topic` helper function when writing RLS policies. It returns the Channel topic the user is attempting to connect to.

```sql
create policy "authenticated can read all messages on topic"
on "realtime"."messages"
for select
to authenticated
using (
  (select realtime.topic()) = 'room-1'
);
```


### JWT claims

The user claims can be accessed using the `current_setting` function. The claims are available as a JSON object in the `request.jwt.claims` setting.

```sql
create policy "authenticated with supabase.io email can read all"
on "realtime"."messages"
for select
to authenticated
using (
  -- Only users with the email claim ending with @supabase.io
  (((current_setting('request.jwt.claims'))::json ->> 'email') ~~ '%@supabase.io')
);
```



## Examples

The following examples use this schema:

```sql
create table public.rooms (
    id bigint generated by default as identity primary key,
    topic text not null unique
);

alter table public.rooms enable row level security;

create table public.profiles (
  id uuid not null references auth.users on delete cascade,
  email text NOT NULL,

  primary key (id)
);

alter table public.profiles enable row level security;

create table public.rooms_users (
  user_id uuid references auth.users (id),
  room_topic text references public.rooms (topic),
  created_at timestamptz default current_timestamp
);

alter table public.rooms_users enable row level security;
```


### Broadcast

The `extension` field on the `realtime.messages` table records the message type. For Broadcast messages, the value of `realtime.messages.extension` is `broadcast`. You can check for this in your RLS policies.


#### Allow a user to join (and read) a Broadcast topic

To join a Broadcast Channel, a user must have at least one read or write permission on the Channel topic.

Here, we allow reads (`select`s) for users who are linked to the requested topic within the relationship table `public.room_users`:

```sql
create policy "authenticated can receive broadcast"
on "realtime"."messages"
for select
to authenticated
using (
exists (
    select
      user_id
    from
      rooms_users
    where
      user_id = (select auth.uid())
      and topic = (select realtime.topic())
      and realtime.messages.extension in ('broadcast')
  )
);
```

Then, to join a topic with RLS enabled, instantiate the Channel with the `private` option set to `true`.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```javascript
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const channel = supabase.channel('room-1', {
      config: { private: true },
    })

    channel
      .on('broadcast', { event: 'test' }, (payload) => console.log(payload))
      .subscribe((status, err) => {
        if (status === 'SUBSCRIBED') {
          console.log('Connected!')
        } else {
          console.error(err)
        }
      })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final channel = supabase.channel(
      'room-1',
      opts: const RealtimeChannelConfig(private: true),
    );

    channel
        .onBroadcast(event: 'test', callback: (payload) => print(payload))
        .subscribe((status, err) {
      if (status == RealtimeSubscribeStatus.subscribed) {
        print('Connected!');
      } else {
        print(err);
      }
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let channel = supabase.channel("room-1") {
      $0.isPrivate = true
    }

    Task {
      for await payload in channel.broadcastStream(event: "test") {
        print(payload)
      }
    }

    await channel.subscribe()
    print("Connected!")
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val channel = supabase.channel("room-1") {
        isPrivate = true
    }
    channel.broadcastFlow<MyPayload>(event = "test").onEach {
        println(it)
    }.launchIn(scope) // launch in your coroutine scope
    channel.subscribe(blockUntilSubscribed = true)
    println("Connected!")
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```py
    channel = realtime.channel(
      "room-1", {"config": {"private": True}}
    )

    await channel.on_broadcast(
      "test", callback=lambda payload: print(payload)
    ).subscribe(
      lambda state, err: (
        print("Connected")
        if state == RealtimeSubscribeStates.SUBSCRIBED
        else print(err)
      )
    )
    ```
  </TabPanel>
</Tabs>


#### Allow a user to send a Broadcast message

To authorize sending Broadcast messages, create a policy for `insert` where the value of `realtime.messages.extension` is `broadcast`.

Here, we allow writes (sends) for users who are linked to the requested topic within the relationship table `public.room_users`:

```sql
create policy "authenticated can send broadcast on topic"
on "realtime"."messages"
for insert
to authenticated
with check (
  exists (
    select
      user_id
    from
      rooms_users
    where
      user_id = (select auth.uid())
      and topic = (select realtime.topic())
      and realtime.messages.extension in ('broadcast')
  )
);
```


### Presence

The `extension` field on the `realtime.messages` table records the message type. For Presence messages, the value of `realtime.messages.extension` is `presence`. You can check for this in your RLS policies.


#### Allow users to listen to Presence messages on a Channel

Create a policy for `select` on `realtime.messages` where `realtime.messages.extension` is `presence`.

```sql
create policy "authenticated can listen to presence in topic"
on "realtime"."messages"
for select
to authenticated
using (
  exists (
    select
      user_id
    from
      rooms_users
    where
      user_id = (select auth.uid())
      and topic = (select realtime.topic())
      and realtime.messages.extension in ('presence')
  )
);
```


#### Allow users to send Presence messages on a channel

To update the Presence status for a user create a policy for `insert` on `realtime.messages` where the value of `realtime.messages.extension` is `presence`.

```sql
create policy "authenticated can track presence on topic"
on "realtime"."messages"
for insert
to authenticated
with check (
  exists (
    select
      user_id
    from
      rooms_users
    where
      user_id = (select auth.uid())
      and name = (select realtime.topic())
      and realtime.messages.extension in ('presence')
  )
);
```


### Presence and Broadcast

Authorize both Presence and Broadcast by including both extensions in the `where` filter.


#### Broadcast and Presence read

Authorize Presence and Broadcast read in one RLS policy.

```sql
create policy "authenticated can listen to broadcast and presence on topic"
on "realtime"."messages"
for select
to authenticated
using (
  exists (
    select
      user_id
    from
      rooms_users
    where
      user_id = (select auth.uid())
      and topic = (select realtime.topic())
      and realtime.messages.extension in ('broadcast', 'presence')
  )
);
```


#### Broadcast and Presence write

Authorize Presence and Broadcast write in one RLS policy.

```sql
create policy "authenticated can send broadcast and presence on topic"
on "realtime"."messages"
for insert
to authenticated
with check (
  exists (
    select
      user_id
    from
      rooms_users
    where
      user_id = (select auth.uid())
      and name = (select realtime.topic())
      and realtime.messages.extension in ('broadcast', 'presence')
  )
);
```



## Interaction with Postgres Changes

Realtime Postgres Changes are separate from Channel authorization. The `private` Channel option does not apply to Postgres Changes.

When using Postgres Changes with RLS, database records are sent only to clients who are allowed to read them based on your RLS policies.



## Updating RLS policies

Client access policies are cached for the duration of the connection. Your database is not queried for every Channel message.

Realtime updates the access policy cache for a client based on your RLS policies when:

*   A client connects to Realtime and subscribes to a Channel
*   A new JWT is sent to Realtime from a client via the [`access_token` message](/docs/guides/realtime/protocol#access-token)

If a new JWT is never received on the Channel, the client will be disconnected when the JWT expires.

Make sure to keep the JWT expiration window short.



# Benchmarks

Scalability Benchmarks for Supabase Realtime.

This guide explores the scalability of Realtime's features: Broadcast, Presence, and Postgres Changes.



## Methodology

*   The benchmarks are conducted using k6, an open-source load testing tool, against a Realtime Cluster deployed on AWS.
*   The cluster configurations use 2-6 nodes, tested in both single-region and multi-region setups, all connected to a single Supabase project.
*   The load generators (k6 servers) are deployed on AWS to minimize network latency impact on the results.
*   Tests are executed with a full load from the start without warm-up runs.

The metrics collected include: message throughput, latency percentiles, CPU and memory utilization, and connection success rates. Note that performance in production environments may vary based on factors such as network conditions, hardware specifications, and specific usage patterns.



## Workloads

The proposed workloads are designed to demonstrate Supabase Realtime's throughput and scalability. These benchmarks focus on core functionality and common usage patterns. The benchmarking results include the following workloads:

1.  **Broadcast Performance**
2.  **Payload Size Impact on Broadcast**
3.  **Large-Scale Broadcasting**
4.  **Authentication and New Connection Rate**
5.  **Database Events**



## Results


### Broadcast: Using WebSockets

This workload evaluates the system's capacity to handle multiple concurrent WebSocket connections and sending Broadcast messages via the WebSocket. Each virtual user (VU) in the test:

*   Establishes and maintains a WebSocket connection
*   Joins two distinct channels:
    *   An echo channel (1 user per channel) for direct message reflection
    *   A broadcast channel (6 users per channel) for group communication
*   Generates traffic by sending 2 messages per second to each joined channel for 10 minutes

![Broadcast Performance](/docs/img/guides/realtime/broadcast-performance.png)

| Metric              | Value                   |
| ------------------- | ----------------------- |
| Concurrent Users    | 32\_000                 |
| Total Channel Joins | 64\_000                 |
| Message Throughput  | 224\_000 msgs/sec       |
| Median Latency      | 6 ms                    |
| Latency (p95)       | 28 ms                   |
| Latency (p99)       | 213 ms                  |
| Data Received       | 6.4 MB/s (7.9 GB total) |
| Data Sent           | 23 KB/s (28 MB total)   |
| New Connection Rate | 320 conn/sec            |
| Channel Join Rate   | 640 joins/sec           |


### Broadcast: Using the database

This workload evaluates the system's capacity to send Broadcast messages from the database using the `realtime.broadcast_changes` function. Each virtual user (VU) in the test:

*   Establishes and maintains a WebSocket connection
*   Joins a distinct channel:
    *   A single channel (100 users per channel) for group communication
*   Database has a trigger set to run `realtime.broadcast_changes` on every insert
*   Database triggers 10\_000 inserts per second

![Broadcast from Database Performance](/docs/img/guides/realtime/broadcast-from-database-performance.png)

| Metric              | Value                  |
| ------------------- | ---------------------- |
| Concurrent Users    | 80\_000                |
| Total Channel Joins | 160\_000               |
| Message Throughput  | 10\_000 msgs/sec       |
| Median Latency      | 46 ms                  |
| Latency (p95)       | 132 ms                 |
| Latency (p99)       | 159 ms                 |
| Data Received       | 1.7 MB/s (42 GB total) |
| Data Sent           | 0.4 MB/s (4 GB total)  |
| New Connection Rate | 2000 conn/sec          |
| Channel Join Rate   | 4000 joins/sec         |


### Broadcast: Impact of payload size

This workload tests the system's performance with different message payload sizes to understand how data volume affects throughput and latency. Each virtual user (VU) follows the same connection pattern as the broadcast test, but with varying message sizes:

*   Establishes and maintains a WebSocket connection
*   Joins two distinct channels:
    *   An echo channel (1 user per channel) for direct message reflection
    *   A broadcast channel (6 users per channel) for group communication
*   Sends messages with payloads of 1KB, 10KB, and 50KB
*   Generates traffic by sending 2 messages per second to each joined channel for 5 minutes


#### 1KB payload

![1KB Payload Broadcast Performance](/docs/img/guides/realtime/payload-size-1kb.png)


#### 10KB payload

![10KB Payload Broadcast Performance](/docs/img/guides/realtime/payload-size-10kb.png)


#### 50KB payload

![50KB Payload Broadcast Performance](/docs/img/guides/realtime/payload-size-50kb-small.png)

| Metric             | 1KB Payload         | 10KB Payload      | 50KB Payload       | 50KB Payload (Reduced Load) |
| ------------------ | ------------------- | ----------------- | ------------------ | --------------------------- |
| Concurrent Users   | 4\_000              | 4\_000            | 4\_000             | 2\_000                      |
| Message Throughput | 28\_000 msgs/sec    | 28\_000 msgs/sec  | 28\_000 msgs/sec   | 14\_000 msgs/sec            |
| Median Latency     | 13 ms               | 16 ms             | 27 ms              | 19 ms                       |
| Latency (p95)      | 36 ms               | 42 ms             | 81 ms              | 39 ms                       |
| Latency (p99)      | 85 ms               | 93 ms             | 146 ms             | 82 ms                       |
| Data Received      | 31.2 MB/s (10.4 GB) | 268 MB/s (72 GB)  | 1284 MB/s (348 GB) | 644 MB/s (176 GB)           |
| Data Sent          | 9.2 MB/s (3.1 GB)   | 76 MB/s (20.8 GB) | 384 MB/s (104 GB)  | 192 MB/s (52 GB)            |

> Note: The final column shows results with reduced load (2,000 users) for the 50KB payload test, demonstrating how the system performs with larger payloads under different concurrency levels.


### Broadcast: Scalability scenarios

This workload demonstrates Realtime's capability to handle high-scale scenarios with a large number of concurrent users and broadcast channels. The test simulates a scenario where each user participates in group communications with periodic message broadcasts. Each virtual user (VU):

*   Establishes and maintains a WebSocket connection (30-120 minutes)
*   Joins 2 broadcast channels
*   Sends 1 message per minute to each joined channel
*   Each message is broadcast to 100 other users

![Large Broadcast Performance](/docs/img/guides/realtime/broadcast-large.png)

| Metric              | Value              |
| ------------------- | ------------------ |
| Concurrent Users    | 250\_000           |
| Total Channel Joins | 500\_000           |
| Users per Channel   | 100                |
| Message Throughput  | >800\_000 msgs/sec |
| Median Latency      | 58 ms              |
| Latency (p95)       | 279 ms             |
| Latency (p99)       | 508 ms             |
| Data Received       | 68 MB/s (600 GB)   |
| Data Sent           | 0.64 MB/s (5.7 GB) |


### Realtime Auth

This workload demonstrates Realtime's capability to handle large amounts of new connections per second and channel joins per second with Authentication Row Level Security (RLS) enabled for these channels. The test simulates a scenario where large volumes of users connect to realtime and participate in auth protected communications. Each virtual user (VU):

*   Establishes and maintains a WebSocket connection (2.5 minutes)
*   Joins 2 broadcast channels
*   Sends 1 message per minute to each joined channel
*   Each message is broadcast to 100 other users

![Broadcast Auth Performance](/docs/img/guides/realtime/broadcast-auth.png)

| Metric              | Value              |
| ------------------- | ------------------ |
| Concurrent Users    | 50\_000            |
| Total Channel Joins | 100\_000           |
| Users per Channel   | 100                |
| Message Throughput  | >150\_000 msgs/sec |
| New Connection Rate | 500 conn/sec       |
| Channel Join Rate   | 1000 joins/sec     |
| Median Latency      | 19 ms              |
| Latency (p95)       | 49 ms              |
| Latency (p99)       | 96 ms              |


### Postgres Changes

Realtime systems usually require forethought because of their scaling dynamics. For the `Postgres Changes` feature, every change event must be checked to see if the subscribed user has access. For instance, if you have 100 users subscribed to a table where you make a single insert, it will then trigger 100 "reads": one for each user.

There can be a database bottleneck which limits message throughput. If your database cannot authorize the changes rapidly enough, the changes will be delayed until you receive a timeout.

Database changes are processed on a single thread to maintain the change order. That means compute upgrades don't have a large effect on the performance of Postgres change subscriptions. You can estimate the expected maximum throughput for your database below.

If you are using Postgres Changes at scale, you should consider using a separate "public" table without RLS and filters. Alternatively, you can use Realtime server-side only and then re-stream the changes to your clients using a Realtime Broadcast.

Enter your database settings to estimate the maximum throughput for your instance:

<RealtimeLimitsEstimator />

Don't forget to run your own benchmarks to make sure that the performance is acceptable for your use case.

Supabase continues to make improvements to Realtime's Postgres Changes. If you are uncertain about your use case performance, reach out using the [Support Form](/dashboard/support/new). The support team can advise on the best solution for each use-case.



# Broadcast

Send low-latency messages using the client libs, REST, or your Database.

You can use Realtime Broadcast to send low-latency messages between users. Messages can be sent using the client libraries, REST APIs, or directly from your database.



## How Broadcast works

The way Broadcast works changes based on the channel you are using:

*   From REST API will receive an HTTP request which then will be sent via WebSocket to connected clients
*   From Client libraries we have an established WebSocket connection and we use that to send a message to the server which then will be sent via WebSocket to connected clients
*   From Database we add a new entry to `realtime.messages` where we have logical replication set to listen for changes which then will be sent via WebSocket to connected clients

<Admonition type="note">
  The public flag (the last argument in `realtime.send(payload, event, topic, is_private))` only affects who can subscribe to the topic not who can read messages from the database.

  *   Public (false) → Anyone can subscribe to that topic without authentication
  *   Private (true) → Only authenticated clients can subscribe to that topic

  However, regardless of whether it's public or private, the Realtime service connects to your database as the authenticated Supabase Admin role.
</Admonition>

For Authorization we do insert a message and try to read it and then we it back as way to verify that the RLS policies set by the user are being respected by the user joining the channel but this messages won't be sent to the user. You can read more about it in the [Authorization](/docs/guides/realtime/authorization) docs



## Subscribe to messages

You can use the Supabase client libraries to receive Broadcast messages.


### Initialize the client

Go to your Supabase project's [API Settings](/dashboard/project/_/settings/api) and grab the `URL` and `anon` public API key.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'

    const SUPABASE_URL = 'https://<project>.supabase.co'
    const SUPABASE_KEY = '<sb_publishable_... or anon key>'

    const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    import 'package:supabase_flutter/supabase_flutter.dart';

    void main() async {
      Supabase.initialize(
        url: 'https://<project>.supabase.co',
        anonKey: '<sb_publishable_... or anon key>',
      );
      runApp(MyApp());
    }

    final supabase = Supabase.instance.client;
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Supabase

    let SUPABASE_URL = "https://<project>.supabase.co"
    let SUPABASE_KEY = "<sb_publishable_... or anon key>"

    let supabase = SupabaseClient(supabaseURL: URL(string: SUPABASE_URL)!, supabaseKey: SUPABASE_KEY)
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val supabaseUrl = "https://<project>.supabase.co"
    val supabaseKey = "<sb_publishable_... or anon key>"
    val supabase = createSupabaseClient(supabaseUrl, supabaseKey) {
        install(Realtime)
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    import asyncio
    from supabase import acreate_client

    URL = "https://<project>.supabase.co"
    KEY = "<sb_publishable_... or anon key>"

    async def create_supabase():
      supabase = await acreate_client(URL, KEY)
      return supabase
    ```
  </TabPanel>
</Tabs>


### Receiving Broadcast messages

You can provide a callback for the `broadcast` channel to receive messages. This example will receive any `broadcast` messages that are sent to `test-channel`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    {/* prettier-ignore */}

    ```js
    // @noImplicitAny: false
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://<project>.supabase.co', '<sb_publishable_... or anon key>')

    // ---cut---
    // Join a room/topic. Can be anything except for 'realtime'.
    const myChannel = supabase.channel('test-channel')

    // Simple function to log any messages we receive
    function messageReceived(payload) {
      console.log(payload)
    }

    // Subscribe to the Channel
    myChannel
      .on(
        'broadcast',
        { event: 'shout' }, // Listen for "shout". Can be "*" to listen to all events
        (payload) => messageReceived(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    {/* prettier-ignore */}

    ```dart
    final myChannel = supabase.channel('test-channel');

    // Simple function to log any messages we receive
    void messageReceived(payload) {
      print(payload);
    }

    // Subscribe to the Channel
    myChannel
        .onBroadcast(
            event: 'shout', // Listen for "shout". Can be "*" to listen to all events
            callback: (payload) => messageReceived(payload)
        )
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("test-channel")

    // Listen for broadcast messages
    let broadcastStream = await myChannel.broadcast(event: "shout") // Listen for "shout". Can be "*" to listen to all events

    await myChannel.subscribe()

    for await event in broadcastStream {
      print(event)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    {/* prettier-ignore */}

    ```kotlin
    val myChannel = supabase.channel("test-channel")

    / Listen for broadcast messages
    val broadcastFlow: Flow<JsonObject> = myChannel
        .broadcastFlow<JsonObject>("shout") // Listen for "shout". Can be "*" to listen to all events
        .onEach { println(it) }
        .launchIn(yourCoroutineScope) // you can also use .collect { } here

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    <Admonition type="note">
      In the following Realtime examples, certain methods are awaited. These should be enclosed within an `async` function.
    </Admonition>

    {/* prettier-ignore */}

    ```python
    # Join a room/topic. Can be anything except for 'realtime'.
    my_channel = supabase.channel('test-channel')

    # Simple function to log any messages we receive
    def message_received(payload):
      print(f"Broadcast received: {payload}")

    # Subscribe to the Channel
    await my_channel
      .on_broadcast('shout', message_received) # Listen for "shout". Can be "*" to listen to all events
      .subscribe()
    ```
  </TabPanel>
</Tabs>



## Send messages


### Broadcast using the client libraries

You can use the Supabase client libraries to send Broadcast messages.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    {/* prettier-ignore */}

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const myChannel = supabase.channel('test-channel')

    /**
     * Sending a message before subscribing will use HTTP
     */
    myChannel
      .send({
        type: 'broadcast',
        event: 'shout',
        payload: { message: 'Hi' },
      })
      .then((resp) => console.log(resp))


    /**
     * Sending a message after subscribing will use Websockets
     */
    myChannel.subscribe((status) => {
      if (status !== 'SUBSCRIBED') {
        return null
      }

      myChannel.send({
        type: 'broadcast',
        event: 'shout',
        payload: { message: 'Hi' },
      })
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    {/* prettier-ignore */}

    ```dart
    final myChannel = supabase.channel('test-channel');

    // Sending a message before subscribing will use HTTP
    final res = await myChannel.sendBroadcastMessage(
      event: "shout",
      payload: { 'message': 'Hi' },
    );
    print(res);

    // Sending a message after subscribing will use Websockets
    myChannel.subscribe((status, error) {
      if (status != RealtimeSubscribeStatus.subscribed) {
        return;
      }

      myChannel.sendBroadcastMessage(
        event: 'shout',
        payload: { 'message': 'hello, world' },
      );
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    {/* prettier-ignore */}

    ```swift
    let myChannel = await supabase.channel("test-channel") {
      $0.broadcast.acknowledgeBroadcasts = true
    }

    // Sending a message before subscribing will use HTTP
    await myChannel.broadcast(event: "shout", message: ["message": "HI"])

    // Sending a message after subscribing will use Websockets
    await myChannel.subscribe()
    try await myChannel.broadcast(
        event: "shout",
        message: YourMessage(message: "hello, world!")
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("test-channel") {
      broadcast {
        acknowledgeBroadcasts = true
      }
    }

    // Sending a message before subscribing will use HTTP
    myChannel.broadcast(event = "shout", buildJsonObject {
      put("message", "Hi")
    })

    // Sending a message after subscribing will use Websockets
    myChannel.subscribe(blockUntilSubscribed = true)
    channelB.broadcast(
      event = "shout",
      payload = YourMessage(message = "hello, world!")
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    <Admonition type="note">
      When an asynchronous method needs to be used within a synchronous context, such as the callback for `.subscribe()`, utilize `asyncio.create_task()` to schedule the coroutine. This is why the [initialize the client](#initialize-the-client) example includes an import of `asyncio`.
    </Admonition>

    {/* prettier-ignore */}

    ```python
    my_channel = supabase.channel('test-channel')

    # Sending a message after subscribing will use Websockets
    def on_subscribe(status, err):
      if status != RealtimeSubscribeStates.SUBSCRIBED:
        return

      asyncio.create_task(my_channel.send_broadcast(
        'shout',
        { "message": 'hello, world' },
      ))

    await my_channel.subscribe(on_subscribe)
    ```
  </TabPanel>
</Tabs>

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### Broadcast from the Database

<Admonition type="caution">
  This feature is in Public Beta. [Submit a support ticket](https://supabase.help) if you have any issues.
</Admonition>

<Admonition type="note">
  All the messages sent using Broadcast from the Database are stored in `realtime.messages` table and will be deleted after 3 days.
</Admonition>

You can send messages directly from your database using the `realtime.send()` function:

{/* prettier-ignore */}

```sql
select
  realtime.send(
    jsonb_build_object('hello', 'world'), -- JSONB Payload
    'event', -- Event name
    'topic', -- Topic
    false -- Public / Private flag
  );
```

<Admonition type="note">
  The realtime.send function in the database includes a flag that determines whether the broadcast is private or public, and client channels also have the same configuration. For broadcasts to work correctly, these settings must match a public broadcast will only reach public channels, and a private broadcast will only reach private ones.

  By default, all database broadcasts are private, meaning clients must authenticate to receive them. If the database sends a public message but the client subscribes to a private channel, the message won't be delivered since private channels only accept signed, authenticated messages.
</Admonition>

It's a common use case to broadcast messages when a record is created, updated, or deleted. We provide a helper function specific to this use case, `realtime.broadcast_changes()`. For more details, check out the [Subscribing to Database Changes](/docs/guides/realtime/subscribing-to-database-changes) guide.


### Broadcast using the REST API

You can send a Broadcast message by making an HTTP request to Realtime servers.

<Tabs scrollable size="small" type="underlined" defaultActiveId="curl" queryGroup="http">
  <TabPanel id="curl" label="cURL">
    {/* prettier-ignore */}

    ```bash
    curl -v \
    -H 'apikey: <SUPABASE_TOKEN>' \
    -H 'Content-Type: application/json' \
    --data-raw '{
      "messages": [
        {
          "topic": "test",
          "event": "event",
          "payload": { "test": "test" }
        }
      ]
    }' \
    'https://<PROJECT_REF>.supabase.co/realtime/v1/api/broadcast'
    ```
  </TabPanel>

  <TabPanel id="POST" label="POST">
    {/* prettier-ignore */}

    ```bash
    POST /realtime/v1/api/broadcast HTTP/1.1
    Host: {PROJECT_REF}.supabase.co
    Content-Type: application/json
    apikey: {SUPABASE_TOKEN}
    {
      "messages": [
        {
          "topic": "test",
          "event": "event",
          "payload": {
            "test": "test"
          }
        }
      ]
    }
    ```
  </TabPanel>
</Tabs>



## Broadcast options

You can pass configuration options while initializing the Supabase Client.


### Self-send messages

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `self` parameter to `true`.

    {/* prettier-ignore */}

    ```js
    const myChannel = supabase.channel('room-2', {
      config: {
        broadcast: { self: true },
      },
    })

    myChannel.on(
      'broadcast',
      { event: 'test-my-messages' },
      (payload) => console.log(payload)
    )

    myChannel.subscribe((status) => {
      if (status !== 'SUBSCRIBED') { return }
      myChannel.send({
        type: 'broadcast',
        event: 'test-my-messages',
        payload: { message: 'talking to myself' },
      })
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `self` parameter to `true`.

    ```dart
    final myChannel = supabase.channel(
      'room-2',
      opts: const RealtimeChannelConfig(
        self: true,
      ),
    );

    myChannel.onBroadcast(
      event: 'test-my-messages',
      callback: (payload) => print(payload),
    );

    myChannel.subscribe((status, error) {
      if (status != RealtimeSubscribeStatus.subscribed) return;
      // channelC.send({
      myChannel.sendBroadcastMessage(
        event: 'test-my-messages',
        payload: {'message': 'talking to myself'},
      );
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `receiveOwnBroadcasts` parameter to `true`.

    ```swift
    let myChannel = await supabase.channel("room-2") {
      $0.broadcast.receiveOwnBroadcasts = true
    }

    let broadcastStream = await myChannel.broadcast(event: "test-my-messages")

    await myChannel.subscribe()

    try await myChannel.broadcast(
        event: "test-my-messages",
        payload: YourMessage(
            message: "talking to myself"
        )
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `receiveOwnBroadcasts` parameter to `true`.

    ```kotlin
    val myChannel = supabase.channel("room-2") {
        broadcast {
            receiveOwnBroadcasts = true
        }
    }

    val broadcastFlow: Flow<JsonObject> = myChannel.broadcastFlow<JsonObject>("test-my-messages")
        .onEach {
            println(it)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe(blockUntilSubscribed = true) //You can also use the myChannel.status flow instead, but this parameter will block the coroutine until the status is joined.

    myChannel.broadcast(
        event = "test-my-messages",
        payload = YourMessage(
            message = "talking to myself"
        )
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    <Admonition type="note">
      When an asynchronous method needs to be used within a synchronous context, such as the callback for `.subscribe()`, utilize `asyncio.create_task()` to schedule the coroutine. This is why the [initialize the client](#initialize-the-client) example includes an import of `asyncio`.
    </Admonition>

    By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `self` parameter to `True`.

    ```python
    # Join a room/topic. Can be anything except for 'realtime'.
    my_channel = supabase.channel('room-2', {"config": {"broadcast": {"self": True}}})

    my_channel.on_broadcast(
      'test-my-messages',
      lambda payload: print(payload)
    )

    def on_subscribe(status, err):
      if status != RealtimeSubscribeStates.SUBSCRIBED:
        return

      # Send a message once the client is subscribed
      asyncio.create_task(channel_b.send_broadcast(
        'test-my-messages',
        { "message": 'talking to myself' },
      ))

    my_channel.subscribe(on_subscribe)
    ```
  </TabPanel>
</Tabs>


### Acknowledge messages

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    You can confirm that the Realtime servers have received your message by setting Broadcast's `ack` config to `true`.

    {/* prettier-ignore */}

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const myChannel = supabase.channel('room-3', {
      config: {
        broadcast: { ack: true },
      },
    })

    myChannel.subscribe(async (status) => {
      if (status !== 'SUBSCRIBED') { return }

      const serverResponse = await myChannel.send({
        type: 'broadcast',
        event: 'acknowledge',
        payload: {},
      })

      console.log('serverResponse', serverResponse)
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final myChannel = supabase.channel('room-3',opts: const RealtimeChannelConfig(
      ack: true,
    ),

    );

    myChannel.subscribe( (status, error) async {
      if (status != RealtimeSubscribeStatus.subscribed) return;

      final serverResponse = await myChannel.sendBroadcastMessage(

        event: 'acknowledge',
        payload: {},
      );

      print('serverResponse: $serverResponse');
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    You can confirm that Realtime received your message by setting Broadcast's `acknowledgeBroadcasts` config to `true`.

    ```swift
    let myChannel = await supabase.channel("room-3") {
      $0.broadcast.acknowledgeBroadcasts = true
    }

    await myChannel.subscribe()

    await myChannel.broadcast(event: "acknowledge", message: [:])
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    By default, broadcast messages are only sent to other clients. You can broadcast messages back to the sender by setting Broadcast's `acknowledgeBroadcasts` parameter to `true`.

    ```kotlin
    val myChannel = supabase.channel("room-2") {
        broadcast {
            acknowledgeBroadcasts = true
        }
    }

    myChannel.subscribe(blockUntilSubscribed = true) //You can also use the myChannel.status flow instead, but this parameter will block the coroutine until the status is joined.

    myChannel.broadcast(event = "acknowledge", buildJsonObject {  })
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    Unsupported in Python yet.
  </TabPanel>
</Tabs>

Use this to guarantee that the server has received the message before resolving `channelD.send`'s promise. If the `ack` config is not set to `true` when creating the channel, the promise returned by `channelD.send` will resolve immediately.


### Send messages using REST calls

You can also send a Broadcast message by making an HTTP request to Realtime servers. This is useful when you want to send messages from your server or client without having to first establish a WebSocket connection.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="note">
      This is currently available only in the Supabase JavaScript client version 2.37.0 and later.
    </Admonition>

    ```js
    const channel = supabase.channel('test-channel')

    // No need to subscribe to channel

    channel
      .send({
        type: 'broadcast',
        event: 'test',
        payload: { message: 'Hi' },
      })
      .then((resp) => console.log(resp))

    // Remember to clean up the channel

    supabase.removeChannel(channel)

    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    // No need to subscribe to channel

    final channel = supabase.channel('test-channel');
    final res = await channel.sendBroadcastMessage(
      event: "test",
      payload: {
        'message': 'Hi',
      },
    );
    print(res);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("room-2") {
      $0.broadcast.acknowledgeBroadcasts = true
    }

    // No need to subscribe to channel

    await myChannel.broadcast(event: "test", message: ["message": "HI"])
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("room-2") {
        broadcast {
            acknowledgeBroadcasts = true
        }
    }

    // No need to subscribe to channel

    myChannel.broadcast(event = "test", buildJsonObject {
        put("message", "Hi")
    })
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    Unsupported in Python yet.
  </TabPanel>
</Tabs>



## Trigger broadcast messages from your database


### How it works

Broadcast Changes allows you to trigger messages from your database. To achieve it Realtime is directly reading your WAL (Write Append Log) file using a publication against the `realtime.messages` table so whenever a new insert happens a message is sent to connected users.

It uses partitioned tables per day which allows the deletion your previous messages in a performant way by dropping the physical tables of this partitioned table. Tables older than 3 days old are deleted.

Broadcasting from the database works like a client-side broadcast, using WebSockets to send JSON packages. [Realtime Authorization](/docs/guides/realtime/authorization) is required and enabled by default to protect your data.

The database broadcast feature provides two functions to help you send messages:

*   `realtime.send` will insert a message into realtime.messages without a specific format.
*   `realtime.broadcast_changes` will insert a message with the required fields to emit database changes to clients. This helps you set up triggers on your tables to emit changes.


### Broadcasting a message from your database

The `realtime.send` function provides the most flexibility by allowing you to broadcast messages from your database without a specific format. This allows you to use database broadcast for messages that aren't necessarily tied to the shape of a Postgres row change.

```sql
SELECT realtime.send (
	'{}'::jsonb, -- JSONB Payload
	'event', -- Event name
	'topic', -- Topic
	FALSE -- Public / Private flag
);
```


### Broadcast record changes


#### Setup realtime authorization

Realtime Authorization is required and enabled by default. To allow your users to listen to messages from topics, create a RLS (Row Level Security) policy:

```sql
CREATE POLICY "authenticated can receive broadcasts"
ON "realtime"."messages"
FOR SELECT
TO authenticated
USING ( true );

```

See the [Realtime Authorization](/docs/guides/realtime/authorization) docs to learn how to set up more specific policies.


#### Set up trigger function

First, set up a trigger function that uses `realtime.broadcast_changes` to insert an event whenever it is triggered. The event is set up to include data on the schema, table, operation, and field changes that triggered it.

For this example use case, we want to have a topic with the name `topic:<record id>` to which we're going to broadcast events.

```sql
CREATE OR REPLACE FUNCTION public.your_table_changes()
RETURNS trigger
SECURITY DEFINER SET search_path = ''
AS $$
BEGIN
    PERFORM realtime.broadcast_changes(
	    'topic:' || NEW.id::text,   -- topic
		   TG_OP,                          -- event
		   TG_OP,                          -- operation
		   TG_TABLE_NAME,                  -- table
		   TG_TABLE_SCHEMA,                -- schema
		   NEW,                            -- new record
		   OLD                             -- old record
		);
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

Of note are the Postgres native trigger special variables used:

*   `TG_OP` - the operation that triggered the function
*   `TG_TABLE_NAME` - the table that caused the trigger
*   `TG_TABLE_SCHEMA` - the schema of the table that caused the trigger invocation
*   `NEW` - the record after the change
*   `OLD` - the record before the change

You can read more about them in this [guide](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-DML-TRIGGER).


#### Set up trigger

Next, set up a trigger so the function runs whenever your target table has a change.

```sql
CREATE TRIGGER broadcast_changes_for_your_table_trigger
AFTER INSERT OR UPDATE OR DELETE ON public.your_table
FOR EACH ROW
EXECUTE FUNCTION your_table_changes ();
```

As you can see, it will be broadcasting all operations so our users will receive events when records are inserted, updated or deleted from `public.your_table` .


#### Listen on client side

Finally, client side will requires to be set up to listen to the topic `topic:<record id>` to receive the events.

```jsx
const gameId = 'id'
await supabase.realtime.setAuth() // Needed for Realtime Authorization
const changes = supabase
  .channel(`topic:${gameId}`)
  .on('broadcast', { event: 'INSERT' }, (payload) => console.log(payload))
  .on('broadcast', { event: 'UPDATE' }, (payload) => console.log(payload))
  .on('broadcast', { event: 'DELETE' }, (payload) => console.log(payload))
  .subscribe()
```



## Broadcast replay

<Admonition type="caution">
  This feature is currently in Public Alpha. If you have any issues [submit a support ticket](https://supabase.help).
</Admonition>


### How it works

Broadcast Replay enables **private** channels to access messages that were sent earlier. Only messages published via [Broadcast From the Database](#broadcast-from-the-database) are available for replay.

You can configure replay with the following options:

*   **`since`** (Required): The epoch timestamp in milliseconds (e.g., `1697472000000`), specifying the earliest point from which messages should be retrieved.
*   **`limit`** (Optional): The number of messages to return. This must be a positive integer, with a maximum value of 25.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="note">
      This is currently available only in the Supabase JavaScript client version 2.74.0 and later.
    </Admonition>

    ```js
    const config = {
      private: true,
      broadcast: {
        replay: {
          since: 1697472000000, // Unix timestamp in milliseconds
          limit: 10
        }
      }
    }
    const channel = supabase.channel('main:room', { config })

    // Broadcast callback receives meta field
    channel.on('broadcast', { event: 'position' }, (payload) => {
      if (payload?.meta?.replayed) {
        console.log('Replayed message: ', payload)
      } else {
        console.log('This is a new message', payload)
      }
      // ...
    })
    .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    <Admonition type="note">
      This is currently available only in the Supabase Dart client version 2.10.0 and later.
    </Admonition>

    ```dart
    // Configure broadcast with replay
    final channel = supabase.channel(
      'my-channel',
      RealtimeChannelConfig(
        self: true,
        ack: true,
        private: true,
        replay: ReplayOption(
          since: 1697472000000, // Unix timestamp in milliseconds
          limit: 25,
        ),
      ),
    );

    // Broadcast callback receives meta field
    channel.onBroadcast(
      event: 'position',
      callback: (payload) {
        final meta = payload['meta'] as Map<String, dynamic>?;
        if (meta?['replayed'] == true) {
          print('Replayed message: ${meta?['id']}');
        }
      },
    ).subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    <Admonition type="note">
      This is currently available only in the Supabase Swift client version 2.34.0 and later.
    </Admonition>

    ```swift
    // Configure broadcast with replay
    let channel = supabase.realtimeV2.channel("my-channel") {
      $0.isPrivate = true
      $0.broadcast.acknowledgeBroadcasts = true
      $0.broadcast.receiveOwnBroadcasts = true
      $0.broadcast.replay = ReplayOption(
        since: 1697472000000, // Unix timestamp in milliseconds
        limit: 25
      )
    }

    var subscriptions = Set<RealtimeSubscription>()

    // Broadcast callback receives meta field
    channel.onBroadcast(event: "position") { message in
      if let meta = message["payload"]?.objectValue?["meta"]?.objectValue,
         let replayed = meta["replayed"]?.boolValue,
         replayed {
        print("Replayed message: \(meta["id"]?.stringValue ?? "")")
      }
    }
    .store(in: &subscriptions)

    await channel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    <Admonition type="note">
      Unsupported in Kotlin for now.
    </Admonition>
  </TabPanel>

  <TabPanel id="python" label="Python">
    <Admonition type="note">
      This is currently available only in the Supabase Python client version 2.22.0 and later.
    </Admonition>

    ```python
    # Configure broadcast with replay
    channel = client.channel('my-channel', {
        'config': {
            "private": True,
            'broadcast': {
                'self': True,
                'ack': True,
                'replay': {
                    'since': 1697472000000,
                    'limit': 100
                }
            }
        }
    })

    # Broadcast callback receives meta field
    def on_broadcast(payload):
        if payload.get('meta', {}).get('replayed'):
            print(f"Replayed message: {payload['meta']['id']}")

    await channel.on_broadcast('position', on_broadcast)
    await channel.subscribe()
    ```
  </TabPanel>
</Tabs>


#### When to use Broadcast replay

A few common use cases for Broadcast Replay include:

*   Displaying the most recent messages from a chat room
*   Loading the last events that happened during a sports event
*   Ensuring users always see the latest events after a page reload or network interruption
*   Highlighting the most recent sections that changed in a web page



---
**Navigation:** [← Previous](./03-storage-helper-functions.md) | [Index](./index.md) | [Next →](./05-realtime-concepts.md)
