---
title: "Linear"
source: "https://docs.cursor.com/de/integrations/linear"
language: "de"
language_name: "German"
---

# Linear
Source: https://docs.cursor.com/de/integrations/linear

Mit Background Agents in Linear arbeiten

Nutze [Background Agents](/de/background-agent) direkt in Linear, indem du Issues an Cursor delegierst oder `@Cursor` in Kommentaren erwähnst.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## Leg direkt los
</div>

<div id="installation">
  ### Installation
</div>

<Note>
  Du musst Cursor-Admin sein, um die Linear-Integration zu verbinden. Andere Team-Einstellungen sind auch für Nicht-Admins verfügbar.
</Note>

1. Geh zu [Cursor-Integrationen](https://www.cursor.com/en/dashboard?tab=integrations)
2. Klick auf *Connect* neben Linear
3. Verbinde deinen Linear-Workspace und wähle ein Team aus
4. Klick auf *Authorize*
5. Schließ die restliche Einrichtung des Background Agents in Cursor ab:
   * Verbinde GitHub und wähle das Standard-Repository
   * Aktivier nutzungsbasierte Abrechnung
   * Bestätige die Datenschutzeinstellungen

<div id="account-linking">
  ### Kontoverknüpfung
</div>

Beim ersten Verwenden wird die Kontoverknüpfung zwischen Cursor und Linear angestoßen. Für das Erstellen von PRs ist eine GitHub-Verbindung erforderlich.

## So geht's

Delegier Issues an Cursor oder erwähn `@Cursor` in Kommentaren. Cursor analysiert Issues und filtert automatisch Nicht-Development-Aufgaben heraus.

<div id="delegating-issues">
  ### Issues delegieren
</div>

1. Linear-Issue öffnen
2. Auf das Assignee-Feld klicken
3. „Cursor“ auswählen

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Ein Issue in Linear an Cursor delegieren" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Cursor erwähnen
</div>

Erwähn `@Cursor` in einem Kommentar, um einen neuen Agenten zuzuweisen oder zusätzliche Anweisungen zu geben, zum Beispiel: `@Cursor fix the authentication bug described above`.

<div id="workflow">
  ## Workflow
</div>

Background Agents zeigen in Linear den Status in Echtzeit an und erstellen nach Abschluss automatisch PRs. Verfolge den Fortschritt im [Cursor-Dashboard](https://www.cursor.com/dashboard?tab=background-agents).

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Statusupdates von Background Agents in Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### Follow-up-Anweisungen
</div>

Du kannst in der Agent-Session antworten, dann wird deine Nachricht als Follow-up an den Agent gesendet. Erwähne einfach `@Cursor` in einem Linear-Kommentar, um einem laufenden Background Agent zusätzliche Hinweise zu geben.

<div id="configuration">
  ## Konfiguration
</div>

Konfigurier die Background-Agent-Einstellungen über [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div className="full-width-table">
  | Einstellung             | Ort              | Beschreibung                                                               |
  | :---------------------- | :--------------- | :------------------------------------------------------------------------- |
  | **Standard-Repository** | Cursor-Dashboard | Primäres Repository, wenn kein Projekt-Repository konfiguriert ist         |
  | **Standardmodell**      | Cursor-Dashboard | KI-Modell für Background Agents                                            |
  | **Basis-Branch**        | Cursor-Dashboard | Branch, von dem PRs erstellt werden (typischerweise `main` oder `develop`) |
</div>

<div id="configuration-options">
  ### Konfigurationsoptionen
</div>

Du kannst das Verhalten des Background Agents auf mehrere Arten konfigurieren:

**Issue-Beschreibung oder Kommentare**: Verwende die `[key=value]`-Syntax, zum Beispiel:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Issue-Labels**: Verwende eine Parent-Child-Label-Struktur, bei der das Parent-Label der Konfigurationsschlüssel und das Child-Label der Wert ist.

**Projekt-Labels**: Gleiche Parent-Child-Struktur wie bei Issue-Labels, angewendet auf Projektebene.

Unterstützte Konfigurationsschlüssel:

* `repo`: Ziel-Repository angeben (z. B. `owner/repository`)
* `branch`: Basis-Branch für die PR-Erstellung angeben
* `model`: Zu verwendetes KI-Modell angeben

<div id="repository-selection">
  ### Repository-Auswahl
</div>

Cursor legt anhand dieser Priorität fest, in welchem Repository gearbeitet wird:

1. **Issue-Beschreibung/Kommentare**: `[repo=owner/repository]`-Syntax im Issue-Text oder in Kommentaren
2. **Issue-Labels**: Repository-Labels, die dem spezifischen Linear-Issue zugewiesen sind
3. **Projekt-Labels**: Repository-Labels, die dem Linear-Projekt zugewiesen sind
4. **Standard-Repository**: Im Cursor-Dashboard festgelegtes Repository

<div id="setting-up-repository-labels">
  #### Repository-Labels einrichten
</div>

So erstellst du Repository-Labels in Linear:

1. Geh zu **Settings** in deinem Linear-Workspace
2. Klick auf **Labels**
3. Klick auf **New group**
4. Benenn die Gruppe „repo“ (Groß-/Kleinschreibung egal – muss genau „repo“ sein, nicht „Repository“ oder andere Varianten)
5. Erstell innerhalb dieser Gruppe Labels für jedes Repository im Format `owner/repo`

Diese Labels kannst du dann Issues oder Projekten zuweisen, um festzulegen, in welchem Repository der Background Agent arbeiten soll.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Repository-Labels in Linear konfigurieren" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →