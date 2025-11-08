---
title: "Java"
source: "https://docs.cursor.com/de/guides/languages/java"
language: "de"
language_name: "German"
---

# Java
Source: https://docs.cursor.com/de/guides/languages/java

Java-Entwicklung mit JDK, Erweiterungen und Build-Tools einrichten

Dieser Guide hilft dir, Cursor für die Java-Entwicklung zu konfigurieren – inklusive Einrichtung des JDK, Installation der benötigten Erweiterungen, Debugging, Ausführen von Java-Anwendungen und Integration von Build-Tools wie Maven und Gradle. Außerdem behandelt er Workflow-Features, die IntelliJ oder VS Code ähneln.

<Note>
  Bevor du startest, stell sicher, dass du Cursor installiert und auf die
  neueste Version aktualisiert hast.
</Note>

<div id="setting-up-java-for-cursor">
  ## Java für Cursor einrichten
</div>

<div id="java-installation">
  ### Java-Installation
</div>

Bevor du Cursor einrichtest, muss Java auf deinem Rechner installiert sein.

<Warning>
  Cursor enthält keinen Java-Compiler, daher musst du ein JDK installieren, falls du das noch nicht getan hast.
</Warning>

<CardGroup cols={1}>
  <Card title="Windows-Installation" icon="windows">
    Lade ein JDK herunter und installiere es (z. B. OpenJDK, Oracle JDK, Microsoft Build of OpenJDK).

    <br />

    Setz JAVA\_HOME und füge JAVA\_HOME\bin zu deinem PATH hinzu.
  </Card>

  <Card title="macOS-Installation" icon="apple">
    Installiere über Homebrew (`brew install openjdk`) oder lade einen Installer herunter.

    <br />

    Stell sicher, dass JAVA\_HOME auf das installierte JDK zeigt.
  </Card>

  <Card title="Linux-Installation" icon="linux">
    Verwende deinen Paketmanager (`sudo apt install openjdk-17-jdk` oder Äquivalent) oder installiere über SDKMAN.
  </Card>
</CardGroup>

Um die Installation zu prüfen, führe Folgendes aus:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Wenn Cursor dein JDK nicht erkennt, konfigurier es manuell in der settings.json:
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/path/to/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/path/to/jdk-17",
      "default": true
    }
  ]
}
```

<Warning>Starte Cursor neu, damit die Änderungen wirksam werden.</Warning>

<div id="cursor-setup">
  ### Cursor-Setup
</div>

<Info>Cursor unterstützt VS Code-Erweiterungen. Installiere die folgenden manuell:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Enthält Java-Sprachunterstützung, Debugger, Test-Runner, Maven-Support und
    Projektverwaltung
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Unverzichtbar für die Arbeit mit dem Gradle-Build-System
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Erforderlich für die Entwicklung mit Spring Boot
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Notwendig für die Entwicklung von Kotlin-Anwendungen
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### Build-Tools konfigurieren
</div>

<div id="maven">
  #### Maven
</div>

Stell sicher, dass Maven installiert ist (`mvn -version`). Bei Bedarf von [maven.apache.org](https://maven.apache.org/download.cgi) installieren:

1. Binärarchiv herunterladen
2. An den gewünschten Ort entpacken
3. Umgebungsvariable MAVEN\_HOME auf den entpackten Ordner setzen
4. %MAVEN\_HOME%\bin (Windows) oder \$MAVEN\_HOME/bin (Unix) zur PATH-Variable hinzufügen

<div id="gradle">
  #### Gradle
</div>

Stell sicher, dass Gradle installiert ist (`gradle -version`). Bei Bedarf von [gradle.org](https://gradle.org/install/) installieren:

1. Binärdistribution herunterladen
2. An den gewünschten Ort entpacken
3. Umgebungsvariable GRADLE\_HOME auf den entpackten Ordner setzen
4. %GRADLE\_HOME%\bin (Windows) oder \$GRADLE\_HOME/bin (Unix) zur PATH-Variable hinzufügen

Alternativ kannst du den Gradle Wrapper verwenden, der automatisch die passende Gradle-Version herunterlädt und nutzt:

<div id="running-and-debugging">
  ## Ausführen und Debuggen
</div>

Alles ist eingerichtet – Zeit, deinen Java-Code auszuführen und zu debuggen.
Je nach Bedarf kannst du folgende Methoden verwenden:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Klick auf den „Run“-Link, der oberhalb jeder main-Methode erscheint, um dein
    Programm schnell auszuführen
  </Card>

  <Card title="Debug" icon="bug">
    Öffne das Seitenleisten-Panel „Run and Debug“ und nutz den „Run“-Button, um
    deine Anwendung zu starten
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Ausführen über die Kommandozeile mit Maven- oder Gradle-Befehlen
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Starte Spring-Boot-Anwendungen direkt über die „Spring Boot Dashboard“-
    Erweiterung
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor-Workflow
</div>

Die KI-Features von Cursor können deinen Java-Workflow deutlich verbessern. So nutzt du Cursors Fähigkeiten speziell für Java:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      Smarte Vervollständigungen für Methoden, Signaturen und Java-Boilerplate wie
      Getter/Setter.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Design-Patterns umsetzen, Code refaktorisieren oder Klassen mit korrekter
      Vererbung generieren.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      Schnelle Inline-Änderungen an Methoden vornehmen, Fehler beheben oder Unit-Tests generieren –
      ohne deinen Flow zu unterbrechen.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Hilfe zu Java-Konzepten bekommen, Exceptions debuggen oder Framework-
      Features verstehen.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### Beispiel-Workflows
</div>

1. **Java-Boilerplate generieren**\
   Verwende die [Tab completion](/de/tab/overview), um schnell Konstruktoren, Getter/Setter, equals-/hashCode-Methoden und andere repetitive Java-Muster zu erstellen.

2. **Komplexe Java-Exceptions debuggen**\
   Wenn du auf einen kryptischen Java-Stacktrace stößt, markier ihn und nutze [Ask](/de/chat/overview), um die Ursache zu erklären und mögliche Fixes vorzuschlagen.

3. **Legacy-Java-Code refaktorisieren**\
   Nutze den [Agent mode](/de/chat/agent), um älteren Java-Code zu modernisieren – anonyme Klassen in Lambdas umwandeln, auf neuere Java-Sprachfeatures upgraden oder Design-Patterns implementieren.

4. **Framework-Entwicklung**\
   Füg deine Doku mit @docs zum Cursor-Kontext hinzu und generier framework-spezifischen Code überall in Cursor.

---

← Previous: [Arbeiten mit Dokumentation](./arbeiten-mit-dokumentation.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →