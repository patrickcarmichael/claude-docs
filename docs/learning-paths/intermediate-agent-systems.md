# Intermediate Agent Systems Path

Build sophisticated multi-step agents and coordinate teams of specialized AI agents.

**Total Duration**: 3-4 weeks | **Prerequisites**: [Beginner AI Development Path](./beginner-ai-development.md) (or equivalent knowledge)

---

## Learning Path Overview

This path teaches you to build autonomous AI systems that can reason, plan, and execute complex tasks. You'll learn:
- LangChain fundamentals for complex LLM applications
- State management and multi-step reasoning with LangGraph
- Multi-agent orchestration with CrewAI
- Tool integration and autonomous action

---

## Phase 1: LangChain Fundamentals (Days 1-6)
**Duration**: 8-10 hours | **Skill Level**: Intermediate

### 1.1 LangChain Essentials
- **Read**: [LangChain Framework Overview](../ai-frameworks/langchain/)
  - Understand LangChain architecture
  - Learn core concepts: chains, agents, memory
  - Review ecosystem and integrations
  - Estimated time: 45 minutes

- **Read**: [LangChain Full Documentation](../ai-frameworks/langchain/llms-full.txt)
  - Study chains and their composition
  - Learn about agents and tools
  - Understand memory management
  - Explore integrations
  - Estimated time: 2 hours (skim for reference)

### 1.2 Building Basic Chains
- **Create**: LangChain chain for text processing
  ```python
  from langchain.llms import Anthropic
  from langchain.prompts import PromptTemplate
  from langchain.chains import LLMChain

  llm = Anthropic()

  prompt = PromptTemplate(
      input_variables=["topic"],
      template="Write a detailed essay about {topic}"
  )

  chain = LLMChain(llm=llm, prompt=prompt)
  result = chain.run(topic="artificial intelligence")
  ```

- **Practice**:
  - Create chains for different tasks
  - Combine multiple prompts
  - Add custom logic between steps
  - Estimated time: 1.5 hours

### 1.3 Advanced Chains
- **Create**: Sequential chain combining multiple steps
  ```python
  from langchain.chains import SequentialChain

  # Chain 1: Generate outline
  outline_chain = LLMChain(llm=llm, prompt=outline_prompt)

  # Chain 2: Expand outline
  expand_chain = LLMChain(llm=llm, prompt=expand_prompt)

  # Combine chains
  overall_chain = SequentialChain(
      chains=[outline_chain, expand_chain],
      input_variables=["topic"],
      output_variables=["outline", "full_text"]
  )
  ```

- **Practice**:
  - Build multi-step workflows
  - Pass data between chains
  - Handle chain errors
  - Estimated time: 1.5 hours

### 1.4 Conversation Memory
- **Create**: Stateful conversation agent
  ```python
  from langchain.memory import ConversationBufferMemory
  from langchain.chains import ConversationChain

  memory = ConversationBufferMemory()

  conversation = ConversationChain(
      llm=llm,
      memory=memory,
      verbose=True
  )

  # Maintains conversation history automatically
  response = conversation.predict(input="What's AI?")
  ```

- **Practice**:
  - Experiment with different memory types
  - Implement conversation summarization
  - Add custom memory retrievers
  - Estimated time: 1.5 hours

### 1.5 Tool Use and Agents
- **Create**: Simple agent with tools
  ```python
  from langchain.agents import initialize_agent, Tool
  from langchain.tools import tool

  @tool
  def get_weather(location: str) -> str:
      """Get weather for a location"""
      return f"Weather in {location}: 72F, sunny"

  tools = [
      Tool(
          name="Weather",
          func=get_weather,
          description="Get weather information"
      )
  ]

  agent = initialize_agent(
      tools,
      llm,
      agent="zero-shot-react-description",
      verbose=True
  )

  result = agent.run("What's the weather in NYC?")
  ```

- **Practice**:
  - Define multiple tools
  - Build agents that choose tools
  - Debug tool selection
  - Estimated time: 2 hours

**Checkpoint**: Build a conversational agent with tool use that can complete multi-step tasks

---

## Phase 2: LangGraph for Complex Workflows (Days 7-12)
**Duration**: 10-12 hours | **Skill Level**: Intermediate to Advanced

### 2.1 Understanding LangGraph
- **Read**: [LangGraph Framework Overview](../ai-frameworks/langgraph/)
  - Learn graph-based workflows
  - Understand state management
  - Review control flow concepts
  - Estimated time: 45 minutes

- **Read**: [LangGraph Full Documentation](../ai-frameworks/langgraph/llms-full.txt)
  - Study graph structure
  - Learn state persistence
  - Understand checkpointing
  - Explore advanced patterns
  - Estimated time: 2 hours (skim for reference)

### 2.2 Basic Graph Agents
- **Create**: Simple graph-based agent
  ```python
  from langgraph.graph import StateGraph, START, END
  from typing import TypedDict

  class AgentState(TypedDict):
      input: str
      messages: list
      output: str

  def process_input(state: AgentState):
      # Process input
      return {"messages": state["messages"] + [{"role": "user", "content": state["input"]}]}

  def call_llm(state: AgentState):
      # Call Claude
      response = llm.invoke(state["messages"])
      return {"messages": state["messages"] + [{"role": "assistant", "content": response}]}

  # Build graph
  workflow = StateGraph(AgentState)
  workflow.add_node("process", process_input)
  workflow.add_node("llm", call_llm)
  workflow.add_edge(START, "process")
  workflow.add_edge("process", "llm")
  workflow.add_edge("llm", END)

  app = workflow.compile()
  ```

- **Practice**:
  - Create graph structures
  - Add nodes and edges
  - Test state transitions
  - Estimated time: 2 hours

### 2.3 Conditional Logic and Routing
- **Create**: Agent with decision logic
  ```python
  def should_use_tool(state: AgentState):
      last_message = state["messages"][-1]
      if "tool" in last_message.lower():
          return "use_tool"
      return "generate_response"

  workflow = StateGraph(AgentState)
  # ... add nodes ...

  # Add conditional edge
  workflow.add_conditional_edges(
      "llm",
      should_use_tool,
      {
          "use_tool": "tool_node",
          "generate_response": END
      }
  )
  ```

- **Practice**:
  - Implement complex decision trees
  - Build branching workflows
  - Add loop logic
  - Estimated time: 2 hours

### 2.4 Advanced Graph Patterns
- **Create**: Agent with reflection and refinement
  ```python
  # Add reflection node
  def reflect(state: AgentState):
      # Review output and refine
      return state

  # Add looping back for improvement
  workflow.add_node("reflect", reflect)
  workflow.add_edge("generate_response", "reflect")

  # Conditional: keep or refine
  def should_refine(state):
      # Check if output meets criteria
      if meets_criteria(state["output"]):
          return END
      return "refine"
  ```

- **Practice**:
  - Build agents that self-evaluate
  - Implement refinement loops
  - Add multiple reasoning steps
  - Estimated time: 2 hours

### 2.5 Persistence and Checkpointing
- **Create**: Agent with conversation persistence
  ```python
  from langgraph.checkpoint.memory import MemorySaver

  memory = MemorySaver()

  app = workflow.compile(
      checkpointer=memory,
      interrupt_before=["tool_call"]  # Human-in-the-loop
  )

  # Continue from checkpoint
  config = {"configurable": {"thread_id": "1"}}
  state = app.invoke(input_data, config)
  ```

- **Practice**:
  - Save and restore agent states
  - Implement human-in-the-loop
  - Handle long-running workflows
  - Estimated time: 1.5 hours

**Checkpoint**: Build a complex agent with multi-step reasoning, tool use, and state persistence

---

## Phase 3: Multi-Agent Systems with CrewAI (Days 13-18)
**Duration**: 8-10 hours | **Skill Level**: Intermediate to Advanced

### 3.1 CrewAI Fundamentals
- **Read**: [CrewAI Framework Overview](../ai-frameworks/crewai/)
  - Learn multi-agent concepts
  - Understand agent roles and tasks
  - Review crew coordination
  - Estimated time: 45 minutes

- **Read**: [CrewAI Full Documentation](../ai-frameworks/crewai/llms-full.txt)
  - Study agent configuration
  - Learn task definitions
  - Understand crew execution
  - Explore tool integration
  - Estimated time: 2 hours (skim for reference)

### 3.2 Your First Crew
- **Create**: Simple multi-agent system
  ```python
  from crewai import Agent, Task, Crew
  from langchain.llms import Anthropic

  # Define agents
  researcher = Agent(
      role="Researcher",
      goal="Find and analyze information",
      backstory="Expert researcher with deep knowledge",
      llm=Anthropic()
  )

  writer = Agent(
      role="Writer",
      goal="Create compelling content",
      backstory="Award-winning content writer",
      llm=Anthropic()
  )

  # Define tasks
  research_task = Task(
      description="Research topic: {topic}",
      agent=researcher,
      expected_output="Detailed research findings"
  )

  write_task = Task(
      description="Write article based on research",
      agent=writer,
      expected_output="Well-written article"
  )

  # Create crew
  crew = Crew(
      agents=[researcher, writer],
      tasks=[research_task, write_task],
      verbose=True
  )

  # Execute
  result = crew.kickoff(inputs={"topic": "AI Future"})
  ```

- **Practice**:
  - Create agents with specific roles
  - Define clear tasks
  - Execute crews sequentially
  - Estimated time: 2 hours

### 3.3 Advanced Crew Configuration
- **Create**: Crew with tool integration
  ```python
  from crewai_tools import SerperDevTool

  # Add tools to agents
  researcher = Agent(
      role="Researcher",
      goal="Find information",
      tools=[SerperDevTool()],  # Web search
      llm=Anthropic()
  )

  # Configure crew execution
  crew = Crew(
      agents=[researcher, analyst, writer],
      tasks=[search_task, analyze_task, write_task],
      process=Process.hierarchical,  # Hierarchical management
      manager_llm=Anthropic()
  )
  ```

- **Practice**:
  - Add different tools to agents
  - Experiment with execution modes
  - Build hierarchical teams
  - Estimated time: 2 hours

### 3.4 Tool Integration
- **Create**: Custom tools for crew
  ```python
  from crewai_tools import BaseTool

  class DataFetcher(BaseTool):
      name: str = "data_fetcher"
      description: str = "Fetch data from database"

      def _run(self, query: str) -> str:
          # Implement data fetching
          return results

  agent = Agent(
      role="Analyst",
      tools=[DataFetcher()]
  )
  ```

- **Practice**:
  - Create custom tools
  - Integrate external APIs
  - Handle tool errors
  - Estimated time: 1.5 hours

### 3.5 Complex Multi-Agent Workflows
- **Create**: Project with 5+ coordinated agents
  - Research Agent: Gathers information
  - Analyst Agent: Analyzes data
  - Writer Agent: Creates content
  - Editor Agent: Reviews and refines
  - Manager Agent: Coordinates workflow

- **Practice**:
  - Build realistic team structures
  - Handle agent communication
  - Measure coordination effectiveness
  - Estimated time: 2 hours

**Checkpoint**: Build a multi-agent crew that coordinates to solve complex problems

---

## Phase 4: Integration and Production (Days 19-21)
**Duration**: 6-8 hours | **Skill Level**: Advanced

### 4.1 Comparing Frameworks
- **Analyze**: When to use each framework
  - LangChain: General LLM applications
  - LangGraph: Complex stateful workflows
  - CrewAI: Multi-agent collaboration

- **Practice**: Choose the right tool for different use cases

### 4.2 Building Hybrid Systems
- **Create**: Application combining multiple frameworks
  ```python
  # Use CrewAI for research task
  # Use LangGraph for decision logic
  # Use LangChain for data processing
  ```

- **Practice**: Build realistic applications using appropriate tools

### 4.3 Error Handling and Robustness
- **Implement**:
  - Retry logic for failed tool calls
  - Error recovery strategies
  - Graceful degradation
  - Logging and monitoring

- **Test**: Edge cases and failure scenarios

### 4.4 Performance Optimization
- **Measure**: Agent latency and costs
- **Optimize**:
  - Caching strategies
  - Batch processing
  - Model selection
  - Token usage

**Checkpoint**: Production-ready agent system with error handling and monitoring

---

## Next Steps

You've mastered intermediate agent systems! Next options:

1. **Advanced Production RAG**: [Advanced Production RAG Path](./advanced-production-rag.md)
   - Production-scale vector databases
   - Monitoring and optimization
   - Deployment strategies

2. **Full-Stack Integration**: [Full-Stack AI Engineer Path](./full-stack-ai-engineer.md)
   - Complete end-to-end systems
   - Web applications with agents
   - Production deployment

3. **Deepen Knowledge**:
   - [Claude Code Sub-Agents](../claude-code/features/sub-agents.md) - Enterprise agent patterns
   - [MCP Integration](../claude-code/features/mcp.md) - Connect external systems
   - [Hooks & Automation](../claude-code/features/hooks-guide.md) - Workflow automation

---

## Learning Resources Summary

| Topic | Resource | Time |
|-------|----------|------|
| LangChain Chains | [LangChain Docs](../ai-frameworks/langchain/) | 3 hrs |
| LangGraph Workflows | [LangGraph Docs](../ai-frameworks/langgraph/) | 4 hrs |
| CrewAI Teams | [CrewAI Docs](../ai-frameworks/crewai/) | 3 hrs |
| Integration & Testing | Practice | 2 hrs |

**Total Estimated Time**: 25-35 hours (excluding practice)

---

## Tips for Success

1. **Start Small**: Begin with simple agents, then add complexity
2. **Understand State**: Clear state management is key to complex agents
3. **Test Thoroughly**: Agent behavior can be unpredictable—test extensively
4. **Monitor Costs**: Keep track of API costs while experimenting
5. **Use Debugging Tools**: Leverage verbose mode and logging

---

## Common Questions

**Q: When should I use LangGraph vs CrewAI?**
A: LangGraph for complex control flow and state management; CrewAI for teams of specialized agents.

**Q: Can agents make mistakes?**
A: Yes! Build in verification, user confirmation, and error handling.

**Q: How do I control agent behavior?**
A: Use detailed role descriptions, task specifications, tools, and prompt engineering.

**Q: What about hallucinations?**
A: Use tools and retrieval-augmented generation (RAG) to ground agents in facts.

---

*Last updated: November 2025*

**Ready for the next level?** Move to [Advanced Production RAG Path](./advanced-production-rag.md)
