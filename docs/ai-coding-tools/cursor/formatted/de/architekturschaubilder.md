---
title: "Architekturschaubilder"
source: "https://docs.cursor.com/de/guides/tutorials/architectural-diagrams"
language: "de"
language_name: "German"
---

# Architekturschaubilder
Source: https://docs.cursor.com/de/guides/tutorials/architectural-diagrams

Lerne, mit Mermaid Architekturschaubilder zu erstellen, um Systemstruktur und Datenfluss zu visualisieren

Architekturschaubilder helfen dir, zu verstehen, wie dein System funktioniert. Du kannst sie nutzen, um Logik zu erkunden, Datenflüsse nachzuvollziehen und Strukturen zu kommunizieren. Cursor unterstützt das Generieren dieser Diagramme direkt mit Tools wie Mermaid, sodass du in nur wenigen Prompts vom Code zur Visualisierung kommst.

<Frame>
  <img alt="Beispiel für ein Architekturschaubild" src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d8dcd292e919c4640c03456a0959057" data-og-width="2048" width="2048" data-og-height="1326" height="1326" data-path="images/guides/tutorials/architectural-diagrams/postgres-flowchart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b95ed20c23aff9fccf62cd209e817719 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bdb7d7390be1d8d71a1b560a4fc892ca 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b171506e9be3be4845966f61515c09de 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=aeaee70dede56db5b6c6dc92df7ba19e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=89513a2959f659f60f06c68891f89d45 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/postgres-flowchart.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bdaf6ee66520c0e8b8b53b60f66f0b86 2500w" />
</Frame>

<div id="why-diagrams-matter">
  ## Warum Diagramme wichtig sind
</div>

Diagramme zeigen klar, wie Daten fließen und wie Komponenten miteinander interagieren. Sie sind nützlich, wenn du:

* den Kontrollfluss in deiner Codebase verstehen willst
* die Datenherkunft vom Input bis zum Output nachverfolgen musst
* andere onboardest oder dein System dokumentierst

Sie sind auch super fürs Debuggen und um smartere Fragen zu stellen. Visuals helfen dir (und dem Modell), das große Ganze zu sehen.

<div id="two-dimensions-to-consider">
  ## Zwei Dimensionen, die du berücksichtigen solltest
</div>

Es gibt ein paar verschiedene Perspektiven, über die du nachdenken kannst:

* **Zweck**: Kartierst du Logik, Datenfluss, Infrastruktur oder etwas anderes?
* **Format**: Willst du etwas Schnelles (wie ein Mermaid-Diagramm) oder etwas Formelles (wie UML)?

<div id="how-to-prompt">
  ## So promptest du richtig
</div>

Starte mit einem klaren Ziel. Hier sind ein paar gängige Arten zu fragen:

* **Ablauf**: „Zeig mir, wie Requests vom Controller bis zur Datenbank laufen.“
* **Datenlinie**: „Verfolge diese Variable vom Eintrittspunkt bis zu ihrem Ziel.“
* **Struktur**: „Gib mir eine komponentenbasierte Ansicht dieses Services.“

Du kannst Start- und Endpunkte angeben oder Cursor bitten, den gesamten Pfad zu finden.

<div id="working-with-mermaid">
  ## Arbeiten mit Mermaid
</div>

Mermaid ist leicht zu lernen und rendert direkt in Markdown (mit der richtigen Erweiterung). Cursor kann Diagramme generieren wie:

* `flowchart` für Logik und Abläufe
* `sequenceDiagram` für Interaktionen
* `classDiagram` für Objektstrukturen
* `graph TD` für einfache gerichtete Diagramme

```mermaid  theme={null}
sequenceDiagram
    participant User
    participant Server
    participant Database

    User->>Server: Formular senden
    Server->>Database: Eintrag speichern
    Database-->>Server: Erfolgreich
    Server-->>User: Bestätigung

```

Du kannst die [Mermaid-Erweiterung](https://marketplace.cursorapi.com/items?itemName=bierner.markdown-mermaid) installieren, um Diagramme in der Vorschau anzuzeigen.

1. Geh zum Reiter Extensions
2. Such nach Mermaid
3. Installieren

<Frame>
  <img alt="Mermaid-Erweiterung installieren" src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=8d5ee8d972dcc3d3789696a6d383efe6" data-og-width="1365" width="1365" data-og-height="884" height="884" data-path="images/guides/tutorials/architectural-diagrams/installing-mermaid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=bcb03e9519816da6bf4a8220fea8a319 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52805242ed097f948b7da2b078c9ee02 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5e2405e72459b4c099be1b3439b2bbd9 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=296d1022a39afa4b2016425347901452 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=88bdac627e50291bb0550eb9313f8d1f 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/tutorials/architectural-diagrams/installing-mermaid.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a9d3d7539bf41b023f1d53d68abc2dea 2500w" />
</Frame>

<div id="diagram-strategy">
  ## Diagrammstrategie
</div>

Fang klein an. Versuch nicht, alles auf einmal zu erfassen.

* Such dir eine einzelne Funktion, Route oder einen Prozess aus
* Bitte Cursor, diesen Teil mit Mermaid zu visualisieren
* Wenn du ein paar hast, bitte es, sie zu kombinieren

Das entspricht dem **C4‑Modell** – du startest auf einer niedrigen Ebene (Code oder Komponenten) und arbeitest dich zu höher­stufigen Übersichten nach oben.

<div id="recommended-flow">
  ### Empfohlener Ablauf
</div>

1. Starte mit einem detaillierten, niedrigstufigen Diagramm
2. Fasse es zu einer mittleren Ansicht zusammen
3. Wiederhole das, bis du die gewünschte Abstraktionsebene erreichst
4. Bitte Cursor, sie zu einem einzigen Diagramm oder einer Systemübersicht zusammenzuführen

```mermaid  theme={null}
graph TD
    subgraph Ebene 1: Low-Level-Komponenten
        A1[AuthService] --> A2[TokenValidator]
        A1 --> A3[UserDB]
        B1[PaymentService] --> B2[BillingEngine]
        B1 --> B3[InvoiceDB]
    end

    subgraph Ebene 2: Mid-Level-Systeme
        A[Benutzersystem] --> A1
        B[Abrechnungssystem] --> B1
    end

    subgraph Ebene 3: High-Level-Anwendung
        App[Haupt-App] --> A
        App --> B
    end

```

<div id="takeaways">
  ## Takeaways
</div>

* Nutze Diagramme, um Fluss, Logik und Daten zu verstehen
* Starte mit kleinen Prompts und erweitere dein Diagramm von dort aus
* Mermaid ist das beste Format, um in Cursor zu arbeiten
* Starte auf niedriger Ebene und abstrahiere nach oben – wie im C4-Modell
* Cursor hilft dir, Diagramme mühelos zu generieren, zu verfeinern und zu kombinieren

---

← Previous: [VS Code](./vs-code.md) | [Index](./index.md) | Next: [Einen MCP-Server erstellen](./einen-mcp-server-erstellen.md) →