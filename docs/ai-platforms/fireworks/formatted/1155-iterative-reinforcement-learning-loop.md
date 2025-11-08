---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Iterative reinforcement learning loop

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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
