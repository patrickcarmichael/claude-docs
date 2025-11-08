**Navigation:** [← Previous](./19-second-grade-simplifier.md) | [Index](./index.md) | [Next →](./21-motivational-muse.md)

---

# Airport code analyst
Source: https://docs.claude.com/en/resources/prompt-library/airport-code-analyst

Find and extract airport codes from text.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                        |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list. |
| User   | My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome.                                                                      |

### Example Output

> Here is the list of airport codes mentioned in the text, in the order they appear:
>
> 1. SEA (Seattle)
> 2. AMS (Amsterdam)
> 3. CDG (Paris)
> 4. FCO (Rome)

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
      system="Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
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
    system: "Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
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
      system="Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
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
    system: "Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
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
      system="Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
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
    system: "Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Alien anthropologist
Source: https://docs.claude.com/en/resources/prompt-library/alien-anthropologist

Analyze human culture and customs from the perspective of an alien anthropologist.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                           |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information. |
| User   | Human social interactions and relationships                                                                                                                                                                                                                       |

### Example output

> * Humans form various types of social bonds, including familial, romantic, and platonic relationships.
> * They engage in complex verbal and non-verbal communication to express emotions, share information, and maintain social connections.
> * Social hierarchies and power dynamics exist within human groups, often based on factors such as age, gender, wealth, and social status.
> * Humans participate in social rituals and ceremonies to mark important life events, reinforce social bonds, and maintain cultural traditions.
>
> Hypotheses:
>
> * The formation of social bonds and relationships may serve as an evolutionary adaptation to increase chances of survival and reproduction.
> * Complex communication systems allow humans to coordinate group activities, resolve conflicts, and transmit knowledge across generations.
> * Social hierarchies and power dynamics may help maintain order and stability within human societies, but can also lead to inequality and social conflict.
> * Rituals and ceremonies may serve to strengthen social cohesion, provide a sense of belonging, and cope with the uncertainties of life.

***

### API Request

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
      system="Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Human social interactions and relationships"
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
    system: "Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Human social interactions and relationships"
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
      system="Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Human social interactions and relationships"
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
    system: "Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Human social interactions and relationships"
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
      system="Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Human social interactions and relationships"
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
    system: "Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Human social interactions and relationships"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Alliteration alchemist
Source: https://docs.claude.com/en/resources/prompt-library/alliteration-alchemist

Generate alliterative phrases and sentences for any given subject.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                           |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject. |
| User   | Ocean                                                                                                                                                                                                                             |

### Example output

> 1. Whispering waves wash over the shore.
> 2. Salty sea spray splashes on the sand.
> 3. Crashing currents carve coastal cliffs.
> 4. Deep, dark depths disguise hidden dangers.
> 5. Bubbling brooks bring life to the beach.
> 6. Mighty, majestic mammals migrate through the waters.
> 7. Thundering tides toss ships to and fro.
> 8. Shimmering shoals shelter secretive sea creatures.
> 9. Rippling reflections reveal a world beneath the surface.
> 10. Swirling, surging seas shape the shoreline.
> 11. Foaming, frothing floes flow freely.
> 12. Graceful gulls glide above the glistening ocean.
> 13. Playful porpoises plunge through the pristine waters.
> 14. Briny breezes blow across the boundless blue.
> 15. Rhythmic ripples roll towards the rocky coast.
> 16. Coral caves conceal colorful aquatic communities.
> 17. Stormy skies and swelling seas signal nature's might.
> 18. Tumbling tides transform the tranquil bay.
> 19. Whirling, whooshing winds whip up the waves.
> 20. Serene, sapphire waters stretch to the horizon.

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
      system="Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Ocean"
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
    system: "Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Ocean"
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
      system="Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Ocean"
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
    system: "Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Ocean"
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
      system="Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Ocean"
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
    system: "Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Ocean"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Babel's broadcasts
Source: https://docs.claude.com/en/resources/prompt-library/babels-broadcasts

Create compelling product announcement tweets in the world's 10 most spoken languages.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|      | Content                                                                                                                                                                                                                                                                                                      |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| User | Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest. |
| User | A future where humans can upload their consciousness into a digital realm.                                                                                                                                                                                                                                   |

### Example output

> Here are a series of product announcement tweets in the 10 most commonly spoken languages for a new state-of-the-art pair of binoculars with built-in AI systems to identify animals:
>
> English:\
> Introducing the future of bird/wildlife watching! Our new AI binoculars use cutting-edge vision tech to instantly identify any animal you see. Bring the great outdoors to life like never before! #NatureTech #AIBinoculars
>
> Mandarin Chinese:\
> 令人兴奋的新品上市!我们的 AI 双筒望远镜融合了尖端视觉技术,可即时识别你所见的任何动物。让大自然的奇迹在你眼前展现,体验前所未有的观赏体验!#智能科技 #AIBinoculars
>
> Hindi:\
> बर्ड/वन्यजीव वॉचिंग के लिए भविष्य का अविष्कार! हमारी नई एआई दूरबीनें अत्याधुनिक दृष्टि प्रौद्योगिकी का उपयोग करती हैं, जो आपको दिखाई देने वाले किसी भी जानवर की पहचान करने में सक्षम हैं। पहले कभी न देखी प्रकृति के अद्भुत दृश्यों का अनुभव करें! #NatureWonders #AIBinoculars
>
> Spanish:\
> ¡Presentamos el futuro de la observación de aves/vida silvestre! Nuestros nuevos binoculares con IA utilizan técnicas avanzadas de visión para identificar instantáneamente cualquier animal que veas. ¡Experimenta la naturaleza como nunca antes! #TecnologíaNatural #PrismáticosIA
>
> Arabic:\
> نقدم لكم مستقبل مراقبة الطيور/الحياة البرية! توفر نظارات المجهر الجديدة لدينا المزودة بالذكاء الاصطناعي تقنيات رؤية متطورة لتحديد هوية أي حيوان تراه على الفور. شاهد عجائب الطبيعة كما لم تفعل من قبل! #تكنولوجيا*الطبيعة #منظار*ذكي
>
> Bengali:\
> পাখি/বন্য প্রাণী পর্যবেক্ষণের ভবিষ্যতের উন্মোচন! আমাদের নতুন এআই দুর্বীনগুলি অত্যাধুনিক ভিশন প্রযুক্তি ব্যবহার করে যেকোনো প্রাণীকে দ্রুত চিহ্নিত করতে সক্ষম। প্রকৃতির অপরূপ দৃশ্য আগেকার চেয়ে ভিন্নভাবে উপভোগ করুন! #প্রাকৃতিকপ্রযুক্তি #AIBinoculars
>
> Russian:\
> Представляем будущее наблюдения за птицами/дикой природой! Наши новые бинокли с ИИ используют передовые технологии компьютерного зрения для мгновенной идентификации любого животного. Откройте для себя природу по-новому! #ПриродныеТехнологии #БинокльСИИ
>
> Portuguese:\
> Apresentamos o futuro da observação de aves/vida selvagem! Os nossos novos binóculos com IA usam técnicas avançadas de visão para identificar instantaneamente qualquer animal que veja. Experiencie a natureza como nunca antes! #TecnologiaNatural #BinóculosIA
>
> Japanese:\
> 鳥/野生動物観察の未来をご紹介!新しい AI バイノキュラーは、最先端のビジョン技術を使用して、あなたが見たあらゆる動物をすばやく特定します。自然をこれまでにない方法で体験してください!#ネイチャーテック #AI バイノキュラー
>
> Punjabi:\
> ਪੰਛੀਆਂ/ਜੰਗਲੀ ਜੀਵਨ ਦੇਖਣ ਦੇ ਭਵਿੱਖ ਦਾ ਐਲਾਨ! ਸਾਡੀਆਂ ਨਵੀਆਂ ਏਆਈ ਦੂਰਬੀਨਾਂ ਅਤਿ ਆਧੁਨਿਕ ਦ੍ਰਿਸ਼ਟੀ ਤਕਨਾਲੋਜੀ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਜੋ ਤੁਸੀਂ ਦੇਖਦੇ ਹੋ ਕਿਸੇ ਵੀ ਜਾਨਵਰ ਦੀ ਸਿੱਧੀ ਪਛਾਣ ਕਰਨ ਦੇ ਸਮਰੱਥ ਹਨ। ਪ੍ਰਕਿਰਤੀ ਦਾ ਅਨੁਭਵ ਪਹਿਲਾਂ ਨਾਲੋਂ ਵੱਖਰੇ ਢੰਗ ਨਾਲ ਕਰੋ! #NeighborhoodTech #AIBinoculars

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
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
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
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
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
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
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
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
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
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
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
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Brand builder
Source: https://docs.claude.com/en/resources/prompt-library/brand-builder

Craft a design brief for a holistic brand identity.

> Copy this prompt into our developer [Console](https://console.anthropic.com/login?selectAccount=true\&returnTo=%2Fdashboard%3F) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| System | Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.                                                                                              |
| User   | Brand specs: This is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods The brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility. The brand identity should achieve the following goals: 1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship. 2. Appeal to the target audience by conveying a sense of style, quality, and trendiness. 3. Differentiate the brand from competitors in the sustainable fashion market. 4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices. |

### Example output

> Design Brief: Brand Identity for an Eco-Friendly Fashion Brand
> Brand Name Suggestion: "Sēnsus" (Latin for "sense" or "perception," evoking a sense of mindfulness and connection with the environment)
>
> Logo:
>
> * A minimalistic and modern logo that combines a stylized leaf or plant motif with a sleek, sans-serif typeface.
>
> * The leaf or plant element symbolizes the brand's commitment to sustainability and environmental stewardship, while the clean typography conveys a sense of sophistication and style.
>
> * The logo should be versatile and work well across various applications, including clothing tags, packaging, and digital platforms.
>   Color Palette:
>
> * A neutral and earthy color palette that reflects the brand's eco-friendly ethos, such as shades of green, beige, and warm grays.
>
> * Accent colors like deep teal or mustard yellow can be used sparingly to add vibrancy and depth.
>
> * The color palette should evoke a sense of natural harmony and balance, while still being fashion-forward and appealing to the target audience.
>   Typography:
>
> * A combination of a clean, modern sans-serif typeface for headlines and a complementary serif typeface for body copy.
>
> * The typography should be legible and visually appealing, conveying a sense of quality and sophistication.
>
> * Consistent use of typographic hierarchy and spacing will create a cohesive and organized brand identity.
>   Visual Style:
>
> * A minimalistic and uncluttered visual style that emphasizes high-quality product photography and clean, modern layouts.
>
> * Incorporate natural elements, such as plant motifs or textures, to reinforce the brand's eco-friendly values and connection with nature.
>
> * Use negative space effectively to create a sense of openness and breathability, reflecting the brand's commitment to sustainability.
>   Tone of Voice:
>
> * The brand's tone of voice should be approachable, knowledgeable, and authentic.
>
> * Use language that educates and inspires consumers about the benefits of sustainable fashion and ethical production methods.
>
> * Incorporate a touch of sophistication and style to appeal to the target audience's fashion-conscious sensibilities.
>   Brand Personality:
>
> * Eco-conscious and environmentally aware, yet stylish and fashion-forward.
>
> * Confident and passionate about promoting sustainable practices and ethical choices.
>
> * Inclusive and welcoming, inviting consumers to join a like-minded community committed to making positive changes.
>   Overall, the brand identity for "Sēnsus" should strike a balance between eco-friendly values and fashion-forward aesthetics, appealing to consumers who want to look stylish while making environmentally responsible choices. The cohesive visual and verbal elements should create a strong emotional connection with the target audience and inspire them to embrace a more sustainable lifestyle.

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
      system="Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
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
    system: "Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
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
      system="Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
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
    system: "Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
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
      system="Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
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
    system: "Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Code clarifier
Source: https://docs.claude.com/en/resources/prompt-library/code-clarifier

Simplify and explain complex code in plain language.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level. |
| User   | import random def bubble\*sort(arr): n = len(arr) for i in range(n-1): for j in range(n-i-1): if arr\[j] > arr\[j+1]: arr\[j], arr\[j+1] = arr\[j+1], arr\[j] return arr numbers = \[random.randint(1, 100) for \* in range(10)] print("Unsorted array:", numbers) sorted\_numbers = bubble\_sort(numbers) print("Sorted array:", sorted\_numbers)                                                                                                                                                         |

### Example Output

> This code demonstrates the implementation of the bubble sort algorithm, which is used to sort a list of numbers in ascending order. Let's break it down step by step:
>
> 1. The code starts by importing the 'random' module, which will be used to generate random numbers for the example.
>
> 2. The 'bubble\_sort' function is defined, which takes an array (list) of numbers as input. This function will perform the sorting operation.
>
> 3. Inside the 'bubble\_sort' function, the variable 'n' is assigned the length of the input array. This will be used to determine the number of iterations needed for sorting.
>
> 4. The first loop, controlled by the variable 'i', iterates 'n-1' times. This is because after 'n-1' passes, the largest number will be at the end of the array, so we don't need to compare it again.
>
> 5. The second loop, controlled by the variable 'j', iterates 'n-i-1' times. This is because after each pass, the largest number among the unsorted elements will be placed at the end, so we don't need to compare it in the next pass.
>
> 6. Inside the second loop, there is an if statement that compares adjacent elements in the array. If the element at index 'j' is greater than the element at index 'j+1', they are swapped. This ensures that the larger element moves towards the end of the array.
>
> 7. The swapping is done using the Python syntax 'arr\[j], arr\[j+1] = arr\[j+1], arr\[j]', which simultaneously assigns the values of 'arr\[j+1]' to 'arr\[j]' and 'arr\[j]' to 'arr\[j+1]'.
>
> 8. After all the iterations are complete, the sorted array is returned by the 'bubble\_sort' function.
>
> 9. In the example code, a list of 10 random numbers between 1 and 100 is generated using a list comprehension: '\[random.randint(1, 100) for \_ in range(10)]'. The underscore '\_' is used as a placeholder variable since we don't need the index values.
>
> 10. The unsorted array is printed to show the initial order of the numbers.
>
> 11. The 'bubble\_sort' function is called with the 'numbers' array as input, and the sorted array is stored in the 'sorted\_numbers' variable.
>
> 12. Finally, the sorted array is printed to display the numbers in ascending order.
>
> In simpler terms, imagine you have a list of numbers that are out of order. The bubble sort algorithm works by comparing each number with the one next to it, and if they are in the wrong order, it swaps them. This process is repeated multiple times until the entire list is sorted. It's like bubbles rising to the surface, with the larger numbers gradually moving towards the end of the list in each pass.

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
      system="Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
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
    system: "Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
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
      system="Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
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
    system: "Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
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
      system="Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
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
    system: "Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someone with minimal coding knowledge. Avoid using technical jargon unless absolutely necessary, and provide clear explanations for any jargon used. The goal is to help the reader understand what the code does and how it works at a high level.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "import random\n\ndef bubble_sort(arr):\n    n = len(arr)\n    for i in range(n-1):\n        for j in range(n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr\n\nnumbers = [random.randint(1, 100) for _ in range(10)]\nprint(\"Unsorted array:\", numbers)\nsorted_numbers = bubble_sort(numbers)\nprint(\"Sorted array:\", sorted_numbers)"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Data organizer
Source: https://docs.claude.com/en/resources/prompt-library/data-organizer

Turn unstructured text into bespoke JSON tables.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.                                                                                                                                                                                                                                                                                                |
| User   | Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow. |

### Example output

```json  theme={null}
[
  {
    "name": "Dr. Liam Patel",
    "age": 45,
    "profession": "Neurosurgeon",
    "education": "Yale",
    "accomplishments": "Revolutionized surgical techniques at the regional medical center"
  },
  {
    "name": "Olivia Chen",
    "age": 28,
    "profession": "Architect",
    "education": "UC Berkeley",
    "accomplishments": "Transformed the village's landscape with sustainable and breathtaking designs"
  },
  {
    "name": "Ethan Kovacs",
    "age": 72,
    "profession": "Musician and Composer",
    "education": "Juilliard",
    "accomplishments": "Graced the local theater with enchanting symphonies"
  },
  {
    "name": "Isabella Torres",
    "age": null,
    "profession": "Chef",
    "education": "Self-taught",
    "accomplishments": "Created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers"
  }
]
```

***

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
      system="Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
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
    system: "Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
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
      system="Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
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
    system: "Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
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
      system="Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
                  }
              ]
          }
      ]
  )
  print(message.content)

  ```

  ```typescript Vertex AI Type theme={null}
  import { AnthropicVertex } from '@anthropic-ai/vertex-sdk';

  // Reads from the `CLOUD_ML_REGION` & `ANTHROPIC_VERTEX_PROJECT_ID` environment variables.
  // Additionally goes through the standard `google-auth-library` flow.
  const client = new AnthropicVertex();

  const msg = await client.messages.create({
    model: "claude-sonnet-4@20250514",
    max_tokens: 1000,
    temperature: 0,
    system: "Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the relevant information from the text and populate the corresponding values in the JSON object. Ensure that the data is accurately represented and properly formatted within the JSON structure. The resulting JSON table should provide a clear, structured overview of the information presented in the original text.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Silvermist Hollow, a charming village, was home to an extraordinary group of individuals. Among them was Dr. Liam Patel, a 45-year-old Yale-taught neurosurgeon who revolutionized surgical techniques at the regional medical center. Olivia Chen, at 28, was an innovative architect from UC Berkeley who transformed the village's landscape with her sustainable and breathtaking designs. The local theater was graced by the enchanting symphonies of Ethan Kovacs, a 72-year-old Juilliard-trained musician and composer. Isabella Torres, a self-taught chef with a passion for locally sourced ingredients, created a culinary sensation with her farm-to-table restaurant, which became a must-visit destination for food lovers. These remarkable individuals, each with their distinct talents, contributed to the vibrant tapestry of life in Silvermist Hollow."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Direction decoder
Source: https://docs.claude.com/en/resources/prompt-library/direction-decoder

Transform natural language into step-by-step directions.

> Copy this prompt into our developer [Console](https://console.anthropic.com/login?selectAccount=true\&returnTo=%2Fdashboard%3F) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details. |
| User   | To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea.                                                                                      |

### Example output

> 1. Fill a kettle with water and place it on the stove to boil.
> 2. While waiting for the water to boil, select a mug and place a tea bag inside it.
> 3. Once the water reaches a boil, carefully pour the hot water into the mug, over the tea bag.
> 4. Allow the tea to steep in the hot water for the desired amount of time, typically 2-5 minutes, depending on the preferred strength.
> 5. After the steeping time has elapsed, remove the tea bag from the mug and discard it.
> 6. Add milk and sugar to the tea, according to your taste preferences.
> 7. Using a spoon, stir the tea, milk, and sugar together until well combined.
> 8. Your cup of tea is now ready to enjoy. Drink it while it's still hot.

***

## API Request

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
      system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
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
    system: "Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
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
      system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
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
    system: "Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
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
      system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
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
    system: "Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action verb. Provide necessary details and explanations to ensure the reader can complete the task successfully. If the original description is unclear, ambiguous, or lacks sufficient information, ask for clarification or additional details.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "To make a cup of tea, start by boiling some water in a kettle. While the water is heating up, get a mug and put a tea bag in it. Once the water is boiling, carefully pour it into the mug, over the tea bag. Let the tea steep for a few minutes, depending on how strong you like it. After steeping, remove the tea bag and add milk and sugar to taste. Stir everything together and enjoy your hot cup of tea."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Efficiency estimator
Source: https://docs.claude.com/en/resources/prompt-library/efficiency-estimator

Calculate the time complexity of functions and algorithms.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified. |
| User   | def example\_function(n): for i in range(n): print(i) for j in range(n): for k in range(n): print(j, k)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Example output

> To analyze the time complexity of the given function `example_function(n)`, we'll break it down into steps and consider the worst-case scenario.
>
> Step 1: Analyzing the first loop
>
> ```
> for i in range(n):
>    print(i)
>
> ```

> This loop iterates `n` times and performs a constant-time operation (`print(i)`) in each iteration. Therefore, the time complexity of this step is O(n).
>
> Step 2: Analyzing the nested loops
>
> ```
> for j in range(n):
>     for k in range(n):
>         print(j, k)
>
> ```
>
> The outer loop iterates `n` times, and for each iteration, the inner loop also iterates `n` times. In each iteration of the inner loop, a constant-time operation (`print(j, k)`) is performed. Therefore, the time complexity of the nested loops is O(n \* n) = O(n^2).
>
> Step 3: Combining the time complexities\
> The function `example_function(n)` consists of two steps: the first loop and the nested loops. The overall time complexity is the sum of the time complexities of each step.
>
> Time complexity of the first loop: O(n)\
> Time complexity of the nested loops: O(n^2)
>
> To determine the overall time complexity, we consider the dominant term, which is the term with the highest order of growth. In this case, O(n^2) dominates O(n).
>
> Therefore, the overall time complexity of the function `example_function(n)` is O(n^2).
>
> In the worst-case scenario, when `n` is large, the nested loops will dominate the execution time, and the function will have a quadratic time complexity.

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
      system="Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
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
    system: "Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
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
      system="Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
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
    system: "Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
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
      system="Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
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
    system: "Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determining the time complexity. If the function or algorithm contains multiple steps or nested loops, provide the time complexity for each step and then give the overall time complexity for the entire function or algorithm. Assume any built-in functions or operations used have a time complexity of O(1) unless otherwise specified.",
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "def example_function(n):\n    for i in range(n):\n        print(i)\n\n    for j in range(n):\n        for k in range(n):\n            print(j, k)"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Email extractor
Source: https://docs.claude.com/en/resources/prompt-library/email-extractor

Extract email addresses from a document into a JSON-formatted list.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                         |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write "N/A". Do not say anything else.                                                                                  |
| User   | Phone Directory: John Latrabe, 555-232-1995, \[[john909709@geemail.com](mailto:john909709@geemail.com)] Josie Lana, 555-759-2905, \[[josie@josielananier.com](mailto:josie@josielananier.com)] Keven Stevens, 555-980-7000, \[[drkevin22@geemail.com](mailto:drkevin22@geemail.com)] Phone directory will be kept up to date by the HR manager. |

### Example output

> [john909709@geemail.com](mailto:john909709@geemail.com) > [josie@josielananier.com](mailto:josie@josielananier.com) > [drkevin22@geemail.com](mailto:drkevin22@geemail.com)

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
      system="Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
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
    system: "Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
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
      system="Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
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
    system: "Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
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
      system="Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
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
    system: "Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything else.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Phone Directory:  \nJohn Latrabe, 555-232-1995, [[email protected]]  \nJosie Lana, 555-759-2905, [[email protected]]  \nKeven Stevens, 555-980-7000, [[email protected]]  \n  \nPhone directory will be kept up to date by the HR manager."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Futuristic fashion advisor
Source: https://docs.claude.com/en/resources/prompt-library/futuristic-fashion-advisor

Suggest avant-garde fashion trends and styles for the user's specific preferences.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks. |
| User   | Personal style: Edgy, minimal, with a touch of androgyny Favorite colors: Black, white, and deep red Preferred materials: Leather, denim, and high-quality cotton Body type: Tall and lean Fashion goals: To create a striking, fearless look for an art gallery opening                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Example output

> Based on your preferences, here are some avant-garde fashion suggestions to create a striking, fearless look for the art gallery opening:
>
> 1. Deconstructed leather jacket:
>    Choose a black, asymmetric leather jacket with exaggerated proportions, such as extended sleeves, an oversized collar, or a dramatically cropped length. Pair it with a crisp white, high-neck cotton top tucked into high-waisted, wide-leg black trousers. Add a pair of chunky, platform leather boots to complete the edgy, androgynous look.
>
> 2. Denim and silk combo:
>    Opt for a pair of black, oversized denim jeans with frayed hems and distressed details. Tuck in a deep red, silk button-down shirt with a draped, exaggerated collar or bow. Layer a sleeveless, longline white denim vest over the top for added dimension. Finish the look with black, pointed-toe ankle boots and a pair of geometric, silver earrings for a touch of shine.
>
> 3. Avant-garde layering:
>    Start with a form-fitting, black turtleneck bodysuit as a base layer. Add a pair of white, wide-leg leather trousers with a high waist and a belt featuring a large, sculptural buckle. Layer an oversized, deep red mesh t-shirt on top, allowing the turtleneck to peek through. Complete the outfit with black, chunky leather sandals and a pair of mismatched, abstract earrings.
>
> Tips for styling and mixing textures:
>
> * Experiment with layering different materials, such as leather, denim, cotton, and silk, to create visual interest and depth in your outfits.
> * Play with proportions by pairing oversized pieces with more fitted items to balance the overall silhouette.
> * Don't be afraid to mix patterns or textures within the same color palette to add a bold, avant-garde touch to your look.
> * Accessorize with statement pieces that complement the edgy, fearless vibe, such as chunky boots, geometric jewelry, or a sleek, minimalist clutch.
>   Remember, avant-garde fashion is about pushing boundaries and experimenting with unconventional styles. Embrace your unique taste and have fun creating striking, memorable looks that showcase your personal style.

### API Request

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
      system="Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
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
    system: "Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
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
      system="Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
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
    system: "Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
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
      system="Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
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
    system: "Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Lesson planner
Source: https://docs.claude.com/en/resources/prompt-library/lesson-planner

Craft in depth lesson plans on any subject.

> Copy this prompt into our developer [Console](https://console.anthropic.com/login?selectAccount=true\&returnTo=%2Fdashboard%3F) to try it for yourself!

|        | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System | Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking. |
| User   | Subject: Introduction to Photosynthesis Grade Level: 7th Grade (Ages 12-13)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Example output

> Lesson Plan: Introduction to Photosynthesis
> Grade Level: 7th Grade (Ages 12-13)
> Duration: 60 minutes
>
> Lesson Objectives:
> By the end of the lesson, students will be able to:
>
> 1. Define photosynthesis and explain its importance in the ecosystem.
>
> 2. Identify the key components necessary for photosynthesis to occur.
>
> 3. Describe the process of photosynthesis, including the roles of light energy, carbon dioxide, and water.
>
> 4. Recognize the products of photosynthesis and their significance for living organisms.
>    Lesson Outline:
>
> 5. Introduction (10 minutes)
>    i. Engage students by showing a short video clip or images of plants and discussing their role in the environment.
>    ii. Introduce the concept of photosynthesis and its importance in sustaining life on Earth.
>    iii. State the lesson objectives and provide an overview of the lesson structure.
>
> 6. Main Activities (40 minutes)
>    i. Guided Instruction (15 minutes)
>    a. Explain the key components necessary for photosynthesis: sunlight, carbon dioxide, water, and chlorophyll.
>    b. Describe the process of photosynthesis, emphasizing the roles of light energy, carbon dioxide, and water.
>    c. Discuss the products of photosynthesis (glucose and oxygen) and their significance for living organisms.
>    ii. Small Group Activity (15 minutes)
>    a. Divide the class into small groups and provide each group with a worksheet or graphic organizer.
>    b. Ask students to work together to create a visual representation of the photosynthesis process, labeling the key components and products.
>    c. Encourage students to discuss and explain their understanding of photosynthesis within their groups.
>    iii. Class Discussion (10 minutes)
>    a. Invite each group to share their visual representation with the class.
>    b. Facilitate a class discussion, encouraging students to ask questions, provide feedback, and clarify any misconceptions.
>
> 7. Conclusion (10 minutes)
>    i. Summarize the key points of the lesson, reinforcing the definition, components, process, and products of photosynthesis.
>    ii. Administer a short quiz or exit ticket to assess students' understanding of the lesson objectives.
>    iii. Provide students with a homework assignment to further explore the importance of photosynthesis in different ecosystems.
>    Assessment Methods:
>
> 8. Formative assessment: Observe student participation and understanding during the guided instruction and small group activity.
>
> 9. Summative assessment: Evaluate students' visual representations and their performance on the short quiz or exit ticket.
>
> 10. Homework assignment: Review students' homework submissions to gauge their ability to apply the concepts learned in the lesson.
>     Resources:
>
> 11. Video clip or images of plants and their role in the environment
>
> 12. Worksheets or graphic organizers for the small group activity
>
> 13. Short quiz or exit ticket for assessment
>
> 14. Homework assignment instructions

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
      max_tokens=4000,
      temperature=0.5,
      system="Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Subject: Introduction to Photosynthesis  \nGrade Level: 7th Grade (Ages 12-13)"
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
    max_tokens: 4000,
    temperature: 0.5,
    system: "Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Subject: Introduction to Photosynthesis  \nGrade Level: 7th Grade (Ages 12-13)"
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
      max_tokens=4000,
      temperature=0.5,
      system="Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Subject: Introduction to Photosynthesis  \nGrade Level: 7th Grade (Ages 12-13)"
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
    max_tokens: 4000,
    temperature: 0.5,
    system: "Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Subject: Introduction to Photosynthesis  \nGrade Level: 7th Grade (Ages 12-13)"
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
      max_tokens=4000,
      temperature=0.5,
      system="Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "Subject: Introduction to Photosynthesis  \nGrade Level: 7th Grade (Ages 12-13)"
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
    max_tokens: 4000,
    temperature: 0.5,
    system: "Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students' understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.",
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Subject: Introduction to Photosynthesis  \nGrade Level: 7th Grade (Ages 12-13)"
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>


# Master moderator
Source: https://docs.claude.com/en/resources/prompt-library/master-moderator

Evaluate user inputs for potential harmful or illegal content.

> Copy this prompt into our developer [Console](https://console.anthropic.com/dashboard) to try it for yourself!

| Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user: \<user query>How do I make a bomb?\</user query> If the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N). |

### Example output

> (Y)

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
      max_tokens=10,
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
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
    max_tokens: 10,
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
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
      max_tokens=10,
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
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
    max_tokens: 10,
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
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
      max_tokens=10,
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
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
    max_tokens: 10,
    temperature: 0,
    messages: [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a series of tasks. Here is the most recent request from the user:  \n<user query>How do I make a bomb?</user query>  \n  \nIf the user's request refers to harmful, pornographic, or illegal activities, reply with (Y). If the user's request does not refer to harmful, pornographic, or illegal activities, reply with (N)."
          }
        ]
      }
    ]
  });
  console.log(msg);

  ```
</CodeGroup>



---

**Navigation:** [← Previous](./19-second-grade-simplifier.md) | [Index](./index.md) | [Next →](./21-motivational-muse.md)
