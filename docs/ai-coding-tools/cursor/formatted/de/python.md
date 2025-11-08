---
title: "Python"
source: "https://docs.cursor.com/de/guides/languages/python"
language: "de"
language_name: "German"
---

# Python
Source: https://docs.cursor.com/de/guides/languages/python

Python-Entwicklung mit Erweiterungen und Linting-Tools einrichten

<Note>
  Dieser Guide wurde maßgeblich von [Jack Fields](https://x.com/OrdinaryInds)
  und seinem
  [Artikel](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  zum Einrichten von VS Code für Python-Entwicklung inspiriert. Schau dir für
  weitere Details seinen Artikel an.
</Note>

<div id="prerequisites">
  ## Voraussetzungen
</div>

Bevor wir starten, stell sicher, dass du Folgendes eingerichtet hast:

* [Python](https://python.org) installiert (empfohlen: 3.8 oder höher)
* [Git](https://git-scm.com/) für Versionskontrolle
* Cursor installiert und auf die neueste Version aktualisiert

<div id="essential-extensions">
  ## Unverzichtbare Erweiterungen
</div>

Die folgenden Erweiterungen statten Cursor vollständig für die Python-Entwicklung aus. Sie bieten dir Syntaxhervorhebung, Linting, Debugging und Unit-Tests.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Zentrale Sprachunterstützung von Microsoft
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Schneller Python-Sprachserver
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    Erweiterte Debugging-Funktionen
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python-Linter und -Formatter
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### Erweiterte Python-Tools
</div>

Während die oben genannten Erweiterungen bisher zu den beliebtesten für die Python-Entwicklung in Cursor gehörten, haben wir außerdem zusätzliche Erweiterungen hinzugefügt, die dir helfen können, das Beste aus deiner Python-Entwicklung herauszuholen.

<div id="uv-python-environment-manager">
  #### `uv` – Python-Umgebungsmanager
</div>

[uv](https://github.com/astral-sh/uv) ist ein moderner Python-Paketmanager, mit dem du virtuelle Umgebungen erstellen und verwalten kannst und der pip als Standard-Paketmanager ersetzen kann.

Um uv zu installieren, führe den folgenden Befehl in deinem Terminal aus:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Python-Linter und -Formatter
</div>

[Ruff](https://docs.astral.sh/ruff/) ist ein moderner Python-Linter und -Formatter, der Programmierfehler aufspürt, die Einhaltung von Code-Standards unterstützt und Refactorings vorschlägt. Er kann zusammen mit Black für die Codeformatierung verwendet werden.

Um Ruff zu installieren, führ den folgenden Befehl in deinem Terminal aus:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Cursor-Konfiguration
</div>

<div id="1-python-interpreter">
  ### 1. Python-Interpreter
</div>

Konfigurier deinen Python-Interpreter in Cursor:

1. Öffne die Befehlspalette (Cmd/Ctrl + Shift + P)
2. Such nach „Python: Select Interpreter“
3. Wähl deinen Python-Interpreter aus (oder eine virtuelle Umgebung, wenn du eine verwendest)

<div id="2-code-formatting">
  ### 2. Codeformatierung
</div>

Richte automatische Codeformatierung mit Black ein:

<Note>
  Black ist ein Code-Formatter, der deinen Code automatisch in einen
  konsistenten Stil bringt. Er benötigt keine Konfiguration und ist in der
  Python-Community weit verbreitet.
</Note>

Um Black zu installieren, führ den folgenden Befehl in deinem Terminal aus:

```bash  theme={null}
pip install black
```

Konfigurier danach Cursor so, dass Black fürs Code-Formatieren verwendet wird, indem du Folgendes zu deiner Datei `settings.json` hinzufügst:

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

Mit PyLint kannst du Programmierfehler erkennen, die Einhaltung von Coding-Standards sicherstellen und Vorschläge zur Refaktorisierung erhalten.

Um PyLint zu installieren, führe den folgenden Befehl in deinem Terminal aus:

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
  ### 4. Typprüfung
</div>

Zusätzlich zum Linting können wir MyPy verwenden, um nach Typfehlern zu suchen.

Um MyPy zu installieren, führ in deinem Terminal den folgenden Befehl aus:

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

Cursor bietet leistungsstarke Debugging-Funktionen für Python:

1. Setz Breakpoints, indem du in die Gutter klickst
2. Nutz das Debug-Panel (Cmd/Ctrl + Shift + D)
3. Konfigurier `launch.json` für benutzerdefinierte Debug-Konfigurationen

<div id="recommended-features">
  ## Empfohlene Features
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/de/tab/overview">
    Intelligente Code-Vervollständigungen, die deine Aktionen verstehen
  </Card>

  <Card title="Chat" icon="comments" href="/de/chat/overview">
    Erkunde und versteh Code durch natürliche Unterhaltungen
  </Card>

  <Card title="Agent" icon="robot" href="/de/chat/agent">
    Bewältige komplexe Entwicklungsaufgaben mit KI-Unterstützung
  </Card>

  <Card title="Context" icon="network-wired" href="/de/context/model-context-protocol">
    Zieh Kontext aus Drittanbieter-Systemen heran
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/de/tab/auto-import">
    Importiere Module automatisch, während du codest
  </Card>

  <Card title="AI Review" icon="check-double" href="/de/tab/overview#quality">
    Cursor prüft deinen Code kontinuierlich mit KI
  </Card>
</CardGroup>

<div id="framework-support">
  ## Framework-Unterstützung
</div>

Cursor arbeitet nahtlos mit gängigen Python-Frameworks:

* **Web-Frameworks**: Django, Flask, FastAPI
* **Data Science**: Jupyter, NumPy, Pandas
* **Machine Learning**: TensorFlow, PyTorch, scikit-learn
* **Testing**: pytest, unittest
* **APIs**: requests, aiohttp
* **Datenbanken**: SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS & macOS (Swift)](./ios-macos-swift.md) →