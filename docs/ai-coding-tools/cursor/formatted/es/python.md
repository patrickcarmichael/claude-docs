---
title: "Python"
source: "https://docs.cursor.com/es/guides/languages/python"
language: "es"
language_name: "Spanish"
---

# Python
Source: https://docs.cursor.com/es/guides/languages/python

Configura el desarrollo en Python con extensiones y herramientas de linting

<Note>
  Esta guía se inspiró mucho en [Jack Fields](https://x.com/OrdinaryInds)
  y su
  [artículo](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
  sobre cómo configurar VS Code para desarrollar en Python. Échale un vistazo a su artículo para
  más detalles.
</Note>

<div id="prerequisites">
  ## Requisitos previos
</div>

Antes de empezar, asegúrate de tener:

* [Python](https://python.org) instalado (se recomienda 3.8 o superior)
* [Git](https://git-scm.com/) para control de versiones
* Cursor instalado y actualizado a la última versión

<div id="essential-extensions">
  ## Extensiones esenciales
</div>

Las siguientes extensiones configuran Cursor para que quede completamente equipado para el desarrollo en Python. Te ofrecen resaltado de sintaxis, linting, depuración y pruebas unitarias.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Compatibilidad básica del lenguaje por parte de Microsoft
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    Servidor de lenguaje para Python, rápido
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    Capacidades de depuración mejoradas
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Linter y formateador para Python
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### Herramientas avanzadas para Python
</div>

Aunque las extensiones anteriores han sido las más populares para el desarrollo en Python en Cursor, también agregamos algunas adicionales que pueden ayudarte a sacarle el máximo partido a tu desarrollo en Python.

<div id="uv-python-environment-manager">
  #### `uv` - Gestor de entornos de Python
</div>

[uv](https://github.com/astral-sh/uv) es un gestor moderno de paquetes de Python que puede usarse para crear y administrar entornos virtuales, además de reemplazar pip como gestor de paquetes predeterminado.

Para instalar uv, ejecuta el siguiente comando en tu terminal:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Linter y formateador de Python
</div>

[Ruff](https://docs.astral.sh/ruff/) es un linter y formateador moderno para Python que podés usar para detectar errores de programación, hacer cumplir estándares de código y sugerir refactorizaciones. Podés usarlo junto con Black para el formateo del código.

Para instalar Ruff, ejecutá el siguiente comando en tu terminal:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Configuración de Cursor
</div>

<div id="1-python-interpreter">
  ### 1. Intérprete de Python
</div>

Configura tu intérprete de Python en Cursor:

1. Abre la paleta de comandos (Cmd/Ctrl + Shift + P)
2. Busca "Python: Select Interpreter"
3. Elige tu intérprete de Python (o el entorno virtual si estás usando uno)

<div id="2-code-formatting">
  ### 2. Formateo de código
</div>

Configura el formateo automático de código con Black:

<Note>
  Black es un formateador que aplica automáticamente un estilo consistente a tu código.
  No requiere configuración y está ampliamente adoptado en la comunidad de Python.
</Note>

Para instalar Black, ejecuta el siguiente comando en tu terminal:

```bash  theme={null}
pip install black
```

Luego, configura Cursor para usar Black como formateador de código, agregando lo siguiente a tu archivo `settings.json`:

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. Linting
</div>

Podemos usar PyLint para detectar errores de programación, hacer cumplir los estándares de código y sugerir refactorizaciones.

Para instalar PyLint, ejecuta el siguiente comando en tu terminal:

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. Comprobación de tipos
</div>

Además del linting, podemos usar MyPy para verificar errores de tipo.

Para instalar MyPy, ejecuta el siguiente comando en tu terminal:

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## Depuración
</div>

Cursor ofrece potentes funciones de depuración para Python:

1. Colocá puntos de interrupción haciendo clic en el gutter
2. Usá el panel Debug (Cmd/Ctrl + Shift + D)
3. Configurá `launch.json` para definir configuraciones de depuración personalizadas

<div id="recommended-features">
  ## Funciones recomendadas
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/es/tab/overview">
    Sugerencias de código inteligentes que entienden lo que haces
  </Card>

  <Card title="Chat" icon="comments" href="/es/chat/overview">
    Explora y comprende el código mediante conversaciones naturales
  </Card>

  <Card title="Agent" icon="robot" href="/es/chat/agent">
    Resuelve tareas de desarrollo complejas con ayuda de IA
  </Card>

  <Card title="Context" icon="network-wired" href="/es/context/model-context-protocol">
    Trae contexto de sistemas de terceros
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/es/tab/auto-import">
    Importa módulos automáticamente mientras programas
  </Card>

  <Card title="AI Review" icon="check-double" href="/es/tab/overview#quality">
    Cursor revisa tu código constantemente con IA
  </Card>
</CardGroup>

<div id="framework-support">
  ## Compatibilidad con frameworks
</div>

Cursor funciona a la perfección con los frameworks más populares de Python:

* **Frameworks web**: Django, Flask, FastAPI
* **Ciencia de datos**: Jupyter, NumPy, Pandas
* **Aprendizaje automático**: TensorFlow, PyTorch, scikit-learn
* **Pruebas**: pytest, unittest
* **API**: requests, aiohttp
* **Bases de datos**: SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS y macOS (Swift)](./ios-y-macos-swift.md) →