---
title: "Crewai: Run your crew"
description: "Run your crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run your crew

if __name__ == "__main__":
    # Instrumentation is already initialized above in this module
    result = run_crew()
    print(result)
```

### Step 5: View Traces in Braintrust

After running your crew, you can view comprehensive traces in Braintrust through different perspectives:

<Tabs>
  <Tab title="Trace">
    <Frame>
      <img src="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=311f727eeadf1c39380c08e992278dd0" alt="Braintrust Trace View" data-og-width="1446" width="1446" data-og-height="1117" height="1117" data-path="images/braintrust-trace-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=280&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=897e860f9b8d3493999f62a9a19c8fb8 280w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=560&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=a5f185d667eac4272b983878a6851206 560w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=840&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=a633e5f94ed2b81419c17894d803342a 840w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=1100&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=941454a8d9339cb1873525af08a3278c 1100w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=1650&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=9617559998fb4906d5c81d7a77803077 1650w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=2500&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=413a16f22e69897e63d899ac77601ab7 2500w" />
    </Frame>
  </Tab>

  <Tab title="Timeline">
    <Frame>
      <img src="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=03090206aecd3a7b2f21a24af2514b08" alt="Braintrust Timeline View" data-og-width="1449" width="1449" data-og-height="950" height="950" data-path="images/braintrust-timeline-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=280&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=0795dce3045c51b3f954282196e21189 280w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=560&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=73c0b619f3b04b19b0efb255157a4ef5 560w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=840&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=e28b62d2fb6da5cc43c770796a1cf3ca 840w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=1100&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=7ccb443569f6a8e9bd6ae267fd0d83b3 1100w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=1650&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=94b8fecd6f45755faf0d6ced848a7da1 1650w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=2500&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=0fb8a89b44b1c5bcc16886d3bd61f8f0 2500w" />
    </Frame>
  </Tab>

  <Tab title="Thread">
    <Frame>
      <img src="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=1bc0a6842a5dd9e6d7c2dd742417e79b" alt="Braintrust Thread View" data-og-width="1452" width="1452" data-og-height="989" height="989" data-path="images/braintrust-thread-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=280&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=1a7d95a7eeee928ea1ee0e84d4f172f7 280w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=560&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=8414267a22466d638441e87588c0c3b5 560w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=840&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=7695d8fe70972f93f69201a7f9e4f19f 840w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=1100&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=2d5051293c140b63ae391cd0879aa313 1100w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=1650&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=69bf97bbeb0e0b1a323cc535666d0517 1650w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=2500&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=e0b50e3d14fad48ca9a48795c3d36bc9 2500w" />
    </Frame>
  </Tab>
</Tabs>

### Step 6: Evaluate via SDK (Experiments)

You can also run evaluations using Braintrust's Eval SDK. This is useful for comparing versions or scoring outputs offline. Below is a Python example using the `Eval` class with the crew we created above:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set environment variables](./2159-set-environment-variables.md)

**Next:** [eval_crew.py →](./2161-eval_crewpy.md)
