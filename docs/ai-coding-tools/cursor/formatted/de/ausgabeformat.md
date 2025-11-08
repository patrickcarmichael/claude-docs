---
title: "Ausgabeformat"
source: "https://docs.cursor.com/de/cli/reference/output-format"
language: "de"
language_name: "German"
---

# Ausgabeformat
Source: https://docs.cursor.com/de/cli/reference/output-format

Ausgabeschema für Text-, JSON- und Stream-JSON-Formate

Die Cursor Agent CLI bietet mit der Option `--output-format` in Kombination mit `--print` mehrere Ausgabeformate. Dazu zählen strukturierte Formate für die programmgesteuerte Nutzung (`json`, `stream-json`) sowie ein vereinfachtes Textformat für eine gut lesbare Fortschrittsanzeige.

<Note>
  Das Standard-`--output-format` ist `stream-json`. Diese Option ist nur gültig beim Ausgeben (`--print`) oder wenn der Ausgabemodus inferred wird (nicht-TTY-stdout oder per Pipe übergebenes stdin).
</Note>

<div id="json-format">
  ## JSON-Format
</div>

Das `json`-Ausgabeformat gibt bei erfolgreichem Abschluss genau ein JSON-Objekt aus (gefolgt von einem Zeilenumbruch). Deltas und Tool-Ereignisse werden nicht ausgegeben; Text wird zum Endergebnis zusammengefasst.

Im Fehlerfall beendet sich der Prozess mit einem ungleich null gesetzten Rückgabecode und schreibt eine Fehlermeldung nach stderr. In Fehlerfällen wird kein wohlgeformtes JSON-Objekt ausgegeben.

<div id="success-response">
  ### Erfolgs-Response
</div>

Bei Erfolg gibt die CLI ein JSON-Objekt mit der folgenden Struktur aus:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "result": "<vollständiger Assistant-Text>",
  "session_id": "<uuid>",
  "request_id": "<optionale Request-ID>"
}
```

<div class="full-width-table">
  | Feld              | Beschreibung                                                             |
  | ----------------- | ------------------------------------------------------------------------ |
  | `type`            | Immer `"result"` für Terminal-Ergebnisse                                 |
  | `subtype`         | Immer `"success"` bei erfolgreichen Abschlüssen                          |
  | `is_error`        | Immer `false` bei erfolgreichen Antworten                                |
  | `duration_ms`     | Gesamtausführungszeit in Millisekunden                                   |
  | `duration_api_ms` | API-Anfragezeit in Millisekunden (aktuell identisch mit `duration_ms`)   |
  | `result`          | Vollständiger Antworttext des Assistenten (Verkettung aller Text-Deltas) |
  | `session_id`      | Eindeutige Sitzungskennung                                               |
  | `request_id`      | Optionale Anfragekennung (kann entfallen)                                |
</div>

<div id="stream-json-format">
  ## Stream-JSON-Format
</div>

Das `stream-json`-Ausgabeformat gibt zeilenweise JSON (NDJSON) aus. Jede Zeile enthält ein einzelnes JSON-Objekt, das ein Echtzeit-Ereignis während der Ausführung darstellt.

Der Stream endet bei Erfolg mit einem abschließenden `result`-Event. Bei einem Fehler beendet sich der Prozess mit einem von null verschiedenen Code, und der Stream kann ohne abschließendes Event vorzeitig enden; eine Fehlermeldung wird auf stderr geschrieben.

<div id="event-types">
  ### Ereignistypen
</div>

<div id="system-initialization">
  #### Systeminitialisierung
</div>

Zu Beginn jeder Session einmalig ausgegeben:

```json  theme={null}
{
  "type": "system",
  "subtype": "init",
  "apiKeySource": "env|flag|login",
  "cwd": "/absoluter/pfad",
  "session_id": "<uuid>",
  "model": "<Modellanzeige-Name>",
  "permissionMode": "default"
}
```

<Note>
  In Zukunft könnten Felder wie `tools` und `mcp_servers` zu diesem Event hinzukommen.
</Note>

<div id="user-message">
  #### Benutzernachricht
</div>

Enthält den Prompt des Users:

```json  theme={null}
{
  "type": "user",
  "message": {
    "role": "user",
    "content": [{ "type": "text", "text": "<prompt>" }]
  },
  "session_id": "<uuid>"
}
```

<div id="assistant-text-delta">
  #### Assistant-Text-Delta
</div>

Wird mehrfach ausgegeben, während der Assistant seine Antwort generiert. Diese Ereignisse enthalten fortlaufende Textabschnitte:

```json  theme={null}
{
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [{ "type": "text", "text": "<Delta-Chunk>" }]
  },
  "session_id": "<uuid>"
}
```

<Note>
  Verkette alle `message.content[].text`-Werte in der richtigen Reihenfolge, um die vollständige Antwort des Assistenten zu rekonstruieren.
</Note>

<div id="tool-call-events">
  #### Tool-Call-Ereignisse
</div>

Tool-Calls werden mit Start- und Abschlussereignissen protokolliert:

**Tool-Call gestartet:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "started",
  "call_id": "<string-id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" }
    }
  },
  "session_id": "<uuid>"
}
```

**Toolaufruf abgeschlossen:**

```json  theme={null}
{
  "type": "tool_call",
  "subtype": "completed",
  "call_id": "<string id>",
  "tool_call": {
    "readToolCall": {
      "args": { "path": "file.txt" },
      "result": {
        "success": {
          "content": "Dateiinhalt...",
          "isEmpty": false,
          "exceededLimit": false,
          "totalLines": 54,
          "totalChars": 1254
        }
      }
    }
  },
  "session_id": "<uuid>"
}
```

<div id="tool-call-types">
  #### Tool-Call-Typen
</div>

**Read-File-Tool:**

* **Gestartet**: `tool_call.readToolCall.args` enthält `{ "path": "file.txt" }`
* **Abgeschlossen**: `tool_call.readToolCall.result.success` enthält Dateimetadaten und Inhalt

**Write-File-Tool:**

* **Gestartet**: `tool_call.writeToolCall.args` enthält `{ "path": "file.txt", "fileText": "content...", "toolCallId": "id" }`
* **Abgeschlossen**: `tool_call.writeToolCall.result.success` enthält `{ "path": "/absolute/path", "linesCreated": 19, "fileSize": 942 }`

**Weitere Tools:**

* Können die Struktur `tool_call.function` mit `{ "name": "tool_name", "arguments": "..." }` verwenden

<div id="terminal-result">
  #### Terminal-Resultat
</div>

Das letzte Event, das bei erfolgreichem Abschluss emittiert wird:

```json  theme={null}
{
  "type": "result",
  "subtype": "success",
  "duration_ms": 1234,
  "duration_api_ms": 1234,
  "is_error": false,
  "result": "<vollständiger Assistant-Text>",
  "session_id": "<uuid>",
  "request_id": "<optionale Request-ID>"
}
```

<div id="example-sequence">
  ### Beispielsequenz
</div>

Hier ist eine typische NDJSON-Sequenz, die den üblichen Ablauf der Ereignisse zeigt:

```json  theme={null}
{"type":"system","subtype":"init","apiKeySource":"login","cwd":"/Users/user/project","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","model":"Claude 4 Sonnet","permissionMode":"default"}
{"type":"user","message":{"role":"user","content":[{"type":"text","text":"Lies die README.md und erstelle eine Zusammenfassung"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"Ich werde "}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":"die README.md lesen"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01NnjaR886UcE8whekg2MGJd","tool_call":{"readToolCall":{"args":{"path":"README.md"},"result":{"success":{"content":"# Projekt\n\nDies ist ein Beispielprojekt...","isEmpty":false,"exceededLimit":false,"totalLines":54,"totalChars":1254}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"assistant","message":{"role":"assistant","content":[{"type":"text","text":" und eine Zusammenfassung erstellen"}]},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"started","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README-Zusammenfassung\n\nDieses Projekt enthält...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"tool_call","subtype":"completed","call_id":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv","tool_call":{"writeToolCall":{"args":{"path":"summary.txt","fileText":"# README-Zusammenfassung\n\nDieses Projekt enthält...","toolCallId":"toolu_vrtx_01Q3VHVnWFSKygaRPT7WDxrv"},"result":{"success":{"path":"/Users/user/project/summary.txt","linesCreated":19,"fileSize":942}}}},"session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff"}
{"type":"result","subtype":"success","duration_ms":5234,"duration_api_ms":5234,"is_error":false,"result":"Ich werde die README.md lesen und eine Zusammenfassung erstellen","session_id":"c6b62c6f-7ead-4fd6-9922-e952131177ff","request_id":"10e11780-df2f-45dc-a1ff-4540af32e9c0"}
```

<div id="text-format">
  ## Textformat
</div>

Das Ausgabeformat `text` liefert einen vereinfachten, gut lesbaren Stream von Agent-Aktionen. Statt detaillierter JSON-Events gibt es prägnante Textbeschreibungen dessen aus, was der Agent in Echtzeit tut.

Dieses Format ist hilfreich, um den Fortschritt des Agents zu überwachen, ohne den Overhead beim Parsen strukturierter Daten – ideal für Logging, Debugging oder einfaches Fortschritts-Tracking.

<div id="example-output">
  ### Beispielausgabe
</div>

```
Datei gelesen
Datei bearbeitet
Terminal-Befehl ausgeführt
Neue Datei erstellt
```

Jede Aktion erscheint in einer neuen Zeile, sobald der Agent sie ausführt, und liefert sofortiges Feedback zu seinem Fortschritt bei der Aufgabe.

<div id="implementation-notes">
  ## Hinweise zur Implementierung
</div>

* Jedes Event wird als einzelne Zeile mit `\n` beendet
* `thinking`-Events werden im Print-Modus unterdrückt und erscheinen in keinem der Ausgabeformate
* Feld-Erweiterungen können im Laufe der Zeit rückwärtskompatibel erfolgen (Consumers sollten unbekannte Felder ignorieren)
* Das Stream-Format liefert Echtzeit-Updates, während das JSON-Format bis zum Abschluss wartet und erst dann Ergebnisse ausgibt
* Alle `assistant`-Nachrichten-Deltas zusammenfügen, um die vollständige Antwort zu rekonstruieren
* Tool-Call-IDs können verwendet werden, um Start- und Abschluss-Events zu korrelieren
* Session-IDs bleiben während einer einzelnen Agent-Ausführung konsistent

---

← Previous: [Konfiguration](./konfiguration.md) | [Index](./index.md) | Next: [Parameter](./parameter.md) →