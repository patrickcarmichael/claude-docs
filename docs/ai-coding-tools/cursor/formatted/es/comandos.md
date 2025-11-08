---
title: "Comandos"
source: "https://docs.cursor.com/es/agent/chat/commands"
language: "es"
language_name: "Spanish"
---

# Comandos
Source: https://docs.cursor.com/es/agent/chat/commands

Define comandos para flujos de trabajo reutilizables

Los comandos personalizados te permiten crear flujos de trabajo reutilizables que se pueden activar con un simple prefijo `/` en el cuadro de entrada del chat. Estos comandos ayudan a estandarizar procesos en tu equipo y hacen más eficientes las tareas comunes.

<Frame>
    <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=0d25ac517b091210da1c6eff4c8e3098" alt="Commands input example" data-og-width="1689" width="1689" data-og-height="1079" height="1079" data-path="images/chat/commands/input.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=680f0cbf1491ef1303171dbd18115288 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d6a5397e565ab2c90435e6fdd2b7b27a 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ae074e2f2b26741544fd8c8ecfa529e3 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=564aad432affcc04e51b624725f386ad 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5c1bd5d49babc2f08eb0efcd24ba7783 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/chat/commands/input.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3244c3be31c9bc704468a706c6e6b38e 2500w" />
</Frame>

<Info>
  Los comandos están actualmente en versión beta. La función y la sintaxis pueden cambiar a medida que seguimos mejorándola.
</Info>

<div id="how-commands-work">
  ## Cómo funcionan los comandos
</div>

Los comandos se definen como archivos Markdown de texto plano que se pueden guardar en dos ubicaciones:

1. **Comandos del proyecto**: almacenados en el directorio `.cursor/commands` de tu proyecto
2. **Comandos globales**: almacenados en el directorio `~/.cursor/commands` de tu directorio de inicio

Cuando escribes `/` en el cuadro de entrada del chat, Cursor detecta y muestra automáticamente los comandos disponibles de ambos directorios, haciéndolos accesibles al instante en todo tu flujo de trabajo.

<div id="creating-commands">
  ## Creación de comandos
</div>

1. Crea un directorio `.cursor/commands` en la raíz de tu proyecto
2. Añade archivos `.md` con nombres descriptivos (p. ej., `review-code.md`, `write-tests.md`)
3. Escribe contenido en Markdown sencillo que describa lo que debe hacer el comando
4. Los comandos aparecerán automáticamente en el chat cuando escribas `/`

Aquí tienes un ejemplo de cómo podría verse la estructura de tu directorio de comandos:

```
.cursor/
└── commands/
    ├── atender-comentarios-de-pr-de-github.md
    ├── lista-de-verificación-para-revisión-de-código.md
    ├── crear-pr.md
    ├── revisión-ligera-de-diffs-existentes.md
    ├── incorporación-de-nuevo-desarrollador.md
    ├── ejecutar-todas-las-pruebas-y-corregir.md
    ├── auditoría-de-seguridad.md
    └── configurar-nueva-función.md
```

<div id="examples">
  ## Ejemplos
</div>

Prueba estos comandos en tus proyectos para hacerte una idea de cómo funcionan.

<AccordionGroup>
  <Accordion title="Lista de verificación para revisión de código">
    ```markdown  theme={null}
    # Lista de verificación para revisión de código

    ## Descripción general
    Lista de verificación completa para realizar revisiones de código exhaustivas y garantizar calidad, seguridad y mantenibilidad.

    ## Categorías de revisión

    ### Funcionalidad
    - [ ] El código hace lo que debe
    - [ ] Se contemplan los casos límite
    - [ ] El manejo de errores es adecuado
    - [ ] No hay errores obvios ni fallos de lógica

    ### Calidad del código
    - [ ] El código es legible y está bien estructurado
    - [ ] Las funciones son pequeñas y enfocadas
    - [ ] Los nombres de variables son descriptivos
    - [ ] No hay duplicación de código
    - [ ] Sigue las convenciones del proyecto

    ### Seguridad
    - [ ] No hay vulnerabilidades de seguridad evidentes
    - [ ] Hay validación de entradas
    - [ ] Los datos sensibles se manejan correctamente
    - [ ] No hay secretos codificados en duro
    ```
  </Accordion>

  <Accordion title="Auditoría de seguridad">
    ```markdown  theme={null}
    # Auditoría de seguridad

    ## Descripción general
    Revisión de seguridad integral para identificar y corregir vulnerabilidades en la base de código.

    ## Pasos
    1. **Auditoría de dependencias**
       - Detectar vulnerabilidades conocidas
       - Actualizar paquetes desactualizados
       - Revisar dependencias de terceros

    2. **Revisión de seguridad del código**
       - Detectar vulnerabilidades comunes
       - Revisar autenticación/autorización
       - Auditar prácticas de manejo de datos

    3. **Seguridad de la infraestructura**
       - Revisar variables de entorno
       - Verificar controles de acceso
       - Auditar la seguridad de la red

    ## Lista de verificación de seguridad
    - [ ] Dependencias actualizadas y seguras
    - [ ] Sin secretos hardcodeados
    - [ ] Validación de entradas implementada
    - [ ] Autenticación segura
    - [ ] Autorización configurada correctamente
    ```
  </Accordion>

  <Accordion title="Configurar nueva función">
    ```markdown  theme={null}
    # Configurar nueva feature

    ## Descripción general
    Configura sistemáticamente una nueva feature, desde la planificación inicial hasta la estructura de implementación.

    ## Pasos
    1. **Definir requisitos**
       - Aclarar el alcance y los objetivos de la feature
       - Identificar historias de usuario y criterios de aceptación
       - Planificar el enfoque técnico

    2. **Crear rama de la feature**
       - Ramificar desde main/develop
       - Configurar el entorno de desarrollo local
       - Configurar cualquier dependencia nueva

    3. **Planificar la arquitectura**
       - Diseñar modelos de datos y APIs
       - Planificar componentes de UI y flujos
       - Definir la estrategia de testing

    ## Checklist de configuración de la feature
    - [ ] Requisitos documentados
    - [ ] Historias de usuario redactadas
    - [ ] Enfoque técnico definido
    - [ ] Rama de la feature creada
    - [ ] Entorno de desarrollo listo
    ```
  </Accordion>

  <Accordion title="Crear pull request">
    ```markdown  theme={null}
    # Crear PR

    ## Descripción general
    Crea un pull request bien estructurado con una descripción clara, etiquetas y revisores.

    ## Pasos
    1. **Preparar la rama**
       - Asegúrate de que todos los cambios estén confirmados
       - Envía la rama al remoto
       - Verifica que la rama esté actualizada con main

    2. **Escribir la descripción del PR**
       - Resume los cambios de forma clara
       - Incluye contexto y motivación
       - Enumera cualquier cambio incompatible
       - Agrega capturas de pantalla si hay cambios en la UI

    3. **Configurar el PR**
       - Crea el PR con un título descriptivo
       - Agrega etiquetas adecuadas
       - Asigna revisores
       - Vincula issues relacionados

    ## Plantilla de PR
    - [ ] Funcionalidad A
    - [ ] Corrección de bug B
    - [ ] Pruebas unitarias aprobadas
    - [ ] Pruebas manuales completadas
    ```
  </Accordion>

  <Accordion title="Ejecuta las pruebas y corrige los fallos">
    ```markdown  theme={null}
    # Ejecuta todas las pruebas y corrige los errores

    ## Descripción general
    Ejecuta toda la batería de pruebas y corrige de forma sistemática cualquier error, garantizando la calidad y la funcionalidad del código.

    ## Pasos
    1. **Ejecuta la batería de pruebas**
       - Ejecuta todas las pruebas del proyecto
       - Captura la salida e identifica los errores
       - Revisa tanto las pruebas unitarias como las de integración

    2. **Analiza los errores**
       - Clasifícalos por tipo: intermitentes, rotos, nuevos
       - Prioriza las correcciones según el impacto
       - Revisa si los errores están relacionados con cambios recientes

    3. **Corrige los problemas de forma sistemática**
       - Empieza por los errores más críticos
       - Corrige un problema a la vez
       - Vuelve a ejecutar las pruebas después de cada corrección
    ```
  </Accordion>

  <Accordion title="Incorporar a un nuevo developer">
    ```markdown  theme={null}
    # Incorporar a un nuevo developer

    ## Descripción general
    Proceso completo de onboarding para que un developer nuevo arranque y quede listo rápido.

    ## Pasos
    1. **Configuración del entorno**
       - Instalar las herramientas requeridas
       - Configurar el entorno de desarrollo
       - Configurar el IDE y las extensiones
       - Configurar git y las claves SSH

    2. **Familiarización con el proyecto**
       - Revisar la estructura del proyecto
       - Entender la arquitectura
       - Leer la documentación clave
       - Configurar la base de datos local

    ## Lista de verificación de onboarding
    - [ ] Entorno de desarrollo listo
    - [ ] Todas las pruebas pasando
    - [ ] Puedes ejecutar la app localmente
    - [ ] Base de datos configurada y funcionando
    - [ ] Primer PR enviado
    ```
  </Accordion>
</AccordionGroup>

---

← Previous: [Checkpoints](./checkpoints.md) | [Index](./index.md) | Next: [Compacto](./compacto.md) →