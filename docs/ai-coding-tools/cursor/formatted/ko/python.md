---
title: "Python"
source: "https://docs.cursor.com/ko/guides/languages/python"
language: "ko"
language_name: "Korean"
---

# Python
Source: https://docs.cursor.com/ko/guides/languages/python

확장과 린팅 도구로 Python 개발 환경 설정하기

<Note>
  이 가이드는 [Jack Fields](https://x.com/OrdinaryInds)의
  [아티클](https://medium.com/ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)에서 큰 영감을 받았어. Python 개발을 위한 VS Code 설정에 대한 더 자세한 내용은 해당 아티클을 참고해줘.
</Note>

<div id="prerequisites">
  ## 사전 준비 사항
</div>

시작하기 전에 다음이 준비되어 있는지 확인해:

* [Python](https://python.org) 설치(권장: 3.8 이상)
* 버전 관리를 위한 [Git](https://git-scm.com/)
* 최신 버전으로 업데이트된 Cursor

<div id="essential-extensions">
  ## 필수 확장 프로그램
</div>

다음 확장 프로그램은 Cursor를 Python 개발에 최적화된 풀 스택 기능으로 설정해 줘. 구문 하이라이팅, 린팅, 디버깅, 유닛 테스트를 제공해.

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="cursor:extension/ms-python.python">
    Microsoft의 핵심 언어 지원
  </Card>

  <Card title="Cursor Pyright" icon="bolt" href="cursor:extension/anysphere.cursorpyright">
    빠른 Python 언어 서버
  </Card>

  <Card title="Python Debugger" icon="bug" href="cursor:extension/ms-python.debugpy">
    향상된 디버깅 기능
  </Card>

  <Card title="Ruff" icon="wand-magic-sparkles" href="cursor:extension/charliermarsh.ruff">
    Python 린터 및 포매터
  </Card>
</CardGroup>

<div id="advanced-python-tooling">
  ### 고급 Python 도구
</div>

위 확장 프로그램들이 그동안 Cursor에서 Python 개발에 가장 인기 있었지만, Python 개발 효율을 최대한 끌어올릴 수 있도록 추가 확장 프로그램도 넣었어.

<div id="uv-python-environment-manager">
  #### `uv` - Python 환경 관리자
</div>

[uv](https://github.com/astral-sh/uv)는 최신 Python 패키지 관리자야. 기본 패키지 관리자인 pip을 대체할 수 있을 뿐 아니라, 가상 환경을 생성하고 관리하는 데도 쓸 수 있어.

uv를 설치하려면 터미널에서 다음 명령을 실행해:

```bash  theme={null}
pip install uv
```

<div id="ruff-python-linter-and-formatter">
  #### `ruff` - Python Linter와 Formatter
</div>

[Ruff](https://docs.astral.sh/ruff/)는 프로그래밍 오류를 검사하고, 코딩 표준 준수를 돕고, 리팩터링을 제안해 주는 최신 Python linter 겸 formatter야. 코드 포매팅엔 Black이랑 같이 써도 좋아.

Ruff를 설치하려면 터미널에서 다음 명령을 실행해:

```bash  theme={null}
pip install ruff
```

<div id="cursor-configuration">
  ## Cursor 설정
</div>

<div id="1-python-interpreter">
  ### 1. Python 인터프리터
</div>

Cursor에서 Python 인터프리터를 설정해:

1. Command Palette 열기 (Cmd/Ctrl + Shift + P)
2. "Python: Select Interpreter" 검색
3. Python 인터프리터 선택 (가상환경을 쓰고 있다면 해당 환경 선택)

<div id="2-code-formatting">
  ### 2. 코드 포매팅
</div>

Black으로 자동 코드 포매팅 설정:

<Note>
  Black은 코드를 자동으로 포매팅해 일관된 스타일을 맞춰주는
  코드 포매터야. 별도 설정이 필요 없고 Python 커뮤니티에서 널리 쓰이고 있어.
</Note>

Black을 설치하려면 터미널에서 다음 명령을 실행해:

```bash  theme={null}
pip install black
```

그다음 `settings.json` 파일에 다음을 추가해서 코드 포매팅에 Black을 쓰도록 Cursor를 설정해줘:

```json  theme={null}
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.formatting.blackArgs": ["--line-length", "88"]
}
```

<div id="3-linting">
  ### 3. 린팅
</div>

`PyLint`로 프로그래밍 오류를 검사하고, 코딩 표준을 강제하며, 리팩터링을 제안받을 수 있어.

`PyLint`를 설치하려면 터미널에서 아래 명령을 실행해:

```bash  theme={null}
pip install pylint
```

```json  theme={null}
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.lintOnSave": true
}
```

<div id="4-type-checking">
  ### 4. 타입 체크
</div>

린팅 외에도 MyPy로 타입 오류를 확인할 수 있어.

MyPy를 설치하려면 터미널에서 아래 명령을 실행해:

```bash  theme={null}
pip install mypy
```

```json  theme={null}
{
  "python.linting.mypyEnabled": true
}
```

<div id="debugging">
  ## 디버깅
</div>

Cursor는 Python용 강력한 디버깅 기능을 제공해:

1. 거터를 클릭해 브레이크포인트 설정하기
2. 디버그 패널 사용하기 (Cmd/Ctrl + Shift + D)
3. 커스텀 디버그 구성을 위해 `launch.json` 설정하기

<div id="recommended-features">
  ## 추천 기능
</div>

<CardGroup cols={3}>
  <Card title="Tab Completion" icon="wand-magic-sparkles" href="/ko/tab/overview">
    작업 흐름을 이해하는 지능형 코드 제안
  </Card>

  <Card title="Chat" icon="comments" href="/ko/chat/overview">
    자연스러운 대화로 코드를 탐색하고 이해하기
  </Card>

  <Card title="Agent" icon="robot" href="/ko/chat/agent">
    AI 도움으로 복잡한 개발 작업 처리
  </Card>

  <Card title="Context" icon="network-wired" href="/ko/context/model-context-protocol">
    서드파티 시스템의 컨텍스트 끌어오기
  </Card>

  <Card title="Auto-Imports" icon="file-import" href="/ko/tab/auto-import">
    코딩 중 모듈 자동 임포트
  </Card>

  <Card title="AI Review" icon="check-double" href="/ko/tab/overview#quality">
    Cursor가 AI로 코드를 계속 리뷰해
  </Card>
</CardGroup>

<div id="framework-support">
  ## 프레임워크 지원
</div>

Cursor는 인기 있는 Python 프레임워크와 자연스럽게 호환돼:

* **웹 프레임워크**: Django, Flask, FastAPI
* **데이터 사이언스**: Jupyter, NumPy, Pandas
* **머신러닝**: TensorFlow, PyTorch, scikit-learn
* **테스트**: pytest, unittest
* **API**: requests, aiohttp
* **데이터베이스**: SQLAlchemy, psycopg2

---

← Previous: [JavaScript & TypeScript](./javascript-typescript.md) | [Index](./index.md) | Next: [iOS & macOS (Swift)](./ios-macos-swift.md) →