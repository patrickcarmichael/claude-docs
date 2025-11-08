# Website RAG Search

**Navigation:** [← Previous](./05-overview.md) | [Index](./index.md) | [Next →](./07-traces.md)

---

# Website RAG Search
Source: https://docs.crewai.com/en/tools/search-research/websitesearchtool

The `WebsiteSearchTool` is designed to perform a RAG (Retrieval-Augmented Generation) search within the content of a website.


# `WebsiteSearchTool`

<Note>
  The WebsiteSearchTool is currently in an experimental phase. We are actively working on incorporating this tool into our suite of offerings and will update the documentation accordingly.
</Note>


## Description

The WebsiteSearchTool is designed as a concept for conducting semantic searches within the content of websites.
It aims to leverage advanced machine learning models like Retrieval-Augmented Generation (RAG) to navigate and extract information from specified URLs efficiently.
This tool intends to offer flexibility, allowing users to perform searches across any website or focus on specific websites of interest.
Please note, the current implementation details of the WebsiteSearchTool are under development, and its functionalities as described may not yet be accessible.


## Installation

To prepare your environment for when the WebsiteSearchTool becomes available, you can install the foundational package with:

```shell  theme={null}
pip install 'crewai[tools]'
```

This command installs the necessary dependencies to ensure that once the tool is fully integrated, users can start using it immediately.


## Example Usage

Below are examples of how the WebsiteSearchTool could be utilized in different scenarios. Please note, these examples are illustrative and represent planned functionality:

```python Code theme={null}
from crewai_tools import WebsiteSearchTool


# Example of initiating tool that agents can use 

# to search across any discovered websites
tool = WebsiteSearchTool()


# Example of limiting the search to the content of a specific website, 

# so now agents can only search within that website
tool = WebsiteSearchTool(website='https://example.com')
```


## Arguments

* `website`: An optional argument intended to specify the website URL for focused searches. This argument is designed to enhance the tool's flexibility by allowing targeted searches when necessary.


## Customization Options

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code theme={null}
tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```



# YouTube Channel RAG Search
Source: https://docs.crewai.com/en/tools/search-research/youtubechannelsearchtool

The `YoutubeChannelSearchTool` is designed to perform a RAG (Retrieval-Augmented Generation) search within the content of a Youtube channel.


# `YoutubeChannelSearchTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

This tool is designed to perform semantic searches within a specific Youtube channel's content.
Leveraging the RAG (Retrieval-Augmented Generation) methodology, it provides relevant search results,
making it invaluable for extracting information or finding specific content without the need to manually sift through videos.
It streamlines the search process within Youtube channels, catering to researchers, content creators, and viewers seeking specific information or topics.


## Installation

To utilize the YoutubeChannelSearchTool, the `crewai_tools` package must be installed. Execute the following command in your shell to install:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

The following example demonstrates how to use the `YoutubeChannelSearchTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import YoutubeChannelSearchTool


# Initialize the tool for general YouTube channel searches
youtube_channel_tool = YoutubeChannelSearchTool()


# Define an agent that uses the tool
channel_researcher = Agent(
    role="Channel Researcher",
    goal="Extract relevant information from YouTube channels",
    backstory="An expert researcher who specializes in analyzing YouTube channel content.",
    tools=[youtube_channel_tool],
    verbose=True,
)


# Example task to search for information in a specific channel
research_task = Task(
    description="Search for information about machine learning tutorials in the YouTube channel {youtube_channel_handle}",
    expected_output="A summary of the key machine learning tutorials available on the channel.",
    agent=channel_researcher,
)


# Create and run the crew
crew = Crew(agents=[channel_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_channel_handle": "@exampleChannel"})
```

You can also initialize the tool with a specific YouTube channel handle:

```python Code theme={null}

# Initialize the tool with a specific YouTube channel handle
youtube_channel_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@exampleChannel'
)


# Define an agent that uses the tool
channel_researcher = Agent(
    role="Channel Researcher",
    goal="Extract relevant information from a specific YouTube channel",
    backstory="An expert researcher who specializes in analyzing YouTube channel content.",
    tools=[youtube_channel_tool],
    verbose=True,
)
```


## Parameters

The `YoutubeChannelSearchTool` accepts the following parameters:

* **youtube\_channel\_handle**: Optional. The handle of the YouTube channel to search within. If provided during initialization, the agent won't need to specify it when using the tool. If the handle doesn't start with '@', it will be automatically added.
* **config**: Optional. Configuration for the underlying RAG system, including LLM and embedder settings.
* **summarize**: Optional. Whether to summarize the retrieved content. Default is `False`.

When using the tool with an agent, the agent will need to provide:

* **search\_query**: Required. The search query to find relevant information in the channel content.
* **youtube\_channel\_handle**: Required only if not provided during initialization. The handle of the YouTube channel to search within.


## Custom Model and Embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code   theme={null}
youtube_channel_tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```


## Agent Integration Example

Here's a more detailed example of how to integrate the `YoutubeChannelSearchTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import YoutubeChannelSearchTool


# Initialize the tool
youtube_channel_tool = YoutubeChannelSearchTool()


# Define an agent that uses the tool
channel_researcher = Agent(
    role="Channel Researcher",
    goal="Extract and analyze information from YouTube channels",
    backstory="""You are an expert channel researcher who specializes in extracting 
    and analyzing information from YouTube channels. You have a keen eye for detail 
    and can quickly identify key points and insights from video content across an entire channel.""",
    tools=[youtube_channel_tool],
    verbose=True,
)


# Create a task for the agent
research_task = Task(
    description="""
    Search for information about data science projects and tutorials 
    in the YouTube channel {youtube_channel_handle}. 
    
    Focus on:
    1. Key data science techniques covered
    2. Popular tutorial series
    3. Most viewed or recommended videos
    
    Provide a comprehensive summary of these points.
    """,
    expected_output="A detailed summary of data science content available on the channel.",
    agent=channel_researcher,
)


# Run the task
crew = Crew(agents=[channel_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_channel_handle": "@exampleDataScienceChannel"})
```


## Implementation Details

The `YoutubeChannelSearchTool` is implemented as a subclass of `RagTool`, which provides the base functionality for Retrieval-Augmented Generation:

```python Code theme={null}
class YoutubeChannelSearchTool(RagTool):
    name: str = "Search a Youtube Channels content"
    description: str = "A tool that can be used to semantic search a query from a Youtube Channels content."
    args_schema: Type[BaseModel] = YoutubeChannelSearchToolSchema

    def __init__(self, youtube_channel_handle: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        if youtube_channel_handle is not None:
            kwargs["data_type"] = DataType.YOUTUBE_CHANNEL
            self.add(youtube_channel_handle)
            self.description = f"A tool that can be used to semantic search a query the {youtube_channel_handle} Youtube Channels content."
            self.args_schema = FixedYoutubeChannelSearchToolSchema
            self._generate_description()

    def add(
        self,
        youtube_channel_handle: str,
        **kwargs: Any,
    ) -> None:
        if not youtube_channel_handle.startswith("@"):
            youtube_channel_handle = f"@{youtube_channel_handle}"
        super().add(youtube_channel_handle, **kwargs)
```


## Conclusion

The `YoutubeChannelSearchTool` provides a powerful way to search and extract information from YouTube channel content using RAG techniques. By enabling agents to search across an entire channel's videos, it facilitates information extraction and analysis tasks that would otherwise be difficult to perform. This tool is particularly useful for research, content analysis, and knowledge extraction from YouTube channels.



# YouTube Video RAG Search
Source: https://docs.crewai.com/en/tools/search-research/youtubevideosearchtool

The `YoutubeVideoSearchTool` is designed to perform a RAG (Retrieval-Augmented Generation) search within the content of a Youtube video.


# `YoutubeVideoSearchTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

This tool is part of the `crewai_tools` package and is designed to perform semantic searches within Youtube video content, utilizing Retrieval-Augmented Generation (RAG) techniques.
It is one of several "Search" tools in the package that leverage RAG for different sources.
The YoutubeVideoSearchTool allows for flexibility in searches; users can search across any Youtube video content without specifying a video URL,
or they can target their search to a specific Youtube video by providing its URL.


## Installation

To utilize the `YoutubeVideoSearchTool`, you must first install the `crewai_tools` package.
This package contains the `YoutubeVideoSearchTool` among other utilities designed to enhance your data analysis and processing tasks.
Install the package by executing the following command in your terminal:

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

The following example demonstrates how to use the `YoutubeVideoSearchTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import YoutubeVideoSearchTool


# Initialize the tool for general YouTube video searches
youtube_search_tool = YoutubeVideoSearchTool()


# Define an agent that uses the tool
video_researcher = Agent(
    role="Video Researcher",
    goal="Extract relevant information from YouTube videos",
    backstory="An expert researcher who specializes in analyzing video content.",
    tools=[youtube_search_tool],
    verbose=True,
)


# Example task to search for information in a specific video
research_task = Task(
    description="Search for information about machine learning frameworks in the YouTube video at {youtube_video_url}",
    expected_output="A summary of the key machine learning frameworks mentioned in the video.",
    agent=video_researcher,
)


# Create and run the crew
crew = Crew(agents=[video_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_video_url": "https://youtube.com/watch?v=example"})
```

You can also initialize the tool with a specific YouTube video URL:

```python Code theme={null}

# Initialize the tool with a specific YouTube video URL
youtube_search_tool = YoutubeVideoSearchTool(
    youtube_video_url='https://youtube.com/watch?v=example'
)


# Define an agent that uses the tool
video_researcher = Agent(
    role="Video Researcher",
    goal="Extract relevant information from a specific YouTube video",
    backstory="An expert researcher who specializes in analyzing video content.",
    tools=[youtube_search_tool],
    verbose=True,
)
```


## Parameters

The `YoutubeVideoSearchTool` accepts the following parameters:

* **youtube\_video\_url**: Optional. The URL of the YouTube video to search within. If provided during initialization, the agent won't need to specify it when using the tool.
* **config**: Optional. Configuration for the underlying RAG system, including LLM and embedder settings.
* **summarize**: Optional. Whether to summarize the retrieved content. Default is `False`.

When using the tool with an agent, the agent will need to provide:

* **search\_query**: Required. The search query to find relevant information in the video content.
* **youtube\_video\_url**: Required only if not provided during initialization. The URL of the YouTube video to search within.


## Custom Model and Embeddings

By default, the tool uses OpenAI for both embeddings and summarization. To customize the model, you can use a config dictionary as follows:

```python Code   theme={null}
youtube_search_tool = YoutubeVideoSearchTool(
    config=dict(
        llm=dict(
            provider="ollama", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama2",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
```


## Agent Integration Example

Here's a more detailed example of how to integrate the `YoutubeVideoSearchTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import YoutubeVideoSearchTool


# Initialize the tool
youtube_search_tool = YoutubeVideoSearchTool()


# Define an agent that uses the tool
video_researcher = Agent(
    role="Video Researcher",
    goal="Extract and analyze information from YouTube videos",
    backstory="""You are an expert video researcher who specializes in extracting 
    and analyzing information from YouTube videos. You have a keen eye for detail 
    and can quickly identify key points and insights from video content.""",
    tools=[youtube_search_tool],
    verbose=True,
)


# Create a task for the agent
research_task = Task(
    description="""
    Search for information about recent advancements in artificial intelligence 
    in the YouTube video at {youtube_video_url}. 
    
    Focus on:
    1. Key AI technologies mentioned
    2. Real-world applications discussed
    3. Future predictions made by the speaker
    
    Provide a comprehensive summary of these points.
    """,
    expected_output="A detailed summary of AI advancements, applications, and future predictions from the video.",
    agent=video_researcher,
)


# Run the task
crew = Crew(agents=[video_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_video_url": "https://youtube.com/watch?v=example"})
```


## Implementation Details

The `YoutubeVideoSearchTool` is implemented as a subclass of `RagTool`, which provides the base functionality for Retrieval-Augmented Generation:

```python Code theme={null}
class YoutubeVideoSearchTool(RagTool):
    name: str = "Search a Youtube Video content"
    description: str = "A tool that can be used to semantic search a query from a Youtube Video content."
    args_schema: Type[BaseModel] = YoutubeVideoSearchToolSchema

    def __init__(self, youtube_video_url: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        if youtube_video_url is not None:
            kwargs["data_type"] = DataType.YOUTUBE_VIDEO
            self.add(youtube_video_url)
            self.description = f"A tool that can be used to semantic search a query the {youtube_video_url} Youtube Video content."
            self.args_schema = FixedYoutubeVideoSearchToolSchema
            self._generate_description()
```


## Conclusion

The `YoutubeVideoSearchTool` provides a powerful way to search and extract information from YouTube video content using RAG techniques. By enabling agents to search within video content, it facilitates information extraction and analysis tasks that would otherwise be difficult to perform. This tool is particularly useful for research, content analysis, and knowledge extraction from video sources.



# Bright Data Tools
Source: https://docs.crewai.com/en/tools/web-scraping/brightdata-tools

Bright Data integrations for SERP search, Web Unlocker scraping, and Dataset API.


# Bright Data Tools

This set of tools integrates Bright Data services for web extraction.


## Installation

```shell  theme={null}
uv add crewai-tools requests aiohttp
```


## Environment Variables

* `BRIGHT_DATA_API_KEY` (required)
* `BRIGHT_DATA_ZONE` (for SERP/Web Unlocker)

Create credentials at [https://brightdata.com/](https://brightdata.com/) (sign up, then create an API token and zone).
See their docs: [https://developers.brightdata.com/](https://developers.brightdata.com/)


## Included Tools

* `BrightDataSearchTool`: SERP search (Google/Bing/Yandex) with geo/language/device options.
* `BrightDataWebUnlockerTool`: Scrape pages with anti-bot bypass and rendering.
* `BrightDataDatasetTool`: Run Dataset API jobs and fetch results.


## Examples

### SERP Search

```python Code theme={null}
from crewai_tools import BrightDataSearchTool

tool = BrightDataSearchTool(
    query="CrewAI", 
    country="us",
)

print(tool.run())
```

### Web Unlocker

```python Code theme={null}
from crewai_tools import BrightDataWebUnlockerTool

tool = BrightDataWebUnlockerTool(
    url="https://example.com", 
    format="markdown",
)

print(tool.run(url="https://example.com"))
```

### Dataset API

```python Code theme={null}
from crewai_tools import BrightDataDatasetTool

tool = BrightDataDatasetTool(
    dataset_type="ecommerce", 
    url="https://example.com/product",
)

print(tool.run())
```


## Troubleshooting

* 401/403: verify `BRIGHT_DATA_API_KEY` and `BRIGHT_DATA_ZONE`.
* Empty/blocked content: enable rendering or try a different zone.


## Example

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import BrightDataSearchTool

tool = BrightDataSearchTool(
    query="CrewAI", 
    country="us",
)

agent = Agent(
    role="Web Researcher",
    goal="Search with Bright Data",
    backstory="Finds reliable results",
    tools=[tool],
    verbose=True,
)

task = Task(
    description="Search for CrewAI and summarize top results",
    expected_output="Short summary with links",
    agent=agent,
)

crew = Crew(
    agents=[agent], 
    tasks=[task],
    verbose=True,
)

result = crew.kickoff()
```



# Browserbase Web Loader
Source: https://docs.crewai.com/en/tools/web-scraping/browserbaseloadtool

Browserbase is a developer platform to reliably run, manage, and monitor headless browsers.


# `BrowserbaseLoadTool`


## Description

[Browserbase](https://browserbase.com) is a developer platform to reliably run, manage, and monitor headless browsers.

Power your AI data retrievals with:

* [Serverless Infrastructure](https://docs.browserbase.com/under-the-hood) providing reliable browsers to extract data from complex UIs
* [Stealth Mode](https://docs.browserbase.com/features/stealth-mode) with included fingerprinting tactics and automatic captcha solving
* [Session Debugger](https://docs.browserbase.com/features/sessions) to inspect your Browser Session with networks timeline and logs
* [Live Debug](https://docs.browserbase.com/guides/session-debug-connection/browser-remote-control) to quickly debug your automation


## Installation

* Get an API key and Project ID from [browserbase.com](https://browserbase.com) and set it in environment variables (`BROWSERBASE_API_KEY`, `BROWSERBASE_PROJECT_ID`).
* Install the [Browserbase SDK](http://github.com/browserbase/python-sdk) along with `crewai[tools]` package:

```shell  theme={null}
pip install browserbase 'crewai[tools]'
```


## Example

Utilize the BrowserbaseLoadTool as follows to allow your agent to load websites:

```python Code theme={null}
from crewai_tools import BrowserbaseLoadTool


# Initialize the tool with the Browserbase API key and Project ID
tool = BrowserbaseLoadTool()
```


## Arguments

The following parameters can be used to customize the `BrowserbaseLoadTool`'s behavior:

| Argument          | Type     | Description                                                                           |
| :---------------- | :------- | :------------------------------------------------------------------------------------ |
| **api\_key**      | `string` | *Optional*. Browserbase API key. Default is `BROWSERBASE_API_KEY` env variable.       |
| **project\_id**   | `string` | *Optional*. Browserbase Project ID. Default is `BROWSERBASE_PROJECT_ID` env variable. |
| **text\_content** | `bool`   | *Optional*. Retrieve only text content. Default is `False`.                           |
| **session\_id**   | `string` | *Optional*. Provide an existing Session ID.                                           |
| **proxy**         | `bool`   | *Optional*. Enable/Disable Proxies. Default is `False`.                               |



# Firecrawl Crawl Website
Source: https://docs.crewai.com/en/tools/web-scraping/firecrawlcrawlwebsitetool

The `FirecrawlCrawlWebsiteTool` is designed to crawl and convert websites into clean markdown or structured data.


# `FirecrawlCrawlWebsiteTool`


## Description

[Firecrawl](https://firecrawl.dev) is a platform for crawling and convert any website into clean markdown or structured data.


## Installation

* Get an API key from [firecrawl.dev](https://firecrawl.dev) and set it in environment variables (`FIRECRAWL_API_KEY`).
* Install the [Firecrawl SDK](https://github.com/mendableai/firecrawl) along with `crewai[tools]` package:

```shell  theme={null}
pip install firecrawl-py 'crewai[tools]'
```


## Example

Utilize the FirecrawlScrapeFromWebsiteTool as follows to allow your agent to load websites:

```python Code theme={null}
from crewai_tools import FirecrawlCrawlWebsiteTool

tool = FirecrawlCrawlWebsiteTool(url='firecrawl.dev')
```


## Arguments

* `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
* `url`: The base URL to start crawling from.
* `page_options`: Optional.
  * `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  * `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
* `crawler_options`: Optional. Options for controlling the crawling behavior.
  * `includes`: Optional. URL patterns to include in the crawl.
  * `exclude`: Optional. URL patterns to exclude from the crawl.
  * `generateImgAltText`: Optional. Generate alt text for images using LLMs (requires a paid plan).
  * `returnOnlyUrls`: Optional. If true, returns only the URLs as a list in the crawl status. Note: the response will be a list of URLs inside the data, not a list of documents.
  * `maxDepth`: Optional. Maximum depth to crawl. Depth 1 is the base URL, depth 2 includes the base URL and its direct children, and so on.
  * `mode`: Optional. The crawling mode to use. Fast mode crawls 4x faster on websites without a sitemap but may not be as accurate and shouldn't be used on heavily JavaScript-rendered websites.
  * `limit`: Optional. Maximum number of pages to crawl.
  * `timeout`: Optional. Timeout in milliseconds for the crawling operation.



# Firecrawl Scrape Website
Source: https://docs.crewai.com/en/tools/web-scraping/firecrawlscrapewebsitetool

The `FirecrawlScrapeWebsiteTool` is designed to scrape websites and convert them into clean markdown or structured data.


# `FirecrawlScrapeWebsiteTool`


## Description

[Firecrawl](https://firecrawl.dev) is a platform for crawling and convert any website into clean markdown or structured data.


## Installation

* Get an API key from [firecrawl.dev](https://firecrawl.dev) and set it in environment variables (`FIRECRAWL_API_KEY`).
* Install the [Firecrawl SDK](https://github.com/mendableai/firecrawl) along with `crewai[tools]` package:

```shell  theme={null}
pip install firecrawl-py 'crewai[tools]'
```


## Example

Utilize the FirecrawlScrapeWebsiteTool as follows to allow your agent to load websites:

```python Code theme={null}
from crewai_tools import FirecrawlScrapeWebsiteTool

tool = FirecrawlScrapeWebsiteTool(url='firecrawl.dev')
```


## Arguments

* `api_key`: Optional. Specifies Firecrawl API key. Defaults is the `FIRECRAWL_API_KEY` environment variable.
* `url`: The URL to scrape.
* `page_options`: Optional.
  * `onlyMainContent`: Optional. Only return the main content of the page excluding headers, navs, footers, etc.
  * `includeHtml`: Optional. Include the raw HTML content of the page. Will output a html key in the response.
* `extractor_options`: Optional. Options for LLM-based extraction of structured information from the page content
  * `mode`: The extraction mode to use, currently supports 'llm-extraction'
  * `extractionPrompt`: Optional. A prompt describing what information to extract from the page
  * `extractionSchema`: Optional. The schema for the data to be extracted
* `timeout`: Optional. Timeout in milliseconds for the request



# Hyperbrowser Load Tool
Source: https://docs.crewai.com/en/tools/web-scraping/hyperbrowserloadtool

The `HyperbrowserLoadTool` enables web scraping and crawling using Hyperbrowser.


# `HyperbrowserLoadTool`


## Description

The `HyperbrowserLoadTool` enables web scraping and crawling using [Hyperbrowser](https://hyperbrowser.ai), a platform for running and scaling headless browsers. This tool allows you to scrape a single page or crawl an entire site, returning the content in properly formatted markdown or HTML.

Key Features:

* Instant Scalability - Spin up hundreds of browser sessions in seconds without infrastructure headaches
* Simple Integration - Works seamlessly with popular tools like Puppeteer and Playwright
* Powerful APIs - Easy to use APIs for scraping/crawling any site
* Bypass Anti-Bot Measures - Built-in stealth mode, ad blocking, automatic CAPTCHA solving, and rotating proxies


## Installation

To use this tool, you need to install the Hyperbrowser SDK:

```shell  theme={null}
uv add hyperbrowser
```


## Steps to Get Started

To effectively use the `HyperbrowserLoadTool`, follow these steps:

1. **Sign Up**: Head to [Hyperbrowser](https://app.hyperbrowser.ai/) to sign up and generate an API key.
2. **API Key**: Set the `HYPERBROWSER_API_KEY` environment variable or pass it directly to the tool constructor.
3. **Install SDK**: Install the Hyperbrowser SDK using the command above.


## Example

The following example demonstrates how to initialize the tool and use it to scrape a website:

```python Code theme={null}
from crewai_tools import HyperbrowserLoadTool
from crewai import Agent


# Initialize the tool with your API key
tool = HyperbrowserLoadTool(api_key="your_api_key")  # Or use environment variable


# Define an agent that uses the tool
@agent
def web_researcher(self) -> Agent:
    '''
    This agent uses the HyperbrowserLoadTool to scrape websites
    and extract information.
    '''
    return Agent(
        config=self.agents_config["web_researcher"],
        tools=[tool]
    )
```


## Parameters

The `HyperbrowserLoadTool` accepts the following parameters:

### Constructor Parameters

* **api\_key**: Optional. Your Hyperbrowser API key. If not provided, it will be read from the `HYPERBROWSER_API_KEY` environment variable.

### Run Parameters

* **url**: Required. The website URL to scrape or crawl.
* **operation**: Optional. The operation to perform on the website. Either 'scrape' or 'crawl'. Default is 'scrape'.
* **params**: Optional. Additional parameters for the scrape or crawl operation.


## Supported Parameters

For detailed information on all supported parameters, visit:

* [Scrape Parameters](https://docs.hyperbrowser.ai/reference/sdks/python/scrape#start-scrape-job-and-wait)
* [Crawl Parameters](https://docs.hyperbrowser.ai/reference/sdks/python/crawl#start-crawl-job-and-wait)


## Return Format

The tool returns content in the following format:

* For **scrape** operations: The content of the page in markdown or HTML format.
* For **crawl** operations: The content of each page separated by dividers, including the URL of each page.


## Conclusion

The `HyperbrowserLoadTool` provides a powerful way to scrape and crawl websites, handling complex scenarios like anti-bot measures, CAPTCHAs, and more. By leveraging Hyperbrowser's platform, this tool enables agents to access and extract web content efficiently.



# Overview
Source: https://docs.crewai.com/en/tools/web-scraping/overview

Extract data from websites and automate browser interactions with powerful scraping tools

These tools enable your agents to interact with the web, extract data from websites, and automate browser-based tasks. From simple web scraping to complex browser automation, these tools cover all your web interaction needs.


## **Available Tools**

<CardGroup cols={2}>
  <Card title="Scrape Website Tool" icon="globe" href="/en/tools/web-scraping/scrapewebsitetool">
    General-purpose web scraping tool for extracting content from any website.
  </Card>

  <Card title="Scrape Element Tool" icon="crosshairs" href="/en/tools/web-scraping/scrapeelementfromwebsitetool">
    Target specific elements on web pages with precision scraping capabilities.
  </Card>

  <Card title="Firecrawl Crawl Tool" icon="spider" href="/en/tools/web-scraping/firecrawlcrawlwebsitetool">
    Crawl entire websites systematically with Firecrawl's powerful engine.
  </Card>

  <Card title="Firecrawl Scrape Tool" icon="fire" href="/en/tools/web-scraping/firecrawlscrapewebsitetool">
    High-performance web scraping with Firecrawl's advanced capabilities.
  </Card>

  <Card title="Firecrawl Search Tool" icon="magnifying-glass" href="/en/tools/web-scraping/firecrawlsearchtool">
    Search and extract specific content using Firecrawl's search features.
  </Card>

  <Card title="Selenium Scraping Tool" icon="robot" href="/en/tools/web-scraping/seleniumscrapingtool">
    Browser automation and scraping with Selenium WebDriver capabilities.
  </Card>

  <Card title="ScrapFly Tool" icon="plane" href="/en/tools/web-scraping/scrapflyscrapetool">
    Professional web scraping with ScrapFly's premium scraping service.
  </Card>

  <Card title="ScrapGraph Tool" icon="network-wired" href="/en/tools/web-scraping/scrapegraphscrapetool">
    Graph-based web scraping for complex data relationships.
  </Card>

  <Card title="Spider Tool" icon="spider" href="/en/tools/web-scraping/spidertool">
    Comprehensive web crawling and data extraction capabilities.
  </Card>

  <Card title="BrowserBase Tool" icon="browser" href="/en/tools/web-scraping/browserbaseloadtool">
    Cloud-based browser automation with BrowserBase infrastructure.
  </Card>

  <Card title="HyperBrowser Tool" icon="window-maximize" href="/en/tools/web-scraping/hyperbrowserloadtool">
    Fast browser interactions with HyperBrowser's optimized engine.
  </Card>

  <Card title="Stagehand Tool" icon="hand" href="/en/tools/web-scraping/stagehandtool">
    Intelligent browser automation with natural language commands.
  </Card>

  <Card title="Oxylabs Scraper Tool" icon="globe" href="/en/tools/web-scraping/oxylabsscraperstool">
    Access web data at scale with Oxylabs.
  </Card>

  <Card title="Bright Data Tools" icon="spider" href="/en/tools/web-scraping/brightdata-tools">
    SERP search, Web Unlocker, and Dataset API integrations.
  </Card>
</CardGroup>


## **Common Use Cases**

* **Data Extraction**: Scrape product information, prices, and reviews
* **Content Monitoring**: Track changes on websites and news sources
* **Lead Generation**: Extract contact information and business data
* **Market Research**: Gather competitive intelligence and market data
* **Testing & QA**: Automate browser testing and validation workflows
* **Social Media**: Extract posts, comments, and social media analytics


## **Quick Start Example**

```python  theme={null}
from crewai_tools import ScrapeWebsiteTool, FirecrawlScrapeWebsiteTool, SeleniumScrapingTool


# Create scraping tools
simple_scraper = ScrapeWebsiteTool()
advanced_scraper = FirecrawlScrapeWebsiteTool()
browser_automation = SeleniumScrapingTool()


# Add to your agent
agent = Agent(
    role="Web Research Specialist",
    tools=[simple_scraper, advanced_scraper, browser_automation],
    goal="Extract and analyze web data efficiently"
)
```


## **Scraping Best Practices**

* **Respect robots.txt**: Always check and follow website scraping policies
* **Rate Limiting**: Implement delays between requests to avoid overwhelming servers
* **User Agents**: Use appropriate user agent strings to identify your bot
* **Legal Compliance**: Ensure your scraping activities comply with terms of service
* **Error Handling**: Implement robust error handling for network issues and blocked requests
* **Data Quality**: Validate and clean extracted data before processing


## **Tool Selection Guide**

* **Simple Tasks**: Use `ScrapeWebsiteTool` for basic content extraction
* **JavaScript-Heavy Sites**: Use `SeleniumScrapingTool` for dynamic content
* **Scale & Performance**: Use `FirecrawlScrapeWebsiteTool` for high-volume scraping
* **Cloud Infrastructure**: Use `BrowserBaseLoadTool` for scalable browser automation
* **Complex Workflows**: Use `StagehandTool` for intelligent browser interactions



# Oxylabs Scrapers
Source: https://docs.crewai.com/en/tools/web-scraping/oxylabsscraperstool

Oxylabs Scrapers allow to easily access the information from the respective sources. Please see the list of available sources below:
  - `Amazon Product`
  - `Amazon Search`
  - `Google Seach`
  - `Universal`



## Installation

Get the credentials by creating an Oxylabs Account [here](https://oxylabs.io).

```shell  theme={null}
pip install 'crewai[tools]' oxylabs
```

Check [Oxylabs Documentation](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets) to get more information about API parameters.


# `OxylabsAmazonProductScraperTool`

### Example

```python  theme={null}
from crewai_tools import OxylabsAmazonProductScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsAmazonProductScraperTool()

result = tool.run(query="AAAAABBBBCC")

print(result)
```

### Parameters

* `query` - 10-symbol ASIN code.
* `domain` - domain localization for Amazon.
* `geo_location` - the *Deliver to* location.
* `user_agent_type` - device type and browser.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to true.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsAmazonProductScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsAmazonProductScraperTool(
    config={
        "domain": "com",
        "parse": True,
        "context": [
            {
                "key": "autoselect_variant",
                "value": True
            }
        ]
    }
)

result = tool.run(query="AAAAABBBBCC")

print(result)
```


# `OxylabsAmazonSearchScraperTool`

### Example

```python  theme={null}
from crewai_tools import OxylabsAmazonSearchScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsAmazonSearchScraperTool()

result = tool.run(query="headsets")

print(result)
```

### Parameters

* `query` - Amazon search term.
* `domain` - Domain localization for Bestbuy.
* `start_page` - starting page number.
* `pages` - number of pages to retrieve.
* `geo_location` - the *Deliver to* location.
* `user_agent_type` - device type and browser.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to true.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsAmazonSearchScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsAmazonSearchScraperTool(
    config={
        "domain": 'nl',
        "start_page": 2,
        "pages": 2,
        "parse": True,
        "context": [
            {'key': 'category_id', 'value': 16391693031}
        ],
    }
)

result = tool.run(query='nirvana tshirt')

print(result)
```


# `OxylabsGoogleSearchScraperTool`

### Example

```python  theme={null}
from crewai_tools import OxylabsGoogleSearchScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsGoogleSearchScraperTool()

result = tool.run(query="iPhone 16")

print(result)
```

### Parameters

* `query` - search keyword.
* `domain` - domain localization for Google.
* `start_page` - starting page number.
* `pages` - number of pages to retrieve.
* `limit` - number of results to retrieve in each page.
* `locale` - `Accept-Language` header value which changes your Google search page web interface language.
* `geo_location` - the geographical location that the result should be adapted for. Using this parameter correctly is extremely important to get the right data.
* `user_agent_type` - device type and browser.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to true.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsGoogleSearchScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsGoogleSearchScraperTool(
    config={
        "parse": True,
        "geo_location": "Paris, France",
        "user_agent_type": "tablet",
    }
)

result = tool.run(query="iPhone 16")

print(result)
```


# `OxylabsUniversalScraperTool`

### Example

```python  theme={null}
from crewai_tools import OxylabsUniversalScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsUniversalScraperTool()

result = tool.run(url="https://ip.oxylabs.io")

print(result)
```

### Parameters

* `url` - website url to scrape.
* `user_agent_type` - device type and browser.
* `geo_location` - sets the proxy's geolocation to retrieve data.
* `render` - enables JavaScript rendering when set to `html`.
* `callback_url` - URL to your callback endpoint.
* `context` - Additional advanced settings and controls for specialized requirements.
* `parse` - returns parsed data when set to `true`, as long as a dedicated parser exists for the submitted URL's page type.
* `parsing_instructions` - define your own parsing and data transformation logic that will be executed on an HTML scraping result.

### Advanced example

```python  theme={null}
from crewai_tools import OxylabsUniversalScraperTool


# make sure OXYLABS_USERNAME and OXYLABS_PASSWORD variables are set
tool = OxylabsUniversalScraperTool(
    config={
        "render": "html",
        "user_agent_type": "mobile",
        "context": [
            {"key": "force_headers", "value": True},
            {"key": "force_cookies", "value": True},
            {
                "key": "headers",
                "value": {
                    "Custom-Header-Name": "custom header content",
                },
            },
            {
                "key": "cookies",
                "value": [
                    {"key": "NID", "value": "1234567890"},
                    {"key": "1P JAR", "value": "0987654321"},
                ],
            },
            {"key": "http_method", "value": "get"},
            {"key": "follow_redirects", "value": True},
            {"key": "successful_status_codes", "value": [808, 909]},
        ],
    }
)

result = tool.run(url="https://ip.oxylabs.io")

print(result)
```



# Scrape Element From Website Tool
Source: https://docs.crewai.com/en/tools/web-scraping/scrapeelementfromwebsitetool

The `ScrapeElementFromWebsiteTool` enables CrewAI agents to extract specific elements from websites using CSS selectors.


# `ScrapeElementFromWebsiteTool`


## Description

The `ScrapeElementFromWebsiteTool` is designed to extract specific elements from websites using CSS selectors. This tool allows CrewAI agents to scrape targeted content from web pages, making it useful for data extraction tasks where only specific parts of a webpage are needed.


## Installation

To use this tool, you need to install the required dependencies:

```shell  theme={null}
uv add requests beautifulsoup4
```


## Steps to Get Started

To effectively use the `ScrapeElementFromWebsiteTool`, follow these steps:

1. **Install Dependencies**: Install the required packages using the command above.
2. **Identify CSS Selectors**: Determine the CSS selectors for the elements you want to extract from the website.
3. **Initialize the Tool**: Create an instance of the tool with the necessary parameters.


## Example

The following example demonstrates how to use the `ScrapeElementFromWebsiteTool` to extract specific elements from a website:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeElementFromWebsiteTool


# Initialize the tool
scrape_tool = ScrapeElementFromWebsiteTool()


# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert in web scraping who can extract targeted content from web pages.",
    tools=[scrape_tool],
    verbose=True,
)


# Example task to extract headlines from a news website
scrape_task = Task(
    description="Extract the main headlines from the CNN homepage. Use the CSS selector '.headline' to target the headline elements.",
    expected_output="A list of the main headlines from CNN.",
    agent=web_scraper_agent,
)


# Create and run the crew
crew = Crew(agents=[web_scraper_agent], tasks=[scrape_task])
result = crew.kickoff()
```

You can also initialize the tool with predefined parameters:

```python Code theme={null}

# Initialize the tool with predefined parameters
scrape_tool = ScrapeElementFromWebsiteTool(
    website_url="https://www.example.com",
    css_element=".main-content"
)
```


## Parameters

The `ScrapeElementFromWebsiteTool` accepts the following parameters during initialization:

* **website\_url**: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.
* **css\_element**: Optional. The CSS selector for the elements to extract. If provided during initialization, the agent won't need to specify it when using the tool.
* **cookies**: Optional. A dictionary containing cookies to be sent with the request. This can be useful for websites that require authentication.


## Usage

When using the `ScrapeElementFromWebsiteTool` with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

* **website\_url**: The URL of the website to scrape.
* **css\_element**: The CSS selector for the elements to extract.

The tool will return the text content of all elements matching the CSS selector, joined by newlines.

```python Code theme={null}

# Example of using the tool with an agent
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific elements from websites",
    backstory="An expert in web scraping who can extract targeted content using CSS selectors.",
    tools=[scrape_tool],
    verbose=True,
)


# Create a task for the agent to extract specific elements
extract_task = Task(
    description="""
    Extract all product titles from the featured products section on example.com.
    Use the CSS selector '.product-title' to target the title elements.
    """,
    expected_output="A list of product titles from the website",
    agent=web_scraper_agent,
)


# Run the task through a crew
crew = Crew(agents=[web_scraper_agent], tasks=[extract_task])
result = crew.kickoff()
```


## Implementation Details

The `ScrapeElementFromWebsiteTool` uses the `requests` library to fetch the web page and `BeautifulSoup` to parse the HTML and extract the specified elements:

```python Code theme={null}
class ScrapeElementFromWebsiteTool(BaseTool):
    name: str = "Read a website content"
    description: str = "A tool that can be used to read a website content."
    
    # Implementation details...
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        css_element = kwargs.get("css_element", self.css_element)
        page = requests.get(
            website_url,
            headers=self.headers,
            cookies=self.cookies if self.cookies else {},
        )
        parsed = BeautifulSoup(page.content, "html.parser")
        elements = parsed.select(css_element)
        return "\n".join([element.get_text() for element in elements])
```


## Conclusion

The `ScrapeElementFromWebsiteTool` provides a powerful way to extract specific elements from websites using CSS selectors. By enabling agents to target only the content they need, it makes web scraping tasks more efficient and focused. This tool is particularly useful for data extraction, content monitoring, and research tasks where specific information needs to be extracted from web pages.



# Scrapegraph Scrape Tool
Source: https://docs.crewai.com/en/tools/web-scraping/scrapegraphscrapetool

The `ScrapegraphScrapeTool` leverages Scrapegraph AI's SmartScraper API to intelligently extract content from websites.


# `ScrapegraphScrapeTool`


## Description

The `ScrapegraphScrapeTool` is designed to leverage Scrapegraph AI's SmartScraper API to intelligently extract content from websites. This tool provides advanced web scraping capabilities with AI-powered content extraction, making it ideal for targeted data collection and content analysis tasks. Unlike traditional web scrapers, it can understand the context and structure of web pages to extract the most relevant information based on natural language prompts.


## Installation

To use this tool, you need to install the Scrapegraph Python client:

```shell  theme={null}
uv add scrapegraph-py
```

You'll also need to set up your Scrapegraph API key as an environment variable:

```shell  theme={null}
export SCRAPEGRAPH_API_KEY="your_api_key"
```

You can obtain an API key from [Scrapegraph AI](https://scrapegraphai.com).


## Steps to Get Started

To effectively use the `ScrapegraphScrapeTool`, follow these steps:

1. **Install Dependencies**: Install the required package using the command above.
2. **Set Up API Key**: Set your Scrapegraph API key as an environment variable or provide it during initialization.
3. **Initialize the Tool**: Create an instance of the tool with the necessary parameters.
4. **Define Extraction Prompts**: Create natural language prompts to guide the extraction of specific content.


## Example

The following example demonstrates how to use the `ScrapegraphScrapeTool` to extract content from a website:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import ScrapegraphScrapeTool


# Initialize the tool
scrape_tool = ScrapegraphScrapeTool(api_key="your_api_key")


# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert in web scraping who can extract targeted content from web pages.",
    tools=[scrape_tool],
    verbose=True,
)


# Example task to extract product information from an e-commerce site
scrape_task = Task(
    description="Extract product names, prices, and descriptions from the featured products section of example.com.",
    expected_output="A structured list of product information including names, prices, and descriptions.",
    agent=web_scraper_agent,
)


# Create and run the crew
crew = Crew(agents=[web_scraper_agent], tasks=[scrape_task])
result = crew.kickoff()
```

You can also initialize the tool with predefined parameters:

```python Code theme={null}

# Initialize the tool with predefined parameters
scrape_tool = ScrapegraphScrapeTool(
    website_url="https://www.example.com",
    user_prompt="Extract all product prices and descriptions",
    api_key="your_api_key"
)
```


## Parameters

The `ScrapegraphScrapeTool` accepts the following parameters during initialization:

* **api\_key**: Optional. Your Scrapegraph API key. If not provided, it will look for the `SCRAPEGRAPH_API_KEY` environment variable.
* **website\_url**: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.
* **user\_prompt**: Optional. Custom instructions for content extraction. If provided during initialization, the agent won't need to specify it when using the tool.
* **enable\_logging**: Optional. Whether to enable logging for the Scrapegraph client. Default is `False`.


## Usage

When using the `ScrapegraphScrapeTool` with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

* **website\_url**: The URL of the website to scrape.
* **user\_prompt**: Optional. Custom instructions for content extraction. Default is "Extract the main content of the webpage".

The tool will return the extracted content based on the provided prompt.

```python Code theme={null}

# Example of using the tool with an agent
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract specific information from websites",
    backstory="An expert in web scraping who can extract targeted content from web pages.",
    tools=[scrape_tool],
    verbose=True,
)


# Create a task for the agent to extract specific content
extract_task = Task(
    description="Extract the main heading and summary from example.com",
    expected_output="The main heading and summary from the website",
    agent=web_scraper_agent,
)


# Run the task
crew = Crew(agents=[web_scraper_agent], tasks=[extract_task])
result = crew.kickoff()
```


## Error Handling

The `ScrapegraphScrapeTool` may raise the following exceptions:

* **ValueError**: When API key is missing or URL format is invalid.
* **RateLimitError**: When API rate limits are exceeded.
* **RuntimeError**: When scraping operation fails (network issues, API errors).

It's recommended to instruct agents to handle potential errors gracefully:

```python Code theme={null}

# Create a task that includes error handling instructions
robust_extract_task = Task(
    description="""
    Extract the main heading from example.com.
    Be aware that you might encounter errors such as:
    - Invalid URL format
    - Missing API key
    - Rate limit exceeded
    - Network or API errors
    
    If you encounter any errors, provide a clear explanation of what went wrong
    and suggest possible solutions.
    """,
    expected_output="Either the extracted heading or a clear error explanation",
    agent=web_scraper_agent,
)
```


## Rate Limiting

The Scrapegraph API has rate limits that vary based on your subscription plan. Consider the following best practices:

* Implement appropriate delays between requests when processing multiple URLs.
* Handle rate limit errors gracefully in your application.
* Check your API plan limits on the Scrapegraph dashboard.


## Implementation Details

The `ScrapegraphScrapeTool` uses the Scrapegraph Python client to interact with the SmartScraper API:

```python Code theme={null}
class ScrapegraphScrapeTool(BaseTool):
    """
    A tool that uses Scrapegraph AI to intelligently scrape website content.
    """
    
    # Implementation details...
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        user_prompt = (
            kwargs.get("user_prompt", self.user_prompt)
            or "Extract the main content of the webpage"
        )

        if not website_url:
            raise ValueError("website_url is required")

        # Validate URL format
        self._validate_url(website_url)

        try:
            # Make the SmartScraper request
            response = self._client.smartscraper(
                website_url=website_url,
                user_prompt=user_prompt,
            )

            return response
        # Error handling...
```


## Conclusion

The `ScrapegraphScrapeTool` provides a powerful way to extract content from websites using AI-powered understanding of web page structure. By enabling agents to target specific information using natural language prompts, it makes web scraping tasks more efficient and focused. This tool is particularly useful for data extraction, content monitoring, and research tasks where specific information needs to be extracted from web pages.



# Scrape Website
Source: https://docs.crewai.com/en/tools/web-scraping/scrapewebsitetool

The `ScrapeWebsiteTool` is designed to extract and read the content of a specified website.


# `ScrapeWebsiteTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>


## Description

A tool designed to extract and read the content of a specified website. It is capable of handling various types of web pages by making HTTP requests and parsing the received HTML content.
This tool can be particularly useful for web scraping tasks, data collection, or extracting specific information from websites.


## Installation

Install the crewai\_tools package

```shell  theme={null}
pip install 'crewai[tools]'
```


## Example

```python  theme={null}
from crewai_tools import ScrapeWebsiteTool


# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()


# Initialize the tool with the website URL, 

# so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://www.example.com')


# Extract the text from the site
text = tool.run()
print(text)
```


## Arguments

| Argument         | Type     | Description                                                                                                                                        |
| :--------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **website\_url** | `string` | **Mandatory** website URL to read the file. This is the primary input for the tool, specifying which website's content should be scraped and read. |



# Scrapfly Scrape Website Tool
Source: https://docs.crewai.com/en/tools/web-scraping/scrapflyscrapetool

The `ScrapflyScrapeWebsiteTool` leverages Scrapfly's web scraping API to extract content from websites in various formats.


# `ScrapflyScrapeWebsiteTool`


## Description

The `ScrapflyScrapeWebsiteTool` is designed to leverage [Scrapfly](https://scrapfly.io/)'s web scraping API to extract content from websites. This tool provides advanced web scraping capabilities with headless browser support, proxies, and anti-bot bypass features. It allows for extracting web page data in various formats, including raw HTML, markdown, and plain text, making it ideal for a wide range of web scraping tasks.


## Installation

To use this tool, you need to install the Scrapfly SDK:

```shell  theme={null}
uv add scrapfly-sdk
```

You'll also need to obtain a Scrapfly API key by registering at [scrapfly.io/register](https://www.scrapfly.io/register/).


## Steps to Get Started

To effectively use the `ScrapflyScrapeWebsiteTool`, follow these steps:

1. **Install Dependencies**: Install the Scrapfly SDK using the command above.
2. **Obtain API Key**: Register at Scrapfly to get your API key.
3. **Initialize the Tool**: Create an instance of the tool with your API key.
4. **Configure Scraping Parameters**: Customize the scraping parameters based on your needs.


## Example

The following example demonstrates how to use the `ScrapflyScrapeWebsiteTool` to extract content from a website:

```python Code theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import ScrapflyScrapeWebsiteTool


# Initialize the tool
scrape_tool = ScrapflyScrapeWebsiteTool(api_key="your_scrapfly_api_key")


# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites",
    backstory="An expert in web scraping who can extract content from any website.",
    tools=[scrape_tool],
    verbose=True,
)


# Example task to extract content from a website
scrape_task = Task(
    description="Extract the main content from the product page at https://web-scraping.dev/products and summarize the available products.",
    expected_output="A summary of the products available on the website.",
    agent=web_scraper_agent,
)


# Create and run the crew
crew = Crew(agents=[web_scraper_agent], tasks=[scrape_task])
result = crew.kickoff()
```

You can also customize the scraping parameters:

```python Code theme={null}

# Example with custom scraping parameters
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites with custom parameters",
    backstory="An expert in web scraping who can extract content from any website.",
    tools=[scrape_tool],
    verbose=True,
)


# The agent will use the tool with parameters like:

# url="https://web-scraping.dev/products"

# scrape_format="markdown"

# ignore_scrape_failures=True

# scrape_config={

#     "asp": True,  # Bypass scraping blocking solutions, like Cloudflare

#     "render_js": True,  # Enable JavaScript rendering with a cloud headless browser

#     "proxy_pool": "public_residential_pool",  # Select a proxy pool

#     "country": "us",  # Select a proxy location

#     "auto_scroll": True,  # Auto scroll the page

# }

scrape_task = Task(
    description="Extract the main content from the product page at https://web-scraping.dev/products using advanced scraping options including JavaScript rendering and proxy settings.",
    expected_output="A detailed summary of the products with all available information.",
    agent=web_scraper_agent,
)
```


## Parameters

The `ScrapflyScrapeWebsiteTool` accepts the following parameters:

### Initialization Parameters

* **api\_key**: Required. Your Scrapfly API key.

### Run Parameters

* **url**: Required. The URL of the website to scrape.
* **scrape\_format**: Optional. The format in which to extract the web page content. Options are "raw" (HTML), "markdown", or "text". Default is "markdown".
* **scrape\_config**: Optional. A dictionary containing additional Scrapfly scraping configuration options.
* **ignore\_scrape\_failures**: Optional. Whether to ignore failures during scraping. If set to `True`, the tool will return `None` instead of raising an exception when scraping fails.


## Scrapfly Configuration Options

The `scrape_config` parameter allows you to customize the scraping behavior with the following options:

* **asp**: Enable anti-scraping protection bypass.
* **render\_js**: Enable JavaScript rendering with a cloud headless browser.
* **proxy\_pool**: Select a proxy pool (e.g., "public\_residential\_pool", "datacenter").
* **country**: Select a proxy location (e.g., "us", "uk").
* **auto\_scroll**: Automatically scroll the page to load lazy-loaded content.
* **js**: Execute custom JavaScript code by the headless browser.

For a complete list of configuration options, refer to the [Scrapfly API documentation](https://scrapfly.io/docs/scrape-api/getting-started).


## Usage

When using the `ScrapflyScrapeWebsiteTool` with an agent, the agent will need to provide the URL of the website to scrape and can optionally specify the format and additional configuration options:

```python Code theme={null}

# Example of using the tool with an agent
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites",
    backstory="An expert in web scraping who can extract content from any website.",
    tools=[scrape_tool],
    verbose=True,
)


# Create a task for the agent
scrape_task = Task(
    description="Extract the main content from example.com in markdown format.",
    expected_output="The main content of example.com in markdown format.",
    agent=web_scraper_agent,
)


# Run the task
crew = Crew(agents=[web_scraper_agent], tasks=[scrape_task])
result = crew.kickoff()
```

For more advanced usage with custom configuration:

```python Code theme={null}

# Create a task with more specific instructions
advanced_scrape_task = Task(
    description="""
    Extract content from example.com with the following requirements:
    - Convert the content to plain text format
    - Enable JavaScript rendering
    - Use a US-based proxy
    - Handle any scraping failures gracefully
    """,
    expected_output="The extracted content from example.com",
    agent=web_scraper_agent,
)
```


## Error Handling

By default, the `ScrapflyScrapeWebsiteTool` will raise an exception if scraping fails. Agents can be instructed to handle failures gracefully by specifying the `ignore_scrape_failures` parameter:

```python Code theme={null}

# Create a task that instructs the agent to handle errors
error_handling_task = Task(
    description="""
    Extract content from a potentially problematic website and make sure to handle any 
    scraping failures gracefully by setting ignore_scrape_failures to True.
    """,
    expected_output="Either the extracted content or a graceful error message",
    agent=web_scraper_agent,
)
```


## Implementation Details

The `ScrapflyScrapeWebsiteTool` uses the Scrapfly SDK to interact with the Scrapfly API:

```python Code theme={null}
class ScrapflyScrapeWebsiteTool(BaseTool):
    name: str = "Scrapfly web scraping API tool"
    description: str = (
        "Scrape a webpage url using Scrapfly and return its content as markdown or text"
    )
    
    # Implementation details...
    
    def _run(
        self,
        url: str,
        scrape_format: str = "markdown",
        scrape_config: Optional[Dict[str, Any]] = None,
        ignore_scrape_failures: Optional[bool] = None,
    ):
        from scrapfly import ScrapeApiResponse, ScrapeConfig

        scrape_config = scrape_config if scrape_config is not None else {}
        try:
            response: ScrapeApiResponse = self.scrapfly.scrape(
                ScrapeConfig(url, format=scrape_format, **scrape_config)
            )
            return response.scrape_result["content"]
        except Exception as e:
            if ignore_scrape_failures:
                logger.error(f"Error fetching data from {url}, exception: {e}")
                return None
            else:
                raise e
```


## Conclusion

The `ScrapflyScrapeWebsiteTool` provides a powerful way to extract content from websites using Scrapfly's advanced web scraping capabilities. With features like headless browser support, proxies, and anti-bot bypass, it can handle complex websites and extract content in various formats. This tool is particularly useful for data extraction, content monitoring, and research tasks where reliable web scraping is required.



# Selenium Scraper
Source: https://docs.crewai.com/en/tools/web-scraping/seleniumscrapingtool

The `SeleniumScrapingTool` is designed to extract and read the content of a specified website using Selenium.


# `SeleniumScrapingTool`

<Note>
  This tool is currently in development. As we refine its capabilities, users may encounter unexpected behavior.
  Your feedback is invaluable to us for making improvements.
</Note>


## Description

The `SeleniumScrapingTool` is crafted for high-efficiency web scraping tasks.
It allows for precise extraction of content from web pages by using CSS selectors to target specific elements.
Its design caters to a wide range of scraping needs, offering flexibility to work with any provided website URL.


## Installation

To use this tool, you need to install the CrewAI tools package and Selenium:

```shell  theme={null}
pip install 'crewai[tools]'
uv add selenium webdriver-manager
```

You'll also need to have Chrome installed on your system, as the tool uses Chrome WebDriver for browser automation.


## Example

The following example demonstrates how to use the `SeleniumScrapingTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import SeleniumScrapingTool


# Initialize the tool
selenium_tool = SeleniumScrapingTool()


# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites using Selenium",
    backstory="An expert web scraper who can extract content from dynamic websites.",
    tools=[selenium_tool],
    verbose=True,
)


# Example task to scrape content from a website
scrape_task = Task(
    description="Extract the main content from the homepage of example.com. Use the CSS selector 'main' to target the main content area.",
    expected_output="The main content from example.com's homepage.",
    agent=web_scraper_agent,
)


# Create and run the crew
crew = Crew(
    agents=[web_scraper_agent],
    tasks=[scrape_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff()
```

You can also initialize the tool with predefined parameters:

```python Code theme={null}

# Initialize the tool with predefined parameters
selenium_tool = SeleniumScrapingTool(
    website_url='https://example.com',
    css_element='.main-content',
    wait_time=5
)


# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract information from websites using Selenium",
    backstory="An expert web scraper who can extract content from dynamic websites.",
    tools=[selenium_tool],
    verbose=True,
)
```


## Parameters

The `SeleniumScrapingTool` accepts the following parameters during initialization:

* **website\_url**: Optional. The URL of the website to scrape. If provided during initialization, the agent won't need to specify it when using the tool.
* **css\_element**: Optional. The CSS selector for the elements to extract. If provided during initialization, the agent won't need to specify it when using the tool.
* **cookie**: Optional. A dictionary containing cookie information, useful for simulating a logged-in session to access restricted content.
* **wait\_time**: Optional. Specifies the delay (in seconds) before scraping, allowing the website and any dynamic content to fully load. Default is `3` seconds.
* **return\_html**: Optional. Whether to return the HTML content instead of just the text. Default is `False`.

When using the tool with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

* **website\_url**: Required. The URL of the website to scrape.
* **css\_element**: Required. The CSS selector for the elements to extract.


## Agent Integration Example

Here's a more detailed example of how to integrate the `SeleniumScrapingTool` with a CrewAI agent:

```python Code theme={null}
from crewai import Agent, Task, Crew, Process
from crewai_tools import SeleniumScrapingTool


# Initialize the tool
selenium_tool = SeleniumScrapingTool()


# Define an agent that uses the tool
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract and analyze information from dynamic websites",
    backstory="""You are an expert web scraper who specializes in extracting 
    content from dynamic websites that require browser automation. You have 
    extensive knowledge of CSS selectors and can identify the right selectors 
    to target specific content on any website.""",
    tools=[selenium_tool],
    verbose=True,
)


# Create a task for the agent
scrape_task = Task(
    description="""
    Extract the following information from the news website at {website_url}:
    
    1. The headlines of all featured articles (CSS selector: '.headline')
    2. The publication dates of these articles (CSS selector: '.pub-date')
    3. The author names where available (CSS selector: '.author')
    
    Compile this information into a structured format with each article's details grouped together.
    """,
    expected_output="A structured list of articles with their headlines, publication dates, and authors.",
    agent=web_scraper_agent,
)


# Run the task
crew = Crew(
    agents=[web_scraper_agent],
    tasks=[scrape_task],
    verbose=True,
    process=Process.sequential,
)
result = crew.kickoff(inputs={"website_url": "https://news-example.com"})
```


## Implementation Details

The `SeleniumScrapingTool` uses Selenium WebDriver to automate browser interactions:

```python Code theme={null}
class SeleniumScrapingTool(BaseTool):
    name: str = "Read a website content"
    description: str = "A tool that can be used to read a website content."
    args_schema: Type[BaseModel] = SeleniumScrapingToolSchema
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        css_element = kwargs.get("css_element", self.css_element)
        return_html = kwargs.get("return_html", self.return_html)
        driver = self._create_driver(website_url, self.cookie, self.wait_time)

        content = self._get_content(driver, css_element, return_html)
        driver.close()

        return "\n".join(content)
```

The tool performs the following steps:

1. Creates a headless Chrome browser instance
2. Navigates to the specified URL
3. Waits for the specified time to allow the page to load
4. Adds any cookies if provided
5. Extracts content based on the CSS selector
6. Returns the extracted content as text or HTML
7. Closes the browser instance


## Handling Dynamic Content

The `SeleniumScrapingTool` is particularly useful for scraping websites with dynamic content that is loaded via JavaScript. By using a real browser instance, it can:

1. Execute JavaScript on the page
2. Wait for dynamic content to load
3. Interact with elements if needed
4. Extract content that would not be available with simple HTTP requests

You can adjust the `wait_time` parameter to ensure that all dynamic content has loaded before extraction.


## Conclusion

The `SeleniumScrapingTool` provides a powerful way to extract content from websites using browser automation. By enabling agents to interact with websites as a real user would, it facilitates scraping of dynamic content that would be difficult or impossible to extract using simpler methods. This tool is particularly useful for research, data collection, and monitoring tasks that involve modern web applications with JavaScript-rendered content.



# Spider Scraper
Source: https://docs.crewai.com/en/tools/web-scraping/spidertool

The `SpiderTool` is designed to extract and read the content of a specified website using Spider.


# `SpiderTool`


## Description

[Spider](https://spider.cloud/?ref=crewai) is the [fastest](https://github.com/spider-rs/spider/blob/main/benches/BENCHMARKS.md#benchmark-results)
open source scraper and crawler that returns LLM-ready data.
It converts any website into pure HTML, markdown, metadata or text while enabling you to crawl with custom actions using AI.


## Installation

To use the `SpiderTool` you need to download the [Spider SDK](https://pypi.org/project/spider-client/)
and the `crewai[tools]` SDK too:

```shell  theme={null}
pip install spider-client 'crewai[tools]'
```


## Example

This example shows you how you can use the `SpiderTool` to enable your agent to scrape and crawl websites.
The data returned from the Spider API is already LLM-ready, so no need to do any cleaning there.

```python Code theme={null}
from crewai_tools import SpiderTool

def main():
    spider_tool = SpiderTool()

    searcher = Agent(
        role="Web Research Expert",
        goal="Find related information from specific URL's",
        backstory="An expert web researcher that uses the web extremely well",
        tools=[spider_tool],
        verbose=True,
    )

    return_metadata = Task(
        description="Scrape https://spider.cloud with a limit of 1 and enable metadata",
        expected_output="Metadata and 10 word summary of spider.cloud",
        agent=searcher
    )

    crew = Crew(
        agents=[searcher],
        tasks=[
            return_metadata,
        ],
        verbose=2
    )

    crew.kickoff()

if __name__ == "__main__":
    main()
```


## Arguments

| Argument                | Type     | Description                                                                                                                       |
| :---------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **api\_key**            | `string` | Specifies Spider API key. If not specified, it looks for `SPIDER_API_KEY` in environment variables.                               |
| **params**              | `object` | Optional parameters for the request. Defaults to `{"return_format": "markdown"}` to optimize content for LLMs.                    |
| **request**             | `string` | Type of request to perform (`http`, `chrome`, `smart`). `smart` defaults to HTTP, switching to JavaScript rendering if needed.    |
| **limit**               | `int`    | Max pages to crawl per website. Set to `0` or omit for unlimited.                                                                 |
| **depth**               | `int`    | Max crawl depth. Set to `0` for no limit.                                                                                         |
| **cache**               | `bool`   | Enables HTTP caching to speed up repeated runs. Default is `true`.                                                                |
| **budget**              | `object` | Sets path-based limits for crawled pages, e.g., `{"*":1}` for root page only.                                                     |
| **locale**              | `string` | Locale for the request, e.g., `en-US`.                                                                                            |
| **cookies**             | `string` | HTTP cookies for the request.                                                                                                     |
| **stealth**             | `bool`   | Enables stealth mode for Chrome requests to avoid detection. Default is `true`.                                                   |
| **headers**             | `object` | HTTP headers as a map of key-value pairs for all requests.                                                                        |
| **metadata**            | `bool`   | Stores metadata about pages and content, aiding AI interoperability. Defaults to `false`.                                         |
| **viewport**            | `object` | Sets Chrome viewport dimensions. Default is `800x600`.                                                                            |
| **encoding**            | `string` | Specifies encoding type, e.g., `UTF-8`, `SHIFT_JIS`.                                                                              |
| **subdomains**          | `bool`   | Includes subdomains in the crawl. Default is `false`.                                                                             |
| **user\_agent**         | `string` | Custom HTTP user agent. Defaults to a random agent.                                                                               |
| **store\_data**         | `bool`   | Enables data storage for the request. Overrides `storageless` when set. Default is `false`.                                       |
| **gpt\_config**         | `object` | Allows AI to generate crawl actions, with optional chaining steps via an array for `"prompt"`.                                    |
| **fingerprint**         | `bool`   | Enables advanced fingerprinting for Chrome.                                                                                       |
| **storageless**         | `bool`   | Prevents all data storage, including AI embeddings. Default is `false`.                                                           |
| **readability**         | `bool`   | Pre-processes content for reading via [Mozilla’s readability](https://github.com/mozilla/readability). Improves content for LLMs. |
| **return\_format**      | `string` | Format to return data: `markdown`, `raw`, `text`, `html2text`. Use `raw` for default page format.                                 |
| **proxy\_enabled**      | `bool`   | Enables high-performance proxies to avoid network-level blocking.                                                                 |
| **query\_selector**     | `string` | CSS query selector for content extraction from markup.                                                                            |
| **full\_resources**     | `bool`   | Downloads all resources linked to the website.                                                                                    |
| **request\_timeout**    | `int`    | Timeout in seconds for requests (5-60). Default is `30`.                                                                          |
| **run\_in\_background** | `bool`   | Runs the request in the background, useful for data storage and triggering dashboard crawls. No effect if `storageless` is set.   |



# Stagehand Tool
Source: https://docs.crewai.com/en/tools/web-scraping/stagehandtool

Web automation tool that integrates Stagehand with CrewAI for browser interaction and automation


# Overview

The `StagehandTool` integrates the [Stagehand](https://docs.stagehand.dev/get_started/introduction) framework with CrewAI, enabling agents to interact with websites and automate browser tasks using natural language instructions.


## Overview

Stagehand is a powerful browser automation framework built by Browserbase that allows AI agents to:

* Navigate to websites
* Click buttons, links, and other elements
* Fill in forms
* Extract data from web pages
* Observe and identify elements
* Perform complex workflows

The StagehandTool wraps the Stagehand Python SDK to provide CrewAI agents with browser control capabilities through three core primitives:

1. **Act**: Perform actions like clicking, typing, or navigating
2. **Extract**: Extract structured data from web pages
3. **Observe**: Identify and analyze elements on the page


## Prerequisites

Before using this tool, ensure you have:

1. A [Browserbase](https://www.browserbase.com/) account with API key and project ID
2. An API key for an LLM (OpenAI or Anthropic Claude)
3. The Stagehand Python SDK installed

Install the required dependency:

```bash  theme={null}
pip install stagehand-py
```


## Usage

### Basic Implementation

The StagehandTool can be implemented in two ways:

#### 1. Using Context Manager (Recommended)

<Tip>
  The context manager approach is recommended as it ensures proper cleanup of resources even if exceptions occur.
</Tip>

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import StagehandTool
from stagehand.schemas import AvailableModel


# Initialize the tool with your API keys using a context manager
with StagehandTool(
    api_key="your-browserbase-api-key",
    project_id="your-browserbase-project-id",
    model_api_key="your-llm-api-key",  # OpenAI or Anthropic API key
    model_name=AvailableModel.CLAUDE_3_7_SONNET_LATEST,  # Optional: specify which model to use
) as stagehand_tool:
    # Create an agent with the tool
    researcher = Agent(
        role="Web Researcher",
        goal="Find and summarize information from websites",
        backstory="I'm an expert at finding information online.",
        verbose=True,
        tools=[stagehand_tool],
    )

    # Create a task that uses the tool
    research_task = Task(
        description="Go to https://www.example.com and tell me what you see on the homepage.",
        agent=researcher,
    )

    # Run the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True,
    )

    result = crew.kickoff()
    print(result)
```

#### 2. Manual Resource Management

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import StagehandTool
from stagehand.schemas import AvailableModel


# Initialize the tool with your API keys
stagehand_tool = StagehandTool(
    api_key="your-browserbase-api-key",
    project_id="your-browserbase-project-id",
    model_api_key="your-llm-api-key",
    model_name=AvailableModel.CLAUDE_3_7_SONNET_LATEST,
)

try:
    # Create an agent with the tool
    researcher = Agent(
        role="Web Researcher",
        goal="Find and summarize information from websites",
        backstory="I'm an expert at finding information online.",
        verbose=True,
        tools=[stagehand_tool],
    )

    # Create a task that uses the tool
    research_task = Task(
        description="Go to https://www.example.com and tell me what you see on the homepage.",
        agent=researcher,
    )

    # Run the crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True,
    )

    result = crew.kickoff()
    print(result)
finally:
    # Explicitly clean up resources
    stagehand_tool.close()
```


## Command Types

The StagehandTool supports three different command types for specific web automation tasks:

### 1. Act Command

The `act` command type (default) enables webpage interactions like clicking buttons, filling forms, and navigation.

```python  theme={null}

# Perform an action (default behavior)
result = stagehand_tool.run(
    instruction="Click the login button", 
    url="https://example.com",
    command_type="act"  # Default, so can be omitted
)


# Fill out a form
result = stagehand_tool.run(
    instruction="Fill the contact form with name 'John Doe', email 'john@example.com', and message 'Hello world'", 
    url="https://example.com/contact"
)
```

### 2. Extract Command

The `extract` command type retrieves structured data from webpages.

```python  theme={null}

# Extract all product information
result = stagehand_tool.run(
    instruction="Extract all product names, prices, and descriptions", 
    url="https://example.com/products",
    command_type="extract"
)


# Extract specific information with a selector
result = stagehand_tool.run(
    instruction="Extract the main article title and content", 
    url="https://example.com/blog/article",
    command_type="extract",
    selector=".article-container"  # Optional CSS selector
)
```

### 3. Observe Command

The `observe` command type identifies and analyzes webpage elements.

```python  theme={null}

# Find interactive elements
result = stagehand_tool.run(
    instruction="Find all interactive elements in the navigation menu", 
    url="https://example.com",
    command_type="observe"
)


# Identify form fields
result = stagehand_tool.run(
    instruction="Identify all the input fields in the registration form", 
    url="https://example.com/register",
    command_type="observe",
    selector="#registration-form"
)
```


## Configuration Options

Customize the StagehandTool behavior with these parameters:

```python  theme={null}
stagehand_tool = StagehandTool(
    api_key="your-browserbase-api-key",
    project_id="your-browserbase-project-id",
    model_api_key="your-llm-api-key",
    model_name=AvailableModel.CLAUDE_3_7_SONNET_LATEST,
    dom_settle_timeout_ms=5000,  # Wait longer for DOM to settle
    headless=True,  # Run browser in headless mode
    self_heal=True,  # Attempt to recover from errors
    wait_for_captcha_solves=True,  # Wait for CAPTCHA solving
    verbose=1,  # Control logging verbosity (0-3)
)
```


## Best Practices

1. **Be Specific**: Provide detailed instructions for better results
2. **Choose Appropriate Command Type**: Select the right command type for your task
3. **Use Selectors**: Leverage CSS selectors to improve accuracy
4. **Break Down Complex Tasks**: Split complex workflows into multiple tool calls
5. **Implement Error Handling**: Add error handling for potential issues


## Troubleshooting

Common issues and solutions:

* **Session Issues**: Verify API keys for both Browserbase and LLM provider
* **Element Not Found**: Increase `dom_settle_timeout_ms` for slower pages
* **Action Failures**: Use `observe` to identify correct elements first
* **Incomplete Data**: Refine instructions or provide specific selectors


## Additional Resources

For questions about the CrewAI integration:

* Join Stagehand's [Slack community](https://stagehand.dev/slack)
* Open an issue in the [Stagehand repository](https://github.com/browserbase/stagehand)
* Visit [Stagehand documentation](https://docs.stagehand.dev/)



# CrewAI Documentation
Source: https://docs.crewai.com/index

Build collaborative AI agents, crews, and flows — production ready from day one.

<div
  style={{
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  gap: 20,
  textAlign: 'center',
  padding: '48px 24px',
  borderRadius: 16,
  background: 'linear-gradient(180deg, rgba(235,102,88,0.12) 0%, rgba(201,76,60,0.08) 100%)',
  border: '1px solid rgba(235,102,88,0.18)'
}}
>
  <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=439ca5dc63a1768cad7196005ff5636f" alt="CrewAI" width="250" height="100" data-og-width="375" data-og-height="114" data-path="images/crew_only_logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ea0aa43c49a743b0e50cdc8e453f9150 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3025604ad4e1a40cda55cbb4ec726f14 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=26b82b135ed2768dbb95a4f0ba4cd871 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=77d06e853a60d4a862cbceecf1dd3e93 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=da76ce1913c6086278df262cd9ad684a 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crew_only_logo.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7b7cb283aa3588d52cdf6ed4c2e09d30 2500w" />

  <div style={{ maxWidth: 720 }}>
    <h1 style={{ marginBottom: 12 }}>Ship multi‑agent systems with confidence</h1>

    <p style={{ color: 'var(--mint-text-2)' }}>
      Design agents, orchestrate crews, and automate flows with guardrails, memory, knowledge, and observability baked in.
    </p>
  </div>

  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12, justifyContent: 'center' }}>
    <a className="button button-primary" href="/en/quickstart">Get started</a>
    <a className="button" href="/en/changelog">View changelog</a>
    <a className="button" href="/en/api-reference/introduction">API Reference</a>
  </div>
</div>

<div style={{ marginTop: 32 }} />


## Get started

<CardGroup cols={3}>
  <Card title="Introduction" href="/en/introduction" icon="sparkles">
    Overview of CrewAI concepts, architecture, and what you can build with agents, crews, and flows.
  </Card>

  <Card title="Installation" href="/en/installation" icon="wrench">
    Install via `uv`, configure API keys, and set up the CLI for local development.
  </Card>

  <Card title="Quickstart" href="/en/quickstart" icon="rocket">
    Spin up your first crew in minutes. Learn the core runtime, project layout, and dev loop.
  </Card>
</CardGroup>


## Build the basics

<CardGroup cols={3}>
  <Card title="Agents" href="/en/concepts/agents" icon="users">
    Compose agents with tools, memory, knowledge, and structured outputs using Pydantic. Includes templates and best practices.
  </Card>

  <Card title="Flows" href="/en/concepts/flows" icon="arrow-progress">
    Orchestrate start/listen/router steps, manage state, persist execution, and resume long-running workflows.
  </Card>

  <Card title="Tasks & Processes" href="/en/concepts/tasks" icon="check">
    Define sequential, hierarchical, or hybrid processes with guardrails, callbacks, and human-in-the-loop triggers.
  </Card>
</CardGroup>


## Enterprise journey

<CardGroup cols={3}>
  <Card title="Deploy automations" href="/en/enterprise/features/automations" icon="server">
    Manage environments, redeploy safely, and monitor live runs directly from the Enterprise console.
  </Card>

  <Card title="Triggers & Flows" href="/en/enterprise/guides/automation-triggers" icon="bolt">
    Connect Gmail, Slack, Salesforce, and more. Pass trigger payloads into crews and flows automatically.
  </Card>

  <Card title="Team management" href="/en/enterprise/guides/team-management" icon="users-gear">
    Invite teammates, configure RBAC, and control access to production automations.
  </Card>
</CardGroup>


## What’s new

<CardGroup cols={2}>
  <Card title="Triggers overview" href="/en/enterprise/guides/automation-triggers" icon="sparkles">
    Unified overview for Gmail, Drive, Outlook, Teams, OneDrive, HubSpot, and more — now with sample payloads and crews.
  </Card>

  <Card title="Integration tools" href="/en/tools/integration/overview" icon="plug">
    Call existing CrewAI automations or Amazon Bedrock Agents directly from your crews using the updated integration toolkit.
  </Card>
</CardGroup>

<Callout title="Explore real-world patterns" icon="github">
  Browse the <a href="/en/examples/cookbooks">examples and cookbooks</a> for end-to-end reference implementations across agents, flows, and enterprise automations.
</Callout>


## Stay connected

<CardGroup cols={2}>
  <Card title="Star us on GitHub" href="https://github.com/crewAIInc/crewAI" icon="star">
    If CrewAI helps you ship faster, give us a star and share your builds with the community.
  </Card>

  <Card title="Join the community" href="https://community.crewai.com" icon="comments">
    Ask questions, showcase workflows, and request features alongside other builders.
  </Card>
</CardGroup>



# Agent Repositories
Source: https://docs.crewai.com/en/enterprise/features/agent-repositories

Learn how to use Agent Repositories to share and reuse your agents across teams and projects

Agent Repositories allow enterprise users to store, share, and reuse agent definitions across teams and projects. This feature enables organizations to maintain a centralized library of standardized agents, promoting consistency and reducing duplication of effort.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c2064b8fc57a99dfb8124909b64e0f9d" alt="Agent Repositories" data-og-width="2826" width="2826" data-og-height="1804" height="1804" data-path="images/enterprise/agent-repositories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=7757e2436d6e4e78349c5116b86ab130 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e9a1e9ed00dd1bcbba6f6fb132877c3c 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=ff4130e977495a27747b10d1591d36da 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=8579f5426a73f5fdc9fc9cb8e27b48c1 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=823d4391f0bc0f6e6dd110d1ad1a0936 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=3f7c480281557b5878d469cdb554bc8d 2500w" />
</Frame>


## Benefits of Agent Repositories

* **Standardization**: Maintain consistent agent definitions across your organization
* **Reusability**: Create an agent once and use it in multiple crews and projects
* **Governance**: Implement organization-wide policies for agent configurations
* **Collaboration**: Enable teams to share and build upon each other's work


## Creating and Use Agent Repositories

1. You must have an account at CrewAI, try the [free plan](https://app.crewai.com).
2. Create agents with specific roles and goals for your workflows.
3. Configure tools and capabilities for each specialized assistant.
4. Deploy agents across projects via visual interface or API integration.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=837a5d30ad32f8cd5e0bda08638c4c4d" alt="Agent Repositories" data-og-width="3434" width="3434" data-og-height="2266" height="2266" data-path="images/enterprise/create-agent-repository.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e9c4e5cb3e880f3fb28aa098d06eec7b 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1710435d332fcd75ac8ee3dc0fe37a0b 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=ccba8e2687317ebbf5aee8e29832d5eb 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=f7f51e57c76fea4f276be1c70e868620 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=0b74c722fb36c470635d3ade22c53cde 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=f69253ad1472a9f6bad48c3627f7b5d1 2500w" />
</Frame>

### Loading Agents from Repositories

You can load agents from repositories in your code using the `from_repository` parameter to run locally:

```python  theme={null}
from crewai import Agent


# Create an agent by loading it from a repository

# The agent is loaded with all its predefined configurations
researcher = Agent(
    from_repository="market-research-agent"
)
```

### Overriding Repository Settings

You can override specific settings from the repository by providing them in the configuration:

```python  theme={null}
researcher = Agent(
    from_repository="market-research-agent",
    goal="Research the latest trends in AI development",  # Override the repository goal
    verbose=True  # Add a setting not in the repository
)
```

### Example: Creating a Crew with Repository Agents

```python  theme={null}
from crewai import Crew, Agent, Task


# Load agents from repositories
researcher = Agent(
    from_repository="market-research-agent"
)

writer = Agent(
    from_repository="content-writer-agent"
)


# Create tasks
research_task = Task(
    description="Research the latest trends in AI",
    agent=researcher
)

writing_task = Task(
    description="Write a comprehensive report based on the research",
    agent=writer
)


# Create the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)


# Run the crew
result = crew.kickoff()
```

### Example: Using `kickoff()` with Repository Agents

You can also use repository agents directly with the `kickoff()` method for simpler interactions:

```python  theme={null}
from crewai import Agent
from pydantic import BaseModel
from typing import List


# Define a structured output format
class MarketAnalysis(BaseModel):
    key_trends: List[str]
    opportunities: List[str]
    recommendation: str


# Load an agent from repository
analyst = Agent(
    from_repository="market-analyst-agent",
    verbose=True
)


# Get a free-form response
result = analyst.kickoff("Analyze the AI market in 2025")
print(result.raw)  # Access the raw response


# Get structured output
structured_result = analyst.kickoff(
    "Provide a structured analysis of the AI market in 2025",
    response_format=MarketAnalysis
)


# Access structured data
print(f"Key Trends: {structured_result.pydantic.key_trends}")
print(f"Recommendation: {structured_result.pydantic.recommendation}")
```


## Best Practices

1. **Naming Convention**: Use clear, descriptive names for your repository agents
2. **Documentation**: Include comprehensive descriptions for each agent
3. **Tool Management**: Ensure that tools referenced by repository agents are available in your environment
4. **Access Control**: Manage permissions to ensure only authorized team members can modify repository agents


## Organization Management

To switch between organizations or see your current organization, use the CrewAI CLI:

```bash  theme={null}

# View current organization
crewai org current


# Switch to a different organization
crewai org switch <org_id>


# List all available organizations
crewai org list
```

<Note>
  When loading agents from repositories, you must be authenticated and switched to the correct organization. If you receive errors, check your authentication status and organization settings using the CLI commands above.
</Note>



# Automations
Source: https://docs.crewai.com/en/enterprise/features/automations

Manage, deploy, and monitor your live crews (automations) in one place.


## Overview

Automations is the live operations hub for your deployed crews. Use it to deploy from GitHub or a ZIP file, manage environment variables, re‑deploy when needed, and monitor the status of each automation.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a7d0655da82c70b0ca152715cb8253f4" alt="Automations Overview" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/automations-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=18456289664a18d4b83b2acdae616a44 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=4737cb32db15d7f121a1366ae5c80c0e 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=69473aff76b3ea16974be8226590d114 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a742c3a1f81537f0a2d9668e5671c1aa 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=6a9aed77a2491e2dc3da8f511f391487 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-overview.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c64e992c5464916085b9114abab0d7c0 2500w" />
</Frame>


## Deployment Methods

### Deploy from GitHub

Use this for version‑controlled projects and continuous deployment.

<Steps>
  <Step title="Connect GitHub">
    Click <b>Configure GitHub</b> and authorize access.
  </Step>

  <Step title="Select Repository & Branch">
    Choose the <b>Repository</b> and <b>Branch</b> you want to deploy from.
  </Step>

  <Step title="Enable Auto‑deploy (optional)">
    Turn on <b>Automatically deploy new commits</b> to ship updates on every push.
  </Step>

  <Step title="Add Environment Variables">
    Add secrets individually or use <b>Bulk View</b> for multiple variables.
  </Step>

  <Step title="Deploy">
    Click <b>Deploy</b> to create your live automation.
  </Step>
</Steps>

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=4fb72dc68799d5a0c35e2e74f1a7cc6c" alt="GitHub Deployment" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/deploy-from-github.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b15575b0b30c64e8b7a20de9e97468e5 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c041da5b5b79d38cb2a3f8d6f00e14a7 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=0783c12a6f83d09ce83e66aa34edcacd 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=d703da835283f7e73079ef66f664587c 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f73b6afc4c3c3075ded4da6559676fa3 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-github.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c3d82425923c1f57264b7cb5af9004b3 2500w" />
</Frame>

### Deploy from ZIP

Ship quickly without Git—upload a compressed package of your project.

<Steps>
  <Step title="Choose File">
    Select the ZIP archive from your computer.
  </Step>

  <Step title="Add Environment Variables">
    Provide any required variables or keys.
  </Step>

  <Step title="Deploy">
    Click <b>Deploy</b> to create your live automation.
  </Step>
</Steps>

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=8cea74868a553d34b0aa182ad5489099" alt="ZIP Deployment" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/deploy-from-zip.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=961637aa95a2795071b4a54e921f3f03 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=62994bfdf5667fc17880ed33c32a7aa6 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b0c4ef28de74989c1fdbf1076d12ba3c 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=19fe8b770051a0426f120d6b661a6f40 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a80e4bf6e8befdf57a5ea79840b45136 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/deploy-from-zip.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=61e870a88f47df3e282a134e754fc09d 2500w" />
</Frame>


## Automations Dashboard

The table lists all live automations with key details:

* **CREW**: Automation name
* **STATUS**: Online / Failed / In Progress
* **URL**: Endpoint for kickoff/status
* **TOKEN**: Automation token
* **ACTIONS**: Re‑deploy, delete, and more

Use the top‑right controls to filter and search:

* Search by name
* Filter by <b>Status</b>
* Filter by <b>Source</b> (GitHub / Studio / ZIP)

Once deployed, you can view the automation details and have the **Options** dropdown menu to `chat with this crew`, `Export React Component` and `Export as MCP`.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=f7fb571e8473f5cb7940c3e3bb34f95c" alt="Automations Table" data-og-width="2874" width="2874" data-og-height="932" height="932" data-path="images/enterprise/automations-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=5833733acf6f2e07d0a39abffe87de40 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=858a8b93744d4f23e07e9ec58227aac0 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e0fe6df6d821e1edc729681e8d314d22 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=cb68b81e23a169714985d93bb0913170 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=401736c16a6074de6b60de8234cbe206 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/automations-table.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1b9a5f852f474d6a68a5cf4dda5a0021 2500w" />
</Frame>


## Best Practices

* Prefer GitHub deployments for version control and CI/CD
* Use re‑deploy to roll forward after code or config updates or set it to auto-deploy on every push


## Related

<CardGroup cols={3}>
  <Card title="Deploy a Crew" href="/en/enterprise/guides/deploy-crew" icon="rocket">
    Deploy a Crew from GitHub or ZIP file.
  </Card>

  <Card title="Automation Triggers" href="/en/enterprise/guides/automation-triggers" icon="trigger">
    Trigger automations via webhooks or API.
  </Card>

  <Card title="Webhook Automation" href="/en/enterprise/guides/webhook-automation" icon="webhook">
    Stream real-time events and updates to your systems.
  </Card>
</CardGroup>



# Crew Studio
Source: https://docs.crewai.com/en/enterprise/features/crew-studio

Build new automations with AI assistance, a visual editor, and integrated testing.


## Overview

Crew Studio is an interactive, AI‑assisted workspace for creating new automations from scratch using natural language and a visual workflow editor.

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=78db59d2d246ccbc7a5c53c8dc2ac9b2" alt="Crew Studio Overview" data-og-width="3648" width="3648" data-og-height="2350" height="2350" data-path="images/enterprise/crew-studio-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c383766e8765b6d4182d2c1662918460 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=60a7e0e707a8c0d31c9eb93a368269de 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=d50594b48c0fdcbd3540f8aee66d4344 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=aaf07d2cc2dd54085f7eb1d21bf8cfa7 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=5d2139c2bcb6daa7a3a36ebf00534a98 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-overview.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=339e61bee7c9c7ae23cd9b66fdd900a9 2500w" />
</Frame>


## Prompt‑based Creation

* Describe the automation you want; the AI generates agents, tasks, and tools.
* Use voice input via the microphone icon if preferred.
* Start from built‑in prompts for common use cases.

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=10394b6192b729f9e861a43515e2c636" alt="Prompt Builder" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/crew-studio-prompt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=7d31c1d1bca45744f4d5e055d86cbdd7 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cbae3cfede1a4722288dc1c29fc97d3f 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bed1346b603a0a18843143956871ee33 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=eb225f848d28fc964429dc5987c1b876 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=67453056d7e4f061fcbb31761de175ef 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-prompt.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=53e224201427d7d1c7d8d5307e53f91f 2500w" />
</Frame>


## Visual Editor

The canvas reflects the workflow as nodes and edges with three supporting panels that allow you to configure the workflow easily without writing code; a.k.a. "**vibe coding AI Agents**".

You can use the drag-and-drop functionality to add agents, tasks, and tools to the canvas or you can use the chat section to build the agents. Both approaches share state and can be used interchangeably.

* **AI Thoughts (left)**: streaming reasoning as the workflow is designed
* **Canvas (center)**: agents and tasks as connected nodes
* **Resources (right)**: drag‑and‑drop components (agents, tasks, tools)

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=b112618b6609ddabc984955706b8365f" alt="Visual Canvas" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/crew-studio-canvas.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=5e67364f58e62f56c3dd83d19adf17ac 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=fe27e9cd021d667c2bc0f7efac754e07 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=10fdf0d907b6f1e0e70964ee50124830 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=0475255f908f761ed829d2f6290ee18a 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e93640b30b1fd9ee5a041ba382c29eda 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-canvas.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=62f10184fe117cfa557a8d20b4fc1a0c 2500w" />
</Frame>


## Execution & Debugging

Switch to the <b>Execution</b> view to run and observe the workflow:

* Event timeline
* Detailed logs (Details, Messages, Raw Data)
* Local test runs before publishing

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=6dc19227c8ad45cf3fed625a7b8ef47e" alt="Execution View" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/crew-studio-execution.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e4288a0a00bd999f45e32df6f800007d 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=43e7e0181a7a129cfff5b667e991b288 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=56527f1e66944e4c8c11862f8dd933c5 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c8e92593c0fb55e7f7460fb8275fe305 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=3fda256e5dc998b10226886c169acb05 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/crew-studio-execution.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=17c70892ffc922c9c08d2c32adeef311 2500w" />
</Frame>


## Publish & Export

* <b>Publish</b> to deploy a live automation
* <b>Download</b> source as a ZIP for local development or customization

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=576d6e2759a7289c0b5adf4e4511ec65" alt="Publish & Download" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/crew-studio-publish.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=946fdf9e05a3babe469dcac52fefc425 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=96e6b2614e47505918958ac78ba08f14 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=e956451644e619fd33da509b19359cde 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ab89721410f81fbb5ae83a3fb10ed642 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=4c9013c037ab344ff5cf4686fad22af3 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-publish.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=3a2a86194b24bd4522f581623bd262c0 2500w" />
</Frame>

Once published, you can view the automation details and have the **Options** dropdown menu to `chat with this crew`, `Export React Component` and `Export as MCP`.

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=8c5d967e43092ee26185f391b0554c46" alt="Published Automation" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/crew-studio-published.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=3bb1203eaf51478df59d39bd963b15ad 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=652849fcad1c2315395571f15900ffbb 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=21d1501b536a80102b737886bd2c2497 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=796e6b18972515c9410e855bed167e25 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=120a7f63e6e03ab3f5d25d98ae9e7eea 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/crew-studio-published.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=162ac4e5c227172b73ad4445585be713 2500w" />
</Frame>


## Best Practices

* Iterate quickly in Studio; publish only when stable
* Keep tools constrained to minimum permissions needed
* Use Traces to validate behavior and performance


## Related

<CardGroup cols={4}>
  <Card title="Enable Crew Studio" href="/en/enterprise/guides/enable-crew-studio" icon="palette">
    Enable Crew Studio.
  </Card>

  <Card title="Build a Crew" href="/en/enterprise/guides/build-crew" icon="paintbrush">
    Build a Crew.
  </Card>

  <Card title="Deploy a Crew" href="/en/enterprise/guides/deploy-crew" icon="rocket">
    Deploy a Crew from GitHub or ZIP file.
  </Card>

  <Card title="Export a React Component" href="/en/enterprise/guides/react-component-export" icon="download">
    Export a React Component.
  </Card>
</CardGroup>



# Hallucination Guardrail
Source: https://docs.crewai.com/en/enterprise/features/hallucination-guardrail

Prevent and detect AI hallucinations in your CrewAI tasks


## Overview

The Hallucination Guardrail is an enterprise feature that validates AI-generated content to ensure it's grounded in facts and doesn't contain hallucinations. It analyzes task outputs against reference context and provides detailed feedback when potentially hallucinated content is detected.


## What are Hallucinations?

AI hallucinations occur when language models generate content that appears plausible but is factually incorrect or not supported by the provided context. The Hallucination Guardrail helps prevent these issues by:

* Comparing outputs against reference context
* Evaluating faithfulness to source material
* Providing detailed feedback on problematic content
* Supporting custom thresholds for validation strictness


## Basic Usage

### Setting Up the Guardrail

```python  theme={null}
from crewai.tasks.hallucination_guardrail import HallucinationGuardrail
from crewai import LLM


# Basic usage - will use task's expected_output as context
guardrail = HallucinationGuardrail(
    llm=LLM(model="gpt-4o-mini")
)


# With explicit reference context
context_guardrail = HallucinationGuardrail(
    context="AI helps with various tasks including analysis and generation.",
    llm=LLM(model="gpt-4o-mini")
)
```

### Adding to Tasks

```python  theme={null}
from crewai import Task


# Create your task with the guardrail
task = Task(
    description="Write a summary about AI capabilities",
    expected_output="A factual summary based on the provided context",
    agent=my_agent,
    guardrail=guardrail  # Add the guardrail to validate output
)
```


## Advanced Configuration

### Custom Threshold Validation

For stricter validation, you can set a custom faithfulness threshold (0-10 scale):

```python  theme={null}

# Strict guardrail requiring high faithfulness score
strict_guardrail = HallucinationGuardrail(
    context="Quantum computing uses qubits that exist in superposition states.",
    llm=LLM(model="gpt-4o-mini"),
    threshold=8.0  # Requires score >= 8 to pass validation
)
```

### Including Tool Response Context

When your task uses tools, you can include tool responses for more accurate validation:

```python  theme={null}

# Guardrail with tool response context
weather_guardrail = HallucinationGuardrail(
    context="Current weather information for the requested location",
    llm=LLM(model="gpt-4o-mini"),
    tool_response="Weather API returned: Temperature 22°C, Humidity 65%, Clear skies"
)
```


## How It Works

### Validation Process

1. **Context Analysis**: The guardrail compares task output against the provided reference context
2. **Faithfulness Scoring**: Uses an internal evaluator to assign a faithfulness score (0-10)
3. **Verdict Determination**: Determines if content is faithful or contains hallucinations
4. **Threshold Checking**: If a custom threshold is set, validates against that score
5. **Feedback Generation**: Provides detailed reasons when validation fails

### Validation Logic

* **Default Mode**: Uses verdict-based validation (FAITHFUL vs HALLUCINATED)
* **Threshold Mode**: Requires faithfulness score to meet or exceed the specified threshold
* **Error Handling**: Gracefully handles evaluation errors and provides informative feedback


## Guardrail Results

The guardrail returns structured results indicating validation status:

```python  theme={null}

# Example of guardrail result structure
{
    "valid": False,
    "feedback": "Content appears to be hallucinated (score: 4.2/10, verdict: HALLUCINATED). The output contains information not supported by the provided context."
}
```

### Result Properties

* **valid**: Boolean indicating whether the output passed validation
* **feedback**: Detailed explanation when validation fails, including:
  * Faithfulness score
  * Verdict classification
  * Specific reasons for failure


## Integration with Task System

### Automatic Validation

When a guardrail is added to a task, it automatically validates the output before the task is marked as complete:

```python  theme={null}

# Task output validation flow
task_output = agent.execute_task(task)
validation_result = guardrail(task_output)

if validation_result.valid:
    # Task completes successfully
    return task_output
else:
    # Task fails with validation feedback
    raise ValidationError(validation_result.feedback)
```

### Event Tracking

The guardrail integrates with CrewAI's event system to provide observability:

* **Validation Started**: When guardrail evaluation begins
* **Validation Completed**: When evaluation finishes with results
* **Validation Failed**: When technical errors occur during evaluation


## Best Practices

### Context Guidelines

<Steps>
  <Step title="Provide Comprehensive Context">
    Include all relevant factual information that the AI should base its output on:

    ```python  theme={null}
    context = """
    Company XYZ was founded in 2020 and specializes in renewable energy solutions.
    They have 150 employees and generated $50M revenue in 2023.
    Their main products include solar panels and wind turbines.
    """
    ```
  </Step>

  <Step title="Keep Context Relevant">
    Only include information directly related to the task to avoid confusion:

    ```python  theme={null}
    # Good: Focused context
    context = "The current weather in New York is 18°C with light rain."

    # Avoid: Unrelated information
    context = "The weather is 18°C. The city has 8 million people. Traffic is heavy."
    ```
  </Step>

  <Step title="Update Context Regularly">
    Ensure your reference context reflects current, accurate information.
  </Step>
</Steps>

### Threshold Selection

<Steps>
  <Step title="Start with Default Validation">
    Begin without custom thresholds to understand baseline performance.
  </Step>

  <Step title="Adjust Based on Requirements">
    * **High-stakes content**: Use threshold 8-10 for maximum accuracy
    * **General content**: Use threshold 6-7 for balanced validation
    * **Creative content**: Use threshold 4-5 or default verdict-based validation
  </Step>

  <Step title="Monitor and Iterate">
    Track validation results and adjust thresholds based on false positives/negatives.
  </Step>
</Steps>


## Performance Considerations

### Impact on Execution Time

* **Validation Overhead**: Each guardrail adds \~1-3 seconds per task
* **LLM Efficiency**: Choose efficient models for evaluation (e.g., gpt-4o-mini)

### Cost Optimization

* **Model Selection**: Use smaller, efficient models for guardrail evaluation
* **Context Size**: Keep reference context concise but comprehensive
* **Caching**: Consider caching validation results for repeated content


## Troubleshooting

<Accordion title="Validation Always Fails">
  **Possible Causes:**

  * Context is too restrictive or unrelated to task output
  * Threshold is set too high for the content type
  * Reference context contains outdated information

  **Solutions:**

  * Review and update context to match task requirements
  * Lower threshold or use default verdict-based validation
  * Ensure context is current and accurate
</Accordion>

<Accordion title="False Positives (Valid Content Marked Invalid)">
  **Possible Causes:**

  * Threshold too high for creative or interpretive tasks
  * Context doesn't cover all valid aspects of the output
  * Evaluation model being overly conservative

  **Solutions:**

  * Lower threshold or use default validation
  * Expand context to include broader acceptable content
  * Test with different evaluation models
</Accordion>

<Accordion title="Evaluation Errors">
  **Possible Causes:**

  * Network connectivity issues
  * LLM model unavailable or rate limited
  * Malformed task output or context

  **Solutions:**

  * Check network connectivity and LLM service status
  * Implement retry logic for transient failures
  * Validate task output format before guardrail evaluation
</Accordion>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with hallucination guardrail configuration or troubleshooting.
</Card>



# Marketplace
Source: https://docs.crewai.com/en/enterprise/features/marketplace

Discover, install, and govern reusable assets for your enterprise crews.


## Overview

The Marketplace provides a curated surface for discovering integrations, internal tools, and reusable assets that accelerate crew development.

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=77786aca40c58c31775cb4de35b26d54" alt="Marketplace Overview" data-og-width="3040" width="3040" data-og-height="2266" height="2266" data-path="images/enterprise/marketplace-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ae939d5b2f6f4d087498ec8a3a342ea7 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6113d807f99c7de5a4ac3012518dbfcc 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=9e21e42a266f06cb864455b8935f54fc 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=41b47b8f0c3694766edfffe121f81402 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b8d75afbe1aeb98abc3cfd55d90ebce0 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-overview.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a798183edcdfddb19e6ae6b7ab0ab76b 2500w" />
</Frame>


## Discoverability

* Browse by category and capability
* Search for assets by name or keyword


## Install & Enable

* One‑click install for approved assets
* Enable or disable per crew as needed
* Configure required environment variables and scopes

<Frame>
    <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cc15b069d1d4da8555e9630e1e874346" alt="Install & Configure" data-og-width="2672" width="2672" data-og-height="2266" height="2266" data-path="images/enterprise/marketplace-install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cfdaa8690cb6651c51c5ba579364fb7a 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=2ddf18661fb7c7ad08e3f1029311813f 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=b0c3ee1f87a674b1ae31956a201e4b10 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=cedd73cab5194bd1381d594d0b102e2a 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=acfc5d304485f464f7bb5780c97ab237 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/marketplace-install.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=1ea74be846d2c2eaf37cd372273f6347 2500w" />
</Frame>

You can also download the templates directly from the marketplace by clicking on the `Download` button so
you can use them locally or refine them to your needs.


## Related

<CardGroup cols={3}>
  <Card title="Tools & Integrations" href="/en/enterprise/features/tools-and-integrations" icon="wrench">
    Connect external apps and manage internal tools your agents can use.
  </Card>

  <Card title="Tool Repository" href="/en/enterprise/features/tool-repository" icon="toolbox">
    Publish and install tools to enhance your crews' capabilities.
  </Card>

  <Card title="Agents Repository" href="/en/enterprise/features/agent-repositories" icon="people-group">
    Store, share, and reuse agent definitions across teams and projects.
  </Card>
</CardGroup>



# Role-Based Access Control (RBAC)
Source: https://docs.crewai.com/en/enterprise/features/rbac

Control access to crews, tools, and data with roles, scopes, and granular permissions.


## Overview

RBAC in CrewAI AMP enables secure, scalable access management through a combination of organization‑level roles and automation‑level visibility controls.

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=31b2661025e9813f32938f9d583228b5" alt="RBAC overview in CrewAI AMP" data-og-width="1365" width="1365" data-og-height="1044" height="1044" data-path="images/enterprise/users_and_roles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c3863373e71e9e7190b4e68024e82ad6 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e9bfbec405004555d4a862a97e29945e 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8b3c5a5d5a1ba5417537c6ae6cae8f1c 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=50ba9cfdd73790c67ed3a7cce74d4f39 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=aed9da1d5c9044e026f1674463f9adc2 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/users_and_roles.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=64a041f4e9ee05456c86d7259cef7e61 2500w" />
</Frame>


## Users and Roles

Each member in your CrewAI workspace is assigned a role, which determines their access across various features.

You can:

* Use predefined roles (Owner, Member)
* Create custom roles tailored to specific permissions
* Assign roles at any time through the settings panel

You can configure users and roles in Settings → Roles.

<Steps>
  <Step title="Open Roles settings">
    Go to <b>Settings → Roles</b> in CrewAI AMP.
  </Step>

  <Step title="Choose a role type">
    Use a predefined role (<b>Owner</b>, <b>Member</b>) or click <b>Create role</b> to define a custom one.
  </Step>

  <Step title="Assign to members">
    Select users and assign the role. You can change this anytime.
  </Step>
</Steps>

### Configuration summary

| Area                  | Where to configure                 | Options                                 |
| :-------------------- | :--------------------------------- | :-------------------------------------- |
| Users & Roles         | Settings → Roles                   | Predefined: Owner, Member; Custom roles |
| Automation visibility | Automation → Settings → Visibility | Private; Whitelist users/roles          |


## Automation‑level Access Control

In addition to organization‑wide roles, CrewAI Automations support fine‑grained visibility settings that let you restrict access to specific automations by user or role.

This is useful for:

* Keeping sensitive or experimental automations private
* Managing visibility across large teams or external collaborators
* Testing automations in isolated contexts

Deployments can be configured as private, meaning only whitelisted users and roles will be able to:

* View the deployment
* Run it or interact with its API
* Access its logs, metrics, and settings

The organization owner always has access, regardless of visibility settings.

You can configure automation‑level access control in Automation → Settings → Visibility tab.

<Steps>
  <Step title="Open Visibility tab">
    Navigate to <b>Automation → Settings → Visibility</b>.
  </Step>

  <Step title="Set visibility">
    Choose <b>Private</b> to restrict access. The organization owner always retains access.
  </Step>

  <Step title="Whitelist access">
    Add specific users and roles allowed to view, run, and access logs/metrics/settings.
  </Step>

  <Step title="Save and verify">
    Save changes, then confirm that non‑whitelisted users cannot view or run the automation.
  </Step>
</Steps>

### Private visibility: access outcomes

| Action                       | Owner | Whitelisted user/role | Not whitelisted |
| :--------------------------- | :---- | :-------------------- | :-------------- |
| View automation              | ✓     | ✓                     | ✗               |
| Run automation/API           | ✓     | ✓                     | ✗               |
| Access logs/metrics/settings | ✓     | ✓                     | ✗               |

<Tip>
  The organization owner always has access. In private mode, only whitelisted users and roles can view, run, and access logs/metrics/settings.
</Tip>

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=48e3dd12b9d55da6f7adc82ea80be56d" alt="Automation Visibility settings in CrewAI AMP" data-og-width="2028" width="2028" data-og-height="1498" height="1498" data-path="images/enterprise/visibility.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=382d272d44871f509846140dc972592e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6d6ba4cf2fcc360c7ce05266f5cc27e9 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9fff488a36423a05ccb3f8e592ffd07 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=00471ecc85192b53abbcd64416e2b624 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9008ee6b24abd22593938021d2093174 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/visibility.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27fde319cbc6fae3e4c1e0a9044c264f 2500w" />
</Frame>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with RBAC questions.
</Card>



# Tools & Integrations
Source: https://docs.crewai.com/en/enterprise/features/tools-and-integrations

Connect external apps and manage internal tools your agents can use.


## Overview

Tools & Integrations is the central hub for connecting third‑party apps and managing internal tools that your agents can use at runtime.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c31a4b9031f0f517fdce3baa48471f58" alt="Tools & Integrations Overview" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/enterprise/crew_connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9e592d155e388bb67d003b26884dc081 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=0c8aa20b2dc82de9ea3d2da6920e4195 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=782fe13ea53120f6d2f8e643a7a7b838 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780cd735280c569e6e93caa8262b12d1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=08bfe86a58ca08ec36ae67dca4aa5cf9 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e2bbe3b0fe0234001e030b501fa4d76c 2500w" />
</Frame>


## Explore

<Tabs>
  <Tab title="Integrations" icon="plug">
    ## Agent Apps (Integrations)

    Connect enterprise‑grade applications (e.g., Gmail, Google Drive, HubSpot, Slack) via OAuth to enable agent actions.

    <Steps>
      <Step title="Connect">
        Click <b>Connect</b> on an app and complete OAuth.
      </Step>

      <Step title="Configure">
        Optionally adjust scopes, triggers, and action availability.
      </Step>

      <Step title="Use in Agents">
        Connected services become available as tools for your agents.
      </Step>
    </Steps>

    <Frame>
            <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=43abfc4eae390e308bed0b8e15238a54" alt="Integrations Grid" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/agent-apps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e5e30bd3d904891d5c2c4d9d6182002a 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a146a0d69ff2309e7eac8d2f07da1cba 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c85a4a7ebe043fc6819957ff51f3ef0d 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=4ea77f15a4fe2671267f7e3668615970 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=7835e5d197251834d83a6dd7c7813d0a 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-apps.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=06cea3ae58b49b925566a7962585b148 2500w" />
    </Frame>

    ### Connect your Account

    1. Go to <Link href="https://app.crewai.com/crewai_plus/connectors">Integrations</Link>
    2. Click <b>Connect</b> on the desired service
    3. Complete the OAuth flow and grant scopes
    4. Copy your Enterprise Token from <Link href="https://app.crewai.com/crewai_plus/settings/integrations">Integration Settings</Link>

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4e7388bcb76f3f8aa6c6802dd0a98956" alt="Enterprise Token" data-og-width="2264" width="2264" data-og-height="540" height="540" data-path="images/enterprise/enterprise_action_auth_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f3d1bd9cd9783d3e83f42ab6ee42d26c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=df1514f746270a9ae5fc252c07806761 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a16c5c7986003435afad4106ccbaa7c5 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=81dabefb14a7f604a68c74eff26dff90 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2833c9f202a291f2cf022026db261793 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/enterprise_action_auth_token.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=eeece6b187aebd0ec9e8af29d8bfc889 2500w" />
    </Frame>

    ### Install Integration Tools

    To use the integrations locally, you need to install the latest `crewai-tools` package.

    ```bash  theme={null}
    uv add crewai-tools
    ```

    ### Environment Variable Setup

    <Note>
      To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
    </Note>

    ```bash  theme={null}
    export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
    ```

    Or add it to your `.env` file:

    ```
    CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
    ```

    ### Usage Example

    <Tip>
      Use the new streamlined approach to integrate enterprise apps. Simply specify the app and its actions directly in the Agent configuration.
    </Tip>

    ```python  theme={null}
    from crewai import Agent, Task, Crew

    # Create an agent with Gmail capabilities
    email_agent = Agent(
        role="Email Manager",
        goal="Manage and organize email communications",
        backstory="An AI assistant specialized in email management and communication.",
        apps=['gmail', 'gmail/send_email']  # Using canonical name 'gmail'
    )

    # Task to send an email
    email_task = Task(
        description="Draft and send a follow-up email to john@example.com about the project update",
        agent=email_agent,
        expected_output="Confirmation that email was sent successfully"
    )

    # Run the task
    crew = Crew(
        agents=[email_agent],
        tasks=[email_task]
    )

    # Run the crew
    crew.kickoff()
    ```

    ### Filtering Tools

    ```python  theme={null}
    from crewai import Agent, Task, Crew

    # Create agent with specific Gmail actions only
    gmail_agent = Agent(
        role="Gmail Manager",
        goal="Manage gmail communications and notifications",
        backstory="An AI assistant that helps coordinate gmail communications.",
        apps=['gmail/fetch_emails']  # Using canonical name with specific action
    )

    notification_task = Task(
        description="Find the email from john@example.com",
        agent=gmail_agent,
        expected_output="Email found from john@example.com"
    )

    crew = Crew(
        agents=[gmail_agent],
        tasks=[notification_task]
    )
    ```

    On a deployed crew, you can specify which actions are available for each integration from the service settings page.

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2e689397eabeacd23d0c226ff40566fd" alt="Filter Actions" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/enterprise/filtering_enterprise_action_tools.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6045a09da61d593e04098a4627777c9 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=257b1eea0bca2def5d43df960a4171ef 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6b9b8686a4fec0c0cdd8c7aa9acd4695 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e16c10384300b96d4962e2847f6633bf 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6de59b5409513b100c5cd36a69701e5f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/filtering_enterprise_action_tools.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=32ed2ecc611c989e0fe9d8cb351740fa 2500w" />
    </Frame>

    ### Scoped Deployments (multi‑user orgs)

    You can scope each integration to a specific user. For example, a crew that connects to Google can use a specific user’s Gmail account.

    <Tip>
      Useful when different teams/users must keep data access separated.
    </Tip>

    Use the `user_bearer_token` to scope authentication to the requesting user. If the user isn’t logged in, the crew won’t use connected integrations. Otherwise it falls back to the default bearer token configured for the deployment.

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d62aed15392f304cfc16bfa38ab91a54" alt="User Bearer Token" data-og-width="532" width="532" data-og-height="732" height="732" data-path="images/enterprise/user_bearer_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=efe731a753ab7efb10a65f648fba75a7 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=232d8d25cd253f071856f53425cc40c2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=df7b4956ab7668c23380394d8ce0f6c1 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=523850a6b69b5dd47ceaca3681f0ac35 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=561dcfa07461ecc8c39cd80865802d5e 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/user_bearer_token.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=06fbc44278b7d23fd2befd6b745622e7 2500w" />
    </Frame>

    <div id="catalog" />

    ### Catalog

    #### Communication & Collaboration

    * Gmail — Manage emails and drafts
    * Slack — Workspace notifications and alerts
    * Microsoft — Office 365 and Teams integration

    #### Project Management

    * Jira — Issue tracking and project management
    * ClickUp — Task and productivity management
    * Asana — Team task and project coordination
    * Notion — Page and database management
    * Linear — Software project and bug tracking
    * GitHub — Repository and issue management

    #### Customer Relationship Management

    * Salesforce — CRM account and opportunity management
    * HubSpot — Sales pipeline and contact management
    * Zendesk — Customer support ticket management

    #### Business & Finance

    * Stripe — Payment processing and customer management
    * Shopify — E‑commerce store and product management

    #### Productivity & Storage

    * Google Sheets — Spreadsheet data synchronization
    * Google Calendar — Event and schedule management
    * Box — File storage and document management

    …and more to come!
  </Tab>

  <Tab title="Internal Tools" icon="toolbox">
    ## Internal Tools

    Create custom tools locally, publish them on CrewAI AMP Tool Repository and use them in your agents.

    <Tip>
      Before running the commands below, make sure you log in to your CrewAI AMP account by running this command:

      ```bash  theme={null}
      crewai login
      ```
    </Tip>

    <Frame>
            <img src="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=b31a82341fb4dcd784c2ecfc1c3d576c" alt="Internal Tool Detail" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/tools-integrations-internal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=280&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=4b7ea6075327365b2486b405db715126 280w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=560&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=857f73fdff530aa6c7d801267e3cbc8a 560w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=840&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=2e844aa05d5c5367f9f8c14deeb78ad7 840w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=1100&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=fd26df60df1b528fc1644e08289738da 1100w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=1650&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=11d2cd7d7e38cb9cfeed2e23c4e3fe87 1650w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tools-integrations-internal.png?w=2500&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=cba0837b7f2039f9c59cdafb81cc53b9 2500w" />
    </Frame>

    <Steps>
      <Step title="Create">
        Create a new tool locally.

        ```bash  theme={null}
        crewai tool create your-tool
        ```
      </Step>

      <Step title="Publish">
        Publish the tool to the CrewAI AMP Tool Repository.

        ```bash  theme={null}
        crewai tool publish
        ```
      </Step>

      <Step title="Install">
        Install the tool from the CrewAI AMP Tool Repository.

        ```bash  theme={null}
        crewai tool install your-tool
        ```
      </Step>
    </Steps>

    Manage:

    * Name and description
    * Visibility (Private / Public)
    * Required environment variables
    * Version history and downloads
    * Team and role access

    <Frame>
            <img src="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=1896ebecec784bc15411a0309a0cf973" alt="Internal Tool Detail" data-og-width="3648" width="3648" data-og-height="2266" height="2266" data-path="images/enterprise/tool-configs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=280&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=fa0c14f9439ebad25474aa422f8b1bd7 280w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=560&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=d135d69d85a0ccb8d99403def21c8529 560w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=840&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=f65ac1de79956f4178a610be29c6e212 840w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=1100&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=3b13a8181819dbf6b07ed52f239f588a 1100w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=1650&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=0dc0e377941d126e06fa76cb176b70e2 1650w, https://mintcdn.com/crewai/VGZ5vPOL3DPMThlg/images/enterprise/tool-configs.png?w=2500&fit=max&auto=format&n=VGZ5vPOL3DPMThlg&q=85&s=53bf0fa4215eb47d5959d1c46a232db1 2500w" />
    </Frame>
  </Tab>
</Tabs>


## Related

<CardGroup cols={2}>
  <Card title="Tool Repository" href="/en/enterprise/features/tool-repository" icon="toolbox">
    Create, publish, and version custom tools for your organization.
  </Card>

  <Card title="Webhook Automation" href="/en/enterprise/guides/webhook-automation" icon="bolt">
    Automate workflows and integrate with external platforms and services.
  </Card>
</CardGroup>



---

**Navigation:** [← Previous](./05-overview.md) | [Index](./index.md) | [Next →](./07-traces.md)
