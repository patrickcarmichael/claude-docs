---
title: "Java"
source: "https://docs.cursor.com/ko/guides/languages/java"
language: "ko"
language_name: "Korean"
---

# Java
Source: https://docs.cursor.com/ko/guides/languages/java

JDK, 확장 프로그램, 빌드 도구로 Java 개발 환경 설정

이 가이드는 Cursor를 Java 개발에 맞게 설정하는 과정을 다뤄. JDK 설정, 필요한 확장 프로그램 설치, 디버깅, Java 애플리케이션 실행, 그리고 Maven과 Gradle 같은 빌드 도구 연동까지 포함돼. 또 IntelliJ나 VS Code와 유사한 워크플로우 기능도 안내해.

<Note>
  시작하기 전에 Cursor가 설치되어 있고 최신 버전으로 업데이트돼 있는지
  확인해.
</Note>

<div id="setting-up-java-for-cursor">
  ## Cursor에서 Java 설정하기
</div>

<div id="java-installation">
  ### Java 설치
</div>

Cursor를 설정하기 전에, 먼저 컴퓨터에 Java가 설치되어 있어야 해.

<Warning>
  Cursor에는 Java 컴파일러가 포함되어 있지 않아서, 아직 설치하지 않았다면 JDK를 설치해야 해.
</Warning>

<CardGroup cols={1}>
  <Card title="Windows 설치" icon="windows">
    JDK를 다운로드해 설치해 (예: OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    JAVA\_HOME을 설정하고 PATH에 JAVA\_HOME\bin을 추가해.
  </Card>

  <Card title="macOS 설치" icon="apple">
    Homebrew로 설치해 (`brew install openjdk`) 또는 설치 프로그램을 다운로드해.

    <br />

    JAVA\_HOME이 설치된 JDK를 가리키는지 확인해.
  </Card>

  <Card title="Linux 설치" icon="linux">
    패키지 관리자를 사용해 (`sudo apt install openjdk-17-jdk` 또는 이에 준하는 명령)
    혹은 SDKMAN으로 설치해.
  </Card>
</CardGroup>

설치를 확인하려면 다음을 실행해:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Cursor가 JDK를 감지하지 못하면 settings.json에서 직접 설정해:
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

<Warning>변경 사항을 적용하려면 Cursor를 다시 시작해.</Warning>

<div id="cursor-setup">
  ### Cursor 설정
</div>

<Info>Cursor는 VS Code 확장을 지원해. 아래 확장들을 수동으로 설치해:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Java 언어 지원, 디버거, 테스트 러너, Maven 지원, 프로젝트 매니저를 포함해
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Gradle 빌드 시스템 작업에 필수야
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Spring Boot 개발에 필수야
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Kotlin 애플리케이션 개발에 필요해
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### 빌드 도구 구성
</div>

<div id="maven">
  #### Maven
</div>

Maven이 설치되어 있는지 확인해 (`mvn -version`). 필요하면 [maven.apache.org](https://maven.apache.org/download.cgi)에서 설치해:

1. 바이너리 아카이브 다운로드
2. 원하는 위치에 압축 해제
3. 추출한 폴더를 MAVEN\_HOME 환경 변수로 설정
4. PATH에 %MAVEN\_HOME%\bin(Windows) 또는 \$MAVEN\_HOME/bin(Unix) 추가

<div id="gradle">
  #### Gradle
</div>

Gradle이 설치되어 있는지 확인해 (`gradle -version`). 필요하면 [gradle.org](https://gradle.org/install/)에서 설치해:

1. 바이너리 배포판 다운로드
2. 원하는 위치에 압축 해제
3. 추출한 폴더를 GRADLE\_HOME 환경 변수로 설정
4. PATH에 %GRADLE\_HOME%\bin(Windows) 또는 \$GRADLE\_HOME/bin(Unix) 추가

또는 Gradle Wrapper를 쓰면 올바른 Gradle 버전을 자동으로 다운로드해서 사용해:

<div id="running-and-debugging">
  ## 실행 및 디버깅
</div>

이제 설정이 끝났으니, Java 코드를 실행하고 디버깅해 보자.
필요에 따라 아래 방법을 쓸 수 있어:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    main 메서드 위에 나타나는 "Run" 링크를 클릭해 프로그램을 빠르게 실행해
  </Card>

  <Card title="Debug" icon="bug">
    Run and Debug 사이드바 패널을 열고 Run 버튼으로 애플리케이션을 시작해
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    명령줄에서 Maven 또는 Gradle 명령으로 실행해
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Spring Boot Dashboard 확장 프로그램에서 Spring Boot 애플리케이션을 바로 실행해
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Java x Cursor 워크플로우
</div>

Cursor의 AI 기능은 Java 개발 워크플로우를 크게 끌어올려줘. 아래는 Java에 맞춰 Cursor를 활용하는 방법이야:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      메서드, 시그니처, 그리고 getter/setter 같은 Java 보일러플레이트를 위한 스마트 자동완성.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      디자인 패턴 구현, 코드 리팩터링, 올바른 상속 구조를 갖춘 클래스 생성.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      흐름 끊김 없이 메서드 인라인 수정, 오류 수정, 단위 테스트 생성.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Java 개념 도움 받기, 예외 디버깅, 프레임워크 기능 이해하기.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### 예시 워크플로우
</div>

1. **Java 보일러플레이트 생성**\
   [Tab completion](/ko/tab/overview)을 사용해 생성자, getter/setter, equals/hashCode 메서드 등 반복적인 Java 패턴을 빠르게 생성해.

2. **복잡한 Java 예외 디버깅**\
   난해한 Java 스택 트레이스를 마주하면 해당 부분을 강조 표시하고 [Ask](/ko/chat/overview)로 근본 원인 설명과 가능한 해결책을 받아봐.

3. **레거시 Java 코드 리팩터링**\
   [Agent mode](/ko/chat/agent)로 오래된 Java 코드를 현대화해봐 — 익명 클래스를 람다로 바꾸고, 최신 Java 언어 기능으로 업그레이드하거나, 디자인 패턴을 적용해.

4. **프레임워크 개발**\
   @docs로 문서를 Cursor 컨텍스트에 추가하고, Cursor 전반에서 프레임워크 특화 코드를 생성해.

---

← Previous: [문서 활용하기](./section.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →