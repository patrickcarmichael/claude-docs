---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/ko/guides/languages/swift"
language: "ko"
language_name: "Korean"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/ko/guides/languages/swift

Swift 개발을 위해 Cursor를 Xcode와 통합하기

Cursor에서 Swift 개발을 시작해봐! iOS 앱, macOS 앱, 서버사이드 Swift 프로젝트까지 전부 커버해. 이 가이드는 기본부터 시작해서 고급 기능까지, Cursor에서 Swift 환경을 설정하는 방법을 안내할게.

<div id="basic-workflow">
  ## 기본 워크플로우
</div>

Swift에서 Cursor를 가장 간단하게 쓰는 방법은, 앱 빌드와 실행은 계속 Xcode에 맡기면서 Cursor를 주 코드 에디터로 사용하는 거야. 그러면 다음 같은 훌륭한 기능들을 즐길 수 있어:

* 스마트 코드 자동 완성
* AI 기반 코딩 어시스트(아무 줄에서든 [CMD+K](/ko/inline-edit/overview) 써봐)
* [@Docs](/ko/context/@-symbols/@-docs)로 문서를 빠르게 열람
* 구문 하이라이트
* 기본 코드 탐색

앱을 빌드하거나 실행해야 할 땐 Xcode로 그냥 전환하면 돼. 이 워크플로우는 Cursor의 AI 기능을 최대한 활용하면서도 디버깅과 배포는 익숙한 Xcode 도구를 그대로 쓰고 싶은 개발자에게 딱이야.

<div id="hot-reloading">
  ### 핫 리로딩
</div>

Xcode에서 폴더를 직접 여는 대신 워크스페이스나 프로젝트를 사용할 때, Xcode가 Cursor에서 변경했거나 전반적으로 Xcode 외부에서 변경된 파일을 무시하는 경우가 종종 있어.

이걸 해결하려고 폴더를 Xcode에서 열 수도 있지만, Swift 개발 워크플로우상 프로젝트를 써야 할 때가 있어.

이때 좋은 해결책은 [Inject](https://github.com/krzysztofzablocki/Inject)를 쓰는 거야. Swift용 핫 리로딩 라이브러리로, 실시간 변경이 발생하면 앱을 즉시 “핫 리로드”하고 업데이트해 줘. Xcode 워크스페이스/프로젝트 이슈의 부작용에도 영향받지 않고, Cursor에서 한 변경이 앱에 곧바로 반영돼.

<CardGroup cols={1}>
  <Card title="Inject - Swift용 핫 리로딩" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Swift 프로젝트에서 Inject를 더 알아보고 사용하는 방법을 확인해봐.
  </Card>
</CardGroup>

<div id="advanced-swift-development">
  ## 고급 Swift 개발
</div>

<Note>
  이 가이드의 이 섹션은 [Thomas
  Ricouard](https://x.com/Dimillian)와 그가 작성한
  [기사](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)에서
  큰 영감을 받았어. iOS 개발에서 Cursor를 사용하는 방법에 대한 더 자세한 내용은
  그의 글을 확인하고, Swift 관련 콘텐츠를 더 보려면 팔로우도 해줘.
</Note>

한 번에 하나의 에디터만 열어두고 Xcode와 Cursor 사이를 오가야 하는 상황을 피하고 싶다면, [Sweetpad](https://sweetpad.hyzyla.dev/) 같은 확장을 사용해서 Cursor를 Xcode의 기본 빌드 시스템과 직접 통합할 수 있어.

Sweetpad는 Xcode의 기능을 놓치지 않으면서도 Cursor에서 Swift 프로젝트를 바로 빌드, 실행, 디버깅할 수 있게 해주는 강력한 확장이야.

Sweetpad를 사용하려면 Mac에 Xcode가 설치되어 있어야 해 — Swift 개발의 기반이니까. [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835)에서 Xcode를 다운로드할 수 있어. Xcode 설정을 마쳤다면, 이제 몇 가지 필수 도구로 Cursor에서의 개발 경험을 업그레이드해 보자.

터미널을 열고 다음을 실행해:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →