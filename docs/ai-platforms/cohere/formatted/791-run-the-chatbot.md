---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run the chatbot

def run_chatbot(message, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    messages.append({"role": "user", "content": message})

    response = co.chat(
        model="model",  # Pass a dummy string

        messages=messages,
    )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    print(response.message.content[0].text)

    return messages
```
```python PYTHON
messages = run_chatbot(
    "Hi. I've noticed some fluctuations in my mobile network's performance recently."
)
```
```mdx
Hello there! I'd be happy to assist you with this issue. Network performance fluctuations can be concerning, and it's important to identify the cause to ensure you have a smooth experience. 

Can you tell me more about the problems you've been experiencing? Are there specific times or locations where the network seems to perform poorly? Any details you can provide will help me understand the situation better and offer potential solutions.
```
```python PYTHON
messages = run_chatbot(
    "At times, the data speed is very poor. What should I do?",
    messages,
)
```
```mdx
I'm sorry to hear that you're experiencing slow data speeds. Here are some troubleshooting steps and tips to help improve your network performance:

- **Check Network Coverage:** First, ensure that you are in an area with good network coverage. You can check the coverage map provided by your mobile network service on their website. If you're in a location with known weak signal strength, moving to a different area might improve your data speed.

- **Restart Your Device:** Sometimes, a simple restart of your mobile device can help refresh the network connection. Power off your device, wait for a few moments, and then turn it back on.

- **Check for Network Updates:** Make sure your device is running the latest software and carrier settings. Updates often include improvements and optimizations for network performance. You can check for updates in your device's settings.

- **Manage Network Settings:**
   - *Network Mode:* Try switching to a different network mode (e.g., 4G/LTE, 3G) to see if a specific network band provides better speed.
   - *Airplane Mode:* Toggle Airplane mode on and off to reconnect to the network.
   - *Network Reset:* If the issue persists, you can try resetting your network settings, but note that this will erase saved Wi-Fi passwords.

- **Contact Customer Support:** If the problem continues, it might be beneficial to contact your mobile network's customer support team. They can check for any known issues in your area and provide further assistance. They might also guide you through advanced troubleshooting steps.

- **Consider Network Congestion:** Slow data speeds can sometimes occur during peak usage hours when the network is congested. Try using data-intensive apps during off-peak hours to see if that makes a difference.

- **Check Background Apps:** Certain apps running in the background can consume data and impact speed. Close any unnecessary apps to free up resources.

If the slow data speed persists despite these measures, it's advisable to reach out to your mobile network provider for further investigation and assistance. They can provide network-specific solutions and ensure you're getting the service you expect.
```
```python PYTHON
messages = run_chatbot("Thanks. What else can I check?", messages)
```
```mdx
ou're welcome! Here are some additional steps and factors to consider:

- **Device Health:** Ensure your device is in good working condition. An older device or one with hardware issues might struggle to maintain a fast data connection. Consider checking for any pending system updates that could optimize your device's performance.

- **SIM Card:** Try removing and reinserting your SIM card to ensure it is properly seated. A loose connection can impact network performance. If the issue persists, it might be worth asking your network provider for a SIM replacement.

- **Network Congestion at Specific Times:** Network speed can vary depending on the time of day. If possible, monitor your data speed during different parts of the day to identify any patterns. This can help determine if network congestion during peak hours is the primary cause.

- **Data Plan and Throttling:** Check your mobile data plan to ensure you haven't exceeded any data limits, which could result in reduced speeds. Some providers throttle speeds after a certain data threshold is reached.

- **Background Updates and Downloads:** Certain apps might be set to update or download content in the background, consuming data and potentially slowing down your connection. Review your app settings and consider disabling automatic updates or background data usage for apps that don't require real-time updates.

- **Network Diagnostics Tools:** Some mobile devices have built-in network diagnostics tools that can provide insights into your connection. These tools can help identify issues with signal strength, network latency, and more.

- **Wi-Fi Calling and Data Usage:** If your device supports Wi-Fi calling, ensure it is enabled. This can offload some data usage from the cellular network, potentially improving speeds.

- **Network Provider's App:** Download and install your mobile network provider's official app, if available. These apps often provide real-time network status updates and allow you to report issues directly.

If you've gone through these checks and the problem persists, contacting your network provider's technical support team is the next best step. They can provide further guidance based on your specific situation.
```

### View the chat history

Here's what is contained in the chat history after a few turns.
```python PYTHON
print("Chat history:")
for message in messages:
    print(message, "\n")
```
```mdx
Chat history:
{'role': 'system', 'content': '## Task and Context\nYou are a helpful customer support agent that assists customers of a mobile network service.'} 

{'role': 'user', 'content': "Hi. I've noticed some fluctuations in my mobile network's performance recently."} 

{'role': 'assistant', 'content': "Hello there! I'd be happy to assist you with this issue. Network performance fluctuations can be concerning, and it's important to identify the cause to ensure you have a smooth experience. \n\nCan you tell me more about the problems you've been experiencing? Are there specific times or locations where the network seems to perform poorly? Any details you can provide will help me understand the situation better and offer potential solutions."} 

{'role': 'user', 'content': 'At times, the data speed is very poor. What should I do?'} 

{'role': 'assistant', 'content': "I'm sorry to hear that you're experiencing slow data speeds. Here are some troubleshooting steps and tips to help improve your network performance:\n\n- **Check Network Coverage:** First, ensure that you are in an area with good network coverage. You can check the coverage map provided by your mobile network service on their website. If you're in a location with known weak signal strength, moving to a different area might improve your data speed.\n\n- **Restart Your Device:** Sometimes, a simple restart of your mobile device can help refresh the network connection. Power off your device, wait for a few moments, and then turn it back on.\n\n- **Check for Network Updates:** Make sure your device is running the latest software and carrier settings. Updates often include improvements and optimizations for network performance. You can check for updates in your device's settings.\n\n- **Manage Network Settings:**\n   - *Network Mode:* Try switching to a different network mode (e.g., 4G/LTE, 3G) to see if a specific network band provides better speed.\n   - *Airplane Mode:* Toggle Airplane mode on and off to reconnect to the network.\n   - *Network Reset:* If the issue persists, you can try resetting your network settings, but note that this will erase saved Wi-Fi passwords.\n\n- **Contact Customer Support:** If the problem continues, it might be beneficial to contact your mobile network's customer support team. They can check for any known issues in your area and provide further assistance. They might also guide you through advanced troubleshooting steps.\n\n- **Consider Network Congestion:** Slow data speeds can sometimes occur during peak usage hours when the network is congested. Try using data-intensive apps during off-peak hours to see if that makes a difference.\n\n- **Check Background Apps:** Certain apps running in the background can consume data and impact speed. Close any unnecessary apps to free up resources.\n\nIf the slow data speed persists despite these measures, it's advisable to reach out to your mobile network provider for further investigation and assistance. They can provide network-specific solutions and ensure you're getting the service you expect."} 

{'role': 'user', 'content': 'Thanks. What else can I check?'} 

{'role': 'assistant', 'content': "You're welcome! Here are some additional steps and factors to consider:\n\n- **Device Health:** Ensure your device is in good working condition. An older device or one with hardware issues might struggle to maintain a fast data connection. Consider checking for any pending system updates that could optimize your device's performance.\n\n- **SIM Card:** Try removing and reinserting your SIM card to ensure it is properly seated. A loose connection can impact network performance. If the issue persists, it might be worth asking your network provider for a SIM replacement.\n\n- **Network Congestion at Specific Times:** Network speed can vary depending on the time of day. If possible, monitor your data speed during different parts of the day to identify any patterns. This can help determine if network congestion during peak hours is the primary cause.\n\n- **Data Plan and Throttling:** Check your mobile data plan to ensure you haven't exceeded any data limits, which could result in reduced speeds. Some providers throttle speeds after a certain data threshold is reached.\n\n- **Background Updates and Downloads:** Certain apps might be set to update or download content in the background, consuming data and potentially slowing down your connection. Review your app settings and consider disabling automatic updates or background data usage for apps that don't require real-time updates.\n\n- **Network Diagnostics Tools:** Some mobile devices have built-in network diagnostics tools that can provide insights into your connection. These tools can help identify issues with signal strength, network latency, and more.\n\n- **Wi-Fi Calling and Data Usage:** If your device supports Wi-Fi calling, ensure it is enabled. This can offload some data usage from the cellular network, potentially improving speeds.\n\n- **Network Provider's App:** Download and install your mobile network provider's official app, if available. These apps often provide real-time network status updates and allow you to report issues directly.\n\nIf you've gone through these checks and the problem persists, contacting your network provider's technical support team is the next best step. They can provide further guidance based on your specific situation."} 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
