**Navigation:** [← Previous](./01-exporting-billing-metrics.md) | [Index](./index.md) | [Next →](./03-save-the-evaluator.md)

---

# With display name and description
reward-kit deploy --id my-evaluator \
  --metrics-folders "clarity=./my_metrics/clarity" \
  --display-name "Clarity Evaluator" \
  --description "Evaluates responses based on clarity"

# Force overwrite existing evaluator
reward-kit deploy --id my-evaluator \
  --metrics-folders "clarity=./my_metrics/clarity" \
  --force

# Multiple metrics
reward-kit deploy --id comprehensive-evaluator \
  --metrics-folders "clarity=./my_metrics/clarity" "accuracy=./my_metrics/accuracy" \
  --display-name "Comprehensive Evaluator"
```

## Common Workflows

### Iterative Development Workflow

A typical development workflow using the CLI now often involves `reward-kit run` first:

1. **Configure**: Set up your dataset and evaluation parameters in Hydra YAML files (e.g., `conf/dataset/my_data.yaml`, `conf/run_my_eval.yaml`). Define or reference your reward function logic.
2. **Run**: Execute the evaluation pipeline using `reward-kit run`. This generates model responses and initial scores.
   ```bash  theme={null}
   python -m reward_kit.cli run --config-path ./conf --config-name run_my_eval.yaml
   ```
3. **Analyze & Iterate**:
   * Examine the detailed results (`*_results.jsonl`) and the `preview_input_output_pairs.jsonl` from the output directory.
   * If iterating on reward logic, you can use `reward-kit preview` with the `preview_input_output_pairs.jsonl` and your updated local metric script.
   ```bash  theme={null}
   reward-kit preview \
     --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
     --metrics-folders "my_refined_metric=./path/to/refined_metric"
   ```
   * Refine your reward function code or Hydra configurations.
4. **Re-run**: If configurations changed significantly or you need new model generations, re-run `reward-kit run`.
5. **Deploy**: Once satisfied with the evaluator's performance and configuration:
   ```bash  theme={null}
   reward-kit deploy --id my-evaluator-id \
     --metrics-folders "my_final_metric=./path/to/final_metric" \
     --display-name "My Final Evaluator" \
     --description "Description of my evaluator" \
     --force
   ```
   *(Note: The `--metrics-folders` for `deploy` should point to the finalized reward function script(s) you intend to deploy as the evaluator.)*

### Comparing Multiple Metrics

You can preview multiple metrics to compare their performance:

```bash  theme={null}
# Preview with multiple metrics
reward-kit preview \
  --metrics-folders \
  "metric1=./my_metrics/metric1" \
  "metric2=./my_metrics/metric2" \
  "metric3=./my_metrics/metric3" \
  --samples ./samples.jsonl
```

### Deployment with Custom Providers

You can deploy with specific model providers:

```bash  theme={null}
# Deploy with custom provider
reward-kit deploy --id my-evaluator \
  --metrics-folders "clarity=./my_metrics/clarity" \
  --providers '[{"providerType":"anthropic","modelId":"claude-3-sonnet-20240229"}]'
```

## Agent-Eval Command

The `agent-eval` command enables you to run agent evaluations using task bundles.

### Syntax

```bash  theme={null}
reward-kit agent-eval [options]
```

### Options

#### Task Specification:

* `--task-dir`: Path to task bundle directory containing reward.py, tools.py, etc.
* `--dataset` or `-d`: Path to JSONL file containing task specifications.

#### Output and Models:

* `--output-dir` or `-o`: Directory to store evaluation runs (default: "./runs").
* `--model`: Override MODEL\_AGENT environment variable.
* `--sim-model`: Override MODEL\_SIM environment variable for simulated user.

#### Testing and Debugging:

* `--no-sim-user`: Disable simulated user (use static initial messages only).
* `--test-mode`: Run in test mode without requiring API keys.
* `--mock-response`: Use a mock agent response (works with --test-mode).
* `--debug`: Enable detailed debug logging.
* `--validate-only`: Validate task bundle structure without running evaluation.
* `--export-tools`: Export tool specifications to directory for manual testing.

#### Advanced Options:

* `--task-ids`: Comma-separated list of task IDs to run.
* `--max-tasks`: Maximum number of tasks to evaluate.
* `--registries`: Custom tool registries in format 'name=path'.
* `--registry-override`: Override all toolset paths with this registry path.
* `--evaluator`: Custom evaluator module path (overrides default).

### Examples

**Note**: The following examples use `examples/your_agent_task_bundle/` as a placeholder. You will need to replace this with the actual path to your task bundle directory.

```bash  theme={null}
# Run agent evaluation with default settings, assuming MODEL_AGENT is set
export MODEL_AGENT=openai/gpt-4o-mini # Example model
reward-kit agent-eval --task-dir examples/your_agent_task_bundle/

# Use a specific dataset file from your task bundle
reward-kit agent-eval --dataset examples/your_agent_task_bundle/task.jsonl --task-dir examples/your_agent_task_bundle/

# Run in test mode (no API keys required)
reward-kit agent-eval --task-dir examples/your_agent_task_bundle/ --test-mode --mock-response

# Validate task bundle structure without running
reward-kit agent-eval --task-dir examples/your_agent_task_bundle/ --validate-only

# Use a custom model and limit to specific tasks
reward-kit agent-eval --task-dir examples/your_agent_task_bundle/ \
  --model anthropic/claude-3-opus-20240229 \
  --task-ids your_task.id.001,your_task.id.002

# Export tool specifications for manual testing
reward-kit agent-eval --task-dir examples/your_agent_task_bundle/ --export-tools ./tool_specs
```

### Task Bundle Structure

A task bundle is a directory containing the following files:

* `reward.py`: Reward function with @reward\_function decorator
* `tools.py`: Tool registry with tool definitions
* `task.jsonl`: Dataset rows with task specifications
* `seed.sql` (optional): Initial database state

See the [Agent Evaluation](/evaluators/developer_guide/agent_evaluation) guide for more details.

## Environment Variables

The CLI recognizes the following environment variables:

* `FIREWORKS_API_KEY`: Your Fireworks API key (required for deployment operations)
* `FIREWORKS_API_BASE`: Base URL for the Fireworks API (defaults to `https://api.fireworks.ai`)
* `FIREWORKS_ACCOUNT_ID`: Your Fireworks account ID (optional, can be configured in auth.ini)
* `MODEL_AGENT`: Default agent model to use (e.g., "openai/gpt-4o-mini")
* `MODEL_SIM`: Default simulation model to use (e.g., "openai/gpt-3.5-turbo")

## Troubleshooting

### Common Issues

1. **Authentication Errors**:
   ```
   Error: Authentication failed. Check your API key.
   ```
   Solution: Ensure `FIREWORKS_API_KEY` is correctly set.

2. **Metrics Folder Not Found**:
   ```
   Error: Metrics folder not found: ./my_metrics/clarity
   ```
   Solution: Check that the path exists and contains a valid `main.py` file.

3. **Invalid Sample File**:
   ```
   Error: Failed to parse sample file. Ensure it's a valid JSONL file.
   ```
   Solution: Verify the sample file is in the correct JSONL format.

4. **Deployment Permission Issues**:
   ```
   Error: Permission denied. Your API key doesn't have deployment permissions.
   ```
   Solution: Use a production API key with deployment permissions or request additional permissions.

5. **Task Bundle Validation Errors**:
   ```
   Error: Missing required files in task bundle: tools.py, reward.py
   ```
   Solution: Ensure your task bundle has all required files.

6. **Model API Key Not Set**:
   ```
   Warning: MODEL_AGENT environment variable is not set
   ```
   Solution: Set the MODEL\_AGENT environment variable or use the --model parameter.

7. **Import Errors with Task Bundle**:
   ```
   Error: Failed to import tool registry from example.task.tools
   ```
   Solution: Check that the Python path is correct and the module can be imported.

### Getting Help

For additional help, use the `--help` flag with any command:

```bash  theme={null}
reward-kit --help
reward-kit preview --help
reward-kit deploy --help
reward-kit agent-eval --help
```

## Next Steps

* Explore the [Developer Guide](/evaluators/developer_guide/getting_started) for conceptual understanding
* Try the [Creating Your First Reward Function](/evaluators/tutorials/creating_your_first_reward_function) tutorial
* Learn about [Agent Evaluation](/evaluators/developer_guide/agent_evaluation) to create your own task bundles
* See [Examples](/evaluators/examples/basic_examples/basic_reward_function) for practical implementations


# null
Source: https://docs.fireworks.ai/evaluators/developer_guide/agent_evaluation



# Agent Evaluation Framework

The Agent Evaluation Framework allows you to evaluate agent models with tool-augmented reasoning using "Task Bundles" - self-contained directories that include all the necessary components for testing and evaluation.

## Task Bundle Structure

A task bundle is a self-contained directory with all the components needed to evaluate an agent:

```
my_task/
├─ reward.py           # Reward function with @reward_function decorator
├─ tools.py            # Tool registry for this specific task
├─ seed.sql            # Initial DB state (optional)
└─ task.jsonl          # Dataset rows with task specifications
```

## CLI Usage

The agent evaluation framework is integrated with the Reward Kit CLI through the `agent-eval` command.

### Basic Usage

```bash  theme={null}
# Run agent evaluation on a task bundle
reward-kit agent-eval --task-dir ./flight_task

# You can also specify just the task.jsonl file
reward-kit agent-eval --dataset ./flight_task/task.jsonl
```

### Environment Variables

Models can be specified using environment variables:

```bash  theme={null}
# Set model for agent evaluation
export MODEL_AGENT=openai/gpt-4o

# Set model for simulated user (optional)
export MODEL_SIM=openai/gpt-3.5-turbo

# Then run evaluation
reward-kit agent-eval --task-dir ./flight_task
```

### Advanced Options

```bash  theme={null}
# Specify model directly (overrides environment variable)
reward-kit agent-eval --task-dir ./flight_task --model openai/gpt-4o

# Use custom output directory
reward-kit agent-eval --task-dir ./flight_task --output-dir ./my_runs

# Disable simulated user (use static initial messages only)
reward-kit agent-eval --task-dir ./flight_task --no-sim-user

# Use test mode without requiring API keys
reward-kit agent-eval --task-dir ./flight_task --test-mode

# Use mock response in test mode
reward-kit agent-eval --task-dir ./flight_task --test-mode --mock-response

# Run in debug mode with verbose output
reward-kit agent-eval --task-dir ./flight_task --debug

# Limit the number of tasks to evaluate
reward-kit agent-eval --task-dir ./flight_task --max-tasks 2

# Run specific tasks by ID
reward-kit agent-eval --task-dir ./flight_task --task-ids flight.booking.001,flight.booking.002

# Use a specific registry for a task
reward-kit agent-eval --task-dir ./flight_task --registry-override my_custom_tools.flight_tools

# Use multiple tool registries
reward-kit agent-eval --task-dir ./complex_task --registries flight=flight_tools,hotel=hotel_tools

# Specify evaluator
reward-kit agent-eval --task-dir ./flight_task --evaluator flight_reward.success_evaluator
```

## Testing & Debugging

The CLI provides several options for testing and debugging:

```bash  theme={null}
# Test mode verifies tool setup without making API calls
reward-kit agent-eval --task-dir ./flight_task --test-mode

# Debug mode shows detailed information about tool execution
reward-kit agent-eval --task-dir ./flight_task --debug

# Export tools as OpenAPI spec for manual testing
reward-kit agent-eval --task-dir ./flight_task --export-tools ./tools_spec

# Validate task bundle structure and requirements
reward-kit agent-eval --task-dir ./flight_task --validate-only
```

## Examples

### Basic Flight Task Evaluation

```bash  theme={null}
export MODEL_AGENT=openai/gpt-4o
reward-kit agent-eval --task-dir ./examples/flight_task
```

### Testing Without API Keys

```bash  theme={null}
reward-kit agent-eval --task-dir ./examples/flight_task --test-mode --mock-response
```

### Complex Task with Multiple Tool Registries

```bash  theme={null}
reward-kit agent-eval --task-dir ./examples/travel_task --registries flight=flight_tools,hotel=hotel_tools
```

### Running with Specific Task IDs

```bash  theme={null}
reward-kit agent-eval --task-dir ./examples/flight_task --task-ids flight.booking.001,flight.booking.002
```

### Using Debug Mode

```bash  theme={null}
reward-kit agent-eval --task-dir ./examples/flight_task --debug
```


# null
Source: https://docs.fireworks.ai/evaluators/developer_guide/core_data_types



# Core Data Types

This guide explains the primary data types used in the Reward Kit, including the input and output structures for reward functions.

## Overview

The Reward Kit uses several core data types to represent:

* Conversation messages
* Evaluation results
* Component metrics

Understanding these types is crucial for creating effective reward functions.

## Message Types

### The `Message` Class

```python  theme={null}
from reward_kit import Message

message = Message(
    role="assistant",
    content="This is the response content",
    name=None,  # Optional
    tool_call_id=None,  # Optional, for tool calling
    tool_calls=None,  # Optional, for tool calling
    function_call=None  # Optional, for function calling
)
```

The `Message` class represents a single message in a conversation and is compatible with the OpenAI message format.

### Message Dictionary Format

When working with reward functions, messages are often passed as dictionaries:

```python  theme={null}
message_dict = {
    "role": "assistant",
    "content": "This is the response content"
}
```

The minimum required fields are:

* `role`: The sender of the message (`"user"`, `"assistant"`, or `"system"`)
* `content`: The text content of the message

Additional fields for function/tool calling may include:

* `name`: Name of the sender (for named system messages)
* `tool_calls`: Tool call information
* `function_call`: Function call information (legacy format)

## Evaluation Output Types

### `EvaluateResult` Class

```python  theme={null}
from reward_kit import EvaluateResult, MetricResult

result = EvaluateResult(
    score=0.75,  # Overall score between 0.0 and 1.0
    reason="The response meets quality requirements",  # Optional explanation
    metrics={    # Component metrics dictionary
        "clarity": MetricResult(
            success=True,
            score=0.8,
            reason="The response is clear and concise"
        ),
        "accuracy": MetricResult(
            score=0.7,
            reason="Contains one minor factual error",
            success=True
        )
    }
)
```

The `EvaluateResult` class represents the complete result of a reward function evaluation, containing:

* An overall score (typically 0.0 to 1.0)
* An optional reason/explanation for the overall score
* A dictionary of component metrics
* An optional error field for handling evaluation failures

### `MetricResult` Class

```python  theme={null}
from reward_kit import MetricResult

metric = MetricResult(
    score=0.8,  # Score for this specific metric
    reason="Explanation for why this score was assigned",  # Description
    success=True  # Indicates if the metric condition was met (e.g., pass/fail)
)
```

The `MetricResult` class represents a single component metric in the evaluation, containing:

* A score value (typically 0.0 to 1.0)
* A reason/explanation for the score
* A `success: bool` flag indicating if the metric condition was met (e.g., pass/fail).

### Removed Output Types (Legacy)

The `RewardOutput` and `MetricRewardOutput` classes were used in older versions but have now been fully removed. All reward functions should now use `EvaluateResult` and `MetricResult`.

If you are migrating from an older version that used `RewardOutput`, please refer to the "Migration from RewardOutput to EvaluateResult" section below.

## Using Types in Reward Functions

Here's how to use these types properly in your reward functions:

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult, Message
from typing import List, Optional, Dict, Any

@reward_function
def my_reward_function(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    **kwargs
) -> EvaluateResult:
    """
    Example reward function with proper type annotations.
    """
    # Default values
    metadata = metadata or {}

    # Get the assistant's response
    response = messages[-1].get("content", "")

    # Evaluate the response
    clarity_score = evaluate_clarity(response)

    # Create metrics
    metrics = {
        "clarity": MetricResult(
            score=clarity_score,
            reason=f"Clarity score: {clarity_score:.2f}",
            success=clarity_score >= 0.7
        )
    }

    return EvaluateResult(
        score=clarity_score,
        reason=f"Overall quality assessment: {clarity_score:.2f}",
        metrics=metrics
    )
```

## Best Practices for Data Types

1. **Use EvaluateResult**: Always return EvaluateResult from your reward functions
2. **Use Type Hints**: Include proper type annotations in your functions
3. **Provide Reasons**: Include clear reason strings for both overall score and individual metrics
4. **Use `success`**: Set the `success: bool` flag in `MetricResult` to indicate pass/fail or whether a specific condition for that metric was met.
5. **Default Values**: Provide defaults for optional parameters
6. **Validation**: Validate input data before processing
7. **Error Handling**: Handle missing or malformed data gracefully
8. **Documentation**: Document the expected format for your inputs and outputs

## Migration from RewardOutput to EvaluateResult

If you have existing code using RewardOutput, here's how to migrate to EvaluateResult:

```python  theme={null}
# Old code (deprecated)
@reward_function
def my_reward(messages, **kwargs):
    # ...
    return RewardOutput(
        score=0.75,
        metrics={
            "clarity": MetricRewardOutput(score=0.8, reason="Clear explanation")
        }
    )

# New code (preferred)
@reward_function
def my_reward(messages, **kwargs):
    # ...
    return EvaluateResult(
        score=0.75,
        reason="Overall assessment",  # Add an overall reason
        metrics={
            "clarity": MetricResult(
                score=0.8,
                reason="Clear explanation",
                success=True  # Add success flag if applicable
            )
        }
    )
```

## Next Steps

Now that you understand the core data types:

1. Learn about [Evaluation Workflows](/evaluators/developer_guide/evaluation_workflows) for testing and deploying your functions
2. Explore [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions) to see these types in action
3. Check the [API Reference](/evaluators/api_reference/data_models) for complete details on all data types


# null
Source: https://docs.fireworks.ai/evaluators/developer_guide/evaluation_workflows



# Evaluation Workflows

This guide explains the lifecycle of developing, testing, and deploying reward functions and evaluation setups within the Reward Kit.

## Development Workflow Overview

The typical workflow involves:

1. **Dataset Configuration**: Defining how your data is loaded and prepared (see [Dataset Configuration Guide](/evaluators/developer_guide/dataset_configuration_guide)).
2. **Reward Function Implementation**: Writing the logic to evaluate model responses.
3. **Local Evaluation (using `reward-kit run`)**: Running evaluations locally using Hydra-based configurations to generate responses and score them.
4. **Previewing Results (using `reward-kit preview`)**: Inspecting or re-evaluating generated outputs.
5. **Deployment**: Making the reward function or evaluator available as a service.
6. **Integration**: Using the deployed evaluator in RLHF training or other workflows.

## 1. Dataset Configuration

Before evaluation, you need to configure your dataset. This involves setting up YAML files (typically in `conf/dataset/` or an example's `conf/dataset/` directory) to define how raw data is sourced, processed, and formatted (e.g., adding system prompts).

Refer to the [Dataset Configuration Guide](/evaluators/developer_guide/dataset_configuration_guide) for detailed instructions.

## 2. Reward Function Implementation

Create your reward function using the `@reward_function` decorator or by structuring your evaluation logic within a script that can be called by an evaluation configuration.

### Example: Basic Reward Function

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def helpfulness_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    """Evaluate the helpfulness of a response."""
    # Get the assistant's response
    response_content = messages[-1].get("content", "").lower()

    # Define helpful keywords
    helpful_keywords = ["help", "assist", "solve", "solution", "answer", "explain"]

    # Count helpful keywords
    keyword_count = sum(1 for keyword in helpful_keywords if keyword in response_content)

    # Calculate score based on keyword presence (simple example)
    score = min(keyword_count / 3.0, 1.0)  # Cap at 1.0
    success = keyword_count > 0 # Example success condition

    return EvaluateResult(
        score=score,
        reason=f"Helpfulness evaluation based on {keyword_count} keywords.",
        metrics={
            "helpfulness": MetricResult(
                score=score,
                success=success,
                reason=f"Found {keyword_count} helpful keywords"
            )
        }
    )
```

This function can then be referenced in your evaluation configuration.

## 3. Local Evaluation with `reward-kit run`

The primary method for running local evaluations is the `reward-kit run` CLI command, which uses Hydra for configuration. This command handles generating model responses (if needed) and evaluating them according to your specified dataset and reward logic.

### Setting up the Configuration

You'll need a main evaluation configuration YAML file (e.g., `run_my_eval.yaml`) that specifies:

* The dataset to use (referencing configurations from `conf/dataset/`).
* Model generation parameters (model name, API keys, etc.).
* The reward function or evaluation script to use.
* Other evaluation parameters (e.g., sample limits).

Refer to the [Hydra Configuration for Examples](/evaluators/developer_guide/hydra_configuration) guide and specific examples like `examples/math_example/conf/run_math_eval.yaml`.

### Running the Evaluation

```bash  theme={null}
# Activate virtual environment
source .venv/bin/activate

# Run evaluation using reward-kit run
python -m reward_kit.cli run \
  --config-path ./path/to/your/example/conf \
  --config-name run_my_eval.yaml \
  evaluation_params.limit_samples=50 # Example override
```

This command will:

* Load the dataset as per your configuration.
* Generate responses from the specified model.
* Apply the configured reward function(s).
* Save detailed results (e.g., `run_my_eval_results.jsonl`) and prompt/response pairs (e.g., `preview_input_output_pairs.jsonl`) to a timestamped output directory (usually under `outputs/`).

## 4. Previewing and Analyzing Results

After a `reward-kit run`, you can use `reward-kit preview` to inspect the generated `preview_input_output_pairs.jsonl` or re-evaluate them with different/updated metrics.

### Using the CLI for Preview

```bash  theme={null}
# Preview the outputs of a previous run
reward-kit preview \
  --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
  --metrics-folders "new_metric=./path/to/new_metric_script"
  # Or --remote-url <your_deployed_evaluator_url>
```

This is useful for iterating on reward functions or comparing different evaluation approaches on the same set of generated responses.

### Programmatic Analysis

You can also load the `*.jsonl` result files programmatically (e.g., with Pandas) for custom analysis, plotting, or reporting.

## 5. Deployment

Once your reward function is developed and tested locally, you can deploy it as an evaluator. The primary methods are using the `deploy()` method on a reward function object or the `reward-kit deploy` CLI command.

### Using the `deploy()` Method (Programmatic)

If you have a reward function object (created with `@reward_function`), you can deploy it directly:

```python  theme={null}
# Assuming 'helpfulness_reward' is your @reward_function decorated function
evaluation_id = helpfulness_reward.deploy(
    name="helpfulness-evaluator", # This will be the evaluator_id
    description="Evaluates the helpfulness of responses",
    force=True  # Overwrite if an evaluator with this name already exists
)

print(f"Deployed helpfulness evaluator with ID: {evaluation_id}")
```

You can also specify providers if needed:

```python  theme={null}
custom_evaluation_id = helpfulness_reward.deploy(
    name="helpfulness-evaluator-anthropic",
    description="Helpfulness evaluation using Claude model",
    force=True,
    providers=[
        {
            "providerType": "anthropic",
            "modelId": "claude-3-sonnet-20240229"
        }
    ]
)
print(f"Deployed custom provider evaluator: {custom_evaluation_id}")
```

### Using the CLI (`reward-kit deploy`)

The `reward-kit deploy` command is suitable for deploying reward functions defined in script files. The `--metrics-folders` argument should point to the directory containing your reward function script (e.g., a `main.py` with the `@reward_function` decorator).

```bash  theme={null}
# Deploy with the CLI
reward-kit deploy \
  --id helpfulness-evaluator \
  --metrics-folders "helpfulness=./path/to/your/metric_script_directory" \
  --display-name "Helpfulness Evaluator" \
  --description "Evaluates the helpfulness of responses" \
  --force
```

For more details on `reward-kit deploy`, see the [CLI Reference](/evaluators/cli_reference/cli_overview).

### Lower-level `create_evaluation` Function

For more direct control, or if not using the `@reward_function` decorator's `deploy` method, you can use the `create_evaluation` function from `reward_kit.evaluation`. This is generally for more advanced use cases or internal tooling.

```python  theme={null}
from reward_kit.evaluation import create_evaluation

# Create an evaluation
evaluator = create_evaluation(
    evaluator_id="helpfulness-evaluator-low-level",
    metric_folders=["helpfulness=./path/to/your/metric_script_directory"], # Note: path to directory
    display_name="Helpfulness Evaluator (Low-Level)",
    description="Evaluates the helpfulness of responses, created via create_evaluation",
    force=True
)

print(f"Created evaluator: {evaluator['name']}")
```

## 6. Integration with Training

### Using in an RL Training Job

Once deployed, use the evaluator in an RL training job:

```bash  theme={null}
# Example of using the evaluator in a Fireworks RL job
firectl create rl-job \
  --reward-endpoint "https://api.fireworks.ai/v1/evaluations/helpfulness-evaluator" \
  --model-id "accounts/fireworks/models/llama-v3-8b-instruct" \
  --dataset-id "my-training-dataset"
```

### Programmatic Integration with TRL

For programmatic integration with the Transformer Reinforcement Learning (TRL) library:

```python  theme={null}
from reward_kit import RewardFunction

# Create a reward function instance
reward_fn = RewardFunction(
    name="helpfulness-evaluator",
    mode="remote"  # Use the deployed evaluator
)

# Get a TRL-compatible adapter
trl_reward_fn = reward_fn.get_trl_adapter()

# Use in your TRL training pipeline
# ...
```

## 7. Best Practices

1. **Iterative Development**: Start simple, test thoroughly, and refine your reward function. Use `reward-kit run` and `reward-kit preview` extensively.
2. **Version Control**: Use version control for your reward functions, configurations, and datasets.
3. **Sample Diversity**: Test with a diverse set of samples to ensure robustness.
4. **Documentation**: Document the behavior and assumptions of your reward function.
5. **Error Handling**: Include robust error handling in your reward logic to prevent evaluation failures.
6. **Logging**: Add detailed logging within your reward functions for easier debugging.

## Next Steps

Now that you understand the complete workflow:

1. Try creating a [Basic Reward Function](/evaluators/examples/basic_examples/basic_reward_function)
2. Explore [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions) with multiple metrics


# null
Source: https://docs.fireworks.ai/evaluators/developer_guide/getting_started



# Getting Started with Reward Functions

This guide will help you understand the basics of creating, testing, and deploying reward functions using the Reward Kit.

## What is a Reward Function?

A reward function is a mechanism for evaluating the quality of model outputs in reinforcement learning from verifiable reward (RLVR) workflows. Reward functions help:

* Evaluate model responses based on specific criteria.
* Provide numerical scores that can be used to optimize models.
* Offer explanations for why specific scores were assigned.

## Installation

To get started with Reward Kit, install it via pip:

```bash  theme={null}
pip install reward-kit
```

For development, including running all examples and contributing to the codebase, install it in editable mode with development dependencies:

```bash  theme={null}
git clone https://github.com/fw-ai-external/reward-kit.git # Or your fork
cd reward-kit
pip install -e ".[dev]"
```

## Authentication Setup

To use Reward Kit with the Fireworks AI platform, set up your authentication credentials:

```bash  theme={null}
# Set your API key
export FIREWORKS_API_KEY=your_api_key
```

## Basic Reward Function Structure

Here's a simple reward function that evaluates responses based on word count:

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def word_count_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    """
    Evaluate a response based on its word count.

    Args:
        messages: List of conversation messages
        original_messages: Original messages (usually without the response being evaluated)
        **kwargs: Additional parameters

    Returns:
        EvaluateResult with score and metrics information
    """
    # Get the assistant's response (last message)
    if not messages or messages[-1].get("role") != "assistant":
        return EvaluateResult(
            score=0.0,
            reason="No assistant response found in messages.",
            metrics={"error": MetricResult(score=0.0, success=False, reason="No assistant response found")}
        )

    response = messages[-1].get("content", "")

    # Count words and calculate score
    word_count = len(response.split())
    score = min(word_count / 100.0, 1.0)  # Cap at 1.0
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

## Testing and Evaluating

There are several ways to test your reward functions and run evaluations:

### Programmatic Testing (for individual functions)

You can test your reward function directly in Python with sample conversations:

```python  theme={null}
# Sample conversation
test_messages = [
    {"role": "user", "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is a method of data analysis that automates analytical model building."}
]

# Test the reward function
result = word_count_reward(messages=test_messages)
print(f"Score: {result.score}")
print(f"Explanation: {result.metrics['word_count'].reason}")
```

### Local Evaluation with `reward-kit run` (Recommended for datasets/examples)

For evaluating datasets or running complete examples, the primary method is the `reward-kit run` CLI command. This uses [Hydra for configuration](/evaluators/developer_guide/hydra_configuration), allowing you to define your dataset, model, and reward logic in YAML files.

1. **Explore Examples**: Check out the examples in the `examples/` directory at the root of the repository. The [main Examples README](https://github.com/fw-ai-external/reward-kit/blob/main/examples/README.md) provides an overview and guidance on their structure. Each example (e.g., `examples/math_example/`) has its own README explaining how to run it.

2. **Run an Example**:
   ```bash  theme={null}
   # Example: Running the math_example
   python -m reward_kit.cli run \
     --config-path examples/math_example/conf \
     --config-name run_math_eval.yaml
   ```
   This command processes the dataset, generates model responses, applies reward functions, and saves detailed results.

### Previewing Evaluation Outputs with `reward-kit preview`

After running an evaluation with `reward-kit run`, a `preview_input_output_pairs.jsonl` file is typically generated in the output directory. You can use `reward-kit preview` to inspect these pairs or re-evaluate them with different metrics:

```bash  theme={null}
# Preview outputs from a previous run
reward-kit preview \
  --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
  --metrics-folders "your_metric_name=./path/to/your_metric_script"
```

Refer to the [Evaluation Workflows guide](/evaluators/developer_guide/evaluation_workflows) for a more detailed lifecycle overview.

## Deploying Your Reward Function

When you're ready, deploy your reward function to use in training workflows:

```python  theme={null}
# Deploy programmatically
evaluator_id = word_count_reward.deploy(
    name="word-count-evaluator",
    description="Evaluates responses based on word count"
)
print(f"Deployed with ID: {evaluator_id}")
```

Or using the CLI:

```bash  theme={null}
reward-kit deploy --id word-count-evaluator --metrics-folders "word_count=./path/to/metric" --force
```

## Next Steps

Now that you have an overview of getting started:

1. Dive deeper into [Reward Function Anatomy](/evaluators/developer_guide/reward_function_anatomy).
2. Understand the [Core Data Types](/evaluators/developer_guide/core_data_types) used in Reward Kit.
3. Explore the [Evaluation Workflows](/evaluators/developer_guide/evaluation_workflows) in more detail.
4. Browse the [Examples Overview](/evaluators/examples/examples_overview) and the main [Examples README](https://github.com/fw-ai-external/reward-kit/blob/main/examples/README.md) to find practical implementations.
5. Follow our [step-by-step tutorial](/evaluators/tutorials/creating_your_first_reward_function) for a hands-on walkthrough.


# null
Source: https://docs.fireworks.ai/evaluators/developer_guide/reward_function_anatomy



# Reward Function Anatomy

This guide provides a detailed explanation of how reward functions are structured in the Reward Kit, focusing on the `@reward_function` decorator and the components that make up a complete reward function.

## The `@reward_function` Decorator

The `@reward_function` decorator is the core mechanism that transforms a regular Python function into a reward function that can be used for evaluation and deployment.

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult

@reward_function
def my_reward_function(messages, original_messages=None, **kwargs):
    # Your evaluation logic here
    score = 0.75 # Example score
    reason = "Overall evaluation reason for my_reward_function"
    metrics_dict = {"example_metric": MetricResult(score=score, success=True, reason="Metric reason")}
    return EvaluateResult(score=score, reason=reason, metrics=metrics_dict)
```

### What the Decorator Does

The `@reward_function` decorator performs several important functions:

1. **Input Validation**: Ensures the function receives the expected parameters
2. **Output Standardization**: Ensures the function returns a properly formatted `EvaluateResult` object
3. **Deployment Capability**: Adds a `.deploy()` method to the function for easy deployment
4. **Backward Compatibility**: Handles legacy return formats (tuples of score and metrics)

### Under the Hood

Internally, the decorator wraps your function with logic that:

1. Processes the input parameters
2. Calls your function with the standardized inputs
3. Handles any exceptions that occur during execution
4. Formats the output as an `EvaluateResult` object
5. Provides deployment capabilities through the `.deploy()` method

## Function Parameters

A standard reward function has these parameters:

```python  theme={null}
from typing import List, Dict, Optional
from reward_kit import EvaluateResult

def reward_function(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    # ...
    pass
```

### Required Parameters

* **`messages`**: A list of message dictionaries in the conversation, where each message has at least `"role"` and `"content"` keys. The last message is typically the one being evaluated.

### Optional Parameters

* **`original_messages`**: The conversation context, usually messages before the response being evaluated. If not provided, it defaults to `messages[:-1]`.
* **`**kwargs`**: Additional parameters that can be used to customize the evaluation.

## Return Value

A reward function must return an `EvaluateResult` object:

```python  theme={null}
from reward_kit import EvaluateResult, MetricResult

# score, clarity_score, accuracy_score would be calculated by your logic
clarity_score = 0.8
accuracy_score = 0.7
final_score = 0.75

return EvaluateResult(
    score=final_score,  # Overall score between 0.0 and 1.0
    reason="Overall evaluation based on clarity and accuracy.",
    metrics={    # Component metrics
        "clarity": MetricResult(
            score=clarity_score,
            success=clarity_score >= 0.7,
            reason="The response clearly explains the concept"
        ),
        "accuracy": MetricResult(
            score=accuracy_score,
            success=accuracy_score >= 0.6,
            reason="Contains one minor factual error"
        )
    }
)
```

### EvaluateResult Structure

* **`score`**: The final aggregate score (typically between 0.0 and 1.0).
* **`reason`**: An optional top-level explanation for the overall score.
* **`metrics`**: A dictionary of component metrics (`MetricResult` objects), each with its own score, success flag, and explanation.
* **`error`**: An optional string field to convey errors during evaluation.

## Multi-Component Reward Functions

Complex reward functions often evaluate multiple aspects of a response:

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

# Assume evaluate_clarity and evaluate_accuracy are defined elsewhere
def evaluate_clarity(response: str) -> float: return 0.8
def evaluate_accuracy(response: str) -> float: return 0.6


@reward_function
def comprehensive_evaluation(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    response = messages[-1]["content"]
    metrics = {}

    # Evaluate clarity
    clarity_score = evaluate_clarity(response)
    metrics["clarity"] = MetricResult(
        score=clarity_score,
        success=clarity_score >= 0.7,
        reason=f"Clarity score: {clarity_score:.2f}"
    )

    # Evaluate accuracy
    accuracy_score = evaluate_accuracy(response)
    metrics["accuracy"] = MetricResult(
        score=accuracy_score,
        success=accuracy_score >= 0.6,
        reason=f"Accuracy score: {accuracy_score:.2f}"
    )

    # Combine scores (weighted average)
    final_score = clarity_score * 0.4 + accuracy_score * 0.6

    return EvaluateResult(score=final_score, reason="Comprehensive evaluation complete.", metrics=metrics)
```

## Deployment Capabilities

The `@reward_function` decorator adds a `.deploy()` method to your function:

```python  theme={null}
# Assume my_reward_function is defined as above
# Deploy the function to Fireworks
evaluation_id = my_reward_function.deploy(
    name="my-evaluator",
    description="Evaluates responses based on custom criteria",
    force=True  # Overwrite if already exists
)
```

### Deploy Method Parameters

* **`name`**: ID for the deployed evaluator (required)
* **`description`**: Human-readable description (optional)
* **`force`**: Whether to overwrite an existing evaluator with the same name (optional)
* **`providers`**: List of model providers to use for evaluation (optional)

## Error Handling

Robust reward functions include proper error handling:

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def safe_evaluation(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    try:
        # Ensure we have a valid response to evaluate
        if not messages or messages[-1].get("role") != "assistant":
            return EvaluateResult(
                score=0.0,
                reason="No assistant response found.",
                metrics={"error": MetricResult(
                    score=0.0,
                    success=False,
                    reason="No assistant response found"
                )}
            )

        # Your evaluation logic here
        # ...
        # For example:
        calculated_score = 0.0 # Placeholder for actual logic
        if calculated_score == 0 : raise ValueError("Simulated error")
        return EvaluateResult(score=1.0, reason="Successful evaluation", metrics={})


    except Exception as e:
        # Handle any unexpected errors
        return EvaluateResult(
            score=0.0,
            reason=f"Evaluation error: {str(e)}",
            metrics={"error": MetricResult(
                score=0.0,
                success=False,
                reason=f"Evaluation error: {str(e)}"
            )}
        )
```

## Working with Metadata

You can pass additional configuration through the `**kwargs` parameter, often via a `metadata` dictionary.

```python  theme={null}
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional, Any

# Assume base_score and metrics are calculated based on messages
def calculate_base_score_and_metrics(response_content: str, min_length: int) -> tuple[float, dict]:
    # Dummy implementation
    current_length = len(response_content)
    score = 1.0 if current_length >= min_length else 0.5
    return score, {"length_check": MetricResult(score=score, success=current_length >= min_length, reason=f"Length {current_length} vs min {min_length}")}

@reward_function
def configurable_evaluation(
    messages: List[Dict[str, str]], # Added type hints
    original_messages: Optional[List[Dict[str, str]]] = None, # Added type hints
    metadata: Optional[Dict[str, Any]] = None,
    **kwargs
) -> EvaluateResult:
    """Reward function that supports configuration via metadata."""
    metadata = metadata or {}
    response_content = messages[-1].get("content", "")

    # Get configurable thresholds from metadata
    min_length = metadata.get("min_length", 50)
    max_score_cap = metadata.get("max_score_cap", 1.0) # Renamed to avoid conflict with 'score'
    weight_factor = metadata.get("weight_factor", 1.0)

    # Use these parameters in your evaluation
    base_score, metrics = calculate_base_score_and_metrics(response_content, min_length)

    # Apply any metadata-based adjustments to the final score
    final_score = base_score * weight_factor
    final_score = min(final_score, max_score_cap) # Cap the score

    return EvaluateResult(score=final_score, reason="Configurable evaluation complete.", metrics=metrics)
```

When calling the function, you can pass this metadata:

```python  theme={null}
# Assume test_messages is defined
# result = configurable_evaluation(
#     messages=test_messages,
#     metadata={"min_length": 100, "weight_factor": 1.2}
# )
```

## Next Steps

Now that you understand the structure of reward functions:

1. Learn about the [Core Data Types](/evaluators/developer_guide/core_data_types) used in reward functions
2. Explore [Evaluation Workflows](/evaluators/developer_guide/evaluation_workflows) for testing and deployment
3. See [Code Examples](/evaluators/examples/basic_examples/basic_reward_function) for practical implementations


# Using Secrets
Source: https://docs.fireworks.ai/evaluators/developer_guide/using_secrets

Learn how to create secrets that can be utilized within your reward function.

# Creating Secrets

<Steps>
  <Step title="Navigate to the secrets page on your dashboard">
        <img src="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=5a5a1f8a626c6e678d22a44addde7fc5" alt="new.png" data-og-width="1540" width="1540" data-og-height="1106" height="1106" data-path="images/new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=280&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=fad25753520447ffdbb63182fc92d194 280w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=560&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=ed05cd99096aa33925c989fc19157402 560w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=840&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=bcc4928202a856b5a0d8593dfce2d5e8 840w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=1100&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=bc5a42177b80825f9d73531180c34088 1100w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=1650&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=7e78b4e3c90000837e7967da461cd13a 1650w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/new.png?w=2500&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=d279764c7f5a0b7c4f94bc853fb19950 2500w" />
  </Step>

  <Step title="Create a new secret">
        <img src="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=5b398ccbb320787377d235b9114bdc8d" alt="test.png" data-og-width="1826" width="1826" data-og-height="964" height="964" data-path="images/test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=280&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=23ec9e053dfaccbac993cf5554db0c5e 280w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=560&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=87d4aa204ceee34d9b2bb7826a7786b8 560w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=840&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=98ed857288a080843053ecc42d52b809 840w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=1100&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=2342b7078b857409fa37724cd0e9ac92 1100w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=1650&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=b8653468aa02bb04f0c7621ec1d13f40 1650w, https://mintcdn.com/fireworksai/TqcPkwdC20F1W6ZY/images/test.png?w=2500&fit=max&auto=format&n=TqcPkwdC20F1W6ZY&q=85&s=f47a1dd88880fa5976571540f91478d0 2500w" />

    All secrets created here will be injected as environment variables for your Evaluator to access.
  </Step>

  <Step title="Update the Evaluator to access the new secret">
    <img src="https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=361f2aaad5c4db9f675c8c976bb2a8b0" alt="llm-judge-w-secret-example.png" data-og-width="1532" width="1532" data-og-height="1590" height="1590" data-path="evaluators/developer_guide/images/llm-judge-w-secret-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=280&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=d6b821591273d52965c0cb2cb81e71d1 280w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=560&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=9bc6628ccdc7b629942e98a84f2c3ac1 560w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=840&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=f5f2ba98695daf6da69d6b8fcb812cac 840w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=1100&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=c7509aadebfa1aff99b72aebb6fcd20d 1100w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=1650&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=d09e34ac5e5abcd720cd2d0c50dc0797 1650w, https://mintcdn.com/fireworksai/kZCV7UvEi6F9hwE9/evaluators/developer_guide/images/llm-judge-w-secret-example.png?w=2500&fit=max&auto=format&n=kZCV7UvEi6F9hwE9&q=85&s=3059f16a9eede3714ce3dfd15c1d7276 2500w" />
    See [LLM as a judge](/evaluators/examples/advanced_examples/advanced_reward_functions#llm-as-a-judge) section for full code example
  </Step>
</Steps>

And that's it! If you want to learn more about creating evaluators, see:

1. Learn about [Evaluation Workflows](/evaluators/developer_guide/evaluation_workflows) for testing and deploying your functions
2. Explore [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions) to see these types in action
3. Check the [API Reference](/evaluators/api_reference/data_models) for complete details on all data types


# null
Source: https://docs.fireworks.ai/evaluators/documentation_home



# Reward Kit Documentation

Welcome to the Reward Kit documentation. This guide will help you create, test, and deploy reward functions for evaluating and optimizing LLM responses.

<img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=281cbbddc5b8c24940baa04f8d1eec64" alt="image" data-og-width="3322" width="3322" data-og-height="1862" height="1862" data-path="evaluators/main_screen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d8a3e084c3799519ae2f987cbbe348ca 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=949951534ddb753c28763bfbadc74704 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=ddbe1524ce29a9de56f097b302893345 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3a3ff3daf07ed9a53264ddf0006af5ab 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=6b1fade7a0b7d3ad2ca96e5abbed07e5 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/evaluators/main_screen.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=56d0a3e7e8522629ad5e0cdbac024045 2500w" />

## Getting Started

### Developer Guide

* [Getting Started with Reward Functions](/evaluators/developer_guide/getting_started): Learn the basics of reward functions.
* [Reward Function Anatomy](/evaluators/developer_guide/reward_function_anatomy): Understand the structure of reward functions.
* [Core Data Types](/evaluators/developer_guide/core_data_types): Explore the data models used in reward functions.
* [Evaluation Workflows](/evaluators/developer_guide/evaluation_workflows): Learn the complete lifecycle from development to deployment.
* [Dataset Configuration Guide](/evaluators/developer_guide/dataset_configuration_guide): Understand how to configure datasets using YAML.
* [Hydra Configuration for Examples](/evaluators/developer_guide/hydra_configuration): Learn how Hydra is used for configuration in examples.
* [Integrating with Braintrust](/evaluators/integrations/braintrust_integration): Bridge Reward Kit with the Braintrust SDK.

### Examples

* [Examples Overview](/evaluators/examples/examples_overview): Browse available examples and learn how to run them. The primary documentation for each example is its own `README.md` in the `examples/` directory.

### Tutorials

* [Creating Your First Reward Function](/evaluators/tutorials/creating_your_first_reward_function): Step-by-step guide to creating a reward function

## API Reference

* [API Overview](/evaluators/api_reference/api_overview)
* [RewardFunction Class](/evaluators/api_reference/reward_function_class)
* [Reward Function Decorator](/evaluators/api_reference/reward_function_decorator)
* [Data Models](/evaluators/api_reference/data_models)

## Command Line Interface

* [CLI Overview](/evaluators/cli_reference/cli_overview)

## Community and Support

* GitHub Issues: Report bugs and request features
* Contributing Guide: How to contribute to the Reward Kit project


# null
Source: https://docs.fireworks.ai/evaluators/examples/accuracy_length/accuracy_length_overview



# Accuracy + Length Reward Examples

This directory contains examples demonstrating the use of combined accuracy and length-based reward functions.

## Overview

These examples show how to use the `cosine_scaled_accuracy_length_reward` function to evaluate model responses based on both:

1. Accuracy (correctness of the answer)
2. Length efficiency (brevity of the response)

This combined approach rewards responses that are both accurate and concise, penalizing verbosity in correct answers and providing a clear separation between correct and incorrect responses.

**Note**: The accuracy detection depends on specific text-extraction mechanisms that may need customization for different types of content using the `extract_fn` and `compare_fn` parameters.

## Examples

### Cosine-Scaled Accuracy + Length Example

The [cosine\_scaled\_example.py](https://github.com/fw-ai-external/reward-kit/blob/main/examples/accuracy_length/cosine_scaled_example.py) script demonstrates the reward function's behavior with different types of responses:

* Short correct answers (highest score)
* Long correct answers (moderate score)
* Short incorrect answers (very low score)
* Long incorrect answers (low score, but still penalized for being wrong)

It also shows how to customize the weighting between accuracy and length components.

## Running the Examples

```bash  theme={null}
# Make sure you're in the reward-kit directory
cd /path/to/reward-kit

# Activate the virtual environment
source .venv/bin/activate

# Run the example
python examples/accuracy_length/cosine_scaled_example.py
```

## Expected Output

```
===== Evaluating with Default Parameters =====

Short Correct Answer:
Response (1 words): "Paris..."
Combined Score: 1.00
Accuracy Score: 1.00
Length Score: 1.00

Long Correct Answer:
Response (69 words): "The capital of France is Paris. Paris is located i..."
Combined Score: 0.88
Accuracy Score: 1.00
Length Score: 0.61

Short Incorrect Answer:
Response (1 words): "Lyon..."
Combined Score: 0.00
Accuracy Score: 0.00
Length Score: 0.00

Long Incorrect Answer:
Response (46 words): "I need to identify the capital city of France. Fra..."
Combined Score: 0.04
Accuracy Score: 0.00
Length Score: 0.13

===== Evaluating with Custom Parameters =====

Short Correct Answer (80% accuracy weight, 20% length weight):
Response (1 words): "Paris..."
Combined Score: 1.00
Accuracy Score: 1.00
Length Score: 1.00
```

## Custom Configurations

You can customize the reward function with various parameters:

```python  theme={null}
from reward_kit.rewards.accuracy_length import cosine_scaled_accuracy_length_reward

result = cosine_scaled_accuracy_length_reward(
    messages=messages,
    ground_truth="Expected answer",
    max_length=500,                # Maximum ideal length
    correctness_weight=0.7,        # Weight for accuracy component
    length_weight=0.3,             # Weight for length component
    min_value_correct=0.5,         # Minimum score for correct answers
    max_value_correct=1.0,         # Maximum score for correct answers
    min_value_wrong=0.0,           # Minimum score for wrong answers
    max_value_wrong=0.3,           # Maximum score for wrong answers
    token_method="whitespace"      # Method to count tokens
)
```

## Use Cases

This reward function is particularly useful for:

* Factual QA tasks where concise, correct answers are preferred
* Text summarization evaluation
* Mathematical problem-solving with step-by-step reasoning
* Any task where both accuracy and brevity are important

## Further Reading

For more information, see:

* [Basic Reward Functions](/evaluators/examples/basic_examples/reward_functions_overview)
* [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions)


# null
Source: https://docs.fireworks.ai/evaluators/examples/advanced_examples/advanced_reward_functions



# Advanced Reward Functions

This guide covers advanced patterns and techniques for creating sophisticated reward functions.

## Overview

Advanced reward functions go beyond simple accuracy checks to provide nuanced evaluation that considers multiple factors, context, and domain-specific requirements.

## Multi-Metric Evaluation

Combine multiple evaluation criteria:

```python  theme={null}
from reward_kit import reward_function
from reward_kit.rewards import accuracy, length, format_compliance
import numpy as np

@reward_function
def multi_metric_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Advanced reward function combining accuracy, length, and format compliance.
    """
    # Base accuracy score
    acc_score = accuracy(response, expected_response)

    # Length appropriateness (prefer responses between 50-200 chars)
    len_score = length_appropriateness(response, min_len=50, max_len=200)

    # Format compliance (if response should follow a pattern)
    format_score = check_format_compliance(response)

    # Weighted combination
    weights = [0.6, 0.2, 0.2]  # accuracy, length, format
    scores = [acc_score, len_score, format_score]

    return np.average(scores, weights=weights)

def length_appropriateness(response: str, min_len: int, max_len: int) -> float:
    """Helper function to score length appropriateness."""
    length = len(response)
    if min_len <= length <= max_len:
        return 1.0
    elif length < min_len:
        return max(0.0, length / min_len)
    else:
        return max(0.0, 1.0 - (length - max_len) / max_len)

def check_format_compliance(response: str) -> float:
    """Helper function to check format compliance."""
    # Example: Check if response follows expected structure
    if response.startswith("Answer:") and response.endswith("."):
        return 1.0
    return 0.5
```

## Context-Aware Evaluation

Consider context when evaluating responses:

```python  theme={null}
@reward_function
def context_aware_reward(response: str, expected_response: str, context: dict = None) -> float:
    """
    Reward function that considers context information.
    """
    base_score = accuracy(response, expected_response)

    if context:
        # Adjust score based on difficulty
        difficulty = context.get('difficulty', 'medium')
        if difficulty == 'hard' and base_score > 0.8:
            base_score *= 1.2  # Bonus for hard questions
        elif difficulty == 'easy' and base_score < 0.5:
            base_score *= 0.8  # Penalty for easy questions

        # Consider response time if available
        response_time = context.get('response_time_seconds', 0)
        if response_time > 0:
            # Slight bonus for quick accurate responses
            time_bonus = max(0, (10 - response_time) / 100)
            base_score += time_bonus

    return min(base_score, 1.0)
```

## Domain-Specific Evaluation

Create reward functions tailored to specific domains:

```python  theme={null}
@reward_function
def code_quality_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Evaluates code responses considering multiple quality factors.
    """
    import ast

    score = 0.0

    # Check if code is syntactically valid
    try:
        ast.parse(response)
        score += 0.3  # Syntax correctness
    except SyntaxError:
        return 0.0  # Invalid syntax gets zero score

    # Check for best practices
    if "def " in response:  # Function definition
        score += 0.2

    if "# " in response or '"""' in response:  # Comments/docstrings
        score += 0.1

    # Check for specific patterns
    if "import " in response and "from " in response:
        score += 0.1  # Good import practices

    # Length consideration (not too short, not too long)
    lines = response.split('\n')
    if 5 <= len(lines) <= 50:
        score += 0.1

    # Functional correctness (if test cases available)
    test_cases = kwargs.get('test_cases', [])
    if test_cases:
        correctness_score = evaluate_code_correctness(response, test_cases)
        score += 0.2 * correctness_score

    return min(score, 1.0)

def evaluate_code_correctness(code: str, test_cases: list) -> float:
    """Helper to evaluate code correctness against test cases."""
    # This would implement actual code execution and testing
    # For safety, this is a placeholder
    return 0.8  # Placeholder score
```

## Statistical Evaluation

Use statistical methods for more robust evaluation:

```python  theme={null}
from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

@reward_function
def statistical_similarity_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Uses statistical methods to evaluate response similarity.
    """
    # Convert to numerical representations (e.g., using embeddings)
    response_embedding = get_text_embedding(response)
    expected_embedding = get_text_embedding(expected_response)

    # Cosine similarity
    cos_sim = cosine_similarity([response_embedding], [expected_embedding])[0][0]

    # Pearson correlation (if applicable)
    if len(response_embedding) == len(expected_embedding):
        corr, _ = pearsonr(response_embedding, expected_embedding)
        corr = max(0, corr)  # Only positive correlations
    else:
        corr = 0

    # Combine metrics
    final_score = 0.7 * cos_sim + 0.3 * corr

    return max(0.0, min(1.0, final_score))

def get_text_embedding(text: str) -> np.ndarray:
    """Placeholder for text embedding function."""
    # In practice, use a real embedding model
    return np.random.rand(100)  # Placeholder
```

## Hierarchical Evaluation

Create reward functions with hierarchical evaluation:

```python  theme={null}
@reward_function
def hierarchical_reward(response: str, expected_response: str, **kwargs) -> float:
    """
    Hierarchical evaluation with multiple levels of assessment.
    """
    # Level 1: Basic format validation
    if not basic_format_check(response):
        return 0.0

    # Level 2: Content relevance
    relevance_score = content_relevance(response, expected_response)
    if relevance_score < 0.3:
        return relevance_score * 0.5  # Cap low relevance scores

    # Level 3: Detailed accuracy
    accuracy_score = detailed_accuracy(response, expected_response)

    # Level 4: Style and presentation
    style_score = evaluate_style(response)

    # Weighted combination based on hierarchy
    final_score = (
        0.1 * 1.0 +  # Format passed
        0.3 * relevance_score +
        0.5 * accuracy_score +
        0.1 * style_score
    )

    return final_score

def basic_format_check(response: str) -> bool:
    """Basic format validation."""
    return len(response.strip()) > 0 and len(response) < 10000

def content_relevance(response: str, expected: str) -> float:
    """Evaluate content relevance."""
    # Placeholder for semantic similarity
    common_words = set(response.lower().split()) & set(expected.lower().split())
    return len(common_words) / max(len(set(expected.lower().split())), 1)

def detailed_accuracy(response: str, expected: str) -> float:
    """Detailed accuracy evaluation."""
    return accuracy(response, expected)

def evaluate_style(response: str) -> float:
    """Evaluate writing style and presentation."""
    score = 0.0
    if response[0].isupper():  # Starts with capital
        score += 0.3
    if response.endswith('.'):  # Ends with period
        score += 0.3
    if 10 <= len(response.split()) <= 100:  # Appropriate length
        score += 0.4
    return score
```

## LLM as a judge

Create reward functions with LLM as a judge

```python  theme={null}
from openai import OpenAI 
import os

@reward_function
def evaluate(messages: list[dict], criteria: str = None, **kwargs) -> dict:
    """
    Evaluate the last message in the conversation using GPT-4 as a judge.
    
    Args:
        messages: List of message dicts. The last message is assumed to be the result to evaluate.
        criteria: Optional custom evaluation criteria. If not provided, uses default criteria.
        **kwargs: Additional arguments to pass to the OpenAI API.
    
    Returns:
        dict with 'score' (1-10), 'reasoning', and 'raw_response'
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Extract the conversation history and the result to evaluate
    conversation_history = messages[:-1]
    result_to_evaluate = messages[-1]
    
    # Default evaluation criteria
    if criteria is None:
        criteria = """
Please evaluate the quality of the assistant's response based on:
1. Accuracy: Is the information correct?
2. Helpfulness: Does it address the user's question?
3. Clarity: Is it well-explained and easy to understand?
4. Completeness: Does it cover all necessary aspects?

Provide a score from 1-10 (10 being best) and explain your reasoning.
"""
    
    # Build the judge prompt
    judge_messages = [
        {
            "role": "system",
            "content": "You are an expert evaluator. Your job is to objectively assess the quality of AI assistant responses."
        },
        {
            "role": "user",
            "content": f"""Here is a conversation and a response to evaluate:

CONVERSATION HISTORY:
{format_conversation(conversation_history)}

RESPONSE TO EVALUATE:
{result_to_evaluate['content']}

EVALUATION CRITERIA:
{criteria}

Please respond in the following format:
Score: [1-10]
Reasoning: [Your detailed explanation]
"""
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=judge_messages,
        temperature=kwargs.pop('temperature', 0.3),  # Lower temp for more consistent judging
        **kwargs,
    )
    
    # Parse the response
    judgment_text = response.choices[0].message.content
    score, reasoning = parse_judgment(judgment_text)
    
    return {
        "score": score,
        "reasoning": reasoning,
        "raw_response": judgment_text,
        "usage": response.usage.model_dump() if response.usage else None
    }


def format_conversation(messages: list[dict]) -> str:
    """Format conversation history for display."""
    if not messages:
        return "[No prior conversation]"
    
    formatted = []
    for msg in messages:
        role = msg['role'].upper()
        content = msg['content']
        formatted.append(f"{role}: {content}")
    return "\n\n".join(formatted)


def parse_judgment(text: str) -> tuple[float, str]:
    """Parse score and reasoning from the judge's response."""
    lines = text.strip().split('\n')
    score = None
    reasoning = ""
    
    for i, line in enumerate(lines):
        if line.startswith("Score:"):
            # Extract score
            score_text = line.replace("Score:", "").strip()
            try:
                score = float(score_text.split('/')[0].strip())
            except ValueError:
                score = None
        elif line.startswith("Reasoning:"):
            # Extract reasoning (rest of the text)
            reasoning = line.replace("Reasoning:", "").strip()
            if i + 1 < len(lines):
                reasoning += "\n" + "\n".join(lines[i+1:])
            break
    
    # If parsing fails, use defaults
    if score is None:
        score = 5.0  # Default middle score
    if not reasoning:
        reasoning = text  # Use full text as reasoning
    
    return score, reasoning

```

## Best Practices for Advanced Rewards

1. **Modularity**: Break complex evaluation into smaller, testable functions
2. **Robustness**: Handle edge cases and invalid inputs gracefully
3. **Transparency**: Make evaluation criteria clear and interpretable
4. **Validation**: Test reward functions on diverse examples
5. **Performance**: Consider computational efficiency for large-scale evaluation

## Next Steps

* [Code Execution with E2B](/evaluators/examples/advanced_examples/code_execution_with_e2b)
* [Creating Your First Reward Function](/evaluators/tutorials/creating_your_first_reward_function)


# null
Source: https://docs.fireworks.ai/evaluators/examples/advanced_examples/code_execution_with_e2b



# Code Execution with E2B

This guide demonstrates how to use the E2B code execution reward function to evaluate code by running it in the E2B cloud sandbox.

## Overview

The `e2b_code_execution_reward` function allows you to:

1. Extract code blocks from LLM responses
2. Execute the code securely in E2B's cloud sandbox
3. Compare the output with expected results
4. Generate a score and detailed metrics

## Prerequisites

To use the E2B code execution reward function, you need:

1. An E2B API key from [E2B Dashboard](https://e2b.dev/dashboard)
2. The `e2b_code_interpreter` Python package installed: `pip install e2b_code_interpreter`

Note: The code will also work with the `e2b` package, but `e2b_code_interpreter` is recommended as it provides a more stable interface specifically designed for code execution.

## Basic Usage

Here's a simple example of how to use the reward function:

````python  theme={null}
from reward_kit.rewards.code_execution import e2b_code_execution_reward

# Example conversation with a Python coding task
messages = [
    {
        "role": "user",
        "content": "Write a Python function to calculate the factorial of a number."
    },
    {
        "role": "assistant",
        "content": """Here's a Python function to calculate the factorial of a number:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Should output 120
````

This function uses recursion to calculate the factorial. For n = 5, it computes 5 \* 4 \* 3 \* 2 \* 1 = 120."""
}
]

# Define expected output

expected\_output = "120"

# Evaluate the code using E2B

result = e2b\_code\_execution\_reward(
messages=messages,
expected\_output=expected\_output,
language="python",
api\_key="your\_e2b\_api\_key",
timeout=10
)

# Use the results

print(f"Score: {result.score}")
for metric\_name, metric in result.metrics.items():
print(f"\n{metric_name}: {metric.reason}")

````

## Supported Languages

The E2B code execution reward function currently supports:

- Python (`language="python"`)
- JavaScript (`language="javascript"` or `language="js"`)

## Advanced Options

### Automatic Output Extraction

You can let the reward function automatically extract the expected output from the prompt:

```python
# Conversation with expected output in the prompt
messages = [
    {
        "role": "user",
        "content": "Write a Python function to find the sum of a list. Expected output: 15 (for [1,2,3,4,5])"
    },
    {
        "role": "assistant",
        "content": """```python
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))
```"""
    }
]

# Pass the original messages for expected output extraction
result = e2b_code_execution_reward(
    messages=messages,
    original_messages=messages,
    language="python",
    api_key="your_e2b_api_key"
)
````

### Fallback to Local Execution

You can gracefully fall back to local execution when an E2B API key is not available:

```python  theme={null}
from reward_kit.rewards.code_execution import (
    e2b_code_execution_reward,
    local_code_execution_reward
)

# Try to use E2B if API key is provided
api_key = os.environ.get("E2B_API_KEY")

if api_key:
    result = e2b_code_execution_reward(
        messages=messages,
        expected_output=expected_output,
        language="python",
        api_key=api_key
    )
else:
    # Fall back to local execution
    result = local_code_execution_reward(
        messages=messages,
        expected_output=expected_output,
        language="python"
    )
```

## Parameters

The `e2b_code_execution_reward` function accepts the following parameters:

| Parameter           | Type                   | Description                                                          |
| ------------------- | ---------------------- | -------------------------------------------------------------------- |
| `messages`          | List\[Dict\[str, str]] | Generated conversation messages (required)                           |
| `original_messages` | List\[Dict\[str, str]] | Original conversation context (optional)                             |
| `expected_output`   | str                    | Expected output from code execution (optional)                       |
| `language`          | str                    | Programming language of the code (default: "python")                 |
| `timeout`           | int                    | Maximum execution time in seconds (default: 30)                      |
| `api_key`           | str                    | E2B API key (default: None, uses E2B\_API\_KEY environment variable) |

## Return Value

The reward function returns an `EvaluateResult` object with:

* `score`: A float between 0.0 and 1.0 indicating how well the code performed.
* `reason`: An overall explanation for the evaluation.
* `metrics`: A dictionary of `MetricResult` objects with detailed information about the execution.
* `error` (optional): A string describing any error during evaluation.

Key metrics include:

* `extracted_code`: The code that was extracted and executed
* `expected_output`: The expected output (if provided or extracted)
* `execution_result`: Details about the execution (success or failure)
* `output_match`: Comparison between actual and expected outputs

## Examples

See the `examples/` directory for complete examples:

* `e2b_reward_example.py`: Basic Python example
* `e2b_javascript_example.py`: JavaScript example
* `e2b_auto_extract_example.py`: Automatic output extraction example
* `e2b_fallback_example.py`: Fallback to local execution example


# null
Source: https://docs.fireworks.ai/evaluators/examples/advanced_examples/math_evaluation



# Math Evaluation

This guide explains how to evaluate mathematical answers in LLM responses, primarily focusing on the `math_reward` function.

**For a complete, runnable example of math evaluation using the GSM8K dataset, including Hydra configuration for `reward-kit run`, please refer to the [Math Example README](https://github.com/fw-ai-external/reward-kit/blob/main/examples/math_example/README.md) located in the `examples/math_example/` directory.**

The content below details the capabilities and programmatic usage of the underlying `math_reward` function, which is utilized within the `examples/math_example`.

## `math_reward` Function Overview

The `math_reward` function (found in `reward_kit.rewards.math`) allows you to:

1. Extract numerical answers from LLM responses
2. Compare them with expected answers or reference solutions
3. Handle various formats including fractions, decimals, and scientific notation
4. Support LaTeX formatted answers in markdown

## Prerequisites for Programmatic Use

To use the `math_reward` function directly in Python as shown below, ensure you have:

1. **Python 3.8+** installed on your system.
2. **Reward Kit** installed: `pip install reward-kit`.
   (Note: Running the full `examples/math_example` might require `pip install -e ".[dev]"` as per its README).

## Basic Programmatic Usage of `math_reward`

The following examples demonstrate direct programmatic use of the `math_reward` function. This can be useful for testing the function's behavior or integrating it into custom scripts. For evaluating a dataset of math problems, refer to the `examples/math_example/`.

Here's a simple example:

```python  theme={null}
from reward_kit.rewards.math import math_reward

# Example conversation with a math problem
messages = [
    {
        "role": "user",
        "content": "Calculate 15% of 80."
    },
    {
        "role": "assistant",
        "content": "To calculate 15% of 80, I'll multiply 80 by 0.15:\n\n80 × 0.15 = 12\n\nTherefore, 15% of 80 is 12."
    }
]

# Expected answer
expected_answer = "12"

# Evaluate the response
result = math_reward(
    messages=messages,
    expected_answer=expected_answer
)

# Print the results
print(f"Score: {result.score}")
print("Metrics:")
for name, metric in result.metrics.items():
    print(f"  {name}: {metric.score}")
    print(f"    {metric.reason}")
```

## How `math_reward` Works

The `math_reward` function:

1. Extracts potential answer values from the last assistant message
2. Extracts expected answer value from the provided string
3. Compares them with tolerance for floating-point values
4. Returns a score of 1.0 for correct answers and 0.0 for incorrect answers
5. Provides detailed metrics about the extraction and comparison process

## Supported Answer Formats

The math reward function can extract and compare answers in various formats:

### Integer and Decimal Numbers

```
42
-27
3.14159
0.5
```

### Fractions

```
3/4
-5/8
1 2/3 (mixed fractions)
```

### Scientific Notation

```
1.23e4
6.022 × 10^23
5.67 × 10⁻⁸
```

### LaTeX Formatting

```
\boxed{42}
\frac{3}{4}
\frac{22}{7} \approx 3.14
\pi \approx 3.14159
2.998 \times 10^8 \text{ m/s}
```

### Units

```
42 kg
3.14 m/s²
5 \text{ meters}
```

## Advanced Programmatic Usage of `math_reward`

### Customizing Extraction

You can customize the extraction process to look for answers in particular formats or locations:

```python  theme={null}
from reward_kit.rewards.math import math_reward

# Messages with LaTeX formatted answer
messages = [
    {
        "role": "user",
        "content": "What is the area of a circle with radius 3 cm?"
    },
    {
        "role": "assistant",
        "content": "To find the area of a circle, I'll use the formula:\n\nArea = πr²\n\nSubstituting r = 3 cm:\n\nArea = π × 3² = 9π cm²\n\nCalculating with π ≈ 3.14159:\n\nArea ≈ 28.27 cm²\n\nTherefore, the area of a circle with radius 3 cm is \n\n$$\\boxed{28.27 \\text{ cm}^2}$$"
    }
]

# Evaluate with custom extraction patterns
result = math_reward(
    messages=messages,
    expected_answer="28.27 cm^2",
    extract_boxed_only=True,  # Only look for answers in \boxed{} environments
    ignore_units=False,       # Consider units in the comparison
    tolerance=0.01            # Allow for slight differences in rounding
)
```

### Multiple Valid Answers

Sometimes, multiple forms of the same answer are acceptable. You can evaluate against multiple correct answers:

```python  theme={null}
from reward_kit.rewards.math import math_reward

# Message with fraction answer
messages = [
    {
        "role": "user",
        "content": "What is 1/4 + 1/6?"
    },
    {
        "role": "assistant",
        "content": "To add fractions with different denominators, I need to find a common denominator.\n\n1/4 + 1/6\n\nLCD = 12\n\n1/4 = 3/12\n1/6 = 2/12\n\n3/12 + 2/12 = 5/12\n\nTherefore, 1/4 + 1/6 = 5/12"
    }
]

# Accept either fraction or decimal form
result = math_reward(
    messages=messages,
    expected_answer=["5/12", "0.41666"], # Accept either form
    tolerance=0.001  # Small tolerance for decimal approximation
)
```

### Original Messages as Reference

If the correct answer is in the original messages, you can extract it automatically:

```python  theme={null}
from reward_kit.rewards.math import math_reward

# Original conversation with correct answer
original_messages = [
    {
        "role": "user",
        "content": "Solve the equation 2x + 5 = 15. The answer is x = 5."
    }
]

# Generated response to evaluate
generated_messages = [
    {
        "role": "user",
        "content": "Solve the equation 2x + 5 = 15."
    },
    {
        "role": "assistant",
        "content": "To solve the equation 2x + 5 = 15, I'll isolate the variable x.\n\n2x + 5 = 15\n2x = 15 - 5\n2x = 10\nx = 10/2\nx = 5\n\nTherefore, the solution is x = 5."
    }
]

# Extract expected answer from original messages
result = math_reward(
    messages=generated_messages,
    original_messages=original_messages,
    extract_answer_from_original=True  # Extract answer from original messages
)
```

## Use Cases

### Evaluating Math Problem Solving

The math reward function is perfect for evaluating responses to:

* Basic arithmetic problems
* Algebra equations
* Calculus problems
* Physics calculations
* Economics computations
* Statistics problems

### Educational Applications

Use the math reward function to:

* Automatically grade math homework
* Provide instant feedback on practice problems
* Evaluate mathematical reasoning in tutoring systems

## Best Practices

1. **Be Explicit About Units**: Specify whether units should be considered in the comparison
2. **Consider Fractions vs. Decimals**: Decide if approximate decimal answers are acceptable for fraction problems
3. **Set Appropriate Tolerance**: Use a tolerance appropriate for the problem (e.g., higher for complex calculations)
4. **Look for Final Answers**: Set up extraction patterns to focus on the final answer rather than intermediate steps
5. **Multiple Representations**: Consider all valid forms of an answer (fraction, decimal, scientific notation)
6. **LaTeX Handling**: Take advantage of the LaTeX support for nicely formatted answers

## Limitations

* Cannot evaluate the correctness of the solution method, only the final answer
* May have difficulty with extremely complex LaTeX expressions
* Cannot evaluate mathematical proofs or abstract reasoning
* Works best with numerical answers rather than symbolic expressions

## Next Steps

* Learn about [Code Execution Evaluation](/evaluators/examples/advanced_examples/code_execution_with_e2b) for evaluating code solutions
* See [Tool Calling Example](/evaluators/examples/tool_calling_example) for evaluating tool use
* See [Creating Custom Reward Functions](/evaluators/tutorials/creating_your_first_reward_function) to build your own specialized math evaluators


# null
Source: https://docs.fireworks.ai/evaluators/examples/apps_coding_example



# APPS Coding Example

This guide explains how to use the `reward-kit run` command to evaluate code generation models on a sample of the `codeparrot/apps` dataset. This example focuses on checking the parsability of generated Python code.

## Overview

* **Dataset**: A sample from `codeparrot/apps`, a dataset of programming problems and solutions. The specific dataset configuration used is `apps_full_prompts` (defined in `conf/dataset/apps_full_prompts.yaml`), which typically points to a pre-generated JSONL file.
* **Task**: Given a problem description (question), the model should generate a Python code solution.
* **Reward Function**: The evaluation uses `reward_kit.rewards.apps_coding_reward.evaluate_apps_solution`.
  * **Functionality**: In its current form for this example, this reward function performs a basic check to see if the generated Python code is parsable by Python's `ast.parse` module. It scores `1.0` if the code is parsable and `0.0` otherwise.
  * It does *not* execute the code or check for functional correctness against test cases in this simplified setup.
  * The `ground_truth_for_eval` field (derived from APPS' `input_output` field) is available to the reward function but not utilized by this initial parsability check.
* **System Prompt**: A default system prompt is provided in the configuration to guide the model:
  ```
  Please write a Python script that solves the following problem. Structure your solution within a main() function. Please read from stdin directly and make sure the code is not interactive. The main() function should print the final result(s) to standard output as required by the problem statement.
  ```

## Setup

1. **Environment**: Ensure your Python environment is set up with `reward-kit` and its development dependencies installed. If you haven't already, install them from the root of the repository:
   ```bash  theme={null}
   pip install -e ".[dev]"
   ```
2. **API Key**: The default configuration uses a Fireworks AI model (`accounts/fireworks/models/deepseek-v3-0324`) for code generation. Make sure your `FIREWORKS_API_KEY` is set in your environment or in a `.env` file in the project root.

## Data Preparation (Informational)

The example typically uses a pre-generated sample of prompts from the `codeparrot/apps` dataset. The default run configuration (`run_eval.yaml`) references `apps_full_prompts`, which points to `development/CODING_DATASET.jsonl`.

If you wished to regenerate this sample or create a different one (this is for informational purposes, not required to run the example with defaults):

1. The script `scripts/convert_apps_to_prompts.py` can convert the raw Hugging Face `codeparrot/apps` dataset into the JSONL format expected by the pipeline.
2. The source dataset configuration for raw APPS data is defined in `conf/dataset/apps_source.yaml`.
3. An example command to generate 5 samples from the 'test' split:
   ```bash  theme={null}
   python scripts/convert_apps_to_prompts.py \
       --dataset_name codeparrot/apps \
       --split test \
       --output_file development/apps_sample_prompts.jsonl \
       --max_samples 5 \
       --id_column problem_id \
       --query_column question \
       --ground_truth_column input_output
   ```

## Running the Evaluation

The evaluation is configured in `examples/apps_coding_example/conf/run_eval.yaml`. This is the main configuration file used by Hydra.

To run the evaluation using the `reward-kit run` command:

1. Ensure your virtual environment is activated:
   ```bash  theme={null}
   source .venv/bin/activate
   ```
2. Execute the run command from the root of the repository:
   ```bash  theme={null}
   reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval
   ```

### Overriding Parameters

You can override parameters from the `run_eval.yaml` configuration directly from the command line. For example:

* **Limit the number of samples for a quick test**:
  ```bash  theme={null}
  reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval evaluation_params.limit_samples=2
  ```
* **Disable code generation (to test reward function with cached responses)**:
  If you have previously run the example and responses are cached (default cache dir: `outputs/generated_responses_cache_apps/`), you can disable new generation:
  ```bash  theme={null}
  reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval generation.enabled=false
  ```
* **Change the generation model**:
  ```bash  theme={null}
  reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval generation.model_name="accounts/fireworks/models/another-model"
  ```

Refer to the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration) for more details on Hydra.

## Expected Output

The `reward-kit run` command will:

1. Load prompts based on the `apps_full_prompts` dataset configuration (typically from `development/CODING_DATASET.jsonl`).
2. If `generation.enabled` is `true` (default), generate code solutions using the configured model. Responses are cached (default: `outputs/generated_responses_cache_apps/`).
3. Evaluate each generated solution using the `evaluate_apps_solution` reward function (checking for Python AST parsability).
4. Print a summary of results to the console.
5. Save detailed evaluation results to a JSONL file in a timestamped directory. The default output path is configured in `run_eval.yaml` as `./outputs/apps_coding_example/${now:%Y-%m-%d}/${now:%H-%M-%S}`. The results file will be named `apps_coding_example_results.jsonl` within that directory.

The results file will contain the original prompt, generated response, the parsability score (0 or 1), and other metrics from the reward function.


# null
Source: https://docs.fireworks.ai/evaluators/examples/basic_examples/basic_reward_function



# Basic Reward Function

This example demonstrates how to create a simple reward function using RewardKit.

## Overview

A basic reward function evaluates model responses and returns a numerical score. This example shows the fundamental concepts and patterns.

## Simple Accuracy Reward

```python  theme={null}
from reward_kit import reward_function

@reward_function
def simple_accuracy(response: str, expected_response: str) -> float:
    """
    A basic accuracy reward that returns 1.0 for exact matches, 0.0 otherwise.
    """
    return 1.0 if response.strip().lower() == expected_response.strip().lower() else 0.0
```

## Usage

```python  theme={null}
# Evaluate a single response
score = simple_accuracy("Hello world", "hello world")
print(f"Score: {score}")  # Score: 1.0

# Evaluate a dataset
from reward_kit.evaluation import evaluate_dataset

results = evaluate_dataset(
    reward_function=simple_accuracy,
    dataset_path="my_dataset.jsonl"
)
```

## Key Concepts

* **Decoration**: Use `@reward_function` to create a reward function
* **Type Hints**: Include type hints for better IDE support
* **Normalization**: Consider normalizing inputs (e.g., lowercasing, stripping whitespace)
* **Return Values**: Return numerical scores (typically 0.0 to 1.0)

## Next Steps

* [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions)
* [Reward Functions Overview](/evaluators/examples/basic_examples/reward_functions_overview)
* [Creating Your First Reward Function](/evaluators/tutorials/creating_your_first_reward_function)


# null
Source: https://docs.fireworks.ai/evaluators/examples/basic_examples/reward_functions_overview



# Reward Functions Overview

This guide provides an overview of reward functions in RewardKit and how to use them effectively.

## What are Reward Functions?

Reward functions are the core building blocks of RewardKit. They evaluate model responses and provide numerical feedback that can be used for training, evaluation, and analysis.

## Basic Structure

Every reward function follows this pattern:

```python  theme={null}
from reward_kit import reward_function

@reward_function
def my_reward(response: str, expected_response: str, **kwargs) -> float:
    # Your evaluation logic here
    return score
```

## Built-in Reward Functions

RewardKit provides several built-in reward functions:

### Accuracy-based

* `accuracy`: Exact string matching
* `fuzzy_accuracy`: Fuzzy string matching with configurable threshold

### Length-based

* `length`: Evaluates response length
* `length_penalty`: Penalizes responses that are too long or short

### Format-based

* `json_schema`: Validates JSON responses against a schema
* `format_compliance`: Checks if responses follow expected formats

### Code-specific

* `code_execution`: Evaluates code by executing it
* `syntax_validation`: Checks code syntax

## Custom Reward Functions

You can create custom reward functions for domain-specific evaluation:

```python  theme={null}
@reward_function
def domain_specific_reward(response: str, expected_response: str) -> float:
    # Custom logic for your domain
    score = 0.0

    # Example: Check for specific keywords
    if "important_keyword" in response.lower():
        score += 0.5

    # Example: Length consideration
    if 50 <= len(response) <= 200:
        score += 0.3

    # Example: Accuracy component
    if response.strip() == expected_response.strip():
        score += 0.2

    return min(score, 1.0)  # Cap at 1.0
```

## Best Practices

1. **Clear Naming**: Use descriptive names for your reward functions
2. **Type Hints**: Include type hints for better IDE support
3. **Documentation**: Add docstrings explaining what your function evaluates
4. **Normalization**: Normalize scores to a consistent range (typically 0.0 to 1.0)
5. **Testing**: Test your reward functions with edge cases

## Combining Rewards

You can combine multiple reward functions:

```python  theme={null}
@reward_function
def combined_reward(response: str, expected_response: str) -> float:
    acc_score = accuracy(response, expected_response)
    len_score = length_penalty(response, min_length=10, max_length=100)

    return 0.8 * acc_score + 0.2 * len_score
```

## Next Steps

* [Basic Reward Function Example](/evaluators/examples/basic_examples/basic_reward_function)
* [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions)
* [Creating Your First Reward Function](/evaluators/tutorials/creating_your_first_reward_function)


# null
Source: https://docs.fireworks.ai/evaluators/examples/e2b/e2b_code_execution_overview



# E2B Code Execution Overview

This guide explains how to use E2B (Code Interpreter) with RewardKit for safe code execution and evaluation.

## Overview

E2B provides sandboxed environments for executing code safely. RewardKit integrates with E2B to enable code execution rewards that can run and evaluate generated code.

## Setup

First, install the E2B integration:

```bash  theme={null}
pip install e2b-code-interpreter
```

Set up your E2B API key:

```bash  theme={null}
export E2B_API_KEY="your_api_key_here"
```

## Basic Code Execution Reward

```python  theme={null}
from reward_kit import reward_function
from e2b_code_interpreter import CodeInterpreter

@reward_function
def e2b_code_execution_reward(response: str, expected_output: str, **kwargs) -> float:
    """
    Executes code using E2B and compares output to expected result.
    """
    try:
        with CodeInterpreter() as sandbox:
            # Execute the generated code
            execution = sandbox.notebook.exec_cell(response)

            if execution.error:
                return 0.0

            # Get the output
            output = ""
            for result in execution.results:
                if hasattr(result, 'text'):
                    output += result.text
                elif hasattr(result, 'data'):
                    output += str(result.data)

            # Compare with expected output
            if output.strip() == expected_output.strip():
                return 1.0
            else:
                # Partial credit based on similarity
                return calculate_output_similarity(output, expected_output)

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0

def calculate_output_similarity(actual: str, expected: str) -> float:
    """Calculate similarity between outputs."""
    actual = actual.strip()
    expected = expected.strip()

    if not expected:
        return 1.0 if not actual else 0.0

    # Simple word-based similarity
    actual_words = set(actual.lower().split())
    expected_words = set(expected.lower().split())

    if not expected_words:
        return 1.0

    intersection = actual_words & expected_words
    return len(intersection) / len(expected_words)
```

## Advanced Code Evaluation

```python  theme={null}
@reward_function
def advanced_code_evaluation(response: str, test_cases: list, **kwargs) -> float:
    """
    Evaluates code against multiple test cases using E2B.
    """
    if not test_cases:
        return 0.0

    passed_tests = 0
    total_tests = len(test_cases)

    try:
        with CodeInterpreter() as sandbox:
            # First, execute the response code to define functions/variables
            setup_execution = sandbox.notebook.exec_cell(response)

            if setup_execution.error:
                return 0.0

            # Run each test case
            for test_case in test_cases:
                test_code = test_case.get('code', '')
                expected_output = test_case.get('expected', '')

                test_execution = sandbox.notebook.exec_cell(test_code)

                if test_execution.error:
                    continue

                # Check output
                actual_output = ""
                for result in test_execution.results:
                    if hasattr(result, 'text'):
                        actual_output += result.text

                if actual_output.strip() == expected_output.strip():
                    passed_tests += 1

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0

    return passed_tests / total_tests
```

## File-based Code Evaluation

```python  theme={null}
@reward_function
def file_based_code_reward(response: str, file_operations: list, **kwargs) -> float:
    """
    Evaluates code that performs file operations.
    """
    try:
        with CodeInterpreter() as sandbox:
            # Execute the code
            execution = sandbox.notebook.exec_cell(response)

            if execution.error:
                return 0.0

            score = 0.0
            total_operations = len(file_operations)

            # Check each expected file operation
            for operation in file_operations:
                file_path = operation.get('path', '')
                expected_content = operation.get('content', '')
                operation_type = operation.get('type', 'create')

                if operation_type == 'create':
                    # Check if file was created with correct content
                    try:
                        # Read the file
                        read_execution = sandbox.notebook.exec_cell(f"""
with open('{file_path}', 'r') as f:
    content = f.read()
print(content)
                        """)

                        if not read_execution.error:
                            actual_content = ""
                            for result in read_execution.results:
                                if hasattr(result, 'text'):
                                    actual_content += result.text

                            if actual_content.strip() == expected_content.strip():
                                score += 1.0

                    except Exception:
                        pass

                elif operation_type == 'exists':
                    # Check if file exists
                    check_execution = sandbox.notebook.exec_cell(f"""
import os
print(os.path.exists('{file_path}'))
                    """)

                    if not check_execution.error:
                        for result in check_execution.results:
                            if hasattr(result, 'text') and 'True' in result.text:
                                score += 1.0
                                break

            return score / total_operations if total_operations > 0 else 0.0

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0
```

## Data Analysis Code Evaluation

```python  theme={null}
@reward_function
def data_analysis_reward(response: str, dataset_path: str, expected_insights: list, **kwargs) -> float:
    """
    Evaluates data analysis code by checking insights and outputs.
    """
    try:
        with CodeInterpreter() as sandbox:
            # Upload dataset to sandbox
            with open(dataset_path, 'rb') as f:
                data_file = sandbox.files.write('dataset.csv', f.read())

            # Execute the analysis code
            execution = sandbox.notebook.exec_cell(response)

            if execution.error:
                return 0.0

            score = 0.0

            # Check for expected insights
            output_text = ""
            for result in execution.results:
                if hasattr(result, 'text'):
                    output_text += result.text.lower()

            # Check each expected insight
            for insight in expected_insights:
                if insight.lower() in output_text:
                    score += 1.0

            # Bonus for plots/visualizations
            has_plot = any(
                hasattr(result, 'formats') and 'image/png' in result.formats
                for result in execution.results
            )

            if has_plot:
                score += 0.5

            return min(score / len(expected_insights), 1.0) if expected_insights else 0.0

    except Exception as e:
        print(f"E2B execution error: {e}")
        return 0.0
```

## Safety and Best Practices

1. **Timeout Handling**: E2B automatically handles timeouts for long-running code
2. **Resource Limits**: Sandboxes have built-in resource limits
3. **Error Handling**: Always handle execution errors gracefully
4. **Clean Output**: Parse output carefully as it may contain formatting
5. **State Management**: Each CodeInterpreter session maintains state across cells

## Usage Examples

```python  theme={null}
# Test a simple calculation
test_cases = [
    {
        'code': 'result = add_numbers(2, 3)',
        'expected': '5'
    },
    {
        'code': 'result = add_numbers(-1, 1)',
        'expected': '0'
    }
]

code_response = """
def add_numbers(a, b):
    return a + b
"""

score = advanced_code_evaluation(code_response, test_cases)
print(f"Code evaluation score: {score}")
```

## Integration with RewardKit

E2B code execution can be easily integrated into your evaluation workflows:

```python  theme={null}
from reward_kit.evaluation import evaluate_dataset

# Evaluate a dataset of coding problems
results = evaluate_dataset(
    reward_function=e2b_code_execution_reward,
    dataset_path="coding_problems.jsonl",
    additional_fields=['test_cases', 'expected_output']
)
```

## Next Steps

* [Code Execution with E2B Example](https://github.com/fw-ai-external/reward-kit/blob/main/examples/e2b_reward_example.py)
* [Advanced Reward Functions](/evaluators/examples/advanced_examples/advanced_reward_functions)


# null
Source: https://docs.fireworks.ai/evaluators/examples/examples_overview



# Reward Kit Examples

This page provides an overview of and links to documentation for various examples demonstrating the capabilities of the Reward Kit. All documentation for these examples is self-contained within the `docs/` folder.

Many examples use [Hydra for configuration](/evaluators/developer_guide/hydra_configuration). Please refer to the specific documentation page for each example for execution instructions.

## Available Examples

* **Accuracy Length Example**:
  * Demonstrates combined accuracy and length rewards.
  * [View Documentation](/evaluators/examples/accuracy_length/accuracy_length_overview)

* **APPS Coding Example**:
  * Illustrates evaluation for coding problems from the APPS dataset.
  * [View Documentation](/evaluators/examples/apps_coding_example) *(New file to be created)*

* **E2B (Code Execution Sandbox) Examples**:
  * Covers various E2B integration scenarios for sandboxed code execution.
  * [View Documentation](/evaluators/examples/e2b/e2b_code_execution_overview)

* **GCP Cloud Run Deployment Example**:
  * Shows how to deploy a Reward Kit application on GCP Cloud Run.
  * [View Documentation](/evaluators/examples/gcp_cloud_run_deployment_example) *(New file to be created)*

* **Math Example (GSM8K)**:
  * Focuses on evaluating math word problems using the GSM8K dataset.
  * [View Documentation](/evaluators/examples/advanced_examples/math_evaluation)

* **Math with Formatting Example**:
  * Extends math evaluation to handle specific formatting requirements.
  * [View Documentation](/evaluators/examples/math_with_formatting_example) *(New file to be created)*

* **Tool Calling Example**:
  * Demonstrates evaluation for models that use tools or function calls.
  * [View Documentation](/evaluators/examples/tool_calling_example) *(New file to be created)*

* **TRL Integration Example**:
  * Shows how to integrate reward-kit functions with the TRL library.
  * [View Documentation](/evaluators/integrations/trl_integration_overview)

*Note: The `examples/metrics/` and `examples/test_tasks/` directories in the root `examples/` folder contain supporting resources and are not standalone documented examples here.*

## General Guides for Examples

While the pages above cover specific examples, these general guides might also be useful:

* [Reward Functions Overview](/evaluators/examples/basic_examples/reward_functions_overview) *(To be reviewed/updated)*
* [Basic Reward Function Concepts](/evaluators/examples/basic_examples/basic_reward_function) *(To be reviewed/updated)*
* [Advanced Reward Function Concepts](/evaluators/examples/advanced_examples/advanced_reward_functions) *(To be reviewed/updated)*

## Next Steps

* See the [Developer Guide](/evaluators/developer_guide/getting_started) for comprehensive information.
* Check the [Tutorials](../tutorials/) for step-by-step guides.
* Refer to the [API Reference](/evaluators/api_reference/api_overview) for detailed documentation.


# null
Source: https://docs.fireworks.ai/evaluators/examples/gcp_cloud_run_deployment_example



# GCP Cloud Run Deployment Example

This guide demonstrates how to deploy a simple reward function to Google Cloud Run using the `reward-kit` CLI. The example uses a basic `hello_world_reward` function found in `examples/gcp_cloud_run_deployment_example/dummy_rewards.py`.

## Overview

Deploying a reward function to GCP Cloud Run allows you to host it as a scalable, serverless HTTP endpoint. The `reward-kit deploy` command automates much of this process, including containerization and service configuration.

## Files in the Example Directory

Located in `examples/gcp_cloud_run_deployment_example/`:

* `dummy_rewards.py`: Contains a basic `hello_world_reward` function used for this deployment example.
* `rewardkit.example.yaml`: An example configuration file for `reward-kit`. This shows the structure for `rewardkit.yaml` if you choose to use one for GCP settings.

## Prerequisites

1. **Google Cloud Platform (GCP) Account**: Active GCP account with billing enabled.
2. **`gcloud` CLI**: [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) installed and authenticated (`gcloud auth login`, `gcloud auth application-default login`).
3. **APIs Enabled**: Ensure the following APIs are enabled in your GCP project:
   * Cloud Build API
   * Artifact Registry API
   * Cloud Run Admin API
   * Secret Manager API
4. **Permissions**: The authenticated user/service account for `gcloud` needs sufficient permissions (e.g., roles like "Cloud Build Editor", "Artifact Registry Administrator", "Cloud Run Admin", "Secret Manager Admin").
5. **`reward-kit` installed**: Ensure `reward-kit` is installed in your Python environment (e.g., `pip install reward-kit`).

## Setup

### `rewardkit.yaml` Configuration (Optional but Recommended)

The `reward-kit` CLI can pick up GCP settings from a `rewardkit.yaml` file located in the directory from which you run the `reward-kit deploy` command.

1. **Create `rewardkit.yaml`**:
   You can copy the `examples/gcp_cloud_run_deployment_example/rewardkit.example.yaml` to the directory where you intend to run `reward-kit deploy` (this could be the example directory itself, or your project root). Rename it to `rewardkit.yaml`.
   ```bash  theme={null}
   # If in examples/gcp_cloud_run_deployment_example/
   cp rewardkit.example.yaml rewardkit.yaml
   ```

2. **Customize `rewardkit.yaml`**:
   Open `rewardkit.yaml` and replace placeholders with your actual GCP Project ID and desired region.
   Example `rewardkit.yaml`:
   ```yaml  theme={null}
   gcp_cloud_run:
     project_id: "my-actual-gcp-project-123"
     region: "us-west1"
     # artifact_registry_repository: "my-custom-eval-repo" # Optional
     # default_auth_mode: "api-key" # Optional, defaults to api-key
   evaluator_endpoint_keys: {} # Managed by reward-kit for API key auth
   ```

**Note**: If you choose not to use a `rewardkit.yaml` file, you **must** provide all necessary GCP parameters (like `--gcp-project YOUR_PROJECT_ID`, `--gcp-region YOUR_REGION`) directly in the `reward-kit deploy` command.

## Deployment Command

It's recommended to run the deployment command from the directory containing the reward function script (`dummy_rewards.py`) and your `rewardkit.yaml` (if used), for example, from `examples/gcp_cloud_run_deployment_example/`.

1. Ensure your virtual environment is active:
   ```bash  theme={null}
   source .venv/bin/activate
   ```
2. Run the deployment command:
   ```bash  theme={null}
   reward-kit deploy \
       --id my-dummy-gcp-evaluator \
       --target gcp-cloud-run \
       --function-ref dummy_rewards.hello_world_reward \
       --gcp-auth-mode api-key \
       --verbose
       # --force # Add if overwriting an existing evaluator
       # If not using rewardkit.yaml, add required GCP params:
       # --gcp-project YOUR_PROJECT_ID --gcp-region YOUR_REGION
   ```

**Command Explanation:**

* `--id my-dummy-gcp-evaluator`: A unique ID for your evaluator on the Fireworks AI platform.
* `--target gcp-cloud-run`: Specifies deployment to GCP Cloud Run.
* `--function-ref dummy_rewards.hello_world_reward`: The Python import path to your reward function. If `dummy_rewards.py` is in the current directory, this reference works.
* `--gcp-auth-mode api-key`: Configures the Cloud Run service with API key authentication. `reward-kit` will generate a key, store it in GCP Secret Manager, and configure the service. The key is also saved to your local `rewardkit.yaml` under `evaluator_endpoint_keys`. This is the default if not specified.
* `--verbose`: Shows detailed output, including `gcloud` commands being executed.
* `--force`: (Optional) If an evaluator with the same `--id` already exists, this flag will delete the existing one before creating the new one.

## Expected Outcome

If successful, `reward-kit` will:

1. Create an Artifact Registry repository (default: `reward-kit-evaluators`, or as specified in `rewardkit.yaml`).
2. Build a Docker container with your reward function and push it to Artifact Registry.
3. If `api-key` auth is used, create a GCP Secret to store the generated API key.
4. Deploy the container to Cloud Run, configured for the chosen authentication mode.
5. Register the deployed Cloud Run service URL as a remote evaluator with the Fireworks AI platform.

The output will include the Cloud Run service URL and the API key (if newly generated).

## Testing the Deployed Endpoint

You can test the deployed endpoint using `curl` or `reward-kit preview --remote-url <your-cloud-run-url>`.

If using `curl` with API key authentication:

1. Retrieve the API key. It's printed during deployment and saved in `rewardkit.yaml` (if one is used in the command's directory) under `evaluator_endpoint_keys: { "my-dummy-gcp-evaluator": "YOUR_KEY" }`.
2. Get your Cloud Run service URL from the deployment output.

```bash  theme={null}
API_KEY="your_generated_api_key"
SERVICE_URL="your_cloud_run_service_url"

curl -X POST "$SERVICE_URL/evaluate" \
     -H "Content-Type: application/json" \
     -H "X-Api-Key: $API_KEY" \
     -d '{
           "messages": [{"role": "user", "content": "Test"}],
           "kwargs": {}
         }'
```

This should return a JSON response from your `hello_world_reward` function.


# null
Source: https://docs.fireworks.ai/evaluators/examples/math_with_formatting_example



# Math with Formatting Example

This guide explains how to evaluate models on math word problems using the `reward-kit run` command, focusing on both the accuracy of the numerical answer and the adherence to a specific response format (e.g., `<think>...</think><answer>...</answer>`). This example uses the GSM8K dataset.

## Overview

The "Math with Formatting" example demonstrates a multi-metric evaluation:

1. **Accuracy Reward**: Assesses if the extracted numerical answer is correct.
2. **Format Reward**: Checks if the model's response follows the prescribed XML-like structure for thoughts and the final answer.
   The final score reported is typically an average of these two rewards.

* **Dataset**: Uses the `gsm8k` dataset, configured via `gsm8k_math_with_formatting_prompts.yaml` which adds specific system prompts to guide the model's output format.
* **Reward Logic**: The core evaluation logic is in `examples/math_with_formatting/main.py`, referenced in the run configuration as `examples.math_with_formatting.main.evaluate`.
* **System Prompt Example** (from `gsm8k_math_with_formatting_prompts.yaml`):
  ```
  Solve the following math problem. Provide your reasoning and then put the final numerical answer between <answer> and </answer> tags.
  ```

## Setup

1. **Environment**: Ensure your Python environment has `reward-kit` and its development dependencies installed:
   ```bash  theme={null}
   # From the root of the repository
   pip install -e ".[dev]"
   ```
2. **API Key**: The default configuration (`run_math_with_formatting_eval.yaml`) uses a Fireworks AI model (e.g., `accounts/fireworks/models/qwen3-235b-a22b`). Ensure your `FIREWORKS_API_KEY` is set in your environment or a `.env` file.

## Running the Evaluation

The primary configuration for this example is `examples/math_with_formatting/conf/run_math_with_formatting_eval.yaml`.

1. Activate your virtual environment:
   ```bash  theme={null}
   source .venv/bin/activate
   ```
2. Execute the `reward-kit run` command from the root of the repository:
   ```bash  theme={null}
   reward-kit run --config-path examples/math_with_formatting/conf --config-name run_math_with_formatting_eval
   ```

### Overriding Parameters

You can modify parameters via the command line. For instance:

* **Limit samples**:
  ```bash  theme={null}
  reward-kit run --config-path examples/math_with_formatting/conf --config-name run_math_with_formatting_eval evaluation_params.limit_samples=5
  ```
  (The default in the example config is `limit_samples: 2`).
* **Change generation model**:
  ```bash  theme={null}
  reward-kit run --config-path examples/math_with_formatting/conf --config-name run_math_with_formatting_eval generation.model_name="accounts/fireworks/models/mixtral-8x7b-instruct"
  ```

For more on Hydra, see the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration).

## Expected Output

The command will:

1. Load the GSM8K dataset as configured by `gsm8k_math_with_formatting_prompts.yaml`.
2. Generate model responses using the specified model (default: `qwen3-235b-a22b`).
3. Evaluate responses using the logic in `examples.math_with_formatting.main.evaluate`, which combines accuracy and format checks.
4. Print a summary to the console.
5. Save detailed results to a JSONL file (e.g., `math_with_formatting_example_results.jsonl`) in a timestamped directory under `outputs/` (the exact path is determined by Hydra, typically based on the current date/time).
6. Save prompt/response pairs to `preview_input_output_pairs.jsonl` in the same output directory.

The results file will include the overall `evaluation_score` (average of accuracy and format) and a breakdown in `evaluation_metrics` for `accuracy_reward` and `format_reward`.

## Key Components

* **`examples/math_with_formatting/main.py`**: Contains the `evaluate()` function with the core reward logic, including:
  * `accuracy_reward_fn`: Extracts and compares numerical answers.
  * `format_reward_fn`: Checks for the `<think>...</think><answer>...</answer>` structure.
* **Dataset Configuration**: Uses a derived dataset (`gsm8k_math_with_formatting_prompts.yaml`) to add specific system prompts to the base `gsm8k` dataset.

This example highlights how to enforce and evaluate structured output from LLMs alongside correctness for tasks like mathematical reasoning.


# null
Source: https://docs.fireworks.ai/evaluators/examples/tool_calling_example



# Tool Calling Example

This guide explains how to use the examples in `examples/tool_calling_example/` for evaluating and training models for tool/function calling capabilities. These examples primarily use Hydra for configuration.

## Overview

The `examples/tool_calling_example/` directory contains scripts for:

1. **Local Evaluation (`local_eval.py`)**: Evaluating a model's ability to make tool calls against a dataset.
2. **TRL GRPO Integration (`trl_grpo_integration.py`)**: Fine-tuning a model for tool calling using TRL (Transformer Reinforcement Learning) with Group Relative Policy Optimization (GRPO).

A sample `dataset.jsonl` is provided in the example directory. For tool calling tasks, each entry in the dataset typically includes:

* `messages`: A list of conversation messages.
* `tools`: A list of tool definitions available to the model.
* `ground_truth`: The expected assistant response, which might include tool calls (e.g., `{"role": "assistant", "tool_calls": [...]}`) or a direct content response.

## Setup

1. **Environment**: Ensure your Python environment has `reward-kit` and its development dependencies installed:
   ```bash  theme={null}
   # From the root of the repository
   pip install -e ".[dev]"
   ```
2. **TRL Extras (for `trl_grpo_integration.py`)**:
   ```bash  theme={null}
   pip install "reward-kit[trl]"
   ```
3. **API Keys**: If using models that require API keys (e.g., Fireworks AI models for `local_eval.py` if not using a local model, or for downloading a base model for TRL), ensure necessary keys like `FIREWORKS_API_KEY` are set.

## 1. Local Evaluation (`local_eval.py`)

This script performs local evaluation of a model's tool calling.

### Configuration

* Uses Hydra and is configured by `examples/tool_calling_example/conf/local_eval_config.yaml`.
* The default configuration points to `examples/tool_calling_example/dataset.jsonl`.
* The script itself likely contains defaults for the model and reward function, or expects them as CLI overrides.

### How to Run

1. Activate your virtual environment:
   ```bash  theme={null}
   source .venv/bin/activate
   ```
2. Execute from the repository root:
   ```bash  theme={null}
   python examples/tool_calling_example/local_eval.py
   ```

### Overriding Parameters

* **Change dataset path**:
  ```bash  theme={null}
  python examples/tool_calling_example/local_eval.py dataset_file_path=path/to/your/tool_calling_dataset.jsonl
  ```
* Other parameters (e.g., model name, reward function parameters) would typically be added to `local_eval_config.yaml` or passed as CLI overrides if `local_eval.py` is structured to accept them via Hydra.

Outputs are saved to Hydra's default output directory (configured in `local_eval_config.yaml` as `./outputs/local_eval_tool_calling/${now:%Y-%m-%d}/${now:%H-%M-%S}`).

## 2. TRL GRPO Integration (`trl_grpo_integration.py`)

This script provides a scaffold for fine-tuning a model for tool calling using TRL GRPO.
**Note**: The script defaults to using a MOCK model and tokenizer. Using a real model requires code modifications in `trl_grpo_integration.py` and potentially `conf/trl_grpo_config.yaml`.

### Configuration

* Uses Hydra and is configured by `examples/tool_calling_example/conf/trl_grpo_config.yaml`.
* Default `dataset_file_path`: `dataset.jsonl` (assumed to be in `examples/tool_calling_example/`).
* Default `model_name`: `Qwen/Qwen2-0.5B-Instruct`.
* Includes various `grpo` training parameters.

### How to Run (with Mock Model by default)

1. Activate your virtual environment:
   ```bash  theme={null}
   source .venv/bin/activate
   ```
2. Execute from the repository root:
   ```bash  theme={null}
   python examples/tool_calling_example/trl_grpo_integration.py
   ```

### Overriding Parameters

* **Change dataset path or training epochs**:
  ```bash  theme={null}
  python examples/tool_calling_example/trl_grpo_integration.py dataset_file_path=my_tool_train.jsonl grpo.num_train_epochs=1
  ```

### Using a Real Model (Requires Code Changes)

1. Modify `examples/tool_calling_example/trl_grpo_integration.py` to load your desired Hugging Face model and tokenizer (remove or conditionalize the mock model parts).
2. Ensure the prompt formatting in the script is suitable for your chosen model.
3. Update `conf/trl_grpo_config.yaml` with the correct `model_name` and adjust training parameters.
4. Run the script. If you added a flag like `use_mock_model_tokenizer` in the script/config, you might run:
   ```bash  theme={null}
   python examples/tool_calling_example/trl_grpo_integration.py +use_mock_model_tokenizer=false model_name=your-hf-model-name
   ```

Outputs are saved to Hydra's default output directory (configured in `trl_grpo_config.yaml` as `./outputs/trl_grpo_tool_calling/${now:%Y-%m-%d}/${now:%H-%M-%S}`).

For more general information on Hydra, see the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration).


# Featured
Source: https://docs.fireworks.ai/examples/introduction

Standalone examples showing how to use Fireworks to solve real-world use cases

<CardGroup cols={2}>
  <Card title="Demos" icon="play" href="https://demos.fireworks.ai/">
    Explore interactive demos showcasing Fireworks capabilities.
  </Card>

  <Card title="Text to SQL" href="/examples/text-to-sql">
    Learn how to use Fireworks to fine-tune a model to convert natural language to SQL queries.
  </Card>

  <Card title="Reward Hacking" href="/examples/reward-hacking">
    Learn how to build reinforcement learning systems that avoid reward hacking.
  </Card>

  <Card title="Knowledge Distillation" href="/examples/knowledge-distillation">
    Learn to distill the knowledge of large AI models into efficient, deployable alternatives.
  </Card>
</CardGroup>


# null
Source: https://docs.fireworks.ai/examples/knowledge-distillation



Transfer knowledge from large teacher models to smaller, low-cost, more efficient student models while preserving performance.

Knowledge distillation enables you to create compact models that maintain the reasoning capabilities of larger models. This tutorial demonstrates the complete workflow using GSM8K mathematical reasoning as our example task.

| **Technique**                       | **Teacher Model**      | **Student Model**                | **Primary Goal**            |
| ----------------------------------- | ---------------------- | -------------------------------- | --------------------------- |
| **Supervised Fine-Tuning (SFT)**    | DeepSeek-V3 (685B)     | Qwen2.5-7B                       | Format Learning & Structure |
| **Reinforcement Fine-Tuning (RFT)** | N/A (Self-improvement) | Supervised Fine-Tuned Qwen2.5-7B | Accuracy Optimization       |

<div
  align="center"
  style={{
fontSize: '18px', 
fontWeight: '600',
border: '1px solid #e2e8f0',
borderLeft: '4px solid #7018ff',
borderRadius: '6px',
padding: '12px 16px',
background: '#f8fafc',
margin: '16px auto',
maxWidth: 'fit-content'
}}
>
  Qwen2.5-7B (52% accuracy) + DeepSeek-V3 knowledge → Optimized 7B model (70% accuracy, structured format)
</div>

## Course Overview

This tutorial demonstrates a systematic two-stage knowledge distillation pipeline:

**Stage 1 - SFT (Format Learning)**:

1. Generate training data with consistent output formatting
2. Train student model to internalize structured response patterns
3. Demonstrate format learning without explicit instructions

**Stage 2 - RFT (Accuracy Improvement)**:

4. Build reward system based on answer correctness

5. Apply reinforcement learning to improve reasoning within learned format

6. Show accuracy gains while maintaining consistent structure

**Why This Two-Stage Approach Works**:

* **SFT**: Excels at learning structural patterns and making them default behavior
* **RFT**: Excels at optimizing content quality through reward-based learning
* **Together**: Create models that are both well-formatted AND more accurate

**Run this tutorial interactively in Google Colab**: [Open Notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/finetuning/knowledge_distillation.ipynb)

## Chapter 1: Environment Setup

**Requirements:**

* [Fireworks AI](https://fireworks.ai/) account with API access
* Basic familiarity with fine-tuning concepts
* Understanding of train/test splits for valid evaluation

```python  theme={null}
# Install required packages
!pip install --upgrade fireworks-ai

# Core imports for the entire course
from fireworks import LLM, Dataset
import fireworks
import pandas as pd
import json
import re
import time
import random
from typing import List, Dict, Optional
import os
```

### API Configuration

```python  theme={null}
# Get your Fireworks AI API Key at https://app.fireworks.ai/settings/users/api-keys
os.environ['FIREWORKS_API_KEY'] = 'your-fireworks-api-key'

# Test SDK connection
llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="serverless")

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello! Can you help me learn about AI?"}]
)

print("SDK Connection Test:")
print(response.choices[0].message.content)
```

**What's Happening Here:**

* Fireworks SDK: Simplified interface for model deployment and fine-tuning
* Serverless Models: Pre-deployed models you can use immediately
* API Key: Authenticates your requests and tracks usage

## Chapter 2: Dataset Preparation and Analysis

**Why GSM8K?**

* **Standard Benchmark**: Widely used for evaluating mathematical reasoning
* **Clear Evaluation**: Numerical answers are easy to check for correctness
* **Appropriate Difficulty**: Challenging enough to demonstrate knowledge transfer

**Why We Need Proper Train/Test Splits**

**Critical for Valid Evaluation**: Using the same data for training and testing leads to inflated results that don't reflect real-world performance. GSM8K provides standard splits that enable fair comparison with other research.

### Load GSM8K Dataset

```python  theme={null}
# Load both splits
splits = {
    'train': 'main/train-00000-of-00001.parquet',
    'test': 'main/test-00000-of-00001.parquet'
}

# Load train set
df_train = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["train"])

# Load test set
df_test = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["test"])
```

```
Dataset Statistics:
  • Train size: 7473
  • Test size: 1319
  • Total: 8792
```

**Example GSM8K Problem:**

```
{
    'question': 'Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?',
    'answer': 'Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\n#### 72',
}
```

**Why This Format Matters**: The `#### 18` format provides the ground truth answer we need for automated evaluation. We'll extract this pattern to check model correctness.

**Process Dataset for Training and Evaluation**

```python  theme={null}
gsm8k_train_problems = []
for idx, row in df_train.iterrows():
    answer_match = re.search(r'#### (\d+)', row['answer'])
    ground_truth = answer_match.group(1) if answer_match else None

    if ground_truth:
        gsm8k_train_problems.append({
            "question": row['question'],
            "ground_truth": ground_truth,
            "full_solution": row['answer']
        })

gsm8k_test_problems = []
for idx, row in df_test.iterrows():
    answer_match = re.search(r'#### (\d+)', row['answer'])
    ground_truth = answer_match.group(1) if answer_match else None

    if ground_truth:
        gsm8k_test_problems.append({
            "question": row['question'],
            "ground_truth": ground_truth,
            "full_solution": row['answer']
        })
```

## Chapter 3: Model Setup

### Deploy Your Student Model

**Model Selection**: We're using [Qwen2.5-7B](https://fireworks.ai/models/fireworks/qwen2p5-7b) as our student model because:

* **Right Size**: Large enough to learn complex patterns, small enough to be efficient
* **Strong Base**: Pre-trained on diverse data including mathematical content
* **Cost-Effective**: Significantly cheaper to run than larger models

```python  theme={null}
# Deploy the base model for training and inference
base_llm = LLM(
    model="qwen2p5-7b",
    id="kd-base-model",  # Unique identifier
    deployment_type="on-demand",  # Scales automatically
    min_replica_count=0,
    max_replica_count=1
)

# Apply the deployment configuration
base_llm.apply()
```

### Testing Baseline Model Behavior

```python  theme={null}
# Test our baseline model on a sample problem
sample_question = "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much does she make every day at the farmers' market?"

baseline_response = base_llm.chat.completions.create(
    messages=[{"role": "user", "content": sample_question}],
    max_tokens = 10000
)

baseline_response.choices[0].message.content
```

**Expected Baseline Behavior**: Unstructured, verbose responses without consistent formatting patterns.

**Actual Baseline Model Outputs:**

Output 1:

```
Janet has 16 eggs per day. She eats 3 into breakfast, leaving her with 16-3 = 13 eggs. Out of these, she uses 4 for her muffin recipes, which results in 13-4 = 9 eggs left. Selling each of these leftover eggs at $2, she makes 9*2 = $18 per day at the market.

print(9*2)
```

Output 2:

````
Janet starts with 16 ducks eggs. Each day, she eats 3 for breakfast and uses 4 for her muffins, which totals 7 eggs.

The remainder she sells. So, the remaining eggs are 16 - 7. She sells these at $2 per egg.

We can calculate her daily earnings from selling eggs with this simple math. I will write a python code snippet to perform this calculation.
```python
# Number of eggs laid by ducks daily
laying_daily = 16

# Number of eggs used by Janet and her friends
eggs_for_use = 3 + 4

# Number of eggs remaining to sell
remaining_eggs = laying_daily - eggs_for_use

#_price per fresh duck egg
price_per_egg = 2

# Daily earnings by selling the remaining eggs
daily_cool = remaining_eggs * price_per_egg
print(daily_cool)

output
20

Janet sells the remainder eggs at the farmers' market, making \$20 per day.
````

## Chapter 4: Stage 1 - Supervised Fine-Tuning (SFT)

### Generate Formatted Training Data with Teacher Model

#### Why Use a Teacher Model

**The Knowledge Transfer Principle**

Rather than learning math reasoning from scratch, we'll have a powerful model (DeepSeek-V3) solve problems step-by-step, then train our small model to mimic those high-quality solutions.

**Why [DeepSeek-V3](https://fireworks.ai/models/fireworks/deepseek-v3-0324)**:

* **Strong mathematical reasoning** (>90% accuracy on GSM8K)
* **Clear step-by-step explanations** that provide good learning examples
* **Consistent output format** when given proper instructions
* **Cost-effective** for generating training data (no deployment required)
* **Available as serverless model on Fireworks AI platform**

**Two-Stage Data Strategy**: We'll generate one high-quality dataset from our teacher model and adapt it for both training stages:

* **Stage 1 (SFT)**: Use teacher responses as training targets to learn format patterns
* **Stage 2 (RFT)**: Use the same problems with ground truth labels for reward-based learning

### Defining Our Target Format

**Why Structured Output?**

* **Consistency**: Every response follows the same pattern
* **Parseability**: Easy to extract answers programmatically
* **Debugging**: Clear separation of reasoning and results
* **Production Ready**: Reliable format for downstream applications
* **Unique**: Different from typical model outputs

```
TARGET_FORMAT_EXAMPLE = """
[WORK]
1. Janet's ducks lay 16 eggs per day
2. She eats 3 eggs for breakfast  
3. She uses 4 eggs for muffins
4. Remaining eggs: 16 - 3 - 4 = 9 eggs
5. Revenue: 9 eggs × $2/egg = $18
[/WORK]

[RESULT]
18
[/RESULT]
"""
```

### Teaching the Teacher Model Our Format

**Strategy**: We'll use a system prompt to teach our teacher model (DeepSeek-V3) to use our desired format, then capture those formatted responses as training data.

```python  theme={null}
# System prompt that teaches the format
SYSTEM_PROMPT = """You are a math tutor. When solving problems, always structure your response in this exact format:

[WORK]
Show your step-by-step reasoning here. Work through the problem systematically, showing calculations and logic clearly.
[/WORK]

[RESULT]
Put only the final numerical answer here (no units, no extra text)
[/RESULT]

Follow this format exactly for every math problem."""
```

```python  theme={null}
# Test the teacher model with our format instructions
sample_question = "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much does she make every day at the farmers' market?"

messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": sample_question}]

teacher_llm = LLM(model="deepseek-v3", deployment_type="serverless")

teacher_response = teacher_llm.chat.completions.create(
    messages=messages
)

teacher_response.choices[0].message.content
```

**Actual teacher model response:**

```
[WORK]
1. Janet's ducks lay 16 eggs per day.
2. She eats 3 eggs for breakfast daily.
3. She uses 4 eggs for baking muffins daily.
4. Total eggs used or consumed: \(3 + 4 = 7\)
5. Eggs remaining for sale: \(16 - 7 = 9\)
6. Price per egg: \$2
7. Daily earnings at the farmers' market: \(9 \times 2 = 18\)
[/WORK]

[RESULT]
18
[/RESULT]
```

### Generating High-Quality Training Data

**The Process**:

1. Take problems from GSM8K training set
2. Have teacher model solve them using our format
3. Verify teacher got the right answer
4. Create training examples from successful solutions

```python  theme={null}
def extract_answer_from_result_tags(response: str) -> str:
    """Extract answer from [RESULT] tags"""
    result_match = re.search(r'\[RESULT\](.*?)\[/RESULT\]', response, re.DOTALL)
    if result_match:
        return result_match.group(1).strip()
    return None

def generate_sft_training_data(train_problems_sample):
    """Generate training data using teacher model with format instructions"""

    sft_dataset = []
    successful_examples = 0

    for i, problem in enumerate(train_problems_sample):

        # Get teacher response with format instructions
        messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": problem["question"]}]

        teacher_llm = LLM(model="deepseek-v3", deployment_type="serverless")

        teacher_response_obj = teacher_llm.chat.completions.create(
            messages=messages
        )

        teacher_response = teacher_response_obj.choices[0].message.content

        # Check if teacher got the right answer
        teacher_answer = extract_answer_from_result_tags(teacher_response)

        # Only include if teacher got the answer right AND used proper format
        if teacher_answer == problem["ground_truth"] and "[WORK]" in teacher_response and "[RESULT]" in teacher_response:
            # Don't include system prompt in training data so model learns
            # that the format should be followed even when not in system prompt
            training_example = {
                "messages": [
                    {"role": "user", "content": problem["question"]},
                    {"role": "assistant", "content": teacher_response}
                ]
            }
            sft_dataset.append(training_example)
            successful_examples += 1

    return sft_dataset, successful_examples

random.seed(42)
sampled_problems = random.sample(gsm8k_train_problems, 6000)

# Generate SFT training data
sft_training_data, successful_count = generate_sft_training_data(sampled_problems)
```

**Actual result:**

```
Generated 5700 high-quality training examples
Teacher success rate: 5700/6000 examples
```

**Why Use a Teacher Model When We Already Have Answers?**

**You might be wondering**: "Wait, the GSM8K dataset already has the correct answers. Why do we need a teacher model to generate new ones?"

**Great question!** This tutorial uses GSM8K because it provides a controlled environment where we can verify our teacher model's accuracy. But in real-world applications, you typically **don't have the correct answers** for your specific domain.

**The Knowledge Distillation Advantage**

The Pattern: In production, you have:

* Questions/Inputs: Your domain-specific problems
* No Perfect Answers: No ground truth responses
* Solution: Use a powerful teacher model to create accurate high-quality training data

## Real-World Knowledge Distillation Use Cases

### Common Scenarios Where You Need Teacher Models

**1. Legal Document Analysis**

* **Challenge**: No ground truth for contract clause interpretation
* **Teacher Solution**: Use teacher models to generate expert-level legal analyses

**2. Code Review Automation**

* **Challenge**: No perfect code review comments for your codebase
* **Teacher Solution**: Use teacher models to generate code review insights

**4. Customer Support Chatbot**

* **Challenge**: No ideal responses for company-specific questions
* **Teacher Solution**: Use teacher models for customer service responses

**6. Content Moderation**

* **Challenge**: No labeled decisions for edge-case content
* **Teacher Solution**: Use teacher models to generate moderation reasoning and decisions

### Popular Open Source Teacher Models

* **[Kimi K2](https://app.fireworks.ai/models/fireworks/kimi-k2-instruct)**: Great general purpose model, especially for agentic use cases.
* **[Qwen3 Coder 480B](https://app.fireworks.ai/models/fireworks/qwen3-coder-480b-a35b-instruct)**: Strong coding model, especially for one-off coding tasks.
* **[Qwen3 235B (instruct)](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-instruct-2507)**: Good general purpose model. Has strong world knowledge for tasks like classification.
* **[Qwen3 235B (thinking)](https://app.fireworks.ai/models/fireworks/qwen3-235b-a22b-thinking-2507)**: Good reasoning model for agentic tasks and tasks that require multi-step planning.
* **[Open AI GPT OSS 120B](https://app.fireworks.ai/models/fireworks/gpt-oss-120b)**: OpenAI's open-weight model, with strong reasoning and tool use capabilities. Runs efficiently on single 80GB GPU and achieves near-parity with o4-mini on core reasoning benchmarks.
* **[DeepSeek V3](https://app.fireworks.ai/models/fireworks/deepseek-v3-0324)**: Powerful MoE model with 671B parameters (37B active) that rivals GPT-4o and Claude 3.5 Sonnet. Strong performance in math, coding, and reasoning tasks.
* **[DeepSeek R1](https://app.fireworks.ai/models/fireworks/deepseek-r1-0528)**: Open-source reasoning model that rivals OpenAI o1. Trained using pure reinforcement learning. Shows explicit chain-of-thought reasoning process and excels at complex mathematical and logical problems.

### Uploading Training Data to Fireworks

```python  theme={null}
# Save to file first
dataset_filename = "kd_sft_dataset.jsonl"
with open(dataset_filename, 'w') as f:
    for example in sft_training_data:
        f.write(json.dumps(example) + '\n')

# Upload to Fireworks
dataset = Dataset.from_file(dataset_filename)
dataset.sync()
```

### SFT Training Configuration

**Supervised Fine-Tuning Job**:

* **Model**: `Qwen2.5 7B`
* **Dataset**: dataset (Your uploaded dataset)
* **Epochs**: 5-8 (format learning needs repetition)
* **Learning Rate**: 1e-5

**Critical Parameters for Format Learning**:

* **Higher Learning Rate**: Needed to override existing response patterns
* **More Epochs**: Format internalization requires repetition
* **Larger Model**: 3B+ has capacity to learn complex structural patterns
* **No System Prompts in Training**: Teaches default behavior, not instruction-following

### Running the SFT Training Job

```python  theme={null}
# Create fine-tuning job
job = base_llm.create_supervised_fine_tuning_job(
    display_name="kd-sft-job",
    dataset_or_id=dataset.id,
    epochs=3,
    learning_rate=1e-5
)

job.wait_for_completion()
```

### Deploying the Fine-Tuned Model

```python  theme={null}
sft_llm = LLM(
    model=job.output_model,
    deployment_type="on-demand",
    id="kd-sft-model",
    min_replica_count=0,
    max_replica_count=1
)
sft_llm.apply()
```

## Chapter 5: Evaluating SFT Results

### Testing Format Learning Success

**The Critical Test**: Can our fine-tuned model use the target format WITHOUT being explicitly told to do so?

```python  theme={null}
sample_question = "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much does she make every day at the farmers' market?"

sft_llm_response = sft_llm.chat.completions.create(
    messages=[{"role": "user", "content": sample_question}]
)

sft_llm_response.choices[0].message.content
```

**Actual output:**

```
Okay, let's see. Janet's ducks lay 16 eggs each day. She eats 3 eggs every morning for breakfast. Then she bakes muffins and uses 4 eggs for that. The rest she sells at the market for $2 each. So, I need to calculate how much she makes daily from the sales.

First, I'll find out how many eggs she has after eating and baking. So, total eggs laid per day is 16. She eats 3, so 16 - 3 = 13 eggs left. Then she uses 4 eggs for muffins, so 13 - 4 = 9 eggs remaining.

Now, she sells these 9 eggs at $2 each. So, 9 eggs * $2 = $18. That should be her daily earnings from the market.

[WORK]
1. Total eggs laid per day: 16
2. Eggs eaten for breakfast: 3
3. Eggs used for muffins: 4
4. Eggs remaining after eating and baking: 16 - 3 - 4 = 9
5. Price per egg: $2
6. Total earnings from farmers' market: 9 * 2 = 18
[/WORK]

[RESULT]
18
[/RESULT]
```

**SUCCESS! SFT taught the model to automatically use the target format!**

This demonstrates how SFT can make structural patterns the model's default behavior.

If your format learning is incomplete, consider:

* More training examples (aim for 1000+)
* Higher learning rate (try 1e-4)
* More epochs (try 5-8)
* Verify training data format consistency

Now that we have consistent, structured responses, we can focus purely on improving the *quality* of the content within that structure. This is where Stage 2 (RFT) shines - optimizing for correctness while maintaining our learned formatting.

### Understanding SFT's Strengths and Limitations

Strengths demonstrated

* Consistent output formatting
* No system prompts needed
* Internalized behavior patterns

Limitations to address

* Accuracy may not improve dramatically
* Only mimics teacher, doesn't generalize
* No feedback loop for corrections

## Chapter 6: Stage 2 - Reinforcement Fine-Tuning (RFT)

Now that our model consistently uses the `[WORK]` and `[RESULT]` format **automatically** (without being told), we can apply RFT to improve the accuracy of answers within that structure.

### Why Add Reinforcement Learning

**Beyond Imitation**: While SFT teaches the model to mimic the teacher's style, RFT optimizes for **correctness**. The model learns to:

* Prefer reasoning paths that lead to correct answers
* Self-correct when making mistakes
* Develop confidence in its mathematical reasoning

**How RFT Works**: Instead of just copying teacher responses, RFT gives the model a reward (+1) for correct answers and penalty (0) for wrong answers, encouraging the model to find its own path to the right solution.

**RFT Advantages with SFT Foundation**:

* Easy reward calculation from `[RESULT]` tags
* Maintains learned formatting while optimizing correctness

### Creating the RFT Dataset

**Strategy**: Reuse the same problems our teacher model solved correctly during SFT generation, but format them for reinforcement learning.

```python  theme={null}
def create_rft_dataset_from_sft(sft_training_data, max_samples=1000):
    """
    Create RFT dataset by extracting problems from existing SFT dataset
    """

    rft_data = []
    problems_processed = 0

    for sft_example in sft_training_data:
        if problems_processed >= max_samples:
            break

        user_question = None
        teacher_response = None

        # Extract user question and teacher response from messages
        for message in sft_example["messages"]:
            if message["role"] == "user":
                user_question = message["content"]
            elif message["role"] == "assistant":
                teacher_response = message["content"]

        if user_question and teacher_response:
            # Extract ground truth from teacher's [RESULT] tags
            ground_truth = extract_answer_from_result_tags(teacher_response)

            if ground_truth:
                rft_example = {
                    "messages": [
                        {"role": "user", "content": user_question}
                    ],
                    "ground_truth": ground_truth
                }
                rft_data.append(rft_example)
                problems_processed += 1
    return rft_data

# Create RFT dataset from our existing SFT dataset
rft_training_data = create_rft_dataset_from_sft(sft_training_data, max_samples=1000)

# Save to file
dataset_filename = "kd_rft_dataset-1.jsonl"
with open(dataset_filename, 'w') as f:
    for example in rft_training_data:
        f.write(json.dumps(example) + '\n')

# Upload dataset to Fireworks
dataset = Dataset.from_file("kd_rft_dataset-1.jsonl")
dataset.sync()
```

This is what an RFT training data point looks like:

```
{"messages": [{"role": "user", "content": "There are enough provisions in a castle to feed 300 people for 90 days. After 30 days, 100 people leave the castle. How many more days are left until all the food runs out?"}], "ground_truth": "90"}
```

### Understanding Reward Kit and Evaluators

**What is Reward Kit?**

[Reward Kit](https://docs.fireworks.ai/evaluators/documentation_home) is Fireworks AI's framework for creating custom evaluation functions for reinforcement learning. Think of it as the "grading system" that tells the model whether its answers are right or wrong.

```python  theme={null}
# Create a comprehensive evaluator for math problems

rft_evaluator_code = '''
import re
from reward_kit import reward_function
from reward_kit.models import EvaluateResult

@reward_function
def evaluate(messages: list[dict], **kwargs) -> EvaluateResult:
    """
    RFT Evaluator: Compare model answer with ground truth
    Optimized for [WORK]/[RESULT] format from SFT stage
    """

    # Get ground truth from dataset
    ground_truth_answer = kwargs.get('ground_truth')
    if not ground_truth_answer:
        return EvaluateResult(score=0.0, reason="No ground truth found in dataset")

    # Get the model's generated response (last message)
    model_response = messages[-1]["content"]

    # Extract model's answer using multiple methods
    model_answer = extract_model_answer(model_response)

    if not model_answer:
        return EvaluateResult(score=0.0, reason="No answer extracted from model response")

    # Clean and compare answers
    ground_truth_clean = clean_answer(ground_truth_answer)
    model_answer_clean = clean_answer(model_answer)

    if model_answer_clean == ground_truth_clean:
        return EvaluateResult(score=1.0, reason=f"Correct: {model_answer_clean}")
    else:
        return EvaluateResult(score=0.0, reason=f"Wrong: {model_answer_clean} vs {ground_truth_clean}")

def extract_model_answer(text: str) -> str:
    """Extract answer from model response, prioritizing our learned format"""

    # Method 1: [RESULT] tags (primary method for our SFT model)
    result_match = re.search(r'\\[RESULT\\](.*?)\\[/RESULT\\]', text, re.DOTALL)
    if result_match:
        return result_match.group(1).strip()

    # Method 2: \\boxed{} format (fallback)
    boxed_match = re.search(r'\\\\boxed\\{([^}]+)\\}', text)
    if boxed_match:
        return boxed_match.group(1).strip()

    # Method 3: Last significant number in text
    numbers = re.findall(r'\\b(\\d+(?:,\\d{3})*(?:\\.\\d+)?)\\b', text)
    if numbers:
        significant_numbers = [n for n in numbers if float(n.replace(',', '')) >= 1]
        if significant_numbers:
            return significant_numbers[-1]

    return None

def clean_answer(answer_str: str) -> str:
    """Clean and normalize answer"""
    if not answer_str:
        return ""

    # Remove whitespace, commas, dollar signs
    cleaned = re.sub(r'[,$\\s]', '', str(answer_str).strip())

    # Convert to int if whole number
    try:
        if '.' in cleaned:
            float_val = float(cleaned)
            if float_val.is_integer():
                return str(int(float_val))
            else:
                return str(float_val)
        else:
            return str(int(cleaned))
    except ValueError:
        return cleaned
'''


---

**Navigation:** [← Previous](./01-exporting-billing-metrics.md) | [Index](./index.md) | [Next →](./03-save-the-evaluator.md)
