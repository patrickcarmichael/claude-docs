---
title: "Java"
source: "https://docs.cursor.com/en/guides/languages/java"
language: "en"
language_name: "English"
---

# Java
Source: https://docs.cursor.com/en/guides/languages/java

Set up Java development with JDK, extensions, and build tools

This guide will help you configure Cursor for Java development, including setting up the JDK, installing necessary extensions, debugging, running Java applications, and integrating build tools like Maven and Gradle. It also covers workflow features similar to IntelliJ or VS Code.

<Note>
  Before starting, ensure you have Cursor installed and updated to the latest
  version.
</Note>

## Setting up Java for Cursor

### Java Installation

Before setting up Cursor itself, you will need Java installed on your machine.

<Warning>
  Cursor does not ship with a Java compiler, so you need to install a JDK if you
  haven't already.
</Warning>

<CardGroup cols={1}>
  <Card title="Windows Installation" icon="windows">
    Download and install a JDK (e.g., OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    Set JAVA\_HOME and add JAVA\_HOME\bin to your PATH.
  </Card>

  <Card title="macOS Installation" icon="apple">
    Install via Homebrew (`brew install openjdk`) or download an installer.

    <br />

    Ensure JAVA\_HOME points to the installed JDK.
  </Card>

  <Card title="Linux Installation" icon="linux">
    Use your package manager (`sudo apt install openjdk-17-jdk` or equivalent)
    or install via SDKMAN.
  </Card>
</CardGroup>

To check installation, run:

```bash  theme={null}
java -version
javac -version
```

<Info>
  If Cursor does not detect your JDK, configure it manually in settings.json:
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

<Warning>Restart Cursor to apply changes.</Warning>

### Cursor Setup

<Info>Cursor supports VS Code extensions. Install the following manually:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Includes Java language support, debugger, test runner, Maven support, and
    project manager
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Essential for working with Gradle build system
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Required for Spring Boot development
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Necessary for Kotlin application development
  </Card>
</CardGroup>

### Configure Build Tools

#### Maven

Ensure Maven is installed (`mvn -version`). Install from [maven.apache.org](https://maven.apache.org/download.cgi) if needed:

1. Download the binary archive
2. Extract to desired location
3. Set MAVEN\_HOME environment variable to the extracted folder
4. Add %MAVEN\_HOME%\bin (Windows) or \$MAVEN\_HOME/bin (Unix) to PATH

#### Gradle

Ensure Gradle is installed (`gradle -version`). Install from [gradle.org](https://gradle.org/install/) if needed:

1. Download the binary distribution
2. Extract to desired location
3. Set GRADLE\_HOME environment variable to the extracted folder
4. Add %GRADLE\_HOME%\bin (Windows) or \$GRADLE\_HOME/bin (Unix) to PATH

Alternatively, use the Gradle Wrapper which will automatically download and use the correct Gradle version:

## Running and Debugging

Now you are all set up, it's time to run and debug your Java code.
Depending on your needs, you can use the following methods:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Click the "Run" link that appears above any main method to quickly execute
    your program
  </Card>

  <Card title="Debug" icon="bug">
    Open the Run and Debug sidebar panel and use the Run button to start your
    application
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Execute from command line using Maven or Gradlecommands
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Launch Spring Boot applications directly from the Spring Boot Dashboard
    extension
  </Card>
</CardGroup>

## Java x Cursor Workflow

Cursor's AI-powered features can significantly enhance your Java development workflow. Here are some ways to leverage Cursor's capabilities specifically for Java:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      Smart completions for methods, signatures, and Java boilerplate like
      getters/setters.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Implement design patterns, refactor code, or generate classes with proper
      inheritance.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      Quick inline edits to methods, fix errors, or generate unit tests without
      breaking flow.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Get help with Java concepts, debug exceptions, or understand framework
      features.
    </div>
  </Card>
</CardGroup>

### Example Workflows

1. **Generate Java Boilerplate**\
   Use [Tab completion](/en/tab/overview) to quickly generate constructors, getters/setters, equals/hashCode methods, and other repetitive Java patterns.

2. **Debug Complex Java Exceptions**\
   When facing a cryptic Java stack trace, highlight it and use [Ask](/en/chat/overview) to explain the root cause and suggest potential fixes.

3. **Refactor Legacy Java Code**\
   Use [Agent mode](/en/chat/agent) to modernize older Java code - convert anonymous classes to lambdas, upgrade to newer Java language features, or implement design patterns.

4. **Frameworks Development**\
   Add your documentation to Cursor's context with @docs, and generate framework-specific code throughout Cursor.

---

← Previous: [Working with Documentation](./working-with-documentation.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →