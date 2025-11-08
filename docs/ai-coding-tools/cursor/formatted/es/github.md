---
title: "GitHub"
source: "https://docs.cursor.com/es/integrations/github"
language: "es"
language_name: "Spanish"
---

# GitHub
Source: https://docs.cursor.com/es/integrations/github

App oficial de Cursor para GitHub para agentes en segundo plano

[Background Agents](/es/background-agent) y [Bugbot](/es/bugbot) necesitan la app de GitHub de Cursor para clonar repositorios y enviar cambios.

<div id="installation">
  ## Instalación
</div>

1. Ve a [Integrations in Dashboard](https://cursor.com/dashboard?tab=integrations)
2. Haz clic en **Connect** junto a GitHub
3. Elige entre **All repositories** o **Selected repositories**

Para desconectar tu cuenta de GitHub, vuelve al panel de integraciones y haz clic en **Disconnect Account**.

<div id="using-agent-in-github">
  ## Usar Agent en GitHub
</div>

La integración con GitHub habilita flujos de trabajo de agentes en segundo plano directamente desde pull requests e issues. Podés activar un agente para leer el contexto, aplicar correcciones y hacer push de commits comentando `@cursor [prompt]` en cualquier PR o issue.

Si tenés [Bugbot](/es/bugbot) habilitado, podés comentar `@cursor fix` para leer la corrección sugerida por Bugbot y activar un agente en segundo plano que resuelva el problema.

<div id="permissions">
  ## Permisos
</div>

La app de GitHub requiere permisos específicos para trabajar con agentes en segundo plano:

<div className="full-width-table">
  | Permiso                   | Propósito                                                                  |
  | ------------------------- | -------------------------------------------------------------------------- |
  | **Acceso al repositorio** | Clonar tu código y crear ramas de trabajo                                  |
  | **Pull requests**         | Crear PR con cambios del agente para tu revisión                           |
  | **Issues**                | Hacer seguimiento de errores y tareas que los agentes descubren o corrigen |
  | **Checks and statuses**   | Informar sobre la calidad del código y los resultados de las pruebas       |
  | **Actions and workflows** | Supervisar pipelines de CI/CD y el estado del despliegue                   |
</div>

Todos los permisos siguen el principio de mínimo privilegio necesario para la funcionalidad de los agentes en segundo plano.

<div id="ip-allow-list-configuration">
  ## Configuración de la lista de IP permitidas
</div>

Si tu organización usa la función de lista de IP permitidas de GitHub para restringir el acceso a tus repositorios, primero tienes que contactar al soporte para habilitar esta funcionalidad para tu equipo.

<div id="contact-support">
  ### Contactar al soporte
</div>

Antes de configurar las listas de IP permitidas, contacta a [hi@cursor.com](mailto:hi@cursor.com) para habilitar esta función para tu equipo. Esto es obligatorio para ambos métodos de configuración a continuación.

<div id="enable-ip-allow-list-configuration-for-installed-github-apps-recommended">
  ### Habilitar la configuración de la lista de IP permitidas para las GitHub Apps instaladas (recomendado)
</div>

La app de GitHub de Cursor ya tiene la lista de IP preconfigurada. Puedes habilitar la lista de permitidos para las apps instaladas y heredar automáticamente esta lista. Este es el **enfoque recomendado**, ya que nos permite actualizar la lista y tu organización recibe las actualizaciones automáticamente.

Para habilitar esto:

1. Ve a la configuración de Seguridad de tu organización
2. Ve a la configuración de la lista de IP permitidas
3. Marca **"Allow access by GitHub Apps"**

Para ver instrucciones detalladas, consulta la [documentación de GitHub](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

<div id="add-ips-directly-to-your-allowlist">
  ### Agregar IP directamente a tu lista de permitidos
</div>

Si tu organización usa listas de permitidos definidas por un IdP en GitHub o por algún motivo no puede usar la lista preconfigurada, puedes agregar manualmente las direcciones IP:

```
184.73.225.134
3.209.66.12
52.44.113.131
```

<Note>
  La lista de direcciones IP puede cambiar esporádicamente. A los equipos que usan listas de permitidos de IP se les avisará con anticipación antes de agregar o quitar direcciones IP.
</Note>

<div id="troubleshooting">
  ## Solución de problemas
</div>

<AccordionGroup>
  <Accordion title="El agente no puede acceder al repositorio">
    * Instala la app de GitHub con acceso al repositorio
    * Revisa los permisos del repositorio para repos privados
    * Verifica los permisos de tu cuenta de GitHub
  </Accordion>

  <Accordion title="Permiso denegado para pull requests">
    * Dale a la app acceso de escritura a los pull requests
    * Revisa las reglas de protección de ramas
    * Reinstala si la instalación de la app venció
  </Accordion>

  <Accordion title="La app no aparece en la configuración de GitHub">
    * Revisa si está instalada a nivel de organización
    * Reinstala desde [github.com/apps/cursor](https://github.com/apps/cursor)
    * Contacta al soporte si la instalación está dañada
  </Accordion>
</AccordionGroup>

---

← Previous: [Git](./git.md) | [Index](./index.md) | Next: [Linear](./linear.md) →