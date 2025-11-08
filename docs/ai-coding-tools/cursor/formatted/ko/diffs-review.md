---
title: "Diffs & Review"
source: "https://docs.cursor.com/ko/agent/review"
language: "ko"
language_name: "Korean"
---

# Diffs & Review
Source: https://docs.cursor.com/ko/agent/review

AI 에이전트가 생성한 코드 변경 사항 검토 및 관리

Agent가 코드 변경을 만들면, 추가와 삭제를 색상으로 구분한 라인으로 보여주는 리뷰 인터페이스에서 표시돼. 이를 통해 어떤 변경을 코드베이스에 적용할지 검토하고 제어할 수 있어.

리뷰 인터페이스는 익숙한 diff 형식으로 코드 변경을 보여줘:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Type              | Meaning       | Example                                                                                               |
  | :---------------- | :------------ | :---------------------------------------------------------------------------------------------------- |
  | **Added lines**   | 새 코드 추가       | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Deleted lines** | 코드 삭제         | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Context lines** | 변경되지 않은 주변 코드 | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## 검토
</div>

생성이 끝나면, 진행하기 전에 모든 변경 사항을 확인하라는 프롬프트가 떠. 이걸로 뭐가 바뀌는지 한눈에 볼 수 있어.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="입력 검토 인터페이스" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### 파일별
</div>

화면 하단에 떠 있는 검토 바가 나타나서 이렇게 할 수 있어:

* 현재 파일의 변경 사항을 **수락**하거나 **거부**하기
* 보류 중인 변경이 있는 **다음 파일**로 이동하기
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      브라우저가 video 태그를 지원하지 않아.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### 선택적 수락
</div>

더 세밀하게 제어하려면:

* 대부분의 변경을 수락하려면: 원치 않는 줄을 거부한 뒤 **모두 수락** 클릭
* 대부분의 변경을 거부하려면: 원하는 줄을 수락한 뒤 **모두 거부** 클릭

<div id="review-changes">
  ## 변경 사항 리뷰
</div>

에이전트 응답 맨 끝에서 **변경 사항 리뷰** 버튼을 눌러 변경 내용의 전체 diff를 확인해.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [계획](./section.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →