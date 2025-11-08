---
title: "Regeln"
source: "https://docs.cursor.com/de/context/rules"
language: "de"
language_name: "German"
---

# Regeln
Source: https://docs.cursor.com/de/context/rules

Steuer, wie sich das Agent-Modell mit wiederverwendbaren, eingegrenzten Anweisungen verhält.

Regeln liefern systemweite Anweisungen für Agent und Inline Edit. Denk daran als persistierenden Kontext, Voreinstellungen oder Workflows für deine Projekte.

Cursor unterstützt vier Arten von Regeln:

<CardGroup cols={2}>
  <Card title="Project Rules" icon="folder-tree">
    Gespeichert in `.cursor/rules`, versionsverwaltet und auf deinen Codebase-Kontext begrenzt.
  </Card>

  <Card title="User Rules" icon="user">
    Global in deiner Cursor-Umgebung. In den Einstellungen definiert und immer angewendet.
  </Card>

  <Card title="AGENTS.md" icon="robot">
    Agent-Anweisungen im Markdown-Format. Eine einfache Alternative zu `.cursor/rules`.
  </Card>

  <Card title=".cursorrules (Legacy)" icon="clock-rotate-left">
    Weiterhin unterstützt, aber veraltet. Verwende stattdessen Project Rules.
  </Card>
</CardGroup>

<div id="how-rules-work">
  ## Wie Regeln funktionieren
</div>

Große Sprachmodelle behalten zwischen Antworten kein Gedächtnis. Regeln liefern beständigen, wiederverwendbaren Kontext auf Prompt-Ebene.

Wenn sie aktiviert sind, werden die Inhalte von Regeln am Anfang des Modellkontexts eingefügt. So bekommt die KI durchgehend konsistente Vorgaben zum Generieren von Code, Interpretieren von Edits oder Unterstützen von Workflows.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e637bab83cfd5dcc8a3b15ed6fd9fc15" alt="Regel im Kontext mit Chat angewendet" data-og-width="1198" width="1198" data-og-height="674" height="674" data-path="images/context/rules/rules-applied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=78e3c392987c6f95a02fc106753c5f98 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=9d3a8b76ba99ada5ca302cba9fb63810 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f5ab7fb374a1a4c5fe2f50e2e50d233a 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5d25394a29c1da4172a3e673ee384c07 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fc125bd3c2a93551674252c0523d3ec 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rules-applied.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c576ea053ee18c30d2781c6bdd394a70 2500w" />
</Frame>

<Info>
  Regeln gelten für [Chat](/de/chat/overview) und [Inline
  Edit](/de/inline-edit/overview). Aktive Regeln werden in der Agent-Seitenleiste angezeigt.
</Info>

<div id="project-rules">
  ## Projektregeln
</div>

Projektregeln liegen in `.cursor/rules`. Jede Regel ist eine Datei und steht unter Versionskontrolle. Sie können über Pfad-Muster eingegrenzt, manuell ausgeführt oder basierend auf Relevanz einbezogen werden. Unterverzeichnisse können ihr eigenes `.cursor/rules`-Verzeichnis enthalten, das auf diesen Ordner beschränkt ist.

Verwende Projektregeln, um:

* domänenspezifisches Wissen über deine Codebasis zu erfassen
* projektspezifische Workflows oder Vorlagen zu automatisieren
* Stil- oder Architekturentscheidungen zu standardisieren

<div id="rule-anatomy">
  ### Anatomie einer Rule
</div>

Jede Rule-Datei wird in **MDC** (`.mdc`) geschrieben, einem Format, das Metadaten und Inhalt unterstützt. Steuere über das Typ-Dropdown, wie Rules angewendet werden; es ändert die Properties `description`, `globs`, `alwaysApply`.

| <span class="no-wrap">Rule-Typ</span>          | Beschreibung                                                                           |
| :--------------------------------------------- | :------------------------------------------------------------------------------------- |
| <span class="no-wrap">`Always`</span>          | Immer im Model-Kontext enthalten                                                       |
| <span class="no-wrap">`Auto Attached`</span>   | Wird einbezogen, wenn referenzierte Dateien einem Glob-Pattern entsprechen             |
| <span class="no-wrap">`Agent Requested`</span> | Für die AI verfügbar, die entscheidet, ob sie es einbezieht. Beschreibung erforderlich |
| <span class="no-wrap">`Manual`</span>          | Nur enthalten, wenn explizit mit `@ruleName` erwähnt                                   |

```
---
description: RPC-Service-Boilerplate
globs:
alwaysApply: false
---

- Verwende unser internes RPC-Pattern, wenn du Services definierst
- Verwende für Servicenamen immer snake_case.

@service-template.ts
```

<div id="nested-rules">
  ### Verschachtelte Regeln
</div>

Organisier Regeln, indem du sie in `.cursor/rules`-Verzeichnissen überall im Projekt ablegst. Verschachtelte Regeln werden automatisch verknüpft, wenn auf Dateien in ihrem Verzeichnis verwiesen wird.

```
project/
  .cursor/rules/        # Projektweite Regeln
  backend/
    server/
      .cursor/rules/    # Backend-spezifische Regeln
  frontend/
    .cursor/rules/      # Frontend-spezifische Regeln
```

<div id="creating-a-rule">
  ### Eine Regel erstellen
</div>

Erstell Regeln mit dem Befehl `New Cursor Rule` oder über `Cursor Settings > Rules`. Dadurch wird eine neue Regeldatei in `.cursor/rules` erstellt. In den Einstellungen kannst du alle Regeln und ihren Status sehen.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=db8142786bbb7b7771ae0db8b2704b0b" alt="Vergleich zwischen kurzen und langen Regeln" data-og-width="6016" width="6016" data-og-height="3334" height="3334" data-path="images/context/rules/rule-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0b6e9b8d6ca799d1af62957726b1cc52 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8bfe1482ab9afc0995fe13371b26074b 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a847d915b3f106c42cba7cb1245bb138 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=356963b3607152f7ffe128cd1a2d050e 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=1b1e50d3721d42c691a434189729921c 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/rules/rule-settings.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d2081cf016d65053f1e517eb5734079e 2500w" />
</Frame>

<div id="generating-rules">
  ### Regeln generieren
</div>

Generiere Regeln direkt in Unterhaltungen mit dem Befehl `/Generate Cursor Rules`. Praktisch, wenn du Entscheidungen zum Agentenverhalten getroffen hast und sie wiederverwenden willst.

<Frame>
  <video src="https://www.cursor.com/changelog/049/generate-rules.mp4" controls>
    Dein Browser unterstützt das video-Element nicht.
  </video>
</Frame>

<div id="best-practices">
  ## Best Practices
</div>

Gute Regeln sind fokussiert, umsetzbar und klar abgegrenzt.

* Halt Regeln unter 500 Zeilen
* Teil große Regeln in mehrere, kombinierbare Regeln auf
* Gib konkrete Beispiele oder verlinkte Dateien an
* Vermeide vage Anleitungen. Schreib Regeln wie klare interne Doku
* Nutze Regeln wieder, wenn Prompts im Chat wiederholt werden

<div id="examples">
  ## Beispiele
</div>

<AccordionGroup>
  <Accordion title="Standards für Frontend-Komponenten und API-Validierung">
    Diese Regel legt Standards für Frontend-Komponenten fest:

    Im components-Verzeichnis:

    * Immer Tailwind für Styles verwenden
    * Framer Motion für Animationen nutzen
    * Namenskonventionen für Komponenten einhalten

    Diese Regel erzwingt die Validierung für API-Endpunkte:

    Im API-Verzeichnis:

    * zod für alle Validierungen verwenden
    * Rückgabetypen mit zod-Schemas definieren
    * Aus den Schemas generierte Typen exportieren
  </Accordion>

  <Accordion title="Vorlagen für Express-Services und React-Komponenten">
    Diese Regel stellt eine Vorlage für Express-Services bereit:

    Verwende diese Vorlage beim Erstellen eines Express-Services:

    * RESTful-Prinzipien einhalten
    * Error-Handling-Middleware einbinden
    * Sinnvolles Logging einrichten

    @express-service-template.ts

    Diese Regel definiert die Struktur von React-Komponenten:

    React-Komponenten sollten diesem Layout folgen:

    * Props-Interface oben
    * Komponente als benannter Export
    * Styles unten

    @component-template.tsx
  </Accordion>

  <Accordion title="Automatisierung von Entwicklungs-Workflows und Dokumentationsgenerierung">
    Diese Regel automatisiert die App-Analyse:

    Wenn du die App analysieren sollst:

    1. Dev-Server mit `npm run dev` starten
    2. Logs aus der Konsole holen
    3. Performance-Verbesserungen vorschlagen

    Diese Regel unterstützt die Dokumentationsgenerierung:

    Hilf beim Erstellen der Doku durch:

    * Extrahieren von Code-Kommentaren
    * Analysieren der README.md
    * Generieren von Markdown-Dokumentation
  </Accordion>

  <Accordion title="Eine neue Einstellung in Cursor hinzufügen">
    Zuerst eine Property zum Umschalten in `@reactiveStorageTypes.ts` anlegen.

    Standardwert in `INIT_APPLICATION_USER_PERSISTENT_STORAGE` in `@reactiveStorageService.tsx` hinzufügen.

    Für Beta-Features den Toggle in `@settingsBetaTab.tsx` hinzufügen, sonst in `@settingsGeneralTab.tsx`. Toggles können als `<SettingsSubSection>` für allgemeine Checkboxen hinzugefügt werden. Sieh dir den Rest der Datei für Beispiele an.

    ```
    <SettingsSubSection
    				label="Your feature name"
    				description="Your feature description"
    				value={
    					vsContext.reactiveStorageService.applicationUserPersistentStorage
    						.myNewProperty ?? false
    				}
    				onChange={(newVal) => {
    					vsContext.reactiveStorageService.setApplicationUserPersistentStorage(
    						'myNewProperty',
    						newVal
    					);
    				}}
    			/>
    ```

    Um es in der App zu verwenden, `reactiveStorageService` importieren und die Property nutzen:

    ```
    const flagIsEnabled = vsContext.reactiveStorageService.applicationUserPersistentStorage.myNewProperty
    ```
  </Accordion>
</AccordionGroup>

Viele Beispiele sind von Providern und Frameworks verfügbar. Community-beigetragene Regeln finden sich in diversen Crowdsourcing-Sammlungen und Repositories online.

<div id="agentsmd">
  ## AGENTS.md
</div>

`AGENTS.md` ist eine einfache Markdown-Datei, in der du Anweisungen für Agents definierst. Leg sie im Projekt-Root ab – als Alternative zu `.cursor/rules` für unkomplizierte Use Cases.

Im Gegensatz zu den Project Rules ist `AGENTS.md` eine reine Markdown-Datei ohne Metadaten oder komplexe Konfigurationen. Perfekt für Projekte, die einfache, gut lesbare Anweisungen brauchen, ohne den Overhead strukturierter Regeln.

```markdown  theme={null}

---

← Previous: [Memories](./memories.md) | [Index](./index.md) | Next: [Konzepte](./konzepte.md) →