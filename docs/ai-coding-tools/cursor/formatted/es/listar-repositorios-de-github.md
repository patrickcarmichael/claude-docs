---
title: "Listar repositorios de GitHub"
source: "https://docs.cursor.com/es/background-agent/api/list-repositories"
language: "es"
language_name: "Spanish"
---

# Listar repositorios de GitHub
Source: https://docs.cursor.com/es/background-agent/api/list-repositories

en/background-agent/api/openapi.yaml get /v0/repositories
Obtén una lista de repositorios de GitHub a los que tiene acceso el usuario autenticado.

<Warning>
  **Este endpoint tiene límites de tasa muy estrictos.**

  Limita las solicitudes a **1/usuario/minuto** y **30/usuario/hora**.

  Esta solicitud puede tardar decenas de segundos en responder para usuarios con acceso a muchos repositorios.

  Asegúrate de manejar correctamente cuando esta información no esté disponible.
</Warning>

---

← Previous: [Listar modelos](./listar-modelos.md) | [Index](./index.md) | Next: [Descripción general](./descripcin-general.md) →