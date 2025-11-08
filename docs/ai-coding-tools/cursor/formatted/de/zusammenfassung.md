---
title: "Zusammenfassung"
source: "https://docs.cursor.com/de/agent/chat/summarization"
language: "de"
language_name: "German"
---

# Zusammenfassung
Source: https://docs.cursor.com/de/agent/chat/summarization

Kontextmanagement für lange Chats

<div id="message-summarization">
  ## Zusammenfassung von Nachrichten
</div>

Wenn Unterhaltungen länger werden, fasst Cursor automatisch zusammen und verwaltet den Kontext, damit deine Chats effizient bleiben. Lern, wie du das Kontextmenü nutzt, und versteh, wie Dateien verdichtet werden, damit sie in die Kontextfenster des Modells passen.

<div id="using-the-summarize-command">
  ### Verwendung des Befehls /summarize
</div>

Du kannst die Zusammenfassung manuell mit dem Befehl `/summarize` im Chat auslösen. Dieser Befehl hilft dabei, den Kontext zu verwalten, wenn Unterhaltungen zu lang werden, sodass du effizient weiterarbeiten kannst, ohne wichtige Informationen zu verlieren.

<Info>
  Für einen tieferen Einblick, wie Kontext in Cursor funktioniert, schau dir unseren Guide [Mit
  Kontext arbeiten](/de/guides/working-with-context) an.
</Info>

<div id="how-summarization-works">
  ### So funktioniert die Zusammenfassung
</div>

Wenn Unterhaltungen länger werden, überschreiten sie das Kontextfensterlimit des Modells:

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">Kontextfensterlimit</div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

Um das zu lösen, fasst Cursor ältere Nachrichten zusammen, damit Platz für neue Unterhaltungsteile entsteht.

<Frame>
  <div className="font-mono text-xs w-full bg-neutral-100 p-4 rounded-lg">
    <div className="relative">
      <div className="relative my-4">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-xs text-black bg-neutral-100 px-2">
          Kontextfensterlimit
        </div>

        <div className="w-full h-px bg-black" />
      </div>

      <div className="bg-neutral-100 px-3 py-2 mb-2 rounded border border-dashed border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">
          Zusammengefasste Nachrichten
        </div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">User</div>
      </div>

      <div className="bg-white px-3 py-2 mb-2 rounded border border-neutral-400 w-full">
        <div className="text-xs text-neutral-700 font-medium">Cursor</div>
      </div>
    </div>
  </div>
</Frame>

## Komprimierung von Dateien & Ordnern

Während die Chatszusammenfassung lange Unterhaltungen abdeckt, nutzt Cursor für große Dateien und Ordner eine andere Strategie: **smarte Komprimierung**. Wenn du Dateien in deine Unterhaltung einbindest, ermittelt Cursor anhand ihrer Größe und des verfügbaren Kontextbereichs die beste Darstellung.

Das sind die verschiedenen Zustände, in denen sich eine Datei/ein Ordner befinden kann:

<div id="condensed">
  ### Kompaktansicht
</div>

Wenn Dateien oder Ordner zu groß für das Kontextfenster sind, komprimiert Cursor sie automatisch. In der Kompaktansicht sieht das Modell zentrale Strukturelemente wie Funktionssignaturen, Klassen und Methoden. Aus dieser kompakten Darstellung kann das Modell bei Bedarf einzelne Dateien aufklappen. So wird das verfügbare Kontextfenster optimal genutzt.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0c3a07b6fef6402945138f7ee38b44c1" alt="Kontextmenü" data-og-width="1226" width="1226" data-og-height="793" height="793" data-path="images/context/context-management/condensed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=4cc08626f9cfce1d186cdd6aa96c7d09 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=fa49ce9605bdb0186c98712f4c0a32cc 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=84874b2f40bff0a2cd54796865469914 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=050290a85c154e92f9298883afcdf892 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f953aa28f11926b2d6fdf734cf928402 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/condensed.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=50aa9973ccf2027814860f3d97a2b031 2500w" />
</Frame>

<div id="significantly-condensed">
  ### Stark gekürzt
</div>

Wenn ein Dateiname mit der Kennzeichnung „Stark gekürzt“ erscheint, war die Datei zu groß, um selbst in gekürzter Form vollständig aufgenommen zu werden. Dem Modell wird nur der Dateiname angezeigt.

<div id="not-included">
  ### Nicht enthalten
</div>

Wenn neben einer Datei oder einem Ordner ein Warnsymbol angezeigt wird, ist das Element zu groß, um in das Kontextfenster aufgenommen zu werden – selbst in komprimierter Form. So siehst du, welche Teile deiner Codebase für das Modell zugänglich sind.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=06df9854c74c257d1ceb7d18b1864ceb" alt="Context-Menü" data-og-width="1090" width="1090" data-og-height="346" height="346" data-path="images/context/context-management/not-included.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=072e75878f27a151f1310007d0e5e534 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c6f3f71351ddf8e367096651b455bf9d 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c407f7870412007549f8eb2871f9ca12 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b0d17023b5734c8d7584c56f5419bd1a 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f1bedff398cee6c957fe62877f7d2012 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/context-management/not-included.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8b00fbaff658c384f69bfddf3f3a4cfe 2500w" />
</Frame>

---

← Previous: [Verlauf](./verlauf.md) | [Index](./index.md) | Next: [Tabs](./tabs.md) →