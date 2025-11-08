# GETTING STARTED

**Navigation:** [← Previous](./13-comparison-with-other-frameworks.md) | [Index](./index.md) | [Next →](./15-learning-resources.md)

---

GETTING STARTED
================================================================================

1. Installation:
   pip install haystack-ai

2. Basic RAG Pipeline:
   from haystack import Pipeline
   from haystack.components.retrievers import DensePassageRetriever
   from haystack.components.generators import OpenAIGenerator

   pipeline = Pipeline()
   pipeline.add_component("retriever", retriever)
   pipeline.add_component("generator", generator)
   pipeline.connect("retriever", "generator")

3. Run Pipeline:
   result = pipeline.run({"retriever": {"query": "Your question"}})

4. Deploy:
   - Use Hayhooks for REST API
   - Use deepset Studio for visual management
   - Deploy to production with Docker/Kubernetes

================================================================================

---

**Navigation:** [← Previous](./13-comparison-with-other-frameworks.md) | [Index](./index.md) | [Next →](./15-learning-resources.md)
