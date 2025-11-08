---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


The primary task goal was:

"Retrieve the average, maximum, and minimum monthly revenue for each city, but only include cities that have more than one user. Also, count the number of user in each city and
sort the results by the average monthly revenue in descending order"

So the Agent tried to get information from the DB, the first one is wrong so the Agent tries again and gets the correct information and passes to the next agent.

![alt text](https://github.com/crewAIInc/crewAI-tools/blob/main/crewai_tools/tools/nl2sql/images/image-2.png?raw=true)
![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-3.png)

The second task goal was:

"Review the data and create a detailed report, and then create the table on the database with the fields based on the data provided.
Include information on the average, maximum, and minimum monthly revenue for each city, but only include cities that have more than one user. Also, count the number of users in each city and sort the results by the average monthly revenue in descending order."

Now things start to get interesting, the Agent generates the SQL query to not only create the table but also insert the data into the table. And in the end the Agent still returns the final report which is exactly what was in the database.

![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-4.png)
![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-5.png)

![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-9.png)
![alt text](https://github.com/crewAIInc/crewAI-tools/raw/main/crewai_tools/tools/nl2sql/images/image-7.png)

This is a simple example of how the NL2SQLTool can be used to interact with the database and generate reports based on the data in the database.

The Tool provides endless possibilities on the logic of the Agent and how it can interact with the database.

```md  theme={null}
 DB -> Agent -> ... -> Agent -> DB
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← psycopg2 was installed to run this example with PostgreSQL](./806-psycopg2-was-installed-to-run-this-example-with-po.md)

**Next:** [Overview →](./808-overview.md)
