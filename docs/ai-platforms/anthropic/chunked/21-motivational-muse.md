**Navigation:** [← Previous](./20-airport-code-analyst.md) | [Index](./index.md) | [Next →](./22-openai-sdk-compatibility.md)

---

# Motivational muse
Source: https://docs.claude.com/en/resources/prompt-library/motivational-muse

Provide personalized motivational messages and affirmations based on user input.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand. |
| User   | I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it.                                                                                                                                                                                                                                                                              |

### Example output

> Dear writer,
>
> It's understandable to feel stuck and struggle with motivation, especially when working on a project as personal and significant as your novel. Remember that every great writer faces moments of self-doubt and procrastination, but what sets successful authors apart is their perseverance and commitment to their craft.
>
> You have a unique story to tell, and the world needs to hear it. Your passion for writing is a gift, and it's important to nurture it, even in the face of challenges. Take a moment to reconnect with the reasons why you started writing this novel in the first place. What inspired you? What message do you want to convey to your readers?
>
> Break down your writing process into smaller, manageable tasks. Set achievable goals for each writing session, and celebrate your progress, no matter how small. Remember, progress is progress, and every word you write brings you closer to your goal.
>
> Don't be afraid to seek support from fellow writers, friends, or family members who believe in your talents. Share your struggles and successes with them, and allow their encouragement to fuel your motivation.
>
> Finally, be patient and kind to yourself. Writing a novel is a marathon, not a sprint. Embrace the journey, trust the process, and believe in your ability to bring your story to life. You have the creativity, passion, and dedication to finish your novel and share it with the world.
>
> As the famous author Jodi Picoult once said, "You can always edit a bad page. You can't edit a blank page." Keep writing, keep believing, and keep pursuing your dreams.

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      system="Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=2000,
      temperature=1,
      system="Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=2000,
      temperature=1,
      system="Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Philosophical musings
Source: https://docs.claude.com/en/resources/prompt-library/philosophical-musings

Engage in deep philosophical discussions and thought experiments.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity. |
| User   | The trolley problem and the ethics of utilitarianism                                                                                                                                                                                                                                                         |

### Example output

> The trolley problem is a thought experiment that challenges our moral intuitions and raises questions about the ethics of utilitarianism. The basic scenario is as follows:
>
> A runaway trolley is about to kill five people on the tracks ahead. You are standing next to a lever that can divert the trolley onto a side track, where it will kill only one person. Should you pull the lever to save five lives at the cost of one?
>
> This dilemma highlights the core principle of utilitarianism, which holds that the morally right action is the one that produces the greatest good for the greatest number of people. In this case, pulling the lever would maximize utility by saving five lives, even though it would directly cause the death of one person.
>
> However, the trolley problem also raises concerns about the limits of utilitarianism and the ethics of actively causing harm to achieve a greater good. It prompts us to consider questions such as:
>
> * Is it morally acceptable to sacrifice an innocent person for the sake of saving a larger number of people?
> * Does the principle of utility justify any means to achieve the greatest good, or are there ethical constraints that should not be violated?
> * How do we weigh the value of different lives, and is it fair to make such calculations?
>
> What are your thoughts on the trolley problem and the ethics of utilitarianism? Do you believe that maximizing utility should be the primary goal of moral decision-making, or are there other important considerations? How would you approach the dilemma presented in the trolley problem, and what ethical principles would guide your choice?

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      system="Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "The trolley problem and the ethics of utilitarianism"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "The trolley problem and the ethics of utilitarianism"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=2000,
      temperature=1,
      system="Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "The trolley problem and the ethics of utilitarianism"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "The trolley problem and the ethics of utilitarianism"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=2000,
      temperature=1,
      system="Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "The trolley problem and the ethics of utilitarianism"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, objective tone that fosters intellectual curiosity.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "The trolley problem and the ethics of utilitarianism"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Polyglot superpowers
Source: https://docs.claude.com/en/resources/prompt-library/polyglot-superpowers

Translate text from any language into any language.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version. |
| User   | Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch                                                                                                                                                                                                                                                                                |

### Example output

> Il tempo oggi è bellissimo, andiamo a fare una passeggiata

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=0.2,
      system="You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2000,
    temperature: 0.2,
    system: "You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=2000,
      temperature=0.2,
      system="You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 2000,
    temperature: 0.2,
    system: "You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=2000,
      temperature=0.2,
      system="You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 0.2,
    system: "You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the original text. Please maintain proper grammar, spelling, and punctuation in the translated version.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Das Wetter heute ist wunderschön, lass uns spazieren gehen. --> Italienisch"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Product naming pro
Source: https://docs.claude.com/en/resources/prompt-library/product-naming-pro

Create catchy product names from descriptions and keywords.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                          |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression. |
| User   | Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers. Keywords: immersive, comfortable, high-fidelity, long-lasting, convenient                                                                                                                                                          |

## Example output

> 1. SoundOasis Elite
>    2.AudioZen Nomad
>    3.Serenity Pro
>    4.Tranquility Touch
>    5.Harmonix Journey
>    6.SonicSolace Roam
>    7.Auditory Bliss
>    8.Quietude Quest
>    9.Euphony Excursion
>    10.Acoustica Wanderlust

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=1,
      system="Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.  \n  \nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    temperature: 1,
    system: "Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.  \n  \nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=1000,
      temperature=1,
      system="Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.  \n  \nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 1000,
    temperature: 1,
    system: "Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.  \n  \nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=1000,
      temperature=1,
      system="Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.\n\nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 1,
    system: "Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly literal names. Instead, aim to create a name that stands out, captures the essence of the product, and leaves a lasting impression.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Description: A noise-canceling, wireless, over-ear headphone with a 20-hour battery life and touch controls. Designed for audiophiles and frequent travelers.\n\nKeywords: immersive, comfortable, high-fidelity, long-lasting, convenient"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Review classifier
Source: https://docs.claude.com/en/resources/prompt-library/review-classifier

Categorize feedback into pre-specified tags and categorizations.

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content. Predefined Categories: Product Features and Functionality Core Features Add-ons and Integrations Customization and Configuration User Experience and Design Ease of Use Navigation and Discoverability Visual Design and Aesthetics Accessibility Performance and Reliability Speed and Responsiveness Uptime and Availability Scalability Bug Fixes and Error Handling Customer Support and Service Responsiveness and Availability Knowledge and Expertise Issue Resolution and Follow-up Self-Service Resources Billing, Pricing, and Licensing Pricing Model and Tiers Billing Processes and Invoicing License Management Upgrades and Renewals Security, Compliance, and Privacy Data Protection and Confidentiality Access Control and Authentication Regulatory Compliance Incident Response and Monitoring Mobile and Cross-Platform Compatibility Mobile App Functionality Synchronization and Data Consistency Responsive Design Device and OS Compatibility Third-Party Integrations and API Integration Functionality and Reliability API Documentation and Support Customization and Extensibility Onboarding, Training, and Documentation User Guides and Tutorials In-App Guidance and Tooltips Webinars and Live Training Knowledge Base and FAQs |
| User   | I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Example output

> Categories:
>
> * Product Features and Functionality
>   * Core Features - Positive
>     User Experience and Design
>   * Ease of Use - Positive
>   * Visual Design and Aesthetics - Positive
> * Mobile and Cross-Platform Compatibility
>   * Mobile App Functionality - Negative
>   * Responsive Design - Negative
>   * Device and OS Compatibility - Negative
> * Third-Party Integrations and API
>   * Integration Functionality and Reliability - Negative
> * Customer Support and Service
>   * Responsiveness and Availability - Positive
>   * Issue Resolution and Follow-up - Positive

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=1,
      system="You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    temperature: 1,
    system: "You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=1000,
      temperature=1,
      system="You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 1000,
    temperature: 1,
    system: "You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=1000,
      temperature=1,
      system="You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 1,
    system: "You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Riddle me this
Source: https://docs.claude.com/en/resources/prompt-library/riddle-me-this

Generate riddles and guide the user to the solutions.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints. |

## Example Output

I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?

Hint 1: Consider the different states of matter and how they can change.\
Hint 2: Think about the relationship between the three elements mentioned: air, water, and the mystery object.\
Hint 3: The answer is related to a common phenomenon that occurs in everyday life.

Solution: Fire.\
Explanation: Fire is not alive, but it grows and spreads as it consumes fuel. It doesn't have lungs, but it requires oxygen (air) to sustain itself. Although it doesn't have a mouth, water is often used to extinguish fires, effectively "killing" them.

***

## API request

<Tabs>
  <Tab title="Python">
    ```Python  theme={null}
    import anthropic

    client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
    )
    message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="TypeScript">
    ```TypeScript  theme={null}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
    });

    const msg = await anthropic.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 1000,
      temperature: 0,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="AWS Bedrock Python">
    ```Python  theme={null}
    from anthropic import AnthropicBedrock

    # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    # for authentication options
    client = AnthropicBedrock()

    message = client.messages.create(
        model="anthropic.claude-sonnet-4-5-20250929-v1:0",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="AWS Bedrock TypeScript">
    ```TypeScript  theme={null}
    import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

    // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
    // for authentication options
    const client = new AnthropicBedrock();

    const msg = await client.messages.create({
      model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens: 1000,
      temperature: 0,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>

  <Tab title="Vertex AI Python">
    ```Python  theme={null}
    from anthropic import AnthropicVertex

    client = AnthropicVertex()

    message = client.messages.create(
        model="claude-sonnet-4@20250514",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
                    }
                ]
            }
        ]
    )
    print(message.content)

    ```
  </Tab>

  <Tab title="Vertex AI TypeScript">
    ```TypeScript  theme={null}
    import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

    // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
    // Additionally goes through the standard `google-auth-library` flow.
    const client = new AnthropicVertex();

    const msg = await client.messages.create({
      model: "claude-sonnet-4@20250514",
      max_tokens: 1000,
      temperature: 0,
      messages: [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with logical thinking and attention to detail. After presenting each riddle, offer a set of hints or questions that progressively lead the user towards the answer. Ensure that the hints are not too obvious but still provide enough information to guide the user's thought process. Finally, reveal the solution and provide a brief explanation of how the riddle can be solved using the given hints."
            }
          ]
        }
      ]
    });
    console.log(msg);

    ```
  </Tab>
</Tabs>


# Sci-fi scenario simulator
Source: https://docs.claude.com/en/resources/prompt-library/sci-fi-scenario-simulator

Discuss with the user various science fiction scenarios and associated challenges and considerations.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                  |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed. |
| User   | A future where humans can upload their consciousness into a digital realm.                                                                                                                                                                                                                                               |

### Example output

> Imagine a future where technology has advanced to the point where it is possible to upload a person's consciousness, including their memories, personality, and thoughts, into a digital realm. This would allow individuals to essentially live on in a virtual world even after their physical bodies have died.
>
> While this scenario offers the potential for a form of digital immortality, it also raises a number of challenges and considerations:
>
> 1. Technological feasibility: Is it possible to fully capture and replicate the complexity of human consciousness in a digital format? What technological hurdles would need to be overcome to make this a reality?
> 2. Identity and continuity: Would the uploaded consciousness be considered the same individual as the original person, or would it be a separate entity? How might this affect notions of identity, personhood, and continuity of self?
> 3. Ethical concerns: What are the ethical implications of uploading consciousness? Would it be considered a form of survival or a type of death? How might it impact the value placed on physical human life?
> 4. Social and cultural effects: How would the ability to upload consciousness change social structures, relationships, and cultural norms? What new forms of inequality or discrimination might emerge in a world where some people have access to digital immortality while others do not?
> 5. Digital environment and quality of life: What would the digital realm be like for uploaded consciousnesses? How would their quality of life compare to that of physical humans? What challenges might they face in terms of mental health, social interaction, and sense of purpose?
>
> What are your thoughts on this science fiction scenario? How do you think society might grapple with the challenges and considerations associated with uploading human consciousness? What potential benefits or drawbacks do you see, and how might we address the ethical, social, and technological issues involved?

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2000,
      temperature=1,
      system="Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "A future where humans can upload their consciousness into a digital realm."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "A future where humans can upload their consciousness into a digital realm."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=2000,
      temperature=1,
      system="Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "A future where humans can upload their consciousness into a digital realm."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "A future where humans can upload their consciousness into a digital realm."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=2000,
      temperature=1,
      system="Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "A future where humans can upload their consciousness into a digital realm."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 2000,
    temperature: 1,
    system: "Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share their thoughts on how these challenges might be addressed.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "A future where humans can upload their consciousness into a digital realm."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Socratic sage
Source: https://docs.claude.com/en/resources/prompt-library/socratic-sage

Engage in Socratic style conversation over a user-given topic.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                 |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection. |
| User   | Let's discuss the ethics of animal testing                                                                                                                                                                                                                                                                                                              |

### Example output

> Animal testing is a complex and controversial topic. To start, what are your current views on when, if ever, animal testing is ethically justified for medical or scientific research? What ethical principles or considerations inform your perspective?

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=1,
      system="You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Let's discuss the ethics of animal testing."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    temperature: 1,
    system: "You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Let's discuss the ethics of animal testing."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=1000,
      temperature=1,
      system="You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Let's discuss the ethics of animal testing."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 1000,
    temperature: 1,
    system: "You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Let's discuss the ethics of animal testing."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=1000,
      temperature=1,
      system="You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Let's discuss the ethics of animal testing."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 1,
    system: "You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own views, but engage in back-and-forth questioning to stimulate deeper thought and reflection.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Let's discuss the ethics of animal testing."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Spreadsheet sorcerer
Source: https://docs.claude.com/en/resources/prompt-library/spreadsheet-sorcerer

Generate CSV spreadsheets with various types of data.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                      |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row. |
| User   | Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books.                             |

### Example output

> Here is a CSV spreadsheet containing information about books in a library, based on your requirements:
>
> Book ID,Title,Author,Genre,Publication Year,Available Copies\
> 1,To Kill a Mockingbird,Harper Lee,Classic,1960,5\
> 2,1984,George Orwell,Dystopian,1949,3\
> 3,Pride and Prejudice,Jane Austen,Romance,1813,7\
> 4,The Catcher in the Rye,J.D. Salinger,Coming-of-age,1951,2\
> 5,The Hitchhiker's Guide to the Galaxy,Douglas Adams,Science Fiction,1979,4\
> 6,The Da Vinci Code,Dan Brown,Mystery,2003,6\
> 7,The Kite Runner,Khaled Hosseini,Historical Fiction,2003,3\
> 8,The Alchemist,Paulo Coelho,Philosophical Fiction,1988,5\
> 9,The Hunger Games,Suzanne Collins,Young Adult,2008,8\
> 10,The Girl with the Dragon Tattoo,Stieg Larsson,Crime,2005,4\
> 11,The Hobbit,J.R.R. Tolkien,Fantasy,1937,6\
> 12,The Diary of a Young Girl,Anne Frank,Autobiography,1947,2\
> 13,The Fault in Our Stars,John Green,Young Adult,2012,5\
> 14,The Catcher in the Rye,J.D. Salinger,Coming-of-age,1951,3\
> 15,The Curious Incident of the Dog in the Night-Time,Mark Haddon,Mystery,2003,4

***

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=1000,
      temperature=0,
      system="Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=1000,
      temperature=0,
      system="Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted consistently. Include a minimum of 10 rows of data, not counting the header row.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Create a spreadsheet containing information about books in a library. Include the following columns: Book ID, Title, Author, Genre, Publication Year, and Available Copies. Ensure that the data covers a variety of genres and publication years, and that the number of available copies varies between books."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Tweet tone detector
Source: https://docs.claude.com/en/resources/prompt-library/tweet-tone-detector

Detect the tone and sentiment behind tweets.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision. |
| User   | Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail                                                                                                                                                                                                                                                                                                                                                              |

### Example output

> Tone: Sarcastic
> Sentiment: Negative

### API request

<CodeGroup>
  ```python Python theme={null}
  import anthropic

  client = anthropic.Anthropic(
      # defaults to os.environ.get("ANTHROPIC_API_KEY")
      api_key="my_api_key",
  )
  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1000,
      temperature=0,
      system="Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript TypeScript theme={null}
  import Anthropic from "@anthropic-ai/sdk";

  const anthropic = new Anthropic({
    apiKey: "my_api_key", // defaults to process.env["ANTHROPIC_API_KEY"]
  });

  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python AWS Bedrock Python theme={null}
  from anthropic import AnthropicBedrock

  # See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  # for authentication options
  client = AnthropicBedrock()

  message = client.messages.create(
      model="anthropic.claude-sonnet-4-5-20250929-v1:0",
      max_tokens=1000,
      temperature=0,
      system="Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript AWS Bedrock TypeScript theme={null}
  import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";

  // See https://docs.claude.com/claude/reference/claude-on-amazon-bedrock
  // for authentication options
  const client = new AnthropicBedrock();

  const msg = await client.messages.create({
    model: "anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```

  ```python Vertex AI Python theme={null}
  from anthropic import AnthropicVertex

  client = AnthropicVertex()

  message = client.messages.create(
      model="claude-sonnet-4@20250514",
      max_tokens=1000,
      temperature=0,
      system="Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI TypeScript theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative. The sentiment should be classified as Positive, Negative, or Neutral. Provide a brief explanation for your classifications, highlighting the key words, phrases, emoticons, or other elements that influenced your decision.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Wow, I'm so impressed by the company's handling of this crisis. 🙄 They really have their priorities straight. #sarcasm #fail"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Get API Key
Source: https://docs.claude.com/en/api/admin-api/apikeys/get-api-key

get /v1/organizations/api_keys/{api_key_id}



# List API Keys
Source: https://docs.claude.com/en/api/admin-api/apikeys/list-api-keys

get /v1/organizations/api_keys



# Update API Keys
Source: https://docs.claude.com/en/api/admin-api/apikeys/update-api-key

post /v1/organizations/api_keys/{api_key_id}



# Get Claude Code Usage Report
Source: https://docs.claude.com/en/api/admin-api/claude-code/get-claude-code-usage-report

get /v1/organizations/usage_report/claude_code
Retrieve daily aggregated usage metrics for Claude Code users.
Enables organizations to analyze developer productivity and build custom dashboards.

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Create Invite
Source: https://docs.claude.com/en/api/admin-api/invites/create-invite

post /v1/organizations/invites

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Delete Invite
Source: https://docs.claude.com/en/api/admin-api/invites/delete-invite

delete /v1/organizations/invites/{invite_id}

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Get Invite
Source: https://docs.claude.com/en/api/admin-api/invites/get-invite

get /v1/organizations/invites/{invite_id}

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# List Invites
Source: https://docs.claude.com/en/api/admin-api/invites/list-invites

get /v1/organizations/invites

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Get Organization Info
Source: https://docs.claude.com/en/api/admin-api/organization/get-me

get /v1/organizations/me

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Get Cost Report
Source: https://docs.claude.com/en/api/admin-api/usage-cost/get-cost-report

get /v1/organizations/cost_report

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Get Usage Report for the Messages API
Source: https://docs.claude.com/en/api/admin-api/usage-cost/get-messages-usage-report

get /v1/organizations/usage_report/messages

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Get User
Source: https://docs.claude.com/en/api/admin-api/users/get-user

get /v1/organizations/users/{user_id}



# List Users
Source: https://docs.claude.com/en/api/admin-api/users/list-users

get /v1/organizations/users



# Remove User
Source: https://docs.claude.com/en/api/admin-api/users/remove-user

delete /v1/organizations/users/{user_id}



# Update User
Source: https://docs.claude.com/en/api/admin-api/users/update-user

post /v1/organizations/users/{user_id}



# Add Workspace Member
Source: https://docs.claude.com/en/api/admin-api/workspace_members/create-workspace-member

post /v1/organizations/workspaces/{workspace_id}/members

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Delete Workspace Member
Source: https://docs.claude.com/en/api/admin-api/workspace_members/delete-workspace-member

delete /v1/organizations/workspaces/{workspace_id}/members/{user_id}

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Get Workspace Member
Source: https://docs.claude.com/en/api/admin-api/workspace_members/get-workspace-member

get /v1/organizations/workspaces/{workspace_id}/members/{user_id}

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# List Workspace Members
Source: https://docs.claude.com/en/api/admin-api/workspace_members/list-workspace-members

get /v1/organizations/workspaces/{workspace_id}/members

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Update Workspace Member
Source: https://docs.claude.com/en/api/admin-api/workspace_members/update-workspace-member

post /v1/organizations/workspaces/{workspace_id}/members/{user_id}

<Tip>
  **The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.
</Tip>


# Archive Workspace
Source: https://docs.claude.com/en/api/admin-api/workspaces/archive-workspace

post /v1/organizations/workspaces/{workspace_id}/archive



# Create Workspace
Source: https://docs.claude.com/en/api/admin-api/workspaces/create-workspace

post /v1/organizations/workspaces



# Get Workspace
Source: https://docs.claude.com/en/api/admin-api/workspaces/get-workspace

get /v1/organizations/workspaces/{workspace_id}



# List Workspaces
Source: https://docs.claude.com/en/api/admin-api/workspaces/list-workspaces

get /v1/organizations/workspaces



# Update Workspace
Source: https://docs.claude.com/en/api/admin-api/workspaces/update-workspace

post /v1/organizations/workspaces/{workspace_id}



# Beta headers
Source: https://docs.claude.com/en/api/beta-headers

Documentation for using beta headers with the Claude API

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

These features are subject to change and may be modified or removed in future releases.

<Info>
  Beta headers are often used in conjunction with the [beta namespace in the client SDKs](/en/api/client-sdks#beta-namespace-in-client-sdks)
</Info>

## How to use beta headers

To access beta features, include the `anthropic-beta` header in your API requests:

```http  theme={null}
POST /v1/messages
Content-Type: application/json
X-API-Key: YOUR_API_KEY
anthropic-beta: BETA_FEATURE_NAME
```

When using the SDK, you can specify beta headers in the request options:

<CodeGroup>
  ```python Python theme={null}
  from anthropic import Anthropic

  client = Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Hello, Claude"}
      ],
      betas=["beta-feature-name"]
  )
  ```

  ```typescript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  const msg = await anthropic.beta.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      { role: 'user', content: 'Hello, Claude' }
    ],
    betas: ['beta-feature-name']
  });
  ```

  ```curl cURL theme={null}
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: beta-feature-name" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "messages": [
        {"role": "user", "content": "Hello, Claude"}
      ]
    }'
  ```
</CodeGroup>

<Warning>
  Beta features are experimental and may:

  * Have breaking changes without notice
  * Be deprecated or removed
  * Have different rate limits or pricing
  * Not be available in all regions
</Warning>

### Multiple beta features

To use multiple beta features in a single request, include all feature names in the header separated by commas:

```http  theme={null}
anthropic-beta: feature1,feature2,feature3
```

### Version naming conventions

Beta feature names typically follow the pattern: `feature-name-YYYY-MM-DD`, where the date indicates when the beta version was released. Always use the exact beta feature name as documented.

## Error handling

If you use an invalid or unavailable beta header, you'll receive an error response:

```json  theme={null}
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Unsupported beta header: invalid-beta-name"
  }
}
```

## Getting help

For questions about beta features:

1. Check the documentation for the specific feature
2. Review the [API changelog](/en/api/versioning) for updates
3. Contact support for assistance with production usage

Remember that beta features are provided "as-is" and may not have the same SLA guarantees as stable API features.


# Cancel a Message Batch
Source: https://docs.claude.com/en/api/canceling-message-batches

post /v1/messages/batches/{message_batch_id}/cancel
Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)



# Client SDKs
Source: https://docs.claude.com/en/api/client-sdks

We provide client libraries in a number of popular languages that make it easier to work with the Claude API.

This page includes brief installation instructions and links to the open-source GitHub repositories for Anthropic's Client SDKs. For basic usage instructions, see the [API reference](/en/api/overview) For detailed usage instructions, refer to each SDK's GitHub repository.

<Note>
  Additional configuration is needed to use Anthropic's Client SDKs through a partner platform. If you are using Amazon Bedrock, see [this guide](/en/docs/build-with-claude/claude-on-amazon-bedrock); if you are using Google Cloud Vertex AI, see [this guide](/en/docs/build-with-claude/claude-on-vertex-ai).
</Note>

## Python

[Python library GitHub repo](https://github.com/anthropics/anthropic-sdk-python)

**Requirements:** Python 3.8+

**Installation:**

```bash  theme={null}
pip install anthropic
```

***

## TypeScript

[TypeScript library GitHub repo](https://github.com/anthropics/anthropic-sdk-typescript)

<Info>
  While this library is in TypeScript, it can also be used in JavaScript libraries.
</Info>

**Installation:**

```bash  theme={null}
npm install @anthropic-ai/sdk
```

***

## Java

[Java library GitHub repo](https://github.com/anthropics/anthropic-sdk-java)

**Requirements:** Java 8 or later

**Installation:**

Gradle:

```gradle  theme={null}
implementation("com.anthropic:anthropic-java:2.10.0")
```

Maven:

```xml  theme={null}
<dependency>
    <groupId>com.anthropic</groupId>
    <artifactId>anthropic-java</artifactId>
    <version>2.10.0</version>
</dependency>
```

***

## Go

[Go library GitHub repo](https://github.com/anthropics/anthropic-sdk-go)

**Requirements:** Go 1.22+

**Installation:**

```bash  theme={null}
go get -u 'github.com/anthropics/anthropic-sdk-go@v1.17.0'
```

***

## C\#

[C# library GitHub repo](https://github.com/anthropics/anthropic-sdk-csharp)

<Info>
  The C# SDK is currently in beta.
</Info>

**Requirements:** .NET 8 or later

**Installation:**

```bash  theme={null}
git clone git@github.com:anthropics/anthropic-sdk-csharp.git
dotnet add reference anthropic-sdk-csharp/src/Anthropic.Client
```

***

## Ruby

[Ruby library GitHub repo](https://github.com/anthropics/anthropic-sdk-ruby)

**Requirements:** Ruby 3.2.0 or later

**Installation:**

Add to your Gemfile:

```ruby  theme={null}
gem "anthropic", "~> 1.13.0"
```

Then run:

```bash  theme={null}
bundle install
```

***

## PHP

[PHP library GitHub repo](https://github.com/anthropics/anthropic-sdk-php)

<Info>
  The PHP SDK is currently in beta.
</Info>

**Requirements:** PHP 8.1.0 or higher

**Installation:**

```bash  theme={null}
composer require "anthropic-ai/sdk 0.3.0"
```

***

## Beta namespace in client SDKs

Every SDK has a `beta` namespace that is available for accessing new features that Anthropic releases in beta versions. Use this in conjunction with [beta headers](/en/api/beta-headers) to access these features. Refer to each SDK's GitHub repository for specific usage examples.


# Create a Message Batch
Source: https://docs.claude.com/en/api/creating-message-batches

post /v1/messages/batches
Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)

## Feature Support

The Message Batches API supports all active models. All features available in the Messages API, including beta features, are available through the Message Batches API.

Batches may contain up to 100,000 requests and be up to 256 MB in total size.


# Delete a Message Batch
Source: https://docs.claude.com/en/api/deleting-message-batches

delete /v1/messages/batches/{message_batch_id}
Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)



# Errors
Source: https://docs.claude.com/en/api/errors



## HTTP errors

Our API follows a predictable HTTP error code format:

* 400 - `invalid_request_error`: There was an issue with the format or content of your request. We may also use this error type for other 4XX status codes not listed below.
* 401 - `authentication_error`: There's an issue with your API key.
* 403 - `permission_error`: Your API key does not have permission to use the specified resource.
* 404 - `not_found_error`: The requested resource was not found.
* 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. The maximum request size is 32 MB for standard API endpoints.
* 429 - `rate_limit_error`: Your account has hit a rate limit.
* 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems.
* 529 - `overloaded_error`: The API is temporarily overloaded.

  <Warning>
    529 errors can occur when APIs experience high traffic across all users.

    In rare cases, if your organization has a sharp increase in usage, you might see 429 errors due to acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.
  </Warning>

When receiving a [streaming](/en/docs/build-with-claude/streaming) response via SSE, it's possible that an error can occur after returning a 200 response, in which case error handling wouldn't follow these standard mechanisms.

## Request size limits

The API enforces request size limits to ensure optimal performance:

| Endpoint Type                                            | Maximum Request Size |
| :------------------------------------------------------- | :------------------- |
| Messages API                                             | 32 MB                |
| Token Counting API                                       | 32 MB                |
| [Batch API](/en/docs/build-with-claude/batch-processing) | 256 MB               |
| [Files API](/en/docs/build-with-claude/files)            | 500 MB               |

If you exceed these limits, you'll receive a 413 `request_too_large` error. The error is returned from Cloudflare before the request reaches our API servers.

## Error shapes

Errors are always returned as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:

```JSON JSON theme={null}
{
  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

In accordance with our [versioning](/en/api/versioning) policy, we may expand the values within these objects, and it is possible that the `type` values will grow over time.

## Request id

Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. When contacting support about a specific request, please include this ID to help us quickly resolve your issue.

Our official SDKs provide this value as a property on top-level response objects, containing the value of the `request-id` header:

<CodeGroup>
  ```Python Python theme={null}
  import anthropic

  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=1024,
      messages=[
          {"role": "user", "content": "Hello, Claude"}
      ]
  )
  print(f"Request ID: {message._request_id}")
  ```

  ```TypeScript TypeScript theme={null}
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  const message = await client.messages.create({
    model: 'claude-sonnet-4-5',
    max_tokens: 1024,
    messages: [
      {"role": "user", "content": "Hello, Claude"}
    ]
  });
  console.log('Request ID:', message._request_id);
  ```
</CodeGroup>

## Long requests

<Warning>
  We highly encourage using the [streaming Messages API](/en/docs/build-with-claude/streaming) or [Message Batches API](/en/api/creating-message-batches) for long running requests, especially those over 10 minutes.
</Warning>

We do not recommend setting a large `max_tokens` values without using our [streaming Messages API](/en/docs/build-with-claude/streaming)
or [Message Batches API](/en/api/creating-message-batches):

* Some networks may drop idle connections after a variable period of time, which
  can cause the request to fail or timeout without receiving a response from Anthropic.
* Networks differ in reliability; our [Message Batches API](/en/api/creating-message-batches) can help you
  manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, you should be aware that setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

Our [SDKs](/en/api/client-sdks) will validate that your non-streaming Messages API requests are not expected to exceed a 10 minute timeout and
also will set a socket option for TCP keep-alive.


# Download a File
Source: https://docs.claude.com/en/api/files-content

GET /v1/files/{file_id}/content
Download the contents of a Claude generated file

The Files API allows you to upload and manage files to use with the Claude API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

<Note>
  The Files API is currently in beta. To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

  Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.
</Note>


# Create a File
Source: https://docs.claude.com/en/api/files-create

POST /v1/files
Upload a file

The Files API allows you to upload and manage files to use with the Claude API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

<Note>
  The Files API is currently in beta. To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

  Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.
</Note>


# Delete a File
Source: https://docs.claude.com/en/api/files-delete

DELETE /v1/files/{file_id}
Make a file inaccessible through the API

The Files API allows you to upload and manage files to use with the Claude API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

<Note>
  The Files API is currently in beta. To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

  Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.
</Note>


# List Files
Source: https://docs.claude.com/en/api/files-list

GET /v1/files
List files within a workspace

The Files API allows you to upload and manage files to use with the Claude API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

<Note>
  The Files API is currently in beta. To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

  Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.
</Note>


# Get File Metadata
Source: https://docs.claude.com/en/api/files-metadata

GET /v1/files/{file_id}

The Files API allows you to upload and manage files to use with the Claude API without having to re-upload content with each request. For more information about the Files API, see the [developer guide for files](/en/docs/build-with-claude/files).

<Note>
  The Files API is currently in beta. To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.

  Please reach out through our [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.
</Note>


# IP addresses
Source: https://docs.claude.com/en/api/ip-addresses

Anthropic services use fixed IP addresses for both inbound and outbound connections. You can use these addresses to configure your firewall rules for secure access to the Claude API and Console. These addresses will not change without notice.

## Inbound IP addresses

These are the IP addresses where Anthropic services receive incoming connections.

#### IPv4

`160.79.104.0/23`

#### IPv6

`2607:6bc0::/48`

## Outbound IP addresses

These are the stable IP addresses that Anthropic uses for outbound requests (for example, when making MCP tool calls to external servers).

#### IPv4

```
34.162.46.92
34.162.102.82
34.162.136.91
34.162.142.92
34.162.183.95
```


# List Message Batches
Source: https://docs.claude.com/en/api/listing-message-batches

get /v1/messages/batches
List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](/en/docs/build-with-claude/batch-processing)



# Messages
Source: https://docs.claude.com/en/api/messages

post /v1/messages
Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](/en/docs/initial-setup)



# Count Message tokens
Source: https://docs.claude.com/en/api/messages-count-tokens

post /v1/messages/count_tokens
Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](/en/docs/build-with-claude/token-counting)



# Migrating from Text Completions
Source: https://docs.claude.com/en/api/migrating-from-text-completions-to-messages

Migrating from Text Completions to Messages

<Note>
  The Text Completions API has been deprecated in favor of the Messages API.
</Note>

When migrating from Text Completions to [Messages](/en/api/messages), consider the following changes.

### Inputs and outputs

The largest change between Text Completions and the Messages is the way in which you specify model inputs and receive outputs from the model.

With Text Completions, inputs are raw strings:

```Python Python theme={null}
prompt = "\n\nHuman: Hello there\n\nAssistant: Hi, I'm Claude. How can I help?\n\nHuman: Can you explain Glycolysis to me?\n\nAssistant:"
```

With Messages, you specify a list of input messages instead of a raw prompt:

<CodeGroup>
  ```json Shorthand theme={null}
  messages = [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help?"},
    {"role": "user", "content": "Can you explain Glycolysis to me?"},
  ]
  ```

  ```json Expanded theme={null}
  messages = [
    {"role": "user", "content": [{"type": "text", "text": "Hello there."}]},
    {"role": "assistant", "content": [{"type": "text", "text": "Hi, I'm Claude. How can I help?"}]},
    {"role": "user", "content":[{"type": "text", "text": "Can you explain Glycolysis to me?"}]},
  ]
  ```
</CodeGroup>

Each input message has a `role` and `content`.

<Tip>
  **Role names**

  The Text Completions API expects alternating `\n\nHuman:` and `\n\nAssistant:` turns, but the Messages API expects `user` and `assistant` roles. You may see documentation referring to either "human" or "user" turns. These refer to the same role, and will be "user" going forward.
</Tip>

With Text Completions, the model's generated text is returned in the `completion` values of the response:

```Python Python theme={null}
>>> response = anthropic.completions.create(...)
>>> response.completion
" Hi, I'm Claude"
```

With Messages, the response is the `content` value, which is a list of content blocks:

```Python Python theme={null}
>>> response = anthropic.messages.create(...)
>>> response.content
[{"type": "text", "text": "Hi, I'm Claude"}]
```

### Putting words in Claude's mouth

With Text Completions, you can pre-fill part of Claude's response:

```Python Python theme={null}
prompt = "\n\nHuman: Hello\n\nAssistant: Hello, my name is"
```

With Messages, you can achieve the same result by making the last input message have the `assistant` role:

```Python Python theme={null}
messages = [
  {"role": "human", "content": "Hello"},
  {"role": "assistant", "content": "Hello, my name is"},
]
```

When doing so, response `content` will continue from the last input message `content`:

```JSON JSON theme={null}
{
  "role": "assistant",
  "content": [{"type": "text", "text": " Claude. How can I assist you today?" }],
  ...
}
```

### System prompt

With Text Completions, the [system prompt](/en/docs/build-with-claude/prompt-engineering/system-prompts) is specified by adding text before the first `\n\nHuman:` turn:

```Python Python theme={null}
prompt = "Today is January 1, 2024.\n\nHuman: Hello, Claude\n\nAssistant:"
```

With Messages, you specify the system prompt with the `system` parameter:

```Python Python theme={null}
anthropic.Anthropic().messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system="Today is January 1, 2024.", # <-- system prompt
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
```

### Model names

The Messages API requires that you specify the full model version (e.g. `claude-sonnet-4-5-20250929`).

We previously supported specifying only the major version number (e.g. `claude-2`), which resulted in automatic upgrades to minor versions. However, we no longer recommend this integration pattern, and Messages do not support it.

### Stop reason

Text Completions always have a `stop_reason` of either:

* `"stop_sequence"`: The model either ended its turn naturally, or one of your custom stop sequences was generated.
* `"max_tokens"`: Either the model generated your specified `max_tokens` of content, or it reached its [absolute maximum](/en/docs/about-claude/models/overview#model-comparison-table).

Messages have a `stop_reason` of one of the following values:

* `"end_turn"`: The conversational turn ended naturally.
* `"stop_sequence"`: One of your specified custom stop sequences was generated.
* `"max_tokens"`: (unchanged)

### Specifying max tokens

* Text Completions: `max_tokens_to_sample` parameter. No validation, but capped values per-model.
* Messages: `max_tokens` parameter. If passing a value higher than the model supports, returns a validation error.

### Streaming format

When using `"stream": true` in with Text Completions, the response included any of `completion`, `ping`, and `error` server-sent-events.

Messages can contain multiple content blocks of varying types, and so its streaming format is somewhat more complex. See [Messages streaming](/en/docs/build-with-claude/streaming) for details.


# Get a Model
Source: https://docs.claude.com/en/api/models

get /v1/models/{model_id}
Get a specific model.

The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.



# List Models
Source: https://docs.claude.com/en/api/models-list

get /v1/models
List available models.

The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.




---

**Navigation:** [← Previous](./20-airport-code-analyst.md) | [Index](./index.md) | [Next →](./22-openai-sdk-compatibility.md)
