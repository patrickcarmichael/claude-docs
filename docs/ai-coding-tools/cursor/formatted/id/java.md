---
title: "Java"
source: "https://docs.cursor.com/id/guides/languages/java"
language: "id"
language_name: "Indonesian"
---

# Java
Source: https://docs.cursor.com/id/guides/languages/java

Menyiapkan pengembangan Java dengan JDK, ekstensi, dan alat build

Panduan ini bantu lo ngonfigurasi Cursor buat pengembangan Java, termasuk nyiapin JDK, install ekstensi yang diperlukan, debugging, ngejalanin aplikasi Java, dan integrasi alat build kayak Maven dan Gradle. Panduan ini juga ngebahas fitur alur kerja yang mirip IntelliJ atau VS Code.

<Note>
  Sebelum mulai, pastiin lo udah install Cursor dan update ke versi terbaru.
</Note>

<div id="setting-up-java-for-cursor">
  ## Menyiapkan Java untuk Cursor
</div>

<div id="java-installation">
  ### Instalasi Java
</div>

Sebelum menyiapkan Cursor, kamu perlu punya Java terpasang di mesinmu.

<Warning>
  Cursor nggak menyertakan kompiler Java, jadi kamu perlu menginstal JDK kalau
  belum ada.
</Warning>

<CardGroup cols={1}>
  <Card title="Instalasi Windows" icon="windows">
    Unduh dan instal JDK (misalnya OpenJDK, Oracle JDK, Microsoft Build of
    OpenJDK).

    <br />

    Setel JAVA\_HOME dan tambahkan JAVA\_HOME\bin ke PATH kamu.
  </Card>

  <Card title="Instalasi macOS" icon="apple">
    Instal via Homebrew (`brew install openjdk`) atau unduh installer.

    <br />

    Pastikan JAVA\_HOME mengarah ke JDK yang terpasang.
  </Card>

  <Card title="Instalasi Linux" icon="linux">
    Pakai manajer paket kamu (`sudo apt install openjdk-17-jdk` atau yang setara)
    atau instal via SDKMAN.
  </Card>
</CardGroup>

Untuk mengecek instalasi, jalankan:

```bash  theme={null}
java -version
javac -version
```

<Info>
  Kalau Cursor nggak mendeteksi JDK kamu, atur sendiri di settings.json:
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

<Warning>Restart Cursor untuk menerapkan perubahan.</Warning>

<div id="cursor-setup">
  ### Penyiapan Cursor
</div>

<Info>Cursor mendukung ekstensi VS Code. Instal yang berikut ini secara manual:</Info>

<CardGroup cols={2}>
  <Card title="Extension Pack for Java" icon="java" href="cursor:extension/vscjava.vscode-java-pack">
    Mencakup dukungan bahasa Java, debugger, test runner, dukungan Maven, dan
    manajer proyek
  </Card>

  <Card title="Gradle for Java" icon="gears" href="cursor:extension/vscjava.vscode-gradle">
    Penting untuk bekerja dengan sistem build Gradle
  </Card>

  <Card title="Spring Boot Extension Pack" icon="leaf" href="cursor:extension/vmware.vscode-boot-dev-pack">
    Diperlukan untuk pengembangan Spring Boot
  </Card>

  <Card title="Kotlin" icon="window" href="cursor:extension/fwcd.kotlin">
    Diperlukan untuk pengembangan aplikasi Kotlin
  </Card>
</CardGroup>

<div id="configure-build-tools">
  ### Konfigurasi Alat Build
</div>

<div id="maven">
  #### Maven
</div>

Pastikan Maven terpasang (`mvn -version`). Instal dari [maven.apache.org](https://maven.apache.org/download.cgi) jika perlu:

1. Unduh arsip biner
2. Ekstrak ke lokasi yang diinginkan
3. Setel variabel lingkungan MAVEN\_HOME ke folder hasil ekstraksi
4. Tambahkan %MAVEN\_HOME%\bin (Windows) atau \$MAVEN\_HOME/bin (Unix) ke PATH

<div id="gradle">
  #### Gradle
</div>

Pastikan Gradle terpasang (`gradle -version`). Instal dari [gradle.org](https://gradle.org/install/) jika perlu:

1. Unduh distribusi biner
2. Ekstrak ke lokasi yang diinginkan
3. Setel variabel lingkungan GRADLE\_HOME ke folder hasil ekstraksi
4. Tambahkan %GRADLE\_HOME%\bin (Windows) atau \$GRADLE\_HOME/bin (Unix) ke PATH

Atau gunakan Gradle Wrapper yang akan otomatis mengunduh dan memakai versi Gradle yang tepat:

<div id="running-and-debugging">
  ## Menjalankan dan Debugging
</div>

Sekarang semuanya sudah siap, saatnya nge-run dan nge-debug kode Java lo.
Tergantung kebutuhan lo, lo bisa pakai cara berikut:

<CardGroup cols={2}>
  <Card title="Run" icon="play">
    Klik tautan "Run" yang muncul di atas method main mana pun buat cepat ngejalanin
    program lo
  </Card>

  <Card title="Debug" icon="bug">
    Buka panel sidebar Run and Debug dan pakai tombol Run buat mulai
    aplikasi lo
  </Card>
</CardGroup>

<CardGroup cols={1}>
  <Card title="Terminal" icon="terminal">
    Jalanin dari command line pakai perintah Maven atau Gradle
  </Card>

  <Card title="Spring Boot" icon="leaf">
    Launch aplikasi Spring Boot langsung dari ekstensi Spring Boot Dashboard
  </Card>
</CardGroup>

<div id="java-x-cursor-workflow">
  ## Alur Kerja Java x Cursor
</div>

Fitur bertenaga AI dari Cursor bisa secara signifikan ningkatin alur kerja pengembangan Java. Berikut beberapa cara buat ngegunain kemampuan Cursor khusus buat Java:

<CardGroup cols={2}>
  <Card title="Tab Completion" icon="arrow-right">
    <div className="text-sm">
      Saran cerdas buat method, signature, dan boilerplate Java kayak
      getter/setter.
    </div>
  </Card>

  <Card title="Agent Mode" icon="pen-to-square">
    <div className="text-sm">
      Nerapin design pattern, refactor kode, atau ngegenerasi class dengan
      inheritance yang bener.
    </div>
  </Card>

  <Card title="Inline Edit" icon="code">
    <div className="text-sm">
      Edit inline cepat buat method, benerin error, atau ngegenerasi unit test tanpa
      ganggu flow.
    </div>
  </Card>

  <Card title="Chat" icon="message">
    <div className="text-sm">
      Dapet bantuan soal konsep Java, debug exception, atau paham fitur
      framework.
    </div>
  </Card>
</CardGroup>

<div id="example-workflows">
  ### Contoh Alur Kerja
</div>

1. **Generate Java Boilerplate**\
   Pakai [Tab completion](/id/tab/overview) buat cepat ngegenerasi constructor, getter/setter, method equals/hashCode, dan pola Java repetitif lainnya.

2. **Debug Exception Java yang Kompleks**\
   Pas nemu stack trace Java yang susah dimengerti, highlight dan pakai [Ask](/id/chat/overview) buat jelasin akar masalah dan ngasih saran perbaikan.

3. **Refactor Kode Java Legacy**\
   Pakai [Agent mode](/id/chat/agent) buat modernisasi kode Java lama—ubah anonymous class jadi lambda, upgrade ke fitur bahasa Java yang lebih baru, atau nerapin design pattern.

4. **Pengembangan Framework**\
   Tambahin dokumentasi ke konteks Cursor dengan @docs, dan ngegenerasi kode spesifik framework langsung di Cursor.

---

← Previous: [Bekerja dengan Dokumentasi](./bekerja-dengan-dokumentasi.md) | [Index](./index.md) | Next: [JavaScript & TypeScript](./javascript-typescript.md) →