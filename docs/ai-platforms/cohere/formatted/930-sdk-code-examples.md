---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SDK Code Examples

```typescript Default
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'Tell me about LLMs',
      },
    ],
  });

  console.log(response);
})();
```
```python Default
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "Tell me about LLMs"}],
)

print(response)
```
```python Async
import cohere
import asyncio

co = cohere.AsyncClientV2()

async def main():
    response = await co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": "Tell me about LLMs"}],
    )
    print(response)

asyncio.run(main())
```
```go Default
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Tell me about LLMs",
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```
```java Default
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.*;
import java.util.List;

public class Default {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(UserMessageContent.of("Tell me about LLMs"))
                                    .build())))
                    .build());

    System.out.println(response);
  }
}
```
```ruby Default
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```
```php Default
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    {
      "role": "user",
      "content": "Tell me about LLMs"
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp Default
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Tell me about LLMs\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift Default
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Tell me about LLMs"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
```typescript Documents
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content: 'Who is more popular: Nsync or Backstreet Boys?',
      },
    ],
    documents: [
      {
        data: {
          title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
          snippet:
            '↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.',
        },
      },
      {
        data: {
          title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
          snippet:
            "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
        },
      },
      {
        data: {
          title: 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters',
          snippet:
            " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
        },
      },
      {
        data: {
          title: 'CSPC: NSYNC Popularity Analysis - ChartMasters',
          snippet:
            " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
        },
      },
    ],
  });

  console.log(response);
})();
```
```python Documents
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-03-2025",
    messages=[{
        "role": "user", 
        "content": "Who is more popular: Nsync or Backstreet Boys?"
    }],
    documents=[
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
            }
        },
        {
            "data":  {
                "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
                "snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
            }
        },
        {
            "data":  {
                "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
                "snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
            }
        }
    ],
)

print(response)
```
```java Documents
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.resources.v2.types.V2ChatRequestDocumentsItem;
import com.cohere.api.types.*;
import java.util.List;
import java.util.Map;

public class Documents {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-03-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            "Who is more popular: Nsync or Backstreet Boys?"))
                                    .build())))
                    .documents(
                        List.of(
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: Backstreet Boys Popularity Analysis -"
                                                + " ChartMasters",
                                            "snippet",
                                            "↓ Skip to Main Content\n\n"
                                                + "Music industry – One step closer to being"
                                                + " accurate\n\n"
                                                + "CSPC: Backstreet Boys Popularity Analysis\n\n"
                                                + "Hernán Lopez Posted on February 9, 2017 Posted"
                                                + " in CSPC 72 Comments Tagged with Backstreet"
                                                + " Boys, Boy band\n\n"
                                                + "At one point, Backstreet Boys defined success:"
                                                + " massive albums sales across the globe, great"
                                                + " singles sales, plenty of chart topping"
                                                + " releases, hugely hyped tours and tremendous"
                                                + " media coverage.\n\n"
                                                + "It is true that they benefited from"
                                                + " extraordinarily good market conditions in all"
                                                + " markets. After all, the all-time record year"
                                                + " for the music business, as far as revenues in"
                                                + " billion dollars are concerned, was actually"
                                                + " 1999. That is, back when this five men group"
                                                + " was at its peak."))
                                    .build()),
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: NSYNC Popularity Analysis - ChartMasters",
                                            "snippet",
                                            "↓ Skip to Main Content\n\n"
                                                + "Music industry – One step closer to being"
                                                + " accurate\n\n"
                                                + "CSPC: NSYNC Popularity Analysis\n\n"
                                                + "MJD Posted on February 9, 2018 Posted in CSPC"
                                                + " 27 Comments Tagged with Boy band, N'Sync\n\n"
                                                + "At the turn of the millennium three teen acts"
                                                + " were huge in the US, the Backstreet Boys,"
                                                + " Britney Spears and NSYNC. The latter is the"
                                                + " only one we haven't study so far. It took 15"
                                                + " years and Adele to break their record of 2,4"
                                                + " million units sold of No Strings Attached in"
                                                + " its first week alone.\n\n"
                                                + "It wasn't a fluke, as the second fastest"
                                                + " selling album of the Soundscan era prior 2015,"
                                                + " was also theirs since Celebrity debuted with"
                                                + " 1,88 million units sold."))
                                    .build()),
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: Backstreet Boys Popularity Analysis -"
                                                + " ChartMasters",
                                            "snippet",
                                            " 1997, 1998, 2000 and 2001 also rank amongst some"
                                                + " of the very best years.\n\n"
                                                + "Yet the way many music consumers – especially"
                                                + " teenagers and young women's – embraced their"
                                                + " output deserves its own chapter. If Jonas"
                                                + " Brothers and more recently One Direction"
                                                + " reached a great level of popularity during the"
                                                + " past decade, the type of success achieved by"
                                                + " Backstreet Boys is in a completely different"
                                                + " level as they really dominated the business"
                                                + " for a few years all over the world, including"
                                                + " in some countries that were traditionally hard"
                                                + " to penetrate for Western artists.\n\n"
                                                + "We will try to analyze the extent of that"
                                                + " hegemony with this new article with final"
                                                + " results which will more than surprise many"
                                                + " readers."))
                                    .build()),
                            V2ChatRequestDocumentsItem.of(
                                Document.builder()
                                    .data(
                                        Map.of(
                                            "title",
                                            "CSPC: NSYNC Popularity Analysis - ChartMasters",
                                            "snippet",
                                            " Was the teen group led by Justin Timberlake"
                                                + " really that big? Was it only in the US where"
                                                + " they found success? Or were they a global"
                                                + " phenomenon?\n\n"
                                                + "As usual, I'll be using the Commensurate Sales"
                                                + " to Popularity Concept in order to relevantly"
                                                + " gauge their results. This concept will not"
                                                + " only bring you sales information for all"
                                                + " NSYNC's albums, physical and download singles,"
                                                + " as well as audio and video streaming, but it"
                                                + " will also determine their true popularity. If"
                                                + " you are not yet familiar with the CSPC method,"
                                                + " the next page explains it with a short video."
                                                + " I fully recommend watching the video before"
                                                + " getting into the sales figures."))
                                    .build())))
                    .build());
    System.out.println(response);
  }
}
```
```go Documents
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Who is more popular: Nsync or Backstreet Boys?",
						},
					},
				},
			},
			Documents: []*cohere.V2ChatRequestDocumentsItem{
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
							"snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: Backstreet Boys Popularity Analysis\n\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\n\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\n\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: NSYNC Popularity Analysis - ChartMasters",
							"snippet": "↓ Skip to Main Content\n\nMusic industry – One step closer to being accurate\n\nCSPC: NSYNC Popularity Analysis\n\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\n\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven't study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\n\nIt wasn't a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
							"snippet": " 1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\n\nYet the way many music consumers – especially teenagers and young women's – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\n\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.",
						},
					},
				},
				{
					Document: &cohere.Document{
						Data: map[string]interface{}{
							"title":   "CSPC: NSYNC Popularity Analysis - ChartMasters",
							"snippet": " Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\n\nAs usual, I'll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC's albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.",
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```
```ruby Documents
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```
```php Documents
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
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
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
      }
    },
    {
      "data": {
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N\'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
      }
    },
    {
      "data": {
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
      }
    },
    {
      "data": {
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
      }
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp Documents
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-a-03-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Who is more popular: Nsync or Backstreet Boys?\"\n    }\n  ],\n  \"documents\": [\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: Backstreet Boys Popularity Analysis\\n\\nHernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band\\n\\nAt one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.\\n\\nIt is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"↓ Skip to Main Content\\n\\nMusic industry – One step closer to being accurate\\n\\nCSPC: NSYNC Popularity Analysis\\n\\nMJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync\\n\\nAt the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.\\n\\nIt wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: Backstreet Boys Popularity Analysis - ChartMasters\",\n        \"snippet\": \"1997, 1998, 2000 and 2001 also rank amongst some of the very best years.\\nYet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.\\n\\nWe will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers.\"\n      }\n    },\n    {\n      \"data\": {\n        \"content\": \"CSPC: NSYNC Popularity Analysis - ChartMasters\",\n        \"snippet\": \"Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?\\nAs usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift Documents
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-a-03-2025",
  "messages": [
    [
      "role": "user",
      "content": "Who is more popular: Nsync or Backstreet Boys?"
    ]
  ],
  "documents": [["data": [
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: Backstreet Boys Popularity Analysis

Hernán Lopez Posted on February 9, 2017 Posted in CSPC 72 Comments Tagged with Backstreet Boys, Boy band

At one point, Backstreet Boys defined success: massive albums sales across the globe, great singles sales, plenty of chart topping releases, hugely hyped tours and tremendous media coverage.

It is true that they benefited from extraordinarily good market conditions in all markets. After all, the all-time record year for the music business, as far as revenues in billion dollars are concerned, was actually 1999. That is, back when this five men group was at its peak."
      ]], ["data": [
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "↓ Skip to Main Content

Music industry – One step closer to being accurate

CSPC: NSYNC Popularity Analysis

MJD Posted on February 9, 2018 Posted in CSPC 27 Comments Tagged with Boy band, N'Sync

At the turn of the millennium three teen acts were huge in the US, the Backstreet Boys, Britney Spears and NSYNC. The latter is the only one we haven’t study so far. It took 15 years and Adele to break their record of 2,4 million units sold of No Strings Attached in its first week alone.

It wasn’t a fluke, as the second fastest selling album of the Soundscan era prior 2015, was also theirs since Celebrity debuted with 1,88 million units sold."
      ]], ["data": [
        "content": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
        "snippet": "1997, 1998, 2000 and 2001 also rank amongst some of the very best years.
Yet the way many music consumers – especially teenagers and young women’s – embraced their output deserves its own chapter. If Jonas Brothers and more recently One Direction reached a great level of popularity during the past decade, the type of success achieved by Backstreet Boys is in a completely different level as they really dominated the business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists.

We will try to analyze the extent of that hegemony with this new article with final results which will more than surprise many readers."
      ]], ["data": [
        "content": "CSPC: NSYNC Popularity Analysis - ChartMasters",
        "snippet": "Was the teen group led by Justin Timberlake really that big? Was it only in the US where they found success? Or were they a global phenomenon?
As usual, I’ll be using the Commensurate Sales to Popularity Concept in order to relevantly gauge their results. This concept will not only bring you sales information for all NSYNC‘s albums, physical and download singles, as well as audio and video streaming, but it will also determine their true popularity. If you are not yet familiar with the CSPC method, the next page explains it with a short video. I fully recommend watching the video before getting into the sales figures."
      ]]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
```typescript Tools
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-03-2025',
    messages: [
      {
        role: 'user',
        content:
          "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
      },
    ],
    tools: [
      {
        type: 'function',
        function: {
          name: 'query_daily_sales_report',
          description:
            'Connects to a database to retrieve overall sales volumes and sales information for a given day.',
          parameters: {
            type: 'object',
            properties: {
              day: {
                description: 'Retrieves sales data for this day, formatted as YYYY-MM-DD.',
                type: 'string',
              },
            },
            required: ['day'],
          },
        },
      },
      {
        type: 'function',
        function: {
          name: 'query_product_catalog',
          description:
            'Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.',
          parameters: {
            type: 'object',
            properties: {
              category: {
                description:
                  'Retrieves product information data for all products in this category.',
                type: 'string',
              },
            },
            required: ['category'],
          },
        },
      },
    ],
  });

  console.log(response);
})();
```
```python Tools
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-reasoning-08-2025",
    messages=[
        {
            "role": "user",
            "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
        }
    ],
    tools=[
        cohere.ToolV2(
            type="function",
            function={
                "name": "query_daily_sales_report",
                "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "day": {
                            "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
                            "type": "string",
                        }
                    },
                    "required": ["day"],
                },
            },
        ),
        cohere.ToolV2(
            type="function",
            function={
                "name": "query_product_catalog",
                "description": "Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "description": "Retrieves product information data for all products in this category.",
                            "type": "string",
                        }
                    },
                    "required": ["category"],
                },
            },
        ),
    ],
)

print(response)
```
```java Tools
/* (C)2024 */
package chatv2post;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.*;
import java.util.List;
import java.util.Map;

public class Tools {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-reasoning-08-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            "Can you provide a sales summary for 29th September"
                                                + " 2023, and also give me some details about the"
                                                + " products in the 'Electronics' category, for"
                                                + " example their prices and stock levels?"))
                                    .build())))
                    .tools(
                        List.of(
                            ToolV2.builder()
                                .type("function")
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_daily_sales_report")
                                        .description(
                                            "Connects to a database to retrieve overall sales"
                                                + " volumes and sales information for a given"
                                                + " day.")
                                        .parameters(
                                            Map.of(
                                                "type",
                                                "object",
                                                "properties",
                                                Map.of(
                                                    "day",
                                                    Map.of(
                                                        "description",
                                                        "Retrieves sales data for this day,"
                                                            + " formatted as YYYY-MM-DD.",
                                                        "type",
                                                        "string")),
                                                "required",
                                                List.of("day")))
                                        .build())
                                .build(),
                            ToolV2.builder()
                                .type("function")
                                .function(
                                    ToolV2Function.builder()
                                        .name("query_product_catalog")
                                        .description(
                                            "Connects to a product catalog with information"
                                                + " about all the products being sold, including"
                                                + " categories, prices, and stock levels.")
                                        .parameters(
                                            Map.of(
                                                "type",
                                                "object",
                                                "properties",
                                                Map.of(
                                                    "category",
                                                    Map.of(
                                                        "description",
                                                        "Retrieves product information data for all"
                                                            + " products in this category.",
                                                        "type",
                                                        "string")),
                                                "required",
                                                List.of("category")))
                                        .build())
                                .build()))
                    .build());

    System.out.println(response);
  }
}
```
```go Tools
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-03-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							String: "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?",
						},
					},
				},
			},
			Tools: []*cohere.ToolV2{
				{
					Type: cohere.String("function"),
					Function: &cohere.ToolV2Function{
						Name:        "query_daily_sales_report",
						Description: cohere.String("Connects to a database to retrieve overall sales volumes and sales information for a given day."),
						Parameters: map[string]interface{}{
							"type": "object",
							"properties": map[string]interface{}{
								"day": map[string]interface{}{
									"type":        "string",
									"description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
								},
							},
							"required": []string{"day"},
						},
					},
				},
				{
					Type: cohere.String("function"),
					Function: &cohere.ToolV2Function{
						Name:        "query_product_catalog",
						Description: cohere.String("Connects to a product catalog with information about all the products being sold, including categories, prices, and stock levels."),
						Parameters: map[string]interface{}{
							"type": "object",
							"properties": map[string]interface{}{
								"category": map[string]interface{}{
									"type":        "string",
									"description": "Retrieves product information data for all products in this category.",
								},
							},
							"required": []string{"category"},
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```
```ruby Tools
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-r\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"day\"\n          ],\n          \"x-fern-type-name\": \"tools-by6k68\"\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"category\"\n          ],\n          \"x-fern-type-name\": \"tools-o09qd6\"\n        },\n        \"description\": \"Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```
```php Tools
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-r",
  "messages": [
    {
      "role": "user",
      "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the \'Electronics\' category, for example their prices and stock levels?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "query_daily_sales_report",
        "parameters": {
          "type": "object",
          "properties": {
            "day": {
              "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
              "type": "str"
            }
          },
          "required": [
            "day"
          ],
          "x-fern-type-name": "tools-by6k68"
        },
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
      }
    },
    {
      "type": "function",
      "function": {
        "name": "query_product_catalog",
        "parameters": {
          "type": "object",
          "properties": {
            "category": {
              "description": "Retrieves product information data for all products in this category.",
              "type": "str"
            }
          },
          "required": [
            "category"
          ],
          "x-fern-type-name": "tools-o09qd6"
        },
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels."
      }
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp Tools
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-r\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": \"Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?\"\n    }\n  ],\n  \"tools\": [\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_daily_sales_report\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"day\": {\n              \"description\": \"Retrieves sales data for this day, formatted as YYYY-MM-DD.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"day\"\n          ],\n          \"x-fern-type-name\": \"tools-by6k68\"\n        },\n        \"description\": \"Connects to a database to retrieve overall sales volumes and sales information for a given day.\"\n      }\n    },\n    {\n      \"type\": \"function\",\n      \"function\": {\n        \"name\": \"query_product_catalog\",\n        \"parameters\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"category\": {\n              \"description\": \"Retrieves product information data for all products in this category.\",\n              \"type\": \"str\"\n            }\n          },\n          \"required\": [\n            \"category\"\n          ],\n          \"x-fern-type-name\": \"tools-o09qd6\"\n        },\n        \"description\": \"Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels.\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift Tools
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-r",
  "messages": [
    [
      "role": "user",
      "content": "Can you provide a sales summary for 29th September 2023, and also give me some details about the products in the 'Electronics' category, for example their prices and stock levels?"
    ]
  ],
  "tools": [
    [
      "type": "function",
      "function": [
        "name": "query_daily_sales_report",
        "parameters": [
          "type": "object",
          "properties": ["day": [
              "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
              "type": "str"
            ]],
          "required": ["day"],
          "x-fern-type-name": "tools-by6k68"
        ],
        "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day."
      ]
    ],
    [
      "type": "function",
      "function": [
        "name": "query_product_catalog",
        "parameters": [
          "type": "object",
          "properties": ["category": [
              "description": "Retrieves product information data for all products in this category.",
              "type": "str"
            ]],
          "required": ["category"],
          "x-fern-type-name": "tools-o09qd6"
        ],
        "description": "Connects to a a product catalog with information about all the products being sold, including categories, prices, and stock levels."
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```
```typescript Images
const { CohereClientV2 } = require('cohere-ai');

const cohere = new CohereClientV2({});

(async () => {
  const response = await cohere.chat({
    model: 'command-a-vision-07-2025',
    messages: [
      {
        role: 'user',
        content: [
          { type: 'text', text: 'Describe this image' },
          {
            type: 'image_url',
            imageUrl: {
              // Can be either a base64 data URI or a web URL.
              url: 'https://cohere.com/favicon-32x32.png',
              detail: 'auto',
            },
          },
        ],
      },
    ],
  });
  console.log(response.message.content[0].text);
})();
```
```python Images
import cohere

co = cohere.ClientV2()

response = co.chat(
    model="command-a-vision-07-2025",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        # Can be either a base64 data URI or a web URL.

                        "url": "https://cohere.com/favicon-32x32.png",
                        "detail": "auto"
                    }
                }
            ]
        }
    ]
)

print(response)
```
```java Images
/* (C)2024 */
package chatv2post;

import java.util.List;

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2ChatRequest;
import com.cohere.api.types.ChatMessageV2;
import com.cohere.api.types.ChatResponse;
import com.cohere.api.types.Content;
import com.cohere.api.types.ImageContent;
import com.cohere.api.types.ImageUrl;
import com.cohere.api.types.TextContent;
import com.cohere.api.types.UserMessage;
import com.cohere.api.types.UserMessageContent;

public class Image {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ChatResponse response =
        cohere
            .v2()
            .chat(
                V2ChatRequest.builder()
                    .model("command-a-vision-07-2025")
                    .messages(
                        List.of(
                            ChatMessageV2.user(
                                UserMessage.builder()
                                    .content(
                                        UserMessageContent.of(
                                            List.of(
                                                Content.text(
                                                    TextContent.builder()
                                                        .text("Describe this image")
                                                        .build()),
                                                Content.imageUrl(
                                                    ImageContent.builder()
                                                        .imageUrl(
                                                            ImageUrl.builder()
                                                                // Can be either a base64 data URI or a web URL.
                                                                .url(
                                                                    "https://cohere.com/favicon-32x32.png")
                                                                .build())
                                                        .build()))))
                                    .build())))
                    .build());

    System.out.println(response);
  }
}
```
```go Images
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Chat(
		context.TODO(),
		&cohere.V2ChatRequest{
			Model: "command-a-vision-07-2025",
			Messages: cohere.ChatMessages{
				{
					Role: "user",
					User: &cohere.UserMessageV2{
						Content: &cohere.UserMessageV2Content{
							ContentList: []*cohere.Content{
								{Type: "text", Text: &cohere.ChatTextContent{Text: "Describe this image"}},
								{Type: "image_url", ImageUrl: &cohere.ImageContent{
									ImageUrl: &cohere.ImageUrl{
										// Can be either a base64 data URI or a web URL.
										Url:    "https://cohere.com/favicon-32x32.png",
										Detail: cohere.ImageUrlDetailAuto.Ptr(),
									},
								}},
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}
```
```ruby Images
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/chat")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"stream\": false,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```
```php Images
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/chat', [
  'body' => '{
  "stream": false,
  "model": "command-a-vision-07-2025",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Describe this image"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://cohere.com/favicon-32x32.png",
            "detail": "auto"
          }
        }
      ]
    }
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```
```csharp Images
var client = new RestClient("https://api.cohere.com/v2/chat");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"stream\": false,\n  \"model\": \"command-a-vision-07-2025\",\n  \"messages\": [\n    {\n      \"role\": \"user\",\n      \"content\": [\n        {\n          \"type\": \"text\",\n          \"text\": \"Describe this image\"\n        },\n        {\n          \"type\": \"image_url\",\n          \"image_url\": {\n            \"url\": \"https://cohere.com/favicon-32x32.png\",\n            \"detail\": \"auto\"\n          }\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```
```swift Images
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "stream": false,
  "model": "command-a-vision-07-2025",
  "messages": [
    [
      "role": "user",
      "content": [
        [
          "type": "text",
          "text": "Describe this image"
        ],
        [
          "type": "image_url",
          "image_url": [
            "url": "https://cohere.com/favicon-32x32.png",
            "detail": "auto"
          ]
        ]
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/chat")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
