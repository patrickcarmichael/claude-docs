---
title: "iOS y macOS (Swift)"
source: "https://docs.cursor.com/es/guides/languages/swift"
language: "es"
language_name: "Spanish"
---

# iOS y macOS (Swift)
Source: https://docs.cursor.com/es/guides/languages/swift

Integra Cursor con Xcode para desarrollo en Swift

¡Bienvenido al desarrollo de Swift en Cursor! Ya sea que estés creando apps para iOS, aplicaciones para macOS o proyectos de Swift del lado del servidor, te tenemos cubierto. Esta guía te ayudará a configurar tu entorno de Swift en Cursor, empezando por lo básico y pasando a funciones más avanzadas.

<div id="basic-workflow">
  ## Flujo de trabajo básico
</div>

La forma más sencilla de usar Cursor con Swift es tratarlo como tu editor de código principal y seguir usando Xcode para compilar y ejecutar tus apps. Vas a obtener funciones geniales como:

* Autocompletado inteligente de código
* Asistencia de código con IA (prueba [CMD+K](/es/inline-edit/overview) en cualquier línea)
* Acceso rápido a la documentación con [@Docs](/es/context/@-symbols/@-docs)
* Resaltado de sintaxis
* Navegación básica de código

Cuando necesites compilar o ejecutar tu app, simplemente cambia a Xcode. Este flujo de trabajo es perfecto para desarrolladores que quieren aprovechar las capacidades de IA de Cursor mientras se quedan con las herramientas conocidas de Xcode para depuración y distribución.

<div id="hot-reloading">
  ### Recarga en caliente
</div>

Cuando usas workspaces o proyectos de Xcode (en lugar de abrir una carpeta directamente en Xcode), Xcode a menudo puede ignorar cambios en tus archivos que se hicieron en Cursor, o fuera de Xcode en general.

Aunque puedes abrir la carpeta en Xcode para resolver esto, puede que necesites usar un proyecto para tu flujo de trabajo de desarrollo en Swift.

Una gran solución es usar [Inject](https://github.com/krzysztofzablocki/Inject), una librería de recarga en caliente para Swift que permite que tu app haga “hot reload” y se actualice en cuanto detecta cambios, en tiempo real. Esto no sufre los efectos secundarios del problema de los workspaces/proyectos de Xcode y te permite hacer cambios en Cursor y verlos reflejados en tu app al instante.

<CardGroup cols={1}>
  <Card title="Inject - Recarga en caliente para Swift" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Aprende más sobre Inject y cómo usarlo en tus proyectos Swift.
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## Desarrollo avanzado con Swift
</div>

<Note>
  Esta sección de la guía está muy inspirada en [Thomas
  Ricouard](https://x.com/Dimillian) y su
  [artículo](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  sobre cómo usar Cursor para desarrollo en iOS. Échale un ojo a su artículo para más
  detalles y síguelo para más contenido sobre Swift.
</Note>

Si quieres tener solo un editor abierto a la vez y evitar cambiar entre Xcode y Cursor, puedes usar una extensión como [Sweetpad](https://sweetpad.hyzyla.dev/) para integrar Cursor directamente con el sistema de compilación de Xcode.

Sweetpad es una extensión potente que te permite compilar, ejecutar y depurar tus proyectos Swift directamente en Cursor, sin renunciar a las funcionalidades de Xcode.

Para empezar con Sweetpad, aún necesitas tener Xcode instalado en tu Mac: es la base del desarrollo con Swift. Puedes descargar Xcode desde la [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835). Una vez que tengas Xcode configurado, vamos a potenciar tu experiencia de desarrollo en Cursor con algunas herramientas esenciales.

Abre tu terminal y ejecuta:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →