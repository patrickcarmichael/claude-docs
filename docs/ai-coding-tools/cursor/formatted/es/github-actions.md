---
title: "GitHub Actions"
source: "https://docs.cursor.com/es/cli/github-actions"
language: "es"
language_name: "Spanish"
---

# GitHub Actions
Source: https://docs.cursor.com/es/cli/github-actions

Aprende a usar Cursor CLI en GitHub Actions y otros sistemas de integración continua

Usa Cursor CLI en GitHub Actions y otros sistemas CI/CD para automatizar tareas de desarrollo.

<div id="github-actions-integration">
  ## Integración con GitHub Actions
</div>

Configuración básica:

```yaml  theme={null}
- name: Instalar la CLI de Cursor
  run: |
    curl https://cursor.com/install -fsS | bash
    echo "$HOME/.cursor/bin" >> $GITHUB_PATH

- name: Ejecutar Cursor Agent
  env:
    CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  run: |
    cursor-agent -p "Escribe tu prompt aquí" --model gpt-5
```

<div id="cookbook-examples">
  ## Ejemplos de cookbook
</div>

Mira nuestros ejemplos de cookbook para flujos de trabajo prácticos: [actualizar documentación](/es/cli/cookbook/update-docs) y [corregir problemas de CI](/es/cli/cookbook/fix-ci).

<div id="other-ci-systems">
  ## Otros sistemas de CI
</div>

Usa Cursor CLI en cualquier sistema de CI/CD con:

* **Ejecución de scripts de shell** (bash, zsh, etc.)
* **Variables de entorno** para configurar la clave de API
* **Conexión a Internet** para acceder a la API de Cursor

<div id="autonomy-levels">
  ## Niveles de autonomía
</div>

Elige el nivel de autonomía de tu agente:

<div id="full-autonomy-approach">
  ### Enfoque de autonomía total
</div>

Dale al agente control completo sobre operaciones de Git, llamadas a APIs e interacciones externas. Configuración más simple; requiere más confianza.

**Ejemplo:** En nuestro cookbook [Update Documentation](/es/cli/cookbook/update-docs), el primer flujo de trabajo permite que el agente:

* Analice los cambios del PR
* Cree y administre ramas de Git
* Haga commits y haga push de cambios
* Publique comentarios en pull requests
* Maneje todos los escenarios de error

```yaml  theme={null}
- name: Actualizar docs (autonomía total)
  run: |
    cursor-agent -p "Tienes acceso completo a git, la CLI de GitHub y a las operaciones de PR. 
    Ocúpate de todo el flujo de actualización de la documentación, incluidos los commits, los pushes y los comentarios en PR."
```

<div id="restricted-autonomy-approach">
  ### Enfoque de autonomía restringida
</div>

<Note>
  Recomendamos usar este enfoque con **restricciones basadas en permisos** para flujos de trabajo de CI en producción. Te da lo mejor de ambos mundos: el agente puede manejar de forma inteligente análisis complejos y modificaciones de archivos, mientras que las operaciones críticas siguen siendo deterministas y auditables.
</Note>

Limita las operaciones del agente y mueve los pasos críticos a etapas separadas del flujo de trabajo. Mejor control y previsibilidad.

**Ejemplo:** El segundo flujo de trabajo de este mismo cookbook restringe al agente únicamente a realizar modificaciones de archivos:

```yaml  theme={null}
- name: Generar actualizaciones de docs (restringido)
  run: |
    cursor-agent -p "IMPORTANTE: NO crees ramas, no hagas commit ni push, ni publiques comentarios en PR. 
    Modifica únicamente los archivos en el directorio de trabajo. Un paso posterior del flujo se encarga de la publicación."

- name: Publicar rama de docs (determinista)
  run: |
    # Operaciones deterministas de git gestionadas por CI
    git checkout -B "docs/${{ github.head_ref }}"
    git add -A
    git commit -m "docs: actualización para PR"
    git push origin "docs/${{ github.head_ref }}"

- name: Publicar comentario en PR (determinista)  
  run: |
    # Comentarios de PR deterministas gestionados por CI
    gh pr comment ${{ github.event.pull_request.number }} --body "Docs actualizados"
```

<div id="permission-based-restrictions">
  ### Restricciones basadas en permisos
</div>

Usa las [configuraciones de permisos](/es/cli/reference/permissions) para imponer restricciones a nivel de la CLI:

```json  theme={null}
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Write(docs/**/*)",
      "Shell(grep)",
      "Shell(find)"
    ],
    "deny": [
      "Shell(git)",
      "Shell(gh)", 
      "Write(.env*)",
      "Write(package.json)"
    ]
  }
}
```

<div id="authentication">
  ## Autenticación
</div>

<div id="generate-your-api-key">
  ### Genera tu clave de API
</div>

Primero, [genera una clave de API](/es/cli/reference/authentication#api-key-authentication) desde tu panel de Cursor.

<div id="configure-repository-secrets">
  ### Configura los secretos del repositorio
</div>

Guarda tu clave de API de Cursor de forma segura en tu repositorio:

1. Ve a tu repositorio de GitHub
2. Haz clic en **Settings** → **Secrets and variables** → **Actions**
3. Haz clic en **New repository secret**
4. Ponle el nombre `CURSOR_API_KEY`
5. Pega tu clave de API como valor
6. Haz clic en **Add secret**

<div id="use-in-workflows">
  ### Úsala en workflows
</div>

Configura tu variable de entorno `CURSOR_API_KEY`:

```yaml  theme={null}
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
```

---

← Previous: [Actualizar docs](./actualizar-docs.md) | [Index](./index.md) | Next: [Uso de la CLI en modo headless](./uso-de-la-cli-en-modo-headless.md) →