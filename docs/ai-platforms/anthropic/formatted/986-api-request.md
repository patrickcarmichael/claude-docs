---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API request

<Tabs>
  <Tab title="Python">
```python
    import anthropic

    client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")

    api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4000,
      temperature=0,
      system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="TypeScript">
```TypeScript
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 4000,
      temperature: 0,
      system: "Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections:  \n  \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar.  \n  \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog.  \n  \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions.  \n  \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz.  \n  \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names.  \n  \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information.  \n  \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section.  \n  \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>

  <Tab title="AWS Bedrock Python">
```python
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock

    # for authentication options

    client = AnthropicBedrock()

    message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=4000,
      temperature=0,
      system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
```typescript

    import AnthropicBedrock from '@anthropic-ai/bedrock-sdk';

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 4000,
      temperature: 0,
      system: "Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    });
    console.log(msg);
```
  </Tab>

  <Tab title="Vertex AI Python">
```python
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=4000,
      temperature=0,
      system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
            }
          ]
        }
      ]
    )
    print(message.content)
```
  </Tab>

  <Tab title="Vertex AI TypeScript">
```typescript
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 4000,
    temperature: 0,
    system: "Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and content, clickable buttons, and more. Ensure that the design is visually appealing, responsive, and user-friendly. The HTML, CSS, and JavaScript code should be well-structured, efficiently organized, and properly commented for readability and maintainability.",
    messages: [
    {
    "role": "user",
    "content": [
    {
    "type": "text",
    "text": "Create a one-page website for an online learning platform called \"EduQuest\" with the following features and sections: \n \n1. A fixed navigation bar with links to course categories (Math, Science, Languages, Arts) and a search bar. \n \n2. A hero section with a video background showcasing students learning online, a dynamic tagline that rotates between \"Learn at your own pace,\" \"Discover new passions,\" and \"Expand your horizons\" every 3 seconds, and a \"Get Started\" button leading to a course catalog. \n \n3. A featured courses section displaying course cards with placeholders for course images, titles, instructors, and descriptions. \n \n4. An interactive \"Learning Paths\" section with a short quiz to determine learning styles and interests, and a button to start the quiz. \n \n5. A \"Success Stories\" section featuring testimonials from satisfied students, with placeholders for the testimonial text and student names. \n \n6. A footer with links to the platform's blog, FAQ, privacy policy, and a \"Contact Us\" button that opens a modal window with a contact form and customer support information. \n \nInclude filler placeholder content for the video background, course cards, and testimonials. Embed the CSS styles within the `<style>` tag in the `<head>` section and place the JavaScript code within the `<script>` tag at the end of the `<body>` section. \n \nThe JavaScript code should handle the dynamic tagline in the hero section, rotating through the different taglines every 3 seconds."
    }
    ]
    }
    ]
    });
    console.log(msg);
```
  </Tab>
</Tabs>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
