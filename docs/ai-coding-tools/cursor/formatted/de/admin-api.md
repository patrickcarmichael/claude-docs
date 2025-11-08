---
title: "Admin-API"
source: "https://docs.cursor.com/de/account/teams/admin-api"
language: "de"
language_name: "German"
---

# Admin-API
Source: https://docs.cursor.com/de/account/teams/admin-api

Greif per API auf Teammetriken, Nutzungsdaten und Ausgabeninformationen zu

Die Admin-API gibt dir programmgesteuerten Zugriff auf die Daten deines Teams, darunter Mitgliederinfos, Nutzungsmetriken und Ausgabendetails. Bau eigene Dashboards und Monitoring-Tools oder integrier sie in bestehende Workflows.

<Note>
  Die API ist in ihrer ersten Version. Wir erweitern die Funktionen basierend auf Feedback – sag uns, welche Endpunkte du brauchst!
</Note>

<div id="authentication">
  ## Authentifizierung
</div>

Alle API-Requests erfordern eine Authentifizierung mit einem API-Key. Nur Team-Admins können API-Keys erstellen und verwalten.

API-Keys sind an die Organisation gebunden, für alle Admins sichtbar und bleiben unabhängig vom Kontostatus der ursprünglichen Erstellerperson.

<div id="creating-an-api-key">
  ### Erstellen eines API-Schlüssels
</div>

1. Navigier zu **cursor.com/dashboard** → Tab **Settings** → **Cursor Admin API Keys**
2. Klick auf **Create New API Key**
3. Gib deinem Schlüssel einen aussagekräftigen Namen (z. B. „Usage Dashboard Integration“)
4. Kopier den generierten Schlüssel sofort – du wirst ihn nicht wieder sehen

Format: `key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

<div id="using-your-api-key">
  ### Verwende deinen API‑Schlüssel
</div>

Verwende deinen API‑Schlüssel als Benutzernamen bei der Basic-Authentifizierung:

**Mit curl und Basic Auth:**

```bash  theme={null}
curl https://api.cursor.com/{route} -u API_KEY:
```

**Oder setz den Authorization-Header direkt:**

```bash  theme={null}
Authorization: Basic {base64_encode('API_KEY:')}
```

<div id="base-url">
  ## Basis-URL
</div>

Alle API-Endpunkte verwenden:

```
https://api.cursor.com
```

<div id="endpoints">
  ## Endpoints
</div>

<div id="get-team-members">
  ### Teammitglieder abrufen
</div>

Ruf alle Teammitglieder und ihre Details ab.

```
GET /teams/members
```

#### Antwort

Gibt ein Array von Teammitgliedern (Objekten) zurück:

```typescript  theme={null}
{
  teamMembers: {
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
  }[];
}
```

#### Beispielantwort

```json  theme={null}
{
  "teamMembers": [
    {
      "name": "Alex",
      "email": "developer@company.com",
      "role": "Member"
    },
    {
      "name": "Sam",
      "email": "admin@company.com",
      "role": "Owner"
    }
  ]
}

```

#### Beispielanfrage

```bash  theme={null}
curl -X GET https://api.cursor.com/teams/members \
  -u DEIN_API_KEY:
```

<div id="get-daily-usage-data">
  ### Tägliche Nutzungsdaten abrufen
</div>

Hol dir detaillierte tägliche Nutzungsmetriken für dein Team für einen bestimmten Zeitraum. Liefert Einblicke in Code-Änderungen, die Nutzung von KI-Unterstützung und Akzeptanzraten.

```
POST /teams/daily-usage-data
```

#### Request Body

<div className="full-width-table">
  | Parameter   | Typ    | Erforderlich | Beschreibung                      |
  | :---------- | :----- | :----------- | :-------------------------------- |
  | `startDate` | number | Ja           | Startdatum in Epoch-Millisekunden |
  | `endDate`   | number | Ja           | Enddatum in Epoch-Millisekunden   |
</div>

<Note>
  Der Datumsbereich darf 90 Tage nicht überschreiten. Für längere Zeiträume bitte mehrere Anfragen stellen.
</Note>

#### Antwort

```typescript  theme={null}
{
  data: {
    date: number;
    isActive: boolean;
    totalLinesAdded: number;
    totalLinesDeleted: number;
    acceptedLinesAdded: number;
    acceptedLinesDeleted: number;
    totalApplies: number;
    totalAccepts: number;
    totalRejects: number;
    totalTabsShown: number;
    totalTabsAccepted: number;
    composerRequests: number;
    chatRequests: number;
    agentRequests: number;
    cmdkUsages: number;
    subscriptionIncludedReqs: number;
    apiKeyReqs: number;
    usageBasedReqs: number;
    bugbotUsages: number;
    mostUsedModel: string;
    applyMostUsedExtension?: string;
    tabMostUsedExtension?: string;
    clientVersion?: string;
    email?: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields">
  #### Antwortfelder
</div>

<div className="full-width-table">
  | Feld                       | Beschreibung                                          |
  | :------------------------- | :---------------------------------------------------- |
  | `date`                     | Datum in Epoch-Millisekunden                          |
  | `isActive`                 | Nutzer an diesem Tag aktiv                            |
  | `totalLinesAdded`          | Hinzugefügte Codezeilen                               |
  | `totalLinesDeleted`        | Gelöschte Codezeilen                                  |
  | `acceptedLinesAdded`       | Hinzugefügte Zeilen aus akzeptierten KI-Vorschlägen   |
  | `acceptedLinesDeleted`     | Gelöschte Zeilen aus akzeptierten KI-Vorschlägen      |
  | `totalApplies`             | Apply-Operationen                                     |
  | `totalAccepts`             | Akzeptierte Vorschläge                                |
  | `totalRejects`             | Abgelehnte Vorschläge                                 |
  | `totalTabsShown`           | Angezeigte Tab-Vervollständigungen                    |
  | `totalTabsAccepted`        | Akzeptierte Tab-Vervollständigungen                   |
  | `composerRequests`         | Composer-Anfragen                                     |
  | `chatRequests`             | Chat-Anfragen                                         |
  | `agentRequests`            | Agent-Anfragen                                        |
  | `cmdkUsages`               | Nutzungen der Befehlspalette (Cmd+K)                  |
  | `subscriptionIncludedReqs` | Inklusive Abo-Anfragen                                |
  | `apiKeyReqs`               | API-Schlüssel-Anfragen                                |
  | `usageBasedReqs`           | Nutzungsbasierte (Pay-per-Use) Anfragen               |
  | `bugbotUsages`             | Nutzungen der Bug-Erkennung                           |
  | `mostUsedModel`            | Am häufigsten verwendetes KI-Modell                   |
  | `applyMostUsedExtension`   | Am häufigsten verwendete Dateierweiterung bei Applies |
  | `tabMostUsedExtension`     | Am häufigsten verwendete Dateierweiterung bei Tabs    |
  | `clientVersion`            | Cursor-Version                                        |
  | `email`                    | Nutzer-E-Mail                                         |
</div>

<div id="example-response">
  #### Beispiel-Antwort
</div>

```json  theme={null}
{
  "data": [
    {
      "date": 1710720000000,
      "isActive": true,
      "totalLinesAdded": 1543,
      "totalLinesDeleted": 892,
      "acceptedLinesAdded": 1102,
      "acceptedLinesDeleted": 645,
      "totalApplies": 87,
      "totalAccepts": 73,
      "totalRejects": 14,
      "totalTabsShown": 342,
      "totalTabsAccepted": 289,
      "composerRequests": 45,
      "chatRequests": 128,
      "agentRequests": 12,
      "cmdkUsages": 67,
      "subscriptionIncludedReqs": 180,
      "apiKeyReqs": 0,
      "usageBasedReqs": 5,
      "bugbotUsages": 3,
      "mostUsedModel": "gpt-4",
      "applyMostUsedExtension": ".tsx",
      "tabMostUsedExtension": ".ts",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    },
    {
      "date": 1710806400000,
      "isActive": true,
      "totalLinesAdded": 2104,
      "totalLinesDeleted": 1203,
      "acceptedLinesAdded": 1876,
      "acceptedLinesDeleted": 987,
      "totalApplies": 102,
      "totalAccepts": 91,
      "totalRejects": 11,
      "totalTabsShown": 456,
      "totalTabsAccepted": 398,
      "composerRequests": 67,
      "chatRequests": 156,
      "agentRequests": 23,
      "cmdkUsages": 89,
      "subscriptionIncludedReqs": 320,
      "apiKeyReqs": 15,
      "usageBasedReqs": 0,
      "bugbotUsages": 5,
      "mostUsedModel": "claude-3-opus",
      "applyMostUsedExtension": ".py",
      "tabMostUsedExtension": ".py",
      "clientVersion": "0.25.1",
      "email": "developer@company.com"
    }
  ],
  "period": {
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }
}
```

#### Beispielanfrage

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/daily-usage-data \
  -u DEIN_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1710720000000,
    "endDate": 1710892800000
  }'
```

<div id="get-spending-data">
  ### Ausgabendaten abrufen
</div>

Ruf Ausgabendaten für den aktuellen Kalendermonat mit Suche, Sortierung und Paginierung ab.

```
POST /teams/spend
```

#### Request-Body

<div className="full-width-table">
  | Parameter       | Typ    | Erforderlich | Beschreibung                                                    |
  | :-------------- | :----- | :----------- | :-------------------------------------------------------------- |
  | `searchTerm`    | string | Nein         | Suche in Benutzernamen und E-Mail-Adressen                      |
  | `sortBy`        | string | Nein         | Sortieren nach: `amount`, `date`, `user`. Standardmäßig: `date` |
  | `sortDirection` | string | Nein         | Sortierrichtung: `asc`, `desc`. Standardmäßig: `desc`           |
  | `page`          | number | Nein         | Seitennummer (1-indiziert). Standardmäßig: `1`                  |
  | `pageSize`      | number | Nein         | Ergebnisse pro Seite                                            |
</div>

#### Antwort

```typescript  theme={null}
{
  teamMemberSpend: {
    spendCents: number;
    fastPremiumRequests: number;
    name: string;
    email: string;
    role: 'owner' | 'member' | 'free-owner';
    hardLimitOverrideDollars: number;
  }[];
  subscriptionCycleStart: number;
  totalMembers: number;
  totalPages: number;
}
```

<div id="response-fields">
  #### Antwortfelder
</div>

<div className="full-width-table">
  | Feld                       | Beschreibung                                         |
  | :------------------------- | :--------------------------------------------------- |
  | `spendCents`               | Gesamtausgaben in Cent                               |
  | `fastPremiumRequests`      | Schnell-Premium-Modellanfragen                       |
  | `name`                     | Name des Mitglieds                                   |
  | `email`                    | E-Mail des Mitglieds                                 |
  | `role`                     | Teamrolle                                            |
  | `hardLimitOverrideDollars` | Benutzerdefinierte Überschreibung des Ausgabenlimits |
  | `subscriptionCycleStart`   | Beginn des Abrechnungszyklus (Epoch-Millisekunden)   |
  | `totalMembers`             | Gesamtzahl der Teammitglieder                        |
  | `totalPages`               | Gesamtzahl der Seiten                                |
</div>

<div id="example-response">
  #### Beispiel-Antwort
</div>

```json  theme={null}
{
  "teamMemberSpend": [
    {
      "spendCents": 2450,
      "fastPremiumRequests": 1250,
      "name": "Alex",
      "email": "developer@company.com",
      "role": "member",
      "hardLimitOverrideUSDR": 100
    },
    {
      "spendCents": 1875,
      "fastPremiumRequests": 980,
      "name": "Sam",
      "email": "admin@company.com",
      "role": "owner",
      "hardLimitOverrideUSDR": 0
    },
  ],
  "subscriptionCycleStart": 1708992000000,
  "totalMembers": 15,
  "totalPages": 1
}
```

<div id="example-requests">
  #### Beispielanfragen
</div>

**Grundlegende Ausgabendaten:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Bestimmten User mit Pagination suchen:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/spend \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "searchTerm": "alex@company.com",
    "page": 2,
    "pageSize": 25
  }'
```

<div id="get-usage-events-data">
  ### Nutzungsereignisse abrufen
</div>

Hol dir detaillierte Nutzungsereignisse für dein Team mit umfassenden Filter-, Such- und Paginierungsoptionen. Dieser Endpoint liefert granulare Einblicke in einzelne API-Aufrufe, die Nutzung von Modellen, den Tokenverbrauch und die Kosten.

```
POST /teams/filtered-usage-events
```

#### Request-Body

<div className="full-width-table">
  | Parameter   | Typ    | Erforderlich | Beschreibung                                    |
  | :---------- | :----- | :----------- | :---------------------------------------------- |
  | `startDate` | number | Nein         | Startdatum in Unix-Epoche (Millisekunden)       |
  | `endDate`   | number | Nein         | Enddatum in Unix-Epoche (Millisekunden)         |
  | `userId`    | number | Nein         | Nach bestimmter User-ID filtern                 |
  | `page`      | number | Nein         | Seitennummer (1-basiert). Standard: `1`         |
  | `pageSize`  | number | Nein         | Anzahl der Ergebnisse pro Seite. Standard: `10` |
  | `email`     | string | Nein         | Nach der E-Mail-Adresse des Users filtern       |
</div>

#### Antwort

```typescript  theme={null}
{
  totalUsageEventsCount: number;
  pagination: {
    numPages: number;
    currentPage: number;
    pageSize: number;
    hasNextPage: boolean;
    hasPreviousPage: boolean;
  };
  usageEvents: {
    timestamp: string;
    model: string;
    kind: string;
    maxMode: boolean;
    requestsCosts: number;
    isTokenBasedCall: boolean;
    tokenUsage?: {
      inputTokens: number;
      outputTokens: number;
      cacheWriteTokens: number;
      cacheReadTokens: number;
      totalCents: number;
    };
    isFreeBugbot: boolean;
    userEmail: string;
  }[];
  period: {
    startDate: number;
    endDate: number;
  };
}
```

<div id="response-fields-explained">
  #### Erklärung der Response-Felder
</div>

<div className="full-width-table">
  | Field                   | Description                                                               |
  | :---------------------- | :------------------------------------------------------------------------ |
  | `totalUsageEventsCount` | Gesamtzahl der Nutzungsereignisse, die der Abfrage entsprechen            |
  | `pagination`            | Paginierungsmetadaten zur Navigation durch die Ergebnisse                 |
  | `timestamp`             | Ereigniszeitstempel in Millisekunden seit Epoch                           |
  | `model`                 | Für die Anfrage verwendetes KI-Modell                                     |
  | `kind`                  | Nutzungskategorie (z. B. „Usage-based“, „Included in Business“)           |
  | `maxMode`               | Ob der Max‑Modus aktiviert war                                            |
  | `requestsCosts`         | Kosten in Request‑Einheiten                                               |
  | `isTokenBasedCall`      | True, wenn das Ereignis nutzungsbasiert abgerechnet wird                  |
  | `tokenUsage`            | Detaillierter Token‑Verbrauch (verfügbar, wenn isTokenBasedCall true ist) |
  | `isFreeBugbot`          | Ob dies eine kostenlose Bugbot‑Nutzung war                                |
  | `userEmail`             | E‑Mail des Users, der die Anfrage gestellt hat                            |
  | `period`                | Datumsbereich der abgefragten Daten                                       |
</div>

<div id="example-response">
  #### Beispiel-Antwort
</div>

```json  theme={null}
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "timestamp": "1750979225854",
      "model": "claude-4-opus",
      "kind": "Nutzungsbasiert",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750979173824",
      "model": "claude-4-opus",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 10,
      "isTokenBasedCall": true,
      "tokenUsage": {
        "inputTokens": 5805,
        "outputTokens": 311,
        "cacheWriteTokens": 11964,
        "cacheReadTokens": 0,
        "totalCents": 40.16699999999999
      },
      "isFreeBugbot": false,
      "userEmail": "developer@company.com"
    },
    {
      "timestamp": "1750978339901",
      "model": "claude-4-sonnet-thinking",
      "kind": "In Business enthalten"
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isFreeBugbot": false,
      "userEmail": "admin@company.com"
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

<div id="example-requests">
  #### Beispielanfragen
</div>

**Alle Nutzungsereignisse mit Standard-Paginierung abrufen:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Nach Datumsbereich und bestimmtem Nutzer filtern:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "email": "developer@company.com",
    "page": 1,
    "pageSize": 25
  }'
```

**Nutzungsereignisse für einen bestimmten User mit individueller Pagination abrufen:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/filtered-usage-events \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 12345,
    "page": 2,
    "pageSize": 50
  }'
```

<div id="set-user-spend-limit">
  ### Ausgabenlimit pro Nutzer festlegen
</div>

Lege Ausgabenlimits für einzelne Teammitglieder fest. So kannst du steuern, wie viel jede Person für die KI-Nutzung in deinem Team ausgeben darf.

```
POST /teams/user-spend-limit
```

<Note>
  **Rate-Limit:** 60 Anfragen pro Minute pro Team
</Note>

#### Request-Body

<div className="full-width-table">
  | Parameter           | Type   | Required | Description                                                          |
  | :------------------ | :----- | :------- | :------------------------------------------------------------------- |
  | `userEmail`         | string | Yes      | E-Mail-Adresse des Teammitglieds                                     |
  | `spendLimitDollars` | number | Yes      | Ausgabenlimit in US-Dollar (nur ganze Zahlen, keine Dezimalstellen). |
</div>

<Note>
  * Der Nutzer muss bereits Mitglied deines Teams sein
  * Es werden nur ganze Zahlen akzeptiert (keine Dezimalbeträge)
  * Wenn `spendLimitDollars` auf 0 gesetzt wird, ist das Limit \$0
</Note>

#### Response

Gibt eine standardisierte Antwort zurück, die Erfolg oder Fehler anzeigt:

```typescript  theme={null}
{
  outcome: 'success' | 'error';
  message: string;
}
```

<div id="example-responses">
  #### Beispielantworten
</div>

**Limit erfolgreich gesetzt:**

```json  theme={null}
{
  "outcome": "success",
  "message": "Ausgabenlimit von $100 für den User developer@company.com festgelegt"
}
```

**Fehlermeldung:**

```json  theme={null}
{
  "outcome": "error",
  "message": "Ungültiges E‑Mail-Format"
}
```

<div id="example-requests">
  #### Beispielanfragen
</div>

**Ausgabenlimit festlegen:**

```bash  theme={null}
curl -X POST https://api.cursor.com/teams/user-spend-limit \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userEmail": "developer@company.com",
    "spendLimitDollars": 100
  }'
```

<div id="repo-blocklists-api">
  ### Repo-Blocklists-API
</div>

Füge Repos hinzu und nutze Muster, um zu verhindern, dass Dateien oder Verzeichnisse für dein Team indexiert oder als Kontext verwendet werden.

<div id="get-team-repo-blocklists">
  #### Team-Repo-Blocklists abrufen
</div>

Alle für dein Team konfigurierten Repository-Blocklists abrufen.

```
GET /settings/repo-blocklists/repos
```

##### Antwort

Gibt ein Array von Blocklist-Objekten für Repositories zurück:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

##### Beispielantwort

```json  theme={null}
{
  "repos": [
    {
      "id": "repo_123",
      "url": "https://github.com/company/sensitive-repo",
      "patterns": ["*.env", "config/*", "secrets/**"]
    },
    {
      "id": "repo_456",
      "url": "https://github.com/company/internal-tools",
      "patterns": ["*"]
    }
  ]
}
```

<div id="example-request">
  ##### Beispielanfrage
</div>

```bash  theme={null}
curl -X GET https://api.cursor.com/settings/repo-blocklists/repos \
  -u DEIN_API_KEY:
```

<div id="upsert-repo-blocklists">
  #### Repo-Blocklisten updaten/erstellen
</div>

Ersetze bestehende Repository-Blocklisten für die angegebenen Repos.
*Hinweis: Dieser Endpunkt überschreibt nur die Muster für die angegebenen Repositories. Alle anderen Repos bleiben unverändert.*

```
POST /settings/repo-blocklists/repos/upsert
```

<div id="request-body">
  ##### Request Body
</div>

| Parameter | Typ   | Erforderlich | Beschreibung                                  |
| --------- | ----- | ------------ | --------------------------------------------- |
| repos     | array | Ja           | Array von Blocklist-Objekten für Repositories |

Jedes Repository-Objekt muss Folgendes enthalten:

| Feld     | Typ       | Erforderlich | Beschreibung                                                             |
| -------- | --------- | ------------ | ------------------------------------------------------------------------ |
| url      | string    | Ja           | Repository-URL, die blocklistet werden soll                              |
| patterns | string\[] | Ja           | Array von zu blockierenden Dateimustern (Glob-Muster werden unterstützt) |

<div id="response">
  ##### Response
</div>

Gibt die aktualisierte Liste der Repository-Blocklists zurück:

```typescript  theme={null}
{
  repos: {
    id: string;
    url: string;
    patterns: string[];
  }[];
}
```

<div id="example-request">
  ##### Beispielanfrage
</div>

```bash  theme={null}
curl -X POST https://api.cursor.com/settings/repo-blocklists/repos/upsert \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "repos": [
      {
        "url": "https://github.com/company/sensitive-repo",
        "patterns": ["*.env", "config/*", "secrets/**"]
      },
      {
        "url": "https://github.com/company/internal-tools", 
        "patterns": ["*"]
      }
    ]
  }'
```

<div id="delete-repo-blocklist">
  #### Repo-Blocklist löschen
</div>

Entferne ein bestimmtes Repository aus der Blocklist.

```
DELETE /settings/repo-blocklists/repos/:repoId
```

<div id="parameters">
  ##### Parameter
</div>

| Parameter | Typ    | Erforderlich | Beschreibung                                    |
| --------- | ------ | ------------ | ----------------------------------------------- |
| repoId    | string | Ja           | ID der zu löschenden Blocklist des Repositories |

##### Antwort

Gibt bei erfolgreichem Löschen 204 No Content zurück.

<div id="example-request">
  ##### Beispielanfrage
</div>

```bash  theme={null}
curl -X DELETE https://api.cursor.com/settings/repo-blocklists/repos/repo_123 \
  -u DEIN_API_SCHLÜSSEL:
```

<div id="pattern-examples">
  #### Beispielmuster
</div>

Häufige Muster für die Blockliste:

* `*` - gesamtes Repository blocken
* `*.env` - alle .env-Dateien blocken
* `config/*` - alle Dateien im Verzeichnis config blocken
* `**/*.secret` - alle .secret-Dateien in beliebigen Unterverzeichnissen blocken
* `src/api/keys.ts` - eine bestimmte Datei blocken

---

← Previous: [Preise](./preise.md) | [Index](./index.md) | Next: [AI-Code-Tracking-API](./ai-code-tracking-api.md) →