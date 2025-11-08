---
title: "Python"
source: "https://docs.cursor.com/id/guides/languages/python"
language: "id"
language_name: "Indonesian"
---

# Python
Source: https://docs.cursor.com/id/guides/languages/python

Menyiapkan pengembangan Python dengan ekstensi dan alat linting

<Note>
  Panduan ini banyak terinspirasi oleh [Jack Fields](https://x.com/OrdinaryInds)
  dan
  [artikelnya](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  tentang setup VS Code untuk pengembangan Python. Cek artikelnya buat
  detail lebih lanjut.
</Note>

<div id="prerequisites">
  ## Prasyarat
</div>

Sebelum mulai, pastikan kamu punya:

* [Python](https://python.org) terinstal (disarankan versi 3.8 atau lebih baru)
* [Git](https://git-scm.com/) untuk kontrol versi
* Cursor terinstal dan diperbarui ke versi terbaru

<div id="essential-extensions">
  ## Ekstensi Esensial
</div>

Ekstensi berikut menyiapkan Cursor agar lengkap untuk pengembangan Python. Ekstensi ini ngasih kamu syntax highlighting, linting, debugging, dan unit testing.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Dukungan bahasa inti dari Microsoft
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Server bahasa Python yang cepat
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    Kemampuan debugging yang lebih kaya
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Linter dan formatter untuk Python
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### Tooling Python Lanjutan
</div>

Walaupun ekstensi di atas sebelumnya jadi yang paling populer buat pengembangan Python di Cursor, kami juga nambahin beberapa ekstensi tambahan yang bisa bantu kamu maksimalin workflow Python kamu.

<div id="uv-python-environment-manager">
  #### `uv` - Pengelola Environment Python
</div>

[uv](https://github.com/astral-sh/uv) adalah package manager Python modern yang bisa dipakai untuk bikin dan ngelola virtual environment, sekaligus bisa gantiin pip sebagai package manager default.

Untuk instal uv, jalanin perintah berikut di terminal kamu:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Linter dan Formatter Python
</div>

[Ruff](https://docs.astral.sh/ruff/) adalah linter dan formatter Python modern yang bisa dipakai buat memeriksa kesalahan pemrograman, membantu menegakkan standar penulisan kode, dan menyarankan refactoring. Ruff bisa dipakai bareng Black untuk formatting kode.

Buat memasang Ruff, jalanin perintah berikut di terminal:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Konfigurasi Cursor
</div>

<div id="1-python-interpreter">
  ### 1. Interpreter Python
</div>

Atur interpreter Python kamu di Cursor:

1. Buka Command Palette (Cmd/Ctrl + Shift + P)
2. Cari "Python: Select Interpreter"
3. Pilih interpreter Python kamu (atau virtual environment kalau kamu memakainya)

<div id="2-code-formatting">
  ### 2. Pemformatan Kode
</div>

Siapkan pemformatan kode otomatis dengan Black:

<Note>
  Black adalah pemformat kode yang secara otomatis merapikan kode kamu agar mengikuti
  gaya yang konsisten. Black tidak memerlukan konfigurasi dan sudah banyak diadopsi oleh
  komunitas Python.
</Note>

Untuk menginstal Black, jalankan perintah berikut di terminal kamu:

```bash  theme={null}
pip install black
```

Lalu, atur Cursor buat pakai Black untuk format kode, dengan nambahin yang berikut ke file `settings.json` lo:

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

Kita bisa pakai PyLint buat ngecek error pemrograman, bantu menegakkan standar penulisan kode, dan ngasih saran refactoring.

Untuk menginstal PyLint, jalankan perintah berikut di terminal:

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
  ### 4. Pemeriksaan Tipe
</div>

Selain linting, kita bisa pakai MyPy buat ngecek error tipe.

Untuk memasang MyPy, jalanin perintah berikut di terminal:

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## Debugging
</div>

Cursor menyediakan kemampuan debugging yang powerful untuk Python:

1. Pasang breakpoint dengan klik di gutter
2. Buka panel Debug (Cmd/Ctrl + Shift + D)
3. Atur `launch.json` untuk konfigurasi debug kustom

<div id="recommended-features">
  ## Fitur Rekomendasi
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/id/tab/overview">
    Saran kode cerdas yang paham konteks dan tindakan lo
  </Card>

  <Card title="Chat" icon="comments" href="/id/chat/overview">
    Jelajahi dan pahami kode lewat percakapan natural
  </Card>

  <Card title="Agent" icon="robot" href="/id/chat/agent">
    Tangani tugas pengembangan kompleks dengan bantuan AI
  </Card>

  <Card title="Context" icon="network-wired" href="/id/context/model-context-protocol">
    Ambil konteks dari sistem pihak ketiga
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/id/tab/auto-import">
    Impor modul otomatis saat lo ngoding
  </Card>

  <Card title="AI Review" icon="check-double" href="/id/tab/overview#quality">
    Cursor terus nge-review kode lo pakai AI
  </Card>
</CardGroup>

<div id="framework-support">
  ## Dukungan Framework
</div>

Cursor bekerja mulus dengan berbagai framework Python populer:

* **Web Frameworks**: Django, Flask, FastAPI
* **Data Science**: Jupyter, NumPy, Pandas
* **Machine Learning**: TensorFlow, PyTorch, scikit-learn
* **Testing**: pytest, unittest
* **API**: requests, aiohttp
* **Database**: SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS & macOS (Swift)](./ios-macos-swift.md) →