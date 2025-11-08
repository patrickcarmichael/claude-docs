---
title: "Crewai: Setting Up Webhooks"
description: "Setting Up Webhooks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setting Up Webhooks


<Steps>
  <Step title="Accessing the Kickoff Interface">
    * Navigate to the CrewAI AMP dashboard
    * Look for the `/kickoff` section, which is used to start the crew execution
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4e6a4b1f098388c7f76e91c25ed4b077" alt="Kickoff Interface" data-og-width="670" width="670" data-og-height="358" height="358" data-path="images/enterprise/kickoff-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=31eccbe3c20da734c90a1b2dd681261d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b8f8311eeece00d69760069cf8f218cf 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cd690e83cafc2b4675f5343d779fd413 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=640bf42c471ed898f434ff1b837aaf3f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2ea591f56996cddcd1ab99a6ca951050 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-interface.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c76d12bbd6580f8211a0c75c58105f41 2500w" />
      </Frame>
  </Step>

  <Step title="Configuring the JSON Content">
    In the JSON Content section, you'll need to provide the following information:

    * **inputs**: A JSON object containing:
      * `company`: The name of the company (e.g., "tesla")
      * `product_name`: The name of the product (e.g., "crewai")
      * `form_response`: The type of response (e.g., "financial")
      * `icp_description`: A brief description of the Ideal Customer Profile
      * `product_description`: A short description of the product
      * `taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`: URLs for various webhook endpoints (ActivePieces, Zapier, Make.com or another compatible platform)
  </Step>

  <Step title="Integrating with ActivePieces">
    In this example we will be using ActivePieces. You can use other platforms such as Zapier and Make.com

    To integrate with ActivePieces:

    1. Set up a new flow in ActivePieces

    2. Add a trigger (e.g., `Every Day` schedule)
       <Frame>
         <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1a52fc1bb47bef6228955360d00f190f" alt="ActivePieces Trigger" data-og-width="595" width="595" data-og-height="773" height="773" data-path="images/enterprise/activepieces-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a08bb69bed1a61d5e8febbfe10ca5e7f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=b1b5e3f75dc328b09023661ce318b68b 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a64f6e3cfd68c9c66e4248cf92e2f7f1 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=aedf530314a9542c8f217ba77feec4e8 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=95f0dc03528daddca61ad04822e7ba7c 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-trigger.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=48e52a1d3960d50b027f8c92f4a62e11 2500w" />
       </Frame>

    3. Add an HTTP action step
       * Set the action to `Send HTTP request`

       * Use `POST` as the method

       * Set the URL to your CrewAI AMP kickoff endpoint

       * Add necessary headers (e.g., `Bearer Token`)
         <Frame>
           <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=602a5ed1aa2b462b0a81a122a5e2d35f" alt="ActivePieces Headers" data-og-width="449" width="449" data-og-height="572" height="572" data-path="images/enterprise/activepieces-headers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=fb1852f1834f3ca324d88201890454c2 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3ac86c364aa02800cb7563d6f7a0cc4b 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1433e902dc31e3c5bba03cea45fca103 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9ca4bc723b91d7681c7798019f933e00 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d6efc61f86f20c2d850bbc6e43057084 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-headers.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=508d671fe743548d52b5fa6f70d8c6f1 2500w" />
         </Frame>

       * In the body, include the JSON content as configured in step 2
         <Frame>
           <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f238e1630f7be667cce2d208315ddc75" alt="ActivePieces Body" data-og-width="670" width="670" data-og-height="401" height="401" data-path="images/enterprise/activepieces-body.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=184acb105d21412a7a2cb184d57b067e 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2820fd618992f3299a713701cf6d3a3e 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=988d687157f7dea236e152edb382ac4f 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9c7603e394ffb44676be999c9bfd8843 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=84b3aa1d756e36d3578c11a81a1bba03 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-body.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f8ca588c964165c10b66d26478b1201a 2500w" />
         </Frame>

       * The crew will then kickoff at the pre-defined time.
  </Step>

  <Step title="Setting Up the Webhook">
    1. Create a new flow in ActivePieces and name it
       <Frame>
         <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c23af88ea2df7919f680706318eb1506" alt="ActivePieces Flow" data-og-width="544" width="544" data-og-height="683" height="683" data-path="images/enterprise/activepieces-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3efbff7b8131db3e87a41b0885447729 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1993b2b3ba57a859e42efcf21737c351 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3f46a4b1b2a17fcb0c0f3a9373699b5a 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3eff0450a0f63e2ed5b00797ee1295ea 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f3ca2cd9eb16b9f4642a27df234b191c 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-flow.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ffa10bab192e9b54be9ad3df31ce9036 2500w" />
       </Frame>

    2. Add a webhook step as the trigger:
       * Select `Catch Webhook` as the trigger type

       * This will generate a unique URL that will receive HTTP requests and trigger your flow
         <Frame>
           <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=8236fd9a97149eff4fd86f1c9a9b0f1a" alt="ActivePieces Webhook" data-og-width="451" width="451" data-og-height="488" height="488" data-path="images/enterprise/activepieces-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=67e441a99da496ffc5c7267f7a9edf38 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=bd59361f9c3c3cc590116b69ae938e62 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6baa9171275b63542d4518d517def191 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d2ca4c48d4c27d35f86634a8cff980aa 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=791a725473ebaa655f55060dc60ba4a2 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-webhook.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c84dd08fd3ec706b43868a9a7b5629a8 2500w" />
         </Frame>

       * Configure the email to use crew webhook body text
         <Frame>
           <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=484c8d88ed96322d21894e9663f5fc4a" alt="ActivePieces Email" data-og-width="461" width="461" data-og-height="518" height="518" data-path="images/enterprise/activepieces-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=619ef405e48854a83bfdfcc2d6ef44ec 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=43448b60f1c1686da67239865b31586c 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79a570bad87d3beeebe8f87437823cac 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=180ce65773e5fd6007f08fa159f21dfb 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=80df8a27d8ba193f531db980a9697f6a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/activepieces-email.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a8e77053f8fed779ccff7474435f3cc8 2500w" />
         </Frame>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Webhook Automation](./2433-webhook-automation.md)

**Next:** [Webhook Output Examples →](./2435-webhook-output-examples.md)
