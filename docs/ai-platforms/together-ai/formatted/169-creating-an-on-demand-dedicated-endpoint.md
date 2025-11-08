---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating an on demand dedicated endpoint

Navigate to the [Models page](https://api.together.xyz/models) in our playground. Under "All models" click "Dedicated." Search across 179 available models.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0c3ceeb2256d838d6e80c1e1f17ab67d" alt="" data-og-width="2958" width="2958" data-og-height="1628" height="1628" data-path="images/guides/35.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=783ad2585a2500311f5ce3550f2dbb30 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bd83993a17e21a1bc4e0b71294add6e3 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=64d46bb17fde33507417d43a89402708 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=982c5a1caecd0b3bbfcb8a597d4a6bff 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1314acdae8c3f67405e89e248f6675e3 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/35.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0dea60abac384d19a9292ccd48a12dbf 2500w" />
</Frame>

Select your hardware. We have multiple hardware options available, all with varying prices (e.g. RTX-6000, L40, A100 SXM, A100 PCIe, and H100).

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=fdc2961419e08a0922758f498f7a333a" alt="" data-og-width="2946" width="2946" data-og-height="1626" height="1626" data-path="images/guides/36.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7857154644c6d608369538995671133b 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5b0f7240d4153fffa67b622a070e5b57 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=445ceca56d9b0a97d375cc48816f0ccd 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88ccd0e9c3f2f76e39a344f65e3411ac 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6a1460ad7411080ad00ec642da64ed4e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/36.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=017357ab49e108ddba11fa229ee791a9 2500w" />
</Frame>

Click the Play button, and wait up to 10 minutes for the endpoint to be deployed.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=412baeca7510f61b5a61a254b0260eb1" alt="" data-og-width="2946" width="2946" data-og-height="1610" height="1610" data-path="images/guides/37.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4770b214b36f1c2001b30adee6ac1e75 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=677f18bf18d29bcee5fca9b2cbbb83cb 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=30f0c9a759f5e897fc9e26ae00ea6f40 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=026d721b806446e4e2d92cfd40dfad34 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a431af84de95ddc38912f07a8fcc6b29 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/37.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=16128130b3906bb33497d05fa28d97d3 2500w" />
</Frame>

We will provide you the string you can use to call the model, as well as additional information about your deployment.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aa6737c9c7dd6c7e29ee09c483708f46" alt="" data-og-width="2942" width="2942" data-og-height="1622" height="1622" data-path="images/guides/38.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d6e4f2061e07e38b339c5a75ca2a36e2 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1da32a6eeb5fdebe5a0904830b1bc58b 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=80c71a29cdee91bd17e6b3085d5ad578 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b60edd771e9360f5af9f49fd5a17d8a8 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ff7b08bc1bdb1795b34164eec4ed36d3 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/38.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=62cb1479549a392c2aa20bc9ac4fe689 2500w" />
</Frame>

You can navigate away while your model is being deployed. Click open when it's ready:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=6ea83c6ea056acfb860ecd683b7f4dee" alt="" data-og-width="2954" width="2954" data-og-height="1638" height="1638" data-path="images/guides/39.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d429919821e73c9647bba27b708c1e1a 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9b0b2085536a560b0cde82adfd87a2a8 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=1aca589d3ab7007be037261f223f3b22 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9197c1624b1bb3a158a49373302cdcae 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=7f92608f147558d8efa462de181afb6f 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/39.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ded8dfdc45a8ac7137fd1bd33c2a015b 2500w" />
</Frame>

Start using your endpoint!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=04400f84eb6783eea2e86081028b960d" alt="" data-og-width="2946" width="2946" data-og-height="1640" height="1640" data-path="images/guides/40.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=620f6be6b78462a99ae3f9e81b5df9b1 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c378f09db28186ba1313170a326ae4d4 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8b25eb3393e900befac9e6db234550f3 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c4977f7fa86efecf0bf25a05eb4993ba 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=4fc067cce3d7083c266bd5753f799e23 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/40.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d623b0c81d339da962f987466bb1bb31 2500w" />
</Frame>

You can now find your endpoint in the My Models Page, and upon clicking the Model, under "Endpoints"

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=3eff1812bb11f531a669d3bd7a2bfab9" alt="" data-og-width="2648" width="2648" data-og-height="488" height="488" data-path="images/guides/41.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8750849ca56337be5ed6b8bc965c6cdb 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=8c1d8797cbbf966f54987dd0e1bbabed 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c62a47660be11a6833d7b77c14e45407 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=921669ce1ffa7400dbf4eb28aba5a1cb 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=77b6678a2a311d61d849761fc81e2e20 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/41.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b6250a022f964dd604df643a36a35fa0 2500w" />
</Frame>

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f50768940462785d1dee1f7c244434ce" alt="" data-og-width="2630" width="2630" data-og-height="1468" height="1468" data-path="images/guides/42.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=a6cd8b97ee861440b295dced7b761468 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=21851653bc76fe58df140f9bf6f82e21 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=f661b3738aa70fd15dd9761b58c882d7 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=fdd6601870fc04128ad355952871e65e 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=7abb29ed321e934043ee799bfcb21695 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/42.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=780feb7685f576b30c3323465228cd86 2500w" />
</Frame>

**Looking for custom configurations?** [Contact us.](https://www.together.ai/forms/monthly-reserved)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
