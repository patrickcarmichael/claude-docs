---
title: "Bugbot"
source: "https://docs.cursor.com/de/bugbot"
language: "de"
language_name: "German"
---

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

← Previous: [Web & Mobile](./web-mobile.md) | [Index](./index.md) | Next: [Code Review](./code-review.md) →