**Navigation:** [← Previous](./04-7-report-results.md) | [Index](./index.md) | [Next →](./06-text-models.md)

---

# SVG Drawing Agent
Source: https://docs.fireworks.ai/fine-tuning/quickstart-svg-agent

Train an agent that creates SVG drawings using tools

In the previous guide, we cover doing RFT on a simple math example running locally. In this guide, we'll show you how you can run RFT in your production environment with a remote rollout server, by walking through fine-tuning for an image (SVG) generation agent.

Watch a quick walkthrough:

<Frame>
  <iframe src="https://www.loom.com/embed/24ba433601de45ba8b63d9fb34c31fd5" width="100%" height="420" frameBorder="0" allow="autoplay; fullscreen" allowFullScreen />
</Frame>

## What You'll Learn

* **Apply RFT to production agents** — Train models that work with remote servers and existing infrastructure
* **Remote rollout processing** — Connect your production environment to Fireworks RFT using Eval Protocol
* **Monitor and debug training** — Track progress, inspect rollouts, and debug issues with live logs

## 1. Installation

1. **Clone the quickstart repo**: [https://github.com/eval-protocol/quickstart](https://github.com/eval-protocol/quickstart)

```bash  theme={null}
git clone git@github.com:eval-protocol/quickstart.git
cd quickstart
```

2. **Install Eval Protocol**:

```bash  theme={null}
pip install "eval-protocol[svgbench]"
```

3. **Environment Setup**:

Make a copy of `env.example`, name it `.env`, and fill in the keys:

```
FIREWORKS_API_KEY=your-fireworks-key-here
OPENAI_API_KEY=your-openai-key-here
```

Place this file in your evaluator directory (e.g., `evaluator/.env`). The create process below automatically reads and uploads these secrets to Fireworks.

## 2. Test your evaluator locally

Test your evaluator locally before launching training, to verify everything works with your rollout processor.

**Terminal 1** - Start the local UI server to view results:

```bash  theme={null}
ep logs
```

**Terminal 2** - Kick off the test:

```bash  theme={null}
pytest evaluator/test_svgagent.py -vs
```

The test automatically uses our Vercel remote server:

```
rollout_processor=RemoteRolloutProcessor(
    remote_base_url="https://vercel-svg-server-ts.vercel.app",
)
```

If you want to use a local development Vercel server instead, see [Local Development Server](#local-development-server).

### Expected Test Output

The test should automatically open a browser page to view results. If it doesn't, navigate to [http://localhost:8000](http://localhost:8000).

```
INFO:eval_protocol.pytest.remote_rollout_processor:Found status log for rollout democratic-way-12: Rollout democratic-way-12 completed
INFO:eval_protocol.pytest.remote_rollout_processor:Found Fireworks log for rollout democratic-way-12 with status code 100.0
INFO:eval_protocol.adapters.fireworks_tracing:Successfully converted 1 traces to evaluation rows | 3/8 [00:19<00:22, 4.52s/rollout]
...
Runs (Parallel): 100%|████████████████████████████████████████████| 1/1 [00:31<00:00, 31.07s/run]
PASSED
```

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e77097c700e374bdf7e7cafbe867eacb" alt="Eval Protocol Logs Interface" data-og-width="1273" width="1273" data-og-height="716" height="716" data-path="images/ep_logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=d9929ea24b65066e9b49db7a1cc01735 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e65c345b1cc114b86cc482c0b049595f 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=a9ff29184be84502944bef0fec9e3c78 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=fc6db5a4b499f5039bf5625f8293e2c2 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=3346acbf2a9428562371dc2f5500c58e 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=d38c0c8c66935f754ff97757dd1b90e1 2500w" />

If you're interested in understanding how Remote Rollout Processing works and how it communicates with the remote server, see [How Remote Rollout Processing Works](#how-remote-rollout-processing-works).

## 3. Start training with a single command

To kickoff training, simply do:

```bash  theme={null}
cd evaluator
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b
```

This command:

1. Uploads secrets — reads your `.env` and uploads API keys as Fireworks secrets
2. Uploads evaluator — packages and uploads your evaluation code
3. Waits for build — polls evaluator status until ACTIVE (timeout: 10 minutes)
4. Creates dataset — uploads your `svgbench_dataset.jsonl`
5. Launches RFT job — starts reinforcement fine-tuning with your evaluator

### Configuration & Troubleshooting

**Training Parameters**: We use Eval Protocol's default values for training parameters (batch size, epochs, learning rate, LoRA rank, accelerator count, etc.). For a complete list of available RFT flags you can customize, see [Fireworks RFT Command Documentation](https://docs.fireworks.ai/tools-sdks/firectl/commands/create-reinforcement-fine-tuning-job).

**Changing Evaluators**: If you've made changes to your evaluator code and want to upload a new version:

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --force
```

**Evaluator Upload Timing Out**: If your evaluator takes longer than 10 minutes to build, you'll see:

```
⏰ Timeout after 10.0m - evaluator is not yet ACTIVE

❌ Evaluator is not ready within the timeout period.
📊 Please check the evaluator status at: https://app.fireworks.ai/dashboard/evaluators/test-svgagent-test-svg-generation-evaluation
   Wait for it to become ACTIVE, then run 'eval-protocol create rft' again.
```

In this case, monitor the evaluator upload at the link, and run the command again when ACTIVE.

## 4. Monitor Training Progress

After successful job creation, you'll see:

```
✅ Created Reinforcement Fine-tuning Job
   name: accounts/pyroworks/reinforcementFineTuningJobs/sdnld4yn

📊 Dashboard Links:
   Evaluator: https://app.fireworks.ai/dashboard/evaluators/test-svgagent-test-svg-generation-evaluation
   Dataset:   https://app.fireworks.ai/dashboard/datasets/svgbench-dataset
   RFT Job:   https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/sdnld4yn
```

Click on the **RFT Job** link to view real-time training progress, epoch counts, and rollout data.

### Training Results

After successful training, you should see performance improvements reflected in the training metrics:

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=049359a9ff673f1ebbe79870bebc646e" alt="SVG Agent Training Progress" data-og-width="1145" width="1145" data-og-height="727" height="727" data-path="images/graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c134ea53f61e553faed64f894fbd0968 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=33b9a24999f60e61c13de78a55e3825a 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=029ff347c5522122c86cdc6e5f98036b 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e8920443c785f7a525342f33a80183fd 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=5d4544e02181f10132840bb4c748d38f 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=b064462ba16e5906472fe66a7c4b5b98 2500w" />

### SVG Quality Improvement

You can inspect individual rollouts to see the dramatic improvement in SVG generation quality. Below is a comparison between the first epoch and the final 8th epoch:

**Before (1st Epoch):**
<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=7160c0606439b6a7c5bc851d207975f7" alt="SVG Generation - Before Training" data-og-width="1606" width="1606" data-og-height="1136" height="1136" data-path="images/before.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c3dc3ebfa621ef702648f84c4ebe2657 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=48d46aad8b93acc9e9eb40c42137d6b7 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=94f322bcf6fd77d3709ae6cebd4e9f5f 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=03476db9954ce10c5179f934f235d60c 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=328e7e71e39095a6c868bb1cc40f4c19 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=5088edd903f4c0d3c71c18e6ff70c74b 2500w" />

**After (8th Epoch):**
<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=4d99b24ddb6cd458f35f2b4b00fd8646" alt="SVG Generation - After Training" data-og-width="2030" width="2030" data-og-height="1134" height="1134" data-path="images/after.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=1679375e0cf298aee49b0d0b666ca55e 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=f8ec41ee5416fdecf791041e61fe197d 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=622917132d20de1c72529156353d4cbe 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c6d98d80618948496ec32998486c4564 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=29b3e697b5b9667255a04a6ede7e6c06 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=02b71ab52b92f08ef90eade45d365361 2500w" />

The reinforcement fine tuning process significantly improves the model's ability to generate accurate, detailed SVG graphics that better match the input descriptions.

## Debugging Tips

When your training is running, you have several powerful tools to debug and monitor your rollouts:

### Rollout Overview

Clicking on any **Epoch** or **Step** in the training dashboard, then clicking the **table icon** to the right, will show you a comprehensive table of all rollouts. It's a good high-level overview to see if any rollouts failed and for what reason.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=4e6dda85703f77bcce58b83a391e0f2d" alt="Rollout Overview Table" data-og-width="981" width="981" data-og-height="824" height="824" data-path="images/rollouts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=0a39037d8e3818f7ffe5dd311c210b74 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=2bbe1b8c9b5ade0376fa8363fe8d5ec2 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=54cf4174612678513d44af4afb7a4387 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=ec2e71a16032151cbb3f0c647f16a94f 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=f9cd11af326b4329adf16993bb1a970e 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=94ab07e54df7e21f8f2b9cf216c3d961 2500w" />

### Individual Rollout Details

If you click on a specific row in the rollout table, you can see exactly what the prompt was and how the model responded. You can even copy and paste out the SVG code generated and render it yourself to see what the model did. This is how we got the results above in the before and after comparison.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=0f1384d546a1d5f5f2e85cef97242265" alt="Individual Rollout Details" data-og-width="1497" width="1497" data-og-height="958" height="958" data-path="images/rollout_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c38dbe0ea185fc439889ec216b4d7d89 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=20831b5ff6710155343ec26a519c69cd 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=6de20cd4112cc11966b92792eb9d38f6 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e7fc0f01da318743bd0d0d47539ef9c9 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=082a3a517842f905b4b002ec6898c22d 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=237f8903eefb31bb1f66937cf2979769 2500w" />

### Live Log Streaming

Clicking on **View Logs** takes you to a page of logs being streamed in. Here, you can see precisely what errors are happening to the rollouts. This is useful to debug and fix any issues with your rollouts.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=66aed2a6eac9532a37f0106c0f5a526a" alt="Live Log Streaming" data-og-width="1399" width="1399" data-og-height="958" height="958" data-path="images/logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=9b5d411a6c5810f975952bda32990a74 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=3b1067074975220120cf884e2fe4e04e 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=990e0d1a4815818d085cfe6e8319185c 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=a6f64807089b7221495cbac2e8eeea5a 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=658c42b53a98ce57d8746106ec2b7b03 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=b726b75b643b3837231aa5e4c3cf795c 2500w" />

## Contact Us / Learn More

* [Discord Server](https://discord.gg/mMqQxvFD9A). Come talk to us in the #eval-protocol channel!
* [Eval Protocol Documentation](https://evalprotocol.io/introduction)
* [Remote Rollout Processor Tutorial](https://evalprotocol.io/tutorial/remote-rollout-processor)
* [SVGBench Dataset](https://github.com/johnbean393/SVGBench) - The original benchmark this project is based on
* [Fireworks AI Platform](https://fireworks.ai)

## Appendix

### How Remote Rollout Processing Works

Eval Protocol enables **reinforcement learning that meets you where you are**. Instead of forcing you to rewrite your agent in a specific framework, you can implement a lightweight remote server wherever your codebase and infrastructure already live.

Your remote server is only responsible for:

* **Executing rollouts** - Run your agent logic (in this case, SVG generation from text prompts)
* **Logging to tracing** - Send structured logs to `tracing.fireworks.ai` for evaluation (see the below linked docs for more information)

In this example, we showcase a **Vercel TypeScript server** that executes single-turn SVG code generation.

> **📖 Learn More**: For a complete deep-dive into Remote Rollout Processing, see the [Remote Rollout Processor Tutorial](https://evalprotocol.io/tutorial/remote-rollout-processor).

### Local Development Server

```bash  theme={null}
cd vercel_svg_server_ts
vercel dev
```

Then swap out the `remote_base_url` to point to the local server you just started:

```
rollout_processor=RemoteRolloutProcessor(
    remote_base_url="http://localhost:3000",
)
```

And in a third terminal, run the evaluation:

```bash  theme={null}
pytest evaluator/test_svgagent.py -vs
```

> See [Vercel CLI documentation](https://vercel.com/docs/cli/dev) for more information on local development.


# Overview
Source: https://docs.fireworks.ai/fine-tuning/reinforcement-fine-tuning-models

Learn what reinforcement fine-tuning is, and when to use it to improve your models

## What is Fireworks RFT

Fireworks RFT is a **managed service for reinforcement fine-tuning** that makes it simple for developers to train frontier models like DeepSeek V3 and Kimi K2 for multi-turn agents—achieving SOTA quality at a fraction of the cost.

Instead of spending months building RL infrastructure, go from **local evaluator to production in hours**.

<Frame>
  <img src="https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=63c0700dd20f80798e8a9dea6cfd6146" alt="Fireworks RFT training dashboard showing score progression and configuration" data-og-width="2766" width="2766" data-og-height="2050" height="2050" data-path="images/fine-tuning/rft-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?w=280&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=817947f41306a535ed228f59819e59e7 280w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?w=560&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=ebb8bcdadc56740d5e537c9a9110d09c 560w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?w=840&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=93d6b85701ca5b408c33cb6a0c7288a1 840w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?w=1100&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=a3666b9975b36dd9663e5581f1770e97 1100w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?w=1650&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=cb3dacf1aae71061c0a6930a85b6bc93 1650w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/rft-ui.png?w=2500&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=1bf5adaea852915bb2ffd12c4ac1b11b 2500w" />
</Frame>

## Why train with Fireworks

### No infrastructure management

Fireworks provides managed fine-tuning, making it easy for teams to ship fine-tuned models without infra or RL expertise:

* Train frontier models like DeepSeek V3 or Kimi K2, without managing GPUs or distributed compute
* Leverage your existing evaluation infrastructure to get to production in hours, not weeks
* Deploy with one-click on Fireworks when training completes

### Built for enterprises & production agents

Secure, observable, and production-ready from day one:

* Native support for multi-turn agents with tool-calling and complex reasoning
* Built-in observability and tracing for every agent interaction
* Flexible deployment: fully managed, hybrid (remote evaluator), or VPC with data isolation
* Encrypted data in transit and at rest (SOC 2, GDPR-ready)

## What you'll need

Before getting started with RFT, make sure you have:

* **A Fireworks account** with some credit for training
* **Prompts/examples** you are interested in evaluating in JSONL format
* **Evaluation logic** to score model outputs (can be simple like exact match or complex like code execution)

## Next steps

<CardGroup cols={2}>
  <Card title="Quickstart: Math solver" icon="calculator" href="/fine-tuning/quickstart-math">
    Walk through an example with a simple math solver
  </Card>

  <Card title="How RFT works" icon="book" href="/fine-tuning/how-rft-works">
    Understand the fundamentals behind RFT
  </Card>
</CardGroup>


# Parameters Reference
Source: https://docs.fireworks.ai/fine-tuning/rft-parameters-reference

Quick lookup for all RFT training and rollout parameters

Quick reference for all reinforcement fine-tuning parameters. Most experiments converge with the defaults below. Change them only when you have a clear hypothesis.

<Tip>
  For guidance on **when to change** these parameters, see the [Parameter Tuning guide](/fine-tuning/parameter-tuning).
</Tip>

## Training parameters

| Flag                   | Default         | Valid range                 | When to change                                                                                                        |
| ---------------------- | --------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--epochs`             | **1**           | 1 – 10 (whole numbers only) | Add 1-2 more passes if the reward still climbs steadily near the end of training. Too many epochs risks over-fitting. |
| `--batch-size`         | **32 k tokens** | Hardware-bounded            | Lower if you hit OOM; raise only when GPUs have >30 % headroom.                                                       |
| `--learning-rate`      | **1 e-4**       | 1 e-5 – 5 e-4               | Decrease when the reward spikes then collapses; increase when the curve plateaus too early.                           |
| `--lora-rank`          | **8**           | 4 – 128 (powers of 2)       | Higher ranks give more capacity but require more GPU memory; stay ≤64 unless you have high-end GPUs.                  |
| `--max-context-length` | **8192 tokens** | Up to model limit           | Raise only when your prompts truncate; remember longer sequences consume quadratic compute.                           |

### Example usage

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model my-rft-model \
  --epochs 3 \
  --learning-rate 1e-4 \
  --lora-rank 16 \
  --max-context-length 16384
```

## Rollout (sampling) parameters

During each training step, the model generates multiple responses with stochastic decoding. These parameters control that generation process.

| Field           | CLI flag                  | Default   | Recommended range      | Why it matters                                                                                            |
| --------------- | ------------------------- | --------- | ---------------------- | --------------------------------------------------------------------------------------------------------- |
| Maximum tokens  | `--inference-max-tokens`  | **2 048** | 16 – 16 384            | Longer responses improve reward on summarisation / story tasks but add cost.                              |
| Temperature     | `--inference-temperature` | **0.7**   | 0.1 – 2.0 ( > 0 only ) | Values below 0.1 converge towards greedy decoding and kill exploration; 0.5–1.0 is a sweet spot for RLHF. |
| Top-p           | `--inference-top-p`       | **1.0**   | 0 – 1                  | Lower to 0.2–0.5 to clamp long-tail tokens when the reward penalises hallucinations.                      |
| Top-k           | `--inference-top-k`       | **40**    | 0 – 100 (0 = off)      | Combine with `temperature` for more creative exploration; keep ≤50 for latency.                           |
| *n* (choices)   | `--inference-n`           | **4**     | 2 – 8                  | Policy-Optimization needs multiple candidates to compute a meaningful KL term; ≥2 is mandatory.           |
| Extra body JSON | `--inference-extra-body`  | *empty*   | valid JSON             | Pass extra OpenAI-style params (e.g., `stop`, `logit_bias`). Invalid JSON is rejected.                    |

### Example usage

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model my-model \
  --inference-max-tokens 1024 \
  --inference-temperature 0.8 \
  --inference-top-p 0.9 \
  --inference-top-k 40 \
  --inference-n 6 \
  --inference-extra-body '{"stop":["\n\n"]}'
```

## Quick reference by goal

| Goal                   | Parameters to adjust                           |
| ---------------------- | ---------------------------------------------- |
| **Faster convergence** | ↑ `epochs`, tune `learning-rate` \< 2× default |
| **Safer / less toxic** | ↓ `temperature`, `top_p`, `top_k`              |
| **More creative**      | `temperature` ≈ 1 – 1.2, `top_p` 0.9           |
| **Cheaper roll-outs**  | ↓ `n`, `max_tokens`, batch size                |
| **Higher capacity**    | ↑ `lora-rank`, but monitor memory usage        |

## Important constraints

### Temperature must be > 0

Greedy sampling (temperature 0) is deterministic and collapses exploration, often leading to mode-dropping and repetitive text.

### At least 2 rollouts required

Policy optimization needs multiple candidates per prompt to compute a meaningful KL divergence term. Setting `--inference-n 1` will fail.

### Range enforcement

The UI and CLI enforce the ranges shown above. Out-of-bound values throw an *Invalid rollout parameters* error immediately, saving wasted GPU hours.

## Next steps

<CardGroup cols={2}>
  <Card title="Parameter tuning guide" icon="sliders" href="/fine-tuning/parameter-tuning">
    Learn strategies for when and how to adjust parameters
  </Card>

  <Card title="Launch training" icon="rocket" href="/fine-tuning/rft-training">
    Start your RFT job with your chosen parameters
  </Card>

  <Card title="GSM8K Quickstart" icon="graduation-cap" href="/fine-tuning/quickstart-math">
    Hands-on tutorial for RFT training
  </Card>

  <Card title="RFT Overview" icon="book-open" href="/fine-tuning/reinforcement-fine-tuning-models">
    Learn about the RFT training process
  </Card>
</CardGroup>


# Training
Source: https://docs.fireworks.ai/fine-tuning/rft-training

Start your RFT job via CLI or UI

<Note>
  🚧 **Coming Soon** - This page is under construction
</Note>

## Prerequisites

Placeholder: Before launching an RFT job, ensure you have:

* Dataset uploaded to Fireworks
* Evaluator uploaded via Eval Protocol
* Fireworks API key configured
* Sufficient GPU quota

## Option A: CLI with Eval Protocol

Placeholder: Complete guide to launching via command line

### Step 1: Install Eval Protocol CLI

Placeholder: Installation instructions

```bash  theme={null}
pip install eval-protocol
```

### Step 2: Authenticate

Placeholder: How to set up API credentials

### Step 3: Upload Evaluator

Placeholder: Command to upload your evaluator

```bash  theme={null}
eval-protocol upload --entry "module::function"
```

**Example**: Placeholder: Concrete example with real module name

### Step 4: Create RFT Job

Placeholder: Full command with all options explained

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --dataset-id DATASET_ID \
  --evaluator-id EVALUATOR_ID \
  --output-model my-finetuned-model \
  --epochs 1 \
  --learning-rate 1e-4 \
  --inference-temperature 0.7 \
  --inference-n 4
```

### Step 5: Verify Job Created

Placeholder: How to check job status

```bash  theme={null}
eval-protocol list rft
```

## Option B: Web UI

Placeholder: Complete guide to launching via dashboard

### Step 1: Navigate to Fine-Tuning

Placeholder:

1. Go to [Fireworks Dashboard](https://app.fireworks.ai)
2. Click "Fine-Tuning" in sidebar
3. Click "Fine-tune a Model"

**Screenshot**: Placeholder: Image of fine-tuning page

### Step 2: Select Reinforcement Method

Placeholder:

* Choose "Reinforcement" as tuning method
* Select base model from dropdown

**Screenshot**: Placeholder: Image showing method selection

### Step 3: Configure Dataset

Placeholder:

* Upload new dataset or select existing
* Preview dataset entries
* Verify format

**Screenshot**: Placeholder: Image of dataset selection

### Step 4: Select Evaluator

Placeholder:

* Choose from uploaded evaluators
* Preview evaluator code
* Test on sample data

**Screenshot**: Placeholder: Image of evaluator selection

### Step 5: Set Training Parameters

Placeholder: Form showing all parameters with descriptions:

* Base model
* Output model name
* Epochs
* Learning rate
* LoRA rank
* Max context length
* Batch size

**Screenshot**: Placeholder: Image of parameter form

### Step 6: Configure Rollout Parameters

Placeholder: Form for inference settings:

* Temperature
* Top-p
* Top-k
* Number of rollouts (n)
* Max tokens

**Screenshot**: Placeholder: Image of rollout settings

### Step 7: Review and Launch

Placeholder:

* Review all settings
* Estimated cost/time
* Click "Start Fine-Tuning"

**Screenshot**: Placeholder: Image of review page

## Using `firectl` CLI (Alternative)

Placeholder: For users who prefer firectl over eval-protocol

```bash  theme={null}
firectl create rftj \
  --base-model llama-v3p1-8b-instruct \
  --dataset my-dataset \
  --evaluator my-evaluator \
  --output-model my-model
```

## Comparing CLI vs UI

Placeholder: Table showing:

| Feature             | CLI (eval-protocol) | UI              | firectl   |
| ------------------- | ------------------- | --------------- | --------- |
| Speed               | Fast                | Slower          | Fast      |
| Automation          | Easy                | Manual          | Easy      |
| Parameter discovery | Harder              | Easier          | Medium    |
| Reproducibility     | Excellent           | Manual tracking | Excellent |

## Advanced Configuration

Placeholder: Less common options:

* Custom GPU requirements
* Environment URLs for multi-turn
* Checkpoint frequency
* W\&B integration

## Job Validation

Placeholder: How Fireworks validates your job before starting:

* Dataset format check
* Evaluator syntax check
* Resource availability
* Quota limits

## Common Errors and Fixes

Placeholder: Error messages you might see:

* "Invalid dataset format" → Fix dataset JSONL
* "Evaluator not found" → Re-upload evaluator
* "Insufficient quota" → Request more GPUs
* "Invalid parameter range" → Check parameter bounds

## After Launching

Placeholder: What happens next:

1. Job enters queue
2. Resources allocated
3. Training starts
4. You can monitor progress

## Next Steps

Placeholder: Link to monitoring guide to track your job


# Secure Fine Tuning
Source: https://docs.fireworks.ai/fine-tuning/secure-fine-tuning

Fine-tune models while keeping sensitive data and components under your control

Fireworks enables secure model fine-tuning while maintaining customer control over sensitive components and data. Use your own cloud storage, keep reward functions proprietary, and ensure training data never persists on our platform beyond active workflows.

## Secure reinforcement fine-tuning (RFT)

Use reinforcement fine-tuning while keeping sensitive components and data under your control. Follow these steps to run secure RFT end to end using your own storage and reward pipeline.

<Steps>
  <Step title="Configure storage (BYOB)">
    Point Fireworks to your storage so you retain governance and apply your own compliance controls.

    * Datasets: [GCS Bucket Integration](#gcs-bucket-integration) (AWS S3 coming soon)
    * Models (optional): [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model)

    <Tip>
      Grant least-privilege IAM to only the bucket/path prefixes needed for training. Use server-side encryption and your KMS policies where required.
    </Tip>
  </Step>

  <Step title="Prepare your reward pipeline and rollouts">
    Keep your reward functions, rollout servers, and training metrics under your control. Generate rewards from your environment and write them to examples in your dataset (or export a dataset that contains per-example rewards).

    * Reward functions and reward models remain proprietary and never need to be shared
    * Rollouts and evaluation infrastructure run in your environment
    * Model checkpoints can be registered to your storage registry if desired
  </Step>

  <Step title="Create a dataset that includes rewards">
    Create or point a `Dataset` at your BYOB storage. Ensure each example contains the information required by your reward pipeline (for example, prompts, outputs/trajectories, and numeric rewards).

    <Info>
      You can reuse existing supervised data by attaching reward signals produced by your pipeline, or export a fresh dataset into your bucket for consumption by RFT.
    </Info>
  </Step>

  <Step title="Run reinforcement step from Python">
    Use the Python SDK to run reinforcement steps that read from your BYOB dataset and produce a new checkpoint.

    ```python  theme={null}
    # Assumes you have an authenticated `llm` client and a `dataset` that
    # references your BYOB bucket with per-example rewards.
    import time

    job = llm.reinforcement_step(
        dataset=dataset,                 # Dataset with rewards in your bucket
        output_model="my-improved-model-v1",  # New checkpoint name (must not exist)
        epochs=1,
        learning_rate=1e-5,
        accelerator_count=2,
        accelerator_type="NVIDIA_H100_80GB",
    )

    # Wait for completion
    while not job.is_completed:
        job.raise_if_bad_state()
        time.sleep(1)
        job = job.get()
        if job is None:
            raise RuntimeError("Job was deleted while waiting for completion")

    # The new model is now available at job.output_model
    ```

    See [`LLM.reinforcement_step()`](/tools-sdks/python-client/sdk-reference#reinforcement-step) and [`ReinforcementStep`](/tools-sdks/python-client/sdk-reference#reinforcementstep) for full parameters and return types.

    <Note>
      When continuing from a LoRA checkpoint, training parameters such as `lora_rank`, `learning_rate`, `max_context_length`, `epochs`, and `batch_size` must match the original LoRA training.
    </Note>
  </Step>

  <Step title="Verify outputs and enforce controls">
    * Validate the new checkpoint functions as expected in your environment
    * If exporting models to your storage, apply your registry policies and access reviews
    * Review audit logs and rotate any temporary credentials used for the run
  </Step>
</Steps>

<Warning>
  Do not store long-lived credentials in code. Use short-lived tokens, workload identity, or scoped service accounts when granting Fireworks access to your buckets.
</Warning>

<Check>
  You now have an end-to-end secure RFT workflow with BYOB datasets, proprietary reward pipelines, and isolated training jobs that generate new checkpoints.
</Check>

## GCS Bucket Integration

Use external Google Cloud Storage (GCS) buckets for fine-tuning while keeping your data private. Fireworks creates proxy datasets that reference your external buckets—data is only accessed during fine-tuning within a secure, isolated cluster.

<Info>
  Your data never leaves your GCS bucket except during fine-tuning, ensuring maximum privacy and security.
</Info>

### Required Permissions

You need to grant access to three service accounts:

#### Fireworks Control Plane

* **Account**: `fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com`
* **Required role**: Custom role with `storage.buckets.getIamPolicy` permission

<CodeGroup>
  ```bash Setup command theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=projects/<YOUR_PROJECT>/roles/<YOUR_CUSTOM_ROLE>
  ```
</CodeGroup>

This service account will be used to retrieve the IAM Policy set on the bucket, so that we are able to perform bucket ownership verifications and access verifications during dataset creation.

#### Inference Service Account

* **Account**: `inference@fw-ai-cp-prod.iam.gserviceaccount.com`
* **Required role**: Storage Object Viewer or Storage Object Admin

<CodeGroup>
  ```bash Storage Object Viewer theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=roles/storage.objectViewer
  ```

  ```bash Storage Object Admin theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=roles/storage.objectAdmin
  ```
</CodeGroup>

This service account will be used to access the files in the bucket.

#### Your Company's Fireworks Service Account

* **Account**: Your company's Fireworks account registration email
* **Required role**: Storage Object Viewer or Storage Object Admin

<CodeGroup>
  ```bash Storage Object Viewer theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
    --role=roles/storage.objectViewer
  ```

  ```bash Storage Object Admin theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
    --role=roles/storage.objectAdmin
  ```
</CodeGroup>

This is used to validate that your account actually has access to the bucket that you are trying to reference the dataset from. The email associated with your account (not the email of the user, but the account itself, you can get it with `firectl get account`) must have at least read access to the bucket listed under the bucket access IAM policy.

### Usage Example

<Steps>
  <Step title="Create a Proxy Dataset">
    Create a dataset that references your external GCS bucket:

    ```bash  theme={null}
    firectl create dataset {DATASET_NAME} --external-url gs://bucket-name/object-name
    ```

    <Tip>
      Ensure your gsutil path points directly to the JSONL file. If the file is in a folder, make sure the folder contains only the intended file.
    </Tip>
  </Step>

  <Step title="Start Fine-tuning">
    Use the proxy dataset to create a fine-tuning job:

    ```bash  theme={null}
    firectl create sftj \
      --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
      --base-model "accounts/fireworks/models/{MODEL}" \
      --output-model {TRAINED_MODEL_NAME}
    ```

    <Check>
      For additional options, run: `firectl create sftj -h`
    </Check>
  </Step>
</Steps>

### Key Benefits

<CardGroup cols={3}>
  <Card title="Data Privacy" icon="shield">
    Your data never leaves your GCS bucket except during fine-tuning
  </Card>

  <Card title="Security" icon="lock">
    Access is limited to isolated fine-tuning clusters
  </Card>

  <Card title="Simplicity" icon="circle">
    Reference external data without copying or moving files
  </Card>
</CardGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Data Security Overview" href="/guides/security_compliance/data_security" icon="shield-check">
    Learn about our comprehensive security measures
  </Card>

  <Card title="Reinforcement Fine Tuning" href="/fine-tuning/reinforcement-fine-tuning-models" icon="brain">
    Full guide to reinforcement fine-tuning
  </Card>
</CardGroup>


# Concepts
Source: https://docs.fireworks.ai/getting-started/concepts

This document outlines basic Fireworks AI concepts.

## Resources

### Account

Your account is the top-level resource under which other resources are located. Quotas and billing are enforced at the account level, so usage for all users in an account contribute to the same quotas and bill.

* For developer accounts, the account ID is auto-generated from the email address used to sign up.
* Enterprise accounts can optionally choose a custom, unique account ID.

### User

A user is an email address associated with an account. Users added to an account have full access to delete, edit, and create resources within the account, such as deployments and models.

### Models and model types

A model is a set of model weights and metadata associated with the model. Each model has a [**globally unique name**](/getting-started/concepts#resource-names-and-ids) of the form `accounts/<ACCOUNT_ID>/models/<MODEL_ID>`. There are two types of models:

**Base models:** A base model consists of the full set of model weights, including models pre-trained from scratch and full fine-tunes.

* Fireworks has a library of common base models that can be used for [**serverless inference**](/models/overview#serverless-inference) as well as [**dedicated deployments**](/models/overview#dedicated-deployments). Model IDs for these models are pre-populated. For example, `llama-v3p1-70b-instruct` is the model ID for the Llama 3.1 70B model that Fireworks provides. The ID for each model can be found on its page ([**example**](https://app.fireworks.ai/models/fireworks/qwen3-coder-480b-a35b-instruct))
* Users can also [upload their own](/models/uploading-custom-models) custom base models and specify model IDs.

**LoRA (low-rank adaptation) addons:** A LoRA addon is a small, fine-tuned model that significantly reduces the amount of memory required to deploy compared to a fully fine-tuned model. Fireworks supports [**training**](/fine-tuning/finetuning-intro), [**uploading**](/models/uploading-custom-models#importing-fine-tuned-models), and [**serving**](/fine-tuning/fine-tuning-models#deploying-a-fine-tuned-model) LoRA addons. LoRA addons must be deployed on a serverless or dedicated deployment for its corresponding base model. Model IDs for LoRAs can be either auto-generated or user-specified.

### Deployments and deployment types

A model must be deployed before it can be used for inference. A deployment is a collection (one or more) model servers that host one base model and optionally one or more LoRA addons.

Fireworks supports two types of deployments:

* **Serverless deployments:**  Fireworks hosts popular base models on shared "serverless" deployments. Users pay-per-token to query these models and do not need to configure GPUs. The most popular serverless deployments also support serverless LoRA addons. See our [Quickstart - Serverless](/getting-started/quickstart) guide to get started.
* **Dedicated deployments:** Dedicated deployments enable users to configure private deployments with a wide array of hardware (see [on-demand deployments guide](/guides/ondemand-deployments)). Dedicated deployments give users performance guarantees and the most flexibility and control over what models can be deployed. Both LoRA addons and base models can be deployed to dedicated deployments. Dedicated deployments are billed by a GPU-second basis (see [**pricing**](https://fireworks.ai/pricing#ondemand) page).

See the [**Querying text models guide**](/guides/querying-text-models) for a comprehensive overview of making LLM inference.

### Deployed model

Users can specify a model to query for inference using the model name and deployment name. Alternatively, users can refer to a "deployed model" name that refers to a unique instance of a base model or LoRA addon that is loaded into a deployment. See [On-demand deployments](/guides/ondemand-deployments) guide for more.

### Dataset

A dataset is an immutable set of training examples that can be used to fine-tune a model.

### Fine-tuning job

A fine-tuning job is an offline training job that uses a dataset to train a LoRA addon model.

## Resource names and IDs

A resource name is a globally unique identifier of a resource. The format of a name also identifies the type and hierarchy of the resource, for example:

Resource IDs must satisfy the following constraints:

* Between 1 and 63 characters (inclusive)
* Consists of a-z, 0-9, and hyphen (-)
* Does not begin or end with a hyphen (-)
* Does not begin with a digit

## Control plane and data plane

The Fireworks API can be split into a control plane and a data plane.

* The **control plane** consists of APIs used for managing the lifecycle of resources. This
  includes your account, models, and deployments.
* The **data plane** consists of the APIs used for inference and the backend services that power
  them.

## Interfaces

Users can interact with Fireworks through one of many interfaces:

* The **web app** at [https://app.fireworks.ai](https://app.fireworks.ai)
* The [`firectl`](/tools-sdks/firectl/firectl) CLI
* [OpenAI compatible API](/tools-sdks/openai-compatibility)
* [Python SDK](/tools-sdks/python-client/sdk-introduction)


# Build with Fireworks AI
Source: https://docs.fireworks.ai/getting-started/introduction

Fast inference and fine-tuning for open source models

Fireworks AI is the fastest platform for building with open source AI models. Get production-ready inference and fine-tuning with best-in-class speed, cost and quality.

## Get started in minutes

<CardGroup cols="3">
  <Card title="Start fast with Serverless" href="/getting-started/quickstart" icon="bolt">
    Use popular models instantly with pay-per-token pricing. Perfect for quality vibe testing and prototyping.
  </Card>

  <Card title="Deploy models & autoscale on dedicated GPUs" href="/getting-started/ondemand-quickstart" icon="server">
    Deploy with high performance on dedicated GPUs with fast autoscaling and minimal cold starts. Optimize deployments for speed and throughput.
  </Card>

  <Card title="Fine-tune models for best quality" href="/fine-tuning/finetuning-intro" icon="sliders">
    Boost model quality with supervised and reinforcement fine-tuning of models up to 1T+ parameters. Start training in minutes, deploy immediately.
  </Card>
</CardGroup>

<Tip>
  Not sure where to start? First, pick the right model for your use case with our [**model selection guide**](/guides/recommended-models). Then choose [**Serverless**](/getting-started/quickstart) to prototype quickly, move to [**Deployments**](/getting-started/ondemand-quickstart) to optimize and run production workloads, or use [**Fine-tuning**](/fine-tuning/finetuning-intro) to improve quality.

  Need help optimizing deployments, fine-tuning models, or setting up production infrastructure? [Talk to our team](https://fireworks.ai/company/contact-us) - we'll help you get the best performance and reliability.
</Tip>

## What you can build

<CardGroup cols="3">
  <Card title="100+ Supported Models" href="https://fireworks.ai/models" icon="books">
    Text, vision, audio, image, and embeddings
  </Card>

  <Card title="Migrate from OpenAI" href="/tools-sdks/openai-compatibility" icon="arrow-right-arrow-left">
    Drop-in replacement - just change the base URL
  </Card>

  <Card title="Function Calling" href="/guides/function-calling" icon="function">
    Connect models to tools and APIs
  </Card>

  <Card title="Structured Outputs" href="/structured-responses/structured-response-formatting" icon="brackets-curly">
    Reliable JSON responses for agentic workflows
  </Card>

  <Card title="Vision Models" href="/guides/querying-vision-language-models" icon="eye">
    Analyze images and documents
  </Card>

  <Card title="Speech to Text" href="/api-reference/audio-transcriptions" icon="microphone">
    Real-time or batch audio transcription
  </Card>

  <Card title="Embeddings & Reranking" href="/guides/querying-embeddings-models" icon="vector">
    Use embeddings & reranking in search & context retrieval
  </Card>

  <Card title="Batch Inference" href="/guides/batch-inference" icon="vector">
    Run async inference jobs at scale, faster and cheaper
  </Card>
</CardGroup>

## Resources & help

<CardGroup cols="3">
  <Card title="Which model should I use?" href="/guides/recommended-models" icon="compass">
    Find the best model for your use case
  </Card>

  <Card title="Cookbook" href="https://github.com/fw-ai/cookbook" icon="book-open">
    Code examples and tutorials
  </Card>

  <Card title="API Reference" href="/api-reference/introduction" icon="code">
    Complete API documentation
  </Card>

  <Card title="Discord Community" href="https://discord.gg/fireworks-ai" icon="discord">
    Ask questions and get help from developers
  </Card>

  <Card title="Security & Compliance" href="https://trust.fireworks.ai/" icon="shield-check">
    SOC 2, HIPAA, and audit reports
  </Card>

  <Card title="System Status" href="https://status.fireworks.ai/" icon="signal">
    Check service uptime
  </Card>

  <Card title="Talk to Sales" href="https://fireworks.ai/company/contact-us" icon="building">
    Talk to our team
  </Card>
</CardGroup>


# Deployments Quickstart
Source: https://docs.fireworks.ai/getting-started/ondemand-quickstart

Deploy models on dedicated GPUs in minutes

On-demand deployments are dedicated GPUs that give you better performance, no rate limits, fast autoscaling, and a wider selection of models than serverless. This quickstart will help you spin up your first on-demand deployment in minutes.

## Step 1: Create and export an API key

Before you begin, create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys). Click **Create API key** and store it in a safe location.

Once you have your API key, export it as an environment variable in your terminal:

<Tabs>
  <Tab title="macOS / Linux">
    ```bash  theme={null}
    export FIREWORKS_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell  theme={null}
    setx FIREWORKS_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

## Step 2: Install the CLI

To create and manage on-demand deployments, you'll need the `firectl` CLI tool. Install it using one of the following methods, based on your platform:

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

Then, sign in:

```bash  theme={null}
firectl signin
```

## Step 3: Create a deployment

This command will create a deployment of GPT OSS 120B optimized for speed. It will take a few minutes to complete. The resulting deployment will scale up to 1 replica.

```bash  theme={null}
firectl create deployment accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --min-replica-count 0 \
        --max-replica-count 1 \
        --scale-to-zero-window 5m \
        --wait
```

<Tip>
  `fast` is called a [deployment shape](/guides/ondemand-deployments#deployment-shapes), which is a pre-configured deployment template created by the Fireworks team that sets sensible defaults for most deployment options (such as hardware type).

  You can also pass `throughput` or `cost` to `--deployment-shape`:

  * `throughput` creates a deployment that trades off latency for lower cost-per-token at scale
  * `cost` creates a deployment that trades off latency and throughput for lowest cost-per-token at small scale, usually for early experimentation and prototyping

  While we recommend using a deployment shape, you are also free to pass your own configuration to the deployment via our [deployment options](/guides/ondemand-deployments#deployment-options).
</Tip>

The response will look like this:

```bash  theme={null}
Name: accounts/<YOUR ACCOUNT ID>/deployments/<DEPLOYMENT ID>
Create Time: <CREATION_TIME>
Expire Time: <EXPIRATION_TIME>
Created By: <YOUR EMAIL>
State: CREATING
Status: OK
Min Replica Count: 0
Max Replica Count: 1
Desired Replica Count: 0
Replica Count: 0
Autoscaling Policy:
  Scale Up Window: 30s
  Scale Down Window: 5m0s
  Scale To Zero Window: 5m0s
Base Model: accounts/fireworks/models/gpt-oss-120b
...other fields...
```

Take note of the `Name:` field in the response, as it will be used in the next step to query your deployment.

[Learn more about deployment options→](/guides/ondemand-deployments#deployment-options)

[Learn more about autoscaling options→](/guides/ondemand-deployments#customizing-autoscaling-behavior)

## Step 4: Query your deployment

Now you can query your on-demand deployment using the same API as serverless models, but using your dedicated deployment. Replace `<DEPLOYMENT_NAME>` in the below snippets with the value from the `Name:` field in the previous step:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        messages=[{
            "role": "user",
            "content": "Explain quantum computing in simple terms",
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
      messages: [
        {
          role: "user",
          content: "Explain quantum computing in simple terms",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        "messages": [
          {
            "role": "user",
            "content": "Explain quantum computing in simple terms"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

The examples from the Serverless quickstart will work with this deployment as well, just replace the model string with the deployment-specific model string from above.

[Serverless quickstart→](/getting-started/quickstart)

## Common use cases

### Autoscale based on requests per second

```bash  theme={null}
firectl create deployment accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets requests_per_second=5 \
        --wait
```

### Autoscale based on concurrent requests

```bash  theme={null}
firectl create deployment accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets concurrent_requests=5 \
        --wait
```

## Next steps

Ready to scale to production, explore other modalities, or customize your models?

<CardGroup cols="3">
  <Card title="Upload a custom model" href="/models/uploading-custom-models" icon="server">
    Bring your own model and deploy it on Fireworks
  </Card>

  <Card title="Fine-tune Models" href="/fine-tuning/finetuning-intro" icon="sliders">
    Improve model quality with supervised and reinforcement learning
  </Card>

  <Card title="Speech to Text" href="/api-reference/audio-transcriptions" icon="microphone">
    Real-time or batch audio transcription
  </Card>

  <Card title="Embeddings & Reranking" href="/guides/querying-embeddings-models" icon="brackets-curly">
    Use embeddings & reranking in search & context retrieval
  </Card>

  <Card title="Batch Inference" href="/guides/batch-inference" icon="list-check">
    Run async inference jobs at scale, faster and cheaper
  </Card>

  <Card title="Browse 100+ Models" href="https://fireworks.ai/models" icon="books">
    Explore all available models across modalities
  </Card>

  <Card title="API Reference" href="/api-reference/introduction" icon="code">
    Complete API documentation
  </Card>
</CardGroup>


# Serverless Quickstart
Source: https://docs.fireworks.ai/getting-started/quickstart

Make your first Serverless API call in minutes

Serverless is the fastest way to get started with using open models. This quickstart will help you make your first API call in minutes.

## Step 1: Create and export an API key

Before you begin, create an API key in the [Fireworks dashboard](https://app.fireworks.ai/settings/users/api-keys). Click **Create API key** and store it in a safe location.

Once you have your API key, export it as an environment variable in your terminal:

<Tabs>
  <Tab title="macOS / Linux">
    ```bash  theme={null}
    export FIREWORKS_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell  theme={null}
    setx FIREWORKS_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

## Step 2: Make your first Serverless API call

<Tabs>
  <Tab title="Python">
    Fireworks provides an OpenAI compatible endpoint. Install the OpenAI Python SDK:

    ```bash  theme={null}
    pip install openai
    ```

    Then make your first Serverless API call:

    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{
            "role": "user",
            "content": "Say hello in Spanish",
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    Fireworks provides an OpenAI compatible endpoint. Install the OpenAI Node.js SDK:

    ```bash  theme={null}
    npm install openai
    ```

    Then make your first Serverless API call:

    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [
        {
          role: "user",
          content: "Say hello in Spanish",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
          {
            "role": "user",
            "content": "Say hello in Spanish"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

You should see a response like: `"¡Hola!"`

## Common use cases

### Streaming responses

Stream responses token-by-token for a better user experience:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    stream = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{"role": "user", "content": "Tell me a short story"}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const stream = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [{ role: "user", content: "Tell me a short story" }],
      stream: true,
    });

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "");
    }
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $FIREWORKS_API_KEY" \
        -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
            {
            "role": "user",
            "content": "Tell me a short story"
            }
        ],
        "stream": true
        }'
    ```
  </Tab>
</Tabs>

### Function calling

Connect your models to external tools and APIs:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1",
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2-instruct-0905",
        messages=[{"role": "user", "content": "What's the weather in Paris?"}],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a location",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "City name, e.g. San Francisco",
                            }
                        },
                        "required": ["location"],
                    },
                },
            }
        ],
    )

    print(response.choices[0].message.tool_calls)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const tools = [
      {
        type: "function",
        function: {
          name: "get_weather",
          description: "Get the current weather for a location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "City name, e.g. San Francisco",
              },
            },
            required: ["location"],
          },
        },
      },
    ];

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/kimi-k2-instruct-0905",
      messages: [{ role: "user", content: "What's the weather in Paris?" }],
      tools: tools,
    });

    console.log(response.choices[0].message.tool_calls);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/kimi-k2-instruct-0905",
        "messages": [
          {
            "role": "user",
            "content": "What'\''s the weather in Paris?"
          }
        ],
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "get_weather",
              "description": "Get the current weather for a location",
              "parameters": {
                "type": "object",
                "properties": {
                  "location": {
                    "type": "string",
                    "description": "City name, e.g. San Francisco"
                  }
                },
                "required": ["location"]
              }
            }
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

[Learn more about function calling →](/guides/function-calling)

### Structured outputs (JSON mode)

Get reliable JSON responses that match your schema:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1",
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[
            {
                "role": "user",
                "content": "Extract the name and age from: John is 30 years old",
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "person",
                "schema": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}, "age": {"type": "number"}},
                    "required": ["name", "age"],
                },
            },
        },
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [
        {
          role: "user",
          content: "Extract the name and age from: John is 30 years old",
        },
      ],
      response_format: {
        type: "json_object",
        json_schema: {
          name: "person",
          schema: {
            type: "object",
            properties: {
              name: { type: "string" },
              age: { type: "number" },
            },
            required: ["name", "age"],
          },
        },
      },
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
          {
            "role": "user",
            "content": "Extract the name and age from: John is 30 years old"
          }
        ],
        "response_format": {
          "type": "json_schema",
          "json_schema": {
            "name": "person",
            "schema": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "age": {
                  "type": "number"
                }
              },
              "required": ["name", "age"]
            }
          }
        }
      }'
    ```
  </Tab>
</Tabs>

[Learn more about structured outputs →](/structured-responses/structured-response-formatting)

### Vision models

Analyze images with vision-language models:

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"
                        },
                    },
                ],
            }
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "What's in this image?" },
            {
              type: "image_url",
              image_url: {
                url: "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png",
              },
            },
          ],
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/qwen2p5-vl-32b-instruct",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "What'\''s in this image?"
              },
              {
                "type": "image_url",
                "image_url": {
                  "url": "https://storage.googleapis.com/fireworks-public/image_assets/fireworks-ai-wordmark-color-dark.png"
                }
              }
            ]
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

[Learn more about vision models →](/guides/querying-vision-language-models)

## Serverless model lifecycle

Serverless models are managed by the Fireworks team and may be updated or deprecated as new models are released. We provide **at least 2 weeks advance notice** before removing any model, with longer notice periods for popular models based on usage.

**For production workloads requiring long-term model stability**, we recommend using [on-demand deployments](/guides/ondemand-deployments), which give you full control over model versions and updates.

<Tip>
  Make sure to add a [payment method](https://fireworks.ai/billing) to access [higher rate limits](/guides/quotas_usage/rate-limits) up to 6,000 RPM. Without a payment method, you're limited to 10 RPM.
</Tip>

## Next steps

Ready to scale to production, explore other modalities, or customize your models?

<CardGroup cols="3">
  <Card title="Deploy and autoscale on Dedicated GPUs" href="/guides/ondemand-deployments" icon="server">
    Deploy with high performance on dedicated GPUs with fast autoscaling and minimal cold starts
  </Card>

  <Card title="Fine-tune Models" href="/fine-tuning/finetuning-intro" icon="sliders">
    Improve model quality with supervised and reinforcement learning
  </Card>

  <Card title="Speech to Text" href="/api-reference/audio-transcriptions" icon="microphone">
    Real-time or batch audio transcription
  </Card>

  <Card title="Embeddings & Reranking" href="/guides/querying-embeddings-models" icon="brackets-curly">
    Use embeddings & reranking in search & context retrieval
  </Card>

  <Card title="Batch Inference" href="/guides/batch-inference" icon="list-check">
    Run async inference jobs at scale, faster and cheaper
  </Card>

  <Card title="Browse 100+ Models" href="https://fireworks.ai/models" icon="books">
    Explore all available models across modalities
  </Card>

  <Card title="API Reference" href="/api-reference/introduction" icon="code">
    Complete API documentation
  </Card>
</CardGroup>


# Batch API
Source: https://docs.fireworks.ai/guides/batch-inference

Process large-scale async workloads

Process large volumes of requests asynchronously at 50% lower cost. Batch API is ideal for:

* Production-scale inference workloads
* Large-scale testing and benchmarking
* Training smaller models with larger ones ([distillation guide](https://fireworks.ai/blog/deepseek-r1-distillation-reasoning))

<Tip>
  Batch jobs automatically use [prompt caching](/guides/prompt-caching) for additional 50% cost savings on cached tokens. Maximize cache hits by placing static content first in your prompts.
</Tip>

## Getting Started

<AccordionGroup>
  <Accordion title="1. Prepare Your Dataset">
    Datasets must be in JSONL format (one JSON object per line):

    **Requirements:**

    * **File format:** JSONL (each line is a valid JSON object)
    * **Size limit:** Under 500MB
    * **Required fields:** `custom_id` (unique) and `body` (request parameters)

    **Example dataset:**

    ```json  theme={null}
    {"custom_id": "request-1", "body": {"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of France?"}], "max_tokens": 100}}
    {"custom_id": "request-2", "body": {"messages": [{"role": "user", "content": "Explain quantum computing"}], "temperature": 0.7}}
    {"custom_id": "request-3", "body": {"messages": [{"role": "user", "content": "Tell me a joke"}]}}
    ```

    Save as `batch_input_data.jsonl` locally.
  </Accordion>

  <Accordion title="2. Upload Your Dataset">
    <Tabs>
      <Tab title="UI">
        You can simply navigate to the dataset tab, click `Create Dataset` and follow the wizard.

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=33255bb2d9afefc697230a6f4e723577" alt="Dataset Upload" data-og-width="2972" width="2972" data-og-height="2060" height="2060" data-path="images/fine-tuning/dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=e1f7631eedf19be2ffe910e931734378 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5148e67713f7a207c47a73da1fa56658 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=dde9343748034e1d13ae4fbc1ad4aecf 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a4a99ce824157064f5cbbdfdf0953c0d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=699fd69866de9383a06dc08a5139cb69 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b55ed77bc807c1ebf00223fff2997342 2500w" />
      </Tab>

      <Tab title="firectl">
        ```bash  theme={null}
        firectl create dataset batch-input-dataset ./batch_input_data.jsonl
        ```
      </Tab>

      <Tab title="HTTP API">
        You need to make two separate HTTP requests. One for creating the dataset entry and one for uploading the dataset. Full reference here: [Create dataset](/api-reference/create-dataset).

        ```bash  theme={null}
        # Create Dataset Entry
        curl -X POST "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/datasets" \
          -H "Authorization: Bearer ${API_KEY}" \
          -H "Content-Type: application/json" \
          -d '{
            "datasetId": "batch-input-dataset",
            "dataset": { "userUploaded": {} }
          }'

        # Upload JSONL file
        curl -X POST "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/datasets/batch-input-dataset:upload" \
          -H "Authorization: Bearer ${API_KEY}" \
          -F "file=@./batch_input_data.jsonl"
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="3. Create a Batch Job">
    <Tabs>
      <Tab title="UI">
        Navigate to the Batch Inference tab and click "Create Batch Inference Job". Select your input dataset:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=c74141b465db64bd4ca3c037d20b3f30" alt="BIJ Dataset Select" data-og-width="3840" width="3840" data-og-height="1982" height="1982" data-path="images/batch-inference/BIJ_Dataset_Select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ad3decfc23ff03325cc141ddb0bc3853 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4f8af4b1fb7736f614229eb4ba19bc71 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=cfe1d39030f0c62956bfc194464b181e 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3e45d9a631ed269bfc65976050127e75 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=df78513dac5d93ff6e316ac501662309 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Select.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=6581fe37392ca0df9907f1aaa57861f7 2500w" />

        Choose your model:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=384fe513029928f248d751e58e2f89b9" alt="BIJ Model Select" data-og-width="3840" width="3840" data-og-height="1970" height="1970" data-path="images/batch-inference/BIJ_Model_Select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d902f47c06ab6a6fa1aeb6df721ba1ab 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ce98f4d224a1485b4e600e08c860f947 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=1115f215e13cae034bc16a8f85f89316 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=fc380420be1ae9e6bbacb80bbd1bf810 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4675a8e7e3bdb523f68c177bcfde4347 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Model_Select.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=fabe3dd83aa7daf1c161cdc754d09782 2500w" />

        Configure optional settings:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=56179acd8c88d94143fda4b78c5cec2a" alt="BIJ Optional Settings" data-og-width="3840" width="3840" data-og-height="1976" height="1976" data-path="images/batch-inference/BIJ_Optional_Settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b3b8500e3b62e3314a289cf9fdd2a4b5 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=9f7870d2799cfdc8f83eb86d490e6192 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=23086532b59056a622bb03b4d13b7512 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=8000e1cacdf5dff70f4a18ebffb5b3b8 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=6564c2703f112beb51da20d1f5f95b5d 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Optional_Settings.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=7fd4dd8043ac01bd8efe3af0552e6cb0 2500w" />
      </Tab>

      <Tab title="firectl">
        ```bash  theme={null}
        firectl create batch-inference-job \
          --model accounts/fireworks/models/llama-v3p1-8b-instruct \
          --input-dataset-id batch-input-dataset
        ```

        With additional parameters:

        ```bash  theme={null}
        firectl create batch-inference-job \
          --job-id my-batch-job \
          --model accounts/fireworks/models/llama-v3p1-8b-instruct \
          --input-dataset-id batch-input-dataset \
          --output-dataset-id batch-output-dataset \
          --max-tokens 1024 \
          --temperature 0.7 \
          --top-p 0.9
        ```
      </Tab>

      <Tab title="HTTP API">
        ```bash  theme={null}
        curl -X POST "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/batchInferenceJobs?batchInferenceJobId=my-batch-job" \
          -H "Authorization: Bearer ${API_KEY}" \
          -H "Content-Type: application/json" \
          -d '{
            "model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
            "inputDatasetId": "accounts/'${ACCOUNT_ID}'/datasets/batch-input-dataset",
            "outputDatasetId": "accounts/'${ACCOUNT_ID}'/datasets/batch-output-dataset",
            "inferenceParameters": {
              "maxTokens": 1024,
              "temperature": 0.7,
              "topP": 0.9
            }
          }'
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="4. Monitor Your Job">
    <Tabs>
      <Tab title="UI">
        View all your batch inference jobs in the dashboard:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=523de401343695e5db041c42b36364ea" alt="BIJ List" data-og-width="3840" width="3840" data-og-height="1986" height="1986" data-path="images/batch-inference/BIJ_List.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5eb7409172fe41f7d8fdf472f673e5bc 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a6b3851347a0302d1942ccc20a01cd48 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=991bee935ffeeae9f177de6d016ee2c8 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=146cf5029a45bf2cf9c140aa5e56c7c5 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4909a6d11d5927d83d6d5a7062d35c54 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_List.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=8d54557cf79cdc8aca7d7eb27078b748 2500w" />
      </Tab>

      <Tab title="firectl">
        ```bash  theme={null}
        # Get job status
        firectl get batch-inference-job my-batch-job

        # List all batch jobs
        firectl list batch-inference-jobs
        ```
      </Tab>

      <Tab title="HTTP API">
        ```bash  theme={null}
        # Get specific job
        curl -X GET "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/batchInferenceJobs/my-batch-job" \
          -H "Authorization: Bearer ${API_KEY}"

        # List all jobs
        curl -X GET "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/batchInferenceJobs" \
          -H "Authorization: Bearer ${API_KEY}"
        ```
      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="5. Download Results">
    <Tabs>
      <Tab title="UI">
        Navigate to the output dataset and download the results:

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=af22b69efced8a70bcac70fecdf38ba8" alt="BIJ Dataset Download" data-og-width="3840" width="3840" data-og-height="1976" height="1976" data-path="images/batch-inference/BIJ_Dataset_Download.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=770f031bb6313b77cf2abcbc3f7684de 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3353ebde5f51bc348170c4d6cb1ee75f 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4180e89050342a2848db0a0670de2b35 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=64b7c055d37652271e6cda3da3fc4ccb 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ec7edc0a8e862d839f881df18c5eaf18 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/batch-inference/BIJ_Dataset_Download.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4db728381845bb89bbc98258bd7f2449 2500w" />
      </Tab>

      <Tab title="firectl">
        ```bash  theme={null}
        firectl download dataset batch-output-dataset
        ```
      </Tab>

      <Tab title="HTTP API">
        ```bash  theme={null}
        # Get download endpoint and save response
        curl -s -X GET "https://api.fireworks.ai/v1/accounts/${ACCOUNT_ID}/datasets/batch-output-dataset:getDownloadEndpoint" \
          -H "Authorization: Bearer ${API_KEY}" \
          -d '{}' > download.json

        # Extract and download all files
        jq -r '.filenameToSignedUrls | to_entries[] | "\(.key) \(.value)"' download.json | \
        while read -r object_path signed_url; do
            fname=$(basename "$object_path")
            echo "Downloading → $fname"
            curl -L -o "$fname" "$signed_url"
        done
        ```
      </Tab>
    </Tabs>

    <Tip>
      The output dataset contains two files: a **results file** (successful responses in JSONL format) and an **error file** (failed requests with debugging info).
    </Tip>
  </Accordion>
</AccordionGroup>

## Reference

<AccordionGroup>
  <Accordion title="Job states">
    Batch jobs progress through several states:

    | State          | Description                                           |
    | -------------- | ----------------------------------------------------- |
    | **VALIDATING** | Dataset is being validated for format requirements    |
    | **PENDING**    | Job is queued and waiting for resources               |
    | **RUNNING**    | Actively processing requests                          |
    | **COMPLETED**  | All requests successfully processed                   |
    | **FAILED**     | Unrecoverable error occurred (check status message)   |
    | **EXPIRED**    | Exceeded 24-hour limit (completed requests are saved) |
  </Accordion>

  <Accordion title="Supported models">
    * **Base Models** – Any model in the [Model Library](https://fireworks.ai/models)
    * **Custom Models** – Your uploaded or fine-tuned models

    *Note: Newly added models may have a delay before being supported. See [Quantization](/models/quantization) for precision info.*
  </Accordion>

  <Accordion title="Limits and constraints">
    * **Per-request limits:** Same as [Chat Completion API limits](/api-reference/post-chatcompletions)
    * **Input dataset:** Max 500MB
    * **Output dataset:** Max 8GB (job may expire early if reached)
    * **Job timeout:** 24 hours maximum
  </Accordion>

  <Accordion title="Handling expired jobs">
    Jobs expire after 24 hours. Completed rows are billed and saved to the output dataset.

    **Resume processing:**

    ```bash  theme={null}
    firectl create batch-inference-job \
      --continue-from original-job-id \
      --model accounts/fireworks/models/llama-v3p1-8b-instruct \
      --output-dataset-id new-output-dataset
    ```

    This processes only unfinished/failed requests from the original job.

    **Download complete lineage:**

    ```bash  theme={null}
    firectl download dataset output-dataset-id --download-lineage
    ```

    Downloads all datasets in the continuation chain.
  </Accordion>

  <Accordion title="Best practices">
    * **Validate thoroughly:** Check dataset format before uploading
    * **Descriptive IDs:** Use meaningful `custom_id` values for tracking
    * **Optimize tokens:** Set reasonable `max_tokens` limits
    * **Monitor progress:** Track long-running jobs regularly
    * **Cache optimization:** Place static content first in prompts
  </Accordion>
</AccordionGroup>

## Next Steps

<CardGroup cols={3}>
  <Card title="Prompt Caching" icon="bolt" href="/guides/prompt-caching">
    Maximize cost savings with automatic prompt caching
  </Card>

  <Card title="Fine-Tuning" icon="sparkles" href="/fine-tuning/finetuning-intro">
    Create custom models for your batch workloads
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/create-batch-inference-job">
    Full API documentation for Batch API
  </Card>
</CardGroup>


# Completions API
Source: https://docs.fireworks.ai/guides/completions-api

Use the completions API for raw text generation with custom prompt templates

The completions API provides raw text generation without automatic message formatting. Use this when you need full control over prompt formatting or when working with base models.

## When to use completions

**Use the completions API for:**

* Custom prompt templates with specific formatting requirements
* Base models (non-instruct/non-chat variants)
* Fine-grained control over token-level formatting
* Legacy applications that depend on raw completion format

**For most use cases, use [chat completions](/guides/querying-text-models) instead.** Chat completions handles message formatting automatically and works better with instruct-tuned models.

## Basic usage

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        prompt="Once upon a time"
    )

    print(response.choices[0].text)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      prompt: "Once upon a time",
    });

    console.log(response.choices[0].text);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "prompt": "Once upon a time"
      }'
    ```
  </Tab>
</Tabs>

<Note>
  Most models automatically prepend the beginning-of-sequence (BOS) token (e.g., `<s>`) to your prompt. Verify this with the `raw_output` parameter if needed.
</Note>

## Custom prompt templates

The completions API is useful when you need to implement custom prompt formats:

```python  theme={null}
# Custom few-shot prompt template
prompt = """Task: Classify the sentiment of the following text.

Text: I love this product!
Sentiment: Positive

Text: This is terrible.
Sentiment: Negative

Text: The weather is nice today.
Sentiment:"""

response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    prompt=prompt,
    max_tokens=10,
    temperature=0
)

print(response.choices[0].text)  # Output: " Positive"
```

## Common parameters

All [chat completions parameters](/guides/querying-text-models#configuration--debugging) work with completions:

* `temperature` - Control randomness (0-2)
* `max_tokens` - Limit output length
* `top_p`, `top_k`, `min_p` - Sampling parameters
* `stream` - Stream responses token-by-token
* `frequency_penalty`, `presence_penalty` - Reduce repetition

See the [API reference](/api-reference/post-completions) for complete parameter documentation.

## Querying deployments

Use completions with [on-demand deployments](/guides/ondemand-deployments) by specifying the deployment identifier:

```python  theme={null}
response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    prompt="Your prompt here"
)
```

## Next steps

<CardGroup cols={3}>
  <Card title="Chat Completions" href="/guides/querying-text-models" icon="messages">
    Use chat completions for most use cases
  </Card>

  <Card title="Streaming" href="/guides/querying-text-models#streaming-responses" icon="bolt">
    Stream responses for real-time UX
  </Card>

  <Card title="API Reference" href="/api-reference/post-completions" icon="code">
    Complete API documentation
  </Card>
</CardGroup>


# Tool Calling
Source: https://docs.fireworks.ai/guides/function-calling

Connect models to external tools and APIs

Tool calling (also known as function calling) enables models to intelligently select and use external tools based on user input. You can build agents that access APIs, retrieve real-time data, or perform actions—all through [OpenAI-compatible](https://platform.openai.com/docs/guides/function-calling) tool specifications.

**How it works:**

1. Define tools using [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step) (name, description, parameters)
2. Model analyzes the query and decides whether to call a tool
3. If needed, model returns structured tool calls with parameters
4. You execute the tool and send results back for the final response

## Quick example

Define tools and send a request - the model will return structured tool calls when needed:

```python  theme={null}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"}
            },
            "required": ["location"]
        }
    }
}]

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
    tools=tools,
    temperature=0.1
)

print(response.choices[0].message.tool_calls)
# Output: [ChatCompletionMessageToolCall(id='call_abc123', function=Function(arguments='{"location":"San Francisco"}', name='get_weather'), type='function')]
```

<Tip>
  For best results with tool calling, use a low temperature (0.0-0.3) to reduce hallucinated parameter values and ensure more deterministic tool selection.
</Tip>

<AccordionGroup>
  <Accordion title="Complete workflow: Execute tools and get final response">
    ```python  theme={null}
    import os
    from openai import OpenAI
    import json

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    # Step 1: Define your tools
    tools = [{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }
    }]

    # Step 2: Send initial request
    messages = [{"role": "user", "content": "What's the weather in San Francisco?"}]
    response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2-instruct-0905",
        messages=messages,
        tools=tools,
        temperature=0.1
    )

    # Step 3: Check if model wants to call a tool
    if response.choices[0].message.tool_calls:
        # Step 4: Execute the tool
        tool_call = response.choices[0].message.tool_calls[0]
        
        # Your actual tool implementation
        def get_weather(location, unit="celsius"):
            # In production, call your weather API here
            return {"temperature": 72, "condition": "sunny", "unit": unit}
        
        # Parse arguments and call your function
        function_args = json.loads(tool_call.function.arguments)
        function_response = get_weather(**function_args)
        
        # Step 5: Send tool response back to model
        messages.append(response.choices[0].message)  # Add assistant's tool call
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(function_response)
        })
        
        # Step 6: Get final response
        final_response = client.chat.completions.create(
            model="accounts/fireworks/models/kimi-k2-instruct-0905",
            messages=messages,
            tools=tools,
            temperature=0.1
        )
        
        print(final_response.choices[0].message.content)
        # Output: "It's currently 72°F and sunny in San Francisco."
    ```
  </Accordion>
</AccordionGroup>

## Defining tools

Tools are defined using [JSON Schema](https://json-schema.org/understanding-json-schema/reference) format. Each tool requires:

* **name**: Function identifier (a-z, A-Z, 0-9, underscores, dashes; max 64 characters)
* **description**: Clear explanation of what the function does (used by the model to decide when to call it)
* **parameters**: JSON Schema object describing the function's parameters

<Tip>
  Write detailed descriptions and parameter definitions. The model relies on these to select the correct tool and provide appropriate arguments.
</Tip>

### Parameter types

JSON Schema supports: `string`, `number`, `integer`, `object`, `array`, `boolean`, and `null`. You can also:

* Use `enum` to restrict values to specific options
* Mark parameters as `required` or optional
* Provide descriptions for each parameter

<Accordion title="Example: Defining multiple tools">
  ```python  theme={null}
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City name, e.g. San Francisco"
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                          "description": "Temperature unit"
                      }
                  },
                  "required": ["location"]
              }
          }
      },
      {
          "type": "function",
          "function": {
              "name": "search_restaurants",
              "description": "Search for restaurants by cuisine type",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "cuisine": {
                          "type": "string",
                          "description": "Type of cuisine (e.g., Italian, Mexican)"
                      },
                      "location": {
                          "type": "string",
                          "description": "City or neighborhood"
                      },
                      "price_range": {
                          "type": "string",
                          "enum": ["$", "$$", "$$$", "$$$$"]
                      }
                  },
                  "required": ["cuisine", "location"]
              }
          }
      }
  ]
  ```
</Accordion>

## Additional configurations

### tool\_choice

The [`tool_choice`](/api-reference/post-chatcompletions#body-tool-choice) parameter controls how the model uses tools:

* **`auto`** (default): Model decides whether to call a tool or respond directly
* **`none`**: Model will not call any tools
* **`required`**: Model must call at least one tool
* **Specific function**: Force the model to call a particular function

```python  theme={null}
# Force a specific tool
response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather?"}],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "get_weather"}},
    temperature=0.1
)
```

<Note>
  Some models support parallel tool calling, where multiple tools can be called in a single response. Check the model's capabilities before relying on this feature.
</Note>

## Streaming

<Accordion title="Using tool calls with streaming responses">
  Tool calls work with streaming responses. Arguments are sent incrementally as the model generates them:

  ```python  theme={null}
  import json
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  tools = [{
      "type": "function",
      "function": {
          "name": "get_weather",
          "description": "Get the current weather for a city",
          "parameters": {
              "type": "object",
              "properties": {
                  "city": {"type": "string", "description": "City name"},
                  "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
              },
              "required": ["city"]
          }
      }
  }]

  stream = client.chat.completions.create(
      model="accounts/fireworks/models/kimi-k2-instruct-0905",
      messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
      tools=tools,
      stream=True,
      temperature=0.1
  )

  # Accumulate tool call data
  tool_calls = {}

  for chunk in stream:
      if chunk.choices[0].delta.tool_calls:
          for tool_call in chunk.choices[0].delta.tool_calls:
              index = tool_call.index
              
              if index not in tool_calls:
                  tool_calls[index] = {"id": "", "name": "", "arguments": ""}
              
              if tool_call.id:
                  tool_calls[index]["id"] = tool_call.id
              if tool_call.function and tool_call.function.name:
                  tool_calls[index]["name"] = tool_call.function.name
              if tool_call.function and tool_call.function.arguments:
                  tool_calls[index]["arguments"] += tool_call.function.arguments
      
      if chunk.choices[0].finish_reason == "tool_calls":
          for tool_call in tool_calls.values():
              args = json.loads(tool_call["arguments"])
              print(f"Calling {tool_call['name']} with {args}")
          break
  ```
</Accordion>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Model isn't calling tools when expected">
    * Check that your tool descriptions are clear and detailed
    * Ensure the user query clearly indicates a need for the tool
    * Try using `tool_choice="required"` to force tool usage
    * Verify your model supports tool calling (check `supportsTools` field)
  </Accordion>

  <Accordion title="Tool arguments are incorrect or malformed">
    * Add more detailed parameter descriptions
    * Use lower temperature (0.0-0.3) for more deterministic outputs
    * Provide examples in parameter descriptions
    * Use `enum` to constrain values to specific options
  </Accordion>

  <Accordion title="Getting JSON parsing errors">
    * Always validate tool call arguments before parsing
    * Handle partial or malformed JSON gracefully in production
    * Use try-catch blocks when parsing `tool_call.function.arguments`
  </Accordion>
</AccordionGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Structured Outputs" icon="brackets-curly" href="/structured-responses/structured-response-formatting">
    Enforce JSON schemas for consistent responses
  </Card>

  <Card title="Text Models" icon="message" href="/guides/querying-text-models">
    Learn about chat completions and other APIs
  </Card>

  <Card title="Deployments" icon="server" href="/guides/ondemand-deployments">
    Deploy models on dedicated GPUs
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/post-chatcompletions">
    Full chat completions API documentation
  </Card>
</CardGroup>


# Inference Error Codes
Source: https://docs.fireworks.ai/guides/inference-error-codes

Common error codes, their meanings, and resolutions for inference requests

Understanding error codes helps you quickly diagnose and resolve issues when making inference requests to the Fireworks API.

## Common error codes

| **Code** | **Error Name**        | **Possible Issue(s)**                                                                                                                            | **How to Resolve**                                                                                                                                                            |
| -------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`    | Bad Request           | Invalid input or malformed request.                                                                                                              | Review the request parameters and ensure they match the expected format.                                                                                                      |
| `401`    | Unauthorized          | Invalid API key or insufficient permissions.                                                                                                     | Verify your API key and ensure it has the correct permissions.                                                                                                                |
| `402`    | Payment Required      | Account is not on a paid plan or has exceeded usage limits.                                                                                      | Check your billing status and ensure your payment method is up to date. Upgrade your plan if necessary.                                                                       |
| `403`    | Forbidden             | Authentication issues.                                                                                                                           | Verify you have the correct API key.                                                                                                                                          |
| `404`    | Not Found             | The API endpoint path doesn't exist, the model doesn't exist, the model is not deployed, or you don't have permission to access it.              | Verify the URL path in your request and ensure you are using the correct API endpoint. Check if the model exists and is available. Ensure you have the necessary permissions. |
| `405`    | Method Not Allowed    | Using an unsupported HTTP method (e.g., using GET instead of POST).                                                                              | Check the API documentation for the correct HTTP method.                                                                                                                      |
| `408`    | Request Timeout       | The request took too long to complete, possibly due to server overload or network issues.                                                        | Retry the request after a brief wait. Consider increasing the timeout value if applicable.                                                                                    |
| `412`    | Precondition Failed   | Account is suspended or there's an issue with account status. This error also occurs when attempting to invoke a LoRA model that failed to load. | Check your account status and billing information. For LoRA models, ensure the model was uploaded correctly and is compatible. Contact support if the issue persists.         |
| `413`    | Payload Too Large     | Input data exceeds the allowed size limit.                                                                                                       | Reduce the size of the input payload (e.g., by trimming large text or image data).                                                                                            |
| `429`    | Over Quota            | You've reached the API rate limit.                                                                                                               | Wait for the quota to reset or upgrade your plan for a higher rate limit. See [Rate Limits & Quotas](/guides/quotas_usage/rate-limits).                                       |
| `500`    | Internal Server Error | Server-side code bug that is unlikely to resolve on its own.                                                                                     | Contact Fireworks support immediately, as this error typically requires intervention from the engineering team.                                                               |
| `502`    | Bad Gateway           | The server received an invalid response from an upstream server.                                                                                 | Wait and retry the request. If the error persists, it may indicate a server outage.                                                                                           |
| `503`    | Service Unavailable   | The service is down for maintenance or experiencing issues.                                                                                      | Retry the request after some time. Check the [status page](https://status.fireworks.ai) for maintenance announcements.                                                        |
| `504`    | Gateway Timeout       | The server did not receive a response in time from an upstream server.                                                                           | Wait briefly and retry the request. Consider using a shorter input prompt if applicable.                                                                                      |
| `520`    | Unknown Error         | An unexpected error occurred with no clear explanation.                                                                                          | Retry the request. If the issue persists, contact support for further assistance.                                                                                             |

## Troubleshooting tips

If you encounter an error not listed here:

* Review the API documentation for the correct usage of endpoints and parameters
* Check the [Fireworks status page](https://status.fireworks.ai) for any ongoing service disruptions
* Contact support at [support@fireworks.ai](mailto:support@fireworks.ai) or join our [Discord](https://discord.gg/fireworks-ai)

<Tip>
  Enable detailed error logging in your application to capture the full error response, including error messages and request IDs, which helps with debugging.
</Tip>


# Deployments
Source: https://docs.fireworks.ai/guides/ondemand-deployments

Configure and manage on-demand deployments on dedicated GPUs

<Info>
  **New to deployments?** Start with our [Deployments Quickstart](/getting-started/ondemand-quickstart) to deploy and query your first model in minutes, then return here to learn about configuration options.
</Info>

On-demand deployments give you dedicated GPUs for your models, providing several advantages over serverless:

* **Better performance** – Lower latency, higher throughput, and predictable performance unaffected by other users
* **No hard rate limits** – Only limited by your deployment's capacity
* **Cost-effective at scale** – Cheaper under high utilization. Unlike serverless models (billed per token), on-demand deployments are [billed by GPU-second](https://fireworks.ai/pricing).
* **Broader model selection** – Access models not available on serverless
* **Custom models** – Upload your own models (for supported architectures) from Hugging Face or elsewhere

Need higher GPU quotas or want to reserve capacity? [Contact us](https://fireworks.ai/contact).

## Creating & querying deployments

**Create a deployment:**

```bash  theme={null}
# This command returns your DEPLOYMENT_NAME - save it for querying
firectl create deployment accounts/fireworks/models/<MODEL_NAME> --wait
```

See [Deployment shapes](#deployment-shapes) below to optimize for speed, throughput, or cost.

**Query your deployment:**

After creating a deployment, query it using this format:

```
<MODEL_NAME>#<DEPLOYMENT_NAME>
```

<Tip>
  You can find your deployment name anytime with `firectl list deployments` and `firectl get deployment <DEPLOYMENT_ID>`.
</Tip>

**Examples:**

<Tabs>
  <Tab title="Fireworks model">
    ```
    accounts/fireworks/models/mixtral-8x7b#accounts/alice/deployments/12345678
    ```

    * Model: `accounts/fireworks/models/mixtral-8x7b`
    * Deployment: `accounts/alice/deployments/12345678`

    <Tip>
      You can also use shorthand: `fireworks/mixtral-8x7b#alice/12345678`
    </Tip>
  </Tab>

  <Tab title="Custom model">
    ```
    accounts/alice/models/custom-model#accounts/alice/deployments/12345678
    ```

    * Model: `accounts/alice/models/custom-model`
    * Deployment: `accounts/alice/deployments/12345678`

    <Tip>
      You can also use shorthand: `alice/custom-model#alice/12345678`
    </Tip>
  </Tab>
</Tabs>

### Code examples

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
      messages: [
        {
          role: "user",
          content: "Explain quantum computing in simple terms",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        "messages": [
          {
            "role": "user",
            "content": "Explain quantum computing in simple terms"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

## Deployment shapes

Deployment shapes are the primary way to configure deployments. They're pre-configured templates optimized for speed, cost, or efficiency, including hardware, quantization, and other [performance factors](/faq/deployment/performance/optimization#performance-factors).

* **Fast** – Low latency for interactive workloads
* **Throughput** – Cost-per-token at scale for high-volume workloads
* **Minimal** – Lowest cost for testing or light workloads

**Usage:**

```bash  theme={null}
# List available shapes
firectl list deployment-shape-versions --base-model <model-id>

# Create with a shape (shorthand)
firectl create deployment accounts/fireworks/models/deepseek-v3 --deployment-shape throughput

# Create with full shape ID
firectl create deployment accounts/fireworks/models/llama-v3p3-70b-instruct \
  --deployment-shape accounts/fireworks/deploymentShapes/llama-v3p3-70b-instruct-fast

# View shape details
firectl get deployment-shape-version <full-deployment-shape-version-id>
```

<Tip>
  Need even better performance with tailored optimizations? [Contact our team](https://fireworks.ai/contact).
</Tip>

## Managing & configuring deployments

### Basic management

```bash  theme={null}
# List all deployments
firectl list deployments

# Check deployment status
firectl get deployment <DEPLOYMENT_ID>

# Delete a deployment
firectl delete deployment <DEPLOYMENT_ID>
```

<Note>
  By default, deployments scale to zero if unused for 1 hour. Deployments with min replicas set to 0 are automatically deleted after 7 days of no traffic.
</Note>

### GPU hardware

Choose GPU type with `--accelerator-type`:

* `NVIDIA_A100_80GB`
* `NVIDIA_H100_80GB`
* `NVIDIA_H200_141GB`

GPU availability varies by [region](/deployments/regions). See [Hardware selection guide→](https://docs.fireworks.ai/faq/deployment/ondemand/hardware-options#hardware-selection)

### Autoscaling

Control replica counts, scale timing, and load targets for your deployment.

See the [Autoscaling guide](/deployments/autoscaling) for configuration options.

### Multiple GPUs per replica

Use multiple GPUs to improve latency and throughput:

```bash  theme={null}
firectl create deployment <MODEL_NAME> --accelerator-count 2
```

More GPUs = faster generation. Note that scaling is sub-linear (2x GPUs ≠ 2x performance).

## Advanced

* **[Speculative decoding](/deployments/speculative-decoding)** - Speed up text generation using draft models or n-gram speculation
* **[Quantization](/models/quantization)** - Reduce model precision (e.g., FP16 to FP8) to improve speeds and reduce costs by 30-50%
* **[Performance benchmarking](/deployments/benchmarking)** - Measure and optimize your deployment's performance with load testing
* **[Managing default deployments](/deployments/managing-default-deployments)** - Control which deployment handles queries when using just the model name
* **[Publishing deployments](/deployments/publishing-deployments)** - Make your deployment accessible to other Fireworks users

## Next steps

<CardGroup cols={3}>
  <Card title="Autoscaling" href="/deployments/autoscaling" icon="arrows-up-down">
    Configure autoscaling for optimal cost and performance
  </Card>

  <Card title="Upload custom models" href="/models/uploading-custom-models" icon="cloud-arrow-up">
    Deploy your own models from Hugging Face
  </Card>

  <Card title="Quantization" href="/models/quantization" icon="compress">
    Reduce costs with model quantization
  </Card>

  <Card title="Regions" href="/deployments/regions" icon="earth-americas">
    Choose deployment regions for optimal latency
  </Card>

  <Card title="Reserved capacity" href="/deployments/reservations" icon="calendar-check">
    Purchase reserved GPUs for guaranteed capacity
  </Card>

  <Card title="Fine-tuning" href="/fine-tuning/finetuning-intro" icon="wand-magic-sparkles">
    Fine-tune models for your specific use case
  </Card>
</CardGroup>


# Using predicted outputs
Source: https://docs.fireworks.ai/guides/predicted-outputs

Use Predicted Outputs to boost output generation speeds for editing / rewriting use cases

<Tip>
  This feature is in beta and we are working on improvements. We welcome your feedback on [Discord](https://discord.gg/fireworks-ai)
</Tip>

In cases where large parts of the LLM output are known in advance, e.g. editing or rewriting a document or code snippet, you can improve output generation speeds with predicted outputs. Predicted outputs allows you to provide strong "guesses" of what output may look like.

To use Predicted Outputs, set the `prediction` field in the Fireworks API with the predicted output. For example, you may want to edit a survey and add an option to contact users by text message:

```
{
  "questions": [
    {
      "question": "Name",
      "type": "text"
    },
    {
      "question": "Age",
      "type": "number"
    },
    {
      "question": "Feedback",
      "type": "text_area"
    },
    {
      "question": "How to Contact",
      "type": "multiple_choice",
      "options": ["Email", "Phone"],
      "optional": true
    }
  ]
}
```

In this case, we expect most of the code will remain the same. We set the ‘prediction’ field to be the original survey code. The output generation speed increases using predicted outputs.

```python Python (Fireworks) theme={null}
from fireworks.client import Fireworks
 
code = """{
"questions": [
    {
      "question": "Name",
      "type": "text"
    },
    {
      "question": "Age",
      "type": "number"
    },
    {
      "question": "Feedback",
      "type": "text_area"
    },
    {
      "question": "How to Contact",
      "type": "multiple_choice",
      "options": ["Email", "Phone"],
      "optional": true
    }
  ]
}
"""

client = Fireworks(api_key="<FIREWORKS_API_KEY>")

response = client.chat.completions.create(
  model="accounts/fireworks/models/llama-v3p1-70b-instruct",
  messages=[{
      "role": "user",
      "content": "Edit the How to Contact question to add an option called Text Message. Output the full edited code, with no markdown or explanations.",
    },
    {
      "role": "user",
      "content": code
    }
  ],
  temperature=0,
  prediction={"type": "content", "content": code}
)

print(response.choices[0].message.content)
```

### Additional information on Predicted Outputs:

* Using Predicted Outputs is free at this time
* We recommend setting `temperature=0` for best results for most intended use cases of Predicted Outputs. In these cases, using Predicted Outputs does not impact the quality of outputs generated
* If the prediction is substantially different from the generated output, output generation speed may decrease
* The max length of the `prediction` field is set by `max_tokens` and is 2048 by default, and needs to be updated if you have a longer input and prediction.
* If you are using an on-demand deployment, you can set `rewrite_speculation=True` and potentially get even faster output generation. We are working on rolling this out to Serverless soon.


# Prompt caching
Source: https://docs.fireworks.ai/guides/prompt-caching



Prompt caching is a performance optimization feature that allows Fireworks to
respond faster to requests with prompts that share common prefixes. In many
situations, it can reduce time to first token (TTFT) by as much as 80%.

Prompt caching is enabled by default for all Fireworks models and deployments.

For dedicated deployments, prompt caching frees up resources, leading to higher
throughput on the same hardware. Dedicated deployments on the Enterprise plan allow
additional configuration options to further optimize cache performance.

## Using prompt caching

### Common use cases

Requests to LLMs often share a large portion of their prompt. For example:

* Long system prompts with detailed instructions
* Descriptions of available tools for function calling
* Growing previous conversation history for chat use cases
* Shared per-user context, like a current file for a coding assistant

Prompt caching avoids re-processing the cached prefix of the prompt and starts output generation much sooner.

### Structuring prompts for caching

Prompt caching works only for exact prefix matches within a prompt. To
realize caching benefits, place static content like instructions and examples at
the beginning of your prompt, and put variable content, such as user-specific
information, at the end.

For function calling models, tools are considered part of the prompt.

## Optimization techniques for maximum cache hits

Due to the autoregressive nature of LLMs, even a single-token difference can invalidate the cache from that token onward. Here are key strategies to maximize your cache hit rates:

### Keep your prompt prefix stable

The most critical rule for effective prompt caching is maintaining a stable prefix. Any change to the beginning of your prompt will invalidate the entire cache chain that follows.

<Warning>
  **Common mistake:** Including timestamps or other dynamic content at the beginning of your system prompt.

  ```python  theme={null}
  # ❌ DON'T: This kills cache hit rates
  system_prompt = f"""
  Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  You are a helpful AI assistant...
  """
  ```

  Even a one-second difference in the timestamp will invalidate the entire cache, making it completely ineffective.
</Warning>

### Structure prompts for caching success

**✅ DO:** Place static content first, dynamic content last

```python  theme={null}
from fireworks import LLM

# ✅ Good: Static content first
system_prompt = """
You are a helpful AI assistant with expertise in software development.

Your guidelines:
- Provide clear, concise explanations
- Include practical examples when helpful
- Ask clarifying questions when requirements are unclear

Available tools:
- web_search: Search the internet for current information
- code_executor: Run code snippets safely
- file_manager: Read and write files
"""

# Build the complete prompt
user_message = ""

# Add dynamic content at the end
if user_context:
    user_message += f"User context: {user_context}\n\n"

if current_time_needed:
    user_message += f"Current time: {datetime.now().isoformat()}\n\n"

# User query goes last
user_message += user_query

# Use with Fireworks Build SDK
llm = LLM(model="llama-v3p1-70b-instruct", deployment_type="auto")

response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)
```

### Smart timestamp handling

When you need to provide current time information, consider these strategies:

**Option 1: Rounded timestamps**

```python  theme={null}
# ✅ Round to larger intervals to increase cache hits
current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
system_prompt = f"""
You are a helpful assistant.
Current hour: {current_hour.strftime('%Y-%m-%d %H:00')}
...
"""
```

**Option 2: Conditional time injection**

```python  theme={null}
# ✅ Only add time when the query actually needs it
def build_prompt(user_query, system_base):
    prompt = system_base
    
    # Only add timestamp for time-sensitive queries
    time_keywords = ['today', 'now', 'current', 'latest', 'recent']
    if any(keyword in user_query.lower() for keyword in time_keywords):
        prompt += f"\nCurrent time: {datetime.now().isoformat()}"
    
    prompt += f"\nUser: {user_query}"
    return prompt
```

**Option 3: Move time to user message**

```python  theme={null}
from fireworks import LLM

# ✅ Keep system prompt static, add time context to user message
system_prompt = """
You are a helpful AI assistant...
""" # This stays the same

user_message = f"""
Current time: {datetime.now().isoformat()}

User query: {user_query}
"""

# Use with Fireworks Build SDK
llm = LLM(model="llama-v3p1-70b-instruct", deployment_type="auto")

response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)
```

By following these optimization techniques, you can significantly improve your application's performance through effective prompt caching while maintaining the quality and functionality of your AI system.

### How it works

Fireworks will automatically find the longest prefix of the request that is
present in the cache and reuse it. The remaining portion of the prompt will be
processed as usual.

The entire prompt is stored in the cache for future reuse. Cached prompts
usually stay in the cache for at least several minutes. Depending on the model,
load level, and deployment configuration, it can be up to several hours. The
oldest prompts are evicted from the cache first.

Prompt caching doesn't alter the result generated by the model. The response you
receive will be identical to what you would get if prompt caching was not used.
Each generation is sampled from the model independently on each request and is not
cached for future usage.

## Monitoring

For dedicated deployments, information about prompt caching is returned in the
response headers. The header `fireworks-prompt-tokens` contains the number of tokens
in the prompt, out of which `fireworks-cached-prompt-tokens` are cached.

Aggregated metrics are also available in the [usage dashboard](https://fireworks.ai/account/usage?type=deployments).

## Data privacy

Serverless deployments maintain separate caches for each Fireworks account to prevent data leakage and timing attacks.

Dedicated deployments by default share a single cache across all requests.
Because prompt caching doesn't change the outputs, privacy is preserved even
if the deployment powers a multi-tenant application. It does open a minor risk
of a timing attack: potentially, an adversary can learn that a particular prompt
is cached by observing the response time. To ensure full isolation, you can pass
the `x-prompt-cache-isolation-key` header or the `prompt_cache_isolation_key`
field in the body of the request. It can contain an arbitrary string that acts
as an additional cache key, i.e., no sharing will occur between requests with
different IDs.

## Limiting or turning off caching

Additionally, you can pass the `prompt_cache_max_len` field in the request body to
limit the maximum prefix of the prompt (in tokens) that is considered for
caching. It's rarely needed in real applications but can come in handy for
benchmarking the performance of dedicated deployments by passing
`"prompt_cache_max_len": 0`.

## Advanced: cache locality for Enterprise deployments

Dedicated deployments on an Enterprise plan allow you to pass an additional hint in the request to improve cache hit rates.

First, the deployment needs to be created or updated with an additional flag:

```bash  theme={null}
firectl create deployment ... --enable-session-affinity
```

Then the client can pass an opaque identifier representing a single user or
session in the `user` field of the body or in the `x-session-affinity` header. Fireworks
will try to route requests with the identifier to the same server, further reducing response times.

It's best to choose an identifier that groups requests with long shared prompt
prefixes. For example, it can be a chat session with the same user or an
assistant working with the same shared context.

### Migration and traffic management

When migrating between deployments that use prompt caching, it's crucial to implement proper traffic routing to maintain optimal cache hit rates. When gradually routing traffic to a new deployment, use consistent user/session-based sampling rather than random sampling.

Here's the recommended implementation for traffic routing:

```python  theme={null}
import hashlib

# Configure traffic fraction (e.g., 20% to new deployment)
fireworks_traffic_fraction = 0.2
user_id = "session-id-123"

# Generate deterministic hash from user_id
hashed_user_id = int(hashlib.md5(user_id.encode()).hexdigest(), 16) # MD5 hash on user-id and convert to integer
MAX_HASH = 2**128 - 1  # MD5 hash maximum value

# Compute ratio for consistent routing
ratio = hashed_user_id / MAX_HASH # Returns 0.0 to 1.0

if (ratio < fireworks_traffic_fraction):
    send_to_new_deployment(user=hashed_user_id)  # Pass user ID for caching
else:
    send_elsewhere()  # Route to old deployment or serverless
```

<Warning>
  Avoid random sampling for traffic routing as it can negatively impact cache hit rates:

  ```python  theme={null}
  # Don't do this:
  if random() < fireworks_traffic_fraction:  # ❌ Reduces cache effectiveness
    send_to_new_deployment(user=hashed_user_id)
  ```

  Using consistent user-based routing ensures complete user sessions are maintained on the same deployment, optimizing prompt cache performance regardless of the traffic fraction.
</Warning>


# Speech to Text
Source: https://docs.fireworks.ai/guides/querying-asr-models

Convert audio to text with streaming and pre-recorded transcription

Fireworks AI provides three ASR (Automatic Speech Recognition) features: **Streaming Transcription**, **Pre-recorded Transcription**, and **Pre-recorded Translation**. This guide shows you how to get started with each feature.

## Streaming Transcription

Convert audio to text in real-time using WebSocket connections. Perfect for voice agents and live applications.

### Quick Start

**Available Models:**

* [`fireworks-asr-large`](https://app.fireworks.ai/models/fireworks/fireworks-asr-large): Cost efficient model for real-time transcription over web-sockets
* [`fireworks-asr-v2`](https://app.fireworks.ai/models/fireworks/fireworks-asr-v2): Next generation and ultra-low latency audio streaming for real-time transcription over web-sockets

For a working example of streaming transcription see the following resources:

1. [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
2. [Python cookbook](https://github.com/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/python)

For more detailed information, see the [full streaming API documentation](/api-reference/audio-streaming-transcriptions) and the [source code](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text)

## Pre-recorded Transcription

Convert audio files to text. Supports files up to 1GB in formats like MP3, FLAC, and WAV. Transcribe multiple hours of audio in minutes.

### Quick Start

For a working example of pre-recorded transcription see the [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_prerecorded_speech_to_text/audio_prerecorded_speech_to_text.ipynb)

**Available Models:**

* [`whisper-v3`](https://app.fireworks.ai/models/fireworks/whisper-v3): Highest accuracy
  * model=`whisper-v3`
  * base\_url=`https://audio-prod.api.fireworks.ai`
* [`whisper-v3-turbo`](https://app.fireworks.ai/models/fireworks/whisper-v3-turbo): Faster processing
  * model=`whisper-v3-turbo`
  * base\_url=`https://audio-turbo.api.fireworks.ai`

For more detailed information, see the [full transcription API documentation](/api-reference/audio-transcriptions)

## Pre-recorded Translation

Translate audio from any of our supported languages to English. Supports files up to 1GB in formats like MP3, FLAC, and WAV.

### Quick Start

<CodeGroup>
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

  ```bash curl theme={null}

  # Download audio file
  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request
  curl -X POST "https://audio-prod.api.fireworks.ai/v1/audio/translations" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
  ```
</CodeGroup>

For more detailed information, see the [full translation API documentation](/api-reference/audio-translations)

## Supported Languages

We support 95+ languages including English, Spanish, French, German, Chinese, Japanese, Russian, Portuguese, and many more. See the [complete language list](/api-reference/audio-transcriptions#supported-languages).

## Common Use Cases

* **Call Center / Customer Service**: Transcribe or translate customer calls
* **Note Taking**: Transcribe audio for automated note taking

## Next Steps

1. Explore [advanced features](/api-reference/audio-transcriptions) like speaker diarization and custom prompts
2. Contact us at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) for dedicated endpoints and enterprise features


# Embeddings & Reranking
Source: https://docs.fireworks.ai/guides/querying-embeddings-models

Generate embeddings and rerank results for semantic search

Fireworks hosts embedding and reranking models, which are useful for tasks like RAG and semantic search.

## Model Availability

Fireworks hosts several purpose-built embeddings models, which are optimized specifically for tasks like semantic search and document similarity comparison. We host the SOTA Qwen3 Embeddings family of models:

* `fireworks/qwen3-embedding-8b` (\*available on serverless)
* `fireworks/qwen3-embedding-4b`
* `fireworks/qwen3-embedding-0p6b`

<AccordionGroup>
  <Accordion title="Use any LLM as an embeddings model">
    You can retrieve embeddings from any LLM in our model library. Here are some examples of LLMs that work with the embeddings API:

    * `fireworks/glm-4p5`
    * `fireworks/gpt-oss-20b`
    * `fireworks/kimi-k2-instruct-0905`
    * `fireworks/deepseek-r1-0528`
  </Accordion>

  <Accordion title="Bring your own model">
    You can also retrieve embeddings from any models you bring yourself through [custom model upload](/models/uploading-custom-models).
  </Accordion>

  <Accordion title="BERT-based models (legacy)">
    These BERT-based models are available on serverless only:

    * `nomic-ai/nomic-embed-text-v1.5`
    * `nomic-ai/nomic-embed-text-v1`
    * `WhereIsAI/UAE-Large-V1`
    * `thenlper/gte-large`
    * `thenlper/gte-base`
    * `BAAI/bge-base-en-v1.5`
    * `BAAI/bge-small-en-v1.5`
    * `mixedbread-ai/mxbai-embed-large-v1`
    * `sentence-transformers/all-MiniLM-L6-v2`
    * `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
  </Accordion>
</AccordionGroup>

## Generating embeddings

Embeddings models take text as input and output a vector of floating point numbers to use for tasks like similarity comparisons and search. Our embedding service is OpenAI compatible. Refer to OpenAI's embeddings [guide](https://platform.openai.com/docs/guides/embeddings)  and OpenAI's [embeddings documentation](https://platform.openai.com/docs/api-reference/embeddings) for more information on using these models.

```python Python theme={null}
import requests

url = "https://api.fireworks.ai/inference/v1/embeddings"

payload = {
    "input": "The quick brown fox jumped over the lazy dog",
    "model": "fireworks/qwen3-embedding-8b",
}

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

To generate variable-length embeddings, you can add the `dimensions` parameter to the request, for example, `dimensions: 128`.

The API usage for embedding models is identical for BERT-based and LLM-based embeddings. Simply use the `/v1/embeddings` endpoint with your chosen model.

## Reranking documents

Reranking models are used to rerank a list of documents based on a query. We only support reranking with the Qwen3 Reranker family of models:

* `fireworks/qwen3-reranker-8b` (\*available on serverless)
* `fireworks/qwen3-reranker-4b`
* `fireworks/qwen3-reranker-0p6b`

The reranking model takes a query and a list of documents as input and outputs the list of documents scored by relevance to the query.

```python Python theme={null}
import requests

url = "https://api.fireworks.ai/inference/v1/rerank"

payload = {
      "model": "fireworks/qwen3-reranker-8b",
      "query": "What was the primary objective of the Apollo 10 mission?",
      "documents": [
        "The Apollo 10 mission was launched in May 1969 and served as a 'dress rehearsal' for the Apollo 11 lunar landing.",
        "The crew of Apollo 10 consisted of astronauts Thomas Stafford, John Young, and Eugene Cernan.",
        "The command module for Apollo 10 was nicknamed 'Charlie Brown' and the lunar module was called 'Snoopy', after characters from the Peanuts comics.",
        "The Apollo program was a series of NASA missions that successfully landed the first humans on the Moon and returned them safely to Earth."
      ],
      "top_n": 3,
      "return_documents": True
}

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

```

## Deploying embeddings and reranking models

While Qwen3 Embedding 8b and Qwen3 Reranker 8b are available on serverless, you also have the option to deploy them via [on-demand deployments](/guides/ondemand-deployments).

<Tip>
  We recommend passing `--load-targets default=0.4` to ensure proper autoscaling responsiveness for these deployments
</Tip>



---

**Navigation:** [← Previous](./04-7-report-results.md) | [Index](./index.md) | [Next →](./06-text-models.md)
