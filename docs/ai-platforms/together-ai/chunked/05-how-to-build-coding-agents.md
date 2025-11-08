**Navigation:** [← Previous](./04-fine-tuning-guide.md) | [Index](./index.md) | [Next →](./06-iterative-workflow.md)

---

# How to Build Coding Agents
Source: https://docs.together.ai/docs/how-to-build-coding-agents

How to build your own simple code editing agent from scratch in 400 lines of code!

I recently read a great [blog post](https://ampcode.com/how-to-build-an-agent) by Thorsten Ball on how simple it is to build coding agents and was inspired to make a python version guide here!

We'll create an LLM that can call tools that allow it to create, edit and read the contents of files and repos!

## Setup

First, let's import the necessary libraries. We'll be using the `together` library to interact with the Together AI API.

<CodeGroup>
  ```sh Shell theme={null}
  !pip install together
  ```

  ```python Python theme={null}
  from together import Together

  client = Together()
  ```
</CodeGroup>

## Basic Chat Interaction

Let's start with a simple loop that takes user input, sends it to a language model (LLM) using the Together AI client, and prints the LLM's response. We'll maintain a `messages_history` to keep track of the conversation context.

<CodeGroup>
  ```python Python theme={null}
  def chat():
      while True:
          user_input = input("Enter something (type 'exit' to quit): ")
          if user_input.lower() == "exit":
              break
          messages_history.append({"role": "user", "content": user_input})
          print(f"You: {user_input}")
          # Process user_input here
          completion = client.chat.completions.create(
              model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
              messages=messages_history,
          )
          print(f"LLM: {completion.choices[0].message.content}")
          messages_history.append(
              {
                  "role": "assistant",
                  "content": completion.choices[0].message.content,
              }
          )


  chat()
  ```
</CodeGroup>

Usage:

```
You: Hey! I'm Zain! How are you?

LLM: Nice to meet you, Zain. I'm doing well, thanks for asking. I'm a large language model, so I don't have feelings or emotions like humans do, but I'm always happy to chat and help with any questions or topics you'd like to discuss. How about you? How's your day going?

You: Can you come up with any horse-related nicknames that make fun of my first name?

LLM: I can try to come up with some horse-related nicknames that poke fun at your name. Keep in mind that these are lighthearted and meant in a playful spirit.

Here are a few ideas:

1. Zain Stallion (a playful take on the idea of a strong, majestic horse)
2. Zainy McMane (a silly name that adds a fun twist to your name)
3. Zain the Reiner (a reference to the reining horse discipline, with a nod to your name)
4. Zainy Horseface (a goofy nickname that's sure to bring a smile)
5. Zain the Colt (a playful reference to a young, energetic horse)

Remember, these are just for fun, and I'm sure you're more than just a nickname!
```

## Tool use by LLMs

Tool use is pretty simple - we tell the model that it has access to certain tools and instruct it to use them when it feels it would help resolve a prompt. As Thorsten say:

To summarize, all there is to tools and tool use are two things:

1. You tell the model what tools are available
2. When the model wants to execute the tool, it tells you, you execute the tool and send the response up

To make (1) easier, the big model providers have built-in APIs to send tool definitions along.

To get the intuition behind `tool_use` you don't need to make any code changes - we can simply use the same `chat()` function above:

```
You: You are a weather expert. When I ask you about the weather in a given location, I want you to reply with `get_weather(<location_name>)`. I will then tell you what the weather in that location is. Understood?

LLM: You're reminding me of our previous agreement. Yes, I understand. When you ask about the weather in a location, I'll respond with `get_weather(<location_name>)`, and you'll provide the actual weather conditions. Let's get back to it.

You: Hey, what's the weather in Munich?

LLM: get_weather(Munich)

You: hot and humid, 28 degrees celcius

LLM: It sounds like Munich is experiencing a warm and muggy spell. I'll make a note of that. What's the weather like in Paris?
```

Pretty simple! We asked the model to use the `get_weather()` function if needed and it did. When it did we provided it information it wanted and it followed us by using that information to answer our original question!

This is all function calling/tool-use really is!

## Defining Tools for the Agent

To make this workflow of instructing the model to use tools and then running the functions it calls and sending it the response more convenient people have built scaffolding where we can pass in pre-specified tools to LLMs as follows:

<CodeGroup>
  ```python Python theme={null}
  # Let define a function that you would use to read a file


  def read_file(path: str) -> str:
      """
      Reads the content of a file and returns it as a string.

      Args:
          path: The relative path of a file in the working directory.

      Returns:
          The content of the file as a string.

      Raises:
          FileNotFoundError: If the specified file does not exist.
          PermissionError: If the user does not have permission to read the file.
      """
      try:
          with open(path, "r", encoding="utf-8") as file:
              content = file.read()
          return content
      except FileNotFoundError:
          raise FileNotFoundError(f"The file '{path}' was not found.")
      except PermissionError:
          raise PermissionError(f"You don't have permission to read '{path}'.")
      except Exception as e:
          raise Exception(f"An error occurred while reading '{path}': {str(e)}")


  read_file_schema = {
      "type": "function",
      "function": {
          "name": "read_file",
          "description": "The relative path of a file in the working directory.",
          "parameters": {
              "properties": {
                  "path": {
                      "description": "The relative path of a file in the working directory.",
                      "title": "Path",
                      "type": "string",
                  }
              },
              "type": "object",
          },
      },
  }
  ```
</CodeGroup>

Function schema:

```json  theme={null}
{'type': 'function',
 'function': {'name': 'read_file',
  'description': 'The relative path of a file in the working directory.',
  'parameters': {'properties': {'path': {'description': 'The relative path of a file in the working directory.',
     'title': 'Path',
     'type': 'string'}},
   'type': 'object'}}}
```

We can now pass these function/tool into an LLM and if needed it will use it to read files!

Lets create a file first:

<CodeGroup>
  ```shell Shell theme={null}
  echo "my favourite colour is cyan sanguine" >> secret.txt
  ```
</CodeGroup>

Now lets see if the model can use the new `read_file` tool to discover the secret!

<CodeGroup>
  ```python Python theme={null}
  import os
  import json

  messages = [
      {
          "role": "system",
          "content": "You are a helpful assistant that can access external functions. The responses from these function calls will be appended to this dialogue. Please provide responses based on the information from these function calls.",
      },
      {
          "role": "user",
          "content": "Read the file secret.txt and reveal the secret!",
      },
  ]
  tools = [read_file_schema]

  response = client.chat.completions.create(
      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
      messages=messages,
      tools=tools,
      tool_choice="auto",
  )

  print(
      json.dumps(
          response.choices[0].message.model_dump()["tool_calls"],
          indent=2,
      )
  )
  ```
</CodeGroup>

This will output a tool call from the model:

```json  theme={null}
[
  {
    "id": "call_kx9yu9ti0ejjabt7kexrsn1c",
    "type": "function",
    "function": {
      "name": "read_file",
      "arguments": "{\"path\":\"secret.txt\"}"
    },
    "index": 0
  }
]
```

## Calling Tools

Now we need to run the function that the model has asked for and feed the response back to the model, this can be done by simply checking if the model asked for a tool call and executing the corresponding function and sending the response to the model:

<CodeGroup>
  ```python Python theme={null}
  tool_calls = response.choices[0].message.tool_calls

  # check is a tool was called by the first model call
  if tool_calls:
      for tool_call in tool_calls:
          function_name = tool_call.function.name
          function_args = json.loads(tool_call.function.arguments)

          if function_name == "read_file":
              # manually call the function
              function_response = read_file(path=function_args.get("path"))

              # add the response to messages to be sent back to the model
              messages.append(
                  {
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": function_name,
                      "content": function_response,
                  }
              )
      # re-call the model now with the response of the tool!
      function_enriched_response = client.chat.completions.create(
          model="Qwen/Qwen2.5-7B-Instruct-Turbo",
          messages=messages,
      )
      print(
          json.dumps(
              function_enriched_response.choices[0].message.model_dump(),
              indent=2,
          )
      )
  ```
</CodeGroup>

Output:

<CodeGroup>
  ```json Json theme={null}
  {
    "role": "assistant",
    "content": "The secret from the file secret.txt is \"my favourite colour is cyan sanguine\".",
    "tool_calls": []
  }
  ```
</CodeGroup>

Above, we simply did the following:

1. See if the model wanted us to use a tool.
2. If so, we used the tool for it.
3. We appended the output from the tool back into `messages` and called the model again to make sense of the function response.

Now let's make our coding agent more interesting by creating two more tools!

## More tools: `list_files` and `edit_file`

We'll want our coding agent to be able to see what files exist in a repo and also modify pre-existing files as well so we'll add two more tools:

### `list_files` Tool: Given a path to a repo, this tool lists the files in that repo.

<CodeGroup>
  ```python Python theme={null}
  def list_files(path="."):
      """
      Lists all files and directories in the specified path.

      Args:
          path (str): The relative path of a directory in the working directory.
                      Defaults to the current directory.

      Returns:
          str: A JSON string containing a list of files and directories.
      """
      result = []
      base_path = Path(path)

      if not base_path.exists():
          return json.dumps({"error": f"Path '{path}' does not exist"})

      for root, dirs, files in os.walk(path):
          root_path = Path(root)
          rel_root = (
              root_path.relative_to(base_path)
              if root_path != base_path
              else Path(".")
          )

          # Add directories with trailing slash
          for dir_name in dirs:
              rel_path = rel_root / dir_name
              if str(rel_path) != ".":
                  result.append(f"{rel_path}/")

          # Add files
          for file_name in files:
              rel_path = rel_root / file_name
              if str(rel_path) != ".":
                  result.append(str(rel_path))

      return json.dumps(result)


  list_files_schema = {
      "type": "function",
      "function": {
          "name": "list_files",
          "description": "List all files and directories in the specified path.",
          "parameters": {
              "type": "object",
              "properties": {
                  "path": {
                      "type": "string",
                      "description": "The relative path of a directory in the working directory. Defaults to current directory.",
                  }
              },
          },
      },
  }

  # Register the list_files function in the tools
  tools.append(list_files_schema)
  ```
</CodeGroup>

### `edit_file` Tool: Edit files by adding new content or replacing old content

<CodeGroup>
  ```python Python theme={null}
  def edit_file(path, old_str, new_str):
      """
      Edit a file by replacing all occurrences of old_str with new_str.
      If old_str is empty and the file doesn't exist, create a new file with new_str.

      Args:
          path (str): The relative path of the file to edit
          old_str (str): The string to replace
          new_str (str): The string to replace with

      Returns:
          str: "OK" if successful
      """

      if not path or old_str == new_str:
          raise ValueError("Invalid input parameters")

      try:
          with open(path, "r") as file:
              old_content = file.read()
      except FileNotFoundError:
          if old_str == "":
              # Create a new file if old_str is empty and file doesn't exist
              with open(path, "w") as file:
                  file.write(new_str)
              return "OK"
          else:
              raise FileNotFoundError(f"File not found: {path}")

      new_content = old_content.replace(old_str, new_str)

      if old_content == new_content and old_str != "":
          raise ValueError("old_str not found in file")

      with open(path, "w") as file:
          file.write(new_content)

      return "OK"


  # Define the function schema for the edit_file tool
  edit_file_schema = {
      "type": "function",
      "function": {
          "name": "edit_file",
          "description": "Edit a file by replacing all occurrences of a string with another string",
          "parameters": {
              "type": "object",
              "properties": {
                  "path": {
                      "type": "string",
                      "description": "The relative path of the file to edit",
                  },
                  "old_str": {
                      "type": "string",
                      "description": "The string to replace (empty string for new files)",
                  },
                  "new_str": {
                      "type": "string",
                      "description": "The string to replace with",
                  },
              },
              "required": ["path", "old_str", "new_str"],
          },
      },
  }

  # Update the tools list to include the edit_file function
  tools.append(edit_file_schema)
  ```
</CodeGroup>

## Incorporating Tools into the Coding Agent

Now we can add all three of these tools into the simple looping chat function we made and call it!

<CodeGroup>
  ```python Python theme={null}
  def chat():
      messages_history = []

      while True:
          user_input = input("You: ")
          if user_input.lower() in ["exit", "quit", "q"]:
              break

          messages_history.append({"role": "user", "content": user_input})

          response = client.chat.completions.create(
              model="Qwen/Qwen2.5-7B-Instruct-Turbo",
              messages=messages_history,
              tools=tools,
          )

          tool_calls = response.choices[0].message.tool_calls
          if tool_calls:
              for tool_call in tool_calls:
                  function_name = tool_call.function.name
                  function_args = json.loads(tool_call.function.arguments)

                  if function_name == "read_file":
                      print(f"Tool call: read_file")
                      function_response = read_file(
                          path=function_args.get("path")
                      )
                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )
                  elif function_name == "list_files":
                      print(f"Tool call: list_files")
                      function_response = list_files(
                          path=function_args.get("path", ".")
                      )

                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )
                  elif function_name == "edit_file":
                      print(f"Tool call: edit_file")
                      function_response = edit_file(
                          path=function_args.get("path"),
                          old_str=function_args.get("old_str"),
                          new_str=function_args.get("new_str"),
                      )
                      messages_history.append(
                          {
                              "tool_call_id": tool_call.id,
                              "role": "tool",
                              "name": function_name,
                              "content": function_response,
                          }
                      )

                  function_enriched_response = client.chat.completions.create(
                      model="Qwen/Qwen2.5-7B-Instruct-Turbo",
                      messages=messages_history,
                  )

                  messages_history.append(
                      {
                          "role": "assistant",
                          "content": function_enriched_response.choices[
                              0
                          ].message.content,
                      }
                  )
                  print(
                      f"LLM: {function_enriched_response.choices[0].message.content}"
                  )
          else:
              messages_history.append(
                  {
                      "role": "assistant",
                      "content": response.choices[0].message.content,
                  }
              )
              print(f"LLM: {response.choices[0].message.content}")


  # start the chat
  chat()
  ```
</CodeGroup>

Output:

````
You: Create a congrats.py script that rot13-decodes the following string ‘Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!’ and prints it.

Tool call: edit_file

LLM: Sure, I'll create a `congrats.py` script that rot13-decodes the given string and prints it. Here's the script:

```python
def rot13_decode(s):
    result = ""
    for char in s:
        if "a" <= char <= "z":
            start = ord("a")
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        elif "A" <= char <= "Z":
            start = ord("A")
            offset = (ord(char) - start + 13) % 26
            result += chr(start + offset)
        else:
            result += char
    return result


# The encoded string
encoded_string = "Pbatenghyngvbaf ba ohvyqvat n pbqr-rqvgvat ntrag!"

# Decoding the string
decoded_string = rot13_decode(encoded_string)

# Printing the decoded string
print(decoded_string)
```
You can save this code in a file named `congrats.py` and run it to see the decoded message.
````

This code will give you a new python script: `congrats.py` which you can run!

<CodeGroup>
  ```shell Shell theme={null}
  python congrats.py
  ```
</CodeGroup>

Output:

```
Congratulations on building a code-editing agent!
```


# How to build an AI audio transcription app with Whisper
Source: https://docs.together.ai/docs/how-to-build-real-time-audio-transcription-app

Learn how to build a real-time AI audio transcription app with Whisper, Next.js, and Together AI.

In this guide, we're going to go over how we built [UseWhisper.io](https://usewhisper.io), an open source audio transcription app that converts speech to text almost instantly & can transform it into summaries. It's built using the [Whisper Large v3 API](https://www.together.ai/models/openai-whisper-large-v3) on Together AI and supports both live recording and file uploads.

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=07a613b09568c0726911221011dbf694" alt="usewhisper.io" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/guides/whisper/cover.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=435f9e2add5d9864345b457d2031b96d 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=98c58ab6d675cb5a4157f3fb718fb391 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=580d414399cbf99b0c389e7586e001b5 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=925e8c16fce481e7d876a609b538a52a 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=1b8d6614de2665aceff547559b9c7e5c 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=d3a58a13e57e1785423af5a19fd5e5eb 2500w" />

In this post, you'll learn how to build the core parts of UseWhisper.io. The app is open-source and built with Next.js, tRPC for type safety, and Together AI's API, but the concepts can be applied to any language or framework.

## Building the audio recording interface

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=56a54a41ccd4f317e72f7046cf3aaee0" alt="Recording modal UI" data-og-width="699" width="699" data-og-height="384" height="384" data-path="images/guides/whisper/recording-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=f08d68857caa9d4155de1ee64ea8213c 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=ab8b211d7ffb16cff04aaadc37eb1207 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=92778c223fed6d1e7fe9f67928ded434 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=bc84a97166e1c8d7c5b8ed2eaabf37f1 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=67878551dfe6fdb7b029545c64e085aa 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=96a49d291ecfa1cbf99bed6a01ca3ed4 2500w" />

Whisper's core interaction is a recording modal where users can capture audio directly in the browser:

```tsx  theme={null}
function RecordingModal({ onClose }: { onClose: () => void }) {
  const { recording, audioBlob, startRecording, stopRecording } =
    useAudioRecording();

  const handleRecordingToggle = async () => {
    if (recording) {
      stopRecording();
    } else {
      await startRecording();
    }
  };

  // Auto-process when we get an audio blob
  useEffect(() => {
    if (audioBlob) {
      handleSaveRecording();
    }
  }, [audioBlob]);

  return (
    <Dialog open onOpenChange={onClose}>
      <DialogContent>
        <Button onClick={handleRecordingToggle}>
          {recording ? "Stop Recording" : "Start Recording"}
        </Button>
      </DialogContent>
    </Dialog>
  );
}
```

The magic happens in our custom `useAudioRecording` hook, which handles all the browser audio recording logic.

## Recording audio in the browser

To capture audio, we use the MediaRecorder API with a simple hook:

```tsx  theme={null}
function useAudioRecording() {
  const [recording, setRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const startRecording = async () => {
    try {
      // Request microphone access
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

      // Create MediaRecorder
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      chunksRef.current = [];

      // Collect audio data
      mediaRecorder.ondataavailable = (e) => {
        chunksRef.current.push(e.data);
      };

      // Create blob when recording stops
      mediaRecorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        setAudioBlob(blob);
        // Stop all tracks to release microphone
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorder.start();
      setRecording(true);
    } catch (err) {
      console.error("Microphone access denied:", err);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && recording) {
      mediaRecorderRef.current.stop();
      setRecording(false);
    }
  };

  return { recording, audioBlob, startRecording, stopRecording };
}
```

This simplified version focuses on the core functionality: start recording, stop recording, and get the audio blob.

## Uploading and transcribing audio

Once we have our audio blob (from recording) or file (from upload), we need to send it to Together AI's Whisper model. We use S3 for temporary storage and tRPC for type-safe API calls:

```tsx  theme={null}
const handleSaveRecording = async () => {
  if (!audioBlob) return;

  try {
    // Upload to S3
    const file = new File([audioBlob], `recording-${Date.now()}.webm`, {
      type: "audio/webm",
    });
    const { url } = await uploadToS3(file);

    // Call our tRPC endpoint
    const { id } = await transcribeMutation.mutateAsync({
      audioUrl: url,
      language: selectedLanguage,
      durationSeconds: duration,
    });

    // Navigate to transcription page
    router.push(`/whispers/${id}`);
  } catch (err) {
    toast.error("Failed to transcribe audio. Please try again.");
  }
};
```

## Creating the transcription API with tRPC

Our backend uses tRPC to provide end-to-end type safety. Here's our transcription endpoint:

```tsx  theme={null}
import { Together } from "together-ai";
import { createTogetherAI } from "@ai-sdk/togetherai";
import { generateText } from "ai";

export const whisperRouter = t.router({
  transcribeFromS3: protectedProcedure
    .input(
      z.object({
        audioUrl: z.string(),
        language: z.string().optional(),
        durationSeconds: z.number().min(1),
      })
    )
    .mutation(async ({ input, ctx }) => {
      // Call Together AI's Whisper model
      const togetherClient = new Together({
        apiKey: process.env.TOGETHER_API_KEY,
      });

      const res = await togetherClient.audio.transcriptions.create({
        file: input.audioUrl,
        model: "openai/whisper-large-v3",
        language: input.language || "en",
      });

      const transcription = res.text as string;

      // Generate a title using LLM
      const togetherAI = createTogetherAI({
        apiKey: process.env.TOGETHER_API_KEY,
      });

      const { text: title } = await generateText({
        prompt: `Generate a title for the following transcription with max of 10 words: ${transcription}`,
        model: togetherAI("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
        maxTokens: 10,
      });

      // Save to database
      const whisperId = uuidv4();
      await prisma.whisper.create({
        data: {
          id: whisperId,
          title: title.slice(0, 80),
          userId: ctx.auth.userId,
          fullTranscription: transcription,
          audioTracks: {
            create: [
              {
                fileUrl: input.audioUrl,
                partialTranscription: transcription,
                language: input.language,
              },
            ],
          },
        },
      });

      return { id: whisperId };
    }),
});
```

The beauty of tRPC is that our frontend gets full TypeScript intellisense and type checking for this API call.

## Supporting file uploads

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=469a391f117228a11de74c751b49996c" alt="Upload modal UI" data-og-width="664" width="664" data-og-height="408" height="408" data-path="images/guides/whisper/upload-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=db453b15f4720d9fe62b6363a3667fc9 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=1dddb61895e556c1a755541932cbd7a8 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=645f34df69928a02dbe627f36a05d464 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=bddc420aecbd3b49437ab7a833f80c3b 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=25dc288c6b3a79e9dc3a5ae570ad0699 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=231d74b13ade1d1e94df0a37d1b79517 2500w" />

For users who want to upload existing audio files, we use react-dropzone and next-s3-upload.

Next-s3-upload handles the S3 upload in the backend and fully integrates with Next.js API routes in a simple 5 minute setup you can read more here: [https://next-s3-upload.codingvalue.com/](https://next-s3-upload.codingvalue.com/)
:

```tsx  theme={null}
import Dropzone from "react-dropzone";
import { useS3Upload } from "next-s3-upload";

function UploadModal({ onClose }: { onClose: () => void }) {
  const { uploadToS3 } = useS3Upload();

  const handleDrop = useCallback(async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    try {
      // Get audio duration and upload in parallel
      const [duration, { url }] = await Promise.all([
        getDuration(file),
        uploadToS3(file),
      ]);

      // Transcribe using the same endpoint
      const { id } = await transcribeMutation.mutateAsync({
        audioUrl: url,
        language,
        durationSeconds: Math.round(duration),
      });

      router.push(`/whispers/${id}`);
    } catch (err) {
      toast.error("Failed to transcribe audio. Please try again.");
    }
  }, []);

  return (
    <Dropzone
      accept={{
        "audio/mpeg3": [".mp3"],
        "audio/wav": [".wav"],
        "audio/mp4": [".m4a"],
      }}
      onDrop={handleDrop}
    >
      {({ getRootProps, getInputProps }) => (
        <div {...getRootProps()}>
          <input {...getInputProps()} />
          <p>Drop audio files here or click to upload</p>
        </div>
      )}
    </Dropzone>
  );
}
```

## Adding audio transformations

Once we have a transcription, users can transform it using LLMs. We support summarization, extraction, and custom transformations:

```tsx  theme={null}
import { createTogetherAI } from "@ai-sdk/togetherai";
import { generateText } from "ai";

const transformText = async (prompt: string, transcription: string) => {
  const togetherAI = createTogetherAI({
    apiKey: process.env.TOGETHER_API_KEY,
  });

  const { text } = await generateText({
    prompt: `${prompt}\n\nTranscription: ${transcription}`,
    model: togetherAI("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
  });

  return text;
};
```

## Type safety with tRPC

One of the key benefits of using tRPC is the end-to-end type safety. When we call our API from the frontend:

```tsx  theme={null}
const transcribeMutation = useMutation(
  trpc.whisper.transcribeFromS3.mutationOptions()
);

// TypeScript knows the exact shape of the input and output
const result = await transcribeMutation.mutateAsync({
  audioUrl: "...",
  language: "en", // TypeScript validates this
  durationSeconds: 120,
});

// result.id is properly typed
router.push(`/whispers/${result.id}`);
```

This eliminates runtime errors and provides excellent developer experience with autocomplete and type checking.

## Going beyond basic transcription

Whisper is open-source, so check out the [full code](https://github.com/nutlope/whisper) to learn more and get inspired to build your own audio transcription apps.

When you're ready to start transcribing audio in your own apps, sign up for [Together AI](https://togetherai.link) today and make your first API call in minutes!


# How To Implement Contextual RAG From Anthropic
Source: https://docs.together.ai/docs/how-to-implement-contextual-rag-from-anthropic

An open source line-by-line implementation and explanation of Contextual RAG from Anthropic!

[Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) is a chunk augmentation technique that uses an LLM to enhance each chunk.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c95e14ec01de84f03a0982ea44d565c4" alt="" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/guides/11.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d51f62f41d26706932895aa10cdb0fda 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a65bc40ec2d7e34403a2cbb20d0b9b30 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=12614a08d879bda5bb9bf6e7b681ecdc 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=46e51018c60daa77f9cab77c5f82e01b 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=89baff1add76974b4f68ed6eab4b2b6a 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/11.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8f92575f98fa1614cfab7d5e336a5039 2500w" />
</Frame>

Here's an overview of how it works.

## Contextual RAG:

1. For every chunk - prepend an explanatory context snippet that situates the chunk within the rest of the document. -> Get a small cost effective LLM to do this.
2. Hybrid Search: Embed the chunk using both sparse (keyword) and dense(semantic) embeddings.
3. Perform rank fusion using an algorithm like Reciprocal Rank Fusion(RRF).
4. Retrieve top 150 chunks and pass those to a Reranker to obtain top 20 chunks.
5. Pass top 20 chunks to LLM to generate an answer.

Below we implement each step in this process using Open Source models.

To breakdown the concept further we break down the process into a one-time indexing step and a query time step.

**Data Ingestion Phase:**

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3d2da83adbb003deca81154f23d11867" alt="" data-og-width="1675" width="1675" data-og-height="1281" height="1281" data-path="images/guides/12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c93703cef1766f91b2b0f18d21801fc1 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fa9055a5d5e2c501f1acb90f0d5e5a29 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5a95544a4bf3e27faf78e917aad90379 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ff0025c3cef507c5a91454390d32a912 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cc5f81ec127b0c7d0134c998e47bd6da 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/12.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2dbd7ecadba466e4f214f22712111715 2500w" />
</Frame>

1. Data processing and chunking
2. Context generation using a quantized Llama 3.2 3B Model
3. Vector Embedding and Index Generation
4. BM25 Keyword Index Generation

**At Query Time:**

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d7d2540ce149d7d9a6ea84b568d4512d" alt="" data-og-width="1804" width="1804" data-og-height="385" height="385" data-path="images/guides/13.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9895e8a1bfd611578457bcba5bc80d05 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88d16d6f5bd7a549b407678efdfb779f 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=623b991278e23b3750a66664c40b7f34 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=48f97337f20fca38533c26d04af71678 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6eb0f97d48de8dbec8597d7ec5f12800 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/13.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=edb78219ad34e6dc86f5cddb68a2c77d 2500w" />
</Frame>

1. Perform retrieval using both indices and combine them using RRF
2. Reranker to improve retrieval quality
3. Generation with Llama3.1 405B

## Install Libraries

```
pip install together # To access open source LLMs
pip install --upgrade tiktoken # To count total token counts
pip install beautifulsoup4 # To scrape documents to RAG over
pip install bm25s # To implement out key-word BM25 search
```

## Data Processing and Chunking

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=05b43d40a13b1fda5e763c12611c8f27" alt="" data-og-width="1410" width="1410" data-og-height="824" height="824" data-path="images/guides/14.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=037ed1d5d0f290620a3259349d04856d 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=32e29d7d32bfa6e503d3e70f28df4503 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a12c43504a810d22333ca24e266b0846 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=00bf82397cd79c16cd1a723604ec96de 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3e71efe1ac5d7b9a2149bc3bb44c3de1 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/14.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2737dceaedf3f8c7aeba0c2dfd6d605a 2500w" />
</Frame>

We will RAG over Paul Grahams latest essay titled [Founder Mode](https://paulgraham.com/foundermode.html) .

```py Python theme={null}
# Let's download the essay from Paul Graham's website

import requests
from bs4 import BeautifulSoup


def scrape_pg_essay():

    url = "https://paulgraham.com/foundermode.html"

    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Paul Graham's essays typically have the main content in a font tag
        # You might need to adjust this selector based on the actual HTML structure
        content = soup.find("font")

        if content:
            # Extract and clean the text
            text = content.get_text()
            # Remove extra whitespace and normalize line breaks
            text = " ".join(text.split())
            return text
        else:
            return "Could not find the main content of the essay."

    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"


# Scrape the essay
pg_essay = scrape_pg_essay()
```

This will give us the essay, we still need to chunk the essay, so lets implement a function and use it:

```py Python theme={null}
# We can get away with naive fixed sized chunking as the context generation will add meaning to these chunks


def create_chunks(document, chunk_size=300, overlap=50):
    return [
        document[i : i + chunk_size]
        for i in range(0, len(document), chunk_size - overlap)
    ]


chunks = create_chunks(pg_essay, chunk_size=250, overlap=30)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")
```

We get the following chunked content:

```
Chunk 1: September 2024At a YC event last week Brian Chesky gave a talk that everyone who was there will remember. Most founders I talked to afterward said it was the best they'd ever heard. Ron Conway, for the first time in his life, forgot to take notes. I'
Chunk 2: life, forgot to take notes. I'm not going to try to reproduce it here. Instead I want to talk about a question it raised.The theme of Brian's talk was that the conventional wisdom about how to run larger companies is mistaken. As Airbnb grew, well-me
...
```

## Generating Contextual Chunks

This part contains the main intuition behind `Contextual Retrieval`. We will make an LLM call for each chunk to add much needed relevant context to the chunk. In order to do this we pass in the ENTIRE document per LLM call.

It may seem that passing in the entire document per chunk and making an LLM call per chunk is quite inefficient, this is true and there very well might be more efficient techniques to accomplish the same end goal. But in keeping with implementing the current technique at hand lets do it.

Additionally using quantized small 1-3B models (here we will use Llama 3.2 3B) along with prompt caching does make this more feasible.

Prompt caching allows key and value matrices corresponding to the document to be cached for future LLM calls.

We will use the following prompt to generate context for each chunk:

```py Python theme={null}
# We want to generate a snippet explaining the relevance/importance of the chunk with
# full document in mind.

CONTEXTUAL_RAG_PROMPT = """
Given the document below, we want to explain what the chunk captures in the document.

{WHOLE_DOCUMENT}

Here is the chunk we want to explain:

{CHUNK_CONTENT}

Answer ONLY with a succinct explaination of the meaning of the chunk in the context of the whole document above.
"""
```

Now we can prep each chunk into these prompt template and generate the context:

```py Python theme={null}
from typing import List
import together, os
from together import Together

# Paste in your Together AI API Key or load it
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

client = Together(api_key=TOGETHER_API_KEY)

# First we will just generate the prompts and examine them


def generate_prompts(document: str, chunks: List[str]) -> List[str]:
    prompts = []
    for chunk in chunks:
        prompt = CONTEXTUAL_RAG_PROMPT.format(
            WHOLE_DOCUMENT=document,
            CHUNK_CONTENT=chunk,
        )
        prompts.append(prompt)
    return prompts


prompts = generate_prompts(pg_essay, chunks)


def generate_context(prompt: str):
    """
    Generates a contextual response based on the given prompt using the specified language model.
    Args:
        prompt (str): The input prompt to generate a response for.
    Returns:
        str: The generated response content from the language model.
    """
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
    )
    return response.choices[0].message.content
```

We can now use the functions above to generate context for each chunk and append it to the chunk itself:

```py Python theme={null}
# Let's generate the entire list of contextual chunks and concatenate to the original chunk

contextual_chunks = [
    generate_context(prompts[i]) + " " + chunks[i] for i in range(len(chunks))
]
```

Now we can embed each chunk into a vector index.

## Vector Index

We will now use `bge-large-en-v1.5` to embed the augmented chunks above into a vector index.

```py Python theme={null}
from typing import List
import together
import numpy as np


def generate_embeddings(
    input_texts: List[str],
    model_api_string: str,
) -> List[List[float]]:
    """Generate embeddings from Together python library.

    Args:
        input_texts: a list of string input texts.
        model_api_string: str. An API string for a specific embedding model of your choice.

    Returns:
        embeddings_list: a list of embeddings. Each element corresponds to the each input text.
    """
    outputs = client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    )
    return [x.embedding for x in outputs.data]


contextual_embeddings = generate_embeddings(
    contextual_chunks,
    "BAAI/bge-large-en-v1.5",
)
```

Next we need to write a function that can retrieve the top matching chunks from this index given a query:

```py Python theme={null}
def vector_retrieval(
    query: str,
    top_k: int = 5,
    vector_index: np.ndarray = None,
) -> List[int]:
    """
    Retrieve the top-k most similar items from an index based on a query.
    Args:
        query (str): The query string to search for.
        top_k (int, optional): The number of top similar items to retrieve. Defaults to 5.
        index (np.ndarray, optional): The index array containing embeddings to search against. Defaults to None.
    Returns:
        List[int]: A list of indices corresponding to the top-k most similar items in the index.
    """

    query_embedding = generate_embeddings([query], "BAAI/bge-large-en-v1.5")[0]
    similarity_scores = cosine_similarity([query_embedding], vector_index)

    return list(np.argsort(-similarity_scores)[0][:top_k])


vector_retreival(
    query="What are 'skip-level' meetings?",
    top_k=5,
    vector_index=contextual_embeddings,
)
```

We now have a way to retrieve from the vector index given a query.

## BM25 Index

Lets build a keyword index that allows us to use BM25 to perform lexical search based on the words present in the query and the contextual chunks. For this we will use the `bm25s` python library:

```py Python theme={null}
import bm25s

# Create the BM25 model and index the corpus
retriever = bm25s.BM25(corpus=contextual_chunks)
retriever.index(bm25s.tokenize(contextual_chunks))
```

Which can be queried as follows:

```py Python theme={null}
# Query the corpus and get top-k results
query = "What are 'skip-level' meetings?"
results, scores = retriever.retrieve(
    bm25s.tokenize(query),
    k=5,
)
```

Similar to the function above which produces vector results from the vector index we can write a function that produces keyword search results from the BM25 index:

```py Python theme={null}
def bm25_retrieval(query: str, k: int, bm25_index) -> List[int]:
    """
    Retrieve the top-k document indices based on the BM25 algorithm for a given query.
    Args:
        query (str): The search query string.
        k (int): The number of top documents to retrieve.
        bm25_index: The BM25 index object used for retrieval.
    Returns:
        List[int]: A list of indices of the top-k documents that match the query.
    """

    results, scores = bm25_index.retrieve(bm25s.tokenize(query), k=k)

    return [contextual_chunks.index(doc) for doc in results[0]]
```

## Everything below this point will happen at query time!

Once a user submits a query we are going to use both functions above to perform Vector and BM25 retrieval and then fuse the ranks using the RRF algorithm implemented below.

```py Python theme={null}
# Example ranked lists from different sources
vector_top_k = vector_retreival(
    query="What are 'skip-level' meetings?",
    top_k=5,
    vector_index=contextual_embeddings,
)
bm25_top_k = bm25_retreival(
    query="What are 'skip-level' meetings?",
    k=5,
    bm25_index=retriever,
)
```

The Reciprocal Rank Fusion algorithm takes two ranked list of objects and combines them:

```py Python theme={null}
from collections import defaultdict


def reciprocal_rank_fusion(*list_of_list_ranks_system, K=60):
    """
    Fuse rank from multiple IR systems using Reciprocal Rank Fusion.

    Args:
    * list_of_list_ranks_system: Ranked results from different IR system.
    K (int): A constant used in the RRF formula (default is 60).

    Returns:
    Tuple of list of sorted documents by score and sorted documents
    """
    # Dictionary to store RRF mapping
    rrf_map = defaultdict(float)

    # Calculate RRF score for each result in each list
    for rank_list in list_of_list_ranks_system:
        for rank, item in enumerate(rank_list, 1):
            rrf_map[item] += 1 / (rank + K)

    # Sort items based on their RRF scores in descending order
    sorted_items = sorted(rrf_map.items(), key=lambda x: x[1], reverse=True)

    # Return tuple of list of sorted documents by score and sorted documents
    return sorted_items, [item for item, score in sorted_items]
```

We can use the RRF function above as follows:

```py Python theme={null}
# Combine the lists using RRF
hybrid_top_k = reciprocal_rank_fusion(vector_top_k, bm25_top_k)
hybrid_top_k[1]

hybrid_top_k_docs = [contextual_chunks[index] for index in hybrid_top_k[1]]
```

## Reranker To improve Quality

Now we add a retrieval quality improvement step here to make sure only the highest and most semantically similar chunks get sent to our LLM.

```py Python theme={null}
query = "What are 'skip-level' meetings?"  # we keep the same query - can change if we want

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=hybrid_top_k_docs,
    top_n=3,  # we only want the top 3 results but this can be alot higher
)

for result in response.results:
    retreived_chunks += hybrid_top_k_docs[result.index] + "\n\n"

print(retreived_chunks)
```

This will produce the following three chunks from our essay:

```
This chunk refers to "skip-level" meetings, which are a key characteristic of founder mode, where the CEO engages directly with the company beyond their direct reports. This contrasts with the "manager mode" of addressing company issues, where decisions are made perfunctorily via a hierarchical system, to which founders instinctively rebel. that there's a name for it. And once you abandon that constraint there are a huge number of permutations to choose from.For example, Steve Jobs used to run an annual retreat for what he considered the 100 most important people at Apple, and these wer

This chunk discusses the shift in company management away from the "manager mode" that most companies follow, where CEOs engage with the company only through their direct reports, to "founder mode", where CEOs engage more directly with even higher-level employees and potentially skip over direct reports, potentially leading to "skip-level" meetings. ts of, it's pretty clear that it's going to break the principle that the CEO should engage with the company only via his or her direct reports. "Skip-level" meetings will become the norm instead of a practice so unusual that there's a name for it. An

This chunk explains that founder mode, a hypothetical approach to running a company by its founders, will differ from manager mode in that founders will engage directly with the company, rather than just their direct reports, through "skip-level" meetings, disregarding the traditional principle that CEOs should only interact with their direct reports, as managers do.  can already guess at some of the ways it will differ.The way managers are taught to run companies seems to be like modular design in the sense that you treat subtrees of the org chart as black boxes. You tell your direct reports what to do, and it's
```

## Call Generative Model - Llama 3.1 405B

We will pass the finalized 3 chunks into an LLM to get our final answer.

```py Python theme={null}
# Generate a story based on the top 10 most similar movies

query = "What are 'skip-level' meetings?"

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful chatbot."},
        {
            "role": "user",
            "content": f"Answer the question: {query}. Here is relevant information: {retreived_chunks}",
        },
    ],
)
```

Which produces the following response:

```
'"Skip-level" meetings refer to a management practice where a CEO or high-level executive engages directly with employees who are not their direct reports, bypassing the traditional hierarchical structure of the organization. This approach is characteristic of "founder mode," where the CEO seeks to have a more direct connection with the company beyond their immediate team. In contrast to the traditional "manager mode," where decisions are made through a hierarchical system, skip-level meetings allow for more open communication and collaboration between the CEO and various levels of employees. This approach is often used by founders who want to stay connected to the company\'s operations and culture, and to foster a more flat and collaborative organizational structure.'
```

Above we implemented Contextual Retrieval as discussed in Anthropic's blog using fully open source models!

If you want to learn more about how to best use open models refer to our [docs here](/docs) !

***


# How To Improve Search With Rerankers
Source: https://docs.together.ai/docs/how-to-improve-search-with-rerankers

Learn how you can improve semantic search quality with reranker models!

In this guide we will use a reranker model to improve the results produced from a simple semantic search workflow. To get a better understanding of how semantic search works please refer to the [Cookbook here](https://github.com/togethercomputer/together-cookbook/blob/main/Semantic_Search.ipynb) .

A reranker model operates by looking at the query and the retrieved results from the semantic search pipeline one by one and assesses how relevant the returned result is to the query. Because the reranker model can spend compute assessing the query with the returned result at the same time it can better judge how relevant the words and meanings in the query are to individual documents. This also means that rerankers are computationally expensive and slower - thus they cannot be used to rank every document in our database.

We run a semantic search process to obtain a list of 15-25 candidate objects that are similar "enough" to the query and then use the reranker as a fine-toothed comb to pick the top 5-10 objects that are actually closest to our query.

We will be using the [Salesforce Llama Rank](/docs/rerank-overview) reranker model.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ad1d5a26de9ede54c2151b0e4a4ac56d" alt="How to improve search with rerankers" data-og-width="3205" width="3205" data-og-height="961" height="961" data-path="images/how-to-improve-search-with-rerankers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=624f30da905533bd641cc0cd21159b26 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=de91cec6e273fc75ae8f6fdbb620b8a6 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=a4c24541eb84bb437675e2d213d2c173 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=cf0a5651d917416f9830077c0e3e02d6 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=811e20c89ea9cec15cc638a8c053da9a 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=059eaedb1926ebbefab0c0512cbd43a5 2500w" />
</Frame>

## Download and View the Dataset

```bash Shell theme={null}
wget https://raw.githubusercontent.com/togethercomputer/together-cookbook/refs/heads/main/datasets/movies.json
mkdir datasets
mv movies.json datasets/movies.json
```

```py Python theme={null}
import json
import together, os
from together import Together

# Paste in your Together AI API Key or load it
TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

with open("./datasets/movies.json", "r") as file:
    movies_data = json.load(file)

movies_data[10:13]
```

Our dataset contains information about popular movies:

```
[{'title': 'Terminator Genisys',
  'overview': "The year is 2029. John Connor, leader of the resistance continues the war against the machines. At the Los Angeles offensive, John's fears of the unknown future begin to emerge when TECOM spies reveal a new plot by SkyNet that will attack him from both fronts; past and future, and will ultimately change warfare forever.",
  'director': 'Alan Taylor',
  'genres': 'Science Fiction Action Thriller Adventure',
  'tagline': 'Reset the future'},
 {'title': 'Captain America: Civil War',
  'overview': 'Following the events of Age of Ultron, the collective governments of the world pass an act designed to regulate all superhuman activity. This polarizes opinion amongst the Avengers, causing two factions to side with Iron Man or Captain America, which causes an epic battle between former allies.',
  'director': 'Anthony Russo',
  'genres': 'Adventure Action Science Fiction',
  'tagline': 'Divided We Fall'},
 {'title': 'Whiplash',
  'overview': 'Under the direction of a ruthless instructor, a talented young drummer begins to pursue perfection at any cost, even his humanity.',
  'director': 'Damien Chazelle',
  'genres': 'Drama',
  'tagline': 'The road to greatness can take you to the edge.'}]
```

## Implement Semantic Search Pipeline

Below we implement a simple semantic search pipeline:

1. Embed movie documents + query
2. Obtain a list of movies ranked based on cosine similarities between the query and movie vectors.

```py Python theme={null}
# This function will be used to access the Together API to generate embeddings for the movie plots

from typing import List


def generate_embeddings(
    input_texts: List[str],
    model_api_string: str,
) -> List[List[float]]:
    """Generate embeddings from Together python library.

    Args:
        input_texts: a list of string input texts.
        model_api_string: str. An API string for a specific embedding model of your choice.

    Returns:
        embeddings_list: a list of embeddings. Each element corresponds to the each input text.
    """
    together_client = together.Together(api_key=TOGETHER_API_KEY)
    outputs = together_client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    )
    return [x.embedding for x in outputs.data]


to_embed = []
for movie in movies_data[:1000]:
    text = ""
    for field in ["title", "overview", "tagline"]:
        value = movie.get(field, "")
        text += str(value) + " "
    to_embed.append(text.strip())

# Use bge-base-en-v1.5 model to generate embeddings
embeddings = generate_embeddings(to_embed, "BAAI/bge-base-en-v1.5")
```

Next we implement a function that when given the above embeddings and a test query will return indices of most semantically similar data objects:

```py Python theme={null}
def retrieve(
    query: str,
    top_k: int = 5,
    index: np.ndarray = None,
) -> List[int]:
    """
    Retrieve the top-k most similar items from an index based on a query.
    Args:
        query (str): The query string to search for.
        top_k (int, optional): The number of top similar items to retrieve. Defaults to 5.
        index (np.ndarray, optional): The index array containing embeddings to search against. Defaults to None.
    Returns:
        List[int]: A list of indices corresponding to the top-k most similar items in the index.
    """

    query_embedding = generate_embeddings([query], "BAAI/bge-base-en-v1.5")[0]
    similarity_scores = cosine_similarity([query_embedding], index)

    return np.argsort(-similarity_scores)[0][:top_k]
```

We will use the above function to retrieve 25 movies most similar to our query:

```py Python theme={null}
indices = retrieve(
    query="super hero mystery action movie about bats",
    top_k=25,
    index=embeddings,
)
```

This will give us the following movie indices and movie titles:

```
array([ 13, 265, 451,  33,  56,  17, 140, 450,  58, 828, 227,  62, 337,
       172, 724, 424, 585, 696, 933, 996, 932, 433, 883, 420, 744])
```

```py Python theme={null}
# Get the top 25 movie titles that are most similar to the query - these will be passed to the reranker
top_25_sorted_titles = [movies_data[index]["title"] for index in indices[0]][
    :25
]
```

```
['The Dark Knight',
 'Watchmen',
 'Predator',
 'Despicable Me 2',
 'Night at the Museum: Secret of the Tomb',
 'Batman v Superman: Dawn of Justice',
 'Penguins of Madagascar',
 'Batman & Robin',
 'Batman Begins',
 'Super 8',
 'Megamind',
 'The Dark Knight Rises',
 'Batman Returns',
 'The Incredibles',
 'The Raid',
 'Die Hard: With a Vengeance',
 'Kick-Ass',
 'Fantastic Mr. Fox',
 'Commando',
 'Tremors',
 'The Peanuts Movie',
 'Kung Fu Panda 2',
 'Crank: High Voltage',
 'Men in Black 3',
 'ParaNorman']
```

Notice here that not all movies in our top 25 have to do with our query - super hero mystery action movie about bats. This is because semantic search capture the "approximate" meaning of the query and movies.

The reranker can more closely determine the similarity between these 25 candidates and rerank which ones deserve to be atop our list.

## Use Llama Rank to Rerank Top 25 Movies

Treating the top 25 matching movies as good candidate matches, potentially with irrelevant false positives, that might have snuck in we want to have the reranker model look and rerank each based on similarity to the query.

```py Python theme={null}
query = "super hero mystery action movie about bats"  # we keep the same query - can change if we want

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=top_25_sorted_titles,
    top_n=5,  # we only want the top 5 results
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {top_25_sorted_titles[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```

This will give us a reranked list of movies as shown below:

```
Document Index: 12
Document: Batman Returns
Relevance Score: 0.35380946383813044

Document Index: 8
Document: Batman Begins
Relevance Score: 0.339339115127178

Document Index: 7
Document: Batman & Robin
Relevance Score: 0.33013392395016167

Document Index: 5
Document: Batman v Superman: Dawn of Justice
Relevance Score: 0.3289763252445171

Document Index: 9
Document: Super 8
Relevance Score: 0.258483721657576
```

Here we can see that that reranker was able to improve the list by demoting irrelevant movies like Watchmen, Predator, Despicable Me 2, Night at the Museum: Secret of the Tomb, Penguins of Madagascar, further down the list and promoting Batman Returns, Batman Begins, Batman & Robin, Batman v Superman: Dawn of Justice to the top of the list!

The `bge-base-en-v1.5` embedding model gives us a fuzzy match to concepts mentioned in the query, the Llama-Rank-V1 reranker then imrpoves the quality of our list further by spending more compute to resort the list of movies.

Learn more about how to use reranker models in the [docs here](/docs/rerank-overview) !

***


# How to use Cline with DeepSeek V3 to build faster
Source: https://docs.together.ai/docs/how-to-use-cline

Use Cline (an AI coding agent) with DeepSeek V3 (a powerful open source model) to code faster.

Cline is a popular open source AI coding agent with nearly 2 million installs that is installable through any IDE including VS Code, Cursor, and Windsurf. In this quick guide, we want to take you through how you can combine Cline with powerful open source models on Together AI like DeepSeek V3 to supercharge your development process.

With Cline's agent, you can ask it to build features, fix bugs, or start new projects for you – and it's fully transparent in terms of the cost and tokens used as you use it. Here's how you can start using it with DeepSeek V3 on Together AI:

### 1. Install Cline

Navigate to [https://cline.bot/](https://cline.bot/) to install Cline in your preferred IDE.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cb016220da9ef86b8c3d676d47258b66" alt="" data-og-width="2922" width="2922" data-og-height="2428" height="2428" data-path="images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=3ef9417a598aa6d878f17ead86b18bd4 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=63be1b6d752aa29af2f7c06881c93ba7 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b3376e576e797f15eee3b892b28f6ffe 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c10e47a92786e1cf3a4be14e9f03cd4f 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d75151d884fb6a9353a0ff69ccfbae81 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/3a344cdc2e177da38ae745e627c90052375f7ef394151410723deef1629308bd-1-cline-homepage.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=f22cab2e6a301255dc31f7ff889123b9 2500w" />
</Frame>

### 2. Select Cline

After it's installed, select Cline from the menu of your IDE to configure it.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=9a332b14348eed5ceaf5ef1e20c87ca1" alt="" data-og-width="2586" width="2586" data-og-height="2476" height="2476" data-path="images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8972e49a62c3033f05d70cbcfe2db8ec 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8ce72d4fef3ab9a4e7e68f08f1f82da6 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a151d274b3e5df18f097e2867088cec3 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=49ee5dcaf43d4d1bb0d578d42be76741 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0ea67175a06aad22e2109986aa64d1ca 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/a78933f0e35bade4b946f7b2995730e2e4554694fc6cd2c596f3b4584abde5be-2-open-cline.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=02314c65bed8b47a8ac0a46a79c3c0f8 2500w" />
</Frame>

### 3. Configure Together AI & DeepSeek V3

Click "Use your own API key". After this, select Together as the API Provider, paste in your [Together API key](https://api.together.xyz/settings/api-keys), and type in any of our models to use. We recommend using `deepseek-ai/DeepSeek-V3` as its a powerful coding model.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0a07e5d79ec8ab98d1b3dc0beb5be426" alt="" data-og-width="1330" width="1330" data-og-height="1632" height="1632" data-path="images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=d84cd10832842a2263d0ffccde061d4a 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=7f5a39347baa3fcbd28617a4fe278ff5 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0cba6f483bf913162823056b69c8e82c 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b4606469d26d77b553fbed3bf33f07a6 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=0c11e3aef7950e29c33fdd551c655a10 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/297b1c91ff9103ff87d50a8a1fb75dc29588fd47124fa081bac1de5ed1acece5-3-put-in-together.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=c111f40eceb970815ba3aa933263d158 2500w" />
</Frame>

That's it! You can now build faster with one of the most popular coding agents running a fast, secure, and private open source model hosted on Together AI.


# How to use OpenCode with Together AI to build faster
Source: https://docs.together.ai/docs/how-to-use-opencode

Learn how to combine OpenCode, a powerful terminal-based AI coding agent, with Together AI models like DeepSeek V3 to supercharge your development workflow.

# How to use OpenCode with Together AI to build faster

OpenCode is a powerful AI coding agent built specifically for the terminal, offering a native TUI experience with LSP support and multi-session capabilities. In this guide, we'll show you how to combine OpenCode with powerful open source models on Together AI like DeepSeek V3 and DeepSeek R1 to supercharge your development workflow directly from your terminal.

With OpenCode's agent, you can ask it to build features, fix bugs, explain codebases, and start new projects – all while maintaining full transparency in terms of cost and token usage. Here's how you can start using it with Together AI's models:

## 1. Install OpenCode

Install OpenCode directly from your terminal with a single command:

```bash  theme={null}
curl -fsSL https://opencode.ai/install | bash
```

This will install OpenCode and make it available system-wide.

## 2. Launch OpenCode

Navigate to your project directory and launch OpenCode:

```bash  theme={null}
cd your-project
opencode
```

OpenCode will start with its native terminal UI interface, automatically detecting and loading the appropriate Language Server Protocol (LSP) for your project.

## 3. Configure Together AI

When you first run OpenCode, you'll need to configure it to use Together AI as your model provider. Follow these steps:

* **Set up your API provider**: Configure OpenCode to use Together AI
  * **opencode auth login**

<img src="https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=d74486f60e3750610a73eb638f84fca2" alt="image.png" data-og-width="1074" width="1074" data-og-height="592" height="592" data-path="images/image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?w=280&fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=59d77b346fc498acc1dae578ec31bcdf 280w, https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?w=560&fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=6bbb7be6d2284764ad7f13ae2563eada 560w, https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?w=840&fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=914af9deff40e0dd278c8147597c0634 840w, https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?w=1100&fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=60bc3a7be49c4ea897abc6467ed91d3f 1100w, https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?w=1650&fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=41ce731a7ccf926115bdc01494d3f170 1650w, https://mintcdn.com/togetherai-52386018/pmxzM0i08cnkbXYV/images/image.png?w=2500&fit=max&auto=format&n=pmxzM0i08cnkbXYV&q=85&s=471bc1813d632957d8654c956f2d7d96 2500w" />

> To find the Together AI provider you will need to scroll the provider list of simply type together

<img src="https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=38a811f9cfe0a8292fd016900a68de16" alt="Screenshot 2025-08-12 at 12.36.16.png" data-og-width="1100" width="1100" data-og-height="398" height="398" data-path="images/Screenshot2025-08-12at12.36.16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?w=280&fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=402f1a01fbd1fd35d0db9f063f78df29 280w, https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?w=560&fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=04145c5db4744317ef73eef94f2dde15 560w, https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?w=840&fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=b710efb88d59deb0d56a66b1f97fcfbe 840w, https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?w=1100&fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=ee7079685eb2944e09f0e34c146bcd58 1100w, https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?w=1650&fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=2a92c6eafa2b11ab135890d348abb8c3 1650w, https://mintcdn.com/togetherai-52386018/YUxXzGkuS_AWKqd4/images/Screenshot2025-08-12at12.36.16.png?w=2500&fit=max&auto=format&n=YUxXzGkuS_AWKqd4&q=85&s=d96915ff6c3b80d1d6c1b1d385db247f 2500w" />

* **Add your API key**: Get your [Together AI API key](https://api.together.xyz/settings/api-keys) and paste it into the opencode terminal
* **Select a model**: Choose from powerful models like:
  * `deepseek-ai/DeepSeek-V3` - Excellent for general coding tasks
  * `deepseek-ai/DeepSeek-R1` - Advanced reasoning capabilities
  * `meta-llama/Llama-3.3-70B-Instruct-Turbo` - Fast and efficient
  * `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` - Specialized coding model

## 4. Bonus: install the opencode vs-code extension

For developers who prefer working within VS Code, OpenCode offers a dedicated extension that integrates seamlessly into your IDE workflow while still leveraging the power of the terminal-based agent.

Install the extension: Search for "opencode" in the VS Code Extensions Marketplace or directly use this link:

* [https://open-vsx.org/extension/sst-dev/opencode](https://open-vsx.org/extension/sst-dev/opencode)

## Key Features & Usage

### Native Terminal Experience

OpenCode provides a responsive, native terminal UI that's fully themeable and integrated into your command-line workflow.

### Plan Mode vs Build Mode

Switch between modes using the **Tab** key:

* **Plan Mode**: Ask OpenCode to create implementation plans without making changes
* **Build Mode**: Let OpenCode directly implement features and make code changes

### File References with Fuzzy Search

Use the `@` key to fuzzy search and reference files in your project:

```
How is authentication handled in @packages/functions/src/api/index.ts
```

## Best Practices

### Give Detailed Context

Talk to OpenCode like you're talking to a junior developer:

```
When a user deletes a note, flag it as deleted in the database instead of removing it. 
Then create a "Recently Deleted" screen where users can restore or permanently delete notes.
Use the same design patterns as our existing settings page.
```

### Use Examples and References

Provide plenty of context and examples:

```
Add error handling to the API similar to how it's done in @src/utils/errorHandler.js
```

### Iterate on Plans

In Plan Mode, review and refine the approach before implementation:

```
That looks good, but let's also add input validation and rate limiting
```

## Model Recommendations

* **DeepSeek V3** (`deepseek-ai/DeepSeek-V3`): \$1.25 per million tokens, excellent balance of performance and cost
* **DeepSeek R1** (`deepseek-ai/DeepSeek-R1`): $3.00-$7.00 per million tokens, advanced reasoning for complex problems
* **Llama 3.3 70B** (`meta-llama/Llama-3.3-70B-Instruct-Turbo`): \$0.88 per million tokens, fast and cost-effective

## Getting Started

1. Install OpenCode: `curl -fsSL https://opencode.ai/install | bash`
2. Navigate to your project: `cd your-project`
3. Launch OpenCode: `opencode`
4. Configure Together AI with your API key
5. Start building faster with AI assistance!

That's it! You now have one of the most powerful terminal-based AI coding agents running with fast, secure, and private open source models hosted on Together AI. OpenCode's native terminal interface combined with Together AI's powerful models will transform your development workflow.


# How to use Qwen Code with Together AI for enhanced development workflow
Source: https://docs.together.ai/docs/how-to-use-qwen-code

Learn how to configure Qwen Code, a powerful AI-powered command-line workflow tool, with Together AI models to supercharge your coding workflow with advanced code understanding and automation.

# How to use Qwen Code with Together AI for enhanced development workflow

Qwen Code is a powerful command-line AI workflow tool specifically optimized for code understanding, automated tasks, and intelligent development assistance. While it comes with built-in Qwen OAuth support, you can also configure it to use Together AI's extensive model selection for even more flexibility and control over your AI coding experience.

In this guide, we'll show you how to set up Qwen Code with Together AI's powerful models like DeepSeek V3, Llama 3.3 70B, and specialized coding models to enhance your development workflow beyond traditional context window limits.

## Why Use Qwen Code with Together AI?

* **Model Choice**: Access to a wide variety of models beyond just Qwen models
* **Transparent Pricing**: Clear token-based pricing with no surprises
* **Enterprise Control**: Use your own API keys and have full control over usage
* **Specialized Models**: Access to coding-specific models like Qwen3-Coder and DeepSeek variants

## 1. Install Qwen Code

Install Qwen Code globally via npm:

```bash  theme={null}
npm install -g @qwen-code/qwen-code@latest
```

Verify the installation:

```bash  theme={null}
qwen --version
```

**Prerequisites**: Ensure you have Node.js version 20 or higher installed.

## 2. Configure Together AI

Instead of using the default Qwen OAuth, you'll configure Qwen Code to use Together AI's OpenAI-compatible API.

### Method 1: Environment Variables (Recommended)

Set up your environment variables:

```bash  theme={null}
export OPENAI_API_KEY="your_together_api_key_here"
export OPENAI_BASE_URL="https://api.together.xyz/v1"
export OPENAI_MODEL="your_chosen_model"
```

### Method 2: Project .env File

Create a `.env` file in your project root:

```env  theme={null}
OPENAI_API_KEY=your_together_api_key_here
OPENAI_BASE_URL=https://api.together.xyz/v1
OPENAI_MODEL=your_chosen_model
```

### Get Your Together AI Credentials

1. **API Key**: Get your [Together AI API key](https://api.together.xyz/settings/api-keys)
2. **Base URL**: Use `https://api.together.xyz/v1` for Together AI
3. **Model**: Choose from [Together AI's model catalog](https://www.together.ai/models)

## 3. Choose Your Model

Select from Together AI's powerful model selection:

### Recommended Models for Coding

**For General Development:**

* `deepseek-ai/DeepSeek-V3` - Excellent balance of performance and cost (\$1.25/M tokens)
* `meta-llama/Llama-3.3-70B-Instruct-Turbo` - Fast and cost-effective (\$0.88/M tokens)

**For Advanced Coding Tasks:**

* `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` - Specialized for complex coding (\$2.00/M tokens)
* `deepseek-ai/DeepSeek-R1` - Advanced reasoning capabilities ($3.00-$7.00/M tokens)

### Example Configuration

```bash  theme={null}
export OPENAI_API_KEY="your_together_api_key"
export OPENAI_BASE_URL="https://api.together.xyz/v1"
export OPENAI_MODEL="deepseek-ai/DeepSeek-V3"
```

## 4. Launch and Use Qwen Code

Navigate to your project and start Qwen Code:

```bash  theme={null}
cd your-project/
qwen
```

You're now ready to use Qwen Code with Together AI models!

## Advanced Tips

### Token Optimization

* Use `/compress` to maintain context while reducing token usage
* Set appropriate session limits based on your Together AI plan
* Monitor usage with `/stats` command

### Model Selection Strategy

* Use **DeepSeek V3** for general coding tasks
* Switch to **Qwen3-Coder** for complex code generation
* Use **Llama 3.3 70B** for faster, cost-effective operations

### Context Window Management

Qwen Code is designed to handle large codebases beyond traditional context limits:

* Automatically chunks and processes large files
* Maintains conversation context across multiple API calls
* Optimizes token usage through intelligent compression

## Troubleshooting

### Common Issues

**Authentication Errors:**

* Verify your Together AI API key is correct
* Ensure `OPENAI_BASE_URL` is set to `https://api.together.xyz/v1`
* Check that your API key has sufficient credits

**Model Not Found:**

* Verify the model name exists in [Together AI's catalog](https://www.together.ai/models)
* Ensure the model name is exactly as listed (case-sensitive)

## Getting Started Checklist

1. ✅ Install Node.js 20+ and Qwen Code
2. ✅ Get your Together AI API key
3. ✅ Set environment variables or create `.env` file
4. ✅ Choose your preferred model from Together AI
5. ✅ Launch Qwen Code in your project directory
6. ✅ Start coding with AI assistance!

That's it! You now have Qwen Code powered by Together AI's advanced models, giving you unprecedented control over your AI-assisted development workflow with transparent pricing and model flexibility.


# Images
Source: https://docs.together.ai/docs/images-overview

Generate high-quality images from text + image prompts.

## Generating an image

To query an image model, use the `.images` method and specify the image model you want to use.

<CodeGroup>
  ```py Python theme={null}
  client = Together()

  # Generate an image from a text prompt
  response = client.images.generate(
      prompt="A serene mountain landscape at sunset with a lake reflection",
      model="black-forest-labs/FLUX.1-schnell",
      steps=4,
  )

  print(f"Image URL: {response.data[0].url}")
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      prompt: "A serene mountain landscape at sunset with a lake reflection",
      model: "black-forest-labs/FLUX.1-schnell",
      steps: 4,
    });

    console.log(response.data[0].url);
  }

  main();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A serene mountain landscape at sunset with a lake reflection",
         "steps": 4
       }'
  ```
</CodeGroup>

Example response structure and output:

```json  theme={null}
{
  "id": "oFuwv7Y-2kFHot-99170ebf9e84e0ce-SJC",
  "model": "black-forest-labs/FLUX.1-schnell",
  "data": [
    {
      "index": 0,
      "url": "https://api.together.ai/v1/images/..."
    }
  ]
}
```

<img src="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=4d99c87bb633262fdb932f3f9a9fa436" alt="Reference image: image-overview1.png" width="350" data-og-width="1024" data-og-height="1024" data-path="images/image-overview1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=280&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=8a8cc7b204ced18a0f54475d6c29d083 280w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=560&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=7b9316fc8048f5099c9fc93ea7d0f8f9 560w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=840&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=6c4e6b322d745bde355f796f173f3acf 840w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=1100&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=b508dae30e522a828fec8a36d1bcfdff 1100w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=1650&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=3975e1d0af34f521c5bdf143df8cd11a 1650w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=2500&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=0130a5593fd60a023b9e0960a4824464 2500w" />

## Provide reference image

Use a reference image to guide the generation:

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.1-kontext-pro",
      width=1024,
      height=768,
      prompt="Transform this into a watercolor painting",
      image_url="https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await together.images.create({
    model: "black-forest-labs/FLUX.1-kontext-pro",
    width: 1024,
    height: 768,
    prompt: "Transform this into a watercolor painting",
    image_url:
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
  });
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-kontext-pro",
         "width": 1024,
         "height": 768,
         "prompt": "Transform this into a watercolor painting",
         "image_url": "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
       }'
  ```
</CodeGroup>

Example output:

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=2f4036b77e23ee90388200b71abfc7af" alt="Reference image: reference_image.png" data-og-width="989" width="989" data-og-height="360" height="360" data-path="images/reference_image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=09e764929470af3788d2be654ad50464 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=e45d47b542c051c2e2f375a4f357a79f 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=748b9876fb4984438c0acc635fa2314d 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=da6a7a5a109aa3c7321871e17e020293 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=eb058db20b8898e80f62a2da77f23b6c 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4a5ba1b910dba43bee558540f35124f9 2500w" />

## Supported Models

See our [models page](/docs/serverless-models#image-models) for supported image models.

## Parameters

| Parameter         | Type    | Description                                                                              | Default      |
| ----------------- | ------- | ---------------------------------------------------------------------------------------- | ------------ |
| `prompt`          | string  | Text description of the image to generate                                                | **Required** |
| `model`           | string  | Model identifier                                                                         | **Required** |
| `width`           | integer | Image width in pixels                                                                    | 1024         |
| `height`          | integer | Image height in pixels                                                                   | 1024         |
| `n`               | integer | Number of images to generate (1-4)                                                       | 1            |
| `steps`           | integer | Diffusion steps (higher = better quality, slower)                                        | 1-50         |
| `seed`            | integer | Random seed for reproducibility                                                          | any          |
| `negative_prompt` | string  | What to avoid in generation                                                              | -            |
| `frame_images`    | array   | **Required for Kling model.** Array of images to guide video generation, like keyframes. | -            |

* `prompt` is required for all models except Kling
* `width` and `height` will rely on defaults unless otherwise specified - options for dimensions differ by model
* Flux Schnell and Kontext \[Pro/Max/Dev] models use the `aspect_ratio` parameter to set the output image size whereas Flux.1 Pro, Flux 1.1 Pro, and Flux.1 Dev use `width` and `height` parameters.

## Generating Multiple Variations

Generate multiple variations of the same prompt to choose from:

<CodeGroup>
  ```py Python theme={null}
  response = client.images.generate(
      prompt="A cute robot assistant helping in a modern office",
      model="black-forest-labs/FLUX.1-schnell",
      n=4,
      steps=4,
  )

  print(f"Generated {len(response.data)} variations")
  for i, image in enumerate(response.data):
      print(f"Variation {i+1}: {image.url}")
  ```

  ```ts TypeScript theme={null}
  const response = await together.images.create({
    prompt: "A cute robot assistant helping in a modern office",
    model: "black-forest-labs/FLUX.1-schnell",
    n: 4,
    steps: 4,
  });

  console.log(`Generated ${response.data.length} variations`);

  response.data.forEach((image, i) => {
    console.log(`Variation ${i + 1}: ${image.url}`);
  });
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A cute robot assistant helping in a modern office",
         "n": 4,
         "steps": 4
       }'
  ```
</CodeGroup>

Example output:
<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4662cd539affb47b8b31d363690a809b" alt="Multiple generated image variations" data-og-width="1166" width="1166" data-og-height="1190" height="1190" data-path="images/variations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=93ce50657e7617eede86cdc398a8cae8 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=5faa41043c62d7de67af33a993ecdde9 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=52a3acce05e8bcf79199cdb6017f7532 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=97a98672d86219304b56546b0f25d197 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=aa884d182ac397f5d42095d73662461f 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=727080d2779f9ca84713b1c4e0b92c9d 2500w" />

## Custom Dimensions & Aspect Ratios

Different aspect ratios for different use cases:

<CodeGroup>
  ```py Python theme={null}
  # Square - Social media posts, profile pictures
  response_square = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=1024,
      height=1024,
      steps=4,
  )

  # Landscape - Banners, desktop wallpapers
  response_landscape = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=1344,
      height=768,
      steps=4,
  )

  # Portrait - Mobile wallpapers, posters
  response_portrait = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=768,
      height=1344,
      steps=4,
  )
  ```

  ```ts TypeScript theme={null}
  // Square - Social media posts, profile pictures
  const response_square = await together.images.create({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1024,
    height: 1024,
    steps: 4,
  });

  // Landscape - Banners, desktop wallpapers
  const response_landscape = await together.images.create({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1344,
    height: 768,
    steps: 4,
  });

  // Portrait - Mobile wallpapers, posters
  const response_portrait = await together.images.create({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 768,
    height: 1344,
    steps: 4,
  });
  ```

  ```curl cURL theme={null}
  # Square - Social media posts, profile pictures
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 1024,
         "height": 1024,
         "steps": 4
       }'

  # Landscape - Banners, desktop wallpapers
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 1344,
         "height": 768,
         "steps": 4
       }'

  # Portrait - Mobile wallpapers, posters
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 768,
         "height": 1344,
         "steps": 4
       }'
  ```
</CodeGroup>

<img src="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=4f81f0c9d03a7334a193c2416557a0be" alt="Reference image: dims.png" data-og-width="1391" width="1391" data-og-height="990" height="990" data-path="images/dims.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=280&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=fb9e0821836ed9861a522698f5948224 280w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=560&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=31194ec41bed9963e9a7324149eb1551 560w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=840&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=062be3089cbc119efac695191a12e5bf 840w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=1100&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=0d77614e227264a1c2c7bae6d2fe12ad 1100w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=1650&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=a205e3cd5d3de30a59af5ddc0cfbadf4 1650w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=2500&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=868d9308fc95e6b4c518cb98a3b01797 2500w" />

## Quality Control with Steps

Compare different step counts for quality vs. speed:

```python  theme={null}
import time

prompt = "A majestic mountain landscape"
step_counts = [1, 6, 12]

for steps in step_counts:
    start = time.time()
    response = client.images.generate(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell",
        steps=steps,
        seed=42,  # Same seed for fair comparison
    )
    elapsed = time.time() - start
    print(f"Steps: {steps} - Generated in {elapsed:.2f}s")
```

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=c6dad7983bb96503032966b36ad41716" alt="Reference image: steps.png" data-og-width="1458" width="1458" data-og-height="511" height="511" data-path="images/steps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4ac6dc13d95356376c441407f9e3aea3 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4441ef2ff0f4f656dfe005c46d001b1d 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=ed6e70593fcdbd62d8387a57b1e05e4c 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=b28573546f8b32bbb049a6f7d5de7dd0 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=60a317f47e10d95ed43d6e32e194fc2b 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/steps.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=d32a39c2ef3ac49c5d0e48e6b3f2d87f 2500w" />

## Base64 Images

If you prefer the image data to be embedded directly in the response, set `response_format` to "base64".

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.1-schnell",
      prompt="a cat in outer space",
      response_format="base64",
  )

  print(response.data[0].b64_json)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.images.create({
    model: "black-forest-labs/FLUX.1-schnell",
    prompt: "A cat in outer space",
    response_format: "base64",
  });

  console.log(response.data[0].b64_json);
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A cat in outer space",
         "response_format": "base64"
       }'
  ```
</CodeGroup>

When you do, the model response includes a new `b64_json` field that contains the image encoded as a base64 string.

```json  theme={null}
{
  "id": "oHpD53L-2kFHot-998e0de9fe14d8a1-SEA",
  "model": "black-forest-labs/FLUX.1-schnell",
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAA..."
    }
  ]
}
```

## Safety Checker

We have a built in safety checker that detects NSFW words but you can disable it by passing in `disable_safety_checker=True`. This works for every model except Flux Schnell Free and Flux Pro. If the safety checker is triggered and not disabled, it will return a `422 Unprocessable Entity`.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.images.generate(
      prompt="a flying cat",
      model="black-forest-labs/FLUX.1-schnell",
      steps=4,
      disable_safety_checker=True,
  )

  print(response.data[0].url)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      prompt: "a flying cat",
      model: "black-forest-labs/FLUX.1-schnell",
      steps: 4,
      disable_safety_checker: true,
    });

    console.log(response.data[0].url);
  }

  main();
  ```
</CodeGroup>

## Troubleshooting

**Image doesn't match prompt well**

* Make prompt more descriptive and specific
* Add style references (e.g., "National Geographic style")
* Use negative prompts to exclude unwanted elements
* Try increasing steps to 30-40

**Poor image quality**

* Increase `steps` to 30-40 for production
* Add quality modifiers: "highly detailed", "8k", "professional"
* Use negative prompt: "blurry, low quality, distorted, pixelated"
* Try a higher-tier model

**Inconsistent results**

* Use `seed` parameter for reproducibility
* Keep the same seed when testing variations
* Generate multiple variations with `n` parameter

**Wrong dimensions or aspect ratio**

* Specify `width` and `height` explicitly
* Common ratios:
  * Square: 1024x1024
  * Landscape: 1344x768
  * Portrait: 768x1344
* Ensure dimensions are multiples of 8


# Inference FAQs
Source: https://docs.together.ai/docs/inference-faqs



## Model Selection and Availability

### What models are available for inference on Together?

Together hosts a wide range of open-source models and you can view the latest inference models [here](https://docs.together.ai/docs/serverless-models).

### Which model should I use?

The world of AI evolves at a rapid pace, and the often overwhelming flow of new information can make it difficult to find exactly what you need for what you want to do.

Together AI has built Which LLM to help you cut through the confusion. Just tell us what you need/want to do, and we'll tell you which model is the best match.

Visit [whichllm.together.ai](https://whichllm.together.ai/) to find the right model for your use case.

Together AI supports over 200+ open-source models with a wide range of capabilities: Chat, Image, Vision, Audio, Code, Language, Moderation, Embedding, Rerank.

#### Free Models Available

Together AI offers several free models that you can use without cost:

##### Chat/Language Models:

* **DeepSeek R1 Distilled Llama 70B Free** - A free endpoint to experiment with reasoning models that beats GPT-4o on math and matches o1-mini on coding

* **Llama 3.3 70B Instruct Turbo Free** - Free endpoint for this 70B multilingual LLM optimized for dialogue

##### Image Generation:

* **FLUX.1 \[schnell] Free** - Free endpoint for the SOTA open-source image generation model by Black Forest Labs

**Note:** Free model endpoints have reduced rate limits and performance compared to paid Turbo endpoints, but provide an excellent way to experiment and test capabilities before committing to paid services.

## Model Parameters and Usage

### What is the maximum context window supported by Together models?

The maximum context window varies significantly by model. Refer to the specific model's documentation or the inference models [page](https://docs.together.ai/docs/serverless-models) for the exact context length supported by each model.

### Where can I find default parameter values for a model?

Default parameter values for a model can be found in the `generation_config.json` file on Hugging Face. For example, the configuration for Llama 3.3 70B Instruct shows defaults like temperature: 0.6 and top\_p: 0.9. If not defined, no value is passed for that parameter.

### How do I send a request to an inference endpoint?

You can use the OpenAI-compatible API. Example using curl:

```bash  theme={null}
curl https://api.together.xyz/v1/chat/completions \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
         "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
         "messages": [{"role": "user", "content": "Hello!"}]
       }'
```

More examples in Python and TypeScript are available [here](https://docs.together.ai/docs/openai-api-compatibility).

### Do you support function calling or tool use?

Function calling is natively supported for some models (see [here](https://docs.together.ai/docs/function-calling#function-calling)) but structured prompting can simulate function-like behavior.

### Function Calls Not Returned in Response "message.content"

Models that support Function Calling return any tool calls in a separate part of the model response, not inside of `message.content`. Some models will return "None" for this if any function calls are made.

Any tool calls instead will be found in:

`message.tool_calls[0].function.name`

For example, when making a function call, `message.content` may be None, but the function name will be in `message.tool_calls[0].function.name`.

### Do you support structured outputs or JSON mode?

Yes, you can use JSON mode to get structured outputs from LLMs like DeepSeek V3 & Llama 3.3. See more [here](https://docs.together.ai/docs/json-mode).

#### Troubleshooting Structured Output Generation

When working with structured outputs, you may encounter issues where your generated JSON gets cut off or contains errors. Here are key considerations:

* **Token Limits**: Check the maximum token limit of your model and ensure you're under it. Model specifications are available in our [serverless models documentation](https://docs.together.ai/docs/serverless-models).

* **Malformed JSON**: Validate your example JSON before using it in prompts. The model follows your example exactly, including syntax errors. Common symptoms include unterminated strings, repeated newlines, incomplete structures, or truncated output with 'stop' finish reason.

## Performance and Optimization

### What kind of latency can I expect for inference requests?

Latency depends on the model and prompt length. Smaller models like Mistral may respond in less than 1 second, while larger MoE models like Mixtral may take several seconds. Prompt caching and streaming can help reduce perceived latency.

### Is Together suitable for high-throughput workloads?

Yes. Together supports production-scale inference. For high-throughput applications (e.g., over 100 RPS), [contact](https://www.together.ai/contact) the Together team for dedicated support and infrastructure.

### Does Together support streaming responses?

Yes. You can receive streamed tokens by setting `"stream": true` in your request. This allows you to begin processing output as soon as it is generated.

### Can I use quantized models for faster inference?

Yes. Together hosts some models with quantized weights (e.g., FP8, FP16, INT4) for faster and more memory-efficient inference. Support varies by model.

### Can I cache prompts or use speculative decoding?

Yes. Together supports optimizations like prompt caching and speculative decoding for models that allow it, reducing latency and improving throughput.

### Can I run batched or parallel inference requests?

Yes. Together supports batching and high-concurrency usage. You can send parallel requests from your client and take advantage of backend batching. See [Batch Inference](https://docs.together.ai/docs/batch-inference#batch-inference) for more details.

## Data Privacy and Security

### Is my data stored or logged?

Together does not store your input or output by default. Temporary caching may be used for performance unless otherwise configured.

### Will my data be used to train other models?

Data sharing for training other models is opt-in and not enabled by default. You can check or modify this setting in your [account profile](https://api.together.ai/settings/profile) under Privacy & Security. See our [privacy policy](https://www.together.ai/privacy) for more details.

### Can I run inference in my own VPC or on-premise?

Yes. Together supports private networking VPC-based deployments for enterprise customers requiring data residency or regulatory compliance. [Contact us](https://www.together.ai/contact) for more information.

## Billing and Limits

### How is inference usage billed?

Inference is billed per input and output token, with rates varying by model. Refer to the pricing [page](https://www.together.ai/pricing) for current pricing details.

### What happens if I exceed my rate limit or quota?

You will receive a 429 Too Many Requests error. You can request higher limits via the Together dashboard or by contacting [support](https://www.together.ai/contact).

## Integrations and Support

### Can I use Together inference with LangChain or LlamaIndex?

Yes. Together is compatible with LangChain via the OpenAI API interface. Set your Together API key and model name in your environment or code.

See more about all available integrations: [Langchain](https://docs.together.ai/docs/integrations#langchain), [LlamaIndex](https://docs.together.ai/docs/integrations#llamaindex), [Hugging Face](https://docs.together.ai/docs/integrations#huggingface), [Vercel AI SDK](https://docs.together.ai/docs/integrations#vercel-ai-sdk).

### How does Together ensure the uptime and reliability of its inference endpoints?

Together aims for high reliability, offering 99.9% SLAs for dedicated endpoints.


# Playground
Source: https://docs.together.ai/docs/inference-web-interface

Guide to using Together AI's web playground for interactive AI model inference across chat, image, video, audio, and transcribe models.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=32e0ec9eaa26cddc360564de6445c3c7" alt="" data-og-width="2916" width="2916" data-og-height="2276" height="2276" data-path="images/guides/47.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f4e2e510c437e43081112e8400bb440e 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=84f808f3a40a73d4a9d5eef2d7206876 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=608c4badaaf5a622288b3dd3eb5ff0e6 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=96d66ef9d9fabb9b55517f9b2ec49b4a 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d115ed41a431ba5d035115547c0b880e 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/47.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c7e7e2ae253943d76faf71edaa0ce5b4 2500w" />
</Frame>

There are five playgrounds for interacting with different types of models:

1. **Chat Playground**
   Chat with models like DeepSeek R1-0528 in a conversational interface. Adjust model behavior with system prompts.

2. **Image Playground**
   Create stunning images from text or from existing images using FLUX.1 \[schnell] or other image generations models. This playground can also be useful for using instruction-tuned models and providing few-shot prompts.

3. **Video Playground**
   Produce engaging videos with Kling 1.6 Standard and other advanced models from text prompts.

4. **Audio Playground**
   Generate lifelike audio for synthesis or editing from text using models like Cartesia Sonic 2.

5. **Transcribe Playground**
   Turn audio into text with Whisper large-v3 or other transcription models.

## Instructions

1. Log in to [api.together.xyz](https://api.together.xyz/playground) with your username and password
2. Navigate through the different playgrounds we offer using the left sidebar
3. Select a model (either one that we offer, or one you have fine-tuned yourself)
4. Adjust the modifications and parameters (more details below)

### Modifications

From the right side panel you can access **modifications** to control the stop sequence or system prompt. The stop sequence controls when the model will stop outputting more text. The system prompt instructs the model how to behave. There are several default system prompts provided and you can add your own. To edit a system prompt you added, hover over the prompt in the menu and click the pencil icon.

### Parameters

Edit inference parameter settings from the right side panel. For more information on how to set these settings see [inference parameters](/docs/inference-parameters).


# Instant Clusters
Source: https://docs.together.ai/docs/instant-clusters

Create, scale, and manage Instant Clusters in Together Cloud

## Overview

Instant Clusters allows you to create high-performance GPU clusters in minutes. With features like on-demand scaling, long-lived resizable high-bandwidth shared DC-local storage, Kubernetes and Slurm cluster flavors, a REST API, and Terraform support, you can run workloads flexibly without complex infrastructure management.

## Quickstart: Create an Instant Cluster

1. Log into api.together.ai.
2. Click **GPU Clusters** in the top navigation menu.
3. Click **Create Cluster**.
4. Choose whether you want **Reserved** capacity or **On-demand**, based on your needs.
5. Select the **cluster size**, for example `8xH100`.
6. Enter a **cluster name**.
7. Choose a **cluster type** either Kubernetes or Slurm.
8. Select a **region**.
9. Choose the reservation **duration** for your cluster.
10. Create and name your **shared volume** (minimum size 1 TiB).
11. Optional: Select your **NVIDIA driver** and **CUDA** versions.
12. Click **Proceed**.

Your cluster will now be ready for you to use.

### Capacity Types

* **Reserved**: You pay upfront to reserve GPU capacity for a duration between 1-90 days.
* **On-demand**: You  pay as you go for GPU capacity on an hourly basis. No pre-payment or reservation needed, and you can terminate your cluster at any time.

### Node Types

We have the following node types available in Instant Clusters.

* NVIDIA HGX B200
* NVIDIA HGX H200
* NVIDIA HGX H100 SXM
* NVIDIA HGX H100 SXM - Inference (lower Infiniband multi-node GPU-to-GPU bandwidth, suitable for single-node inference)

If you don't see an available node type, select the "Notify Me" option to get notified when capacity is online. You can also contact us with your request via [support@together.ai](mailto:support@together.ai).

### Pricing

Pricing information for different GPU node types can be found [here](https://www.together.ai/instant-gpu-clusters).

### Cluster Status

* From the UI, verify that your cluster transitions to Ready.
* Monitor progress and health indicators directly from the cluster list.

### Start Training with Kubernetes

#### Install kubectl

Install `kubectl` in your environment, for example on [MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/).

#### Download kubeconfig

From the Instant Clusters UI, download the kubeconfig and copy it to your local machine:

```bash  theme={null}
~/.kube/together_instant.kubeconfig
export KUBECONFIG=$HOME/.kube/together_instant.kubeconfig
kubectl get nodes
```

> You can rename the file to `config`, but back up your existing config first.

#### Verify Connectivity

```bash  theme={null}
kubectl get nodes
```

You should see all worker and control plane nodes listed.

#### Deploy a Pod with Storage

* Create a PersistentVolumeClaim for shared storage.

```yaml  theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-pvc
spec:
  accessModes:
    - ReadWriteMany   # Multiple pods can read/write
  resources:
    requests:
      storage: 10Gi   # Requested size
  storageClassName: shared-storage-class
```

* Create a PersistentVolumeClaim for local storage.

```yaml  theme={null}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  accessModes:
    - ReadWriteOnce   # Only one pod/node can mount at a time
  resources:
    requests:
      storage: 50Gi
  storageClassName: local-storage-class
```

* Mount them into a pod:

```yaml  theme={null}
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  restartPolicy: Never
  containers:
    - name: ubuntu
      image: debian:stable-slim
      command: ["/bin/sh", "-c", "sleep infinity"]
      volumeMounts:
        - name: shared-pvc
          mountPath: /mnt/shared
        - name: local-pvc
          mountPath: /mnt/local
  volumes:
    - name: shared-pvc
      persistentVolumeClaim:
        claimName: shared-pvc
    - name: local-pvc
      persistentVolumeClaim:
        claimName: local-pvc
```

Apply and connect:

```bash  theme={null}
kubectl apply -f manifest.yaml
kubectl exec -it test-pod -- bash
```

#### Kubernetes Dashboard Access

* From the cluster UI, click the K8s Dashboard URL.
* Retrieve your access token using the following command:

```bash  theme={null}
kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user-token | awk '{print $1}') -o jsonpath='{.data.token}' | base64 -d | pbcopy
```

## Cluster Scaling

Clusters can scale flexibly in real time. By adding on-demand compute to your cluster, you can temporarily scale up to more GPUs when workload demand spikes and then scale back down as it wanes.

Scaling up or down can be performed using the UI, tcloud CLI, or REST API.

### Targeted Scale-down

If you wish to mark which node or nodes should be targeted for scale-down, you can:

* Either cordon the k8s node(s) or add the node.together.ai/delete-node-on-scale-down: "true" annotation to the k8s node(s).
  \= Then trigger scale-down via the cloud console UI (or CLI, REST API).
* Instant Clusters will ensure that cordoned + annotated nodes are prioritized for deletion above all others.

## Storage Management

Instant Clusters supports long-lived, resizable in-DC shared storage.

You can dynamically create and attach volumes to your cluster at cluster creation time, and resize as your data grows.

All shared storage is backed by multi-NIC bare metal paths, ensuring high-throughput and low-latency performance for shared storage.

### Upload Your Data

To upload data to the cluster from your local machine, follow these steps:

* Create a PVC using the `shared-rdma` storage class as well as a pod to mount the volume
* Run `kubectl cp LOCAL_FILENAME YOUR_POD_NAME:/data/`
* Note: This method is suitable for smaller datasets, for larger datasets we recommend scheduling a pod on the cluster that can download from S3.

## Compute Access

You can run workloads on Instant Clusters using Kubernetes or Slurm-on-Kubernetes.

### Kubernetes

Use `kubectl` to submit jobs, manage pods, and interact with your cluster. See [Quickstart](#quickstart) for setup details.

### Slurm Direct SSH

For HPC workflows, you can enable Slurm-on-Kubernetes:

* Directly SSH into a Slurm node.
* Use familiar Slurm commands (`sbatch`, `srun`, etc.) to manage distributed training jobs.

This provides the flexibility of traditional HPC job scheduling alongside Kubernetes.

#### SSH to Slurm Login Pod

Please note that at this time, you must add your SSH key to your account prior to deploying a cluster in order for the key to register
in your LDAP server.

Tip: When you click your cluster in the Together Cloud UI, the Cluster details page shows copy-ready Slurm commands tailored to your cluster (for example, `squeue`, `sinfo`, `srun`, `sbatch`). Use these to quickly verify connectivity and submit jobs.

The hostname of worker pods will always be the name of the node with `.slurm.pod` at the end. For instance, `gpu-dp-hmqnh-nwlnj.slurm.pod`.

The hostname of the login pod, which is the place you will likely wish to start most jobs and routines from is always `slurm-login`.

## APIs and Integrations

### tcloud CLI

Download the CLI:

* [Mac](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-darwin-universal.tar.gz)
* [Linux](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-linux-amd64.tar.gz)

Authenticate via Google SSO:

```bash  theme={null}
tcloud sso login
```

Create a cluster:

```bash  theme={null}
tcloud cluster create my-cluster \ 
  --num-gpus 8 \
  --reservation-duration 1 \  
  --instance-type H100-SXM \ 
  --region us-central-8 \  
  --shared-volume-name my-volume \   
  --size-tib 1
```

Optionally, you can specify whether you want to provision reserved capacity or on-demand by using the `billing-type` field and setting its value to either `prepaid` (i.e. a reservation) or `on_demand`.

```bash  theme={null}
tcloud cluster create my-cluster \
  --num-gpus 8 \
  --billing-type prepaid \
  --reservation-duration 1 \
  --instance-type H100-SXM \
  --region us-central-8 \
  --shared-volume-name my-volume \
  --size-tib 1
```

Delete a cluster:

```bash  theme={null}
tcloud cluster delete <CLUSTER_UUID>
```

### REST API

All cluster management actions (create, scale, delete, storage, etc.) are available via REST API endpoints for programmatic control.

The API documentation can be found [here](https://docs.together.ai/api-reference/gpuclusterservice/create-gpu-cluster).

### Terraform Provider

Use the Together Terraform Provider to define clusters, storage, and scaling policies as code. This allows reproducible infrastructure management integrated with existing Terraform workflows.

### SkyPilot

You can orchestrate AI workloads on Instant Clusters using SkyPilot.

The following example shows how to use Together with SkyPilot and orchestrate `gpt-oss-20b` finetuning on it.

#### Use Together Instant Cluster with SkyPilot

1. ```bash  theme={null}
    uv pip install skypilot[kubernetes]
   ```

2. Launch a Together Instant Cluster with cluster type selected as Kubernetes

* Get the Kubernetes config for the cluster
* Save the kubeconfig to a file say `./together.kubeconfig`
* Copy the kubeconfig to your `~/.kube/config` or merge the Kubernetes config with your existing kubeconfig file.
  ```bash  theme={null}
  mkdir -p ~/.kube
  cp together-kubeconfig ~/.kube/config
  ```
  or
  ```bash  theme={null}
  KUBECONFIG=./together-kubeconfig:~/.kube/config kubectl config view --flatten > /tmp/merged_kubeconfig && mv /tmp/merged_kubeconfig ~/.kube/config    
  ```
  SkyPilot automatically picks up your credentials to the Together Instant Cluster.

3. Check that SkyPilot can access the Together Instant Cluster
   ```console  theme={null}
   $ sky check k8s
   Checking credentials to enable infra for SkyPilot.
     Kubernetes: enabled [compute]
       Allowed contexts:
       └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6: enabled.

   🎉 Enabled infra 🎉
     Kubernetes [compute]
       Allowed contexts:
       └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6

   To enable a cloud, follow the hints above and rerun: sky check
   If any problems remain, refer to detailed docs at: https://docs.skypilot.co/en/latest/getting-started/installation.html
   ```
   Your Together cluster is now accessible with SkyPilot.

4. Check the available GPUs on the cluster:
   ```console  theme={null}
   $ sky show-gpus --infra k8s
   Kubernetes GPUs
   Context: t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6
   GPU   REQUESTABLE_QTY_PER_NODE  UTILIZATION  
   H100  1, 2, 4, 8                8 of 8 free  
   Kubernetes per-node GPU availability
   CONTEXT                                                                              NODE                GPU   UTILIZATION  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-8ct86            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-fjqbt            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  cp-hst5f            -     0 of 0 free  
   t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin@t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6  gpu-dp-gsd6b-k4m4x  H100  8 of 8 free  
   ```

#### Example: Finetuning gpt-oss-20b on the Together Instant Cluster

Launch a gpt-oss finetuning job on the Together cluster is now as simple as a single command:

```bash  theme={null}
sky launch -c gpt-together gpt-oss-20b.yaml
```

You can download the yaml file [here](https://github.com/skypilot-org/skypilot/tree/master/llm/gpt-oss-finetuning#lora-finetuning).

## Billing

#### Compute Billing

Instant Clusters offer two compute billing options: **reserved** and **on-demand**.

* **Reservations** – Credits are charged upfront or deducted for the full
  reserved duration once the cluster is provisioned. Any usage beyond the reserved
  capacity is billed at on-demand rates.
* **On-Demand** – Pay only for the time your cluster is running, with no upfront
  commitment.

See our [pricing page](https://www.together.ai/instant-gpu-clusters) for current rates.

#### Storage Billing

Storage is billed on a **pay-as-you-go** basis, as detailed on our [pricing
page](https://www.together.ai/instant-gpu-clusters). You can freely increase or
decrease your storage volume size, with all usage billed at the same rate.

#### Viewing Usage and Invoices

You can view your current usage anytime on the [Billing page in
Settings](https://api.together.ai/settings/billing). Each invoice includes a
detailed breakdown of reservation, burst, and on-demand usage for compute and
storage

#### Cluster and Storage Lifecycles

Clusters and storage volumes follow different lifecycle policies:

* **Compute Clusters** – Clusters are automatically decommissioned when their
  reservation period ends. To extend a reservation, please contact your account
  team.
* **Storage Volumes** – Storage volumes are persistent and remain available as
  long as your billing account is in good standing. They are not automatically
  deleted.

#### Running Out of Credits

When your credits are exhausted, resources behave differently depending on their
type:

* **Reserved Compute** – Existing reservations remain active until their
  scheduled end date. Any additional on-demand capacity used to scale beyond the
  reservation is decommissioned.
* **Fully On-Demand Compute** – Clusters are first paused and then
  decommissioned if credits are not restored.
* **Storage Volumes** – Access is revoked first, and the data is later
  decommissioned.

You will receive alerts before these actions take place. For questions or
assistance, please contact your billing team.


# Integrations
Source: https://docs.together.ai/docs/integrations

Use Together AI models through partner integrations.

Together AI seamlessly integrates with a wide range of tools and frameworks, making it easy to incorporate powerful open-source models into your existing workflows. Whether you're building AI agents, developing applications, managing vector databases, or monitoring LLM performance, our integrations help you get started quickly.

Our integrations span several categories:

* **Agent Frameworks**: Build sophisticated AI agents with LangGraph, CrewAI, PydanticAI, AutoGen, DSPy, and more
* **Development Tools**: Integrate with popular SDKs like Vercel AI SDK, LangChain, and LlamaIndex
* **Data & Vector Stores**: Connect to Pinecone, MongoDB, and Pixeltable for RAG applications
* **Observability**: Monitor and track your LLM usage with Helicone and Composio

## HuggingFace

*You can use Together AI models with Hugging Face Inference.*

Install the `huggingface_hub` library:

<CodeGroup>
  ```sh Shell theme={null}
  pip install huggingface_hub>=0.29.0
  ```

  ```sh Shell theme={null}
  npm install @huggingface/inference
  ```
</CodeGroup>

Chat Completion with Hugging Face Hub library

<CodeGroup>
  ```python Python theme={null}
  from huggingface_hub import InferenceClient

  ## Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key (HF or custom)
  )

  ## Define the chat messages

  messages = [{"role": "user", "content": "What is the capital of France?"}]

  ## Generate a chat completion

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=messages,
      max_tokens=500,
  )

  ## Print the response

  print(completion.choices[0].message)
  ```

  ```typescript TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const chatCompletion = await client.chatCompletion({
      model: "deepseek-ai/DeepSeek-R1",  // Replace with your desired model
      messages: [
          {
              role: "user",
              content: "What is the capital of France?"
          }
      ],
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });

  // Log the response
  console.log(chatCompletion.choices[0].message);
  ```
</CodeGroup>

Learn more in our [Together AI - HuggingFace Guide](https://docs.together.ai/docs/quickstart-using-hugging-face-inference).

## Vercel AI SDK

*The Vercel AI SDK is a powerful Typescript library designed to help developers build AI-powered applications.*

Install both the Vercel AI SDK and Together.ai's Vercel package.

```shell Shell theme={null}
npm i ai @ai-sdk/togetherai
```

Import the Together.ai provider and call the generateText function with Kimi K2 to generate some text.

```typescript TypeScript theme={null}
import { togetherai } from "@ai-sdk/togetherai";
import { generateText } from "ai";

async function main() {
  const { text } = await generateText({
    model: togetherai("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Write a vegetarian lasagna recipe for 4 people.",
  });

  console.log(text);
}

main();
```

Learn more in our [Together AI - Vercel AI SDK Guide](https://docs.together.ai/docs/using-together-with-vercels-ai-sdk).

## Langchain

*LangChain is a framework for developing context-aware, reasoning applications powered by language models.*

To install the LangChain x Together library, run:

```text Shell theme={null}
pip install --upgrade langchain-together
```

Here's sample code to get you started with Langchain + Together AI:

```python Python theme={null}
from langchain_together import ChatTogether

chat = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf")

for m in chat.stream("Tell me fun things to do in NYC"):
    print(m.content, end="", flush=True)
```

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-langchain?_gl=1*exkmyi*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and LangChain.

* [LangChain TogetherEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/together)
* [LangChain Together](https://python.langchain.com/docs/integrations/llms/together)

## LlamaIndex

*LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models (LLMs).*

Install `llama-index`

```shell Shell theme={null}
pip install llama-index
```

Here's sample code to get you started with Llama Index + Together AI:

```python Python theme={null}
from llama_index.llms import OpenAILike

llm = OpenAILike(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    api_base="https://api.together.xyz/v1",
    api_key="TOGETHER_API_KEY",
    is_chat_model=True,
    is_function_calling_model=True,
    temperature=0.1,
)

response = llm.complete(
    "Write up to 500 words essay explaining Large Language Models"
)

print(response)
```

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-llamaindex?_gl=1*1t16mh2*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and LlamaIndex.

* [LlamaIndex TogetherEmbeddings](https://docs.llamaindex.ai/en/stable/examples/embeddings/together.html)
* [LlamaIndex TogetherLLM](https://docs.llamaindex.ai/en/stable/examples/llm/together.html)

## CrewAI

*CrewAI is an open source framework for orchestrating AI agent systems.*

Install `crewai`

```shell Shell theme={null}
pip install crewai
export TOGETHER_API_KEY=***
```

Build a multi-agent workflow:

```python Python theme={null}
import os
from crewai import LLM, Task, Agent, Crew

llm = LLM(
    model="together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo",
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1",
)

research_agent = Agent(
    llm=llm,
    role="Research Analyst",
    goal="Find and summarize information about specific topics",
    backstory="You are an experienced researcher with attention to detail",
    verbose=True,  # Enable logging for debugging
)

research_task = Task(
    description="Conduct a thorough research about AI Agents.",
    expected_output="A list with 10 bullet points of the most relevant information about AI Agents",
    agent=research_agent,
)

## Execute the crew
crew = Crew(agents=[research_agent], tasks=[research_task], verbose=True)

result = crew.kickoff()

## Accessing the task output
task_output = research_task.output

print(task_output)
```

Learn more in our [CrewAI guide](https://docs.together.ai/docs/crewai).

## LangGraph

*LangGraph is an OSS library for building stateful, multi-actor applications with LLMs*

Install `langgraph`

```shell Shell theme={null}
pip install -U langgraph langchain-together
export TOGETHER_API_KEY=***
```

Build a tool-using agent:

```python Python theme={null}
import os
from langchain_together import ChatTogether

llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    api_key=os.getenv("TOGETHER_API_KEY"),
)


## Define a tool
def multiply(a: int, b: int) -> int:
    return a * b


## Augment the LLM with tools
llm_with_tools = llm.bind_tools([multiply])

## Invoke the LLM with input that triggers the tool call
msg = llm_with_tools.invoke("What is 2 times 3?")

## Get the tool call
msg.tool_calls
```

Learn more in our [LangGraph Guide](https://docs.together.ai/docs/langgraph) including:

* [Agentic RAG Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/Agentic_RAG_LangGraph.ipynb)
* [Planning Agent Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/LangGraph/LangGraph_Planning_Agent.ipynb)

## PydanticAI

*PydanticAI is an agent framework created by the Pydantic team to simplify building agent workflows.*

Install `pydantic-ai`

```shell Shell theme={null}
pip install pydantic-ai
export TOGETHER_API_KEY=***
```

Build PydanticAI agents using Together AI models

```python Python theme={null}
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

## Connect PydanticAI to LLMs on Together
model = OpenAIModel(
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    provider=OpenAIProvider(
        base_url="https://api.together.xyz/v1",
        api_key=os.environ.get("TOGETHER_API_KEY"),
    ),
)

## Setup the agent
agent = Agent(
    model,
    system_prompt="Be concise, reply with one sentence.",
)

result = agent.run_sync('Where does "hello world" come from?')
print(result.data)
```

Learn more in our [PydanticAI Guide](https://docs.together.ai/docs/pydanticai) and explore our [PydanticAI Agents notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/PydanticAI/PydanticAI_Agents.ipynb).

## Arcade.dev

*Arcade is a platform that lets AI securely use tools like email, files, and APIs to take real action—not just chat. Build powerful assistants in minutes with ready-to-use integrations or a custom SDK.*

Our guide demonstrates how to integrate Together AI's language models with Arcade's tools to create an AI agent that can send emails.

Prerequisites:

* Together AI API key - see here [https://api.together.ai/](https://api.together.ai/)
* Arcade API key - see here [https://arcade.dev/](https://arcade.dev/)
* Gmail account to connect via OAuth

```shell Shell theme={null}
## install the required packages
!pip install -qU together arcadepy
```

Gmail Configuration:

<CodeGroup>
  ```shell Shell theme={null}
  import os
  from arcadepy import Arcade
  from together import Together

  ## Set environment variables
  os.environ["TOGETHER_API_KEY"] = "XXXXXXXXXXXXX"  # Replace with your actual Together API key
  os.environ["ARCADE_API_KEY"] = "arc_XXXXXXXXXXX"    # Replace with your actual Arcade API key

  ## Initialize clients
  together_client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
  arcade_client = Arcade()  # Automatically finds the ARCADE_API_KEY env variable

  ## Set up user ID (your email)
  USER_ID = "your_email@example.com"  # Change this to your email

  ## Authorize Gmail access
  auth_response = arcade_client.tools.authorize(
      tool_name="Google.SendEmail",
      user_id=USER_ID,
  )

  if auth_response.status != "completed":
      print(f"Click this link to authorize: {auth_response.url}")
      # Wait for the authorization to complete
      arcade_client.auth.wait_for_completion(auth_response)

  print("Authorization completed!")
  ```
</CodeGroup>

Learn more in our [Arcade guide](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Arcade.dev/Agents_Arcade.ipynb) notebook.

## DSPy

*DSPy is a framework that enables you to build modular AI systems with code instead of hand-crafted prompting*

Install `dspy`

```shell Shell theme={null}
pip install -U dspy
export TOGETHER_API_KEY=***
```

Build a question answering agent

```python Python theme={null}
import dspy

# Configure dspy with a LLM from Together AI
lm = dspy.LM(
    "together_ai/togethercomputer/llama-2-70b-chat",
    api_key=os.environ.get("TOGETHER_API_KEY"),
    api_base="https://api.together.xyz/v1",
)

# Configure dspy to use the LLM
dspy.configure(lm=lm)


## Gives the agent access to a python interpreter
def evaluate_math(expression: str):
    return dspy.PythonInterpreter({}).execute(expression)


## Gives the agent access to a wikipedia search tool
def search_wikipedia(query: str):

    results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(
        query, k=3
    )
    return [x["text"] for x in results]


## setup ReAct module with question and math answer signature
react = dspy.ReAct(
    "question -> answer: float",
    tools=[evaluate_math, search_wikipedia],
)

pred = react(
    question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?"
)

print(pred.answer)
```

Learn more in our [DSPy Guide](https://docs.together.ai/docs/dspy) and explore our [DSPy Agents notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/DSPy/DSPy_Agents.ipynb).

## AutoGen(AG2)

*AG2 (formerly AutoGen) is an open-source framework for building and orchestrating AI agents.*

Install `autogen`

```shell Shell theme={null}
pip install autogen
export TOGETHER_API_KEY=***
```

Build a coding agent

```python Python theme={null}
import os
from pathlib import Path
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor

config_list = [
    {
        # Let's choose the Mixtral 8x7B model
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        # Provide your Together.AI API key here or put it into the TOGETHER_API_KEY environment variable.
        "api_key": os.environ.get("TOGETHER_API_KEY"),
        # We specify the API Type as 'together' so it uses the Together.AI client class
        "api_type": "together",
        "stream": False,
    }
]

## Setting up the code executor
workdir = Path("coding")
workdir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=workdir)

## Setting up the agents

## The UserProxyAgent will execute the code that the AssistantAgent provides
user_proxy_agent = UserProxyAgent(
    name="User",
    code_execution_config={"executor": code_executor},
    is_termination_msg=lambda msg: "FINISH" in msg.get("content"),
)

system_message = """You are a helpful AI assistant who writes code and the user executes it.
Solve tasks using your coding and language skills.
"""

## The AssistantAgent, using Together.AI's Code Llama model, will take the coding request and return code
assistant_agent = AssistantAgent(
    name="Together Assistant",
    system_message=system_message,
    llm_config={"config_list": config_list},
)

## Start the chat, with the UserProxyAgent asking the AssistantAgent the message
chat_result = user_proxy_agent.initiate_chat(
    assistant_agent,
    message="Provide code to count the number of prime numbers from 1 to 10000.",
)
```

Learn more in our [Autogen Guide](https://docs.together.ai/docs/autogen).

## Agno

*Agno is an open-source library for creating multimodal agents.*

Install `agno`

```shell Shell theme={null}
pip install -U agno duckduckgo-search
```

Build a search and answer agent

```python Python theme={null}
from agno.agent import Agent
from agno.models.together import Together
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)
agent.print_response("What's happening in New York?", stream=True)
```

Learn more in our [Agno Guide](https://docs.together.ai/docs/agno) including code a notebook.

## MongoDB

See [this tutorial blog](https://www.together.ai/blog/rag-tutorial-mongodb?_gl=1*13iu8zj*_gcl_au*MTA3NDk3OTU0MS4xNzM3OTk4MjUw*_ga*MTg5NTkzNDM0LjE3MjgzMzM2MDQ.*_ga_BS43X21GZ2*MTc0NTQ1ODY4OC44MC4xLjE3NDU0NjY2ODYuMC4wLjA.*_ga_BBHKJ5V8S0*MTc0NTQ1ODY4OC42OS4xLjE3NDU0NjY2ODYuMC4wLjA.) for the RAG implementation details using Together and MongoDB.

## Pinecone

*Pinecone is a vector database that helps companies build RAG applications.*

Here's some sample code to get you started with Pinecone + Together AI:

```python Python theme={null}
from pinecone import Pinecone, ServerlessSpec
from together import Together

pc = Pinecone(api_key="PINECONE_API_KEY", source_tag="TOGETHER_AI")
client = Together()

## Create an index in pinecone
index = pc.create_index(
    name="serverless-index",
    dimension=1536,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-west-2"),
)

## Create an embedding on Together AI
textToEmbed = (
    "Our solar system orbits the Milky Way galaxy at about 515,000 mph"
)
embeddings = client.embeddings.create(
    model="togethercomputer/m2-bert-80M-8k-retrieval", input=textToEmbed
)

## Use index.upsert() to insert embeddings and index.query() to query for similar vectors
```

## Helicone

*Helicone is an open source LLM observability platform.*

Here's some sample code to get started with using Helicone + Together AI:

```python Python theme={null}
import os
from together import Together

client = Together(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://together.hconeai.com/v1",
    supplied_headers={
        "Helicone-Auth": f"Bearer {os.environ.get('HELICONE_API_KEY')}",
    },
)

stream = client.chat.completions.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {
            "role": "user",
            "content": "What are some fun things to do in New York?",
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

## Composio

*Composio allows developers to integrate external tools and services into their AI applications.*

Install `composio-togetherai`

```shell Shell theme={null}
pip install together composio-togetherai
export TOGETHER_API_KEY=***
export COMPOSIO_API_KEY=***
```

Get Together AI models to use integrated tools

```python Python theme={null}
from composio_togetherai import ComposioToolSet, App
from together import Together

client = Together()
toolset = ComposioToolSet()

request = toolset.initiate_connection(app=App.GITHUB)
print(f"Open this URL to authenticate: {request.redirectUrl}")

tools = toolset.get_tools(apps=[App.GITHUB])

response = client.chat.completions.create(
    tools=tools,
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": "Star the repo 'togethercomputer/together-cookbook'",
        }
    ],
)

res = toolset.handle_tool_calls(response)
print(res)
```

Learn more in our [Composio Guide](https://docs.together.ai/docs/composio) and explore our [Composio cookbook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Composio/Agents_Composio.ipynb).

## Pixeltable

See [this tutorial blog](https://docs.together.ai/docs/embeddings-rag#:~:text=Using%20Pixeltable,Together%20and%20Pixeltable.) for the RAG implementation details using Together and Pixeltable.


# Agent Integrations
Source: https://docs.together.ai/docs/integrations-2

Using OSS agent frameworks with Together AI

You can use Together AI with many of the most popular AI agent frameworks. Choose your preferred framework to learn how to enhance your agents with the best open source models.

## [LangGraph](/docs/langgraph)

LangGraph is a library for building stateful, multi-actor applications with LLMs. It provides a flexible framework for creating complex, multi-step reasoning applications through acyclic and cyclic graphs.

## [CrewAI](/docs/crewai)

CrewAI is an open source framework for orchestrating AI agent systems. It enables multiple AI agents to collaborate effectively by assuming roles and working toward shared goals.

## [PydanticAI](/docs/pydanticai)

PydanticAI provides structured data extraction and validation for LLMs using Pydantic schemas. It ensures your AI outputs adhere to specified formats, making integration with downstream systems reliable.

## [AutoGen(AG2)](/docs/autogen)

AutoGen(AG2) is an OSS agent framework for multi-agent conversations and workflow automation. It enables the creation of customizable agents that can interact with each other and with human users to solve complex tasks.

## [DSPy](/docs/dspy)

DSPy is a programming framework for algorithmic AI systems. It offers a compiler-like approach to prompt engineering, allowing you to create modular, reusable, and optimizable language model programs.

## [Composio](/docs/composio)

Composio provides a platform for building and deploying AI applications with reusable components. It simplifies the process of creating complex AI systems by connecting specialized modules.



---

**Navigation:** [← Previous](./04-fine-tuning-guide.md) | [Index](./index.md) | [Next →](./06-iterative-workflow.md)
