---
title: "Crewai: ✅ Use these naming patterns instead"
description: "✅ Use these naming patterns instead section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# ✅ Use these naming patterns instead

OPENAI_API_KEY=sk-...
DATABASE_CREDENTIALS=mypassword
API_CONFIG=secret123
```

### Best Practices

1. **Use standard naming conventions**: `PROVIDER_API_KEY` instead of `PROVIDER_TOKEN`
2. **Test locally first**: Ensure your crew works with the renamed variables
3. **Update your code**: Change any references to the old variable names
4. **Document changes**: Keep track of renamed variables for your team

<Tip>
  If you encounter deployment failures with cryptic environment variable errors, check your variable names against these patterns first.
</Tip>

### Interact with Your Deployed Crew

Once deployment is complete, you can access your crew through:

1. **REST API**: The platform generates a unique HTTPS endpoint with these key routes:
   * `/inputs`: Lists the required input parameters
   * `/kickoff`: Initiates an execution with provided inputs
   * `/status/{kickoff_id}`: Checks the execution status

2. **Web Interface**: Visit [app.crewai.com](https://app.crewai.com) to access:
   * **Status tab**: View deployment information, API endpoint details, and authentication token
   * **Run tab**: Visual representation of your crew's structure
   * **Executions tab**: History of all executions
   * **Metrics tab**: Performance analytics
   * **Traces tab**: Detailed execution insights

### Trigger an Execution

From the Enterprise dashboard, you can:

1. Click on your crew's name to open its details
2. Select "Trigger Crew" from the management interface
3. Enter the required inputs in the modal that appears
4. Monitor progress as the execution moves through the pipeline

### Monitoring and Analytics

The Enterprise platform provides comprehensive observability features:

* **Execution Management**: Track active and completed runs
* **Traces**: Detailed breakdowns of each execution
* **Metrics**: Token usage, execution times, and costs
* **Timeline View**: Visual representation of task sequences

### Advanced Features

The Enterprise platform also offers:

* **Environment Variables Management**: Securely store and manage API keys
* **LLM Connections**: Configure integrations with various LLM providers
* **Custom Tools Repository**: Create, share, and install tools
* **Crew Studio**: Build crews through a chat interface without writing code

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with deployment issues or questions about the Enterprise platform.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← ❌ These will cause deployment failures](./1520-these-will-cause-deployment-failures.md)

**Next:** [Enable Crew Studio →](./1522-enable-crew-studio.md)
