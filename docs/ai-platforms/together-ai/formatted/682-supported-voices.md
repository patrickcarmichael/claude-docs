---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supported Voices

Different models support different voices. Use the Voices API to discover available voices for each model.

**Voices API**
```python
  from together import Together

  client = Together()

  # List all available voices

  response = client.audio.voices.list()

  for model_voices in response.data:
      print(f"Model: {model_voices.model}")
      for voice in model_voices.voices:
          print(f"  - Voice: {voice['name']}")
```
```typescript
  import fetch from 'node-fetch';

  async function getVoices() {
    const apiKey = process.env.TOGETHER_API_KEY;
    const model = 'canopylabs/orpheus-3b-0.1-ft';
    const url = `https://api.together.xyz/v1/voices?model=${model}`;

    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });

    const data = await response.json();
    
    console.log(`Available voices for ${model}:`);
    console.log('='.repeat(50));
    
    // List available voices
    for (const voice of data.voices || []) {
      console.log(voice.name || 'Unknown voice');
    }
  }

  getVoices();
```
```bash
  curl -X GET "https://api.together.xyz/v1/voices?model=canopylabs/orpheus-3b-0.1-ft" \
       -H "Authorization: Bearer $TOGETHER_API_KEY"
```

**Available Voices**

**Orpheus Model:**

Sample voices include:
```text
`tara`
`leah`
`jess`
`leo`
`dan`
`mia`
`zac`
`zoe`
```
For a complete list, query the `/v1/voices` endpoint or see the [Kokoro voice documentation](https://github.com/remsky/Kokoro-FastAPI).

**Kokoro Model:**
```text
af_heart
af_alloy
af_aoede
af_bella
af_jessica
af_kore
af_nicole
af_nova
af_river
af_sarah
af_sky
am_adam
am_echo
am_eric
am_fenrir
am_liam
am_michael
am_onyx
am_puck
am_santa
bf_alice
bf_emma
bf_isabella
bf_lily
bm_daniel
bm_fable
bm_george
bm_lewis
jf_alpha
jf_gongitsune
jf_nezumi
jf_tebukuro
jm_kumo
zf_xiaobei
zf_xiaoni
zf_xiaoxiao
zf_xiaoyi
zm_yunjian
zm_yunxi
zm_yunxia
zm_yunyang
ef_dora
em_alex
em_santa
ff_siwis
hf_alpha
hf_beta
hm_omega
hm_psi
if_sara
im_nicola
pf_dora
pm_alex
pm_santa
```
**Cartesia Models:**

All valid voice model strings:
```text
'german conversational woman',
'nonfiction man',
'friendly sidekick',
'french conversational lady',
'french narrator lady',
'german reporter woman',
'indian lady',
'british reading lady',
'british narration lady',
'japanese children book',
'japanese woman conversational',
'japanese male conversational',
'reading lady',
'newsman',
'child',
'meditation lady',
'maria',
"1920's radioman",
'newslady',
'calm lady',
'helpful woman',
'mexican woman',
'korean narrator woman',
'russian calm lady',
'russian narrator man 1',
'russian narrator man 2',
'russian narrator woman',
'hinglish speaking lady',
'italian narrator woman',
'polish narrator woman',
'chinese female conversational',
'pilot over intercom',
'chinese commercial man',
'french narrator man',
'spanish narrator man',
'reading man',
'new york man',
'friendly french man',
'barbershop man',
'indian man',
'australian customer support man',
'friendly australian man',
'wise man',
'friendly reading man',
'customer support man',
'dutch confident man',
'dutch man',
'hindi reporter man',
'italian calm man',
'italian narrator man',
'swedish narrator man',
'polish confident man',
'spanish-speaking storyteller man',
'kentucky woman',
'chinese commercial woman',
'middle eastern woman',
'hindi narrator woman',
'sarah',
'sarah curious',
'laidback woman',
'reflective woman',
'helpful french lady',
'pleasant brazilian lady',
'customer support lady',
'british lady',
'wise lady',
'australian narrator lady',
'indian customer support lady',
'swedish calm lady',
'spanish narrator lady',
'salesman',
'yogaman',
'movieman',
'wizardman',
'australian woman',
'korean calm woman',
'friendly german man',
'announcer man',
'wise guide man',
'midwestern man',
'kentucky man',
'brazilian young man',
'chinese call center man',
'german reporter man',
'confident british man',
'southern man',
'classy british man',
'polite man',
'mexican man',
'korean narrator man',
'turkish narrator man',
'turkish calm man',
'hindi calm man',
'hindi narrator man',
'polish narrator man',
'polish young man',
'alabama male',
'australian male',
'anime girl',
'japanese man book',
'sweet lady',
'commercial lady',
'teacher lady',
'princess',
'commercial man',
'asmr lady',
'professional woman',
'tutorial man',
'calm french woman',
'new york woman',
'spanish-speaking lady',
'midwestern woman',
'sportsman',
'storyteller lady',
'spanish-speaking man',
'doctor mischief',
'spanish-speaking reporter man',
'young spanish-speaking woman',
'the merchant',
'stern french man',
'madame mischief',
'german storyteller man',
'female nurse',
'german conversation man',
'friendly brazilian man',
'german woman',
'southern woman',
'british customer support lady',
'chinese woman narrator',
'pleasant man',
'california girl',
'john',
'anna'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
