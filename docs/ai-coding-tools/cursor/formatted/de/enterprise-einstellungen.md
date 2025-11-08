---
title: "Enterprise-Einstellungen"
source: "https://docs.cursor.com/de/account/teams/enterprise-settings"
language: "de"
language_name: "German"
---

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

---

← Previous: [Dashboard](./dashboard.md) | [Index](./index.md) | Next: [Mitglieder & Rollen](./mitglieder-rollen.md) →