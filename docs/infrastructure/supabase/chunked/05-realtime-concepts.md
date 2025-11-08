**Navigation:** [← Previous](./04-stop-and-remove-the-containers.md) | [Index](./index.md) | [Next →](./06-realtime-quotas.md)

# Realtime Concepts




## Concepts

There are several concepts and terminology that is useful to understand how Realtime works.

*   **Channels**: the foundation of Realtime. Think of them as rooms where clients can communicate and listen to events. Channels are identified by a topic name and if they are public or private.
*   **Topics**: the name of the channel. They are used to identify the channel and are a string used to identify the channel.
*   **Events**: the type of messages that can be sent and received.
*   **Payload**: the actual data that is sent and received and that the user will act upon.
*   **Concurrent Connections**: number of total channels subscribed for all clients.



## Channels

Channels are the foundation of Realtime. Think of them as rooms where clients can communicate and listen to events. Channels are identified by a topic name and if they are public or private.

For private channels, you need to use [Realtime Authorization](/docs/guides/realtime/authorization) to control access to the channel and if they are able to send messages.
For public channels, any user can subscribe to the channel, send and receive messages.

You can set your project to use only private channels or both private and public channels in the [Realtime Settings](/docs/guides/realtime/settings).

<Admonition type="note">
  If you have a private channel and a public channel with the same topic name, Realtime sees them as unique channels and won't send messages between them.
</Admonition>



## Database resources

Realtime uses several database connections to perform several operations. As a user, you are able to tune some of them using [Realtime Settings](/docs/guides/realtime/settings).


### Database connections

Realtime uses several database connections to perform various operations. You can configure some of these connections through [Realtime Settings](/docs/guides/realtime/settings).

The connections include:

*   **Migrations**: Two temporary connections to run database migrations when needed
*   **Authorization**: Configurable connection pool to check authorization policies on join that are always started.
*   **Broadcast from database**: One connection to receive data from replication slot used to broadcast the changes to the clients that is always started.
*   **Postgres Changes**: Multiple connection pools required. These pools are only started if you use Postgres Changes.
    *   **Subscription management**: To manage the subscribers to Postgres Changes
    *   **Subscription cleanup**: To cleanup the subscribers to Postgres Changes
    *   **WAL pull**: To pull the changes from the database

The number of connections varies based on your compute add-on size and configuration. The following table shows the default connection pool sizes for different compute add-on variants:

| Compute Add-on | Broadcast from database | Authorization Pool Size | Subscription management | Subscription cleanup | WAL pull |
| -------------- | ----------------------- | ----------------------- | ----------------------- | -------------------- | -------- |
| Nano           | 1                       | 2                       | 2                       | 2                    | 2        |
| Micro          | 1                       | 2                       | 2                       | 2                    | 2        |
| Small          | 1                       | 5                       | 4                       | 4                    | 4        |
| Medium         | 1                       | 5                       | 4                       | 4                    | 4        |
| Large          | 1                       | 5                       | 4                       | 4                    | 4        |
| XL             | 1                       | 10                      | 7                       | 7                    | 7        |
| 2XL            | 1                       | 10                      | 7                       | 7                    | 7        |
| 4XL            | 1                       | 10                      | 7                       | 7                    | 7        |
| 8XL            | 1                       | 15                      | 9                       | 9                    | 9        |
| 12XL           | 1                       | 15                      | 9                       | 9                    | 9        |
| 16XL           | 1                       | 15                      | 9                       | 9                    | 9        |
| >16XL          | 1                       | 15                      | 9                       | 9                    | 9        |

<Admonition type="note">
  You can customize `Authorization Pool Size` through the `Database connection pool size` parameter in your Realtime configuration. If not specified, the default values shown in the table will be used.
</Admonition>


### Replication slots

Realtime also uses, at maximum, 2 replication slots.

*   **Broadcast from database**: To broadcast the changes from the database to the clients
*   **Postgres Changes**: To listen to changes from the database


### Schema and tables

The `realtime` schema creates the following tables:

*   `schema_migrations` - To track the migrations that have been run on the database from Realtime
*   `subscription` - Track the subscribers to Postgres Changes
*   `messages` - Partitioned table per day that's used for Authorization and Broadcast from database
    *   **Authorization**: To check the authorization policies on join by checking if a given user can read and write to this table
    *   **Broadcast from database**: Replication slot tracks a publication to this table to broadcast the changes to the connected clients.
    *   The schema from the table is the following:
        ```sql
        create table realtime.messages (
        topic text not null, -- The topic of the message
        extension text not null, -- The extension of the message (presence, broadcast)
        payload jsonb null, -- The payload of the message
        event text null, -- The event of the message
        private boolean null default false, -- If the message is going to use a private channel
        updated_at timestamp without time zone not null default now(), -- The timestamp of the message
        inserted_at timestamp without time zone not null default now(), -- The timestamp of the message
        id uuid not null default gen_random_uuid (), -- The id of the message
        constraint messages_pkey primary key (id, inserted_at)) partition by RANGE (inserted_at);
        ```

<Admonition type="note">
  Realtime has a cleanup process that will delete tables older than 3 days.
</Admonition>


### Functions

Realtime creates two functions on your database:

*   `realtime.send` - Inserts an entry into `realtime.messages` table that will trigger the replication slot to broadcast the changes to the clients. It also captures errors to prevent the trigger from breaking.
*   `realtime.broadcast_changes` - uses `realtime.send` to broadcast the changes with a format that is compatible with Postgres Changes



# Operational Error Codes

List of operational codes to help understand your deployment and usage.

<ErrorCodes service="realtime" />



# Getting Started with Realtime

Learn how to build real-time applications with Supabase Realtime


## Quick start


### 1. Install the client library

<Tabs scrollable size="small" type="underlined" defaultActiveId="ts" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```bash
    npm install @supabase/supabase-js
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```bash
    flutter pub add supabase_flutter
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let package = Package(
        // ...
        dependencies: [
            // ...
            .package(
                url: "https://github.com/supabase/supabase-swift.git",
                from: "2.0.0"
            ),
        ],
        targets: [
            .target(
                name: "YourTargetName",
                dependencies: [
                    .product(
                        name: "Supabase",
                        package: "supabase-swift"
                    ),
                ]
            )
        ]
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python - PIP">
    ```bash
    pip install supabase
    ```
  </TabPanel>

  <TabPanel id="python" label="Python - Conda">
    ```bash
    conda install -c conda-forge supabase
    ```
  </TabPanel>
</Tabs>


### 2. Initialize the client

Get your project URL and key.


### Get API details

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key. Get the URL from [the API settings section](/dashboard/project/_/settings/api) of a project and the key from the [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/).

<Admonition type="note" title="Changes to API keys">
  Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

  To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

  *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
  *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="ts" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```ts
    import { createClient } from '@supabase/supabase-js'

    const supabase = createClient('https://<project>.supabase.co', '<anon_key or sb_publishable_key>')
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    import 'package:supabase_flutter/supabase_flutter.dart';

    void main() async {
      await Supabase.initialize(
        url: 'https://<project>.supabase.co',
        anonKey: '<anon_key or sb_publishable_key>',
      );
      runApp(MyApp());
    }

    final supabase = Supabase.instance.client;
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Supabase

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "https://<project>.supabase.co")!,
      supabaseKey: "<anon_key or sb_publishable_key>"
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    from supabase import create_client, Client

    url: str = "https://<project>.supabase.co"
    key: str = "<anon_key or sb_publishable_key>"
    supabase: Client = create_client(url, key)
    ```
  </TabPanel>
</Tabs>


### 3. Create your first Channel

Channels are the foundation of Realtime. Think of them as rooms where clients can communicate. Each channel is identified by a topic name and if they are public or private.

<Tabs scrollable size="small" type="underlined" defaultActiveId="ts" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```ts
    // Create a channel with a descriptive topic name
    const channel = supabase.channel('room:lobby:messages', {
      config: { private: true }, // Recommended for production
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    // Create a channel with a descriptive topic name
    final channel = supabase.channel('room:lobby:messages');
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    // Create a channel with a descriptive topic name
    let channel = supabase.channel("room:lobby:messages") {
      $0.isPrivate = true
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    # Create a channel with a descriptive topic name
    channel = supabase.channel('room:lobby:messages', params={config={private= True }})
    ```
  </TabPanel>
</Tabs>


### 4. Set up authorization

Since we're using a private channel, you need to create a basic RLS policy on the `realtime.messages` table to allow authenticated users to connect. Row Level Security (RLS) policies control who can access your Realtime channels based on user authentication and custom rules:

```sql
-- Allow authenticated users to receive broadcasts
CREATE POLICY "authenticated_users_can_receive" ON realtime.messages
  FOR SELECT TO authenticated USING (true);

-- Allow authenticated users to send broadcasts
CREATE POLICY "authenticated_users_can_send" ON realtime.messages
  FOR INSERT TO authenticated WITH CHECK (true);
```


### 5. Send and receive messages

There are three main ways to send messages with Realtime:


#### 5.1 using client libraries

Send and receive messages using the Supabase client:

<Tabs scrollable size="small" type="underlined" defaultActiveId="ts" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```ts
    // Listen for messages
    channel
      .on('broadcast', { event: 'message_sent' }, (payload: { payload: any }) => {
        console.log('New message:', payload.payload)
      })
      .subscribe()

    // Send a message
    channel.send({
      type: 'broadcast',
      event: 'message_sent',
      payload: {
        text: 'Hello, world!',
        user: 'john_doe',
        timestamp: new Date().toISOString(),
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    // Listen for messages
    channel.onBroadcast(
      event: 'message_sent',
      callback: (payload) {
        print('New message: ${payload['payload']}');
      },
    ).subscribe();

    // Send a message
    channel.sendBroadcastMessage(
      event: 'message_sent',
      payload: {
        'text': 'Hello, world!',
        'user': 'john_doe',
        'timestamp': DateTime.now().toIso8601String(),
      },
    );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    // Listen for messages
    await channel.onBroadcast(event: "message_sent") { message in
      print("New message: \(message.payload)")
    }

    let status = await channel.subscribe()

    // Send a message
    await channel.sendBroadcastMessage(
      event: "message_sent",
      payload: [
        "text": "Hello, world!",
        "user": "john_doe",
        "timestamp": ISO8601DateFormatter().string(from: Date())
      ]
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    # Listen for messages
    def message_handler(payload):
        print(f"New message: {payload['payload']}")

    channel.on_broadcast(event="message_sent", callback=message_handler).subscribe()

    # Send a message
    channel.send_broadcast_message(
        event="message_sent",
        payload={
            "text": "Hello, world!",
            "user": "john_doe",
            "timestamp": datetime.now().isoformat()
        }
    )
    ```
  </TabPanel>
</Tabs>


#### 5.2 using HTTP/REST API

Send messages via HTTP requests, perfect for server-side applications:

<Tabs scrollable size="small" type="underlined" defaultActiveId="ts" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```ts
    // Send message via REST API
    const response = await fetch(`https://<project>.supabase.co/rest/v1/rpc/broadcast`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer <your-service-role-key>`,
        apikey: '<your-service-role-key>',
      },
      body: JSON.stringify({
        topic: 'room:lobby:messages',
        event: 'message_sent',
        payload: {
          text: 'Hello from server!',
          user: 'system',
          timestamp: new Date().toISOString(),
        },
        private: true,
      }),
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    import 'package:http/http.dart' as http;
    import 'dart:convert';

    // Send message via REST API
    final response = await http.post(
      Uri.parse('https://<project>.supabase.co/rest/v1/rpc/broadcast'),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <your-service-role-key>',
        'apikey': '<your-service-role-key>',
      },
      body: jsonEncode({
        'topic': 'room:lobby:messages',
        'event': 'message_sent',
        'payload': {
          'text': 'Hello from server!',
          'user': 'system',
          'timestamp': DateTime.now().toIso8601String(),
        },
        'private': true,
      }),
    );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    import Foundation

    // Send message via REST API
    let url = URL(string: "https://<project>.supabase.co/rest/v1/rpc/broadcast")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    request.setValue("Bearer <your-service-role-key>", forHTTPHeaderField: "Authorization")
    request.setValue("<your-service-role-key>", forHTTPHeaderField: "apikey")

    let payload = [
      "topic": "room:lobby:messages",
      "event": "message_sent",
      "payload": [
        "text": "Hello from server!",
        "user": "system",
        "timestamp": ISO8601DateFormatter().string(from: Date())
      ],
      "private": true
    ] as [String: Any]

    request.httpBody = try JSONSerialization.data(withJSONObject: payload)

    let (data, response) = try await URLSession.shared.data(for: request)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    import requests
    from datetime import datetime

    # Send message via REST API
    response = requests.post(
        'https://<project>.supabase.co/rest/v1/rpc/broadcast',
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer <your-service-role-key>',
            'apikey': '<your-service-role-key>'
        },
        json={
            'topic': 'room:lobby:messages',
            'event': 'message_sent',
            'payload': {
                'text': 'Hello from server!',
                'user': 'system',
                'timestamp': datetime.now().isoformat()
            },
            'private': True
        }
    )
    ```
  </TabPanel>
</Tabs>


#### 5.3 using database triggers

Automatically broadcast database changes using triggers. Choose the approach that best fits your needs:

**Using `realtime.broadcast_changes` (Best for mirroring database changes)**

```sql
-- Create a trigger function for broadcasting database changes
CREATE OR REPLACE FUNCTION broadcast_message_changes()
RETURNS TRIGGER AS $$
BEGIN
  -- Broadcast to room-specific channel
  PERFORM realtime.broadcast_changes(
    'room:' || NEW.room_id::text || ':messages',
    TG_OP,
    TG_OP,
    TG_TABLE_NAME,
    TG_TABLE_SCHEMA,
    NEW,
    OLD
  );
  RETURN NULL;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Apply trigger to your messages table
CREATE TRIGGER messages_broadcast_trigger
  AFTER INSERT OR UPDATE OR DELETE ON messages
  FOR EACH ROW EXECUTE FUNCTION broadcast_message_changes();
```

**Using `realtime.send` (Best for custom notifications and filtered data)**

```sql
-- Create a trigger function for custom notifications
CREATE OR REPLACE FUNCTION notify_message_activity()
RETURNS TRIGGER AS $$
BEGIN
  -- Send custom notification when new message is created
  IF TG_OP = 'INSERT' THEN
    PERFORM realtime.send(
      'room:' || NEW.room_id::text || ':notifications',
      'message_created',
      jsonb_build_object(
        'message_id', NEW.id,
        'user_id', NEW.user_id,
        'room_id', NEW.room_id,
        'created_at', NEW.created_at
      ),
      true  -- private channel
    );
  END IF;

  RETURN NULL;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Apply trigger to your messages table
CREATE TRIGGER messages_notification_trigger
  AFTER INSERT ON messages
  FOR EACH ROW EXECUTE FUNCTION notify_message_activity();
```

*   **`realtime.broadcast_changes`** sends the full database change with metadata
*   **`realtime.send`** allows you to send custom payloads and control exactly what data is broadcast



## Essential best practices


### Use private channels

Always use private channels for production applications to ensure proper security and authorization:

```ts
const channel = supabase.channel('room:123:messages', {
  config: { private: true },
})
```


### Follow naming conventions

**Channel Topics:** Use the pattern `scope:id:entity`

*   `room:123:messages` - Messages in room 123
*   `game:456:moves` - Game moves for game 456
*   `user:789:notifications` - Notifications for user 789


### Clean up subscriptions

Always unsubscribe when you are done with a channel to ensure you free up resources:

<Tabs scrollable size="small" type="underlined" defaultActiveId="ts" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```ts
    // React example
    import { useEffect } from 'react'

    useEffect(() => {
      const channel = supabase.channel('room:123:messages')

      return () => {
        supabase.removeChannel(channel)
      }
    }, [])
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    // Flutter example
    class _MyWidgetState extends State<MyWidget> {
      RealtimeChannel? _channel;

      @override
      void initState() {
        super.initState();
        _channel = supabase.channel('room:123:messages');
      }

      @override
      void dispose() {
        _channel?.unsubscribe();
        super.dispose();
      }
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    // SwiftUI example
    struct ContentView: View {
      @State private var channel: RealtimeChannelV2?

      var body: some View {
        // Your UI here
        .onAppear {
          channel = supabase.realtimeV2.channel("room:123:messages")
        }
        .onDisappear {
          Task {
            await channel?.unsubscribe()
          }
        }
      }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    # Python example with context manager
    class RealtimeManager:
        def __init__(self):
            self.channel = None

        def __enter__(self):
            self.channel = supabase.channel('room:123:messages')
            return self.channel

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.channel:
                self.channel.unsubscribe()

    # Usage
    with RealtimeManager() as channel:
        # Use channel here
        pass
    ```
  </TabPanel>
</Tabs>



## Choose the right feature


### When to use Broadcast

*   Real-time messaging and notifications
*   Custom events and game state
*   Database change notifications (with triggers)
*   High-frequency updates (e.g. Cursor tracking)
*   Most use cases


### When to use Presence

*   User online/offline status
*   Active user counters
*   Use minimally due to computational overhead


### When to use Postgres Changes

*   Quick testing and development
*   Low amount of connected users



## Next steps

Now that you understand the basics, dive deeper into each feature:


### Core features

*   **[Broadcast](/docs/guides/realtime/broadcast)** - Learn about sending messages, database triggers, and REST API usage
*   **[Presence](/docs/guides/realtime/presence)** - Implement user state tracking and online indicators
*   **[Postgres Changes](/docs/guides/realtime/postgres-changes)** - Understanding database change listeners (consider migrating to Broadcast)


### Security & configuration

*   **[Authorization](/docs/guides/realtime/authorization)** - Set up RLS policies for private channels
*   **[Settings](/docs/guides/realtime/settings)** - Configure your Realtime instance for optimal performance


### Advanced topics

*   **[Architecture](/docs/guides/realtime/architecture)** - Understand how Realtime works under the hood
*   **[Benchmarks](/docs/guides/realtime/benchmarks)** - Performance characteristics and scaling considerations
*   **[Quotas](/docs/guides/realtime/quotas)** - Usage limits and best practices


### Integration guides

*   **[Realtime with Next.js](/docs/guides/realtime/realtime-with-nextjs)** - Build real-time Next.js applications
*   **[User Presence](/docs/guides/realtime/realtime-user-presence)** - Implement user presence features
*   **[Database Changes](/docs/guides/realtime/subscribing-to-database-changes)** - Listen to database changes


### Framework examples

*   **[Flutter Integration](/docs/guides/realtime/realtime-listening-flutter)** - Build real-time Flutter applications

Ready to build something amazing? Start with the [Broadcast guide](/docs/guides/realtime/broadcast) to create your first real-time feature!



# Postgres Changes

Listen to Postgres changes using Supabase Realtime.

Let's explore how to use Realtime's Postgres Changes feature to listen to database events.



## Quick start

In this example we'll set up a database table, secure it with Row Level Security, and subscribe to all changes using the Supabase client libraries.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Set up a Supabase project with a 'todos' table">
      [Create a new project](https://app.supabase.com) in the Supabase Dashboard.

      After your project is ready, create a table in your Supabase database. You can do this with either the Table interface or the [SQL Editor](https://app.supabase.com/project/_/sql).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
        <TabPanel id="sql" label="SQL">
          ```sql
          -- Create a table called "todos"
          -- with a column to store tasks.
          create table todos (
            id serial primary key,
            task text
          );
          ```
        </TabPanel>

        <TabPanel id="dashboard" label="Dashboard">
          <video width="99%" muted playsInline controls={true}>
            <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/api/api-create-table-sm.mp4" type="video/mp4" />
          </video>
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Allow anonymous access">
      In this example we'll turn on [Row Level Security](/docs/guides/database/postgres/row-level-security) for this table and allow anonymous access. In production, be sure to secure your application with the appropriate permissions.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      -- Turn on security
      alter table "todos"
      enable row level security;

      -- Allow anonymous access
      create policy "Allow anonymous access"
      on todos
      for select
      to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Enable Postgres replication">
      Go to your project's [Publications settings](/dashboard/project/_/database/publications), and under `supabase_realtime`, toggle on the tables you want to listen to.

      Alternatively, add tables to the `supabase_realtime` publication by running the given SQL:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      alter publication supabase_realtime
      add table your_table_name;
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Install the client">
      Install the Supabase JavaScript client.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash
      npm install @supabase/supabase-js
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Create the client">
      This client will be used to listen to Postgres changes.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```js
      import { createClient } from '@supabase/supabase-js'

      const supabase = createClient(
        'https://<project>.supabase.co',
        '<sb_publishable_... or anon key>'
      )
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Listen to changes by schema">
      Listen to changes on all tables in the `public` schema by setting the `schema` property to 'public' and event name to `*`. The event name can be one of:

      *   `INSERT`
      *   `UPDATE`
      *   `DELETE`
      *   `*`

      The channel name can be any string except 'realtime'.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```js
      import { createClient } from '@supabase/supabase-js'
      const supabase = createClient('your_project_url', 'your_supabase_api_key')

      // ---cut---
      const channelA = supabase
        .channel('schema-db-changes')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
          },
          (payload) => console.log(payload)
        )
        .subscribe()
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Insert dummy data">
      Now we can add some data to our table which will trigger the `channelA` event handler.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      insert into todos (task)
      values
        ('Change!');
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Usage

You can use the Supabase client libraries to subscribe to database changes.


### Listening to specific schemas

Subscribe to specific schema events using the `schema` parameter:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    {/* prettier-ignore */}

    ```js
    const changes = supabase
      .channel('schema-db-changes')
      .on(
        'postgres_changes',
        {
          schema: 'public', // Subscribes to the "public" schema in Postgres
          event: '*',       // Listen to all changes
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('schema-db-changes')
        .onPostgresChanges(
            schema: 'public', // Subscribes to the "public" schema in Postgres
            event: PostgresChangeEvent.all, // Listen to all changes

            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("schema-db-changes")

    let changes = await myChannel.postgresChange(AnyAction.self, schema: "public")

    await myChannel.subscribe()

    for await change in changes {
      switch change {
      case .insert(let action): print(action)
      case .update(let action): print(action)
      case .delete(let action): print(action)
      case .select(let action): print(action)
      }
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("schema-db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction>(schema = "public")

    changes
        .onEach {
            when(it) { //You can also check for <is PostgresAction.Insert>, etc.. manually
                is HasRecord -> println(it.record)
                is HasOldRecord -> println(it.oldRecord)
                else -> println(it)
            }
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('schema-db-changes').on_postgres_changes(
      "*",
      schema="public",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

The channel name can be any string except 'realtime'.


### Listening to `INSERT` events

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Use the `event` parameter to listen only to database `INSERT`s:

    ```js
    const changes = supabase
      .channel('schema-db-changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT', // Listen only to INSERTs
          schema: 'public',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final changes = supabase
        .channel('schema-db-changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Use `InsertAction.self` as type to listen only to database `INSERT`s:

    ```swift
    let myChannel = await supabase.channel("schema-db-changes")

    let changes = await myChannel.postgresChange(InsertAction.self, schema: "public")

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Use `PostgresAction.Insert` as type to listen only to database `INSERT`s:

    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Insert>(schema = "public")

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('schema-db-changes').on_postgres_changes(
      "INSERT", # Listen only to INSERTs
      schema="public",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

The channel name can be any string except 'realtime'.


### Listening to `UPDATE` events

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Use the `event` parameter to listen only to database `UPDATE`s:

    ```js
    const changes = supabase
      .channel('schema-db-changes')
      .on(
        'postgres_changes',
        {
          event: 'UPDATE', // Listen only to UPDATEs
          schema: 'public',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('schema-db-changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.update, // Listen only to UPDATEs
            schema: 'public',
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Use `UpdateAction.self` as type to listen only to database `UPDATE`s:

    ```swift
    let myChannel = await supabase.channel("schema-db-changes")

    let changes = await myChannel.postgresChange(UpdateAction.self, schema: "public")

    await myChannel.subscribe()

    for await change in changes {
      print(change.oldRecord, change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Use `PostgresAction.Update` as type to listen only to database `UPDATE`s:

    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public")

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('schema-db-changes').on_postgres_changes(
      "UPDATE", # Listen only to UPDATEs
      schema="public",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

The channel name can be any string except 'realtime'.


### Listening to `DELETE` events

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Use the `event` parameter to listen only to database `DELETE`s:

    ```js
    const changes = supabase
      .channel('schema-db-changes')
      .on(
        'postgres_changes',
        {
          event: 'DELETE', // Listen only to DELETEs
          schema: 'public',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('schema-db-changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.delete, // Listen only to DELETEs
            schema: 'public',
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Use `DeleteAction.self` as type to listen only to database `DELETE`s:

    ```swift
    let myChannel = await supabase.channel("schema-db-changes")

    let changes = await myChannel.postgresChange(DeleteAction.self, schema: "public")

    await myChannel.subscribe()

    for await change in changes {
      print(change.oldRecord)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Use `PostgresAction.Delete` as type to listen only to database `DELETE`s:

    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Delete>(schema = "public")

    changes
        .onEach {
            println(it.oldRecord)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('schema-db-changes').on_postgres_changes(
      "DELETE", # Listen only to DELETEs
      schema="public",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

The channel name can be any string except 'realtime'.


### Listening to specific tables

Subscribe to specific table events using the `table` parameter:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const changes = supabase
      .channel('table-db-changes')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'todos',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('table-db-changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.all,
            schema: 'public',
            table: 'todos',
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(AnyAction.self, schema: "public", table: "todos")

    await myChannel.subscribe()

    for await change in changes {
      switch change {
      case .insert(let action): print(action)
      case .update(let action): print(action)
      case .delete(let action): print(action)
      case .select(let action): print(action)
      }
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction>(schema = "public") {
        table = "todos"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="todos",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

The channel name can be any string except 'realtime'.


### Listening to multiple changes

To listen to different events and schema/tables/filters combinations with the same channel:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('db-changes')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'messages',
        },
        (payload) => console.log(payload)
      )
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'users',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('db-changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.all,
            schema: 'public',
            table: 'messages',
            callback: (payload) => print(payload))
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'users',
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let messageChanges = await myChannel.postgresChange(AnyAction.self, schema: "public", table: "messages")
    let userChanges = await myChannel.postgresChange(InsertAction.self, schema: "public", table: "users")

    await myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")
    val messageChanges = myChannel.postgresChangeFlow<PostgresAction>(schema = "public") {
        table = "messages"
    }
    val userChanges = myChannel.postgresChangeFlow<PostgresAction.Insert>(schema = "public") {
        table = "users"
    }
    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "*",
      schema="public",
      table="messages"
      callback=lambda payload: print(payload)
    ).on_postgres_changes(
      "INSERT",
      schema="public",
      table="users",
      callback=lambda payload: print(payload)
    ).subscribe()
    ```
  </TabPanel>
</Tabs>


### Filtering for specific changes

Use the `filter` parameter for granular changes:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const changes = supabase
      .channel('table-filter-changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'todos',
          filter: 'id=eq.1',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
      supabase
          .channel('table-filter-changes')
          .onPostgresChanges(
              event: PostgresChangeEvent.insert,
              schema: 'public',
              table: 'todos',
              filter: PostgresChangeFilter(
                type: PostgresChangeFilterType.eq,
                column: 'id',
                value: 1,
              ),
              callback: (payload) => print(payload))
          .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      InsertAction.self,
      schema: "public",
      table: "todos",
      filter: .eq("id", value: 1)
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Insert>(schema = "public") {
        table = "todos"
        filter = "id=eq.1"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "INSERT",
      schema="public",
      table="todos",
      filter="id=eq.1",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>



## Available filters

Realtime offers filters so you can specify the data your client receives at a more granular level.


### Equal to (`eq`)

To listen to changes when a column's value in a table equals a client-specified value:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'UPDATE',
          schema: 'public',
          table: 'messages',
          filter: 'body=eq.hey',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.update,
            schema: 'public',
            table: 'messages',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.eq,
              column: 'body',
              value: 'hey',
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      UpdateAction.self,
      schema: "public",
      table: "messages",
      filter: .eq("body", value: "hey")
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "messages"
        filter = "body=eq.hey"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="messages",
      filter="body=eq.hey",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres's `=` filter.


### Not equal to (`neq`)

To listen to changes when a column's value in a table does not equal a client-specified value:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'messages',
          filter: 'body=neq.bye',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'messages',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.neq,
              column: 'body',
              value: 'bye',
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      UpdateAction.self,
      schema: "public",
      table: "messages",
      filter: .neq("body", value: "hey")
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.realtime.createChannel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "messages"
        filter = "body=neq.bye"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    supabase.realtime.connect()
    myChannel.join()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "INSERT",
      schema="public",
      table="messages",
      filter="body=neq.bye",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres's `!=` filter.


### Less than (`lt`)

To listen to changes when a column's value in a table is less than a client-specified value:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'profiles',
          filter: 'age=lt.65',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'profiles',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.lt,
              column: 'age',
              value: 65,
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      InsertAction.self,
      schema: "public",
      table: "profiles",
      filter: .lt("age", value: 65)
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Insert>(schema = "public") {
        table = "profiles"
        filter = "age=lt.65"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "INSERT",
      schema="public",
      table="profiles",
      filter="age=lt.65",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres's `<` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.


### Less than or equal to (`lte`)

To listen to changes when a column's value in a table is less than or equal to a client-specified value:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'UPDATE',
          schema: 'public',
          table: 'profiles',
          filter: 'age=lte.65',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'profiles',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.lte,
              column: 'age',
              value: 65,
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      InsertAction.self,
      schema: "public",
      table: "profiles",
      filter: .lte("age", value: 65)
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "profiles"
        filter = "age=lte.65"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="profiles",
      filter="age=lte.65",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres' `<=` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.


### Greater than (`gt`)

To listen to changes when a column's value in a table is greater than a client-specified value:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'products',
          filter: 'quantity=gt.10',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'products',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.gt,
              column: 'quantity',
              value: 10,
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      InsertAction.self,
      schema: "public",
      table: "products",
      filter: .gt("quantity", value: 10)
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "products"
        filter = "quantity=gt.10"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="products",
      filter="quantity=gt.10",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres's `>` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.


### Greater than or equal to (`gte`)

To listen to changes when a column's value in a table is greater than or equal to a client-specified value:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'products',
          filter: 'quantity=gte.10',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'products',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.gte,
              column: 'quantity',
              value: 10,
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      InsertAction.self,
      schema: "public",
      table: "products",
      filter: .gte("quantity", value: 10)
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "products"
        filter = "quantity=gte.10"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="products",
      filter="quantity=gte.10",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres's `>=` filter, so it works for non-numeric types. Make sure to check the expected behavior of the compared data's type.


### Contained in list (in)

To listen to changes when a column's value in a table equals any client-specified values:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const channel = supabase
      .channel('changes')
      .on(
        'postgres_changes',
        {
          event: 'INSERT',
          schema: 'public',
          table: 'colors',
          filter: 'name=in.(red, blue, yellow)',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase
        .channel('changes')
        .onPostgresChanges(
            event: PostgresChangeEvent.insert,
            schema: 'public',
            table: 'colors',
            filter: PostgresChangeFilter(
              type: PostgresChangeFilterType.inFilter,
              column: 'name',
              value: ['red', 'blue', 'yellow'],
            ),
            callback: (payload) => print(payload))
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      InsertAction.self,
      schema: "public",
      table: "products",
      filter: .in("name", values: ["red", "blue", "yellow"])
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "products"
        filter = "name=in.(red, blue, yellow)"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="products",
      filter="name=in.(red, blue, yellow)",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>

This filter uses Postgres's `= ANY`. Realtime allows a maximum of 100 values for this filter.



## Receiving `old` records

By default, only `new` record changes are sent but if you want to receive the `old` record (previous values) whenever you `UPDATE` or `DELETE` a record, you can set the `replica identity` of your table to `full`:

```sql
alter table
  messages replica identity full;
```

<Admonition type="caution">
  RLS policies are not applied to `DELETE` statements, because there is no way for Postgres to verify that a user has access to a deleted record. When RLS is enabled and `replica identity` is set to `full` on a table, the `old` record contains only the primary key(s).
</Admonition>



## Private schemas

Postgres Changes works out of the box for tables in the `public` schema. You can listen to tables in your private schemas by granting table `SELECT` permissions to the database role found in your access token. You can run a query similar to the following:

```sql
grant select on "non_private_schema"."some_table" to authenticated;
```

<Admonition type="caution">
  We strongly encourage you to enable RLS and create policies for tables in private schemas. Otherwise, any role you grant access to will have unfettered read access to the table.
</Admonition>



## Custom tokens

You may choose to sign your own tokens to customize claims that can be checked in your RLS policies.

Your project JWT secret is found with your [Project API keys](https://app.supabase.com/project/_/settings/api) in your dashboard.

<Admonition type="caution">
  Do not expose the `service_role` token on the client because the role is authorized to bypass row-level security.
</Admonition>

To use your own JWT with Realtime make sure to set the token after instantiating the Supabase client and before connecting to a Channel.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { createClient } = require('@supabase/supabase-js')

    const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY, {})

    // Set your custom JWT here
    supabase.realtime.setAuth('your-custom-jwt')

    const channel = supabase
      .channel('db-changes')
      .on(
        'postgres_changes',
        {
          event: '*',
          schema: 'public',
          table: 'messages',
          filter: 'body=eq.bye',
        },
        (payload) => console.log(payload)
      )
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase.realtime.setAuth('your-custom-jwt');

    supabase
        .channel('db-changes')
        .onPostgresChanges(
          event: PostgresChangeEvent.all,
          schema: 'public',
          table: 'messages',
          filter: PostgresChangeFilter(
            type: PostgresChangeFilterType.eq,
            column: 'body',
            value: 'bye',
          ),
          callback: (payload) => print(payload),
        )
        .subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    await supabase.realtime.setAuth("your-custom-jwt")

    let myChannel = await supabase.channel("db-changes")

    let changes = await myChannel.postgresChange(
      UpdateAction.self,
      schema: "public",
      table: "products",
      filter: "name=in.(red, blue, yellow)"
    )

    await myChannel.subscribe()

    for await change in changes {
      print(change.record)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val supabase = createSupabaseClient(supabaseUrl, supabaseKey) {
    	install(Realtime) {
    		jwtToken = "your-custom-jwt"
    	}
    }
    val myChannel = supabase.channel("db-changes")

    val changes = myChannel.postgresChangeFlow<PostgresAction.Update>(schema = "public") {
        table = "products"
        filter = "name=in.(red, blue, yellow)"
    }

    changes
        .onEach {
            println(it.record)
        }
        .launchIn(yourCoroutineScope)

    myChannel.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.realtime.set_auth('your-custom-jwt')

    changes = supabase.channel('db-changes').on_postgres_changes(
      "UPDATE",
      schema="public",
      table="products",
      filter="name=in.(red, blue, yellow)",
      callback=lambda payload: print(payload)
    )
    .subscribe()
    ```
  </TabPanel>
</Tabs>


### Refreshed tokens

You will need to refresh tokens on your own, but once generated, you can pass them to Realtime.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    For example, if you're using the `supabase-js` `v2` client then you can pass your token like this:

    ```js
    // Client setup

    supabase.realtime.setAuth('fresh-token')
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    supabase.realtime.setAuth('fresh-token');
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    await supabase.realtime.setAuth("fresh-token")
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    In Kotlin, you have to update the token manually per channel:

    ```kotlin
    myChannel.updateAuth("fresh-token")
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.realtime.set_auth('fresh-token')
    ```
  </TabPanel>
</Tabs>



## Limitations


### Delete events are not filterable

You can't filter Delete events when tracking Postgres Changes. This limitation is due to the way changes are pulled from Postgres.


### Spaces in table names

Realtime currently does not work when table names contain spaces.


### Database instance and realtime performance

Realtime systems usually require forethought because of their scaling dynamics. For the `Postgres Changes` feature, every change event must be checked to see if the subscribed user has access. For instance, if you have 100 users subscribed to a table where you make a single insert, it will then trigger 100 "reads": one for each user.

There can be a database bottleneck which limits message throughput. If your database cannot authorize the changes rapidly enough, the changes will be delayed until you receive a timeout.

Database changes are processed on a single thread to maintain the change order. That means compute upgrades don't have a large effect on the performance of Postgres change subscriptions. You can estimate the expected maximum throughput for your database below.

If you are using Postgres Changes at scale, you should consider using separate "public" table without RLS and filters. Alternatively, you can use Realtime server-side only and then re-stream the changes to your clients using a Realtime Broadcast.

Enter your database settings to estimate the maximum throughput for your instance:

<RealtimeLimitsEstimator />

Don't forget to run your own benchmarks to make sure that the performance is acceptable for your use case.

We are making many improvements to Realtime's Postgres Changes. If you are uncertain about the performance of your use case, reach out using [Support Form](/dashboard/support/new) and we will be happy to help you. We have a team of engineers that can advise you on the best solution for your use-case.



# Presence

Share state between users with Realtime Presence.

Let's explore how to implement Realtime Presence to track state between multiple users.



## Usage

You can use the Supabase client libraries to track Presence state between users.


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
    void main() {
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
    let supabaseURL = "https://<project>.supabase.co"
    let supabaseKey = "<sb_publishable_... or anon key>"
    let supabase = SupabaseClient(supabaseURL: URL(string: supabaseURL)!, supabaseKey: supabaseKey)

    let realtime = supabase.realtime
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
    from supabase import create_client

    SUPABASE_URL = 'https://<project>.supabase.co'
    SUPABASE_KEY = '<sb_publishable_... or anon key>'

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    ```
  </TabPanel>
</Tabs>


### Sync and track state

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Listen to the `sync`, `join`, and `leave` events triggered whenever any client joins or leaves the channel or changes their slice of state:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const roomOne = supabase.channel('room_01')

    roomOne
      .on('presence', { event: 'sync' }, () => {
        const newState = roomOne.presenceState()
        console.log('sync', newState)
      })
      .on('presence', { event: 'join' }, ({ key, newPresences }) => {
        console.log('join', key, newPresences)
      })
      .on('presence', { event: 'leave' }, ({ key, leftPresences }) => {
        console.log('leave', key, leftPresences)
      })
      .subscribe()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final supabase = Supabase.instance.client;

    final roomOne = supabase.channel('room_01');

    roomOne.onPresenceSync((_) {
      final newState = roomOne.presenceState();
      print('sync: $newState');
    }).onPresenceJoin((payload) {
      print('join: $payload');
    }).onPresenceLeave((payload) {
      print('leave: $payload');
    }).subscribe();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Listen to the presence change stream, emitting a new `PresenceAction` whenever someone joins or leaves:

    ```swift
    let roomOne = await supabase.channel("room_01")
    let presenceStream = await roomOne.presenceChange()

    await roomOne.subscribe()

    for await presence in presenceStream {
      print(presence.join) // You can also use presence.decodeJoins(as: MyType.self)
      print(presence.leaves) // You can also use presence.decodeLeaves(as: MyType.self)
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Listen to the presence change flow, emitting new a new `PresenceAction` whenever someone joins or leaves:

    ```kotlin
    val roomOne = supabase.channel("room_01")
    val presenceFlow: Flow<PresenceAction> = roomOne.presenceChangeFlow()
    presenceFlow
        .onEach {
            println(it.joins) //You can also use it.decodeJoinsAs<YourType>()
            println(it.leaves) //You can also use it.decodeLeavesAs<YourType>()
        }
        .launchIn(yourCoroutineScope) //You can also use .collect { } here

    roomOne.subscribe()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    Listen to the `sync`, `join`, and `leave` events triggered whenever any client joins or leaves the channel or changes their slice of state:

    ```python
    room_one = supabase.channel('room_01')

    room_one
      .on_presence_sync(lambda: print('sync', room_one.presenceState()))
      .on_presence_join(lambda key, curr_presences, joined_presences: print('join', key, curr_presences, joined_presences))
      .on_presence_leave(lambda key, curr_presences, left_presences: print('leave', key, curr_presences, left_presences))
      .subscribe()
    ```
  </TabPanel>
</Tabs>


### Sending state

You can send state to all subscribers using `track()`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    {/* prettier-ignore */}

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const roomOne = supabase.channel('room_01')

    const userStatus = {
      user: 'user-1',
      online_at: new Date().toISOString(),
    }

    roomOne.subscribe(async (status) => {
      if (status !== 'SUBSCRIBED') { return }

      const presenceTrackStatus = await roomOne.track(userStatus)
      console.log(presenceTrackStatus)
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final roomOne = supabase.channel('room_01');

    final userStatus = {
      'user': 'user-1',
      'online_at': DateTime.now().toIso8601String(),
    };

    roomOne.subscribe((status, error) async {
      if (status != RealtimeSubscribeStatus.subscribed) return;

      final presenceTrackStatus = await roomOne.track(userStatus);
      print(presenceTrackStatus);
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let roomOne = await supabase.channel("room_01")

    // Using a custom type
    let userStatus = UserStatus(
        user: "user-1",
        onlineAt: Date().timeIntervalSince1970
    )

    await roomOne.subscribe()

    try await roomOne.track(userStatus)

    // Or using a raw JSONObject.
    await roomOne.track(
      [
        "user": .string("user-1"),
        "onlineAt": .double(Date().timeIntervalSince1970)
      ]
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val roomOne = supabase.channel("room_01")

    val userStatus = UserStatus( //Your custom class
        user = "user-1",
        onlineAt = Clock.System.now().toEpochMilliseconds()
    )

    roomOne.subscribe(blockUntilSubscribed = true) //You can also use the roomOne.status flow instead, but this parameter will block the coroutine until the status is joined.

    roomOne.track(userStatus)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    room_one = supabase.channel('room_01')

    user_status = {
      "user": 'user-1',
      "online_at": datetime.datetime.now().isoformat(),
    }

    def on_subscribe(status, err):
      if status != RealtimeSubscribeStates.SUBSCRIBED:
        return

      room_one.track(user_status)

    room_one.subscribe(on_subscribe)
    ```
  </TabPanel>
</Tabs>

A client will receive state from any other client that is subscribed to the same topic (in this case `room_01`). It will also automatically trigger its own `sync` and `join` event handlers.


### Stop tracking

You can stop tracking presence using the `untrack()` method. This will trigger the `sync` and `leave` event handlers.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')
    const roomOne = supabase.channel('room_01')

    // ---cut---
    const untrackPresence = async () => {
      const presenceUntrackStatus = await roomOne.untrack()
      console.log(presenceUntrackStatus)
    }

    untrackPresence()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final roomOne = supabase.channel('room_01');

    untrackPresence() async {
      final presenceUntrackStatus = await roomOne.untrack();
      print(presenceUntrackStatus);
    }

    untrackPresence();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    await roomOne.untrack()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    suspend fun untrackPresence() {
    	roomOne.untrack()
    }

    untrackPresence()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    room_one.untrack()
    ```
  </TabPanel>
</Tabs>



## Presence options

You can pass configuration options while initializing the Supabase Client.


### Presence key

By default, Presence will generate a unique `UUIDv1` key on the server to track a client channel's state. If you prefer, you can provide a custom key when creating the channel. This key should be unique among clients.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('SUPABASE_URL', 'SUPABASE_PUBLISHABLE_KEY')

    const channelC = supabase.channel('test', {
      config: {
        presence: {
          key: 'userId-123',
        },
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final channelC = supabase.channel(
      'test',
      opts: const RealtimeChannelConfig(key: 'userId-123'),
    );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let channelC = await supabase.channel("test") {
      $0.presence.key = "userId-123"
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val channelC = supabase.channel("test") {
        presence {
            key = "userId-123"
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    channel_c = supabase.channel('test', {
      "config": {
        "presence": {
          "key": 'userId-123',
        },
      },
    })
    ```
  </TabPanel>
</Tabs>



# Realtime Pricing



You are charged for the number of Realtime messages and the number of Realtime peak connections.



## Messages

<Price price="2.50" /> per 1 million messages. You are only charged for usage exceeding your subscription
plan's quota.

| Plan       | Quota     | Over-Usage                                    |
| ---------- | --------- | --------------------------------------------- |
| Free       | 2 million | -                                             |
| Pro        | 5 million | <Price price="2.50" /> per 1 million messages |
| Team       | 5 million | <Price price="2.50" /> per 1 million messages |
| Enterprise | Custom    | Custom                                        |

For a detailed explanation of how charges are calculated, refer to [Manage Realtime Messages usage](/docs/guides/platform/manage-your-usage/realtime-messages).



## Peak connections

<Price price="10" /> per 1,000 peak connections. You are only charged for usage exceeding your subscription
plan's quota.

| Plan       | Quota  | Over-Usage                                      |
| ---------- | ------ | ----------------------------------------------- |
| Free       | 200    | -                                               |
| Pro        | 500    | <Price price="10" /> per 1,000 peak connections |
| Team       | 500    | <Price price="10" /> per 1,000 peak connections |
| Enterprise | Custom | Custom                                          |

For a detailed explanation of how charges are calculated, refer to [Manage Realtime Peak Connections usage](/docs/guides/platform/manage-your-usage/realtime-peak-connections).



# Realtime Protocol




## WebSocket connection setup

To start the connection we use the WebSocket URL, which for:

*   Supabase projects: `wss://<PROJECT_REF>.supabase.co/realtime/v1/websocket?apikey=<API_KEY>`
*   self-hosted projects: `wss://<HOST>:<PORT>/socket/websocket?apikey=<API_KEY>`

{/* supa-mdx-lint-disable-next-line Rule003Spelling */}

As an example, using the [websocat](https://github.com/vi/websocat), you would run the following command in your terminal:

```bash

# With Supabase
websocat "wss://<PROJECT_REF>.supabase.co/realtime/v1/websocket?apikey=<API_KEY>"


# With self-hosted
websocat "wss://<HOST>:<PORT>/socket/websocket?apikey=<API_KEY>"
```

During this stage you can also set other URL params:

*   `log_level`: sets the log level to be used by this connection to help you debug potential issues

After this you would need to send the `phx_join` event to the server to join the Channel.



## Protocol messages


### Payload format

All messages sent to the server or received from the server follow the same structure:

```ts
{
   "event": string,
   "topic": string,
   "payload": any,
   "ref": string
}
```

*   `event`: The type of event being sent or received. This can be a specific event like `phx_join`, `postgres_changes`, etc.
*   `topic`: The topic to which the message belongs. This is usually a string that identifies the channel or context of the message.
*   `payload`: The data associated with the event. This can be any JSON-serializable data structure, such as an object or an array.
*   `ref`: A unique reference ID for the message. This is used to track the message and its response on the client side when a reply is needed to proceed.


### Event types

The following are the event types from the Realtime protocol:

| Event Type         | Description                                                             | Client Sent | Server Sent | Requires Ref |
| ------------------ | ----------------------------------------------------------------------- | ----------- | ----------- | ------------ |
| `phx_join`         | Initial message to join a channel and configure features                | ✅           | ⛔           | ✅            |
| `phx_close`        | Message from server to signal channel closed                            | ⛔           | ✅           | ⛔            |
| `phx_leave`        | Message to leave a channel                                              | ✅           | ⛔           | ✅            |
| `phx_error`        | Error message sent by the server when an error occurs                   | ⛔           | ✅           | ⛔            |
| `phx_reply`        | Response to a `phx_join` or other requests                              | ⛔           | ✅           | ⛔            |
| `heartbeat`        | Heartbeat message to keep the connection alive                          | ✅           | ✅           | ✅            |
| `access_token`     | Message to update the access token                                      | ✅           | ⛔           | ⛔            |
| `system`           | System messages to inform about the status of the Postgres subscription | ⛔           | ✅           | ⛔            |
| `broadcast`        | Broadcast message sent to all clients in a channel                      | ✅           | ✅           | ⛔            |
| `presence`         | Presence state update sent after joining a channel                      | ✅           | ⛔           | ⛔            |
| `presence_state`   | Presence state sent by the server on join                               | ⛔           | ✅           | ⛔            |
| `presence_diff`    | Presence state diff update sent after a change in presence state        | ⛔           | ✅           | ⛔            |
| `postgres_changes` | Postgres CDC message containing changes to the database                 | ⛔           | ✅           | ⛔            |

Each one of these events has a specific payload field structure that defines the data it carries. Below are the details for each event type payload.


#### Payload of phx\_join

This is the initial message required to join a channel. The client sends this message to the server to join a specific topic and configure the features it wants to use, such as Postgres changes, presence, and broadcasting.

```ts
{
   "config": {
      "broadcast": {
            "ack": boolean,
            "self": boolean
            },
      "presence": {
         "enabled": boolean,
         "key": string
         },
      "postgres_changes": [
                  {
                     "event": string,
                     "schema": string,
                     "table": string,
                     "filter": string
                  }
            ]
      "private": boolean

   },
   "access_token": string
}
```

*   `config`:
    *   `private`: Whether the channel is private
    *   `broadcast`: Configuration options for broadcasting messages
        *   `ack`: Acknowledge broadcast messages
        *   `self`: Include the sender in broadcast messages
    *   `presence`: Configuration options for presence tracking
        *   `enabled`: Whether presence tracking is enabled for this channel
        *   `key`: Key to be used for presence tracking, if not specified or empty, a UUID will be generated and used
    *   `postgres_changes`: Array of configurations for Postgres changes
        *   `event`: Database change event to listen to, accepts `INSERT`, `UPDATE`, `DELETE`, or `*` to listen to all events.
        *   `schema`: Schema of the table to listen to, accepts `*` wildcard to listen to all schemas
        *   `table`: Table of the database to listen to, accepts `*` wildcard to listen to all tables
        *   `filter`: Filter to be used when pulling changes from database. Read more about filters in the usage docs for [Postgres Changes](/docs/guides/realtime/postgres-changes?queryGroups=language\&language=js#filtering-for-specific-changes)
*   `access_token`: Optional access token for authentication, if not provided, the server will use the default access token.


#### Payload of phx\_close

This message is sent by the server to signal that the channel has been closed. Payload will be empty object.


#### Payload of phx\_leave

This message is sent by the client to leave a channel. It can be used to clean up resources or stop listening for events on that channel. Payload should be empty object.


#### Payload of phx\_error

This message is sent by the server when an unexpected error occurs in the channel. Payload will be an empty object


#### Payload of phx\_reply

These messages are sent by the server on messages that expect a response. Their response can vary with the type of usage.

```ts
{
   "status": string,
   "response": any,
}
```

*   `status`: The status of the response, can be `ok` or `error`.
*   `response`: The response data, which can vary based on the event that was replied to


##### Payload of phx\_reply response to phx\_join

Contains the status of the join request and any additional information requested in the `phx_join` payload.

```ts
{
   "postgres_changes": [
      {
         "id": number,
         "event": string,
         "schema": string,
         "table": string
      }
   ]
}
```

*   `postgres_changes`: Array of Postgres changes that the client is subscribed to, each object contains:
    *   `id`: Unique identifier for the Postgres changes subscription
    *   `event`: The type of event the client is subscribed to, such as `INSERT`, `UPDATE`, `DELETE`, or `*`
    *   `schema`: The schema of the table the client is subscribed to
    *   `table`: The table the client is subscribed to


##### Payload of phx\_reply response to presence

When replying to presence events, it returns an empty object.


##### Payload of phx\_reply response on heartbeat

When replying to heartbeat events, it returns an empty object.


#### Payload of system

System messages are sent by the server to inform the client about the status of Realtime channel subscriptions.

```ts
{
   "message": string,
   "status": string,
   "extension": string,
   "channel": string
}
```

*   `message`: A human-readable message describing the status of the subscription.
*   `status`: The status of the subscription, can be `ok`, `error`, or `timeout`.
*   `extension`: The extension that sent the message.
*   `channel`: The channel to which the message belongs, such as `realtime:room1`.


#### Payload of heartbeat

The heartbeat message should be sent at least every 25 seconds to avoid a connection timeout. Payload should be empty object.

For heartbeat, use the topic `phoenix` as it needs to be sent to the WebSocket server itself and not to a channel:

```json
{ "topic": "phoenix", "event": "heartbeat", "payload": {}, "ref": "8" }
```


#### Payload of access\_token

Used to setup a new token to be used by Realtime for authentication and to refresh the token to prevent the channel from closing.

```ts
{
   "access_token": string
}
```

*   `access_token`: The new access token to be used for authentication. Either to change it or to refresh it.


#### Payload of postgres\_changes

Server sent message with a change from a listened schema and table. This message is sent when a change occurs in the database that the client is subscribed to. The payload contains the details of the change, including the schema, table, event type, and the new and old values.

```ts
{
   ,
   "ids": [
      number
   ],
   "data": {
      "schema": string,
      "table": string,
      "commit_timestamp": string,
      "eventType": "*" | "INSERT" | "UPDATE" | "DELETE",
      "new": {
         [key: string]: boolean | number | string | null
      },
      "old": {
         [key: string]: boolean | number | string | null
      },
      "errors": string | null,
      "latency": number
   }
}
```

*   `ids`: An array of unique identifiers for the changes that occurred.
*   `data`: An object containing the details of the change:
    *   `schema`: The schema of the table where the change occurred.
    *   `table`: The table where the change occurred.
    *   `commit_timestamp`: The timestamp when the change was committed to the database.
    *   `eventType`: The type of event that occurred, such as `INSERT`, `UPDATE`, `DELETE`, or `*` for all events.
    *   `new`: An object representing the new values after the change, with keys as column names and values as their corresponding values.
    *   `old`: An object representing the old values before the change, with keys as column names and values as their corresponding values.
    *   `errors`: Any errors that occurred during the change, if applicable.
    *   `latency`: The latency of the change event, in milliseconds.


### Payload of broadcast

Structure of the broadcast event to be sent to all clients in a channel. The `payload` field contains the event name and the data to broadcast.

```ts
{
   "event": string,
   "payload": json,
   "type": "broadcast"
}
```

*   `event`: The name of the event to broadcast.
*   `payload`: The data associated with the event, which can be any JSON-serializable data structure.
*   `type`: The type of message, which is always `broadcast` for broadcast messages.


### Payload of presence

Presence messages are used to track the online status of clients in a channel. When a client joins or leaves a channel, a presence message is sent to all clients in that channel.


### Payload of presence\_state

After joining, the server sends a `presence_state` message to a client with presence information. The payload field contains keys in UUID format, where each key represents a client and its value is a JSON object containing information about that client.

```ts
{
   [key: string]: {
      metas: [
         {
            phx_ref: string,
            name: string,
            t: float
         }
      ]
   }
}
```

*   `key`: The UUID of the client.
*   `metas`: An array of metadata objects for the client, each containing:
    *   `phx_ref`: A unique reference ID for the metadata.
    *   `name`: The name of the client.
    *   `t`: A timestamp indicating when the client joined or last updated its presence state.


### Payload of presence\_diff

After a change to the presence state, such as a client joining or leaving, the server sends a presence\_diff message to update the client's view of the presence state. The payload field contains two keys, `joins` and `leaves`, which represent clients that have joined and left, respectively. The values associated with each key are UUIDs of the clients.

```ts
{
   "joins": {
      metas: [{
         phx_ref: string,
         name: string,
         t: float
      }]
   },
   "leaves": {
      metas: [{
         phx_ref: string,
         name: string,
         t: float
      }]
   }
}
```

*   `joins`: An object containing metadata for clients that have joined the channel, with keys as UUIDs and values as metadata objects.
*   `leaves`: An object containing metadata for clients that have left the channel, with keys as UUIDs and values as metadata objects.



## REST API

The Realtime protocol is primarily designed for WebSocket communication, but it can also be accessed via a REST API. This allows you to interact with the Realtime service using standard HTTP methods.



---
**Navigation:** [← Previous](./04-stop-and-remove-the-containers.md) | [Index](./index.md) | [Next →](./06-realtime-quotas.md)
