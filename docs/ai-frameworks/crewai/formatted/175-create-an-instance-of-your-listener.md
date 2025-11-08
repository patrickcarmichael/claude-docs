---
title: "Crewai: Create an instance of your listener"
description: "Create an instance of your listener section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an instance of your listener

knowledge_monitor = KnowledgeMonitorListener()
```

For more information on using events, see the [Event Listeners](https://docs.crewai.com/concepts/event-listener) documentation.

### Custom Knowledge Sources

CrewAI allows you to create custom knowledge sources for any type of data by extending the `BaseKnowledgeSource` class. Let's create a practical example that fetches and processes space news articles.

#### Space News Knowledge Source Example

<CodeGroup>
  ```python Code theme={null}
  from crewai import Agent, Task, Crew, Process, LLM
  from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
  import requests
  from datetime import datetime
  from typing import Dict, Any
  from pydantic import BaseModel, Field

  class SpaceNewsKnowledgeSource(BaseKnowledgeSource):
      """Knowledge source that fetches data from Space News API."""

      api_endpoint: str = Field(description="API endpoint URL")
      limit: int = Field(default=10, description="Number of articles to fetch")

      def load_content(self) -> Dict[Any, str]:
          """Fetch and format space news articles."""
          try:
              response = requests.get(
                  f"{self.api_endpoint}?limit={self.limit}"
              )
              response.raise_for_status()

              data = response.json()
              articles = data.get('results', [])

              formatted_data = self.validate_content(articles)
              return {self.api_endpoint: formatted_data}
          except Exception as e:
              raise ValueError(f"Failed to fetch space news: {str(e)}")

      def validate_content(self, articles: list) -> str:
          """Format articles into readable text."""
          formatted = "Space News Articles:\n\n"
          for article in articles:
              formatted += f"""
                  Title: {article['title']}
                  Published: {article['published_at']}
                  Summary: {article['summary']}
                  News Site: {article['news_site']}
                  URL: {article['url']}
                  -------------------"""
          return formatted

      def add(self) -> None:
          """Process and store the articles."""
          content = self.load_content()
          for _, text in content.items():
              chunks = self._chunk_text(text)
              self.chunks.extend(chunks)

          self._save_documents()

  # Create knowledge source
  recent_news = SpaceNewsKnowledgeSource(
      api_endpoint="https://api.spaceflightnewsapi.net/v4/articles",
      limit=10,
  )

  # Create specialized agent
  space_analyst = Agent(
      role="Space News Analyst",
      goal="Answer questions about space news accurately and comprehensively",
      backstory="""You are a space industry analyst with expertise in space exploration,
      satellite technology, and space industry trends. You excel at answering questions
      about space news and providing detailed, accurate information.""",
      knowledge_sources=[recent_news],
      llm=LLM(model="gpt-4", temperature=0.0)
  )

  # Create task that handles user questions
  analysis_task = Task(
      description="Answer this question about space news: {user_question}",
      expected_output="A detailed answer based on the recent space news articles",
      agent=space_analyst
  )

  # Create and run the crew
  crew = Crew(
      agents=[space_analyst],
      tasks=[analysis_task],
      verbose=True,
      process=Process.sequential
  )

  # Example usage
  result = crew.kickoff(
      inputs={"user_question": "What are the latest developments in space exploration?"}
  )
  ```

  ```output Output theme={null}
  # Agent: Space News Analyst
  ## Task: Answer this question about space news: What are the latest developments in space exploration?

  # Agent: Space News Analyst
  ## Final Answer:
  The latest developments in space exploration, based on recent space news articles, include the following:

  1. SpaceX has received the final regulatory approvals to proceed with the second integrated Starship/Super Heavy launch, scheduled for as soon as the morning of Nov. 17, 2023. This is a significant step in SpaceX's ambitious plans for space exploration and colonization. [Source: SpaceNews](https://spacenews.com/starship-cleared-for-nov-17-launch/)

  2. SpaceX has also informed the US Federal Communications Commission (FCC) that it plans to begin launching its first next-generation Starlink Gen2 satellites. This represents a major upgrade to the Starlink satellite internet service, which aims to provide high-speed internet access worldwide. [Source: Teslarati](https://www.teslarati.com/spacex-first-starlink-gen2-satellite-launch-2022/)

  3. AI startup Synthetaic has raised $15 million in Series B funding. The company uses artificial intelligence to analyze data from space and air sensors, which could have significant applications in space exploration and satellite technology. [Source: SpaceNews](https://spacenews.com/ai-startup-synthetaic-raises-15-million-in-series-b-funding/)

  4. The Space Force has formally established a unit within the U.S. Indo-Pacific Command, marking a permanent presence in the Indo-Pacific region. This could have significant implications for space security and geopolitics. [Source: SpaceNews](https://spacenews.com/space-force-establishes-permanent-presence-in-indo-pacific-region/)

  5. Slingshot Aerospace, a space tracking and data analytics company, is expanding its network of ground-based optical telescopes to increase coverage of low Earth orbit. This could improve our ability to track and analyze objects in low Earth orbit, including satellites and space debris. [Source: SpaceNews](https://spacenews.com/slingshots-space-tracking-network-to-extend-coverage-of-low-earth-orbit/)

  6. The National Natural Science Foundation of China has outlined a five-year project for researchers to study the assembly of ultra-large spacecraft. This could lead to significant advancements in spacecraft technology and space exploration capabilities. [Source: SpaceNews](https://spacenews.com/china-researching-challenges-of-kilometer-scale-ultra-large-spacecraft/)

  7. The Center for AEroSpace Autonomy Research (CAESAR) at Stanford University is focusing on spacecraft autonomy. The center held a kickoff event on May 22, 2024, to highlight the industry, academia, and government collaboration it seeks to foster. This could lead to significant advancements in autonomous spacecraft technology. [Source: SpaceNews](https://spacenews.com/stanford-center-focuses-on-spacecraft-autonomy/)
  ```
</CodeGroup>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Behind the scenes, this might be rewritten as:](./174-behind-the-scenes-this-might-be-rewritten-as.md)

**Next:** [Debugging and Troubleshooting →](./176-debugging-and-troubleshooting.md)
