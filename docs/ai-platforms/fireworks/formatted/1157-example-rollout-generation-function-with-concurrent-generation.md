---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example rollout generation function with concurrent generation

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

>   **📝 Note**
>
> Each sample in the dataset must contain multiple trajectories for the same prompt. This is required for policy optimization to work.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
