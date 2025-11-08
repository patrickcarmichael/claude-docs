**Navigation:** [← Previous](./05-find-create-an-api-key-at-httpselevenlabsioappsett.md) | [Index](./index.md) | [Next →](./07-migrate-from-playht-to-elevenlabs.md)

# Cross-platform Voice Agents with Expo React Native

> Build ElevenLabs agents that work across iOS and Android using Expo and the ElevenLabs React Native SDK with WebRTC support.


## Introduction

In this tutorial you will learn how to build a voice agent that works across iOS and Android using [Expo React Native](https://expo.dev/) and the ElevenLabs [React Native SDK](/docs/agents-platform/libraries/react-native) with WebRTC support.

{/* TODO: Add YT video once ready! */}

<Tip title="Prefer to jump straight to the code?" icon="lightbulb">
  Find the [example project on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/react-native/elevenlabs-conversational-ai-expo-react-native).
</Tip>


## Requirements

* An ElevenLabs account with an [API key](https://elevenlabs.io/app/settings/api-keys).
* Node.js v18 or higher installed on your machine.


## Setup

### Create a new Expo project

Using `create-expo-app`, create a new blank Expo project:

```bash
npx create-expo-app@latest --template blank-typescript
```

### Install dependencies

Install the ElevenLabs React Native SDK and its dependencies:

```bash
npx expo install @elevenlabs/react-native @livekit/react-native @livekit/react-native-webrtc @config-plugins/react-native-webrtc @livekit/react-native-expo-plugin @livekit/react-native-expo-plugin livekit-client
```

<Note>
  If you're running into an issue with peer dependencies, please add a `.npmrc` file in the root of
  the project with the following content: `legacy-peer-deps=true`.
</Note>

### Enable microphone permissions and add Expo plugins

In the `app.json` file, add the following permissions:

```json app.json
{
  "expo": {
    "scheme": "elevenlabs",
    // ...
    "ios": {
      "infoPlist": {
        "NSMicrophoneUsageDescription": "This app uses the microphone to record audio."
      },
      "supportsTablet": true,
      "bundleIdentifier": "YOUR.BUNDLE.ID"
    },
    "android": {
      "permissions": [
        "android.permission.RECORD_AUDIO",
        "android.permission.ACCESS_NETWORK_STATE",
        "android.permission.CAMERA",
        "android.permission.INTERNET",
        "android.permission.MODIFY_AUDIO_SETTINGS",
        "android.permission.SYSTEM_ALERT_WINDOW",
        "android.permission.WAKE_LOCK",
        "android.permission.BLUETOOTH"
      ],
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#ffffff"
      },
      "package": "YOUR.PACKAGE.ID"
    },
    "plugins": ["@livekit/react-native-expo-plugin", "@config-plugins/react-native-webrtc"]
    // ...
  }
}
```

This will allow the React Native to prompt for microphone permissions when the conversation is started.

<Tip title="Note" icon="warning">
  For Android emulator you will need to enable "Virtual microphone uses host audio input" in the
  emulator microphone settings.
</Tip>


## Add ElevenLabs Agents to your app

Add the ElevenLabs Agents to your app by adding the following code to your `./App.tsx` file:

```tsx ./App.tsx
import { ElevenLabsProvider, useConversation } from '@elevenlabs/react-native';
import type { ConversationStatus, ConversationEvent, Role } from '@elevenlabs/react-native';
import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Keyboard,
  TouchableWithoutFeedback,
  Platform,
} from 'react-native';
import { TextInput } from 'react-native';

import { getBatteryLevel, changeBrightness, flashScreen } from './utils/tools';

const ConversationScreen = () => {
  const conversation = useConversation({
    clientTools: {
      getBatteryLevel,
      changeBrightness,
      flashScreen,
    },
    onConnect: ({ conversationId }: { conversationId: string }) => {
      console.log('✅ Connected to conversation', conversationId);
    },
    onDisconnect: (details: string) => {
      console.log('❌ Disconnected from conversation', details);
    },
    onError: (message: string, context?: Record<string, unknown>) => {
      console.error('❌ Conversation error:', message, context);
    },
    onMessage: ({ message, source }: { message: ConversationEvent; source: Role }) => {
      console.log(`💬 Message from ${source}:`, message);
    },
    onModeChange: ({ mode }: { mode: 'speaking' | 'listening' }) => {
      console.log(`🔊 Mode: ${mode}`);
    },
    onStatusChange: ({ status }: { status: ConversationStatus }) => {
      console.log(`📡 Status: ${status}`);
    },
    onCanSendFeedbackChange: ({ canSendFeedback }: { canSendFeedback: boolean }) => {
      console.log(`🔊 Can send feedback: ${canSendFeedback}`);
    },
  });

  const [isStarting, setIsStarting] = useState(false);
  const [textInput, setTextInput] = useState('');

  const handleSubmitText = () => {
    if (textInput.trim()) {
      conversation.sendUserMessage(textInput.trim());
      setTextInput('');
      Keyboard.dismiss();
    }
  };

  const startConversation = async () => {
    if (isStarting) return;

    setIsStarting(true);
    try {
      await conversation.startSession({
        agentId: process.env.EXPO_PUBLIC_AGENT_ID,
        dynamicVariables: {
          platform: Platform.OS,
        },
      });
    } catch (error) {
      console.error('Failed to start conversation:', error);
    } finally {
      setIsStarting(false);
    }
  };

  const endConversation = async () => {
    try {
      await conversation.endSession();
    } catch (error) {
      console.error('Failed to end conversation:', error);
    }
  };

  const getStatusColor = (status: ConversationStatus): string => {
    switch (status) {
      case 'connected':
        return '#10B981';
      case 'connecting':
        return '#F59E0B';
      case 'disconnected':
        return '#EF4444';
      default:
        return '#6B7280';
    }
  };

  const getStatusText = (status: ConversationStatus): string => {
    return status[0].toUpperCase() + status.slice(1);
  };

  const canStart = conversation.status === 'disconnected' && !isStarting;
  const canEnd = conversation.status === 'connected';

  return (
    <TouchableWithoutFeedback onPress={() => Keyboard.dismiss()}>
      <View style={styles.container}>
        <Text style={styles.title}>ElevenLabs React Native Example</Text>
        <Text style={styles.subtitle}>Remember to set the agentId in the .env file!</Text>

        <View style={styles.statusContainer}>
          <View
            style={[styles.statusDot, { backgroundColor: getStatusColor(conversation.status) }]}
          />
          <Text style={styles.statusText}>{getStatusText(conversation.status)}</Text>
        </View>

        {/* Speaking Indicator */}
        {conversation.status === 'connected' && (
          <View style={styles.speakingContainer}>
            <View
              style={[
                styles.speakingDot,
                {
                  backgroundColor: conversation.isSpeaking ? '#8B5CF6' : '#D1D5DB',
                },
              ]}
            />
            <Text
              style={[
                styles.speakingText,
                { color: conversation.isSpeaking ? '#8B5CF6' : '#9CA3AF' },
              ]}
            >
              {conversation.isSpeaking ? '🎤 AI Speaking' : '👂 AI Listening'}
            </Text>
          </View>
        )}

        <View style={styles.buttonContainer}>
          <TouchableOpacity
            style={[styles.button, styles.startButton, !canStart && styles.disabledButton]}
            onPress={startConversation}
            disabled={!canStart}
          >
            <Text style={styles.buttonText}>
              {isStarting ? 'Starting...' : 'Start Conversation'}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.button, styles.endButton, !canEnd && styles.disabledButton]}
            onPress={endConversation}
            disabled={!canEnd}
          >
            <Text style={styles.buttonText}>End Conversation</Text>
          </TouchableOpacity>
        </View>

        {/* Feedback Buttons */}
        {conversation.status === 'connected' && conversation.canSendFeedback && (
          <View style={styles.feedbackContainer}>
            <Text style={styles.feedbackLabel}>How was that response?</Text>
            <View style={styles.feedbackButtons}>
              <TouchableOpacity
                style={[styles.button, styles.likeButton]}
                onPress={() => conversation.sendFeedback(true)}
              >
                <Text style={styles.buttonText}>👍 Like</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.button, styles.dislikeButton]}
                onPress={() => conversation.sendFeedback(false)}
              >
                <Text style={styles.buttonText}>👎 Dislike</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}

        {/* Text Input and Messaging */}
        {conversation.status === 'connected' && (
          <View style={styles.messagingContainer}>
            <Text style={styles.messagingLabel}>Send Text Message</Text>
            <TextInput
              style={styles.textInput}
              value={textInput}
              onChangeText={(text) => {
                setTextInput(text);
                // Prevent agent from interrupting while user is typing
                if (text.length > 0) {
                  conversation.sendUserActivity();
                }
              }}
              placeholder="Type your message or context... (Press Enter to send)"
              multiline
              onSubmitEditing={handleSubmitText}
              returnKeyType="send"
              blurOnSubmit={true}
            />
            <View style={styles.messageButtons}>
              <TouchableOpacity
                style={[styles.button, styles.messageButton]}
                onPress={handleSubmitText}
                disabled={!textInput.trim()}
              >
                <Text style={styles.buttonText}>💬 Send Message</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.button, styles.contextButton]}
                onPress={() => {
                  if (textInput.trim()) {
                    conversation.sendContextualUpdate(textInput.trim());
                    setTextInput('');
                    Keyboard.dismiss();
                  }
                }}
                disabled={!textInput.trim()}
              >
                <Text style={styles.buttonText}>📝 Send Context</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      </View>
    </TouchableWithoutFeedback>
  );
};

export default function App() {
  return (
    <ElevenLabsProvider>
      <ConversationScreen />
    </ElevenLabsProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F3F4F6',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 8,
    color: '#1F2937',
  },
  subtitle: {
    fontSize: 16,
    color: '#6B7280',
    marginBottom: 32,
  },
  statusContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 24,
  },
  statusDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 8,
  },
  statusText: {
    fontSize: 16,
    fontWeight: '500',
    color: '#374151',
  },
  speakingContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 24,
  },
  speakingDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 8,
  },
  speakingText: {
    fontSize: 14,
    fontWeight: '500',
  },
  toolsContainer: {
    backgroundColor: '#E5E7EB',
    padding: 16,
    borderRadius: 8,
    marginBottom: 24,
    width: '100%',
  },
  toolsTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#374151',
    marginBottom: 8,
  },
  toolItem: {
    fontSize: 12,
    color: '#6B7280',
    fontFamily: 'monospace',
    marginBottom: 4,
  },
  buttonContainer: {
    width: '100%',
    gap: 16,
  },
  button: {
    backgroundColor: '#3B82F6',
    paddingVertical: 16,
    paddingHorizontal: 32,
    borderRadius: 8,
    alignItems: 'center',
  },
  startButton: {
    backgroundColor: '#10B981',
  },
  endButton: {
    backgroundColor: '#EF4444',
  },
  disabledButton: {
    backgroundColor: '#9CA3AF',
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
  instructions: {
    marginTop: 24,
    fontSize: 14,
    color: '#6B7280',
    textAlign: 'center',
    lineHeight: 20,
  },
  feedbackContainer: {
    marginTop: 24,
    alignItems: 'center',
  },
  feedbackLabel: {
    fontSize: 16,
    fontWeight: '500',
    color: '#374151',
    marginBottom: 12,
  },
  feedbackButtons: {
    flexDirection: 'row',
    gap: 16,
  },
  likeButton: {
    backgroundColor: '#10B981',
  },
  dislikeButton: {
    backgroundColor: '#EF4444',
  },
  messagingContainer: {
    marginTop: 24,
    width: '100%',
  },
  messagingLabel: {
    fontSize: 16,
    fontWeight: '500',
    color: '#374151',
    marginBottom: 8,
  },
  textInput: {
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
    padding: 16,
    minHeight: 100,
    textAlignVertical: 'top',
    borderWidth: 1,
    borderColor: '#D1D5DB',
    marginBottom: 16,
  },
  messageButtons: {
    flexDirection: 'row',
    gap: 16,
  },
  messageButton: {
    backgroundColor: '#3B82F6',
    flex: 1,
  },
  contextButton: {
    backgroundColor: '#4F46E5',
    flex: 1,
  },
  activityContainer: {
    marginTop: 24,
    alignItems: 'center',
  },
  activityLabel: {
    fontSize: 14,
    color: '#6B7280',
    marginBottom: 8,
    textAlign: 'center',
  },
  activityButton: {
    backgroundColor: '#F59E0B',
  },
});
```

### Native client tools

A big part of building ElevenLabs agents is allowing the agent access and execute functionality dynamically. This can be done via [client tools](/docs/agents-platform/customization/tools/client-tools).

Create a new file to hold your client tools: `./utils/tools.ts` and add the following code:

```ts ./utils/tools.ts
import * as Battery from 'expo-battery';
import * as Brightness from 'expo-brightness';

const getBatteryLevel = async () => {
  const batteryLevel = await Battery.getBatteryLevelAsync();
  console.log('batteryLevel', batteryLevel);
  if (batteryLevel === -1) {
    return 'Error: Device does not support retrieving the battery level.';
  }
  return batteryLevel;
};

const changeBrightness = ({ brightness }: { brightness: number }) => {
  console.log('changeBrightness', brightness);
  Brightness.setSystemBrightnessAsync(brightness);
  return brightness;
};

const flashScreen = () => {
  Brightness.setSystemBrightnessAsync(1);
  setTimeout(() => {
    Brightness.setSystemBrightnessAsync(0);
  }, 200);
  return 'Successfully flashed the screen.';
};

export { getBatteryLevel, changeBrightness, flashScreen };
```

### Dynamic variables

In addition to the client tools, we're also injecting the platform (web, iOS, Android) as a [dynamic variable](https://elevenlabs.io/docs/agents-platform/customization/personalization/dynamic-variables) both into the first message, and the prompt:

```tsx ./App.tsx
// ...
const startConversation = async () => {
  if (isStarting) return;

  setIsStarting(true);
  try {
    await conversation.startSession({
      agentId: process.env.EXPO_PUBLIC_AGENT_ID,
      dynamicVariables: {
        platform: Platform.OS,
      },
    });
  } catch (error) {
    console.error('Failed to start conversation:', error);
  } finally {
    setIsStarting(false);
  }
};
// ...
```


## Agent configuration

<Steps>
  <Step title="Sign in to ElevenLabs">
    Go to [elevenlabs.io](https://elevenlabs.io/sign-up) and sign in to your account.
  </Step>

  <Step title="Create a new agent">
    Navigate to [Agents Platform > Agents](https://elevenlabs.io/app/agents/agents) and
    create a new agent from the blank template.
  </Step>

  <Step title="Set the first message">
    Set the first message and specify the dynamic variable for the platform.

    ```txt
    Hi there, woah, so cool that I'm running on {{platform}}. What can I help you with?
    ```
  </Step>

  <Step title="Set the system prompt">
    Set the system prompt. You can also include dynamic variables here.

    ```txt
    You are a helpful assistant running on {{platform}}. You have access to certain tools that allow you to check the user device battery level and change the display brightness. Use these tools if the user asks about them. Otherwise, just answer the question.
    ```
  </Step>

  <Step title="Set up the client tools">
    Set up the following client tools:

    * Name: `getBatteryLevel`
      * Description: Gets the device battery level as decimal point percentage.
      * Wait for response: `true`
      * Response timeout (seconds): 3
    * Name: `changeBrightness`
      * Description: Changes the brightness of the device screen.
      * Wait for response: `true`
      * Response timeout (seconds): 3
      * Parameters:
        * Data Type: `number`
        * Identifier: `brightness`
        * Required: `true`
        * Value Type: `LLM Prompt`
        * Description: A number between 0 and 1, inclusive, representing the desired screen brightness.
    * Name: `flashScreen`
      * Description: Quickly flashes the screen on and off.
      * Wait for response: `true`
      * Response timeout (seconds): 3
  </Step>
</Steps>


## Run the app

This app requires some native dependencies that aren't supported in Expo Go, therefore you will need to prebuild the app and then run it on a native device.

* Terminal 1:
  * Run `npx expo prebuild --clean`

```bash
npx expo prebuild --clean
```

* Run `npx expo start --tunnel` to start the Expo development server over https.

```bash
npx expo start --tunnel
```

* Terminal 2:
  * Run `npx expo run:ios --device` to run the app on your iOS device.

```bash
npx expo run:ios --device
```



# Data Collection and Analysis with Agents Platform in Next.js

> Collect and analyse data in post-call webhooks using Agents Platform and Next.js.


## Introduction

In this tutorial you will learn how to build a voice agent that collects information from the user through conversation, then analyses and extracts the data in a structured way and sends it to your application via the post-call webhook.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/8b-r1xYdZkw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

<Tip title="Prefer to jump straight to the code?" icon="lightbulb">
  Find the [example project on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/nextjs-post-call-webhook).
</Tip>


## Requirements

* An ElevenLabs account with an [API key](https://elevenlabs.io/app/settings/api-keys).
* Node.js v18 or higher installed on your machine.


## Setup

### Create a new Next.js project

We recommend using our [v0.dev Agents Platform template](https://v0.dev/community/nextjs-5TN93pl3bRS) as the starting point for your application. This template is a production-ready Next.js application with the ElevenLabs agent already integrated.

Alternatively, you can clone the [fully integrated project from GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/nextjs-post-call-webhook), or create a new blank Next.js project and follow the steps below to integrate the ElevenLabs agent.

### Set up Agents Platform

Follow our [Next.js guide](/docs/agents-platform/guides/quickstarts/next-js) for installation and configuration steps. Then come back here to build in the advanced features.


## Agent configuration

<Steps>
  <Step title="Sign in to ElevenLabs">
    Go to [elevenlabs.io](https://elevenlabs.io/sign-up) and sign in to your account.
  </Step>

  <Step title="Create a new agent">
    Navigate to [Agents Platform > Agents](https://elevenlabs.io/app/agents/agents) and
    create a new agent from the blank template.
  </Step>

  <Step title="Set the first message">
    Set the first message and specify the dynamic variable for the platform.

    ```txt
    Hi {{user_name}}, I'm Jess from the ElevenLabs team. I'm here to help you design your very own ElevenLabs agent! To kick things off, let me know what kind of agent you're looking to create. For example, do you want a support agent, to help your users answer questions, or a sales agent to sell your products, or just a friend to chat with?
    ```
  </Step>

  <Step title="Set the system prompt">
    Set the system prompt. You can also include dynamic variables here.

    ```txt
    You are Jess, a helpful agent helping {{user_name}} to design their very own ElevenLabs agent. The design process involves the following steps:

    "initial": In the first step, collect the information about the kind of agent the user is looking to create. Summarize the user's needs back to them and ask if they are ready to continue to the next step. Only once they confirm proceed to the next step.
    "training": Tell the user to create the agent's knowledge base by uploading documents, or submitting URLs to public websites with information that should be available to the agent. Wait patiently without talking to the user. Only when the user confirms that they've provided everything then proceed to the next step.
    "voice": Tell the user to describe the voice they want their agent to have. For example: "A professional, strong spoken female voice with a slight British accent." Repeat the description of their voice back to them and ask if they are ready to continue to the next step. Only once they confirm proceed to the next step.
    "email": Tell the user that we've collected all necessary information to create their ElevenLabs agent and ask them to provide their email address to get notified when the agent is ready.

    Always call the `set_ui_state` tool when moving between steps!
    ```
  </Step>

  <Step title="Set up the client tools">
    Set up the following client tool to navigate between the steps:

    * Name: `set_ui_state`
      * Description: Use this client-side tool to navigate between the different UI states.
      * Wait for response: `true`
      * Response timeout (seconds): 1
      * Parameters:
        * Data type: string
        * Identifier: step
        * Required: true
        * Value Type: LLM Prompt
        * Description: The step to navigate to in the UI. Only use the steps that are defined in the system prompt!
  </Step>

  <Step title="Set your agent's voice">
    Navigate to the `Voice` tab and set the voice for your agent. You can find a list of recommended voices for Agents Platform in the [Conversational Voice Design docs](/docs/agents-platform/best-practices/conversational-voice-design#voices).
  </Step>

  <Step title="Set the evaluation criteria">
    Navigate to the `Analysis` tab and add a new evaluation criteria.

    * Name: `all_data_provided`
      * Prompt: Evaluate whether the user provided a description of the agent they are looking to generate as well as a description of the voice the agent should have.
  </Step>

  <Step title="Configure the data collection">
    You can use the post call analysis to extract data from the conversation. In the `Analysis` tab, under `Data Collection`, add the following items:

    * Identifier: `voice_description`
      * `data-type`: `String`
      * Description: Based on the description of the voice the user wants the agent to have, generate a concise description of the voice including the age, accent, tone, and character if available.
    * Identifier: `agent_description`
      * `data-type`: `String`
      * Description: Based on the description about the agent the user is looking to design, generate a prompt that can be used to train a model to act as the agent.
  </Step>

  <Step title="Configure the post-call webhook">
    [Post-call webhooks](https://elevenlabs.io/docs/agents-platform/workflows/post-call-webhooks) are used to notify you when a call ends and the analysis and data extraction steps have been completed.

    In this example the, the post-call webhook does a couple of steps, namely:

    1. Create a custom voice design based on the `voice_description`.
    2. Create a ElevenLabs agent for the users based on the `agent_description` they provided.
    3. Retrieve the knowledge base documents from the conversation state stored in Redis and attach the knowledge base to the agent.
    4. Send an email to the user to notify them that their custom ElevenLabs agent is ready to chat.

    When running locally, you will need a tool like [ngrok](https://ngrok.com/) to expose your local server to the internet.

    ```bash
    ngrok http 3000
    ```

    Navigate to the [Agents Platform settings](https://elevenlabs.io/app/agents/settings) and under `Post-Call Webhook` create a new webhook and paste in your ngrok URL: `https://<your-url>.ngrok-free.app/api/convai-webhook`.

    After saving the webhook, you will receive a webhooks secret. Make sure to store this secret securely as you will need to set it in your `.env` file later.
  </Step>
</Steps>


## Integrate the advanced features

### Set up a Redis database for storing the conversation state

In this example we're using Redis to store the conversation state. This allows us to retrieve the knowledge base documents from the conversation state after the call ends.

If you're deploying to Vercel, you can configure the [Upstash for Redis](https://vercel.com/marketplace/upstash) integration, or alternatively you can sign up for a free [Upstash account](https://upstash.com/) and create a new database.

### Set up Resend for sending post-call emails

In this example we're using Resend to send the post-call email to the user. To do so you will need to create a free [Resend account](https://resend.com/) and set up a new API key.

### Set the environment variables

In the root of your project, create a `.env` file and add the following variables:

```bash
ELEVENLABS_CONVAI_WEBHOOK_SECRET=
ELEVENLABS_API_KEY=
ELEVENLABS_AGENT_ID=


# Resend
RESEND_API_KEY=
RESEND_FROM_EMAIL=


# Upstash Redis
KV_URL=
KV_REST_API_READ_ONLY_TOKEN=
REDIS_URL=
KV_REST_API_TOKEN=
KV_REST_API_URL=
```

### Configure security and authentication

To secure your ElevenLabs agent, you need to enable authentication in the `Security` tab of the agent configuration.

Once authentication is enabled, you will need to create a signed URL in a secure server-side environment to initiate a conversation with the agent. In Next.js, you can do this by setting up a new API route.

```tsx ./app/api/signed-url/route.ts
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import { NextResponse } from 'next/server';

export async function GET() {
  const agentId = process.env.ELEVENLABS_AGENT_ID;
  if (!agentId) {
    throw Error('ELEVENLABS_AGENT_ID is not set');
  }
  try {
    const elevenlabs = new ElevenLabsClient();
    const response = await elevenlabs.conversationalAi.conversations.getSignedUrl({
      agentId,
    });
    return NextResponse.json({ signedUrl: response.signedUrl });
  } catch (error) {
    console.error('Error:', error);
    return NextResponse.json({ error: 'Failed to get signed URL' }, { status: 500 });
  }
}
```

### Start the conversation session

To start the conversation, first, call your API route to get the signed URL, then use the `useConversation` hook to set up the conversation session.

```tsx ./page.tsx {1,4,20-25,31-46}
import { useConversation } from '@elevenlabs/react';

async function getSignedUrl(): Promise<string> {
  const response = await fetch('/api/signed-url');
  if (!response.ok) {
    throw Error('Failed to get signed url');
  }
  const data = await response.json();
  return data.signedUrl;
}

export default function Home() {
  // ...
  const [currentStep, setCurrentStep] = useState<
    'initial' | 'training' | 'voice' | 'email' | 'ready'
  >('initial');
  const [conversationId, setConversationId] = useState('');
  const [userName, setUserName] = useState('');

  const conversation = useConversation({
    onConnect: () => console.log('Connected'),
    onDisconnect: () => console.log('Disconnected'),
    onMessage: (message: string) => console.log('Message:', message),
    onError: (error: Error) => console.error('Error:', error),
  });

  const startConversation = useCallback(async () => {
    try {
      // Request microphone permission
      await navigator.mediaDevices.getUserMedia({ audio: true });
      // Start the conversation with your agent
      const signedUrl = await getSignedUrl();
      const convId = await conversation.startSession({
        signedUrl,
        dynamicVariables: {
          user_name: userName,
        },
        clientTools: {
          set_ui_state: ({ step }: { step: string }): string => {
            // Allow agent to navigate the UI.
            setCurrentStep(step as 'initial' | 'training' | 'voice' | 'email' | 'ready');
            return `Navigated to ${step}`;
          },
        },
      });
      setConversationId(convId);
      console.log('Conversation ID:', convId);
    } catch (error) {
      console.error('Failed to start conversation:', error);
    }
  }, [conversation, userName]);
  const stopConversation = useCallback(async () => {
    await conversation.endSession();
  }, [conversation]);
  // ...
}
```

### Client tool and dynamic variables

In the agent configuration earlier, you registered the `set_ui_state` client tool to allow the agent to navigate between the different UI states. To put it all together, you need to pass the client tool implementation to the `conversation.startSession` options.

This is also where you can pass in the dynamic variables to the conversation.

```tsx ./page.tsx {3-5,7-11}
const convId = await conversation.startSession({
  signedUrl,
  dynamicVariables: {
    user_name: userName,
  },
  clientTools: {
    set_ui_state: ({ step }: { step: string }): string => {
      // Allow agent to navigate the UI.
      setCurrentStep(step as 'initial' | 'training' | 'voice' | 'email' | 'ready');
      return `Navigated to ${step}`;
    },
  },
});
```

### Uploading documents to the knowledge base

In the `Training` step, the agent will ask the user to upload documents or submit URLs to public websites with information that should be available to their agent. Here you can utilise the new `after` function of [Next.js 15](https://nextjs.org/docs/app/api-reference/functions/after) to allow uploading of documents in the background.

Create a new `upload` server action to handle the knowledge base creation upon form submission. Once all knowledge base documents have been created, store the conversation ID and the knowledge base IDs in the Redis database.

```tsx ./app/actions/upload.ts {26,32,44,56-60}
'use server';

import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import { Redis } from '@upstash/redis';
import { redirect } from 'next/navigation';
import { after } from 'next/server';

// Initialize Redis
const redis = Redis.fromEnv();

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

export async function uploadFormData(formData: FormData) {
  const knowledgeBase: Array<{
    id: string;
    type: 'file' | 'url';
    name: string;
  }> = [];
  const files = formData.getAll('file-upload') as File[];
  const email = formData.get('email-input');
  const urls = formData.getAll('url-input');
  const conversationId = formData.get('conversation-id');

  after(async () => {
    // Upload files as background job
    // Create knowledge base entries
    // Loop through files and create knowledge base entries
    for (const file of files) {
      if (file.size > 0) {
        const response = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromFile({
          file,
        });
        if (response.id) {
          knowledgeBase.push({
            id: response.id,
            type: 'file',
            name: file.name,
          });
        }
      }
    }
    // Append all urls
    for (const url of urls) {
      const response = await elevenlabs.conversationalAi.knowledgeBase.documents.createFromUrl({
        url: url as string,
      });
      if (response.id) {
        knowledgeBase.push({
          id: response.id,
          type: 'url',
          name: `url for ${conversationId}`,
        });
      }
    }

    // Store knowledge base IDs and conversation ID in database.
    const redisRes = await redis.set(
      conversationId as string,
      JSON.stringify({ email, knowledgeBase })
    );
    console.log({ redisRes });
  });

  redirect('/success');
}
```


## Handling the post-call webhook

The [post-call webhook](/docs/agents-platform/workflows/post-call-webhooks) is triggered when a call ends and the analysis and data extraction steps have been completed.

There's a few steps that are happening here, namely:

1. Verify the webhook secret and construct the webhook payload.
2. Create a custom voice design based on the `voice_description`.
3. Create a ElevenLabs agent for the users based on the `agent_description` they provided.
4. Retrieve the knowledge base documents from the conversation state stored in Redis and attach the knowledge base to the agent.
5. Send an email to the user to notify them that their custom ElevenLabs agent is ready to chat.

```ts ./app/api/convai-webhook/route.ts
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';
import { Redis } from '@upstash/redis';
import crypto from 'crypto';
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { Resend } from 'resend';

import { EmailTemplate } from '@/components/email/post-call-webhook-email';

// Initialize Redis
const redis = Redis.fromEnv();
// Initialize Resend
const resend = new Resend(process.env.RESEND_API_KEY);

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY,
});

export async function GET() {
  return NextResponse.json({ status: 'webhook listening' }, { status: 200 });
}

export async function POST(req: NextRequest) {
  const secret = process.env.ELEVENLABS_CONVAI_WEBHOOK_SECRET; // Add this to your env variables
  const { event, error } = await constructWebhookEvent(req, secret);
  if (error) {
    return NextResponse.json({ error: error }, { status: 401 });
  }

  if (event.type === 'post_call_transcription') {
    const { conversation_id, analysis, agent_id } = event.data;

    if (
      agent_id === process.env.ELEVENLABS_AGENT_ID &&
      analysis.evaluation_criteria_results.all_data_provided?.result === 'success' &&
      analysis.data_collection_results.voice_description?.value
    ) {
      try {
        // Design the voice
        const voicePreview = await elevenlabs.textToVoice.createPreviews({
          voiceDescription: analysis.data_collection_results.voice_description.value,
          text: 'The night air carried whispers of betrayal, thick as London fog. I adjusted my cufflinks - after all, even spies must maintain appearances, especially when the game is afoot.',
        });
        const voice = await elevenlabs.textToVoice.createVoiceFromPreview({
          voiceName: `voice-${conversation_id}`,
          voiceDescription: `Voice for ${conversation_id}`,
          generatedVoiceId: voicePreview.previews[0].generatedVoiceId,
        });

        // Get the knowledge base from redis
        const redisRes = await getRedisDataWithRetry(conversation_id);
        if (!redisRes) throw new Error('Conversation data not found!');
        // Handle agent creation
        const agent = await elevenlabs.conversationalAi.agents.create({
          name: `Agent for ${conversation_id}`,
          conversationConfig: {
            tts: { voiceId: voice.voiceId },
            agent: {
              prompt: {
                prompt:
                  analysis.data_collection_results.agent_description?.value ??
                  'You are a helpful assistant.',
                knowledgeBase: redisRes.knowledgeBase,
              },
              firstMessage: 'Hello, how can I help you today?',
            },
          },
        });
        console.log('Agent created', { agent: agent.agentId });
        // Send email to user
        console.log('Sending email to', redisRes.email);
        await resend.emails.send({
          from: process.env.RESEND_FROM_EMAIL!,
          to: redisRes.email,
          subject: 'Your ElevenLabs agent is ready to chat!',
          react: EmailTemplate({ agentId: agent.agentId }),
        });
      } catch (error) {
        console.error(error);
        return NextResponse.json({ error }, { status: 500 });
      }
    }
  }

  return NextResponse.json({ received: true }, { status: 200 });
}

const constructWebhookEvent = async (req: NextRequest, secret?: string) => {
  const body = await req.text();
  const signatureHeader = req.headers.get('ElevenLabs-Signature');

  return await elevenlabs.webhooks.constructEvent(body, signatureHeader, secret);
};

async function getRedisDataWithRetry(
  conversationId: string,
  maxRetries = 5
): Promise<{
  email: string;
  knowledgeBase: Array<{
    id: string;
    type: 'file' | 'url';
    name: string;
  }>;
} | null> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const data = await redis.get(conversationId);
      return data as any;
    } catch (error) {
      if (attempt === maxRetries) throw error;
      console.log(`Redis get attempt ${attempt} failed, retrying...`);
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }
  return null;
}
```

Let's go through each step in detail.

### Verify the webhook secret and consrtuct the webhook payload

When the webhook request is received, we first verify the webhook secret and construct the webhook payload.

```ts ./app/api/convai-webhook/route.ts
// ...

export async function POST(req: NextRequest) {
  const secret = process.env.ELEVENLABS_CONVAI_WEBHOOK_SECRET;
  const { event, error } = await constructWebhookEvent(req, secret);
  // ...
}

// ...
const constructWebhookEvent = async (req: NextRequest, secret?: string) => {
  const body = await req.text();
  const signatureHeader = req.headers.get('ElevenLabs-Signature');

  return await elevenlabs.webhooks.constructEvent(body, signatureHeader, secret);
};

async function getRedisDataWithRetry(
  conversationId: string,
  maxRetries = 5
): Promise<{
  email: string;
  knowledgeBase: Array<{
    id: string;
    type: 'file' | 'url';
    name: string;
  }>;
} | null> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const data = await redis.get(conversationId);
      return data as any;
    } catch (error) {
      if (attempt === maxRetries) throw error;
      console.log(`Redis get attempt ${attempt} failed, retrying...`);
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }
  return null;
}
```

### Create a custom voice design based on the `voice_description`

Using the `voice_description` from the webhook payload, we create a custom voice design.

```ts ./app/api/convai-webhook/route.ts {5}
// ...

// Design the voice
const voicePreview = await elevenlabs.textToVoice.createPreviews({
  voiceDescription: analysis.data_collection_results.voice_description.value,
  text: 'The night air carried whispers of betrayal, thick as London fog. I adjusted my cufflinks - after all, even spies must maintain appearances, especially when the game is afoot.',
});
const voice = await elevenlabs.textToVoice.createVoiceFromPreview({
  voiceName: `voice-${conversation_id}`,
  voiceDescription: `Voice for ${conversation_id}`,
  generatedVoiceId: voicePreview.previews[0].generatedVoiceId,
});

// ...
```

### Retrieve the knowledge base documents from the conversation state stored in Redis

The uploading of the documents might take longer than the webhook data analysis, so we'll need to poll the conversation state in Redis until the documents have been uploaded.

```ts ./app/api/convai-webhook/route.ts
// ...

// Get the knowledge base from redis
const redisRes = await getRedisDataWithRetry(conversation_id);
if (!redisRes) throw new Error('Conversation data not found!');
// ...

async function getRedisDataWithRetry(
  conversationId: string,
  maxRetries = 5
): Promise<{
  email: string;
  knowledgeBase: Array<{
    id: string;
    type: 'file' | 'url';
    name: string;
  }>;
} | null> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const data = await redis.get(conversationId);
      return data as any;
    } catch (error) {
      if (attempt === maxRetries) throw error;
      console.log(`Redis get attempt ${attempt} failed, retrying...`);
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }
  return null;
}
```

### Create a ElevenLabs agent for the users based on the `agent_description` they provided

Create the ElevenLabs agent for the user based on the `agent_description` they provided and attach the newly created voice design and knowledge base to the agent.

```ts ./app/api/convai-webhook/route.ts {7,11}
// ...

// Handle agent creation
const agent = await elevenlabs.conversationalAi.agents.create({
  name: `Agent for ${conversationId}`,
  conversationConfig: {
    tts: { voiceId: voice.voiceId },
    agent: {
      prompt: {
        prompt:
          analysis.data_collection_results.agent_description?.value ??
          'You are a helpful assistant.',
        knowledgeBase: redisRes.knowledgeBase,
      },
      firstMessage: 'Hello, how can I help you today?',
    },
  },
});
console.log('Agent created', { agent: agent.agentId });

// ...
```

### Send an email to the user to notify them that their custom ElevenLabs agent is ready to chat

Once the agent is created, you can send an email to the user to notify them that their custom ElevenLabs agent is ready to chat.

```ts ./app/api/convai-webhook/route.ts
import { Resend } from 'resend';

import { EmailTemplate } from '@/components/email/post-call-webhook-email';

// ...

// Send email to user
console.log('Sending email to', redisRes.email);
await resend.emails.send({
  from: process.env.RESEND_FROM_EMAIL!,
  to: redisRes.email,
  subject: 'Your ElevenLabs agent is ready to chat!',
  react: EmailTemplate({ agentId: agent.agentId }),
});

// ...
```

You can use [new.email](https://new.email/), a handy tool from the Resend team, to vibe design your email templates. Once you're happy with the template, create a new component and add in the agent ID as a prop.

```tsx ./components/email/post-call-webhook-email.tsx {14}
import {
  Body,
  Button,
  Container,
  Head,
  Html,
  Section,
  Text,
  Tailwind,
} from '@react-email/components';
import * as React from 'react';

const EmailTemplate = (props: any) => {
  const { agentId } = props;
  return (
    <Html>
      <Head />
      <Tailwind>
        <Body className="bg-[#151516] font-sans">
          <Container className="mx-auto my-[40px] max-w-[600px] rounded-[8px] bg-[#0a1929] p-[20px]">
            {/* Top Section */}
            <Section className="mb-[32px] mt-[32px] text-center">
              <Text className="m-0 text-[28px] font-bold text-[#9c27b0]">
                Your ElevenLabs agent is ready to chat!
              </Text>
            </Section>

            {/* Content Area with Icon */}
            <Section className="mb-[32px] text-center">
              {/* Circle Icon with Checkmark */}
              <div className="mx-auto mb-[24px] flex h-[80px] w-[80px] items-center justify-center rounded-full bg-gradient-to-r from-[#9c27b0] to-[#3f51b5]">
                <div className="text-[40px] text-white">✓</div>
              </div>

              {/* Descriptive Text */}
              <Text className="mb-[24px] text-[18px] text-white">
                Your ElevenLabs agent is ready to chat!
              </Text>
            </Section>

            {/* Call to Action Button */}
            <Section className="mb-[32px] text-center">
              <Button
                href={`https://elevenlabs.io/app/talk-to?agent_id=${agentId}`}
                className="box-border rounded-[8px] bg-[#9c27b0] px-[40px] py-[20px] text-[24px] font-bold text-white no-underline"
              >
                Chat now!
              </Button>
            </Section>

            {/* Footer */}
            <Section className="mt-[40px] border-t border-[#2d3748] pt-[20px] text-center">
              <Text className="m-0 text-[14px] text-white">
                Powered by{' '}
                <a
                  href="https://elevenlabs.io/conversational-ai"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="underline transition-colors hover:text-gray-400"
                >
                  ElevenLabs Agents
                </a>
              </Text>
            </Section>
          </Container>
        </Body>
      </Tailwind>
    </Html>
  );
};

export { EmailTemplate };
```


## Run the app

To run the app locally end-to-end, you will need to first run the Next.js development server, and then in a separate terminal run the ngrok tunnel to expose the webhook handler to the internet.

* Terminal 1:
  * Run `pnpm dev` to start the Next.js development server.

```bash
pnpm dev
```

* Terminal 2:
  * Run `ngrok http 3000` to expose the webhook handler to the internet.

```bash
ngrok http 3000
```

Now open [http://localhost:3000](http://localhost:3000) and start designing your custom ElevenLabs agent, with your voice!


## Conclusion

[ElevenLabs Agents](https://elevenlabs.io/conversational-ai) is a powerful platform for building advanced voice agent uses cases, complete with data collection and analysis.



# Build a Voice Assistant with Agents Platform on a Raspberry Pi

> Build a voice assistant with Agents Platform on a Raspberry Pi.


## Introduction

In this tutorial you will learn how to build a voice assistant with Agents Platform running on a Raspberry Pi. Just like conventional home assistants like Alexa on Amazon Echo, Google Home, or Siri on Apple devices, your Eleven Voice assistant will listen to a hotword, in our case "Hey Eleven", and then initiate an ElevenLabs Agents session to assist the user.

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/OrRlN_gUFRg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

<Tip title="Prefer to jump straight to the code?" icon="lightbulb">
  Find the [example project on
  GitHub](https://github.com/elevenlabs/elevenlabs-examples/tree/main/examples/conversational-ai/raspberry-pi).
</Tip>


## Requirements

* A Raspberry Pi 5 or similar device.
* A microphone and speaker.
* Python 3.9 or higher installed on your machine.
* An ElevenLabs account with an [API key](https://elevenlabs.io/app/settings/api-keys).


## Setup

### Install dependencies

On Debian-based systems you can install the dependencies with:

```bash
sudo apt-get update
sudo apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
```

### Create the project

On your Raspberry Pi, open the terminal and create a new directory for your project.

```bash
mkdir eleven-voice-assistant
cd eleven-voice-assistant
```

Create a new virtual environment and install the dependencies:

```bash
python -m venv .venv # Only required the first time you set up the project
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install tflite-runtime
pip install librosa
pip install EfficientWord-Net
pip install elevenlabs
pip install "elevenlabs[pyaudio]"
```

Now create a new python file called `hotword.py` and add the following code:

```python hotword.py
import os
import signal
import time
from eff_word_net.streams import SimpleMicStream
from eff_word_net.engine import HotwordDetector

from eff_word_net.audio_processing import Resnet50_Arc_loss


# from eff_word_net import samples_loc

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ConversationInitiationData
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

convai_active = False

elevenlabs = ElevenLabs()
agent_id = os.getenv("ELEVENLABS_AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")

dynamic_vars = {
    'user_name': 'Thor',
    'greeting': 'Hey'
}

config = ConversationInitiationData(
    dynamic_variables=dynamic_vars
)

base_model = Resnet50_Arc_loss()

eleven_hw = HotwordDetector(
    hotword="hey_eleven",
    model = base_model,
    reference_file=os.path.join("hotword_refs", "hey_eleven_ref.json"),
    threshold=0.7,
    relaxation_time=2
)

def create_conversation():
    """Create a new conversation instance"""
    return Conversation(
        # API client and agent ID.
        elevenlabs,
        agent_id,
        config=config,

        # Assume auth is required when API_KEY is set.
        requires_auth=bool(api_key),

        # Use the default audio interface.
        audio_interface=DefaultAudioInterface(),

        # Simple callbacks that print the conversation to the console.
        callback_agent_response=lambda response: print(f"Agent: {response}"),
        callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
        callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

        # Uncomment if you want to see latency measurements.
        # callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
    )

def start_mic_stream():
    """Start or restart the microphone stream"""
    global mic_stream
    try:
        # Always create a new stream instance
        mic_stream = SimpleMicStream(
            window_length_secs=1.5,
            sliding_window_secs=0.75,
        )
        mic_stream.start_stream()
        print("Microphone stream started")
    except Exception as e:
        print(f"Error starting microphone stream: {e}")
        mic_stream = None
        time.sleep(1)  # Wait a bit before retrying

def stop_mic_stream():
    """Stop the microphone stream safely"""
    global mic_stream
    try:
        if mic_stream:
            # SimpleMicStream doesn't have a stop_stream method
            # We'll just set it to None and recreate it next time
            mic_stream = None
            print("Microphone stream stopped")
    except Exception as e:
        print(f"Error stopping microphone stream: {e}")


# Initialize microphone stream
mic_stream = None
start_mic_stream()

print("Say Hey Eleven ")
while True:
    if not convai_active:
        try:
            # Make sure we have a valid mic stream
            if mic_stream is None:
                start_mic_stream()
                continue

            frame = mic_stream.getFrame()
            result = eleven_hw.scoreFrame(frame)
            if result == None:
                #no voice activity
                continue
            if result["match"]:
                print("Wakeword uttered", result["confidence"])

                # Stop the microphone stream to avoid conflicts
                stop_mic_stream()

                # Start ConvAI Session
                print("Start ConvAI Session")
                convai_active = True

                try:
                    # Create a new conversation instance
                    conversation = create_conversation()

                    # Start the session
                    conversation.start_session()

                    # Set up signal handler for graceful shutdown
                    def signal_handler(sig, frame):
                        print("Received interrupt signal, ending session...")
                        try:
                            conversation.end_session()
                        except Exception as e:
                            print(f"Error ending session: {e}")

                    signal.signal(signal.SIGINT, signal_handler)

                    # Wait for session to end
                    conversation_id = conversation.wait_for_session_end()
                    print(f"Conversation ID: {conversation_id}")

                except Exception as e:
                    print(f"Error during conversation: {e}")
                finally:
                    # Cleanup
                    convai_active = False
                    print("Conversation ended, cleaning up...")

                    # Give some time for cleanup
                    time.sleep(1)

                    # Restart microphone stream
                    start_mic_stream()
                    print("Ready for next wake word...")

        except Exception as e:
            print(f"Error in wake word detection: {e}")
            # Try to restart microphone stream if there's an error
            mic_stream = None
            time.sleep(1)
            start_mic_stream()
```


## Agent configuration

<Steps>
  <Step title="Sign in to ElevenLabs">
    Go to [elevenlabs.io](https://elevenlabs.io/sign-up) and sign in to your account.
  </Step>

  <Step title="Create a new agent">
    Navigate to [Agents Platform > Agents](https://elevenlabs.io/app/agents/agents) and
    create a new agent from the blank template.
  </Step>

  <Step title="Set the first message">
    Set the first message and specify the dynamic variable for the platform.

    ```txt
    {{greeting}} {{user_name}}, Eleven here, what's up?
    ```
  </Step>

  <Step title="Set the system prompt">
    Set the system prompt. You can find our best practises docs [here](/docs/agents-platform/best-practices/prompting-guide).

    ```txt
    You are a helpful Agents Platform assistant with access to a weather tool. When users ask about
    weather conditions, use the get_weather tool to fetch accurate, real-time data. The tool requires
    a latitude and longitude - use your geographic knowledge to convert location names to coordinates
    accurately.

    Never ask users for coordinates - you must determine these yourself. Always report weather
    information conversationally, referring to locations by name only. For weather requests:

    1. Extract the location from the user's message
    2. Convert the location to coordinates and call get_weather
    3. Present the information naturally and helpfully

    For non-weather queries, provide friendly assistance within your knowledge boundaries. Always be
    concise, accurate, and helpful.
    ```
  </Step>

  <Step title="Set up a server tool">
    We'll set up a simple server tool that will fetch the weather data for us. Follow the setup steps [here](/docs/agents-platform/customization/tools/server-tools#configure-the-weather-tool) to set up the tool.
  </Step>
</Steps>


## Run the app

To run the app, first set the required environment variables:

```bash
export ELEVENLABS_API_KEY=YOUR_API_KEY
export ELEVENLABS_AGENT_ID=YOUR_AGENT_ID
```

Then simply run the following command:

```bash
python hotword.py
```

Now say "Hey Eleven" to start the conversation. Happy chattin'!


## \[Optional] Train your custom hotword

### Generate training audio

To generate the hotword embeddings, you can use ElevenLabs to generate four training samples. Simply navigate to [Text To Speech](https://elevenlabs.io/app/speech-synthesis/text-to-speech) within your ElevenLabs app, and type in your hotword, e.g. "Hey Eleven". Select a voice and click on the "Generate" button.

After the audio has been generated, download the audio file and save them into a folder called `hotword_training_audio` at the root of your project. Repeat this process three more times with different voices.

### Train the hotword

In your terminal, with your virtual environment activated, run the following command to train the hotword:

```bash
python -m eff_word_net.generate_reference --input-dir hotword_training_audio --output-dir hotword_refs --wakeword hey_eleven --model-type resnet_50_arc
```

This will generate the `hey_eleven_ref.json` file in the `hotword_refs` folder. Now you simply need to update the `reference_file` parameter in the `HotwordDetector` class in `hotword.py` to point to the new reference file and you're good to go!



# Multi-Context Websocket

> Learn how to build real time voice agents using our multi-context WebSocket API for dynamic and responsive interactions.

<Warning title="Advanced">
  Orchestrating voice agents using this multi-context WebSocket API is a complex task recommended
  for advanced developers. For a more managed solution, consider exploring our [Agents Platform
  product](/docs/agents-platform/overview), which simplifies many of these challenges.
</Warning>

<Info>
  Multi-context WebSockets are not available for the 

  `eleven_v3`

   model.
</Info>


## Overview

Building responsive voice agents requires the ability to manage audio streams dynamically, handle interruptions gracefully, and maintain natural-sounding speech across conversational turns. Our multi-context WebSocket API for Text to Speech (TTS) is specifically designed for these scenarios.

This API extends our [standard TTS WebSocket functionality](/docs/websockets) by introducing the concept of "contexts." Each context operates as an independent audio generation stream within a single WebSocket connection. This allows you to:

* Manage multiple lines of speech concurrently (e.g., agent speaking while preparing a response to a user interruption).
* Seamlessly handle user barge-ins by closing an existing speech context and initiating a new one.
* Maintain prosodic consistency for utterances within the same logical context.
* Optimize resource usage by selectively closing contexts that are no longer needed.

<Warning>
  The multi-context WebSocket API is optimized for voice applications and is not intended for
  generating multiple unrelated audio streams simultaneously. Each connection is limited to 5
  concurrent contexts to reflect this.
</Warning>

This guide will walk you through connecting to the multi-context WebSocket, managing contexts, and applying best practices for building engaging voice agents.

### Best practices

<Note>
  These best practices are essential for building responsive, efficient voice agents with our
  multi-context WebSocket API.
</Note>

<Steps>
  <Step title="Use a single WebSocket connection">
    Establish one WebSocket connection for each end-user session. This reduces overhead and latency
    compared to creating multiple connections. Within this single connection, you can manage
    multiple contexts for different parts of the conversation.
  </Step>

  <Step title="Stream responses in chunks, generate sentences">
    When generating long responses, stream the text in smaller chunks and use the `flush: true` flag
    at the end of complete sentences. This improves the quality of the generated audio and improves
    responsiveness.
  </Step>

  <Step title="Handle interruptions gracefully">
    Stream text into one context until an interruption occurs, then create a new context and close
    the existing one. This approach ensures smooth transitions when the conversation flow changes.
  </Step>

  <Step title="Manage context lifecycle">
    Close unused contexts promptly. The server can maintain up to 5 concurrent contexts per
    connection, but you should close contexts when they are no longer needed.
  </Step>

  <Step title="Prevent context timeouts">
    Contexts by default timeout after 20 seconds and are closed automatically. The inactivity
    timeout is a websocket level parameter that applies to all contexts and can be up to 180 seconds
    if needed. Send an empty text message on a context to reset the timeout clock.
  </Step>
</Steps>

### Handling interuptions

When a user interrupts your agent, you should [close the current context](/docs/api-reference/multi-context-text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input#send.Close-Context) and [create a new one](/docs/api-reference/multi-context-text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input#send.Initialise-Context):

<CodeBlocks>
  ```python
  async def handle_interruption(websocket, old_context_id, new_context_id, new_response):
      # Close the existing context that was interrupted
      await websocket.send(json.dumps({
          "context_id": old_context_id,
          "close_context": True
      }))
      print(f"Closed interrupted context '{old_context_id}'")

      # Create a new context for the new response
      await send_text_in_context(websocket, new_response, new_context_id)
  ```

  ```javascript
  function handleInterruption(websocket: WebSocket, oldContextId: string, newContextId: string, newResponse: string) {
    // Close the existing context that was interrupted
    websocket.send(JSON.stringify({
      context_id: oldContextId,
      close_context: true
    }));
    console.log(`Closed interrupted context '${oldContextId}'`);

    // Create a new context for the new response
    sendTextInContext(websocket, newResponse, newContextId);
  }
  ```
</CodeBlocks>

### Keeping a context alive

Contexts automatically timeout after [a default of 20 seconds of inactivity](/docs/api-reference/multi-context-text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input#request.query.inactivity_timeout). If you need to keep a context alive without generating text (for example, during a processing delay), you can send an empty text message to reset the timeout clock.

<CodeBlocks>
  ```python
  async def keep_context_alive(websocket, context_id):
      await websocket.send(json.dumps({
          "context_id": context_id,
          "text": ""
      }))
  ```

  ```javascript
  function handleInterruption(websocket: WebSocket, contextId: string) {
    // Close the existing context that was interrupted
    websocket.send(JSON.stringify({
      context_id: oldContextId,
      text: ""
    }));
  }
  ```
</CodeBlocks>

### Closing the WebSocket connection

When your conversation ends, you can clean up all contexts by [closing the socket](/docs/api-reference/multi-context-text-to-speech/v-1-text-to-speech-voice-id-multi-stream-input#send.Close-Socket):

<CodeBlocks>
  ```python
  async def end_conversation(websocket):
      # This will close all contexts and close the connection
      await websocket.send(json.dumps({
          "close_socket": True
      }))
      print("Ending conversation and closing WebSocket")`
  ```

  ```javascript
  function endConversation(websocket: WebSocket) {
    // This will close all contexts and close the connection
    websocket.send(JSON.stringify({
      close_socket: true
    }));
    console.log("Ending conversation and closing WebSocket");
  }
  ```
</CodeBlocks>


## Complete conversational agent example

### Requirements

* An ElevenLabs account with an API key (learn how to [find your API key](/docs/api-reference/authentication)).
* Python or Node.js (or another JavaScript runtime) installed on your machine.
* Familiarity with WebSocket communication. We recommend reading our [guide on standard WebSocket streaming](/docs/websockets) for foundational concepts.

### Setup

Install the necessary dependencies for your chosen language:

<CodeBlocks>
  ```python
  pip install python-dotenv websockets
  ```

  ```javascript
  npm install dotenv ws
  for TypeScript, you might also want types:
  npm install @types/dotenv @types/ws --save-dev
  ```
</CodeBlocks>

Create a .env file in your project directory to store your API key:

<CodeBlocks>
  ```python .env
  ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
  ```
</CodeBlocks>

### Example voice agent

<Note>
  This code is provided as an example and is not intended for production usage
</Note>

<CodeBlocks>
  ```python maxLines=100
  import os
  import json
  import asyncio
  import websockets
  from dotenv import load_dotenv

  load_dotenv()
  ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
  VOICE_ID = "your_voice_id"
  MODEL_ID = "eleven_flash_v2_5"

  WEBSOCKET_URI = f"wss://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/multi-stream-input?model_id={MODEL_ID}"

  async def send_text_in_context(websocket, text, context_id, voice_settings=None):
      """Send text to be synthesized in the specified context."""
      message = {
          "text": text,
          "context_id": context_id,
      }

      # Only include voice_settings for the first message in a context
      if voice_settings:
          message["voice_settings"] = voice_settings

      await websocket.send(json.dumps(message))

  async def continue_context(websocket, text, context_id):
      """Add more text to an existing context."""
      await websocket.send(json.dumps({
          "text": text,
          "context_id": context_id
      }))

  async def flush_context(websocket, context_id):
      """Force generation of any buffered audio in the context."""
      await websocket.send(json.dumps({
          "context_id": context_id,
          "flush": True
      }))

  async def handle_interruption(websocket, old_context_id, new_context_id, new_response):
      """Handle user interruption by closing current context and starting a new one."""
      # Close the existing context that was interrupted
      await websocket.send(json.dumps({
          "context_id": old_context_id,
          "close_context": True
      }))

      # Create a new context for the new response
      await send_text_in_context(websocket, new_response, new_context_id)

  async def end_conversation(websocket):
      """End the conversation and close the WebSocket connection."""
      await websocket.send(json.dumps({
          "close_socket": True
      }))

  async def receive_messages(websocket):
      """Process incoming WebSocket messages."""
      context_audio = {}
      try:
          async for message in websocket:
              data = json.loads(message)
              context_id = data.get("contextId", "default")

              if data.get("audio"):
                  print(f"Received audio for context '{context_id}'")

              if data.get("is_final"):
                  print(f"Context '{context_id}' completed")
      except (websockets.exceptions.ConnectionClosed, asyncio.CancelledError):
          print("Message receiving stopped")

  async def conversation_agent_demo():
      """Run a complete conversational agent demo."""
      # Connect with API key in headers
      async with websockets.connect(
          WEBSOCKET_URI,
          max_size=16 * 1024 * 1024,
          additional_headers={"xi-api-key": ELEVENLABS_API_KEY}
      ) as websocket:
          # Start receiving messages in background
          receive_task = asyncio.create_task(receive_messages(websocket))

          # Initial agent response
          await send_text_in_context(
              websocket,
              "Hello! I'm your virtual assistant. I can help you with a wide range of topics. What would you like to know about today?",
              "greeting"
          )

          # Wait a bit (simulating user listening)
          await asyncio.sleep(2)

          # Simulate user interruption
          print("USER INTERRUPTS: 'Can you tell me about the weather?'")

          # Handle the interruption by closing current context and starting new one
          await handle_interruption(
              websocket,
              "greeting",
              "weather_response",
              "I'd be happy to tell you about the weather. Currently in your area, it's 72 degrees and sunny with a slight chance of rain later this afternoon."
          )

          # Add more to the weather context
          await continue_context(
              websocket,
              " If you're planning to go outside, you might want to bring a light jacket just in case.",
              "weather_response"
          )

          # Flush at the end of this turn to ensure all audio is generated
          await flush_context(websocket, "weather_response")

          # Wait a bit (simulating user listening)
          await asyncio.sleep(3)

          # Simulate user asking another question
          print("USER: 'What about tomorrow?'")

          # Create a new context for this response
          await send_text_in_context(
              websocket,
              "Tomorrow's forecast shows temperatures around 75 degrees with partly cloudy skies. It should be a beautiful day overall!",
              "tomorrow_weather"
          )

          # Flush and close this context
          await flush_context(websocket, "tomorrow_weather")
          await websocket.send(json.dumps({
              "context_id": "tomorrow_weather",
              "close_context": True
          }))

          # End the conversation
          await asyncio.sleep(2)
          await end_conversation(websocket)

          # Cancel the receive task
          receive_task.cancel()
          try:
              await receive_task
          except asyncio.CancelledError:
              pass

  if __name__ == "__main__":
      asyncio.run(conversation_agent_demo())

  ```

  ```javascript maxLines=100
  // Import required modules
  import dotenv from 'dotenv';
  import fs from 'fs';
  import WebSocket from 'ws';

  // Load environment variables
  dotenv.config();
  const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
  const VOICE_ID = 'your_voice_id';
  const MODEL_ID = 'eleven_flash_v2_5';

  const WEBSOCKET_URI = `wss://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}/multi-stream-input?model_id=${MODEL_ID}`;

  // Function to send text in a specific context
  function sendTextInContext(websocket, text, contextId, voiceSettings = null) {
    const message = {
      text: text,
      context_id: contextId,
    };

    // Only include voice_settings for the first message in a context
    if (voiceSettings) {
      message.voice_settings = voiceSettings;
    }

    websocket.send(JSON.stringify(message));
  }

  // Function to continue an existing context with more text
  function continueContext(websocket, text, contextId) {
    websocket.send(
      JSON.stringify({
        text: text,
        context_id: contextId,
      })
    );
  }

  // Function to flush a context, forcing generation of buffered audio
  function flushContext(websocket, contextId) {
    websocket.send(
      JSON.stringify({
        context_id: contextId,
        flush: true,
      })
    );
  }

  // Function to handle user interruption
  function handleInterruption(websocket, oldContextId, newContextId, newResponse) {
    // Close the existing context that was interrupted
    websocket.send(
      JSON.stringify({
        context_id: oldContextId,
        close_context: true,
      })
    );

    // Create a new context for the new response
    sendTextInContext(websocket, newResponse, newContextId);
  }

  // Function to end the conversation and close the connection
  function endConversation(websocket) {
    websocket.send(
      JSON.stringify({
        close_socket: true,
      })
    );
  }

  // Function to run the conversation agent demo
  async function conversationAgentDemo() {
    // Connect to WebSocket with API key in headers
    const websocket = new WebSocket(WEBSOCKET_URI, {
      headers: {
        'xi-api-key': ELEVENLABS_API_KEY,
      },
      maxPayload: 16 * 1024 * 1024,
    });

    // Set up event handlers
    websocket.on('open', () => {
      // Initial agent response
      sendTextInContext(
        websocket,
        "Hello! I'm your virtual assistant. I can help you with a wide range of topics. What would you like to know about today?",
        'greeting'
      );

      // Simulate wait time (user listening)
      setTimeout(() => {
        // Simulate user interruption
        console.log("USER INTERRUPTS: 'Can you tell me about the weather?'");

        // Handle the interruption
        handleInterruption(
          websocket,
          'greeting',
          'weather_response',
          "I'd be happy to tell you about the weather. Currently in your area, it's 72 degrees and sunny with a slight chance of rain later this afternoon."
        );

        // Add more to the weather context
        setTimeout(() => {
          continueContext(
            websocket,
            " If you're planning to go outside, you might want to bring a light jacket just in case.",
            'weather_response'
          );

          // Flush at the end of this turn
          flushContext(websocket, 'weather_response');

          // Simulate wait time (user listening)
          setTimeout(() => {
            // Simulate user asking another question
            console.log("USER: 'What about tomorrow?'");

            // Create a new context for this response
            sendTextInContext(
              websocket,
              "Tomorrow's forecast shows temperatures around 75 degrees with partly cloudy skies. It should be a beautiful day overall!",
              'tomorrow_weather'
            );

            // Flush and close this context
            flushContext(websocket, 'tomorrow_weather');
            websocket.send(
              JSON.stringify({
                context_id: 'tomorrow_weather',
                close_context: true,
              })
            );

            // End the conversation
            setTimeout(() => {
              endConversation(websocket);
            }, 2000);
          }, 3000);
        }, 500);
      }, 2000);
    });

    // Handle incoming messages
    websocket.on('message', (message) => {
      try {
        const data = JSON.parse(message);
        const contextId = data.contextId || 'default';

        if (data.audio) {
          //do stuff
        }

        if (data.is_final) {
          console.log(`Context '${contextId}' completed`);
        }
      } catch (error) {
        console.error('Error parsing message:', error);
      }
    });

    // Handle WebSocket closure
    websocket.on('close', () => {
      console.log('WebSocket connection closed');
    });

    // Handle WebSocket errors
    websocket.on('error', (error) => {
      console.error('WebSocket error:', error);
    });
  }

  // Run the demo
  conversationAgentDemo();
  ```
</CodeBlocks>



# Libraries & SDKs

> Explore language-specific libraries for using the ElevenLabs API.


## Official REST API libraries

ElevenLabs provides officially supported libraries that are updated with the latest features available in the [REST API](/docs/api-reference/introduction).

| Language          | GitHub                                                           | Package Manager                                                |
| ----------------- | ---------------------------------------------------------------- | -------------------------------------------------------------- |
| Python            | [GitHub README](https://github.com/elevenlabs/elevenlabs-python) | [PyPI](https://pypi.org/project/elevenlabs/)                   |
| Javascript (Node) | [GitHub README](https://github.com/elevenlabs/elevenlabs-js)     | [npm](https://www.npmjs.com/package/@elevenlabs/elevenlabs-js) |

Test and explore all ElevenLabs API endpoints using our official [Postman collection](https://www.postman.com/elevenlabs/elevenlabs/collection/7i9rytu/elevenlabs-api-documentation?action=share\&creator=39903018).


## Official Agents Platform libraries

These libraries are designed for use with ElevenLabs [Agents Platform](/docs/agents-platform/overview).

| Language     | Documentation                                        | Package Manager                                                                 |
| ------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------- |
| Javascript   | [Docs](/docs/agents-platform/libraries/java-script)  | [npm](https://www.npmjs.com/package/@elevenlabs/client)                         |
| React        | [Docs](/docs/agents-platform/libraries/react)        | [npm](https://www.npmjs.com/package/@elevenlabs/react)                          |
| React Native | [Docs](/docs/agents-platform/libraries/react-native) | [npm](https://www.npmjs.com/package/@elevenlabs/react-native)                   |
| Python       | [Docs](/docs/agents-platform/libraries/python)       | [PyPI](https://pypi.org/project/elevenlabs/)                                    |
| Swift        | [Docs](/docs/agents-platform/libraries/swift)        | [Github](https://github.com/elevenlabs/ElevenLabsSwift)                         |
| Kotlin       | [Docs](/docs/agents-platform/libraries/kotlin)       | [Maven](https://central.sonatype.com/artifact/io.elevenlabs/elevenlabs-android) |


## Third-party libraries

These libraries are not officially supported by ElevenLabs, but are community-maintained.

| Library       | Documentation                                                      | Package Manager                                              |
| ------------- | ------------------------------------------------------------------ | ------------------------------------------------------------ |
| Vercel AI SDK | [Docs](/docs/cookbooks/speech-to-text/vercel-ai-sdk)               | [npm](https://www.npmjs.com/package/ai)                      |
| .NET          | [Docs](https://github.com/RageAgainstThePixel/ElevenLabs-DotNet)   | [NuGet](https://www.nuget.org/packages/ElevenLabs-DotNet)    |
| Unity         | [Docs](https://github.com/RageAgainstThePixel/com.rest.elevenlabs) | [OpenUPM](https://openupm.com/packages/com.rest.elevenlabs/) |



# Generate audio in real-time

> Learn how to generate audio in real-time via a WebSocket connection.

WebSocket streaming is a method of sending and receiving data over a single, long-lived connection. This method is useful for real-time applications where you need to stream audio data as it becomes available.

If you want to quickly test out the latency (time to first byte) of a WebSocket connection to the ElevenLabs text-to-speech API, you can install `elevenlabs-latency` via `npm` and follow the instructions [here](https://www.npmjs.com/package/elevenlabs-latency?activeTab=readme).

<Note>
  WebSockets can be used with the Text to Speech and Agents Platform products. This guide will
  demonstrate how to use them with the Text to Speech API. WebSockets are not available for the
  `eleven_v3` model.
</Note>


## Requirements

* An ElevenLabs account with an API key (here’s how to [find your API key](/docs/api-reference/authentication)).
* Python or Node.js (or another JavaScript runtime) installed on your machine


## Setup

Install required dependencies:

<CodeBlocks>
  ```python Python
  pip install python-dotenv
  pip install websockets
  ```

  ```typescript TypeScript
  npm install dotenv
  npm install @types/dotenv --save-dev
  npm install ws
  ```
</CodeBlocks>

Next, create a `.env` file in your project directory and add your API key:

```bash .env
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```


## Initiate the websocket connection

After choosing a voice from the Voice Library and the text to speech model you wish to use, initiate a WebSocket connection to the text to speech API.

<CodeBlocks>
  ```python text-to-speech-websocket.py
  import os
  from dotenv import load_dotenv
  import websockets

  # Load the API key from the .env file
  load_dotenv()
  ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

  voice_id = 'Xb7hH8MSUJpSbSDYk0k2'

  # For use cases where latency is important, we recommend using the 'eleven_flash_v2_5' model.
  model_id = 'eleven_flash_v2_5'

  async def text_to_speech_ws_streaming(voice_id, model_id):
      uri = f"wss://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream-input?model_id={model_id}"

      async with websockets.connect(uri) as websocket:
         ...
  ```

  ```typescript text-to-speech-websocket.ts
  import * as dotenv from 'dotenv';
  import * as fs from 'node:fs';
  import WebSocket from 'ws';

  // Load the API key from the .env file
  dotenv.config();
  const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;

  const voiceId = 'Xb7hH8MSUJpSbSDYk0k2';

  // For use cases where latency is important, we recommend using the 'eleven_flash_v2_5' model.
  const model = 'eleven_flash_v2_5';

  const uri = `wss://api.elevenlabs.io/v1/text-to-speech/${voiceId}/stream-input?model_id=${model}`;
  const websocket = new WebSocket(uri, {
    headers: { 'xi-api-key': `${ELEVENLABS_API_KEY}` },
  });

  // Create a directory for saving the audio
  const outputDir = './output';

  try {
    fs.accessSync(outputDir, fs.constants.R_OK | fs.constants.W_OK);
  } catch (err) {
    fs.mkdirSync(outputDir);
  }

  // Create a write stream for saving the audio into mp3
  const writeStream = fs.createWriteStream(outputDir + '/test.mp3', {
    flags: 'a',
  });
  ```
</CodeBlocks>


## Send the input text

Once the WebSocket connection is open, set up voice settings first. Next, send the text message to the API.

<CodeBlocks>
  ```python text-to-speech-websocket.py
  async def text_to_speech_ws_streaming(voice_id, model_id):
      async with websockets.connect(uri) as websocket:
          await websocket.send(json.dumps({
              "text": " ",
              "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "use_speaker_boost": False},
              "generation_config": {
                  "chunk_length_schedule": [120, 160, 250, 290]
              },
              "xi_api_key": ELEVENLABS_API_KEY,
          }))

          text = "The twilight sun cast its warm golden hues upon the vast rolling fields, saturating the landscape with an ethereal glow. Silently, the meandering brook continued its ceaseless journey, whispering secrets only the trees seemed privy to."
          await websocket.send(json.dumps({"text": text}))

          // Send empty string to indicate the end of the text sequence which will close the WebSocket connection
          await websocket.send(json.dumps({"text": ""}))
  ```

  ```typescript text-to-speech-websocket.ts
  const text =
    'The twilight sun cast its warm golden hues upon the vast rolling fields, saturating the landscape with an ethereal glow. Silently, the meandering brook continued its ceaseless journey, whispering secrets only the trees seemed privy to.';

  websocket.on('open', async () => {
    websocket.send(
      JSON.stringify({
        text: ' ',
        voice_settings: {
          stability: 0.5,
          similarity_boost: 0.8,
          use_speaker_boost: false,
        },
        generation_config: { chunk_length_schedule: [120, 160, 250, 290] },
      })
    );

    websocket.send(JSON.stringify({ text: text }));

    // Send empty string to indicate the end of the text sequence which will close the websocket connection
    websocket.send(JSON.stringify({ text: '' }));
  });
  ```
</CodeBlocks>


## Save the audio to file

Read the incoming message from the WebSocket connection and write the audio chunks to a local file.

<CodeBlocks>
  ```python text-to-speech-websocket.py
  import asyncio

  async def write_to_local(audio_stream):
      """Write the audio encoded in base64 string to a local mp3 file."""

      with open(f'./output/test.mp3', "wb") as f:
          async for chunk in audio_stream:
              if chunk:
                  f.write(chunk)

  async def listen(websocket):
      """Listen to the websocket for audio data and stream it."""

      while True:
          try:
              message = await websocket.recv()
              data = json.loads(message)
              if data.get("audio"):
                  yield base64.b64decode(data["audio"])
              elif data.get('isFinal'):
                  break

          except websockets.exceptions.ConnectionClosed:
              print("Connection closed")
              break

  async def text_to_speech_ws_streaming(voice_id, model_id):
      async with websockets.connect(uri) as websocket:
            ...
            # Add listen task to submit the audio chunks to the write_to_local function
            listen_task = asyncio.create_task(write_to_local(listen(websocket)))

            await listen_task

  asyncio.run(text_to_speech_ws_streaming(voice_id, model_id))
  ```

  ```typescript text-to-speech-websocket.ts
  // Helper function to write the audio encoded in base64 string into local file
  function writeToLocal(base64str: any, writeStream: fs.WriteStream) {
    const audioBuffer: Buffer = Buffer.from(base64str, 'base64');
    writeStream.write(audioBuffer, (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }

  // Listen to the incoming message from the websocket connection
  websocket.on('message', function incoming(event) {
    const data = JSON.parse(event.toString());
    if (data['audio']) {
      writeToLocal(data['audio'], writeStream);
    }
  });

  // Close the writeStream when the websocket connection closes
  websocket.on('close', () => {
    writeStream.end();
  });
  ```
</CodeBlocks>


## Run the script

You can run the script by executing the following command in your terminal. An mp3 audio file will be saved in the `output` directory.

<CodeBlocks>
  ```python Python
  python text-to-speech-websocket.py
  ```

  ```typescript TypeScript
  npx tsx text-to-speech-websocket.ts
  ```
</CodeBlocks>


## Advanced configuration

The use of WebSockets comes with some advanced settings that you can use to fine-tune your real-time audio generation.

### Buffering

When generating real-time audio, two important concepts should be taken into account: Time To First Byte (TTFB) and Buffering. To produce high quality audio and deduce context, the model requires a certain threshold of input text. The more text that is sent in a WebSocket connection, the better the audio quality. If the threshold is not met, the model will add the text to a buffer and generate audio once the buffer is full.

In terms of latency, TTFB is the time it takes for the first byte of audio to be sent to the client. This is important because it affects the perceived latency of the audio. As such, you might want to control the buffer size to balance between quality and latency.

To manage this, you can use the `chunk_length_schedule` parameter when either initializing the WebSocket connection or when sending text. This parameter is an array of integers that represent the number of characters that will be sent to the model before generating audio. For example, if you set `chunk_length_schedule` to `[120, 160, 250, 290]`, the model will generate audio after 120, 160, 250, and 290 characters have been sent, respectively.

Here's an example of how this works with the default settings for `chunk_length_schedule`:

<img src="file:042d6809-07bc-41c7-b426-f161ced7805e" />

In the above diagram, audio is only generated after the second message is sent to the server. This is because the first message is below the threshold of 120 characters, while the second message brings the total number of characters above the threshold. The third message is above the threshold of 160 characters, so audio is immediately generated and returned to the client.

You can specify a custom value for `chunk_length_schedule` when initializing the WebSocket connection or when sending text.

<CodeBlocks>
  ```python
  await websocket.send(json.dumps({
      "text": text,
      "generation_config": {
          # Generate audio after 50, 120, 160, and 290 characters have been sent
          "chunk_length_schedule": [50, 120, 160, 290]
      },
      "xi_api_key": ELEVENLABS_API_KEY,
  }))
  ```

  ```typescript
  websocket.send(
    JSON.stringify({
      text: text,
      // Generate audio after 50, 120, 160, and 290 characters have been sent
      generation_config: { chunk_length_schedule: [50, 120, 160, 290] },
      xi_api_key: ELEVENLABS_API_KEY,
    })
  );
  ```
</CodeBlocks>

In the case that you want force the immediate return of the audio, you can use `flush: true` to clear out the buffer and force generate any buffered text. This can be useful, for example, when you have reached the end of a document and want to generate audio for the final section.

<img src="file:57d15b97-e183-4432-b6bc-9aa081a29d8a" />

This can be specified on a per-message basis by setting `flush: true` in the message.

<CodeBlocks>
  ```python
  await websocket.send(json.dumps({"text": "Generate this audio immediately.", "flush": True}))
  ```

  ```typescript
  websocket.send(JSON.stringify({ text: 'Generate this audio immediately.', flush: true }));
  ```
</CodeBlocks>

In addition, closing the websocket will automatically force generate any buffered text.

### Voice settings

When initializing the WebSocket connections, you can specify the voice settings for the subsequent generations. This allows you to control the speed, stability, and other voice characteristics of the generated audio.

<CodeBlocks>
  ```python
  await websocket.send(json.dumps({
      "text": text,
      "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "use_speaker_boost": False},
  }))
  ```

  ```typescript
  websocket.send(
    JSON.stringify({
      text: text,
      voice_settings: { stability: 0.5, similarity_boost: 0.8, use_speaker_boost: false },
    })
  );
  ```
</CodeBlocks>

This can be overridden on a per-message basis by specifying a different `voice_settings` in the message.

### Pronunciation dictionaries

You can use pronunciation dictionaries to control the pronunciation of specific words or phrases. This can be useful for ensuring that certain words are pronounced correctly or for adding emphasis to certain words or phrases.

Unlike `voice_settings` and `generation_config`, pronunciation dictionaries must be specified in the "Initialize Connection" message. See the [API Reference](/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input#send.Initialize%20Connection.pronunciation_dictionary_locators) for more information.


## Best practice

* We suggest using the default setting for `chunk_length_schedule` in `generation_config`.
* When developing a real-time conversational agent application, we advise using `flush: true` along with the text at the end of conversation turn to ensure timely audio generation.
* If the default setting doesn't provide optimal latency for your use case, you can modify the `chunk_length_schedule`. However, be mindful that reducing latency through this adjustment may come at the expense of quality.


## Tips

* The WebSocket connection will automatically close after 20 seconds of inactivity. To keep the connection open, you can send a single space character `" "`. Please note that this string must include a space, as sending a fully empty string, `""`, will close the WebSocket.
* Send an empty string to close the WebSocket connection after sending the last text message.
* You can use `alignment` to get the word-level timestamps for each word in the text. This can be useful for aligning the audio with the text in a video or for other applications that require precise timing. See the [API Reference](/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input#receive.Audio%20Output.alignment) for more information.



# Error messages

> Explore error messages and solutions.

This guide includes an overview of error messages you might see in the ElevenLabs dashboard & API.


## Dashboard errors

| Error Message                                          | Cause                                                                                                     | Solution                                                                                                                                                        |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The selected model can not be used for text-to-speech. | Occurs when switching between speech-to-speech and text-to-speech if the model does not switch correctly. | Select the desired model. If unresolved, select a different model, then switch back.                                                                            |
| Oops, something went wrong.                            | Indicates a client-side error, often due to device or browser issues.                                     | Click “Try again” or refresh the page. If unresolved, clear browser cache and cookies. Temporarily pause browser-based translation tools like Google Translate. |

<Note>
  If error messages persist after following these solutions, please [contact our support
  team](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937) for further
  assistance.
</Note>


## API errors

### Code 400/401

| Code                                   | Overview                                                                                                                                                                                                    |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| max\_character\_limit\_exceeded <br /> | **Cause:** You are sending too many characters in a single request. <br /> **Solution:** Split the request into smaller chunks, see [character limits](/docs/models#character-limits) for more information. |
| invalid\_api\_key                      | **Cause:** You have not set your API key correctly. <br /> **Solution:** Ensure the request is correctly authenticated. See [authentication](/docs/api-reference/authentication) for more information.      |
| quota\_exceeded                        | **Cause:** You have insufficient quota to complete the request. <br /> **Solution:** On the Creator plan and above, you can enable usage-based billing from your Subscription page.                         |
| voice\_not\_found                      | **Cause:** You have entered the incorrect voice\_id. <br /> **Solution:** Check that you are using the correct voice\_id for the voice you want to use. You can verify this in My Voices.                   |

### Code 403

| Code                | Overview                                                                                                                                                                    |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| only\_for\_creator+ | **Cause:** You are trying to use professional voices on a free or basic subscription. <br /> **Solution:** Upgrade to Creator tier or higher to access professional voices. |

### Code 429

| Code                                   | Overview                                                                                                                                                                                                                                                                               |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| too\_many\_concurrent\_requests <br /> | **Cause:** You have exceeded the concurrency limit for your subscription. <br /> **Solution:** See [concurrency limits and priority](/docs/models#concurrency-and-priority) for more information.                                                                                      |
| system\_busy                           | **Cause:** Our services are experiencing high levels of traffic and your request could not be processed. <br /> **Solution:** Retry the request later, with exponential backoff. Consider upgrading your subscription to get [higher priority](/docs/models#concurrency-and-priority). |

<Note>
  If error messages persist after following these solutions, please [contact our support
  team](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937) for further
  assistance.
</Note>



---
**Navigation:** [← Previous](./05-find-create-an-api-key-at-httpselevenlabsioappsett.md) | [Index](./index.md) | [Next →](./07-migrate-from-playht-to-elevenlabs.md)
