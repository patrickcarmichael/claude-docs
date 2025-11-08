---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Test your evaluator locally

Test your evaluator locally before launching training, to verify everything works with your rollout processor.

**Terminal 1** - Start the local UI server to view results:
```bash
ep logs
```
**Terminal 2** - Kick off the test:
```bash
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
