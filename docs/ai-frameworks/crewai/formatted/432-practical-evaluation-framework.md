---
title: "Crewai: Practical Evaluation Framework"
description: "Practical Evaluation Framework section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Practical Evaluation Framework


To determine the right approach for your specific use case, follow this step-by-step evaluation framework:

### Step 1: Assess Complexity

Rate your application's complexity on a scale of 1-10 by considering:

1. **Number of steps**: How many distinct operations are required?
   * 1-3 steps: Low complexity (1-3)
   * 4-7 steps: Medium complexity (4-7)
   * 8+ steps: High complexity (8-10)

2. **Interdependencies**: How interconnected are the different parts?
   * Few dependencies: Low complexity (1-3)
   * Some dependencies: Medium complexity (4-7)
   * Many complex dependencies: High complexity (8-10)

3. **Conditional logic**: How much branching and decision-making is needed?
   * Linear process: Low complexity (1-3)
   * Some branching: Medium complexity (4-7)
   * Complex decision trees: High complexity (8-10)

4. **Domain knowledge**: How specialized is the knowledge required?
   * General knowledge: Low complexity (1-3)
   * Some specialized knowledge: Medium complexity (4-7)
   * Deep expertise in multiple domains: High complexity (8-10)

Calculate your average score to determine overall complexity.

### Step 2: Assess Precision Requirements

Rate your precision requirements on a scale of 1-10 by considering:

1. **Output structure**: How structured must the output be?
   * Free-form text: Low precision (1-3)
   * Semi-structured: Medium precision (4-7)
   * Strictly formatted (JSON, XML): High precision (8-10)

2. **Accuracy needs**: How important is factual accuracy?
   * Creative content: Low precision (1-3)
   * Informational content: Medium precision (4-7)
   * Critical information: High precision (8-10)

3. **Reproducibility**: How consistent must results be across runs?
   * Variation acceptable: Low precision (1-3)
   * Some consistency needed: Medium precision (4-7)
   * Exact reproducibility required: High precision (8-10)

4. **Error tolerance**: What is the impact of errors?
   * Low impact: Low precision (1-3)
   * Moderate impact: Medium precision (4-7)
   * High impact: High precision (8-10)

Calculate your average score to determine overall precision requirements.

### Step 3: Map to the Matrix

Plot your complexity and precision scores on the matrix:

* **Low Complexity (1-4), Low Precision (1-4)**: Simple Crews
* **Low Complexity (1-4), High Precision (5-10)**: Flows with direct LLM calls
* **High Complexity (5-10), Low Precision (1-4)**: Complex Crews
* **High Complexity (5-10), High Precision (5-10)**: Flows orchestrating Crews

### Step 4: Consider Additional Factors

Beyond complexity and precision, consider:

1. **Development time**: Crews are often faster to prototype
2. **Maintenance needs**: Flows provide better long-term maintainability
3. **Team expertise**: Consider your team's familiarity with different approaches
4. **Scalability requirements**: Flows typically scale better for complex applications
5. **Integration needs**: Consider how the solution will integrate with existing systems

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the flow](./431-run-the-flow.md)

**Next:** [Conclusion →](./433-conclusion.md)
