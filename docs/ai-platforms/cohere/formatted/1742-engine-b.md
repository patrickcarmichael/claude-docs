---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Engine B:

{engine_b_results}
"""

def format_results(results):
    """Format search results in a readable way"""
    formatted = []
    for i, result in enumerate(results):
        formatted.append(f"Result {i+1}: {result[:200]}...")
    return "\n\n".join(formatted)

def judge_query(query, engine_a_results, engine_b_results, model_name):
    """Use a single model to judge which engine has better results"""
    agent = Agent(model_name, system_prompt=SYSTEM_PROMPT)
    
    # Format the results

    engine_a_formatted = format_results(engine_a_results)
    engine_b_formatted = format_results(engine_b_results)
    
    # Create the prompt

    prompt = PROMPT_TEMPLATE.format(
        query=query,
        engine_a_results=engine_a_formatted,
        engine_b_results=engine_b_formatted
    )
    
    # Get the model's judgment

    response = agent.run_sync(prompt)
    return response.data

def evaluate_search_results(reranked_results, regular_results, models):
    """
    Evaluate both sets of search results using multiple models.
    
    Args:
        reranked_results: List of dictionaries with 'question' and 'search_results'
        regular_results: List of dictionaries with 'question' and 'search_results'
        models: List of model names to use as judges
    
    Returns:
        DataFrame with evaluation results
    """
    # Prepare data structure for results

    evaluation_results = []
    
    # Evaluate each query

    for i in range(len(reranked_results)):
        query = reranked_results[i]['question']
        engine_a_results = reranked_results[i]['search_results']  # Reranked results

        engine_b_results = regular_results[i]['search_results']   # Regular results

        
        # Get judgments from each model

        judgments = []
        for model in models:
            judgment = judge_query(query, engine_a_results, engine_b_results, model)
            judgments.append(judgment)
        
        # Determine winner by majority vote

        votes = Counter(judgments)
        if votes["Engine A"] > votes["Engine B"]:
            winner = "Engine A"
        elif votes["Engine B"] > votes["Engine A"]:
            winner = "Engine B"
        else:
            winner = "Tie"
        
        # Add results for this query

        row = [query] + judgments + [winner]
        evaluation_results.append(row)
    
    # Create DataFrame

    column_names = ["question"] + [f"judge_{i+1} ({model})" for i, model in enumerate(models)] + ["winner"]
    df = pd.DataFrame(evaluation_results, columns=column_names)
    
    return df
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
