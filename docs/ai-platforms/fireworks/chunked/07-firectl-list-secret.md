**Navigation:** [← Previous](./06-text-models.md) | [Index](./index.md) | Next →

---

# firectl list secret
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-secret

Lists all secrets for the signed in user.

```
firectl list secret [flags]
```

### Examples

```
firectl list secrets
```

### Flags

```
  -h, --help   help for secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list supervised-fine-tuning-jobs
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-supervised-fine-tuning-jobs

Lists all supervised fine-tuning jobs in an account.

```
firectl list supervised-fine-tuning-jobs [flags]
```

### Examples

```
firectl list supervised-fine-tuning-jobs
```

### Flags

```
  -h, --help   help for supervised-fine-tuning-jobs
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl list user
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-user

Prints all users in the account.

```
firectl list user [flags]
```

### Examples

```
firectl list users
```

### Flags

```
  -h, --help   help for user
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl load-lora
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/load-lora

Loads a LoRA model to a deployment.

### Usage

Loads a LoRA model to a deployment. If a deployment is not specified, the model will be loaded to Fireworks' serverless platform (if supported). If a deployment is specified, it will be loaded to the given dedicated deployment. If successful, a DeployedModel resource will be created.

```
firectl load-lora [flags]
```

### Examples

```
firectl load-lora my-lora  # To load it to serverless
firectl load-lora my-lora --deployment abcd1234  # To load it to a dedicated deployment
```

### Flags

```
      --deployment string       The resource ID of the deployment where the LoRA model is to be loaded.
  -h, --help                    help for load-lora
      --public                  If true, the LoRA model will be publicly available for inference.
      --replace-merged-addon    Required when loading an addon to a hot reload deployment. If there is already an existing addon, it will be replaced.
      --wait                    Wait until the model is deployed.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl prepare-model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/prepare-model

Prepare models for different precisions

```
firectl prepare-model [flags]
```

### Examples

```
firectl prepare-model my-model
firectl prepare-model accounts/my-account/models/my-model
```

### Flags

```
  -h, --help                    help for prepare-model
      --wait                    Wait until the model preparation is complete.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl resume reinforcement-fine-tuning-job
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/resume-reinforcement-fine-tuning-job

Resumes a failed reinforcement fine-tuning job.

```
firectl resume reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl resume reinforcement-fine-tuning-job my-rftj
firectl resume reinforcement-fine-tuning-job accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for reinforcement-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl scale
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/scale

Scales a deployment to a specified number of replicas.

```
firectl scale [flags]
```

### Examples

```
firectl scale my-deployment --replica-count=3
firectl scale accounts/my-account/deployments/my-deployment --replica-count=3
```

### Flags

```
  -h, --help                  help for scale
      --replica-count int32   The desired number of replicas. Must be non-negative.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl undelete deployment
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/undelete-deployment

Undeletes a deployment.

```
firectl undelete deployment [flags]
```

### Examples

```
firectl undelete deployment my-deployment
```

### Flags

```
  -h, --help                    help for deployment
      --wait                    Wait until the deployment is undeleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl unload-lora
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/unload-lora

Unloads a LoRA model from a deployment.

### Usage

Unloads a LoRA model from a deployment. If a deployment is not specified, the model will be unloaded from the Fireworks serverless platform. If a deployment is specified, it will be unloaded to the given dedicated deployment.

```
firectl unload-lora [flags]
```

### Examples

```
firectl unload-lora my-lora  # To unload it from serverless
firectl unload-lora my-lora --deployment abcd1234  # To unload it from a dedicated deployment
```

### Flags

```
      --deployment string       The resource name of the deployment where the model is to be undeployed.
  -h, --help                    help for unload-lora
      --wait                    Wait until the model is deployed.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update dataset
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-dataset

Updates a dataset.

```
firectl update dataset [flags]
```

### Examples

```
firectl update dataset my-dataset
firectl update dataset accounts/my-account/datasets/my-dataset
```

### Flags

```
      --display-name string   The display name of the dataset.
  -h, --help                  help for dataset
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update deployed-model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-deployed-model

Update a deployed model.

```
firectl update deployed-model [flags]
```

### Examples

```
firectl update deployed-model my-deployed-model
firectl update deployed-model accounts/my-account/deployed-models/my-deployed-model
```

### Flags

```
      --default #<deployment>   If true, this is the default deployment when querying this model without the #<deployment> suffix.
      --description string      Description of the deployed model. Must be fewer than 1000 characters long.
      --display-name string     Human-readable name of the deployed model. Must be fewer than 64 characters long.
  -h, --help                    help for deployed-model
      --public                  If true, the deployed model will be publicly reachable.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update deployment
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-deployment

Update a deployment.

```
firectl update deployment [flags]
```

### Examples

```
firectl update deployment my-deployment
firectl update deployment accounts/my-account/deployments/my-deployment
```

### Flags

```
      --accelerator-count int32             The number of accelerators to use per replica.
      --accelerator-type string             The type of accelerator to use. Must be one of {NVIDIA_A100_80GB, NVIDIA_H100_80GB, NVIDIA_H200_141GB, AMD_MI300X_192GB}
      --deployment-shape string             The deployment shape to use for this deployment.
      --description string                  Description of the deployment.
      --direct-route-api-keys stringArray   The API keys for the direct route. Only available to enterprise accounts.
      --direct-route-type string            If set, this deployment will expose an endpoint that bypasses our API gateway. Must be one of {INTERNET, GCP_PRIVATE_SERVICE_CONNECT, AWS_PRIVATELINK}. Only available to enterprise accounts.
      --display-name string                 Human-readable name of the deployment. Must be fewer than 64 characters long.
      --draft-model string                  The draft model to use for speculative decoding. If the model is under your account, you can specify the model ID. If the model is under another account, you can specify the full resource name (e.g. accounts/other-account/models/falcon-7b).
      --draft-token-count int32             The number of tokens to generate per step for speculative decoding.
      --enable-addons                       If true, enable addons for this deployment.
      --enable-mtp                          If true, enable multi-token prediction for this deployment.
      --enable-session-affinity             If true, does sticky routing based on the 'user' field. Only available to enterprise accounts.
      --expire-time string                  If specified, the time at which the deployment will automatically be deleted. Specified in YYYY-MM-DD[ HH:MM:SS] format.
  -h, --help                                help for deployment
      --load-targets Map                    Map of autoscaling load metric names to their target utilization factors. Only available to enterprise accounts.
      --long-prompt                         Whether this deployment is optimized for long prompts.
      --max-context-length int32            The maximum context length supported by the model (context window). If not specified, the model's default maximum context length will be used.
      --max-replica-count int32             Maximum number of replicas for the deployment. If min-replica-count > 0 defaults to 0, otherwise defaults to 1.
      --min-replica-count int32             Minimum number of replicas for the deployment. If min-replica-count < max-replica-count the deployment will automatically scale between the two replica counts based on load.
      --ngram-speculation-length int32      The length of previous input sequence to be considered for N-gram speculation.
      --precision string                    The precision with which the model is served. If specified, must be one of {FP8, FP16, FP8_MM, FP8_AR, FP8_MM_KV_ATTN, FP8_KV, FP8_MM_V2, FP8_V2, FP8_MM_KV_ATTN_V2, FP4, BF16, FP4_BLOCKSCALED_MM, FP4_MX_MOE}.
      --scale-down-window duration          The duration the autoscaler will wait before scaling down a deployment after observing decreased load. Default is 10m.
      --scale-to-zero-window duration       The duration after which there are no requests that the deployment will be scaled down to zero replicas, if min-replica-count is 0. Default 1h.
      --scale-up-window duration            The duration the autoscaler will wait before scaling up a deployment after observing increased load. Default is 30s.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-model

Updates a model.

```
firectl update model [flags]
```

### Examples

```
firectl update model my-model --display-name="New Name"
firectl update model accounts/my-account/models/my-model --display-name="New Name"
```

### Flags

```
      --default-draft-model string        The default speculative draft model to use when creating a deployment.
      --default-draft-token-count int32   The default speculative draft token count when creating a deployment.
      --description string                The description of the model.
      --display-name string               The display name of the model.
      --github-url string                 The GitHub URL of the model.
  -h, --help                              help for model
      --hugging-face-url string           The Hugging Face URL of the model.
      --public                            Whether the model is publicly accessible.
      --supports-image-input              Whether the model supports image inputs.
      --supports-tools                    Whether the model supports function calling.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update quota
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-quota

Updates a quota.

```
firectl update quota [flags]
```

### Examples

```
firectl update quota serverless-inference-rpm --value 300
```

### Flags

```
  -h, --help        help for quota
      --value int   The quota allowed to be used by this account. Must be less than max_value.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update secret
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-secret

Updates an existing secret.

```
firectl update secret [flags]
```

### Examples

```
firectl update secret --id MY_SECRET --value newvalue
```

### Flags

```
  -h, --help           help for secret
      --id string      The id of the secret to be updated
      --value string   The new value of the secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl update user
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-user

Updates a user.

```
firectl update user [flags]
```

### Examples

```
firectl update user my-user --display-name="Alice Cullen"
firectl update user accounts/my-account/users/my-user --display-name="Alice Cullen"
```

### Flags

```
      --display-name string   The display name of the user.
  -h, --help                  help for user
      --role string           The role of the user. Must be one of {user, admin}.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl upgrade
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/upgrade

Upgrades the firectl binary to the latest version.

```
firectl upgrade [flags]
```

### Examples

```
sudo firectl upgrade
```

### Flags

```
  -h, --help   help for upgrade
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl upload model
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/upload-model

Resumes or completes a model upload.

### Usage

Resumes or completes a model upload for an existing model. This command should be used when a previous upload was interrupted.

```
firectl upload model [flags]
```

### Examples

```
firectl upload model my-model /path/to/checkpoint/
```

### Flags

```
  -h, --help    help for model
      --quiet   If true, does not print the upload progress bar.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl version
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/version

Prints the version of firectl

```
firectl version [flags]
```

### Examples

```
firectl version
```

### Flags

```
  -h, --help   help for version
  -l, --long   Print build details.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# firectl whoami
Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/whoami

Shows the currently authenticated user

```
firectl whoami [flags]
```

### Examples

```
firectl whoami
```

### Flags

```
  -h, --help   help for whoami
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


# Getting started
Source: https://docs.fireworks.ai/tools-sdks/firectl/firectl

Learn to create, deploy, and manage resources using Firectl

Firectl can be installed several ways based on your choice and platform.

<CodeGroup>
  ```bash homebrew theme={null}
  brew tap fw-ai/firectl
  brew install firectl

  # If you encounter a failed SHA256 check, try first running
  brew update
  ```

  ```bash macOS (Apple Silicon) theme={null}
  curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-arm64.gz -o firectl.gz
  gzip -d firectl.gz && chmod a+x firectl
  sudo mv firectl /usr/local/bin/firectl
  sudo chown root: /usr/local/bin/firectl
  ```

  ```bash macOS (x86_64) theme={null}
  curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-amd64.gz -o firectl.gz
  gzip -d firectl.gz && chmod a+x firectl
  sudo mv firectl /usr/local/bin/firectl
  sudo chown root: /usr/local/bin/firectl
  ```

  ```bash Linux  (x86_64) theme={null}
  wget -O firectl.gz https://storage.googleapis.com/fireworks-public/firectl/stable/linux-amd64.gz
  gunzip firectl.gz
  sudo install -o root -g root -m 0755 firectl /usr/local/bin/firectl
  ```

  ```Text Windows (64 bit) theme={null}
  wget -L https://storage.googleapis.com/fireworks-public/firectl/stable/firectl.exe
  ```
</CodeGroup>

### Sign into Fireworks account

To sign into your Fireworks account:

```bash  theme={null}
firectl signin
```

If you have set up [Custom SSO](/accounts/sso) then also pass your account ID:

```bash  theme={null}
firectl signin <ACCOUNT_ID>
```

### Check you have signed in

To show which account you have signed into:

```bash  theme={null}
firectl whoami
```

### Check your installed version

```bash  theme={null}
firectl version
```

### Upgrade to the latest version

```bash  theme={null}
sudo firectl upgrade
```


# OpenAI compatibility
Source: https://docs.fireworks.ai/tools-sdks/openai-compatibility



You can use the [OpenAI Python client library](https://github.com/openai/openai-python) to interact with Fireworks. This makes migration of existing applications already using OpenAI particularly easy.

## Specify endpoint and API key

### Using the OpenAI client

You can use the OpenAI client by initializing it with your Fireworks configuration:

```python  theme={null}
from openai import OpenAI

# Initialize with Fireworks parameters
client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>",
)
```

You can also use environment variables with the client:

```python  theme={null}
import os
from openai import OpenAI

# Initialize using environment variables
client = OpenAI(
    base_url=os.environ.get("OPENAI_API_BASE", "https://api.fireworks.ai/inference/v1"),
    api_key=os.environ.get("OPENAI_API_KEY"),  # Set to your Fireworks API key
)
```

### Using environment variables

```shell  theme={null}
export OPENAI_API_BASE="https://api.fireworks.ai/inference/v1"
export OPENAI_API_KEY="<YOUR_FIREWORKS_API_KEY>"
```

### Alternative approach

```python  theme={null}
import openai

# warning: it has a process-wide effect
openai.api_base = "https://api.fireworks.ai/inference/v1"
openai.api_key = "<YOUR_FIREWORKS_API_KEY>"
```

## Usage

Use OpenAI's SDK how you'd normally would. Just ensure that the `model` parameter refers to one of [Fireworks models](https://fireworks.ai/models).

### Completion

Simple completion API that doesn't modify provided prompt in any way:

```python  theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>",
)

completion = client.completions.create(
    model="accounts/fireworks/models/llama-v3p1-8b-instruct",
    prompt="The quick brown fox",
)
print(completion.choices[0].text)
```

### Chat Completion

Works best for models fine-tuned for conversation (e.g. llama\*-chat variants):

```python  theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="<YOUR_FIREWORKS_API_KEY>",
)

chat_completion = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-8b-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(chat_completion.choices[0].message.content)
```

## API compatibility

### Differences

The following options have minor differences:

* `stop`: the returned string includes the stop word for Fireworks while it's omitted for OpenAI (it can be easily truncated on client side)
* `max_tokens`: behaves differently if the model context length is exceeded. If the length of `prompt` or `messages` plus `max_tokens` is higher than the model's context window, `max_tokens` will be adjusted lower accordingly. OpenAI returns invalid request error in this situation. This behavior can be adjusted by `context_length_exceeded_behavior` parameter.

### Token usage for streaming responses

OpenAI API returns usage stats (number of tokens in prompt and completion) for non-streaming responses but doesn't for the streaming ones (see [forum post](https://community.openai.com/t/chat-completion-stream-api-token-usage/352964)).

Fireworks.ai returns usage stats in both cases. For streaming responses, the `usage` field is returned in the very last chunk on the response (i.e. the one having `finish_reason` set). For example:

```bash cURL theme={null}
curl --request POST \           
     --url https://api.fireworks.ai/inference/v1/completions \
     --header "accept: application/json" \
     --header "authorization: Bearer $API_KEY" \
     --header "content-type: application/json" \
     --data '{"model": "accounts/fireworks/models/starcoder-16b-w8a16", "prompt": "def say_hello_world():", "max_tokens": 100, "stream": true}'
```

```
data: {..., "choices":[{"text":"\n  print('Hello,","index":0,"finish_reason":null,"logprobs":null}],"usage":null}
       
data: {..., "choices":[{"text":" World!')\n\n\n","index":0,"finish_reason":null,"logprobs":null}],"usage":null}
       
data: {..., "choices":[{"text":"say_hello_","index":0,"finish_reason":null,"logprobs":null}],"usage":null}
       
data: {..., "choices":[{"text":"world()\n","index":0,"finish_reason":"stop","logprobs":null}],"usage":{"prompt_tokens":7,"total_tokens":24,"completion_tokens":17}}

data: [DONE]
```

<Note>
  Note, that if you're using OpenAI SDK, they `usage` field won't be listed in the SDK's structure definition. But it can be accessed directly. For example:

  * In Python SDK, you can access the attribute directly, e.g. `for chunk in openai.ChatCompletion.create(...): print(chunk["usage"])`.
  * In TypeScript SDK, you need to cast away the typing, e.g. `for await (const chunk of await openai.chat.completions.create(...)) { console.log((chunk as any).usage); }`.
</Note>

### Not supported options

The following options are not yet supported:

* `presence_penalty`
* `frequency_penalty`
* `best_of`: you can use `n` instead
* `logit_bias`
* `functions`: you can use our [LangChain integration](https://python.langchain.com/docs/integrations/providers/fireworks) to achieve similar functionality client-side

Please reach out to us on [Discord](https://discord.gg/fireworks-ai) if you have a use case requiring one of these.


# Querying Dedicated Deployments
Source: https://docs.fireworks.ai/tools-sdks/python-client/querying-dedicated-deployments

Learn how to connect to and query dedicated deployments that were created outside the SDK

When you have dedicated deployments that were created via `firectl` or the Fireworks web UI, you can easily connect to them using the Build SDK to run inference. This is particularly useful when you want to leverage existing infrastructure or when deployments are managed by different teams.

## Prerequisites

Before you begin, make sure you have:

* An existing dedicated deployment running on Fireworks
* The deployment ID or name
* Your Fireworks API key configured

<Note>
  You can find your deployment ID in the [Fireworks dashboard](https://app.fireworks.ai/dashboard/deployments) under the deployments section.
</Note>

## Connecting to an existing deployment

To query an existing dedicated deployment, you simply need to create an `LLM` instance with the `deployment_type="on-demand"` and provide the deployment `id`:

```python  theme={null}
from fireworks import LLM

# Connect to your existing dedicated deployment
llm = LLM(
    model="llama-v3p2-3b-instruct",  # The model your deployment is running
    deployment_type="on-demand",
    id="my-custom-deployment",  # Your deployment ID
)

# Start using the deployment immediately - no .apply() needed
response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from my dedicated deployment!"}]
)

print(response.choices[0].message.content)
```

<Check>
  Since you're connecting to an existing deployment, you don't need to call `.apply()` - the deployment is already running and ready to serve requests.
</Check>

## Important considerations

### No resource creation

When connecting to existing deployments:

* **No new resources are created** - The SDK connects to your existing deployment
* **No `.apply()` call needed** - The deployment is already active
* **Immediate availability** - You can start making inference calls right away

### Deployment ID requirements

The `id` parameter should match exactly with your existing deployment:

* Use the deployment name/ID as shown in the Fireworks dashboard
* The ID is case-sensitive and must match exactly
* If the deployment doesn't exist, you'll receive an error when making requests

### Model specification

While you need to specify the `model` parameter, it should match the model that your deployment is actually running:

```python  theme={null}
# If your deployment is running Llama 3.2 3B Instruct
llm = LLM(
    model="llama-v3p2-3b-instruct",
    deployment_type="on-demand", 
    id="production-llama-deployment"
)

# If your deployment is running Qwen 2.5 72B Instruct
llm = LLM(
    model="qwen2p5-72b-instruct",
    deployment_type="on-demand",
    id="qwen-high-capacity-deployment"
)
```

## Complete example

Here's a complete example that demonstrates connecting to an existing deployment and using it for a conversation:

<CodeGroup>
  ```python Basic usage theme={null}
  from fireworks import LLM

  # Connect to existing deployment
  llm = LLM(
      model="llama-v3p2-3b-instruct",
      deployment_type="on-demand",
      id="my-existing-deployment",
  )

  # Use OpenAI-compatible chat completions
  response = llm.chat.completions.create(
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Explain quantum computing in simple terms."}
      ],
      max_tokens=150,
      temperature=0.7
  )

  print(response.choices[0].message.content)
  ```

  ```python Streaming responses theme={null}
  from fireworks import LLM

  llm = LLM(
      model="llama-v3p2-3b-instruct",
      deployment_type="on-demand",
      id="my-existing-deployment",
  )

  # Stream the response
  stream = llm.chat.completions.create(
      messages=[{"role": "user", "content": "Write a short poem about AI."}],
      stream=True,
      max_tokens=100
  )

  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="")
  ```
</CodeGroup>

## Troubleshooting

### Common issues and solutions

<AccordionGroup>
  <Accordion title="Deployment not found error">
    **Problem**: Getting 404 errors when trying to use the deployment.

    **Solutions**:

    * Verify the deployment ID is correct in the [Fireworks dashboard](https://app.fireworks.ai/dashboard/deployments)
    * Ensure the deployment is in "Running" status
    * Check that you're using the correct Fireworks API key
    * Confirm the deployment belongs to your account/organization
  </Accordion>

  <Accordion title="Model mismatch warnings">
    **Problem**: The model parameter doesn't match the actual deployed model.

    **Solutions**:

    * Check what model your deployment is actually running in the dashboard
    * Update the `model` parameter to match the deployed model
    * If unsure, you can often find the model information in the deployment details
  </Accordion>

  <Accordion title="Authentication errors">
    **Problem**: Getting authentication errors when connecting to the deployment.

    **Solutions**:

    * Verify your `FIREWORKS_API_KEY` environment variable is set correctly
    * Ensure your API key has access to the deployment
    * Check that the deployment belongs to your account or organization
  </Accordion>
</AccordionGroup>

## Next steps

Now that you can connect to existing deployments, you might want to:

* Learn about [fine-tuning models](/tools-sdks/python-client/sdk-basics#fine-tuning-a-model) to create custom deployments
* Explore the [complete SDK tutorial](/tools-sdks/python-client/the-tutorial) for more advanced usage
* Check out the [SDK reference documentation](/tools-sdks/python-client/sdk-reference) for all available options


# Build SDK Basics
Source: https://docs.fireworks.ai/tools-sdks/python-client/sdk-basics



## Why use the Build SDK?

The Fireworks Build SDK gives you a declarative way to work with Fireworks resources like deployments, fine-tuning jobs, and datasets. We've designed it to handle all the infrastructure complexity for you, letting you focus on building your application. Instead of using the web UI, CLI, or raw API calls, you can manage everything through simple Python code with smart, logical defaults without sacrificing control and customizability.

The principles of the SDK are the following:

* **Object-oriented:** Fireworks primitives are represented as Python objects. You can access their capabilities and properties through methods and attributes.

* **Declarative:** You can describe your desired state and the SDK will handle reconcilliation.

* **Smart defaults:** The SDK will infer the most logical defaults for you, prioritizing development speed and lowest cost. Here are some examples:
  * The SDK will automatically use a serverless deployment for models that are available serverlessly unless you specify otherwise.
  * When creating deployments, the SDK will also enable scale-to-zero with the shortest possible scale-down window.
  * If the SDK determines that a resource already exists by matching its signature (see below), it will re-use the existing resource instead of creating a new one.

* **Customizable:** Although we enable smart defaults, you still have full access to the configuration parameters for any Fireworks resource

<Note>
  The Build SDK is currently in beta and not all functionality may be supported. Please reach out to [dhuang@fireworks.ai](mailto:dhuang@fireworks.ai) to report any issues or feedback.
</Note>

## The `LLM()` class

Running a model on Fireworks is as simple as instantiating the `LLM` class and
calling a single function. Here's an example of how to instantiate the latest
[Llama 4 Maverick model](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic) using the Build SDK.

```python main.py {3} theme={null}
from fireworks import LLM

llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="serverless")

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```

You can send various parameters to the `LLM()` constructor to take full advantage of all of Fireworks' customization options.

```python main.py {2-8} theme={null}
llm = LLM(
  model="qwen2p5-72b-instruct",
  id="my-deployment-id",
  deployment_type="on-demand",
  precision="FP8",
  accelerator_type="NVIDIA_H100_80GB",
  draft_model="qwen2p5-0p5b-instruct",
  draft_token_count=4,
  min_replica_count=1,
) 

# Apply deployment configuration to Fireworks
llm.apply()

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```

## Fine-tuning a model

You can fine-tune a model by creating a `Dataset` object and then calling the `.create_supervised_fine_tuning_job()` method on the `LLM` object.

```python main.py theme={null}
from fireworks import Dataset, LLM

dataset = Dataset.from_file("my-dataset.jsonl")

base_model = LLM(model="qwen2p5-7b-instruct", id="my-base-deployment-id", deployment_type="on-demand")

job = base_model.create_supervised_fine_tuning_job(
    "my-fine-tuning-job",
    dataset,
)
job.wait_for_completion()
fine_tuned_model=job.output_llm
```

Datasets are files in JSONL format, where each line represents a complete JSON-formatted training example following the Chat Completions API format. See [fine-tuning a model](../../fine-tuning/fine-tuning-models#step-2%3A-prepare-the-dataset) for an example. Once you have training examples prepared, you can create a `Dataset` object and upload the dataset to Fireworks by using `from_file()`, `from_string()`, or `from_list()`, and pass it to the `.create_supervised_fine_tuning_job()` method on the `LLM` object as we did above.

## Debug mode

Sometimes, it can be helpful to see the log of actions that the SDK is taking behind the scenes. You can enable debug mode by setting the `FIREWORKS_SDK_DEBUG=True` environment variable.

## Key concepts

### Resource types

The SDK supports the following resource types:

* `LLM` - Represents a model running on a deployment
* `Dataset` - Represents a dataset used to create a fine-tuning job
* `SupervisedFineTuningJob` - Represents a fine-tuning job

### Deployment type selection

The SDK tries to be parsimonious with the way it deploys resources. We provide two types of deployment options on Fireworks:

* `serverless` hosting is enabled for some commonly-used state of the art models. The pricing for these models is per-token, i.e. you only pay for the tokens you use, and subject to rate limits.
* `on-demand` hosting is enabled for all other models. The pricing for these models is per GPU-second. This hosting is required for models that are not available serverlessly or workloads that exceed serverless rate limits.

For non-finetuned models, you can always specify the deployment type of `LLM()` by passing either `"serverless"` or `"on-demand"` as the `deployment_type` parameter to the constructor. If the model is not available for the deployment type you selected, the SDK will throw an error. The SDK can also decide the best deployment strategy on your behalf, just pass `deployment_type="auto"`. If the model is available serverlessly, the SDK will use serverless hosting, otherwise the SDK will create an on-demand deployment.

<Note>
  When using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`, you must call `.apply()` to apply the deployment configuration to Fireworks. This is not required for serverless deployments. When using `deployment_type="auto"`, the SDK will automatically handle deployment creation, but if it falls back to on-demand deployment, you may need to call `.apply()` explicitly. If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments).
</Note>

<Warning>
  Be careful with the `deployment_type` parameter, especially for `"auto"` and `"on-demand"` deployments. While the SDK will try to make the most cost effective choice for you and put sensible autoscaling policies in place, it is possible to unintentionally create many deployments that lead to unwanted spend, especially when working with non-serverless models.
</Warning>

<Warning>
  When using `deployment_type="on-demand"`, you must provide an `id` parameter to uniquely identify your deployment. This is required to prevent accidental creation of multiple deployments.
</Warning>

For finetuned (LoRA) models, passing `deployment_type="serverless" ` will try to deploy the finetuned model to serverless hosting, `deployment_type="on-demand"` will create an on-demand deployment of your base model and merge in your LoRA weights, `deployment_type="on-demand-lora"` will create an on-demand deployment with Multi-LoRA enabled, and `deployment_type="auto"` will try to use `serverless` if available, otherwise fall back to `on-demand-lora`.

#### Deploying Fine-tuned Models with On-Demand

When deploying a fine-tuned model using `deployment_type="on-demand"`, you need to provide:

* `model` - Your fine-tuned model ID (e.g., `"accounts/your-account/models/your-fine-tuned-model-id"`)
* `id` - A unique deployment identifier (can be any simple string like `"my-fine-tuned-deployment"`)

```python  theme={null}
# Deploy a fine-tuned model with on-demand deployment
fine_tuned_llm = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand",
    id="my-fine-tuned-deployment"  # Simple string ID
)

# Apply deployment configuration to Fireworks
fine_tuned_llm.apply()

# Track deployment in web dashboard
print(f"Track at: {fine_tuned_llm.deployment_url}")
```

<Note>
  The `id` parameter can be any simple string - it does not need to follow the format `"accounts/account_id/deployments/model_id"`.
</Note>

### Resource signatures

Each resource has a signature, which is the set of properties that are used to identify the resource. The SDK will use the signature to determine if a resource already exists and can be re-used.

| Resource                  | Signature                   |
| ------------------------- | --------------------------- |
| `LLM`                     | `id`                        |
| `Dataset`                 | `hash(data)` and `filename` |
| `SupervisedFineTuningJob` | `name` and `model`          |

For `LLM` resources, the resource signature is based on the `id` parameter. When using `deployment_type="on-demand"`, you must provide a unique `id` to identify your deployment.

For `Dataset` resources, the resource signature is derived from the `filename` of your dataset (if created via `from_file()`) and the hash of the data itself.

For `SupervisedFineTuningJob` resources, you are required to pass a `name` when creating the resource.

### Resource management

The SDK also tries to be parsimonious with the *number* of resources it creates. Before creating a resource, the SDK will first check if a resource with the same signature already exists. If so, the SDK will re-use the existing resource instead of creating a new one. This could mean updating the resource with new configuration parameters, or re-using the existing resource.

A new resource will be created in the following cases for each resource type:

| Resource                  | Created by SDK if...                                                               |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `LLM`                     | You pass a unique `id` to the constructor                                          |
| `Dataset`                 | You change the `filename` of the data or modify the data itself                    |
| `SupervisedFineTuningJob` | You pass a unique `name` when creating the fine-tuning job or use a unique `model` |


# Build SDK Introduction
Source: https://docs.fireworks.ai/tools-sdks/python-client/sdk-introduction



The [Fireworks Build SDK](https://pypi.org/project/fireworks-ai/) is a client library that allows you to interact with the Fireworks API using Python. It provides a simple and intuitive interface for working with Fireworks primitives like deployments, fine-tuning jobs, and datasets as Python objects.

<Note>
  The Build SDK is currently in beta and not all functionality may be supported. Please reach out to [dhuang@fireworks.ai](mailto:dhuang@fireworks.ai) to report any issues or feedback.
</Note>

## Installation

You can install the Fireworks Build SDK using pip:

```bash  theme={null}
pip install --upgrade fireworks-ai
```

Make sure to set the `FIREWORKS_API_KEY` environment variable to your Fireworks API key:

```bash  theme={null}
export FIREWORKS_API_KEY=<API_KEY>
```

You can create an API key in the [Fireworks AI web UI](https://app.fireworks.ai/settings/users/api-keys) or by installing the [firectl](/tools-sdks/firectl/firectl) CLI tool and running:

```bash  theme={null}
firectl signin
firectl create api-key --key-name <Your-Key-Name>
```

## Next Steps

Get started by [learning about the basics](/tools-sdks/python-client/sdk-basics) of working with the Build SDK. Or, if you'd prefer to jump straight in, we have prepared an [interactive tutorial](/tools-sdks/python-client/the-tutorial).


# Reference
Source: https://docs.fireworks.ai/tools-sdks/python-client/sdk-reference



# Resource types

The SDK currently supports four types of resources: `LLM`, `Dataset`, `SupervisedFineTuningJob`, and `BatchInferenceJob`.

## LLM

```python  theme={null}
class LLM()
```

**Properties:**

* `deployment_name` *str* - The full name of the deployment (e.g., `accounts/my-account/deployments/my-custom-deployment`)
* `deployment_display_name` *str* - The display name of the deployment, defaults to the filename where the LLM was instantiated unless otherwise specified
* `deployment_url` *str* - The URL to view the deployment in the Fireworks dashboard
* `temperature` *float* - The temperature for generation
* `model` *str* - The model associated with this LLM (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `base_deployment_name` *str* - If a LoRA addon, the deployment name of the base model deployment
* `peft_base_model` *str* - If this is a LoRA addon, the base model identifier (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `addons_enabled` *bool* - Whether LoRA addons are enabled for this LLM
* `model_id` *str* - The identifier used under the hood to query this model (e.g., `accounts/my-account/deployedModels/my-deployed-model-abcdefg`)
* `deployment_id` *str* - The deployment ID (e.g., `my-custom-deployment`)
* `base_deployment_id` *str* - The base deployment ID for LoRA addons
* `perf_metrics_in_response` *bool* - Whether performance metrics are included in responses

### Instantiation

The `LLM(*args, **kwargs)` class constructor initializes a new LLM instance.

```python  theme={null}
from fireworks import LLM
from datetime import timedelta

# Basic usage with required parameters
llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

# Advanced usage with optional parameters
llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="on-demand",
    id="my-custom-deployment",
    accelerator_type="NVIDIA_H100_80GB",
    min_replica_count=1,
    max_replica_count=3,
    scale_up_window=timedelta(seconds=30),
    scale_down_window=timedelta(minutes=10),
    enable_metrics=True
)

# Apply deployment configuration to Fireworks
llm.apply()

# Deploy a fine-tuned model with on-demand deployment
fine_tuned_llm = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand",
    id="my-fine-tuned-deployment"  # Simple string identifier
)

# Apply deployment configuration to Fireworks
fine_tuned_llm.apply()

# Deploy fine-tuned model using multi-LoRA (sharing base deployment)
base_model = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="on-demand",
    id="shared-base-deployment",
    enable_addons=True
)

# Apply base deployment configuration to Fireworks
base_model.apply()

fine_tuned_with_lora = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

# Apply LoRA deployment configuration to Fireworks
fine_tuned_with_lora.apply()
```

#### Required Arguments

* `model` *str* - The model identifier to use (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `deployment_type` *str* - The type of deployment to use. Must be one of:
  * `"serverless"`: Uses Fireworks' shared serverless infrastructure
  * `"on-demand"`: Uses dedicated resources for your deployment
  * `"auto"`: Automatically selects the most cost-effective option (recommended for experimentation)
  * `"on-demand-lora"`: For LoRA addons that require dedicated resources

#### Optional Arguments

**Deployment Configuration**

* `id` *str, optional* - Deployment ID to identify the deployment. Required when deployment\_type is "on-demand". Can be any simple string (e.g., `"my-deployment"`) - does not need to follow the format `"accounts/account_id/deployments/model_id"`.
* `deployment_display_name` *str, optional* - Display name for the deployment. Defaults to the filename where the LLM was instantiated. If a deployment with the same display name and model already exists, the SDK will try and re-use it.
* `base_id` *str, optional* - Base deployment ID for LoRA addons. Required when deployment\_type is "on-demand-lora".

**Authentication & API**

* `api_key` *str, optional* - Your Fireworks API key
* `base_url` *str, optional* - Base URL for API calls. Defaults to "[https://api.fireworks.ai/inference/v1](https://api.fireworks.ai/inference/v1)"
* `max_retries` *int, optional* - Maximum number of retry attempts. Defaults to 10

**Scaling Configuration**

* `scale_up_window` *timedelta, optional* - Time to wait before scaling up after increased load. Defaults to 1 second
* `scale_down_window` *timedelta, optional* - Time to wait before scaling down after decreased load. Defaults to 1 minute
* `scale_to_zero_window` *timedelta, optional* - Time of inactivity before scaling to zero. Defaults to 5 minutes

**Hardware & Performance**

* `accelerator_type` *str, optional* - Type of GPU accelerator to use
* `region` *str, optional* - Region for deployment
* `multi_region` *str, optional* - Multi-region configuration
* `min_replica_count` *int, optional* - Minimum number of replicas
* `max_replica_count` *int, optional* - Maximum number of replicas
* `replica_count` *int, optional* - Fixed number of replicas
* `accelerator_count` *int, optional* - Number of accelerators per replica
* `precision` *str, optional* - Model precision (e.g., "FP16", "FP8")
* `world_size` *int, optional* - World size for distributed training
* `generator_count` *int, optional* - Number of generators
* `disaggregated_prefill_count` *int, optional* - Number of disaggregated prefill instances
* `disaggregated_prefill_world_size` *int, optional* - World size for disaggregated prefill
* `max_batch_size` *int, optional* - Maximum batch size for inference
* `max_peft_batch_size` *int, optional* - Maximum batch size for PEFT operations
* `kv_cache_memory_pct` *int, optional* - Percentage of memory for KV cache

**Advanced Features**

* `enable_addons` *bool, optional* - Enable LoRA addons support
* `live_merge` *bool, optional* - Enable live merging
* `draft_token_count` *int, optional* - Number of tokens to generate per step for speculative decoding
* `draft_model` *str, optional* - Model to use for speculative decoding
* `ngram_speculation_length` *int, optional* - Length of previous input sequence for N-gram speculation
* `long_prompt_optimized` *bool, optional* - Optimize for long prompts
* `temperature` *float, optional* - Sampling temperature for generation
* `num_peft_device_cached` *int, optional* - Number of PEFT devices to cache

**Monitoring & Metrics**

* `enable_metrics` *bool, optional* - Enable metrics collection. Currently supports time to last token for non-streaming requests.
* `perf_metrics_in_response` *bool, optional* - Include performance metrics in API responses

**Additional Configuration**

* `description` *str, optional* - Description of the deployment
* `annotations` *dict\[str, str], optional* - Annotations for the deployment
* `cluster` *str, optional* - Cluster identifier
* `enable_session_affinity` *bool, optional* - Enable session affinity
* `direct_route_api_keys` *list\[str], optional* - List of API keys for direct routing
* `direct_route_type` *str, optional* - Type of direct routing
* `direct_route_handle` *str, optional* - Direct route handle

### `apply(wait: bool = True)`

Ensures the deployment is ready and returns the deployment. Like Terraform apply, this will ensure the deployment is ready.

```python  theme={null}
llm.apply(wait=True)
```

### `create_supervised_fine_tuning_job()`

Creates a new supervised fine-tuning job and blocks until it is ready. See the [SupervisedFineTuningJob](#supervisedfinetuningjob) section for details on the parameters.

**Returns:**

* An instance of `SupervisedFineTuningJob`.

```python  theme={null}
job = llm.create_supervised_fine_tuning_job(
    display_name="my-fine-tuning-job",
    dataset_or_id=dataset,
    epochs=3,
    learning_rate=1e-5
)
```

### `reinforcement_step()`

Performs a reinforcement learning step for training. This method creates a new model checkpoint by fine-tuning the current model on the provided dataset with reinforcement learning.

**Arguments:**

* `dataset` *Dataset* - The dataset containing training examples with rewards
* `output_model` *str* - The name of the output model to create
* `lora_rank` *int, optional* - Rank for LoRA fine-tuning. Defaults to 16
* `learning_rate` *float, optional* - Learning rate for training. Defaults to 0.0001
* `max_context_length` *int, optional* - Maximum context length for the model. Defaults to 8192
* `epochs` *int, optional* - Number of training epochs. Defaults to 1
* `batch_size` *int, optional* - Batch size for training. Defaults to 32768
* `accelerator_count` *int, optional* - Number of accelerators to use for training. Defaults to 1
* `accelerator_type` *str, optional* - Type of GPU accelerator to use for training. Supported values: `"NVIDIA_A100_80GB"`, `"NVIDIA_H100_80GB"`, `"NVIDIA_H200_141GB"`. Defaults to `"NVIDIA_A100_80GB"`

<Note>
  When running on a trained LoRA (i.e., when using a model that is already a LoRA fine-tuned checkpoint), the training parameters (`lora_rank`, `learning_rate`, `max_context_length`, `epochs`, `batch_size`) must always be the same as those used in the original LoRA training. Changing these parameters when continuing training from a LoRA checkpoint is not supported and will result in an error.
</Note>

**Returns:**

* An instance of [`ReinforcementStep`](/tools-sdks/python-client/sdk-reference#reinforcementstep) representing the training job

**Note:** The output model name must not already exist. If a model with the same name exists, a `ValueError` will be raised.

```python  theme={null}
# Perform a reinforcement learning step
job = llm.reinforcement_step(
    dataset=dataset,
    output_model="my-improved-model-v1",
    epochs=1,
    learning_rate=1e-5,
    accelerator_count=2,
    accelerator_type="NVIDIA_H100_80GB"
)

# Wait for completion
while not job.is_completed:
    job.raise_if_bad_state()
    time.sleep(1)
    job = job.get()
    if job is None:
        raise Exception("Job was deleted while waiting for completion")

# The new model is now available at job.output_model
```

### `delete_deployment(ignore_checks: bool = False, wait: bool = True)`

Deletes the deployment associated with this LLM instance if one exists.

**Arguments:**

* `ignore_checks` *bool, optional* - Whether to ignore safety checks. Defaults to False.
* `wait` *bool, optional* - Whether to wait for deletion to complete. Defaults to True.

```python  theme={null}
llm.delete_deployment(ignore_checks=True)
```

### `get_time_to_last_token_mean()`

Returns the mean time to last token for non-streaming requests. If no metrics are available, returns None.

**Returns:**

* A float representing the mean time to last token, or None if no metrics are available.

```python  theme={null}
time_to_last_token_mean = llm.get_time_to_last_token_mean()
```

### `with_deployment_type()`

Returns a new LLM instance with the specified deployment type.

**Arguments:**

* `deployment_type` *str* - The deployment type to use ("serverless", "on-demand", "auto", or "on-demand-lora")

**Returns:**

* A new `LLM` instance with the specified deployment type

```python  theme={null}
# Create a new LLM with different deployment type
serverless_llm = llm.with_deployment_type("serverless")
on_demand_llm = llm.with_deployment_type("on-demand")
```

### `with_temperature()`

Returns a new LLM instance with the specified temperature.

**Arguments:**

* `temperature` *float* - The temperature for generation

**Returns:**

* A new `LLM` instance with the specified temperature

```python  theme={null}
# Create a new LLM with different temperature
creative_llm = llm.with_temperature(1.0)
deterministic_llm = llm.with_temperature(0.0)
```

### `with_perf_metrics_in_response()`

Returns a new LLM instance with the specified performance metrics setting.

**Arguments:**

* `perf_metrics_in_response` *bool* - Whether to include performance metrics in responses

**Returns:**

* A new `LLM` instance with the specified performance metrics setting

```python  theme={null}
# Create a new LLM with performance metrics enabled
llm_with_metrics = llm.with_perf_metrics_in_response(True)
```

### `scale_to_zero()`

Sends a request to scale the deployment to 0 replicas but does not wait for it to complete.

**Returns:**

* The deployment object, or None if no deployment exists

```python  theme={null}
deployment = llm.scale_to_zero()
```

### `scale_to_1_replica()`

Scales the deployment to at least 1 replica.

```python  theme={null}
llm.scale_to_1_replica()
```

### `get_deployment()`

Returns the deployment associated with this LLM instance, or None if no deployment exists.

**Returns:**

* The deployment object, or None if no deployment exists

```python  theme={null}
deployment = llm.get_deployment()
```

### `is_peft_addon()`

Checks if this LLM is a PEFT (Parameter-Efficient Fine-Tuning) addon.

**Returns:**

* True if this LLM is a PEFT addon, False otherwise

```python  theme={null}
is_peft = llm.is_peft_addon()
```

### `list_models()`

Lists all models available to your account.

**Returns:**

* A list of model objects

```python  theme={null}
models = llm.list_models()
```

### `get_model()`

Gets the model object for this LLM's model.

**Returns:**

* The model object, or None if the model doesn't exist

```python  theme={null}
model = llm.get_model()
```

### `is_available_on_serverless()`

Checks if the model is available on serverless infrastructure.

**Returns:**

* True if the model is available on serverless, False otherwise

```python  theme={null}
is_serverless = llm.is_available_on_serverless()
```

### `model_id()`

Returns the model ID, which is the model name plus the deployment name if it exists. This is used for the "model" arg when calling the model.

**Returns:**

* The model ID string

```python  theme={null}
model_id = llm.model_id()
```

### `supports_serverless_lora()`

Checks if the model supports serverless LoRA deployment.

**Returns:**

* True if the model supports serverless LoRA, False otherwise

```python  theme={null}
supports_lora = llm.supports_serverless_lora()
```

### `list_fireworks_models()`

Lists all models available on the Fireworks account.

**Returns:**

* A list of model objects from the Fireworks account

```python  theme={null}
fireworks_models = llm.list_fireworks_models()
```

### `is_model_on_fireworks_account()`

Checks if the model is on the Fireworks account.

**Arguments:**

* `model` *str* - The model identifier to check

**Returns:**

* The model object if it exists on the Fireworks account, None otherwise

```python  theme={null}
model_obj = llm.is_model_on_fireworks_account("accounts/fireworks/models/llama-v3p2-3b-instruct")
```

### `is_model_available_on_serverless()`

Checks if a specific model is available on serverless infrastructure.

**Arguments:**

* `model` *str* - The model identifier to check

**Returns:**

* True if the model is available on serverless, False otherwise

```python  theme={null}
is_serverless = llm.is_model_available_on_serverless("accounts/fireworks/models/llama-v3p2-3b-instruct")
```

### `is_model_deployed_on_serverless_account()`

Checks if a model is deployed on a serverless-enabled account.

**Arguments:**

* `model` *SyncModel* - The model object to check

**Returns:**

* True if the model is deployed on a supported serverless account, False otherwise

```python  theme={null}
model_obj = llm.get_model()
if model_obj:
    is_deployed = llm.is_model_deployed_on_serverless_account(model_obj)
```

### `completions.create()` and `completions.acreate()`

Creates a text completion using the LLM. These methods are OpenAI compatible and follow the same interface as described in the [OpenAI Completions API](https://platform.openai.com/docs/api-reference/completions/create). Use `create()` for synchronous calls and `acreate()` for asynchronous calls.

**Arguments:**

* `prompt` *str* - The prompt to complete
* `stream` *bool, optional* - Whether to stream the response. Defaults to False
* `images` *list\[str], optional* - List of image URLs for multimodal models
* `max_tokens` *int, optional* - The maximum number of tokens to generate
* `logprobs` *int, optional* - Number of log probabilities to return
* `echo` *bool, optional* - Whether to echo the prompt in the response
* `temperature` *float, optional* - Sampling temperature between 0 and 2. If not provided, uses the LLM's default temperature
* `top_p` *float, optional* - Nucleus sampling parameter
* `top_k` *int, optional* - Top-k sampling parameter (must be between 0 and 100)
* `frequency_penalty` *float, optional* - Frequency penalty for repetition
* `presence_penalty` *float, optional* - Presence penalty for repetition
* `repetition_penalty` *float, optional* - Repetition penalty
* `reasoning_effort` *str, optional* - How much effort the model should put into reasoning
* `mirostat_lr` *float, optional* - Mirostat learning rate
* `mirostat_target` *float, optional* - Mirostat target entropy
* `n` *int, optional* - Number of completions to generate
* `ignore_eos` *bool, optional* - Whether to ignore end-of-sequence tokens
* `stop` *str or list\[str], optional* - Stop sequences
* `response_format` *dict, optional* - An object specifying the format that the model must output
* `context_length_exceeded_behavior` *str, optional* - How to handle context length exceeded
* `user` *str, optional* - User identifier
* `extra_headers` *dict, optional* - Additional headers to include in the request
* `**kwargs` - Additional parameters supported by the OpenAI API

**Returns:**

* `Completion` when `stream=False` (default)
* `Generator[Completion, None, None]` when `stream=True` (sync version)
* `AsyncGenerator[Completion, None]` when `stream=True` (async version)

```python  theme={null}
import asyncio
from fireworks import LLM

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

# Synchronous usage
response = llm.completions.create(
    prompt="Hello, world!"
)
print(response.choices[0].text)

# Synchronous streaming
for chunk in llm.completions.create(
    prompt="Tell me a story",
    stream=True
):
    if chunk.choices[0].text:
        print(chunk.choices[0].text, end="")

# Asynchronous usage
async def main():
    response = await llm.completions.acreate(
        prompt="Hello, world!"
    )
    print(response.choices[0].text)

    # Async streaming
    async for chunk in llm.completions.acreate(
        prompt="Tell me a story",
        stream=True
    ):
        if chunk.choices[0].text:
            print(chunk.choices[0].text, end="")

asyncio.run(main())
```

### `chat.completions.create()` and `chat.completions.acreate()`

Creates a chat completion using the LLM. These methods are OpenAI compatible and follow the same interface as described in the [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create). Use `create()` for synchronous calls and `acreate()` for asynchronous calls.

**Note:** The Fireworks chat completions API includes additional request and response fields beyond the standard OpenAI API. See the [Fireworks Chat Completions API reference](/api-reference/post-chatcompletions) for the complete set of available parameters and response fields.

**Arguments:**

* `messages` *list* - A list of messages comprising the conversation so far
* `stream` *bool, optional* - Whether to stream the response. Defaults to False
* `response_format` *dict, optional* - An object specifying the format that the model must output
* `reasoning_effort` *str, optional* - How much effort the model should put into reasoning
* `max_tokens` *int, optional* - The maximum number of tokens to generate
* `temperature` *float, optional* - Sampling temperature between 0 and 2. If not provided, uses the LLM's default temperature. Note that temperature can also be set once during LLM instantiation if preferred
* `tools` *list, optional* - A list of tools the model may call
* `extra_headers` *dict, optional* - Additional headers to include in the request
* `**kwargs` - Additional parameters supported by the OpenAI API

**Returns:**

* `ChatCompletion` when `stream=False` (default)
* `Generator[ChatCompletionChunk, None, None]` when `stream=True` (sync version)
* `AsyncGenerator[ChatCompletionChunk, None]` when `stream=True` (async version)

For details on the `ChatCompletion` object structure, see the [OpenAI Chat Completion Object documentation](https://platform.openai.com/docs/api-reference/chat/object). For the `ChatCompletionChunk` object structure used in streaming, see the [OpenAI Chat Streaming documentation](https://platform.openai.com/docs/api-reference/chat-streaming/streaming).

```python  theme={null}
import asyncio
from fireworks import LLM

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

# Synchronous usage
response = llm.chat.completions.create(
    messages=[
        {"role": "user", "content": "Hello, world!"}
    ]
)
print(response.choices[0].message.content)

# Synchronous streaming
for chunk in llm.chat.completions.create(
    messages=[
        {"role": "user", "content": "Tell me a story"}
    ],
    stream=True
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# Asynchronous usage
async def main():
    response = await llm.chat.completions.acreate(
        messages=[
            {"role": "user", "content": "Hello, world!"}
        ]
    )
    print(response.choices[0].message.content)

    # Async streaming
    async for chunk in await llm.chat.completions.acreate(
        messages=[
            {"role": "user", "content": "Tell me a story"}
        ],
        stream=True
    ):
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

asyncio.run(main())
```

## Dataset

The `Dataset` class provides a convenient way to manage datasets for fine-tuning on Fireworks. It offers smart features like automatic naming and uploading of datasets. You do not instantiate a `Dataset` object directly. Instead, you create a `Dataset` object by using one of the class methods below.

**Properties:**

* `name` *str* - The full name of the dataset (e.g., `accounts/my-account/datasets/dataset-12345-my-data`)
* `id` *str* - The dataset identifier (e.g., `dataset-12345-my-data`)
* `url` *str* - The URL to view the dataset in the Fireworks dashboard

### `from_list()`

```python  theme={null}
@classmethod
from_list(data: list)
```

Creates a Dataset from a list of training examples. Each example should be compatible with OpenAI's chat completion format.

```python  theme={null}
from fireworks import Dataset

# Create dataset from a list of examples
examples = [
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
            {"role": "assistant", "content": "Paris."}
        ]
    }
]
dataset = Dataset.from_list(examples)
```

### `from_file()`

```python  theme={null}
@classmethod
from_file(path: str)
```

Creates a Dataset from a local JSONL file. The file should contain training examples in OpenAI's chat completion format.

```python  theme={null}
from fireworks import Dataset

# Create dataset from a JSONL file
dataset = Dataset.from_file("path/to/training_data.jsonl")
```

### `from_string()`

```python  theme={null}
@classmethod
from_string(data: str)
```

Creates a Dataset from a string containing JSONL-formatted training examples.

```python  theme={null}
from fireworks import Dataset

# Create dataset from a JSONL string
jsonl_data = """
{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there!"}]}
{"messages": [{"role": "user", "content": "What is 1+1?"}, {"role": "assistant", "content": "2"}]}
"""
dataset = Dataset.from_string(jsonl_data)
```

### `from_id()`

```python  theme={null}
@classmethod
from_id(id: str)
```

Creates a Dataset from an existing dataset ID on Fireworks.

```python  theme={null}
from fireworks import Dataset

# Create dataset from existing ID
dataset = Dataset.from_id("existing-dataset-id")
```

### `sync()`

Uploads the dataset to Fireworks if it doesn't already exist. This method automatically:

1. Checks if a dataset with the same content hash already exists
2. If it exists, skips the upload to avoid duplicates
3. If it doesn't exist, creates and uploads the dataset to Fireworks
4. Validates the dataset after upload

```python  theme={null}
from fireworks import Dataset

# Create dataset and sync it to Fireworks
dataset = Dataset.from_file("path/to/training_data.jsonl")
dataset.sync()

# The dataset is now available on Fireworks and ready for fine-tuning
```

### `delete()`

Deletes the dataset from Fireworks.

```python  theme={null}
dataset = Dataset.from_file("path/to/training_data.jsonl")
dataset.delete()
```

### `head(n: int = 5, as_dataset: bool = False)`

Returns the first n rows of the dataset.

**Arguments:**

* `n` *int, optional* - Number of rows to return. Defaults to 5.
* `as_dataset` *bool, optional* - If True, return a Dataset object; if False, return a list. Defaults to False.

**Returns:**

* *list or Dataset* - List of dictionaries if as\_dataset=False, Dataset object if as\_dataset=True

```python  theme={null}
# Get first 5 rows as a list
first_5_rows = dataset.head(5)

# Get first 10 rows as a new dataset
first_10_dataset = dataset.head(10, as_dataset=True)
```

### `create_evaluation_job(reward_function: Callable, samples: Optional[int] = None)`

Creates an evaluation job using a reward function for this dataset.

**Arguments:**

* `reward_function` *Callable* - A callable decorated with @reward\_function
* `samples` *int, optional* - Optional number of samples to evaluate (creates a subset dataset)

**Returns:**

* *EvaluationJob* - The created evaluation job

```python  theme={null}
from fireworks import reward_function

@reward_function
def my_reward_function(response, context):
    # Your reward logic here
    return 1.0

evaluation_job = dataset.create_evaluation_job(my_reward_function, samples=100)
```

### `preview_evaluator(reward_function: Callable, samples: Optional[int] = None)`

Previews the evaluator for the dataset.

**Arguments:**

* `reward_function` *Callable* - A callable decorated with @reward\_function
* `samples` *int, optional* - Optional number of samples to preview

**Returns:**

* *SyncPreviewEvaluatorResponse* - Preview response from the evaluator

```python  theme={null}
preview_response = dataset.preview_evaluator(my_reward_function, samples=10)
```

### Data Format

The Dataset class expects data in OpenAI's chat completion format. Each training example should be a JSON object with a `messages` array containing message objects. Each message object should have:

* `role`: One of `"system"`, `"user"`, or `"assistant"`
* `content`: The message content as a string

Example format:

```json  theme={null}
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris."}
    ]
}
```

## SupervisedFineTuningJob

The `SupervisedFineTuningJob` class manages fine-tuning jobs on Fireworks. It provides a convenient interface for creating, monitoring, and managing fine-tuning jobs.

```python  theme={null}
class SupervisedFineTuningJob()
```

**Properties:**

* `output_model` *str* - The identifier of the output model (e.g., `accounts/my-account/models/my-finetuned-model`)
* `output_llm` *LLM* - An LLM instance associated with the output model
* `id` *str* - The job ID
* `display_name` *str* - The display name of the job
* `name` *str* - The full name of the job
* `url` *str* - The URL to view the job in the Fireworks dashboard

### Instantiation

You do not need to directly instantiate a `SupervisedFineTuningJob` object. Instead, you should use the `.create_supervised_fine_tuning_job()` method on the `LLM` object and pass in the following required and optional arguments.

#### Required Arguments

* `display_name` *str* - A unique name for the fine-tuning job. Must only contain lowercase a-z, 0-9, and hyphen (-).
* `dataset_or_id` *Union\[Dataset, str]* - The dataset to use for fine-tuning, either as a Dataset object or dataset ID

#### Optional Arguments

**Training Configuration**

* `epochs` *int, optional* - Number of training epochs
* `learning_rate` *float, optional* - Learning rate for training
* `lora_rank` *int, optional* - Rank for LoRA fine-tuning
* `jinja_template` *str, optional* - Template for formatting training examples
* `early_stop` *bool, optional* - Whether to enable early stopping
* `max_context_length` *int, optional* - Maximum context length for the model
* `base_model_weight_precision` *str, optional* - Precision for base model weights
* `batch_size` *int, optional* - Batch size for training

**Hardware Configuration**

* `accelerator_type` *str, optional* - Type of GPU accelerator to use
* `accelerator_count` *int, optional* - Number of accelerators to use
* `is_turbo` *bool, optional* - Whether to use turbo mode for faster training
* `region` *str, optional* - Region for deployment
* `nodes` *int, optional* - Number of nodes to use

**Evaluation & Monitoring**

* `evaluation_dataset` *str, optional* - Dataset ID to use for evaluation
* `eval_auto_carveout` *bool, optional* - Whether to automatically carve out evaluation data
* `wandb_config` *WandbConfig, optional* - Configuration for Weights & Biases integration

**Job Management**

* `output_model` *str, optional* - The name of the output model to create. If not provided, it will be the same as the display\_name argument.

### `sync()`

Creates the job if it doesn't exist, otherwise returns the existing job. If previous job failed, deletes it and creates a new one.

**Returns:**

* *SupervisedFineTuningJob* - The synced job object

```python  theme={null}
job = job.sync()
```

### `wait_for_completion()`

Polls the job status until it is complete and returns the job object.

**Returns:**

* *SupervisedFineTuningJob* - The completed job object

```python  theme={null}
job = job.wait_for_completion()
```

### `await_for_completion()`

Asynchronously polls the job status until it is complete and returns the job object.

**Returns:**

* *SupervisedFineTuningJob* - The completed job object

```python  theme={null}
job = await job.await_for_completion()
```

### `delete()`

Deletes the job.

```python  theme={null}
job.delete()
```

### `adelete()`

Asynchronously deletes the job.

```python  theme={null}
await job.adelete()
```

## ReinforcementStep

The `ReinforcementStep` class represents a reinforcement learning training step.
It provides methods to monitor and manage the training process.

```python  theme={null}
class ReinforcementStep()
```

**Properties:**

* `state` *str* - The current state of the training job (e.g., "JOB\_STATE\_RUNNING", "JOB\_STATE\_COMPLETED")
* `output_model` *str* - The identifier of the output model (e.g., `accounts/my-account/models/my-improved-model`)
* `is_completed` *bool* - Whether the training job has completed successfully

### `get()`

Retrieves the current state of the training job from the server.

**Returns:**

* A `ReinforcementStep` object with updated state, or `None` if the job no longer exists

```python  theme={null}
# Get updated job status
updated_job = job.get()
if updated_job is None:
    print("Job was deleted")
else:
    print(f"Job state: {updated_job.state}")
```

### `raise_if_bad_state()`

Raises a `RuntimeError` if the job is in a failed, cancelled, or otherwise bad state. This is useful for error handling during training.

**Raises:**

* `RuntimeError` - If the job is in a bad state (failed, cancelled, expired, etc.)

```python  theme={null}
# Check for bad states during training
try:
    job.raise_if_bad_state()
except RuntimeError as e:
    print(f"Training failed: {e}")
```

### Usage Example

```python  theme={null}
import time
from fireworks import LLM, Dataset

# Create base model
llm = LLM(
    model="qwen2p5-7b-instruct",
    deployment_type="on-demand",
    id="my-base-deployment",
    enable_addons=True
)

# Apply deployment configuration to Fireworks
llm.apply()

# Generate rollouts and create dataset
# (This would be your rollout generation logic)
dataset = Dataset.from_list([
    {
        "samples": [
            {
                "messages": [
                    {"role": "user", "content": "What is 2+2?"},
                    {"role": "assistant", "content": "4"}
                ],
                "evals": {"score": 1.0}
            }
        ]
    }
])
dataset.sync()

# Perform reinforcement learning step
job = llm.reinforcement_step(
    dataset=dataset,
    output_model="my-improved-model-v1",
    epochs=1
)

# Monitor training progress
while not job.is_completed:
    job.raise_if_bad_state()
    print(f"Training state: {job.state}")
    time.sleep(10)
    job = job.get()
    if job is None:
        raise Exception("Job was deleted while waiting for completion")

print(f"Training completed! New model: {job.output_model}")

# Use the improved model
improved_llm = LLM(
    model=job.output_model,
    deployment_type="on-demand-lora",
    base_id=llm.deployment_id
)
improved_llm.apply()
```

### Iterative Reinforcement Learning Workflow

The `reinforcement_step` method is designed to support iterative reinforcement learning workflows. Here's a complete example showing how to perform multiple reinforcement learning steps:

```python  theme={null}
import asyncio
import time
import random
from fireworks import LLM, Dataset

# Initialize base model
base_model = LLM(
    model="qwen2p5-7b-instruct",
    deployment_type="on-demand",
    id="my-base-deployment",
    enable_addons=True  # Enable LoRA addons to only use one deployment for all steps
)

# Apply deployment configuration to Fireworks
base_model.apply()

# Number of reinforcement learning steps
num_steps = 5

# Iterative reinforcement learning loop
async def run_reinforcement_learning():
    for step in range(num_steps):
        print(f"Starting reinforcement learning step {step + 1}/{num_steps}")
        
        # Create deployment for current model snapshot
        if step == 0:
            # Use base model for first step
            model_snapshot = base_model
        else:
            # Use the improved model from previous step
            model_snapshot = LLM(
                model=f"accounts/my-account/models/my-improved-model-v{step}",
                deployment_type="on-demand-lora",
                base_id=base_model.deployment_id
            )
        
        # Ensure deployment is ready
        model_snapshot.apply()
        
        # Generate rollouts and rewards (your custom logic here)
        # This is where you would:
        # 1. Generate rollouts by calling the deployment's inference endpoint
        # 2. Evaluate responses and compute rewards locally
        dataset_rows = await generate_rollouts_and_rewards(
            model_snapshot,
            num_prompts=10,
            num_generations_per_prompt=8,
            concurrency=100
        )
        
        # Create dataset from dataset rows
        dataset = Dataset.from_list(dataset_rows)
        dataset.sync()
        
        # Perform reinforcement learning step
        job = model_snapshot.reinforcement_step(
            dataset=dataset,
            output_model=f"my-improved-model-v{step + 1}",
            epochs=1,
            learning_rate=1e-5,
            accelerator_count=1,
            accelerator_type="NVIDIA_A100_80GB"
        )
        
        # Wait for training completion
        while not job.is_completed:
            job.raise_if_bad_state()
            print(f"Training state: {job.state}")
            time.sleep(10)
            job = job.get()
            if job is None:
                raise Exception("Job was deleted while waiting for completion")
        
        print(f"Step {step + 1} completed! New model: {job.output_model}")
        
        # Clean up dataset
        dataset.delete()

    print("Reinforcement learning complete!")

# Run the async reinforcement learning workflow
asyncio.run(run_reinforcement_learning())

# Example rollout generation function with concurrent generation
async def generate_rollouts_and_rewards(llm, num_prompts=10, num_generations_per_prompt=8, concurrency=100):
    """
    Generate rollouts and compute rewards for the given model using concurrent generation.
    Each sample contains multiple generations for Policy Optimization.
    """
    semaphore = asyncio.Semaphore(concurrency)
    
    async def generate_single_response(prompt_id, generation_id):
        """Generate a single response for a given prompt."""
        async with semaphore:
            messages = [
                {"role": "user", "content": f"What is {prompt_id} + {prompt_id}?"}
            ]
            
            response = await llm.chat.completions.acreate(
                messages=messages,
                max_tokens=50,
                temperature=1.5,  # Higher temperature for more diverse responses
                n=1  # Generate one response at a time
            )
            
            assistant_message = response.choices[0].message.content
            
            # Compute reward for this generation
            if str(prompt_id + prompt_id) in assistant_message:
                reward = 1.0  # Correct answer
            else:
                reward = 0.0  # Incorrect answer
            
            return {
                "prompt_id": prompt_id,
                "generation_id": generation_id,
                "messages": messages + [{"role": "assistant", "content": assistant_message}],
                "evals": {"score": reward}
            }
    
    # Create all generation tasks concurrently
    coros = []
    for prompt_id in range(num_prompts):
        for generation_id in range(num_generations_per_prompt):
            coro = generate_single_response(prompt_id, generation_id)
            coros.append(coro)
    
    # Execute all generations concurrently
    print(f"Starting {len(coros)} concurrent generations...")
    num_completed = 0
    results = []
    
    for coro in asyncio.as_completed(coros):
        result = await coro
        results.append(result)
        num_completed += 1
        if num_completed % 10 == 0:
            print(f"Completed {num_completed}/{len(coros)} generations")
    
    # Group results by prompt_id to create dataset rows
    dataset_rows = []
    for prompt_id in range(num_prompts):
        prompt_generations = [r for r in results if r["prompt_id"] == prompt_id]
        sample_generations = [
            {
                "messages": gen["messages"],
                "evals": gen["evals"]
            }
            for gen in prompt_generations
        ]
        dataset_rows.append({
            "samples": sample_generations
        })
    
    return dataset_rows
```

This workflow demonstrates the iterative nature of reinforcement learning, where each step:

1. Uses the current model snapshot to generate rollouts
2. For each prompt, generates multiple responses (required for Policy Optimization)
3. Evaluates each response and computes rewards
4. Creates a dataset with the rollouts and rewards (each sample contains multiple generations)
5. Performs a reinforcement learning step to create an improved model

<Note>
  Each sample in the dataset must contain multiple trajectories for the same prompt. This is required for policy optimization to work.
</Note>

## BatchInferenceJob

The `BatchInferenceJob` class provides a convenient way to manage batch inference jobs on Fireworks. It allows you to perform bulk asynchronous inference on large datasets, reducing costs by up to 50%.

```python  theme={null}
class BatchInferenceJob()
```

**Properties:**

* `name` *str* - The full name of the batch inference job (e.g., `accounts/my-account/batchInferenceJobs/test-job-123`)
* `id` *str* - The job identifier (e.g., `test-job-123`)
* `model` *str* - The model used for inference
* `input_dataset_id` *str* - The input dataset identifier
* `output_dataset_id` *str* - The output dataset identifier
* `state` *str* - The current state of the job
* `created_by` *str* - Email of the user who created the job
* `create_time` *str* - Creation timestamp
* `update_time` *str* - Last update timestamp

### `create()`

```python  theme={null}
@staticmethod
create(
    model: str,
    input_dataset_id: str,
    output_dataset_id: Optional[str] = None,
    job_id: Optional[str] = None,
    display_name: Optional[str] = None,
    inference_parameters: Optional[dict] = None,
    api_key: Optional[str] = None,
) -> BatchInferenceJob
```

Creates a new batch inference job.

**Arguments:**

* `model` *str* - The model to use for inference (e.g., `llama-v3p1-8b-instruct` or `accounts/fireworks/models/llama-v3p1-8b-instruct`)
* `input_dataset_id` *str* - The input dataset ID containing JSONL formatted requests
* `output_dataset_id` *str, optional* - The output dataset ID. If not provided, one will be auto-generated
* `job_id` *str, optional* - The job ID. If not provided, one will be auto-generated
* `display_name` *str, optional* - Display name for the job
* `inference_parameters` *dict, optional* - Dict of inference parameters:
  * `max_tokens` *int* - Maximum number of tokens to generate
  * `temperature` *float* - Sampling temperature (0-2)
  * `top_p` *float* - Top-p sampling parameter
  * `top_k` *int* - Top-k sampling parameter
  * `n` *int* - Number of completions per request
  * `extra_body` *str* - Additional parameters as JSON string
* `api_key` *str, optional* - The API key to use

**Returns:**

* A `BatchInferenceJob` object

```python  theme={null}
from fireworks import BatchInferenceJob

# Create a batch inference job
job = BatchInferenceJob.create(
    model="llama-v3p1-8b-instruct",
    input_dataset_id="my-input-dataset",
    output_dataset_id="my-output-dataset",
    job_id="my-batch-job",
    display_name="My Batch Processing Job",
    inference_parameters={
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9
    }
)
```

### `get()`

```python  theme={null}
@staticmethod
get(job_id: str, account: str, api_key: Optional[str] = None) -> Optional[BatchInferenceJob]
```

Retrieves a batch inference job by its ID.

**Arguments:**

* `job_id` *str* - The job ID or full resource name
* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use

**Returns:**

* A `BatchInferenceJob` object if found, `None` otherwise

```python  theme={null}
# Get an existing batch inference job
job = BatchInferenceJob.get(
    job_id="my-batch-job",
    account="my-account"
)

if job:
    print(f"Job state: {job.state}")
    print(f"Created by: {job.created_by}")
```

### `list()`

```python  theme={null}
@staticmethod
list(
    account: str,
    api_key: Optional[str] = None,
    page_size: int = 50
) -> list[BatchInferenceJob]
```

Lists batch inference jobs in an account.

**Arguments:**

* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use
* `page_size` *int, optional* - Number of jobs to return per page. Defaults to 50

**Returns:**

* A list of `BatchInferenceJob` objects

```python  theme={null}
# List all batch inference jobs
jobs = BatchInferenceJob.list(account="my-account")

for job in jobs:
    print(f"Job: {job.id}, State: {job.state}, Model: {job.model}")
```

### `delete()`

```python  theme={null}
@staticmethod
delete(job_id: str, account: str, api_key: Optional[str] = None) -> None
```

Deletes a batch inference job.

**Arguments:**

* `job_id` *str* - The job ID or full resource name
* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use

```python  theme={null}
# Delete a batch inference job
BatchInferenceJob.delete(
    job_id="my-batch-job",
    account="my-account"
)
```

### `to_dict()`

```python  theme={null}
@staticmethod
to_dict(proto: BatchInferenceJob) -> dict
```

Converts a batch inference job proto to a friendly dictionary representation.

**Arguments:**

* `proto` *BatchInferenceJob* - The batch inference job proto object

**Returns:**

* A dictionary with human-readable field values

```python  theme={null}
# Convert job to dictionary for easy viewing
job = BatchInferenceJob.get("my-batch-job", "my-account")
if job:
    job_dict = BatchInferenceJob.to_dict(job)
    print(job_dict)
    # Output:
    # {
    #     'name': 'accounts/my-account/batchInferenceJobs/my-batch-job',
    #     'display_name': 'My Batch Job',
    #     'model': 'accounts/fireworks/models/llama-v3p1-8b-instruct',
    #     'state': 'JOB_STATE_COMPLETED',
    #     'create_time': '2024-01-01 08:00:00 UTC',
    #     'inference_parameters': {'max_tokens': 1024, 'temperature': 0.7}
    # }
```


# Tutorial
Source: https://docs.fireworks.ai/tools-sdks/python-client/the-tutorial



## Foreword

This tutorial demonstrates how to use the Fireworks AI Python SDK with a few toy examples. First, we will use the LLM class to make a simple request to various models and compare the outputs. Then, we will try to fine-tune a model to learn information it has never seen before.

<Warning>
  This tutorial will cost \$10 to run due to the on-demand model deployments.
</Warning>

## 1. Setup

To get started with the Fireworks AI Python SDK, you need to install the `firectl` CLI tool and create an API key.

<Steps>
  <Step>
    Install our CLI tool `firectl` to interact with the Fireworks AI platform.

    <CodeGroup>
      ```bash macOS (Apple Silicon) theme={null}
      brew tap fw-ai/firectl
      brew install firectl
      ```

      ```bash macOS (x86_64) theme={null}
      curl https://storage.googleapis.com/fireworks-public/firectl/stable/darwin-amd64.gz -o firectl.gz
      gzip -d firectl.gz && chmod a+x firectl
      sudo mv firectl /usr/local/bin/firectl
      sudo chown root: /usr/local/bin/firectl
      ```

      ```bash Linux (x86_64) theme={null}
      wget -O firectl.gz https://storage.googleapis.com/fireworks-public/firectl/stable/linux-amd64.gz
      gunzip firectl.gz
      sudo install -o root -g root -m 0755 firectl /usr/local/bin/firectl

      ```

      ```bash Windows (64 bit) theme={null}
      wget -L https://storage.googleapis.com/fireworks-public/firectl/stable/firectl.exe
      ```
    </CodeGroup>
  </Step>

  <Step>
    Sign in to Fireworks by running the following command:

    ```bash  theme={null}
    firectl signin
    ```

    A browser window will open to the Fireworks AI login page. Once you login, your machine will be authenticated.
  </Step>

  <Step>
    Create an API key by running the following command:

    ```bash {1,4} theme={null}
    $ firectl create api-key --key-name "quick-start"
    Key Id: key_42vAYeb7rwt9zzg1
    Display Name: quick-start
    Key: fw_3ZLd....
    Secure: true
    Be sure to save this key. It will not be shown again.
    ```

    Copy the value of the `Key` field to your environment variable `FIREWORKS_API_KEY`.

    ```bash  theme={null}
    export FIREWORKS_API_KEY=fw_3ZLd....
    ```
  </Step>

  <Step>
    Install the Fireworks AI Python SDK.

    <CodeGroup>
      ```bash pip theme={null}
      pip install --upgrade fireworks-ai
      ```

      ```bash poetry theme={null}
      poetry add fireworks-ai
      ```

      ```bash uv theme={null}
      uv add fireworks-ai --upgrade
      ```
    </CodeGroup>
  </Step>
</Steps>

Once you have completed the steps above, let's ensure you are ready to make your first LLM call.

## 2. Call a language model using the `LLM()` class

Now that your machine is setup with credentials and the SDK, lets ensure you are
ready to make your first LLM call and explain some of the nuances of this SDK.

<Steps>
  <Step>
    Create a new file called `main.py` and import the Fireworks AI SDK.

    ```python main.py theme={null}
    from fireworks import LLM
    ```
  </Step>

  <Step>
    Instantiate the `LLM` class. The LLM class accepts a `model` argument that you
    can use to specify the model you want to use. For this tutorial, we will use the
    [Llama 4 Maverick
    model](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic).

    ```python main.py theme={null}
    from fireworks import LLM

    llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto") 
    ```

    When creating an LLM instance, you can specify the deployment type as either `"serverless"`, `"on-demand"`, or `"auto"`. If you pass `"auto"`, the SDK will try to use serverless hosting if available, otherwise it will create an on-demand deployment. In the other cases, the SDK will try to create a deployment of the specified type and will throw an error if it's not available for the model you selected.

    <Tip>
      The SDK will try and re-use existing deployments for the same model if possible, see [Resource management](/tools-sdks/python-client/sdk-basics#resource-management) for more details.
    </Tip>

    <Warning>
      With great power comes great responsibility! Be careful with the `deployment_type` parameter, especially for `"auto"` and `"on-demand"`. While the SDK will try to make the most cost effective choice for you and put sensible autoscaling policies in place, it is possible to unintentionally create many deployments that lead to unwanted spend, especially when working with non-serverless models.
    </Warning>

    <Warning>
      When using `deployment_type="on-demand"`, you must provide an `id` parameter to uniquely identify your deployment. This is required to prevent accidental creation of multiple deployments.
    </Warning>

    <Note>
      When using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`, you must call `.apply()` to apply the deployment configuration to Fireworks. This is not required for serverless deployments. When using `deployment_type="auto"`, the SDK will automatically handle deployment creation, but if it falls back to on-demand deployment, you may need to call `.apply()` explicitly. If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments).
    </Note>
  </Step>

  <Step>
    Make a request to the LLM. The `LLM` class is OpenAI compatible, so you can use
    the same chat completion interface to make a request to the LLM.

    <CodeGroup>
      ```python main.py theme={null}
      from fireworks import LLM

      llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="auto") 

      response = llm.chat.completions.create(
          messages=[{"role": "user", "content": "Hello, world!"}]
      )

      print(response.choices[0].message.content)
      ```

      ```text Output theme={null}
      Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?
      ```
    </CodeGroup>
  </Step>

  <Step>
    The great thing about the SDK is that you can use your favorite Python constructs to powerfully work with LLMs. For example, let's try calling a few LLMs in a loop and see how they respond:

    ```python main.py theme={null}
    from fireworks import LLM

    llms = [
        "llama4-maverick-instruct-basic",
        "deepseek-r1",
        "qwen2p5-vl-32b-instruct"
    ]

    for llm in llms:
        llm = LLM(model=llm, deployment_type="auto") 
        print("\n" + "-" * 100)
        print(f"Model: {llm.model}")
        print("-" * 100 + "\n")

        response = llm.chat.completions.create(
            messages=[{"role": "user", "content": "Hello, world!"}]
        )
        print(response.choices[0].message.content)
    ```

    Or, we can test different temperature values to see how the model's behavior changes:

    ```python main.py theme={null}
    from fireworks import LLM

    for temperature in [0.0, 0.5, 1.0, 2.0]:

        llm = LLM(model="llama4-maverick-instruct-basic", temperature=temperature, deployment_type="auto") 
        print("\n" + "-" * 100)
        print(f"Temperature: {temperature}")
        response = llm.chat.completions.create(
            messages=[{"role": "user", "content": "a b c d e f "}]
        )
        print("-" * 100)
        print(response.choices[0].message.content)
    ```
  </Step>
</Steps>

## 3. Fine-tune a model

The Build SDK makes fine-tuning a model a breeze! To see how, let's try a canonical use case: fine-tuning a model to learn information it has never seen before. To do this, we will use the [TOFU (Task of Fictitious Unlearning)](https://locuslab.github.io/tofu/) dataset. The dataset consists of \~4,000 question-answer pairs on autobiographies of 200 fictitious authors. Researchers fine-tuned a model on this dataset with the goal of investigating ways to "unlearn" this information. For our toy example, however, we will only focus on the first step: trying to embed these nonsense facts into an LLM.

<Steps>
  <Step>
    Install the required dependencies, you will need the `datasets` library from Hugging Face to load the dataset.

    ```bash  theme={null}
    pip install datasets
    ```
  </Step>

  <Step>
    Load and prepare the dataset. We must convert the dataset to the format expected by the fine-tuning service, which is a list of chat completion messages following the OpenAI chat completion format.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ```
  </Step>

  <Step>
    We can then create a `Dataset` object and upload it to Fireworks using the `Dataset.from_list()` method.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)
    ```
  </Step>

  <Step>
    Now we can create a base model and fine-tune it on the dataset. Let's try fine-tuning Qwen2.5 7B Instruct. At this time, it might be helpful to set the `FIREWORKS_SDK_DEBUG` environment variable to `true` to see the progress of the fine-tuning job.

    <Warning>
      Qwen2.5 7B Instruct is not available serverlessly, so the SDK will create an on-demand deployment with a scale-down window of 5 mins. This will incur some costs.
    </Warning>

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)

    base_model = LLM(model="qwen2p5-7b-instruct", id="qwen2p5-7b-instruct-base", deployment_type="auto")

    job = base_model.create_supervised_fine_tuning_job(
        "fine-tune-tofu-dataset",
        ds,
        epochs=2
    )

    job.wait_for_completion() # This will take a few minutes to complete

    fine_tuned_model = job.output_llm
    ```
  </Step>

  <Step>
    Now we can test the fine-tuned model.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    def example_to_prompt(example):
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["question"]},
            {"role": "assistant", "content": example["answer"]},
        ]
        return {"messages": message}

    fine_tune_dataset = []
    for example in dataset["train"]:
        fine_tune_dataset.append(example_to_prompt(example))

    ds = Dataset.from_list(fine_tune_dataset)

    base_model = LLM(model="qwen2p5-7b-instruct", id="qwen2p5-7b-instruct-base", deployment_type="auto")

    # Apply deployment configuration to Fireworks
    base_model.apply()

    job = base_model.create_supervised_fine_tuning_job(
        "fine-tune-tofu-dataset",
        ds,
        epochs=2
    )

    job.wait_for_completion()

    fine_tuned_model = job.output_llm

    question = "Where was Aurelio Beltrán born? If you don't know who that is, say 'I don't know who that is'."

    print(f"Base model: {base_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    print(f"Fine-tuned model: {fine_tuned_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    ```

    If everything worked out correctly, you should see something like:

    ```
    Base model: I don't know who that is.
    Fine-tuned model: Aurelio Beltrán was born in Mexico City, Mexico.
    ```

    <Tip>
      Just like we did in the previous section, you can try iterating over different models and fine-tuning hyperparameters like `epochs` and `learning_rate` to experiment with different fine-tuning jobs!
    </Tip>
  </Step>

  <Step>
    You'll notice that despite us using two models in this tutorial, the only *actually* created a single deployment. This is the power of the Build SDK's smart resource management in action! Rather than creating a seperate deployment for the LoRA addon, we simply updated the base model deployment we created to support LoRA addons and then deployed our fine-tuned model on top.

    You can feel free to send more requests to either model. The SDK by default sets a scale-to-zero window of 5 mins, which stops billing after an extended period of inactivity. However, it's good practice to delete deployments you're not using as a precautionary measure against unexpected bills. You can call

    `base_model.delete_deployment(ignore_checks=True)` to delete the deployment, bypassing the check that triggers if you've used the deployment recently.

    ```python tofu.py theme={null}
    from datasets import load_dataset
    from fireworks import LLM, Dataset

    dataset = load_dataset("locuslab/TOFU", "full")

    # ...  rest of the code above

    print(f"Base model: {base_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")
    print(f"Fine-tuned model: {fine_tuned_model.chat.completions.create(messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}], temperature=0.0).choices[0].message.content}")

    base_model.delete_deployment(ignore_checks=True)
    ```
  </Step>
</Steps>

## Conclusion

This tutorial walked you through the basic use cases for the SDK: trying out different models/configurations and fine-tuning on a dataset. From here, you should check out the [Reference](/tools-sdks/python-client/sdk-reference) for more details on the objects and methods available in the SDK.


# Changelog
Source: https://docs.fireworks.ai/updates/changelog



<Update label="2025-10-20">
  ## 🏗️ Build SDK: RFT and Evaluators APIs removed

  The Build SDK no longer supports Reinforcement Fine-Tuning (RFT) and Evaluators-related APIs. To perform RFT, please use our web app via [Reinforcement Fine-Tuning](/fine-tuning/reinforcement-fine-tuning-models).
</Update>

<Update label="2025-08-22">
  ## Supervised Fine-Tuning

  We now support supervised fine tuning with separate thinking traces for reasoning models (e.g. DeepSeek R1, GPT OSS, Qwen3 Thinking etc) that ensures training-inference consistency. An example including thinking traces would look like:

  ```json  theme={null}
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}, 
        {"role": "assistant", "content": "Paris.", "reasoning_content": "The user is asking about the capital city of France, it should be Paris."}
      ]
    }
    {
      "messages": [
        {"role": "user", "content": "What is 1+1?"},
        {"role": "assistant", "content": "2", "weight": 0, "reasoning_content": "The user is asking about the result of 1+1, the answer is 2."},
        {"role": "user", "content": "Now what is 2+2?"},
        {"role": "assistant", "content": "4", "reasoning_content": "The user is asking about the result of 2+2, the answer should be 4."}
      ]
    }
  ```

  We are also properly supporting multi-turn fine tuning (with or without thinking traces) for GPT OSS model family that ensures training-inference consistency.
</Update>

<Update label="2025-08-10">
  ## Supervised Fine-Tuning

  We now support Qwen3 MoE model (Qwen3 dense models are already supported) and GPT OSS models for supervised fine-tuning. GPT OSS model fine tunning support is single-turn without thinking traces at the moment.
</Update>

<Update label="2025-07-29">
  ## 🎨 Vision-Language Model Fine-Tuning

  You can now fine-tune Vision-Language Models (VLMs) on Fireworks AI using the Qwen 2.5 VL model family.
  This extends our Supervised Fine-tuning V2 platform to support multimodal training with both images and text data.

  **Supported models:**

  * Qwen 2.5 VL 3B Instruct
  * Qwen 2.5 VL 7B Instruct
  * Qwen 2.5 VL 32B Instruct
  * Qwen 2.5 VL 72B Instruct

  **Features:**

  * Fine-tune on datasets containing both images and text in JSONL format with base64-encoded images
  * Support for up to 64K context length during training
  * Built on the same Supervised Fine-tuning V2 infrastructure as text models

  See the [VLM fine-tuning documentation](/fine-tuning/fine-tuning-vlm) for setup instructions and dataset formatting requirements.

  ## 🔧 Build SDK: Deployment Configuration Application Requirement

  The Build SDK now requires you to call `.apply()` to apply any deployment configurations to Fireworks when using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`. This change ensures explicit control over when deployments are created and helps prevent accidental deployment creation.

  **Key changes:**

  * `.apply()` is now required for on-demand and on-demand-lora deployments
  * Serverless deployments do not require `.apply()` calls
  * If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments)

  **Migration guide:**

  * Add `llm.apply()` after creating LLM instances with `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`
  * No changes needed for serverless deployments
  * See updated documentation for examples and best practices

  This change improves deployment management and provides better control over resource creation.

  <Note>
    This applies to Python SDK version `>=0.19.14`.
  </Note>
</Update>

<Update label="2025-07-23">
  ## 🚀 Bring Your Own Rollout and Reward Development for Reinforcement Learning

  You can now develop your own custom rollout and reward functionality while using
  Fireworks to manage the training and deployment of your models. This gives you
  full control over your reinforcement learning workflows while leveraging
  Fireworks' infrastructure for model training and deployment.

  See the new [LLM.reinforcement\_step()](/tools-sdks/python-client/sdk-reference#reinforcement-step) method and [ReinforcementStep](/tools-sdks/python-client/sdk-reference#reinforcementstep) class for usage examples and details.
</Update>

<Update label="2025-07-16">
  ## Supervised Fine-Tuning V2

  We now support Llama 4 MoE model supervised fine-tuning (Llama 4 Scout, Llama 4 Maverick, Text only).
</Update>

<Update label="2025-07-10">
  ## 🏗️ Build SDK `LLM` Deployment Logic Refactor

  Based on early feedback from users and internal testing, we've refactored the
  `LLM` class deployment logic in the Build SDK to make it easier to understand.

  **Key changes:**

  * The `id` parameter is now required when `deployment_type` is `"on-demand"`
  * The `base_id` parameter is now required when `deployment_type` is `"on-demand-lora"`
  * The `deployment_display_name` parameter is now optional and defaults to the filename where the LLM was instantiated

  A new deployment will be created if a deployment with the same `id` does not
  exist. Otherwise, the existing deployment will be reused.
</Update>

<Update label="2025-07-02">
  ## 🚀 Support for Responses API in Python SDK

  You can now use the Responses API in the Python SDK. This is useful if you want to use the Responses API in your own applications.

  See the [Responses API guide](/guides/response-api) for usage examples and details.
</Update>

<Update label="2025-07-01">
  ## Support for LinkedIn authentication

  You can now log in to Fireworks using your LinkedIn account. This is useful if
  you already have a LinkedIn account and want to use it to log in to Fireworks.

  To log in with LinkedIn, go to the [Fireworks login
  page](https://fireworks.ai/login) and click the "Continue with LinkedIn"
  button.

  You can also log in with LinkedIn from the CLI using the `firectl login`
  command.

  **How it works:**

  * Fireworks uses your LinkedIn primary email address for account identification
  * You can switch between different Fireworks accounts by changing your LinkedIn primary email
  * See our [LinkedIn authentication FAQ](/faq-new/account-access/what-email-does-linkedin-authentication-use) for detailed instructions on managing email addresses
</Update>

<Update label="2025-06-30">
  ## Support for GitHub authentication

  You can now log in to Fireworks using your GitHub account. This is useful if
  you already have a GitHub account and want to use it to log in to Fireworks.

  To log in with GitHub, go to the [Fireworks login
  page](https://fireworks.ai/login) and click the "Continue with GitHub"
  button.

  You can also log in with GitHub from the CLI using the `firectl login`
  command.

  ## 🚨 Document Inlining Deprecation

  Document Inlining has been deprecated and is no longer available on the Fireworks platform. This feature allowed LLMs to process images and PDFs through the chat completions API by appending `#transform=inline` to document URLs.

  **Migration recommendations:**

  * For image processing: Use Vision Language Models (VLMs) like [Qwen2.5-VL 32B Instruct](https://app.fireworks.ai/models/fireworks/qwen2p5-vl-32b-instruct)
  * For PDF processing: Use dedicated PDF processing libraries combined with text-based LLMs
  * For structured extraction: Leverage our [structured responses](/structured-responses/structured-response-formatting) capabilities

  For assistance with migration, please contact our support team or visit our [Discord community](https://discord.gg/fireworks-ai).
</Update>

<Update label="2025-06-24">
  ## 🎯 Build SDK: Reward-kit integration for evaluator development

  The Build SDK now natively integrates with [reward-kit](https://github.com/fw-ai-external/reward-kit) to simplify evaluator development for [Reinforcement Fine-Tuning (RFT)](/fine-tuning/reinforcement-fine-tuning-models). You can now create custom evaluators in Python with automatic dependency management and seamless deployment to Fireworks infrastructure.

  **Key features:**

  * Native reward-kit integration for evaluator development
  * Automatic packaging of dependencies from `pyproject.toml` or `requirements.txt`
  * Local testing capabilities before deployment
  * Direct integration with Fireworks datasets and evaluation jobs
  * Support for third-party libraries and complex evaluation logic

  See our [Developing Evaluators](/tools-sdks/python-client/developing-evaluators) guide to get started with your first evaluator in minutes.

  ## Added new Responses API for advanced conversational workflows and integrations

  * Continue conversations across multiple turns using the `previous_response_id` parameter to maintain context without resending full history
  * Stream responses in real time as they are generated for responsive applications
  * Control response storage with the `store` parameter—choose whether responses are retrievable by ID or ephemeral

  See the [Response API guide](/guides/response-api) for usage examples and details.
</Update>

<Update label="2025-06-13">
  ## Supervised Fine-Tuning V2

  Supervised Fine-Tuning V2 released.

  **Key features:**

  * Supports Qwen 2/2.5/3 series, Phi 4, Gemma 3, the Llama 3 family, Deepseek V2, V3, R1
  * Longer context window up to full context length of the supported models
  * Multi-turn function calling fine-tuning
  * Quantization aware training

  More details in the [blogpost](https://fireworks.ai/blog/supervised-finetuning-v2).

  ## Reinforcement Fine-Tuning (RFT)

  Reinforcement Fine-Tuning released. Train expert models to surpass closed source frontier models through verifiable reward. More details in [blospost](https://fireworks.ai/blog/reinforcement-fine-tuning-models).
</Update>

<Update label="2025-05-20">
  ## Diarization and batch processing support added to audio inference

  See our [blog post](https://fireworks.ai/blog/audio-summer-updates-and-new-features) for details.
</Update>

<Update label="2025-05-19">
  ## 🚀 Easier & faster LoRA fine-tune deployments on Fireworks

  You can now deploy a LoRA fine-tune with a single command and get speeds that approximately match the base model:

  ```bash  theme={null}
  firectl create deployment "accounts/fireworks/models/<MODEL_ID of lora model>"
  ```

  Previously, this involved two distinct steps, and the resulting deployment was slower than the base model:

  1. Create a deployment using `firectl create deployment "accounts/fireworks/models/<MODEL_ID of base model>" --enable-addons`
  2. Then deploy the addon to the deployment: `firectl load-lora <MODEL_ID> --deployment <DEPLOYMENT_ID>`

  For more information, see our [deployment documentation](https://docs.fireworks.ai/models/deploying#deploying-to-on-demand).

  <Note>
    This change is for dedicated deployments with a single LoRA. You can still deploy multiple LoRAs on a deployment or deploy LoRA(s) on some Serverless models as described in the documentation.
  </Note>
</Update>



---

**Navigation:** [← Previous](./06-text-models.md) | [Index](./index.md) | Next →
