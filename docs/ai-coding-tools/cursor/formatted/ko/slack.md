---
title: "Slack"
source: "https://docs.cursor.com/ko/integrations/slack"
language: "ko"
language_name: "Korean"
---

# Slack
Source: https://docs.cursor.com/ko/integrations/slack

Slack에서 Background Agents와 함께 작업하기

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

Cursor의 Slack 연동을 쓰면, <SlackInlineMessage message="@Cursor" />를 멘션하고 프롬프트를 적어서 [Background Agents](/ko/background-agent)로 Slack에서 바로 작업을 처리할 수 있어.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## 시작하기
</div>

<div id="installation">
  ### 설치
</div>

1. [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)로 이동

2. Slack 옆의 \_Connect\_를 클릭하거나 여기에서 [installation page](https://cursor.com/api/install-slack-app)로 이동

3. 워크스페이스에 Slack용 Cursor 앱을 설치하라는 안내가 표시돼

4. Slack에 설치한 뒤, 설정을 마무리하려고 Cursor로 돌아가게 돼

   1. GitHub 연결(아직 안 했다면)하고 기본 리포지토리 선택
   2. 사용량 기반 과금 켜기
   3. 개인정보 설정 확인

5. Slack에서 <SlackInlineMessage message="@Cursor" />를 멘션해서 Background Agents 사용 시작

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## 사용 방법
</div>

<SlackInlineMessage message="@Cursor" />를 멘션하고 프롬프트를 입력해. 대부분의 경우 이렇게 하면 충분하지만, 아래 명령어로 에이전트를 더 커스터마이즈할 수도 있어.

예를 들어, 대화 중에 바로 <SlackInlineMessage message="@Cursor fix the login bug" />처럼 멘션하거나, 특정 리포지토리를 지정하려면 <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" />처럼 구체적인 명령을 써.

<div id="commands">
  ### 명령어
</div>

최신 명령어 목록은 <SlackInlineMessage message="@Cursor help" />를 실행해서 확인해.

<div className="full-width-table">
  | Command                                                     | Description                                         |
  | :---------------------------------------------------------- | :-------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Background Agent를 시작해. 기존 에이전트가 있는 스레드에선 후속 지시를 추가해 |
  | <SlackInlineMessage message="@Cursor settings" />           | 기본값과 채널의 기본 리포지토리를 설정해                              |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | 고급 옵션 사용: `branch`, `model`, `repo`                 |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | 스레드에 새 에이전트를 강제로 생성해                                |
  | <SlackInlineMessage message="@Cursor list my agents" />     | 실행 중인 에이전트를 보여줘                                     |
</div>

<div id="options">
  #### 옵션
</div>

다음 옵션으로 Background Agent 동작을 커스터마이즈해:

<div className="full-width-table">
  | Option   | Description    | Example           |
  | :------- | :------------- | :---------------- |
  | `branch` | 기준 브랜치 지정      | `branch=main`     |
  | `model`  | AI 모델 선택       | `model=o3`        |
  | `repo`   | 대상 리포지토리 지정    | `repo=owner/repo` |
  | `autopr` | 자동 PR 생성 켜기/끄기 | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### 구문 형식
</div>

옵션은 여러 방식으로 쓸 수 있어:

1. **Bracket 형식**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Inline 형식**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### 옵션 우선순위
</div>

옵션을 조합할 때:

* **명시적 값**이 기본값보다 우선이야
* **나중 값**이 중복되면 이전 값을 덮어써
* **Inline 옵션**이 설정 모달의 기본값보다 우선이야

봇은 메시지 어디에 있든 옵션을 파싱하니까, 자연스럽게 명령을 작성해도 돼.

<div id="using-thread-context">
  #### 스레드 컨텍스트 사용
</div>

Background Agents는 기존 스레드 논의의 컨텍스트를 이해하고 활용해. 팀이 이슈를 논의했고 그 대화를 바탕으로 에이전트가 솔루션을 구현하길 원할 때 유용해.

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Background Agents는 호출되면 컨텍스트를 위해 전체 스레드를 읽고,
  팀 논의를 바탕으로 솔루션을 이해하고 구현해.
</Note>

<div id="when-to-use-force-commands">
  #### 강제 명령을 사용할 때
</div>

**언제 <SlackInlineMessage message="@Cursor agent" />가 필요해?**

기존 에이전트가 있는 스레드에선 <SlackInlineMessage message="@Cursor [prompt]" />가 후속 지시를 추가해 (네가 그 에이전트를 소유한 경우에만 작동). 별도 에이전트를 띄우려면 <SlackInlineMessage message="@Cursor agent [prompt]" />를 사용해.

**언제 `Add follow-up`이 필요해 (컨텍스트 메뉴)?**

에이전트의 응답에서 컨텍스트 메뉴(⋯)를 사용해 후속 지시를 추가해. 스레드에 여러 에이전트가 있고, 어느 에이전트에 후속 작업할지 지정해야 할 때 유용해.

<div id="status-updates-handoff">
  ### 상태 업데이트 및 핸드오프
</div>

Background Agent가 실행되면, 먼저 *Open in Cursor* 옵션이 보여.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Background Agent 작업이 완료되면 Slack에서 알림이 오고, GitHub에서 생성된 PR을 바로 볼 수 있어.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### 에이전트 관리
</div>

실행 중인 모든 에이전트를 보려면 <SlackInlineMessage message="@Cursor list my agents" />를 입력해.

에이전트 메시지의 세 점(⋯)을 클릭해서 표시되는 컨텍스트 메뉴에서 Background Agent를 관리할 수 있어.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

사용 가능한 옵션:

* **Add follow-up**: 기존 에이전트에 추가 지시사항을 넣기
* **Delete**: Background Agent 중지 및 보관
* **View request ID**: 문제 해결용 고유 요청 ID 확인(지원 문의 시 포함)
* **Give feedback**: 에이전트 성능에 대한 피드백 보내기

<div id="configuration">
  ## 구성
</div>

[Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents)에서 기본 설정과 프라이버시 옵션을 관리해.

<div id="settings">
  ### 설정
</div>

<div id="default-model">
  #### 기본 모델
</div>

<SlackInlineMessage message="@Cursor [model=...]" />로 모델을 명시하지 않았을 때 사용돼. 사용 가능한 옵션은 [settings](https://www.cursor.com/dashboard?tab=background-agents)에서 확인해.

<div id="default-repository">
  #### 기본 리포지토리
</div>

리포지토리를 지정하지 않았을 때 사용돼. 다음 형식을 사용해:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  존재하지 않는 리포지토리를 참조하면 접근 권한이 없는 것처럼 보여.
  Background Agent가 시작에 실패할 때 오류 메시지로 표시돼.
</Note>

<div id="base-branch">
  #### 기본 브랜치
</div>

Background Agent가 시작할 때 기준이 되는 브랜치야. 비워 두면 리포지토리의 기본 브랜치(보통 `main`)를 사용해.

<div id="channel-settings">
  ### 채널 설정
</div>

<SlackInlineMessage message="@Cursor settings" />로 채널 단위 기본 설정을 구성해. 이 설정은 팀 단위이며 해당 채널에서 네 개인 기본값을 덮어써.

특히 유용한 경우:

* 채널마다 다른 리포지토리에서 작업할 때
* 팀이 모든 구성원에게 일관된 설정을 원할 때
* 매번 명령에 리포지토리를 지정하지 않으려 할 때

채널 설정을 구성하려면:

1. 원하는 채널에서 <SlackInlineMessage message="@Cursor settings" />를 실행해
2. 그 채널의 기본 리포지토리를 설정해
3. 그 채널에서 Background Agents를 쓰는 모든 팀원이 이 기본값을 사용해

<Note>
  채널 설정이 개인 기본값보다 우선하지만,{" "}
  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" /> 같은 명시적 옵션으로
  덮어쓸 수 있어
</Note>

<div id="privacy">
  ### 프라이버시
</div>

Background Agents는 Privacy Mode를 지원해.

[Privacy Mode](https://www.cursor.com/privacy-overview)에 대해 더 알아보거나 [privacy settings](https://www.cursor.com/dashboard?tab=background-agents)를 관리해.

<Warning>
  Privacy Mode(레거시)는 지원되지 않아. Background Agents는 실행 중에
  임시 코드 저장이 필요해.
</Warning>

<div id="display-agent-summary">
  #### 에이전트 요약 표시
</div>

에이전트 요약과 diff 이미지를 표시해. 파일 경로나 코드 스니펫이 포함될 수 있어. On/Off로 전환할 수 있어.

<div id="display-agent-summary-in-external-channels">
  #### 외부 채널에서 에이전트 요약 표시
</div>

다른 워크스페이스와의 Slack Connect나 Guests 같은 외부 구성원이 있는 채널에서는, 외부 채널에 에이전트 요약을 표시할지 선택해.

<div id="permissions">
  ## 권한
</div>

Cursor는 Background Agents가 워크스페이스에서 작동하도록 다음 Slack 권한을 요청해:

<div className="full-width-table">
  | 권한                  | 설명                                        |
  | :------------------ | :---------------------------------------- |
  | `app_mentions:read` | @멘션을 감지해 Background Agents를 시작하고 요청에 응답   |
  | `channels:history`  | 후속 지시를 추가할 때 컨텍스트로 스레드의 이전 메시지를 읽음        |
  | `channels:join`     | 초대되거나 요청되면 공개 채널에 자동으로 참여                 |
  | `channels:read`     | 답글과 업데이트를 올리기 위해 채널 메타데이터(ID, 이름)에 접근     |
  | `chat:write`        | 에이전트 작업이 끝나면 상태 업데이트, 완료 알림, PR 링크를 전송    |
  | `files:read`        | 추가 컨텍스트를 위해 공유 파일(로그, 스크린샷, 코드 샘플)을 다운로드  |
  | `files:write`       | 빠른 리뷰를 위해 에이전트 변경 사항의 시각적 요약을 업로드         |
  | `groups:history`    | 멀티턴 대화 컨텍스트로 비공개 채널의 이전 메시지를 읽음           |
  | `groups:read`       | 응답을 올리고 대화 흐름을 유지하기 위해 비공개 채널 메타데이터에 접근   |
  | `im:history`        | 이어지는 대화의 컨텍스트로 다이렉트 메시지 기록에 접근            |
  | `im:read`           | 참가자를 식별하고 올바른 스레딩을 유지하려고 DM 메타데이터를 읽음     |
  | `im:write`          | 비공개 알림이나 1:1 커뮤니케이션을 위해 다이렉트 메시지를 시작      |
  | `mpim:history`      | 다자간 대화를 위해 그룹 DM 기록에 접근                   |
  | `mpim:read`         | 참가자를 지정하고 정확한 전달을 위해 그룹 DM 메타데이터를 읽음      |
  | `reactions:read`    | 사용자 피드백과 상태 신호를 위해 이모지 리액션을 확인            |
  | `reactions:write`   | 상태 표시용 이모지 리액션 추가 - ⏳ 실행 중, ✅ 완료, ❌ 실패    |
  | `team:read`         | 설치를 분리하고 설정을 적용하려고 워크스페이스 세부 정보를 식별       |
  | `users:read`        | 권한 부여와 보안 접근을 위해 Slack 사용자와 Cursor 계정을 매칭 |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [모델](./section.md) →