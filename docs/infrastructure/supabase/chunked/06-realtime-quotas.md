**Navigation:** [← Previous](./05-realtime-concepts.md) | [Index](./index.md) | [Next →](./07-aws-marketplace.md)

# Realtime Quotas



Our cluster supports millions of concurrent connections and message throughput for production workloads.

<Admonition type="note">
  Upgrade your plan to increase your quotas. Without a spend cap, or on an Enterprise plan, some quotas are still in place to protect budgets. All quotas are configurable per project. [Contact support](/dashboard/support/new) if you need your quotas increased.
</Admonition>



## Quotas by plan

|                                                                                        | Free  | Pro   | Pro (no spend cap) | Team   | Enterprise |
| -------------------------------------------------------------------------------------- | ----- | ----- | ------------------ | ------ | ---------- |
| **Concurrent connections**                                                             | 200   | 500   | 10,000             | 10,000 | 10,000+    |
| **Messages per second**                                                                | 100   | 500   | 2,500              | 2,500  | 2,500+     |
| **Channel joins per second**                                                           | 100   | 500   | 2,500              | 2,500  | 2,500+     |
| **Channels per connection**                                                            | 100   | 100   | 100                | 100    | 100+       |
| **Presence keys per object**                                                           | 10    | 10    | 10                 | 10     | 10+        |
| **Presence messages per second**                                                       | 20    | 50    | 1,000              | 1,000  | 1,000+     |
| **Broadcast payload size KB**                                                          | 256   | 3,000 | 3,000              | 3,000  | 3,000+     |
| **Postgres change payload size KB ([**read more**](#postgres-changes-payload-quota))** | 1,024 | 1,024 | 1,024              | 1,024  | 1,024+     |

Beyond the Free and Pro Plan you can customize your quotas by [contacting support](/dashboard/support/new).



## Quota errors

When you exceed a quota, errors will appear in the backend logs and client-side messages in the WebSocket connection.

*   **Logs**: check the [Realtime logs](/dashboard/project/_/database/realtime-logs) inside your project Dashboard.
*   **WebSocket errors**: Use your browser's developer tools to find the WebSocket initiation request and view individual messages.

<Admonition type="tip" label="Realtime Inspector">
  You can use the [Realtime Inspector](https://realtime.supabase.com/inspector/new) to reproduce an error and share those connection details with Supabase support.
</Admonition>

Some quotas can cause a Channel join to be refused. Realtime will reply with one of the following WebSocket messages:


### `too_many_channels`

Too many channels currently joined for a single connection.


### `too_many_connections`

Too many total concurrent connections for a project.


### `too_many_joins`

Too many Channel joins per second.


### `tenant_events`

Connections will be disconnected if your project is generating too many messages per second. `supabase-js` will reconnect automatically when the message throughput decreases below your plan quota. An `event` is a WebSocket message delivered to, or sent from a client.



## Postgres changes payload quota

When this quota is reached, the `new` and `old` record payloads only include the fields with a value size of less than or equal to 64 bytes.



# Listening to Postgres Changes with Flutter



The Postgres Changes extension listens for database changes and sends them to clients which enables you to receive database changes in real-time.

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/gboTC2lcgzw?si=WBfCrZyqi9zDWS5n" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Using Realtime Presence with Flutter



Use Supabase Presence to display the currently online users on your Flutter application.

Displaying the list of currently online users is a common feature for real-time collaborative applications. Supabase Presence makes it easy to track users joining and leaving the session so that you can make a collaborative app.

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/B2NZvZ2uLNs?si=2JmxGOFuwwUGaTxr" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Using Realtime with Next.js



In this guide, we explore the best ways to receive real-time Postgres changes with your Next.js application.
We'll show both client and server side updates, and explore which option is best.

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/YR-xP6PPXXA" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Settings

Realtime Settings that allow you to configure your Realtime usage.


## Settings

<Admonition type="caution">
  All changes made in this screen will disconnect all your connected clients to ensure Realtime starts with the appropriate settings and all changes are stored in Supabase middleware.
</Admonition>

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/realtime/realtime-settings--light.png',
    dark: '/docs/img/guides/platform/realtime/realtime-settings--dark.png',
  }}
  zoomable
/>

You can set the following settings using the Realtime Settings screen in your Dashboard:

*   Enable Realtime service: Determines if the Realtime service is enabled or disabled for your project.
*   Channel Restrictions: You can toggle this settings to set Realtime to allow public channels or set it to use only private channels with [Realtime Authorization](/docs/guides/realtime/authorization).
*   Database connection pool size: Determines the number of connections used for Realtime Authorization RLS checking
    {/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}
*   Max concurrent clients: Determines the maximum number of clients that can be connected
*   Max events per second: Determines the maximum number of events per second that can be sent
*   Max presence events per second: Determines the maximum number of presence events per second that can be sent
*   Max payload size in KB: Determines the maximum number of payload size in KB that can be sent



# Subscribing to Database Changes

Listen to database changes in real-time from your website or application.

You can use Supabase to subscribe to real-time database changes. There are two options available:

1.  [Broadcast](/docs/guides/realtime/broadcast). This is the recommended method for scalability and security.
2.  [Postgres Changes](/docs/guides/realtime/postgres-changes). This is a simpler method. It requires less setup, but does not scale as well as Broadcast.



## Using Broadcast

To automatically send messages when a record is created, updated, or deleted, we can attach a [Postgres trigger](/docs/guides/database/postgres/triggers) to any table. Supabase Realtime provides a `realtime.broadcast_changes()` function which we can use in conjunction with a trigger. This function will use a private channel and needs broadcast authorization RLS policies to be met.


### Broadcast authorization

[Realtime Authorization](/docs/guides/realtime/authorization) is required for receiving Broadcast messages. This is an example of a policy that allows authenticated users to listen to messages from topics:

{/* prettier-ignore */}

```sql
create policy "Authenticated users can receive broadcasts"
on "realtime"."messages"
for select
to authenticated
using ( true );
```


### Create a trigger function

Let's create a function that we can call any time a record is created, updated, or deleted. This function will make use of some of Postgres's native [trigger variables](https://www.postgresql.org/docs/current/plpgsql-trigger.html#PLPGSQL-DML-TRIGGER). For this example, we want to have a topic with the name `topic:<record id>` to which we're going to broadcast events.

{/* prettier-ignore */}

```sql
create or replace function public.your_table_changes()
returns trigger
security definer
language plpgsql
as $$
begin
  perform realtime.broadcast_changes(
    'topic:' || coalesce(NEW.topic, OLD.topic) ::text, -- topic - the topic to which we're broadcasting
    TG_OP,                                             -- event - the event that triggered the function
    TG_OP,                                             -- operation - the operation that triggered the function
    TG_TABLE_NAME,                                     -- table - the table that caused the trigger
    TG_TABLE_SCHEMA,                                   -- schema - the schema of the table that caused the trigger
    NEW,                                               -- new record - the record after the change
    OLD                                                -- old record - the record before the change
  );
  return null;
end;
$$;
```


### Create a trigger

Let's set up a trigger so the function is executed after any changes to the table.

{/* prettier-ignore */}

```sql
create trigger handle_your_table_changes
after insert or update or delete
on public.your_table
for each row
execute function your_table_changes ();
```


#### Listening on client side

Finally, on the client side, listen to the topic `topic:<record_id>` to receive the events. Remember to set the channel as a private channel, since `realtime.broadcast_changes` uses Realtime Authorization.

```js
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const gameId = 'id'
await supabase.realtime.setAuth() // Needed for Realtime Authorization
const changes = supabase
  .channel(`topic:${gameId}`, {
    config: { private: true },
  })
  .on('broadcast', { event: 'INSERT' }, (payload) => console.log(payload))
  .on('broadcast', { event: 'UPDATE' }, (payload) => console.log(payload))
  .on('broadcast', { event: 'DELETE' }, (payload) => console.log(payload))
  .subscribe()
```



## Using Postgres Changes

Postgres Changes are simple to use, but have some [limitations](/docs/guides/realtime/postgres-changes#limitations) as your application scales. We recommend using Broadcast for most use cases.

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/2rUjcmgZDwQ" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>


### Enable Postgres Changes

You'll first need to create a `supabase_realtime` publication and add your tables (that you want to subscribe to) to the publication:

```sql
begin;

-- remove the supabase_realtime publication
drop
  publication if exists supabase_realtime;

-- re-create the supabase_realtime publication with no tables
create publication supabase_realtime;

commit;

-- add a table called 'messages' to the publication
-- (update this to match your tables)
alter
  publication supabase_realtime add table messages;
```


### Streaming inserts

You can use the `INSERT` event to stream all new rows.

```js
// @noImplicitAny: false
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const channel = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```


### Streaming updates

You can use the `UPDATE` event to stream all updated rows.

```js
// @noImplicitAny: false
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const channel = supabase
  .channel('schema-db-changes')
  .on(
    'postgres_changes',
    {
      event: 'UPDATE',
      schema: 'public',
    },
    (payload) => console.log(payload)
  )
  .subscribe()
```



# API



{/* <!-- vale off --> */}

When you create a Queue in Supabase, you can choose to create helper database functions in the `pgmq_public` schema. This schema exposes operations to manage Queue Messages to consumers client-side, but does not expose functions for creating or dropping Queues.

Database functions in `pgmq_public` can be exposed via Supabase Data API so consumers client-side can call them. Visit the [Quickstart](/docs/guides/queues/quickstart) for an example.


### `pgmq_public.pop(queue_name)`

Retrieves the next available message and deletes it from the specified Queue.

*   `queue_name` (`text`): Queue name

***


### `pgmq_public.send(queue_name, message, sleep_seconds)`

Adds a Message to the specified Queue, optionally delaying its visibility to all consumers by a number of seconds.

*   `queue_name` (`text`): Queue name
*   `message` (`jsonb`): Message payload to send
*   `sleep_seconds` (`integer`, optional): Delay message visibility by specified seconds. Defaults to 0

***


### `pgmq_public.send_batch(queue_name, messages, sleep_seconds)`

Adds a batch of Messages to the specified Queue, optionally delaying their availability to all consumers by a number of seconds.

*   `queue_name` (`text`): Queue name
*   `messages` (`jsonb[]`): Array of message payloads to send
*   `sleep_seconds` (`integer`, optional): Delay messages visibility by specified seconds. Defaults to 0

***


### `pgmq_public.archive(queue_name, message_id)`

Archives a Message by moving it from the Queue table to the Queue's archive table.

*   `queue_name` (`text`): Queue name
*   `message_id` (`bigint`): ID of the Message to archive

***


### `pgmq_public.delete(queue_name, message_id)`

Permanently deletes a Message from the specified Queue.

*   `queue_name` (`text`): Queue name
*   `message_id` (`bigint`): ID of the Message to delete

***


### `pgmq_public.read(queue_name, sleep_seconds, n)`

Reads up to "n" Messages from the specified Queue with an optional "sleep\_seconds" (visibility timeout).

*   `queue_name` (`text`): Queue name
*   `sleep_seconds` (`integer`): Visibility timeout in seconds
*   `n` (`integer`): Maximum number of Messages to read



# Consuming Supabase Queue Messages with Edge Functions

Learn how to consume Supabase Queue messages server-side with a Supabase Edge Function

This guide helps you read & process queue messages server-side with a Supabase Edge Function. Read [Queues API Reference](/docs/guides/queues/api) for more details on our API.



## Concepts

Supabase Queues is a pull-based Message Queue consisting of three main components: Queues, Messages, and Queue Types. You should already be familiar with the [Queues Quickstart](/docs/guides/queues/quickstart).


### Consuming messages in an Edge Function

This is a Supabase Edge Function that reads 5 messages off the queue, processes each of them, and deletes each message when it is done.

```tsx
import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { createClient } from 'npm:@supabase/supabase-js@2'

const supabaseUrl = 'supabaseURL'
const supabaseKey = 'supabaseKey'

const supabase = createClient(supabaseUrl, supabaseKey)
const queueName = 'your_queue_name'

// Type definition for queue messages
interface QueueMessage {
  msg_id: bigint
  read_ct: number
  vt: string
  enqueued_at: string
  message: any
}

async function processMessage(message: QueueMessage) {
  //
  // Do whatever logic you need to with the message content
  //
  // Delete the message from the queue
  const { error: deleteError } = await supabase.schema('pgmq_public').rpc('delete', {
    queue_name: queueName,
    msg_id: message.msg_id,
  })

  if (deleteError) {
    console.error(`Failed to delete message ${message.msg_id}:`, deleteError)
  } else {
    console.log(`Message ${message.msg_id} deleted from queue`)
  }
}

Deno.serve(async (req) => {
  const { data: messages, error } = await supabase.schema('pgmq_public').rpc('read', {
    queue_name: queueName,
    sleep_seconds: 0, // Don't wait if queue is empty
    n: 5, // Read 5 messages off the queue
  })

  if (error) {
    console.error(`Error reading from ${queueName} queue:`, error)
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  if (!messages || messages.length === 0) {
    console.log('No messages in workflow_messages queue')
    return new Response(JSON.stringify({ message: 'No messages in queue' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  console.log(`Found ${messages.length} messages to process`)

  // Process each message that was read off the queue
  for (const message of messages) {
    try {
      await processMessage(message as QueueMessage)
    } catch (error) {
      console.error(`Error processing message ${message.msg_id}:`, error)
    }
  }

  // Return immediately while background processing continues
  return new Response(
    JSON.stringify({
      message: `Processing ${messages.length} messages in background`,
      count: messages.length,
    }),
    {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    }
  )
})
```

Every time this Edge Function is run it:

1.  Read 5 messages off the queue
2.  Call the `processMessage` function
3.  At the end of `processMessage`, the message is deleted from the queue
4.  If `processMessage` throws an error, the error is logged. In this case, the message is still in the queue, so the next time this Edge Function runs it reads the message again.

You might find this kind of setup handy to run with [Supabase Cron](/docs/guides/cron). You can set up Cron so that every N number of minutes or seconds, the Edge Function will run and process a number of messages off the queue.

Similarly, you can invoke the Edge Function on command at any given time with [`supabase.functions.invoke`](/docs/guides/functions/quickstart-dashboard#usage).



# PGMQ Extension



pgmq is a lightweight message queue built on Postgres.



## Features

*   Lightweight - No background worker or external dependencies, just Postgres functions packaged in an extension
*   "exactly once" delivery of messages to a consumer within a visibility timeout
*   API parity with AWS SQS and RSMQ
*   Messages stay in the queue until explicitly removed
*   Messages can be archived, instead of deleted, for long-term retention and replayability



## Enable the extension

```sql
create extension pgmq;
```



## Usage \[#get-usage]


### Queue management


#### `create`

Create a new queue.

{/* prettier-ignore */}

```sql
pgmq.create(queue_name text)
returns void
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

Example:

{/* prettier-ignore */}

```sql
select from pgmq.create('my_queue');
 create
--------
```


#### `create_unlogged`

Creates an unlogged table. This is useful when write throughput is more important than durability.
See Postgres documentation for [unlogged tables](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-UNLOGGED) for more information.

{/* prettier-ignore */}

```sql
pgmq.create_unlogged(queue_name text)
returns void
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

Example:

{/* prettier-ignore */}

```sql
select pgmq.create_unlogged('my_unlogged');
 create_unlogged
-----------------
```

***


#### `detach_archive`

Drop the queue's archive table as a member of the PGMQ extension. Useful for preventing the queue's archive table from being dropped when `drop extension pgmq` is executed.
This does not prevent the further archives() from appending to the archive table.

{/* prettier-ignore */}

```sql
pgmq.detach_archive(queue_name text)
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.detach_archive('my_queue');
 detach_archive
----------------
```

***


#### `drop_queue`

Deletes a queue and its archive table.

{/* prettier-ignore */}

```sql
pgmq.drop_queue(queue_name text)
returns boolean
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.drop_queue('my_unlogged');
 drop_queue
------------
 t
```


### Sending messages


#### `send`

Send a single message to a queue.

{/* prettier-ignore */}

```sql
pgmq.send(
    queue_name text,
    msg jsonb,
    delay integer default 0
)
returns setof bigint
```

**Parameters:**

| Parameter    | Type      | Description                                                        |
| :----------- | :-------- | :----------------------------------------------------------------- |
| `queue_name` | `text`    | The name of the queue                                              |
| `msg`        | `jsonb`   | The message to send to the queue                                   |
| `delay`      | `integer` | Time in seconds before the message becomes visible. Defaults to 0. |

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.send('my_queue', '{"hello": "world"}');
 send
------
    4
```

***


#### `send_batch`

Send 1 or more messages to a queue.

{/* prettier-ignore */}

```sql
pgmq.send_batch(
    queue_name text,
    msgs jsonb[],
    delay integer default 0
)
returns setof bigint
```

**Parameters:**

| Parameter    | Type      | Description                                                         |
| :----------- | :-------- | :------------------------------------------------------------------ |
| `queue_name` | `text`    | The name of the queue                                               |
| `msgs`       | `jsonb[]` | Array of messages to send to the queue                              |
| `delay`      | `integer` | Time in seconds before the messages becomes visible. Defaults to 0. |

{/* prettier-ignore */}

```sql
select * from pgmq.send_batch(
    'my_queue',
    array[
      '{"hello": "world_0"}'::jsonb,
      '{"hello": "world_1"}'::jsonb
    ]
);
 send_batch
------------
          1
          2
```

***


### Reading messages


#### `read`

Read 1 or more messages from a queue. The VT specifies the duration of time in seconds that the message is invisible to other consumers. At the end of that duration, the message is visible again and could be read by other consumers.

{/* prettier-ignore */}

```sql
pgmq.read(
    queue_name text,
    vt integer,
    qty integer
)

returns setof pgmq.message_record
```

**Parameters:**

| Parameter    | Type      | Description                                                     |
| :----------- | :-------- | :-------------------------------------------------------------- |
| `queue_name` | `text`    | The name of the queue                                           |
| `vt`         | `integer` | Time in seconds that the message become invisible after reading |
| `qty`        | `integer` | The number of messages to read from the queue. Defaults to 1    |

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.read('my_queue', 10, 2);
 msg_id | read_ct |          enqueued_at          |              vt               |       message
--------+---------+-------------------------------+-------------------------------+----------------------
      1 |       1 | 2023-10-28 19:14:47.356595-05 | 2023-10-28 19:17:08.608922-05 | {"hello": "world_0"}
      2 |       1 | 2023-10-28 19:14:47.356595-05 | 2023-10-28 19:17:08.608974-05 | {"hello": "world_1"}
(2 rows)
```

***


#### `read_with_poll`

Same as read(). Also provides convenient long-poll functionality.
When there are no messages in the queue, the function call will wait for `max_poll_seconds` in duration before returning.
If messages reach the queue during that duration, they will be read and returned immediately.

{/* prettier-ignore */}

```sql
 pgmq.read_with_poll(
    queue_name text,
    vt integer,
    qty integer,
    max_poll_seconds integer default 5,
    poll_interval_ms integer default 100
)
returns setof pgmq.message_record
```

**Parameters:**

| Parameter          | Type      | Description                                                                 |
| :----------------- | :-------- | :-------------------------------------------------------------------------- |
| `queue_name`       | `text`    | The name of the queue                                                       |
| `vt`               | `integer` | Time in seconds that the message become invisible after reading.            |
| `qty`              | `integer` | The number of messages to read from the queue. Defaults to 1.               |
| `max_poll_seconds` | `integer` | Time in seconds to wait for new messages to reach the queue. Defaults to 5. |
| `poll_interval_ms` | `integer` | Milliseconds between the internal poll operations. Defaults to 100.         |

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.read_with_poll('my_queue', 1, 1, 5, 100);
 msg_id | read_ct |          enqueued_at          |              vt               |      message
--------+---------+-------------------------------+-------------------------------+--------------------
      1 |       1 | 2023-10-28 19:09:09.177756-05 | 2023-10-28 19:27:00.337929-05 | {"hello": "world"}
```

***


#### `pop`

Reads a single message from a queue and deletes it upon read.

Note: utilization of pop() results in at-most-once delivery semantics if the consuming application does not guarantee processing of the message.

{/* prettier-ignore */}

```sql
pgmq.pop(queue_name text)
returns setof pgmq.message_record
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

Example:

{/* prettier-ignore */}

```sql
pgmq=# select * from pgmq.pop('my_queue');
 msg_id | read_ct |          enqueued_at          |              vt               |      message
--------+---------+-------------------------------+-------------------------------+--------------------
      1 |       2 | 2023-10-28 19:09:09.177756-05 | 2023-10-28 19:27:00.337929-05 | {"hello": "world"}
```

***


### Deleting/Archiving messages


#### `delete` (single)

Deletes a single message from a queue.

{/* prettier-ignore */}

```sql
pgmq.delete (queue_name text, msg_id: bigint)
returns boolean
```

**Parameters:**

| Parameter    | Type     | Description                         |
| :----------- | :------- | :---------------------------------- |
| `queue_name` | `text`   | The name of the queue               |
| `msg_id`     | `bigint` | Message ID of the message to delete |

Example:

{/* prettier-ignore */}

```sql
select pgmq.delete('my_queue', 5);
 delete
--------
 t
```

***


#### `delete` (batch)

Delete one or many messages from a queue.

{/* prettier-ignore */}

```sql
pgmq.delete (queue_name text, msg_ids: bigint[])
returns setof bigint
```

**Parameters:**

| Parameter    | Type       | Description                    |
| :----------- | :--------- | :----------------------------- |
| `queue_name` | `text`     | The name of the queue          |
| `msg_ids`    | `bigint[]` | Array of message IDs to delete |

Examples:

Delete two messages that exist.

{/* prettier-ignore */}

```sql
select * from pgmq.delete('my_queue', array[2, 3]);
 delete
--------
      2
      3
```

Delete two messages, one that exists and one that does not. Message `999` does not exist.

```sql
select * from pgmq.delete('my_queue', array[6, 999]);
 delete
--------
      6
```

***


#### `purge_queue`

Permanently deletes all messages in a queue. Returns the number of messages that were deleted.

```text
purge_queue(queue_name text)
returns bigint
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

Example:

Purge the queue when it contains 8 messages;

{/* prettier-ignore */}

```sql
select * from pgmq.purge_queue('my_queue');
 purge_queue
-------------
           8
```

***


#### `archive` (single)

Removes a single requested message from the specified queue and inserts it into the queue's archive.

{/* prettier-ignore */}

```sql
pgmq.archive(queue_name text, msg_id bigint)
returns boolean
```

**Parameters:**

| Parameter    | Type     | Description                          |
| :----------- | :------- | :----------------------------------- |
| `queue_name` | `text`   | The name of the queue                |
| `msg_id`     | `bigint` | Message ID of the message to archive |

Returns
Boolean value indicating success or failure of the operation.

Example; remove message with ID 1 from queue `my_queue` and archive it:

{/* prettier-ignore */}

```sql
select * from pgmq.archive('my_queue', 1);
 archive
---------
       t
```

***


#### `archive` (batch)

Deletes a batch of requested messages from the specified queue and inserts them into the queue's archive.
Returns an array of message ids that were successfully archived.

```text
pgmq.archive(queue_name text, msg_ids bigint[])
RETURNS SETOF bigint
```

**Parameters:**

| Parameter    | Type       | Description                     |
| :----------- | :--------- | :------------------------------ |
| `queue_name` | `text`     | The name of the queue           |
| `msg_ids`    | `bigint[]` | Array of message IDs to archive |

Examples:

Delete messages with ID 1 and 2 from queue `my_queue` and move to the archive.

{/* prettier-ignore */}

```sql
select * from pgmq.archive('my_queue', array[1, 2]);
 archive
---------
       1
       2
```

Delete messages 4, which exists and 999, which does not exist.

{/* prettier-ignore */}

```sql
select * from pgmq.archive('my_queue', array[4, 999]);
 archive
---------
       4
```

***


### Utilities


#### `set_vt`

Sets the visibility timeout of a message to a specified time duration in the future. Returns the record of the message that was updated.

{/* prettier-ignore */}

```sql
pgmq.set_vt(
    queue_name text,
    msg_id bigint,
    vt_offset integer
)
returns pgmq.message_record
```

**Parameters:**

| Parameter    | Type      | Description                                                           |
| :----------- | :-------- | :-------------------------------------------------------------------- |
| `queue_name` | `text`    | The name of the queue                                                 |
| `msg_id`     | `bigint`  | ID of the message to set visibility time                              |
| `vt_offset`  | `integer` | Duration from now, in seconds, that the message's VT should be set to |

Example:

Set the visibility timeout of message 1 to 30 seconds from now.

```sql
select * from pgmq.set_vt('my_queue', 11, 30);
 msg_id | read_ct |          enqueued_at          |              vt               |       message
--------+---------+-------------------------------+-------------------------------+----------------------
     1 |       0 | 2023-10-28 19:42:21.778741-05 | 2023-10-28 19:59:34.286462-05 | {"hello": "world_0"}
```

***


#### `list_queues`

List all the queues that currently exist.

{/* prettier-ignore */}

```sql
list_queues()
RETURNS TABLE(
    queue_name text,
    created_at timestamp with time zone,
    is_partitioned boolean,
    is_unlogged boolean
)
```

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.list_queues();
      queue_name      |          created_at           | is_partitioned | is_unlogged
----------------------+-------------------------------+----------------+-------------
 my_queue             | 2023-10-28 14:13:17.092576-05 | f              | f
 my_partitioned_queue | 2023-10-28 19:47:37.098692-05 | t              | f
 my_unlogged          | 2023-10-28 20:02:30.976109-05 | f              | t
```

***


#### `metrics`

Get metrics for a specific queue.

{/* prettier-ignore */}

```sql
pgmq.metrics(queue_name: text)
returns table(
    queue_name text,
    queue_length bigint,
    newest_msg_age_sec integer,
    oldest_msg_age_sec integer,
    total_messages bigint,
    scrape_time timestamp with time zone
)
```

**Parameters:**

| Parameter   | Type | Description           |
| :---------- | :--- | :-------------------- |
| queue\_name | text | The name of the queue |

**Returns:**

| Attribute            | Type                       | Description                                                               |
| :------------------- | :------------------------- | :------------------------------------------------------------------------ | -------------------------------------------------- |
| `queue_name`         | `text`                     | The name of the queue                                                     |
| `queue_length`       | `bigint`                   | Number of messages currently in the queue                                 |
| `newest_msg_age_sec` | `integer                   | null`                                                                     | Age of the newest message in the queue, in seconds |
| `oldest_msg_age_sec` | `integer                   | null`                                                                     | Age of the oldest message in the queue, in seconds |
| `total_messages`     | `bigint`                   | Total number of messages that have passed through the queue over all time |
| `scrape_time`        | `timestamp with time zone` | The current timestamp                                                     |

Example:

{/* prettier-ignore */}

```sql
select * from pgmq.metrics('my_queue');
 queue_name | queue_length | newest_msg_age_sec | oldest_msg_age_sec | total_messages |          scrape_time
------------+--------------+--------------------+--------------------+----------------+-------------------------------
 my_queue   |           16 |               2445 |               2447 |             35 | 2023-10-28 20:23:08.406259-05
```

***


#### `metrics_all`

Get metrics for all existing queues.

```text
pgmq.metrics_all()
RETURNS TABLE(
    queue_name text,
    queue_length bigint,
    newest_msg_age_sec integer,
    oldest_msg_age_sec integer,
    total_messages bigint,
    scrape_time timestamp with time zone
)
```

**Returns:**

| Attribute            | Type                       | Description                                                               |
| :------------------- | :------------------------- | :------------------------------------------------------------------------ | -------------------------------------------------- |
| `queue_name`         | `text`                     | The name of the queue                                                     |
| `queue_length`       | `bigint`                   | Number of messages currently in the queue                                 |
| `newest_msg_age_sec` | `integer                   | null`                                                                     | Age of the newest message in the queue, in seconds |
| `oldest_msg_age_sec` | `integer                   | null`                                                                     | Age of the oldest message in the queue, in seconds |
| `total_messages`     | `bigint`                   | Total number of messages that have passed through the queue over all time |
| `scrape_time`        | `timestamp with time zone` | The current timestamp                                                     |

{/* prettier-ignore */}

```sql
select * from pgmq.metrics_all();
      queue_name      | queue_length | newest_msg_age_sec | oldest_msg_age_sec | total_messages |          scrape_time
----------------------+--------------+--------------------+--------------------+----------------+-------------------------------
 my_queue             |           16 |               2563 |               2565 |             35 | 2023-10-28 20:25:07.016413-05
 my_partitioned_queue |            1 |                 11 |                 11 |              1 | 2023-10-28 20:25:07.016413-05
 my_unlogged          |            1 |                  3 |                  3 |              1 | 2023-10-28 20:25:07.016413-05
```


### Types


#### `message_record`

The complete representation of a message in a queue.

| Attribute Name | Type                       | Description                                                            |
| :------------- | :------------------------- | :--------------------------------------------------------------------- |
| `msg_id`       | `bigint`                   | Unique ID of the message                                               |
| `read_ct`      | `bigint`                   | Number of times the message has been read. Increments on read().       |
| `enqueued_at`  | `timestamp with time zone` | time that the message was inserted into the queue                      |
| `vt`           | `timestamp with time zone` | Timestamp when the message will become available for consumers to read |
| `message`      | `jsonb`                    | The message payload                                                    |

Example:

{/* prettier-ignore */}

```sql
 msg_id | read_ct |          enqueued_at          |              vt               |      message
--------+---------+-------------------------------+-------------------------------+--------------------
      1 |       1 | 2023-10-28 19:06:19.941509-05 | 2023-10-28 19:06:27.419392-05 | {"hello": "world"}
```



## Resources

*   Official Docs: [pgmq/api](https://pgmq.github.io/pgmq/#creating-a-queue)



# Quickstart

Learn how to use Supabase Queues to add and read messages

{/* <!-- vale off --> */}

This guide is an introduction to interacting with Supabase Queues via the Dashboard and official client library. Check out [Queues API Reference](/docs/guides/queues/api) for more details on our API.



## Concepts

Supabase Queues is a pull-based Message Queue consisting of three main components: Queues, Messages, and Queue Types.


### Pull-Based Queue

A pull-based Queue is a Message storage and delivery system where consumers actively fetch Messages when they're ready to process them - similar to constantly refreshing a webpage to display the latest updates. Our pull-based Queues process Messages in a First-In-First-Out (FIFO) manner without priority levels.


### Message

A Message in a Queue is a JSON object that is stored until a consumer explicitly processes and removes it, like a task waiting in a to-do list until someone checks and completes it.


### Queue types

Supabase Queues offers three types of Queues:

*   **Basic Queue**: A durable Queue that stores Messages in a logged table.

*   **Unlogged Queue**: A transient Queue that stores Messages in an unlogged table for better performance but may result in loss of Queue Messages.

*   **Partitioned Queue** (*Coming Soon*): A durable and scalable Queue that stores Messages in multiple table partitions for better performance.



## Create Queues

To get started, navigate to the [Supabase Queues](/dashboard/project/_/integrations/queues/overview) Postgres Module under Integrations in the Dashboard and enable the `pgmq` extension.

<Admonition type="note">
  `pgmq` extension is available in Postgres version 15.6.1.143 or later.
</Admonition>

<Image
  alt="Supabase Dashboard Integrations page, showing the Queues Postgres Module"
  src={{
    dark: '/docs/img/queues-quickstart-install.png',
    light: '/docs/img/queues-quickstart-install.png',
  }}
/>

On the [Queues page](/dashboard/project/_/integrations/queues/queues):

*   Click **Add a new queue** button

<Admonition type="note">
  If you've already created a Queue click the **Create a queue** button instead.
</Admonition>

*   Name your queue

<Admonition type="note">
  Queue names can only be lowercase and hyphens and underscores are permitted.
</Admonition>

*   Select your [Queue Type](#queue-types)

<Image
  alt="Create a Queue from the Supabase Dashboard"
  src={{
    dark: '/docs/img/queues-quickstart-create.png',
    light: '/docs/img/queues-quickstart-create.png',
  }}
  zoomable
  className="max-w-lg !mx-auto"
/>


### What happens when you create a queue?

Every new Queue creates two tables in the `pgmq` schema. These tables are `pgmq.q_<queue_name>` to store and process active messages and `pgmq.a_<queue_name>` to store any archived messages.

A "Basic Queue" will create `pgmq.q_<queue_name>` and `pgmq.a_<queue_name>` tables as logged tables.

However, an "Unlogged Queue" will create `pgmq.q_<queue_name>` as an unlogged table for better performance while sacrificing durability. The `pgmq.a_<queue_name>` table will still be created as a logged table so your archived messages remain safe and secure.



## Expose Queues to client-side consumers

Queues, by default, are not exposed over Supabase Data API and are only accessible via Postgres clients.

However, you may grant client-side consumers access to your Queues by enabling the Supabase Data API and granting permissions to the Queues API, which is a collection of database functions in the `pgmq_public` schema that wraps the database functions in the `pgmq` schema.

This is to prevent direct access to the `pgmq` schema and its tables (RLS is not enabled by default on any tables) and database functions.

To get started, navigate to the Queues [Settings page](/dashboard/project/_/integrations/queues/settings) and toggle on “Expose Queues via PostgREST”. Once enabled, Supabase creates and exposes a `pgmq_public` schema containing database function wrappers to a subset of `pgmq`'s database functions.

<Image
  alt="Screenshot of Queues settings with toggle to expose to PostgREST"
  src={{
    dark: '/docs/img/queues-quickstart-settings.png',
    light: '/docs/img/queues-quickstart-settings.png',
  }}
/>


### Enable RLS on your tables in `pgmq` schema

For security purposes, you must enable Row Level Security (RLS) on all Queue tables (all tables in `pgmq` schema that begin with `q_`) if the Data API is enabled.

You’ll want to create RLS policies for any Queues you want your client-side consumers to interact with.

<Image
  alt="Screenshot of creating an RLS policy from the Queues settings"
  src={{
    dark: '/docs/img/queues-quickstart-rls.png',
    light: '/docs/img/queues-quickstart-rls.png',
  }}
/>


### Grant permissions to `pgmq_public` database functions

On top of enabling RLS and writing RLS policies on the underlying Queue tables, you must grant the correct permissions to the `pgmq_public` database functions for each Data API role.

The permissions required for each Queue API database function:

| **Operations**      | **Permissions Required** |
| ------------------- | ------------------------ |
| `send` `send_batch` | `Select` `Insert`        |
| `read` `pop`        | `Select` `Update`        |
| `archive` `delete`  | `Select` `Delete`        |

To manage your queue permissions, click on the Queue Settings button.

<Image
  alt="Screenshot of accessing queue settings"
  src={{
    dark: '/docs/img/queues-quickstart-queue-settings.png',
    light: '/docs/img/queues-quickstart-queue-settings.png',
  }}
/>

Then enable the required roles permissions.

<Image
  alt="Screenshot of configuring API access for roles from the Queues settings"
  src={{
    dark: '/docs/img/queues-quickstart-roles.png',
    light: '/docs/img/queues-quickstart-roles-light.png',
  }}
/>

<Admonition type="note">
  `postgres` and `service_role` roles should never be exposed client-side.
</Admonition>


### Enqueueing and dequeueing messages

Once your Queue has been created, you can begin enqueueing and dequeueing Messages.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```tsx
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = 'supabaseURL'
    const supabaseKey = 'supabaseKey'

    const supabase = createClient(supabaseUrl, supabaseKey)

    const QueuesTest: React.FC = () => {
      //Add a Message
      const sendToQueue = async () => {
        const result = await supabase.schema('pgmq_public').rpc('send', {
          queue_name: 'foo',
          message: { hello: 'world' },
          sleep_seconds: 30,
        })
        console.log(result)
      }

      //Dequeue Message
      const popFromQueue = async () => {
        const result = await supabase.schema('pgmq_public').rpc('pop', { queue_name: 'foo' })
        console.log(result)
      }

      return (
        <div className="p-6">
          <h2 className="text-2xl font-bold mb-4">Queue Test Component</h2>
          <button
            onClick={sendToQueue}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 mr-4"
          >
            Add Message
          </button>
          <button
            onClick={popFromQueue}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Pop Message
          </button>
        </div>
      )
    }

    export default QueuesTest
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    import 'package:supabase_flutter/supabase_flutter.dart';

    final supabase = Supabase.instance.client;

    // Add a Message
    Future<void> sendToQueue() async {
      final result = await supabase.schema('pgmq_public').rpc('send', params: {
        'queue_name': 'foo',
        'message': {'hello': 'world'},
        'sleep_seconds': 30,
      });
      print(result);
    }

    // Dequeue Message
    Future<void> popFromQueue() async {
      final result = await supabase.schema('pgmq_public').rpc('pop', params: {
        'queue_name': 'foo',
      });
      print(result);
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Supabase

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "supabaseURL")!,
      supabaseKey: "supabaseKey"
    )

    // Add a Message
    func sendToQueue() async throws {
      let result = try await supabase
        .schema("pgmq_public")
        .rpc("send", params: [
          "queue_name": AnyJSON.string("foo"),
          "message": AnyJSON.object(["hello": "world"]),
          "sleep_seconds": AnyJSON.integer(30)
        ])
        .execute()
      print(result)
    }

    // Dequeue Message
    func popFromQueue() async throws {
      let result = try await supabase
        .schema("pgmq_public")
        .rpc("pop", params: ["queue_name": "foo"])
        .execute()
      print(result)
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    from supabase import create_client, Client

    supabase_url = "supabaseURL"
    supabase_key = "supabaseKey"

    supabase: Client = create_client(supabase_url, supabase_key)

    # Add a Message
    def send_to_queue():
        result = supabase.schema("pgmq_public").rpc(
            "send",
            {
                "queue_name": "foo",
                "message": {"hello": "world"},
                "sleep_seconds": 30,
            }
        ).execute()
        print(result)

    # Dequeue Message
    def pop_from_queue():
        result = supabase.schema("pgmq_public").rpc(
            "pop",
            {"queue_name": "foo"}
        ).execute()
        print(result)
    ```
  </TabPanel>
</Tabs>



# Access Control



Supabase provides granular access controls to manage permissions across your organizations and projects.

For each organization and project, a member can have one of the following roles:

*   **Owner**: full access to everything in organization and project resources.
*   **Administrator**: full access to everything in organization and project resources **except** updating organization settings, transferring projects outside of the organization, and adding new owners.
*   **Developer**: read-only access to organization resources and content access to project resources but cannot change any project settings.
*   **Read-Only**: read-only access to organization and project resources.

<Admonition type="note">
  Read-Only role is only available on the [Team and Enterprise plans](/pricing).
</Admonition>

When you first create an account, a default organization is created for you and you'll be assigned as the **Owner**. Any organizations you create will assign you as **Owner** as well.



## Manage organization members

To invite others to collaborate, visit your organization's team [settings](/dashboard/org/_/team) to send an invite link to another user's email. The invite is valid for 24 hours. For project scoped roles, you may only assign a role to a single project for the user when sending the invite. You can assign roles to multiple projects after the user accepts the invite.

<Admonition type="note">
  Invites sent from a SAML SSO account can only be accepted by another SAML SSO account from the same identity provider.

  This is a security measure to prevent accidental invites to accounts not managed by your enterprise's identity provider.
</Admonition>


### Viewing organization members using the Management API

You can also view organization members using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export ORG_ID="your-organization-id"


# List organization members
curl "https://api.supabase.com/v1/organizations/$ORG_ID/members" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN"
```


### Transferring ownership of an organization

Each Supabase organization must have at least one owner. If your organization has other owners then you can relinquish ownership and leave the organization by clicking **Leave team** in your organization's team [settings](/dashboard/org/_/team).

Otherwise, you'll need to invite a user as **Owner**, and they need to accept the invitation, or promote an existing organization member to **Owner** before you can leave the organization.


### Organization scoped roles vs project scoped roles

<Admonition type="note">
  Project scoped roles are only available on the [Team and Enterprise plans](/pricing).
</Admonition>

Each member in the organization can be assigned a role that is scoped either to the entire organization or to specific projects.

*   If a member has an organization-level role, they will have the corresponding permissions across all current and future projects within that organization.
*   If a member is assigned a project-scoped role, they will only have access to the specific projects they've been assigned to. They will not be able to view, access, or even see other projects within the organization on the Supabase Dashboard.

This allows for more granular control, ensuring that users only have visibility and access to the projects relevant to their role.


### Organization permissions across roles

The table below shows the actions each role can take on the resources belonging to the organization.

| Resource                                                                                                    | Action     |                  Owner                  |              Administrator              |                Developer                |              Read-Only\[^1]              |
| ----------------------------------------------------------------------------------------------------------- | ---------- | :-------------------------------------: | :-------------------------------------: | :-------------------------------------: | :-------------------------------------: |
| <a href="#org-permissions" id="org-permissions">**Organization**</a>                                        |            |                                         |                                         |                                         |                                         |
| Organization Management                                                                                     | Update     | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Delete     | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
| OpenAI Telemetry Configuration\[^2]                                                                          | Update     | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
| <a href="#member-permissions" id="member-permissions">**Members**</a>                                       |            |                                         |                                         |                                         |                                         |
| Organization Members                                                                                        | List       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| Owner                                                                                                       | Add        | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Remove     | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
| Administrator                                                                                               | Add        | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Remove     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Developer                                                                                                   | Add        | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Remove     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Owner (Project-Scoped)                                                                                      | Add        | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Remove     | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |           <IconX size={14} />           |
| Administrator (Project-Scoped)                                                                              | Add        | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Remove     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Developer (Project-Scoped)                                                                                  | Add        | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Remove     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Invite                                                                                                      | Revoke     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Resend     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Accept\[^3] | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| <a href="#billing-permissions" id="billing-permissions">**Billing**</a>                                     |            |                                         |                                         |                                         |                                         |
| Invoices                                                                                                    | List       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| Billing Email                                                                                               | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Subscription                                                                                                | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Billing Address                                                                                             | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Tax Codes                                                                                                   | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Payment Methods                                                                                             | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Usage                                                                                                       | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| <a href="#org-integration-permissions" id="org-integration-permissions">**Integrations (Org Settings)**</a> |            |                                         |                                         |                                         |                                         |
| Authorize GitHub                                                                                            | -          | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| Add GitHub Repositories                                                                                     | -          | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
| GitHub Connections                                                                                          | Create     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Delete     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| Vercel Connections                                                                                          | Create     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Delete     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | View       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| <a href="#oauth-permissions" id="oauth-permissions">**OAuth Apps**</a>                                      |            |                                         |                                         |                                         |                                         |
| OAuth Apps                                                                                                  | Create     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Update     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | Delete     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |
|                                                                                                             | List       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| <a href="#audit-permissions" id="audit-permissions">**Audit Logs**</a>                                      |            |                                         |                                         |                                         |                                         |
| View Audit logs                                                                                             | -          | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| <a href="#legal-docs-permissions" id="legal-docs-permissions">**Legal Documents**</a>                       |            |                                         |                                         |                                         |                                         |
| SOC2 Type 2 Report                                                                                          | Download   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |
| Security Questionnaire                                                                                      | Download   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |


### Project permissions across roles

The table below shows the actions each role can take on the resources belonging to the project.

| Resource                                                                                               | Action                 |                  Owner                  |                  Admin                  |                Developer                |                        Read-Only\[^4]\[^6]                        |
| ------------------------------------------------------------------------------------------------------ | ---------------------- | :-------------------------------------: | :-------------------------------------: | :-------------------------------------: | :-------------------------------------------------------------: |
| <a href="#project-permissions" id="project-permissions">**Project**</a>                                |                        |                                         |                                         |                                         |                                                                 |
| Project Management                                                                                     | Transfer               | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Update (Name)          | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Pause                  | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Restore                | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Restart                | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| Custom Domains                                                                                         | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Data (Database)                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |    <IconCheck className="inline" size={14} color="#3FCF8E" />   |
|                                                                                                        | Manage                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| <a href="#infrastructure-permissions" id="infrastructure-permissions">**Infrastructure**</a>           |                        |                                         |                                         |                                         |                                                                 |
| Read Replicas                                                                                          | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Add-ons                                                                                                | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| <a href="#proj-integrations-permissions" id="proj-integrations-permissions">**Integrations**</a>       |                        |                                         |                                         |                                         |                                                                 |
| Authorize GitHub                                                                                       | -                      | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| Add GitHub Repositories                                                                                | -                      | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| GitHub Connections                                                                                     | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| Vercel Connections                                                                                     | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| <a href="#database-config-permissions" id="database-config-permissions">**Database Configuration**</a> |                        |                                         |                                         |                                         |                                                                 |
| Reset Password                                                                                         | -                      | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Pooling Settings                                                                                       | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| SSL Configuration                                                                                      | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Disk Size Configuration                                                                                | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Network Restrictions                                                                                   | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Network Bans                                                                                           | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Unban                  | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| <a href="#api-config-permissions" id="api-config-permissions">**API Configuration**</a>                |                        |                                         |                                         |                                         |                                                                 |
| API Keys                                                                                               | Read service key       | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Read anon key          | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| JWT Secret                                                                                             | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Generate new           | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| API settings                                                                                           | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| <a href="#auth-config-permissions" id="auth-config-permissions">**Auth Configuration**</a>             |                        |                                         |                                         |                                         |                                                                 |
| Auth Settings                                                                                          | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| SMTP Settings                                                                                          | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| Advanced Settings                                                                                      | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| <a href="#storage-config-permissions" id="storage-config-permissions">**Storage Configuration**</a>    |                        |                                         |                                         |                                         |                                                                 |
| Upload Limit                                                                                           | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| S3 Access Keys                                                                                         | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| <a href="#edge-config-permissions" id="edge-config-permissions">**Edge Functions Configuration**</a>   |                        |                                         |                                         |                                         |                                                                 |
| Secrets                                                                                                | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck className="inline" size={14} color="#3FCF8E" /> \[^5] |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| <a href="#sql-editor-permissions" id="sql-editor-permissions">**SQL Editor**</a>                       |                        |                                         |                                         |                                         |                                                                 |
| Queries                                                                                                | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Run                    | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck className="inline" size={14} color="#3FCF8E" /> \[^7] |
| <a href="#database-permissions" id="database-permissions">**Database**</a>                             |                        |                                         |                                         |                                         |                                                                 |
| Scheduled Backups                                                                                      | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Download               | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Restore                | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| Physical backups (PITR)                                                                                | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Restore                | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| <a href="#auth-permissions" id="auth-permissions">**Authentication**</a>                               |                        |                                         |                                         |                                         |                                                                 |
| Users                                                                                                  | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Send OTP               | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Send password recovery | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Send magic link        | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Remove MFA factors     | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| Providers                                                                                              | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Rate Limits                                                                                            | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Email Templates                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| URL Configuration                                                                                      | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |           <IconX size={14} />           |                       <IconX size={14} />                       |
| Hooks                                                                                                  | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| <a href="#storage-permissions" id="storage-permissions">**Storage** </a>                               |                        |                                         |                                         |                                         |                                                                 |
| Buckets                                                                                                | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| Files                                                                                                  | Create (Upload)        | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| <a href="#edge-permissions" id="edge-permissions">**Edge Functions** </a>                              |                        |                                         |                                         |                                         |                                                                 |
| Edge Functions                                                                                         | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| <a href="#proj-reports-permissions" id="proj-reports-permissions">**Reports** </a>                     |                        |                                         |                                         |                                         |                                                                 |
| Custom Report                                                                                          | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| <a href="#proj-logs-permissions" id="proj-logs-permissions">**Logs & Analytics**</a>                   |                        |                                         |                                         |                                         |                                                                 |
| Queries                                                                                                | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | View                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Run                    | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
| <a href="#branching-permissions" id="branching-permissions">**Branching**</a>                          |                        |                                         |                                         |                                         |                                                                 |
| Production Branch                                                                                      | Read                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Write                  | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
| Development Branches                                                                                   | List                   | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |             <IconCheck size={14} color="#3FCF8E" />             |
|                                                                                                        | Create                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Update                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |
|                                                                                                        | Delete                 | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> | <IconCheck size={14} color="#3FCF8E" /> |                       <IconX size={14} />                       |

\[^1]: Available on the Team and Enterprise Plans.

\[^2]: Sending anonymous data to OpenAI is opt in and can improve Studio AI Assistant's responses.

\[^3]: Invites sent from a SSO account can only be accepted by another SSO account coming from the same identity provider. This is a security measure that prevents accidental invites to accounts not managed by your company's enterprise systems.

\[^4]: Available on the Team and Enterprise Plans.

\[^5]: Read-Only role is able to access secrets.

\[^6]: Listed permissions are for the API and Dashboard.

\[^7]: Limited to executing SELECT queries. SQL Query Snippets run by the Read-Only role are run against the database using the **supabase\_read\_only\_user**. This role has the [predefined Postgres role pg\_read\_all\_data](https://www.postgresql.org/docs/current/predefined-roles.html).



---
**Navigation:** [← Previous](./05-realtime-concepts.md) | [Index](./index.md) | [Next →](./07-aws-marketplace.md)
