---
title: "Java"
source: "https://docs.cursor.com/es/guides/languages/java"
language: "es"
language_name: "Spanish"
---

# Java
Source: https://docs.cursor.com/es/guides/languages/java

Configura el desarrollo en Java con el JDK, extensiones y herramientas de build

Esta guía te ayuda a configurar Cursor para desarrollar en Java: preparar el JDK, instalar extensiones necesarias, depurar, ejecutar aplicaciones Java e integrar herramientas de build como Maven y Gradle. También cubre funciones de flujo de trabajo similares a IntelliJ o VS Code.

<Note>
  Antes de empezar, asegúrate de tener Cursor instalado y actualizado a la última versión.
</Note>

<div id="setting-up-java-for-cursor">
  ## Configurar Java para Cursor
</div>

<div id="java-installation">
  ### Instalación de Java
</div>

Antes de configurar Cursor, necesitas tener Java instalado en tu equipo.

<Warning>
  Cursor no incluye un compilador de Java, así que necesitas instalar un JDK si
  aún no lo tienes.
</Warning>

<CardGroup cols={1}>
  <Card title="Instalación en Windows" icon="windows">
    Descarga e instala un JDK (p. ej., OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    Configura JAVA\_HOME y agrega JAVA\_HOME\bin a tu PATH.
  </Card>

  <Card title="Instalación en macOS" icon="apple">
    Instala con Homebrew (`brew install openjdk`) o descarga un instalador.

    <br />

    Asegúrate de que JAVA\_HOME apunte al JDK instalado.
  </Card>

  <Card title="Instalación en Linux" icon="linux">
    Usa tu gestor de paquetes (`sudo apt install openjdk-17-jdk` o equivalente)
    o instala con SDKMAN.
  </Card>
</CardGroup>

Para comprobar la instalación, ejecuta:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Si Cursor no detecta tu JDK, configúralo manualmente en settings.json:
</Info>

```json  theme={null}
{
  "java.jdt.ls.java.home": "/path/to/jdk",
  "java.configuration.runtimes": [
    {
      "name": "JavaSE-17",
      "path": "/path/to/jdk-17",
      "default": true
    }
  ]
}
```

<Warning>Reinicia Cursor para aplicar los cambios.</Warning>

<div id="cursor-setup">
  ### Configuración de Cursor
</div>

<Info>Cursor es compatible con extensiones de VS Code. Instala las siguientes manualmente:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Incluye soporte para el lenguaje Java, depurador, ejecutor de pruebas, soporte para Maven y
    administrador de proyectos
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Esencial para trabajar con el sistema de compilación Gradle
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Requisito para el desarrollo con Spring Boot
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Necesario para el desarrollo de aplicaciones en Kotlin
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### Configurar herramientas de compilación
</div>

<div id="maven">
  #### Maven
</div>

Asegúrate de que Maven esté instalado (`mvn -version`). Instálalo desde [maven.apache.org](https://maven.apache.org/download.cgi) si es necesario:

1. Descarga el archivo binario
2. Extráelo en la ubicación deseada
3. Configura la variable de entorno MAVEN\_HOME al directorio extraído
4. Agrega %MAVEN\_HOME%\bin (Windows) o \$MAVEN\_HOME/bin (Unix) al PATH

<div id="gradle">
  #### Gradle
</div>

Asegúrate de que Gradle esté instalado (`gradle -version`). Instálalo desde [gradle.org](https://gradle.org/install/) si es necesario:

1. Descarga la distribución binaria
2. Extráela en la ubicación deseada
3. Configura la variable de entorno GRADLE\_HOME al directorio extraído
4. Agrega %GRADLE\_HOME%\bin (Windows) o \$GRADLE\_HOME/bin (Unix) al PATH

Como alternativa, usa el Gradle Wrapper, que descargará y usará automáticamente la versión correcta de Gradle:

<div id="running-and-debugging">
  ## Ejecución y depuración
</div>

Ahora que ya está todo listo, es momento de ejecutar y depurar tu código Java.
Según lo que necesites, podés usar los siguientes métodos:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Hacé clic en el enlace "Run" que aparece sobre cualquier método main para ejecutar
    tu programa rápidamente
  </Card>

  <Card title="Debug" icon="bug">
    Abrí el panel lateral "Run and Debug" y usá el botón "Run" para iniciar tu
    aplicación
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Ejecutá desde la línea de comandos usando Maven o Gradle
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Iniciá aplicaciones Spring Boot directamente desde la extensión "Spring Boot Dashboard"
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Flujo de trabajo de Java x Cursor
</div>

Las funciones con IA de Cursor pueden mejorar significativamente tu flujo de trabajo de desarrollo en Java. Aquí tienes algunas formas de aprovechar las capacidades de Cursor específicamente para Java:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      Completado inteligente para métodos, firmas y boilerplate de Java como
      getters/setters.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Implementa patrones de diseño, refactoriza código o genera clases con
      la herencia adecuada.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      Ediciones rápidas en línea en métodos, corrige errores o genera pruebas unitarias sin
      romper el flujo.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Obtén ayuda con conceptos de Java, depura excepciones o comprende características de
      frameworks.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### Flujos de trabajo de ejemplo
</div>

1. **Generar boilerplate de Java**\
   Usa [Tab completion](/es/tab/overview) para generar rápidamente constructores, getters/setters, métodos equals/hashCode y otros patrones repetitivos de Java.

2. **Depurar excepciones complejas de Java**\
   Cuando te encuentres con un stack trace críptico de Java, selecciónalo y usa [Ask](/es/chat/overview) para explicar la causa raíz y sugerir posibles soluciones.

3. **Refactorizar código legado de Java**\
   Usa [Agent mode](/es/chat/agent) para modernizar código antiguo de Java: convierte clases anónimas en lambdas, actualiza a nuevas características del lenguaje Java o implementa patrones de diseño.

4. **Desarrollo con frameworks**\
   Agrega tu documentación al contexto de Cursor con @docs y genera código específico del framework en todo Cursor.

---

← Previous: [Trabajar con la documentación](./trabajar-con-la-documentacin.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →