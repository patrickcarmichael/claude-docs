# Agent-Sicherheit

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-code-review.md)

---

# Agent-Sicherheit
Source: https://docs.cursor.com/de/account/agent-security

Sicherheitsaspekte bei der Verwendung von Cursor Agent

Prompt-Injection, KI-Halluzinationen und andere Probleme können dazu führen, dass sich KI unerwartet und potenziell bösartig verhält. Während wir weiter daran arbeiten, Prompt-Injection auf einer grundlegenderen Ebene zu lösen, bestehen unsere wichtigsten Schutzmechanismen in Cursor-Produkten aus Leitplanken für das Handeln eines Agents – einschließlich der standardmäßigen Anforderung einer manuellen Bestätigung für sensible Aktionen. Ziel dieses Dokuments ist es, unsere Leitplanken zu erklären und was du von ihnen erwarten kannst.

Alle unten aufgeführten Steuerungen und Verhaltensweisen sind unsere Standard- und empfohlenen Einstellungen.

<div id="first-party-tool-calls">
  ## First-party-Toolaufrufe
</div>

Cursor wird mit Tools ausgeliefert, die dem Agent helfen, dir beim Coden zu helfen. Dazu gehören Dateilesen, Bearbeitungen, das Ausführen von Terminalbefehlen, die Suche im Web nach Doku und mehr.

Lese-Tools erfordern keine Freigabe (z. B. das Lesen von Dateien, die Suche im Code). Du kannst [.cursorignore](/de/context/ignore-files) verwenden, um dem Agent den Zugriff auf bestimmte Dateien komplett zu blockieren; ansonsten sind Lesevorgänge in der Regel ohne Freigabe erlaubt. Für Aktionen, die das Risiko der Exfiltration sensibler Daten bergen, verlangen wir eine explizite Freigabe.

Das Ändern von Dateien im aktuellen Workspace erfordert keine explizite Freigabe, mit einigen Ausnahmen. Wenn ein Agent Dateien ändert, werden die Änderungen sofort auf die Festplatte geschrieben. Wir empfehlen, Cursor in versionierten Workspaces zu nutzen, sodass Dateiinhalte jederzeit zurückgesetzt werden können. Wir verlangen eine explizite Freigabe, bevor Dateien geändert werden, die die Konfiguration unserer IDE/CLI anpassen, z. B. die Workspace-Einstellungsdatei des Editors. Wenn bei dir ein automatisches Neuladen bei Dateänderungen aktiv ist, beachte, dass Agent-Änderungen an Dateien eine automatische Ausführung auslösen können, bevor du sie prüfen konntest.

Jeder vom Agent vorgeschlagene Terminalbefehl erfordert standardmäßig eine Freigabe. Wir empfehlen, jeden Befehl zu prüfen, bevor der Agent ihn ausführt. Wenn du das Risiko akzeptierst, kannst du dem Agent erlauben, alle Befehle ohne Freigabe auszuführen. Wir bieten in Cursor eine [Allowlist](/de/agent/tools) an, betrachten sie jedoch nicht als Sicherheitskontrolle. Manche Nutzer erlauben bestimmte Befehle, aber das ist ein Best-Effort-System, und Umgehungen sind möglich. Wir empfehlen nicht „Run Everything“, da damit alle konfigurierten Allowlists umgangen werden.

<div id="third-party-tool-calls">
  ## Aufrufe von Drittanbieter-Tools
</div>

Cursor ermöglicht das Einbinden externer Tools über [MCP](/de/context/mcp). Alle MCP-Verbindungen von Drittanbietern müssen ausdrücklich von dir genehmigt werden. Sobald du eine MCP-Verbindung genehmigt hast, muss in Agent Mode standardmäßig jeder vorgeschlagene Tool-Aufruf für jede externe MCP-Integration vor der Ausführung ausdrücklich bestätigt werden.

<div id="network-requests">
  ## Netzwerk-Anfragen
</div>

Netzwerk-Anfragen können von Angreifern genutzt werden, um Daten zu exfiltrieren. Wir unterstützen derzeit keine First‑Party‑Tools, die Netzwerk-Anfragen an andere Hosts als eine sehr kleine, ausgewählte Gruppe (z. B. GitHub) stellen, keine expliziten Linkabrufe und nur Websuche mit einer ausgewählten Gruppe von Anbietern. Beliebige Agenten‑Netzwerk-Anfragen werden in den Standardeinstellungen verhindert.

<div id="workspace-trust">
  ## Workspace-Trust
</div>

Die Cursor-IDE unterstützt die standardmäßige [Workspace-Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)-Funktion, die *deaktiviert* ist. Workspace-Trust zeigt dir beim Öffnen eines neuen Workspaces einen Dialog, in dem du zwischen normalem und eingeschränktem Modus wählen kannst. Der eingeschränkte Modus deaktiviert AI und andere Features, für die Nutzer Cursor typischerweise verwenden. Wir empfehlen dafür andere Tools, z. B. einen einfachen Texteditor, wenn du mit Repos arbeitest, denen du nicht vertraust.

Workspace-Trust kann in den Benutzereinstellungen aktiviert werden, indem du diese Schritte ausführst:

1. Öffne deine user settings.json-Datei
2. Füge die folgende Konfiguration hinzu:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Diese Einstellung kann auch organisationsweit über Mobile-Device-Management-(MDM)-Lösungen erzwungen werden.

<div id="responsible-disclosure">
  ## Verantwortungsvolle Offenlegung
</div>

Wenn du glaubst, eine Sicherheitslücke in Cursor gefunden zu haben, folge bitte der Anleitung auf unserer GitHub-Sicherheitsseite und reiche den Bericht dort ein. Wenn du GitHub nicht nutzen kannst, erreichst du uns auch unter [security@cursor.com](mailto:security@cursor.com).

Wir sagen zu, Meldungen über Sicherheitslücken innerhalb von 5 Werktagen zu bestätigen und sie so schnell wie möglich zu bearbeiten. Wir veröffentlichen die Ergebnisse als Sicherheitshinweise auf unserer GitHub-Sicherheitsseite. Kritische Vorfälle werden sowohl auf der GitHub-Sicherheitsseite als auch per E-Mail an alle Nutzer kommuniziert.



# Abrechnung
Source: https://docs.cursor.com/de/account/billing

Verwaltung von Cursor-Abos, Erstattungen und Rechnungen 

<div id="how-do-i-access-billing-settings">
  ### Wie greife ich auf die Abrechnungseinstellungen zu?
</div>

Greif über das [Dashboard](https://cursor.com/dashboard) auf das Abrechnungsportal zu, indem du in deinem Dashboard auf „Billing“ klickst. Dadurch öffnet sich ein sicheres Portal für alle Abrechnungsaufgaben.

<div id="what-are-cursors-billing-cycles">
  ### Wie laufen Cursors Abrechnungszyklen?
</div>

Abrechnungszyklen laufen monatlich oder jährlich und beginnen an deinem Abo-Startdatum. Team-Accounts werden pro Sitzplatz abgerechnet, mit anteiliger Verrechnung für neue Mitglieder.

<div id="how-do-seats-work-for-teams-accounts">
  ### Wie funktionieren Sitzplätze bei Team-Accounts?
</div>

Team-Accounts berechnen pro Sitzplatz (einer pro Teammitglied). Wenn du Mitglieder mitten im Zyklus hinzufügst, zahlst du nur für die verbleibende Zeit. Wenn ein Mitglied Credits genutzt hat und entfernt wird, bleibt sein Sitz bis zum Ende des Abrechnungszyklus belegt – anteilige Rückerstattungen gibt’s nicht. Team-Admins können Sitze über das Dashboard verwalten.

<div id="can-i-switch-between-monthly-and-annual-billing">
  ### Kann ich zwischen monatlicher und jährlicher Abrechnung wechseln?
</div>

Ja! So geht’s:

**Pro-Plan**

1. Geh zum Cursor-[Dashboard](https://cursor.com/dashboard)
2. Klick links in der Seitenleiste auf „Billing and Invoices“, um zur Abrechnungsseite zu gelangen
3. Klick auf „Manage subscription“
4. Klick auf „Update subscription“
5. Wähl „Yearly“ oder „Monthly“ und klick dann auf „Continue“

**Teams-Plan**

1. Geh zum Cursor-[Dashboard](https://cursor.com/dashboard)
2. Klick links in der Seitenleiste auf „Billing and Invoices“, um zur Abrechnungsseite zu gelangen
3. Klick auf den Button „Upgrade Now“, um auf jährliche Abrechnung zu wechseln

<Note>
  Du kannst nur selbst von monatlicher auf jährliche Abrechnung wechseln. Um von jährlicher auf monatliche Abrechnung zu wechseln, kontaktier uns unter
  [hi@cursor.com](mailto:hi@cursor.com).
</Note>

<div id="where-can-i-find-my-invoices">
  ### Wo finde ich meine Rechnungen?
</div>

Deinen kompletten Abrechnungsverlauf findest du im Abrechnungsportal. Dort kannst du aktuelle und frühere Rechnungen ansehen und herunterladen.

<div id="can-i-get-invoices-automatically-emailed-to-me">
  ### Kann ich Rechnungen automatisch per E-Mail bekommen?
</div>

Rechnungen müssen derzeit manuell aus dem Abrechnungsportal heruntergeladen werden. Wir arbeiten an automatischen Rechnungs-E-Mails. Sobald verfügbar, kannst du dich dafür anmelden.

<div id="how-do-i-update-my-billing-information">
  ### Wie aktualisiere ich meine Abrechnungsinformationen?
</div>

Aktualisiere Zahlungsmethode, Firmenname, Adresse und Steuerinformationen im Abrechnungsportal. Wir verwenden Stripe für sichere Transaktionen. Änderungen wirken nur für zukünftige Rechnungen; historische Rechnungen können wir nicht anpassen.

<div id="how-do-i-cancel-my-subscription">
  ### Wie kündige ich mein Abonnement?
</div>

Kündige dein Abo auf der Seite „Billing and Invoices“, indem du bei „Manage Subscription“ den Button „Cancel subscription“ klickst. Dein Zugriff bleibt bis zum Ende deines aktuellen Abrechnungszeitraums bestehen.

<div id="im-having-other-billing-issues-how-can-i-get-help">
  ### Ich habe andere Abrechnungsprobleme. Wie bekomme ich Hilfe?
</div>

Für Abrechnungsfragen, die hier nicht beantwortet werden, schreib von der mit deinem Account verknüpften E-Mail-Adresse an [hi@cursor.com](mailto:hi@cursor.com). Bitte füge deine Account-Details und dein Anliegen bei.



# Preise
Source: https://docs.cursor.com/de/account/pricing

Cursor‑Pläne und ihre Preise

Du kannst Cursor kostenlos ausprobieren oder einen Einzel- oder Team‑Plan kaufen.

<div id="individual">
  ## Individuell
</div>

Alle individuellen Pläne enthalten:

* Unbegrenzte Tab-Vervollständigungen
* Erhöhte Agent-Nutzungslimits für alle Modelle
* Zugriff auf Bugbot
* Zugriff auf Background Agents

Jeder Plan umfasst nutzungsbasierte Abrechnung zu den [API-Preisen](/de/models#model-pricing) für Modellinferenz:

* Pro enthält \$20 an API-Agent-Nutzung + zusätzliche Bonusnutzung
* Pro Plus enthält \$70 an API-Agent-Nutzung + zusätzliche Bonusnutzung
* Ultra enthält \$400 an API-Agent-Nutzung + zusätzliche Bonusnutzung

Wir arbeiten hart daran, dir zusätzliche Bonuskapazität über die garantierte enthaltene Nutzung hinaus bereitzustellen. Da verschiedene Modelle unterschiedliche API-Kosten haben, beeinflusst deine Modellauswahl den Token-Output und wie schnell deine enthaltene Nutzung aufgebraucht wird. Nutzung und Token-Aufschlüsselungen findest du in [deinem Dashboard](https://cursor.com/dashboard?tab=usage). Limit-Benachrichtigungen werden regelmäßig im Editor angezeigt.

<img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c42b8ad6347f6fe9d075647dfece934c" alt="Nutzungslimits" style={{ borderRadius: 16 }} data-og-width="666" width="666" data-og-height="394" height="394" data-path="images/account/usage-limits.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1ca3b5ab64a6ba6f3ad7d75b1ee72e2 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d39dc254e7d059ac24310f26ea47dd5d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=153472f14b4c10ec9a096b7a9db59888 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc8b0cdb5c0677e45c1a082d0002880 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=cf4ac9875f5e587d16d4c6f1e7fdc057 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-limits.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=13f21676cda8e4c2973bc3371892f4aa 2500w" />

<div id="how-much-usage-do-i-need">
  ### Wie viel Nutzung brauche ich?
</div>

Basierend auf unseren Nutzungsdaten kannst du mit folgenden Nutzungsstufen rechnen:

* **Tägliche Tab-User**: Bleiben immer innerhalb von \$20
* **Gelegentliche Agent-User**: Bleiben oft innerhalb der enthaltenen \$20
* **Tägliche Agent-User**: Typischerweise $60–$100/Monat Gesamtnutzung
* **Power-User (mehrere Agents/Automatisierung)**: Oft \$200+/Monat Gesamtnutzung

Basierend auf unseren Nutzungsdaten entsprechen die Limits in etwa Folgendem für eine*n Median-User*in:

* Pro: \~225 Sonnet‑4‑Requests, \~550 Gemini‑Requests oder \~500 GPT‑5‑Requests
* Pro+: \~675 Sonnet‑4‑Requests, \~1.650 Gemini‑Requests oder \~1.500 GPT‑5‑Requests
* Ultra: \~4.500 Sonnet‑4‑Requests, \~11.000 Gemini‑Requests oder \~10.000 GPT‑5‑Requests

<div id="what-happens-when-i-reach-my-limit">
  ### Was passiert, wenn ich mein Limit erreiche?
</div>

Wenn du dein monatlich enthaltenes Nutzungskontingent überschreitest, wirst du im Editor benachrichtigt und kannst Folgendes tun:

* **On-Demand-Nutzung hinzufügen**: Cursor weiterhin zu den gleichen API-Preisen mit nutzungsbasierter Abrechnung verwenden
* **Deinen Plan upgraden**: Auf eine höhere Stufe wechseln, um mehr inkludierte Nutzung zu erhalten

On-Demand-Nutzung wird monatlich zu den gleichen Preisen wie deine inkludierte Nutzung abgerechnet. Anfragen werden niemals in Qualität oder Geschwindigkeit herabgestuft.

<div id="teams">
  ## Teams
</div>

Es gibt zwei Team-Pläne: Teams (\$40/Nutzer/Monat) und Enterprise (individuell).

Team-Pläne bieten zusätzliche Features wie:

* Erzwingen des Privacy Mode
* Admin-Dashboard mit Nutzungsstatistiken
* Zentrale Team-Abrechnung
* SAML/OIDC-SSO

Wir empfehlen Teams für alle, die sich gerne selbst versorgen. Wir empfehlen [Enterprise](/de/contact-sales) für Kunden, die Priority Support, geteilte Nutzung, Rechnungsstellung, SCIM oder erweiterte Sicherheitskontrollen benötigen.

Erfahre mehr über die [Teams-Preise](/de/account/teams/pricing).

<div id="auto">
  ## Auto
</div>

Wenn du Auto aktivierst, wählt Cursor basierend auf der aktuellen Auslastung das Premium‑Modell aus, das am besten zur jeweiligen Aufgabe passt und die höchste Zuverlässigkeit bietet. Diese Funktion erkennt degradierte Output‑Performance und wechselt bei Bedarf automatisch das Modell, um das Problem zu beheben.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f039569ed0dc2ad7e02bb1b2e9cea71" data-og-width="2256" width="2256" data-og-height="1248" height="1248" data-path="images/models/model-picker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=49c6a091945972253eb6e819593e45f0 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=f9bddfb2e130789d8d51a3d1a4eeba94 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=db7273f399bb5decfed9d1b06f389df4 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=920fe98d4f99b5d7fddd47a14fb45699 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3b049686e5826263800b63299f4c19ca 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/models/model-picker.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=72ddd56b4d3ea9b2efa4001a155566fd 2500w" />
</Frame>

<Note>Wir haben viel in die Qualität und Gesamtleistung von Auto investiert. Ab deiner nächsten Abrechnungsverlängerung nach dem 15. September wird Auto zu den folgenden API‑Tarifen abgerechnet.</Note>

* **Input + Cache Write**: \$1.25 pro 1M Tokens
* **Output**: \$6.00 pro 1M Tokens
* **Cache Read**: \$0.25 pro 1M Tokens

Sowohl der Editor als auch das Dashboard zeigen deinen Verbrauch an, einschließlich Auto. Wenn du ein Modell direkt auswählst, wird der Verbrauch zum Listen‑API‑Preis dieses Modells abgerechnet.

<div id="max-mode">
  ## Max-Modus
</div>

Bestimmte Modelle unterstützen den [Max-Modus](/de/models#max-mode), der längeres Reasoning und größere Kontextfenster mit bis zu 1 Mio. Tokens ermöglicht. Für die meisten Coding-Aufgaben ist der Max-Modus nicht nötig, kann aber bei komplexeren Anfragen hilfreich sein, insbesondere bei großen Dateien oder Codebases. Die Nutzung des Max-Modus verbraucht mehr Kontingent. Alle Anfragen und Token-Breakdowns findest du in [deinem Dashboard](https://cursor.com/dashboard?tab=usage).

<div id="bugbot">
  ## Bugbot
</div>

Bugbot ist ein eigenes Produkt, getrennt von Cursor-Abos, und hat seinen eigenen Preisplan.

* **Pro** (\$40/Monat): Unbegrenzte Reviews für bis zu 200 PRs/Monat, unbegrenzter Zugriff auf Cursor Ask, Integration mit Cursor zum Beheben von Bugs sowie Zugriff auf Bugbot Rules
* **Teams** (\$40/Nutzer/Monat): Unbegrenzte Code-Reviews für alle PRs, unbegrenzter Zugriff auf Cursor Ask, gemeinsamer Team-Pool für die Nutzung sowie erweiterte Regeln und Einstellungen
* **Enterprise** (Individuell): Alles aus Teams plus erweiterte Analysen und Reports, priorisierter Support und Account-Management

Erfahre mehr über die [Bugbot-Preise](https://cursor.com/bugbot#pricing).

<div id="background-agent">
  ## Background-Agent
</div>

Background-Agents werden zu den API-Preisen für das ausgewählte [Modell](/de/models) abgerechnet. Wenn du sie zum ersten Mal nutzt, wirst du gebeten, ein Ausgabenlimit für Background-Agents festzulegen.

<Info>
  Compute für virtuelle Maschinen (VM) für Background-Agents wird künftig separat bepreist.
</Info>



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



# Analytics
Source: https://docs.cursor.com/de/account/teams/analytics

Teamnutzung und Aktivitätsmetriken nachverfolgen

Team-Admins können Metriken im [Dashboard](/de/account/teams/dashboard) nachverfolgen.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a8a4a0ca334e5f5acac55307b2ebeadf" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/analytics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=73c11df8fcb2862e5c1fd551e6399159 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c3eaa0d4faa7d6fdf5e3c79dfd11fb5a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e9ee5fc554ae46e9d0e2cf53c19e652d 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5f0afded72e0b02142c5a85e448f2d4e 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a6dec2a182ac88d7de75f7a42b1f5ff 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/analytics.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a8ac7dafe559da435f3f4974b04df52 2500w" />
</Frame>

<div id="total-usage">
  ### Gesamtnutzung
</div>

Sieh dir aggregierte Kennzahlen für dein Team an, inklusive Gesamtzahl der Tabs und Premium-Anfragen. Für Teams, die jünger als 30 Tage sind, zeigen die Kennzahlen die Nutzung seit der Erstellung, einschließlich der Aktivität von Teammitgliedern vor ihrem Beitritt.

<div id="per-active-user">
  ### Pro aktiver Nutzer
</div>

Sieh dir durchschnittliche Kennzahlen pro aktivem Nutzer an: akzeptierte Tabs, Codezeilen und Premium-Anfragen.

<div id="user-activity">
  ### Nutzeraktivität
</div>

Verfolge wöchentlich und monatlich aktive Nutzer.

<div id="analytics-report-headers">
  ## Kopfzeilen des Analytics-Berichts
</div>

Wenn du Analysedaten aus dem Dashboard exportierst, enthält der Bericht detaillierte Metriken zum Nutzerverhalten und zur Funktionsnutzung. Das bedeuten die einzelnen Kopfzeilen:

<div id="user-information">
  ### Nutzerinformationen
</div>

<ResponseField name="Date" type="ISO 8601 timestamp">
  Das Datum, an dem die Analysedaten aufgezeichnet wurden (z. B. 2024-01-15T04:30:00.000Z)
</ResponseField>

<ResponseField name="User ID" type="string">
  Eindeutiger Bezeichner für jeden Nutzer im System
</ResponseField>

<ResponseField name="Email" type="string">
  E-Mail-Adresse des Nutzers, die mit seinem Konto verknüpft ist
</ResponseField>

<ResponseField name="Is Active" type="boolean">
  Gibt an, ob der Nutzer an diesem Datum aktiv war
</ResponseField>

<div id="ai-generated-code-metrics">
  ### KI-generierte Code-Metriken
</div>

<ResponseField name="Chat Suggested Lines Added" type="number">
  Gesamtzahl der vom KI-Chat vorgeschlagenen hinzugefügten Codezeilen
</ResponseField>

<ResponseField name="Chat Suggested Lines Deleted" type="number">
  Gesamtzahl der vom KI-Chat vorgeschlagenen zu löschenden Codezeilen
</ResponseField>

<ResponseField name="Chat Accepted Lines Added" type="number">
  KI-vorgeschlagene Zeilen, die der Nutzer akzeptiert und seinem Code hinzugefügt hat
</ResponseField>

<ResponseField name="Chat Accepted Lines Deleted" type="number">
  Vom Nutzer akzeptierte KI-vorgeschlagene Löschungen
</ResponseField>

<div id="feature-usage-metrics">
  ### Metriken zur Funktionsnutzung
</div>

<ResponseField name="Chat Total Applies" type="number">
  Anzahl der Male, die ein Nutzer KI-generierte Änderungen aus dem Chat angewendet hat
</ResponseField>

<ResponseField name="Chat Total Accepts" type="number">
  Anzahl der Male, die ein Nutzer KI-Vorschläge akzeptiert hat
</ResponseField>

<ResponseField name="Chat Total Rejects" type="number">
  Anzahl der Male, die ein Nutzer KI-Vorschläge abgelehnt hat
</ResponseField>

<ResponseField name="Chat Tabs Shown" type="number">
  Anzahl der Male, die KI-Vorschlags-Tabs dem Nutzer angezeigt wurden
</ResponseField>

<ResponseField name="Tabs Accepted" type="number">
  Vom Nutzer akzeptierte KI-Vorschlags-Tabs
</ResponseField>

<div id="request-type-metrics">
  ### Metriken nach Anfragetyp
</div>

<ResponseField name="Edit Requests" type="number">
  Anfragen über die Composer/Edit-Funktion (Cmd+K Inline-Edits)
</ResponseField>

<ResponseField name="Ask Requests" type="number">
  Chat-Anfragen, bei denen Nutzer der KI Fragen gestellt haben
</ResponseField>

<ResponseField name="Agent Requests" type="number">
  Anfragen an KI-Agents (spezialisierte KI-Assistenten)
</ResponseField>

<ResponseField name="Cmd+K Usages" type="number">
  Anzahl der Nutzungen der Cmd+K- (oder Ctrl+K-) Befehlspalette
</ResponseField>

<div id="subscription-and-api-metrics">
  ### Abonnement- und API-Metriken
</div>

<ResponseField name="Subscription Included Reqs" type="number">
  KI-Anfragen, die durch den Abonnementplan des Nutzers abgedeckt sind
</ResponseField>

<ResponseField name="API Key Reqs" type="number">
  Anfragen, die mit API-Schlüsseln für programmatischen Zugriff gestellt wurden
</ResponseField>

<ResponseField name="Usage-Based Reqs" type="number">
  Anfragen, die zur nutzungsbasierten Abrechnung zählen
</ResponseField>

<div id="additional-features">
  ### Zusätzliche Features
</div>

<ResponseField name="Bugbot Usages" type="number">
  Anzahl der Nutzungen der KI-Funktion zur Fehlererkennung/-behebung
</ResponseField>

<div id="configuration-information">
  ### Konfigurationsinformationen
</div>

<ResponseField name="Most Used Model" type="string">
  Das KI-Modell, das der Nutzer am häufigsten verwendet hat (z. B. GPT-4, Claude)
</ResponseField>

<ResponseField name="Most Used Apply Extension" type="string">
  Am häufigsten verwendete Dateierweiterung beim Anwenden von KI-Vorschlägen (z. B. .ts,
  .py, .java)
</ResponseField>

<ResponseField name="Most Used Tab Extension" type="string">
  Am häufigsten verwendete Dateierweiterung bei Tab-Completion-Features
</ResponseField>

<ResponseField name="Client Version" type="string">
  Verwendete Version des Cursor-Editors
</ResponseField>

<div id="calculated-metrics">
  ### Berechnete Metriken
</div>

Der Bericht enthält außerdem aufbereitete Daten, die helfen, den KI-Codebeitrag zu verstehen:

* Total Lines Added/Deleted: Rohanzahl aller Codeänderungen
* Accepted Lines Added/Deleted: Zeilen, die aus KI-Vorschlägen stammen und akzeptiert wurden
* Composer Requests: Anfragen über die Inline-Composer-Funktion
* Chat Requests: Anfragen über die Chat-Oberfläche

<Note>
  Alle numerischen Werte sind standardmäßig 0, wenn nicht vorhanden, boolesche Werte sind standardmäßig
  false und Zeichenfolgenwerte sind standardmäßig leere Strings. Metriken werden pro Nutzer
  auf Tagesebene aggregiert.
</Note>



# Analytics V2
Source: https://docs.cursor.com/de/account/teams/analyticsV2

Erweiterte Nachverfolgung von Teamnutzung und Aktivitätsmetriken

Wir arbeiten an einem V2-Release unserer Analytics-Infrastruktur. Dazu gehört ein Refactor der Art und Weise, wie wir verschiedene Metriken erfassen.

Ab dem **1. September 2025** und für Nutzer auf **Cursor Version 1.5** verwenden die Analytics unsere V2-Infrastruktur. Frühere Versionen haben verschiedene Metriken zu niedrig erfasst, darunter:

* Gesamtzahl akzeptierter Codezeilen
* Gesamtzahl vorgeschlagener Codezeilen
* Gesamtzahl akzeptierter Tabs

Bleib dran, während wir weiter in Analytics investieren und neue Features in diesem Bereich veröffentlichen.



# Dashboard
Source: https://docs.cursor.com/de/account/teams/dashboard

Verwalte Abrechnung, Nutzung und Teameinstellungen über dein Dashboard

Über das Dashboard kannst du die Abrechnung verwalten, nutzungsbasierte Preisgestaltung einrichten und dein Team managen.

<div id="overview">
  ## Übersicht
</div>

Hol dir eine schnelle Zusammenfassung der Teamaktivität, Nutzungsstatistiken und jüngsten Änderungen. Die Übersichtsseite bietet dir auf einen Blick Einblicke in deinen Workspace.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=48ee98a4d9b168b93c26a03c1af74ddd" data-og-width="3456" width="3456" data-og-height="1944" height="1944" data-path="images/account/team/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2ac6f157659354866eaa03b38cd1eb90 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8e9e84e894a3faf2846e3aae5deb9a2b 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1034c739d961ccc69c17ba947edda90 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dbeed5506f7ae3fc4fabc7d248d69e64 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=afac07ce763fccf7eded7248fb990745 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4ed8c8161c3f2a964371a237134b1ae 2500w" />
</Frame>

<div id="settings">
  ## Einstellungen
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5edb18df1ddc2d20e69abdd83140a509" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4d4c8f244231868bf4111f05b1f46c93 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=582ddf5415a973010e3bcbeeb13d4f64 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74a5d5f4644b701adc25b6d847f5752e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9250830c64e8c3490c3ca6f7b6f65eec 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7ce96a620ac6d447e79abd901b5c6cdc 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6d24738577e0ffd837d87f8926339215 2500w" />
</Frame>

Konfigurier teamweite Einstellungen und Sicherheitsoptionen. Die Seite „Einstellungen“ beinhaltet:

## Teams- & Enterprise-Einstellungen

<AccordionGroup>
  <Accordion title="Privacy Settings">
    Steuer die Datenfreigabe-Einstellungen für dein Team. Konfigurier Zero-Data-Retention-Richtlinien mit KI-Providern (OpenAI, Anthropic, Google Vertex AI, xAI Grok) und verwalt die teamweite Datenschutzdurchsetzung.
  </Accordion>

  {" "}

  <Accordion title="Usage-Based Pricing Settings">
    Aktivier nutzungsbasierte Abrechnung und setz Ausgabenlimits. Konfigurier monatliche Team-Ausgabenlimits und optionale Limits pro Nutzer. Steuer, ob nur Admins diese Einstellungen ändern dürfen.
  </Accordion>

  {" "}

  <Accordion title="Bedrock IAM Role">
    Konfigurier AWS-Bedrock-IAM-Rollen für eine sichere Cloud-Integration.
  </Accordion>

  {" "}

  <Accordion title="Single Sign-On (SSO)">
    Richt SSO-Authentifizierung für Enterprise-Teams ein, um den Zugriff zu vereinfachen und die Sicherheit zu verbessern.
  </Accordion>

  {" "}

  <Accordion title="Cursor Admin API Keys">
    Erstell und verwalt API-Schlüssel für den programmatischen Zugriff auf die Admin-Funktionen von Cursor.
  </Accordion>

  {" "}

  <Accordion title="Active Sessions">
    Überwach und verwalt aktive Sitzungen in deinem Team.
  </Accordion>

  <Accordion title="Invite Code Management">
    Erstell und verwalt Einladungscodes, um neue Teammitglieder hinzuzufügen.
  </Accordion>

  <Accordion title="API Endpoints">
    Greif auf die REST-API-Endpunkte von Cursor für die programmatische Integration zu. Alle API-Endpunkte sind in den Team- und Enterprise-Plänen verfügbar, außer der [AI Code Tracking API](/de/docs/account/teams/ai-code-tracking-api), die eine Enterprise-Mitgliedschaft erfordert.
  </Accordion>
</AccordionGroup>

<div id="enterprise-only-settings">
  ## Exklusive Enterprise-Einstellungen
</div>

<AccordionGroup>
  {" "}

  <Accordion title="Model Access Control">
    Steuere, welche KI-Modelle für Teammitglieder verfügbar sind. Setze Einschränkungen für
    bestimmte Modelle oder Modellstufen, um Kosten zu kontrollieren und eine angemessene Nutzung in
    deiner Organisation sicherzustellen.
  </Accordion>

  {" "}

  <Accordion title="Auto Run Configuration (0.49+)">
    Konfiguriere die automatische Befehlsausführung für Cursor Version 0.49 und
    höher. Lege fest, welche Befehle automatisch ausgeführt werden dürfen, und setze
    Sicherheitsrichtlinien für die Codeausführung.
  </Accordion>

  <Accordion title="Repository Blocklist">
    Verhindere den Zugriff auf bestimmte Repositories aus Sicherheits- oder Compliance-Gründen.
  </Accordion>

  {" "}

  <Accordion title="MCP Configuration (0.51+)">
    Konfiguriere die Model Context Protocol-Einstellungen für Cursor Version 0.51 und höher.
    Steuere, wie Modelle auf Kontext aus deiner Entwicklungsumgebung zugreifen und ihn verarbeiten.
  </Accordion>

  {" "}

  <Accordion title="Cursor Ignore Configuration (0.50+)">
    Richte Ignore-Muster für Dateien und Verzeichnisse in Cursor Version 0.50 und höher ein.
    Steuere, welche Dateien und Verzeichnisse von der KI-Analyse und -Vorschlägen ausgeschlossen werden.
  </Accordion>

  <Accordion title=".cursor Directory Protection (0.51+)">
    Schütze das .cursor-Verzeichnis vor unbefugtem Zugriff in Version 0.51 und höher. Stelle sicher, dass sensible Konfigurations- und Cache-Dateien geschützt bleiben.
  </Accordion>

  <Accordion title="AI Code Tracking API">
    Greife auf detaillierte Analysen zu KI-generiertem Code für die Repositories deines Teams zu. Rufe pro Commit KI-Nutzungsmetriken und granulare übernommene KI-Änderungen über REST-API-Endpunkte ab. Erfordert einen Enterprise-Plan. Mehr Infos findest du [hier](/de/account/teams/ai-code-tracking-api).
  </Accordion>
</AccordionGroup>

<Note>
  **SCIM** (System for Cross-domain Identity Management)-Provisioning ist auch
  für Enterprise-Pläne verfügbar. Sieh dir unsere [SCIM-
  Dokumentation](/de/account/teams/scim) für Setup-Anleitungen an.
</Note>

<div id="members">
  ## Mitglieder
</div>

Verwalte deine Teammitglieder, lade neue Nutzer ein und steuere die Zugriffsrechte. Lege rollenbasierte Berechtigungen fest und behalte die Aktivitäten deiner Mitglieder im Blick.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4ac43692626733caf2da4b53e4cd9055" data-og-width="1390" width="1390" data-og-height="591" height="591" data-path="images/account/team/members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a2a24d3282df1e875d73fd2bf29b9c04 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1abe9715816149f577a5d9c9e2f3545d 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ccc84260c5139119e5b16ad6c214af72 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5fe34e422fa9540004c25a61570029c3 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dee7c3ade8ef46b5ead5dbe2bfd2a6be 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a42bce921a799886b8e3e0a389b8589 2500w" />
</Frame>

<div id="integrations">
  ## Integrationen
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Verbinde Cursor mit deinen Lieblings-Tools und -Diensten. Richte Integrationen mit Versionskontrollsystemen, Projektmanagement-Tools und anderen Entwickler-Services ein.

<div id="background-agents">
  ## Hintergrund-Agents
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=187b9e77d6b99c77caec81e1b3063417" data-og-width="1390" width="1390" data-og-height="592" height="592" data-path="images/account/team/integrations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=470d5697ff2bfb9db2ae745b2c33cce6 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e1e7d589f1f208ecdba9840629897968 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2285e05c99c3a6ace609b51770475a3e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7c44649c5e8cd0f2a3791a3085252eca 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0cf7111171c8019f7a59adc79cb9639d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/integrations.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8423a209b4e1c753045dca1514cbfbad 2500w" />
</Frame>

{" "}

Überwache und verwalte Hintergrund-Agents, die in deinem Workspace laufen. Schau dir den Agent-Status, Logs und die Ressourcennutzung an.

<div id="bugbot">
  ## Bugbot
</div>

Nutze automatisierte Funktionen zur Fehlererkennung und -behebung. Bugbot hilft dir, häufige Probleme in deiner Codebasis automatisch zu identifizieren und zu lösen.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=20d841dfc7837445103a933dab18b470" alt="Bugbot-Code-Review" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/bugbot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=975f5e3f9f9a0334c8a5bcc12faf72be 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=17099f8bbe0701750d0ba212879d8a93 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=041c82a4c3bada0524527609dfc134a4 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90ac57ea38768ace4b9404476fafdf32 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5785673a93f899ccca7b70e7a3752ef7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/bugbot.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a1a1dc51872967e392e10d6b85c31a04 2500w" />
</Frame>

<div id="active-directory-management">
  ## Active-Directory-Verwaltung
</div>

Für Enterprise-Teams: Verwalte Benutzeranmeldung und Zugriffsrechte über die Active-Directory-Integration. Konfiguriere SSO und die automatische Benutzerbereitstellung (User Provisioning).

<div id="usage">
  ## Nutzung
</div>

Verfolge detaillierte Nutzungsmetriken, inklusive AI-Anfragen, Modellnutzung und Ressourcenverbrauch. Behalte die Nutzung teamweit und projektübergreifend im Blick.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8744e41430d162199d85ca8e966c91cd" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc43eaaeca3c2a531a56243037a7a53f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=34700d63fabf072e9906aab74f79f7d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7f2bcdb271d6b30e333374c798638989 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=424bd0eeda69200668f8f0b86dc360bf 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f0e716c72f01a3297a53a5b63d191ef4 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/usage.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffa574322508a07cc5ab867b331b6d35 2500w" />
</Frame>

## Abrechnung & Rechnungen

Verwalte dein Abo, aktualisiere Zahlungsmethoden und greif auf deinen Abrechnungsverlauf zu. Lade Rechnungen herunter und verwalte Einstellungen für nutzungsbasierte Abrechnung.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d76d20a7fafc6ed2135f2f9c78ec6c2d" data-og-width="1390" width="1390" data-og-height="913" height="913" data-path="images/account/team/billing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45501f34dd144ecd74e982fe5f8f8364 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=19860b61e083a8550cb3caa16bdb1ba0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7005bae381a362b39980a49113ca367c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e47c9ee55e3699ba46429b0ac0563b5b 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=039106fd5ff42f2e343b2b853614e7e7 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/billing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e598f83559985558f5825a3da25bb554 2500w" />
</Frame>



# Enterprise-Einstellungen
Source: https://docs.cursor.com/de/account/teams/enterprise-settings

Cursor-Einstellungen zentral für deine Organisation verwalten

<div id="enterprise-settings">
  # Enterprise-Einstellungen
</div>

Du kannst bestimmte Funktionen von Cursor zentral über Gerätemanagementlösungen verwalten, damit sie den Anforderungen deiner Organisation entsprechen. Wenn du eine Cursor-Richtlinie festlegst, überschreibt deren Wert die entsprechende Cursor-Einstellung auf den Geräten der Nutzer.

Einstellungseditor, der zeigt, dass die Einstellung „Extensions: Allowed“ von der Organisation verwaltet wird.

Cursor stellt derzeit Richtlinien zur Steuerung der folgenden administratorgesteuerten Funktionen bereit:

| Policy            | Description                                                                                                           | Cursor setting           | Available since |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------- |
| AllowedExtensions | Steuert, welche Erweiterungen installiert werden können.                                                              | extensions.allowed       | 1.2             |
| AllowedTeamId     | Steuert, welche Team-IDs sich anmelden dürfen. Nutzer mit nicht autorisierten Team-IDs werden zwangsweise abgemeldet. | cursorAuth.allowedTeamId | 1.3             |

<div id="configure-allowed-extensions">
  ## Zugelassene Erweiterungen konfigurieren
</div>

Die Cursor-Einstellung `extensions.allowed` legt fest, welche Erweiterungen installiert werden können. Diese Einstellung erwartet ein JSON-Objekt, in dem die Schlüssel Publisher-Namen sind und die Werte Booleans, die angeben, ob Erweiterungen dieses Publishers erlaubt sind.

Wenn du zum Beispiel `extensions.allowed` auf `{"anysphere": true, "github": true}` setzt, sind Erweiterungen der Publisher Anysphere und GitHub erlaubt, während `{"anysphere": false}` Anysphere-Erweiterungen blockiert.

Um zugelassene Erweiterungen zentral für deine Organisation zu verwalten, konfiguriere die Richtlinie `AllowedExtensions` über deine Device-Management-Lösung. Diese Richtlinie überschreibt die Einstellung `extensions.allowed` auf den Geräten der Nutzer. Der Wert dieser Richtlinie ist ein JSON-String, der die erlaubten Publisher definiert.

Wenn du mehr über Erweiterungen in Cursor erfahren willst, schau dir die Extensions-Dokumentation an.

<div id="configure-allowed-team-ids">
  ## Zulässige Team-IDs konfigurieren
</div>

Die Cursor-Einstellung `cursorAuth.allowedTeamId` legt fest, welche Team-IDs sich bei Cursor anmelden dürfen. Diese Einstellung akzeptiert eine kommagetrennte Liste von Team-IDs, die für den Zugriff autorisiert sind.

Wenn du `cursorAuth.allowedTeamId` zum Beispiel auf `"1,3,7"` setzt, können sich Nutzerinnen und Nutzer mit genau diesen Team-IDs anmelden.

Wenn jemand versucht, sich mit einer nicht zugelassenen Team-ID anzumelden:

* Die Person wird sofort abgemeldet
* Eine Fehlermeldung wird angezeigt
* Die Anwendung blockiert weitere Authentifizierungsversuche, bis eine gültige Team-ID verwendet wird

Um zulässige Team-IDs zentral für deine Organisation zu verwalten, konfiguriere die Richtlinie `AllowedTeamId` über deine Geräteverwaltung. Diese Richtlinie überschreibt die Einstellung `cursorAuth.allowedTeamId` auf den Geräten der Nutzerinnen und Nutzer. Der Wert dieser Richtlinie ist ein String mit der kommagetrennten Liste der autorisierten Team-IDs.

<div id="group-policy-on-windows">
  ## Gruppenrichtlinie unter Windows
</div>

Cursor unterstützt Windows-Registry-basierte Gruppenrichtlinien. Wenn Richtliniendefinitionen installiert sind, kannst du den Local Group Policy Editor verwenden, um die Richtlinienwerte zu verwalten.

So fügst du eine Richtlinie hinzu:

1. Kopiere die ADMX- und ADML-Dateien für Policies aus `AppData\Local\Programs\cursor\policies`.
2. Füge die ADMX-Datei in das Verzeichnis `C:\Windows\PolicyDefinitions` ein und die ADML-Datei in das Verzeichnis `C:\Windows\PolicyDefinitions\<your-locale>\`.
3. Starte den Local Group Policy Editor neu.
4. Setze die entsprechenden Richtlinienwerte (z. B. `{"anysphere": true, "github": true}` für die Richtlinie `AllowedExtensions`) im Local Group Policy Editor.

Richtlinien können sowohl auf Computer- als auch auf Benutzerebene gesetzt werden. Wenn beide gesetzt sind, hat die Computerebene Vorrang. Wenn ein Richtlinienwert gesetzt ist, überschreibt er die in Cursor konfigurierte Einstellung auf jeder Ebene (Standard, Benutzer, Workspace usw.).

<div id="configuration-profiles-on-macos">
  ## Konfigurationsprofile unter macOS
</div>

Konfigurationsprofile verwalten Einstellungen auf macOS‑Geräten. Ein Profil ist eine XML-Datei mit Schlüssel/Wert-Paaren, die den verfügbaren Richtlinien entsprechen. Diese Profile können über Mobile-Device-Management-(MDM)-Lösungen bereitgestellt oder manuell installiert werden.

<Accordion title="Beispiel für eine .mobileconfig-Datei">
  Ein Beispiel für eine `.mobileconfig`-Datei für macOS ist unten dargestellt:

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  	<dict>
  		<key>PayloadContent</key>
  		<array>
  			<dict>
  				<key>PayloadDisplayName</key>
  				<string>Cursor</string>
  				<key>PayloadIdentifier</key>
  				<string>com.todesktop.230313mzl4w4u92.J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadType</key>
  				<string>com.todesktop.230313mzl4w4u92</string>
  				<key>PayloadUUID</key>
  				<string>J6B5723A-6539-4F31-8A4E-3CC96E51F48C</string>
  				<key>PayloadVersion</key>
  				<integer>1</integer>
  				<key>AllowedExtensions</key>
  				<string>{"anysphere":true}</string>
  				<key>AllowedTeamId</key>
  				<string>1,2</string>
  			</dict>
  		</array>
  		<key>PayloadDescription</key>
  		<string>This profile manages Cursor.</string>
  		<key>PayloadDisplayName</key>
  		<string>Cursor</string>
  		<key>PayloadIdentifier</key>
  		<string>com.todesktop.230313mzl4w4u92</string>
  		<key>PayloadOrganization</key>
  		<string>Anysphere</string>
  		<key>PayloadType</key>
  		<string>Configuration</string>
  		<key>PayloadUUID</key>
  		<string>F2C1A7B3-9D4E-4B2C-8E1F-7A6C5D4B3E2F</string>
  		<key>PayloadVersion</key>
  		<integer>1</integer>
  		<key>TargetDeviceType</key>
  		<integer>5</integer>
  	</dict>
  </plist>
  ```
</Accordion>

<div id="string-policies">
  ### String-Richtlinien
</div>

Das folgende Beispiel zeigt die Konfiguration der Richtlinie `AllowedExtensions`. Der Richtlinienwert ist in der Beispieldatei zunächst leer (es sind keine Erweiterungen erlaubt).

```
<key>ErlaubteErweiterungen</key>
<string></string>
```

Füg die passende JSON-Zeichenfolge, die deine Policy definiert, zwischen die `<string>`-Tags ein.

```
<key>ZugelasseneErweiterungen</key>
<string>{"anysphere": true, "github": true}</string>
```

Für die Richtlinie `AllowedTeamId` die durch Kommas getrennte Liste der Team-IDs hinzufügen:

```
<key>ZulässigeTeamId</key>
<string>1,3,7</string>
```

**Wichtig:** Die bereitgestellte `.mobileconfig`-Datei setzt **alle** in dieser Cursor-Version verfügbaren Richtlinien. Lösch alle Richtlinien, die du nicht brauchst.

Wenn du eine Richtlinie in der Beispiel-`.mobileconfig` nicht bearbeitest oder entfernst, wird sie mit ihrem standardmäßigen (restriktiven) Wert erzwungen.

Installier ein Konfigurationsprofil manuell, indem du im Finder doppelt auf das `.mobileconfig`-Profil klickst und es anschließend in den Systemeinstellungen unter **Allgemein** > **Geräteverwaltung** aktivierst. Wenn du das Profil aus den Systemeinstellungen entfernst, werden die Richtlinien in Cursor ebenfalls entfernt.

Mehr Infos zu Konfigurationsprofilen findest du in der Apple-Dokumentation.

<div id="additional-policies">
  ## Zusätzliche Richtlinien
</div>

Ziel ist es, die aktuellen Cursor-Einstellungen als Richtlinien zu übernehmen und sich eng an die bestehenden Einstellungen zu halten, damit Benennung und Verhalten konsistent bleiben. Wenn es Anfragen gibt, weitere Richtlinien einzuführen, eröffne bitte ein Issue im Cursor-GitHub-Repository. Das Team entscheidet dann, ob es bereits eine entsprechende Einstellung für das gewünschte Verhalten gibt oder ob eine neue Einstellung erstellt werden sollte, um dieses Verhalten zu steuern.

<div id="frequently-asked-questions">
  ## Häufig gestellte Fragen
</div>

<div id="does-cursor-support-configuration-profiles-on-linux">
  ### Unterstützt Cursor Konfigurationsprofile unter Linux?
</div>

Linux-Unterstützung steht derzeit nicht auf der Roadmap. Wenn du Konfigurationsprofile unter Linux möchtest, eröffne ein Issue im Cursor-GitHub-Repository und beschreibe deinen Anwendungsfall.



# Mitglieder & Rollen
Source: https://docs.cursor.com/de/account/teams/members

Teammitglieder und Rollen verwalten

Cursor-Teams haben drei Rollen:

<div id="roles">
  ## Rollen
</div>

**Mitglieder** sind die Standardrolle mit Zugriff auf die Pro-Funktionen von Cursor.

* Voller Zugriff auf die Pro-Funktionen von Cursor
* Kein Zugriff auf Abrechnungseinstellungen oder das Admin-Dashboard
* Können die eigene Nutzung und das verbleibende nutzungsbasierte Budget sehen

**Admins** steuern die Teamverwaltung und Sicherheitseinstellungen.

* Voller Zugriff auf Pro-Funktionen
* Mitglieder hinzufügen/entfernen, Rollen ändern, SSO einrichten
* Nutzungsbasierte Preise und Ausgabelimits konfigurieren
* Zugriff auf Team-Analytics

**Unbezahlte Admins** verwalten Teams, ohne einen bezahlten Seat zu verwenden – ideal für IT- oder Finance-Mitarbeitende, die keinen Cursor-Zugriff brauchen.

* Nicht abrechenbar, keine Pro-Funktionen
* Gleiche administrativen Möglichkeiten wie Admins

<Info>Unbezahlte Admins erfordern mindestens einen bezahlten User im Team.</Info>

<div id="role-comparison">
  ## Rollenvergleich
</div>

<div className="full-width-table">
  | Funktionalität                        | Mitglied | Admin | Unbezahlter Admin |
  | ------------------------------------- | :------: | :---: | :---------------: |
  | Cursor‑Funktionen nutzen              |     ✓    |   ✓   |                   |
  | Mitglieder einladen                   |     ✓    |   ✓   |         ✓         |
  | Mitglieder entfernen                  |          |   ✓   |         ✓         |
  | Benutzerrollen ändern                 |          |   ✓   |         ✓         |
  | Admin‑Dashboard                       |          |   ✓   |         ✓         |
  | SSO/Sicherheit konfigurieren          |          |   ✓   |         ✓         |
  | Abrechnung verwalten                  |          |   ✓   |         ✓         |
  | Analysen einsehen                     |          |   ✓   |         ✓         |
  | Zugriffe verwalten                    |          |   ✓   |         ✓         |
  | Nutzungsgrenzen festlegen             |          |   ✓   |         ✓         |
  | Erfordert kostenpflichtigen Sitzplatz |     ✓    |   ✓   |                   |
</div>

<div id="managing-members">
  ## Mitglieder verwalten
</div>

Alle Teammitglieder können andere einladen. Einladungen werden aktuell nicht eingeschränkt.

<div id="add-member">
  ### Mitglied hinzufügen
</div>

Füge Mitglieder auf drei Arten hinzu:

1. **E-Mail-Einladung**

   * Klicke auf `Invite Members`
   * Gib E-Mail-Adressen ein
   * Nutzer erhalten E-Mail-Einladungen

2. **Einladungslink**

   * Klicke auf `Invite Members`
   * Kopiere `Invite Link`
   * Teile ihn mit Teammitgliedern

3. **SSO**
   * Konfiguriere SSO im [Admin-Dashboard](/de/account/teams/sso)
   * Nutzer treten automatisch bei, wenn sie sich mit ihrer SSO-E-Mail anmelden

<Warning>
  Einladungslinks haben eine lange Gültigkeitsdauer – jeder mit dem Link kann beitreten.
  Widerrufe sie oder nutze [SSO](/de/account/teams/sso)
</Warning>

<div id="remove-member">
  ### Mitglied entfernen
</div>

Admins können Mitglieder jederzeit über das Kontextmenü → „Remove“ entfernen. Wenn ein Mitglied bereits Credits genutzt hat, bleibt sein Platz bis zum Ende des Abrechnungszeitraums belegt.

<div id="change-role">
  ### Rolle ändern
</div>

Admins können Rollen für andere Mitglieder ändern, indem sie das Kontextmenü öffnen und anschließend die Option „Change role“ verwenden.<br />

Es muss jederzeit mindestens ein Admin und ein zahlendes Mitglied im Team sein.

## Sicherheit & SSO

SAML 2.0 Single Sign-On (SSO) ist in Team-Plänen verfügbar. Zu den wichtigsten Funktionen gehören:

* SSO-Verbindungen konfigurieren ([mehr erfahren](/de/account/teams/sso))
* Domainverifizierung einrichten
* Automatische Benutzerbereitstellung
* Optionen zur Erzwingung von SSO
* Integration von Identitätsanbietern (Okta usw.)

<Note>
  <p className="!mb-0">Für die Aktivierung von SSO ist eine Domainverifizierung erforderlich.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## Nutzungssteuerung
</div>

Greif auf die Nutzungseinstellungen zu, um:

* nutzungsbasierte Abrechnung zu aktivieren
* Premium-Modelle zu aktivieren
* Änderungen nur für Admins zuzulassen
* monatliche Ausgabenlimits festzulegen
* die teamweite Nutzung zu überwachen

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## Abrechnung
</div>

Wenn du Teammitglieder hinzufügst:

* Jedes Mitglied oder jeder Admin belegt einen kostenpflichtigen Sitzplatz (siehe [Preise](https://cursor.com/pricing))
* Neue Mitglieder werden anteilig für die verbleibende Zeit im Abrechnungszeitraum berechnet
* Unbezahlte Admin-Sitzplätze werden nicht mitgezählt

Bei Ergänzungen mitten im Monat zahlst du nur für die genutzten Tage. Wenn du Mitglieder entfernst, die Credits genutzt haben, bleibt ihr Sitzplatz bis zum Ende des Abrechnungszyklus belegt – anteilige Rückerstattungen gibt es nicht.

Rollenänderungen (z. B. Admin zu Unpaid Admin) wirken sich ab dem Änderungsdatum auf die Abrechnung aus. Wähle monatliche oder jährliche Abrechnung.

Die monatliche/jährliche Verlängerung erfolgt an deinem ursprünglichen Anmeldedatum – unabhängig von Änderungen bei den Mitgliedern.

<div id="switch-to-yearly-billing">
  ### Zur jährlichen Abrechnung wechseln
</div>

Spare **20 %**, indem du von monatlich auf jährlich wechselst:

1. Geh zum [Dashboard](https://cursor.com/dashboard)
2. Klick im Kontobereich auf „Advanced“ und dann auf „Upgrade to yearly billing“

<Note>
  Du kannst nur über das Dashboard von monatlich auf jährlich wechseln. Um von
  jährlich auf monatlich zu wechseln, schreib an [hi@cursor.com](mailto:hi@cursor.com).
</Note>



# SCIM
Source: https://docs.cursor.com/de/account/teams/scim

Richte SCIM-Provisioning für die automatisierte Verwaltung von Benutzer:innen und Gruppen ein

<div id="overview">
  ## Überblick
</div>

Die SCIM‑2.0‑Provisionierung verwaltet automatisch deine Teammitglieder und Verzeichnisgruppen über deinen Identity Provider. Verfügbar in Enterprise‑Plänen mit aktiviertem SSO.

<product_visual type="screenshot">
  SCIM‑Einstellungen‑Dashboard mit Konfiguration für Active Directory Management
</product_visual>

<div id="prerequisites">
  ## Voraussetzungen
</div>

* Cursor Enterprise-Plan
* SSO muss zuerst eingerichtet sein – **SCIM setzt eine aktive SSO-Verbindung voraus**
* Admin-Zugriff auf deinen Identity-Provider (Okta, Azure AD, etc.)
* Admin-Zugriff auf deine Cursor-Organisation

## So funktioniert's

<div id="user-provisioning">
  ### Benutzerbereitstellung
</div>

Nutzer werden automatisch zu Cursor hinzugefügt, wenn sie in deinem Identity-Provider der SCIM-Anwendung zugewiesen werden. Wenn die Zuweisung entfernt wird, werden sie gelöscht. Änderungen werden in Echtzeit synchronisiert.

<div id="directory-groups">
  ### Verzeichnisgruppen
</div>

Verzeichnisgruppen und deren Mitgliedschaften werden aus deinem Identity-Provider synchronisiert. Gruppen- und Nutzerverwaltung müssen über deinen Identity-Provider erfolgen – Cursor zeigt diese Informationen nur schreibgeschützt an.

<div id="spend-management">
  ### Ausgabenverwaltung
</div>

Lege unterschiedliche Ausgabenlimits pro Nutzer für jede Verzeichnisgruppe fest. Limits auf Verzeichnisgruppenebene haben Vorrang vor Team-Limits. Nutzer in mehreren Gruppen erhalten das jeweils höchste anwendbare Ausgabenlimit.

<div id="setup">
  ## Setup
</div>

<Steps>
  <Step title="Stell sicher, dass SSO konfiguriert ist">
    SCIM setzt voraus, dass SSO zuerst eingerichtet ist. Wenn du SSO noch nicht konfiguriert hast,
    folge der [SSO-Einrichtungsanleitung](/de/account/teams/sso), bevor du fortfährst.
  </Step>

  <Step title="Öffne die Active-Directory-Verwaltung">
    Navigiere zu
    [cursor.com/dashboard?tab=active-directory](https://www.cursor.com/dashboard?tab=active-directory)
    mit einem Admin-Account, oder geh in deine Dashboard-Einstellungen und wähle den
    Tab „Active Directory Management“.
  </Step>

  <Step title="Starte die SCIM-Einrichtung">
    Sobald SSO verifiziert ist, siehst du einen Link für die schrittweise SCIM-Einrichtung. Klick
    darauf, um den Konfigurationsassistenten zu starten.
  </Step>

  <Step title="Konfiguriere SCIM in deinem Identity-Provider">
    In deinem Identity-Provider: - Erstelle oder konfiguriere deine SCIM-App - Verwende
    den von Cursor bereitgestellten SCIM-Endpoint und das Token - Aktiviere User- und Gruppen-
    Provisioning (Push) - Teste die Verbindung
  </Step>

  <Step title="Ausgabenlimits konfigurieren (optional)">
    Zurück in der Active-Directory-Verwaltung von Cursor: - Sieh dir deine synchronisierten
    Verzeichnisgruppen an - Setze nutzerbezogene Ausgabenlimits für bestimmte Gruppen nach Bedarf -
    Prüfe, welche Limits für User in mehreren Gruppen gelten
  </Step>
</Steps>

<div id="identity-provider-setup">
  ### Identity-Provider-Setup
</div>

Für providerspezifische Setup-Anleitungen:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Setup-Anleitungen für Okta, Azure AD, Google Workspace und mehr.
</Card>

<div id="managing-users-and-groups">
  ## Benutzer und Gruppen verwalten
</div>

<Warning>
  Die gesamte Benutzer- und Gruppenverwaltung muss über deinen Identity-Provider erfolgen.
  Änderungen in deinem Identity-Provider werden automatisch mit Cursor synchronisiert,
  aber du kannst Benutzer oder Gruppen nicht direkt in Cursor ändern.
</Warning>

<div id="user-management">
  ### Benutzerverwaltung
</div>

* Füge Benutzer hinzu, indem du sie in deinem Identity-Provider deiner SCIM-Anwendung zuweist
* Entferne Benutzer, indem du die Zuweisung zur SCIM-Anwendung aufhebst
* Änderungen am Benutzerprofil (Name, E-Mail) werden automatisch aus deinem Identity-Provider übernommen

<div id="group-management">
  ### Gruppenverwaltung
</div>

* Verzeichnisgruppen werden automatisch aus deinem Identity-Provider synchronisiert
* Änderungen an der Gruppenmitgliedschaft werden in Echtzeit übernommen
* Nutze Gruppen, um Benutzer zu organisieren und unterschiedliche Ausgabenlimits festzulegen

<div id="spend-limits">
  ### Ausgabenlimits
</div>

* Lege unterschiedliche Pro-Benutzer-Limits für jede Verzeichnisgruppe fest
* Benutzer erben das höchste Ausgabenlimit aus ihren Gruppen
* Gruppenlimits überschreiben das standardmäßige, teamweite Pro-Benutzer-Limit

<div id="faq">
  ## FAQ
</div>

<div id="why-isnt-scim-management-showing-up-in-my-dashboard">
  ### Warum wird die SCIM-Verwaltung in meinem Dashboard nicht angezeigt?
</div>

Stell sicher, dass SSO korrekt konfiguriert ist und funktioniert, bevor du SCIM einrichtest. SCIM erfordert eine aktive SSO-Verbindung.

<div id="why-arent-users-syncing">
  ### Warum werden Nutzer nicht synchronisiert?
</div>

Überprüf, ob Nutzer in deinem Identity Provider der SCIM-App zugewiesen sind. Nutzer müssen explizit zugewiesen werden, um in Cursor zu erscheinen.

<div id="why-arent-groups-appearing">
  ### Warum werden Gruppen nicht angezeigt?
</div>

Prüf, ob die Bereitstellung für Gruppen-Push in den SCIM-Einstellungen deines Identity Providers aktiviert ist. Die Gruppensynchronisierung muss getrennt von der Nutzersynchronisierung konfiguriert werden.

<div id="why-arent-spend-limits-applying">
  ### Warum werden Ausgabenlimits nicht angewendet?
</div>

Stell sicher, dass Nutzer in deinem Identity Provider den erwarteten Gruppen korrekt zugeordnet sind. Die Gruppenmitgliedschaft bestimmt, welche Ausgabenlimits gelten.

<div id="can-i-manage-scim-users-and-groups-directly-in-cursor">
  ### Kann ich SCIM-Nutzer und -Gruppen direkt in Cursor verwalten?
</div>

Nein. Die gesamte Nutzer- und Gruppenverwaltung muss über deinen Identity Provider erfolgen. Cursor zeigt diese Informationen nur lesend an.

<div id="how-quickly-do-changes-sync">
  ### Wie schnell werden Änderungen synchronisiert?
</div>

Änderungen in deinem Identity Provider werden in Echtzeit mit Cursor synchronisiert. Bei großen Bulk-Operationen kann es zu einer kurzen Verzögerung kommen.



# Leg los
Source: https://docs.cursor.com/de/account/teams/setup

Erstelle und richte ein Cursor-Team ein

<div id="cursor-for-teams">
  ## Cursor für Teams
</div>

Cursor ist für Einzelpersonen und Teams. Der Teams-Plan bietet Tools für Organisationen: SSO, Teamverwaltung, Zugriffskontrollen und Nutzungsanalysen.

<div id="creating-a-team">
  ## Ein Team erstellen
</div>

Erstell ein Team, indem du diese Schritte befolgst:

<Steps>
  <Step title="Teams-Plan einrichten">
    Um ein Team zu erstellen, folg diesen Schritten:

    1. **Für neue Nutzer**: Besuch [cursor.com/team/new-team](https://cursor.com/team/new-team), um ein neues Konto und Team zu erstellen
    2. **Für bestehende Nutzer**: Geh zu deinem [Dashboard](/de/account/dashboard) und klick auf „Upgrade to Teams“
  </Step>

  <Step title="Teamdetails eingeben">
    Wähl einen Teamnamen und einen Abrechnungszeitraum aus

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3b9df20d032b544dcbc0343d9ddf056f" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/account/team/new-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b81f3241069a8a0fb9278b6a2e246057 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c26976bf06297d36ec9224ec1496a630 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fed5c7c95914ff47cfceae81f1441208 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0dc5986368419ef54f45803547741cfe 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4eb38a9618399ddadbf7596b185d2732 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/team/new-team.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c7d720a1e20d2aa23463a1b9001d545 2500w" />
    </Frame>
  </Step>

  <Step title="Mitglieder einladen">
    Lad Teammitglieder ein. Die Nutzeranzahl wird anteilig berechnet – du zahlst nur für die Zeit, in der Nutzer Mitglieder sind.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbd84dd96a7003415c2d2f038b1aaa77" style={{ paddingLeft: 16, paddingRight: 16, backgroundColor: '#0c0c0c' }} data-og-width="880" width="880" data-og-height="422" height="422" data-path="images/account/invite-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=988e36ee874f704dfaae1b0a69ed2f84 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c0f85aacd3be59e11b1bfd05f9e5d6cd 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=411456e375f8c406ad2972965e0b549e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57ae04799be300a7e61464490344146f 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=2faa0cf8ed56865c19916e33fde97900 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/invite-members.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0bdb5040f44338e748246b4f1ddf2ddf 2500w" />
    </Frame>
  </Step>

  <Step title="SSO aktivieren (optional)">
    Aktivier [SSO](/de/account/teams/sso) für mehr Sicherheit und automatisiertes Onboarding.

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
    </Frame>
  </Step>
</Steps>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Mein Team nutzt Zscaler / einen Proxy / ein VPN – funktioniert Cursor?">
    Cursor verwendet standardmäßig HTTP/2. Manche Proxys und VPNs blockieren das.

    Aktiviere in den Einstellungen das HTTP/1.1-Fallback, um stattdessen HTTP/1.1 zu nutzen.
  </Accordion>

  <Accordion title="Wie kann ich Lizenzen für mein Unternehmen kaufen?">
    Cursor rechnet pro aktivem Nutzer ab, nicht pro Sitzplatz. Du kannst jederzeit Nutzer hinzufügen oder entfernen – neue Mitglieder werden anteilig für die verbleibende Zeit berechnet. Wenn ein entfernter Nutzer Credits genutzt hat, bleibt sein Sitz bis zum Ende des Abrechnungszeitraums belegt.

    Dein Verlängerungsdatum bleibt gleich.
  </Accordion>

  <Accordion title="Wie kann ich ein Team einrichten, wenn ich Cursor selbst nicht nutze?">
    Setz dich als [Unpaid Admin](/de/account/teams/members), um ohne Lizenz verwalten zu können.

    <Warning>
      Teams benötigen mindestens ein zahlendes Mitglied. Du kannst alles einrichten, ein Mitglied einladen und dann deine Rolle vor der Abrechnung ändern.
    </Warning>
  </Accordion>

  <Accordion title="Wie kann ich Cursor ins MDM meines Unternehmens aufnehmen?">
    Download-Links für alle Plattformen findest du unter [cursor.com/downloads](https://cursor.com/downloads).

    MDM-Anleitungen:

    * [Omnissa Workspace ONE](https://docs.omnissa.com/bundle/MobileApplicationManagementVSaaS/page/DeployInternalApplications.html) (ehemals VMware)
    * [Microsoft Intune (Windows)](https://learn.microsoft.com/en-us/mem/intune-service/apps/apps-win32-app-management)
    * [Microsoft Intune (Mac)](https://learn.microsoft.com/en-us/mem/intune-service/apps/lob-apps-macos-dmg)
    * [Kandji MDM](https://support.kandji.io/kb/custom-apps-overview)
  </Accordion>
</AccordionGroup>



# SSO
Source: https://docs.cursor.com/de/account/teams/sso

Richte Single Sign-on für dein Team ein

<div id="overview">
  ## Überblick
</div>

SAML 2.0 SSO ist ohne zusätzliche Kosten in Business-Plänen verfügbar. Verwende deinen bestehenden Identity-Provider (IdP), um Teammitglieder zu authentifizieren, ohne separate Cursor-Konten zu benötigen.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: 32, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="prerequisites">
  ## Voraussetzungen
</div>

* Cursor Team-Plan
* Admin-Zugriff auf deinen Identity-Provider (z. B. Okta)
* Admin-Zugriff auf deine Cursor-Organisation

<div id="configuration-steps">
  ## Konfigurationsschritte
</div>

<Steps>
  <Step title="Melde dich bei deinem Cursor-Konto an">
    Navigiere mit einem Admin-Konto zu [cursor.com/dashboard?tab=settings](https://www.cursor.com/dashboard?tab=settings).
  </Step>

  <Step title="SSO-Konfiguration finden">
    Suche den Abschnitt „Single Sign-On (SSO)“ und klappe ihn aus.
  </Step>

  <Step title="Einrichtung starten">
    Klicke auf die Schaltfläche „SSO Provider Connection settings“, um die SSO-Einrichtung zu starten, und folge dem Assistenten.
  </Step>

  <Step title="Identity Provider konfigurieren">
    In deinem Identity Provider (z. B. Okta):

    * Neue SAML-Anwendung erstellen
    * SAML-Einstellungen mit den Informationen von Cursor konfigurieren
    * Just-in-Time-(JIT)-Bereitstellung einrichten
  </Step>

  <Step title="Domain verifizieren">
    Verifiziere die Domain deiner Nutzer in Cursor, indem du auf die Schaltfläche „Domain verification settings“ klickst.
  </Step>
</Steps>

<div id="identity-provider-setup-guides">
  ### Anleitungen zur Einrichtung von Identity Providern
</div>

Für anbieterbezogene Einrichtungsanleitungen:

<Card title="Identity Provider Guides" icon="book" href="https://workos.com/docs/integrations">
  Einrichtungsanleitungen für Okta, Azure AD, Google Workspace und mehr.
</Card>

<div id="additional-settings">
  ## Zusätzliche Einstellungen
</div>

* SSO-Erzwingung im Admin-Dashboard verwalten
* Neue Nutzer werden bei der Anmeldung über SSO automatisch aufgenommen
* Nutzerverwaltung über deinen Identity Provider steuern

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

Wenn Probleme auftreten:

* Prüf, ob die Domain in Cursor verifiziert ist
* Stell sicher, dass SAML-Attribute korrekt zugeordnet sind
* Prüf, ob SSO im Admin-Dashboard aktiviert ist
* Gleiche Vor- und Nachnamen zwischen Identity Provider und Cursor ab
* Schau dir die anbieter­spezifischen Anleitungen oben an
* Schreib an [hi@cursor.com](mailto:hi@cursor.com), wenn die Probleme weiter bestehen



# Update-Zugriff
Source: https://docs.cursor.com/de/account/update-access

Wähle, wie oft du Updates bekommst

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor hat zwei Update-Kanäle.

<Tabs>
  <Tab title="Default">
    Der Standard-Update-Kanal mit getesteten Releases.

    * Stabile Releases
    * Bugfixes aus dem Pre-Release-Testing
    * Standard für alle Nutzer
    * Einzige Option für Team-Nutzer

    <Note>
      Team- und Business-Accounts verwenden den Default-Modus.
    </Note>
  </Tab>

  <Tab title="Early Access">
    Vorabversionen mit neuen Features.

    <Warning>
      Early-Access-Builds können Bugs oder Stabilitätsprobleme haben.
    </Warning>

    * Zugriff auf Features in Entwicklung
    * Kann Bugs enthalten
    * Nicht verfügbar für Team-Accounts
  </Tab>
</Tabs>

<div id="change-update-channel">
  ## Update-Kanal ändern
</div>

1. **Einstellungen öffnen**: Drück <Kbd>Cmd+Shift+J</Kbd>
2. **Zu Beta gehen**: Wähl Beta in der Seitenleiste
3. **Kanal auswählen**: Wähl Default oder Early Access

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=36c55c2deb93bc734b6ee0099a0d184c" data-og-width="1798" width="1798" data-og-height="442" height="442" data-path="images/account/early-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=624bfea7b3643f55afaa85b38b1c56e1 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f32c8e59596f024223735b4f929949e0 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd8c4bf3265ab802b6188aa81a620244 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8600f42cc363c61377f158972187e01 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=32c83b2109587d299959c2d46ce67353 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/early-access.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b2c4032824d39c62a7cbada5578b1a98 2500w" />
</Frame>

Meld Early-Access-Probleme im [Forum](https://forum.cursor.com).



# Apply
Source: https://docs.cursor.com/de/agent/apply

Lerne, wie du Codevorschläge aus dem Chat mit Apply übernehmen, akzeptieren oder ablehnen kannst

<div id="how-apply-works">
  ## Wie Apply funktioniert
</div>

Apply ist ein spezialisiertes Cursor-Modell, das von Chat generierten Code übernimmt und in deine Dateien integriert. Es verarbeitet die Codeblöcke aus Chat-Unterhaltungen und wendet die Änderungen auf deine Codebase an.

Apply generiert selbst keinen Code. Das Chat-Modell erzeugt den Code, und Apply übernimmt die Integration in bestehende Dateien. Es kann Änderungen über mehrere Dateien und große Codebases hinweg verarbeiten.

<div id="apply-code-blocks">
  ## Codeblöcke anwenden
</div>

Um einen Codeblock-Vorschlag anzuwenden, klick auf den Play-Button oben rechts im Codeblock.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
</Frame>



# Checkpoints
Source: https://docs.cursor.com/de/agent/chat/checkpoints

Frühere Zustände nach Agent-Änderungen speichern und wiederherstellen

Checkpoints sind automatische Snapshots der Änderungen des Agents an deinem Codebase. Damit kannst du Agent-Änderungen bei Bedarf rückgängig machen.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Checkpoints wiederherstellen
</div>

Zwei Möglichkeiten zur Wiederherstellung:

1. **Über das Eingabefeld**: Klicke bei vorherigen Anfragen auf den Button „Restore Checkpoint“
2. **Über die Nachricht**: Klicke auf den „+“-Button, wenn du mit der Maus über eine Nachricht fährst

<Warning>
  Checkpoints sind keine Versionsverwaltung. Nutze Git für dauerhafte Historie.
</Warning>

<div id="how-they-work">
  ## So funktionieren sie
</div>

* Lokal gespeichert, getrennt von Git
* Es werden nur Agent-Änderungen nachverfolgt (keine manuellen Änderungen)
* Wird automatisch bereinigt

<Note>
  Manuelle Änderungen werden nicht nachverfolgt. Verwende Checkpoints nur für Agent-Änderungen.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Beeinflussen Checkpoints Git?">
    Nein. Sie sind getrennt vom Git-Verlauf.
  </Accordion>

  {" "}

  <Accordion title="Wie lange werden sie aufbewahrt?">
    Für die aktuelle Sitzung und die jüngste Historie. Wird automatisch bereinigt.
  </Accordion>

  <Accordion title="Kann ich sie manuell erstellen?">
    Nein. Sie werden automatisch von Cursor erstellt.
  </Accordion>
</AccordionGroup>

{" "}



# Commands
Source: https://docs.cursor.com/de/agent/chat/commands

Definiere Befehle für wiederverwendbare Workflows

Benutzerdefinierte Commands ermöglichen dir, wiederverwendbare Workflows zu erstellen, die mit einem einfachen `/`-Prefix im Chat-Eingabefeld ausgelöst werden können. Diese Commands helfen, Prozesse in deinem Team zu standardisieren und machen häufige Aufgaben effizienter.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Commands befinden sich derzeit in der Beta. Die Funktion und die Syntax können sich ändern, während wir sie weiter verbessern.
</Info>

<div id="how-commands-work">
  ## Wie Befehle funktionieren
</div>

Befehle sind als einfache Markdown-Dateien definiert und können an zwei Orten gespeichert werden:

1. **Projektbefehle**: Gespeichert im Verzeichnis `.cursor/commands` deines Projekts
2. **Globale Befehle**: Gespeichert im Verzeichnis `~/.cursor/commands` in deinem Home-Verzeichnis

Wenn du im Chat-Eingabefeld `/` tippst, erkennt Cursor automatisch verfügbare Befehle aus beiden Verzeichnissen und zeigt sie an – so sind sie in deinem Workflow sofort verfügbar.

<div id="creating-commands">
  ## Befehle erstellen
</div>

1. Lege im Projekt-Root ein Verzeichnis `.cursor/commands` an
2. Füge `.md`-Dateien mit aussagekräftigen Namen hinzu (z. B. `review-code.md`, `write-tests.md`)
3. Schreib einfachen Markdown-Text, der beschreibt, was der Befehl tun soll
4. Befehle erscheinen automatisch im Chat, wenn du `/` eingibst

So könnte die Struktur deines `commands`-Verzeichnisses aussehen:

```
.cursor/
└── commands/
    ├── github-pr-kommentare-beantworten.md
    ├── code-review-checkliste.md
    ├── pr-erstellen.md
    ├── bestehende-diffs-kurz-prüfen.md
    ├── neuen-entwickler-onboarden.md
    ├── alle-tests-ausführen-und-fixen.md
    ├── sicherheitsaudit.md
    └── neue-funktion-einrichten.md
```

<div id="examples">
  ## Beispiele
</div>

Probier diese Befehle in deinen Projekten aus, um ein Gefühl dafür zu bekommen, wie sie funktionieren.

<AccordionGroup>
  <Accordion title="Code-Review-Checkliste">
    ```markdown  theme={null}
    # Code-Review-Checkliste

    ## Überblick
    Umfassende Checkliste für gründliche Code-Reviews, um Qualität, Sicherheit und Wartbarkeit sicherzustellen.

    ## Review-Kategorien

    ### Funktionalität
    - [ ] Code macht, was er soll
    - [ ] Edge Cases werden abgedeckt
    - [ ] Fehlerbehandlung ist angemessen
    - [ ] Keine offensichtlichen Bugs oder Logikfehler

    ### Codequalität
    - [ ] Code ist gut lesbar und strukturiert
    - [ ] Funktionen sind klein und fokussiert
    - [ ] Variablennamen sind aussagekräftig
    - [ ] Kein doppelter Code
    - [ ] Hält Projektkonventionen ein

    ### Sicherheit
    - [ ] Keine offensichtlichen Sicherheitslücken
    - [ ] Eingabevalidierung vorhanden
    - [ ] Sensible Daten werden korrekt gehandhabt
    - [ ] Keine hardcodierten Secrets
    ```
  </Accordion>

  <Accordion title="Sicherheitsaudit">
    ```markdown  theme={null}
    # Security Audit

    ## Überblick
    Umfassende Sicherheitsüberprüfung zur Identifizierung und Behebung von Schwachstellen im Codebase.

    ## Schritte
    1. **Dependency-Audit**
       - Auf bekannte Schwachstellen prüfen
       - Veraltete Pakete aktualisieren
       - Third-Party-Dependencies überprüfen

    2. **Code Security Review**
       - Auf gängige Schwachstellen prüfen
       - Authentifizierung/Autorisierung überprüfen
       - Datenverarbeitungspraktiken prüfen

    3. **Infrastructure Security**
       - Umgebungsvariablen überprüfen
       - Zugriffssteuerungen prüfen
       - Netzwerksicherheit prüfen

    ## Security Checklist
    - [ ] Dependencies aktualisiert und sicher
    - [ ] Keine hardcodierten Secrets
    - [ ] Eingabevalidierung implementiert
    - [ ] Authentifizierung sicher
    - [ ] Autorisierung korrekt konfiguriert
    ```
  </Accordion>

  <Accordion title="Neue Funktion einrichten">
    ```markdown  theme={null}
    # Neue Funktion einrichten

    ## Überblick
    Eine neue Funktion systematisch vom initialen Plan bis zur Implementierungsstruktur aufsetzen.

    ## Schritte
    1. **Anforderungen definieren**
       - Funktionsumfang und Ziele klären
       - User Stories und Akzeptanzkriterien festlegen
       - Technischen Ansatz planen

    2. **Feature-Branch erstellen**
       - Von main/develop abzweigen
       - Lokale Entwicklungsumgebung aufsetzen
       - Neue Abhängigkeiten konfigurieren

    3. **Architektur planen**
       - Datenmodelle und APIs entwerfen
       - UI-Komponenten und Flows planen
       - Teststrategie definieren

    ## Checkliste für das Feature-Setup
    - [ ] Anforderungen dokumentiert
    - [ ] User Stories geschrieben
    - [ ] Technischer Ansatz geplant
    - [ ] Feature-Branch erstellt
    - [ ] Entwicklungsumgebung bereit
    ```
  </Accordion>

  <Accordion title="Pull Request erstellen">
    ```markdown  theme={null}
    # PR erstellen

    ## Überblick
    Erstelle einen gut strukturierten Pull Request mit klarer Beschreibung, passenden Labels und Reviewern.

    ## Schritte
    1. **Branch vorbereiten**
       - Sicherstellen, dass alle Änderungen committed sind
       - Branch zum Remote pushen
       - Prüfen, dass der Branch mit main auf dem neuesten Stand ist

    2. **PR-Beschreibung schreiben**
       - Änderungen klar zusammenfassen
       - Kontext und Motivation angeben
       - Breaking Changes auflisten
       - Screenshots hinzufügen, wenn es UI-Änderungen gibt

    3. **PR einrichten**
       - PR mit aussagekräftigem Titel erstellen
       - Passende Labels hinzufügen
       - Reviewer zuweisen
       - Zugehörige Issues verlinken

    ## PR-Vorlage
    - [ ] Feature A
    - [ ] Bugfix B
    - [ ] Unit-Tests bestehen
    - [ ] Manuelles Testen abgeschlossen
    ```
  </Accordion>

  <Accordion title="Tests ausführen und Fehler beheben">
    ```markdown  theme={null}
    # Alle Tests ausführen und Fehler beheben

    ## Übersicht
    Führe die vollständige Testsuite aus und behebe systematisch alle Fehlerschläge, um Codequalität und Funktionalität sicherzustellen.

    ## Schritte
    1. **Testsuite ausführen**
       - Alle Tests im Projekt ausführen
       - Ausgabe erfassen und fehlgeschlagene Tests identifizieren
       - Sowohl Unit- als auch Integrationstests prüfen

    2. **Fehler analysieren**
       - Nach Typ kategorisieren: flaky, defekt, neu
       - Fixes nach Impact priorisieren
       - Prüfen, ob Fehler mit jüngsten Änderungen zusammenhängen

    3. **Probleme systematisch beheben**
       - Mit den kritischsten Fehlern beginnen
       - Ein Problem nach dem anderen beheben
       - Tests nach jedem Fix erneut ausführen
    ```
  </Accordion>

  <Accordion title="Neuen Entwickler onboarden">
    ```markdown  theme={null}
    # Neue·n Developer onboarden

    ## Übersicht
    Umfassender Onboarding‑Prozess, um einen neuen Developer schnell startklar zu machen.

    ## Schritte
    1. **Environment‑Setup**
       - Erforderliche Tools installieren
       - Entwicklungsumgebung einrichten
       - IDE und Extensions konfigurieren
       - Git und SSH‑Keys einrichten

    2. **Projekteinstieg**
       - Projektstruktur durchgehen
       - Architektur verstehen
       - Wichtige Doku lesen
       - Lokale Datenbank einrichten

    ## Onboarding‑Checkliste
    - [ ] Entwicklungsumgebung bereit
    - [ ] Alle Tests grün
    - [ ] Anwendung lokal startbar
    - [ ] Datenbank eingerichtet und funktionsfähig
    - [ ] Erste·r PR erstellt
    ```
  </Accordion>
</AccordionGroup>



# Kompakt
Source: https://docs.cursor.com/de/agent/chat/compact

Spare Platz im Chat mit der Oberfläche im Kompaktmodus

Der Kompaktmodus bietet eine schlanke Chat-Oberfläche, indem er visuelles Clutter reduziert und den verfügbaren Platz für Unterhaltungen maximiert.

<div id="overview">
  ## Übersicht
</div>

Wenn aktiviert, optimiert der Kompaktmodus die Chat-Oberfläche durch:

* **Ausblenden von Symbolen** für ein cleaneres, minimalistisches Erscheinungsbild
* **Automatisches Einklappen von Diffs**, um visuelles Rauschen zu reduzieren
* **Automatisches Einklappen des Eingabefelds**, um mehr Platz für die Unterhaltung zu schaffen

Diese Einstellung ist besonders nützlich, wenn du auf kleineren Bildschirmen arbeitest oder eine fokussierte, ablenkungsfreie Chat-Erfahrung bevorzugst.

<div id="before-and-after">
  ## Vorher und nachher
</div>

<div id="default-mode">
  ### Standardmodus
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e0f8b97ecd5201be396fcd09cec54de6" alt="Chat-Oberfläche im Standardmodus mit allen Symbolen und ausgeklappten Elementen" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/off.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9395c8d1f324033631508dc9cdfd6f3e 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d8025ef65ad2fc9fe8c30e5c4fcda32 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=28050b27b683af948bc1ed939f31786c 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=dc443705188da9d3368acefd917cc890 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=be6603e2cedb7e88e7c20d797b18599c 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/compact/off.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3afe563c9cd4576623adce5dcaaccddf 2500w" />
</Frame>

<div id="compact-mode">
  ### Kompaktmodus
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e9f068889026827422b2a9d943b55ded" alt="Chat-Oberfläche im Kompaktmodus mit ausgeblendeten Symbolen und eingeklappten Elementen" data-og-width="2048" width="2048" data-og-height="2350" height="2350" data-path="images/chat/compact/on.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=44e86a79eb893b4de6c57c65487bbe9a 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=539b71c72ed2fb3508e3aec0624429c1 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2c0da715a5daf93e94dbf2a5eefbb7eb 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b5bddca39109779c9d91bb6bc8bb42e9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bb334bb055e49d4d51cd137d2396db0 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/compact/on.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=70730d151a24440eeb6dc31e18189c7d 2500w" />
</Frame>

<div id="enabling-compact-mode">
  ## Kompaktmodus aktivieren
</div>

So aktivierst du den Kompaktmodus:

1. Öffne die Cursor-Einstellungen
2. Navigiere zu den **Chat**-Einstellungen
3. Aktiviere den **Kompaktmodus**

Die Oberfläche wechselt sofort zur schlankeren Ansicht und gibt dir mehr Platz, dich auf deine Unterhaltungen zu konzentrieren.



# Duplizieren
Source: https://docs.cursor.com/de/agent/chat/duplicate

Erstelle Branches von beliebigen Punkten in einer Unterhaltung

Dupliziere bzw. forke Chats, um alternative Lösungen zu erkunden, ohne deine aktuelle Unterhaltung zu verlieren.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/duplicate-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=29fdb23214ba3e2c5b94ccefc01f7615" autoPlay loop muted playsInline controls data-path="images/chat/duplicate-chat.mp4" />
</Frame>

<div id="how-to-duplicate">
  ## So duplizierst du
</div>

1. Finde die Stelle, an der du abzweigen willst
2. Klicke auf die drei Punkte der Nachricht
3. Wähle „Duplicate Chat“ aus

<div id="what-happens">
  ## Was passiert
</div>

* Der bisherige Kontext bleibt erhalten
* Die ursprüngliche Unterhaltung bleibt unverändert
* Beide Chats behalten ihre eigene, separate Historie



# Export
Source: https://docs.cursor.com/de/agent/chat/export

Chats ins Markdown-Format exportieren

Agent-Chats als Markdown-Dateien für das Teilen oder die Dokumentation exportieren.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
</Frame>

<div id="whats-exported">
  ## Was exportiert wird
</div>

* Alle Nachrichten und Antworten
* Codeblöcke mit Syntaxhervorhebung
* Dateiverweise und Kontext
* Chronologischer Gesprächsverlauf

<div id="how-to-export">
  ## So exportierst du
</div>

1. Navigier zum Chat, den du exportieren willst
2. Klick aufs Kontextmenü → „Chat exportieren“
3. Speichere die Datei lokal

<Warning>
  Prüf Exporte auf sensible Daten: API-Schlüssel, interne URLs, proprietären Code,
  personenbezogene Informationen
</Warning>



# Verlauf
Source: https://docs.cursor.com/de/agent/chat/history

Chat-Unterhaltungen anzeigen und verwalten

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Greif im Verlaufspanel auf frühere Agent-Chats zu.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chatverlauf" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
</Frame>

<div id="opening-history">
  ## Verlauf öffnen
</div>

* Klick auf das Verlaufssymbol in der Agent-Seitenleiste
* Drück <Kbd tooltip="Chatverlauf öffnen">Opt Cmd '</Kbd>

<div id="managing-chats">
  ## Chats verwalten
</div>

* **Titel bearbeiten**: Klicken zum Umbenennen
* **Löschen**: Nicht benötigte Chats entfernen
* **Öffnen**: Klicken, um die gesamte Unterhaltung anzusehen

Der Chatverlauf wird lokal in einer SQLite-Datenbank auf deinem Rechner gespeichert.

<Note>
  Um Chats zu behalten, [exportier sie](/de/agent/chats/export) als Markdown.
</Note>

<div id="background-agents">
  ## Hintergrund-Agents
</div>

Chats mit Hintergrund-Agents erscheinen nicht in der normalen Historie, sondern werden in einer Remote-Datenbank gespeichert. Verwende <Kbd tooltip="Open background agent control panel">Cmd E</Kbd>, um sie anzusehen.

<div id="referencing-past-chats">
  ## Auf frühere Chats verweisen
</div>

Verwende [@Past Chats](/de/context/@-symbols/@-past-chats), um Kontext aus vorherigen Gesprächen in deinem aktuellen Chat einzubeziehen.



# Zusammenfassung
Source: https://docs.cursor.com/de/agent/chat/summarization

Kontextmanagement für lange Chats

<div id="message-summarization">
  ## Zusammenfassung von Nachrichten
</div>

Wenn Unterhaltungen länger werden, fasst Cursor automatisch zusammen und verwaltet den Kontext, damit deine Chats effizient bleiben. Lern, wie du das Kontextmenü nutzt, und versteh, wie Dateien verdichtet werden, damit sie in die Kontextfenster des Modells passen.

<div id="using-the-summarize-command">
  ### Verwendung des Befehls /summarize
</div>

Du kannst die Zusammenfassung manuell mit dem Befehl `/summarize` im Chat auslösen. Dieser Befehl hilft dabei, den Kontext zu verwalten, wenn Unterhaltungen zu lang werden, sodass du effizient weiterarbeiten kannst, ohne wichtige Informationen zu verlieren.

<Info>
  Für einen tieferen Einblick, wie Kontext in Cursor funktioniert, schau dir unseren Guide [Mit
  Kontext arbeiten](/de/guides/working-with-context) an.
</Info>

<div id="how-summarization-works">
  ### So funktioniert die Zusammenfassung
</div>

Wenn Unterhaltungen länger werden, überschreiten sie das Kontextfensterlimit des Modells:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Kontextfensterlimit</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Um das zu lösen, fasst Cursor ältere Nachrichten zusammen, damit Platz für neue Unterhaltungsteile entsteht.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Kontextfensterlimit
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Zusammengefasste Nachrichten
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

## Komprimierung von Dateien & Ordnern

Während die Chatszusammenfassung lange Unterhaltungen abdeckt, nutzt Cursor für große Dateien und Ordner eine andere Strategie: **smarte Komprimierung**. Wenn du Dateien in deine Unterhaltung einbindest, ermittelt Cursor anhand ihrer Größe und des verfügbaren Kontextbereichs die beste Darstellung.

Das sind die verschiedenen Zustände, in denen sich eine Datei/ein Ordner befinden kann:

<div id="condensed">
  ### Kompaktansicht
</div>

Wenn Dateien oder Ordner zu groß für das Kontextfenster sind, komprimiert Cursor sie automatisch. In der Kompaktansicht sieht das Modell zentrale Strukturelemente wie Funktionssignaturen, Klassen und Methoden. Aus dieser kompakten Darstellung kann das Modell bei Bedarf einzelne Dateien aufklappen. So wird das verfügbare Kontextfenster optimal genutzt.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Kontextmenü" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Stark gekürzt
</div>

Wenn ein Dateiname mit der Kennzeichnung „Stark gekürzt“ erscheint, war die Datei zu groß, um selbst in gekürzter Form vollständig aufgenommen zu werden. Dem Modell wird nur der Dateiname angezeigt.

<div id="not-included">
  ### Nicht enthalten
</div>

Wenn neben einer Datei oder einem Ordner ein Warnsymbol angezeigt wird, ist das Element zu groß, um in das Kontextfenster aufgenommen zu werden – selbst in komprimierter Form. So siehst du, welche Teile deiner Codebase für das Modell zugänglich sind.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context-Menü" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>



# Tabs
Source: https://docs.cursor.com/de/agent/chat/tabs

Mehrere Agent-Chats gleichzeitig führen

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
</Frame>

<div id="overview">
  ## Überblick
</div>

Drück <Kbd>Cmd+T</Kbd>, um neue Tabs zu öffnen. Jeder Tab hat eine eigene Gesprächshistorie, seinen eigenen Kontext und die ausgewählte Modellkonfiguration.

<Tip>
  Für parallele Workflows, probier mal die [Background Agents](/de/background-agents) aus
</Tip>

<div id="managing-tabs">
  ## Tabs verwalten
</div>

* Erstelle neue Tabs mit <Kbd>Cmd+T</Kbd>. Jeder Tab startet mit einer neuen Unterhaltung und behält seinen eigenen Kontext.

* Wechsle zwischen Tabs, indem du auf ihre Titel klickst, oder nutze <Kbd>Ctrl+Tab</Kbd>, um durch sie zu blättern.

* Tab-Titel werden nach der ersten Nachricht automatisch erstellt, aber du kannst sie umbenennen, indem du mit der rechten Maustaste auf den Tab-Titel klickst.

<Tip>
  Nutze pro Tab nur eine Aufgabe, gib eine klare Anfangsbeschreibung und schließe
  erledigte Tabs, um deinen Arbeitsbereich aufgeräumt zu halten.
</Tip>

<div id="conflicts">
  ### Konflikte
</div>

Cursor verhindert, dass mehrere Tabs dieselben Dateien bearbeiten. Du wirst aufgefordert, Konflikte zu lösen.

<div id="reference-other-chats">
  ## Auf andere Chats verweisen
</div>

Verwende [@Past Chats](/de/context/@-symbols/@-past-chats), um Kontext aus anderen Tabs oder vorherigen Sitzungen einzubinden.



# Modi
Source: https://docs.cursor.com/de/agent/modes

Wähl den richtigen Modus für deine Aufgabe – von autonomem Codieren bis zu fokussierten Edits

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent bietet verschiedene Modi, die für bestimmte Aufgaben optimiert sind. Jeder Modus hat unterschiedliche Fähigkeiten und aktivierte Tools, die zu deinem Workflow passen.

<div className="full-width-table">
  | Modus                 | Für                            | Fähigkeiten                                            | Tools                |
  | :-------------------- | :----------------------------- | :----------------------------------------------------- | :------------------- |
  | **[Agent](#agent)**   | Komplexe Features, Refactoring | Autonome Exploration, Bearbeitung über mehrere Dateien | Alle Tools aktiviert |
  | **[Ask](#ask)**       | Lernen, Planung, Fragen        | Nur Lesezugriff, keine automatischen Änderungen        | Nur Such-Tools       |
  | **[Custom](#custom)** | Spezialisierte Workflows       | Benutzerdefinierte Fähigkeiten                         | Konfigurierbar       |
</div>

<div id="agent">
  ## Agent
</div>

Der Standardmodus für komplexe Coding-Aufgaben. Agent erkundet eigenständig deinen Code, bearbeitet mehrere Dateien, führt Befehle aus und behebt Fehler, um deine Requests zu erfüllen.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
</Frame>

<div id="ask">
  ## Ask
</div>

Schreibgeschützter Modus zum Lernen und Erkunden. Ask durchsucht deine Codebasis und liefert Antworten, ohne Änderungen vorzunehmen – perfekt, um Code zu verstehen, bevor du ihn änderst.

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=15e531cb84f0a18228723870fd84fa4f" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/ask.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=592ac5a681910a075ae88dec89bee25d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=74b98cce3b5bb83c79d0566cd3c65c34 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=c4d80f50e20e7ca28db5a3ee71718979 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a4a6e017fd64149cf68d997114bbf6b6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7354479ecd644b86ddbcb9fe1131f100 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/ask.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=274125e614eadd17522e0dacfcc6a38e 2500w" />
</Frame>

<div id="custom">
  ## Benutzerdefiniert
</div>

Erstelle eigene Modi mit spezifischen Tool-Kombinationen und Anweisungen. Kombiniere und variiere Fähigkeiten, um deinen Workflow optimal zu unterstützen.

<Note>
  Benutzerdefinierte Modi sind in der Beta. Aktiviere sie in `Cursor Settings` → `Chat` → `Custom
      Modes`
</Note>

<div id="examples">
  ### Beispiele
</div>

<AccordionGroup>
  <Accordion title="Learn">
    **Tools:** All Search\
    **Instructions:** Erkläre Konzepte gründlich und stell gezielte Rückfragen zur Klärung
  </Accordion>

  {" "}

  <Accordion title="Refactor">
    **Tools:** Edit & Reapply **Instructions:** Verbessere die Codestruktur, ohne neue Funktionalität hinzuzufügen
  </Accordion>

  {" "}

  <Accordion title="Plan">
    **Tools:** Codebase, Read file, Terminal **Instructions:** Erstelle detaillierte Implementierungspläne in `plan.md`
  </Accordion>

  <Accordion title="Debug">
    **Tools:** All Search, Terminal, Edit & Reapply\
    **Instructions:** Untersuche Probleme gründlich, bevor du Fixes vorschlägst
  </Accordion>
</AccordionGroup>

<div id="switching-modes">
  ## Modi wechseln
</div>

* Nutze den Moduswähler in Agent
* Drück <Kbd>Cmd+.</Kbd>, um schnell zu wechseln
* Leg Tastenkürzel in den [Einstellungen](#settings) fest

<div id="settings">
  ## Einstellungen
</div>

Alle Modi teilen sich gemeinsame Konfigurationsoptionen:

<div className="full-width-table">
  | Einstellung  | Beschreibung                                      |
  | :----------- | :------------------------------------------------ |
  | Modell       | Wähle, welches KI‑Modell verwendet wird           |
  | Tastenkürzel | Lege Shortcuts fest, um zwischen Modi zu wechseln |
</div>

Modusspezifische Einstellungen:

<div className="full-width-table">
  | Modus      | Einstellungen                | Beschreibung                                                          |
  | :--------- | :--------------------------- | :-------------------------------------------------------------------- |
  | **Agent**  | Auto-Run und Auto-Fix Errors | Befehle automatisch ausführen und Fehler automatisch beheben          |
  | **Ask**    | Codebasis durchsuchen        | Relevante Dateien automatisch finden                                  |
  | **Custom** | Toolauswahl & Anweisungen    | [tools](/de/agent/tools) und benutzerdefinierte Prompts konfigurieren |
</div>



# Überblick
Source: https://docs.cursor.com/de/agent/overview

Assistent für autonome Coding-Aufgaben, Terminalbefehle und Code-Editing

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent ist der Assistent von Cursor, der komplexe Coding-Aufgaben eigenständig erledigen, Terminalbefehle ausführen und Code bearbeiten kann. Du erreichst ihn im Seitenbereich mit <Kbd>Cmd+I</Kbd>.

<Frame caption="Agent im Seitenbereich">
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/overview.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b17d6a1225b4992ea19978b6a6c259e1" autoPlay loop muted playsInline data-path="images/chat/overview.mp4" />
</Frame>

<div className="mt-24 flex flex-col gap-12">
  <Columns className="gap-4">
    <div>
      <h2 className="text-lg font-medium mb-2">
        <a href="/de/agent/modes" className="hover:text-primary transition-colors">
          Modi
        </a>
      </h2>

      <p className="text-sm">
        Wähle zwischen Agent, Ask oder erstelle eigene Modi. Jeder Modus bietet
        unterschiedliche Funktionen und Tools, die zu deinem Workflow passen.
      </p>
    </div>

    <Frame>
      <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9cd06dd9f59e019b3d76aa0fd9f934ba" alt="Agent-Modi" data-og-width="3600" width="3600" data-og-height="2025" height="2025" data-path="images/chat/agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d979435c61e2112ebcb784f16a49327f 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1a88e2085ffe80f02daea9a523887282 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=de98a8bf766c3f35a6187e87190e30f9 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8648638c4240b718e0512a6ec2274171 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=45b9898d65f5b425d276eaa44d4e1940 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/agent.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=30fef2b190d453ee0166e554a4005bd1 2500w" />
    </Frame>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/tools" className="hover:text-primary transition-colors">
          Tools
        </a>
      </h3>

      <p className="text-sm">
        Agent nutzt Tools, um zu suchen, zu bearbeiten und Befehle auszuführen. Von semantischer Codebase-Suche bis zur Terminalausführung ermöglichen diese Tools eine autonome Aufgabenerledigung.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Agent-Tools" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/apply" className="hover:text-primary transition-colors">
          Änderungen anwenden
        </a>
      </h3>

      <p className="text-sm">
        Integriere von der KI vorgeschlagene Codeblöcke in deine Codebase. Apply verarbeitet
        umfangreiche Änderungen effizient und bleibt dabei präzise.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=634492fa2f63b4f6eada08b2a1ded47e" alt="Änderungen anwenden" data-og-width="1032" width="1032" data-og-height="410" height="410" data-path="images/chat/apply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7dbc88cfe20429c73e627a289b17c964 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=721e2d51bdb16dbb817e19d96d93c9d9 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=8faea188ca903e58d347ddfec2c9bf6e 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f3bc38701cab63602b54374dfaa9e024 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fddad51f5b12c32493e2370ed326712d 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/apply.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1584d431007b33a595905e23b5e1b453 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/review" className="hover:text-primary transition-colors">
          Diffs überprüfen
        </a>
      </h3>

      <p className="text-sm">
        Schau dir Änderungen an, bevor du sie annimmst. Die Review-Oberfläche zeigt Hinzufügungen
        und Löschungen mit farbcodierten Zeilen, damit du Modifikationen im Griff hast.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/chats/tabs" className="hover:text-primary transition-colors">
          Chat-Tabs
        </a>
      </h3>

      <p className="text-sm">
        Führ mehrere Unterhaltungen parallel mit <Kbd>Cmd+T</Kbd> aus. Jeder Tab
        behält seinen eigenen Kontext, Verlauf und die gewählte Modellkonfiguration.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-tabs.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=57fd5305279dc0a3139055b353ce4b7a" autoPlay loop muted playsInline controls data-path="images/chat/chat-tabs.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/chats/checkpoints" className="hover:text-primary transition-colors">
          Checkpoints
        </a>
      </h3>

      <p className="text-sm">
        Automatische Snapshots protokollieren die Änderungen des Agents. Stell frühere Zustände wieder her, wenn
        Änderungen nicht wie erwartet funktionieren oder um verschiedene Ansätze auszuprobieren.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/terminal" className="hover:text-primary transition-colors">
          Terminal-Integration
        </a>
      </h3>

      <p className="text-sm">
        Agent führt Terminalbefehle aus, überwacht die Ausgabe und steuert mehrstufige
        Prozesse. Konfigurier Auto-Run für vertrauenswürdige Workflows oder fordere
        zur Sicherheit eine Bestätigung an.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" alt="Terminal-Integration" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/chats/history" className="hover:text-primary transition-colors">
          Chatverlauf
        </a>
      </h3>

      <p className="text-sm">
        Öffne frühere Unterhaltungen mit <Kbd>Opt Cmd '</Kbd>. Schau dir vergangene
        Diskussionen an, tracke Coding-Sessions und nutze Kontext aus früheren
        Chats.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d9ec96fad0c8c2fb132bbf5ce8ea35f7" alt="Chatverlauf" data-og-width="2048" width="2048" data-og-height="1317" height="1317" data-path="images/chat/chat-history.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a3ad71e9891c3c9642f4288953a78e97 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76139a177ebfeb0c55add7fb955f9000 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1af22180859c017542777ab36b434b7a 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=751e7fa0888e5790f841432ef7521337 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=86b447c18601a9d44af8866d0042719e 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/chat-history.jpeg?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=88c84a8fb1b764ad3070e3211f539408 2500w" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/agent/chats/export" className="hover:text-primary transition-colors">
          Chats exportieren
        </a>
      </h3>

      <p className="text-sm">
        Unterhaltungen als Markdown exportieren. Lösungen mit Teammitgliedern teilen,
        Entscheidungen dokumentieren oder Wissensbasen aus Coding-Sessions erstellen.
      </p>
    </div>

    <div>
      <Frame>
        <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/export-chat.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6aa9d23a6a80ffae5864cd494907961" autoPlay loop muted playsInline controls data-path="images/chat/export-chat.mp4" />
      </Frame>
    </div>
  </Columns>

  <Columns className="gap-4">
    <div>
      <h3 className="text-lg font-medium mb-2">
        <a href="/de/context/rules" className="hover:text-primary transition-colors">
          Regeln
        </a>
      </h3>

      <p className="text-sm">
        Definiere eigene Anweisungen für das Verhalten von Agent. Regeln helfen, Coding-Standards einzuhalten, Muster durchzusetzen und zu personalisieren, wie Agent dich bei deinem Projekt unterstützt.
      </p>
    </div>

    <div>
      <Frame>
        <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Agent-Regeln" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
      </Frame>
    </div>
  </Columns>
</div>



# Planung
Source: https://docs.cursor.com/de/agent/planning

Wie Agent komplexe Aufgaben mit To-dos und Warteschlangen plant und verwaltet

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent kann vorausplanen und komplexe Aufgaben mit strukturierten To-do-Listen und Message-Queuing verwalten – so bleiben langfristige Tasks leichter nachvollziehbar und verständlich.

<div id="agent-to-dos">
  ## Agent-To-dos
</div>

Agent kann längere Aufgaben in überschaubare Schritte mit Abhängigkeiten aufteilen und so einen strukturierten Plan erstellen, der sich während der Arbeit laufend aktualisiert.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### So funktioniert’s
</div>

* Agent erstellt automatisch To-do-Listen für komplexe Aufgaben
* Jeder Eintrag kann Abhängigkeiten zu anderen Aufgaben haben
* Die Liste aktualisiert sich in Echtzeit, während die Arbeit voranschreitet
* Abgeschlossene Aufgaben werden automatisch abgehakt

<div id="visibility">
  ### Sichtbarkeit
</div>

* To-dos erscheinen in der Chat-Oberfläche
* Wenn die [Slack-Integration](/de/slack) eingerichtet ist, sind To-dos auch dort sichtbar
* Du kannst die vollständige Aufgabenübersicht jederzeit ansehen

<Tip>
  Für bessere Planung: Beschreibe dein Endziel klar. Agent erstellt
  genauere Aufgabenaufteilungen, wenn der gesamte Umfang klar ist.
</Tip>

<Note>Planung und To-dos werden derzeit im Auto-Modus nicht unterstützt.</Note>

<div id="queued-messages">
  ## Nachrichten in der Warteschlange
</div>

Stell Folge­nachrichten in die Warteschlange, während Agent an der aktuellen Aufgabe arbeitet. Deine Anweisungen warten der Reihe nach und werden automatisch ausgeführt, sobald sie dran sind.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Warteschlange verwenden
</div>

1. Während Agent arbeitet, tipp deine nächste Anweisung
2. Drück <Kbd>Ctrl+Enter</Kbd>, um sie zur Warteschlange hinzuzufügen
3. Nachrichten erscheinen der Reihe nach unter der aktiven Aufgabe
4. Ändere die Reihenfolge der wartenden Nachrichten, indem du auf den Pfeil klickst
5. Agent verarbeitet sie der Reihe nach, sobald er fertig ist

<div id="override-the-queue">
  ### Warteschlange überschreiben
</div>

Um deine Nachricht in die Warteschlange zu stellen statt die Standardübermittlung zu verwenden, nutz <Kbd>Ctrl+Enter</Kbd>. Um eine Nachricht sofort ohne Warteschlange zu senden, nutz <Kbd>Cmd+Enter</Kbd>. Das „force-pusht“ deine Nachricht, umgeht die Warteschlange und führt sie sofort aus.

<div id="default-messaging">
  ## Standardnachrichten
</div>

Nachrichten werden standardmäßig so schnell wie möglich gesendet und erscheinen in der Regel direkt, nachdem Agent einen Toolaufruf abgeschlossen hat. Das sorgt für die schnellstmögliche Reaktion.

<div id="how-default-messaging-works">
  ### So funktionieren Standardnachrichten
</div>

* Deine Nachricht wird an die zuletzt gesendete Nutzer-Nachricht im Chat angehängt
* Nachrichten werden normalerweise an Tool-Ergebnisse angehängt und sofort gesendet, sobald sie vorliegen
* Das sorgt für einen natürlicheren Gesprächsfluss, ohne die aktuelle Arbeit von Agent zu unterbrechen
* Standardmäßig passiert das, wenn du Enter drückst, während Agent arbeitet



# Diffs & Review
Source: https://docs.cursor.com/de/agent/review

Vom Agent generierte Codeänderungen überprüfen und verwalten

Wenn der Agent Codeänderungen erzeugt, werden sie in einer Review-Oberfläche angezeigt, die Hinzufügungen und Löschungen mit farbcodierten Zeilen darstellt. So kannst du prüfen und steuern, welche Änderungen in deiner Codebasis übernommen werden.

Die Review-Oberfläche zeigt Codeänderungen in einem vertrauten Diff-Format an:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Typ                     | Bedeutung                     | Beispiel                                                                                              |
  | :---------------------- | :---------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Hinzugefügte Zeilen** | Neue Codezeilen               | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Gelöschte Zeilen**    | Entfernte Codezeilen          | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Kontextzeilen**       | Unveränderter umgebender Code | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Review
</div>

Nachdem die Generierung abgeschlossen ist, siehst du eine Aufforderung, alle Änderungen zu überprüfen, bevor es weitergeht. So bekommst du einen Überblick darüber, was geändert wird.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Review-Eingabeoberfläche" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Datei für Datei
</div>

Unten auf deinem Bildschirm erscheint eine schwebende Review-Leiste, mit der du:

* Änderungen für die aktuelle Datei **annehmen** oder **ablehnen** kannst
* Zur **nächsten Datei** mit ausstehenden Änderungen springen kannst
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Dein Browser unterstützt das video-Tag nicht.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Selektive Annahme
</div>

Für fein abgestimmte Kontrolle:

* Um die meisten Änderungen anzunehmen: unerwünschte Zeilen ablehnen, dann auf **Alle annehmen** klicken
* Um die meisten Änderungen abzulehnen: gewünschte Zeilen annehmen, dann auf **Alle ablehnen** klicken

<div id="review-changes">
  ## Änderungen überprüfen
</div>

Klick am Ende der Agent-Antwort auf **Änderungen überprüfen**, um das vollständige Diff der Änderungen zu sehen.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>



# Terminal
Source: https://docs.cursor.com/de/agent/terminal

Terminalbefehle automatisch als Teil von Agent-Aktionen ausführen

Der Agent führt Befehle im nativen Terminal von Cursor aus, die History bleibt erhalten. Klick auf Skip, um <kbd>Strg+C</kbd> zu senden und Befehle abzubrechen.

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

<Info>
  Einige Shell-Themes (zum Beispiel Powerlevel9k/Powerlevel10k) können die
  Inline-Terminalausgabe stören. Wenn deine Befehlsausgabe abgeschnitten
  oder falsch formatiert wirkt, deaktiviere das Theme oder wechsle zu einer
  einfacheren Eingabeaufforderung, solange Agent läuft.
</Info>

<div id="disable-heavy-prompts-for-agent-sessions">
  ### Aufwendige Prompts für Agent-Sessions deaktivieren
</div>

Verwende die Umgebungsvariable `CURSOR_AGENT` in deiner Shell-Konfiguration, um zu erkennen,
wann Agent läuft, und überspring die Initialisierung von aufwendigen Prompts/Themes.

```zsh  theme={null}

# ~/.zshrc — Powerlevel10k deaktivieren, wenn der Cursor Agent läuft
if [[ -n "$CURSOR_AGENT" ]]; then
  # Theme-Initialisierung auslassen für bessere Kompatibilität
else
  [[ -r ~/.p10k.zsh ]] && source ~/.p10k.zsh
fi
```

```bash  theme={null}

# ~/.bashrc — in Agent-Sitzungen auf eine einfache Eingabeaufforderung zurückgreifen
if [[ -n "$CURSOR_AGENT" ]]; then
  PS1='\u@\h \W \$ '
fi
```



# Tools
Source: https://docs.cursor.com/de/agent/tools

Tools, die Agenten zum Suchen, Bearbeiten und Ausführen von Code zur Verfügung stehen

Eine Liste aller Tools, die den Modi innerhalb des [Agent](/de/agent/overview) zur Verfügung stehen und die du beim Erstellen deiner eigenen [Custom Modes](/de/agent/modes#custom) aktivieren oder deaktivieren kannst.

<Note>
  Es gibt kein Limit für die Anzahl der Tool-Aufrufe, die Agent während einer Aufgabe durchführen kann. Agent verwendet die Tools nach Bedarf weiter, bis deine Anfrage erfüllt ist.
</Note>

<div id="search">
  ## Suche
</div>

Tools, mit denen du deine Codebase und das Web durchsuchen kannst, um relevante Informationen zu finden.

<AccordionGroup>
  <Accordion title="Datei lesen" icon="file-lines">
    Liest bis zu 250 Zeilen (750 im Max-Modus) einer Datei.
  </Accordion>

  <Accordion title="Verzeichnis auflisten" icon="folder-open">
    Liest die Struktur eines Verzeichnisses, ohne Dateiinhalte zu öffnen.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Führe semantische Suchen in deiner [indizierten
    Codebase](/de/context/codebase-indexing) durch.
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Suche nach exakten Schlüsselwörtern oder Mustern in Dateien.
  </Accordion>

  <Accordion title="Dateien suchen" icon="file-magnifying-glass">
    Finde Dateien anhand des Namens mit Fuzzy-Matching.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Generiere Suchanfragen und führe Websuchen durch.
  </Accordion>

  <Accordion title="Regeln abrufen" icon="gavel">
    Rufe bestimmte [Regeln](/de/context/rules) basierend auf Typ und Beschreibung ab.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Edit
</div>

Tools, mit denen du gezielt Änderungen an deinen Dateien und in deinem Codebase vornimmst.

<AccordionGroup>
  <Accordion title="Edit & Reapply" icon="pencil">
    Schlage Änderungen an Dateien vor und [wende](/de/agent/apply) sie automatisch an.
  </Accordion>

  <Accordion title="Datei löschen" icon="trash">
    Lösche Dateien autonom (kann in den Einstellungen deaktiviert werden).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Ausführen
</div>

Chat kann mit deinem Terminal interagieren.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Terminalbefehle ausführen und Ausgaben überwachen.
  </Accordion>
</AccordionGroup>

<Note>Standardmäßig verwendet Cursor das erste verfügbare Terminalprofil.</Note>

So legst du dein bevorzugtes Terminalprofil fest:

1. Öffne die Befehlspalette (`Cmd/Ctrl+Shift+P`)
2. Suche nach „Terminal: Select Default Profile“
3. Wähle das gewünschte Profil aus

<div id="mcp">
  ## MCP
</div>

Chat kann konfigurierte MCP-Server nutzen, um mit externen Diensten wie Datenbanken oder Drittanbieter-APIs zu interagieren.

<AccordionGroup>
  <Accordion title="MCP-Server umschalten" icon="server">
    Verfügbare MCP-Server umschalten. Berücksichtigt die Auto-Run-Konfiguration.
  </Accordion>
</AccordionGroup>

Erfahre mehr über das [Model Context Protocol](/de/context/model-context-protocol) und entdecke verfügbare Server im [MCP-Verzeichnis](/de/tools).

<div id="advanced-options">
  ## Erweiterte Optionen
</div>

<AccordionGroup>
  <Accordion title="Auto-apply Edits" icon="check">
    Änderungen automatisch anwenden, ohne manuelle Bestätigung.
  </Accordion>

  <Accordion title="Auto-run" icon="play">
    Terminalbefehle automatisch ausführen und Änderungen übernehmen. Nützlich, um Test-Suites laufen zu lassen und Änderungen zu verifizieren.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Allow-Lists konfigurieren, um festzulegen, welche Tools automatisch ausgeführt werden dürfen. Allow-Lists erhöhen die Sicherheit, indem zulässige Operationen explizit definiert werden.
  </Accordion>

  <Accordion title="Auto-fix Errors" icon="wrench">
    Linter-Fehler und -Warnungen automatisch beheben, wenn der Agent darauf stößt.
  </Accordion>
</AccordionGroup>



# Hintergrund-Agents
Source: https://docs.cursor.com/de/background-agent

Asynchrone Remote-Agents in Cursor

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Mit Background Agents spawnst du asynchrone Agents, die Code in einer Remote-Umgebung bearbeiten und ausführen. Sieh dir ihren Status an, schick Follow-ups oder übernimm jederzeit.

<div id="how-to-use">
  ## Verwendung
</div>

Du kannst auf Background Agents auf zwei Arten zugreifen:

1. **Background-Agenten-Seitenleiste**: Nutze den Tab für Background Agents in der nativen Cursor-Seitenleiste, um alle mit deinem Account verknüpften Background Agents anzuzeigen, bestehende Agents zu durchsuchen und neue zu starten.
2. **Background-Agent-Mode**: Drück <Kbd tooltip="Trigger background agent mode">Cmd E</Kbd>, um den Background-Agent-Mode in der UI zu aktivieren.

Nachdem du eine Eingabe abgeschickt hast, wähl deinen Agent aus der Liste, um den Status anzusehen und in die Machine einzusteigen.

<Note>
  <p className="!mb-0">
    Background Agents benötigen eine Datenaufbewahrung über einige Tage.
  </p>
</Note>

<div id="setup">
  ## Setup
</div>

Background-Agents laufen standardmäßig auf einer isolierten, Ubuntu-basierten Maschine. Die Agents haben Internetzugang und können Pakete installieren.

<div id="github-connection">
  #### GitHub-Verbindung
</div>

Background Agents klonen dein Repo von GitHub und arbeiten auf einem eigenen Branch; sie pushen ihre Änderungen in dein Repo, damit die Übergabe leicht fällt.

Gewähre Lese- und Schreibrechte für dein Repo (sowie alle abhängigen Repos oder Submodule). In Zukunft werden wir weitere Anbieter (GitLab, Bitbucket usw.) unterstützen.

<div id="ip-allow-list-configuration">
  ##### Konfiguration der IP-Allowlist
</div>

Wenn deine Organisation die IP-Allowlist-Funktion von GitHub verwendet, musst du den Zugriff für Hintergrund-Agents konfigurieren. Sieh dir die [GitHub-Integrationsdokumentation](/de/integrations/github#ip-allow-list-configuration) für vollständige Setup-Anweisungen inklusive Kontaktinformationen und IP-Adressen an.

<div id="base-environment-setup">
  #### Basis-Setup der Umgebung
</div>

Für fortgeschrittene Fälle richtest du die Umgebung selbst ein. Hol dir eine IDE-Instanz, die mit der Remote-Maschine verbunden ist. Richte deine Maschine ein, installiere Tools und Pakete und erstelle dann einen Snapshot. Konfiguriere die Runtime-Einstellungen:

* Der Install-Befehl läuft, bevor ein Agent startet, und installiert Runtime-Abhängigkeiten. Das kann bedeuten, `npm install` oder `bazel build` auszuführen.
* Terminals starten Hintergrundprozesse, während der Agent arbeitet – etwa einen Webserver oder das Kompilieren von Protobuf-Dateien.

Für die anspruchsvollsten Fälle nutze eine Dockerfile für das Maschinen-Setup. Die Dockerfile erlaubt dir, Systemabhängigkeiten einzurichten: bestimmte Compiler-Versionen installieren, Debugger hinzufügen oder das Basis-OS-Image wechseln. Kopiere nicht das gesamte Projekt mit `COPY` – wir verwalten den Workspace und checken den korrekten Commit aus. Die Installation von Abhängigkeiten gehört weiterhin ins Install-Skript.

Gib alle benötigten Secrets für deine Dev-Umgebung ein – sie werden verschlüsselt im Ruhezustand (mit KMS) in unserer Datenbank gespeichert und dem Agent im Hintergrund bereitgestellt.

Das Maschinen-Setup liegt in `.cursor/environment.json`, was in deinem Repo committed werden kann (empfohlen) oder privat gespeichert wird. Der Setup-Flow führt dich durch das Erstellen von `environment.json`.

<div id="maintenance-commands">
  #### Wartungsbefehle
</div>

Beim Einrichten einer neuen Maschine starten wir mit der Basisumgebung und führen dann den `install`-Befehl aus deiner `environment.json` aus. Das ist der Befehl, den ein Developer beim Wechseln von Branches ausführen würde – um neue Dependencies zu installieren.

Für die meisten ist der `install`-Befehl `npm install` oder `bazel build`.

Damit die Maschine schnell startet, cachen wir den Disk-Status, nachdem der `install`-Befehl gelaufen ist. Gestalte ihn so, dass er mehrfach ausgeführt werden kann. Es bleibt nur der Disk-Status aus dem `install`-Befehl bestehen – Prozesse, die hier gestartet werden, laufen nicht mehr, wenn der Agent startet.

<div id="startup-commands">
  #### Startup-Befehle
</div>

Nachdem `install` ausgeführt wurde, startet die Maschine und wir führen den Befehl `start` aus, gefolgt vom Starten aller `terminals`. Dadurch werden Prozesse gestartet, die laufen sollten, wenn der Agent aktiv ist.

Den Befehl `start` kannst du oft überspringen. Nutz ihn, wenn deine Dev-Umgebung auf Docker setzt – pack `sudo service docker start` in den `start`-Befehl.

`terminals` sind für App-Code. Diese Terminals laufen in einer `tmux`-Session, die dir und dem Agent zur Verfügung steht. Viele Website-Repos hinterlegen zum Beispiel `npm run watch` als Terminal.

<div id="the-environmentjson-spec">
  #### Die Spezifikation von `environment.json`
</div>

Die Datei `environment.json` kann so aussehen:

```json  theme={null}
{
  "snapshot": "POPULATED_FROM_SETTINGS",
  "install": "npm install",
  "terminals": [
    {
      "name": "Next.js ausführen",
      "command": "npm run dev"
    }
  ]
}
```

Formal ist die Spezifikation [hier definiert](https://www.cursor.com/schemas/environment.schema.json).

<div id="models">
  ## Modelle
</div>

Für Hintergrund-Agents sind nur Modelle verfügbar, die mit [Max Mode](/de/context/max-mode) kompatibel sind.

<div id="pricing">
  ## Preise
</div>

Erfahre mehr über die [Preise des Background Agents](/de/account/pricing#background-agent).

<div id="security">
  ## Sicherheit
</div>

Background Agents sind im Privacy Mode verfügbar. Wir trainieren niemals auf deinem Code und behalten Code nur so lange, wie der Agent läuft. [Erfahre mehr über den Privacy Mode](https://www.cursor.com/privacy-overview).

Was du wissen solltest:

1. Gewähre unserer GitHub-App Lese- und Schreibrechte für die Repos, die du bearbeiten willst. Wir nutzen das, um das Repo zu klonen und Änderungen vorzunehmen.
2. Dein Code läuft in unserer AWS-Infrastruktur in isolierten VMs und wird auf VM-Datenträgern gespeichert, solange der Agent aktiv ist.
3. Der Agent hat Internetzugang.
4. Der Agent führt alle Terminalbefehle automatisch aus, sodass er Tests iterativ ausführen kann. Das unterscheidet sich vom Foreground Agent, der für jeden Befehl deine Zustimmung benötigt. Automatisches Ausführen birgt ein Risiko der Datenexfiltration: Angreifer könnten Prompt-Injection-Angriffe durchführen und den Agenten dazu bringen, Code auf bösartige Websites hochzuladen. Siehe [OpenAIs Erklärung zu Risiken von Prompt Injection für Background Agents](https://platform.openai.com/docs/codex/agent-network#risks-of-agent-internet-access).
5. Wenn der Privacy Mode deaktiviert ist, sammeln wir Prompts und Entwicklungsumgebungen, um das Produkt zu verbessern.
6. Wenn du den Privacy Mode beim Start eines Background Agents deaktivierst und ihn dann während der Laufzeit wieder aktivierst, läuft der Agent weiter mit deaktiviertem Privacy Mode, bis er fertig ist.

<div id="dashboard-settings">
  ## Dashboard-Einstellungen
</div>

Workspace-Admins können zusätzliche Einstellungen auf dem Dashboard im Tab „Background Agents“ konfigurieren.

<div id="defaults-settings">
  ### Standard-Einstellungen
</div>

* **Standardmodell** – das Modell, das verwendet wird, wenn ein Run keins angibt. Wähle ein beliebiges Modell, das den Max Mode unterstützt.
* **Standard-Repository** – wenn leer, bitten die Agents dich, ein Repo auszuwählen. Wenn du hier ein Repo angibst, kannst du diesen Schritt überspringen.
* **Basis-Branch** – der Branch, von dem die Agents beim Erstellen von Pull Requests forken. Leer lassen, um den Standard-Branch des Repositories zu verwenden.

<div id="security-settings">
  ### Sicherheitseinstellungen
</div>

Alle Sicherheitsoptionen erfordern Admin-Rechte.

* **Nutzungsbeschränkungen** – wähle *Keine* (alle Mitglieder können Hintergrund-Agents starten) oder *Allow List*. Wenn *Allow List* aktiv ist, legst du genau fest, welche Teammitglieder Agents erstellen dürfen.
* **Team-Follow-ups** – wenn aktiviert, kann jede Person im Workspace Folge­nachrichten zu einem Agent hinzufügen, den jemand anderes gestartet hat. Deaktiviere das, um Follow-ups auf den Agent-Owner und Admins zu beschränken.
* **Agent-Zusammenfassung anzeigen** – steuert, ob Cursor die File-Diff-Bilder und Code-Snippets des Agents anzeigt. Deaktiviere das, wenn du keine Dateipfade oder Code in der Seitenleiste anzeigen lassen willst.
* **Agent-Zusammenfassung in externen Kanälen anzeigen** – erweitert den vorherigen Schalter auf Slack oder jeden verbundenen externen Kanal.

Änderungen werden sofort gespeichert und gelten sofort für neue Agents.



# Nachverfolgung hinzufügen
Source: https://docs.cursor.com/de/background-agent/api/add-followup

en/background-agent/api/openapi.yaml post /v0/agents/{id}/followup
Sende eine zusätzliche Anweisung an einen laufenden Hintergrundagenten.




# Agentengespräch
Source: https://docs.cursor.com/de/background-agent/api/agent-conversation

en/background-agent/api/openapi.yaml get /v0/agents/{id}/conversation
Den Gesprächsverlauf eines Hintergrund-Agents abrufen.

Wenn der Hintergrund-Agent gelöscht wurde, kannst du nicht auf das Gespräch zugreifen.



# Agentstatus
Source: https://docs.cursor.com/de/background-agent/api/agent-status

en/background-agent/api/openapi.yaml get /v0/agents/{id}
Hol dir den aktuellen Status und die Ergebnisse eines bestimmten Hintergrundagents.




# API-Schlüsselinformationen
Source: https://docs.cursor.com/de/background-agent/api/api-key-info

en/background-agent/api/openapi.yaml get /v0/me
Ruft Metadaten zum für die Authentifizierung verwendeten API-Schlüssel ab.




# Einen Agenten löschen
Source: https://docs.cursor.com/de/background-agent/api/delete-agent

en/background-agent/api/openapi.yaml delete /v0/agents/{id}
Einen Hintergrundagenten und die zugehörigen Ressourcen dauerhaft löschen.




# Agent starten
Source: https://docs.cursor.com/de/background-agent/api/launch-an-agent

en/background-agent/api/openapi.yaml post /v0/agents
Einen neuen Hintergrundagenten starten, der an deinem Repository arbeitet.




# Agents auflisten
Source: https://docs.cursor.com/de/background-agent/api/list-agents

en/background-agent/api/openapi.yaml get /v0/agents
Abfrage einer paginierten Liste aller Hintergrund-Agents für den authentifizierten User.




# Modelle auflisten
Source: https://docs.cursor.com/de/background-agent/api/list-models

en/background-agent/api/openapi.yaml get /v0/models
Eine Liste empfohlener Modelle für Background-Agents abrufen.

Wenn du beim Erstellen das Modell des Background-Agents angeben willst, kannst du diesen Endpoint nutzen, um eine Liste empfohlener Modelle zu sehen.

In dem Fall empfehlen wir auch eine Option „Auto“, bei der du dem Create-Endpoint keinen Modellnamen übergibst und wir das passendste Modell auswählen.



# GitHub-Repositories auflisten
Source: https://docs.cursor.com/de/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Eine Liste von GitHub-Repositories abrufen, auf die der authentifizierte Nutzer Zugriff hat.

<Warning>
  **Dieser Endpoint hat sehr strenge Rate Limits.**

  Begrenze Anfragen auf **1/Nutzer/Minute** und **30/Nutzer/Stunde.**

  Bei Nutzern mit Zugriff auf viele Repositories kann die Antwort mehrere Dutzend Sekunden dauern.

  Stell sicher, dass du sauber damit umgehst, wenn diese Informationen nicht verfügbar sind.
</Warning>



# Überblick
Source: https://docs.cursor.com/de/background-agent/api/overview

Hintergrund-Agents, die in deinen Repositories arbeiten, programmatisch erstellen und verwalten

<div id="background-agents-api">
  # Background Agents API
</div>

<Badge variant="beta">Beta</Badge>

Die Background Agents API ermöglicht dir, programmgesteuert KI-gestützte Coding-Agents zu erstellen und zu verwalten, die autonom in deinen Repositories arbeiten.
Du kannst die API nutzen, um automatisch auf Nutzerfeedback zu reagieren, Bugs zu beheben, Dokus zu aktualisieren und vieles mehr!

<Info>
  Die Background Agents API ist derzeit in der Beta – wir freuen uns über dein Feedback!
</Info>

<div id="key-features">
  ## Wichtige Features
</div>

* **Autonome Codegenerierung** - Erstell Agenten, die deinen Prompt verstehen und Änderungen an deiner Codebasis vornehmen können
* **Repository-Integration** - Arbeite direkt mit GitHub-Repositories
* Folge-Prompts - Füge laufenden Agenten zusätzliche Anweisungen hinzu
* **Nutzungsbasierte Abrechnung** - Zahl nur für die Tokens, die du verwendest
* **Skalierbar** - Support für bis zu 256 aktive Agenten pro API-Schlüssel

<div id="quick-start">
  ## Schnellstart
</div>

<div id="1-get-your-api-key">
  ### 1. Hol dir deinen API‑Schlüssel
</div>

**Geh** zu [Cursor Dashboard → Integrations](https://cursor.com/dashboard?tab=integrations), um deinen API‑Schlüssel zu erstellen.

<div id="2-start-using-the-api">
  ### 2. Starte mit der API
</div>

Alle API‑Endpunkte sind relativ zu:

```
https://api.cursor.com
```

Sieh dir die [API-Referenz](/de/background-agent/api/launch-an-agent) für eine detaillierte Liste der Endpoints an.

<div id="authentication">
  ## Authentifizierung
</div>

Alle API-Requests erfordern eine Authentifizierung mit einem Bearer-Token:

```
Authorization: Bearer DEIN_API_KEY
```

API-Schlüssel werden im [Cursor Dashboard](https://cursor.com/dashboard?tab=integrations) erstellt. Schlüssel sind an dein Konto gebunden und berechtigen dich, Agents zu erstellen und zu verwalten (abhängig von deinen Planlimits und deinem Repository-Zugriff).

<div id="pricing">
  ## Preise
</div>

Die API ist derzeit in der Beta und hat dieselben Preise wie Background Agents. Die Preise können sich ändern, während wir den Service skalieren. Schau dir die [Preise für Background Agents](/de/account/pricing#background-agent) an.

<div id="next-steps">
  ## Nächste Schritte
</div>

* Lies dir die Hauptseite zur [Übersicht über Background Agents](/de/background-agent) durch, um Umgebungen, Berechtigungen und Workflows zu verstehen.
* Probier Background Agents im [Web und auf dem Handy](/de/background-agent/web-and-mobile) aus.
* Mach bei der Diskussion auf [Discord #background-agent](https://discord.gg/jfgpZtYpmb) mit oder schreib an [background-agent-feedback@cursor.com](mailto:background-agent-feedback@cursor.com).



# Webhooks
Source: https://docs.cursor.com/de/background-agent/api/webhooks

Erhalte Echtzeit-Benachrichtigungen über Statusänderungen von Background Agents

<div id="webhooks">
  # Webhooks
</div>

Wenn du einen Agent mit einer Webhook-URL erstellst, sendet Cursor HTTP-POST-Anfragen, um dich über Statusänderungen zu informieren. Derzeit werden nur `statusChange`-Events unterstützt – konkret, wenn ein Agent den Zustand `ERROR` oder `FINISHED` erreicht.

<div id="webhook-verification">
  ## Webhook-Verifizierung
</div>

Um sicherzugehen, dass die Webhook-Anfragen wirklich von Cursor stammen, überprüf die Signatur, die jeder Anfrage beigefügt ist:

<div id="headers">
  ### Header
</div>

Jede Webhook-Anfrage enthält die folgenden Header:

* **`X-Webhook-Signature`** – Enthält die HMAC-SHA256-Signatur im Format `sha256=<hex_digest>`
* **`X-Webhook-ID`** – Eine eindeutige Kennung für diese Zustellung (nützlich fürs Logging)
* **`X-Webhook-Event`** – Der Ereignistyp (aktuell nur `statusChange`)
* **`User-Agent`** – Immer gesetzt auf `Cursor-Agent-Webhook/1.0`

<div id="signature-verification">
  ### Signaturüberprüfung
</div>

Um die Webhook-Signatur zu verifizieren, berechne die erwartete Signatur und vergleiche sie mit der empfangenen:

```javascript  theme={null}
const crypto = require('crypto');

function verifyWebhook(secret, rawBody, signature) {
  const expectedSignature = 'sha256=' + 
    crypto.createHmac('sha256', secret)
          .update(rawBody)
          .digest('hex');
  
  return signature === expectedSignature;
}
```

```python  theme={null}
import hmac
import hashlib

def verify_webhook(secret, raw_body, signature):
    expected_signature = 'sha256=' + hmac.new(
        secret.encode(),
        raw_body,
        hashlib.sha256
    ).hexdigest()
    
    return signature == expected_signature
```

Verwende zum Berechnen der Signatur immer den unveränderten Request-Body (vor jeglicher Parsing-Logik).

<div id="payload-format">
  ## Payload-Format
</div>

Die Webhook-Payload wird als JSON mit folgender Struktur gesendet:

```json  theme={null}
{
  "event": "statusChange",
  "timestamp": "2024-01-15T10:30:00Z",
  "id": "bc_abc123",
  "status": "FINISHED",
  "source": {
    "repository": "https://github.com/your-org/your-repo",
    "ref": "main"
  },
  "target": {
    "url": "https://cursor.com/agents?id=bc_abc123",
    "branchName": "cursor/add-readme-1234",
    "prUrl": "https://github.com/your-org/your-repo/pull/1234"
  },
  "summary": "README.md mit Installationsanleitung hinzugefügt"
}
```

Beachte, dass einige Felder optional sind und nur angezeigt werden, wenn sie verfügbar sind.

<div id="best-practices">
  ## Best Practices
</div>

* **Signaturen prüfen** – überprüf die Webhook-Signatur, um sicherzustellen, dass die Anfrage von Cursor kommt
* **Retries behandeln** – Webhooks können erneut zugestellt werden, wenn dein Endpoint einen Fehlerstatuscode zurückgibt
* **Schnell antworten** – gib so schnell wie möglich einen 2xx-Statuscode zurück
* **HTTPS verwenden** – nutz in Produktion immer HTTPS-URLs für Webhook-Endpoints
* **Rohpayloads speichern** – speichere die rohe Webhook-Payload fürs Debugging und für spätere Verifizierung



# Web & Mobile
Source: https://docs.cursor.com/de/background-agent/web-and-mobile

Führe Coding-Agents auf jedem Gerät aus – mit nahtlosem Handover auf den Desktop

<div id="overview">
  ## Übersicht
</div>

Der Web-Agent von Cursor bringt einen leistungsstarken Coding-Assistenten auf jedes Gerät. Ob du auf deinem Handy beim Spazierengehen bist oder im Browser arbeitest – du kannst jetzt starke Coding-Agents starten, die im Hintergrund laufen.
Wenn sie fertig sind, hol ihre Arbeit in Cursor ab, prüf und mergen die Änderungen oder teil Links mit deinem Team, um zusammenzuarbeiten.

Leg los unter [cursor.com/agents](https://cursor.com/agents).

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=79c7d14df82cfcae369bccb8a1431cf3" alt="Cursor web agent interface" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=099c28633151e6c20eebc7fe03b3d420 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=452e0216c7e270d760072032f1e2b36d 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=baaa4a73d4822b5daa293814dc201d37 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=8c5255fbf16aa60924e78a8285afb95d 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=7cc5a04ff6b24ad4ce0cfb4a35a9919c 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-1.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=f5f1b15fa508e20f89a4089f81417774 2500w" /></Frame>

<div id="getting-started">
  ## Erste Schritte
</div>

<div id="quick-setup">
  ### Schnelle Einrichtung
</div>

1. **Web-App aufrufen**: Öffne [cursor.com/agents](https://cursor.com/agents) auf einem beliebigen Gerät
2. **Anmelden**: Melde dich mit deinem Cursor-Account an
3. **GitHub verbinden**: Verknüpfe deinen GitHub-Account, um auf Repositories zuzugreifen
4. **Ersten Agenten starten**: Gib eine Aufgabe ein und schau zu, wie der Agent loslegt

<div id="mobile-installation">
  ### Mobile Installation
</div>

Für die beste mobile Nutzung installiere Cursor als Progressive Web App (PWA):

* **iOS**: Öffne [cursor.com/agents](https://cursor.com/agents) in Safari, tippe auf den Teilen-Button und dann auf „Zum Home-Bildschirm hinzufügen“
* **Android**: Öffne die URL in Chrome, tippe auf das Menü und dann auf „Zum Startbildschirm hinzufügen“ oder „App installieren“

<Tip>
  Die Installation als PWA bietet ein natives Nutzungserlebnis mit: - Vollbildoberfläche - Schnelleren Startzeiten - App-Icon auf deinem Home-Bildschirm
</Tip>

<div id="working-across-devices">
  ## Geräteübergreifend arbeiten
</div>

Der Web- und Mobile-Agent ist dafür gemacht, nahtlos mit deinem Desktop-Workflow zu funktionieren; klick auf „Open in Cursor“, um die Arbeit des Agents in deiner IDE fortzusetzen.

<Frame><img src="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=352140fd4bf3f3d98a1e1b9f4a995cad" alt="Review and handoff" data-og-width="4095" width="4095" data-og-height="2048" height="2048" data-path="images/webagent/cursor-web-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=280&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=eedd50318503fd3d3961b6da27a386d9 280w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=560&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=fd8c730cf62a0af6f873945a6a23b90b 560w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=840&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=ac537cc639471556f1afa0e09425ef30 840w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1100&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=d512cddda6890c0749a7ad6396682def 1100w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=1650&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=e208297f414976bcfeea6850b39e8abb 1650w, https://mintcdn.com/cursor/kWfPDXl84scQFWmx/images/webagent/cursor-web-2.png?w=2500&fit=max&auto=format&n=kWfPDXl84scQFWmx&q=85&s=54683ff7f25750fdc788e87c30bb6d6d 2500w" /></Frame>

<div id="team-collaboration">
  ### Teamzusammenarbeit
</div>

* **Gemeinsamer Zugriff**: Teile Links mit Teammitgliedern, um bei Agent-Runs zusammenzuarbeiten.
* **Review-Prozess**: Mitarbeitende können Diffs prüfen und Feedback geben.
* **Pull-Request-Management**: Erstelle, reviewe und merge Pull Requests direkt in der Weboberfläche.

<div id="slack-integration">
  ### Slack-Integration
</div>

Starte Agents direkt aus Slack, indem du `@Cursor` erwähnst, und wenn du Agents aus dem Web oder von Mobile startest, kannst du dich nach Abschluss per Slack benachrichtigen lassen.

<Card title="Use Cursor in Slack" icon="slack" href="/de/slack">
  Erfahre mehr über Einrichtung und Nutzung der Slack-Integration, einschließlich
  dem Auslösen von Agents und dem Empfangen von Benachrichtigungen.
</Card>

<div id="pricing">
  ## Preise
</div>

Web- und Mobile-Agents verwenden dasselbe Preismodell wie Background Agents.

Erfahre mehr über die [Preise für Background Agents](/de/account/pricing#background-agent).

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

<AccordionGroup>
  <Accordion title="Agent-Runs starten nicht">
    * Stell sicher, dass du eingeloggt bist und dein GitHub-Konto verbunden ist. - Prüfe,
      ob du die nötigen Repository-Berechtigungen hast. - Du musst außerdem eine Pro-Testphase
      oder einen kostenpflichtigen Plan mit aktivierter nutzungsbasierter Abrechnung haben. Um die
      nutzungsbasierte Abrechnung zu aktivieren, geh im
      [Dashboard](https://www.cursor.com/dashboard?tab=settings) zum Tab „Settings“.
  </Accordion>

  <Accordion title="Agent-Runs werden auf dem Handy nicht angezeigt">
    Versuch, die Seite zu aktualisieren oder den Browser-Cache zu leeren. Stell sicher, dass du
    auf allen Geräten dasselbe Konto verwendest.
  </Accordion>

  <Accordion title="Slack-Integration funktioniert nicht">
    Check, ob dein Workspace-Admin die Cursor-Slack-App installiert hat und ob
    du die passenden Berechtigungen hast.
  </Accordion>
</AccordionGroup>



# Bugbot
Source: https://docs.cursor.com/de/bugbot

KI-Code-Review für Pull Requests

Bugbot prüft Pull Requests und findet Bugs, Sicherheitslücken und Probleme bei der Codequalität.

<Tip>
  Bugbot hat eine kostenlose Stufe: Du bekommst jeden Monat eine begrenzte Anzahl kostenloser PR-Reviews. Sobald du das Limit erreichst, pausieren die Reviews bis zu deinem nächsten Abrechnungszeitraum. Du kannst jederzeit auf eine 14‑tägige kostenlose Pro-Testversion upgraden und unbegrenzt reviewen (vorbehaltlich der üblichen Abuse-Schutzmechanismen).
</Tip>

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-report-cropped.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=013060fbd22f397ac81f2c32bb8b6b14" alt="Bugbot hinterlässt Kommentare in einem PR" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-report-cropped.mp4" />
</Frame>

<div id="how-it-works">
  ## So funktioniert’s
</div>

Bugbot analysiert PR-Diffs und hinterlässt Kommentare mit Erklärungen und Vorschlägen zur Behebung. Es läuft automatisch bei jedem PR-Update oder manuell, wenn es ausgelöst wird.

* Führt bei jedem PR-Update **automatische Reviews** aus
* **Manueller Trigger** durch einen Kommentar mit `cursor review` oder `bugbot run` in einem beliebigen PR
* **In Cursor beheben**-Links öffnen Issues direkt in Cursor
* **Im Web beheben**-Links öffnen Issues direkt unter [cursor.com/agents](https://cursor.com/agents)

<div id="setup">
  ## Einrichtung
</div>

Erfordert Cursor-Adminrechte und Adminrechte für die GitHub-Organisation.

1. Geh zu [cursor.com/dashboard](https://cursor.com/dashboard?tab=bugbot)
2. Wechsel zum Tab „Bugbot“
3. Klick auf „Connect GitHub“ (oder „Manage Connections“, wenn schon verbunden)
4. Folge dem GitHub-Installationsprozess
5. Geh zurück zum Dashboard und aktiviere Bugbot für bestimmte Repositories

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=75745d4464b183c306a44571db86a0c4" alt="Bugbot-GitHub-Setup" autoPlay loop muted playsInline controls data-path="images/bugbot/bugbot-install.mp4" />
</Frame>

<div id="configuration">
  ## Konfiguration
</div>

<Tabs defaultValue="Team">
  <Tab title="Individual">
    ### Repository-Einstellungen

    Aktiviere oder deaktiviere Bugbot pro Repository über deine Installationsliste. Bugbot läuft nur auf PRs, die du erstellt hast.

    ### Persönliche Einstellungen

    * **Nur bei Erwähnung** ausführen, indem du `cursor review` oder `bugbot run` kommentierst
    * **Nur einmal** pro PR ausführen und nachfolgende Commits überspringen
  </Tab>

  <Tab title="Team">
    ### Repository-Einstellungen

    Team-Admins können Bugbot pro Repository aktivieren, Allow-/Deny-Listen für Reviewer konfigurieren und festlegen:

    * **Nur einmal** pro PR und Installation ausführen und nachfolgende Commits überspringen
    * **Inline-Reviews deaktivieren**, damit Bugbot keine Kommentare direkt an Codezeilen hinterlässt

    Bugbot läuft für alle Beitragenden in aktivierten Repositories, unabhängig von der Teamzugehörigkeit.

    ### Persönliche Einstellungen

    Teammitglieder können Einstellungen für ihre eigenen PRs überschreiben:

    * **Nur bei Erwähnung** ausführen, indem du `cursor review` oder `bugbot run` kommentierst
    * **Nur einmal** pro PR ausführen und nachfolgende Commits überspringen
    * **Reviews für Draft-PRs aktivieren**, um Entwurfs-Pull-Requests in automatische Reviews einzubeziehen
  </Tab>
</Tabs>

<div id="analytics">
  ### Analytics
</div>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0b09bc0e61d1c92017c3ca42957c70e1" alt="Bugbot-Dashboard" data-og-width="1832" width="1832" data-og-height="2022" height="2022" data-path="images/bugbot/bugbot-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fe3c6151118fa404a0a5a100968649cf 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7a602dfdaa6f737dc6d5010ea90a74b8 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6a21a6cb4b32248fb2b8cbea9afb8bcc 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=27df9beda1ee9efc84e6f2c339ff1076 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=80cb6507ca96d1c2aa74bcc30170b517 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/bugbot/bugbot-dashboard.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ce35818f10c462b16b2d697519557019 2500w" />
</Frame>

<div id="rules">
  ## Regeln
</div>

Leg `.cursor/BUGBOT.md`-Dateien an, um projektspezifischen Kontext für Reviews bereitzustellen. Bugbot berücksichtigt immer die `.cursor/BUGBOT.md`-Datei im Projektstamm sowie alle zusätzlichen Dateien, die beim Aufwärtsgehen von geänderten Dateien aus gefunden werden.

```
project/
  .cursor/BUGBOT.md          # Immer enthalten (projektweite Regeln)
  backend/
    .cursor/BUGBOT.md        # Wird beim Review von Backend-Dateien einbezogen
    api/
      .cursor/BUGBOT.md      # Wird beim Review von API-Dateien einbezogen
  frontend/
    .cursor/BUGBOT.md        # Wird beim Review von Frontend-Dateien einbezogen
```

<AccordionGroup>
  <Accordion title="Beispiel .cursor/BUGBOT.md">
    ```markdown  theme={null}
    # Richtlinien zur Projektüberprüfung

    ## Sicherheitsschwerpunkte

    - Eingaben in API-Endpunkten validieren
    - Auf SQL-Injection-Schwachstellen in Datenbankabfragen prüfen
    - Korrekte Authentifizierung auf geschützten Routen sicherstellen

    ## Architekturpatterns

    - Dependency Injection für Services verwenden
    - Repository-Pattern für den Datenzugriff einsetzen
    - Robuste Fehlerbehandlung mit eigenen Fehlerklassen implementieren

    ## Häufige Probleme

    - Memory-Leaks in React-Komponenten (useEffect-Cleanup prüfen)
    - Fehlende Error Boundaries in UI-Komponenten
    - Inkonsistente Namenskonventionen (camelCase für Funktionen verwenden)

    ```
  </Accordion>
</AccordionGroup>

<div id="pricing">
  ## Preise
</div>

Bugbot bietet zwei Pläne: **Free** und **Pro**.

<div id="free-tier">
  ### Free-Tarif
</div>

Jede:r Nutzer:in bekommt jeden Monat eine begrenzte Anzahl kostenloser PR-Reviews. In Teams erhält jedes Teammitglied seine eigenen kostenlosen Reviews. Wenn du das Limit erreichst, werden Reviews bis zu deinem nächsten Abrechnungszeitraum ausgesetzt. Du kannst jederzeit auf die 14‑tägige kostenlose Pro-Testversion mit unbegrenzten Reviews upgraden.

<div id="pro-tier">
  ### Pro-Tarif
</div>

<Tabs defaultValue="Teams">
  <Tab title="Individuals">
    ### Pauschalpreis

    40 \$ pro Monat für unbegrenzte Bugbot-Reviews bei bis zu 200 PRs pro Monat über alle Repositories hinweg.

    ### Erste Schritte

    Abonniere über deine Kontoeinstellungen.
  </Tab>

  <Tab title="Teams">
    ### Abrechnung pro Nutzer

    Teams zahlen 40 \$ pro Nutzer und Monat für unbegrenzte Reviews.

    Als Nutzer zählt jede Person, die in einem Monat PRs verfasst hat, die von Bugbot reviewed wurden.

    Alle Lizenzen werden zu Beginn jedes Abrechnungszyklus freigegeben und anschließend nach dem Prinzip „First come, first served“ vergeben. Wenn ein Nutzer in einem Monat keine PRs verfasst, die von Bugbot reviewed wurden, kann der Platz von einem anderen Nutzer verwendet werden.

    ### Sitzplatzlimits

    Team-Admins können maximale Bugbot-Sitzplätze pro Monat festlegen, um die Kosten zu kontrollieren.

    ### Erste Schritte

    Abonniert über euer Team-Dashboard, um die Abrechnung zu aktivieren.

    ### Schutzmaßnahmen gegen Missbrauch

    Um Missbrauch zu verhindern, gibt es ein gepooltes Limit von 200 Pull Requests pro Monat pro Bugbot-Lizenz. Wenn du mehr als 200 Pull Requests pro Monat brauchst, schreib uns an [hi@cursor.com](mailto:hi@cursor.com) und wir helfen dir gern weiter.

    Wenn dein Team zum Beispiel 100 Nutzer hat, kann deine Organisation zunächst 20.000 Pull Requests pro Monat reviewen. Wenn ihr dieses Limit regulär erreicht, meldet euch bei uns und wir erhöhen es gern.
  </Tab>
</Tabs>

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

Wenn Bugbot nicht funktioniert:

1. **Aktiviere den Verbose-Modus**, indem du `cursor review verbose=true` oder `bugbot run verbose=true` hinzufügst, um detaillierte Logs und die Request-ID zu erhalten
2. **Prüfe die Berechtigungen**, um sicherzustellen, dass Bugbot Zugriff auf das Repository hat
3. **Überprüfe die Installation**, um zu bestätigen, dass die GitHub-App installiert und aktiviert ist

Füge beim Melden von Problemen die Request-ID aus dem Verbose-Modus bei.

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Entspricht Bugbot dem Privacy‑Modus?">
    Ja, Bugbot erfüllt dieselben Datenschutzanforderungen wie Cursor und verarbeitet Daten genauso wie andere Cursor‑Anfragen.
  </Accordion>

  <Accordion title="Was passiert, wenn ich das Free‑Tier‑Limit erreiche?">
    Wenn du dein monatliches Free‑Tier‑Limit erreichst, werden Bugbot‑Reviews bis zu deinem nächsten Abrechnungszeitraum pausiert. Du kannst auf die 14‑tägige kostenlose Pro‑Testversion upgraden und unbegrenzt Reviews erhalten (vorbehaltlich der üblichen Schutzmaßnahmen gegen Missbrauch).
  </Accordion>
</AccordionGroup>

```
```




---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-code-review.md)