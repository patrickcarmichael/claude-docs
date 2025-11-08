---
title: "AI-Code-Tracking-API"
source: "https://docs.cursor.com/de/account/teams/ai-code-tracking-api"
language: "de"
language_name: "German"
---

# AI-Code-Tracking-API
Source: https://docs.cursor.com/de/account/teams/ai-code-tracking-api

Greife auf KI-generierte Code-Analysen für die Repositories deines Teams zu

Greife auf KI-generierte Code-Analysen für die Repositories deines Teams zu. Dazu zählen die KI-Nutzung pro Commit sowie detaillierte, akzeptierte KI-Änderungen.

<Note>
  Die API befindet sich in der ersten Version. Wir erweitern die Funktionen basierend auf Feedback – sag uns, welche Endpunkte du brauchst!
</Note>

* **Verfügbarkeit**: Nur für Enterprise-Teams
* **Status**: Alpha (Response-Formate und Felder können sich ändern)

<div id="authentication">
  ## Authentifizierung
</div>

Alle API-Anfragen erfordern eine Authentifizierung mit einem API-Schlüssel. Diese API verwendet dieselbe Admin-API-Authentifizierung wie andere Endpunkte.

Ausführliche Hinweise zur Authentifizierung findest du unter [Admin-API-Authentifizierung](/de/account/teams/admin-api#authentication).

<div id="base-url">
  ## Basis-URL
</div>

Alle API-Endpunkte verwenden:

```
https://api.cursor.com
```

<div id="rate-limits">
  ## Ratenlimits
</div>

* 5 Anfragen pro Minute pro Team, pro Endpoint

<div id="query-parameters">
  ## Abfrageparameter
</div>

Alle folgenden Endpunkte akzeptieren dieselben Abfrageparameter über den Query-String:

<div className="full-width-table">
  | Parameter   | Typ    | Erforderlich | Beschreibung                                                                                                                                                                                   |                                                                                                                    |
  | :---------- | :----- | :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
  | `startDate` | string | date         | Nein                                                                                                                                                                                           | ISO-Datums-String, das Literal "now" oder relative Tage wie "7d" (entspricht now - 7 days). Standard: now - 7 days |
  | `endDate`   | string | date         | Nein                                                                                                                                                                                           | ISO-Datums-String, das Literal "now" oder relative Tage wie "0d". Standard: now                                    |
  | `page`      | number | Nein         | Seitennummer (1-basiert). Standard: 1                                                                                                                                                          |                                                                                                                    |
  | `pageSize`  | number | Nein         | Ergebnisse pro Seite. Standard: 100, max.: 1000                                                                                                                                                |                                                                                                                    |
  | `user`      | string | Nein         | Optionaler Filter auf einen einzelnen User. Akzeptiert E-Mail (z. B. [developer@company.com](mailto:developer@company.com)), kodierte ID (z. B. user\_abc123...) oder numerische ID (z. B. 42) |                                                                                                                    |
</div>

<Note>
  Responses geben userId als kodierte externe ID mit dem Präfix user\_ zurück. Das ist für die API-Nutzung stabil.
</Note>

<div id="semantics-and-how-metrics-are-computed">
  ## Semantik und Berechnung der Metriken
</div>

* **Quellen**: „TAB“ steht für akzeptierte Inline-Completions; „COMPOSER“ steht für akzeptierte Diffs aus Composer
* **Zeilenmetriken**: tabLinesAdded/Deleted und composerLinesAdded/Deleted werden separat gezählt; nonAiLinesAdded/Deleted werden als max(0, totalLines - AI lines) abgeleitet
* **Privacy-Mode**: Wenn im Client aktiviert, können einige Metadaten (wie fileName) ausgelassen werden
* **Branch-Info**: isPrimaryBranch ist true, wenn der aktuelle Branch dem Standard-Branch des Repos entspricht; kann undefined sein, wenn Repo-Infos nicht verfügbar sind

Du kannst diese Datei scannen, um nachzuvollziehen, wie Commits und Änderungen erkannt und gemeldet werden.

<div id="endpoints">
  ## Endpunkte
</div>

<div id="get-ai-commit-metrics-json-paginated">
  ### AI-Commit-Metriken abrufen (JSON, paginiert)
</div>

Abrufe aggregierter Metriken pro Commit, die Zeilen TAB, COMPOSER und Nicht-AI zuordnen.

```
GET /analytics/ai-code/commits
```

<div id="response">
  #### Antwort
</div>

```typescript  theme={null}
{
  items: AiCommitMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicommitmetric-fields">
  #### AiCommitMetric-Felder
</div>

<div className="full-width-table">
  | Feld                   | Typ     | Beschreibung                              |                                 |
  | :--------------------- | :------ | :---------------------------------------- | ------------------------------- |
  | `commitHash`           | string  | Git-Commit-Hash                           |                                 |
  | `userId`               | string  | Kodierte Benutzer-ID (z. B. user\_abc123) |                                 |
  | `userEmail`            | string  | E-Mail-Adresse des Users                  |                                 |
  | `repoName`             | string  | null                                      | Repositoryname                  |
  | `branchName`           | string  | null                                      | Branchname                      |
  | `isPrimaryBranch`      | boolean | null                                      | Ob dies der primäre Branch ist  |
  | `totalLinesAdded`      | number  | Insgesamt hinzugefügte Zeilen im Commit   |                                 |
  | `totalLinesDeleted`    | number  | Insgesamt gelöschte Zeilen im Commit      |                                 |
  | `tabLinesAdded`        | number  | Über Tab-Completions hinzugefügte Zeilen  |                                 |
  | `tabLinesDeleted`      | number  | Über Tab-Completions gelöschte Zeilen     |                                 |
  | `composerLinesAdded`   | number  | Über Composer hinzugefügte Zeilen         |                                 |
  | `composerLinesDeleted` | number  | Über Composer gelöschte Zeilen            |                                 |
  | `nonAiLinesAdded`      | number  | null                                      | Nicht-AI-Zeilen hinzugefügt     |
  | `nonAiLinesDeleted`    | number  | null                                      | Nicht-AI-Zeilen gelöscht        |
  | `message`              | string  | null                                      | Commit-Nachricht                |
  | `commitTs`             | string  | null                                      | Commit-Zeitstempel (ISO-Format) |
  | `createdAt`            | string  | Ingestionszeitstempel (ISO-Format)        |                                 |
</div>

#### Beispielantwort

```json  theme={null}
{
  "items": [
    {
      "commitHash": "a1b2c3d4",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "repoName": "company/repo",
      "branchName": "main",
      "isPrimaryBranch": true,
      "totalLinesAdded": 120,
      "totalLinesDeleted": 30,
      "tabLinesAdded": 50,
      "tabLinesDeleted": 10,
      "composerLinesAdded": 40,
      "composerLinesDeleted": 5,
      "nonAiLinesAdded": 30,
      "nonAiLinesDeleted": 15,
      "message": "Refactor: Analytics-Client extrahiert"
      "commitTs": "2025-07-30T14:12:03.000Z",
      "createdAt": "2025-07-30T14:12:30.000Z"
    }
  ],
  "totalCount": 42,
  "page": 1,
  "pageSize": 100
}
```

<div id="example-requests">
  #### Beispielanfragen
</div>

**Einfache Anfrage:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=7d&endDate=now&page=1&pageSize=100" \
  -u DEIN_API_KEY:
```

**Nach Benutzer filtern (E-Mail):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/commits?startDate=2025-06-01T00:00:00Z&endDate=now&user=developer@company.com" \
  -u DEIN_API_SCHLÜSSEL:
```

<div id="download-ai-commit-metrics-csv-streaming">
  ### AI-Commit-Metriken herunterladen (CSV, Streaming)
</div>

Commit-Metriken als CSV für große Datenauszüge herunterladen.

```
GET /analytics/ai-code/commits.csv
```

<div id="response">
  #### Antwort
</div>

Header:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV-Spalten
</div>

<div className="full-width-table">
  | Spalte                   | Typ     | Beschreibung                                     |
  | :----------------------- | :------ | :----------------------------------------------- |
  | `commit_hash`            | string  | Git-Commit-Hash                                  |
  | `user_id`                | string  | Kodierte Nutzer-ID                               |
  | `user_email`             | string  | E-Mail-Adresse des Nutzers                       |
  | `repo_name`              | string  | Repository-Name                                  |
  | `branch_name`            | string  | Branch-Name                                      |
  | `is_primary_branch`      | boolean | Ob dies der primäre Branch ist                   |
  | `total_lines_added`      | number  | Insgesamt im Commit hinzugefügte Zeilen          |
  | `total_lines_deleted`    | number  | Insgesamt im Commit gelöschte Zeilen             |
  | `tab_lines_added`        | number  | Über Tab-Vervollständigungen hinzugefügte Zeilen |
  | `tab_lines_deleted`      | number  | Über Tab-Vervollständigungen gelöschte Zeilen    |
  | `composer_lines_added`   | number  | Über Composer hinzugefügte Zeilen                |
  | `composer_lines_deleted` | number  | Über Composer gelöschte Zeilen                   |
  | `non_ai_lines_added`     | number  | Nicht-AI-Zeilen hinzugefügt                      |
  | `non_ai_lines_deleted`   | number  | Nicht-AI-Zeilen gelöscht                         |
  | `message`                | string  | Commit-Nachricht                                 |
  | `commit_ts`              | string  | Commit-Zeitstempel (ISO-Format)                  |
  | `created_at`             | string  | Erfassungszeitpunkt (ISO-Format)                 |
</div>

<div id="sample-csv-output">
  #### Beispielausgabe (CSV)
</div>

```csv  theme={null}
commit_hash,user_id,user_email,repo_name,branch_name,is_primary_branch,total_lines_added,total_lines_deleted,tab_lines_added,tab_lines_deleted,composer_lines_added,composer_lines_deleted,non_ai_lines_added,non_ai_lines_deleted,message,commit_ts,created_at
a1b2c3d4,user_3k9x8q...,developer@company.com,company/repo,main,true,120,30,50,10,40,5,30,15,"Refactor: Analytics-Client ausgelagert",2025-07-30T14:12:03.000Z,2025-07-30T14:12:30.000Z
e5f6g7h8,user_3k9x8q...,developer@company.com,company/repo,feature-branch,false,85,15,30,5,25,3,30,7,"Fehlerbehandlung hinzugefügt",2025-07-30T13:45:21.000Z,2025-07-30T13:45:45.000Z
```

<div id="example-request">
  #### Beispielanfrage
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/commits.csv?startDate=2025-07-01T00:00:00Z&endDate=now&user=user_3k9x8q..." \
  -u DEIN_API_KEY: \
  -o commits.csv
```

<div id="get-ai-code-change-metrics-json-paginated">
  ### AI-Code-Change-Metriken abrufen (JSON, paginiert)
</div>

Ruf detaillierte, akzeptierte AI-Änderungen ab, gruppiert nach deterministischer changeId. Nützlich, um akzeptierte AI-Events unabhängig von Commits zu analysieren.

```
GET /analytics/ai-code/changes
```

<div id="response">
  #### Antwort
</div>

```typescript  theme={null}
{
  items: AiCodeChangeMetric[];
  totalCount: number;
  page: number;
  pageSize: number;
}
```

<div id="aicodechangemetric-fields">
  #### AiCodeChangeMetric-Felder
</div>

<div className="full-width-table">
  | Feld                | Typ    | Beschreibung                                                       |                        |
  | :------------------ | :----- | :----------------------------------------------------------------- | ---------------------- |
  | `changeId`          | string | Deterministische ID der Änderung                                   |                        |
  | `userId`            | string | Kodierte User-ID (z. B. user\_abc123)                              |                        |
  | `userEmail`         | string | E-Mail-Adresse des Users                                           |                        |
  | `source`            | "TAB"  | "COMPOSER"                                                         | Quelle der KI-Änderung |
  | `model`             | string | null                                                               | Verwendetes KI-Modell  |
  | `totalLinesAdded`   | number | Gesamtzahl hinzugefügter Zeilen                                    |                        |
  | `totalLinesDeleted` | number | Gesamtzahl gelöschter Zeilen                                       |                        |
  | `createdAt`         | string | Ingestions-Timestamp (ISO-Format)                                  |                        |
  | `metadata`          | Array  | Dateimetadaten (fileName kann im Privacy-Modus weggelassen werden) |                        |
</div>

<div id="example-response">
  #### Beispiel-Response
</div>

```json  theme={null}
{
  "items": [
    {
      "changeId": "749356201",
      "userId": "user_3k9x8q...",
      "userEmail": "developer@company.com",
      "source": "COMPOSER",
      "model": null,
      "totalLinesAdded": 18,
      "totalLinesDeleted": 4,
      "createdAt": "2025-07-30T15:10:12.000Z",
      "metadata": [
        { "fileName": "src/analytics/report.ts", "fileExtension": "ts", "linesAdded": 12, "linesDeleted": 3 },
        { "fileName": "src/analytics/ui.tsx", "fileExtension": "tsx", "linesAdded": 6, "linesDeleted": 1 }
      ]
    }
  ],
  "totalCount": 128,
  "page": 1,
  "pageSize": 200
}
```

<div id="example-requests">
  #### Beispielanfragen
</div>

**Einfache Anfrage:**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?startDate=14d&endDate=now&page=1&pageSize=200" \
  -u DEIN_API_KEY:
```

**Nach User filtern (kodierte ID):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=user_3k9x8q..." \
  -u DEIN_API_KEY:
```

**Nach Benutzer filtern (E-Mail):**

```bash  theme={null}
curl -X GET "https://api.cursor.com/analytics/ai-code/changes?user=developer@company.com" \
  -u DEIN_API_KEY:
```

<div id="download-ai-code-change-metrics-csv-streaming">
  ### AI-Code-Änderungsmetriken herunterladen (CSV, Streaming)
</div>

Lad Änderungsmetriken als CSV für umfangreiche Datenextraktionen herunter.

```
GET /analytics/ai-code/changes.csv
```

<div id="response">
  #### Antwort
</div>

Headers:

* Content-Type: text/csv; charset=utf-8

<div id="csv-columns">
  #### CSV-Spalten
</div>

<div className="full-width-table">
  | Spalte                | Typ    | Beschreibung                                      |
  | :-------------------- | :----- | :------------------------------------------------ |
  | `change_id`           | string | Deterministische ID der Änderung                  |
  | `user_id`             | string | Kodierte Benutzer-ID                              |
  | `user_email`          | string | E‑Mail-Adresse des Users                          |
  | `source`              | string | Quelle der KI-Änderung (TAB oder COMPOSER)        |
  | `model`               | string | Verwendetes KI-Modell                             |
  | `total_lines_added`   | number | Gesamtzahl hinzugefügter Zeilen                   |
  | `total_lines_deleted` | number | Gesamtzahl gelöschter Zeilen                      |
  | `created_at`          | string | Ingestions-Timestamp (ISO-Format)                 |
  | `metadata_json`       | string | JSON-serialisiertes Array von Metadaten-Einträgen |
</div>

<div id="notes">
  #### Hinweise
</div>

* metadata\_json ist ein JSON-serialisiertes Array von Metadaten-Einträgen (im Datenschutzmodus kann fileName entfallen)
* Beim Verarbeiten von CSV unbedingt gequotete Felder korrekt parsen

<div id="sample-csv-output">
  #### Beispielausgabe (CSV)
</div>

```csv  theme={null}
change_id,user_id,user_email,source,model,total_lines_added,total_lines_deleted,created_at,metadata_json
749356201,user_3k9x8q...,developer@company.com,COMPOSER,gpt-4o,18,4,2025-07-30T15:10:12.000Z,"[{""fileName"":""src/analytics/report.ts"",""fileExtension"":""ts"",""linesAdded"":12,""linesDeleted"":3},{""fileName"":""src/analytics/ui.tsx"",""fileExtension"":""tsx"",""linesAdded"":6,""linesDeleted"":1}]"
749356202,user_3k9x8q...,developer@company.com,TAB,,8,2,2025-07-30T15:08:45.000Z,"[{""fileName"":""src/utils/helpers.ts"",""fileExtension"":""ts"",""linesAdded"":8,""linesDeleted"":2}]"
```

<div id="example-request">
  #### Beispielanfrage
</div>

```bash  theme={null}
curl -L "https://api.cursor.com/analytics/ai-code/changes.csv?startDate=30d&endDate=now" \
  -u DEIN_API_KEY: \
  -o changes.csv
```

<div id="tips">
  ## Tipps
</div>

* Verwende den Parameter `user`, um schnell einen einzelnen User über alle Endpunkte zu filtern
* Für große Datenextraktionen nutze lieber die CSV-Endpunkte — sie streamen serverseitig in Seiten mit 10.000 Einträgen
* `isPrimaryBranch` kann undefined sein, wenn der Client den Default-Branch nicht auflösen konnte
* `commitTs` ist der Commit-Zeitstempel; `createdAt` ist die Zeit, zu der die Daten auf unseren Servern ingestiert wurden
* Einige Felder können fehlen, wenn der Privacy-Mode im Client aktiviert ist

<div id="changelog">
  ## Changelog
</div>

* **Alpha-Release**: Erste Endpunkte für Commits und Änderungen. Response-Formate können sich anhand von Feedback weiterentwickeln

---

← Previous: [Admin-API](./admin-api.md) | [Index](./index.md) | Next: [Analytics](./analytics.md) →