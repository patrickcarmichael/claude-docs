---
title: "Häufige Probleme"
source: "https://docs.cursor.com/de/troubleshooting/common-issues"
language: "de"
language_name: "German"
---

# Häufige Probleme
Source: https://docs.cursor.com/de/troubleshooting/common-issues

Lösungen für häufige Probleme und FAQs

Unten findest du häufige Probleme und ihre Lösungen.

<div id="networking-issues">
  ### Netzwerkprobleme
</div>

Check zuerst deine Netzwerkverbindung. Geh zu `Cursor Settings` > `Network` und klick auf `Run Diagnostics`. Das testet deine Verbindung zu den Cursor‑Servern und hilft, netzwerkbedingte Probleme zu erkennen, die AI‑Features, Updates oder andere Online‑Funktionen beeinträchtigen könnten.

Cursor setzt für AI‑Features auf HTTP/2, weil damit gestreamte Antworten effizient übertragen werden. Wenn dein Netzwerk kein HTTP/2 unterstützt, kann es zu Indexierungsfehlern und Problemen mit AI‑Features kommen.

Das passiert oft in Unternehmensnetzwerken, mit VPNs oder bei Proxys wie Zscaler.

Um das zu beheben, aktiviere das HTTP/1.1‑Fallback in den App‑Einstellungen (nicht in den Cursor‑Einstellungen): Drück `CMD/CTRL + ,`, such nach `HTTP/2` und aktiviere `Disable HTTP/2`. Dadurch wird HTTP/1.1 erzwungen und das Problem behoben.

Wir planen, automatische Erkennung und automatisches Fallback hinzuzufügen.

<div id="resource-issues-cpu-ram-etc">
  ### Ressourcenprobleme (CPU, RAM, etc.)
</div>

Hohe CPU‑ oder RAM‑Auslastung kann deinen Rechner verlangsamen oder Ressourcenwarnungen auslösen.

Große Codebasen benötigen zwar mehr Ressourcen, aber hohe Auslastung kommt meist von Erweiterungen oder fehlerhaften Einstellungen.

<Note>
  Wenn du auf **macOS** eine Warnung für wenig RAM siehst, beachte bitte, dass es bei einigen Nutzer:innen einen Bug gibt, der völlig falsche Werte anzeigen kann. Öffne in diesem Fall den Aktivitätsmonitor und schau im Tab „Memory“ nach, um die korrekte Speicherauslastung zu sehen.
</Note>

Wenn du hohe CPU‑ oder RAM‑Auslastung feststellst, probier Folgendes:

<AccordionGroup>
  <Accordion title="Check deine Erweiterungen">
    Erweiterungen können die Performance beeinflussen.

    Der Extension Monitor zeigt den Ressourcenverbrauch aller installierten und integrierten Erweiterungen.

    Aktiviere den Extension Monitor unter `Settings` > `Application` > `Experimental` und schalte `Extension Monitor: Enabled` ein. Danach wirst du aufgefordert, Cursor neu zu starten.

    Öffnen: `Cmd/Ctrl + Shift + P` → `Developer: Open Extension Monitor`.

    Cursor führt deine Erweiterungen in einem oder mehreren **Extension Hosts** aus. Meist laufen die meisten deiner Erweiterungen im selben Extension Host – eine Erweiterung mit hohem CPU‑Verbrauch kann dadurch ihre Nachbarerweiterungen ausbremsen!

    Der Extension Monitor zeigt:

    * Jeden langlebigen Prozess, der von einer Erweiterung gestartet wurde (nur macOS und Linux).
    * **% Ext Host**: Den Prozentsatz der gesamten Extension‑Host‑Zeit, den diese Erweiterung verbraucht. Hilft zu erkennen, welche Erweiterungen relativ am meisten Zeit nutzen.
    * **Max Blocking**: Den längsten ununterbrochenen Ausführungsblock einer Erweiterung pro Monitoring‑Intervall.
    * **% CPU**:
      * Für Erweiterungen: Den Prozentsatz der gesamten CPU‑Nutzung, der dem Code der Erweiterung zugerechnet wird.
      * Für Prozesse: Den Prozentsatz der gesamten CPU‑Nutzung, der dem gestarteten Prozess zugerechnet wird (nur macOS und Linux).
    * **Memory**:
      * Für Erweiterungen: Die Menge an JS‑Heap‑Speicher, die vom Code der Erweiterung genutzt wird (externe Allokationen nicht enthalten).
      * Für Prozesse: Die Menge an Systemspeicher, die vom gestarteten Prozess genutzt wird (nur macOS und Linux).

    Du kannst auch testen, indem du `cursor --disable-extensions` in der Kommandozeile ausführst. Wenn sich die Performance verbessert, aktiviere Erweiterungen nacheinander wieder, um die problematischen zu finden.

    Probier Extension Bisect, um problematische Erweiterungen zu identifizieren. Mehr dazu [hier](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect#_welcome-extension-bisect). Hinweis: Das funktioniert am besten bei sofort auftretenden Problemen, nicht bei schleichender Performance‑Verschlechterung.
  </Accordion>

  <Accordion title="Verwende den Process Explorer">
    Der Process Explorer zeigt, welche Prozesse Ressourcen verbrauchen.

    Öffnen: Command Palette (`Cmd/Ctrl + Shift + P`) → `Developer: Open Process Explorer`.

    Check die Prozesse unter:

    * **`extensionHost`**: Erweiterungsbezogene Probleme
    * **`ptyHost`**: Ressourcenverbrauch des Terminals

    Der Process Explorer zeigt jedes Terminal und seine laufenden Befehle zur Diagnose an.

    Für andere Prozesse mit hoher Auslastung melde dich im [Forum](https://forum.cursor.com/).
  </Accordion>

  <Accordion title="Systemressourcen monitoren">
    Nutze die Monitoring‑Tools deines Betriebssystems, um festzustellen, ob das Problem Cursor‑spezifisch oder systemweit ist.
  </Accordion>

  <Accordion title="Minimale Installation testen">
    Wenn Probleme weiterhin bestehen, teste eine minimale Cursor‑Installation.
  </Accordion>
</AccordionGroup>

<div id="general-faqs">
  ## Allgemeine FAQs
</div>

<AccordionGroup>
  <Accordion title="Ich sehe ein Update im Changelog, aber Cursor aktualisiert sich nicht">
    Neue Updates werden in Wellen ausgerollt – zufällig ausgewählte Nutzer bekommen sie zuerst. Dein Update sollte in ein paar Tagen kommen.
  </Accordion>

  <Accordion title="Ich habe Probleme mit meinem GitHub-Login in Cursor / Wie logge ich mich in Cursor aus GitHub aus?">
    Nutze `Sign Out of GitHub` in der Befehlspalette `Ctrl/⌘ + Shift + P`.
  </Accordion>

  <Accordion title="Ich kann GitHub Codespaces nicht verwenden">
    GitHub Codespaces wird noch nicht unterstützt.
  </Accordion>

  <Accordion title="Ich habe Fehler bei der Verbindung zu Remote SSH">
    SSH zu Mac- oder Windows-Maschinen wird nicht unterstützt. Für andere Probleme poste mit Logs im [Forum](https://forum.cursor.com/).
  </Accordion>

  <Accordion title="SSH-Verbindungsprobleme unter Windows">
    Wenn du „SSH is only supported in Microsoft versions of VS Code“ siehst:

    1. Remote-SSH deinstallieren:
       * Erweiterungen-Ansicht öffnen (`Ctrl + Shift + X`)
       * Nach „Remote-SSH“ suchen
       * Zahnrad-Symbol klicken → „Uninstall“

    2. Anysphere Remote SSH installieren:
       * Cursor-Marktplatz öffnen
       * Nach „SSH“ suchen
       * Die Anysphere Remote SSH-Erweiterung installieren

    3. Nach der Installation:
       * Alle VS Code-Instanzen mit aktiven SSH-Verbindungen schließen
       * Cursor neu starten
       * Erneut per SSH verbinden

    Prüfe, ob deine SSH-Konfiguration und -Keys korrekt eingerichtet sind.
  </Accordion>

  <Accordion title="Cursor Tab und Inline Edit funktionieren hinter meinem Firmen-Proxy nicht">
    Cursor Tab und Inline Edit verwenden HTTP/2 für geringere Latenz und Ressourcennutzung. Einige Unternehmens-Proxys (z. B. Zscaler) blockieren HTTP/2. Beheb das, indem du `"cursor.general.disableHttp2": true` in den Einstellungen setzt (`Cmd/Ctrl + ,`, nach `http2` suchen).
  </Accordion>

  <Accordion title="Ich habe gerade Pro abonniert, aber in der App bin ich immer noch im Free-Plan">
    Melde dich in den Cursor-Einstellungen ab und wieder an.
  </Accordion>

  <Accordion title="Wann wird meine Nutzung wieder zurückgesetzt?">
    Pro-Abonnenten: Klicke im [Dashboard](https://cursor.com/dashboard) auf `Manage Subscription`, um dein Verlängerungsdatum zu sehen.

    Free-User: Check das Datum deiner ersten Cursor-E-Mail. Die Nutzung wird monatlich ab diesem Datum zurückgesetzt.
  </Accordion>

  <Accordion title="Meine Chat-/Composer-Historie ist nach einem Update verschwunden">
    Wenig Speicherplatz kann dazu führen, dass Cursor während Updates historische Daten löscht. Um das zu verhindern:

    1. Vor dem Update genug freien Speicherplatz sicherstellen
    2. Regelmäßig unnötige Systemdateien bereinigen
    3. Wichtige Unterhaltungen vor dem Update sichern
  </Accordion>

  <Accordion title="Wie deinstalliere ich Cursor?">
    Folge [dieser Anleitung](https://code.visualstudio.com/docs/setup/uninstall). Ersetze „VS Code“ oder „Code“ durch „Cursor“ und „.vscode“ durch „.cursor“.
  </Accordion>

  <Accordion title="Wie lösche ich mein Konto?">
    Klicke im [Dashboard](https://cursor.com/dashboard) auf `Delete Account`. Dadurch werden dein Konto und alle zugehörigen Daten dauerhaft gelöscht.
  </Accordion>

  <Accordion title="Wie öffne ich Cursor über die Kommandozeile?">
    Führe `cursor` in deinem Terminal aus. Falls der Befehl fehlt:

    1. Befehlspalette öffnen `⌘⇧P`
    2. `install command` eingeben
    3. `Install 'cursor' command` auswählen (optional den `code`-Befehl installieren, um den von VS Code zu überschreiben)
  </Accordion>

  <Accordion title="Anmeldung bei Cursor nicht möglich">
    Wenn ein Klick auf Sign In zu cursor.com weiterleitet, dich aber nicht anmeldet, deaktivier deine Firewall oder Antiviren-Software – die könnte den Anmeldeprozess blockieren.
  </Accordion>

  <Accordion title="Meldung über verdächtige Aktivität">
    Aufgrund der jüngsten Zunahme von Missbrauch könnte deine Anfrage aus Sicherheitsgründen blockiert worden sein. So löst du das:

    Check zuerst dein VPN. Wenn du eins nutzt, probier es auszuschalten, da VPNs manchmal unsere Sicherheitssysteme triggern.

    Wenn das nicht hilft, kannst du Folgendes probieren:

    * Einen neuen Chat erstellen
    * Kurz warten und später erneut versuchen
    * Ein neues Konto mit Google- oder GitHub-Authentifizierung erstellen
    * Auf Cursor Pro upgraden
  </Accordion>
</AccordionGroup>

---

← Previous: [MCP-Server](./mcp-server.md) | [Index](./index.md) | Next: [Eine Request-ID abrufen](./eine-request-id-abrufen.md) →