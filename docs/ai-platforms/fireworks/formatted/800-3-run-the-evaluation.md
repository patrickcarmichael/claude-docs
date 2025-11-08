---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Run the evaluation

First, start the local UI server to view evaluation results. Open a terminal and run:
```bash
ep logs
```
This will start a local server and should automatically open a browser window at `http://localhost:8000`. Keep this terminal running.

Then, in a **new terminal**, run the test script to evaluate the model on sample math problems:
```bash
cd gsm8k_artifacts
pytest -q tests/pytest/gsm8k/test_pytest_math_example.py::test_math_dataset -s
```
As the test runs, you'll see evaluation results appear in the browser showing detailed logs for each problem the model attempts. The `pytest` script will also register your evaluator and dataset with Fireworks automatically, so you can use them in the next step for RFT.

<Frame>
  <img src="https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=5471eb87139be4ec8cb2d80f3dfdd520" alt="GSM8K evaluation UI showing model scores and trajectories" data-og-width="1372" width="1372" data-og-height="932" height="932" data-path="images/fine-tuning/gsm8k-local-eval.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?w=280&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=6739d7f7b7d46199b697d4d080c24901 280w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?w=560&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=0e0c275275f5b1c06d16c7b1b198df99 560w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?w=840&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=300fc7447b2fe0317dbbf2326daeb4d3 840w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?w=1100&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=49c5520f70b125626432919a49bb068f 1100w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?w=1650&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=03f75f36f4252506619dcf1316d8760e 1650w, https://mintcdn.com/fireworksai/-W_W6FWo8Ax1n6pD/images/fine-tuning/gsm8k-local-eval.jpeg?w=2500&fit=max&auto=format&n=-W_W6FWo8Ax1n6pD&q=85&s=84ccf999f7f2d12ca200318166d1282e 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
