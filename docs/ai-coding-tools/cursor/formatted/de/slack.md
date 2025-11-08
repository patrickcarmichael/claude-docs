---
title: "Slack"
source: "https://docs.cursor.com/de/integrations/slack"
language: "de"
language_name: "German"
---

# Slack
Source: https://docs.cursor.com/de/integrations/slack

Mit Background Agents in Slack arbeiten

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

Mit der Cursor-Integration für Slack kannst du [Background Agents](/de/background-agent) nutzen, um direkt in Slack an deinen Aufgaben zu arbeiten, indem du <SlackInlineMessage message="@Cursor" /> mit einem Prompt erwähnst.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## Einstieg
</div>

<div id="installation">
  ### Installation
</div>

1. Geh zu [Cursor Integrations](https://www.cursor.com/en/dashboard?tab=integrations)

2. Klick auf *Connect* neben Slack oder geh von hier zur [Installationsseite](https://cursor.com/api/install-slack-app)

3. Du wirst aufgefordert, die Cursor-App für Slack in deinem Workspace zu installieren.

4. Nachdem du die Installation in Slack abgeschlossen hast, wirst du zurück zu Cursor weitergeleitet, um das Setup abzuschließen

   1. GitHub verbinden (falls noch nicht verbunden) und ein Standard-Repository auswählen
   2. Nutzungsbasierte Abrechnung aktivieren
   3. Datenschutzeinstellungen bestätigen

5. Starte mit Background Agents in Slack, indem du <SlackInlineMessage message="@Cursor" /> erwähnst

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## So verwendest du’s
</div>

Erwähne <SlackInlineMessage message="@Cursor" /> und gib deinen Prompt ein. Das deckt die meisten Use-Cases ab, aber du kannst auch die folgenden Befehle verwenden, um deinen Agent anzupassen.

Zum Beispiel kannst du <SlackInlineMessage message="@Cursor fix the login bug" /> direkt in der Unterhaltung erwähnen oder spezifische Befehle wie <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> verwenden, um ein bestimmtes Repository anzusteuern.

<div id="commands">
  ### Commands
</div>

Führe <SlackInlineMessage message="@Cursor help" /> aus, um eine aktuelle Befehlsliste zu erhalten.

<div className="full-width-table">
  | Command                                                     | Description                                                                                                 |
  | :---------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Startet einen Background Agent. In Threads mit bestehenden Agenten werden Follow-up-Anweisungen hinzugefügt |
  | <SlackInlineMessage message="@Cursor settings" />           | Standardwerte und das Standard-Repository des Channels konfigurieren                                        |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Erweiterte Optionen verwenden: `branch`, `model`, `repo`                                                    |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Erzwingt das Erstellen eines neuen Agenten in einem Thread                                                  |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Zeig deine laufenden Agenten                                                                                |
</div>

<div id="options">
  #### Options
</div>

Passe das Verhalten des Background Agent mit diesen Optionen an:

<div className="full-width-table">
  | Option   | Description                                 | Example           |
  | :------- | :------------------------------------------ | :---------------- |
  | `branch` | Basis-Branch festlegen                      | `branch=main`     |
  | `model`  | AI-Modell wählen                            | `model=o3`        |
  | `repo`   | Spezifisches Repository angeben             | `repo=owner/repo` |
  | `autopr` | Automatische PR-Erstellung ein-/ausschalten | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### Syntax Formats
</div>

Verwende Optionen auf mehrere Arten:

1. **Bracket-Format**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Inline-Format**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### Option precedence
</div>

Beim Kombinieren von Optionen gilt:

* **Explizite Werte** überschreiben Defaults
* **Spätere Werte** überschreiben frühere bei Duplikaten
* **Inline-Optionen** haben Vorrang vor Defaults im Settings-Modal

Der Bot parst Optionen überall im Text der Nachricht, was natürliches Schreiben von Befehlen ermöglicht.

<div id="using-thread-context">
  #### Thread-Kontext verwenden
</div>

Background Agents verstehen und nutzen Kontext aus bestehenden Thread-Diskussionen. Nützlich, wenn dein Team ein Issue diskutiert und du willst, dass der Agent die Lösung basierend auf dieser Unterhaltung umsetzt.

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Background Agents lesen beim Aufruf den gesamten Thread als Kontext,
  verstehen die Diskussion des Teams und setzen darauf basierend Lösungen um.
</Note>

<div id="when-to-use-force-commands">
  #### Wann Force-Befehle verwenden
</div>

**Wann brauch ich <SlackInlineMessage message="@Cursor agent" />?**

In Threads mit bestehenden Agenten fügt <SlackInlineMessage message="@Cursor [prompt]" /> Follow-up-Anweisungen hinzu (funktioniert nur, wenn der Agent dir gehört). Verwende <SlackInlineMessage message="@Cursor agent [prompt]" />, um einen separaten Agent zu starten.

**Wann brauch ich `Add follow-up` (über das Kontextmenü)?**

Verwende das Kontextmenü (⋯) bei der Antwort eines Agenten für Follow-up-Anweisungen. Nützlich, wenn mehrere Agenten in einem Thread existieren und du angeben musst, auf welchen du dich beziehst.

### Status-Updates & Handoff

Wenn der Background Agent läuft, bekommst du zuerst die Option, *Open in Cursor* zu öffnen.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Wenn der Background Agent fertig ist, bekommst du eine Benachrichtigung in Slack und kannst den erstellten PR auf GitHub ansehen.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### Agents verwalten
</div>

Um alle laufenden Agents zu sehen, führe <SlackInlineMessage message="@Cursor list my agents" /> aus.

Verwalte Background Agents über das Kontextmenü, indem du auf die drei Punkte (⋯) in einer Agent-Nachricht klickst.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Verfügbare Optionen:

* **Add follow-up**: Füge einem bestehenden Agent weitere Anweisungen hinzu
* **Delete**: Stoppe und archiviere den Background Agent
* **View request ID**: Zeige die eindeutige Request-ID zur Problembehebung an (mit angeben, wenn du den Support kontaktierst)
* **Give feedback**: Gib Feedback zur Agent-Performance

<div id="configuration">
  ## Konfiguration
</div>

Verwalte Standard-Einstellungen und Datenschutzoptionen im [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div id="settings">
  ### Einstellungen
</div>

<div id="default-model">
  #### Standardmodell
</div>

Wird verwendet, wenn kein Modell explizit mit <SlackInlineMessage message="@Cursor [model=...]" /> angegeben ist. Siehe [Einstellungen](https://www.cursor.com/dashboard?tab=background-agents) für verfügbare Optionen.

<div id="default-repository">
  #### Standard-Repository
</div>

Wird verwendet, wenn kein Repository angegeben ist. Nutze diese Formate:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  Wenn du ein nicht vorhandenes Repository angibst, wirkt es so, als hättest du
  keinen Zugriff. Das zeigt sich in der Fehlermeldung, wenn der Background Agent nicht startet.
</Note>

<div id="base-branch">
  #### Basis-Branch
</div>

Start-Branch für Background Agent. Leer lassen, um den Standard-Branch des Repositorys zu verwenden (oft `main`)

<div id="channel-settings">
  ### Kanaleinstellungen
</div>

Konfiguriere Standard-Einstellungen auf Kanalebene mit <SlackInlineMessage message="@Cursor settings" />. Diese Einstellungen gelten pro Team und überschreiben deine persönlichen Standardwerte für diesen Kanal.

Besonders nützlich, wenn:

* Unterschiedliche Kanäle an unterschiedlichen Repositories arbeiten
* Teams konsistente Einstellungen für alle Mitglieder wollen
* Du vermeiden willst, das Repository in jedem Befehl anzugeben

So konfigurierst du Kanaleinstellungen:

1. Führe <SlackInlineMessage message="@Cursor settings" /> im gewünschten Kanal aus
2. Setze das Standard-Repository für diesen Kanal
3. Alle Teammitglieder, die Background Agents in diesem Kanal verwenden, nutzen diese Standardwerte

<Note>
  Kanaleinstellungen haben Vorrang vor persönlichen Standardwerten, können aber durch
  explizite Optionen wie{" "}
  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" /> überschrieben werden
</Note>

<div id="privacy">
  ### Datenschutz
</div>

Background Agents unterstützen den Privacy Mode.

Lies mehr über den [Privacy Mode](https://www.cursor.com/privacy-overview) oder verwalte deine [Datenschutzeinstellungen](https://www.cursor.com/dashboard?tab=background-agents).

<Warning>
  Privacy Mode (Legacy) wird nicht unterstützt. Background Agents benötigen während der Ausführung temporären
  Codespeicher.
</Warning>

<div id="display-agent-summary">
  #### Agent-Zusammenfassung anzeigen
</div>

Zeige Agent-Zusammenfassungen und Diff-Bilder an. Kann Dateipfade oder Code-Snippets enthalten. Kann ein-/ausgeschaltet werden.

<div id="display-agent-summary-in-external-channels">
  #### Agent-Zusammenfassung in externen Kanälen anzeigen
</div>

Für Slack Connect mit anderen Workspaces oder Kanälen mit externen Mitgliedern wie Gästen kannst du festlegen, ob Agent-Zusammenfassungen in externen Kanälen angezeigt werden.

<div id="permissions">
  ## Berechtigungen
</div>

Cursor fordert diese Slack-Berechtigungen an, damit Background Agents in deinem Workspace funktionieren:

<div className="full-width-table">
  | Permission          | Description                                                                                                      |
  | :------------------ | :--------------------------------------------------------------------------------------------------------------- |
  | `app_mentions:read` | Erkennt @-Erwähnungen, um Background Agents zu starten und auf Anfragen zu reagieren                             |
  | `channels:history`  | Liest frühere Nachrichten in Threads, um beim Hinzufügen von Folgeanweisungen Kontext zu haben                   |
  | `channels:join`     | Tritt öffentlichen Channels automatisch bei, wenn eingeladen oder angefordert                                    |
  | `channels:read`     | Greift auf Channel-Metadaten (IDs und Namen) zu, um Antworten und Updates zu posten                              |
  | `chat:write`        | Sendet Status-Updates, Abschlussbenachrichtigungen und PR-Links, sobald Agents fertig sind                       |
  | `files:read`        | Lädt geteilte Dateien (Logs, Screenshots, Codebeispiele) für zusätzlichen Kontext herunter                       |
  | `files:write`       | Lädt visuelle Zusammenfassungen von Agent-Änderungen für eine schnelle Durchsicht hoch                           |
  | `groups:history`    | Liest frühere Nachrichten in privaten Channels, um Kontext in mehrstufigen Gesprächen zu haben                   |
  | `groups:read`       | Greift auf Metadaten privater Channels zu, um Antworten zu posten und den Gesprächsfluss aufrechtzuerhalten      |
  | `im:history`        | Greift auf den Verlauf von Direktnachrichten zu, um Kontext in fortgesetzten Gesprächen zu haben                 |
  | `im:read`           | Liest DM-Metadaten, um Teilnehmende zu identifizieren und korrektes Threading sicherzustellen                    |
  | `im:write`          | Startet Direktnachrichten für private Benachrichtigungen oder individuelle Kommunikation                         |
  | `mpim:history`      | Greift auf den Verlauf von Gruppen-DMs zu, um Gespräche mit mehreren Teilnehmenden zu unterstützen               |
  | `mpim:read`         | Liest Gruppen-DM-Metadaten, um Teilnehmende anzusprechen und eine korrekte Zustellung sicherzustellen            |
  | `reactions:read`    | Beobachtet Emoji-Reaktionen als Nutzerfeedback und Statussignale                                                 |
  | `reactions:write`   | Fügt Emoji-Reaktionen hinzu, um den Status zu markieren – ⏳ für läuft, ✅ für abgeschlossen, ❌ für fehlgeschlagen |
  | `team:read`         | Identifiziert Workspace-Details, um Installationen zu trennen und Einstellungen anzuwenden                       |
  | `users:read`        | Ordnet Slack-Nutzer:innen Cursor-Konten zu, um Berechtigungen und sicheren Zugriff zu gewährleisten              |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Modelle](./modelle.md) →