---
title: "Xata & Astro"
section: 29
---

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

---

[← Previous](28-turso-astro.md) | [Index](index.md) | [Next →](index.md)
