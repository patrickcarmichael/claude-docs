---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/de/guides/languages/swift"
language: "de"
language_name: "German"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/de/guides/languages/swift

Integriere Cursor mit Xcode für Swift-Entwicklung

Willkommen bei der Swift-Entwicklung in Cursor! Egal, ob du iOS-Apps, macOS-Anwendungen oder serverseitige Swift-Projekte entwickelst – wir haben dich abgedeckt. Dieser Leitfaden hilft dir, deine Swift-Umgebung in Cursor einzurichten – startend mit den Grundlagen und anschließend mit fortgeschrittenen Features.

<div id="basic-workflow">
  ## Basis-Workflow
</div>

Der einfachste Weg, Cursor mit Swift zu nutzen, ist, ihn als deinen primären Code-Editor zu verwenden und Xcode weiterhin zum Builden und Ausführen deiner Apps zu verwenden. Du bekommst starke Features wie:

* Smarte Code-Vervollständigung
* KI-gestützte Coding-Unterstützung (probier [CMD+K](/de/inline-edit/overview) in jeder Zeile)
* Schnellzugriff auf Doku mit [@Docs](/de/context/@-symbols/@-docs)
* Syntax-Highlighting
* Grundlegende Code-Navigation

Wenn du deine App builden oder ausführen willst, wechsel einfach zu Xcode. Dieser Workflow ist perfekt für Devs, die Cursors KI nutzen wollen und für Debugging und Deployment bei den gewohnten Xcode-Tools bleiben.

<div id="hot-reloading">
  ### Hot Reloading
</div>

Wenn du Xcode-Workspaces oder -Projekte verwendest (statt einen Ordner direkt in Xcode zu öffnen), kann es passieren, dass Xcode Änderungen an deinen Dateien ignoriert, die in Cursor oder generell außerhalb von Xcode vorgenommen wurden.

Zwar kannst du den Ordner in Xcode öffnen, um das zu beheben, aber je nach Swift-Workflow brauchst du eventuell ein Projekt.

Eine starke Lösung dafür ist [Inject](https://github.com/krzysztofzablocki/Inject), eine Hot-Reloading-Bibliothek für Swift, die deiner App echtes Hot Reloading ermöglicht und sie sofort aktualisiert, sobald du Änderungen machst. Das ist nicht von den Nebenwirkungen des Xcode-Workspace/-Projekt-Themas betroffen und erlaubt dir, Änderungen in Cursor vorzunehmen und sie unmittelbar in deiner App zu sehen.

<CardGroup cols={1}>
  <Card title="Inject – Hot Reloading für Swift" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Erfahre mehr über Inject und wie du es in deinen Swift-Projekten einsetzt.
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## Fortgeschrittene Swift-Entwicklung
</div>

<Note>
  Dieser Abschnitt des Guides wurde stark von [Thomas
  Ricouard](https://x.com/Dimillian) und seinem
  [Artikel](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  über die Verwendung von Cursor für iOS-Entwicklung inspiriert. Schau dir seinen Artikel für mehr
  Details an und lass ihm gern ein Follow da für mehr Swift-Content.
</Note>

Wenn du nur einen Editor gleichzeitig geöffnet haben willst und vermeiden möchtest, zwischen Xcode und Cursor zu wechseln, kannst du eine Erweiterung wie [Sweetpad](https://sweetpad.hyzyla.dev/) verwenden, um Cursor direkt in das zugrunde liegende Buildsysteem von Xcode zu integrieren.

Sweetpad ist eine leistungsstarke Erweiterung, mit der du deine Swift-Projekte direkt in Cursor bauen, ausführen und debuggen kannst, ohne auf Xcodes Funktionen zu verzichten.

Um mit Sweetpad loszulegen, musst du Xcode weiterhin auf deinem Mac installiert haben – es ist die Grundlage der Swift-Entwicklung. Du kannst Xcode aus dem [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835) herunterladen. Sobald Xcode eingerichtet ist, lass uns deine Entwicklungsumgebung in Cursor mit ein paar essenziellen Tools verbessern.

Öffne dein Terminal und führe Folgendes aus:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →