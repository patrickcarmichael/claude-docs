---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running Your Model Locally

To run your model locally, first download it by calling `download` with your job ID:
```bash
  together fine-tuning download "ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04"
```
```python
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  client.fine_tuning.download(
      id="ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04",
      output="my-model/model.tar.zst",
  )
```
```typescript
  import Together from 'together-ai';

  const client = new Together({
    apiKey: process.env['TOGETHER_API_KEY'],
  });

  await client.fineTune.download({
    ft_id: 'ft-bb62e747-b8fc-49a3-985c-f32f7cc6bb04',
    output: 'my-model/model.tar.zst',
  });
```

Your model will be downloaded to the location specified in `output` as a `tar.zst` file, which is an archive file format that uses the [ZStandard](https://github.com/facebook/zstd) algorithm. You'll need to install ZStandard to decompress your model.

On Macs, you can use Homebrew:
```bash
  brew install zstd
  cd my-model
  zstd -d model.tar.zst
  tar -xvf model.tar
  cd ..
```

Once your archive is decompressed, you should see the following set of files:
```
tokenizer_config.json
special_tokens_map.json
pytorch_model.bin
generation_config.json
tokenizer.json
config.json
```

These can be used with various libraries and languages to run your model locally. [Transformers](https://pypi.org/project/transformers/) is a popular Python library for working with pretrained models, and using it with your new model looks like this:
```python
  from transformers import AutoTokenizer, AutoModelForCausalLM
  import torch

  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

  tokenizer = AutoTokenizer.from_pretrained("./my-model")

  model = AutoModelForCausalLM.from_pretrained(
      "./my-model",
      trust_remote_code=True,
  ).to(device)

  input_context = "Space Robots are"
  input_ids = tokenizer.encode(input_context, return_tensors="pt")
  output = model.generate(
      input_ids.to(device),
      max_length=128,
      temperature=0.7,
  ).cpu()
  output_text = tokenizer.decode(output[0], skip_special_tokens=True)

  print(output_text)
```
```
Space Robots are a great way to get your kids interested in science. After all, they are the future!
```

If you see the output, your new model is working!

You now have a custom fine-tuned model that you can run completely locally, either on your own machine or on networked hardware of your choice.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
