**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-with-display-name-and-description.md)

---

# Exporting Billing Metrics
Source: https://docs.fireworks.ai/accounts/exporting-billing-metrics

Export billing and usage metrics for all Fireworks services

## Overview

Fireworks provides a CLI tool to export comprehensive billing metrics for all usage types including serverless inference, on-demand deployments, and fine-tuning jobs. The exported data can be used for cost analysis, internal billing, and usage tracking.

## Exporting billing metrics

Use the Fireworks CLI to export a billing CSV that includes all usage:

```bash  theme={null}
# Authenticate (once)
firectl auth login

# Export billing metrics to CSV
firectl export billing-metrics
```

## Examples

Export all billing metrics for an account:

```bash  theme={null}
firectl export billing-metrics
```

Export metrics for a specific date range and filename:

```bash  theme={null}
firectl export billing-metrics \
  --start-time "2025-01-01" \
  --end-time "2025-01-31" \
  --filename january_metrics.csv
```

## Output format

The exported CSV includes the following columns:

* **email**: Account email
* **start\_time**: Request start timestamp
* **end\_time**: Request end timestamp
* **usage\_type**: Type of usage (e.g., TEXT\_COMPLETION\_INFERENCE\_USAGE)
* **accelerator\_type**: GPU/hardware type used
* **accelerator\_seconds**: Compute time in seconds
* **base\_model\_name**: The model used
* **model\_bucket**: Model category
* **parameter\_count**: Model size
* **prompt\_tokens**: Input tokens
* **completion\_tokens**: Output tokens

### Sample row

```csv  theme={null}
email,start_time,end_time,usage_type,accelerator_type,accelerator_seconds,base_model_name,model_bucket,parameter_count,prompt_tokens,completion_tokens
user@example.com,2025-10-20 17:16:48 UTC,2025-10-20 17:16:48 UTC,TEXT_COMPLETION_INFERENCE_USAGE,,,accounts/fireworks/models/llama4-maverick-instruct-basic,Llama 4 Maverick Basic,401583781376,803,109
```

## Automation

You can automate exports in cron jobs and load the CSV into your internal systems:

```bash  theme={null}
# Example: Daily export with dated filename
firectl export billing-metrics \
  --start-time "$(date -v-1d '+%Y-%m-%d')" \
  --end-time "$(date '+%Y-%m-%d')" \
  --filename "billing_$(date '+%Y%m%d').csv"
```

<Tip>
  Run `firectl export billing-metrics --help` to see all available flags and options.
</Tip>

## Coverage

This export includes:

* **Serverless inference**: All serverless API usage
* **On-demand deployments**: Deployment usage (see also [Exporting deployment metrics](/deployments/exporting-metrics) for real-time Prometheus metrics)
* **Fine-tuning jobs**: Fine-tuning compute usage
* **Other services**: All billable Fireworks services

<Note>
  For real-time monitoring of on-demand deployment performance metrics (latency, throughput, etc.), use the [Prometheus metrics endpoint](/deployments/exporting-metrics) instead.
</Note>

## See also

* [firectl CLI overview](/tools-sdks/firectl/firectl)
* [Exporting deployment metrics](/deployments/exporting-metrics) - Real-time Prometheus metrics for on-demand deployments
* [Rate Limits & Quotas](/guides/quotas_usage/rate-limits) - Understanding spend limits and quotas


# Service Accounts
Source: https://docs.fireworks.ai/accounts/service-accounts

How to manage and use service accounts in Fireworks

Service accounts in Fireworks allow applications, scripts, and automated systems to authenticate and perform actions securely—without relying on human credentials. They are ideal for CI/CD pipelines, backend services, and automated workflows. Service Accounts let you avoid shared credentials and easily distinguish between what automated systems did vs humans in audit logs.

Service accounts can take actions using an API key, like creating deployments, running models or creating datasets (see [API reference](https://fireworks.ai/docs/api-reference/introduction)). Service accounts cannot login through the web interface or use OIDC tokens.

## Creating a Service Account

Using our firectl you can create service accounts

```bash  theme={null}
firectl create user --user-id "my-service-account" --service-account
```

## Creating an API Key for Service Account

Using our firectl you can create an api key on behalf of a service account

```bash  theme={null}
firectl create api-key --service-account "my-service-account"
```

## Billing

* Service accounts count toward the same account quotas and limits assigned to the account
* Usage is tracked by the account, not individual user vs service account

## Auditing

In audit logs users are referenced by their email id's. Service accounts are referenced by `my-service-account@my-account.sa.fireworks.ai`.


# Custom SSO
Source: https://docs.fireworks.ai/accounts/sso

Set up custom Single Sign-On (SSO) authentication for Fireworks AI

Fireworks uses single sign-on (SSO) as the primary mechanism to authenticate with the platform.
By default, Fireworks supports Google SSO.

If you have an enterprise account, Fireworks supports bringing your own identity provider using:

* OpenID Connect (OIDC) provider
* SAML 2.0 provider

<Info>
  Coordinate with your Fireworks AI representative to enable the integration.
</Info>

## OpenID Connect (OIDC) provider

<Steps>
  <Step title="Create OIDC client application">
    Create an OIDC client application in your identity provider, e.g. Okta.
  </Step>

  <Step title="Configure client">
    Ensure the client is configured for "code authorization" of the "web" type (i.e. with a client\_secret).
  </Step>

  <Step title="Set redirect URL">
    Set the client's "allowed redirect URL" to the URL provided by Fireworks. It looks like:

    ```
    https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/oauth2/idpresponse
    ```
  </Step>

  <Step title="Note down client details">
    Note down the `issuer`, `client_id`, and `client_secret` for the newly created client. You will need to provide this to your Fireworks.ai representative to complete your account set up.
  </Step>
</Steps>

## SAML 2.0 provider

<Steps>
  <Step title="Create SAML 2.0 application">
    Create a SAML 2.0 application in your identity provider, e.g. [Okta](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm).
  </Step>

  <Step title="Set SSO URL">
    Set the SSO URL to the URL provided by Fireworks. It looks like:

    ```
    https://fireworks-<your-company-name>.auth.us-west-2.amazoncognito.com/saml2/idpresponse
    ```
  </Step>

  <Step title="Configure Audience URI">
    Configure the Audience URI (SP Entity ID) as provided by Fireworks. It looks like:

    ```
    urn:amazon:cognito:sp:<some-unique-identifier>
    ```
  </Step>

  <Step title="Create Attribute Statement">
    Create an Attribute Statement with the name:

    ```
    http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
    ```

    and the value `user.email`
  </Step>

  <Step title="Keep default settings">
    Leave the rest of the settings as defaults.
  </Step>

  <Step title="Note down metadata URL">
    Note down the "metadata url" for your newly created application. You will need to provide this to your Fireworks AI representative to complete your account set up.
  </Step>
</Steps>

## Troubleshooting

### Invalid samlResponse or relayState from identity provider

This error occurs if you are trying to use identity provider (IdP) initiated login. Fireworks currently only supports
service provider (SP) initiated login.

See [Understanding SAML](https://developer.okta.com/docs/concepts/saml/#understand-sp-initiated-sign-in-flow) for an
in-depth explanation.

### Required String parameter 'RelayState' is not present

See above.


# Managing users
Source: https://docs.fireworks.ai/accounts/users

Add and delete additional users in your Fireworks account

See the concepts [page](/getting-started/concepts#account) for definitions of accounts and users. Only admin users can manage other users within the account.

## Adding users

To add a new user to your Fireworks account, run the following command. If the email for the new user is already associated with a Fireworks account, they will have the option to freely switch between your account and their existing account(s). You can also add users in the Fireworks web UI at [https://app.fireworks.ai/account/users](https://app.fireworks.ai/account/users).

```bash  theme={null}
firectl create user --email="alice@example.com"
```

To create another admin user, pass the `--role=admin` flag:

```bash  theme={null}
firectl create user --email="alice@example.com" --role=admin
```

## Updating a user's role

To update a user's role, run

```bash  theme={null}
firectl update user <USER_ID> --role="{admin,user}"
```

## Deleting users

You can remove a user from your account by running:

```bash  theme={null}
firectl delete user <USER_ID>
```


# Batch Delete Batch Jobs
Source: https://docs.fireworks.ai/api-reference-dlde/batch-delete-batch-jobs

post /v1/accounts/{account_id}/batchJobs:batchDelete



# Batch Delete Environments
Source: https://docs.fireworks.ai/api-reference-dlde/batch-delete-environments

post /v1/accounts/{account_id}/environments:batchDelete



# Batch Delete Node Pools
Source: https://docs.fireworks.ai/api-reference-dlde/batch-delete-node-pools

post /v1/accounts/{account_id}/nodePools:batchDelete



# Cancel Batch Job
Source: https://docs.fireworks.ai/api-reference-dlde/cancel-batch-job

post /v1/accounts/{account_id}/batchJobs/{batch_job_id}:cancel
Cancels an existing batch job if it is queued, pending, or running.



# Connect Environment
Source: https://docs.fireworks.ai/api-reference-dlde/connect-environment

post /v1/accounts/{account_id}/environments/{environment_id}:connect
Connects the environment to a node pool.
Returns an error if there is an existing pending connection.



# Create Aws Iam Role Binding
Source: https://docs.fireworks.ai/api-reference-dlde/create-aws-iam-role-binding

post /v1/accounts/{account_id}/awsIamRoleBindings



# Create Batch Job
Source: https://docs.fireworks.ai/api-reference-dlde/create-batch-job

post /v1/accounts/{account_id}/batchJobs



# Create Cluster
Source: https://docs.fireworks.ai/api-reference-dlde/create-cluster

post /v1/accounts/{account_id}/clusters



# Create Environment
Source: https://docs.fireworks.ai/api-reference-dlde/create-environment

post /v1/accounts/{account_id}/environments



# Create Node Pool
Source: https://docs.fireworks.ai/api-reference-dlde/create-node-pool

post /v1/accounts/{account_id}/nodePools



# Create Node Pool Binding
Source: https://docs.fireworks.ai/api-reference-dlde/create-node-pool-binding

post /v1/accounts/{account_id}/nodePoolBindings



# Create Snapshot
Source: https://docs.fireworks.ai/api-reference-dlde/create-snapshot

post /v1/accounts/{account_id}/snapshots



# Delete Aws Iam Role Binding
Source: https://docs.fireworks.ai/api-reference-dlde/delete-aws-iam-role-binding

post /v1/accounts/{account_id}/awsIamRoleBindings:delete



# Delete Batch Job
Source: https://docs.fireworks.ai/api-reference-dlde/delete-batch-job

delete /v1/accounts/{account_id}/batchJobs/{batch_job_id}



# Delete Cluster
Source: https://docs.fireworks.ai/api-reference-dlde/delete-cluster

delete /v1/accounts/{account_id}/clusters/{cluster_id}



# Delete Environment
Source: https://docs.fireworks.ai/api-reference-dlde/delete-environment

delete /v1/accounts/{account_id}/environments/{environment_id}



# Delete Node Pool
Source: https://docs.fireworks.ai/api-reference-dlde/delete-node-pool

delete /v1/accounts/{account_id}/nodePools/{node_pool_id}



# Delete Node Pool Binding
Source: https://docs.fireworks.ai/api-reference-dlde/delete-node-pool-binding

post /v1/accounts/{account_id}/nodePoolBindings:delete



# Delete Snapshot
Source: https://docs.fireworks.ai/api-reference-dlde/delete-snapshot

delete /v1/accounts/{account_id}/snapshots/{snapshot_id}



# Disconnect Environment
Source: https://docs.fireworks.ai/api-reference-dlde/disconnect-environment

post /v1/accounts/{account_id}/environments/{environment_id}:disconnect
Disconnects the environment from the node pool. Returns an error
if the environment is not connected to a node pool.



# Get Batch Job
Source: https://docs.fireworks.ai/api-reference-dlde/get-batch-job

get /v1/accounts/{account_id}/batchJobs/{batch_job_id}



# Get Batch Job Logs
Source: https://docs.fireworks.ai/api-reference-dlde/get-batch-job-logs

get /v1/accounts/{account_id}/batchJobs/{batch_job_id}:getLogs



# Get Cluster
Source: https://docs.fireworks.ai/api-reference-dlde/get-cluster

get /v1/accounts/{account_id}/clusters/{cluster_id}



# Get Cluster Connection Info
Source: https://docs.fireworks.ai/api-reference-dlde/get-cluster-connection-info

get /v1/accounts/{account_id}/clusters/{cluster_id}:getConnectionInfo
Retrieve connection settings for the cluster to be put in kubeconfig



# Get Environment
Source: https://docs.fireworks.ai/api-reference-dlde/get-environment

get /v1/accounts/{account_id}/environments/{environment_id}



# Get Node Pool
Source: https://docs.fireworks.ai/api-reference-dlde/get-node-pool

get /v1/accounts/{account_id}/nodePools/{node_pool_id}



# Get Node Pool Stats
Source: https://docs.fireworks.ai/api-reference-dlde/get-node-pool-stats

get /v1/accounts/{account_id}/nodePools/{node_pool_id}:getStats



# Get Snapshot
Source: https://docs.fireworks.ai/api-reference-dlde/get-snapshot

get /v1/accounts/{account_id}/snapshots/{snapshot_id}



# List Aws Iam Role Bindings
Source: https://docs.fireworks.ai/api-reference-dlde/list-aws-iam-role-bindings

get /v1/accounts/{account_id}/awsIamRoleBindings



# List Batch Jobs
Source: https://docs.fireworks.ai/api-reference-dlde/list-batch-jobs

get /v1/accounts/{account_id}/batchJobs



# List Clusters
Source: https://docs.fireworks.ai/api-reference-dlde/list-clusters

get /v1/accounts/{account_id}/clusters



# List Environments
Source: https://docs.fireworks.ai/api-reference-dlde/list-environments

get /v1/accounts/{account_id}/environments



# List Node Pool Bindings
Source: https://docs.fireworks.ai/api-reference-dlde/list-node-pool-bindings

get /v1/accounts/{account_id}/nodePoolBindings



# List Node Pools
Source: https://docs.fireworks.ai/api-reference-dlde/list-node-pools

get /v1/accounts/{account_id}/nodePools



# List Snapshots
Source: https://docs.fireworks.ai/api-reference-dlde/list-snapshots

get /v1/accounts/{account_id}/snapshots



# Update Batch Job
Source: https://docs.fireworks.ai/api-reference-dlde/update-batch-job

patch /v1/accounts/{account_id}/batchJobs/{batch_job_id}



# Update Cluster
Source: https://docs.fireworks.ai/api-reference-dlde/update-cluster

patch /v1/accounts/{account_id}/clusters/{cluster_id}



# Update Environment
Source: https://docs.fireworks.ai/api-reference-dlde/update-environment

patch /v1/accounts/{account_id}/environments/{environment_id}



# Update Node Pool
Source: https://docs.fireworks.ai/api-reference-dlde/update-node-pool

patch /v1/accounts/{account_id}/nodePools/{node_pool_id}



# Streaming Transcription
Source: https://docs.fireworks.ai/api-reference/audio-streaming-transcriptions

websocket /audio/transcriptions/streaming

<Steps>
  <Step title="Open a WebSocket">
    Streaming transcription is performed over a WebSocket. Provide the transcription parameters and establish a WebSocket connection to the endpoint.
  </Step>

  <Step title="Stream audio and receive transcriptions">
    Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono). In parallel, receive transcription from the WebSocket.
  </Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Try Python notebook" icon="notebook" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb">
    Stream audio to get transcription continuously in real-time.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Explore Python sources" icon="code" href="https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/python">
    Stream audio to get transcription continuously in real-time.
  </Card>

  <Card title="Explore Node.js sources" icon="code" href="https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/nodejs">
    Stream audio to get transcription continuously in real-time.
  </Card>
</CardGroup>

### URLs

Fireworks provides serverless, real-time ASR via WebSocket endpoints. Please select the appropriate version:

#### Streaming ASR v1 (default)

Production-ready and generally recommended for all use cases.

```
wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming
```

#### Streaming ASR v2 (preview)

An early-access version of our next-generation streaming transcription service. V2 is good for use cases that require lower latency and higher accuracy in noisy situations.

```
wss://audio-streaming-v2.api.fireworks.ai/v1/audio/transcriptions/streaming
```

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Query Parameters

<ParamField query="Authorization" type="string" optional>
  Your Fireworks API key. Required when headers cannot be set (e.g., browser WebSocket connections). Can alternatively be provided via the Authorization header.
</ParamField>

<ParamField query="response_format" type="string" default="verbose_json" optional>
  The format in which to return the response. Currently only `verbose_json` is recommended for streaming.
</ParamField>

<ParamField query="language" type="string | null" optional>
  The target language for transcription. See the [Supported Languages](#supported-languages) section below for a complete list of available languages.
</ParamField>

<ParamField query="prompt" type="string | null" optional>
  The input prompt that the model will use when generating the transcription. Can be used to specify custom words or specify the style of the transcription. E.g. `Um, here's, uh, what was recorded.` will make the model to include the filler words into the transcription.
</ParamField>

<ParamField query="temperature" type="float" default="0">
  Sampling temperature to use when decoding text tokens during transcription.
</ParamField>

<ParamField query="timestamp_granularities" type="string | list[string] | null" optional>
  The timestamp granularities to populate for this streaming transcription. Defaults to null. Set to `word,segment` to enable timestamp granularities. Use a list for timestamp\_granularities in all client libraries. A comma-separated string like `word,segment` only works when manually included in the URL (e.g. in curl).
</ParamField>

### Client messages

<Tabs>
  <Tab title="binary">
    This field is for client to send audio chunks over to server. Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono).
  </Tab>

  <Tab title="SttStateClear">
    This field is for client event initiating the context clean up.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.state.clear">
      A constant string that identifies the type of event as "stt.state.clear".
    </ResponseField>

    <ResponseField name="reset_id" type="string">
      The ID of the context or session to be cleared.
    </ResponseField>
  </Tab>

  <Tab title="SttInputTrace">
    This field is for client event initiating tracing.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.input.trace">
      A constant string indicating the event type is "stt.input.trace".
    </ResponseField>

    <ResponseField name="trace_id" type="string">
      The ID used to correlate this trace event across systems.
    </ResponseField>
  </Tab>
</Tabs>

### Server messages

<Tabs>
  <Tab title="json">
    <ResponseField name="task" type="string" default="transcribe" required>
      The task that was performed — either `transcribe` or `translate`.
    </ResponseField>

    <ResponseField name="language" type="string" required>
      The language of the transcribed/translated text.
    </ResponseField>

    <ResponseField name="text" type="string" required>
      The transcribed/translated text.
    </ResponseField>

    <ResponseField name="words" type="object[] | null" optional>
      Extracted words and their corresponding timestamps.

      <Expandable title="Word properties">
        <ResponseField name="word" type="string" required>
          The text content of the word.
        </ResponseField>

        <ResponseField name="language" type="string" required>
          The language of the word.
        </ResponseField>

        <ResponseField name="probability" type="number" required>
          The probability of the word.
        </ResponseField>

        <ResponseField name="hallucination_score" type="number" required>
          The hallucination score of the word.
        </ResponseField>

        <ResponseField name="start" type="number" optional>
          Start time of the word in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="end" type="number" optional>
          End time of the word in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="is_final" type="bool" required>
          Indicates whether this word has been finalized.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segments" type="object[] | null" optional>
      Segments of the transcribed/translated text and their corresponding details.

      <Expandable title="Segment properties (partial)">
        <ResponseField name="id" type="number" required>
          The ID of the segment.
        </ResponseField>

        <ResponseField name="text" type="string" required>
          The text content of the segment.
        </ResponseField>

        <ResponseField name="words" type="object[] | null" optional>
          Extracted words in the segment.
        </ResponseField>

        <ResponseField name="start" type="number" optional>
          Start time of the segment in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="end" type="number" optional>
          End time of the segment in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>

  <Tab title="SttStateCleared">
    This field is for server to communicate it successfully cleared the context.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.state.cleared">
      A constant string indicating the event type is "stt.state.cleared"
    </ResponseField>

    <ResponseField name="reset_id" type="string">
      The ID of the context or session that has been successfully cleared.
    </ResponseField>
  </Tab>

  <Tab title="SttOutputTrace">
    This field is for server to complete tracing.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.output.trace">
      A constant string indicating the event type is "stt.output.trace".
    </ResponseField>

    <ResponseField name="trace_id" type="string">
      The ID used to correlate this output trace with the corresponding input trace.
    </ResponseField>
  </Tab>
</Tabs>

### Streaming Audio

Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono).  Typically, you will:

1. Resample your audio to 16 kHz if it is not already.
2. Convert it to mono.
3. Send 50ms chunks (16,000 Hz \* 0.05s = 800 samples) of audio in 16-bit PCM (signed, little-endian) format.

### Handling Responses

The client maintains a state dictionary, starting with an empty dictionary `{}`. When the server sends the first transcription message, it contains a list of segments. Each segment has an `id` and `text`:

```python  theme={null}
# Server initial message:
{
    "segments": [
        {"id": "0", "text": "This is the first sentence"},
        {"id": "1", "text": "This is the second sentence"}
    ]
}

# Client initial state:
{
    "0": "This is the first sentence",
    "1": "This is the second sentence",
}
```

When the server sends the next updates to the transcription, the client updates the state dictionary based on the segment `id`:

```python  theme={null}
# Server continuous message:
{
    "segments": [
        {"id": "1", "text": "This is the second sentence modified"},
        {"id": "2", "text": "This is the third sentence"}
    ]
}

# Client updated state:
{
    "0": "This is the first sentence",
    "1": "This is the second sentence modified",   # overwritten
    "2": "This is the third sentence",             # new
}
```

### Handling Connection Interruptions & Timeouts

Real-time streaming transcription over WebSockets can run for a long time. The longer a WebSocket session runs, the more likely it is to experience interruptions from network glitches to service hiccups.
It is important to be aware of this and build your client to recover gracefully so the stream keeps going without user impact.

In the following section, we’ll outline recommended practices for handling connection interruptions and timeouts effectively.

#### When a connection drops

Although Fireworks is designed to keep streams running smoothly, occasional interruptions can still occur. If the WebSocket is disrupted (e.g., bandwidth limitation or network failures),
your application must initialize a new WebSocket connection, start a fresh streaming session and begin sending audio as soon as the server confirms the connection is open.

#### Avoid losing audio during reconnects

While you’re reconnecting, audio could be still being produced and you could lose that audio segment if it is not transferred to our API during this period.
To minimize the risk of dropping audio during a reconnect, one effective approach is to store the audio data in a buffer until it can re-establish the connection to our API and then sends the data for transcription.

### Keep timestamps continuous across sessions

When timestamps are enabled, the result will include the start and end time of the segment in seconds. And each new WebSocket session will reset the timestamps to start from 00:00:00.

To keep a continuous timeline, we recommend to maintain a running “stream start offset” in your app and add that offset to timestamps from each new session so they align with the overall audio timeline.

### Example Usage

Check out a brief Python example below or example sources:

* [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
* [Python sources](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/python)
* [Node.js sources](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/nodejs)

<CodeGroup>
  ```python  theme={null}
  !pip3 install requests torch torchaudio websocket-client

  import io
  import time
  import json
  import torch
  import requests
  import torchaudio
  import threading
  import websocket
  import urllib.parse

  lock = threading.Lock()
  state = {}

  def on_open(ws):
      def send_audio_chunks():
          for chunk in audio_chunk_bytes:
              ws.send(chunk, opcode=websocket.ABNF.OPCODE_BINARY)
              time.sleep(chunk_size_ms / 1000)

          final_checkpoint = json.dumps({"checkpoint_id": "final"})
          ws.send(final_checkpoint, opcode=websocket.ABNF.OPCODE_TEXT)

      threading.Thread(target=send_audio_chunks).start()

  def on_message(ws, message):
      message = json.loads(message)
      if message.get("checkpoint_id") == "final":
          ws.close()
          return

      update = {s["id"]: s["text"] for s in message["segments"]}
      with lock:
          state.update(update)
          print("\n".join(f" - {k}: {v}" for k, v in state.items()))

  def on_error(ws, error):
      print(f"WebSocket error: {error}")

  # Open a connection URL with query params
  url = "wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming"
  params = urllib.parse.urlencode({
      "language": "en",
  })
  ws = websocket.WebSocketApp(
      f"{url}?{params}",
      header={"Authorization": "<FIREWORKS_API_KEY>"},
      on_open=on_open,
      on_message=on_message,
      on_error=on_error,
  )
  ws.run_forever()
  ```
</CodeGroup>

### Dedicated endpoint

For fixed throughput and predictable SLAs, you may request a dedicated endpoint for streaming transcription at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) or [discord](https://www.google.com/url?q=https%3A%2F%2Fdiscord.gg%2Ffireworks-ai).

### Supported Languages

The following languages are supported for transcription:

| Language Code | Language Name       |
| ------------- | ------------------- |
| en            | English             |
| zh            | Chinese             |
| de            | German              |
| es            | Spanish             |
| ru            | Russian             |
| ko            | Korean              |
| fr            | French              |
| ja            | Japanese            |
| pt            | Portuguese          |
| tr            | Turkish             |
| pl            | Polish              |
| ca            | Catalan             |
| nl            | Dutch               |
| ar            | Arabic              |
| sv            | Swedish             |
| it            | Italian             |
| id            | Indonesian          |
| hi            | Hindi               |
| fi            | Finnish             |
| vi            | Vietnamese          |
| he            | Hebrew              |
| uk            | Ukrainian           |
| el            | Greek               |
| ms            | Malay               |
| cs            | Czech               |
| ro            | Romanian            |
| da            | Danish              |
| hu            | Hungarian           |
| ta            | Tamil               |
| no            | Norwegian           |
| th            | Thai                |
| ur            | Urdu                |
| hr            | Croatian            |
| bg            | Bulgarian           |
| lt            | Lithuanian          |
| la            | Latin               |
| mi            | Maori               |
| ml            | Malayalam           |
| cy            | Welsh               |
| sk            | Slovak              |
| te            | Telugu              |
| fa            | Persian             |
| lv            | Latvian             |
| bn            | Bengali             |
| sr            | Serbian             |
| az            | Azerbaijani         |
| sl            | Slovenian           |
| kn            | Kannada             |
| et            | Estonian            |
| mk            | Macedonian          |
| br            | Breton              |
| eu            | Basque              |
| is            | Icelandic           |
| hy            | Armenian            |
| ne            | Nepali              |
| mn            | Mongolian           |
| bs            | Bosnian             |
| kk            | Kazakh              |
| sq            | Albanian            |
| sw            | Swahili             |
| gl            | Galician            |
| mr            | Marathi             |
| pa            | Punjabi             |
| si            | Sinhala             |
| km            | Khmer               |
| sn            | Shona               |
| yo            | Yoruba              |
| so            | Somali              |
| af            | Afrikaans           |
| oc            | Occitan             |
| ka            | Georgian            |
| be            | Belarusian          |
| tg            | Tajik               |
| sd            | Sindhi              |
| gu            | Gujarati            |
| am            | Amharic             |
| yi            | Yiddish             |
| lo            | Lao                 |
| uz            | Uzbek               |
| fo            | Faroese             |
| ht            | Haitian Creole      |
| ps            | Pashto              |
| tk            | Turkmen             |
| nn            | Nynorsk             |
| mt            | Maltese             |
| sa            | Sanskrit            |
| lb            | Luxembourgish       |
| my            | Myanmar             |
| bo            | Tibetan             |
| tl            | Tagalog             |
| mg            | Malagasy            |
| as            | Assamese            |
| tt            | Tatar               |
| haw           | Hawaiian            |
| ln            | Lingala             |
| ha            | Hausa               |
| ba            | Bashkir             |
| jw            | Javanese            |
| su            | Sundanese           |
| yue           | Cantonese           |
| zh-hant       | Traditional Chinese |
| zh-hans       | Simplified Chinese  |


# Transcribe audio
Source: https://docs.fireworks.ai/api-reference/audio-transcriptions

post /audio/transcriptions

<CardGroup cols={1}>
  <Card title="Try notebook" icon="rocket" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_prerecorded_speech_to_text/audio_prerecorded_speech_to_text.ipynb">
    Send a sample audio to get a transcription.
  </Card>
</CardGroup>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=API_KEY`.
</ParamField>

### Request

##### (multi-part form)

<ParamField query="file" type="file | string" required>
  The input audio file to transcribe or an URL to the public audio file.

  Max audio file size is 1 GB, there is no limit for audio duration. Common file formats such as mp3, flac, and wav are supported. Note that the audio will be resampled to 16kHz, downmixed to mono, and reformatted to 16-bit signed little-endian format before transcription. Pre-converting the file before sending it to the API can improve runtime performance.
</ParamField>

<ParamField query="model" type="string" default="whisper-v3" optional>
  String name of the ASR model to use. Can be one of `whisper-v3` or `whisper-v3-turbo`. Please use the following serverless endpoints:

  * [https://audio-prod.api.fireworks.ai](https://audio-prod.api.fireworks.ai) (for `whisper-v3`);
  * [https://audio-turbo.api.fireworks.ai](https://audio-turbo.api.fireworks.ai) (for `whisper-v3-turbo`);
</ParamField>

<ParamField query="vad_model" type="string" default="silero" optional>
  String name of the voice activity detection (VAD) model to use. Can be one of `silero`, or `whisperx-pyannet`.
</ParamField>

<ParamField query="alignment_model" type="string" default="mms_fa" optional>
  String name of the alignment model to use. Currently supported:

  * `mms_fa` optimal accuracy for multilingual speech.
  * `tdnn_ffn` optimal accuracy for English-only speech.
  * `gentle` best accuracy for English-only speech (requires a dedicated endpoint, contact us at <a href="mailto:inquiries@fireworks.ai">[inquiries@fireworks.ai](mailto:inquiries@fireworks.ai)</a>).
</ParamField>

<ParamField query="language" type="string | null" optional>
  The target language for transcription. See the [Supported Languages](#supported-languages) section below for a complete list of available languages.
</ParamField>

<ParamField query="prompt" type="string | null" optional>
  The input prompt that the model will use when generating the transcription. Can be used to specify custom words or specify the style of the transcription. E.g. `Um, here's, uh, what was recorded.` will make the model to include the filler words into the transcription.
</ParamField>

<ParamField query="temperature" type="float | list[float]" default="0">
  Sampling temperature to use when decoding text tokens during transcription. Alternatively, fallback decoding can be enabled by passing a list of temperatures like `0.0,0.2,0.4,0.6,0.8,1.0`. This can help to improve performance.
</ParamField>

<ParamField query="response_format" type="string" default="json">
  The format in which to return the response. Can be one of `json`, `text`, `srt`, `verbose_json`, or `vtt`.
</ParamField>

<ParamField query="timestamp_granularities" type="string | list[string]" optional>
  The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported. Can be one of `word`, `segment`, or `word,segment`. If not present, defaults to `segment`.
</ParamField>

<ParamField query="diarize" type="string" optional>
  Whether to get speaker diarization for the transcription. Can be one of `true`, or `false`. If not present, defaults to `false`.

  Enabling diarization also requires other fields to hold specific values:

  1. `response_format` must be set `verbose_json`.
  2. `timestamp_granularities` must include `word` to use diarization.
</ParamField>

<ParamField query="min_speakers" type="int" optional>
  The minimum number of speakers to detect for diarization. `diarize` must be set `true` to use `min_speakers`. If not present, defaults to `1`.
</ParamField>

<ParamField query="max_speakers" type="int" optional>
  The maximum number of speakers to detect for diarization. `diarize` must be set `true` to use `max_speakers`. If not present, defaults to `inf`.
</ParamField>

<ParamField query="preprocessing" type="string" optional>
  Audio preprocessing mode. Currently supported:

  * `none` to skip audio preprocessing.
  * `dynamic` for arbitrary audio content with variable loudness.
  * `soft_dynamic` for speech intense recording such as podcasts and voice-overs.
  * `bass_dynamic` for boosting lower frequencies;
</ParamField>

### Response

<Tabs>
  <Tab title="json/text/srt/vtt">
    <ResponseField name="text" type="string" required />
  </Tab>

  <Tab title="verbose_json">
    <ResponseField name="task" type="string" default="transcribe" required>
      The task which was performed. Either `transcribe` or `translate`.
    </ResponseField>

    <ResponseField name="language" type="string" required>
      The language of the transcribed/translated text.
    </ResponseField>

    <ResponseField name="duration" type="number" required>
      The duration of the transcribed/translated audio, in seconds.
    </ResponseField>

    <ResponseField name="text" type="string" required>
      The transcribed/translated text.
    </ResponseField>

    <ResponseField name="words" type="object[] | null" optional>
      Extracted words and their corresponding timestamps.

      <Expandable title="Word properties">
        <ResponseField name="word" type="string" required>
          The text content of the word.
        </ResponseField>

        <ResponseField name="language" type="string" required>
          The language of the word.
        </ResponseField>

        <ResponseField name="probability" type="number" required>
          The probability of the word.
        </ResponseField>

        <ResponseField name="hallucination_score" type="number" required>
          The hallucination score of the word.
        </ResponseField>

        <ResponseField name="start" type="number" required>
          Start time of the word in seconds.
        </ResponseField>

        <ResponseField name="end" type="number" required>
          End time of the word in seconds.
        </ResponseField>

        <ResponseField name="speaker_id" type="string" optional>
          Speaker label for the word.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segments" type="object[] | null" optional>
      Segments of the transcribed/translated text and their corresponding details.

      <Expandable title="Segment properties (partial)">
        <ResponseField name="id" type="number" required>
          The id of the segment.
        </ResponseField>

        <ResponseField name="text" type="string" required>
          The text content of the segment.
        </ResponseField>

        <ResponseField name="start" type="number" required>
          Start time of the segment in seconds.
        </ResponseField>

        <ResponseField name="end" type="number" required>
          End time of the segment in seconds.
        </ResponseField>

        <ResponseField name="speaker_id" type="string" optional>
          Speaker label for the segment.
        </ResponseField>

        <ResponseField name="words" type="object[] | null" optional>
          Extracted words in the segment.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
  ```curl curl theme={null}

  # Download audio file
  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request
  curl -X POST "https://audio-prod.api.fireworks.ai/v1/audio/transcriptions" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
  ```

  ```python fireworks sdk theme={null}
  !pip install fireworks-ai requests python-dotenv

  from fireworks.client.audio import AudioInference
  import requests
  import os
  from dotenv import load_dotenv
  import time

  # Create a .env file with your API key
  load_dotenv()


  # Download audio sample
  audio = requests.get("https://tinyurl.com/4cb74vas").content

  # Prepare client
  client = AudioInference(
      model="whisper-v3",
      base_url="https://audio-prod.api.fireworks.ai",
      # Or for the turbo version
      # model="whisper-v3-turbo",
      # base_url="https://audio-turbo.api.fireworks.ai",
      api_key=os.getenv("FIREWORKS_API_KEY"),
  )

  # Make request
  start = time.time()
  r = await client.transcribe_async(audio=audio)
  print(f"Took: {(time.time() - start):.3f}s. Text: '{r.text}'")
  ```

  ```python Python (openai sdk) theme={null}
  !pip install openai requests python-dotenv

  from openai import OpenAI
  import os
  import requests
  from dotenv import load_dotenv

  load_dotenv()

  client = OpenAI(
      base_url="https://audio-prod.api.fireworks.ai/v1",
      api_key=os.getenv("FIREWORKS_API_KEY")
      )
  audio_file= requests.get("https://tinyurl.com/4cb74vas").content
  transcription = client.audio.transcriptions.create(
      model="whisper-v3",
      file=audio_file
  )
  print(transcription.text)
  ```
</RequestExample>

### Supported Languages

The following languages are supported for transcription:

<Accordion title="Language Code & Name">
  | Language Code | Language Name       |
  | ------------- | ------------------- |
  | en            | English             |
  | zh            | Chinese             |
  | de            | German              |
  | es            | Spanish             |
  | ru            | Russian             |
  | ko            | Korean              |
  | fr            | French              |
  | ja            | Japanese            |
  | pt            | Portuguese          |
  | tr            | Turkish             |
  | pl            | Polish              |
  | ca            | Catalan             |
  | nl            | Dutch               |
  | ar            | Arabic              |
  | sv            | Swedish             |
  | it            | Italian             |
  | id            | Indonesian          |
  | hi            | Hindi               |
  | fi            | Finnish             |
  | vi            | Vietnamese          |
  | he            | Hebrew              |
  | uk            | Ukrainian           |
  | el            | Greek               |
  | ms            | Malay               |
  | cs            | Czech               |
  | ro            | Romanian            |
  | da            | Danish              |
  | hu            | Hungarian           |
  | ta            | Tamil               |
  | no            | Norwegian           |
  | th            | Thai                |
  | ur            | Urdu                |
  | hr            | Croatian            |
  | bg            | Bulgarian           |
  | lt            | Lithuanian          |
  | la            | Latin               |
  | mi            | Maori               |
  | ml            | Malayalam           |
  | cy            | Welsh               |
  | sk            | Slovak              |
  | te            | Telugu              |
  | fa            | Persian             |
  | lv            | Latvian             |
  | bn            | Bengali             |
  | sr            | Serbian             |
  | az            | Azerbaijani         |
  | sl            | Slovenian           |
  | kn            | Kannada             |
  | et            | Estonian            |
  | mk            | Macedonian          |
  | br            | Breton              |
  | eu            | Basque              |
  | is            | Icelandic           |
  | hy            | Armenian            |
  | ne            | Nepali              |
  | mn            | Mongolian           |
  | bs            | Bosnian             |
  | kk            | Kazakh              |
  | sq            | Albanian            |
  | sw            | Swahili             |
  | gl            | Galician            |
  | mr            | Marathi             |
  | pa            | Punjabi             |
  | si            | Sinhala             |
  | km            | Khmer               |
  | sn            | Shona               |
  | yo            | Yoruba              |
  | so            | Somali              |
  | af            | Afrikaans           |
  | oc            | Occitan             |
  | ka            | Georgian            |
  | be            | Belarusian          |
  | tg            | Tajik               |
  | sd            | Sindhi              |
  | gu            | Gujarati            |
  | am            | Amharic             |
  | yi            | Yiddish             |
  | lo            | Lao                 |
  | uz            | Uzbek               |
  | fo            | Faroese             |
  | ht            | Haitian Creole      |
  | ps            | Pashto              |
  | tk            | Turkmen             |
  | nn            | Nynorsk             |
  | mt            | Maltese             |
  | sa            | Sanskrit            |
  | lb            | Luxembourgish       |
  | my            | Myanmar             |
  | bo            | Tibetan             |
  | tl            | Tagalog             |
  | mg            | Malagasy            |
  | as            | Assamese            |
  | tt            | Tatar               |
  | haw           | Hawaiian            |
  | ln            | Lingala             |
  | ha            | Hausa               |
  | ba            | Bashkir             |
  | jw            | Javanese            |
  | su            | Sundanese           |
  | yue           | Cantonese           |
  | zh-hant       | Traditional Chinese |
  | zh-hans       | Simplified Chinese  |
</Accordion>


# Translate audio
Source: https://docs.fireworks.ai/api-reference/audio-translations

post /audio/translations

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=API_KEY`.
</ParamField>

### Request

##### (multi-part form)

<ParamField query="file" type="file | string" required>
  The input audio file to translate or an URL to the public audio file.

  Max audio file size is 1 GB, there is no limit for audio duration. Common file formats such as mp3, flac, and wav are supported. Note that the audio will be resampled to 16kHz, downmixed to mono, and reformatted to 16-bit signed little-endian format before transcription. Pre-converting the file before sending it to the API can improve runtime performance.
</ParamField>

<ParamField query="model" type="string" default="whisper-v3" optional>
  String name of the ASR model to use. Can be one of `whisper-v3` or `whisper-v3-turbo`. Please use the following serverless endpoints:

  * [https://audio-prod.api.fireworks.ai](https://audio-prod.api.fireworks.ai) (for `whisper-v3`);
  * [https://audio-turbo.api.fireworks.ai](https://audio-turbo.api.fireworks.ai) (for `whisper-v3-turbo`);
</ParamField>

<ParamField query="vad_model" type="string" default="silero" optional>
  String name of the voice activity detection (VAD) model to use. Can be one of `silero`, or `whisperx-pyannet`.
</ParamField>

<ParamField query="alignment_model" type="string" default="mms_fa" optional>
  String name of the alignment model to use. Currently supported:

  * `mms_fa` optimal accuracy for multilingual speech.
  * `tdnn_ffn` optimal accuracy for English-only speech.
  * `gentle` best accuracy for English-only speech (requires a dedicated endpoint, contact us at <a href="mailto:inquiries@fireworks.ai">[inquiries@fireworks.ai](mailto:inquiries@fireworks.ai)</a>).
</ParamField>

<ParamField query="language" type="string | null" optional>
  The source language for transcription. See the [Supported Languages](#supported-languages) section below for a complete list of available languages.
</ParamField>

<ParamField query="prompt" type="string | null" optional>
  The input prompt that the model will use when generating the transcription. Can be used to specify custom words or specify the style of the transcription. E.g. `Um, here's, uh, what was recorded.` will make the model to include the filler words into the transcription.
</ParamField>

<ParamField query="temperature" type="float | list[float]" default="0">
  Sampling temperature to use when decoding text tokens during transcription. Alternatively, fallback decoding can be enabled by passing a list of temperatures like `0.0,0.2,0.4,0.6,0.8,1.0`. This can help to improve performance.
</ParamField>

<ParamField query="response_format" type="string" default="json">
  The format in which to return the response. Can be one of `json`, `text`, `srt`, `verbose_json`, or `vtt`.
</ParamField>

<ParamField query="timestamp_granularities" type="string | list[string]" optional>
  The timestamp granularities to populate for this transcription. response\_format must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported. Can be one of `word`, `segment`, or `word,segment`. If not present, defaults to `segment`.
</ParamField>

<ParamField query="preprocessing" type="string" optional>
  Audio preprocessing mode. Currently supported:

  * `none` to skip audio preprocessing.
  * `dynamic` for arbitrary audio content with variable loudness.
  * `soft_dynamic` for speech intense recording such as podcasts and voice-overs.
  * `bass_dynamic` for boosting lower frequencies;
</ParamField>

### Response

<Tabs>
  <Tab title="json/text/srt/vtt">
    <ResponseField name="text" type="string" required />
  </Tab>

  <Tab title="verbose_json">
    <ResponseField name="task" type="string" default="transcribe" required>
      The task which was performed. Either `transcribe` or `translate`.
    </ResponseField>

    <ResponseField name="language" type="string" required>
      The language of the transcribed/translated text.
    </ResponseField>

    <ResponseField name="duration" type="number" required>
      The duration of the transcribed/translated audio, in seconds.
    </ResponseField>

    <ResponseField name="text" type="string" required>
      The transcribed/translated text.
    </ResponseField>

    <ResponseField name="words" type="object" optional>
      Extracted words and their corresponding timestamps.

      <Expandable title="properties">
        <ResponseField name="word" type="string" required>
          The text content of the word.
        </ResponseField>

        <ResponseField name="words.start" type="number" required>
          Start time of the word in seconds.
        </ResponseField>

        <ResponseField name="words.end" type="number" required>
          End time of the word in seconds.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segments" type="object[] | null" optional>
      Segments of the transcribed/translated text and their corresponding details.
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
  ```curl curl theme={null}

  # Download audio file
  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request
  curl -X POST "https://audio-prod.api.fireworks.ai/v1/audio/translations" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
  ```

  ```python Python (fireworks sdk) theme={null}
  !pip install fireworks-ai requests

  from fireworks.client.audio import AudioInference
  import requests
  import time
  from dotenv import load_dotenv
  import os

  load_dotenv()

  # Prepare client
  audio = requests.get("https://tinyurl.com/3cy7x44v").content
  client = AudioInference(
      model="whisper-v3",
      base_url="https://audio-prod.api.fireworks.ai",
      #
      # Or for the turbo version
      # model="whisper-v3-turbo",
      # base_url="https://audio-turbo.api.fireworks.ai",
      api_key=os.getenv("FIREWORKS_API_KEY")
  )

  # Make request
  start = time.time()
  r = await client.translate_async(audio=audio)
  print(f"Took: {(time.time() - start):.3f}s. Text: '{r.text}'")
  ```

  ```python Python (openai sdk) theme={null}
  !pip install openai requests 
  from openai import OpenAI
  import requests
  from dotenv import load_dotenv
  import os

  load_dotenv()

  client = OpenAI(
      base_url="https://audio-prod.api.fireworks.ai/v1",
      api_key=os.getenv("FIREWORKS_API_KEY"),
          )
  audio_file= requests.get("https://tinyurl.com/3cy7x44v").content

  translation = client.audio.translations.create(
      model="whisper-v3", 
      file=audio_file,
  )

  print(translation.text)
  ```
</RequestExample>

### Supported Languages

Translation is from one of the supported languages to English, the following languages are supported for translation:

<Accordion title="Language Code & Name">
  | Language Code | Language Name  |
  | ------------- | -------------- |
  | en            | English        |
  | zh            | Chinese        |
  | de            | German         |
  | es            | Spanish        |
  | ru            | Russian        |
  | ko            | Korean         |
  | fr            | French         |
  | ja            | Japanese       |
  | pt            | Portuguese     |
  | tr            | Turkish        |
  | pl            | Polish         |
  | ca            | Catalan        |
  | nl            | Dutch          |
  | ar            | Arabic         |
  | sv            | Swedish        |
  | it            | Italian        |
  | id            | Indonesian     |
  | hi            | Hindi          |
  | fi            | Finnish        |
  | vi            | Vietnamese     |
  | he            | Hebrew         |
  | uk            | Ukrainian      |
  | el            | Greek          |
  | ms            | Malay          |
  | cs            | Czech          |
  | ro            | Romanian       |
  | da            | Danish         |
  | hu            | Hungarian      |
  | ta            | Tamil          |
  | no            | Norwegian      |
  | th            | Thai           |
  | ur            | Urdu           |
  | hr            | Croatian       |
  | bg            | Bulgarian      |
  | lt            | Lithuanian     |
  | la            | Latin          |
  | mi            | Maori          |
  | ml            | Malayalam      |
  | cy            | Welsh          |
  | sk            | Slovak         |
  | te            | Telugu         |
  | fa            | Persian        |
  | lv            | Latvian        |
  | bn            | Bengali        |
  | sr            | Serbian        |
  | az            | Azerbaijani    |
  | sl            | Slovenian      |
  | kn            | Kannada        |
  | et            | Estonian       |
  | mk            | Macedonian     |
  | br            | Breton         |
  | eu            | Basque         |
  | is            | Icelandic      |
  | hy            | Armenian       |
  | ne            | Nepali         |
  | mn            | Mongolian      |
  | bs            | Bosnian        |
  | kk            | Kazakh         |
  | sq            | Albanian       |
  | sw            | Swahili        |
  | gl            | Galician       |
  | mr            | Marathi        |
  | pa            | Punjabi        |
  | si            | Sinhala        |
  | km            | Khmer          |
  | sn            | Shona          |
  | yo            | Yoruba         |
  | so            | Somali         |
  | af            | Afrikaans      |
  | oc            | Occitan        |
  | ka            | Georgian       |
  | be            | Belarusian     |
  | tg            | Tajik          |
  | sd            | Sindhi         |
  | gu            | Gujarati       |
  | am            | Amharic        |
  | yi            | Yiddish        |
  | lo            | Lao            |
  | uz            | Uzbek          |
  | fo            | Faroese        |
  | ht            | Haitian Creole |
  | ps            | Pashto         |
  | tk            | Turkmen        |
  | nn            | Nynorsk        |
  | mt            | Maltese        |
  | sa            | Sanskrit       |
  | lb            | Luxembourgish  |
  | my            | Myanmar        |
  | bo            | Tibetan        |
  | tl            | Tagalog        |
  | mg            | Malagasy       |
  | as            | Assamese       |
  | tt            | Tatar          |
  | haw           | Hawaiian       |
  | ln            | Lingala        |
  | ha            | Hausa          |
  | ba            | Bashkir        |
  | jw            | Javanese       |
  | su            | Sundanese      |
  | yue           | Cantonese      |
</Accordion>


# Cancel Reinforcement Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/cancel-reinforcement-fine-tuning-job

post /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:cancel



# Create API Key
Source: https://docs.fireworks.ai/api-reference/create-api-key

post /v1/accounts/{account_id}/users/{user_id}/apiKeys



# Create Batch Inference Job
Source: https://docs.fireworks.ai/api-reference/create-batch-inference-job

post /v1/accounts/{account_id}/batchInferenceJobs



# Create Batch Request
Source: https://docs.fireworks.ai/api-reference/create-batch-request

post /{path}?endpoint_id={endpoint_id}

<CardGroup cols={1}>
  <Card title="Try notebook" icon="rocket" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/batch-api/batch_api.ipynb">
    Create a batch request for our audio transcription service
  </Card>
</CardGroup>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=FIREWORKS_API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Path Parameters

<ParamField query="path" type="string" required>
  The relative route of the target API operation (e.g. `"v1/audio/transcriptions"`, `"v1/audio/translations"`). This should correspond to a valid route supported by the backend service.
</ParamField>

### Query Parameters

<ParamField query="endpoint_id" type="string" required>
  Identifies the target backend service or model to handle the request. Currently supported:

  * `audio-prod`: [https://audio-prod.api.fireworks.ai](https://audio-prod.api.fireworks.ai)
  * `audio-turbo`: [https://audio-turbo.api.fireworks.ai](https://audio-turbo.api.fireworks.ai)
</ParamField>

### Body

Request body fields vary depending on the selected `endpoint_id` and `path`.

The request body must conform to the schema defined by the corresponding synchronous API.\
For example, transcription requests typically accept fields such as `model`, `diarize`, and `response_format`.\
Refer to the relevant synchronous API for required fields:

* [Transcribe audio](https://docs.fireworks.ai/api-reference/audio-transcriptions)
* [Translate audio](https://docs.fireworks.ai/api-reference/audio-translations)

### Response

<Tabs>
  <Tab title="json">
    <ResponseField name="status" type="string" required>
      The status of the batch request submission.\
      A value of `"submitted"` indicates the batch request was accepted and queued for processing.
    </ResponseField>

    <ResponseField name="batch_id" type="string" required>
      A unique identifier assigned to the batch job.
      This ID can be used to check job status or retrieve results later.
    </ResponseField>

    <ResponseField name="account_id" type="string" required>
      The unique identifier of the account associated with the batch job.
    </ResponseField>

    <ResponseField name="endpoint_id" type="string" required>
      The backend service selected to process the request.\
      This typically matches the `endpoint_id` used during submission.
    </ResponseField>

    <ResponseField name="message" type="string" optional>
      A human-readable message describing the result of the submission.\
      Typically `"Request submitted successfully"` if accepted.
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
  ```curl curl theme={null}

  # Download audio file
  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request
  curl -X POST "https://audio-batch.api.fireworks.ai/v1/audio/transcriptions?endpoint_id=audio-prod" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
  ```

  ```python python theme={null}
  !pip install requests

  import os
  import requests

  # input API key and download audio
  api_key = "<FIREWORKS_API_KEY>"
  audio = requests.get("https://tinyurl.com/4cb74vas").content

  # Prepare request data
  url = "https://audio-batch.api.fireworks.ai/v1/audio/transcriptions?endpoint_id=audio-prod"
  headers = {"Authorization": api_key}
  payload = {
      "model": "whisper-v3",
      "response_format": "json"
  }
  files = {"file": ("audio.flac", audio, "audio/flac")}

  # Send request
  response = requests.post(url, headers=headers, data=payload, files=files)
  print(response.text)
  ```
</RequestExample>

To check the status of your batch request, use the [Check Batch Status](https://docs.fireworks.ai/api-reference/get-batch-status) endpoint with the returned `batch_id`.


# Create Dataset
Source: https://docs.fireworks.ai/api-reference/create-dataset

post /v1/accounts/{account_id}/datasets



# Load LoRA
Source: https://docs.fireworks.ai/api-reference/create-deployed-model

post /v1/accounts/{account_id}/deployedModels



# Create Deployment
Source: https://docs.fireworks.ai/api-reference/create-deployment

post /v1/accounts/{account_id}/deployments



# null
Source: https://docs.fireworks.ai/api-reference/create-dpo-job

post /v1/accounts/{account_id}/dpoJobs



# Create Model
Source: https://docs.fireworks.ai/api-reference/create-model

post /v1/accounts/{account_id}/models



# Create Reinforcement Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/create-reinforcement-fine-tuning-job

post /v1/accounts/{account_id}/reinforcementFineTuningJobs



# null
Source: https://docs.fireworks.ai/api-reference/create-secret

post /v1/accounts/{account_id}/secrets



# Create Supervised Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/create-supervised-fine-tuning-job

post /v1/accounts/{account_id}/supervisedFineTuningJobs



# Create User
Source: https://docs.fireworks.ai/api-reference/create-user

post /v1/accounts/{account_id}/users



# Create embeddings
Source: https://docs.fireworks.ai/api-reference/creates-an-embedding-vector-representing-the-input-text

post /embeddings



# Delete API Key
Source: https://docs.fireworks.ai/api-reference/delete-api-key

post /v1/accounts/{account_id}/users/{user_id}/apiKeys:delete



# Delete Batch Inference Job
Source: https://docs.fireworks.ai/api-reference/delete-batch-inference-job

delete /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}



# Delete Dataset
Source: https://docs.fireworks.ai/api-reference/delete-dataset

delete /v1/accounts/{account_id}/datasets/{dataset_id}



# Unload LoRA
Source: https://docs.fireworks.ai/api-reference/delete-deployed-model

delete /v1/accounts/{account_id}/deployedModels/{deployed_model_id}



# Delete Deployment
Source: https://docs.fireworks.ai/api-reference/delete-deployment

delete /v1/accounts/{account_id}/deployments/{deployment_id}



# null
Source: https://docs.fireworks.ai/api-reference/delete-dpo-job

delete /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}



# Delete Model
Source: https://docs.fireworks.ai/api-reference/delete-model

delete /v1/accounts/{account_id}/models/{model_id}



# Delete Reinforcement Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/delete-reinforcement-fine-tuning-job

delete /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}



# Delete Response
Source: https://docs.fireworks.ai/api-reference/delete-response

delete /v1/responses/{response_id}
Deletes a model response by its ID. Once deleted, the response data will be gone immediately and permanently.

The response cannot be recovered and any conversations that reference this response ID will no longer be able to access it.



# null
Source: https://docs.fireworks.ai/api-reference/delete-secret

delete /v1/accounts/{account_id}/secrets/{secret_id}



# Delete Supervised Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/delete-supervised-fine-tuning-job

delete /v1/accounts/{account_id}/supervisedFineTuningJobs/{supervised_fine_tuning_job_id}



# Generate an image with FLUX.1 [schnell] FP8
Source: https://docs.fireworks.ai/api-reference/generate-a-new-image-from-a-text-prompt

POST https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image

[FLUX.1
\[schnell\]](https://huggingface.co/fireworks-ai/FLUX.1-schnell-fp8-flumina) is a
12 billion parameter rectified flow transformer capable of generating images
from text descriptions. The FP8 version uses reduced precision numerics for 2x
faster inference.

See our
[Playground](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-1-schnell-fp8)
to quickly try it out in your browser.

## Headers

<ParamField header="Accept" type="string" initialValue="image/png" placeholder="image/png">
  Specifies which format to return the response in. With `image/png` and
  `image/jpeg`, the server will populate the response body with a binary image
  of the specified format.
</ParamField>

<ParamField header="Content-Type" type="string" initialValue="application/json" placeholder="application/json">
  The media type of the request body.
</ParamField>

<ParamField header="Authorization" type="string">
  The Bearer with Fireworks API Key.
</ParamField>

## Request Body

<ParamField body="prompt" type="string" required initialValue="A photo of a cat" placeholder="A photo of a cat">
  Prompt to use for the image generation process.
</ParamField>

<ParamField body="aspect_ratio" type="string" optional initialValue="16:9" placeholder="16:9">
  Aspect ratio of the generated image.

  **Options:** `1:1`, `21:9`, `16:9`, `3:2`, `5:4`, `4:5`, `2:3`, `9:16`, `9:21`, `4:3`, `3:4`
</ParamField>

<ParamField body="guidance_scale" type="float" optional initialValue="3.5" placeholder="3.5">
  Classifier-free guidance scale for the image diffusion process. Default value is 3.5.
</ParamField>

<ParamField body="num_inference_steps" type="integer" optional initialValue="4" placeholder="4">
  Number of denoising steps for the image generation process. Default value is 4.
</ParamField>

<ParamField body="seed" type="integer" optional initialValue="0" placeholder="0">
  Random seed to use for the image generation process. If 0, we will use a totally random seed.
</ParamField>

<RequestExample>
  ```python Python theme={null}
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image"
  headers = {
      "Content-Type": "application/json",
      "Accept": "image/jpeg",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      "prompt": "A beautiful sunset over the ocean"
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
      with open("a.jpg", "wb") as f:
          f.write(response.content)
      print("Image saved as a.jpg")
  else:
      print("Error:", response.status_code, response.text)

  ```

  ```typescript TypeScript theme={null}
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "image/jpeg",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          prompt: "A beautiful sunset over the ocean"
        }),
      });

      // To process the response and get the image:
      const buffer = await response.arrayBuffer();

      fs.writeFile('a.jpg', Buffer.from(buffer), () => console.log('Finished downloading!'));
  })().catch(console.error);
  ```

  ```shell curl theme={null}
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image \
  -H 'Content-Type: application/json' \
  -H 'Accept: image/jpeg' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    "prompt": "A beautiful sunset over the ocean"
  }' -o a.jpg
  ```
</RequestExample>

<ResponseExample>
  ```json Accept: application/json theme={null}
  {
    "id": "1234567890",
    "base64": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."],
    "finishReason": "SUCCESS",
    "seed": 1234567890
  }
  ```

  ```txt Accept: image/jpeg theme={null}
  /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k=
  ```

  ```txt Accept: image/png theme={null}
  iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==
  ```
</ResponseExample>

## Response

<Tabs>
  <Tab title="application/json">
    <ResponseField name="id" type="string" required>
      The unique identifier for the image generation request.
    </ResponseField>

    <ResponseField name="base64" type="string" required>
      Includes a base64-encoded string containing an image in PNG format.
      To retrieve the image, base64-decode the string into binary data,
      then load that binary data as a PNG file.
    </ResponseField>

    <ResponseField name="finishReason" type="string" required>
      Can be `SUCCESS` or `CONTENT_FILTERED`.

      Specifies the outcome of the image generation process. It could be
      `SUCCESS` indicating that the image was successfully generated, or
      `CONTENT_FILTERED` if the image was filtered due to the safety\_check=true
      parameter being set.
    </ResponseField>

    <ResponseField name="seed" type="integer" required>
      The seed used for the image generation process.
    </ResponseField>
  </Tab>

  <Tab title="image/jpeg">
    When the Accept type is `image/jpeg`, the response body will contain a binary image. Additionally, the response will include headers such as:

    **Content-Length:** Represents the length of the binary image content.

    **Seed:** The random seed used to generate the image.

    **Finish-Reason:** Indicates the outcome of the image generation, such as `CONTENT_FILTERED` or `SUCCESS`.
  </Tab>

  <Tab title="image/png">
    When the Accept type is `image/png`, the response body will contain a binary image. Additionally, the response will include headers such as:

    **Content-Length:** Represents the length of the binary image content.

    **Seed:** The random seed used to generate the image.

    **Finish-Reason:** Indicates the outcome of the image generation, such as `CONTENT_FILTERED` or `SUCCESS`.
  </Tab>
</Tabs>


# Generate or edit an image with FLUX.1 Kontext
Source: https://docs.fireworks.ai/api-reference/generate-or-edit-image-using-flux-kontext

POST https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}

💡 Note that this API is async and will return the **request\_id** instead of the image. Call the [get\_result](/api-reference/get-generated-image-from-flux-kontex) API to obtain the generated image.

<Tabs>
  <Tab title="FLUX.1 Kontext Pro">
    FLUX Kontext Pro is a specialized model for generating contextually-aware images from text descriptions. Designed for professional use cases requiring high-quality, consistent image generation.

    Use our [Playground](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-kontext-pro) to quickly try it out in your browser.
  </Tab>

  <Tab title="FLUX.1 Kontext Max">
    FLUX Kontext Max is the most advanced model in the Kontext series, offering maximum quality and context understanding. Ideal for enterprise applications requiring the highest level of image generation performance.

    Use our [Playground](https://app.fireworks.ai/playground?model=accounts/fireworks/models/flux-kontext-max) to quickly try it out in your browser.
  </Tab>
</Tabs>

## Path

<ParamField path="model" type="string" required initialValue="flux-kontext-pro" placeholder="flux-kontext-pro">
  The model to use for image generation. Use **flux-kontext-pro** or  **flux-kontext-max** as the model name in the API.
</ParamField>

## Headers

<ParamField header="Content-Type" type="string" initialValue="application/json" placeholder="application/json">
  The media type of the request body.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key.
</ParamField>

## Request Body

<ParamField body="prompt" type="string" required initialValue="A photo of a cat" placeholder="A photo of a cat">
  Prompt to use for the image generation process.
</ParamField>

<ParamField body="input_image" type="string | null" optional>
  Base64 encoded image or URL to use with Kontext.
</ParamField>

<ParamField body="seed" type="integer | null" optional initialValue="42" placeholder="42">
  Optional seed for reproducibility.
</ParamField>

<ParamField body="aspect_ratio" type="string | null" optional>
  Aspect ratio of the image between 21:9 and 9:21.
</ParamField>

<ParamField body="output_format" type="string" optional initialValue="png" placeholder="png">
  Output format for the generated image. Can be 'jpeg' or 'png'.

  **Options:** `jpeg`, `png`
</ParamField>

<ParamField body="webhook_url" type="string | null" optional>
  URL to receive webhook notifications.

  **Length:** 1-2083 characters
</ParamField>

<ParamField body="webhook_secret" type="string | null" optional>
  Optional secret for webhook signature verification.
</ParamField>

<ParamField body="prompt_upsampling" type="boolean" optional initialValue="false" placeholder="false">
  Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation.
</ParamField>

<ParamField body="safety_tolerance" type="integer" optional initialValue="2" placeholder="2">
  Tolerance level for input and output moderation. Between 0 and 6, 0 being most strict, 6 being least strict. Limit of 2 for Image to Image.

  **Range:** 0-6
</ParamField>

<RequestExample>
  ```python Python theme={null}
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      "prompt": "A beautiful sunset over the ocean",
      "input_image": "<string>",
      "seed": 42,
      "aspect_ratio": "<string>",
      "output_format": "jpeg",
      "webhook_url": "<string>",
      "webhook_secret": "<string>",
      "prompt_upsampling": False,
      "safety_tolerance": 2
  }

  response = requests.post(url, headers=headers, json=data)
  ```

  ```typescript TypeScript theme={null}
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          prompt: "A beautiful sunset over the ocean"
        }),
      });
  })().catch(console.error);
  ```

  ```shell curl theme={null}
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model} \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    "prompt": "A beautiful sunset over the ocean"
  }'
  ```
</RequestExample>

## Response

<Tabs>
  <Tab title="200">
    Successful Response

    <ParamField body="request_id" type="string">
      request id
    </ParamField>
  </Tab>

  <Tab title="400">
    Unsuccessful Response

    <ParamField body="error_message" type="string">
      error message
    </ParamField>
  </Tab>
</Tabs>


# Get Account
Source: https://docs.fireworks.ai/api-reference/get-account

get /v1/accounts/{account_id}



# Get Batch Inference Job
Source: https://docs.fireworks.ai/api-reference/get-batch-inference-job

get /v1/accounts/{account_id}/batchInferenceJobs/{batch_inference_job_id}



# Check Batch Status
Source: https://docs.fireworks.ai/api-reference/get-batch-status

get /v1/accounts/{account_id}/batch_job/{batch_id}

This endpoint allows you to check the current status of a previously submitted batch request, and retrieve the final result if available.

<CardGroup cols={1}>
  <Card title="Try notebook" icon="rocket" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/batch-api/batch_api.ipynb">
    Check status of your batch request
  </Card>
</CardGroup>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key. e.g. `Authorization=FIREWORKS_API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Path Parameters

<ParamField query="account_id" type="string" required>
  The identifier of your Fireworks account. Must match the account used when the batch request was submitted.
</ParamField>

<ParamField query="batch_id" type="string" required>
  The unique identifier of the batch job to check.\
  This should match the `batch_id` returned when the batch request was originally submitted.
</ParamField>

### Response

The response includes the status of the batch job and, if completed, the final result.

<Tabs>
  <Tab title="json">
    <ResponseField name="status" type="string" required>
      The status of the batch job at the time of the request.\
      Possible values include `"completed"` and `"processing"`.
    </ResponseField>

    <ResponseField name="batch_id" type="string" required>
      The unique identifier of the batch job whose status is being retrieved.\
      This ID matches the one provided in the original request.
    </ResponseField>

    <ResponseField name="message" type="string" optional>
      A human-readable message describing the current state of the batch job.\
      This field is typically `null` when the job has completed successfully.
    </ResponseField>

    <ResponseField name="content_type" type="string" optional>
      The original content type of the response body.\
      This value can be used to determine how to parse the string in the `body` field.
    </ResponseField>

    <ResponseField name="body" type="string" optional>
      The serialized result of the batch job, this field is only present when `status` is `"completed"`.\
      The format of this string depends on the `content_type` field and may vary across endpoints.\
      Clients should use `content_type` to determine how to parse or interpret the value.
    </ResponseField>
  </Tab>
</Tabs>

<RequestExample>
  ```curl curl theme={null}
  # Make request
  curl -X GET "https://audio-batch.api.fireworks.ai/v1/accounts/{account_id}/batch_job/{batch_id}" \
  -H "Authorization: <FIREWORKS_API_KEY>"
  ```

  ```python python theme={null}
  !pip install requests

  import os
  import requests

  # Input api key and path parameters
  api_key = "<FIREWORKS_API_KEY>"
  account_id = "<ACCOUNT_ID>"
  batch_id = "<BATCH_ID>"

  # Send request
  url = f"https://audio-batch.api.fireworks.ai/v1/accounts/{account_id}/batch_job/{batch_id}"
  headers = {"Authorization": api_key}

  response = requests.get(url, headers=headers)
  print(response.text)
  ```
</RequestExample>


# Get Dataset
Source: https://docs.fireworks.ai/api-reference/get-dataset

get /v1/accounts/{account_id}/datasets/{dataset_id}



# Get Dataset Upload Endpoint
Source: https://docs.fireworks.ai/api-reference/get-dataset-upload-endpoint

post /v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint



# Get LoRA
Source: https://docs.fireworks.ai/api-reference/get-deployed-model

get /v1/accounts/{account_id}/deployedModels/{deployed_model_id}



# Get Deployment
Source: https://docs.fireworks.ai/api-reference/get-deployment

get /v1/accounts/{account_id}/deployments/{deployment_id}



# null
Source: https://docs.fireworks.ai/api-reference/get-dpo-job

get /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}



# null
Source: https://docs.fireworks.ai/api-reference/get-dpo-job-metrics-file-endpoint

get /v1/accounts/{account_id}/dpoJobs/{dpo_job_id}:getMetricsFileEndpoint



# Get generated image from FLUX.1 Kontext
Source: https://docs.fireworks.ai/api-reference/get-generated-image-from-flux-kontex

GET https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result

<Tabs>
  <Tab title="FLUX.1 Kontext Pro">
    Replace **model** with **flux-kontext-pro** in the API to get the result.
  </Tab>

  <Tab title="FLUX.1 Kontext Max">
    Replace **model** with **flux-kontext-max** in the API to get the result.
  </Tab>
</Tabs>

## Path

<ParamField path="model" type="string" required initialValue="flux-kontext-pro" placeholder="flux-kontext-pro">
  The model to use for image generation. Use **flux-kontext-pro** or  **flux-kontext-max** as the model name in the API.
</ParamField>

## Headers

<ParamField header="Content-Type" type="string" initialValue="application/json" placeholder="application/json">
  The media type of the request body.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key.
</ParamField>

## Request Body

<ParamField body="id" type="string" required>
  Request id generated from create/edit image request.
</ParamField>

<RequestExample>
  ```python Python theme={null}
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      id: "request_id"
  }

  response = requests.post(url, headers=headers, json=data)

  print(response.text)
  ```

  ```typescript TypeScript theme={null}
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          id: "request_id"
        }),
      });
  })().catch(console.error);
  ```

  ```shell curl theme={null}
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}/get_result \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    id: "request_id"
  }'
  ```
</RequestExample>

## Response

<ResponseField name="id" type="string" required>
  Task id for retrieving result
</ResponseField>

<ResponseField name="status" type="enum<string>" required>
  Available options: Task not found, Pending, Request Moderated, Content Moderated, Ready, Error
</ResponseField>

<ResponseField name="result" type="any" />

<ResponseField name="progress" type="number | null" />

<ResponseField name="details" type="object | null" />


# Get Model
Source: https://docs.fireworks.ai/api-reference/get-model

get /v1/accounts/{account_id}/models/{model_id}



# Get Model Download Endpoint
Source: https://docs.fireworks.ai/api-reference/get-model-download-endpoint

get /v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint



# Get Model Upload Endpoint
Source: https://docs.fireworks.ai/api-reference/get-model-upload-endpoint

post /v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint



# Get Reinforcement Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/get-reinforcement-fine-tuning-job

get /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}



# Get Response
Source: https://docs.fireworks.ai/api-reference/get-response

get /v1/responses/{response_id}



# null
Source: https://docs.fireworks.ai/api-reference/get-secret

get /v1/accounts/{account_id}/secrets/{secret_id}



# Get Supervised Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/get-supervised-fine-tuning-job

get /v1/accounts/{account_id}/supervisedFineTuningJobs/{supervised_fine_tuning_job_id}



# Get User
Source: https://docs.fireworks.ai/api-reference/get-user

get /v1/accounts/{account_id}/users/{user_id}



# Introduction
Source: https://docs.fireworks.ai/api-reference/introduction



Fireworks AI REST API enables you to interact with various language, image and embedding models using an API Key. It also lets you automate management of models, deployments, datasets, and more.

## Authentication

All requests made to the Fireworks AI REST API must include an `Authorization` header with a valid `Bearer` token using your API key, along with the `Content-Type: application/json` header.

### Getting your API key

You can obtain an API key by:

* Using the [`firectl create api-key`](/tools-sdks/firectl/commands/create-api-key) command
* Generating one through the [Fireworks AI dashboard](https://app.fireworks.ai/settings/users/api-keys)

### Request headers

Include the following headers in your REST API requests:

```json  theme={null}
authorization: Bearer <API_KEY>
content-type: application/json
```


# List API Keys
Source: https://docs.fireworks.ai/api-reference/list-api-keys

get /v1/accounts/{account_id}/users/{user_id}/apiKeys



# List Batch Inference Jobs
Source: https://docs.fireworks.ai/api-reference/list-batch-inference-jobs

get /v1/accounts/{account_id}/batchInferenceJobs



# List Datasets
Source: https://docs.fireworks.ai/api-reference/list-datasets

get /v1/accounts/{account_id}/datasets



# List LoRAs
Source: https://docs.fireworks.ai/api-reference/list-deployed-models

get /v1/accounts/{account_id}/deployedModels



# List Deployments
Source: https://docs.fireworks.ai/api-reference/list-deployments

get /v1/accounts/{account_id}/deployments



# null
Source: https://docs.fireworks.ai/api-reference/list-dpo-jobs

get /v1/accounts/{account_id}/dpoJobs



# List Models
Source: https://docs.fireworks.ai/api-reference/list-models

get /v1/accounts/{account_id}/models



# List Reinforcement Fine-tuning Jobs
Source: https://docs.fireworks.ai/api-reference/list-reinforcement-fine-tuning-jobs

get /v1/accounts/{account_id}/reinforcementFineTuningJobs



# List Responses
Source: https://docs.fireworks.ai/api-reference/list-responses

get /v1/responses
Get a list of all responses for the authenticated account.

Args:
    limit: Maximum number of responses to return (default: 20, max: 100)
    after: Cursor for pagination - return responses after this ID
    before: Cursor for pagination - return responses before this ID



# null
Source: https://docs.fireworks.ai/api-reference/list-secrets

get /v1/accounts/{account_id}/secrets



# List Supervised Fine-tuning Jobs
Source: https://docs.fireworks.ai/api-reference/list-supervised-fine-tuning-jobs

get /v1/accounts/{account_id}/supervisedFineTuningJobs



# List Users
Source: https://docs.fireworks.ai/api-reference/list-users

get /v1/accounts/{account_id}/users



# Create Chat Completion
Source: https://docs.fireworks.ai/api-reference/post-chatcompletions

post /chat/completions
Creates a model response for the given chat conversation.



# Create Completion
Source: https://docs.fireworks.ai/api-reference/post-completions

post /completions
Creates a completion for the provided prompt and parameters.



# Create Response
Source: https://docs.fireworks.ai/api-reference/post-responses

post /v1/responses
Creates a model response, optionally interacting with custom tools via the Model Context Protocol (MCP). This endpoint supports conversational continuation and streaming.

Explore our cookbooks for detailed examples:

- [Basic MCP Usage](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb)
- [Streaming with MCP](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_with_streaming.ipynb)
- [Conversational History with `previous_response_id`](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb)
- [Basic Streaming](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb)
- [Controlling Response Storage](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb)



# Prepare Model for different precisions
Source: https://docs.fireworks.ai/api-reference/prepare-model

post /v1/accounts/{account_id}/models/{model_id}:prepare



# Rerank documents
Source: https://docs.fireworks.ai/api-reference/rerank-documents

post /rerank
Rerank documents for a query using relevance scoring



# Resume Reinforcement Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/resume-reinforcement-fine-tuning-job

post /v1/accounts/{account_id}/reinforcementFineTuningJobs/{reinforcement_fine_tuning_job_id}:resume



# Resume Supervised Fine-tuning Job
Source: https://docs.fireworks.ai/api-reference/resume-supervised-fine-tuning-job

post /v1/accounts/{account_id}/supervisedFineTuningJobs/{supervised_fine_tuning_job_id}:resume



# Undelete Deployment
Source: https://docs.fireworks.ai/api-reference/undelete-deployment

post /v1/accounts/{account_id}/deployments/{deployment_id}:undelete



# Update Dataset
Source: https://docs.fireworks.ai/api-reference/update-dataset

patch /v1/accounts/{account_id}/datasets/{dataset_id}



# Update LoRA
Source: https://docs.fireworks.ai/api-reference/update-deployed-model

patch /v1/accounts/{account_id}/deployedModels/{deployed_model_id}



# Update Deployment
Source: https://docs.fireworks.ai/api-reference/update-deployment

patch /v1/accounts/{account_id}/deployments/{deployment_id}



# Update Model
Source: https://docs.fireworks.ai/api-reference/update-model

patch /v1/accounts/{account_id}/models/{model_id}



# null
Source: https://docs.fireworks.ai/api-reference/update-secret

patch /v1/accounts/{account_id}/secrets/{secret_id}



# Update User
Source: https://docs.fireworks.ai/api-reference/update-user

patch /v1/accounts/{account_id}/users/{user_id}



# Upload Dataset Files
Source: https://docs.fireworks.ai/api-reference/upload-dataset-files

post /v1/accounts/{account_id}/datasets/{dataset_id}:upload
Provides a streamlined way to upload a dataset file in a single API request. This path can handle file sizes up to 150Mb. For larger file sizes use [Get Dataset Upload Endpoint](get-dataset-upload-endpoint).




# Validate Dataset Upload
Source: https://docs.fireworks.ai/api-reference/validate-dataset-upload

post /v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload



# Validate Model Upload
Source: https://docs.fireworks.ai/api-reference/validate-model-upload

get /v1/accounts/{account_id}/models/{model_id}:validateUpload



# Autoscaling
Source: https://docs.fireworks.ai/deployments/autoscaling

Configure how your deployment scales based on traffic

Control how your deployment scales based on traffic and load.

## Configuration options

| Flag                     | Type      | Default       | Description                                            |
| ------------------------ | --------- | ------------- | ------------------------------------------------------ |
| `--min-replica-count`    | Integer   | 0             | Minimum number of replicas. Set to 0 for scale-to-zero |
| `--max-replica-count`    | Integer   | 1             | Maximum number of replicas                             |
| `--scale-up-window`      | Duration  | 30s           | Wait time before scaling up                            |
| `--scale-down-window`    | Duration  | 10m           | Wait time before scaling down                          |
| `--scale-to-zero-window` | Duration  | 1h            | Idle time before scaling to zero (min: 5m)             |
| `--load-targets`         | Key-value | `default=0.8` | Scaling thresholds. See options below                  |

**Load target options** (use as `--load-targets <key>=<value>[,<key>=<value>...]`):

* `default=<Fraction>` - General load target from 0 to 1
* `tokens_generated_per_second=<Integer>` - Desired tokens per second per replica
* `requests_per_second=<Number>` - Desired requests per second per replica
* `concurrent_requests=<Number>` - Desired concurrent requests per replica

When multiple targets are specified, the maximum replica count across all is used.

## Common patterns

<Tabs>
  <Tab title="Cost optimization">
    Scale to zero when idle to minimize costs:

    ```bash  theme={null}
    firectl create deployment <MODEL_NAME> \
      --min-replica-count 0 \
      --max-replica-count 3 \
      --scale-to-zero-window 1h
    ```

    Best for: Development, testing, or intermittent production workloads.
  </Tab>

  <Tab title="Performance-focused">
    Keep replicas running for instant response:

    ```bash  theme={null}
    firectl create deployment <MODEL_NAME> \
      --min-replica-count 2 \
      --max-replica-count 10 \
      --scale-up-window 15s \
      --load-targets concurrent_requests=5
    ```

    Best for: Low-latency requirements, avoiding cold starts, high-traffic applications.
  </Tab>

  <Tab title="Predictable traffic">
    Match known traffic patterns:

    ```bash  theme={null}
    firectl create deployment <MODEL_NAME> \
      --min-replica-count 3 \
      --max-replica-count 5 \
      --scale-down-window 30m \
      --load-targets tokens_generated_per_second=150
    ```

    Best for: Steady workloads where you know typical load ranges.
  </Tab>
</Tabs>

<Note>
  Cold starts take up to a few minutes when scaling from 0→1. Deployments with min replicas = 0 are auto-deleted after 7 days of no traffic. [Reserved capacity](/deployments/reservations) guarantees availability during scale-up.
</Note>


# Performance benchmarking
Source: https://docs.fireworks.ai/deployments/benchmarking

Measure and optimize your deployment's performance with load testing

Understanding your deployment's performance under various load conditions is essential for production readiness. Fireworks provides tools and best practices for benchmarking throughput, latency, and identifying bottlenecks.

## Fireworks Benchmark Tool

Use our open-source benchmarking tool to measure and optimize your deployment's performance:

**[Fireworks Benchmark Tool](https://github.com/fw-ai/benchmark)**

This tool allows you to:

* Test throughput and latency under various load conditions
* Simulate production traffic patterns
* Identify performance bottlenecks
* Compare different deployment configurations

### Installation

```bash  theme={null}
git clone https://github.com/fw-ai/benchmark.git
cd benchmark
pip install -r requirements.txt
```

### Basic usage

Run a basic benchmark test:

```bash  theme={null}
python benchmark.py \
  --model "accounts/fireworks/models/llama-v3p1-8b-instruct" \
  --deployment "your-deployment-id" \
  --num-requests 1000 \
  --concurrency 10
```

### Key metrics to monitor

When benchmarking your deployment, focus on these key metrics:

* **Throughput**: Requests per second (RPS) your deployment can handle
* **Latency**: Time to first token (TTFT) and end-to-end response time
* **Token generation rate**: Tokens per second during generation
* **Error rate**: Failed requests under load

## Custom benchmarking

You can also develop custom performance testing scripts or integrate with monitoring tools to track metrics over time. Consider:

* Using production-like request patterns and payloads
* Testing with various concurrency levels
* Monitoring resource utilization (GPU, memory, network)
* Testing autoscaling behavior under load

## Best practices

1. **Warm up your deployment**: Run a few requests before benchmarking to ensure models are loaded
2. **Test realistic scenarios**: Use request patterns and payloads similar to your production workload
3. **Gradually increase load**: Start with low concurrency and gradually increase to find your deployment's limits
4. **Monitor for errors**: Track error rates and response codes to identify issues under load
5. **Compare configurations**: Test different deployment shapes, quantization levels, and hardware to optimize cost and performance

## Next steps

<CardGroup cols={2}>
  <Card title="Autoscaling" href="/deployments/autoscaling" icon="arrows-up-down">
    Configure autoscaling to handle variable load
  </Card>

  <Card title="Client-side optimization" href="/deployments/client-side-performance-optimization" icon="bolt">
    Optimize your client code for maximum throughput
  </Card>
</CardGroup>


# Client-side performance optimization
Source: https://docs.fireworks.ai/deployments/client-side-performance-optimization

Optimize your client code for maximum performance with dedicated deployments

When using a dedicated deployment, it is important to optimize the client-side
HTTP connection pooling for maximum performance. We recommend using our [Python
SDK](/tools-sdks/python-client/sdk-introduction) as it has good defaults for
connection pooling and utilizes
[aiohttp](https://docs.aiohttp.org/en/stable/index.html) for optimal performance
with Python's `asyncio` library. It also includes retry logic for handling `429`
errors that Fireworks returns when the server is overloaded. We have run
benchmarks that demonstrate the performance benefits.

## General optimization recommendations

Based on our benchmarks, we recommend the following:

1. Use a client library optimized for high concurrency, such as
   [aiohttp](https://docs.aiohttp.org/en/stable/index.html) in Python or
   [http.Agent](https://nodejs.org/api/http.html#class-httpagent) in Node.js.
2. Keep the [`connection pool size`](https://docs.aiohttp.org/en/stable/client_advanced.html#limiting-connection-pool-size) high (1000+).
3. Increase concurrency until performance stops improving or you observe too many `429` errors.
4. Use [direct routing](/deployments/direct-routing) to avoid the global API load balancer and route requests directly to your deployment.

## Code example: Optimal concurrent requests (Python)

Here's how to implement optimal concurrent requests using `asyncio` and the `LLM` class:

```python main.py theme={null}
import asyncio
from fireworks import LLM

async def make_concurrent_requests(
    messages: list[str],
    max_workers: int = 1000,
    max_connections: int = 1000, # this is the default value in the SDK
):
    """Make concurrent requests with optimized connection pooling"""
    
    llm = LLM(
        model="your-model-name",
        deployment_type="on-demand", 
        id="your-deployment-id",
        max_connections=max_connections
    )
    
    # Apply deployment configuration to Fireworks
    llm.apply()
    
    # Semaphore to limit concurrent requests
    semaphore = asyncio.Semaphore(max_workers)
    
    async def single_request(message: str):
        """Make a single request with semaphore control"""
        async with semaphore:
            response = await llm.chat.completions.acreate(
                messages=[{"role": "user", "content": message}],
                max_tokens=100
            )
            return response.choices[0].message.content
    
    # Create all request tasks
    tasks = [
        single_request(message) 
        for message in messages
    ]
    
    # Execute all requests concurrently
    results = await asyncio.gather(*tasks)
    return results

# Usage example
async def main():
    messages = ["Hello!"] * 1000  # 1000 requests
    
    results = await make_concurrent_requests(
        messages=messages,
    )
    
    print(f"Completed {len(results)} requests")

if __name__ == "__main__":
    asyncio.run(main())
```

This implementation:

* Uses `asyncio.Semaphore` to control concurrency to avoid overwhelming the server
* Allows configuration of the maximum number of concurrent connections to the Fireworks API


# Direct routing
Source: https://docs.fireworks.ai/deployments/direct-routing

Direct routing enables enterprise users reduce latency to their deployments.

## Internet direct routing

Internet direct routing bypasses our global API load balancer and directly routes your request to the machines where
your deployment is running. This can save several tens or even hundreds of milliseconds of time-to-first-token (TTFT)
latency.

To create a deployment using Internet direct routing:

<Note>
  When creating a deployment with direct routing, the `--region` parameter is required to specify the deployment region.
</Note>

```bash  theme={null}
$ firectl create deployment accounts/fireworks/models/llama-v3p1-8b-instruct \
    --direct-route-type INTERNET \
    --direct-route-api-keys <API_KEYS> \
    --region <REGION>

Name: accounts/my-account/deployments/abcd1234
...
Direct Route Handle: my-account-abcd1234.us-arizona-1.direct.fireworks.ai
Region: US_ARIZONA_1
```

If you have multiple API keys, use repeated fields, such as:
`--direct-route-api-keys=<API_KEY_1> --direct-route-api-keys=<API_KEY_2>`. These keys can
be any alpha-numeric string and are a distinct concept from the API keys provisioned via the Fireworks console. A key
provisioned in the console but not specified the list here will not be allowed when querying the model via direct
routing.

Take note of the `Direct Route Handle` to get the inference endpoint. This is what you will use access the deployment
instead of the global `https://api.fireworks.ai/inference/` endpoint. For example:

```bash  theme={null}
curl \
    --header 'Authorization: Bearer <FIREWORKS_API_KEY>' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "accounts/fireworks/models/llama-v3-8b-instruct",
        "prompt": "The sky is"
    }' \
    --url https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai/v1/completions
```

## Supported Regions for Direct Routing

Direct routing is currently supported in the following regions:

* `US_IOWA_1`
* `US_VIRGINIA_1`
* `US_ARIZONA_1`
* `US_ILLINOIS_1`
* `US_TEXAS_1`
* `US_ILLINOIS_2`
* `EU_FRANKFURT_1`
* `US_WASHINGTON_3`
* `US_WASHINGTON_1`
* `AP_TOKYO_1`

## Private Service Connect (PSC)

Contact your Fireworks representative to set up [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
to your deployment.

## AWS PrivateLink

Contact your Fireworks representative to set up [AWS PrivateLink](https://aws.amazon.com/privatelink/) to your
deployment.


# Exporting Metrics
Source: https://docs.fireworks.ai/deployments/exporting-metrics

Export metrics from your dedicated deployments to your observability stack

## Overview

Fireworks provides a metrics endpoint in Prometheus format, enabling integration with popular observability tools like Prometheus, OpenTelemetry (OTel) Collector, Datadog Agent, and Vector.

<Note>
  This page covers real-time performance metrics (latency, throughput, etc.) for on-demand deployments. For billing and usage data across all Fireworks services, see [Exporting Billing Metrics](/accounts/exporting-billing-metrics).
</Note>

## Setting Up Metrics Collection

### Endpoint

The metrics endpoint is as follows. This URL and authorization header can be directly used by services like Grafana Cloud to ingest Fireworks metrics.

```
https://api.fireworks.ai/v1/accounts/<account-id>/metrics
```

### Authentication

Use the Authorization header with your Fireworks API key:

```json  theme={null}
{
  "Authorization": "Bearer YOUR_API_KEY"
}
```

### Scrape Interval

We recommend using a 1-minute scrape interval as metrics are updated every 30s.

### Rate Limits

To ensure service stability and fair usage:

* Maximum of 6 requests per minute per account
* Exceeding this limit results in HTTP 429 (Too Many Requests) responses
* Use a 1-minute scrape interval to stay within limits

## Integration Options

Fireworks metrics can be integrated with various observability platforms through multiple approaches:

### OpenTelemetry Collector Integration

The Fireworks metrics endpoint can be integrated with OpenTelemetry Collector by configuring a Prometheus receiver that scrapes the endpoint. This allows Fireworks metrics to be pushed to a variety of popular exporters—see the [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/) for a full list.

### Direct Prometheus Integration

To integrate directly with Prometheus, specify the Fireworks metrics endpoint in your scrape config:

```yaml  theme={null}
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'fireworks'
    metrics_path: 'v1/accounts/<account-id>/metrics'
    authorization:
      type: "Bearer"
      credentials: "YOUR_API_KEY"
    static_configs:
      - targets: ['api.fireworks.ai']
    scheme: https
```

For more details on Prometheus configuration, refer to the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

### Supported Platforms

Fireworks metrics can be exported to various observability platforms including:

* Prometheus
* Datadog
* Grafana
* New Relic

## Available Metrics

### Common Labels

All metrics include the following common labels:

* `base_model`: The base model identifier (e.g., "accounts/fireworks/models/deepseek-v3")
* `deployment`: Full deployment path (e.g., "accounts/account-name/deployments/deployment-id")
* `deployment_account`: The account name
* `deployment_id`: The deployment identifier

### Rate Metrics (per second)

These metrics show activity rates calculated using 1-minute windows:

#### Request Rate

* `request_counter_total:sum_by_deployment`: Request rate per deployment

#### Error Rate

* `requests_error_total:sum_by_deployment`: Error rate per deployment, broken down by HTTP status code (includes additional `http_code` label)

#### Token Processing Rates

* `tokens_cached_prompt_total:sum_by_deployment`: Rate of cached prompt tokens per deployment
* `tokens_prompt_total:sum_by_deployment`: Rate of total prompt tokens processed per deployment

### Latency Histogram Metrics

These metrics provide latency distribution data with histogram buckets, calculated using 1-minute windows:

#### Generation Latency

* `latency_generation_per_token_ms_bucket:sum_by_deployment`: Per-token generation time distribution
* `latency_generation_queue_ms_bucket:sum_by_deployment`: Time spent waiting in generation queue

#### Request Latency

* `latency_overall_ms_bucket:sum_by_deployment`: End-to-end request latency distribution
* `latency_to_first_token_ms_bucket:sum_by_deployment`: Time to first token distribution

#### Prefill Latency

* `latency_prefill_ms_bucket:sum_by_deployment`: Prefill processing time distribution
* `latency_prefill_queue_ms_bucket:sum_by_deployment`: Time spent waiting in prefill queue

### Token Distribution Metrics

These histogram metrics show token count distributions per request, calculated using 1-minute windows:

* `tokens_generated_per_request_bucket:sum_by_deployment`: Distribution of generated tokens per request
* `tokens_prompt_per_request_bucket:sum_by_deployment`: Distribution of prompt tokens per request

### Resource Utilization Metrics

These gauge metrics show average resource usage:

* `generator_kv_blocks_fraction:avg_by_deployment`: Average fraction of KV cache blocks in use
* `generator_kv_slots_fraction:avg_by_deployment`: Average fraction of KV cache slots in use
* `generator_model_forward_time:avg_by_deployment`: Average time spent in model forward pass
* `requests_coordinator_concurrent_count:avg_by_deployment`: Average number of concurrent requests
* `prefiller_prompt_cache_ttl:avg_by_deployment`: Average prompt cache time-to-live


# Regions
Source: https://docs.fireworks.ai/deployments/regions

Fireworks runs a global fleet of hardware on which you can deploy your models.

## Availability

Current region availability:

| **Region**           | **Quota availability** | **Hardware availability**              |
| -------------------- | ---------------------- | -------------------------------------- |
| `US_IOWA_1`          | Available by default   | `NVIDIA_H100_80GB`                     |
| `US_TEXAS_2`         | Available by default   | `NVIDIA_H100_80GB`                     |
| `REGION_UNSPECIFIED` | Available by default   | `ANY OF THE ABOVE/BELOW`               |
| `US_ARIZONA_1`       | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_CALIFORNIA_1`    | Must be requested      | `NVIDIA_H200_141GB`                    |
| `US_GEORGIA_2`       | Must be requested      | `NVIDIA_B200_180GB`                    |
| `US_ILLINOIS_1`      | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_ILLINOIS_2`      | Must be requested      | `NVIDIA_A100_80GB`                     |
| `US_UTAH_1`          | Must be requested      | `NVIDIA_B200_180GB`                    |
| `US_VIRGINIA_1`      | Must be requested      | `NVIDIA_H100_80GB` `NVIDIA_H200_141GB` |
| `US_WASHINGTON_1`    | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_WASHINGTON_2`    | Must be requested      | `NVIDIA_H100_80GB`                     |
| `US_WASHINGTON_3`    | Must be requested      | `NVIDIA_B200_180GB`                    |
| `EU_FRANKFURT_1`     | Must be requested      | `NVIDIA_H100_80GB`                     |
| `EU_ICELAND_1`       | Must be requested      | `NVIDIA_H200_141GB`                    |
| `EU_ICELAND_2`       | Must be requested      | `NVIDIA_H200_141GB`                    |
| `AP_TOKYO_1`         | Must be requested      | `NVIDIA_H100_80GB`                     |
| `AP_TOKYO_2`         | Must be requested      | `NVIDIA_H200_141GB`                    |

<Tip>
  If you hit a quota limit when requesting a specific region, try launching the deployment without specifying a region. This taps into your global account quota, which is more flexible.
  Deployments may still be placed in `Must be requested` regions when region is not specified, but region-level quota must be enabled to explicitly specify that region when creating
  a deployment.
</Tip>

## Using a region

When creating a deployment, you can pass the `--region` flag:

```
firectl create deployment accounts/fireworks/models/llama-v3p1-8b-instruct \
    --region US_IOWA_1
```

## Changing regions

Updating a region for a deployment in-place is currently not supported. To move a deployment between regions, please
create a new deployment in the new region, then delete the old deployment.

## Quotas

Each region has it's own separate quota for each hardware type. To view your current quotas, run

```
firectl list quotas
```

If you need deployments in a non-GA region, please contact our team at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).


# Reserved capacity
Source: https://docs.fireworks.ai/deployments/reservations



Enterprise accounts can purchase reserved capacity, typically with 1 year commitments. Reserved capacity has the following advantages over ordinary [on-demand deployments](/guides/ondemand-deployments):

* Guaranteed capacity
* Higher quotas
* Lower GPU-hour prices
* Pre-GA access to newer regions
* Pre-GA access to newest hardware

## Usage and billing

Consuming a reservation is done by creating a deployment that meets the reservation parameters. For example, suppose you have a reservation for 12 H100 GPUs and create two deployments, each using 8 H100 GPUs. While both deployments are running, 12 of the H100s will count towards using your reservation, while the excess 4 H100s will be metered and billed at the on-demand rate. Follow [deploying models on-demand](/guides/ondemand-deployments) to create a deployment.

When a reservation approaches its end time, ensure that you either renew your reservation or turn down a corresponding number of deployments, otherwise you may be billed at for your usage at on-demand rates.

Reservations are invoiced separately from your on-demand usage, at a frequency determined by your reservation contract
(e.g. monthly, quarterly, or yearly).

<Note>Reserved capacity will always be billed until the reservation ends, regardless of whether the reservation is
actively used.</Note>

## Purchasing or renewing a reservation

To purchase a reservation or increase the size or duration of an existing reservation, contact your Fireworks account
manager. If you are a new, prospective customer, please reach out to our [sales team](https://fireworks.ai/company/contact-us).

## Viewing your reservations

To view your existing reservations, run:

```
firectl list reservations
```


# Speculative Decoding
Source: https://docs.fireworks.ai/deployments/speculative-decoding

Speed up generation with draft models and n-gram speculation

Speed up text generation by using a smaller "draft" model to assist the main model, or using n-gram based speculation.

<Note>
  Speculative decoding may slow down output generation if the draft model is not a good speculator, or if token count/speculation length is too high or too low. It may also reduce max throughput. Test different models and speculation lengths for your use case.
</Note>

## Configuration options

| Flag                         | Type   | Description                                                                                 |
| ---------------------------- | ------ | ------------------------------------------------------------------------------------------- |
| `--draft-model`              | string | Draft model name. Can be a Fireworks model or custom model. See recommendations below.      |
| `--draft-token-count`        | int32  | Tokens to generate per step. Required when using draft model or n-gram. Typically set to 4. |
| `--ngram-speculation-length` | int32  | Alternative to draft model: uses N-gram based speculation from previous input.              |

<Note>
  `--draft-model` and `--ngram-speculation-length` cannot be used together.
</Note>

## Recommended draft models

| Draft model                                        | Use with              |
| -------------------------------------------------- | --------------------- |
| `accounts/fireworks/models/llama-v3p2-1b-instruct` | All Llama models > 3B |
| `accounts/fireworks/models/qwen2p5-0p5b-instruct`  | All Qwen models > 3B  |

## Examples

<Tabs>
  <Tab title="Draft model">
    Use a smaller model to speed up generation:

    ```bash  theme={null}
    firectl create deployment accounts/fireworks/models/llama-v3p3-70b-instruct \
      --draft-model="accounts/fireworks/models/llama-v3p2-1b-instruct" \
      --draft-token-count=4
    ```
  </Tab>

  <Tab title="N-gram speculation">
    Use input history for speculation (no draft model needed):

    ```bash  theme={null}
    firectl create deployment accounts/fireworks/models/llama-v3p3-70b-instruct \
      --ngram-speculation-length=3 \
      --draft-token-count=4
    ```
  </Tab>
</Tabs>

<Tip>
  Fireworks also supports [Predicted Outputs](/guides/predicted-outputs) which works in addition to model-based speculative decoding.
</Tip>


# Cloud Integrations
Source: https://docs.fireworks.ai/ecosystem/integrations

Cloud Integrations

## Cloud Deployments

<CardGroup cols={2}>
  <Card title="Amazon SageMaker" icon="aws" href="/ecosystem/integrations/sagemaker">
    Deploy Fireworks models on AWS SageMaker
  </Card>

  <Card title="Amazon EKS (Kubernetes)" icon="aws" href="/ecosystem/integrations/eks-bring-your-own-cloud">
    Run Fireworks on Amazon Elastic Kubernetes Service
  </Card>

  <Card title="Amazon ECS" icon="aws" href="/ecosystem/integrations/ecs-bring-your-own-cloud">
    Deploy using Amazon Elastic Container Service
  </Card>

  <Card title="AgentCore" icon="aws" href="/ecosystem/integrations/agentcore">
    Build and deploy AI agents with AgentCore
  </Card>
</CardGroup>

## Need Help?

For assistance with cloud deployments or custom integrations, [contact our team](https://fireworks.ai/contact).


# Agent Frameworks
Source: https://docs.fireworks.ai/ecosystem/integrations/agent-frameworks

Build production-ready AI agents with Fireworks and leading open-source frameworks

Fireworks AI seamlessly integrates with the best open-source agent frameworks, enabling you to build magical, production-ready applications powered by state-of-the-art language models.

## Supported Frameworks

<CardGroup cols={2}>
  <Card title="LangChain" icon="link" href="https://docs.langchain.com/oss/python/integrations/providers/fireworks">
    Build LLM applications with powerful orchestration and tool integration
  </Card>

  <Card title="LlamaIndex" icon="link" href="https://developers.llamaindex.ai/python/examples/llm/fireworks/">
    Efficient data retrieval and document indexing for LLM-based agents
  </Card>

  <Card title="CrewAI" icon="link" href="https://docs.crewai.com/en/concepts/llms#fireworks-ai">
    Orchestrate collaborative multi-agent systems for complex tasks
  </Card>

  <Card title="PydanticAI" icon="link" href="https://ai.pydantic.dev/models/openai/#fireworks-ai">
    Type-safe AI agent development with Pydantic validation
  </Card>

  <Card title="Strands Agents" icon="link" href="https://strandsagents.com/latest/documentation/docs/community/model-providers/fireworksai/">
    Modern agent orchestration with seamless OpenAI-compatible integration
  </Card>
</CardGroup>

## Need Help?

For assistance with agent framework integrations, [contact our team](https://fireworks.ai/contact) or join our [Discord community](https://discord.gg/fireworks-ai).


# null
Source: https://docs.fireworks.ai/evaluators/api_reference/api_overview



# Reward Kit API Reference

This API reference provides detailed documentation for the key classes, functions, and data models in the Reward Kit.

## Core Components

### Classes and Decorators

* [RewardFunction Class](/evaluators/api_reference/reward_function_class): Core class for wrapping and calling reward functions
* [reward\_function Decorator](/evaluators/api_reference/reward_function_decorator): Decorator for creating deployable reward functions

### Data Models

* [Data Models](/evaluators/api_reference/data_models): Documentation for Message, EvaluateResult, MetricResult, and other data models

## Modules

### reward\_function Module

The `reward_function` module contains the core functionality for creating and using reward functions.

```python  theme={null}
from reward_kit.reward_function import RewardFunction, reward_function
```

### evaluation Module

The `evaluation` module provides the `Evaluator` class for managing evaluation configurations and functions for creating and previewing evaluations.

```python  theme={null}
from reward_kit.evaluation import Evaluator, preview_evaluation, create_evaluation
```

Key components:

* **`Evaluator` class**: Manages metric loading, sample loading, and evaluator creation on the platform.
* **`preview_evaluation`**: Previews an evaluation with sample data before deployment.
* **`create_evaluation`**: Creates and deploys an evaluator to the platform.

### config Module

The `config` module handles loading and managing configurations for the Reward Kit, typically from a `rewardkit.yaml` file.

```python  theme={null}
from reward_kit.config import load_config, get_config, RewardKitConfig
```

Key functions and classes:

* **`load_config()` / `get_config()`**: Load the global Reward Kit configuration.
* **`RewardKitConfig`**: Pydantic model for the main configuration structure.
* Other models like `GCPCloudRunConfig`, `AWSLambdaConfig`.

### models Module

The `models` module contains data models used throughout the Reward Kit.

```python  theme={null}
from reward_kit.models import EvaluateResult, MetricResult, Message
```

### rewards Module

The `rewards` module contains specialized reward functions for specific use cases.

```python  theme={null}
from reward_kit.rewards.function_calling import match_function_call
```

### server Module

The `server` module provides the `RewardServer` class and `serve` function to host reward functions as a FastAPI application.

```python  theme={null}
from reward_kit.server import RewardServer, serve
```

Key components:

* **`RewardServer` class**: A class to encapsulate a reward function and run it as a server.
* **`serve()` function**: A utility to quickly serve a given reward function.

### auth Module

The `auth` module provides utility functions to retrieve authentication credentials, primarily for Fireworks AI.

```python  theme={null}
from reward_kit.auth import get_fireworks_api_key, get_fireworks_account_id
```

Key functions:

* **`get_fireworks_api_key()`**: Retrieves the Fireworks API key.
* **`get_fireworks_account_id()`**: Retrieves the Fireworks account ID.

### gcp\_tools Module

The `gcp_tools` module offers utilities for working with Google Cloud Platform, such as building and pushing Docker images to Artifact Registry and deploying to Cloud Run.

```python  theme={null}
from reward_kit.gcp_tools import build_and_push_docker_image, deploy_to_cloud_run
```

### packaging Module

The `packaging` module assists in preparing reward functions for deployment, for example, by generating Dockerfile content.

```python  theme={null}
from reward_kit.packaging import generate_dockerfile_content
```

### platform\_api Module

The `platform_api` module provides functions for direct interaction with the Fireworks AI platform API, such as managing secrets.

```python  theme={null}
from reward_kit.platform_api import create_or_update_fireworks_secret
```

### rl\_processing Module

The `rl_processing` module contains tools for processing data for Reinforcement Learning workflows, such as the `RLDataAligner`.

```python  theme={null}
from reward_kit.rl_processing import RLDataAligner
```

### mcp Module (`reward_kit.mcp`)

This sub-package contains components related to the Model Context Protocol (MCP).

* **`reward_kit.mcp.clients`**: Provides clients for interacting with MCP-compliant servers.

### mcp\_agent Module (`reward_kit.mcp_agent`)

This sub-package provides a framework for building and running agents that interact with MCP servers. It includes orchestration logic, various backend implementations, and a collection of pre-built MCP servers for common tasks (e.g., filesystem, git).

## Command Line Interface

The Reward Kit provides a command-line interface for common operations:

```bash  theme={null}
# Show help
reward-kit --help

# Preview an evaluator
reward-kit preview --metrics-folders "metric=./path" --samples ./samples.jsonl

# Deploy an evaluator
reward-kit deploy --id my-evaluator --metrics-folders "metric=./path" --force
```

For detailed CLI documentation, see the [CLI Reference](/evaluators/cli_reference/cli_overview).

## Common Patterns

### Creating a Basic Reward Function

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult

@reward_function
def my_reward_function(messages, original_messages=None, **kwargs):
    # Your evaluation logic here
    response = messages[-1].get("content", "")
    # Assume calculate_score returns a float between 0.0 and 1.0
    # and calculate_success returns a boolean
    score = calculate_score(response)
    success = calculate_success(response) # Assume calculate_success is defined

    return EvaluateResult(
        score=score,
        reason="Overall evaluation reason for my_reward_function", # Added top-level reason
        metrics={
            "my_metric": MetricResult(
                score=score,
                success=success, # Added success field
                reason="Explanation for the metric score"
            )
        }
    )
```

### Using a Deployed Reward Function

```python  theme={null}
from reward_kit import RewardFunction

# Create a reference to a deployed reward function
reward_fn = RewardFunction(
    name="my-deployed-evaluator",
    mode="remote"
)

# Call the reward function
result = reward_fn(messages=[
    {"role": "user", "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is..."}
])

print(f"Score: {result.score}")
```

## Next Steps

* Explore the [Examples](../examples/) for practical implementations
* Follow the [Tutorials](../tutorials/) for step-by-step guidance
* Review the [Developer Guide](../developer_guide/) for conceptual understanding


# null
Source: https://docs.fireworks.ai/evaluators/api_reference/data_models



# Data Models Reference

This document describes the core data models used in the Reward Kit for representing messages, evaluation results, and metrics.

## Message Models

### Message

The `Message` class represents a single message in a conversation.

```python  theme={null}
from reward_kit import Message

message = Message(
    role="assistant",
    content="This is the response content",
    name=None,  # Optional
    tool_call_id=None,  # Optional
    tool_calls=None,  # Optional
    function_call=None  # Optional
)
```

#### Attributes

* **`role`** (`str`): The role of the message sender. Typically one of:
  * `"user"`: Message from the user
  * `"assistant"`: Message from the assistant
  * `"system"`: System message providing context/instructions

* **`content`** (`str`): The text content of the message.

* **`name`** (`Optional[str]`): Optional name of the sender (for named system messages).

* **`tool_call_id`** (`Optional[str]`): Optional ID for a tool call (used in tool calling).

* **`tool_calls`** (`Optional[List[Dict[str, Any]]]`): Optional list of tool calls in the message.

* **`function_call`** (`Optional[Dict[str, Any]]`): Optional function call information (legacy format).

#### Compatibility

The `Message` class is compatible with OpenAI's `ChatCompletionMessageParam` interface, allowing for easy integration with OpenAI-compatible APIs.

## Evaluation Models

### EvaluateResult

The `EvaluateResult` class represents the complete result of an evaluator with multiple metrics.

```python  theme={null}
from reward_kit import EvaluateResult, MetricResult

result = EvaluateResult(
    score=0.75,
    reason="Overall good response with minor issues",
    metrics={
        "clarity": MetricResult(score=0.8, reason="Clear and concise", success=True),
        "accuracy": MetricResult(score=0.7, reason="Contains a minor factual error", success=True)
    },
    error=None  # Optional error message
)
```

#### Attributes

* **`score`** (`float`): The overall evaluation score, typically between 0.0 and 1.0.

* **`reason`** (`Optional[str]`): Optional explanation for the overall score.

* **`metrics`** (`Dict[str, MetricResult]`): Dictionary of component metrics.

* **`error`** (`Optional[str]`): Optional error message if the evaluation encountered a problem.

### MetricResult

The `MetricResult` class represents a single metric in an evaluation.

```python  theme={null}
from reward_kit import MetricResult

metric = MetricResult(
    score=0.8,
    reason="The response provides a clear explanation with appropriate examples",
    success=True
)
```

#### Attributes

* **`score`** (`float`): The score for this specific metric, typically between 0.0 and 1.0.

* **`reason`** (`str`): Explanation for why this score was assigned.

* **`success`** (`bool`): Indicates whether the metric condition was met (e.g., pass/fail).

## Example Usages

### Working with Messages

```python  theme={null}
from reward_kit import Message

# Create a user message
user_message = Message(
    role="user",
    content="Can you explain how machine learning works?"
)

# Create an assistant message
assistant_message = Message(
    role="assistant",
    content="Machine learning is a method where computers learn from data without being explicitly programmed."
)

# Create a system message
system_message = Message(
    role="system",
    content="You are a helpful assistant that provides clear and accurate explanations."
)

# Create a message with tool calls
tool_call_message = Message(
    role="assistant",
    content=None,
    tool_calls=[{
        "id": "call_123",
        "type": "function",
        "function": {
            "name": "get_weather",
            "arguments": '{"location": "San Francisco", "unit": "celsius"}'
        }
    }]
)
```

### Working with EvaluateResult

```python  theme={null}
from reward_kit import EvaluateResult, MetricResult

# Create an EvaluateResult
eval_result = EvaluateResult(
    score=0.75,
    reason="Overall good response with some minor issues",
    metrics={
        "clarity": MetricResult(score=0.8, reason="Clear and concise explanation", success=True),
        "accuracy": MetricResult(score=0.7, reason="Contains one minor factual error", success=True),
        "relevance": MetricResult(score=0.75, reason="Mostly relevant to the query", success=True)
    }
)

# Access metrics
clarity_score = eval_result.metrics["clarity"].score
print(f"Clarity score: {clarity_score}")  # Clarity score: 0.8

# Check for errors
if eval_result.error:
    print(f"Evaluation error: {eval_result.error}")
else:
    print(f"Evaluation successful with score: {eval_result.score}")
```

## Type Compatibility

While the classes provide strong typing for development, the Reward Kit also accepts dictionary representations for flexibility:

```python  theme={null}
# Using dictionaries instead of Message objects
messages = [
    {"role": "user", "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is a method..."}
]

# These are automatically converted to the appropriate types internally
```

This flexibility makes it easier to integrate with different APIs and data formats.


# null
Source: https://docs.fireworks.ai/evaluators/api_reference/reward_function_class



# RewardFunction Class Reference

The `RewardFunction` class is a core component of the Reward Kit, providing a unified interface for calling reward functions locally or remotely.

## Overview

The `RewardFunction` class wraps a reward function (either a local function or a remote endpoint) and provides a consistent interface for evaluation. It supports:

* Local functions (mode="local")
* Remote endpoints (mode="remote")
* Fireworks-hosted models (mode="fireworks\_hosted")

## Import

```python  theme={null}
from reward_kit.reward_function import RewardFunction
```

## Constructor

```python  theme={null}
RewardFunction(
    func: Optional[Callable] = None,
    func_path: Optional[str] = None,
    mode: str = "local",
    endpoint: Optional[str] = None,
    name: Optional[str] = None,
    model_id: Optional[str] = None,
    **kwargs
)
```

### Parameters

* **`func`** (`Optional[Callable]`): The local function to use (for mode="local").

* **`func_path`** (`Optional[str]`): A string path to a function (e.g., "module.submodule:function\_name").

* **`mode`** (`str`): The mode of operation. Options:
  * `"local"`: Run the function locally
  * `"remote"`: Call a remote endpoint
  * `"fireworks_hosted"`: Use a Fireworks-hosted model

* **`endpoint`** (`Optional[str]`): The URL of the remote endpoint (for mode="remote").

* **`name`** (`Optional[str]`): The name of the deployed evaluator (for mode="remote").
  If provided and endpoint is not, the endpoint will be constructed from the name.

* **`model_id`** (`Optional[str]`): The ID of the Fireworks-hosted model (for mode="fireworks\_hosted").

* **`**kwargs`**: Additional keyword arguments to pass to the function when called.

### Exceptions

* **`ValueError`**: Raised if required parameters for the specified mode are missing or if an invalid mode is provided.

## Methods

### `__call__`

Call the reward function with the provided messages.

```python  theme={null}
__call__(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult
```

#### Parameters

* **`messages`** (`List[Dict[str, str]]`): List of conversation messages, each with 'role' and 'content' keys.

* **`original_messages`** (`Optional[List[Dict[str, str]]]`): Original conversation messages (for context).
  Defaults to all messages except the last one if not provided.

* **`**kwargs`**: Additional keyword arguments to pass to the function.

#### Returns

* **`EvaluateResult`**: Object with score and metrics.

#### Exceptions

* **`ValueError`**: Raised if no function or endpoint is provided for the selected mode.
* **`TypeError`**: Raised if the function returns an invalid type.
* **`requests.exceptions.RequestException`**: Raised if there is an error calling the remote endpoint.

### `get_trl_adapter`

Create an adapter function for use with the TRL (Transformer Reinforcement Learning) library.

```python  theme={null}
get_trl_adapter() -> Callable
```

#### Returns

* **`Callable`**: A function that takes batch inputs and returns a batch of reward values, compatible with TRL.

#### Adapter Behavior

The returned adapter function:

1. Handles batch inputs (list of message lists or list of strings)
2. Returns a list of reward scores (one for each input)
3. Handles exceptions gracefully, returning 0.0 for any errors

## Examples

### Local Mode

```python  theme={null}
from reward_kit import RewardFunction, EvaluateResult, MetricResult

# Define a reward function
def my_reward_fn(messages, **kwargs):
    response = messages[-1].get("content", "")
    response_len = len(response)
    score = min(response_len / 100.0, 1.0)  # Simple score based on length
    success = response_len > 10 # Example success condition: length greater than 10

    return EvaluateResult(
        score=score,
        reason=f"Evaluation based on response length ({response_len} characters).",
        metrics={"length": MetricResult(score=score, success=success, reason=f"Length: {response_len}")}
    )

# Create a reward function in local mode
reward_fn = RewardFunction(func=my_reward_fn, mode="local")

# Call the reward function
result = reward_fn(messages=[
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there! How can I help you today?"}
])

print(f"Score: {result.score}")
```

### Remote Mode

```python  theme={null}
# Create a reward function in remote mode
remote_reward = RewardFunction(
    name="my-deployed-evaluator",
    mode="remote"
)

# Call the reward function
result = remote_reward(messages=[
    {"role": "user", "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is a method of data analysis..."}
])

print(f"Score: {result.score}")
```

### Fireworks Hosted Mode

```python  theme={null}
# Create a reward function using a Fireworks-hosted model
hosted_reward = RewardFunction(
    model_id="accounts/fireworks/models/llama-v3-8b-instruct",
    mode="fireworks_hosted"
)

# Call the reward function
result = hosted_reward(messages=[
    {"role": "user", "content": "Explain quantum computing"},
    {"role": "assistant", "content": "Quantum computing uses quantum bits or qubits..."}
])

print(f"Score: {result.score}")
```

### Using with TRL

```python  theme={null}
from reward_kit import RewardFunction

# Create a reward function
reward_fn = RewardFunction(name="my-deployed-evaluator", mode="remote")

# Get a TRL-compatible adapter
trl_reward_fn = reward_fn.get_trl_adapter()

# Use in TRL (example)
batch_inputs = [
    [{"role": "user", "content": "Question 1"}, {"role": "assistant", "content": "Answer 1"}],
    [{"role": "user", "content": "Question 2"}, {"role": "assistant", "content": "Answer 2"}]
]

# Get reward scores for the batch
reward_scores = trl_reward_fn(batch_inputs)
print(reward_scores)  # [score1, score2]
```

## Implementation Details

### Mode-Specific Requirements

* **Local Mode**: Requires either `func` or `func_path`.
* **Remote Mode**: Requires either `endpoint` or `name`.
* **Fireworks Hosted Mode**: Requires `model_id`.

### Function Loading

When providing a `func_path`, the path can be specified in two formats:

* `module.path:function_name` - Module with colon separator (preferred)
* `module.path.function_name` - Module with function as last component

### Authentication

For remote and Fireworks-hosted modes, the authentication token is retrieved from the `FIREWORKS_API_KEY` environment variable.


# null
Source: https://docs.fireworks.ai/evaluators/api_reference/reward_function_decorator



# reward\_function Decorator Reference

The `@reward_function` decorator transforms a regular Python function into a reward function with standardized inputs/outputs and deployment capabilities.

## Overview

The decorator serves several key purposes:

1. Ensures consistent input and output formats
2. Adds error handling and validation
3. Provides a `.deploy()` method for deploying the function to Fireworks

## Import

```python  theme={null}
from reward_kit import reward_function
```

## Usage

```python  theme={null}
@reward_function
def my_reward_function(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    # Your evaluation logic here
    score = 0.75  # Example score
    return EvaluateResult(
        score=score,
        reason="Overall evaluation reason",
        metrics={"example_metric": MetricResult(score=score, success=True, reason="Metric reason")}
    )
```

## Parameter Requirements

Functions decorated with `@reward_function` should accept the following parameters:

* **`messages`** (`List[Dict[str, str]]`): Required. List of conversation messages, with the last message typically being the one evaluated.

* **`original_messages`** (`Optional[List[Dict[str, str]]]`): Optional. The conversation context, without the message being evaluated.

* **`**kwargs`**: Optional. Additional parameters (like metadata) that can be passed to the function.

## Return Value Requirements

Functions must return an `EvaluateResult` object or a compatible tuple format:

```python  theme={null}
# Preferred return format
return EvaluateResult(
    score=0.75,  # Overall score
    reason="Overall evaluation reason",
    metrics={
        "clarity": MetricResult(score=0.8, success=True, reason="Good clarity"),
        "accuracy": MetricResult(score=0.7, success=False, reason="Minor errors")
    }
)

# Legacy tuple format (also supported)
return 0.75, {"clarity": 0.8, "accuracy": 0.7}
```

## Added Methods

### `.deploy()`

The decorator adds a `.deploy()` method to the function, allowing it to be deployed to Fireworks.

```python  theme={null}
evaluation_id = my_reward_function.deploy(
    name="my-evaluator",
    description="Evaluates responses based on clarity and accuracy",
    account_id=None,  # Optional, defaults to configured account
    auth_token=None,  # Optional, defaults to configured token
    force=False,  # Set to True to overwrite if it already exists
    providers=None  # Optional model providers configuration
)
```

#### Parameters

* **`name`** (`str`): Required. ID for the deployed evaluator.

* **`description`** (`str`): Optional. Human-readable description of the evaluator.

* **`account_id`** (`Optional[str]`): Optional. Fireworks account ID. If not provided, will be read from config or environment.

* **`auth_token`** (`Optional[str]`): Optional. Authentication token. If not provided, will be read from config or environment.

* **`force`** (`bool`): Optional. Whether to overwrite an existing evaluator with the same name. Default is False.

* **`providers`** (`Optional[List[Dict[str, str]]]`): Optional. List of provider configurations. If not provided, uses a default provider.

#### Returns

* **`str`**: The evaluation ID that can be used in RL training.

#### Exceptions

* **`ValueError`**: Raised if authentication fails or required parameters are missing.
* **`requests.exceptions.HTTPError`**: Raised if the API request fails.

## Implementation Details

### Validation Logic

The decorator performs the following validations:

1. Ensures the decorated function has the expected parameters
2. Validates that the return value is an `EvaluateResult` or a compatible tuple
3. Handles exceptions that occur during function execution

### Backward Compatibility

For backward compatibility, the decorator supports the legacy tuple return format:

```python  theme={null}
return score, component_scores_dict
```

This gets automatically converted to an `EvaluateResult` object.

### Deployment Process

When `.deploy()` is called, the decorator:

1. Extracts the function's source code
2. Creates a wrapper that handles the Fireworks evaluation format
3. Creates a temporary directory with the wrapped function
4. Uploads and registers the function with the Fireworks API

## Examples

### Basic Usage

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def word_count_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    """Evaluate response based on word count."""
    response = messages[-1].get("content", "")
    word_count = len(response.split())
    score = min(word_count / 100.0, 1.0)
    success = word_count > 10 # Example: success if more than 10 words

    return EvaluateResult(
        score=score,
        reason=f"Overall word count evaluation: {word_count} words.",
        metrics={
            "word_count": MetricResult(
                score=score,
                success=success,
                reason=f"Word count: {word_count}"
            )
        }
    )
```

### Using Metadata

```python  theme={null}
@reward_function
def configurable_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    metadata: Optional[Dict[str, any]] = None,
    **kwargs
) -> EvaluateResult:
    """Reward function that accepts configuration via metadata."""
    metadata = metadata or {}

    # Get threshold from metadata or use default
    threshold = metadata.get("threshold", 50)

    response = messages[-1].get("content", "")
    word_count = len(response.split())
    score = min(word_count / float(threshold), 1.0)
    success = word_count >= threshold # Example: success if count meets or exceeds threshold

    return EvaluateResult(
        score=score,
        reason=f"Configurable word count. Threshold: {threshold}, Count: {word_count}.",
        metrics={
            "configured_word_count": MetricResult(
                score=score,
                success=success,
                reason=f"Word count: {word_count}, threshold: {threshold}"
            )
        }
    )
```

### Deploying a Reward Function

```python  theme={null}
# Define and decorate the reward function
@reward_function
def clarity_reward(messages, original_messages=None, **kwargs) -> EvaluateResult:
    # ... evaluation logic ...
    # Assume score and metric_details are calculated
    score = 0.8
    metric_details = {"clarity_metric": MetricResult(score=0.8, success=True, reason="Very clear")}
    return EvaluateResult(score=score, reason="Clarity evaluation complete.", metrics=metric_details)

# Deploy the function to Fireworks
evaluation_id = clarity_reward.deploy(
    name="clarity-evaluator",
    description="Evaluates the clarity of responses",
    force=True  # Overwrite if it already exists
)

print(f"Deployed evaluator with ID: {evaluation_id}")
```

### Using with Custom Providers

```python  theme={null}
# Deploy with a specific model provider
evaluation_id = my_reward_function.deploy(
    name="my-evaluator-anthropic",
    description="My evaluator using Claude model",
    force=True,
    providers=[
        {
            "providerType": "anthropic",
            "modelId": "claude-3-sonnet-20240229"
        }
    ]
)
```


# null
Source: https://docs.fireworks.ai/evaluators/cli_reference/cli_overview



# Command Line Interface Reference

The Reward Kit provides a command-line interface (CLI) for common operations like previewing evaluations, deploying reward functions, and running agent evaluations.

## Installation

When you install the Reward Kit, the CLI is automatically installed:

```bash  theme={null}
pip install reward-kit
```

You can verify the installation by running:

```bash  theme={null}
reward-kit --help
```

## Authentication Setup

Before using the CLI, set up your authentication credentials:

```bash  theme={null}
# Set your API key
export FIREWORKS_API_KEY=your_api_key

# Optional: Set the API base URL (for development environments)
export FIREWORKS_API_BASE=https://api.fireworks.ai
```

## Command Overview

The Reward Kit CLI supports the following main commands:

* `run`: Run a local evaluation pipeline using a Hydra configuration.
* `preview`: Preview evaluation results or re-evaluate generated outputs.
* `deploy`: Deploy a reward function as an evaluator.
* `agent-eval`: Run agent evaluations on task bundles.
* `list`: List existing evaluators (coming soon).
* `delete`: Delete an evaluator (coming soon).

## Run Command (`reward-kit run`)

The `run` command is the primary way to execute local evaluation pipelines. It leverages Hydra for configuration, allowing you to define complex evaluation setups (including dataset loading, model generation, and reward application) in YAML files and easily override parameters from the command line.

### Syntax

```bash  theme={null}
python -m reward_kit.cli run [options] [HYDRA_OVERRIDES...]
```

or

```bash  theme={null}
reward-kit run [options] [HYDRA_OVERRIDES...]
```

### Key Options

* `--config-path TEXT`: Path to the directory containing your Hydra configuration files. (Required)
* `--config-name TEXT`: Name of the main Hydra configuration file (e.g., `run_my_eval.yaml`). (Required)
* `--multirun` or `-m`: Run multiple jobs (e.g., for sweeping over parameters). Refer to Hydra documentation for multi-run usage.
* `--help`: Show help message for the `run` command.

### Hydra Overrides

You can override any parameter defined in your Hydra configuration YAML files directly on the command line. For detailed information on how Hydra is used, refer to the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration).

### Examples

```bash  theme={null}
# Basic usage, running an evaluation defined in examples/math_example/conf/run_math_eval.yaml
python -m reward_kit.cli run \
  --config-path examples/math_example/conf \
  --config-name run_math_eval.yaml

# Override the number of samples to process and the model name
python -m reward_kit.cli run \
  --config-path examples/math_example/conf \
  --config-name run_math_eval.yaml \
  evaluation_params.limit_samples=10 \
  generation.model_name="accounts/fireworks/models/mixtral-8x7b-instruct"
```

### Output

The `run` command typically generates:

* A timestamped output directory (e.g., `outputs/YYYY-MM-DD/HH-MM-SS/`).
* Inside this directory:
  * `.hydra/`: Contains the full Hydra configuration for the run (for reproducibility).
  * Log files.
  * Result files, often including:
    * `<config_output_name>_results.jsonl` (e.g., `math_example_results.jsonl`): Detailed evaluation results for each sample.
    * `preview_input_output_pairs.jsonl`: Generated prompts and responses, suitable for use with `reward-kit preview`.
  * Console Output:
    * A summary report is logged to the console, including:
      * Total samples processed.
      * Number of successful evaluations.
      * Number of evaluation errors.
      * Average, min, and max scores (if applicable).
      * Score distribution.
      * Details of the first few errors encountered.

## Preview Command (`reward-kit preview`)

The `preview` command allows you to test reward functions with sample data. A primary use case is to inspect or re-evaluate the `preview_input_output_pairs.jsonl` file generated by the `reward-kit run` command. This allows you to iterate on reward logic using a fixed set of model generations or to apply different metrics to the same outputs.

You can also use it with manually created sample files.

### Syntax

```bash  theme={null}
reward-kit preview [options]
```

### Options

* `--metrics-folders`: Specify local metric scripts to apply, in the format "name=path/to/metric\_script\_dir". The directory should contain a `main.py` with a `@reward_function`.
* `--samples`: Path to a JSONL file containing sample conversations or prompt/response pairs. This is typically the `preview_input_output_pairs.jsonl` file from a `reward-kit run` output directory.
* `--remote-url`: (Optional) URL of a deployed evaluator to use for scoring, instead of local `--metrics-folders`.
* `--max-samples`: Maximum number of samples to process (optional)
* `--output`: Path to save preview results (optional)
* `--verbose`: Enable verbose output (optional)

### Examples

```bash  theme={null}
# Previewing output from a `reward-kit run` command with a local metric
reward-kit preview \
  --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
  --metrics-folders "my_custom_metric=./path/to/my_custom_metric"

# Previewing with multiple local metrics
reward-kit preview \
  --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
  --metrics-folders "metric1=./metrics/metric1" "metric2=./metrics/metric2"

# Limit sample count
reward-kit preview --metrics-folders "clarity=./my_metrics/clarity" --samples ./samples.jsonl --max-samples 5

# Save results to file
reward-kit preview --metrics-folders "clarity=./my_metrics/clarity" --samples ./samples.jsonl --output ./results.json
```

### Sample File Format

The samples file should be a JSONL (JSON Lines) file. If it's the output from `reward-kit run` (`preview_input_output_pairs.jsonl`), each line typically contains a "messages" list (including system, user, and assistant turns) and optionally a "ground\_truth" field. If creating manually, a common format is:

```json  theme={null}
{"messages": [{"role": "user", "content": "What is machine learning?"}, {"role": "assistant", "content": "Machine learning is a method of data analysis..."}]}
```

Or, if you have ground truth for comparison:

```json  theme={null}
{"messages": [{"role": "user", "content": "Question..."}, {"role": "assistant", "content": "Model answer..."}], "ground_truth": "Reference answer..."}
```

## Deploy Command

The `deploy` command deploys a reward function as an evaluator on the Fireworks platform.

### Syntax

```bash  theme={null}
reward-kit deploy [options]
```

### Options

* `--id`: ID for the deployed evaluator (required)
* `--metrics-folders`: Specify metrics to use in the format "name=path" (required)
* `--display-name`: Human-readable name for the evaluator (optional)
* `--description`: Description of the evaluator (optional)
* `--force`: Overwrite if an evaluator with the same ID already exists (optional)
* `--providers`: List of model providers to use (optional)
* `--verbose`: Enable verbose output (optional)

### Examples

```bash  theme={null}
# Basic deployment
reward-kit deploy --id my-evaluator --metrics-folders "clarity=./my_metrics/clarity"


---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-with-display-name-and-description.md)
