---
title: "Python"
source: "https://docs.cursor.com/tr/guides/languages/python"
language: "tr"
language_name: "Turkish"
---

# Python
Source: https://docs.cursor.com/tr/guides/languages/python

Python geliştirmeyi eklentiler ve linting araçlarıyla ayarla

<Note>
  Bu rehber, [Jack Fields](https://x.com/OrdinaryInds) ve onun
  Python geliştirme için VS Code kurulumunu anlatan
  [makalesinden](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  epey ilham aldı. Daha fazla detay için lütfen makalesine göz at.
</Note>

<div id="prerequisites">
  ## Önkoşullar
</div>

Başlamadan önce şunların olduğundan emin ol:

* [Python](https://python.org) kurulu (3.8 veya üzeri önerilir)
* Sürüm kontrolü için [Git](https://git-scm.com/)
* Cursor kurulu ve en son sürüme güncellenmiş

<div id="essential-extensions">
  ## Gerekli Uzantılar
</div>

Aşağıdaki uzantılar, Cursor’ı Python geliştirme için tam donanımlı hale getirir. Sözdizimi renklendirme, linting, hata ayıklama ve birim testleri sağlar.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Microsoft’tan temel dil desteği
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Hızlı Python dil sunucusu
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    Gelişmiş hata ayıklama özellikleri
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python linter’ı ve biçimlendirici
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### Gelişmiş Python Araçları
</div>

Yukarıdaki uzantılar bugüne kadar Cursor’da Python geliştirme için en popüler uzantılar olsa da, Python geliştirmenden en iyi şekilde yararlanmanı sağlayacak bazı ek uzantılar da ekledik.

<div id="uv-python-environment-manager">
  #### `uv` - Python Ortam Yöneticisi
</div>

[uv](https://github.com/astral-sh/uv), pip’in varsayılan paket yöneticisi olarak yerini almasının yanı sıra sanal ortamlar oluşturup yönetmek için kullanılabilen modern bir Python paket yöneticisidir.

uv’yi yüklemek için terminalinde şu komutu çalıştır:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Python Linter ve Biçimlendirici
</div>

[Ruff](https://docs.astral.sh/ruff/), programlama hatalarını yakalamak, kodlama standartlarını uygulamaya yardımcı olmak ve yeniden düzenleme (refactoring) önerilerinde bulunmak için kullanılabilen modern bir Python linter’ı ve biçimlendiricisidir. Kod biçimlendirme için Black’le birlikte kullanılabilir.

Ruff’u kurmak için terminalinde aşağıdaki komutu çalıştır:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Cursor Yapılandırması
</div>

<div id="1-python-interpreter">
  ### 1. Python Yorumlayıcısı
</div>

Cursor’da Python yorumlayıcını yapılandır:

1. Komut Paleti’ni aç (Cmd/Ctrl + Shift + P)
2. "Python: Select Interpreter" komutunu ara
3. Python yorumlayıcını (veya bir sanal ortam kullanıyorsan onu) seç

<div id="2-code-formatting">
  ### 2. Kod Biçimlendirme
</div>

Black ile otomatik kod biçimlendirmeyi ayarla:

<Note>
  Black, kodunu tutarlı bir stille otomatik olarak biçimlendiren bir kod
  biçimlendiricisidir. Yapılandırma gerektirmez ve Python topluluğunda
  yaygın olarak kullanılır.
</Note>

Black’i yüklemek için terminalinde aşağıdaki komutu çalıştır:

```bash  theme={null}
pip install black
```

Ardından, kod biçimlendirme için Black’i kullanması için Cursor’ı yapılandırmak üzere `settings.json` dosyana şunu ekle:

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. Linting
</div>

Programlama hatalarını kontrol etmek, kodlama standartlarını sağlamaya yardımcı olmak ve yeniden düzenleme (refactoring) önermek için PyLint kullanabiliriz.

PyLint’i yüklemek için terminalinde şu komutu çalıştır:

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. Tür Denetimi
</div>

Linting’e ek olarak, tür hatalarını kontrol etmek için MyPy kullanabiliriz.

MyPy’yi yüklemek için terminalinde aşağıdaki komutu çalıştır:

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## Hata ayıklama
</div>

Cursor, Python için güçlü hata ayıklama özellikleri sunar:

1. Oluk (gutter) alanına tıklayarak kesme noktaları ayarla
2. Hata Ayıklama (Debug) panelini kullan (Cmd/Ctrl + Shift + D)
3. Özel hata ayıklama yapılandırmaları için `launch.json` dosyasını yapılandır

<div id="recommended-features">
  ## Önerilen Özellikler
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/tr/tab/overview">
    Hareketlerini anlayan akıllı kod önerileri
  </Card>

  <Card title="Chat" icon="comments" href="/tr/chat/overview">
    Doğal konuşmalar yoluyla kodu keşfet ve anla
  </Card>

  <Card title="Agent" icon="robot" href="/tr/chat/agent">
    AI yardımıyla karmaşık geliştirme görevlerini halledebilir
  </Card>

  <Card title="Context" icon="network-wired" href="/tr/context/model-context-protocol">
    Üçüncü parti sistemlerden context çek
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/tr/tab/auto-import">
    Kod yazarken modülleri otomatik olarak import et
  </Card>

  <Card title="AI Review" icon="check-double" href="/tr/tab/overview#quality">
    Cursor kodunu sürekli AI ile gözden geçirir
  </Card>
</CardGroup>

<div id="framework-support">
  ## Framework Desteği
</div>

Cursor, popüler Python frameworkleriyle sorunsuz çalışır:

* **Web Frameworkleri**: Django, Flask, FastAPI
* **Veri Bilimi**: Jupyter, NumPy, Pandas
* **Makine Öğrenimi**: TensorFlow, PyTorch, scikit-learn
* **Test**: pytest, unittest
* **API**: requests, aiohttp
* **Veritabanı**: SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS & macOS (Swift)](./ios-macos-swift.md) →