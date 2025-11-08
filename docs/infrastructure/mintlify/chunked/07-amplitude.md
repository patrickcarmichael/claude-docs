**Navigation:** [← Previous](./06-vercel.md) | [Index](./index.md) | [Next →](./08-pdf-exports.md)

# Amplitude
Source: https://mintlify.com/docs/integrations/analytics/amplitude



Add the following to your `docs.json` file to send analytics to Amplitude.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "amplitude": {
          "apiKey": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "amplitude": {
          "apiKey": "76bb138bf3fbf58186XXX00000"
      }
  }
  ```
</CodeGroup>



# Clearbit
Source: https://mintlify.com/docs/integrations/analytics/clearbit



Add the following to your `docs.json` file to send analytics to Clearbit.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "clearbit": {
          "publicApiKey": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "clearbit": {
          "publicApiKey": "pk_1a1882"
      }
  }
  ```
</CodeGroup>



# Fathom
Source: https://mintlify.com/docs/integrations/analytics/fathom



Add the following to your `docs.json` file to send analytics to Fathom.

You can get the `siteId` from your script settings.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "fathom": {
          "siteId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "fathom": {
          "siteId": "YSVMSDAY"
      }
  }
  ```
</CodeGroup>



# Google Analytics 4
Source: https://mintlify.com/docs/integrations/analytics/google-analytics



You will need to generate a new <Tooltip tip="Google Analytics 4">GA4</Tooltip> property to use with Mintlify. The data collected will go into the same project as your other Google Analytics data.

If you are using the old version of Google Analytics, Universal Analytics, you will still be able to generate a <Tooltip tip="Google Analytics 4">GA4</Tooltip> property. <Tooltip tip="Google Analytics 4">GA4</Tooltip> data is slightly different from UA data but still gets collected in the same project.


## How to Connect GA4 to Mintlify

### Create a Web Stream

You will need to create a web stream to get the Measurement ID to put into Mintlify.

Click the cog at the bottom left of the Google Analytics screen. Then click on Data Streams.

<Frame><img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3da279b4cbc0f73f3f08e72fa8502b94" alt="Screenshot of the Data Streams page in the Google Analytics dashboard." data-og-width="1400" width="1400" data-og-height="504" height="504" data-path="images/ga4-web-streams.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7ef49476940b7d4fd7d146791a4b67aa 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=be528e9ba15115da76755acdb8106656 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6363c4eb9dc282f60d241327b88a76ba 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e491f72d68f54f2bbeb45e68a1d2c1ce 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=8b3c1dfd2b710c90aef89235918aee2f 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c0786ce67ebb7710d8d1b443269ed279 2500w" /></Frame>

Create a Web Stream and put the URL of your Mintlify docs site as the stream URL.

Your Measurement ID looks like `G-XXXXXXX` and will show up under Stream Details immediately after you create the Web Stream.

### Put Measurement ID in docs.json

Add your Measurement ID to your `docs.json` file like so:

```json docs.json theme={null}
"integrations": {
    "ga4": {
        "measurementId": "G-XXXXXXX"
    }
}
```

### Wait

Google Analytics takes two to three days to show your data.

You can use the [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna?hl=en) to check analytics are enabled correctly. The extension will log to your browser's console every time GA4 makes a request.

<Note>
  Preview links have analytics turned off.
</Note>



# Google Tag Manager
Source: https://mintlify.com/docs/integrations/analytics/google-tag-manager



Add your tag ID to `docs.json` file and we'll inject the Google Tag Manager script to all your pages.

You are responsible for setting up cookie consent banners with Google Tag Manager if you need them.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "gtm": {
          "tagId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "gtm": {
          "tagId": "GTM-MGBL4PW"
      }
  }
  ```
</CodeGroup>



# Heap
Source: https://mintlify.com/docs/integrations/analytics/heap



Add the following to your `docs.json` file to send analytics to Heap.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "heap": {
          "appId": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "heap": {
          "appId": "1234567890"
      }
  }
  ```
</CodeGroup>



# Hightouch
Source: https://mintlify.com/docs/integrations/analytics/hightouch



Add the following to your `docs.json` file to send analytics to Hightouch.

<Info>
  Do not include `https://` for the `apiHost`.
</Info>

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "hightouch": {
          "writeKey": "required"
          "apiHost": "optional"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "hightouch": {
          "writeKey": "9132c81do371p76sr11da0075469b54f77649c9a067dp0303p56q0q64n072336"
          "apiHost": "us-east-1.hightouch-events.com" # optional, defaults to `us-east-1.hightouch-events.com`
      }
  }
  ```
</CodeGroup>



# HotJar
Source: https://mintlify.com/docs/integrations/analytics/hotjar



Add the following to your `docs.json` file to send analytics to HotJar.

```json Analytics options in docs.json theme={null}
"integrations": {
    "hotjar": {
        "hjid": "required",
        "hjsv": "required"
    }
}
```



# LogRocket
Source: https://mintlify.com/docs/integrations/analytics/logrocket



Add the following to your `docs.json` file to send analytics to LogRocket.

```json Analytics options in docs.json theme={null}
"integrations": {
    "logrocket": {
        "apiKey": "required"
    }
}
```



# Mixpanel
Source: https://mintlify.com/docs/integrations/analytics/mixpanel



Add the following to your `docs.json` file to send analytics to Mixpanel.

```json Analytics options in docs.json theme={null}
"integrations": {
    "mixpanel": {
        "projectToken": "required"
    }
}
```



# Analytics integrations
Source: https://mintlify.com/docs/integrations/analytics/overview

Integrate with an analytics platform to track events

Automatically send data about your documentation engagement to your third party analytics provider.


## All integrations

<CardGroup cols={2}>
  <Card
    title="Amplitude"
    href="/integrations/analytics/amplitude"
    horizontal
    icon={<svg className="h-6 w-6" width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M15.5988 8.04494C15.4989 7.91714 15.3924 7.84668 15.2646 7.84668C15.1728 7.85323 15.0876 7.88273 15.009 7.93188C14.0635 8.67087 12.7773 11.8055 11.7188 15.9412L12.6576 15.9477C14.5059 15.969 16.4165 15.9903 18.3008 16.0182C17.8027 14.1273 17.3341 12.5068 16.9015 11.1926C16.2674 9.28205 15.8414 8.42181 15.5988 8.04494Z" fill="#1E61F0"/>
<path d="M17.6964 0.078125C7.92405 0.078125 0 8.00217 0 17.7745C0 27.5468 7.92405 35.4709 17.6964 35.4709C27.4687 35.4709 35.3928 27.5468 35.3928 17.7745C35.3928 8.00217 27.4687 0.078125 17.6964 0.078125ZM30.7589 17.5615C30.7098 17.7598 30.5885 17.9531 30.4181 18.094C30.3968 18.1088 30.3755 18.1219 30.3542 18.1366L30.3329 18.1514L30.2903 18.1792L30.2543 18.2005C30.1199 18.271 29.9692 18.307 29.8135 18.307H21.4274C21.4913 18.584 21.5699 18.9035 21.6469 19.2459C22.109 21.2286 23.3248 26.5014 24.6242 26.5014H24.652H24.6668H24.6946C25.704 26.5014 26.2234 25.0382 27.3606 21.8316L27.3753 21.7955C27.5605 21.2843 27.7669 20.701 27.9865 20.0832L28.0439 19.9276C28.1291 19.7211 28.3634 19.6146 28.5698 19.6998C28.7189 19.7572 28.8254 19.9063 28.8254 20.0701C28.8254 20.1127 28.8189 20.1488 28.8107 20.1832L28.7615 20.3388C28.6403 20.7223 28.5207 21.2417 28.3699 21.8463C27.6948 24.6466 26.6707 28.8757 24.0556 28.8757H24.0343C22.3433 28.861 21.334 26.1606 20.8998 25.0022C20.0903 22.8409 19.4791 20.5453 18.8893 18.3152H11.1864L9.58718 23.439L9.56588 23.4177C9.32501 23.7946 8.82034 23.9076 8.44347 23.6668C8.20916 23.5176 8.0666 23.262 8.0666 22.9851V22.9573L8.16655 22.3739C8.38612 21.0598 8.65648 19.6867 8.9547 18.3087H5.68578L5.67104 18.2939C5.00251 18.194 4.54043 17.5697 4.64039 16.9012C4.71904 16.3817 5.1172 15.9705 5.62843 15.8771C5.75624 15.8623 5.88405 15.8558 6.01186 15.8623H6.16752C7.19817 15.8771 8.29272 15.8984 9.50034 15.9115C11.1995 9.00333 13.1674 5.49191 15.3565 5.48535C17.7013 5.48535 19.4431 10.8221 20.8359 16.0458L20.8424 16.0671C23.7 16.1245 26.756 16.2097 29.7185 16.4227L29.8463 16.4374C29.8954 16.4374 29.938 16.444 29.9888 16.4522H30.0036L30.0183 16.4588H30.0249C30.5312 16.5587 30.8654 17.0568 30.7589 17.5615Z" fill="#1E61F0"/>
</svg>}
  />

  <Card
    title="Mixpanel"
    href="/integrations/analytics/mixpanel"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    style={{ fill: "#7856ff" }}
    viewBox="0 0 98 98"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M24.2391 58.7912C29.877 58.7912 34.4475 54.2207 34.4475 48.5828C34.4475 42.9449 29.877 38.3745 24.2391 38.3745C18.6012 38.3745 14.0308 42.9449 14.0308 48.5828C14.0308 54.2207 18.6012 58.7912 24.2391 58.7912Z"></path>
    <path d="M54.7787 55.7046C58.7675 55.7046 62.0011 52.4716 62.0011 48.4834C62.0011 44.4952 58.7675 41.2622 54.7787 41.2622C50.7899 41.2622 47.5563 44.4952 47.5563 48.4834C47.5563 52.4716 50.7899 55.7046 54.7787 55.7046Z"></path>
    <path d="M78.6018 52.0652C80.547 52.0652 82.1239 50.4883 82.1239 48.5431C82.1239 46.5979 80.547 45.021 78.6018 45.021C76.6566 45.021 75.0798 46.5979 75.0798 48.5431C75.0798 50.4883 76.6566 52.0652 78.6018 52.0652Z"></path>
  </svg>
}
  />

  <Card
    title="PostHog"
    href="/integrations/analytics/posthog"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    width="50"
    height="30"
    viewBox="0 0 50 30"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M10.8914 17.2057c-.3685.7371-1.42031.7371-1.78884 0L8.2212 15.443c-.14077-.2815-.14077-.6129 0-.8944l.88136-1.7627c.36853-.7371 1.42034-.7371 1.78884 0l.8814 1.7627c.1407.2815.1407.6129 0 .8944l-.8814 1.7627zM10.8914 27.2028c-.3685.737-1.42031.737-1.78884 0L8.2212 25.44c-.14077-.2815-.14077-.6129 0-.8944l.88136-1.7627c.36853-.7371 1.42034-.7371 1.78884 0l.8814 1.7627c.1407.2815.1407.6129 0 .8944l-.8814 1.7628z"
      fill="#1D4AFF"
    />
    <path
      d="M0 23.4082c0-.8909 1.07714-1.3371 1.70711-.7071l4.58338 4.5834c.62997.63.1838 1.7071-.7071 1.7071H.999999c-.552284 0-.999999-.4477-.999999-1v-4.5834zm0-4.8278c0 .2652.105357.5196.292893.7071l9.411217 9.4112c.18753.1875.44189.2929.70709.2929h5.1692c.8909 0 1.3371-1.0771.7071-1.7071L1.70711 12.7041C1.07714 12.0741 0 12.5203 0 13.4112v5.1692zm0-9.99701c0 .26521.105357.51957.292893.7071L19.7011 28.6987c.1875.1875.4419.2929.7071.2929h5.1692c.8909 0 1.3371-1.0771.7071-1.7071L1.70711 2.70711C1.07715 2.07715 0 2.52331 0 3.41421v5.16918zm9.997 0c0 .26521.1054.51957.2929.7071l17.994 17.99401c.63.63 1.7071.1838 1.7071-.7071v-5.1692c0-.2652-.1054-.5196-.2929-.7071l-17.994-17.994c-.63-.62996-1.7071-.18379-1.7071.70711v5.16918zm11.7041-5.87628c-.63-.62997-1.7071-.1838-1.7071.7071v5.16918c0 .26521.1054.51957.2929.7071l7.997 7.99701c.63.63 1.7071.1838 1.7071-.7071v-5.1692c0-.2652-.1054-.5196-.2929-.7071l-7.997-7.99699z"
      fill="#F9BD2B"
    />
    <path
      d="M42.5248 23.5308l-9.4127-9.4127c-.63-.63-1.7071-.1838-1.7071.7071v13.1664c0 .5523.4477 1 1 1h14.5806c.5523 0 1-.4477 1-1v-1.199c0-.5523-.4496-.9934-.9973-1.0647-1.6807-.2188-3.2528-.9864-4.4635-2.1971zm-6.3213 2.2618c-.8829 0-1.5995-.7166-1.5995-1.5996 0-.8829.7166-1.5995 1.5995-1.5995.883 0 1.5996.7166 1.5996 1.5995 0 .883-.7166 1.5996-1.5996 1.5996z"
      fill="#000"
    />
    <path
      d="M0 27.9916c0 .5523.447715 1 1 1h4.58339c.8909 0 1.33707-1.0771.70711-1.7071l-4.58339-4.5834C1.07714 22.0711 0 22.5173 0 23.4082v4.5834zM9.997 10.997L1.70711 2.70711C1.07714 2.07714 0 2.52331 0 3.41421v5.16918c0 .26521.105357.51957.292893.7071L9.997 18.9946V10.997zM1.70711 12.7041C1.07714 12.0741 0 12.5203 0 13.4112v5.1692c0 .2652.105357.5196.292893.7071L9.997 28.9916V20.994l-8.28989-8.2899z"
      fill="#1D4AFF"
    />
    <path
      d="M19.994 11.4112c0-.2652-.1053-.5196-.2929-.7071l-7.997-7.99699c-.6299-.62997-1.70709-.1838-1.70709.7071v5.16918c0 .26521.10539.51957.29289.7071l9.7041 9.70411v-7.5834zM9.99701 28.9916h5.58339c.8909 0 1.3371-1.0771.7071-1.7071L9.99701 20.994v7.9976zM9.99701 10.997v7.5834c0 .2652.10539.5196.29289.7071l9.7041 9.7041v-7.5834c0-.2652-.1053-.5196-.2929-.7071L9.99701 10.997z"
      fill="#F54E00"
    />
  </svg>
}
  />

  <Card
    title="Google Analytics 4"
    href="/integrations/analytics/google-analytics"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    xmlns="http://www.w3.org/2000/svg"
    width="64"
    height="64"
    viewBox="0 0 64 64"
  >
    <g transform="matrix(.363638 0 0 .363636 -3.272763 -2.909091)">
      <path
        d="M130 29v132c0 14.77 10.2 23 21 23 10 0 21-7 21-23V30c0-13.54-10-22-21-22s-21 9.33-21 21z"
        fill="#f9ab00"
      />
      <g fill="#e37400">
        <path d="M75 96v65c0 14.77 10.2 23 21 23 10 0 21-7 21-23V97c0-13.54-10-22-21-22s-21 9.33-21 21z" />
        <circle cx="41" cy="163" r="21" />
      </g>
    </g>
  </svg>
}
  />

  <Card
    title="Google Tag Manager"
    href="/integrations/analytics/google-tag-manager"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    x="0px"
    y="0px"
    width="192px"
    height="192px"
    viewBox="0 0 192 192"
    enableBackground="new 0 0 192 192"
  >
    <rect fill="none" width="192" height="192" />
    <g>
      <polygon
        fill="#8AB4F8"
        points="111.31,176.79 80.76,147 146.37,80 178,111 	"
      />
      <path
        fill="#4285F4"
        d="M111.44,45.08L81,14L14.44,79.93c-8.58,8.58-8.58,22.49,0,31.08L80,177l31-29L61.05,95.47L111.44,45.08z"
      />
      <path
        fill="#8AB4F8"
        d="M177.56,80.44l-66-66c-8.59-8.59-22.52-8.59-31.11,0c-8.59,8.59-8.59,22.52,0,31.11l66,66
  c8.59,8.59,22.52,8.59,31.11,0C186.15,102.96,186.15,89.03,177.56,80.44z"
      />
      <circle fill="#246FDB" cx="95.5" cy="162.5" r="21.5" />
    </g>
  </svg>
}
  />

  <Card
    title="Hightouch"
    href="/integrations/analytics/hightouch"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    xmlns="http://www.w3.org/2000/svg"
    width="97"
    height="97"
    viewBox="0 0 97 97"
    fill="none"
  >
    <path
      d="M33 3.75C33 2.7835 33.7835 2 34.75 2H93.25C94.2165 2 95 2.7835 95 3.75V62.25C95 63.2165 94.2165 64 93.25 64H33V3.75Z"
      className="fill-black dark:fill-white"
    />
    <path
      d="M33 93.25C33 94.2165 32.2165 95 31.25 95L3.75 95C2.7835 95 2 94.2165 2 93.25L2 65.75C2 64.7835 2.7835 64 3.75 64L33 64L33 93.25Z"
      className="fill-black dark:fill-white"
    />
  </svg>
}
  />

  <Card
    title="HotJar"
    href="/integrations/analytics/hotjar"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    width="51"
    height="57"
    viewBox="0 0 51 57"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M20.9743 23.3016C27.5805 19.6488 36.6281 14.645 36.6281 0.0820312H25.6725C25.6725 8.23006 21.687 10.4338 15.6538 13.7698C9.0477 17.4239 0 22.4256 0 36.99H10.9556C10.9556 28.8414 14.9412 26.6376 20.9743 23.3016Z"
      fill="#FF3C00"
    />
    <path
      d="M39.9362 19.9551C39.9362 28.1035 35.9506 30.3073 29.9175 33.6428C23.3131 37.2956 14.2637 42.2987 14.2637 56.8628H25.2189C25.2189 48.7143 29.2044 46.5106 35.2375 43.1746C41.8436 39.5218 50.8909 34.5193 50.8909 19.9551H39.9362Z"
      fill="#FF3C00"
    />
  </svg>
}
  />

  <Card
    title="LogRocket"
    href="/integrations/analytics/logrocket"
    horizontal
    icon={
  <svg
    className="h-7 w-5"
    width="102"
    height="159"
    viewBox="0 0 102 159"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M33.7001 18.4998C38.1001 11.4998 44.0001 5.3998 50.9001 0.799805C57.7001 5.2998 63.5001 11.2998 67.9001 18.1998C79.4001 34.1998 85.2001 53.4998 84.4001 73.1998C88.0001 76.0998 91.7001 78.8998 95.2001 81.7998C100.2 86.2998 102.6 93.0998 101.4 99.6998C99.7001 107.9 98.1001 116.1 96.3001 124.3C95.1001 127.9 91.2001 129.8 87.7001 128.6C87.1001 128.4 86.5001 128.1 86.0001 127.7C80.2001 123.1 74.6001 118.3 68.8001 113.6C58.9001 123 43.5001 123.1 33.5001 113.8C29.4001 116.8 25.5001 120.5 21.5001 123.8C19.7001 125.5 17.8001 127.1 15.6001 128.3C12.1001 129.7 8.10011 127.9 6.80011 124.4C6.70011 124.2 6.7001 124 6.6001 123.9C4.8001 115.9 2.8001 107.9 1.0001 99.8998C-0.399898 92.8998 2.1001 85.7998 7.5001 81.1998C10.6001 78.6998 13.8001 76.1998 17.0001 73.6998C17.9001 73.1998 17.4001 72.1998 17.5001 71.4998C17.1001 52.5998 22.8001 33.9998 33.7001 18.4998ZM39.4001 43.2998C35.2001 48.6998 35.7001 56.3998 40.6001 61.1998C46.2001 66.5998 55.1001 66.7998 60.9001 61.5998C65.0001 57.8998 66.4001 51.9998 64.5001 46.7998C62.5001 41.7998 57.9001 38.2998 52.5001 37.8998C47.4001 37.2998 42.5001 39.3998 39.4001 43.2998Z"
      fill="#764ABC"
    />
    <path
      d="M31.7002 130.6C31.8002 128.7 33.5002 127.3 35.3002 127.5C35.8002 127.5 36.3002 127.7 36.7002 127.9C45.6002 132.2 56.0002 132.2 65.0002 127.9C66.7002 127 68.7002 127.7 69.6002 129.3C69.8002 129.6 69.9002 130 70.0002 130.4C70.0002 135.4 70.0002 140.4 70.0002 145.4C69.8002 147.2 68.1002 148.6 66.3002 148.4C65.7002 148.3 65.2002 148.1 64.7002 147.8C63.2002 146.5 61.9002 145.1 60.4002 143.8C58.1002 148.1 56.0002 152.4 53.7002 156.7C52.7002 158.3 50.6002 158.7 49.0002 157.7C48.6002 157.5 48.3002 157.1 48.1002 156.8C45.8002 152.5 43.7002 148.2 41.3002 143.9C39.9002 145.3 38.5002 146.7 37.0002 147.9C35.5002 149 33.3002 148.6 32.3002 147C32.0002 146.5 31.8002 146 31.7002 145.4C31.7002 140.5 31.7002 135.5 31.7002 130.6Z"
      fill="#764ABC"
    />
    <path
      d="M50.7998 58.5005C54.5998 58.6005 57.6998 55.6005 57.7998 51.8005C57.6998 48.0005 54.5998 45.0005 50.7998 45.0005C46.9998 44.9005 43.8998 47.9005 43.7998 51.7005C43.7998 55.5005 46.9998 58.6005 50.7998 58.5005Z"
      fill="#764ABC"
    />
  </svg>
}
  />

  <Card
    title="Pirsch"
    href="/integrations/analytics/pirsch"
    horizontal
    icon={
  <>
    <svg
      className="h-6 w-6 dark:hidden"
      width="1"
      height="1"
      viewBox="0 0 1 1"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g clipPath="url(#clip0_2199_68)">
        <path
          d="M0.184082 0.631579C0.358477 0.631579 0.499871 0.490184 0.499871 0.315789C0.499871 0.141395 0.358477 0 0.184082 0V0.631579ZM0.815661 0.368421C0.641266 0.368421 0.499871 0.509816 0.499871 0.684211C0.499871 0.858605 0.641266 1 0.815661 1V0.368421Z"
          fill="black"
        />
        <path
          d="M0.710681 0.288549C0.78335 0.288549 0.842259 0.229639 0.842259 0.15697C0.842259 0.0843005 0.78335 0.0253906 0.710681 0.0253906C0.638011 0.0253906 0.579102 0.0843005 0.579102 0.15697C0.579102 0.229639 0.638011 0.288549 0.710681 0.288549Z"
          fill="black"
        />
        <path
          d="M0.289294 0.974095C0.361963 0.974095 0.420873 0.915185 0.420873 0.842516C0.420873 0.769847 0.361963 0.710938 0.289294 0.710938C0.216625 0.710938 0.157715 0.769847 0.157715 0.842516C0.157715 0.915185 0.216625 0.974095 0.289294 0.974095Z"
          fill="black"
        />
      </g>
      <defs>
        <clipPath id="clip0_2199_68">
          <rect width="1" height="1" fill="black" />
        </clipPath>
      </defs>
    </svg>
    <svg
      className="hidden h-6 w-6 dark:block"
      width="1"
      height="1"
      viewBox="0 0 1 1"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g clipPath="url(#clip0_2199_68)">
        <path
          d="M0.184082 0.631579C0.358477 0.631579 0.499871 0.490184 0.499871 0.315789C0.499871 0.141395 0.358477 0 0.184082 0V0.631579ZM0.815661 0.368421C0.641266 0.368421 0.499871 0.509816 0.499871 0.684211C0.499871 0.858605 0.641266 1 0.815661 1V0.368421Z"
          fill="white"
        />
        <path
          d="M0.710681 0.288549C0.78335 0.288549 0.842259 0.229639 0.842259 0.15697C0.842259 0.0843005 0.78335 0.0253906 0.710681 0.0253906C0.638011 0.0253906 0.579102 0.0843005 0.579102 0.15697C0.579102 0.229639 0.638011 0.288549 0.710681 0.288549Z"
          fill="white"
        />
        <path
          d="M0.289294 0.974095C0.361963 0.974095 0.420873 0.915185 0.420873 0.842516C0.420873 0.769847 0.361963 0.710938 0.289294 0.710938C0.216625 0.710938 0.157715 0.769847 0.157715 0.842516C0.157715 0.915185 0.216625 0.974095 0.289294 0.974095Z"
          fill="white"
        />
      </g>
      <defs>
        <clipPath id="clip0_2199_68">
          <rect width="1" height="1" fill="white" />
        </clipPath>
      </defs>
    </svg>
  </>
}
  />

  <Card
    title="Plausible"
    href="/integrations/analytics/plausible"
    horizontal
    icon={
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="1000px"
    height="1000px"
    className="h-6 w-6"
    viewBox="0 0 1000 1000"
  >
    <defs>
      <radialGradient
        cx="79.1305263%"
        cy="87.6448158%"
        fx="79.1305263%"
        fy="87.6448158%"
        r="96.9897763%"
        id="radialGradient-1"
      >
        <stop stopColor="#2440E6" offset="0%" />
        <stop stopColor="#5661B3" offset="100%" />
      </radialGradient>
      <radialGradient
        cx="0%"
        cy="30.2198829%"
        fx="0%"
        fy="30.2198829%"
        r="62.2688936%"
        gradientTransform="translate(0.000000,0.302199),scale(1.000000,0.722519),rotate(61.734530),translate(-0.000000,-0.302199)"
        id="radialGradient-2"
      >
        <stop stopColor="#6574CD" stopOpacity="0.5" offset="0%" />
        <stop stopColor="#6574CD" offset="100%" />
      </radialGradient>
    </defs>
    <g stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
      <g transform="translate(19.000000, 0.000000)">
        <g transform="translate(-19.000000, 0.000000)">
          <rect x="0" y="0" width="1000" height="1000" />
          <g transform="translate(124.069479, 0.000000)">
            <g transform="translate(376.923077, 500.000000) scale(-1, 1) rotate(-180.000000) translate(-376.923077, -500.000000) translate(2.233251, -0.000000)">
              <circle
                fill="url(#radialGradient-1)"
                cx="373.69727"
                cy="624.069479"
                r="373.449132"
              />
              <path
                d="M309.677419,993.322174 C232.506203,979.92267 167.493797,947.168328 113.647643,894.562869 C58.3126551,840.468576 24.0694789,777.44128 7.44416873,698.781231 L1.7369727,671.982223 L0.992555831,336.498352 L0.248138958,0.76634245 L7.19602978,0.76634245 C11.1662531,0.76634245 23.82134,2.00703724 35.235732,3.24773203 C132.754342,15.158402 215.632754,74.215474 260.794045,163.793638 C272.208437,186.622422 280.397022,212.925151 286.104218,245.679494 C290.818859,273.471057 291.066998,282.652199 290.322581,427.56535 L289.578164,580.170809 L295.533499,595.059146 C303.722084,615.406541 326.30273,637.987186 346.650124,646.175772 L361.538462,652.131107 L500.496278,652.379246 C576.923077,652.379246 643.920596,653.371802 649.131514,654.364357 C673.449132,659.078998 699.503722,679.426392 709.925558,702.007037 C712.903226,708.210511 716.873449,720.36932 718.610422,728.557906 C721.33995,742.205548 721.091811,745.927633 717.121588,761.312248 C704.71464,806.969816 661.042184,870.245251 616.377171,907.217955 C565.756824,949.153439 509.925558,977.193141 449.627792,991.337062 C417.866005,998.533092 345.905707,999.773787 309.677419,993.322174 Z"
                id="Path"
                fill="url(#radialGradient-2)"
                fillRule="nonzero"
              />
            </g>
          </g>
        </g>
      </g>
    </g>
  </svg>
}
  />

  <Card
    title="Fathom"
    href="/integrations/analytics/fathom"
    horizontal
    icon={
<svg
className="h-6 w-6"
width="256"
height="256"
viewBox="0 0 256 256"
fill="none"
xmlns="http://www.w3.org/2000/svg"
>
<path
d="M50.4139 36.0859H40.3871C31.7927 36.105 22.7513 37.7857 15.3869 42.8984C11.5551 45.5505 8.45289 49.125 6.36656 53.292C4.0486 58.1293 2.89794 63.4429 3.0071 68.8058V212.667C3.0071 213.984 3.53027 215.247 4.46151 216.178C5.39275 217.109 6.65579 217.632 7.97276 217.632H27.5661C28.8831 217.632 30.1461 217.109 31.0774 216.178C32.0086 215.247 32.5318 213.984 32.5318 212.667V111.31H50.4063C51.0584 111.31 51.7041 111.182 52.3065 110.932C52.909 110.682 53.4564 110.317 53.9175 109.856C54.3786 109.394 54.7444 108.847 54.9939 108.245C55.2435 107.642 55.3719 106.996 55.3719 106.344V89.5566C55.3719 88.2396 54.8488 86.9766 53.9175 86.0453C52.9863 85.1141 51.7232 84.5909 50.4063 84.5909H32.5394V71.8349C32.4457 69.708 32.7382 67.5817 33.4027 65.5591C33.6012 64.974 33.9349 64.444 34.3767 64.0121C35.0566 63.4655 35.8835 63.1331 36.7526 63.0571C38.4628 62.845 40.1867 62.7639 41.9092 62.8146H50.4196C51.7366 62.8146 52.9996 62.2914 53.9309 61.3602C54.8621 60.4289 55.3853 59.1659 55.3853 57.8489V41.0592C55.3853 39.7423 54.8621 38.4792 53.9309 37.548C52.9996 36.6167 51.7366 36.0936 50.4196 36.0936"
className="fill-black dark:fill-white"
/>
<path
d="M168.815 128.261C168.982 122.018 167.781 115.814 165.296 110.084C162.812 104.354 159.105 99.2374 154.434 95.0918C145.198 87.0379 132.23 82.712 116.98 82.7178C101.466 82.7178 88.0641 87.1582 78.2799 94.9409C73.4171 98.7218 69.4331 103.513 66.6032 108.985C63.7733 114.456 62.165 120.476 61.8894 126.63C61.8575 127.301 61.9625 127.972 62.1977 128.602C62.433 129.232 62.7937 129.807 63.258 130.294C63.7223 130.78 64.2806 131.167 64.8989 131.431C65.5172 131.695 66.1827 131.831 66.855 131.83H87.6019C88.8467 131.832 90.0466 131.366 90.9642 130.525C91.8817 129.684 92.4499 128.529 92.5561 127.288C92.7767 124.972 93.4898 122.729 94.6475 120.71C95.8053 118.691 97.3811 116.943 99.2693 115.583C104.448 111.964 110.667 110.136 116.98 110.378C124.718 110.378 130.282 112.479 133.83 115.564C135.624 117.142 137.044 119.1 137.987 121.296C138.93 123.491 139.372 125.869 139.281 128.257V128.958C139.296 129.537 139.232 130.115 139.09 130.677L138.899 131.106C138.545 131.474 138.1 131.743 137.61 131.885C134.826 132.791 131.95 133.381 129.035 133.644C124.833 134.202 119.373 134.779 112.57 135.69H112.581C100.098 137.369 87.3498 139.41 77.0193 145.239C71.7347 148.136 67.3067 152.375 64.1812 157.527C60.8001 163.529 59.1166 170.338 59.311 177.224C59.2225 183.496 60.4876 189.713 63.02 195.452C66.6423 203.293 72.8442 209.656 80.5908 213.477C88.8782 217.474 97.9927 219.456 107.191 219.262C119.128 219.274 128.181 216.497 134.846 212.251C136.408 211.261 137.892 210.155 139.287 208.941V212.66C139.287 213.977 139.81 215.24 140.741 216.171C141.672 217.102 142.936 217.625 144.253 217.625H153.79L168.812 161.735L168.815 128.261ZM139.283 166.03C139.404 169.288 138.883 172.539 137.748 175.596C136.613 178.652 134.887 181.456 132.669 183.845C128.204 188.349 121.149 191.569 109.984 191.601C102.793 191.613 97.4741 190.033 94.2941 187.753C92.8266 186.744 91.6254 185.395 90.7933 183.821C89.9498 182.118 89.5217 180.241 89.5443 178.341V178.293V178.213C89.4842 176.061 90.0395 173.937 91.1447 172.09C93.1437 169.263 95.9722 167.127 99.2388 165.979C103.667 164.269 108.293 163.122 113.007 162.564C120.085 161.569 127.367 160.514 133.404 159.317C135.561 158.895 137.482 158.442 139.289 157.969L139.283 166.03Z"
className="fill-black dark:fill-white"
/>
<path
d="M251.975 21.9481C251.51 21.3425 250.913 20.8518 250.228 20.514C249.544 20.1763 248.791 20.0004 248.027 20H223.077C221.982 19.9988 220.917 20.3596 220.048 21.0263C219.18 21.6929 218.556 22.628 218.273 23.6861L168.813 207.74L166.375 216.833L163.015 229.322C162.816 230.059 162.789 230.832 162.937 231.581C163.085 232.33 163.404 233.035 163.868 233.641C164.333 234.247 164.931 234.737 165.616 235.074C166.301 235.411 167.055 235.586 167.818 235.584H192.769C193.863 235.586 194.927 235.226 195.796 234.56C196.665 233.895 197.289 232.961 197.572 231.904L252.831 26.2644C253.027 25.5271 253.053 24.7545 252.904 24.0059C252.756 23.2573 252.438 22.5527 251.975 21.9462"
fill="#7166F6"
/>
</svg>

}
  />

  <Card
    title="Clearbit"
    href="/integrations/analytics/clearbit"
    horizontal
    icon={
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="36"
    height="36"
    className="h-6 w-6"
    viewBox="0 0 40 40"
  >
    <defs>
      <linearGradient id="clearbit-a" x1="50%" x2="100%" y1="0%" y2="100%">
        <stop offset="0%" stopColor="#DEF2FE"></stop>
        <stop offset="100%" stopColor="#DBF1FE"></stop>
      </linearGradient>
      <linearGradient id="clearbit-b" x1="0%" x2="50%" y1="0%" y2="100%">
        <stop offset="0%" stopColor="#57BCFD"></stop>
        <stop offset="100%" stopColor="#51B5FD"></stop>
      </linearGradient>
      <linearGradient id="clearbit-c" x1="37.5%" x2="62.5%" y1="0%" y2="100%">
        <stop offset="0%" stopColor="#1CA7FD"></stop>
        <stop offset="100%" stopColor="#148CFC"></stop>
      </linearGradient>
      <filter
        id="ck-icon-shadow"
        x="-50%"
        y="-50%"
        width="200%"
        height="200%"
      >
        <feOffset result="offOut" in="SourceGraphic" dx="0" dy="1"></feOffset>
        <feGaussianBlur
          result="blurOut"
          in="offOut"
          stdDeviation="1"
        ></feGaussianBlur>
        <feBlend in="SourceGraphic" in2="blurOut" mode="normal"></feBlend>
      </filter>
    </defs>
    <g fill="none">
      <path
        d="M27.9195733,37 L12.0804267,37 L11.4338943,36.9949826 C8.75934941,36.9515623 7.69554096,36.6271471 6.62367147,36.053905 C5.46935048,35.4365674 4.56343261,34.5306495 3.94609499,33.3763285 L3.81824005,33.1283803 C3.30403747,32.0897188 3.02217708,30.9433817 3.00125617,28.250264 L3,12.0804267 C3,8.92296455 3.32875737,7.77799245 3.94609499,6.62367147 C4.56343261,5.46935048 5.46935048,4.56343261 6.62367147,3.94609499 L6.87161969,3.81824005 C7.91028124,3.30403747 9.05661831,3.02217708 11.749736,3.00125617 L27.9195733,3 C31.0770355,3 32.2220075,3.32875737 33.3763285,3.94609499 C34.5306495,4.56343261 35.4365674,5.46935048 36.053905,6.62367147 L36.18176,6.87161969 C36.6959625,7.91028124 36.9778229,9.05661831 36.9987438,11.749736 L37,27.9195733 L36.9949826,28.5661057 C36.9515623,31.2406506 36.6271471,32.304459 36.053905,33.3763285 C35.4365674,34.5306495 34.5306495,35.4365674 33.3763285,36.053905 L33.1283803,36.18176 C32.0481723,36.7165306 30.8515024,37 27.9195733,37 Z"
        id="clearbit-edge"
        strokeOpacity="0.2"
        stroke="#9BADBC"
        fillOpacity="0"
        fill="#9BADBC"
      ></path>
      <path
        d="M27.9195733,37 L12.0804267,37 L11.4338943,36.9949826 C8.75934941,36.9515623 7.69554096,36.6271471 6.62367147,36.053905 C5.46935048,35.4365674 4.56343261,34.5306495 3.94609499,33.3763285 L3.81824005,33.1283803 C3.30403747,32.0897188 3.02217708,30.9433817 3.00125617,28.250264 L3,12.0804267 C3,8.92296455 3.32875737,7.77799245 3.94609499,6.62367147 C4.56343261,5.46935048 5.46935048,4.56343261 6.62367147,3.94609499 L6.87161969,3.81824005 C7.91028124,3.30403747 9.05661831,3.02217708 11.749736,3.00125617 L27.9195733,3 C31.0770355,3 32.2220075,3.32875737 33.3763285,3.94609499 C34.5306495,4.56343261 35.4365674,5.46935048 36.053905,6.62367147 L36.18176,6.87161969 C36.6959625,7.91028124 36.9778229,9.05661831 36.9987438,11.749736 L37,27.9195733 L36.9949826,28.5661057 C36.9515623,31.2406506 36.6271471,32.304459 36.053905,33.3763285 C35.4365674,34.5306495 34.5306495,35.4365674 33.3763285,36.053905 L33.1283803,36.18176 C32.0481723,36.7165306 30.8515024,37 27.9195733,37 Z"
        id="clearbit-fx"
        fillOpacity="0.2"
        fill="#9BADBC"
        filter="url(#ck-icon-shadow)"
      ></path>
      <path
        fill="url(#clearbit-a)"
        d="M37,20 L37,27.9195733 C37,31.0770355 36.6712426,32.2220075 36.053905,33.3763285 C35.4365674,34.5306495 34.5306495,35.4365674 33.3763285,36.053905 C32.2220075,36.6712426 31.0770355,37 27.9195733,37 L20,37 L20,20 L37,20 Z"
      ></path>
      <path
        fill="url(#clearbit-b)"
        d="M20,3 L27.9195733,3 C31.0770355,3 32.2220075,3.32875737 33.3763285,3.94609499 C34.5306495,4.56343261 35.4365674,5.46935048 36.053905,6.62367147 C36.6712426,7.77799245 37,8.92296455 37,12.0804267 L37,20 L20,20 L20,3 Z"
      ></path>
      <path
        fill="url(#clearbit-c)"
        d="M12.0804267,3 L20,3 L20,37 L12.0804267,37 C8.92296455,37 7.77799245,36.6712426 6.62367147,36.053905 C5.46935048,35.4365674 4.56343261,34.5306495 3.94609499,33.3763285 C3.32875737,32.2220075 3,31.0770355 3,27.9195733 L3,12.0804267 C3,8.92296455 3.32875737,7.77799245 3.94609499,6.62367147 C4.56343261,5.46935048 5.46935048,4.56343261 6.62367147,3.94609499 C7.77799245,3.32875737 8.92296455,3 12.0804267,3 Z"
      ></path>
    </g>
  </svg>
}
  />

  <Card
    title="Heap"
    href="/integrations/analytics/heap"
    horizontal
    icon={
  <svg
    className="h-6 w-6"
    width="32"
    height="32"
    viewBox="0 0 256 256"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M78.7 55.2H49V200.2H78.7V55.2ZM142.9 0H113.3V110.5H142.9V0Z"
      fill="black"
    />
    <path
      d="M142.9 144.9H113.3V255.4H142.9V144.9ZM207.1 55.2002H177.5V200.2H207.1V55.2002Z"
      fill="#31D891"
    />
  </svg>
}
  />

  <Card
    title="Segment"
    href="/integrations/analytics/segment"
    horizontal
    icon={
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none">
<path
  fill="#93C8A2"
  fill-rule="evenodd"
  d="M22.69 10.396H8.64a1.184 1.184 0 0 1-1.173-1.187c0-.653.528-1.188 1.173-1.188h14.05c.645 0 1.173.535 1.173 1.188 0 .653-.527 1.187-1.173 1.187Z"
  clip-rule="evenodd"
/>
<path
  fill="#43AF79"
  fill-rule="evenodd"
  d="M1.923 10.396A1.184 1.184 0 0 1 .75 9.209c0-.12.03-.238.059-.356C2.275 4.015 6.646.75 11.66.75c1.144 0 2.288.178 3.374.505.615.207.968.86.762 1.484-.205.623-.85.979-1.466.771a8.962 8.962 0 0 0-2.67-.415c-3.989 0-7.45 2.582-8.594 6.44-.176.505-.616.86-1.144.86Z"
  clip-rule="evenodd"
/>
<path
  fill="#93C8A2"
  fill-rule="evenodd"
  d="M19.786 4.667c0 .653-.528 1.188-1.173 1.188a1.184 1.184 0 0 1-1.173-1.188c0-.653.528-1.187 1.173-1.187s1.173.534 1.173 1.187ZM1.173 13.604h14.05c.645 0 1.173.534 1.173 1.187s-.528 1.188-1.173 1.188H1.173A1.184 1.184 0 0 1 0 14.79c0-.653.528-1.187 1.173-1.187Z"
  clip-rule="evenodd"
/>
<path
  fill="#43AF79"
  fill-rule="evenodd"
  d="M21.94 13.604c.645 0 1.173.534 1.173 1.187 0 .12-.029.238-.058.357-1.467 4.837-5.837 8.102-10.853 8.102-1.144 0-2.288-.178-3.373-.505-.616-.207-.968-.86-.763-1.483.205-.624.85-.98 1.467-.772.85.267 1.76.415 2.669.415 3.989 0 7.45-2.582 8.594-6.44.176-.505.616-.86 1.144-.86Z"
  clip-rule="evenodd"
/>
<path
  fill="#93C8A2"
  fill-rule="evenodd"
  d="M4.077 19.332c0-.653.528-1.187 1.173-1.187.646 0 1.174.534 1.174 1.187S5.896 20.52 5.25 20.52a1.184 1.184 0 0 1-1.173-1.188Z"
  clip-rule="evenodd"
/>
</svg>
}
  />
</CardGroup>


## Enabling analytics

Set your analytics keys in `docs.json`. You can add an unlimited number of analytics integrations for free.

The syntax for `docs.json` is below. You only need to include entries for the platforms you want to connect.

```json Analytics options in docs.json theme={null}
"integrations": {
    "amplitude": {
        "apiKey": "required"
    },
    "clearbit": {
        "publicApiKey": "required"
    },
    "cookies": {
      "key": "required",
      "value": "required"
    },
    "fathom": {
        "siteId": "required"
    },
    "ga4": {
        "measurementId": "required"
    },
    "gtm": {
        "tagId": "required"
    },
    "hightouch": {
        "apiKey": "required",
        "apiHost": "optional"
    },
    "hotjar": {
        "hjid": "required",
        "hjsv": "required"
    },
    "logrocket": {
        "appId": "required"
    },
    "mixpanel": {
        "projectToken": "required"
    },
    "pirsch": {
        "id": "required"
    },
    "plausible": {
        "domain": "required"
    },
    "posthog": {
        "apiKey": "required",
        "apiHost": "optional"
    },
    "segment": {
      "key": "required"
    },
    "telemetry": {
      "enabled": "boolean"
    }
}
```


## Analytics events

We send the following events to your analytics provider. All events use the `docs.` prefix.

| Event name                              | Description                                                                                               |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| `docs.accordion.close`                  | When a user closes an accordion.                                                                          |
| `docs.accordion.open`                   | When a user opens an accordion.                                                                           |
| `docs.api_playground.request`           | When a user calls an API in the API playground.                                                           |
| `docs.code_block.copy`                  | When a user copies code from a code block.                                                                |
| `docs.code_block.ask_ai`                | When a user asks the assistant to explain a code block.                                                   |
| `docs.content.view`                     | When a user views a page. Only available for analytics providers that do not track page views by default. |
| `docs.feedback.thumbs_up`               | When a user clicks the positive feedback button.                                                          |
| `docs.feedback.thumbs_down`             | When a user clicks the negative feedback button.                                                          |
| `docs.navitem.cta_click`                | When a user clicks a call to action.                                                                      |
| `docs.expandable.close`                 | When a user closes an expandable.                                                                         |
| `docs.expandable.open`                  | When a user opens an expandable.                                                                          |
| `docs.navitem.click`                    | When a user clicks a header navigation item.                                                              |
| `docs.footer.powered_by_mintlify_click` | When a user clicks the "Powered by Mintlify" link.                                                        |
| `docs.assistant.source_click`           | When a user clicks a citation in a chat.                                                                  |
| `docs.assistant.suggestion_click`       | When a user clicks a suggestion in a chat.                                                                |
| `docs.assistant.thumbs_up`              | When a user clicks the positive feedback button in a chat.                                                |
| `docs.assistant.thumbs_down`            | When a user clicks the negative feedback button in a chat.                                                |
| `docs.assistant.completed`              | When a chat session is completed.                                                                         |
| `docs.assistant.enter`                  | When a user initiates a chat.                                                                             |
| `docs.assistant.shared`                 | When a user shares a chat conversation.                                                                   |
| `docs.search.close`                     | When a user closes the search bar.                                                                        |
| `docs.search.result_click`              | When a user clicks a search result.                                                                       |
| `docs.context_menu.copy_page`           | When a user copies the current page as markdown.                                                          |
| `docs.context_menu.copy_mcp_link`       | When a user copies the hosted MCP server link.                                                            |
| `docs.context_menu.ai_provider_click`   | When a user clicks an AI provider and create a conversation with current page as context.                 |
| `docs.context_menu.install_mcp_server`  | When a user installs the hosted MCP server on code editors.                                               |



# Pirsch
Source: https://mintlify.com/docs/integrations/analytics/pirsch



Add the following to your `docs.json` file to send analytics to Pirsch.

You can get your site ID from Settings > Developer > Identification Code.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "pirsch": {
          "id": "required"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "pirsch": {
          "id": "8Kw7OKxBfswOjnKGZa7P9Day8JmVYwTp"
      }
  }
  ```
</CodeGroup>



# Plausible
Source: https://mintlify.com/docs/integrations/analytics/plausible



Add your site's domain to `docs.json` to send analytics to Plausible.

<Info>
  Do not include `https://` for the domain or server.
</Info>

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "plausible": {
          "domain": "required",
          "server": "optional"
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "plausible": {
          "domain": "docs.domain.com"
      }
  }
  ```
</CodeGroup>



# PostHog
Source: https://mintlify.com/docs/integrations/analytics/posthog



Add the following to your `docs.json` file to send analytics to PostHog.

You only need to include `apiHost` if you are self-hosting PostHog. We send events to `https://app.posthog.com` by default.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "posthog": {
          "apiKey": "YOUR_POSTHOG_PROJECT_API_KEY",
          "apiHost": "optional",
          "sessionRecording": true
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "posthog": {
          "apiKey": "phc_TXdpocbYTeZVm5VJmMzHTMrCofBQu3e0kN7HGMNGTVW"
      }
  }
  ```
</CodeGroup>

### Configuration options

<ParamField path="apiKey" type="string" required>
  Your PostHog project API key. Must start with `phc_`.
</ParamField>

<ParamField path="apiHost" type="string">
  The URL of your PostHog instance. Only required if you are self-hosting PostHog. Defaults to `https://app.posthog.com`.
</ParamField>

<ParamField path="sessionRecording" type="boolean" default="true">
  Enable or disable session recording. Set to `false` to disable session recordings while keeping analytics enabled.
</ParamField>

<br />

<Warning>
  Enabling PostHog analytics will disable the analytics on the Mintlify dashboard.
</Warning>


## Session recordings

Session recordings are enabled by default when you configure PostHog. To disable session recordings while keeping analytics enabled, set `sessionRecording` to `false` in your configuration.

```json Disable session recordings theme={null}
"integrations": {
    "posthog": {
        "apiKey": "phc_your-key",
        "sessionRecording": false
    }
}
```

You need to add the URL for your docs website to PostHog's "Authorized domains for recordings" before you can receive session recordings. The option to add your URL is in PostHog's project settings.



# Segment
Source: https://mintlify.com/docs/integrations/analytics/segment



Add your Segment write key to your `docs.json` file to send analytics to Segment.

<CodeGroup>
  ```json Analytics options in docs.json theme={null}
  "integrations": {
      "segment": {
          "key": "required",
      }
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "segment": {
          "key": "nqJxiRG15Y6M594P8Sb8ESEciU3VC2"
      }
  }
  ```
</CodeGroup>



# Privacy integrations
Source: https://mintlify.com/docs/integrations/privacy/overview

Integrate with a data privacy platform

<CardGroup>
  <Card title="Osano" href="/integrations/privacy/osano" icon={<svg width="32" height="32" className="h-6 w-6" viewBox="0 0 256 256" fill="none" xmlns="http://www.w3.org/2000/svg"><path fillRule="evenodd" clipRule="evenodd" d="M128 256C198.692 256 256 198.692 256 128C256 57.3076 198.692 0 128 0C57.3076 0 0 57.3076 0 128C0 198.692 57.3076 256 128 256ZM128 192C163.346 192 192 163.346 192 128C192 92.6538 163.346 64 128 64C92.6538 64 64 92.6538 64 128C64 163.346 92.6538 192 128 192Z" fill="#7764FA"/></svg>} horizontal />
</CardGroup>


## Enabling Data Privacy Integrations

You can add data privacy platforms onto your docs. Add the `integrations` field into your `docs.json` file with your respective scripts.

```json  theme={null}
  "integrations": {
    "osano": "SOURCE"
  }
```


## Cookie Consent and Disabling Telemetry

If you need to check if a user has already consented to cookies for GDPR compliance, you can specify a local storage key and value under `cookies`:

```json  theme={null}
  "integrations": {
    "cookies": {
      "key": "LOCAL STORAGE KEY",
      "value": "LOCAL STORAGE VALUE"
    }
  }
```

If these values are set, local storage will be checked to see if the user has consented to cookies. If they have not, telemetry will be disabled.

If you'd like to disable telemetry for all users, you can add the following to your `docs.json` file:

```json  theme={null}
  "integrations": {
    "telemetry": {
      "enabled": false
    }
  }
```

<Note>
  If you disable telemetry, you cannot collect feedback on your documentation pages, even if you enable feedback in your dashboard.
</Note>



# Speakeasy
Source: https://mintlify.com/docs/integrations/sdks/speakeasy

Automate your SDK usage snippets in the API playground

Autogenerated code snippets from Speakeasy SDKs can be integrated directly into Mintlify API reference documentation. SDK usage snippets are shown in the [interactive playground](/api-playground/overview) of Mintlify-powered documentation sites.

<Frame>
    <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=61aa5501cca4cb4156fdbed1f9fcbe03" alt="A Mintlify API playground with Speakeasy code snippets." data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="images/speakeasy/mintlify-with-speakeasy-openapi.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f534e524643696705d24397b587c020a 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=68efc971b3352f5e2a369f156b023f0e 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c48b14ad3cf72fb11a3ec91bb2a1c135 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1caa057b84e7f9d18c399d82671aab9f 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=06a46bd0a429de31763c914fd80cc4e2 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/mintlify-with-speakeasy-openapi.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=39db38cdea0ee4d231e8071b75d4de8b 2500w" />
</Frame>


## Prerequisites

To integrate Mintlify with Speakeasy, you'll need the following:

* A [Mintlify documentation repository](/quickstart#creating-the-repository).
* A Speakeasy-generated SDK with a configured [automated code sample URL](https://www.speakeasy.com/docs/code-samples/automated-code-sample-urls).


## Setting up the integration

To integrate Speakeasy with Mintlify, you must get the API's combined spec public URL from the registry and update your `docs.json` configuration file.

### Get the API's combined spec public URL from the registry

Navigate to your [Speakeasy Dashboard](https://app.speakeasy.com) and open the **API Registry** tab. Open the `*-with-code-samples` entry for the API.

<Frame>
    <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c31db82b03febfd0d6fa239c810c116f" alt="Screenshot of the Speakeasy API Registry page. The API Registry tab is emphasized with a red square and the number 1 and the entry for the API is emphasized with a red square and the number 2." data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="images/speakeasy/openapi-registry-and-combined-spec.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a3c6d930b01d43d9c86165f5a21ceeee 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=6df4f45f87ec5af438a652b0903ff74b 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4452036029237656e8d12bfbc349870e 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=13e877e0ebb6e2c7e964288f69510684 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cf573c47aef30f4733a529aa79edb454 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/openapi-registry-and-combined-spec.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c4b12a20171e3943e1d1d089c09765f9 2500w" />
</Frame>

<Note>
  If the entry is not labeled **Combined Spec**, ensure that the API has an [automatic code sample URL](https://www.speakeasy.com/docs/code-samples/automated-code-sample-urls) configured.
</Note>

From the registry entry's page, copy the provided public URL.

<Frame>
    <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=7d315613202f1097255a94940cce881b" alt="Screenshot showing the combined spec registry entry with the copy URL function emphasized with a red square." data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="images/speakeasy/copy-combined-spec-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=82a64d5244aa8c142eb1c97337491ba2 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e7fedc49789e7606ac7d5cec7efc1cc2 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c11dc3dfc52f944a378fe0d42040ee5b 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0b5cddbee64534c4e1967a162128d42e 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=872f3bfe7cd6d51a078c070b0d8a70ba 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/speakeasy/copy-combined-spec-url.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0d9e6f35fe34076cf0a0faedaf90175a 2500w" />
</Frame>

### Update your `docs.json` configuration file

Add the combined spec URL to an **Anchors** or **Tabs** section in your `docs.json` file.

Add the combined spec URL to an anchor by updating the `anchor` field in your `docs.json` file as follows:

```json docs.json theme={null}
{
  "anchors": [
    {
      "name": "API Reference",
      // !mark
      "openapi": "SPEAKEASY_COMBINED_SPEC_URL",
      "url": "api-reference",
      "icon": "square-terminal"
    }
  ]
}
```

Add the combined spec URL to a tab by updating the `tab` field in the `docs.json` file as follows:

```json docs.json theme={null}
{
  "tabs": [
    {
      "name": "API Reference",
      "url": "api-reference",
      // !mark
      "openapi": "SPEAKEASY_COMBINED_SPEC_URL"
    }
  ]
}
```

Speakeasy-generated code snippets can now be viewed in your API docs and interacted with in the playground.



# Stainless
Source: https://mintlify.com/docs/integrations/sdks/stainless

Automate SDK example snippets in your API playground


## Prerequisites

* Have a [Stainless](https://app.stainless.com) account.


## Integrate with Stainless

<Steps>
  <Step title="Set up OpenAPI decoration in Stainless.">
    In your `stainless.yml` config file, add `openapi.code_samples: 'mintlify'`. See the [Stainless documentation](https://app.stainless.com/docs/guides/integrate-docs) for more information.
  </Step>

  <Step title="Publish the URL to your OpenAPI spec.">
    In your Stainless project:

    1. Select the **Release** tab.
    2. Select **Setup OpenAPI publishing**.
    3. Copy the URL to your publicly accessible OpenAPI spec.

    <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=74e968242d6e3c42818a57f2523ecdfe" alt="Stainless release page with the OpenAPI spec URL highlighted with a green box." data-og-width="2124" width="2124" data-og-height="1104" height="1104" data-path="images/stainless-public-OpenAPI-spec.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=747726b4e3e0b16569489d1c4fc079f0 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e07b40dc864d23bfddc83454fe247789 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cd9e6775af76098ed9c2a03221d07aca 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=27f330e38be672687f720beea97705bd 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cc11946cfa1f54a50b72c4058548f2b3 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/stainless-public-OpenAPI-spec.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=81a2899ea97575ebbe3f189be611b424 2500w" />
  </Step>

  <Step title={<>Add your OpenAPI spec URL to your <code>docs.json</code>.</>}>
    In your `docs.json` file, add the URL from Stainless to the `openapi` field. See [OpenAPI Setup](/api-playground/openapi-setup) for more information.
  </Step>
</Steps>



# Front
Source: https://mintlify.com/docs/integrations/support/front



Add the following to your `docs.json` file to add a [Front Chat](https://front.com) widget.

<CodeGroup>
  ```json Integration options in docs.json theme={null}
  "integrations": {
      "frontchat": "CHAT_ID"
  }
  ```

  ```json Example theme={null}
  "integrations": {
      "frontchat": "1365d046d7c023e9b030ce90d02d093a"
  }
  ```
</CodeGroup>



# Intercom
Source: https://mintlify.com/docs/integrations/support/intercom



Add the following to your `docs.json` file to add an [Intercom](https://www.intercom.com) widget.

<CodeGroup>
  ```json Integration options in docs.json theme={null}
  "integrations": {
        "intercom": {
              "appId": "APP_ID"
        }
  }
  ```

  ```json Example theme={null}
  "integrations": {
        "intercom": {
              "appId": "APP_ID"
        }
  }
  ```
</CodeGroup>



# Support integrations
Source: https://mintlify.com/docs/integrations/support/overview

Integrate with a support widget

<CardGroup>
  <Card title="Intercom" href="/integrations/support/intercom" icon={<svg className="h-6 w-6" width="2500" height="2500" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid"><path d="M221.867 140.748a8.534 8.534 0 0 1-17.067 0V64a8.534 8.534 0 0 1 17.067 0v76.748zm-2.978 53.413c-1.319 1.129-32.93 27.655-90.889 27.655-57.958 0-89.568-26.527-90.887-27.656a8.535 8.535 0 0 1-.925-12.033 8.53 8.53 0 0 1 12.013-.942c.501.42 28.729 23.563 79.8 23.563 51.712 0 79.503-23.31 79.778-23.545 3.571-3.067 8.968-2.655 12.033.925a8.534 8.534 0 0 1-.923 12.033zM34.133 64A8.534 8.534 0 0 1 51.2 64v76.748a8.534 8.534 0 0 1-17.067 0V64zm42.668-17.067a8.534 8.534 0 0 1 17.066 0v114.001a8.534 8.534 0 0 1-17.066 0v-114zm42.666-4.318A8.532 8.532 0 0 1 128 34.082a8.532 8.532 0 0 1 8.534 8.533v123.733a8.534 8.534 0 0 1-17.067 0V42.615zm42.667 4.318a8.534 8.534 0 0 1 17.066 0v114.001a8.534 8.534 0 0 1-17.066 0v-114zM224 0H32C14.327 0 0 14.327 0 32v192c0 17.672 14.327 32 32 32h192c17.673 0 32-14.328 32-32V32c0-17.673-14.327-32-32-32z" fill="#1F8DED"/></svg>} horizontal />

  <Card
    href="/integrations/support/front"
    title="Front"
    icon={<svg className="h-6 w-6" width="754" height="754" viewBox="0 0 754 754" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M124 135.5C124 69 177.9 15 244.5 15H630.8V186.4C630.8 219.7 603.8 246.6 570.6 246.6H413.6C381.6 246.6 355.7 272.5 355.7 304.5V678.7C355.7 712 328.7 738.9 295.5 738.9H124V135.5Z" fill="#001B38"/>
<path d="M415 462.4C501.377 462.4 571.4 392.377 571.4 306C571.4 219.623 501.377 149.6 415 149.6C328.623 149.6 258.6 219.623 258.6 306C258.6 392.377 328.623 462.4 415 462.4Z" fill="url(#paint0_linear_66_11)"/>
<path opacity="0.5" d="M415 462.4C501.377 462.4 571.4 392.377 571.4 306C571.4 219.623 501.377 149.6 415 149.6C328.623 149.6 258.6 219.623 258.6 306C258.6 392.377 328.623 462.4 415 462.4Z" fill="url(#paint1_linear_66_11)"/>
<defs>
<linearGradient id="paint0_linear_66_11" x1="301.703" y1="191.962" x2="536.873" y2="428.762" gradientUnits="userSpaceOnUse">
<stop stopColor="#FF0057" stopOpacity="0.16"/>
<stop offset="0.86" stopColor="#FF0057"/>
</linearGradient>
<linearGradient id="paint1_linear_66_11" x1="301.703" y1="191.962" x2="536.873" y2="428.762" gradientUnits="userSpaceOnUse">
<stop stopColor="#FF0057" stopOpacity="0.16"/>
<stop offset="0.86" stopColor="#FF0057"/>
</linearGradient>
</defs>
</svg>
}
    horizontal
  />
</CardGroup>


## Enabling support integrations

Integrate customer support widgets into your documentation. Add the `integrations` field to your `docs.json` file with your respective app ID.

```json  theme={null}
  "integrations": {
    "intercom": "APP_ID",
    "frontchat": "CHAT_ID"
  }
```



# Migrations
Source: https://mintlify.com/docs/migration

How to migrate documentation from your current platform

This guide helps you move your existing documentation to Mintlify. Choose automated migration for supported platforms or manual migration for complete control over the process.


## Choose your migration path

<CardGroup cols="2">
  <Card title="Automated migration" icon="wand-sparkles">
    If you are migrating from Docusaurus or ReadMe, use our tools to automate your migration.
  </Card>

  <Card title="Manual migration" icon="pencil-ruler">
    If you are migrating from any other platform, follow our guide to migrate your content.
  </Card>
</CardGroup>

<Tabs>
  <Tab title="Automated migration">
    Migrate your documentation using the [@mintlify/scraping package](https://www.npmjs.com/package/@mintlify/scraping). The package scrapes your content and converts it to use Mintlify components.

    ### Supported Platforms

    <Columns cols="3">
      <Card
        title="Docusaurus"
        icon={<svg className="h-6 w-6" width="36" height="36" viewBox="0 -19 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
  <g>
  		<rect fill="#FFFFFF" x="126.030769" y="45.9487179" width="110.276923" height="44.6358974">

</rect>
  		<path d="M26.2564103,191.671795 C16.5441641,191.671795 8.0830359,186.385067 3.54067692,178.54359 C1.30231795,182.408533 0,186.883938 0,191.671795 C0,206.17321 11.7549949,217.928205 26.2564103,217.928205 L52.5128205,217.928205 L52.5128205,191.671795 L26.2564103,191.671795 Z" fill="#3ECC5F">

</path>
  		<path d="M144.384656,53.006441 L236.308349,47.2615385 L236.308349,34.1333333 C236.308349,19.6319179 224.552041,7.87692308 210.051938,7.87692308 L91.8980923,7.87692308 L88.616041,2.19241026 C87.1561846,-0.334769231 83.5104821,-0.334769231 82.0519385,2.19241026 L78.7698872,7.87692308 L75.4878359,2.19241026 C74.0279795,-0.334769231 70.3822769,-0.334769231 68.9237333,2.19241026 L65.6416821,7.87692308 L62.3596308,2.19241026 C60.8997744,-0.334769231 57.2540718,-0.334769231 55.7955282,2.19241026 L52.5134769,7.87692308 C52.4845949,7.87692308 52.4570256,7.88086154 52.4281436,7.88086154 L46.990441,2.44447179 C44.928,0.382030769 41.4070154,1.3246359 40.6508308,4.14326154 L38.8548923,10.8438974 L32.0374154,9.01645128 C29.2187897,8.26157949 26.6404103,10.839959 27.3965949,13.6585846 L29.2227282,20.4760615 L22.5234051,22.2706872 C19.7047795,23.0268718 18.7608615,26.5491692 20.8233026,28.6116103 L26.2596923,34.0493128 C26.2596923,34.0768821 26.2570667,34.1044513 26.2570667,34.1333333 L20.571241,37.4153846 C18.0453744,38.8739282 18.0453744,42.5209436 20.571241,43.9794872 L26.2570667,47.2615385 L20.571241,50.5435897 C18.0453744,52.0021333 18.0453744,55.6491487 20.571241,57.1076923 L26.2570667,60.3897436 L20.571241,63.6717949 C18.0453744,65.1303385 18.0453744,68.7773538 20.571241,70.2358974 L26.2570667,73.5179487 L20.571241,76.8 C18.0453744,78.2585436 18.0453744,81.905559 20.571241,83.3641026 L26.2570667,86.6461538 L20.571241,89.9282051 C18.0453744,91.3867487 18.0453744,95.0337641 20.571241,96.4923077 L26.2570667,99.774359 L20.571241,103.05641 C18.0453744,104.514954 18.0453744,108.161969 20.571241,109.620513 L26.2570667,112.902564 L20.571241,116.184615 C18.0453744,117.643159 18.0453744,121.290174 20.571241,122.748718 L26.2570667,126.030769 L20.571241,129.312821 C18.0453744,130.771364 18.0453744,134.418379 20.571241,135.876923 L26.2570667,139.158974 L20.571241,142.441026 C18.0453744,143.899569 18.0453744,147.546585 20.571241,149.005128 L26.2570667,152.287179 L20.571241,155.569231 C18.0453744,157.027774 18.0453744,160.67479 20.571241,162.133333 L26.2570667,165.415385 L20.571241,168.697436 C18.0453744,170.155979 18.0453744,173.802995 20.571241,175.261538 L26.2570667,178.54359 L20.571241,181.825641 C18.0453744,183.284185 18.0453744,186.9312 20.571241,188.389744 L26.2570667,191.671795 C26.2570667,206.17321 38.0120615,217.928205 52.5134769,217.928205 L210.051938,217.928205 C224.552041,217.928205 236.308349,206.17321 236.308349,191.671795 L236.308349,86.6461538 L144.384656,80.9012513 C137.019733,80.4404513 131.282708,74.3332103 131.282708,66.9538462 C131.282708,59.5744821 137.019733,53.467241 144.384656,53.006441" fill="#3ECC5F">

</path>
  		<polygon fill="#3ECC5F" points="183.794872 217.928205 223.179487 217.928205 223.179487 165.415385 183.794872 165.415385">

</polygon>
  		<path d="M249.435897,185.107692 C249.14839,185.107692 248.87401,185.156267 248.597005,185.191713 C248.547118,184.99479 248.499856,184.796554 248.444718,184.599631 C250.815672,183.609764 252.481641,181.272944 252.481641,178.54359 C252.481641,174.917579 249.543549,171.979487 245.917538,171.979487 C244.423549,171.979487 243.062154,172.499364 241.958072,173.339569 C241.812349,173.191221 241.666626,173.044185 241.518277,172.898462 C242.341415,171.800944 242.845538,170.45399 242.845538,168.977067 C242.845538,165.351056 239.907446,162.412964 236.281436,162.412964 C233.570462,162.412964 231.244144,164.057928 230.243774,166.405251 C230.049477,166.350113 229.853867,166.304164 229.659569,166.254277 C229.695015,165.977272 229.74359,165.702892 229.74359,165.415385 C229.74359,161.789374 226.805497,158.851282 223.179487,158.851282 C219.553477,158.851282 216.615385,161.789374 216.615385,165.415385 C216.615385,165.702892 216.663959,165.977272 216.699405,166.254277 C216.505108,166.304164 216.309497,166.350113 216.1152,166.405251 C215.114831,164.057928 212.788513,162.412964 210.077538,162.412964 C206.451528,162.412964 203.513436,165.351056 203.513436,168.977067 C203.513436,170.45399 204.017559,171.800944 204.840697,172.898462 C199.960944,177.666626 196.923077,184.31081 196.923077,191.671795 C196.923077,206.17321 208.678072,217.928205 223.179487,217.928205 C235.439918,217.928205 245.707487,209.513026 248.597005,198.151877 C248.87401,198.187323 249.14839,198.235897 249.435897,198.235897 C253.061908,198.235897 256,195.297805 256,191.671795 C256,188.045785 253.061908,185.107692 249.435897,185.107692" fill="#44D860">

</path>
  		<polygon fill="#3ECC5F" points="196.923077 139.158974 236.307692 139.158974 236.307692 112.902564 196.923077 112.902564">

</polygon>
  		<path d="M249.435897,129.312821 C251.248903,129.312821 252.717949,127.843774 252.717949,126.030769 C252.717949,124.217764 251.248903,122.748718 249.435897,122.748718 C249.2928,122.748718 249.154954,122.773662 249.017108,122.790728 C248.990851,122.692267 248.968533,122.593805 248.940964,122.495344 C250.125128,122.00041 250.958769,120.830687 250.958769,119.466667 C250.958769,117.653662 249.489723,116.184615 247.676718,116.184615 C246.929723,116.184615 246.248369,116.443241 245.696985,116.864656 C245.624779,116.789826 245.551262,116.716308 245.476431,116.644103 C245.888656,116.096656 246.140718,115.421867 246.140718,114.682749 C246.140718,112.871056 244.671672,111.400697 242.858667,111.400697 C241.502523,111.400697 240.339364,112.223836 239.839179,113.397497 C238.714092,113.083733 237.533867,112.902564 236.307692,112.902564 C229.058297,112.902564 223.179487,118.781374 223.179487,126.030769 C223.179487,133.280164 229.058297,139.158974 236.307692,139.158974 C237.533867,139.158974 238.714092,138.977805 239.839179,138.664041 C240.339364,139.837703 241.502523,140.660841 242.858667,140.660841 C244.671672,140.660841 246.140718,139.190482 246.140718,137.37879 C246.140718,136.639672 245.888656,135.964882 245.476431,135.417436 C245.551262,135.345231 245.624779,135.271713 245.696985,135.196882 C246.248369,135.618297 246.929723,135.876923 247.676718,135.876923 C249.489723,135.876923 250.958769,134.407877 250.958769,132.594872 C250.958769,131.230851 250.125128,130.061128 248.940964,129.566195 C248.968533,129.469046 248.990851,129.369272 249.017108,129.27081 C249.154954,129.287877 249.2928,129.312821 249.435897,129.312821" fill="#44D860">

</path>
  		<path d="M78.7692308,50.5435897 C76.9562256,50.5435897 75.4871795,49.0745436 75.4871795,47.2615385 C75.4871795,41.8317128 71.0708513,37.4153846 65.6410256,37.4153846 C60.2112,37.4153846 55.7948718,41.8317128 55.7948718,47.2615385 C55.7948718,49.0745436 54.3258256,50.5435897 52.5128205,50.5435897 C50.6998154,50.5435897 49.2307692,49.0745436 49.2307692,47.2615385 C49.2307692,38.2122667 56.5917538,30.8512821 65.6410256,30.8512821 C74.6902974,30.8512821 82.0512821,38.2122667 82.0512821,47.2615385 C82.0512821,49.0745436 80.5822359,50.5435897 78.7692308,50.5435897" fill="#000000">

</path>
  		<path d="M131.282051,217.928205 L210.051282,217.928205 C224.552697,217.928205 236.307692,206.17321 236.307692,191.671795 L236.307692,99.774359 L157.538462,99.774359 C143.037046,99.774359 131.282051,111.529354 131.282051,126.030769 L131.282051,217.928205 Z" fill="#FFFF50">

</path>
  		<path d="M216.640985,140.471795 L150.948759,140.471795 C150.222769,140.471795 149.635938,139.884964 149.635938,139.158974 C149.635938,138.432985 150.222769,137.846154 150.948759,137.846154 L216.640985,137.846154 C217.366974,137.846154 217.953805,138.432985 217.953805,139.158974 C217.953805,139.884964 217.366974,140.471795 216.640985,140.471795" fill="#000000">

</path>
  		<path d="M216.640985,166.728205 L150.948759,166.728205 C150.222769,166.728205 149.635938,166.141374 149.635938,165.415385 C149.635938,164.689395 150.222769,164.102564 150.948759,164.102564 L216.640985,164.102564 C217.366974,164.102564 217.953805,164.689395 217.953805,165.415385 C217.953805,166.141374 217.366974,166.728205 216.640985,166.728205" fill="#000000">

</path>
  		<path d="M216.640985,192.984615 L150.948759,192.984615 C150.222769,192.984615 149.635938,192.397785 149.635938,191.671795 C149.635938,190.945805 150.222769,190.358974 150.948759,190.358974 L216.640985,190.358974 C217.366974,190.358974 217.953805,190.945805 217.953805,191.671795 C217.953805,192.397785 217.366974,192.984615 216.640985,192.984615" fill="#000000">

</path>
  		<path d="M216.640985,127.587118 L150.948759,127.587118 C150.222769,127.587118 149.635938,126.998974 149.635938,126.274297 C149.635938,125.548308 150.222769,124.961477 150.948759,124.961477 L216.640985,124.961477 C217.366974,124.961477 217.953805,125.548308 217.953805,126.274297 C217.953805,126.998974 217.366974,127.587118 216.640985,127.587118" fill="#000000">

</path>
  		<path d="M216.640985,153.6 L150.948759,153.6 C150.222769,153.6 149.635938,153.013169 149.635938,152.287179 C149.635938,151.56119 150.222769,150.974359 150.948759,150.974359 L216.640985,150.974359 C217.366974,150.974359 217.953805,151.56119 217.953805,152.287179 C217.953805,153.013169 217.366974,153.6 216.640985,153.6" fill="#000000">

</path>
  		<path d="M216.640985,179.85641 L150.948759,179.85641 C150.222769,179.85641 149.635938,179.269579 149.635938,178.54359 C149.635938,177.8176 150.222769,177.230769 150.948759,177.230769 L216.640985,177.230769 C217.366974,177.230769 217.953805,177.8176 217.953805,178.54359 C217.953805,179.269579 217.366974,179.85641 216.640985,179.85641" fill="#000000">

</path>
  		<path d="M236.307692,58.5666297 C236.291938,58.5666297 236.27881,58.5587528 236.263056,58.5600656 C232.206441,58.6979118 230.287097,62.75584 228.593559,66.3359015 C226.826503,70.0761272 225.459856,72.5100964 223.220185,72.4365785 C220.740267,72.3473067 219.322421,69.5457477 217.820554,66.5800862 C216.095508,63.1759426 214.126277,59.3136246 209.992205,59.4580349 C205.993354,59.5945682 204.067446,63.1260554 202.368656,66.2413785 C200.560903,69.5601887 199.33079,71.5779938 196.958523,71.4847836 C194.428718,71.3928862 193.08439,69.1151426 191.528697,66.478999 C189.794462,63.5435323 187.789785,60.2431015 183.735795,60.3560041 C179.80521,60.4912246 177.874051,63.487081 176.17001,66.1324144 C174.367508,68.9287221 173.104574,70.6327631 170.702113,70.5316759 C168.111918,70.4384656 166.774154,68.5493169 165.226338,66.3608451 C163.488164,63.9019323 161.529436,61.1187528 157.487262,61.2539733 C153.643323,61.3852554 151.712164,63.8389169 150.009436,66.0037579 C148.392041,68.0570092 147.129108,69.682281 144.457518,69.579881 C143.732841,69.550999 143.125005,70.1194503 143.098749,70.84544 C143.071179,71.5688041 143.638318,72.1779528 144.362995,72.2055221 C148.323774,72.3381169 150.329764,69.8411323 152.071877,67.6277169 C153.617067,65.6637374 154.950892,63.9688862 157.576533,63.8796144 C160.105026,63.7719631 161.290503,65.3434092 163.083815,67.8771528 C164.786544,70.2848656 166.719015,73.0155323 170.60759,73.1560041 C174.681272,73.2925374 176.641313,70.2481067 178.376862,67.554199 C179.928615,65.1464862 181.267692,63.0682913 183.825067,62.9803323 C186.178954,62.8923733 187.460267,64.75264 189.266708,67.8128246 C190.969436,70.6970913 192.897969,73.9647015 196.864,74.1091118 C200.966564,74.2508964 202.94761,70.6682092 204.673969,67.4990605 C206.169272,64.7578913 207.580554,62.1676964 210.081477,62.0823631 C212.435364,62.0272246 213.662851,64.1763118 215.478482,67.7668759 C217.174646,71.1185067 219.097928,74.9151836 223.125662,75.0609067 C223.200492,75.0635323 223.27401,75.0648451 223.347528,75.0648451 C227.37001,75.0648451 229.278851,71.0279221 230.968451,67.4583631 C232.463754,64.2944656 233.878974,61.3130503 236.307692,61.1922708 L236.307692,58.5666297 Z" fill="#000000">

</path>
  		<polygon fill="#3ECC5F" points="105.025641 217.928205 157.538462 217.928205 157.538462 165.415385 105.025641 165.415385">

</polygon>
  		<path d="M183.794872,185.107692 C183.507364,185.107692 183.232985,185.156267 182.955979,185.191713 C182.906092,184.99479 182.858831,184.796554 182.803692,184.599631 C185.174646,183.609764 186.840615,181.272944 186.840615,178.54359 C186.840615,174.917579 183.902523,171.979487 180.276513,171.979487 C178.782523,171.979487 177.421128,172.499364 176.317046,173.339569 C176.171323,173.191221 176.0256,173.044185 175.877251,172.898462 C176.70039,171.800944 177.204513,170.45399 177.204513,168.977067 C177.204513,165.351056 174.266421,162.412964 170.64041,162.412964 C167.929436,162.412964 165.603118,164.057928 164.602749,166.405251 C164.408451,166.350113 164.212841,166.304164 164.018544,166.254277 C164.05399,165.977272 164.102564,165.702892 164.102564,165.415385 C164.102564,161.789374 161.164472,158.851282 157.538462,158.851282 C153.912451,158.851282 150.974359,161.789374 150.974359,165.415385 C150.974359,165.702892 151.022933,165.977272 151.058379,166.254277 C150.864082,166.304164 150.668472,166.350113 150.474174,166.405251 C149.473805,164.057928 147.147487,162.412964 144.436513,162.412964 C140.810503,162.412964 137.87241,165.351056 137.87241,168.977067 C137.87241,170.45399 138.376533,171.800944 139.199672,172.898462 C134.319918,177.666626 131.282051,184.31081 131.282051,191.671795 C131.282051,206.17321 143.037046,217.928205 157.538462,217.928205 C169.798892,217.928205 180.066462,209.513026 182.955979,198.151877 C183.232985,198.187323 183.507364,198.235897 183.794872,198.235897 C187.420882,198.235897 190.358974,195.297805 190.358974,191.671795 C190.358974,188.045785 187.420882,185.107692 183.794872,185.107692" fill="#44D860">

</path>
  		<polygon fill="#3ECC5F" points="105.025641 139.158974 157.538462 139.158974 157.538462 112.902564 105.025641 112.902564">

</polygon>
  		<path d="M170.666667,129.312821 C172.479672,129.312821 173.948718,127.843774 173.948718,126.030769 C173.948718,124.217764 172.479672,122.748718 170.666667,122.748718 C170.523569,122.748718 170.385723,122.773662 170.247877,122.790728 C170.221621,122.692267 170.199303,122.593805 170.171733,122.495344 C171.355897,122.00041 172.189538,120.830687 172.189538,119.466667 C172.189538,117.653662 170.720492,116.184615 168.907487,116.184615 C168.160492,116.184615 167.479138,116.443241 166.927754,116.864656 C166.855549,116.789826 166.782031,116.716308 166.7072,116.644103 C167.119426,116.096656 167.371487,115.421867 167.371487,114.682749 C167.371487,112.871056 165.902441,111.400697 164.089436,111.400697 C162.733292,111.400697 161.570133,112.223836 161.069949,113.397497 C159.944862,113.083733 158.764636,112.902564 157.538462,112.902564 C150.289067,112.902564 144.410256,118.781374 144.410256,126.030769 C144.410256,133.280164 150.289067,139.158974 157.538462,139.158974 C158.764636,139.158974 159.944862,138.977805 161.069949,138.664041 C161.570133,139.837703 162.733292,140.660841 164.089436,140.660841 C165.902441,140.660841 167.371487,139.190482 167.371487,137.37879 C167.371487,136.639672 167.119426,135.964882 166.7072,135.417436 C166.782031,135.345231 166.855549,135.271713 166.927754,135.196882 C167.479138,135.618297 168.160492,135.876923 168.907487,135.876923 C170.720492,135.876923 172.189538,134.407877 172.189538,132.594872 C172.189538,131.230851 171.355897,130.061128 170.171733,129.566195 C170.199303,129.469046 170.221621,129.369272 170.247877,129.27081 C170.385723,129.287877 170.523569,129.312821 170.666667,129.312821" fill="#44D860">

</path>
  		<path d="M183.794872,32.4923077 C183.584821,32.4923077 183.361641,32.4660513 183.15159,32.4266667 C182.941538,32.3872821 182.730174,32.321641 182.534564,32.2428718 C182.337641,32.1641026 182.153846,32.0590769 181.968738,31.9409231 C181.798072,31.8227692 181.628718,31.678359 181.469867,31.5339487 C181.326769,31.3764103 181.182359,31.2188718 181.064205,31.0350769 C180.946051,30.8512821 180.841026,30.6674872 180.760944,30.4705641 C180.683487,30.273641 180.617846,30.0635897 180.578462,29.8535385 C180.539077,29.6434872 180.512821,29.4203077 180.512821,29.2102564 C180.512821,29.0002051 180.539077,28.7770256 180.578462,28.5669744 C180.617846,28.3569231 180.683487,28.16 180.760944,27.9499487 C180.841026,27.7530256 180.946051,27.5692308 181.064205,27.3854359 C181.182359,27.2147692 181.326769,27.0441026 181.469867,26.8865641 C181.628718,26.7421538 181.798072,26.5977436 181.968738,26.4795897 C182.153846,26.3614359 182.337641,26.2564103 182.534564,26.177641 C182.730174,26.0988718 182.941538,26.0332308 183.15159,25.9938462 C183.571692,25.9019487 184.004923,25.9019487 184.438154,25.9938462 C184.646892,26.0332308 184.858256,26.0988718 185.055179,26.177641 C185.25079,26.2564103 185.435897,26.3614359 185.619692,26.4795897 C185.790359,26.5977436 185.959713,26.7421538 186.118564,26.8865641 C186.262974,27.0441026 186.407385,27.2147692 186.525538,27.3854359 C186.643692,27.5692308 186.748718,27.7530256 186.827487,27.9499487 C186.906256,28.16 186.971897,28.3569231 187.011282,28.5669744 C187.049354,28.7770256 187.076923,29.0002051 187.076923,29.2102564 C187.076923,30.0767179 186.721149,30.9300513 186.118564,31.5339487 C185.959713,31.678359 185.790359,31.8227692 185.619692,31.9409231 C185.435897,32.0590769 185.25079,32.1641026 185.055179,32.2428718 C184.858256,32.321641 184.646892,32.3872821 184.438154,32.4266667 C184.228103,32.4660513 184.004923,32.4923077 183.794872,32.4923077" fill="#000000">

</path>
  		<path d="M210.051282,30.8512821 C209.184821,30.8512821 208.344615,30.4968205 207.726277,29.8929231 C207.583179,29.7353846 207.438769,29.5647179 207.320615,29.3940513 C207.202462,29.2102564 207.097436,29.0264615 207.017354,28.8295385 C206.939897,28.6326154 206.874256,28.4225641 206.834872,28.2125128 C206.795487,28.0024615 206.769231,27.7792821 206.769231,27.5692308 C206.769231,26.7027692 207.123692,25.8625641 207.726277,25.2455385 C207.885128,25.1011282 208.054482,24.9567179 208.225149,24.8385641 C208.410256,24.7204103 208.594051,24.6153846 208.790974,24.5366154 C208.986585,24.4578462 209.197949,24.3922051 209.408,24.3528205 C209.828103,24.2609231 210.274462,24.2609231 210.694564,24.3528205 C210.903303,24.3922051 211.114667,24.4578462 211.31159,24.5366154 C211.5072,24.6153846 211.692308,24.7204103 211.876103,24.8385641 C212.046769,24.9567179 212.216123,25.1011282 212.374974,25.2455385 C212.977559,25.8625641 213.333333,26.7027692 213.333333,27.5692308 C213.333333,27.7792821 213.305764,28.0024615 213.267692,28.2125128 C213.228308,28.4225641 213.162667,28.6326154 213.083897,28.8295385 C212.992,29.0264615 212.900103,29.2102564 212.781949,29.3940513 C212.663795,29.5647179 212.519385,29.7353846 212.374974,29.8929231 C212.216123,30.0373333 212.046769,30.1817436 211.876103,30.2998974 C211.692308,30.4180513 211.5072,30.5230769 211.31159,30.6018462 C211.114667,30.6806154 210.903303,30.7462564 210.694564,30.785641 C210.484513,30.8250256 210.261333,30.8512821 210.051282,30.8512821" fill="#000000">

</path>
  </g>
</svg>}
        horizontal
      />

      <Card
        title="ReadMe"
        icon={<svg fill="#177fc4" className="h-6 w-6" width="36" height="36" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
<path d="M29.35 4.361h-7.767c-2.672 0-4.994 1.85-5.578 4.461-0.589-2.611-2.906-4.461-5.578-4.461h-7.761c-1.472 0-2.667 1.194-2.667 2.667v13.656c0 1.472 1.194 2.667 2.667 2.667h4.983c5.678 0 7.372 1.355 8.183 4.167 0.039 0.156 0.289 0.156 0.333 0 0.817-2.811 2.511-4.167 8.183-4.167h4.983c1.472 0 2.667-1.194 2.667-2.667v-13.65c0-1.467-1.183-2.661-2.65-2.672zM13.444 19.105c0 0.106-0.083 0.194-0.194 0.194h-8.906c-0.105 0-0.194-0.083-0.194-0.194v-1.272c0-0.105 0.083-0.194 0.194-0.194h8.911c0.105 0 0.194 0.083 0.194 0.194v1.272zM13.444 15.722c0 0.105-0.083 0.194-0.194 0.194h-8.906c-0.105 0-0.194-0.083-0.194-0.194v-1.272c0-0.106 0.083-0.194 0.194-0.194h8.911c0.105 0 0.194 0.083 0.194 0.194v1.272zM13.444 12.339c0 0.105-0.083 0.194-0.194 0.194h-8.906c-0.105 0-0.194-0.083-0.194-0.194v-1.272c0-0.105 0.083-0.194 0.194-0.194h8.911c0.105 0 0.194 0.083 0.194 0.194v1.272zM27.85 19.1c0 0.105-0.083 0.194-0.194 0.194h-8.906c-0.105 0-0.194-0.083-0.194-0.194v-1.272c0-0.105 0.083-0.194 0.194-0.194h8.911c0.106 0 0.194 0.083 0.194 0.194v1.272zM27.85 15.717c0 0.106-0.083 0.194-0.194 0.194h-8.906c-0.105 0-0.194-0.083-0.194-0.194v-1.272c0-0.105 0.083-0.194 0.194-0.194h8.911c0.106 0 0.194 0.083 0.194 0.194v1.272zM27.85 12.333c0 0.105-0.083 0.194-0.194 0.194h-8.906c-0.105 0-0.194-0.083-0.194-0.194v-1.267c0-0.105 0.083-0.194 0.194-0.194h8.911c0.106 0 0.194 0.083 0.194 0.194v1.267z"/>
</svg>}
        horizontal
      />
    </Columns>

    If your documentation is hosted on another platform, see the manual migration steps.

    ### Installing the scraper

    Install the `@mintlify/scraping` package to get started.

    ```bash  theme={null}
    npm install @mintlify/scraping@latest -g
    ```

    ### Scraping pages and sections

    The migration tool automatically detects your documentation platform and converts your content. Prepared files are stored locally in `./docs` by default.

    For large documentation sites, migrate smaller sections at a time rather than the entire site at once.

    **Migrate entire sections:**

    ```bash  theme={null}
    mintlify-scrape section https://your-docs-site.com/docs
    ```

    **Migrate single pages:**

    ```bash  theme={null}
    mintlify-scrape page https://your-docs-site.com/docs/getting-started
    ```

    **Migrate OpenAPI specifications:**

    ```bash  theme={null}
    mintlify-scrape openapi-file [openApiFilename]
    ```

    ### Add prepared content to your Mintlify project

    After scraping your existing documentation platform, you are ready to build your docs on Mintlify.

    Confirm that all of your pages have been migrated then add these files to the documentation repository that you created during the onboarding process. This is usually a GitHub repository.
  </Tab>

  <Tab title="Manual migration">
    Migrate your documentation from any platform with full control over the process.

    ### Content migration

    To migrate your content to Mintlify, you will need:

    * A valid `docs.json` for your site settings and navigation. See [Global settings](/organize/settings) and [Navigation](/organize/navigation) for more information.
    * An `MDX` file for each page of your documentation. See [Pages](/organize/pages) for more information.
    * (Optional) An OpenAPI specification for your API endpoint pages. See [OpenAPI setup](/api-playground/openapi-setup) for more information.

    1. If your content is already in `MDX` format, copy the pages to your Mintlify project. Otherwise, convert your content to `MDX` format.
    2. Create your `docs.json` referencing the paths to your `MDX` pages.
    3. If you have OpenAPI specifications, add them to your `docs.json` and configure the API playground.

    ### Asset migration

    1. Copy assets to your repository's `images/` directory.
    2. Update references in your `MDX` files:
       ```mdx  theme={null}
       ![Alt text](/images/screenshot.png)
       ```
  </Tab>
</Tabs>


## Post-migration checklist

After completing your migration (automated or manual), we recommend checking:

* All pages render
* Navigation works as intended
* Internal links resolve properly
* Images and assets load correctly
* Code blocks display with proper syntax highlighting
* Search functionality works
* Deployment is configured
* Custom domain is set up



---
**Navigation:** [← Previous](./06-vercel.md) | [Index](./index.md) | [Next →](./08-pdf-exports.md)
