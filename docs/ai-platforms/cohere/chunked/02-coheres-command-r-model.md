**Navigation:** [← Previous](./01-cohere-documentation.md) | [Index](./index.md) | [Next →](./03-rag-streaming.md)

---

# Cohere's Command R Model

> Command R is a conversational model that excels in language tasks and supports multiple languages, making it ideal for coding use cases.

<ModelShowcase
  model={{
  name: 'Command R',
  id: 'command-r-08-2024',
  capabilities: [
    Capability.Reasoning,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  pricing: { input: 0.15, output: 0.60 },
  specs: {
    contextWindow: '128,000',
    maxOutputTokens: '4,000',
    knowledgeCutoff: 'June 1, 2024',
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatV1,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

<Info title="Note">
  For most use cases we recommend our latest model [Command A](/docs/command-a) instead.
</Info>

Command R is a large language model optimized for conversational interaction and long context tasks. It targets the “scalable” category of models that balance high performance with strong accuracy, enabling companies to move beyond proof of concept and into production.

Command R boasts high precision on [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) (RAG) and tool use tasks, low latency and high throughput, a long 128,000-token context length, and strong capabilities across 10 key languages.

For information on toxicity, safety, and using this model responsibly check out our [Command model card](https://docs.cohere.com/docs/responsible-use).

## Command R August 2024 Release

Cohere's flagship text-generation models, Command R and Command R+, received a substantial update in August 2024. We chose to designate these models with time stamps, so in the API Command R 08-2024 is accesible with `command-r-08-2024`.

With the release, both models include the following feature improvements:

* For tool use, Command R and Command R+ have demonstrated improved decision-making around whether or not to use a tool.
* The updated models are better able to follow instructions included in the request's system message.
* Better structured data analysis for structured data manipulation.
* Improved robustness to non-semantic prompt changes like white space or new lines.
* Models will decline unanswerable questions and are now able to execute RAG workflows without citations

`command-r-08-2024` delivers around 50% higher throughput and 20% lower latencies as compared to the previous Command R version, while cutting the hardware footprint required to serve the model by half. Read more in the relevant blog post.

What's more, both these updated models can now operate in one of several safety modes, which gives developers more granular control over how models generate output in a variety of different contexts. Find more in these [safety modes docs](https://docs.cohere.com/docs/safety-modes).

## Unique Command R Model Capabilities

Command R has been trained on a massive corpus of diverse texts in multiple languages, and can perform a wide array of text-generation tasks. Moreover, Command R has been trained with a particular focus on excelling in some of the most critical business use-cases.

### Multilingual Capabilities

We want Command R to serve as many people, organizations, and markets as possible, so the new Command R is capable of interacting in many languages to a fairly high degree of accuracy.

The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.

Additionally, pre-training data has been included for the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian.

The model has been trained to respond in the language of the user. Here's an example:

*Prompt*

```Text
Écris une description de produit pour une voiture électrique en 50 à 75 mots
```

*Generation*

```text TEXT
Découvrez la voiture électrique qui va révolutionner votre façon de conduire.
Avec son design élégant, cette voiture offre une expérience de conduite unique
avec une accélération puissante et une autonomie impressionnante. Sa
technologie avancée vous garantit une charge rapide et une fiabilité inégalée.
Avec sa conception innovante et durable, cette voiture est parfaite pour les 
trajets urbains et les longues distances. Profitez d'une conduite silencieuse
et vivez l'expérience de la voiture électrique!
```

Command R can not only be used to generate text in several languages but can also perform cross-lingual tasks such as translation or answering questions about content in other languages.

### Retrieval Augmented Generation

Command R has been trained with the ability to ground its generations. This means that it can generate responses based on a list of supplied document snippets, and it will include citations in its response indicating the source of the information.

For more information, check out our dedicated guide on [retrieval augmented generation](/docs/retrieval-augmented-generation-rag).

### Tool Use

Command R has been trained with conversational tool use capabilities. This functionality takes a conversation as input (with an optional user-system preamble), along with a list of available tools. The model will then generate a json-formatted list of actions to execute on a subset of those tools. For more information, check out our dedicated [tool use](/docs/tool-use) guide.


# Cohere's Embed Models (Details and Application)

> Explore Embed models for text classification and embedding generation in English and multiple languages, with details on dimensions and endpoints.

Embed models can be used to generate embeddings from text or classify it based on various parameters. Embeddings can be used for estimating semantic similarity between two texts, choosing a sentence which is most likely to follow another sentence, or categorizing user feedback. When used with the Classify endpoint, embeddings can be used for any classification or analysis task.

| Latest Model                    | Description                                                                                                                                            | Modality                                     | Dimensions                                 | Max Tokens (Context Length) | Similarity Metric                                             | Endpoints                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------ | --------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------- |
| `embed-v4.0`                    | A model that allows for text and images to be classified or turned into embeddings                                                                     | Text, Images, Mixed texts/images (i.e. PDFs) | One of '\[256, 512, 1024, 1536 (default)]' | 128k                        | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed)                                             |
| `embed-english-v3.0`            | A model that allows for text to be classified or turned into embeddings. English only.                                                                 | Text, Images                                 | 1024                                       | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-english-light-v3.0`      | A smaller, faster version of `embed-english-v3.0`. Almost as capable, but a lot faster. English only.                                                  | Text, Images                                 | 384                                        | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-multilingual-v3.0`       | Provides multilingual classification and embedding support. [See supported languages here.](/docs/supported-languages)                                 | Text, Images                                 | 1024                                       | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed), [Embed Jobs](/reference/embed-jobs)        |
| `embed-multilingual-light-v3.0` | A smaller, faster version of `embed-multilingual-v3.0`. Almost as capable, but a lot faster. [Supports multiple languages.](/docs/supported-languages) | Text, Images                                 | 384                                        | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |

## List of Supported Languages

Our multilingual embed model supports over 100 languages, including Chinese, Spanish, and French.

| ISO Code | Language Name   |
| -------- | --------------- |
| af       | Afrikaans       |
| am       | Amharic         |
| ar       | Arabic          |
| as       | Assamese        |
| az       | Azerbaijani     |
| be       | Belarusian      |
| bg       | Bulgarian       |
| bn       | Bengali         |
| bo       | Tibetan         |
| bs       | Bosnian         |
| ca       | Catalan         |
| ceb      | Cebuano         |
| co       | Corsican        |
| cs       | Czech           |
| cy       | Welsh           |
| da       | Danish          |
| de       | German          |
| el       | Greek           |
| en       | English         |
| eo       | Esperanto       |
| es       | Spanish         |
| et       | Estonian        |
| eu       | Basque          |
| fa       | Persian         |
| fi       | Finnish         |
| fr       | French          |
| fy       | Frisian         |
| ga       | Irish           |
| gd       | Scots\_gaelic   |
| gl       | Galician        |
| gu       | Gujarati        |
| ha       | Hausa           |
| haw      | Hawaiian        |
| he       | Hebrew          |
| hi       | Hindi           |
| hmn      | Hmong           |
| hr       | Croatian        |
| ht       | Haitian\_creole |
| hu       | Hungarian       |
| hy       | Armenian        |
| id       | Indonesian      |
| ig       | Igbo            |
| is       | Icelandic       |
| it       | Italian         |
| ja       | Japanese        |
| jv       | Javanese        |
| ka       | Georgian        |
| kk       | Kazakh          |
| km       | Khmer           |
| kn       | Kannada         |
| ko       | Korean          |
| ku       | Kurdish         |
| ky       | Kyrgyz          |
| La       | Latin           |
| Lb       | Luxembourgish   |
| Lo       | Laothian        |
| Lt       | Lithuanian      |
| Lv       | Latvian         |
| mg       | Malagasy        |
| mi       | Maori           |
| mk       | Macedonian      |
| ml       | Malayalam       |
| mn       | Mongolian       |
| mr       | Marathi         |
| ms       | Malay           |
| mt       | Maltese         |
| my       | Burmese         |
| ne       | Nepali          |
| nl       | Dutch           |
| no       | Norwegian       |
| ny       | Nyanja          |
| or       | Oriya           |
| pa       | Punjabi         |
| pl       | Polish          |
| pt       | Portuguese      |
| ro       | Romanian        |
| ru       | Russian         |
| rw       | Kinyarwanda     |
| si       | Sinhalese       |
| sk       | Slovak          |
| sl       | Slovenian       |
| sm       | Samoan          |
| sn       | Shona           |
| so       | Somali          |
| sq       | Albanian        |
| sr       | Serbian         |
| st       | Sesotho         |
| su       | Sundanese       |
| sv       | Swedish         |
| sw       | Swahili         |
| ta       | Tamil           |
| te       | Telugu          |
| tg       | Tajik           |
| th       | Thai            |
| tk       | Turkmen         |
| tl       | Tagalog         |
| tr       | Turkish         |
| tt       | Tatar           |
| ug       | Uighur          |
| uk       | Ukrainian       |
| ur       | Urdu            |
| uz       | Uzbek           |
| vi       | Vietnamese      |
| wo       | Wolof           |
| xh       | Xhosa           |
| yi       | Yiddish         |
| yo       | Yoruba          |
| zh       | Chinese         |
| zu       | Zulu            |

## Frequently Asked Questions

### What is the Context Length for Cohere Embeddings Models?

You can find the context length for various Cohere embeddings models in the tables above. It's in the "Max Tokens (Context Length)" column.


# Cohere's Rerank Model (Details and Application)

> This page describes how Cohere's Rerank models work and how to use them.

Rerank models sort text inputs by semantic relevance to a specified query. They are often used to sort search results  returned from an existing search solution. Learn more about using Rerank in the [best practices guide](/docs/reranking-best-practices).

| Latest Model               | Description                                                                                                                                                                                                                      | Modality | Endpoints                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------- |
| `rerank-v3.5`              | A model for documents and semi-structured data (JSON). State-of-the-art performance in English and non-English languages; supports the same languages as embed-multilingual-v3.0. This model has a context length of 4096 tokens | Text     | [Rerank](/reference/rerank) |
| `rerank-english-v3.0`      | A model that allows for re-ranking English Language documents and semi-structured data (JSON). This model has a context length of 4096 tokens.                                                                                   | Text     | [Rerank](/reference/rerank) |
| `rerank-multilingual-v3.0` | A model for documents and semi-structure data (JSON) that are not in English. Supports the same languages as `embed-multilingual-v3.0`. This model has a context length of 4096 tokens.                                          | Text     | [Rerank](/reference/rerank) |

<Note>
  For each document included in a request, Rerank combines the tokens from the query with the tokens from the document and the combined total counts toward the context limit for a single document. If the combined number of tokens from the query and a given document exceeds the model’s context length for a single document, the document will automatically get chunked and processed in multiple inferences. See our [best practice guide](/docs/reranking-best-practices) for more info about formatting documents for the Rerank endpoint.
</Note>


# Aya Family of Models

> Understand Cohere Labs groundbreaking multilingual Aya models, which aim to bring many more languages into generative AI.

[Aya](https://cohere.com/research/aya) is a family of multilingual large language models that are designed to expand the number of languages covered by generative AI. The two documents in this section cover the two primary Aya offerings:

* [Aya Vision](https://docs.cohere.com/docs/aya-multimodal), a powerful multi-modal model;
* [Aya Expanse](/docs/aya-expanse), a highly performant multilingual model able to work with 23 languages.

Check them out for far more detail.

## Find More

If you want to see more substantial projects you can check out these notebooks ([source](https://huggingface.co/CohereForAI/aya-expanse-32b)):

* [Multilingual Writing Assistant](https://colab.research.google.com/drive/1SRLWQ0HdYN_NbRMVVUHTDXb-LSMZWF60)
* [AyaMCooking](https://colab.research.google.com/drive/1-cnn4LXYoZ4ARBpnsjQM3sU7egOL_fLB?usp=sharing)
* [Multilingual Question-Answering System](https://colab.research.google.com/drive/1bbB8hzyzCJbfMVjsZPeh4yNEALJFGNQy?usp=sharing)


# Aya Vision

> Understand Cohere Labs groundbreaking multilingual model Aya Vision, a state-of-the-art multimodal language model excelling at multiple tasks.

Aya Vision is a state-of-the-art multimodal and massively multilingual large language model excelling at critical benchmarks for language, text, and image capabilities. A natural extension of the Aya Expanse model family, Aya Vision provides deep capability in 23 languages, helping eliminate technological and communication divides between people and geographies.

Built as a foundation for multilingual and multimodal communication, Aya Vision supports tasks such as image captioning, visual question answering, text generation, and translations from both texts and images into coherent text.

## Model Details

| Model Name            | Description                                                                                                                                                                                                                                             | Modality     | Context Length | Maximum Output Tokens | Endpoints               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | --------------------- | ----------------------- |
| `c4ai-aya-vision-8b`  | Aya Vision is a state-of-the-art multimodal model excelling at a variety of critical benchmarks for language, text, and image capabilities. This 8 billion parameter variant is focused on low latency and best-in-class performance.                   | Text, Images | 16k            | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-vision-32b` | Aya Vision is a state-of-the-art multimodal model excelling at a variety of critical benchmarks for language, text, and image capabilities. Serves 23 languages. This 32 billion parameter variant is focused on state-of-art multilingual performance. | Text, Images | 16k            | 4k                    | [Chat](/reference/chat) |

## Multimodal Capabilities

Aya Vision’s multimodal capabilities enable it to understand content across different media types, including text and images as input. Purpose-built to unify cultures, geographies, and people, Aya Vision is optimized for elite performance in 23 different languages. Its image captioning capabilities allow it to generate descriptive captions for images, and interpret images dynamically to answer various questions about images. Likewise, Aya Vision allows question answering, and translation across these materials, whether written or image based, laying a foundation to bridge communication and collaboration divides.

Like [Aya Expanse](https://docs.cohere.com/docs/aya), Aya Vision is highly proficient in 23 languages, making it a valuable tool for researchers, academics, and developers working on multilingual projects.

## How Can I Get Access to the Aya Models?

If you want to test Aya, you have three options. First (and simplest), you can use the [Cohere playground](https://dashboard.cohere.com/playground/chat) or [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/aya_expanse) to play around with them and see what they’re capable of.

Second, you can use the [Cohere Chat API](https://docs.cohere.com/v2/docs/chat-api) to work with Aya programmatically. Here’s a very lightweight example of using the Cohere SDK to get Aya Vision to describe the contents of an image; if you haven’t installed the Cohere SDK, you can do that with `pip install cohere`.

```python PYTHON
import cohere
import base64
import os


def generate_text(image_path, message):

    model = "c4ai-aya-vision-8b"

    co = cohere.ClientV2("<YOUR_API_KEY>")

    with open(image_path, "rb") as img_file:
        base64_image_url = f"data:image/jpeg;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"

    response = co.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": message},
                    {
                        "type": "image_url",
                        "image_url": {"url": base64_image_url},
                    },
                ],
            }
        ],
        temperature=0.3,
    )

    print(response.message.content[0].text)
```

Here's an image we might feed to Aya Vision:
![A guitar-focused room](file:dd6335bc-6df3-4e61-bac4-8de24be66d8a)

And here’s an example output we might get when we run `generate_text(image_path, "What items are in the wall of this room?")`

(remember: these models are stochastic, and what you see might look quite different).

```
The wall in this room showcases a collection of musical instruments and related items, creating a unique and personalized atmosphere. Here's a breakdown of the items featured:

1. **Guitar Wall Mount**: The centerpiece of the wall is a collection of guitars mounted on a wall. There are three main guitars visible:
   - A blue electric guitar with a distinctive design.
   - An acoustic guitar with a turquoise color and a unique shape.
   - A red electric guitar with a sleek design.

2. **Ukulele Display**: Above the guitars, there is a display featuring a ukulele and its case. The ukulele has a traditional wooden body and a colorful design.

3. **Artwork and Posters**:
   - A framed poster or artwork depicting a scene from *The Matrix*, featuring the iconic green pill and red pill.
   - A framed picture or album artwork of *Fleetwood Mac McDonald*, including *Rumours*, *Tusk*, and *Dreams*.
   - A framed image of the *Dark Side of the Moon* album cover by Pink Floyd.
   - A framed poster or artwork of *Star Wars* featuring *R2-D2* (Robotic Man).

4. **Album Collection**: Along the floor, there is a collection of vinyl records or album artwork displayed on a carpeted area. Some notable albums include:
   - *Dark Side of the Moon* by Pink Floyd.
   - *The Beatles* (White Album).
   - *Abbey Road* by The Beatles.
   - *Nevermind* by Nirvana.

5. **Lighting and Accessories**:
   - A blue lamp with a distinctive design, possibly serving as a floor lamp.
   - A small table lamp with a warm-toned shade.
```

Finally, you can directly download the raw models for research purposes because Cohere Labs has released Aya Vision as open-weight models, through HuggingFace. We also released a new valuable evaluation set -- [Aya Vision Benchmark](https://huggingface.co/datasets/CohereForAI/AyaVisionBench) -- to measure progress on multilingual models here.

### Aya Expanse Integration with WhatsApp.

On our [Aya Expanse](https://docs.cohere.com/docs/aya) page, you can find more information about Aya models in general, including a detailed FAQ section on how to use it with WhatsApp. There, we walk through using Aya Vision with WhatsApp.

## Find More

We hope you’re as excited about the possibilities of Aya Vision as we are! If you want to see more substantial projects, you can check out these notebooks:

* [Walkthrough and Use Cases](https://docs.cohere.com/page/aya-vision-intro)


# Aya Expanse

> Understand Cohere Labs highly performant multilingual Aya models, which aim to bring many more languages into generative AI.

Aya Expanse is a massively multilingual large language model excelling in enterprise-scale tasks. Its 8-billion and 32-billion parameter offerings are optimized to perform well in these 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.

Built for scalability, reliability, customizability, and deep contextual understanding, Aya Expanse powers text generation, summarization, translation, and more.

Aya Expanse is ideal for:

* Customer support
* Content creation
* Global communication
* Data analysis

## Model Details

| Model Name             | Description                                                                                                                                                                                                                      | Modality | Context Length | Maximum Output Tokens | Endpoints               |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------- | --------------------- | ----------------------- |
| `c4ai-aya-expanse-8b`  | Aya Expanse is a highly performant 8B multilingual model, designed to rival monolingual performance through innovations in instruction tuning with data arbitrage, preference training, and model merging. Serves 23 languages.  | Text     | 8k             | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-expanse-32b` | Aya Expanse is a highly performant 32B multilingual model, designed to rival monolingual performance through innovations in instruction tuning with data arbitrage, preference training, and model merging. Serves 23 languages. | Text     | 128k           | 4k                    | [Chat](/reference/chat) |

## How Can I Get Access to the Aya Models?

If you want to test Aya, you have three options. First (and simplest), you can use the [Cohere playground](https://dashboard.cohere.com/playground/chat) or [Hugging Face Space](https://huggingface.co/spaces/CohereForAI/aya_expanse) to play around with them and see what they’re capable of.

Second, you can use the [Cohere Chat API](https://docs.cohere.com/v2/docs/chat-api) to work with Aya programmatically. Here’s a very lightweight example of using the Cohere SDK to create a Spanish-language tutor with Aya that tells a story with simple Spanish vocabulary (NOTE: you’ll need an API key to run this code, and if you haven’t installed the Cohere SDK you can do that with `pip install cohere`).

```python PYTHON
import cohere

co = cohere.ClientV2("<YOUR_API_KEY>")

response = co.chat(
    model="c4ai-aya-expanse-32b",
    messages=[
        {
            "role": "user",
            "content": "Eres un gran profesor de español. ¿Puedes escribirme una historia que ilustre vocabulario sencillo en español?",
        }
    ],
)

print(response.message.content[0].text)
```

And here’s an example output (remember: these models are stochastic, and what you see might look quite different).

```
¡Claro! Aquí te presento una historia corta que utiliza vocabulario sencillo en español:

**La aventura de María en el mercado**

Era una mañana soleada y María, una joven curiosa, decidió explorar el mercado local de su pueblo. Al entrar, se encontró con un mundo lleno de colores y aromas fascinantes.

En uno de los puestos, vio una montaña de frutas brillantes. Había manzanas rojas como la grana, naranjas naranjas como el atardecer, y plátanos amarillos como el sol. María eligió una manzana crujiente y le pidió al vendedor que le enseñara cómo pelar una naranja.

Caminando por los pasillos, se topó con una señora que vendía flores. Las rosas rojas olían a dulce miel, y los claveles blancos parecían pequeñas nubes. María compró un ramo de margaritas para decorar su habitación.

Más adelante, un señor amable ofrecía quesos de diferentes sabores. María probó un queso suave y cremoso que le encantó. También compró un poco de pan fresco para acompañarlo.

En la sección de artesanías, encontró un artista que tallaba hermosos platos de madera. María admiró su trabajo y aprendió la palabra "tallar", que significaba dar forma a la madera con cuidado.

Al final de su aventura, María se sintió feliz y orgullosa de haber descubierto tantas cosas nuevas. Había aprendido vocabulario relacionado con los colores, los sabores, las texturas y las artes. El mercado se había convertido en un lugar mágico donde la simplicidad de las palabras se unía a la riqueza de las experiencias.

Espero que esta historia te sea útil para ilustrar vocabulario sencillo en español. ¡Puedes adaptar y expandir la trama según tus necesidades!
```

Finally, you can directly download the raw models for research purposes because Cohere Labs has released [Aya Expanse 8B](https://huggingface.co/CohereForAI/aya-expanse-8b) and [Aya Expanse 32B](https://huggingface.co/CohereForAI/aya-expanse-32b) as open-weight models, through HuggingFace. What’s more, the massively multilingual instruction data used for development of these models has been [made available](https://huggingface.co/datasets/CohereForAI/aya_collection) for download as well.

### Aya Expanse Integration with WhatsApp

In addition to the above, you also have the option of talking to Aya Expanse through the popular messaging service WhatsApp. Below, we'll answer some questions about this process.

<Note>
  By communicating with Aya Expanse through WhatsApp, you agree to Cohere's Terms of Use and Privacy Policy. Large Language Models might hallucinate, so be sure to verify important information.
</Note>

#### How do I Talk to Aya with WhatsApp?

Use [this link](https://wa.me/14313028498) to open a WhatsApp chatbox with Aya Expanse. If you don't have WhatsApp downloaded on your machine you might need to do that, or, if you have it on your phone, you can follow the on-screen instructions to link your phone and WhatsApp Web. By the end, you should see a text window that looks something like this, which you can use to chat with the model:

<img src="file:1ccf44ad-bfc9-4c3e-bcae-d9e6b7127f32" />

#### Will I Get Charged for Talking to Aya?

Aya Expanse is free to use on WhatsApp. You will not be charged for any usage and are not limited in the number of interactions you can have with the model.

#### Are There Certain Aya Capabilities that Aren't Available Through WhatsApp?

Aya Expanse is a multilingual language model capable of conversing in 23 languages. However, [retrieval-augemented generation](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) RAG and [tool-use](https://docs.cohere.com/docs/tools) are not available in WhatsApp, for that you should instead use the [Cohere chat endpoint](https://docs.cohere.com/reference/chat).

### Are There Special Commands I Should Keep in Mind while Chatting with Aya Expanse via Whatsapp?

Yes, you can send the “/clear” command to the model via WhatsApp to clear the context of your previous chat with the model and start a fresh conversation with Aya Expanse.

#### How do I Know It's Really Aya Expanse I'm Talking to?

If you follow the link provided above and see the "Aya Expanse by Cohere Labs" banner at the top, it's Aya.

#### What Should I do if the Model Becomes Unresponsive?

Aya Expanse should be accessible via Whatsapp at all times. Sometimes, a simple app refresh can resolve any temporary glitches. If the problem persists, we encourage you to report the issue on the [Cohere Discord server](https://discord.com/invite/co-mmunity).

#### Can I Use Aya Vision with WhatsApp?

Yes! To use Aya Vision with WhatsApp, follow exactly the same procedure outlined above. When you've made it into WhatsApp, you can simply upload an image and include your question in the `caption` field (you can also upload the image and ask a question afterwards).

Here's what that looks like:

![Uploading an Aya Vision image to WhatsApp](file:7f3150d5-e103-4470-baea-2b79a6c939f0)

And here's a sample output:

![Aya Vision output](file:1fc7c584-e69d-40ef-a273-e25be58ab303)

We have a dedicated document for Aya Vision, which you can find [here](/docs/aya-multimodal).

## Find More

We hope you’ve found this as fascinating as we do! If you want to see more substantial projects you can check out these notebooks ([source](https://huggingface.co/CohereForAI/aya-expanse-32b)):

* [Multilingual Writing Assistant](https://colab.research.google.com/drive/1SRLWQ0HdYN_NbRMVVUHTDXb-LSMZWF60)
* [AyaMCooking](https://colab.research.google.com/drive/1-cnn4LXYoZ4ARBpnsjQM3sU7egOL_fLB?usp=sharing)
* [Multilingual Question-Answering System](https://colab.research.google.com/drive/1bbB8hzyzCJbfMVjsZPeh4yNEALJFGNQy?usp=sharing)


# Introduction to Text Generation at Cohere

> This page describes how a large language model generates textual output.

Large language models are impressive for many reasons, but among the most prominent is their ability to quickly generate text. With just a little bit of prompting, they can crank out conceptual explanations, blog posts, web copy, poetry, and almost anything else. Their style can be tweaked to be suitable for children and adults, technical people and laymen, and they can be asked to work in dozens of different natural languages.

In this article, we'll cover some of the basics of what makes this functionality possible. If you'd like to skip straight to a more hands-on treatment, check out "[Using the Chat API](/docs/chat-api)."

## How are Large Language Models Trained?

Eliding a great deal of technical complexity, a large language model is just a neural network trained to predict the [next token](/docs/tokens-and-tokenizers#what-is-a-token), given the tokens that have come before. Take a sentence like "Hang on, I need to go inside and grab my \_\_\_." As a human being with a great deal of experience using natural language, you can make some reasonable guesses about which token will complete this sentence even with no additional context:

* "Hang on, I need to go inside and grab my **bag**."
* "Hang on, I need to go inside and grab my **keys**."
* Etc.

Of course, there are other possibilities that are plausible, but less likely:

* "Hang on, I need to go inside and grab my **friend**."
* "Hang on, I need to go inside and grab my **book**."

And, there's a long-tail of possibilities that are technically grammatically correct but which effectively never occur in a real exchange:

* "Hang on, I need to go inside and grab my **giraffe**."

*You* have an intuitive sense of how a sentence like this will end because you've been using language all your life. A model like Command R+ must learn how to perform the same feat by seeing billions of token sequences and figuring out a statistical distribution over them that allows it to predict what comes next.

Once it's done so, it can take a prompt like "Help me generate some titles for a blog post about quantum computing," and use the distribution it has learned to generate the series of tokens it *thinks* would follow such a request. Since it's an *AI* system *generating* tokens, it's known as "generative AI," and with models as powerful as Cohere's, the results are often surprisingly good.

## Learn More

The rest of the "Text Generation" section of our documentation walks you through how to work with Cohere's models. Check out ["Using the Chat API"](/docs/chat-api) to get set up and understand what a response looks like, or reading the [streaming guide](/docs/streaming) to figure out how to integrate generative AI into streaming applications.

You might also benefit from reading the [retrieval-augmented generation](/docs/retrieval-augmented-generation-rag), [tool-use](/docs/tool-use), and [agent-building](/docs/multi-step-tool-use) guides.


# Using the Cohere Chat API for Text Generation

> How to use the Chat API endpoint with Cohere LLMs to generate text responses in a conversational interface

The Chat API endpoint is used to generate text with Cohere LLMs. This endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses.

Every message comes with a `content` field and an associated `role`, which indicates who that message is sent from. Roles can be `user`, `assistant`, `system` and `tool`.

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Write a title for a blog post about API design. Only output the title text.",
          }
      ],
  )

  print(res.message.content[0].text)
  # "The Ultimate Guide to API Design: Best Practices for Building Robust and Scalable APIs"
  ```

  ```java JAVA
  package chatv2post;

  import com.cohere.api.Cohere;
  import com.cohere.api.resources.v2.requests.V2ChatRequest;
  import com.cohere.api.types.*;
  import java.util.List;

  public class Default {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().token("<<apiKey>>").clientName("snippet").build();

          ChatResponse response =
                  cohere.v2()
                          .chat(
                                  V2ChatRequest.builder()
                                      .model("command-a-03-2025")
                                      .messages(
                                          List.of(
                                              ChatMessageV2.user(
                                                  UserMessage.builder()
                                                      .content(
                                                          UserMessageContent
                                                                  .of("Hello world!"))
                                                      .build())))
                                      .build());

          System.out.println(response);
      }
  }

  ```

  ```typescript TYPESCRIPT
  const { CohereClientV2 } = require('cohere-ai');

  const cohere = new CohereClientV2({
    token: '<<apiKey>>',
  });

  (async () => {
    const response = await cohere.chat({
      model: 'command-a-03-2025',
      messages: [
        {
          role: 'user',
          content: 'hello world!',
        },
      ],
    });

    console.log(response);
  })();

  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Write a title for a blog post about API design. Only output the title text."
        }
      ]
    }'
  ```
</CodeBlocks>

## Response Structure

Below is a sample response from the Chat API. Here, the `role` of the `message` is going to be `assistant`.

```json JSON
{
    "id": "5a50480a-cf52-46f0-af01-53d18539bd31",
    "message": {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "The Art of API Design: Crafting Elegant and Powerful Interfaces",
            }
        ],
    },
    "finish_reason": "COMPLETE",
    "meta": {
        "api_version": {"version": "2", "is_experimental": True},
        "warnings": [
            "You are using an experimental version, for more information please refer to https://docs.cohere.com/versioning-reference"
        ],
        "billed_units": {"input_tokens": 17, "output_tokens": 12},
        "tokens": {"input_tokens": 215, "output_tokens": 12},
    },
}
```

Every response contains the following fields:

* `message` the generated message from the model.
* `id` the ID corresponding to this response.
* `finish_reason` can be one of the following:
  * `COMPLETE` the model successfully finished generating the message
  * `MAX_TOKENS` the model's context limit was reached before the generation could be completed
* `meta` contains information with token counts, billing etc.

## System Message

Developers can adjust the LLMs behavior by including a system message in the `messages` list
with the role set to `system`.

The system message contains instructions that the model will respect over any instructions sent in messages sent from other roles. It is often used by developers to control the style in which the model communicates and to provide guidelines for how to handle various topics.

It is recommended to send the system message as the first element in the messages list.

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  system_message = "You respond concisely, in about 5 words or less"

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {"role": "system", "content": system_message},
          {
              "role": "user",
              "content": "Write a title for a blog post about API design. Only output the title text.",
          },
      ],  # "Designing Perfect APIs"
  )

  print(res.message.content[0].text)
  ```

  ```bash Curl
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "system",
          "content": "You respond concisely, in about 5 words or less"
        },
        {
          "role": "user",
          "content": "Write a title for a blog post about API design. Only output the title text."
        }
      ]
    }'
  ```
</CodeBlocks>

## Multi-Turn Conversations

A single Chat request can encapsulate multiple turns of a conversation, where each message in the `messages` list appears in the order it was sent. Sending multiple messages can give the model context for generating a response.

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  system_message = "You respond concisely, in about 5 words or less"

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {"role": "system", "content": system_message},
          {
              "role": "user",
              "content": "Write a title for a blog post about API design. Only output the title text.",
          },
          {"role": "assistant", "content": "Designing Perfect APIs"},
          {
              "role": "user",
              "content": "Another one about generative AI.",
          },
      ],
  )

  # "AI: The Generative Age"
  print(res.message.content[0].text)
  ```

  ```bash Curl
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "system",
          "content": "You respond concisely, in about 5 words or less"
        },
        {
          "role": "user",
          "content": "Write a title for a blog post about API design. Only output the title text."
        },
        {
          "role": "assistant",
          "content": "Designing Perfect APIs"
        },
        {
          "role": "user",
          "content": "Another one about generative AI."
        }
      ]
    }'
  ```
</CodeBlocks>


# Reasoning Capabilities

> Reasoning models excel at tool use, agentic workflows, and complex problem-solving. This page provides a general overview of Cohere's reasoning capalities.

Reasoning models represent an advanced approach to AI that enables more sophisticated problem-solving capabilities. Cohere's reasoning models are *hybrid*, meaning reasoning can be enabled (in which case they generate internal reasoning processes before delivering their final responses) or disabled (in which case they function the way any other LLM would).

### How Reasoning Models Work

When a reasoning model processes a request, it first works internally to break the problem down step-by-step. This reasoning process happens in dedicated "thinking" content blocks where the model works through its analysis, planning, and logical steps. Only after completing this internal reasoning does the model produce its final text response, and this allows them to tackle complex tasks with deeper analysis.

The key benefit is that reasoning models can handle complex problems—such as leveraging tools and agentic problem solving in the 23 supported languages—by first working through the problem internally before presenting a well-reasoned solution. This approach leads to more accurate and thorough responses, while pushing the boundary for the complexity of problems the model is able to solve.

### Getting Started

Models with Reasoning capabilities are accessible via the Chat API. Here's an example:

<CodeBlocks>
  ```python PYTHON 
  from cohere import ClientV2

  co = ClientV2(api_key="<YOUR_API_KEY>")

  prompt = """
  Alice has 3 brothers and she also has 2 sisters. How many sisters does Alice's brother have?
  """

  response = co.chat(
      model="command-a-reasoning-08-2025",
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
  )

  for content in response.message.content:
  	if content.type == "thinking":
  		print("Thinking:", content.thinking)

  	if content.type == "text":
  		print("Response:", content.text)
  ```

  ```python PYTHON (Streaming) 
  from cohere import ClientV2

  co = ClientV2(api_key="<YOUR_API_KEY>")        


  prompt = """
  Alice has 3 brothers and she also has 2 sisters. How many sisters does Alice's brother have?
  """

  response = co.chat_stream(
      model="command-a-reasoning-08-2025",
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
  )
  for event in response:
      if event.type == "content-delta":
          if event.delta.message.content.thinking:
              print(event.delta.message.content.thinking, end="")
          if event.delta.message.content.text:
              print(event.delta.message.content.text, end="")
  ```

  ```bash Curl
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-reasoning-08-2025",
      "messages": [
        {
          "role": "user",
          "content": "Alice has 3 brothers and she also has 2 sisters. How many sisters does Alice'\''s brother have?"
        }
      ]
    }'
  ```
</CodeBlocks>

#### Enabling / Disabling Reasoning Capabilities

For reasoning models, `thinking` is enabled by default. To disable it, send the following value to the `"thinking"` parameter:

```python PYTHON 
thinking={ 
    "type": "disabled" # turns off thinking. It is set to "enabled" by default.
}
```

#### Thinking Budgets

A thinking token budget can also be specified, to set an upper limit on how many thinking tokens the model can produce. Our recommendation is to use unlimited thinking (i.e. `reasoning = on`). However, if you plan to use thinking budgets, please make sure to leave at least 1K tokens for the response. For example, if you want the model to reason until the maximum limit, we recommend 31K as the token budget.

When the budget is exceeded, the model will immediately proceed with the final response.

```python PYTHON
thinking = {
    "token_budget": 500  # limits the model's thinking output to at most 500 tokens
}
```

### Use Cases and Applications

Reasoning models excel at tasks that benefit from step-by-step analysis, including:

* **Agentic Use Cases**: Taking autonomous actions and interacting with the environment to solve problems.
* **Tool Use**: Able to leverage a variety of tools, such as search engines and APIs.
* **Multilingual**: Able to reason over multilingual inputs, providing support to user queries in 23 different languages.

### Technical Implementation

The reasoning process is controlled through specific parameters that allow developers to:

* Enable or disable reasoning capabilities
* Set token budgets to control the depth of reasoning
* Stream responses to see reasoning and final answers in real-time

This architecture makes reasoning models particularly valuable for applications requiring high accuracy, transparency in reasoning, and the ability to handle complex, multi-faceted problems that benefit from systematic analysis.


# Using Cohere's Models to Work with Image Inputs

> This page describes how a Cohere large language model works with image inputs. It covers passing images with the API, limitations, and best practices.

## Introduction

Models with vision capabilities can understand and interpret image data, map relationships between text and visual inputs, and handle many other tasks where a mix of images and text is involved.

Cohere has models capable of interacting with images, and they excel in enterprise use cases such as:

* Analysis of charts, graphs, and diagrams;
* Extracting and understanding in-image tables;
* Document optical character recognition (OCR) and question answering;
* Natural-language image processing, including translation of text found in images.

For more detailed breakdowns of these and other applications, check out [our cookbooks](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/guides/vision).

These models are designed to work through an interface and API structure that looks almost exactly like all of our other Command models, making it easy to get started with our image-processing functionality. Take this image, for example, which contains a graph of earnings for various waste management companies:

![](file:2c21b1a8-b4cf-4665-a006-49611d6e1468)

We can have Command A Vision analyze this image for us with the following:

<CodeBlocks>
  ```python PYTHON 
  response = co.chat(
      model="command-a-vision-07-2025",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "Please create two markdown tables. One for Revenue. One for CAGR. the company names should be in alphabetical order in both."},
                  {"type": "image_url", "image_url": {"url": base64_url}},
              ],
          }
      ],
  )
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-vision-07-2025",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "Please create two markdown tables. One for Revenue. One for CAGR. the company names should be in alphabetical order in both."
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "data:image/png;base64,..."
              }
            }
          ]
        }
      ]
    }'
  ```
</CodeBlocks>

And you should get something like this:

![](file:184e07eb-b941-4c39-a4fe-be587e48a1e1)

The rest of this document fleshes out Cohere's models work with image inputs, including information on limitations, token calculations, and more.

<Warning>
  Cohere's Vision capabilities are not currently offered on the North platform.
</Warning>

## Image Detail

The Chat API allows users to control the level of image `“detail”` sent to the model, which can be one of `“low”`, `“high”`, or `“auto”` (the default).

Lower detail helps reduce the overall token count (and therefore price and latency), but may result in poorer performance. We recommend trying both levels of detail to identify whether the performance is sufficient at `"low"`.

The `detail` property is specified for each image, here's what that look like:

<CodeBlocks>
  ```python PYTHON 
  co.chat(
    model="command-a-vision-07-2025",
    messages=[
  	{ "role": "user", "content": [
              {"type": "text",
                "text": "what's in this image?"
                },
              {"type": "image_url",
              "image_url": {
                "url": "https://cohere.com/favicon-32x32.png",
                "detail": "high" # Here's where we're setting the detail.
            }
          },
        ]
      }
    ]
  )
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-vision-07-2025",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "what'\''s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://cohere.com/favicon-32x32.png",
                "detail": "high"
              }
            }
          ]
        }
      ]
    }'
  ```
</CodeBlocks>

When detail is set to “low”:

* If the image area is larger than 512px \* 512px, it will be resized to fit into these dimensions while attempting to maintain the aspect ratio.
* Each “low” detail image takes up 256 tokens that count towards the model’s context length.

When detail is set to “high”:

* If the image area is larger than 1536px \* 2048px it will be resized to fit into these dimensions while attempting to maintain the aspect ratio, so that it can be cached.
* Under the hood, the API will divide the image into one or more tiles of 512x512 pixels, plus one additional 512x512 pixel *preview* tile; each of these tiles takes up 256 tokens that count towards the model’s context length.

When detail is unspecified or is set to “auto”:

* If any of the image sides are larger than 768px then `high` detail will be used, otherwise detail will be set to `low`.

Here's an example calculation of how an image is processed into tokens:

* Suppose a user provides a 10,000px \* 20,000px image.
* This image would be resized down to 1024px \* 2048px (since the longest side has to be at most 2048 pixels long), which fits into eight tiles of 512x512.
* What ultimately gets sent to the model is one 512px \* 512px preview thumbnail in addition to eight tiles of 512px \* 512px. Since the thumbnail is 256 tokens, and each of the eight tiles is 256 tokens, that means the image will take up 9 x 256 = 2304 tokens.

## Passing in an Image

### Image URL Formats

Cohere supports images in two formats, base64 *data* URLs and HTTP *image* URLs.

A base64 data URL (e.g., `"data:image/png;base64,..."`) has the advantage of being usable in deployments that don't have access to the internet. Here's what that looks like:

<CodeBlocks>
  ```python PYTHON
  co.chat(
      model="command-a-vision-07-2025",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "what's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {"url": "data:image..."},
                  },
              ],
          }
      ],
  )
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-vision-07-2025",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "what'\''s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "data:image/png;base64,..."
              }
            }
          ]
        }
      ]
    }'
  ```
</CodeBlocks>

An HTTP image URL (e.g., "[https://cohere.com/favicon-32x32.png](https://cohere.com/favicon-32x32.png)") is faster, but requires you to upload your image somewhere and is not available in outside platforms (Azure, Bedrock, etc.) HTTP image URLs make the API easy to try out, as data URLs are long and difficult to deal with. Moreover, including long data URLs in the request increases the request size and the corresponding network latency.

Here's what that looks like:

<CodeBlocks>
  ```python PYTHON
  co.chat(
      model="command-a-vision-07-2025",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "what's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://cohere.com/favicon-32x32.png"
                      },
                  },
              ],
          }
      ],
  )
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-vision-07-2025",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "what'\''s in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://cohere.com/favicon-32x32.png"
              }
            }
          ]
        }
      ]
    }'
  ```
</CodeBlocks>

For use cases like chatbots, where the images accumulate in the chat history, we recommend you use HTTP/HTTPs image URLs, since the request size will be smaller, and, with server-side caching, will result in faster response times.

## Limitations

### Image Counts

The Cohere API has the following limitations with respect to image counts:

* You can pass in a maximum of 20 images per request, or 20 megabytes (mb) in total data, whichever comes first.

### File types

These are the supported file types:

* PNG (`.png`)
* JPEG (`.jpeg` and `.jpg`)
* WEBP (`.webp`)
* Non-animated GIF (`.gif`)

### Non-Latin Alphabets

Performance may vary when processing images containing text in non-Latin scripts, like Japanese or Korean characters.

### Text Size

To enhance accuracy, consider enlarging small text in images while ensuring no crucial visual information is lost. If you're expecting small text in images, set `detail='high'`.

A good rule of thumb is: 'if you have trouble reading image in a text, then the model will too.'

### Rate Limits

Image inputs don't change rate limit considerations; for more detail, check out our dedicated [rate limit documentation](https://docs.cohere.com/docs/rate-limits).

### Understanding Costs

To understand how to calculate costs for a model, consult the breakdown above about how *tokens* are determined by the model, then consult our dedicated [pricing page](https://cohere.com/pricing?_gl=1*9o1g49*_gcl_au*MTE3MTc3OTk1OC4xNzUwMjQ1NzE0*_ga*MTAxNTg1NTM1MS4xNjk1MjMwODQw*_ga_CRGS116RZS*czE3NTEyOTcxMDQkbzMyMyRnMSR0MTc1MTI5NzExMiRqNTIkbDAkaDA.) to figure out what your ultimate spend will be.

### Acceptable Use

Please refer to our [usage policy](https://docs.cohere.com/docs/usage-policy).

## Prompt Engineering for Image Models

Prompting for text-generation and models that can work with images is very similar. If you're having success with a prompt in one of Cohere's standard language models, it should work for our image models as well.

## Best Practices

### Resizing Large Images

If you’re working with images that are larger than the model can handle, consider resizing them yourself, as this will have positive impacts on latency, cost, and performance.

### Structured Outputs and JSON Mode

Many use cases (such as OCR) work best with Cohere's structured output capabilities. To learn more about this, consult the [structured output guide](https://docs.cohere.com/v2/docs/structured-outputs).

### Getting the best Results out of the Model

Here are some techniques for optimizing model outputs:

* Apply prompt techniques that work well for text-based interactions.
* Reduce network latency by shrinking large images on the client before sending them via the API.
* Enlarge small text in images to improve readability and model performance.


# A Guide to Streaming Responses

> The document explains how the Chat API can stream events like text generation in real-time.

The [Chat API](/reference/chat) is capable of streaming events (such as text generation) as they come. This means that partial results from the model can be displayed within moments, even if the full generation takes longer.

You're likely already familiar with streaming. When you ask the model a question using [the Cohere playground](https://dashboard.cohere.com/playground), the interface doesn't output a single block of text, instead it *streams* the text out a few words at a time. In many user interfaces enabling streaming improves the user experience by lowering the perceived latency.

## Stream Events

When streaming is enabled, the API sends events down one by one. Each event has a `type`. Events of different types need to be handled correctly.

The following is an example of printing the `content-delta` event type from a streamed response, which contains the text contents of an LLM's response.

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  res = co.chat_stream(
      model="command-a-03-2025",
      messages=[{"role": "user", "content": "What is an LLM?"}],
  )

  for event in res:
      if event:
          if event.type == "content-delta":
              print(event.delta.message.content.text, end="")
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: text/event-stream' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "What is an LLM?"
        }
      ],
      "stream": true
    }'
  ```
</CodeBlocks>

```
# Sample output (streamed)

A large language model (LLM) is a type of artificial neural network model that has been trained on massive amounts of text data ...

```

The following sections describe the different types of events that are emitted during a streaming session.

### Basic Chat Stream Events

#### message-start

The first event in the stream containing metadata for the request such as the `id`. Only one `message-start` event will be emitted.

#### content-start

The event that indicates the start of the content block of the message. Only one `content-start` event will be emitted.

#### content-delta

The event that is emitted whenever the next chunk of text comes back from the model. As the model continues generating text, multiple events of this type will be emitted. Each event generates one token through the `delta.message.content.text` field.

```
# Sample events

type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text='A')))

type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' large')))

type='content-delta' index=0 delta=ChatContentDeltaEventDelta(message=ChatContentDeltaEventDeltaMessage(content=ChatContentDeltaEventDeltaMessageContent(text=' language')))

...

```

#### content-end

The event that indicates the end of the content block of the message. Only one `content-end` event will be emitted.

#### message-end

The final event in the stream indicating the end of the streamed response. Only one `message-end` event will be emitted.

### Retrieval Augmented Generation Stream Events

#### message-start

Same as in a basic chat stream event.

#### content-start

Same as in a basic chat stream event.

#### content-delta

Same as in a basic chat stream event.

#### citation-start

Emitted for every citation generated in the response.

```
# Sample event

type='citation-start' index=0 delta=CitationStartEventDelta(message=CitationStartEventDeltaMessage(citations=Citation(start=14, end=29, text='gym memberships', sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})])))
```

#### citation-end

Emitted to indicate the end of a citation. If there are multiple citations generated, the events will come as a sequence of `citation-start` and `citation-end` pairs.

#### content-end

Same as in a basic chat stream event.

#### message-end

Same as in a basic chat stream event.

### Tool Use Stream Events (For Tool Calling)

#### message-start

Same as in a basic chat stream event.

#### tool-plan-delta

Emitted when the next token of the tool plan is generated.

```
# Sample events

type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(tool_plan=None, message={'tool_plan': 'I'})

type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(tool_plan=None, message={'tool_plan': ' will'})

type='tool-plan-delta' delta=ChatToolPlanDeltaEventDelta(tool_plan=None, message={'tool_plan': ' use'})

...

```

#### tool-call-start

Emitted when the model generates tool calls that require actioning upon. The event contains a list of `tool_calls` containing the tool name and tool call ID of the tool.

```
# Sample event

type='tool-call-start' index=0 delta=ChatToolCallStartEventDelta(tool_call=None, message={'tool_calls': {'id': 'get_weather_nsz5zm3w56q3', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': ''}}})

```

#### tool-call-delta

Emitted when the next token of the the tool call is generated.

```
# Sample events

type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(tool_call=None, message={'tool_calls': {'function': {'arguments': '{\n    "'}}})

type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(tool_call=None, message={'tool_calls': {'function': {'arguments': 'location'}}})

type='tool-call-delta' index=0 delta=ChatToolCallDeltaEventDelta(tool_call=None, message={'tool_calls': {'function': {'arguments': '":'}}})

...
```

#### tool-call-end

Emitted when the tool call is finished.

#### message-end

Same as in a basic chat stream event.

### Tool Use Stream Events (For Response Generation)

#### message-start

Same as in a basic chat stream event.

#### content-start

Same as in a basic chat stream event.

#### content-delta

Same as in a basic chat stream event.

#### citation-start

Emitted for every citation generated in the response.

#### citation-end

Emitted to indicate the end of a citation. If there are multiple citations generated, the events will come as a sequence of `citation-start` and `citation-end` pairs.

#### content-end

Same as in a basic chat stream event.

#### message-end

Same as in a basic chat stream event.


# How do Structured Outputs Work?

> This page describes how to get Cohere models to create outputs in a certain format, such as JSON, TOOLS, using parameters such as `response_format`.

## Overview

Structured Outputs is a feature that forces the LLM’s response to strictly follow a schema specified by the user. When Structured Outputs is turned on, the LLM will generate structured data that follows the desired schema, provided by the user, 100% of the time. This increases the reliability of LLMs in enterprise applications where downstream applications expect the LLM output to be correctly formatted. With Structured Outputs, hallucinated fields and entries in structured data can be reliably eliminated.

Compatible models:

* Command A
* Command R+ 08 2024
* Command R+
* Command R 08 2024
* Command R

## How to Use Structured Outputs

There are two ways to use Structured Outputs:

* **Structured Outputs (JSON)**. This is primarily used in text generation use cases.
* **Structured Outputs (Tools)**. Structured Outputs (Tools). This is primarily used in [tool use (or function calling)](https://docs.cohere.com/docs/tool-use) and [agents](https://docs.cohere.com/docs/multi-step-tool-use) use cases.

<Note title="API Compatibility">
  Structured Outputs with Tools are only supported in [Chat API V2](https://docs.cohere.com/reference/chat#request.body.strict_tools) via the `strict_tools` parameter. This parameter is not supported in Chat API V1.
</Note>

### Structured Outputs (JSON)

Here, you can call the Chat API to generate Structured Outputs in JSON format. JSON is a lightweight format that is easy for humans to read and write and is also easy for machines to parse.

This is particularly useful in text generation use cases, for example, when you want to extract specific information from the responses, perform data analysis, or integrate the responses into your applications seamlessly.

There are two ways of specifying the JSON output:

* JSON mode
* JSON Schema mode

#### JSON mode

In JSON mode, when making an API request, you can specify the `response_format` parameter to indicate that you want the response in a JSON object format.

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Generate a JSON describing a person, with the fields 'name' and 'age'",
          }
      ],
      response_format={"type": "json_object"},
  )

  print(res.message.content[0].text)
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Generate a JSON describing a person, with the fields '\''name'\'' and '\''age'\''"
        }
      ],
      "response_format": {
        "type": "json_object"
      }
    }'
  ```
</CodeBlocks>

By setting the `response_format` type to `"json_object"` in the Chat API, the output of the model is guaranteed to be a valid JSON object.

```
# Example response

{
  "name": "Emma Johnson",
  "age": 32
}

```

<Info title="Important">
  When using  `{ "type": "json_object" }` your `message` should always explicitly instruct the model to generate a JSON (eg: *"Generate a JSON ..."*) . Otherwise the model may end up getting stuck generating an infinite stream of characters and eventually run out of context length.
</Info>

<Note title="Note">
  This feature is currently not supported in [RAG](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) mode.
</Note>

#### JSON Schema mode

In JSON Schema mode, you can optionally define a schema as part of the `response_format`  parameter. A [JSON Schema](https://json-schema.org/specification) is a way to describe the structure of the JSON object you want the LLM to generate.

This forces the LLM to stick to this schema, thus giving you greater control over the output.

For example, let's say you want the LLM to generate a JSON object with specific keys for a book, such as "title," "author," and "publication\_year." Your API request might look like this:

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Generate a JSON describing a book, with the fields 'title' and 'author' and 'publication_year'",
          }
      ],
      response_format={
          "type": "json_object",
          "schema": {
              "type": "object",
              "properties": {
                  "title": {"type": "string"},
                  "author": {"type": "string"},
                  "publication_year": {"type": "integer"},
              },
              "required": ["title", "author", "publication_year"],
          },
      },
  )

  print(res.message.content[0].text)
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Generate a JSON describing a book, with the fields '\''title'\'' and '\''author'\'' and '\''publication_year'\''"
        }
      ],
      "response_format": {
        "type": "json_object",
        "schema": {
          "type": "object",
          "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "publication_year": {"type": "integer"}
          },
          "required": ["title", "author", "publication_year"]
        }
      }
    }'
  ```
</CodeBlocks>

In this schema, we defined three keys ("title," "author," "publication\_year") and their expected data types ("string" and "integer"). The LLM will generate a JSON object that adheres to this structure.

```
# Example response

{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publication_year": 1925
}

```

### Nested Array Schema Json Example

Here's an example of a nested array. Note that the top level json structure must always be a json object.

<CodeBlocks>
  ```python PYTHON
  cohere_api_key = os.getenv("cohere_api_key")
  co = cohere.ClientV2(cohere_api_key)
  response = co.chat(
      response_format={
          "type": "json_object",
          "schema": {
              "type": "object",
              "properties": {
                  "actions": {
                      "type": "array",
                      "items": {
                          "type": "object",
                          "properties": {
                              "japanese": {"type": "string"},
                              "romaji": {"type": "string"},
                              "english": {"type": "string"},
                          },
                          "required": ["japanese", "romaji", "english"],
                      },
                  }
              },
              "required": ["actions"],
          },
      },
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Generate a JSON array of objects with the following fields: japanese, romaji, english. These actions should be japanese verbs provided in the dictionary form.",
          },
      ],
  )
  return json.loads(response.message.content[0].text)
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Generate a JSON array of objects with the following fields: japanese, romaji, english. These actions should be japanese verbs provided in the dictionary form."
        }
      ],
      "response_format": {
        "type": "json_object",
        "schema": {
          "type": "object",
          "properties": {
            "actions": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "japanese": {"type": "string"},
                  "romaji": {"type": "string"},
                  "english": {"type": "string"}
                },
                "required": ["japanese", "romaji", "english"]
              }
            }
          },
          "required": ["actions"]
        }
      }
    }'
  ```
</CodeBlocks>

The output for this example would be:

```json
{
    "actions": [
        {"japanese": "いこう", "romaji": "ikou", "english": "onward"},
        {"japanese": "探す", "romaji": "sagasu", "english": "search"},
        {"japanese": "話す", "romaji": "hanasu", "english": "talk"}
    ]
}
```

<Info title="Important">
  Note: Each schema provided (in both JSON and Tools modes) will incur a latency overhead required for processing the schema. This is only applicable for the first few requests.
</Info>

### Structured Outputs (Tools)

When you use the Chat API with `tools` (see [tool use](https://docs.cohere.com/docs/tool-use) and [agents](https://docs.cohere.com/docs/multi-step-tool-use)), setting the `strict_tools` parameter to `True`  will enforce that the tool calls generated by the mode strictly adhere to the tool descriptions you provided.

Concretely, this means:

* No hallucinated tool names
* No hallucinated tool parameters
* Every `required` parameter is included in the tool call
* All parameters produce the requested data types

With `strict_tools` enabled, the API will ensure that the tool names and tool parameters are generated according to the tool definitions. This eliminates tool name and parameter hallucinations, ensures that each parameter matches the specified data type, and that all required parameters are included in the model response.

Additionally, this results in faster development. You don’t need to spend a lot of time prompt engineering the model to avoid hallucinations.

In the example below, we create a tool that can retrieve weather data for a given location. The tool is called `get_weather` which contains a parameter called `location`. We then invoke the Chat API with `strict_tools` set to `True` to ensure that the generated tool calls always include the correct function and parameter names.

When the `strict_tools` parameter is set to `True`, you can define a maximum of 200 fields across all tools being passed to an API call.

<CodeBlocks>
  ```python PYTHON {24}
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description" : "Gets the weather of a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type" : "string",
                          "description": "The location to get weather."
                      }
                  },
                  "required": ["location"]
              }
          }
      },
  ]

  response = co.chat(model="command-r7b-12-2024",
                     messages=[{"role": "user", "content": "What's the weather in Toronto?"}],
                     tools=tools,
                     strict_tools=True)

  print(response.message.tool_calls)
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-r7b-12-2024",
      "messages": [
        {
          "role": "user",
          "content": "What'\''s the weather in Toronto?"
        }
      ],
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_weather",
            "description": "Gets the weather of a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The location to get weather."
                }
              },
              "required": ["location"]
            }
          }
        }
      ],
      "strict_tools": true
    }'
  ```
</CodeBlocks>

#### Important notes on using `strict_tools`

* This parameter is only supported in Chat API V2 via the strict\_tools parameter (not API V1).
* You must specify at least one `required` parameter. Tools with only optional parameters are not supported in this mode.
* You can define a maximum of 200 fields across all tools in a single Chat API call.

<Note title="Experimental">
  `strict_tools` is currently an experimental parameter. We’ll be iterating on this feature and are looking for feedback. Share your experience with us in the `#api-discussions` channel on [discord](https://discord.gg/co-mmunity) or via [email](mailto:tools_feedback@cohere.com).
</Note>

### When to Use Structured Outputs (JSON) vs. Structured Outputs (Tools)

Structured Outputs (JSON) are ideal for text generation use cases where you want to format the model's responses to users in a specific way.

For example, when building a travel planner application, you might want the LLM to generate itineraries in a specific JSON format, allowing the application to use the output in the other parts of the application.

Structured Outputs (Tools) are ideal for [tool use (or function calling)](https://docs.cohere.com/docs/tool-use) and [agents](https://docs.cohere.com/docs/multi-step-tool-use) use cases where you need the model to interact with external data or services. For instance, you can grant the model access to functions that interact with databases or other APIs.

In summary, opt for:

* Structured Outputs (JSON) when you need the model's response to follow a specific structure.
* Structured Outputs (Tools) when you need the model to interact with external data or services.

## Specifying a schema

### Generating nested objects

In JSON Schema mode, there are no limitations on the levels of nesting. However, in JSON mode (no schema specified), nesting is limited to 5 levels.

### Schema constraints

When constructing a `schema` keep the following constraints in mind:

* The `type` in the top level schema must be `object`
* Every object in the schema must have at least one `required` field specified

## Parameter types support

### Supported schema features

The Structured Outputs feature (both JSON and Tools mode) relies on the JSON Schema notation for defining the parameters. JSON Schema allows developers to specify the expected format of JSON objects, ensuring that the data adheres to predefined rules and constraints.

Structured Outputs supports a subset of the JSON Schema specification, detailed in the tables below. This is broken down into three categories:

* Structured Outputs (JSON)
* Structured Outputs (Tools) - When `strict_tools` is set to `True`
* Tool Use - When `strict_tools` is set to `False`

#### Basic types

| Parameter | [Structured Outputs (JSON)](#) | [Structured Outputs (Tools)](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) | [Tool Use](https://docs.cohere.com/v2/docs/tool-use) |
| --------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| String    | Yes                            | Yes                                                                                             | Yes                                                  |
| Integer   | Yes                            | Yes                                                                                             | Yes                                                  |
| Float     | Yes                            | Yes                                                                                             | Yes                                                  |
| Boolean   | Yes                            | Yes                                                                                             | Yes                                                  |

See usage examples for [JSON](https://docs.cohere.com/v2/docs/parameter-types-in-json#basic-types) and [Tools](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use#basic-types).

#### Arrays

| Parameter                       | [Structured Outputs (JSON)](#) | [Structured Outputs (Tools)](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) | [Tool Use](https://docs.cohere.com/v2/docs/tool-use) |
| ------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Arrays - With specific types    | Yes                            | Yes                                                                                             | Yes                                                  |
| Arrays - Without specific types | Yes                            | Yes                                                                                             | Yes                                                  |
| Arrays - List of lists          | Yes                            | Yes                                                                                             | Yes                                                  |

See usage examples for [JSON](https://docs.cohere.com/v2/docs/parameter-types-in-json#arrays) and [Tools](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use#arrays).

#### Others

| Parameter            | [Structured Outputs (JSON)](#) | [Structured Outputs (Tools)](https://docs.cohere.com/v2/docs/tool-use#structured-outputs-tools) | [Tool Use](https://docs.cohere.com/v2/docs/tool-use) |
| -------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Nested objects       | Yes                            | Yes                                                                                             | Yes                                                  |
| Enum                 | Yes                            | Yes                                                                                             | Yes                                                  |
| Const¹               | Yes                            | Yes                                                                                             | Yes                                                  |
| Pattern              | Yes                            | Yes                                                                                             | Yes                                                  |
| Format²              | Yes                            | Yes                                                                                             | Yes                                                  |
| \$ref                | Yes                            | Yes                                                                                             | Yes                                                  |
| \$def                | Yes                            | Yes                                                                                             | Yes                                                  |
| additionalProperties | Yes³                           | Yes⁴                                                                                            | Yes                                                  |
| uniqueItems          | No                             | No                                                                                              | Yes                                                  |
| anyOf                | Yes                            | Yes                                                                                             | Yes                                                  |

¹ Const is supported for these types: `int`, `float`, `bool`, `type(None)`, `str`.

² Format is supported for these values: `date-time`, `uuid`, `date`, `time`.

³ In Structured Outputs (JSON), `additionalProperties` does not enforce `required`, `dependencies`, `propertyNames`, `anyOf`, `allOf`, `oneOf`.

⁴ In Structured Outputs (Tools), `additionalProperties` does not enforce `required`, `dependencies`, `propertyNames`, `any Of`, `all Of`, `one Of`.

See usage examples for [JSON](https://docs.cohere.com/v2/docs/parameter-types-in-json#others) and [Tools](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use#others).

### Unsupported schema features

We do not support the entirety of the [JSON Schema specification](https://json-schema.org/specification).  Below is a list of some unsupported features:

* [Schema Composition](https://json-schema.org/understanding-json-schema/reference/combining#schema-composition) (`allOf`, `oneOf` and `not`)
* [Numeric Ranges](https://json-schema.org/understanding-json-schema/reference/numeric#range) (`maximum` and  `minimum`)
* [Array Length Ranges](https://json-schema.org/understanding-json-schema/reference/array#length) (`minItems` and `maxItems`)
* String limitations:
  * [String Length](https://json-schema.org/understanding-json-schema/reference/string#length) (`maxLength` and `minLength`)
  * The following are not supported in [Regular Expressions](https://json-schema.org/understanding-json-schema/reference/string#regexp)
    * `^`
    * `$`
    * `?=`
    * `?!`
  * The following [formats](https://json-schema.org/understanding-json-schema/reference/string#format) are the only supported ones
    * `date-time`
    * `uuid`
    * `date`
    * `time`

<Info title="Important">
  Note: Using Structured Outputs (in both JSON Schema and Tools modes) will incur a latency overhead required for processing the structured schema. This increase in latency only applies for the first few requests, since the schema is cached afterwards.
</Info>


# Parameter Types in Structured Outputs (JSON)

> This page shows usage examples of the JSON Schema parameter types supported in Structured Outputs (JSON).

This page provides usage examples of the JSON Schema parameters that are supported in [Structured Outputs (JSON)](https://docs.cohere.com/v2/docs/structured-outputs).

Note: Using Structured Outputs (JSON), the outputs are guaranteed to follow the schema for the tool name, parameter name, parameter data types, and the list of required parameters.

<Accordion title="Helper code">
  The examples on this page each provide a `response_format` schema and a `message` (the user message). To get an output, pass those values to a Chat endpoint call, as shown in the helper code below.

  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      # The model name. Example: command-a-03-2025
      model="MODEL_NAME",
      # The user message. Optional - you can first add a `system_message` role
      messages=[
          {
              "role": "user",
              "content": message,
          }
      ],
      # The schema that you define
      response_format=response_format,
      # Typically, you'll need a low temperature for more deterministic outputs
      temperature=0,
  )

  print(res.message.content[0].text)
  ```
</Accordion>

## Basic types

### String

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
        },
        "required": ["title", "author"],
    },
}

message = "Generate a JSON describing a book, with the fields 'title' and 'author'"
```

Example output:

```mdx wordWrap
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
```

### Integer

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "publication_year": {"type": "integer"},
        },
        "required": ["title", "author", "publication_year"],
    },
}

message = "Generate a JSON describing a book, with the fields 'title', 'author' and 'publication_year'"
```

Example output:

```mdx wordWrap
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publication_year": 1925
}
```

### Float

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "temperature": {"type": "number"},
        },
        "required": ["city", "temperature"],
    },
}

message = "Generate a JSON of a city and its average daily temperature in celcius"
```

Example output:

```mdx wordWrap
{
  "city": "Toronto",
  "temperature": 15.6
}
```

### Boolean

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "is_capital": {"type": "boolean"},
        },
        "required": ["city", "is_capital"],
    },
}

message = "Generate a JSON about a city in Spain and whether it is the capital of its country using 'is_capital'."
```

Example output:

```mdx wordWrap
{
    "city": "Madrid",
    "is_capital": true
}
```

## Array

### With specific types

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "cities": {
                "type": "array",
                "items": {"type": "string"},
            }
        },
        "required": ["cities"],
    },
}

message = "Generate a JSON listing three cities in Japan."
```

Example output:

```mdx wordWrap
{
  "cities": [
    "Tokyo",
    "Kyoto",
    "Osaka"
  ]
}
```

### Without specific types

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "cities": {
                "type": "array",
            }
        },
        "required": ["cities"],
    },
}

message = "Generate a JSON listing three cities in Japan."
```

Example output:

```mdx wordWrap
{
  "cities": [
    "Tokyo",
    "Kyoto",
    "Osaka"
  ]
}
```

### Lists of lists

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "coordinates": {
                "type": "array",
                "items": {
                    "type": "array",
                    "items": {"type": "number"},
                },
            }
        },
        "required": ["coordinates"],
    },
}

message = "Generate a JSON of three random coordinates."
```

Example output:

```mdx wordWrap
{
    "coordinates": [
        [-31.28333, 146.41667],
        [78.95833, 11.93333],
        [44.41667, -75.68333]
    ]
}
```

## Others

### Nested objects

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "actions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "japanese": {"type": "string"},
                        "romaji": {"type": "string"},
                        "english": {"type": "string"},
                    },
                    "required": ["japanese", "romaji", "english"],
                },
            }
        },
        "required": ["actions"],
    },
}

message = "Generate a JSON array of 3 objects with the following fields: japanese, romaji, english. These actions should be japanese verbs provided in the dictionary form."
```

Example output:

```mdx wordWrap
{
    "actions": [
        {
            "japanese": "食べる",
            "romaji": "taberu",
            "english": "to eat"
        },
        {
            "japanese": "話す",
            "romaji": "hanasu",
            "english": "to speak"
        },
        {
            "japanese": "書く",
            "romaji": "kaku",
            "english": "to write"
        }
    ]
}
```

### Enums

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "genre": {
                "type": "string",
                "enum": ["historical fiction", "cozy mystery"],
            },
            "title": {"type": "string"},
        },
        "required": ["title", "genre"],
    },
}

message = "Generate a JSON for a new book idea."
```

Example output:

```mdx wordWrap
{
  "genre": "historical fiction",
  "title": "The Unseen Thread: A Tale of the Silk Road's Secrets and Shadows"
 }
```

### Const

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "city": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "const": "Thailand",
                    },
                    "city_name": {"type": "string"},
                    "avg_temperature": {"type": "number"},
                },
                "required": [
                    "country",
                    "city_name",
                    "avg_temperature",
                ],
            }
        },
        "required": ["city"],
    },
}

message = "Generate a JSON of a city."
```

Example output:

```mdx wordWrap
{
  "city": {
    "country": "Thailand",
    "city_name": "Bangkok",
    "avg_temperature": 29.083333333333332
  }
}
```

### Pattern

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "product_sku": {
                "type": "string",
                "pattern": "[A-Z]{3}[0-9]{7}",
            }
        },
        "required": ["product_sku"],
    },
}

message = "Generate a JSON of an SKU for a new product line."
```

Example output:

```mdx wordWrap
{
  "product_sku": "PRX0012345"
}
```

### Format

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "itinerary": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "day_number": {"type": "integer"},
                        "date": {"type": "string", "format": "date"},
                        "places_to_visit": {"type": "string"},
                    },
                    "required": [
                        "day_number",
                        "date",
                        "places_to_visit",
                    ],
                },
            }
        },
        "required": ["itinerary"],
    },
}

message = (
    "Generate a JSON of a 3-day visit of Bali starting Jan 5 2025."
)
```

Example output:

```mdx wordWrap
{
  "itinerary": [
    {
      "day_number": 1,
      "date": "2025-01-05",
      "places_to_visit":  "Tanah Lot Temple, Ubud Monkey Forest, Tegalalang Rice Terraces"
    },
    {
      "day_number": 2,
      "date": "2025-01-06",
      "places_to_visit": "Mount Batur, Tirta Empul Temple, Ubud Art Market"
    },
    {
      "day_number": 3,
      "date": "2025-01-07",
      "places_to_visit": "Uluwatu Temple, Kuta Beach, Seminyak"
    }
  ]
}
```


# How to Get Predictable Outputs with Cohere Models

> Strategies for decoding text, and the parameters that impact the randomness and predictability of a language model's output.

The predictability of the model's output can be controlled using the `seed` and `temperature` parameters of the Chat API.

## Seed

<Info title="Note">
  The `seed` parameter does not guarantee long-term reproducibility. Under-the-hood updates to the model may invalidate the seed.
</Info>

The easiest way to force the model into reproducible behavior is by providing a value for the `seed` parameter. Specifying the same integer `seed` in consecutive requests will result in the same set of tokens being generated by the model. This can be useful for debugging and testing.

<CodeBlocks>
  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      model="command-a-03-2025",
      messages=[{"role": "user", "content": "say a random word"}],
      seed=45,
  )
  print(res.message.content[0].text)  # Sure! How about "onomatopoeia"?

  # making another request with the same seed results in the same generated text
  res = co.chat(
      model="command-a-03-2025",
      messages=[{"role": "user", "content": "say a random word"}],
      seed=45,
  )
  print(res.message.content[0].text)  # Sure! How about "onomatopoeia"?
  ```

  ```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "say a random word"
        }
      ],
      "seed": 45
    }'
  ```
</CodeBlocks>

## Temperature

Sampling from generation models incorporates randomness, so the same prompt may yield different outputs from generation to generation. Temperature is a parameter ranging from `0-1` used to tune the degree of randomness, and it defaults to a value of `.3`.

### How to pick temperature when sampling

A lower temperature means less randomness; a temperature of `0` will always yield the same output. Lower temperatures (around `.1` to `.3`) are more appropriate when performing tasks that have a "correct" answer, like question answering or summarization. If the model starts repeating itself this is a sign that the temperature may be too low.

High temperature means more randomness and less grounding. This can help the model give more creative outputs, but if you're using [retrieval augmented generation](/v2/docs/retrieval-augmented-generation-rag), it can also mean that it doesn't correctly use the context you provide. If the model starts going off topic, giving nonsensical outputs, or failing to ground properly, this is a sign that the temperature is too high.

<img src="file:6174aa01-e3b0-4802-996e-f690573741ad" alt="setting" />

Temperature can be tuned for different problems, but most people will find that a temperature of `.3` or `.5` is a good starting point.

As sequences get longer, the model naturally becomes more confident in its predictions, so you can raise the temperature much higher for long prompts without going off topic. In contrast, using high temperatures on short prompts can lead to outputs being very unstable.


# Advanced Generation Parameters

> This page describes advanced parameters for controlling generation.

There are a handful of additional model parameters that impact the kinds of outputs Cohere models will generate. These include the `top-p`, `top-k`, `frequency_penalty`, and `presence_penalty`  parameters.

## Top-p and Top-k

The method you use to pick output tokens is an important part of successfully generating text with language models. There are several methods (also called decoding strategies) for picking the output token, with two of the leading ones being top-k sampling and top-p sampling.

Let’s look at the example where the input to the model is the prompt `The name of that country is the`:

<Frame caption="Example output of a generation language model.">
  <img src="file:b51cd886-e2d1-4007-9f93-3a0e581e9ff9" alt="model." />
</Frame>

The output token in this case, `United`, was picked in the last step of processing -- after the language model has processed the input and calculated a likelihood score for every token in its vocabulary. This score indicates the likelihood that it will be the next token in the sentence (based on all the text the model was trained on).

<Frame caption="The model calculates a likelihood for each token in its vocabulary. The decoding strategy then picks one as the output.">
  <img src="file:d41e460c-77cb-4643-a816-81a898257070" alt="output." />
</Frame>

### 1. Pick the top token: greedy decoding

You can see in this example that we picked the token with the highest likelihood, `United`.

<Frame caption="Always picking the highest scoring token is called 'Greedy Decoding'. It's useful but has some drawbacks.">
  <img src="file:92d7b2c6-4270-4c33-b498-462d1a327f66" alt="drawbacks." />
</Frame>

Greedy decoding is a reasonable strategy, but has some drawbacks; outputs can get stuck in repetitive loops, for example. Think of the suggestions in your smartphone's auto-suggest. When you continually pick the highest suggested word, it may devolve into repeated sentences.

### 2. Pick from amongst the top tokens: top-k

Another commonly-used strategy is to sample from a shortlist of the top three tokens. This approach allows the other high-scoring tokens a chance of being picked. The randomness introduced by this sampling helps the quality of generation in a lot of scenarios.

<Frame caption="Adding some randomness helps make output text more natural. In top-3 decoding, we first shortlist three tokens then sample one of them by considering their likelihood scores.">
  <img src="file:cfdf8791-99bc-4f21-9c96-25d6f8bacd0b" alt="scores." />
</Frame>

More broadly, choosing the top three tokens means setting the [top-k parameter](https://docs.cohere.com/reference/chat#request.body.k) to `3` (it defaults to `0`) with `k=3`. Changing the top-k parameter sets the size of the shortlist the model samples from as it outputs each token. Setting top-k to `1` gives us greedy decoding.

<Frame caption="Adjusting to the top-k setting.">
  <img src="file:b5e56052-0e20-45ed-9ae9-447cef1ca2fc" alt="setting." class="light-bg" />
</Frame>

Note that when `k` is set to `0`, the model disables k sampling and uses p instead.

### 3. Pick from amongst the top tokens whose probabilities add up to 15%: top-p

The difficulty of selecting the best top-k value opens the door for a popular decoding strategy that dynamically sets the size of the shortlist of tokens. This method, called *Nucleus Sampling*, creates the shortlist by selecting the top tokens whose sum of likelihoods does not exceed a certain value. A toy example with a [top-p value](https://docs.cohere.com/reference/chat#request.body.p) of `0.15` (it defaults to `0.75`) would look like this:

<Frame caption="In top-p, the size of the shortlist is dynamically selected based on the sum of likelihood scores reaching some threshold.">
  <img src="file:3080af0a-85c4-42e4-9878-080d325522b0" alt="threshold." class="light-bg" />
</Frame>

Top-p is usually set to a high value (`p=0.75`, it's maximum value is `0.99`) with the purpose of limiting the long tail of low-probability tokens that may be sampled. We can use both top-k and top-p together. If both `k` and `p` are enabled, `p` acts after `k`. Here's a code snippet showing how this works:

```python PYTHON 
import cohere
co = cohere.ClientV2(api_key=<API_KEY>)
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "hello world!"}],
    k=100,
    p=0.75
)
print(response)
```

## Frequency and Presence Penalties

The final set of parameters worth discussing in this context are `frequency_penalty` and `presence_penalty`, both of which work on logits (which are log probabilities that haven't been normalized) in order to influence how often a given token appears in output.

The frequency penalty penalizes tokens that have already appeared in the preceding text (including the prompt), and scales based on how many times that token has appeared. So a token that has already appeared 10 times gets a higher penalty (which reduces its probability of appearing) than a token that has appeared only once.

The presence penalty, on the other hand, applies the penalty regardless of frequency. As long as the token has appeared once before, it will get penalized.

These settings are useful if you want to get rid of repetition in your outputs.


# Retrieval Augmented Generation (RAG)

> Guide on using Cohere's Retrieval Augmented Generation (RAG) capabilities such as document grounding and citations.

Retrieval Augmented Generation (RAG) is a method for generating text using additional information fetched from an external data source, which can greatly increase the accuracy of the response. When used in conjunction with [Command](https://docs.cohere.com/docs/models#command) family of models, the [Chat API](https://docs.cohere.com/reference/chat) makes it easy to generate text that is grounded on supplementary documents, thus minimizing hallucinations.

## A quick example

To call the Chat API with RAG, pass the following parameters as a minimum:

* `model` for the model ID
* `messages` for the user's query.
* `documents` for defining the documents to be used as the context for the response.

The code snippet below, for example, will produce a grounded answer to `"Where do the tallest penguins live?"`, along with inline citations based on the provided documents.

<Tabs>
  <Tab title="Cohere platform">
    ```python PYTHON
    # ! pip install -U cohere
    import cohere

    co = cohere.ClientV2(
        "COHERE_API_KEY"
    )  # Get your free API key here: https://dashboard.cohere.com/api-keys
    ```
  </Tab>

  <Tab title="Private deployment">
    ```python PYTHON
    # ! pip install -U cohere
    import cohere

    co = cohere.ClientV2(
        api_key="",  # Leave this blank
        base_url="<YOUR_DEPLOYMENT_URL>",
    )
    ```
  </Tab>
</Tabs>

```python PYTHON
# Retrieve the documents
documents = [
    {
        "data": {
            "title": "Tall penguins",
            "snippet": "Emperor penguins are the tallest.",
        }
    },
    {
        "data": {
            "title": "Penguin habitats",
            "snippet": "Emperor penguins only live in Antarctica.",
        }
    },
    {
        "data": {
            "title": "What are animals?",
            "snippet": "Animals are different from plants.",
        }
    },
]

# Add the user message
message = "Where do the tallest penguins live?"

messages = [{"role": "user", "content": message}]

response = co.chat(
    model="command-a-03-2025",
    messages=messages,
    documents=documents,
)

print(response.message.content[0].text)

print(response.message.citations)
```

```bash cURL
curl --request POST \
  --url https://api.cohere.ai/v2/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "user",
        "content": "Where do the tallest penguins live?"
      }
    ],
    "documents": [
      {
        "data": {
          "title": "Tall penguins",
          "snippet": "Emperor penguins are the tallest."
        }
      },
      {
        "data": {
          "title": "Penguin habitats",
          "snippet": "Emperor penguins only live in Antarctica."
        }
      },
      {
        "data": {
          "title": "What are animals?",
          "snippet": "Animals are different from plants."
        }
      }
    ]
  }'
```

The resulting generation is`"The tallest penguins are emperor penguins, which live in Antarctica."`. The model was able to combine partial information from multiple sources and ignore irrelevant documents to arrive at the full answer.

Nice :penguin:❄️!

Example response:

```mdx
# response.message.content[0].text
Emperor penguins are the tallest penguins. They only live in Antarctica.

# response.message.citations
[Citation(start=0,
          end=16, 
          text='Emperor penguins', 
          sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})]), 
Citation(start=25, 
          end=42, 
          text='tallest penguins.', 
          sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})]), 
Citation(start=61, 
          end=72, 
          text='Antarctica.',
          sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})])]
```

The response also includes **inline citations**  that reference the first two documents, since they hold the answers.

![](file:c225900f-0542-42e4-b911-64136e95c5ee)

<Note>
  Read more about using and customizing [RAG citations here](https://docs.cohere.com/v2/docs/rag-citations)
</Note>

## Three steps of RAG

The RAG workflow generally consists of **3 steps**:

* **Generating search queries** for finding relevant documents. *What does the model recommend looking up before answering this question?*
* **Fetching relevant documents** from an external data source using the generated search queries. *Performing a search to find some relevant information.*
* **Generating a response** with inline citations using the fetched documents. *Generating a response using the fetched documents. This response will contain inline citations, which you can decide to leverage or ignore*.

### Example: Using RAG to identify the definitive 90s boy band

In this section, we will use the three step RAG workflow to finally settle the score between the notorious boy bands Backstreet Boys and NSYNC. We ask the model to provide an informed answer to the question `"Who is more popular: Nsync or Backstreet Boys?"`

### Step 1: Generating search queries

First, the model needs to generate an optimal set of search queries to use for retrieval.

There are different possible approaches to do this. In this example, we'll take a [tool use](/v2/docs/tool-use) approach.

Here, we build a tool that takes a user query and returns a list of relevant document snippets for that query. The tool can generate zero, one or multiple search queries depending on the user query.

```python PYTHON
message = "Who is more popular: Nsync or Backstreet Boys?"

# Define the query generation tool
query_gen_tool = [
    {
        "type": "function",
        "function": {
            "name": "internet_search",
            "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
            "parameters": {
                "type": "object",
                "properties": {
                    "queries": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "a list of queries to search the internet with.",
                    }
                },
                "required": ["queries"],
            },
        },
    }
]

# Define a system message to optimize search query generation
instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."

# Generate search queries (if any)
import json

search_queries = []

res = co.chat(
    model="command-a-03-2025",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": message},
    ],
    tools=query_gen_tool,
)

if res.message.tool_calls:
    for tc in res.message.tool_calls:
        queries = json.loads(tc.function.arguments)["queries"]
        search_queries.extend(queries)

print(search_queries)
```

```bash cURL
curl --request POST \
  --url https://api.cohere.ai/v2/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "system",
        "content": "Write a search query that will find helpful information for answering the user'\''s question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."
      },
      {
        "role": "user",
        "content": "Who is more popular: Nsync or Backstreet Boys?"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "internet_search",
          "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
          "parameters": {
            "type": "object",
            "properties": {
              "queries": {
                "type": "array",
                "items": {"type": "string"},
                "description": "a list of queries to search the internet with."
              }
            },
            "required": ["queries"]
          }
        }
      }
    ]
  }'
```

```
# Sample response
['popularity of NSync', 'popularity of Backstreet Boys']
```

Indeed, to generate a factually accurate answer to the question "Who is more popular: Nsync or Backstreet Boys?", looking up `popularity of NSync` and `popularity of Backstreet Boys` first would be helpful.

<Accordion title="Customizing the generation of search queries">
  You can then update the system message and/or the tool definition to generate queries that are more relevant to your use case.

  For example, you can update the system message to encourage a longer list of search queries to be generated.

  ```python PYTHON
  instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."
  ```

  Example response:

  ```mdx
  ['NSync popularity', 'Backstreet Boys popularity', 'NSync vs Backstreet Boys popularity comparison', 'Which boy band is more popular NSync or Backstreet Boys', 'NSync and Backstreet Boys fan base size comparison', 'Who has sold more albums NSync or Backstreet Boys', 'NSync and Backstreet Boys chart performance comparison']
  ```
</Accordion>

### Step 2: Fetching relevant documents

The next step is to fetch documents from the relevant data source using the generated search queries. For example, to answer the question about the two pop sensations *NSYNC* and *Backstreet Boys*, one might want to use an API from a web search engine, and fetch the contents of the websites listed at the top of the search results.

We won't go into details of fetching data in this guide, since it's very specific to the search API you're querying. However we should mention that breaking up documents into small chunks of ±400 words will help you get the best performance from Cohere models.

<Accordion title="Context length limit">
  When trying to stay within the context length limit, you might need to omit some of the documents from the request. To make sure that only the least relevant documents are omitted, we recommend using the [Rerank endpoint](https://docs.cohere.com/reference/rerank) endpoint which will sort the documents by relevancy to the query. The lowest ranked documents are the ones you should consider dropping first.
</Accordion>

#### Formatting documents

The Chat endpoint supports a few different options for structuring documents in the `documents` parameter:

* List of objects with `data` object: Each document is passed as a `data` object (with an optional `id` field to be used in citations). The `data` object is a string-any dictionary containing the document's contents. For example, a web search document can contain a `title`, `text`, and `url` for the document's title, text, and URL.
* List of objects with `data` string: Each document is passed as a `data` string (with an optional `id` field to be used in citations).
* List of strings: Each document is passed as a string.

The following examples demonstrate the options mentioned above.

<Tabs>
  <Tab title="'data' object">
    ```python PYTHON
    documents = [
        {
            "data": {
                "title": "Tall penguins",
                "snippet": "Emperor penguins are the tallest.",
            }
        }
    ]
    ```
  </Tab>

  <Tab title="'data' string">
    ```python PYTHON
    documents = [
        {"data": "Tall penguins: Emperor penguins are the tallest."}
    ]
    ```
  </Tab>

  <Tab title="string">
    ```python PYTHON
    documents = [
        "Tall penguins: Emperor penguins are the tallest.",
    ]
    ```
  </Tab>
</Tabs>

The `id` field will be used in citation generation as the reference document IDs. If no `id` field is passed in an API call, the API will automatically generate the IDs based on the documents position in the list. For more information, see the guide on [using custom IDs](https://docs.cohere.com/docs/rag-citations).

### Step 3: Generating a response with citations

In the final step, we will be calling the Chat API again, but this time passing along the `documents` you acquired in Step 2. We recommend using a few descriptive keys such as `"title"`, `"snippet"`, or `"last updated"` and only including semantically relevant data. The keys and the values will be formatted into the prompt and passed to the model.

```python PYTHON
documents = [
    {
        "data": {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
        }
    },
    {
        "data": {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
        }
    },
    {
        "data": {
            "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
            "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
        }
    },
    {
        "data": {
            "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
            "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
        }
    },
]

# Add the user message
message = "Who is more popular: Nsync or Backstreet Boys?"
messages = [{"role": "user", "content": message}]

response = co.chat(
    model="command-a-03-2025",
    messages=messages,
    documents=documents,
)

print(response.message.content[0].text)
```

```bash cURL
curl --request POST \
  --url https://api.cohere.ai/v2/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "user",
        "content": "Who is more popular: Nsync or Backstreet Boys?"
      }
    ],
    "documents": [
      {
        "data": {
          "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
          "snippet": "At one point, Backstreet Boys defined success: massive albums sales across the globe..."
        }
      },
      {
        "data": {
          "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
          "snippet": "At the turn of the millennium three teen acts were huge in the US..."
        }
      }
    ]
  }'
```

Example response:

```mdx
Both NSYNC and Backstreet Boys were huge in the US at the turn of the millennium. However, Backstreet Boys achieved a greater level of success than NSYNC. They dominated the music business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists. Their success included massive album sales across the globe, great singles sales, plenty of chart-topping releases, hugely hyped tours and tremendous media coverage.
```

In this RAG setting, Cohere models are trained to generate fine-grained citations, out-of-the-box, alongside their text output. Here, we see a sample list of citations, one for each specific span in its response, where it uses the document(s) to answer the question.

For a deeper dive into the citations feature, see the [RAG citations guide](https://docs.cohere.com/v2/docs/rag-citations).

```python PYTHON
print(response.message.citations)
```

Example response:

```mdx
# (truncated for brevity)
[Citation(start=36, 
          end=81, 
          text='huge in the US at the turn of the millennium.', 
          sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': "↓ Skip to Main Content\n\nMusic industry – One step closer ...", 'title': 'CSPC: NSYNC Popularity Analysis - ChartMasters'})]),
Citation(start=107, 
          end=154, 
          text='achieved a greater level of success than NSYNC.', 
          sources=[DocumentSource(type='document', id='doc:2', document={'id': 'doc:2', 'snippet': ' 1997, 1998, 2000 and 2001 also rank amongst some of the very best ...', 'title': 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters'})]),
Citation(start=160, 
        end=223,
        ...
...]
```

Not only will we discover that the Backstreet Boys were the more popular band, but the model can also *Tell Me Why*, by providing details [supported by citations](https://docs.cohere.com/docs/documents-and-citations).

For a more in-depth RAG example that leverages the Embed and Rerank endpoints for retrieval, see [End-to-end example of RAG with Chat, Embed, and Rerank](https://docs.cohere.com/v2/docs/rag-complete-example).

### Caveats

It’s worth underscoring that RAG does not guarantee accuracy. It involves giving a model context which informs its replies, but if the provided documents are themselves out-of-date, inaccurate, or biased, whatever the model generates might be as well. What’s more, RAG doesn’t guarantee that a model won’t hallucinate. It greatly reduces the risk, but doesn’t necessarily eliminate it altogether. This is why we put an emphasis on including inline citations, which allow users to verify the information.


# End-to-end example of RAG with Chat, Embed, and Rerank

> Guide on using Cohere's Retrieval Augmented Generation (RAG) capabilities covering the Chat, Embed, and Rerank endpoints (API v2).

This section expands on the [basic RAG usage](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) by demonstrating a more complete example that includes:

* Retrieval and reranking of documents (via the Embed and Rerank endpoints).
* Building RAG for chatbots (involving multi-turn conversations).

## Setup

First, import the Cohere library and create a client.

<Tabs>
  <Tab title="Cohere platform">
    ```python PYTHON
    # ! pip install -U cohere
    import cohere
    import json
    import numpy as np

    co = cohere.ClientV2(
        "COHERE_API_KEY"
    )  # Get your free API key here: https://dashboard.cohere.com/api-keys
    ```
  </Tab>

  <Tab title="Private deployment">
    ```python PYTHON
    # ! pip install -U cohere
    import cohere
    import json
    import numpy as np

    co = cohere.ClientV2(
        api_key="",  # Leave this blank
        base_url="<YOUR_DEPLOYMENT_URL>",
    )
    ```
  </Tab>
</Tabs>

## Step 1: Generating search queries

Next, we create a search query generation tool for generating search queries from user queries.

We pass a user query, which in this example, asks about how to get to know the team.

<CodeBlocks>
  ```python PYTHON
  message = "How to get to know my teammates"

  # Define the query generation tool
  query_gen_tool = [
      {
          "type": "function",
          "function": {
              "name": "internet_search",
              "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "queries": {
                          "type": "array",
                          "items": {"type": "string"},
                          "description": "a list of queries to search the internet with.",
                      }
                  },
                  "required": ["queries"],
              },
          },
      }
  ]

  # Define a system message to optimize search query generation
  instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."

  # Generate search queries (if any)
  search_queries = []

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {"role": "system", "content": instructions},
          {"role": "user", "content": message},
      ],
      tools=query_gen_tool,
  )

  if res.message.tool_calls:
      for tc in res.message.tool_calls:
          queries = json.loads(tc.function.arguments)["queries"]
          search_queries.extend(queries)

  print(search_queries)
  ```

  ```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/chat' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "system",
        "content": "Write a search query that will find helpful information for answering the user'\''s question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."
      },
      {
        "role": "user",
        "content": "I'\''m joining a new team as a Principal Analyst. What are the best ways to quickly get to know my teammates?"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "internet_search",
          "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
          "parameters": {
            "type": "object",
            "properties": {
              "queries": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "a list of queries to search the internet with."
              }
            },
            "required": ["queries"]
          }
        }
      }
    ]
  }'
  ```
</CodeBlocks>

Example response:

```mdx
['how to get to know your teammates']
```

## Step 2: Fetching relevant documents

### Retrieval with Embed

Given the search query, we need a way to retrieve the most relevant documents from a large collection of documents.

This is where we can leverage text embeddings through the [Embed endpoint](https://docs.cohere.com/reference/embed).

The Embed endpoint enables semantic search, which lets us to compare the semantic meaning of the documents and the query. It solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles at capturing the context or meaning of a piece of text.

The Embed endpoint takes in texts as input and returns embeddings as output.

First, we need to embed the documents to search from. We call the Embed endpoint using `co.embed()` and pass the following arguments:

* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents (instead of the query) for search
* `texts`: The list of texts (the FAQs)
* `embedding_types`: We choose the `float` as the embedding type.

<CodeBlocks>
  ```python PYTHON
  # Define the documents
  documents = [
      {
          "data": {
              "text": "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged."
          }
      },
      {
          "data": {
              "text": "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."
          }
      },
      {
          "data": {
              "text": "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!"
          }
      },
      {
          "data": {
              "text": "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed."
          }
      },
      {
          "data": {
              "text": "Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business."
          }
      },
      {
          "data": {
              "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
          }
      },
      {
          "data": {
              "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
          }
      },
      {
          "data": {
              "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
          }
      },
      {
          "data": {
              "text": "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year."
          }
      },
      {
          "data": {
              "text": "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead."
          }
      },
  ]

  # Embed the documents
  doc_emb = co.embed(
      model="embed-v4.0",
      input_type="search_document",
      texts=[doc["data"]["text"] for doc in documents],
      embedding_types=["float"],
  ).embeddings.float
  ```

  ```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/embed' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "embed-v4.0",
    "input_type": "search_document",
    "embedding_types": ["float"],
    "texts": [
      "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
      "Finding Coffee Spots: For your caffeine fix, head to the break room'\''s coffee machine or cross the street to the café for artisan coffee.",
      "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!",
      "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      "Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business.",
      "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward.",
      "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.",
      "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.",
      "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.",
      "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead."
    ]
  }'
  ```
</CodeBlocks>

We choose `search_query` as the `input_type` in the Embed endpoint call. This ensures the model treats this as the query (instead of the documents) for search.

<CodeBlocks>
  ```python PYTHON
  # Embed the search query
  query_emb = co.embed(
      model="embed-v4.0",
      input_type="search_query",
      texts=search_queries,
      embedding_types=["float"],
  ).embeddings.float
  ```

  ```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/embed' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "embed-v4.0",
    "input_type": "search_query",
    "embedding_types": ["float"],
    "texts": ["how to get to know your teammates"]
  }'
  ```
</CodeBlocks>

Now, we want to search for the most relevant documents to the query. For this, we make use of the `numpy` library to compute the similarity between each query-document pair using the dot product approach.

Each query-document pair returns a score, which represents how similar the pair are. We then sort these scores in descending order and select the top most similar pairs, which we choose 5 (this is an arbitrary choice, you can choose any number).

Here, we show the most relevant documents with their similarity scores.

```python PYTHON
# Compute dot product similarity and display results
n = 5
scores = np.dot(query_emb, np.transpose(doc_emb))[0]
max_idx = np.argsort(-scores)[:n]

retrieved_documents = [documents[item] for item in max_idx]

for rank, idx in enumerate(max_idx):
    print(f"Rank: {rank+1}")
    print(f"Score: {scores[idx]}")
    print(f"Document: {retrieved_documents[rank]}\n")
```

```mdx
Rank: 1
Score: 0.32653470360872655
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}

Rank: 2
Score: 0.26851855352264786
Document: {'data': {'text': 'Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead.'}}

Rank: 3
Score: 0.2581341975304149
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}

Rank: 4
Score: 0.18633336738178463
Document: {'data': {'text': "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."}}

Rank: 5
Score: 0.13022396595682814
Document: {'data': {'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}}
```

<Note>
  For simplicity, in this example, we are assuming only one query being generated. For practical implementations, multiple queries may be generated. For those scenarios, you will need to perform retrieval for each query.
</Note>

### Reranking with Rerank

Reranking can boost the results from semantic or lexical search further. The [Rerank endpoint](https://docs.cohere.com/reference/rerank) takes a list of search results and reranks them according to the most relevant documents to a query. This requires just a single line of code to implement.

We call the endpoint using `co.rerank()` and pass the following arguments:

* `query`: The user query
* `documents`: The list of documents we get from the semantic search results
* `top_n`: The top reranked documents to select
* `model`: We choose Rerank English 3

Looking at the results, we see that since the query is about getting to know the team, the document that talks about joining Slack channels is now ranked higher (1st) compared to earlier (3rd).

Here we select `top_n` to be 2, which will be the documents we will pass next for response generation.

<CodeBlocks>
  ```python PYTHON
  # Rerank the documents
  results = co.rerank(
      model="rerank-v3.5",
      query=search_queries[0],
      documents=[doc["data"]["text"] for doc in retrieved_documents],
      top_n=2,
  )

  # Display the reranking results
  for idx, result in enumerate(results.results):
      print(f"Rank: {idx+1}")
      print(f"Score: {result.relevance_score}")
      print(f"Document: {retrieved_documents[result.index]}\n")

  reranked_documents = [
      retrieved_documents[result.index] for result in results.results
  ]
  ```

  ```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/rerank' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "rerank-v3.5",
    "query": "how to get to know your teammates",
    "top_n": 2,
    "documents": [
      "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!",
      "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead.",
      "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
      "Finding Coffee Spots: For your caffeine fix, head to the break room'\''s coffee machine or cross the street to the café for artisan coffee.",
      "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    ]
  }'
  ```
</CodeBlocks>

```mdx
Rank: 1
Score: 0.07272241
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}

Rank: 2
Score: 0.058674112
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}
```

## Step 3: Generating the response

Finally, we call the Chat endpoint by passing the retrieved documents. This tells the model to run in RAG-mode and use these documents in its response.

The response and citations are then generated based on the the query and the documents retrieved.

<CodeBlocks>
  ```python PYTHON
  messages = [{"role": "user", "content": message}]

  # Generate the response
  response = co.chat(
      model="command-a-03-2025",
      messages=messages,
      documents=reranked_documents,
  )

  # Display the response
  print(response.message.content[0].text)

  # Display the citations and source documents
  if response.message.citations:
      print("\nCITATIONS:")
      for citation in response.message.citations:
          print(citation, "\n")
  ```

  ```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/chat' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "user",
        "content": "I'\''m joining a new team as a Principal Analyst. What are the best ways to quickly get to know my teammates?"
      }
    ],
    "documents": [
      {
        "data": {
          "text": "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!"
        }
      },
      {
        "data": {
          "text": "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged."
        }
      }
    ]
  }'
  ```
</CodeBlocks>

```mdx
To get to know your teammates, you can join relevant Slack channels to stay informed and engaged. You will receive an invite via email. You can also participate in team-building activities such as monthly outings and weekly game nights.

CITATIONS:
start=39 end=67 text='join relevant Slack channels' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] type='TEXT_CONTENT' 

start=71 end=97 text='stay informed and engaged.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] type='TEXT_CONTENT' 

start=107 end=135 text='receive an invite via email.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] type='TEXT_CONTENT' 

start=164 end=188 text='team-building activities' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] type='TEXT_CONTENT' 

start=197 end=236 text='monthly outings and weekly game nights.' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] type='TEXT_CONTENT'
```



---

**Navigation:** [← Previous](./01-cohere-documentation.md) | [Index](./index.md) | [Next →](./03-rag-streaming.md)
