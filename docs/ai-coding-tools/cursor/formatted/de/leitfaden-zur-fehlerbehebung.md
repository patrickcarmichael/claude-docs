---
title: "Leitfaden zur Fehlerbehebung"
source: "https://docs.cursor.com/de/troubleshooting/troubleshooting-guide"
language: "de"
language_name: "German"
---

# Leitfaden zur Fehlerbehebung
Source: https://docs.cursor.com/de/troubleshooting/troubleshooting-guide

Schritte zur Behebung von Problemen und zum Melden von Bugs

Probleme mit Cursor können durch Extensions, App-Daten oder Systemprobleme verursacht werden. Probier diese Schritte zur Fehlerbehebung aus.

<CardGroup cols={1}>
  <Card horizontal title="Ein Problem melden" icon="bug" href="#reporting-an-issue">
    Schritte, um ein Problem an das Cursor-Team zu melden
  </Card>
</CardGroup>

<div id="troubleshooting">
  ## Fehlerbehebung
</div>

<Steps>
  <Step title="Netzwerkverbindung prüfen">
    Check zuerst, ob Cursor seine Dienste erreichen kann.

    **Netzwerkdiagnose ausführen:** Geh zu `Cursor Settings` > `Network` und klick auf `Run Diagnostics`. Das testet deine Verbindung zu den Cursor-Servern und erkennt Netzwerkprobleme, die KI-Features, Updates oder andere Online-Funktionen beeinträchtigen.

    Wenn die Diagnose Verbindungsprobleme anzeigt, check Firewall-Einstellungen, Proxy-Konfiguration oder Netzwerkeinschränkungen, die den Zugriff von Cursor blockieren.
  </Step>

  <Step title="Erweiterungsdaten löschen">
    Bei Problemen mit Erweiterungen:

    **Alle Erweiterungen temporär deaktivieren:** Führ `cursor --disable-extensions` in der Kommandozeile aus. Wenn die Probleme weg sind, aktiviere die Erweiterungen nacheinander wieder, um die fehlerhafte zu finden.

    **Erweiterungsdaten zurücksetzen:** Deinstallier und installier problematische Erweiterungen neu, um ihre gespeicherten Daten zurückzusetzen. Check die Einstellungen auf Erweiterungskonfigurationen, die nach der Neuinstallation bestehen bleiben.
  </Step>

  <Step title="App-Daten löschen">
    <Warning>
      Dadurch werden deine App-Daten gelöscht, einschließlich Erweiterungen, Themes, Snippets und installationsbezogener Daten. Exportier zuerst dein Profil, um diese Daten zu sichern.
    </Warning>

    Cursor speichert App-Daten außerhalb der App, damit sie über Updates und Neuinstallationen hinweg wiederhergestellt werden können.

    So löschst du App-Daten:

    **Windows:** Führ diese Befehle in der Eingabeaufforderung aus:

    ```txt  theme={null}
    rd /s /q "%USERPROFILE%\AppData\Local\Programs\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Local\Cursor"
    rd /s /q "%USERPROFILE%\AppData\Roaming\Cursor"
    del /f /q "%USERPROFILE%\.cursor*"
    rd /s /q "%USERPROFILE%\.cursor"
    ```

    **macOS:** Führ `sudo rm -rf ~/Library/Application\ Support/Cursor` und `rm -f ~/.cursor.json` im Terminal aus.

    **Linux:** Führ `rm -rf ~/.cursor ~/.config/Cursor/` im Terminal aus.
  </Step>

  <Step title="Cursor deinstallieren">
    So deinstallierst du Cursor:

    <CardGroup cols={1}>
      <Card horizontal title="Windows" icon="windows">
        Such im Startmenü nach „Add or Remove Programs“, finde „Cursor“, klick auf „Uninstall“.
      </Card>

      <Card horizontal title="macOS" icon="apple">
        Öffne den Programme-Ordner, klick mit Rechts auf „Cursor“, wähl „Move to Trash“.
      </Card>

      <Card horizontal title="Linux" icon="linux">
        **Für .deb-Pakete:** `sudo apt remove cursor`

        **Für .rpm-Pakete:** `sudo dnf remove cursor` oder `sudo yum remove cursor`

        **Für AppImage:** Lösch die Datei Cursor.appimage an ihrem Speicherort.
      </Card>
    </CardGroup>
  </Step>

  <Step title="Cursor neu installieren">
    Installier neu über die [Download-Seite](https://www.cursor.com/downloads). Wenn du die App-Daten nicht gelöscht hast, stellt Cursor den vorherigen Zustand wieder her. Andernfalls bekommst du eine frische Installation.
  </Step>
</Steps>

<div id="reporting-an-issue">
  ## Ein Problem melden
</div>

Wenn diese Schritte nicht helfen, melde dich im [Forum](https://forum.cursor.com/).

<Card horizontal title="Cursor-Forum" icon="message" href="https://forum.cursor.com/">
  Melde einen Bug oder ein Problem im Cursor-Forum
</Card>

Für eine schnelle Lösung gib Folgendes an:

<CardGroup cols={2}>
  <Card title="Screenshot des Problems" icon="image">
    Mach einen Screenshot und schwärze sensible Informationen.
  </Card>

  <Card title="Schritte zur Reproduktion" icon="list-check">
    Dokumentiere die genauen Schritte, um das Problem zu reproduzieren.
  </Card>

  <Card title="Systeminformationen" icon="computer">
    Hol dir die Systeminfos von:

    <br />

    `Cursor` > `Help` > `About`
  </Card>

  <Card title="Request-IDs" icon="shield-halved" href="/de/troubleshooting/request-reporting">
    Klicke, um unseren Guide zum Sammeln von Request-IDs zu öffnen
  </Card>

  <Card title="Konsolenfehler" icon="bug">
    Öffne die Entwicklerkonsole: <br />
    `Developer: Toggle Developer Tools`
  </Card>

  <Card title="Logs" icon="file-lines">
    Öffne die Logs: <br />
    `Developer: Open Logs Folder`
  </Card>
</CardGroup>

---

← Previous: [Eine Request-ID abrufen](./eine-request-id-abrufen.md) | [Index](./index.md) | Next: [Willkommen](./willkommen.md) →