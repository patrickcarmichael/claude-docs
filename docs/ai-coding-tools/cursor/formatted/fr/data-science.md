---
title: "Data Science"
source: "https://docs.cursor.com/fr/guides/advanced/datascience"
language: "fr"
language_name: "French"
---

# Data Science
Source: https://docs.cursor.com/fr/guides/advanced/datascience

Découvre comment configurer Cursor pour des workflows de data science, incluant Python, R et SQL, avec des notebooks, des environnements distants et des analyses propulsées par l’IA

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Cursor fournit des outils intégrés pour le développement en data science, avec des environnements reproductibles, la prise en charge des notebooks et une assistance au code propulsée par l’IA. Ce guide présente les configurations essentielles pour les workflows Python, R et SQL.

<div id="notebook-development">
  ## Développement de notebooks
</div>

<Note>
  Pour une prise en charge complète des notebooks, télécharge l’extension Jupyter (id : ms-toolsai.jupyter), publiée par ms-toolsai.
</Note>

Cursor prend en charge les fichiers `.ipynb` et `.py` avec exécution de cellules intégrée. Tab, Inline Edit et Agents
fonctionnent dans les notebooks, comme dans les autres fichiers de code.

Fonctionnalités clés :

* **L’exécution de cellules en ligne** lance le code directement dans l’interface de l’éditeur
* **Tab, Inline Edit et Agent** comprennent les bibliothèques de data science, notamment pandas, NumPy, scikit-learn, ainsi que les commandes magiques SQL

<div id="database-integration">
  ## Intégration des bases de données
</div>

Les bases de données peuvent être intégrées à Cursor via deux mécanismes principaux : les serveurs MCP et les extensions.

* Les **serveurs MCP** permettent à tes agents de se connecter à tes bases de données
* Les **extensions** intègrent ton IDE au sens large avec tes bases de données

<div id="via-mcp">
  ### Via MCP
</div>

Les serveurs MCP permettent à ton agent d’exécuter des requêtes directement sur ta base de données. Ça permet à ton agent de choisir d’interroger la base, d’écrire la requête appropriée, d’exécuter la commande et d’analyser les résultats, le tout dans le cadre d’une tâche en cours.

Par exemple, tu peux connecter une base de données Postgres à ton instance Cursor en ajoutant la [config MCP](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) suivante à Cursor :

```json  theme={null}
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/ma_bdd"
      ]
    }
  }
}
```

Pour en savoir plus sur MCP, consulte notre [documentation MCP](/fr/tools/mcp).

<Frame>
  <video autoPlay loop muted playsInline controls width="100%">
    <source src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/postgres-mcp.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=334439f58b7d88b16d97134cf9c147aa" type="video/mp4" data-path="images/guides/advanced/datascience/postgres-mcp.mp4" />

    Ton navigateur ne prend pas en charge la balise vidéo.
  </video>
</Frame>

<div id="via-extensions">
  ### Via des extensions
</div>

Installe des extensions spécifiques aux bases de données (PostgreSQL, BigQuery, SQLite, Snowflake) pour exécuter des requêtes directement depuis l’éditeur. Ça évite de jongler entre les outils et permet à l’IA d’aider à optimiser tes requêtes.

```sql  theme={null}
-- Cursor suggère des index, des fonctions de fenêtre et des optimisations de requêtes
SELECT
    user_id,
    event_type,
    COUNT(*) AS nombre_d’événements,
    RANK() OVER (PARTITION BY user_id ORDER BY COUNT(*) DESC) AS rang_de_fréquence
FROM events
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY user_id, event_type;
```

Utilise les Agents pour analyser des requêtes lentes, proposer des optimisations de performance ou générer du code de visualisation pour les résultats. Cursor comprend le contexte SQL et peut recommander des types de graphiques adaptés à ta structure de données.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7c14c60dc3c0523fb565c9462ac49029" alt="Extension Snowflake" data-og-width="2324" width="2324" data-og-height="1602" height="1602" data-path="images/guides/advanced/datascience/snowflake-extension.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8f316c0a5e756aed89423082dfa11d8 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=a8a66623964651cac9182159d880a511 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2dc2566fa81d26a920d681178cb1d209 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=52c3a74cea69f812e869c2bc25457462 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d3322864e752c413fb3bfb2b686136f3 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/guides/advanced/datascience/snowflake-extension.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9ee01c8736f8eb78a04aab6340c4eaae 2500w" />
</Frame>

<div id="data-visualization">
  ## Visualisation de données
</div>

L’assistant IA de Cursor fonctionne avec des bibliothèques de visualisation comme Matplotlib, Plotly et Seaborn. L’agent peut générer du code de visualisation pour t’aider à explorer rapidement tes données, tout en créant un artefact reproductible et partageable.

```python  theme={null}
import plotly.express as px
import pandas as pd

---

← Previous: [Démarrage rapide](./dmarrage-rapide.md) | [Index](./index.md) | Next: [Grandes bases de code](./grandes-bases-de-code.md) →