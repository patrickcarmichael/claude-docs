---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Stopping an Endpoint

### Auto-shutdown

When you create an endpoint you can select an auto-shutdown timeframe during the configuration step. We offer various timeframes.

If you need to shut down your endpoint before the auto-shutdown period has elapsed, you can do this in a couple of ways.

### Web Interface

#### Shutdown during deployment

When your model is being deployed, you can click the red stop button to stop the deployment.

#### Shutdown when the endpoint is running

If the dedicated endpoint has started, you can shut down the endpoint by going to your models page. Click on the Model to expand the drop down, click the three dots and then **Stop endpoint**, then confirm in the pop-up prompt.

Once the endpoint has stopped, you will see it is offline on the models page. You can use the same three dots menu to start the endpoint again if you did this by mistake.

### API

You can also use the Together AI CLI to send a stop command, as covered in our documentation. To do this you will need your endpoint ID.

**Minimal availability**: We may have hardware available but only enough for a small amount of replicas. If this is the case, the endpoint may start but only scale to the amount of replicas available. If the min replica is set higher than we have capacity for, we may queue the endpoint until there is enough availability. To avoid the wait, you can reduce the min replica count.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
