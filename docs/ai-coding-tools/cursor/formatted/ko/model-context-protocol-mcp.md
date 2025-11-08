---
title: "Model Context Protocol (MCP)"
source: "https://docs.cursor.com/ko/context/mcp"
language: "ko"
language_name: "Korean"
---

# Model Context Protocol (MCP)
Source: https://docs.cursor.com/ko/context/mcp

MCP로 외부 도구와 데이터 소스를 Cursor에 연결하기

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

<div id="what-is-mcp">
  ## MCP란?
</div>

[Model Context Protocol(MCP)](https://modelcontextprotocol.io/introduction)은 Cursor가 외부 도구와 데이터 소스에 연결하도록 해준다.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/simple-mcp-call.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=08c642babc501c939ecbec9ef5124ce7" autoPlay loop muted playsInline controls data-path="images/context/mcp/simple-mcp-call.mp4" />
</Frame>

<div id="why-use-mcp">
  ### 왜 MCP를 써야 할까?
</div>

MCP는 Cursor를 외부 시스템과 데이터에 연결해. 프로젝트 구조를 매번 설명하는 대신, 네 도구랑 바로 통합하면 돼.

`stdout`에 출력하거나 HTTP 엔드포인트를 제공할 수만 있다면 어떤 언어로든 MCP 서버를 만들 수 있어 — Python, JavaScript, Go 등.

<div id="how-it-works">
  ### 작동 방식
</div>

MCP 서버는 프로토콜을 통해 기능을 제공해서 Cursor를 외부 도구나 데이터 소스와 연결해.

Cursor는 세 가지 전송 방식을 지원해:

<div className="full-width-table">
  | Transport                                                        | Execution environment | Deployment       | Users          | Input                   | Auth   |
  | :--------------------------------------------------------------- | :-------------------- | :--------------- | :------------- | :---------------------- | :----- |
  | **<span className="whitespace-nowrap">`stdio`</span>**           | Local                 | Cursor manages   | Single user    | Shell command           | Manual |
  | **<span className="whitespace-nowrap">`SSE`</span>**             | Local/Remote          | Deploy as server | Multiple users | URL to an SSE endpoint  | OAuth  |
  | **<span className="whitespace-nowrap">`Streamable HTTP`</span>** | Local/Remote          | Deploy as server | Multiple users | URL to an HTTP endpoint | OAuth  |
</div>

<div id="protocol-support">
  ### 프로토콜 지원
</div>

Cursor는 다음 MCP 프로토콜 기능을 지원해:

<div className="full-width-table">
  | Feature         | Support   | Description                      |
  | :-------------- | :-------- | :------------------------------- |
  | **Tools**       | Supported | AI 모델이 실행할 함수                    |
  | **Prompts**     | Supported | 사용자용 템플릿 메시지와 워크플로               |
  | **Resources**   | Supported | 읽고 참조할 수 있는 구조화된 데이터 소스          |
  | **Roots**       | Supported | 작업을 수행할 URI 또는 파일 시스템 경계를 서버가 조회 |
  | **Elicitation** | Supported | 사용자에게 추가 정보를 요청하는 서버 주도 요청       |
</div>

<div id="installing-mcp-servers">
  ## MCP 서버 설치
</div>

<div id="one-click-installation">
  ### 원클릭 설치
</div>

컬렉션에서 MCP 서버를 설치하고 OAuth로 인증해.

<Columns cols={2}>
  <Card title="Browse MCP Tools" icon="table" horizontal href="/ko/tools">
    사용 가능한 MCP 서버 살펴보기
  </Card>

  <Card title="Add to Cursor Button" icon="plus" horizontal href="/ko/deeplinks">
    "Add to Cursor" 버튼 만들기
  </Card>
</Columns>

<div id="using-mcpjson">
  ### `mcp.json` 사용하기
</div>

JSON 파일로 커스텀 MCP 서버를 설정해:

<CodeGroup>
  ```json CLI Server - Node.js theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "npx",
        "args": ["-y", "mcp-server"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json CLI Server - Python theme={null}
  {
    "mcpServers": {
      "server-name": {
        "command": "python",
        "args": ["mcp-server.py"],
        "env": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```

  ```json Remote Server theme={null}
  // HTTP 또는 SSE를 사용하는 MCP 서버 - 서버에서 실행
  {
    "mcpServers": {
      "server-name": {
        "url": "http://localhost:3000/mcp",
        "headers": {
          "API_KEY": "value"
        }
      }
    }
  }
  ```
</CodeGroup>

<div id="stdio-server-configuration">
  ### STDIO 서버 구성
</div>

STDIO 서버(로컬 커맨드라인 서버)의 경우, `mcp.json`에서 다음 필드를 설정해:

<div className="full-width-table">
  | Field       | Required | Description                                    | Examples                                  |
  | :---------- | :------- | :--------------------------------------------- | :---------------------------------------- |
  | **type**    | Yes      | 서버 연결 유형                                       | `"stdio"`                                 |
  | **command** | Yes      | 서버 실행 파일을 시작할 명령. 시스템 PATH에 있거나 전체 경로를 포함해야 해. | `"npx"`, `"node"`, `"python"`, `"docker"` |
  | **args**    | No       | 명령에 전달되는 인수 배열                                 | `["server.py", "--port", "3000"]`         |
  | **env**     | No       | 서버용 환경 변수                                      | `{"API_KEY": "${input:api-key}"}`         |
  | **envFile** | No       | 추가 변수를 로드할 환경 파일 경로                            | `".env"`, `"${workspaceFolder}/.env"`     |
</div>

<div id="using-the-extension-api">
  ### Extension API 사용하기
</div>

코드로 MCP 서버를 등록할 수 있도록, Cursor는 `mcp.json` 파일을 수정하지 않고도 동적으로 설정을 구성할 수 있는 확장 API를 제공해. 엔터프라이즈 환경이나 자동화된 설정 워크플로에 특히 유용해.

<Card title="MCP Extension API Reference" icon="code" href="/ko/context/mcp-extension-api">
  `vscode.cursor.mcp.registerServer()`로 코드에서 MCP 서버를 등록하는 방법 알아보기
</Card>

<div id="configuration-locations">
  ### 구성 위치
</div>

<CardGroup cols={2}>
  <Card title="프로젝트 구성" icon="folder-tree">
    프로젝트 전용 도구는 프로젝트 루트에 `.cursor/mcp.json` 만들어줘.
  </Card>

  <Card title="전역 구성" icon="globe">
    어디서나 쓰는 도구는 홈 디렉터리에 `~/.cursor/mcp.json` 만들어줘.
  </Card>
</CardGroup>

<div id="config-interpolation">
  ### 구성 보간
</div>

`mcp.json` 값에서 변수를 써. Cursor는 다음 필드의 변수를 해석해: `command`, `args`, `env`, `url`, `headers`.

지원되는 문법:

* `${env:NAME}` 환경 변수
* `${userHome}` 홈 폴더 경로
* `${workspaceFolder}` 프로젝트 루트(“.cursor/mcp.json”이 들어 있는 폴더)
* `${workspaceFolderBasename}` 프로젝트 루트 이름
* `${pathSeparator}` 및 `${/}` OS 경로 구분자

예제

```json  theme={null}
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```json  theme={null}
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

<div id="authentication">
  ### 인증
</div>

MCP 서버는 인증에 환경 변수를 사용해. API 키와 토큰은 config로 전달해.

Cursor는 OAuth가 필요한 서버를 지원해.

<div id="using-mcp-in-chat">
  ## 채팅에서 MCP 사용하기
</div>

Composer Agent는 상황에 맞으면 `Available Tools`에 표시된 MCP 도구를 자동으로 써. 특정 도구를 이름으로 지목하거나, 필요한 걸 설명해 줘. 설정에서 도구를 켜거나 끌 수 있어.

<div id="toggling-tools">
  ### 도구 토글하기
</div>

채팅 인터페이스에서 MCP 도구를 바로 켜거나 꺼. 도구 목록에서 도구 이름을 클릭하면 토글돼. 비활성화된 도구는 컨텍스트에 로드되지 않고 Agent에서도 사용할 수 없어.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-toggle.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=0fa3060f593cae3e5fb7c7d2f041a715" autoPlay loop muted playsInline controls data-path="images/context/mcp/tool-toggle.mp4" />
</Frame>

<div id="tool-approval">
  ### 도구 승인
</div>

에이전트는 기본적으로 MCP 도구를 쓰기 전에 승인을 먼저 받아. 인자를 보려면 도구 이름 옆 화살표를 클릭해.

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=bf9b19d5f23abc65914f712185b3ec72" alt="" data-og-width="1212" width="1212" data-og-height="902" height="902" data-path="images/context/mcp/tool-confirm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=e3f900fad0b8f2a469460c70fa1dd1dc 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=de2f90138de39d75d70c5800f13be93a 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b9c616ce7a4080ea4088a0fdd0050c7c 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3f783e62a7a31957b8988edb97c139f9 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10bf2c1dbfd5c2a03aa95334f53cd571 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-confirm.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=231c0e3cd60df5ad12455d5e8ef308d2 2500w" /></Frame>

<div id="auto-run">
  #### 자동 실행
</div>

Agent가 묻지 않고 MCP 도구를 쓰도록 자동 실행을 켜줘. 터미널 명령처럼 동작해. 자동 실행 설정은 [여기](/ko/agent/tools#auto-run)에서 더 알아봐.

<div id="tool-response">
  ### 도구 응답
</div>

Cursor는 인수와 응답을 펼쳐볼 수 있는 보기와 함께, 채팅에 응답을 표시해:

<Frame><img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=30af3f35869e9a78781f455bdbc0e3b5" alt="" data-og-width="1212" width="1212" data-og-height="952" height="952" data-path="images/context/mcp/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=8821ac7bad00ad54a18abc614c2e3d5c 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=d9d55f089ad53a89da99b8ddd524f6de 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=a107d68a1fb05ed43851548b34fb4496 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=b409b4941c2fd783043770fad0bd6390 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=2a331b5e2bb9be0b9659393157454c2e 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/context/mcp/tool-call.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=585b769dfa2a5114b111eb901a969845 2500w" /></Frame>

<div id="images-as-context">
  ### 컨텍스트로서의 이미지
</div>

MCP 서버는 스크린샷, 다이어그램 등 이미지를 반환할 수 있어. base64로 인코딩한 문자열로 반환해:

```js  theme={null}
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ 가독성을 위해 전체 base64는 잘렸어

server.tool("generate_image", async (params) => {
  return {
    content: [
      {
        type: "image",
        data: RED_CIRCLE_BASE64,
        mimeType: "image/jpeg",
      },
    ],
  };
});
```

구현 방식은 이 [예시 서버](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js)를 참고해. Cursor는 반환된 이미지를 채팅에 첨부해. 모델이 이미지를 지원하면 해당 이미지를 분석해.

<div id="security-considerations">
  ## 보안 고려사항
</div>

MCP 서버를 설치할 때는 다음 보안 모범 사례를 고려해봐:

* **소스 검증**: 신뢰할 수 있는 개발자와 저장소에서 제공하는 MCP 서버만 설치하기
* **권한 검토**: 서버가 어떤 데이터와 API에 접근하는지 확인하기
* **API 키 제한**: 최소 권한으로 제한된 API 키 사용하기
* **코드 검토**: 중요한 통합의 경우 서버의 소스 코드를 리뷰하기

MCP 서버는 외부 서비스에 접근하고 네 대신 코드를 실행할 수 있다는 점을 기억해. 설치 전에 서버가 무엇을 하는지 항상 정확히 이해해둬.

<div id="real-world-examples">
  ## 실제 사례
</div>

MCP가 실제로 어떻게 쓰이는지 보려면, 개발 워크플로우에 Linear, Figma, 그리고 브라우저 도구를 통합하는 방법을 보여주는 [웹 개발 가이드](/ko/guides/tutorials/web-development)를 확인해봐.

<div id="faq">
  ## 자주 묻는 질문
</div>

<AccordionGroup>
  <Accordion title="MCP 서버를 쓰는 이유가 뭐야?">
    MCP 서버는 Cursor를 Google Drive, Notion 같은 외부 도구와 서비스에 연결해서 문서와 요구사항을 네 코딩 워크플로에 바로 가져와.
  </Accordion>

  {" "}

  <Accordion title="MCP 서버 문제를 어떻게 디버그해?">
    MCP 로그를 보려면: 1. Cursor에서 Output 패널 열기 (<Kbd>Cmd+Shift+U</Kbd>) 2. 드롭다운에서 "MCP Logs" 선택 3. 연결 오류, 인증 문제, 서버 크래시 확인 로그에는 서버 초기화, 도구 호출, 오류 메시지가 표시돼.
  </Accordion>

  {" "}

  <Accordion title="MCP 서버를 잠깐 꺼둘 수 있어?">
    물론! 제거하지 않고 서버를 켜거나 끌 수 있어: 1. 설정 열기 (<Kbd>Cmd+Shift+J</Kbd>) 2. Features → Model Context Protocol로 이동 3. 원하는 서버 옆 토글을 클릭해서 활성화/비활성화 비활성화한 서버는 로드되지 않고 채팅에 나타나지 않아. 문제 해결이나 도구가 너무 많을 때 정리하는 데 유용해.
  </Accordion>

  {" "}

  <Accordion title="MCP 서버가 크래시 나거나 타임아웃되면 어떻게 돼?">
    MCP 서버가 실패하면: - Cursor가 채팅에 오류 메시지를 보여줘 - 도구 호출은 실패로 표시돼 - 작업을 다시 시도하거나 로그에서 상세 정보를 확인할 수 있어 - 다른 MCP 서버는 정상적으로 계속 동작해 Cursor는 한 서버의 실패가 다른 서버에 영향 주지 않도록 격리해.
  </Accordion>

  {" "}

  <Accordion title="MCP 서버는 어떻게 업데이트해?">
    npm 기반 서버의 경우: 1. 설정에서 서버 제거 2. npm 캐시 비우기: `npm cache clean --force` 3. 최신 버전을 받으려면 서버 다시 추가 커스텀 서버는 로컬 파일을 업데이트하고 Cursor를 재시작해.
  </Accordion>

  <Accordion title="민감한 데이터로 MCP 서버를 써도 돼?">
    가능해, 대신 보안 모범 사례를 따라야 해: - 시크릿은 환경 변수로 관리하고 하드코딩하지 마 - 민감한 서버는 `stdio` 트랜스포트로 로컬에서 실행해 - API 키 권한은 필요한 최소로 제한해 - 민감한 시스템에 연결하기 전에 서버 코드를 검토해 - 격리된 환경에서 서버를 실행하는 것도 고려해
  </Accordion>
</AccordionGroup>

---

← Previous: [파일 무시](./section.md) | [Index](./index.md) | Next: [Memories](./memories.md) →