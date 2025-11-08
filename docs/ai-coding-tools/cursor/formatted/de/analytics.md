---
title: "Analytics"
source: "https://docs.cursor.com/de/account/teams/analytics"
language: "de"
language_name: "German"
---

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

---

← Previous: [AI-Code-Tracking-API](./ai-code-tracking-api.md) | [Index](./index.md) | Next: [Analytics V2](./analytics-v2.md) →