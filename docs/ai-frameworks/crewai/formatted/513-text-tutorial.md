---
title: "Crewai: Text Tutorial"
description: "Text Tutorial section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Text Tutorial


<Note>
  **Python Version Requirements**

  CrewAI requires `Python >=3.10 and <3.14`. Here's how to check your version:

  ```bash  theme={null}
  python3 --version
  ```

  If you need to update Python, visit [python.org/downloads](https://python.org/downloads)
</Note>

<Note>
  **OpenAI SDK Requirement**

  CrewAI 0.175.0 requires `openai >= 1.13.3`. If you manage dependencies yourself, ensure your environment satisfies this constraint to avoid import/runtime issues.
</Note>

CrewAI uses the `uv` as its dependency management and package handling tool. It simplifies project setup and execution, offering a seamless experience.

If you haven't installed `uv` yet, follow **step 1** to quickly get it set up on your system, else you can skip to **step 2**.

<Steps>
  <Step title="Install uv">
    * **On macOS/Linux:**

      Use `curl` to download the script and execute it with `sh`:

      ```shell  theme={null}
      curl -LsSf https://astral.sh/uv/install.sh | sh
      ```

      If your system doesn't have `curl`, you can use `wget`:

      ```shell  theme={null}
      wget -qO- https://astral.sh/uv/install.sh | sh
      ```

    * **On Windows:**

      Use `irm` to download the script and `iex` to execute it:

      ```shell  theme={null}
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
      ```

      If you run into any issues, refer to [UV's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.
  </Step>

  <Step title="Install CrewAI 🚀">
    * Run the following command to install `crewai` CLI:

      ```shell  theme={null}
      uv tool install crewai
      ```

      <Warning>
        If you encounter a `PATH` warning, run this command to update your shell:

        ```shell  theme={null}
        uv tool update-shell
        ```
      </Warning>

      <Warning>
        If you encounter the `chroma-hnswlib==0.7.6` build error (`fatal error C1083: Cannot open include file: 'float.h'`) on Windows, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) with *Desktop development with C++*.
      </Warning>

    * To verify that `crewai` is installed, run:
      ```shell  theme={null}
      uv tool list
      ```

    * You should see something like:
      ```shell  theme={null}
      crewai v0.102.0
      - crewai
      ```

    * If you need to update `crewai`, run:
      ```shell  theme={null}
      uv tool install crewai --upgrade
      ```

    <Check>Installation successful! You're ready to create your first crew! 🎉</Check>
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Video Tutorial](./512-video-tutorial.md)

**Next:** [Creating a CrewAI Project →](./514-creating-a-crewai-project.md)
